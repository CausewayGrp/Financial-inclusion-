# Public naming, terminology and rights presentation — log

The owner's brief of 10 October 2026, Part B, under the steward designation recorded in
`audit/OWNER_DECISIONS_2026-10-10.md` (OWN-NAME-01). **Nothing here is accepted: the owner approves names.** Nothing
here declares DESIGN HANDOFF READY anew or PUBLIC RELEASE READY, and nothing here claims WCAG conformance, legal
review, rights clearance, native-language certification or a security guarantee.

Entry state: pull request #16's head `9f53874775693a29f5a48cb87f5cde0e731b07ae`, Master
`cf5254825da8b06e8812ee0c033382270b731e1001c40bf6ad929f843f27278a`. This work is built on top of #16 so that nothing
has to be re-run later; if #16 is rejected, Part B rebases onto `main` and re-runs transaction PN-1 unchanged.

## 1. How it was decided

The question the brief asks is whether the words this product uses to name itself are the clearest, most professional
and most truthful available, in English and in Arabic, across every label a reader navigates by or relies on.

It was run as a hub and spoke. Five independent judgements, none of which saw another's:

| Role | What it was asked for |
|---|---|
| Arabic editor | Every Arabic label judged **as Arabic**, by the standard of IMF Arabic, World Bank Arabic, the Arab Monetary Fund and ESCWA; naturalness, exactness, distinctness, grammatical parity at each level, and length in RTL at 390 px |
| English editor | Every English label judged on first-click clarity for five readers, truthfulness, distinctness, consistency and length; one house rule for case and connectors, with its authority |
| Information-architecture lead | The label **system**: levels, parallelism within a level, one term per concept across every surface, the rename cost surface by surface, search continuity, and a rank by clarity ÷ disruption |
| Red team | Five personas (a Yemeni citizen on a phone, a journalist on deadline, a Central Bank of Yemen official, a researcher, a donor or programme team) run over the proposed labels, then the strongest argument against each proposal, then a fatal / survivable / safe verdict |
| Institutional benchmark | How the World Bank, IMF, BIS, OECD, Our World in Data, CGAP, the Arab Monetary Fund, ESCWA, Eurostat, the UK ONS and the GOV.UK style guide name the same things, in English and in Arabic, with the pages actually read |

The lead decided. Every label has KEEP or CHANGE with one line of reason (§3). Where a reviewer dissented from the
decision, the dissent is recorded (§3, §4) so the owner sees it.

### What the benchmark found, and the pages it rests on

Fetched live: worldbank.org (home, research, legal, the Global Findex publication page, the financial-sector and
financial-inclusion topic pages), data.worldbank.org (home, data portals and tools, data programs, summary terms of
use), blogs.worldbank.org; albankaldawli.org and data.albankaldawli.org in Arabic (home, topics, about, terms of use,
two remittance blog posts); imf.org (Data, Publications, Topics, Blogs) and imf.org/ar (home, F&D, WEO, departmental
papers, two Arabic articles); bis.org and data.bis.org (home, statistics, about, terms); ourworldindata.org (home,
poverty, latest, search, FAQs, about, one grapher page); cgap.org (home, topics, research, blog, about); Eurostat;
ons.gov.uk (home, economy, methodology); the GOV.UK style guide A-to-Z and writing guidelines, and the GOV.UK Design
System footer and page-template pages. **Not reachable:** oecd.org, unescwa.org and amf.org.ae returned bot
challenges, and the World Bank Open Knowledge Repository returned 403; those institutions' navigation, footers and
titles are therefore not verified here, and where they are cited below it is from a search result, marked as such.

1. **Navigation labels are nouns.** Every menu read — World Bank, World Bank Open Data, BIS, BIS Data Portal, Our
   World in Data, CGAP, Eurostat, ONS — is nouns. Imperatives appear in hero and card buttons ("Learn More",
   "Explore the data", "Download data", "Read the Report"), not in menus. Arabic menus likewise: the World Bank's
   Arabic Data navigation is all nouns, and its calls to action are imperative or infinitive. **No «استكشف» appeared
   in any Arabic menu or button read.**
2. **Topic-page `<title>`s are a stable name plus the site name**, never a thesis: "Poverty | Our World in Data",
   "Financial Inclusion | World Bank Group", "Statistics | Bank for International Settlements", "Digital Innovation |
   Financial Inclusion Topics | CGAP", "Economy - Office for National Statistics". Arabic titles often drop the site
   name ("الخدمات المالية").
3. **A section may share its item genre's name** — BIS "Speeches", CGAP "Blog", ONS "Blog" — so naming a section after
   the thing it holds is normal practice, not a defect.
4. **Case and connectors are split.** GOV.UK is explicit: "Always use sentence case, even in page titles and service
   names" and "Use 'and' rather than '&', unless it's a department's logo image or a company's name"; ONS and Eurostat
   follow it. The World Bank and CGAP use Title Case with "&"; BIS mixes sentence case with "&", and its page title
   reads "Terms & conditions" while its own heading reads "Terms and conditions". Both conventions exist; what does
   not exist anywhere is a site that keeps both at once, which is what this product does today.
