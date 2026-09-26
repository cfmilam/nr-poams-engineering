# Persistent-winding register protocol

## 1. Objective and technology-first gate

Demonstrate and characterize a physical register whose states are distinguished by signed winding/fluxoid number or another independently imaged closed circulation, and determine whether it supports reliable write, pump-off hold, read, erase, reversal and cycling.

1. **Native intervention:** add, remove or reverse a completed circulation through a declared boundary operation; do not infer winding from a command bit.
2. **Raw observable:** native SQUID voltage/flux feedback and switching records, plus source voltage/current, thermometry and environmental channels. If another platform is selected, substitute an independently calibrated magnetic image or torque/phase readout.
3. **Frozen discriminator:** state clusters must remain separable after pump-off, transform according to the signed commands, and show a retention/transition distribution inconsistent with the measured electronics-only and thermal/mechanical controls.
4. **Artifact controls:** direct heat, field, current pickup, vibration, cable, readout-backaction, trapped-field, software-latch and analyst-path injections.
5. **Leverage:** nonvolatile cryogenic memory, flux/phase calibration, phase-slip metrology, state preparation for later gate work, and a clean null separating coherent bus from register.

No anomalous support response, reactionless transfer, POAMS-only memory effect or gate performance is asserted.

## 2. Claim grades and hypotheses

| Item | Pre-run grade |
|---|---|
| Fluxoid quantization, persistent currents, SQUID readout and phase slips | Imported extant physics and engineering craft |
| Integer state assignment from locally calibrated readout | Operational reduction |
| A retained state as a POAMS completed circulation | Candidate interpretation; not established by successful storage alone |
| Complete energy and angular-momentum receipt | Prospective apparatus achievement |
| Residual beyond ordinary superconducting/device behavior | Prospective; requires a separately frozen prediction |

- **H0-R:** after pump-off and registered settling, read records contain no stable physical-state information beyond electronics memory, trapped external field, drift and calibrated nuisance paths.
- **H1-R:** at least two independently witnessed signed physical states persist through the frozen hold interval and remount/thermal-control structure.
- **H0-WER:** apparent write/erase/reversal follows command electronics or thermal history rather than the physical loop state.
- **H1-WER:** the physical state follows the registered signed operation with bounded error, including sham and polarity transformations.
- **H0-ND:** repeated reads perturb the state at or above the allowed read-disturbance limit.
- **H1-ND:** a qualified nondestructive read mode stays below that limit; a deliberately destructive mode produces the predicted reset/transition receipt.
- **H0-P:** transition times and rates are explained by directly measured temperature, field, vibration and read/write backaction.
- **H1-P:** an additional state-dependent transition component remains after the registered controls; it is unexplained until replicated, not automatically POAMS.

## 3. Candidate platforms and down-select

| Platform | State/readout | Strength | Disqualifier for Generation 1 |
|---|---|---|---|
| **Superconducting multiply connected loop with weak link(s), SQUID readout** | Signed fluxoid/persistent-current state; inductive read | Mature write/read/erase, countable slips, direct Josephson/flux-vortex dependencies | Inadequate thermal/field shielding, hysteretic readout not separable from state, or no independent state calibration |
| Pinned Abrikosov vortex or vortex ensemble | Vortex occupancy/location; Hall/SQUID/magnetic imaging | Physical winding plus pinning/creep/endurance tests | Ambiguous vortex count, uncontrolled pinning landscape, destructive imaging, or excessive creep |
| Magnetic ring/domain-wall/vortex state | Magnetometry or imaging | Room-temperature possibility, easy cycling | State is domain texture without demonstrated closed-winding invariant; ordinary hysteresis may dominate |
| YIG coherent/retained mode | Independent phase/magnetic witness | Direct continuity with Lane-A YIG and spin-transport work | Ring-down or magnon population without pump-off signed retention; no erase/reversal receipt |
| Mechanical/topological loop | Imaging/torque | Direct geometric Tw/Wr visibility | Low cycle rate, uncontrolled friction/creep, no scalable independent readout |

**Default down-select:** superconducting loop for Generation 1; single pinned-vortex device as an optional topology-visible companion. Choose the final device family only after a paper design review establishes operating temperature, energy scale, expected signal, read disturbance, write margin, shielding, fabrication access and a complete boundary diagram. Do not splice parameters from different materials or device families.

## 4. Apparatus boundaries

