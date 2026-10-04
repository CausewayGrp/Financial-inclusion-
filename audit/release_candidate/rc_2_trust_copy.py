# -*- coding: utf-8 -*-
"""Release-candidate transaction RC-2 — trust copy (audit/release_candidate/INSTRUCTIONS.md, Part A, G2 items 9, 10, 13, 14, 15).

  python3 rc_2_trust_copy.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

  9  /about/ §6: the owner-approved funding and relationships paragraph (audit/OWNER_DECISIONS_2026-10-02.md, OWN-01),
     directly after the paragraph that begins "CauseWay’s role:", EN and AR.
  10 /corrections/ §3 "How history works": the edition statement (cut-off 26 September 2026 = audit/FINAL_CURRENTNESS_CUTOFF.md
     and 04 UI-CONTENT-VERSION, which is not changed).
  13 YSC-012 linked to SRC-CBY-UNLICENSED-EWALLET-2024-001 and SRC-CBY-DEC-23-2024-001 (the two 26 June 2024 instruments).
     The chronology_events count follows its definition ("Dated events in the system chronology") through the generator's
     counting rule (public_inventory_contract.json, rule count_where_not_in, installed with --install): 23, the analytical rule
     row YSC-020 excluded. The /data/ line keeps its label-value form.
  14 Stale counts in Master sheets 00 and 37 set to the derived values (public_inventory.json where it holds the key; the
     projection's record count otherwise), Expected and Actual alike.
  15 Publisher name: no governed text prints an Arabic transliteration of CauseWay (sweep recorded in the ledger); no write.
"""
import json, os, re, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rc_lib import Session, Table, TxError, formula_of, set_formula_cache  # noqa: E402

ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

I9_EN_ANCHOR = "CauseWay’s role: CauseWay develops and maintains this resource."
I9_EN = ("Funding. CauseWay funded the development of this edition entirely from its own resources. No donor, regulator, source "
         "institution or external commissioning party funded it. This resource is not a deliverable of any contract or partnership "
         "with the institutions whose data it presents.")
I9_AR_ANCHOR = "دور CauseWay: تطوّر CauseWay هذا المورد وتتولى إدارته."
I9_AR = ("التمويل: موّلت CauseWay تطوير هذا الإصدار بالكامل من مواردها الخاصة، ولم تموّله أي جهة مانحة أو تنظيمية، ولا أي جهة ناشرة "
         "لمصدر، ولا أي جهة خارجية كلّفت به. وليس هذا المورد ناتجًا عن أي عقد أو شراكة مع المؤسسات التي يعرض بياناتها.")

I10_EN = ("This edition reflects what its sources showed when they were checked, up to 26 September 2026. It is not a continuous "
          "monitoring service: between editions, the resource states what it held on the edition date.")
I10_AR = ("يعكس هذا الإصدار ما أظهرته مصادره عند مراجعتها حتى 26 سبتمبر 2026. وهو ليس خدمة رصد مستمر؛ فبين إصدار وآخر يعرض المورد "
          "ما كان لديه في تاريخ الإصدار.")

I13_FROM = "SRC-WB-YEM-FRAGMENTATION-2025-001"
I13_TO = "SRC-WB-YEM-FRAGMENTATION-2025-001 | SRC-CBY-UNLICENSED-EWALLET-2024-001 | SRC-CBY-DEC-23-2024-001"


def _x(v):
    """The editor reads a cell back as its XML text: a numeric cell's expected value is its text form."""
    return str(v) if isinstance(v, (int, float)) and not isinstance(v, bool) else v


