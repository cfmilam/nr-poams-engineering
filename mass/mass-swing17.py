#!/usr/bin/env python3
# Swing 17 — the derived capacity-graph transcription. Registration: 827a193 (pre-run).
# Lock graph = maximum-cardinality degree-<=5 subgraph of the availability graph
# (distance-greedy + length-3 alternating augmentation; exact bound reported).
# Ensembles rebuilt deterministically: swing-16 functional (seed 160811),
# swing-12 equilibrium liquid (seed 20260811). Rule C census; books scoring.
import numpy as np, math, time

RHO = 0.138; CORE = 1.72; REACH = 2.14; ZC = 4.78; HB2M = 41.47
DP = 14.02; TAUB = 20.1; H = 0.84; BOOKS = 35.85; WIN = (32.0, 40.0)
CAP = 5
D0 = RHO ** (-1.0/3.0)

# ---------------- shared machinery ----------------
def rulec_census(A, N):
    nbrs = [np.flatnonzero(A[i]) for i in range(N)]
    edges = [(i, int(j)) for i in range(N) for j in nbrs[i] if j > i]
    E = len(edges); eidx = {e: k for k, e in enumerate(edges)}
    z = float(A.sum(1).mean())
    seen = np.zeros(N, bool); ncomp = 0
    for s0 in range(N):
        if seen[s0]: continue
        ncomp += 1; st = [s0]; seen[s0] = True
        while st:
            u = st.pop()
            for v in nbrs[u]:
                if not seen[v]: seen[v] = True; st.append(int(v))
    beta1 = E - N + ncomp
    disc = [-1]*N; low = [0]*N; nbr_cnt = 0; timer = [0]
    for s0 in range(N):
        if disc[s0] != -1: continue
        st = [(s0, -1, iter(nbrs[s0]))]; disc[s0] = low[s0] = timer[0]; timer[0] += 1
        while st:
            u, pe, it = st[-1]
            adv = False
            for v in it:
                v = int(v)
                if v == pe: pe = -2; continue
                if disc[v] == -1:
                    disc[v] = low[v] = timer[0]; timer[0] += 1
                    st.append((v, u, iter(nbrs[v]))); adv = True; break
                else: low[u] = min(low[u], disc[v])
            if not adv:
                st.pop()
                if st:
                    p = st[-1][0]; low[p] = min(low[p], low[u])
                    if low[u] > disc[p]: nbr_cnt += 1
    f = 1.0 - nbr_cnt/E if E else 0.0
    tri = []
    for i in range(N):
        ni = [v for v in nbrs[i] if v > i]
        for a in range(len(ni)):
            for b in range(a+1, len(ni)):
                j, kk = int(ni[a]), int(ni[b])
                if A[j, kk]:
                    tri.append((1 << eidx[(i, j)]) | (1 << eidx[(i, kk)])
                               | (1 << eidx[(min(j, kk), max(j, kk))]))
    quads = set()
    for (i, j) in edges:
        Ni = set(int(v) for v in nbrs[i]); Nj = set(int(v) for v in nbrs[j])
        for x in Nj - {i}:
            for y in (set(int(v) for v in nbrs[x]) & Ni) - {i, j}:
                if x == y or A[i, x] or A[j, y]: continue
                m = (1 << eidx[(i, j)]) | (1 << eidx[(min(j, x), max(j, x))]) \
                    | (1 << eidx[(min(x, y), max(x, y))]) | (1 << eidx[(min(y, i), max(y, i))])
                quads.add(m)
    piv = {}
    def add(v):
        while v:
            b = v.bit_length() - 1
            if b in piv: v ^= piv[b]
            else: piv[b] = v; return 1
        return 0
    T_ = sum(add(v) for v in tri)
    Q_ = sum(add(v) for v in quads)
    return dict(z=z, E=E, ncomp=ncomp, beta1=beta1, T=T_, Q=Q_, R=beta1-T_-Q_, f=f)

