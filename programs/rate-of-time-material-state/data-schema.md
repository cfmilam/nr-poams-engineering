# Rate-of-Time data and custody schema

## 1. Custody principles

Raw means the earliest obtainable instrument record: phase samples, counter gates, servo error, ADC counts/voltages, sensor frames, command acknowledgements, and hardware event markers. Derived frequency, corrected ratios, state coordinates, averages, exclusions, and model residuals are separate layers. Raw objects are immutable and content-hashed.

All timestamps carry clock domain, epoch convention, nominal resolution, measured latency/skew, synchronization health, and conversion history. UTC labels alone do not prove simultaneity.

## 2. Run manifest (`run_manifest.json`)

Required fields:

`program_id`, `run_id`, `site_id`, `protocol_version`, `preregistration_hash`, `analysis_commit`, `randomization_commit`, `operator_ids`, `analyst_blind_id`, `start_utc`, `end_utc`, `clock_A_id`, `clock_B_id`, `reference_R_id`, `comb_transfer_id`, `article_id`, `dummy_id`, `mount_id`, `geometry_id`, `firmware_map`, `calibration_bundle_hash`, `raw_object_manifest_hash`, `safety_permit_ids`, `deviations`, `unblind_time`, `signatures`.

## 3. Common sample envelope

Every stream row/object includes:

`run_id`, `stream_id`, `sequence_no`, `timestamp_native`, `clock_domain`, `timestamp_utc_estimate`, `timestamp_uncertainty_s`, `event_marker_no`, `quality_bits`, `range_code`, `saturation_flag`, `raw_value`, `raw_unit_or_adc_code`, `instrument_id`, `channel_id`, `calibration_id`, `object_hash`.

Native binary files remain authoritative; tabular exports point back to byte offsets or frame identifiers.

## 4. Raw stream groups

### `clock_phase_raw`

For A, B and R: local-oscillator phase/time error, interrogation cycle, atom/ion number where relevant, transition/state selector, servo error, correction command, lock flag, dead time, cycle-slip flag, probe/lattice/microwave power monitors, magnetic-field proxy, chamber temperature and instrument-native diagnostics. Preserve clock corrections as separate commanded streams; do not overwrite raw phase.

### `ratio_transfer_raw`

Beat-note I/Q or phase/frequency, comb repetition and carrier-envelope signals, transfer-oscillator channels, counter gate definitions, fibre/link round-trip phase, link servo error, branch power, packet/frame loss, reference phase/frequency steps, redundant-counter outputs.

### `material_state_raw`

Drive command and acknowledgement; source voltage/current/power/phase/return; vector magnetometry or flux; polarization charge/current; strain tensor; diffraction/image frame references; trapped flux/current; state-witness calibration; article temperatures; spatial-position encoder; write/erase/reverse markers; drive-off intervals.

### `environment_raw`

Temperature array; heat-flow proxies; magnetic/electric fields and gradients; accelerometer/seismometer; tilt; acoustic pressure; displacement/height; strain/load; pressure/humidity/flow; RF spectrum/power; optical leakage; ground current and mains quality; vacuum/cooling/cryogen status.

### `command_event_log`

`event_id`, opaque `condition_code`, requested action, controller, request/acknowledge/physical-marker times, interlock state, success/failure, operator intervention, safety stop, free-text note hash. Operators must not edit prior records.

### `calibration_events`

Instrument/channel; standard/artefact ID; before/after/in-run status; injected waveform/amplitude; raw response; model/version; coefficients and covariance; validity interval; operator; certificate/object hashes; pass/fail; deviation.

### `geometry_and_configuration`

Survey points and covariance; effective clock reference points; article pose; distances; mount torque/order; cable/fibre topology; photographs/3-D scans; shielding state; wiring netlist; power-source mapping; support and boundary drawings.

## 5. Trial/block table (`trial_index.parquet`)

Fields:

`trial_id`, `block_id`, `blind_condition_code`, `article_code`, `state_level_code`, `physical_reversal_code`, `geometry_code`, `reference_path_code`, `control_family`, `scheduled_start`, `actual_start`, `analysis_window_start`, `analysis_window_end`, `washout_start_end`, `state_witness_pass`, `clock_A_lock_fraction`, `clock_B_lock_fraction`, `reference_lock_fraction`, `injection_coverage_pass`, `predeclared_exclusion_code`, `safety_event_id`, `included_primary`, `notes_hash`.

Condition meanings remain in escrow until the frozen blind report is signed.

## 6. Derived tables

Derived outputs live under a new immutable analysis receipt and never replace raw data.

- `state_coordinate`: registered `u(t)`, method/version, calibration propagation, hysteresis branch, uncertainty.
- `ratio_series`: A/R, B/R, A/B phase and fractional frequency; gate/window; cycle-slip treatment; no physics label.
- `nuisance_transfer`: injection ID, input/output transfer function, bandwidth, uncertainty, training/validation status.
- `design_rank`: singular values, condition number, common-vector projection, target bandwidth, pass/fail.
- `block_estimands`: blind condition, local/common estimates, covariance, residual diagnostics.
- `model_scores`: N/L/R/C1/C2/CD/CH held-out predictive metric, preregistered penalties and multiplicity adjustment.
- `finite_bounds`: coefficient/kernel norm, confidence construction, material/state interval, geometry, bandwidth, averaging time.
- `classification`: controlled vocabulary plus exact gate evidence and reviewer signatures.

## 7. Quality bits

At minimum: `CLOCK_UNLOCK`, `CYCLE_SLIP`, `COUNTER_OVERFLOW`, `ADC_CLIP`, `SENSOR_SATURATION`, `CAL_EXPIRED`, `TIMING_UNLOCK`, `MISSING_FRAME`, `INTERLOCK`, `MANUAL_INTERVENTION`, `OUTSIDE_APPROVED_RANGE`, `STATE_WITNESS_FAIL`, `REFERENCE_FAIL`, `LINK_FAIL`, `THERMAL_UNSETTLED`, `VIBRATION_EXCURSION`, `GEOMETRY_UNKNOWN`.

Flags do not silently delete samples. Frozen exclusion logic converts flags into analysis inclusion; all records remain.

## 8. Directory contract

```text
run_id/
  manifest/run_manifest.json
  preregistration/
  raw/clock_A/ clock_B/ reference_R/ transfer/ state/ environment/ commands/
  calibration/before/ in_run/ after/
  geometry/
  blind/trial_index.parquet randomization_commit.txt
  derived/<analysis_commit>/
  reports/blind/ unblinded/ deviations/
  custody/hashes.sha256 signatures/
```

## 9. Minimum receipt for any reported point

A reported ratio, coefficient or bound must resolve to: raw object hashes; clock/reference configuration; exact time window; state-witness record; all relevant nuisance records; calibration versions; geometry; command history; exclusion decision; code commit/container; uncertainty propagation; and analyst/reviewer signature. Missing linkage demotes the result to apparatus-inconclusive.
