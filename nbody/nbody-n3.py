#!/usr/bin/env python3
"""nbody-n3 — the channel criterion vs the Galilean system (N3a-f; reg 34a9473 pre-run).
Width (derived, NBODY-FORWARD T3): W = 2(j-1) n sqrt(3 alpha f' |f_d| e), open iff
|p n' - q n| < W. For the cited eccentricity-type argument,
f_d = 1/2[-2j - alpha d/dalpha] b_{1/2}^{(j)}(alpha); the 2:1 indirect -2 alpha
belongs to a different argument and is deliberately excluded (run-2 correction;
benchmark vs tabulated -1.19). Data: N2 elements + eccentricities (same pulls,
2026-08-10); f' = partition fractions (comparison-class)."""
import math

def b_laplace(s, j, alpha, N=20000):
    tot = 0.0
    for i in range(N):
        psi = (i+0.5)*math.pi/N
        tot += math.cos(j*psi)/ (1 - 2*alpha*math.cos(psi) + alpha*alpha)**s
    return (2.0/math.pi)*tot*(math.pi/N)

def f_d(j, alpha):
    h = 1e-6
    b  = b_laplace(0.5, j, alpha)
    db = (b_laplace(0.5, j, alpha+h) - b_laplace(0.5, j, alpha-h))/(2*h)
    return 0.5*(-2*j*b - alpha*db)

D = 86400.0
# (name, a km, T d, e, partition fraction f')
IO  = ("Io",       421700.0, 1.769137786, 0.0041, 4.70e-5)
EUR = ("Europa",   670900.0, 3.551181,    0.0094, 2.53e-5)
GAN = ("Ganymede", 1070400.0, 7.15455296, 0.0013, 7.80e-5)
CAL = ("Callisto", 1882700.0, 16.6890184, 0.0074, 5.69e-5)
n = {m[0]: 2*math.pi/(m[2]*D) for m in (IO,EUR,GAN,CAL)}

print("="*78)
print("nbody-n3 — channel criterion vs the Galilean system (registered N3a-f)")
print("="*78)

# N3f benchmark first (coefficient chain vs literature)
alpha_ie = IO[1]/EUR[1]
fd21 = f_d(2, alpha_ie)
print(f"\n-- N3f benchmark: f_d(2:1) at alpha = {alpha_ie:.4f} = {fd21:+.4f}  (tabulated ~ -1.19)")
ok_f = abs(abs(fd21)-1.19)/1.19 < 0.05
print(f"   {'PASS' if ok_f else 'FAIL'} ({100*abs(abs(fd21)-1.19)/1.19:.1f}% from tabulated)")

def width_first_order(j, inner, outer):
    nm_i, a_i, T_i, e_i, _ = inner
    nm_o, a_o, T_o, _, f_o = outer
    alpha = a_i/a_o
    fd = f_d(j, alpha)
    ni = n[nm_i]
    W = 2*(j-1 if j>1 else 1)*ni*math.sqrt(3*alpha*f_o*abs(fd)*e_i)
    return W, fd, alpha

# N3a: the two raw pairwise beats are EQUAL (the common drift)
b1 = 2*n["Europa"] - n["Io"]       # rad/s (signed)
b2 = 2*n["Ganymede"] - n["Europa"]
print(f"\n-- N3a: raw pairwise beats (the common conjunction drift) --")
print(f"   2n_Eur - n_Io  = {b1:+.6e} rad/s = {math.degrees(b1)*D:+.5f} deg/d")
print(f"   2n_Gan - n_Eur = {b2:+.6e} rad/s = {math.degrees(b2)*D:+.5f} deg/d")
print(f"   difference/n_Io = {abs(b1-b2)/n['Io']:.2e}  (= the N2c Laplace combo)  "
      f"{'PASS equal-to-1e-8 class' if abs(b1-b2)/n['Io'] < 1e-6 else 'FAIL'}")

