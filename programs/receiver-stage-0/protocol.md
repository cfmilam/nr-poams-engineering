# Receiver Stage 0 laboratory protocol

## 1. Question, boundary and claim grade

With source command fixed and unkeyed, does changing only the declared far-end completion constraint produce a source-local record outside the predeclared control envelope, with frozen sign, chronology and geometry behavior, after every measured ordinary transfer path is accounted for?

Imported transmission-line, circuit, RF and metrology machinery is permitted and labelled. The endpoint-sensitive relation is a prospective POAMS hypothesis. A run can earn only a bounded empirical endpoint/source relation for the tested system. Stage 0 cannot establish a channel, capacity, silence everywhere, no carrier, no transit, efficacy or ontology.

## 2. Reference source system

Use a current-limited, phase-stable waveform source at endpoint A, a replaceable shielded two-conductor route of measured length and distributed parameters, and endpoint B containing an independently witnessed switch matrix that selects:

1. **OPEN** — finite characterized open network;
2. **CLOSED/MATCHED** — calibrated termination;
3. **MATCHED DUMMY** — same local switch burden and thermal/electrical command load without the declared completion;
4. **DETUNED RETURN** — known impedance/reactance offset;
5. **LOCAL-SWITCH CONTROL** — equivalent switching operation at A;
6. optional declared capacitor insertion/bypass, with terminal voltage/current measured.

The return conductor, shield, grounds, source impedance and every parasitic termination are part of the apparatus. “Open” never means metaphysical nothing; it means the measured network state.

### Observable candidates

Primary candidate: source-current residual

\[
\Delta I_A(t;L,s)=I_{A,s}(t;L)-I_{A,blank}(t;L).
\]

Freeze one primary statistic `T` over one window before physics acquisition. Candidate secondary observables—reported with multiplicity control, not substituted after viewing data—are source voltage, instantaneous source power, integrated work, forward/reflected I/Q or complex reflection, source-control error, and local termination voltage/current. Far-end and return V/I, contact witness, common-mode/shield current and capacitor V/I are explanatory/state channels, not source-local primary endpoints.

## 3. Apparatus boundary

- **B0/source boundary:** source output plane, source supply and controller, local termination and local sensors. Establishes the primary local record.
- **B1/link boundary:** B0 plus complete cable/return/shield, far switch/termination/storage network and feedthroughs. Establishes ordinary transfer and stored-energy accounting.
- **B2/reaction/environment boundary:** power supplies, grounds, clocks, command links, thermal/mechanical mounts and environmental couplings. Establishes whether a purported endpoint effect is command feedthrough or exported reaction.

Before data freeze a wiring/geometry diagram, grounding diagram, cable construction and route, reference planes, polarity, common clock, and exhaustive crossing manifest. Any unmeasured path between A and B—including switch control, shared mains, network link, shield, ground, optical command leakage, air/acoustic or mechanical coupling—blocks attribution.

## 4. Hypothesis envelopes

- **H0/control-only:** both OPEN and CLOSED remain within the same finite source residual band `|ΔI_A| ≤ δI_A` over the frozen window.
- **H1/endpoint-sensitive:** OPEN remains within that finite band; CLOSED enters the signed acceptance region `s*ΔI_A ≥ Δ*` within frozen onset/lag window `W_L`, with `Δ* > δI_A + margin`, and follows the frozen length/geometry rule `κ*`.
- **Neither/contradiction:** trace misses both, wrong sign/order/window/scaling, or the account fails closure.

Artifact vetoes are separate from H0/H1: any direct injection reproducing sign, lag, waveform or length behavior prevents endpoint attribution.

## 5. Stage gates

### S0-A — component metrology

Measure source Thevenin/Norton behavior, noise spectrum and control-loop response; line S-parameters or time-domain response; distributed R/L/C/G over operating band; termination impedances; switch contact timing/bounce/leakage; capacitor/storage behavior; sensor impulse responses; and common-mode/shield/ground paths. Verify dynamic range and no clipping.

### S0-B — common-clock and chronology proof

Distribute one traceable reference or discipline all digitizers to one hardware epoch. Record raw counter ticks, trigger fan-out and per-device health. Inject simultaneous electrical markers at A and B; map fixed delay, drift and jitter. Then inject known offset, dropped timestamp, channel swap and delayed command faults. The pipeline must recover or reject them at the preregistered tolerance. Software receipt time is never primary event time.

### S0-C — nuisance transfer qualification

Directly inject crosstalk, source-sensor pickup, shield/ground currents, known capacitance, thermal steps at each component, cable motion, vibration, acoustic drive, magnetic/electric fields, source drift, contact bounce, local switching, detector saturation and label/timing faults. Freeze each transfer function and attribution bound.

### S0-D — blinded endpoint matrix

Run balanced randomized blocks containing all six reference states. Source command waveform and local instrumentation remain unchanged. Include at least two prespecified lengths/geometries in development; reserve one length and one return geometry for held-out confirmation. Calibrate before/after every block group.

### S0-E — physical repeat

Repeat the full frozen matrix after disassembly/remount and on the held-out geometry with unchanged code and bounds. Independent analysis replay is required but does not replace the physical repeat.

## 6. Calibration

