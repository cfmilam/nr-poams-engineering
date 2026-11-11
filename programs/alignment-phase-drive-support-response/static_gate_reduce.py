#!/usr/bin/env python3
"""static_gate_reduce.py — preregistered reduction for the YIG static gate.
Implements STATIC-GATE-PREREG.md sections 6-7 and nothing else.
Reviewer-verbatim numbers GOVERN reporting; formula uses the receipt's exact
geometry so the cross-check reproduces them exactly (re-check item 3).
"""
import argparse, csv, json, math, sys
from statistics import mean, stdev

# --- Locked constants (provenance: STATIC-GATE-PREREG.md section 9 + re-check item 3) ---
W_MG            = 2707.0056698432051738086443819258383185498942991282  # receipt-exact (1000*5.17*pi/6)
INCR_MG         = 0.01
D_THRESH_MG     = 0.04          # raw N-S threshold, mg (Convention A)
C_THRESH        = 0.02 / W_MG   # half-contrast threshold
GRAD_LIMIT      = 1.0           # uT/m (axial component along bias axis)
CTRL_LIMIT_MG   = 0.02          # dummy/empty zero-criterion; remount consistency band
MIN_CTRL_PAIRS  = 3
K0_J            = 24437249.848418309006512168499783362205747730377583   # receipt-exact
GAMMA           = 1.0034734147481825853397496237992791448191139223730   # receipt-exact
G_HI_EXACT      = 0.7454518768075703   # receipt-exact geometry (display 0.75)
G_LO_EXACT      = 0.4797876129279153   # receipt-exact geometry (display 0.48)
KS_VERBATIM     = (482.7226, 750.0121)
EXCL_VERBATIM   = (23.2436, 36.1139)
TOGGLE_CEIL_10  = 1.1224e-7
Z95             = 1.96
RUN_TYPES       = {"main", "dummy", "empty", "remount", "ew_null"}
BIAS_OK         = {"main": {"N","S"}, "dummy": {"N","S"}, "empty": {"N","S"},
                   "remount": {"N","S"}, "ew_null": {"E","W"}}

def die(msg):
    print(json.dumps({"error": msg}), file=sys.stderr); sys.exit(2)

def ks_equiv(C, g):
    return 2.0 * K0_J * C / (GAMMA * g)

def paired(rows, a, b):
    seq = [(r["bias_state"], float(r["reading_mg"])) for r in rows]
    diffs, orients, i = [], set(), 0
    while i + 1 < len(seq):
        s1, v1 = seq[i]; s2, v2 = seq[i+1]
        if s1 == a and s2 == b: diffs.append(v1 - v2); orients.add("ab"); i += 2
        elif s1 == b and s2 == a: diffs.append(v2 - v1); orients.add("ba"); i += 2
        else: i += 1
    return diffs, orients

