# -*- coding: utf-8 -*-
"""Edition 2 transaction E2-6: the IMF's two statements on correspondent banking, each with its speaker.

  python3 e2_6_imf_correspondent.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Original: IMF Country Report No. 26/80 (April 2026), the PDF the owner supplied on 4 October 2026 (92 pages), read:
- PDF page 4, press release, Executive Board assessment (Board consideration 31 March 2026): "Directors considered the
  relocation of major banks to Aden as an opportunity to strengthen financial stability and integrity. They encouraged
  extending regulation to all deposit-taking institutions and enhancing the AML-CFT framework to safeguard
  correspondent banking relationships."
- PDF page 90, statement by the Executive Director for the Republic of Yemen (the authorities' view): "Following the
  designation of the Houthi militia as a foreign terrorist organization (FTO) by the United States, all major banks
  relocated their headquarters to Aden to protect correspondent banking relationships and maintain liquidity."
Both join QUAL-001, the qualitative record on /finance/, whose title widens from the OECD alone to the OECD and the
IMF; each sentence names its speaker; the boundary says that neither counts relationships and that a relocation is not
a measure of de-risking. Source dates of the IMF report filled from its cover (document date 2026-04).
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "release_candidate"))
from rc_lib import Session, Table, TxError  # noqa: E402

F = "E2-6:S5-CORRESPONDENT"
IMF = "SRC-IMF-YEM-AIV-2025-2026"
IMF_URL = "https://www.imf.org/-/media/files/publications/cr/2026/english/1yemea2026001-source-pdf.pdf"
Q = [
    ("title_en", "OECD: institutional fragility and weak formal access (qualitative interpretation)",
     "OECD and IMF: institutional fragility, weak formal access and correspondent banking (qualitative assessments)"),
    ("title_ar", "OECD: الهشاشة المؤسسية وضعف الوصول الرسمي (تفسير نوعي)",
     "OECD وصندوق النقد الدولي: الهشاشة المؤسسية وضعف الوصول الرسمي والمراسلة المصرفية (تقديرات نوعية)"),
    ("summary_en", "isolating the Yemeni banking sector from regional and international financial networks.",
     "isolating the Yemeni banking sector from regional and international financial networks. The IMF's Executive "
     "Board, concluding the 2025 Article IV consultation on 31 March 2026, considered the relocation of major banks to "
     "Aden an opportunity to strengthen financial stability and integrity, and encouraged enhancing the AML-CFT framework "
     "to safeguard correspondent banking relationships. In the statement of Yemen's Executive Director at the IMF, the "
     "authorities say that after the United States designated the Houthis a foreign terrorist organization, all major "
     "banks moved their headquarters to Aden to protect correspondent banking relationships and maintain liquidity."),
    ("summary_ar", "مما عزل القطاع المصرفي اليمني عن الشبكات المالية الإقليمية والدولية.",
     "مما عزل القطاع المصرفي اليمني عن الشبكات المالية الإقليمية والدولية. وعند اختتام مشاورات المادة الرابعة لعام 2025 "
     "في 31 مارس 2026، رأى المجلس التنفيذي لصندوق النقد الدولي في نقل البنوك الرئيسية إلى عدن فرصةً لتعزيز الاستقرار "
     "المالي والنزاهة المالية، وشجّع على تعزيز إطار مكافحة غسل الأموال وتمويل الإرهاب لصون علاقات المراسلة المصرفية. "
     "وفي بيان المدير التنفيذي لليمن لدى الصندوق، تقول السلطات إنه بعد أن صنّفت الولايات المتحدة الحوثيين منظمةً "
     "إرهابية أجنبية، نقلت جميع البنوك الرئيسية مقارّها إلى عدن لحماية علاقات المراسلة المصرفية والحفاظ على السيولة."),
    ("definition_en", "relate to financial-sector fragility and low trust in Yemen.",
     "relate to financial-sector fragility and low trust in Yemen; and two IMF statements of 2026 on correspondent "
     "banking: the Executive Board's assessment and the authorities' account."),
    ("definition_ar", "وهشاشة القطاع المالي وانخفاض الثقة في اليمن من جهة أخرى.",
     "وهشاشة القطاع المالي وانخفاض الثقة في اليمن من جهة أخرى؛ وبيانان لصندوق النقد الدولي في 2026 عن المراسلة "
     "المصرفية: تقدير المجلس التنفيذي، ورواية السلطات."),
    ("universe_en", "OECD/EU institutional analysis based on consultations, workshops and sector analysis.",
     "OECD/EU institutional analysis based on consultations, workshops and sector analysis; the IMF Executive Board's "
     "assessment and the Yemeni authorities' statement in the 2025 Article IV consultation."),
    ("universe_ar", "يستند إلى مشاورات وورش عمل وتحليل قطاعي.",
     "يستند إلى مشاورات وورش عمل وتحليل قطاعي؛ وتقدير المجلس التنفيذي لصندوق النقد الدولي وبيان السلطات اليمنية في "
     "مشاورات المادة الرابعة لعام 2025."),
    ("method_en", "drawing on consultations, workshops and sector analysis under an OECD–EU project.",
     "drawing on consultations, workshops and sector analysis under an OECD–EU project. The IMF statements are quoted "
     "from IMF Country Report No. 26/80 (April 2026): the press release on the Executive Board's assessment (PDF page 4) "
     "and the statement by the Executive Director for the Republic of Yemen (PDF page 90)."),
    ("method_ar", "ضمن مشروع مشترك بين المنظمة والاتحاد الأوروبي.",
     "ضمن مشروع مشترك بين المنظمة والاتحاد الأوروبي. ويُنقل بيانا صندوق النقد الدولي من تقريره القُطري رقم 26/80 "
     "(أبريل 2026): البيان الصحفي عن تقدير المجلس التنفيذي (الصفحة 4 من ملف PDF)، وبيان المدير التنفيذي للجمهورية "
     "اليمنية (الصفحة 90 من ملف PDF)."),
    ("limitations_en", "it is the OECD's assessment, not a supervisory record or a measure of de-risking.",
     "it is the OECD's assessment, not a supervisory record or a measure of de-risking. The IMF passages are the "
     "Board's assessment and the authorities' account: neither counts correspondent relationships, and a bank's "
     "relocation is not a measure of de-risking or of restored access."),
    ("limitations_ar", "فهي تقدير المنظمة، لا سجل رقابي ولا قياس لظاهرة تجنّب المخاطر (de-risking).",
     "فهي تقدير المنظمة، لا سجل رقابي ولا قياس لظاهرة تجنّب المخاطر (de-risking). وعبارتا صندوق النقد الدولي هما "
     "تقدير المجلس التنفيذي ورواية السلطات: لا تحصي أيٌّ منهما علاقات المراسلة، وليس نقل بنك لمقره قياسًا لتجنّب "
     "المخاطر ولا لاستعادة الوصول."),
]
META = ("The OECD links fragmented institutions, supervisory gaps and weak formal access to financial-sector fragility and low trust: a qualitative interpretation.",
        "The OECD on institutional fragility and weak formal access, and the IMF Board and the authorities on correspondent banking: qualitative assessments, each with its speaker.",
        "تربط منظمة التعاون الاقتصادي والتنمية (OECD) تفتت المؤسسات وفجوات الرقابة وضعف الوصول الرسمي بهشاشة القطاع المالي وانخفاض الثقة: تفسير نوعي.",
        "منظمة التعاون الاقتصادي والتنمية عن الهشاشة المؤسسية وضعف الوصول الرسمي، والمجلس التنفيذي لصندوق النقد الدولي والسلطات عن المراسلة المصرفية: تقديرات نوعية، لكلٍّ منها قائلها.")


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    t06 = Table(s, "06_EVIDENCE_OBJECTS", 4)
    for field, old, new in Q:
        s.replace(F, "06_EVIDENCE_OBJECTS", t06.rows["QUAL-001"], t06.col(field), old, new, f"QUAL-001.{field}")
    deps = t06.get("QUAL-001", "source_dependencies")
    t06.set(F, "QUAL-001", "source_dependencies", deps + "; " + IMF, deps)
    links = t06.get("QUAL-001", "source_links")
    new_links = json.loads(links) + [{"source_id": IMF, "url": IMF_URL, "audit_state": "PRIMARY_OFFICIAL_DOCUMENT"}]
    t06.set(F, "QUAL-001", "source_links", json.dumps(new_links, ensure_ascii=False, separators=(",", ":")), links)
    t02 = Table(s, "02_SITE_MAP", 4)
    t02.set(F, "/evidence/QUAL-001/", "meta_description_en", META[1], META[0])
    t02.set(F, "/evidence/QUAL-001/", "meta_description_ar", META[3], META[2])
    t15 = Table(s, "15_SOURCE_LIBRARY", 4)
    t15.set(F, IMF, "document_date", "2026-04", None)
    t15.set(F, IMF, "retrieval_date", "2026-10-04", None)
    rep = s.save(out, ledger, OrderedDict([("transaction", "E2-6"), ("summary", "IMF CR 26/80: the Board's assessment and the authorities' statement on correspondent banking in QUAL-001, each with its speaker")]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