def lock_graph(pos, L, N):
    """availability graph at REACH; lock graph = max-cardinality deg<=CAP subgraph.
    distance-greedy seed + length-3 alternating augmentation to local optimality;
    exact upper bound sum(min(deg,CAP))/2 reported."""
    d = pos[:, None, :] - pos[None, :, :]
    d -= L * np.round(d / L)
    d2 = np.einsum('ijk,ijk->ij', d, d)
    np.fill_diagonal(d2, 1e9)
    avail = d2 <= REACH*REACH
    deg_av = avail.sum(1)
    ub = int(np.minimum(deg_av, CAP).sum()) // 2
    # edge list sorted by distance (greedy: lock nearest first)
    ii, jj = np.nonzero(np.triu(avail, 1))
    order = np.argsort(d2[ii, jj])
    ii, jj = ii[order], jj[order]
    adj_av = [set(int(v) for v in np.flatnonzero(avail[i])) for i in range(N)]
    locked = [set() for _ in range(N)]
    for a, b in zip(ii, jj):
        a, b = int(a), int(b)
        if len(locked[a]) < CAP and len(locked[b]) < CAP:
            locked[a].add(b); locked[b].add(a)
    # augmentation passes: add free-free edges; length-3 swap to gain one
    improved = True; passes = 0
    while improved and passes < 40:
        improved = False; passes += 1
        for u in range(N):
            if len(locked[u]) >= CAP: continue
            # direct add
            for v in adj_av[u]:
                if v in locked[u]: continue
                if len(locked[u]) >= CAP: break
                if len(locked[v]) < CAP:
                    locked[u].add(v); locked[v].add(u); improved = True
            if len(locked[u]) >= CAP: continue
            # length-3: u -(new)- v -(drop)- w -(new)- x
            done = False
            for v in adj_av[u]:
                if v in locked[u] or len(locked[v]) < CAP: continue
                for w in list(locked[v]):
                    if w == u: continue
                    for x in adj_av[w]:
                        if x in locked[w] or x == v or x == u: continue
                        if len(locked[x]) < CAP:
                            locked[v].discard(w); locked[w].discard(v)
                            locked[u].add(v); locked[v].add(u)
                            locked[w].add(x); locked[x].add(w)
                            improved = True; done = True; break
                    if done: break
                if done: break
    A = np.zeros((N, N), bool)
    for i in range(N):
        for j in locked[i]:
            A[i, j] = True
    nlock = int(A.sum()) // 2
    return A, ub, nlock, float(np.mean(np.minimum(deg_av, CAP)))

def score_ensemble(name, snaps):
    zbar = float(np.mean([c['z'] for c in snaps]))
    Em = float(np.mean([c['E'] for c in snaps]))
    Tm = float(np.mean([c['T'] for c in snaps])); Qm = float(np.mean([c['Q'] for c in snaps]))
    Rm = float(np.mean([c['R'] for c in snaps])); fm = float(np.mean([c['f'] for c in snaps]))
    b1E = float(np.mean([c['beta1']/c['E'] for c in snaps]))
    print("\n== %s MEANS: z_lock=%.3f E=%.0f T=%.1f Q=%.1f R=%.1f f=%.3f beta1/E=%.3f"
          % (name, zbar, Em, Tm, Qm, Rm, fm, b1E))
    res = {}
    for rq in (0.84, 0.86, 0.88):
        dp = HB2M/(4*rq*rq); c3 = HB2M*0.75/(18*rq*rq); c4 = HB2M*0.5/(32*rq*rq)
        cred = (c3*Tm + c4*Qm)/Em
        g0 = dp + cred; g1 = dp + cred + H*fm
        pref = min(zbar, ZC)/2.0
        res[rq] = (pref*g0, pref*g1, g0, g1)
        print("  r_q=%.2f: gross_h0=%.2f gross_h1=%.2f | G_h0=%.2f G_h1=%.2f"
              % (rq, g0, g1, pref*g0, pref*g1))
    return zbar, res

# ---------------- ensemble A: swing-16 functional (verbatim rebuild, seed 160811) ----------------
print("ENSEMBLE A: swing-16 functional anneal (seed 160811)")
N = 256; L = (N/RHO) ** (1/3.0)
SWEEPS = 3000; STEP = 0.22
rng = np.random.default_rng(160811)
grid = np.array([[i, j, k] for i in range(7) for j in range(7) for k in range(7)], float) * (L/7)
sel = rng.permutation(343)[:N]
pos = grid[sel] + rng.uniform(-0.01, 0.01, (N, 3))
pos %= L

