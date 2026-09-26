# Functional bill of goods

No pricing is supplied. Procurement follows achieved noise, field, bandwidth and safety requirements set in the run annex.

| Group | Item | Minimum functional specification / acceptance test |
|---|---|---|
| Articles | YIG specimens, at least 2 | Stable IDs; simple documented geometry; crystallographic orientation available; locally measurable magnetization, resonance and thermal properties; one held out for replication |
| Controls | Matched nonmagnetic dummy | Mass, external geometry, mount interface, thermal capacity/conductivity and microwave loading matched as closely as measured |
| Controls | Nonresonant magnetic control | Comparable static magnetic response but no mode in selected drive band, or registered alternative with measured mismatch |
| Mechanics | Nonmagnetic low-creep mount | Repeatable datum surfaces; negligible unmeasured magnetic material; strain and thermal path instrumentable; containment included |
| Bias | Reversible electromagnet or pole assembly | Both polarities; sufficient field for chosen state range; mapped vector uniformity and gradients; current readback; mechanical reaction monitored |
| Bias | Vector trim coils | Three-axis trim with calibrated current-to-field tensor and polarity verification |
| RF | Tunable resonator/cavity | Covers locally measured FMR branch; measurable field map; coupling adjustable; loaded Q and ring-down directly measurable; accepts dummy and heater |
| RF | Synthesizer/reference | Phase-continuous programmable frequency/amplitude; external common reference; hardware marker output |
| RF | Amplifier, isolator/circulator, loads | Operate without compression in qualified range; forward/reflected power monitored; rated dummy load; arc/overpower protection |
| RF | Directional coupler + I/Q detection/VNA capability | Calibrated complex S-parameter or equivalent phase/amplitude readout; enough bandwidth for pulses and ring-down |
| State | Vector magnetometry or equivalent | Measures three-axis operational state without using support signal; calibration traceable over bias/temperature range |
| State | Mode-amplitude/trajectory readout | Independent cone/trajectory proxy with uncertainty; resolves ring-down and lock loss; raw quadratures retained |
| Support | Primary force transducer | Resolution/noise demonstrated below frozen smallest effect over required load and bandwidth; bidirectional calibration; creep and off-axis sensitivity characterized |
| Support | Independent force/strain channel | Different transduction principle where practical; synchronized raw analog output |
| Reaction | Six-axis force/torque sensor(s) | Measures complete support wrench about registered origin; dynamic range includes actuator reactions and injections |
| Thermal | Article, cavity, mount, cable and electronics thermometry | Calibrated, low self-heating, time response measured; sensors placed to identify gradients |
| Thermal | Calibration heaters | Independent programmable injection at article-equivalent, cavity, cable and support locations; electrical energy metered |
| Environment | Accelerometers, tilt sensor, microphone, pressure, humidity | Bandwidth and resolution cover Gate-0 transfer functions; synchronized native outputs |
| Magnetic | Three-axis field and gradient probes | Calibrated for bias range; fixtures permit maps at article and sensitive support components |
| Electrical | Current shunts, voltage probes, charge/electric-field monitor | Captures coil/RF return currents, grounds and electrostatic state without saturating |
| Cables | Cable-force/fixture-strain sensors | Directly measure feedthrough reaction or bound it by calibrated injections |
| Enclosures | RF + thermal + acoustic enclosure | RF leakage compliant; thermal settling measurable; no hidden load-bearing or airflow path |
| Atmosphere | Pressure/gas-flow control or sealed chamber | Enables convection/buoyancy discrimination; all pressure and flow reactions included in B2 |
| Acquisition | Simultaneous ADC/DAQ | Common hardware clock; sufficient channels, resolution and anti-aliasing; raw status/overrange bits; external event markers |
| Timing | Frequency reference and distribution | Shared reference for RF and DAQ; skew measured with injected marker |
| Compute | Acquisition controller + immutable storage | Automated schedule; condition blinding; lossless native data; checksums; versioned firmware/software |
| Safety | Interlocks, E-stop, guards, leakage meter | RF-open, reflected-power, overtemperature and overcurrent trips; magnet/projectile and article-containment controls |

## Procurement release criteria

Before orders are finalized, the run annex must specify: article size/mass; FMR band; bias range; resonator mode; expected thermal load; support load and bandwidth; smallest effect/equivalence region; required force-noise spectrum; DAQ channel count/rates; magnetic exclusion radius; and atmosphere choice. Nominal legacy values are not purchase requirements.
