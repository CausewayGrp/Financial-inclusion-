# -*- coding: utf-8 -*-
"""Close-out transaction CLOSE-6D (Stage A final instruction v5, 11 October 2026, section 4): the truth corrections 6B-1 to
6B-5, with the repair of Reading CWR-012 (6B-5) in the same transaction as 6B-1(c). English and Arabic change together.

  python3 close_6d.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Every write checks the exact current value; the texts are in close_6d_text.py. The reads behind them (11 October 2026) are
kept in audit/close_out/v5_reads/ (V1 Findex DDI and methodology; V2 YLG Annual Report 2022 and OECD 2026; V3 the deposit
guarantee law and the consumer-protection Instructions; V4 IMF CR 26/80 and World Bank FSD 2024; V5 humanitarian, SMEPS,
IFAD and price data; V6 the POS files and the OECD locators), and the World Bank API values in
audit/close_out/fixtures/wb_api_close6d_2026-10-11.json (no microdata, no API key).

- 6B-1 People and Findex: (a) the low-income comparator: 24.5% (fiaccount.t.d) is the like-for-like aggregate, 35.2% is
  the headline account figure; the reproduction sentence and the economy count leave the public method (the derivation stays
  in 25_FINDEX_BASELINE as CauseWay's check); FY24 classification; (b) 0.4% labelled as printed, 0.6% the current database
  value; (c) the printed zero for receipt into an account and the published variable documentation, shown as found;
  (d) the OECD sentence on /finance/; (e) every flat "not asked" outside CLM-001's method becomes the observation.
- 6B-2 Firms: (a) YLG from two publishers side by side (new source SRC-YLG-AR-2022; 15 rows in 20_FIRM_FINANCE, of which
  the youth, rural and outstanding rows are held, not public; PAR not stored); (b) the SMEPS passport title; (c) the
  141-firm survey; (d) MA-004.
- 6B-3 Regulation: (a) the deposit-guarantee law (Arts 13, 31, 33) under the five constraints; (b) the consumer-protection
  Instructions read in the original: ref. 589/CBY/2023 dated 20 August 2023, announced 28 August 2023; the complaint path
  item by item (Art. 9 ج, د, ذ), scope in its own sentence; MA-006; the OECD statements shown as found; (c) Yemen Post.
- 6B-4 Remittances: (a) CLM-041; (b) CLM-007 and the 23 caveat; (c) CLM-039.
- 6B-5 CWR-012: title, question, first heading, thesis, prohibited inference, sections 2, 3, 4, 7, 8, 9 and the route
  description. The overlap bound (at least 62.7%) is CauseWay's calculation from two published shares and is held, with its
  inputs, on VIS-FINDEX-FLOW-CHANNELS.
"""
import json, os, sys, unicodedata
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from close_lib import Session, Table, TxError, refresh_self_counts, S03, COL03  # noqa: E402
import close_6d_text as T  # noqa: E402

F = "CLOSE-6D"
TODAY = "2026-10-11"
YLG_URL = "https://www.ylg-yemen.org/_files/ugd/82b85d_8562d5fe47644538ab12044bb8938bc6.pdf"


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


def append_vs(s, fid, sheet, key, drop, add):
    cur = get(s, sheet, key, "value_states")
    vs = json.loads(cur)
    for t in drop:
        n = sum(1 for e in vs if e.get("t") == t)
        if n != 1:
            raise TxError(f"{F}: {key} value_states holds {t!r} {n} times")
        vs = [e for e in vs if e.get("t") != t]
    have = {(e.get("t"), e.get("k")) for e in vs}
    for e in add:
        if (e["t"], e["k"]) not in have:
            vs.append(OrderedDict(e))
            have.add((e["t"], e["k"]))
    put(s, fid, sheet, key, "value_states", json.dumps(nfc(vs), ensure_ascii=False, separators=(",", ":")), cur)


