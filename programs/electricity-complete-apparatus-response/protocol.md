# Electricity complete-apparatus response protocol

## 1. Objective and evidential boundary

Test a complete source–line–load–return apparatus over full driven cycles and determine whether all observed electrical, energetic, thermal, mechanical, and angular-momentum postings reconcile with calibrated ordinary response. Only then test whether a bounded residual covaries with link completion/readiness.

| Item | Pre-run grade |
|---|---|
| Lumped/distributed circuit response, line impedance, reflection, RLC behavior | Imported established engineering; locally calibrated |
| Voltage, current, charge, work, heat, force, torque, strain | Raw records plus disclosed operational reductions |
| Two-ended completion / no in-transit object | POAMS event architecture and interpretation |
| Sink-exclusive suppression or extra complete-link response | Prospective hypothesis |
| Completion intensity/rate and magnitude | Constitutively open; not supplied by current POAMS premises |
| Instantaneous/nonlocal source response | Not assumed and not a Generation-1 claim |

The experiment can establish an M0 whole-apparatus response and bounds on stated contrasts. It cannot by itself prove an ontology, exact zero, or a universal electrical coupling.

## 2. Frozen apparatus and boundaries

### 2.1 Physical chain

Use a fully specified two-conductor circuit:

1. internal isolated energy store and four-quadrant source `S`;
2. source reference plane `P_S` with independent differential voltage and current sensing;
3. outbound conductor and dedicated return conductor of a characterized line;
4. remote switching/load module at reference plane `P_L`;
5. selectable load states: open, short, matched resistance, detuned RLC, dissipative dummy, and storage load;
6. return reference plane at the source;
7. shields/guards with measured currents and a single declared bonding topology.

The word “remote” means separated within the apparatus; no remote-signalling claim is made.

### 2.2 Complete boundary `B`

Boundary `B` contains source, energy store, switching, both conductors, load, shields, fixtures, internal sensors, and local DAQ front ends. Prefer battery operation and fiber command/data isolation. Every remaining crossing—support, fiber, interlock, thermal path, gas/vacuum line if any, and safety ground—is listed and instrumented or conservatively bounded.

Also freeze sub-boundaries `B_S`, `B_line`, and `B_L`. A quantity may be an internal stock or a crossing for one boundary, but may not be double-counted in the same receipt.

## 3. Raw observables and receipts

### 3.1 Electrical occurrence

Preserve native ADC counts, clock ticks, status bits, and range state for:

- `V_S(t), I_S(t)` at `P_S` with redundant sensors of different principle where practical;
- `V_L(t), I_L(t)` at `P_L`;
- return, shield, chassis, common-mode, leakage, and safety-ground currents;
- intermediate line probes or directional coupler ports used as diagnostics;
- switch command and independently sensed contact/device state;
- source DC-bus voltage/current and regenerated energy channel.

Charge is an operational integral, `Q_k=integral I_k dt`, not proof that a material carrier traversed the line. Terminal work is

\[
W_k=\int_{t_0}^{t_1}V_k(t)I_k(t)\,dt
\]

using registered polarity and reference plane. Report signed and gross work.

### 3.2 Energy receipt

For boundary `B`, require

\[
\epsilon_E= W_{\partial B}^{\rm in}-W_{\partial B}^{\rm out}
-\Delta U_{\rm store}-\Delta U_{\rm source}
-Q_{\rm heat}-W_{\rm mech}-E_{\rm other}.
\]

Each term must be tied to a sensor or a registered conservative bound. State energy of a selected load is measured by a complete charge–hold–recover–discharge cycle; recoverable work is the returned energy at the declared reference plane, not `1/2 CV^2` by assertion. `1/2 CV^2`, `1/2 LI^2`, and imported distributed-line energies are comparators whose parameters are independently calibrated.

### 3.3 Charge/continuity receipt

For each sub-boundary,

\[
\epsilon_Q=\Delta Q_{\rm stored}-\int I_{\partial B}\,dt.
\]

Include stray/reference capacitances, shield and common-mode current, switch displacement current, sensor input currents, leakage, and uncertainty. An open circuit is not expected to have identically zero transient current; the registered test reports a calibrated bound and waveform.

### 3.4 Linear and angular momentum receipt

Record six-axis support force/torque about a frozen origin, independent force/strain, internal load/electrode force and displacement, accelerometry, tilt, acoustic pressure, and all moving-part kinematics. Operational external receipts are

