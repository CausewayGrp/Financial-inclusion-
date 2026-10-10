# Public naming and terminology — decisions of 10 October 2026 (transaction NB-1)

Owner brief "Rights closure + public naming and terminology", Part B (10 October 2026). The owner designated this session
programme steward for the naming change (`audit/OWNER_DECISIONS_2026-10-10.md`). **The owner approves the final labels;
naming is the product's public identity. This record is the proposal; it is not merged until the owner says "merge".**

## How the labels were decided (B2)

Four independent reviewers, none of whom saw the others' work, then the lead's decision:

- an Arabic editor (native economic-editor standard), judging each label as Arabic, not as a translation;
- an English editor (World Bank, BIS and GOV.UK house style);
- an information-architecture lead (distinctness, first-click clarity, and where each label propagates);
- a red team reading every candidate as five personas: a Yemeni citizen on a phone, a journalist, a CBY official, a researcher and a donor.

Benchmarks fetched on 10 October 2026 (only what was seen is cited):

- World Bank, English and Arabic: "Research & Publications" / «البحوث والمطبوعات», with the conjunction spelled out in Arabic.
- Global Findex 2025: Report, Visualizations, Download data, Methodology; sentence case.
- BIS: "Research & publications", "Data Portal"; footer has "Copyright and permissions", "Terms and conditions", "Privacy notice".
- Our World in Data: Data, Resources, About; footer licence line "licensed under CC BY" with a link to the deed.
- CGAP: About, Research, Topics.
- GOV.UK style guide: "Always use sentence case, even in page titles"; "Use 'and' rather than '&'".
- IMF, OECD, UN ESCWA and the Arab Monetary Fund returned HTTP 403 to the fetch and are not cited.

**The pattern:** top-level labels are nouns, and imperatives appear only as calls to action.

## (a) The final label table

