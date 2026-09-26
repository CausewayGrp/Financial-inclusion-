# P16 — Held Tranche-B additions: evidence analysis and dispositions (READ-ONLY)

Specialist roles: B (Evidence, survey & measurement), C (Firms), D (Payments/providers/access), with E (FCV) and H (Arabic) checks.
Status: analysis only. No repository file was modified. Every material decision belongs to the Team Lead.

**Authority state read:** Master `authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx` sha256 `4403a353…c6dbd`; `site-src/content/page_specs.json` sha256 `776558e4…20635`. Both match `audit/PUBLIC_LITERAL_CLOSURE.json`. The brief's entry hashes (`e698…`, `ff2b…`) are superseded, as S00 recorded.

**Method:**
1. Master rows were read with `scripts/projection/master_reader.Workbook`. Excel row numbers are given as `r<n>`.
2. Projections were cross-read.
3. Each proposed text was run through the shipped classifier `scripts/audit_public_literals.classify_route_token`.
4. A **strict, token-bounded** closure test was also run: the regex `(?<![\d.,])TOKEN(?![\d]|[.,]\d)`, applied against the governed text of source-closed records bound to the route.
5. Recommended bindings and extensions were simulated **in memory only**. All recommended texts below close 100% under the strict test.

---

## 0. Cross-cutting findings (these affect all six roots)

**X1 — The shipped literal audit gives false closures through substring matching. This is MATERIAL and extends U-14/EXF-003.**

`classify_route_token` accepts `token in t or bare in t`, which is a substring match. It also has the keyword heuristic already logged as EXF-003. Running the *proposed* held texts through the shipped script gives these results:

| Root | Token | False closure | Why it passed |
|---|---|---|---|
| PB-0522 /access/ | 98, 225, 106, 817, 1,021 | NON_SUBSTANTIVE | The paragraph contains «مصدر» / "source" |
| PB-0522 /access/ | 26 | CLM-003 | "26" is a substring of "2026" |
| PB-0520 /firms/ | 217 | CLM-059 | Substring of SMEPS "8,217" |
| PB-0521 /payments/ | EN tokens | Heuristic pass | — |
| PB-0345 /evidence/compare/ | 23 | CLM-033 | Substring of "2023" |
| PB-0345 /evidence/compare/ | EN/AR tokens | Heuristic pass | — |
| PB-0614 /methodology/ | 15.5% | CLM-024 | See X6 |

- In EN, **PB-0522 would have passed the shipped audit in full.** The HOLD therefore rested on the Lead's strict check. That was the correct call.
- Recommendation: before release, replace substring matching with token-bounded matching and replace the paragraph-keyword test with token-level classification. Add a date-range rule for "YYYY–YY". Until then, write ranges in full as "2022–2023".

**X2 — /reforms/ §6 already publishes five FMIIP baselines that no record carries. This is MATERIAL, on a live route.**

- The row is 03 r539/r540 (PB-0340/0341 APPLIED). It publishes 1,062,441; 200,898; 375,252; 170; 65.
- They pass `PUBLIC_LITERAL_CLOSURE.json` only by heuristic:
  - EN: `NON_SUBSTANTIVE_SYSTEM_INVENTORY…`. The trigger is the keyword "records" in "the project's results framework also records".
  - AR: `STABLE_ID_OR_TECHNICAL_STANDARD`. The trigger is "FPS/RTGS" in the paragraph.
- No 06/07/11 record carries these values. Once X1 is fixed, /reforms/ fails. This bears directly on PB-0345; see §5.

**X3 — XW-FMIIP-005 publishes the 2030 target of 1,021 without the 817 baseline. This is MATERIAL and a governed-rule breach.**

- The record text is in 06 r32 `summary_en/ar`, 02 r118 and 03 r298.
- It renders in `dist/en|ar/evidence/XW-FMIIP-005/index.html`: "1,021" appears once and "817" appears zero times.
- It is also a governed object on /payments/.
- This breaches the governed rule in VIS-TARGET-RESULT-STATE `limitations_en` (06 r83): "never show the 2030 target of 1,021 access points without the January-2025 baseline of 817". It also breaches PB-0522's own validation rule. The fix is in §4.

**X4 — CLM-054 carries values from SRC-CBY-001 but does not cite that source. This is MATERIAL, a lineage defect.**

- PB-0122/0123 (APPLIED) added the CBY-Aden market rates 792.69 → 1,529.4 YER/USD to CLM-054 in 06 r98 and 07 r57. Their Master rows are 18_CBY_MONETARY OBS-CBY-00621/00657, source SRC-CBY-001.
- CLM-054 `source_dependencies` = `SRC-SFD-Q4-2015-001; SRC-SFD-Q4-2020-001; SRC-SANAA-MFB-2024; INS-K04-023`. That is, no SRC-CBY-001.
- A reader who verifies 1,529.4 on /finance/ or /evidence/compare/ is sent to SFD and Sana'a microfinance documents that do not contain it.
- Two consequences:
  - Add SRC-CBY-001 to CLM-054's dependencies. It stays BOUND_EXACT.
  - Every EXTEND_EXISTING below adds the number's own source to the record's dependencies. Do not repeat the CLM-054 pattern.

**X5 — Two different sources are cited for the same FMIIP baselines. This is MATERIAL and goes to Specialist F.**

- 31_REFORMS_REGULATION FMIIP-RF-004/012–017 (r83, r91–r96) cite **SRC-WB-FMIIP-P180708**. Its `row_count` of 24 matches the 24 RF rows.
- 33_ANALYTICS_MASTER XW-FMIIP-001…005 (r152–156) name the **UNDP project page** as `project_source`.
- The 06 record XW-FMIIP-005 depends on SRC-UNDP-FMIIP-001 plus SRC-CBY-PAYREPORT-H1-2025.
- VIS-TARGET-RESULT-STATE (06 r83), which is BOUND_EXACT to SRC-WB-FMIIP-P180708, already asserts both 817 and 1,021.
- Recommendation: every FMIIP baseline binding below uses SRC-WB-FMIIP-P180708. F should confirm the values in the PAD PDF listed under its `additional_urls`. This cannot be re-verified offline in this pass.

**X6 — The same literal carries two meanings on /methodology/. This is MATERIAL.**

- On /methodology/, "15.5%" is already bound through CLM-024 (06 r39 `limitations_en`): "Do not publish raw 19.9%, 69.9%, 40.8%, 15.5% or other case shares as Yemen population estimates". There it is an **unweighted raw case share**.
- PB-0614 uses 15.5% as the **weighted** richest-60% account-ownership rate (25_FINDEX_BASELINE WB-FINDEX-OBS-2022-005, r9).
- Publishing PB-0614 as drafted would put two different "15.5%" on one route. The audit would also trace the new one to the record that forbids it.

