#!/usr/bin/env python3
# Pool campaign stage P-1 — exact bracket collapse. Registration: e466d14 (pre-run).
# Upper bound: double-cover max-flow (Dinic, integer); lower: greedy+restarts+augment.
import numpy as np, math, itertools, random

RHO = 0.138; CORE = 1.72; REACH = 2.14
DP = 14.02; TAUB = 20.1
D0 = RHO ** (-1.0/3.0)
SIZES = [20, 30, 40, 60, 90, 130, 180, 220]
SEEDS = [160812, 260812, 360812]
SWEEPS = 2200; STEP = 0.22; CAP = 5
core2, reach2 = CORE*CORE, REACH*REACH

# ---------------- Dinic max-flow (integer) ----------------
class Dinic:
    def __init__(self, n):
        self.n = n; self.g = [[] for _ in range(n)]
    def add(self, u, v, c):
        self.g[u].append([v, c, len(self.g[v])])
        self.g[v].append([u, 0, len(self.g[u]) - 1])
    def bfs(self, s, t):
        self.lev = [-1]*self.n; self.lev[s] = 0; q = [s]
        for u in q:
            for e in self.g[u]:
                if e[1] > 0 and self.lev[e[0]] < 0:
                    self.lev[e[0]] = self.lev[u] + 1; q.append(e[0])
        return self.lev[t] >= 0
    def dfs(self, u, t, f):
        if u == t: return f
        while self.it[u] < len(self.g[u]):
            e = self.g[u][self.it[u]]
            if e[1] > 0 and self.lev[e[0]] == self.lev[u] + 1:
                d = self.dfs(e[0], t, min(f, e[1]))
                if d > 0:
                    e[1] -= d; self.g[e[0]][e[2]][1] += d; return d
            self.it[u] += 1
        return 0
    def maxflow(self, s, t):
        fl = 0
        while self.bfs(s, t):
            self.it = [0]*self.n
            while True:
                f = self.dfs(s, t, 1 << 30)
                if f == 0: break
                fl += f
        return fl

def upper_bound_edges(A, edges):
    """floor(F/2) with F = max flow on bipartite double cover (fractional b-matching x2)."""
    # nodes: 0 = source, 1..A = left, A+1..2A = right, 2A+1 = sink
    dz = Dinic(2*A + 2)
    S, T = 0, 2*A + 1
    for v in range(A):
        dz.add(S, 1 + v, CAP)
        dz.add(1 + A + v, T, CAP)
    for (i, j) in edges:
        dz.add(1 + i, 1 + A + j, 1)
        dz.add(1 + j, 1 + A + i, 1)
    F = dz.maxflow(S, T)
    return F // 2

def augment_paths(A, edges, M, deg, max_depth=24):
    """Alternating-path augmentation for the degree-constrained subgraph (paths only,
    blossoms not implemented — as registered). M: set of (i,j) i<j. Returns #added."""
    nbr = [[] for _ in range(A)]
    for (i, j) in edges:
        nbr[i].append(j); nbr[j].append(i)
    def key(a, b): return (a, b) if a < b else (b, a)
    added = 0
    progress = True
    while progress:
        progress = False
        deficient = [v for v in range(A) if deg[v] < CAP]
        for u in deficient:
            if deg[u] >= CAP: continue
            # iterative DFS: state = (vertex, need_unmatched, path_edges tuple)
            stack = [(u, True, ())]
            seen = set()
            done = False
            while stack and not done:
                v, needU, path = stack.pop()
                if (v, needU) in seen and not path: continue
                seen.add((v, needU))
                if len(path) >= max_depth: continue
                for w in nbr[v]:
                    e = key(v, w)
                    if e in path: continue
                    inM = e in M
                    if needU and not inM:
                        # arriving at w via unmatched edge: accept if w deficient (and path odd)
                        if deg[w] < CAP and (w != u or path):
                            if w != u:
                                # flip: odd-position edges added, even removed
                                newpath = path + (e,)
                                for idx, pe in enumerate(newpath):
                                    if idx % 2 == 0:
                                        M.add(pe)
                                        deg[pe[0]] += 1; deg[pe[1]] += 1
                                    else:
                                        M.discard(pe)
                                        deg[pe[0]] -= 1; deg[pe[1]] -= 1
                                added += 1; progress = True; done = True
                                break
                        if (w, False) not in seen:
                            stack.append((w, False, path + (e,)))
                    elif (not needU) and inM:
                        if (w, True) not in seen:
                            stack.append((w, True, path + (e,)))
                if done: break
    return added