| Label (id) | Old EN | Old AR | New EN | New AR | Decision | Reason |
|---|---|---|---|---|---|---|
| Global nav 01 (NAV-EXPLORE) | Explore | استكشف | Questions | الأسئلة | CHANGE | An imperative among nouns reads as a button; matches the page's own h1 «Start with the question» |
| Global nav 02 (NAV-EVIDENCE) | Evidence | الأدلة | Evidence | الأدلة | KEEP | KEEP — clear, distinct |
| Global nav 03 (NAV-READINGS) | Evidence Readings | قراءات الأدلة | Readings | القراءات التحليلية | CHANGE | Drops the repeated 'Evidence'; «التحليلات» means web analytics on /privacy/ and 'Analysis' collides with 31 in-page eyebrows; bare «القراءات» suggests Quranic readings |
| Global nav 04 (NAV-DATA) | Data & sources | البيانات والمصادر | Sources | المصادر | CHANGE | Over-promised: no dataset is downloadable (public_downloads = false); becomes 'Sources and data / المصادر والبيانات' on the day downloads go live (rule in 04 R-017 and TERM-020) |
| Global nav 05 (NAV-METHOD-MEASUREMENT) | Method & Measurement | المنهج والقياس | Method and measurement | المنهج والقياس | CHANGE | Sentence case and 'and' (GOV.UK; BIS, OWID, Findex use sentence case) |
| Nav child (NAV-MEASUREMENT) | Measurement Agenda | أولويات القياس | Measurement priorities | أولويات القياس | CHANGE | EN and AR named the same thing differently; matches the object type |
| Nav child (NAV-METHODOLOGY) | Methodology | المنهجية | Methodology | المنهجية | KEEP | KEEP |
| Footer group (explore_verify, contract) | Explore and verify | الاستكشاف والتحقق | Main sections | الأقسام الرئيسية | CHANGE | Its links are nouns now |
| Footer group / trust h3 (trust_use, contract) | Trust and responsible use | الثقة والاستخدام المسؤول | About and policies | عن هذا المورد وسياساته | CHANGE | 'Trust' is jargon; «هذا» avoids reading «المورد» as «المورِّد» (supplier) |
| Trust link /about/ (04 r608) | About | عن الموقع | About | التعريف بهذا المورد | CHANGE | The product calls itself «هذا المورد»; the link must not repeat its group heading |
| Trust link /rights/ (04 r610) | Rights & reuse | الحقوق وإعادة الاستخدام | Rights and reuse | حقوق إعادة الاستخدام | CHANGE | 'and'; the AR was 23 characters, over the phone-menu length |
| Trust link /accessibility/ (04 r611) | Accessibility | إتاحة الوصول | Accessibility | إمكانية الوصول | CHANGE | «إتاحة الوصول» collides with the Access domain |
| Trust link /terms/ (04 r613) | Terms | شروط الاستخدام | Terms of use | شروط الاستخدام | CHANGE | 'Terms' is ambiguous on a terminology site; matches the AR |
| Trust links /corrections/, /privacy/, /contact/ | Corrections · Privacy · Contact | التصحيحات · الخصوصية · التواصل | (same) | (same) | KEEP | KEEP |
| Utility (contract utilities.report_issue) | Report an issue | أبلغ عن مشكلة | Report an error | أبلغ عن خطأ | CHANGE | Matches /contact/; «مشكلة» reads as a complaint about a bank or wallet |
| Utilities: Search, Cite this page | Search · Cite this page | بحث · استشهد بهذه الصفحة | (same) | (same) | KEEP | KEEP |
| Domain /people/ | People | الأفراد | People | الأفراد | KEEP | KEEP (route dictionary aligned: People & Needs / الناس والاحتياجات retired) |
| Domain /firms/ | Firms | المنشآت | Firms | المنشآت | KEEP | KEEP (route dictionary aligned) |
| Domain /finance/ (UI-LAND-DOM-FINANCE) | Finance | التمويل | Banks and microfinance | البنوك والتمويل الأصغر | CHANGE | On a financial-inclusion site everything is finance; the page covers microfinance and bank balance sheets. Rejected: 'Credit and savings' (promises consumer help), 'Financial system' (over-promises) |
| Domain /providers/ (UI-LAND-DOM-PROVIDERS) | Providers | مقدمو الخدمات | Providers | مقدمو الخدمات المالية | CHANGE | Bare «مقدمو الخدمات» suggests telecoms or utilities |
| Domain /payments/ | Payments | المدفوعات | Payments | المدفوعات | KEEP | KEEP (route dictionary aligned) |
| Domain /remittances/ (UI-LAND-DOM-REMITTANCES) | Remittances | التحويلات | Remittances | الحوالات | CHANGE | Bare «التحويلات» also means cash and bank transfers |
| Domain /access/ (UI-LAND-DOM-ACCESS) | Access | الوصول | Access | الوصول إلى الخدمات | CHANGE | «الوصول» alone is incomplete in Arabic |
| Domain /reforms/ | Reforms | الإصلاحات | Reforms | الإصلاحات | KEEP | KEEP (route dictionary aligned) |
| Domain h1 prefixes (02 titles) | 7 of 8 EN; 5 of 8 AR | — | 8 of 8 | 8 of 8 | CHANGE | Parity: /providers/ and /access/ gain an AR prefix, /reforms/ gains one in both languages; /finance/ and /remittances/ carry their new names |
| <title> / og:title of hubs and domains (renderer) | the dated thesis | the dated thesis | {stable name} — Yemen Financial Inclusion Evidence | {stable name} — أدلة الشمول المالي في اليمن | CHANGE | Tabs, search results and shares no longer go stale; the h1 keeps the thesis; Readings, records and policy pages keep their own titles (TC-G02) |
| /readings/ title and h1 (02 r137) | Evidence Readings | قراءات الأدلة | Readings | القراءات التحليلية | CHANGE | Its navigation name |
| UI-HEADER-REPORT-AN-ISSUE | Report an issue | أبلغ عن مشكلة | Report an error | أبلغ عن خطأ | CHANGE | Matches /contact/ ('Contact and report an error'); 'مشكلة' reads as a complaint about a bank or wallet |
| UI-EVID-REPORT-AN-ISSUE | Report an issue | أبلغ عن مشكلة | Report an error | أبلغ عن خطأ | CHANGE | Same action, same label as the header tool |
| UI-JS-COPY-LONG-CITATION | Copy long form | (unchanged) | Copy long citation | (unchanged) | CHANGE | 'long form' does not say what is copied |
| UI-READING-RETURN | (unchanged) | عد إلى السؤال | (unchanged) | ارجع إلى السؤال | CHANGE | Unvowelled «عد» also reads as 'count' |
| UI-EVID-RETURN-TO-INTERPRETATION | (unchanged) | عد إلى التفسير | (unchanged) | ارجع إلى التفسير | CHANGE | Unvowelled «عد» also reads as 'count' |
| UI-COLOPHON-CITATION | (unchanged) | الاستشهاد بهذه الصفحة | (unchanged) | استشهد بهذه الصفحة | CHANGE | Same action as the page tool, same imperative form |
| UI-READING-EYEBROW | Evidence Reading | قراءة أدلة | Reading | قراءة تحليلية | CHANGE | One genre name everywhere; the section is 'Readings' |
| UI-READING-FEATURED | Featured Reading | قراءة مختارة | Featured reading | قراءة تحليلية مختارة | CHANGE | Sentence case; one genre name |
| UI-READING-ALL-H | All Evidence Readings | كل قراءات الأدلة | All readings | كل القراءات التحليلية | CHANGE | Sentence case; drops the repeated 'Evidence' |
| UI-EVIDENCE-USED-IN-READINGS | Used in these Evidence Readings | يُستخدم هذا الدليل في قراءات الأدلة الآتية | Used in these readings | يُستخدم هذا الدليل في القراءات التحليلية الآتية | CHANGE | One genre name |
| UI-DOM-EVIDENCE-READINGS-ON-THIS-QUESTION | Evidence Readings on this question | قراءات الأدلة المتعلقة بهذا السؤال | Readings on this question | القراءات التحليلية المتعلقة بهذا السؤال | CHANGE | One genre name |
| UI-DATA-READINGS-USING-SOURCE | Evidence Readings using this source | قراءات الأدلة التي تستخدم هذا المصدر | Readings using this source | القراءات التحليلية التي تستخدم هذا المصدر | CHANGE | One genre name |
| UI-JS-TYPE-READING | (unchanged) | قراءة | (unchanged) | قراءة تحليلية | CHANGE | One genre name; the search result type |
| UI-READING-DO-NOT-INFER | (unchanged) | ما لا يُستنتج | (unchanged) | ما لا ينبغي استنتاجه | CHANGE | «ما لا يُستنتج» is ambiguous ('what cannot be inferred'); matches the Home h2 |
| UI-DOM-WHAT-NOT-TO-CONCLUDE | (unchanged) | ما لا يُستنتج | (unchanged) | ما لا ينبغي استنتاجه | CHANGE | Same heading, same wording |
| UI-JS-COMPARE-BOUNDARY | (unchanged) | ما لا يُستنتج | (unchanged) | ما لا ينبغي استنتاجه | CHANGE | Same heading, same wording |
| UI-VIS-STATE-UNKNOWN | (unchanged) | غير معروف — ليس صفرًا | (unchanged) | غير معروف — لا يعني صفرًا | CHANGE | «ليس صفرًا» reads as 'the value is not zero'; the rule is that missing does not mean zero |
| UI-VIS-MISSING | (unchanged) | لا قيمة موثَّقة لهذه الفترة — ليست صفرًا | (unchanged) | لا قيمة متحقَّق منها لهذه الفترة — وهذا لا يعني صفرًا | CHANGE | English says 'verified', not 'documented'; same zero rule |
| UI-VIS-CHAIN-OPEN | (unchanged) | لم تُقس بعد — ليس إخفاقًا | (unchanged) | لم تُقس بعد — وهذا لا يعني إخفاقًا | CHANGE | Same construction as the zero rule |
| UI-VIS-RESULT-NOT-HELD | (unchanged) | لا تتضمن قاعدة الأدلة نتيجة مرصودة — ليست صفرًا | (unchanged) | لا تتضمن قاعدة الأدلة نتيجة مرصودة — وهذا لا يعني صفرًا | CHANGE | Same zero rule |
| UI-LAND-COV-SUFFICIENT_FOR_QUESTION | Sufficient for its question | كافٍ لسؤاله | Sufficient for the question | كافٍ للإجابة عن السؤال | CHANGE | «كافٍ لسؤاله» is opaque |
| UI-LAND-CLASS-REGULATORY | (unchanged) | مادة تنظيمية | (unchanged) | نص تنظيمي | CHANGE | «مادة» reads as 'article of a law' |
| UI-LAND-CLASS-CONTEXT | Context source | (unchanged) | Contextual source | (unchanged) | CHANGE | Adjective form, parallel to the other classes |
| UI-DATA-FILTER-DOMAIN | (unchanged) | مستخدم في | (unchanged) | يُستخدم في | CHANGE | «مستخدم» reads as 'user' |
| UI-DATA-FILTER-CLEAR | (unchanged) | مسح عوامل التصفية | (unchanged) | إلغاء التصفية | CHANGE | «مسح» means 'survey' on this site |
| UI-DATA-SORT | Order | (unchanged) | Sort by | (unchanged) | CHANGE | 'Order' is ambiguous (an order, a decree) |
| UI-COLOPHON-H | Evidence colophon | بيان الأدلة | About this edition | معلومات الإصدار | CHANGE | 'Colophon' is printers' jargon; «بيان الأدلة» reads as 'statement of evidence' |
| UI-HEADER-TRUST-LINKS | Trust links | روابط الثقة | About and policies | عن هذا المورد وسياساته | CHANGE | Screen-reader name of the footer group; 'trust' is jargon |
| UI-FOOTER-PRODUCT-AND-TRUST-LINKS | Product and trust links | روابط المنتج والثقة | Site sections | أقسام المورد | CHANGE | Jargon removed |
| UI-CRUMB-BREADCRUMB | (unchanged) | مسار الصفحة | (unchanged) | مسار التنقل | CHANGE | The usual Arabic term for a breadcrumb |
| UI-404-EXPLORE | Explore | استكشف | Questions | الأسئلة | CHANGE | Same as the navigation item it links to |
| UI-EVID-DATA-SOURCES | Data & sources | البيانات والمصادر | Sources | المصادر | CHANGE | Same as the navigation item it links to |
| UI-EVID-CORRECTIONS-RELEASE-HISTORY | Corrections & release history | (unchanged) | Corrections and release history | (unchanged) | CHANGE | 'and', not '&' |
| UI-LAND-DOM-FINANCE | Finance | التمويل | Banks and microfinance | البنوك والتمويل الأصغر | CHANGE | On a financial-inclusion site everything is finance; the page covers microfinance and bank balance sheets |
| UI-LAND-DOM-REMITTANCES | (unchanged) | التحويلات | (unchanged) | الحوالات | CHANGE | Bare «التحويلات» also means cash and bank transfers |
| UI-LAND-DOM-PROVIDERS | (unchanged) | مقدمو الخدمات | (unchanged) | مقدمو الخدمات المالية | CHANGE | Bare «مقدمو الخدمات» suggests telecoms or utilities |
| UI-LAND-DOM-ACCESS | (unchanged) | الوصول | (unchanged) | الوصول إلى الخدمات | CHANGE | «الوصول» alone is incomplete and collides with the accessibility statement |

