# The Madelung Fixed-Point Theorem — Consolidated Record

Consolidated 2026-08-10 from the research ledger (MADELUNG-THEOREM-SKETCH §C1–C3,
MADELUNG-FORWARD, instruments tier3–tier3n). This document is the single citable chain:
statements, proofs or proof-status, verification record, attributions, open items.
House rule throughout: every claim carries its tier; a named negative outranks a
fabricated positive.

## 0 · Claim map (tiers)

| # | Claim | Tier |
|---|-------|------|
| 1 | Closure + self-duality + Coulomb eye ⇒ U_½ exactly (k = 2, n+l families) | THEOREM modulo (H2), citations closed |
| 2 | ⟨t⟩∠ ≡ 1 on every bounded E=0 orbit (zero-energy criticality) | PROVED (elementary; folklore flag) |
| 3 | k(J) = exact linear functional of the ledger's width density (Lemma 3) | PROVED + verified (K0/K1) |
| 4 | Madelung deficit 2−k = Abel transform of the width deficit D = T*−T | PROVED (identity) + verified (K1b) |
| 5 | Sign structure D ≥ 0, D′ ≤ 0 on every occupied row ⇒ k < 2 strict | VERIFIED, two chassis (K2, M2); analytic proof OPEN |
| 6 | k(l) hierarchy = Abel-kernel reach into the over-screened wing | VERIFIED (K3) |
| 7 | Edge identity k_edge = √(2/(2−√(x³χ)))\|_{t=1} | PROVED (one line) + verified 0.1–0.4% (K4) |
| 8 | TF k-table = one universal curve k(J/√f₀) | PROVED (corollary) |
| 9 | Valve/tangency theorem: 3/2 = tangency of the census flow at criticality | PROVED (exact algebra) |
| 10 | The dip: S = √q(1) = 1.467319754 < 3/2 (⇒ k_edge < 2) | COMPUTER-ASSISTED (budget 1e-8); formal enclosure OPEN |
| 11 | Pointwise master inequality E ≥ 1 | FALSE — named negative (eye face; exact asymptote) |

## 1 · Setting

Central ledger V(r) = −Zχ(r)/r; zero-energy (frontier) orbits; f(θ) = −2r²V = 2Zr·χ,
θ = log-radius; J = L. Apsidal slope k = A/π with A the peri→apo azimuth. The closure
member (Demkov–Ostrovsky U_½) has k = 2 for every J — the 720° double turn that
generates the n+l degeneracy families. The physical license (POAMS): a quantum is a
completed turn; the census grows at the E=0 frontier, which must close for every
winding being filed. The census stand-in is Thomas–Fermi: χ″ = χ^{3/2}/√x (import,
named; a POAMS-native census is separate open work).

## 2 · C1 — the ideal theorem (closure ⇒ U_½), status: theorem modulo H2