5. **A directory with nothing downloadable is still titled "Data …" at the World Bank** ("Data Portals & Tools",
   "Data programs"). **No institution read uses "Sources" as a top-level label.** This is the one finding that
   argues against the decision taken in §3 #7, and it is recorded here for that reason.
6. **"Methodology" is a top-level or sub-navigation label** at ONS, Eurostat and the Findex site.
7. **Legal and policy pages cluster under "Legal" or "Legal information"**; ONS and Eurostat also use "Help". No
   footer group read carried "Corrections".
8. **Arabic «تحويلات» covers both senses.** The World Bank, IMF, Arab Monetary Fund and ESCWA all use
   «تحويلات العاملين / المغتربين / المهاجرين» for remittances and «التحويلات النقدية» for cash transfers; one IMF blog
   title uses «تحويلاتهم النقدية» for remittances. **«الحوالات» appeared on none of the four.** This argues against a
   pan-Arab institutional reading of «الحوالات» and is weighed in §3 #4 and §4.
9. **رخصة and ترخيص are not cleanly split in practice.** The World Bank's own Arabic terms page uses «رخصة المشاع
   الإبداعي» and «مرخصة بموجب الترخيص» for a copyright licence on one page. The distinction this product governs
   (§5, TERM-LICENCE-REUSE / TERM-LICENSING) is therefore a house rule that is clearer than institutional practice,
   not a copy of it.
10. **No institution read uses "Credit" or "Savings" as a topic label**: the World Bank has "Financial Services
    Sector" / «الخدمات المالية» beside "Financial Inclusion" / «الشمول المالي»; CGAP has "Financial Inclusion"; the
    IMF's nearest is "Digital Payments and Finance". This is weighed in §4.

## 2. The house rule

**Sentence case for every label, heading, navigation item, facet and page title** — capitalise only the first word,
proper nouns (Central Bank of Yemen – Aden, Global Findex), acronyms, record IDs and the product name — **and "and",
never "&"**. Authority: the GOV.UK style guide (capitalisation; ampersands). Exempt: the product name
"Yemen Financial Inclusion Evidence", and **Evidence Record, Evidence Reading and Evidence Passport where they are
named object types in prose**, because this product's citability depends on a reader and a reviewer recognising them
as things with definitions. Arabic has no case; the connector question is English only.

## 3. The final label table

Every label a reader navigates by or relies on. "n/4" is how many of the four judging reviewers supported the decision.

### Global navigation (the five hubs; Master `04_NAV_UX`, "Primary navigation")

| Old EN | Old AR | New EN | New AR | Verdict | Reason |
|---|---|---|---|---|---|
| Explore | استكشف | **Key questions** | **الأسئلة الرئيسية** | CHANGE | The only imperative among five nouns, and the only verb in the Arabic menu; no Arabic institutional menu read uses an imperative. Qualified so it cannot be read as an FAQ: bare "Questions" / «الأسئلة» would collide with 103 governed uses of «الأسئلة» in other senses and sits one word from «الأسئلة الشائعة». 4/4 for a noun. |
| Evidence | الأدلة | — | — | KEEP | The product's core object; exact, nominal, distinct, and the shortest label here. 4/4. |
| Evidence Readings | قراءات الأدلة | **Evidence readings** | — | CHANGE (case only) | The house rule. The rename to "Analysis / التحليلات" is **rejected**: see §4. |
| Data & sources | البيانات والمصادر | **Sources** | **المصادر** | CHANGE | The one truthfulness failure in the navigation: nothing on the page is downloadable (`public_downloads` false); it is a directory of the original sources. Promotion rule in §5, TERM-SOURCES. 4/4, the red team with a condition; against the benchmark, §1 #5. |
| Method & Measurement | المنهج والقياس | **Method and measurement** | — | CHANGE (connector and case) | The house rule; the Arabic pair is already exactly "method and measurement". |
| Methodology | المنهجية | — | — | KEEP | The institutional name, and a label all five readers predict. 4/4. |
| Measurement Agenda | أولويات القياس | **Measurement priorities** | — | CHANGE | "Agenda" implies this resource will carry out the measurement; it only names what is missing. The object type (UI-MA-OPEN), the Arabic label and the search facet already say priorities, so English was the sole outlier. 4/4. |

### Trust navigation (Master `04_NAV_UX`, "Trust navigation")

| Old EN | Old AR | New EN | New AR | Verdict | Reason |
|---|---|---|---|---|---|
| About | عن الموقع | — | — | KEEP | The web convention in English, and in Arabic «عن الموقع» is what Arabic institutional sites use. «عن المورد» is **rejected**: see §4. |
| Corrections | التصحيحات | — | — | KEEP | Names the log of corrections made; distinct from the act of reporting one. |
| Rights & reuse | الحقوق وإعادة الاستخدام | **Rights and reuse** | — | CHANGE (connector) | The house rule. "Reuse" correctly signals the licence rather than legalese. |
| Accessibility | إتاحة الوصول | — | — | KEEP | The expected name; the label claims no conformance. The Arabic editor would prefer «إمكانية الوصول»; **deferred**, §4. |
| Privacy | الخصوصية | — | — | KEEP | Convention; shorter than "Privacy notice" and predicts the same page. |
| Terms | شروط الاستخدام | — | — | KEEP | English needs no complement, Arabic does; a benign non-mirror. |
| Contact | التواصل | — | — | KEEP | Nominal and parallel with its siblings. |

