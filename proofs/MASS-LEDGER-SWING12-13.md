# Mass Ledger — Swings 12–13: The Landing Attempt (Bulk Sector Rejected as Registered)
> **SUPERSEDED IN PART — corrected 2026-09-08.** This historical landing attempt inherits the
> failed cluster anchor and its pair/loop-credit decomposition. Its preserved failures remain useful
> controls, but no numerical `STANDS` statement that spends that chain is current. Values and scored
> outputs remain verbatim; see the
> [canonical correction](../MASS-LEDGER-CORRECTION-2026-09-08.md).

**Follows:** swings 9–11. Registrations 521f4ff / 880e176, each pre-run, with the
decision rule fixed in advance. Instruments mass-swing12/13{.py,-run.txt}.

## The composed claim under test
δ_bond = δ_pair + h + c₃·max(0, P₂−1) + c₄·P₃ with every constant from standing
imports (δ_pair = 14.02, c₃ = 2.34, c₄ = 0.876) plus one named import
(h = 0.84, defined at the trinucleon). Cluster sector already scored (pair 2%;
trinucleon; alpha 17.20 ∈ band). The landing = the bulk books: composed
δ_bulk ∈ [20.0, 24.9] at a census (P₂, P₃) of the capacity packing.

## Swing 12 — equilibrium hard-sphere census: VOID + FAIL-low
z̄ = 5.47 ∉ [4.3, 5.3] (void as registered). Census P₂ = 1.10, P₃ = 2.25;
composed = 17.1 — short by ~3 MeV even with chord-inflated P₃ (overcount, still
low: the fail is robust). Instrument note: snapshot print line mislabeled
columns (cosmetic); MEANS and scoring verified by hand.
Post-mortem, named: the census model omitted the lock physics itself — locks
are adhesive (T = 0 packing maximizes credits) and capacity caps the lock graph.

## Swing 13 — sticky anneal + capacity-capped mutual lock graph: VOID + FAIL-low
Corrected instrument (declared pre-run; same composed formula, nothing
re-tuned): sticky Metropolis (E = −bonds, T → 0.05) at fixed ρ₀, lock graph =
mutual 5-nearest-in-reach. Result: z_lock = 3.97 ∉ [4.3, 5.0] (void), P₂ = 0.43,
P₃ = 0.79; composed = 15.6 — **FAIL low, decisively.**
Post-mortem, named: at fixed box density the sticky system phase-separates into
clumps + voids (the toy adhesion lacks the tax pressure that enforces
saturation); in the clumps, mutual-nearest capping severs the very triangles
adhesion built. The two censuses missed the capacity graph in OPPOSITE
directions (5.47 / 3.97 vs z_c = 4.78).

## Verdict (per the pre-registered decision rule — honored, no rescue)
**The shared-turn loop ledger's BULK closure is rejected under both declared
censuses.** What this does and does not kill:
- STANDS (scored): the cluster sector — δ_pair = ħ²/4mr_q² (2%, parameter-free);
  the loop-credit quantum c₃ = 2.34 ≈ the measured marginal 2.55(20); the
  composition structure (first loop dependent — the cheap step); trinucleon and
  alpha within ~3% at one in-band r_q.
- REJECTED (scored): closing the bulk value 22.2 by counting 3- and 4-loops in
  a DISORDERED capacity packing. Neither census instrument could even produce
  the capacity graph (both void) — and within what they produced, the credits
  fall 3–5 MeV short.
- THE REAL SHAPE OF THE REMAINING PROBLEM, exactly stated: the bulk landing
  requires the STRUCTURE of the capacity packing itself — the T = 0 arrangement
  of circulations at ρ₀ under core + lock reach + patch capacity. That is not an
  afternoon toy-MC; it is the same object as swing 4's kink-profile prediction
  (the interior that meets ρ₀ at finite depth) and swing 5's frozen mixing. If
  the true capacity packing is polytetrahedral-ordered (P₂ ≈ 2.5–3.5), the loop
  ledger closes; if it is liquid-like (P₂ ≈ 1), the bulk deepening is not loop
  turns and the model's bulk sector is wrong. **The census question = the
  saturated-matter structure question.** One object, three fronts already
  pointing at it.

## Day scorecard for the crown (swings 9–13)
| attempt | verdict |
|---|---|
| rigid-pin spectrum | rejected (registered) |
| finite-pin spectrum | rejected 6/6 (registered) |
| shared-turn: pair anchor | **PASS 2% — parameter-free identification** |
| shared-turn: cluster sector | within ~3% with composition structure |
| shared-turn: bulk via census 1 | void + fail-low (registered) |
| shared-turn: bulk via census 2 | void + fail-low (registered) — sector closed today |
| crown | OPEN; contracted to the capacity-packing structure problem |
