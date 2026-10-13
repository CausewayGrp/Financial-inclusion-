# -*- coding: utf-8 -*-
"""Close-out transaction CLOSE-6F (Stage A final instruction v5, 11 October 2026, section 7): sources (7a) and Master
hygiene (7c). Nothing here changes a public sentence; the registers and the two repository findings (7d) are repository
documents, edited beside this transaction.

  python3 close_6f.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Every write checks the exact current value. Reads: audit/close_out/v5_reads/V2 (OECD 2026, printed pages), V6 (the two
January 2026 POS files and the OECD PDF), the World Bank API fixture fixtures/wb_api_close6d_2026-10-11.json (fin34a).

- 7a SRC-OECD-YEM-RESILIENCE-001: the PDF (publisher text read 11 October 2026) and the chapter HTML as additional
  locators; the DOI landing page and the chapter HTML refuse automated requests. SRC-CBY-POS-2026-01: the 2 August 2026
  re-issue is recorded with both SHA-256 values; its values are NOT identical (four governorate cells differ), so the
  original stays primary. CR-11 is already CLOSED on main (dropped).
- 7c 24_FINDEX_CODEBOOK fin11a-f and the 27_FINDEX_SUBGROUPS compute contracts: NOT_PUBLISHED__DERIVATION_REQUIRES_D16_REVIEW.
  fin34a: the published label and both values (25_FINDEX_BASELINE, data only). 605 and 1,114: UNVERIFIED__DO_NOT_PROJECT
  in 00_MASTER and 12_VISUAL_PREVIEWS. OECD-YEM-012-014 labelled; OECD 2026 assertions recorded ATTRIBUTED__NOT_PROJECTED.
  The 2013 Enterprise Survey collateral value 281.5% was re-read and is right (284.3% is the Medium column): no change.
"""
import json, os, sys, unicodedata
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from close_lib import Session, Table, TxError, refresh_self_counts  # noqa: E402

F = "CLOSE-6F"
TODAY = "2026-10-11"
D16 = "NOT_PUBLISHED__DERIVATION_REQUIRES_D16_REVIEW"
OLD27 = "CONTROLLED_MICRODATA_WEIGHTED_COMPUTE_REQUIRED"
OECD = "SRC-OECD-YEM-RESILIENCE-001"
OECD_PDF = ("https://www.oecd.org/content/dam/oecd/en/publications/reports/2026/02/promoting-economic-resilience-in-yemen_b66657c1/"
            "81ed2898-en.pdf")
OECD_CH = ("https://www.oecd.org/en/publications/promoting-economic-resilience-in-yemen_81ed2898-en/full-report/"
           "the-financial-sector_4d6228a4.html")
POS = "SRC-CBY-POS-2026-01"
POS_B = "https://cby-ye.com/files/6a6f950da3173.pdf"
V2 = "audit/close_out/v5_reads/V2_ylg_oecd.md"


def nfc(o):
    if isinstance(o, str):
        return unicodedata.normalize("NFC", o)
    if isinstance(o, (list, tuple)):
        return type(o)(nfc(x) for x in o)
    if isinstance(o, dict):
        return OrderedDict((k, nfc(v)) for k, v in o.items())
    return o


def rows_where(s, sheet, col, value):
    return [i for i, r in enumerate(s.grid(sheet), 1) if r and len(r) >= col and r[col - 1] == value]


def one(s, sheet, col, value):
    hits = rows_where(s, sheet, col, value)
    if len(hits) != 1:
        raise TxError(f"{F}: {sheet} holds {value!r} in column {col} {len(hits)} times")
    return hits[0]


def colh(s, sheet, field, hr=4):
    h = [str(x) if x is not None else None for x in s.grid(sheet)[hr - 1]]
    if h.count(field) != 1:
        raise TxError(f"{F}: {sheet} row {hr} has no single header {field!r}")
    return h.index(field) + 1


