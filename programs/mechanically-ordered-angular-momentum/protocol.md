# Mechanical gyro ordered-angular-momentum protocol

## 1. Objective and evidential boundary

Test whether a characterized mechanical rotor and containing motion exhibit a reproducible whole-apparatus force, torque, impulse, or work component odd under a matched reversal of local spin/orbit sense after ordinary transfer paths are measured.

| Item | Pre-run grade |
|---|---|
| Rigid-body kinematics, bearing mechanics, motor control, gyroscopic torque | Imported established apparatus physics, locally calibrated |
| Rotor/platform angular momentum and energy | Operational reductions from measured inertia, attitude, rate, force, torque, voltage, and current |
| Co/anti settlement ordering | POAMS organizing hypothesis; no magnitude supplied |
| State-linked support response beyond ordinary paths | Prospective hypothesis |
| Twist/writhe assignment | Open unless a physical framed curve is measured |
| Retained state | Open; requires an independent post-drive witness |
| Prior gyro reports or videos | Motivation only; not local M0 evidence |

No levitation, propulsion, variable-`G` coefficient, instantaneous response, universal coupling, or cross-scale transfer is claimed.

## 2. Frozen accounts and raw observables

Freeze a single physical boundary `B`. Each component is either an internal stock or a boundary crossing, never both. At minimum,

\[
\mathbf J_B=\mathbf S_{r}+\mathbf L_{p},\qquad
\boldsymbol\epsilon_J=\Delta\mathbf S_r+\Delta\mathbf L_p-\int\mathbf N_{\partial B}^{\rm in}dt.
\]

`S_r` is only the test rotor's intrinsic bulk spin about its centre of mass. `L_p` contains all other in-boundary angular-momentum stocks: rotor-centre orbit, platform, gimbals, bearings, motor/brake rotors, and other moving parts. Boundary torque is measured at every mechanical/electrical/fluid interface.

Primary native records:

- six-axis support force/torque counts about a frozen origin;
- independent vertical-force or strain channel;
- rotor tachometer/encoder counts and full three-axis rotor-axis attitude;
- platform position, velocity, acceleration, jerk, orbit centre/radius/plane/rate;
- motor/brake shaft torque or reaction, voltage/current, regenerative return, and controller state;
- gimbal angles, stops, lock force, bearing temperatures, preload/strain, and vibration;
- boundary temperature/heat flow, pressure, gas flow, acoustic pressure, tilt, magnetic field, ground/leakage current, cable/hosing reaction;
- UTC/common-clock ticks, hardware markers, range/overload/status bits, and all commands.

Derived endpoints are `N_odd,q`, `P_odd`, integrated odd impulse/work, vector-AM closure, energy closure, attitude trajectory, latency bound, and state-conditioned support wrench. Raw support counts—not a corrected coefficient—remain the custody anchor.

## 3. Hypotheses by physical branch

### H-S — steady spin

At constant measured `|S_r|`, fixed attitude, no platform orbit, and after settling, compare `+S`, `-S`, low-spin, rotor-off, dummy-inertia, and sham-command states. H0-S is equivalence inside the frozen region. A contrast that follows speed-squared, temperature, imbalance, bearing state, magnetic field, controller polarity, or cable reaction is ordinary unless independently separated.

### H-T — acceleration and reversal transients

Measure complete paths during spin-up, coast-down, braking, and fixed-magnitude reversal. Equal endpoint kinetic energies do not imply zero impulse, gross work, or dissipation. H1-T requires the odd residual to survive matched angular acceleration, jerk, controller-channel swaps, dummy inertia, and reaction/energy closure.

### H-O — containing orbit

Use the EXP-S3 co/anti × free/locked matrix. H1-O requires a response to appear with the declared containing orbit, reverse with `S_r·L_containing`, survive translation controls, track the local orbit plane rather than apparatus bias, and close both free and locked branch books.

### H-E — Earth-orientation dependence

