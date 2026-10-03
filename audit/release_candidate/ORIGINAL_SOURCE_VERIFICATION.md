# Original-source verification — release candidate (from 3 October 2026)

The owner's update of 3 October 2026: now that the originals can be read, every number on the first screen of Home and of
the eight domain pages, and every number in a drawn figure, is re-read in its original source before B15 — value, unit,
period, universe and the wording of what it does not establish. A mismatch is a truth defect, fixed Master-first in both
languages; a source that has moved gets its current locator; a newer original release is reflected through the governed
path or recorded as "checked on <date>". Every check is recorded here, matches included.

How to read a row: **Object** is what a reader sees; **Original** is the document read (publisher's own copy) and its
locator; **Result** is MATCH, CORRECTED (transaction), FLAGGED (kept flagged: not confirmable in the original) or
NEWER (a newer original exists). Verification was done by reading the original, by a verifier working only from
originals, and by a second, independent spot-check of the key passages against the downloaded text.

## Network and access (3 October 2026)

cby-ye.com, english.cby-ye.com, www.elibrary.imf.org, documents.worldbank.org and www.worldbank.org answer. www.imf.org
refuses automated clients at its own CDN (Akamai "Access Denied", HTTP 403) although the session's proxy now passes the
connection; IMF country reports are read in full from the IMF eLibrary, the IMF's own publication platform.
microdata.worldbank.org and remittanceprices.worldbank.org returned HTTP 403 to a plain request (see the currentness
sweep for what was tried).

## 1. Part A item 3 — the four IMF-attributed chronology events (EXT-01)

Original: IMF Country Report No. 26/80, *Republic of Yemen: 2025 Article IV Consultation — Press Release; Staff Report;
and Statement by the Executive Director* (published April 2026; staff report dated 20 November 2025), full PDF from
https://www.elibrary.imf.org/downloadpdf/view/journals/002/2026/080/002.2026.issue-080-en.pdf, read 3 October 2026.

| Object | Element | Original says (locator) | Result |
|---|---|---|---|
| YSC-008 | dates | "Following the October 2022 attacks on oil export facilities in Hadramout and Shabwa governorates, oil exports have been suspended since January 2023." (staff report ¶6, p. 6) | MATCH. The suspected October–November 2022 date for the suspension is not in the report (¶4 says "end-2022"; nowhere October or November) |
| YSC-008 | revenue and scope | "cutting government revenues by almost half" (¶4); data relate to areas under the authorities' control (¶2) | MATCH |
| YSC-014 | values | "a decline in the capital to assets ratio from about 5 in 2022 to 2½ in April 2025. The liquid assets to short term liability ratio have sharply declined, from 148 in 2022 to 69 in April 2025" (¶13, p. 9) | MATCH for 148, 69 and "about 5"; CORRECTED (RC-7): the end value is 2½, not "about 2.5" |
| YSC-014 | attribution | ¶13 is the staff report's text; its FSI table (Table 5, p. 31) is sourced "Yemeni Authorities; IMF Staff Calculations" and gives Dec-22 147.2 and 4.9, Aug-25 73.6 and 3.8; no April 2025 column | CORRECTED (RC-7): "the IMF's banking data" → "According to the IMF staff report, which focuses on…, the banking sector's ratio of liquid assets to short-term liabilities…"; the note says that Table 5 gives different values and dates |
| YSC-014 | coverage | ¶2 (p. 5): data relate to areas under the authorities' control unless otherwise stated; Annex IV (p. 42): the banks' balance-sheet data cover the whole of Yemen; the coverage of the two ratios is not stated | CORRECTED (RC-7): "covers" → "focuses on"; the note states both passages |
| YSC-014 | unit | neither ¶13 nor Table 5 states a unit | MATCH (the event gives none); now stated with the event |
| YSC-015 | name, date | "the government established the NCRFI in July 2025" (¶39, p. 21); full name in ¶8 (p. 7) | MATCH |
| YSC-015 | wording | "to prioritize FX use for essential imports, enhance import transparency, and channel FX into the formal banking sector" (¶8) | CORRECTED (RC-7) to the report's words ("FX use", "enhance", "into") |
| YSC-017 | value, date, term | "operational FX reserves as of September 2025 remain low at USD$350million, covering about a month worth of imports" (¶12, p. 9) | MATCH for the term, date and cover; CORRECTED (RC-7): US$350 million, not "about" |
| YSC-017 | same report, other date | The joint IMF–IDA debt sustainability analysis in the same country report: "At US$ 0.35 billion as of June 2025" (DSA ¶13, p. 7); Table 1 gives gross reserves, a different measure | DISCLOSED (RC-7): a note with the event says the DSA dates the same amount to June 2025 |
| Methodology lead | — | — | Kept in its Path B wording (true and precise); no event is now flagged |

## 2. Part A item 6 — VIS-FIRM-CONSTRAINTS (Table 8)

Original: World Bank, *Yemen Financial Sector Diagnostics* (Report No. 194269, 5 April 2024), PDF
https://documents1.worldbank.org/curated/en/099102324070011985/pdf/P177631-d18a7ee4-3fcf-4393-9665-77f98b3e43a7.pdf
(152 pages; SHA-256 b245520c91d3891bf1d742521a341d6a296ca57afefb2bd36cd74198d0e0f682), Annex III, Table 8 "List of
Challenges to the Establishment", p. 146, read 3 October 2026 (page text and rendered page image).

| Row | Label in the original | Original | Ours | Result |
|---|---|---:|---:|---|
| CH-01 | Electricity | 50% | 50 | MATCH |
| CH-02 | Fuel shortages | 46% | 46 | MATCH |
| CH-03 | Transport/road blockade | 32% | 32 | MATCH (Figure 108 on the same page shows 22; the method now says so) |
| CH-04 | Tax administration/tax rates | 30% | 30 | MATCH |
| CH-05 | Political instability | 27% | 27 | MATCH |
| CH-06 | Access to finance | 22% | 22 | MATCH |
| CH-07 | Siege | 18% | 18 | MATCH |
| CH-08 | Practices of competitors in informal sector | 17% | 17 | MATCH |
| CH-09 | Labor regulations | 15% | 15 | MATCH; bound (RC-7) |
| CH-10 | Customs and trade regulation | 14% | 14 | MATCH; bound |
| CH-11 | Corruption | 10% | 10 | MATCH; bound |
| CH-12 | Access to land | 7% | 7 | MATCH; bound |
| CH-13 | Business licensing and permits | 6% | 6 | MATCH; bound |
| CH-14 | Inadequately educated workers | 5% | 5 | MATCH; bound |
| CH-15 | Courts | 1% | 1 | MATCH; bound |
| CH-16 | Crime, theft, disorder | 0% | 0 | MATCH; bound |

Also read in the original, and acted on in RC-7:

- **The survey's name.** The source calls it "the 2022 Yemen Enterprise Survey" (Annex III title) and "the World Bank's
  Enterprise Survey of 2022" (introduction). "Custom" is not the source's word: CORRECTED everywhere it was written, in
  both languages.
- **Sample.** The survey covered 328 formal and 217 informal enterprises (Annex III, p. 139); Table 8 is the formal-firm
  sample. CORRECTED (RC-7): the method names "the formal-firm sample of the World Bank's 2022 Yemen Enterprise Survey".
- **Universe.** 328 formal enterprises in seven governorates (Aden, Amanat Al Asimah, Al Hudaydah, Taizz, Hadramaut,
  Marib, Ibb), 164 in areas under the internationally recognized government and 164 in areas under the Houthis; data
  collected in September 2022 (Annex III introduction, p. 139). MATCH with "formal firms in seven governorates
  (September 2022)".
- **Base and response rule.** Table 8 states neither; the sixteen shares add up to 300. MATCH with the record's
  limitation ("neither the number of firms answering nor the exact question wording is recorded"; "firms could name
  more than one challenge").
- **Caution.** The source gives no caution that Table 8 is not the standard Enterprise Survey "biggest obstacle"
  question; that caution is the resource's own method statement and stays one, now resting on the indicator (shares can
  count more than one challenge per firm), not on the survey being non-standard — the source counts this survey among its
  Enterprise Surveys (p. 108; Figure 82, p. 111). The source is not consistent with itself: p. 145 says access to finance
  "remained on top of the main challenges"; Figure 83 (p. 111) puts it at 12%, level with political instability, behind
  electricity at 24%. DISCLOSED (RC-7) in the method of CLM-005 and VIS-FIRM-CONSTRAINTS; the values shown are Table 8's.
- **Not yet read:** VIS-FIRM-FINANCE-PATH's method cites Figure 105 (p. 143; 31 of 328 firms with a line of credit) and
  Table 6 (p. 144; 18 valid responses); CLM-006 cites the filtered "major obstacle" shares (68.71%, 23.13%). These are
  re-read in the original before B15 (section 4).
- **Report title in Arabic.** Written two ways; CORRECTED to the source library's «تشخيص القطاع المالي في اليمن (2024)».

## 3. Currentness and enrichment sweep (Owner Addendum 2; B13d / B14e watch points), 3 October 2026

Read by a verifier working only from publishers' own pages and files (every request logged with its HTTP status), with the
key readings re-checked independently by eye on the original images (POS values for all six months of 2026; the Decision
18 entity list; the Decision 10 date block and letterhead).

| Watch point | Original read | Finding | Result |
|---|---|---|---|
| CBY-Aden decisions after No. 18 of 2026 | Arabic news pages (cby-ye.com/news), English news list | Newest is No. 18 (news/975, 24 September 2026); news ids 976 and above return HTTP 500; the English list's newest item is dated 30 September 2025 | Checked on 3 October 2026 — nothing newer |
| Decision No. 18 of 2026, entity names (EXT-03) | Signed scan https://www.cby-ye.com/files/6ab52faa3604f.pdf (Ref 599/CBY/2026; 24 September 2026 = 12 Rabi' al-Thani 1448) | Article 1 suspends the licences and closes the premises of: «شركة صدام اكسبرس للصرافة والتحويلات»؛ «منشأة خالد العصواني للصرافة»؛ «منشأة مرتع للصرافة والتحويلات»؛ «بن عمر وكيل حوالة». Effective from issue; «سحب» (withdrawal) does not appear. CBY publishes no English names | NEW — transcribed Arabic-first; to be held in the Master with the status-event table (pending) |
| Decision No. 10 of 2026, date (EXT-02) | Signed scan https://www.cby-ye.com/files/6a27bc7883b9c.pdf (Ref 345/CBY/2026) | The instrument is dated **8 June 2026** (22 Dhu al-Hijjah 1447) on the letterhead and in the closing block; the news page (news/944) is dated 9 June 2026. Title: «بشأن إيقاف ترخيص بن دابي وكيل حوالة – شبوة/ حبان- العرم وإغلاق مقرها» | CORRECTION PENDING (next transaction): the held 9 June is the news page's date, not the instrument's |
| CBY-Aden monthly POS releases after January 2026 | Arabic list https://cby-ye.com/pages/33; English list https://english.cby-ye.com/pages/27 | **February–June 2026 are published on the Arabic list only** (files dated about 2 August 2026); the English list still ends at January 2026. June 2026: 1,651 terminals, 27,504 transactions, value 1,045 (YER million in the series' unit; the tile says «مليار»). The May release's printed changes (+2.4% terminals, +9.9% transactions) contradict its own totals (+3.3%, +18.5%) | NEWER — to be reflected Master-first (pending transaction). The cut-off of 26 September 2026 recorded January as the latest because only the English list was read; the Arabic list already held the newer releases |
| World Bank FMIIP (P180708) ISR No. 2 | ISR PDF of 8 April 2026 (documents.worldbank.org) | No indicator reports an observed value: every "actual" is 0, "No" or blank, dated 29 or 31 August 2025 (before effectiveness, 1 September 2025). Access points: baseline 817, actual 0, target 1,021 (June 2030); FPS and RTGS operational: No; participating institutions 0 (target 10 each). No ISR No. 3, restructuring or additional financing on the World Bank's documents API | Checked on 3 October 2026 — no RESULT row exists for VIS-TARGET-RESULT-STATE |
| IMF Staff-Monitored Program (SLA of 16 July 2026) | IMF eLibrary search; www.imf.org (CDN 403) | No approval notice or later Yemen document in the eLibrary; newest is CR 26/80 (3 April 2026). An approval press release published only on www.imf.org cannot be ruled out from this session | Checked on 3 October 2026 — nothing newer found; www.imf.org unreadable |
| 2023 SFD/SMED primary source for 78,686 borrowers (EXT-06) | smed.sfd-yemen.org (connection reset ×6; HTTP 503 upstream timeout); sfd-yemen.org annual reports end at 2020; web.archive.org blocked by egress policy | — | NOT READ — stays flagged (EXT-06 open) |
| Global Findex 2025 — Yemen coverage | Findex 2025 methodology annex, Table A.1 (141 economies); GlobalFindexDatabase2025.csv | **Yemen is not covered by the 2025 edition** (2024 fieldwork): absent from Table A.1; the database has Yemen rows for 2011, 2014 and 2022 only. Yemen's latest remains the 2021-edition wave (stored as 2022; account ownership 0.119) | MATCH with the resource ("no Yemen wave newer than the 2021 wave"); to be stated where people-side currentness is discussed (Addendum lesson) |
| Findex 2021 Yemen coverage (Microdata Library, catalog 5862) | https://microdata.worldbank.org/index.php/catalog/5862/study-description | "Al Baydaa, Al Jawf, Mareb, Sadah, the Island of Socotra, and several districts in other governorates were excluded … approximately 23% of the population"; over one-fourth of PSUs replaced; n = 1,000; face-to-face in Arabic; 7 November 2022 – 9 January 2023. Universe (adults 15+) from the Findex 2021 report's methodology | MATCH (about 23% excluded; the excluded areas can now be named) |
| Remittance Prices Worldwide, Saudi Arabia and UAE to Yemen after 2025 Q3 | remittanceprices.worldbank.org (Cloudflare JavaScript challenge, HTTP 403 on every URL); Data Catalog API (HTTP 429 ×5) | — | NOT READ — 2025 Q3 stays the latest held; recheck in a browser session |
| CBY-Aden list of licensed banks | Arabic page https://cby-ye.com/pages/14 → https://cby-ye.com/files/6a665add29feb.pdf (scan, created 26 July 2026); English page still links the 15 April 2026 file | Same count, **26 banks**; no printed date; row 26 is now «بنك الاتحاد للتمويل الأصغر» / Etihad Bank for Microfinance; two rows' contact details changed | MATCH for the count; the locator moves to the newer file (pending transaction) |

## 4. Resolved Master-first in RC-8 (3 October 2026)

The "pending" results of §3 are carried into the Master by one merged transaction
(`audit/release_candidate/rc_8_truth_currentness.py`; ledger `runs/RC-8_MASTER_LEDGER.json`). What each check now
changes, and the two records the owner asked to be kept here:

| Item | Original read | What the Master now holds |
|---|---|---|
| POS February–June 2026: **the Arabic-site discovery** | Arabic list https://cby-ye.com/pages/33 (five files, ids 6a6f958d49cc2 … 6a6f973c98c25); English list https://english.cby-ye.com/pages/27 (ends at January 2026) | 15 observations OBS-00083..OBS-00097 and five source records SRC-CBY-POS-2026-02..06, each with its Arabic-list file as primary locator. The cut-off of 26 September 2026 read only the English list; the Arabic list is now named on CLM-017, /payments/ and PAYCUR-001, and the publication-page record lists pages/33 (it listed pages/11, which is not the POS list). Values read by eye on the KPI tiles of all five files: terminals 1,502 / 1,544 / 1,583 / 1,636 / 1,651; transactions 23,037 / 25,663 / 30,559 / 36,201 / 27,504; value 1,232 / 1,124 / 1,244 / 1,579 / 1,045 (YER million in the series' unit) |
| POS May 2026: the release contradicts itself | May file 6a6f96ed5c009 | The tiles display +2.4% (terminals) and +9.9% (transactions); the published April and May totals do not give those percentages. Per the owner (note of 3 October 2026, point 2) nothing resolves it and no change is computed: public copy prints the totals and the displayed percentage and says that no change is derived for April to May 2026; the May rows carry the source-internal-contradiction state (chart marker "Source figures disagree"); CTR-013/014 record it. February displays +1.9% (terminals) and −2.3% (value) where the totals give about 1.97% and −2.38%: read as truncation, noted on the row, not flagged |
| POS value unit | Every 2026 file | The YER tile is labelled «مليار» (billion) from January 2026; the earlier releases state million YER and the printed month-on-month changes reconcile only in millions. The series stays in YER million; the disclosure is printed on VIS-POS-VALUE (summary, text alternative, chart note) and in the passport |
| POS January 2026: **the locator change** | Held file https://www.cby-ye.com/files/69b058d4bc306.pdf (still resolves, HTTP 200; no longer linked from either list); Arabic list's re-issue https://cby-ye.com/files/6a6f950da3173.pdf | The re-issue prints the same totals (1,473; 24,026; 1,262) and percentages (+11%; +4.9%). SRC-CBY-POS-2026-01 keeps the file that was read as its primary locator and lists the re-issue and the Arabic list beside it |
| Decision No. 10 of 2026 (EXT-02) | Signed scan https://www.cby-ye.com/files/6a27bc7883b9c.pdf | PSE-012 event date 8 June 2026 (was the news page's 9 June); the source record carries the instrument date, the scan and the date in its title, in both languages. Prints as "2026-06-08" in the status-event table |
| Decision No. 18 of 2026 (EXT-03) | Signed scan https://www.cby-ye.com/files/6ab52faa3604f.pdf | The four entities are held as non-public lineage only (PRV-EXCH-E023..E025, PRV-REM-E006: Arabic as printed; an English rendering marked as this resource's, the decision being in Arabic only), with the scan as locator; printed nowhere. PSE-015 prints as the other decisions; CLM-019 no longer says "not yet transcribed". The class label now reads "Exchange company, establishments and remittance agent" / «شركة صرافة ومنشآت صرافة ووكيل حوالات» (one company, two establishments, one agent). The governed `public_use` of five other status events still allows a subject to be shown; recorded in `design/ESCALATIONS.md`, nothing printed |
| Licensed-bank list | https://cby-ye.com/files/6a665add29feb.pdf (Arabic, July 2026) | Primary locator moves to the newer Arabic file; the April English file stays listed. Every public "as checked on 7 September 2026" for the bank list now reads 3 October 2026 (26 banks; 12 named as microfinance banks) |
| Edition | — | The edition moves to 3 October 2026, the date of this sweep. The remittance-corridor statement keeps "as checked on 26 September 2026": the corridor pages could not be read on 3 October |

Not carried in RC-8 (next): the Global Findex 2025 non-coverage of Yemen and the Microdata Library's named exclusions
(about 23% of the population) — both MATCH what the resource says; adding them is enrichment, queued after B6.

## 5. Independent reviews of RC-8, folded into RC-8b (3 October 2026)

Two reviewers who did not write RC-8 read it: one bilingual reviewer (Arabic first; NOT ACCEPTABLE, one blocking finding)
and one adversarial reviewer who re-read the originals (BROKEN, two blocking findings). The adversarial reviewer
confirmed every new number against the originals: the February–June 2026 tiles; the May treatment (no derived change
anywhere in `dist/`); the monthly highs; Decision No. 10's date (the scan reads "Ref:345/CBY/2026, Date: 8/6/2026" and
«الموافق 8 يونيو 2026م»); Decision No. 18's four names character for character, with none in `dist/` or the search data;
the 23 regulatory documents, all from CBY-Aden; the bank list's 26 rows, 12 of them named as microfinance banks.
All findings were applied in `rc_8b_review_fixes.py` (ledger `runs/RC-8b_MASTER_LEDGER.json`).

