# -*- coding: utf-8 -*-
"""RC-1 staged controlled inputs (installed by audit/tranche_b_execution/run_stage.py with --install).

  python3 rc_1_stage_inputs.py <stage_dir>

Writes, from the repository's current files, the two files inside the runner's snapshot that RC-1 changes besides the
Master:
  * scripts/projection/controlled_inputs/visual_design_contract.json — frame_labels: UI-VIS-NOTE-POS-SCOPE bound to
    RV-CWR-004 and RV-CWR-009 (item 5); UI-VIS-NOTE-FIRM-CONSTRAINTS-PARTIAL bound to VIS-FIRM-CONSTRAINTS (item 6, Path B);
    VIS-REMITTANCE-COST series rpw state MEASURED → REPORTED (item 8 b).
  * scripts/projection/master_structure.json — 14_SYSTEM_CHRONOLOGY gains verification_note_en / verification_note_ar
    (item 3, Path B; CONTRIBUTING.md §9).
The JSON indent of each file is kept (one space).
"""
import json, os, sys
from collections import OrderedDict

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


def load(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return json.load(fh, object_pairs_hook=OrderedDict)


def dump(obj, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=1)
        fh.write("\n")


def main():
    stage = sys.argv[1]
    vdc = load("scripts/projection/controlled_inputs/visual_design_contract.json")
    want = {"RV-CWR-004": "UI-VIS-NOTE-POS-SCOPE", "RV-CWR-009": "UI-VIS-NOTE-POS-SCOPE", "VIS-FIRM-CONSTRAINTS": "UI-VIS-NOTE-FIRM-CONSTRAINTS-PARTIAL"}
    seen = set()
    for v in vdc["visuals"]:
        vid = v["visual_id"]
        if vid in want:
            fl = v["contract"].setdefault("frame_labels", [])
            if want[vid] in fl:
                raise SystemExit(f"{vid} already binds {want[vid]}")
            fl.append(want[vid])
            seen.add(vid)
    if seen != set(want):
        raise SystemExit(f"contracts not found: {set(want) - seen}")
    # item 8 (b): VIS-REMITTANCE-COST — averages of published price quotes are REPORTED by the source, not MEASURED in a population survey
    rc = next(v for v in vdc["visuals"] if v["visual_id"] == "VIS-REMITTANCE-COST")
    rpw = next(x for x in rc["contract"]["series"] if x["id"] == "rpw")
    if rpw["state"] != "MEASURED":
        raise SystemExit(f"VIS-REMITTANCE-COST rpw state is {rpw['state']!r}, expected MEASURED")
    rpw["state"] = "REPORTED"
    dump(vdc, os.path.join(stage, "visual_design_contract.json"))

    ms = load("scripts/projection/master_structure.json")
    labels = ms["sheets"]["14_SYSTEM_CHRONOLOGY"]["main_labels"]
    if labels[-1] != "period_ar" or len(labels) != 17:
        raise SystemExit(f"14 main_labels not as expected: {labels}")
    labels.extend(["verification_note_en", "verification_note_ar"])
    dump(ms, os.path.join(stage, "master_structure.json"))
    print("staged:", os.path.join(stage, "visual_design_contract.json"), os.path.join(stage, "master_structure.json"))


if __name__ == "__main__":
    main()
