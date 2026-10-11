# V2 - Verification of YLG Annual Report 2022 and OECD (2026) Promoting Economic Resilience in Yemen

Read-only check. Nothing under <repository> was modified. Downloads: <session scratchpad>/v5/dl/V2/ (text read with pdftotext -layout; tables, charts and Box 2.1 also rendered with pdftoppm and looked at; arithmetic with `python3 -I`, script in scratchpad/v5/scripts/ylg_check.py).

| Document | File | Bytes | SHA-256 | Pages |
|---|---|---|---|---|
| A. YLGP Annual Report 2022 | ylg2022.pdf | 3,252,129 | fc6651b7bf87f299243c1b78cdf3a5507b5702bfd6bb8b23cc4419a5f9c3fb22 | 35 PDF pages |
| B. OECD (2026) | oecd.pdf | 2,028,063 | 4ae2f699e06796b25e2e13312f125fa2582a37b9a7b0aa108bf81606a6ef33b0 | 71 PDF pages |

Page convention. A: printed page number = PDF page number on pp.2-35 (cover is p.1, unnumbered). B: printed page = PDF page - 2 (PDF p.5 is printed "3"; PDF p.34 is printed "32"). Cites below read "PDF n / printed m".

---------------------------------------------------------------------------------------------------

## A. Yemen Loan Guarantee Program (YLGP), Annual Report 2022

Title on cover: "ANNUAL REPORT 2022"; running header "YLGP ANNUAL REPORT 2022"; PDF title metadata "YLGP Annual Report 2022".

### A1. Headline figures

| Item | Expected | Found | Verbatim quote | Page |
|---|---|---|---|---|
| Guarantees (letters of guarantee) issued in 2022 | 3,387 | CONFIRMED 3,387 (printed "3387" on pp.4, 8) | "During the fiscal year 2022, 3387 letters of guarantee were issued in the amount of YER 6.4 billion to cover loans worth YER 9.4 billion." Also: "During 2022, the program issued 3,387 letters of guarantee, with an increase of 155% over the productivity of 2021." Glance panel: "3387 Issued Guarantee" | p.8 (text); p.14 (text, table); p.4 (panel) |
| Guarantee amount | YER 6,397,627.81 thousand | CONFIRMED. Unit is THOUSAND YER (column header). 6,397,627.81 thousand = YER 6.40 billion | Header: "Guarantees Amount (Thousand YER)"; row: "Grand Total 3387 1327 155% 6,397,627.81 3,307,126.62 93% 9,371,245.29 5,046,982.67 86%" | p.14 |
| Covered loan principal | YER 9,371,245.29 thousand | CONFIRMED. Unit THOUSAND YER = YER 9.37 billion. Label used is "Guaranteed Loans Amount (Thousand YER)", not "principal". Glance panel rounds to YER 9.4B | Header: "Guaranteed Loans Amount (Thousand YER)"; panel: "YER 9.4B Guaranteed Loans" | p.14 (table); p.4 (panel); p.8 ("to cover loans worth YER 9.4 billion") |
| Amount/loan relation | not asked | Guarantee amount is 68.3% of guaranteed loans (6,397,627.81 / 9,371,245.29); the report states no coverage ratio for individual guarantees, only "90% coverage" for the women's portfolio product | "women-led MSMEs with 90% coverage" | p.9, p.15 |
| Growth 2022 vs 2021 | not asked | Number +155%, amount +93%, loans +86% (arithmetic agrees: 155.2%, 93.4%, 85.7%) | "The growth percentages of guarantees number, guarantees amount, and guaranteed loans amount are 155%, 93%, and 86% respectively." | p.8 |
| Partner institutions | 12 | CONFIRMED 12 "Total PFIs" (1 new in 2022: Yemen Kuwait Islamic Bank). Report calls them "PFIs"/"Partner Financial Institutions" (acronym list p.3); it never defines PFI as "banks and microfinance providers" in one phrase | "1 new PFI 12 Total PFIs"; "a new partnership agreement was signed with the Yemen and Kuwait Islamic Bank to become the partner number 12." | p.4; p.17; p.9 ("making the total PFIs as 12") |
| Governorates / districts | not asked | 18 governorates, 156 districts (Governorate table has 19 rows; Raymah = 0 in 2022, so 18 with guarantees) | "18 Governorates 156 Districts" | p.4; table p.18 |