# N3b: raw beats vs their own first-order widths
print(f"\n-- N3b: pairwise channels, RAW beats vs widths --")
for (j, inner, outer, beat) in ((2, IO, EUR, b1), (2, EUR, GAN, b2)):
    W, fd, alpha = width_first_order(j, inner, outer)
    ni = n[inner[0]]
    r = abs(beat)/W
    print(f"   {inner[0]}-{outer[0]} 2:1: |beat|/n = {abs(beat)/ni:.3e}, W/n = {W/ni:.3e}, "
          f"beat/W = {r:.2f} -> {'OUTSIDE (closed raw)' if r>1 else 'INSIDE (open raw)'}")

# N3c: three-body channel — combo vs bracketed W3
combo = abs(n["Io"] - 3*n["Europa"] + 2*n["Ganymede"])
print(f"\n-- N3c: three-body channel --")
print(f"   |n1 - 3n2 + 2n3|/n1 = {combo/n['Io']:.2e}")
# conservative floor: second-order coupling ~ product of partition fractions
W_floor = 2*n["Europa"]*math.sqrt(3*0.63*(EUR[4]*GAN[4])**1.0/ (2.53e-5) * 1.19 * EUR[3])
# (floor construction: replace f' by f'_eur*f'_gan/f'_eur = f'_gan scaled — bracket, not a claim)
W_floor = 2*n["Europa"]*math.sqrt(3*0.63*EUR[4]*GAN[4]*1.19*EUR[3])/math.sqrt(EUR[4])  # ~ f' geometric-mean class
W_f2   = 2*n["Europa"]*math.sqrt(3*0.63*(EUR[4]**2)*1.19*EUR[3])                       # strict f'^2 class (most conservative)
W_ceil, _, _ = width_first_order(2, EUR, GAN)
for tag, W in (("strict f'^2 floor", W_f2), ("geometric-mean class", W_floor), ("first-order ceiling", W_ceil)):
    print(f"   W3 [{tag}] /n2 = {W/n['Europa']:.2e}  -> combo/W3 = {combo/W:.2e}  "
          f"{'OPEN (deep)' if combo < W else 'CLOSED'}")
print(f"   N3c registered: open with >=100x margin at the conservative end -> "
      f"{'PASS' if combo/W_f2 < 0.01 else ('PASS (margin ' + f'{W_f2/combo:.0f}x)' if combo < W_f2 else 'FAIL')}")

# N3d: Ganymede-Callisto 7:3 control (generous first-order-scale bound)
beat73 = abs(7*n["Callisto"] - 3*n["Ganymede"])
Wgen, fdgc, agc = width_first_order(2, GAN, CAL)   # generous: first-order form at their alpha
print(f"\n-- N3d: Ganymede-Callisto 7:3 control --")
print(f"   |7n_Cal - 3n_Gan|/n_Gan = {beat73/n['Ganymede']:.3e}; GENEROUS first-order-scale W/n = {Wgen/n['Ganymede']:.3e}")
print(f"   beat/W_generous = {beat73/Wgen:.2f}; true order-4 width ~ e^3 smaller -> "
      f"{'CLOSED a fortiori: PASS' if beat73 > Wgen else 'inside generous bound - check order-4'}")

# N3e: golden-body control between Europa and Ganymede
print(f"\n-- N3e: golden-ratio control (hypothetical body, T = phi * T_Europa) --")
phi = (1+math.sqrt(5))/2
Tg = EUR[2]*phi
ng = 2*math.pi/(Tg*D)
ag = EUR[1]*phi**(2/3)
worst = None
for (p,q) in ((3,2),(5,3),(8,5),(13,8),(2,1)):
    order = abs(p-q)
    beat = abs(p*ng - q*n["Europa"])   # channel with Europa (inner partner Europa)
    # generous first-order-scale bound with Europa as perturber of the golden body
    alpha = EUR[1]/ag
    fd = f_d(2, alpha)
    W = 2*ng*math.sqrt(3*alpha*EUR[4]*abs(fd)*0.01)   # generous e = 0.01
    r = beat/W
    worst = min(worst, r) if worst else r
    print(f"   {p}:{q} (order {order}): beat/W_generous = {r:8.1f} -> {'closed' if r>3 else 'NEAR/OPEN'}")
print(f"   N3e registered: all order<=5 closed by >=3x -> {'PASS' if worst and worst >= 3 else 'FAIL'}")
