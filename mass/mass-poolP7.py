#!/usr/bin/env python3
"""Pool stage P-7 — THE NATIVE DEPTH MAP (the named decider after P-5/P-6).

WHAT IS OWED: P-6 re-opened the plateau count (frozen window artifact share
-0.165) and left the light-edge saturation with exactly one owner standing:
credit-side pricing. Its named weakness was the u-map joint — the imported
Fermi map (a = 0.574 on the median radius) prices depth by a coordinate the
annealed droplet (compact core + diffuse halo) no longer matches.

THE MAP (zero new dials): the ledger's own energy IS the depth. Per node,
E_i = node_E (the same energy the anneal minimizes: lock credit + compression).
Bulk reference E_bulk = median E over the inner half (r <= Rh_eff). Native
depth coordinate:

    u_i = clip( 1 - E_i / E_bulk , 0, 1 )    (0 = fully bulk-bound, 1 = free)

— the same meaning the cost law's Fermi coordinate had (0 deep, 1 outside),
now read off the droplet itself. The cost law and credit are UNCHANGED:
cost(u) = CC u - TAUB2 u^{2/3} <= CREDIT (CC = 35.9, TAUB2 = 20.1,
CREDIT = gamma*^2 delta_pair = 9.694). phi_N = sum (CAP - deg)[in-pool] / A.
One map, three questions: plateau, asymptote, light edge.

GATES (pre-run; kills live; the escalation is pre-named):
  P7-fid  CONFIG IDENTITY: deterministic chassis (same seeds) must reproduce
          P-6 booked z_bulk(500) = 4.873 +- 0.005 and the retained-map ladder
          phi_W {30:0.656, 55:0.515, 107:0.305, 150:0.218, 195:0.200,
          220:0.177, 350:0.164, 500:0.101} each +- 0.002 — else STOP.
  P7a     THE PLATEAU: phi_N(220) in [0.265, 0.397] (measured 0.331 +- 20%).
          KILL below 0.15 or above 0.60 (dead-pole class).
  P7b     THE LIGHT EDGE (the credit-side owner's decisive test):
          phi_N(55) in [0.72, 1.08] (measured 0.90 +- 20%); phi_N(30)
          reported (intercept region expects ~1). FAIL here = the last owner
          dies -> ESCALATION PRE-NAMED: the T1 light-edge fact would then
          challenge the count-dilution FORM itself at small A (the form
          theorem's domain boundary becomes the object).
  P7c     THE ASYMPTOTE: A^{-1/3} fit on {150,195,220,350,500} family means:
          phi_inf in [0.08, 0.25].
  P7d     HONESTY + REPORTS: solver gap <= 1; E_bulk < 0 every cell (else
          cell flagged instrument-limit for the native map); u-distribution
          and in-pool fraction per size; halo share (u >= 0.9) vs evaporation
          counts; coordination fork u = 1 - q_i/q_bulk (q = availability,
          q_bulk = inner-quartile median) reported beside, not gated.

Run from workspace root. Registration commit = this file, pre-run.
"""
import numpy as np, math, random, time

RHO = 0.138; CORE = 1.72; REACH = 2.14
DP = 14.02; TAUB = 20.1
D0 = RHO ** (-1.0/3.0)
A_SKIN = 0.574
CAP = 5
core2, reach2 = CORE*CORE, REACH*REACH
SIZES = [30, 55, 107, 150, 195, 220, 350, 500]
SEEDS = [160812, 260812, 360812]
SWEEPS = 1500
FSWEEPS = 1500
SIGMA = 0.10*D0

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

def flow_ub(A, edges):
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

def rhalf_for(A):
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
            ax = rng.normal(size=3); ax -= ax.dot(pos[i])/max(r*r,1e-12)*pos[i]
            na = np.linalg.norm(ax)
            if na < 1e-9: continue
            ang = rng.uniform(-0.12, 0.12)
            newp = pos[i] + ax/na * (r*ang)
            newp *= r/np.linalg.norm(newp)
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

def full_anneal(pos, D2, rng):
    A = len(pos)
    E = np.array([node_E_row(D2[i], A) for i in range(A)])
    for s in range(FSWEEPS):
        T = 6.0 * (0.04/6.0) ** (s / (FSWEEPS-1))
        order = rng.permutation(A)
        for k in range(A):
            i = order[k]
            newp = pos[i] + SIGMA*rng.normal(size=3)
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

TAUB2, CC = 20.1, 35.9
CREDIT = 0.8314**2 * 14.02

def cost_u(u):
    return CC*u - TAUB2*max(u, 1e-12)**(2.0/3.0)

