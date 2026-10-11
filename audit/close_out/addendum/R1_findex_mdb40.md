# R1: Global Findex 2021 methodology (CR-21, CR-22) and Migration and Development Brief 40 (CLM-039)

Retrieval date: 2026-10-11 (downloads made 05:39 to 05:40 UTC).
Reader: Claude Code subagent R1. Read-only. No API key was used, no respondent microdata was requested or downloaded, and no figure below was computed from microdata.

## Key findings

1. **Findex Table A.1 prints the Yemen end date as "Jan 10, 2023".** The full cell reads "Nov 7, 2022–Jan 10, 2023" (printed p. 17, PDF p. 15).
2. **The Microdata Library catalog (study 5862) prints a different end date: "2023-01-09".** Its "Dates of Data Collection" table reads Start "2022-11-07", End "2023-01-09". The two World Bank sources differ by one day on the end date and agree on the start date. The website's "7 November 2022 to 9 January 2023" matches the catalog, not the methodology PDF.
3. **Table A.1 and the catalog both describe the Yemen exclusion as "approximately 23% of the population".** They use identical wording and give these reasons: "small size, remoteness or security issues". They also say "over one-fourth of the PSUs were replaced".
4. **Footnote b says the design effect reflects only the weights.** It "does not incorporate the intraclass correlation coefficients because they vary by question". Yemen's printed design effect is 1.9 and its margin of error is 4.3.
5. **The MDB 40 Figure A.4.2 note says Yemen is excluded, but panel a shows a Yemen bar.** The note reads "*The Islamic Republic of Iran, the Syrian Arab Republic, and the Republic of Yemen are excluded due to data availability." However, panel a ($ billion, 2023) plots a bar labelled "Yemen, Rep." with the value "3.8". Panel b (percentage of GDP, 2023) has no Yemen bar. The asterisk sits on the subtitles of both panels. This was verified by rendering the page and from the PDF text layer. The printed figure contradicts its own note for panel a, so the note cannot be cited on its own as saying Yemen is absent from the figure.

---

## Sources, retrieval and hashes

| File | URL | HTTP | Bytes | SHA-256 |
|---|---|---|---|---|
| `Findex2021-22-Methodology.pdf` | https://thedocs.worldbank.org/en/doc/fe026d04da1eb78f5ce8bb5e1529d60b-0430062023/original/Findex2021-22-Methodology.pdf | 200, application/pdf | 675157 | `42529b07b4086c99f30d9dad8de6a91951189df6013065e97bcc1436580d388b` |
| `MDB40.pdf` | https://documents1.worldbank.org/curated/en/099714008132436612/pdf/IDU-a9cf73b5-fcad-425a-a0dd-cc8f2f3331ce.pdf | 200, application/pdf | 996818 | `57ec3dfba3601b3a4a80441c09993a4bc897d4306fc081f8b83b851c788c26ec` |
| `catalog_5862.html` (metadata page) | https://microdata.worldbank.org/catalog/5862 | 200, text/html | 61392 | `efeb2731dcae2e4e0f3b762b8a5d8c5fb91eb6a779ffa5549ee21cf78513acb8` |
| `catalog_5862_study-description.html` (metadata page) | https://microdata.worldbank.org/catalog/5862/study-description | 200, text/html | 61419 | `f7ecc0716984b9621625ed030660f419f07e0f256495e7a754ba89253774de46` |

- **Download location:** all files are in `/tmp/claude-0/-home-user-Financial-inclusion-/794e1c72-3c18-5d8f-9569-397126d62800/scratchpad/addendum/dl/r1/`.
- **HTML hashes:** the HTML pages are generated per request, so their hashes identify this retrieval only.
- **No data files:** no "Get Microdata" link or data file was opened.

### How text was extracted

- Text came from `pdftotext` in `-layout`, `-raw` and `-bbox` modes.
- Every verbatim quote marked "(render-verified)" was also checked against a `pdftoppm` image of the page.

### Page numbering

- **Findex methodology PDF:** 27 PDF pages. It starts at printed page 3 ("Appendix A"), so printed page = PDF page + 2. PDF pages 26 and 27 carry no text.
- **MDB 40:** 56 PDF pages.
  - PDF pp. 1 to 6 are the cover, the rights page, the KNOMAD page and the contents with lists. These have no printed page numbers.
  - PDF pp. 7 to 9 are printed v to vii.
  - PDF p. 10 is blank.
  - From PDF p. 11 on, printed page = PDF page − 10 (printed pp. 1 to 42 = PDF pp. 11 to 52).
  - PDF pp. 53 to 55 are blank and PDF p. 56 is a plain back cover.

