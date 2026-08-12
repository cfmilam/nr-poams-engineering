#!/usr/bin/env python3
# Swing 24 — split-residual audit: radius chains + honest gamma propagation.
# Registration: 77fa487 (pre-run). Swing-8 extraction machinery, two chains.
import math, re, itertools

HB2M = 41.47; AC = 0.72
RP2 = 0.8409**2
RN2 = -0.1155
GAMS = (0.80, 0.85, 0.90)

BA = {}
for ln in open("data/mass.mas20.txt", encoding="ascii", errors="replace"):
    if len(ln) < 70: continue
    try: N=int(ln[4:9]); Z=int(ln[9:14]); A=int(ln[14:19])
    except ValueError: continue
    if A != N+Z: continue
    fld = ln[54:68]
    if "#" in fld: continue
    m = re.search(r"[-\d.]+", fld)
    if not m: continue
    BA[(Z,N)] = float(m.group())
def B(Z,N): return BA[(Z,N)]*(Z+N)/1000.0
B_d, B_t, B_h, B_a = B(1,1), B(1,2), B(2,1), B(2,2)

def tau(n, r2): return (9.0/8.0)*HB2M*(1.0-1.0/n)/r2
def strain(Z, A): return AC*Z*(Z-1)/A**(1.0/3.0)
def d0(Bv, Z, N, r2, n, s, w, g):
    return (Bv + (Z+N)*tau(n,r2) + strain(Z,Z+N))/(s + w*g)

# ---------- Chain A: charge-unfolded, muonic era ----------
rch = {"d": (2.12799, 0.00074), "h": (1.9661, 0.0030),
       "t": (1.7591, 0.0363), "a": (1.67824, 0.00083)}
def pp2(rc, Z, N): return rc*rc - RP2 - (N/Z)*RN2
def pp2_band(lab, Z, N):
    rc, drc = rch[lab]
    return [pp2(rc+k*drc, Z, N) for k in (-1, 0, 1)]

d_pp2 = pp2_band("d", 1, 1)
h_pp2 = pp2_band("h", 2, 1)
t_pp2 = pp2_band("t", 1, 2)
a_pp2 = pp2_band("a", 2, 2)
# mirror-matter for trinucleons: (2 h_pp2 + t_pp2)/3, band = corner span
tri_m2 = sorted((2*h + t)/3.0 for h, t in itertools.product(h_pp2, t_pp2))
tri_m2_band = (tri_m2[0], (2*h_pp2[1]+t_pp2[1])/3.0, tri_m2[-1])

print("SWING 24 — radius chains + gamma propagation")
print("Chain A radii (fm): d %.4f | tri matter %.4f | alpha %.4f"
      % (math.sqrt(d_pp2[1]), math.sqrt(tri_m2_band[1]), math.sqrt(a_pp2[1])))

# S24a: vs swing-8 booked bands
booked = {"d": (1.95, 1.98), "tri": (1.65, 1.75), "a": (1.45, 1.48)}
chainA_r = {"d": math.sqrt(d_pp2[1]), "tri": math.sqrt(tri_m2_band[1]), "a": math.sqrt(a_pp2[1])}
print("\nS24a chain-A vs swing-8 booked bands:")
for k in ("d", "tri", "a"):
    lo, hi = booked[k]
    r = chainA_r[k]
    verdict = "IN" if lo <= r <= hi else ("OUT high" if r > hi else "OUT low")
    print("  %-4s %.4f vs [%.2f, %.2f] -> %s" % (k, r, lo, hi, verdict))

# ---------- extraction under a chain ----------
def ladder(chain):
    """chain: dict lab -> list of r^2 values (band). Returns dict lab -> (central, lo, hi)
    with FULL gamma propagation."""
    out = {}
    specs = [("d", B_d, 1, 1, chain["d"], 2, 1, 0),
             ("h", B_h, 2, 1, chain["tri"], 3, 1, 2),
             ("t", B_t, 1, 2, chain["tri"], 3, 1, 2),
             ("a", B_a, 2, 2, chain["a"], 4, 2, 4)]
    for lab, Bv, Z, N, r2b, n, s, w in specs:
        vals = [d0(Bv, Z, N, r2, n, s, w, g) for r2 in r2b for g in GAMS]
        c = d0(Bv, Z, N, r2b[1], n, s, w, 0.85)
        out[lab] = (c, min(vals), max(vals))
    return out