### Footer groups and accessible names

| Old EN | Old AR | New EN | New AR | Verdict | Reason |
|---|---|---|---|---|---|
| Explore and verify | الاستكشاف والتحقق | — | — | KEEP | A footer group names a job, not a page, so it survives the hub rename; two parallel verbal nouns in Arabic. |
| Method & Measurement (group) | المنهج والقياس | **Method and measurement** | — | CHANGE | Mirrors the navigation family by contract; it moves when the hub moves. |
| Trust and responsible use | الثقة والاستخدام المسؤول | **About and policies** | **عن الموقع وسياساته** | CHANGE | "Trust" named four things no reader would say and named none of the seven pages in the group. The responsible-use text is governed page copy on `/rights/` and `/terms/` and is unchanged. 3/4; the red team dissents, §4. |
| Trust links | روابط الثقة | **About and policy links** | **روابط المعلومات والسياسات** | CHANGE | An accessible name must say what it opens; "trust" tells a screen-reader user nothing. 3/4. |
| Product and trust links | روابط المنتج والثقة | **Site and policy links** | **روابط الموقع والسياسات** | CHANGE | Same, and "product" is repository vocabulary a reader never sees. Distinct from the one above. 3/4. |
| Primary navigation | التنقل الرئيسي | — | — | KEEP | The standard landmark name, unique on the page. |
| Menu | القائمة | — | — | KEEP | The shortest unambiguous control name at 390 px. |

### Utilities and page tools

| Old EN | Old AR | New EN | New AR | Verdict | Reason |
|---|---|---|---|---|---|
| Report an issue | أبلغ عن مشكلة | **Report an error** | **أبلغ عن خطأ** | CHANGE (both controls) | The destination's own governed copy says error twice: `/contact/`'s title is "Contact and report an error / التواصل والإبلاغ عن خطأ" and its section heading is "Report a suspected error / أبلغ عن خطأ محتمل". The header control was the outlier. 3/4; the English editor dissents, §4. |
| Cite this page (header) | استشهد بهذه الصفحة | — | — | KEEP | The one citation action label. |
| Cite this page (colophon) | الاستشهاد بهذه الصفحة | — | **استشهد بهذه الصفحة** | CHANGE | One English label had two Arabic strings on the same page. Both are links a reader activates, so the header's imperative is the survivor. |
| Search · Close · Copied · Search status · Search the published evidence | بحث · إغلاق · تم النسخ · حالة البحث · ابحث في الأدلة المنشورة | — | — | KEEP | Exact, distinct and short; one-word controls as a verbal noun and placeholders as an imperative is the Arabic norm. |
| Search questions, evidence, readings and sources**...** | ابحث في الأسئلة والأدلة والقراءات والمصادر**...** | same, **without the trailing dots** | same, **without the trailing dots** | CHANGE (typography) | Three ASCII dots in an RTL placeholder render badly, and GOV.UK uses no ellipsis in placeholders. |
| Evidence colophon | بيان الأدلة | — | — | KEEP | "Colophon" is print-trade jargon and the English editor would change it, but the owner approved this exact label on 9 October (decision B-b, transaction V1B-1). **Deferred**, §4. |

### The eight domain names (the phone menu under the questions hub, and the evidence-landscape table)

| Old EN | Old AR | New EN | New AR | Verdict | Reason |
|---|---|---|---|---|---|
| People | الأفراد | — | — | KEEP | Carries the people ≠ accounts firewall in the label, and «الأفراد» is the institutional Arabic. |
| Access | الوصول | — | **الوصول إلى الخدمات المالية** | CHANGE (AR only) | Bare «الوصول» did three jobs in Arabic — this domain, the chain label, and the accessibility statement «إتاحة الوصول». This exact string is already governed for English "Access" at UI-VIS-CHAIN-ACCESS, so no new string enters the corpus and one divergence leaves it. English unchanged. 3/4; the red team dissents, §4. |
| Payments | المدفوعات | — | — | KEEP | Exact, distinct, short. |
| Remittances | التحويلات | — | **الحوالات** | CHANGE (AR only) | One page had two Arabic names: this label said «التحويلات» while the route surface said «الحوالات». «الحوالات» is the operation sense this corpus already reserves («وكيل حوالات»; «الحوالات المحلية», 216 occurrences) and it never collides with «التحويلات النقدية» (cash transfers, 102 occurrences). **No sweep**: §4 and §5, TERM-REMIT. 4/4. |
| Providers | مقدمو الخدمات | — | **مقدمو الخدمات المالية** | CHANGE (AR only) | Bare «مقدمو الخدمات» is generic; the page is banks, exchange companies, remittance agents and e-wallet services. English unchanged, so no new claim is made in English. 3/4; the red team dissents, §4. |
| Finance | التمويل | — | — | KEEP | The advisor's "Credit and savings" is **rejected**: see §4. |
| Firms | المنشآت | — | — | KEEP | The universe is formal establishments; "Businesses" would over-promise informal firms. |
| Reforms | الإصلاحات | — | — | KEEP | Rule, funding and institution stages; the label claims no outcome, and the page's title states the limit. |

