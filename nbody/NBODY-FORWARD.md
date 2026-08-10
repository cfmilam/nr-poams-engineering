# NBODY-FORWARD.md — The Momentum Ledger: forward computations

Front OPENED 2026-08-10 ~14:10 CT on Star Lord's conditional go ("If it's all clean,
then we move to n-body" — the Madelung queue closed clean: census-flow exhibit live,
tier3m/n booked, consolidated theorem record shipped). Charter: NBODY-CHARTER.md —
its GROUNDING gate, three-way split, named imports, and firewall govern everything
here. Public anchor: Navigation Engine §D.

## 0. Discipline reminders (from the charter, binding)
- Registration BEFORE any ephemeris/data pull. Predictions in rates/ratios/momenta.
- No G, no masses anywhere in the engine. Every import named at point of use.
- Long-horizon single trajectories are REFUSED by construction (Lyapunov honesty).
- A rigorous null naming the missing piece beats any fit.

## 1. T1 — the two-centre restatement (derivation target, stated before work)
Two circulations about a common barycentre; one ledger, two centres. Max's
single-orbit engine (Navigation Engine A–C) reads a orbit's invariants off its own
apsidal observables: v₀ = ½(v_a+v_p), r₀ = harmonic mean(r_a, r_p), μ = h·v₀.
T1 applies this to the SEPARATION (relative orbit) of a pair, plus one partition
datum, and must deliver — with no G and no masses:
(a) the pair invariant μ_rel = h_rel·v₀_rel from separation observables alone
    (numerically = the Newtonian G(M₁+M₂), obtained strictly by measurement);
(b) the period of BOTH partners = the separation period, from μ_rel and the
    separation's natural radius (Kepler identity as conservation statement);
(c) the barycentric partition: each partner rides a scaled copy of the separation
    ellipse; the scale fractions f₁ + f₂ = 1 are constant along the orbit (ledger
    partition read from ONE measured barycentric radius, not from masses);
(d) each partner's speed amplitude v_i = f_j · v_rel (i≠j) and both barycentric
    apsidal radii.
Named import (charter §3): the 1/r² step shape inside the propagator (Newtonian
form) — imported, not derived, named every time it is used.

## 2. N1 REGISTRATION (2026-08-10 ~14:10, BEFORE any data pull)
Two real binaries, one near-circular (clean doubles check) and one eccentric (real
apsidal-machinery check). INPUTS allowed per target: the separation's apsidal
distances (r_a, r_p), ONE separation apsidal speed (v_a or v_p; the other comes from
AM conservation), and ONE partner's barycentric semi-major axis (the partition
datum). Everything else is PREDICTION.
- **N1a — Pluto–Charon (near-circular):** from {r_a, r_p, v_a(sep), a₁(Pluto about
  barycentre)} predict: (i) the orbital period; (ii) Charon's barycentric semi-major
  axis a₂ = a_sep − a₁; (iii) both partners' orbital speed amplitudes.
  PASS = all within 1% of published values (data-quality bound; the system is nearly
  circular so v_a ≈ v_p — registered as the weak-apsidal case on purpose).
- **N1b — Earth–Moon (eccentric, e ≈ 0.055):** from {r_a, r_p, v_p(sep), a₁(Earth
  about the Earth–Moon barycentre ≈ 4.67e3 km — the partition datum)} predict:
  (i) the anomalistic-month-scale period (tolerance 1.5% — the lunar orbit is
  strongly solar-perturbed; the residual IS the three-body signal T2 must own);
  (ii) the Moon's barycentric apsidal radii; (iii) perigee/apogee speed ratio =
  r_a/r_p (pure AM conservation — must land at data precision, < 0.1%).
- Pre-named failure meanings: (i)-class misses beyond tolerance = T1's generalization
  wrong as constructed (book loudly); N1b(i) missing by ~1% in the KNOWN direction of
  solar perturbation = not a failure but the registered handoff to T2 (the pairwise
  books don't close at three bodies — the charter's named risk made visible).
- Data source (to be pulled ONLY after this registration is committed): JPL/NASA
  published orbital elements; exact values quoted with retrieval date in the results
  section.

