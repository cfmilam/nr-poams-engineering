#!/usr/bin/env python3
# Swing 32 — credit transfer through the shared bond. Registration: 72428eb (pre-run).
# Scored at FROZEN gamma* = swing-30 extraction; fork table frozen in registration.
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
B_d, B_t, B_h, B_a = B(1,1), B(1,2), B(2,1), B(2,2)

# chain z_c + derived credits (identical to swing 30)
xi = 2*HBARC/MN
sin_t = 2*RQ/(2*RQ + xi)
cos_t = math.sqrt(1 - sin_t*sin_t)
zc = 2.0/(1.0 - cos_t)
dp = HB2M/(4*RQ*RQ); c3 = HB2M*0.75/(18*RQ*RQ); h = 2*c3/zc
t_tri = dp + h; t_alp = dp + h + c3

# muonic radii chain (swing 25)
def pp2(rc, Z, N): return rc*rc - RP2 - (N/Z)*RN2
tri_r2 = (2*pp2(1.9661,2,1) + pp2(1.7591,1,2))/3.0
a_r2 = pp2(1.67824,2,2)
tau3 = (9.0/8.0)*HB2M*(2.0/3.0)/tri_r2
tau4 = (9.0/8.0)*HB2M*(3.0/4.0)/a_r2
st_h = AC*2/3**(1.0/3.0); st_a = AC*2/4**(1.0/3.0)

# frozen gamma* (swing-30 extraction, recomputed identically)
g_h = ((B_h + 3*tau3 + st_h)/t_tri - 1.0)/2.0
g_t = ((B_t + 3*tau3)/t_tri - 1.0)/2.0
g_a = ((B_a + 4*tau4 + st_a)/t_alp - 2.0)/4.0
gstar = (g_h + g_t + g_a)/3.0
W2 = 1 + 2*gstar; W4 = 2 + 4*gstar
d_anchor = 14.075
z2 = ((B_h + 3*tau3 + st_h)/W2 + (B_t + 3*tau3)/W2)/2.0
da = (B_a + 4*tau4 + st_a)/W4
s1 = z2 - d_anchor; s2 = da - z2; tot = da - d_anchor
print("frozen state: z_c=%.4f dp=%.4f h=%.4f c3=%.4f | gamma*=%.4f" % (zc, dp, h, c3, gstar))
print("measured at gamma*: step1=%.4f step2=%.4f sum=%.4f" % (s1, s2, tot))
base1 = abs(h - s1)/s1; base2 = abs(c3 - s2)/s2
print("baseline residuals: step1 %+.2f%% step2 %+.2f%% (improvement thresholds %.2f%% / %.2f%%)"
      % (100*(h-s1)/s1, 100*(c3-s2)/s2, 90*base1, 90*base2))

# THE FROZEN FORK TABLE (registration 72428eb)
forks = [
    ("F1 1/3 closing-vertex excess", 1.0/3.0),
    ("F2 1/2 even per-bond",         0.5),
    ("F3 2/z_c re-suppression",      2.0/zc),
    ("F4 cos^2(theta_w) projector",  cos_t*cos_t),
    ("F5 1/z_c patch budget",        1.0/zc),
    ("F6 1/6 half closing-vertex",   1.0/6.0),
    ("F7 (2/z_c)^2 second sweep",    (2.0/zc)**2),
    ("F8 1/(2z_c) patch per turn",   1.0/(2*zc)),
]
print("\n%-34s %-7s %-7s %-7s %-6s %-6s %-6s %-6s verdict" %
      ("fork", "f", "h'", "c3'", "G32a", "G32b", "G32c", "G32d"))
survivors = []
for name, f in forks:
    d = f*h; hp = h - d; cp = c3 + d; sm = hp + cp
    a = 0.75 <= hp <= 0.95
    b = 2.35 <= cp <= 2.58
    c = abs(sm - tot)/tot < 0.03
    r1 = abs(hp - s1)/s1; r2 = abs(cp - s2)/s2
    dgate = (r1 < 0.9*base1) and (r2 < 0.9*base2)
    ok = a and b and c and dgate
    if ok: survivors.append((name, f, hp, cp, r1, r2))
    print("%-34s %.4f  %.4f  %.4f  %-6s %-6s %-6s %-6s %s" %
          (name, f, hp, cp, a, b, c, dgate, "SURVIVES" if ok else "dead"))

print("\nSURVIVORS (%d):" % len(survivors))
for name, f, hp, cp, r1, r2 in survivors:
    print("  %-34s h' %.4f (res %+.2f%%)  c3' %.4f (res %+.2f%%)" %
          (name, hp, 100*(hp-s1)/s1, cp, 100*(cp-s2)/s2))

# DIAGNOSTIC 1: re-triangulation at each survivor (reported signed, unclaimed)
print("\nre-triangulation diagnostic (unclaimed):")
X_t = B_t + 3*tau3; X_h = B_h + 3*tau3 + st_h; X_a = B_a + 4*tau4 + st_a
for name, f, hp, cp, r1, r2 in survivors:
    tt = dp + hp  # transferred trinucleon target; alpha target invariant
    gt = (X_t/tt - 1)/2; gh = (X_h/tt - 1)/2; ga = (X_a/t_alp - 2)/4
    gs = (gt+gh+ga)/3; sp = max(gt,gh,ga)-min(gt,gh,ga)
    print("  %-34s gamma_t %.4f gamma_h %.4f gamma_a %.4f | gamma*' %.4f spread %.4f (was 0.0142)"
          % (name, gt, gh, ga, gs, sp))

# DIAGNOSTIC 2: one fixed-point iteration at the derived central F6 (convergence note only)
f6 = 1.0/6.0
tt = dp + h*(1-f6)
gt = (X_t/tt - 1)/2; gh = (X_h/tt - 1)/2; ga = (X_a/t_alp - 2)/4
gs2 = (gt+gh+ga)/3
W2i = 1+2*gs2; W4i = 2+4*gs2
z2i = (X_h/W2i + X_t/W2i)/2.0; dai = X_a/W4i
s1i = z2i - d_anchor; s2i = dai - z2i
hp = h*(1-f6); cp = c3 + f6*h
print("\nfixed-point iteration at F6 (note only): gamma*' %.4f -> steps %.4f / %.4f;"
      % (gs2, s1i, s2i))
print("  predicted %.4f / %.4f -> residuals %+.2f%% / %+.2f%% (frozen-gamma* scoring stands)"
      % (hp, cp, 100*(hp-s1i)/s1i, 100*(cp-s2i)/s2i))

# invariance checks (declared): alpha total, sum class
print("\ninvariance: alpha target %.4f unchanged under every row; sum %.4f all rows (%+.2f%% vs measured)"
      % (t_alp, h+c3, 100*((h+c3)-tot)/tot))
