#!/usr/bin/env python3
# Swing 36 — the cluster displacement layer + joint fraction resolution.
# Registration: 696992d (pre-run).
import math, re

HB2M = 41.47; AC = 0.72; RQ = 0.86
HBARC = 197.327; MN = 938.92
RP2 = 0.8409**2; RN2 = -0.1155
K = 1.44; CG = math.sqrt(6/math.pi)

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
def B(Z,N): return BA[(Z,N)]*(Z+N)/1000.0
B_d, B_t, B_h, B_a = B(1,1), B(1,2), B(2,1), B(2,2)

xi = 2*HBARC/MN; sin_t = 2*RQ/(2*RQ+xi); cos_t = math.sqrt(1-sin_t*sin_t)
zc = 2/(1-cos_t); dp = HB2M/(4*RQ*RQ); c3 = HB2M*0.75/(18*RQ*RQ); h = 2*c3/zc
def pp2(rc,Z,N): return rc*rc - RP2 - (N/Z)*RN2
tri_r2 = (2*pp2(1.9661,2,1)+pp2(1.7591,1,2))/3.0; a_r2 = pp2(1.67824,2,2)
tau3 = (9/8)*HB2M*(2/3)/tri_r2; tau4 = (9/8)*HB2M*(3/4)/a_r2
t_tri0 = dp + h; t_alp = dp + h + c3
D_ANCH = 14.075

# ---- Part A: the layer ----
rpp_h = math.sqrt(2*pp2(1.9661,2,1))          # 3He point-proton pair separation
rpp_a = math.sqrt(2*pp2(1.67824,2,2))
st_h_new = K*CG/rpp_h
st_a_new = K*CG/rpp_a
st_h_old = AC*2/3**(1/3); st_a_old = AC*2/4**(1/3)
dB_mirror = B_t - B_h
print("swing 36 — the displacement layer at cluster scale")
print("3He: r_pp = %.4f fm -> st_h' = %.4f (bare %.4f) | mirror dB = %.4f" %
      (rpp_h, st_h_new, st_h_old, dB_mirror))
print("alpha: r_pp = %.4f fm -> st_a' = %.4f (bare %.4f)" % (rpp_a, st_a_new, st_a_old))
ok_a = abs(st_h_new/dB_mirror - 1) < 0.10
print("S36a |st_h'/dB - 1| = %.1f%% < 10%% -> %s  (bare ran %+.1f%%)"
      % (100*abs(st_h_new/dB_mirror-1), "PASS" if ok_a else "FAIL", 100*(st_h_old/dB_mirror-1)))

X_t = B_t + 3*tau3
X_h = B_h + 3*tau3 + st_h_new
X_a = B_a + 4*tau4 + st_a_new

# ---- Part B: triangulation under strain' ----
def gammas(f):
    tt = t_tri0 - f*h
    gt = (X_t/tt-1)/2; gh = (X_h/tt-1)/2; ga = (X_a/t_alp-2)/4
    return gt, gh, ga
gt0, gh0, ga0 = gammas(0.0)
gap_th = abs(gh0 - gt0)
ok_b = gap_th < 0.002
print("\nS36b at f=0: gamma_t %.5f gamma_h %.5f gamma_a %.5f | t-h gap %.5f (was 0.0078) -> %s"
      % (gt0, gh0, ga0, gap_th, "PASS" if ok_b else "FAIL"))

# spread minimization over f
def spread(f):
    g = gammas(f); return max(g)-min(g)
fs = [i/10000 for i in range(0, 3500)]
fstar = min(fs, key=spread)
sp_star = spread(fstar)
rows = {"F6 1/6": 1/6, "F7 (2/zc)^2": (2/zc)**2, "F8 1/(2zc)": 1/(2*zc)}
near = {k: abs(fstar-v) for k, v in rows.items()}
sel = [k for k, d in near.items() if d < 0.033]
# F6/F7 degeneracy: treat as one class if both inside
distinct = set()
for k in sel:
    distinct.add("F6/F7 class" if k in ("F6 1/6", "F7 (2/zc)^2") else k)
ok_c = (0.10 <= fstar <= 0.25) and (len(distinct) == 1)
print("\nS36c spread-min: f* = %.4f, spread %.5f | distances: %s" %
      (fstar, sp_star, {k: round(d,4) for k,d in near.items()}))
print("     unique selection (F6/F7 degeneracy = one class): %s -> %s"
      % (sorted(distinct), "PASS" if ok_c else "FAIL"))

# S36d joint closure at f = 1/6 exactly
f6 = 1/6
g6 = gammas(f6); sp6 = max(g6)-min(g6)
gstar6 = sum(g6)/3
W2 = 1+2*gstar6; W4 = 2+4*gstar6
z2 = (X_t/W2 + X_h/W2)/2; da = X_a/W4
s1 = z2 - D_ANCH; s2 = da - z2
# step ledger in anchor units: predicted step1 = (t_tri0 - f*h) - D_ANCH  (J3 offset propagates)
pred1 = (t_tri0 - f6*h) - D_ANCH
pred2 = c3 + f6*h
res1 = 100*(pred1-s1)/s1; res2 = 100*(pred2-s2)/s2
ok_d = (sp6 < 0.0015) and abs(res1) < 1.0
print("\nS36d at f = 1/6: gammas %.5f/%.5f/%.5f spread %.5f (<0.0015) | step1 pred %.4f vs %.4f (%+.2f%%) | step2 pred %.4f vs %.4f (%+.2f%%) -> %s"
      % (g6[0], g6[1], g6[2], sp6, pred1, s1, res1, pred2, s2, res2, "PASS" if ok_d else "FAIL"))

# S36e reports
print("\nS36e reports (unclaimed): gamma*'' = %.4f (spread-conditional band ~%.4f);" % (gstar6, sp6))
print("  F8 spread at criterion: %.5f (exclusion factor %.1fx vs F6)" % (spread(1/(2*zc)), spread(1/(2*zc))/sp6))
print("  st_a ripple +%.4f into gamma_a; a_sym contact rescale ~(1+2*0.85)/(1+2*%.3f) ripple report" % (st_a_new-st_a_old, gstar6))
print("  RE-ANCHOR (strain' + f=1/6 operational) PROPOSED — ratification required.")
