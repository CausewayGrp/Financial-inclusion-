# V1 - World Bank verification: Yemen Global Findex 2021-22 (read-only)

Run date: 2026-10-11. Nothing under <repository> was modified. No Microdata API key was used or requested.
No respondent-level file was downloaded. Downloaded material (all in
`<session scratchpad>/v5/dl/V1/`):
catalogue HTML pages, the public DDI codebook XML (metadata only; `ddi.xml`), the catalogue JSON metadata, four published PDFs,
and World Bank API JSON. Python was run as `python3 -I`.

Page conventions: "PDF p" = page index in the file; "printed p" = number printed on the page.

---------------------------------------------------------------------------------------------------

## HEADLINE FINDINGS

1. CONFIRMED. fin29_1 (catalogue variable V67): 393 valid (asked), 39 yes, 354 no, 0 dk, 0 ref, 607 system-missing. Unweighted.
   (Percentages as printed: yes 9.9%, no 90.1%.)
2. The catalogue and DDI give NO question text, NO universe, NO pre-question and NO skip logic for fin29_1. They also give no
   derivation of any published indicator. The wording and skip logic exist only in the generic 2021 Global Findex questionnaire PDF
   attached to the catalogue (not a Yemen-specific instrument).
3. The published indicator `fin29` is "% age 15+" (all adults, not % of recipients). Its definition does NOT explain a 0 for
   Yemen. The Yemen microdata has 39 of 1,000 respondents answering yes (3.9% unweighted). The definition and universe cannot
   reduce that to 0.
   Published value for Yemen: 0 (an integer 0, wave date "2022"). The same integer 0 appears for Azerbaijan, whose DDI shows 97 yes
   of 182 recipients. Azerbaijan and Yemen are the only two of the 16 economies collected in 2022 whose microdata lacks all
   mobile-money items. Both have fin28 = fin29 = 0. So the zero looks like a database artefact, but the derivation is NOT
   documented on any page I could read. This is an inference.
4. The 2021-22 Methodology PDF contains NO statement that mobile-money questions or modules were not asked in Yemen. NOT FOUND.
   "Yemen" appears only in Table A.1 and Table B.1. The Yemen microdata DDI does show every mobile-money item as 100% system-missing.
5. The Findex database (source 28) metadata for the LIC aggregate says verbatim: "The World Bank's FY24 classification is used,
   where low-income economies had a 2022 Atlas GNI per capita of $1,135 or less." No page I found states a COUNT of economies in
   the LIC aggregate for the 2021 wave. NOT FOUND.
6. WDI BX.TRF.PWKR.CD.DT, Yemen: last non-null observation is 2016 = 3,770,584,000 current US$ (US$3,770.6 million). CONFIRMED.
   2017-2025 are null.

Contradictions or surprises against the stated expectations are in section "SURPRISES" at the end.

---------------------------------------------------------------------------------------------------

## TASK 1 - Microdata Library catalogue 5862 (YEM_2022_FINDEX_v01_M)

