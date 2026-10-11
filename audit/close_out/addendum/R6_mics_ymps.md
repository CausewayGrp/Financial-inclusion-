# R6 - Yemen MPS Round I (WB Microdata 5999) and Yemen MICS 2022-2023: verbatim reads

Retrieval date: 2026-10-11. Method: curl through the agent proxy, HTML text extracted with a script kept outside the download folder; PDF text via pdftotext, spot-checked against page renders. Quotes are copied from the extracted text; line breaks inside a sentence are joined, nothing else is altered. Square brackets are my notes.

Data hygiene: no data file downloaded (no .dta/.csv/.sav, no "Get Microdata" download, no API key). Only catalog HTML metadata pages and the published MICS PDF were fetched, all into `.../scratchpad/addendum/dl/r6/`. One extra HTML page (`/catalog/5999/get-microdata`, the access page) was requested by mistake in the first batch; it was deleted before it was opened or read, and nothing from it is used. The questionnaire XLSX (`/download/64445`) and the Stata do-file (`/download/64444`) were NOT fetched. `/home/user/Financial-inclusion-` was not modified.

---

## ITEM 1 - World Bank Microdata Library, catalog 5999

URLs fetched (all HTTP 200, text/html):
- https://microdata.worldbank.org/index.php/catalog/5999 (SHA-256 16a9162904586c8d8d10dcf8efd87291312de1c25f3f9fb674ef82025d563b2a)
- https://microdata.worldbank.org/index.php/catalog/5999/study-description (SHA-256 b23a54eca764569d28cd096c1b5501e9c87761399d8e85e19b018b39519211dc). Its extracted text is byte-identical to the main catalog page: the main page already shows the full Study Description.
- https://microdata.worldbank.org/index.php/catalog/5999/data-dictionary (bcad6857c03407ce4de5c52de2592069467c24f34a1ef80ff9ebcb29d3bc0494)
- https://microdata.worldbank.org/index.php/catalog/5999/variable-groups (08cf745bd88b886a71e24a440c2af23ca1b5700242b3917cb41d06667765abcb): shows only the word "variable_groups"; no groups listed.
- https://microdata.worldbank.org/index.php/catalog/5999/related_materials (2ed308d4dce85e51d397107ff0754d75d0f5ea8e313dc3d74e8b8d015ac188bc)
- https://microdata.worldbank.org/catalog/5999/data-dictionary/F1?file_name=ymps_2022_r1 (variable list; 3de151f884f4257aaf37ae3faa61d2fbeae4802e6341b413d8d3b652eeb8e291)
- Variable metadata pages `https://microdata.worldbank.org/catalog/5999/variable/F1/V{n}?name={var}` for sec1_dom_act (V5), sec1_dfa (V6), sec1_irg (V7), sec1_auth (V8), sec3_q01a (V71). These are catalog metadata pages (label, range, category counts), not data.

### 1a. Sample size - VERIFIED
Page: Study Description > Identification > Abstract:
> "The survey draws on a probability sample of 1,297 adult Yemenis (18 years of age and older) with mobile phones, targeted across 21 governorates based on the latest population projections."

Page: Study Description > Sampling > Response Rate:
> "A total of 1,297 respondents completed the interview resulting in a response rate of around 28 percent, indicating the difficulty of completing phone interviews."

Page: Data Dictionary (data file ymps_2022_r1): "Dataset for Yemen Mobile Phone Survey Monitoring Round I, 2022" - Cases: 1297 - Variables: 91.

Note for the record: the same page's Abstract says "21 governorates"; Coverage > Geographic Coverage says "All governorates of Yemen except for Socotra islands"; Sampling > Sampling Procedure lists 18 names for the quotas: "We used sample quotas were to obtain a diverse set of individuals across the governorates of Abyan, Aden, Al-Baida, Al-Dhale, Al-Hodeida, Al-Jawf, Al-Maharh, Al-Mahweet, Amran, Dhamar, Hadramout, Hajja, Ibb, Laheg, Mareb, Remah, Saadah, and Sanaa City." (sic). Sampling > Deviations from the Sample Design: "Some governorate quotas were not achieved due to small populations with mobile phones, lack of infrastructure for mobile phones, or blocking of international numbers for certain mobile phone service providers." The pages do not reconcile 21 vs 18; I do not either.

