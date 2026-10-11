# -*- coding: utf-8 -*-
"""Close-out transaction CLOSE-6E (Stage A final instruction v5, 11 October 2026, section 5): evidence strengthening 6C-1 to
6C-5. English and Arabic change together. 6C-6 (the D16 channel tabulation) is not run: the owner's aggregate file has not
arrived, so it is a FRONTIER card (audit/close_out/FRONTIER_CARDS.md), not a Master change.

  python3 close_6e.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Every write checks the exact current value; the texts are in close_6e_text.py, checked against the reads kept in
audit/close_out/v5_reads/ (V3, V4, V5). The work directory receives the updated visual design contract.

- 6C-1 Firms: (a) the 217 informal firms' business debt and main sources of financing on CLM-062 (Annex III, Figures 115
  and 116; multiple answers; not comparable with formal firms' supplier-credit share); (b) SMEPS's 2024 type split on CLM-059.
- 6C-2 After a transfer: (a) the UNICEF programme around the pilot (new sources SRC-UNICEF-UCT-2024-10 and -12): announced
  reach, channels and the programme's end, on CLM-045 and CWR-010; (b) cash-out at agents (one interview); (c) debt
  repayment as an early use of transfers (SAM 2024; Cash Duration 2026); (d) /people/ section 6; (e) MA-001, MA-004,
  MA-005, MA-008 and MA-009 bindings and text.
- 6C-3 Remittance cost: the United States–Yemen corridor (new source SRC-WB-RPW-US-YEM-2025Q3-001; rows
  RMO-RPW-US-2025Q3-200 and -500), the visual, its contract, labels and the pages that said "two corridors".
- 6C-4 Credit infrastructure: (a) REF-REG-012 and YSC-030; (b) Doing Business 2020 (new source SRC-WB-DB2020-YEM-001) on
  YSC-030, with MA-008 pointing to it; (c) FATF is RESERVED (not read on fatf-gafi.org).
- 6C-5 The IFAD Country Programme Evaluation (new source SRC-IFAD-CPE-YEM-2011; new record IFAD-CPE-YEM-2011-RF with its D9
  detail route, on /finance/ and /firms/; MA-004).
"""
import json, os, sys, unicodedata
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from close_lib import Session, Table, TxError, refresh_self_counts, insert_ui_rows, set_ui  # noqa: E402
import close_6e_text as T  # noqa: E402

F = "CLOSE-6E"
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
CONTRACT = os.path.join(ROOT, "scripts", "projection", "controlled_inputs", "visual_design_contract.json")
DESIGN_INTENT = os.path.join(ROOT, "scripts", "projection", "controlled_inputs", "page_spec_design_intent.json")
O6, S07, V11, S14, S15, S23, S31, SMA = ("06_EVIDENCE_OBJECTS", "07_PUBLIC_CLAIMS", "11_VISUAL_LIBRARY", "14_SYSTEM_CHRONOLOGY",
                                         "15_SOURCE_LIBRARY", "23_REMITTANCES", "31_REFORMS_REGULATION", "10_MEASUREMENT_AGENDA")


def nfc(o):
    if isinstance(o, str):
        return unicodedata.normalize("NFC", o)
    if isinstance(o, (list, tuple)):
        return type(o)(nfc(x) for x in o)
    if isinstance(o, dict):
        return OrderedDict((k, nfc(v)) for k, v in o.items())
    return o


def row_of(s, sheet, key):
    hits = [i for i, r in enumerate(s.grid(sheet), 1) if r and r[0] == key]
    if len(hits) != 1:
        raise TxError(f"{F}: {sheet} holds {key} {len(hits)} times")
    return hits[0]


def col_of(s, sheet, field):
    if isinstance(field, int):
        return field
    g = s.grid(sheet)
    for hr in range(1, 7):
        h = [str(x) if x is not None else None for x in g[hr - 1]]
        if h.count(field) == 1:
            return h.index(field) + 1
    raise TxError(f"{F}: {sheet} has no single header {field!r}")


def get(s, sheet, key, field):
    return s.ed.get_value(sheet, row_of(s, sheet, key), col_of(s, sheet, field))