---

## Task A: Global Findex 2021 methodology

### A1. Table name and location

- **Label and title (render-verified):** "TABLE A.1", "Details of survey methodology for economies included in the Global Findex 2021 survey and database".
- **Where it starts:** the table starts on printed p. 6 (PDF p. 4) and runs to printed p. 17 (PDF p. 15).
- **Yemen row and footnotes:** both are on **printed p. 17, PDF p. 15**. The footnotes are printed once, at the end of the table, and apply to the whole table.
- **Footnote markers:** the column headers carry the markers "Region a", "Design effect b", "Margin of error c" and "Mode of interview d". The Yemen economy name carries marker "e".
- **Context:** Appendix A is titled "Survey Methodology" (printed p. 3, PDF p. 1). The PDF has no title page. Its running head is "The Global Findex Database 2021".

### A2. Yemen row, every column

Printed p. 17, PDF p. 15. Render-verified; line breaks inside cells are removed.

| Column header as printed | Yemen cell as printed |
|---|---|
| "Economy" | "Yemen, Rep" followed by superscript "e" (no full stop after "Rep" in the rendered page) |
| "Region" (marker a) | "MENA" |
| "Income group" | "Low" |
| "Data collection date" | "Nov 7, 2022–Jan 10, 2023" |
| "Number of interviews" | "1,000" |
| "Design effect" (marker b) | "1.9" |
| "Margin of error" (marker c) | "4.3" |
| "Mode of interview" (marker d) | "Face-to-face (HH)d" (set as "Face-" / "to-face" / "(HH)d") |
| "Languages" | "Arabic" |
| "Exclusions and other sampling details (samples are nationally representative unless otherwise noted)" | "Al Baydaa, Al Jawf, Mareb, Sadah, the Island of Socotra, and several districts in other governorates were excluded due to their small size, remoteness or security issues. The excluded areas represent approximately 23% of the population. In addition, due to the ongoing security situation, during field over one-fourth of the PSUs were replaced with a similar PSU in the same province." |

- **End date: yes, Table A.1 prints 10 January 2023.** The exact text is "Nov 7, 2022–Jan 10, 2023", with start date 7 November 2022 and end date 10 January 2023.
- **Wording as printed:** the cell says "during field" (not "during fieldwork") and "in the same province". Both are reproduced exactly.
- **Arithmetic check (not a source claim):** footnote c gives the formula √(0.25/N)*1.96*√(DE). With the printed N = 1,000 and DE = 1.9 it gives 0.0427, which rounds to the printed 4.3. The printed values are internally consistent.

### A3. Footnotes applying to the Yemen row

All are on printed p. 17, PDF p. 15, and all are render-verified.

- **Note:** "Note: EAP = East Asia and Pacific; ECA = Europe and Central Asia; LAC = Latin America and the Caribbean; MENA = Middle East and North Africa (referred to as MNA in Global Findex 2017); SAR = South Asia (referred to as SAS in Global Findex 2017); SSA = Sub-Saharan Africa."
- **a.** "Regions exclude high-income economies (HI) and may differ from common geographic usage."
- **b.** "The design effect calculation reflects the weights and does not incorporate the intraclass correlation coefficients because they vary by question. Design effect calculation: n*(sum of squared weights)/[(sum of weights)*(sum of weights)]."
- **c.** "The margin of error is calculated around a proportion at the 95 percent confidence level. The maximum margin of error was calculated assuming a reported percentage of 50 percent and takes into account the design effect. Margin of error calculation: √(0.25/N)*1.96*√(DE). Other errors that can affect survey validity include measurement error associated with the questionnaire, such as translation issues, and coverage error, where a part of the target population has a zero probability of being selected for the survey."
- **d.** "Hand-held (HH) data collection."
- **e.** (attached to "Yemen, Rep") "In these countries, data collection took place in 2022 due to COVID-19 related issues that restricted earlier access."

#### Related methodology text: weighting and clustering