### Route surfaces (Master `04_NAV_UX`, "Route dictionary")

| Old EN | Old AR | New EN | New AR | Verdict | Reason |
|---|---|---|---|---|---|
| Explore | استكشف | **Key questions** | **الأسئلة الرئيسية** | CHANGE | Follows the hub. |
| People & Needs | الناس والاحتياجات | **People and needs** | **الأفراد والاحتياجات** | CHANGE | Connector and case; and one page should carry one Arabic noun — the navigation says «الأفراد». |
| Firms & Finance · Payments & Flows · Access & Infrastructure · Reforms & Programmes · Finance & Institutions | — | **Firms and finance · Payments and flows · Access and infrastructure · Reforms and programmes · Finance and institutions** | — | CHANGE (connector and case) | The house rule. The surfaces keep their extra scope: they serve the sitemap and the route list, not the navigation. |
| Providers | مقدمو الخدمات | — | **مقدمو الخدمات المالية** | CHANGE (AR only) | Parity with the domain label. |
| Remittances | الحوالات | — | — | KEEP | Already correct; the domain label moved to meet it. |
| Compare Evidence | مقارنة الأدلة | **Compare evidence** | — | CHANGE (case) | The house rule. |
| Evidence Readings | قراءات الأدلة | **Evidence readings** | — | CHANGE (case) | The house rule. |
| Reading detail | تفاصيل القراءة | **Reading** | **قراءة** | CHANGE | "Detail" is internal vocabulary; the surface should be the item genre, which the search facet and the breadcrumb family key already use. |
| Measurement Agenda | أولويات القياس | **Measurement priorities** | — | CHANGE | Follows the hub. |
| Data & sources | البيانات والمصادر | **Sources** | **المصادر** | CHANGE | Follows the hub. |
| Evidence record · About · the rest | سجل الدليل · عن الموقع · … | — | — | KEEP | Exact, nominal, distinct; «سجل الدليل» is a closed decision. |

### Object-type names, recurring headings, search facets and the 404

| Old EN | Old AR | New EN | New AR | Verdict | Reason |
|---|---|---|---|---|---|
| Evidence Reading (item eyebrow) | قراءة أدلة | **Reading** | **قراءة** | CHANGE | Removes the Evidence/Evidence stutter where a reader meets it; the facet and the breadcrumb key already say Reading / قراءة. The collection keeps its own name. 3/4. |
| All Evidence Readings · Used in these Evidence Readings · Evidence Readings on this question · Evidence Readings using this source | — | **All Evidence readings · Used in these Evidence readings · Evidence readings on this question · Evidence readings using this source** | — | CHANGE (case) | The house rule, applied to the four recurring headings so the collection is named one way site-wide. |
| Evidence record · Source record · measurement priority · claim / خلاصة · Evidence Passport | سجل الدليل · سجل المصدر · أولوية القياس · خلاصة | — | — | KEEP | Governed and closed. "Claim" → "conclusion" in English prose is **deferred**, §4. The Evidence Passport is internal and never rendered. |
| "These are the priorities the **Measurement Agenda** marks P0. The full **agenda** … on the **Measurement Agenda** page." | the Arabic already says «أولويات القياس» twice | **"… the Measurement priorities page marks P0. The full list … on the Measurement priorities page."** | — | CHANGE | English follows the rename; the Arabic was already right, so this closes an EN/AR divergence rather than opening one. |
| "… the original documents are linked from **Data & sources**." | «… من صفحة **البيانات والمصادر**» | **"… linked from Sources."** | **«… من صفحة المصادر»** | CHANGE | Follows the rename, in both languages. |
| Evidence Readings: {{n}} · Measurement Agenda priorities: {{n}} (the `/data/` coverage list) | the Arabic already says «قراءات الأدلة» and «أولويات القياس» | **Evidence readings: {{n}} · Measurement priorities: {{n}}** | — | CHANGE | Follows the renames; no count moves. |
| Used on | مستخدم في | **Where it is used** | **مجال الاستخدام** | CHANGE | A cryptic fragment among three nominal sibling facets (Document type, Publisher, Year of the document). 3/4. |
| Document type · Publisher · Year of the document · Any · Not recorded · Clear filters · Order · As grouped · Newest document first · Find a source by title or reference · e.g. SRC-CBY… | — | — | — | KEEP | Exact and parallel; "Not recorded" correctly holds missing ≠ zero. Four English refinements are **deferred**, §4. |
| Explore (404) | استكشف | **Key questions** | **الأسئلة الرئيسية** | CHANGE | Must follow the hub, or the 404 offers a destination the header no longer has. |
| Page not found · We could not find this page · Home · Evidence · Search (Arabic and English) · the no-results sentence | — | — | — | KEEP | Plain, non-blaming, and the no-results sentence is a model empty state: it corrects the missing ≠ zero inference and offers the next move. |
| Understand → Explore → Verify · Explore questions | افهم ← استكشف ← تحقّق · استكشف الأسئلة | — | — | KEEP | These are the verb "explore", not the hub's name. Renaming the hub frees the verb rather than retiring it. |

### Page titles — prefix parity (`02_SITE_MAP`)

