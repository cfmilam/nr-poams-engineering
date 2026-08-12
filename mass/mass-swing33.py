#!/usr/bin/env python3
# Swing 33 — the pairing candidate walks into the ambush. Registration: 5fa1759 (pre-run).
# Mechanism: borrow-exchange (gamma^2, two vertices); pool P read from frozen T1 record.
import math, re
import numpy as np

HB2M = 41.47; AC = 0.72; RQ = 0.86
HBARC = 197.327; MN = 938.92
RP2 = 0.8409**2; RN2 = -0.1155
K_COUL = 1.44  # MeV*fm, the named import

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

# --- frozen constants (registration) ---
T1_Q = np.array([6.86, 9.48, 10.51, 10.55]); T1_ALL = 9.65   # seen record, frozen
SPLIT_SCALE = K_COUL/(2*RQ)                                   # 0.8372, zero dials
PRED_OVERALL = SPLIT_SCALE * (T1_ALL/T1_Q[3])                 # 0.766
PRED_Q = SPLIT_SCALE * (T1_Q/T1_Q[3])                         # {0.54,0.75,0.83,0.84}
ASYM = 24.5                                                   # ledger's derived a_sym

# gamma* (swing-30 pipeline, identical) for the conditional report
xi = 2*HBARC/MN; sin_t = 2*RQ/(2*RQ+xi); cos_t = math.sqrt(1-sin_t*sin_t)
zc = 2/(1-cos_t); dp = HB2M/(4*RQ*RQ); c3 = HB2M*0.75/(18*RQ*RQ); h = 2*c3/zc
def pp2(rc,Z,N): return rc*rc - RP2 - (N/Z)*RN2
tri_r2 = (2*pp2(1.9661,2,1)+pp2(1.7591,1,2))/3.0; a_r2 = pp2(1.67824,2,2)
tau3 = (9/8)*HB2M*(2/3)/tri_r2; tau4 = (9/8)*HB2M*(3/4)/a_r2
st_h = AC*2/3**(1/3); st_a = AC*2/4**(1/3)
t_tri = dp+h; t_alp = dp+h+c3
g = ((B(2,1)+3*tau3+st_h)/t_tri-1)/2, ((B(1,2)+3*tau3)/t_tri-1)/2, ((B(2,2)+4*tau4+st_a)/t_alp-2)/4
gstar = sum(g)/3

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
n_arr = arr[arr[:,2]==1]; p_arr = arr[arr[:,2]==0]
print("swing 33 ambush confrontation — %d gaps (%d n, %d p); gamma* = %.4f" %
      (len(arr), len(n_arr), len(p_arr), gstar))
print("frozen: split scale k/(2r_q) = %.4f; predicted overall %.3f; predicted quartiles %s"
      % (SPLIT_SCALE, PRED_OVERALL, np.round(PRED_Q,2)))

# S33a — overall n/p split
n_med = float(np.median(n_arr[:,1])); p_med = float(np.median(p_arr[:,1]))
split = n_med - p_med
ok_a = 0.50 <= split <= 1.15
print("\nS33a T2 overall split: Dn %.2f - Dp %.2f = %.3f | predicted %.3f (%+.1f%%) | band [0.50,1.15] -> %s"
      % (n_med, p_med, split, PRED_OVERALL, 100*(PRED_OVERALL-split)/split, "PASS" if ok_a else "FAIL"))

# S33b — co-drift by A-quartile (pooled quartile boundaries)
qs = np.percentile(arr[:,0], [25,50,75])
edges = [20] + list(qs) + [220]
print("\nS33b T2 co-drift (A-quartile splits vs predicted, gate +-60% each, all>0):")
ok_b = True; qsplits = []
for i in range(4):
    sel = (arr[:,0] >= edges[i]) & (arr[:,0] <= edges[i+1])
    nq = arr[sel & (arr[:,2]==1)][:,1]; pq = arr[sel & (arr[:,2]==0)][:,1]
    s = float(np.median(nq)) - float(np.median(pq)); qsplits.append(s)
    lo, hi = 0.4*PRED_Q[i], 1.6*PRED_Q[i]
    ok = (s > 0) and (lo <= s <= hi)
    ok_b = ok_b and ok
    print("  Q%d (A %3.0f-%3.0f, n=%4d): split %+.3f | pred %.3f | [%.2f,%.2f] -> %s"
          % (i+1, edges[i], edges[i+1], int(sel.sum()), s, PRED_Q[i], lo, hi, "pass" if ok else "FAIL"))
print("S33b ->", "PASS" if ok_b else "FAIL")

# S33c — T3 sign (pooled)
def med_at(lo, hi):
    sel = arr[(arr[:,3]>=lo)&(arr[:,3]<=hi)]
    return float(np.median(sel[:,1])), len(sel)
d1,n1 = med_at(1,1); d3,n3 = med_at(3,99)
ok_c = d1 < d3
print("\nS33c T3 sign: dist-1 %.2f (n=%d) < dist-3+ %.2f (n=%d) -> %s" %
      (d1,n1,d3,n3,"PASS" if ok_c else "FAIL"))
for t,lab in ((1,'n'),(0,'p')):
    s1 = arr[(arr[:,3]==1)&(arr[:,2]==t)][:,1]; s3 = arr[(arr[:,3]>=3)&(arr[:,2]==t)][:,1]
    print("   report %s-only: dist-1 %.2f vs dist-3+ %.2f (%+.0f%%)" %
          (lab, np.median(s1), np.median(s3), 100*(np.median(s1)-np.median(s3))/np.median(s3)))

# S33d — T4 census identity
vals = []
for (Z,N) in list(BA.keys()):
    A = Z+N
    if not (20 <= A <= 220): continue
    if Z%2==0 and N%2==0:
        b = [B(Z,N),B(Z,N-2),B(Z-2,N),B(Z-2,N-2)]
        if None not in b:
            dv = (b[0]-b[1]-b[2]+b[3])/4
            y = (N-Z)/A
            vals.append((dv, dv*A/(2*(1-y*y)), A))
vals = np.array(vals)
med_dv = float(np.median(vals[:,0])); med_id = float(np.median(vals[:,1]))
ok_d = 19.6 <= med_id <= 29.4
print("\nS33d T4 census identity: median dV_pn %.3f (n=%d, med A %.0f); median[dV_pn*A/(2(1-y^2))] = %.2f | band [19.6,29.4] (a_sym 24.5+-20%%) -> %s"
      % (med_dv, len(vals), float(np.median(vals[:,2])), med_id, "PASS" if ok_d else "FAIL"))
print("   residual vs derived a_sym 24.5: %+.1f%%" % (100*(med_id-ASYM)/ASYM))

# REPORTS — conditional absolute (no gate, no credit; Wyler-adjacent flagged)
cond = gstar*gstar*dp
print("\nREPORT (ungated, conditional on underived pool): gamma*^2*dp = %.3f;" % cond)
po = cond*(T1_ALL/T1_Q[3])
print("  x P(Q4-normalized): overall %.2f vs measured %.2f (%+.1f%%); Q4 %.2f vs %.2f (%+.1f%%)"
      % (po, T1_ALL, 100*(po-T1_ALL)/T1_ALL, cond, T1_Q[3], 100*(cond-T1_Q[3])/T1_Q[3]))