- **Weighting**, printed p. 4, PDF p. 2, under "Data preparation": "Data weighting is used to ensure a nationally representative sample for each economy. Final weights consist of the base sampling weight, which corrects for unequal probability of selection based on household size, and the poststratification weight, which corrects for sampling and nonresponse error. Poststratification weights use economy-level population statistics on gender and age and, where reliable data are available, education or socioeconomic status. Table A.1 shows the data collection period, number of interviews, approximate design effect, and margin of error for each economy as well as sampling details where relevant."
- **Clustering in face-to-face samples**, printed p. 4, PDF p. 2: "In economies where face-to-face surveys are conducted, the first stage of sampling is the identification of primary sampling units. These units are stratified by population size, geography, or both, and clustering is achieved through one or more stages of sampling. Where population information is available, sample selection is based on probabilities proportional to population size; otherwise, simple random sampling is used."
- **What this means for the design effect:** footnote b and this passage, read together, mean that the printed 1.9 is a weighting-only design effect for a clustered face-to-face sample. The document gives no clustering-inclusive design effect for Yemen, so any larger figure is NOT VERIFIED from this source.

#### Other footnote on Yemen in the same PDF (outside Table A.1)

- **Table B.1 Yemen row:** "TABLE B.1", "Indicator table", "ACCOUNT OWNERSHIP, 2021", printed p. 21, PDF p. 19, render-verified. The row reads "Yemen" with superscript b, then "12", "5", "7". The columns are "Adults with an account (%)", "Women with an account (%)" and "Poor adults with an account (%)a".
- **Table B.1 notes:**
  - "Source: Global Findex Database 2021."
  - "a. Adults in the poorest 40 percent of households. Data are based on household income quintiles."
  - "b. In these countries, data collection took place in 2022 due to COVID-19 related issues that restricted earlier access."

#### Release timing

Printed p. 4, PDF p. 2: "In 2021, however, phone surveys were not a viable option in 16 economies that had been part of previous Global Findex surveys because of low mobile phone ownership and surveying restrictions. Data for 16 of these economies, including Mexico and Vietnam, were collected through face-to-face interviews in 2022 and were released in early 2023."

### A4. Excluded population for Yemen

- **Wording and percentage:** the only Yemen-specific text in the PDF is the Table A.1 cell quoted in A2. The percentage is "approximately 23% of the population".
  - The excluded areas are "Al Baydaa, Al Jawf, Mareb, Sadah, the Island of Socotra, and several districts in other governorates".
  - The reasons given are "due to their small size, remoteness or security issues".
- **Separate statement on PSU replacement:** "due to the ongoing security situation, during field over one-fourth of the PSUs were replaced with a similar PSU in the same province."
- **What the 23% is a share of:** the document says "of the population". It does not say "adult population" or "target population", and it does not name the population source or year behind the 23%. Any narrower reading is NOT VERIFIED.
- **General statements in the Appendix A text:**
  - Target population, printed p. 3, PDF p. 1: "The target population is the entire civilian, noninstitutionalized population age 15 and up."
  - Samples, printed p. 4, PDF p. 2: "All samples are probability-based and nationally representative of the resident adult population."
  - Table column header: "(samples are nationally representative unless otherwise noted)".
- **Coverage error:** footnote c defines it as "coverage error, where a part of the target population has a zero probability of being selected for the survey."
- **No other mention of Yemen:** the word "Yemen" appears nowhere else in the methodology PDF's text layer apart from Table A.1 and Table B.1. Map A.1 on printed p. 3 is a raster image and was not examined for Yemen. It covers economies that switched to phone surveys in 2021, so it is not relevant to Yemen's 2022–23 face-to-face survey.

### A5. Microdata Library catalog metadata (study 5862)

- **What was fetched:** both URLs returned the same study-description content; only a form-action URL and a CSS class differ. The page has no separate "Data Collection" tab URL. Its "Data collection" section is inside the study-description page. Metadata only: no data file and no "Get Microdata" link was opened.
- **Page details:**
  - Page `<title>`: "Yemen, Rep. - Global Financial Inclusion (Global Findex) Database 2021"
  - Heading: "Global Financial Inclusion (Global Findex) Database 2021"; subtitle "Yemen, Rep., 2022 - 2023"
  - "Survey ID number YEM_2022_FINDEX_v01_M"
