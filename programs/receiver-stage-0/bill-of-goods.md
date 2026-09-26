# Receiver Stage-0 functional bill of goods

| Group | Item | Functional requirement |
|---|---|---|
| Source | Programmable isolated waveform source | Fixed unkeyed waveform; external reference/trigger; current limit; raw monitor output; amplitude/phase stability measurable |
| Source | Source impedance/current-limit network | Swappable, characterized over band; thermal coefficient measured |
| Link | Two or more shielded line assemblies | Known construction; measured lengths and geometry; accessible shield/return current points; one held-out assembly |
| Far end | Remotely selectable termination matrix | OPEN, matched closed, dummy, detuned and capacitor states; low and measured leakage; break-before-make where required |
| State | Independent contact/impedance witness | Proves physical far state separately from command |
| Storage | Calibrated capacitor/network set | Terminal V/I access; discharge path; dielectric absorption characterized |
| Measurement | Differential voltage probes | Bandwidth/dynamic range exceed operating envelope; calibrated phase and common-mode rejection |
| Measurement | Current sensors/shunts at A, B and return | Bidirectional; phase-calibrated; raw analog output; no saturation in injections |
| RF option | Directional coupler and I/Q receiver/VNA | Complex forward/reflected measurement with common reference |
| Common mode | Shield/ground/common-mode probes | Capture all conductive return paths and command feedthrough |
| Timing | Common frequency/epoch reference + trigger fan-out | Hardware timestamps; measured fixed delay, skew, jitter and health |
| DAQ | Simultaneous digitizer | Shared clock, enough channels/rate/resolution, anti-aliasing, native status/overrange flags |
| Command | Galvanically or optically isolated switch controller | Logged command and acknowledgement; sham command mode; independent timing marker |
| Calibration | Impedance analyzer/VNA/TDR or equivalent | Measures line/termination distributed response and reference planes |
| Injection | Electrical/crosstalk injection source | Calibrated amplitude/phase; multiple injection points; shield rerouting |
| Injection | Heater set | Independent source/cable/switch/termination/sensor thermal injections with metered energy |
| Environment | Temperature, E/B pickup, accelerometer, microphone, humidity sensors | Synchronized native channels covering nuisance bandwidth |
| Mechanics | Cable shaker/displacement fixture | Known cable/mount motion and repeatable geometry |
| Controls | Local switch, matched dummy, sensor blanks | Same command/thermal/electrical burden with declared completion unchanged |
| Safety | Touch-safe enclosures, fuse/current limit, discharge indicator, E-stop | Rated for selected source; safe rewiring and stored-energy discharge |
| Custody | Acquisition controller + immutable storage | Automated blinded schedule, lossless raw data, checksums and version capture |

## Numerical specifications still owed

Operating waveform/band, voltage/current limit, line length/construction, termination range, sensor noise and bandwidth, DAQ rate/resolution, timing tolerance, thermal range, `δI_A`, `Δ*`, equivalence region and trial count must be set from the selected source and a non-physics pilot—not copied from a symbolic exhibit.
