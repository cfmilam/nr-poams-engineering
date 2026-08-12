#!/usr/bin/env python3
# Swing 20 — consistency audit of the swing-19 rule table. Registration: 0b00a0d.
# Corrected cluster table (all rules under single conventions) + deterministic
# bulk rerun (swing-17/19 constructions). R1 expected sole survivor.
import numpy as np, math, time

RHO = 0.138; CORE = 1.72; REACH = 2.14; ZC = 4.78; HB2M = 41.47
DP0 = 14.02; TAUB = 20.1; BOOKS = 35.85; WIN = (32.0, 40.0); CAP = 5
D0 = RHO ** (-1.0/3.0)

def consts(rq):
    dp = HB2M/(4*rq*rq); c3 = HB2M*0.75/(18*rq*rq); c4 = HB2M*0.5/(32*rq*rq)
    return dp, c3, c4, 2*c3/ZC

dp, c3, c4, h = consts(0.86)
T_MEAS, T_BAND = 0.84, 0.15
A_MEAS, A_BAND = 3.39, 0.20

print("SWING 20 — corrected cluster kill table (single-convention rules)")
print("constants: dp=%.3f c3=%.3f c4=%.3f h=%.3f" % (dp, c3, c4, h))
# (t_step, a_step) — hand-derivable, single convention each:
rules = {
    "R1 first-suppressed(raw)":  (h, h + c3),          # per bond: 1st->h, rest->c3
    "R2a loop=c3 total /E":      (c3/3.0, 3*c3/6.0),   # t: T=1,E=3; K4: T=3,E=6
    "R2b loop=3c3 mode /E":      (c3, 9*c3/6.0),       # t: 3c3/3; K4: 9c3/6
    "R3 R2a + blanket h":        (c3/3.0 + h, 3*c3/6.0 + h),
    "R4 h per loop /E":          (h/3.0, 3*h/6.0),
    "R5 raw-full":               (c3, 2*c3),           # per bond: n3 full credits
    "R6 first-supp(indep/bond)": (h, h + 0.5*c3),      # K4 mean indep-through-bond 1.5
}
survivors = []
for name, (ts, as_) in rules.items():
    rt = (ts - T_MEAS)/T_BAND; ra = (as_ - A_MEAS)/A_BAND
    chi2 = rt*rt + ra*ra
    dead = abs(rt) > 4 or abs(ra) > 4 or chi2 > 9
    print("  %-26s t=%.3f (%+.1fx)  a=%.3f (%+.1fx)  chi2=%.2f -> %s"
          % (name, ts, rt, as_, ra, chi2, "DEAD" if dead else "SURVIVES"))
    if not dead: survivors.append(name)
print("Survivors:", ", ".join(survivors))
print("S20a UNIQUENESS:", "PASS — R1 is the sole admissible bookkeeping"
      if survivors == ["R1 first-suppressed(raw)"] else "DEVIATION — inspect")

# ---------------- bulk rerun (deterministic; swing-17/19 machinery) ----------------
def full_d2(pos, L):
    d = pos[:, None, :] - pos[None, :, :]
    d -= L * np.round(d / L)
    d2 = np.einsum('ijk,ijk->ij', d, d)
    np.fill_diagonal(d2, 1e9)
    return d2

def lock_graph(pos, L, N):
    d2 = full_d2(pos, L)
    avail = d2 <= REACH*REACH
    ii, jj = np.nonzero(np.triu(avail, 1))
    order = np.argsort(d2[ii, jj])
    ii, jj = ii[order], jj[order]
    adj_av = [set(int(v) for v in np.flatnonzero(avail[i])) for i in range(N)]
    locked = [set() for _ in range(N)]
    for a, b in zip(ii, jj):
        a, b = int(a), int(b)
        if len(locked[a]) < CAP and len(locked[b]) < CAP:
            locked[a].add(b); locked[b].add(a)
    improved = True; passes = 0
    while improved and passes < 40:
        improved = False; passes += 1
        for u in range(N):
            if len(locked[u]) >= CAP: continue
            for v in adj_av[u]:
                if v in locked[u]: continue
                if len(locked[u]) >= CAP: break
                if len(locked[v]) < CAP:
                    locked[u].add(v); locked[v].add(u); improved = True
            if len(locked[u]) >= CAP: continue
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
    return A