The `<title>` is the h1 plus " — Yemen Financial Inclusion Evidence". The split of the two is **escalated, not done**
(§4). Its cheap half is taken here: every domain title now identifies its domain in its first two words, in both
languages, and none ends in a full stop.

| Route | Old | New | Verdict |
|---|---|---|---|
| /access/ (AR) | «نعرف أجزاءً من شبكة الوصول إلى الخدمات المالية، لكننا لا نملك بعد خريطة وطنية موثوقة لما يعمل فعليًا على الأرض.» | «الوصول إلى الخدمات المالية: نعرف أجزاءً من الشبكة، لكننا لا نملك بعد خريطة وطنية موثوقة لما يعمل فعليًا على الأرض» | CHANGE — the prefix is added and the phrase it repeats is said once; both propositions and the limit are unchanged |
| /providers/ (AR) | «قائمة مقدمي الخدمات تثبت وضعًا رسميًا في تاريخ محدد، لكنها لا تثبت التشغيل بذاتها.» | «مقدمو الخدمات المالية: القائمة الرسمية تثبت وضعًا رسميًا في تاريخ محدد، لكنها لا تثبت التشغيل بذاتها» | CHANGE — the prefix is added; «لا تثبت» and the dated-status limit are kept exactly |
| /reforms/ (EN) | "A reform can be real before its outcome is known." | "Reforms: a reform can be real before its outcome is known" | CHANGE — the only English domain title with no prefix |
| /reforms/ (AR) | «قد يقع الإصلاح فعلًا وتبقى نتيجته مجهولة.» | «الإصلاحات: قد يقع الإصلاح فعلًا وتبقى نتيجته مجهولة» | CHANGE — the same gap in Arabic |
| /readings/ (EN) | "Evidence Readings" | "Evidence readings" | CHANGE — the house rule; this title is the hub's h1 |
| /people/ · /payments/ · /remittances/ · /finance/ · /firms/ | — | — | KEEP — the prefix is already present and the title carries no terminal full stop |

Every other `<title>` and meta description is unchanged. **No number, period, universe, limit or source moves
anywhere in this transaction.**

## 4. What was rejected, and why

### The advisor's hypothesis 2 — "Evidence Readings" → "Analysis / التحليلات": REJECTED

Three collisions, two of them in the repository's own bytes.

1. **"Analysis" / «التحليل» is already a rendered section role on 31 page sections**, across `/`, `/access/`,
   `/finance/`, `/remittances/` and others, and a section role is drawn as a visible eyebrow. A hub and an in-page
   eyebrow would carry one name for two different objects.
2. **«التحليلات» already means analytics on this site**: the `/privacy/` heading is
   «التحليلات وملفات الارتباط والتتبع من طرف ثالث».
3. In Gulf and Levant Arabic «تحليلات» reads first as medical tests.

Beyond the collisions: "Analysis" promises interpretation beyond the evidence, which this resource refuses (no
composite scores, no rankings, no averaging of disagreement), and it invites a reader to attribute a source's figure
to CauseWay — the journalist persona's likeliest failure. The benchmark found no institution naming this layer
"Analysis" in a menu, and found that naming a section after its item genre is ordinary practice (BIS "Speeches",
CGAP and ONS "Blog"), so "Readings" is a defensible name rather than a mistake. It is also the most expensive rename
on the list: a breadcrumb parent, five recurring headings, a `<title>` and two social images.

The English defect the advisor names is real — "Evidence" repeats the next hub and the product name, and in English
"readings" also means instrument output on a measurement site. It is answered where a reader actually meets it: the
item's eyebrow becomes "Reading / قراءة" (§3), and the collection takes sentence case.

### The advisor's hypothesis 8 (English) — "Finance" → "Credit and savings": REJECTED

