# Arabic terminology and style ledger — سجل المصطلحات والأسلوب العربي

> **Execution-state correction (Tranche B execution, 2026-09-26).** D1 and D3 were re-adjudicated per cell under the recipient acceptance directive: «المنظومة» meaning the financial system stays; the product's self-reference is rendered by context — «هذا الموقع» (agentive, with masculine agreement rewritten in each window), «قاعدة الأدلة» (what the evidence base holds or lacks), «هنا» (locative), or an impersonal/passive verb — and «المنصة» is not used. «خلاصة» is applied only where the governed-claim sense is meant; the user-voiced QE-011 question keeps «الادعاء» (fact-checking sense). All 68 non-derived PB-0414 cells were revised by the Lead (audit/tranche_b_execution/stage5_execute.py R414; row outcomes in STAGE5_SWEEP_ROW_LEDGER.csv). The §3/§4 tables below record the Tranche B proposal; the executed text is the revised one. External native-speaker certification was not performed.


**Status:** `VERIFIED_BY_CLAUDE_TEAM` · `EXTERNAL_HUMAN_CERTIFICATION_NOT_PERFORMED` · `SPEC_PENDING_EXECUTION`

This ledger governs the Arabic edition, which is co-authoritative with the English: neither text is a translation of the other. Every change it motivates is a row in `MASTER_FIRST_PATCH_SPEC.csv`. The ledger itself installs nothing.

## 1. Standard

Public Arabic must read as if a senior Arab economic and financial editor wrote it:
- restrained and exact;
- clear to a non-specialist;
- free of translated-English cadence and repository vocabulary.

Smoothness never buys a weaker boundary. When a natural phrasing would drop a limit («لا يثبت»، «بحسب المصدر»، «في تاريخ محدد»), the limit stays.

## 2. Decisions

| # | Decision | Rows | Rationale |
|---|---|---|---|
| D1 | The noun for a governed "claim" is **«خلاصة» / «الخلاصات»**, and **«خلاصة مسندة»** where the evidentiary link must be explicit. | PB-0413 (39 cells + T01 + B01–B03), PB-0373, PB-0412 | In public Arabic «ادعاء» reads as "allegation", and next to «الدليل» it sounds prosecutorial. «خلاصة» names a finding drawn from evidence. «عبارة مسندة» and «إفادة» were rejected: the first is clumsy in headings and buttons, and the second implies testimony. |
| D2 | «ادعاء» / «الادعاء بأن» is **kept** where the sense is "to assert (without proof)". | 24 KEEP occurrences (`TERMINOLOGY_SWEEP_KEEP_REGISTER.csv`) | «من دون ادعاء إثباته»، «لا يجوز الادعاء بأن…»، «ولا ادعاء فعالية البرنامج» are idiomatic and exact. |
| D3 | The product's self-referent is **«المنصة»**. **«منظومة/المنظومة»** is reserved for the financial or financial-inclusion system. | PB-0414 (113 substitutions), B01, B02; 49 KEEP | «المنظومة» was used for both, so «لا تعرض المنظومة…» could be read as "the financial system does not show…". «المنصة» is feminine, so each substitution is one word and every agreement («تعرض»، «تفصل»، «لا تنسب») survives. «هذا المورد» would force masculine agreement throughout, with a high risk of error in a mechanical execution. Locative build.py string: «داخل المنظومة» → «هنا». |
| D4 | Authority is always qualified: **«البنك المركزي اليمني – عدن»**, and «– صنعاء» where a Sana'a instrument is meant. Never a bare «البنك المركزي» for a list or decision. | PB-0210–0216, PB-0513 | Scope of authority is evidence, not a political statement (LEAD-M02). |
| D5 | YPCC: **«الشركة اليمنية للمدفوعات والمقاصة»**, not «مركز اليمن للمقاصة…». | PB-0230 (`PRIMARY_SOURCE_PENDING` for the exact registered form) | The entity is a company, not a centre. The name must be confirmed from its founding instrument. |
| D6 | IMF 2018–2024 remittance values are **«تاريخ وفق تقديرات خبراء الصندوق»**, never «تاريخ مرصود». | Arabic rows of PB-0170–0196 | Evidence state is `HISTORICAL_REPORTED` / staff calculations (LEAD-B06). |
| D7 | "Active savers" as a source term is quoted: **«مدخر نشط»** in guillemets, attributed to the source. | PB-0121/0123/0144 and variants | The source's label, not a verified definition. |
| D8 | Survey levels come before differences: «تملك 5.44% من النساء و18.35% من الرجال حسابًا، بفارق 12.91 نقطة مئوية». The number word is «نقطة مئوية» (never «%» for a difference). | PB-0303/0305/0310, PB-0449/0450 | Binding correction #6. The precision of a derived value equals the precision of its inputs («9.0 نقاط»). |

