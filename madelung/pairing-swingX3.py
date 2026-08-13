#!/usr/bin/env python3
# Pairing swing X-3 — gradient exposure of the d-collapse. Registration: a92bf6e (pre-run).
# TF profile at Z=21; s(x); enhancement (10/81)s^2; region-weighted means 3d vs 4s.
import numpy as np, math

B1 = 1.5880710226113753
Z = 21.0
MU = 10.0/81.0
b = 0.25*(9*math.pi**2/(2*Z))**(1/3)   # a0 units

# solve TF chi on x in [0.01, 60] (RK4, series start; stop on chip>0 drift guard)
x0 = 0.01
chi = 1 - B1*x0 + (4/3)*x0**1.5 - (2*B1/5)*x0**2.5 + (1/3)*x0**3
chip = -B1 + 2*math.sqrt(x0) - B1*x0**1.5 + x0*x0
h = 1e-4
X = [x0]; C = [chi]; CP = [chip]
x = x0
while x < 60.0:
    if chip > 0 or chi <= 1e-9: break
    def f(xx, c, cp):
        return cp, max(c, 0.0)**1.5/math.sqrt(xx)
    k1 = f(x, chi, chip)
    k2 = f(x+h/2, chi+h/2*k1[0], chip+h/2*k1[1])
    k3 = f(x+h/2, chi+h/2*k2[0], chip+h/2*k2[1])
    k4 = f(x+h, chi+h*k3[0], chip+h*k3[1])
    chi += h/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0])
    chip += h/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1])
    x += h
    X.append(x); C.append(chi); CP.append(chip)
X = np.array(X); C = np.array(C); CP = np.array(CP)
print("TF solved: x range [%.2f, %.2f] (guard at chi=%.2e); b = %.4f a0" % (X[0], X[-1], C[-1], b))

# density and s on the profile (atomic units, e=hbar=m=1)
# rho(r) = (Z/(4 pi b^3)) * (chi/x)^{3/2};  r = b x
rho = (Z/(4*math.pi*b**3)) * np.maximum(C/X, 1e-30)**1.5
# d rho/dr = (Z/(4 pi b^4)) * (3/2) sqrt(chi/x) * (chi' x - chi)/x^2
drho = (Z/(4*math.pi*b**4)) * 1.5*np.sqrt(np.maximum(C/X, 1e-30)) * (CP*X - C)/X**2
kF = (3*math.pi**2*rho)**(1/3)
s = np.abs(drho)/(2*kF*rho)
enh = MU*s*s
r = b*X

def region_stats(rlo, rhi, label):
    m = (r >= rlo) & (r <= rhi)
    w = rho[m]*r[m]**2                       # density weight (quanta per shell)
    mean_enh = float(np.sum(enh[m]*w)/np.sum(w))
    smean = float(np.sum(s[m]*w)/np.sum(w))
    print("  %-22s r in [%.1f, %.1f] a0: <s> = %.3f  <enhancement> = %.2f%%"
          % (label, rlo, rhi, smean, 100*mean_enh))
    return mean_enh

print("\nX-3c exposure on the Z = 21 profile (mu = 10/81):")
e3d = region_stats(0.5, 2.0, "3d scoring region")
e4s = region_stats(2.5, 6.0, "4s region")
print("  differential (4s - 3d): %+.2f%% — enhancement concentrates %s"
      % (100*(e4s - e3d), "OUTWARD (4s side)" if e4s > e3d else "INWARD (3d side)"))
print("  spot values of s: r=0.5: %.3f | r=1: %.3f | r=2: %.3f | r=4: %.3f | r=6: %.3f"
      % tuple(float(np.interp(rr, r, s)) for rr in (0.5, 1, 2, 4, 6)))

verdict_robust = abs(e3d) < 0.03
print("\nVERDICT RULE: 3d-region uniform-equivalent %.2f%% vs the 3%% line ->" % (100*e3d),
      "GRADIENT-ROBUST in the scoring region" if verdict_robust else "EXPOSURE BOOKED")
if e4s > e3d:
    print("  direction note: the excess discount sits on the 4s side — it deepens the OUTER")
    print("  orbit's books, i.e., pushes AGAINST early collapse; the Sc verdict's exposure is")
    print("  therefore on the safe side IF the differential dominates (signed, reported, unclaimed).")
