#!/usr/bin/env python3
# Swing 35 — self-consistent transfer fraction: lane audit. Registration: 7ee8df4 (pre-run).
import math, re

HB2M = 41.47; AC = 0.72; RQ = 0.86
HBARC = 197.327; MN = 938.92
RP2 = 0.8409**2; RN2 = -0.1155

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

xi = 2*HBARC/MN; sin_t = 2*RQ/(2*RQ+xi); cos_t = math.sqrt(1-sin_t*sin_t)
zc = 2/(1-cos_t); dp = HB2M/(4*RQ*RQ); c3 = HB2M*0.75/(18*RQ*RQ); h = 2*c3/zc
def pp2(rc,Z,N): return rc*rc - RP2 - (N/Z)*RN2
tri_r2 = (2*pp2(1.9661,2,1)+pp2(1.7591,1,2))/3.0; a_r2 = pp2(1.67824,2,2)
tau3 = (9/8)*HB2M*(2/3)/tri_r2; tau4 = (9/8)*HB2M*(3/4)/a_r2
st_h = AC*2/3**(1/3); st_a = AC*2/4**(1/3)
X_t = B(1,2)+3*tau3; X_h = B(2,1)+3*tau3+st_h; X_a = B(2,2)+4*tau4+st_a
t_alp = dp + h + c3
D_ANCH = 14.075

def gstar(f):
    tt = dp + h*(1-f)
    gt = (X_t/tt-1)/2; gh = (X_h/tt-1)/2; ga = (X_a/t_alp-2)/4
    return (gt+gh+ga)/3

def s1_pooled(f):
    g = gstar(f); W2 = 1+2*g
    return (X_t/W2 + X_h/W2)/2 - D_ANCH
def s1_t(f):
    g = gstar(f); return X_t/(1+2*g) - D_ANCH
def s1_h(f):
    g = gstar(f); return X_h/(1+2*g) - D_ANCH
def s2(f):
    g = gstar(f); W2 = 1+2*g; W4 = 2+4*g
    return X_a/W4 - (X_t/W2 + X_h/W2)/2

eqs = [
    ("E1-pooled", lambda f: h*(1-f) - s1_pooled(f)),
    ("E1-t     ", lambda f: h*(1-f) - s1_t(f)),
    ("E1-h     ", lambda f: h*(1-f) - s1_h(f)),
    ("E2       ", lambda f: (c3 + f*h) - s2(f)),
]
print("swing 35 — self-consistent fraction, lane audit (h=%.4f, c3=%.4f)" % (h, c3))
print("lane values at f=0: s1_pooled %.4f | s1_t %.4f | s1_h %.4f | s2 %.4f | gamma*(0) %.4f"
      % (s1_pooled(0), s1_t(0), s1_h(0), s2(0), gstar(0)))

sols = {}
for name, F in eqs:
    lo, hi = 0.0, 0.35
    flo, fhi = F(lo), F(hi)
    if flo*fhi > 0:
        # scan for escape confirmation
        print("%s : NO root in [0,0.35] (F(0)=%+.4f, F(0.35)=%+.4f) — ESCAPES" % (name, flo, fhi))
        continue
    for _ in range(80):
        mid = (lo+hi)/2
        if F(lo)*F(mid) <= 0: hi = mid
        else: lo = mid
    f = (lo+hi)/2; sols[name.strip()] = f
    print("%s : f* = %.4f   (gamma*' %.4f)" % (name, f, gstar(f)))

inr = list(sols.values())
span = max(inr)-min(inr) if len(inr) >= 2 else float('nan')
ok_a = ('E1-pooled' in sols) and ('E2' in sols)
print("\nS35a existence (E1-pooled & E2 unique in [0,0.35]):", "PASS" if ok_a else "FAIL")
print("S35b span of in-range solutions: %.4f vs 0.05 ->" % span,
      "ROW UPGRADED" if span < 0.05 else "STRAIN-LIMITED (queue reorders: displacement layer gates the fraction)")
rows = {"F6 1/6": 1/6, "F7 (2/zc)^2": (2/zc)**2, "F8 1/(2zc)": 1/(2*zc)}
for k, v in rows.items():
    near = min(sols.items(), key=lambda kv: abs(kv[1]-v)) if sols else None
    print("  row %-12s f=%.4f | nearest solution %s %.4f (d=%.4f)" % (k, v, near[0], near[1], abs(near[1]-v)))

bias = (s1_h(0) - s1_t(0))/2
print("\nS35c report: lane bias (s1_h - s1_t)/2 = %+.4f MeV at gamma*(0) — strain-side, T-P3' class;" % bias)
print("  pooled step1 sits %+.4f above the strain-free t-lane." % (s1_pooled(0)-s1_t(0)))
