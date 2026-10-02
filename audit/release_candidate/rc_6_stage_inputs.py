# -*- coding: utf-8 -*-
"""RC-6 staged controlled input: scripts/projection/master_structure.json — 34_EVIDENCE_PASSPORTS gains publisher_ar
(CONTRIBUTING.md §9), installed by run_stage.py --install. One-space JSON indent kept.

  python3 rc_6_stage_inputs.py <stage_dir>
"""
import json, os, sys
from collections import OrderedDict

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


def main():
    stage = sys.argv[1]
    os.makedirs(stage, exist_ok=True)
    with open(os.path.join(ROOT, "scripts/projection/master_structure.json"), encoding="utf-8") as fh:
        ms = json.load(fh, object_pairs_hook=OrderedDict)
    labels = ms["sheets"]["34_EVIDENCE_PASSPORTS"]["main_labels"]
    if labels[-1] != "display_requirements":
        raise SystemExit(f"34 main_labels not as expected: {labels}")
    labels.append("publisher_ar")
    with open(os.path.join(stage, "master_structure.json"), "w", encoding="utf-8") as fh:
        json.dump(ms, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("staged:", os.path.join(stage, "master_structure.json"))


if __name__ == "__main__":
    main()
