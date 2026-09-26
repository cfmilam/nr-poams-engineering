# Receiver Stage 1 conditional protocol

## 1. Objective and claim grades

Conditional on a real Stage-0 M0 occurrence and independent M1 replay passing unchanged, test whether the frozen source-local observable distinguishes an **intended qualified sink** from matched, detuned, dummy, clone, absent and geometry-reversed alternatives under direct artifact control.

| Proposition | Grade before Stage 1 |
|---|---|
| Circuit/transmission-line/resonator craft | Imported apparatus physics and control model |
| Stage-0 transfer function, if supplied | Empirical input limited to its M0/M1 scope |
| Sink-selective source response | Prospective Stage-1 hypothesis |
| Identity beyond frequency matching | Prospective; requires a multidimensional physical signature |
| Information channel or capacity | Prohibited inference at Stage 1 |
| Nonstandard timing or no-transit ontology | Prohibited inference at Stage 1 |

A pass earns only a bounded, reproducible source/sink state relation for this apparatus and authority to design Stage 2.

## 2. Mandatory entry packet from Stage 0

Do not commission Stage 1 without immutable M0/M1 identifiers and numerical values for: source technology and article IDs; primary raw observable `Y_A`; source command; bandwidth and filters; B0/B1/B2 diagrams; baseline/open envelopes; Stage-0 transfer function with covariance; timebase and latency bounds; source noise/settling/correlation; artifact transfer functions and veto limits; energy/storage closure; selected source/sink geometry; physical repeat and held-out result; calibration files; smallest effect/equivalence region; and all unresolved anomalies.

If any Stage-0 value is changed, Stage 1 is a new protocol branch and must repeat the affected qualification.

## 3. Qualified source and sink

### Source qualification

The source remains fixed and unkeyed. Its waveform, impedance, control state, local termination, supply and primary observable are exactly the Stage-0 configuration. Pre-block checks must reproduce its blank/open noise and calibration within frozen equivalence bounds.

### Intended sink qualification

Define the sink by a frozen vector signature, not a name:

`S = {resonant frequencies/linewidths, impedance tensor or network response, phase/group response, coupling orientation, geometry, state-transition witness, dissipation/temperature, control burden}`.

Measure each component locally before the blinded run. A sink state is achieved only when its independent witness lies inside the registered state envelope. Source output never defines sink state.

## 4. Required state matrix

1. **INTENDED-MATCHED:** qualified sink in its preregistered ready state.
2. **INTENDED-DETUNED:** same sink and control burden, detuned by registered linewidth/impedance offset.
3. **MATCHED-DUMMY:** matches ordinary impedance, heat and command burden but lacks the proposed distinguishing signature.
4. **FREQUENCY-MATCHED CLONE:** independent article matched in frequency and gross loading but outside at least one declared signature coordinate.
5. **SINK-ABSENT:** calibrated fixture/open state with parasitic inventory measured.
6. **GEOMETRY-REVERSED:** intended sink with a preregistered orientation/handedness/placement transformation while gross loading and distance remain matched.
7. **SHAM-COMMAND:** command traffic and local actuation burden without sink-state transition.
8. **MULTIPLE-SINK CHALLENGE:** intended sink plus dummy/clone where safe, to detect ordinary loading and ambiguity.

No state is “zero”; every one has a finite measured network and nuisance envelope.

## 5. Apparatus boundaries

- **B0:** frozen source output plane, supply/controller, local termination and all local sensors. Owns the primary source record.
- **B1:** B0 plus complete guided/near-field coupling route, return/shield, sink fixture and state actuator to named reference planes. Owns transfer, storage and dissipation accounting.
- **B2:** complete reaction system: source/sink power supplies, control links, clocks, grounds, enclosures, mounts, thermal/fluid/mechanical paths and support/Earth crossings. Owns command-feedthrough and reaction closure.

Freeze exhaustive crossing and component manifests. Any unmeasured alternate A↔B path blocks selectivity attribution.

## 6. Competing preregistered trace envelopes

All families use the same source-local coordinate

\[
\Delta Y_A(t;s)=Y_A(t;s)-Y_{A,blank}(t).
\]

- **C0 / nonselective-null:** every sink state remains inside the Stage-0-derived finite control band.
- **C1 / ordinary-load family:** responses rank and scale according to the measured B1 impedance/coupling model; intended, dummy and clone are equivalent when ordinary network coordinates are matched.
- **C2 / sink-selective family:** intended-matched alone enters a disjoint signed/time-windowed acceptance region; detuned, dummy, clone, absent and reversed states remain below their frozen bounds or follow a separately frozen transform.
- **CX / contradiction:** traces miss all families, exhibit wrong chronology/order/sign, fail closure or change on held-out geometry.

Artifact vetoes are orthogonal. C2 is admissible only if its acceptance region is disjoint from C0/C1 after uncertainty and no injection reproduces it. If POAMS supplies no justified sign for geometry reversal, freeze “different/equivalent” magnitude logic rather than inventing a sign.

## 7. Common-clock and latency logic

Retain Stage-0 common epoch and hardware timestamps. Record source command, sink command, independent sink witness, source response, endpoint V/I or I/Q and nuisance channels on the same clock. Calibrate fixed delays, drift and jitter before/after blocks with simultaneous markers.

