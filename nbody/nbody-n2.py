#!/usr/bin/env python3
"""nbody-n2 — pair-invariant consistency at Jupiter (N2a/b/c; registration 3042d63 pre-data).
DATA (retrieved 2026-08-10, en.wikipedia.org moon infoboxes; hygiene notes below):
  Io:       a = 421700 km (mean orbit radius),  T = 1.769137786 d, e = 0.0040313
  Europa:   a = 670900 km (mean orbit radius),  T = 3.551181 d
  Ganymede: a = 1070400 km (semi-major axis),   T = 7.15455296 d
  Callisto: a = 1882700 km (semi-major axis),   T = 16.6890184 d
  HYGIENE (pre-named branch): the Galilean-moons summary table gives Io 421800,
  Europa 671100 (vs infobox 421700/670900): 2-3e-4 source-internal spread on a;
  'mean orbit radius' vs 'semi-major axis' labels mixed. a-precision ~1e-4 class.
COMPARISON ONLY (never engine input): masses m_i = {8.93e22, 4.8e22, 1.48e23,
  1.08e23} kg, M_J = 1.898e27 kg -> partition fractions m_i/M_J."""
import math
D = 86400.0
moons = [
    ("Io",       421700.0, 1.769137786, 8.93e22),
    ("Europa",   670900.0, 3.551181,    4.8e22),
    ("Ganymede", 1070400.0, 7.15455296, 1.48e23),
    ("Callisto", 1882700.0, 16.6890184, 1.08e23),
]
MJ = 1.898e27
print("="*78)
print("nbody-n2 — four pairwise invariants at Jupiter, no G, no masses")
print("="*78)
mus = []
for (nm, a, Td, m) in moons:
    mu = 4*math.pi**2 * a**3 / (Td*D)**2
    mus.append(mu)
    print(f"  {nm:9s} a = {a:9.0f} km  T = {Td:11.7f} d  ->  mu = {mu:,.0f} km^3/s^2")
mean = sum(mus)/4
spread = (max(mus)-min(mus))/mean
print(f"\n-- N2a: books close? --")
print(f"  mean mu = {mean:,.0f} km^3/s^2   [comparison: GM_J ~ 1.26687e8 -> {100*abs(mean-1.26687e8)/1.26687e8:.3f}%]")
print(f"  spread (max-min)/mean = {spread:.2e}  registered < 5e-4 -> {'PASS' if spread < 5e-4 else 'FAIL -> hygiene branch'}")
print(f"  per-moon residuals about mean (x1e4):", ["%+.2f" % (1e4*(mu-mean)/mean) for mu in mus])
print(f"\n-- N2b: does the pairwise invariant read the partner's ledger weight? --")
fr = [m/MJ for (_,_,_,m) in moons]
print(f"  partition fractions m_i/M_J (comparison, x1e5):", ["%.2f" % (1e5*f) for f in fr])
pred_rank = sorted(range(4), key=lambda i: -fr[i])
obs_rank  = sorted(range(4), key=lambda i: -(mus[i]-mean))
names = [m[0] for m in moons]
print(f"  registered rank (by partition): {[names[i] for i in pred_rank]}")
print(f"  observed rank (by mu residual): {[names[i] for i in obs_rank]}")
match = pred_rank == obs_rank
resid_scale = max(abs(mu-mean)/mean for mu in mus)
sig_scale = max(fr) - min(fr)
print(f"  residual scale {resid_scale:.1e} vs partition signal {sig_scale:.1e}")
if resid_scale > 3*sig_scale:
    print(f"  N2b VERDICT: DATA-PRECISION-LIMITED (pre-named outcome): a-rounding noise")
    print(f"  ({resid_scale:.0e}) exceeds the partition signal ({sig_scale:.0e}); rank test not scoreable")
    print(f"  against these public elements. Rank match anyway: {match}.")
else:
    print(f"  N2b VERDICT: {'PASS (1/24 by chance)' if match else 'FAIL'}")
print(f"\n-- N2c: the Laplace channel, sized from the fetched periods --")
n = [2*math.pi/(Td*D) for (_,_,Td,_) in moons]
combo = n[0] - 3*n[1] + 2*n[2]
rel = abs(combo)/n[0]
print(f"  mean motions n_i (rad/s): Io {n[0]:.6e}  Eur {n[1]:.6e}  Gan {n[2]:.6e}")
print(f"  Laplace combination n_Io - 3 n_Eur + 2 n_Gan = {combo:+.3e} rad/s")
print(f"  |combo|/n_Io = {rel:.2e}   registered < 1e-5 -> {'PASS' if rel < 1e-5 else 'FAIL'}")
print(f"  pairwise ratios (NOT integers - the lock is three-body):")
print(f"    T_Eur/T_Io = {moons[1][2]/moons[0][2]:.5f}   T_Gan/T_Eur = {moons[2][2]/moons[1][2]:.5f}")
print(f"  Callisto control: T_Cal/T_Gan = {moons[3][2]/moons[2][2]:.5f} (near 7/3 = {7/3:.5f} but off; no exact")
print(f"    combination involves Callisto - the out-of-lock control as registered)")
print(f"\n  READING: nothing in T1 (four independent pairwise ledgers) relates the three")
print(f"  periods; yet the three-body combination vanishes {1e-5/max(rel,1e-30):.0f}x deeper than the")
print(f"  registered bound. The lock is not pairwise commensurability (ratios 2.007, 2.015)")
print(f"  but a three-body PHASE closure - the open inter-resonance channel, empirically")
print(f"  sized. This is T3's object.")
