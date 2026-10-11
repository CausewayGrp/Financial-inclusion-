# FRONTIER verification cards

The cards behind the FRONTIER rows of the live view in `FINAL_OPEN_ITEMS_REGISTER.md` (brief W3f). States: `OPEN_ITEMS_STATES.json`.

Each card follows the W3a rule: the dated attempt, the exact human step (URL, what to read), the Master record it
changes, the honest public state meanwhile, and a cadence. A card closes only through a Master transaction after the
original is read; then the item moves to CLOSED in the live view and a dated line is appended under its old table.

**New IDs created in this view** (each continues its class sequence; the highest before were REL-04, EXT-19, FRN-09, OWN-10):

- REL-05 (HOSTING): Phone check of the live site from Yemen
- REL-06 (HOSTING): Deployment switch-on
- REL-07 (HOSTING): Optional aggregate request counts (D5)
- EXT-20 (FRONTIER): ESCWA, *Enhancing MSME Support Systems in Yemen* (July 2025)
- EXT-21 (FRONTIER): SMEPS annual report 2025
- EXT-22 (FRONTIER): CBY-Aden bulletin Issue No. 56 (July 2026)
- EXT-23 (FRONTIER): CBY-Aden POS releases, July–September 2026
- EXT-24 (FRONTIER): FMIIP (P180708) ISR sequence 3
- EXT-25 (FRONTIER): IMF SMP staff report and a new remittance vintage
- EXT-26 (FRONTIER): Governor's Decision No. 8 of 2026
- EXT-27 (FRONTIER): Governor's Decision No. 12 of 2026
- EXT-28 (FRONTIER): Governor's Decision No. 16 of 2026
- EXT-29 (FRONTIER): February 2026 SAR exchange-rate repricing decision
- EXT-30 (FRONTIER): Text of Governor's Decision No. 4 of 1991
- EXT-31 (FRONTIER): July 2024 licence revocation
- EXT-32 (FRONTIER): `cby-ye.com/news/709` (HTTP 500)
- EXT-33 (FRONTIER): `cby-ye.com/news/722` (HTTP 500)
- EXT-34 (FRONTIER): `cby-ye.com/news/731` (HTTP 500)
- EXT-35 (FRONTIER): SDRPY deposit notice (SPA N2234277)
- EXT-36 (FRONTIER): Own locator for CBY Sana'a Circular No. 14 of 2024
- EXT-37 (FRONTIER): Printed date of OECD *Digital Financial Inclusion of Youth*
- EXT-38 (FRONTIER): Identity of the World Bank FASTT fast-payments paper
- EXT-39 (FRONTIER): CBY-Aden Quarterly Bulletin, June 2021
- EXT-40 (FRONTIER): Owner's aggregate file for the 2021-wave domestic transfer channels (D16; added by CLOSE-6E)
- OWN-11 (OWNER-OPTIONAL): CWR-011 on `/finance/`
- OWN-12 (CLOSED): Domain pages show at most two Measurement priorities
- OWN-13 (OWNER-OPTIONAL): A twelfth Reading (RD8, CWR-012)

Cards: 47. No new FRN- ID was needed.

## REL-02 — Reuse terms of the original sources are not assessed

- **Dated attempt:** 10 Oct 2026, counted at `19105ede`: `rights_state` NOT_ASSESSED on 198 of the 199 source records in `site-src/content/sources/source_library.json`; one carries RESEARCH_LICENCE__AGGREGATE_STATISTICS_ONLY (ADJ-RG-01, AR-1). D4 counted 166 of 167 before the close-out added sources. No source's terms were read.
- **Human step:** For each source, open its locator and read the publisher's terms-of-use or licence page; record what reuse beyond linking and short citation it allows.
- **Record it changes:** Each source's row in the Master source register: `rights_state`, `licence`, `attribution_requirement`.
- **Public state meanwhile:** Source cards carry the reuse notice; `/data/` states the reuse terms once; no third-party document is bundled; downloads and exports stay off (D4); the launch is link-and-short-citation.
- **Cadence:** Each new edition, and before any download or export is switched on.
- **Who:** Owner (with counsel if the owner wants it); no legal review is claimed

## EXT-05 — OECD 2026 financial-sector review: product-holding and mobile-access figures

- **Dated attempt:** 3 Oct 2026, B13d link check: the publisher's CDN refused the request (403). Not re-attempted in W3a on 10 Oct 2026 (another oecd.org PDF, OECD/INFE 2023, did open that day: `audit/close_out/w0/A2_imf_yem.md`).
- **Human step:** Open https://doi.org/10.1787/81ed2898-en in a browser. Find the product-holding and mobile-access figures attributed to the review and read them in its own tables, with page numbers, period and universe.
- **Record it changes:** SRC-OECD-YEM-RESILIENCE-001; new bound records Master-first if the figures are confirmed.
- **Public state meanwhile:** `/finance/` says the figures have not been verified against the review's text and are not shown.
- **Cadence:** Once before release; then each new edition.
- **Who:** A person with a browser

## EXT-06 — Primary 2023 SFD/SMED loan-portfolio document (78,686 active borrowers)

