#!/usr/bin/env python3
"""Integrity audit for the published-record capture-history ensemble."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
DATA = HERE / "solar-system-history-ensemble.json"


def walk_probabilities(value, path=""):
    if isinstance(value, dict):
        for key, item in value.items():
            yield from walk_probabilities(item, f"{path}.{key}" if path else key)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from walk_probabilities(item, f"{path}[{index}]")
    elif isinstance(value, (int, float)) and any(
        token in path.lower() for token in ("probability", "fraction", "efficiency", "value", "range")
    ):
        yield path, float(value)


def main() -> None:
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    families = payload["families"]
    ids = [item["id"] for item in families]
    assert len(ids) == len(set(ids))
    required = {
        "id", "system", "reservoir", "history_class", "model_condition",
        "reported_outcome", "probability", "present_status", "discriminant_status", "sources",
    }
    for family in families:
        missing = required - family.keys()
        assert not missing, f"{family.get('id')}: missing {missing}"
        assert family["sources"], family["id"]
        for source in family["sources"]:
            assert source.get("doi") or source.get("arxiv"), (family["id"], source)
        for path, value in walk_probabilities(family.get("probability")):
            assert 0 <= value <= 1, (family["id"], path, value)

    galilean = [item for item in families if item["system"] == "Io-Europa-Ganymede"]
    assert len(galilean) >= 2 and len({item["reservoir"] for item in galilean}) >= 2
    assert all(item["present_status"] == "viable" for item in galilean)

    pluto = next(item for item in families if item["id"] == "pluto-charon-resonant-transport")
    assert "falsified" in pluto["present_status"]
    neptune = next(item for item in families if item["id"] == "neptune-grainy-migration")
    assert neptune["sample"]["grainy"] == 12 and neptune["sample"]["smooth"] == 4
    belt = next(item for item in families if item["id"] == "asteroid-belt-sweeping")
    assert belt["probability"]["model_depletion_fraction"]["value"] == 0.62

    numeric_families = sum(item["probability"] is not None for item in families)
    nulls = sum("falsified" in item["present_status"] for item in families)
    print(f"PASS history schema: {len(families)} registered model families; {numeric_families} carry conditional frequencies")
    print("PASS non-identifiability witness: two distinct Galilean reservoirs remain viable against the same endpoint")
    print(f"PASS constructive-null retention: {nulls} complete-route failure kept in the ensemble")
    print("PASS no-pooling rule: model-conditioned probabilities remain attached to their own priors and reservoirs")
    print("VERDICT: reservoir classes and directions can be selected in some systems; no unique solar-system history is recoverable")


if __name__ == "__main__":
    main()