\[
\epsilon_p=\Delta \mathbf p_B-\int \mathbf F_{\partial B}\,dt,
\qquad
\boldsymbol\epsilon_J=\Delta \mathbf J_B-\int \mathbf N_{\partial B}\,dt.
\]

Mechanical stocks and rotations are measured directly. Imported electromagnetic momentum/AM models may be calculated as comparators, but no unmeasured “field momentum” is declared a POAMS receipt. A candidate residual requires closure or a stated upper bound for conductor, electrode, shield, magnetic component, source, fixture, support, and environmental reactions.

## 4. Preregistered condition matrix

Every condition uses the same command waveform, analysis pipeline, acquisition bandwidth, and full-cycle window where safe.

| State | Physical implementation | Purpose |
|---|---|---|
| `OPEN-L` | physical gap at `P_L`, characterized parasitic C/leakage | finite open-state transient and source baseline |
| `SHORT-L` | low-inductance characterized short | high-current/low-load-voltage endpoint and protection test |
| `MATCH-L` | measured termination matched over registered band | minimized ordinary reflection comparator |
| `DETUNE+/-` | RLC load shifted by preregistered linewidth offsets | readiness/selectivity gradient |
| `DUMMY-R` | dissipative load matched in terminal response but mechanically isolated/substituted | separates load heat/force/material state |
| `STORE-L` | characterized capacitor/inductor/material specimen | recoverable work, retention and strain cycle |
| `ABSENT-L` | module removed with same fixture/shield geometry | distinguishes device presence from selected connection |
| `SHAM` | commands and trigger traffic with source disabled | pickup/software baseline |

Cross these with at least two line lengths, polarity reversal, waveform reversal, source-channel swap, normal/mirrored/rotated geometry, conductor-pair swap, shield-bond topology, and whole-platform orientation. Match peak voltage/current/energy where physically possible; where not, estimate contrasts conditional on measured state rather than pretending equivalence.

Geometry controls include: straight parallel pair, folded/spooled pair with preserved terminal response, mirror image, 180-degree rotation on the support, source/load end swap, and dummy mass/thermal symmetry. Geometry changes must be recharacterized electrically.

## 5. Competing models frozen before data

### M0 — calibrated ordinary network plus apparatus response

Predict the complex terminal response from measured network parameters or an identified state-space/multiport model. Feed its measured current, voltage, temperature, magnetic, vibration, and switch trajectories through independently calibrated mechanical/thermal transfer functions. Residuals are instrument noise plus locked model discrepancy.

### M1 — ordinary network with omitted parasitic/environment path

Allows additional measured common-mode, shield, ground, radiative, mechanical, or thermal coupling. Discovery of such a path improves M0; it is not a POAMS result.

### M2 — additional local complete-link state term

Adds a bounded response after the apparatus's ordinary local/network response time:

\[
y(t)=y_{\rm M0/M1}(t)+a\,g(r_L,\phi,\text{geometry},H;t)+\xi(t).
\]

The basis `g`, sign, onset window, and scaling variables are frozen from pilot data without condition unblinding. `a=0` is the nested null.

### M3 — pre-ordinary-response/nonlocal term

Not adopted. It may only be tested in a separately registered, synchronization-qualified extension with explicit pre-response bins, no-anticipation alternatives, cable/feedthrough exclusion, and false-positive control. Generation 1 neither assumes nor claims it.

### M4 — exact sink exclusivity

Exact zero is not an observable model. Operationally, define a norm of source-side or external response in `OPEN-L`/`ABSENT-L` and report an upper confidence bound over a stated band, window, geometry, and parasitic-sink census. Current premises do not supply a nonzero expected contrast or scaling law.

Model selection uses held-out blocks and complexity penalties fixed before unblinding. A better fit without successful out-of-sample prediction is exploratory.

## 6. Staged protocol

### Gate 0 — safety and metrology qualification

1. freeze drawings, reference planes, polarity, coordinate frames, boundary inventory, and energy ceiling;
2. calibrate voltage/current/charge channels in both signs across bandwidth, common-mode voltage, temperature, and range transitions;
3. calibrate force/torque/strain/displacement, heat-flow, temperature, tilt, vibration, acoustic, magnetic, and timing channels;
4. measure line two-port/multiport response, loss, characteristic impedance, delay, dispersion, parasitics, common-mode conversion, and switch behavior over the declared band;
5. verify common clock and channel latency with simultaneous injected markers;
6. qualify open, short, matched, detuned, dummy, and storage states independently;
7. demonstrate charge and energy closure on slow, low-energy calibration cycles;
8. map support and internal-mechanical response under direct injections;
9. demonstrate randomization, opaque labels, immutable raw capture, range/clip retention, and replay;
10. pass current, voltage, thermal, discharge, enclosure, interlock, and power-loss safety tests.