- **Dated attempt:** 3 Oct 2026: smed.sfd-yemen.org reset or 503 (`audit/release_candidate/ORIGINAL_SOURCE_VERIFICATION.md` §3). RC-14 matched 78,686 to the Sana'a Center paper (secondary). Not re-attempted on 10 Oct 2026.
- **Human step:** Open https://smed.sfd-yemen.org in a browser (and the archived SMED page held as SRC-SFD-SMED-LP-2023-NOV). Locate the 2023 portfolio document and read the active-borrower count with its date and universe.
- **Record it changes:** CLM-053, CLM-054, CLM-057; a new source record for the primary document.
- **Public state meanwhile:** CLM-053 says the primary document is identified but not yet in the evidence base.
- **Cadence:** Each new edition.
- **Who:** A person with a browser

## EXT-09 — Seven locator-only sources without a governed title, publisher or document type

- **Dated attempt:** 3 Oct 2026 (B16): 9 such cards. 10 Oct 2026, counted at `19105ede`: 7 records with a public locator and no `document_label`: SRC-SFD-MF-HISTORY-TOR-2012-001, SRC-CBY-AR2015-HIST-001, SRC-CBY-SANAA-C12-2024, SRC-CBY-SANAA-C14-2024, SRC-LIT-INVEST-ISLAMIC-FI-2024, SRC-LIT-OEB-FX-PRICES-2025, SRC-ADEN-CBY-LIQ-2016. None was read for its metadata in W3a.
- **Human step:** Open each locator; record title, publisher, document type and date in both languages. Four overlap other cards: X-REG-LINK-AR2015, X-REG-LINK-C12, X-LINK-TLS-SIGNIN (two), EXT-36.
- **Record it changes:** Each source's `display_title`, `publisher`, `document_type`, `document_label` (EN, AR), Master-first.
- **Public state meanwhile:** `/data/` lists them as "reference · locator" under "Document type not recorded".
- **Cadence:** Each new edition.
- **Who:** A person with a browser

## EXT-11 — IFAD *Sending Money Home 2026*