- **B1 device boundary:** loop/weak links, local write line, sensor coupling element, thermometer and declared substrate anchors.
- **B2 complete reaction boundary:** cryostat, shields, magnets/write source and returns, SQUID/readout electronics, cables, attenuators/filters, grounds, refrigerator, vacuum plant and mechanical support to Earth.

Every state transition must post: source volt-time and charge transfer, delivered/returned electrical energy, magnetic/inductive energy change, heat released or absorbed, electromagnetic impulse/torque where measurable, mechanical reaction/bound, and readout energy. Terms below resolution receive conservative bounds; they do not disappear.

## 5. Stage gates

### Gate 0 — apparatus and custody qualification

Pass before retention claims:

1. common-clock timing, raw native channels, immutable hashes and blind-label replay;
2. readout calibration across the full flux range, both polarities, with noise, drift, hysteresis, reset and saturation mapped;
3. direct transfer functions from controlled temperature, field/gradient, write-line pickup, vibration, read-amplitude, cable motion and electronics-reset injections;
4. superconducting device, open-loop/dummy, shorted-turn and electronics-only controls characterized;
5. shield remanence and field-cool/zero-field-cool histories mapped;
6. write/read source energy and B1/B2 boundary channels calibrated before and after runs;
7. pilot estimates of cluster separation, state-preparation error, phase-slip rate, autocorrelation and censoring;
8. preregistration commitment generated from pilot data before confirmatory trials.

### Gate 1 — state observability

At pump-off, show at least two signed state clusters using the physical sensor. Demonstrate label permutation, lead reversal and calibrated flux injection. A software variable or command echo cannot count as the independent witness.

### Gate 2 — write, erase and reversal

Randomize `write +`, `write -`, `erase`, `sham`, and `no-operation`. Verify transitions from every starting state, not only from an assumed zero. Record full pulse waveform and post-pulse settling. Build a transition matrix with confidence intervals.

### Gate 3 — retention and spontaneous phase slips

After all registered electrical, thermal and mechanical settling thresholds are crossed, conduct logarithmically spaced reads through the frozen hold horizon. Preserve right-censored trials. Repeat over a preregistered temperature and field grid. Time-tag every state transition; distinguish single-quantum, multi-quantum and unresolved events by calibrated likelihood. Do not discard “glitches” that coincide with environmental channels.

### Gate 4 — readback mode and backaction

Interleave no-read holds, low-amplitude repeated reads, amplitude/duty-cycle sweeps and a deliberately destructive read/reset. Estimate transition hazard per read and per unit read energy separately from elapsed-time hazard. Nondestructive status is empirical, never assumed from circuit topology.

### Gate 5 — cycling and endurance

Run balanced cycles across both signs and erase paths. Include periodic calibration, cold restart, field-history reset, device remount/rewire where possible, and held-out blocks. Track drift in state separation, write energy, BER, slip rate, thermal load and read disturbance. Report all failed cycles and stopping reasons.

### Gate 6 — replication and gate eligibility

Repeat the frozen protocol on a second device and independent analysis. Only a register passing Gates 1–5 becomes an input to Lane-B persistent-register/gate mathematics. Coherent superposition, quantum advantage or logic-gate fidelity is not inferred from classical retained-state performance.

## 6. Conditions, randomization and blinding

Use balanced permuted blocks stratified by device, temperature band and run day. The scheduler enforces washout/cooldown but does not inspect the state readout. Operators receive safety-necessary commands under opaque condition labels. Analysts remain blind through exclusions, reduction and the primary report.

Required conditions:

- device / open-loop dummy / electronics-only replay / optional pinned-vortex companion;
- write + / write − / erase / sham / no-operation;
- low read / high read / no-read hold / destructive read;
- nominal field / reversed field / offset-field injections / shield reset;
- nominal temperature / matched heat injection / controlled temperature grid;
- quiet / calibrated vibration and cable injections;
- normal electronics / latched-state reset / swapped readout chain;
- initial assembly / rewire or remount / second device.

## 7. Predeclared estimands and thresholds

The pilot supplies numerical values; the confirmatory annex freezes them. Required entries are:

