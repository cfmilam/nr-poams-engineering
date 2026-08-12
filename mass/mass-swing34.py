#!/usr/bin/env python3
# Swing 34 — the pool census: frontier-share form. Registration: a8c671e (pre-run).
import math, re
import numpy as np

HB2M = 41.47; RQ = 0.86
DP = HB2M/(4*RQ*RQ)           # 14.0177
HBARC = 197.327; MN = 938.92
xi = 2*HBARC/MN; sin_t = 2*RQ/(2*RQ+xi); cos_t = math.sqrt(1-sin_t*sin_t)
ZC = 2/(1-cos_t)              # 4.9401
K_COUL = 1.44
T1_Q = np.array([6.86, 9.48, 10.51, 10.55])
PRED_SPLIT_Q = (K_COUL/(2*RQ)) * (T1_Q/T1_Q[3])   # swing-33 co-drift track (frozen)

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

MAGIC = (2,8,20,28,50,82,126)
def dist(x): return min(abs(x-m) for m in MAGIC)

rows = []
for (Z,N) in list(BA.keys()):
    A = Z+N
    if not (20 <= A <= 220): continue
    if N%2 == 1:
        b0,bm,bp = B(Z,N),B(Z,N-1),B(Z,N+1)
        if None not in (b0,bm,bp):
            d = (bm+bp)/2 - b0
            if 0 < d < 6: rows.append((A, d*math.sqrt(A), 1, dist(N)))
    if Z%2 == 1:
        b0,bm,bp = B(Z,N),B(Z-1,N),B(Z+1,N)
        if None not in (b0,bm,bp):
            d = (bm+bp)/2 - b0
            if 0 < d < 6: rows.append((A, d*math.sqrt(A), 0, dist(Z)))
arr = np.array(rows, float)
print("swing 34 — pool census: %d gaps; dp/2 = %.3f; 2/z_c = %.4f" % (len(arr), DP/2, 2/ZC))

# S34a — theorem: scored on the registration's lattice argument (prose; no computation).
print("\nS34a exclusion theorem: stands as registered (exponent lattice {p/3}; -1/2 not in lattice)")

# S34b/S34c — declared ops
edge = arr[(arr[:,0]>=20)&(arr[:,0]<=40)]
plat = arr[(arr[:,0]>=150)&(arr[:,0]<=220)]
d_cell = float(np.median(edge[:,1])); plateau = float(np.median(plat[:,1]))
phi = (d_cell/plateau)**2
ok_b = 5.26 <= d_cell <= 8.76
ok_c = 0.30 <= phi <= 0.52
print("\nS34b light-edge intercept delta_cell (A 20-40, n=%d): %.3f | dp/2 = %.3f (%+.1f%%) | [5.26,8.76] -> %s"
      % (len(edge), d_cell, DP/2, 100*(d_cell-DP/2)/(DP/2), "PASS" if ok_b else "FAIL"))
print("S34c plateau (A 150-220, n=%d): %.3f -> phi = (%.3f/%.3f)^2 = %.4f | [0.30,0.52] -> %s | vs 2/z_c %.4f (%+.1f%%)"
      % (len(plat), plateau, d_cell, plateau, phi, "PASS" if ok_c else "FAIL", 2/ZC, 100*(phi-2/ZC)/(2/ZC)))

# S34d — consistency (seen; zero credit)
qs = np.percentile(arr[:,0], [25,50,75]); edges = [20]+list(qs)+[220]
qmeds = []
for i in range(4):
    sel = arr[(arr[:,0]>=edges[i])&(arr[:,0]<=edges[i+1])]
    qmeds.append(float(np.median(sel[:,1])))
mono = all(qmeds[i+1] >= qmeds[i]-0.3 for i in range(3))
sat = (qmeds[3]-qmeds[2]) < 0.3*(qmeds[2]-qmeds[0])
print("\nS34d consistency: quartile medians %s | monotone(0.3) %s | saturating %s -> %s"
      % (np.round(qmeds,2), mono, sat, "PASS" if (mono and sat) else "FAIL"))

# implied n_f/A curve (report): (delta_cell/DsqrtA)^2
print("\nreport — implied frontier share n_f/A per quartile: %s (light limit 1 by construction)"
      % np.round([(d_cell/q)**2 for q in qmeds], 3))

# S34e — T5 diagnostic: quartile n/p splits excluding dist<=1
print("\nS34e T5 diagnostic (exclude dist<=1):")
sub = arr[arr[:,3] >= 2]
rec = []
for i in range(4):
    sel = (sub[:,0]>=edges[i])&(sub[:,0]<=edges[i+1])
    nq = sub[sel&(sub[:,2]==1)][:,1]; pq = sub[sel&(sub[:,2]==0)][:,1]
    s = float(np.median(nq))-float(np.median(pq)); rec.append(s)
    print("  Q%d: split %+.3f | full-sample %+.3f | co-drift track %.3f (n=%d)"
          % (i+1, s, [0.541,0.927,0.298,1.263][i], PRED_SPLIT_Q[i], int(sel.sum())))
gap_full = abs(0.298 - PRED_SPLIT_Q[2]); gap_new = abs(rec[2] - PRED_SPLIT_Q[2])
print("  Q3 gap to track: full %.3f -> filtered %.3f (%s recovery %.0f%%)"
      % (gap_full, gap_new, "≥half" if gap_new <= 0.5*gap_full else "<half", 100*(1-gap_new/gap_full)))
