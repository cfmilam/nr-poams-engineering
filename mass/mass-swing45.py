#!/usr/bin/env python3
# Swing 45 — THE ORIENTATION CELL CENSUS. Registration: 43dea7e (pre-run).
# 3 seeds x 8 sizes; four-channel T=0 assignment on lock graphs; primary census =
# {deg<5} U {zero-mode at deg 5}; refined weak-slot census reported unclaimed.
import numpy as np, math, time

RHO = 0.138; CORE = 1.72; REACH = 2.14; HB2M = 41.47
DP = 14.02; TAUB = 20.1; GSTAR = 0.8314
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
    d = pos[:, None, :] - pos[None, :, :]
    D2 = np.einsum('ijk,ijk->ij', d, d); np.fill_diagonal(D2, 1e9)
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
            dd = pos - newp
            rnew = np.einsum('ij,ij->i', dd, dd); rnew[i] = 1e9
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

def lock_graph(D2, A, rng):
    edges = [(D2[i, j], i, j) for i in range(A) for j in range(i+1, A)
             if core2 <= D2[i, j] <= reach2]
    best = None
    orders = [sorted(edges)]
    for _ in range(2):
        e2 = edges[:]; rng.shuffle(e2); orders.append(e2)
    for elist in orders:
        deg = np.zeros(A, int); adj = [[] for _ in range(A)]; used = []
        for w, i, j in elist:
            if deg[i] < CAP and deg[j] < CAP:
                deg[i] += 1; deg[j] += 1
                adj[i].append(j); adj[j].append(i); used.append((i, j))
        # augmentation pass on the sorted remainder
        for w, i, j in sorted(edges):
            if (i, j) in used or (j, i) in used: continue
            if deg[i] < CAP and deg[j] < CAP:
                deg[i] += 1; deg[j] += 1
                adj[i].append(j); adj[j].append(i); used.append((i, j))
        if best is None or len(used) > len(best[2]):
            best = (deg, adj, used)
    deg, adj, used = best
    ub = min(len(edges), (CAP*A)//2)
    return deg, adj, used, len(edges), ub

def orient_assign(A, adj, used, rng):
    """Four-channel T=0: sense fixed-count balanced, orientation free.
    weights: unlike-parallel 1; antiparallel gamma*; like-parallel 0."""
    sense = np.array([1]*(A//2) + [0]*(A - A//2)); rng.shuffle(sense)
    orient = rng.integers(0, 2, A)
    def W_edge(i, j):
        if orient[i] != orient[j]: return GSTAR
        return 1.0 if sense[i] != sense[j] else 0.0
    def node_W(i):
        return sum(W_edge(i, j) for j in adj[i])
    # anneal: orientation flips + sense swaps
    for s in range(4000):
        T = 1.0 * (0.005) ** (s/3999)
        # orientation flip
        i = rng.integers(0, A)
        w0 = node_W(i); orient[i] ^= 1; w1 = node_W(i)
        dW = w1 - w0
        if dW < 0 and (T < 1e-9 or math.exp(dW/T) < rng.random()):
            orient[i] ^= 1
        # sense swap (preserve counts)
        i, j = rng.integers(0, A), rng.integers(0, A)
        if sense[i] != sense[j]:
            w0 = node_W(i) + node_W(j) - (W_edge(i, j) if j in adj[i] else 0)
            sense[i], sense[j] = sense[j], sense[i]
            w1 = node_W(i) + node_W(j) - (W_edge(i, j) if j in adj[i] else 0)
            dW = w1 - w0
            if dW < 0 and (T < 1e-9 or math.exp(dW/T) < rng.random()):
                sense[i], sense[j] = sense[j], sense[i]
    Wtot = sum(W_edge(i, j) for (i, j) in used)
    # zero-cost polish: greedy accept any non-negative flip until none improves
    for _ in range(3):
        moved = 0
        for i in range(A):
            w0 = node_W(i); orient[i] ^= 1; w1 = node_W(i)
            if w1 > w0 + 1e-12: moved += 1
            else: orient[i] ^= 1
        if not moved: break
    Wtot = sum(W_edge(i, j) for (i, j) in used)
    return sense, orient, Wtot, W_edge, node_W

def census(A, deg, adj, sense, orient, node_W, W_edge):
    geo = set(np.flatnonzero(deg < CAP))
    zero_all = set(); weak_slot = set()
    for i in range(A):
        if deg[i] < CAP: continue
        w0 = node_W(i); orient[i] ^= 1; w1 = node_W(i)
        if abs(w1 - w0) < 1e-9:
            zero_all.add(i)
            # refined: does the flipped state hold an antiparallel slot to a like-sense neighbor?
            if any(orient[i] != orient[j] and sense[i] == sense[j] for j in adj[i]):
                weak_slot.add(i)
        orient[i] ^= 1
    return geo, zero_all, weak_slot

res = {}   # (A,seed) -> dict
t0 = time.time()
for seed in SEEDS:
    for A0 in SIZES:
        rng = np.random.default_rng(seed + A0)
        pos, D2, A = anneal(A0, rng)
        deg, adj, used, ne, ub = lock_graph(D2, A, rng)
        sense, orient, Wt, W_edge, node_W = orient_assign(A, adj, used, rng)
        geo, zm, ws = census(A, deg, adj, sense, orient, node_W, W_edge)
        union = geo | zm; refined = geo | ws
        res[(A0, seed)] = dict(A=A, geo=len(geo)/A, uni=len(union)/A,
                               ref=len(refined)/A, zm=len(zm)/A, gap=1-len(used)/ub)
        print("seed %d A=%3d: geo %.3f  zero-mode(deg5) %.3f  UNION %.3f  refined %.3f  (gap %.2f)  [%.0fs]"
              % (seed, A0, len(geo)/A, len(zm)/A, len(union)/A, len(refined)/A,
                 1-len(used)/ub, time.time()-t0), flush=True)

def mean3(A0, key):
    return float(np.mean([res[(A0, s)][key] for s in SEEDS]))
def spread3(A0, key):
    v = [res[(A0, s)][key] for s in SEEDS]
    return max(v) - min(v)

heavy = [130, 180, 220]; light = [20, 30, 40]
uni_h = float(np.mean([mean3(a, 'uni') for a in heavy]))
geo_h = float(np.mean([mean3(a, 'geo') for a in heavy]))
ref_h = float(np.mean([mean3(a, 'ref') for a in heavy]))
inc = uni_h - geo_h
uni_l = float(np.mean([mean3(a, 'uni') for a in light]))
geo_l = float(np.mean([mean3(a, 'geo') for a in light]))
spr = max(spread3(a, 'uni') for a in heavy)

print("\n3-SEED MEANS (heavy trio): geometric %.3f | UNION %.3f | refined %.3f | increment %.3f" %
      (geo_h, uni_h, ref_h, inc))
ok_a = 0.28 <= uni_h <= 0.38 and abs(uni_h - 0.331)/0.331 <= 0.15
print("S45a UNION in [0.28,0.38] & +-15%% of 0.331: %s (%.3f, %+.1f%% vs measured)"
      % ("PASS" if ok_a else "FAIL", uni_h, 100*(uni_h-0.331)/0.331))
ok_b = 0.02 <= inc <= 0.12
print("S45b increment in [0.02,0.12]:", "PASS (%.3f)" % inc if ok_b else "FAIL (%.3f)" % inc)
ok_c = uni_l > geo_l
print("S45c light-edge sign: union %.3f > geometric %.3f ->" % (uni_l, geo_l),
      "PASS" if ok_c else "FAIL", "(measured Q1 share 0.65)")
means_by_A = [float(np.mean([res[(a, s)]['uni'] for s in SEEDS])) for a in SIZES]
mono = all(means_by_A[i+1] <= means_by_A[i] + 0.02 for i in range(len(means_by_A)-1))
sat = abs(means_by_A[-1] - means_by_A[-3]) < 0.05
print("S45d seed spread (max heavy) %.3f < 0.06:" % spr, "PASS" if spr < 0.06 else "FAIL",
      "| 3-seed monotone %s saturating %s (report)" % (mono, sat))
print("    union means by A: %s" % np.round(means_by_A, 3))
near = abs(uni_h - 1/3) < 0.01
print("S45e 1/3 clause:", "within 3%% (%.3f) — counting reason required" % uni_h if near
      else "dormant (%.3f)" % uni_h)