def put(s, fid, sheet, key, field, new, expect):
    s.set(f"{F}:{fid}", sheet, row_of(s, sheet, key), col_of(s, sheet, field), nfc(new), expect, f"{key}.{field}")


def rep(s, fid, sheet, key, field, old, new):
    s.replace(f"{F}:{fid}", sheet, row_of(s, sheet, key), col_of(s, sheet, field), nfc(old), nfc(new), f"{key}.{field}")


def whole(s, fid, sheet, key, field, must_start, new):
    cur = get(s, sheet, key, field)
    if not isinstance(cur, str) or not cur.startswith(nfc(must_start)):
        raise TxError(f"{F}: {sheet} {key}.{field} does not start with {must_start[:50]!r}: {str(cur)[:70]!r}")
    put(s, fid, sheet, key, field, new, cur)


def append_text(s, fid, sheet, key, field, add, must_not_hold=None):
    cur = get(s, sheet, key, field)
    if not isinstance(cur, str) or not cur.strip():
        raise TxError(f"{F}: {sheet} {key}.{field} is empty")
    if nfc(must_not_hold or add.strip()[:60]) in cur:
        raise TxError(f"{F}: {sheet} {key}.{field} already holds the addition")
    put(s, fid, sheet, key, field, cur.rstrip() + nfc(add), cur)


def append_vs(s, fid, sheet, key, add):
    """Add value states; an entry is new unless one with the same text, kind and source is already held."""
    cur = get(s, sheet, key, "value_states")
    vs = json.loads(cur)
    have = {(e.get("t"), e.get("k"), e.get("src")) for e in vs}
    for e in nfc(add):
        if (e["t"], e["k"], e.get("src")) not in have:
            vs.append(OrderedDict(e))
            have.add((e["t"], e["k"], e.get("src")))
    put(s, fid, sheet, key, "value_states", json.dumps(vs, ensure_ascii=False, separators=(",", ":")), cur)


def add_to_list(s, fid, sheet, key, field, ids, compact=False):
    cur = get(s, sheet, key, field)
    lst = json.loads(cur or "[]")
    for i in ids:
        if i not in lst:
            lst.append(i)
    new = json.dumps(lst, separators=(",", ":")) if compact else json.dumps(lst)
    if new != cur:
        put(s, fid, sheet, key, field, new, cur)


def insert_after(s, fid, sheet, after_row, rows, head):
    s.ed.insert_rows(sheet, after_row + 1, [{head.index(k) + 1: v for k, v in nfc(r).items() if v is not None} for r in rows])
    for j, r in enumerate(rows):
        s.ledger.append(OrderedDict([("finding", f"{F}:{fid}"), ("sheet", sheet), ("row", after_row + 1 + j), ("col", None),
                                     ("field", r[head[0]]), ("old", None), ("new", json.dumps(r, ensure_ascii=False)[:2000])]))


