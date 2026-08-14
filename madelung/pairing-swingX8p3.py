#!/usr/bin/env python3
"""Pairing swing X-8'-P3 — precision pass, second registration (P2's STOP stands).

P2 DIAGNOSIS (booked): the difference trick cut the systematic 7x but left
|F(-10)-1| = 2.3e-4 vs the 2e-4 gate — the residual is CHIRP MISMATCH: the
census DM's oscillation phase drifts against the fixed-k uniform reference,
and the mismatch ACCUMULATES WITH RANGE, while the truncated tails cancel
identically in the difference regardless (the cos^2 average is chirp-blind).
So the range is not a convergence knob to maximize — it is a mismatch knob to
set: SHORT range, tails cancelled by construction.

DECLARED CRITERION (not a tuned dial): rng_fac = 12 central (a few local
oscillation periods: enough to capture the hole, short enough to bound chirp),
VALIDITY GATE = the range ladder {8, 16} must move F_nat at zbar = -10 by
< 3e-5 each — else the mu readout is INSTRUMENT-LIMIT, no knob re-picking.

SEQUENCING FIX (P2 lesson): the LAW table (1e-3-grade, already achieved) is
produced and exported UNCONDITIONALLY at its own working gate; only the mu
claim rides the tight precision chain.

GATES:
  P3-a  stack rerun (Airy/Bessel/census) — STOP on fail.
  P3-b  LAW WORKING GATE: |F_nat(-10) - 1| < 1e-3 -> law stations + export
        licensed (this bound was already met at 2.3e-4 in P2).
  P3-c  PRECISION CHAIN (mu license): |F_nat(-10) - 1| < 1e-4 AND range
        ladder {8,16} each < 3e-5 AND dt/2 < 2e-5 — else mu = INSTRUMENT-LIMIT
        (law still delivered).
  P3-d  THE mu CLAIM (only if P3-c): stations {-8,-7,-6,-5,-4}, fit
        mu s^2 + beta s^4; claim = within 10% of exactly one of
        {7/81 | 10/81}, other excluded >= 3x scatter; scatter > 5% = limit.
        Hand expectation (unchanged, declared): 10/81.
  P3-e  THE LAW + EXPORT (under P3-b): stations -8..0 working, {0.5, 1}
        report; sign structure vs the imported form stated as measured;
        native-gradient-law.csv written for X-9.

Run from workspace root. Registration commit = this file, pre-run.
"""
import numpy as np, math, time

C_LDA = (3.0/4.0)*(3.0/math.pi)**(1.0/3.0)
CS_LDA = (3.0/4.0)*(6.0/math.pi)**(1.0/3.0)

XHI, XLO, H = 16.0, -40.0, 5.0e-4
def build_airy():
    n = int(round((XHI - XLO)/H)) + 1
    xs = np.linspace(XLO, XHI, n)
    ai = np.zeros(n); aip = np.zeros(n)
    x0 = XHI
    xi = (2.0/3.0)*x0**1.5
    u1, u2, u3 = 5.0/72.0, 385.0/10368.0, 85085.0/2239488.0
    v1, v2, v3 = -7.0/72.0, -455.0/10368.0, -95095.0/2239488.0
    pref = math.exp(-xi)/(2.0*math.sqrt(math.pi))
    y = pref*x0**-0.25*(1.0 - u1/xi + u2/xi**2 - u3/xi**3)
    yp = -pref*x0**0.25*(1.0 - v1/xi + v2/xi**2 - v3/xi**3)
    ai[-1], aip[-1] = y, yp
    h = -H; x = x0
    for i in range(n-2, -1, -1):
        k1y, k1p = yp, x*y
        k2y, k2p = yp + 0.5*h*k1p, (x + 0.5*h)*(y + 0.5*h*k1y)
        k3y, k3p = yp + 0.5*h*k2p, (x + 0.5*h)*(y + 0.5*h*k2y)
        k4y, k4p = yp + h*k3p, (x + h)*(y + h*k3y)
        y += (h/6.0)*(k1y + 2*k2y + 2*k3y + k4y)
        yp += (h/6.0)*(k1p + 2*k2p + 2*k3p + k4p)
        x += h
        ai[i], aip[i] = y, yp
    return xs, ai, aip