### 1b. Universe / population - VERIFIED (wording is in the Abstract; there is no separate "Universe" field)
The raw HTML of every fetched page contains zero occurrences of "universe". The only population statement is the Abstract sentence quoted in 1a: "...1,297 adult Yemenis (18 years of age and older) with mobile phones...". Note it says "adult Yemenis", not just "adults". Other fields: Unit of Analysis: "Household and individual". Study type: "Other Household Survey [hh/oth]". Sampling Procedure: "The survey used random digit dialing, relying on the range of valid numbers, with up to three attempts when a phone number was not reached...". Data Collection Mode: "Computer Assisted Telephone Interview [cati]".

### 1c. Data-collection dates - VERIFIED (month resolution only)
Page: Study Description > Data collection > Dates of Data Collection: Start "2022-08", End "2022-09", Cycle "Round 1".
Abstract: "Interviews were conducted over the phone in August and September 2022, using a questionnaire consisting of four sections mainly focusing on labor market experiences and food insecurity."
Data Collection Notes: "Data was collected by a firm based in Amman, Jordan - Mindset. Interviews lasted approximately 30 minutes."
No day-level dates are given on these pages.

### 1d. Area-of-control variable - VERIFIED (variables exist; value labels for sec1_auth are NOT shown)
Page: Data Dictionary > ymps_2022_r1 > Variables (all in Section 1 prefix `sec1_`):
- `sec1_dom_act` - "Dominant actor (from CSV file)" - variable page: Valid 1297, range 1 - 5, no category labels shown.
- `sec1_dfa` - "Area of control - DFA" - variable page: Valid 1297, range 0 - 1; Categories: "0. No" 412 (31.8%), "1. Yes" 885 (68.2%).
- `sec1_irg` - "Area of control -Internationally Recognized Government" - variable page: Valid 1297, range 0 - 1; Categories: "0. No" 885 (68.2%), "1. Yes" 412 (31.8%).
- `sec1_auth` - "Area of control" - variable page: Valid 1297, Invalid 0, range 1 - 2, Type Discrete; NO category labels and no question text shown, so which code is which authority is NOT stated on the page.
- `sec1_gov` - "Governorate".
The variable pages carry this warning verbatim: "Warning: these figures indicate the number of cases found in the data file. They cannot be interpreted as summary statistics of the population of interest." So 412 / 885 are unweighted file case counts, not population shares.
Limits of what the pages say: the abbreviation "DFA" is not expanded anywhere on the fetched pages (I did not infer "de facto authorities"); the words "Houthi", "de facto" and "Ansar" do not occur in any fetched page. The "Questions and instructions" block is empty on all of these variable pages.

### 1e. "Rank the three most important sources" - VERIFIED (variables exist; label omits "of income")
Page: Data Dictionary > Variables:
- `sec3_q01a` - "Can you rank the three most important source?- 1st"
- `sec3_q01b` - "Can you rank the three most important source?- 2nd"
- `sec3_q01c` - "Can you rank the three most important source?- 3rd"
The catalog label reads "source" with no "of income" in it. That these are income sources is shown by the category list on the sec3_q01a page (values with counts of the 1297 file cases): "-96. Other (specify)" 16; "2. Wages" 784 (60.4%); "3. Profit from non-household based enterprise" 115; "4. Sale of food crops" 89; "5. Sale of livestock/animal products" 31; "6. Sale of food assistance" 8; "7. Sale of other goods or profit from other hh based enterprise..." 73; "8. Cash transfers from humanitarian agencies" 8; "9. International remittances" 15; "10. National remittances" 3; "11. Renting of land, buildings or machinery" 12; "12. Support from family or friends" 31; "13. Pensions" 34; "14. Other social benefits" 7; "15. Begging" 7; "16. Regular government salary" 36; "17. Irregular government salary" 28. (Same "cannot be interpreted as summary statistics of the population" warning applies. I did not open the 2nd/3rd variable pages.) Study Description > Scope > Notes: "Food security, displacement, income sources and working conditions". Also in the list: `sec3_q03` "Are you doing any work for this job in the public sector?", `sec4_q02_2a` "Did you recieve any financial aid?" (sic).

