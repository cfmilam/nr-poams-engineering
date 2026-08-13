#!/usr/bin/env python3
"""Mass swing L1 — the skin seat: proton-radius census response layer.
(The first of swing 37's two named boundary owners; 'skin L1, queued derivable'.)

MECHANISM (exact potential theory, zero dials): the strain column prices every
charge at the volume-averaged seat — a charge in a uniform ball of the others
sees <1/d> = (6/5)/R on average (that 6/5 is baked into the 0.72 coefficient:
(1/2)(1.44/1.2)(6/5) = 0.72). But the mirror-odd construct differences the
LEAST-BOUND quanta, and the least-bound proton is SKIN-SEATED: at radius
fraction x its seat reads <1/d> = ((3 - x^2)/2)/R. At the skin (x = 1) that is
1/R — a 1/6 discount against the average seat (5/6 vs 6/5: potential theory's
own numbers, noted, unclaimed against the ledger's recurring sixths).

THE LAYER: one seat charge per nucleus (the valence proton — the quantum the
mirror difference actually moves), corrected from the average seat to x = 1:
    dE(Z, A) = -(k (Z-1)/R) * (6/5 - (3 - x^2)/2)   [x = 1: -0.24 (Z-1)/A^{1/3} MeV]
applied on top of the full booked column (strain' from T-P3' + exchange filing
+ L4 charge-quantum finite size, untouched).

HAND-DECLARED (registered pre-run):
  Hand-derived slope shift: -0.12/A^{1/3} per step, i.e. -0.036 ... -0.030
  across the chain span; hand-estimated ownership of the +0.076 residual ~ 44%.
GATES:
  L1-fid FIDELITY: reproduce the booked post-L4 state on the same chains:
      slope +0.076 +/- 0.005, median |odd(1.5)| 0.112 +/- 0.005, 13 chains
      — else STOP, no score.
  L1a THE LAYER: median odd-slope shift in [-0.045, -0.020] MeV/step AND
      chain band < 0.02 (the layer is analytic in (Z, A); scatter would mean
      a coding error, not physics).
  L1b THE SCORE: direction must be TOWARD zero; owned share of the +0.076
      residual in [30%, 70%] = CLAIM band (hand ~44%). owned < 25% -> FAIL
      booked (CSB owns the boundary alone). owned > 85% -> flagged
      OVER-OWNERSHIP (CSB is a real, extant-open co-owner; eating its share
      is suspicious, not a win).
  L1c REPORT: post-L1 median |odd(1.5)|, |odd(0.5)|, linearity 3x0.5 vs 1.5,
      per-chain residual slopes, negative-slope count.
  L1d SENSITIVITY (report-only, no gates, all pre-named):
      x = 0.95 seat; two seat charges; the m = 9 full-skin variant (expected
      DEAD by overshoot — the skin chain's other modes are common-mode across
      the mirror difference and must not each be seat-priced); erf-interplay
      bound (seat pairs live at d ~ R >> a, smearing nil); exchange-seat
      truncation eta = 1/2 bound (Z^{-2/3} suppressed, ~0.002/step class).
BOUNDARY: whatever remains after L1 is named CSB (open in the extant
literature too) + seat-profile refinement (x-distribution of the skin mode).

Run from workspace root. Registration commit = this file, pre-run.
"""
import math, re, statistics

K = 1.44; R0 = 1.2; RP = 0.8409
A_FS = 2*RP/math.sqrt(3.0)

BA = {}
for ln in open("memory/poams-audit/data/mass.mas20.txt", encoding="ascii", errors="replace"):
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
    R = R0*A**(1/3.0)
    n = 4000
    num = 0.0; den = 0.0
    for i in range(1, n):
        d = 2*R*i/n
        P = (3*d*d/R**3)*(1 - 3*d/(4*R) + d**3/(16*R**3))
        num += P*(1 - math.erf(d/A_FS))/d
        den += P/d
    return num/den

def seat_corr(Z, A, x=1.0, seats=1):
    """dE = -(k (Z-1)/R)(6/5 - (3-x^2)/2) per seat charge (MeV, negative)."""
    if Z < 2: return 0.0
    R = R0*A**(1/3.0)
    return -seats*(K*(Z-1)/R)*(6.0/5.0 - (3.0 - x*x)/2.0)

def strain(Z, A, fs, l1=False, x=1.0, seats=1):
    s = 0.72*Z*(Z-1)*(1-fs) - 0.53*Z**(4/3.0)
    s = s/A**(1/3.0)
    if l1: s += seat_corr(Z, A, x, seats)
    return s

