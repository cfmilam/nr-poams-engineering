# Receiver Stage-0 raw-data schema

## Manifest

`protocol_version, run_id, commitment_hash, source_id, line_id, line_length_m, geometry_id, return_id, termination_matrix_id, source_command_hash, b0_hash, b1_hash, b2_hash, clock_id, trigger_map_hash, calibration_bundle_hash, software_revision, firmware_revisions, randomization_commitment, blind_escrow_id, T_definition, windows, delta_I_A, delta_star, margin, sign_star, kappa_star, equivalence_region, confidence_rule, max_blocks, stopping_rule`.

## Channel registry

`channel_id, endpoint, boundary, instrument_model, serial, native_quantity, native_unit, polarity, reference_plane, range, resolution, sample_rate_hz, analog_filter, digital_filter, adc_scale, clock_source, fixed_delay_s, sync_uncertainty_s, saturation_flag, missing_flag, calibration_id, reduction_id`.

Native values include ADC counts/volts, raw I/Q, switch witness, clock counter, command/status bits and environmental sensor outputs. Current, voltage, power, impedance, energy, residual and latency are derived through sealed reductions.

## Trial table

`trial_id, opaque_condition, block_id, day_stratum, length_code, geometry_code, scheduled_order, actual_order, command_tick, witness_transition_tick, source_window_start_tick, source_window_stop_tick, washout_end_tick, abort_reason, operator_intervention, overload, clipping, lock_loss, dropped_samples, inclusion_by_frozen_rule`.

## Waveforms and events

Preserve every channel’s native samples, hardware ticks, sequence numbers and flags. The event stream records source commands, far commands, physical witness changes, triggers, range switches, interlocks and manual interventions. Never replace hardware event time with receipt time.

## Calibration and crossing ledgers

Each calibration records before/after status, reference, raw path/hash, coefficients, covariance and valid range. Each B0/B1/B2 crossing records physical path, sign, raw channels, transfer-function reduction, bandwidth, uncertainty and conservative bound. Shared grounds, command link and clock distribution are explicit crossings.

## Derived outputs

Per trial: calibrated source/far/return V/I and I/Q; source power/work; state-witness timing; `ΔI_A(t)`; primary `T`; `U_open`; `D_CO`; onset/lag; nuisance projections; energy/storage residual; envelope class; artifact-veto status; uncertainty and flags. Derivations must replay from raw bytes without manual editing.

## Release bundle

Raw waveforms, all failed/aborted runs, manifests, wiring/geometry drawings, calibrations, transfer injections, randomization commitment and unblinded map, code/environment, frozen outputs, SHA-256 inventory and replay instructions. M0 is the physical raw package; code replay is M1 analysis, not another occurrence.
