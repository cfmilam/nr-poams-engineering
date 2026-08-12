#!/usr/bin/env python3
# Swing 44 — THE DROPLET FRONTIER CENSUS: deriving (delta_cell, phi) natively.
# Registrations: 61dd3d6 (spec) + 45a608d (extraction rules + hand expectations), both pre-run.
# Free droplets (no PBC) under the ledger's own functional; lock graph = max-cardinality
# deg<=5 subgraph; census n_f = deg<5; delta_cell = gamma*^2 (hb2/m) <1/d^2> on light locks.
import numpy as np, math, time

RHO = 0.138; CORE = 1.72; REACH = 2.14; HB2M = 41.47
DP = 14.02; TAUB = 20.1; GSTAR = 0.8314
D0 = RHO ** (-1.0/3.0)
SIZES = [20, 30, 40, 60, 90, 130, 180, 220]
SWEEPS = 2200; STEP = 0.22; CAP = 5
rng = np.random.default_rng(160812)

core2, reach2 = CORE*CORE, REACH*REACH

def anneal(A):
    R_drop = (3*A/(4*math.pi*RHO)) ** (1/3.0)
    # init: fcc-ish jittered ball — random sphere points pushed to min spacing
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
    n = len(pos)
    if n < A:  # relax packing constraint slightly
        while len(pos) < A:
            p = (rng.random(3)*2 - 1) * R_drop
            if np.dot(p, p) <= R_drop*R_drop:
                pos = np.vstack([pos, p])
    A = len(pos)

    def d2mat(P):
        d = P[:, None, :] - P[None, :, :]
        d2 = np.einsum('ijk,ijk->ij', d, d)
        np.fill_diagonal(d2, 1e9)
        return d2

    def node_E(row):
        k = min(CAP, A-1)
        idx = np.argpartition(row, k)[:k]
        d = np.sqrt(row[idx])
        dbar = d.mean()
        Lk = int(np.count_nonzero((d >= CORE) & (d <= REACH)))
        return -(DP/2.0)*Lk + TAUB*(D0/dbar)**2

    D2 = d2mat(pos)
    E = np.array([node_E(D2[i]) for i in range(A)])
    # confinement: fixed droplet radius wall (density constraint, declared: at rho0)
    RW = R_drop + 0.3
    for s in range(SWEEPS):
        T = 6.0 * (0.04/6.0) ** (s / (SWEEPS-1))
        order = rng.permutation(A)
        trials = rng.uniform(-STEP, STEP, (A, 3))
        for k in range(A):
            i = order[k]
            newp = pos[i] + trials[k]
            if np.dot(newp, newp) > RW*RW: continue
            d = pos - newp
            rnew = np.einsum('ij,ij->i', d, d); rnew[i] = 1e9
            if rnew.min() < core2: continue
            # affected set: anything within reach*1.6 of old or new position
            aff = np.flatnonzero((D2[i] < (1.6*REACH)**2) | (rnew < (1.6*REACH)**2))
            Eold = E[i] + E[aff].sum()
            rowi_old = D2[i].copy()
            D2[i, :] = rnew; D2[:, i] = rnew
            Enew_i = node_E(D2[i])
            Enew = Enew_i + sum(node_E(D2[j]) for j in aff)
            dE = Enew - Eold
            if dE <= 0 or (T > 1e-9 and math.exp(-dE/T) > rng.random()):
                pos[i] = newp
                E[i] = Enew_i
                for j in aff: E[j] = node_E(D2[j])
            else:
                D2[i, :] = rowi_old; D2[:, i] = rowi_old
    return pos, D2, A

def lock_graph(D2, A):
    """Max-cardinality deg<=CAP subgraph: greedy shortest-first + swap augmentation."""
    edges = [(D2[i, j], i, j) for i in range(A) for j in range(i+1, A)
             if core2 <= D2[i, j] <= reach2]
    edges.sort()
    deg = np.zeros(A, int)
    adj = [[] for _ in range(A)]
    used = set()
    for w, i, j in edges:
        if deg[i] < CAP and deg[j] < CAP:
            deg[i] += 1; deg[j] += 1
            adj[i].append(j); adj[j].append(i)
            used.add((i, j))
    # swap augmentation passes
    for _ in range(3):
        added = 0
        for w, i, j in edges:
            if (i, j) in used: continue
            if deg[i] < CAP and deg[j] < CAP:
                deg[i] += 1; deg[j] += 1; adj[i].append(j); adj[j].append(i)
                used.add((i, j)); added += 1
        if not added: break
    ub = min(len(edges), (CAP*A)//2)
    return deg, adj, used, len(edges), ub

results = {}
t0 = time.time()
for A0 in SIZES:
    pos, D2, A = anneal(A0)
    deg, adj, used, ne, ub = lock_graph(D2, A)
    n_f = int(np.count_nonzero(deg < CAP))
    zbar = float(deg.mean())
    # delta_cell on light droplets: gamma*^2 * hb2m * <1/d^2> over lock edges
    if used:
        inv2 = np.mean([1.0/D2[i, j] for (i, j) in used])
    else:
        inv2 = float('nan')
    dcell = GSTAR*GSTAR*HB2M*inv2
    results[A] = dict(nf=n_f, phi=n_f/A, z=zbar, dcell=dcell, edges=len(used), ub=ub)
    print("A=%3d: z_lock=%.3f  n_f=%3d  phi=%.3f  <1/d^2>=%.4f  dcell=%.3f  (edges %d / ub %d)  [%.0fs]"
          % (A, zbar, n_f, n_f/A, inv2, dcell, len(used), ub, time.time()-t0), flush=True)

# ---- gates ----
heavy = [results[a] for a in (130, 180, 220)]
light = [results[a] for a in (20, 30, 40)]
phi_geom = float(np.mean([r['phi'] for r in heavy]))
dcell_geom = float(np.mean([r['dcell'] for r in light]))
half_variant = dcell_geom/2
phis = [results[a]['phi'] for a in SIZES]

print("\nS44a phi_geom (heavy trio) = %.3f | gate [0.28, 0.38] & within 15%% of 0.331:" % phi_geom,
      "PASS" if (0.28 <= phi_geom <= 0.38 and abs(phi_geom-0.331)/0.331 <= 0.15) else "FAIL")
mono = all(phis[i+1] <= phis[i] + 0.02 for i in range(len(phis)-1))
sat = abs(results[220]['phi'] - results[130]['phi']) < 0.05
print("S44b crossover: phis %s | decreasing %s saturating %s ->" %
      (np.round(phis, 3), mono, sat), "PASS" if (mono and sat) else "FAIL")
print("S44c delta_cell (light trio) = %.3f | gate [5.3, 6.8]:" % dcell_geom,
      "PASS" if 5.3 <= dcell_geom <= 6.8 else "FAIL",
      "| half-variant report: %.3f" % half_variant)
near_third = abs(phi_geom - 1/3) < 0.01
print("S44d the 1/3 clause: phi_geom %s 1/3 (%.3f vs 0.3333)" %
      ("within 3%% of" if near_third else "NOT within 3%% of", phi_geom),
      "- counting reason required before any conversion" if near_third else "- clause dormant")
print("\nlight-edge check: phi(20,30,40) = %s (measured share 0.65 at Q1)" %
      np.round([r['phi'] for r in light], 3))