### 1f. Title, producer, DOI - VERIFIED
- Page title: "Yemen, Rep. - Mobile Phone Survey Monitoring Round I, 2022"
- Title (Identification): "Mobile Phone Survey Monitoring Round I, 2022"; Subtitle: "Monitoring Food Insecurity and Employment in Yemen"
- Survey ID / Reference ID: "YEM_2022_YMPS-R1_v01_M" (the page header also shows "YEM_2022_YMPS-R1_V01_M")
- DOI: "https://doi.org/10.48529/3na0-xa83"
- Producer(s) (header): "Alia Aghajanian". Primary investigators: Alia Aghajanian, World Bank. Producers: Romeo Gansey, World Bank, role "Data analyst". Funding Agency/Sponsor: "Joint Data Center on Forced Displacement (World Bank and UNHCR) Forced Displacement", role "Funder". Depositor: "Poverty Reduction and Policy Management Network (PREM)". Metadata producer: Development Data Group, World Bank; DDI Document ID "DDI_YEM_2022_YMPS-R1_v01_M_WB"; date of metadata production 2023-09-07. Collection: "Fragility, Conflict and Violence". Created on "Sep 07, 2023"; Last modified "Sep 07, 2023". Version Description: "v2.1: Edited, anonymous dataset for public distribution."
- Citation requirement example: "Alia Aghajanian (World Bank). Yemen - Mobile Phone Survey Monitoring Round I, 2022, Monitoring Food Insecurity and Employment in Yemen (YMPS 2022 R1). Ref: YEM_2022_YMPS-R1_v01_M. Downloaded from [uri] on [date]." Also: "When using data the accompanying report should be cited for methodology and background."
- Related report (External link, Documentation): "Publication: Monitoring Food Insecurity and Employment in Yemen: Results from the Yemen Mobile Phone Survey Monitoring - Round I", Romeo Gansey and Alia Aghajanian (World Bank Group), https://openknowledge.worldbank.org/handle/10986/40265 (listed only; not fetched).

---

## ITEM 2 - Yemen MICS 2022-2023 Survey Findings Report

URL: https://www.unicef.org/yemen/media/9006/file/YEMEN%20MICS%20MULTIPLE%20INDICATOR%20CLUSTER%20SURVEY.pdf
HTTP 200, application/pdf, 9,148,530 bytes, 410 PDF pages, Acrobat Pro 23.6, created 2023-11-23.
SHA-256: `03bf052dd0d23bf66961f9a03dced541b22fe5259cdbc4a5771b8bae5ca1a230`
Retrieval date: 2026-10-11.

Page numbering: PDF page labels equal PDF positions (1..410). The printed page numbers are in the running footers and are offset by section: body PDF p.17 prints "Page 3" (offset 14); Appendix A PDF p.270 prints "page 258"; Appendix E PDF p.332 prints "page 330". The footer text of PDF p.17 and p.19 reads "Sample coverage and characteristics OF RESPONDENTS" although their headings are chapter "5 SURVEY ORGANISATION AND METHODOLOGY"; the printed page numbers are still 3 and 5. The section numbers print as "5.11", "5.12", etc. (as shown on the page render).

### 2a. 22 governorates - VERIFIED
Printed p.3 (Page 3) / PDF p.17, section "5.12 SAMPLE DESIGN":
> "The sample for the Yemen MICS 2022-2023 was designed to provide estimates for a large number of indicators on the situation of children and women at the sub-national and rural/urban levels, for the 22 governorates in Yemen."

Also, printed page 258 / PDF p.270, "APPENDIX A SAMPLE DESIGN":
> "The primary objective of the sample design for the Yemen 2022-2023 MICS was to produce statistically reliable estimates of most indicators, at the national level, for urban and rural areas, and for the 22 governorates of the country. Urban and rural areas in each of the 22 governorates were defined as the sampling strata."

### 2b. 41 enumeration areas not visited - VERIFIED
Printed p.3 / PDF p.17, section 5.12 SAMPLE DESIGN:
> "A total of forty-one (41) of the selected enumeration areas could not be visited because they were inaccessible due to security and safety reasons during the fieldwork period."

Same paragraph: "The total target sample size for the Yemen MICS was 880 clusters and 22,000 households." and "As the sample is not self-weighting, sample weights are used for reporting survey results." Search of the full text for "forty", "inaccessible", "could not be visited" finds these only on PDF p.17.

