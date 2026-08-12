#!/usr/bin/env python3
# Swing 19 — the attribution seam: rule enumeration, cluster kill, rule-robust
# books. Registration: 5bcb14f (pre-run). Survivors R1/R2 applied unchanged to
# the swing-17 lock graphs (deterministic rebuilds).
import numpy as np, math, time

RHO = 0.138; CORE = 1.72; REACH = 2.14; ZC = 4.78; HB2M = 41.47
DP0 = 14.02; TAUB = 20.1; BOOKS = 35.85; WIN = (32.0, 40.0); CAP = 5
D0 = RHO ** (-1.0/3.0)

def consts(rq):
    dp = HB2M/(4*rq*rq); c3 = HB2M*0.75/(18*rq*rq); c4 = HB2M*0.5/(32*rq*rq)
    return dp, c3, c4, 2*c3/ZC

# ---------------- Part 1: cluster kill table ----------------
dp, c3, c4, h = consts(0.86)
print("SWING 19 — constants (central): dp=%.3f c3=%.3f c4=%.3f h=2c3/z_c=%.3f" % (dp, c3, c4, h))
T_MEAS, T_BAND = 0.84, 0.15
A_MEAS, A_BAND = 3.39, 0.20
rules = {
    # (t_step, a_step) per rule on triangle graph / K4
    "R1 first-suppressed": (h, h + c3),
    "R2 independent-mean": (c3/3.0, 1.5*c3),
    "R3 indep+blanket-h":  (c3/3.0 + h, 1.5*c3 + h),
    "R4 h-per-loop":       (h/3.0, 3*h/6.0*3.0/3.0),  # 3 basis loops x h over 6 bonds -> per-bond h/2? see note
    "R5 raw-full":         (c3, 2*c3),
}
# R4 exact: trinucleon: 1 loop x h over 3 bonds = h/3; K4: 3 basis loops x h,
# each loop over its 3 bonds -> total 3h, per bond 3h/6 = h/2.
rules["R4 h-per-loop"] = (h/3.0, h/2.0)
print("\nCLUSTER KILL TABLE (bands: t %.2f±%.2f, alpha %.2f±%.2f; kill >4x or chi2>9)" % (T_MEAS, T_BAND, A_MEAS, A_BAND))
survivors = []
for name, (ts, as_) in rules.items():
    rt = (ts - T_MEAS)/T_BAND; ra = (as_ - A_MEAS)/A_BAND
    chi2 = rt*rt + ra*ra
    dead = abs(rt) > 4 or abs(ra) > 4 or chi2 > 9
    print("  %-22s t=%.3f (%+.1fx)  a=%.3f (%+.1fx)  chi2=%.2f  -> %s"
          % (name, ts, rt, as_, ra, chi2, "DEAD" if dead else "SURVIVES"))
    if not dead: survivors.append(name)
print("Survivors:", ", ".join(survivors))
print("Seam: suppression factor measured %.3f ± %.3f; candidates 1/3=%.3f (R2), 2/z_c=%.3f (R1) — both inside"
      % (T_MEAS/c3, T_BAND/c3, 1/3.0, 2/ZC))

# ---------------- shared: lock graph (swing-17 rule) + censuses ----------------
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

def census_all(A, N):
    """Rule C ranks (T,Q) + per-bond raw counts n3, n4(chordless)."""
    nbrs = [np.flatnonzero(A[i]) for i in range(N)]
    edges = [(i, int(j)) for i in range(N) for j in nbrs[i] if j > i]
    E = len(edges); eidx = {e: k for k, e in enumerate(edges)}
    z = float(A.sum(1).mean())
    n3 = np.zeros(E, int); n4 = np.zeros(E, int)
    tri_masks = []
    quad_masks = set()
    for k, (i, j) in enumerate(edges):
        Ni = set(int(v) for v in nbrs[i]); Nj = set(int(v) for v in nbrs[j])
        common = (Ni & Nj) - {i, j}
        n3[k] = len(common)
        cnt4 = 0
        for x in Nj - {i}:
            for y in (set(int(v) for v in nbrs[x]) & Ni) - {i, j}:
                if x == y or A[i, x] or A[j, y]: continue
                cnt4 += 1
                m = (1 << eidx[(i, j)]) | (1 << eidx[(min(j, x), max(j, x))]) \
                    | (1 << eidx[(min(x, y), max(x, y))]) | (1 << eidx[(min(y, i), max(y, i))])
                quad_masks.add(m)
        n4[k] = cnt4
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
    raw_tri = len(tri_masks); raw_quad = len(quad_masks)
    return dict(z=z, E=E, T=T, Q=Q, raw_tri=raw_tri, raw_quad=raw_quad, n3=n3, n4=n4)

def bulk_scores(c, rq=0.86):
    dp, c3, c4, h = consts(rq)
    E = c['E']; n3, n4 = c['n3'], c['n4']
    # R2
    credR2 = (c3*c['T'] + c4*c['Q'])/E
    # R1 per-bond
    tot = 0.0
    nb_first = 0
    for k in range(E):
        if n3[k] >= 1:
            tot += h + (n3[k]-1)*c3 + n4[k]*c4; nb_first += 1
        elif n4[k] >= 1:
            tot += h + (n4[k]-1)*c4; nb_first += 1
    credR1 = tot/E
    pref = min(c['z'], ZC)/2.0
    return dict(G1=pref*(dp+credR1), G2=pref*(dp+credR2),
                g1=dp+credR1, g2=dp+credR2, fb=nb_first/E,
                infl_t=c['raw_tri']/max(1, c['T']), infl_q=c['raw_quad']/max(1, c['Q']))