| Finding | Check in the original | Result |
|---|---|---|
| The reason given for reading the POS value in YER million was false: a month-on-month percentage is the same in millions and in billions | December 2025 file (69b058981b681) prints «910,688» under «مليون» with ▲24.4%; April 2025 prints «317,639 مليون» beside March's «320» (the Master already records it as 317.639) | **Corrected.** Every release writes the decimal mark as a comma. From January 2026 the value is given in billions, so «1,262» under «مليار» is 1.262 billion, i.e. YER 1,262 million. The label is right, and the series stays in YER million. The summaries, chart note, passport and observation caveats now say this. The value per transaction (about YER 52,500) is close to the Q3 2024 report's. December's printed +24.4% matches no reading of November's 783,583 (+16.2%); recorded here, not used |
| The exchange and remittance roster has been replaced | cby-ye.com/pages/14 links https://cby-ye.com/files/6ab391c11043b.pdf (created 22 September 2026; 20 pages, the last blank but for a stray "232"); the serial numbering restarts per section and ends at **100, 231 and 111**; the third heading «ثالثا: وكلاء الحوالات المرخصة لمزاولة نشاط الصرافة للعام 2026م» was read by eye on page 8 after establishment row 231 | **Corrected.** The Master held the 19 August file (6a87039fd05bb; 11 pages; 98 / 225 / 106; 429 rows). Counts, copy, contract pins and the locator now follow the 22 September file (442 rows). CLM-009 states that CBY-Aden has replaced the roster file during 2026. The 22 September file still lists an establishment that Decision No. 18 (24 September) suspended; this fits the rule that decisions are not subtracted from the roster |
| CLM-019 said entity names were recorded "from the signed decisions" | Only Decisions 10 and 18 have a signed-scan locator; the others are read from news pages | **Corrected** to "entity names, where transcribed, are held only in this resource's internal source records" |
| The other 2026 decision dates are news-page dates | Decision No. 10 shows that the instrument date can differ from the news page's date by a day | **Open.** Recorded in `FINAL_OPEN_ITEMS_REGISTER.md` for the B14e re-run: read each decision's signed scan where one is linked |
| Regulatory group "(23)" with 22 cards | `dist/*/data/`: the group renders 22 cards plus a link to the curated card of Decision No. 23 of 2024 | No change: the count is right |
| The bank list's foot may carry a handwritten «٢٦/٧» | July 2026 scan | The source title now says "no printed date" rather than "undated" |

