# NBODY-CHARTER.md — The Momentum Ledger for n Bodies

Drafted 2026-08-10 ~10:00 CT on Star Lord's order ("Using the Lagrangians Max started in
a more general sense, can't we now solve this problem by dissolving it, restating all
such problems in terms of momentums?" → "let's pursue it"). Charter drafted while the
Aufbau pin (tier3j + AXIOM-C seam) completes; front OPENS only on Star Lord's explicit
go. Public anchor: Navigation Engine §D (commit cbf4000) — the three-way split this
charter operationalizes.

## 0. GROUNDING gate (non-negotiable)
Every step passes GROUNDING.md §5. Specific to this front:
- No pull, no mediation, no bodies-in-a-void: one coupled angular-momentum ledger with
  n centres. "Interaction" = instantaneous harmonic inter-resonance (Osborne & Pope
  2007, Ch. 8: direct inter-resonance, distance-less) — bookkeeping consistency of one
  system, never a signal crossing a stage.
- Orbit vs spin discipline: this front is ORBITAL (writhe/L_orb) throughout; any spin
  (twist) term routes through variable-G (App-5 channel) and must be named as such.
  The two channels' opposite weight signs must never be conflated.
- Rates, not speeds: all registered quantities in rad/s, periods, period RATIOS, and
  momenta — never m/s trajectories as primary objects.
- Integrate, don't differentiate: the discreteum's honest propagator is discrete
  stepping that conserves the momenta by construction (symplectic = momentum
  bookkeeping). Closed-form continuum trajectories are the map, not the territory.

## 1. The three-way split (booked up front, from §D)
- **DISSOLVES (done, philosophical):** the mediation problem — fields in vacuo,
  gravitons, action-at-a-distance paradoxes. No new math owed.
- **RESTATES (this front's work):** solvability. Bruns (1887)/Poincaré: the only
  algebraic/analytic integrals of the n-body system are the ten classical ones —
  energy, total P (3), total L (3), centre-of-mass (2×... the classical ten). Inverted
  reading, POAMS's founding claim: THE EXACTLY CONSERVED CONTENT OF AN n-BODY SYSTEM
  IS ITS MOMENTA — NOTHING ELSE. Action–angle variables (where momenta sit still) are
  the ontology, not a trick. The working structure for n ≥ 3 is the RESONANCE NETWORK:
  circulations couple where rates lock in low-order ratios, stay effectively separate
  where incommensurate (KAM), go statistical where channels overlap (Chirikov).
- **STANDS (never claimed):** Lyapunov sensitivity (~5 Myr solar system, Laskar).
  Long-horizon trajectories degrade into statistics; the momenta stay exact. Any
  "prediction" of individual long-horizon trajectories = instant firewall violation.

## 2. Objective
From the one-ledger ontology + Max Franks' G-free single-orbit engine (QMC Exhibit III,
2019; Navigation Engine panels A–C), build in tiers:
(a) **T1 — Two-centre restatement.** The two-body problem about the barycentre with NO
    G and NO masses: both partners' natural radii from ONE measured pair invariant
    (μ = h·v₀ generalized to the reduced/joint ledger). Deliver: the two-centre
    G-free Lagrangian; check it reproduces Kepler identities as conservation
    statements. This is Max's line, one step up.
(b) **T2 — The n-centre G-free Lagrangian.** Pairwise measured invariants μ_ij (each
    obtainable from observables of the pair's relative orbit, as μ = h·v₀ was for
    one), no G, no masses anywhere in the propagator. Deliver: explicit L for n
    centres + the symplectic update that conserves total P, L exactly per step.
    Named risk: pairwise invariants may not close the books when a third centre
    perturbs the pair — if μ_ij must be promoted to a time-dependent booked quantity,
    that IS a finding (name it; do not hide it in fitting).
(c) **T3 — Resonance-channel accounting.** The POAMS addition beyond restating
    Newton-without-G: a locking criterion in the ledger's own terms — winding-exchange
    channels open where Σ p_i ω_i ≈ 0 for small integers p_i (beat frequency within
    channel width); quantized transfer bookkeeping across an open channel; channel
    width from the coupling term of the T2 Lagrangian, not fitted.