### 2c. Fieldwork periods - VERIFIED
Printed p.5 (Page 5) / PDF p.19, section "5.17 FIELDWORK":
> "Fieldwork (data collection) was conducted from July - September 2022 in the Aden hub covering Abyan, Hadramout, Shabwah, Aden, Lahj, Al Maharah, Socotra, Al Dhale'e6, Taizz6, Marib6, Al Jawf6 and Al Hudaydah6 governorates. The data collection for Sana'a hub was conducted from January - May 2023 covering Ibb, Sana'a city, Al-Bayda, Hajjah, Dhamar, Sa'ada, Sana'a, Al-Mahwiet, Amran, Raymah, Al Dhale'e6, Taizz6, Marib6, Al-Jawf6 and Al Hudaydah6 governorates. Since the data collection was conducted at different periods in Aden and Sana's hubs, effects of seasonality on some indicators (such as nutrition and food insecurity) may vary across the governorates. The results should be used with this consideration."
[The superscript "6" after five governorate names is footnote 6 on that page: "Data collected partly from Aden and Sana'a hubs". "Sana's" is the report's own typo.]

Same page, "5.16 TRAINING": "Training for the fieldwork was conducted for 21 days in May-June 2022 (Aden hub) and October-November 2022 (Sana'a hub)."
PDF p.4 (front-matter "SUMMARY TABLE OF SURVEY IMPLEMENTATION AND THE SURVEY POPULATION"; no printed page number on that page): "Fieldwork July-Sep 2022 (Aden hub) / Jan-May 2023 (Sana'a hub)"; "Interviewer training May-Jun 2022 (Aden hub) / Oct-Nov. 2022 (Sana'a hub)"; "Sample frame Census 2004 update in 2014"; "- Updated March-May 2022 (Aden hub) / April-Dec 2022 (Sana'a hub)".
Also from PDF p.19: "The data were collected by 32 teams; each was comprised of 6 female interviewers, one measurer, one supervisor and a driver."

### 2d. HC19 in the household questionnaire - VERIFIED
Printed p.330 ("Appendix E: Yemen MICS 2022-2023 Questionnaires| page 330") / PDF p.332 (page render checked):
> "HC19. Does any member of this household have a bank account?"  with response options  "YES ... 1" and "NO ... 2".
[Preceding items on the same page: HC14 dwelling ownership; HC15 "Does any member of this household own any land that can be used for agriculture?"; HC17 "Does this household own any livestock, herds, other farm animals, or poultry?" with routing "2 -> HC19" (printed as "2 HC19").]
The expected locator (printed p.330 / PDF p.332) is correct. In the extracted text the question wraps as "...have a / bank account?"; the sentence is the same.

### 2e. Is HC19 tabulated in any results table - VERIFIED as "no occurrence found in the text" (extraction-based; see caveat)
Full-text search (pdftotext, all 410 pages):
- "bank account" (also allowing line-break whitespace): 1 hit, PDF p.332 (the HC19 item itself).
- "HC19" / "HC 19": hits only on PDF p.332 (the item and the HC17 skip instruction).
- "bank" / "banks": 4 hits, PDF p.240 (3 hits, all in footnote citations naming "The International Bank for Reconstruction and Development / The World Bank" and "World Bank Press") and PDF p.332.
- "mobile money", "mobile banking", "financial inclusion", "financial account", "financial service", "savings account", "banking": 0 hits.
- Table SR.2.2 "Household and personal assets (Part 1)" (printed page 20 / PDF p.34, with Part 2 on PDF p.35) lists Television, Refrigerator, Washing Machine, Agricultural land, Farm animals/Livestock, Bicycle, Motorcycle or scooter, Car, truck, or van, Boat with a motor, Boat/canoe without a motor/Canoe, Computer or tablet, Mobile telephone, and dwelling ownership; there is no bank-account row.
Conclusion: on the extractable text, no results table or narrative tabulates HC19; the household bank-account item appears only as a questionnaire item in Appendix E. Caveat: only PDF p.2 and p.410 have no extractable text (cover/photo pages); every other page has a text layer, so a table rendered purely as an image would be the only way for a tabulation to be missed, and none of the table pages checked (p.34-35) are images. I did not visually page through all 410 pages.

---

## Summary
| Item | Status |
|---|---|
| 1a sample size 1,297 | VERIFIED (Abstract + Response Rate + Data Dictionary cases) |
| 1b universe | VERIFIED as Abstract wording only; no "Universe" field exists on the pages |
| 1c collection dates | VERIFIED (2022-08 to 2022-09; month resolution) |
| 1d area-of-control variable | VERIFIED: sec1_auth, sec1_irg, sec1_dfa (and sec1_dom_act); sec1_auth value labels not shown; "DFA" not expanded |
| 1e rank three most important sources | VERIFIED: sec3_q01a/b/c; label lacks "of income" |
| 1f title / producer / DOI | VERIFIED |
| 2a 22 governorates | VERIFIED (printed p.3 / PDF p.17; also printed p.258 / PDF p.270) |
| 2b 41 EAs not visited | VERIFIED (printed p.3 / PDF p.17) |
| 2c fieldwork periods | VERIFIED (printed p.5 / PDF p.19; PDF p.4) |
| 2d HC19 | VERIFIED (printed p.330 / PDF p.332) |
| 2e HC19 tabulated | VERIFIED as not found in extracted text (only the questionnaire item) |
