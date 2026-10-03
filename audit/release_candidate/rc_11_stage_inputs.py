# -*- coding: utf-8 -*-
"""RC-11 staged controlled input: scripts/projection/controlled_inputs/visual_design_contract.json — VIS-POS-TRANSACTIONS
binds the frame note UI-VIS-NOTE-POS-H1-WITHHELD (Part B B11), installed by run_stage.py --install. One-space indent kept.

  python3 rc_11_stage_inputs.py <stage_dir>
"""
import json, os, sys
from collections import OrderedDict

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
REL = "scripts/projection/controlled_inputs/visual_design_contract.json"


def main():
    stage = sys.argv[1]
    os.makedirs(stage, exist_ok=True)
    with open(os.path.join(ROOT, REL), encoding="utf-8") as fh:
        d = json.load(fh, object_pairs_hook=OrderedDict)
    c = [v for v in d["visuals"] if v.get("visual_id") == "VIS-POS-TRANSACTIONS" and "contract" in v]
    if len(c) != 1 or c[0]["contract"].get("frame_labels"):
        raise SystemExit("VIS-POS-TRANSACTIONS contract not as expected")
    c[0]["contract"]["frame_labels"] = ["UI-VIS-NOTE-POS-H1-WITHHELD"]
    with open(os.path.join(stage, "visual_design_contract.json"), "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("staged:", os.path.join(stage, "visual_design_contract.json"))


if __name__ == "__main__":
    main()