## 3. «ادعاء» → «خلاصة» replacement table (exact, as executed by the sweep)

| Before (exact) | After | Where |
|---|---|---|
| افتح الادعاءات وسجلات الأدلة | افتح الخلاصات وسجلات الأدلة | 30 cells (03, 09 and 02 derived) |
| قد يتحول الرقم إلى ادعاء مختلف | قد يكتسب الرقم معنى مختلفًا | /data/ s3 (03 r70 and 02 r10) |
| للوصول إلى ادعاء أو مؤشر | للوصول إلى خلاصة أو مؤشر | /evidence/ (03 r83 and 02 r120) |
| ادعاءات عامة مسندة بالأدلة | {N_CLAIMS} خلاصة عامة مسندة بالأدلة (PB-0373) / خلاصات عامة مسندة بالأدلة | /data/ count line |
| الدليل وراء الادعاء، | الدليل وراء الخلاصة، | 05 QE-011 |
| في هذا الادعاء | في هذه الخلاصة | 06 r8 |
| يضيق نطاق الادعاء | يضيق نطاق الخلاصة | 06 r112, 07 r63 |
| الادعاءات التحليلية العامة (sheet title) | الخلاصات التحليلية العامة | 07 A1 |
| build.py: مربوطًا بالادعاءات والأدلة · لا يرقّيها إلى نتيجة أو ادعاء · ابحث في الادعاءات والأدلة والقراءات... | مربوطًا بالخلاصات والأدلة · لا يرقّيها إلى نتيجة أو خلاصة · ابحث في الخلاصات والأدلة والقراءات… | PB-0413.B01–B03 |
| Footer strapline: مورد عام يربط الادعاء بالدليل والمصدر. | مورد عام يربط كل خلاصة بدليلها ومصدرها الأصلي. | PB-0412, now governed in 04_NAV_UX |

## 4. «المنظومة» rules

**Replace with «المنصة»** when «المنظومة» is the grammatical subject or locus of an action the product performs:
- «لا تعرض المنظومة» → «لا تعرض المنصة»;
- «تفصل المنظومة» → «تفصل المنصة»;
- «الموثقة في المنظومة» → «الموثقة في المنصة»;
- «يمكن للمنظومة» → «يمكن للمنصة»;
- «معرفة المنظومة» → «معرفة المنصة».

**Keep «منظومة»** in these cases:
- the indefinite or construct form: «منظومة الشمول المالي»، «منظومة المدفوعات»، «منظومة التجار»، «منظومة انتقال»؛
- «المنظومة الأوسع»;
- the section label «سياق المنظومة» ("System context");
- «علاقات المنظومة»;
- «ما المنظومة التي تحاول الأدلة وصفها؟»;
- «جزء من هذه المنظومة» (the financial system);
- «موقع شركات الصرافة… في المنظومة»;
- «مجالات المنظومة»;
- «صورة مترابطة للمنظومة»;
- «التسلسل الزمني للمنظومة».

All 49 kept occurrences are listed with their rule in the KEEP register.

**Headings:** «لماذا القياس جزء من المنظومة؟» → «لماذا القياس جزء من المنصة؟». The English body says "connects the rest of the product", so the product is meant.

## 5. Calques removed

