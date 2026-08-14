# Pairing — The Gradient Layer at Next Fidelity (Swings X-5 … X-9)

**Date:** 2026-08-13. Registrations pre-run; every gate scored as hand-declared.
Chain: X-3 (exposure measured, `a92bf6e/ee66e98`) → X-4 (bounded paste, kill measured,
`5396a66/aa434ae`) → **X-5** (proper functional derivative, `445089e/0875f3f`) →
**X-6** (first-order energy booking, `9ddf43d/` + score commit).
Instruments: `madelung/pairing-swingX5{.py,-run.txt}`, `madelung/pairing-swingX6{.py,-run.txt}`.
Import unchanged and named throughout: μ = 10/81 (Sham→Antoniewicz–Kleinman lineage), κ = 0.804.

## What was asked

The Aufbau open item (1): does the d-collapse verdict (Sc flip at Z\* = 21) survive the
gradient layer at *proper* fidelity? X-4 answered at identification grade by **pasting**
F(s) onto the whole discount potential — the flip dragged to Z\* = 20/19. Two candidate
artifacts of the paste were named on the page: the proper functional-derivative treatment,
or the native hole shape.

## X-5 — the proper functional derivative (instrument-limit, booked)

The booked felt functional E[ρ] = −(3/4) m C_X ∫ ρ^{4/3} F(s) (whose F≡1 derivative is
*exactly* the baseline potential — structure check passed at 0.0e0) taken at its true
derivative: local part (F − sF′) plus the divergence term.

- **Structural finding that survives:** in the collapse-relevant region (s = 1.3–1.7 on the
  Z = 21 felt-floor profile) the proper **local part sits BELOW one** — (F − sF′) ≈ 0.90 —
  i.e. at derivative level the local piece points **opposite** to X-4's paste (F ≈ 1.17–1.25
  there). Whatever drags, it is not the local term.
- **Instrument limit, as pre-declared:** the divergence term (second derivatives of the
  deposit-grid density) runs 2.1–2.8× the local term with oscillating sign and wrecks every
  SCF cell (3d unbinds; no cell converges). The declared clause fired: **no verdict, no
  smoothing, no rescue.** The placement question rides entirely on a term this grid cannot
  evaluate honestly.

## X-6 — first-order energy booking (the honest fidelity in between)

The energy functional needs only first derivatives. At each deciding cell (Q, m): converge
the baseline SCF (booked tier3g chassis, untouched — fidelity gate passed, Z\* = 21 floor),
freeze it, build the two competing densities (core + one quantum in 4s vs in 3d), and price
the layer on each: dD = E_grad[4s-filling] − E_grad[3d-filling].

- **X-6b — direction: dD > 0 UNIFORM** across all claimable deciding cells (+0.033 … +0.100).
  The layer taxes the **4s filling harder** — X-4's drag **direction is confirmed** at energy
  fidelity. The paste-artifact hypothesis dies. (Consistent mechanism: the diffuse tail the
  enhancement concentrates on belongs to the 4s-heavy filling.)
- **X-6c — magnitude: the flip does NOT move at first order.** Effective Z\* = 21 at every m;
  at the felt floor's deciding cell (m = 1.50, Q = 20): D0 = −0.052, dD = +0.033,
  D1 = −0.018 — 4s holds.
- **X-6d — the honest boundary:** the two cells that *would* flip (m = 1.70, 1.949 at Q = 20)
  are excluded by the pre-declared |dD| > 5|D0| rule (12.7×, 24×): they are near-degenerate
  cells where |D0| ≈ 0 — **first-order booking is weakest exactly where the physics decides,
  by construction.** s > 3 saturation share 0.54–0.62 on both fillings (the bounded form is
  doing real work; no runaway).

## State of the item after the arc

The Sc/Ca placement stays **open and gradient-owned — now bracketed from both sides**:

| fidelity | treatment | verdict at felt floor |
|---|---|---|
| X-4 | paste (potential × F) | drags, Z\* → 20 |
| X-5 | proper derivative | instrument-limit (divergence term grid-unevaluable); local part alone points the other way |
| X-6 | first-order energy | direction of drag confirmed; magnitude insufficient — Z\* = 21 stands |

The deciding instrument is named: a **self-consistent smooth-density gradient chassis**
(spline/analytic density representation that can carry the divergence term), or the
**native hole shape** carried beyond the uniform census (deriving μ from the AXIOM-C kernel
itself, which would also retire the last import of this layer). Either is a fresh
registration.

