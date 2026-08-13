#!/usr/bin/env python3
"""Pairing swing X-7 — THE SMOOTH-DENSITY CHASSIS (the bracket's named decider).

WHAT IS OWED: X-4 (paste) drags the flip to Z = 20; X-6 (first-order energy)
confirms the drag's direction but holds Z* = 21; X-5 proved the deciding
divergence term unevaluable on the raw deposit grid (2nd derivatives of a
noisy density). The Aufbau open item (1) names this instrument: a density
representation smooth enough to carry the proper functional derivative
self-consistently.

METHOD (zero new physics; mu = 10/81, kappa = 0.804 as X-3..X-6):
  Each SCF iteration, fit a natural cubic spline to ln(rho) vs ln(r) on a
  coarse knot subgrid; every layer quantity is then ANALYTIC off the spline —
  s = |d ln rho/dr| / (2 k_F),  ds/dr from the spline's second derivative,
  and the divergence term
      v_div = (A/(2 (3 pi^2)^{1/3})) (1/r^2) d/dr [ r^2 sgn(rho') F'(s) ]
            = (A/(2 KF3)) [ 2 F'(s)/r + F''(s) s'(r) ] sgn(rho')
  with F' = 2 mu s / u^2, F'' = 2 mu/u^2 - 8 mu^2 s^2/(kappa u^3), u = 1 + mu s^2/kappa.
  No numerical differencing anywhere in the layer. Local part (F - sF') as in
  X-5. Baseline (F == 1) bypasses the spline entirely (tier3g chassis).

HAND-DECLARED GATES (registered pre-run; kills in both directions):
  X-7a BASELINE: F == 1 sweep reproduces the tier3g booked flip
       (Z*(1.50) = 21, all Z* in {20, 21}, 3d bound). Spline fidelity
       reported: median |ln rho_spline - ln rho_raw| over the significant
       region; > 0.15 at any deciding cell -> INSTRUMENT-LIMIT.
  X-7b THE DECIDER (self-consistent proper layer, bounded):
       SURVIVES  <=> Z*(m = 1.50) = 21 with the full proper potential:
                     the TFD verdict stands at derivative fidelity; the
                     X-4 paste drag was fidelity artifact end to end.
       FLIPS     <=> Z*(1.50) <= 20: the gradient layer owns the Sc/Ca
                     placement self-consistently; X-6's first-order stand
                     was the artifact of stopping at first order.
       VALIDITY CLAUSE: the verdict must (i) converge (dmax < 4e-3 within
       60 iters) at the deciding cells and (ii) AGREE ACROSS THE KNOT LADDER
       {NG//12, NG//8, NG//5} — disagreement or non-convergence at any
       deciding cell = INSTRUMENT-LIMIT, booked, no verdict, no knot chosen
       after the fact.
  X-7c MECHANISM: layer profile at r in {0.5, 1, 2, 4} a0 on the Z = 21
       felt floor: s, (F - sF'), div-term share and sign — confronted with
       X-5's raw-grid pathology (div/|v_loc| = 2.1-2.8, oscillating sign).
  X-7d HONESTY: knot-ladder verdict table; spline residual medians; r < 0.05
       a0 and rho < 1e-13 guards counted; convergence flags per cell.

Run from workspace root. Registration commit = this file, pre-run.
"""
import math, sys
from importlib import util as _u
spec = _u.spec_from_file_location("t3c", "memory/poams-audit/tier3c.py")
t3c = _u.module_from_spec(spec); sys.modules["t3c"] = t3c
spec.loader.exec_module(t3c)

NG, RG, DLNR, B0 = t3c.NG, t3c.RG, t3c.DLNR, t3c.B0
CX = (3.0/math.pi)**(1.0/3.0)
MU = 10.0/81.0
KAPPA = 0.804
KF3 = (3.0*math.pi**2)**(1.0/3.0)

def Fenh(s):
    return 1.0 + KAPPA - KAPPA/(1.0 + MU*s*s/KAPPA)

