#!/usr/bin/env python3
# Swing 10 — crown, finite-stiffness refinement. Registration: ledger e9dfdf5 (pre-run).
# delta(z) = (eps/2) * sum_{i<=M} [sqrt(lam_i(z,k)) - sqrt(lam_i(free))]
# eps = hbar^2/(m r_q^2) declared; k calibrated from delta(1) = 14.31 ONLY.
import numpy as np
from math import factorial, pi, sqrt

ZC = 4.78; COS_W = 1.0 - 2.0/ZC
LMAX = 15
EPS_C = 41.47/0.86**2                    # 56.08 MeV central
EPS_BAND = (41.47/0.88**2, 41.47/0.84**2)  # (53.55, 58.77)
D1 = 14.31                                # pair calibration datum

NT, NP = 96, 192
x_gl, w_gl = np.polynomial.legendre.leggauss(NT)
phi = 2*np.pi*np.arange(NP)/NP
wphi = 2*np.pi/NP

def plm_all(lmax, x):
    P = {(0,0): np.ones_like(x)}
    for m in range(1, lmax+1):
        P[(m,m)] = -(2*m-1)*np.sqrt(np.maximum(0,1-x*x))*P[(m-1,m-1)]
    for m in range(0, lmax):
        P[(m+1,m)] = (2*m+1)*x*P[(m,m)]
    for m in range(0, lmax+1):
        for l in range(m+2, lmax+1):
            P[(l,m)] = ((2*l-1)*x*P[(l-1,m)] - (l+m-1)*P[(l-2,m)])/(l-m)
    return P

P = plm_all(LMAX, x_gl)
basis = []
for l in range(LMAX+1):
    for m in range(0, l+1):
        if m == 0: basis.append((l,0,0))
        else: basis.append((l,m,0)); basis.append((l,m,1))
N = len(basis)
Y = np.zeros((N, NT, NP))
for i,(l,m,kind) in enumerate(basis):
    nrm = sqrt((2*l+1)/(4*pi)*factorial(l-m)/factorial(l+m))
    if m == 0: Y[i] = (nrm*P[(l,0)])[:,None]*np.ones(NP)[None,:]
    else:
        nrm *= sqrt(2.0)
        az = np.cos(m*phi) if kind==0 else np.sin(m*phi)
        Y[i] = (nrm*P[(l,m)])[:,None]*az[None,:]
Wq = w_gl[:,None]*wphi
L = np.diag([l*(l+1) for (l,m,k) in basis]).astype(float)
free_sqrt = np.sqrt(np.sort(np.diag(L)))

def codes(z):
    if z==1: return [np.array([0,0,1.0])]
    if z==2: return [np.array([0,0,1.0]), np.array([0,0,-1.0])]
    if z==3: return [np.array([np.cos(a),np.sin(a),0.0]) for a in (0,2*pi/3,4*pi/3)]
    if z==4: return [np.array(v)/np.linalg.norm(v) for v in [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]]
    if z==5: return [np.array([0,0,1.0]),np.array([0,0,-1.0])]+[np.array([np.cos(a),np.sin(a),0.0]) for a in (0,2*pi/3,4*pi/3)]
    raise ValueError

def gram(z):
    st = np.sqrt(np.maximum(0,1-x_gl**2))
    px = st[:,None]*np.cos(phi)[None,:]; py = st[:,None]*np.sin(phi)[None,:]
    pz = x_gl[:,None]*np.ones(NP)[None,:]
    m = np.zeros((NT,NP), bool)
    for c in codes(z): m |= (px*c[0]+py*c[1]+pz*c[2]) >= COS_W
    G = np.einsum('itp,jtp,tp->ij', Y, Y*m.astype(float)[None,:,:], Wq)
    return 0.5*(G+G.T)

G = {z: gram(z) for z in (1,2,3,4,5)}

def delta(z, k, M, eps):
    ev = np.sort(np.linalg.eigvalsh(L + k*G[z]))
    return (eps/2.0)*(np.sum(np.sqrt(np.maximum(ev[:M],0))) - np.sum(free_sqrt[:M]))

def calibrate(M, eps):
    lo, hi = 1e-4, 5e3
    for _ in range(200):
        mid = sqrt(lo*hi)
        if delta(1, mid, M, eps) < D1: lo = mid
        else: hi = mid
    return sqrt(lo*hi)

for M in (4, 9):
    for eps in (EPS_C,) + EPS_BAND:
        k = calibrate(M, eps)
        d = {z: delta(z, k, M, eps) for z in (1,2,3,4,5)}
        d23 = d[3]-d[2]; d35 = (d[5]-d[3])/2
        shape = (0.5 <= (d35/d23 if d23 else 99) <= 2.0)
        print("M=%d eps=%.2f  k=%.3f  delta: 1:%.2f 2:%.2f 3:%.2f 4:%.2f 5:%.2f" %
              (M, eps, k, d[1], d[2], d[3], d[4], d[5]))
        print("   S10a d(2)=%.2f in [13.9,16.5]: %s | S10b d(3)=%.2f in [16.6,18.4]: %s | "
              "S10c d(5)=%.2f in [20.0,24.9]: %s | S10d d35/d23=%.2f in [0.5,2]: %s" %
              (d[2], 13.9<=d[2]<=16.5, d[3], 16.6<=d[3]<=18.4,
               d[5], 20.0<=d[5]<=24.9, (d35/d23 if d23 else 99), shape))
