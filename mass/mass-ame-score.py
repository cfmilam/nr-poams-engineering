#!/usr/bin/env python3
# AME2020 confrontation — T-P4 (pairing staggering) & T-P3 (census evenness).
# Tolerances registered 2026-08-11 (swing-1 booking 56b6f16) BEFORE this pull.
import os, re, subprocess, statistics, sys, urllib.request

F = "data/mass.mas20.txt"
os.makedirs("data", exist_ok=True)
if not os.path.exists(F) or os.path.getsize(F) < 100000:
    for url in ("https://www-nds.iaea.org/amdc/ame2020/mass_1.mas20.txt",
                "https://www-nds.iaea.org/amdc/ame2020/mass.mas20.txt"):
        try:
            urllib.request.urlretrieve(url, F); break
        except Exception as e: print("fetch fail", url, e)
lines = open(F, encoding="ascii", errors="replace").read().splitlines()
print("file lines:", len(lines))

# Parse: find data start (first line whose cols parse as N,Z,A ints). AME2020 fixed width:
# N: 4-9, Z: 9-14, A: 14-19, el: 20-23, B/A field around cols 54-68 (verify via spot check).
BA = {}  # (Z,N) -> B/A keV (experimental only; '#' = extrapolated -> skip)
for ln in lines:
    if len(ln) < 70: continue
    try:
        N = int(ln[4:9]); Z = int(ln[9:14]); A = int(ln[14:19])
    except ValueError: continue
    if A != N + Z: continue
    fld = ln[54:68]
    if "#" in fld: continue          # extrapolated, excluded (mechanical, logged)
    m = re.search(r"[-\d.]+", fld)
    if not m: continue
    try: ba = float(m.group())
    except ValueError: continue
    BA[(Z, N)] = ba
print("experimental nuclides parsed:", len(BA))
fe = BA.get((26, 30)); print("spot-check Fe-56 B/A keV:", fe)
assert fe is not None and abs(fe - 8790.36) < 2.0, "PARSE FAILURE - fix slices"
B = {k: v * (k[0] + k[1]) / 1000.0 for k, v in BA.items()}  # total binding, MeV

# ---- T-P4: staggering. For each Z chain over N: triples (N-1,N,N+1), N odd, A>=16.
res = {0: [0, 0], 1: [0, 0]}  # Zparity -> [hits, total]
for (Z, N) in sorted(B):
    if N % 2 == 0: continue
    if (Z, N - 1) in B and (Z, N + 1) in B and (Z + N) >= 16:
        hit = B[(Z, N)] < (B[(Z, N - 1)] + B[(Z, N + 1)]) / 2
        res[Z % 2][0] += hit; res[Z % 2][1] += 1
fe_ = 100 * res[0][0] / res[0][1]; fo = 100 * res[1][0] / res[1][1]
tot = 100 * (res[0][0] + res[1][0]) / (res[0][1] + res[1][1])
print(f"\nT-P4 staggering: even-Z {res[0][0]}/{res[0][1]} = {fe_:.2f}%   "
      f"odd-Z {res[1][0]}/{res[1][1]} = {fo:.2f}%   combined {tot:.2f}%")
print("T-P4 VERDICT (registered >=90% each):",
      "PASS" if fe_ >= 90 and fo >= 90 else "FAIL")

# ---- T-P3: odd-A isobars A in [31,199]; y(Z) = -B + 0.72 Z(Z-1)/A^(1/3); cubic vs quad.
def polyfit3(xs, ys):
    import math
    n = len(xs); X = [[x**k for k in range(4)] for x in xs]
    # normal equations 4x4
    M = [[sum(X[i][a] * X[i][b] for i in range(n)) for b in range(4)] for a in range(4)]
    V = [sum(X[i][a] * ys[i] for i in range(n)) for a in range(4)]
    # gaussian elim
    for c in range(4):
        p = max(range(c, 4), key=lambda r: abs(M[r][c]))
        M[c], M[p] = M[p], M[c]; V[c], V[p] = V[p], V[c]
        for r in range(c + 1, 4):
            f = M[r][c] / M[c][c]
            for k in range(c, 4): M[r][k] -= f * M[c][k]
            V[r] -= f * V[c]
    coef = [0] * 4
    for r in (3, 2, 1, 0):
        coef[r] = (V[r] - sum(M[r][k] * coef[k] for k in range(r + 1, 4))) / M[r][r]
    return coef  # c0..c3
ratios = []; skipped = 0
for A in range(31, 200, 2):
    chain = sorted((Z, y) for (Z, N), b in B.items() if Z + N == A
                   for y in [-b + 0.72 * Z * (Z - 1) / A ** (1 / 3)])
    if len(chain) < 6: skipped += 1; continue
    Zs = [z for z, _ in chain]; ys = [y for _, y in chain]
    zstar = Zs[ys.index(min(ys))]
    pts = [(z - zstar, y) for z, y in chain if abs(z - zstar) <= 4]
    left = sum(1 for x, _ in pts if x < 0); right = sum(1 for x, _ in pts if x > 0)
    if len(pts) < 6 or left < 2 or right < 2: skipped += 1; continue
    c = polyfit3([p[0] for p in pts], [p[1] for p in pts])
    if abs(c[2]) < 1e-9: skipped += 1; continue
    ratios.append(abs(4 * c[3] / c[2]))
med = statistics.median(ratios)
q1 = statistics.quantiles(ratios, n=4)[0]; q3 = statistics.quantiles(ratios, n=4)[2]
print(f"\nT-P3 census evenness: {len(ratios)} odd-A chains scored ({skipped} skipped, "
      f"mechanical floor); 4|c3/c2| median {med:.4f}  IQR [{q1:.4f},{q3:.4f}]")
print("T-P3 VERDICT (registered median < 0.10):", "PASS" if med < 0.10 else "FAIL")