# ---------------- ensemble A: functional (swing-16/17 rebuild, seed 160811) ----------------
print("\nENSEMBLE A: functional (seed 160811)")
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
    d = np.sqrt(row[idx])
    dbar = d.mean()
    Lk = int(np.count_nonzero((d >= CORE) & (d <= REACH)))
    return -(DP0/2.0)*Lk + TAUB*(D0/dbar)**2, d.max()

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
SWEEPS = 3000
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
        r5sq = R5 * R5 + 1e-9
        J = np.flatnonzero((D2[i] <= r5sq) | (rnew <= r5sq))
        Eold = Ecache[i] + Ecache[J].sum()
        Ei_new, r5i = node_E_from_row(rnew)
        Enew = Ei_new
        newE_J = []; newR_J = []
        for j in J:
            rowj = D2[j].copy(); rowj[i] = rnew[j]
            ej, rj = node_E_from_row(rowj)
            newE_J.append(ej); newR_J.append(rj); Enew += ej
        dE = Enew - Eold
        if dE <= 0 or (T > 1e-9 and math.exp(-dE/T) > us[k]):
            pos[i] = newp
            D2[i, :] = rnew; D2[:, i] = rnew
            Ecache[i] = Ei_new
            R5[i] = math.sqrt(node_E_from_row(rnew)[1])
            for m, j in enumerate(J):
                Ecache[j] = newE_J[m]; R5[j] = math.sqrt(newR_J[m])
    if s % 100 == 0:
        rebuild()
print("  anneal done (%.0fs) E/N=%.3f" % (time.time()-t0, Ecache.mean()), flush=True)
A = lock_graph(pos, L, N)
cA = census_all(A, N)
sA = bulk_scores(cA)
print("  z=%.3f E=%d T=%d(raw %d) Q=%d(raw %d) infl %.2f/%.2f fb=%.2f"
      % (cA['z'], cA['E'], cA['T'], cA['raw_tri'], cA['Q'], cA['raw_quad'], sA['infl_t'], sA['infl_q'], sA['fb']))
print("  R1: gross=%.2f G=%.2f | R2: gross=%.2f G=%.2f" % (sA['g1'], sA['G1'], sA['g2'], sA['G2']))

# ---------------- ensemble B: liquid (swing-12/17 rebuild, seed 20260811) ----------------
print("\nENSEMBLE B: liquid (seed 20260811)")
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

for s in range(1500):
    mc_sweep(pos, L, N)
A = lock_graph(pos, L, N)
cB = census_all(A, N)
sB = bulk_scores(cB)
print("  z=%.3f E=%d T=%d(raw %d) Q=%d(raw %d) infl %.2f/%.2f fb=%.2f"
      % (cB['z'], cB['E'], cB['T'], cB['raw_tri'], cB['Q'], cB['raw_quad'], sB['infl_t'], sB['infl_q'], sB['fb']))
print("  R1: gross=%.2f G=%.2f | R2: gross=%.2f G=%.2f" % (sB['g1'], sB['G1'], sB['g2'], sB['G2']))

# ---------------- gates ----------------
print("\n---- GATES ----")
print("S19a kill table: R3/R4/R5 dead, R1/R2 survive:", "AS REGISTERED" if survivors == ["R1 first-suppressed", "R2 independent-mean"] else "DEVIATION — check")
taintR1 = sA['infl_t'] > 1.5 or sA['infl_q'] > 1.5
ok1 = WIN[0] <= sA['G1'] <= WIN[1]; ok2 = WIN[0] <= sA['G2'] <= WIN[1]
print("S19d raw-vs-rank inflation (functional): tri %.2f quad %.2f ->" % (sA['infl_t'], sA['infl_q']),
      "R1 TAINTED (verdict falls to R2-only)" if taintR1 else "R1 clean")
print("S19b THE FENCE (functional, central): R1 G=%.2f %s | R2 G=%.2f %s"
      % (sA['G1'], "IN" if ok1 else "OUT", sA['G2'], "IN" if ok2 else "OUT"))
if ok1 and ok2 and not taintR1:
    print("  ==> PASS — THE CROWN BOOKS ARE TAKEN (rule-robust grade)")
elif ok2 and (taintR1):
    print("  ==> R2-only grade (R1 tainted) — crown at reduced grade, booked")
else:
    print("  ==> FAIL — crown NOT taken, booked")
print("S19c spread (functional): R1-R2 = %.2f MeV (%.1f%% of C); liquid R1 %.2f / R2 %.2f"
      % (sA['G1']-sA['G2'], 100*(sA['G1']-sA['G2'])/BOOKS, sB['G1'], sB['G2']))
for rq in (0.84, 0.88):
    a = bulk_scores(cA, rq)
    print("  r_q=%.2f functional: R1 %.2f | R2 %.2f" % (rq, a['G1'], a['G2']))
print("  central precision vs C=35.85: R1 %+.1f%% | R2 %+.1f%%"
      % (100*(sA['G1']-BOOKS)/BOOKS, 100*(sA['G2']-BOOKS)/BOOKS))
