# V5 verification read: cash, SMEPS, IFAD, RPW, FATF

Read date: 2026-10-11. Read-only: nothing under <repository> was modified.
Downloads: `<session scratchpad>/v5/dl/V5/` (new empty folder).
Tools: curl (browser User-Agent for the sites that needed one), `pdftotext -layout` and raw, `pdftoppm` for figures, `openpyxl` read-only, all Python via `python3 -I`. Scripts and text extracts are in `.../scratchpad/v5/work/` (outside the download folder).

SHA-256 of what was read:

| file | sha256 |
|---|---|
| A1.html | 215a60f659953baa91a4f0d23ca1eb2b67c1ac6ea43f12ffa35888f3d08cf06d |
| A2.html | f48823f8bc7937138fd665391f854e9f85f787230e3df4ebea6c9ea5c4945184 |
| B_report.html (ReliefWeb landing page) | 0762e9c5e7fe8404347f6ec53a91c9cf24f07d6470e1e8a25641621f67db514b |
| B.pdf (1,112,784 bytes, 15 pp) | recorded in work/sha256.txt |
| C.pdf (SAM multiplier, 42 PDF pp) | a3057de2829e43a8667f02fdb9bc49a22df3e5048f45a58fafe05db47301b32f |
| D.pdf (Cash Duration, 28 PDF pp) | 5ede6b063ddcd90c7a2ceec8132aa0a60754eb8921b01cb0387bd7f0fe85af29 |
| E.pdf (SMEPS, 30 PDF pp, spreads) | cc52b202bbf0d64bb53b241d66f00ae159202fe1505ad3300e2fffd3d71d285c |
| F.pdf (IFAD CPE, 136 PDF pp) | a5a9cfd3380264541c5debf5cc4dc93581e261434f314b98edaffcdbf0c5f687 |
| G.xlsx (50,780,339 bytes) | f1d7265b1856d61812c158d3d03fae686dbff58735deabe016a6bfe23482d2a8 |

Page convention: "PDF p." is the page number in the PDF viewer. "printed p." is the number printed on the page.

---

## Summary table

| Item | Result |
|---|---|
| A1 UNICEF 2 Oct 2024 | CONFIRMED, with wording notes (62.5 M is "will be disbursed", i.e. planned in that release) |
| A2 UNICEF 7 Dec 2024 | CONFIRMED that the 19th cycle starts 11 Dec 2024 and "marks the end of the current UCT program". NO US$62.5 million anywhere in A2. |
| B CCY "Yemen Under Pressure" | CONFIRMED on PDF p.8 = printed p.7. DIFFERENCES: page number, "notes", "Eid al-Adha 2026", and the single-KII scope (below) |
| C1 40% debt repayment | CONFIRMED, printed p.15 (PDF p.16) and Table 3 on printed p.16 (PDF p.17). Base is the pooled surveyed beneficiary HHs, n = 500 |
| C2 credit sentence | CONFIRMED: Ad-Dali 11 of 21, Ja'ar 10 of 21 (printed p.31, PDF p.32) |
| D Cash duration | CONFIRMED. Debts paid off 40% (3-month) vs 60% (6-month); Increased income 41% vs 29%. Area is Ja'ar sub-district (Abyan) only, not "areas administered from Aden" |
| E SMEPS | CONFIRMED on printed p.9 (PDF p.5). Cover calls it the "2024 SMEPS EXECUTIVE REPORT", not "Annual Report" |
| F IFAD CPE | CONFIRMED on printed p.40 and p.33. Notes on Raymah bases and the Southern Governorates |
| G RPW | CONFIRMED: USA 12 quotes, 3.92% at 200, 2.30% at 500. SAU 2.70%. UAE 7.53% |
| H FATF | NOT READ. fatf-gafi.org returned a Cloudflare challenge ("Just a moment...", HTTP 403) |

---

## A. UNICEF Yemen press releases

### A1. 2 October 2024

URL read: https://www.unicef.org/yemen/press-releases/143-million-vulnerable-families-supported-cash-assistance-across-yemen
Page metadata: `article:published_time` 2024-10-02T08:46:34+0000; `article:modified_time` 2024-10-24T10:17:41+0000. Page shows "Press release", "02 October 2024".

Headline: "1.43 million vulnerable families supported with cash assistance across Yemen". Sub-headline: "Unconditional cash assistance provides a lifeline for families needing urgent support".

Verbatim paragraphs:

