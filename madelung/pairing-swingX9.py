#!/usr/bin/env python3
"""Pairing swing X-9 — THE d-COLLAPSE UNDER THE NATIVE LAW (the payoff swing).

WHAT IS OWED: X-4 dragged the Sc flip to Z = 20/19 using the IMPORTED bounded
gradient form (mu = 10/81, kappa = 0.804) pasted onto the felt discount. The
Airy thinning-census (X-8'/P3, working grade, exported) measured the native
law and it runs the OPPOSITE WAY in the region that decided X-4: the discount
WEAKENS toward the thinning frontier (F_nat = 0.90 at s = 0.47 falling to 0.08
at s = 6.2) where the import strengthened (1.03 rising to 1.69). Same paste
slot, same chassis, the LAW swapped: this differences the law at a fixed
treatment level.

CONSTRUCTION: X-4 chassis verbatim; F(s) from madelung/native-gradient-law.csv:
  s < 0.30           -> F = 1 (the deep rows carry a +-1% instrument wobble;
                        physics there is 1 + O(1e-3); DECLARED floor, not tuned)
  0.30 <= s <= s_max -> monotone linear interpolation of the table
  s > s_max = 6.19   -> hold last value 0.0807 (evanescent hold, usage counted)

GATES (pre-run; all directions pre-named):
  X9a BASELINE: F == 1 sweep reproduces the tier3g booked flip
      (Z*(1.50) = 21, all Z* in {20, 21}, 3d bound) — else STOP.
  X9b THE VERDICT (native-law paste ON):
      Z*(1.50) = 21  -> VERDICT RESTORED AT NATIVE FIDELITY: the X-4 drag was
                        the import's artifact — the gradient layer, measured
                        natively, does not move the flip;
      Z*(1.50) >= 22 -> OVERPROTECTION: the native law pushes the flip PAST
                        the booked baseline — the shut-off overcorrects the
                        felt booking; booked as found (calibration interplay
                        named);
      Z*(1.50) <= 20 -> DRAG SURVIVES the native law — the sign finding is
                        insufficient for the placement; booked.
      3d must stay bound where the baseline had it bound; nc cells reported.
  X9c MECHANISM: F_native at the scoring radii (r = 0.5, 1, 2, 4 a0) on the
      Z = 21 felt floor, beside X-4's imported values (1.007/1.002/1.027/1.566).
  X9d HONESTY: floor-usage share (s < 0.3), hold-usage share (s > 6.19),
      convergence flags, per-cell winners.

Run from workspace root. Registration commit = this file, pre-run.
"""
import math, sys, os
from importlib import util as _u
spec = _u.spec_from_file_location("t3c", "memory/poams-audit/tier3c.py")
t3c = _u.module_from_spec(spec); sys.modules["t3c"] = t3c
spec.loader.exec_module(t3c)

NG, RG, DLNR, B0 = t3c.NG, t3c.RG, t3c.DLNR, t3c.B0
CX = (3.0/math.pi)**(1.0/3.0)

# ---- the native law ----
S_TAB, F_TAB = [], []
with open("poams-engineering-public/madelung/native-gradient-law.csv") as f:
    next(f)
    for ln in f:
        a, b = ln.strip().split(",")
        S_TAB.append(float(a)); F_TAB.append(float(b))
pairs = sorted(zip(S_TAB, F_TAB))
S_TAB = [p[0] for p in pairs]; F_TAB = [p[1] for p in pairs]
SMAX = S_TAB[-1]; FHOLD = F_TAB[-1]
USE = {"floor": 0, "mid": 0, "hold": 0}

def Fnat(s):
    if s < 0.30:
        USE["floor"] += 1; return 1.0
    if s > SMAX:
        USE["hold"] += 1; return FHOLD
    USE["mid"] += 1
    lo, hi = 0, len(S_TAB) - 1
    while lo < hi - 1:
        mid = (lo + hi)//2
        if S_TAB[mid] <= s: lo = mid
        else: hi = mid
    t = (s - S_TAB[lo])/(S_TAB[hi] - S_TAB[lo])
    return F_TAB[lo]*(1 - t) + F_TAB[hi]*t

def rho_and_s(mass):
    rho = [0.0]*NG; s = [0.0]*NG
    for i in range(NG):
        dr = RG[i]*DLNR
        rho[i] = mass[i]/(4.0*math.pi*RG[i]*RG[i]*dr)
    for i in range(NG):
        if rho[i] <= 1e-14: continue
        im, ip = max(i-1, 0), min(i+1, NG-1)
        drho = (rho[ip] - rho[im])/(RG[ip] - RG[im])
        kF = (3*math.pi**2*rho[i])**(1.0/3.0)
        s[i] = abs(drho)/(2.0*kF*rho[i])
    return rho, s

