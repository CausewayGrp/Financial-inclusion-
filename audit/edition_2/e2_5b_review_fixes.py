# -*- coding: utf-8 -*-
"""Edition 2 transaction E2-5b: the independent bilingual and adversarial review of E2-5, folded in (same commit).

  python3 e2_5b_review_fixes.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

The reviewer confirmed every number against the OECD text (printed page 32, PDF page 34; the report asks to be cited
as OECD (2026)). Findings:
1. CLM-059 currentness: "the latest observation in this record refers to 2024" may be false now that YLG totals with
   no end date sit in the record: "the latest SMEPS observation".
2. CLM-059 method_ar: the report's Arabic title as the source register and QUAL-001 give it («تعزيز المرونة الاقتصادية»).
3. CLM-059 limitations: the SMEPS and YLG figures must not be added (different sources, periods and units), and the
   evidence does not show whether they overlap.
4. QUAL-001 limitations: the OECD says confidence was undermined, not that relationships ended: "dates no change";
   Arabic «تجنّب المخاطر (de-risking)», not «تقليص المخاطر», which reads as mitigation.
5. Arabic «ضمن منذ عام 2017» can be read as «ضِمن» ("within"): «بلغ عدد المعاملات التي ضمنها … ».
6. The OECD's "in nominal terms" and "cumulative" restored.
7. The /firms/ paragraph opens plainly: "Guarantee data tell a different story".
8. The English title plural, as the Arabic. 9. The Arabic meta description spells out the OECD's name.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "release_candidate"))
from rc_lib import Session, Table, TxError  # noqa: E402

F = "E2-5b:REVIEW"
C59 = [
    ("title_en", "Programme reach describes the programme, not all MSMEs in Yemen",
     "Programme reach describes the programmes, not all MSMEs in Yemen"),
    ("currentness_en", "The latest observation in this record refers to 2024,", "The latest SMEPS observation refers to 2024,"),
    ("currentness_ar", "تعود أحدث مشاهدة في هذا السجل إلى عام 2024،", "تعود أحدث مشاهدة لوكالة SMEPS إلى عام 2024،"),
    ("method_ar", "«تعزيز الصمود الاقتصادي في اليمن»", "«تعزيز المرونة الاقتصادية في اليمن»"),
    ("limitations_en", "or what share of MSME lending they represent. |",
     "or what share of MSME lending they represent. The SMEPS and YLG figures come from different sources, periods and "
     "units (firms supported vs guaranteed transactions); they must not be added, and the evidence base does not "
     "establish whether they overlap. |"),
    ("limitations_ar", "ولا حصته من إقراض المنشآت الأصغر والصغيرة والمتوسطة. |",
     "ولا حصته من إقراض المنشآت الأصغر والصغيرة والمتوسطة. وتأتي أرقام SMEPS وأرقام YLG من مصادر وفترات ووحدات مختلفة "
     "(منشآت مدعومة مقابل معاملات مضمونة)؛ فلا تُجمع، ولا تثبت قاعدة الأدلة ما إذا كانت تتداخل. |"),
    ("summary_en", "with a cumulative USD 42.8 million of guarantees for USD 63.6 million",
     "with a cumulative USD 42.8 million of guarantees, in nominal terms, for USD 63.6 million"),
    ("summary_ar", "ضمن منذ عام 2017 ما مجموعه 5,731 معاملة، بضمانات تراكمية قدرها 42.8 مليون دولار لأصل",
     "بلغ عدد المعاملات التي ضمنها منذ عام 2017 ما مجموعه 5,731 معاملة، بضمانات تراكمية قدرها 42.8 مليون دولار بالقيمة "
     "الاسمية لأصل"),
]
QUAL = [
    ("limitations_en", "Its statement on correspondent banks counts no relationships and dates no loss:",
     "Its statement on correspondent banks counts no relationships and dates no change:"),
    ("limitations_ar", "ولا يحصي ما يقوله عن البنوك المراسلة أي علاقات، ولا يؤرخ أي انقطاع: فهو تقدير المنظمة، لا سجل رقابي "
                       "ولا قياس لتقليص المخاطر (de-risking).",
     "ولا تحصي عبارتها عن البنوك المراسلة أي علاقات، ولا تحدد متى حدث ذلك: فهي تقدير المنظمة، لا سجل رقابي ولا قياس لظاهرة "
     "تجنّب المخاطر (de-risking)."),
]
S7 = [
    ("en", "A different kind of programme evidence: the OECD reports", "Guarantee data tell a different story: the OECD reports"),
    ("en", "with USD 42.8 million of guarantees for", "with a cumulative USD 42.8 million of guarantees, in nominal terms, for"),
    ("ar", "ونوع آخر من الأدلة البرنامجية: تفيد", "وتقدم بيانات الضمانات صورة من نوع آخر: تفيد"),
    ("ar", "ضمن منذ عام 2017 ما مجموعه 5,731 معاملة، بضمانات قدرها 42.8 مليون دولار لأصل",
     "بلغ عدد المعاملات التي ضمنها منذ عام 2017 ما مجموعه 5,731 معاملة، بضمانات تراكمية قدرها 42.8 مليون دولار بالقيمة "
     "الاسمية لأصل"),
]
META_AR = ("وأرقام برنامج ضمان القروض اليمني كما تنقلها OECD،", "وأرقام برنامج ضمان القروض اليمني كما تنقلها منظمة التعاون الاقتصادي والتنمية،")


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    t06 = Table(s, "06_EVIDENCE_OBJECTS", 4)
    for field, old, new in C59:
        s.replace(F, "06_EVIDENCE_OBJECTS", t06.rows["CLM-059"], t06.col(field), old, new, f"CLM-059.{field}")
    for field, old, new in QUAL:
        s.replace(F, "06_EVIDENCE_OBJECTS", t06.rows["QUAL-001"], t06.col(field), old, new, f"QUAL-001.{field}")
    for lang, old, new in S7:
        s.replace_section(F, "/firms/", 7, lang, "body", old, new)
    t02 = Table(s, "02_SITE_MAP", 4)
    s.replace(F, "02_SITE_MAP", t02.rows["/evidence/CLM-059/"], t02.col("meta_description_ar"), *META_AR,
              "/evidence/CLM-059/.meta_description_ar")
    rep = s.save(out, ledger, OrderedDict([("transaction", "E2-5b"), ("summary", "E2-5 review fixes: never add the two programmes; SMEPS-specific currentness; no cut-off implied; Arabic")]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