## 3. Queue after N1
T1 writeup (the two-centre G-free Lagrangian, explicit) → N2 registration (Galilean
pair-invariant consistency — the T2 risk falsifiable) → T3 locking criterion
derivation (resonance channels from the coupling term, no fitted widths) → N3
(channel criterion vs Laplace 4:2:1, Neptune–Pluto 3:2, Kirkwood) — each with its own
pre-committed registration.

## N1 RESULTS (run1, 2026-08-10 ~13:40 CT; data retrieved same hour, provenance in
## nbody-n1.py header; declared input deviations named there — registration 88acc0a)
- **The engine's central claim lands at 1e-4:** the pair invariant μ_rel = 4π²a³/T²
  measured from Pluto–Charon's separation geometry + period alone — no G, no masses
  anywhere — agrees with the comparison GM_P+GM_C (Brozović 2024) to 0.01%
  (975.4 vs 975.5 km³/s²). Geometry identity: a_sep, e reproduce the published
  elements to all quoted digits.
- **N1a FINDING (the partition arithmetic catches a published data error):** the
  source infobox's a₂(Charon, barycentric) = 17,181.0 km is internally inconsistent
  with the SAME infobox's mass ratio — the engine partition gives a₂ = 17,464 km
  (17,181 is 1.62% low); the infobox's "0.21 km/s" speed note matches neither
  partition (196/199 m/s; 2 s.f., too coarse to adjudicate). Independent GMs side
  against 17,181. The registered 1% scoring of (ii)/(iii) is therefore VOID AGAINST
  SELF-INCONSISTENT REFERENCE DATA (pre-named data-quality bound) — booked as a
  data-adjudication instead. Declared input-swap (period as precision datum) stands
  as named in the run header.
- **N1b (i) PASS:** period PREDICTED 27.000 d from {r_p, r_a, v̄₂ = 1.022 km/s,
  a₁ = 4,670 km} via the mean-speed relation (no T, no G in the engine) vs sidereal
  27.322 d = 1.18% — inside the registered 1.5%, and the miss's size and direction
  are the REGISTERED THREE-BODY HANDOFF: the solar perturbation contaminates the
  mean-speed datum / lengthens the real month; the pairwise books close only to ~1%
  at three bodies. THE RESIDUAL IS NOW EMPIRICALLY SIZED — T2's first target.
- N1b (ii) on record: Moon barycentric apsides 358,886/400,581 km; Earth's monthly
  wobble amplitude v₁ = 12.6 m/s (matches the classic figure). (iii) apsidal speed
  ratio = r_a/r_p = 1.11618 — engine identity; no independent published apsidal-speed
  pair in the consulted sources (noted, not scored).
- **T1 verdict: STANDS.** The two-centre restatement computes real binaries with no
  gravitational constant and no masses; its one deliberate blind spot (three-body
  exchange) shows up exactly where and how the charter predicted. Next: T1 Lagrangian
  writeup + N2 registration (Galilean pair-invariant consistency).

## T1 WRITEUP — the two-centre G-free engine, explicit (2026-08-10 ~14:20)
**The exactness theorem (two lines, proved in-session 2026-08-10 morning).** For any
ellipse: h = r_p v_p, v₀ = ½(v_a+v_p) = ½v_p(r_a+r_p)/r_a; vis-viva gives
v_p² = μ r_a/(r_p a) with 2a = r_a+r_p ⇒ h·v₀ = ½ v_p² r_p (r_a+r_p)/r_a = μ exactly.
So Max's measured invariant μ = h·v₀ IS the pair invariant — identically, not
approximately. Equivalently μ = 4π²a³/T². No G, no masses, ever.
**The Lagrangian (mass-free form).** One ledger, two centres; separation R = r₂ − r₁:
    ℒ_pair = ½|Ṙ|² + μ/|R|        (μ measured; per-unit-ledger-weight form)
    barycentre: R_B free (Ṙ_B = const — total-momentum conservation, kinematic)
    partition map (exact, kinematic): r₁ = R_B − f₁R,  r₂ = R_B + f₂R,
    f₁ + f₂ = 1, f_i constant along the orbit.