results = {}
import time
t0 = time.time()

def anneal(A, rng):
    R_drop = (3*A/(4*math.pi*RHO)) ** (1/3.0)
    pos = []
    tries = 0
    while len(pos) < A and tries < 200000:
        tries += 1
        p = (rng.random(3)*2 - 1) * R_drop
        if np.dot(p, p) > R_drop*R_drop: continue
        ok = True
        for q in pos:
            d = p - q
            if np.dot(d, d) < (0.95*D0)**2: ok = False; break
        if ok: pos.append(p)
    pos = np.array(pos)
    while len(pos) < A:
        p = (rng.random(3)*2 - 1) * R_drop
        if np.dot(p, p) <= R_drop*R_drop: pos = np.vstack([pos, p])
    A = len(pos)
    def node_E(row):
        k = min(CAP, A-1)
        idx = np.argpartition(row, k)[:k]
        d = np.sqrt(row[idx]); dbar = d.mean()
        Lk = int(np.count_nonzero((d >= CORE) & (d <= REACH)))
        return -(DP/2.0)*Lk + TAUB*(D0/dbar)**2
    dd = pos[:, None, :] - pos[None, :, :]
    D2 = np.einsum('ijk,ijk->ij', dd, dd); np.fill_diagonal(D2, 1e9)
    E = np.array([node_E(D2[i]) for i in range(A)])
    RW = R_drop + 0.3
    for s in range(SWEEPS):
        T = 6.0 * (0.04/6.0) ** (s / (SWEEPS-1))
        order = rng.permutation(A)
        trials = rng.uniform(-STEP, STEP, (A, 3))
        for k in range(A):
            i = order[k]
            newp = pos[i] + trials[k]
            if np.dot(newp, newp) > RW*RW: continue
            d1 = pos - newp
            rnew = np.einsum('ij,ij->i', d1, d1); rnew[i] = 1e9
            if rnew.min() < core2: continue
            aff = np.flatnonzero((D2[i] < (1.6*REACH)**2) | (rnew < (1.6*REACH)**2))
            Eold = E[i] + E[aff].sum()
            rowi_old = D2[i].copy()
            D2[i, :] = rnew; D2[:, i] = rnew
            Enew_i = node_E(D2[i])
            Enew = Enew_i + sum(node_E(D2[j]) for j in aff)
            if Enew - Eold <= 0 or (T > 1e-9 and math.exp(-(Enew-Eold)/T) > rng.random()):
                pos[i] = newp; E[i] = Enew_i
                for j in aff: E[j] = node_E(D2[j])
            else:
                D2[i, :] = rowi_old; D2[:, i] = rowi_old
    return pos, D2, A

