# The Dip Enclosure — S < 3/2 with an Exact Certificate

**Madelung front, swing M-B.** Registration 3ccc992 (pre-run; architecture, saddle constants,
and exact saddle inequalities hand-declared). Instrument `madelung/madelung-swingB.py` /
`-run.txt`. Companion: `MADELUNG-INTERIOR-REDUCTION.md` (swing M-A: the merge theorem),
`MADELUNG-FIXEDPOINT-THEOREM.md` (the consolidated record; this closes its open item 2).
2026-08-12.

## 1 · Theorem

Let φ be the census heteroclinic — the graph σ = φ(t) of the neutral Thomas–Fermi flow
$t' = t + t^2 - \sigma$, $\sigma' = \tfrac12\sigma(3-t)$ from the eye node (0,0) to the
Sommerfeld saddle (3,12) — and S = φ(1) the dip (the value of √(x³χ) at the criticality
point t = 1). Then, with an exact rational certificate:

$$\frac{1465319}{1000000} \;\le\; S \;\le\; \frac{36733}{25000}, \qquad\text{hence}\qquad
S < \frac{3}{2} \;\text{ with margin } \frac{767}{25000} = 0.030680.$$

Corollary (edge identity, proved in the record): $k_{\text{edge}} = \sqrt{2/(2-S)} \in
[1.93405, 1.94133]$ — **k_edge < 2 with rigorous margin ≥ 0.0587**. Corollary (merge
theorem, M-A): the interior inequality σ̂ ≥ σ* holds strictly in a neighborhood of the peak.

**Imports (named, classical):** existence of the census heteroclinic and its convergence to
the Sommerfeld point (Sommerfeld 1932; rigorous TF asymptotics: Hille 1970); tangency of a
saddle-convergent orbit to the stable eigendirection (stable-manifold theorem, Perko/Hartman
class). Everything else is proved here or in M-A (t-monotonicity: nullcline invariance).

## 2 · Proof architecture

**Reduction.** By M-A Lemma A1 the heteroclinic is a graph φ(t) below the nullcline, and
dφ/dt = G(t,φ) = φ(3−t)/(2(t+t²−φ)) with G defined (nullcline gap positive along the chain,
verified per segment).

**Crossing lemma (scalar).** If h = U − φ ≥ 0 at a segment's right endpoint and
G(t, U(t)) > U′(t) on the segment, then h ≥ 0 on the segment: at any zero of h,
h′ = U′ − G < 0, so zeros are strict down-crossings in increasing t and h cannot become
negative to the left of a nonnegative anchor. Mirror statement for a lower barrier L with
G(t, L(t)) < L′(t). Induction over segments propagates the anchor right-to-left.

**Saddle anchor.** Take straight lines through (3,12): U = 12 − K₁(3−t), L = 12 − K₂(3−t)
with K₁ = 153/20 = 7.65, K₂ = 39/5 = 7.8. Exact checks: (2K₁−7)² = 68.89 < 73 < 73.96 =
(2K₂−7)², so K₁ < λ = (7+√73)/2 < K₂ (λ = the stable eigenslope). Tangency (import) gives
(12−φ)/(3−t) → λ, so eventually φ < U and φ > L as t → 3⁻: anchors exist inside [2.95, 3).
Barrier conditions on [2.95, 3): for the line 12 − K(3−t), G > K ⟺ 12 − 2K(K−7) > 3Kε;
at K₁: 2.055 > 3K₁ε on ε ≤ 1/20 (exact: 2.055 > 1.1475); at K₂ the reverse holds for all
ε ≥ 0 (12 − 2K₂(K₂−7) = −12/25 < 0). Hence φ(2.95) ∈ [L(2.95), U(2.95)] = [11.61, 11.6175]
— rigorously. (Consistency: the second-order manifold expansion φ ≈ 12 − λε + c₂ε²,
c₂ = 3λ/(6λ−28) = 1.2514, gives φ(2.95) ≈ 11.6145.)

**Piecewise-linear chain.** 390 segments of width 1/200 on [1, 2.95]; breakpoint values are
rationals (denominator 10⁶) at guide ± δ, δ graded 0.002 → 0.004 near the junction; junction
values forced to the saddle lines. Per segment and per barrier, two exact quadratic
positivity checks (nullcline gap; the barrier condition P(t) = W(3−t) − 2b(N−W) ≷ 0, a
concave quadratic — endpoint/vertex evaluation in `fractions.Fraction`, **zero floating
point in the verification**). Total 1564 checks: **0 failures** (`madelung-swingB-run.txt`).

**Conclusion.** L(1) ≤ φ(1) = S ≤ U(1) with U(1) = 36733/25000 < 3/2 exactly. ∎

## 3 · The construction story (booked honestly)

The barrier values are float-guided; the guide's first version (eye-side s-domain
integration, M-A chassis) is float-contaminated near the saddle — **the exact certificate
caught it** (61 failures clustered at t ≥ 2.795; the guide read φ(2.95) = 10.85 vs the
manifold series 11.6145). Rebuilt guide: backward graph-ODE integration from the
second-order manifold expansion at ε = 0.05 — backward-in-t is transverse-contracting, so
the O(10⁻³) series start error dies immediately. Two-route consistency: backward S =
1.467319743 vs eye-side booked 1.467319749 — **6×10⁻⁹ agreement between independent
routes**. A second construction iteration smoothed the δ-grading step (2 failures at the
ramp discontinuity). Final certificate clean. Registration allowed mechanical construction
retuning pre-verification; the gates were scored only on the verified object.

## 4 · Status changes to the consolidated record

- Claim 10 (the dip): COMPUTER-ASSISTED → **THEOREM with exact certificate** (this doc);
  S < 3/2 unconditional modulo the named classical imports.
- Claim 5 (sign structure ⇒ k < 2): the peak case is now theorem-grade via the merge
  theorem + this enclosure; the compact middle (relative margins 5–23%) and the eye tail
  bound remain for M-C — after which the interior inequality is a theorem end to end.
- k_edge = 1.9377 gains rigorous brackets [1.93405, 1.94133].