Record Earth-fixed and inertial coordinates for every trial. Compare mirrored apparatus azimuths, vertical/horizontal rotor axes, reversed rotor sense, and—if the campaign duration and drift allow—sidereal phase. The preregistered competitors are: Earth-axis dependence, local-vertical dependence, apparatus-fixed dependence, magnetic-field dependence, thermal/day dependence, and null. No Earth-axis claim is made from a single orientation or time-of-day correlation.

### H-W — twist/writhe channel

Operationally label rotor body spin and platform centre-of-mass winding. Do not call them topological `Tw` and `Wr` unless a material/ribbon centreline and framing are imaged in 3-D, `Lk=Tw+Wr` is reduced under frozen closure/reconnection rules, and the corresponding boundary action account is measured. A sign response alone can distinguish operational branches, not prove topology.

### H-R — retained state

After drive/orbit/rotor commands cease, begin analysis only after registered thresholds for rate, vibration, controller current, temperature derivative, bearing relaxation, and platform motion are crossed. H1-R requires an independent signed state coordinate, dose relation, commanded reverse/erase, support covariance, remount repeat, and closed boundary receipt. Otherwise report drift or unexplained occurrence, not memory.

## 4. Apparatus stages and gates

### Gate 0 — metrology qualification

Pass before confirmatory acquisition:

1. calibrate six-axis force/torque in both signs across load, bandwidth, orientation, and temperature;
2. measure rotor/platform inertia tensors and attitude/rate calibration independently;
3. verify common-clock skew and latency by injected markers;
4. map bearing friction/preload versus speed, sign, orientation, temperature, and pressure;
5. map rotor imbalance, runout, harmonics, structural modes, gimbal friction, and controller ripple;
6. inject known force, torque, tilt, vibration, heat, magnetic field, ground current, cable pull, pressure, and acoustic signals and estimate transfer functions into every endpoint;
7. characterize empty, dummy-inertia, rotor-off, low-spin, free, and locked configurations;
8. demonstrate end-to-end randomization/blinding and immutable raw capture;
9. demonstrate safe containment, overspeed trip, brake, vacuum and power-loss response;
10. close AM and energy ledgers for ordinary calibration maneuvers within frozen thresholds.

Gate-0 failure is an apparatus failure, not a POAMS null.

### Gate 1 — steady-spin factorial

Randomize spin sign × speed level × axis orientation × platform stationary. Require settled windows and matched thermal/bearing age. Repeat with controller polarity/channel swap and passive coast windows. This tests steady support covariance without importing orbit.

### Gate 2 — path/transient factorial

Randomize spin-up, coast-down, controlled brake, and physical sign reversal at matched `|dS/dt|`, duration, temperature, and platform state. Preserve endpoints and all rejected/aborted paths. Report signed and gross work separately.

### Gate 3 — translation-null and orbit-onset

Run matched straight translations and closed local orbits with the same speed/acceleration/jerk envelope. Require any orbit candidate to begin only after nonzero winding about the declared centre and to be absent from matched translation within sensitivity.

### Gate 4 — plane tracking and orientation

Use at least three orbit-plane normals and mirrored support geometries. Cross rotor sign, orbit sign, apparatus azimuth, and axis attitude. A candidate must track the preregistered physical vector, not camera, bench, gravity-gradient, ambient magnetic, or support axes.

### Gate 5 — free versus locked branch

Compare `CO-FREE`, `ANTI-FREE`, `CO-LOCK`, and `ANTI-LOCK`. Free-axis attitude and locked-branch support/impulse/work/heat must reconcile quantitatively. Grinding or rapid spin-down explained by preload/friction is ordinary response.

### Gate 6 — pump-off/retention search

Optional and downstream. It begins only if an independent persistent coordinate exists. Run write/sham/reverse/erase/no-operation conditions after all settling thresholds. A balance offset alone cannot pass.

### Gate 7 — replication

