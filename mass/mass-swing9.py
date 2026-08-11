#!/usr/bin/env python3
# Swing 9 — crown confrontation. Registration: ledger 3737696 (pre-run).
# Surface-phase stiffening: sphere Laplacian, penalty-Dirichlet caps at codes,
# credit S(z) = sum over M softest of sqrt(lambda_i(z)) - sqrt(lambda_i(free)).
import numpy as np

ZC = 4.78
COS_W = 1.0 - 2.0/ZC              # cap half-angle: cos(theta_w) = 1 - 2/z_c
LMAX = 15
MU = (1e4, 1e5)                   # penalty (sensitivity pair)

# ---- real spherical harmonics on a quadrature grid ----
NT, NP = 96, 192
x_gl, w_gl = np.polynomial.legendre.leggauss(NT)   # x = cos(theta)
phi = 2*np.pi*np.arange(NP)/NP
wphi = 2*np.pi/NP

def plm_all(lmax, x):
    """associated Legendre P_l^m(x), normalized real-SH ready; returns dict (l,m)->array"""
    P = {}
    P[(0,0)] = np.ones_like(x)
    for m in range(1, lmax+1):
        P[(m,m)] = -(2*m-1)*np.sqrt(np.maximum(0,1-x*x))*P[(m-1,m-1)]
    for m in range(0, lmax):
        P[(m+1,m)] = (2*m+1)*x*P[(m,m)]
    for m in range(0, lmax+1):
        for l in range(m+2, lmax+1):
            P[(l,m)] = ((2*l-1)*x*P[(l-1,m)] - (l+m-1)*P[(l-2,m)])/(l-m)
    return P

from math import factorial, pi, sqrt
P = plm_all(LMAX, x_gl)
basis = []   # (l, m, kind) kind: 0 cos, 1 sin (m>0), m=0 single
for l in range(LMAX+1):
    for m in range(0, l+1):
        if m == 0: basis.append((l, 0, 0))
        else: basis.append((l, m, 0)); basis.append((l, m, 1))
N = len(basis)
print("basis size:", N)

# evaluate basis on grid: Y[i, itheta, iphi]
Y = np.zeros((N, NT, NP))
for i,(l,m,kind) in enumerate(basis):
    norm = sqrt((2*l+1)/(4*pi) * factorial(l-m)/factorial(l+m))
    if m == 0:
        Y[i] = (norm*P[(l,0)])[:,None]*np.ones(NP)[None,:]
    else:
        norm *= sqrt(2.0)
        az = np.cos(m*phi) if kind==0 else np.sin(m*phi)
        Y[i] = (norm*P[(l,m)])[:,None]*az[None,:]

Wq = w_gl[:,None]*wphi   # quadrature weights (NT,NP)
# orthonormality check
gram = np.einsum('itp,jtp,tp->ij', Y[:6], Y[:6], Wq)
print("orthonormality err (first 6):", np.abs(gram-np.eye(6)).max())

def cap_mask(centers):
    """indicator of union of caps: centers = list of unit vectors"""
    st = np.sqrt(np.maximum(0, 1-x_gl**2))
    px = st[:,None]*np.cos(phi)[None,:]
    py = st[:,None]*np.sin(phi)[None,:]
    pz = x_gl[:,None]*np.ones(NP)[None,:]
    m = np.zeros((NT,NP), bool)
    for c in centers:
        m |= (px*c[0]+py*c[1]+pz*c[2]) >= COS_W
    return m.astype(float)

def codes(z):
    if z==0: return []
    if z==1: return [np.array([0,0,1.0])]
    if z==2: return [np.array([0,0,1.0]), np.array([0,0,-1.0])]
    if z==3:
        return [np.array([np.cos(a), np.sin(a), 0.0]) for a in (0, 2*pi/3, 4*pi/3)]
    if z==4:
        return [np.array(v)/np.linalg.norm(v) for v in
                [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]]
    if z==5:  # trigonal bipyramid
        return [np.array([0,0,1.0]), np.array([0,0,-1.0])] + \
               [np.array([np.cos(a), np.sin(a), 0.0]) for a in (0, 2*pi/3, 4*pi/3)]
    raise ValueError

L = np.diag([l*(l+1) for (l,m,k) in basis]).astype(float)
free_sqrt = np.sqrt(np.sort(np.diag(L)))

def spectrum(z, mu):
    mask = cap_mask(codes(z))
    G = np.einsum('itp,jtp,tp->ij', Y, Y*mask[None,:,:], Wq)
    G = 0.5*(G+G.T)
    H = L + mu*G
    ev = np.linalg.eigvalsh(H)
    return np.sort(ev), mask.__mul__(Wq).sum()/(4*pi)

print("\ncap fraction & lowest constrained eigenvalues:")
res = {}
for z in (1,2,3,4,5):
    ev4, frac = spectrum(z, MU[0])
    ev5, _    = spectrum(z, MU[1])
    res[z] = (ev4, ev5, frac)
    print(" z=%d union=%.3f  lam(mu1e4)=%s  lam(mu1e5)=%s" %
          (z, frac, np.round(ev4[:5],3), np.round(ev5[:5],3)))

def S(z, M, mu_idx):
    ev = res[z][mu_idx]
    return np.sum(np.sqrt(np.maximum(ev[:M],0))) - np.sum(free_sqrt[:M])

for M in (4, 9):
    for mu_idx, mu in enumerate(MU):
        Sv = {z: S(z, M, mu_idx) for z in (1,2,3,4,5)}
        d12 = Sv[2]-Sv[1]; d23 = Sv[3]-Sv[2]; d34 = Sv[4]-Sv[3]; d35 = (Sv[5]-Sv[3])/2
        r1 = d12/d23 if d23 else float('inf'); r2 = d35/d23 if d23 else float('inf')
        print("\nM=%d mu=%.0e  S: %s" % (M, mu, {z: round(Sv[z],3) for z in Sv}))
        print("  increments: d12=%.3f d23=%.3f d34=%.3f d35/step=%.3f" % (d12,d23,d34,d35))
        print("  S9a (d12<d23): %s | S9b r1=%.3f in [0.15,0.55]: %s | S9c r2=%.3f in [0.7,1.3]: %s"
              % (d12<d23, r1, 0.15<=r1<=0.55, r2, 0.7<=r2<=1.3))

# implied scale (M=4, mu=1e4): w = eps * d23  ->  eps = 2.55/d23 (report only)
Sv = {z: S(z, 4, 0) for z in (1,2,3,5)}
d23 = Sv[3]-Sv[2]
if d23 > 0:
    print("\nimplied eps = 2.55/d23 = %.2f MeV per sqrt-eigen unit; surface rotational class hbar^2/(m r_q^2) = %.1f MeV"
          % (2.55/d23, 41.47/0.86**2))