## (b) The glossary rules applied, with counts

| Rule | Applied | Count |
|---|---|---|
| remittances = الحوالات where the meaning is identical (six conditions T1–T6: person-to-person flow; payer not a government or programme; not the act of transferring; not inside a quoted title or label; the English says "remittance"; nothing but the noun moves) | Master text cells, cell by cell (`nb_1_remittance_substitutions.json`, each with its English counterpart and the six tests) | **102 cells** swapped (one of them, CLM-035's meta description, restored to the bank's own label by NB-2); 25 kept by ruling (19 balance-of-payments metric labels in 23_REMITTANCES keep the source's concept; CLM-035 keeps the bank's own label; the sheet header row; 04 r531 is the domain label above); 63 further occurrences kept by test (cash transfers 15, government or programme transfers 10, titles and source labels 26, other meaning 8, the act of transferring 4) |
| regulatory licensing = الترخيص where «الرخصة» meant it ("القائمة أو الرخصة") | CLM-018 (06) and VIS-PROVIDER-OBSERVABILITY (11) | **4 cells** |
| web accessibility = إمكانية الوصول where «إتاحة الوصول» meant accessibility (not where it means access to services: 03 /explore/ s6 is kept) | /accessibility/, /contact/, the trust link | **8 cells** |
| missing ≠ zero: «ليس صفرًا» (reads as a stated value) → «لا يعني صفرًا» | four state labels | **4 labels** |
| one genre name: Reading / قراءة تحليلية; section Readings / القراءات التحليلية | navigation, breadcrumb, eyebrow, featured, lists, search type | **9 labels** |
| copyright licence = رخصة; licence (noun) / license (verb) | register only; the public text already used رخصة for CC BY 4.0 | 0 changes |

