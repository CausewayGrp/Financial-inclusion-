# Evidence Readings — final portfolio adjudication (Session F1)

**Date:** 26 September 2026 · **Decision owner:** Team Lead (Product Lead / Evidence Integrator) · **State:** FROZEN

**Inputs:** the V3 ten-Reading editorial candidate supplied as Appendix A of the OpenAI final-integration prompt (26 September 2026), and the post-Tranche-C Production Master (`f0150122…7224`): 08 Reading headers, 03 Reading sections, 09 section index, 11 Reading visuals, and every Evidence Record the Readings bind (06/07).

**Outputs:** one disposition per Reading (below); the change ledger `audit/READING_PORTFOLIO_CHANGE_LEDGER.csv` (every material departure from Appendix A); the transaction input `audit/reading_integration/rp_final_texts.py`, applied Master-first by transaction RP-F2 (`audit/reading_integration/rp_integration.py`). After RP-F2 the Master is the only Reading truth. The transaction input is lineage; nothing reads it except the transaction.

## 1. Rule applied

The winning text is the one that is most truthful, most precise, hardest to misuse, most natural in its language, most useful to its reader and best supported by governed evidence. A candidate line was kept unless a verified source, the Master, EN/AR parity, detached-use safety or a demonstrable editorial defect required a change. Every figure in the final texts was matched, on token boundaries, to the governed text of a record the Reading binds (the public-literal audit enforces this: 12,741 records, 0 unresolved).

## 2. Portfolio decision

| Reading | Territory | Disposition | Title (EN / AR) |
|---|---|---|---|
| CWR-001 | vintage | MERGE NARROWLY | Same year, different number / العام نفسه، رقم مختلف |
| CWR-002 | baseline / method break | ADOPT CANDIDATE | When the baseline moves / حين يتحرك خط الأساس |
| CWR-003 | unit / universe / denominator | MERGE NARROWLY | When the unit changes, the story changes / حين تتغير وحدة القياس، تتغير القصة |
| CWR-004 | evidence clocks / currentness | MERGE NARROWLY · **FEATURED** | The system is changing. What has reached people? / المنظومة المالية تتغير. فما الذي وصل إلى الناس؟ |
| CWR-005 | durable digital use | MERGE NARROWLY | When does digital growth become durable use? / متى يتحول النمو الرقمي إلى استخدام مستمر؟ |
| CWR-006 | dimensions of microfinance growth | MERGE NARROWLY (title replaced) | What exactly do we mean by microfinance growth? / ماذا نعني تحديدًا بنمو التمويل الأصغر؟ |
| CWR-007 | measured disparity vs mechanism | MERGE NARROWLY | The gender gap is measured. Its explanation is still open. / الفجوة بين النساء والرجال مقاسة. أما تفسيرها فما يزال مفتوحًا. |
| CWR-008 | question + denominator | MERGE NARROWLY | How can 22% and 91.84% both be right? / كيف تكون 22% و91.84% صحيحتين معًا؟ |
| CWR-009 | transmission / proof | ADOPT CANDIDATE | When does a payment reform become financial inclusion? / متى يصبح إصلاح المدفوعات تحسنًا في الشمول المالي؟ |
| CWR-010 | persistence after a transfer trigger | MERGE NARROWLY | The payment arrived. What happened next? / وصلت الدفعة. ماذا حدث بعدها؟ |

No Reading is KEEP CURRENT: every Tranche C body used the same nine-box schema ("What supports this reading", "What qualifies…", … "Trace the reading back to evidence"), which the editorial direction retires. No Reading is SOURCE HOLD: every figure the final texts print is governed; the one figure that is not (the ~50% firm-finance narrative) stays out of the essay (§4.2).

**Featured Reading: CWR-004.** It carries the product's system view (rules, institutions and infrastructure moving faster than evidence about people) and its currentness discipline ("latest evidence of what?"), so it is the most useful first Reading on Home, Explore and the Readings index.