def chains(l1, x=1.0, seats=1):
    out = []
    for A in range(31, 76, 2):
        fs = delta_fs(A)
        y = {}
        for u in (-3, -1, 1, 3):
            if (A - u) % 2: continue
            N = (A + u)//2; Z = (A - u)//2
            b = B(Z, N)
            if b is None: continue
            y[u] = -b - strain(Z, A, fs, l1, x, seats)
        if all(u in y for u in (-3, -1, 1, 3)):
            o05 = (y[1] - y[-1])/2.0
            o15 = (y[3] - y[-3])/2.0
            out.append((A, o05, o15, o15 - o05))
    return out

# ---- L1-fid: reproduce the booked post-L4 state ----
base = chains(False)
b15 = statistics.median([abs(o) for _, _, o, _ in base])
bsl = statistics.median([s for _, _, _, s in base])
print("L1-fid: %d chains | slope %+.3f (booked +0.076) | |odd(1.5)| %.3f (booked 0.112)"
      % (len(base), bsl, b15))
fid = len(base) == 13 and abs(bsl - 0.076) <= 0.005 and abs(b15 - 0.112) <= 0.005
print("FIDELITY CLAUSE:", "PASS — scoring proceeds" if fid else "FAIL — STOP, no score")
if not fid:
    raise SystemExit(1)

# ---- L1a: the layer ----
corr = chains(True)
sb = {a: s for a, _, _, s in base}
sc = {a: s for a, _, _, s in corr}
deltas = [sc[a] - sb[a] for a in sb]
d_med = statistics.median(deltas); d_band = max(deltas) - min(deltas)
ok_a = (-0.045 <= d_med <= -0.020) and d_band < 0.02
print("\nL1a seat-layer slope shift: median %+.4f MeV/step (declared [-0.045,-0.020]), band %.4f (<0.02) -> %s"
      % (d_med, d_band, "PASS" if ok_a else "FAIL"))

# ---- L1b: the score ----
csl = statistics.median([s for _, _, _, s in corr])
toward = abs(csl) < abs(bsl) and (csl == 0 or (csl > 0) == (bsl > 0) or abs(csl) < 0.02)
owned = 100*(1 - abs(csl)/abs(bsl))
flag = ""
if owned > 85: flag = "  [OVER-OWNERSHIP FLAG — CSB is a real co-owner]"
ok_b = toward and 30 <= owned <= 70
verdict = "PASS — CLAIM" if ok_b else ("FAIL — booked (CSB owns the boundary alone)" if owned < 25 else "outside claim band — booked as found")
print("L1b post-L1 slope: %+.4f MeV/step (was %+.3f) | owned %.0f%% (claim [30,70], hand ~44) -> %s%s"
      % (csl, bsl, owned, verdict, flag))

# ---- L1c: reports ----
c05 = statistics.median([abs(o) for _, o, _, _ in corr])
c15 = statistics.median([abs(o) for _, _, o, _ in corr])
neg = sum(1 for _, _, _, s in corr if s < 0)
print("L1c post-L1 |odd(1.5)| %.3f (was %.3f) | |odd(0.5)| %.3f | linearity 3x: %.3f vs %.3f | neg slopes %d/%d"
      % (c15, b15, c05, 3*c05, c15, neg, len(corr)))
print("    per-chain residual slopes: %s" % [round(s, 3) for _, _, _, s in corr])

# ---- L1d: sensitivities (report-only) ----
print("\nL1d sensitivities (report-only):")
for lab, kw in (("x=0.95", dict(x=0.95)), ("seats=2", dict(seats=2)), ("m=9 full skin (pre-named DEAD)", dict(seats=9))):
    cc = chains(True, **kw)
    scc = statistics.median([s for _, _, _, s in cc])
    sh = statistics.median([s2 - sb[a2] for (a2, _, _, s2) in cc])
    print("  %-32s slope %+.4f | shift %+.4f" % (lab, scc, sh))
# erf interplay bound: seat pairs at d ~ R; smearing factor there
A_mid = 47; Rm = R0*A_mid**(1/3.0)
print("  erf interplay at d=R (A=47): (1-erf(R/a)) = %.2e -> nil, as declared" % (1 - math.erf(Rm/A_FS)))
# exchange-seat truncation bound (eta = 1/2): per-step class
Zm = 23.0
xs = 0.5*0.53*(4.0/3.0)*(1.0/3.0)*Zm**(-2.0/3.0)/A_mid**(1/3.0)
print("  exchange-seat eta=1/2 per-step class: ~%.4f MeV/step -> report-only, as declared" % xs)
print("\nBOUNDARY STATEMENT: post-L1 residual %+.4f -> remainder named: CSB (extant-open) + seat-profile refinement" % csl)
