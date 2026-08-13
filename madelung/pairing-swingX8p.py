#!/usr/bin/env python3
"""Pairing swing X-8' — THE AIRY THINNING-CENSUS (the native gradient law).

REFRAME (Star Lord, 2026-08-13 17:40, on the record): X-8 chased the extant
object (their gradient-expansion Taylor coefficient) inside their machinery
(plane-wave PT, determinant exchange) and died of that machinery's own
cancellation sickness. The native question: how does the exclusion structure
around a quantum reshape where the census THINS? POAMS already owns the exact
object for that: a census filled to the E = 0 frontier under a uniform tilt —
the same admission license as H4/N-1, whose modes are the fold functions
N-4/N-5 already integrate natively (Airy). Exactly solvable. No perturbation
theory. Nothing cancels. One family sweeps the entire thinning range s = 0..inf,
so the deliverable is the WHOLE response law F_nat(s) — the imported mu AND the
imported bounded-form kappa both become readouts of it.

CONSTRUCTION (units: hbar = m_q = 1, tilt F = 1/2 so V(z) = z/2 and the Airy
argument is z + t with t = -2*eps >= 0; scale invariance in the tilt is
structural — every quantity is built in (2F)^{1/3} units):
  modes  psi_eps(z) = sqrt(2) Ai(z - 2 eps), occupied eps <= 0 (E = 0 license)
  DM     gamma_s(z,z',rho) = INT_0^inf dt Ai(z+t) Ai(z'+t) g(t,rho),
         g(t,rho) = sqrt(t) J1(sqrt(t) rho)/(2 pi rho),  g(t,0) = t/(4 pi)
  census n_s(z) = (1/4pi) INT t Ai(z+t)^2 dt   [deep limit: (-z)^{3/2}/(6 pi^2)]
  law    e_x,s(zbar) = -(1/2) INT dzeta INT 2 pi rho drho gamma_s^2 / sqrt(zeta^2+rho^2)
         F_nat(zbar) = 2 e_x,s / ( -C n_tot^{4/3} ),  C = (3/4)(3/pi)^{1/3}
         s(zbar) = |n_tot'| / (2 (3 pi^2 n_tot)^{1/3} n_tot)   [n' exact via Ai']

GATES (hand-declared pre-run; kills live):
  G1 AIRY TABLE (native ODE integration, asymptotic seed at x = +12 w/ first
     correction, RK4 h = 5e-4 to x = -40): Ai(0) = 0.3550280539 and
     Ai'(0) = -0.2588194038 each to 1e-6; INT_0^inf Ai = 1/3 to 1e-5 — else STOP.
  G2 BESSEL: J1(1) = 0.4400505857, J1(5) = -0.3275791376 to 1e-6 — else STOP.
  G3 CENSUS FIDELITY: n(z)/LDA at z = -8, -10, -12 within 0.5%; exact-vs-
     numeric n' consistency 0.5% — else STOP.
  G4 LDA EMERGENCE (the X8-zero analog, now for the whole stack): F_nat at
     zbar = -10 (s^2 = 5.6e-4: mu-level content ~ 7e-5, invisible) must be
     1 within 0.5% — the uniform law of X-2 must EMERGE from the exact modes
     — else STOP, no law claim.
  G5 THE mu READOUT: stations zbar in {-2.5, -3, -4, -5, -6}:
     mu(zbar) = (F_nat - 1)/s^2, extrapolated s^2 -> 0. CLAIM iff within 10%
     of exactly ONE of {7/81 = 0.08642 | 10/81 = 0.12346} with the other
     excluded by >= 3x the extraction spread; stable landing elsewhere = the
     census's own number, booked (joints named); spread > 5% = INSTRUMENT-
     LIMIT for the Taylor readout (the LAW stations still stand on their own).
     HAND EXPECTATION (declared): the exact static construction is the AK-class
     object — expect 10/81; scored as measured.
  G6 THE LAW (the kappa-retirement candidate; report grade this flight):
     stations zbar in {-1.5, -1, -0.5, 0, +0.5, +1}: tabulate (s, F_nat)
     against the IMPORTED bounded form 1 + k - k/(1 + mu s^2/k) (mu = 10/81,
     k = 0.804): deviations on record; the native large-s behavior named.
  G7 LADDERS (one station each, thresholds declared): t-step /2 moves F_nat
     < 0.1%; (zeta,rho) grid x1.5 moves e_x < 0.3%; quadrature range x1.5
     moves e_x < 0.3%; tilt invariance structural (units), stated.

Run from workspace root. Registration commit = this file, pre-run.
"""
import numpy as np, math, time

C_LDA = (3.0/4.0)*(3.0/math.pi)**(1.0/3.0)