def census(A, N):
    nbrs = [np.flatnonzero(A[i]) for i in range(N)]
    edges = [(i, int(j)) for i in range(N) for j in nbrs[i] if j > i]
    E = len(edges); eidx = {e: k for k, e in enumerate(edges)}
    z = float(A.sum(1).mean())
    n3 = np.zeros(E, int); n4 = np.zeros(E, int)
    tri_masks = []; quad_masks = set()
    for k, (i, j) in enumerate(edges):
        Ni = set(int(v) for v in nbrs[i]); Nj = set(int(v) for v in nbrs[j])
        n3[k] = len((Ni & Nj) - {i, j})
        for x in Nj - {i}:
            for y in (set(int(v) for v in nbrs[x]) & Ni) - {i, j}:
                if x == y or A[i, x] or A[j, y]: continue
                n4[k] += 1
                m = (1 << eidx[(i, j)]) | (1 << eidx[(min(j, x), max(j, x))]) \
                    | (1 << eidx[(min(x, y), max(x, y))]) | (1 << eidx[(min(y, i), max(y, i))])
                quad_masks.add(m)
    for i in range(N):
        ni = [v for v in nbrs[i] if v > i]
        for a in range(len(ni)):
            for b in range(a+1, len(ni)):
                j, kk = int(ni[a]), int(ni[b])
                if A[j, kk]:
                    tri_masks.append((1 << eidx[(i, j)]) | (1 << eidx[(i, kk)])
                                     | (1 << eidx[(min(j, kk), max(j, kk))]))
    piv = {}
    def add(v):
        while v:
            b = v.bit_length() - 1
            if b in piv: v ^= piv[b]
            else: piv[b] = v; return 1
        return 0
    T = sum(add(v) for v in tri_masks)
    Q = sum(add(v) for v in sorted(quad_masks))
    return dict(z=z, E=E, T=T, Q=Q, n3=n3, n4=n4)

def scores(c, rq=0.86):
    dp, c3, c4, h = consts(rq)
    E = c['E']
    tot = 0.0
    for k in range(E):
        if c['n3'][k] >= 1: tot += h + (c['n3'][k]-1)*c3 + c['n4'][k]*c4
        elif c['n4'][k] >= 1: tot += h + (c['n4'][k]-1)*c4
    credR1 = tot/E
    credR2a = (c3*c['T'] + c4*c['Q'])/E   # dead rule, record only
    pref = min(c['z'], ZC)/2.0
    return pref*(dp+credR1), pref*(dp+credR2a)

# ensemble A: functional (seed 160811) — swing-16/17/19 construction verbatim
N = 256; L = (N/RHO) ** (1/3.0); STEP = 0.22
rng = np.random.default_rng(160811)
grid = np.array([[i, j, k] for i in range(7) for j in range(7) for k in range(7)], float) * (L/7)
sel = rng.permutation(343)[:N]
pos = grid[sel] + rng.uniform(-0.01, 0.01, (N, 3))
pos %= L
D2 = full_d2(pos, L)
core2 = CORE*CORE
def node_E_from_row(row):
    idx = np.argpartition(row, CAP)[:CAP]
    d = np.sqrt(row[idx]); dbar = d.mean()
    Lk = int(np.count_nonzero((d >= CORE) & (d <= REACH)))
    return -(DP0/2.0)*Lk + TAUB*(D0/dbar)**2, d.max()
Ecache = np.zeros(N); R5v = np.zeros(N)
def rebuild():
    for j in range(N):
        Ecache[j], R5v[j] = node_E_from_row(D2[j])