### 1.0 What the catalogue lists
URL: https://microdata.worldbank.org/catalog/5862  (and /data-dictionary).
- Title: "Global Financial Inclusion (Global Findex) Database 2021", "Yemen, Rep.", "2022 - 2023".
- Reference ID "YEM_2022_FINDEX_v01_M", DOI https://doi.org/10.48529/10py-nv58. Created and last modified Jun 08, 2023.
- Data file: micro_yem.dta, 1000 cases, 113 variables (data-dictionary page).
- DDI/XML: https://microdata.worldbank.org/metadata/export/5862/ddi. JSON: https://microdata.worldbank.org/metadata/export/5862/json.
- Documentation attached (https://microdata.worldbank.org/catalog/5862/related-materials):
  "2021 Global Findex Questionnaire" (PDF, /download/62139); "The Global Findex Database 2021" report (PDF, /download/62142);
  "Microdata Codebook" (PDF, /download/62140); "Microdata update details" (XLSX, /download/62141);
  "Micro 2021 Indicator Stata do-file" (DO, 8.06 KB, /download/62143).
  NOT OPENED, see "Leads not followed" below.

### 1.1 fin29_1 (catalogue variable V67)
URL: https://microdata.worldbank.org/catalog/5862/variable/F1/V67?name=fin29_1  (same content in the DDI, `<var ID="V67" name="fin29_1">`).

- Variable name: `fin29_1`.
- Label (page heading): "Received domestic remittances through an account (fin29_1)". DDI `<labl>`: "Received domestic remittances through an account".
- Overview as printed: "Valid: 393 / Invalid: 607 / Minimum: 1 / Maximum: 2 / Type: Discrete / Decimal: 0 / Width: 1 / Range: 1 - 2 / Format: Numeric".
- Question text, pre-question, universe, skip logic: the page has a heading "Questions and instructions" and nothing under it except the
  Categories table. The DDI has zero `<qstn>`, `<universe>`, `<preQTxt>`, `<qstnLit>`, `<postQTxt>`, `<ivuInstr>` and `<txt>` elements
  anywhere in the file, and no `<anlysUnit>`, `<derivation>` or `<drvdesc>`. NOT FOUND in the catalogue or DDI.
- Frequency table as printed (unweighted):

  | Value | Category | Cases | % as printed |
  |---|---|---|---|
  | 1 | yes | 39 | 9.9% |
  | 2 | no | 354 | 90.1% |
  | 3 | (dk) | 0 | 0% |
  | 4 | (ref) | 0 | 0% |
  | Sysmiss | | 607 | |

- Warning printed on the page: "Warning: these figures indicate the number of cases found in the data file. They cannot be
  interpreted as summary statistics of the population of interest."

### 1.2 Question text and skip logic (from the questionnaire PDF, not the DDI)
Source: "2021 Global Findex Questionnaire", https://microdata.worldbank.org/catalog/5862/download/62139 (file `questionnaire_globalfindex.pdf`,
21 pages, created 2022-11-18). PDF p11 = printed p11. This is the generic global instrument: "(your country)" is a placeholder and
there is no Yemen/Arabic version in the catalogue.

FIN28 (PDF p11):
> "In the PAST 12 MONTHS, have you, personally, RECEIVED MONEY from a relative or friend living in a different city or area INSIDE (your country) including any money you received in person? Yes or no? (INTERVIEWER: This can be money received for any reason except payments for goods and services)"
> "(If code 1 in FIN28, Continue; Otherwise, Skip to FIN30)"

FIN29_1 (PDF p11):
> "In the PAST 12 MONTHS, have you, personally, RECEIVED MONEY from a relative or friend living in a different city or area inside (your country) using a bank account or a mobile money account?"
> Codes: "Yes 1 / No 2 / (DK) 3 / (Refused) 4"
> "(If code 2-4 in FIN29_1, Continue; Otherwise, Skip to FIN30)"

FIN29C (PDF p11), asked of those who did not say yes at FIN29_1:
> "FIN29C1 You were handed cash by this person or by someone you know" and "FIN29C2 You received money through a money transfer service"

Wording point: FIN29_1 asks about "a bank account OR a mobile money account" in one item. It is not an account-only question.

Universe, as documented by the Microdata Codebook PDF (https://microdata.worldbank.org/catalog/5862/download/62140, file
`globalfindex2021_microdatacodebook.pdf`, 19 pages, created 2022-12-05), PDF p13 = printed p12:
> "fin29_1 | Received domestic remittances through an account | = 1 if the respondent received money from a relative or friend living in a different city or area inside the same country using a bank account or a mobile money account in the past year ... Note: Asked only of adults who received domestic remittances."
> "fin29c1 ... Note: Asked only of adults who received domestic remittances, but not through an account."

Consistency check against the Yemen counts: fin28 yes = 393 and fin29_1 valid = 393; fin29_1 no = 354 and fin29c1/fin29c2 valid = 354 each. So the observed skip pattern matches the documented logic. (This is my inference from counts, not a printed statement.)

