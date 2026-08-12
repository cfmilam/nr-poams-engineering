#!/usr/bin/env python3
# Pool stage P-2 — THE DIFFUSE-SKIN TEST. Registration: 7c06416 (pre-run).
# Profile: Fermi with a = 0.574 fm (ledger's derived tail); tangential-only anneal;
# exact solver (P-1); census fork R-A gated / R-B reported. Kill live both directions.
import numpy as np, math, random, time

RHO = 0.138; CORE = 1.72; REACH = 2.14
DP = 14.02; TAUB = 20.1
D0 = RHO ** (-1.0/3.0)
A_SKIN = 0.574
CAP = 5
core2, reach2 = CORE*CORE, REACH*REACH
SIZES = [60, 130, 220]
SEEDS = [160812, 260812, 360812]
SWEEPS = 1500

# ---------------- Dinic (from P-1, validated) ----------------
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
    dz = Dinic(2*A + 2); S, T = 0, 2*A + 1
    for v in range(A):
        dz.add(S, 1 + v, CAP); dz.add(1 + A + v, T, CAP)
    for (i, j) in edges:
        dz.add(1 + i, 1 + A + j, 1); dz.add(1 + j, 1 + A + i, 1)
    return dz.maxflow(S, T) // 2

def augment_paths(A, edges, M, deg, max_depth=24):
    nbr = [[] for _ in range(A)]
    for (i, j) in edges:
        nbr[i].append(j); nbr[j].append(i)
    def key(a, b): return (a, b) if a < b else (b, a)
    progress = True
    while progress:
        progress = False
        for u in [v for v in range(A) if deg[v] < CAP]:
            if deg[u] >= CAP: continue
            stack = [(u, True, ())]
            seen = set(); done = False
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
                        if deg[w] < CAP and w != u:
                            newpath = path + (e,)
                            for idx, pe in enumerate(newpath):
                                if idx % 2 == 0:
                                    M.add(pe); deg[pe[0]] += 1; deg[pe[1]] += 1
                                else:
                                    M.discard(pe); deg[pe[0]] -= 1; deg[pe[1]] -= 1
                            progress = True; done = True; break
                        if (w, False) not in seen:
                            stack.append((w, False, path + (e,)))
                    elif (not needU) and inM:
                        if (w, True) not in seen:
                            stack.append((w, True, path + (e,)))
                if done: break
    return M, deg

# ---------------- profile ----------------
def rhalf_for(A):
    # solve int 4 pi r^2 rho0/(1+exp((r-Rh)/a)) dr = A
    lo, hi = 1.0, 15.0
    for _ in range(80):
        mid = 0.5*(lo + hi)
        rs = np.linspace(0, mid + 12*A_SKIN, 4000)
        m = np.trapezoid(4*math.pi*rs**2 * RHO/(1 + np.exp((rs - mid)/A_SKIN)), rs)
        if m < A: lo = mid
        else: hi = mid
    return 0.5*(lo + hi)

def sample_positions(A, Rh, rng):
    rs_grid = np.linspace(0, Rh + 12*A_SKIN, 6000)
    w = 4*math.pi*rs_grid**2 * RHO/(1 + np.exp((rs_grid - Rh)/A_SKIN))
    cdf = np.cumsum(w); cdf /= cdf[-1]
    pos = []
    tries = 0
    while len(pos) < A and tries < 400000:
        tries += 1
        r = float(np.interp(rng.random(), cdf, rs_grid))
        u = rng.random()*2 - 1; ph = rng.random()*2*math.pi
        s = math.sqrt(1 - u*u)
        p = np.array([r*s*math.cos(ph), r*s*math.sin(ph), r*u])
        ok = True
        for q in pos:
            d = p - q
            if np.dot(d, d) < (0.95*D0)**2: ok = False; break
        if ok: pos.append(p)
    return np.array(pos)

def node_E_row(row, A):
    k = min(CAP, A-1)
    idx = np.argpartition(row, k)[:k]
    d = np.sqrt(row[idx]); dbar = d.mean()
    Lk = int(np.count_nonzero((d >= CORE) & (d <= REACH)))
    return -(DP/2.0)*Lk + TAUB*(D0/dbar)**2

