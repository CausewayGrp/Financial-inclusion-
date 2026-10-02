# -*- coding: utf-8 -*-
"""RC-2 staged controlled inputs (installed by audit/tranche_b_execution/run_stage.py with --install).

  python3 rc_2_stage_inputs.py <stage_dir>

Writes, from the repository's current files, the three files inside the runner's snapshot that RC-2 changes besides the
Master (item 13: the public count chronology_events follows its own definition, "Dated events in the system chronology"):
  * scripts/projection/controlled_inputs/public_inventory_contract.json — chronology_events: rule count_records →
    count_where_not_in (field event_class, exclude SYSTEM_INTERPRETATION: YSC-020, the analytical rule, is not an event);
  * scripts/projection/projection_manifest.json — the inventory output's transformation lists the new rule;
  * README.md — "24 documented chronology events" → 23 (the count the generator now derives).
Each file's JSON formatting is kept (two-space indent, trailing newline).
"""
import json, os, sys
from collections import OrderedDict

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


def load(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return json.load(fh, object_pairs_hook=OrderedDict)


def dump(obj, path):
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=2)
        fh.write("\n")


def main():
    stage = sys.argv[1]
    os.makedirs(stage, exist_ok=True)

    pic = load("scripts/projection/controlled_inputs/public_inventory_contract.json")
    ce = pic["counts"]["chronology_events"]
    if ce["rule"] != "count_records" or ce["projection"] != "visuals/system_chronology.json":
        raise SystemExit(f"chronology_events not as expected: {dict(ce)}")
    new = OrderedDict()
    for k, v in ce.items():
        new[k] = v
        if k == "rule":
            new["rule"] = "count_where_not_in"
            new["field"] = "event_class"
            new["exclude"] = ["SYSTEM_INTERPRETATION"]
    pic["counts"]["chronology_events"] = new
    dump(pic, os.path.join(stage, "public_inventory_contract.json"))

    pm = load("scripts/projection/projection_manifest.json")
    old = "count_records, count_where_http_primary_url, count_where_true or spec_count"
    hits = 0

    def walk(node):
        nonlocal hits
        if isinstance(node, dict):
            for k, v in node.items():
                if isinstance(v, str) and old in v:
                    node[k] = v.replace(old, "count_records, count_where_http_primary_url, count_where_true, count_where_not_in or spec_count")
                    hits += 1
                else:
                    walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)
    walk(pm)
    if hits != 1:
        raise SystemExit(f"projection_manifest rule list found {hits} times")
    dump(pm, os.path.join(stage, "projection_manifest.json"))

    readme = open(os.path.join(ROOT, "README.md"), encoding="utf-8").read()
    if readme.count("- 24 documented chronology events.") != 1:
        raise SystemExit("README chronology line not found once")
    with open(os.path.join(stage, "README.md"), "w", encoding="utf-8") as fh:
        fh.write(readme.replace("- 24 documented chronology events.", "- 23 documented chronology events (the analytical rule YSC-020 is not counted)."))
    print("staged:", ", ".join(os.path.join(stage, f) for f in ("public_inventory_contract.json", "projection_manifest.json", "README.md")))


if __name__ == "__main__":
    main()
