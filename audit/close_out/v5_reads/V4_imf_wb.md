# V4 verification: IMF CR 26/80, World Bank FSD 2024, Enterprise Surveys Yemen 2013, Doing Business 2020 Yemen

Read-only with respect to <repository> (the repo was only grepped, to see what "1.838" refers to there).
Downloads: `<session scratchpad>/v5/dl/V4/` (PDFs, `*.txt` from `pdftotext -layout`, `fig/` PNG renders). All text analysis ran under `python3 -I`.
Page convention below: "PDF p." = page index in the file; "printed" = number printed on the page.

## Files fetched

| Doc | URL | HTTP | Bytes | SHA-256 | Pages |
|---|---|---|---|---|---|
| A. IMF CR 26/80 | https://www.imf.org/-/media/files/publications/cr/2026/english/1yemea2026001-source-pdf.pdf | 200 (see note) | 2,432,886 | 01af28f0d96cd635c3b39520ee98cd32b4936bcee92f667a9b84d7abf016507e | 92 |
| B. WB Yemen Financial Sector Diagnostics | https://documents1.worldbank.org/curated/en/099102324070011985/pdf/P177631-d18a7ee4-3fcf-4393-9665-77f98b3e43a7.pdf | 200 | 9,941,078 | b245520c91d3891bf1d742521a341d6a296ca57afefb2bd36cd74198d0e0f682 | 152 (153 text pages incl. trailing form feed) |
| C. WBES Yemen 2013 profile | https://www.enterprisesurveys.org/content/dam/enterprisesurveys/documents/country/Yemen-2013.pdf | 200 | 675,445 | 7ebd74a35be9e99813035c8af51ebd568562230f14cc61f66b435d909c1f8beb | 15 |
| D. Doing Business 2020 Yemen | https://www.doingbusiness.org/content/dam/doingBusiness/country/y/yemen/YEM.pdf | 200 | 1,801,736 | 7c9e4ba60891e279ca57167e1a969e3321472bef113a1599fad420269beac375 | 63 |

- Note on A: the first request, sent with a Chrome User-Agent, got `403 Access Denied` (Akamai). Retried with `-A "curl/8.5.0"`, it returned the PDF (200), and a later plain `curl` with no User-Agent also returned 200. Treat the 403 as UA-dependent or transient.
- D: the original URL works. No archived copy was needed.
- A metadata: title "Republic of Yemen: 2025 Article IV Consultation-Press Release; Staff Report; and Statement by the Executive Director for Republic of Yemen; IMF Country Report No. 26/80; November 20, 2025". The file also holds a Staff Report supplement dated March 18, 2026 (PDF p.79 onward).
- B: title page "YEMEN FINANCIAL SECTOR DIAGNOSTICS, April 5, 2024"; PDF creation date 22 Oct 2024. In this file the printed page number equals the PDF page index (checked on pp. 16, 139, 148, 151).

---

## A. IMF Country Report No. 26/80

### A1. Annex IV para 2: CONFIRMED, at PDF p.46, printed p.41

Annex IV starts at PDF p.45 (printed p.40): "Annex IV. Statistical Enhancements with the Resumption of the 2025 Article IV Consultation with Yemen". The same page defines the acronym: "...has enabled the internationally recognized government (IRG) to gather macroeconomic data..."

Verbatim, PDF p.46 / printed p.41 (line breaks flattened; I read the rendered page as well):