# ---- P-1c solver validation on random small graphs (brute force) ----
print("P-1c solver validation (brute force vs flow sandwich, b=2 for tractability):")
ok_all = True
rngv = random.Random(7)
for trial in range(10):
    n = rngv.randint(6, 10)
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            if rngv.random() < 0.45: edges.append((i, j))
    CAPv = 2
    # brute force max size subset with deg <= 2
    best = 0
    for r in range(len(edges), -1, -1):
        if r <= best: break
        from itertools import combinations
        found = False
        for comb in combinations(edges, r):
            deg = [0]*n
            ok = True
            for (i, j) in comb:
                deg[i] += 1; deg[j] += 1
                if deg[i] > CAPv or deg[j] > CAPv: ok = False; break
            if ok: best = r; found = True; break
        if found: break
    # flow bound with cap 2
    dz = Dinic(2*n + 2); S, T = 0, 2*n+1
    for v in range(n):
        dz.add(S, 1+v, CAPv); dz.add(1+n+v, T, CAPv)
    for (i, j) in edges:
        dz.add(1+i, 1+n+j, 1); dz.add(1+j, 1+n+i, 1)
    ub = dz.maxflow(S, T)//2
    ok = best <= ub
    ok_all = ok_all and ok
    print("  trial %d: n=%d E=%d brute=%d flow-UB=%d %s" % (trial, n, len(edges), best, ub,
          "ok" if ok else "VIOLATION"))
print("P-1c:", "PASS" if ok_all else "FAIL")

# ---- main: three families ----
print("\nfamilies (deterministic rebuild):")
for seed in SEEDS:
    for A0 in SIZES:
        rng = np.random.default_rng(seed + A0)
        pos, D2, A = anneal(A0, rng)
        wedges = [(D2[i, j], i, j) for i in range(A) for j in range(i+1, A)
                  if core2 <= D2[i, j] <= reach2]
        edges = [(i, j) for w, i, j in wedges]
        ub = upper_bound_edges(A, edges)
        # lower bound: greedy + restarts (python RNG for shuffles)
        prng = random.Random(seed + A0)
        best = None; best_deg = None
        orders = [sorted(wedges)]
        for _ in range(8):
            e2 = wedges[:]; prng.shuffle(e2); orders.append(e2)
        for elist in orders:
            deg = np.zeros(A, int); used = set()
            for w, i, j in elist:
                if deg[i] < CAP and deg[j] < CAP:
                    deg[i] += 1; deg[j] += 1; used.add((i, j) if i < j else (j, i))
            for w, i, j in sorted(wedges):
                e = (i, j) if i < j else (j, i)
                if deg[i] < CAP and deg[j] < CAP and e not in used:
                    deg[i] += 1; deg[j] += 1; used.add(e)
            if best is None or len(used) > len(best):
                best = set(used); best_deg = deg.copy()
        # registered alternating-path augmentation (paths only)
        eset = [(i, j) if i < j else (j, i) for (i, j) in edges]
        augment_paths(A, eset, best, best_deg)
        lb = len(best)
        s_lo = 5 - 2*ub/A; s_hi = 5 - 2*lb/A
        results[(A0, seed)] = (s_lo, s_hi, lb, ub)
        print("seed %d A=%3d: E in [%d, %d] (gap %d) -> seats/A in [%.3f, %.3f] width %.3f [%.0fs]"
              % (seed, A0, lb, ub, ub-lb, s_lo, s_hi, s_hi-s_lo, time.time()-t0), flush=True)

heavy = [130, 180, 220]
centers = [ (results[(a,s)][0]+results[(a,s)][1])/2 for a in heavy for s in SEEDS ]
widths = [ results[(a,s)][1]-results[(a,s)][0] for a in heavy for s in SEEDS ]
c_h = float(np.mean(centers)); w_max = max(widths)
print("\nP-1a max heavy bracket width: %.3f (gate <= 0.02):" % w_max, "PASS" if w_max <= 0.02 else "FAIL")
ng = sum(1 for a in SIZES for s in SEEDS if results[(a,s)][3] == results[(a,s)][2])
print("   proven-optimal graphs (gap 0): %d / 24" % ng)
in_band = 0.22 <= c_h <= 0.30
print("P-1b heavy 3-family center: %.3f | declared [0.22, 0.30]:" % c_h, "PASS" if in_band else "FAIL")
print("   VERDICT: sharp-wall seat census vs measured 0.331: %+.1f%% -> undershoot %s"
      % (100*(c_h-0.331)/0.331, "CONFIRMED AND PINNED (physics fix = P-2 diffuse skin)" if c_h < 0.331 else "NOT confirmed"))
