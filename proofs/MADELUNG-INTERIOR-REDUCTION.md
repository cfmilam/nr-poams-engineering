# The Interior Inequality, Reduced — and the Merge Theorem

**Madelung front, swing M-A.** Registration b4ad780 (pre-derivation, hand declarations in the
research ledger); instrument `madelung-swingA.py` / `-run2.txt` (consistency grade, non-validated).
Companion to `MADELUNG-FIXEDPOINT-THEOREM.md` (the consolidated record; its open item 1 is the
subject here, its open item 2 the dip). 2026-08-12.

## 0 · What this document does

The interior inequality — σ̂ ≥ σ* at every level, "the rearranged census is steeper-per-level
than closure," equivalent to the sign structure D′ ≤ 0 that makes k < 2 strict on every row —
was verified on two chassis and analytically OPEN, with the pointwise route provably false
(M1: the census's eye face is genuinely shallower than closure; the inequality is irreducibly
two-point). This document reduces it to a single coordinate, proves both endpoint cases, and
proves that **its hard endpoint is exactly the dip** — open items (1) and (2) of the
consolidated record are one object at the frontier. What remains open is stated as a finite
compact-window enclosure with fat margins (the M-B/M-C instrument spec).

## 1 · Setting (inherited)

Census flow in the classical variables: t = −d ln χ/d ln x, σ = √q = √(x³χ), s = ln x:

$$t' = t + t^2 - \sigma, \qquad \sigma' = \tfrac{1}{2}\sigma(3 - t),$$

with the neutral census the heteroclinic Γ from the eye node (0,0) to the Sommerfeld saddle
(3,12). The profile level is p = ln(xχ), p′ = 1 − t, peak at t = 1 (criticality), dip value
S = σ|_{t=1} = 1.467319754 (1e-8 budget, non-validated). Width bookkeeping (Lemma 3 of the
record): at level u, the two faces contribute width density 1/(u·β) per face with
β = |dp/dθ| = |1 − t|; the closure member's width density is 2/(u√(1−v)), v = u/f₀.

## 2 · Lemma A1 — t is a global coordinate on Γ

**Claim.** Along Γ, σ < t + t² strictly; hence t′ > 0 and t parameterizes Γ over (0,3).

**Proof.** Let N(t) = t + t², g = σ − N(t). On the parabola g = 0 with 0 < t < 3:
t′ = 0 and ġ = σ′ − (1+2t)t′ = σ′ = ½N(t)(3−t) > 0. So every touch of {g = 0} at interior t
has g strictly increasing: orbits cross only from {g<0} to {g>0}, and {g > 0} is forward-
invariant. Near the saddle, the stable eigenvalue is λ₋ = −(√73−7)/2 and its eigenvector has
slope 7 − λ₋ = (7+√73)/2 ≈ 7.772 > N′(3) = 7; approaching (3,12) from t < 3 along that
direction, g ≈ −(7.772−7)(3−t) < 0: **the tail of Γ lies in {g < 0}**. If Γ entered {g > 0}
at any finite s, forward-invariance would trap it there, contradicting the tail; a touch of
the parabola is excluded by ġ > 0 (it would be an entry). Near the eye, σ ~ (t/B₁)^{3/2} ≪
N(t): Γ launches in {g < 0}. Hence g < 0 on all of Γ. ∎

Consequences: p is increasing on t ∈ (0,1), decreasing on (1,3); v = e^{p − p(1)} is a
bijection from each face to (0,1); the level pairing τ : (0,1) → (1,3), v(τ(t)) = v(t), is
well-defined and continuous.

## 3 · Lemma A2 — the exact restatement

At level v, the faces carry β_in = 1 − t and β_out = τ(t) − 1. The interior inequality
σ̂ ≥ σ* (harmonic-mean face slope ≥ closure slope, every level) is **exactly**

$$\Psi(t) \;=\; \frac{1}{1-t} \;+\; \frac{1}{\tau(t)-1} \;-\; \frac{2}{\sqrt{1 - v(t)}} \;\le\; 0
\qquad \text{for all } t \in (0,1),$$

with τ and v computed on Γ via φ(t) = σ(t) and dp/dt = (1−t)/(t + t² − φ(t)). (This is
D′ ≤ 0 written in the t-coordinate; nothing is approximated.)

