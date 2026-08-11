#!/usr/bin/env python3
# Swing 13 — corrected census: sticky T->0 anneal + capacity-capped mutual lock
# graph. Registration: ledger 880e176 (pre-run). Composed formula unchanged.
import numpy as np, math, time

rng = np.random.default_rng(1113)
N = 512; RHO = 0.138
L = (N/RHO)**(1/3.0)
CORE = 1.72; REACH = 2.14; CAP = 5
STEP = 0.20

g = L/8.0
pos = np.array([[i,j,k] for i in range(8) for j in range(8) for k in range(8)], float)*g
pos += rng.uniform(-0.08, 0.08, pos.shape); pos %= L

def min_image(d): return d - L*np.round(d/L)
core2, reach2 = CORE*CORE, REACH*REACH

def local_bonds(p, idx, arr):
    d = min_image(arr - p); d2 = np.einsum('ij,ij->i', d, d); d2[idx] = 1e9
    return d2

def anneal(pos, sweeps, T0, T1):
    t0 = time.time()
    for s in range(sweeps):
        T = T0*(T1/T0)**(s/max(1,sweeps-1))
        order = rng.permutation(N)
        trials = rng.uniform(-STEP, STEP, (N,3))
        for k in range(N):
            i = order[k]
            d2o = local_bonds(pos[i], i, pos)
            if d2o.min() < core2: pass
            Eo = -np.count_nonzero(d2o <= reach2)
            new = (pos[i] + trials[k]) % L
            d2n = local_bonds(new, i, pos)
            if d2n.min() < core2: continue
            En = -np.count_nonzero(d2n <= reach2)
            if En <= Eo or rng.random() < math.exp(-(En-Eo)/T):
                pos[i] = new
        if s % 500 == 0:
            d = min_image(pos[:,None,:]-pos[None,:,:])
            d2 = np.einsum('ijk,ijk->ij', d, d); np.fill_diagonal(d2, 1e9)
            zb = (d2 <= reach2).sum()/N
            print("  sweep %d T=%.3f z_dist=%.2f (%.0fs)" % (s, T, zb, time.time()-t0), flush=True)
    return pos

pos = anneal(pos, 3000, 1.0, 0.05)

def census(pos):
    d = min_image(pos[:,None,:]-pos[None,:,:])
    d2 = np.einsum('ijk,ijk->ij', d, d); np.fill_diagonal(d2, 1e9)
    inreach = d2 <= reach2
    # capacity cap: each node keeps CAP nearest in reach; edge kept iff mutual
    keep = np.zeros((N,N), bool)
    for i in range(N):
        cand = np.flatnonzero(inreach[i])
        if len(cand) > CAP:
            cand = cand[np.argsort(d2[i][cand])[:CAP]]
        keep[i, cand] = True
    A = keep & keep.T
    deg = A.sum(1)
    nbrs = [np.flatnonzero(A[i]) for i in range(N)]
    bonds = [(i,j) for i in range(N) for j in nbrs[i] if j > i]
    P2s, P3s = [], []
    for (i,j) in bonds:
        Ni, Nj = set(nbrs[i]), set(nbrs[j])
        P2s.append(len((Ni & Nj) - {i,j}))
        c3 = 0
        for x in Nj - {i}:
            for y in (set(nbrs[x]) & Ni) - {i,j}:
                if x != y: c3 += 1
        P3s.append(c3)
    return deg.mean(), float(np.mean(P2s)), float(np.mean(P3s)), len(bonds)

Zs, P2s_, P3s_ = [], [], []
for snap in range(4):
    pos = anneal(pos, 150, 0.05, 0.05)
    z, p2, p3, nb = census(pos)
    Zs.append(z); P2s_.append(p2); P3s_.append(p3)
    print("snap %d: z_lock=%.3f  P2=%.3f  P3=%.3f  bonds=%d" % (snap, z, p2, p3, nb), flush=True)

z, p2, p3 = np.mean(Zs), np.mean(P2s_), np.mean(P3s_)
print("\nMEANS: z_lock=%.3f  P2=%.3f  P3=%.3f" % (z, p2, p3))
print("S13a gate z in [4.3,5.0]:", "PASS" if 4.3 <= z <= 5.0 else "VOID")
HB2M = 41.47
for rq in (0.84, 0.86, 0.88):
    dp = HB2M/(4*rq*rq)
    c3 = HB2M*0.75/(18*rq*rq); c4 = HB2M*0.5/(32*rq*rq)
    dA = dp + 0.84 + c3*max(0.0, p2-1) + c4*p3
    print("r_q=%.2f: composed delta_bulk (Rule A) = %.2f" % (rq, dA))
rq = 0.86
dp = HB2M/(4*rq*rq); c3 = HB2M*0.75/(18*rq*rq); c4 = HB2M*0.5/(32*rq*rq)
dA = dp + 0.84 + c3*max(0.0, p2-1) + c4*p3
print("\nS13c THE LANDING: composed = %.2f in [20.0, 24.9]:" % dA,
      "PASS — CROWN tier (ii)" if 20.0 <= dA <= 24.9 else ("FAIL high" if dA > 24.9 else "FAIL low — bulk sector rejected"))
