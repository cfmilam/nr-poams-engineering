#!/usr/bin/env python3
"""Pool stage P-5 — THE LIGHT-EDGE SATURATION CLAUSE (the lock-surcharge census).

WHAT IS OWED: P-4's booked Q1 FAIL (+21.3%: predicted 8.32 vs measured 6.86 at
A = 55) named 'light-edge saturation' — swing-34's intercept fact reads n_f -> A
at the light edge ('light limit 1 by construction'), while the seat census reads
0.61. The clause must produce the crossover FROM STANDING CONSTANTS ONLY and
must NOT flood the plateau.

MECHANISM (registered; zero new dials): participation = the seat pool (P-3,
untouched) PLUS the lock-surcharge channel: an interior cell pair can host the
borrowed half-turn by OPENING its lock — paying the ledger's own lock price
DP/2 = 7.01 — profitable while

    (cost(u_i) + cost(u_j))/2 + DP/2 <= CREDIT = gamma*^2 delta_pair = 9.694,

i.e. mean depth cost <= 2.684 (all standing constants: CC = 35.9, TAUB2 = 20.1,
cost(u) = CC u - TAUB2 u^{2/3}). STRUCTURAL RESTRICTION (the physics that can
kill it): only a NON-CRITICAL lock can open — a lock present in EVERY maximum
matching (critical) cannot release capacity without cascading beyond its own
price. Criticality is exactly computable: e is critical iff maxflow(G - e) <
maxflow(G) on the validated double-cover flow oracle (P-1). RIGID bulk ->
few non-critical locks -> plateau preserved; LOOSE light droplets -> many ->
saturation. The instrument decides which way the matching structure actually
falls; BOTH outcomes are pre-named.

    phi_eff = [ SUM (CAP - deg)[in-pool]  +  N_open ] / A,
    N_open = #{ locks in the scored matching : profitable AND non-critical },
    one hosting site per opened lock (the swing-33 borrow-through-a-pair
    reading; the 2-patch variant is report-only).

HAND EXPECTATIONS (declared): N_open/A at A=55 needs ~0.29 to hit the measured
0.90; at A=220 the clause lands only if N_open/A < ~0.05. If the bulk matching
carries abundant alternating cycles the channel floods and THE CLAUSE DIES AS
REGISTERED (finding: saturation owner is credit-side, not structure-side).

GATES (pre-run):
  P5-fid  FIDELITY: same chassis, same seeds -> phi_W must reproduce P-4 booked
          {55: 0.612, 107: 0.595, 150: 0.425, 195: 0.398, 220: 0.342} within
          +/-0.010 each — else STOP, no score.
  P5a     THE LIGHT EDGE: phi_eff(55) in [0.75, 1.05] (measured 0.90).
  P5b     THE PLATEAU KILL: phi_eff(220) <= phi_W(220) + 0.05 — else FAIL:
          channel floods, clause dead, booked as found.
  P5c     THE CURVE RE-SCORE at T1 quartile centers (pred = 6.51/sqrt(phi_eff)):
          Q1 |dev| <= 12% (booked +21.3%); Q2 |dev| <= 8% (booked -11%);
          Q3 dev >= -8% (booked -4.9%); Q4 dev >= -5% (booked -2.2%) —
          the clause must fix the light edge WITHOUT degrading the landed
          quartiles beyond ~3 points.
  P5d     REPORTS: A=30 light anchor (swing-34 intercept region; expect -> ~1);
          crossover scale A_sat (N_open/A falls to half its A=30 value);
          solver honesty (gap <= 1 all cells; criticality oracle = flow UB,
          the <=1 LP-gap joint named); 2-patch variant; per-cell N_open/A.

Run from workspace root. Registration commit = this file, pre-run.
"""
import numpy as np, math, random, time

RHO = 0.138; CORE = 1.72; REACH = 2.14
DP = 14.02; TAUB = 20.1
D0 = RHO ** (-1.0/3.0)
A_SKIN = 0.574
CAP = 5
core2, reach2 = CORE*CORE, REACH*REACH
SIZES = [30, 55, 107, 150, 195, 220]
SEEDS = [160812, 260812, 360812]
SWEEPS = 1500

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

def flow_ub(A, edges, skip=None):
    dz = Dinic(2*A + 2); S, T = 0, 2*A + 1
    for v in range(A):
        dz.add(S, 1 + v, CAP); dz.add(1 + A + v, T, CAP)
    for (i, j) in edges:
        if skip is not None and (i, j) == skip: continue
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

