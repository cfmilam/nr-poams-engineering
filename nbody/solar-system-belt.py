#!/usr/bin/env python3
"""Population-level destructive-closure audit of the asteroid belt.

Registration (2026-09-09, before widening the prior 2.30--3.50 AU pull):
  * JPL SBDB numbered asteroids, H <= 15, 2.00 <= a <= 4.20 AU;
  * primary gap sample 0.10 <= e <= 0.20, 0.005 AU bins;
  * gap edge = contiguous bins below half the registered flank median;
  * prediction gate: centers within 0.2%; all four half-widths within factor 3;
  * storage control: density within +/-0.05 AU of the 3:2 Hilda centre exceeds
    the registered equal-width sideband density;
  * migration-scar control: exterior/interior density ratios are reported for
    the regions used by Minton & Malhotra (2009), never fit.

The width calculation is the direct-term, eccentricity-order normal form already
benchmarked independently by nbody-n4-extract.py.  Population gaps are outcomes of
the full solar-system history; agreement is a forward confrontation, not an input.
"""

from __future__ import annotations

import argparse
import gzip
import json
import math
import statistics
import subprocess
import tempfile
import urllib.parse
import urllib.request
from pathlib import Path


API = "https://ssd-api.jpl.nasa.gov/sbdb_query.api"
PROPER_URL = "https://www2.boulder.swri.edu/~davidn/Proper24/proper_catalog24.dat.gz"
A_MIN, A_MAX, H_MAX = 2.00, 4.20, 15.0
BIN_WIDTH = 0.005
A_JUPITER = 5.2044
MARS_APHELION = 1.666
JUPITER_PERIHELION = 4.951
JUPITER_SHARE = 9.5458e-4

# Direct coefficients produced by nbody-n4-extract.py at the exact nominal alpha.
RESONANCES = {
    "4:1": {"p": 4, "q": 1, "coefficient": None, "published_center": 2.06},
    "3:1": {"p": 3, "q": 1, "coefficient": 0.5983, "published_center": 2.502,
            "flanks": [(2.36, 2.46), (2.54, 2.64)]},
    "5:2": {"p": 5, "q": 2, "coefficient": -1.1297, "published_center": 2.825,
            "flanks": [(2.72, 2.79), (2.86, 2.91)]},
    "7:3": {"p": 7, "q": 3, "coefficient": 2.2323, "published_center": 2.958,
            "flanks": [(2.88, 2.93), (2.99, 3.02)]},
    "2:1": {"p": 2, "q": 1, "coefficient": -1.1910, "published_center": 3.279,
            "flanks": [(3.10, 3.22)]},
    "3:2": {"p": 3, "q": 2, "coefficient": None, "published_center": 3.97},
}


def fetch(cache_dir: Path, refresh: bool) -> list[tuple[float, float, float]]:
    cache_dir.mkdir(parents=True, exist_ok=True)
    path = cache_dir / "jpl-sbdb-numbered-H15-a2.00-4.20.json"
    if not path.exists() or refresh:
        params = {
            "fields": "a,e,H",
            "sb-kind": "a",
            "sb-ns": "n",
            "sb-cdata": json.dumps({"AND": [f"a|GE|{A_MIN}", f"a|LE|{A_MAX}", f"H|LE|{H_MAX}"]}),
        }
        url = API + "?" + urllib.parse.urlencode(params)
        request = urllib.request.Request(url, headers={"User-Agent": "NR-POAMS solar-system audit"})
        with urllib.request.urlopen(request, timeout=180) as response:
            path.write_bytes(response.read())
    payload = json.loads(path.read_text(encoding="utf-8"))
    rows = []
    for raw in payload["data"]:
        try:
            rows.append(tuple(float(value) for value in raw))
        except (TypeError, ValueError):
            continue
    return rows


def fetch_proper_7_3(cache_dir: Path, refresh: bool) -> list[tuple[float, float, float]]:
    """Read the 2024 synthetic proper-orbit catalog for the prospective 7:3 test."""
    cache_dir.mkdir(parents=True, exist_ok=True)
    path = cache_dir / "proper_catalog24.dat.gz"
    if not path.exists() or refresh:
        subprocess.run(["curl", "-fL", "-sS", PROPER_URL, "-o", str(path)], check=True, timeout=300)
    rows = []
    with gzip.open(path, "rt", encoding="utf-8", errors="replace") as stream:
        for line in stream:
            columns = line.split()
            if len(columns) < 10:
                continue
            try:
                a, e, h = float(columns[0]), float(columns[2]), float(columns[8])
            except ValueError:
                continue
            if 2.88 <= a <= 3.02 and h <= H_MAX:
                rows.append((a, e, h))
    return rows