**X7 — Cost of a new record.** Each new 06 record needs all of the following. It adds 2 HTML pages (en/ar) and 1 Page Spec.
- A 02_SITE_MAP evidence-detail row and 03 detail sections, plus a 07 row if it is a claim.
- A `page_spec_design_intent` entry (the generator raises an error if the route is missing) and search records.
- A change to the handoff manifest `controlled_counts`.
- A change to the hard-coded `284` in `scripts/validate.py` line 108.

Binding and extending existing records costs no routes. It only changes 06 `public_routes` (pipe list, with trailing slash) and 07 `public_routes` (JSON list, without trailing slash).

**X8 — Minor.** CLM-009's 07 route list includes `/measurement`, but its 06 list does not (06 r7 vs 07 r13). This asymmetry already exists. Align both when CLM-009 is re-bound.

---

## 1. PB-0160 / PB-0161 — /finance/: bank credit to the private sector, YER 1,350.4 bn, May 2026

**Target cells:**
- 02 r122 `full_copy_en/ar`.
- 03 r319 `body_en` / r320 `body_ar`.
- The spec says "#s5". In the current Master, r319/320 is **section_order 6, "System context"** ("Balance-sheet capacity is visible…"). The substring locator is still exact; only the section label has drifted.

### (a) Numbers
| Number | Master location | Source | Verification state |
|---|---|---|---|
| 1,350.4 | 18_CBY_MONETARY r385, OBS-CBY-00381, `BANK_CREDIT_PRIVATE_SECTOR_BN_YER` "Banks Credit to Private Sector", table T4_Bank_Assets, period 2026-05, YER billion, geography "Yemen / CBY statistical framework", SOURCE_DEFINED | SRC-CBY-001 (english.cby-ye.com/files/6a5a2e6bcc3cd.pdf; LOCATOR_ONLY; rights NOT_ASSESSED) | Master-verified, as the ledger states. Not re-opened against the PDF in this pass. |
| Jan 2023 (date) | CLM-033 and CLM-038 (bound to /finance/). Also the 18 flag on r379/380: "2022 market-exchange-rate revaluation break; preserve dual 2022 values" (legacy 338 vs revalued 1,301.6) | SRC-CBY-AR2023-001 et al.; SRC-CBY-001 | Closed as a date |

Context for the Lead:
- In the same table and month, loans and advances = 3,500.3 (r349) and total bank assets = 13,362.1 (r253). Private-sector credit is therefore a distinct, smaller line.
- The series fell from 2,105.1 (2024) to 1,392.3 (2025) while the market rate moved from 2,059.2 to 1,624.45 YER/USD (r673 → r685). That illustrates why movement must not be read as lending.

### (b) Existing carriers
- **None.** No 06/07/11/34 governed text contains 1,350.4.
- **No 06 record lists SRC-CBY-001** in `source_dependencies`. DS-CBY-MONETARY, with 686 rows, appears only in 16/17/33 metadata.
- Passport EP-CBY-BANKING-2025 (34 r25) points to /finance/ and /firms/ for "private/public/government credit", but it is not a record.

### (c) What is already on the route, and the deletion test
- §6 (r319) already says the compiled series cover "credit to the private sector" but gives no value.
- §5 (r317, CLM-033) already carries the January-2023 valuation caveat.
- /methodology/ §4 tells the public that current observations exist for "bank credit and other monetary statistics", yet no public page shows one.
- **Unique value:** the only current (May 2026) bank-side magnitude on /finance/, and the only public anchor for SRC-CBY-001.
- **A number-free rewrite fails the deletion test.** It would duplicate §6's first sentence and §5.

### (d) Least-invasive truthful option: **NEW_RECORD**
- No existing record's source contains the value.
- CLM-033 and CLM-038 are method and vintage claims ("AR2022 vs AR2023+"). They are also bound to /firms/ and /evidence/compare/. Extending them would change their period and meaning and push a May 2026 level onto three routes. Rejected.
- Proposed record:
  - Class TEMPORAL_OBSERVATION. The precedent is MFI-SPINE-2015-Q4 (06 r35).
  - ID for the Lead to assign, e.g. `CBY-CREDIT-2026-05`.
  - `source_dependencies: SRC-CBY-001`; `lineage_state: BOUND_EXACT`; verification template UI-VERIFY-BOUND.
  - `public_routes: /finance/`.
- **Why a new object is justified:**
  1. It gives SRC-CBY-001 its first record-level binding (686 Master rows, 0 records).
  2. It is independently citable as current banking context.
  3. It makes the X4 lineage fix coherent.
- **Fallback if routes stay frozen: REJECT.** Do not publish the number-free version.

### (e) Semantic-firewall risks
- A credit stock is not borrowers, firms, households or MSME credit.
- Bank credit to the private sector ≠ "loans and advances".
- Nominal ≠ real. No USD conversion (directive A).
- No ratio to the microfinance portfolio (PB-0162/0163: twelve MFBs sit on the same CBY-Aden bank list).
- CBY-Aden scope only.
- **FCV (E):** 14_SYSTEM_CHRONOLOGY r16 records an April 2024 CBY-Aden directive for Sana'a-headquartered banks to relocate to Aden. The institutional coverage of the statistics over time is not documented. State this in the record; do not assert a coverage change.

### (f) Recommended text

This is appended after "…common definitions and vintages." in 03 r319 and 02 r122.

- **EN:** For scale, statistics published by the Central Bank of Yemen in Aden record bank credit to the private sector of YER 1,350.4 billion in May 2026, in nominal rials. Because foreign-currency positions have been valued at the market exchange rate since January 2023, movements in this series can reflect revaluation as well as lending, and the figure does not show how many firms or households borrow.
- **AR:** ولتقدير الحجم، تسجل إحصاءات البنك المركزي اليمني في عدن ائتمانًا مصرفيًا مقدمًا للقطاع الخاص قدره 1,350.4 مليار ريال في مايو 2026 بالقيمة الاسمية. ولأن المراكز بالعملات الأجنبية تُقيَّم بسعر الصرف السوقي منذ يناير 2023، فقد تعكس تحركات هذه السلسلة أثر إعادة التقييم إلى جانب الإقراض نفسه، ولا يبين الرقم عدد المنشآت أو الأسر المقترضة.