Define latency only between physical sink-witness crossing and source-record onset. Report an interval including state-witness, sensor, filter and clock uncertainty. Do not subtract an expected propagation delay to manufacture an anomaly. Ordinary causal/reflection models remain explicit competing explanations. A Stage-1 latency is not a signalling latency and cannot support backwards-signalling language.

## 8. Raw observables

Primary: the unchanged Stage-0 native source channel and frozen reduction `Y_A`.

Required explanatory channels: source V/I and forward/reflected I/Q; source supply/control error; sink V/I or I/Q; sink-state witness; actuator command and reaction; line/return/shield/common-mode currents; termination/storage V/I; temperatures at every active element; electric/magnetic pickup; vibration, acoustic, pressure/humidity, cable motion/strain; common-clock ticks and health; range/saturation/drop flags; configuration and command logs.

All force, power, energy, impedance, latency, signature coordinates and classifications are derived from preserved native samples.

## 9. Calibration and nuisance injections

Repeat affected Stage-0 calibrations and add:

- signature-coordinate calibration and cross-covariance;
- intended/detuned/dummy/clone network equivalence mapping;
- sink actuator command feedthrough at B0/B1/B2;
- controlled impedance/load sweeps spanning all state values;
- frequency/phase/linewidth sweeps across the intended and clone;
- geometry translation/rotation with invariant electrical loads;
- parasitic sink census using movable absorbers/conductors/loads;
- multiple-load superposition and saturation tests;
- isolated heat injections at intended, clone and actuator;
- clock offsets, label swaps, delayed witness, dropped packets and channel swaps;
- cable reroute, shield/ground reversal, EM injection, vibration/acoustic and source-drift injections.

An ordinary load model that predicts the source trace within the frozen error budget classifies C1, not C2.

## 10. Randomization and blinding

Use balanced permuted blocks stratified by day, geometry and sink article. Commit the seed and escrow the state map. Operators receive only safe setup codes; independent state witnesses are hidden from primary analysts. Include indistinguishable sham commands. Freeze maximum blocks, washout, exclusions, missing-data policy and any sequential spending before acquisition. Unblind only after calibration checks, raw hashes and the primary C0/C1/C2/CX classification report are immutable. Retain every abort and intervention.

## 11. Analysis

Primary estimands are preregistered pairwise contrasts between intended-matched and each required control, plus the full state-class effect in a block-level model. Report intervals and equivalence tests, not p-values alone. Account for autocorrelation and multiplicity; samples are not trials. Assess:

- covariance with independent sink state rather than command;
- residual after the measured ordinary-load model;
- detuning/selectivity curve with uncertainty;
- clone false-distinction or equivalence;
- absent-state upper bound;
- geometry transformation;
- latency interval and chronology;
- energy/storage/reaction closure;
- remount, second-sink and held-out geometry repeatability;
- artifact-injection predictive checks.

### Capacity-prohibition boundary

Do **not** encode a message, optimize a decoder, quote bit error rate, mutual information, bits/s, energy/bit, security, interception resistance or channel capacity. Repeated randomized condition labels are experimental treatments, not symbols. A positive state classifier on laboratory trials is not a communication channel.

## 12. Decision rules and consequences

- **No qualified sink state:** no Stage-1 test occurred.
- **C0/equivalence null:** no controlled coupling above the declared bound for the tested signature and geometry.
- **C1 ordinary-load result:** useful calibrated source/load response; retire the stronger sink-selective reading at this scope.
- **C2 qualified candidate:** all required intended-vs-control contrasts pass, B1/B2 close, no artifact reproduces the signature, physical repeat and held-out geometry pass. Earn only a bounded selective source/sink relation.
- **Clone equivalence:** frequency/gross-load matching is sufficient at measured sensitivity; identity claim fails but ordinary coupling remains.
- **Clone confusion:** retire the proposed signature coordinate and do not promote to Stage 2.
- **Sink-absent excursion:** retire exclusivity/standby-silence for the apparatus and expand the parasitic census.
- **Geometry reversal null:** constrains only the declared geometry-sensitive branch; do not universalize.
- **Wrong sign/order/latency or nonclosing ledger:** adverse contradiction; repeat once frozen, then retire the affected mapping if reproduced.
- **Artifact replica:** attribution fails even if the raw contrast is repeatable.

## 13. Safety

Inherit Stage-0 limits and interlocks. Reassess hazards for resonators, higher RF, strong fields, actuators, stored energy and moving geometry. Use touch-safe/current-limited construction, discharge indicators, RF leakage survey and open-enclosure interlock, thermal/reflected-power trips, guarded motion and strain relief. Safety overrides blinding and every intervention is logged.

## 14. Gate to Stage 2

Stage 2 may be designed only after a C2 candidate has: complete M0 custody and independent M1 replay; unchanged physical repeat; held-out geometry and second sink/article success; closed B1/B2 ledgers; quantified intended/detuned/dummy/clone/absent/reversed confusion matrix as experimental state classification; stable latency and settling bounds; finite absent-state limit; demonstrated artifact rejection; and a frozen, non-postselected set of sink states suitable for later symbolization.

Only then may a separate Stage-2 protocol define symbols, decoder, rates, error bounds, mutual-information lower bounds and capacity claims. Stage 1 itself establishes none of those.