### 1.3 The sibling remittance items (catalogue pages V62-V69, V109; all fetched and matched against the DDI)
URL pattern: https://microdata.worldbank.org/catalog/5862/variable/F1/{V}?name={name}

| Var | Name | Label (DDI) | Valid | yes | no | dk | ref | Sysmiss |
|---|---|---|---|---|---|---|---|---|
| V62 | fin26 | Sent domestic remittances | 1000 | 241 | 755 | 4 | 0 | 0 |
| V63 | fin27_1 | Sent domestic remittances through an account | 241 | 37 | 204 | 0 | 0 | 759 |
| V64 | fin27c1 | Sent domestic remittances in cash | 204 | 146 | 58 | 0 | 0 | 796 |
| V65 | fin27c2 | Sent domestic remittances through an MTO | 204 | 126 | 78 | 0 | 0 | 796 |
| V66 | fin28 | Received domestic remittances | 1000 | 393 | 606 | 1 | 0 | 0 |
| V67 | fin29_1 | Received domestic remittances through an account | 393 | 39 | 354 | 0 | 0 | 607 |
| V68 | fin29c1 | Received domestic remittances in cash | 354 | 280 | 74 | 0 | 0 | 646 |
| V69 | fin29c2 | Received domestic remittances through an MTO | 354 | 157 | 197 | 0 | 0 | 646 |

There are no fin29_2 or fin29_3 variables. The data dictionary lists V1-V113 and the only fin29 variables are fin29_1, fin29c1, fin29c2.

Derived variable V109 `remittances`, label "Made or received a domestic remittance payment", valid 1000: "sent/received through an account" 59; "sent/received through an otc transaction" 190; "sent/received in cash only" 185; "sent/received using other methods" 29; "did not send/receive" 532; "dk/ref" 5. Note printed: "This includes adults who made or received a domestic remittance payment in the past year."
So the Yemen microdata itself records 59 of 1,000 respondents (5.9% unweighted) as sending or receiving remittances through an account.

### 1.4 Does the DDI document how a published indicator is derived?
NO.
- The DDI has no derivation elements. Its only derivation-like text is the `notes` on V109 and V105 (e.g. "This includes adults who received a government transfer payment in the past year.").
- The Microdata Codebook PDF documents "Constructed Variables" (account_fin, account_mob, account, borrowed, saved, receive_*, merchantpay_dig, pay_utilities, remittances, anydigpayment) but nothing for the database indicators `fin28` / `fin29`.
- The Codebook (PDF p1) states: "'Don't know' and 'Refused to answer' are coded as 'no' in the Global Findex 2021 country-level database". This matters only for denominators. Here fin29_1 has 0 dk and 0 ref.
- The Microdata Library lists a "Micro 2021 Indicator Stata do-file" (download/62143) that probably shows the derivation. I did NOT open it; see "Leads not followed".

### 1.5 Other facts the DDI and codebook establish about Yemen (relevant to the zero)
a) Variables absent from the Yemen file that the generic codebook defines: `account_mob`, `fin10_1a-e`, `fin13_1a-f` (computed by comparing the codebook variable list with the DDI variable list). `account` and `account_fin` are both present and identical (0:no 801, 1:yes 199).
b) Mobile-money items present in the Yemen file but with zero valid responses ("Valid: 0, Invalid: 1000", range "*"): `fin13a`, `fin13b`, `fin13c`, `fin13d` (V38-V41), `fin17a1` (V53), `fin34b` (V79), `fin39b` (V86), `fin43b` (V92).
   Example: https://microdata.worldbank.org/catalog/5862/variable/F1/V38?name=fin13a and .../V79?name=fin34b.
   The fin34b blank is informative. In the questionnaire FIN34D (cash) is asked only if neither FIN34A nor FIN34B is yes (PDF p13). Yemen fin34d valid = 103 = fin34a "no" count (103). So FIN34B cannot have been asked-and-answered "no" for those people. The item looks not to have been collected. This is inference. Items 0-valid are consistent with "not asked" and, for fin13a-d only, also with "everyone answered no to the FIN13 gate question" (the gate FIN12/FIN13 is not a published variable). Caution applies.
