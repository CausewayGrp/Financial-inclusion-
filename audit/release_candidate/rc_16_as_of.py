# -*- coding: utf-8 -*-
"""Release-candidate transaction RC-16: two lessons of Owner Addendum 2 ("Lessons from comparable products"), applied
where governed fields exist. English and Arabic change together.

  python3 rc_16_as_of.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

1. "Never label anything 'latest'; say 'as of <date>'. Add a lint gate over titles and meta."
   A title, heading or page description that calls a measure "the latest" goes stale silently the day a newer one
   appears. Record titles and section headings now name the wave or period they mean (the Global Findex 2021 wave).
   Page descriptions that need the currency claim say when it was checked ("As checked on 3 October 2026, …"), as
   CLM-017's already does. Uses that carry their own check date ("… as checked on 3 October 2026") or deny a single
   latest year ("There is no single latest year …") are kept. The gate RC-LATEST holds the rule over every title,
   description and h1 (scripts/validate.py).
2. "Every survey-derived record states its coverage … with the excluded areas named. Add this where the governed
   universe does not already say it." Four 2021-wave indicator records (VIS-FINDEX-ACCESS-USE, -BARRIERS, -RESILIENCE,
   -FLOW-CHANNELS) did not; they gain CLM-025's governed sentence (the excluded areas, about 23% of the population).
   The records that describe the sample itself (VIS-FINDEX-SAMPLE-SUPPORT, CLM-023, CLM-024) or a specification
   (CLM-026) are not population estimates and are left as they are. CLM-031, VIS-DEMAND-VINTAGE-LADDER and
   DS-FINDEX-HISTORY-CROSSWALK set several waves side by side; a coverage sentence there would have to name the 2021
   wave alone, and each links CLM-025 through its wave. They are left for the steward (docs/ROADMAP_V1_1.md).

3. B15 red-team condition on B-7: until VIS-MFI-SPINE has the contract escalated to the owner, its title must not
   promise a view of the gaps it does not draw. The record renders no figure and no table; its summary names each gap
   in words. "…, with gaps and breaks shown" becomes "…, with their gaps and breaks".

4. B16, register item "the base of VIS-FIRM-FINANCE-SEVERITY" (RELEASE, a truth risk). The World Bank's Yemen Financial
   Sector Diagnostics (2024), read again on 3 October 2026 at its locator, p. 145: "Around 69% believed that access to
   finance is a major obstacle to their operations (this ranking tabulated after excluding those that checked 'no need
   for a loan') when asking for the reasons of not applying." The governed universe (firms that said they needed no
   loan excluded) may be wider than the source's base (firms that did not apply, less those). The record's measurement
   limitation now says so, and says that which base the source used is not established here. No value changes.

No number is added: 23% and the excluded areas are CLM-025's, and every wave and fieldwork date is already governed.

Review: one bilingual reviewer (Arabic first), NOT ACCEPTABLE at the first run on two points. "When each function was
last measured" was false: saving and borrowing were measured in the 2021 wave, only their weighted values are not
produced. And the vintage ladder's description, without "latest", claimed that weighted account-ownership evidence
dates from 2021, when weighted 2011 and 2014 values are published. Both are corrected: the title names the last weighted
value, and the description keeps "latest" with its check date. The minor findings were folded into the same rerun:
one Arabic name for the wave («موجة Global Findex 2021»), no «قاس … عند», "all of Yemen", and the reforms Reading's
description keeping its point, dated.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rc_lib import Session, Table, TxError  # noqa: E402

F1, F2 = "RC-16:LATEST", "RC-16:COVERAGE"

SPINE = [  # 06 title (B15 B-7 condition)
    ("VIS-MFI-SPINE", "title_en", "Microfinance observations by date, with gaps and breaks shown",
     "Microfinance observations by date, with their gaps and breaks"),
    ("VIS-MFI-SPINE", "title_ar", "مشاهدات التمويل الأصغر بحسب التاريخ، مع إظهار الفجوات والانقطاعات",
     "مشاهدات التمويل الأصغر بحسب التاريخ، مع فجواتها وانقطاعاتها"),
]

TITLES = [  # 06 title_en / title_ar: (key, field, old, new)
    ("CLM-001", "title_en", "Latest representative account-ownership measure available",
     "Account ownership: the representative measure from the Global Findex 2021 wave"),
    ("CLM-001", "title_ar", "أحدث قياس ممثل متاح لامتلاك الحساب",
     "امتلاك الحساب: القياس الممثل من موجة Global Findex 2021"),
    ("CLM-025", "title_en", "Geographic coverage limits of the latest Findex wave",
     "Geographic coverage limits of the Global Findex 2021 wave in Yemen"),
    ("CLM-025", "title_ar", "حدود التغطية الجغرافية لأحدث موجة من Findex",
     "حدود التغطية الجغرافية لموجة Global Findex 2021 في اليمن"),
    ("VIS-DEMAND-VINTAGE-LADDER", "title_en", "Latest observation for each people-side financial function",
     "Year of the last weighted value for each people-side financial function"),
    ("VIS-DEMAND-VINTAGE-LADDER", "title_ar", "أحدث مشاهدة لكل وظيفة مالية على جانب الأفراد",
     "سنة آخر قيمة موزونة لكل وظيفة مالية على جانب الأفراد"),
    ("DS-FINDEX-HISTORY-CROSSWALK", "title_en", "Which historical Findex measures can be compared with the latest wave",
     "Which historical Findex measures can be compared with the 2021 wave"),
    ("DS-FINDEX-HISTORY-CROSSWALK", "title_ar", "مقاييس Findex التاريخية التي يمكن مقارنتها بأحدث موجة",
     "مقاييس Findex التاريخية التي يمكن مقارنتها بموجة 2021"),
]

DESCRIPTIONS = [  # 02 meta_description_en / _ar: (route, lang, old, new) — whole values
    ("/evidence/CLM-001/", "en",
     "The latest representative observation of account ownership in Yemen published by the World Bank remains 11.9% (Global Findex 2021; fieldwork 2022–23).",
     "As checked on 3 October 2026, the most recent representative observation of account ownership in Yemen published by the World Bank was 11.9% (Global Findex 2021; fieldwork 2022–23)."),
    ("/evidence/CLM-001/", "ar",
     "تظل أحدث مشاهدة ممثلة ينشرها البنك الدولي لامتلاك الحساب في اليمن عند 11.9% (Global Findex 2021؛ العمل الميداني 2022–2023).",
     "عند الاطلاع في 3 أكتوبر 2026، كانت أحدث مشاهدة ممثلة نشرها البنك الدولي لامتلاك الحساب في اليمن 11.9% (Global Findex 2021؛ العمل الميداني 2022–2023)."),
    ("/evidence/CLM-025/", "en",
     "The latest Yemen Findex wave excludes Al Baydaa, Al Jawf, Mareb, Sadah, Socotra and several districts elsewhere: areas with about 23% of the population.",
     "The Global Findex 2021 wave for Yemen excludes Al Baydaa, Al Jawf, Mareb, Sadah, Socotra and several districts elsewhere: areas with about 23% of the population."),
    ("/evidence/CLM-025/", "ar",
     "تستبعد أحدث موجة من Findex في اليمن محافظات البيضاء والجوف ومأرب وصعدة وسقطرى وعددًا من المديريات في محافظات أخرى، وهي مناطق تضم نحو 23% من السكان.",
     "تستبعد موجة Findex 2021 في اليمن محافظات البيضاء والجوف ومأرب وصعدة وسقطرى وعددًا من المديريات في محافظات أخرى، وهي مناطق تضم نحو 23% من السكان."),
    ("/evidence/DS-FINDEX-HISTORY-CROSSWALK/", "en",
     "This comparability map links historical Findex measures for Yemen to those for the latest wave, keeping publishable values apart from pending ones.",
     "This comparability map links historical Findex measures for Yemen to those for the 2021 wave, keeping publishable values apart from pending ones."),
    ("/evidence/DS-FINDEX-HISTORY-CROSSWALK/", "ar",
     "تربط خريطة قابلية المقارنة هذه مقاييس Findex التاريخية لليمن بمقاييس أحدث موجة، مع الفصل بين القيم القابلة للنشر والمقاييس التي لم تُستكمل حساباتها.",
     "تربط خريطة قابلية المقارنة هذه مقاييس Findex التاريخية لليمن بمقاييس موجة 2021، مع الفصل بين القيم القابلة للنشر والمقاييس التي لم تُستكمل حساباتها."),
    ("/evidence/VIS-DEMAND-VINTAGE-LADDER/", "en",
     "The latest weighted evidence differs by function: account ownership from the 2021 Findex wave; saving, borrowing and domestic remittances from 2014.",
     "As checked on 3 October 2026, the latest weighted evidence on people differs by function: account ownership from the 2021 Findex wave; saving, borrowing and domestic remittances from 2014."),
    ("/evidence/VIS-DEMAND-VINTAGE-LADDER/", "ar",
     "يختلف أحدث دليل موزون بحسب الوظيفة: امتلاك الحساب من موجة Findex 2021، والادخار والاقتراض والحوالات المحلية من 2014.",
     "عند الاطلاع في 3 أكتوبر 2026، كان أحدث دليل موزون عن الأفراد يختلف بحسب الوظيفة: امتلاك الحساب من موجة Findex 2021، والادخار والاقتراض والحوالات المحلية من 2014."),
    ("/people/", "en",
     "The latest representative survey, the Global Findex 2021 wave (fieldwork 2022–23), found 11.9% of adults in surveyed areas had an account; not a 2026 rate.",
     "The Global Findex 2021 wave, a representative survey (fieldwork 2022–23), found that 11.9% of adults in surveyed areas had an account; not a 2026 rate."),
    ("/people/", "ar",
     "وجد أحدث مسح ممثل، موجة Global Findex 2021 (العمل الميداني 2022–2023)، أن 11.9% من البالغين في المناطق المشمولة يملكون حسابًا؛ وليس هذا معدلًا لعام 2026.",
     "وجدت موجة Global Findex 2021، وهي مسح ممثل (العمل الميداني 2022–2023)، أن 11.9% من البالغين في المناطق المشمولة يملكون حسابًا؛ وليس هذا معدلًا لعام 2026."),
    ("/readings/gender-gap-measured-causes-open/", "en",
     "In the latest Global Findex wave for Yemen, 18.35% of men and 5.44% of women in surveyed areas had an account: a measured gap whose explanation is open.",
     "In the Global Findex 2021 wave for Yemen, 18.35% of men and 5.44% of women in surveyed areas had an account: a measured gap whose explanation is open."),
    ("/readings/gender-gap-measured-causes-open/", "ar",
     "في أحدث موجة من Findex في اليمن، كان لدى 18.35% من الرجال و5.44% من النساء في المناطق المشمولة حساب؛ وهي فجوة مقاسة ما يزال تفسيرها مفتوحًا.",
     "في موجة Global Findex 2021 الخاصة باليمن، كان لدى 18.35% من الرجال و5.44% من النساء في المناطق المشمولة حساب؛ وهي فجوة مقاسة ما يزال تفسيرها مفتوحًا."),
    ("/readings/reforms-newer-than-people-evidence/", "en",
     "The latest representative measure of account ownership in Yemen is 11.9% of adults in surveyed areas (fieldwork 2022–23); the system has kept moving.",
     "As checked on 3 October 2026, the most recent representative measure of account ownership in Yemen is 11.9% of adults in surveyed areas (Findex 2021; fieldwork 2022–23); the system has moved since."),
    ("/readings/reforms-newer-than-people-evidence/", "ar",
     "يبقى أحدث قياس ممثل لامتلاك الحساب في اليمن عند 11.9% من البالغين في المناطق المشمولة (العمل الميداني 2022–2023)؛ والمنظومة لم تتوقف.",
     "عند الاطلاع في 3 أكتوبر 2026، كانت أحدث نسبة ممثلة لامتلاك الحساب في اليمن 11.9% من البالغين في المناطق المشمولة (Findex 2021؛ العمل الميداني 2022–2023)؛ والمنظومة تغيّرت منذ ذلك الحين."),
]

HEADINGS = [  # 03 /people/ section headings: (order, lang, old, new)
    (None, "en", "The latest representative account-ownership measure available",
     "Account ownership: the representative measure from the Global Findex 2021 wave"),
    (None, "ar", "أحدث قياس ممثل متاح لامتلاك الحساب", "امتلاك الحساب: القياس الممثل من موجة Global Findex 2021"),
    (None, "en", "The latest wave does not cover all geography", "The 2021 wave does not cover all of Yemen"),
    (None, "ar", "التغطية الجغرافية لأحدث موجة ليست كاملة", "التغطية الجغرافية لموجة 2021 ليست كاملة"),
]

COVERAGE_EN = (" The survey frame excludes Al Baydaa, Al Jawf, Mareb, Sadah, Socotra and several districts elsewhere: "
               "areas with about 23% of the population.")
COVERAGE_AR = (" ويستبعد إطار المسح محافظات البيضاء والجوف ومأرب وصعدة وسقطرى وعددًا من المديريات في محافظات أخرى، "
               "وهي مناطق تضم نحو 23% من السكان.")
COVERAGE_KEYS = ["VIS-FINDEX-ACCESS-USE", "VIS-FINDEX-BARRIERS", "VIS-FINDEX-RESILIENCE", "VIS-FINDEX-FLOW-CHANNELS"]


SEVERITY = [
    ("en", " The source introduces the tabulation 'when asking for the reasons of not applying' (p. 145), so its base may be "
           "narrower still: firms that did not apply for a loan, less those that said they did not need one. Which base the "
           "source used is not established here."),
    ("ar", " ويعرض المصدر هذا الجدول في سياق السؤال عن أسباب عدم التقدم بطلب قرض (الصفحة 145)، لذا قد تكون قاعدته أضيق: "
           "المنشآت التي لم تتقدم بطلب قرض، باستثناء التي قالت إنها لا تحتاج إليه. ولم يُثبت هنا أي القاعدتين استخدمها المصدر."),
]


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    t06 = Table(s, "06_EVIDENCE_OBJECTS", 4)
    t02 = Table(s, "02_SITE_MAP", 4)
    for key, field, old, new in TITLES:
        t06.set(F1, key, field, new, old)
    for key, field, old, new in SPINE:
        t06.set("RC-16:B15-B-7", key, field, new, old)
    for route, lang, old, new in DESCRIPTIONS:
        t02.set(F1, route, f"meta_description_{lang}", new, old)
    g03 = s.grid("03_PAGE_SECTIONS")
    for _, lang, old, new in HEADINGS:
        col = 4 if lang == "en" else 6
        rows = [i for i, r in enumerate(g03, 1) if r and r[0] == "/people/" and len(r) >= col and r[col - 1] == old]
        if len(rows) != 1:
            raise TxError(f"{F1}: /people/ heading {old!r} found {len(rows)} times")
        s.set(F1, "03_PAGE_SECTIONS", rows[0], col, new, old, f"/people/.heading_{lang}")
    for key in COVERAGE_KEYS:
        for lang, add in (("en", COVERAGE_EN), ("ar", COVERAGE_AR)):
            cur = t06.get(key, f"universe_{lang}")
            if not isinstance(cur, str) or "23%" in cur:
                raise TxError(f"{F2}: {key}.universe_{lang} is empty or already states the coverage")
            t06.set(F2, key, f"universe_{lang}", cur.rstrip() + add, cur)
    for lang, add in SEVERITY:
        cur = t06.get("VIS-FIRM-FINANCE-SEVERITY", f"limitations_{lang}")
        if not isinstance(cur, str) or " | " not in cur or "145" in cur:
            raise TxError(f"RC-16:SEVERITY-BASE: VIS-FIRM-FINANCE-SEVERITY.limitations_{lang} is not the expected two-part field")
        t06.set("RC-16:SEVERITY-BASE", "VIS-FIRM-FINANCE-SEVERITY", f"limitations_{lang}", cur.rstrip() + add, cur)
    rep = s.save(out, ledger, OrderedDict([("transaction", "RC-16"), ("summary", "Addendum 2 lessons: no undated 'latest' label; survey coverage stated"),
                                           ("items", OrderedDict([("titles", len(TITLES)), ("descriptions", len(DESCRIPTIONS)),
                                                                  ("headings", len(HEADINGS)), ("coverage", 2 * len(COVERAGE_KEYS)), ("B15_B-7_title", len(SPINE)), ("severity_base", len(SEVERITY))]))]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
