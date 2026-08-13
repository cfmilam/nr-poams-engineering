#!/usr/bin/env python3
"""Pool stage P-6 — THE FULL-ANNEAL INSTRUMENT (asymptote + light-edge retest).

WHAT IS OWED: (1) P-4 booked the asymptote NOT-extractable — tangential-frozen
interiors undercoordinate (z 4.31-4.38 vs the seam's realized 4.846); the
full-anneal follow-up was named on the record. (2) P-5 killed the structure-side
saturation clause both directions — the light edge's owner narrowed to
credit-side pricing OR anneal fidelity. One instrument answers both.

METHOD (chassis unchanged through the tangential stage, then the new stage):
  sample Fermi(a = 0.574) -> tangential anneal 1500 sweeps (identical code
  path, same seeds — P-4/P-5 continuity) -> FULL 3-D anneal 1500 further
  sweeps: free displacement moves (gaussian sigma = 0.10 D0 per component,
  core guard, same node_E, same T ladder restarted) — the interaction builds
  its own droplet; the Fermi envelope is no longer frozen. Recenter, then
  lock graph + exact solver (P-1, unchanged) + the P-3 weighted census with
  the u-map anchored at the annealed droplet's own half-count radius
  (Rh_eff = median node radius; tail parameter a = 0.574 retained as the map
  — JOINT NAMED: the annealed tail's true width is reported beside it).

GATES (pre-run; kills live):
  P6a FIDELITY ANCHOR (the ledger's own derived target): interior coordination
      z_bulk(500) (nodes with u < 0.2) must land in [4.65, 5.00] — the
      capacity seam's REALIZED count 4.846 (swing 41) is what honest bulk
      looks like. Below band -> the anneal is still inadequate: INSTRUMENT-
      LIMIT booked, NO phi_inf claim (no score of P6b). Above 5.00 ->
      overpacking, same clause.
  P6b THE ASYMPTOTE (only if P6a passes): A^{-1/3} fit on {150,195,220,350,500}
      family means: phi_inf in [0.08, 0.25] (the 5 - z_bulk ~ 0.15-class
      expectation, swing-41 lineage). Outside -> FAIL booked, band named.
  P6c THE WINDOW — PRE-NAMED TENSION, both outcomes booked: phi_W(220) vs
      measured 0.331. Honest annealing raises z and LOWERS phi(220); within
      +/-15% -> the window survives full fidelity; below -> the tangential-
      frozen window pass carried an instrument-artifact share — named, with
      the frozen-vs-annealed delta quantified.
  P6d THE LIGHT EDGE RETEST (report-grade): phi_W(30), phi_W(55) — direction
      vs the measured 0.90 at A=55 (and ~1 at the intercept region). Does
      honest annealing move the light edge toward saturation (anneal-fidelity
      owner) or not (credit-side owner)?
  P6e HONESTY: solver gap <= 1 every cell; anneal convergence (mean node-E
      drift over the last 150 full-anneal sweeps, |drift| < 1% of |E|,
      reported per size); evaporation guard (nodes beyond Rh_eff + 6a
      counted; > 2% of A flags the cell); z_bulk ladder and measured tail
      width reported per size.

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
    """Free-displacement stage: the interaction builds its own droplet."""
    A = len(pos)
    E = np.array([node_E_row(D2[i], A) for i in range(A)])
    drift_track = []
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
        if s >= FSWEEPS - 150:
            drift_track.append(float(E.mean()))
    drift = (drift_track[-1] - drift_track[0])/max(abs(drift_track[0]), 1e-9) if len(drift_track) > 1 else 0.0
    return pos, D2, drift

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
    pos, D2, drift = full_anneal(pos, D2, rng)
    pos = pos - pos.mean(axis=0)          # recenter
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
    uu = 1.0/(1.0 + np.exp(-(rr - Rh_eff)/A_SKIN))
    inpool = np.array([cost_u(float(u)) for u in uu]) <= CREDIT
    seats_W = float((CAP - deg)[inpool].sum())/A
    interior = uu < 0.2
    zb = float(deg[interior].mean()) if interior.sum() > 3 else float('nan')
    evap = int((rr > Rh_eff + 6*A_SKIN).sum())
    # measured tail width: r span between 90% and 10% node-count shells / 4.4 (Fermi t90-10 = 4.4a)
    r10, r90 = np.percentile(rr, [10, 90])
    a_meas = float((np.percentile(rr, 97.5) - np.percentile(rr, 84)))/2.2  # crude outer-shell width scale, report-only
    results[(A0, seed)] = dict(W=seats_W, gap=ub-lb, A=A, z=float(deg.mean()), zb=zb,
                               drift=drift, evap=evap, Rh=Rh_eff, am=a_meas)
    print("seed %d A=%3d: gap %d | z %.3f z_bulk %s | phi_W %.3f | drift %+.4f evap %d | Rh_eff %.2f a_meas %.2f [%.0fs]"
          % (seed, A0, ub-lb, float(deg.mean()),
             ("%.3f" % zb) if zb == zb else "n/a", seats_W, drift, evap, Rh_eff, a_meas, time.time()-t0), flush=True)

def fam(A0, key):
    vals = [results[(A0, s)][key] for s in SEEDS]
    vals = [v for v in vals if v == v]
    return float(np.mean(vals)) if vals else float('nan')

print("\nP6a FIDELITY ANCHOR: z_bulk(500) = %.3f | seam realized 4.846 | gate [4.65, 5.00]" % fam(500, 'zb'))
p6a = 4.65 <= fam(500, 'zb') <= 5.00
print("P6a:", "PASS — honest bulk reached; scoring proceeds" if p6a else
      "INSTRUMENT-LIMIT — anneal inadequate (or overpacked); NO phi_inf claim, P6b unscored")

if p6a:
    As = np.array([150, 195, 220, 350, 500], float)
    ph = np.array([fam(int(a), 'W') for a in As])
    X = As**(-1.0/3.0)
    c1, c0 = np.polyfit(X, ph, 1)
    res = ph - (c0 + c1*X)
    print("\nP6b asymptote: phi_W = %.3f + %.3f A^-1/3 | phi_inf = %.3f | gate [0.08, 0.25] -> %s | residuals %s"
          % (c0, c1, c0, "PASS" if 0.08 <= c0 <= 0.25 else "FAIL", np.round(res, 3)))
else:
    print("\nP6b: unscored (P6a clause)")

w220 = fam(220, 'W')
dev = (w220 - 0.331)/0.331
print("\nP6c window at full fidelity: phi_W(220) = %.3f vs 0.331 (%+.1f%%)" % (w220, 100*dev))
print("P6c:", ("window SURVIVES full anneal (within 15%)" if abs(dev) <= 0.15 else
      "window carried a frozen-instrument share — named: frozen 0.342 vs annealed %.3f (delta %+.3f)" % (w220, w220 - 0.342)))

print("\nP6d light edge retest: phi_W(30) = %.3f, phi_W(55) = %.3f (measured light edge 0.90 at 55; ~1 at intercept)"
      % (fam(30, 'W'), fam(55, 'W')))
print("     direction: %s" % ("TOWARD saturation — anneal-fidelity owns a share" if fam(55, 'W') > 0.65 else
      "NOT toward saturation — credit-side owner stands alone"))

gmax = max(r['gap'] for r in results.values())
emax = max(r['evap'] for r in results.values())
dmax = max(abs(r['drift']) for r in results.values())
print("\nP6e honesty: solver max gap %d (<=1) %s | max evap %d | max |drift| %.4f (<0.01) %s"
      % (gmax, "PASS" if gmax <= 1 else "FAIL", emax, dmax, "PASS" if dmax < 0.01 else "FLAG"))
print("     z_bulk ladder: %s" % {a: round(fam(a, 'zb'), 3) for a in SIZES})
print("     phi_W ladder:  %s" % {a: round(fam(a, 'W'), 3) for a in SIZES})
print("     a_meas ladder: %s (map retained a = 0.574 — joint named)" % {a: round(fam(a, 'am'), 2) for a in SIZES})