c) Codebook Note1 (Codebook PDF p17, no printed number visible) lists the economies in which fin28, fin29_1, fin29c1, fin29c2 (and fin26, fin27_1, ...) "were only surveyed in": Afghanistan ... Zimbabwe. Yemen, Rep. is NOT in that list. Nor is any of the 16 economies collected in 2022. The codebook PDF was created 2022-12-05, before the May 2023 release that added the 2022 economies. The Yemen DDI nonetheless shows 1000 valid fin28 and 393 valid fin29_1 responses. I read the Note1 list as stale (not updated for the 2022 economies); that is my reading, not a World Bank statement.
d) DDI study-level facts: collection "2022-11-07" to "2023-01-09"; collMode "Face-to-face [f2f]"; "Sample size for Yemen, Rep. is 1000."; geogCover "Al Baydaa, Al Jawf, Mareb, Sadah, the Island of Socotra, and several districts in other governorates were excluded due to their small size, remoteness or security issues. The excluded areas represent approximately 23% of the population. In addition, due to the ongoing security situation, during field over one-fourth of the PSUs were replaced with a similar PSU in the same province."; "Data was collected in the following language(s): Arabic"; "Questionnaires are available on the website."

Confidence for Task 1: HIGH on the counts, labels and absence of question text; HIGH on the questionnaire wording; MEDIUM-HIGH that the generic questionnaire's skip logic is what Yemen used (the observed counts match it).

---------------------------------------------------------------------------------------------------

## TASK 2 - Published indicator `fin29` (source 28, Global Findex database)

