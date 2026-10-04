# -*- coding: utf-8 -*-
"""Release-candidate transaction RC-19: the fix batch from the independent review of 70398d1 (owner message of
4 October 2026, about 00:10 Aden) and the owner decision of 3 October 2026, 23:54 Aden on X-ESC-RC17-01
(audit/OWNER_DECISIONS_2026-10-02.md). English and Arabic change together. The code half (the language switch and the
menu as links, the redirect page of the old NEG-EW-011 address, the emphasis rule) ships in the same commit.

  python3 rc_19_independent_review.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

R-01, the FMIIP dates. The World Bank's Implementation Status and Results Report, sequence 2 (8 April 2026;
SRC-WB-FMIIP-ISR2-2026-001, read on 4 October 2026), gives the key dates of P180708: Board approval 17-Jun-2025,
signing 26-Jun-2025, effectiveness 01-Sep-2025; it names no start date, and lists the three components (Fast Payment
Systems; RTGS and CBY-Aden core banking; access and usage of the payment infrastructure) as approved on 17 June 2025.
Sequence 1 (22 September 2025) prints the same dates. "Started in July 2025" came from the UNDP project page, which
answers automated requests with HTTP 403 and was never read in this pull request. So:
- the three prose cells that said "started in July 2025" (VIS-PAYMENT-RAILS in 06 and 11, RV-CWR-009 in 11) now give
  the approval and effectiveness dates;
- the event REF-PAY-002 becomes "FMIIP effective" on 2025-09-01 and the three component events are dated 2025-06-17,
  the approval of the project that defines them; all four are bound to the World Bank report (a primary locator of a
  governed source record), not to the unread UNDP page;
- the access component's label follows the report's component name; "access-point database" was the UNDP wording.

X-ESC-RC17-01, owner decision of 3 October 2026, 23:54 Aden. /evidence/NEG-EW-011/ is no longer published as its own
record: its 02 and 06 rows are removed, and its address leads to CLM-015, the aggregate record of the circular, through
a page that says so (two governed labels). The circular's twelve names stay non-public lineage in 22_PROVIDERS_DATA,
where RC-NAMES reads them.

R-05, R-08. The no-JavaScript note names exactly what needs JavaScript once the language switch and the menu are
links. /privacy/ section 3 says what is decided about hosting (DigitalOcean App Platform, reached through
causewaygrp.com) and what the two services receive, and leaves what is not yet confirmed (fields, retention) open.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rc_lib import Session, Table, TxError, insert_ui_rows, ui_block_end, set_ui  # noqa: E402

ISR2 = "https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099040826144025755"
UNDP = "https://www.undp.org/yemen/projects/yemen-financial-market-infrastructure-and-inclusion-project"

FMIIP_PROSE = [
    # (sheet, object id, column, old substring, new substring)
    ("06_EVIDENCE_OBJECTS", "VIS-PAYMENT-RAILS", 6,
     "(FMIIP), which started in July 2025, with components",
     "(FMIIP), approved by the World Bank's Board on 17 June 2025 and effective from 1 September 2025, with components"),
    ("06_EVIDENCE_OBJECTS", "VIS-PAYMENT-RAILS", 7,
     "الذي بدأ في يوليو 2025، ويتضمن مكونات",
     "الذي أقرّه مجلس البنك الدولي في 17 يونيو 2025 وأصبح نافذًا اعتبارًا من 1 سبتمبر 2025، ويتضمن مكونات"),
    ("11_VISUAL_LIBRARY", "VIS-PAYMENT-RAILS", 21,
     "(FMIIP), which started in July 2025, with components",
     "(FMIIP), approved by the World Bank's Board on 17 June 2025 and effective from 1 September 2025, with components"),
    ("11_VISUAL_LIBRARY", "VIS-PAYMENT-RAILS", 22,
     "الذي بدأ في يوليو 2025، ويتضمن مكونات",
     "الذي أقرّه مجلس البنك الدولي في 17 يونيو 2025 وأصبح نافذًا اعتبارًا من 1 سبتمبر 2025، ويتضمن مكونات"),
    ("11_VISUAL_LIBRARY", "RV-CWR-009", 21,
     "(FMIIP), which started in July 2025 with components to support a Fast Payment System in areas under the "
     "internationally recognized government, a real-time gross settlement system with an upgrade of CBY-Aden core banking, "
     "and an access-point database;",
     "(FMIIP), approved by the World Bank's Board on 17 June 2025 and effective from 1 September 2025, with components for a "
     "Fast Payment System, a real-time gross settlement system with an upgrade of CBY-Aden core banking, and support for "
     "access to and use of the payment infrastructure;"),
    ("11_VISUAL_LIBRARY", "RV-CWR-009", 22,
     "الذي بدأ في يوليو 2025 بمكونات لدعم تطوير نظام للدفع السريع في مناطق الحكومة المعترف بها دوليًا، وإنشاء نظام للتسوية "
     "الإجمالية الفورية مع تحديث النظام المصرفي الأساسي للبنك المركزي في عدن، وإنشاء قاعدة بيانات لنقاط الوصول؛ وقرار مجلس "
     "إدارة البنك المركزي في عدن في 29 مارس 2026",
     "الذي أقرّه مجلس البنك الدولي في 17 يونيو 2025 وأصبح نافذًا اعتبارًا من 1 سبتمبر 2025، ويتضمن مكونات لتطوير نظام "
     "للدفع السريع ونظام للتسوية الإجمالية الفورية مع تحديث النظام المصرفي الأساسي للبنك المركزي اليمني – عدن، ولدعم "
     "الوصول إلى البنية التحتية للمدفوعات واستخدامها؛ وقرار مجلس إدارة البنك المركزي اليمني – عدن في 29 مارس 2026"),
]
ISR_NOTE = "World Bank ISR for P180708, sequence 2 (8 April 2026), key dates and components"
REF_EVENTS = {
    # event id: {field: (old, new)}
    "REF-PAY-002": {
        "date": ("2025-07", "2025-09-01"),
        "event": ("FMIIP starts", "FMIIP effective"),
        "normalized_description": (
            "Five-year Yemen Financial Market Infrastructure and Inclusion Project starts, funded by the World Bank and implemented by UNDP, with CBY-Aden as primary beneficiary.",
            "The World Bank-financed Yemen Financial Market Infrastructure and Inclusion Project (P180708), implemented by UNDP "
            "with CBY-Aden as primary beneficiary, became effective on 1 September 2025, after Board approval on 17 June 2025 "
            "and signing on 26 June 2025 (" + ISR_NOTE + "). The report gives no separate start date."),
        "source_url": (UNDP, ISR2),
    },
    "REF-PAY-003": {
        "date": ("2025-07", "2025-06-17"),
        "normalized_description": (
            "Project component supports development of a Fast Payment System (FPS) in IRG-controlled areas as a distinct payment-infrastructure component.",
            "Project component 'Development of Fast Payment Systems (FPS)', approved with the project on 17 June 2025 (" + ISR_NOTE + ")."),
        "source_url": (UNDP, ISR2),
    },
    "REF-PAY-004": {
        "date": ("2025-07", "2025-06-17"),
        "normalized_description": (
            "Project component supports establishment of a Real-Time Gross Settlement system (RTGS) managed by CBY-Aden, alongside upgrading CBY-Aden core banking; the project describes RTGS as foundational payment infrastructure.",
            "Project component 'Development of a Real Time Gross Settlement System and upgrading Core Banking for CBY Aden', "
            "approved with the project on 17 June 2025 (" + ISR_NOTE + ")."),
        "source_url": (UNDP, ISR2),
    },
    "REF-PAY-005": {
        "date": ("2025-07", "2025-06-17"),
        "normalized_description": (
            "Project includes geographically distributed access-point database, FI/PSP capacity building, merchant onboarding support in underserved areas and outreach.",
            "Project component 'Supporting access and usage of the payment's infrastructure', approved with the project on "
            "17 June 2025 (" + ISR_NOTE + "); its results indicators are merchants accepting electronic payments, active bank "
            "and e-wallet accounts and agents. The UNDP description of an access-point database is not read here."),
        "source_url": (UNDP, ISR2),
    },
}
COMPONENT_LABELS = [
    ("UI-VIS-CAT-EVT-FPS", "FMIIP component: support for developing a Fast Payment System",
     "FMIIP component, approved with the project: support for developing a Fast Payment System",
     "مكوّن في مشروع FMIIP: دعم تطوير نظام الدفع السريع", "مكوّن أُقرّ مع مشروع FMIIP: دعم تطوير نظام الدفع السريع"),
    ("UI-VIS-CAT-EVT-RTGS-CORE",
     "FMIIP component: support for establishing a real-time gross settlement (RTGS) system and upgrading CBY-Aden core banking",
     "FMIIP component, approved with the project: support for developing a real-time gross settlement (RTGS) system and upgrading CBY-Aden core banking",
     "مكوّن في مشروع FMIIP: دعم إنشاء نظام التسوية الإجمالية الفورية (RTGS) وتحديث النظام المصرفي الأساسي للبنك المركزي اليمني – عدن",
     "مكوّن أُقرّ مع مشروع FMIIP: دعم تطوير نظام التسوية الإجمالية الفورية (RTGS) وتحديث النظام المصرفي الأساسي للبنك المركزي اليمني – عدن"),
]
UI_EDITS = [
    # ui id, (old en, new en), (old ar, new ar), (old rule, new rule) or None
    ("UI-VIS-CAT-EVT-FMIIP-START", ("FMIIP starts", "FMIIP effective"), ("بدء مشروع FMIIP", "بدء نفاذ مشروع FMIIP"),
     ("Pre-Tranche-C P4 (V-D5). Chart label: event value 'FMIIP starts'.",
      "Pre-Tranche-C P4 (V-D5); RC-19 R-01. Chart label: event value 'FMIIP effective' (World Bank ISR: effectiveness 1 September 2025).")),
    ("UI-VIS-CAT-EVT-ACCESS-DB", ("FMIIP component: access-point database",
                                  "FMIIP component, approved with the project: support for access to and use of the payment infrastructure"),
     ("مكوّن في مشروع FMIIP: قاعدة بيانات لنقاط الوصول", "مكوّن أُقرّ مع مشروع FMIIP: دعم الوصول إلى البنية التحتية للمدفوعات واستخدامها"),
     None),
    ("UI-NOSCRIPT-NOTE",
     ("Search, Compare and the copy buttons need JavaScript. Every page of evidence remains readable without it.",
      "Search, Compare and the copy and print buttons need JavaScript. Every other page, the menu and the language switch work without it."),
     ("يحتاج البحث والمقارنة وأزرار النسخ إلى JavaScript، وتبقى كل صفحات الأدلة قابلة للقراءة من دونه.",
      "يحتاج البحث والمقارنة وأزرار النسخ والطباعة إلى JavaScript، وتعمل سائر الصفحات والقائمة وتبديل اللغة من دونه."),
     ("Tranche C TC-F (TOOL-17).", "Tranche C TC-F (TOOL-17); RC-19 R-05: the language switch and the menu are links, so they work without JavaScript.")),
]
UI_NEW = [
    ("UI-MOVED-RECORD-TITLE", "This record is no longer published on its own",
     "لم يعد هذا السجل منشورًا بمفرده",
     "RC-19 (owner decision of 3 October 2026, 23:54 Aden, X-ESC-RC17-01). Heading of the page at a retired record address."),
    ("UI-MOVED-RECORD-BODY",
     "This address now leads to the record of the Central Bank of Yemen – Aden (CBY-Aden) circular of 26 June 2024. "
     "Names from the regulator's lists are not reproduced here.",
     "يُحيل هذا الرابط الآن إلى سجل التعميم المؤرخ في 26 يونيو 2024 والصادر عن البنك المركزي اليمني – عدن. ولا تُذكر هنا "
     "الأسماء الواردة في قوائم الجهة الرقابية.",
     "RC-19 (owner decision of 3 October 2026, 23:54 Aden). Body of the page at a retired record address; the link that "
     "follows is the target record's governed title."),
]
PRIVACY_S3 = [
    ("en",
     "The hosting service may keep limited technical logs needed to deliver, secure and diagnose the site. Which fields are kept, for how long and by which service providers will be stated here once the hosting arrangements are confirmed.",
     "This resource is hosted on DigitalOcean App Platform. Readers reach it through causewaygrp.com, CauseWay's own "
     "website, which passes each request for these pages on to it. The causewaygrp.com website therefore receives the "
     "technical details that come with every request, such as the page address, the time of the request, the IP address "
     "and the browser type; if the browser holds the cookie that the causewaygrp.com website sets, that cookie is sent to "
     "the website with each request. App Platform, including the content-delivery network it serves through, receives "
     "each request as it is passed on. Either may keep such details in logs. Which details are kept, for what purpose, "
     "for how long and by which provider has not yet been confirmed; it will be stated here once it is."),
    ("ar",
     "قد تحتفظ خدمة الاستضافة بقدر محدود من السجلات التقنية اللازمة لتقديم الموقع وتأمينه وتشخيص أعطاله. وستُذكر هنا الحقول التي تُحفظ ومدة الاحتفاظ بها ومقدمو الخدمة المعنيون بمجرد تأكيد ترتيبات الاستضافة.",
     "يُستضاف هذا المورد على خدمة App Platform من DigitalOcean، ويصل إليه القرّاء عبر causewaygrp.com، وهو موقع CauseWay "
     "الإلكتروني الذي يمرّر إليه كل طلب لهذه الصفحات. ولذلك يتلقى موقع causewaygrp.com البيانات التقنية المصاحبة لكل طلب، "
     "مثل رابط الصفحة ووقت الطلب وعنوان IP ونوع المتصفح؛ وإذا كان المتصفح يحتفظ بملف تعريف الارتباط الذي يضعه موقع "
     "causewaygrp.com، فإنه يرسله إلى ذلك الموقع مع كل طلب. وتتلقى App Platform، بما فيها شبكة توصيل المحتوى التي تقدّم "
     "الصفحات عبرها، كل طلب كما يُمرَّر إليها. وقد يحتفظ أيٌّ منهما بهذه البيانات في سجلات. ولم يُؤكَّد بعدُ أيّ البيانات تُحفظ، "
     "ولا الغرض من حفظها، ولا مدة حفظها، ولا الجهة التي تحفظها؛ وسيُذكر ذلك هنا عند تأكيده."),
]


def row_of(s, sheet, key, header_row):
    g = s.grid(sheet)
    hits = [i for i, r in enumerate(g, 1) if i > header_row and r and r[0] == key]
    if len(hits) != 1:
        raise TxError(f"{sheet}: {key} found {len(hits)} times")
    return hits[0]


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    # R-01 prose
    for sheet, oid, col, old, new in FMIIP_PROSE:
        hr = 4
        s.replace("RC-19:R-01", sheet, row_of(s, sheet, oid, hr), col, old, new, f"{oid}.c{col}")
    # R-01 events
    t31 = Table(s, "31_REFORMS_REGULATION", 5)
    for eid, fields in REF_EVENTS.items():
        for fld, (old, new) in fields.items():
            t31.set("RC-19:R-01", eid, fld, new, old)
    # R-01 labels, R-05 note
    _, ui = ui_block_end(s)
    for uid, old_en, new_en, old_ar, new_ar in COMPONENT_LABELS:
        set_ui(s, "RC-19:R-01", uid, new_en, new_ar, old_en, old_ar)
    for uid, en, ar, rule in UI_EDITS:
        set_ui(s, "RC-19", uid, en[1], ar[1], en[0], ar[0])
        if rule:
            s.set("RC-19", "04_NAV_UX", ui[uid], 4, rule[1], rule[0], f"{uid}.use_rule")
    insert_ui_rows(s, "RC-19:X-ESC-RC17-01", UI_NEW)
    # R-08
    for lang, old, new in PRIVACY_S3:
        s.set_section("RC-19:R-08", "/privacy/", 3, lang, "body", new, old)
    # X-ESC-RC17-01: the record and its route are removed (rows, not cells; the lineage row in 22 stays)
    for sheet, key in (("06_EVIDENCE_OBJECTS", "NEG-EW-011"), ("02_SITE_MAP", "/evidence/NEG-EW-011/")):
        r = row_of(s, sheet, key, 4)
        s.ed.delete_rows(sheet, r, r)
        s.ledger.append(OrderedDict([("finding", "RC-19:X-ESC-RC17-01"), ("sheet", sheet), ("row", r), ("col", None),
                                     ("field", key), ("old", "row"), ("new", None),
                                     ("note", "row removed: the record is no longer published on its own (owner decision of 3 October 2026, 23:54 Aden)")]))
    if "NEG-EW-011" not in [r[0] for r in s.grid("22_PROVIDERS_DATA") if r]:
        raise TxError("22: the NEG-EW-011 lineage row must stay")
    rep = s.save(out, ledger, OrderedDict([("transaction", "RC-19"), ("summary", "Independent review of 70398d1: FMIIP dates (R-01), NEG-EW-011 to CLM-015 (X-ESC-RC17-01), /privacy/ hosting (R-08), no-JavaScript note (R-05)")]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
