# -*- coding: utf-8 -*-
"""Close-out transaction CLOSE-1: decisions and truth fixes that need no new reading (brief W1). EN and AR together.

  python3 close_1.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

D1  /about/ section 6: the owner's independence statement (OWN-01), verbatim in English, written as Arabic, as its own
    labelled paragraph after "Funding". AR-035 (/about/ section 1) rides with it: the register's condition puts it in the
    transaction that touches /about/.
D3  /rights/ section 6: the software code is not openly licensed; CauseWay reserves all rights in it.
OWN-10  00_MASTER and 37_READINESS_CHECKLIST self-counts recomputed from the sheets (close_lib.refresh_self_counts);
    the validator gate CO-G01 keeps them from drifting again.
CR-03  CLM-026 said that 29 of its 32 measures have "no published value for this wave". The World Bank's open Findex
    series (source 28) publish a Yemen value for this wave for {CR03_PUBLISHED} of them; the sentence and the two others
    that rest on it now say so. The values themselves are added by CLOSE-3 (U1).
CR-04  WB-FINDEX-OBS-2022-010/011/012 pointed at the FX.OWN.TOTL.ZS page; each now points at its own series.
CR-10  SRC-WB-NFID-RFX-2026-001 (a World Bank procurement page) feeds nothing public: set non-public, its address kept in
    the non-public note (the LA-A DIV-03 pattern), so it leaves /data/ and search.
CR-12  29_OECD_BENCHMARKS (25 rows) → REJECTED__UNTRACEABLE, and the illustrative legacy block of 24_FINDEX_CODEBOOK
    (42 rows) → NON_PUBLIC__ILLUSTRATIVE, each with its reason. Gate CO-G02 keeps both out of every public output.
CR-18  The 32 rurality rows of 27_FINDEX_SUBGROUPS get their permanent reason.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from close_lib import Session, Table, TxError, refresh_self_counts, register_rows, apply_register_ar, apply_register_en  # noqa: E402

F = "CLOSE-1"
DATE = "10 October 2026"

# ---- D1 -----------------------------------------------------------------------------------------
D1_EN_ANCHOR = ("This resource is not a deliverable of any contract or partnership with the institutions whose data it "
                "presents.")
D1_EN = (D1_EN_ANCHOR + "\n\nIndependence. CauseWay develops and publishes this resource independently. It was not "
         "commissioned by, and is not reviewed or endorsed by, any institution whose data it presents.")
D1_AR_ANCHOR = "وليس هذا المورد ناتجًا عن أي عقد أو شراكة مع المؤسسات التي يعرض بياناتها."
D1_AR = (D1_AR_ANCHOR + "\n\nالاستقلال: تطوّر CauseWay هذا المورد وتنشره باستقلال. ولم تكلّف به أي مؤسسة يعرض "
         "بياناتها، ولا تراجعه أي منها ولا تؤيده.")

# ---- D3 -----------------------------------------------------------------------------------------
D3_EN_OLD = "and the software code of the repository that builds this resource, which is outside this licence."
D3_EN_NEW = ("and the software code of the repository that builds this resource, which is outside this licence: the code "
             "is not openly licensed, and CauseWay reserves all rights in it.")
D3_AR_OLD = "والشيفرة البرمجية للمستودع الذي يبني هذا المورد، فهي خارج نطاق هذه الرخصة."
D3_AR_NEW = ("والشيفرة البرمجية للمستودع الذي يبني هذا المورد، فهي خارج نطاق هذه الرخصة: إذ لا تُتاح الشيفرة بأي رخصة "
             "مفتوحة، وتحتفظ CauseWay بجميع الحقوق فيها.")

# ---- CR-03 (filled from the World Bank open series, read 10 October 2026; see audit/close_out/W0_VERIFICATION.md) -----
CR03 = json.load(open(os.path.join(HERE, "cr03_text.json"), encoding="utf-8"))

# ---- CR-04 --------------------------------------------------------------------------------------
API = "https://api.worldbank.org/v2/country/YEM/indicator/{code}?source=28"
CR04 = [("WB-FINDEX-OBS-2022-010", "save.any.t.d"), ("WB-FINDEX-OBS-2022-011", "borrow.any.t.d"),
        ("WB-FINDEX-OBS-2022-012", "g20.any")]
OLD_URL = "https://data.worldbank.org/indicator/FX.OWN.TOTL.ZS?locations=YE"

# ---- CR-12 --------------------------------------------------------------------------------------
OECD_STATE = "REJECTED__UNTRACEABLE"
OECD_REASON = ("REJECTED__UNTRACEABLE (close-out CR-12, " + DATE + "): an attached table, not an OECD/INFE publication. "
               "Its rows cannot be traced to any published OECD/INFE table: the cohort, regional and demographic "
               "averages are not figures the OECD published, and the economies listed are not the survey's set. Lineage "
               "only; never projected or published.")
CODEBOOK_STATE = "NON_PUBLIC__ILLUSTRATIVE"
CODEBOOK_REASON = ("NON_PUBLIC__ILLUSTRATIVE (close-out CR-12, " + DATE + "): a predecessor pseudo-codebook, not the "
                   "World Bank DDI. Its question wording is invented and some variables (e.g. account_mob) do not exist "
                   "in the study. Lineage only; never projected to a public page.")

# ---- CR-18 --------------------------------------------------------------------------------------
CR18 = ("No rural/urban comparison is published. The World Bank publishes no rural/urban split for Yemen; the survey's "
        "rurality classification is under method review.")


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    reg = register_rows()

    # D1 + AR-035
    s.replace_section(F + ":D1", "/about/", 6, "en", "body", D1_EN_ANCHOR, D1_EN)
    s.replace_section(F + ":D1", "/about/", 6, "ar", "body", D1_AR_ANCHOR, D1_AR)
    r35 = reg["AR-035"]
    apply_register_ar(s, F, r35)
    apply_register_en(s, F, r35, r35["en_new"], must_start="This page explains why the resource exists")

    # D3
    s.replace_section(F + ":D3", "/rights/", 6, "en", "body", D3_EN_OLD, D3_EN_NEW)
    s.replace_section(F + ":D3", "/rights/", 6, "ar", "body", D3_AR_OLD, D3_AR_NEW)

    # CR-03: CLM-026 (06_EVIDENCE_OBJECTS) — each edit is an exact, single-occurrence substring replacement
    t06 = Table(s, "06_EVIDENCE_OBJECTS")
    for field, old, new in CR03["edits"]:
        cur = t06.get("CLM-026", field)
        if not isinstance(cur, str) or cur.count(old) != 1:
            raise TxError(f"{F}:CR-03 CLM-026.{field}: substring occurs {0 if not isinstance(cur, str) else cur.count(old)} times")
        t06.set(F + ":CR-03", "CLM-026", field, cur.replace(old, new), cur)

    # CR-04
    t25 = Table(s, "25_FINDEX_BASELINE")
    for oid, code in CR04:
        if t25.get(oid, "indicator_code") != code:
            raise TxError(f"{F}:CR-04 {oid} is not {code}")
        t25.set(F + ":CR-04", oid, "source_url", API.format(code=code), OLD_URL)

    # CR-10
    t15 = Table(s, "15_SOURCE_LIBRARY")
    sid = "SRC-WB-NFID-RFX-2026-001"
    url = t15.get(sid, "primary_url")
    if url != "https://www.worldbank.org/en/about/corporate-procurement/business-opportunities/administrative-procurement":
        raise TxError(f"{F}:CR-10 unexpected primary_url {url!r}")
    t15.set(F + ":CR-10", sid, "primary_url", None, url)
    t15.set(F + ":CR-10", sid, "non_public_locator_note",
            "NON_PUBLIC (close-out CR-10, " + DATE + "): a World Bank procurement page; it feeds no public record and no "
            "procurement document is cited or named publicly. Address: " + url, None)

    # CR-12: 29_OECD_BENCHMARKS rows 6–30 (header row 5; column 13 public_use, column 14 the new quarantine_reason)
    S29 = "29_OECD_BENCHMARKS"
    g29 = s.grid(S29)
    if g29[4][12] != "public_use":
        raise TxError(f"{F}:CR-12 29 header is not where expected: {g29[4][12]!r}")
    s.set(F + ":CR-12", S29, 5, 14, "quarantine_reason", None, "29.header.quarantine_reason")
    n29 = 0
    for i in range(6, 31):
        r = g29[i - 1]
        if not r[0] or r[12] != "NON_PUBLIC__PROVENANCE_DEFECT":
            raise TxError(f"{F}:CR-12 29!r{i} is not a quarantined benchmark row: {r[:1]!r} {r[12]!r}")
        s.set(F + ":CR-12", S29, i, 13, OECD_STATE, "NON_PUBLIC__PROVENANCE_DEFECT", f"{r[0]}.public_use")
        s.set(F + ":CR-12", S29, i, 14, OECD_REASON, None, f"{r[0]}.quarantine_reason")
        n29 += 1
    if any(x and x[0] not in (None, "") for x in g29[30:]):
        raise TxError(f"{F}:CR-12 29 has rows after row 30")
    # 24_FINDEX_CODEBOOK legacy block: title row 121, rows 122–163 (columns 9 and 10 are empty in this block)
    S24 = "24_FINDEX_CODEBOOK"
    g24 = s.grid(S24)
    if not str(g24[120][0]).startswith("Uploaded predecessor Findex codebook"):
        raise TxError(f"{F}:CR-12 24 legacy block title not at row 121")
    n24 = 0
    for i in range(122, len(g24) + 1):
        r = g24[i - 1]
        if not r or not r[0]:
            continue
        if r[8] not in (None, "") or r[9] not in (None, ""):
            raise TxError(f"{F}:CR-12 24!r{i} columns 9–10 are not empty")
        s.set(F + ":CR-12", S24, i, 9, CODEBOOK_STATE, None, f"{r[0]}.legacy_state")
        s.set(F + ":CR-12", S24, i, 10, CODEBOOK_REASON, None, f"{r[0]}.legacy_reason")
        n24 += 1
    if n29 != 25 or n24 != 42:
        raise TxError(f"{F}:CR-12 counts {n29}/{n24}, expected 25/42")

    # CR-18
    t27 = Table(s, "27_FINDEX_SUBGROUPS")
    n18 = 0
    for key in list(t27.rows):
        if t27.get(key, "subgroup_dimension") == "RURALITY":
            t27.set(F + ":CR-18", key, "public_behavior", CR18, t27.get(key, "public_behavior"))
            n18 += 1
    if n18 != 32:
        raise TxError(f"{F}:CR-18 {n18} rurality rows, expected 32")

    s.regenerate_full_copy(F + ":EXF-002")
    counts = refresh_self_counts(s, F + ":OWN-10")
    rep = s.save(out, ledger, OrderedDict([
        ("transaction", F),
        ("summary", "D1 independence statement and AR-035 on /about/; D3 code licence on /rights/; OWN-10 self-counts; "
                    "CR-03 CLM-026; CR-04 locators; CR-10 NFID non-public; CR-12 quarantines; CR-18 rurality reason"),
        ("self_counts", counts)]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
