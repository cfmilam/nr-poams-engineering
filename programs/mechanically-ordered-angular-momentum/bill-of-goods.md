# Functional bill of goods

No vendor, part number, purchase, or price quote is authorized. Final ranges follow the pilot; safety-critical components require qualified engineering review.

| Group | Item | Minimum function / acceptance test |
|---|---|---|
| Rotor | At least 2 interchangeable rotors | Certified material/geometry; measured mass, centre, inertia tensor, balance, runout, safe-speed margin; one held out |
| Control | Matched dummy inertia | Same mass/inertia and mount interface with no high-speed rotor state, or a registered measurable mismatch |
| Spin drive | Bidirectional motor/brake or air/magnetic drive | Controlled `+/-` spin, coast and braking; torque/reaction measurable; polarity/channel swaps; regenerative work metered |
| Rate/attitude | Redundant tachometry + 3-D axis tracking | Independent rate channels; full attitude with calibrated latency; survives maximum rate and enclosure |
| Gimbal | Three-axis free/lockable assembly | Quantified free friction, backlash and stops; instrumented locks; reproducible intermediate restraint |
| Platform | Translation and local-orbit stage | Declared centre/radius/plane/rate; matched translation/orbit profiles; position/velocity/acceleration/jerk recorded |
| Reaction | Six-axis force/torque transducers | At all external mechanical supports; bidirectional calibration, overload margin, bandwidth, cross-talk matrix |
| Support | Independent vertical-force/strain channel | Different transduction principle where practical; synchronized native output |
| Shaft/drive | Torque and work instrumentation | Shaft torque/reaction plus synchronized voltage/current and returned energy; traceable sign |
| Mechanics | Instrumented bearings/mounts | Preload/strain, temperature, vibration and replaceable bearing/control configurations |
| Inertia | Calibration fixtures | Pendulum/bifilar/torsional or equivalent measurements for rotor/platform inertia tensors with covariance |
| Motion | Optical metrology | Independent platform/rotor trajectory and runout; calibrated coordinate transform to support frame |
| Thermal | Distributed thermometry and heat-flow channels | Rotor-near, bearings, motor, frame, supports, cables, chamber; response/self-heating characterized |
| Injection | Programmable heaters | Bearing, motor, frame, cable and sensor locations; metered energy and matched trajectories |
| Injection | Calibrated force/torque actuators | Both signs and all endpoint axes over analysis band; known lever arms |
| Injection | Tip/tilt stage or actuator | Safe known angular perturbations; inclinometer verification |
| Injection | Shaker/impulse system | Structural transfer-function mapping below safe rotor limits |
| Environment | Accelerometers, microphones, tilt sensors | Resolve rotor/platform harmonics, building motion, acoustic and gravity-projection paths |
| Atmosphere | Rated chamber and pressure/gas instrumentation | Ambient-to-selected reduced pressure; pump/feedthrough reactions measurable; overspeed containment remains valid |
| Magnetic | Three-axis field/gradient probes and injection coil | Maps motors/rotor/environment; reproduces measured field changes without primary state |
| Electrical | Isolated voltage/current/ground monitors | Captures controller, ground, leakage, regeneration and pickup; supports deliberate injection |
| Cables | Feedthrough force/torque sensing | Directly measures or conservatively bounds cable/hose/slip-ring reaction |
| Timing | Common reference and hardware markers | Measures channel skew, latency and drift; all devices timestamp raw samples |
| Acquisition | Simultaneous DAQ | Sufficient channels/rate/dynamic range; anti-aliasing; raw counts and status/overrange bits retained |
| Compute | Acquisition controller + immutable storage | Automated recipes, blinding, append-only logs, versioned code, lossless raw capture and hashes |
| Safety | Rated containment, guards, interlocks, redundant overspeed, E-stop | Documented stored-energy/fragment basis; enclosure, pressure, vibration, temperature and power-loss trips |
| Service | Alignment, balancing, NDT/inspection capability | Acceptance records before first spin and at frozen service intervals |

## Procurement release criteria

Freeze from a selected concept and non-physics pilot:

1. rotor material, dimensions, mass/inertia, maximum kinetic energy, operating speeds, proof/safe-speed policy, containment basis, and service interval;
2. platform radius, rate, acceleration/jerk, payload, orbit-plane range, and gimbal travel;
3. support load, full-scale torque, noise spectra, bandwidth, drift, cross-talk, and smallest effect/equivalence region;
4. atmosphere range, vacuum reactions, thermal load, heat rejection, and pump-isolation plan;
5. DAQ channel inventory, rates, clock tolerance, data volume, and isolation;
6. boundary `B`, every feedthrough/crossing, and where each AM/energy stock is measured;
7. direct-injection ranges covering the observed nuisance envelope;
8. site floor/tilt/vibration/magnetic survey and allowable operating zone;
9. independently reviewed rotor dynamics, containment, braking, failure-mode, and emergency procedures.

## Cost/readiness bands

- **Bench metrology demonstrator:** low-to-moderate rotor energy, ambient enclosure, stationary/steady/transient branches. Suitable for sensor and artifact qualification only.
- **Integrated orbit/gimbal rig:** custom platform, six-axis reactions, optical tracking, instrumented locks, automated reversal. Main Generation-1 physics apparatus.
- **Vacuum/high-energy replication rig:** substantial chamber, containment, remote operations, redundant safety, and independent build. Release only after the integrated rig is qualified.

Dollar estimates are intentionally deferred until the safety envelope, sensor noise, platform topology, and existing laboratory assets are inventoried. A cheap uncontrolled high-speed rotor would be false economy with teeth.
