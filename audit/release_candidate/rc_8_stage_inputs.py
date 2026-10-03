# -*- coding: utf-8 -*-
"""RC-8 staged controlled input: scripts/projection/controlled_inputs/visual_design_contract.json, installed by
run_stage.py --install. The three POS panels expect the months to June 2026 and pin the June observations; RV-CWR-009
draws the June 2026 terminal stock and transactions (OBS-00095, OBS-00096) instead of January's; the transactions
rationale names the new monthly high (May 2026). One-space JSON indent kept; every change states what it expects to find.

  python3 rc_8_stage_inputs.py <stage_dir>
"""
import json, os, sys
from collections import OrderedDict

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
REL = "scripts/projection/controlled_inputs/visual_design_contract.json"
OLD_X = ["2025-03", "2025-04", "2025-05", "2025-06", "2025-07", "2025-08", "2025-09", "2025-10", "2025-11", "2025-12", "2026-01"]
NEW_X = OLD_X + ["2026-02", "2026-03", "2026-04", "2026-05", "2026-06"]
PINS = {  # visual: (old must_equal, new must_equal)
    "VIS-POS-TERMINALS": ({"OBS-00051": 561, "OBS-00077": 1357, "OBS-00080": 1473},
                          {"OBS-00051": 561, "OBS-00077": 1357, "OBS-00080": 1473, "OBS-00092": 1636, "OBS-00095": 1651}),
    "VIS-POS-TRANSACTIONS": ({"OBS-00052": 8015, "OBS-00064": 27187, "OBS-00081": 24026},
                             {"OBS-00052": 8015, "OBS-00064": 27187, "OBS-00081": 24026, "OBS-00093": 36201, "OBS-00096": 27504}),
    "VIS-POS-VALUE": ({"OBS-00053": 320, "OBS-00082": 1262},
                      {"OBS-00053": 320, "OBS-00082": 1262, "OBS-00094": 1579, "OBS-00097": 1045}),
}
OLD_RAT = "Panel 2 of the POS small multiple. The path is not steady (July 2025 high), which endpoint framing hid."
NEW_RAT = "Panel 2 of the POS small multiple. The path is not steady (May 2026 high), which endpoint framing hid."
STEP_SUBS = [("UI-VIS-CHAIN-IMPLEMENTATION", "the POS terminal stock (OBS-00080)", "the POS terminal stock (OBS-00095, June 2026)"),
             ("UI-VIS-CHAIN-OPERATION", "POS transactions (OBS-00081)", "POS transactions (OBS-00096, June 2026)")]


def one(d, vid):
    c = [v for v in d["visuals"] if v.get("visual_id") == vid and "contract" in v]
    if len(c) != 1:
        raise SystemExit(f"{vid} contract found {len(c)} times")
    return c[0]


def main():
    stage = sys.argv[1]
    os.makedirs(stage, exist_ok=True)
    with open(os.path.join(ROOT, REL), encoding="utf-8") as fh:
        d = json.load(fh, object_pairs_hook=OrderedDict)
    for vid, (old, new) in PINS.items():
        ser = one(d, vid)["contract"]["series"][0]
        if ser["expected_x"] != OLD_X or dict(ser["must_equal"]) != old:
            raise SystemExit(f"{vid}: expected_x or must_equal not as expected")
        ser["expected_x"] = list(NEW_X)
        ser["must_equal"] = OrderedDict(new)
    v = one(d, "VIS-POS-TRANSACTIONS")
    if v.get("rationale") != OLD_RAT:
        raise SystemExit(f"VIS-POS-TRANSACTIONS rationale not as expected: {v.get('rationale')!r}")
    v["rationale"] = NEW_RAT
    k = one(d, "RV-CWR-009")["contract"]
    act = [x for x in k["objects"] if x.get("id") == "pos_activity"]
    if len(act) != 1 or act[0]["rows"]["ids"] != ["OBS-00080", "OBS-00081"]:
        raise SystemExit("RV-CWR-009 pos_activity not as expected")
    act[0]["rows"]["ids"] = ["OBS-00095", "OBS-00096"]
    for key, old, new in STEP_SUBS:
        if k["step_mapping"][key].count(old) != 1:
            raise SystemExit(f"RV-CWR-009 step_mapping {key} not as expected")
        k["step_mapping"][key] = k["step_mapping"][key].replace(old, new)
    with open(os.path.join(stage, "visual_design_contract.json"), "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("staged:", os.path.join(stage, "visual_design_contract.json"))


if __name__ == "__main__":
    main()
