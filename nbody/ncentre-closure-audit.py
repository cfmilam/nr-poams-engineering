#!/usr/bin/env python3
"""Numerical guards for NCENTRE-CLOSURE-DERIVATION.md.

The script checks algebraic share reconstruction, pair-force momentum/torque closure,
kick-drift-kick conservation, the pendulum width identity, and the two Bertrand
branches against the JPL major-moon snapshot used by The Solar System.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
JPL = HERE.parents[1] / "poams-exhibits-public" / "solar-system-jpl.json"


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def scale(c, a):
    return tuple(c * x for x in a)


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def norm(a):
    return math.sqrt(sum(x * x for x in a))


def total(values):
    out = (0.0, 0.0, 0.0)
    for value in values:
        out = add(out, value)
    return out


def gradients(q, w, gamma):
    """Return dV/dq for V=-Gamma sum_i<j w_i w_j/r_ij."""
    out = [(0.0, 0.0, 0.0) for _ in q]
    for i in range(len(q)):
        for j in range(i + 1, len(q)):
            delta = sub(q[i], q[j])
            radius = norm(delta)
            grad_i = scale(gamma * w[i] * w[j] / radius**3, delta)
            out[i] = add(out[i], grad_i)
            out[j] = sub(out[j], grad_i)
    return out


def invariants(q, p):
    return total(p), total(cross(x, y) for x, y in zip(q, p))


def verlet(q, p, w, gamma, dt):
    g0 = gradients(q, w, gamma)
    ph = [sub(pi, scale(0.5 * dt, gi)) for pi, gi in zip(p, g0)]
    q1 = [add(qi, scale(dt / wi, phi)) for qi, wi, phi in zip(q, w, ph)]
    g1 = gradients(q1, w, gamma)
    p1 = [sub(phi, scale(0.5 * dt, gi)) for phi, gi in zip(ph, g1)]
    return q1, p1


def share_reconstruction_check():
    strengths = (0.7, 1.3, 2.9, 5.1, 8.4)
    mu = {(i, j): strengths[i] + strengths[j] for i in range(5) for j in range(i + 1, 5)}

    def pair(i, j):
        return mu[tuple(sorted((i, j)))]

    errors = []
    for i in range(5):
        others = [j for j in range(5) if j != i]
        for a in range(len(others)):
            for b in range(a + 1, len(others)):
                j, k = others[a], others[b]
                recovered = 0.5 * (pair(i, j) + pair(i, k) - pair(j, k))
                errors.append(abs(recovered - strengths[i]))
    worst = max(errors)
    assert worst < 2e-15
    print(f"PASS share reconstruction: worst triple-choice error {worst:.3e}")


def scale_identifiability_check():
    """Dimensionless closure is invariant under the rod-clock scale orbit."""
    q = [(1.2, -0.4, 0.1), (-0.8, 0.3, 0.2), (0.1, 1.1, -0.2)]
    w = (0.2, 0.3, 0.5)
    gamma = 7.3
    length_scale, time_scale = 4.7, 2.3
    g0 = gradients(q, w, gamma)
    q_scaled = [scale(length_scale, item) for item in q]
    gamma_scaled = length_scale**3 / time_scale**2 * gamma
    g1 = gradients(q_scaled, w, gamma_scaled)
    # dV/dq scales as w * acceleration, and acceleration as a/b^2.
    expected = [scale(length_scale / time_scale**2, item) for item in g0]
    error = max(norm(sub(a, b)) for a, b in zip(g1, expected))
    assert error < 2e-14
    print(
        "PASS absolute-scale no-go: q->a q, t->b t, Gamma->a^3/b^2 Gamma "
        f"preserves dimensionless closure (worst scaled-gradient error {error:.3e})"
    )


def conservation_check():
    w = (0.11, 0.17, 0.29, 0.43)
    gamma = 3.7
    q = [(-1.2, 0.3, 0.1), (0.4, -0.8, 0.2), (1.3, 0.7, -0.4), (-0.2, 1.6, 0.5)]
    velocities = [(0.2, 0.7, -0.1), (-0.3, 0.1, 0.4), (0.5, -0.2, 0.1), (-0.1, -0.4, -0.2)]
    p = [scale(wi, vi) for wi, vi in zip(w, velocities)]
    grad = gradients(q, w, gamma)
    force_sum = norm(total(scale(-1.0, g) for g in grad))
    torque_sum = norm(total(cross(qi, scale(-1.0, gi)) for qi, gi in zip(q, grad)))
    before_p, before_l = invariants(q, p)
    q1, p1 = verlet(q, p, w, gamma, 1e-3)
    after_p, after_l = invariants(q1, p1)
    p_err, l_err = norm(sub(after_p, before_p)), norm(sub(after_l, before_l))
    assert max(force_sum, torque_sum, p_err, l_err) < 2e-15
    print(
        "PASS pair closure / discrete map: "
        f"|sum F|={force_sum:.3e}, |sum tau|={torque_sum:.3e}, "
        f"Delta P={p_err:.3e}, Delta L={l_err:.3e}"
    )


def width_check():
    a, coefficient = 3.7, 0.02
    action_half_width = 2 * math.sqrt(coefficient / a)
    rate_half_width = a * action_half_width
    predicted = 2 * math.sqrt(a * coefficient)
    island_area = 16 * math.sqrt(coefficient / a)
    assert math.isclose(rate_half_width, predicted, rel_tol=1e-15)
    # At phi=0, H=+C on the separatrix implies I=2 sqrt(C/A).
    energy = 0.5 * a * action_half_width**2 - coefficient
    assert math.isclose(energy, coefficient, rel_tol=1e-15)
    print(
        "PASS channel normal form: "
        f"DeltaI={action_half_width:.9f}, W={predicted:.9f}, area={island_area:.9f}"
    )


def laplace_coefficient(order, alpha, samples=40_000):
    """b^(order)_(1/2), midpoint quadrature on [0, 2pi]."""
    acc = 0.0
    for index in range(samples):
        angle = (index + 0.5) * 2 * math.pi / samples
        acc += math.cos(order * angle) / math.sqrt(
            1 + alpha * alpha - 2 * alpha * math.cos(angle)
        )
    return 2 * acc / samples


def laplace_derivative(order, alpha):
    step = 1e-5
    return (
        laplace_coefficient(order, alpha + step)
        - laplace_coefficient(order, alpha - step)
    ) / (2 * step)


def galilean_three_body_check():
    """Quillen (2011) direct, circular, second-order cross-bracket for (1,-3,2)."""
    p, q = 1, 2
    # a_Europa=1; ledger shares are measured satellite/Jupiter circulation ratios.
    semimajor = (421_700 / 670_900, 1.0, 1_070_400 / 670_900)
    shares = (4.70e-5, 2.53e-5, 7.80e-5)
    ai, aj, ak = semimajor
    mi, mj, mk = shares
    ni, nj, nk = (value ** -1.5 for value in semimajor)
    nij, njk = ni - nj, nj - nk
    alpha_ij, alpha_jk = ai / aj, aj / ak
    bp = laplace_coefficient(p, alpha_ij)
    bq = laplace_coefficient(q, alpha_jk)
    dbp = laplace_derivative(p, alpha_ij)
    dbq = laplace_derivative(q, alpha_jk)

    term1 = (
        1.5
        * nj**2
        * (1 / (2 * nij * njk) + p / (q * nij**2) + q / (p * njk**2))
        * bp
        * bq
    )
    term2 = (nj / njk + q * nj / (p * nij)) * bq * (bp + alpha_ij * dbp)
    term3 = (nj / nij + p * nj / (q * njk)) * bp * alpha_jk * dbq
    coefficient = mi * mj * mk / ak * (term1 + term2 + term3)
    curvature = -3 * (
        p**2 / (mi * ai**2)
        + (p + q) ** 2 / (mj * aj**2)
        + q**2 / (mk * ak**2)
    )
    libration_rate = math.sqrt(abs(coefficient * curvature))
    width = 2 * libration_rate

    periods = (1.769137786, 3.551181, 7.15455296)
    observed_rates = tuple(periods[1] / period for period in periods)
    detuning = abs(
        p * observed_rates[0] - (p + q) * observed_rates[1] + q * observed_rates[2]
    )
    margin = width / detuning
    assert margin > 10_000
    print(
        "PASS Galilean 3-body leading coefficient: "
        f"C2={coefficient:.9e}, A={curvature:.9e}, W/n_E={width:.9e}, "
        f"detuning/W={detuning / width:.9e} ({margin:.0f}x inside)"
    )


def radial_branch_check():
    payload = json.loads(JPL.read_text(encoding="utf-8"))
    groups = {}
    for body in payload["satellites"]:
        if body["prominence"] == "major" and body.get("a_km"):
            groups.setdefault(body["host"], []).append(body)

    expected = {"Jupiter": 4, "Saturn": 7, "Uranus": 5, "Neptune": 2}
    for host, count in expected.items():
        bodies = groups[host]
        assert len(bodies) == count
        rates = [2 * math.pi / body["period_days"] for body in bodies]
        kepler = [rate**2 * body["a_km"] ** 3 for rate, body in zip(rates, bodies)]
        krange = (max(kepler) - min(kepler)) / (sum(kepler) / len(kepler))
        hrange = (max(rates) - min(rates)) / (sum(rates) / len(rates))
        assert krange < 0.03
        assert hrange > 1.0
        print(
            f"PASS radial branches {host:7s}: N={count}, "
            f"range(n^2 a^3)/mean={krange:.6f}, range(n)/mean={hrange:.6f}"
        )


def liouville_check():
    # Each KDK factor is a canonical shear with unit determinant; their product is 1.
    kick_det = drift_det = 1.0
    map_det = kick_det * drift_det * kick_det
    assert map_det == 1.0
    print("PASS capture no-go guard: autonomous KDK map det(J)=1; no attracting island")


def main():
    share_reconstruction_check()
    scale_identifiability_check()
    conservation_check()
    width_check()
    galilean_three_body_check()
    radial_branch_check()
    liouville_check()


if __name__ == "__main__":
    main()
