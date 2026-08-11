# Mass Ledger — Swing 4: Saturation at Capacity, and the Skin Integral
**Follows:** swings 1–3 (56b6f16, 43fb9a7/71d6382/44656c2, 5be7b5e/4aec87f).
GROUNDING gate binding; labels tagged; imports named; fitting is the only sin.

## 1. Saturation-at-Capacity Theorem (the kink equilibrium)
Swing 1 scaffolded bulk on fcc z = 12 with a diluted δ_eff; swing 3's capacity law
makes the scaffold unnecessary — and answers what SETS the equilibrium density.
Per-quantum energy at relative density u = ρ/ρ₀ with contact count z(u) = z_c·u^ν
(contacts within the fixed lock shell ∝ local density, ν ≈ 1 leading order):
    e(u) = τ_b·u^{2/3} − (δ₀/2)·min(z(u), z_c)  [+ any clash cost for z > z_c]
THEOREM. e(u) has its minimum AT the capacity point z(u) = z_c (u = 1) for every
contact exponent ν > 2τ_b/(3C) = 0.373 and every clash cost ≥ 0 (including zero):
    e′(1⁻) = (2/3)τ_b − νC < 0 ⇔ ν > 2τ_b/3C;   e′(1⁺) = (2/3)τ_b + clash′ > 0.
The equilibrium is a KINK minimum — pinned at capacity, no tuning, no hard core
required: expansion loses profit (linear) faster than tax (u^{2/3}); compression
gains nothing (profit capped) and pays tax. **Saturation density is the capacity
point: the packing self-tunes until each quantum's contact count equals its patch
capacity, z(ρ₀) = z_c.** ("Nuclear saturation" — comparative label — as solid-angle
bookkeeping; the hard core is optional decoration, entering only the compressibility.)
NO-DIAL CHECK (imports: ρ₀ = 0.138 fm⁻³ from r₀; quantum matter radius r_q = 0.86 fm;
lock range ξ = 2λ̄ ≈ 0.42 fm from swing 3): geometric contact count
    z = ρ₀·(4π/3)(2r_q + ξ)³ − 1 = 4.5 … 5.3  (ξ = 0.40 … 0.50 fm)
vs z_c = 4.78 ± 0.35 extracted from the ENERGY ledger. Two independent routes —
one through measured density and sizes, one through binding arithmetic — meet
inside each other's brackets. Nothing was tuned.
COROLLARY (retro-coherence): swing 2's bulk arithmetic is unchanged — per-quantum
gross (z_c/2)δ₀ = 35.9, tax 20.1, net 15.8 — the same equation, now with z_c as the
REAL coordination (≈5 nearest partners at ρ₀), not a diluted 12.
PREDICTION (kink signature): the interior density profile meets ρ₀ at finite depth
(no exponential approach from inside); only the outer tail is exponential.

## 2. The Skin Integral (P2's coefficient: structure closed, question relocated)
Surface energy = gradient tax vs profit deficit across the density skin. Excess
free energy per area, ρ(x) from ρ₀ to 0:
    σ = ∫ [ λ·(ħ²/8m)(ρ′)²/ρ + ρ·Δ(u) ] dx,   Δ(u) ≡ e(u) − e(1) ≥ 0
(the gradient term is the localization tax of a varying amplitude — the same
uncertainty bookkeeping as the swing-2 tax column; λ tabulated below). With the
capacity-point Δ(u) = τ_b u^{2/3} − C u + a_v (ν = 1): Δ(1) = 0, Δ(0) = a_v. ✓
EULER–LAGRANGE FIRST INTEGRAL (equipartition — theorem): λ(ħ²/8m)(ρ′)²/ρ = ρΔ ⇒
    σ = √(λħ²/2m)·ρ₀·J,   J = ∫₀¹ √Δ(u) du = 2.992 √MeV (computed; ν-sensitivity
    J = 2.34 … 2.99 for ν = 2/3 … 1),
    a_s = 4πr₀²σ = (3/r₀)·√(λ·ħ²/2m)·J = 34.1·√λ MeV.
FORCED: the equipartition structure, Δ(u) from the capacity point, J, and the
LIMITS of λ — filled-ladder gradient bookkeeping gives λ = 1/9; a lone amplitude
tail gives λ = 1 (both derivable statements about the tax of inhomogeneity; the
skin traverses both regimes). Hence
    a_s ∈ [11.4, 34.1] MeV  (λ ∈ [1/9, 1]);   fitted shadow 17.8 ⇒ λ_eff = 0.273,
INTERIOR — exactly where a two-regime skin must sit (dilute tail pushes toward 1,
filled interior toward 1/9; the profit-live inner skin dominates the weight).
STATUS, stated plainly: swing 3 promised the 3/2 → 1.13 softening coefficient;
the E-L instrument CLOSES the geometry (no free shape left — Δ is derived, J is
computed) and RELOCATES the one remaining unknown into λ: a pure localization-tax
coefficient for partially filled ladders. The question got smaller and sharper —
from "what is the surface?" to "what is the gradient tax of a two-regime skin?"
λ_eff derivation (self-consistent skin ladder) = named open instrument, swing 5.
No coefficient credit claimed beyond the derived bracket and interior position.

## 3. Census magnitude — the forced kinetic floor (booked, component one of two)
The filing ladder alone (two sense classes, double-filing ban, capacity-point
density): imbalance u = (N−Z)/A splits the ladder tops; expanding the tax column,
    a_sym^{ladder} = E_F/3 = 33.4/3 = 11.1 MeV — FORCED, import-free arithmetic.
Observed class (label a_A ≈ 23–24 MeV in the shadow's convention): the remainder
~12 MeV must sit in the CONTACT column via orientation-forcing (imbalance pushes
excess same-sense pairs into reversed-orientation meshes — the weak channel of the
dimer quartet). Structure forced; combinatoric coefficient OPEN (swing 5, with λ).

## Swing-4 scorecard
| item | status |
|---|---|
| saturation mechanism | THEOREM: kink at capacity; ν > 0.373 robust; no hard core |
| z two-route check | 4.5–5.3 (geometry) vs 4.78 ± 0.35 (energy) — no dial |
| surface structure | E-L equipartition + derived Δ(u); J = 2.99 √MeV |
| a_s | = 34.1√λ; bracket [11.4, 34.1] ∋ 17.8; λ_eff = 0.273 interior |
| open (named) | λ from two-regime skin; a_sym contact combinatorics; A^{-1/2}; θ_w |
