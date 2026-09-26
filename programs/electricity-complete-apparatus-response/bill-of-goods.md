# Functional bill of goods

This is a requirements BOM, not purchase authority. Final models, ranges, quantities, safety ratings, and prices follow apparatus down-select and pilot noise measurements.

## 1. Source and energy boundary

| Function | Requirement / acceptance test |
|---|---|
| Isolated energy store | Low-voltage battery or equivalent inside boundary `B`; voltage/current/temperature/state monitored; safe fused disconnect and containment |
| Four-quadrant source/load | Generates registered DC, step, pulse, ramp and bipolar waveforms; sinks/regenerates energy; native telemetry independently checked |
| Current limiting/protection | Hardware current and energy limit independent of software; qualified into open, short, reactive and fault states |
| Source-plane voltage sensing | Differential, isolated, calibrated in both signs over common-mode, temperature, range and bandwidth |
| Source-plane current sensing | Redundant principles where practical (precision shunt plus flux/current probe); phase and insertion characterized |
| DC-bus/regeneration metering | Measures source stock change and returned work rather than relying on commanded values |
| Safe discharge | Redundant bleeders/crowbar, discharge-status sensing, manual verification points and interlock |

## 2. Line, return, and switching

| Function | Requirement / acceptance test |
|---|---|
| Interchangeable two-conductor lines | At least two lengths; characterized geometry, resistance, impedance, delay, dispersion, loss, parasitic C/L, common-mode conversion and thermal coefficient |
| Dedicated return | Physically identified return conductor; no silent chassis/ground return; all alternative return paths measured |
| Reference-plane fixtures | Repeatable `P_S` and `P_L` connections with calibration/de-embedding custody |
| Remote load switch matrix | Open, short, matched, detuned, dummy, storage, absent/sham states; independently sensed state; break-before-make and fault-safe |
| Shield/guard system | Configurable declared bonding; shield current sensing; optical control preferred |
| Switch diagnostics | Contact/device voltage/current, trigger, actual-state sensor, bounce/transition timing and temperature |
| Directional/multiport diagnostics | Optional coupler or VNA-compatible ports; raw ports retained; not treated as ontological measurement |

## 3. Load articles

| Article | Requirement / acceptance test |
|---|---|
| Matched termination | Measured complex impedance and power/temperature coefficient across registered band |
| Characterized short | Low inductance, four-terminal characterization, pulse/thermal rating |
| Characterized open | Defined physical gap, guarded fixture, measured leakage and parasitic capacitance |
| Detuned RLC bank | Independently measured resonance, linewidth/Q, loss, switching repeatability and temperature dependence |
| Dissipative dummy | Terminal response matched to target where possible while changing internal material/mechanical geometry |
| Storage load | Capacitor/inductor/material specimen with state witness, voltage/current/temperature/strain/force instrumentation and safe discharge |
| Geometry-reversal fixtures | Mirror, rotation and source/load-swap configurations with repeatable fiducials and mass/thermal symmetry |

## 4. Mechanical and thermal metrology

| Function | Requirement / acceptance test |
|---|---|
| Whole-apparatus support | Six-axis force/torque transducer or calibrated flexure system; bidirectional calibration, cross-talk, drift, creep and temperature mapped |
| Independent endpoint | Separate vertical/axial force or strain channel of different principle |
| Internal load force | Differential electrode/load-cell or flexure displacement channel; both signs calibrated under voltage-off actuation |
| Strain/displacement | Strain gauges/fiber sensors and optical/capacitive displacement where compatible; electrical pickup characterized |
| Motion/environment | Triaxial accelerometers, tiltmeters, microphones, fixture position/attitude fiducials |
| Temperature | Source, switches, line segments, load, sensors, supports, ambient; self-heating calibrated |
| Heat flow/calorimetry | Insulated enclosure plus heat-flux/calorimetric capability sufficient to reconcile dissipated cycle energy |
| Thermal injection | Metered heaters at source, line, load, switch, sensor and support locations |
| Mechanical injection | Calibrated force/torque actuator, shaker/impulse input, cable/feedthrough pull fixture and tip/tilt injection |

## 5. Electromagnetic and common-mode controls