The partition fraction f is the pair's MOMENTUM-LEDGER SPLIT: a measured, dimensionless
number (one barycentric datum fixes it). In Newtonian language it is the mass ratio;
the engine never performs that conversion — masses appear nowhere. Consequences
(immediate): both partners share the separation period; each rides a scaled copy of
the separation ellipse (a_i = f_i a_sep, r_i^{peri/apo} = f_i r_{p/a}); speed
amplitudes v_i = f_i v_rel. All N1 predictions were these three lines.
Named import (every use): the 1/R step form of the pair term (Newtonian shape) — the
ledger's radial law is imported, not derived, at this tier.

## N2 REGISTRATION (2026-08-10 ~14:25, BEFORE any Galilean data pull)
Target: pair-invariant consistency at Jupiter — the first genuinely n-body-sensitive
ledger reading, and the T2 risk made falsifiable.
Inputs per moon i ∈ {Io, Europa, Ganymede, Callisto}: published a_i (planetocentric
semi-major axis) and T_i (sidereal period) ONLY. Engine: μ_i = 4π²a_i³/T_i² per pair
(Jupiter, moon_i) — four independent no-G no-mass invariants.
- **N2a (books close):** spread(μ_i) ≡ (max−min)/mean < 5×10⁻⁴. Pre-named data-hygiene
  branch: if spread > 5e-4, FIRST diagnose frame/epoch inconsistencies in the
  published a_i (planetocentric vs barycentric, mean vs osculating) before any physics
  claim.
- **N2b (the ledger reads the partner's weight):** the residuals δμ_i about the
  common mean rank-order with the moons' partition fractions (published moon/Jupiter
  mass ratios ~ 2–8 ×10⁻⁵, COMPARISON ONLY, never input): Ganymede highest, then
  Callisto, Io, Europa. Pass = exact rank match (4! = 24 orderings; chance 1/24).
  This tests μ_i = μ_J(1 + partition_i) — the pairwise invariant carrying the
  partner's ledger weight.
- **N2c (the open channel, empirically):** the Laplace combination of mean motions
  n_Io − 3n_Eur + 2n_Gan, computed from the fetched T_i: registered |combo|/n_Io
  < 1×10⁻⁵ — a lock DEEPER than anything the four independent pairwise books
  constrain (nothing in T1 relates the three periods). Callisto = out-of-lock
  control. This is the measured signature of an OPEN INTER-RESONANCE CHANNEL —
  T3's object, sized before T3 exists.
Falsifier honesty: N2a failing after the hygiene branch = pairwise invariants do NOT
close at Jupiter (T2 finding, book loudly); N2b failing = the ledger-weight reading
is wrong or data-precision-limited (report which); N2c failing = the Laplace lock is
not in the elements consulted (data problem — it is one of the best-measured facts in
the solar system).

## N2 RESULTS (run1 + hygiene branch, 2026-08-10 ~14:35; data retrieved same hour,
## provenance in nbody-n2.py header; registration 3042d63 pre-data)
- **Four independent pairwise invariants, no G, no masses:** μ_i ∈ {126.713, 126.637,
  126.708, 126.711} ×10⁶ km³/s²; mean = 1.26692e8 vs comparison GM_J = 1.26687e8 —
  **0.004%.** Four separate two-body ledgers, one number.
- **N2a: hygiene branch fired exactly as pre-named, and resolved.** Raw spread 5.98e-4
  (> 5e-4) with Europa the sole large residual (−4.4e-4) — and Europa is precisely
  where the consulted source is internally split (infobox a = 670,900 vs summary
  table 671,100, +3e-4). With the alternate published a: spread = 3.29e-4 → PASS.
  Verdict: source-internal data inconsistency (non-physics); the books close at the
  precision the public elements permit. Second data-inconsistency catch of the day
  (after Charon's 17,181).
- **N2b: DATA-PRECISION-LIMITED (pre-named outcome).** Residual noise 4.4e-4 vs
  partition signal 5.3e-5 — the rounded public a's cannot score the ledger-weight
  rank test. Upgrade path named: JPL-grade elements (a to ~1 km ⇒ 7e-6) would make
  the 1/24 rank test live. Not scored; not claimed.
- **N2c PASS, 589× deeper than registered:** from independently-quoted periods,
  |n_Io − 3n_Eur + 2n_Gan|/n_Io = 1.70e-8 (registered < 1e-5). The pairwise ratios
  are NOT integers (2.00729, 2.01470): the lock is a THREE-BODY PHASE CLOSURE that
  no set of independent pairwise books can produce — the open inter-resonance
  channel, empirically sized. Callisto control clean (2.3326, near-7/3 but off, no
  exact combination). **T3's object is now a measured fact on this front's own
  terms.**
- Standing state: T1 stands (two skies); T2's target sized (Earth–Moon 1.18%
  residual); T3's target sized (the 1.7e-8 phase closure). Next: T3 — derive the
  locking criterion from the ledger (winding-exchange channels where Σp_iω_i ≈ 0,
  channel width from the coupling term, no fitted widths), then N3 (the criterion
  must re-derive the resonance map from rates alone).

