#!/usr/bin/env python3
"""Pairing swing X-8'-P2 — THE PRECISION PASS on the Airy thinning-census law.

WHAT X-8' LEFT: stack true (LDA emergence 0.17%), mu Taylor readout
instrument-limited (quadrature 1e-3-class vs signal 1e-3-class), law stations
carrying a candidate SIGN finding (native law bends BELOW 1 near the frontier),
evanescent stations dead (t-grid clamped negative by the Ai-table limit at
large zeta — a construction bug, fixed here: the t-range is set by physics,
z + t <= 14, and np.interp's endpoint clamp is safely ~1e-20 beyond).

THE PRECISION ROUTE (difference trick): evaluate the MATCHED UNIFORM census
gamma_u(s) = n_s * 3 j1(k s)/(k s), k = (6 pi^2 n_s)^{1/3), on the SAME
quadrature nodes with the SAME kernel and range. Its exact answer is known
(e_xs = -(3/4)(6/pi)^{1/3} n_s^{4/3}), so

    e_xs_census = Q(census) + [ E_exact_uniform - Q(uniform) ]

cancels the shared systematic (truncated oscillatory tail, grid bias) to the
anisotropy x systematic level. F_nat = e_xs_census / E_exact_uniform(n_s).

GATES (pre-run; kills live):
  P2-a  INHERITED STACK: G1/G2/G3 rerun (Airy, Bessel, census fidelity) — STOP
        on any; edge fix validated: gamma nonzero at zbar = 0.
  P2-b  DIFFERENCE-TRICK VALIDATION at zbar = -10: |F_nat - 1| < 2e-4
        (10x tighter than X-8' G4; the shared-systematic size |E - Q_u|/|E|
        reported beside it) — else STOP, no claim-grade readouts.
  P2-c  PRECISION LADDERS at zbar = -6: grid x1.5 and range x1.5 each move
        F_nat by < 3e-5 — else the mu readout is booked instrument-limit again.
  P2-d  THE mu CLAIM: stations zbar in {-8, -7, -6, -5, -4}: fit
        F_nat - 1 = mu s^2 + beta s^4. CLAIM iff mu within 10% of exactly ONE
        of {7/81 = 0.08642 | 10/81 = 0.12346} with the other excluded by
        >= 3x the fit scatter; stable elsewhere = the census's own number,
        booked; scatter > 5% of mu = INSTRUMENT-LIMIT. Hand expectation
        (declared, unchanged): 10/81.
  P2-e  THE LAW at working grade: stations zbar in {-3, -2.5, -2, -1.5, -1,
        -0.5, 0} (+ {0.5, 1} report-only): (s, F_nat) table; the sign
        structure vs the imported bounded form stated as measured;
        monotonicity/shape named.
  P2-f  EXPORT: the measured law written to madelung/native-gradient-law.csv
        (s, F_nat rows, deep-to-edge) for X-9 (the d-collapse re-run with the
        native law replacing both imports).

Run from workspace root. Registration commit = this file, pre-run.
"""
import numpy as np, math, time

C_LDA = (3.0/4.0)*(3.0/math.pi)**(1.0/3.0)
CS_LDA = (3.0/4.0)*(6.0/math.pi)**(1.0/3.0)   # per-sense coefficient

# ---------------- Airy table (as X-8', seed through zeta^-3) ----------------
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
g2 = abs(float(J1(np.array(1.0))) - 0.4400505857) < 1e-6

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
print("P2-a stack: Airy %s | Bessel %s | census %s ->" %
      ("ok" if g1 else "FAIL", "ok" if g2 else "FAIL", "ok" if g3 else "FAIL"),
      "PASS" if (g1 and g2 and g3) else "FAIL — STOP")
if not (g1 and g2 and g3): raise SystemExit(1)