> 2. External Sector. The external sector data was compiled using multiple sources and estimation techniques to overcome significant data limitations and complexities. To disaggregate between IRG and non-IRG controlled regions, the mission applied the population ratio, allocating 33 percent² to the IRG controlled areas. Virtual engagements with CBY over September 2024–April 2025 followed by an in-person offsite TA mission (July 20–31) supported compilation efforts and enhanced accuracy.
>
> • Trade. For 2014–24, export and import estimates relied primarily on the UN Comtrade database, while non-oil imports reported by partner countries (recorded as Yemen's exports) were adjusted downward by 15 percent to convert CIF to FOB values. Oil export data was drawn from the Ministry of Oil. For the disaggregation between IRG and non-IRG controlled regions, export and import data reported by the IRG was used and temporary imports were excluded.
>
> • Personal transfers. Estimating personal transfers was particularly challenging given limited data and the role of informal channels; thus, a demographic and behavioral model—based on the number of Yemenis abroad, family size, and average transfer amounts— as well as the ratio of 33percent to the IRG controlled areas was applied.
>
> • Grants. Official grants from Saudi Arabia and the UAE, key for current transfers, were compiled using publicly announced disbursements, budget support records, and data from the CBY and the Ministry of Finance, with all grants allocated to the IRG. SWIFT-scope transactions—both incoming and outgoing were used to estimate some balance of payments components such as humanitarian grants, services, earned income, and some financial account transactions. [...]

Footnote 2 (same page): "As proposed by the authorities."

Checks against the expectations:
- 33% population ratio for IRG areas: CONFIRMED. The text says "the population ratio, allocating 33 percent". The Personal transfers bullet repeats it as "the ratio of 33percent" (the missing space is in the original).
- "As proposed by the authorities": CONFIRMED. It is footnote 2, and the superscript sits on "33 percent" in the lead sentence. It qualifies the 33 figure only, not the whole method.
- Trade from government-reported data: PARTLY DIFFERENT. Trade estimates "relied primarily on the UN Comtrade database", with oil exports from the Ministry of Oil. IRG-reported export and import data is used only "for the disaggregation between IRG and non-IRG controlled regions", and temporary imports are excluded. The same Annex says the same data differently on PDF p.45 (printed p.40, para 1, Real Sector): "External trade estimates for the IRG-controlled region were estimated from UN Comtrade mirror data". PDF p.52 (Annex VII, printed p.47 by sequence; the footer is not in the text layer) adds: "External trade data for IRG-controlled areas have been received from customs authorities since 2022."
- Official grants allocated wholly to the government: CONFIRMED, with a scope limit. "with all grants allocated to the IRG" comes at the end of the sentence on official grants from Saudi Arabia and the UAE. The next sentence says humanitarian grants and some other components were estimated from SWIFT-scope transactions, and no allocation rule is given for those.
- Demographic and behavioural model for remittances: CONFIRMED. The Annex calls the item "Personal transfers"; the tables call it "Remittances". Inputs named: number of Yemenis abroad, family size, average transfer amounts. It says "limited data and the role of informal channels".

### A2. Where "1.838" appears: NOT FOUND in the IMF report

NOT FOUND (searched the full text, layout and raw `pdftotext` modes, for `1.838`, `1,838`, `1838`, `838`, `1.84`; zero hits for `1.838` in either mode; the other near-matches are unrelated table cells such as 1.8 and 1,818 (an exchange rate)). It is not printed anywhere in CR 26/80.

What it is, from the repo (read-only grep of `site-src/content/page_specs.json`, `dist/en/evidence/CLM-042/index.html`): a ratio computed by the evidence site, "the ratio of the CBY-Aden level to the IMF level is 1.838 in every year" over 2021-2024, i.e. CBY-Aden Annual Report 2025 remittances divided by the IMF Article IV remittances series. It is derived, not published by the IMF. The CBY-Aden side is not among the four documents I was asked to read, so I did not verify that numerator.

Series the denominator would come from (IMF Table 4, "Yemen: External Sector, 2018–2030, (In millions of U.S. dollars)", PDF p.36 / printed p.31; "Remittances" row): 2018 1329.2; 2019 1408.4; 2020 1491.1; 2021 1577.7; 2022 1668.2; 2023 1762.8; 2024 1861.7 (in the header the six labels "Est. Proj. Proj. Proj. Proj. Proj." sit over 2025-2030, so 2025 is "Est." and 2026-2030 "Proj."; 2018-2024 carry no label). Table 1 (PDF p.32 / printed p.27) shows the same values rounded (1,578; 1,668; 1,763; 1,862). The 2018-2024 values are identical in the press-release Table 1 (PDF p.5), the staff-report Table 1 and the supplement Table 2 (PDF p.86, printed p.8 of the supplement). Only 2025 onward differs between vintages: remittances 2025 = 1,973.4 in Table 4 and 1,977 in the PDF p.5 and p.86 tables.

### A3. Whole-of-Yemen total for remittances or the external sector: NOT FOUND

NOT FOUND (searched for "whole of Yemen", "all of Yemen", "non-IRG", "entire", "nationwide", "Sana", "CBY-Sana", "disaggregat", and every "remittance" and "personal transfer" mention, 26 pages). No table or sentence gives a whole-of-Yemen remittances or balance-of-payments total, and there is no non-IRG column.

The scope evidence that exists:
- Table 4 note, PDF p.36 / printed p.31: "Note: GDP in current prices is IRG estimate based on the production approach." Table 1 rows (PDF p.5, p.32, p.86): "Population (IRG, in millions)".
- Annex IV (above): a demographic and behavioural model "as well as the ratio of 33percent to the IRG controlled areas was applied". The report never labels the Table 4 "Remittances" row itself as IRG-only; the IRG scope is implied by this method text and the GDP note, not stated on the row. I would not call the row "IRG remittances" in quotation marks; say "the series the IMF publishes, which its Annex IV method places on an IRG-area basis".
- DSA annex, PDF p.64 (printed p.5 of the annex): "The macro framework is focused on the territory under effective control of Yemen's IRG, in line with the 2025 Article IV consultation. The IRG controls approximately two thirds of Yemen's territory." and (para 8) "Surveillance in 2025 focuses on the territories controlled by the IRG while coverage in 2014 included the entire territory."
- The only whole-Yemen conversion in the report concerns debt, not remittances. PDF p.20 / printed p.15, footnote 9: "Expressed as a share of GDP estimates for IRG-controlled areas. These figures represent 62 and 35 percent of the whole Yemen's GDP, though the latter estimates remain highly uncertain." It hangs on "By July 2025, Yemen's IRG had accrued debt totaling 135 percent of GDP, which includes 90 percent of external debt inherited from the time before the conflict."
- Related "whole of Yemen" mentions that are not about the external sector: footnote 6, PDF p.15 / printed p.10, "Data encompasses all of Yemen" (attached to the USAID assistance figure); ODC balance sheets "covers the whole of Yemen while the CBY data covers the IRG controlled region" (PDF p.47 / printed p.42, Monetary Sector); CPI "covers whole of Yemen and would need to be bifurcated between IRG and non-IRG" (PDF p.49 / printed p.44).
- Any whole-Yemen remittances figure (for example dividing by 0.33) would be the site's own arithmetic. The IMF does not publish one.

---

## B. World Bank, Yemen Financial Sector Diagnostics (April 2024)

### B1. Yemen Post / postal authority: CONFIRMED, PDF p.16, printed p.16 (Executive Summary)

Verbatim:

> The main financial players operating in Yemen are banks and money exchangers. Insurance companies, pension funds, and other traditional intermediaries play only a marginal role, though the Yemen Post and Postal Savings Authority (YPPSA) and Postal Savings Fund (PSF) provide payment services, savings accounts, and other financial products.

Other mentions (searched "Post", "postal", "YPPSA", "PSF", "post office" on all pages):
- PDF p.12 (Abbreviations): "PSF Postal Savings Fund"; "YPPSA Yemen Post and Postal Savings Authority".
- PDF p.116 / printed p.116 (Box 10, civil-service pay): "Salary payments are no longer made to accounts held by employees in commercial banks and are either paid in cash via a teller at the spending unit, over the counter at an exchange house, or at the post office."
- No dedicated section, no customer or account counts, no volumes for the post. Hits on p.10 and p.150 are "Post-Conflict" only.
- Difference from a simple reading: the sentence names two bodies, YPPSA and PSF, and gives no figures. It does not say the post is large; it sits in a "though" clause under a statement that these intermediaries play "only a marginal role".

### B2. Annex III, Figures 114-116 (2022 informal-firm survey): PDF p.151, printed p.151

Annex III starts PDF p.139 (TOC p.5 also says 139). I rendered p.151 (and p.148, 141, 120) and read the labels from the images.

**Base: 217 informal firms: CONFIRMED.** p.139: "The enterprise survey was collected towards the end of 2022 and consists of 328 formal and 217 informal enterprises or businesses." "Data was collected in September 2022." p.140: "Out of the 328 formal firms and 217 informal firms, most were in Amanat al Asimah and in areas under Houthi control (Figure 100)." Figure 101 (PDF p.141, read from the render): informal = 38 in IRG areas + 179 in Houthi areas = 217; formal = 164 + 164 = 328.
- The figures on p.151 do not print their own "n". I checked each bar as a count over 217 and every value is an exact whole count over 217 (for example 18.43 = 40/217; 54.38 = 118/217; 47.00 = 102/217; 22.12 = 48/217; 1.84 = 4/217; 2.76 = 6/217; 49.8 = 108/217 = 49.77, 50.2 = 109/217). So the base of Figures 114-116 is all 217 informal firms. That is arithmetic inference; the report does not state it.

**Figure 114 "Ownership of Bank Account"**: Have a bank account 18.43; No bank account 80.18; I do not know 1.38.

**Figure 115 "Owner has Loan or Debt Related to Business"**: Have a loan or debt related to business 49.8; No loan or debt related to business 50.2. EXPECTED 49.8% CONFIRMED. Text under it (p.151): "Fifty percent of the informal establishments interviewed said they have a loan or a debt."

**Figure 116 "Main Sources of Financing for the Business"**, labels read from the render, left to right:

| Label on chart | Value (%) |
|---|---|
| (Money lenders) | 22.12 |
| (Relatives) | 47.00 |
| (Savings) | 54.38 |
| (Microfinance institute) | 1.84 |
| (Retained earnings) | 8.29 |
| (buying goods on credit) | 2.76 |
| (No need for finance) | 0.46 |

Expected values CONFIRMED: savings 54.4 (54.38), relatives 47.0 (47.00), money lenders 22.1 (22.12), microfinance 1.8 (1.84), buying goods on credit 2.8 (2.76).

Text on p.151 (verbatim): "Using personal savings scored the highest in the informal sector with 54.38% saying that their main source of financing for their business activities. Loans from relatives or money lenders rated second and third which reflect the informal trust network among the Yemenis." And: "Fifty percent of the informal establishments interviewed said they have a loan or a debt. Predicting from the bar chart above, their loans are probably from informal lenders such as friends and lenders as only 2% of the respondents said they have loans from a microfinance institute."

Differences and cautions:
1. **Figure 116 is not "sources of debt".** Its title is "Main Sources of Financing for the Business" and its categories include savings, retained earnings and "No need for finance". Its base is all 217 firms (see above), not the 108 or so owners who report a loan or debt (savings alone is 118 firms). The report's own sentence that "their loans are probably from informal lenders" is the author's inference ("Predicting from the bar chart above ... probably"), not a survey result.
2. **Multiple answers: apparently yes, but never stated.** The seven values sum to 136.85 percent, so the question cannot have been single-choice, although the caption and text say "main source". No sentence in Annex III says "multiple answers" for this question (the only "multiple option" wording is for the financial-intermediary question, PDF p.147). Do not write "multiple answers allowed" as a report statement. Write "values sum to 136.85%, so respondents evidently gave more than one answer".
3. **The report's main text gives different numbers for the same survey.** Figure 91, PDF p.120 / printed p.120, "Sources of Financing among Informal Firms in Yemen, 2022": Savings 40%, Relatives 34%, Money lenders 16%, MFIs 1%, Other 8%. Text on p.118: "Informal firms mainly rely on their own savings and loans from relatives to meet their financing needs, but 16 percent use informal money lenders, and 1.3 percent access microfinance institutions (Figure 91)." Text on p.108: "just 1.3 percent of informal firms reported working with a microfinance institution". These match Figure 116 re-expressed as shares of the 136.85 total (54.38 -> 39.7; 47.00 -> 34.3; 22.12 -> 16.2; 1.84 -> 1.3; 8.29 + 2.76 + 0.46 = 11.51 -> 8.4). That re-scaling is my inference; the report does not say so. So "1.3% MFI" (body text, share of mentions) and "1.84% MFI" (Annex, share of firms) are not the same measure, and "2%" appears in the Annex text. Any public sentence has to say which one it uses.
4. Bank-account share: the body says "just 18 percent of informal firms had a bank account" (PDF p.103 and p.150); Figure 114 shows 18.43.

**How the sample was drawn.** Seven governorates were chosen "in consultation with local partners ... due to their economic significance and private sector dynamism. These are Aden, Amanat Al Asimah, Al Hudaydah, Taizz, Hadramaut, Marib, and Ibb." (PDF p.139). Informal sector, PDF p.140, verbatim:

> All enterprises that are not legally registered nor have any type of licensing from the authorities are identified as informal enterprises. As informal enterprises are not registered, sampling from an existing list was not possible. Instead, in consultation with the local partner, 30 types of activities were identified as the main operating fields for informal enterprises. The survey team visited the main market areas within each governorate (2-4 per governorate), and after scanning the area and speaking with key interlocuters, a list of informal businesses was developed. Once enough businesses for each of the main economic activities were identified, the team randomly sampled businesses per economic activity and interviewed the first business owner that consented.
>
> A quota of enterprises for each governorate, as well as the main activities within each governorate, was determined ahead of time, and fieldworkers attempted to reach this quota as much as possible.

Also: "Face-to-face interviews were conducted with the owner or manager of the enterprise..." (p.139). p.140: "13 out of the total businesses were in rural areas, eight from the formal sector and five from the informal sector. However, this likely reflects the sampling approach described in the previous section." The informal sample is 38 IRG vs 179 Houthi-area firms (Figure 101, p.141). It is a quota-based, market-area, first-consenting-owner sample in seven chosen governorates, not a national probability sample. It states no weights.

### B3. Formal-firm comparison (supplier credit 1.31%): value CONFIRMED; labelling needs care

- Where: **Figure 110 "Sources of Working Capital", PDF p.148, printed p.148** (render checked). Bars: Internal funds or retained earnings 69.12; borrowed from banks: private or state-owned 0.56; borrowed from nonbank financial institution 1.97; **purchased on credit from suppliers 1.31**; Advanced payments by clients 10.15; others, money lenders, friends, relatives 16.66. They sum to 99.77, so they are shares of working capital, not multi-answer percentages.
- Figure 111 (same page, same title) splits by control area, labelled "IRG (average)" and "Houthi (average)". Supplier credit is 1.55 (IRG) and 1.07 (Houthi). 1.31 equals their simple mean (the other five bars also equal the mean of the two area values, to rounding), which fits equal 164/164 area samples.
- Text on the preceding page, PDF p.147 (verbatim): "Most of the establishments reported that they rely on their internal funds or retained earnings to finance their investments. The bar chart below shows 69% (on average) spent from internal funds and retained earnings while second source of funding 17% (on average) comes as loans from informal channels such as money lenders, friends, and relatives."
- What is NOT in the report: Figure 110 does not use the word "formal" and prints no "n". It is placed under the section heading "ACCESS TO FINANCE OF FORMAL ENTERPRISES" (PDF p.142, printed p.142), which runs until the "Access to Finance of informal Enterprises" heading on p.150. So "328 formal firms" comes from p.139 (sample size) and the section placement, plus Figure 101 (164 + 164). The words "average share of working capital" are a fair reading of the title plus "(on average)", not a quoted definition. Safe wording: "Figure 110 (Annex III, formal-enterprise section): on average 1.31% of working capital was purchased on credit from suppliers."
- Note the p.147 text describes the 69% and 17% as sources "to finance their investments" while the figure is titled "Sources of Working Capital".

---

## C. World Bank Enterprise Surveys, Yemen Country Profile 2013

**Answer: 281.5 is the Yemen all-firms value. 284.3 is the Medium Firms column.** Row on PDF p.13, printed p.13 ("Summary of Enterprise Survey Indicators", Finance Indicators block; checked on the rendered page):

> Value of Collateral Needed for a Loan (% of the Loan Amount)    281.5    287.3    284.3    193.2    188.9    196.3

Column headers (same table): Yemen | Small Firms (1-19 Employees) | Medium Firms (20-99 Employees) | Large Firms (100+ Employees) | Middle East & North Africa | Lower middle income.

| Column | Value (% of loan amount) |
|---|---|
| Yemen | 281.5 |
| Small Firms (1-19) | 287.3 |
| Medium Firms (20-99) | 284.3 |
| Large Firms (100+) | 193.2 |
| Middle East & North Africa | 188.9 |
| Lower middle income | 196.3 |

Neighbouring rows (same page, same columns): "% of Firms With Bank Loans/line of Credit" 4.7 | 1.9 | 25.3 | 11.8 | 19.8 | 34.7; "Working Capital External Financing (%)" 9.5 | 8.7 | 15.7 | 12.1 | 19.1 | 27.0. This is the only place "collateral" appears with a value (the p.11 intro says "collateral levels relative to the value of the loans"). The cover (PDF p.1) reads "Yemen Country Profile 2013"; footer "Enterprise Surveys: YEMEN - 2013". PDF created 7 Jan 2015. This is a 2013 survey, so it predates the 2015 conflict.

---

## D. World Bank Doing Business 2020, Yemen economy profile

**Working URL: https://www.doingbusiness.org/content/dam/doingBusiness/country/y/yemen/YEM.pdf** (HTTP 200 on the original path, with and without a User-Agent; no archive copy needed). PDF created 23 Oct 2019; title page "Doing Business 2020 / Yemen, Rep. / Economy Profile". The "Page N" footer equals the PDF page index.

All four expectations CONFIRMED.

1. Public credit registry coverage 1.3% of adults; 216,245 individuals and firms: **PDF p.30, printed "Page 30"**, "Details – Credit Information in Yemen, Rep.", table "Coverage":

> Coverage | Credit bureau | Credit registry
> Number of individuals | 0 | 211,476
> Number of firms | 0 | 4,769
> Total | 0 | 216,245
> Percentage of adult population | 0.0 | 1.3

So 216,245 = 211,476 individuals + 4,769 firms. Also on p.27 ("Getting Credit - Yemen, Rep."): "Credit registry coverage (% of adults) 1.3 | 15.8 | 24.4 | 100.0 (2 Economies)" (Yemen | Middle East & North Africa | OECD high income | Best Regulatory Performance); and on the p.4 summary: "Credit registry coverage (% of adults) 1.3".
2. Private credit bureau coverage 0%: p.30 "Credit bureau | 0 individuals | 0 firms | Total 0 | Percentage of adult population 0.0". p.27: "Credit bureau coverage (% of adults) 0.0 | 16.3 | 66.7 | 100.0 (14 Economies)". p.4: "Credit bureau coverage (% of adults) 0.0".
3. Data-collection date: **PDF p.26 ("Getting Credit")**: "This topic explores two sets of issues—the strength of credit reporting systems and the effectiveness of collateral and bankruptcy laws in facilitating lending. The most recent round of data collection for the project was completed in May 2019." (The same sentence is repeated on each topic page.)
4. City covered: **"City Covered Sanaa"** (PDF p.4, summary page; also the header of other topic tables such as p.6). The spelling is "Sanaa", not "Sana'a". The Getting Credit pages themselves (p.26 to p.30) do not print the city. p.26 says only that the case company "has its headquarters and only base of operations in the economy's largest business city. For 11 economies the data are also collected for the second largest business city."

Related context in the same section: Getting Credit score 0.0 and rank 186 of 190 (p.4, p.27); strength of legal rights index 0 (0-12) and depth of credit information index 0 (0-8). p.30 note: "If the credit bureau or registry is not operational or covers less than 5% of the adult population, the total score on the depth of credit information index is 0." (Yemen's registry covers 1.3%.) From memory, not checked in this session: the World Bank discontinued the Doing Business series in September 2021 after data irregularities in other economies.

---

## Summary of differences from expectations (A-D)

1. A, trade: the report says trade "relied primarily on the UN Comtrade database"; IRG-reported data is used only to split IRG from non-IRG. "Trade from government-reported data" overstates it.
2. A, "as proposed by the authorities": confirmed, but it is footnote 2 on the 33 percent figure only.
3. A, 1.838: NOT FOUND in the IMF report (a site-computed CBY-Aden / IMF ratio per the repo).
4. A, whole-of-Yemen total: NOT FOUND. The IMF remittances series is not labelled IRG on its row; its IRG basis is implied by the Annex IV method text and the "IRG estimate" GDP note.
5. B, Fig 116: its title is "Main Sources of Financing for the Business", not debt, and its base is all 217 firms (arithmetic), not the 108 with debt. The values sum to 136.85%, so multiple answers are implied but never stated. The body text uses different numbers for the same data (1.3% MFI, Figure 91 shares 40/34/16/1/8) that appear to be the Annex values re-expressed as shares of 136.85.
6. B, supplier credit 1.31: it is Figure 110 on p.148 (not Annex-level text), unlabelled as "formal" and with no "n" on the figure; the formal-firm scope comes from the surrounding section and the 328 in the sample description.
7. C: 281.5 is Yemen; 284.3 is Medium Firms (20-99 employees).
8. D: city is spelled "Sanaa"; the city statement is on the summary page, not the Getting Credit page.
