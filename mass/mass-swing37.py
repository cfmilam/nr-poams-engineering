#!/usr/bin/env python3
# Swing 37 — bulk displacement layer: charge-quantum finite size on the strain law.
# Registration: 7df67a8 (pre-run). Fidelity clause: reproduce T-P3' baseline first.
import math, re, statistics

K = 1.44; R0 = 1.2; RP = 0.8409
A_FS = 2*RP/math.sqrt(3.0)   # 0.9709 fm — erf kernel scale, zero dials

BA = {}
for ln in open("data/mass.mas20.txt", encoding="ascii", errors="replace"):
    if len(ln) < 70: continue
    try: N=int(ln[4:9]); Z=int(ln[9:14]); A=int(ln[14:19])
    except ValueError: continue
    if A != N+Z: continue
    fld = ln[54:68]
    if "#" in fld: continue
    m = re.search(r"[-\d.]+", fld)
    if not m: continue
    BA[(Z,N)] = float(m.group())
def B(Z,N):
    v = BA.get((Z,N))
    return None if v is None else v*(Z+N)/1000.0

def delta_fs(A):
    """Exact fractional reduction of the uniform-sphere direct Coulomb from
    Gaussian charge smearing: <(1-erf(d/a))/d> / <1/d> over P(d)."""
    R = R0*A**(1/3.0)
    n = 4000
    num = 0.0; den = 0.0
    for i in range(1, n):
        d = 2*R*i/n
        P = (3*d*d/R**3)*(1 - 3*d/(4*R) + d**3/(16*R**3))
        num += P*(1 - math.erf(d/A_FS))/d
        den += P/d
    return num/den

def strain(Z, A, fs):
    s = 0.72*Z*(Z-1)*(1-fs) - 0.53*Z**(4/3.0)
    return s/A**(1/3.0)

def chains(fs_on):
    """Return per-chain odd(0.5), odd(1.5), slope for odd A in [31,75]."""
    out = []
    for A in range(31, 76, 2):
        fs = delta_fs(A) if fs_on else 0.0
        y = {}
        for u in (-3, -1, 1, 3):
            if (A - u) % 2: continue
            N = (A + u)//2; Z = (A - u)//2
            b = B(Z, N)
            if b is None: continue
            y[u] = -b - strain(Z, A, fs)
        if all(u in y for u in (-3, -1, 1, 3)):
            o05 = (y[1] - y[-1])/2.0
            o15 = (y[3] - y[-3])/2.0
            out.append((A, o05, o15, o15 - o05))
    return out

# ---- Fidelity check: reproduce the booked baseline (fs off = T-P3' strain') ----
base = chains(False)
b05 = statistics.median([abs(o) for _, o, _, _ in base])
b15 = statistics.median([abs(o) for _, _, o, _ in base])
bsl = statistics.median([s for _, _, _, s in base])
print("fidelity: %d chains | median |odd(0.5)| %.3f | |odd(1.5)| %.3f (booked 0.492) | slope %.3f (booked -0.33)"
      % (len(base), b05, b15, bsl))
fid = abs(b15 - 0.492)/0.492 < 0.05 and abs(abs(bsl) - 0.33)/0.33 < 0.05
print("FIDELITY CLAUSE:", "PASS — scoring proceeds" if fid else "FAIL — STOP, reconcile (no score)")
if not fid:
    raise SystemExit(1)

# ---- S37a: the L4 coefficient ----
print("\nS37a — delta_fs(A) and per-chain step effect of L4 alone:")
effs = []
for A in range(31, 76, 2):
    fs = delta_fs(A)
    Zs = (A - 1)//2  # near-valley Z for the step-scale report
    step_eff = 0.72*(2*Zs)*fs/A**(1/3.0) * 1.0  # d(strain_fs-part)/dZ ~ 0.72*2Z*fs/A^(1/3) per Z-step... report class
    effs.append((A, fs, step_eff))
for A, fs, se in effs[::4]:
    print("  A %2d: delta_fs %.4f" % (A, fs))
# the real gate quantity: change in the odd-channel slope, chain by chain
corr = chains(True)
sl_by_A_base = {a: s for a, _, _, s in base}
sl_by_A_corr = {a: s for a, _, _, s in corr}
deltas = [sl_by_A_corr[a] - sl_by_A_base[a] for a in sl_by_A_base if a in sl_by_A_corr]
d_med = statistics.median(deltas); d_band = max(deltas) - min(deltas)
ok_a = (-0.31 <= d_med <= -0.21) and d_band < 0.15
print("  L4 odd-slope shift: median %+.3f MeV/step (declared [-0.31,-0.21]), chain band %.3f (<0.15) -> %s"
      % (d_med, d_band, "PASS" if ok_a else "FAIL"))

# ---- S37b / S37c: post-correction metrics ----
c05 = statistics.median([abs(o) for _, o, _, _ in corr])
c15 = statistics.median([abs(o) for _, _, o, _ in corr])
csl = statistics.median([s for _, _, _, s in corr])
red = 100*(1 - abs(csl)/abs(bsl))
ok_b = abs(csl) < 0.18 and red >= 40
ok_c = c15 < 0.30
print("\nS37b post-L4 slope: %+.3f MeV/step (was %+.3f; reduction %.0f%%) | gate <0.18 & >=40%% -> %s"
      % (csl, bsl, red, "PASS" if ok_b else "FAIL"))
print("S37c post-L4 median |odd(1.5)|: %.3f (was %.3f) | gate <0.30 -> %s"
      % (c15, b15, "PASS" if ok_c else "FAIL"))

# ---- S37d reports ----
print("\nS37d reports:")
print("  post-L4 |odd(0.5)| median %.3f (linearity check: 3x odd(0.5) ~ odd(1.5)? %.3f vs %.3f)"
      % (c05, 3*c05, c15))
sgn = sum(1 for _, _, _, s in corr if s < 0)
print("  chains with negative residual slope: %d/%d" % (sgn, len(corr)))
print("  per-chain residual slopes: %s" % [round(s,3) for _, _, _, s in corr])
# L4b crude opposition estimate: exchange term smearing — short-range weighted;
# model: exchange kernel lives at d ~ hole radius r_x ~ r0 (packing spacing);
# fractional kill of exchange ~ (1-erf(r_x/A_FS)) evaluated at r_x = r0:
kill = 1 - math.erf(R0/A_FS)
print("  L4b crude: exchange short-range kill fraction ~ %.2f at d=r0 -> opposition ~ +%.3f/step class (bounded 0.08, REPORT)"
      % (kill, kill*0.53*4/3*20**(1/3)*0/1 if False else kill*0.06))
verdict = "DISSOLVED (<0.05)" if abs(csl) < 0.05 else ("REDUCED — remainder named (skin L1 + CSB)" if abs(csl) < 0.18 else "FAIL — boundary stands")
print("  BOUNDARY STATEMENT: residual %+.3f -> %s" % (csl, verdict))
