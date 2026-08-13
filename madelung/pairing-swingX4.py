#!/usr/bin/env python3
"""Pairing swing X-4 — bounded-enhancement d-collapse re-run. Registration: 5396a66.
F(s) = 1 + k - k/(1 + mu s^2 / k), mu = 10/81, kappa = 0.804 (imported, named),
applied to the same-sense discount potential v_x (felt-booking analog; identification
grade). Baseline F==1 must reproduce tier3g's booked flip; then the test sweep.
Run from workspace root."""
import math, sys
from importlib import util as _u
spec = _u.spec_from_file_location("t3c", "memory/poams-audit/tier3c.py")
t3c = _u.module_from_spec(spec); sys.modules["t3c"] = t3c
spec.loader.exec_module(t3c)

NG, RG, DLNR, B0 = t3c.NG, t3c.RG, t3c.DLNR, t3c.B0
CX = (3.0/math.pi)**(1.0/3.0)
MU = 10.0/81.0
KAPPA = 0.804

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

def Fenh(si):
    return 1.0 + KAPPA - KAPPA/(1.0 + MU*si*si/KAPPA)

def vx(mass, mult, bounded):
    rho, s = rho_and_s(mass)
    out = [0.0]*NG
    fmax = 1.0
    for i in range(NG):
        if rho[i] > 0:
            F = Fenh(s[i]) if bounded else 1.0
            fmax = max(fmax, F)
            out[i] = -mult*CX*(rho[i]**(1.0/3.0))*F
    return out, fmax, s, rho

def scf(Z, cfg, mult, bounded, iters=30, mix=0.4):
    b = B0*max(Z,1)**(-1.0/3.0)
    Qf = sum(cfg.values())
    Ve = [min(Qf, Z)*(1.0 - t3c.TF(r/b))/r for r in RG]
    Vx = [0.0]*NG
    fmax = 1.0; s_last = None; rho_last = None
    for it in range(iters):
        Vt = [-Z/RG[i] + Ve[i] + Vx[i] for i in range(NG)]
        mass = [0.0]*NG
        for (n,l), occ in sorted(cfg.items()):
            E = t3c.solve_mode(Vt, n, l)
            if E is None: E = -1e-9
            t3c.orbit(Vt, E, l+0.5, deposit=mass, occ=occ)
        Vnew = t3c.potential_of(mass)
        Vxnew, fmax, s_last, rho_last = vx(mass, mult, bounded)
        dmax = max(abs(Vnew[i]-Ve[i])*RG[i] for i in range(NG))
        Ve = [mix*Vnew[i] + (1-mix)*Ve[i] for i in range(NG)]
        Vx = [mix*Vxnew[i] + (1-mix)*Vx[i] for i in range(NG)]
        if dmax < 4e-3: break
    Vt = [-Z/RG[i] + Ve[i] + Vx[i] for i in range(NG)]
    return Vt, fmax, s_last

def sweep(bounded, mults=(1.50, 1.70, 1.949), qs=(19, 20, 21, 22, 23)):
    zstars = {}
    for m in mults:
        wins = []; zstar = None; bound = True; fm_all = 1.0
        for Q in qs:
            core = t3c.madelung_config_upto(Q-1)
            Vt, fm, s = scf(Q, core, m, bounded)
            fm_all = max(fm_all, fm)
            es = {}
            for (lab, n, l) in (("4s",4,0), ("3d",3,2), ("4p",4,1)):
                es[lab] = t3c.solve_mode(Vt, n, l)
            if Q >= 21 and es["3d"] is None: bound = False
            cands = {k: v for k, v in es.items() if v is not None}
            w = min(cands, key=cands.get) if cands else "-"
            wins.append(w)
            if zstar is None and w == "3d": zstar = Q
        zstars[m] = (zstar, bound, wins, fm_all)
        print("  m=%.3f | %s | Z*=%s  3d-bound=%s  maxF=%.3f"
              % (m, " ".join("%4s" % w for w in wins), zstar, bound, fm_all))
    return zstars

print("X-4a BASELINE (F == 1) — must reproduce tier3g booked flip:")
base = sweep(False)
ok_a = base[1.50][0] == 21 and all(v[0] in (20, 21) for v in base.values()) and all(v[1] for v in base.values())
print("X-4a:", "PASS — baseline reproduced (floor Z*=21, all in {20,21}, 3d bound)" if ok_a else "FAIL")

print("\nX-4b THE TEST (bounded enhancement ON):")
enh = sweep(True)
ok_b = enh[1.50][0] == 21 and all(v[0] in (20, 21) for v in enh.values()) and all(v[1] for v in enh.values())
print("X-4b:", "PASS — VERDICT SURVIVES the bounded gradient layer" if ok_b else
      ("KILL: collapse dragged into Ca" if enh[1.50][0] and enh[1.50][0] <= 20 else "KILL: collapse lost/unbound"))

print("\nX-4c report: max F reached %.3f (bound 1.804);" % max(v[3] for v in enh.values()))
# F at scoring radii for Z=21 felt floor
core = t3c.madelung_config_upto(20)
Vt, fm, s = scf(21, core, 1.50, True)
for rr in (0.5, 1.0, 2.0, 4.0):
    i = min(range(NG), key=lambda j: abs(RG[j]-rr))
    print("  r=%.1f a0: s=%.2f  F=%.3f" % (rr, s[i], Fenh(s[i])))