def station(zbar, ngrid=140, rng_fac=24.0, dt=DT):
    """(s, F_nat) via the difference trick; also returns the shared-systematic size."""
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
    # matched uniform census on the SAME nodes
    x = k*S
    j1x = np.sin(x)/(x*x) - np.cos(x)/x
    gu = ns*3.0*j1x/x
    Qu = -0.5*2.0*float(np.sum(gu*gu*kern))*cell
    Eu = -CS_LDA*ns**(4.0/3.0)
    exs = Qc + (Eu - Qu)
    F_nat = exs/Eu
    npr = 2*n_s_prime(zbar)
    s = abs(npr)/(2*(3*math.pi**2*ntot)**(1.0/3.0)*ntot)
    return s, F_nat, (Eu - Qu)/Eu

t0 = time.time()
s10, F10, sys10 = station(-10.0)
print("\nP2-b difference-trick validation at zbar = -10:")
print("  shared systematic |E-Qu|/E = %.2e | F_nat = %.6f (|F-1| = %.1e, gate < 2e-4) -> %s"
      % (abs(sys10), F10, abs(F10 - 1), "PASS" if abs(F10 - 1) < 2e-4 else "FAIL — STOP"))
if abs(F10 - 1) >= 2e-4: raise SystemExit(1)

print("\nP2-c precision ladders at zbar = -6:")
sA, FA, _ = station(-6.0)
_, Fg, _ = station(-6.0, ngrid=210)
_, Fr, _ = station(-6.0, rng_fac=36.0)
okg = abs(Fg - FA) < 3e-5; okr = abs(Fr - FA) < 3e-5
print("  grid x1.5: dF = %+.2e (gate < 3e-5) -> %s" % (Fg - FA, "PASS" if okg else "FAIL"))
print("  range x1.5: dF = %+.2e (gate < 3e-5) -> %s" % (Fr - FA, "PASS" if okr else "FAIL"))
prec_ok = okg and okr

print("\nP2-d THE mu CLAIM (deep stations):")
pts = []
for zb in (-8.0, -7.0, -6.0, -5.0, -4.0):
    s, F, _ = station(zb)
    pts.append((s*s, F - 1.0))
    print("  zbar=%5.1f: s = %.4f  F-1 = %+.3e  (F-1)/s^2 = %.5f" % (zb, s, F - 1, (F-1)/(s*s)))
X = np.array([[x, x*x] for x, _ in pts])
Y = np.array([y for _, y in pts])
coef, res, *_ = np.linalg.lstsq(X, Y, rcond=None)
mu_fit, beta = float(coef[0]), float(coef[1])
resid = Y - X @ coef
scatter = float(np.std([(y/x) for (x, y) in pts]))
SH, AK = 7.0/81.0, 10.0/81.0
print("  fit: mu = %.5f  beta(s^4) = %+.4f | per-station (F-1)/s^2 std = %.5f | fit resid rms = %.1e"
      % (mu_fit, beta, scatter, float(np.sqrt(np.mean(resid**2)))))
if not prec_ok:
    print("P2-d: INSTRUMENT-LIMIT (precision ladders failed) — booked")
elif scatter > 0.05*abs(mu_fit):
    print("P2-d: INSTRUMENT-LIMIT — station scatter %.1f%% of mu > 5%%" % (100*scatter/abs(mu_fit)))
elif abs(mu_fit - AK)/AK < 0.10 and abs(mu_fit - SH) >= 3*scatter:
    print("P2-d: PASS — mu_native = %.5f lands on 10/81 = %.5f (%+.1f%%); 7/81 EXCLUDED by %.0fx scatter"
          % (mu_fit, AK, 100*(mu_fit - AK)/AK, abs(mu_fit - SH)/max(scatter, 1e-12)))
elif abs(mu_fit - SH)/SH < 0.10 and abs(mu_fit - AK) >= 3*scatter:
    print("P2-d: PASS-INVERTED — mu_native = %.5f lands on 7/81 (%+.1f%%); 10/81 EXCLUDED"
          % (mu_fit, 100*(mu_fit - SH)/SH))
else:
    print("P2-d: mu_native = %.5f — neither fork value at claim grade; booked as the census's own number" % mu_fit)

print("\nP2-e THE LAW (working grade) + P2-f export:")
MU_I, KAP = 10.0/81.0, 0.804
rows = []
for zb in (-8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0):
    s, F, _ = station(zb)
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
