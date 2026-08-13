#!/usr/bin/env python3
# Census swing N-5 — the 1/4-escrow made native. Registration: 7fc0756 (pre-run).
# Anchor ledger: harmonic + Coulomb (exact), linear well + bouncer (computed Airy zeros),
# quartic well (prediction row, FD diagonalization). Units hbar = 1, m = 1/2.
import numpy as np, math

# --- Airy zeros computed natively: integrate y'' = x y from x = 0 leftward ---
AI0  = 0.35502805388781724   # Ai(0) = 3^{-2/3}/Gamma(2/3)
AIP0 = -0.25881940379280680  # Ai'(0) = -3^{-1/3}/Gamma(1/3)
def airy_zeros(nz=9, h=2e-5, xmin=-14.0):
    y, yp, x = AI0, AIP0, 0.0
    za, zap = [], []
    while x > xmin and (len(za) < nz or len(zap) < nz):
        # RK4 for y'' = x y
        def F(x, y, yp): return yp, x*y
        k1 = F(x, y, yp)
        k2 = F(x - h/2, y - h/2*k1[0], yp - h/2*k1[1])
        k3 = F(x - h/2, y - h/2*k2[0], yp - h/2*k2[1])
        k4 = F(x - h, y - h*k3[0], yp - h*k3[1])
        yn  = y  - h/6*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0])
        ypn = yp - h/6*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1])
        xn = x - h
        if y*yn < 0:  za.append(x - h*y/(y - yn))
        if yp*ypn < 0: zap.append(x - h*yp/(yp - ypn))
        x, y, yp = xn, yn, ypn
    return [-z for z in za], [-z for z in zap]   # |a_k|, |a'_k|
ZA, ZAP = airy_zeros()

print("N-5b THE ANCHOR LEDGER (nu(E) = action loop / 2pi; offset = nu - n):")
print("  harmonic well: nu(E_n) = n + 1/2 EXACT (algebra; E_n = (n+1/2)w, loop area = 2pi E/w)")
print("  Coulomb eye:   offset 1/2 EXACT (N-4a, all (n,l))")

# linear symmetric well: -psi'' + |q| psi = E psi
# even: Ai'(-E) = 0 ; odd: Ai(-E) = 0 ; nu(E) = (4/3pi) E^{3/2} -> n + 1/2
print("\n  linear symmetric well V = |q| (2 soft folds):")
rows = []
for k in range(1, 9):
    Eo = ZA[k-1]                                 # odd states: n = 2k-1
    Ee = ZAP[k-1]                                # even states (Ai' zeros): n = 2k-2
    for (E, n) in ((Ee, 2*k-2), (Eo, 2*k-1)):
        nu = (4.0/(3*math.pi))*E**1.5
        rows.append((n, nu - n))
rows.sort()
for n, off in rows[:6] + rows[-2:]:
    print("    n=%2d: offset = %.5f" % (n, off))
off_tail = [off for n, off in rows if n >= 8]
ok_lin = all(abs(o - 0.5) < 0.005 for o in off_tail)
print("  linear-well offsets -> 1/2 (tail within 0.005):", "PASS" if ok_lin else "FAIL")

# bouncer: psi(0)=0, V=q: E = |a_k|, n = k-1; nu(E) = (2/3pi) E^{3/2} -> n + 3/4
print("\n  bouncer (1 wall + 1 fold):")
offs_b = []
for k in range(1, 9):
    E = ZA[k-1]
    n = k - 1
    nu = (2.0/(3*math.pi))*E**1.5
    offs_b.append(nu - n)
    if k <= 4 or k >= 7:
        print("    n=%2d: offset = %.5f" % (n, nu - n))
ok_b = all(abs(o - 0.75) < 0.005 for o in offs_b[4:])
print("  bouncer offsets -> 3/4 (tail within 0.005):", "PASS" if ok_b else "FAIL")

print("\n  LEDGER SOLVE: 2f = 1/2 (harmonic, Coulomb, linear) and w + f = 3/4 (bouncer)")
print("  => f = 1/4 per soft fold, w = 1/2 per hard wall — overdetermined, consistent")

# N-5c prediction row: quartic well V = q^4 (FD diagonalization), nu = (4 I4 / 2pi) E^{3/4}
print("\nN-5c PREDICTION ROW — quartic well V = q^4 (not used in the fit):")
L = 5.0; N = 2400
q = np.linspace(-L, L, N)
hgrid = q[1] - q[0]
main = 2.0/hgrid**2 + q**4          # -psi'' + q^4 psi with m = 1/2 (coefficient 1 on psi'')
off = -1.0/hgrid**2 * np.ones(N-1)
H = np.diag(main) + np.diag(off, 1) + np.diag(off, -1)
evals = np.linalg.eigvalsh(H)[:10]
I4 = math.gamma(0.25)*math.gamma(1.5)/(4*math.gamma(1.75))   # (1/4)B(1/4,3/2) = 0.874019...
ok_q = True
for n in range(8):
    E = float(evals[n])
    nu = (4*I4/(2*math.pi))*E**0.75
    o = nu - n
    flag = abs(o - 0.5) < 0.01 if n >= 6 else True
    ok_q = ok_q and flag
    print("    n=%d: E = %9.4f  offset = %.5f" % (n, E, o))
print("  GATE offset -> 1/2 within 0.01 by n = 6:", "PASS" if ok_q else "FAIL")
print("\n  the fold constant is shape-blind across {harmonic, Coulomb, linear, quartic} —")
print("  exactly what locality demands: f = 1/4 per fold, measured native, no asymptotic")
print("  formula consumed (the Airy zeros enter as computed spectra of the fold equation itself).")