XS, AI, AIP = build_airy()
def Ai(x): return np.interp(x, XS, AI)
def Aip(x): return np.interp(x, XS, AIP)

i0 = int(round((0.0 - XLO)/H))
g1 = (abs(AI[i0] - 0.3550280539) < 1e-6 and abs(AIP[i0] + 0.2588194038) < 1e-6)
TH = (np.arange(384) + 0.5)*(math.pi/384)
def J1(x):
    x = np.asarray(x, float)
    return np.trapezoid(np.cos(TH[None, :] - x[..., None]*np.sin(TH[None, :])), TH, axis=-1)/math.pi
g2 = abs(float(np.ravel(J1(np.array([1.0])))[0]) - 0.4400505857) < 1e-6

DT = 2.0e-3
def n_s(z):
    tmax = max(1.0, 14.0 - z)
    t = (np.arange(int(tmax/DT)) + 0.5)*DT
    a = Ai(z + t)
    return float(np.sum(t*a*a)*DT/(4*math.pi))
def n_s_prime(z):
    tmax = max(1.0, 14.0 - z)
    t = (np.arange(int(tmax/DT)) + 0.5)*DT
    return float(np.sum(t*2*Ai(z + t)*Aip(z + t))*DT/(4*math.pi))

g3 = True
for z in (-8.0, -12.0):
    dev = (n_s(z) - (-z)**1.5/(6*math.pi**2))/((-z)**1.5/(6*math.pi**2))
    g3 = g3 and abs(dev) < 0.005
print("P3-a stack:", "PASS" if (g1 and g2 and g3) else "FAIL — STOP")
if not (g1 and g2 and g3): raise SystemExit(1)

def station(zbar, ngrid=140, rng_fac=12.0, dt=DT):
    ns = n_s(zbar)
    ntot = 2*ns
    k = (3*math.pi**2*ntot)**(1.0/3.0)
    rng = min(rng_fac/max(k, 0.35), 40.0)
    zet = (np.arange(ngrid) + 0.5)*(rng/ngrid)
    rho = (np.arange(ngrid) + 0.5)*(rng/ngrid)
    tmax = max(1.0, 14.0 - zbar)
    t = (np.arange(int(tmax/dt)) + 0.5)*dt
    A = Ai(zbar + zet[:, None]/2 + t[None, :])*Ai(zbar - zet[:, None]/2 + t[None, :])
    st = np.sqrt(t)
    G = (st[:, None]*J1(np.outer(st, rho)))/(2*math.pi*rho[None, :])
    gam = (A*dt) @ G
    S = np.sqrt(zet[:, None]**2 + rho[None, :]**2)
    kern = 2*math.pi*rho[None, :]/S
    cell = (rng/ngrid)**2
    Qc = -0.5*2.0*float(np.sum(gam*gam*kern))*cell
    x = k*S
    j1x = np.sin(x)/(x*x) - np.cos(x)/x
    gu = ns*3.0*j1x/x
    Qu = -0.5*2.0*float(np.sum(gu*gu*kern))*cell
    Eu = -CS_LDA*ns**(4.0/3.0)
    F_nat = (Qc + (Eu - Qu))/Eu
    npr = 2*n_s_prime(zbar)
    s = abs(npr)/(2*(3*math.pi**2*ntot)**(1.0/3.0)*ntot)
    return s, F_nat

t0 = time.time()
s10, F10 = station(-10.0)
law_ok = abs(F10 - 1) < 1e-3
print("\nP3-b law working gate: F_nat(-10) = %.6f (|F-1| = %.1e < 1e-3) -> %s"
      % (F10, abs(F10 - 1), "PASS — law licensed" if law_ok else "FAIL — STOP"))
if not law_ok: raise SystemExit(1)