**New record, core fields:**
- **title_en:** Bank credit to the private sector is a nominal stock, not a count of borrowers
- **title_ar:** الائتمان المصرفي المقدم للقطاع الخاص رصيد اسمي، لا عدد للمقترضين
- **summary_en:** Statistics published by the Central Bank of Yemen in Aden record bank credit to the private sector of YER 1,350.4 billion in May 2026, in nominal rials. Foreign-currency positions have been valued at the market exchange rate since January 2023, so movements in the series can reflect revaluation as well as lending. *[Optional, Lead choice; Master r379/380:]* The source publishes the end-2022 value on both bases: YER 338 billion on the earlier basis and YER 1,301.6 billion after revaluation.
- **summary_ar:** تسجل إحصاءات البنك المركزي اليمني في عدن ائتمانًا مصرفيًا مقدمًا للقطاع الخاص قدره 1,350.4 مليار ريال في مايو 2026 بالقيمة الاسمية. وتُقيَّم المراكز بالعملات الأجنبية بسعر الصرف السوقي منذ يناير 2023، لذلك قد تعكس تحركات السلسلة أثر إعادة التقييم إلى جانب الإقراض. *[اختياري:]* وينشر المصدر قيمة نهاية 2022 على الأساسين: 338 مليار ريال على الأساس السابق و1,301.6 مليار ريال بعد إعادة التقييم.
- **universe_en/ar:**
  - EN: Banks' credit to the private sector as compiled in CBY-Aden's statistical tables (bank assets), within the reporting scope defined by the issuing authority.
  - AR: الائتمان الذي تقدمه البنوك للقطاع الخاص كما تجمعه الجداول الإحصائية للبنك المركزي اليمني في عدن (أصول البنوك)، ضمن نطاق الإبلاغ الذي تحدده الجهة المصدِرة.
- **limitations_en:** A credit stock is not a count of borrowers, firms or households, and it is not credit to MSMEs. It is a separate line from "loans and advances" in the same table. Do not convert it to US dollars, deflate it, express it as growth across the January-2023 valuation change, or divide it by the microfinance portfolio. The institutional coverage of these statistics over time is not documented in the evidence base.
- **limitations_ar:** رصيد الائتمان ليس عددًا للمقترضين أو المنشآت أو الأسر، وليس ائتمانًا موجهًا للمنشآت الصغيرة والأصغر، وهو بند مستقل عن «القروض والسلف» في الجدول نفسه. ولا يجوز تحويله إلى الدولار أو تعديله بالأسعار الحقيقية أو حساب نمو عبر تغيير التقييم في يناير 2023، ولا قسمته على محفظة التمويل الأصغر. ولا توثق قاعدة الأدلة تطور النطاق المؤسسي لهذه الإحصاءات عبر الزمن.

---

## 2. PB-0520 — /firms/: formal firms' accounts and working-capital sources, 2022 seven-governorate survey

### (a) Numbers
All rows below are from 20_FIRM_FINANCE, source SRC-WB-FSD-2024-001, 2022-09, "Seven selected governorates". All are SOURCE_REPORTED.