def insert_after_paragraph(text, anchor, para, where):
    paras = text.split("\n\n")
    idx = [i for i, p in enumerate(paras) if p.startswith(anchor)]
    if len(idx) != 1:
        raise TxError(f"{where}: paragraph starting {anchor[:40]!r} found {len(idx)} times")
    if para in paras:
        raise TxError(f"{where}: paragraph already present")
    paras.insert(idx[0] + 1, para)
    return "\n\n".join(paras)


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    notes = OrderedDict()

    # ---- item 9 · /about/ §6 funding paragraph
    for lang, anchor, para in (("en", I9_EN_ANCHOR, I9_EN), ("ar", I9_AR_ANCHOR, I9_AR)):
        row = s.section_row("/about/", 6, lang)
        col = 5 if lang == "en" else 7
        cur = s.ed.get_value("03_PAGE_SECTIONS", row, col)
        s.set("RC-2:ITEM-09", "03_PAGE_SECTIONS", row, col, insert_after_paragraph(cur, anchor, para, f"/about/#s6.body_{lang}"), cur, f"/about/#s6.body_{lang}")
    notes["item_9"] = "DONE — OWN-01 paragraph inserted after the 'CauseWay’s role' paragraph of /about/ §6, EN and AR, verbatim as approved."

    # ---- item 10 · /corrections/ §3 "How history works" (one row carries both languages)
    g03 = s.grid("03_PAGE_SECTIONS")
    rows = [i for i, r in enumerate(g03, 1) if r and r[0] == "/corrections/" and r[3] == "How history works"]
    if len(rows) != 1:
        raise TxError(f"/corrections/ 'How history works' found {len(rows)} times")
    r = rows[0]
    for col, para in ((5, I10_EN), (7, I10_AR)):
        cur = s.ed.get_value("03_PAGE_SECTIONS", r, col)
        if para in cur:
            raise TxError("/corrections/ edition paragraph already present")
        s.set("RC-2:ITEM-10", "03_PAGE_SECTIONS", r, col, cur + "\n\n" + para, cur, f"/corrections/#s3.body_{'en' if col == 5 else 'ar'}")
    t04 = s.grid("04_NAV_UX")
    cv = [x for x in t04 if x and x[0] == "UI-CONTENT-VERSION"]
    if len(cv) != 1 or "26 September 2026" not in cv[0][1] or "26 سبتمبر 2026" not in cv[0][2]:
        raise TxError("UI-CONTENT-VERSION does not carry the 26 September 2026 edition date")
    notes["item_10"] = "DONE — appended to /corrections/ §3 in both languages; the date equals UI-CONTENT-VERSION (unchanged) and audit/FINAL_CURRENTNESS_CUTOFF.md."

    # ---- item 13 · YSC-012 sources
    t14 = Table(s, "14_SYSTEM_CHRONOLOGY")
    t14.set("RC-2:ITEM-13", "YSC-012", "source_ids", I13_TO, I13_FROM)
    t15 = Table(s, "15_SOURCE_LIBRARY")
    for sid, date in (("SRC-CBY-UNLICENSED-EWALLET-2024-001", "2024-06-26"), ("SRC-CBY-DEC-23-2024-001", "2024-06-26")):
        if sid not in t15.rows or t15.get(sid, "document_date") != date:
            raise TxError(f"{sid} is not the 26 June 2024 instrument the brief names")
    notes["item_13"] = ("DONE — YSC-012 source_ids now name the World Bank account and the two 26 June 2024 CBY-Aden instruments (both dated 2024-06-26 in "
                        "15_SOURCE_LIBRARY). The chronology_events count follows its definition through the generator's rule count_where_not_in "
                        "(event_class SYSTEM_INTERPRETATION excluded: YSC-020, 'Current analytical rule', no source) — 23 — in "
                        "scripts/projection/controlled_inputs/public_inventory_contract.json (installed), with the same rule in the validator's "
                        "independent recount (P1-G02) and scripts/rebind_authority.py. The /data/ inventory line keeps 'label: N'.")

    # ---- item 14 · stale counts in 00 and 37
    C = os.path.join(ROOT, "site-src", "content")

    def n(rel):
        d = json.load(open(os.path.join(C, rel), encoding="utf-8"))
        if isinstance(d, dict):   # a data projection: {"sheet", "rows"} with a title block and a header row before the observations
            rows = d["rows"]
            hdr = next(i for i, r in enumerate(rows) if r and r[0] == "observation_id")
            return sum(1 for r in rows[hdr + 1:] if r and r[0] not in (None, ""))
        return len(d)
    chron = json.load(open(os.path.join(C, "visuals/system_chronology.json"), encoding="utf-8"))
    derived = OrderedDict([
        ("Site pages", json.load(open(os.path.join(C, "page_specs.json"), encoding="utf-8"))["spec_count"]),
        ("Bilingual page sections", n("content/page_sections.json")),
        ("Questions", n("content/questions.json")),
        ("Evidence objects", n("evidence/evidence_objects.json")),
        ("Public claims", n("evidence/public_claims.json")),
        ("Readings", n("content/readings.json")),
        ("Measurement priorities", n("content/measurement_agenda.json")),
        ("Visual objects", n("visuals/visual_library.json")),
        ("System relationships", n("visuals/system_relationships.json")),
        ("Chronology events", sum(1 for e in chron if e.get("event_class") != "SYSTEM_INTERPRETATION")),
        ("Sources", n("sources/source_library.json")),
        ("Datasets", n("sources/master_dataset_catalog.json")),
        ("Indicators", n("sources/indicator_library.json")),
    ])
    def put(sheet, i, col, want, old, field):
        """A count cell that holds a COUNTA formula keeps it (only its cached result changes); a typed count is rewritten."""
        f = formula_of(s, sheet, i, col)
        if f is None:
            s.set("RC-2:ITEM-14", sheet, i, col, want, _x(old), field)
        elif f.startswith("COUNTA("):
            set_formula_cache(s, "RC-2:ITEM-14", sheet, i, col, want, _x(old), f, field)
        else:
            raise TxError(f"{sheet} r{i}c{col}: unexpected formula ={f}")

    g00 = s.grid("00_MASTER")
    seen = set()
    for i, r in enumerate(g00, 1):
        if r and r[0] in derived and isinstance(r[1], int) and isinstance(r[2], int):
            want = derived[r[0]]
            if r[1] != want:
                put("00_MASTER", i, 2, want, r[1], f"00 {r[0]} actual")
            if r[2] != want:
                put("00_MASTER", i, 3, want, r[2], f"00 {r[0]} expected")
            seen.add(r[0])
    if seen != set(derived):
        raise TxError(f"00 count rows not found: {set(derived) - seen}")
    # the snapshot panel's chronology phrase
    for i, r in enumerate(g00, 1):
        for j, c in enumerate(r, 1):
            if isinstance(c, str) and "24-event macro-financial" in c:
                s.replace("RC-2:ITEM-14", "00_MASTER", i, j, "24-event macro-financial", f"{derived['Chronology events']}-event macro-financial", "00 SYSTEM panel")
    map37 = OrderedDict([
        ("All site pages", derived["Site pages"]), ("Bilingual page sections", derived["Bilingual page sections"]),
        ("Question entry system", derived["Questions"]), ("Public evidence objects", derived["Evidence objects"]),
        ("Public claims", derived["Public claims"]), ("Readings", derived["Readings"]), ("Measurement agenda", derived["Measurement priorities"]),
        ("Visualization objects", derived["Visual objects"]), ("System relationships", derived["System relationships"]),
        ("Chronology events", derived["Chronology events"]), ("Source records", derived["Sources"]), ("Dataset catalogue", derived["Datasets"]),
        ("Indicator library", derived["Indicators"]), ("CBY monetary observations", n("data/cby_monetary.json")),
        ("Payment observations", n("data/payments_data.json")), ("Firm finance observations", n("data/firm_finance.json")),
        ("Remittance observations", n("data/remittances.json")),
    ])
    g37 = s.grid("37_READINESS_CHECKLIST")
    seen37 = set()
    for i, r in enumerate(g37, 1):
        if i > 4 and r and r[1] in map37:
            want = map37[r[1]]
            if r[2] != want:
                put("37_READINESS_CHECKLIST", i, 3, want, r[2], f"37 {r[1]} expected")
            if r[3] != want:
                put("37_READINESS_CHECKLIST", i, 4, want, r[3], f"37 {r[1]} actual")
            seen37.add(r[1])
    if seen37 != set(map37):
        raise TxError(f"37 rows not found: {set(map37) - seen37}")
    notes["item_14"] = OrderedDict([("rule", "Expected and Actual set to the derived value: public_inventory.json where it holds the key, otherwise the "
                                              "record count of the projection generated from the named sheet (data projections count records, not header rows). "
                                              "A cell that holds a COUNTA formula keeps its formula; only its cached result is updated (the formula "
                                              "computes the same value on recalculation), so the 37 READY/REVIEW status formulas still compare a live count."),
                                    ("values_00", derived), ("values_37", map37)])

    # ---- item 15 · publisher name sweep (no write)
    pat = re.compile(r"كوزواي|كاوزواي|كوز واي|كاوز واي|كوزوي|كاوزوي")
    hits = []
    from projection.master_reader import Workbook  # noqa: E402  (ptc_lib put scripts/ on sys.path)
    wb = Workbook(src)
    for name in wb.sheet_names:
        for i, r in enumerate(wb.grid(name), 1):
            for j, c in enumerate(r, 1):
                if isinstance(c, str) and pat.search(c):
                    hits.append(f"{name}!r{i}c{j}")
    if hits:
        raise TxError(f"item 15: Arabic transliteration of CauseWay found in {hits[:5]}")
    notes["item_15"] = ("CONFIRMED — no Master cell prints an Arabic transliteration of CauseWay (patterns كوزواي, كاوزواي, كوز واي, كاوز واي, كوزوي, "
                        "كاوزوي; all sheets). The Arabic edition prints 'CauseWay' in Latin script (isolated by <bdi> in the header brand, frames and social cards; in body text a single Latin word between Arabic words, with no adjacent digits or punctuation, needs no isolation to render in order). The only "
                        "occurrence in the repository is a historical reader report (design/evidence/d7/cold_read/lens-arabic-closure.md), not governed text.")

    notes["independent_review"] = OrderedDict([
        ("reviewer", "independent subagent that did not write the transaction (senior Arab economic editor and senior institutional English editor lenses)"),
        ("verdict", "ACCEPTABLE — no blocking finding; items 9 and 10 verbatim and in place in both languages; item 13 and 14 values match the projections"),
        ("applied", ["SHOULD FIX 1: the first run replaced seven COUNTA formulas (00 B14, B17, B18; 37 D5, D8, D9, D21) with typed numbers and "
                     "recorded their stale cached result as the old value; the transaction now keeps each formula and updates only its cached result "
                     "(rc_lib.set_formula_cache, recorded per cell with formula_kept)",
                     "SHOULD FIX 2: the item 15 note no longer says body text isolates 'CauseWay' (only the header brand, frames and social cards do)"]),
        ("for_the_owner", ["OPTIONAL: item 9 EN opens 'Funding.' where the section's other lead-ins use a colon (AR «التمويل:»); owner wording, not changed",
                           "OPTIONAL: item 9 AR «ليس هذا المورد ناتجًا عن» is slightly broader than 'is not a deliverable of'; equivalent in meaning; owner wording, not changed"]),
        ("deferred", ["YSC-012 source_scope (Master-only, not printed) still describes the World Bank account alone; refresh with the Part B chronology work"]),
    ])

    rep = s.save(out, ledger, OrderedDict([("transaction", "RC-2"), ("summary", "Release-candidate trust copy: items 9, 10, 13, 14, 15 of audit/release_candidate/INSTRUCTIONS.md Part A G2"),
                                           ("items", notes)]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