print("\nP3-c precision chain (mu license):")
_, F8 = station(-10.0, rng_fac=8.0)
_, F16 = station(-10.0, rng_fac=16.0)
_, Fdt = station(-10.0, dt=DT/2)
c1 = abs(F10 - 1) < 1e-4
c2 = abs(F8 - F10) < 3e-5 and abs(F16 - F10) < 3e-5
c3 = abs(Fdt - F10) < 2e-5
print("  |F(-10)-1| = %.2e (< 1e-4) -> %s" % (abs(F10 - 1), "ok" if c1 else "MISS"))
print("  range ladder: dF(8) = %+.2e  dF(16) = %+.2e (< 3e-5) -> %s"
      % (F8 - F10, F16 - F10, "ok" if c2 else "MISS"))
print("  dt/2: dF = %+.2e (< 2e-5) -> %s" % (Fdt - F10, "ok" if c3 else "MISS"))
mu_lic = c1 and c2 and c3
print("P3-c:", "PASS — mu licensed" if mu_lic else "FAIL — mu INSTRUMENT-LIMIT (law still delivered)")

if mu_lic:
    print("\nP3-d THE mu CLAIM:")
    pts = []
    for zb in (-8.0, -7.0, -6.0, -5.0, -4.0):
        s, F = station(zb)
        pts.append((s*s, F - 1.0))
        print("  zbar=%5.1f: s = %.4f  F-1 = %+.3e  (F-1)/s^2 = %.5f" % (zb, s, F - 1, (F-1)/(s*s)))
    X = np.array([[x, x*x] for x, _ in pts])
    Y = np.array([y for _, y in pts])
    coef, *_ = np.linalg.lstsq(X, Y, rcond=None)
    mu_fit = float(coef[0])
    scatter = float(np.std([(y/x) for (x, y) in pts]))
    SH, AK = 7.0/81.0, 10.0/81.0
    print("  fit: mu = %.5f (s^4 coef %+.4f) | station scatter %.5f" % (mu_fit, float(coef[1]), scatter))
    if scatter > 0.05*abs(mu_fit):
        print("P3-d: INSTRUMENT-LIMIT — scatter %.0f%% of mu" % (100*scatter/abs(mu_fit)))
    elif abs(mu_fit - AK)/AK < 0.10 and abs(mu_fit - SH) >= 3*scatter:
        print("P3-d: PASS — mu_native = %.5f on 10/81 (%+.1f%%); 7/81 EXCLUDED %.0fx"
              % (mu_fit, 100*(mu_fit - AK)/AK, abs(mu_fit - SH)/max(scatter, 1e-12)))
    elif abs(mu_fit - SH)/SH < 0.10 and abs(mu_fit - AK) >= 3*scatter:
        print("P3-d: PASS-INVERTED — mu_native = %.5f on 7/81 (%+.1f%%); 10/81 EXCLUDED"
              % (mu_fit, 100*(mu_fit - SH)/SH))
    else:
        print("P3-d: mu_native = %.5f — neither fork at claim grade; booked as the census's own number" % mu_fit)
else:
    print("\nP3-d: unscored (P3-c clause)")

print("\nP3-e THE LAW + EXPORT:")
MU_I, KAP = 10.0/81.0, 0.804
rows = []
for zb in (-8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0):
    s, F = station(zb)
    Fimp = 1.0 + KAP - KAP/(1.0 + MU_I*s*s/KAP)
    tag = " (report-only)" if zb >= 0.5 else ""
    rows.append((s, F))
    print("  zbar=%5.1f: s = %.4f  F_nat = %.5f  vs imported %.5f  (%+.1f%%)%s"
          % (zb, s, F, Fimp, 100*(F - Fimp)/Fimp, tag))
with open("poams-engineering-public/madelung/native-gradient-law.csv", "w") as f:
    f.write("s,F_native\n")
    for s, F in rows:
        f.write("%.6f,%.6f\n" % (s, F))
print("  exported %d rows -> madelung/native-gradient-law.csv" % len(rows))
print("[total %.0fs]" % (time.time() - t0))
