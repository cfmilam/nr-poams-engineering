# Receiver Stage-1 data schema

## Parent binding

Every run manifest binds `stage0_m0_manifest_hash`, `stage0_m1_replay_hash`, `stage0_protocol_hash`, `stage0_transfer_function_hash`, `stage0_calibration_bundle_hash` and `stage0_unresolved_findings`. Missing bindings invalidate entry.

## Run manifest

Add: `stage1_protocol_hash, source_id, intended_sink_id, dummy_id, clone_id, absent_fixture_id, detuning_plan_hash, signature_definition_hash, signature_tolerances, geometry_transform_hashes, b0_hash, b1_hash, b2_hash, common_clock_id, latency_rule, competing_envelope_hash, artifact_bounds_hash, equivalence_regions, maximum_blocks, stop_rule, randomization_commitment, blind_escrow_id`.

## State registry

`state_code, article_id, class_expected_only_after_unblind, frequency, linewidth, impedance_coordinates, phase_coordinates, geometry_coordinates, temperature, dissipation, actuator_burden, witness_channel_ids, equivalence_group, calibration_ids`.

## Trial record

`trial_id, opaque_state, block, day, geometry_stratum, source_precheck, scheduled_order, actual_order, source_command_tick, sink_command_tick, sink_witness_tick, analysis_start_tick, analysis_stop_tick, washout_end_tick, remount_id, abort, intervention, missing, saturation, inclusion_by_frozen_rule`.

## Native channels

Retain hardware ticks and raw samples/status for source V/I/IQ/control, sink V/I/IQ/state witness/actuator, line/return/shield/common mode, storage, thermometry, EM pickup, vibration/acoustic/strain/pressure/humidity, commands, acknowledgements and clock health. Derived quantities never overwrite native bytes.

## Derived outputs

Per trial: calibrated source coordinate and trace; sink signature vector and state qualification; ordinary-load prediction and residual; pairwise contrasts; detuning coordinate; clone/dummy equivalence; absent bound; geometry transform; latency interval; energy/storage/reaction residuals; artifact-veto results; C0/C1/C2/CX classification; uncertainty and exclusion flags.

## Release

Include raw/failed/aborted runs, Stage-0 parent package, calibrations, diagrams, crossing ledger, injection data, blind commitment/map, code/environment, frozen reports, complete hash inventory and replay instructions. No Stage-1 field may contain symbol, decoded bit, bit error rate or capacity output.