Failure is an apparatus failure, not a physics null.

### Gate 1 — quasi-static complete cycles

Use slow charge–hold–recover–discharge waveforms where distributed transients are negligible by the measured comparator. Compare storage, dissipation, internal force/strain, and whole-support response across load/material states and polarity. This establishes state-energy and mechanical baselines.

### Gate 2 — transient termination matrix

Apply registered steps/pulses with safe matched peak states across `OPEN-L`, `SHORT-L`, `MATCH-L`, `DETUNE`, `DUMMY-R`, `STORE-L`, `ABSENT-L`, and `SHAM`. Capture source and load planes continuously before, during, and after switching until all storage/thermal settling criteria are met.

### Gate 3 — readiness and geometry

Sweep detuning in registered linewidth units and repeat selected conditions under mirror, rotation, line-length, source/load swap, conductor-pair swap, and shield topology. A candidate completion-state term must follow its predeclared readiness coordinate and physical geometry rather than a cable, bench, sensor, or ambient axis.

### Gate 4 — complete-apparatus mechanical response

Repeat qualified cycles on the six-axis platform with internal force/strain and all environmental channels active. Compare the integral of local electrode/fixture reactions with the external support wrench. Test matched electrical terminal trajectories produced with different internal load geometries and matched mechanical/thermal trajectories produced with different electrical states.

### Gate 5 — blinded confirmatory campaign

Run balanced permuted blocks, frozen exclusions, maximum blocks, and stop rules. The pilot is excluded. Unblind only after before/after calibrations pass and the raw bundle, code, manifest, and opaque reduction outputs are hashed.

### Gate 6 — replication

Repeat after disassembly/remount and with a second line/load article. A separate apparatus/site is required before “replicated response.”

## 7. Direct artifact injections

Fit transfer functions without physics labels and lock them before confirmatory unblinding.

| Path | Direct injection / control | Candidate fails when |
|---|---|---|
| Differential pickup | isolated known voltage/current waveforms into each front end | endpoint is reproduced by channel transfer/cross-talk |
| Common-mode/ground | injected common-mode voltage/current, alternate bond, isolation transformer/emulator | common-mode or return path predicts contrast |
| EMI | calibrated electric/magnetic near-field probe and radiated susceptibility sweep | waveform/scaling is reproduced |
| Magnetic force/torque | calibrated coil/current loop and non-current dummy | support/internal response follows measured field/gradient |
| Electrostatic force | calibrated electrode voltage with blocked line exchange or local dummy capacitor | local force/strain closes response |
| Thermal | metered heaters at source, line, load, switch, sensor, support; matched temperature trajectories | thermal transfer predicts candidate |
| Mechanical | calibrated force/torque actuator, shaker, impulse, cable pull, fixture preload | support or strain transfer predicts signal |
| Acoustic | speaker/structure-borne injection | microphone/accelerometer transfer closes it |
| Tilt/gravity | tip/tilt injection and apparatus rotation | force follows projection/cross-axis response |
| Switching | dummy switch, snubber variation, optical/electrical trigger swap | contact/device impulse or trigger pickup explains it |
| Software/timing | synthetic events, replay, channel permutation, sample loss/skew injection | pipeline creates, moves, or amplifies effect |
| Analyst | null labels, duplicated blocks, blind sign reversal | result depends on labels or optional choices |

Injections span the candidate amplitude and bandwidth. Extrapolation beyond calibrated range is labeled and cannot close a residual by decree.

## 8. Blinding, randomization, and custody

Use balanced permuted blocks stratified by load state, polarity, amplitude, line length, geometry, and day. Safe state changes and thermal washout may constrain order but are fixed before viewing endpoints. Operators receive opaque recipes where safety permits; analysts see opaque labels. Freeze and hash randomization seed, escrow map, waveform library, analysis windows, filters, model bases, exclusions, multiplicity plan, maximum blocks, and stop rules.