1. **State separability:** blind classifier and physical calibration must agree. Freeze a minimum Mahalanobis/likelihood separation and a maximum ambiguous fraction. Suggested Generation-1 target: lower 95% confidence bound on state-assignment accuracy ≥99.9% in held-out trials.
2. **Write/erase/reversal:** upper 95% confidence bound on each operation error ≤10⁻³, reported separately by starting state and sign. Zero observed failures is reported with its binomial upper bound, never as zero error.
3. **Retention:** freeze a mission hold time and temperature/field envelope. The lower confidence bound on survival at that horizon must exceed the application target; report median or lower-bound lifetime only if supported by observed transitions, otherwise a censored lower bound.
4. **Nondestructive read:** upper 95% bound on excess transition probability per read ≤10⁻⁶ and no monotone state-coordinate drift exceeding the registered equivalence band over the read-count target.
5. **Phase-slip model:** publish event counts and exposure. Compare constant-hazard, temperature/field/read-dependent and overdispersed models; accept a model only after residual/time-rescaling checks. No event implies an upper rate bound (approximately 3/exposure at 95% for a simple Poisson model), not infinite lifetime.
6. **Energy receipt:** measured plus conservatively bounded B2 output must close to input within the preregistered combined uncertainty for calibration transitions. An unexplained residual blocks mechanism claims.
7. **Angular-momentum receipt:** state-change angular momentum from the declared imported device model plus measured/bounded electromagnetic and mechanical reaction must close within the frozen uncertainty. If device geometry prevents a meaningful AM reduction, say so; energy closure alone does not substitute.
8. **Endurance:** freeze cycle target and permitted drift. Suggested first engineering target: ≥10⁶ balanced operations with no confidence-bounded BER or state-separation degradation beyond 20% of its initial qualified margin.

Suggested targets are design goals, not claims and not valid until the run annex uses pilot-achieved noise and application needs.

## 8. Analysis

Primary outputs are the confusion/transition matrices; survival curves with interval/right censoring; state-conditional phase-slip rate and multiplicity; read-hazard slope versus count and energy; endurance drift; and signed energy/AM closure per transition.

Use trial/block as the experimental unit. Retain time correlation and refrigerator/run-day random effects. The primary classifier, state boundaries, censoring rule, event-merging window, glitch rule, exclusion set and model family are frozen. Secondary hidden-Markov or Bayesian analyses may be reported but cannot replace the registered reduction. Multiplicity is separated across write performance, retention, read disturbance and endurance families.

## 9. Artifact controls

| Apparent result | Alternative | Direct control |
|---|---|---|
| Stable state | SQUID/electronics latch | electronics reset, second readout chain, calibrated flux injection, device warm-normal control |
| Signed retention | trapped external field/shield remanence | field probe, polarity reversal, shield degauss/reset, field-cool history matrix |
| Phase slip | readout dropout/reset | raw I/Q/feedback/status bits, redundant sensor, injected dropout library |
| Write success | direct pickup in readout | open-loop dummy, delayed read after source disconnection, swapped cable topology |
| Lifetime change | temperature drift | device thermometry, matched heaters, direct thermal transfer calibration |
| Read disturbance | Joule heating or flux injection | no-read holds, amplitude/duty sweep, matched heater and dummy mutual inductance |
| Cycling degradation | refrigerator or amplifier drift | witness device, calibration cadence, block/day model |
| “AM residual” | cable/magnet/support torque | full B2 reaction sensors or conservative calibrated bounds, geometry reversal |

## 10. Useful nulls and failure interpretation

- No independent pump-off state: the platform is a bus/relaxing reservoir, not a register.
- State exists but cannot be reliably erased or reversed: it is retained matter history, not a controllable register.
- Read hazard above threshold: it may be a destructive memory; label it honestly and redesign the readout.
- Ordinary trapped-flux memory reproduces while no additional residual appears: M0 apparatus qualification succeeds and bounds the tested POAMS extension.
- Slip rate is fully explained by temperature/field/read controls: useful barrier and reliability metrology; no extra mechanism.
- Energy closes but AM cannot be measured or bounded: memory performance may stand, but the POAMS receipt remains incomplete.
- Device-to-device failure: scope the result to the qualified article/fabrication; do not average away heterogeneity.
- A robust adverse sign or scaling retires the contradicted prospective map at that scope.

## 11. Safety

Cryogen training and oxygen-deficiency assessment; pressure relief and quench plan; magnet/projectile and pacemaker exclusion; stored-energy/current limits; filtered interlocks; guarded vacuum and cold surfaces; electrical isolation; RF/microwave survey if used; remote operation for ramps; logged abort thresholds; and safe state after control loss. Safety overrides blinding and every override remains in the record.

## 12. Downstream boundary

A passed register provides measured state labels, transition laws, lifetime, operation energy, read disturbance and endurance to the future gate-mathematics unit. It does not by itself establish a native microscopic POAMS law, quantum coherence, useful computation, a universal winding register, or support-response coupling.