- **"Dates of Data Collection" table:** "Start" = "2022-11-07"; "End" = "2023-01-09".
- **"Data Collection Mode":** "Face-to-face [f2f]"
- **"Data Collection Notes":** "Data was collected in the following language(s): Arabic"
- **"Geographic Coverage"** (identical to the Table A.1 cell): "Al Baydaa, Al Jawf, Mareb, Sadah, the Island of Socotra, and several districts in other governorates were excluded due to their small size, remoteness or security issues. The excluded areas represent approximately 23% of the population. In addition, due to the ongoing security situation, during field over one-fourth of the PSUs were replaced with a similar PSU in the same province."
- **Sample size:** "Sample size for Yemen, Rep. is 1000."
- **Version:**
  - "Version Date 2023-05-19"
  - "Version Notes This is the second update (May 2023) to the microdata originally released in Oct 2022 with the first update in Dec 2022. This includes 16 new countries that were surveyed in 2022 (... Vietnam, Yemen, Rep.)."
- **Metadata dates:** "Date of Metadata Production 2023-05-23". The embedded JSON-LD has "dateCreated": "2023-06-08T14:56:41-04:00" and "temporalCoverage": "2022/2023".
- **"Estimates of Sampling Error":** "Estimates of standard errors (which account for sampling error) vary by country and indicator. For country-specific margins of error, please refer to the Methodology section and corresponding table in Demirgüç-Kunt, Asli, Leora Klapper, Dorothe Singer, Saniya Ansar. 2022. The Global Findex Database 2021: ..."
- **Producers:**
  - Primary investigator: "Development Research Group, Finance and Private Sector Development Unit", "World Bank".
  - Producer: "Gallup, Inc.", "Carried out the survey in association with its annual Gallup World Poll."

**Date check, confirmed:** the catalog says **9 January 2023** (2023-01-09) and the methodology Table A.1 says **10 January 2023** ("Jan 10, 2023"). Both start on 7 November 2022. Neither source explains the one-day difference. Which date is correct is NOT VERIFIED.

---

## Task B: Migration and Development Brief 40 (June 2024)

### B4. Title, authors and date

- **Cover (PDF p. 1, render-verified):**
  - Title: "Remittances Slowed in 2023, Expected to Grow Faster in 2024"
  - Series and date: "Migration and Development Brief 40", "June 2024"
  - Logos: WORLD BANK GROUP and KNOMAD.
- **Suggested citation (rights page, PDF p. 2, no printed page number):** "Attribution – Please cite the work as follows: Dilip Ratha, Vandana Chandra, Eung Ju Kim, Sonia Plaza, and Akhtar Mahmood. 2024. “Remittances Slowed in 2023, Expected to Grow Faster in 2024.” World Bank, Washington, DC.” License: Creative Commons Attribution CC BY 3.0 IGO." The stray closing quotation mark after "DC." is in the source.
- **Rights page (PDF p. 2):** "© 2024 International Bank for Reconstruction and Development/The World Bank." and "This work was produced under the Global Knowledge Partnership on Migration and Development (KNOMAD)."
- **Team (Acknowledgments, printed p. v, PDF p. 7):** "This brief was prepared by Dilip Ratha (lead author), Vandana Chandra, Eung Ju Kim, and Akhtar Mahmood of the Social Protection and Jobs Global Practice, and Sonia Plaza of the Finance, Competitiveness, and Innovation Global Practice."
- **PDF metadata:** CreationDate 2024-07-01, ModDate 2024-08-13. These are file metadata, not the publication date.

### B1. Figure A.4.2

- **Title (render-verified):** "Figure A.4.2 Top Remittance Recipients in the Middle East and North Africa, 2023"
- **Location:** **printed p. 29, PDF p. 39**.
  - It sits in "Appendix A. Regional Trends in Migration and Remittance Flows" (starts printed p. 15, PDF p. 25), section "A.4 Middle East and North Africa" (starts printed p. 27, PDF p. 37). The brief says "Appendix", not "Annex".
  - The List of Figures (PDF p. 6) gives page 29.
- **Panel subtitles:** "($ billion, 2023)*" and "(Percentage of GDP, 2023)*".
- **Panel a ($ billion, 2023), as printed (render-verified and text layer):**

  | Economy | $ billion, 2023 |
  |---|---|
  | Egypt, Arab Rep. | 19.5 |
  | Morocco | 11.8 |
  | Lebanon | 6.0 |
  | Jordan | 4.5 |
  | **Yemen, Rep.** | **3.8** |
  | West Bank and Gaza | 3.5 |
  | Tunisia | 2.7 |
  | Algeria | 1.9 |
  | Djibouti | 0.1 |