Preserve every trial, including open/short trips, clipping, relay bounce, incomplete settling, interlock stops, dropped packets, manual interventions, and emergency discharge. No trace is overwritten or “cleaned.”

## 9. Primary estimands and analysis

Primary endpoints are selected before confirmatory acquisition from:

- whole-cycle energy residual `epsilon_E` and normalized closure error;
- charge/continuity residual `epsilon_Q` at each sub-boundary;
- recoverable-work fraction and dissipated energy;
- peak/integrated internal electrode force and strain;
- whole-apparatus force/torque projection, impulse, and work;
- external-minus-internal linear/angular momentum receipt;
- source-side readiness contrast and detuning response;
- latency interval relative to hardware markers, with no pre-response claim in Generation 1.

For a paired condition contrast,

\[
\Delta y_{a,b}=y_a-y_b,
\]

and for reversal parity,

\[
y_{\rm odd}=[y(+)-y(-)]/2,\qquad y_{\rm even}=[y(+)+y(-)]/2.
\]

Use block—not sample—as the experimental unit; model autocorrelation and day/remount effects. Report raw means, intervals, equivalence tests, injection-predicted contribution, held-out residuals, all vector components, and sensitivity to frozen exclusions. Correct for the preregistered family of load, geometry, mechanical, and timing contrasts.

No “anomalous energy” is reported if the residual is within combined calibration/model uncertainty, if any unmeasured boundary channel remains material, or if the result vanishes under held-out prediction/remount.

## 10. Pilot sizing and release

No numerical sample size is honest before pilot covariance exists. An unblinded, non-claim pilot includes all conditions and injections. Estimate block-level standard deviation `s_d`, autocorrelation/design effect, calibration floors, model-discrepancy floor, remount/day variance, smallest technically meaningful effect `delta`, and equivalence half-width `Delta_eq`.

For a balanced paired approximation,

\[
n_{\rm pairs}\approx
\left[{(z_{1-\alpha/2}+z_{1-\beta})s_d\over\delta}\right]^2,
\]

then inflate for multiplicity, exclusions, heterogeneity, and design effect. Simulate the actual block/model pipeline and freeze the maximum count. Pilot data never enter the confirmatory inference.

Release requires: electrical and mechanical sensors do not clip; common-mode rejection is demonstrated; timing skew is below the smallest registered bin; energy/charge closure uncertainty is below the equivalence region; direct artifact paths are estimable; thermal washout is practical; run count is feasible; and all safety gates pass.

## 11. Decision language and finite nulls

- **Preparation not qualified:** the intended load/readiness/material state was not instantiated; no test.
- **Ordinary apparatus response:** calibrated network plus injected electrical/thermal/mechanical paths explain the record.
- **Scoped null:** the registered extra contrast is equivalent to zero within stated sensitivity, band, windows, line/load family, energy range, geometry, and model class.
- **Unresolved residual:** some controls survive but boundary closure, model discrepancy, scaling, remount, or replication is incomplete.
- **Promoted candidate response:** frozen sign/order/scaling, receipts, all artifact controls, held-out prediction, and remount pass; independent replication remains required.
- **Replicated response:** separate apparatus repeats the registered behavior and receipts.

A finite null can bound an extra complete-link term for the tested apparatus and retire a proposed sign/scaling in that domain. It cannot prove that “nothing travels,” that all open circuits are exactly silent, that all completion laws vanish, or that no other geometry/material could respond. An adverse sign or ordinary explanation is retained, not renamed.

## 12. Safety

Generation 1 is intentionally low voltage and current limited, but all capacitors, inductors, batteries, pulse-forming elements, and long lines can store hazardous energy. Use a documented maximum stored-energy inventory; current limiting; fusing; precharge; bleeders; redundant automatic discharge; visible discharge verification; interlocked enclosure; guarded contacts; rated switches, cables, connectors, loads, insulation and clearances; thermal and smoke monitoring; fire-compatible battery containment; remote operation; emergency stop; and lockout/tagout.

Short-circuit tests require a separately reviewed current/time envelope, arc suppression, protective enclosure, and abort logic. No person touches the apparatus until two independent voltage checks confirm the safe state. Whole-platform fixtures must tolerate electromagnetic force, thermal expansion, switch impulse, and cable reaction. RF/microwave operation, vacuum, cryogens, or mains connection are outside Generation 1 unless separately designed and reviewed.

Safety overrides blinding. Every trip remains in raw custody.
