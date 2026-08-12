#!/usr/bin/env python3
# Swing 21 — lambda skin: amplitude-count fork. Registration: 2d6fb86 (pre-run).
# Skin integral (swing 4): a_s = (3/r0) sqrt(lambda hbar^2/2m) J, J = 2.992;
# double-tangent excess g(u) = u^{2/3} - u; profile-weighted effective lambda.
import numpy as np

HB2M_HALF = 41.47/2.0     # hbar^2/2m = 20.735 MeV fm^2
R0 = 1.2
J_BOOKED = 2.992
AS_SHADOW, AS_BAND = 17.8, 1.0
LAM_WIN = ((AS_SHADOW-AS_BAND)/34.1)**2, ((AS_SHADOW+AS_BAND)/34.1)**2

u = np.linspace(1e-9, 1.0, 400001)
g = u**(2.0/3.0) - u
g = np.clip(g, 0.0, None)
sqrt_g = np.sqrt(g)
I0 = np.trapezoid(sqrt_g, u)

def a_s(lam_scalar):
    return (3.0/R0)*np.sqrt(lam_scalar*HB2M_HALF)*J_BOOKED

def lam_eff_profile(lam_u):
    I1 = np.trapezoid(np.sqrt(lam_u*g), u)
    return (I1/I0)**2

print("SWING 21 — lambda skin fork. g-integral I0 = %.6f" % I0)
print("S21a CALIBRATION: a_s(1) = %.2f (booked 34.1) | a_s(1/9) = %.2f (booked 11.4):"
      % (a_s(1.0), a_s(1.0/9.0)),
      "PASS" if abs(a_s(1.0)-34.1) < 0.15 and abs(a_s(1.0/9.0)-11.4) < 0.1 else "FAIL")
print("window: lambda_eff in [%.3f, %.3f]  (a_s = %.1f±%.1f)" % (*LAM_WIN, AS_SHADOW, AS_BAND))

print("\nFORK:")
results = {}
# L1, L2 brackets
results["L1 filled-only 1/9"] = 1.0/9.0
results["L2 lone-only 1"] = 1.0
# L3 two-channel equal split
results["L3 two-channel 1/4"] = 0.25
# L4 profile amplitude count with E-L weight
lam_u = 1.0/(1.0 + 8.0*u)
results["L4 profile 1/(1+8u)"] = lam_eff_profile(lam_u)
# L5 sqrt-interpolation at mean filling 1/2 -> lambda = 4/9
results["L5 sqrt-interp 4/9"] = 4.0/9.0
# L6 harmonic count at mean filling -> 1/5
results["L6 harmonic-nu-bar 1/5"] = 0.2

survivors = []
for name, lam in results.items():
    a = a_s(lam)
    inwin = LAM_WIN[0] <= lam <= LAM_WIN[1]
    print("  %-24s lambda=%.4f  a_s=%.2f  %s" % (name, lam, a, "IN WINDOW" if inwin else "out"))
    if inwin: survivors.append(name)

print("\nS21b survivors:", ", ".join(survivors) if survivors else "NONE — booked miss")
# extra diagnostics for the record
lam4 = results["L4 profile 1/(1+8u)"]
print("  L4 detail: uniform-measure mean ln9/8 = %.4f; E-L-weighted = %.4f; implied a_s = %.2f"
      % (np.log(9.0)/8.0, lam4, a_s(lam4)))
print("  L3 vs L4 spread: %.4f vs %.4f (a_s %.2f vs %.2f)" % (0.25, lam4, a_s(0.25), a_s(lam4)))
print("\nS21c GRADE CAP: any survivor = IDENTIFICATION grade (joints named: L3 equal-stiffness; L4 m-linearity).")
print("S21d shadow lambda_eff = %.4f (a_s = %.1f); capacity-softened ratio direction: report only."
      % ((AS_SHADOW/34.1)**2, AS_SHADOW))