### A2. Gender, age, area (2022)

| Item | Expected | Found | Verbatim quote | Page |
|---|---|---|---|---|
| Female-led / women-led: 693 of 3,387 | 693 / 3,387 | CONFIRMED 693 (20.5%). Terms used: the table row is "FEMALE" under header "Gender" (male 2,694); text says "women beneficiaries" and "women-led MSMEs"; glance panel says "Women-led MSMEs". The report defines none of these terms (no ownership/management test given) | "The percentage of women beneficiaries is about 20% in 2022"; "the number of guarantees issued in 2022 for women-led MSMEs by 100% compared to the previous year"; table row "FEMALE 693 347 100% 658,302.25 311,975.72 111% 802,094.93 466,766.28 72%"; panel "20% Women-led MSMEs" | p.15 (text and table); p.4 (panel) |
| Youth 1,907 of 3,387 | 1,907 | CONFIRMED 1,907 (56.3%). Row label "YOUTH" vs "NOT YOUTH (+35Y)" (1,480). The "+35Y" label is as printed, so the report does not state an upper youth age limit | "YOUTH 1907 699 173% 3,370,438.79 1,656,153.64 104% 4,831,718.81 2,454,078.68 97%" | p.16 |
| Rural 1,748 of 3,387 | 1,748 | CONFIRMED 1,748 (51.6%); urban 1,639 | "Rural 1748 847 106% 3,386,611.28 2,101,490.75 61% 4,701,233.61 2,987,935.17 57%" | p.17 (table); intro sentence p.16 |

Internal inconsistency to note (p.15): the text says "the guarantees issued in favor of youth beneficiaries increased by 175% compared by 2021", but the table gives youth +173% (1,907 vs 699 = +172.8%); +175% is the MALE row (2,694 vs 980). Do not cite 175% for youth.

### A3. Annex I (pp.29-31) - "Culminative Guarantees Analysis 2018-2022"

Annex I is charts only, with data labels and no data table. I read the label-to-category mapping from the rendered pages (legend colours checked).

| Item | Expected | Found | Verbatim quote (chart labels) | Page |
|---|---|---|---|---|
| Yearly guarantees issued | 301, 691, 1,270, 1,327, 3,387 | CONFIRMED, by year: 2018 = 301; 2019 = 691; 2020 = 1,270; 2021 = 1,327; 2022 = 3,387. Chart title "Historical data of Issued Guarantees". No 2017 bar although p.6 says "official launch in July 2017" | "301", "691", "1270", "1327", "3387" on axis 2018-2022 | p.29 |
| Sum = 6,976? | 6,976 | YES arithmetically: 301+691+1,270+1,327+3,387 = 6,976. The figure 6,976 is NEVER PRINTED in the report; it is my sum | n/a | p.29 |
| Every Annex I split totals 6,976? | 6,976 | YES, all six: Product 4,987+1,989 = 6,976; Sector 2,464+2,155+1,267+598+462+30 = 6,976; Gender 5,451+1,525 = 6,976; Age 3,825+3,151 = 6,976; Area 4,183+2,793 = 6,976; PFIs 1,828+1,282+1,066+981+870+399+383+123+37+5+2 = 6,976 | Product: "4987; 71%" INDIVIDUAL, "1989; 29%" PORTFOLIO. Sector: "2464; 35%" AGRICULTURAL, "2155; 31%" COMMERCIAL, "1267; 18%" ANIMAL, "598; 9%" SERVICE, "462; 7%" PRODUCE, "30; 0%" FISH. Gender: "5451; 78%" MALE, "1525; 22%" FEMALE. Age: "3825; 55%" YOUTH, "3151; 45%" NOT YOUTH. Area: "4183; 60%" Rural, "2793; 40%" Urban. PFIs: KURAIMI 1828, AZAL 1282, AMAL 1066, TADHAMON 981, NMF 870, YKB 399, ETIHAD 383, NAMAA 123, SBYB 37, HADHRAMOUT 5, YKI-BANK 2 | pp.29, 30, 31 |
| Women's total to end 2022 | 1,525 | CONFIRMED 1,525 (22%). Counted in guarantees, not women | "1525; 22%" (legend FEMALE) | p.30 |
| Cumulative youth / rural | not asked | Youth 3,825 (55%); rural 4,183 (60%) cumulative 2018-2022 | as above | p.30 |
| Women's total, other statement | not asked | CAUTION: the Managing Director's remarks give a different unit: "YER 1.5 billion of loans to over 1,360 women-led MSMEs" (MSMEs, not guarantees). 1,525 guarantees vs "over 1,360" MSMEs are not reconciled in the report | "The YLGP has to date guaranteed YER 1.5 billion of loans to over 1,360 women-led MSMEs" | p.9 |

