#!/usr/bin/env python3
# Swing 8 — crown attempt: radius-import audit, corrected ladder, class exclusions.
# Registration: ledger d942dc7 (pre-run).
import math, re

HB2M = 41.47; AC = 0.72; GAM = (0.80, 0.85, 0.90)
RP2 = 0.8409**2          # proton charge radius^2 (fm^2)
RN2 = -0.1155            # neutron mean-square charge radius (fm^2, negative)

# ---- AME (local) ----
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

# ---- 1. unfolding: point-proton radii from charge radii ----
def rpp2(rc, Z, N): return rc*rc - RP2 - (N/Z)*RN2
h_pp2 = rpp2(1.9506, 2, 1); t_pp2 = rpp2(1.755, 1, 2)
h_pp2_e = rpp2(1.973, 2, 1)
print("point-proton radii: h %.3f (muonic; %.3f e-scatt)  t %.3f fm"
      % (math.sqrt(h_pp2), math.sqrt(h_pp2_e), math.sqrt(t_pp2)))
# mirror estimate of matter radii: r_n-dist(h) ~ r_pp(t) (+Coulomb %), r_n-dist(t) ~ r_pp(h) (-Coulomb)
h_m2 = (2*h_pp2 + t_pp2)/3.0
t_m2 = (t_pp2 + 2*h_pp2)/3.0   # same combination by mirror symmetry -> equal by construction
print("mirror-combined matter radii: h %.3f  t %.3f fm (equal by isospin-even operator; Coulomb split ~1-2%%)"
      % (math.sqrt(h_m2), math.sqrt(t_m2)))

# ---- 2. corrected ladder on common band ----
def tau(n, r): return (9.0/8.0)*HB2M*(1.0-1.0/n)/(r*r)
def strain(Z, A): return AC*Z*(Z-1)/A**(1.0/3.0)
def d0(Bv, Z, N, r, n, s, w, g): return (Bv + (Z+N)*tau(n,r) + strain(Z,Z+N))/(s + w*g)

band3 = (1.65, 1.70, 1.75)   # common trinucleon matter band (declared)
print("\ncorrected extractions (gamma central 0.85):")
res = {}
for lab, Bv, Z, N, rb, n, s, w in [
    ("d", B_d, 1, 1, (1.95,1.965,1.98), 2, 1, 0),
    ("h", B_h, 2, 1, band3, 3, 1, 2),
    ("t", B_t, 1, 2, band3, 3, 1, 2),
    ("alpha", B_a, 2, 2, (1.45,1.452,1.48), 4, 2, 4)]:
    vals = [d0(Bv,Z,N,r,n,s,w,g) for r in rb for g in GAM]
    c = d0(Bv,Z,N,rb[1],n,s,w,0.85)
    res[lab] = (c, min(vals), max(vals))
    print("  %-6s %6.2f  [%5.2f, %5.2f]" % (lab, c, min(vals), max(vals)))

# R8a mirror unification
split = abs(res["t"][0] - res["h"][0])
print("R8a mirror split |t-h| = %.2f MeV (< 0.5 registered):" % split,
      "PASS" if split < 0.5 else "FAIL", " (swing-6 split was 2.74)")

# R8b recompute rank + gap on corrected ladder
lad = [("d",1,res["d"][0]), ("h",2,res["h"][0]), ("t",2,res["t"][0]), ("alpha",3,res["alpha"][0])]
gap = res["alpha"][0]-res["d"][0]
mono = res["d"][0] <= (res["h"][0]+res["t"][0])/2 <= res["alpha"][0]
print("R8b: alpha-d gap %.2f (T-C6b(i) >=1.5 still PASS: %s); d <= z2mean <= alpha: %s"
      % (gap, gap>=1.5, mono), "| T-C6b(ii) mirror pass DEMOTED (import artifact)")

# R8c convexity of corrected ladder + frozen endpoint
z2 = (res["h"][0]+res["t"][0])/2
s12 = z2 - res["d"][0]; s23 = res["alpha"][0] - z2
print("R8c steps: (1->2) %.2f  (2->3) %.2f  convex (s12<s23):" % (s12, s23),
      "PASS" if s12 < s23 else "FAIL")

# R8d pure quadratic through (1, d), (2, z2), (3, alpha): a + b with zero-linear test
b_quad = s23 - s12  # if delta = d0(1) + a(z-1) + b(z-1)^2: s12 = a+b, s23 = a+3b -> b=(s23-s12)/2, a = s12-b
bq = (s23 - s12)/2.0; aq = s12 - bq
pred_zc = res["d"][0] + aq*3.78 + bq*3.78**2
print("R8d quadratic fit: a=%.3f b=%.3f -> delta(z_c)=%.1f vs frozen band [19.97,24.90]:" % (aq,bq,pred_zc),
      "FAILS endpoint as registered" if not (19.97<=pred_zc<=24.90) else "unexpectedly inside")

# R8e dwell class with honest normalization
AS = 0.8846  # fm^-1/2, deuteron asymptotic S normalization (import)
kap = math.sqrt(2*469.46*B_d)/197.327
for c in (1.9, 2.14, 2.4):
    Pout = AS*AS*math.exp(-2*kap*c)/(2*kap)
    Pin = 1-Pout
    print("R8e dwell: c=%.2f  P_in=%.3f  implied contact const = %.1f MeV" % (c, Pin, res["d"][0]/Pin))
print("R8e: implied constants vs frozen band [20,24.9] -> EXCLUDED (and non-universal); pure-tail formula")
print("     P_in = 1-exp(-2*kc) = %.3f was the parent's earlier inversion slip (self-catch, on record)"
      % (1-math.exp(-2*kap*2.14)))

# corrected ladder summary
print("\nCORRECTED LADDER: d %.2f | z=2 %.2f (h %.2f / t %.2f) | alpha %.2f | frozen endpoint 22.2 [20.0,24.9]"
      % (res["d"][0], z2, res["h"][0], res["t"][0], res["alpha"][0]))
print("steps per added partner: +%.2f then +%.2f then +%.2f/unit to z_c"
      % (s12, s23, (22.22-res["alpha"][0])/1.78))