Source: World Bank Indicators API, source 28 "Global Findex database" (lastupdated 2025-10-06).
- https://api.worldbank.org/v2/indicator/fin29?source=28&format=json
- https://api.worldbank.org/v2/sources/28/series/fin29/metadata?format=json
(The DataBank glossary page https://databank.worldbank.org/metadataglossary/global-financial-inclusion/series/fin29 returned only a "DataBank Error Page". https://www.worldbank.org/en/publication/globalfindex/Data returned a 403 login redirect. The API metadata is the same DataBank source metadata.)

### 2.1 Exact definition and universe
Indicator id `fin29`; name: "Received domestic remittances: into an account  (% age 15+)".
sourceNote / Longdefinition, verbatim:
> "The percentage of respondents who report personally receiving any money in the past year from a relative or friend living in a different area of their country, and received it into a bank or similar financial institution account or a mobile money account, (% age 15+)"

- Unit of measure: "Percent". Periodicity: "Triennial". License: CC BY-4.0.
- Universe: all respondents, "% age 15+". It is NOT "% of recipients".
- No derivation, rounding or "not asked" rule appears in the series metadata. The ten metatypes are Aggregationmethod, Dataset, IndicatorName, License_Type, License_URL, Longdefinition, Periodicity, Source, Topic, Unitofmeasure.
- Aggregation method (series metadata), verbatim: "Weighted Average: For aggregate data, each economy is classified according to the World Bank Group's fiscal year 2024, which runs from July 1, 2023, to June 30, 2024. The Russian Federation is excluded from the Europe and Central Asia (ECA) averages for all indicators, with the exception of account ownership (account.t.d), bank or similar financial institution account ownership (fiaccount.t.d), mobile phone ownership (con1), mobile money account use (mobileaccount.t.d), and internet use (internet)."

Naming trap: the API ids do not match the microdata variable names. API `fin28` = "Sent domestic remittances: using an account  (% age 15+)" (microdata `fin27_1`). API `fin29` = "Received ... into an account" (microdata `fin29_1`). Microdata `fin28` = "Received domestic remittances" (API `fh2`). Related API ids: `fh1` "Sent domestic remittances", `fh2` "Received domestic remittances" ("This includes any money received in-person").

2021-22 Methodology PDF, Appendix C glossary (PDF p25, printed p27, https://thedocs.worldbank.org/en/doc/fe026d04da1eb78f5ce8bb5e1529d60b-0430062023/original/Findex2021-22-Methodology.pdf) defines only the combined indicator:
> "Sent or received domestic remittances: using an account (%): The percentage of respondents who report personally sending or receiving any of their money in the past year to or from a relative or friend living in a different area of their country and who sent or received the money using a financial institution account or a mobile money account."
It has no separate "received into an account" entry. That is database-only.

### 2.2 Published Yemen values (API, source 28)
URLs: https://api.worldbank.org/v2/country/YEM/indicator/{id}?source=28&format=json&per_page=100

| Indicator | 2022 (Yemen's wave date) | 2021 | 2024 |
|---|---|---|---|
| fin29 Received domestic remittances: into an account | 0 (integer, raw JSON `"value":0`) | null | null |
| fin28 Sent domestic remittances: using an account | 0 (integer) | null | null |
| fh2 Received domestic remittances | 31.9313981068809 | null | null |
| fh1 Sent domestic remittances | 17.6714332248251 | null | null |
| account.t.d Account | 11.9033656433415 | null | null |
| mobileaccount.t.d Mobile money account | null | null | null |

All Yemen values sit under date "2022". The 2021 slot is null. 2017, 2014 and 2011 for fin29 are null; for account.t.d 2014 = 6.45 and 2011 = 3.66.
Table B.1 of the Methodology PDF prints Yemen account ownership as 12 (PDF p19, printed p21), consistent with 11.9.

### 2.3 Can the definition or derivation explain a published 0 given positive answers?
NO. State this plainly: the published definitions do not explain the difference.

- Definition and universe: numerator = respondents who received money AND received it into a bank/financial institution or mobile-money account; denominator = all adults 15+. Yemen has 39 such yes answers among 1,000 respondents (3.9% unweighted). Weights can scale this, but cannot take it to zero. For scale only: the published/unweighted ratios are fh2 31.9/39.3 = 0.81, fh1 17.7/24.1 = 0.73, account 11.9/19.9 = 0.60. Applied to 3.9% that would give roughly 2-3%. This is an illustration, not a computed value; the weights (`wgt`) were not accessed.
- The "% of recipients" reading would give 39/393 = 9.9% unweighted. That is not 0 either.
- Don't-know/refused coded as "no" (Codebook p1): irrelevant; Yemen has 0 dk and 0 ref on fin29_1.
- The published value is an integer 0, while every other non-null value in this series is a long float (e.g. 11.9033656433415).
- Cross-check with the other 15 economies collected in 2022 (API `?date=2022`, https://api.worldbank.org/v2/country/all/indicator/fin29?source=28&date=2022&format=json&per_page=500; DDIs at https://microdata.worldbank.org/metadata/export/{5847..5862}/ddi):

  | Economy (catalogue id) | published fin29 / fin28 (2022) | published fh2 | DDI fin29_1 yes / valid | DDI mobile-money items (fin13a valid) |
  |---|---|---|---|---|
  | Azerbaijan (5847) | 0 / 0 | 16.48 | 97 / 182 | 0 valid; no `account_mob` variable |
  | Yemen (5862) | 0 / 0 | 31.93 | 39 / 393 | 0 valid; no `account_mob` variable |
  | Botswana (5848) | 21.97 / 20.67 | 31.88 | 307 / 405 | 414 valid |
  | Chad (5849) | 10.46 / 9.63 | 24.68 | 141 / 273 | 107 valid |
  | Comoros (5850) | 7.62 / 3.47 | 21.12 | 87 / 246 | 68 valid |
  | Ethiopia (5853) | 5.80 / 5.81 | 13.08 | 79 / 161 | 43 valid |
  | Mexico (5859) | 10.33 / 8.87 | 16.15 | 79 / 144 | 120 valid |
  | other 9 economies (Congo Dem. Rep., Eswatini, Gambia, Guatemala, Lesotho, Madagascar, Mauritania, Niger, Vietnam) | all positive | all positive | valid counts present | fin13a valid (28 to 557) in all |

  (The DDIs of Congo Dem. Rep., Guatemala, Niger and Vietnam print no category frequencies for fin29_1, only valid counts: 392, 116, 276 and 184. Their published fin29 is positive: 16.13, 4.23, 4.91, 12.30.)
  Only Azerbaijan and Yemen have the zero. The zero is not generated by the "% age 15+" definition. It coincides with the absence of mobile-money items in the microdata. Azerbaijan has 97 yes of 182 recipients (53%) and still a published 0.

Interpretation (INFERENCE, not stated by the World Bank): the database computation of `fin29` appears to depend on a mobile-money-based constructed variable or on a per-economy indicator mapping that is empty for Yemen and Azerbaijan, so a missing component was set to 0 instead of missing. The public pages I could read do not document this. The 2025 Findex site lists a file "Indicator mapping by economy" (xlsx) and the microdata catalogue lists the indicator do-file; either might confirm it. See "Leads not followed".

Confidence for Task 2: HIGH on definition, universe and the published 0; HIGH that the definition does not explain a 0; MEDIUM on the artefact interpretation (it is the best-fitting inference, with Azerbaijan as the corroborating case).

---------------------------------------------------------------------------------------------------

## TASK 3 - 2021-22 Survey Methodology PDF

File: https://thedocs.worldbank.org/en/doc/fe026d04da1eb78f5ce8bb5e1529d60b-0430062023/original/Findex2021-22-Methodology.pdf
(27 pages, created 2023-04-17).

### 3.1 Yemen's Table A.1 row
PDF p15 (printed p17; the footer reads "Survey Methodology 17"). Table A.1 title: "Details of survey methodology for economies included in the Global Findex 2021 survey and database". Row as extracted, verbatim cell text:

- Economy: "Yemen, Rep e" (footnote e)
- Region: "MENA"
- Income group: "Low"
- Data collection date: "Nov 7, 2022–Jan 10, 2023"
- Number of interviews: "1,000"
- Design effect: "1.9"
- Margin of error: "4.3"
- Mode of interview: "Face-to-face (HH)d"
- Languages: "Arabic"
- Exclusions and other sampling details: "Al Baydaa, Al Jawf, Mareb, Sadah, the Island of Socotra, and several districts in other governorates were excluded due to their small size, remoteness or security issues. The excluded areas represent approximately 23% of the population. In addition, due to the ongoing security situation, during field over one-fourth of the PSUs were replaced with a similar PSU in the same province."

Footnotes printed under the table (same PDF p15, printed p17):
> "b. The design effect calculation reflects the weights and does not incorporate the intraclass correlation coefficients because they vary by question. Design effect calculation: n*(sum of squared weights)/[(sum of weights)*(sum of weights)]."
> "c. The margin of error is calculated around a proportion at the 95 percent confidence level. The maximum margin of error was calculated assuming a reported percentage of 50 percent and takes into account the design effect. Margin of error calculation: √(0.25/N)*1.96*√(DE). ..."
> "d. Hand-held (HH) data collection."
> "e. In these countries, data collection took place in 2022 due to COVID-19 related issues that restricted earlier access."

Note b is a general calculation note. It is not Yemen-specific. The PDF does not state which income-classification vintage "Low" refers to.

Date discrepancy: Table A.1 says the fieldwork ended "Jan 10, 2023". The catalogue DDI says `<collDate date="2023-01-09" event="end"/>`. Start date agrees (Nov 7, 2022).

Yemen also appears in Table B.1 (PDF p19, printed p21): "Yemen b | 12 | 5 | 7" (adults / women / poor adults with an account, %), with footnote b "In these countries, data collection took place in 2022 due to COVID-19 related issues that restricted earlier access."

### 3.2 Search for "mobile-money questions not asked in Yemen"
Searched the whole extracted text for "Yemen", "mobile", "module", "not asked", "not ask", "were not", "was not", "omitted", "not included", "not collected", "not surveyed", "not available", "skipped", "only in", "only asked".
- "Yemen" occurs only in Table A.1 (PDF p15) and Table B.1 (PDF p19).
- "mobile" occurs in (i) Mode-of-interview and sampling text (mobile phone/landline sampling) and (ii) the Appendix C glossary definitions and footnote 2 (mobile money account = GSMA MMU services). None mentions Yemen.
- Nothing says mobile-money questions or modules were not asked in Yemen or in any 2022 economy.
- The only "not available" hit is: "Note: Data for all indicators are available at http://www.worldbank.org/globalfindex." (Table B.1 note).
RESULT: NOT FOUND (searched: full text of all 27 pages for the terms above).

What the public pages do show on this point: the Yemen DDI has fin13a-d, fin17a1, fin34b, fin39b, fin43b all system-missing (1000 of 1000), and no `account_mob` variable (see 1.5). That is evidence in the microdata documentation, not a statement in the methodology PDF.

Confidence for Task 3: HIGH (full-text search of a short PDF).

---------------------------------------------------------------------------------------------------

## TASK 4 - Low-income (LIC) aggregate

### 4.1 Classification used by the Findex database (source 28)
URL: https://api.worldbank.org/v2/sources/28/country/LIC/series/account.t.d/metadata?format=json
Country concept "LIC", metatype SpecialNotes, verbatim:
> "The World Bank's FY24 classification is used, where low-income economies had a 2022 Atlas GNI per capita of $1,135 or less. Historical member composition is available at https://datacatalog.worldbank.org/int/search/dataset/0037712/World-Development-Indicators."

Also from the same metadata (LongName "Low income", ShortName "Low income", 2-alphacode "XM") and from the series metadata for fin29 (quoted in 2.1): "each economy is classified according to the World Bank Group's fiscal year 2024, which runs from July 1, 2023, to June 30, 2024."
Yemen's own record in source 28 (https://api.worldbank.org/v2/sources/28/country/YEM/series/fin29/metadata?format=json): "IncomeGroup" = "Low income (FY24)".

The aggregate is published under date "2021" for the 2021 wave (e.g. LIC account.t.d 2021 = 35.18; fin29 2021 = 12.85; fh2 2021 = 27.18). The LIC 2022 slot is null, so the 2022-collected economies are not given their own aggregate. The pages do not say whether Yemen's 2022 data are in the LIC 2021 figure. (If they are, Yemen's published 0 would be inside the LIC fin29 average of 12.85. I cannot tell from public pages.)

### 4.2 Other classification statements (they differ in vintage)
- 2021 report (https://microdata.worldbank.org/catalog/5862/download/62142, PDF p17, printed p. xv): "Income group classifications reflect the World Bank income group classifications from 2020." Regional averages "include only developing economies (low- and middle-income economies as classified by the World Bank)."
- Microdata Codebook (PDF p2, printed p1), `regionwb`: "Note: High income based on GNI per capita data from 2020."
- 2021-22 Methodology Table A.1: has an "Income group" column ("Low" for Yemen) but states no classification year (searched "Atlas", "1,135", "FY2", "classif", "income group": only the column header).
So three vintages are in play: 2020 classification (2021 report, microdata codebook), unstated (Methodology Table A.1), FY24 (database aggregates, July 2023 to June 2024; Atlas threshold $1,135).

### 4.3 COUNT of economies in the LIC aggregate for the 2021 wave
NOT FOUND (searched: API country record for LIC, source-28 metadata for LIC and fin29/account.t.d series, the 2021 report text for "N low-income economies" patterns, the Methodology PDF, the 2025 Survey-methodology PDF, the Findex 2025 landing, download-data and methodology pages). The only pointer is the external WDI "historical member composition" catalogue page named in the SpecialNotes; its page is a very large JavaScript catalogue record and I did not extract a count from it.
Derived count, for information only, NOT a World Bank statement: Table A.1 of the Methodology PDF shows 18 economies with income group "Low": Afghanistan, Burkina Faso, Chad, Congo (Dem. Rep.), Ethiopia, Gambia, Guinea, Liberia, Madagascar, Malawi, Mali, Mozambique, Niger, Sierra Leone, South Sudan, Togo, Uganda, Yemen. Its vintage is unstated and probably differs from FY24. Do not publish a count of LIC economies "in the aggregate" from this.

Confidence for Task 4: HIGH on the quoted FY24 wording; HIGH that no count is stated on the surfaces searched (MEDIUM-HIGH overall, because DataBank's own glossary page could not be loaded).

---------------------------------------------------------------------------------------------------

## TASK 5 - WDI personal remittances received, Yemen

URL: https://api.worldbank.org/v2/country/YEM/indicator/BX.TRF.PWKR.CD.DT?format=json&per_page=100 (source id 2, lastupdated 2026-10-08; 66 rows, 27 non-null).
Indicator name: "Personal remittances, received (current US$)". Source organisation: "IMF balance of payments data, International Monetary Fund (IMF); Staff estimates, World Bank (WB)".

- Last non-null observation: 2016 = 3770584000 (US$3,770.6 million). CONFIRMED.
- 2017 to 2025: all null.
- Earlier values (for context): 2015 = 3350500000; 2014 = 3350500000 (identical to 2015 as returned); 2013 = 3342500000; 2012 = 3351000000; 2011 = 1403920000; earliest non-null 1990 = 1498199951.
- Yemen metadata (source 28 country record): "BalanceofPaymentsManualinuse" = "BPM5 (Converted into BPM6 by IMF)"; "Latesttradedata" = "2015".

Confidence: HIGH.

---------------------------------------------------------------------------------------------------

## SURPRISES (things that differ from, or add to, the stated expectations)

1. fin29_1 counts (393 asked / 39 yes) are exactly as expected.
2. The published fin29 is keyed to date "2022" for Yemen, not "2021". The 2021 slot is null.
3. The published API ids and microdata variable names collide: API `fin28` = SENT via account; microdata `fin28` = RECEIVED (any channel). Quoting "fin28" without saying which source will mislead.
4. The microdata codebook's "only surveyed in" list (Note1) omits Yemen and all 2022 economies, yet Yemen has valid responses. Treat Note1 as stale, not as evidence that the items were not asked.
5. The zero is not unique to Yemen: Azerbaijan has the same integer 0 for fin28 and fin29 with 97 of 182 recipients saying yes. That strongly suggests a database artefact tied to missing mobile-money data, not a genuine zero.
6. The Methodology PDF is silent on mobile-money coverage in Yemen (NOT FOUND), but the DDI shows the mobile-money items empty.
7. Fieldwork end date: DDI "2023-01-09" vs Methodology Table A.1 "Jan 10, 2023".
8. Three different income-classification vintages appear across World Bank surfaces (2020, unstated, FY24).
9. The catalogue's 1,000-case file is described as unweighted in the page warning; all percentages above from the DDI are unweighted and are NOT population estimates.

## Leads not followed (rule: read only catalogue/DDI web pages and published PDFs)
- Stata do-file "Micro 2021 Indicator Stata do-file": https://microdata.worldbank.org/catalog/5862/download/62143 (8 KB). Probably documents how `fin29`/`fin28` are derived. A code file, not respondent data, but outside the permitted file types, so not opened.
- XLSX "Microdata update details": https://microdata.worldbank.org/catalog/5862/download/62141 - may list changes for the added 2022 economies.
- XLSX "Indicator mapping by economy" (Findex 2025 methodology page): https://thedocs.worldbank.org/en/doc/be6615202d1f08a25855c8ac2d615122-0050012025/related/indicator-mapping-by-economy.xlsx - may state which indicators are available per economy (possibly 2024 wave only).
- XLSX glossary https://thedocs.worldbank.org/en/doc/be6615202d1f08a25855c8ac2d615122-0050012025/related/GlobalFindex2025-glossary.xlsx.
- Country-level data files (.csv/.dta/.xlsx) on https://www.worldbank.org/en/publication/globalfindex/download-data were not downloaded.
- Respondent weights (`wgt`) would be needed to compute the weighted `fin29_1` share. Not accessible under the rules.