Repeat the frozen confirmatory package after disassembly/remount and with a second rotor. A separate apparatus is required before “replicated exchange.”

## 5. Reversal and null matrix

Every primary condition receives the same reduction pipeline.

| Factor | Levels / purpose |
|---|---|
| Rotor | `+S`, `-S`, low-spin, off, matched dummy inertia |
| Containing motion | `+L`, `-L`, straight translation, stationary, sham orbit |
| Constraint | free gimbal, locked gimbal, calibrated intermediate restraint |
| Axis | vertical, horizontal N-S, horizontal E-W, oblique registered orientation |
| Support | normal, mirrored, rotated, stiffness-changed, sensor swap |
| Drive | normal channel, channel/polarity swap, passive coast, sham commands |
| Atmosphere | qualified ambient and reduced pressure/vacuum levels |
| Time | balanced randomized blocks; sidereal/solar covariates recorded, not fished |

Odd/even decomposition is performed for rotor reversal, orbit reversal, simultaneous reversal, apparatus mirror, and drive polarity. A true physical reversal must be verified from measured vectors; command labels are insufficient.

## 6. Direct artifact injections

For each nuisance, inject through the same physical path, spanning the observed amplitude and bandwidth. Freeze the response model on injection data before unblinding physics labels.

| Artifact | Direct injection / diagnostic | Failure condition |
|---|---|---|
| Force/torque cross-talk | calibrated masses, electrostatic/voice-coil forces, known lever torques on each axis | candidate reproduced within uncertainty |
| Tilt / gravity projection | calibrated tip/tilt actuator and inclinometer | endpoint follows measured tilt transfer |
| Vibration / structural resonance | shaker/impulse hammer over rotor/platform harmonics | spectral/coherent reproduction |
| Bearing friction/preload | controlled preload, lubrication/temperature/pressure sweep, dummy rotor | odd term tracks bearing state |
| Imbalance/runout | known trial mass and phase; speed sweep | harmonic scaling explains endpoint |
| Motor/controller reaction | locked shaft or reaction fixture; channel/polarity swap; regenerative load | controller state reproduces sign |
| Cable/hose force | calibrated pull/twist at feedthrough over motion envelope | transfer closes residual |
| Magnetic coupling | calibrated coil/source and nonmagnetic dummy; field map | response follows field/gradient |
| Ground/electrical pickup | injected common/differential current and isolated acquisition | pickup reproduces waveform |
| Thermal | heaters at bearing, motor, frame, cable, sensor with matched trajectories | thermal model predicts candidate |
| Aerodynamic/pressure | pressure sweep, spin-direction swap, stationary airflow where safe | windage/convection explains signal |
| Acoustic | calibrated speaker/structure-borne injection | microphone/support transfer closes it |
| Software/timing | synthetic marker, replay, label permutation, dropped-sample injection | pipeline creates or shifts effect |

An injection need not look visually identical; it must bound the calibrated transfer at the endpoint. Unmeasured paths block residual language.

## 7. Blinding, randomization, and custody

Use balanced permuted blocks stratified by rotor, axis, constraint, speed, and day. The scheduler may enforce safe washout but does not see support data. Operators receive opaque recipes except where safety requires the real condition; analyst files use opaque labels. Freeze and hash the seed, condition map escrow, run annex, calibration bundle, exclusions, maximum blocks, and stopping rule.

Unblind only after acquisition completes or a registered safety/data-quality stop fires, before/after calibrations pass, frozen exclusions are applied, and raw/derived bundles are hashed. Preserve aborted runs, overspeed/overrange states, controller trips, grinding, lock failure, interventions, and emergency unblinds.

## 8. Analysis

Choose before acquisition a signed torque projection `q` and independent boundary-power channel:

\[
N_{\rm odd,q}(t)=\frac{N_{\rm anti,q}(t)-N_{\rm co,q}(t)}2,
\qquad
P_{\rm odd}(t)=\frac{P_{\rm anti}(t)-P_{\rm co}(t)}2.
\]