## 3. Preflight findings (OpenAI §5A) — each resolved once

| Finding | Resolution |
|---|---|
| Portfolio provenance: CWR-006 completed and CWR-010 authored in V3 | Accepted as V3 authorship; both were verified line by line against CLM-054–058 and CLM-045 like the other eight. Nothing in this record presents them as recovered historical drafts. |
| CWR-001 repeated `2024` | The Arabic opening now names 2024 as often as the English (four times); both editions print the same numbers. |
| CWR-003 `11.9%`, `561 → 1,473`, `1,000`, five-question list | Arabic carries all three figures with their period and scope; the five questions are a bulleted list in both editions (no numbered list); CLM-001, CLM-003 and XW-FMIIP-005 are now bound to CWR-003. |
| CWR-004 `23%` boundary and extra 2026 reference | Both editions carry the 23% exclusion, the fieldwork dates and the same three 2026 references (institution-building, POS count, not a 2026 estimate). |
| CWR-005 "not a 2026 estimate" | Stated in both editions. |
| CWR-007 poorest 40% / richest 60% and numbered list | The income gap is printed with both group values (6.5%, 15.5%) and "about 9.0 percentage points" in both editions; the four-part design list became one sentence; 12.91 appears twice in each edition. |
| CWR-008 repeated 22%/91.84%, 328/31/18, working-capital mix, three-question list | Both editions carry the same payload: 22% four times, 91.84% four times, 328/31/18, the full six-part working-capital mix, SMEPS 19%/15%/40%. The three-question list became prose. |
| CWR-006 title burden of proof | **Replaced** (§4.1). |
| CWR-008 Arabic compression | Rewritten: «أفادت 22% من المنشآت بأن الوصول إلى التمويل كان من بين التحديات التي تواجه أعمالها». |
| CWR-010 Arabic calques | Removed: «التعرض للخدمة المالية» → «إتاحة حساب قابل للاستخدام»; «تعريض المستفيدين لحسابات» → «إتاحة حسابات قابلة للاستخدام للمستفيدين»; «نقطة نهائية سلبية» → «متلقيًا سلبيًا لدفعة برنامجية». |
| Method/comparator binding ("Global G2P practice…") | Rewritten so the Reading does not rest on an unbound external authority: the sentence now states the design features on which account use depends, as reasoning, not as a cited practice. CWR-007's "International literature provides hypotheses" became "For Yemen these are hypotheses to test, not findings". No Reading now invokes an unbound comparator. |
| CWR-007 "rose between observed waves" | **Removed** from the standfirst. A 2014 women's value (1.7%) exists only in the Master analytical table 26 (FHOBS-2014-002); no public Evidence Record carries it and the Reading's argument does not need it. Creating a new public claim to keep one clause fails the deletion test. |

## 4. Mandatory source adjudications

### 4.1 CWR-006 — microfinance

Verified against CLM-054 (93,118 end-2015 and 88,445 end-2020 verified primary borrowers; 78,686 end-2023 from a 2024 policy paper citing SFD data, provider set unverified; 1.611 million savers/depositors 2020 vs 3.3 million "active savers" 2023; YER 33.379 billion vs about YER 44 billion nominal), CLM-055 (12 of 26 listed banks classified as microfinance banks by name, list checked 7 September 2026), CLM-056 (91% = share of saver *growth*, not of the 2023 stock), CLM-057 (June/end-2023 points not one series) and CLM-058 (borrower base broadly 80,000–90,000 through 2021 while average loans rose).