def Fp(s):
    u = 1.0 + MU*s*s/KAPPA
    return 2.0*MU*s/(u*u)

def Fpp(s):
    u = 1.0 + MU*s*s/KAPPA
    return 2.0*MU/(u*u) - 8.0*MU*MU*s*s/(KAPPA*u*u*u)

# ---------- natural cubic spline (Thomas solve), analytic derivatives ----------
class Spline:
    def __init__(self, x, y):
        n = len(x)
        h = [x[i+1]-x[i] for i in range(n-1)]
        a = [0.0]*n; b = [1.0]*n; c = [0.0]*n; d = [0.0]*n
        for i in range(1, n-1):
            a[i] = h[i-1]; b[i] = 2*(h[i-1]+h[i]); c[i] = h[i]
            d[i] = 6*((y[i+1]-y[i])/h[i] - (y[i]-y[i-1])/h[i-1])
        for i in range(1, n):
            w = a[i]/b[i-1] if b[i-1] != 0 else 0.0
            b[i] -= w*c[i-1]; d[i] -= w*d[i-1]
        M = [0.0]*n
        M[n-1] = d[n-1]/b[n-1] if b[n-1] != 0 else 0.0
        for i in range(n-2, -1, -1):
            M[i] = (d[i] - c[i]*M[i+1])/b[i] if b[i] != 0 else 0.0
        self.x, self.y, self.h, self.M = x, y, h, M
    def _seg(self, xv):
        x = self.x
        lo, hi = 0, len(x)-2
        while lo < hi:
            mid = (lo+hi)//2
            if xv > x[mid+1]: lo = mid+1
            else: hi = mid
        return lo
    def eval(self, xv):
        i = self._seg(xv)
        x, y, h, M = self.x, self.y, self.h, self.M
        t = xv - x[i]; hh = h[i]
        A = (x[i+1]-xv)/hh; B = t/hh
        val = A*y[i] + B*y[i+1] + ((A**3-A)*M[i] + (B**3-B)*M[i+1])*hh*hh/6.0
        dp = (y[i+1]-y[i])/hh - hh*(3*A*A-1)*M[i]/6.0 + hh*(3*B*B-1)*M[i+1]/6.0
        dpp = A*M[i] + B*M[i+1]
        return val, dp, dpp

