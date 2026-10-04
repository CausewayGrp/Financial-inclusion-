# Four-digit unit check — item 17 (RC-1)

Instruction: `audit/release_candidate/INSTRUCTIONS.md`, Part A, G2 item 17 — sweep every public figure of four or more digits
for the item 4 failure (a decimal point and a thousands separator mixed in one displayed series) and for a figure shown with
no unit beside it. Tool: `python3 audit/release_candidate/four_digit_unit_check.py dist --write <file>` (re-runnable).

## Result

| Sweep | Before RC-1 (build at `ef3c490`) | After RC-1 |
|---|---|---|
| A · drawn series mixing a point-only value with a comma value | 1 (VIS-POS-VALUE: 317.639 … 910.688 beside 1,262) | 0 |
| A · prose or table sentence mixing the two notations | 18 | 10 |
| B · figure of four or more digits with no unit in its sentence or cell | 127 | 111 |

## True instances, fixed in RC-1 (transaction `audit/release_candidate/rc_1_truth_fixes.py`)

1. **VIS-POS-VALUE series** (item 4): values now displayed in whole YER million (318 … 911, 1,262); a rounding note is on
   each row's caveats and in the record's method, in both editions; prose "YER 1.262 billion" → "YER 1,262 million".
2. **Remittance prose** (item 4): "USD 6.245 billion / 3.42 billion" → "USD 6,245 million / 3,422.16 million" in the Reading
   *Same year, different number*, /remittances/ and CLM-032, so the prose matches the chart's unit and notation.
3. **YSC-004** (item 17): "from YER 810.9 billion … to 1,673 billion" now reads "from about YER 811 billion"; the source value
   is kept in the event's interpretation note.
4. **CBY-Aden market rate** (item 17): "792.69 to 1,529.4 rials per US dollar" → "about 793 to about 1,529 rials per US
   dollar" in /finance/ §3 and CLM-054.
5. **SFD savers** (item 17): "1.61 million savers" beside "88,445 borrowers" → "1,611,206 savers/depositors" in /finance/ §3,
   CLM-054, VIS-MFI-DIVERGENCE and the Reading *Microfinance structural divergence*.

## Remaining lines — dispositions (all NOT AN INSTANCE)

The raw lines are listed below the dispositions, exactly as the tool printed them after RC-1. Each falls under one of these
classes; none is a figure shown in a series with mixed notation or a figure a reader sees without its unit.

| Class | Lines | Why it is not an instance |
|---|---|---|
| **A1 · different quantities in one sentence** | VIS-POS-TRANSACTIONS (21,099 / 24,026 counts beside the derived 13.87%), /finance/ (1,611,206 savers beside YER 33.379 billion) — both editions | Each number is its own quantity with its own unit; no series mixes notation. A percentage or a billion-scale amount keeps its decimals by the evidence record's precision rule. |
| **A2 · chart text run-together** | Reading *Same year, different number*: "2,900.22 / 1,577.7 USD million … 105.74 111.73 118" | The sweep joins an SVG's text nodes: the USD-million value labels of one chart and the index-value labels (2021 = 100) of a second panel. Each series is notation-consistent. |
| **B1 · table cell under a unit-bearing header** | CLM-037, VIS-FINDEX-GAPS, VIS-POS-TERMINALS, VIS-POS-TRANSACTIONS, VIS-POS-VALUE, VIS-PAYMENT-ANATOMY, VIS-REMITTANCE-MACRO, Reading *Same year, different number* (cells) | The cell is a value in a table whose column header or caption carries the unit (USD million, %, count, YER million); the sweep reads the cell alone. |
| **B2 · chart axis tick or data label** | "1,000 2,000 3,000 4,000", "0 2,000 4,000 6,000" | Scale presentation; the axis title carries the unit. |
| **B3 · count with its noun outside the sentence window** | CLM-054, CLM-057, CLM-058, /finance/, Reading *Microfinance structural divergence* (78,686; 80,800; 80,000–90,000) | The measure is named in the preceding clause ("93,118 active borrowers … and 88,445 at end-2020. A 2024 policy paper … reports 78,686") or as "active-borrower point" / "borrower base", which the sweep's word list ("borrowers") does not match, or across a semicolon the sweep splits on; a reader sees the unit. |
| **B4 · percentage-point gap written as "-point"** | /people/ §4, Reading *Gender gap* (12.91-point …) | "12.91-point difference" carries its unit (percentage points); the sweep's list has "points", not "-point". |
| **B5 · derived ratio or a target in its own unit** | CLM-042 (1.838), CLM-043 AR (7.117 / 3.614 = 1.97), XW-FMIIP-005 (1,021 target against 817 baseline) | A dimensionless ratio and its stated inputs; a project indicator whose unit is printed on the same record ("Population or base: Access points as defined by the project"). |
| **B6 · identifier, not a figure** | /data/ (project 47229) | A funder's project number, printed beside the project's name. |
| **B7 · run-together of separate elements** | /evidence/ ("20142014", "19981997"), Reading *Reforms newer than people evidence* ("12025-06-17") | The sweep strips inline tags, joining a list's ordinal or its "when" span to the date next to it; the page renders them as separate elements ("1", "2025-06-17"; "2014"). |

