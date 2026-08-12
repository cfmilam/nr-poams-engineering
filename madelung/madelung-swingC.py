#!/usr/bin/env python3
# Madelung swing M-C — THE INTERIOR INEQUALITY, END TO END. Registration: 9543b00 (pre-run).
# Four-piece exact-rational certificate: chain extension + exp-free pairing + Pade closure
# bound + endpoint pieces. Zero floats in the verification layer.
from fractions import Fraction as Fr
import numpy as np, math

# ================= construction guide (floats; verification is exact) =================
LAM = (7 + math.sqrt(73))/2
C2 = 3*LAM/(6*LAM - 28)
EPS_START = 0.05
phi_start = 12 - LAM*EPS_START + C2*EPS_START*EPS_START
def Gf(t, p): return p*(3.0 - t)/(2.0*(t + t*t - p))
hB = 1e-5
tg = 2.95; pg = phi_start
TT = [tg]; PP = [pg]
nB = int(round((2.95 - 0.05)/hB))          # go all the way down to t = 0.05
for i in range(nB):
    k1 = Gf(tg, pg); k2 = Gf(tg - 0.5*hB, pg - 0.5*hB*k1)
    k3 = Gf(tg - 0.5*hB, pg - 0.5*hB*k2); k4 = Gf(tg - hB, pg - hB*k3)
    pg = pg - (hB/6.0)*(k1 + 2*k2 + 2*k3 + k4)
    tg = tg - hB
    if i % 20 == 0: TT.append(tg); PP.append(pg)
TT.append(tg); PP.append(pg)
TT = np.array(TT[::-1]); PP = np.array(PP[::-1])
def phi_num(t): return float(np.interp(t, TT, PP))
print("guide: phi(1) = %.9f (M-B booked 1.4673197); phi(0.1) = %.6f" % (phi_num(1.0), phi_num(0.1)))

# ================= exact chain: [0.1, 1] extension + [1, 2.95] rebuild =================
H = Fr(1, 200); DEC = 10**6
T0 = Fr(1, 10); TJ = Fr(59, 20)            # 0.1 .. 2.95
NSEG = int((TJ - T0)/H)                    # 570
K1 = Fr(153, 20); K2 = Fr(78, 10); EPS0 = Fr(1, 20)

def DELTA(t):
    # M-B's verified grading: 0.002 flat, ramp to 0.004 across [2.7, 2.9]
    if t <= 2.7: return 0.002
    if t >= 2.9: return 0.004
    return 0.002 + 0.002*(t - 2.7)/0.2

fails = []
def chk(name, cond):
    if not cond: fails.append(name)

chk("saddle-U-eigen", (2*K1 - 7)**2 < 73)
chk("saddle-L-eigen", (2*K2 - 7)**2 > 73)
chk("saddle-U-window", 12 - 2*K1*(K1 - 7) > 3*K1*EPS0)
chk("saddle-L-window", 12 - 2*K2*(K2 - 7) < 0)

ts = [T0 + j*H for j in range(NSEG + 1)]
Uv = []; Lv = []
for tq in ts:
    ft = float(tq); p = phi_num(ft); d = DELTA(ft)
    Uv.append(Fr(math.ceil((p + d)*DEC), DEC))
    Lv.append(Fr(math.floor((p - d)*DEC), DEC))
Uv[-1] = 12 - K1*EPS0; Lv[-1] = 12 - K2*EPS0

def quad_range(c2, c1, c0, a, b):
    va = c2*a*a + c1*a + c0; vb = c2*b*b + c1*b + c0
    lo, hi = min(va, vb), max(va, vb)
    if c2 != 0:
        tv = -c1/(2*c2)
        if a < tv < b:
            vv = c2*tv*tv + c1*tv + c0
            lo, hi = min(lo, vv), max(hi, vv)
    return lo, hi

gapmm = []   # per segment: (gapU_lo, gapU_hi, gapL_lo, gapL_hi) for m-extrema and integrals
for j in range(NSEG):
    ta, tb = ts[j], ts[j+1]
    seg_g = {}
    for (W0, W1, upper) in ((Uv[j], Uv[j+1], True), (Lv[j], Lv[j+1], False)):
        b = (W1 - W0)/(tb - ta)
        w0 = W0 - b*ta
        glo, ghi = quad_range(Fr(1), 1 - b, -w0, ta, tb)   # N - W range
        chk("gap seg%d %s" % (j, "U" if upper else "L"), glo > 0)
        c2p = -3*b
        c1p = 3*b - w0 - 2*b*(1 - b)
        c0p = (3 + 2*b)*w0
        plo, phi_ = quad_range(c2p, c1p, c0p, ta, tb)
        if upper: chk("P>0 seg%d U" % j, plo > 0); seg_g['U'] = (glo, ghi)
        else:     chk("P<0 seg%d L" % j, phi_ < 0); seg_g['L'] = (glo, ghi)
    gapmm.append(seg_g)