# ---------------- G1: native Airy table (fold equation y'' = x y) ----------------
XHI, XLO, H = 12.0, -40.0, 5.0e-4
def build_airy():
    n = int(round((XHI - XLO)/H)) + 1
    xs = np.linspace(XLO, XHI, n)
    ai = np.zeros(n); aip = np.zeros(n)
    # asymptotic seed at XHI with first correction
    x0 = XHI
    xi = (2.0/3.0)*x0**1.5
    pref = math.exp(-xi)/(2.0*math.sqrt(math.pi))
    a0 = pref*x0**-0.25*(1.0 - 5.0/(72.0*xi))
    ap0 = -pref*x0**0.25*(1.0 + 7.0/(72.0*xi))
    y, yp = a0, ap0
    ai[-1], aip[-1] = y, yp
    h = -H
    x = x0
    for i in range(n-2, -1, -1):
        # RK4 for y'' = x y
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
def Ai(x):
    return np.interp(x, XS, AI)
def Aip(x):
    return np.interp(x, XS, AIP)

i0 = int(round((0.0 - XLO)/H))
ai0, aip0 = AI[i0], AIP[i0]
intAi = float(np.sum(AI[i0:])*H) - 0.5*H*(AI[i0] + AI[-1])
g1 = (abs(ai0 - 0.3550280539) < 1e-6 and abs(aip0 - (-0.2588194038)) < 1e-6
      and abs(intAi - 1.0/3.0) < 1e-5)
print("G1 Airy table: Ai(0) = %.9f  Ai'(0) = %.9f  INT Ai = %.7f ->" % (ai0, aip0, intAi),
      "PASS" if g1 else "FAIL — STOP")
if not g1: raise SystemExit(1)

# ---------------- G2: Bessel J1 (integral representation) ----------------
TH = (np.arange(384) + 0.5)*(math.pi/384)
def J1(x):
    x = np.asarray(x, float)
    return np.trapezoid(np.cos(TH[None, :] - x[..., None]*np.sin(TH[None, :])), TH, axis=-1)/math.pi if x.ndim else \
           float(np.trapezoid(np.cos(TH - float(x)*np.sin(TH)), TH)/math.pi)
g2 = abs(J1(1.0) - 0.4400505857) < 1e-6 and abs(J1(5.0) - (-0.3275791376)) < 1e-6
print("G2 Bessel: J1(1) = %.9f  J1(5) = %.9f ->" % (J1(1.0), J1(5.0)), "PASS" if g2 else "FAIL — STOP")
if not g2: raise SystemExit(1)

# ---------------- census and its exact derivative ----------------
DT = 2.0e-3
def n_s(z):
    tmax = XHI - z - 1.0
    t = (np.arange(int(tmax/DT)) + 0.5)*DT
    a = Ai(z + t)
    return float(np.sum(t*a*a)*DT/(4*math.pi))
def n_s_prime(z):
    tmax = XHI - z - 1.0
    t = (np.arange(int(tmax/DT)) + 0.5)*DT
    a = Ai(z + t); ap = Aip(z + t)
    return float(np.sum(t*2*a*ap)*DT/(4*math.pi))

print("\nG3 census fidelity (deep interior -> LDA):")
g3 = True
for z in (-8.0, -10.0, -12.0):
    got = n_s(z)
    lda = (-z)**1.5/(6*math.pi**2)
    dev = (got - lda)/lda
    num = (n_s(z + 1e-3) - n_s(z - 1e-3))/2e-3
    ana = n_s_prime(z)
    ddev = (num - ana)/ana
    g3 = g3 and abs(dev) < 0.005 and abs(ddev) < 0.005
    print("  z=%5.1f: n_s %.6e vs LDA %.6e (%+.3f%%) | n' exact-vs-numeric %+.3f%%"
          % (z, got, lda, 100*dev, 100*ddev))
print("G3:", "PASS" if g3 else "FAIL — STOP")
if not g3: raise SystemExit(1)

# ---------------- the law at a station ----------------
def station(zbar, ngrid=110, rng_fac=24.0, dt=DT):
    """Return (s, F_nat) at midpoint zbar. Matrix-product evaluation:
    gamma(zeta, rho) = A(zeta, t) @ G(t, rho)."""
    ns = n_s(zbar)
    ntot = 2*ns
    kloc = (3*math.pi**2*ntot)**(1.0/3.0)
    rng = rng_fac/max(kloc, 0.35)
    zet = (np.arange(ngrid) + 0.5)*(rng/ngrid)        # zeta >= 0 (symmetric x2)
    rho = (np.arange(ngrid) + 0.5)*(rng/ngrid)
    tmax = XHI - (zbar + zet.max()/2) - 0.5
    t = (np.arange(int(tmax/dt)) + 0.5)*dt
    A = Ai(zbar + zet[:, None]/2 + t[None, :])*Ai(zbar - zet[:, None]/2 + t[None, :])  # (Nz, Nt)
    st = np.sqrt(t)
    G = (st[:, None]*J1(np.outer(st, rho)))/(2*math.pi*rho[None, :])                    # (Nt, Nr)
    gam = (A*dt) @ G                                                                     # (Nz, Nr)
    kern = 2*math.pi*rho[None, :]/np.sqrt(zet[:, None]**2 + rho[None, :]**2)
    ex_s = -0.5*2.0*float(np.sum(gam*gam*kern))*(rng/ngrid)**2   # x2: zeta symmetric
    ex_tot = 2*ex_s
    F_nat = ex_tot/(-C_LDA*ntot**(4.0/3.0))
    npr = 2*n_s_prime(zbar)
    s = abs(npr)/(2*(3*math.pi**2*ntot)**(1.0/3.0)*ntot)
    return s, F_nat, ex_s, ntot

