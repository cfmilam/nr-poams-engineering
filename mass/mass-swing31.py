#!/usr/bin/env python3
# Swing 31 — the pairing ambush: target-set characterization, UNSCORED.
# Registration: 1fbb6ec (pre-run). No formula; four targets on the record.
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

MAGIC = (2, 8, 20, 28, 50, 82, 126)
def dist(x): return min(abs(x-m) for m in MAGIC)

rows = []  # (A, gap*sqrtA, type, frontier_dist)
for (Z, N) in list(BA.keys()):
    A = Z + N
    if not (20 <= A <= 220): continue
    if N % 2 == 1:
        b0, bm, bp = B(Z,N), B(Z,N-1), B(Z,N+1)
        if None not in (b0, bm, bp):
            d = (bm + bp)/2.0 - b0
            if 0 < d < 6: rows.append((A, d*math.sqrt(A), 'n', dist(N)))
    if Z % 2 == 1:
        b0, bm, bp = B(Z,N), B(Z-1,N), B(Z+1,N)
        if None not in (b0, bm, bp):
            d = (bm + bp)/2.0 - b0
            if 0 < d < 6: rows.append((A, d*math.sqrt(A), 'p', dist(Z)))

arr = np.array([(a, g, 1 if t=='n' else 0, fd) for a, g, t, fd in rows], float)
print("SWING 31 — the pairing target set (characterization, UNSCORED)")
print("gaps: %d total (%d n, %d p)" % (len(arr), int(arr[:,2].sum()), int((1-arr[:,2]).sum())))

print("\nT1 (already on record, swing 27): A-drift medians 6.86 / 9.48 / 10.51 / 10.55; overall 9.65")

n_med = float(np.median(arr[arr[:,2]==1][:,1]))
p_med = float(np.median(arr[arr[:,2]==0][:,1]))
print("T2 n/p split: median Dn*sqrtA = %.2f | Dp*sqrtA = %.2f | ratio p/n = %.3f | diff = %+.2f MeV"
      % (n_med, p_med, p_med/n_med, p_med - n_med))

print("T3 frontier suppression (median gap*sqrtA by distance to closure, n+p pooled):")
for lo, hi, lab in ((0,0,'0'), (1,1,'1'), (2,2,'2'), (3,99,'3+')):
    sel = arr[(arr[:,3] >= lo) & (arr[:,3] <= hi)]
    if len(sel):
        print("    dist %-3s: %.2f  (n=%d)" % (lab, float(np.median(sel[:,1])), len(sel)))

# T4: np-pair indicator dV_pn (quarter double difference; extant label, tagged)
dvs = []
for (Z, N) in list(BA.keys()):
    A = Z + N
    if not (20 <= A <= 220): continue
    if Z % 2 == 0 and N % 2 == 0:
        b = [B(Z,N), B(Z,N-2), B(Z-2,N), B(Z-2,N-2)]
        if None not in b:
            dvs.append((b[0] - b[1] - b[2] + b[3])/4.0)
dvs = np.array(dvs)
print("T4 np-pair indicator dV_pn (ee, quarter double-diff): median %.3f MeV (n=%d, IQR %.3f-%.3f)"
      % (float(np.median(dvs)), len(dvs), float(np.percentile(dvs,25)), float(np.percentile(dvs,75))))

print("\nNO SCORING. These four numbers + T1 = the registered ambush for any future")
print("pairing candidate (derived with zero pairing-data inputs, confronts all four).")
print("Inoculated near-coincidences (REFUSED post-hoc): (2/3)deltabar=9.68,")
print("gamma^2*dp=10.13, 4c3=9.35, mu*deltabar=9.79.")
