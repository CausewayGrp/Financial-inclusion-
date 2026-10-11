# -*- coding: utf-8 -*-
"""Close-out transaction CLOSE-6C (Stage A addendum, item 4): Reading CWR-012 "How money reaches households", with the
two Cash Consortium of Yemen findings it uses held as Evidence Records. English and Arabic change together.

  python3 close_6c.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

- The draft is audit/close_out/drafts/CWR-012_draft.json (W3e, RD8), kept for the owner when it was dropped for want of a
  native Arabic review and of held CCY findings. Both conditions are now met: R5 read the two CCY studies in full
  (audit/close_out/addendum/R5_ccy_isp_sam.md), and the review pair (red-team with exchange-company and central-bank
  readers; Arabic economic editor) is in audit/close_out/addendum/.
- CCY-ISP-2024 holds what "The Unseen Assistance" (June 2024) reports on informal loans and gifts in the cash income of
  cash-assistance households in three areas the study calls sub-districts, and the changes in giving and receiving they reported.
  CCY-SAM-2024 holds the pilot study's estimated multiplier for selected villages of Ad-Dali and Ja'ar (activity,
  transfer included; not income) and the income sources of the assessed households, with the hawala caveat. Neither study
  records how money moves between households: the Reading says so, and prints none of their values.
- The draft's day-precise Findex fieldwork dates follow CR-21 (month precision). The humanitarian-cash alternative now
  states what the two records show and what they do not.
- The review pair's changes are in close_6c_text.py as exact edits, each matched once. The red-team (exchange-company,
  central-bank and methods readers) held the first text on three blockers: B1, licensed transfers called "informal";
  B2, "mainly" where the only channel shares are 31.1% and 2.0% of 2014 recipients; B3, CBY-Aden's balance of payments
  called "the economy as a whole". The hypothesis is now comparative ("more through exchange companies and other
  money-transfer providers than through accounts"). The June 2024 domestic-transfer rule is stated and bound
  (VIS-PAYMENT-RAILS, SRC-CBY-DEC-23-2024-001), and the roster's CBY-Aden scope is stated. Owner questions 1 (F2 stays:
  /remittances/ carries CWR-001 and CWR-012) and 3 (CWR-002 -> MA-008 kept) stand as accepted.
"""
import json, os, sys, unicodedata
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from close_lib import Session, Table, TxError, refresh_self_counts  # noqa: E402
from rc_lib import S04  # noqa: E402
from close_6c_records import NEW_RECORDS  # noqa: E402
from close_6c_text import SET, EDITS, GONE, HUM_EN, HUM_AR, ADD_CLAIMS, ADD_SOURCES, ALIAS001  # noqa: E402

F = "CLOSE-6C"
TODAY = "2026-10-11"
DRAFT = os.path.join(HERE, "drafts", "CWR-012_draft.json")
RID = "CWR-012"
NEW_IDS = [r["object_id"] for r in NEW_RECORDS]


def nfc(o):
    if isinstance(o, str):
        return unicodedata.normalize("NFC", o)
    if isinstance(o, (list, tuple)):
        return type(o)(nfc(x) for x in o)
    if isinstance(o, dict):
        return OrderedDict((k, nfc(v)) for k, v in o.items())
    return o


CR21 = [("from 7 November 2022 to 9 January 2023", "from November 2022 to January 2023"),
        ("من 7 نوفمبر 2022 إلى 9 يناير 2023", "من نوفمبر 2022 إلى يناير 2023"),
        ("survey fieldwork ended on 9 January 2023", "survey fieldwork ended in January 2023"),
        ("انتهى العمل الميداني للمسح في 9 يناير 2023", "انتهى العمل الميداني للمسح في يناير 2023"),
        ("7 November 2022 – 9 January 2023", "November 2022 – January 2023"),
        ("7 نوفمبر 2022 – 9 يناير 2023", "نوفمبر 2022 – يناير 2023")]

