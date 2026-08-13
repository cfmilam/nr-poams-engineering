# Pairing — The Gradient Layer at Next Fidelity (Swings X-5, X-6)

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
