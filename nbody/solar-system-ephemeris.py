#!/usr/bin/env python3
"""Ephemeris-grade closure audit for the Galilean Laplace angle.

The instrument downloads geometric osculating elements directly from the JPL
Horizons API and evaluates

    Phi_L = lambda_Io - 3 lambda_Europa + 2 lambda_Ganymede.

Horizons explicitly warns that satellite osculating elements are not initial
conditions for a separate propagation.  This program does not propagate them;
it evaluates the integrated JUP365 solution exactly at the returned epochs.

Registration (2026-09-09, before the 30-year pull):
  * interval: 2000-01-01 through 2030-01-01 TDB, one-day cadence;
  * frame/origin: J2000 ecliptic, Jupiter body centre (500@599);
  * lock gate: one circular cluster, full wrapped span < 180 degrees;
  * robustness: both 15-year halves and cadences 1/2/4/8 days pass the gate;
  * no orbital element from this table is used to initialize an integration.

Cross-system registration (same date, before the added pulls): the published
critical arguments for Mimas-Tethys, Enceladus-Dione, Titan-Hyperion, and
Naiad-Thalassa must remain bounded (wrapped span < 350 degrees) over the same
interval and both halves. These finite-window gates are consistency checks for
the cited locks; by themselves they do not prove sustained libration. Node-
bearing satellite arguments are evaluated in the central body's IAU equator-
and-node-of-date frame; node-free arguments are frame invariant. Janus-
Epimetheus is reported as a co-orbital exchange control because its horseshoe
angle need not fit inside one semicircle.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import math
import tempfile
import urllib.parse
import urllib.request
from pathlib import Path

import numpy as np


API = "https://ssd.jpl.nasa.gov/api/horizons.api"
MOONS = {"Io": "501", "Europa": "502", "Ganymede": "503"}
START = "2000-01-01"
STOP = "2030-01-01"
STEP = "1d"
PLUTO_START = "9000bc-Jan-01"
PLUTO_STOP = "9000-Jan-01"
# The preregistered 100 d pull exceeded Horizons' 90,024-row service ceiling.
# 400 d is the smallest round multiple that the service accepts across the
# full DE441 interval and remains orders finer than the millennial libration.
PLUTO_STEP = "400d"


def wrap_degrees(values: np.ndarray) -> np.ndarray:
    return (values + 180.0) % 360.0 - 180.0


def circular_center(values_deg: np.ndarray) -> float:
    radians = np.deg2rad(values_deg)
    return math.degrees(math.atan2(np.sin(radians).mean(), np.cos(radians).mean()))


def horizons_text(
    target: str,
    cache_dir: Path,
    refresh: bool,
    center: str = "500@599",
    start: str = START,
    stop: str = STOP,
    step: str = STEP,
    ref_plane: str = "ECLIPTIC",
) -> str:
    cache_dir.mkdir(parents=True, exist_ok=True)
    safe_center = center.replace("@", "at")
    safe_plane = ref_plane.lower().replace(" ", "-")
    path = cache_dir / f"horizons-{target}-{safe_center}-{start}-{stop}-{step}-{safe_plane}.txt"
    if path.exists() and not refresh:
        return path.read_text(encoding="utf-8")
    params = {
        "format": "text",
        "COMMAND": f"'{target}'",
        "OBJ_DATA": "'NO'",
        "MAKE_EPHEM": "'YES'",
        "EPHEM_TYPE": "'ELEMENTS'",
        "CENTER": f"'{center}'",
        "START_TIME": f"'{start}'",
        "STOP_TIME": f"'{stop}'",
        "STEP_SIZE": f"'{step}'",
        "REF_PLANE": f"'{ref_plane}'",
        "OUT_UNITS": "'KM-S'",
        "CSV_FORMAT": "'YES'",
    }
    url = API + "?" + urllib.parse.urlencode(params)
    request = urllib.request.Request(url, headers={"User-Agent": "NR-POAMS solar-system audit"})
    with urllib.request.urlopen(request, timeout=180) as response:
        text = response.read().decode("utf-8")
    if "$$SOE" not in text or "$$EOE" not in text:
        raise RuntimeError(f"Horizons returned no element table for target {target}: {text[:500]}")
    path.write_text(text, encoding="utf-8")
    return text


def parse_elements(text: str) -> dict[str, np.ndarray]:
    table = text.split("$$SOE", 1)[1].split("$$EOE", 1)[0]
    rows = []
    for row in csv.reader(io.StringIO(table)):
        if not row or not row[0].strip():
            continue
        # JDTDB, calendar, EC, QR, IN, OM, W, Tp, N, MA, TA, A, AD, PR
        rows.append([float(row[i].strip()) for i in (0, 2, 4, 5, 6, 8, 9, 11, 13)])
    values = np.asarray(rows, dtype=float)
    if values.shape[1] != 9:
        raise AssertionError(values.shape)
    return {
        "jd": values[:, 0],
        "e": values[:, 1],
        "inc_deg": values[:, 2],
        "node_deg": values[:, 3],
        "argperi_deg": values[:, 4],
        "mean_motion_deg_s": values[:, 5],
        "mean_anomaly_deg": values[:, 6],
        "a_km": values[:, 7],
        "period_s": values[:, 8],
    }


def cluster_metrics(phi_deg: np.ndarray, jd: np.ndarray) -> dict[str, float | bool]:
    center = circular_center(phi_deg)
    residual = wrap_degrees(phi_deg - center)
    span = float(residual.max() - residual.min())
    p995 = float(np.quantile(np.abs(residual), 0.995))
    slope, intercept = np.polyfit(jd - jd.mean(), residual, 1)
    # A true circulation cannot stay inside a semicircle for the full interval.
    passed = bool(span < 180.0)
    return {
        "center_deg": center,
        "span_deg": span,
        "max_abs_deg": float(np.max(np.abs(residual))),
        "p99_5_abs_deg": p995,
        "linear_drift_deg_per_year": float(slope * 365.25),
        "passed": passed,
    }


def dominant_period(phi_deg: np.ndarray, cadence_days: float) -> float:
    center = circular_center(phi_deg)
    series = wrap_degrees(phi_deg - center)
    series = series - np.polyval(np.polyfit(np.arange(len(series)), series, 1), np.arange(len(series)))
    spectrum = np.abs(np.fft.rfft(series)) ** 2
    frequencies = np.fft.rfftfreq(len(series), d=cadence_days)
    # The slow Laplace libration is sought between 100 d and 20 yr; faster
    # osculating terms are deliberately outside the reported peak search.
    mask = (frequencies >= 1.0 / (20 * 365.25)) & (frequencies <= 1.0 / 100.0)
    index = np.flatnonzero(mask)[np.argmax(spectrum[mask])]
    return float(1.0 / frequencies[index])


def dominant_period_between(
    phi_deg: np.ndarray, cadence_days: float, minimum_days: float, maximum_days: float
) -> float:
    """Return the strongest detrended period inside a preregistered band."""
    center = circular_center(phi_deg)
    series = wrap_degrees(phi_deg - center)
    index_axis = np.arange(len(series))
    series = series - np.polyval(np.polyfit(index_axis, series, 1), index_axis)
    spectrum = np.abs(np.fft.rfft(series)) ** 2
    frequencies = np.fft.rfftfreq(len(series), d=cadence_days)
    mask = (frequencies >= 1.0 / maximum_days) & (frequencies <= 1.0 / minimum_days)
    index = np.flatnonzero(mask)[np.argmax(spectrum[mask])]
    return float(1.0 / frequencies[index])


def element_system(
    targets: dict[str, str],
    center: str,
    cache_dir: Path,
    refresh: bool,
    ref_plane: str = "ECLIPTIC",
) -> dict[str, dict[str, np.ndarray]]:
    result = {
        name: parse_elements(
            horizons_text(target, cache_dir, refresh, center=center, ref_plane=ref_plane)
        )
        for name, target in targets.items()
    }
    jd = next(iter(result.values()))["jd"]
    for name, data in result.items():
        if not np.array_equal(jd, data["jd"]):
            raise AssertionError(f"epoch mismatch for {center} / {name}")
    return result


def angles_for(elements: dict[str, dict[str, np.ndarray]]) -> tuple[dict[str, np.ndarray], dict[str, np.ndarray]]:
    longitude = {
        name: wrap_degrees(data["node_deg"] + data["argperi_deg"] + data["mean_anomaly_deg"])
        for name, data in elements.items()
    }
    longitude_peri = {
        name: wrap_degrees(data["node_deg"] + data["argperi_deg"])
        for name, data in elements.items()
    }
    return longitude, longitude_peri


def run(cache_dir: Path, refresh: bool) -> dict:
    elements = element_system(MOONS, "500@599", cache_dir, refresh)
    lengths = {name: len(data["jd"]) for name, data in elements.items()}
    if len(set(lengths.values())) != 1:
        raise AssertionError(f"epoch count mismatch: {lengths}")
    jd = elements["Io"]["jd"]
    for name, data in elements.items():
        if not np.array_equal(jd, data["jd"]):
            raise AssertionError(f"epoch mismatch for {name}")

    longitude, longitude_peri = angles_for(elements)
    phi = wrap_degrees(longitude["Io"] - 3 * longitude["Europa"] + 2 * longitude["Ganymede"])
    full = cluster_metrics(phi, jd)
    half = len(jd) // 2
    windows = {
        "first_half": cluster_metrics(phi[:half], jd[:half]),
        "second_half": cluster_metrics(phi[half:], jd[half:]),
    }
    cadences = {
        f"{stride}d": cluster_metrics(phi[::stride], jd[::stride])
        for stride in (1, 2, 4, 8)
    }
    if not full["passed"] or not all(x["passed"] for x in windows.values()) or not all(
        x["passed"] for x in cadences.values()
    ):
        raise AssertionError("registered bounded-libration gate failed")

    # The Galilean lock is a connected chain, not an isolated pure three-body
    # pendulum.  Three of the four first-order 2:1 arguments librate while the
    # Ganymede-pericentre argument circulates.  This topology is the physical
    # reason a single scalar "Laplace width" is not a precision observable.
    resonant_angles = {
        "Io-Europa / varpi_Io": wrap_degrees(
            longitude["Io"] - 2 * longitude["Europa"] + longitude_peri["Io"]
        ),
        "Io-Europa / varpi_Europa": wrap_degrees(
            longitude["Io"] - 2 * longitude["Europa"] + longitude_peri["Europa"]
        ),
        "Europa-Ganymede / varpi_Europa": wrap_degrees(
            longitude["Europa"] - 2 * longitude["Ganymede"] + longitude_peri["Europa"]
        ),
        "Europa-Ganymede / varpi_Ganymede": wrap_degrees(
            longitude["Europa"] - 2 * longitude["Ganymede"] + longitude_peri["Ganymede"]
        ),
    }
    angle_topology = {
        name: {
            **cluster_metrics(angle, jd),
            "dominant_slow_period_days": dominant_period(angle, 1.0),
        }
        for name, angle in resonant_angles.items()
    }
    librating_count = sum(bool(item["passed"]) for item in angle_topology.values())
    if librating_count != 3:
        raise AssertionError(f"expected 3/4 first-order arguments to librate, found {librating_count}/4")

    # The instantaneous osculating rate combination is a noisy diagnostic, not
    # the derivative of a separately propagated orbit.
    detuning_deg_s = (
        elements["Io"]["mean_motion_deg_s"]
        - 3 * elements["Europa"]["mean_motion_deg_s"]
        + 2 * elements["Ganymede"]["mean_motion_deg_s"]
    )

    saturn = element_system(
        {
            "Mimas": "601", "Enceladus": "602", "Tethys": "603", "Dione": "604",
            "Titan": "606", "Hyperion": "607", "Janus": "610", "Epimetheus": "611",
        },
        "500@699",
        cache_dir,
        refresh,
        ref_plane="BODY",
    )
    saturn_lam, saturn_varpi = angles_for(saturn)
    saturn_node = {name: data["node_deg"] for name, data in saturn.items()}
    saturn_angles = {
        "Mimas-Tethys 4:2 mixed-inclination": wrap_degrees(
            4 * saturn_lam["Tethys"] - 2 * saturn_lam["Mimas"]
            - saturn_node["Mimas"] - saturn_node["Tethys"]
        ),
        "Enceladus-Dione 2:1 / varpi_Enceladus": wrap_degrees(
            2 * saturn_lam["Dione"] - saturn_lam["Enceladus"] - saturn_varpi["Enceladus"]
        ),
        "Titan-Hyperion 4:3 / varpi_Hyperion": wrap_degrees(
            4 * saturn_lam["Hyperion"] - 3 * saturn_lam["Titan"] - saturn_varpi["Hyperion"]
        ),
    }
    cross_system = {}
    saturn_jd = saturn["Mimas"]["jd"]
    for name, angle in saturn_angles.items():
        metrics = cluster_metrics(angle, saturn_jd)
        halves = [
            cluster_metrics(angle[: len(angle) // 2], saturn_jd[: len(angle) // 2]),
            cluster_metrics(angle[len(angle) // 2 :], saturn_jd[len(angle) // 2 :]),
        ]
        bounded = metrics["span_deg"] < 350 and all(item["span_deg"] < 350 for item in halves)
        cross_system[name] = {**metrics, "bounded_350deg_gate": bounded}
        if not bounded:
            raise AssertionError(f"registered cross-system angle gate failed: {name}")

    janus_angle = wrap_degrees(saturn_lam["Janus"] - saturn_lam["Epimetheus"])
    cross_system["Janus-Epimetheus 1:1 horseshoe control"] = {
        **cluster_metrics(janus_angle, saturn_jd),
        "bounded_350deg_gate": None,
        "classification": "co-orbital exchange control; reported, not scored by the semicircle gate",
    }

    neptune = element_system(
        {"Naiad": "803", "Thalassa": "804"},
        "500@899",
        cache_dir,
        refresh,
        ref_plane="BODY",
    )
    neptune_lam, _ = angles_for(neptune)
    naiad_angle = wrap_degrees(
        73 * neptune_lam["Thalassa"] - 69 * neptune_lam["Naiad"] - 4 * neptune["Naiad"]["node_deg"]
    )
    neptune_jd = neptune["Naiad"]["jd"]
    naiad_metrics = cluster_metrics(naiad_angle, neptune_jd)
    naiad_halves = [
        cluster_metrics(naiad_angle[: len(naiad_angle) // 2], neptune_jd[: len(naiad_angle) // 2]),
        cluster_metrics(naiad_angle[len(naiad_angle) // 2 :], neptune_jd[len(naiad_angle) // 2 :]),
    ]
    naiad_bounded = naiad_metrics["span_deg"] < 350 and all(item["span_deg"] < 350 for item in naiad_halves)
    cross_system["Naiad-Thalassa 73:69 inclination"] = {
        **naiad_metrics,
        "bounded_350deg_gate": naiad_bounded,
    }
    if not naiad_bounded:
        raise AssertionError("registered cross-system angle gate failed: Naiad-Thalassa")

    # DE441 covers almost one full Neptune-Pluto resonant cycle.  The 400-day
    # cadence is far finer than the roughly 20 kyr libration and satisfies the
    # Horizons row ceiling.  Barycentres avoid internal-system
    # wobble in this heliocentric planetary argument.
    trans_neptunian = {
        name: parse_elements(
            horizons_text(
                target,
                cache_dir,
                refresh,
                center="500@10",
                start=PLUTO_START,
                stop=PLUTO_STOP,
                step=PLUTO_STEP,
                ref_plane="ECLIPTIC",
            )
        )
        for name, target in {"Neptune barycenter": "8", "Pluto barycenter": "9"}.items()
    }
    pluto_jd = trans_neptunian["Pluto barycenter"]["jd"]
    if not np.array_equal(pluto_jd, trans_neptunian["Neptune barycenter"]["jd"]):
        raise AssertionError("epoch mismatch for Neptune-Pluto long interval")
    trans_lam, trans_varpi = angles_for(trans_neptunian)
    pluto_argument = wrap_degrees(
        3 * trans_lam["Pluto barycenter"]
        - 2 * trans_lam["Neptune barycenter"]
        - trans_varpi["Pluto barycenter"]
    )
    pluto_metrics = cluster_metrics(pluto_argument, pluto_jd)
    pluto_half = len(pluto_jd) // 2
    pluto_halves = {
        "first_half": cluster_metrics(pluto_argument[:pluto_half], pluto_jd[:pluto_half]),
        "second_half": cluster_metrics(pluto_argument[pluto_half:], pluto_jd[pluto_half:]),
    }
    if not pluto_metrics["passed"] or not all(item["passed"] for item in pluto_halves.values()):
        raise AssertionError("registered Neptune-Pluto long-interval libration gate failed")
    cross_system["Neptune-Pluto 3:2 / varpi_Pluto"] = {
        **pluto_metrics,
        "epochs": int(len(pluto_jd)),
        "interval": f"{PLUTO_START} to {PLUTO_STOP}",
        "step": PLUTO_STEP,
        "window_robustness": pluto_halves,
        "dominant_period_years": dominant_period_between(
            pluto_argument,
            400.0,
            minimum_days=5_000 * 365.25,
            maximum_days=40_000 * 365.25,
        ) / 365.25,
    }
    summary = {
        "provenance": {
            "service": "NASA/JPL Horizons API",
            "source_solution": "JUP365 merged (reported by Horizons)",
            "api": API,
            "retrieved_utc": np.datetime_as_string(np.datetime64("now"), unit="s") + "Z",
            "start_tdb": START,
            "stop_tdb": STOP,
            "step": STEP,
            "center": "500@599 (Jupiter body center)",
            "reference_plane": "J2000 ecliptic",
            "node_bearing_cross_system_reference_plane": (
                "central-body IAU equator and node of date (Horizons REF_PLANE=BODY)"
            ),
            "warning": "Osculating elements evaluated in place; never used to initialize a separate integration.",
        },
        "epochs": int(len(jd)),
        "laplace_angle": "lambda_Io - 3 lambda_Europa + 2 lambda_Ganymede",
        "full_interval": full,
        "window_robustness": windows,
        "cadence_robustness": cadences,
        "dominant_slow_period_days": dominant_period(phi, 1.0),
        "connected_angle_topology": angle_topology,
        "connected_angle_librating_count": librating_count,
        "width_interpretation": (
            "The observed object is a connected two-resonance domain. The isolated pure-three-body "
            "leading coefficient remains an identification calculation, not a precision scalar width."
        ),
        "cross_system_named_angles": cross_system,
        "osculating_detuning_deg_per_day": {
            "median": float(np.median(detuning_deg_s) * 86400.0),
            "p01": float(np.quantile(detuning_deg_s, 0.01) * 86400.0),
            "p99": float(np.quantile(detuning_deg_s, 0.99) * 86400.0),
        },
        "element_ranges": {
            name: {
                "a_km_min": float(data["a_km"].min()),
                "a_km_max": float(data["a_km"].max()),
                "e_min": float(data["e"].min()),
                "e_max": float(data["e"].max()),
            }
            for name, data in elements.items()
        },
    }
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cache-dir", type=Path, default=Path(tempfile.gettempdir()) / "poams-horizons")
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    summary = run(args.cache_dir, args.refresh)
    rendered = json.dumps(summary, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