TAUB2, CC = 20.1, 35.9
CREDIT = 0.8314**2 * 14.02
SURCH = DP/2.0

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
    seats_RA = float((CAP - deg).sum())/A
    rr = np.linalg.norm(pos, axis=1)
    uu = 1.0/(1.0 + np.exp(-(rr - Rh)/A_SKIN))
    costs = np.array([cost_u(float(u)) for u in uu])
    inpool = costs <= CREDIT
    seats_W = float((CAP - deg)[inpool].sum())/A
    # ---- P-5 lock-surcharge channel ----
    locks = sorted(best)
    n_prof = 0; n_open = 0; n_crit_prof = 0
    for (i, j) in locks:
        cpair = 0.5*(costs[i] + costs[j])
        if cpair + SURCH <= CREDIT:
            n_prof += 1
            if flow_ub(A, eset, skip=(i, j)) < ub:
                n_crit_prof += 1
            else:
                n_open += 1
    phi_eff = seats_W + n_open/A
    phi_eff2 = seats_W + 2.0*n_open/A  # 2-patch variant, report-only
    results[(A0, seed)] = dict(RA=seats_RA, W=seats_W, EFF=phi_eff, EFF2=phi_eff2,
                               NOPEN=n_open, NPROF=n_prof, NCRIT=n_crit_prof,
                               gap=ub-lb, A=A, z=float(deg.mean()))
    print("seed %d A=%3d: gap %d | z %.3f | phi_W %.3f | locks %d prof %d crit %d OPEN %d -> phi_eff %.3f (2p %.3f) [%.0fs]"
          % (seed, A0, ub-lb, float(deg.mean()), seats_W, len(locks), n_prof,
             n_crit_prof, n_open, phi_eff, phi_eff2, time.time()-t0), flush=True)

def fam(A0, key):
    return float(np.mean([results[(A0, s)][key] for s in SEEDS]))

BOOKED = {55: 0.612, 107: 0.595, 150: 0.425, 195: 0.398, 220: 0.342}
print("\nP5-fid FIDELITY (phi_W vs P-4 booked):")
fid = True
for a, bv in BOOKED.items():
    got = fam(a, 'W')
    ok = abs(got - bv) <= 0.010
    fid = fid and ok
    print("  A=%3d: phi_W %.3f vs booked %.3f -> %s" % (a, got, bv, "ok" if ok else "MISS"))
print("P5-fid:", "PASS — scoring proceeds" if fid else "FAIL — STOP, no score")
if not fid:
    raise SystemExit(1)

e55 = fam(55, 'EFF')
print("\nP5a light edge: phi_eff(55) = %.3f (measured 0.90; gate [0.75, 1.05]) -> %s"
      % (e55, "PASS" if 0.75 <= e55 <= 1.05 else "FAIL"))
e220, w220 = fam(220, 'EFF'), fam(220, 'W')
print("P5b plateau: phi_eff(220) = %.3f vs phi_W %.3f (drift %.3f, gate <= 0.05) -> %s"
      % (e220, w220, e220 - w220, "PASS" if e220 - w220 <= 0.05 else
         "FAIL — CHANNEL FLOODS, clause dead as registered"))

DCELL = 6.51
T1_MEAS = {55: 6.86, 107: 9.48, 150: 10.51, 195: 10.55}
GATE = {55: ("|dev|<=12%", lambda d: abs(d) <= 0.12),
        107: ("|dev|<=8%", lambda d: abs(d) <= 0.08),
        150: ("dev>=-8%", lambda d: d >= -0.08),
        195: ("dev>=-5%", lambda d: d >= -0.05)}
print("\nP5c curve re-score (pred = 6.51/sqrt(phi_eff)):")
allok = True
for a in (55, 107, 150, 195):
    ph = fam(a, 'EFF')
    pred = DCELL/math.sqrt(ph)
    dev = (pred - T1_MEAS[a])/T1_MEAS[a]
    lab, fn = GATE[a]
    ok = fn(dev)
    allok = allok and ok
    print("  A=%3d: phi_eff %.3f -> pred %.2f vs %.2f  (%+.1f%%; %s) -> %s"
          % (a, ph, pred, T1_MEAS[a], 100*dev, lab, "PASS" if ok else "FAIL"))
print("P5c:", "PASS — the clause lands" if allok else "FAIL — booked as found")

print("\nP5d reports:")
print("  A=30 light anchor: phi_eff %.3f (phi_W %.3f) — intercept region, expect -> ~1" % (fam(30,'EFF'), fam(30,'W')))
no30 = fam(30, 'NOPEN')/30.0
asat = None
for a in SIZES:
    if fam(a, 'NOPEN')/a <= 0.5*no30:
        asat = a; break
print("  N_open/A per size: %s | crossover A_sat (half the A=30 share): %s"
      % ({a: round(fam(a,'NOPEN')/a, 3) for a in SIZES}, asat))
print("  2-patch variant phi_eff2: %s" % {a: round(fam(a,'EFF2'), 3) for a in SIZES})
gmax = max(r['gap'] for r in results.values())
print("  solver: max gap %d (<=1) -> %s | criticality oracle = flow UB (LP-gap <=1 joint, named)"
      % (gmax, "PASS" if gmax <= 1 else "FAIL"))
print("  profitable/critical/open per size: %s"
      % {a: (round(fam(a,'NPROF'),1), round(fam(a,'NCRIT'),1), round(fam(a,'NOPEN'),1)) for a in SIZES})
