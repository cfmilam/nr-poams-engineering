#!/usr/bin/env python3
# Swing 15 — Rule C: independent-closure counting (cycle-space basis, shortest-
# first) + books-level landing. Registration: ledger 0c7be63 (pre-run).
# Candidates: sc, bcc references at rho0; PHYSICAL = capacity-capped equilibrium
# liquid (swing-12 construction, seed 20260811 + swing-13 mutual CAP=5 rule).
import numpy as np, math, time

RHO = 0.138; CORE = 1.72; REACH = 2.14; ZC = 4.78; HB2M = 41.47
H = 0.84; BOOKS = 35.85; WIN = (32.0, 40.0)

# ---------- graph census under Rule C ----------
def rulec_census(A):
    """A: boolean adjacency (numpy). Returns dict with z, E, ncomp, beta1,
    T (triangle rank), Q (quad rank beyond triangles), R (residue),
    f (non-bridge edge fraction), plus raw counts."""
    N = A.shape[0]
    nbrs = [np.flatnonzero(A[i]) for i in range(N)]
    edges = [(i, int(j)) for i in range(N) for j in nbrs[i] if j > i]
    E = len(edges)
    eidx = {e: k for k, e in enumerate(edges)}
    deg = A.sum(1)
    z = float(deg.mean())
    # components
    seen = np.zeros(N, bool); ncomp = 0
    for s in range(N):
        if seen[s]: continue
        ncomp += 1; stack = [s]; seen[s] = True
        while stack:
            u = stack.pop()
            for v in nbrs[u]:
                if not seen[v]: seen[v] = True; stack.append(int(v))
    beta1 = E - N + ncomp
    # bridges (iterative Tarjan)
    disc = [-1]*N; low = [0]*N; nbridge = 0; timer = [0]
    for s in range(N):
        if disc[s] != -1: continue
        stack = [(s, -1, iter(nbrs[s]))]
        disc[s] = low[s] = timer[0]; timer[0] += 1
        while stack:
            u, pe, it = stack[-1]
            adv = False
            for v in it:
                v = int(v)
                if v == pe: pe = -2; continue   # skip parent edge once (simple graph)
                if disc[v] == -1:
                    disc[v] = low[v] = timer[0]; timer[0] += 1
                    stack.append((v, u, iter(nbrs[v]))); adv = True; break
                else:
                    low[u] = min(low[u], disc[v])
            if not adv:
                stack.pop()
                if stack:
                    p = stack[-1][0]
                    low[p] = min(low[p], low[u])
                    if low[u] > disc[p]: nbridge += 1
    f = 1.0 - nbridge/E if E else 0.0
    # triangles as edge-bitmask vectors
    tri = []
    for i in range(N):
        ni = [v for v in nbrs[i] if v > i]
        for a in range(len(ni)):
            for b in range(a+1, len(ni)):
                j, k = int(ni[a]), int(ni[b])
                if A[j, k]:
                    tri.append((1 << eidx[(i, j)]) | (1 << eidx[(i, k)])
                               | (1 << eidx[(min(j, k), max(j, k))]))
    # chordless quads i-j-x-y (dedupe by bitmask)
    quads = set()
    for (i, j) in edges:
        Ni = set(int(v) for v in nbrs[i]); Nj = set(int(v) for v in nbrs[j])
        for x in Nj - {i}:
            for y in (set(int(v) for v in nbrs[x]) & Ni) - {i, j}:
                if x == y: continue
                if A[i, x] or A[j, y]: continue   # chordless only
                m = (1 << eidx[(i, j)]) | (1 << eidx[(min(j, x), max(j, x))]) \
                    | (1 << eidx[(min(x, y), max(x, y))]) | (1 << eidx[(min(y, i), max(y, i))])
                quads.add(m)
    quads = list(quads)
    # GF(2) ranks, triangles first (shortest-first basis)
    piv = {}
    def add(v):
        while v:
            b = v.bit_length() - 1
            if b in piv: v ^= piv[b]
            else: piv[b] = v; return 1
        return 0
    T = sum(add(v) for v in tri)
    Q = sum(add(v) for v in quads)
    R = beta1 - T - Q
    return dict(z=z, E=E, ncomp=ncomp, beta1=beta1, T=T, Q=Q, R=R, f=f,
                ntri=len(tri), nquad=len(quads))

# ---------- scoring ----------
def score(name, c, zc=ZC, band=True):
    print("\n== %s: z=%.3f E=%d comp=%d beta1=%d (b1/E=%.3f) T=%d Q=%d R=%d f=%.3f (raw tri=%d quad=%d)"
          % (name, c['z'], c['E'], c['ncomp'], c['beta1'], c['beta1']/c['E'],
             c['T'], c['Q'], c['R'], c['f'], c['ntri'], c['nquad']))
    out = {}
    for rq in (0.84, 0.86, 0.88):
        dp = HB2M/(4*rq*rq); c3 = HB2M*0.75/(18*rq*rq); c4 = HB2M*0.5/(32*rq*rq)
        cred0 = (c3*c['T'] + c4*c['Q'])/c['E']
        credU = cred0 + c4*c['R']/c['E']
        pref = min(c['z'], zc)/2.0
        g0 = pref*(dp + cred0)             # h0 primary
        g1 = pref*(dp + cred0 + H*c['f'])  # h1 bracket
        gU = pref*(dp + credU + H*c['f'])  # upper bracket (R at c4)
        out[rq] = (g0, g1)
        print("  r_q=%.2f: cred0=%.3f credU=%.3f | G_h0=%.2f  G_h1=%.2f  (upper %.2f)"
              % (rq, cred0, credU, g0, g1, gU))
    if band:
        rq = 0.86; dp = HB2M/(4*rq*rq); c3 = HB2M*0.75/(18*rq*rq); c4 = HB2M*0.5/(32*rq*rq)
        cred0 = (c3*c['T'] + c4*c['Q'])/c['E']
        for zcb in (4.43, 4.78, 5.13):
            pref = min(c['z'], zcb)/2.0
            print("  z_c=%.2f: G_h0=%.2f G_h1=%.2f"
                  % (zcb, pref*(dp+cred0), pref*(dp+cred0+H*c['f'])))
    return out