def full_d2(pos, L):
    d = pos[:, None, :] - pos[None, :, :]
    d -= L * np.round(d / L)
    d2 = np.einsum('ijk,ijk->ij', d, d)
    np.fill_diagonal(d2, 1e9)
    return d2

D2 = full_d2(pos, L)
core2, reach2 = CORE*CORE, REACH*REACH

def node_E_from_row(row):
    idx = np.argpartition(row, CAP)[:CAP]
    d = np.sqrt(row[idx])
    dbar = d.mean()
    Lk = int(np.count_nonzero((d >= CORE) & (d <= REACH)))
    return -(DP/2.0)*Lk + TAUB*(D0/dbar)**2, d.max()

Ecache = np.zeros(N); R5 = np.zeros(N)
def rebuild():
    for j in range(N):
        Ecache[j], R5[j] = node_E_from_row(D2[j])
rebuild()

def row_to(p, i, pos, L):
    d = pos - p
    d -= L * np.round(d / L)
    r = np.einsum('ij,ij->i', d, d)
    r[i] = 1e9
    return r

t0 = time.time()
for s in range(SWEEPS):
    T = 8.0 * (0.05/8.0) ** (s / (SWEEPS - 1))
    order = rng.permutation(N)
    trials = rng.uniform(-STEP, STEP, (N, 3))
    us = rng.random(N)
    for k in range(N):
        i = order[k]
        newp = (pos[i] + trials[k]) % L
        rnew = row_to(newp, i, pos, L)
        if rnew.min() < core2: continue
        rold = D2[i]
        r5sq = R5 * R5 + 1e-9
        J = np.flatnonzero((rold <= r5sq) | (rnew <= r5sq))
        Eold = Ecache[i] + Ecache[J].sum()
        Ei_new, r5i = node_E_from_row(rnew)
        Enew = Ei_new
        newE_J = []; newR_J = []
        for j in J:
            rowj = D2[j].copy(); rowj[i] = rnew[j]
            ej, rj = node_E_from_row(rowj)
            newE_J.append(ej); newR_J.append(rj); Enew += ej
        dE = Enew - Eold
        if dE <= 0 or (T > 1e-9 and math.exp(-dE/T) > (us[k] if k < N else rng.random())):
            pos[i] = newp
            D2[i, :] = rnew; D2[:, i] = rnew
            Ecache[i] = Ei_new; R5[i] = math.sqrt(r5i) if r5i < 1e8 else R5[i]
            R5[i] = math.sqrt(node_E_from_row(rnew)[1])
            for m, j in enumerate(J):
                Ecache[j] = newE_J[m]; R5[j] = math.sqrt(newR_J[m])
    if s % 100 == 0:
        rebuild()
print("  anneal done (%.0fs) E/N=%.3f" % (time.time()-t0, Ecache.mean()), flush=True)

snapsA = []
for snap in range(3):
    if snap:
        for s in range(100):
            order = rng.permutation(N); trials = rng.uniform(-STEP, STEP, (N, 3))
            for k in range(N):
                i = order[k]
                newp = (pos[i] + trials[k]) % L
                rnew = row_to(newp, i, pos, L)
                if rnew.min() < core2: continue
                r5sq = R5*R5 + 1e-9
                J = np.flatnonzero((D2[i] <= r5sq) | (rnew <= r5sq))
                Eold = Ecache[i] + Ecache[J].sum()
                Ei_new, _ = node_E_from_row(rnew); Enew = Ei_new
                newE_J = []; newR_J = []
                for j in J:
                    rowj = D2[j].copy(); rowj[i] = rnew[j]
                    ej, rj = node_E_from_row(rowj); newE_J.append(ej); newR_J.append(rj); Enew += ej
                if Enew - Eold <= 0 or math.exp(-(Enew-Eold)/0.05) > rng.random():
                    pos[i] = newp; D2[i, :] = rnew; D2[:, i] = rnew
                    Ecache[i] = Ei_new
                    R5[i] = math.sqrt(node_E_from_row(rnew)[1])
                    for m, j in enumerate(J):
                        Ecache[j] = newE_J[m]; R5[j] = math.sqrt(newR_J[m])
        rebuild()
    A, ub, nlock, zub = lock_graph(pos, L, N)
    c = rulec_census(A, N)
    print("  snap %d: locks=%d (bound %d, gap %d)  z_lock=%.3f  z_ub=%.3f  T=%d Q=%d R=%d"
          % (snap, nlock, ub, ub-nlock, c['z'], zub, c['T'], c['Q'], c['R']), flush=True)
    snapsA.append(c)

