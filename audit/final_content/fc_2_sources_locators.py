# -*- coding: utf-8 -*-
"""Final content pass, transaction FC-2: source locators — two broken links fixed, the missing originals added.

  python3 fc_2_sources_locators.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Finding FC-2:A2-LOCATORS (owner message of 4 October 2026, block A). Every locator written here was opened from this
session on 4 October 2026 and its HTTP status, content type and byte size observed; where a document date or an issue
number is recorded, it was read off the document itself, not inferred from a URL, a filename or a listing label.

WHAT THE SWEEP FOUND, against the owner's list

1. BROKEN, and worse than a dead link. SRC-CBY-SANAA-C14-2024 pointed at
   https://www.ecoi.net/en/file/local/2117585/n2425953.pdf, which is not Circular No. 14 of 2024 at all: it is the
   537-page final report of the UN Panel of Experts on Yemen, UN document S/2024/731, 11 October 2024, on a mirror.
   The circular is inside it, reproduced as an image at printed page 114, "Figure 28.2 — Circular No 14 dated
   26 March 2024 issued by CBY, Sana'a", captioned "Source: Panel". No public locator for the circular itself could be
   found: the Sana'a central bank's own domain is unreachable from here, and cbyemen.com has been repurposed and now
   serves an unrelated commercial site, so it must never be cited. The honest fix is therefore not to delete the
   locator but to say what it is: the UN's own address replaces the mirror, and the record states the page the
   circular is reproduced on, so a reader is sent to a document that really contains it.

2. BROKEN. SRC-CBY-SANAA-C12-2024's locator returns HTTP 404 (observed twice). The same host serves the document under
   a different filename, which returns 200 and a 775,973-byte PDF of 3 pages. This was not on the owner's list; the
   sweep found it.

3. GENUINELY MISSING, and added: the Central Bank of Yemen — Aden "Monetary and Financial Developments" issues for
   2021 and 2022, and the pages the bank publishes them and its regulations on. All 686 observations of the monetary
   series were traced to one source record, the May 2026 issue, so a reader checking a 2021 or 2022 monthly value was
   sent to a document published four years later. Thirteen issues now stand with it. Each URL was opened; the issue
   number was read from the document, and May 2022 prints none, so none is claimed for it.

4. ALREADY PRESENT, contrary to the brief's premise, and so not added: the SFD newsletters of 2012-2020 (twelve
   records, SRC-SFD-Q1-2012-001 … SRC-SFD-Q4-2020-001, each with a locator) and IGC "From cash to capital"
   (SRC-IGC-AIDDATA-REMIT-YEM-2026). Edition 1 or 2 had closed them. The IGC record held only its landing page, so the
   two documents behind it — the 90-page final report and the 12-page policy brief, both opened here — are added to it.

5. LEFT OUT, with the reason recorded: the SDRPY deposit notice. sdrpy.gov.sa could not be opened from this session at
   all (TLS failure on every attempt). The Saudi Press Agency item that reports the deposit does open, but its body is
   rendered by JavaScript and only its headline could be read from here, so the deposit's amount, date and recipient
   could not be read in the original. Nothing is published from it, and it is carried to the handover as a source that
   needs a human with a browser. Also left out for the same reason: the OECD youth paper, the World Bank FASTT paper
   and the UNDP FMIIP project page, each of which answers an automated request with a bot challenge.

6. DATES. A finding worth stating plainly: most of the CBY-Aden documents this resource cites print no date of their
   own — only a period or a year. Those were checked one by one and no date was invented for them; where a date is
   recorded below it is printed on the document.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "release_candidate"))
from rc_lib import Session, Table, TxError  # noqa: E402

F = "FC-2:A2-LOCATORS"
S15 = "15_SOURCE_LIBRARY"

UN_PDF = "https://documents.un.org/doc/undoc/gen/n24/259/53/pdf/n2425953.pdf"
ECOI = "https://www.ecoi.net/en/file/local/2117585/n2425953.pdf"
C12_OLD = ("https://yemeneco.org/wp-content/uploads/2024/03/"
           "تعميم-رقم-12-خدمات-"
           "البنوك-والمؤسسات-"
           "المالية-العاملة-"
           "في-خدمات-الحوالات-"
           "الخارجية.pdf")
C12_NEW = ("https://yemeneco.org/wp-content/uploads/2024/03/"
           "تعميم_رقم_12_خدمات_"
           "البنوك_والمؤسسات_"
           "المالية_المشغلة_"
           "لخدمات_الحوالات.pdf")

SERIES_INDEX = "https://english.cby-ye.com/researchandstatistics"
CBY_PAGES = ["https://cby-ye.com/publicationsandcirculars", "https://english.cby-ye.com/publicationsandcirculars",
             "https://cby-ye.com/rulesandregulations", "https://english.cby-ye.com/rulesandregulations",
             "https://cby-ye.com/researchandstatistics", SERIES_INDEX]
# (month label, printed issue number or None, file id, bytes observed). Opened 2026-10-04; issue number read from the
# document's own header. May 2022 prints no issue number, so none is claimed.
ISSUES = [("December 2021", "1", "630342f7c26ae", 2045202), ("January 2022", "2", "6303431ed26c1", 2064757),
          ("February 2022", "3", "63034338c577c", 2061931), ("March 2022", "4", "63033876c3f92", 2005502),
          ("April 2022", "5", "630338c8b5600", 2004667), ("May 2022", None, "6303391a7e9e7", 1664491),
          ("June 2022", "7", "634f8fcb92d5f", 1759599), ("July 2022", "8", "634f90085bdcd", 1802087),
          ("August 2022", "9", "634f9042dbb84", 1738055), ("September 2022", "10", "63aadf8d70ae1", 1745646),
          ("October 2022", "11", "63aadfbe154e8", 1759228), ("November 2022", "12", "63d231418c14b", 1756231),
          ("December 2022", "13", "64115abe770bb", 1755844)]
IGC_DOCS = ["https://www.theigc.org/sites/default/files/2026-02/YEM-24338%20From%20cash%20to%20capital.pdf",
            "https://www.theigc.org/sites/default/files/2026-02/"
            "From-Cash-to-Capital-Leveraging-Remittances-for-Yemens-Economic-Future.pdf"]

# the two papers the sweep added. Titles, issuing bodies and dates read from each publication's own page.
NEW_SOURCES = [
    OrderedDict([
        ("source_id", "SRC-SANAA-CTR-EMONEY-2022"),
        ("primary_url", "https://deeproot.consulting/en/publications/"
                        "challenges-and-prospects-for-electronic-money-and-payment-systems-in-yemen"),
        ("additional_urls", json.dumps(["https://deeproot.consulting/en/publications/73/download"])),
        ("datasets_or_use", "DS-K04-PUBLICATION-BENCHMARK"),
        ("row_count", 1),
        ("display_title", "Challenges and Prospects for Electronic Money and Payment Systems in Yemen (March 2022)"),
        ("display_title_ar", "تحديات وآفاق النقود "
                             "الإلكترونية ونظم "
                             "المدفوعات في اليمن "
                             "(مارس 2022)"),
        ("publisher", "DeepRoot Consulting"),
        ("publisher_ar", "ديب روت للاستشارات"),
        ("public_card_state", "CITATION_CARD"),
        ("rights_state", "NOT_ASSESSED"),
        ("retrieval_date", "2026-10-04"),
        ("document_type", "research-or-policy-paper"),
        ("document_label", "Research or policy paper"),
        ("document_label_ar", "ورقة بحثية أو سياساتية"),
        ("document_date", "2022-03-11"),
        ("evidence_roles", "context and interpretation"),
    ]),
    OrderedDict([
        ("source_id", "SRC-SANAA-CTR-MFB-2024"),
        ("primary_url", "https://deeproot.consulting/en/publications/"
                        "enhancing-the-role-of-microfinance-banks-for-sustainable-impact-in-yemen"),
        ("additional_urls", json.dumps(["https://deeproot.consulting/en/publications/83/download"])),
        ("datasets_or_use", "DS-K04-PUBLICATION-BENCHMARK"),
        ("row_count", 1),
        ("display_title", "Enhancing the Role of Microfinance Banks for Sustainable Impact in Yemen "
                          "(Sana'a Center Economic Unit, 23 September 2024)"),
        ("display_title_ar", "تعزيز دور بنوك "
                             "التمويل الأصغر "
                             "لتحقيق أثر مستدام "
                             "في اليمن (الوحدة "
                             "الاقتصادية في مركز "
                             "صنعاء، 23 سبتمبر 2024)"),
        ("publisher", "Sana'a Center Economic Unit, published by DeepRoot Consulting"),
        ("publisher_ar", "الوحدة الاقتصادية "
                         "في مركز صنعاء، نشرتها "
                         "ديب روت للاستشارات"),
        ("public_card_state", "CITATION_CARD"),
        ("rights_state", "NOT_ASSESSED"),
        ("retrieval_date", "2026-10-04"),
        ("document_type", "research-or-policy-paper"),
        ("document_label", "Research or policy paper"),
        ("document_label_ar", "ورقة بحثية أو سياساتية"),
        ("document_date", "2024-09-23"),
        ("evidence_roles", "context and interpretation"),
    ]),
]


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    t15 = Table(s, S15, 4)

    # 1. the wrong document: the UN's own address, and the page the circular is reproduced on
    t15.set(F, "SRC-CBY-SANAA-C14-2024", "primary_url", UN_PDF, ECOI)
    t15.set(F, "SRC-CBY-SANAA-C14-2024", "additional_urls",
            json.dumps(["https://docs.un.org/en/S/2024/731", ECOI]), None)
    t15.set(F, "SRC-CBY-SANAA-C14-2024", "non_public_locator_note",
            "Circular No. 14 of 2024 of the Central Bank of Yemen in Sana'a has no public locator of its own that "
            "could be opened on 4 October 2026. The locator here is the document that reproduces it: the final report "
            "of the UN Panel of Experts on Yemen, UN document S/2024/731 of 11 October 2024, where the circular is "
            "reproduced as an image at printed page 114, \"Figure 28.2 - Circular No 14 dated 26 March 2024 issued by "
            "CBY, Sana'a\", captioned \"Source: Panel\". Cite the circular only through that page, never as if the "
            "Panel's report were the circular. The earlier locator was a mirror of the same UN report and is kept as "
            "an additional address. cbyemen.com must not be cited: that domain has been repurposed and serves an "
            "unrelated commercial site.", None)
    t15.set(F, "SRC-CBY-SANAA-C14-2024", "issuer",
            "Central Bank of Yemen, Sana'a (the circular); UN Security Council Panel of Experts on Yemen (the "
            "document that reproduces it)", None)
    t15.set(F, "SRC-CBY-SANAA-C14-2024", "document_date", "2024-03-26", None)

    # 2. the 404
    t15.set(F, "SRC-CBY-SANAA-C12-2024", "primary_url", C12_NEW, C12_OLD)
    t15.set(F, "SRC-CBY-SANAA-C12-2024", "additional_urls",
            json.dumps(["https://yemeneco.org/archives/77824"]), None)
    t15.set(F, "SRC-CBY-SANAA-C12-2024", "retrieval_date", "2026-10-04", None)
    t15.set(F, "SRC-CBY-SANAA-C12-2024", "non_public_locator_note",
            "The address this record carried until 4 October 2026 returns HTTP 404. The same host serves the document "
            "under a different filename, which is the locator now recorded and which returned a 3-page PDF when it "
            "was opened on 4 October 2026. The host is a Yemeni news site, not the issuing bank: the Sana'a central "
            "bank publishes no public copy that could be opened from here.", None)

    # 3. the monetary series: its publication pages and the contemporaneous 2021-2022 issues
    issue_urls = ["https://english.cby-ye.com/files/%s.pdf" % fid for _, _, fid, _ in ISSUES]
    t15.set(F, "SRC-CBY-001", "additional_urls", json.dumps(CBY_PAGES + issue_urls), None)
    t15.set(F, "SRC-CBY-001", "non_public_locator_note",
            "The monetary series is a periodical. Every observation of this resource's monetary series is read from "
            "the issue recorded as the primary locator, which carries the back-data tables; the thirteen issues for "
            "December 2021 to December 2022 are recorded beside it so a reader can also reach the issue that first "
            "published a monthly value of those two years, together with the bank's own index of the series and its "
            "regulations and publications pages. All nineteen addresses were opened on 4 October 2026. The issue "
            "number of each was read from the document itself; the May 2022 issue prints no issue number, so none is "
            "stated for it.", None)

    # 4. the IGC record held only its landing page
    t15.set(F, "SRC-IGC-AIDDATA-REMIT-YEM-2026", "additional_urls", json.dumps(IGC_DOCS), None)

    # 5. the two papers
    hdr = t15.head
    rows = []
    for rec in NEW_SOURCES:
        if rec["source_id"] in t15.rows:
            raise TxError("%s already holds %s" % (S15, rec["source_id"]))
        cells = {}
        for field, value in rec.items():
            if field not in hdr:
                raise TxError("%s has no column %r" % (S15, field))
            cells[hdr.index(field) + 1] = value
        rows.append(cells)
    at = max(t15.rows.values()) + 1
    g = s.grid(S15)
    if at - 1 < len(g) and any(c not in (None, "") for c in g[at - 1]):
        raise TxError("%s: row %d after the last source is not blank" % (S15, at))
    s.ed.insert_rows(S15, at, rows)
    for rec in NEW_SOURCES:
        s.ledger.append(OrderedDict([("finding", F), ("sheet", S15), ("row", None), ("col", None),
                                     ("field", rec["source_id"]), ("old", None),
                                     ("new", json.dumps(rec, ensure_ascii=False))]))

    rep = s.save(out, ledger, OrderedDict([
        ("transaction", "FC-2"),
        ("summary", "Two broken source locators fixed (one pointed at the wrong document, one returned 404); the "
                    "CBY-Aden monetary series' own index and its thirteen 2021-2022 issues recorded; the two IGC "
                    "documents and two Yemen e-money and microfinance papers added; what could not be opened recorded "
                    "with its reason")]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
