#!/usr/bin/env python3
# Pairing swing X-2 — the same-sense hole coefficient by composition.
# Registration: d9b815b (pre-run). Chain: N-1 census + AXIOM-C kernel + pair-exclusion
# subtraction + 1/r strain law. Zero dials; every check hand-declared.
import numpy as np, math
# ---- C2: the coherent overlap kernel of the filled ball (hbar = 1, per sense) ----
# K(s) = int_{|p|<=pF} e^{i p.s} d^3p/(2pi)^3 = rho_s * 3 j1(x)/x,  x = pF s
def j1(x):
    return np.sin(x)/x**2 - np.cos(x)/x

# numeric kernel from the ball (radial reduction): K(s) = (1/2pi^2 s) ∫_0^pF p sin(ps) dp
def K_ball(s, pF, n=20000):
    p = np.linspace(1e-9, pF, n)
    return np.trapezoid(p*np.sin(p*s), p)/(2*math.pi**2*s)

pF = 1.0
rho_s = pF**3/(6*math.pi**2)
print("X-2 verification (per sense, pF = 1, rho_s = %.6f):" % rho_s)

# closed form vs ball integral (3 spot separations)
ok_kernel = True
for s in (0.7, 2.3, 5.1):
    x = pF*s
    closed = rho_s*3*j1(x)/x
    ball = K_ball(s, pF)
    ok_kernel = ok_kernel and abs(closed - ball) < 1e-8
print("  kernel closed-form = ball integral at 3 separations:", "PASS" if ok_kernel else "FAIL")

# ---- X-2a: the two derived hole constraints as kernel checks ----
# contact: g(0) = 1 - |K(0)|^2/rho_s^2 = 0  (K(0) = rho_s)
g0 = 1 - (K_ball(1e-6, pF)/rho_s)**2
# sum rule: int d^3 s |K|^2 / rho_s = 1
ss = np.linspace(1e-6, 400.0, 4_000_000)
integrand = 4*math.pi*ss**2 * (rho_s*3*j1(pF*ss)/(pF*ss))**2 / rho_s
sumrule = np.trapezoid(integrand, ss)
tail = 18*math.pi*rho_s/(pF**4*ss[-1])   # analytic cos^2-averaged tail beyond s_max
sumrule += tail
print("X-2a contact deficit: g(0) = %.2e (exact 0):" % g0, "PASS" if abs(g0) < 1e-6 else "FAIL")
print("X-2a hole total: int |K|^2/rho_s d^3s = %.6f (exact 1):" % sumrule,
      "PASS" if abs(sumrule - 1) < 2e-3 else "FAIL")

# ---- X-2b: the strain discount coefficient ----
# per-volume discount (both senses): 2 * (1/2) * e^2 * int d^3s (1/s) |K(s)|^2
# per quantum: divide by rho = 2 rho_s; express as C_x * e^2 * rho^{1/3}
I = np.trapezoid(4*math.pi*ss * (3*j1(pF*ss)/(pF*ss))**2, ss)   # int d^3s |K/rho_s|^2 / s
Ex_per_volume = rho_s**2 * I      # = (1/2)*2*int |K|^2/s : pair half x two senses (e^2 = 1)
rho_tot = 2*rho_s
per_quantum = Ex_per_volume/rho_tot
Cx = per_quantum/rho_tot**(1/3)
target = (3/4)*(3/math.pi)**(1/3)
print("X-2b coefficient: eps_x per quantum = %.6f e^2 rho^{1/3}" % Cx)
print("      hand-declared (3/4)(3/pi)^{1/3} = %.6f -> |diff| = %.2e:" % (target, abs(Cx-target)),
      "PASS" if abs(Cx - target) < 1e-4 else "FAIL")

# scaling check: pF from the derived census at rho' = 8 rho -> coefficient invariant
pF2 = 2.0; rho_s2 = pF2**3/(6*math.pi**2)
ss2 = np.linspace(1e-6, 200.0, 2_000_000)
I2 = np.trapezoid(4*math.pi*ss2 * (3*j1(pF2*ss2)/(pF2*ss2))**2, ss2)
Cx2 = ((rho_s2**2*I2)/(2*rho_s2))/(2*rho_s2)**(1/3)
print("      scale invariance (rho x8): C_x = %.6f (rho^{4/3} law forced):" % Cx2,
      "PASS" if abs(Cx2 - target) < 1e-4 else "FAIL")

# ---- X-2c: the convention fork ----
print("X-2c: derived ENERGY coefficient = (3/4)(3/pi)^{1/3} -> the extant record's")
print("      Dirac / Gaspar-Kohn-Sham convention (alpha = 2/3 in Xalpha language);")
print("      Slater alpha = 1 is the potential-averaging variant, NOT selected.")
print("      The d-collapse instrument's convention-sensitivity: resolved to alpha = 2/3.")