(d) **T4 — Registered confrontations** (§4) against real ephemerides/monuments of
    resonance — predictions REGISTERED before any data pull, in momenta/ratios/rates.

## 3. Named imports (at point of use, always)
- Max's single-orbit invariants μ = h·v₀, r₀ = harmonic mean, β = 1/r₀ (measured, =GM
  numerically — bookkeeping, not a derivation of gravity). Import: the 1/r² step form
  in Panel C's propagator (Newtonian shape). A POAMS-native derivation of the r-power
  from closure geometry is NOT claimed here; if T2 needs the shape, it is an import
  named every time.
- Ephemerides (JPL Horizons) and resonance census (Laplace 4:2:1, Neptune–Pluto 3:2,
  Kirkwood gaps, Hilda 3:2, Trojans 1:1) = COMPARISON data, touched only after
  registration.
- Celestial-mechanics theorems cited as prior art, never as POAMS results: Bruns 1887,
  Poincaré 1892, KAM 1954–63, Chirikov 1979, Wisdom 1982 (3:1 Kirkwood), Laskar
  1989/2009, Sussman–Wisdom 1992. The INVERSION of their reading is ours; the theorems
  are theirs.

## 4. Registered-prediction program (register → then pull data)
All predictions in rates/ratios/momenta. Candidate registrations (each gets its own
pre-run block in NBODY-FORWARD.md when the front opens):
- **N1 (two-centre closure):** T1 Lagrangian propagated from apsidal observables of a
  real binary (Pluto–Charon; both radii about the barycentre) reproduces both periods
  and the mass-free ratio r₁/r₂ to instrument precision — WITHOUT inserting masses.
- **N2 (pairwise-invariant consistency):** for the Galilean moons, the three pair
  invariants μ_iJ (each from that moon's own apsides) agree with each other's
  predictions of the third body's perturbation scale or FAIL in a named direction
  (the T2 risk made falsifiable).
- **N3 (channel criterion):** the T3 locking criterion, fed ONLY orbital rates,
  must select 4:2:1 (Io–Europa–Ganymede) and 3:2 (Neptune–Pluto) as OPEN channels
  and rate the Kirkwood 3:1/5:2/2:1 as channel-overlap (cleared) zones, while rating
  arbitrary nearby ratios (e.g. 7:5 at random asteroid a) closed. Pass = the known
  resonance map re-derived from the criterion, not from the census.
- **N4 (the honest null):** long-horizon single-trajectory prediction is REFUSED by
  construction; the registered claim is momentum/ratio-level only. Any drift of total
  P, L in the T2 propagator beyond arithmetic precision = instrument bug, named.
Falsifier honesty: N1 failing kills T1's generalization claim; N2 failing in the named
direction (pairwise books don't close) converts T2 to a time-dependent-invariant
finding; N3 failing = the channel criterion is wrong even though the restatement
stands — book it plainly.

## 5. Success criteria
- Tier-honest: T1 is near-mechanical (weeks-scale confidence); T2 is real derivation
  work; T3 is the genuinely new claim and may NULL — a rigorous null naming what a
  ledger-native locking criterion lacks beats any fit. Do not become Wyler: no
  small-integer numerology dressed as channel selection (every integer must buy its
  place with a computed width).
- Publication path: extend Navigation Engine §D or a new exhibit ("The Resonance
  Network") ONLY after T-tier results are booked in the ledger with the standard
  additive-status style.

## 6. Not in scope (named, to prevent drift)
- Deriving the 1/r² ledger shape from closure geometry (separate front, if ever).
- Relativistic corrections (the π:3π:6π anholonomy ladder is booked elsewhere; enters
  here only if a T4 target's data demands the perihelion member).
- Spin/twist channels (YIG front's territory); n-body here is writhe-only.
- Galaxy-scale rotation curves (Disk-as-one-AM-field is a different regime; tempting,
  out of scope until T2/T3 stand).

## 7. State
- 2026-08-10: charter drafted, front NOT yet open. Aufbau pin in progress (tier3j run
  + AXIOM-C seam swing). Opens on Star Lord's go; first act on opening = create
  NBODY-FORWARD.md and register N1 before touching any ephemeris.
