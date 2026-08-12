#!/usr/bin/env python3
# Swing 25 — THE RECONCILIATION. Registration: b58a995 (pre-run).
# Chain z_c + muonic radii as operational centrals; recompute everything.
import math, re

HB2M = 41.47; AC = 0.72; HBARC = 197.327; MN = 938.92
RP2 = 0.8409**2; RN2 = -0.1155
RQ = 0.86; AV = 15.75; TAUB = 20.1; CBOOKS = AV + TAUB

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

# chain z_c
xi = 2*HBARC/MN
sin_t = 2*RQ/(2*RQ + xi)
zc = 2.0/(1.0 - math.sqrt(1 - sin_t*sin_t))
print("z_c(chain) = %.4f   xi = %.4f" % (zc, xi))

# muonic ladder
def pp2(rc, Z, N): return rc*rc - RP2 - (N/Z)*RN2
d_r2 = pp2(2.12799, 1, 1)
h_r2 = pp2(1.9661, 2, 1); t_r2 = pp2(1.7591, 1, 2)
tri_r2 = (2*h_r2 + t_r2)/3.0
a_r2 = pp2(1.67824, 2, 2)
def tau(n, r2): return (9.0/8.0)*HB2M*(1.0-1.0/n)/r2
def strain(Z, A): return AC*Z*(Z-1)/A**(1.0/3.0)
def d0(Bv, Z, N, r2, n, s, w, g=0.85):
    return (Bv + (Z+N)*tau(n,r2) + strain(Z,Z+N))/(s + w*g)
dd = d0(B(1,1),1,1,d_r2,2,1,0)
dh = d0(B(2,1),2,1,tri_r2,3,1,2)
dt = d0(B(1,2),1,2,tri_r2,3,1,2)
da = d0(B(2,2),2,2,a_r2,4,2,4)
z2 = (dh+dt)/2
print("ladder: d %.3f | z2 %.3f (h %.3f / t %.3f, split %.3f) | alpha %.3f"
      % (dd, z2, dh, dt, abs(dh-dt), da))
print("steps: %+.2f, %+.2f | alpha-total %+.2f" % (z2-dd, da-z2, da-dd))

dp = HB2M/(4*RQ*RQ); c3 = HB2M*0.75/(18*RQ*RQ); c4 = HB2M*0.5/(32*RQ*RQ)
h = 2*c3/zc; s = 2/zc; dbar = 2*CBOOKS/zc
print("\nCONFRONTATIONS (signed):")
print("  pair anchor: %.3f derived vs %.3f -> %+.2f%%" % (dp, dd, 100*(dp-dd)/dd))
print("  c3 marginal: %.3f vs %.2f -> %+.1f%%" % (c3, da-z2, 100*(c3-(da-z2))/(da-z2)))
print("  h = %.3f  s = %.4f (gamma-limited vs step1 %.2f)" % (h, s, z2-dd))
print("  two-loop sum: %.3f vs %.2f -> %+.1f%% (gamma band on step [2.35,3.61]: %s)"
      % (h+c3, da-dd, 100*(h+c3-(da-dd))/(da-dd), 2.35 <= h+c3 <= 3.61))
print("  deltabar = %.3f in Rule-C bracket [14.02, 15.74]: %s ; functional gross 14.47/15.31 straddles: %s"
      % (dbar, 14.02 <= dbar <= 15.74, 14.47 <= dbar <= 15.31))
print("  level identity: delta0(z_c) = %.2f  (band ~[20.5, 22.6])" % (dbar/0.675))

# crown books (swing-19 censuses, h updated)
for name, zbar, Tm, Qm, Em, fb, n3c3, n4c4 in ():
    pass
# functional: z=4.891 E=626 T(raw)=89 Q(raw chordless)=113 fb=0.79 (swing 19)
def booksR1(zbar, E, ntri_sum, nquad_sum, nb_first_frac):
    tot = h*nb_first_frac*E + (ntri_sum - nb_first_frac*E*0)*0  # placeholder
    return None
# use swing-19 measured per-bond composition: credR1(central, h=0.978) was g=15.16-14.018=1.142
# h enters via fb=0.79 share: adjust credit by (h_new - 0.978)*fb
for name, zbar, gross_old, fb in (("functional", 4.891, 15.16, 0.79), ("liquid", 4.594, 15.29, 0.80)):
    gross = gross_old + (h - 0.978)*fb
    G = min(zbar, zc)/2.0*gross
    print("  books %s: gross %.2f -> G = %.2f (%+.1f%% vs C = %.2f) in [32,40]: %s"
          % (name, gross, G, 100*(G-CBOOKS)/CBOOKS, CBOOKS, 32 <= G <= 40))

a_s_derived = 18.39
Astar = 2*(a_s_derived/AV)*(AV/AC)
print("  T-PEAK: A* = %.1f in registered [49, 66] (measured 62): %s" % (Astar, 49 <= Astar <= 66))
print("\nS25 gates: compare against registered hand values; shifts booked signed in ledger.")