## Raw sweep after RC-1

Built site: `dist`; pages swept: 287.

### A. Drawn series mixing a decimal point with a thousands separator

- none

### A. Prose or table sentences mixing a point-only figure with a comma-separated figure

- `en` /evidence/VIS-POS-TRANSACTIONS/ — 21,099, 24,026, 13.87% — “Between December 2025 (21,099) and January 2026 (24,026), the raw totals imply growth of 13.87%, while the January source graphic displays +4.9%;”
- `en` /evidence/VIS-POS-TRANSACTIONS/ — 13.87%, 24,026, 21,099 — “The December 2025 to January 2026 change of 13.87% is derived by this resource (24,026 divided by 21,099, minus one) and is kept beside the +4.9% displayed in the January release.”
- `en` /finance/ — 1,611,206, 33.379 — “The verified 2020 figures are 1,611,206 savers/depositors and YER 33.379 billion;”
- `en` /readings/same-year-different-number/ — 2,900.22, 105.74, 111.73 — “2021 · 2,900.22 USD million 110 120 130 100 2021 2022 2023 2024 105.74 111.73 118”
- `en` /readings/same-year-different-number/ — 1,577.7, 105.74, 111.73 — “2021 · 1,577.7 USD million 110 120 130 100 2021 2022 2023 2024 105.74 111.73 118”
- `ar` /evidence/VIS-POS-TRANSACTIONS/ — 21,099, 24,026, 13.87% — “وبين ديسمبر 2025 (21,099) ويناير 2026 (24,026) تعطي الإجماليات الخام نموًا نسبته 13.87%، بينما يعرض رسم مصدر يناير نسبة +4.9%؛”
- `ar` /evidence/VIS-POS-TRANSACTIONS/ — 13.87%, 24,026, 21,099 — “ويشتق هذا المورد التغير بين ديسمبر 2025 ويناير 2026 البالغ 13.87% (بقسمة 24,026 على 21,099 ثم طرح واحد)، ويُبقيه إلى جانب نسبة +4.9% المعروضة في إصدار يناير.”
- `ar` /finance/ — 1,611,206, 33.379 — “أما النقاط المرجعية الموثقة لعام 2020 فهي 1,611,206 من المدخرين/المودعين ومحفظة قدرها 33.379 مليار ريال، ولم يثبت أن «المدخر النشط» و«المدخر/المودع» مقياس واحد.”
- `ar` /readings/same-year-different-number/ — 2,900.22, 105.74, 111.73 — “2021 · 2,900.22 مليون دولار أمريكي 110 120 130 100 2021 2022 2023 2024 105.74 111.73 118”
- `ar` /readings/same-year-different-number/ — 1,577.7, 105.74, 111.73 — “2021 · 1,577.7 مليون دولار أمريكي 110 120 130 100 2021 2022 2023 2024 105.74 111.73 118”

### B. Figures of four or more digits with no unit beside them (sentence or cell carries no unit, currency, percentage or count noun)

