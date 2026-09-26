# Functional bill of goods

No pricing, vendor selection or procurement authority is supplied. Final specifications come from the selected platform and Gate-0 pilot.

| Group | Item | Minimum function / acceptance test |
|---|---|---|
| Device | Superconducting loop/weak-link devices, ≥2 + witness | Stable IDs and geometry; measured critical temperature/current, inductance, mutual inductance, state range and write margin; one held out |
| Controls | Open-loop/dummy, shorted-turn and electronics-only fixtures | Match substrate, wiring, thermal mass and mutual pickup while removing the retained-state degree of freedom |
| Optional | Single-vortex/pinned-vortex device | Count/location independently resolvable; controlled pinning and reset; only after Gen-1 loop qualification |
| Cryogenic | Cryostat/refrigerator and temperature stage | Stable across selected operating range; known cooling power; vibration and magnetic signatures measured; safe quench/relief |
| Thermal | Device-stage thermometry and heaters | Calibrated at operating temperature; time constants and self-heating measured; local and matched-control injection |
| Magnetic | Nested shielding, degauss/reset method, vector field source | Residual field and gradients measured; both polarities; remanence history reproducible |
| Magnetic | Three-axis field probe(s) | Qualified for relevant temperature/location or transferable warm calibration; logs ambient and source fields |
| Write | Bipolar pulse/current/flux source | Full native V/I waveform; programmable polarity/area; isolated return; compliance and ringing measured |
| Read | DC/RF SQUID or equivalent flux sensor | Resolves adjacent states with frozen margin; native output and feedback retained; reset, saturation and hysteresis observable |
| Read | Independent/read-chain witness | Different channel or sensor where feasible; exposes electronics latching and dropouts |
| Coupling | Calibrated input/read mutual-inductance structures | Geometry documented; coupling measured both signs and versus temperature |
| Electrical | Low-noise amplifiers, filters, attenuators, isolators | Noise, delay, gain, phase, heating and saturation calibrated in situ |
| Reaction | Source V/I metrology and calorimetry | Captures write/read energy, returned energy and heat with uncertainty |
| Reaction | Torque/force/strain or conservative boundary sensors | Measures or bounds magnet, cable and support reaction at B2 for AM receipt |
| Environment | Accelerometer, microphone, pressure/vacuum and vibration channels | Resolve transfer-function band and cryocooler harmonics |
| Timing | Common clock and hardware event markers | Skew/jitter measured; read, write and sensor streams align to event window |
| DAQ | Simultaneous native-sample acquisition | Preserves raw counts/volts, timestamps, sequence and status/overrange bits |
| Compute | Automated blinded scheduler and immutable storage | Commitment-hashed schedule; no raw overwrite; checksums and software environment lock |
| Safety | Interlocks, E-stop, current/temperature/quench protection | Fails safe under control loss; every activation logged |

## Fabrication/acquisition release criteria

Freeze: device family and material; operating-temperature envelope; expected state spacing and barrier; loop and weak-link geometry; write/read mutual inductances; critical current and stored-energy range; shield residual-field requirement; read-noise spectrum; write pulse bandwidth; allowable read energy; required hold time, BER and cycle target; channel count/sample rates; B1/B2 diagrams; and safety review. Catalogue values may size a pilot but cannot replace device-level calibration.
