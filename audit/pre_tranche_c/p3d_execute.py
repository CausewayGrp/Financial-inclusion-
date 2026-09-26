# -*- coding: utf-8 -*-
"""P3-D — Arabic scope for the twelve visuals that have no Evidence Record (Master-first).

  python3 p3d_execute.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

11_VISUAL_LIBRARY holds period and universe in English only. Visuals that are also Evidence Records take a bilingual
scope from 06; the ten Reading visuals and two domain visuals below have no 06 record, so their Arabic text alternative
and detached frame lost the scope line (red-team C2). Two columns are appended to 11 (period_ar, universe_ar) and filled
for those twelve; each Arabic value renders the row's own English period / denominator_universe, adding nothing.
Arabic authored by the Lead in the product's register; not certified by an external native editor.
"""
import sys
from ptc_lib import Session, TxError
from projection.master_reader import Workbook

AR = {
    "VIS-MFI-DIVERGENCE": ("نهاية 2015 ونهاية 2020 ونقطة مقيدة لنهاية 2023، إضافة إلى معلومة سياقية لعام 2021",
                           "نطاقات الإبلاغ الخاصة بكل مصدر لمؤسسات وبنوك التمويل الأصغر؛ ولا تزال مجموعة مقدمي الخدمة المشمولين في 2023 وإزالة تكرار المدخرين دون حسم"),
    "VIS-ACCESS-EVIDENCE-LAYER": ("بحسب كل عنصر", "المواقع المرصودة والمؤرخة في سجل الأدلة فقط"),
    "RV-CWR-001": ("نسختا نشر لعام 2024؛ ومسار مُطبَّع 2021–2024", "السنة المرجعية 2024 عبر نسختي نشر مسماتين؛ ومسار مُطبَّع 2021–2024"),
    "RV-CWR-002": ("مراكز 2022 كما نُشرت قبل تغيير منهج 2023 وبعده", "المراكز المصرفية لفترة الإسناد نفسها عبر نسخ النشر"),
    "RV-CWR-003": ("الأدلة الحالية المتاحة هنا؛ وتختلف التواريخ بحسب العنصر", "يحتفظ كل مسار بمجتمع المسح أو السجل الإداري الخاص به"),
    "RV-CWR-004": ("العمل الميداني السكاني في 2022–2023 إلى جانب أحداث المنظومة في 2025–2026", "مجتمعات مسحية وإدارية ومؤسسية وبرامجية منفصلة"),
    "RV-CWR-005": ("2016–2019، مع مستوى الحسابات في ديسمبر 2019", "خمسة مقدمي خدمات في الدراسة التاريخية لـIBS؛ وفئات قيمة المعاملات مقيدة بالمصدر"),
    "RV-CWR-006": ("نقاط مرجعية لعامي 2015 و2020، ونقطة مقيدة لعام 2023",
                   "مجموعات مؤسسات ومقدمي التمويل الأصغر كما يغطيها كل مصدر؛ وتعريفات المدخرين أو المودعين غير متسقة بالكامل"),
    "RV-CWR-007": ("موجة 2021؛ العمل الميداني في اليمن 2022–2023", "البالغون ضمن تغطية مسح Findex؛ مقارنة بين الرجال والنساء داخل الموجة نفسها"),
    "RV-CWR-008": ("مسح 2022؛ وتقارير البرنامج لعام 2024 وللفترة 2021–2024",
                   "مسح منشآت في سبع محافظات؛ ومجموعة فرعية بحسب الحاجة إلى التمويل؛ ومجتمع المنشآت الصغيرة والمتوسطة المدعومة من SMEPS"),
    "RV-CWR-009": ("تختلف التواريخ بحسب الإصلاح أو نظام الدفع؛ وترافق تواريخ الحدث أو المشاهدة كل حلقة",
                   "تحتفظ كل حالة بمجتمعها الإداري أو مجتمع مقدم الخدمة أو المستخدم أو السكان"),
    "RV-CWR-010": ("تواريخ خاصة بكل برنامج؛ ولم تُقس فترة الاستمرار بعد",
                   "المستفيدون من البرامج وحالات نشاط البرامج ومقدمي الخدمة؛ وليسوا تلقائيًا مستخدمين ماليين نشطين فريدين"),
}


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    g = Workbook(src).grid("11_VISUAL_LIBRARY")
    hdr = [str(x) if x is not None else None for x in g[3]]
    if hdr[22] != "public_routes" or (len(hdr) > 23 and hdr[23] not in (None, "")):
        raise TxError(f"11: unexpected header tail {hdr[20:]}")
    s.set("P3-F13", "11_VISUAL_LIBRARY", 4, 24, "period_ar", None, "header")
    s.set("P3-F13", "11_VISUAL_LIBRARY", 4, 25, "universe_ar", None, "header")
    for vid, (p, u) in AR.items():
        r = next(i for i, x in enumerate(g, 1) if x and x[0] == vid)
        s.set("P3-F13", "11_VISUAL_LIBRARY", r, 24, p, None, f"{vid}.period_ar")
        s.set("P3-F13", "11_VISUAL_LIBRARY", r, 25, u, None, f"{vid}.universe_ar")
    rep = s.save(out, ledger, [("transaction", "P3-D"), ("scope", "Arabic period/universe for the twelve visuals without an Evidence Record")])
    print(f"P3-D staged: {rep['cells_written']} changes; Master {rep['output_master_sha256']}")


if __name__ == "__main__":
    main()
