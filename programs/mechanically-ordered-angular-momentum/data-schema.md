# Raw-data and custody schema

Use open self-describing containers (HDF5/Zarr plus CSV/JSON/Parquet manifests). Preserve native samples, device counters, timestamps, and status bits. Derived force, angular momentum, energy, topology, and orientation coordinates must be reproducible from raw records.

## 1. Campaign manifest (`campaign.json`)

Required keys:

`protocol_version, registration_hash, campaign_id, apparatus_revision, site, latitude_deg, longitude_deg, altitude_m, boundary_diagram_hash, boundary_inventory_hash, rotor_ids, platform_id, gimbal_id, support_id, containment_review_id, operator_ids, analyst_ids, software_revision, firmware_revisions, common_clock_id, calibration_bundle_hash, randomization_commitment, blind_escrow_id, primary_axis_q, coordinate_frames, origin, effect_region, equivalence_region, alpha_interval_policy, maximum_blocks, stop_rule, exclusion_rule, analysis_revision`.

## 2. Coordinate frames (`frames.json`)

Define transformations and uncertainties among:

- sensor native frames;
- rotor body/axis frame;
- gimbal and platform frames;
- support-transducer frame and frozen torque origin;
- laboratory ENU/NED frame, local vertical, and geographic North;
- Earth rotation axis / inertial or sidereal frame used by the preregistration.

Store calibration observations, not only final matrices. Frame transformations are time-dependent where the apparatus moves.

## 3. Component and boundary inventory (`components.csv`, `crossings.csv`)

`components.csv` fields:

`component_id, serial, boundary, parent, mass_kg, inertia_tensor_ref, com_ref, attitude_channels, rate_channels, internal_stock_types, energy_reduction_id, angular_momentum_reduction_id, calibration_ids`.

`crossings.csv` fields:

`crossing_id, boundary, physical_interface, quantity_type, positive_direction, native_channel_ids, reduction_id, bandwidth, uncertainty_model, conservative_bound, internal_or_crossing`.

No component/packet may be posted both as an internal stock and a boundary crossing.

## 4. Channel registry (`channels.csv`)

One row per native channel:

`channel_id, instrument_type, manufacturer_model, serial, native_quantity, native_unit, polarity, axis, location, frame_id, boundary, range, resolution, sample_rate_hz, analog_filter, digital_filter, adc_conversion, clock_source, sync_tolerance_s, latency_s, saturation_code, missing_code, calibration_id, reduction_id`.

Required families include support wrench, independent force/strain, tachometers, attitude/optical tracking, platform kinematics, gimbal state, motor/brake torque, voltage/current/returned energy, bearing strain/temperature, accelerometry, tilt, acoustics, pressure/flow, thermal/heat flow, magnetic field/gradient, ground/leakage current, cable/feedthrough reaction, and safety status.

## 5. Trial table (`trials.csv`)

`trial_id, opaque_condition, block_id, scheduled_order, actual_order, rotor_id, dummy_id, spin_level_code, rotor_sense_measured, containing_motion_code, containing_sense_measured, constraint_code, axis_orientation_code, apparatus_azimuth_code, support_geometry_code, atmosphere_code, drive_channel_code, mount_cycle, command_start_tick, state_qualified_tick, intervention_start_tick, intervention_stop_tick, settle_start_tick, analysis_start_tick, analysis_stop_tick, washout_end_tick, safety_stop, abort_reason, operator_intervention, overspeed, clipping, dropped_samples, inclusion_by_frozen_rule`.

True labels remain escrowed through primary reduction.

## 6. Event stream and waveforms

`events.csv`:

`clock_tick, utc_estimate, event_code, source_device, command_value, acknowledged_value, status_bits, operator_note_id`.

`raw.h5`/`raw.zarr` stores for each channel: native samples, clock ticks, device sequence number, status bits, range, and loss/overload markers. Raw arrays are never overwritten, filtered, baseline-corrected, resampled, or manually patched.

## 7. Calibrations and injections

`calibrations.csv`:

`calibration_id, channel_id, before_after, method, reference_id, applied_value, axis, coefficients, covariance_ref, valid_range, environment, timestamp, operator, raw_path, raw_hash`.

`injections.csv`:

`injection_id, type, physical_path, actuator_id, amplitude, waveform, frequency_band, axis, start_tick, stop_tick, endpoint_channels, transfer_model_id, fit_window, holdout_window, acceptance_result, raw_hash`.

Direct injection models are fitted without physics condition labels and version-locked before unblinding.

## 8. Rotor/platform characterization

`rotors.csv`:

`rotor_id, material, mass_kg, geometry_ref, com_ref, inertia_tensor, inertia_covariance_ref, balance_grade_or_result, runout_ref, inspection_ref, proof_test_ref, max_allowed_rate, service_cycles, mount_interface, remount_fiducials`.

`platform.csv` records mass/inertia tensors, centres, trajectory calibration, gimbal friction/backlash/lock force, bearing/preload maps, structural modes, safe motion limits, and coordinate-frame IDs.

## 9. Derived trial table (`derived.parquet`)

Each row retains:

`trial_id, reduction_code_hash, calibration_ids, window_ids, frame_transform_hash, measured_S_vector, measured_L_containing_vector, sigma, state_match_metrics, support_wrench_vector, independent_force, N_odd_components, P_odd, odd_impulse, odd_work, delta_S, delta_L_platform, boundary_torque_integral, epsilon_J, energy_fluxes, stored_energy_changes, epsilon_E, attitude_metrics, latency_interval, thermal_metrics, vibration_metrics, bearing_metrics, pressure_metrics, magnetic_metrics, electrical_metrics, cable_reaction_metrics, injection_prediction, residual, uncertainty_components, flags`.

Topology fields (`centreline_ref, framing_ref, Lk, Tw, Wr`) remain null unless Gate H-W is physically instantiated. Retention fields remain null unless an independent coordinate exists.

## 10. Earth-orientation table (`orientation.parquet`)

At sufficient cadence record:

`clock_tick, latitude, longitude, local_sidereal_time, earth_axis_in_lab, local_vertical_in_lab, geographic_north_in_lab, rotor_axis_in_lab, platform_orbit_normal_in_lab, apparatus_bench_axes, ambient_B_vector, sun_or_solar_time_optional`.

Orientation hypotheses and harmonics are frozen before unblinding; this table is not permission for post-hoc period mining.

## 11. Safety and maintenance custody

Preserve `safety-events.csv`, inspection photographs, balancing certificates, containment analysis, service hours/cycles, component replacements, torque settings, enclosure/interlock tests, and every trip. A safety-excluded trial remains in raw custody.

## 12. Release bundle

Include raw data; campaign/run manifests; boundary diagrams/inventories; frames; all calibration/injection observations; randomization commitment and post-unblind map; all trials including failed/aborted runs; analysis source and environment lock; frozen and exploratory outputs clearly separated; SHA-256 inventory; replay instructions; and operator/analyst signatures. M0 is the raw physical occurrence plus this custody chain. A code replay without the M0 bytes is not replication.