- Dateline paragraph: "Sana'a, 02 October 2024 – More than 1.43 million families received cash assistance as part of the ongoing Unconditional Cash Transfer (UCT) programme implemented across Yemen."
- Funding, implementation, amount: "Funded by the World Bank and implemented by UNICEF in partnership with the Social Fund for Development (SFD), approximately US$ 62.5 million will be disbursed in the current payment cycle through mid-October to provide a safety net for around 9.2 million people from over 1.43 million families, considered some of the poorest and the most vulnerable, including households headed by females or with people with disabilities."
- Channels: "The assistance provided at payment sites, through mobile teams and home outreach services, or as part of the e-wallet pilot scheme, is often the only source of income for many families. Together with a further distribution in December, the Cash Transfer is expected to fulfill their most immediate and urgent needs such as food and healthcare costs, as well as paying back debts related to purchasing food and covering medical costs."
- Cycle: "The current 18th payment cycle is the first nationwide unconditional cash transfer in Yemen this year. Households will collect their base benefit with an additional 50 per cent."
- Programme start: "To sustain the lives of the most vulnerable families, UNICEF has been providing cash assistance under the UCT programme since 2017."

Findings:
- 1.43 million families: stated twice, as "More than 1.43 million families received" (past tense, first sentence) and "over 1.43 million families" (with "around 9.2 million people").
- Cycle: the 18th payment cycle. Funder: World Bank. Implementer: UNICEF in partnership with SFD. The channels are exactly: payment sites, mobile teams, home outreach services, e-wallet pilot scheme.
- US$62.5 million is "approximately", is for "the current payment cycle through mid-October", and the verb is "will be disbursed", so at release date it is a planned amount for cycle 18, not a reported disbursement. The release has no disbursed-to-date figure.
- The release mixes tenses: "received" (headline and first sentence) against "will be disbursed" and "Households will collect". Treat 1.43 million as the families covered by the cycle, not a verified count of families paid.
- The "further distribution in December" is not numbered in A1. A2 numbers it as the 19th cycle.

### A2. 7 December 2024

URL read: https://www.unicef.org/yemen/press-releases/unicef-and-partners-launch-19th-payment-cycle-current-unconditional-cash-transfer
Title on page: "UNICEF and partners launch the 19th Payment Cycle of the current Unconditional Cash Transfer Project in Yemen". Date "07 December 2024". Metadata: published 2024-12-07T20:17:52+0000; modified 2024-12-08T11:29:16+0000.

Verbatim:
- "Sana'a/Aden, Yemen – 07 December 2024 – UNICEF Yemen and its partners are launching the 19th payment cycle of the Unconditional Cash Transfer (UCT) project. Starting 11 December 2024 in the fixed payment sites, over 1.43 million vulnerable families will receive cash assistance to help meet their basic needs."
- "Since its inception in 2017, the UCT project has been critical financial support to nearly 9 million people, acting as a lifeline amidst Yemen's ongoing humanitarian crisis. The program's achievements are a testament to the unwavering commitment of donors, partners, and stakeholders. The 19th payment cycle marks the end of the current UCT program. UNICEF and its partners are currently working on developing new cash-based initiatives to better meet the evolving needs of Yemen's most vulnerable households."
- Quote of Peter Hawkins: "The success of the UCT project is the result of joint efforts from international partners and central and local authorities." And: "UNICEF remains committed to serve and protect the children in Yemen and continues to work with the authorities on the development of other cash-based programmes that will positively impact the lives of children and their families."

Findings:
- Start date: the text says "Starting 11 December 2024 in the fixed payment sites". It is a stated start date, not worded as "expected". It applies to the fixed payment sites only. The future "will receive" is a plan.
- Ends the programme in its current form: YES, in these words: "The 19th payment cycle marks the end of the current UCT program." New initiatives are "being developed", with nothing committed in the release.
- Amount: NOT FOUND. A2 contains no US$ amount at all (grep "62.5" returns 0). The US$62.5 million appears only in A1 and is tied to the 18th cycle, as a planned amount.
- 1.43 million is repeated for cycle 19 as "over 1.43 million vulnerable families will receive": planned, same figure as cycle 18.
- Cumulative: "nearly 9 million people" since 2017.

---

## B. CCY, "Yemen Under Pressure: How the Iran-US Conflict Is Disrupting Trade, Prices, and Cash Access", May 2026

Landing page read: https://reliefweb.int/report/yemen/yemen-under-pressure-how-iran-us-conflict-disrupting-trade-prices-and-cash-access-may-2026 (ReliefWeb: Format Analysis; "Posted 29 Jul 2026", "Originally published 29 Jul 2026"; sources include ACTED, CCY, DRC and others; PDF 1.06 MB).
PDF read: https://reliefweb.int/attachments/329ba888-6c77-46c3-b920-e0ca0d5ab982/Economic%20Impact%20of%20Iran-US%20War%20on%20Yemen_May%202026.pdf (HTTP 200, 15 PDF pages; metadata created 10 June 2026).
Cover (rendered): "Yemen Under Pressure: How the Iran-US Conflict Is Disrupting Trade, Prices, and Cash Access", "May 2026", logos CCY, Crisis Analysis MENA/Europe, EU Civil Protection and Humanitarian Aid.

