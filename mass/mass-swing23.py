#!/usr/bin/env python3
# Swing 23 — lock range + patch angle: the capacity chain from r_q and m alone.
# Registration: 3ab5d86 (pre-run). Arithmetic instrument.
import numpy as np

HBARC = 197.327          # MeV fm
MN = 938.92              # MeV (average nucleon)
ZC_ENERGY, DZC = 4.78, 0.35
XI_BAND = (0.40, 0.50)
CHAIN_WIN = (4.5, 5.13)  # energy band cap ∩ geometric route
THETA_BOOKED = 54.5      # deg, from Omega_w = 4pi/z_c at 4.78

xi = 2.0*HBARC/MN
print("SWING 23 — the capacity chain")
print("CLAIM 1: xi = 2 hbar/(m_N c) = %.4f fm" % xi)
print("S23a xi in [%.2f, %.2f] (booked geometric band; reach-core = 0.42):" % XI_BAND,
      "PASS" if XI_BAND[0] <= xi <= XI_BAND[1] else "FAIL")

print("\nCLAIM 2 + CHAIN over r_q band:")
rows = []
for rq in (0.84, 0.86, 0.88):
    reach = 2*rq + xi
    sin_t = 2*rq/reach
    theta = np.degrees(np.arcsin(sin_t))
    cos_t = np.sqrt(1 - sin_t*sin_t)
    zc = 2.0/(1.0 - cos_t)
    rows.append((rq, reach, theta, zc))
    print("  r_q=%.2f: reach=%.4f fm  theta_w=%.2f deg  z_c(chain)=%.3f" % (rq, reach, theta, zc))

rq_c = rows[1]
print("\nS23b theta_w derived %.2f deg vs booked %.1f deg: signed tension %+.1f%%"
      % (rq_c[2], THETA_BOOKED, 100*(rq_c[2]-THETA_BOOKED)/THETA_BOOKED))
zc_lo, zc_c, zc_hi = rows[0][3], rq_c[3], rows[2][3]
zmin, zmax = min(r[3] for r in rows), max(r[3] for r in rows)
ok = CHAIN_WIN[0] <= zc_c <= CHAIN_WIN[1]
print("S23c THE CHAIN GATE: z_c(derived) = %.3f [%.3f, %.3f] vs window [%.2f, %.2f]:"
      % (zc_c, zmin, zmax, *CHAIN_WIN), "PASS" if ok else "FAIL")
print("  signed vs energy central 4.78: %+.1f%%" % (100*(zc_c-ZC_ENERGY)/ZC_ENERGY))
print("  named-rejected cos-assignment would give z_c = %.1f (outside every band)"
      % (2.0/(1.0 - 2*0.86/(2*0.86+xi))))

# S23d ripple report (no gate)
c3 = 41.47*0.75/(18*0.86*0.86)
print("\nS23d ripple (report only, z_c = %.3f):" % zc_c)
print("  h = 2c3/z_c: %.3f (was 0.978 at 4.78) — vs measured 0.84(15): %+.0f%%"
      % (2*c3/zc_c, 100*(2*c3/zc_c-0.84)/0.84))
print("  deltabar = 2C/z_c: %.2f (was 15.00) — books gross target"
      % (2*35.85/zc_c))
print("  suppression s = 2/z_c: %.4f (was 0.4184) vs measured 0.360±0.064: %+.1fx"
      % (2/zc_c, (0.360-2/zc_c)/0.064))
