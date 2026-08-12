# Mass Ledger — Swings 14–15: The Geometry Answer and the Independence Rule

**Date:** 2026-08-11 · **Registrations:** fdcf31e (swing 14), 0c7be63 (swing 15) — both pre-run.
**Scores:** b8088e0 (swing 14), 0af5482 (swing 15). Instruments: `mass/mass-swing{14,15}{.py,-run.txt}`.
**Question inherited from swings 12–13:** what census does the T = 0 capacity packing carry, and do
the shared-turn loop credits close the bulk ledger?

---

## 1. Swing 14 — the enumeration: capacity packing is TRIANGLE-FREE

Enumeration of ordered candidates at ρ₀ = 0.138 fm⁻³ (core 1.72 fm, reach band 2.06/2.14/2.22 fm):
sc, bcc, fcc, hcp, A15, diamond, plus contact-scale local references (tetrahelix, icosahedral-13).

**Findings (all as registered):**
- **fcc/hcp do not bond at ρ₀** within central reach (NN 2.172 fm vs 2.14) — saturation density sits
  1.5% outside close-packing's lock reach. Flagged as a suspicious near-coincidence, unclaimed.
- **S14b answered: P₂ = 0 for every feasible homogeneous candidate at central reach.** Mean spacing
  1.94–2.14 fm at ρ₀ forbids mutual-contact triples. Contact triangles exist only in contact-scale
  local order (tetrahelix P₂ = 3, icos13 P₂ = 3.6), which cannot fill space at ρ₀.
  **The polytetrahedral route is closed. Bulk deepening is not 3-loop turns.**
- S14c FAIL all candidates (sc 43.9 / bcc 60.6 / fcc@2.22 ≈ 98 vs [32, 40]).
- **S14d triggered as registered:** the composed formula's linear extension to dense graphs is
  REJECTED — raw P₃ counts constraints that are not independent (chord/multiplicity inflation).

The cluster sector is untouched: cluster bonds sit at contact separation (~1.75 fm) where triangles
are feasible; the bulk sits at ρ₀ spacing where they are not. **The triangle→square crossover is
forced by geometry, not chosen.**

## 2. Swing 15 Part A — Rule C, the independent-closure rule (derivation)

Loop credits may charge only **independent** closure constraints: elements of the lock graph's cycle
space, dimension β₁ = E − V + n_comp. Basis taken shortest-first (minimum cycle basis): triangle
rank T, then chordless-quad rank Q, residue R = β₁ − T − Q (longer closures; zero primary credit).

**Theorem (any lock graph):** connected ⇒ β₁/E < 1 ⇒ per-bond credit < c₄ = 0.876 MeV ⇒

> per-bond depth ≤ δ_pair + h + c₄ = **15.73 MeV < 20.0**.

Consequences, registered before any count:
1. The swing-14 square-route lead (δ ≈ 22.3 needs P₃_indep ≈ 8.5 per bond) is **impossible under
   independence — retired.**
2. Combined with S14d, the per-bond deep-mesh reading of δ₀(z_c) = 22.2 is **dead both ways**:
   dependent counting is rejected overcounting; independent counting cannot reach the window.
3. δ₀(z_c) = 22.2 is a **decomposition-level quantity** (frozen-mixing strong channel, swing 7),
   not a per-bond mesh depth. The raw per-bond gross is near-flat (~14–16 MeV) across the ladder —
   consistent with the bare shared turn δ_pair = ħ²/4mr_q² = 14.02 plus sub-c₄ loop credits.
4. Bulk closure, if it exists, is **books-level**: G = min(z̄, z_c)/2 · gross_bond, with gross_bond
   forced into [14.02, 15.74] and the required value C/(z_c/2) = 35.85/2.39 = **15.00 sitting inside
   the forced bracket**. Zero freedom beyond the named bands (r_q, z_c).

## 3. Swing 15 Part B — the census (instrument, scored as registered)

Physical candidate: capacity-capped equilibrium liquid (swing-12 construction + swing-13 mutual
CAP = 5 rule; declared the third and FINAL hard-sphere census). References: sc, bcc periodic at ρ₀.

| graph | z̄ | β₁/E | T | Q | R | G_h₀ | G_h₁ | vs C = 35.85 |
|---|---|---|---|---|---|---|---|---|
| sc (ref) | 6.00 | 0.668 | 0 | 430 | 3 | 34.89 | 36.90 | −2.7% / +2.9% |
| bcc (ref) | 8.00 | 0.751 | 0 | 748 | 3 | 35.07 | 37.08 | −2.2% / +3.4% |
| capped liquid (physical) | **4.22** | 0.527 | 193 | 108 | 269 | 30.65 | 32.42 | −14.5% / −9.6% |

(central r_q = 0.86; full band 0.84–0.88 spans 33.3–38.8 for the references, all in-window.)

**Gates:**
- **S15b VOID** — z̄ = 4.22 ∉ [4.3, 5.3]. Third miss of the capacity window by hard-sphere toys
  (5.47 uncapped / 3.97 sticky / 4.22 capped; z_c = 4.78 sits between the uncapped liquid and every
  capped construction). **The hard-sphere toy class is closed by rule — no fourth census.**
- **S15c FAIL** (and void) — booked, no rescue. Census composition is the informative part:
  in the disordered toy ~47% of the cycle space sits in closures longer than 4 (zero primary
  credit); **disorder wastes closure**. Ordered packings put ≥99% of β₁ in quads (R = 3, pure
  toroidal homology) — order maximizes creditable closure.
- **S15d (report-only):** every ordered feasible candidate books in-window under both anholonomy
  variants across the full r_q band — central precision ±3.4% or better, with zero fitted numbers.
  The capacity cap min(z, z_c)/2 makes the books nearly candidate-invariant across ordered packings.
  Registration hand-estimates confirmed exactly.

## 4. Verdict

**The crown is reframed, not landed.**
- Theorem-grade (stands regardless of any instrument): bulk deepening is **not** per-bond loop
  turns; 22.2-per-bond is dead both ways; the bulk ledger closes at books level or not at all.
- Consistency (ungated): C = a_v + τ_b = 35.85 ≈ (z_c/2)·(δ_pair + basis credits [+h]) within
  ±3.4% central on ordered references — every number named, none fitted.
- The gated landing FAILED on the declared physical toy, and the toy class is exhausted.
  **Swing 16's instrument must be the ledger's own energy functional** (capped contact profit +
  uncertainty tax at fixed μ): the capacity structure must emerge from the same books it feeds.
  Also queued: the γ-channel reconciliation (frozen-random bare turns 9.5 vs required gross 15.0).

**Standing after the day:** cluster sector intact (pair anchor 2%, c₃ ≈ measured marginal,
composition structure); 10 candidate classes now excluded with instruments on record; every score
of swings 9–15 landed exactly as registered — misses booked beside hits.