| Function | Requirement / acceptance test |
|---|---|
| Electric/magnetic probes | Calibrated near-field measurements at source, line, load, shield and support over analysis band |
| Injection probes/coils | Controlled differential/common-mode, electric and magnetic injections spanning observed amplitude/bandwidth |
| Leakage/ground monitors | All shields, chassis bonds, safety grounds, support and auxiliary paths monitored or bounded |
| Isolation | Fiber control/data, isolated power where allowed, battery operation and characterized isolation capacitance |
| Bonding matrix | Safe, repeatable alternate shield/ground topologies used only within reviewed configuration |
| Non-current/electrostatic dummy | Reproduces local electrode voltage/force without the full line exchange where physically possible |

## 6. Timing, acquisition, and custody

| Function | Requirement / acceptance test |
|---|---|
| Common clock | All fast electrical and mechanical channels referenced to one clock or calibrated continuously for skew/drift |
| Hardware markers | Simultaneous electrical/optical event injected into source and load acquisitions to measure latency |
| Simultaneous DAQ | Adequate bandwidth, dynamic range and channel count; raw counts, native timestamps, range/status/overload retained |
| Slow DAQ | Temperatures, heat flow, tilt, environmental and source-stock channels synchronized to fast stream |
| Acquisition controller | Automated opaque recipes, safety supervision separated from analysis, append-only logs |
| Immutable storage | Redundant lossless raw capture, manifest and SHA-256 inventory; analysis never overwrites raw arrays |
| Calibration standards | Traceable voltage, current, resistance, capacitance, inductance, time, force, torque, displacement and temperature references |

## 7. Safety infrastructure

Rated insulated enclosure; interlocks; emergency stop; lockout/tagout; fuses/current limiters; precharge; redundant discharge; touch-safe connectors; fire detection/extinguishing appropriate to the battery and components; thermal trips; smoke monitoring; short-circuit shield; remote camera/operation; warning indicators; PPE and written procedure. RF, mains, vacuum and cryogenic hardware are excluded unless separately reviewed.

## 8. Acceptance tests before physics use

1. every sensor passes before/after calibration and range/clip tests;
2. open, short, matched and detuned standards replay within frozen uncertainty;
3. line/source/load multiport response is repeatable after remount;
4. common-clock skew and latency stay below the registered limit;
5. charge and energy receipts close for low-energy calibration cycles;
6. support response to known electrical, magnetic, electrostatic, thermal, mechanical, acoustic and tilt injections is measured;
7. all alternative return/common-mode paths are detected or bounded;
8. safe discharge and fault response pass after loss of control power;
9. randomization/blinding and immutable capture complete an end-to-end dry run;
10. every component stays within voltage, current, energy, temperature and duty-cycle ratings.

## 9. Cost and readiness bands

### Band A — benchtop electrical receipt pilot

Existing precision source/DAQ, short interchangeable lines, termination standards, low-energy storage load, electrical/thermal sensors, basic force fixture. Intended to qualify timing and charge/energy closure, not high-sensitivity whole-apparatus claims. **Indicative incremental cost:** roughly **USD 8k–30k** if core lab instruments exist; **USD 35k–100k** if they do not.

### Band B — integrated whole-apparatus platform

Battery/fiber-isolated boundary, six-axis metrology, calorimetry, configurable line/load fixtures, automated switch matrix, injection systems and environmental enclosure. **Indicative:** **USD 60k–250k**, dominated by force metrology, digitizers, precision source/load and custom mechanics.

### Band C — independent replication / extended line

Second apparatus, longer controlled line, improved shielding/environment, separate operators/site. **Indicative:** **USD 150k–500k+**. High voltage, RF power, vacuum or cryogenic extensions are separate projects.

These are planning bands, not quotes. Existing assets, required bandwidth, force sensitivity, line length, calorimetric accuracy and safety review can move cost substantially.

## 10. Procurement release criteria

Freeze: maximum voltage/current/pulse/stored energy; load family and bandwidth; line lengths/geometry; smallest effect and equivalence region from pilot; force/torque/energy/charge closure targets; common-mode and timing limits; boundary and crossing inventory; data volume; facility grounding/environment; safety analysis; and independently reviewed schematics/FMEA. Procurement before these choices would buy impressive boxes without a defined experiment.