results = {}
t0 = time.time()
run_list = [(A0, sd) for sd in SEEDS for A0 in SIZES]
for (A0, seed) in run_list:
    rng = np.random.default_rng(seed + A0)
    Rh = rhalf_for(A0)
    pos = sample_positions(A0, Rh, rng)
    A = len(pos)
    pos, D2 = tangential_anneal(pos, rng)
    pos, D2 = full_anneal(pos, D2, rng)
    pos = pos - pos.mean(axis=0)
    dd = pos[:, None, :] - pos[None, :, :]
    D2 = np.einsum('ijk,ijk->ij', dd, dd); np.fill_diagonal(D2, 1e9)
    wedges = [(D2[i, j], i, j) for i in range(A) for j in range(i+1, A)
              if core2 <= D2[i, j] <= reach2]
    edges = [(i, j) for w, i, j in wedges]
    ub = flow_ub(A, edges)
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
    rr = np.linalg.norm(pos, axis=1)
    Rh_eff = float(np.median(rr))
    # retained map (fidelity)
    uu_f = 1.0/(1.0 + np.exp(-(rr - Rh_eff)/A_SKIN))
    inpool_f = np.array([cost_u(float(u)) for u in uu_f]) <= CREDIT
    phi_W = float((CAP - deg)[inpool_f].sum())/A
    interior = uu_f < 0.2
    zb = float(deg[interior].mean()) if interior.sum() > 3 else float('nan')
    # native energy-depth map (central)
    E = np.array([node_E_row(D2[i], A) for i in range(A)])
    inner = rr <= Rh_eff
    E_bulk = float(np.median(E[inner]))
    ok_native = E_bulk < 0
    if ok_native:
        u_nat = np.clip(1.0 - E/E_bulk, 0.0, 1.0)
        inpool_n = np.array([cost_u(float(u)) for u in u_nat]) <= CREDIT
        phi_N = float((CAP - deg)[inpool_n].sum())/A
        halo = float((u_nat >= 0.9).mean())
        poolfrac = float(inpool_n.mean())
    else:
        phi_N = float('nan'); halo = float('nan'); poolfrac = float('nan')
    # coordination fork (report)
    avail = np.zeros(A, int)
    for (i, j) in eset: avail[i] += 1; avail[j] += 1
    q_bulk = float(np.median(avail[rr <= np.percentile(rr, 25)]))
    u_co = np.clip(1.0 - avail/max(q_bulk, 1.0), 0.0, 1.0)
    inpool_c = np.array([cost_u(float(u)) for u in u_co]) <= CREDIT
    phi_C = float((CAP - deg)[inpool_c].sum())/A
    results[(A0, seed)] = dict(W=phi_W, N=phi_N, C=phi_C, gap=ub-lb, zb=zb,
                               Eb=E_bulk, halo=halo, pf=poolfrac, okn=ok_native)
    print("seed %d A=%3d: gap %d | z_bulk %s | phi_W %.3f | E_bulk %+.2f | PHI_N %s (pool %.0f%%, halo %.0f%%) | fork %.3f [%.0fs]"
          % (seed, A0, ub-lb, ("%.3f" % zb) if zb == zb else "n/a", phi_W, E_bulk,
             ("%.3f" % phi_N) if phi_N == phi_N else "n/a",
             100*poolfrac if poolfrac == poolfrac else -1,
             100*halo if halo == halo else -1, phi_C, time.time()-t0), flush=True)

def fam(A0, key):
    vals = [results[(A0, s)][key] for s in SEEDS]
    vals = [v for v in vals if v == v]
    return float(np.mean(vals)) if vals else float('nan')

BOOKED_W = {30: 0.656, 55: 0.515, 107: 0.305, 150: 0.218, 195: 0.200, 220: 0.177, 350: 0.164, 500: 0.101}
print("\nP7-fid CONFIG IDENTITY:")
fid = True
zb500 = fam(500, 'zb')
okz = abs(zb500 - 4.873) <= 0.005
print("  z_bulk(500) %.3f vs booked 4.873 -> %s" % (zb500, "ok" if okz else "MISS"))
fid = fid and okz
for a, bv in BOOKED_W.items():
    got = fam(a, 'W')
    ok = abs(got - bv) <= 0.002
    fid = fid and ok
    if not ok:
        print("  A=%3d: phi_W %.3f vs booked %.3f -> MISS" % (a, got, bv))
print("P7-fid:", "PASS — configs identical; scoring proceeds" if fid else "FAIL — STOP, no score")
if not fid:
    raise SystemExit(1)

n220 = fam(220, 'N')
print("\nP7a plateau: phi_N(220) = %.3f (measured 0.331; gate [0.265, 0.397]; kills <0.15 / >0.60) -> %s"
      % (n220, "PASS" if 0.265 <= n220 <= 0.397 else ("KILL" if (n220 < 0.15 or n220 > 0.60) else "FAIL")))
n55, n30 = fam(55, 'N'), fam(30, 'N')
print("P7b light edge: phi_N(55) = %.3f (measured 0.90; gate [0.72, 1.08]) -> %s | phi_N(30) = %.3f (expect ~1)"
      % (n55, "PASS — credit-side owner lands" if 0.72 <= n55 <= 1.08 else
         "FAIL — LAST OWNER DIES; escalation pre-named: the form's small-A domain becomes the object", n30))
As = np.array([150, 195, 220, 350, 500], float)
ph = np.array([fam(int(a), 'N') for a in As])
X = As**(-1.0/3.0)
c1, c0 = np.polyfit(X, ph, 1)
print("P7c asymptote: phi_N = %.3f + %.3f A^-1/3 | phi_inf = %.3f | gate [0.08, 0.25] -> %s | residuals %s"
      % (c0, c1, c0, "PASS" if 0.08 <= c0 <= 0.25 else "FAIL", np.round(ph - (c0 + c1*X), 3)))

gmax = max(r['gap'] for r in results.values())
badE = sum(1 for r in results.values() if not r['okn'])
print("\nP7d honesty: solver max gap %d (<=1) %s | E_bulk<0 violations: %d" % (gmax, "PASS" if gmax <= 1 else "FAIL", badE))
print("     phi_N ladder: %s" % {a: round(fam(a, 'N'), 3) for a in SIZES})
print("     phi_W ladder: %s (retained map, fidelity)" % {a: round(fam(a, 'W'), 3) for a in SIZES})
print("     fork ladder:  %s (coordination map, report-only)" % {a: round(fam(a, 'C'), 3) for a in SIZES})
print("     E_bulk ladder: %s MeV" % {a: round(fam(a, 'Eb'), 2) for a in SIZES})
print("     halo (u>=0.9) share: %s | in-pool frac: %s"
      % ({a: round(fam(a, 'halo'), 2) for a in SIZES}, {a: round(fam(a, 'pf'), 2) for a in SIZES}))
