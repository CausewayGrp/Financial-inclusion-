# -*- coding: utf-8 -*-
"""Release-candidate transaction RC-8 — truth and currentness, one merged transaction (owner note, 3 October 2026, 03:10,
point 3: "RC-8 to RC-10 may merge where they touch different cells").

  python3 rc_8_truth_currentness.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Every source statement below was read in its original on 3 October 2026 and is recorded in
audit/release_candidate/ORIGINAL_SOURCE_VERIFICATION.md.

A1  VIS-PAYMENT-RAILS. The text alternative and the record's answer name two steps the drawing and its table do not have
    (the mobile e-money amendment, 9 July 2025; the FMIIP approval, 17 June 2025). The figure draws the deduplicated event
    set of the accepted signature chain RV-CWR-009, so the two steps leave the text, in both languages and both places.
    scripts/validate.py gains gate RC-A1 with a negative control.
A2  Search for "law" / «قانون». SEARCH-ALIAS-001 gains a boundary note in the pattern of SEARCH-ALIAS-025; the B5 scope
    line on /data/ names the issuer and what is not held. All 23 documents in the regulatory group were issued by CBY-Aden
    and no source in the evidence base is a law; the base does list one CBY-Sana'a circular as an unread locator
    (SRC-CBY-SANAA-C12-2024), so "not held" is said of the group only.
POS The CBY-Aden monthly POS series moves from January to June 2026: five releases (February–June 2026) listed on the
    Arabic payments page only (https://cby-ye.com/pages/33); the English page still ends at January 2026. Fifteen
    observations, five source records, the copy (rc_8_pos_copy.py), the analytics rows, and the contract and code pins
    (rc_8_stage_inputs.py, scripts/yfie/visuals.py, scripts/validate.py). Owner condition: the May release contradicts
    itself (terminals +2.4%, transactions +9.9%, against totals that do not give them); the totals and the displayed
    percentages are printed and no change is derived for that month. The value tile is labelled «مليار» from January
    2026; the series stays in YER million, disclosed.
D10 Governor's Decision No. 10 of 2026 (EXT-02): the signed decision is dated 8 June 2026 (Ref. 345/CBY/2026); the news
    page that announced it is dated 9 June. PSE-012 and the source record take the instrument date and the scan.
D18 Governor's Decision No. 18 of 2026 (EXT-03; owner note point 1): the four entities, read Arabic first from the signed
    scan, enter the Master as non-public lineage only (PRV-EXCH-E023..E025, PRV-REM-E006), with the scan as locator.
    No name is printed anywhere. PSE-015 prints what the other decisions print; CLM-019 drops "not yet transcribed" and
    states the governed rule; the class label is corrected (one exchange company, two establishments, one agent).
LOC Locators read on 3 October 2026: the licensed-bank list (newer Arabic file of July 2026, 26 banks, names unchanged);
    the POS publication pages (Arabic page is pages/33, not pages/11); the January 2026 POS re-issue on the Arabic list.
ED  The edition moves to 3 October 2026, the date of the currentness sweep: the edition label and the cells that state
    the edition date. VIS-REMITTANCE-COST keeps "as checked on 26 September 2026" (the corridor pages could not be read
    on 3 October; Cloudflare).
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rc_lib import Session, Table, TxError, set_ui  # noqa: E402
import rc_8_pos_copy as POS  # noqa: E402

F_A1, F_A2, F_POS, F_D10, F_D18, F_LOC, F_ED = ("RC-8:A1", "RC-8:A2", "RC-8:POS", "RC-8:D10", "RC-8:D18", "RC-8:LOC",
                                                "RC-8:EDITION")

# ---------------------------------------------------------------------------------------------------------------- A1
A1_SUBS = [
    (", and the mobile e-money amendment (9 July 2025).", "."),
    ("(FMIIP), approved on 17 June 2025 and started in July 2025,", "(FMIIP), which started in July 2025,"),
    ("، وتعديل تعليمات النقود الإلكترونية عبر الهاتف المحمول (9 يوليو 2025).", "."),
    ("الذي أُقر في 17 يونيو 2025 وبدأ في يوليو 2025", "الذي بدأ في يوليو 2025"),
]
A1_CELLS = [("06_EVIDENCE_OBJECTS", "VIS-PAYMENT-RAILS", "summary_en"), ("06_EVIDENCE_OBJECTS", "VIS-PAYMENT-RAILS", "summary_ar"),
            ("11_VISUAL_LIBRARY", "VIS-PAYMENT-RAILS", "accessible_summary_en"), ("11_VISUAL_LIBRARY", "VIS-PAYMENT-RAILS", "accessible_summary_ar")]

# ---------------------------------------------------------------------------------------------------------------- A2
ALIAS_NOTE_EN = ("Discovery aid only: this evidence base holds no laws. It holds regulations, circulars, decisions and official "
                 "lists issued by the Central Bank of Yemen – Aden, listed on the Data page.")
ALIAS_NOTE_AR = ("أداة اكتشاف فقط: لا تضم قاعدة الأدلة هذه أي قانون. وتضم لوائح وتعاميم وقرارات وقوائم رسمية صادرة عن البنك "
                 "المركزي اليمني – عدن، مدرجة في صفحة البيانات.")
SCOPE_OLD_EN = "These are the regulatory documents held in this evidence base, not a complete register of Yemen's financial regulation."
SCOPE_OLD_AR = "هذه هي الوثائق التنظيمية المتوفرة في قاعدة الأدلة هذه، وليست سجلًا كاملًا للتنظيم المالي في اليمن."
SCOPE_NEW_EN = SCOPE_OLD_EN + (" All were issued by the Central Bank of Yemen – Aden. The evidence base holds no laws, and this "
                               "group holds no instrument issued in Sana'a.")
SCOPE_NEW_AR = SCOPE_OLD_AR + (" وقد أصدرها جميعًا البنك المركزي اليمني – عدن. ولا تضم قاعدة الأدلة أي قانون، ولا تضم هذه "
                               "المجموعة أي وثيقة صادرة في صنعاء.")

# ---------------------------------------------------------------------------------------------------------- edition
ED_EN, ED_AR = ("26 September 2026", "3 October 2026"), ("26 سبتمبر 2026", "3 أكتوبر 2026")
ED_CELLS = [("03_PAGE_SECTIONS", 63, 5, "en"), ("03_PAGE_SECTIONS", 63, 7, "ar")]
ED_CELLS += [("06_EVIDENCE_OBJECTS", r, c, "en" if c % 2 == 0 else "ar") for r, cs in ((12, (8, 9, 10, 11, 18, 19)), (63, (18, 19)),
                                                                                    (78, (6, 7, 10, 11, 18, 19)), (80, (10, 11, 18, 19)))
             for c in cs]
ED_CELLS += [("11_VISUAL_LIBRARY", 6, 17, "en"), ("11_VISUAL_LIBRARY", 7, 17, "en"), ("11_VISUAL_LIBRARY", 8, 17, "en"),
             ("11_VISUAL_LIBRARY", 8, 21, "en"), ("11_VISUAL_LIBRARY", 8, 22, "ar")]

# ------------------------------------------------------------------------------------- licensed-bank list, check date
BL_EN, BL_AR = ("7 September 2026", "3 October 2026"), ("7 سبتمبر 2026", "3 أكتوبر 2026")
BL_CELLS = [("02_SITE_MAP", 18, 7, "en"), ("02_SITE_MAP", 18, 8, "ar")]
BL_CELLS += [("03_PAGE_SECTIONS", r, c, "en" if c == 5 else "ar") for r, c in ((216, 5), (216, 7), (217, 5), (218, 7), (278, 5), (278, 7),
                                                                              (343, 5), (344, 7), (345, 5), (346, 7), (355, 5), (356, 7))]
BL_CELLS += [("06_EVIDENCE_OBJECTS", 18, c, "en" if c % 2 == 0 else "ar") for c in (6, 7, 18, 19)]
BL_CELLS += [("06_EVIDENCE_OBJECTS", r, c, "en" if c % 2 == 0 else "ar") for r in (62, 99) for c in (6, 7, 8, 9, 10, 11, 14, 15, 18, 19)]
BL_CELLS += [("08_READINGS", 10, 21, "en"), ("08_READINGS", 10, 22, "ar"), ("11_VISUAL_LIBRARY", 19, 21, "en"),
             ("11_VISUAL_LIBRARY", 19, 22, "ar"), ("15_SOURCE_LIBRARY", 6, 6, "en"), ("15_SOURCE_LIBRARY", 6, 12, "ar")]

# --------------------------------------------------------------------------------------------------------- POS data
POS_PAGE_AR = "https://cby-ye.com/pages/33"
MONTHS = [  # month, file id, terminals, transactions, value (YER million as read), displayed % (terminals, transactions, value)
    ("2026-02", "6a6f958d49cc2", "February", "فبراير", 1502, 23037, 1232, ("+1.9%", "-4.1%", "-2.3%")),
    ("2026-03", "6a6f960871730", "March", "مارس", 1544, 25663, 1124, ("+2.8%", "+11.4%", "-8.8%")),
    ("2026-04", "6a6f968423908", "April", "أبريل", 1583, 30559, 1244, ("+2.5%", "+19.1%", "+10.7%")),
    ("2026-05", "6a6f96ed5c009", "May", "مايو", 1636, 36201, 1579, ("+2.4%", "+9.9%", "+26.9%")),
    ("2026-06", "6a6f973c98c25", "June", "يونيو", 1651, 27504, 1045, ("+0.9%", "-24.0%", "-33.8%")),
]
SCOPE_NOTE = "CBY POS reporting scope; not automatically equivalent to full-population or person-level coverage."
LOCATOR = "one-page monthly POS infographic (Arabic payments page, https://cby-ye.com/pages/33); KPI tile"
VALUE_CAVEAT = ("Normalized to YER millions. The tile is labelled «مليار» (billion), as in every release from January 2026; it is read "
                "as YER million in continuity with the earlier releases, which state million YER, because only that reading "
                "reconciles with the month-on-month changes the releases print (displayed {pct}).")
CONTRA = "DIRECTLY_COMPARABLE_WITH_SOURCE_INTERNAL_PERCENT_CONTRADICTION"
MAY_CAVEAT = {
    "IND-0002": ("May 2026 source-displayed +2.4% POS change does not reconcile to the published April 1,583 and May 1,636; retain "
                 "raw totals and control the contradiction; no change is derived for this month because the source contradicts "
                 "itself (owner note, 3 October 2026)."),
    "IND-0003": ("May 2026 source-displayed +9.9% transaction-count change does not reconcile to the published April 30,559 and May "
                 "36,201; retain raw totals and control the contradiction; no change is derived for this month because the source "
                 "contradicts itself (owner note, 3 October 2026)."),
}
FEB_CAVEAT = {"IND-0002": "February 2026 displays +1.9% where the totals give about 1.97%: read as truncation, not contradiction."}


def obs_rows(first_id):
    rows, n = [], first_id
    for ym, fid, _, _, term, txn, val, pct in MONTHS:
        for ind, v, unit, cur, p in (("IND-0002", term, "count", None, pct[0]), ("IND-0003", txn, "count", None, pct[1]),
                                     ("IND-0004", val, "YER_million", "YER", pct[2])):
            if ind == "IND-0004":
                state, cav = "DIRECTLY_COMPARABLE", VALUE_CAVEAT.format(pct=p.replace("-", "−"))
            elif ym == "2026-05":
                state, cav = CONTRA, MAY_CAVEAT[ind]
            else:
                state, cav = "DIRECTLY_COMPARABLE", (FEB_CAVEAT.get(ind) if ym == "2026-02" else None)
            rows.append({1: f"OBS-{n:05d}", 2: ind, 3: v, 4: unit, 5: cur, 6: ym, 7: "GEO-YEM-NAT", 8: SCOPE_NOTE,
                         9: "CBY POS reporting scope", 10: f"SRC-CBY-POS-{ym}", 11: LOCATOR, 12: f"{v:,}", 13: v, 14: state, 15: cav})
            n += 1
    return rows


def pos_source_rows():
    out = []
    for ym, fid, m_en, m_ar, *_ in MONTHS:
        uses = "DS-CBY-PAYMENTS,DS-PAYMENT-CURRENTNESS" if ym == "2026-06" else "DS-CBY-PAYMENTS"
        out.append({1: f"SRC-CBY-POS-{ym}", 2: f"https://cby-ye.com/files/{fid}.pdf", 3: json.dumps([POS_PAGE_AR]), 4: uses, 5: 3,
                    6: f"Monthly Point of Sale Transactions ({m_en} 2026)", 7: "Central Bank of Yemen — Aden", 11: "CITATION_CARD",
                    12: f"معاملات نقاط البيع الشهرية ({m_ar} 2026)", 19: "NOT_ASSESSED", 22: "2026-10-03",
                    25: "البنك المركزي اليمني – عدن", 26: "Statistical release", 27: "إصدار إحصائي"})
    return out


NEW_POS = [f"SRC-CBY-POS-{m[0]}" for m in MONTHS]


def link(sid, fid):
    return OrderedDict([("source_id", sid), ("url", f"https://cby-ye.com/files/{fid}.pdf"), ("audit_state", "PASS_AUTHORITY_OR_PROVIDER_LOCATOR")])


# ------------------------------------------------------------------------------------------------- Decision 18 (D18)
SCAN18 = "https://www.cby-ye.com/files/6ab52faa3604f.pdf"
SCAN10 = "https://www.cby-ye.com/files/6a27bc7883b9c.pdf"
LINEAGE_RULE = ("NON-PUBLIC LINEAGE ONLY (owner note, 3 October 2026, point 1): the name is printed on no page, table, search "
                "record or social image. The public record shows the dated event, decision number, class and action only.")
D18_ENTITIES = [  # id, rendering (not official), Arabic as printed in the signed decision, class
    ("PRV-EXCH-E023", "Saddam Express Exchange and Transfers Company", "شركة صدام اكسبرس للصرافة والتحويلات", "EXCHANGE_COMPANY"),
    ("PRV-EXCH-E024", "Khalid Al-Asawani Exchange Establishment", "منشأة خالد العصواني للصرافة", "EXCHANGE_ESTABLISHMENT"),
    ("PRV-EXCH-E025", "Marta' Exchange and Transfers Establishment", "منشأة مرتع للصرافة والتحويلات", "EXCHANGE_ESTABLISHMENT"),
    ("PRV-REM-E006", "Bin Omar — remittance agent", "بن عمر وكيل حوالة", "REMITTANCE_AGENT"),
]

CLM019 = {
    "universe_en": ("Only the providers named in the decisions covered here (for Decision No. 18, the named entities have not "
                    "yet been transcribed); not the full set of exchange and remittance providers",
                    "Only the providers named in the decisions covered here; not the full set of exchange and remittance providers"),
    "universe_ar": ("الجهات المسماة في القرارات التي يشملها هذا السجل فقط (ولم تُنقل بعد أسماء الجهات الواردة في القرار رقم 18)؛ "
                    "ولا تمثل المجموعة الكاملة لمقدمي خدمات الصرافة والحوالات.",
                    "الجهات المسماة في القرارات التي يشملها هذا السجل فقط؛ ولا تمثل المجموعة الكاملة لمقدمي خدمات الصرافة والحوالات."),
    "method_en": ("Each decision is taken from its official publication by the Central Bank of Yemen – Aden (CBY-Aden) and "
                  "recorded by date, action and the entity or class of entity it names. The entities named in Decision No. 18 of "
                  "24 September 2026 have not yet been transcribed. The decisions are not treated as a census of all providers or "
                  "as proof that a listed provider is currently operating.",
                  "Each decision is taken from its official publication by the Central Bank of Yemen – Aden (CBY-Aden) and "
                  "recorded by date, decision number, action and the class of entity it names. The names of the entities are "
                  "recorded in this resource's lineage from the signed decisions and are not printed on this site. The decisions "
                  "are not treated as a census of all providers or as proof that a listed provider is currently operating."),
    "method_ar": ("يؤخذ كل قرار من نشره الرسمي لدى البنك المركزي اليمني – عدن، ويُسجَّل بحسب تاريخه ونوع الإجراء والجهة أو فئة "
                  "الجهات المسماة فيه. ولم تُنقل بعد أسماء الجهات الواردة في القرار رقم 18 المؤرخ في 24 سبتمبر 2026. ولا تُعامل "
                  "القرارات بوصفها تعدادًا لجميع مقدمي الخدمات أو دليلًا على أن مقدم خدمة مدرجًا يعمل حاليًا.",
                  "يؤخذ كل قرار من نشره الرسمي لدى البنك المركزي اليمني – عدن، ويُسجَّل بحسب تاريخه ورقمه ونوع الإجراء وفئة "
                  "الجهات التي يسميها. وتُسجَّل أسماء الجهات في سجل المصادر الداخلي لهذا المورد من القرارات الموقعة، ولا تُطبع "
                  "في هذا الموقع. ولا تُعامل القرارات بوصفها تعدادًا لجميع مقدمي الخدمات أو دليلًا على أن مقدم خدمة مدرجًا "
                  "يعمل حاليًا."),
}


def replace_once(s, finding, sheet, r, c, pair):
    cur = s.ed.get_value(sheet, r, c)
    if not isinstance(cur, str) or cur.count(pair[0]) != 1:
        raise TxError(f"{finding}: {sheet}!r{r}c{c}: {pair[0]!r} occurs {0 if not isinstance(cur, str) else cur.count(pair[0])} times")
    s.set(finding, sheet, r, c, cur.replace(*pair), cur)


def set_json_list(t, finding, key, field, expect, new):
    cur = t.get(key, field)
    if (json.loads(cur) if cur else None) != expect:
        raise TxError(f"{finding}: {t.sheet} {key}.{field} holds {cur!r}")
    t.set(finding, key, field, json.dumps(new), cur)


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    notes = OrderedDict()

    # ---- 1. cell rewrites at fixed coordinates (before any row is inserted) --------------------------------------
    n_pos = POS.apply(s, F_POS)
    for sheet, r, c, lang in ED_CELLS:
        replace_once(s, F_ED, sheet, r, c, ED_EN if lang == "en" else ED_AR)
    for sheet, r, c, lang in BL_CELLS:
        replace_once(s, F_LOC, sheet, r, c, BL_EN if lang == "en" else BL_AR)

    # ---- 2. keyed edits -------------------------------------------------------------------------------------------
    hits = OrderedDict((a, 0) for a, _ in A1_SUBS)
    for sheet, key, field in A1_CELLS:
        t = Table(s, sheet, 4)
        cur = t.get(key, field)
        new = cur
        for a, b in A1_SUBS:
            hits[a] += new.count(a)
            new = new.replace(a, b)
        if new == cur:
            raise TxError(f"A1: {sheet} {key}.{field}: nothing to change")
        t.set(F_A1, key, field, new, cur)
    if any(n != 2 for n in hits.values()):
        raise TxError(f"A1: each substitution must apply twice (record answer and text alternative): {dict(hits)}")
    notes["A1"] = ("DONE — the two steps the drawing lacks (the e-money amendment, 9 July 2025; the FMIIP approval, 17 June 2025) "
                   "leave the record's answer and the text alternative of VIS-PAYMENT-RAILS, in both languages; gate RC-A1")

    t04 = Table(s, "04_NAV_UX", 533)
    for lang, val in (("en", ALIAS_NOTE_EN), ("ar", ALIAS_NOTE_AR)):
        t04.set(F_A2, "SEARCH-ALIAS-001", f"boundary_note_{lang}", val, None)
    set_ui(s, F_A2, "UI-DATA-GROUP-REGULATORY-SCOPE", SCOPE_NEW_EN, SCOPE_NEW_AR, SCOPE_OLD_EN, SCOPE_OLD_AR)
    notes["A2"] = ("DONE — SEARCH-ALIAS-001 carries a boundary note; the B5 scope line names the issuer and what is not held "
                   "(no laws in the evidence base; no Sana'a instrument in the group)")

    set_ui(s, F_ED, "UI-CONTENT-VERSION", "Edition of 3 October 2026", "إصدار 3 أكتوبر 2026",
           "Edition of 26 September 2026", "إصدار 26 سبتمبر 2026")
    set_ui(s, F_D18, "UI-VIS-CAT-PRV-EVCLASS-COMPANY-ESTS-AGENT", "Exchange company, establishments and remittance agent",
           "شركة صرافة ومنشآت صرافة ووكيل حوالات", "Exchange company establishments and remittance agent", "منشآت شركة صرافة ووكيل حوالات")

    t06 = Table(s, "06_EVIDENCE_OBJECTS", 4)
    for field, (old, new) in CLM019.items():
        t06.set(F_D18, "CLM-019", field, new, old)
    # source dependencies and links of the POS records
    deps = {"CLM-003": ("SRC-CBY-POS-2025-03; SRC-CBY-POS-2025-12; SRC-CBY-POS-2026-01",
                        "SRC-CBY-POS-2025-03; SRC-CBY-POS-2025-12; SRC-CBY-POS-2026-01; SRC-CBY-POS-2026-04; SRC-CBY-POS-2026-05; SRC-CBY-POS-2026-06"),
            "CLM-017": ("SRC-CBY-POS-2026-01; SRC-CBY-POS-PUBLICATION-PAGE-2026-001",
                        "SRC-CBY-POS-2026-06; SRC-CBY-POS-2026-01; SRC-CBY-POS-PUBLICATION-PAGE-2026-001")}
    for vid in ("VIS-POS-TERMINALS", "VIS-POS-TRANSACTIONS", "VIS-POS-VALUE"):
        cur = t06.get(vid, "source_dependencies")
        if not cur.endswith("SRC-CBY-POS-2025-12; SRC-CBY-POS-2026-01"):
            raise TxError(f"POS: {vid} source_dependencies end unexpectedly: {cur[-60:]!r}")
        deps[vid] = (cur, cur + "; " + "; ".join(NEW_POS))
    for oid, (old, new) in deps.items():
        t06.set(F_POS, oid, "source_dependencies", new, old)
    fids = {f"SRC-CBY-POS-{m[0]}": m[1] for m in MONTHS}
    links = json.loads(t06.get("CLM-003", "source_links"))
    if [x["source_id"] for x in links] != ["SRC-CBY-POS-2025-03", "SRC-CBY-POS-2025-12", "SRC-CBY-POS-2026-01"]:
        raise TxError("POS: CLM-003 source_links not as expected")
    old = t06.get("CLM-003", "source_links")
    links += [link(sid, fids[sid]) for sid in ("SRC-CBY-POS-2026-04", "SRC-CBY-POS-2026-05", "SRC-CBY-POS-2026-06")]
    t06.set(F_POS, "CLM-003", "source_links", json.dumps(links, ensure_ascii=False, separators=(",", ":")), old)
    old = t06.get("CLM-017", "source_links")
    links = json.loads(old)
    if [x["source_id"] for x in links] != ["SRC-CBY-POS-2026-01"]:
        raise TxError("POS: CLM-017 source_links not as expected")
    links = [link("SRC-CBY-POS-2026-06", fids["SRC-CBY-POS-2026-06"])] + links
    t06.set(F_POS, "CLM-017", "source_links", json.dumps(links, ensure_ascii=False, separators=(",", ":")), old)

    t15 = Table(s, "15_SOURCE_LIBRARY", 4)
    if any(k in t15.rows for k in NEW_POS):
        raise TxError("POS: a February–June 2026 source record already exists")
    t15.set(F_D10, "SRC-CBY-ENF-10-2026", "display_title",
            "Governor's Decision No. 10 of 2026 on the licence suspension and closure of a remittance agent (8 June 2026)",
            "Governor's Decision No. 10 of 2026 on the licence suspension and closure of a remittance agent")
    t15.set(F_D10, "SRC-CBY-ENF-10-2026", "display_title_ar",
            "قرار المحافظ رقم (10) لسنة 2026 بشأن إيقاف ترخيص وكيل حوالة وإغلاق مقره (8 يونيو 2026)",
            "قرار المحافظ رقم (10) لسنة 2026 بشأن إيقاف ترخيص وكيل حوالة وإغلاق مقره")
    t15.set(F_D10, "SRC-CBY-ENF-10-2026", "document_date", "2026-06-08", None)
    t15.set(F_D10, "SRC-CBY-ENF-10-2026", "additional_urls", json.dumps([SCAN10]), None)
    t15.set(F_D10, "SRC-CBY-ENF-10-2026", "retrieval_date", "2026-10-03", None)
    t15.set(F_D18, "SRC-CBY-ENF-18-2026", "additional_urls", json.dumps([SCAN18]), None)
    t15.set(F_D18, "SRC-CBY-ENF-18-2026", "retrieval_date", "2026-10-03", "2026-09-25")
    t15.set(F_LOC, "SRC-CBY-BANKLIST-AR-2026-001", "primary_url", "https://cby-ye.com/files/6a665add29feb.pdf",
            "https://english.cby-ye.com/files/69dfc71a51c14.pdf")
    set_json_list(t15, F_LOC, "SRC-CBY-BANKLIST-AR-2026-001", "additional_urls",
                  ["https://english.cby-ye.com/pages/14", "https://english.cby-ye.com/files/670f66ad9ce87.pdf"],
                  ["https://english.cby-ye.com/files/69dfc71a51c14.pdf", "https://english.cby-ye.com/pages/14",
                   "https://english.cby-ye.com/files/670f66ad9ce87.pdf"])
    t15.set(F_LOC, "SRC-CBY-BANKLIST-AR-2026-001", "retrieval_date", "2026-10-03", "2026-09-26")
    set_json_list(t15, F_LOC, "SRC-CBY-POS-PUBLICATION-PAGE-2026-001", "additional_urls", ["https://cby-ye.com/pages/11"], [POS_PAGE_AR])
    t15.set(F_LOC, "SRC-CBY-POS-PUBLICATION-PAGE-2026-001", "retrieval_date", "2026-10-03", "2026-09-26")
    set_json_list(t15, F_LOC, "SRC-CBY-POS-2026-01", "additional_urls", ["https://english.cby-ye.com/pages/27"],
                  ["https://english.cby-ye.com/pages/27", "https://cby-ye.com/files/6a6f950da3173.pdf", POS_PAGE_AR])

    # status events (22, PSE block) and the payment-currentness control row
    t22e = Table(s, "22_PROVIDERS_DATA", 72)
    t22e.set(F_D10, "PSE-012", "event_date", "2026-06-08", "2026-06-09")
    t22e.set(F_D10, "PSE-012", "entity_subject_state", "PRIMARY_OFFICIAL_EVENT_VERIFIED__SIGNED_DECISION_READ",
             "PRIMARY_OFFICIAL_PAGE_TITLE_VERIFIED__DATE_CROSS_CORROBORATED")
    old = t22e.get("PSE-012", "public_use")
    if not old.startswith("May show the event subject; if exact date is surfaced publicly"):
        raise TxError(f"D10: PSE-012 public_use unexpected: {old[:80]!r}")
    t22e.set(F_D10, "PSE-012", "public_use",
             "May show the exact dated event. The date is the signed decision's (Ref. 345/CBY/2026, 8 June 2026; scan "
             f"{SCAN10}); the news page that announced it is dated 9 June 2026.", old)
    t22e.set(F_D18, "PSE-015", "event_scope",
             "one exchange company, two exchange establishments and one remittance agent (PRV-EXCH-E023 to PRV-EXCH-E025 and "
             "PRV-REM-E006; names are non-public lineage)",
             "one exchange company, exchange establishments and one remittance agent, as announced")
    t22e.set(F_D18, "PSE-015", "normalized_event",
             "Governor Decision No. 18 of 2026 suspends the licences of one exchange company, two exchange establishments and "
             "one remittance agent and closes their premises.",
             "Governor Decision No. 18 of 2026 suspends licences of an exchange company, exchange establishments and a "
             "remittance agent and closes their premises")
    t22e.set(F_D18, "PSE-015", "entity_subject_state", "PRIMARY_OFFICIAL_EVENT_AND_SUBJECTS_TRANSCRIBED__NAMES_NON_PUBLIC",
             "NAMES_PRIMARY_SOURCE_PENDING")
    t22e.set(F_D18, "PSE-015", "public_use",
             "May show the dated event, decision number, class and action. The entity names, transcribed from the signed "
             f"decision (Ref. 599/CBY/2026; scan {SCAN18}), are non-public lineage and are not printed (owner note, "
             "3 October 2026, point 1).", "PUBLIC_EVENT__NAMES_WITHHELD_UNTIL_TRANSCRIBED")
    t22c = Table(s, "22_PROVIDERS_DATA", 123)
    t22c.set(F_POS, "PAYCUR-001", "latest_period_or_date", "2026-06", "2026-01")
    t22c.set(F_POS, "PAYCUR-001", "normalization_state", "NORMALIZED_IN_11_CBY_PAYMENTS__CURRENTNESS_RECHECKED_2026-10-03",
             "NORMALIZED_IN_11_CBY_PAYMENTS__CURRENTNESS_RECHECKED_2026-09-26")
    t22c.set(F_POS, "PAYCUR-001", "remaining_gap",
             "No later monthly POS object was exposed on the official Arabic payments page when rechecked on 2026-10-03; do not "
             "extrapolate July onward. The English payments page still ends at January 2026.",
             "No later monthly POS object was exposed on the official payments page when rechecked on 2026-09-26; do not "
             "extrapolate February onward.")
    t22c.set(F_POS, "PAYCUR-001", "source_url", f"{POS_PAGE_AR} ; https://english.cby-ye.com/pages/27", "https://english.cby-ye.com/pages/27")

    # analytics, master summary, catalog, indicator library, readings
    t33 = Table(s, "33_ANALYTICS_MASTER", 5)
    for da, val, old_val in (("DA-003", 1651 / 561 - 1, 1.6256684491978608), ("DA-004", 27504 / 8015 - 1, 1.9976294447910168),
                             ("DA-005", 1045 / 320 - 1, 2.94375)):
        t33.set(F_POS, da, "comparison", "Mar-2025 to Jun-2026", "Mar-2025 to Jan-2026")
        t33.set(F_POS, da, "value", val, old_val)
    t33.set(F_POS, "DA-004", "critical_caveat",
            "January and May 2026 source-displayed growth rates conflict with raw totals; raw totals and both contradictions remain "
            "visible, and no change is derived for April to May 2026.",
            "January source-displayed growth rate conflicts with raw totals; raw totals and contradiction both remain visible.")
    tct = Table(s, "33_ANALYTICS_MASTER", 107)
    tct.set(F_POS, "CON-036", "period", "reviewed 2026-10-03", "reviewed 2026-09-10")
    s.set(F_POS, "00_MASTER", 36, 2, 1651, "1473")   # get_value returns the stored text
    s.set(F_POS, "00_MASTER", 36, 4, "Jun-2026", "Jan-2026")
    s.set(F_POS, "00_MASTER", 36, 5, "SRC-CBY-POS-2026-06", "SRC-CBY-POS-2026-01")
    t16 = Table(s, "16_DATASET_CATALOG", 4)
    for ds, field, new, old in (("DS-CBY-PAYMENTS", "rows", 97, 82), ("DS-CBY-PAYMENTS", "period_max", "2026-06", "2026-01"),
                                ("DS-CBY-PAYMENTS", "source_id_count", 18, 13), ("DS-DERIVED-ANALYTICS", "period_max", "2026-06", "2026-01"),
                                ("DS-CONTRADICTIONS", "rows", 30, 28), ("DS-CONTRADICTIONS", "period_max", "2026-05", "2026-01"),
                                ("DS-PROVIDER-MASTER", "rows", 60, 56), ("DS-PROVIDER-MASTER", "source_id_count", 15, 14)):
        t16.set(F_POS if "PROVIDER" not in ds else F_D18, ds, field, new, old)
    for r, old_rows in ((55, 13), (56, 14), (57, 13)):
        s.set(F_POS, "17_INDICATOR_LIBRARY", r, 6, old_rows + 5, str(old_rows))
        s.set(F_POS, "17_INDICATOR_LIBRARY", r, 8, "2026-06", "2026-01")
    t08 = Table(s, "08_READINGS", 4)
    for cwr in ("CWR-003", "CWR-004", "CWR-009"):
        t08.set(F_POS, cwr, "last_reviewed", "2026-10-03", "2026-09-26")

    # ---- 3. row insertions (each table re-read after the insert above it) -----------------------------------------
    g19 = s.grid("19_PAYMENTS_DATA")
    last = max(i for i, r in enumerate(g19, 1) if r and str(r[0]).startswith("OBS-"))
    if g19[last - 1][0] != "OBS-00082" or any(r and r[0] for r in g19[last:]):
        raise TxError("POS: 19_PAYMENTS_DATA does not end at OBS-00082")
    s.ed.insert_rows("19_PAYMENTS_DATA", last + 1, obs_rows(83))
    t15 = Table(s, "15_SOURCE_LIBRARY", 4)
    s.ed.insert_rows("15_SOURCE_LIBRARY", t15.rows["SRC-CBY-POS-2026-01"] + 1, pos_source_rows())
    t33 = Table(s, "33_ANALYTICS_MASTER", 107)
    ctr = [k for k in t33.rows if k.startswith("CTR-")]
    if ctr[-1] != "CTR-012":
        raise TxError(f"POS: last contradiction is {ctr[-1]}")
    s.ed.insert_rows("33_ANALYTICS_MASTER", t33.rows["CTR-012"] + 1, [
        {1: "CTR-013", 2: "CBY POS terminals", 3: "2026-04 → 2026-05", 4: "Source-displayed +2.4% versus raw totals 1,583 → 1,636",
         5: "RAW_TOTALS_AND_DISPLAYED_GROWTH_CONFLICT", 6: "PRESERVE_TOTALS_AND_DISPLAYED__NO_DERIVED_CHANGE",
         7: "The published totals and the displayed +2.4% are shown; no change is derived for this month because the source "
            "contradicts itself (owner note, 3 October 2026).", 8: "/payments"},
        {1: "CTR-014", 2: "CBY POS transactions", 3: "2026-04 → 2026-05", 4: "Source-displayed +9.9% versus raw totals 30,559 → 36,201",
         5: "RAW_TOTALS_AND_DISPLAYED_GROWTH_CONFLICT", 6: "PRESERVE_TOTALS_AND_DISPLAYED__NO_DERIVED_CHANGE",
         7: "The published totals and the displayed +9.9% are shown; no change is derived for this month because the source "
            "contradicts itself (owner note, 3 October 2026).", 8: "/payments"}])
    t22 = Table(s, "22_PROVIDERS_DATA", 4)
    if any(e[0] in t22.rows for e in D18_ENTITIES):
        raise TxError("D18: an entity row already exists")
    s.ed.insert_rows("22_PROVIDERS_DATA", t22.rows["PRV-EXCH-E022"] + 1, [
        {1: eid, 2: f"{en} (English rendering by this resource; the decision names it in Arabic only)", 3: ar, 4: cls,
         5: "CBY_ADEN_EXCHANGE_REMITTANCE_SUPERVISION", 6: "STATUS_EVENT_CONFIRMED__BASE_ROSTER_MEMBERSHIP_NOT_YET_RECONCILED",
         7: "DO_NOT_INFER_BEYOND_EVENT", 8: "2026-09-24", 9: "SRC-CBY-ENF-18-2026",
         10: f"Decision No. 18 of 2026 (Ref. 599/CBY/2026, 24 September 2026), signed scan {SCAN18}; entity {i} of 4",
         11: "event-specific", 14: LINEAGE_RULE,
         15: "Transcribed Arabic first from the signed decision on 3 October 2026. Base 2026 roster membership is not reconciled at row level.",
         16: "CBY_ADEN"} for i, (eid, en, ar, cls) in enumerate(D18_ENTITIES, 1)])

    notes["POS"] = (f"DONE — {n_pos} copy cells; 15 observations OBS-00083..OBS-00097 (February–June 2026); five source records; "
                    "the May 2026 contradiction shown and not resolved (no derived change); value unit «مليار» disclosed; analytics "
                    "DA-003..005 to June 2026; CTR-013/014; PAYCUR-001; catalog and indicator counts")
    notes["D10"] = "DONE — PSE-012 and SRC-CBY-ENF-10-2026 take the instrument date 8 June 2026 and the signed scan"
    notes["D18"] = ("DONE — four entities as non-public lineage (PRV-EXCH-E023..E025, PRV-REM-E006); PSE-015 prints as the other "
                    "decisions; CLM-019 states the rule; class label corrected")
    notes["LOC"] = "DONE — bank list (July 2026 Arabic file, checked 3 October 2026); POS publication pages; January re-issue"
    notes["EDITION"] = "DONE — edition of 3 October 2026 (UI-CONTENT-VERSION and the edition-dated cells)"
    rep = s.save(out, ledger, OrderedDict([("transaction", "RC-8"), ("summary", "Truth and currentness: A1, A2, POS to June 2026, "
                                                                                "Decisions 10 and 18, locators, edition"), ("items", notes)]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except (TxError, ValueError) as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
