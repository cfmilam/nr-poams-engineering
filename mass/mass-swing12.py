#!/usr/bin/env python3
# Swing 12 — THE LANDING. Registration: ledger 521f4ff (pre-run).
# Equilibrium hard-sphere liquid at rho0; contact graph at lock reach; per-bond
# loop census (P2 triangles, P3 four-cycle paths); composed shared-turn ledger.
import numpy as np, math, time

rng = np.random.default_rng(20260811)
N = 512
RHO = 0.138
L = (N/RHO)**(1/3.0)
CORE = 1.72          # 2 r_q
REACH = 2.14         # 2 r_q + xi
SWEEPS_EQ = 1500
SNAPSHOTS = 5
SNAP_EVERY = 60
STEP = 0.22

print("box L = %.3f fm  phi(hard) = %.3f" % (L, RHO*math.pi/6*CORE**3))

# init: 8x8x8 sc lattice, spacing L/8 = 1.935 > 1.72 (overlap-free), small jitter
g = L/8.0
pos = np.array([[i, j, k] for i in range(8) for j in range(8) for k in range(8)], float)*g
pos += rng.uniform(-0.08, 0.08, pos.shape)
pos %= L

def min_image(d):
    return d - L*np.round(d/L)

core2 = CORE*CORE
def mc_sweep(pos):
    acc = 0
    order = rng.permutation(N)
    trials = rng.uniform(-STEP, STEP, (N,3))
    for idx in range(N):
        i = order[idx]
        new = (pos[i] + trials[idx]) % L
        d = min_image(pos - new)
        d2 = np.einsum('ij,ij->i', d, d)
        d2[i] = 1e9
        if d2.min() >= core2:
            pos[i] = new
            acc += 1
    return acc/N

t0 = time.time()
for s in range(SWEEPS_EQ):
    a = mc_sweep(pos)
    if s % 300 == 0:
        print("  sweep %d acc %.2f  (%.0fs)" % (s, a, time.time()-t0), flush=True)

def census(pos):
    d = min_image(pos[:,None,:] - pos[None,:,:])
    d2 = np.einsum('ijk,ijk->ij', d, d)
    A = (d2 <= REACH*REACH)
    np.fill_diagonal(A, False)
    deg = A.sum(1)
    nbrs = [np.flatnonzero(A[i]) for i in range(N)]
    bonds = [(i, j) for i in range(N) for j in nbrs[i] if j > i]
    P2s, P3s = [], []
    for (i, j) in bonds:
        Ni, Nj = set(nbrs[i]), set(nbrs[j])
        common = (Ni & Nj) - {i, j}
        P2s.append(len(common))
        c3 = 0
        for x in Nj - {i}:
            # simple 3-paths j-x-y-i (x adj j, y adj x, y adj i; x,y distinct, x!=i, y!=j)
            for y in (set(nbrs[x]) & Ni) - {i, j}:
                if x != y:
                    c3 += 1
        P3s.append(c3)
    return deg.mean(), np.mean(P2s), np.mean(P3s), np.std(P2s), np.std(P3s), len(bonds)

Z, P2, P3, sP2, sP3, NB = [], [], [], [], [], []
for snap in range(SNAPSHOTS):
    for s in range(SNAP_EVERY):
        mc_sweep(pos)
    z, p2, p3, s2, s3, nb = census(pos)
    Z.append(z); P2.append(p2); P3.append(p3); sP2.append(s2); sP3.append(s3); NB.append(nb)
    print("snap %d: z=%.3f  P2=%.3f(%.2f)  P3=%.3f(%.2f)  bonds=%d  (%.0fs)"
          % (snap, z, p2, p3, s2, s3, nb, time.time()-t0), flush=True)

z, p2, p3 = np.mean(Z), np.mean(P2), np.mean(P3)
print("\nMEANS: z = %.3f   P2 = %.3f   P3 = %.3f" % (z, p2, p3))

# ---- scoring ----
print("\nS12a void gate: z in [4.3, 5.3]:", "PASS (graph = capacity graph)" if 4.3 <= z <= 5.3 else "VOID")
HB2M = 41.47
for rq in (0.84, 0.86, 0.88):
    dp = HB2M/(4*rq*rq)
    c3 = HB2M*(math.sin(math.pi/3)**2)/(2*9*rq*rq)
    c4 = HB2M*(math.sin(math.pi/4)**2)/(2*16*rq*rq)
    h = 0.84
    dA = dp + h + c3*max(0.0, p2-1) + c4*p3            # Rule A (primary)
    dB = dp + h + c3*max(0.0, p2-1) + c4*max(0.0, p3-1) # Rule B (sensitivity)
    print("r_q=%.2f: dp=%.2f c3=%.3f c4=%.3f | RuleA delta_bulk=%.2f | RuleB=%.2f"
          % (rq, dp, c3, c4, dA, dB))
rq = 0.86
dp = HB2M/(4*rq*rq); c3 = HB2M*0.75/(18*rq*rq); c4 = HB2M*0.5/(32*rq*rq)
dA = dp + 0.84 + c3*max(0.0, p2-1) + c4*p3
print("\nS12c THE LANDING (central): composed delta_bulk = %.2f  in [20.0, 24.9]:" % dA,
      "PASS — CROWN tier (ii)" if 20.0 <= dA <= 24.9 else ("FAIL high" if dA > 24.9 else "FAIL low"))
print("S12d alpha restatement: %.2f in [16.6,18.4]: %s" % (dp+0.84+c3, 16.6 <= dp+0.84+c3 <= 18.4))
# reach sensitivity note printed for the record (no re-scoring): census at 2.06/2.22 would shift z, P2, P3
