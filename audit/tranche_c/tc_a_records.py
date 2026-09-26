# -*- coding: utf-8 -*-
"""Tranche C transaction TC-A — Evidence Record and visual text, and the Findex comparators it cites.

  python3 tc_a_records.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Inputs: audit/tranche_c/inputs/TC-A_records.json (adjudicated 06 / 11 replacement text; each edit applies only if the
Master still holds its 'old' value).

Also, Master-first, because the new VIS-FINDEX-GAPS text cites them (EVM-24, JRN-05, Lead decision):
  * 25_FINDEX_BASELINE gains three World Bank rows for data year 2022, verified on 26 Sep 2026 against the World Bank API:
    FX.OWN.TOTL.SO.ZS 19.5270… -> 19.53; FX.OWN.TOTL.YG.ZS 5.00996… -> 5.01; FX.OWN.TOTL.OL.ZS 16.1081… -> 16.11
    (two decimals, the precision of the existing rows);
  * 27_FINDEX_SUBGROUPS FSG-0002 (age) and FSG-0003 (education) become same-wave gap ready, with the published pair named;
  * 04 gains the chart labels for the three new groups and two units.
Guard (one owner, A == prohibited inference): for every visual record present in both 06 and 11, the 06 title equals the
11 title and the first part of the 06 limitations equals the 11 prohibited inference, in both languages.
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from tc_lib import Session, Table, TxError, insert_ui_rows, norm  # noqa: E402

SHEETS = {"06": "06_EVIDENCE_OBJECTS", "11": "11_VISUAL_LIBRARY"}
WB_ROWS = [
    ("WB-FINDEX-OBS-2022-007", "FX.OWN.TOTL.SO.ZS", "Account ownership", "secondary education or more", "2022", 19.53,
     "percent of population ages 15+", "World Bank Global Findex",
     "https://data.worldbank.org/indicator/FX.OWN.TOTL.SO.ZS?locations=YE", "PUBLIC_PRIMARY_AGGREGATE",
     "Education category definition must be kept exact. Verified 26 Sep 2026 against the World Bank API (19.5270…)."),
    ("WB-FINDEX-OBS-2022-008", "FX.OWN.TOTL.YG.ZS", "Account ownership", "ages 15-24", "2022", 5.01,
     "percent of population ages 15-24", "World Bank Global Findex",
     "https://data.worldbank.org/indicator/FX.OWN.TOTL.YG.ZS?locations=YE", "PUBLIC_PRIMARY_AGGREGATE",
     "Young adults, ages 15-24. Verified 26 Sep 2026 against the World Bank API (5.00996…)."),
    ("WB-FINDEX-OBS-2022-009", "FX.OWN.TOTL.OL.ZS", "Account ownership", "ages 25+", "2022", 16.11,
     "percent of population ages 25+", "World Bank Global Findex",
     "https://data.worldbank.org/indicator/FX.OWN.TOTL.OL.ZS?locations=YE", "PUBLIC_PRIMARY_AGGREGATE",
     "Older adults, ages 25 and over. Verified 26 Sep 2026 against the World Bank API (16.1081…)."),
]
UI_ROWS = [
    ("UI-VIS-CAT-FINDEX-SECONDARY-EDU", "Adults with secondary education or more", "البالغون الحاصلون على تعليم ثانوي أو أعلى",
     "Tranche C TC-A. Chart label: findex_group value 'secondary education or more'."),
    ("UI-VIS-CAT-FINDEX-AGE-15-24", "Young adults (ages 15–24)", "الشباب (15–24 سنة)",
     "Tranche C TC-A. Chart label: findex_group value 'ages 15-24'."),
    ("UI-VIS-CAT-FINDEX-AGE-25-PLUS", "Adults aged 25 and over", "البالغون بعمر 25 سنة فأكثر",
     "Tranche C TC-A. Chart label: findex_group value 'ages 25+'."),
    ("UI-VIS-UNIT-PCT-AGES-15-24", "% of young adults (ages 15–24)", "% من الشباب (15–24 سنة)",
     "Tranche C TC-A. Chart label: unit value 'percent of population ages 15-24'."),
    ("UI-VIS-UNIT-PCT-AGES-25-PLUS", "% of adults aged 25 and over", "% من البالغين بعمر 25 سنة فأكثر",
     "Tranche C TC-A. Chart label: unit value 'percent of population ages 25+'."),
]
FSG = {
    "FSG-0002": {"current_state": ("HOLD_FOR_VALUE_CONTROL_OR_MICRODATA", "PUBLIC_SAME_WAVE_GAP_READY"),
                 "published_anchor_state": ("OFFICIAL_WORLD_BANK_SERIES_EXISTS__SYSTEM_VALUE_NOT_CONTROLLED",
                                            "PUBLISHED_AGES_15_24_AND_25_PLUS_ANCHORS_CONTROLLED"),
                 "public_behavior": ("No age gap until weighted values or official aggregate values are controlled.",
                                     "May display ages 15-24 and 25+ and the percentage-point gap (World Bank published aggregates, same wave).")},
    "FSG-0003": {"current_state": ("PARTIAL_HOLD_FOR_COMPLETE_PAIR", "PUBLIC_SAME_WAVE_GAP_READY"),
                 "published_anchor_state": ("PARTIAL__PRIMARY_OR_LESS_VALUE_CONTROLLED__OTHER_EDU_VALUE_NOT_IN_SYSTEM",
                                            "PUBLISHED_PRIMARY_OR_LESS_AND_SECONDARY_OR_MORE_ANCHORS_CONTROLLED"),
                 "public_behavior": ("May show controlled primary-or-less value alone; no education gap until pair is controlled.",
                                     "May display primary education or less and secondary education or more and the percentage-point gap (World Bank published aggregates, same wave).")},
}


def split_a(lim):
    return norm(lim).split(" | ")[0].strip()


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    data = json.load(open(os.path.join(HERE, "inputs", "TC-A_records.json"), encoding="utf-8"))
    tables = {k: Table(s, v) for k, v in SHEETS.items()}
    n = 0
    for e in data["edits"]:
        t = tables[e["sheet"]]
        field = e["field"]
        if field not in t.head:
            raise TxError(f"{e['sheet']} has no column {field}")
        n += t.set("TC-A:" + e["batch"], e["id"], field, e["new"], e["old"])
    # 03: Reading prose that repeats a record statement changed above (exact-substring replacement)
    for sec in data.get("sections", []):
        s.replace_section("TC-A:" + sec["why"][:40], sec["route"], sec["order"], sec["lang"], sec["field"], sec["old_sub"], sec["new_sub"])

    # 25: three verified World Bank comparators after WB-FINDEX-OBS-2022-006
    t25 = Table(s, "25_FINDEX_BASELINE")
    if any(r[0] in t25.rows for r in WB_ROWS) or "WB-FINDEX-OBS-2022-006" not in t25.rows:
        raise TxError("25: unexpected rows")
    at = t25.rows["WB-FINDEX-OBS-2022-006"] + 1
    s.ed.insert_rows("25_FINDEX_BASELINE", at, [{i + 1: v for i, v in enumerate(r)} for r in WB_ROWS])
    for r in WB_ROWS:
        s.ledger.append({"finding": "TC-A:EVM-24", "sheet": "25_FINDEX_BASELINE", "row": None, "col": None, "field": r[0],
                         "old": None, "new": f"{r[1]} {r[3]} {r[4]} = {r[5]}"})
    # 27: FSG states
    t27 = Table(s, "27_FINDEX_SUBGROUPS")
    for key, fields in FSG.items():
        for f, (old, new) in fields.items():
            t27.set("TC-A:EVM-24", key, f, new, old)
    # 04: labels
    insert_ui_rows(s, "TC-A:EVM-24", UI_ROWS)

    # guard: 06 == 11 for shared visual records
    t06, t11 = Table(s, SHEETS["06"]), Table(s, SHEETS["11"])
    bad = []
    for vid in t11.rows:
        if vid not in t06.rows:
            continue
        for lang in ("en", "ar"):
            if norm(t06.get(vid, "title_" + lang)) != norm(t11.get(vid, "title_" + lang)):
                bad.append(f"{vid} title_{lang}")
            if split_a(t06.get(vid, "limitations_" + lang)) != norm(t11.get(vid, "prohibited_inference_" + lang)):
                bad.append(f"{vid} A/PI {lang}")
    if bad:
        raise TxError("06/11 guard: " + "; ".join(bad))

    rep = s.save(out, ledger, {"transaction": "TC-A", "input": "audit/tranche_c/inputs/TC-A_records.json",
                              "text_cells_changed": n,
                              "summary": "06/11 record and visual text (1 owner, declarative limits, currentness answers, "
                                         "RULES §C terminology); 25 +3 World Bank rows; 27 FSG-0002/0003; 04 +5 labels"})
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