## T3 DERIVATION — the channel criterion and its width (2026-08-10 ~14:55, in-session;
## booked BEFORE the N3 instrument runs)
**Ontology (the license):** winding exchange between two circulations requires phase
matching — a beat angle whose accumulation is slow enough that transfer is coherent
over many turns (the planetary-scale instantaneous harmonic inter-resonance). No
matching, no channel: the beat averages to zero and the books stay pairwise.
**The channel Hamiltonian (derived; classical machinery cited, restated in ledger
variables — no masses, only measured invariants μ, partition fractions f′, rates n).**
For a first-order channel j:(j−1) between inner circulation (n, a, e) and partner
(n′, a′, partition f′), the resonant term of the coupling is
    R = (μ f′/a′) f_d(α) e cos φ,  φ = jλ′ − (j−1)λ − ϖ,  α = a/a′,
with f_d(α) the standard Laplace-coefficient combination (cited import: the expansion
of 1/|R_i−R_j|; benchmark f_d(2:1, α=0.63) ≈ −1.19, to be verified numerically in the
instrument against the tabulated value). Pendulum reduction (10 lines, done here):
δΛ conjugate to φ, Λ = √(μa) = na², ∂n/∂Λ = −3n/Λ ⇒
    φ̈ = −ω₀² sin φ,   ω₀² = 3(j−1)² n² · α f′ |f_d| e .
Separatrix ⇒ **CHANNEL HALF-WIDTH (in rate units):  W = 2ω₀ = 2(j−1) n √(3 α f′ |f_d| e)**
— no fitted quantity anywhere: rates, geometry ratio, partition fraction,
eccentricity, and a computed coefficient. d'Alembert scaling (cited): an order-k
channel (|p−q| = k) carries coupling ∝ e^k ⇒ W_k ~ W₁ e^{(k−1)/2}·(coeff) — channels
narrow steeply with order; that is what defeats the density of the rationals (every
ratio is near a rational; almost none is near an OPEN channel). Wyler gate: every
integer pair must buy its place through a computed W — no resonance named by
numerology.
**Criterion:** channel (p,q) OPEN at a configuration iff |p n′ − q n| < W_{pq};
transfer/locking lives inside; incommensurate = closed = pairwise books hold.
**The three-body reading (the Galilean lock, stated before scoring):** the raw
pairwise beats at Io–Europa and Europa–Ganymede are EQUAL (the common 0.74°/d
conjunction drift) — the lock is the EQUALITY, i.e., the vanishing of the three-body
combination, not of either pairwise beat. Prediction: each raw pairwise beat sits
OUTSIDE its own first-order width (the pairwise channels alone cannot hold the raw
offsets — they are dressed by forced precession), while the three-body combination
sits DEEP inside any width in the plausible coupling bracket. The exact three-body
channel Hamiltonian (Laplace-argument coupling at second order) is NAMED OPEN WORK —
cited as research-grade (Sinclair 1975; Yoder 1979; Henrard); this run brackets its
width rather than fabricating a coefficient. The lock's observed DEPTH (1.7e-8) is an
attractor property (dissipative capture — cited, not claimed by the width).