def setc(s, fid, sheet, r, c, new, expect, label):
    s.set(f"{F}:{fid}", sheet, r, c, nfc(new), expect, label)


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    S15 = "15_SOURCE_LIBRARY"

    # ------------------------------------------------------------------------------------------------ 7a: sources
    r = one(s, S15, 1, OECD)
    ca, cn, cd = colh(s, S15, "additional_urls"), colh(s, S15, "non_public_locator_note"), colh(s, S15, "retrieval_date")
    cur = s.ed.get_value(S15, r, ca)
    urls = json.loads(cur) if cur else []
    if OECD_PDF in urls:
        raise TxError(f"{F}: {OECD} already lists the PDF")
    setc(s, "7a", S15, r, ca, json.dumps(urls + [OECD_PDF, OECD_CH]), cur, f"{OECD}.additional_urls")
    note = s.ed.get_value(S15, r, cn)
    add = ("Publisher text read 11 October 2026 from the PDF (additional URL; 71 pages, SHA-256 4ae2f699e06796b25e2e13312f125fa"
           "2582a37b9a7b0aa108bf81606a6ef33b0; printed page = PDF page - 2). The DOI landing page and the chapter HTML (additional "
           "URL, as OECD-YEM-003 to 017 cite it; URL from an oecd.org-restricted web search, content not read) refuse automated requests (Cloudflare challenge, HTTP 403, 11 October "
           "2026). Rights state unchanged; nothing reproduced.")
    setc(s, "7a", S15, r, cn, (note + " " if note else "") + add, note, f"{OECD}.non_public_locator_note")
    setc(s, "7a", S15, r, cd, TODAY, s.ed.get_value(S15, r, cd), f"{OECD}.retrieval_date")

    r = one(s, S15, 1, POS)
    cur = s.ed.get_value(S15, r, ca)
    if POS_B not in json.loads(cur):
        raise TxError(f"{F}: {POS} does not list the re-issued file")
    note = s.ed.get_value(S15, r, cn)
    add = ("January 2026 file read in two forms on 11 October 2026 (audit/close_out/v5_reads/V6_pos_oecd.md): the original, the "
           "primary locator 69b058d4bc306 (SHA-256 6036fcdc445c28289c45b86a4f3e37578fba10636251f46ebde52ac3e5025d88; the English "
           "listing's 69b05c24bea8d is byte-identical), and 6a6f950da3173 (SHA-256 52fa66f423f5072a3b73185dff24398dc289d8d3a448"
           "214420d19c61d4af46bf), re-issued in a redesigned layout on 2 August 2026 (HTTP Last-Modified and PDF creation date; "
           "the Arabic listing links it). The values are not identical: totals and sector shares match, four governorate "
           "cells differ (Aden SAR change +866% / +86.6%; Hadhramout and Shabwah YER change signs; Shabwah SAR 480 / 0). The "
           "original's figures are kept: its Aden change fits the published total, the re-issue's does not. The re-issue is "
           "image-only; its values were read visually. The Shabwah SAR cell and the two YER change signs cannot be settled "
           "from the files, and CBY-Aden has not said which version is authoritative.")
    setc(s, "7a", S15, r, cn, (note + " " if note else "") + add, note, f"{POS}.non_public_locator_note")

    # ------------------------------------------------------------------------------------------------ 7c: 24 and 27
    S24 = "24_FINDEX_CODEBOOK"
    cv, cu = colh(s, S24, "variable_name"), colh(s, S24, "use_class")
    for v in ("fin11a", "fin11b", "fin11c", "fin11d", "fin11e", "fin11f"):
        rr = one(s, S24, cv, v)
        old = s.ed.get_value(S24, rr, cu)
        if old != "PUBLIC_INDICATOR_CANDIDATE__WEIGHTED_COMPUTATION_REQUIRED":
            raise TxError(f"{F}: {v} use_class is {old!r}")
        setc(s, "7c-D16", S24, rr, cu, D16, old, f"{v}.use_class")
    rr = one(s, S24, cv, "fin34a")
    cl, cc = colh(s, S24, "candidate_public_label_en"), colh(s, S24, "critical_caveat")
    setc(s, "7c-fin34a", S24, rr, cl, "Received wages: into a bank or similar financial institution account (% age 15+)",
         s.ed.get_value(S24, rr, cl), "fin34a.candidate_public_label_en")
    cav = s.ed.get_value(S24, rr, cc)
    setc(s, "7c-fin34a", S24, rr, cc, cav + " The World Bank publishes fin34a as wages received into a bank or similar "
         "financial institution account (not any account): 3.11% of adults in 2022 and 1.75% in 2014 (open API source 28, "
         "read 11 October 2026); both held in 25_FINDEX_BASELINE as data only. The DDI labels the microdata variable "
         "'Received wage payments into an account'; the published series label is the World Bank's and was not checked "
         "against the questionnaire text.", cav, "fin34a.critical_caveat")

    S27 = "27_FINDEX_SUBGROUPS"
    cs = colh(s, S27, "current_state")
    n27 = 0
    for i, row in enumerate(s.grid(S27), 1):
        if row and str(row[0] or "").startswith("FSG-") and row[cs - 1] == OLD27:
            setc(s, "7c-D16", S27, i, cs, D16, OLD27, f"{row[0]}.current_state")
            n27 += 1
    if n27 != 95:
        raise TxError(f"{F}: {n27} compute contracts relabelled, 95 expected")

    # ------------------------------------------------------------------------------------------------ 7c: fin34a in 25
    S25 = "25_FINDEX_BASELINE"
    t25 = Table(s, S25)
    fx = json.load(open(os.path.join(HERE, "fixtures", "wb_api_close6d_2026-10-11.json"), encoding="utf-8"))
    vals = {x["date"]: x["value"] for x in fx["series"] if x["indicator"] == "fin34a"}
    if round(vals["2022"], 2) != 3.11 or round(vals["2014"], 2) != 1.75:
        raise TxError(f"{F}: the fixture's fin34a values are {vals}")
    label = "Received wages: into a bank or similar financial institution account  (% age 15+)"
    rows25 = []
    for oid, yr, v in (("WB-FINDEX-OBS-2022-160", 2022, vals["2022"]), ("WB-FINDEX-OBS-2014-FIN34A", 2014, vals["2014"])):
        if oid in t25.rows:
            raise TxError(f"{F}: 25 already holds {oid}")
        rows25.append(OrderedDict([
            ("observation_id", oid), ("indicator_code", "fin34a"), ("indicator", label), ("group", "total"), ("year", yr),
            ("value", round(v, 1)), ("unit", "percent of population ages 15+"), ("publisher", "World Bank Global Findex"),
            ("source_url", f"https://api.worldbank.org/v2/country/YEM/indicator/fin34a?source=28&format=json&date={yr}"),
            ("evidence_state", "PUBLIC_PRIMARY_AGGREGATE"),
            ("caveat", f"Data only, not projected to a page (close-out v5 7c). World Bank published value for Yemen (Global "
                       f"Findex database, open API source 28, lastupdated 2025-10-06; read 11 October 2026; "
                       f"audit/close_out/fixtures/wb_api_close6d_2026-10-11.json); unrounded value {v!r}. Wages received into a "
                       f"bank or similar financial institution account, not into any account.")]))
    h25 = t25.head
    last = max(t25.rows.values())
    s.ed.insert_rows(S25, last + 1, [{h25.index(k) + 1: v for k, v in nfc(rw).items()} for rw in rows25])
    for j, rw in enumerate(rows25):
        s.ledger.append(OrderedDict([("finding", f"{F}:7c-fin34a"), ("sheet", S25), ("row", last + 1 + j), ("col", None),
                                     ("field", rw["observation_id"]), ("old", None), ("new", json.dumps(rw)[:1500])]))

    # ------------------------------------------------------------------------------------------------ 7c: 605 and 1,114
    MARK = "UNVERIFIED__DO_NOT_PROJECT"
    for label_, v in (("Licensed money exchangers", 605), ("Money-exchange businesses", 1114)):
        rr = one(s, "00_MASTER", 1, label_)
        held = s.ed.get_value("00_MASTER", rr, 2)
        if str(held) != str(v):
            raise TxError(f"{F}: 00_MASTER {label_} does not hold {v}")
        setc(s, "7c-605", "00_MASTER", rr, 2, MARK, held, f"00_MASTER.{label_}.value")
        setc(s, "7c-605", "00_MASTER", rr, 6, f"{MARK}: OECD (2026) figure {v:,} not verified against the OECD text; held only "
             "in 29_OECD_BENCHMARKS (OECD-YEM-006/007); close-out v5 7c, 11 October 2026", s.ed.get_value("00_MASTER", rr, 6),
             f"00_MASTER.{label_}.note")
    for rr, v in ((3, 605), (4, 1114)):
        held = s.ed.get_value("12_VISUAL_PREVIEWS", rr, 18)
        if str(held) != str(v):
            raise TxError(f"{F}: 12_VISUAL_PREVIEWS r{rr} c18 does not hold {v}")
        setc(s, "7c-605", "12_VISUAL_PREVIEWS", rr, 18, MARK, held, f"12_VISUAL_PREVIEWS.r{rr}.c18")

    # ------------------------------------------------------------------------------------------------ 7c: 29_OECD_BENCHMARKS
    S29 = "29_OECD_BENCHMARKS"
    if s.ed.get_value(S29, 34, 1) != "fact_id" or s.ed.get_value(S29, 34, 12) != "reconciliation_note":
        raise TxError(f"{F}: the Yemen facts header is not on row 34")
    for k in ("OECD-YEM-012", "OECD-YEM-013", "OECD-YEM-014"):
        rr = one(s, S29, 1, k)
        setc(s, "7c-29", S29, rr, 12, "NOT_PROJECTED__DIFFERENT_UNIT_AND_WINDOW_FROM_SMEPS_AR2024: the OECD counts SMEPS "
             "beneficiaries since 2017 (micro-producers, job opportunities); SMEPS's own report counts MSMEs supported by year. "
             "Not superseded; not projected.", s.ed.get_value(S29, rr, 12), f"{k}.reconciliation_note")
    reasons = {"OECD-YEM-003": "printed p.32: 'Just 12% of adults declared having a current account …'; no survey, year or source named",
               "OECD-YEM-004": "printed p.32: '11% declared having a savings account'; no survey, year or source named",
               "OECD-YEM-005": "printed p.42, in the recommendations: 'access to mobile phones (68%)'; no survey, year or source; "
                               "the population is ambiguous (rural areas or all)"}
    for k, why in reasons.items():
        rr = one(s, S29, 1, k)
        setc(s, "7c-29", S29, rr, 11, "ATTRIBUTED__NOT_PROJECTED", s.ed.get_value(S29, rr, 11), f"{k}.verification_state")
        setc(s, "7c-29", S29, rr, 12, f"ATTRIBUTED__NOT_PROJECTED (11 October 2026; earlier state "
             f"NOT_CONFIRMED__INSTRUMENT_AND_PERIOD_UNKNOWN): the OECD's own words, {why} ({V2}). Not projected.",
             s.ed.get_value(S29, rr, 12), f"{k}.reconciliation_note")
    new29 = [
        ("OECD-YEM-019", "Informal sector", "Financial transactions outside the formal financial sector", 70, "percent (almost)",
         "currently (undated)",
         "OECD (2026) states that almost 70% of financial transactions in Yemen are currently performed outside the formal "
         "financial sector (printed p.35).",
         "تذكر منظمة التعاون الاقتصادي والتنمية (2026) أن قرابة 70% من المعاملات المالية في اليمن تجري حاليًا خارج القطاع المالي "
         "الرسمي (ص. 35).",
         "no source, date or method is given; not to be confused with 'approximately 70% of surveyed firms' (printed p.9)"),
        ("OECD-YEM-020", "Deposits", "Deposits covered by the deposit guarantee scheme", 70, "percent (some)", "undated",
         "OECD (2026) states that under the current deposit guarantee scheme some 70% of deposits would be covered in case of a "
         "bank failure (printed p.38).",
         "تذكر منظمة التعاون الاقتصادي والتنمية (2026) أن نحو 70% من الودائع ستكون مشمولة بنظام ضمان الودائع الحالي في حال تعثر "
         "بنك (ص. 38).",
         "no source or date; the deposit-guarantee law's own rules are on YSC-028, and no OECD '70%' appears on any public page (v5 test 2)"),
        ("OECD-YEM-021", "Banks", "Banks operating in Yemen", 22, "banks", "currently (undated)",
         "OECD (2026) states that 22 banks are currently operating in Yemen: 3 state-owned, 4 domestic commercial, 4 foreign-owned "
         "commercial, 5 Islamic and 6 microfinance banks (printed p.29).",
         "تذكر منظمة التعاون الاقتصادي والتنمية (2026) أن 22 بنكًا تعمل حاليًا في اليمن: 3 بنوك حكومية و4 بنوك تجارية محلية و4 بنوك "
         "تجارية مملوكة لأجانب و5 بنوك إسلامية و6 بنوك للتمويل الأصغر (ص. 29).",
         "no as-of date and no source; not reconciled with the CBY-Aden rosters"),
        ("OECD-YEM-022", "Reforms", "Box 2.1 board resolutions and decisions 7-11/2022", None, None, "2022 (box titled 2021-2022)",
         "OECD (2026), Box 2.1 (printed p.28), lists Board Resolution No. (7/2022) and No. (11/2022) and Board of Directors "
         "Decisions No. (8/2022), (9/2022) and (10/2022), and one resolution without a number.",
         "يورد الإطار 2.1 في تقرير منظمة التعاون الاقتصادي والتنمية (2026) (ص. 28) قراري المجلس رقم (7/2022) ورقم (11/2022)، "
         "وقرارات مجلس الإدارة رقم (8/2022) و(9/2022) و(10/2022)، وقرارًا للمجلس بلا رقم.",
         "the two-part numbers probably abbreviate CBY-Aden three-part numbers; not mapped until the signed decisions are read"),
        ("OECD-YEM-023", "Firms", "YLG sector shares of the amount of guarantees", None, "percent (six shares as printed; CauseWay sum 104)", "since 2017",
         "OECD (2026) gives six sector shares of the amount of YLG guarantees (36%, 29%, 19%, 9%, 7% and 4%), which sum to 104% "
         "(printed p.32).",
         "تعطي منظمة التعاون الاقتصادي والتنمية (2026) ست حصص قطاعية من مبلغ ضمانات برنامج ضمان القروض في اليمن (36% و29% و19% و9% و7% و4%) مجموعها "
         "104% (ص. 32).",
         "the shares sum to 104%, so they are shown neither as a breakdown nor renormalised"),
    ]
    rr18 = one(s, S29, 1, "OECD-YEM-018")
    for k, *_ in new29:
        if rows_where(s, S29, 1, k):
            raise TxError(f"{F}: 29 already holds {k}")
    rows = [{1: k, 2: d, 3: m, 4: v, 5: u, 6: p, 7: en, 8: ar, 9: OECD, 10: OECD_PDF, 11: "ATTRIBUTED__NOT_PROJECTED",
             12: f"ATTRIBUTED__NOT_PROJECTED (11 October 2026): {why} ({V2}). Not projected."}
            for k, d, m, v, u, p, en, ar, why in new29]
    s.ed.insert_rows(S29, rr18 + 1, [{c: x for c, x in nfc(rw).items() if x is not None} for rw in rows])
    for j, rw in enumerate(rows):
        s.ledger.append(OrderedDict([("finding", f"{F}:7c-29"), ("sheet", S29), ("row", rr18 + 1 + j), ("col", None),
                                     ("field", rw[1]), ("old", None), ("new", json.dumps(rw, ensure_ascii=False)[:1500])]))

    counts = refresh_self_counts(s, F + ":OWN-10")
    rep = s.save(out, ledger, OrderedDict([
        ("transaction", F),
        ("summary", "Stage A final instruction v5, section 7 (7a, 7c): the OECD PDF and chapter locators; the January 2026 POS "
                    "re-issue recorded (not value-identical); fin11a-f and 95 subgroup contracts relabelled for D16 review; "
                    "fin34a's published label and values; 605 and 1,114 marked not to project; OECD-YEM-012-014 labelled; five "
                    "OECD assertions recorded and three re-stated as attributed, not projected."),
        ("self_counts", counts)]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