chainA = {"d": d_pp2, "tri": list(tri_m2_band), "a": a_pp2}
chainC = {"d": [1.95**2, 1.965**2, 1.98**2],
          "tri": [1.65**2, 1.70**2, 1.75**2],
          "a": [1.45**2, 1.452**2, 1.48**2]}

for name, ch in (("C (booked swing-8)", chainC), ("A (muonic charge-unfolded)", chainA)):
    res = ladder(ch)
    z2c = (res["h"][0] + res["t"][0])/2.0
    z2lo = (res["h"][1] + res["t"][1])/2.0
    z2hi = (res["h"][2] + res["t"][2])/2.0
    s1c = z2c - res["d"][0]; s1lo = z2lo - res["d"][2]; s1hi = z2hi - res["d"][1]
    s2c = res["a"][0] - z2c; s2lo = res["a"][1] - z2hi; s2hi = res["a"][2] - z2lo
    # gamma-correlated second step: evaluate at common gamma
    s2corr = []
    for g in GAMS:
        for r2t in ch["tri"]:
            for r2a in ch["a"]:
                za = d0(B_a, 2, 2, r2a, 4, 2, 4, g)
                zt = (d0(B_h, 2, 1, r2t, 3, 1, 2, g) + d0(B_t, 1, 2, r2t, 3, 1, 2, g))/2
                s2corr.append(za - zt)
    s1corr = []
    for g in GAMS:
        for r2t in ch["tri"]:
            for r2d in ch["d"]:
                zt = (d0(B_h, 2, 1, r2t, 3, 1, 2, g) + d0(B_t, 1, 2, r2t, 3, 1, 2, g))/2
                s1corr.append(zt - d0(B_d, 1, 1, r2d, 2, 1, 0, 0.85))
    c3 = HB2M*0.75/(18*0.86*0.86)
    print("\nCHAIN %s:" % name)
    print("  ladder: d %.2f [%.2f,%.2f] | z2 %.2f [%.2f,%.2f] | alpha %.2f [%.2f,%.2f] | split %.2f"
          % (res["d"][0], res["d"][1], res["d"][2], z2c, z2lo, z2hi,
             res["a"][0], res["a"][1], res["a"][2], abs(res["h"][0]-res["t"][0])))
    print("  step1 (h-target): %.2f [%.2f, %.2f]  -> s = %.3f [%.3f, %.3f]"
          % (s1c, min(s1corr), max(s1corr), s1c/c3, min(s1corr)/c3, max(s1corr)/c3))
    print("  step2 (c3-target, gamma-correlated): %.2f [%.2f, %.2f]"
          % (s2c, min(s2corr), max(s2corr)))
    print("  c3 derived 2.336 vs step2: %+.1f%% | h derived 0.978/0.946 vs step1: %+.0f%% / %+.0f%%"
          % (100*(2.336-s2c)/s2c, 100*(0.978-s1c)/s1c, 100*(0.946-s1c)/s1c))
    print("  s-window check: derived s 0.4184 (energy z_c) in band: %s | 0.4049 (chain z_c): %s"
          % (min(s1corr)/c3 <= 0.4184 <= max(s1corr)/c3,
             min(s1corr)/c3 <= 0.4049 <= max(s1corr)/c3))

print("\nS24c pair anchor (chain A): d0(d) = %.3f [%.3f, %.3f] vs derived delta_pair = 14.018 (%+.2f%%) — FLAGGED UNCLAIMED"
      % (ladder(chainA)["d"][0], ladder(chainA)["d"][1], ladder(chainA)["d"][2],
         100*(14.018-ladder(chainA)["d"][0])/ladder(chainA)["d"][0]))
print("S24 verdicts: gamma dominates step1 bands; step2 gamma-robust — see gates in ledger.")
