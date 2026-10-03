# -*- coding: utf-8 -*-
"""RC-7 staged controlled input (Part A item 6, Path A): scripts/projection/controlled_inputs/visual_design_contract.json,
installed by run_stage.py --install. VIS-FIRM-CONSTRAINTS binds all sixteen rows of the source's Table 8 (FFO-2022-CH-01..16,
checked against the original on 3 October 2026), each with its governed label, and no longer carries the partial-list frame
note. One-space JSON indent kept; every change states what it expects to find.

  python3 rc_7_stage_inputs.py <stage_dir>
"""
import json, os, sys
from collections import OrderedDict

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
REL = "scripts/projection/controlled_inputs/visual_design_contract.json"
NEW_IDS = [f"FFO-2022-CH-{n:02d}" for n in range(9, 17)]
NEW_MAP = OrderedDict([
    ("Business challenge: Labor regulations", "UI-VIS-CAT-FIRM-CH-LABOUR"),
    ("Business challenge: Customs/trade regulation", "UI-VIS-CAT-FIRM-CH-CUSTOMS"),
    ("Business challenge: Corruption", "UI-VIS-CAT-FIRM-CH-CORRUPTION"),
    ("Business challenge: Land", "UI-VIS-CAT-FIRM-CH-LAND"),
    ("Business challenge: Business licensing", "UI-VIS-CAT-FIRM-CH-LICENSING"),
    ("Business challenge: Inadequately educated workforce", "UI-VIS-CAT-FIRM-CH-WORKFORCE"),
    ("Business challenge: Courts", "UI-VIS-CAT-FIRM-CH-COURTS"),
    ("Business challenge: Crime/theft/disorder", "UI-VIS-CAT-FIRM-CH-CRIME"),
])
OLD_TRANSFORMATION = ("None. The eight items named in the governed contract are drawn; the other eight governed items "
                      "(FFO-2022-CH-09..16) appear in the table fallback.")
NEW_TRANSFORMATION = ("None. All sixteen items of the source's Table 8 (Annex III, p. 146) are drawn and listed "
                      "(FFO-2022-CH-01..16), each checked against the original on 3 October 2026 (RC-7).")


def main():
    stage = sys.argv[1]
    os.makedirs(stage, exist_ok=True)
    with open(os.path.join(ROOT, REL), encoding="utf-8") as fh:
        d = json.load(fh, object_pairs_hook=OrderedDict)
    c = [v for v in d["visuals"] if v.get("visual_id") == "VIS-FIRM-CONSTRAINTS" and "contract" in v]
    if len(c) != 1:
        raise SystemExit(f"VIS-FIRM-CONSTRAINTS contract found {len(c)} times")
    k = c[0]["contract"]
    ids = k["series"][0]["rows"]["ids"]
    if ids != [f"FFO-2022-CH-{n:02d}" for n in range(1, 9)]:
        raise SystemExit(f"bound rows not as expected: {ids}")
    ids.extend(NEW_IDS)
    if k.get("transformation") != OLD_TRANSFORMATION:
        raise SystemExit(f"transformation not as expected: {k.get('transformation')!r}")
    k["transformation"] = NEW_TRANSFORMATION
    if k.get("frame_labels") != ["UI-VIS-NOTE-FIRM-CONSTRAINTS-PARTIAL"]:
        raise SystemExit(f"frame_labels not as expected: {k.get('frame_labels')!r}")
    del k["frame_labels"]
    ns = d["display_labels"]["namespaces"]["firm_challenge"]
    if len(ns) != 8 or any(key in ns for key in NEW_MAP):
        raise SystemExit(f"firm_challenge labels not as expected: {list(ns)}")
    ns.update(NEW_MAP)
    with open(os.path.join(stage, "visual_design_contract.json"), "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("staged:", os.path.join(stage, "visual_design_contract.json"))


if __name__ == "__main__":
    main()
