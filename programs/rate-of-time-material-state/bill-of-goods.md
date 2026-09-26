# Rate-of-Time bill of goods

This is a functional procurement specification, not authorization to buy. Final part numbers, quantities, prices, compatibility, facility work, and lead times require the selected host and clock platforms.

## Budget classes

| Class | Scope | Order-of-magnitude planning band | What it can establish |
|---|---|---:|---|
| P0 — paper/pilot bench | state article, witness, environmental sensors, inert oscillator emulators | USD 25k–150k incremental | intervention repeatability and nuisance maps; **not** a proper-rate test |
| P1 — metrology partnership | use existing two-clock laboratory and independent reference; add intervention, shielding, sensors, transfer branches | USD 250k–2M incremental | credible two-clock system-identification run if host capability passes |
| P2 — dedicated precision build | new dissimilar clocks, comb, reference, enclosures and facility work | USD 3M–15M+ | independent full architecture; schedule likely multi-year |
| P3 — replicated/cross-process program | second laboratory/apparatus and qualified process C | USD 10M–40M+ programmatic | independent confirmation and cross-process test |

Bands are rough 2026 planning classes, not vendor quotes. Personnel, building services, maintenance, clock development risk, and institutional overhead can dominate.

## A. Clock ensemble

1. **Clock A — optical class**
   - trapped-ion or optical-lattice system with raw servo/error signals, interrogation logs, environmental telemetry, evaluated systematic budget, and external comb access;
   - host-demonstrated stability and uptime over the registered block duration;
   - magnetic, electric, blackbody, density/collision, probe, lattice/quadrupole, Doppler/motion, gravitational-height, and servo responses available for direct injection.

2. **Clock B — microwave class**
   - caesium fountain, hydrogen maser, cold-atom microwave clock, or equivalent research instrument;
   - transition and apparatus physically dissimilar from A;
   - raw phase/frequency and control-loop records, not display-only frequency output.

3. **Clock R — independent reference**
   - remote optical/primary-standard comparison over calibrated fibre is preferred;
   - alternatively an independent local species with separate enclosure, power, environmental loop and transfer branch;
   - GNSS/TWSTFT receiver may add long-term traceability and gross-fault detection but is not adequate alone for the primary short-term comparison.

4. **Comparison system**
   - self-referenced optical frequency comb where optical/microwave transfer requires it;
   - transfer oscillator/multiple independent beat branches;
   - low-noise distribution amplifiers, fibre-noise cancellation, phase-stable cabling;
   - cycle-slip detection and redundant counters sharing a verified timebase.

## B. Intervention module

Procure only after down-select.

- active article and at least two matched blanks/dummies;
- reversible drive with logged source and return channels;
- state witness independent of clock output (vector magnetometry/flux, polarization charge and strain, trapped flux/current, diffraction/domain imaging, or registered equivalent);
- translation/rotation fixture for frozen geometry levels with surveyed fiducials;
- symmetric low-creep mount and matched thermal mass;
- source work/energy measurement and drive-off isolation;
- shielding appropriate to the candidate without hiding the witness channel;
- replaceable feedthrough panel defining the intervention boundary.

## C. Direct nuisance injection hardware

- multi-zone resistive heaters and calibrated heat-flow/temperature-gradient actuation;
- three-axis field and gradient coils plus calibrated current/voltage monitoring;
- guarded electrodes/high-voltage source where approved, leakage-current monitor and field probe;
- piezo/shaker or inertial actuator for vibration; precision tilt and vertical translation stages;
- strain/load actuators and displacement metrology;
- RF/optical leakage injection ports, attenuators, dummy loads and power detectors;
- programmable reference phase/frequency step and link-delay emulator;
- humidity/pressure/gas-flow actuation only where compatible with clock enclosures.

Every injector must cover the observed intervention exposure with margin while remaining inside clock and safety linearity limits.

## D. Sensors and environment

- traceable multi-point thermometry at article, clocks, comb, electronics, enclosure and cable/feedthrough planes;
- vector magnetic-field sensors and mapped gradient probes at both clock effective locations;
- electric-field/leakage monitors where technically feasible;
- triaxial accelerometers, seismometer, tiltmeters, acoustic pressure sensors;
- interferometric or equivalent displacement/height monitoring of clock reference points and article;
- strain gauges/fibre Bragg sensors and support load cells as candidate requires;
- pressure, humidity, gas-flow and vacuum telemetry;
- RF spectrum/power monitoring and optical scatter/leakage photodiodes;
- power-line, ground-current and source-return monitoring.

## E. Data, timing, and custody

- hardware timestamp/event-marker fanout with measured latency and skew;
- synchronous digitizers sized for all channels plus anti-alias filtering;
- independent frequency counters and phase recorders;
- append-only acquisition server, local redundant storage, checksum service, offsite immutable copy;
- machine-readable configuration/version capture and uninterruptible power for orderly shutdown;
- calibration artefacts for temperature, force/strain, field, voltage/current, displacement and timing.

## F. Mechanical and facility

- thermally controlled enclosure with measured gradients;
- magnetic/RF shielding and characterized penetrations;
- vibration-isolated optical/clock supports while retaining independently monitored mechanical paths;
- cable trays and strain relief designed for repeatable topology;
- surveyed fixed reference monuments;
- vacuum, cooling water, cryogen, exhaust and clean electrical services as selected clocks require;
- access controls and safety interlocks.

## G. Personnel/functions

- optical-clock lead; microwave-clock lead; frequency-comb/time-transfer specialist;
- intervention/materials specialist; metrologist/calibration lead;
- RF/magnetic/thermal/mechanical engineers;
- independent statistician and blinded-data custodian;
- laser, electrical, magnet/cryogen, vacuum and radiation safety officers as applicable;
- independent replication partner.

## H. Procurement acceptance tests

No component enters confirmatory service until its serial/firmware identity, calibration, noise, drift, saturation, latency, cross-sensitivity, environmental envelope, failure behavior, and raw-data interface are recorded. Vendor accuracy statements size selection only; local calibrations drive the error budget.