For every V/I/IQ channel calibrate gain, offset, phase, bandwidth, impulse response, common-mode rejection, noise, nonlinearity, saturation and recovery. Calibrate switch state with an independent contact or impedance witness, not command alone. Measure timebase frequency/phase error and cable delays. Characterize source drift versus load, supply, temperature and time. Map thermal and mechanical transfer into each electrical channel. Record calibration covariance; correlated errors are not combined as independent.

## 7. Controls and matched comparisons

| Control | Must match or measure | Failure consequence |
|---|---|---|
| OPEN vs CLOSED | source command, route, window, environment | primary contrast |
| matched dummy | switch command current, timing, heat, cable burden | matching response identifies control feedthrough |
| detuned return | delivered command and geometry | maps ordinary impedance dependence |
| local-switch control | switch type, command, heat, timing at A | matching transient identifies local switch artifact |
| cable-route/shield reversal | length and termination | response tied to route/shield is ordinary coupling |
| capacitor swap/bypass | terminal V/I and stored energy | unbooked storage blocks claim |
| command-link sham | packets/light/current without contact change | response identifies command leakage |
| source blank | acquisition/analysis identical | defines finite source floor |
| sensor blank/swap | range and bandwidth | detector-specific response blocks claim |
| held-out geometry | frozen code/thresholds | failure prevents Stage 1 |

## 8. Randomization and blinding

Use balanced permuted blocks stratified by day, cable length and geometry. Generate conditions from a commitment-hashed seed; escrow state labels. Operators see only safety and connection instructions. Automate far-state selection when possible; keep independent witness hidden from analysts. Blind analysts until maximum trials are complete, frozen exclusions applied, raw/derived hashes sealed and the primary report emitted. Preserve aborts, overloads, missing samples, interventions and emergency unblinds. No result-driven extension or window selection.

## 9. Analysis and decision quantities

Define

\[
U_{open}=\max_{t\in W_{open}}|I_A(t)-I_{A,blank}(t)|,
\quad D_{CO}=T(R_A|closed)-T(R_A|open).
\]

Before acquisition freeze: blank construction, statistic `T`, filters, baselining, windows, sign `s*`, `δI_A`, `Δ*`, margin, `W_L`, `κ*`, equivalence region, trial count, block estimator, confidence method, multiplicity, exclusions and stopping. Use block—not samples—as the independent unit; account for autocorrelation. Report full traces, pointwise/simultaneous interval as registered, effect interval and equivalence conclusion.

Stage-0 pass requires simultaneously:

1. finite OPEN bound `U_open ≤ δI_A`;
2. CLOSED/OPEN contrast meets the disjoint H1 gate;
3. required state witness and complete energy/storage ledger close;
4. no injected path reproduces the registered signature;
5. physical repeat and held-out geometry pass unchanged.

Otherwise classify H0/null, artifact-bound, neither/contradiction, boundary-not-closed, or state-not-achieved.

## 10. Nuisance and error budget

Quantify sensor noise/drift, ADC quantization and aperture, timebase skew/jitter, source amplitude/phase/control error, source/load impedance uncertainty, cable dispersion/reflections/loss, switch bounce/leakage/contact resistance, capacitor dielectric absorption and charge memory, common-mode/shield/ground currents, direct capacitive/inductive coupling, EM pickup/rectification, command feedthrough, power-supply/mains covariance, thermal EMF/resistance drift, vibration/microphonics/cable triboelectricity, acoustic response, humidity/sorption, geometry/remount variation, filtering/aliasing/clipping/dropouts, order/carryover/day/operator effects and model uncertainty.

Each entry receives raw channels, injection data, bound, covariance and veto rule. A calculated-small artifact without injection is not cleared.

## 11. Safety

Begin low-voltage/current-limited. Use touch-safe enclosures, current limiting, fusing, discharge resistors and capacitor state indicators; RF shielding/interlocks if RF is used; strain relief and guarded switching; thermal aborts; isolated command/control where appropriate; emergency stop; and lockout before rewiring. Preserve every safety abort as data. Higher voltage or radiated architecture requires a new hazard review and does not inherit this clearance.

## 12. Finite-null consequences

- H0 with closed custody retires endpoint sensitivity below the stated bound for the tested source, bandwidth, length and geometry; it does not prove universal absence.
- An OPEN excursion above its bound retires exclusivity/silence for that apparatus.
- Ordinary delay/storage scaling establishes the conventional transfer envelope and defeats any stronger chronology claim in that regime.
- Artifact replication retires endpoint attribution but yields a calibrated nuisance model useful for later instruments.
- Held-out failure blocks generalization and Stage 1 even if development data pass.
- Wrong sign/order/chronology is adverse evidence against the registered mapping, not a new positive channel.

## 13. Handoff gate to Stage 1

Stage 1 may begin only if Stage 0 has: selected one stable source technology and primary observable; passed all five pass conditions; frozen a reproducible source-state transfer function with uncertainty; demonstrated open/absent, matched, detuned, dummy, clone-ready and geometry-reversal controls; established common-clock latency bounds; closed energy/storage and command-feedthrough accounts; repeated physically; passed held-out geometry; released M0 custody and independent M1 replay; and defined a symbol rate safely below the measured settling/correlation limit.

Stage 0 pass authorizes design of a signalling bench only. It does not itself establish a bit, channel, information rate or nonstandard causal behavior.
