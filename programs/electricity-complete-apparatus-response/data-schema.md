# Raw-data and custody schema

Use open self-describing containers (HDF5/Zarr for waveforms; CSV/JSON/Parquet for manifests and reductions). Native samples, device counters, timestamps, status/range bits and all aborted trials are immutable.

## 1. Campaign manifest (`campaign.json`)

Required keys:

`protocol_version, registration_hash, campaign_id, apparatus_revision, site, operator_ids, analyst_ids, software_revision, firmware_revisions, boundary_B_hash, subboundary_hashes, schematic_hash, grounding_bonding_hash, reference_planes, coordinate_frames, source_id, line_ids, load_ids, switch_matrix_id, support_id, calorimetry_id, common_clock_id, calibration_bundle_hash, randomization_commitment, blind_escrow_id, primary_endpoints, primary_windows, effect_regions, equivalence_regions, model_set, alpha_interval_policy, multiplicity_policy, maximum_blocks, stop_rule, exclusion_rule, safety_review_id`.

## 2. Boundary and component inventory

`components.csv`:

`component_id, type, serial, parent, boundary, subboundary, mass, position_ref, orientation_ref, electrical_ports, mechanical_mounts, thermal_interfaces, internal_energy_types, internal_AM_types, calibration_ids`.

`crossings.csv`:

`crossing_id, boundary, physical_interface, quantity_type, sign_convention, channel_ids, reduction_id, bandwidth, uncertainty_model, conservative_bound, internal_or_crossing`.

Include support contacts, fiber, interlocks, shields, grounds, thermal paths, air/gas paths, enclosure, and any person/tool intervention. No posting may be both internal and a crossing for the same boundary.

## 3. Electrical topology and standards

`topology.json` stores nodes, ports, conductors, shields, bonds, switch states, safety devices, reference planes, line geometry, load connections and schematic checksum.

`standards.csv`:

`standard_id, kind, nominal_value, measured_complex_value_ref, uncertainty_ref, frequency_band, temperature, date, raw_path, raw_hash`.

Keep open, short, matched, detuned and dummy characterization raw records, not only fitted parameters.

## 4. Channel registry (`channels.csv`)

One row per native channel:

`channel_id, instrument_type, manufacturer_model, serial, native_quantity, native_unit, polarity, axis, location, reference_plane, boundary, range, resolution, sample_rate_hz, analog_filter, digital_filter, adc_conversion, clock_source, sync_tolerance_s, latency_s, isolation_type, isolation_capacitance, saturation_code, missing_code, calibration_id, reduction_id`.

Required families: source/load voltage and current; return/shield/chassis/ground current; DC bus and regeneration; switch state; intermediate/coupler diagnostics; force/torque/strain/displacement; accelerometry/tilt/acoustic; temperatures/heat flow; electric/magnetic field diagnostics; line/load state witness; source stock; safety and interlock state.

## 5. Trial table (`trials.csv`)

`trial_id, opaque_condition, block_id, scheduled_order, actual_order, source_program_id, source_channel_code, line_id, line_length_code, load_article_id, load_state_code, detuning_code, polarity_code, waveform_reversal_code, geometry_code, orientation_code, conductor_swap_code, source_load_swap_code, shield_bond_code, mount_cycle, command_tick, source_on_tick, remote_switch_command_tick, remote_switch_sensed_tick, cycle_end_tick, settle_end_tick, analysis_start_tick, analysis_stop_tick, safety_stop, abort_reason, operator_intervention, clipping, dropped_samples, inclusion_by_frozen_rule`.

True labels remain escrowed for confirmatory primary reduction.

## 6. Event and waveform stores

`events.csv`:

`clock_tick, utc_estimate, event_code, source_device, command_value, acknowledged_value, sensed_state, status_bits, operator_note_id`.

`raw-fast.h5`/`raw-fast.zarr` stores native fast samples and device sequence numbers. `raw-slow.*` stores thermal, heat, tilt, environment, source stock and maintenance states. Arrays are never overwritten, resampled, baseline-corrected, de-embedded, or manually repaired.

## 7. Calibration and injection custody

`calibrations.csv`:

`calibration_id, channel_id, before_after, method, reference_id, applied_value, frequency_or_waveform, polarity, coefficients, covariance_ref, valid_range, environment, timestamp, operator, raw_path, raw_hash`.

`injections.csv`:

`injection_id, type, physical_path, actuator_id, amplitude, waveform, frequency_band, common_or_differential, axis, start_tick, stop_tick, endpoint_channels, transfer_model_id, fit_window, holdout_window, acceptance_result, raw_hash`.

Types include differential/common-mode electrical, ground/leakage, electric field, magnetic field/gradient, electrostatic force, heat, force, torque, vibration, acoustic, tilt, cable/feedthrough reaction, switching impulse, clock skew/sample loss and synthetic software replay.

## 8. Line/load characterization

`lines.csv`:

`line_id, conductor_material, geometry_ref, length_m, mass, dc_resistance, complex_multiport_ref, impedance_ref, delay_ref, dispersion_ref, loss_ref, parasitic_ref, common_mode_conversion_ref, thermal_coeff_ref, max_voltage, max_current, max_energy, raw_hashes`.

`loads.csv`:

`load_id, type, material, geometry_ref, complex_impedance_ref, resonance_ref, linewidth_ref, state_witness_channels, force_strain_channels, thermal_channels, storage_model_id, rating_ref, remount_fiducials, raw_hashes`.

## 9. Derived electrical/energy trial table (`derived-electrical.parquet`)

Each row retains:

`trial_id, reduction_code_hash, calibration_ids, reference_plane_reduction, window_ids, V_S_metrics, I_S_metrics, V_L_metrics, I_L_metrics, return_metrics, shield_ground_metrics, Q_source, Q_load, Q_shield, delta_Q_stored, epsilon_Q_by_boundary, W_source_signed, W_source_gross, W_load_signed, W_returned, delta_U_source, delta_U_store, Q_heat, W_mech, E_other, epsilon_E, energy_closure_fraction, recoverable_work_fraction, complex_response_metrics, reflection_diagnostic_metrics, detuning_coordinate, state_match_metrics, uncertainty_components, flags`.

Every transform references source raw channels and code hash. Directional-wave or de-embedded values are operational reductions, never replacements for terminal raw records.

## 10. Derived mechanical/AM table (`derived-mechanical.parquet`)

`trial_id, frame_transform_hash, support_wrench_vector, independent_force, internal_load_force, electrode_strain, displacement, apparatus_motion, impulse_vector, support_work, torque_impulse_vector, measured_delta_p_stocks, measured_delta_J_stocks, imported_EM_comparator_ref, epsilon_p, epsilon_J, vibration_metrics, acoustic_metrics, tilt_metrics, thermal_expansion_metrics, magnetic_metrics, electrostatic_metrics, injection_prediction, heldout_residual, uncertainty_components, flags`.

Imported electromagnetic momentum/AM calculations remain separately labeled and include model/version/parameter provenance.

## 11. Timing and model ledger

`timing.parquet` records hardware-marker arrival, per-channel latency/skew, switch command and sensed state, source/load feature times, uncertainty intervals and valid bandwidth. No sub-resolution order is inferred.

`models.json` records M0–M4 equations/code, fitted parameters and their training blocks, holdout blocks, priors/constraints if any, complexity penalty, frozen basis functions, expected scaling/sign/order, and model checksum. Exploratory revisions receive new IDs and cannot replace the registered model.

## 12. Safety and maintenance

Preserve `safety-events.csv`, interlock tests, stored-energy inventory, discharge verification, inspection photographs, connector/fixture torque, fuse/protection states, battery/service history, component replacements, short-circuit review, trips and emergency interventions. A safety-excluded trial remains in raw custody.

## 13. Release bundle

Include raw fast/slow records; manifests; schematics/topologies; boundary/crossing inventories; line/load standards; all calibrations and injections; randomization commitment and post-unblind map; all trials including failed/aborted runs; registered and exploratory analyses separated; source/environment lock; SHA-256 inventory; replay instructions; operator/analyst signatures; and an explicit missing-data table. M0 means the raw occurrence plus this receipt chain, not a plotted residual alone.
