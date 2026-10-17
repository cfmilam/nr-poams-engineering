#!/usr/bin/env python3
"""Arithmetic/logic checks for a proposed experiment. NO empirical data.

Run: python3 check_design.py
Writes deterministic design-checks.json beside this file. The release manifest is separate.
Python standard library only. No instrument access, network calls or measurements.
"""

from __future__ import annotations

import cmath
import hashlib
import json
import math
from pathlib import Path
from statistics import NormalDist


ROOT = Path(__file__).resolve().parent
TOL = 2e-12


def rotate(a: complex, b: complex, theta: float) -> tuple[complex, complex]:
    c, s = math.cos(theta), math.sin(theta)
    return c * a - 1j * s * b, -1j * s * a + c * b


def energy(a: complex, b: complex) -> float:
    return abs(a) ** 2 + abs(b) ** 2


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def adjoint(a):
    return [[complex(a[j][i]).conjugate() for j in range(len(a))]
            for i in range(len(a[0]))]


def kron(a, b):
    return [[a[i][j] * b[k][l]
             for j in range(len(a[0])) for l in range(len(b[0]))]
            for i in range(len(a)) for k in range(len(b))]


def density(v):
    norm = math.sqrt(sum(abs(x) ** 2 for x in v))
    v = [x / norm for x in v]
    return [[x * complex(y).conjugate() for y in v] for x in v]


def marginal_b(rho):
    return [[sum(rho[2 * a + b][2 * a + bp] for a in range(2))
             for bp in range(2)] for b in range(2)]


def local_channel_a(rho, kraus):
    identity = [[1, 0], [0, 1]]
    result = [[0j for _ in range(4)] for _ in range(4)]
    for k in kraus:
        op = kron(k, identity)
        term = matmul(matmul(op, rho), adjoint(op))
        result = [[result[i][j] + term[i][j] for j in range(4)]
                  for i in range(4)]
    return result


def max_matrix_error(a, b):
    return max(abs(a[i][j] - b[i][j]) for i in range(len(a))
               for j in range(len(a[0])))


def run_readiness(plan):
    missing = [key for key, value in plan["run_specific_required"].items()
               if value is None or value == "" or value == [] or value == {}]
    return {
        "ready": plan["status"] == "FROZEN_READY" and not missing,
        "status": plan["status"],
        "missing_required_fields": missing,
    }


def weak_exchange_bound(delta, kappa, duration):
    if duration <= 0 or delta < 0:
        raise ValueError("Positive duration and nonnegative bound required")
    argument = delta * math.exp(kappa * duration) / 2
    if argument >= 1:
        return None
    return math.asin(argument) / (2 * duration)