## X-7 — the smooth-density chassis (2026-08-13 evening; `8a040fe/04ec95f`, construction fix `baed686`)

Natural cubic spline of ln ρ per SCF iteration; every layer quantity analytic off the spline
(no numerical differencing anywhere); validity clause: the verdict must converge AND agree
across the knot ladder {NG//12, NG//8, NG//5}, no knot chosen after the fact. Run 1's baseline
failed its own gate correctly (a construction bug — the baseline touched the spline; fixed and
booked, run-1 output kept). Rerun: **baseline reproduced exactly** (resid 0.000), and
**X-7b INSTRUMENT-LIMIT as declared** — with the layer on, no deciding cell converges at any
knot setting. The smooth representation cured the pointwise pathology (div share 0.07–0.16 at
r = 1, 4 a₀ vs the raw grid's 2.1–2.8 oscillating) but pockets remain (1.2 at r = 0.5, 2.6 at
r = 2), and the potential-iteration SCF is genuinely unstable under the divergence term's
feedback.

## State of the item after X-5/X-6/X-7

The bracket stands — paste drags to 20, first-order holds 21 — now with potential-iteration
instrument-limited at **both** raw and smooth density representation. The deciding instrument
narrows to: an **energy-variational treatment** (minimize E[ρ] directly; no v_x iteration for
the imported-μ layer), or the **native hole shape / native μ** (X-8: the census's own
second-order response, where count conservation resolves the Sham-vs-AK limit-order fork —
retiring the import changes the object itself). X-8 is the named next registration.

## X-8 / X-8′ / P2 / P3 — the native law (2026-08-13 evening)

**X-8** (`7d077bd/157881b`): the fork arbitrated inside the extant machinery — plane-wave PT,
determinant exchange. Chassis exact (E₀ to 0.000%, Lindhard to 0.03–0.14%), seven construction
iterations each pinned by a gate, and the LDA gate finally refused: the answer lives inside a
near-total cancellation the fixed-set quadrature cannot hold at small q. Booked instrument-limit
— the same structure that produced two published wrong answers in the extant record.

**X-8′** (`cbe2504/d61518f`, Star Lord's ontology reframe on the record): the native object —
a census filled to the E = 0 frontier under uniform tilt (the Airy thinning-census; same
admission license as H4/N-1, same fold machinery as N-4/N-5). Exactly solvable; the DM integral
factorizes; 46 s end to end. **X-2's uniform law emerges from the exact modes** (F = 1.0017 at
the deep gate). μ Taylor readout instrument-limited as declared.

**P2/P3** (`a37f638/5185afe/912c800`): difference-trick precision passes. P2's 2e-4 gate refused
at 2.3e-4 (chirp mismatch diagnosed); P3 decoupled the law from the μ chain, converged the
ladders (range < 2e-5, dt 1e-9), and found the structural fact: on the Airy family the
Laplacian content rides at fixed ℓ = s²/3, so station-local readouts measure μ + λ/3 — μ alone
needs an integrated observable or a second exact family (harmonic census). Named. **The law
itself landed at working grade**: F_nat = 0.90 / 0.71 / 0.49 / 0.29 / 0.15 / 0.08 across
s = 0.47 … 6.2 — **the same-sense discount shuts off at the thinning frontier** (surface-cut
exclusion hole), the OPPOSITE sign from the imported bounded form (which rises to 1.69 there).
Report-grade note, uninoculated: F·s drifts 0.60/0.54/0.50 at the evanescent stations.
Law exported (`native-gradient-law.csv`).

## X-9 — the d-collapse under the native law (`912c800/b651366`)

Same chassis as X-4, the law swapped. Baseline exact. **Under the native law at paste level the
diffuse 3d unbinds entirely** — the shut-off removes the tail exchange well the barely-bound 3d
rode on: feedback exactly opposite X-4's. Booked as found (the pre-named fourth branch).

## State of the item after the full arc

The placement question is **law-dominated at paste level in both directions**: the imported
paste drags the flip to 20/19; the native paste dissolves the question (3d unbound). Therefore
the local-multiplier paste class cannot carry either law faithfully for the Sc/Ca cell. What
stands: the **native thinning law itself** (working grade, exported, independent of any paste),
the first-order energy bracket, and the fully-derived uniform layer beneath it. The deciding
instrument is **mode-level pricing of the natively-measured law** — the discount priced per
mode-pair against the census it actually overlaps (X-10 class, fresh registration). The μ
Taylor coefficient remains open at instrument grade (integrated observable or harmonic-census
family named); the κ import is already superseded by the measured law wherever the law is used.