- **Title.** "Microfinance is growing" fails the detached-quotation test: every verified borrower observation after 2015 is lower, and the only upward readings are nominal (portfolio) or rest on an unharmonised definition (savers). Adopted: *What exactly do we mean by microfinance growth? / ماذا نعني تحديدًا بنمو التمويل الأصغر؟*
- **Savers.** The 3.3 million figure is printed only as the source's own label ("what it calls 'active savers'"), explicitly *not* unique people and *not* a national savings rate.
- **Institutions.** "The institutional landscape has also changed" asserted an unmeasured change; replaced with the dated CLM-055 listing and its boundary.
- **Nominal portfolio.** The CBY-Aden exchange rates in CLM-054 were considered and left out: quoting one area's market rate beside rial figures of unrecorded valuation invites exactly the deflation the record says cannot be done.
- Central point kept: borrowers, savers/depositors, nominal portfolio and institutional form can move differently.

### 4.2 CWR-008 — firms

From the source tabulations held in CLM-005, CLM-006, CLM-062, VIS-FIRM-CONSTRAINTS, VIS-FIRM-FINANCE-PATH and VIS-FIRM-FINANCE-SEVERITY (World Bank custom enterprise survey, September 2022, seven governorates, in *Yemen Financial Sector Diagnostics* 2024, Annex III):

| Point | Adjudication |
|---|---|
| 22% | Share of surveyed formal firms naming access to finance among business challenges (Figure 108 / Table 8, p. 146); multiple response; the number answering and the exact question wording are not held; it is the survey's own item, **not** the standard Enterprise Survey "biggest obstacle" indicator. The 328 firms are **not** asserted as its base. |
| ~50% narrative | Not in any governed record; its base (possibly all firms, including those needing no loan) is not established. Kept out of the essay: omitting it does not weaken the Reading. |
| 68.71% + 23.13% = 91.84% | Figure 107, p. 145: filtered tabulation that excludes firms that said they did not need a loan; the number of firms in it is not held; 91.84% is a sum computed by this resource. |
| Filter / weighting | The filter is stated. Weighting is not documented in the evidence base, so the Reading makes no weighting claim. |
| 328 → 31 → 18 | The candidate's "evidence path narrows quickly … only 18 valid responses remained" implied the 18 come from the 31; VIS-FIRM-FINANCE-PATH says this is not established. The final text states it. |
| Working capital | The full six-part mix (69.12 / 16.66 / 10.15 / 1.97 / 1.31 / 0.56) is printed in both editions, as average shares, not shares of firms. |

The denominator is part of the result: both editions say so, and the Reading's question (08) now names the 2022 seven-governorate frame (BIL-05 item 2).

### 4.3 CWR-009 — payments reform

