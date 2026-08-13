#!/usr/bin/env python3
# Pool stage P-4 — FINITE-SIZE CAMPAIGN + THE PARTICIPATION CURVE. Registration: 7dcc50e (pre-run).
# Profile: Fermi with a = 0.574 fm (ledger's derived tail); tangential-only anneal;
# exact solver (P-1); census fork R-A gated / R-B reported. Kill live both directions.
import numpy as np, math, random, time

RHO = 0.138; CORE = 1.72; REACH = 2.14
DP = 14.02; TAUB = 20.1
D0 = RHO ** (-1.0/3.0)
A_SKIN = 0.574
CAP = 5
core2, reach2 = CORE*CORE, REACH*REACH
SIZES = [55, 107, 150, 195, 220, 350, 500]
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
run_list = [(A0, sd) for sd in SEEDS for A0 in SIZES]
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
    # P-3 weighted census: cost(u) <= credit, u from the droplet's own profile
    TAUB2, CC, AV = 20.1, 35.9, 15.8
    CREDIT = 0.8314**2 * 14.02
    rr = np.linalg.norm(pos, axis=1)
    uu = 1.0/(1.0 + np.exp(-(rr - Rh)/A_SKIN))
    inpool = (CC*uu - TAUB2*np.maximum(uu, 1e-12)**(2/3)) <= CREDIT
    seats_W = float((CAP - deg)[inpool].sum())/A
    # fork (reported): coordination-local u = 1 - avail/z_bulk_avail (z_bulk approx 6.6 at rho0 reach shell, annealed)
    avail = np.zeros(A, int)
    for (i, j) in eset: avail[i] += 1; avail[j] += 1
    ucoord = np.clip(1.0 - avail/6.0, 0.0, 1.0)
    inpool2 = (CC*ucoord - TAUB2*np.maximum(ucoord, 1e-12)**(2/3)) <= CREDIT
    seats_W2 = float((CAP - deg)[inpool2].sum())/A
    results[(A0, seed)] = dict(RA=seats_RA, W=seats_W, W2=seats_W2, gap=ub-lb, A=A,
                               Rh=Rh, z=float(deg.mean()), fin=float(inpool.mean()))
    print("seed %d A=%3d: E*[%d,%d] gap %d | z %.3f | raw %.3f  WEIGHTED %.3f (in-pool cells %.0f%%)  fork %.3f  [%.0fs]"
          % (seed, A0, lb, ub, ub-lb, float(deg.mean()), seats_RA, seats_W,
             100*float(inpool.mean()), seats_W2, time.time()-t0), flush=True)

def fam_mean(A0, key):
    return float(np.mean([results[(A0, s)][key] for s in SEEDS]))

DCELL = 6.51
T1_MEAS = {55: 6.86, 107: 9.48, 150: 10.51, 195: 10.55}
print("\nP-4a THE CURVE: predicted Delta*sqrtA = dcell/sqrt(phi_W) at the T1 quartile centers")
worst = 0.0; all20 = True
for a in (55, 107, 150, 195):
    phi = fam_mean(a, 'W')
    pred = DCELL/math.sqrt(phi)
    meas = T1_MEAS[a]
    dev = (pred - meas)/meas
    worst = max(worst, abs(dev))
    all20 = all20 and abs(dev) <= 0.20
    print("  A=%3d: phi_W %.3f -> pred %.2f vs measured %.2f  (%+.1f%%)" % (a, phi, pred, meas, 100*dev))
print("P-4a:", "PASS (all within 20%%, worst %.1f%%)" % (100*worst) if all20 else
      ("KILL — off by >35%" if worst > 0.35 else "FAIL (worst %.1f%%)" % (100*worst)))
w220 = fam_mean(220, 'W')
print("P-4b window A=220: %.3f vs 0.331 (%+.1f%%):" % (w220, 100*(w220-0.331)/0.331),
      "PASS" if abs(w220-0.331)/0.331 <= 0.15 else "FAIL")
# asymptote fit on {150, 195, 220, 350, 500}
import numpy as _np
As = _np.array([150, 195, 220, 350, 500], float)
ph = _np.array([fam_mean(int(a), 'W') for a in As])
X = As**(-1.0/3.0)
c1, c0 = _np.polyfit(X, ph, 1)
res = ph - (c0 + c1*X)
print("P-4c asymptote: phi_W = %.3f + %.3f A^-1/3 | phi_inf = %.3f | residuals %s" %
      (c0, c1, c0, _np.round(res, 3)))
print("      gate phi_inf in [0.20, 0.35]:", "PASS" if 0.20 <= c0 <= 0.35 else "FAIL",
      "| A=500 3-family mean: %.3f" % fam_mean(500, 'W'))
gmax = max(r['gap'] for r in results.values())
mono = all(fam_mean(a,'W') >= fam_mean(b,'W') - 0.02 for a, b in zip((55,107,150,195,220,350),(107,150,195,220,350,500)))
print("P-4d solver max gap %d (<=1): %s | monotone shape: %s" %
      (gmax, "PASS" if gmax <= 1 else "FAIL", "PASS" if mono else "FAIL"))