| Calque | Replacement principle | Rows |
|---|---|---|
| «كائن / كائنات» (object) | Name what is counted: «مقياس/مقاييس», «وحدات قياس», «الأعداد الإدارية», «سجلات», «مؤشر كمي», «قيمة مشتقة». In titles: «مقابل المقاييس الإدارية الحالية». | PB-0530–0551 (38 occurrences, 0 residual) |
| «منزوَع الازدواج» | «بعد إزالة الازدواج» / «خالية من الازدواج» | PB-0552–0555 |
| «صفًا مصرفيًا / صفًا للبنوك» (bank rows) | «26 بنكًا»، «تحدد المنصة 12 منها كبنوك تمويل أصغر استنادًا إلى وصف المصدر» | PB-0201/0224/0225 |
| «الخاضعة للحوكمة» in public copy | «الموثقة» (not «المعتمدة», which would assert institutional approval) | PB-0550/0551 |
| «الكون» (universe) | «المجموعة الكاملة / الحالية لمقدمي الخدمات», «المجتمع المقيس», «النطاق المقيس», «قائمة الجهات المرخصة» | PB-0600–0607, PB-0595 (0 residual) |
| «ساعات الأدلة» (evidence clocks) | Not introduced. /people/ title: «الأفراد: مجتمع سكاني واحد، وأدلة من تواريخ مختلفة» | PB-0526 |

«عنصر» (16 uses) was reviewed and **kept**. In context it reads naturally («عنصر تحليلي»، «عناصر الإصلاح»).

## 6. Canonical term matrix (public Arabic)

These terms are already dominant in the corpus unless marked **new**. Where the English has a variant, the English column shows the governed form.

| English | Arabic (governed) | Note |
|---|---|---|
| claim / evidence-backed claim | خلاصة / خلاصة مسندة | new (D1) |
| evidence record | سجل الدليل | in use (22×) |
| source record · original link | سجل المصدر · الرابط الأصلي | |
| Evidence Readings | قراءات الأدلة | nav already migrated |
| Measurement Agenda | أجندة القياس | |
| Methodology · Method & Measurement | المنهجية · المنهج والقياس | PB-0422 |
| Data & sources | البيانات والمصادر | PB-0421 |
| account ownership | امتلاك الحساب | |
| percentage point | نقطة مئوية | never «نقاط مئوية %» |
| calculation base / denominator | قاعدة الاحتساب (381×); قاعدة القياس for survey measures | «المقام» is not used |
| population covered / universe | المجتمع الذي يغطيه المصدر / نطاق المصدر | avoid «الكون» |
| nominal · real · USD-equivalent | اسمي · حقيقي (بالقيمة الحقيقية) · ما يعادله بالدولار الأمريكي | never «حقيقي» for an FX conversion (directive A) |
| estimate · projection · reported history | تقدير · توقعات/إسقاطات · تاريخ مُبلَّغ عنه / وفق تقديرات خبراء الصندوق | D6 |
| vintage / publication version | نسخة النشر · إصدار | |
| deduplication | إزالة الازدواج | §5 |
| exchange company · exchange establishment · remittance agent | شركة صرافة · منشأة صرافة · وكيل حوالات | source categories, never summed |
| licensed bank · microfinance bank | بنك مرخص · بنك تمويل أصغر | |
| e-wallet · subscriber · POS terminal · transaction | محفظة إلكترونية · مشترك · جهاز نقطة بيع · معاملة | |
| payment rails / infrastructure | البنية التحتية للمدفوعات · أنظمة الدفع | «سكك الدفع» (3 existing uses) is acceptable in the system map; prefer «أنظمة الدفع» in prose |
| RTGS · FPS | نظام التسوية الإجمالية الفورية · نظام الدفع السريع | |
| Global Findex | المؤشر العالمي للشمول المالي (Findex) | acronym kept in parentheses |
| target · baseline · result | مستهدف · خط الأساس · نتيجة | |
| listing / licensing ≠ operation | الإدراج أو الترخيص ≠ التشغيل | |
| does not establish | لا يثبت | preferred over «لا يدل» for evidentiary limits |

## 7. Tier-1 native text — keep as is

