# -*- coding: utf-8 -*-
"""Edition 2 transaction E2-5: firm finance beyond 2022 and correspondent banking, from originals read (candidate a).

  python3 e2_5_guarantees_correspondent.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Originals read on 4 October 2026:
- OECD, Promoting Economic Resilience in Yemen (SRC-OECD-YEM-RESILIENCE-001). The HTML pages answer automated requests
  with HTTP 403; the full-report PDF at oecd.org/content/dam/oecd/en/publications/reports/2026/02/
  promoting-economic-resilience-in-yemen_b66657c1/81ed2898-en.pdf (71 pages) was read. Printed page 32: "Since 2017,
  the YLG has guaranteed 5 731 transactions, of which 72.7% were granted to men-owned businesses … In nominal terms,
  the YLG has provided a cumulative amount of USD 42.8 million of guarantees for a loan principal amount of USD 63.6
  million." The same page confirms the SMEPS facts OECD-YEM-012 to 014 (22 529, 20%, 8 624, 115 927). Chapter 2 (The
  Financial Sector): "the conflict has severely undermined the confidence of several foreign correspondent banks,
  given the level of perceived risks of money laundering and terrorism financing, isolating the Yemeni banking sector
  from regional and international financial networks."
- World Bank, Yemen Financial Sector Diagnostics 2024 (SRC-WB-FSD-2024-001), Box 5, read and matching the earlier
  record; not bound here (QUAL-001 is the OECD's record).
- IMF Country Report No. 26/80: not read here (imf.org answers HTTP 403; the IMF eLibrary PDF answers 202 with no body).
  Its statements stay unbound; the owner can supply the PDF (audit/edition_2/EDITION_2_LOG.md).

Where they go, without a new route (a new Evidence Record would need an entry in the steward's navigation contract):
- The guarantee volumes join CLM-059, whose frame is already the right one: programme reach describes the programme,
  not all MSMEs. Its title widens from SMEPS to programmes; the YLG sentences say what the programme backed and keep
  it apart from firms' access to finance (a guarantee volume is not firm access; transactions are not unique firms;
  the cumulative period has no stated end). /firms/ section 7 carries one paragraph.
- The correspondent-banking statement joins QUAL-001 (the OECD's qualitative interpretation, /finance/), as the OECD's
  assessment, with the boundary that it counts no relationships and dates no loss.
- 29_OECD_BENCHMARKS: OECD-YEM-012 to 017 become CONFIRMED.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "release_candidate"))
from rc_lib import Session, Table, TxError  # noqa: E402

F = "E2-5:S5-GUARANTEES/S5-CORRESPONDENT"
OECD = "SRC-OECD-YEM-RESILIENCE-001"
OECD_LINK = {"source_id": OECD, "url": "https://doi.org/10.1787/81ed2898-en", "audit_state": "SECONDARY_RESEARCH_LOCATOR"}

CLM059 = {
    "title_en": ("SMEPS programme reach describes the programme, not all MSMEs in Yemen",
                 "Programme reach describes the programme, not all MSMEs in Yemen"),
    "title_ar": ("وصول برنامج SMEPS دليل على نطاق البرنامج، لا على حجم قطاع المنشآت في اليمن",
                 "وصول البرامج دليل على نطاقها، لا على حجم قطاع المنشآت في اليمن"),
    "summary_en": ("they describe programme reach and finance, not national MSME prevalence or financial-sector lending.",
                   "they describe programme reach and finance, not national MSME prevalence or financial-sector lending. "
                   "Separately, the Organisation for Economic Co-operation and Development (OECD) reports that since 2017 "
                   "the Yemen Loan Guarantee Program (YLG), which offers partial guarantees on loans that banks and "
                   "microfinance institutions make to MSMEs, has guaranteed 5,731 transactions, with a cumulative USD 42.8 "
                   "million of guarantees for USD 63.6 million of loan principal."),
    "summary_ar": ("وتصف نطاق البرنامج وتمويله، لا انتشار المنشآت الأصغر والصغيرة والمتوسطة على المستوى الوطني ولا حجم "
                   "الإقراض في القطاع المالي.",
                   "وتصف نطاق البرنامج وتمويله، لا انتشار المنشآت الأصغر والصغيرة والمتوسطة على المستوى الوطني ولا حجم "
                   "الإقراض في القطاع المالي. وبصورة منفصلة، تفيد منظمة التعاون الاقتصادي والتنمية (OECD) بأن برنامج ضمان "
                   "القروض اليمني (YLG)، الذي يقدم ضمانات جزئية للقروض التي تمنحها البنوك ومؤسسات التمويل الأصغر للمنشآت "
                   "الأصغر والصغيرة والمتوسطة، ضمن منذ عام 2017 ما مجموعه 5,731 معاملة، بضمانات تراكمية قدرها 42.8 مليون "
                   "دولار لأصل قروض قدره 63.6 مليون دولار."),
    "definition_en": ("for 2024 and for 2021–2024.",
                      "for 2024 and for 2021–2024; and the transactions, guarantees and loan principal of the Yemen Loan "
                      "Guarantee Program (YLG) since 2017, as the OECD reports them."),
    "definition_ar": ("لعام 2024 وللفترة 2021–2024.",
                      "لعام 2024 وللفترة 2021–2024؛ والمعاملات والضمانات وأصل القروض في برنامج ضمان القروض اليمني (YLG) منذ "
                      "عام 2017، كما تفيد بها منظمة التعاون الاقتصادي والتنمية (OECD)."),
    "period_en": ("2024; cumulative 2021–2024", "2024; cumulative 2021–2024 (SMEPS); cumulative since 2017, reported in 2026 (YLG)"),
    "period_ar": ("2024؛ وتراكمي 2021–2024", "2024؛ وتراكمي 2021–2024 (SMEPS)؛ وتراكمي منذ 2017، أُبلغ عنه في 2026 (YLG)"),
    "universe_en": ("Micro, small and medium enterprises supported by SMEPS programmes, and the programme portfolio",
                    "Micro, small and medium enterprises supported by SMEPS programmes, and the programme portfolio; loan "
                    "transactions guaranteed by the Yemen Loan Guarantee Program (YLG)"),
    "universe_ar": ("المنشآت الأصغر والصغيرة والمتوسطة التي دعمتها برامج وكالة SMEPS، ومحفظة هذه البرامج.",
                    "المنشآت الأصغر والصغيرة والمتوسطة التي دعمتها برامج وكالة SMEPS، ومحفظة هذه البرامج؛ ومعاملات القروض التي "
                    "ضمنها برنامج ضمان القروض اليمني (YLG)."),
    "method_en": ("Programme outputs and funding as reported by SMEPS in its 2024 annual report.",
                  "Programme outputs and funding as reported by SMEPS in its 2024 annual report. The YLG figures as reported "
                  "by the OECD in Promoting Economic Resilience in Yemen (2026), page 32."),
    "method_ar": ("مخرجات البرامج وتمويلها كما أوردتها وكالة SMEPS في تقريرها السنوي لعام 2024.",
                  "مخرجات البرامج وتمويلها كما أوردتها وكالة SMEPS في تقريرها السنوي لعام 2024. وأرقام برنامج YLG كما أوردتها "
                  "منظمة التعاون الاقتصادي والتنمية (OECD) في تقرير «تعزيز الصمود الاقتصادي في اليمن» (2026)، الصفحة 32."),
    "limitations_en": ("The 2021–2024 total is not a count of unique firms. |",
                       "The 2021–2024 total is not a count of unique firms. A guarantee volume is not firms' access to "
                       "finance: guaranteed transactions are not unique firms, and guarantees and loan principal show what "
                       "the programme backed, not how many firms could borrow, on what terms, or what share of MSME lending "
                       "they represent. |"),
    "limitations_ar": ("ولا يمثل إجمالي 2021–2024 عددًا للمنشآت الفريدة. |",
                       "ولا يمثل إجمالي 2021–2024 عددًا للمنشآت الفريدة. وليس حجم الضمانات وصولًا للمنشآت إلى التمويل: "
                       "فالمعاملات المضمونة ليست منشآت فريدة، والضمانات وأصل القروض يبينان ما دعمه البرنامج، لا عدد المنشآت "
                       "التي تمكنت من الاقتراض ولا شروطه ولا حصته من إقراض المنشآت الأصغر والصغيرة والمتوسطة. |"),
    "currentness_en": ("It should not be read as describing a later period unless a newer comparable observation is published.",
                       "The YLG figures are cumulative since 2017 as reported in a report published in 2026, which states no "
                       "end date for that period. It should not be read as describing a later period unless a newer "
                       "comparable observation is published."),
    "currentness_ar": ("ولا تُقرأ على أنها تصف فترة لاحقة ما لم تُنشر مشاهدة أحدث قابلة للمقارنة.",
                       "وأرقام برنامج YLG تراكمية منذ عام 2017 كما وردت في تقرير نُشر عام 2026، لا يذكر تاريخًا لنهاية تلك "
                       "الفترة. ولا تُقرأ على أنها تصف فترة لاحقة ما لم تُنشر مشاهدة أحدث قابلة للمقارنة."),
}
META059 = ("Support and disbursement figures reported by the Small and Micro Enterprise Promotion Service (SMEPS) describe the programme, not all MSMEs in Yemen.",
           "Figures reported by the Small and Micro Enterprise Promotion Service (SMEPS) and, via the OECD, by the Yemen Loan Guarantee Program describe the programmes, not all MSMEs in Yemen.",
           "أرقام الدعم والصرف التي تفيد بها وكالة تنمية المنشآت الصغيرة والأصغر (SMEPS) تصف البرنامج، لا جميع المنشآت في اليمن.",
           "أرقام وكالة تنمية المنشآت الصغيرة والأصغر (SMEPS)، وأرقام برنامج ضمان القروض اليمني كما تنقلها OECD، تصف البرنامجين، لا جميع المنشآت في اليمن.")
FIRMS7 = (
    "A different kind of programme evidence: the OECD reports that since 2017 the Yemen Loan Guarantee Program (YLG) has "
    "guaranteed 5,731 transactions, with USD 42.8 million of guarantees for USD 63.6 million of loan principal. These are "
    "guarantee volumes: they show what the programme backed, not how many firms could borrow, on what terms, or what share "
    "of MSME lending they represent.",
    "ونوع آخر من الأدلة البرنامجية: تفيد منظمة التعاون الاقتصادي والتنمية (OECD) بأن برنامج ضمان القروض اليمني (YLG) ضمن "
    "منذ عام 2017 ما مجموعه 5,731 معاملة، بضمانات قدرها 42.8 مليون دولار لأصل قروض قدره 63.6 مليون دولار. وهذه أحجام ضمانات: "
    "تبين ما دعمه البرنامج، لا عدد المنشآت التي تمكنت من الاقتراض ولا شروطه ولا حصته من إقراض المنشآت الأصغر والصغيرة "
    "والمتوسطة.")
QUAL = {
    "summary_en": ("The evidence is contextual interpretation, not measured prevalence or a causal effect estimate.",
                   "On correspondent banking, the OECD writes that the conflict has severely undermined the confidence of "
                   "several foreign correspondent banks, given perceived risks of money laundering and terrorism financing, "
                   "isolating the Yemeni banking sector from regional and international financial networks. The evidence "
                   "is contextual interpretation, not measured prevalence or a causal effect estimate."),
    "summary_ar": ("هذا دليل تفسيري سياقي، وليس قياسًا للانتشار أو تقديرًا لأثر سببي.",
                   "وفي ما يخص المراسلة المصرفية، تكتب المنظمة أن النزاع أضعف بشدة ثقة عدد من البنوك المراسلة الأجنبية، بالنظر "
                   "إلى المخاطر المتصوَّرة لغسل الأموال وتمويل الإرهاب، مما عزل القطاع المصرفي اليمني عن الشبكات المالية "
                   "الإقليمية والدولية. هذا دليل تفسيري سياقي، وليس قياسًا للانتشار أو تقديرًا لأثر سببي."),
    "limitations_en": ("It cannot establish prevalence, a quantified level of trust or a causal effect size.",
                       "It cannot establish prevalence, a quantified level of trust or a causal effect size. Its statement on "
                       "correspondent banks counts no relationships and dates no loss: it is the OECD's assessment, not a "
                       "supervisory record or a measure of de-risking."),
    "limitations_ar": ("لا يثبت الانتشار أو مستوى ثقة كميًا أو حجم أثر سببي.",
                       "لا يثبت الانتشار أو مستوى ثقة كميًا أو حجم أثر سببي. ولا يحصي ما يقوله عن البنوك المراسلة أي علاقات، "
                       "ولا يؤرخ أي انقطاع: فهو تقدير المنظمة، لا سجل رقابي ولا قياس لتقليص المخاطر (de-risking)."),
}


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    t06 = Table(s, "06_EVIDENCE_OBJECTS", 4)
    for field, (old, new) in CLM059.items():
        s.replace(F, "06_EVIDENCE_OBJECTS", t06.rows["CLM-059"], t06.col(field), old, new, f"CLM-059.{field}")
    t06.set(F, "CLM-059", "source_dependencies", "SRC-SMEPS-AR2024-2025; " + OECD, "SRC-SMEPS-AR2024-2025")
    old_links = t06.get("CLM-059", "source_links")
    links = json.loads(old_links) + [OECD_LINK]
    t06.set(F, "CLM-059", "source_links", json.dumps(links, ensure_ascii=False, separators=(",", ":")), old_links)
    for field, (old, new) in QUAL.items():
        s.replace(F, "06_EVIDENCE_OBJECTS", t06.rows["QUAL-001"], t06.col(field), old, new, f"QUAL-001.{field}")
    t02 = Table(s, "02_SITE_MAP", 4)
    t02.set(F, "/evidence/CLM-059/", "meta_description_en", META059[1], META059[0])
    t02.set(F, "/evidence/CLM-059/", "meta_description_ar", META059[3], META059[2])
    t07 = Table(s, "07_PUBLIC_CLAIMS", 4)
    t07.set(F, "CLM-059", "evidence_inputs",
            '["219_SMEPS_PROGRAMME_EVIDENCE","EP-SMEPS-2024-PROGRAMME","OECD-YEM-015","OECD-YEM-016","OECD-YEM-017"]',
            '["219_SMEPS_PROGRAMME_EVIDENCE","EP-SMEPS-2024-PROGRAMME"]')
    t07.set(F, "CLM-059", "theme", "Firms / SME programme reach and guarantees", "Firms / SME programme reach")
    for lang, text in (("en", FIRMS7[0]), ("ar", FIRMS7[1])):
        row = s.section_row("/firms/", 7, lang)
        col = 5 if lang == "en" else 7
        cur = s.ed.get_value("03_PAGE_SECTIONS", row, col)
        s.set(F, "03_PAGE_SECTIONS", row, col, cur.rstrip() + "\n" + text, cur, f"/firms/#s7.body_{lang}")
    t29 = Table(s, "29_OECD_BENCHMARKS", 34)
    for fid in ("OECD-YEM-012", "OECD-YEM-013", "OECD-YEM-014", "OECD-YEM-015", "OECD-YEM-016", "OECD-YEM-017"):
        t29.set(F, fid, "verification_state", "CONFIRMED", "NOT_VERIFIED_AGAINST_OECD_TEXT")
    rep = s.save(out, ledger, OrderedDict([("transaction", "E2-5"), ("summary", "Yemen Loan Guarantee volumes (OECD, read in the original) beside SMEPS in CLM-059 and on /firms/; the OECD's correspondent-banking statement in QUAL-001; OECD-YEM-012 to 017 confirmed")]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
