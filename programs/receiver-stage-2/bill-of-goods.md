# Receiver Stage-2 functional bill of goods

No item is procured under this package. Stage-0/1 qualified hardware is inherited; changes trigger requalification.

| Group | Item | Functional requirement | Planning band (USD) |
|---|---|---|---:|
| Entry custody | Immutable parent-stage archive/replay workstation | Verify M0/M1 hashes, manifests, code and unresolved findings offline | 1k–5k |
| Alphabet | Qualified sink-state controller and independent witness | Offline committed schedule; physical state readout; sham and replay modes | 2k–15k |
| Source | Frozen Stage-0/1 article and DAQ | Fixed unkeyed command; unchanged native primary record | inherited |
| Local enclosure | Two shielded/isolated enclosures with characterized penetrations | Measure conducted, RF, optical, acoustic and thermal attenuation | 5k–40k |
| Power | Independent battery/isolated supplies and monitors | Raw V/I; no shared hidden control path; safe capacity | 2k–15k |
| Conducted-path monitor | Current probes, LISN/isolation fixtures, ground/shield sensors | Mains/earth/shield/plumbing/cable transfer and injection | 5k–30k |
| RF monitoring | Spectrum receiver/analyzer, calibrated antennas/probes and injection source | Continuous justified-band custody; harmonics/intermodulation/near-field tests | 15k–100k |
| Optical | Photodiodes/cameras, opaque feedthroughs, calibrated source | Visible/IR path qualification and injection | 1k–10k |
| Acoustic/mechanical | Microphones, accelerometers/seismometers, shaker/actuator | Airborne/structural transfer and injection | 3k–30k |
| Thermal | Distributed thermometry, heat-flux/air-path sensors and metered heaters | Sink/source/enclosure thermal transfer | 2k–20k |
| Timing | Hardware counters, stable independent clocks, time-interval comparator | Raw ticks; offset/drift/jitter; before/after common-event calibration | 10k–80k |
| Energy/AM | Source/sink V/I/IQ, torque/force/strain and support sensors | Whole B2 energy, linear-AM and angular-AM receipts | 10k–100k |
| DAQ | Simultaneous isolated digitizers and event logger | No ambiguous multiplexing; native status/overrange/sequence flags | 10k–80k |
| Software custody | Offline scheduler, blinded analysis machine, write-once/archive storage | No label path; reproducible container; hash inventory | 3k–20k |
| Separated site | Second room/site, duplicate monitors/enclosures and access logging | Independent power/clock; no live cross-site path | 25k–250k+ |
| Safety | Interlocks, RF/laser survey, fusing, discharge, fire and E-stop equipment | Independent review against selected apparatus | 5k–40k |

## Cost reality

- Local pilot using inherited instruments: roughly **USD 20k–75k incremental**.
- Fully monitored local confirmatory apparatus: **USD 75k–300k**.
- Separated two-site replication: **USD 150k–750k+**, strongly dependent on timing, RF coverage, duplicated DAQ and facility isolation.
- Independent replication is additional.

These are order-of-magnitude planning bands, not quotes or procurement authority. A real BOM requires exact parent-stage articles, operating band, symbol duration, separation, monitor coverage, clock uncertainty and safety review.

## Down-select sequence

1. Verify immutable Stage-0/1 entry packet—otherwise stop.
2. Select the smallest qualified binary alphabet.
3. Build only the local leakage/injection metrology shell.
4. Run the unblinded non-claim pilot and freeze numerical specifications.
5. Authorize local confirmatory acquisition only after monitor coverage and receipts pass.
6. Design separated replication only after a frozen local T2 candidate.

