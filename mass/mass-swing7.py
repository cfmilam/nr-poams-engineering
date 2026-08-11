#!/usr/bin/env python3
# Swing 7 — the two books, one statement. Registration: ledger 058a82c (pre-run).
# L1 K4 enumeration; L2 unconditional floor; L3 freeze value; L4 loop closure;
# L5 eta=1/2 leakage-law discrimination against swing-6 bands.
import itertools

GAM = (0.80, 0.85, 0.90)
AV, TAUB = 15.75, 20.1          # bulk plateau import + filled-ladder tax (swings 2-4)
ZC = (4.43, 4.78, 5.13)         # capacity band (swing 3)

# ---- L1: K4 enumeration over all 4^4 type labelings ----
# types: 0 Z-up, 1 Z-dn, 2 N-up, 3 N-dn. sense = t//2, orient = t%2
def bond(a, b):
    sense_eq = (a // 2) == (b // 2)
    orient_eq = (a % 2) == (b % 2)
    if not sense_eq and orient_eq:  return "S"
    if not orient_eq:               return "W"
    return "B"                       # like sense, same orientation: barred
best = {}
for g in GAM:
    mx, argmx = -1, None
    for lab in itertools.product(range(4), repeat=4):
        s = w = b = 0
        for i, j in itertools.combinations(range(4), 2):
            c = bond(lab[i], lab[j])
            if c == "S": s += 1
            elif c == "W": w += 1
            else: b += 1
        mu = (s + g * w) / 6.0
        if mu > mx: mx, argmx = mu, (lab, s, w, b)
    best[g] = (mx, argmx)
    print("L1 K4: gamma=%.2f  mu_max=%.4f  labeling=%s  (S,W,B)=%s" %
          (g, mx, argmx[0], argmx[1:]))
mu_k4 = best[0.85][0]
s85 = best[0.85][1][1:]
print("L1 registered claim mu_max = (2+4g)/6 =", (2 + 4*0.85) / 6.0,
      "-> ENUM CONFIRMS" if abs(mu_k4 - (2+4*0.85)/6.0) < 1e-12 and s85 == (2,4,0)
      else "-> ENUM CONTRADICTS")
# triangle bound
tri = {}
for g in GAM:
    mx = -1
    for lab in itertools.product(range(4), repeat=3):
        s = w = b = 0
        for i, j in itertools.combinations(range(3), 2):
            c = bond(lab[i], lab[j])
            if c == "S": s += 1
            elif c == "W": w += 1
            else: b += 1
        mx = max(mx, (s + g * w) / 3.0)
    tri[g] = mx
print("L1 triangle bound:", {g: round(v, 4) for g, v in tri.items()},
      " (registered (2+g)/3 =", round((2 + 0.85) / 3, 4), ")")

# ---- L2/L3: books ----
print("\nL2/L3: dbar = 2(a_v+tau_b)/z_c")
C = AV + TAUB
vals = {}
for zc in ZC:
    vals[zc] = 2 * C / zc
print("dbar central %.2f  band [%.2f, %.2f]" % (vals[4.78], vals[5.13], vals[4.43]))
floor_weak = vals[5.13] / tri[0.90]        # most permissive: triangle bound, low dbar
floor_tetra = vals[5.13] / mu_k4
print("L2 unconditional floor: delta0(z_c) >= %.2f (triangle) / %.2f (tetrahedral)"
      % (floor_weak, floor_tetra), " vs free-pair 14.31")
froz = {}
for g in GAM:
    mu = (1 + 2 * g) / 4.0
    froz[g] = [2 * C / zc / mu for zc in ZC]
central = froz[0.85][1]
lo = min(min(v) for v in froz.values()); hi = max(max(v) for v in froz.values())
print("L3 frozen value: delta0(z_c) = %.2f  band [%.2f, %.2f]" % (central, lo, hi))

# ---- L4: loop closure vs ladder linear extrapolation ----
# swing-6 ladder (central): z=1: 14.31; z=2: mean(14.07,16.81)=15.44; z=3: 17.70
import statistics
zs = [1, 2, 3]; d0 = [14.31, (14.07 + 16.81) / 2, 17.70]
n = len(zs)
mz = statistics.mean(zs); md = statistics.mean(d0)
slope = sum((a - mz) * (b - md) for a, b in zip(zs, d0)) / sum((a - mz) ** 2 for a in zs)
icept = md - slope * mz
ext = icept + slope * 4.78
print("\nL4: ladder linear fit delta0(z) = %.2f + %.2f (z-1); extrapolation at z_c=4.78: %.2f"
      % (icept + slope, slope, ext))
print("L4 loop closure: %.2f in [%.2f, %.2f]?" % (ext, lo, hi),
      "PASS" if lo <= ext <= hi else "FAIL")

# ---- L5: eta = 1/2 free-arc leakage law vs swing-6 bands ----
print("\nL5: delta(z) = delta0(zc)*(1 - f/2), f = 1 - z/z_c   [delta0(zc)=%.2f central]" % central)
bands = {"d": (1, 14.12, 14.49), "h": (2, 13.17, 15.07),
         "t": (2, 14.84, 18.39), "alpha": (3, 16.63, 18.42)}
fails = []
for lab, (z, blo, bhi) in bands.items():
    f = 1 - z / 4.78
    pred = central * (1 - f / 2)
    ok = blo <= pred <= bhi
    if not ok: fails.append(lab)
    print("  %-6s z=%d  pred %.2f  band [%.2f, %.2f]  %s"
          % (lab, z, pred, blo, bhi, "inside" if ok else "OUTSIDE"))
print("L5 registered: form predicted to FAIL at d (and h). Failures:", fails,
      "-> REJECTED as registered" if "d" in fails else "-> registration wrong, form survives d")
