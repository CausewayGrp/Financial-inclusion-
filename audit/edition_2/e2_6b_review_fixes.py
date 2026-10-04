# -*- coding: utf-8 -*-
"""Edition 2 transaction E2-6b: the bilingual and adversarial review of E2-6, folded in (same commit).

  python3 e2_6b_review_fixes.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

1. The title credited the authorities' account to the IMF: it now names the OECD, the IMF Executive Board and the
   Yemeni authorities, as "qualitative accounts".
2. Definition and method called both passages "IMF statements" and said "quoted" for a paraphrase: "two passages of
   IMF Country Report No. 26/80 … drawn from".
3. The Executive Director's role as the source titles it: "the Executive Director for the Republic of Yemen".
4. The English meta description says "IMF Executive Board".
"""
import json, os, sys
from collections import OrderedDict
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "release_candidate"))
from rc_lib import Session, Table, TxError  # noqa: E402

F = "E2-6b:REVIEW"
Q = [
    ("title_en", "OECD and IMF: institutional fragility, weak formal access and correspondent banking (qualitative assessments)",
     "OECD, IMF Executive Board and Yemeni authorities: institutional fragility, weak formal access and correspondent banking (qualitative accounts)"),
    ("title_ar", "OECD وصندوق النقد الدولي: الهشاشة المؤسسية وضعف الوصول الرسمي والمراسلة المصرفية (تقديرات نوعية)",
     "OECD والمجلس التنفيذي لصندوق النقد الدولي والسلطات اليمنية: الهشاشة المؤسسية وضعف الوصول الرسمي والمراسلة المصرفية (تقديرات وروايات نوعية)"),
    ("definition_en", "and two IMF statements of 2026 on correspondent banking:",
     "and two passages of IMF Country Report No. 26/80 (2026) on correspondent banking:"),
    ("definition_ar", "وبيانان لصندوق النقد الدولي في 2026 عن المراسلة المصرفية:",
     "وفقرتان من التقرير القُطري لصندوق النقد الدولي رقم 26/80 (2026) عن المراسلة المصرفية:"),
    ("method_en", "The IMF statements are quoted from IMF Country Report No. 26/80 (April 2026):",
     "The two passages are drawn from IMF Country Report No. 26/80 (April 2026):"),
    ("method_ar", "ويُنقل بيانا صندوق النقد الدولي من تقريره القُطري رقم 26/80", "وتُستمد الفقرتان من التقرير القُطري لصندوق النقد الدولي رقم 26/80"),
    ("method_ar", "وبيان المدير التنفيذي للجمهورية اليمنية", "وبيان المدير التنفيذي عن الجمهورية اليمنية"),
    ("summary_en", "In the statement of Yemen's Executive Director at the IMF, the authorities say",
     "In the statement by the Executive Director for the Republic of Yemen, the authorities say"),
    ("summary_ar", "وفي بيان المدير التنفيذي لليمن لدى الصندوق، تقول السلطات", "وفي بيان المدير التنفيذي عن الجمهورية اليمنية في الصندوق، تقول السلطات"),
]


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    t06 = Table(s, "06_EVIDENCE_OBJECTS", 4)
    for field, old, new in Q:
        s.replace(F, "06_EVIDENCE_OBJECTS", t06.rows["QUAL-001"], t06.col(field), old, new, f"QUAL-001.{field}")
    t02 = Table(s, "02_SITE_MAP", 4)
    s.replace(F, "02_SITE_MAP", t02.rows["/evidence/QUAL-001/"], t02.col("meta_description_en"), "and the IMF Board and",
              "and the IMF Executive Board and", "/evidence/QUAL-001/.meta_description_en")
    rep = s.save(out, ledger, OrderedDict([("transaction", "E2-6b"), ("summary", "E2-6 review: each speaker named in the title; passages, not IMF statements; the Executive Director's role")]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex); sys.exit(2)
