# -*- coding: utf-8 -*-
"""RC-12 staged controlled input: scripts/projection/controlled_inputs/visual_design_contract.json, installed by
run_stage.py --install. Part B B12: the two TABLE_TEXT_FIRST contracts whose rationale describes a table bind it from
governed rows (`table`, resolved and guarded by scripts/projection/derived.py `_vdc_text_table`). One-space JSON indent
kept; every change states what it expects to find.

  python3 rc_12_stage_inputs.py <stage_dir>
"""
import json, os, sys
from collections import OrderedDict

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
REL = "scripts/projection/controlled_inputs/visual_design_contract.json"
FM = "fmiip.FMIIP-RF-004."
TABLES = OrderedDict([
    ("VIS-TARGET-RESULT-STATE", OrderedDict([
        ("form", "Three rows (state, date, value): the project's baseline, its target, and the result, which the evidence base "
                 "does not hold. No dated axis, no percentage of the target, no comparison with administrative counts."),
        ("objects", [OrderedDict([
            ("id", "fmiip"),
            ("rows", OrderedDict([("file", "data/reforms_regulation.json"), ("header_key", "metric_id"), ("ids", ["FMIIP-RF-004"])])),
            ("fields", OrderedDict([("baseline_period", "baseline_period"), ("baseline_value", "baseline_value"),
                                    ("target_period", "target_period"), ("target_value", "target_value"), ("source", "source_id")])),
            ("month_year_fields", ["baseline_period", "target_period"]),
            ("must_equal", OrderedDict([("FMIIP-RF-004", OrderedDict([("baseline_value", 817), ("target_value", 1021)]))])),
        ])]),
        ("head", ["UI-VIS-TH-ITEM", "UI-VIS-TH-DATE", "UI-VIS-UNIT-PROJECT-ACCESS-POINTS"]),
        ("caption", ["UI-VIS-STATE-PROGRAMME"]),
        ("rows", [
            OrderedDict([("head", "UI-VIS-BASELINE"), ("cells", [OrderedDict([("ref", FM + "baseline_period_iso"), ("as", "month")]),
                                                                 OrderedDict([("ref", FM + "baseline_value")])])]),
            OrderedDict([("head", "UI-VIS-TARGET"), ("cells", [OrderedDict([("ref", FM + "target_period_iso"), ("as", "month")]),
                                                               OrderedDict([("ref", FM + "target_value")])])]),
            # the World Bank's ISR (seq. 2) prints a placeholder "0" as the current value: not bound, never a zero here
            OrderedDict([("head", "UI-VIS-RESULT"), ("cells", [OrderedDict([("ui", "UI-VIS-RESULT-NOT-HELD"), ("span", 2)])])]),
        ]),
    ])),
    ("VIS-FIRM-FINANCE-PATH", OrderedDict([
        ("form", "Item and number under each base (a row group opened by \"Out of\" and the base), in the source's order. A "
                 "governed marker separates the establishments with a line of credit from the loan-source responses: the "
                 "Master does not establish that the 18 come from the 31, so nothing is drawn or read as a funnel."),
        ("objects", [OrderedDict([
            ("id", "firm"),
            ("rows", OrderedDict([("file", "data/firm_finance.json"), ("header_key", "observation_id"),
                                  ("ids", ["FFO-2022-004", "FFO-2022-LS-01", "FFO-2022-LS-02", "FFO-2022-LS-03", "FFO-2022-LS-04"])])),
            ("fields", OrderedDict([("metric_label", "metric_label"), ("breakdown_value", "breakdown_value"), ("value", "value"),
                                    ("denominator_n", "denominator_n"), ("source", "source_id")])),
            ("must_equal", OrderedDict([
                ("FFO-2022-004", OrderedDict([("value", 31), ("denominator_n", 328)])),
                ("FFO-2022-LS-01", OrderedDict([("value", 10), ("denominator_n", 18)])),
                ("FFO-2022-LS-02", OrderedDict([("value", 1), ("denominator_n", 18)])),
                ("FFO-2022-LS-03", OrderedDict([("value", 5), ("denominator_n", 18)])),
                ("FFO-2022-LS-04", OrderedDict([("value", 2), ("denominator_n", 18)])),
            ])),
        ])]),
        # two columns, each base opening its row group (the design's row-group pattern), so the table fits 256 px
        ("head", ["UI-VIS-TH-ITEM", "UI-VIS-UNIT-COUNT"]),
        ("caption", []),
        ("rows", [OrderedDict([("group", OrderedDict([("lead", "UI-VIS-TH-BASE"), ("ref", "firm.FFO-2022-004.denominator_n"),
                                                      ("unit", "UI-VIS-UNIT-FIRMS-SURVEYED")]))]),
                  OrderedDict([("head", OrderedDict([("ref", "firm.FFO-2022-004.metric_label"), ("ns", "firm_finance")])),
                               ("cells", [OrderedDict([("ref", "firm.FFO-2022-004.value")])])]),
                  OrderedDict([("marker", "UI-VIS-NOTE-FIRM-LOAN-SUBSET")]),
                  # all four responses share the base of 18 (each row's must_equal holds denominator_n = 18)
                  OrderedDict([("group", OrderedDict([("lead", "UI-VIS-TH-BASE"), ("ref", "firm.FFO-2022-LS-01.denominator_n"),
                                                      ("unit", "UI-VIS-UNIT-VALID-RESPONSES")]))])]
                 + [OrderedDict([("head", OrderedDict([("ref", f"firm.FFO-2022-LS-0{i}.breakdown_value"), ("ns", "firm_finance")])),
                                 ("cells", [OrderedDict([("ref", f"firm.FFO-2022-LS-0{i}.value")])])])
                    for i in range(1, 5)]),
    ])),
])


def main():
    stage = sys.argv[1]
    os.makedirs(stage, exist_ok=True)
    with open(os.path.join(ROOT, REL), encoding="utf-8") as fh:
        d = json.load(fh, object_pairs_hook=OrderedDict)
    for vid, t in TABLES.items():
        hits = [v for v in d["visuals"] if v.get("visual_id") == vid]
        if len(hits) != 1 or hits[0].get("tier") != "TABLE_TEXT_FIRST" or "table" in hits[0] or "contract" in hits[0]:
            raise SystemExit(f"{vid} not as expected")
        hits[0]["table"] = t
    with open(os.path.join(stage, "visual_design_contract.json"), "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("staged:", os.path.join(stage, "visual_design_contract.json"))


if __name__ == "__main__":
    main()