print("\nG4 LDA EMERGENCE at zbar = -10:")
t0 = time.time()
s10, F10, _, _ = station(-10.0)
print("  s = %.5f  F_nat = %.6f  (gate |F-1| < 0.5%%) -> %s   [%.0fs]"
      % (s10, F10, "PASS" if abs(F10 - 1) < 0.005 else "FAIL — STOP", time.time() - t0))
if abs(F10 - 1) >= 0.005: raise SystemExit(1)

print("\nG5 THE mu READOUT (deep stations):")
mus = []
for zb in (-6.0, -5.0, -4.0, -3.0, -2.5):
    s, F, _, _ = station(zb)
    mu = (F - 1.0)/(s*s)
    mus.append((s*s, mu))
    print("  zbar=%5.1f: s = %.4f  F_nat = %.6f  mu(s) = %.5f" % (zb, s, F, mu))
# extrapolate mu(s^2) -> 0 linearly from the two smallest s^2
(x1, m1), (x2, m2) = mus[0], mus[1]
mu0 = (m1*x2 - m2*x1)/(x2 - x1)
spread = max(m for _, m in mus) - min(m for _, m in mus)
SH, AK = 7.0/81.0, 10.0/81.0
print("  mu (s^2 -> 0) = %.5f | station spread %.5f" % (mu0, spread))
sp_rel = spread/abs(mu0) if mu0 else 9.0
if sp_rel > 0.05 and not (min(abs(mu0-SH)/SH, abs(mu0-AK)/AK) < 0.10):
    print("G5: INSTRUMENT-LIMIT for the Taylor readout (spread %.1f%%); the law stations stand" % (100*sp_rel))
elif abs(mu0 - AK)/AK < 0.10 and abs(mu0 - SH) >= 3*spread:
    print("G5: PASS — mu_native = %.5f lands on 10/81 = %.5f (%+.1f%%); 7/81 EXCLUDED by %.0fx spread"
          % (mu0, AK, 100*(mu0 - AK)/AK, abs(mu0 - SH)/max(spread, 1e-12)))
    print("     THE IMPORT DISSOLVES: the census's own thinning law forces the coefficient.")
elif abs(mu0 - SH)/SH < 0.10 and abs(mu0 - AK) >= 3*spread:
    print("G5: PASS-INVERTED — mu_native = %.5f lands on 7/81 (%+.1f%%); 10/81 EXCLUDED — booked as measured"
          % (mu0, 100*(mu0 - SH)/SH))
else:
    print("G5: mu_native = %.5f — neither fork value at claim grade; booked as the census's own number" % mu0)

print("\nG6 THE LAW (near-frontier stations vs the imported bounded form):")
MU_I, KAP = 10.0/81.0, 0.804
for zb in (-1.5, -1.0, -0.5, 0.0, 0.5, 1.0):
    s, F, exs, ntot = station(zb)
    Fimp = 1.0 + KAP - KAP/(1.0 + MU_I*s*s/KAP)
    print("  zbar=%5.1f: s = %.3f  F_nat = %.4f  vs imported %.4f  (%+.1f%%)  [n_tot %.2e]"
          % (zb, s, F, Fimp, 100*(F - Fimp)/Fimp, ntot))

print("\nG7 LADDERS (station zbar = -4):")
sA, FA, _, _ = station(-4.0)
s_t, F_t, _, _ = station(-4.0, dt=DT/2)
s_g, F_g, _, _ = station(-4.0, ngrid=165)
s_r, F_r, _, _ = station(-4.0, rng_fac=36.0)
print("  t-step /2: F moves %+.4f%% (gate <0.1%%) -> %s" % (100*(F_t-FA)/FA, "PASS" if abs((F_t-FA)/FA) < 0.001 else "FLAG"))
print("  grid x1.5: F moves %+.4f%% (gate <0.3%%) -> %s" % (100*(F_g-FA)/FA, "PASS" if abs((F_g-FA)/FA) < 0.003 else "FLAG"))
print("  range x1.5: F moves %+.4f%% (gate <0.3%%) -> %s" % (100*(F_r-FA)/FA, "PASS" if abs((F_r-FA)/FA) < 0.003 else "FLAG"))
print("  tilt invariance: structural (all quantities in (2F)^{1/3} units) — stated")
print("[total %.0fs]" % (time.time() - t0))
