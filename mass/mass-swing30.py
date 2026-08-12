#!/usr/bin/env python3
# Swing 30 — gamma triangulation. Registration: 1fbb6ec (pre-run).
# The derived credits make each cluster extraction an equation in gamma alone.
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

# chain z_c + derived credits
xi = 2*HBARC/MN
sin_t = 2*RQ/(2*RQ + xi)
zc = 2.0/(1.0 - math.sqrt(1 - sin_t*sin_t))
dp = HB2M/(4*RQ*RQ); c3 = HB2M*0.75/(18*RQ*RQ); h = 2*c3/zc
t_tri = dp + h            # trinucleon target
t_alp = dp + h + c3       # alpha target
print("credits: dp=%.4f h=%.4f c3=%.4f | targets: tri %.4f alpha %.4f | z_c=%.4f"
      % (dp, h, c3, t_tri, t_alp, zc))

# muonic radii (swing-25 chain)
def pp2(rc, Z, N): return rc*rc - RP2 - (N/Z)*RN2
tri_r2 = (2*pp2(1.9661,2,1) + pp2(1.7591,1,2))/3.0
a_r2 = pp2(1.67824,2,2)
tau3 = (9.0/8.0)*HB2M*(2.0/3.0)/tri_r2
tau4 = (9.0/8.0)*HB2M*(3.0/4.0)/a_r2
st_h = AC*2/3**(1.0/3.0); st_a = AC*2/4**(1.0/3.0)

# the three gamma equations
g_h = ((B_h + 3*tau3 + st_h)/t_tri - 1.0)/2.0
g_t = ((B_t + 3*tau3)/t_tri - 1.0)/2.0
g_a = ((B_a + 4*tau4 + st_a)/t_alp - 2.0)/4.0
gstar = (g_h + g_t + g_a)/3.0
spread = max(g_h, g_t, g_a) - min(g_h, g_t, g_a)
print("\nTHE TRIANGULATION:")
print("  gamma_t = %.4f   gamma_h = %.4f   gamma_alpha = %.4f" % (g_t, g_h, g_a))
print("  joint gamma* = %.4f   spread = %.4f" % (gstar, spread))
print("\nS30a COHERENCE (spread < 0.05):", "PASS — %.1fx conditional sharpening" % (0.10/spread) if spread < 0.05 else "FAIL")
print("S30b CONSISTENCY (gamma* in [0.80, 0.90]):", "PASS (%.1f%% below import central)" % (100*(0.85-gstar)/0.85) if 0.80 <= gstar <= 0.90 else "FAIL")

# S30c residual structure at gamma*
W2 = 1 + 2*gstar; W4 = 2 + 4*gstar
d_d = 14.075  # muonic pair anchor (swing 25)
z2 = ((B_h + 3*tau3 + st_h)/W2 + (B_t + 3*tau3)/W2)/2.0
da = (B_a + 4*tau4 + st_a)/W4
s1 = z2 - d_d; s2 = da - z2; tot = da - d_d
print("\nS30c residuals at gamma* (signed):")
print("  ladder: d %.3f | z2 %.3f | alpha %.3f" % (d_d, z2, da))
print("  step1 %.3f vs h %.3f -> h runs %+.1f%%" % (s1, h, 100*(h-s1)/s1))
print("  step2 %.3f vs c3 %.3f -> c3 runs %+.1f%%" % (s2, c3, 100*(c3-s2)/s2))
print("  sum   %.3f vs h+c3 %.3f -> %+.1f%%" % (tot, h+c3, 100*(h+c3-tot)/tot))
print("  suppression s = step1/c3 = %.3f vs 2/z_c = %.4f -> %+.1f%%"
      % (s1/c3, 2/zc, 100*(2/zc - s1/c3)/(s1/c3)))

# S30d a_sym ripple
EF3 = 11.1
for label, g in (("import 0.85", 0.85), ("gamma*", gstar)):
    # swing-5 contact term scale: total 24.0-24.9 at gamma band; use central 24.45 at 0.85 to extract C
    C_term = (24.45 - EF3)*(1 + 2*0.85)
    total = EF3 + C_term/(1 + 2*g)
    print("S30d a_sym at %-12s = %.2f (shadow 23.2-23.7, %+.1f%% vs 23.45)"
          % (label, total, 100*(total-23.45)/23.45))
print("\nGRADE: CONDITIONAL (theory-conditioned). Import gamma = 0.85(5) unchanged; no re-anchor.")
