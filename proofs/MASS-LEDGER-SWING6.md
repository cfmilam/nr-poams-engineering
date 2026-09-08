# Mass Ledger — Swing 6: The Cluster Ladder (Enhancement Measured, Residual Named)
> **VOIDED CALIBRATION — corrected 2026-09-08.** The localization tax below used one power of
> \((1-1/n)\); Robertson requires the square for the stated intrinsic variables. Re-running the
> frozen gates gives **FAIL / PASS / FAIL**, and the corrected lower bounds are not interaction
> energies or a flat cluster anchor. Every dependent `PASS` or extraction below is historical,
> not current. Values remain verbatim; see the
> [canonical correction](../MASS-LEDGER-CORRECTION-2026-09-08.md).

**Follows:** swings 1–5. Registration T-C6 (ledger 5ff4541) committed BEFORE the run.
GROUNDING gate binding; labels tagged; imports named; fitting is the only sin.
Instrument: mass-swing6.py, run file mass-swing6-run.txt (AME2020 local, experimental).

## 1. The extraction (channel-weighted, swing-5 ledger)
Per cluster: δ₀ = (B + Σ_q τ_q + E_strain)/W with τ = (9/8)(ħ²/m)(1−1/n)/⟨r²⟩,
W = strong + γ·weak bond count (d: 1+0; t,h: 1+2γ; α: 2+4γ), γ = 0.85(5),
declared matter-radius bands, ρ = uniform-equivalent density.
    cluster   δ₀ (central [band])     ρ (fm⁻³)    z (coordination)
    d         14.31 [14.12, 14.49]    0.029       1
    h         14.07 [13.17, 15.07]    0.059       2
    t         16.81 [14.84, 18.39]    0.083       2
    α         17.70 [16.63, 18.42]    0.145       3
Bulk (for reference, swings 3–5): ρ₀ = 0.138, z = z_c = 4.78, frozen-mixing
requirement δ₀ = 22.3.

## 2. Scorecard — all six registered predictions PASS
- **T-C6a PASS:** all four central extractions in [13, 19]; full import bands
  inside [12, 20]. The four-channel ledger + tax column survive the cluster
  ladder jointly.
- **T-C6b PASS (three parts):** enhancement sign real —
  (i) δ₀(α) − δ₀(d) = **+3.39 MeV** (registered ≥ +1.5);
  (ii) mirror split δ₀(t) = 16.81 > δ₀(h) = 14.07 — the strain-swollen isobar
  extracts weaker, exactly the control the registration demanded;
  (iii) Spearman rank(δ₀, ρ) = +0.80 > 0.
- **T-C6c PASS:** δ₀(α) = 17.70 ∈ [16, 20] — **the in-medium enhancement is real
  but partial at cluster scale**; residual to the bulk-required value:
  22.3/17.7 = ×1.26.
- **T-C6d PASS (credit-free, famous):** B/A strict local maximum at A = 4 across
  A ∈ [2, 8] — including over Be-8 by 11.5 keV/quantum. Cell-closure direction.
- Readings (booked, not scored): A = 5 unbound vs α+n by 0.73 MeV (next-rung tax
  vs spare capacity; rung tax underived); Li-6 − (α+d) = +1.474 MeV (weak
  inter-cell net, small positive as read); Be-8 − 2α = −0.092 MeV (the two-cell
  problem, named open).

## 3. What the ladder settles about the ×1.55
Swing 5's recalibration said the bulk strong channel must be 22.3 MeV = ×1.55 the
free-cluster value if bulk mixing is frozen-random. The ladder now splits that
factor into measured parts:
- **×1.24 is measured** (d → α, 14.31 → 17.70) — and it is NOT a density effect
  at the top: the alpha already sits AT saturation density (ρ = 0.145 vs
  ρ₀ = 0.138) yet extracts 17.7, not 22.3.
- **×1.26 remains** between the densest cluster and the bulk requirement.
  Since density is exhausted, the residual variable is COORDINATION (z = 3 → 4.78)
  and/or the arrangement freeze at capacity.
**Named tension (new, on the record):** the frozen-random mixing factor is
(1+2γ)/4 = 0.675, but the bulk books (δ̄ = 2C/z_c = 15.02) against the
ladder-measured δ₀(ρ₀) = 17.7 imply a mixing factor 0.849 — between frozen
(0.675) and best-arranged (~0.94). Swing 5's a_sym assembly used the frozen
limit and landed +3%; the ladder now presses on that reading. The two books
must be reconciled by ONE mixing/coherence statement — swing-7 target #1.

## 4. Post-hoc observation — FLAGGED, unregistered, no credit
Against coordination z (not density), the extractions run
    z:  1     2      3     (4.78)
    δ₀: 14.3  15.4̄   17.7   22.3-required
— consistent with a near-linear coordination law δ₀(z) ≈ 14.3 + 2.1(z−1), whose
extrapolation to z_c = 4.78 gives 22.2 ≈ the bulk-required 22.3. If a
patch-sharing coherence law (each additional locked partner stiffens the
quantum's phase, raising every bond's gross) can be DERIVED from winding
bookkeeping, the frozen-mixing tension dissolves and the ×1.55 becomes the
z-law evaluated at capacity. Two-parameter line through four banded points =
exactly the Wyler shape — therefore: NOT claimed, derivation target only.

## Swing-6 scorecard
| item | status |
|---|---|
| T-C6a free-limit band | PASS (4/4 in window, bands inside) |
| T-C6b enhancement sign | PASS ×3 (gap +3.39; mirror control; rank +0.8) |
| T-C6c partial enhancement | PASS (17.70 ∈ [16,20]; residual ×1.26) |
| T-C6d cell-closure direction | PASS (strict max at A=4 over [2,8]) |
| ×1.55 decomposition | ×1.24 measured (saturates by α) · ×1.26 residual (coordination/freeze) |
| frozen-mixing vs ladder | NAMED TENSION — mixing factor 0.675 (assumed) vs 0.849 (implied) |
| δ₀(z) linear candidate | post-hoc, flagged, underived — swing-7 derivation target |


## Correction (2026-08-11, swing 7 — additive; original above stands as written)
The §4 line "δ₀(z) ≈ 14.3 + 2.1(z−1) … extrapolating to 22.2 at z_c" contains a
slope error: the ladder points give slope 1.69 (LSQ) / 1.70 (endpoints), not 2.1 —
the quoted line had been bent toward the famous endpoint, exactly what the flag
warned against. Honest extrapolation: 20.5–20.7. Swing 7 (registered run) scores
the loop closure on the BAND: 20.53 ∈ [19.97, 24.90] — PASS at the low edge; the
point-coincidence "22.2 ≈ 22.3" is withdrawn. See MASS-LEDGER-SWING7.md §4.


## Correction 2 (2026-08-11, swing 8 — additive; original stands)
The §2 mirror-control pass T-C6b(ii), δ₀(t) > δ₀(h), is DEMOTED to an import
artifact: the swing-6 radius bands compared two conventions (h from naive
charge-subtraction 1.75–1.82 vs t point-proton-flavored 1.54–1.68). On the
common matter band forced by the isospin-even matter operator (1.724 fm both,
unfolding declared in swing 8), the mirror pair UNIFIES: δ₀(h) = 15.19,
δ₀(t) = 15.10 — split 0.09 MeV, and the mirror binding difference is carried by
the strain entry (1.00 MeV) to 0.09 MeV residual. T-C6b(i)/(iii) re-verified on
the corrected ladder. See MASS-LEDGER-SWING8.md §1–3.