| Number | Row / ID | Source figure | Base |
|---|---|---|---|
| 58.2%, 191, 328 | r5 FFO-2022-001 FFM-001 (191/328 = 58.23%) | Annex III Fig. 104, p.143 | num 191 / den 328. Comparability NOT_DIRECT_WITH_2013; the caveat notes micro firms under 5 employees |
| 69.12 / 0.56 / 1.97 / 1.31 / 10.15 / 16.66 | r50–55 FFO-2022-WC-01…06 FFM-009 | Fig. 110, p.148 | Average shares; `denominator_n` **empty**. Sum = 99.77 |
| 24.39 / 73.48 / 26.52 | r47–49 FFO-2022-INT-01…03 FFM-008 | Fig. 109, p.147 | MULTIPLE_RESPONSE; `denominator_n` **empty** |
| 80.18, 217 | r71 FFO-2022-INF-002 FFM-011 (18.43 have an account; 1.38 don't know) | Figs. 114–115, p.151 | den 217. Frame: activity and location lists |

### (b) Existing carriers
- **328** is carried by VIS-FIRM-FINANCE-PATH (06 r74; BOUND_EXACT; CLOSED_TO_SOURCE_ID; bound to /firms/).
- **217** is falsely matched to CLM-059 ("8,217"; see X1).
- **All other values: no governed record.**
- Passport EP-FIRM-2022 (34 r9) covers FFM-001…007 only. It does not cover FFM-008, FFM-009 or FFM-011.

### (c) What is already on the route, and the deletion test
/firms/ already has:
- constraints (22% finance; VIS-FIRM-CONSTRAINTS);
- severity (91.84%, filtered base);
- credit path (31/328; 18 responses);
- SMEPS programme figures.

It has no account-holding, working-capital, intermediary or informal-firm evidence. Every item in the section is unique on the site. It is the clearest firm-side "access ≠ use" evidence and sits in the same survey as the existing /firms/ items. **The deletion test passes.**

### (d) Least-invasive truthful option: **NEW_RECORD**
- **Proposed record:**
  - One CLAIM record (06 + 07), BOUND_EXACT to SRC-WB-FSD-2024-001 (already source-closed and FULL_PUBLIC_CARD).
  - `public_routes: /firms/`.
  - Next free CLM ID; CLM-061 is reserved by the held PB-0322.
  - Extend EP-FIRM-2022 to FFM-008, FFM-009 and FFM-011.
- **Why not EXTEND VIS-FIRM-FINANCE-PATH** (the queue's suggestion):
  1. It is a VISUAL record. Its 06 summary mirrors the 11 `accessible_summary` (11 r24), and its universe is fixed as "328 formal-firm sample; 31…; 18…". The encoding is "Two-stage funnel/composition".
  2. None of the new measures fits that record:
     - working-capital averages and intermediary shares have unknown bases;
     - the informal firms are a different sample frame;
     - the average-share and multiple-response items are not funnel stages.
  3. Extending only the 06 text would make the record describe numbers its visual does not show. Extending the contract is a J-level redesign.
  4. **"191 with an account → 31 with a credit line" cannot be drawn as nested.** The data do not show that the 31 are a subset of the 191.
- **Fallback if routes stay frozen: REJECT (hold).** Any number-free version would still be an untraced factual claim.

### (e) Semantic-firewall risks and corrections to the spec text
- **Missing sources:** the spec lists 4 of the 6 working-capital sources (96.49%). Readers will assume they are exhaustive, so add NBFI 1.97% and supplier credit 1.31%.
- **Base not held:** this applies to the working-capital averages as well as the intermediary item. The spec flags only the latter.
- **Base wording:** "73.48% of the surveyed formal firms" asserts a base that is not held. Use "of responding formal firms".
- **"Most frequently reported":** drop it. Only 3 response options are held.
- **Micro-firm caveat:** it belongs to the formal sample (FFO-2022-001 caveat).
- **Firewall rules:**
  - An average share is not a share of firms. Multiple-response figures are not market shares.
  - Firms ≠ people: never place 58.2% beside 11.9%. Account ≠ use.
  - Informal list frame ≠ national. No comparison with 2013.
- **FCV (E):** Fig. 111 area splits (r56–67, "IRG" / "Houthi-controlled") must not be published without E's review.

### (f) Recommended text

This is a new /firms/ section at order 5, after "Formal credit is a narrow path in this sample".

- **EN heading:** Formal firms in this sample: most held a bank account, but banks financed almost none of their working capital
- **EN body:** Among formal firms in the 2022 seven-governorate survey, 58.2% (191 of 328) reported a checking or savings account. Their working capital came mainly from internal sources: on average, 69.12% came from internal funds or retained earnings, 16.66% from money lenders, friends or relatives, 10.15% from advance payments by clients, 1.97% from non-bank financial institutions, 1.31% from supplier credit and 0.56% from banks. In a separate question on the financial intermediaries they use, 73.48% of responding formal firms named an exchange store or money exchanger and 24.39% a commercial bank; firms could name more than one, so these are not market shares. The evidence base does not hold the number of firms behind the working-capital averages or the intermediary question. Among the 217 informal firms surveyed, 80.18% had no bank account; that sample was drawn from activity and location lists rather than a national register. The formal-firm sample includes micro firms with fewer than five employees, and neither sample represents all Yemeni firms.
- **AR heading:** المنشآت الرسمية في هذه العينة: لدى أغلبها حساب مصرفي، لكن البنوك لم تموّل إلا جزءًا ضئيلًا جدًا من رأس مالها العامل
- **AR body:** أفادت 58.2% من المنشآت الرسمية في مسح عام 2022 الذي شمل سبع محافظات (191 من أصل 328 منشأة) بأن لديها حسابًا جاريًا أو حساب ادخار. غير أن رأس مالها العامل اعتمد أساسًا على مصادر داخلية: ففي المتوسط جاء 69.12% منه من الأموال الذاتية أو الأرباح المحتجزة، و16.66% من المقرضين أو الأصدقاء أو الأقارب، و10.15% من دفعات مقدمة من العملاء، و1.97% من مؤسسات مالية غير مصرفية، و1.31% من ائتمان الموردين، و0.56% فقط من البنوك. وفي سؤال مستقل عن الوسطاء الماليين الذين تتعامل معهم، ذكرت 73.48% من المنشآت الرسمية المجيبة محلات الصرافة أو الصرافين، و24.39% البنوك التجارية؛ ولأن المنشأة كان بإمكانها ذكر أكثر من وسيط، فهذه النسب ليست حصصًا سوقية. ولا تتضمن قاعدة الأدلة عدد المنشآت التي تستند إليها متوسطات رأس المال العامل ولا عدد المجيبين عن سؤال الوسطاء. أما المنشآت غير الرسمية التي شملها المسح، وعددها 217 منشأة، فلم يكن لدى 80.18% منها حساب مصرفي، وقد سُحبت عينتها من قوائم للأنشطة والمواقع لا من سجل وطني. وتضم عينة المنشآت الرسمية منشآت أصغر يقل عدد العاملين فيها عن خمسة، ولا تمثل أيٌّ من العينتين جميع المنشآت في اليمن.
- **New record title:**
  - EN: Formal firms in the 2022 survey: accounts were common, bank finance for working capital was not
  - AR: المنشآت الرسمية في مسح 2022: الحساب المصرفي شائع، أما تمويل البنوك لرأس المال العامل فنادر
- **New record summary:** the section body. The universe must state both samples separately.

---

## 3. PB-0521 — /payments/: e-wallet subscribers 2024 Q1–Q3 and H1 2025, with the series break

### (a) Numbers
All rows are in 19_PAYMENTS_DATA, IND-0011 "E-wallet subscribers".

| Number | Row / ID | Source | Comparability |
|---|---|---|---|
| 414,631 / 507,585 / 581,075 (2024 Q1/Q2/Q3) | r18–20 OBS-00014/15/16 | SRC-CBY-PAYREPORT-Q3-2024, p.5, lines 147–178 | COMPARABLE_WITH_QUALIFICATION. Caveat: "requires reconciliation with H1 2025 before treating as one continuous series" |
| 2,102,484 (2025 H1) | r38 OBS-00034 | SRC-CBY-PAYREPORT-H1-2025, p.1, lines 2–86 | **BREAK_IN_SERIES** |
| 11.9% | 25_FINDEX_BASELINE r5 | SRC-WB-FINDEX-AGG-2022 | Not carried on /payments/ |

### (b) Existing carriers
- **None of the four subscriber values** is in 06/07/11. 33 XW-FMIIP-002 holds 2,102,484 only in analytics.
- **CLM-010** (06 r8, 07 r14; BOUND_EXACT; CLOSED_TO_SOURCE_ID) depends on **both** SRC-CBY-PAYREPORT-Q3-2024 and SRC-CBY-PAYREPORT-H1-2025.
  - Title: "Wallet counts require semantic reconciliation".
  - claim_type: SOURCE_DISAGREEMENT.
  - It carries the provider-count break 7 → 9 → 8, drawn from the same two publications.
  - It is bound only to /evidence/compare/.
- VIS-PAYMENT-ANATOMY (bound to /payments/) depends on H1-2025 only, so it cannot carry the 2024 values.
- On /payments/, 11.9% is not carried by any record. CLM-004 is FRAMING_NO_FACT.

### (c) What is already on the route, and the deletion test
- §4 and §7 already say that subscribers may be duplicated or inactive and are "not necessarily active people". The page's point about subscribers is therefore already made in words.
- What is missing is the actual series and a concrete break. Red team: "you do not show the subscriber series".
- The 11.9% sentence fails the deletion test. It duplicates CLM-004 and /people/, and placing it beside 2.1 million subscribers invites a subscribers ÷ adults calculation. Remove it.

### (d) Least-invasive truthful option: **BIND_EXISTING + EXTEND_EXISTING CLM-010** (no new route)
- Both source documents are already its dependencies.
- The subscriber break is the same Q3-2024 vs H1-2025 reconciliation problem the claim already describes.

**Master cells to change:**
- **06 r8 CLM-010:**
  - `public_routes`: `/evidence/compare/ | /payments/`.
  - `title_en/ar`, `summary_en/ar`, `universe_en/ar` (add subscriber counts), `period_en/ar` (add 2024 Q1–Q3), `method_en/ar`, `limitations_en/ar`, `currentness_en/ar`.
- **07 r14 CLM-010:**
  - `public_routes`: `["/evidence/compare","/payments"]`.
  - `headline_en/ar`, `copy_en/ar`, `does_not_prove_en/ar`.
  - `evidence_inputs`: add OBS-00014/15/16/34.
- **02 r20 `full_copy_en/ar`; 03 r102 `body_en/ar`:** the /evidence/CLM-010/ detail page.

### (e) Semantic-firewall risks
- Subscribers ≠ people ≠ active users ≠ active e-wallet accounts. FMIIP-RF-015's rule is "Active e-wallet accounts are not subscribers".
- The H1 2025 infographic itself classes 1% of subscribers as companies (OBS-00040). That comparability is UNKNOWN, so do not publish it, but it confirms "not people".
- The heading must not imply growth across the break. The spec's "a rising count" is true only inside 2024.
- No line may join Q3 2024 to H1 2025.
- The reporting scope is CBY-Aden's.

### (f) Recommended text

This is a new /payments/ section at order 5, after "Before comparing payment numbers, ask what each one counts".

- **EN heading:** E-wallet subscribers: figures from two reports that do not form one series
- **EN body:** The CBY-Aden payments report for the third quarter of 2024 gives e-wallet subscriber counts of 414,631 for Q1, 507,585 for Q2 and 581,075 for Q3. The first-half 2025 infographic reports 2,102,484 subscribers. The two publications' subscriber definitions and reporting scope have not been reconciled, so the 2025 figure is not joined to the 2024 quarters and the difference is not read as growth. A subscriber count is not a count of unique people or of active users, and neither publication measures how many adults use a wallet.
- **AR heading:** مشتركو المحافظ الإلكترونية: أرقام من تقريرين لا تشكل سلسلة واحدة
- **AR body:** يورد تقرير المدفوعات الصادر عن البنك المركزي اليمني – عدن للربع الثالث من 2024 أعداد مشتركي المحافظ الإلكترونية: 414,631 في الربع الأول، و507,585 في الربع الثاني، و581,075 في الربع الثالث. أما إنفوغرافيك النصف الأول من 2025 فيورد 2,102,484 مشتركًا. ولم يُطابَق تعريف المشترك ولا نطاق الإبلاغ بين الإصدارين، لذلك لا يُوصل رقم 2025 بأرباع 2024، ولا يُقرأ الفرق بينهما نموًا. وعدد المشتركين ليس عددًا للأشخاص الفريدين ولا للمستخدمين النشطين، ولا يقيس أيٌّ من الإصدارين عدد البالغين الذين يستخدمون المحافظ.

**CLM-010 extended text (06 summary / 07 copy / 03 r102 / 02 r20):**
- **Title EN:** Wallet and subscriber counts require semantic reconciliation
- **Title AR:** اختلاف أعداد المحافظ ومشتركيها يحتاج إلى مطابقة دلالية
- **EN:** Official CBY-Aden publications report different wallet counts at different dates and in different contexts—7 in 2024 Q3, 9 in 2025 H1 and 8 licensed e-wallets in a September 2025 official statement. The same two payment reports give e-wallet subscriber counts of 414,631, 507,585 and 581,075 for 2024 Q1–Q3 (Q3 2024 report) and 2,102,484 for 2025 H1 (H1 2025 infographic). Because definitions and reporting scope have not been reconciled across these publications, neither set is presented as a continuous trend, and subscribers are not unique people or active users.
- **AR:** تورد وثائق رسمية للبنك المركزي اليمني – عدن أعدادًا مختلفة للمحافظ في تواريخ وسياقات مختلفة: 7 في الربع الثالث 2024، و9 في النصف الأول 2025، و8 محافظ إلكترونية مرخصة في بيان رسمي في سبتمبر 2025. ويورد تقريرا المدفوعات نفسهما أعداد مشتركي المحافظ الإلكترونية: 414,631 و507,585 و581,075 للأرباع الثلاثة الأولى من 2024 (تقرير الربع الثالث 2024)، و2,102,484 للنصف الأول من 2025 (إنفوغرافيك النصف الأول 2025). ولأن التعريفات ونطاق الإبلاغ لم تُطابَق بين هذه الإصدارات، لا تُعرض أيٌّ من المجموعتين كسلسلة اتجاه متصلة، والمشتركون ليسوا أشخاصًا فريدين ولا مستخدمين نشطين.
- **Limitations: add to EN/AR:**
  - EN: Do not join 581,075 (2024 Q3) and 2,102,484 (2025 H1) as growth, and do not treat subscribers as unique people or active users.
  - AR: لا يجوز وصل 581,075 (الربع الثالث 2024) بـ2,102,484 (النصف الأول 2025) بوصفه نموًا، ولا معاملة المشتركين كأشخاص فريدين أو مستخدمين نشطين.

---

## 4. PB-0522 — /access/: provider lists (98 / 225 / 106), 26 banks, FMIIP 817 vs 1,021

### (a) Numbers
| Number | Master location | Source |
|---|---|---|
| 98 / 225 / 106 | 22_PROVIDERS_DATA r139–141, CBY-ROSTER-2026-COMP/EST/AGT, unit "source-listed rows". Row r142 (429) is an "arithmetic sum only" and **must not be published** | SRC-CBY-EXCH-LIST-2026-001 |
| 26 | 22_PROVIDERS_DATA: 26 rows (8 BANK, 6 ISLAMIC_BANK, 12 MICROFINANCE_BANK) | SRC-CBY-BANKLIST-AR-2026-001 |
| 817 (Jan-2025 baseline) / 1,021 (Jun-2030 target) | 31 r83 FMIIP-RF-004. Unit "project-defined access points"; state "Project baseline / target" | SRC-WB-FMIIP-P180708 |

### (b) Existing carriers
All carriers below are BOUND_EXACT / CLOSED_TO_SOURCE_ID. **None is bound to /access/.**

| Value | Carrier | Rows | Routes | Source |
|---|---|---|---|---|
| 98 / 225 / 106 | **CLM-009** | 06 r7, 07 r13 | /providers/, /evidence/ (07 also /measurement) | — |
| 26 | **CLM-008** "Listing or licensing does not establish operation" | 06 r62, 07 r12 | /providers/ | — |
| 26 | CLM-055 | — | /providers/, /finance/ | — |
| 1,021 | **XW-FMIIP-005** "Financial access-point target versus current administrative objects" | 06 r32 | /reforms/, /payments/ | UNDP + CBY H1-2025. Breaches the rule: see X3 |
| 817 and 1,021 | VIS-TARGET-RESULT-STATE | 06 r83 `limitations` | /reforms/ | SRC-WB-FMIIP-P180708 |

/access/ is currently bound to CLM-003/050/052 and VIS-ACCESS-EVIDENCE-LAYER only.

### (c) What is already on the route, and the deletion test
- §2 ("What can be observed now") and §3 already say, in words, that rosters show listing and not operation.
- No provider magnitudes are shown, and the exchange/remittance sector is absent (red team, DOM-ACC-01).
- **Unique value:** the concrete lists that bear on the access question, with the listing ≠ operation firewall attached. **Pass.**
- Housekeeping, outside this root: §3 and §6 on /access/ repeat, word for word, the hero "Inference boundary" and "What remains unknown" blocks. This is stale duplicate copy for the R8.5 subtraction.

### (d) Least-invasive truthful option: **BIND_EXISTING (CLM-009, CLM-008) + EXTEND_EXISTING and BIND (XW-FMIIP-005)** (no new route)

**Master cells to change:**
- **CLM-009:**
  - 06 r7 `public_routes` += `/access/`.
  - 07 r13 `public_routes` += `"/access"`. At the same time, align 06 and 07 (X8).
- **CLM-008:**
  - 06 r62 `public_routes` += `/access/`.
  - 07 r12 `public_routes` += `"/access"`.
- **XW-FMIIP-005:**
  - 06 r32 `public_routes`: `/reforms/ | /payments/ | /access/`.
  - `summary_en/ar` and `limitations_en/ar`: add the 817 baseline.
  - `period_en/ar`: "January 2025 project baseline / 2030 project target; 2025 administrative context".
  - `source_dependencies` and `source_links`: add **SRC-WB-FMIIP-P180708**.
  - Mirror the change in 02 r118 `full_copy_en/ar` and 03 r298 `body_en/ar`.
  - This also fixes X3 on /evidence/XW-FMIIP-005/ and /payments/.
- **Why not bind VIS-TARGET-RESULT-STATE:** it is a generic reform visual contract. Binding its 06 row without its 11 row creates an object/visual route mismatch.

### (e) Semantic-firewall risks and corrections to the spec text
- Listing or licence ≠ operation. The three roster classes are never summed, so no 429.
- The 26 banks include 12 MFBs. Never add them to microfinance-provider counts.
- Target ≠ result. 1,021 always appears with 817, and no progress percentage is calculated.
- 817 ≠ ATMs + POS + agents.
- CBY-Aden scope only. Absence from a list ≠ "unlicensed elsewhere".
- **Wording changes:**
  - The spec says "the FMIIP project records 817 financial access points in January 2025". This reads as an observed count, so use "sets a January 2025 **baseline** of 817".
  - The spec says "None of these is a count of operating service points". The evidence base does not document the definition behind 817, so do not assert what it counts. Use "under a project definition that the evidence base does not document", then "None of these figures shows where services operate".
  - Use CLM-009's "individual exchange establishments".
  - Keep "substantial", which is the wording of binding correction #4.

### (f) Recommended text

This is a new /access/ section at order 3, after "What can be observed now".

- **EN heading:** Lists show who is registered, not where services operate
- **EN body:** Official lists document a substantial exchange and remittance provider presence relevant to the access question. The 2026 CBY-Aden roster lists 98 exchange companies, 225 individual exchange establishments and 106 remittance agents — three source categories, not a deduplicated count of firms — and the current CBY-Aden list of licensed banks names 26 banks. Listing or licensing is not operation, and later suspension or closure decisions are separate status events. Separately, the FMIIP results framework sets a January 2025 baseline of 817 financial access points against a 2030 target of 1,021, under a project definition that the evidence base does not document. None of these figures shows where services operate or how far people are from them.
- **AR heading:** القوائم الرسمية تبيّن الجهات المسجلة، لا أماكن تقديم الخدمة
- **AR body:** توثق القوائم الرسمية حضورًا كبيرًا لمقدمي خدمات الصرافة والحوالات يتصل بسؤال الوصول: فقائمة البنك المركزي اليمني – عدن لعام 2026 تضم 98 شركة صرافة و225 منشأة صرافة فردية و106 وكلاء حوالات — وهي ثلاث فئات يحددها المصدر، لا عددًا لمنشآت فريدة بعد إزالة الازدواج — كما تضم قائمته الحالية للبنوك المرخصة 26 بنكًا. والإدراج أو الترخيص لا يعني التشغيل، وقرارات الإيقاف أو الإغلاق اللاحقة أحداث حالة منفصلة. وبصورة مستقلة، يحدد إطار نتائج مشروع FMIIP خط أساس قدره 817 نقطة وصول مالي في يناير 2025 مقابل مستهدف قدره 1,021 نقطة في 2030، وفق تعريف للمشروع لا توثقه قاعدة الأدلة. ولا يبين أي من هذه الأرقام أين تعمل الخدمات ولا مدى بُعد الناس عنها.

**XW-FMIIP-005 extended summary:**
- **EN:** The FMIIP 2030 target of 1,021 access points, set against a January 2025 project baseline of 817 under the same project definition, cannot be added to or directly compared with ATMs, POS terminals or agents unless the project's access-point taxonomy and deduplication rules are documented.
- **AR:** لا يجوز جمع مستهدف FMIIP البالغ 1,021 نقطة وصول بحلول 2030، مقابل خط أساس للمشروع قدره 817 نقطة في يناير 2025 وفق التعريف نفسه، أو مقارنته مباشرة بأجهزة الصراف الآلي أو نقاط البيع أو الوكلاء ما لم تُوثق تصنيفات المشروع وقواعد إزالة الازدواج.

---

## 5. PB-0345 — /evidence/compare/: 11.9% vs about 3.3 million vs 1,062,441 and 375,252

### (a) Numbers
| Number | Master location | Source |
|---|---|---|
| 11.9% | 25_FINDEX_BASELINE r5 WB-FINDEX-OBS-2022-001 (adults 15+; 2021 wave; fieldwork 2022-11-07 to 2023-01-09) | SRC-WB-FINDEX-AGG-2022 |
| about 3.3 million | CLM-054 (06 r98, 07 r57) and passport EP-MFB-SAVERS-2023-K04. Secondary, source-termed "active savers" | SRC-SANAA-MFB-2024 |
| 1,062,441 / 375,252 | 31 r92/r94 FMIIP-RF-013/015 (Jan-2025 baselines). Also 33 r152/153 XW-FMIIP-001/002 | SRC-WB-FMIIP-P180708 (see X5) |

### (b) Existing carriers
- **11.9%:**
  - CLM-001 (06 r5, 07 r5; routes /people/ and /; BOUND_EXACT).
  - CLM-027 and VIS-FINDEX-GAPS (both /people/).
  - Not bound to /evidence/compare/.
- **3.3 million:** CLM-054 is **already bound to /evidence/compare/**, so this value is closed.
- **1,062,441 / 375,252:** no governed record anywhere. They are published on /reforms/ by heuristic only (X2).
- Note on the tool: the /evidence/compare/ interface lists exactly the records bound to the route as selectable options (CLM-010, CLM-054, CLM-041, …). Binding the underlying records therefore also makes the worked example **runnable in the tool**.

### (c) What is already on the route, and the deletion test
- The page has one section: tool instructions saying "not comparable" is a valid result.
- This would be the only worked example of that principle, applied to the product's three most-cited magnitudes (red team, IFI).
- **Pass.**

### (d) Least-invasive truthful option: **BIND_EXISTING (CLM-001) + NEW_RECORD (FMIIP January-2025 baselines)**
- **CLM-001:**
  - 06 r5 `public_routes` += `/evidence/compare/`.
  - 07 r5 += `"/evidence/compare"`.
- **New record:**
  - One new 06 record, BOUND_EXACT to SRC-WB-FMIIP-P180708.
  - It carries the published FMIIP-RF baselines: 1,062,441 (200,898 women-owned), 375,252, 170, 65. It does not carry targets or zero baselines.
  - `public_routes: /reforms/ | /evidence/compare/`.
  - Class: CROSSWALK_OBJECT in the XW-FMIIP family, or CLAIM. The Lead assigns the ID.
  - Its summary can mirror the already-approved /reforms/ §6 wording (PB-0340/0341).
- **Why genuine:** the same object closes X2 on /reforms/, which becomes a live failure as soon as U-14/X1 is fixed. It also gives the compare tool a selectable FMIIP record.
- **Why not extend XW-FMIIP-005:** accounts, merchants and agents are not access points. Folding them in would change that stable ID's meaning and break the one-to-one mapping to 33 XW-FMIIP-005.
- **Do not include CBY H1 2025 "accounts" 5,202,019.** Its row (19 r41, OBS-00037) has comparability UNKNOWN: "definition/period semantics require methodology note before public use". 33 XW-FMIIP-001 pairs it with 1,062,441, but it is not cleared.
- **Fallback if routes stay frozen: REWRITE.**
  - Keep 11.9% (closed through the CLM-001 binding) and 3.3 million (CLM-054).
  - Replace the FMIIP sentence with the number-free text below.
  - The heading still holds, because the section is about three kinds of measure.

### (e) Semantic-firewall risks and corrections to the spec text
- **Firewall rules:**
  - People ≠ savers ≠ accounts.
  - Survey estimate ≠ secondary report ≠ project baseline.
  - Different dates: 2022–2023 vs 2023 vs January 2025.
  - No population denominator (directive D).
- **Wording changes:**
  - "Three numbers" labels four figures. Use "Three measures" / "three kinds of figure".
  - "Relationships with providers" is an unsupported interpretation. Use "a count that has not been deduplicated into unique people", as CLM-054 states.
  - Write "2022–23" as "2022–2023" (X1).
  - Arabic: name the survey «المؤشر العالمي للشمول المالي (Findex)», per the terminology ledger §6. Write «3.3 مليون», as in CLM-054, and «بعد إزالة الازدواج», per ledger §5.

### (f) Recommended text

This is a new /evidence/compare/ section at order 2.

- **EN heading:** Three measures that cannot be combined
- **EN body:** Three kinds of figure are often set side by side. 11.9% is the share of adults (15+) in the survey's covered areas who had an account in the 2021 Global Findex wave, with fieldwork in 2022–2023. About 3.3 million is what a 2024 secondary source calls "active savers" in microfinance in 2023 — a count that has not been deduplicated into unique people. And 1,062,441 active bank accounts and 375,252 active e-wallet accounts are the FMIIP project's baselines for January 2025 — accounts, not people. These figures measure different things, for different populations and dates, from different kinds of evidence. They cannot be added, subtracted, ranked or converted into one another, and no population total is used here to turn the counts into shares. For these figures, "not comparable" is the correct result.
- **AR heading:** ثلاثة مقاييس لا يصح الجمع بينها
- **AR body:** كثيرًا ما توضع ثلاثة أنواع من الأرقام جنبًا إلى جنب. فنسبة 11.9% هي حصة البالغين (15 سنة فأكثر) في المناطق التي غطاها المسح ممن كان لديهم حساب في موجة 2021 من المؤشر العالمي للشمول المالي (Findex)، التي نُفذ عملها الميداني خلال 2022–2023. ونحو 3.3 مليون هو ما يسميه مصدر ثانوي منشور في 2024 «مدخرين نشطين» في قطاع التمويل الأصغر في 2023، وهو عدد لم يُحتسب بعد إزالة الازدواج، فلا يمثل أشخاصًا فريدين. أما 1,062,441 حسابًا مصرفيًا نشطًا و375,252 حساب محفظة إلكترونية نشطًا فهي خطوط الأساس لمشروع FMIIP في يناير 2025، أي حسابات لا أشخاص. وتقيس هذه الأرقام أشياء مختلفة، لمجتمعات وتواريخ مختلفة، ومن أنواع مختلفة من الأدلة؛ فلا يجوز جمعها أو طرحها أو ترتيبها أو تحويل بعضها إلى بعض، ولا يُستخدم هنا أي عدد للسكان لتحويل الأعداد إلى نسب. والنتيجة الصحيحة في هذه الحالة هي «غير قابلة للمقارنة».
- **Fallback FMIIP sentence (no new record):**
  - EN: And the FMIIP project's January 2025 baselines count active bank accounts and active e-wallet accounts — accounts, not people.
  - AR: أما خطوط الأساس لمشروع FMIIP في يناير 2025 فتعدّ الحسابات المصرفية النشطة وحسابات المحافظ الإلكترونية النشطة، أي حسابات لا أشخاص.

---

## 6. PB-0614 — /methodology/: "Uncertainty is stated, not manufactured" (15.5% / 6.5% / 9.0-point example)

### (a) Numbers
| Number | Master location | Source |
|---|---|---|
| 15.5 / 6.5 | 25_FINDEX_BASELINE r9 (richest 60%) / r8 (poorest 40%) | SRC-WB-FINDEX-AGG-2022 |
| 9.0 | Derived (15.5 − 6.5). Carried in VIS-FINDEX-GAPS | — |

### (b) Existing carriers
- 15.5, 6.5 and 9.0 are carried only by **VIS-FINDEX-GAPS** (06 r65, 11 r10; /people/; BOUND_EXACT).
- On /methodology/, "15.5%" is also carried by **CLM-024** (06 r39) as a *raw unweighted case share that must not be published as a population estimate*. See X6: this is a false trace.
- 6.5 and 9.0 are not carried on /methodology/.

### (c) What is already on the route, and the deletion test
- /methodology/ has no precision or sampling-uncertainty rule. §11 mentions uncertainty only for unresolved source conflicts, and §7 covers reproducibility, not precision.
- **The rule passes the deletion test; the numeric example fails it.**
  - The example duplicates /people/, where the 9.0-point gap is shown with its caveat: "No confidence intervals for these subgroup values are held in the evidence base".
  - It creates the X6 collision.

### (d) Least-invasive truthful option: **REWRITE_WITHOUT_UNTRACEABLE_NUMBERS**
- No binding is needed.
- Binding VIS-FINDEX-GAPS to /methodology/ would import a people-domain visual only to close an illustration, and it would put two different 15.5% figures on one route.
- The rule stays consistent with correction C and with U-08 (future design-based intervals from authorised microdata, reproduced rather than invented).

### (e) Semantic-firewall risks
- Weighted population estimate ≠ raw case share.
- A derived difference inherits the precision of its inputs (no "9.00"; validation rule met).
- No manufactured CI, SE or p-value.

### (f) Recommended text

This is a new /methodology/ section, placed after PB-0613.

- **EN heading:** Uncertainty is stated, not manufactured
- **EN body:** Survey estimates carry sampling and coverage uncertainty. Where a source publishes a confidence interval or standard error, it is reported with the estimate. Where it does not, no interval, standard error or significance test is added unless it can be reproduced from the survey's own weights and design. A derived value, such as the difference between two percentages, keeps the precision of its inputs, with no added decimal places, and small differences between estimates are not read as a ranking.
- **AR heading:** عدم اليقين يُبيَّن ولا يُصطنع
- **AR body:** تنطوي تقديرات المسوح على قدر من عدم اليقين مصدره المعاينة ونطاق التغطية. فإذا نشر المصدر فترة ثقة أو خطأً معياريًا عُرض مع التقدير، وإذا لم ينشره فلا تُضاف فترة ثقة ولا خطأ معياري ولا اختبار دلالة ما لم يمكن إعادة احتسابها من أوزان المسح وتصميمه. وتحتفظ القيمة المشتقة، كالفرق بين نسبتين، بدقة مدخلاتها من دون منازل عشرية إضافية، ولا تُقرأ الفروق الطفيفة بين التقديرات على أنها ترتيب.

---

## 7. Strict closure check of the recommended texts (in-memory simulation)

The recommended bindings and extensions were applied in memory, and every recommended EN and AR text was then checked with the token-bounded rule.

| Root | Result | Closing records |
|---|---|---|
| PB-0160/0161 | 1,350.4 closed | new CBY record |
| PB-0520 | all 13 tokens closed | new firm record; 328 also closed by VIS-FIRM-FINANCE-PATH |
| PB-0521 | 414,631 / 507,585 / 581,075 / 2,102,484 closed | extended CLM-010 |
| PB-0522 | 98 / 225 / 106 closed | CLM-009 |
| PB-0522 | 26 closed | CLM-008 |
| PB-0522 | 817 / 1,021 closed | extended XW-FMIIP-005 |
| PB-0345 | 11.9% and 15 closed | CLM-001 |
| PB-0345 | 3.3 closed | CLM-054 |
| PB-0345 | 1,062,441 / 375,252 closed | new FMIIP record |
| PB-0614 | no numbers | — |

- **0 unresolved tokens.** Years were classed as dates, and "2022–2023" is written in full.
- The same new FMIIP record also closes 1,062,441, 200,898, 375,252, 170 and 65 on /reforms/ (X2).

**Route impact:**

| Scenario | HTML pages | Page Specs |
|---|---|---|
| Recommended set (3 new records: CBY credit, firm finance, FMIIP baselines) | 284 → 290 | 141 → 144 |
| Minimal set (no new routes: PB-0521, PB-0522, PB-0614, and PB-0345 fallback; PB-0160 and PB-0520 stay held or rejected) | 284 | 141 |

---

## 8. Summary table

| Root | Target route | Recommended disposition | Records to bind / extend | Numbers | Rationale (one line) |
|---|---|---|---|---|---|
| PB-0160/0161 | /finance/ (§6, r319/320) | NEW_RECORD (fallback: REJECT) | New TEMPORAL_OBSERVATION record on SRC-CBY-001, bound to /finance/. Separately, add SRC-CBY-001 to CLM-054 deps (X4) | 1,350.4 (18 r385 OBS-CBY-00381) | No record binds SRC-CBY-001; CLM-033/038 are vintage claims; a number-free version fails the deletion test |
| PB-0520 | /firms/ (new §5) | NEW_RECORD (fallback: hold) | New CLAIM on SRC-WB-FSD-2024-001, bound to /firms/; extend EP-FIRM-2022 to FFM-008/009/011 | 58.2, 191, 328, 69.12, 16.66, 10.15, 1.97, 1.31, 0.56, 73.48, 24.39, 217, 80.18 (20 r5, r47–55, r71) | Four measures on three bases do not fit the VIS-FIRM-FINANCE-PATH funnel; nesting 191 → 31 is not established; add the two omitted WC shares and the base caveat |
| PB-0521 | /payments/ (new §5) | BIND_EXISTING + EXTEND_EXISTING | CLM-010: 06 r8 and 07 r14 (+/payments/; subscriber text), 02 r20, 03 r102 | 414,631; 507,585; 581,075; 2,102,484 (19 r18–20, r38) | CLM-010 already depends on both reports and states the same break; drop 11.9% |
| PB-0522 | /access/ (new §3) | BIND_EXISTING + EXTEND_EXISTING | CLM-009 (06 r7 / 07 r13), CLM-008 (06 r62 / 07 r12) +/access/; XW-FMIIP-005 (06 r32 +817, +SRC-WB-FMIIP-P180708, +/access/; 02 r118; 03 r298) | 98 / 225 / 106 (22 r139–141); 26 (22 bank list); 817 / 1,021 (31 r83) | No new route; also fixes the live "1,021 without 817" breach (X3) |
| PB-0345 | /evidence/compare/ (new §2) | BIND_EXISTING + NEW_RECORD (fallback: REWRITE without the FMIIP numbers) | CLM-001 (06 r5 / 07 r5) +/evidence/compare/; CLM-054 already bound; new FMIIP-baseline record on SRC-WB-FMIIP-P180708 bound to /reforms/ and /evidence/compare/ | 11.9 (25 r5); 3.3 m (CLM-054); 1,062,441 / 375,252 (31 r92/94) | The new record also closes the /reforms/ baselines that now pass only by heuristic (X2) and makes the example selectable in Compare |
| PB-0614 | /methodology/ (new section) | REWRITE_WITHOUT_UNTRACEABLE_NUMBERS | none | none (15.5 / 6.5 / 9.0 removed) | 15.5% on this route already means a forbidden raw case share (CLM-024); the rule is unique, the example is not |
