#!/usr/bin/env python3
"""Pairing swing X-6 — first-order ENERGY booking of the bounded gradient layer
(the honest fidelity between X-4's potential paste and X-5's instrument-limited
proper derivative).

WHY: X-5 established (a) the proper LOCAL part (F - sF') sits BELOW 1 in the
collapse region (opposite X-4's paste) and (b) the divergence term cannot be
evaluated honestly on the deposit grid (2nd derivatives of a noisy density).
The energy functional needs only FIRST derivatives: book the layer at first
order instead.

METHOD (zero new imports; mu = 10/81, kappa = 0.804 as X-3/X-4/X-5):
  At each flip-deciding cell (Q, m): converge the BASELINE SCF (F == 1, the
  booked tier3g chassis, untouched physics). In that one frozen potential,
  build the two competing total densities at fixed modes:
      rho_A = core(Q-1) + one quantum in 4s
      rho_B = core(Q-1) + one quantum in 3d
  and price the gradient layer's energy on each:
      E_grad[rho] = -(3/4) m C_X INT rho^{4/3} (F(s) - 1) d3r.
  First-order preference of the layer:
      D(Q, m) = ( eps_4s + E_grad[rho_A] ) - ( eps_3d + E_grad[rho_B] )
  vs the baseline preference D0 = eps_4s - eps_3d. The LAYER's push is
  dD = D - D0 = E_grad[rho_A] - E_grad[rho_B]:
      dD > 0  -> the layer taxes the 4s filling harder  -> pushes TOWARD 3d
                 (the drag direction: kill-confirming at first order)
      dD < 0  -> the layer taxes the 3d filling harder  -> protects 4s
                 (the verdict-restoring direction)
  and the FLIP test: does D change sign relative to D0 at any deciding cell?

HAND-DECLARED GATES (registered pre-run; kills in both directions):
  X-6a FIDELITY: baseline SCF must reproduce the tier3g flip on the same
       sweep (Z*(1.50) = 21, all Z* in {20,21}, 3d bound, deciding cells
       converged) — else STOP, no score.
  X-6b THE SIGN: at the flip-deciding cells (Q = 20 and Q = 21, all three m):
       report dD sign.  UNIFORM dD > 0 across cells -> X-4's drag direction is
       CONFIRMED at first-order energy fidelity (paste artifact hypothesis
       dies); UNIFORM dD < 0 -> the paste direction REVERSES at energy
       fidelity (4s protected; TFD verdict restored at first order); mixed
       signs -> booked as cell-dependent, no clean owner, both named.
  X-6c THE FLIP: does eps + E_grad flip any deciding cell's winner relative
       to baseline? Report the effective Z* under first-order booking per m
       (floor m = 1.50 is the verdict line, as booked).
  X-6d MAGNITUDE HONESTY: |dD| vs |D0| per cell — a first-order booking is
       only claimable while |dD| is not >> the baseline gap scale; cells with
       |dD| > 5 |D0| are flagged 'beyond first order' and excluded from the
       X-6c verdict line (declared now). Also reported: the layer integral's
       s-histogram sanity (share of E_grad accrued at s > 3, where the
       bounded form saturates).

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

def Fenh(si):
    return 1.0 + KAPPA - KAPPA/(1.0 + MU*si*si/KAPPA)

def rho_of(mass):
    rho = [0.0]*NG
    for i in range(NG):
        dr = RG[i]*DLNR
        rho[i] = mass[i]/(4.0*math.pi*RG[i]*RG[i]*dr)
    return rho

def s_of(rho):
    s = [0.0]*NG
    for i in range(NG):
        if rho[i] <= 1e-14: continue
        im, ip = max(i-1, 0), min(i+1, NG-1)
        drho = (rho[ip] - rho[im])/(RG[ip] - RG[im])
        kF = (3*math.pi**2*rho[i])**(1.0/3.0)
        s[i] = abs(drho)/(2.0*kF*rho[i])
    return s

def E_grad(rho, mult):
    """-(3/4) mult CX INT rho^{4/3}(F(s)-1) d3r on the log grid; also s>3 share."""
    s = s_of(rho)
    tot = 0.0; hi = 0.0
    for i in range(NG):
        if rho[i] <= 1e-12: continue
        dV = 4.0*math.pi*RG[i]*RG[i]*RG[i]*DLNR
        w = -(0.75*mult*CX)*(rho[i]**(4.0/3.0))*(Fenh(s[i]) - 1.0)*dV
        tot += w
        if s[i] > 3.0: hi += w
    share = (hi/tot) if tot != 0 else 0.0
    return tot, share

def scf_baseline(Z, cfg, mult, iters=40, mix=0.4):
    b = B0*max(Z,1)**(-1.0/3.0)
    Qf = sum(cfg.values())
    Ve = [min(Qf, Z)*(1.0 - t3c.TF(r/b))/r for r in RG]
    Vx = [0.0]*NG
    conv = False
    for it in range(iters):
        Vt = [-Z/RG[i] + Ve[i] + Vx[i] for i in range(NG)]
        mass = [0.0]*NG
        for (n,l), occ in sorted(cfg.items()):
            E = t3c.solve_mode(Vt, n, l)
            if E is None: E = -1e-9
            t3c.orbit(Vt, E, l+0.5, deposit=mass, occ=occ)
        Vnew = t3c.potential_of(mass)
        rho = rho_of(mass)
        Vxnew = [-mult*CX*(rho[i]**(1.0/3.0)) if rho[i] > 0 else 0.0 for i in range(NG)]
        dmax = max(abs(Vnew[i]-Ve[i])*RG[i] for i in range(NG))
        Ve = [mix*Vnew[i] + (1-mix)*Ve[i] for i in range(NG)]
        Vx = [mix*Vxnew[i] + (1-mix)*Vx[i] for i in range(NG)]
        if dmax < 4e-3:
            conv = True; break
    Vt = [-Z/RG[i] + Ve[i] + Vx[i] for i in range(NG)]
    return Vt, conv

MULTS = (1.50, 1.70, 1.949)
QS = (19, 20, 21, 22, 23)

# ---- X-6a fidelity sweep ----
print("X-6a FIDELITY (baseline chassis, F == 1):")
fid_ok = True
Vts = {}
for m in MULTS:
    wins = []; zstar = None; bound = True; ncs = []
    for Q in QS:
        core = t3c.madelung_config_upto(Q-1)
        Vt, conv = scf_baseline(Q, core, m)
        Vts[(Q, m)] = Vt
        if not conv: ncs.append(Q)
        es = {}
        for (lab, n, l) in (("4s",4,0), ("3d",3,2), ("4p",4,1)):
            es[lab] = t3c.solve_mode(Vt, n, l)
        if Q >= 21 and es["3d"] is None: bound = False
        cands = {k: v for k, v in es.items() if v is not None}
        w = min(cands, key=cands.get) if cands else "-"
        wins.append(w)
        if zstar is None and w == "3d": zstar = Q
    print("  m=%.3f | %s | Z*=%s  3d-bound=%s  nc=%s"
          % (m, " ".join("%4s" % w for w in wins), zstar, bound, ncs if ncs else "none"))
    if m == 1.50 and zstar != 21: fid_ok = False
    if zstar not in (20, 21) or not bound: fid_ok = False
    if any(q in ncs for q in (20, 21)): fid_ok = False
print("X-6a:", "PASS — scoring proceeds" if fid_ok else "FAIL — STOP (no score)")
if not fid_ok:
    raise SystemExit(1)

# ---- X-6b/c/d: first-order booking at the deciding cells ----
print("\nX-6b/c first-order energy booking at deciding cells:")
signs = []
zstar_fo = {}
for m in MULTS:
    zfo = None
    for Q in QS:
        Vt = Vts[(Q, m)]
        core = t3c.madelung_config_upto(Q-1)
        # frozen-mode densities: core + one quantum in each candidate
        built = {}
        eps = {}
        for (lab, n, l) in (("4s",4,0), ("3d",3,2)):
            E = t3c.solve_mode(Vt, n, l)
            eps[lab] = E
            mass = [0.0]*NG
            for (nn,ll), occ in sorted(core.items()):
                Ec = t3c.solve_mode(Vt, nn, ll)
                if Ec is None: Ec = -1e-9
                t3c.orbit(Vt, Ec, ll+0.5, deposit=mass, occ=occ)
            if E is not None:
                t3c.orbit(Vt, E, l+0.5, deposit=mass, occ=1)
            built[lab] = rho_of(mass)
        if eps["4s"] is None or eps["3d"] is None:
            print("  m=%.3f Q=%d: candidate unbound at baseline — cell skipped" % (m, Q))
            continue
        EgA, shA = E_grad(built["4s"], m)
        EgB, shB = E_grad(built["3d"], m)
        dD = EgA - EgB
        D0 = eps["4s"] - eps["3d"]
        D1 = D0 + dD
        w0 = "4s" if D0 < 0 else "3d"
        w1 = "4s" if D1 < 0 else "3d"
        beyond = abs(dD) > 5.0*abs(D0)
        if Q in (20, 21):
            signs.append((m, Q, dD, beyond))
        if zfo is None and w1 == "3d" and not beyond:
            zfo = Q
        flag = " BEYOND-1st-ORDER" if beyond else ""
        print("  m=%.3f Q=%2d: D0=%+.5f  dD=%+.6f  D1=%+.5f  win %s->%s  s>3 share A/B %.2f/%.2f%s"
              % (m, Q, D0, dD, D1, w0, w1, shA, shB, flag))
    zstar_fo[m] = zfo
print("X-6c effective Z* under first-order booking:", {m: zstar_fo[m] for m in MULTS},
      "(baseline booked: floor Z*=21)")

pos = [1 for (_,_,d,b) in signs if d > 0 and not b]
neg = [1 for (_,_,d,b) in signs if d < 0 and not b]
exc = [1 for (_,_,_,b) in signs if b]
if exc and not (pos or neg):
    print("X-6b: INSTRUMENT-LIMIT — all deciding cells beyond first order")
elif pos and not neg:
    print("X-6b: dD > 0 UNIFORM — layer taxes 4s harder: X-4's DRAG DIRECTION CONFIRMED at energy fidelity")
elif neg and not pos:
    print("X-6b: dD < 0 UNIFORM — layer taxes 3d harder: paste direction REVERSES; 4s protected at first order")
else:
    print("X-6b: MIXED signs — cell-dependent, no clean owner; booked as found")
print("X-6d: excluded-beyond-first-order cells:", len(exc), "of", len(signs))