def est(diffs):
    n = len(diffs)
    if n == 0: return None
    D = mean(diffs)
    sd = stdev(diffs)/math.sqrt(n) if n > 1 else float("inf")
    return {"n_pairs": n, "D_mg": D, "sigma_D_mg": sd,
            "ci95_lo": D - Z95*sd, "ci95_hi": D + Z95*sd}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv_path")
    ap.add_argument("--gradient-pre", type=float, required=True)
    ap.add_argument("--gradient-post", type=float, required=True)
    args = ap.parse_args()
    rows = []
    with open(args.csv_path) as f:
        for ln, r in enumerate(csv.DictReader(f), start=2):
            rt, bs = r.get("run_type",""), r.get("bias_state","")
            if rt not in RUN_TYPES: die(f"line {ln}: unknown run_type '{rt}'")
            if bs not in BIAS_OK[rt]: die(f"line {ln}: bias_state '{bs}' invalid for run_type '{rt}'")
            try: float(r["reading_mg"])
            except Exception: die(f"line {ln}: reading_mg not a number")
            rows.append(r)
    by = {}
    for r in rows: by.setdefault(r["run_type"], []).append(r)

    out = {"inputs": {"csv": args.csv_path, "rows": len(rows),
                      "gradient_pre_uT_m": args.gradient_pre,
                      "gradient_post_uT_m": args.gradient_post},
           "constants": {"W_mg": W_MG, "D_thresh_mg": D_THRESH_MG, "C_thresh": C_THRESH,
                         "convention": "A (half-contrast)",
                         "g_geo_exact": [G_HI_EXACT, G_LO_EXACT]}}

    gate0 = []
    if max(args.gradient_pre, args.gradient_post) > GRAD_LIMIT:
        gate0.append("gradient survey (axial component) > 1 uT/m")

    # Required controls: all four present with >= MIN_CTRL_PAIRS pairs
    ests = {}
    for ct in ("dummy", "empty", "remount", "ew_null"):
        a, b = ("E","W") if ct == "ew_null" else ("N","S")
        diffs, _ = paired(by.get(ct, []), a, b)
        e = est(diffs); ests[ct] = e
        if not e or e["n_pairs"] < MIN_CTRL_PAIRS:
            gate0.append(f"control '{ct}' missing or under {MIN_CTRL_PAIRS} pairs")
    out["controls"] = ests

    # Step-0 required-N rule (from dummy repeatability)
    n_req = None
    if ests.get("dummy") and ests["dummy"]["n_pairs"] >= 2:
        sigma_single = (ests["dummy"]["sigma_D_mg"] * math.sqrt(ests["dummy"]["n_pairs"])) / math.sqrt(2)
        sigma_d = math.sqrt(2) * sigma_single
        n_req = max(1, math.ceil((Z95 * sigma_d / (D_THRESH_MG/2.0))**2))
    out["step0"] = {"n_pairs_required": n_req}

    main_diffs, orients = paired(by.get("main", []), "N", "S")
    m = est(main_diffs)
    out["main"] = m
    abba_ok = orients == {"ab", "ba"}
    if m:
        out["main"]["C_static"] = m["D_mg"] / (2.0 * W_MG)
        out["main"]["resolved"] = (Z95 * m["sigma_D_mg"]) <= (D_THRESH_MG/2.0)
        out["main"]["abba_both_orientations"] = abba_ok

    # Zero-criterion controls (no sphere-field coupling)
    dirty = []
    for ct in ("dummy", "empty"):
        e = ests.get(ct)
        if e and abs(e["D_mg"]) >= CTRL_LIMIT_MG: dirty.append(f"{ct} reads nonzero (|D|>={CTRL_LIMIT_MG} mg)")
    ew = ests.get("ew_null")
    if ew and abs(ew["D_mg"]) >= CTRL_LIMIT_MG:
        dirty.append(f"east-west null reads nonzero (|D|>={CTRL_LIMIT_MG} mg)")
    gate0.extend(dirty)

    # Remount: consistency with main (a true contrast REPRODUCES after remount)
    remount_note = None
    if ests.get("remount") and m:
        delta = abs(ests["remount"]["D_mg"] - m["D_mg"])
        out["remount_consistency_mg"] = delta
        if delta >= CTRL_LIMIT_MG:
            remount_note = f"remount disagrees with main by {delta:.4f} mg (seating artifact)"

    if gate0:
        verdict, why = "GATE0_FAIL", gate0
    elif not m:
        verdict, why = "AMBIGUOUS", ["no main-run pairs"]
    elif not abba_ok:
        verdict, why = "AMBIGUOUS", ["main ordering lacks ABBA (both pair orientations); linear drift uncancelled"]
    elif remount_note:
        verdict, why = "AMBIGUOUS", [remount_note, "disposition: re-seat and repeat remount block"]
    else:
        absD = abs(m["D_mg"]); hi = absD + Z95*m["sigma_D_mg"]; lo = absD - Z95*m["sigma_D_mg"]
        if hi < D_THRESH_MG and m["resolved"] and n_req is not None and m["n_pairs"] >= n_req:
            verdict, why = "NULL", [f"|D| CI upper {hi:.4f} mg < {D_THRESH_MG} mg; n_pairs {m['n_pairs']} >= required {n_req}"]
        elif lo >= D_THRESH_MG:
            verdict, why = "CONTRAST", [f"CI lower {lo:.4f} mg >= {D_THRESH_MG} mg; remount consistent"]
        else:
            reasons = ["CI straddles threshold or unresolved"]
            if n_req is None: reasons.append("step0 repeatability missing: NULL unavailable")
            elif m["n_pairs"] < n_req: reasons.append(f"n_pairs {m['n_pairs']} < required {n_req}: NULL unavailable")
            reasons.append("disposition: re-survey gradient, increase N per step0, or stop")
            verdict, why = "AMBIGUOUS", reasons
    out["verdict"] = verdict
    out["verdict_basis"] = why

    if verdict == "NULL":
        out["consequence"] = {
            "K_s_upper_bound_J_verbatim": {"g_geo_0.75": KS_VERBATIM[0], "g_geo_0.48": KS_VERBATIM[1]},
            "K_s_upper_bound_J_formula_exact_geometry": {"g_hi": round(ks_equiv(C_THRESH, G_HI_EXACT), 10),
                                                         "g_lo": round(ks_equiv(C_THRESH, G_LO_EXACT), 10)},
            "refused_price_excluded_x_verbatim": EXCL_VERBATIM,
            "toggle_ceiling_10deg_verbatim": TOGGLE_CEIL_10,
            "note": "A null is a successful measurement that fixes an UPPER bound."}
    elif verdict == "CONTRAST":
        C = out["main"]["C_static"]
        out["consequence"] = {
            "conditional_effective_support_coefficient_Ks_equivalent_J":
                {"g_hi_exact": ks_equiv(abs(C), G_HI_EXACT), "g_lo_exact": ks_equiv(abs(C), G_LO_EXACT)},
            "note": ("Static directed-order candidate only (protocol Gate 1, reviewer F1): "
                     "NOT independently measured K_s or twist; NOT an independent spin-energy "
                     "receipt; NOT validation of any larger claim.")}
    print(json.dumps(out, indent=1))
    return 0

if __name__ == "__main__":
    sys.exit(main())
