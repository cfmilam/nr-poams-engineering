# Rate-of-Time material-state protocol

## 1. Question and evidential boundary

Can a controlled material-state contrast `X_1-X_0`, witnessed independently of the clocks, produce a shared fractional component in two dissimilar clock outputs that is not reproduced by measured thermal, electromagnetic, mechanical, optical/RF, source, reference, software, or analyst paths?

Before a run, the proposed common term is conjectural. Frequency ratios and phase records are measurements when fully receipted; “proper time changed” is an interpretation. No single clock can distinguish a universal factor from a transition shift. Two clocks do so only relative to a nuisance/local model of adequate rank. Even a passed two-clock result is a **common-clock candidate**, not universal time.

## 2. Registered variables

For clocks `i in {A,B}`:

`y_i(t)=Delta ln nu_i(t)=g[u](t)+ell_i[u,H](t)+sum_q s_iq z_q(t)+d_i(t)+epsilon_i(t)`.

- `u(t)`: dimensionless, independently measured intervention coordinate, baseline `u=0`.
- `g`: candidate shared fractional component.
- `ell_i`: clock-local state response.
- `z_q`: measured nuisance and reference/link coordinates.
- `s_iq`: coefficients learned only from direct injections/training data.
- `d_i`: frozen drift/dead-time model.

Primary contrasts are the simultaneously recorded closure ratios A/R, B/R, and A/B. The analysis must show whether the common vector `(1,1)` is outside the span of calibrated nuisance and reference columns over the analysis bandwidth.

## 3. Preregistered hypotheses

- **H-N:** all common-family coefficients lie within registered equivalence margins; local/nuisance models explain the records.
- **H-L:** one or both clocks respond to state, but responses are clock-specific and do not support one shared fractional component.
- **H-R:** apparent A/R and B/R covariance is attributable to R, transfer oscillator, comb, link, acquisition, or synchronization.
- **H-C:** one shared component improves held-out prediction for A/R and B/R, is seen consistently in A/B closure, lies outside the calibrated nuisance span, follows the independent state witness, and survives reference swap/remount.
- **H-X:** H-C plus the same fractional response in a preregistered non-clock process. This remains a cross-process candidate, not universal proof.
- **H-A:** a frozen common family predicts sign/symmetry/scaling/persistence that the record contradicts.

## 4. Stage gates

### Gate 0 — paper design and host survey

Freeze clock species, interrogation schemes, reference path, intervention candidate, geometry factors, all raw channels, safety envelope, injection ranges, exclusion rules, model families, equivalence margins, and stopping rule. Produce a signed causal diagram and full transfer-path inventory. Do not estimate detectable physics from catalogue clock accuracy.

### Gate 1 — independent baseline qualification

Operate A, B, and R with the intervention hardware installed but inactive for enough duration to estimate overlapping Allan deviation, modified Allan deviation where applicable, drift, dead time, cycle slips, ratio closure, and environmental transfer. Repeat after shutdown/restart and remount. Pass criteria are host-specific and frozen from pilot data.

### Gate 2 — nuisance injection matrix

With an inert/dummy article, inject each nuisance separately and in registered pairs over a range bracketing or exceeding the intervention exposure without violating safety or clock linearity:

1. temperature offset and ramp at article, clock chambers, electronics, comb, cables, and enclosure;
2. magnetic field and three-axis gradient, both signs;
3. electric field/leakage and ground-potential change, both signs;
4. strain/displacement and vertical-height perturbation at article, clock supports, cavities and transfer optics;
5. vibration, tilt and acoustic drive across the analysis band;
6. RF/optical leakage and source power/load changes, including sham commands;
7. reference phase/frequency step, link-delay change, comb-mode/transfer-oscillator swap, and acquisition timestamp offset;
8. pressure, humidity and gas-flow changes where paths are exposed.

Estimate transfer functions on training blocks; validate them on held-out amplitudes and waveforms. Regression against ambient variation does not replace injection. Failure to span the actual exposure makes the physics block apparatus-inconclusive.

### Gate 3 — state preparation qualification

Demonstrate `u(t)` without using clock output: repeatability, reversal or magnitude steps, hysteresis, relaxation, cycle life, spatial map, source work, heat, force/strain, fields, and drive-off retention if claimed. Use active state, matched dummy, sham command, and nuisance-equivalent controls. Down-select using the README rule before any clock-outcome unblinding.

### Gate 4 — blinded discovery run

Use balanced permuted blocks over:

- baseline `X0`;
- state `X+` and physical reverse `X-` when meaningful;
- at least three registered magnitudes;
- matched thermal control;
- matched electromagnetic control;
- matched mechanical/strain control;
- dummy article and sham actuation;
- two registered specimen-to-clock geometries/distances;
- normal and reference-swap/alternate-transfer conditions.

Operators see only safety-required instructions. Condition labels and randomization seed are escrowed by commitment hash. Analysts train nuisance/local models on designated blocks, freeze code and checksums, then score held-out blocks. All aborted trials and emergency unblinds remain in custody.

### Gate 5 — confirmation