## 6. Read in the original for B12 and B13 (3 October 2026, RC-12)

| Source | What was read | Result |
|---|---|---|
| `SRC-WB-FMIIP-ISR2-2026-001` (World Bank ISR, sequence 2), p. 3 | The access-point indicator. | It prints "Actual (Current) 0" against the 817 baseline, and does the same for beneficiaries. This is a reporting placeholder. It is **not bound**: VIS-TARGET-RESULT-STATE's result row says no observed result is held, not zero. |
| `SRC-WB-FSD-2024-001`, Annex III | p. 143: Figure 105 and its sentence. p. 144: Table 6, "Number of Loans, by Financial Institution". p. 145: Figure 107. | 31 of 328; the loan sources 10, 1, 5, 2 of 18; and 68.71 % / 23.13 % / 3.4 % / 4.76 % all match the bound rows. The p. 143 sentence links the line of credit and the loans in narrative only. The p. 145 sentence places the severity tabulation under "reasons of not applying": a register item. |
| SFD newsletters, the publisher's current files (`sfd-yemen.org/uploads/issues/Newsletter-Quarter-<q>-<year>.pdf`) | Issue number, quarter and the provider-table values that the Master binds. | No. 57 (Q1 2012): 69,121 / 96,593 / 3,962. No. 66 (Q2 2014): 116,188 / 495,940 / 12,693. No. 80 (Q4 2017): 85,259 / 746,387 / 7,800. No. 85 (Q1 2019): 85,219 and "YR 14.664 billions". No. 92 (Q4 2020): 88,445 / 1,611,206 / 33,379. All found: **same documents**, and the locators were moved in RC-12. |
| SFD newsletter No. 62 (Q2 2013), the publisher's current file | The same check. | **Another edition.** Its provider table, headed "until end of June 2014", totals 84,760 / 151,465 / 6,845. Its narrative gives "88 thousand" borrowers, "176 thousand" savers and a portfolio "approached 8 billion". The bound values are 88,169 / 175,447 / 7,845, from the original edition ("…en-62-2 NEW2…"). The locator became that address's web.archive.org copy. The archived file could not be opened here (egress policy). Register item. |
| `SRC-IBS-EPAY-YEM-2020`, pp. 54 and 68; `SRC-SMEPS-AR2024-2025`, printed pp. 8–9 | The rows that RV-CWR-005 and RV-CWR-008 panel 3 would need. | Read and recorded as missing Master rows in `B12_TEXT_FIRST_DISPOSITIONS.md`. Nothing is bound. |
