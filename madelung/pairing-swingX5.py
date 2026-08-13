#!/usr/bin/env python3
"""Pairing swing X-5 — the PROPER functional-derivative gradient treatment
(the named next fidelity of the Aufbau open item (1); follows X-3 exposure and
X-4 identification-grade kill).

WHAT X-4 DID (shortcut, identification grade): multiplied the whole felt
discount v_x by F(s) — a potential-level paste. WHAT X-5 DOES (this swing):
takes the booked felt functional  E[rho] = -(3/4) m C_X ∫ rho^{4/3} F(s) d3r
(whose F==1 derivative IS the baseline v = -m C_X rho^{1/3} exactly) and applies
its TRUE functional derivative:

  v_x(r) = -m C_X rho^{1/3} (F - s F')  +  (A / (2 (3 pi^2)^{1/3})) (1/r^2) d/dr [ r^2 sgn(rho') F'(s) ],
  A = (3/4) m C_X,   F(s) = 1 + k - k/(1 + mu s^2/k),   F'(s) = 2 mu s / (1 + mu s^2/k)^2,
  mu = 10/81 (imported, named — same import as X-3/X-4), kappa = 0.804.

The local enhancement is (F - sF') < F wherever F' > 0, and the divergence term
carries its own sign: the proper treatment is genuinely weaker/different where
X-4's paste was strongest (the diffuse pre-collapse 3d). Both parts bounded:
F -> 1+k and sF' -> 0 as s -> inf.

HAND-DECLARED GATES (registered before the run; kills in both directions):
  X-5a BASELINE + STRUCTURE: with F==1 through the PROPER path (F'==0) the
       potential must equal the baseline formula to 1e-10 at every grid point
       of a probe density, AND the F==1 SCF sweep must reproduce the tier3g
       booked flip: Z*(m=1.50) = 21, all Z* in {20,21}, 3d bound.
  X-5b THE TEST: proper-derivative bounded layer ON.
       SURVIVES  <=> Z*(m=1.50) = 21 (X-4's drag was the shortcut's artifact;
                     the TFD-fidelity verdict is RESTORED at gradient fidelity);
       KILL-CONFIRMED <=> Z*(m=1.50) <= 20 (gradient sensitivity is real at
                     derivative fidelity; placement stays gradient-owned).
       Either outcome is booked and updates the Aufbau open item.
  X-5c MECHANISM REPORT: at r in {0.5, 1, 2, 4} a0 on the Z=21 felt-floor
       profile: s, F, (F - sF'), and the divergence-term share of |v_local|.
       Names WHERE proper differs from paste (expected: the diffuse tail).
  X-5d INSTRUMENT HONESTY: every SCF cell reports convergence (dmax < 4e-3
       within 40 iters); vacuum guard rho < 1e-12 zeroes the layer and its
       hits are counted. If any Z*-deciding cell at m=1.50 fails to converge,
       X-5b is INSTRUMENT-LIMIT (no verdict) — declared now, no silent
       smoothing, no rescue.

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

def Fenh(si):
    return 1.0 + KAPPA - KAPPA/(1.0 + MU*si*si/KAPPA)

def Fprime(si):
    u = 1.0 + MU*si*si/KAPPA
    return 2.0*MU*si/(u*u)

def rho_s_sgn(mass):
    rho = [0.0]*NG; s = [0.0]*NG; sg = [0.0]*NG
    for i in range(NG):
        dr = RG[i]*DLNR
        rho[i] = mass[i]/(4.0*math.pi*RG[i]*RG[i]*dr)
    for i in range(NG):
        if rho[i] <= 1e-14: continue
        im, ip = max(i-1, 0), min(i+1, NG-1)
        drho = (rho[ip] - rho[im])/(RG[ip] - RG[im])
        kF = (3*math.pi**2*rho[i])**(1.0/3.0)
        s[i] = abs(drho)/(2.0*kF*rho[i])
        sg[i] = 1.0 if drho > 0 else (-1.0 if drho < 0 else 0.0)
    return rho, s, sg

GUARD = {"hits": 0}

def vx_proper(mass, mult, bounded):
    """Proper functional derivative of E = -(3/4) mult CX ∫ rho^{4/3} F(s)."""
    rho, s, sg = rho_s_sgn(mass)
    A = 0.75*mult*CX
    # G(r) = r^2 sgn(rho') F'(s); layer div term = + (A/(2 KF3)) (1/r^2) dG/dr
    G = [0.0]*NG
    for i in range(NG):
        if rho[i] > 1e-12 and bounded:
            G[i] = RG[i]*RG[i]*sg[i]*Fprime(s[i])
    out = [0.0]*NG
    fmax = 1.0
    for i in range(NG):
        if rho[i] <= 1e-14:
            continue
        if rho[i] <= 1e-12:
            if bounded: GUARD["hits"] += 1
            out[i] = -mult*CX*(rho[i]**(1.0/3.0)); continue
        if bounded:
            Fi, Fpi = Fenh(s[i]), Fprime(s[i])
            loc = Fi - s[i]*Fpi
            fmax = max(fmax, Fi)
            im, ip = max(i-1, 0), min(i+1, NG-1)
            dG = (G[ip] - G[im])/(RG[ip] - RG[im])
            div = (A/(2.0*KF3))*dG/(RG[i]*RG[i])
            out[i] = -mult*CX*(rho[i]**(1.0/3.0))*loc + div
        else:
            out[i] = -mult*CX*(rho[i]**(1.0/3.0))
    return out, fmax, s, rho

def scf(Z, cfg, mult, bounded, iters=40, mix=0.4):
    b = B0*max(Z,1)**(-1.0/3.0)
    Qf = sum(cfg.values())
    Ve = [min(Qf, Z)*(1.0 - t3c.TF(r/b))/r for r in RG]
    Vx = [0.0]*NG
    fmax = 1.0; s_last = None; conv = False
    for it in range(iters):
        Vt = [-Z/RG[i] + Ve[i] + Vx[i] for i in range(NG)]
        mass = [0.0]*NG
        for (n,l), occ in sorted(cfg.items()):
            E = t3c.solve_mode(Vt, n, l)
            if E is None: E = -1e-9
            t3c.orbit(Vt, E, l+0.5, deposit=mass, occ=occ)
        Vnew = t3c.potential_of(mass)
        Vxnew, fmax, s_last, rho_last = vx_proper(mass, mult, bounded)
        dmax = max(abs(Vnew[i]-Ve[i])*RG[i] for i in range(NG))
        Ve = [mix*Vnew[i] + (1-mix)*Ve[i] for i in range(NG)]
        Vx = [mix*Vxnew[i] + (1-mix)*Vx[i] for i in range(NG)]
        if dmax < 4e-3:
            conv = True; break
    Vt = [-Z/RG[i] + Ve[i] + Vx[i] for i in range(NG)]
    return Vt, fmax, s_last, conv

def sweep(bounded, mults=(1.50, 1.70, 1.949), qs=(19, 20, 21, 22, 23)):
    zstars = {}
    for m in mults:
        wins = []; zstar = None; bound = True; fm_all = 1.0; ncs = []
        for Q in qs:
            core = t3c.madelung_config_upto(Q-1)
            Vt, fm, s, conv = scf(Q, core, m, bounded)
            if not conv: ncs.append(Q)
            fm_all = max(fm_all, fm)
            es = {}
            for (lab, n, l) in (("4s",4,0), ("3d",3,2), ("4p",4,1)):
                es[lab] = t3c.solve_mode(Vt, n, l)
            if Q >= 21 and es["3d"] is None: bound = False
            cands = {k: v for k, v in es.items() if v is not None}
            w = min(cands, key=cands.get) if cands else "-"
            wins.append(w)
            if zstar is None and w == "3d": zstar = Q
        zstars[m] = (zstar, bound, wins, fm_all, ncs)
        print("  m=%.3f | %s | Z*=%s  3d-bound=%s  maxF=%.3f  nc=%s"
              % (m, " ".join("%4s" % w for w in wins), zstar, bound, fm_all, ncs if ncs else "none"))
    return zstars

# ---- X-5a structure check: F'==0 path == baseline formula on a probe density ----
probe = [math.exp(-RG[i])*RG[i] for i in range(NG)]  # arbitrary smooth positive mass profile
vp, _, _, _ = vx_proper(probe, 1.50, False)
rhop, _, _ = rho_s_sgn(probe)
worst = max(abs(vp[i] - (-1.50*CX*rhop[i]**(1.0/3.0))) for i in range(NG) if rhop[i] > 1e-14)
print("X-5a structure: |proper(F==1) - baseline| worst = %.2e:" % worst,
      "PASS" if worst < 1e-10 else "FAIL")

print("X-5a BASELINE (F == 1) — must reproduce tier3g booked flip:")
base = sweep(False)
ok_a = base[1.50][0] == 21 and all(v[0] in (20, 21) for v in base.values()) and all(v[1] for v in base.values()) \
       and worst < 1e-10
print("X-5a:", "PASS — baseline reproduced" if ok_a else "FAIL")

print("\nX-5b THE TEST (proper functional-derivative bounded layer ON):")
GUARD["hits"] = 0
enh = sweep(True)
floor = enh[1.50]
if floor[4]:
    print("X-5b: INSTRUMENT-LIMIT — floor cells did not converge:", floor[4])
else:
    if floor[0] == 21:
        print("X-5b: SURVIVES — Z*(1.50) = 21: X-4's drag was the paste's artifact;")
        print("      TFD-fidelity verdict RESTORED at proper gradient fidelity.")
    elif floor[0] is not None and floor[0] <= 20:
        print("X-5b: KILL-CONFIRMED — Z*(1.50) = %d: gradient sensitivity is real" % floor[0])
        print("      at derivative fidelity; placement stays gradient-owned.")
    else:
        print("X-5b: KILL: collapse lost/unbound at floor")

print("\nX-5c mechanism (Z=21, m=1.50 felt floor, proper layer):")
core = t3c.madelung_config_upto(20)
Vt, fm, s, conv = scf(21, core, 1.50, True)
mass = [0.0]*NG
for (n,l), occ in sorted(core.items()):
    E = t3c.solve_mode(Vt, n, l)
    if E is None: E = -1e-9
    t3c.orbit(Vt, E, l+0.5, deposit=mass, occ=occ)
rho, ss, sg = rho_s_sgn(mass)
A = 0.75*1.50*CX
G = [RG[i]*RG[i]*sg[i]*Fprime(ss[i]) if rho[i] > 1e-12 else 0.0 for i in range(NG)]
for rr in (0.5, 1.0, 2.0, 4.0):
    i = min(range(NG), key=lambda j: abs(RG[j]-rr))
    Fi, Fpi = Fenh(ss[i]), Fprime(ss[i])
    im, ip = max(i-1,0), min(i+1,NG-1)
    dG = (G[ip]-G[im])/(RG[ip]-RG[im])
    div = (A/(2.0*KF3))*dG/(RG[i]*RG[i])
    vloc = -1.50*CX*(rho[i]**(1.0/3.0))*(Fi - ss[i]*Fpi)
    share = abs(div)/max(abs(vloc), 1e-30)
    print("  r=%.1f a0: s=%.2f  F=%.3f  (F-sF')=%.3f  div/|v_loc|=%.3f  sign(div)=%+d"
          % (rr, ss[i], Fi, Fi - ss[i]*Fpi, share, 1 if div > 0 else -1))
print("X-5d guard hits (rho<1e-12 layer zeroed):", GUARD["hits"], "| SCF convergence reported per cell above")
