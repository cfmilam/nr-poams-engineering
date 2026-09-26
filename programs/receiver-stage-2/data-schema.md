# Receiver Stage-2 raw-data and custody schema

## Parent entry manifest

`stage0_m0_hash, stage0_m1_hash, stage0_protocol_hash, stage0_pass_report_hash, stage1_m0_hash, stage1_m1_hash, stage1_protocol_hash, stage1_c2_report_hash, parent_hardware_manifest_hash, parent_calibration_hash, parent_transfer_hash, parent_artifact_bounds_hash, parent_confusion_matrix_hash, parent_repeat_hash, parent_heldout_hash, parent_unresolved_findings`.

Any missing or mismatched field sets `entry_valid=false` and blocks physics acquisition.

## Stage-2 manifest

`protocol_hash, architecture_code, site_ids, source_id, sink_id, second_article_id, alphabet_hash, symbol_schedule_commitment, escrow_id, symbol_duration_ticks, guard_ticks, transition_constraints, decoder_container_hash, feature_map_hash, training_partition_hash, heldout_partition_hash, null_model_hash, z_monitor_registry_hash, b0_hash, b1_hash, b2_hash, b3_hash, timing_model_hash, ordinary_envelope_hash, veto_threshold_hash, equivalence_regions, maximum_blocks, stop_rule, randomization_commitment, software_firmware_hashes`.

## Channel registry

`channel_id, site, boundary, crossing_class, instrument_model, serial, native_quantity, native_unit, polarity, reference_plane, range, resolution, sample_rate, analog_filter, clock_id, fixed_delay, delay_uncertainty, calibration_id, coverage_band, detection_limit, saturation_flag, missing_flag`.

Crossing classes: source, intended link, conducted/mains/earth/shield/plumbing, RF-electric, RF-magnetic, optical, acoustic, vibration/seismic, thermal/air, force/torque/strain, clock, software/network, access/human and environment.

## Trial/block table

`trial_id, opaque_symbol, block_id, architecture, site_pair, scheduled_index, scheduled_tick, sink_command_tick, sink_witness_tick, source_onset_tick, actual_state_code, state_qualified, condition_code, geometry_code, direction_code, remount_id, article_id, training_or_heldout_opaque, clock_health, enclosure_health, network_scan_status, access_event, abort_reason, operator_intervention, clipping, dropped_samples, inclusion_by_frozen_rule`.

The unblinded symbol and partition maps remain escrowed until frozen outputs and raw hashes are sealed.

## Native data

Preserve continuous native samples, ticks, sequence numbers and status for:

- frozen source V/I/IQ/control and primary Stage-0 channel;
- sink V/I/IQ, actuator, state witness and local signature coordinates;
- return/shield/common-mode and all conducted crossings;
- RF spectrum/probes, optical detectors, microphones and accelerometers;
- temperatures, heat, pressure/airflow and humidity;
- force, torque, strain and support reaction;
- independent clocks, calibration pulses, trigger health and oscillator telemetry;
- software process/network/access logs and enclosure/interlock events.

Never overwrite native bytes with calibrated or filtered values. Hardware event time is distinct from software receipt time.

## Injection ledger

`injection_id, path_class, location, waveform_or_symbol_hash, amplitude, band, reference_plane, raw_monitor_ids, transfer_model_hash, linear_range, candidate_similarity_metric, prediction_interval, veto_bound, before_after_calibration_ids`.

## Derived table

Per trial/block: qualified symbol state; frozen feature vector; decoder output; prediction/error; full monitor vector `Z`; ordinary-path predicted score; residual score; confusion-matrix cell; latency interval; energy/storage/dissipation residual; linear/angular momentum residual; injection-veto results; T0/T1/T2/TX classification; uncertainty; exclusions and reasons.

Conditional mutual information or achievable-rate fields are absent from the primary schema. They may be added only in a versioned post-candidate information-analysis package after all promotion gates pass.

## Release bundle

Release all raw, aborted and failed runs; parent packages; schedule commitment and unblind map; channel/crossing registries; facility and grounding diagrams; RF/optical/acoustic/conducted surveys; calibrations and injections; code/container; frozen training and held-out outputs; safety/interlock log; SHA-256 inventory and replay instructions. M0 is the physical occurrence; M1 is the replay, not a second occurrence.