A governed terminology register is added to the Master: titled block "Terminology register" in 04_NAV_UX. It holds 21
concepts, each with EN, AR, definition (EN, AR), variants not to use, and the rule (EN, AR). It is projected to
`site-src/content/content/terminology_register.json`, which is reference material and not rendered.

## (c) What was rejected from the advisor's hypotheses, and why

- **H2 "Analysis / التحليلات" — rejected; adopted "Readings / القراءات التحليلية".**
  - «التحليلات» already means web analytics on /privacy/.
  - "Analysis" is a section eyebrow on 12 pages (31 uses), and it collides with the evidence class "Secondary analysis" and the /data/ group "Research and analysis".
  - None of the benchmarked institutions uses "Analysis" as a navigation label.
  - The genre name stays one word in each language.
- **H6 "عن المورد" — refined to «عن هذا المورد وسياساته» and «التعريف بهذا المورد».**
  - Without diacritics, «المورد» reads as «المورِّد» (supplier); «هذا» removes that reading and matches the product's own self-reference.
- **H8 "Credit and savings / الائتمان والادخار" — rejected; adopted "Banks and microfinance / البنوك والتمويل الأصغر".**
  - "Credit and savings" promises consumer help.
  - The page covers microfinance and bank balance sheets.
  - "Financial system" (the IA lead's option) over-promises.
- **H9 "التحويلات المالية من الخارج" — rejected.**
  - It is wordy and excludes domestic remittances.
  - «التحويلات المالية» also means funds transfers.
  - In balance-of-payments text the source's own concept is kept instead.
- **H10 — the stable `<title>` applies to the eight domains and the six hubs; Readings keep title = h1** (gate TC-G02).
- **H11 — agreed: the product name, "Evidence record / سجل الدليل", "How to read this evidence" and «هذا المورد» are unchanged.**
  - The Reading eyebrow «قراءة أدلة» was not protected and changes.
- **Red-team options not adopted:**
  - "Key questions" (the Arabic and English editors judged the FAQ risk low beside content nouns);
  - "Evidence gaps" for /measurement/ (it changes what the page is called, not just how);
  - «تحويلات المغتربين» as the domain name (it excludes domestic remittances; it is kept as a search alias for the balance-of-payments concept).
- **Kept as they are:**
  - the rubric "Understand → Explore → Verify" (a journey, not a navigation label);
  - the in-page "Analysis" eyebrows (no longer in conflict once the navigation says "Readings").

## (d) Downstream effects

- **Master:** `cf5254825da8` → `e444320569ae`, 271 cells.
- **Navigation contract** (`navigation_interaction.json`), steward edits closing this naming finding:
  - footer groups `explore_verify` and `trust_use`, and `utilities.report_issue`;
  - the navigation labels, breadcrumb parent labels and footer links are aligned by the generator from the Master.
- **Renderer:**
  - `<title>` and og:title carry the stable name of hubs and domains;
  - the footer licence line;
  - `<link rel="license">` in every page's head, linking each language's own CC deed.
- **Search:** 12 aliases added (SEARCH-ALIAS-034…045). Old labels keep finding their pages: Explore, Evidence Readings, Data & sources, Report an issue, Trust, Finance, Accessibility, Access, Providers, and the Arabic remittance and licensing terms.
- **Rights (B4):**
  - /rights/ section 6 states the exact scope:
    - covered: CauseWay's text, analysis, visual designs, compiled records and calculated figures, and the export structure;
    - not covered: third-party material; the CauseWay name, logo and marks; the repository's software code, which is outside this licence and on which nothing is decided.
  - Figures derived from the Global Findex microdata (the intervals in CLM-026) are covered by the World Bank Microdata Research License, with the citation that licence requires, and CC BY 4.0 does not extend to the underlying microdata.
  - The page links the deed and the legal code. An official Arabic legal code exists on creativecommons.org (`legalcode.ar`, HTTP 200), and the Arabic page links it.
  - Attribution follows CC's TASL practice (title, author, source, licence, and changes made) inside the two-line form.
  - No rights clearance, legal review or certification is claimed.
- **Social images:** 140 cards regenerated. **Diagrams:** the three architecture diagrams are redrawn, and their label literals are updated in `scripts/architecture_diagrams.py`.
- **Docs:** README, `handoff/CLAUDE_DESIGN_MASTER_PROMPT.md` §4.2 and `handoff/DESIGN_ACCEPTANCE_CRITERIA.md` use the new labels. History records are unchanged.
- **Unchanged:** routes, URLs, identifiers, `data-*` hooks, every figure, unit, period, universe and source.

## NB-2 — the independent review of NB-1

An independent reviewer who did not build NB-1 read every changed cell and the built pages, in both languages. It found
**no blocker**; the lead accepted its should-fix items and most of its nits. They were applied in transaction NB-2:
Master `e444320569ae` → `370d72a4cb40`, 38 cells, plus one renderer change.

- **Footer licence line, Arabic.** Now «تُتاح نصوص CauseWay وتحليلاتها وتصاميمها المرئية…»: CauseWay takes feminine
  agreement, as in the strapline and on /rights/.
- **Three labels NB-1 missed:**
  - /measurement/ section rubric: "Measurement priorities";
  - "P0/P1 among these measurement priorities" in the ten priority rationales;
  - /ar/terms/ «حقوق إعادة الاستخدام».
- **One grammar slip** after NB-1 made the subject plural: "They do not rank…".
- **CLM-035.** Its Arabic meta description keeps the bank's own label «التحويلات», as its body does.
- **Findex citation on /rights/.** It now has the year and place the source record's attribution requirement gives:
  (2022), Washington, DC: World Bank.
- **Licence addresses on /rights/ are links.** The deed and the legal code, each language's own, now link out. The
  renderer links only the official creativecommons.org licence addresses and no other address in governed text.
- **Rights page title.** It is now "Rights and reuse / حقوق إعادة الاستخدام", the name its link carries. It was "Source
  and data rights / حقوق المصادر والبيانات", and the Arabic over-promised data rights.
- **Informal hawala named as a system.** Now that «الحوالات» means remittances, the informal hawala system is
  «التحويلات عبر نظام الحوالة غير الرسمي» in 4 places.
- **Two substitutions whose English did not say "remittance"** were reworded:
  - the boundary note of SEARCH-ALIAS-032;
  - «ما تتسلمه الأسر من حوالات».
- **Missing ≠ zero in body text (TERM-021).** 6 cells: «لا يعني صفرًا», not «ليس صفرًا».
- **"Do not infer:"** is «لا تستنتج:», an instruction, as in English.
- **Arabic h1s of /access/ and /providers/** no longer repeat the domain name after the prefix.
- **TERM-001's rule** is narrowed to what was applied:
  - quote a source's own balance-of-payments label;
  - in running text, remittances = الحوالات.
- **SEARCH-ALIAS-044** gains "remittance fees", pairing its terms across the languages.

**Not changed, with reasons:**
- /404.html carries no footer, so it has no licence line.
- The two NEG-EW-011 redirect stubs have no `<title>` page head to carry `<link rel="license">`.
- "External sector" is rendered two ways in Arabic in two records (06 r29, r70). That is outside the naming scope and
  is left to the next editorial pass.

## If the owner rejects or edits a label

NB-1 is one transaction. A change to any label is made by editing `UI`, `NAV_SUBS` or `COPY_SUBS` in `nb_1_naming.py`
and replaying the transaction on the current `main` (it is exact-value-guarded).