Statement: (A) L-uniform E=0 closure + (B) inversion self-duality + (C) Coulomb eye +
(D) neutral far field ⇒ V = U_½ exactly; hence Φ = 2π (k = 2) and the n+l families.
Proof chain: self-dual class W(r) = r²V symmetric under r ↔ R²/r ⇒ conformal cylinder
reduction ds² = f(θ)(dθ²+dφ²), f even; Δφ(J) ≡ const is an Abel equation for the width
of f; Abel inversion gives f = f₀ sech²(πθ/Φ) uniquely among even single-peaked wells;
the Coulomb eye pins the exponent: Φ = 2π. Rigor citations (recon #3): injectivity —
Gorenflo & Vessella, Abel Integral Equations, LNM 1461 (1991), under W ∈ L¹, (H2)
single-peaked, f → 0 at both ends; evenness-kills-shear — symmetric-member uniqueness,
lineage Borg 1946. (H2)'s failure mode is the double well — exactly the d-collapse
boundary, which belongs to the pairing ledger (separate front). Attribution: the U_μ
family, the fish-eye group theory, and the E=0 focusing non-uniqueness are
Demkov–Ostrovskii(–Berezina) 1971–72; the *selection principle* (self-duality/evenness
killing their documented shear freedom) appears nowhere in their corpus — the gap is
declared open by them, twice.

## 3 · Lemma 2 — zero-energy criticality (⟨t⟩∠ ≡ 1)

On every bounded E=0 orbit in every central ledger: (1/Φ)∮ t dφ = 1, t = −dlnχ/dlnr.
Proof: with G = 2Zrχ, ∮ t dφ = Φ − L∮ dG/(G√(G−L²)); the antiderivative
(2/J)arctan(√(G−J²)/J) telescopes around the closed loop. QED. Consequence: frontier
orbits self-average any screening to the marginal exponent; k is a functional of the
FLUCTUATION of t about 1, not its mean. Folklore flag: elementary enough that we
phrase it "we note"; no prior statement found as searched (virial lineage cited
defensively).

## 4 · Lemma 3 — width linearity (the machinery of the whole front)

Under (H2), layer-cake in the level variable u:
    A(J) = J ∫_{J²}^{f₀} (−T′(u)) du/√(u−J²),   k = A/π,
T(u) = width of {f ≥ u}. EXACT and linear in the width density. Corollaries:
(i) shear-blindness — asymmetric redistributions of width change nothing (the
Firsov/D–O–Berezina non-uniqueness in one line); (ii) Lemma 2 is its mean statement;
(iii) for TF, f = 2Zb·(xχ) has Z-independent shape ⇒ the whole k-table is ONE
universal curve k(J/√f₀). Verified: K0a (analytic anchor A* ≡ 2π, 1e-11), K1 (matches
direct orbit integral row-wise). Attribution: the machinery is the classical period
inverse problem (Landau–Lifshitz §12) transposed to the E=0 azimuth; the apsidal-angle
integral and ℓ-monotonicity are Castelli (JMAA 2015) and Rojas (2017); the E=0
width-linearity, shear-blindness statement, and everything below are, as searched,
new here.

## 5 · The deficit identity, the sign structure, and the interior inequality

Peak-matched closure member T*(u) = 4 arccosh√(f₀/u). Deficit D = T* − T:
    2 − k(J) = (J/π) ∫_{J²}^{f₀} (−D′(u)) du/√(u−J²)    (exact identity; K1b at 9e-12).
Sign theorem: D nonincreasing (D′ ≤ 0, D(f₀) = 0) ⇒ k(J) < 2 strictly for all J.
Verification: D ≥ 0 AND D′ ≤ 0 hold on every occupied row — two independent chassis
(BVP tier3k K2; shooting tier3m M2, worst LHS/RHS = 0.9687 at the peak, min margin
0.230 at u/f₀ = 0.75). The k(l) hierarchy is the kernel's reach into the wing: s-rows
collect 94–98% of their deficit below the midpoint level, d/f-rows 50–71% (K3).
Exact reformulation: 1/σ_in + 1/σ_out = 2/σ̂ (σ̂ = slope of the even rearrangement), so
the interior theorem ⟺ σ̂ ≥ σ* — "the rearranged census is steeper-per-level than
closure." NAMED NEGATIVE (tier3m M1): the pointwise sufficient route E ≡ (1−t)² +
f/f₀ ≥ 1 is FALSE — E < 1 on the eye face (t ∈ (0.02, 0.76), min 0.9654 at t = 0.178;
exact asymptote E−1 ~ (1/m₀ − 2B₁)x = −1.1200·x). The census's eye face is genuinely
shallower than closure; the outer face (t → 3 vs 2) overcompensates. The inequality is
irreducibly two-point. Analytic proof: OPEN (the sharpest formulation: prove σ̂ ≥ σ*
from the cylinder profile equation p″ = e^{θ+p/2} − (1−p′)(2−p′)).

## 6 · The edge identity

At the binding edge, k is set by the peak curvature, and the peak of xχ is the t=1
criticality point. One line from the TF equation:
    x t′|_{t=1} = 2 − √(x³χ)   ⇒   k_edge = √( 2 / (2 − √(x³χ)) )|_{t=1}.
Verified: predicted 1.9377 vs measured 1.93501/1.94148 at 99%/99.9% of L_max (K4).
The peak POINT is classical (Fermi 1928; Oliphant 1956); the curvature identity and
k_edge formula are new as searched.

## 7 · The valve/tangency theorem (why 3/2) — proved

Autonomous reduction (classical variables): t = −dlnχ/dlnx, q = x³χ:
    dt/ds = t + t² − √q,   dq/ds = q(3 − t),   s = ln x.
The neutral census is the heteroclinic orbit (0,0) → (3,144); the Sommerfeld far field
is the flow's fixed point. On the closure-rate curve B_{1/2}: √q = t + t² − ½ (the
locus dt/ds = ½ = the closure member's peak rate), crossing reduces to one polynomial
with an exact factorization:
    5 − 3t − 4t² + 2t³ = (t − 1)(2t² − 2t − 5).
Hence: one-way valve (downward-only), strict, for ALL t ∈ (0,1); EXACT TANGENCY at
t = 1, where B_{1/2} passes through the closure point (1, 9/4), i.e. √q = 3/2; valve
flips upward-crossable on (1, (1+√11)/2 ≈ 2.158). The number 3/2 is where (t−1)
divides the census field's crossing polynomial — not imported, not fitted.
Verified along the orbit (tier3l): downward crossing t* = 0.8818; upward re-cross
t = 2.0628 ∈ (1, 2.158); tangency algebra at 1.4e-16.

## 8 · The dip (the one number), high precision

S ≡ √q at the t=1 crossing (mpmath dps=40 shooting, launch series with Baker
B₁ = 1.5880710226113753…):
    S = 1.467319754 (±1e-8; budget: integrator truncation 8e-9 dominates; dS/dB₁ =
    162.7 × B₁ precision — negligible)
    dip = 3/2 − S = 0.032680246;   k_edge = √(2/(2−S)) = 1.937678418.
S is transcendental-grade (inherits B₁); computable to arbitrary digits; no closed
form claimed. Status: computer-assisted verification with explicit budget; a formal
validated enclosure (⇒ unconditional S < 3/2) is OPEN — soft estimates are provably
blind at this margin (the stay-above branch of the barrier argument fails only by
0.033).

## 9 · The one sentence

The census — the atom's own bookkeeping of stacked closures — flows from the bare eye
to the Sommerfeld far field along one universal curve; the geometry of that flow
contains a one-way valve whose only point of tangency is the closure value 3/2 at the
criticality line; the orbit ducks under at the last window the tangency leaves open
and reads k_edge = 1.9377 from the depth of the dip. The table of elements closes at
two turns because the census kisses closure at its frontier and cannot pierce it —
and every period opens with an s-orbit because the kernel of the deficit identity
reaches deepest into the over-screened wing exactly for the humblest winding.

## 10 · Open items (exact statements)

1. Interior inequality: prove σ̂ ≥ σ* (even-rearrangement slope ≥ closure slope at
   every level) from the cylinder profile equation. Pointwise routes provably
   insufficient (M1 named negative); the two-chassis verification stands meanwhile.
2. Formal validated enclosure of the dip (interval arithmetic / Taylor models),
   upgrading S < 3/2 to unconditional theorem.
3. Physics-level import: replace the TF census stand-in with a POAMS-native closure-
   stacking census (shared with the Aufbau exhibit's Scope).

## 11 · Instrument index (research-ledger workspace)

tier3k.py / -run1/2 (width confrontation, K0–K5) · tier3l.py / -run1/2 (phase plane,
L1–L4) · tier3m runs (master inequality, M1–M3) · tier3n.py / -run1 (high-precision
dip) · earlier: tier3–tier3g (apsidal/aufbau chassis), tf-apsidal.py (BVP χ).
Registrations were committed to this repo BEFORE each run (see DERIVATION-LEDGER
entries of 2026-08-09/10).

---

## 12 · Addendum 2026-08-12 — the mathematical tier closes

Same-day sequence M-A → M-B → M-C (docs: MADELUNG-INTERIOR-REDUCTION.md,
MADELUNG-DIP-ENCLOSURE.md; instruments `madelung/`; registrations pre-run throughout):

- **Claim 5 (sign structure ⇒ k < 2): VERIFIED → THEOREM.** Exact-rational certificate,
  2447 checks: σ̂ ≥ σ* at every level (four-piece cover; the pointwise impossibility M1
  circumvented by the two-point structure exactly as required). Hence D′ ≤ 0, D ≥ 0, and
  k(J) < 2 strict on every row via the deficit identity (claim 4).
- **Claim 10 (the dip): COMPUTER-ASSISTED → THEOREM.** S ∈ [1465319/1000000, 36733/25000],
  S < 3/2 with exact margin 767/25000; k_edge ∈ [1.93405, 1.94133]. Certificate: 1564
  exact checks; barrier chain + saddle cone; zero floats in verification.
- **The merge theorem (new):** the interior inequality's peak case ⟺ S < 3/2; its peak
  ratio = k_edge/2. Open items 1 and 2 were one object; both are now closed.
- **Open item 3 (POAMS-native census) is the front's only remaining open** — the physics
  tier. Imports carried by the theorems: TF census stand-in; Sommerfeld/Hille heteroclinic;
  stable-manifold tangency (Perko/Hartman class).