The page is not credit and savings. It carries bank balance-sheet figures including a valuation-driven break,
external-support stages that must not be summed, financial-soundness limits, and the 24-event dated chronology of the
financial system. The label would hide all four, and the chronology is one of the product's strongest assets. The
benchmark found that **no institution read uses "Credit" or "Savings" as a topic label** (World Bank "Financial
Services Sector" / «الخدمات المالية»; CGAP "Financial Inclusion"; IMF "Digital Payments and Finance"), and
«الادخار» carries a deposit-product connotation on a page with no deposit-protection evidence. The weakness the
advisor names — on a financial-inclusion site everything is finance — is real, and is answered by the page's own
title, "Finance: borrower, saver and balance figures measure different things". The Arabic editor supported
«الائتمان والادخار»; the red team, the IA lead and the benchmark did not, and the lead sided with them.

### The advisor's hypothesis 9 — a governed sweep of «التحويلات» → «الحوالات»: REJECTED as a sweep

The two forms are not drift. **This corpus already works the distinction deliberately**: page_sections.json carries
«سلسلة التحويلات الكلية لا تقيس حجم الحوالة غير الرسمية» — the published series in one word, the individual
remittance in the other, correctly, in one sentence. Protected collocations in governed content, measured:
«التحويلات النقدية» 102 (cash transfers), «الحوالات المحلية» 216, «تحويل أموال» 91, «التحويلات الواردة» 75 (a
balance-of-payments series), «تحويلات العاملين» 67, «التحويلات الحكومية» 29, «التحويلات الشخصية» 13 (a BPM6 concept
name). One live heading reads «… الأجور والتحويلات الحكومية والمدفوعات الزراعية والحوالات المحلية …»; a mechanical
replacement would make it nonsense and change a claim. A changed concept name is a changed universe, which the brief
forbids. The benchmark also found «الحوالات» on none of the four Arabic institutions, which is a reason to govern it
narrowly rather than adopt it as the generic term.

What is done instead: the one genuine defect — the same page named two ways in Arabic — is fixed (§3), and the two
senses are governed separately in the register (§5, TERM-REMIT and TERM-CASH-TRANSFER), with the do-not-replace
contexts written out so no later editor can flatten them. **No occurrence of «التحويلات» in body prose was changed.**

### The advisor's hypothesis 6 (Arabic) — "About / عن الموقع" → «عن المورد»: REJECTED

Unvocalised «المورد» reads as *muwarrid*, "supplier", which on a financial site is a live misreading, and no Arabic
institutional site read uses «عن المورد» (the World Bank's Arabic Data site uses «نبذة عن»; IMF Arabic uses «عن
الصندوق»). The prose «هذا المورد» is a different grammatical job: a demonstrative inside a sentence has context, a
two-word menu label has none. It also sits with the executed Arabic-ledger decision D3, which names «هذا الموقع» as
the agentive self-reference. The footer group's change (§3) delivers what the hypothesis was reaching for.

### The advisor's hypothesis 10 — `<title>` uses the stable name, the thesis stays the h1: ESCALATED, not done

The diagnosis is right, and the benchmark confirms it: every institution's topic-page `<title>` is a stable name plus
the site name, never a thesis. A browser tab shows roughly thirty characters, so eight open domain tabs read as eight
near-identical truncations; search engines truncate near sixty and rewrite titles they judge unhelpful; and a shared
card turns the thesis into the headline, so "reported POS terminals rose between March 2025 and June 2026" circulates
stripped of its scope and goes stale on the next Central Bank report.

It cannot be done inside this brief's constraints. `page["title"]` is **one** governed field feeding `<title>`,
`og:title`, `twitter:title`, the BreadcrumbList and Article structured data, the print foot and the social frame.
Splitting it needs a second governed field in the Master **and** in the page-spec projection, read in four code paths
(`render.py head`, `discovery.py social_meta`, the breadcrumb structured data, `frames.py`), 284 regenerated images
and a schema change — none of which is "language only". A breadcrumb for the eight domain pages would be a new
navigation element: `breadcrumbs` covers only Evidence Record and Reading today. **Escalated** (`design/ESCALATIONS.md`)
for the edition that also turns downloads on, so the renderer change, the schema change and the image regeneration are
paid for once. Its cheap half — prefix parity — is taken now (§3), which buys most of the clarity for a fraction of
the disruption.

### Dissents recorded against decisions that were taken

- **The red team judges three of the adopted changes fatal.** «مقدمو الخدمات المالية» (it says naming them financial
  service providers upgrades a dated roster into a regulatory category, and a citizen may take a listing for an
  operating firm); «الوصول إلى الخدمات المالية» (it says a longer form asserts a completed relation between a person
  and a service, breaching access ≠ use); and "About and policies" (it says "policies" names instruments the site does
  not have, and that dropping "responsible use" deletes a warning). The lead overruled all three: the English labels
  are unchanged so no new claim is made in English; the Arabic strings are ones the Master already governs or that name
  a subject rather than a status; the pages' own governed text continues to state that a listing or a licence does not
  establish operation and that the access map is incomplete; and the responsible-use text is page copy on `/rights/`
  and `/terms/`, not a footer label. **The owner may reverse any of the three on the red team's reasoning alone.**
- **The English editor would keep "Report an issue"**, on the ground that the destination accepts corrections, broken
  links, rights, accessibility, privacy and technical faults, so "error" under-promises it. Overruled on the
  destination's own governed wording, which says error twice.
- **The Arabic editor would change «إتاحة الوصول» to «إمكانية الوصول»** for Accessibility, the settled Arabic term
  (11 governed uses elsewhere). Deferred: «إتاحة الوصول» has 47 governed uses, and keeping it distinct is what stops
  bare «الوصول» doing three jobs. One for a native certifier.

### Deferred, with the reason

- "Evidence colophon" → "About this page". The owner approved this exact label on 9 October (decision B-b); not the
  steward's to re-decide a day later.
- English "claim" → "conclusion" in prose. The governed Arabic «خلاصة» is a closed decision and the English does drift
  from it, but this is a prose change across many strings, not a label.
- Four `/data/` facet refinements: "Order" → "Sort by", "Year of the document" → "Document year", "As grouped" →
  "Default grouping", "Search the published evidence" → "Search this resource". Sound, English-only, outside the
  naming question.
- Collapsing the route surfaces to the single domain names. The surfaces carry scope the sitemap and route list use;
  only the contradictions were fixed and the connectors normalised.
- The eight domain answers in the desktop navigation, and a breadcrumb for the eight domain pages. Both are new
  navigation elements, which the brief excludes.

## 5. The governed terminology register

Added to the Master as a new declared block of `04_NAV_UX`, "Governed terminology register / سجل المصطلحات الخاضعة
للحوكمة", with the columns the brief asks for: `term_id | term_en | term_ar | definition_en | definition_ar |
do_not_use | rule`. Eleven terms: TERM-REMIT, TERM-CASH-TRANSFER, TERM-LICENCE-REUSE, TERM-LICENSING, TERM-SOURCES,
TERM-QUESTIONS, TERM-MEASUREMENT-PRIORITY, TERM-EVIDENCE-READING, TERM-RESOURCE-SELF, TERM-ACCESS, TERM-PROVIDERS.

It is in `04_NAV_UX` because that sheet already governs every public label, the trust navigation and the search
aliases, so a term, the label that carries it and the alias that rescues its retired form sit on one sheet and move in
one transaction. It is declared in `scripts/projection/master_structure.json`, so the generator fails if it is removed
or renamed. It is mirrored into `audit/ARABIC_TERMINOLOGY_AND_STYLE_LEDGER.md` §6, which is where an Arabic editor
looks first.

The two rules the brief asks for, as the register states them:

- **Remittances = «الحوالات»** for the operation — the flow, the corridor, the channel, the method, the cost, the
  agent. **«التحويلات»** stays for a published balance-of-payments or national-accounts series, aggregate, revision,
  vintage or scope, and «التحويلات الشخصية» only where the source's caption says personal transfers. Never
  substituted: «التحويلات النقدية», «التحويلات الحكومية», «التحويلات الواردة», «الحوالات النقدية الداخلية»,
  «تحويل مصرفي», and any quoted source title or a source's own term. **Cash transfers = «التحويلات النقدية»**, never
  «الحوالات» and never called remittances in English: the payer is a programme, not a person.
- **Copyright licence = «رخصة»; regulatory licensing = «ترخيص».** The public copy was already right — `/rights/`
  uses «رخصة المشاع الإبداعي» and «الرخصة» for the reuse instrument, and every «مرخص / مرخصة / الترخيص» in the
  interface copy and the visual contracts is regulatory. The register fixes it so it cannot drift. CauseWay is not a
  licensed financial institution and claims no such status (`audit/OWNER_DECISIONS_2026-10-10.md`).

### Counts

| Rule | Occurrences changed | Occurrences deliberately left | Measured where |
|---|---|---|---|
| remittances = «الحوالات» | 1 label (UI-LAND-DOM-REMITTANCES) and 1 title prefix | «التحويلات» 1,451 in governed content, of which 102 «التحويلات النقدية», 75 «التحويلات الواردة», 67 «تحويلات العاملين», 29 «التحويلات الحكومية», 13 «التحويلات الشخصية» — **none changed** | `site-src/content/` |
| cash transfers = «التحويلات النقدية» | 0 (already correct) | 102 | `site-src/content/` |
| licence = «رخصة» / licensing = «ترخيص» | 0 (already correct) | 5 reuse-sense uses on `/rights/` and `/terms/`; every regulatory use in the interface copy and the visual contracts | `site-src/content/` |
| «مقدمو الخدمات» → «مقدمو الخدمات المالية» | 2 (the domain label and the route surface) | the compound «مقدمو خدمات الدفع» (payment service providers), which is a different category | `site-src/content/` |
| «الوصول» → «الوصول إلى الخدمات المالية» | 1 (the domain label) | «إتاحة الوصول» 47 (this resource's accessibility statement); «الوصول» inside prose | `site-src/content/` |

## 6. Rights presentation

See `audit/public_naming/RIGHTS_PRESENTATION.md`.

## 6a. Propagation — one decision, applied everywhere

Never a menu-only rename. Every accepted change reached, in the same change set:

| Surface | How |
|---|---|
| The Master | `04_NAV_UX` primary navigation (label_en, label_ar and the `route_or_group` JSON of each row), the route dictionary, the trust navigation, the governed interface copy, the search aliases and the new register block; `02_SITE_MAP` titles; `03_PAGE_SECTIONS` the `/data/` coverage list |
| Regenerated projections | All 39 outputs, by `scripts/generate_projections.py`; `PROJECTION CHECK PASS` proves the Master regenerates every byte |
| `navigation_interaction.json` | `global_navigation`, `trust_navigation`, the footer group links and the breadcrumb parent labels are regenerated from the Master by the generator's own alignment; the hand-governed parts were edited in place under the steward designation — the `report_issue` utility labels, the `trust_use` footer group label, and five new search smoke tests |
| Search facets and aliases | The `/data/` facet `Used on` → `Where it is used`; five new aliases (034–038) carrying every retired word, English and Arabic; gate PN-G02 fails if a retired word loses its alias |
| Page `<title>` and meta | The five titles of §3; every `<title>` is `h1 — product`, so the four prefix changes and the `/readings/` case change reach the tab, the Open Graph title, the Twitter title, the breadcrumb and Article structured data and the print foot in one move. No meta description changed |
| Social images | Regenerated: 284 PNG, 1200 × 630, one per route and language; `social_images.py --check` reports CURRENT |
| Sitemap and route list | `site_map.json` is a projection and follows the Master; no route or URL changed, so the sitemap's addresses are untouched |
| README, the checkpoint, the Context and the handoff manifest | The Master and Page Spec hashes were rebound by `scripts/rebind_authority.py`; `README.md`'s "Public path" paragraph was rewritten to the new labels by hand |
| The handoff package | `handoff/CLAUDE_DESIGN_MASTER_PROMPT.md` §4.2's verbatim label list, and its other eight uses of a retired label, now read the new names and tell the recipient to read the contract rather than the paragraph if the two ever differ |
| `design/` records | `00_DESIGN_README.md`, `01_FOUNDATIONS.md` and `10_ACCEPTANCE_CHECKLIST.md`; `design/ESCALATIONS.md` closes the label half of C-10 ("'Data & sources' holds no data") with a dated line and raises the four new escalations |
| The Arabic ledger | `audit/ARABIC_TERMINOLOGY_AND_STYLE_LEDGER.md` §9 mirrors the register, records the remittance gap §6 had left open, lists every retired string with the alias that rescues it, and corrects three stale §6 rows without rewriting them |
| History | `docs/CHANGELOG.md`, `audit/INDEX.md`. Nothing in `docs/CHANGELOG.md`, `audit/**` or the dated dispositions inside `design/ESCALATIONS.md` was rewritten |

## 6b. Gates and verification

| Gate | Result |
|---|---|
| `checksums.py --check` | CHECKSUM MANIFEST CURRENT |
| `generate_projections.py --check` | PROJECTION CHECK PASS (39 outputs, 0 differences) |
| `unittest discover scripts/projection/tests` | Ran 22 tests — OK |
| `build.py` + `audit_public_literals.py` | 288 HTML from 142 page specs; records 14563 unresolved 0 |
| `validate.py` | HTML=288 ERRORS=0 WARN=0 — WEBSITE REPOSITORY VALIDATION PASS, including the two new gates |
| `repository_manifest.py --check` | REPOSITORY MANIFEST CURRENT |
| `bilingual_invariance.py` | **0 page pairs with differing numbers** (143 pairs) — the brief's bilingual numeric invariance at 0 |
| `test_content_parity.py` | PASS, 286 documents, 0 differing |
| `test_literal_audit_determinism.py` | PASS, 8 hash seeds, one SHA-256 |
| `source_lineage_truth_test.py` | PASS 8/8 |
| `architecture_diagrams.py --check` · `social_images.py --check` · `logo_derivatives.py --check` | CURRENT · CURRENT (284) · CURRENT (8) |
| `test_public_tools.py` (browser) | PASS 35/36, 1 not applicable to the current data |
| `viewport_acceptance.py` (browser) | 168/168 page-width checks pass |
| `test_security_headers.py` (browser) | PASS, 288 pages, 0 problems |
| `test_base_path.py` (browser) | PASS, 60 page loads at 390 and 1440 px in both languages, 644 requests, 0 problems; its own negative controls caught |
| `test_no_javascript.py` (browser) | PASS, 0 problems |
| `test_gate_negative_controls.py` | Every control caught its fault, including the eight new ones |

**Preservation.** Every one of the 288 built documents was compared, element by element, against pull request #16's
head: **no `id`, no link target and no `data-*` hook was lost on any page, and no document was deleted.** The visible
text of 287 documents changed, in 68 distinct ways, and every one of them is a label, a governed term, one of the four
title prefixes, one of the three terminal full stops, the new footer licence line, the restated `/rights/` section, or
the colophon's Master fingerprint — which moves with any Master transaction. The complete list is the change set of
§3; the largest are «البيانات والمصادر» → «المصادر» (526 occurrences), "Explore" → "Key questions" and «استكشف» →
«الأسئلة الرئيسية» (293 each), "&" → "and" (292), "issue" → "error" and «مشكلة» → «خطأ» (285 each), «التحويلات» →
«الحوالات» (151, all of them the domain label and the title prefix).

**Negative controls, new.** Eight, all caught: three for PN-G02 (a retired label reappearing on a page; the alias that
rescues a retired word removed; a new alias losing its smoke test) and five for PN-G01 (§6 of
`RIGHTS_PRESENTATION.md`). **No existing gate's logic was changed and no existing fault string was touched**, so every
control that passed before still proves the same thing.

**Not claimed.** No WCAG conformance, no legal review, no rights clearance, no native-language certification and no
security guarantee. The Arabic carries the ledger's standing status, `EXTERNAL_HUMAN_CERTIFICATION_NOT_PERFORMED`.

## 7. Transaction PN-1

Script `pn_1_public_naming.py`; ledger `runs/PN-1_MASTER_LEDGER.json`; run report `runs/PN-1_RUN_REPORT.json`.
79 cells written across `04_NAV_UX` (primary navigation, the route dictionary, the trust navigation, the governed
interface copy, the search aliases, the new register block), `02_SITE_MAP` (five titles) and `03_PAGE_SECTIONS` (the
`/data/` coverage list, English row only — the Arabic row already said «قراءات الأدلة» and «أولويات القياس»).
No figure, unit, period, universe, source, record or count is touched.

Hand-governed contract, edited in place under the steward designation, in the commit that names the finding it closes
(`site-src/content/content/navigation_interaction.json`): the `report_issue` utility labels; the `trust_use` footer
group label; and five search smoke tests, one per new alias, so every retired word is proved to still find its page.
`presentation_priority.json` is not in scope and is not touched.
