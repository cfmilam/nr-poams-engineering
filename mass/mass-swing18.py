#!/usr/bin/env python3
# Swing 18 — the first-loop anholonomy credit, derived. Registration: 2161822 (pre-run).
# h = c3 * (Omega_w / 2pi) = 2*c3/z_c  (patch-cone geometric phase, J=1, Berry exact)
import numpy as np

HB2M = 41.47
ZC, DZC = 4.78, 0.35
RQS = (0.84, 0.86, 0.88)
MEAS_H, DMEAS_H = 0.84, 0.15          # trinucleon step 15.14 - 14.31 (swing-8 common radii)
MEAS_C3, DMEAS_C3 = 2.55, 0.20        # measured marginal (swings 6-8)
MEAS_STEP_ALPHA = 3.39                # alpha - pair total step 17.70 - 14.31
DMEAS_STEP = 0.20

print("SWING 18 — h = 2*c3/z_c (patch-cone anholonomy, J=1)")
print("capacity identity: Omega_w = 4pi/z_c => fraction Omega_w/2pi = 2/z_c = %.4f central" % (2/ZC))

rows = []
for rq in RQS:
    c3 = HB2M * 0.75 / (18 * rq * rq)
    for zc in (ZC - DZC, ZC, ZC + DZC):
        h = 2 * c3 / zc
        rows.append((rq, zc, c3, h))
        print("r_q=%.2f z_c=%.2f: c3=%.3f  h=%.3f  (h+c3=%.3f)" % (rq, zc, c3, h, h + c3))

hs = [r[3] for r in rows]
c3c = HB2M * 0.75 / (18 * 0.86 * 0.86)
hc = 2 * c3c / ZC
print("\nCENTRAL: c3 = %.3f, h = %.3f;  band h = [%.3f, %.3f]" % (c3c, hc, min(hs), max(hs)))

print("\nS18b identification window [0.6, 1.1]:", "PASS" if 0.6 <= hc <= 1.1 else "FAIL")

lo, hi = min(hs), max(hs)
mlo, mhi = MEAS_H - DMEAS_H, MEAS_H + DMEAS_H
overlap = max(0.0, min(hi, mhi) - max(lo, mlo))
print("S18c confrontation vs measured %.2f(%.0f): derived [%.2f, %.2f] vs measured [%.2f, %.2f] — overlap %s"
      % (MEAS_H, 100*DMEAS_H, lo, hi, mlo, mhi, "YES (%.2f MeV)" % overlap if overlap > 0 else "NO"))
print("  central tension SIGNED: h_derived - h_meas = %+.3f MeV (%+.0f%%)" % (hc - MEAS_H, 100*(hc-MEAS_H)/MEAS_H))
print("  c3 tension SIGNED:      c3_derived - c3_meas = %+.3f MeV (%+.0f%%)" % (c3c - MEAS_C3, 100*(c3c-MEAS_C3)/MEAS_C3))
print("  opposite-sign pattern per registration:", "YES — booked as split-structure residual"
      if (hc - MEAS_H) * (c3c - MEAS_C3) < 0 else "no")

s = hc + c3c
sums = [r[3] + r[2] for r in rows]
print("\nS18d sum check: h + c3 = %.3f [%.3f, %.3f] vs measured alpha-step %.2f(%.0f):"
      % (s, min(sums), max(sums), MEAS_STEP_ALPHA, 100*DMEAS_STEP),
      "inside" if MEAS_STEP_ALPHA - DMEAS_STEP <= s <= MEAS_STEP_ALPHA + DMEAS_STEP or
                  (min(sums) <= MEAS_STEP_ALPHA + DMEAS_STEP and max(sums) >= MEAS_STEP_ALPHA - DMEAS_STEP)
      else "outside")
print("  central offset: %+.3f MeV (%+.1f%%)" % (s - MEAS_STEP_ALPHA, 100*(s-MEAS_STEP_ALPHA)/MEAS_STEP_ALPHA))

# S18e bulk restatement (report only): swing-17 books with h_derived in h1 variant
print("\nS18e bulk restatement (report only) — swing-17 ensembles, h1 with h_derived = %.3f:" % hc)
for name, zbar, Tm, Qm, Em, fm in (
    ("functional", 4.846, 83.3, 97.3, 620.0, 1.000),
    ("liquid",     4.586, 231.0, 142.7, 1174.0, 0.999),
):
    for rq in RQS:
        dp = HB2M/(4*rq*rq); c3 = HB2M*0.75/(18*rq*rq); c4 = HB2M*0.5/(32*rq*rq)
        hd = 2*c3/ZC
        cred = (c3*Tm + c4*Qm)/Em
        g1 = dp + cred + hd*fm
        pref = min(zbar, ZC)/2.0
        G1 = pref*g1
        tag = " <-- central" if rq == 0.86 else ""
        print("  %-10s r_q=%.2f: gross_h1'=%.2f  G_h1'=%.2f (%+.1f%% vs 35.85)%s"
              % (name, rq, g1, G1, 100*(G1-35.85)/35.85, tag))
