# Raw-data and custody schema

Use open, self-describing containers (for example HDF5 plus CSV/JSON manifests) with immutable hashes. This is a field contract, not software implementation.

## 1. Run manifest (`run.json`)

Required keys: `protocol_version`, `commitment_hash`, `run_id`, `article_id`, `mount_id`, `operator_ids`, `site`, `start_utc`, `common_clock_id`, `software_revision`, `firmware_revisions`, `b1_diagram_hash`, `b2_diagram_hash`, `calibration_bundle_hash`, `randomization_commitment`, `blind_map_escrow_id`, `registered_axis`, `frame_transform`, `origin`, `smallest_effect`, `equivalence_region`, `alpha_or_interval_rule`, `max_blocks`, `stop_rule`, `exclusion_rule`, `analysis_revision`.

## 2. Channel registry (`channels.csv`)

One row per native channel:

`channel_id, instrument_type, manufacturer_model, serial, native_quantity, native_unit, polarity, axis, location, boundary, range, resolution, sample_rate_hz, analog_filter, digital_filter, adc_conversion, clock_source, sync_tolerance_s, saturation_code, missing_code, calibration_id, reduction_id`.

Force, field, moment, cone angle, power, energy, torque impulse and state coordinates are derived; native volts/counts/IQ/status bits remain primary.

## 3. Trial table (`trials.csv`)

`trial_id, opaque_condition, block_id, scheduled_order, actual_order, command_start_tick, intervention_start_tick, intervention_stop_tick, analysis_window_start_tick, analysis_window_stop_tick, washout_end_tick, article_id, mount_state, orientation_code, safety_stop, abort_reason, operator_intervention, lock_loss, clipping, dropped_samples, inclusion_by_frozen_rule`.

True condition labels remain escrowed until unblinding.

## 4. Event stream (`events.csv`)

`clock_tick, event_code, source_device, command_value, acknowledged_value, status_bits`. Include every bias/RF/heater/servo command, hardware marker, interlock, range switch and manual note.

## 5. Waveforms (`raw.h5`)

For each channel preserve native samples, clock ticks, device sequence numbers and status bits. Do not overwrite or baseline-correct raw arrays. Store calibration observations in a separate immutable group.

## 6. Calibration and boundary ledgers

- `calibrations.csv`: `calibration_id, channel_id, before_after, method, reference_id, coefficients, covariance_ref, valid_range, timestamp, operator, raw_path, raw_hash`.
- `crossings.csv`: `crossing_id, boundary, physical_type, sign_convention, raw_channel_ids, reduction_id, bandwidth, uncertainty, conservative_bound, internal_or_crossing`.
- `components.csv`: `component_id, boundary, state_channels, angular_momentum_reduction, energy_reduction, linear_momentum_reduction`.

An item cannot be counted both as an internal state change and a boundary crossing.

## 7. Derived table (`derived.parquet` or CSV)

Each row retains `trial_id`, reduction code hash, calibration IDs, window, filter, state coordinates, coherent/ring-down measures, retained coordinate, support-wrench components, nuisance covariates, uncertainty components and flags. Derived files are reproducible from raw files without manual edits.

## 8. Release bundle

Include raw data; manifests; calibration data; boundary diagrams; randomization commitment and post-unblind map; source code and environment lock; frozen analysis output; all exclusions and failed runs; SHA-256 inventory; README replay command; and analyst signature. M0 requires this physical custody. M1 may replay it. Neither simulations nor regenerated figures substitute for missing M0 bytes.

## 9. Compensation warning — M-null ≠ J-null (amendment 2026-09-27)

Magnetometry (`M`) and angular-momentum (`J`) entries are distinct typed fields and are never derived from one another. Sublattice or orbital/spin compensation can null the magnetization tariff while a nonzero angular-momentum posting remains — and conversely. Twin nulls, detuned controls, and background subtractions must therefore carry both fields explicitly. Any analysis that infers `J = 0` from `M = 0` (or the reverse) is invalid and must be flagged in `derived` provenance.