Page mapping: the cover is unnumbered. Printed page = PDF page - 1. The text you called "p.8" is PDF p.8 = printed p.7 (footnotes 31-32 are on the same page). Figure 2 (exchange rate) sits above it.

Verbatim (PDF p.8, printed p.7, section "Burgeoning liquidity constraints and their possible effects on MPCA programming"):

"The liquidity crisis temporarily disrupted MPCA programs during the holiday period when demand for rials increased, with beneficiaries in rural areas most affected. Most cash assistance is disbursed through microfinance banks via vouchers that beneficiaries can exchange at local financial service provider agents. However, during Ramadan and Eid al-Adha, agents often lacked sufficient liquidity to meet demand, resulting in wait times of four to five hours, with some beneficiaries reportedly waiting from morning until dusk.[31] The situation was further complicated by releasing funds only in denominations of YER 100 and 200. To mitigate these issues, organizations considered deploying mobile distribution teams, though at a significantly higher operational cost. Following the high demand period, liquidity issues for MPCA programs have decreased but humanitarian and aid organizations continue to monitor currency availability closely. Notably, an e-wallet pilot was also undertaken, with funds disbursement facing no issues or delays, suggesting that it could be used as a mitigation tool in the event of largescale liquidity issues.[32]"

Footnotes, verbatim: "31 KII with MPCA program manager April 2026" and "32 ibid."

Related caution, printed p.13 (PDF p.14, Conclusion and Outlook): "Early indications from e-wallet pilots are encouraging, but it remains unclear whether digital disbursements will ultimately translate into reliable access to physical cash in a predominantly cash-based economy where only 12% of adults hold a bank account."

Findings and differences:
1. One interview or not: footnote 31 is "KII with MPCA program manager April 2026" and footnote 32 is "ibid.", so both markers cite the same single key informant interview (one MPCA programme manager, April 2026). Two points of scope: (a) footnote 31 sits after the "four to five hours ... dusk" sentence and footnote 32 after the e-wallet sentence. The "microfinance banks via vouchers" sentence, the "YER 100 and 200" sentence and the mobile-teams sentence carry no footnote of their own. The page does not say they come from the same KII, although they sit between the two markers. (b) Whether "program manager" is one person or one organisation is not stated, and the programme, agency and governorates are not named on this page.
2. "Four to five hours": the source writes "four to five hours" (words), "reportedly" for the morning-to-dusk waits.
3. "Notes only in YER 100 and 200": the source says "releasing funds only in denominations of YER 100 and 200". It does not use the word "notes" and does not say who released the funds. Use "denominations".
4. "Ramadan and Eid al-Adha 2026": the sentence says "during Ramadan and Eid al-Adha" with no year. The wider report puts the rial liquidity crisis from late February to mid-May 2026 (Key Takeaways, printed p.1) and the interview is dated April 2026. My own calendar check, not from the document: Eid al-Adha 2026 falls around 27 May 2026, after the April 2026 interview and after the report's mid-May cut-off. The source's "Eid al-Adha" therefore cannot be an observation of Eid al-Adha 2026 on that interview date. Elsewhere the report writes "the Eid and Ramadan period" (printed p.6) and "holiday periods (Ramadan and Eid)" (printed p.1). Safer public wording: "the Ramadan and Eid holiday period", attributed to a programme manager interviewed in April 2026.
5. Geography: the report's liquidity crisis is framed as "IRG areas" (Key Takeaways, printed p.1). The MPCA paragraph itself does not name an area.
6. E-wallet: "an e-wallet pilot was also undertaken, with funds disbursement facing no issues or delays". This is the informant's account. The report itself says it is unclear whether digital disbursement gives access to physical cash (printed p.13).
7. ReliefWeb shows "Posted 29 Jul 2026" while the document is dated May 2026 (PDF created 10 June 2026). Cite the document as May 2026.

---

## C. CCY multiplier study (SAM), 2024

URL read: https://www.calpnetwork.org/wp-content/uploads/2024/11/SAM_Multiplie-Effect-of-Cash-Study.pdf (HTTP 200; PDF metadata created 1 Aug 2024; 42 PDF pages). Printed page = PDF page - 1 (cover and unnumbered page 1; "Executive Summary" is PDF p.2 = printed p.1).

### C1. Debt repayment, 40%

The sentence is on PDF p.16 = printed p.15, and Table 3 repeats it on PDF p.17 = printed p.16. So "p.16" matches Table 3 if printed pages are meant, and the sentence if PDF pages are meant.