# ---------- reference lattices at rho0 ----------
def lattice_adj(kind, reps):
    if kind == "sc": basis = [[0,0,0]]
    elif kind == "bcc": basis = [[0,0,0],[.5,.5,.5]]
    a = (len(basis)/RHO)**(1/3.0)
    pts = []
    for i in range(reps):
        for j in range(reps):
            for k in range(reps):
                for b in basis: pts.append((np.array([i,j,k], float)+b)*a)
    pts = np.array(pts); Lb = reps*a
    d = pts[:,None,:]-pts[None,:,:]; d -= Lb*np.round(d/Lb)
    d2 = np.einsum('ijk,ijk->ij', d, d); np.fill_diagonal(d2, 1e9)
    return d2 <= REACH*REACH

print("SWING 15 — Rule C census. Theorem check: per-bond depth ceiling = %.2f MeV"
      % (HB2M/(4*0.86*0.86) + H + HB2M*0.5/(32*0.86*0.86)))

res_sc  = rulec_census(lattice_adj("sc", 6))
score("sc (reference)", res_sc, band=False)
res_bcc = rulec_census(lattice_adj("bcc", 5))
score("bcc (reference)", res_bcc, band=False)

# ---------- PHYSICAL: capacity-capped equilibrium liquid ----------
rng = np.random.default_rng(20260811)
N = 512; L = (N/RHO)**(1/3.0); STEP = 0.22; CAP = 5
g = L/8.0
pos = np.array([[i,j,k] for i in range(8) for j in range(8) for k in range(8)], float)*g
pos += rng.uniform(-0.08, 0.08, pos.shape); pos %= L
def min_image(d): return d - L*np.round(d/L)
core2 = CORE*CORE
def mc_sweep(pos):
    order = rng.permutation(N); trials = rng.uniform(-STEP, STEP, (N,3))
    for idx in range(N):
        i = order[idx]
        new = (pos[i] + trials[idx]) % L
        d = min_image(pos - new); d2 = np.einsum('ij,ij->i', d, d); d2[i] = 1e9
        if d2.min() >= core2: pos[i] = new

t0 = time.time()
for s in range(1500):
    mc_sweep(pos)
    if s % 500 == 0: print("  eq sweep %d (%.0fs)" % (s, time.time()-t0), flush=True)

def capped_adj(pos):
    d = min_image(pos[:,None,:]-pos[None,:,:])
    d2 = np.einsum('ijk,ijk->ij', d, d); np.fill_diagonal(d2, 1e9)
    inreach = d2 <= REACH*REACH
    keep = np.zeros((N,N), bool)
    for i in range(N):
        cand = np.flatnonzero(inreach[i])
        if len(cand) > CAP: cand = cand[np.argsort(d2[i][cand])[:CAP]]
        keep[i, cand] = True
    return keep & keep.T, float(inreach.sum(1).mean())

snaps = []
for k in range(3):
    for s in range(60): mc_sweep(pos)
    A, zraw = capped_adj(pos)
    c = rulec_census(A)
    print("snap %d: z_raw(in-reach)=%.2f  z_capped=%.3f  (%.0fs)" % (k, zraw, c['z'], time.time()-t0), flush=True)
    snaps.append(c)

avg = dict(z=np.mean([c['z'] for c in snaps]), E=int(np.mean([c['E'] for c in snaps])),
           ncomp=int(np.mean([c['ncomp'] for c in snaps])), beta1=int(np.mean([c['beta1'] for c in snaps])),
           T=int(round(np.mean([c['T'] for c in snaps]))), Q=int(round(np.mean([c['Q'] for c in snaps]))),
           R=int(round(np.mean([c['R'] for c in snaps]))), f=float(np.mean([c['f'] for c in snaps])),
           ntri=int(np.mean([c['ntri'] for c in snaps])), nquad=int(np.mean([c['nquad'] for c in snaps])))
out = score("CAPPED EQUILIBRIUM LIQUID (physical)", avg)

# ---------- gates ----------
zp = avg['z']
print("\nS15b candidate gate: z_capped = %.3f in [4.3, 5.3]:" % zp,
      "PASS" if 4.3 <= zp <= 5.3 else "VOID")
allin = all(WIN[0] <= gv <= WIN[1] for pair in out.values() for gv in pair)
g0c, g1c = out[0.86]
print("S15c THE LANDING (books): G in [32,40] for BOTH h-variants x r_q band:",
      "PASS — CROWN BOOKS CLOSE (tier ii, books level)" if allin else "FAIL")
print("  central: G_h0 = %.2f (%.1f%% vs C=35.85)   G_h1 = %.2f (%+.1f%%)"
      % (g0c, 100*(g0c-BOOKS)/BOOKS, g1c, 100*(g1c-BOOKS)/BOOKS))
print("S15d references reported above (no gate).")
print("S15e gamma-channel reconciliation: deferred to swing 16 (report only).")
