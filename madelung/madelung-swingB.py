#!/usr/bin/env python3
# Madelung swing M-B — THE VALIDATED DIP ENCLOSURE. Registration: 3ccc992 (pre-run).
# Exact-rational barrier certificate: S = phi(1) in [L(1), U(1)], U(1) < 3/2.
# Construction float-guided; VERIFICATION pure fractions (zero floats).
from fractions import Fraction as Fr
import numpy as np, math

# ---------- construction guide: BACKWARD graph-ODE from the manifold series ----------
# (run 1 used the eye-side s-domain integration; its tail is float-contaminated near
# the saddle — the exact checks caught it. Backward-in-t is contracting: start error dies.)
LAM = (7 + math.sqrt(73))/2
C2 = 3*LAM/(6*LAM - 28)
EPS_START = 0.05
phi_start = 12 - LAM*EPS_START + C2*EPS_START*EPS_START      # 11.614528 (series, err ~1e-3 max)
def Gf(t, p):
    return p*(3.0 - t)/(2.0*(t + t*t - p))
hB = 1e-5
nB = int(round((2.95 - 1.0)/hB))
tg = 2.95; pg = phi_start
TT = [tg]; PP = [pg]
for i in range(nB):
    k1 = Gf(tg, pg); k2 = Gf(tg - 0.5*hB, pg - 0.5*hB*k1)
    k3 = Gf(tg - 0.5*hB, pg - 0.5*hB*k2); k4 = Gf(tg - hB, pg - hB*k3)
    pg = pg - (hB/6.0)*(k1 + 2*k2 + 2*k3 + k4)
    tg = tg - hB
    if i % 20 == 0:
        TT.append(tg); PP.append(pg)
TT.append(tg); PP.append(pg)
TT = np.array(TT[::-1]); PP = np.array(PP[::-1])
def phi_num(t):
    return float(np.interp(t, TT, PP))
S_num = phi_num(1.0)
print("backward guide: phi(2.95) = %.6f (series start), S_backward = %.9f" % (phi_start, S_num))
print("  two-route check: eye-side booked S = 1.467319749 -> agreement %.2e" % abs(S_num - 1.467319749))

# ---------- exact certificate ----------
K1 = Fr(153, 20); K2 = Fr(78, 10); EPS0 = Fr(1, 20)   # K1 = 7.65 (junction headroom), K2 = 7.8
TJ = Fr(3) - EPS0                    # 2.95 junction
H = Fr(1, 200)                       # segment width 0.005
NSEG = int((TJ - 1) / H)             # 390
DEC = 10**6
def DELTA(t):
    # graded: 0.002 flat, ramping smoothly to 0.004 across [2.7, 2.9] (no slope jump)
    if t <= 2.7: return 0.002
    if t >= 2.9: return 0.004
    return 0.002 + 0.002*(t - 2.7)/0.2

fails = []
def chk(name, cond):
    if not cond: fails.append(name)

# saddle checks (exact, as hand-declared)
chk("saddle-U-eigen", (2*K1 - 7)**2 < 73)
chk("saddle-L-eigen", (2*K2 - 7)**2 > 73)
chk("saddle-U-window", 12 - 2*K1*(K1 - 7) > 3*K1*EPS0)
chk("saddle-L-window", 12 - 2*K2*(K2 - 7) < 0)

# breakpoints and barrier values
ts = [Fr(1) + j*H for j in range(NSEG + 1)]      # 1 .. 2.95
Uv = []; Lv = []
for tq in ts:
    ft = float(tq)
    p = phi_num(ft); d = DELTA(ft)
    Uv.append(Fr(math.ceil((p + d)*DEC), DEC))
    Lv.append(Fr(math.floor((p - d)*DEC), DEC))
Uv[-1] = 12 - K1*EPS0     # 2323/200 = 11.615
Lv[-1] = 12 - K2*EPS0     # 1161/100 = 11.61

def quad_range(c2, c1, c0, a, b):
    """exact [min, max] of c2 t^2 + c1 t + c0 over [a, b]"""
    va = c2*a*a + c1*a + c0
    vb = c2*b*b + c1*b + c0
    lo, hi = min(va, vb), max(va, vb)
    if c2 != 0:
        tv = -c1/(2*c2)
        if a < tv < b:
            vv = c2*tv*tv + c1*tv + c0
            lo, hi = min(lo, vv), max(hi, vv)
    return lo, hi

for j in range(NSEG):
    ta, tb = ts[j], ts[j+1]
    for (W0, W1, upper) in ((Uv[j], Uv[j+1], True), (Lv[j], Lv[j+1], False)):
        b = (W1 - W0)/(tb - ta)
        w0 = W0 - b*ta            # W(t) = w0 + b t
        # nullcline gap: N - W = t^2 + (1-b) t - w0 > 0
        lo, _ = quad_range(Fr(1), 1 - b, -w0, ta, tb)
        chk("gap seg%d %s" % (j, "U" if upper else "L"), lo > 0)
        # P(t) = W(3-t) - 2b(N - W) = -3b t^2 + [3b - w0 - 2b(1-b)] t + (3 + 2b) w0
        c2 = -3*b
        c1 = 3*b - w0 - 2*b*(1 - b)
        c0 = (3 + 2*b)*w0
        lo, hi = quad_range(c2, c1, c0, ta, tb)
        if upper:
            chk("P>0 seg%d U" % j, lo > 0)
        else:
            chk("P<0 seg%d L" % j, hi < 0)

n_checks = 4 + 2*NSEG*2
print("\nEXACT CERTIFICATE: %d checks, %d failures" % (n_checks, len(fails)))
if fails:
    print("FAILED:", fails[:20])
else:
    U1, L1 = Uv[0], Lv[0]
    print("G-B1 PASS: all segment + saddle checks verified in exact rational arithmetic")
    print("\nS ENCLOSURE:  %s <= S <= %s" % (L1, U1))
    print("   floats: [%.6f, %.6f], width %.6f" % (L1, U1, float(U1 - L1)))
    print("G-B2:", "PASS — U(1) = %s < 3/2 EXACTLY (margin %s = %.6f)" % (U1, Fr(3,2)-U1, float(Fr(3,2)-U1))
          if U1 < Fr(3,2) else "FAIL")
    print("G-B3 consistency: numeric S = %.9f in enclosure:" % S_num,
          "PASS" if float(L1) <= S_num <= float(U1) else "FAIL")
    # k_edge enclosure (monotone in S)
    klo = math.sqrt(2/(2 - float(L1))); khi = math.sqrt(2/(2 - float(U1)))
    print("G-B4 report: k_edge in [%.6f, %.6f]; 2 - k_edge >= %.6f rigorously" % (klo, khi, 2 - khi))
    print("\nTHEOREM (modulo named classical imports): S < 3/2; the dip is real;")
    print("k_edge < 2; via the merge theorem the interior inequality holds in a peak neighborhood.")