The Arabic specialist judged these as reading natively. They were **not rewritten**:
- the 11 governed questions (05), except QE-011's noun (D1);
- the 10 Reading titles;
- the 10 Measurement titles;
- the Home hero.

## 8. Certification

The decisions and every Arabic row are `VERIFIED_BY_CLAUDE_TEAM`. Native-speaker certification by an external Arab financial editor was **not performed** (`EXTERNAL_HUMAN_CERTIFICATION_NOT_PERFORMED`). A certifier should start with D1, D3 and §5, since those are the highest-frequency changes.

## 9. Appended 10 October 2026 — the governed terminology register (extends §6; nothing above is rewritten)

The owner's brief of 10 October 2026, Part B, under the steward designation of
`audit/OWNER_DECISIONS_2026-10-10.md` (OWN-NAME-01). The authoritative copy of this register is the Master, in a new
declared block of `04_NAV_UX`, "Governed terminology register / سجل المصطلحات الخاضعة للحوكمة", written by transaction
PN-1 and declared in `scripts/projection/master_structure.json`. It is mirrored here because this is where an Arabic
editor looks first. The full reasoning, the dissents and the hypotheses that were overturned are in
`audit/public_naming/PUBLIC_NAMING_LOG.md`. Certification status is unchanged: `EXTERNAL_HUMAN_CERTIFICATION_NOT_PERFORMED`.

### 9.1 Remittances — the gap §6 left open

§6 has no entry for remittances, and both «الحوالات» and «التحويلات» were in use, including for the same page. They
are **not** drift and are **not** collapsed into one term. The corpus already works the distinction deliberately:
«سلسلة التحويلات الكلية لا تقيس حجم الحوالة غير الرسمية» — the published series in one word, the individual remittance
in the other, in one sentence, correctly.

| English | Arabic (governed) | Do not use | Rule |
|---|---|---|---|
| remittances (the operation: the flow, the corridor, the channel, the method, the cost, the agent, the recipient) | **الحوالات** (sing. «حوالة») | «التحويلات» as the generic word for remittances; «تحويلات العاملين» as a generic term (it is a pre-BPM6 concept — source captions only) | «الحوالات» names the operation. «وكيل حوالات» for a remittance agent is unchanged (§6). |
| a published balance-of-payments or national-accounts remittance series, aggregate, revision, vintage or scope | **التحويلات**; **التحويلات الشخصية** only where the source's caption says personal transfers | «الحوالات» | The concept name belongs to the source. A changed concept name is a changed universe. |
| cash transfers (humanitarian or social assistance) | **التحويلات النقدية** | «الحوالات»; "remittances" in English | The payer is a programme, not a person. 102 governed occurrences; none was changed. |
| domestic cash remittance transfers under CBY-Aden Governor's Decision (23) of 2024 | **الحوالات النقدية الداخلية** | — | Already correct; one word from «التحويلات النقدية», so never touched by a sweep. |
| a transfer instruction between accounts | **تحويل مصرفي** / **حوالة مصرفية**, as the source has it | a substitution of either | Never substituted. |

**No mechanical replacement is permitted.** Substituting «التحويلات» with «الحوالات» is allowed only when the token
stands alone (not followed by «النقدية»، «الحكومية»، «الشخصية»، «المالية»، «الداخلية»، «المصرفية»، «الواردة»), the
sentence is about money sent rather than about a series, and the string is not inside a quoted source title, a chart
or source caption, a decision title, a filter value, a search alias or a clause attributing the word to a source. Any
doubt: do not replace. PN-1 replaced **one label and one title prefix** and left all 1,451 governed occurrences of
«التحويلات» in prose untouched.

### 9.2 Licence — the two senses