**Cross-chassis verification that this is the same object the record measured:** the two
booked M2 numbers are both recovered from the reduction — the worst ratio σ*/σ̂ = 0.9687 "at
the peak" (here: → 0.9688, §4) and the minimum margin "0.230 at u/f₀ = 0.75" (here: the |Ψ|
minimum is 0.2299 at v = 0.738 — the M2 margin metric is identified as |Ψ|, the width-density
gap). Instrument: RK4 on the polynomial system, series launch (Baker B₁), divergence guard at
t < 3 (data region s ≤ 5.3; S reproduced to 5.2×10⁻⁹).

## 4 · Theorem A3 — the Merge Theorem (the peak case IS the dip)

**Claim.** As t → 1: Ψ(t) = \frac{2}{1-t}\left(1 - \sqrt{2(2-S)}\right) + o\!\left(\frac{1}{1-t}\right).
Hence the peak case of the interior inequality holds strictly iff **S < 3/2** — the dip
statement. Open items (1) and (2) of the consolidated record merge at the frontier.

**Proof.** t + t² − φ → 2 − S ≡ m₀ as t → 1 (φ continuous, φ(1) = S). From
dp/dt = (1−t)/(t+t²−φ): p(1) − p(t) = (1−t)²/(2m₀)·(1+o(1)) on the eye face, and the same
expansion with (τ−1)² on the outer face; equal levels force τ − 1 = (1−t)(1+o(1)). Then
1 − v = (1−t)²/(2m₀)(1+o(1)) and

$$\Psi = \frac{2}{1-t} - \frac{2\sqrt{2m_0}}{1-t} + o\Big(\frac{1}{1-t}\Big)
      = \frac{2}{1-t}\Big(1 - \sqrt{2(2-S)}\Big) + o\Big(\frac{1}{1-t}\Big). \;\blacksquare$$

**Identities that close the circle.** The peak ratio is
σ*/σ̂ → 1/√(2(2−S)) = **k_edge/2** (edge identity k_edge = √(2/(2−S))): the interior
inequality's peak limit is literally k_edge < 2 — the level-resolved tie-break collapses to
the edge statement at its own frontier, and the booked M2 worst ratio 0.9687 is k_edge/2 =
1.9377/2. One number — the dip — controls the tie-break at every scale of resolution.

## 5 · Lemma A4 — the eye endpoint (with the gate miss booked)

**Claim.** Ψ(t) → 1 + ½ − 2 = **−1/2** as t → 0⁺ (strict margin at the eye).

**Proof.** v → 0 on the eye face; the pairing sends the level to the far tail where τ → 3;
each term converges. ∎

**Convergence rate (the booked miss).** The approach is O(x_out^{−λ}) with
λ = (√73−7)/2 = 0.7720 — the Sommerfeld saddle's stable eigenvalue controls the eye margin.
The registered numeric gate (Ψ(0.02) ∈ −0.5 ± 0.03) **FAILED as scored** (measured −0.418):
the hand-declared convergence estimate ignored this slow power tail. The limit is algebra and
stands; the gate's proxy was misconceived; diagnostics (report-only) Ψ(0.01) = −0.440,
Ψ(0.005) = −0.459 confirm the trend and the rate.

## 6 · The margin map, and what remains

Measured on the reduction (consistency grade): the relative margin 1 − σ*/σ̂ **decreases
monotonically** from 0.229 at the eye to 0.0312 at the peak. The global pinch of the interior
inequality is its peak limit, and the peak limit is the dip margin (2 − k_edge)/... = 3.1%.
Everything away from the peak carries 5–23% room.

**Remaining open, exactly (the M-B/M-C spec):**
- **M-B (the tight end):** a validated enclosure of Γ for the polynomial field — saddle-cone
  local stable-manifold enclosure + interval Taylor backward integration (backward from the
  saddle the transverse direction contracts) — giving unconditional **S < 3/2** and an
  explicit peak neighborhood where Theorem A3's leading term dominates. This single
  instrument closes consolidated-record open item 2 AND the hard end of item 1.
- **M-C (the fat middle):** the same enclosure walked over a compact window t ∈ [t₀, t₁]
  with the pairing bracketed; margins 5–23% mean coarse interval bounds suffice.
- The eye end is Lemma A4 (algebra) plus an explicit tail bound at rate λ = 0.772.

Nothing else stands between the two-chassis verification and a validated theorem.