def ui_row(s, ui_id):
    return row_of(s, "04_NAV_UX", ui_id)


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)

    # ------------------------------------------------------------------------------------------------ 15: five sources
    t15 = Table(s, S15)
    held = {str(x) for r in s.grid(S15)[4:] if r for x in r[1:3] if x}
    for r in T.NEW_SOURCES:
        if r["source_id"] in t15.rows or r["primary_url"] in held:
            raise TxError(f"{F}: {r['source_id']} or its locator is already in the library")
    insert_after(s, "SOURCES", S15, max(t15.rows.values()), T.NEW_SOURCES, t15.head)
    url = {r["source_id"]: r["primary_url"] for r in T.NEW_SOURCES}

    # ------------------------------------------------------------------------------------------------ 6C-1(a): CLM-062
    for i, lang in enumerate(("en", "ar")):
        rep(s, "6C-1a", O6, "CLM-062", f"summary_{lang}", T.INF_OLD[i], T.INF_NEW[i])
        rep(s, "6C-1a", O6, "CLM-062", f"definition_{lang}", *T.INF_DEF[i])
        rep(s, "6C-1a", O6, "CLM-062", f"method_{lang}", *T.INF_METHOD[i])
        rep(s, "6C-1a", O6, "CLM-062", f"limitations_{lang}", *T.INF_LIM[i])
    append_vs(s, "6C-1a", O6, "CLM-062", T.INF_VS)
    add_to_list(s, "6C-1a", S07, "CLM-062", "evidence_inputs", ["FFM-012", "FFM-013"], compact=True)

    # ------------------------------------------------------------------------------------------------ 6C-1(b): CLM-059
    for i, lang in enumerate(("en", "ar")):
        rep(s, "6C-1b", O6, "CLM-059", f"summary_{lang}", T.SMEPS_OLD[i], T.SMEPS_NEW[i])
    append_vs(s, "6C-1b", O6, "CLM-059", T.SMEPS_VS)

    # ------------------------------------------------------------------------------------------------ 6C-2: CLM-045 and CWR-010
    for i, lang in enumerate(("en", "ar")):
        append_text(s, "6C-2a", O6, "CLM-045", f"summary_{lang}", " " + T.UCT[i] + " " + T.DEBT[i])
    rep(s, "6C-2b", O6, "CLM-045", "limitations_en", "given the scarcity of bank branches and ATMs. | ",
        "given the scarcity of bank branches and ATMs. " + T.CASH_RECORD[0] + " | ")
    rep(s, "6C-2b", O6, "CLM-045", "limitations_ar", "نظرًا إلى ندرة فروع البنوك وأجهزة الصراف الآلي. | ",
        "نظرًا إلى ندرة فروع البنوك وأجهزة الصراف الآلي. " + T.CASH_RECORD[1] + " | ")
    dep = get(s, O6, "CLM-045", "source_dependencies")
    add = [x for x in (T.UNI10, T.UNI12, T.PRESS) if x not in dep]
    put(s, "6C-2", O6, "CLM-045", "source_dependencies", dep + "".join("; " + x for x in add), dep)
    append_vs(s, "6C-2", O6, "CLM-045", T.CLM045_VS)

    R10 = "/readings/after-transfer-persistence/"
    for i, lang in enumerate(("en", "ar")):
        old3 = ("account opening should not automatically be labelled inclusion.", "ولا وصف فتح الحساب بالشمول تلقائيًا.")[i]
        s.replace_section(f"{F}:6C-2c", R10, 3, lang, "body", nfc(old3), nfc(old3 + "\n" + T.DEBT[i]))
        old5 = ("but whether recipients could exercise it without risking their access to the payment.",
                "بل يشمل ما إذا استطاع المستفيدون ممارسته من دون المخاطرة بوصولهم إلى الدفعة.")[i]
        s.replace_section(f"{F}:6C-2a", R10, 5, lang, "body", nfc(old5), nfc(old5 + "\n" + T.UCT[i]))
        old6 = ("attributes it to the regional conflict and to cash hoarding without testing that explanation.",
                "ويعزوها التقرير إلى النزاع الإقليمي وإلى اكتناز النقد دون أن يختبر هذا التفسير.")[i]
        s.replace_section(f"{F}:6C-2b", R10, 6, lang, "body", nfc(old6), nfc(old6 + "\n" + T.CASH_READING[i]))
    add_to_list(s, "6C-2", "08_READINGS", "CWR-010", "source_bindings", [T.UNI10, T.UNI12, T.SAM, T.CDUR])
    vb = json.loads(get(s, "08_READINGS", "CWR-010", "verification_bindings"))
    old_vb = get(s, "08_READINGS", "CWR-010", "verification_bindings")
    for x in (T.UNI10, T.UNI12, T.SAM, T.CDUR):
        if x not in vb["direct_source_ids"]:
            vb["direct_source_ids"].append(x)
    put(s, "6C-2", "08_READINGS", "CWR-010", "verification_bindings", json.dumps(vb, ensure_ascii=False), old_vb)
    append_text(s, "6C-2", "08_READINGS", "CWR-010", "evidence_period_en", T.CWR010_PERIOD[0])
    append_text(s, "6C-2", "08_READINGS", "CWR-010", "evidence_period_ar", T.CWR010_PERIOD[1])

    for i, lang in enumerate(("en", "ar")):
        s.replace_section(f"{F}:6C-2d", "/people/", 6, lang, "body", *nfc(T.PEOPLE_S6[i]))

    for mid, (en, ar, ev, srcs) in T.MA_ADD.items():
        append_text(s, "6C-2e" if mid not in ("MA-004", "MA-008") else ("6C-5" if mid == "MA-004" else "6C-4b"),
                    SMA, mid, "current_evidence_en", en)
        append_text(s, "6C-2e" if mid not in ("MA-004", "MA-008") else ("6C-5" if mid == "MA-004" else "6C-4b"),
                    SMA, mid, "current_evidence_ar", ar)
        if ev:
            add_to_list(s, "6C-2e", SMA, mid, "evidence_bindings", ev)
        if srcs:
            add_to_list(s, "6C-2e", SMA, mid, "source_bindings", srcs)

    # ------------------------------------------------------------------------------------------------ 6C-3: the US corridor
    VID = "VIS-REMITTANCE-COST"
    t23 = Table(s, S23)
    for r in T.RPW_ROWS:
        if r["observation_id"] in t23.rows:
            raise TxError(f"{F}: 23 already holds {r['observation_id']}")
    insert_after(s, "6C-3", S23, row_of(s, S23, "RMO-RPW-UAE-2025Q3-500"), T.RPW_ROWS, t23.head)
    for k in ("RMO-WDI-RMTCOST-2016", "RMO-WDI-RMTCOST-2017", "RMO-WDI-RMTCOST-2022", "RMO-WDI-RMTCOST-2023"):
        rep(s, "6C-3", S23, k, "caveat_ar", *T.WDI_CAVEAT_AR)

    for i, lang in enumerate(("en", "ar")):
        for sheet, f in ((O6, "title"), (V11, "title")):
            put(s, "6C-3", sheet, VID, f"{f}_{lang}", T.RPW_TITLE[i], T.RPW_OLD_TITLE[i])
        for sheet, f in ((O6, "summary"), (V11, "accessible_summary")):
            rep(s, "6C-3", sheet, VID, f"{f}_{lang}", *T.RPW_SUM[i])
        rep(s, "6C-3", O6, VID, f"definition_{lang}", *T.RPW_DEF[i])
        rep(s, "6C-3", O6, VID, f"universe_{lang}", *T.RPW_UNIV[i])
        rep(s, "6C-3", O6, VID, f"method_{lang}", *T.RPW_METHOD[i])
        for sheet, f in ((O6, "limitations"), (V11, "prohibited_inference")):
            rep(s, "6C-3", sheet, VID, f"{f}_{lang}", *T.RPW_LIM1[i])
        rep(s, "6C-3", O6, VID, f"limitations_{lang}", *T.RPW_LIM2[i])
        rep(s, "6C-3", O6, VID, f"currentness_{lang}", *T.RPW_CURR[i])
        rep(s, "6C-3", V11, VID, f"what_it_shows_{lang}", *T.RPW_SHOWS[i])
        rep(s, "6C-3", V11, VID, f"decision_value_{lang}", *T.RPW_DECISION[i])
    rep(s, "6C-3", O6, VID, "period_ar", *T.RPW_PERIOD_AR)
    rep(s, "6C-3", V11, VID, "denominator_universe", *T.RPW_UNIV[0])
    rep(s, "6C-3", V11, VID, "encoding_contract", *T.RPW_ENCODING)
    rep(s, "6C-3", V11, VID, "encoding_contract", *T.RPW_ENCODING2)
    dep = get(s, O6, VID, "source_dependencies")
    put(s, "6C-3", O6, VID, "source_dependencies",
        dep.replace("SRC-WB-RPW-UAE-YEM-2025Q3-001", "SRC-WB-RPW-UAE-YEM-2025Q3-001; " + T.RPWUS), dep)
    append_vs(s, "6C-3", O6, VID, T.RPW_VS)
    for fid, route, order, lang, field, old, new in T.SECTIONS_RPW:
        s.replace_section(f"{F}:{fid}", route, order, lang, field, nfc(old), nfc(new))
    add_to_list(s, "6C-3", "08_READINGS", "CWR-012", "source_bindings", [T.RPWUS], compact=True)
    old_vb = get(s, "08_READINGS", "CWR-012", "verification_bindings")
    vb = json.loads(old_vb, object_pairs_hook=OrderedDict)
    if T.RPWUS not in vb["direct_source_ids"]:
        vb["direct_source_ids"].insert(vb["direct_source_ids"].index("SRC-WB-RPW-SA-YEM-2025Q3-001") + 1, T.RPWUS)
        put(s, "6C-3", "08_READINGS", "CWR-012", "verification_bindings",
            json.dumps(vb, ensure_ascii=False, separators=(",", ":")), old_vb)
    insert_ui_rows(s, f"{F}:6C-3", nfc(T.UI_NEW))
    for ui_id, en, ar, old_en, old_ar in T.UI_RPW:
        set_ui(s, f"{F}:6C-3", ui_id, nfc(en), nfc(ar), nfc(old_en), nfc(old_ar))
    for ui_id, old, new in T.UI_RPW_AR_FIX:
        r = ui_row(s, ui_id)
        cur = s.ed.get_value("04_NAV_UX", r, 3)
        if cur.count(nfc(old)) != 1:
            raise TxError(f"{F}: {ui_id} label_ar does not hold {old!r} once")
        set_ui(s, f"{F}:6C-3", ui_id, None, cur.replace(nfc(old), nfc(new)), None, cur)

    with open(CONTRACT, encoding="utf-8") as fh:
        c = json.load(fh, object_pairs_hook=OrderedDict)
    v = next(x for x in c["visuals"] if x["visual_id"] == VID)
    k = v["contract"]
    if not k["form"].startswith("Dot plot: two corridors × two send amounts"):
        raise TxError(f"{F}: the {VID} contract form is not the one expected")
    k["form"] = k["form"].replace("Dot plot: two corridors × two send amounts", "Dot plot: three corridors × two send amounts", 1)
    rpw = next(x for x in k["series"] if x["id"] == "rpw")
    rpw["must_equal"]["RMO-RPW-US-2025Q3-200"] = 3.92
    if not k["missing"].startswith("Provider and quote counts are not held; not drawn."):
        raise TxError(f"{F}: the {VID} contract's missing note is not the one expected")
    k["missing"] = k["missing"].replace("Provider and quote counts are not held; not drawn.",
                                        "Quote counts are given in the record's limitations; not drawn.", 1)
    if k.get("mobile") == "Two rows of paired dots; then one row per year.":
        k["mobile"] = "Three rows of paired dots; then one row per year."
    k["credit"]["source_ids"] = list(k["credit"]["source_ids"]) + ([T.RPWUS] if T.RPWUS not in k["credit"]["source_ids"] else [])
    ns = c["display_labels"]["namespaces"]
    if ns["corridor"].get("Saudi Arabia") != "UI-VIS-CAT-CORRIDOR-SA" or "United States" in ns["corridor"]:
        raise TxError(f"{F}: the contract's corridor labels are not the ones expected")
    ns["corridor"]["United States"] = "UI-VIS-CAT-CORRIDOR-US"
    with open(os.path.join(work, "visual_design_contract.json"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(c, ensure_ascii=False, indent=2) + "\n")

    # ------------------------------------------------------------------------------------------------ 6C-4: credit infrastructure
    whole(s, "6C-4a", S31, "REF-REG-012", 5, T.REF_REG_012_START, T.REF_REG_012)
    append_text(s, "6C-4a", S14, "YSC-030", "fact_en", T.YSC030_FACT[0])
    append_text(s, "6C-4a", S14, "YSC-030", "fact_ar", T.YSC030_FACT[1])
    put(s, "6C-4a", S14, "YSC-030", "system_implication_en", T.YSC030_IMPL[0], nfc(T.YSC030_IMPL_OLD[0]))
    put(s, "6C-4a", S14, "YSC-030", "system_implication_ar", T.YSC030_IMPL[1], nfc(T.YSC030_IMPL_OLD[1]))
    append_text(s, "6C-4b", S14, "YSC-030", "fi_relevance_en", T.YSC030_REL[0])
    append_text(s, "6C-4b", S14, "YSC-030", "fi_relevance_ar", T.YSC030_REL[1])
    ids = get(s, S14, "YSC-030", "source_ids")
    put(s, "6C-4b", S14, "YSC-030", "source_ids", ids + " | " + T.DB20, ids)
    append_vs(s, "6C-4", S14, "YSC-030", T.YSC030_VS)

    # ------------------------------------------------------------------------------------------------ 6C-5: the IFAD record
    t06 = Table(s, O6)
    if T.IFADR in t06.rows:
        raise TxError(f"{F}: 06 already holds {T.IFADR}")
    rec = OrderedDict(nfc(T.IFAD_RECORD))
    rec["value_states"] = json.dumps(rec["value_states"], ensure_ascii=False, separators=(",", ":"))
    rec["source_links"] = json.dumps([{"source_id": T.IFADS, "url": url[T.IFADS], "audit_state": "PASS_AUTHORITY_OR_PROVIDER_LOCATOR"}],
                                     separators=(",", ":"))
    insert_after(s, "6C-5", O6, max(t06.rows.values()), [rec], t06.head)
    t02 = Table(s, "02_SITE_MAP")
    after = max(i for kk, i in t02.rows.items() if str(kk).startswith("/evidence/") and str(kk) != "/evidence/compare/")
    row02 = OrderedDict([("route", f"/evidence/{T.IFADR}/"), ("page_class", "evidence_detail"), ("template_route", "/evidence/[id]"),
                         ("instance_id", T.IFADR), ("meta_description_en", T.IFAD_META[0]), ("meta_description_ar", T.IFAD_META[1])])
    insert_after(s, "6C-5", "02_SITE_MAP", after, [row02], t02.head)
    with open(DESIGN_INTENT, encoding="utf-8") as fh:
        di = json.load(fh, object_pairs_hook=OrderedDict)
    route = f"/evidence/{T.IFADR}/"
    if route in di["routes"]:
        raise TxError(f"{F}: page_spec_design_intent already holds {route}")
    routes = OrderedDict()
    for kk, vv in di["routes"].items():
        routes[kk] = vv
        if kk == "/evidence/CCY-SAM-2024/":
            routes[route] = OrderedDict([
                ("user_job_internal", "Let the user verify one governed evidence object without losing definition, scope, "
                                      "period, method, source, limits or correction state."),
                ("primary_user_question_internal", "What exactly supports and limits “rural credit in IFAD-financed projects "
                                                   "in Yemen, 1993 to 2010”?")])
    if route not in routes:
        raise TxError(f"{F}: page_spec_design_intent has no /evidence/CCY-SAM-2024/ to follow")
    di["routes"] = routes
    with open(os.path.join(work, "page_spec_design_intent.json"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(di, ensure_ascii=False, indent=2) + "\n")

    # ------------------------------------------------------------------------------------------------ checks before saving
    for route in (f"/evidence/{T.IFADR}/",):
        for f in ("meta_description_en", "meta_description_ar"):
            val = get(s, "02_SITE_MAP", route, f)
            if len(val) > 200:
                raise TxError(f"{F}: {route} {f} is {len(val)} characters (F6-G01 allows 200)")

    counts = refresh_self_counts(s, F + ":OWN-10")
    rep_ = s.save(out, ledger, OrderedDict([
        ("transaction", F),
        ("summary", "Stage A final instruction v5, section 5: evidence strengthening 6C-1 to 6C-5 (informal firms; SMEPS type "
                    "split; the UNICEF programme, cash-out and debt repayment around the pilot; the United States corridor; "
                    "credit-information rules and Doing Business 2020; the IFAD evaluation as record IFAD-CPE-YEM-2011-RF); five "
                    "new sources. 6C-6 is a FRONTIER card: the owner's aggregate file has not arrived."),
        ("self_counts", counts)]))
    print(json.dumps({k_: rep_[k_] for k_ in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
