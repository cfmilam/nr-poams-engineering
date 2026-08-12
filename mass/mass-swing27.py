#!/usr/bin/env python3
# Swings 27 + 29 instruments. Registration: 3c8e478 (pre-run, block).
# 27: pairing = gamma*delta_pair/sqrt(A) vs AME2020 odd-even gaps.
# 29: two-cell sign gates (AME reads).
import math, re
import numpy as np

BA = {}
for ln in open("data/mass.mas20.txt", encoding="ascii", errors="replace"):
    if len(ln) < 70: continue
    try: N=int(ln[4:9]); Z=int(ln[9:14]); A=int(ln[14:19])
    except ValueError: continue
    if A != N+Z: continue
    fld = ln[54:68]
    if "#" in fld: continue
    m = re.search(r"[-\d.]+", fld)
    if not m: continue
    BA[(Z,N)] = float(m.group())
def B(Z,N):
    v = BA.get((Z,N))
    return None if v is None else v*(Z+N)/1000.0

print("SWING 27 — pairing magnitude vs AME odd-even gaps")
PRED_C, PRED_LO, PRED_HI = 11.92, 10.7, 13.2
gaps = []
for (Z, N) in list(BA.keys()):
    A = Z + N
    if not (20 <= A <= 220): continue
    # neutron 3-point gap centered on odd N
    if N % 2 == 1:
        b0, bm, bp = B(Z,N), B(Z,N-1), B(Z,N+1)
        if None not in (b0, bm, bp):
            d = ((bm + bp)/2.0 - b0)   # positive when odd-N is less bound
            if 0 < d < 6: gaps.append((A, d*math.sqrt(A)))
    # proton 3-point gap centered on odd Z
    if Z % 2 == 1:
        b0, bm, bp = B(Z,N), B(Z-1,N), B(Z+1,N)
        if None not in (b0, bm, bp):
            d = ((bm + bp)/2.0 - b0)
            if 0 < d < 6: gaps.append((A, d*math.sqrt(A)))
gaps = np.array(gaps)
med = float(np.median(gaps[:,1]))
print("  gaps used: %d | median Delta*sqrt(A) = %.2f MeV" % (len(gaps), med))
print("  S27a: predicted %.2f [%.1f, %.1f] — median in band:" % (PRED_C, PRED_LO, PRED_HI),
      "PASS — IDENTIFIED" if PRED_LO <= med <= PRED_HI else "FAIL")
print("  central offset: %+.1f%%" % (100*(PRED_C-med)/med))
qs = [20, 70, 120, 170, 220]
print("  S27b A-shape (median Delta*sqrt(A) per A-band; flat = A^-1/2 holds):")
for lo, hi in zip(qs[:-1], qs[1:]):
    sel = gaps[(gaps[:,0] >= lo) & (gaps[:,0] < hi)]
    if len(sel): print("    A in [%d,%d): %.2f  (n=%d)" % (lo, hi, float(np.median(sel[:,1])), len(sel)))
print("  S27c: dimensional route sqrt(delta0*d) (x1.5 high) RETIRED.")

print("\nSWING 29 — two-cell sign gates (AME reads)")
be8 = B(4,4) - 2*B(2,2)
li6 = B(3,3) - B(2,2) - B(1,1)
he5 = B(2,3) - B(2,2)   # alpha + free n (n contributes 0 binding)
print("  Be-8 - 2a       = %+.3f MeV  (predicted ~0-): %s" % (be8, "SIGN OK" if -1.0 < be8 <= 0.05 else "CHECK"))
print("  Li-6 - a - d    = %+.3f MeV  (predicted > 0): %s" % (li6, "SIGN OK" if li6 > 0 else "FAIL"))
print("  He-5 - a (n)    = %+.3f MeV  (predicted < 0): %s" % (he5, "SIGN OK" if he5 < 0 else "FAIL"))
print("  S29a: three signs as predicted by the cell-closure bar:",
      "PASS" if (-1.0 < be8 <= 0.05 and li6 > 0 and he5 < 0) else "FAIL")
print("  S29b magnitudes reported, not scored: %.3f / %.3f / %.3f (rung-tax coefficient stays open)"
      % (be8, li6, he5))
