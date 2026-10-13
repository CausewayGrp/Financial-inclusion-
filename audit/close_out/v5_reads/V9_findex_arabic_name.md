# V9 — Arabic-editor ruling: the Arabic name of the Global Findex (11 October 2026)

Asked by the Stage A final instruction v5, §9 ("ARABIC-EDITOR QUESTION, not a change in this run"). The Arabic-editor lens
ran read-only; nothing was changed. No microdata and no API key were used.

## The World Bank's own Arabic (read 11 October 2026)

- blogs.worldbank.org/ar/voices/digital-technology-is-unlocking-financial-inclusion («التكنولوجيا الرقمية تعزز الشمول
  المالي»; datePublished 2025-08-07): the tag and the product reference read «قاعدة بيانات المؤشر العالمي للشمول المالي»;
  the body also writes «مؤشر الشمول المالي العالمي», «المؤشر العالمي لتعميم الخدمات المالية» and «المؤشر العالمي للتمويل
  المالي».
- blogs.worldbank.org/ar/voices/Mobile-phone-ownership-is-widespread-Why-is-digital-inclusion-still-lagging
  (datePublished 2025-10-24): «…مؤشر تتبع الاتصال الرقمي ضمن المؤشر العالمي للشمول المالي».
- Not usable: worldbank.org/ar/publication/globalfindex redirects to albankaldawli.org, which returned 404; data and
  documents pages carry the title in English only. No official Arabic report summary or Arabic press release was found.
- Not the World Bank (search titles only, not fetched): FinDev Gateway «قاعدة بيانات المؤشر العالمي للشمول المالي 2025»;
  Egyptian press «تقرير المؤشر العالمى للشمول المالى».

## Counts in the repository (raw bytes, `grep -roF | wc -l`)

| Form | site-src/content | dist/ar |
|---|---|---|
| «المؤشر العالمي للشمول المالي» (all, including inside the longer form) | 584 (page_specs 460) | 194 (about 107 in visible text) |
| «قاعدة بيانات Global Findex» | 108 | 5 (all «(قاعدة بيانات Global Findex، المصدر 28)») |
| «قاعدة بيانات المؤشر العالمي للشمول المالي (Global Findex)» | 20 | 25 |

The instruction's 574 is not reproduced (584 here; its counting method is not stated).

## Ruling

1. «المؤشر العالمي للشمول المالي» is established usage, and it is the World Bank's own Arabic in its 2025 Arabic blogs. It
   is not an error, though the World Bank's own Arabic is itself inconsistent.
2. «مؤشر» can read as a single composite index; it does not read as a ranking («تصنيف»/«ترتيب»). The risk is small because
   the site nearly always adds «(Global Findex)», and smaller still when «قاعدة بيانات» comes first.
3. The inconsistency matters more than either form. Three forms name one source, and one of them is a hybrid of Arabic
   and English, so a reader cannot tell whether one object is named or two.
4. Recommendation, for one future Master transaction rather than a find-replace:
   - the first mention on a page, and the source-library title: «قاعدة بيانات المؤشر العالمي للشمول المالي (Global
     Findex)»;
   - later mentions: «Global Findex» or «قاعدة البيانات»;
   - retire «قاعدة بيانات Global Findex»;
   - keep respondent counts, editions and «المصدر 28» byte-stable.

Recorded in the register as AR-FINDEX-NAME (OWNER-OPTIONAL). Nothing was changed in this run.

Confidence: high on the counts. Medium-high that the form is established, because it rests on two official Arabic blogs.