print("chain: %d segments; failures so far: %d" % (NSEG, len(fails)))
if fails: print("  ", fails[:10])

# ================= exact m-brackets per segment: m = N - phi in [N-U, N-L] ============
# m_lo over segment = min(N - U) = gapU_lo ; m_hi = max(N - L) = gapL_hi.
def rdown(x, den=10**9): return Fr(math.floor(x*den), den)
def rup(x, den=10**9):   return Fr(math.ceil(x*den), den)

# ================= D-brackets (log-level drops), exp-free =============================
# eye face: D(t_j) = int_{t_j}^{1} (1-t)/m dt ; outer: D_out(t_j) = int_1^{t_j} (t-1)/m dt
NSUB = 4
i_peak = int((Fr(1) - T0)/H)   # index of t = 1
Dlo = [Fr(0)]*(NSEG + 1); Dhi = [Fr(0)]*(NSEG + 1)
# eye side: accumulate from t=1 leftward
for j in range(i_peak - 1, -1, -1):
    ta, tb = ts[j], ts[j+1]
    m_lo, _ = gapmm[j]['U']; _, m_hi = gapmm[j]['L']
    add_lo = Fr(0); add_hi = Fr(0)
    for k in range(NSUB):
        sa = ta + (tb - ta)*k/NSUB; sb = ta + (tb - ta)*(k+1)/NSUB
        I = (sb - sa)*(1 - (sa + sb)/2)          # exact integral of (1-t) over [sa,sb]
        add_lo += I/m_hi; add_hi += I/m_lo
    Dlo[j] = rdown(Dlo[j+1] + add_lo); Dhi[j] = rup(Dhi[j+1] + add_hi)
# outer side: accumulate from t=1 rightward
DOlo = [Fr(0)]*(NSEG + 1); DOhi = [Fr(0)]*(NSEG + 1)
for j in range(i_peak, NSEG):
    ta, tb = ts[j], ts[j+1]
    m_lo, _ = gapmm[j]['U']; _, m_hi = gapmm[j]['L']
    add_lo = Fr(0); add_hi = Fr(0)
    for k in range(NSUB):
        sa = ta + (tb - ta)*k/NSUB; sb = ta + (tb - ta)*(k+1)/NSUB
        I = (sb - sa)*((sa + sb)/2 - 1)          # exact integral of (t-1)
        add_lo += I/m_hi; add_hi += I/m_lo
    DOlo[j+1] = rdown(DOlo[j] + add_lo); DOhi[j+1] = rup(DOhi[j] + add_hi)

print("D-brackets: eye D(0.1) in [%.5f, %.5f] (width %.4f); outer D(2.5) in [%.5f, %.5f]"
      % (Dlo[0], Dhi[0], float(Dhi[0]-Dlo[0]),
         DOlo[int((Fr(5,2)-T0)/H)], DOhi[int((Fr(5,2)-T0)/H)]))

# ================= pairing: tau_min per eye breakpoint ================================
def tau_min_for(Dlo_t):
    """largest breakpoint tau' with DOhi(tau') <= Dlo_t (D_out increasing)."""
    lo, hi = i_peak, NSEG
    if DOhi[NSEG] <= Dlo_t: return ts[NSEG]
    while hi - lo > 1:
        mid = (lo + hi)//2
        if DOhi[mid] <= Dlo_t: lo = mid
        else: hi = mid
    return ts[lo]