- **Panel b (Percentage of GDP, 2023), as printed:**

  | Economy | % of GDP, 2023 |
  |---|---|
  | Lebanon | 27.5 |
  | West Bank and Gaza | 18.8 |
  | Jordan | 8.9 |
  | Morocco | 8.2 |
  | Tunisia | 5.2 |
  | Egypt, Arab Rep. | 5.0 |
  | Djibouti | 1.4 |
  | Algeria | 0.8 |
  | Iraq | 0.3 |

  Yemen does not appear in panel b.
- **Pairing check:** the PDF text layer lists the panel a values in the order "19.5 11.8 6.0 4.5 3.8 3.5 2.7 1.9 0.1" and the labels in the order "Egypt, Arab Rep. Morocco Lebanon Jordan Yemen, Rep. West Bank and Gaza Tunisia Algeria Djibouti". A 300 dpi render confirms that the label "Yemen, Rep." sits under the bar labelled 3.8.

### B2. Note to Figure A.4.2

Printed p. 29, PDF p. 39, render-verified:

- "Sources: World Bank/KNOMAD staff ; World Development Indicators; IMF Balance of Payments Statistics." The source prints "staff ;" with no following word.
- "Note: GDP = gross domestic product."
- "*The Islamic Republic of Iran, the Syrian Arab Republic, and the Republic of Yemen are excluded due to data availability."

**Does the note say Yemen is excluded "due to data availability"? Yes, verbatim.** But the asterisk is attached to both panel subtitles, and panel a still plots "Yemen, Rep." at 3.8 ($ billion, 2023).

- **What the printed figure shows:** Yemen is absent only from panel b.
- **What is NOT VERIFIED:**
  - whether the note was meant to apply only to panel b (for example, because of missing GDP data);
  - whether panel a's Yemen bar is an error.

  The brief gives no explanation.
- **How the note can be cited:** it supports, at most, the statement that this brief's MENA figure note prints Yemen as excluded "due to data availability". It does not support the statement that the brief contains no 2023 Yemen remittance value: panel a prints 3.8 for "Yemen, Rep.".
- **Comparable note elsewhere in the brief, for contrast:** printed p. 36, PDF p. 46, Figure A.6.2: "*South Sudan is excluded due to issues related to data validity."

### B3. Every other mention of Yemen in the brief

The `-raw` text layer of all 56 PDF pages was searched for "Yemen" (spacing-tolerant), "Sana", "Aden" and "Houthi". The only Yemen mentions are the three below; the other terms returned nothing. All figures in the brief are vector graphics with a text layer; the only raster images are the cover photo and logos.

1. **Figure A.4.2, printed p. 29, PDF p. 39:** the panel a label "Yemen, Rep." (3.8) and the note quoted in B2.
2. **Printed p. 30, PDF p. 40, "Migration trends" paragraph:** "According to the UNHCR, as of April 2024, Egypt hosted 575,000 registered refugees and asylum seekers from 61 countries, nearly double the number from a year previous, due to major conflicts across its borders. The main countries of origin for migrants in Egypt are Sudan, the Syrian Arab Republic, the Republic of Yemen, and Libya, reflecting political crises in the Middle East and North Africa."
3. **Figure A.4.4, printed p. 31, PDF p. 41:** "Figure A.4.4 Sending Money within the Region is Less Expensive than Sending Money from Outside".
   - Panel "a. Five Least Expensive Corridors" includes the corridor label "Saudi Arabia to Yemen, Rep." with bars for "2022Q4" and "2023Q4".
   - Source: "Source: World Bank Remittance Prices Worldwide database."
   - Note: "Note: Cost of sending $200 or equivalent."
   - The bars carry no printed values, so no cost figure for this corridor can be quoted from the brief (NOT VERIFIED; bar heights were not estimated).

---

## Not verified

- **Correct end date:** whether 9 or 10 January 2023 is the true end of Yemen fieldwork. The two World Bank sources disagree, and neither gives a reason.
- **Basis of the 23% figure:** the population source and year behind "approximately 23% of the population". The document does not give them.
- **Yemen design effect including clustering:** footnote b excludes intraclass correlation, and no such value is published in the document.
- **Intended scope of the MDB 40 Figure A.4.2 note:** whether it was meant for panel b only, and whether panel a's Yemen value of 3.8 is intended or an error.
- **Saudi Arabia to Yemen corridor cost:** the bars in Figure A.4.4 have no printed values.
- **Map A.1 in the Findex PDF:** a raster image, not examined; it is not relevant to Yemen.