def tangential_anneal(pos, rng):
    A = len(pos)
    dd = pos[:, None, :] - pos[None, :, :]
    D2 = np.einsum('ijk,ijk->ij', dd, dd); np.fill_diagonal(D2, 1e9)
    E = np.array([node_E_row(D2[i], A) for i in range(A)])
    for s in range(SWEEPS):
        T = 6.0 * (0.04/6.0) ** (s / (SWEEPS-1))
        order = rng.permutation(A)
        for k in range(A):
            i = order[k]
            r = np.linalg.norm(pos[i])
            if r < 1e-6: continue
            # tangential step: random small rotation of the position vector
            ax = rng.normal(size=3); ax -= ax.dot(pos[i])/max(r*r,1e-12)*pos[i]
            na = np.linalg.norm(ax)
            if na < 1e-9: continue
            ang = rng.uniform(-0.12, 0.12)
            newp = pos[i] + ax/na * (r*ang)
            newp *= r/np.linalg.norm(newp)          # exact radius preservation
            d1 = pos - newp
            rnew = np.einsum('ij,ij->i', d1, d1); rnew[i] = 1e9
            if rnew.min() < core2: continue
            aff = np.flatnonzero((D2[i] < (1.6*REACH)**2) | (rnew < (1.6*REACH)**2))
            Eold = E[i] + E[aff].sum()
            rowi_old = D2[i].copy()
            D2[i, :] = rnew; D2[:, i] = rnew
            Enew_i = node_E_row(D2[i], A)
            Enew = Enew_i + sum(node_E_row(D2[j], A) for j in aff)
            if Enew - Eold <= 0 or (T > 1e-9 and math.exp(-(Enew-Eold)/T) > rng.random()):
                pos[i] = newp; E[i] = Enew_i
                for j in aff: E[j] = node_E_row(D2[j], A)
            else:
                D2[i, :] = rowi_old; D2[:, i] = rowi_old
    return pos, D2

results = {}
t0 = time.time()
run_list = [(A0, sd) for sd in SEEDS for A0 in SIZES] + [(350, 160812)]
for (A0, seed) in run_list:
    rng = np.random.default_rng(seed + A0)
    Rh = rhalf_for(A0)
    pos = sample_positions(A0, Rh, rng)
    A = len(pos)
    pos, D2 = tangential_anneal(pos, rng)
    wedges = [(D2[i, j], i, j) for i in range(A) for j in range(i+1, A)
              if core2 <= D2[i, j] <= reach2]
    edges = [(i, j) for w, i, j in wedges]
    ub = upper_bound_edges(A, edges)
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
        if best is None or len(used) > len(best):
            best = set(used); best_deg = deg.copy()
    eset = [(i, j) if i < j else (j, i) for (i, j) in edges]
    best, best_deg = augment_paths(A, eset, best, best_deg)
    lb = len(best)
    deg = best_deg
    seats_RA = float((CAP - deg).sum())/A
    hosts = deg >= 1
    seats_RB = float((CAP - deg)[hosts].sum())/A
    ndeg0 = int((deg == 0).sum())
    results[(A0, seed)] = dict(RA=seats_RA, RB=seats_RB, gap=ub-lb, A=A, deg0=ndeg0,
                               Rh=Rh, z=float(deg.mean()))
    print("seed %d A=%3d (Rh %.2f): E*[%d,%d] gap %d | z %.3f deg0 %d | R-A %.3f  R-B %.3f  [%.0fs]"
          % (seed, A0, Rh, lb, ub, ub-lb, float(deg.mean()), ndeg0, seats_RA, seats_RB,
             time.time()-t0), flush=True)

def fam_mean(A0, key):
    return float(np.mean([results[(A0, s)][key] for s in SEEDS]))
heavyRA = float(np.mean([fam_mean(a, 'RA') for a in (130, 220)]))
heavyRB = float(np.mean([fam_mean(a, 'RB') for a in (130, 220)]))
print("\nP-2a R-A heavy mean = %.3f | gate [0.25, 0.41] (measured 0.331):" % heavyRA,
      "PASS" if 0.25 <= heavyRA <= 0.41 else ("FAIL LOW — SEAT UNIT DEAD" if heavyRA < 0.25
      else "FAIL HIGH — raw rule dead; R-B fork = %.3f (reported)" % heavyRB))
print("   R-B heavy mean (host-adjacency, reported): %.3f (%+.1f%% vs 0.331)"
      % (heavyRB, 100*(heavyRB-0.331)/0.331))
sh = fam_mean(60, 'RA') > fam_mean(220, 'RA')
print("P-2b shape: R-A phi(60) %.3f > phi(220) %.3f ->" % (fam_mean(60,'RA'), fam_mean(220,'RA')),
      "PASS" if sh else "FAIL", "| R-B: %.3f vs %.3f" % (fam_mean(60,'RB'), fam_mean(220,'RB')))
gmax = max(r['gap'] for r in results.values())
print("P-2c solver: max gap %d (<=1):" % gmax, "PASS" if gmax <= 1 else "FAIL")
print("A=350 report: R-A %.3f R-B %.3f (gap %d)" % (results[(350,160812)]['RA'],
      results[(350,160812)]['RB'], results[(350,160812)]['gap']))