HUM_OLD = ("The Cash Consortium of Yemen has studied informal social protection (“The Unseen Assistance”) and the multiplier "
           "effect of cash assistance in Ad’ Dhali and Ja’ar; their findings are not yet held as records here, so this Reading "
           "prints none of them.",
           "وقد درس تحالف النقد في اليمن (Cash Consortium of Yemen) الحماية الاجتماعية غير الرسمية («المساعدة غير المرئية») "
           "والأثر المضاعف للمساعدات النقدية في عزلتَي الضالع وجعار؛ ولم تُدرج نتائج الدراستين بعدُ سجلاتٍ في قاعدة الأدلة هذه، "
           "لذلك لا تعرض هذه القراءة أيًّا منها.")


def fix(text):
    if not isinstance(text, str):
        return text
    for a, b in CR21:
        text = text.replace(a, b)
    return text


def assemble():
    """The Reading as it will be written: the draft, CR-21, the CCY sentence and the review pair's edits."""
    d = json.load(open(DRAFT, encoding="utf-8"))
    rd = OrderedDict(d["reading"])
    sections = [OrderedDict(x) for x in d["sections"]]

    # ---------------------------------------------------------------- the draft, brought up to date
    sm = OrderedDict(d["site_map"])
    for k in ("thesis_en", "thesis_ar", "evidence_period_en", "evidence_period_ar", "prohibited_inference_en", "prohibited_inference_ar"):
        rd[k] = fix(rd[k])
    for sec in sections:
        for f in ("heading_en", "body_en", "heading_ar", "body_ar"):
            sec[f] = fix(sec.get(f))
    s5 = next(x for x in sections if x["section_order"] == 5)
    for f, old, new in (("body_en", HUM_OLD[0], HUM_EN), ("body_ar", HUM_OLD[1], HUM_AR)):
        if s5[f].count(old) != 1:
            raise TxError(f"{F}: CWR-012 s5 {f} does not hold the humanitarian-cash sentence once")
        s5[f] = s5[f].replace(old, new)
    # the review pair's changes (close_6c_text.py): whole fields, then exact edits
    target = {"reading": rd, "site_map": sm}
    target.update({x["section_order"]: x for x in sections})
    for (tg, f), new in SET.items():
        target[tg][f] = new
    for tg, f, old, new in EDITS:
        if str(target[tg].get(f) or "").count(old) != 1:
            raise TxError(f"{F}: CWR-012 {tg}.{f} does not hold the edited text once: {old[:60]}")
        target[tg][f] = target[tg][f].replace(old, new)
    for tg, obj in target.items():
        for f, v in obj.items():
            if isinstance(v, str):
                left = [g for g in GONE if g in v]
                if left:
                    raise TxError(f"{F}: CWR-012 {tg}.{f} still holds {left}")
                if any(x in v for x in ("9 January 2023", "9 يناير 2023", "2023-01-09")):
                    raise TxError(f"{F}: CR-21 left a day-precise date in CWR-012 {tg}.{f}")
    for k in ("claim_bindings", "evidence_bindings"):
        rd[k] = list(rd[k]) + ADD_CLAIMS + NEW_IDS
    rd["source_bindings"] = list(rd["source_bindings"]) + ADD_SOURCES
    vb = OrderedDict(rd["verification_bindings"])
    vb["claim_ids"] = list(vb["claim_ids"]) + ADD_CLAIMS + NEW_IDS
    vb["direct_source_ids"] = list(vb["direct_source_ids"]) + ADD_SOURCES
    rd["verification_bindings"] = vb
    rd["last_reviewed"] = TODAY
    return d, rd, sections, sm


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    d, rd, sections, sm = assemble()

    # ---------------------------------------------------------------- 06: the two CCY records
    t06 = Table(s, "06_EVIDENCE_OBJECTS")
    h06 = t06.head
    last06 = max(t06.rows.values())
    rows = []
    for r in nfc(NEW_RECORDS):
        if r["object_id"] in t06.rows:
            raise TxError(f"{F}: 06 already holds {r['object_id']}")
        row = OrderedDict((k, v) for k, v in r.items() if k not in ("meta_en", "meta_ar"))
        row["value_states"] = json.dumps(row["value_states"], ensure_ascii=False, separators=(",", ":"))
        url = t15_url(s, row["source_dependencies"])
        row["source_links"] = json.dumps([{"source_id": row["source_dependencies"], "url": url,
                                           "audit_state": "PASS_AUTHORITY_OR_PROVIDER_LOCATOR"}], separators=(",", ":"))
        rows.append(row)
    s.ed.insert_rows("06_EVIDENCE_OBJECTS", last06 + 1, [{h06.index(k) + 1: v for k, v in row.items() if v is not None} for row in rows])
    for j, row in enumerate(rows):
        for k, v in row.items():
            if v is not None:
                s.ledger.append(OrderedDict([("finding", F), ("sheet", "06_EVIDENCE_OBJECTS"), ("row", last06 + 1 + j),
                                             ("col", h06.index(k) + 1), ("field", f"{row['object_id']}.{k}"), ("old", None), ("new", v)]))

    # ---------------------------------------------------------------- 08, 09, 03: the Reading
    g08 = s.grid("08_READINGS")
    h08 = [str(x) if x is not None else None for x in g08[3]]
    if any(r and r[0] == RID for r in g08):
        raise TxError(f"{F}: 08 already holds {RID}")
    row08 = OrderedDict()
    route3 = rd["route"] if rd["route"].endswith("/") else rd["route"] + "/"
    rd["route"] = route3.rstrip("/")                  # 08 holds the route without its trailing slash (as CWR-001..011)
    for k, v in rd.items():
        if k not in h08:
            raise TxError(f"{F}: 08 has no column {k}")
        if k == "domain_surface_routes" and isinstance(v, list):
            v = " | ".join(v)                         # a plain route, as CWR-001 and CWR-011 hold it
        elif isinstance(v, (list, dict)):
            v = json.dumps(v, ensure_ascii=False, separators=(",", ":"))
        row08[k] = v
    row08 = nfc(row08)
    s.ed.insert_rows("08_READINGS", len(g08) + 1, [{h08.index(k) + 1: v for k, v in row08.items() if v is not None}])
    s.ledger.append(OrderedDict([("finding", F), ("sheet", "08_READINGS"), ("row", len(g08) + 1), ("col", None), ("field", RID),
                                 ("old", None), ("new", json.dumps(row08, ensure_ascii=False)[:2000])]))
    g09 = s.grid("09_READING_SECTIONS")
    s1 = next(x for x in sections if x["section_order"] == 1)
    rows9 = [{1: RID, 2: 1, 3: s1["section_id"], 4: s1["heading_en"], 5: s1["heading_ar"]}]
    rows9 += [{1: RID, 2: x["section_order"], 3: x["section_id"]} for x in sections if x["section_order"] > 1]
    s.ed.insert_rows("09_READING_SECTIONS", len(g09) + 1, nfc(rows9))
    g03 = s.grid("03_PAGE_SECTIONS")
    rows3 = []
    for x in sections:
        if x["section_order"] == 1:
            continue
        r = {1: route3, 2: x["section_order"], 5: x["body_en"], 7: x["body_ar"]}
        if x.get("heading_en"):
            r[4], r[6] = x["heading_en"], x["heading_ar"]
        rows3.append(r)
    s.ed.insert_rows("03_PAGE_SECTIONS", len(g03) + 1, nfc(rows3))
    for what, n in (("09 rows", len(rows9)), ("03 rows", len(rows3))):
        s.ledger.append(OrderedDict([("finding", F), ("sheet", what), ("row", None), ("col", None), ("field", RID), ("old", None),
                                     ("new", f"{n} appended")]))

    # ---------------------------------------------------------------- 02: the Reading's route and the records' routes
    t02 = Table(s, "02_SITE_MAP")
    h02 = t02.head
    after = max(i for k, i in t02.rows.items() if str(k).startswith("/evidence/") and str(k) != "/evidence/compare/")
    new02 = [OrderedDict([("route", f"/evidence/{r['object_id']}/"), ("page_class", "evidence_detail"), ("template_route", "/evidence/[id]"),
                          ("instance_id", r["object_id"]), ("meta_description_en", r["meta_en"]), ("meta_description_ar", r["meta_ar"])])
             for r in nfc(NEW_RECORDS)]
    s.ed.insert_rows("02_SITE_MAP", after + 1, [{h02.index(k) + 1: v for k, v in row.items()} for row in new02])
    g02 = s.grid("02_SITE_MAP")
    rrow = OrderedDict([("route", sm["route"]), ("page_class", sm["page_class"]), ("template_route", sm["template_route"]),
                        ("instance_id", sm["instance_id"]), ("meta_description_en", sm["meta_description_en"]),
                        ("meta_description_ar", sm["meta_description_ar"])])
    last_rd = max(i for i, r in enumerate(g02, 1) if r and str(r[0] or "").startswith("/readings/") and r[0] != "/readings/")
    s.ed.insert_rows("02_SITE_MAP", last_rd + 1, [{h02.index(k) + 1: v for k, v in nfc(rrow).items() if v is not None}])
    for row in new02 + [rrow]:
        s.ledger.append(OrderedDict([("finding", F), ("sheet", "02_SITE_MAP"), ("row", None), ("col", None), ("field", row["route"]),
                                     ("old", None), ("new", json.dumps(row, ensure_ascii=False))]))

    # ---------------------------------------------------------------- 08: CWR-001 relates to CWR-012 (draft related_back)
    t08 = Table(s, "08_READINGS")
    rb = d["related_back"]
    cur = t08.get(rb["reading_id"], "related_readings")
    if json.loads(cur) != rb["current"]:
        raise TxError(f"{F}: {rb['reading_id']} related_readings is {cur}")
    t08.set(F, rb["reading_id"], "related_readings", json.dumps(rb["proposed"]), cur)

    # ---------------------------------------------------------------- 04: search alias 001 (found while closing CLOSE-6B)
    # Its boundary note said the evidence base holds no law; it holds one (SRC-CBY-DIL-21-2008, on the Bank Deposit
    # Insurance Institution), as the /data/ scope line says, and one of its regulatory documents was issued in Sana'a.
    g04 = s.grid(S04)
    at = [i for i, r in enumerate(g04, 1) if r and r[0] == ALIAS001["alias_id"]]
    if len(at) != 1:
        raise TxError(f"{F}: 04 holds {ALIAS001['alias_id']} {len(at)} times")
    for col, f in ((5, "boundary_note_en"), (6, "boundary_note_ar")):
        old, new = ALIAS001[f]
        s.set(F + ":ALIAS-001", S04, at[0], col, unicodedata.normalize("NFC", new), old, field=f"{ALIAS001['alias_id']}.{f}")

    counts = refresh_self_counts(s, F + ":OWN-10")
    rep = s.save(out, ledger, OrderedDict([
        ("transaction", F),
        ("summary", "Stage A addendum item 4: Reading CWR-012 'How money reaches households', with the two Cash Consortium of "
                    "Yemen findings it uses held as records CCY-ISP-2024 and CCY-SAM-2024; and search alias 001's boundary "
                    "note, which said the evidence base holds no law (found while closing CLOSE-6B)."),
        ("self_counts", counts)]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


def t15_url(s, sid):
    t15 = Table(s, "15_SOURCE_LIBRARY")
    url = t15.get(sid, "primary_url")
    if not str(url or "").startswith("http"):
        raise TxError(f"{F}: {sid} has no public locator")
    return url


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
