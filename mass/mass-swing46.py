#!/usr/bin/env python3
# Swing 46 — THE SLOT CENSUS: seats, not sites. Registration: 6fe139f (pre-run).
# Rebuild swing-45 families exactly (deterministic); n_f = sum(5 - deg_lock);
# bracket via degree-bounded optimum; gates on bracket centers.
import numpy as np, math, time

RHO = 0.138; CORE = 1.72; REACH = 2.14
DP = 14.02; TAUB = 20.1; DCELL = 6.51
D0 = RHO ** (-1.0/3.0)
SIZES = [20, 30, 40, 60, 90, 130, 180, 220]
SEEDS = [160812, 260812, 360812]
SWEEPS = 2200; STEP = 0.22; CAP = 5
core2, reach2 = CORE*CORE, REACH*REACH

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
        if np.dot(p, p) <= R_drop*R_drop:
            pos = np.vstack([pos, p])
    A = len(pos)
    def node_E(row):
        k = min(CAP, A-1)
        idx = np.argpartition(row, k)[:k]
        d = np.sqrt(row[idx])
        dbar = d.mean()
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

def lock_and_slots(D2, A, rng):
    edges = [(D2[i, j], i, j) for i in range(A) for j in range(i+1, A)
             if core2 <= D2[i, j] <= reach2]
    avail = np.zeros(A, int)
    for w, i, j in edges: avail[i] += 1; avail[j] += 1
    best = None
    orders = [sorted(edges)]
    for _ in range(2):
        e2 = edges[:]; rng.shuffle(e2); orders.append(e2)
    for elist in orders:
        deg = np.zeros(A, int); used = []
        for w, i, j in elist:
            if deg[i] < CAP and deg[j] < CAP:
                deg[i] += 1; deg[j] += 1; used.append((i, j))
        for w, i, j in sorted(edges):
            if deg[i] < CAP and deg[j] < CAP and (i, j) not in used:
                deg[i] += 1; deg[j] += 1; used.append((i, j))
        if best is None or len(used) > len(best[1]):
            best = (deg, used)
    deg, used = best
    opt_ub = min(len(edges), int(np.minimum(avail, CAP).sum()) // 2)
    slots_ach = float((CAP - deg).sum()) / A
    slots_lb = float(CAP - 2*opt_ub/A)
    return slots_ach, slots_lb, len(used), opt_ub, float(deg.mean())

res = {}
t0 = time.time()
for seed in SEEDS:
    for A0 in SIZES:
        rng = np.random.default_rng(seed + A0)
        pos, D2, A = anneal(A0, rng)
        s_ach, s_lb, ne, ub, zb = lock_and_slots(D2, A, rng)
        center = 0.5*(s_ach + s_lb)
        res[(A0, seed)] = dict(ach=s_ach, lb=s_lb, c=center, z=zb)
        print("seed %d A=%3d: z=%.3f slots/A achieved %.3f | LB %.3f | center %.3f (edges %d/ub %d) [%.0fs]"
              % (seed, A0, zb, s_ach, s_lb, center, ne, ub, time.time()-t0), flush=True)

def m3(A0, k): return float(np.mean([res[(A0, s)][k] for s in SEEDS]))
heavy = [130, 180, 220]; light = [20, 30, 40]
c_h = float(np.mean([m3(a, 'c') for a in heavy]))
a_h = float(np.mean([m3(a, 'ach') for a in heavy]))
l_h = float(np.mean([m3(a, 'lb') for a in heavy]))
c_l = float(np.mean([m3(a, 'c') for a in light]))
sprd = max(max(res[(a, s)]['c'] for s in SEEDS) - min(res[(a, s)]['c'] for s in SEEDS) for a in heavy)
centers_by_A = [m3(a, 'c') for a in SIZES]

print("\nHEAVY: achieved %.3f | LB %.3f | bracket center %.3f (width %.3f)" % (a_h, l_h, c_h, a_h-l_h))
ok_a = abs(c_h - 0.331)/0.331 <= 0.15
print("S46a heavy center within 15%% of 0.331: %s (%.3f, %+.1f%%)" %
      ("PASS" if ok_a else "FAIL", c_h, 100*(c_h-0.331)/0.331))
ok_b = abs(c_l - 0.65)/0.65 <= 0.20
print("S46b light center within 20%% of 0.65: %s (%.3f, %+.1f%%)" %
      ("PASS" if ok_b else "FAIL", c_l, 100*(c_l-0.65)/0.65))
mono = all(centers_by_A[i+1] <= centers_by_A[i] + 0.02 for i in range(len(centers_by_A)-1))
sat = abs(centers_by_A[-1] - centers_by_A[-3]) < 0.05
print("S46c shape: centers %s | decreasing %s saturating %s -> %s" %
      (np.round(centers_by_A, 3), mono, sat, "PASS" if (mono and sat) else "FAIL"))
print("S46d heavy center seed spread %.3f < 0.08:" % sprd, "PASS" if sprd < 0.08 else "FAIL")
comp = DCELL/math.sqrt(c_h)
print("S46e composed report: delta_cell/sqrt(phi) = %.3f/sqrt(%.3f) = %.2f vs measured 10.55 (%+.1f%%) [hand 11.05]"
      % (DCELL, c_h, comp, 100*(comp-10.55)/10.55))
print("\n1/3 note: center %.3f — not 1/3, no conversion sought (inoculation intact)" % c_h)