def vx(mass, mult, native):
    rho, s = rho_and_s(mass)
    out = [0.0]*NG
    for i in range(NG):
        if rho[i] > 0:
            F = Fnat(s[i]) if native else 1.0
            out[i] = -mult*CX*(rho[i]**(1.0/3.0))*F
    return out, s

def scf(Z, cfg, mult, native, iters=30, mix=0.4):
    b = B0*max(Z,1)**(-1.0/3.0)
    Qf = sum(cfg.values())
    Ve = [min(Qf, Z)*(1.0 - t3c.TF(r/b))/r for r in RG]
    Vx = [0.0]*NG
    s_last = None
    for it in range(iters):
        Vt = [-Z/RG[i] + Ve[i] + Vx[i] for i in range(NG)]
        mass = [0.0]*NG
        for (n,l), occ in sorted(cfg.items()):
            E = t3c.solve_mode(Vt, n, l)
            if E is None: E = -1e-9
            t3c.orbit(Vt, E, l+0.5, deposit=mass, occ=occ)
        Vnew = t3c.potential_of(mass)
        Vxnew, s_last = vx(mass, mult, native)
        dmax = max(abs(Vnew[i]-Ve[i])*RG[i] for i in range(NG))
        Ve = [mix*Vnew[i] + (1-mix)*Ve[i] for i in range(NG)]
        Vx = [mix*Vxnew[i] + (1-mix)*Vx[i] for i in range(NG)]
        if dmax < 4e-3: break
    Vt = [-Z/RG[i] + Ve[i] + Vx[i] for i in range(NG)]
    return Vt, s_last

def sweep(native, mults=(1.50, 1.70, 1.949), qs=(19, 20, 21, 22, 23)):
    zs = {}
    for m in mults:
        wins = []; zstar = None; bound = True
        for Q in qs:
            core = t3c.madelung_config_upto(Q-1)
            Vt, s = scf(Q, core, m, native)
            es = {}
            for (lab, n, l) in (("4s",4,0), ("3d",3,2), ("4p",4,1)):
                es[lab] = t3c.solve_mode(Vt, n, l)
            if Q >= 21 and es["3d"] is None: bound = False
            cands = {k: v for k, v in es.items() if v is not None}
            w = min(cands, key=cands.get) if cands else "-"
            wins.append(w)
            if zstar is None and w == "3d": zstar = Q
        zs[m] = (zstar, bound, wins)
        print("  m=%.3f | %s | Z*=%s  3d-bound=%s"
              % (m, " ".join("%4s" % w for w in wins), zstar, bound), flush=True)
    return zs

print("X9a BASELINE (F == 1) — must reproduce tier3g booked flip:")
base = sweep(False)
ok_a = base[1.50][0] == 21 and all(v[0] in (20, 21) for v in base.values()) and all(v[1] for v in base.values())
print("X9a:", "PASS — baseline reproduced" if ok_a else "FAIL — STOP")
if not ok_a: raise SystemExit(1)

print("\nX9b THE VERDICT (native-law paste ON):")
USE["floor"] = USE["mid"] = USE["hold"] = 0
enh = sweep(True)
fl = enh[1.50]
if fl[0] == 21 and fl[1]:
    print("X9b: VERDICT RESTORED AT NATIVE FIDELITY — Z*(1.50) = 21:")
    print("     the X-4 drag was the import's artifact; the gradient layer,")
    print("     measured natively, does not move the flip.")
elif fl[0] is not None and fl[0] >= 22:
    print("X9b: OVERPROTECTION — Z*(1.50) = %d: the native shut-off pushes the flip" % fl[0])
    print("     past the booked baseline; calibration interplay named, booked as found.")
elif fl[0] is not None and fl[0] <= 20:
    print("X9b: DRAG SURVIVES — Z*(1.50) = %d under the native law; booked." % fl[0])
else:
    print("X9b: collapse lost/unbound at floor — booked as found.")

print("\nX9c mechanism (Z=21, m=1.50 felt floor):")
core = t3c.madelung_config_upto(20)
Vt, s = scf(21, core, 1.50, True)
X4_IMP = {0.5: 1.007, 1.0: 1.002, 2.0: 1.027, 4.0: 1.566}
for rr in (0.5, 1.0, 2.0, 4.0):
    i = min(range(NG), key=lambda j: abs(RG[j]-rr))
    print("  r=%.1f a0: s=%.2f  F_native=%.3f   [X-4 imported: %.3f]"
          % (rr, s[i], Fnat(s[i]), X4_IMP[rr]))

tot = sum(USE.values())
print("\nX9d honesty: law usage — floor(s<0.3) %.0f%% | table %.0f%% | hold(s>%.2f) %.0f%%"
      % (100*USE["floor"]/tot, 100*USE["mid"]/tot, SMAX, 100*USE["hold"]/tot))