Verbatim (printed p.15, PDF p.16): "The most common items reported as regular expenditures were food (100% of HHs), hygiene items (85%), fuel (50%), transport (52%) and debt repayment (40%).[48] In terms of median YER expenditure, HHs spent the most on food (YER 120,000) and debt repayment (YER 52,500) (see Table 3)."

Table 3 (printed p.16, PDF p.17), caption verbatim: "Table 3. Median amount of regular expenditure 30 days prior to data collection (adjusted to a HH of 7 people) per type in YER, % of HH reporting type of expenditure and % of average regular expenditure." Row "Debt | 40% | YER 52,500 | 28%". Column header: "% of HH reporting regular expenditure category".

Related verbatim (printed p.14, PDF p.15): "HHs that received MPCA within 30 days of the interview were more likely to report spending money on debt repayment in the same period. Specifically, about 47% of HHs that received MPCA reported debt repayment compared to approximately 30% of HHs that did not receive MPCA within 30 days of the interview."

Base (from printed pp.7-8):
- "In January 2024, the CCY conducted a HH survey to assess HH income and expenditure patterns". Regular expenditure refers to "regular purchasing behavior 30 days prior to data collection".
- Eligibility: "Beneficiary HHs were eligible for the study if they received at least two rounds of MPCA between July and December 2023, with the last distribution received in October, November, or December 2023. Each HH received 240,000 Yemeni rials (YER) (USD 155.93) per MPCA distribution".
- Sample: "A statistically representative sample of these beneficiaries was drawn, which required a sample of 291 HHs in Ad Dali sub-district and 209 HH in Ja'ar sub-district". Figure 2 (rendered) bars sum to 291 (Ad-Dali) and 209 (Ja'ar), so n = 500. Footnote 37: "95% confidence interval; 5% margin of error". Footnote 38: 8 duplicate surveys deleted in Ad Dali. Footnote 52: "99.8% of the total sample of households" (reported that MPCA allowed higher quantity and quality).
- Table 3 is not split by sub-district, so 40% is of the pooled beneficiary households surveyed (n = 500, by my reading of Figure 2 and the sample sentence). The page does not print "n = 500" next to the 40%.

Differences and cautions:
- The source word is "regular expenditures"/"debt repayment (40%)" of surveyed HHs, all drawn from beneficiaries of the CCY MPCA in two sub-districts (Ad-Dali sub-district, Ad-Dali governorate; Ja'ar sub-district, Abyan governorate). Not Yemen-wide and not all "recipient households" nationally. The 47% / 30% split shows some sampled HHs had not received MPCA in the previous 30 days, so "40%" is not "of households that spent the MPCA on debt".
- Sample-level representativeness is stated for the beneficiaries in the selected villages ("Villages and cities that received the most cash assistance ... that were accessible by partners"), not for Yemen.
- Internal inconsistency in the source: printed p.32 (Discussion) says "HH data was collected in mid-January 2023 and KIIs was conducted in early-to-mid February 2023", while printed p.7 says January 2024 and the MPCA rounds ran to December 2023. The 2023 is almost certainly a typo, but it is the document's own wording.
- Transport is listed as 52% and fuel 50% in the sentence order (fuel before transport), same values in Table 3.

### C2. Business owners and customer credit

Printed p.31 = PDF p.32, section "Qualitative Insights from Business Owners", paragraph headed "MPCA facilitated customer debt repayment."

Verbatim: "In Ad-Dali, 11 of 21[80] (52%) of interviewed business owners reported that the number of customers buying goods or services on credit decreased when cash assistance was distributed. Similarly, 10 of 21 (48%) interviewed business owners in Ja'ar said that the number of customers buying goods or services on credit decreased when cash assistance was distributed."

Footnote 80, verbatim: "Four business owners responded with "don't know", which is why the total number of responses is 21 instead of 25."

Which is which: Ad-Dali sub-district = 11 of 21 (52%); Ja'ar sub-district = 10 of 21 (48%). Interviewed base: 25 KIIs in Ad-Dali and 21 in Ja'ar (printed p.8); Ad-Dali's response base is 21 after four "don't know". Both are sub-districts in the paper, and the paper calls them sub-districts, not districts.

Neighbouring statements, verbatim, in case wanted: "In Ad-Dali, 7 of 15[81] (47%) interviewed business owners said that debt repayments positively impacted their ability to operate their business; specifically, greater liquidity allowed them to extend additional credit lines to customers. In Ja'ar, 6 of 21 (29%) business owners observed that customers receiving cash assistance more often pay back their debt from buying goods and services from businesses on credit." Footnote 81: "Ten business owners responded with "don't know", which is why the total number of responses is 15 instead of 25."

Caution: business-owner counts are small (21 and 21), qualitative key informants, self-reported.

---

## D. CCY, "The More the Merrier? Comparing Outcomes and Preferences for Three- vs. Six-Month Cash Transfers" (2026)

URL read: https://www.calpnetwork.org/gf-uploads/2026/06/Cash-Duration-Report_CCY_2026.06.22.pdf (HTTP 200; 28 PDF pages; PDF created 6 May 2026, modified 24 June 2026). The cover (rendered) shows title, Crisis Analysis MENA/Europe, EU Civil Protection and Humanitarian Aid, CCY. No date is printed on the cover. The only dates are the URL path (2026/06/22) and PDF metadata. Printed page = PDF page - 1.

Where: Figure 1 is on PDF p.7 = printed p.6. The text answering it is on PDF p.8 = printed p.7.

Verbatim, printed p.7: "The first descriptive indicator analyzed is "what aspect of your HH economy improved the most" at the endline. The results are shown in Figure 1. The most common responses were "Debts are paid off" and "Increased Income." The latter was more frequently reported by three-month recipients and the former more often by six-month recipients."

Figure 1 caption, verbatim (printed p.6): "Figure 1. What aspect of your HH economy improved the most at the endline? Only one answer option could be selected." Y axis "% of Recipients".

Figure 1 values (read from the rendered chart, data labels):

| answer | 3-month | 6-month |
|---|---|---|
| Debts are paid off | 40% | 60% |
| Improved education | 3% | 0% |
| Improved health | 10% | 11% |
| Improved shelter | 1% | 0% |
| Increased income | 41% | 29% |
| Managed to save money for future | 5% | 0% |

Both columns sum to 100%.

Answer: YES. "Debts are paid off" is one of the two most common answers (with "Increased Income"), and it is more frequent among six-month recipients (60% vs 40%). Increased income is more frequent among three-month recipients (41% vs 29%).

Base and area (printed p.6): "Data for three-month recipients in the most recent endline dataset was only available for HHs located in Ja'ar subdistrict (Abyan governorate); therefore, comparisons are calculated using only the three- and six-month recipient HHs located in the Ja'ar subdistrict." Sample: "only cash recipients with endline assessments conducted in November 2025 are included in the analysis. Therefore, the sample for the descriptive data analysis comprises 45 HHs that received six-month distributions and 107 HHs that received three-month distributions." Dataset context: 107 three-month and 167 six-month HHs in Ja'ar before the November 2025 restriction; endline surveys of six-month HHs ran 29 Sep 2024 to 26 Nov 2025 and of three-month HHs 20 to 30 Nov 2025.

Differences and cautions:
- Area: NOT "areas administered from Aden" in general. The Figure 1 comparison covers one sub-district only, Ja'ar, Abyan governorate (n = 45 and n = 107). The paper elsewhere calls Abyan and Taizz "the IRG-controlled areas" (page with the food security models) and the wider study also uses DfA-controlled areas (Saada, a Hodeidah sub-district) in other analyses. Say "Ja'ar sub-district, Abyan governorate" and, if needed, attribute "IRG-controlled" to the paper.
- No significance test is reported for Figure 1: the text calls it a "descriptive indicator". (The statistical test on printed p.7 is for another indicator, coping with shocks: mean difference 0.178, 95% CI 0.002 to 0.354, p = 0.047.)
- The authors' own reading: "three months of cash transfers may not be sufficient to mostly or fully repay debt ... more debt can be paid off with three more months of additional income". Single-answer question, self-reported, perception of "improved the most".
- The report's headline conclusion is the opposite emphasis: "three monthly transfers achieved the most measurable household welfare gains" (Key findings, printed p.1). Keep the debt result as one descriptive indicator.

---

## E. SMEPS 2024 report

URL read: https://smeps.org.ye/upfiles/posts/SMEPS_File_08-10-2025-44011.pdf (HTTP 200; 30 PDF pages; metadata created 4 Oct 2025, Adobe InDesign). Pages are two-page spreads: PDF p.5 holds printed pp.8-9, the table is on the right half, printed p.9.

Cover (rendered): "2024 SMEPS EXECUTIVE REPORT". The words "Annual Report" do not appear anywhere in the text (grep returns nothing). Cite it as the "SMEPS 2024 Executive Report".

Printed p.9, section "KEY INDICATORS", table (verbatim row labels and 2024 column):
- "Number of MSMEs supported disaggregated by type: Total Achieved #" - Year 2021 4,123; 2022 10,622; 2023 8,598; **2024 8,217**; Total 2021-2024 31,560; Target 32,000.
- "Smallholder producers & micro supply chain enablers" - 3,059 / 9,255 / 7,108 / **7,257**.
- "SMEs and BAs" - 1,064 / 1,367 / 1,490 / **960**.
- "% of Females" (cumulative only): 41% against a 40% target. "# of Indirect Beneficiaries": 24,738 / 63,732 / 51,588 / 49,302; 189,360 vs 192,000.
- Arithmetic: 7,257 + 960 = 8,217, so the two type rows partition the total.

Also verbatim, executive summary, printed p.6 (PDF p.4): "In 2024, SMEPS disbursed an amount of $22,865,322 demonstrating remarkable success by supporting 8,217 MSMEs, of which 44% were female-owned, leading to the creation and sustainability of 24,088 jobs, with women representing 16% of the workforce."

Findings and differences:
- 8,217 MSMEs supported in 2024 and 7,257 "Smallholder producers & micro supply chain enablers": CONFIRMED, as a disaggregation by type (the report does not use the words "of which" for the 7,257; the table lists type rows beneath the total).
- "BAs" is not defined anywhere in the document text (grep). Do not expand it.
- Title: cover says Executive Report, not Annual Report.
- The executive summary's "44% were female-owned" for 2024 has no 2024 counterpart in the table: the table shows only the cumulative 41% for 2021-2024.
- "Used Funds in 2024: $22.8 Million" in the Financial Snapshot (printed p.9) against $22,865,322 in the text (which rounds to $22.9 million). Use the exact figure and its page.
- Other 2024 results on the same page, if needed: financial services accessed 19% of MSMEs supported (2024); incomes increased 49%; productivity increased 35%.

---

## F. IFAD Independent Office of Evaluation, Republic of Yemen Country Programme Evaluation

URL read: https://webapps.ifad.org/members/ec/69/docs/EC-2011-69-W-P-4-Rev-1.pdf (HTTP 200; 136 PDF pages; metadata title "Projects Evaluation", created 6 Oct 2011).

Cover page (PDF p.1), verbatim: "Document: EC 2011/69/W.P.4/Rev.1", "Date: 6 October 2011", "Distribution: Public", "Original: English", "Republic of Yemen Country Programme Evaluation", "Evaluation Committee - Sixty-ninth Session Rome, 7 October 2011", "For: Review". Contact: "Director, Independent Office of Evaluation of IFAD". Inner title page (PDF p.2): "Document of the International Fund for Agricultural Development", "Republic of Yemen", "Country Programme Evaluation", "23 September, 2011". So two dates: 6 October 2011 on the Rev.1 cover and 23 September 2011 on the title page.

Page mapping: printed p.40 = PDF p.57; printed p.33 = PDF p.50; printed p.3 = PDF p.20.

### Paras 176-177 (printed p.40, PDF p.57)

Verbatim:
"176. In the last fifteen years the effectiveness of IFAD financed projects in the provision of rural finance has been poor, though improvements are now apparent in Dhamar and Al-Dhala. Targets with respect to the number of loans and the amount of loans to be disbursed were not achieved in any of the completed IFAD projects. The projects disbursed loans valued at US$4.165 million (31 per cent of the total amount of funds provided for lines of credit worth US$13.37 million) to 3,723 clients (6 per cent of the planned targets of 58,867 clients in terms of outreach). The average loan was of US$1,119 per borrower. Repayment rates ranged from 31 per cent to 64 per cent.[101]"

"177. Achievements have ranged between 0 to 85 per cent in terms of the loan amounts disbursed and have been even more modest in terms of the number of loans disbursed. Placing this in a wider context, Yemen has the lowest bank penetration rates in the region. Table 6 below gives a summary of the four completed projects. Only 6 per cent of the households in the Tihama project area obtained loans from CACB. In the Southern Governorates the rural finance component was not really implemented at all, apart from a few loans which the project staff tried to disburse on their own but then stopped. The Raymah project did not succeed in providing rural financial services to the rural households in the project area to any significant degree or in any sustainable manner. It did not reach the 10 per cent of landowning farmers which was given as an indicator of its success. Less than 1 per cent of the farmers in the project area received financing during the project period.[102]"

Footnotes, verbatim: "101 These figures were estimated by the evaluation team using the latest information available with CACB." "102 Assuming that there were 48,000 households in the project area."

Table 6 (same page, "Achievement of SAR Targets"; loans disbursed as % of SAR / amount disbursed as % of SAR): TEPP 15 / 85; SGRDP 0 / 0; RADP 3 / 50; AMRDP 21 / 34.

Checks: 4.165 / 13.37 = 31.2%; 3,723 / 58,867 = 6.3%; 4,165,000 / 3,723 = US$1,119. All confirmed.

Differences and cautions:
- Raymah uses two bases: the 10% target is of "landowning farmers", while the "less than 1 per cent" is of "the farmers in the project area" (fn 102 assumes 48,000 households). Not like-for-like; do not write "under 1% vs 10%" as one measure.
- Southern Governorates: text says "not really implemented at all, apart from a few loans"; Table 6 shows 0 and 0 for SGRDP. Use the text wording "not really implemented at all".
- Figures are "estimated by the evaluation team using the latest information available with CACB" (fn 101): estimates, not audited figures. Para 176 refers to "the completed IFAD projects" and "the last fifteen years".
- Para 177 range: 0 to 85 per cent of loan amounts disbursed against SAR targets.

### Paras 138-140 (printed p.33, PDF p.50)

Verbatim:
"138. Despite the inclusion of these various strategies IFAD financed projects were obliged to depend mainly on a Government Bank (the CACB) as its key partner, which may have not been an appropriate choice.[86] Poor households were said to be reluctant to apply for CACB credit due to their inability to meet the collateral requirements, the high transaction costs, lengthy approval procedures and the inherent reluctance to deal with any institution that is perceived to charge "interest rates" in contradiction to Islamic precepts.[87] Women had little access to CACB credit due to the low ceiling for collateral free loans and the requirement of land collateral for larger loans. Women did not generally own land and, as such, a woman could not fulfil this requirement without the support of their husbands or another male household member. The same was true of sharecroppers who could qualify for a loan only if the landowner was willing to offer his land as collateral.[88] However, IFAD did not have a choice as CACB was the chosen agent of the Government and was the only agency with outreach in rural areas at the time."

"139. In terms of rural finance activities the main emphasis in most of the IFAD projects under review has been on the provision of credit in rural areas. Only two projects - Dhamar and Al-Dhala - made provision for enhancing access to saving services."

"140. Certain decisions regarding IFAD support to CACB were not optimal. IFAD helped to build several of CACB branches where none existed previously (in Al-Jabeen in Raymah and Sayhut in Al-Mahara). However, these were not located near the commercial centres and as such have limited utility. It is instructive to note that when CACB decided to enhance its operations in Sayhut they opened another branch on the relatively busy main road that served 80 to 100 clients per day whereas the IFAD built branch in the centre of town has a client call of only between 5 to 15 per day."

Footnotes: 87 "Project Completion Evaluation. Raymah Project. May 2009 and discussions with potential clients in Al-Mahara during the CPE Mission in October 2010." 88 "Tihama Environmental Protection Project - Interim Evaluation Mission Report. March 2002."
CACB expansion (abbreviations list): "Cooperative and Agriculture Credit Bank".

Differences: sharecroppers are a separate group in the sentence ("The same was true of sharecroppers"), not a description of women. The household-reluctance reasons are reported with "were said to be", i.e. reported views, sourced to fn 87. Branches: the text says "not located near the commercial centres" (the evaluation's own claim), and it names two branches (Al-Jabeen in Raymah, Sayhut in Al-Mahara).

### Period evaluated (printed p.3, PDF p.20, paras 9-10)

Verbatim: "9. ... At the request of the Government of Yemen and as agreed by IFAD Programme Management Department this CPE analyses the ten projects approved after the 1992 CPE (table 1) ..." and "10. ... the oldest project in the cohort is the Tihama Environment Protection Project (TEPP), approved in 1993. This implies that the CPE would need to go significantly back further than the customary ten years and would cover more or less 18 years (1993-2010) of IFAD-Government cooperation in Yemen."

Confirmed: 1993 to 2010 ("more or less 18 years"). Distribution "Public". Date 6 October 2011 (cover), with the title page dated 23 September 2011.

---

## G. Remittance Prices Worldwide, dataset rpw_dataset_2011_2025_q3.xlsx

File read: https://datacatalogfiles.worldbank.org/ddh-published/0037898/DR0095523/rpw_dataset_2011_2025_q3.xlsx (HTTP 200; 50.8 MB).
Workbook sheets: Terms of Use, Methodology (empty), Legend, Countries, Dataset (up to Q1 2016), Dataset (from Q2 2016). Used sheet: "Dataset (from Q2 2016)" (204,470 rows).

Columns used:
- `period` (filter: `2025_3Q`)
- `source_code` (USA, SAU, ARE), `source_name`
- `destination_code` = `YEM`, `destination_name` = "Yemen, Rep."
- `corridor` (USAYEM, SAUYEM, AREYEM; used as a check)
- `cc1 denomination amount` = 200 (USD sent), `cc1 total cost %` for US$200
- `cc2 denomination amount` = 500 (USD sent), `cc2 total cost %` for US$500
- Legend, verbatim: "cc(X) total cost %: total cost of the transaction in percentage"; "cc(X) denomination amount: surveyed amount sent in USD".

Method: simple arithmetic mean across all quotes in the corridor for the period (no weighting by firm, instrument or access point). Every quote had a non-blank value in both columns.

Results:

| corridor, 2025_3Q | quotes | mean total cost at US$200 (`cc1 total cost %`) | mean at US$500 (`cc2 total cost %`) | expected | match |
|---|---|---|---|---|---|
| United States to Yemen | 12 | 3.9167 -> 3.92% | 2.3000 -> 2.30% | 12 quotes; 3.92%; 2.30% | YES |
| Saudi Arabia to Yemen | 8 | 2.695 -> 2.70% (round half up; exact 21.56 / 8) | 1.2625 -> 1.26% | 2.70% at 200 | YES |
| United Arab Emirates to Yemen | 6 | 7.5317 -> 7.53% | 5.6217 -> 5.62% | 7.53% at 200 | YES |

US to Yemen quotes (firm, instrument, access point, cc1, cc2): MoneyGram credit card/internet 6 / 4.5; MoneyGram debit card/internet 3 / 1.8; MoneyGram bank account transfer/internet 2 / 0.8; Walmart2World credit card/internet 6 / 4.5; Western Union cash/agent 4 / 1.6; Western Union credit card/internet 2 / 1; Western Union debit card/internet 2 / 1; Walmart2World cash/agent 7.5 / 3; Walmart2World debit card/agent 3 / 1.8; Ria debit card/call center 2.5 / 1.8; Ria credit card/call center 6 / 4; Walmart2World debit card/internet 3 / 1.8. Collection dates 12 to 26 Aug 2025. All "transparent: Yes".

Observations for downstream use:
- Only 2 of the 12 US quotes are cash to agent (Western Union 4% / 1.6%, Walmart2World 7.5% / 3%). The mean mixes card, bank-account and cash products and online and agent access points, so it is the average listed quote, not the cost to a typical Yemen-bound sender.
- UAE mean at US$200 is driven by one quote: Al Ansari 22.71% (20.24% at 500). Without it the five other quotes average 4.50% at 200. Dahabshiil is 2.97% at 200 but 3.12% at 500, the only quote costing more at the larger amount.
- Saudi quotes were collected 21 Aug to 2 Sep 2025; UAE quotes 15 to 21 Aug 2025.
- No `2025_2Q` rows exist in the whole sheet: 2025 has only `2025_1Q` and `2025_3Q`. Yemen has 26 quotes in 2025_3Q (12 USA, 8 SAU, 6 ARE), so these three are the only source countries for Yemen that quarter. Yemen has 27 quotes in 2025_1Q (13 USA, 8 SAU, 6 ARE).
- "Terms of Use" sheet text reads "REFERENCES: / Terms of use: Restricted Data / Terms of use for datasets / World Bank Terms and Conditions" (no further wording in cells). I did not interpret it. You described it as a public published dataset and it was downloaded from the World Bank data catalogue file URL; check the licence on the catalogue page before reuse.

---

## H. FATF

NOT READ. Requests to fatf-gafi.org were blocked by a Cloudflare bot challenge:
- https://www.fatf-gafi.org/en/countries/black-and-grey-lists.html: HTTP 403, body "Just a moment..." (curl); HTTP 403 (WebFetch).
- https://www.fatf-gafi.org/en/publications/High-risk-and-other-monitored-jurisdictions/increased-monitoring-october-2025.html: HTTP 403 (curl and WebFetch).
- https://www.fatf-gafi.org/en/countries/detail/Yemen.html: HTTP 403 (curl).
I did not try to bypass the challenge. No status of Yemen, document title or date is reported, because none was read on fatf-gafi.org. Needs a person in a browser, or an agent with a browser, to open the current "Jurisdictions under Increased Monitoring" and "High-Risk Jurisdictions subject to a Call for Action" documents and record the plenary date.

---

## NOT FOUND (searched ...)

- US$62.5 million in A2 (searched the whole page text of the 7 Dec 2024 release): not present. Present only in A1, tied to the 18th cycle.
- "Annual Report" as the title of the SMEPS document (searched the full PDF text and the rendered cover): not present. Cover reads "2024 SMEPS EXECUTIVE REPORT".
- Definition of "BAs" in the SMEPS report (searched the full text): not present.
- A printed publication date on the CCY cash-duration report (searched cover and full text): not present. Date evidence is the URL path and PDF metadata only.
- A year ("2026") in the B sentence naming "Ramadan and Eid al-Adha": not present in that sentence.
- FATF status of Yemen: NOT READ (above).