- **Dated attempt:** Deferred at F3 (#2). No reopening attempt is recorded (B16); it was not a W3a target.
- **Human step:** On IFAD's site (https://www.ifad.org), open *Sending Money Home 2026* and read whether it publishes a Yemen estimate with a documented method.
- **Record it changes:** A new source record; 23_REMITTANCES only if a Yemen estimate has a documented method (the F3 reopening trigger).
- **Public state meanwhile:** Not in the source register; nothing is shown.
- **Cadence:** Yearly.
- **Who:** A person with a browser

## EXT-12 — Remittance Prices Worldwide after 2025 Q3

- **Dated attempt:** 10 Oct 2026 (CLOSE-3D): the RPW corridor pages refused automated requests; the World Bank data catalogue file ends at 2025 Q3 (`rpw_dataset_2011_2025_q3.xlsx`). 3 Oct 2026: HTTP 403.
- **Human step:** Open https://remittanceprices.worldbank.org/corridor/Saudi%20Arabia/Yemen and https://remittanceprices.worldbank.org/corridor/United%20Arab%20Emirates/Yemen in a browser. Read the latest quarter and the corridor average costs the visual uses; check the data catalogue for a newer dataset file.
- **Record it changes:** SRC-WB-RPW-SA-YEM-2025Q3-001, SRC-WB-RPW-UAE-YEM-2025Q3-001, the RPW rows of 23_REMITTANCES, VIS-REMITTANCE-COST; four values of X-REG-FIRSTSCREEN22.
- **Public state meanwhile:** VIS-REMITTANCE-COST shows RPW 2025 Q3 with the quarter in its title and period, beside the WDI yearly average (U7).
- **Cadence:** Quarterly (each RPW release).
- **Who:** A person with a browser

## EXT-13 — IMF Financial Access Survey after 2015

- **Dated attempt:** 10 Oct 2026 (U8): the WDI copies of the FAS series hold no Yemen value after 2015 (SRC-WB-WDI-FAS-YEM-001). The IMF FAS portal refuses automated requests.
- **Human step:** Open the IMF FAS data portal (https://data.imf.org) in a browser and look for any Yemen series after 2015.
- **Record it changes:** MA-005 current evidence; SRC-WB-WDI-FAS-YEM-001 or a new IMF FAS source record.
- **Public state meanwhile:** MA-005 shows 2015 as dated historical context and says the series stopped in 2015.
- **Cadence:** Yearly (each FAS release).
- **Who:** A person with a browser

## EXT-14 — ESPECRP unit of reach (households or individuals)

- **Dated attempt:** 10 Oct 2026: ISR sequence 10 (30 Jun 2026) was read for the UCT cycles and the closing date (U12; SRC-WB-ESPECRP-ISR10-2026-001). The unit of its reach indicators was not recorded.
- **Human step:** Open https://documents.worldbank.org/curated/en/099063026134041997/pdf/P173582-a6512878-8a11-454d-98f2-213c6f4df820.pdf; read §6.1, each reach indicator's name and definition; record households or individuals.
- **Record it changes:** The gate for any ESPECRP reach figure (`docs/S06_3_*`); CLM-045 and CWR-010 if a reach figure is ever added.
- **Public state meanwhile:** No ESPECRP reach figure is published.
- **Cadence:** Each new ESPECRP ISR until closing (31 Dec 2026), then the completion report.
- **Who:** Claude Code

## EXT-15 — CBY-Aden definition of "subscriber"

- **Dated attempt:** 10 Oct 2026: checked on the H1-2025 payments infographic; no definition is printed (§10).
- **Human step:** On each new CBY-Aden payments report (https://cby-ye.com/pages/33), look for a definition of «مشترك» (subscriber).
- **Record it changes:** The `/payments/` and `/reforms/` sentences (LA-A); CLM-027 and CWR-007 share text.
- **Public state meanwhile:** `/payments/` and `/reforms/` say no definition is published.
- **Cadence:** Each CBY-Aden payments report (half-yearly).
- **Who:** Claude Code (currentness re-run); a person with a browser if the host refuses

## EXT-16 — Source and year of the FMIIP PAD's "two percent"

- **Dated attempt:** 10 Oct 2026 (LA-B): the PAD sentence (¶9, p. 2) gives no year and no source. W0 (`audit/close_out/w0/A4_projects.md`) noted that ¶61 of the same PAD says five percent of women held a financial account in 2022: a lead, not the source of ¶9.
- **Human step:** Read the FMIIP PAD (https://documents.worldbank.org/curated/en/099052825174515006/pdf/BOSIB-524dd7c7-d52c-4876-80ed-1e3ea9df2463.pdf) ¶9 and its references; if none is printed, ask the World Bank task team for the source.
- **Record it changes:** CWR-007 (the PAD statement); SRC-WB-FMIIP-P180708.
- **Public state meanwhile:** CWR-007 shows it as what the PAD says, not as a measurement.
- **Cadence:** Each new FMIIP document.
- **Who:** Owner or Claude Code

## EXT-17 — Two Cash Consortium of Yemen reports without a public copy

- **Dated attempt:** 10 Oct 2026 (U3, CR-11): four of the six CCY reports now have public locators (SAM-2024, CASH-DURATION-2026, ISP-2024, PRESSURE-2026). No public copy found for SRC-CCY-REMIT-ESTIMATE-2025 and SRC-CCY-AMAL-2025.
- **Human step:** Ask the Cash Consortium of Yemen for public copies, or check https://www.calpnetwork.org and https://reliefweb.int for the two titles.
- **Record it changes:** SRC-CCY-REMIT-ESTIMATE-2025, SRC-CCY-AMAL-2025; CLM-044 (FRN-01).
- **Public state meanwhile:** Both stay non-public and are never named; CLM-044's value is withheld.
- **Cadence:** Each new edition.
- **Who:** Owner

## EXT-18 — Date of the CBY-Aden list of 26 licensed banks

- **Dated attempt:** 10 Oct 2026 (W0 A3): the list was re-read; no printed date (PDF created 26 Jul 2026) and no type column.
- **Human step:** Open https://cby-ye.com/pages/14; check for a newer, dated list and read its date.
- **Record it changes:** SRC-CBY-BANKLIST-AR-2026-001; CLM-008, CLM-055; the bank rows on `/providers/`.
- **Public state meanwhile:** The bank list is shown "as checked on 3 October 2026"; microfinance banks are counted by name.
- **Cadence:** Monthly, with the currentness re-run.
- **Who:** Claude Code (currentness re-run); a person with a browser if the host refuses

## EXT-20 — ESCWA, *Enhancing MSME Support Systems in Yemen* (July 2025)

- **Dated attempt:** 10 Oct 2026 (W3a): Cloudflare challenge; HTTP 403 to curl and WebFetch; headless Chromium still on the challenge after 30 s; the archive copy blocked by the session's egress policy. Verdict UNREACHABLE.
- **Human step:** Open https://depar.unescwa.org/system/files/2025-07/Enhancing_MSME%20Support_Systems_in_Yemen_ESCWA.pdf in a browser. Read title, date and publisher, and any MSME-finance figures with their sources and periods.
- **Record it changes:** A new source record; CWR-008 (RD4) only if it adds bounded evidence.
- **Public state meanwhile:** Not in the source register; nothing is shown.
- **Cadence:** Once before release; then each new edition.
- **Who:** A person with a browser

## EXT-21 — SMEPS annual report 2025

- **Dated attempt:** 10 Oct 2026 (W3a): https://smeps.org.ye/posts/Annual%20Reports lists the 2024 report (published 8 Oct 2025) as the latest. NOT FOUND; the 2024 report appeared about nine months after year-end.
- **Human step:** Check the list; when the 2025 report appears, read disbursements, MSMEs supported and the female-owned share, with page numbers.
- **Record it changes:** A new SMEPS 2025 source record; CWR-008 (RD4); RV-CWR-008 panel 3 (X-B12-RV-CWR-008).
- **Public state meanwhile:** The SMEPS figures shown are from the 2024 report (SRC-SMEPS-AR2024-2025), as programme figures, not national ones.
- **Cadence:** Quarterly until found; then yearly.
- **Who:** Claude Code

## EXT-22 — CBY-Aden *Monetary and Financial Developments*, Issue No. 56 (July 2026)

- **Dated attempt:** 10 Oct 2026 (W3a): not on https://english.cby-ye.com/researchandstatistics or https://cby-ye.com/pages/28; the latest is Issue No. 55 (June 2026, PDF created 16 Sep 2026).
- **Human step:** Check both listings; read Issue No. 56 Tables 1, 4, 5 and 6 for the indicators on `/finance/` and the rate line.
- **Record it changes:** SRC-CBY-001; 18_CBY_MONETARY; VIS-CBY-MONETARY-SNAPSHOT, VIS-YER-MARKET-RATE; CBY-BANKS rows; RV-CWR-011 and CWR-011.
- **Public state meanwhile:** `/finance/` and CWR-011 show June 2026 as the latest month and claim no later month.
- **Cadence:** Monthly.
- **Who:** Claude Code (currentness re-run); a person with a browser if the host refuses

## EXT-23 — CBY-Aden monthly POS releases, July–September 2026

- **Dated attempt:** 10 Oct 2026 (W3a): https://cby-ye.com/pages/33 lists March 2025 to June 2026 only; the English page ends January 2026. Also seen: the page now links January 2026 to `/files/6a6f950da3173.pdf`, while SRC-CBY-POS-2026-01 points at `69b058d4bc306` (values not re-read).
- **Human step:** Check pages/33; read each new release's transactions, value and terminal count. Re-read the January 2026 file at its new address and repoint the locator if the values match.
- **Record it changes:** New SRC-CBY-POS-2026-07 and later; 19_PAYMENTS_DATA; VIS-POS-VALUE; CWR-003, CWR-009 (RD6); SRC-CBY-POS-2026-01 locator.
- **Public state meanwhile:** The POS series ends at June 2026 and says so.
- **Cadence:** Monthly.
- **Who:** Claude Code (currentness re-run); a person with a browser if the host refuses

## EXT-24 — FMIIP (P180708) Implementation Status Report, sequence 3

- **Dated attempt:** 10 Oct 2026 (W3a): the World Bank documents API lists 14 FMIIP documents; the newest ISR is sequence 2 (8 Apr 2026). NOT FOUND.
- **Human step:** Check https://search.worldbank.org/api/v3/wds?format=json&proid=P180708 and https://projects.worldbank.org/en/projects-operations/project-detail/P180708; when sequence 3 appears, read the PDO indicator actuals (access points, beneficiaries) and their dates.
- **Record it changes:** A new FMIIP ISR source record; VIS-TARGET-RESULT-STATE (X-B12 drawing); CWR-003, CWR-009 (RD6).
- **Public state meanwhile:** VIS-TARGET-RESULT-STATE shows targets; the ISR's placeholder 0 is not bound; no observed result is drawn.
- **Cadence:** Half-yearly (ISR cycle).
- **Who:** Claude Code

## EXT-25 — IMF SMP staff report and a new remittance vintage

- **Dated attempt:** 10 Oct 2026 (W3a, W0 A2): the IMF Management approval of 7 Oct 2026 is held (press release pr26324; CR-07 closed). No staff report, country-report number or new remittance vintage is published; imf.org searches returned only CR 26/80.
- **Human step:** Check https://www.imf.org/en/Countries/YEM for the SMP staff report; read its remittance table and its scope (IRG areas or whole of Yemen).
- **Record it changes:** IMF rows of 23_REMITTANCES; CLM-007, CLM-037, CWR-001 (RD7), VIS-REMITTANCE-MACRO; FRN-03.
- **Public state meanwhile:** `/reforms/` and CLM-049 state the approval; the remittance history stays CR 26/80 (IMF estimates, IRG scope).
- **Cadence:** Monthly until published; then each SMP review.
- **Who:** A person with a browser

## EXT-26 — Governor's Decision No. 8 of 2026

- **Dated attempt:** 10 Oct 2026 (W0 A3, CLOSE-4): CBY-Aden news items 900–975 (every 2026 item) publish Decisions 1–6, 9–11, 13–15 and 17–18; No. 7 is on pages/14; No. 8 is on neither.
- **Human step:** Check https://cby-ye.com/news and https://cby-ye.com/pages/14; read the signed scan: number, date, subject and class. No entity names (D10).
- **Record it changes:** 31_REFORMS_REGULATION or the provider status events; CLM-019; 14_SYSTEM_CHRONOLOGY if it is a dated event.
- **Public state meanwhile:** CLM-019 states the decisions it holds; the `/data/` regulatory group says it is not a complete register.
- **Cadence:** Monthly, with the currentness re-run.
- **Who:** Claude Code (currentness re-run); a person with a browser if the host refuses

## EXT-27 — Governor's Decision No. 12 of 2026

- **Dated attempt:** 10 Oct 2026 (W0 A3, CLOSE-4): CBY-Aden news items 900–975 (every 2026 item) publish Decisions 1–6, 9–11, 13–15 and 17–18; No. 7 is on pages/14; No. 12 is on neither.
- **Human step:** Check https://cby-ye.com/news and https://cby-ye.com/pages/14; read the signed scan: number, date, subject and class. No entity names (D10).
- **Record it changes:** 31_REFORMS_REGULATION or the provider status events; CLM-019; 14_SYSTEM_CHRONOLOGY if it is a dated event.
- **Public state meanwhile:** CLM-019 states the decisions it holds; the `/data/` regulatory group says it is not a complete register.
- **Cadence:** Monthly, with the currentness re-run.
- **Who:** Claude Code (currentness re-run); a person with a browser if the host refuses

## EXT-28 — Governor's Decision No. 16 of 2026

- **Dated attempt:** 10 Oct 2026 (W0 A3, CLOSE-4): CBY-Aden news items 900–975 (every 2026 item) publish Decisions 1–6, 9–11, 13–15 and 17–18; No. 7 is on pages/14; No. 16 is on neither.
- **Human step:** Check https://cby-ye.com/news and https://cby-ye.com/pages/14; read the signed scan: number, date, subject and class. No entity names (D10).
- **Record it changes:** 31_REFORMS_REGULATION or the provider status events; CLM-019; 14_SYSTEM_CHRONOLOGY if it is a dated event.
- **Public state meanwhile:** CLM-019 states the decisions it holds; the `/data/` regulatory group says it is not a complete register.
- **Cadence:** Monthly, with the currentness re-run.
- **Who:** Claude Code (currentness re-run); a person with a browser if the host refuses

## EXT-29 — February 2026 SAR exchange-rate repricing decision

- **Dated attempt:** 10 Oct 2026 (W0 A3, CLOSE-4): not on cby-ye.com news, pages/14, or the February, March and June 2026 bulletins (EN and AR). Nearest original: the Board's extraordinary meeting of 12 Feb 2026 on exchange rates, which delegated action to the executive management (https://cby-ye.com/news/918).
- **Human step:** Search cby-ye.com and later bulletin appendices for the decision text; read its number, date and what it sets.
- **Record it changes:** 14_SYSTEM_CHRONOLOGY (a dated event); CLM-033 context.
- **Public state meanwhile:** No SAR repricing event is published.
- **Cadence:** Once more at release (runbook step 4); then each new edition.
- **Who:** Claude Code (currentness re-run); a person with a browser if the host refuses

## EXT-30 — Text of Governor's Decision No. 4 of 1991 (credit-information exchange)

- **Dated attempt:** 10 Oct 2026 (W0 A3, CLOSE-4): cited by https://cby-ye.com/publications/149 with circulars 33379 (14/8/1991) and 54064 (2/7/2006); the decision itself is not published on cby-ye.com.
- **Human step:** Ask CBY-Aden for the text, or find it in an official legal compilation; read its scope and date.
- **Record it changes:** 31_REFORMS_REGULATION (credit-information instruments); passport EP-CBY-CREDIT-INFO-SPINE-K04.
- **Public state meanwhile:** The decision appears only as publication 149 cites it; its text is not described.
- **Cadence:** Each new edition.
- **Who:** Owner (a request to CBY-Aden)

## EXT-31 — July 2024 licence revocation

- **Dated attempt:** 10 Oct 2026 (CLOSE-4): not found; the 2024 bank measure held is Governor's Decision No. 20 of 2024.
- **Human step:** Search https://cby-ye.com/news for July 2024; read any revocation decision: number, date, class and action. No entity names (D10).
- **Record it changes:** 14_SYSTEM_CHRONOLOGY (a neutral event entry, brief Appendix C); provider status events.
- **Public state meanwhile:** The 2024 measure shown is Decision No. 20 of 2024; no July 2024 revocation event is published.
- **Cadence:** Once more at release; then each new edition.
- **Who:** Claude Code (currentness re-run); a person with a browser if the host refuses

## EXT-32 — CBY-Aden news page 709

- **Dated attempt:** 10 Oct 2026 (CLOSE-4): https://cby-ye.com/news/709 returned HTTP 500.
- **Human step:** Open https://cby-ye.com/news/709 in a browser; read its title and date; decide whether it bears on the chronology or the regulatory group.
- **Record it changes:** Not known until read; candidates 14_SYSTEM_CHRONOLOGY and 31_REFORMS_REGULATION.
- **Public state meanwhile:** Nothing from this page is shown.
- **Cadence:** At release (runbook step 4); then each new edition.
- **Who:** A person with a browser

## EXT-33 — CBY-Aden news page 722

- **Dated attempt:** 10 Oct 2026 (CLOSE-4): https://cby-ye.com/news/722 returned HTTP 500.
- **Human step:** Open https://cby-ye.com/news/722 in a browser; read its title and date; decide whether it bears on the chronology or the regulatory group.
- **Record it changes:** Not known until read; candidates 14_SYSTEM_CHRONOLOGY and 31_REFORMS_REGULATION.
- **Public state meanwhile:** Nothing from this page is shown.
- **Cadence:** At release (runbook step 4); then each new edition.
- **Who:** A person with a browser

## EXT-34 — CBY-Aden news page 731

- **Dated attempt:** 10 Oct 2026 (CLOSE-4): https://cby-ye.com/news/731 returned HTTP 500.
- **Human step:** Open https://cby-ye.com/news/731 in a browser; read its title and date; decide whether it bears on the chronology or the regulatory group.
- **Record it changes:** Not known until read; candidates 14_SYSTEM_CHRONOLOGY and 31_REFORMS_REGULATION.
- **Public state meanwhile:** Nothing from this page is shown.
- **Cadence:** At release (runbook step 4); then each new edition.
- **Who:** A person with a browser

## EXT-35 — SDRPY deposit notice (Saudi Press Agency N2234277)

- **Dated attempt:** 4 Oct 2026 (`docs/HANDOVER_TO_DEVELOPER.md` §4): sdrpy.gov.sa failed TLS; the SPA page renders its body in JavaScript. No 10 Oct 2026 retry of this item is recorded.
- **Human step:** Open https://spa.gov.sa/en/N2234277 in a browser; read the deposit's amount, date and recipient. Keep apart: a $300m deposit in the CBY, $200m of budget support and a $1.2bn pledge.
- **Record it changes:** Sheet 190 inputs of CLM-046; a chronology or finance deposit record (additive).
- **Public state meanwhile:** Not published; nothing depends on it.
- **Cadence:** Once before release.
- **Who:** A person with a browser

## EXT-36 — Own locator for CBY Sana'a Circular No. 14 of 2024

- **Dated attempt:** 4 Oct 2026 (handover §4): no public locator of its own; the record points at UN document S/2024/731, printed p. 114, Fig. 28.2. No 10 Oct 2026 retry recorded.
- **Human step:** Search for a copy issued by the circular's own publisher. Never cite `cbyemen.com`, which now serves an unrelated site.
- **Record it changes:** SRC-CBY-SANAA-C14-2024.
- **Public state meanwhile:** A locator-only card pointing at the UN document.
- **Cadence:** Each new edition.
- **Who:** A person with a browser

## EXT-37 — Printed date of OECD, *Advancing the Digital Financial Inclusion of Youth*

- **Dated attempt:** 4 Oct 2026 (handover §4): Cloudflare challenge. No 10 Oct 2026 retry recorded.
- **Human step:** Open https://www.oecd.org/en/publications/advancing-the-digital-financial-inclusion-of-youth_21b829d8-en.html in a browser; read the printed publication date.
- **Record it changes:** SRC-OECD-YOUTH-DFI-2020-001 (`document_date`).
- **Public state meanwhile:** The card shows the date held; it is not yet checked against the printed page.
- **Cadence:** Once before release.
- **Who:** A person with a browser

## EXT-38 — Identity of the World Bank FASTT fast-payments paper

- **Dated attempt:** 4 Oct 2026 (handover §4): Cloudflare challenge; the repository shell needs JavaScript. No 10 Oct 2026 retry recorded.
- **Human step:** Open https://fastpayments.worldbank.org/sites/default/files/2021-11/Fast%20Payment%20Flagship_Final_Nov%201.pdf in a browser; confirm it is the flagship report, not *Implementation Considerations for Fast Payment Systems*.
- **Record it changes:** SRC-WB-FASTT-FPS-2021-001.
- **Public state meanwhile:** The card links the flagship PDF as held.
- **Cadence:** Once before release.
- **Who:** A person with a browser

## EXT-39 — CBY-Aden Quarterly Bulletin, June 2021

- **Dated attempt:** 4 Oct 2026 (handover §4): CBY-Aden's own link points to a CDN with a TLS hostname mismatch. No 10 Oct 2026 retry recorded.
- **Human step:** Ask CBY-Aden for the file, or cite another issue that carries the same table.
- **Record it changes:** The bulletin's source record.
- **Public state meanwhile:** Not published; nothing depends on it.
- **Cadence:** Each new edition.
- **Who:** Owner (a request to CBY-Aden)

## FRN-01 — CLM-044 residual-model value withheld

- **Dated attempt:** 3 Oct 2026 (B16): unchanged. 10 Oct 2026 (U3): its source report has no public copy (EXT-17).
- **Human step:** None for a reader; it closes only if the source report is made public (EXT-17) and its method can be read.
- **Record it changes:** CLM-044; SRC-CCY-REMIT-ESTIMATE-2025.
- **Public state meanwhile:** `/evidence/CLM-044/` withholds the value; it must never print.
- **Cadence:** Each new edition.
- **Who:** Owner (through EXT-17)

## FRN-02 — Firm base (about 147) and question wording behind the 91.84% table

- **Dated attempt:** 3 Oct 2026 (B16): unchanged.
- **Human step:** Read the 2022 Yemen Enterprise Survey's published questionnaire and tabulation notes (https://www.enterprisesurveys.org) for the question's wording and the filtered base.
- **Record it changes:** CLM-005.
- **Public state meanwhile:** `/evidence/CLM-005/` states that the base and the wording are not recorded.
- **Cadence:** Each new edition, or a new Enterprise Survey wave.
- **Who:** A person with a browser

## FRN-03 — No crosswalk between CBY-Aden and IMF remittance levels

- **Dated attempt:** 3 Oct 2026 (B16): unchanged. 10 Oct 2026: CR-05 confirmed the IMF series is model-based, IRG scope; no crosswalk published.
- **Human step:** On each new IMF Yemen report (EXT-25) and CBY-Aden annual report, look for a reconciliation of the two levels.
- **Record it changes:** CLM-037; RV-CWR-001.
- **Public state meanwhile:** `/evidence/CLM-037/` and RV-CWR-001 compare the paths only as indices.
- **Cadence:** Each IMF Yemen report and each CBY-Aden annual report.
- **Who:** Claude Code

## FRN-04 — The causes of the gender gap are not established

- **Dated attempt:** 3 Oct 2026 (B16): unchanged. 10 Oct 2026 (U10): the concordance adds statements and a hypothesis, no causal evidence.
- **Human step:** On each new survey wave or study of Yemen, check for a design that identifies causes.
- **Record it changes:** CWR-007; MA-003.
- **Public state meanwhile:** CWR-007 and MA-003 say the causes are not established.
- **Cadence:** Each new edition.
- **Who:** Claude Code

## FRN-05 — No reconciled view of current operating status across provider classes

- **Dated attempt:** 3 Oct 2026 (B16): unchanged; the provider matrix shows dimensions without a roll-up by design.
- **Human step:** Closes only if CBY-Aden publishes a dated register of operating providers; check https://cby-ye.com/pages/14.
- **Record it changes:** CLM-009, CLM-019; VIS-PROVIDER-OBSERVABILITY.
- **Public state meanwhile:** `/providers/` shows dated dimensions and no current-status summary.
- **Cadence:** Monthly, with the currentness re-run.
- **Who:** Claude Code (currentness re-run); a person with a browser if the host refuses

## FRN-06 — Size of the 2022 banking restatement

- **Dated attempt:** 3 Oct 2026 (B16): unchanged; the two vintages are not reconciled line by line (origin table 173 is not a Master sheet).
- **Human step:** Read the CBY-Aden annual reports for 2022 and 2023 side by side, balance-sheet line by line, and look for a published reconciliation.
- **Record it changes:** CLM-033; RV-CWR-002.
- **Public state meanwhile:** The "banking jump" Reading and CLM-033 say the size is not quantified.
- **Cadence:** Each CBY-Aden annual report.
- **Who:** Claude Code

## FRN-07 — Composite records whose member records are not listed

- **Dated attempt:** 10 Oct 2026, counted on the built site at `19105ede`: 8 records carry the note (CLM-014, DS-DEMAND-VINTAGE-LENS, VIS-INCLUSION-TRANSMISSION, VIS-MECHANISM-METRIC-BRIDGE, VIS-EVIDENCE-CLASS-LADDER, VIS-PROVIDER-OBSERVABILITY, VIS-EVIDENCE-GAPS, VIS-SOURCE-COMPARISON).
- **Human step:** None external: list each member record Master-first when it exists as a public record.
- **Record it changes:** The eight records above; `public_object_source_closure.json` regenerated.
- **Public state meanwhile:** Each page says the view summarises other evidence records that are not yet linked.
- **Cadence:** Each new edition.
- **Who:** Programme steward

## FRN-08 — World Bank Joint Food Security Monitor sub-national exchange-rate series

- **Dated attempt:** 3 Oct 2026 (B16): deferred; Addendum 2 rejects food-security monitoring (ADD2-REJ-11).
- **Human step:** Only if the owner reopens scope: read the series' definition, area and lineage in the Monitor's own notes.
- **Record it changes:** A new source record (none today).
- **Public state meanwhile:** Not in the source register.
- **Cadence:** Each new edition.
- **Who:** Owner

## X-B12-VIS-ACCESS-EVIDENCE-LAYER — VIS-ACCESS-EVIDENCE-LAYER needs a register of verified, dated operating locations

- **Dated attempt:** 3 Oct 2026 (B12): no such register is in the evidence base; MA-005 names it as missing evidence.
- **Human step:** If CBY-Aden or a programme publishes a dated register of operating access points, read its definition, date and coverage.
- **Record it changes:** MA-005; VIS-ACCESS-EVIDENCE-LAYER.
- **Public state meanwhile:** The visual renders as a text frame that names the missing input.
- **Cadence:** Each new edition.
- **Who:** Claude Code

## X-B12-VIS-TARGET-RESULT-STATE-DRAWING — VIS-TARGET-RESULT-STATE drawing needs an observed FMIIP result

- **Dated attempt:** 3 Oct 2026 (B12): table bound; the ISR's 0 is a placeholder. 10 Oct 2026: ISR sequence 3 not published (EXT-24).
- **Human step:** As EXT-24: read the first observed result under FMIIP-RF-004's definition.
- **Record it changes:** VIS-TARGET-RESULT-STATE; FMIIP-RF-004.
- **Public state meanwhile:** The table renders; no trajectory is drawn.
- **Cadence:** Half-yearly, with each FMIIP ISR.
- **Who:** Claude Code

## X-LINK-TLS-SIGNIN — Two locators: a TLS failure and a sign-in wall

- **Dated attempt:** 3 Oct 2026: SRC-LIT-OEB-FX-PRICES-2025 (asjp.cerist.dz, TLS chain does not verify) and SRC-ADEN-CBY-LIQ-2016 (search.mandumah.com, redirects to sign-in). Not re-checked on 10 Oct 2026.
- **Human step:** Open https://asjp.cerist.dz/en/article/273259 and https://search.mandumah.com/Record/932295 in a browser. If a locator stays sign-in only, add a note on the card under rule 5, Master-first.
- **Record it changes:** SRC-LIT-OEB-FX-PRICES-2025, SRC-ADEN-CBY-LIQ-2016.
- **Public state meanwhile:** Locator-only cards.
- **Cadence:** At release; then each new edition.
- **Who:** A person with a browser

## X-REG-FIRSTSCREEN22 — First-screen and drawn values not re-read on 3 October

- **Dated attempt:** 3 Oct 2026: 22 values unreadable (13 IMF, 4 RPW, 4 UNDP FMIIP start dates of July 2025, SFD 93,118). 10 Oct 2026: CR 26/80 opened in full (W0 A2) and its Table 4 remittance rows match the Master; RPW still refused (EXT-12); the UNDP page and SFD 93,118 not re-read.
- **Human step:** In a browser: (1) the four FMIIP component start dates on https://www.undp.org/yemen/projects/yemen-financial-market-infrastructure-and-inclusion-project (and the Arabic page), against the ISR's effectiveness date of 1 Sep 2025; (2) SFD's 93,118 at its locator; (3) tick the remaining IMF values in `ORIGINAL_SOURCE_VERIFICATION.md` §8.
- **Record it changes:** SRC-UNDP-FMIIP-001 (dates); the SFD record; `ORIGINAL_SOURCE_VERIFICATION.md` §8.
- **Public state meanwhile:** The values print as bound, each attributed; the UNDP dates are UNDP's, and the possible conflict with 1 Sep 2025 is not resolved.
- **Cadence:** Before release.
- **Who:** A person with a browser

## X-REG-LINK-AR2015 — CBY annual report 2015 host

- **Dated attempt:** 3 Oct 2026: HTTP 503 at both checks (`audit/FINAL_CURRENTNESS_CUTOFF.md`, CHECK BY HAND). Not re-checked on 10 Oct 2026.
- **Human step:** Open http://centralbank.gov.ye/App_Upload/Ann_rep2015AR.pdf in a browser. If it stays dead, repoint to the 2022 web.archive.org snapshot, labelled as an archived copy, Master-first.
- **Record it changes:** SRC-CBY-AR2015-HIST-001.
- **Public state meanwhile:** A locator-only card with the original address.
- **Cadence:** At release (runbook step 4); then each new edition.
- **Who:** A person with a browser
- **Update, 11 Oct 2026 (CLOSE-6B, addendum item 3):** HTTP 503 or a reset connection again; the Wayback Machine lists captures of 16 March 2019 and 30 June 2022, which could not be opened from this environment. The source feeds no record and is now withheld from the public directory (NON_PUBLIC). Public state meanwhile: not listed. Human step unchanged: confirm an archived copy; if confirmed, the steward may restore it Master-first, labelled as an archived copy.

## X-REG-LINK-C12 — CBY Sana'a Circular No. 12 of 2024: no working locator

- **Dated attempt:** 3 Oct 2026 (B13d, `audit/release_candidate/LINK_CHECK.md`): no working address and no archived copy. Not re-checked on 10 Oct 2026.
- **Human step:** Open the locator held for SRC-CBY-SANAA-C12-2024 in a browser and search for another copy. If none, the steward decides Master-first whether the source may stay publicly named (rule 5).
- **Record it changes:** SRC-CBY-SANAA-C12-2024.
- **Public state meanwhile:** A locator-only card.
- **Cadence:** At release (runbook step 4); then each new edition.
- **Who:** A person with a browser
- **Closed, 11 Oct 2026 (CLOSE-6B, addendum item 3):** the locator recorded on 4 Oct 2026 (a copy on yemeneco.org; the issuer publishes none that opens from here) was opened and read in full (`audit/close_out/addendum/R3_cby_completions.md`). The card is completed: issuer CBY-Sana'a, 13 March 2024, why it matters and what it does not establish. Register state: CLOSED. A link check at release (runbook step 4) still covers it.

## X-REG-LINK-CDN14 — 14 locators refused by publishers' CDNs

- **Dated attempt:** 3 Oct 2026 (B13d): IMF ×6, OECD ×2, MDPI, ResearchGate, UNDP, WB Fast Payments, RPW ×2 refused automated requests. 10 Oct 2026: the IMF CR 26/80 PDF opened by curl (W0 A2); RPW still refused (EXT-12); the rest not re-checked.
- **Human step:** Open each locator listed in `audit/release_candidate/LINK_CHECK.md` in a browser; record OK, moved or broken.
- **Record it changes:** Each source's `primary_url`, Master-first if it moved.
- **Public state meanwhile:** The cards link them; none is known to be broken.
- **Cadence:** At release (runbook steps 4 and 12); then each new edition.
- **Who:** A person with a browser

## EXT-40 — Owner's aggregate file for the 2021-wave domestic transfer channels (D16)

- **Dated attempt:** 11 Oct 2026 (CLOSE-6E, instruction v5 item 6C-6): `audit/close_out/fixtures/findex_yem_channels_aggregates.json` has not arrived, so the item was not run. The respondent file was not read and no World Bank Microdata API key was used, requested or stored (D16).
- **Human step:** The owner runs `findex_domestic_channels_aggregates.py` on the respondent file under the World Bank's terms and commits the script and `findex_yem_channels_aggregates.json` (aggregates only, never the data) under `audit/close_out/fixtures/`. Claude Code then checks the four anchors (account at a financial institution 11.9; received domestic remittances 31.9; sent 17.7; sent or received 37.8) and stops the item if any fails to reproduce.
- **Record it changes:** A new Evidence Record FINDEX-YEM-DOM-CHANNELS (class CAUSEWAY_DERIVED_AGGREGATE, with a D9 route), bound to `/remittances/`, `/people/` and MA-001; MA-001's sentence on channels.
- **Public state meanwhile:** MA-001 says the channels through which the money moved are not shown; CWR-012 says that no weighted estimate of the channel usable here is published or held for the 2021 wave, and that the World Bank's variable documentation records the item as asked and answered.
- **Cadence:** When the owner supplies the file.
- **Who:** Owner (runs the script); Claude Code (the transaction)
