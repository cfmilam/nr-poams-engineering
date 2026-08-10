#!/usr/bin/env python3
"""nbody-n4 step 1 — numerical resonant-coefficient extractor (reg f7780dd).
C_pq(alpha): double-Fourier component of the direct term 1/|r-r'| (+ indirect for
the arguments that carry it) for argument p*lam' - q*lam - (p-q)*pi_w, inner ellipse
(a=1, e, varpi=0), outer circle (a'=1/alpha). Coefficient normalized as in R =
(mu f'/a') * C * e^{p-q} cos(phi)  ->  extract F/e^{p-q} with F in units of 1/a'.
Benchmark gates: f_d(2:1) = -1.19 (2%), d'Alembert exponent (5%)."""
import math

def kepler_E(M, e):
    E = M if e < 0.8 else math.pi
    for _ in range(60):
        E -= (E - e*math.sin(E) - M)/(1 - e*math.cos(E))
    return E

def extract(p, q, alpha, e, N=512):
    """Fourier coefficient of cos(p lam' - q lam) of a'*(1/Delta - indirect) with
    inner ellipse (varpi=0). Returns C such that term = C e^{p-q}... (C at this e)."""
    ap = 1.0/alpha   # outer radius (a=1 inner)
    tot = 0.0
    for i in range(N):
        lam = 2*math.pi*(i+0.5)/N
        E = kepler_E(lam, e)                       # lam = mean anomaly (varpi=0)
        x = math.cos(E) - e; y = math.sqrt(1-e*e)*math.sin(E)   # a=1
        for jj in range(N):
            lamp = 2*math.pi*(jj+0.5)/N
            xp, yp = ap*math.cos(lamp), ap*math.sin(lamp)
            d = math.sqrt((x-xp)**2 + (y-yp)**2)
            r2 = 1.0 - 2*e*math.cos(lam)*0.0       # placeholder no-op
            # direct + indirect (indirect = - r.r'/a'^3, standard)
            f = ap*(1.0/d) - ap*((x*xp + y*yp)/ap**3)
            tot += f*math.cos(p*lamp - q*lam)
    return 2.0*tot/(N*N)   # cos-component (double average, x2 for cos norm)

def coeff(p, q, alpha):
    """C_pq and measured d'Alembert exponent from two small e values."""
    k = p - q
    e1, e2 = 0.05, 0.10
    F1, F2 = extract(p, q, alpha, e1), extract(p, q, alpha, e2)
    kfit = math.log(abs(F2/F1))/math.log(e2/e1)
    C = F1/ e1**k
    return C, kfit

print("nbody-n4 extractor — benchmark gates first")
# Gate (i): 2:1 at the Galilean alpha 0.6286 -> expect ~ -1.19 (f_d includes the
# indirect part? tabulated -1.19 is the DIRECT term per N3 run2; here we include
# indirect explicitly, so benchmark against N3's verified direct-only -1.1832 by
# subtracting the analytic indirect for 2:1... simpler: extract WITHOUT indirect.)
def extract_direct(p, q, alpha, e, N=512):
    ap = 1.0/alpha; tot = 0.0
    for i in range(N):
        lam = 2*math.pi*(i+0.5)/N
        E = kepler_E(lam, e)
        x = math.cos(E) - e; y = math.sqrt(1-e*e)*math.sin(E)
        for jj in range(N):
            lamp = 2*math.pi*(jj+0.5)/N
            d = math.sqrt((x-ap*math.cos(lamp))**2 + (y-ap*math.sin(lamp))**2)
            tot += (ap/d)*math.cos(p*lamp - q*lam)
    return 2.0*tot/(N*N)

def coeff_direct(p, q, alpha):
    k = p - q
    e1, e2 = 0.05, 0.10
    F1 = extract_direct(p, q, alpha, e1); F2 = extract_direct(p, q, alpha, e2)
    kfit = math.log(abs(F2/F1))/math.log(e2/e1)
    return F1/e1**k, kfit

a21 = 0.6286
C21, k21 = coeff_direct(2, 1, a21)
print(f"  2:1 direct @ alpha={a21}: C = {C21:+.4f} (N3-verified -1.1832; tabulated -1.19)  "
      f"exponent = {k21:.3f} (want 1)")
gate1 = abs(abs(C21) - 1.1832)/1.1832 < 0.02 and abs(k21-1) < 0.05
print(f"  GATE (i): {'PASS' if gate1 else 'FAIL'}")
# Kirkwood alphas: a_res = (q/p)^{2/3} * a_Jup; alpha = a_res/a_Jup = (q/p)^{2/3}
for (p_, q_) in ((3,1),(5,2),(7,3),(2,1)):
    al = (q_/p_)**(2.0/3.0)
    C, kf = coeff_direct(p_, q_, al)
    print(f"  {p_}:{q_} @ alpha={al:.4f}: C = {C:+.4f}   e-exponent = {kf:.3f} (d'Alembert {p_-q_})")