rebuild()
def row_to(p, i, pos, L):
    d = pos - p; d -= L * np.round(d / L)
    r = np.einsum('ij,ij->i', d, d); r[i] = 1e9
    return r
t0 = time.time()
for s in range(3000):
    T = 8.0 * (0.05/8.0) ** (s / 2999.0)
    order = rng.permutation(N); trials = rng.uniform(-STEP, STEP, (N, 3)); us = rng.random(N)
    for k in range(N):
        i = order[k]
        newp = (pos[i] + trials[k]) % L
        rnew = row_to(newp, i, pos, L)
        if rnew.min() < core2: continue
        r5sq = R5v * R5v + 1e-9
        J = np.flatnonzero((D2[i] <= r5sq) | (rnew <= r5sq))
        Eold = Ecache[i] + Ecache[J].sum()
        Ei_new, _ = node_E_from_row(rnew); Enew = Ei_new
        newE_J = []; newR_J = []
        for j in J:
            rowj = D2[j].copy(); rowj[i] = rnew[j]
            ej, rj = node_E_from_row(rowj); newE_J.append(ej); newR_J.append(rj); Enew += ej
        dE = Enew - Eold
        if dE <= 0 or (T > 1e-9 and math.exp(-dE/T) > us[k]):
            pos[i] = newp; D2[i, :] = rnew; D2[:, i] = rnew
            Ecache[i] = Ei_new
            R5v[i] = math.sqrt(node_E_from_row(rnew)[1])
            for m, j in enumerate(J):
                Ecache[j] = newE_J[m]; R5v[j] = math.sqrt(newR_J[m])
    if s % 100 == 0: rebuild()
print("functional anneal done (%.0fs)" % (time.time()-t0), flush=True)
cA = census(lock_graph(pos, L, N), N)
GA1, GA2a = scores(cA)
print("functional: z=%.3f | R1 G=%.2f (%+.1f%%) | [dead R2a would read %.2f]"
      % (cA['z'], GA1, 100*(GA1-BOOKS)/BOOKS, GA2a))
for rq in (0.84, 0.88):
    g1, _ = scores(cA, rq)
    print("  r_q=%.2f: R1 G=%.2f" % (rq, g1))

# ensemble B: liquid (seed 20260811)
N = 512; L = (N/RHO) ** (1/3.0)
rng = np.random.default_rng(20260811)
g = L/8.0
pos = np.array([[i, j, k] for i in range(8) for j in range(8) for k in range(8)], float)*g
pos += rng.uniform(-0.08, 0.08, pos.shape); pos %= L
def mc_sweep(pos, L, N):
    order = rng.permutation(N); trials = rng.uniform(-STEP, STEP, (N, 3))
    for idx in range(N):
        i = order[idx]
        new = (pos[i] + trials[idx]) % L
        d = pos - new; d -= L*np.round(d/L)
        d2 = np.einsum('ij,ij->i', d, d); d2[i] = 1e9
        if d2.min() >= core2: pos[i] = new
for s in range(1500): mc_sweep(pos, L, N)
cB = census(lock_graph(pos, L, N), N)
GB1, GB2a = scores(cB)
print("liquid: z=%.3f | R1 G=%.2f (%+.1f%%) | [dead R2a would read %.2f]"
      % (cB['z'], GB1, 100*(GB1-BOOKS)/BOOKS, GB2a))

print("\nS20b CROWN RESTATEMENT (unique rule R1): functional G=%.2f in [32,40]:" % GA1,
      "PASS" if WIN[0] <= GA1 <= WIN[1] else "FAIL")
print("S20c SEAM: suppression = 2/z_c = %.3f (sole reading); measured 0.360±0.064 -> %+.1fx"
      % (2/ZC, (0.360 - 2/ZC)/0.064))
print("S20d dead-rule values above, record only.")
