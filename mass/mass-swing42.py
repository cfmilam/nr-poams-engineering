#!/usr/bin/env python3
# Swing 42 — two-mesh share: sensitivity theorem + the two pins. Reg: f44a8d3 (pre-run).
import math, re

HB2M = 41.47; AC = 0.72
HBARC = 197.327; MN = 938.92
RP2 = 0.8409**2; RN2 = -0.1155
CG = math.sqrt(6/math.pi)

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

def pp2(rc,Z,N): return rc*rc - RP2 - (N/Z)*RN2
tri_r2 = (2*pp2(1.9661,2,1)+pp2(1.7591,1,2))/3.0; a_r2 = pp2(1.67824,2,2)
tau3 = (9/8)*HB2M*(2/3)/tri_r2; tau4 = (9/8)*HB2M*(3/4)/a_r2
rpp_h = math.sqrt(2*pp2(1.9661,2,1)); rpp_a = math.sqrt(2*pp2(1.67824,2,2))
st_h = 1.44*CG/rpp_h; st_a = 1.44*CG/rpp_a          # strain' (ratified)
X_t = B(1,2)+3*tau3; X_h = B(2,1)+3*tau3+st_h; X_a = B(2,2)+4*tau4+st_a

def gstar(rq):
    """Joint gamma extraction at radius rq, strain' + f=1/6 operational."""
    xi = 2*HBARC/MN
    sin_t = 2*rq/(2*rq+xi); cos_t = math.sqrt(1-sin_t*sin_t)
    zc = 2/(1-cos_t)
    dp = HB2M/(4*rq*rq); c3 = HB2M*0.75/(18*rq*rq); h = 2*c3/zc
    tt = dp + (5/6)*h; ta = dp + h + c3
    gt = (X_t/tt-1)/2; gh = (X_h/tt-1)/2; ga = (X_a/ta-2)/4
    return (gt+gh+ga)/3, max(gt,gh,ga)-min(gt,gh,ga), dp

g0, sp0, dp0 = gstar(0.86)
print("S42b-1 gamma* at r_q=0.86: %.4f (spread %.4f, dp %.3f) [hand 0.8314(2)]" % (g0, sp0, dp0))

# sensitivity dgamma/dln r_q (finite difference)
eps = 1e-4
g1, _, _ = gstar(0.86*(1+eps))
sens = (g1-g0)/eps
print("S42b-2 sensitivity dgamma/dln(r_q) = %.3f [hand 2.4-2.9]" % sens)

# pin 1: r_q* for gamma* = 5/6
lo, hi = 0.85, 0.87
for _ in range(60):
    mid = (lo+hi)/2
    if gstar(mid)[0] < 5/6: lo = mid
    else: hi = mid
rqstar = (lo+hi)/2
dpstar = HB2M/(4*rqstar*rqstar)
print("S42b-3 r_q* (gamma*=5/6): %.4f fm -> dp = %.3f vs anchor 14.075 (%+.2f%%) [hand 0.8606, -0.55%%]"
      % (rqstar, dpstar, 100*(dpstar-14.075)/14.075))

# pin 2: anchor-pinned r_q (dp = 14.075)
rq_anch = 0.86*math.sqrt(HB2M/(4*0.86*0.86)/14.075)
g_anch, sp_anch, _ = gstar(rq_anch)
print("S42b-4 anchor-pinned r_q = %.4f -> gamma* = %.4f (5/6 sits %+.4f = %s the 0.004 window) [hand 0.826(1)]"
      % (rq_anch, g_anch, 5/6-g_anch, "OUTSIDE" if abs(5/6-g_anch) > 0.004 else "inside"))

ok = (abs(g0-0.8314) < 0.0004 and 2.4 <= sens <= 2.9 and abs(rqstar-0.8606) < 0.0004
      and abs(g_anch-0.826) < 0.001)
print("S42b VERDICT (all four hand numbers):", "PASS" if ok else "FAIL")

# S42c report: zero-parameter table at exact 5/6, r_q = 0.86
xi = 2*HBARC/MN; sin_t = 2*0.86/(2*0.86+xi); cos_t = math.sqrt(1-sin_t*sin_t)
zc = 2/(1-cos_t); dp = HB2M/(4*0.86**2); c3 = HB2M*0.75/(18*0.86**2); h = 2*c3/zc
W2 = 8/3; W4 = 16/3
z2 = (X_t/W2 + X_h/W2)/2; da = X_a/W4
s1 = z2-14.075; s2 = da-z2
p1 = (5/6)*h; p2 = c3 + h/6
print("\nS42c report (unclaimed) — zero-parameter cluster table at gamma == 5/6 exact:")
print("  W2 = 8/3, W4 = 16/3 | z2 %.4f  alpha %.4f" % (z2, da))
print("  step1 %.4f vs (5/6)h = %.4f -> %+.1f%% | step2 %.4f vs c3+h/6 = %.4f -> %+.1f%% | sum %+.1f%%"
      % (s1, p1, 100*(p1-s1)/s1, s2, p2, 100*(p2-s2)/s2, 100*((p1+p2)-(s1+s2))/(s1+s2)))
print("  [declared class: +11%% / ~0%% / +2.5%%]")
print("\nc3/delta_pair = %.6f (exactly 1/6: %s) — flagged, unclaimed (moment lineage)" %
      (c3/dp, abs(c3/dp-1/6) < 1e-12))
