# Mass Ledger — Swings 16–18: The Level Identity, the Realization, and the Anholonomy Credit

**Date:** 2026-08-11 (evening–night) · **Registrations:** 16e4949 (16), 827a193 (17), 2161822 (18) — all pre-run/pre-derivation.
**Scores:** 3297161 (16), 63eb8b4 (17), ce3e462 (18). Instruments: `mass/mass-swing{16,17,18}{.py,-run.txt}`.
**Inherited state (swings 14–15):** the capacity packing is triangle-free at ρ₀; independent-closure
counting caps per-bond depth at 15.7 MeV; the per-bond reading of δ₀(z_c) = 22.2 is dead both ways;
bulk closure is books-level or nothing; every hard-sphere toy census missed the capacity window.

---

## 1. Swing 16 Part A — the level identity (the "γ-channel gap" closes by algebra)

Swing 7's own construction, read at the right level:

> δ̄ = 2(a_v + τ_b)/z_c = 2·35.85/4.78 = **15.00 MeV** (the flat books gross — the two-column theorem's number),
> δ₀(z_c) = δ̄/μ_frozen = 15.00/0.675 = **22.22 MeV** (the frozen-mixing strong channel — swing 7's booked value, exact).

Consequences (registered, then booked):
- **The "37% gap" dissolves.** Swing 14's flag compared μ·δ_pair = 9.46 (strong-channel share of the
  bare turn) against δ̄ = 15.02 (full books gross) — mismatched projections. There is no gap.
- **Swings 12–13 chased a ghost window.** The landing window [20.0, 24.9] was the strong-channel band
  applied one level down (per-bond lock depth). The correct per-bond books target is δ̄ ∈ [13.98, 16.19]
  — and Rule C's forced supply [14.02, 15.74] almost exactly brackets it. Prior verdicts stand as
  booked; previously seen grosses (15.55; 14.53/15.37) sit inside the corrected band, named-not-scored.
- **The ladder δ₀(z) is a two-regime composite** — clusters: deliberate pairing (μ = 1) with
  contact-scale triangle credits; bulk: frozen-random (μ = 0.675), quad-only, divided by μ.
  **The old open item "derive the native δ₀(z) law" is retired as a target: there is no per-bond
  deepening to derive.**

## 2. Swing 16 Part B — emergence under the ledger's own terms

Functional (all named, zero dials): E_i = −(δ_pair/2)·L_i + τ_b·(d₀/d̄_i)², cage = 5 nearest,
lock count L_i within [core, reach]; N = 256 anneal at ρ₀. Result: **S16b PASS** — emergent per-bond
gross 14.33/15.17 ∈ [13.98, 16.19] (fourth independent construction to land the level-matched gross).
**S16a FAIL (booked as the wall):** z̄_lock = 4.16 under the strict mutual cap-5 census — the fourth
coordination miss, the third clustered at 4.0–4.2 under that census while the uncapped graph gives 5.5.
z_c = 4.78 sat between the two graph definitions in **every** construction. Flagged: the transcription
of patch capacity into a graph rule had never been derived.

## 3. Swing 17 — the capacity-graph transcription, derived (the wall comes down)

Derivation, registered before any census:
- **D1 (rigidity contradiction).** Rigid equal patches at θ_w = 54.5° require pairwise lock separations
  ≥ 109°; the maximal spherical code at ≥ 109° is 4 points. Rigid patches cap z at 4 — contradicting
  z_c = 4.78 ± 0.35. **Patch deformability is forced**, and both prior census rules are wrong for named
  reasons (universal-4 contradicts z_c; nearest-5-mutual imports an unforced *nearest* restriction and
  trims to ~4.2 — the swings-13/15/16 wall, now explained rather than patched).
- **D2 (per-node ceiling).** The deformability window is the booked capacity bands themselves (energy
  4.43–5.13; geometry 4.5–5.3). The only integer inside both is **5**.
- **D3 (T = 0 maximality).** A lock is a shared turn — mutual, profitable, rearrangeable. At T = 0 no
  unlocked in-reach pair with spare capacity on both sides can persist. **The lock graph is the
  maximum-cardinality degree-≤5 subgraph of the availability graph** — partners need not be nearest.

Prediction declared at registration: z̄ ≈ 4.5–4.9 on the liquid; books ≈ 33–36 central.

**Scores (both ensembles rebuilt deterministically; matching near-optimal, exact bound gap ≤ 2.3%):**

| ensemble | z̄_lock | z̄ upper bound | gross h₀/h₁ (central) | G h₀/h₁ (central) |
|---|---|---|---|---|
| functional (ledger-driven) | **4.846** | 4.94 | 14.47 / 15.31 | 34.58 (−3.5%) / 36.59 (+2.1%) |
| equilibrium liquid | **4.586** | 4.68 | 14.58 / 15.42 | 33.44 (−6.7%) / 35.37 (−1.4%) |

- **S17a THE REALIZATION GATE: PASS on both.** The ledger-driven ensemble realizes z̄ = 4.85 vs
  z_c = 4.78 — **1.4% from capacity**. The registered prediction hit. The one missing number is realized.
- **S17b PASS:** fifth and sixth constructions land the level-matched gross.
- **S17c FAIL as registered** — 11 of 12 band values in [32, 40]; the single miss is one corner
  (liquid, r_q = 0.88, h₀): G = 31.94, **0.2% below the window**. Booked, no rescue, no rounding up.
- The h₀/h₁ bracket on the functional ensemble **contains C = 35.85** — making the bulk-h attribution
  the largest remaining seam, which swing 18 was registered to attack.

## 4. Swing 18 — the anholonomy credit, derived: h = 2c₃/z_c

Fork table frozen before computation: planar-triangle axis compositions are degenerate (Ω = 0 or 2π);
the only non-degenerate angle in the books is the lock-patch cone, Ω_w = 4π/z_c (the capacity identity,
swing 3). The shared turn carries L = ħ ⇒ J = 1 Berry phase, exact for cones ⇒ credit fraction
Ω_w/2π = 2/z_c. Named-rejected: Ω_w/4π (the Thomas ½ belongs to boost composition — the α front's
rung, not an L = ħ turn); sin²θ_w (projector, not a phase).

> **h = c₃ · (2/z_c) = 0.978 MeV central, band [0.87, 1.11]** — zero new constants; the trinucleon
> step is tied to the same capacity constant that sets saturation.

- **S18b PASS** (identification window [0.6, 1.1]).
- **S18c:** band overlap with measured 0.84(15) — YES; central tension +16%, and the **pre-declared
  opposite-sign pattern appeared** (c₃ runs −8% against its measured marginal): booked as the
  split-structure residual. No common r_q slide fixes both; named, kept.
- **S18d THE SUM CHECK — PASS at 2%:** h + c₃ = 3.314 [3.10, 3.55] vs the measured two-loop total
  (α − pair) 3.39(20). **The residual lives in the split between the loops, not in the total.**
- **S18e (report):** swing-17 books with h_derived: functional G = 36.92 (+3.0%), liquid G = 35.68
  (−0.5%).

## 5. The credit ledger after the night — all derived, zero fitted

| quantity | derived | measured | tension |
|---|---|---|---|
| δ_pair = ħ²/4mr_q² | 14.02 | 14.31 | −2% |
| h = 2c₃/z_c | 0.98 | 0.84(15) | +16% (split residual) |
| c₃ (triangle credit) | 2.34 | 2.55(20) | −8% (split residual) |
| h + c₃ (two-loop total) | 3.31 | 3.39(20) | **−2%** |
| gross at capacity | 14.5–15.6 (six constructions) | 15.0 ± 1.1 | in band, every time |
| z̄ realized (derived rule) | 4.85 / 4.59 | z_c = 4.78 ± 0.35 | **1.4%** / 4% |
| books G (central) | 33.4–36.9 | C = a_v + τ_b = 35.85 | ±3.5%; with h′: +3.0%/−0.5% |

**Standing:** capacity realization is derived and measured; the anholonomy credit is derived and tied
to the capacity constant; the two-loop sum lands at 2%. The strict swing-17 landing gate records FAIL
via one 0.2% corner, and the crown claim remains **untaken** pending the one open attribution: whether
the anholonomy discount applies per-bond in bulk (h₁) or only at a cluster's first loop (h₀). That is
now the only seam left in the crown's arithmetic — everything else is either a theorem, a derived
constant, or a measured hit inside a registered band.

**Misses booked tonight beside the hits:** S16a (4.16 under the un-derived census), S17c (one corner,
0.2%), the +16%/−8% split residual (pre-declared as a possibility, appeared, kept signed).