def center(p: int, q: int) -> float:
    return (q / p) ** (2.0 / 3.0) * A_JUPITER


def leading_half_width(p: int, q: int, coefficient: float, eccentricity: float) -> float:
    alpha = (q / p) ** (2.0 / 3.0)
    order = p - q
    # The resonant-angle width is W_phi/n=2q*sqrt(...), but
    # phi_dot = p*n_J-q*n-(p-q)*varpi_dot, so delta n=W_phi/q.
    # The earlier N4 run accidentally retained q in the subsequent da conversion.
    mean_motion_width_over_n = 2 * math.sqrt(
        3 * alpha * JUPITER_SHARE * abs(coefficient) * eccentricity**order
    )
    return (2.0 / 3.0) * center(p, q) * mean_motion_width_over_n


def bins(rows: list[tuple[float, float, float]], e_range: tuple[float, float] | None) -> list[int]:
    count = round((A_MAX - A_MIN) / BIN_WIDTH)
    values = [0] * count
    for a, e, _ in rows:
        if e_range is not None and not (e_range[0] <= e <= e_range[1]):
            continue
        index = int((a - A_MIN) / BIN_WIDTH)
        if 0 <= index < count:
            values[index] += 1
    return values


def indices(lo: float, hi: float) -> list[int]:
    count = round((A_MAX - A_MIN) / BIN_WIDTH)
    return [
        i for i in range(count)
        if A_MIN + i * BIN_WIDTH >= lo - 1e-12 and A_MIN + (i + 1) * BIN_WIDTH <= hi + 1e-12
    ]


def gap_measure(hist: list[int], nominal: float, flanks: list[tuple[float, float]], one_sided: bool) -> dict:
    flank_bins = [i for lo, hi in flanks for i in indices(lo, hi)]
    background = statistics.median(hist[i] for i in flank_bins)
    threshold = 0.5 * background
    candidates = [i for i in range(len(hist)) if abs(A_MIN + (i + 0.5) * BIN_WIDTH - nominal) <= 0.02]
    core = min(candidates, key=lambda i: (hist[i], abs(A_MIN + (i + 0.5) * BIN_WIDTH - nominal)))
    if hist[core] >= threshold:
        return {"status": "null", "background_per_bin": background, "threshold": threshold}
    left = right = core
    while left > 0 and hist[left - 1] < threshold:
        left -= 1
    while right + 1 < len(hist) and hist[right + 1] < threshold:
        right += 1
    lo, hi = A_MIN + left * BIN_WIDTH, A_MIN + (right + 1) * BIN_WIDTH
    core_center = A_MIN + (core + 0.5) * BIN_WIDTH
    half_width = core_center - lo if one_sided else (hi - lo) / 2
    return {
        "status": "measured",
        "background_per_bin": background,
        "threshold": threshold,
        "minimum_bin_center_au": core_center,
        "minimum_bin_count": hist[core],
        "run_au": [lo, hi],
        "half_width_au": half_width,
    }


def density(rows: list[tuple[float, float, float]], lo: float, hi: float) -> float:
    return sum(lo <= a < hi for a, _, _ in rows) / (hi - lo)