Rebound to CLM-003 (POS 561 → 1,473 within CBY-Aden's reporting scope), CLM-004 (accounts and transactions are not people) and CLM-018 (institution-building June–August 2026; YPCC established, not a system in operation; FMIIP results framework: FPS and RTGS not yet operational in January 2025, no later state recorded). The proof chain is kept exactly: **rule or funding → implementation or institution → operation → reachable access → actual use → quality and protection → outcome** (Arabic uses the right-to-left arrow «←»). No rule, institution, rail, terminal count or transaction becomes a population outcome, and missing downstream evidence is not called failure. "Conflict" was removed as a blanket explanation; the Yemen-specific reason is fragmented authority, infrastructure constraints and different reporting universes.

### 4.4 CWR-010 — post-transfer persistence

CLM-045 establishes: World Bank/G2Px material (May 2024) describes a digital-payment pilot within the unconditional cash-transfer programme in **eight districts**, **reported by programme partners** to have benefited **45,460 recipients** (reference period not recorded), with an emphasis on payment into **fully functional accounts** and **recipient choice**. Delivery and exposure to a formal service are supported; **persistent post-transfer use is not observed**. The final text says "reported by programme partners", states that 45,460 counts recipients and not continuing users, keeps "cash-out is not automatic failure", and renders the 30/90/180/365-day windows in words (a month, three months, six months and a year) so no unbound figure is printed.

## 5. Portfolio discipline

- **Ten territories, ten disciplines** (vintage; method break; unit/universe/denominator; evidence clocks; durable use; dimensions of growth; disparity vs mechanism; question + denominator; transmission; persistence) — kept distinct; no two Readings share a conclusion.
- **One family:** Evidence Readings / قراءات الأدلة. No second analytical taxonomy; no "In plain terms" component was needed.
- **Structure without template:** 4 to 7 body sections per Reading, headings written for each argument; the opening section may run on from the standfirst without a heading. The only shared element is the ending — *What would change this reading? / ما الذي قد يغيّر هذه القراءة؟* — followed on the page by *Trace the evidence / تتبّع الأدلة* and one or two related Readings.
- **One signature visual:** 08 visual_bindings now lists only the Reading's RV-CWR contract (the only visuals routed to Reading pages in 11); it sits after the opening.
- **Relations (new 08 fields):** related_readings (1–2), measurement_bindings (the Measurement Agenda priority each Reading examines), domain placement (at most two Readings per answer page), evidence_period (EN/AR), last_reviewed (26 September 2026), featured (exactly one).

## 6. Editorial acceptance (one cold read, one repair pass)

**English.** Staccato one-line paragraphs merged; repeated "That difference matters / This distinction matters" and the identical "What this evidence does not tell us" caveat block not repeated across Readings; em dashes 4 in ~6,200 words; "not X, but Y" twice; no consultancy filler or generic transitions; every numeric sentence carries its unit, universe and period (POS counts always "reported by the Central Bank of Yemen – Aden … within its reporting scope"; Findex values always "adults aged 15 and over in the areas surveyed"). "Controlled" (internal vocabulary) removed from public sentences.

**Arabic, read as Arabic.** Authored to the same section structure, not translated line by line. Register decisions: «قاعدة الاحتساب» for denominator (the house gate rejects «المقام» in public copy); no "clock" metaphor (the house gate rejects «ساعات الدليل»; replaced by «توقيت القياس» and «الإيقاع»); «مستمر» for durable use (not «مستدام», which reads as sustainability); «التحويلات» for remittances, consistent with the Evidence Records; Arabic numerals in figures (80,000–90,000, not «80 ألفًا»); Latin script only for proper names that have no settled Arabic form in the evidence base (Findex, G2Px, CauseWay).

**Parity.** Field-level and page-level: every English/Arabic page pair on the site now prints the same numbers (bilingual invariance: **0** differing pairs, down from the 6 held under BIL-05).

## 7. Integration plan executed in F2 (one transaction, RP-F2)

| Owner | Change |
|---|---|
| 08_READINGS | titles, questions (CWR-001, 002, 004, 008, 010), standfirsts, prohibited inferences (CWR-002, 005, 006, 010), bindings (CWR-003, 004, 007, 008 extended/trimmed to what the text uses), visual bindings (signature only), domain placement; `domain_context_routes` retired → `related_readings`; new `measurement_bindings`, `evidence_period_en/ar`, `last_reviewed`, `featured` |
| 03_PAGE_SECTIONS | ten Reading bodies (sections 2..n); surplus rows deleted, including the retired generic "Trace the reading back to evidence" section; /readings/ definition (verbatim from the programme owner) |
| 09_READING_SECTIONS | index follows each Reading's section count; semantic section ids (opening, evidence_*, interpretation_*, why_it_matters, boundary, use, what_would_change) |
| 02_SITE_MAP | /readings/ title: Evidence Readings / قراءات الأدلة |
| 11_VISUAL_LIBRARY | RV-CWR-001 and RV-CWR-002 Arabic as specific as English (2024; 2022 positions) — BIL-05 item 3; RV-CWR-005/010 «مستمر» |
| 04_NAV_UX | twelve governed interface labels for the Reading family, the Explore pointer, Evidence "Used in" and Measurement "examined in" |

F1 is frozen. Re-open only on a verified source conflict, a gate regression or an explicit scope change.