Cumulative cross-checks that agree with the 2021/2022 tables: portfolio 1,989 = 1,953 (2022) + 36 (2021); individual 4,987 = 1,434 + 1,291 + 2,262 (2018-2020).

Annex III (p.33) shows 12 partner logos (Azal, Al-Amal, Shamil Bank of Yemen & Bahrain, Hadhramout MFP, Al-Kuraimi, YKB, YKB Islamic, Tadhamon, NMF, Yemen Commercial Bank, Al-Ithad, Nama). Yemen Commercial Bank does not appear in the 2022 PFI table (p.17) or the Annex I PFI chart (11 institutions), so 11 of the 12 partners have issued guarantees.

### A4. Outstanding portfolio and PAR

| Item | Expected | Found | Verbatim quote | Page |
|---|---|---|---|---|
| Outstanding guarantees 3,526 | 3,526 | CONFIRMED, glance panel only | "3526 Outstanding Guarantees" | p.4 |
| Outstanding amount about YER 4.6 billion | ~YER 4.6bn | CONFIRMED, glance panel only; shown as "YER 4.6B" with no unit beyond that, no basis (guarantee amount or loan amount) | "YER 4.6B Outstanding Guarantees" | p.4 |
| As-of date for outstanding | stated? | NOT FOUND. Searched the full text for "outstanding", "as of", "as at", "December", "31st", "fiscal" in all 35 pages. "Outstanding" occurs only on p.4. No date or definition is printed; the only dated text is "fiscal year 2022" (p.8) | n/a | NOT FOUND |
| PAR 8.54% | 8.54% | CONFIRMED as "PAR >=120" (Total row, ">=120" column) | p.4: "8.54% PAR >=120". p.20: "Total 4.89% 12.46% 11.01% 9.15% 8.54%" under columns "<30 >=30 >=60 >=90 >=120" | p.4; p.20 |
| PAR base stated? | whether stated | NOT STATED. Section title is "PORTFOLIO AT RISK ANALYSIS". The page gives no denominator (outstanding amount? number?), no unit for the thresholds (days is not said), no as-of date, no definition. Note: rows add to the Total, so the per-category figures are shares of the whole book, not within-category rates: sector rows >=120 add to 8.54; product 0.86+7.68 = 8.54; gender 1.01+7.52 = 8.53; governorate rows add to 8.52 (rounding). This reading is my inference, not stated by the report | "PAR Distribution Per Type of Business"; "PAR Distribution Per Product"; "PAR Distribution Per Gender"; "PAR Distribution Per Governorate" | p.20 |

### A5. What the programme does, in its own words