Integrate over frozen windows for odd impulse and work. Report all vector/even components, not just the favorable projection. Primary inference uses block as the experimental unit and includes only preregistered nuisance covariates validated on injection data. Account for autocorrelation; sample count is not trial count. Report interval estimates and equivalence against a frozen region, with family-wise allocation across steady, transient, orbit, orientation, and retention branches.

Required diagnostics: AM and energy closure; state matching; latency at instrumental resolution; speed/rate/radius scaling; orientation harmonics; reversal parity; spectrum and coherence; injection prediction residual; dummy/low-spin response; free/locked redistribution; remount/rotor heterogeneity; and sensitivity to frozen exclusions. Do not infer total power as `Nω` unless that exact boundary channel and relative rate are measured and agree with the independent power ledger.

## 9. Pilot sizing and confirmatory release

No honest numerical sample size exists before the apparatus covariance is measured. Conduct an unblinded, non-claim pilot containing all nulls and injections. From independent pilot blocks estimate:

- block-level standard deviation `s_b` of the primary odd contrast after the frozen filter;
- autocorrelation/effective block spacing and day/remount variance;
- calibration and drift floors;
- the smallest technically meaningful effect `δ` and equivalence half-width `Δ_eq`.

For a two-sided balanced paired approximation,

\[
n_{\rm pairs}\approx\left[\frac{(z_{1-\alpha/2}+z_{1-\beta})s_d}{\delta}\right]^2,
\]

then inflate for multiplicity, heterogeneity, exclusions, and design effect. For equivalence use the stricter block count needed to place the registered interval inside `[-Δ_eq,+Δ_eq]`. Simulate the actual mixed/block design from pilot residuals and freeze a maximum count. Pilot data do not enter the confirmatory test.

Release to confirmatory work only when: calibration uncertainty is below the equivalence region; ordinary calibration maneuvers close; injected artifacts are estimable; the DAQ does not clip; condition matching is achieved; the required count/runtime is practical; and safety/containment tests pass.

## 10. Decision language and finite nulls

- **State/preparation not achieved:** branch not tested.
- **Ordinary apparatus response:** direct injection, dummy, reaction, or closure account explains the signal.
- **Scoped null:** qualified preparation is equivalent to zero at the stated sensitivity, bandwidth, geometry, speeds, orientations, pressure, and analysis window.
- **Unresolved candidate:** odd residual survives some controls but closure, scaling, topology, retention, or replication is incomplete.
- **Promoted candidate exchange:** sign reversal, AM/energy closure, complete control survival, free/locked prediction, and out-of-sample scaling pass; replication still pending.
- **Replicated exchange:** separate apparatus repeats the frozen sign and scale behavior.

A finite null excludes only the registered coupling family over the achieved parameter volume. It can retire a proposed sign or scaling law for that domain, bound engineering authority, and prevent coefficient transfer. It does not prove all spin-support couplings impossible, null YIG, or adjudicate universal ontology.

## 11. Safety

Use a rated rotor, containment vessel, overspeed protection, remote operation, guarded pinch/gimbal zones, verified balance, crack/NDT inspection as appropriate, redundant tachometry, independent emergency stop, safe braking/dump load, vacuum-rated feedthroughs, chamber interlock, projectile exclusion zone, and written stored-energy limits. Calculate maximum rotor kinetic energy and fragment containment before spin. Establish aborts for overspeed, vibration, bearing temperature, pressure, controller fault, enclosure opening, sensor saturation, and abnormal sound. Power loss must drive a known safe state. No person occupies the rotor plane during energized operation. Safety overrides blinding and all interventions remain in custody.

## 12. Downstream meaning

A qualified result can constrain the operational twist-versus-orbit partition, support-response engineering, navigation claims, and comparison with YIG/EdH-Barnett accounting. It cannot alone establish topological writhe, retained memory, a gravitational law, propulsion, or a universal coefficient.