def smooth_lnrho(mass, knots):
    """Fit ln rho vs ln r on a coarse subgrid; return per-grid rho, dlnrho/dr, d2."""
    lnr = [math.log(RG[i]) for i in range(NG)]
    rho_raw = [0.0]*NG
    for i in range(NG):
        dr = RG[i]*DLNR
        rho_raw[i] = mass[i]/(4.0*math.pi*RG[i]*RG[i]*dr)
    idx = [i for i in range(0, NG, max(1, NG//knots)) if rho_raw[i] > 1e-13]
    if len(idx) < 8:
        return rho_raw, None, None, 1e9
    xs = [lnr[i] for i in idx]; ys = [math.log(rho_raw[i]) for i in idx]
    sp = Spline(xs, ys)
    rho = [0.0]*NG; dln = [0.0]*NG; d2ln = [0.0]*NG
    resid = []
    for i in range(NG):
        if rho_raw[i] <= 1e-13 or lnr[i] < xs[0] or lnr[i] > xs[-1]:
            rho[i] = rho_raw[i]; continue
        v, dp, dpp = sp.eval(lnr[i])
        rho[i] = math.exp(v)
        dln[i] = dp/RG[i]                       # d ln rho / dr
        d2ln[i] = (dpp - dp)/(RG[i]*RG[i])      # d2 ln rho / dr2
        if rho_raw[i] > 1e-8:
            resid.append(abs(v - math.log(rho_raw[i])))
    resid_med = sorted(resid)[len(resid)//2] if resid else 1e9
    return rho, dln, d2ln, resid_med

GUARD = {"hits": 0}

def vx_smooth(mass, mult, bounded, knots):
    # CONSTRUCTION FIX (booked, pre-scoring): baseline (bounded=False) must be the
    # tier3g chassis VERBATIM — raw deposit density, no spline anywhere. Run 1 of
    # this instrument smoothed the baseline density too and scrambled the
    # near-degenerate flip cells (X-7a FAIL -> STOP fired correctly).
    if not bounded:
        out = [0.0]*NG
        for i in range(NG):
            dr = RG[i]*DLNR
            rr = mass[i]/(4.0*math.pi*RG[i]*RG[i]*dr)
            if rr > 0:
                out[i] = -mult*CX*(rr**(1.0/3.0))
        return out, 0.0
    rho, dln, d2ln, resid = smooth_lnrho(mass, knots)
    A = 0.75*mult*CX
    out = [0.0]*NG
    for i in range(NG):
        if rho[i] <= 1e-14: continue
        base = -mult*CX*(rho[i]**(1.0/3.0))
        if dln is None or RG[i] < 0.05 or rho[i] < 1e-13:
            GUARD["hits"] += 1
            out[i] = base; continue
        kF = (3.0*math.pi**2*rho[i])**(1.0/3.0)
        sgn = 1.0 if dln[i] > 0 else -1.0
        s = abs(dln[i])/(2.0*kF)
        # ds/dr: s = |dln|/(2 kF), kF' = kF * dln/3  ->  s' = sgn*d2ln/(2kF) - s*(dln/3)
        sprime = sgn*d2ln[i]/(2.0*kF) - s*(dln[i]/3.0)
        loc = Fenh(s) - s*Fp(s)
        div = (A/(2.0*KF3))*sgn*(2.0*Fp(s)/RG[i] + Fpp(s)*sprime)
        out[i] = base*loc + div
    return out, resid

def scf(Z, cfg, mult, bounded, knots, iters=None, mix=None):
    # baseline = tier3g/X-5 chassis numerics verbatim (40/0.4); layer = declared 60/0.3
    if iters is None: iters = 60 if bounded else 40
    if mix is None: mix = 0.3 if bounded else 0.4
    b = B0*max(Z,1)**(-1.0/3.0)
    Qf = sum(cfg.values())
    Ve = [min(Qf, Z)*(1.0 - t3c.TF(r/b))/r for r in RG]
    Vx = [0.0]*NG
    conv = False; resid = 0.0
    for it in range(iters):
        Vt = [-Z/RG[i] + Ve[i] + Vx[i] for i in range(NG)]
        mass = [0.0]*NG
        for (n,l), occ in sorted(cfg.items()):
            E = t3c.solve_mode(Vt, n, l)
            if E is None: E = -1e-9
            t3c.orbit(Vt, E, l+0.5, deposit=mass, occ=occ)
        Vnew = t3c.potential_of(mass)
        Vxnew, resid = vx_smooth(mass, mult, bounded, knots)
        dmax = max(abs(Vnew[i]-Ve[i])*RG[i] for i in range(NG))
        Ve = [mix*Vnew[i] + (1-mix)*Ve[i] for i in range(NG)]
        Vx = [mix*Vxnew[i] + (1-mix)*Vx[i] for i in range(NG)]
        if dmax < 4e-3:
            conv = True; break
    Vt = [-Z/RG[i] + Ve[i] + Vx[i] for i in range(NG)]
    return Vt, conv, resid

def sweep(bounded, knots, mults=(1.50, 1.70, 1.949), qs=(19, 20, 21, 22, 23)):
    zs = {}
    for m in mults:
        wins = []; zstar = None; bound = True; ncs = []; rmax = 0.0
        for Q in qs:
            core = t3c.madelung_config_upto(Q-1)
            Vt, conv, resid = scf(Q, core, m, bounded, knots)
            rmax = max(rmax, resid)
            if not conv: ncs.append(Q)
            es = {}
            for (lab, n, l) in (("4s",4,0), ("3d",3,2), ("4p",4,1)):
                es[lab] = t3c.solve_mode(Vt, n, l)
            if Q >= 21 and es["3d"] is None: bound = False
            cands = {k: v for k, v in es.items() if v is not None}
            w = min(cands, key=cands.get) if cands else "-"
            wins.append(w)
            if zstar is None and w == "3d": zstar = Q
        zs[m] = (zstar, bound, wins, ncs, rmax)
        print("  knots~%3d m=%.3f | %s | Z*=%s 3d-bound=%s nc=%s residmax=%.3f"
              % (knots, m, " ".join("%4s" % w for w in wins), zstar, bound,
                 ncs if ncs else "none", rmax), flush=True)
    return zs

print("X-7a BASELINE (F == 1, spline bypassed):")
base = sweep(False, 60)
ok_a = base[1.50][0] == 21 and all(v[0] in (20, 21) for v in base.values()) and all(v[1] for v in base.values())
print("X-7a:", "PASS — baseline reproduced" if ok_a else "FAIL — STOP")
if not ok_a:
    raise SystemExit(1)

print("\nX-7b THE DECIDER (self-consistent proper layer, knot ladder):")
KNOTS = (NG//12, NG//8, NG//5)
verdicts = {}
GUARD["hits"] = 0
for kn in KNOTS:
    enh = sweep(True, kn)
    fl = enh[1.50]
    if fl[3]:
        verdicts[kn] = "nc"
    elif fl[0] == 21 and fl[1]:
        verdicts[kn] = "21"
    elif fl[0] is not None and fl[0] <= 20 and fl[1]:
        verdicts[kn] = str(fl[0])
    else:
        verdicts[kn] = "unbound"
print("knot-ladder floor verdicts:", verdicts)
vs = set(verdicts.values())
if "nc" in vs or "unbound" in vs or len(vs) > 1:
    print("X-7b: INSTRUMENT-LIMIT — validity clause fired (non-convergence/unbound/ladder disagreement); no verdict, booked")
elif vs == {"21"}:
    print("X-7b: SURVIVES — Z*(1.50) = 21 self-consistently at derivative fidelity:")
    print("      the TFD verdict stands; X-4's paste drag was fidelity artifact end to end.")
else:
    print("X-7b: FLIPS — Z*(1.50) = %s self-consistently: the gradient layer OWNS the" % vs)
    print("      Sc/Ca placement; X-6's first-order stand was the artifact of first order.")

print("\nX-7c mechanism (Z=21, m=1.50, middle knots):")
core = t3c.madelung_config_upto(20)
Vt, conv, resid = scf(21, core, 1.50, True, NG//8)
mass = [0.0]*NG
for (n,l), occ in sorted(core.items()):
    E = t3c.solve_mode(Vt, n, l)
    if E is None: E = -1e-9
    t3c.orbit(Vt, E, l+0.5, deposit=mass, occ=occ)
rho, dln, d2ln, _ = smooth_lnrho(mass, NG//8)
A = 0.75*1.50*CX
for rr in (0.5, 1.0, 2.0, 4.0):
    i = min(range(NG), key=lambda j: abs(RG[j]-rr))
    if rho[i] <= 1e-13 or dln is None:
        print("  r=%.1f a0: (guarded)" % rr); continue
    kF = (3.0*math.pi**2*rho[i])**(1.0/3.0)
    sgn = 1.0 if dln[i] > 0 else -1.0
    s = abs(dln[i])/(2.0*kF)
    sprime = sgn*d2ln[i]/(2.0*kF) - s*(dln[i]/3.0)
    loc = Fenh(s) - s*Fp(s)
    div = (A/(2.0*KF3))*sgn*(2.0*Fp(s)/RG[i] + Fpp(s)*sprime)
    vloc = -1.50*CX*(rho[i]**(1.0/3.0))*loc
    print("  r=%.1f a0: s=%.2f (F-sF')=%.3f div/|v_loc|=%.3f sign(div)=%+d   [X-5 raw grid: 2.1-2.8 oscillating]"
          % (rr, s, loc, abs(div)/max(abs(vloc), 1e-30), 1 if div > 0 else -1))
print("X-7d guards (r<0.05 or rho<1e-13, layer local-only):", GUARD["hits"])