| Item | Expected | Found | Verbatim quote | Page |
|---|---|---|---|---|
| Mission | risk sharing with partner banks / MFIs on MSME loans | CONFIRMED in substance. The report speaks of "guarantees" and "risk-sharing", not of a single defining sentence | "Facilitate financial access for target segments through the provision of guarantees products and services to those with insufficient collateral." | p.5 |
| Role vis-a-vis PFIs | | | "empowers micro, small and medium-sized enterprises (MSMEs) across Yemen to grow by accessing the required financing from our partner financial institutions (PFIs.)" | p.6 |
| Risk sharing | | | "...position YLGP as the go-to institution for risk-sharing mechanisms in the whole republic." and "As a partner for risks with our PFIs, the program seeks to consolidate its relationship with all existing partners" | p.7; p.17 |
| No direct contact with borrowers | | | "As we work in invisible mode without any direct interactions with the borrowers, it is a must to increase the network of our PFIs" | p.8 |
| Products | | | "both Individual and Portfolio guarantee models"; "The portfolio guarantee model is representing 58% and the individual guarantee model is representing 42%." | p.7; p.14 |
| Gap addressed | | | "to reduce the financial gap between the Yemeni MSMEs and the MFIs" (the report's wording; it says MFIs here) | p.8 |
| Banks vs MFIs | | PFIs include banks (e.g. Tadhamon, YKB, Al-Kuraimi Islamic Microfinance Bank, Shamil Bank) and microfinance programmes/foundations (Azal, NMF, Etihad, Nama), per tables and Annex III; the report does not itself label them "banks and microfinance providers" | n/a | pp.17, 33 |

### A6. Period and publication date

| Item | Found | Verbatim | Page |
|---|---|---|---|
| Fiscal year covered | "fiscal year 2022". No start/end dates for the fiscal year are printed. Activity log runs 22 Feb 2022 to 29 Dec 2022 | "During the fiscal year 2022, 3387 letters of guarantee were issued" | p.8; log pp.21-28 |
| Publication date | NOT FOUND printed (searched cover, p.2 contents, p.35 back page and full text). Only "© Copyright reserved 2022" (p.35). PDF file metadata (not printed text): Title "YLGP Annual Report 2022", Author "Rami Al-Sabri", CreationDate 16 Apr 2023 (Word) | "© Copyright reserved 2022" | p.35 |
| Programme history | "official launch in July 2017" | "Since its official launch in July 2017 ... the Yemen Loan Guarantee Program has grown over the past 5 years" | p.6 |

---------------------------------------------------------------------------------------------------

## B. OECD (2026), Promoting Economic Resilience in Yemen, DOI 10.1787/81ed2898-en

Citation as printed: "OECD (2026), Promoting Economic Resilience in Yemen, OECD Publishing, Paris, https://doi.org/10.1787/81ed2898-en." (PDF 4). Copyright page: "(c) OECD 2026"; the running footer on every body page says "PROMOTING ECONOMIC RESILIENCE IN YEMEN (c) OECD 2025". Author metadata "OECD"; PDF creation 14 Jan 2026, modified 9 Feb 2026.

### B1. YLG paragraph (printed p.32, PDF 34)

| Item | Expected | Found | Verbatim quote | Page |
|---|---|---|---|---|
| 5,731 transactions "since 2017" | 5,731; "since 2017" | CONFIRMED. Printed with a space separator, "5 731" | "Since 2017, the YLG has guaranteed 5 731 transactions, of which 72.7% were granted to men-owned businesses, 60% to businesses located in rural areas and 55% to young-owned businesses." | PDF 34 / printed 32 |
| USD 42.8m guarantees; USD 63.6m loan principal | 42.8; 63.6 | CONFIRMED. "cumulative", "in nominal terms" | "In nominal terms, the YLG has provided a cumulative amount of USD 42.8 million of guarantees for a loan principal amount of USD 63.6 million." | PDF 34 / printed 32 |
| 72.7% men-owned; 60% rural; 55% young-owned | as stated | CONFIRMED as printed. The basis (count of transactions, by the sentence's grammar) is not labelled | (same sentence) | printed 32 |
| Sector shares and sum | do they sum to 104%? | YES, they sum to 104%: 36+29+19+9+7+4 = 104. The sentence says they are shares "of the amount of guarantees" | "The largest share of the amount of guarantees has been provided to agricultural businesses (36%), followed by commercial (29%), livestock (19%), services (9%), industrial and manufactures (7%) and fisheries (4%) businesses." | printed 32 |
| Cutoff date / exchange rate stated | | NOT FOUND. The paragraph gives no end date for the cumulative figures (only "Since 2017") and no YER/USD exchange rate. "In nominal terms" is the only qualifier. The paragraph carries no citation or source note; the references list (printed pp.66-69) has no YLG entry; "YLG" appears only on printed pp.31, 32, 36 | n/a | NOT FOUND (searched all 71 PDF pages for "exchange rate", "as of", "cut-off", "end-20", "31 December", "YER", "USD 1"; the only exchange-rate text is about the dual-currency system on printed p.33 and p.38) |
| Describes YLG as | | "partial loan guarantees on loans made by banks and microfinance institutions to MSMEs"; it also says the YLG "primarily concentrates on enterprises that operate in agricultural, manufacturing and industry, and technological sectors" (a sector description not in the YLG report) | "The Yemen Loan Guarantee Program (YLG) aims to facilitate financial accessibility for MSMEs through the provision of partial loan guarantees on loans made by banks and microfinance institutions to MSMEs located in Yemen." | printed 32 |

Do the OECD numbers agree with the YLG report? (arithmetic on A3)
- 5,731 transactions: does NOT match the YLG cumulative 6,976 guarantees to end 2022 (difference 1,245). No cutoff is given by OECD, so the gap cannot be explained from the two documents. The two counts need to be published with their own bases.
- 72.7% men-owned: does NOT match the YLG cumulative male share, 5,451 of 6,976 = 78.1% (female 1,525 = 21.9%). OECD says "men-owned"; YLG says MALE. 72.7% is not the complement of 21.9%.
- 60% rural and 55% young: MATCH the YLG Annex I cumulative shares (rural 4,183/6,976 = 60.0%; youth 3,825/6,976 = 54.8%), even though the totals differ.
- Sector shares: OECD (36/29/19/9/7/4, by "amount of guarantees") differ from the YLG Annex I counts (agricultural 35%, commercial 31%, animal 18%, service 9%, produce 7%, fish 0%; by number, not amount). The OECD label "industrial and manufactures" does not appear in the YLG report; the nearest YLG category is "PRODUCE". Fisheries 4% (OECD) vs 30 of 6,976 = 0.4% by count (YLG) cannot be reconciled on the information given.
- USD 42.8m / USD 63.6m cannot be checked against the YLG report (which is in YER, 2022 only: YER 6.40bn / YER 9.37bn for 2022). The ratio 42.8/63.6 = 67.3% is close to the 2022 ratio of 68.3%.

### B2. Financial consumer protection and redress

| Item | Expected | Found | Verbatim quote | Page |
|---|---|---|---|---|
| Instructions "adopted in August 2023"; "in the process of being implemented" | printed p.35 | CONFIRMED wording, but on printed p.33 (PDF 35), NOT printed p.35. The expected "p.35" matches the PDF page number, not the printed number | "The Regulatory Instructions for Financial Consumer Protection, which were reviewed by the OECD, were adopted by the CBY-Aden in August 2023 and at the time of writing are in the process of being implemented." | PDF 35 / printed 33 |
| Same instructions, second mention | | "adopted by the CBY-Aden in August 2023" with implementation challenges; also "recently adopted" | "While the Regulatory Instructions for Financial Consumer Protection that were adopted by the CBY-Aden in August 2023 align with the OECD Financial Consumer Protection (FCP) Principles, the CBY-Aden team mentioned challenges related to the effective implementation and supervision of these Regulatory Instructions." | PDF 38 / printed 36 (and printed 43 "recently adopted") |
| Money-exchange customers: no avenue for complaints or redress | "no avenue" | CONFIRMED, but wording is plural "no avenues", and it says "consumers ... of money exchange companies" | "Moreover, remaining regulatory gaps impede the effective protection of financial customers. For instance, consumers have currently no avenues for complaints or redress for consumers of money exchange companies. This is especially affecting customers facing frozen deposits and cross-border transactions." | PDF 38 / printed 36 |
| Earlier baseline | | "as of end 2021, there was no clear financial consumer protection framework in place for bank or microfinance organisations clients" | | PDF 35 / printed 33 |

### B3. Deposit insurance

| Item | Expected | Found | Verbatim quote | Page |
|---|---|---|---|---|
| "some 70% of deposits would be covered" | as stated | CONFIRMED. No source cited, no date | "Under the current DGS, some 70% of deposits would be covered in case of a bank failure and depositors would receive their compensation within one month." | PDF 40 / printed 38 |
| Funds at CBY-Sana'a invested in distressed bonds | as stated | CONFIRMED, as two sentences; the second says "invested in distressed sovereign government bonds", with no named holder or amount | "Yet DGS funds are currently stored in accounts administrated by the CBY in Sana'a. Another major challenge is that DGS funds have been invested in distressed sovereign government bonds." | PDF 40 / printed 38 |
| Money exchangers: no DGS | not asked | "customers' deposits are not covered by any deposit guarantee scheme (DGS)" | | PDF 37 / printed 35 |

### B4. Account ownership, mobile phone access

| Item | Expected | Found | Verbatim quote | Page |
|---|---|---|---|---|
| Current accounts 12%; savings accounts 11% | 12%, 11% | CONFIRMED. Survey / period NOT NAMED in the sentence or in a footnote: no citation, no year. The adjacent paragraphs cite "OECD/INFE 2023 International Survey of Adult Financial Literacy" for the 15/100 well-being and 42/100 literacy scores, and "FinDev Gateway, n.d." for 4% in 2011 and 6% in 2014, but those do not tie to the 12%/11%. Reference list (printed 66-69) has nothing that names an account-ownership survey for them | "Just 12% of adults declared having a current account at a formal financial institution and 11% declared having a savings account, while these two products are the most widespread financial products in Yemen." | PDF 34 / printed 32 |
| Mobile phone access 68% | 68% | CONFIRMED. NOT in the same place as 12%/11%: it is in the recommendations. No survey, year or source named. The sentence is ambiguous: it may refer to rural areas or to the whole population | "Finally, electronic money accounts could be leveraged to increase financial inclusion levels, especially for those living in remote areas. In fact, financial inclusion levels are especially low in rural areas, and access to mobile phones (68%) is higher than financial inclusion levels (below 10%)." | PDF 44 / printed 42 |

### B5. Informal-sector share, banks, Box 2.1

| Item | Expected | Found | Verbatim quote | Page |
|---|---|---|---|---|
| "almost 70%" of transactions outside the formal sector | as stated | CONFIRMED. No source, no date ("currently"). Not to be confused with "approximately 70% of surveyed firms" (World Bank 2023, printed 9) and "nearly 70% primarily selling within Yemen" (printed 9) | "Money exchangers are vulnerable to money laundering and terrorism financing as almost 70% of financial transactions in Yemen are currently performed outside of the formal financial sector." | PDF 37 / printed 35 |
| "22 banks operating" | 22 | CONFIRMED. Breakdown sums to 22 (3+4+4+5+6). No as-of date ("currently") | "22 banks are currently operating in Yemen: 3 state-owned banks, 4 domestic commercial banks, 4 foreign-owned commercial banks, 5 Islamic banks, and 6 microfinance banks." | PDF 31 / printed 29 |
| Box 2.1 title | | | "Box 2.1. Bank regulatory and supervisory measures implemented by the CBY-Aden in 2021-2022" | PDF 30 / printed 28 |
| Box 2.1 Decision 7 | 7/2022 | CONFIRMED; printed as "Board Resolution" | "Board Resolution No. (7/2022) for the creation of a Licensing Committee." | printed 28 |
| Decision 8 | 8/2022 | CONFIRMED; "Board of Directors Decision" | "Board of Directors Decision No. (8/2022) to increase bank capital requirements. The capital of commercial banks and Islamic banks has been raised from YER 6 billion to YER 45 billion (Yemeni riyal). The capital of microfinance banks has been increased from YER 500 million to YER 5 billion." | printed 28 |
| Decision 9 | 9/2022 | CONFIRMED; "Board of Directors Decision" | "Board of Directors Decision No. (9/2022) for amendments to the mandatory reserve ratio. The percentage of legal reserves that banks must withhold from annual profits has been increased from 15% to 25% at least." | printed 28 |
| Decision 10 | 10/2022 | CONFIRMED; "Board of Directors Decision" | "Board of Directors Decision No. (10/2022) for the conditions and the procedures for initial licencing of domestic and foreign banking entities." | printed 28 |
| Decision 11 | 11/2022 | CONFIRMED; "Board Resolution" | "Board Resolution No. (11/2022) for revisions of the Microfinance Banks Law." | printed 28 |
| Unnumbered item | not asked | The next bullet has no number as printed: "Board Resolution No. (/ 2022) for amendments to the regulatory requirements for payment service providers and payment system operators." | | printed 28 |

Numbers in Box 2.1 are as printed with the mixed labels "Board Resolution" (7, 11) and "Board of Directors Decision" (8, 9, 10). Do not render them all as "Decision".

### B6. HTML chapter locators on oecd.org

Result: NOT VERIFIED - could not be resolved from this environment. Every oecd.org HTML URL returned HTTP 403 to curl (also with a browser User-Agent: Cloudflare "Just a moment..." challenge page) and to WebFetch. I did not attempt to bypass the challenge. The PDF's own link annotations (pdfinfo -url) contain no chapter URLs (only the DOI, corrigenda page and external links).

URLs surfaced by a web search (WebSearch, oecd.org domain only; indexed by the search engine, but not fetched by me):

| Part | URL (as returned by the search) |
|---|---|
| Landing page (search result) | https://www.oecd.org/en/publications/2026/02/promoting-economic-resilience-in-yemen_b66657c1.html |
| DOI resolves (redirect seen with curl) to | https://www.oecd.org/en/publications/promoting-economic-resilience-in-yemen_81ed2898-en.html (403) |
| Introduction | https://www.oecd.org/en/publications/promoting-economic-resilience-in-yemen_81ed2898-en/full-report/introduction_bf2047ce.html |
| 1 Domestic Revenue Mobilisation | https://www.oecd.org/en/publications/promoting-economic-resilience-in-yemen_81ed2898-en/full-report/domestic-revenue-mobilisation_c0ce5075.html |
| 2 The Financial Sector (printed pp.26-43 per the table of contents; every B1-B5 item sits on a printed page in this range) | https://www.oecd.org/en/publications/promoting-economic-resilience-in-yemen_81ed2898-en/full-report/the-financial-sector_4d6228a4.html |
| 3 Capacity for Economic Data Collection and Analysis | https://www.oecd.org/en/publications/promoting-economic-resilience-in-yemen_81ed2898-en/full-report/capacity-for-economic-data-collection-and-analysis_a909c60d.html |
| 4 Effective PPD in the context of Yemen (GRC/MEA). | https://www.oecd.org/en/publications/promoting-economic-resilience-in-yemen_81ed2898-en/full-report/effective-ppd-in-the-context-of-yemen-grc-mea_bdc84e09.html |
| Full PDF (downloaded, 200 OK) | https://www.oecd.org/content/dam/oecd/en/publications/reports/2026/02/promoting-economic-resilience-in-yemen_b66657c1/81ed2898-en.pdf |
| Arabic version (search result) | https://www.oecd.org/mena/competitiveness/economic-resilience-in-yemen-arabic/ |

Two path forms appear: `/en/publications/promoting-economic-resilience-in-yemen_81ed2898-en/...` (DOI-id based, used for chapters and for the DOI redirect) and `/en/publications/2026/02/promoting-economic-resilience-in-yemen_b66657c1.html` (landing, b66657c1 id). The search summary said the publication date listed on OECD's page is 16 February 2026; I could not verify that on the page. The Financial Sector chapter is the one that contains printed pp.26-43 (per the table of contents); the YLG paragraph (printed p.32) falls in its "Context and Overview" part (TOC: starts p.27; "Current Challenges" p.33; "Policy Priorities" p.37).

Table of contents (PDF 7 / printed 5): Introduction 8; 1 Domestic Revenue Mobilisation 13; 2 The Financial Sector 26 (Context and Overview 27, Current Challenges 33, Policy Priorities 37); 3 Capacity for Economic Data Collection and Analysis 44; 4 Effective PPD in the context of Yemen (GRC/MEA). 52.

---------------------------------------------------------------------------------------------------

## Differences from the expectation (summary)

1. OECD financial consumer protection wording is on printed p.33 (PDF 35), and the "avenues" redress sentence on printed p.36 (PDF 38). Printed p.35 holds the "almost 70%" money-exchanger passage instead.
2. OECD says "no avenues" (plural), not "no avenue".
3. OECD sector shares sum to 104% (36+29+19+9+7+4).
4. OECD 5,731 transactions and 72.7% men-owned do not agree with YLG's own cumulative 6,976 and 78.1% male (Annex I, to end 2022); 60% rural and 55% youth do agree. No OECD cutoff date or exchange rate.
5. YLG: 6,976 is not printed anywhere (it is the sum); outstanding guarantees (3,526; YER 4.6B) have no as-of date and are on p.4 only; PAR 8.54% has no stated base, unit or date; no publication date printed.
6. YLG p.15 text says youth +175% while its table says +173% (175% is the male row).
7. YLG p.9 says "over 1,360 women-led MSMEs" (YER 1.5bn) vs Annex I 1,525 women guarantees: different units, not reconciled.
8. YLG Annex III shows 12 partners, but only 11 appear in the 2022 PFI table and the Annex I chart (Yemen Commercial Bank has no guarantees listed).
9. OECD footers say "(c) OECD 2025" while the citation and copyright page say 2026.

## NOT FOUND

- YLG: as-of date for 3,526 / YER 4.6B outstanding; PAR base/unit/date; publication date; definition of "women-led"; the total 6,976 as a printed figure.
- OECD: cutoff date and exchange rate for the YLG USD figures; source or survey and period for 12%, 11%, 68%, "almost 70%", "some 70% of deposits", and the YLG paragraph; any YLG entry in the reference list.
- oecd.org chapter HTML pages: not fetched (HTTP 403, Cloudflare challenge); the URLs above are from search results and are unverified.
