#!/usr/bin/env python3
# Swing 22 — lambda closure: tail discriminator + weight correction.
# Registration: 94e5848 (pre-run). Booked functional (swing 4):
# Delta(u) = tau_b u^{2/3} - (a_v+tau_b) u + a_v; J = int sqrt(Delta) = 2.992;
# stiffness lambda(u) (hbar^2/8m) rho0 / u; per-volume excess rho0 u Delta.
import numpy as np

TAUB, AV = 20.1, 15.75
C = TAUB + AV
HB2_8M = 41.47/8.0     # 5.184 MeV fm^2
HB2_2M = 41.47/2.0
R0 = 1.2
AS_WIN = (16.8, 18.8)
ELL_WIN = (0.49, 0.61)

u = np.linspace(1e-12, 1.0, 800001)
Delta = TAUB*u**(2.0/3.0) - C*u + AV
Delta = np.clip(Delta, 0.0, None)
sqrtD = np.sqrt(Delta)
J = np.trapezoid(sqrtD, u)
a_s_of = lambda lam_eff: (3.0/R0)*np.sqrt(lam_eff*HB2_2M)*J

print("SWING 22 — lambda closure under the booked functional")
print("S22a CALIBRATION: J = %.4f (booked 2.992) | a_s(1) = %.2f | a_s(1/9) = %.2f:"
      % (J, a_s_of(1.0), a_s_of(1.0/9.0)),
      "PASS" if abs(J-2.992) < 0.02 else "FAIL")

def lam_eff_profile(lam_u):
    I1 = np.trapezoid(np.sqrt(lam_u*Delta), u)
    return (I1/J)**2

# candidates
lam_lin  = 1.0/(1.0 + 8.0*u)            # m = 1+8u
lam_thr  = 1.0/np.maximum(1.0, 9.0*u)   # m = max(1,9u)
cands = {
    "L3 constant 1/4":       dict(lam_eff=0.25,                    ell=0.574*np.sqrt(0.25)),
    "L4 linear m=1+8u":      dict(lam_eff=lam_eff_profile(lam_lin), ell=0.574*1.0),
    "L4t threshold m=max(1,9u)": dict(lam_eff=lam_eff_profile(lam_thr), ell=0.574*1.0),
}
# exact tail length from the functional: ell = sqrt(lam_tail*HB2_8M/AV)
ell_lone = np.sqrt(HB2_8M/AV)
print("exact lone tail length = %.4f fm (0.574 hand)" % ell_lone)
for k in cands:
    lt = 0.25 if k.startswith("L3") else 1.0
    cands[k]["ell"] = float(np.sqrt(lt*HB2_8M/AV))

print("\nCANDIDATES:")
rows = {}
for name, c in cands.items():
    a = a_s_of(c["lam_eff"])
    ok_ell = ELL_WIN[0] <= c["ell"] <= ELL_WIN[1]
    ok_as = AS_WIN[0] <= a <= AS_WIN[1]
    rows[name] = (c["lam_eff"], a, c["ell"], ok_ell, ok_as)
    print("  %-26s lam_eff=%.4f  a_s=%.2f (%s)  tail=%.3f fm (%s)"
          % (name, c["lam_eff"], a, "IN" if ok_as else "OUT",
             c["ell"], "IN" if ok_ell else "OUT"))

print("\nS22b TAIL KILL (window %.2f-%.2f fm):" % ELL_WIN)
for name, r in rows.items():
    print("  %-26s tail %.3f -> %s" % (name, r[2], "SURVIVES" if r[3] else "DEAD"))
print("S22c m-FORM KILL (a_s window %.1f-%.1f):" % AS_WIN)
for name, r in rows.items():
    print("  %-26s a_s %.2f -> %s" % (name, r[1], "SURVIVES" if r[4] else "DEAD"))

joint = [n for n, r in rows.items() if r[3] and r[4]]
print("\nS22d CLOSURE: joint survivors:", ", ".join(joint) if joint else "NONE")
if len(joint) == 1:
    n = joint[0]; r = rows[n]
    print("  ==> LAMBDA CLOSED (measured-selection grade): %s" % n)
    print("      lambda(u) = 1/(1+8u); lambda_eff = %.4f; a_s = %.2f MeV (%+.1f%% vs shadow 17.8)"
          % (r[0], r[1], 100*(r[1]-17.8)/17.8))
    print("      tail prediction %.3f fm vs measured 0.55±0.06 (%+.1f%% of central)"
          % (r[2], 100*(r[2]-0.55)/0.55))
elif len(joint) == 0:
    print("  ==> NO CLOSURE — booked miss; lambda stays open")
else:
    print("  ==> MULTIPLE SURVIVORS — fork stays open, booked")

# corrections + diagnostics for the record
print("\nRECORD:")
print("  swing-21 Lambda4 rescore under booked sqrt-Delta weight: %.4f (was 0.2641 under sqrt-g — corrected)"
      % rows["L4 linear m=1+8u"][0])
print("  uniform-measure aside ln9/8 = %.4f (not the E-L value)" % (np.log(9.0)/8.0))
# profile widths for the record (10-90 of u, absolute fm) per surviving lambda(u)
def width_10_90(lam_u_fn, lam_const=None):
    uu = np.linspace(0.1, 0.9, 200001)
    D = np.clip(TAUB*uu**(2.0/3.0) - C*uu + AV, 1e-12, None)
    lam = lam_const if lam_const is not None else lam_u_fn(uu)
    integ = np.sqrt(lam*HB2_8M)/(uu*np.sqrt(D))
    return np.trapezoid(integ, uu)
print("  10-90 core width (u=0.9 to 0.1, absolute): L4 %.2f fm | L3 %.2f fm  (tail adds ~2.3*ell)"
      % (width_10_90(lambda x: 1.0/(1.0+8.0*x)), width_10_90(None, 0.25)))
print("  skewness signature (report): inner shoulder width prop sqrt(1/9), outer tail 0.574 — fat-tail/sharp-shoulder profile named")