def insert_rows(s, fid, sheet, after_row, rows, head):
    s.ed.insert_rows(sheet, after_row + 1, [{head.index(k) + 1: v for k, v in nfc(r).items() if v is not None} for r in rows])
    for j, r in enumerate(rows):
        s.ledger.append(OrderedDict([("finding", f"{F}:{fid}"), ("sheet", sheet), ("row", after_row + 1 + j), ("col", None),
                                     ("field", r[head[0]]), ("old", None), ("new", json.dumps(r, ensure_ascii=False)[:1500])]))


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    O6, V11 = "06_EVIDENCE_OBJECTS", "11_VISUAL_LIBRARY"

    # ------------------------------------------------------------------------------------------------ cell edits
    for fid, route, order, lang, field, old, new in T.SEC:
        s.replace_section(f"{F}:{fid}", route, order, lang, field, nfc(old), nfc(new))
    for fid, route, order, lang, field, must, new in T.SECW:
        s.rewrite_section(f"{F}:{fid}", route, order, lang, field, nfc(new), nfc(must))
    for fid, sheet, key, field, old, new in T.CELL:
        rep(s, fid, sheet, key, field, old, new)
    for fid, sheet, key, field, must, new in T.WHOLE:
        whole(s, fid, sheet, key, field, must, new)
    for key, (drop, add) in T.VS.items():
        append_vs(s, "VS", O6, key, drop, add)

    # ------------------------------------------------------------------------------------------------ 6B-5: CWR-012
    for f, new in T.CWR_SET.items():
        whole(s, "6B-5", "08_READINGS", "CWR-012", f, T.CWR_OLD_START[f], new)
    r9 = [i for i, r in enumerate(s.grid("09_READING_SECTIONS"), 1) if r and r[0] == "CWR-012" and r[1] == 1]
    if len(r9) != 1:
        raise TxError(f"{F}: 09 holds CWR-012 section 1 {len(r9)} times")
    for col, (old, new) in ((4, T.S1_HEAD[0]), (5, T.S1_HEAD[1])):
        s.set(f"{F}:6B-5", "09_READING_SECTIONS", r9[0], col, nfc(new), old, "CWR-012#s1.heading")
    for f, must, new in (("meta_description_en", T.META_OLD_START[0], T.META_EN),
                         ("meta_description_ar", T.META_OLD_START[1], T.META_AR)):
        whole(s, "6B-5", "02_SITE_MAP", T.R, f, must, new)
    # the bound's record also names the World Bank's published variable documentation (SRC-WB-FINDEX-001)
    dep = get(s, O6, "VIS-FINDEX-FLOW-CHANNELS", "source_dependencies")
    if "SRC-WB-FINDEX-001" not in dep:
        put(s, "6B-1c", O6, "VIS-FINDEX-FLOW-CHANNELS", "source_dependencies", dep + "; SRC-WB-FINDEX-001", dep)
        lk = get(s, O6, "VIS-FINDEX-FLOW-CHANNELS", "source_links")
        links = json.loads(lk or "[]")
        links.append({"source_id": "SRC-WB-FINDEX-001", "url": Table(s, "15_SOURCE_LIBRARY").get("SRC-WB-FINDEX-001", "primary_url"),
                      "audit_state": "PASS_AUTHORITY_OR_PROVIDER_LOCATOR"})
        put(s, "6B-1c", O6, "VIS-FINDEX-FLOW-CHANNELS", "source_links", json.dumps(links, separators=(",", ":")), lk)

    # ------------------------------------------------------------------------------------------------ 6B-1(a)(b): 25_FINDEX_BASELINE
    S25 = "25_FINDEX_BASELINE"
    lic = "WB-FINDEX-CTX-2021-LIC"
    rep(s, "6B-1a", S25, lic, "group", "low-income economies (19 economies with a 2021-wave observation, Yemen included)",
        "low-income economies (World Bank FY24 income classification; Yemen included)")
    put(s, "6B-1a", S25, lic, "year", "2021 (database year; the same survey wave as Yemen's 2022 observation)", "2021 wave")
    rep(s, "6B-1a", S25, lic, "caveat",
        "reproduced as the adult-population-weighted mean of the 19 economies the file classes Low income with a 2021-wave "
        "observation, Yemen's 2022 observation included.",
        "CauseWay's check, not for publication: reproduced as the adult-population-weighted mean of the 19 economies the file "
        "classes Low income with a 2021-wave observation, Yemen's 2022 observation included; the publisher states no economy "
        "count for this aggregate, so no count is printed (CLOSE-6D). The same value on the open API: account.t.d, LIC, date "
        "2021, 35.1821646573129 (read 11 October 2026; " + T.FX + "). The aggregate for mobileaccount.t.d (18.3073126606225) "
        "is not published by this resource: in the publisher's aggregation Yemen's missing mobile-money value enters the "
        "numerator as zero while Yemen's adults stay in the denominator (CauseWay's reconstruction, not a published statement).")
    t25 = Table(s, S25)
    h25 = t25.head
    last25 = max(t25.rows.values())
    rows25 = [
        OrderedDict([("observation_id", "WB-FINDEX-CTX-2021-LIC-FI"), ("indicator_code", "fiaccount_t_d"),
                     ("indicator", "Bank or similar financial institution account (% age 15+)"),
                     ("group", "low-income economies (World Bank FY24 income classification; Yemen included)"),
                     ("year", "2021 (database year; the same survey wave as Yemen's 2022 observation)"), ("value", 24.5),
                     ("unit", "percent of population ages 15+"), ("publisher", "World Bank Global Findex"),
                     ("source_url", "https://api.worldbank.org/v2/country/LIC/indicator/fiaccount.t.d?date=2021&format=json&source=28"),
                     ("evidence_state", "PUBLIC_PRIMARY_AGGREGATE_CONTEXT"),
                     ("caveat", "World Bank aggregate 24.4577497822049 (open API, source 28, LIC, date 2021, lastupdated "
                                "2025-10-06; read 11 October 2026; " + T.FX + "). The like-for-like comparator for Yemen's "
                                "11.9% (fiaccount.t.d equals account.t.d for Yemen). The database's metadata name the FY24 "
                                "classification (2022 Atlas GNI per capita of $1,135 or less) and state no economy count. "
                                "Context only: not a benchmark, target or ranking (CLOSE-6D, 6B-1(a)).")]),
        OrderedDict([("observation_id", "WB-FINDEX-OBS-2014-FIN22A"), ("indicator_code", "fin22a"),
                     ("indicator", "Borrowed from a formal bank or similar financial institution (% age 15+)"),
                     ("group", "total"), ("year", 2014), ("value", 0.6), ("unit", "percent of population ages 15+"),
                     ("publisher", "World Bank Global Findex"),
                     ("source_url", "https://api.worldbank.org/v2/country/YEM/indicator/fin22a?date=2014&format=json&source=28"),
                     ("evidence_state", "PUBLIC_PRIMARY_AGGREGATE"),
                     ("caveat", "Current database value 0.602877248196788 (open API, source 28, lastupdated 2025-10-06; read "
                                "11 October 2026; " + T.FX + "). The Little Data Book on Financial Inclusion 2015 printed 0.4% "
                                "for the same 2014 measure (p.160); any comparison of 2014 with 2022 (1.8%) uses 0.6% "
                                "(CLOSE-6D, 6B-1(b)).")]),
    ]
    for r in rows25:
        if r["observation_id"] in t25.rows:
            raise TxError(f"{F}: 25 already holds {r['observation_id']}")
    insert_rows(s, "6B-1", S25, last25, rows25, h25)

    # ------------------------------------------------------------------------------------------------ 6B-2(a): YLG source and rows
    t15 = Table(s, "15_SOURCE_LIBRARY")
    h15 = t15.head
    if "SRC-YLG-AR-2022" in t15.rows:
        raise TxError(f"{F}: 15 already holds SRC-YLG-AR-2022")
    for k, i in t15.rows.items():
        for c in ("primary_url", "additional_urls"):
            if "ylg-yemen" in str(t15.get(k, c) or ""):
                raise TxError(f"{F}: {k} already carries a YLG locator")
    src = OrderedDict([
        ("source_id", "SRC-YLG-AR-2022"), ("primary_url", YLG_URL), ("datasets_or_use", "DS-FIRM-FINANCE"), ("row_count", 15),
        ("display_title", "Yemen Loan Guarantee Program (YLGP) Annual Report 2022"), ("publisher", "Yemen Loan Guarantee Program"),
        ("public_card_state", "CITATION_CARD"), ("display_title_ar", "التقرير السنوي لبرنامج ضمان القروض في اليمن لعام 2022"),
        ("non_public_locator_note", "Source type PRIMARY_PROGRAMME_REPORT. Fiscal year 2022; pages used 4, 8, 9, 14-17, 29-31 (the 12th partner p.9; the partner chart p.31). No "
                                    "publication date is printed (p.35 '© Copyright reserved 2022'; the file's metadata give 16 "
                                    "April 2023). Amounts are in thousand YER (p.14). Read 11 October 2026 (35 pages, SHA-256 "
                                    "fc6651b7bf87f299243c1b78cdf3a5507b5702bfd6bb8b23cc4419a5f9c3fb22). Facts cited; nothing "
                                    "reproduced."),
        ("rights_state", "NOT_ASSESSED"), ("attribution_requirement", "Facts cited; nothing reproduced"),
        ("retrieval_date", TODAY), ("publisher_ar", "برنامج ضمان القروض في اليمن"), ("document_label", "Annual report"),
        ("document_label_ar", "تقرير سنوي"),
    ])
    insert_rows(s, "6B-2a", "15_SOURCE_LIBRARY", max(t15.rows.values()), [src], h15)

    t20 = Table(s, "20_FIRM_FINANCE")
    h20 = t20.head
    base = OrderedDict([("source_id", "SRC-YLG-AR-2022"), ("survey_wave", "YLGP Annual Report 2022"),
                        ("universe", "Letters of guarantee issued by the Yemen Loan Guarantee Program through its partner "
                                     "financial institutions"),
                        ("formality", "PROGRAMME"), ("geography", "Programme scope as reported"),
                        ("evidence_type", "SOURCE_REPORTED"), ("calculation_state", "SOURCE_REPORTED"), ("source_url", YLG_URL)])
    pub = "PROGRAMME_REPORTED__GUARANTEES_NOT_FIRMS"
    held = "HELD_NOT_PUBLIC"
    spec = [
        ("001", "2022", "FFM-021", "Letters of guarantee issued", 3387, "letters of guarantee", None, None, "pp.4, 8, 14", pub,
         "Counts guarantees, not firms. Public on CLM-059."),
        ("002", "2022", "FFM-022", "Guarantee amount", 6397627.81, "YER thousand", None, None, "p.14 (Guarantees Amount, Thousand YER)",
         pub, "Nominal rials as reported; the report does not say in which area's rial; not converted. Printed rounded as YER "
              "6.4 billion (pp.4, 8)."),
        ("003", "2022", "FFM-023", "Guaranteed loans amount (covered principal)", 9371245.29, "YER thousand", None, None,
         "p.14 (Guaranteed Loans Amount, Thousand YER)", pub, "Nominal rials as reported; printed rounded as YER 9.4 billion."),
        ("004", "2022", "FFM-024", "Letters of guarantee, gender table row FEMALE", 693, "letters of guarantee", 3387, 693, "p.15",
         pub, "Row label 'FEMALE'; the text says 'women-led MSMEs' (about 20%); the report defines neither term."),
        ("005", "2022", "FFM-025", "Partner financial institutions (total)", 12, "institutions", None, None, "pp.4, 17", pub,
         "Annex III shows 12 partners; 11 appear in the 2022 guarantee table."),
        ("006", "2018", "FFM-026", "Letters of guarantee issued, by year (Annex I)", 301, "letters of guarantee", None, None, "p.29", pub, None),
        ("007", "2019", "FFM-026", "Letters of guarantee issued, by year (Annex I)", 691, "letters of guarantee", None, None, "p.29", pub, None),
        ("008", "2020", "FFM-026", "Letters of guarantee issued, by year (Annex I)", 1270, "letters of guarantee", None, None, "p.29", pub, None),
        ("009", "2021", "FFM-026", "Letters of guarantee issued, by year (Annex I)", 1327, "letters of guarantee", None, None, "p.29", pub, None),
        ("010", "2022", "FFM-026", "Letters of guarantee issued, by year (Annex I)", 3387, "letters of guarantee", None, None, "p.29", pub, None),
        ("011", "2018-2022", "FFM-027", "Sum of the yearly counts 2018-2022 (calculated here)", 6976, "letters of guarantee", None,
         None, "p.29 (sum not printed)", pub, "CauseWay sum of the Annex I yearly counts; each Annex I split also totals 6,976."),
        ("012", "2022", "FFM-028", "Letters of guarantee, row YOUTH", 1907, "letters of guarantee", 3387, 1907, "p.16", held,
         "Held, not public (instruction v5, 6B-2(a)); the report states no upper youth age."),
        ("013", "2022", "FFM-029", "Letters of guarantee, row Rural", 1748, "letters of guarantee", 3387, 1748, "p.17", held,
         "Held, not public (instruction v5, 6B-2(a))."),
        ("014", "as of date not stated", "FFM-030", "Outstanding guarantees (glance panel)", 3526, "letters of guarantee", None,
         None, "p.4", held + "__AS_OF_DATE_NOT_STATED", "Held, not public: the report states no as-of date."),
        ("015", "as of date not stated", "FFM-031", "Outstanding guarantees amount (glance panel, 'YER 4.6B')", 4.6, "YER billion",
         None, None, "p.4", held + "__AS_OF_DATE_NOT_STATED", "Held, not public: no as-of date and no stated basis. PAR (p.20) "
                                                              "is not stored: its base is not stated."),
    ]
    rows20 = []
    for n, per, mid, lab, val, unit, den, num, page, comp, cav in spec:
        r = OrderedDict(base)
        r.update([("observation_id", f"FFO-YLG-2022-{n}"), ("period", per), ("metric_id", mid), ("metric_label", lab),
                  ("value", val), ("unit", unit), ("denominator_n", den), ("numerator_n", num), ("source_page_figure", page),
                  ("comparability_state", comp), ("caveat", cav)])
        rows20.append(OrderedDict((k, r.get(k)) for k in h20 if k in r))
    insert_rows(s, "6B-2a", "20_FIRM_FINANCE", max(t20.rows.values()), rows20, h20)

    dep = get(s, O6, "CLM-059", "source_dependencies")
    put(s, "6B-2a", O6, "CLM-059", "source_dependencies", dep + "; SRC-YLG-AR-2022", dep)
    lk = get(s, O6, "CLM-059", "source_links")
    links = json.loads(lk)
    links.append({"source_id": "SRC-YLG-AR-2022", "url": YLG_URL, "audit_state": "PASS_AUTHORITY_OR_PROVIDER_LOCATOR"})
    put(s, "6B-2a", O6, "CLM-059", "source_links", json.dumps(links, separators=(",", ":")), lk)
    ei = get(s, "07_PUBLIC_CLAIMS", "CLM-059", "evidence_inputs")
    put(s, "6B-2a", "07_PUBLIC_CLAIMS", "CLM-059", "evidence_inputs",
        json.dumps(json.loads(ei) + ["SRC-YLG-AR-2022", "20_FIRM_FINANCE"]).replace(", ", ","), ei)
    # 29_OECD_BENCHMARKS: the OECD's YLG facts stay, with the reconciliation note (column 12)
    S29 = "29_OECD_BENCHMARKS"
    hr = row_of(s, S29, "fact_id")
    if s.ed.get_value(S29, hr, 12) is None:
        s.set(f"{F}:6B-2a", S29, hr, 12, "reconciliation_note", None, "29.header")
    for k in ("OECD-YEM-015", "OECD-YEM-016", "OECD-YEM-017"):
        s.set(f"{F}:6B-2a", S29, row_of(s, S29, k), 12, "NOT_RECONCILED_WITH_SRC-YLG-AR-2022: cutoff and definitions differ; "
              "not combined", s.ed.get_value(S29, row_of(s, S29, k), 12), f"{k}.reconciliation_note")

    # ------------------------------------------------------------------------------------------------ 6B-3(a): YSC-028
    S14 = "14_SYSTEM_CHRONOLOGY"
    put(s, "6B-3a", S14, "YSC-028", "fi_relevance_en", T.DI_EN, T.DI_OLD[0])
    put(s, "6B-3a", S14, "YSC-028", "fi_relevance_ar", T.DI_AR, T.DI_OLD[1])
    append_vs(s, "6B-3a", S14, "YSC-028", [], T.DI_VS)

    # ------------------------------------------------------------------------------------------------ 6B-3(b): the complaint path
    for key in ("CLM-011", "VIS-FCP-REDRESS-PATH"):
        for f, new in T.CP_DEF.items():
            cur = get(s, O6, key, f)
            if not cur:
                raise TxError(f"{F}: {key}.{f} is empty")
            put(s, "6B-3b", O6, key, f, new, cur)
        append_vs(s, "6B-3b", O6, key, [], T.CP_VS + [{"t": "1", "k": "v", "s": "LOCATOR"},
                                                      {"t": "11 October 2026", "k": "d", "s": "SITE"}])
    whole(s, "6B-3b", O6, "CLM-011", "summary_en", "A 2024 consumer-protection awareness brochure", T.CP_EN)
    whole(s, "6B-3b", O6, "CLM-011", "summary_ar", "يصف كتيّب توعوي لحماية المستهلك", T.CP_AR)
    rep(s, "6B-3b", O6, "CLM-011", "limitations_en", *T.CLM011_LIM[0])
    rep(s, "6B-3b", O6, "CLM-011", "limitations_ar", *T.CLM011_LIM[1])
    for sheet, fe, fa in ((O6, "summary_en", "summary_ar"), (V11, "accessible_summary_en", "accessible_summary_ar")):
        whole(s, "6B-3b", sheet, "VIS-FCP-REDRESS-PATH", fe, "A 2024 consumer-protection awareness brochure", T.VIS_CP_EN)
        whole(s, "6B-3b", sheet, "VIS-FCP-REDRESS-PATH", fa, "يصف كتيّب توعوي لحماية المستهلك", T.VIS_CP_AR)
    for sheet, fe, fa in ((O6, "limitations_en", "limitations_ar"), (V11, "prohibited_inference_en", "prohibited_inference_ar")):
        rep(s, "6B-3b", sheet, "VIS-FCP-REDRESS-PATH", fe, *T.VIS_LIM[0])
        rep(s, "6B-3b", sheet, "VIS-FCP-REDRESS-PATH", fa, *T.VIS_LIM[1])
    for f, new in T.VIS11.items():
        put(s, "6B-3b", V11, "VIS-FCP-REDRESS-PATH", f, new, get(s, V11, "VIS-FCP-REDRESS-PATH", f))
    for k, (text, trig) in T.FCP_ARCH.items():
        r = row_of(s, "31_REFORMS_REGULATION", k)
        for col, new in ((2, T.INSTR), (5, text), (6, trig), (9, T.INSTR_URL)):
            if new is not None:
                s.set(f"{F}:6B-3b", "31_REFORMS_REGULATION", r, col, nfc(new), s.ed.get_value("31_REFORMS_REGULATION", r, col),
                      f"{k}.c{col}")
    r = row_of(s, "31_REFORMS_REGULATION", "REF-FCP-001")
    s.set(f"{F}:6B-3b", "31_REFORMS_REGULATION", r, 2, T.REF_FCP["date"][1], T.REF_FCP["date"][0], "REF-FCP-001.date")
    cur = s.ed.get_value("31_REFORMS_REGULATION", r, 5)
    s.set(f"{F}:6B-3b", "31_REFORMS_REGULATION", r, 5, cur + T.REF_FCP["text_add"], cur, "REF-FCP-001.text")
    s.set(f"{F}:6B-3b", "31_REFORMS_REGULATION", r, 8, T.REF_FCP["url"][1], T.REF_FCP["url"][0], "REF-FCP-001.url")
    for f, (old, new) in T.INSTR_SRC.items():
        put(s, "6B-3b", "15_SOURCE_LIBRARY", T.INSTR, f, new, old)
    put(s, "6B-3b", "10_MEASUREMENT_AGENDA", "MA-006", "current_evidence_en", T.MA006[0][1], T.MA006[0][0])
    put(s, "6B-3b", "10_MEASUREMENT_AGENDA", "MA-006", "current_evidence_ar", T.MA006[1][1], T.MA006[1][0])
    for sheet, fe, fa in ((O6, "summary_en", "summary_ar"), (V11, "accessible_summary_en", "accessible_summary_ar")):
        rep(s, "6B-3b", sheet, "VIS-OECD-FCP-TIMELINE", fe, *T.OECD_FCP_ANN[0])
        rep(s, "6B-3b", sheet, "VIS-OECD-FCP-TIMELINE", fa, *T.OECD_FCP_ANN[1])
        rep(s, "6B-3b", sheet, "VIS-OECD-FCP-TIMELINE", fe, *T.OECD_FCP[0])
        rep(s, "6B-3b", sheet, "VIS-OECD-FCP-TIMELINE", fa, *T.OECD_FCP[1])
    append_vs(s, "6B-3b", O6, "VIS-OECD-FCP-TIMELINE", [], T.OECD_VS)
    for lang, i in (("en", 0), ("ar", 1)):
        s.replace_section(f"{F}:6B-3b", "/reforms/", 3, lang, "body", nfc(T.REF_S3[i][0]), nfc(T.REF_S3[i][1]))
        s.set_section(f"{F}:6B-3b", "/reforms/", 3, lang, "heading", nfc(T.REF_S3_HEAD[i][1]), T.REF_S3_HEAD[i][0])

    # ------------------------------------------------------------------------------------------------ 6B-4(b): the 23 caveat
    for k in T.RMO_IDS:
        rep(s, "6B-4b", "23_REMITTANCES", k, "caveat_en", T.RMO_OLD, T.RMO_NEW)

    # ------------------------------------------------------------------------------------------------ checks before saving
    for route in (T.R, "/evidence/CLM-028/", "/evidence/CLM-059/"):
        for f in ("meta_description_en", "meta_description_ar"):
            v = get(s, "02_SITE_MAP", route, f)
            if len(v) > 200:
                raise TxError(f"{F}: {route} {f} is {len(v)} characters (F6-G01 allows 200)")

    counts = refresh_self_counts(s, F + ":OWN-10")
    rep_ = s.save(out, ledger, OrderedDict([
        ("transaction", F),
        ("summary", "Stage A final instruction v5, section 4: truth corrections 6B-1 to 6B-5, with the repair of Reading "
                    "CWR-012 in the same transaction as 6B-1(c); new source SRC-YLG-AR-2022, 15 YLG rows in 20_FIRM_FINANCE "
                    "and two rows in 25_FINDEX_BASELINE."),
        ("self_counts", counts)]))
    print(json.dumps({k: rep_[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