def main():
    plan = json.loads((ROOT / "preregistration.json").read_text())
    p = plan["illustrative_parameters_not_hardware_receipts"]
    checks = []

    def check(name, condition, detail):
        checks.append({"name": name, "passed": bool(condition), "detail": detail})
        if not condition:
            raise AssertionError(name)

    # Arbitrary populated inputs, not only the special equal-energy example.
    cases = [(1 + 2j, -0.7 + 0.4j), (1j, 0j), (0.2 - 0.1j, 3j)]
    angles = [0.0, 0.017, 0.25, math.pi / 4, 1.9]
    conserve_err = inverse_err = 0.0
    for a, b in cases:
        for theta in angles:
            out = rotate(a, b, theta)
            back = rotate(*out, -theta)
            conserve_err = max(conserve_err, abs(energy(*out) - energy(a, b)))
            inverse_err = max(inverse_err, abs(back[0] - a), abs(back[1] - b))
    check("finite_joint_map_conserves_equal_frequency_energy_and_is_reversible",
          conserve_err < TOL and inverse_err < TOL,
          {"max_energy_error": conserve_err, "max_inverse_error": inverse_err})

    phase_err = 0.0
    for theta in angles:
        for phi in [0, math.pi / 2, math.pi, 3 * math.pi / 2, 0.31]:
            a, b = rotate(cmath.exp(1j * phi), 1, theta)
            expected = math.sin(2 * theta) * math.sin(phi)
            phase_err = max(phase_err, abs((abs(b) ** 2 - 1) - expected),
                            abs((abs(a) ** 2 - 1) + expected))
    check("seeded_phase_odd_transfer_matches_derived_sign_and_magnitude",
          phase_err < TOL, {"max_error": phase_err})

    seedless_err = global_err = 0.0
    for theta in angles:
        for phi in [0.0, 0.4, math.pi / 2, math.pi]:
            a, b = rotate(cmath.exp(1j * phi), 0j, theta)
            seedless_err = max(seedless_err, abs(abs(b) ** 2 - math.sin(theta) ** 2))
            ref = rotate(1 + 2j, 0.3 - 0.7j, theta)
            alt = rotate((1 + 2j) * cmath.exp(1j * phi),
                         (0.3 - 0.7j) * cmath.exp(1j * phi), theta)
            global_err = max(global_err, abs(abs(ref[0]) ** 2 - abs(alt[0]) ** 2),
                             abs(abs(ref[1]) ** 2 - abs(alt[1]) ** 2))
    check("global_phase_and_seedless_phase_do_not_fake_address_selectivity",
          seedless_err < TOL and global_err < TOL,
          {"seedless_max_error": seedless_err, "global_max_error": global_err})

    theta = 0.13
    phase_average = sum(abs(rotate(cmath.exp(1j * phi), 1, theta)[1]) ** 2 - 1
                        for phi in [0, math.pi / 2, math.pi, 3 * math.pi / 2]) / 4
    unseeded_transfer = abs(rotate(1, 0, theta)[1]) ** 2
    check("dephasing_zeroes_seeded_mean_without_proving_channel_erasure",
          abs(phase_average) < TOL and unseeded_transfer > 0,
          {"phase_averaged_seeded_excess": phase_average,
           "unseeded_transfer_fraction_same_coupling": unseeded_transfer})

    omega = 2 * math.pi * p["frequency_hz"]
    kappa = omega / p["loaded_q"]
    total = p["guard_s"] + p["phase_operation_s"] + p["observation_s"]
    before = energy(1 + 2j, 0.5j)
    rotated = rotate(1 + 2j, 0.5j, 0.2)
    damping = math.exp(-kappa * p["observation_s"] / 2)
    after = energy(*(z * damping for z in rotated))
    loss = before * (1 - math.exp(-kappa * p["observation_s"]))
    check("passive_loss_account_closes_without_equating_amplitude_and_energy_lifetimes",
          abs(after + loss - before) < TOL,
          {"energy_before": before, "energy_after": after, "posted_loss": loss})

    # The no-signaling calculation uses both unitary and nonunitary local CPTP maps.
    gamma = 0.37
    local_u = [[math.cos(0.4), -1j * math.sin(0.4)],
               [-1j * math.sin(0.4), math.cos(0.4)]]
    amplitude_damping = [[[1, 0], [0, math.sqrt(1 - gamma)]],
                         [[0, math.sqrt(gamma)], [0, 0]]]
    ns_error = 0.0
    for rho in [density([1, 0, 0, 1]), density([1, 2j, 0.3, -0.7j])]:
        for kraus in [[local_u], amplitude_damping]:
            ns_error = max(ns_error, max_matrix_error(
                marginal_b(rho), marginal_b(local_channel_a(rho, kraus))))
    check("local_trace_preserving_operations_do_not_signal_to_correlated_receiver",
          ns_error < TOL, {"max_remote_marginal_error": ns_error})

    # Any ordinary coupling with the same angle yields the same phase signature.
    ordinary = rotate(1j, 1, 0.07)
    hypothesized = rotate(1j, 1, 0.07)
    check("endpoint_curve_does_not_identify_an_ordinary_or_new_path",
          ordinary == hypothesized,
          "Identical joint maps are observationally identical; isolation evidence is necessary.")

    bound = weak_exchange_bound(p["illustrative_null_contrast_upper_bound"],
                               kappa, p["observation_s"])
    recovered = 2 * math.exp(-kappa * p["observation_s"]) * math.sin(
        2 * bound * p["observation_s"])
    check("conditional_weak_exchange_null_bound_inverts_only_its_stated_branch",
          abs(recovered - p["illustrative_null_contrast_upper_bound"]) < TOL
          and bound * p["observation_s"] < math.pi / 4
          and weak_exchange_bound(3.0, kappa, p["observation_s"]) is None,
          {"illustrative_bound_rad_per_s": bound,
           "recovered_contrast": recovered,
           "large_bound_gives_no_constraint": True})

    stats = plan["statistical_plan"]
    nd = NormalDist()
    z_alpha = nd.inv_cdf(1 - stats["alpha_two_sided"] / 2)
    z_power = nd.inv_cdf(stats["target_power"])
    d = stats["illustrative_standardized_effect"]
    required = math.ceil(2 * ((z_alpha + z_power) / d) ** 2)
    planned = stats["illustrative_independent_units_per_sign"]
    noncentral = d * math.sqrt(planned / 2)
    power = 1 - nd.cdf(z_alpha - noncentral) + nd.cdf(-z_alpha - noncentral)
    check("planning_sample_size_attains_nominal_power_under_declared_iid_assumption",
          planned >= required and power >= stats["target_power"],
          {"required_per_sign": required, "planned_per_sign": planned,
           "approximate_power": power, "not_validated_for_actual_apparatus": True})

    readiness = run_readiness(plan)
    renamed = json.loads(json.dumps(plan))
    renamed["status"] = "FROZEN_READY"
    check("draft_cannot_be_misclassified_as_run_ready_by_status_label_alone",
          not readiness["ready"] and not run_readiness(renamed)["ready"],
          {"missing_required_fields": len(readiness["missing_required_fields"])})

    report = {
        "schema": "poams.direct-arrival.design-checks.v0.1",
        "evidence_kind": "DESIGN_CHECKS_NOT_EMPIRICAL",
        "physical_verification": False,
        "independent_review": False,
        "checks_passed": sum(c["passed"] for c in checks),
        "checks_total": len(checks),
        "checks": checks,
        "illustrative_budget": {
            "frequency_hz": p["frequency_hz"],
            "loaded_q": p["loaded_q"],
            "energy_decay_rate_per_s": kappa,
            "energy_lifetime_s": 1 / kappa,
            "amplitude_lifetime_s": 2 / kappa,
            "total_retained_interval_s": total,
            "energy_survival": math.exp(-kappa * total),
            "amplitude_survival": math.exp(-kappa * total / 2),
            "phase_step_average_frequency_shift_hz":
                p["phase_step_magnitude_rad"] / (2 * math.pi * p["phase_operation_s"]),
            "constant_relative_frequency_error_limit_hz":
                p["max_phase_uncertainty_rad"] / (2 * math.pi * total),
            "one_mhz_linewidth_energy_lifetime_s": 1 / (2 * math.pi * 1e6),
            "light_travel_s_at_1m_100m_1km": [d / 299792458 for d in [1, 100, 1000]],
            "qualified_circular_mode_only_J_for_illustrative_energy":
                p["illustrative_stored_energy_j"] / omega,
            "one_percent_of_that_angular_impulse":
                0.01 * p["illustrative_stored_energy_j"] / omega,
        },
        "readiness": readiness,
    }
    report_path = ROOT / "design-checks.json"
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"checks_passed": report["checks_passed"],
                      "checks_total": report["checks_total"],
                      "evidence_kind": report["evidence_kind"],
                      "run_ready": readiness["ready"],
                      "missing_required_fields": len(readiness["missing_required_fields"]),
                      "illustrative_budget": report["illustrative_budget"],
                      "nominal_independent_units_per_sign": required,
                      "nominal_power_at_planned_units": power}, indent=2))


if __name__ == "__main__":
    main()