- `en` /data/ — 47229 — “Promotion of the Financial Sector for Micro, Small and Medium-sized Enterprises (MSMEs) III, Yemen (project 47229)”
- `en` /evidence/CLM-037/ — 3,066.58 — “3,066.58;”
- `en` /evidence/CLM-037/ — 3,240.46 — “3,240.46;”
- `en` /evidence/CLM-037/ — 1,668.2 — “1,668.2;”
- `en` /evidence/CLM-037/ — 1,762.8 — “1,762.8;”
- `en` /evidence/CLM-042/ — 1.838 — “the result is 1.838 in each year.”
- `en` /evidence/CLM-054/ — 78,686 — “A 2024 policy paper citing SFD/SMED data reports 78,686 at end-2023;”
- `en` /evidence/CLM-057/ — 80,800, 78,686 — “The roughly 80,800 active-borrower point cited for June 2023 and the 78,686 end-2023 point come through different source chains.”
- `en` /evidence/CLM-058/ — 80,000, 90,000 — “World Bank Financial Sector Diagnostics reports that Yemen's active microfinance borrower base remained broadly around 80,000–90,000 through 2021 while average loan amounts rose, with subsector growth appearing to be driven more by larger l”
- `en` /evidence/VIS-FINDEX-GAPS/ — 18.35 — “18.35”
- `en` /evidence/VIS-FINDEX-GAPS/ — 19.53 — “19.53”
- `en` /evidence/VIS-FINDEX-GAPS/ — 16.11 — “16.11”
- `en` /evidence/VIS-FINDEX-GAPS/ — 12.91 — “12.91”
- `en` /evidence/VIS-FINDEX-GAPS/ — 12.55 — “12.55”
- `en` /evidence/VIS-PAYMENT-ANATOMY/ — 2,341,752 — “Payment cards 2,341,752”
- `en` /evidence/VIS-POS-TERMINALS/ — 1,060 — “1,060”
- `en` /evidence/VIS-POS-TERMINALS/ — 1,149 — “1,149”
- `en` /evidence/VIS-POS-TERMINALS/ — 1,226 — “1,226”
- `en` /evidence/VIS-POS-TERMINALS/ — 1,357 — “1,357 · Source figures disagree — the published total is plotted;”
- `en` /evidence/VIS-POS-TERMINALS/ — 1,473 — “1,473 · Source figures disagree — the published total is plotted;”
- `en` /evidence/VIS-POS-TRANSACTIONS/ — 8,015 — “8,015”
- `en` /evidence/VIS-POS-TRANSACTIONS/ — 10,143 — “10,143”
- `en` /evidence/VIS-POS-TRANSACTIONS/ — 12,096 — “12,096”
- `en` /evidence/VIS-POS-TRANSACTIONS/ — 11,832 — “11,832”
- `en` /evidence/VIS-POS-TRANSACTIONS/ — 27,187 — “27,187”
- `en` /evidence/VIS-POS-TRANSACTIONS/ — 22,605 — “22,605”
- `en` /evidence/VIS-POS-TRANSACTIONS/ — 18,737 — “18,737”
- `en` /evidence/VIS-POS-TRANSACTIONS/ — 19,548 — “19,548”
- `en` /evidence/VIS-POS-TRANSACTIONS/ — 22,194 — “22,194”
- `en` /evidence/VIS-POS-TRANSACTIONS/ — 21,099 — “21,099 · Source figures disagree — the published total is plotted;”
- `en` /evidence/VIS-POS-TRANSACTIONS/ — 24,026 — “24,026 · Source figures disagree — the published total is plotted;”
- `en` /evidence/VIS-POS-VALUE/ — 1,262 — “1,262”
- `en` /evidence/VIS-REMITTANCE-MACRO/ — 1,000, 2,000, 3,000, 4,000, 1,329.2, 1,408.4, 1,491.1, 1,577.7, 1,668.2, 1,762.8, 1,861.7, 1,977, 2,159, 2,364, 2,591, 2,840, 3,110 — “1,000 2,000 3,000 4,000 0 2018 2019 2020 2021 2022 2023 2024 2025 2026 2027 2028 2029 2030 1,329.2 1,408.4 1,491.1 1,577.7 1,668.2 1,762.8 1,861.7 1,977 2,159 2,364 2,591 2,840 3,110 Reported by the source Estimate — not an observation Proj”
- `en` /evidence/VIS-REMITTANCE-MACRO/ — 1,329.2 — “1,329.2 · Reported by the source · IMF 2025 Article IV staff report”
- `en` /evidence/VIS-REMITTANCE-MACRO/ — 1,408.4 — “1,408.4 · Reported by the source · IMF 2025 Article IV staff report”
- `en` /evidence/VIS-REMITTANCE-MACRO/ — 1,491.1 — “1,491.1 · Reported by the source · IMF 2025 Article IV staff report”
- `en` /evidence/VIS-REMITTANCE-MACRO/ — 1,577.7 — “1,577.7 · Reported by the source · IMF 2025 Article IV staff report”
- `en` /evidence/VIS-REMITTANCE-MACRO/ — 1,668.2 — “1,668.2 · Reported by the source · IMF 2025 Article IV staff report”
- `en` /evidence/VIS-REMITTANCE-MACRO/ — 1,762.8 — “1,762.8 · Reported by the source · IMF 2025 Article IV staff report”
- `en` /evidence/VIS-REMITTANCE-MACRO/ — 1,861.7 — “1,861.7 · Reported by the source · IMF 2025 Article IV staff report”
- `en` /evidence/XW-FMIIP-005/ — 1,021 — “The 1,021 target has meaning only against the 817 baseline under the same project definition;”
- `en` /evidence/ — 20142014 — “Historical borrowing patterns in 20142014”
- `en` /evidence/ — 20142014 — “Historical saving patterns in 20142014”
- `en` /evidence/ — 20142014 — “Domestic-remittance pathways in 20142014”
- `en` /finance/ — 78,686 — “a 2024 policy paper citing SFD/SMED data reports 78,686 for end-2023, for a set of providers that has not yet been verified.”
- `en` /finance/ — 78,686 — “A 2024 policy paper citing SFD/SMED data reports 78,686 for end-2023;”
- `en` /people/ — 12.91, 12.55, 11.10 — “The 12.91-point gender difference, the 9.0-point income difference, the 12.55-point education difference and the 11.10-point age difference do not establish their causes.”
- `en` /readings/gender-gap-measured-causes-open/ — 12.91 — “the current evidence does not divide the 12.91-point gap among them.”
- `en` /readings/microfinance-structural-divergence/ — 78,686 — “a 2024 Sana’a Center for Strategic Studies paper citing SFD/SMED data reports 78,686 for end-2023, for a set of providers not yet verified.”
- `en` /readings/microfinance-structural-divergence/ — 80,000, 90,000 — “The World Bank’s Financial Sector Diagnostics describe an active borrower base that stayed broadly around 80,000–90,000 through 2021 while average loan amounts rose.”
- `en` /readings/reforms-newer-than-people-evidence/ — 12025 — “1 2 3–6 12025-06-17FMIIP approved ↗”
- `en` /readings/reforms-newer-than-people-evidence/ — 32026 — “32026-06-17Unified network as the main transfer channel ↗”
- `en` /readings/reforms-newer-than-people-evidence/ — 42026 — “42026-07-27Unified Money Network company: restructuring, capital increase and new bank shareholders ↗”
- `en` /readings/reforms-newer-than-people-evidence/ — 52026 — “52026-08-03Founding assembly of the Yemeni Payments and Clearing Company (YPCC) ↗”
- `en` /readings/reforms-newer-than-people-evidence/ — 62026 — “62026-08-04First board meeting of the Yemeni Payments and Clearing Company (YPCC) ↗”
- `en` /readings/same-year-different-number/ — 6,245 — “6,245”
- `en` /readings/same-year-different-number/ — 3,422.16 — “3,422.16”
- `en` /readings/same-year-different-number/ — 2,000, 4,000, 6,000 — “0 2,000 4,000 6,000”
- `en` /readings/same-year-different-number/ — 2,900.22 — “2,900.22”
- `en` /readings/same-year-different-number/ — 3,066.58 — “3,066.58”
- `en` /readings/same-year-different-number/ — 105.74 — “105.74”
- `en` /readings/same-year-different-number/ — 3,240.46 — “3,240.46”
- `en` /readings/same-year-different-number/ — 111.73 — “111.73”
- `en` /readings/same-year-different-number/ — 1,577.7 — “1,577.7”
- `en` /readings/same-year-different-number/ — 1,668.2 — “1,668.2”
- `en` /readings/same-year-different-number/ — 1,762.8 — “1,762.8”
- `en` /readings/same-year-different-number/ — 1,861.7 — “1,861.7”
- `ar` /evidence/CLM-037/ — 3,066.58 — “3,066.58؛”
- `ar` /evidence/CLM-037/ — 3,240.46 — “3,240.46؛”
- `ar` /evidence/CLM-037/ — 1,668.2 — “1,668.2؛”
- `ar` /evidence/CLM-037/ — 1,762.8 — “1,762.8؛”
- `ar` /evidence/CLM-043/ — 7.117, 3.614 — “واحتسب هذا المورد النسبة بقسمة صافي السهو والخطأ على بند التحويلات (2025: 7.117 مقسومًا على 3.614 يساوي 1.97).”
- `ar` /evidence/VIS-FINDEX-GAPS/ — 18.35 — “18.35”
- `ar` /evidence/VIS-FINDEX-GAPS/ — 19.53 — “19.53”
- `ar` /evidence/VIS-FINDEX-GAPS/ — 16.11 — “16.11”
- `ar` /evidence/VIS-FINDEX-GAPS/ — 12.91 — “12.91”
- `ar` /evidence/VIS-FINDEX-GAPS/ — 12.55 — “12.55”
- `ar` /evidence/VIS-PAYMENT-ANATOMY/ — 2,341,752 — “بطاقات الدفع 2,341,752”
- `ar` /evidence/VIS-PAYMENT-ANATOMY/ — 2,341,752 — “2,341,752 · ليست أشخاصًا، ولا حاملي بطاقات نشطين · لا تصح المقارنة المباشرة”
- `ar` /evidence/VIS-PAYMENT-ANATOMY/ — 2,102,484 — “2,102,484 · ليسوا أشخاصًا فريدين، ولا مستخدمين نشطين · لا تصح المقارنة المباشرة”
- `ar` /evidence/VIS-POS-TERMINALS/ — 1,060 — “1,060”
- `ar` /evidence/VIS-POS-TERMINALS/ — 1,149 — “1,149”
- `ar` /evidence/VIS-POS-TERMINALS/ — 1,226 — “1,226”
- `ar` /evidence/VIS-POS-TRANSACTIONS/ — 8,015 — “8,015”
- `ar` /evidence/VIS-POS-TRANSACTIONS/ — 10,143 — “10,143”
- `ar` /evidence/VIS-POS-TRANSACTIONS/ — 12,096 — “12,096”
- `ar` /evidence/VIS-POS-TRANSACTIONS/ — 11,832 — “11,832”
- `ar` /evidence/VIS-POS-TRANSACTIONS/ — 27,187 — “27,187”
- `ar` /evidence/VIS-POS-TRANSACTIONS/ — 22,605 — “22,605”
- `ar` /evidence/VIS-POS-TRANSACTIONS/ — 18,737 — “18,737”
- `ar` /evidence/VIS-POS-TRANSACTIONS/ — 19,548 — “19,548”
- `ar` /evidence/VIS-POS-TRANSACTIONS/ — 22,194 — “22,194”
- `ar` /evidence/VIS-POS-VALUE/ — 1,262 — “1,262”
- `ar` /evidence/ — 20142014 — “أنماط اقتراض تاريخية في 20142014”
- `ar` /evidence/ — 20142014 — “أنماط ادخار تاريخية في 20142014”
- `ar` /evidence/ — 20142014 — “مسارات الحوالات المحلية في 20142014”
- `ar` /evidence/ — 19981997 — “الأصل المؤسسي في 1997 وبداية البرنامج التشغيلي في 19981997 / 1998”
- `ar` /readings/reforms-newer-than-people-evidence/ — 12025 — “1 2 3–6 12025-06-17الموافقة على مشروع FMIIP ↗”
- `ar` /readings/reforms-newer-than-people-evidence/ — 32026 — “32026-06-17الشبكة الموحدة قناةً رئيسية للحوالات ↗”
- `ar` /readings/same-year-different-number/ — 6,245 — “6,245”
- `ar` /readings/same-year-different-number/ — 3,422.16 — “3,422.16”
- `ar` /readings/same-year-different-number/ — 2,000, 4,000, 6,000 — “0 2,000 4,000 6,000”
- `ar` /readings/same-year-different-number/ — 2,900.22 — “2,900.22”
- `ar` /readings/same-year-different-number/ — 3,066.58 — “3,066.58”
- `ar` /readings/same-year-different-number/ — 105.74 — “105.74”
- `ar` /readings/same-year-different-number/ — 3,240.46 — “3,240.46”
- `ar` /readings/same-year-different-number/ — 111.73 — “111.73”
- `ar` /readings/same-year-different-number/ — 1,577.7 — “1,577.7”
- `ar` /readings/same-year-different-number/ — 1,668.2 — “1,668.2”
- `ar` /readings/same-year-different-number/ — 1,762.8 — “1,762.8”
- `ar` /readings/same-year-different-number/ — 1,861.7 — “1,861.7”