def run(cache_dir: Path, refresh: bool) -> dict:
    rows = fetch(cache_dir, refresh)
    proper_7_3_rows = fetch_proper_7_3(cache_dir, refresh)
    primary_rows = [row for row in rows if 0.10 <= row[1] <= 0.20]
    hist = bins(primary_rows, None)
    results = {}
    passed_widths = 0
    scored_widths = 0
    for name in ("3:1", "5:2", "7:3", "2:1"):
        item = RESONANCES[name]
        p, q = item["p"], item["q"]
        predicted_center = center(p, q)
        predicted_width = leading_half_width(p, q, item["coefficient"], 0.15)
        observed = gap_measure(hist, item["published_center"], item["flanks"], name == "2:1")
        factor = None
        if observed["status"] == "measured":
            factor = max(predicted_width / observed["half_width_au"], observed["half_width_au"] / predicted_width)
        scored = True
        if scored:
            scored_widths += 1
            passed_widths += int(factor is not None and factor <= 3.0)
        results[name] = {
            "computed_center_au": predicted_center,
            "published_center_au": item["published_center"],
            "center_error_percent": 100 * (predicted_center / item["published_center"] - 1),
            "leading_half_width_at_e_0.15_au": predicted_width,
            "observed": observed,
            "width_factor": factor,
            "registered_width_scored": scored,
            "mars_crossing_e": 1 - MARS_APHELION / predicted_center,
            "jupiter_crossing_e": JUPITER_PERIHELION / predicted_center - 1,
        }
    if max(abs(item["center_error_percent"]) for item in results.values()) > 0.2:
        raise AssertionError("resonance-center gate failed")
    if passed_widths != scored_widths:
        raise AssertionError(f"registered width gate failed: {passed_widths}/{scored_widths}")

    proper_7_3_primary = [row for row in proper_7_3_rows if 0.10 <= row[1] <= 0.20]
    proper_7_3_hist = bins(proper_7_3_primary, None)
    proper_7_3 = gap_measure(
        proper_7_3_hist,
        RESONANCES["7:3"]["published_center"],
        RESONANCES["7:3"]["flanks"],
        False,
    )
    predicted_7_3 = results["7:3"]["leading_half_width_at_e_0.15_au"]
    proper_7_3_factor = max(
        predicted_7_3 / proper_7_3["half_width_au"],
        proper_7_3["half_width_au"] / predicted_7_3,
    )

    hilda_center = center(3, 2)
    hilda_core = density(rows, hilda_center - 0.05, hilda_center + 0.05)
    hilda_side = 0.5 * (
        density(rows, hilda_center - 0.20, hilda_center - 0.10)
        + density(rows, hilda_center + 0.10, hilda_center + 0.20)
    )
    hilda_ratio = hilda_core / hilda_side
    if hilda_ratio <= 1:
        raise AssertionError(f"Hilda storage control failed: density ratio {hilda_ratio}")

    scars = {
        "outside_5:2_to_7:3_vs_inside_5:2": {
            "outside_interval_au": [2.86, 2.93],
            "inside_interval_au": [2.72, 2.79],
            "density_ratio": density(rows, 2.86, 2.93) / density(rows, 2.72, 2.79),
        },
        "outside_2:1_vs_inside_2:1": {
            "outside_interval_au": [3.34, 3.47],
            "inside_interval_au": [3.10, 3.23],
            "density_ratio": density(rows, 3.34, 3.47) / density(rows, 3.10, 3.23),
        },
    }
    return {
        "provenance": {
            "service": "NASA/JPL Small-Body Database Query API",
            "api": API,
            "selection": f"numbered asteroids, H<={H_MAX}, {A_MIN}<=a<={A_MAX} AU",
            "note": "Osculating semimajor axes; population-edge comparison, not proper-element dynamics.",
        },
        "population": {"all": len(rows), "primary_e_0.10_0.20": len(primary_rows)},
        "resonances": results,
        "registered_width_gate": f"{passed_widths}/{scored_widths} pass within factor 3",
        "proper_orbit_7:3_control": {
            "source": PROPER_URL,
            "catalog": "Nesvorny et al. 2024 synthetic proper-orbit catalog",
            "selected_rows": len(proper_7_3_primary),
            "observed": proper_7_3,
            "predicted_half_width_au": predicted_7_3,
            "width_factor": proper_7_3_factor,
            "passed_factor_3": proper_7_3_factor <= 3.0,
        },
        "hilda_3:2_storage_control": {
            "computed_center_au": hilda_center,
            "core_density_per_au": hilda_core,
            "sideband_density_per_au": hilda_side,
            "core_to_sideband_ratio": hilda_ratio,
            "passed": True,
        },
        "migration_scar_density_controls": scars,
        "interpretation": (
            "The pair kernel predicts channel locations and leading eccentricity-dependent widths. "
            "Escape requires eccentricity growth to a crossing boundary; storage versus clearing is "
            "therefore a phase-space topology result, not a property of the integer ratio alone."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cache-dir", type=Path, default=Path(tempfile.gettempdir()) / "poams-sbdb")
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run(args.cache_dir, args.refresh)
    text = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