Repeat the frozen winning or null design after complete shutdown/restart, article remount, clock-role/reference swap, and preferably in a second laboratory. A candidate effect must reproduce out of sample. If feasible, add process C only after its direct material-state nuisance map is separately complete.

## 5. Clock and reference requirements

Clock A and B must differ in species or transition class and have demonstrably non-collinear sensitivity vectors. Two nominally separate copies of one architecture are useful replication but do not satisfy the primary dissimilarity requirement. Clock R must not share the intervention enclosure, power/source path, comb branch, or environmental control loop without those shared paths being separately monitored and injected.

Height is a first-class variable. Survey the effective reference points of A, B, and R before and after remount; log support displacement continuously at a precision justified by the target fractional sensitivity. No “co-located” shorthand substitutes for a height/gradient receipt.

## 6. Intervention geometry

Because coupling range is unknown, register geometry as a factor. Minimum layout uses a symmetric specimen position between A and B plus a translated/far condition and a dummy of matched mass/thermal/electromagnetic loading. The material state witness must resolve the state at every geometry. Geometry scans are exploratory unless their levels were frozen from pilot data; they may not be used to tune the confirmatory model after viewing outcomes.

## 7. Analysis

### Primary estimands

For each common family, estimate `kappa` or the registered kernel coefficients jointly from A/R and B/R while checking A/B closure. Report clock-local coefficients separately. Use block/day as experimental units; account for colored noise and dead time using a method frozen after baseline pilot.

### Rank and identifiability gate

Construct the design matrix from injected nuisance, reference/link, drift, and registered local-state bases. Compute singular values and the projection of `(1,1)` onto its column space across the target bandwidth. If common mode is not resolvable at the preregistered condition threshold, do not fit or report H-C as identified.

### Model comparison

Compare N, L, R, C1, C2, CD, and CH using one frozen predictive criterion on held-out blocks. Report absolute residuals, predictive intervals, transfer-function validation, and sensitivity to permitted analysis variants. A favorable information criterion alone cannot pass H-C; every Gate-4 discriminator must pass.

### Equivalence and finite null

Set equivalence margins from pilot stability, independently motivated device relevance, and achievable state interval before the confirmatory run. For linear response report `|kappa| < kappa_95` over the named material, normalized coordinate, interval, geometry, bandwidth, averaging time, and confidence construction. For dynamic response report a bound on the preregistered kernel norm over `[0,Omega]`. Never report zero or “time unaffected.”

### Multiple testing

One primary family, state coordinate, bandwidth, geometry contrast, and averaging window are confirmatory. All others are multiplicity-controlled secondary tests or explicitly exploratory. No post-unblinding axis, sign, lag, subset, or normalization changes may be relabeled confirmatory.

## 8. Classification rules

- **Finite null:** common families inside equivalence bounds; publish the tested-domain limits.
- **Clock-local:** state-linked response differs by clock or is absorbed by independently calibrated local response.
- **Common nuisance/reference:** apparent shared component is reproduced by injection, disappears on reference/transfer swap, or lies in nuisance span.
- **Common-clock candidate:** H-C passes every gate on held-out and remount data.
- **Cross-process candidate:** H-X passes with process C and its nuisance map.
- **Adverse:** frozen sign, symmetry, persistence, or scaling is contradicted.
- **Apparatus-inconclusive:** missing rank, calibration, exposure coverage, custody, or stability prevents inference.

## 9. Calibration and custody

- Calibrate all sensors before and after each run series; include range, nonlinearity, drift, hysteresis, saturation, cross-axis response, timestamp latency, and uncertainty.
- Distribute a common hardware event marker to every digitizer and clock record; independently verify timestamp ordering.
- Raw files are append-only and hashed at closure. Preserve native instrument formats plus documented lossless exports.
- Store calibration certificates, firmware/software versions, wiring photographs, geometry surveys, operator log, randomization commitment, exclusions, and analysis environment.
- Generate derived data only by versioned code from immutable manifests. Preserve every failed and excluded trial with reason codes.

## 10. Safety and stop conditions

Host institutional rules control. Required reviews may include laser safety, ionizing/radiation source control if process C uses one, cryogen/oxygen-deficiency hazards, superconducting magnet exclusion zones, high voltage, RF exposure, strong static magnetic fields and projectile risk, vacuum, pressure, electrical lockout/tagout, lifting/seismic restraint, and chemical handling for specimen preparation.

Hard stops include interlock trip; magnet quench or cryogen alarm; vacuum or cooling loss; overtemperature; unexpected field outside the exclusion boundary; sensor/clock saturation; reference loss; timing desynchronization; specimen fracture; smoke/odor; or any exposure beyond the approved envelope. Safety stops are never overridden to preserve randomization.

## 11. Stopping rule and replication

The run annex fixes minimum and maximum blocks from pilot variance and the smallest effect of interest. No optional stopping on effect direction. Early termination is allowed only for safety, irrecoverable apparatus failure, or a preregistered futility boundary evaluated blind to sign. Replication requires the frozen pipeline, a fresh randomization seed, remount/restart, and a held-out article or second state amplitude.