## N3 REGISTRATION (2026-08-10 ~14:55, BEFORE the instrument runs; structural
## predictions with margin classes — coefficients computed only after this commit)
Feed: the N2 elements (booked) + eccentricities from the same infobox pulls (Io
0.0041, Europa 0.0094, Ganymede 0.0013, Callisto 0.0074) + partition fractions
(comparison-class data, conversion-never-performed) f′ = {4.70, 2.53, 7.80, 5.69}e-5.
- **N3a (internal check):** the two raw pairwise beats print EQUAL to ~1e-8·n (both
  = the common drift; their difference IS the N2c combo). Fail = arithmetic bug.
- **N3b (pairwise channels, raw):** |2n₂−n₁| > W(Io–Eur 2:1) AND |2n₃−n₂| >
  W(Eur–Gan 2:1) — both raw beats OUTSIDE their first-order widths (closed raw;
  the dressing is forced-ϖ, as derived above). Expected margin class: beat/W ~ 3–4×.
- **N3c (three-body channel):** |n₁−3n₂+2n₃| < W₃ for EVERY W₃ in the bracket
  [f′²-scale, first-order ceiling] — open with margin ≥ 100× at the conservative
  end. The Laplace lock is irreducibly three-body in the channel accounting.
- **N3d (control, Ganymede–Callisto 7:3):** CLOSED even under the GENEROUS
  first-order-scale width bound (true order-4 width is ~e³ smaller — a fortiori).
  Beat ~9e-4·n₃ vs generous bound < that.
- **N3e (control, golden body):** hypothetical circulation between Europa and
  Ganymede at period ratio φ_golden = 1.618 from Europa: every channel of order ≤ 5
  (3/2, 5/3, 8/5, 13/8) closed by ≥ 3× under generous first-order-scale bounds.
- **N3f (benchmark):** numerically computed f_d(2:1) at the Galilean α reproduces
  the tabulated ≈ −1.19 (cited value) within 5% — verifies the coefficient chain
  against literature before any verdict counts.
Falsifier honesty: N3b failing (raw beats INSIDE pairwise widths) = the three-body
reading above is wrong — the lock would be pairwise-explicable; N3c failing = the
channel criterion cannot hold the measured lock (T3 falsified as constructed); N3f
failing = coefficient bug, fix before scoring anything.

## N3 RESULTS (runs 1+2, 2026-08-10 ~15:05; registration 34a9473 pre-run) — ALL PASS
Run1 → run2: one fix, driven by the registered benchmark exactly as pre-named (N3f
caught it before anything was scored): the added "indirect −2α" belongs to a
different argument — the tabulated −1.19 IS the whole coefficient; direct-only
computation lands −1.1832 (0.6% from tabulated) ✓.
- **N3a PASS:** the two raw pairwise beats print −0.73950 / −0.73951 °/d — EQUAL to
  1e-8 class; their difference is the N2c Laplace combo. The "common conjunction
  drift" structure confirmed from the fetched elements alone.
- **N3b PASS (the three-body reading's first half):** both raw pairwise beats sit
  OUTSIDE their own first-order channel widths — Io–Europa beat/W = 3.78, Europa–
  Ganymede 2.87 (registered class 3–4×). The pairwise channels alone CANNOT hold the
  raw offsets; the dressing is forced precession, as derived.
- **N3c PASS (the second half):** the three-body combination sits INSIDE every W₃ in
  the plausible coupling bracket — margin 216× at the STRICTEST (f′²) floor, ~10⁵×
  at the ceiling. **The Laplace lock is irreducibly three-body in channel
  accounting** — the registered reading, now scored.
- **N3d PASS (control):** Ganymede–Callisto 7:3 CLOSED even under the generous
  first-order-scale bound (beat/W = 1.31); the true order-4 width is ~e³ smaller —
  closed a fortiori by ~5 orders.
- **N3e PASS (control):** golden-ratio body — every channel of order ≤ 5 closed by
  28–191×. The density of the rationals is defeated by the width's order-scaling,
  as derived. The Wyler gate held: every integer bought its place through a
  computed W; no resonance was named by numerology.
- Standing state of T3: criterion + width formula DERIVED (no fits) and CONFIRMED in
  the registered pattern on the best-locked system in the sky. Named open work:
  the exact three-body channel Hamiltonian (bracketed here, never fabricated);
  N4 = Kirkwood confrontation with real gap-width data; N2b upgrade path (JPL
  elements). Public exhibit surfaces untouched pending ratification.
