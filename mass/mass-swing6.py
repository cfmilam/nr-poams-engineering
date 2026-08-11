#!/usr/bin/env python3
# Swing 6 — T-C6: cluster ladder A=2-6. Registration: ledger 5ff4541 (pre-run).
# Channel-weighted strong-bond extraction; enhancement sign; cell-closure direction.
import re, itertools, statistics, math

HBAR2_M = 41.47          # MeV fm^2 (named import)
GAMMA = (0.80, 0.85, 0.90)  # weak/strong gross ratio band (swing 5)
AC = 0.72                # curve-free strain coefficient convention

# ---- AME2020 (local file, experimental only) ----
F = "data/mass.mas20.txt"
BA = {}
for ln in open(F, encoding="ascii", errors="replace"):
    if len(ln) < 70: continue
    try: N = int(ln[4:9]); Z = int(ln[9:14]); A = int(ln[14:19])
    except ValueError: continue
    if A != N + Z: continue
    fld = ln[54:68]
    if "#" in fld: continue
    m = re.search(r"[-\d.]+", fld)
    if not m: continue
    BA[(Z, N)] = float(m.group())  # keV per A
def B(Z, N): return BA[(Z, N)] * (Z + N) / 1000.0  # MeV total

B_d = B(1,1); B_t = B(1,2); B_h = B(2,1); B_a = B(2,2)
print("B (MeV): d %.4f  t %.4f  h %.4f  alpha %.4f" % (B_d, B_t, B_h, B_a))

# ---- clusters: (label, Z, N, B, radius band (matter rms, fm), n, W-weights fn, strain) ----
def W(gam, s, w): return s + w*gam   # s strong bonds, w weak bonds
CL = [
  ("d",     1,1, B_d, (1.95,1.965,1.98), 2, (1,0)),
  ("h",     2,1, B_h, (1.75,1.785,1.82), 3, (1,2)),
  ("t",     1,2, B_t, (1.54,1.59,1.68),  3, (1,2)),
  ("alpha", 2,2, B_a, (1.45,1.452,1.48), 4, (2,4)),
]
def tau(n, r): return (9.0/8.0)*HBAR2_M*(1.0-1.0/n)/(r*r)   # per quantum
def strain(Z, A): return AC*Z*(Z-1)/A**(1.0/3.0)
def rho(A, r):
    R = math.sqrt(5.0/3.0)*r
    return 3.0*A/(4.0*math.pi*R**3)

rows = {}
print("\ncluster  delta0 central [band]      rho central [band]   (tax/q central)")
for (lab, Z, N, Bv, rband, n, (s, w)) in CL:
    A = Z + N
    vals, rhos = [], []
    for r in rband:
        for g in GAMMA:
            gross = Bv + A*tau(n, r) + strain(Z, A)
            vals.append(gross / W(g, s, w))
        rhos.append(rho(A, r))
    rc, gc = rband[1], GAMMA[1]
    d0c = (Bv + A*tau(n, rc) + strain(Z, A)) / W(gc, s, w)
    rows[lab] = dict(d0=d0c, lo=min(vals), hi=max(vals), rho=rho(A, rc),
                     rlo=min(rhos), rhi=max(rhos))
    print("%-7s  %6.2f  [%5.2f, %5.2f]    %6.4f [%6.4f, %6.4f]   (%5.2f)" %
          (lab, d0c, min(vals), max(vals), rho(A, rc), min(rhos), max(rhos), tau(n, rc)))

# ---- T-C6a: all four in [13,19] ----
a_ok = all(13.0 <= rows[k]["d0"] <= 19.0 for k in rows)
a_band = all(rows[k]["lo"] >= 12.0 and rows[k]["hi"] <= 20.0 for k in rows)  # info
print("\nT-C6a (all central delta0 in [13,19]):", "PASS" if a_ok else "FAIL",
      " | full bands inside [12,20]:", a_band)

# ---- T-C6b: enhancement sign ----
gap = rows["alpha"]["d0"] - rows["d"]["d0"]
b1 = gap >= 1.5
b2 = rows["t"]["d0"] > rows["h"]["d0"]
order = sorted(rows, key=lambda k: rows[k]["rho"])
d0s = [rows[k]["d0"] for k in order]
rh  = [rows[k]["rho"] for k in order]
def spearman(x, y):
    rx = {v:i for i,v in enumerate(sorted(x))}; ry = {v:i for i,v in enumerate(sorted(y))}
    xr = [rx[v] for v in x]; yr = [ry[v] for v in y]
    mx = statistics.mean(xr); my = statistics.mean(yr)
    num = sum((a-mx)*(b-my) for a,b in zip(xr,yr))
    den = math.sqrt(sum((a-mx)**2 for a in xr)*sum((b-my)**2 for b in yr))
    return num/den
sp = spearman(rh, d0s)
b3 = sp > 0
print("T-C6b: alpha-d gap = %.2f MeV (>=1.5: %s) | mirror t>h: %s (t %.2f vs h %.2f)"
      % (gap, "PASS" if b1 else "FAIL", "PASS" if b2 else "FAIL",
         rows["t"]["d0"], rows["h"]["d0"]))
print("       density order:", order, " delta0:", ["%.2f"%v for v in d0s],
      " spearman = %.3f (>0: %s)" % (sp, "PASS" if b3 else "FAIL"))

# ---- T-C6c: alpha window ----
da = rows["alpha"]["d0"]
c_ok = 16.0 <= da <= 20.0
print("T-C6c: delta0(alpha) = %.2f  in [16,20]: %s   (bulk-required 22.3; residual x%.2f)"
      % (da, "PASS" if c_ok else "FAIL", 22.3/da))

# ---- T-C6d: B/A strict local max at A=4 over A in [2,8] ----
env = {}
for (Z, N), v in BA.items():
    A = Z + N
    if 2 <= A <= 8 and (A not in env or v > env[A]): env[A] = v
print("\nB/A envelope A=2..8 (keV):", {a: round(env[a],1) for a in sorted(env)})
d_ok = all(env[4] > env[a] for a in env if a != 4)
print("T-C6d (strict local max at A=4):", "PASS" if d_ok else "FAIL")

# ---- readings (not scored) ----
print("\nreadings: A=5 max B/A %.3f < alpha %.3f (unbound vs alpha+n by %.2f MeV)"
      % (env[5]/1000, env[4]/1000, B_a + 0.0 - env[5]*5/1e3))
B_li6 = B(3,3); B_be8 = B(4,4)
print("Li-6 - (alpha+d) = %.3f MeV (weak inter-cell net, positive small)"
      % (B_li6 - B_a - B_d))
print("Be-8 - 2*alpha  = %+.3f MeV (two-cell problem, named open)"
      % (B_be8 - 2*B_a))
