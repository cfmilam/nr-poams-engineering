# Raw-data and custody schema

Use open, self-describing containers (HDF5/Parquet plus CSV/JSON manifests) and SHA-256 inventories. Raw arrays are append-only.

## 1. Run manifest (`run.json`)

Required keys: `protocol_version`, `commitment_hash`, `run_id`, `device_id`, `device_family`, `fabrication_lot`, `mount_id`, `cryostat_id`, `site`, `operator_ids`, `start_utc`, `software_revision`, `firmware_revisions`, `common_clock_id`, `b1_hash`, `b2_hash`, `calibration_bundle_hash`, `randomization_commitment`, `blind_escrow_id`, `temperature_band`, `field_history_code`, `mission_hold_s`, `state_accuracy_target`, `operation_error_target`, `read_disturbance_target`, `cycle_target`, `max_trials`, `stop_rule`, `exclusion_rule`, `analysis_revision`.

## 2. Channel registry (`channels.csv`)

`channel_id,instrument_type,manufacturer_model,serial,native_quantity,native_unit,polarity,axis,location,boundary,range,resolution,sample_rate_hz,analog_filter,digital_filter,adc_conversion,clock_source,sync_tolerance_s,saturation_code,missing_code,calibration_id,reduction_id`.

Preserve native SQUID output/feedback, write V/I, field-probe voltage, thermometer resistance/voltage, heater V/I, vibration/strain/force outputs and every status bit. Flux, winding number, energy, AM and event class are derived.

## 3. Device registry (`devices.csv`)

`device_id,lot,wafer_or_article,platform,material_stack,geometry_file_hash,loop_area,inductance_method,inductance_value,critical_temperature,critical_current,mutual_write,mutual_read,weak_link_count,pinning_description,mount_id,control_class,characterization_bundle_hash`.

## 4. Trial table (`trials.csv`)

`trial_id,opaque_condition,block_id,scheduled_order,actual_order,start_state_blind,command_start_tick,command_stop_tick,pump_off_tick,settling_pass_tick,hold_end_tick,read_mode,read_count_target,temperature_setpoint,field_condition,device_id,safety_stop,abort_reason,operator_intervention,clipping,dropped_samples,inclusion_by_frozen_rule`.

True command/state labels remain escrowed until the frozen report is generated.

## 5. Event and waveform custody

- `events.csv`: `clock_tick,event_id,event_code,source_device,command_value,acknowledged_value,status_bits,operator_note_id`. Event identifiers are immutable and unique across the run.
- `raw.h5`: native samples, clock ticks, device sequence numbers and status bits per channel; no baseline correction.
- `reads.csv`: `trial_id,read_id,start_tick,stop_tick,read_amplitude,read_energy,raw_feature_refs,classifier_revision,blind_state_call,ambiguity_score,sensor_reset,status_bits`.
- `transitions.csv`: `event_id,trial_id,lower_tick,upper_tick,pre_state_blind,post_state_blind,delta_state_blind,event_probability,event_method,witness_channel_ids,witness_pass,settling_gate_pass,eligibility_pass,signed_topology_change,topology_reduction_id,receipt_consumed,reset_or_inverse_event_id,article_am_value,article_am_unit,article_am_uncertainty,apparatus_am_value,apparatus_am_unit,apparatus_am_uncertainty,closure_residual,residual_bound,concurrent_environment_refs,censoring,event_merge_rule`.

Interval bounds are mandatory when a transition occurs between reads. No-read holds remain right/interval censored rather than assigned an invented event time.
Each event may enter the transaction account once. Reclassification, reread or replay retains the same ID and cannot create another posting. Erase and reversal are new oppositely signed events linked through `reset_or_inverse_event_id`; neither deletes the occurrence history. If topology is not independently established, `signed_topology_change` remains blank rather than inheriting a command label.

## 6. Calibration and boundary ledgers

- `calibrations.csv`: `calibration_id,channel_id,before_after,method,reference_id,coefficients,covariance_ref,valid_range,timestamp,operator,raw_path,raw_hash`.
- `crossings.csv`: `crossing_id,boundary,physical_type,sign_convention,raw_channel_ids,reduction_id,bandwidth,uncertainty,conservative_bound,internal_or_crossing`.
- `state_calibration.csv`: `device_id,calibration_id,injected_flux_or_reference,state_label,raw_centroid,covariance,temperature,field_history,read_mode,validity_interval`.
- `receipt_terms.csv`: `trial_id,term_id,energy_or_am,input_output_internal,raw_refs,reduction_id,value,unit,uncertainty,bound_type,correlation_group`.

A term cannot be both an internal state change and a boundary crossing.

## 7. Derived outputs

`derived_trials.parquet`: operation result, starting/ending state distributions, settle time, hold exposure, read count/energy, transition count/multiplicity, contributing event IDs, receipt-consumption and reset/inverse links, temperature/field/vibration summaries, input/output energy, AM receipt and closure residual.

`endurance.parquet`: cycle index, operation type/sign, error, state separation, write margin/energy, read disturbance, slip-rate estimate, calibration drift, thermal load, cumulative exposure and device-health flags.

Every derived row stores code hash, calibration IDs, filter/window, classifier revision and uncertainty components. Derived artifacts must reproduce without manual edits.

## 8. Release bundle

Include raw and failed runs; device/fabrication geometry; calibration and boundary data; field and temperature histories; preregistration commitment and unblind map; source/reduction code with environment lock; frozen and sensitivity reports; all exclusions/stops; SHA-256 inventory; and replay instructions. A generated trace is not M0 without the physical raw bytes and receipts.
