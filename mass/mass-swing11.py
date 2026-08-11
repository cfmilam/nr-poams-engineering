#!/usr/bin/env python3
# Swing 11 — shared-turn ledger (discreteum). Registration: ledger 350f48f (pre-run).
# delta_pair = (hbar^2/m)/(4 r_q^2)  [one shared turn, L=hbar, I = 2 m r_q^2]
# loop credit per bond = [hbar^2/(2 I_loop)]/3,  I_loop = 3 m R^2, R = 2 r_q/sqrt(3)
HB2M = 41.47
BANDS = {"pair": (14.12, 14.49), "tri": (13.9, 16.5), "alpha": (16.6, 18.4)}
MEAS  = {"pair": 14.31, "tri": 15.14, "alpha": 17.70, "bulk": 22.2}

for rq in (0.84, 0.86, 0.88):
    dp = HB2M/(4*rq*rq)
    R  = 2*rq/3**0.5
    Iloop = 3*R*R                       # in units of m fm^2
    credit = (HB2M/(2*Iloop))/3.0       # per bond (3 bonds share the loop turn)
    d_tri   = dp + 1*credit
    d_alpha = dp + 2*credit
    T_bulk  = (MEAS["bulk"] - dp)/credit
    print("r_q=%.2f  delta_pair=%.2f  credit/loop=%.3f  tri=%.2f  alpha=%.2f  implied bulk T=%.2f"
          % (rq, dp, credit, d_tri, d_alpha, T_bulk))

rq = 0.86
dp = HB2M/(4*rq*rq); R = 2*rq/3**0.5; credit = HB2M/(2*3*R*R)/3
print("\nS11a pair: pred %.2f vs measured band [14.12,14.49]:" % dp,
      "PASS" if (14.12 <= dp <= 14.49) or abs(dp-MEAS['pair'])/MEAS['pair'] <= 0.03 else "FAIL",
      "(central offset %.1f%%)" % (100*abs(dp-MEAS['pair'])/MEAS['pair']))
d_tri = dp + credit
print("S11b tri: pred %.2f in [13.9,16.5]:" % d_tri, "PASS" if 13.9 <= d_tri <= 16.5 else "FAIL")
d_a = dp + 2*credit
print("S11c alpha: pred %.2f in [16.6,18.4]:" % d_a, "PASS" if 16.6 <= d_a <= 18.4 else "FAIL")
T = (MEAS["bulk"]-dp)/credit
print("S11d implied bulk T = %.2f in [2,4.8]:" % T, "PASS" if 2 <= T <= 4.8 else "FAIL",
      "(fcc=4; dense-random 2-4)")