| English | Arabic (governed) | Do not use | Rule |
|---|---|---|---|
| licence (reuse / copyright) | **رخصة** | «ترخيص» for the reuse licence | The instrument content is made available under; here CC BY 4.0 for CauseWay's own content. |
| licensing (regulatory) | **ترخيص** | «رخصة» for regulatory licensing | The act and status of being licensed by a financial authority, as that authority recorded it on a date. A licence or a listing does not establish operation (the semantic firewall, and §6's «الإدراج أو الترخيص ≠ التشغيل»). |

The public copy was already right: `/rights/` uses «رخصة المشاع الإبداعي» and «الرخصة» for the reuse instrument, and
every «مرخص / مرخصة / الترخيص» in the interface copy and the visual contracts is regulatory. **CauseWay is not a
licensed financial institution and claims no such status** (`audit/OWNER_DECISIONS_2026-10-10.md`, OWN-04-R-a).
Nothing was changed under this rule; it is recorded so it cannot drift.

Note on institutional practice: the World Bank's own Arabic terms-of-use page uses both «رخصة المشاع الإبداعي» and
«مرخصة بموجب الترخيص» for a copyright licence. This rule is therefore clearer than institutional practice, not a copy
of it.

### 9.3 Labels retired on 10 October 2026, and what replaced them

Each retired Arabic string is kept working by a search alias, so no reader's typed word stops finding its page.

| Retired | Replaced by | Alias that keeps the retired word working |
|---|---|---|
| «استكشف» as the questions hub's name (it stays a verb elsewhere) | «الأسئلة الرئيسية» | SEARCH-ALIAS-034 |
| «البيانات والمصادر» | «المصادر» | SEARCH-ALIAS-035 |
| «أبلغ عن مشكلة» | «أبلغ عن خطأ» | SEARCH-ALIAS-036 |
| «الوصول» (bare, as the /access/ domain label) | «الوصول إلى الخدمات المالية» | SEARCH-ALIAS-037 |
| «مقدمو الخدمات» (bare) | «مقدمو الخدمات المالية» | SEARCH-ALIAS-038 |
| «التحويلات» as the /remittances/ domain label | «الحوالات» | SEARCH-ALIAS-005, 016, 032 (already in place) |
| «الثقة والاستخدام المسؤول» (footer group) · «روابط الثقة» · «روابط المنتج والثقة» | «عن الموقع وسياساته» · «روابط المعلومات والسياسات» · «روابط الموقع والسياسات» | not search targets |
| «قراءة أدلة» (the item's eyebrow) | «قراءة» | SEARCH-ALIAS-005 is unrelated; the Reading routes are found by title |
| «الاستشهاد بهذه الصفحة» (the colophon's second form) | «استشهد بهذه الصفحة», the one form | not a search target |
| «مستخدم في» (a /data/ facet) | «مجال الاستخدام» | not a search target |

### 9.4 Corrections to §6, recorded not rewritten

- §6's row "Measurement Agenda | أجندة القياس" is **stale against executed content**. The Arabic is
  «أولويات القياس» (23 governed occurrences against 2 for «أجندة القياس», both of which are search-alias terms kept so
  the retired word still finds the page), and from 10 October 2026 the English is "Measurement priorities". The object
  type is «أولوية القياس».
- §6's row "Data & sources | البيانات والمصادر" is superseded: the page is "Sources / المصادر" (§9.3). It becomes
  "Sources and data / المصادر والبيانات" only when a machine-readable file of the published evidence is downloadable
  from this site and reachable from that page.
- §6's row "Evidence Readings | قراءات الأدلة" stands in Arabic. The English takes sentence case, "Evidence readings",
  and the **item's** eyebrow becomes "Reading / قراءة". The collection is never called "Analysis" or «التحليلات»:
  «التحليلات» already names analytics on `/privacy/`, and "Analysis" / «التحليل» already names a section role on 31
  page sections.

### 9.5 Left open for a native certifier

- **«إتاحة الوصول» for Accessibility.** The independent Arabic editor judges «إمكانية الوصول» the settled Arabic term,
  and it has 11 governed uses elsewhere; «إتاحة الوصول» has 47. The information-architecture review argues the other
  way, because keeping the two apart is what stops bare «الوصول» doing three jobs. Not changed; escalated
  (`design/ESCALATIONS.md`, 10 October 2026).
- **«مقدمو الخدمات المالية» and «الوصول إلى الخدمات المالية».** Adopted over a red-team objection that each may be
  read as a status or a completed relation. Both are strings the Master already governed elsewhere, and both English
  labels are unchanged. The owner may reverse either.
