#!/usr/bin/env python3
# Swing 16 Part B — THE EMERGENCE INSTRUMENT. Registration: ledger 16e4949 (pre-run).
# Does z -> z_c emerge under the ledger's OWN terms? E_i = -(dp/2)*L_i + tau_b*(d0/dbar_i)^2
# cage = 5 nearest; L_i = cage members in [core, reach]. Anneal at rho0, exact dE.
import numpy as np, math, time

RHO = 0.138; CORE = 1.72; REACH = 2.14; ZC = 4.78; HB2M = 41.47
DP = 14.02; TAUB = 20.1; H = 0.84; BOOKS = 35.85; WIN = (32.0, 40.0)
D0 = RHO ** (-1.0/3.0)
N = 256; L = (N/RHO) ** (1/3.0)
SWEEPS = 3000; STEP = 0.22; CAP = 5
rng = np.random.default_rng(160811)

print("N=%d L=%.3f fm d0=%.4f fm  (grid init spacing %.4f)" % (N, L, D0, L/7))

# init: 7^3 grid, choose 256 sites (spacing 1.754 > core), tiny jitter
grid = np.array([[i, j, k] for i in range(7) for j in range(7) for k in range(7)], float) * (L/7)
sel = rng.permutation(343)[:N]
pos = grid[sel] + rng.uniform(-0.01, 0.01, (N, 3))
pos %= L

def full_d2(pos):
    d = pos[:, None, :] - pos[None, :, :]
    d -= L * np.round(d / L)
    d2 = np.einsum('ijk,ijk->ij', d, d)
    np.fill_diagonal(d2, 1e9)
    return d2

D2 = full_d2(pos)
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

def row_to(p, i):
    d = pos - p
    d -= L * np.round(d / L)
    r = np.einsum('ij,ij->i', d, d)
    r[i] = 1e9
    return r

t0 = time.time(); acc = 0; tot = 0
for s in range(SWEEPS):
    T = 8.0 * (0.05/8.0) ** (s / (SWEEPS - 1))
    order = rng.permutation(N)
    trials = rng.uniform(-STEP, STEP, (N, 3))
    us = rng.random(N)
    for k in range(N):
        i = order[k]; tot += 1
        newp = (pos[i] + trials[k]) % L
        rnew = row_to(newp, i)
        if rnew.min() < core2: continue
        rold = D2[i]
        # affected: i plus nodes whose cage could change
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
            acc += 1
    if s % 100 == 0:
        rebuild()  # kill drift
        if s % 250 == 0:
            print("  sweep %d T=%.3f acc=%.2f E/N=%.3f (%.0fs)"
                  % (s, T, acc/max(1, tot), Ecache.mean(), time.time()-t0), flush=True)

print("anneal done (%.0fs), final E/N = %.3f" % (time.time()-t0, Ecache.mean()), flush=True)

# ---------- lock graph (strict mutual cap-5 in reach) + Rule C census ----------
def capped_adj(pos):
    d2 = full_d2(pos)
    inreach = d2 <= reach2
    keep = np.zeros((N, N), bool)
    for i in range(N):
        cand = np.flatnonzero(inreach[i])
        if len(cand) > CAP:
            cand = cand[np.argsort(d2[i][cand])[:CAP]]
        keep[i, cand] = True
    return keep & keep.T

def rulec_census(A):
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
    return dict(z=z, E=E, ncomp=ncomp, beta1=beta1, T=T_, Q=Q_, R=beta1-T_-Q_,
                f=f, ntri=len(tri), nquad=len(quads))

snaps = []
for snap in range(3):
    if snap:
        for s in range(100):
            order = rng.permutation(N); trials = rng.uniform(-STEP, STEP, (N, 3))
            for k in range(N):
                i = order[k]
                newp = (pos[i] + trials[k]) % L
                rnew = row_to(newp, i)
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
    c = rulec_census(capped_adj(pos))
    print("snap %d: z_lock=%.3f E=%d beta1=%d T=%d Q=%d R=%d f=%.3f (tri=%d quad=%d)"
          % (snap, c['z'], c['E'], c['beta1'], c['T'], c['Q'], c['R'], c['f'], c['ntri'], c['nquad']), flush=True)
    snaps.append(c)

zbar = float(np.mean([c['z'] for c in snaps]))
Em = float(np.mean([c['E'] for c in snaps]))
Tm = float(np.mean([c['T'] for c in snaps])); Qm = float(np.mean([c['Q'] for c in snaps]))
Rm = float(np.mean([c['R'] for c in snaps])); fm = float(np.mean([c['f'] for c in snaps]))
print("\nMEANS: z_lock=%.3f E=%.0f T=%.1f Q=%.1f R=%.1f f=%.3f beta1/E=%.3f"
      % (zbar, Em, Tm, Qm, Rm, fm, float(np.mean([c['beta1']/c['E'] for c in snaps]))))

print("\nS16a THE EMERGENCE GATE: z_lock = %.3f in [4.3, 5.3]:" % zbar,
      "PASS — capacity coordination EMERGES" if 4.3 <= zbar <= 5.3 else "FAIL — booked as the wall")
res = {}
for rq in (0.84, 0.86, 0.88):
    dp = HB2M/(4*rq*rq); c3 = HB2M*0.75/(18*rq*rq); c4 = HB2M*0.5/(32*rq*rq)
    cred0 = (c3*Tm + c4*Qm)/Em
    g_h0 = dp + cred0; g_h1 = dp + cred0 + H*fm
    pref = min(zbar, ZC)/2.0
    res[rq] = (pref*g_h0, pref*g_h1, g_h0, g_h1)
    print("r_q=%.2f: gross_h0=%.2f gross_h1=%.2f | G_h0=%.2f G_h1=%.2f"
          % (rq, g_h0, g_h1, pref*g_h0, pref*g_h1))
g0, g1, gr0, gr1 = res[0.86]
print("\nS16b gross gate (central r_q): h0=%.2f h1=%.2f in [13.98, 16.19]:" % (gr0, gr1),
      "PASS" if (13.98 <= gr0 <= 16.19 and 13.98 <= gr1 <= 16.19) else "FAIL")
allin = all(WIN[0] <= v <= WIN[1] for r in res.values() for v in r[:2])
print("S16c THE LANDING (books): all G in [32,40]:",
      "PASS — CROWN BOOKS CLOSE (emergent)" if allin else "FAIL")
print("  central: G_h0=%.2f (%+.1f%% vs C)  G_h1=%.2f (%+.1f%%)"
      % (g0, 100*(g0-BOOKS)/BOOKS, g1, 100*(g1-BOOKS)/BOOKS))
print("S16d census composition reported above.")