zA, resA = score_ensemble("FUNCTIONAL (swing-16 rebuild)", snapsA)

# ---------------- ensemble B: swing-12 equilibrium liquid (verbatim rebuild, seed 20260811) ----------------
print("\nENSEMBLE B: swing-12 equilibrium liquid (seed 20260811)")
N = 512; L = (N/RHO) ** (1/3.0)
rng = np.random.default_rng(20260811)
g = L/8.0
pos = np.array([[i, j, k] for i in range(8) for j in range(8) for k in range(8)], float)*g
pos += rng.uniform(-0.08, 0.08, pos.shape); pos %= L

def min_image(d, L): return d - L*np.round(d/L)
def mc_sweep(pos, L, N):
    order = rng.permutation(N); trials = rng.uniform(-STEP, STEP, (N, 3))
    for idx in range(N):
        i = order[idx]
        new = (pos[i] + trials[idx]) % L
        d = min_image(pos - new, L); d2 = np.einsum('ij,ij->i', d, d); d2[i] = 1e9
        if d2.min() >= core2: pos[i] = new

t0 = time.time()
for s in range(1500):
    mc_sweep(pos, L, N)
    if s % 500 == 0: print("  eq sweep %d (%.0fs)" % (s, time.time()-t0), flush=True)

snapsB = []
for snap in range(3):
    for s in range(60): mc_sweep(pos, L, N)
    A, ub, nlock, zub = lock_graph(pos, L, N)
    c = rulec_census(A, N)
    print("  snap %d: locks=%d (bound %d, gap %d)  z_lock=%.3f  z_ub=%.3f  T=%d Q=%d R=%d"
          % (snap, nlock, ub, ub-nlock, c['z'], zub, c['T'], c['Q'], c['R']), flush=True)
    snapsB.append(c)

zB, resB = score_ensemble("LIQUID (swing-12 rebuild)", snapsB)

# ---------------- gates ----------------
print("\n---- GATES ----")
okA, okB = 4.3 <= zA <= 5.3, 4.3 <= zB <= 5.3
print("S17a REALIZATION: functional z=%.3f %s | liquid z=%.3f %s | gate:" %
      (zA, "in" if okA else "OUT", zB, "in" if okB else "OUT"),
      "PASS" if okA and okB else "FAIL")
gA0, gA1 = resA[0.86][2], resA[0.86][3]
gB0, gB1 = resB[0.86][2], resB[0.86][3]
okg = all(13.98 <= g <= 16.19 for g in (gA0, gA1, gB0, gB1))
print("S17b GROSS (central): functional %.2f/%.2f  liquid %.2f/%.2f  in [13.98,16.19]:" %
      (gA0, gA1, gB0, gB1), "PASS" if okg else "FAIL")
allG = [v for res in (resA, resB) for pair in res.values() for v in pair[:2]]
okG = all(WIN[0] <= v <= WIN[1] for v in allG)
GA0, GA1 = resA[0.86][0], resA[0.86][1]
GB0, GB1 = resB[0.86][0], resB[0.86][1]
print("S17c THE LANDING: all G in [32,40]:", "PASS — CROWN BOOKS CLOSE" if okG else "FAIL")
print("  functional central: G_h0=%.2f (%+.1f%%)  G_h1=%.2f (%+.1f%%)"
      % (GA0, 100*(GA0-BOOKS)/BOOKS, GA1, 100*(GA1-BOOKS)/BOOKS))
print("  liquid central:     G_h0=%.2f (%+.1f%%)  G_h1=%.2f (%+.1f%%)"
      % (GB0, 100*(GB0-BOOKS)/BOOKS, GB1, 100*(GB1-BOOKS)/BOOKS))
print("S17d composition + matching-bound gaps reported above.")
