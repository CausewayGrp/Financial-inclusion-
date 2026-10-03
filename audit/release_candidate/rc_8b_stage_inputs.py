# -*- coding: utf-8 -*-
"""RC-8b staged controlled input: scripts/projection/controlled_inputs/visual_design_contract.json, installed by
run_stage.py --install. The provider-observability contract follows the roster file linked on 3 October 2026 (created
22 September 2026): the pins move to 100 / 231 / 111, and the two label-map keys and the transformation text that quote
the governed state strings follow the Master (442 rows). Text replacements must each occur exactly once.

  python3 rc_8b_stage_inputs.py <stage_dir>
"""
import json, os, sys
from collections import OrderedDict

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
REL = "scripts/projection/controlled_inputs/visual_design_contract.json"
PINS_OLD = {"CBY-ROSTER-2026-COMP": 98, "CBY-ROSTER-2026-EST": 225, "CBY-ROSTER-2026-AGT": 106}
PINS_NEW = {"CBY-ROSTER-2026-COMP": 100, "CBY-ROSTER-2026-EST": 231, "CBY-ROSTER-2026-AGT": 111}
TEXT_SUBS = [
    ('"SOURCE_LISTED_ROWS__98_COMPANIES__225_ESTABLISHMENTS__106_REMITTANCE_AGENTS"',
     '"SOURCE_LISTED_ROWS__100_COMPANIES__231_ESTABLISHMENTS__111_REMITTANCE_AGENTS"'),
    ('"429 is the arithmetic sum of source-listed rows', '"442 is the arithmetic sum of source-listed rows'),
    ("the 429 roster total is not shown as a number of providers", "the 442 roster total is not shown as a number of providers"),
]


def main():
    stage = sys.argv[1]
    os.makedirs(stage, exist_ok=True)
    with open(os.path.join(ROOT, REL), encoding="utf-8") as fh:
        d = json.load(fh, object_pairs_hook=OrderedDict)
    hits = []

    def walk(o):
        if isinstance(o, dict):
            if isinstance(o.get("must_equal"), dict) and dict(o["must_equal"]) == PINS_OLD:
                o["must_equal"] = OrderedDict(PINS_NEW)
                hits.append(1)
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(d)
    if len(hits) != 1:
        raise SystemExit(f"roster pins found {len(hits)} times")
    text = json.dumps(d, ensure_ascii=False, indent=1)
    for old, new in TEXT_SUBS:
        if text.count(old) != 1:
            raise SystemExit(f"{old[:60]!r} occurs {text.count(old)} times")
        text = text.replace(old, new)
    with open(os.path.join(stage, "visual_design_contract.json"), "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    print("staged:", os.path.join(stage, "visual_design_contract.json"))


if __name__ == "__main__":
    main()