# ================= MIDDLE PIECE: interval checks on [t0, t1] ==========================
T1 = Fr(9, 10)
i_t1 = int((T1 - T0)/H)
mid_fails = 0; worst_margin = None
for j in range(0, i_t1):                       # intervals [ts[j], ts[j+1]] cover [0.1, 0.9]
    tb = ts[j+1]
    Dl = Dlo[j+1]                              # D decreasing in t: for t <= tb, D >= Dlo(tb)
    tmin = tau_min_for(Dl)
    S_sum = 1/(1 - tb) + 1/(tmin - 1)
    # sufficient: SUM <= 2/sqrt(1-v), 1-v >= (D + D^2/2)/(1 + D + D^2/2)
    #   <=>  SUM^2 * (D + D^2/2) <= 4 * (1 + D + D^2/2)
    lhs = S_sum*S_sum*(Dl + Dl*Dl/2)
    rhs = 4*(1 + Dl + Dl*Dl/2)
    ok = lhs <= rhs
    if not ok:
        mid_fails += 1
        if mid_fails <= 6: print("  MIDDLE FAIL at interval right end t=%.3f" % float(tb))
    marg = float(1 - lhs/rhs)
    if worst_margin is None or marg < worst_margin[0]: worst_margin = (marg, float(tb))
chk("middle piece", mid_fails == 0)
print("middle piece: %d intervals, %d failures; worst margin %.3f at t=%.3f"
      % (i_t1, mid_fails, worst_margin[0], worst_margin[1]))

# ================= EYE PIECE: one check at t0 =========================================
tmin0 = tau_min_for(Dlo[0])
eye_sum = 1/(1 - T0) + 1/(tmin0 - 1)
chk("eye piece", eye_sum <= 2)
print("eye piece: 1/(1-t0) + 1/(tau_min-1) = %.5f <= 2:" % float(eye_sum),
      "PASS (tau_min = %.3f, margin %.1f%%)" % (float(tmin0), 100*float(1 - eye_sum/2))
      if eye_sum <= 2 else "FAIL")

# ================= PEAK PIECE: [t1, 1) ================================================
# m extrema over eye window [t1, 1]; M extrema over outer window [1, 1+DLT]
DLT = Fr(3, 20)   # outer window width 0.15; self-consistency checked below
i_out = int((Fr(1) + DLT - T0)/H)
m_min = None; m_max = None
for j in range(i_t1, i_peak):
    glo, _ = gapmm[j]['U']; _, ghi = gapmm[j]['L']
    m_min = glo if m_min is None else min(m_min, glo)
    m_max = ghi if m_max is None else max(m_max, ghi)
M_min = None; M_max = None
for j in range(i_peak, i_out):
    glo, _ = gapmm[j]['U']; _, ghi = gapmm[j]['L']
    M_min = glo if M_min is None else min(M_min, glo)
    M_max = ghi if M_max is None else max(M_max, ghi)
r = m_max/M_min
peak_ok = (3 + r)**2 <= 32*m_min
chk("peak piece", peak_ok)
print("peak piece: m in [%.5f, %.5f] on [0.9,1]; M_min %.5f on [1,1.15]; r = %.5f" %
      (m_min, m_max, M_min, r))
print("  (3+r)^2 = %.5f <= 32*m_min = %.5f:" % (float((3+r)**2), float(32*m_min)),
      "PASS (margin %.2f%%)" % (100*float(1 - (3+r)**2/(32*m_min))) if peak_ok else "FAIL")
# self-consistency: tau(t1) - 1 <= (1-t1) sqrt(M_max/m_min) <= DLT  <=  check squared
sc_ok = (1 - T1)**2 * M_max <= DLT*DLT*m_min
chk("peak window self-consistency", sc_ok)
print("  outer-window self-consistency (0.1^2 M_max <= 0.15^2 m_min):", "PASS" if sc_ok else "FAIL")

# ================= verdict ============================================================
n_checks = 4 + 2*NSEG*2 + 3 + i_t1
print("\nTOTAL exact checks: %d; failures: %d" % (n_checks, len(fails)))
if not fails:
    print("G-C1 PASS (chain, %d segments incl. extension)" % NSEG)
    print("G-C2 PASS — THE INTERIOR INEQUALITY sigma_hat >= sigma* IS A THEOREM on (0,1)")
    print("  (eye piece + middle intervals + peak piece + chain certificates;")
    print("   modulo the two named classical imports of M-B)")
else:
    print("G-C2 FAIL — gaps at:", fails[:12])

# G-C3 consistency spot rows vs M-A numeric profile
print("\nG-C3 spot rows (D-bracket vs M-A numeric v = e^-D):")
for tv in (0.14, 0.5, 0.74):
    j = int((Fr(*float(tv).as_integer_ratio()) - T0)/H) if False else int(round((tv - 0.1)/0.005))
    print("  t=%.2f: D in [%.5f, %.5f] -> v in [%.5f, %.5f]"
          % (tv, Dlo[j], Dhi[j], math.exp(-float(Dhi[j])), math.exp(-float(Dlo[j]))))
