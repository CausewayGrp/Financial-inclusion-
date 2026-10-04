# -*- coding: utf-8 -*-
"""RC-10 staged controlled input: scripts/projection/master_structure.json — 00_MASTER declares its new titled block
"EVIDENCE LANDSCAPE / مشهد الأدلة" (the evidence landscape, Owner Addendum 2 improvement 3), installed by run_stage.py
--install. One-space JSON indent kept.

  python3 rc_10_stage_inputs.py <stage_dir>
"""
import json, os, sys
from collections import OrderedDict

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
TITLE = "EVIDENCE LANDSCAPE / مشهد الأدلة"


def main():
    stage = sys.argv[1]
    os.makedirs(stage, exist_ok=True)
    with open(os.path.join(ROOT, "scripts/projection/master_structure.json"), encoding="utf-8") as fh:
        ms = json.load(fh, object_pairs_hook=OrderedDict)
    blocks = ms["sheets"]["00_MASTER"]["blocks"]
    if blocks:
        raise SystemExit(f"00_MASTER blocks not as expected: {blocks}")
    blocks.append(OrderedDict([("title", TITLE), ("header", True)]))
    with open(os.path.join(stage, "master_structure.json"), "w", encoding="utf-8") as fh:
        json.dump(ms, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("staged:", os.path.join(stage, "master_structure.json"))


if __name__ == "__main__":
    main()
