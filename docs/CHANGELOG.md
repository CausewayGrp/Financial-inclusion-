# Repository Change Log

## 2026-10-09 — V1B-1: interface labels for design integration Phase B (owner decision B-b)

One Master transaction, labels only, English and Arabic together (`audit/design_integration/`): the summary label of
the `/finance/` chronology list, "About this source" for a `/data/` source row, the currentness strip ("Sources checked
up to {date}") with the edition's check date, the Evidence Colophon labels and the hub numerals 01–05. No figure, unit,
period, universe, source or record changed; no page changes until the renderer uses them. Gate CS-01 holds the check
date equal to the date `/corrections/` section 3 states and to the edition label, in both languages. Master
`fdb24bdfeae5` → `cf5254825da8`.


## 2026-10-09 — V1 design integration, phase 2 (disclosure and density; not accepted)

Renderer and stylesheet, no governed text or contract changed (`design/DESIGN_INTEGRATION_V1.md`, DL-V1-009…012): the
depth figures of the domain answers and the dated chronology list on `/data/` become disclosures named by their existing
governed labels; one disclosure pattern for every governed `details`; the phone's in-page index as a row of chips; two
cards to a row on tablets; source rows on wide screens. Phone length (Arabic, 390 px): `/data/` 77.8 → 57.2 screens,
`/payments/` 30.9 → 19.9, `/firms/` 20.5 → 16.7, `/people/` 16.9 → 15.3. Home and `/finance/` need a contract tier or a
governed label first (`design/ESCALATIONS.md`, V1 phase 2). Not accepted: acceptance is the owner's.


## 2026-10-09 — V1 design integration, phase 1 (screen stylesheet; not accepted)

The owner's palette and hierarchy on the accepted D7 structure (`design/DESIGN_INTEGRATION_V1.md`, DL-V1-001…008):
warm paper, one green, sage and brass; a one-row product bar; a deep-green colophon with the logo on a paper tile; key
figures, numerals and calls to action in green; "does not establish" as a sage panel under a brass double rule; white
figure plates; one filter-bar pattern. Screen only: the 288 documents are byte-identical and print is unchanged. No
content, Master, controlled contract, `app.js`, test or gate changed; no font added. Three accessibility defects the
full audit found are fixed in the stylesheet; the social images are regenerated. What needs copy or a contract is
escalated (`design/ESCALATIONS.md`, V1). Not accepted: acceptance is the owner's. Public release is not declared.


## 2026-10-04 — Non-design v1 front door

README, the current-state projection and the re-entry checkpoint now say the non-design v1 product is complete, the current phase is design / presentation integration, and C1–C3 are post-v1. Public release is not declared. Three documentation diagrams added. No Master or product change.


## 2026-10-04 — B3 decision, Batch C held, Batch D records

- **B3.** The 24 chronology events are not search results. They have no event route and no search-eligibility field. Search stays evidence, measurement and source.
- **Batch C.** C1 (typed difference block), C2 (dedicated guarantee record) and C3 (public contradiction register) stay unbuilt. Each needs a new surface. The existing public forms stand.
- **Batch D.** Programme records no longer call pull request #9 the current release candidate. Pull requests #9 and #10 are merged. The open content pass is pull request #11. Not declared: content complete, or public release ready.


## 2026-10-04 — FC-2, FC-3, FC-3b: source locators; a false "no later value" claim removed

Master `2713c086b7f9…` → `1fa11bad82ed…` (FC-2) → `439fdce82563…` (FC-3) →
`fdb24bdfeae5c2604e326dd19effb4d79a783d44272f4dc08da2373979893999` (FC-3b), through `run_stage.py`.

- **FC-2 — locators.** Two broken links fixed: `SRC-CBY-SANAA-C14-2024` pointed at the *wrong document* (the 537-page
  UN Panel of Experts report, not the circular — the circular is reproduced inside it at printed page 114), and
  `SRC-CBY-SANAA-C12-2024` returned HTTP 404. The CBY-Aden monetary series' own index, the bank's regulations and
  publications pages and its **thirteen 2021–2022 issues** now stand beside the single May 2026 issue that all 686
  monetary observations had been traced to. Two Yemen e-money and microfinance papers added; the two IGC documents
  added to the record that held only their landing page. The SFD newsletters and the IGC paper were **already
  present**, contrary to the brief's premise, so they were not duplicated. What could not be opened — the SDRPY
  notice, the OECD youth paper, the World Bank FASTT paper, the UNDP FMIIP page — is recorded with its reason and
  carried to the handover; nothing is published from any of them.
- **FC-3 / FC-3b — currentness.** Five records and one page section claimed, in both languages, that no weighted value
  later than 2014 existed for saving, borrowing and domestic remittances. The World Bank publishes 2022 values in the
  same series and the respondent file reproduces them exactly, so the claim was false. `CLM-026` — whose three stated
  preconditions for publishing a weighted estimate are now all met — carries 21.6% saving, 51.3% borrowing and 9.3%
  digital payments with their derived intervals; `/people/` leads with them and keeps the 2014 source-and-method
  detail below, named as 2014.
- **Three restraints kept:** no 2014→2022 difference is computed (the publisher's own two vintages disagree, 65.9 vs
  66.0 — finding FC-A-04); no 2022 domestic-remittance value is published (that series holds no 2014 value to read it
  against); and a digital *payment* is not account *use*, so the access/use ladder is unchanged.
- **Records:** `audit/final_content/FINAL_CONTENT_LOG.md`.

## 2026-10-04 — FC-1, FC-1b: margins of error for every published Global Findex figure

Master `f3e06fb935d0…` → `9d059c07309a…` (FC-1) → `2713c086b7f98c0145e48a21d31812cdefebef7e90cd1364de51954b078e968e`
(FC-1b), through `run_stage.py` (`audit/final_content/fc_1_findex_margins.py`, `fc_1b_gap_bases.py`).

The owner supplied the Yemen Global Findex respondent file with the message of 4 October 2026, under the World Bank
Microdata Research License, with the decision to publish aggregate statistics only. Edition 2 (E2-2) had recorded that
no interval could be computed because the file needed a login, and left the public text saying the uncertainty "is not
quantified here". That sentence is now gone from both editions.

- **Method, recorded as a CauseWay derivation:** Hájek ratio estimator on the published weight `wgt`, design-based
  variance by Taylor linearisation, 95% interval. The public-use file carries no PSU or stratum identifier, so
  clustering is not captured and the true interval may be wider, never narrower — stated publicly, not buried.
- **Reconciled against the publisher before publishing:** all nine published World Bank values for Yemen, and the three
  other 2022 indicators of the same wave, reproduce from the file to the World Bank's own unrounded values. No
  difference to record. Two base definitions were settled by that reconciliation and are recorded: "ages 25+" is the
  complement of 15-24 (n = 770), and `female` is coded 1 = female, 2 = male — which releases the owner's hold on
  by-sex figures on two independent confirmations.
- **Published:** 17 derivation rows `CW-FINDEX-MOE-2022-001`…`-017` in `25_FINDEX_BASELINE`, each with its point
  estimate, interval, base, design effect and method; the intervals printed on `CLM-002` and `VIS-FINDEX-GAPS` in both
  languages; the method on `/methodology/` section 7.
- **Design effect stated honestly:** 0.82 to 1.82 across the fourteen estimates — for two small domains a binomial
  standard error slightly *overstates* the uncertainty, so no single direction is claimed.
- **Rights:** `28_METHODS_RIGHTS` records the custody rule (`respondent_microdata_controlled` NO → YES; aggregate
  statistics only; never redistributed, never committed), and `SRC-WB-FINDEX-001` carries the licence and the citation
  the licence requires. The respondent file is not in this repository, `dist/` or the site.
- **Gate:** `FC-MOE` in `scripts/validate.py` — the intervals asserted on what a reader sees, their attribution to this
  resource, their clustering limit, and the arithmetic of every derivation row; four negative controls.
- **Records:** `audit/final_content/FINAL_CONTENT_LOG.md` (with the findings the reconciliation opened), `audit/INDEX.md`.

## 2026-10-04 — E2-8, E2-7b, E2-7c: chronology states, gates E2-READ and E2-DATES, the review folded in

Master `332a942f6685…` → `6d10b18d6c00…` (E2-8) → `7222cb53d2ce…` (E2-7b) →
`f3e06fb935d0181211cc73f648eff588388ddda41a4c8f7eb2406b8396333514` (E2-7c).
- **E2-8:** the 24 chronology events carry value states (14 `value_states`).
  - YSC-003 and YSC-005 are dated as their sources date them (2016; March 2018).
  - YSC-007 binds the SPA item that dates the 2018 deposit.
  - YSC-021: the Board "approved"; its press release bound.
  - YSC-023 is labelled as not re-read.
  - Source dates filled.
- **E2-7b:** the gaps the new gates found (QUAL-001 dates, locators, the POS February 2026 change) and CLM-054's
  savers universe (microfinance banks).
- **E2-7c:** the independent bilingual and adversarial review of E2-7.
- **Gates:** E2-READ and E2-DATES in `scripts/validate.py`, five negative controls.
- **Records:** `audit/edition_2/CONTRADICTION_REGISTER.md`; edition-2 log and open-items addendum.

## 2026-10-04 — E2-7: a state for every published value; discrepancies fixed Master-first

Master `dd14eed79a97…` → `332a942f6685e1463301f17d5bb1475cc2c341fab6b323ae06859c74b7f6914c` through `run_stage.py`
(`audit/edition_2/e2_7_value_states.py`; inputs in `audit/edition_2/inputs/`). The originals were re-read on 4 October 2026.
- **06 `value_states`** (new column, projected as JSON): one state per printed value and date of the 109 records the
  literal audit traces (READ with locator, DERIVED, SITE, SEE, UNREACHABLE, TRIVIAL).
- **Fixed, both languages:**
  - POS limitation: every release since March 2025 is a one-page infographic, not "from July 2025".
  - CLM-059 and /firms/: SMEPS reports the USD 54.7 million as disbursed.
  - CLM-062: Figure 114, with the base of 217 on pp. 139 and 141.
- **Bound:** sources read for a value now bind to its record (13 records).
- **Named beside their values:**
  - CLM-049, /reforms/ (the IMF release, 403): not re-read.
  - CLM-020 and MF-ORIG-001+002 (the 2012 SFD document): not re-read.
  - VIS-REMITTANCE-COST: reproduced exactly from the RPW quote-level dataset (8 and 6 quotes, one 22.71% outlier named).
- **CLM-032 (lead 1):** the 2021 and 2022 remittance vintages in four CBY-Aden annual reports.
- **Source library:** retrieval and document dates filled in 15.
- **01:** the v0.42R3 lineage recorded.
- **Renderer and runtime:** a printed table number ("4-1") is isolated left to right in Arabic.

## 2026-10-04 — E2-6, E2-6b: the IMF on correspondent banking, each speaker named; docs/JUDGEMENT.md

Master `e81b2ebc4068…` → `4ae052c9e51a…` (E2-6) → `dd14eed79a97c5222d989ef8fb251aa4b0493c1b3889b215d267e6f2643b8dc7`
(E2-6b, review folded in). IMF Country Report No. 26/80 (owner-supplied PDF): the Executive Board's assessment (PDF p. 4)
and the statement by the Executive Director for the Republic of Yemen (PDF p. 90) join QUAL-001 beside the OECD, each
attributed; neither counts relationships, and a relocation is not a measure of de-risking. `docs/JUDGEMENT.md` (one page)
joins AGENTS.md's reading order.

## 2026-10-04 — Edition 2 records: the lane's dispositions, what was not built, what the owner could supply

`audit/edition_2/EDITION_2_LOG.md` closes with the candidates recorded and not built (e, the Findex waves drawn; f, phone
length, measured and handed to Design; d's next form; a's remainder; b's intervals), the two documents the owner could
supply (the Global Findex 2021 microdata for Yemen; IMF Country Report No. 26/80) and a short self-critique.
`audit/release_candidate/OPEN_ITEMS_DISPOSITION.md` gains an edition-2 addendum (R-11, REOPEN-INTL, S5-GUARANTEES,
S5-CORRESPONDENT, S5-DERISKING, N1115-4.3, E2-PAIRS, E2-PHONE, the payment-rails wording). No Master change.

## 2026-10-04 — E2-5, E2-5b: guarantees and correspondent banking, read in the originals (edition 2, candidate a)

Master `7cc4fafc0116…` → `a01011868a4b…` (E2-5) → `e81b2ebc40687fb344bb1c155ae85208b5b9f62dd1e59d4687bb0d88d480d229`
(E2-5b, the independent bilingual and adversarial review folded in) through `run_stage.py`
(`audit/edition_2/e2_5_guarantees_correspondent.py`, `audit/edition_2/e2_5b_review_fixes.py`).
- **Read in the original.** The OECD's HTML refuses automated requests (HTTP 403), but its full-report PDF does not:
  Promoting Economic Resilience in Yemen (OECD, 2026), printed page 32, gives the Yemen Loan Guarantee Program's 5,731
  guaranteed transactions since 2017 and, in nominal terms, a cumulative USD 42.8 million of guarantees for USD 63.6
  million of loan principal; the same page confirms the SMEPS facts. OECD-YEM-012 to 017 become CONFIRMED.
- **CLM-059** (now "Programme reach describes the programmes, not all MSMEs in Yemen") carries the YLG volumes beside
  SMEPS, each with its own source, with the boundaries: a guarantee volume is not firms' access to finance;
  transactions are not unique firms; the two programmes' figures must not be added; the cumulative period has no stated
  end. /firms/ section 7 carries one paragraph. No new route: a new Evidence Record would need the steward's navigation
  contract.
- **QUAL-001** (the OECD's qualitative interpretation, /finance/) carries the OECD's correspondent-banking sentence
  (confidence of several foreign correspondent banks severely undermined; perceived money-laundering and
  terrorism-financing risks), with the boundary that it counts no relationships, dates no change and is not a measure of
  de-risking.
- **Not bound:** IMF Country Report No. 26/80's statements (imf.org 403; IMF eLibrary 202 with no body). Owner input in
  audit/edition_2/EDITION_2_LOG.md.
- Gate E2-YLG: every page printing the guarantee volume says it is not firms' access to finance; one negative control.

## 2026-10-04 — E2-4, E2-4b: "Why the numbers differ" where contradictory-looking numbers meet (edition 2, candidate d)

Master `1c107148bd92…` → `04c727047a76…` (E2-4) → `7cc4fafc0116e352aabec49783b0c450ce4653a7cceefa6943e4f7f99c0349e1`
(E2-4b, the independent bilingual and adversarial review folded in) through `run_stage.py`
(`audit/edition_2/e2_4_why_numbers_differ.py`, `audit/edition_2/e2_4b_review_fixes.py`).
- A sweep of every record that prints a number on the eight domain pages found three pairs a reader meets without an
  explanation (the remittance revision, 22% vs 91.84% and the POS series already have one):
  A. 2,102,484 e-wallet subscribers (CBY-Aden, first half of 2025; CLM-010) and 375,252 active e-wallet accounts (FMIIP
     baseline, January 2025; FMIIP-BASELINE-2025-01), on /payments/ and /reforms/;
  B. 807,919 e-money accounts (IBS study of five providers, December 2019; CLM-050) and 414,631 to 581,075 subscribers
     (CBY-Aden, 2024; CLM-010), on /payments/ — it read as a fall;
  C. the 2025 roster (79, 195, 108; CLM-016) and the 2026 roster (100, 231, 111; CLM-009), on /providers/ — it read as
     new providers.
- The same treatment each time, from what the records govern: a paragraph that opens "Why the numbers differ:" /
  «لماذا تختلف الأرقام:», names both numbers with publisher, date and the counterpart's record ID, says what each counts
  and what the gap cannot be read as; and in both records' limitations a sentence that names the counterpart by record
  ID and measure, never by its number.
- The review's blocking finding, fixed in E2-4b: E2-4 had written each counterpart's number into the other record, so
  the literal closure traced CBY-Aden's 2,102,484 to the World Bank project record (hard rule 5). Now each number traces
  to the record that governs it; CLM-010 is bound to /reforms/ and FMIIP-BASELINE-2025-01 to /payments/ for that.
  Wording for pairs A and C now rests only on governed statements ("carry different labels … not reconciled"; "this
  evidence base has not compared the two rosters entry by entry").
- Renderer: in a right-to-left document the one isolation pass (`isolate_document`) now isolates identifiers in
  running text too (FMIIP-BASELINE-2025-01 in Arabic prose), so their digits never read as a date (RC-DATES).
- Gate E2-DIFF: the explanation paragraph on each page and record of a pair, and each pair number's trace to its
  governing record in the literal closure. Three negative controls, all caught; the negative-control runner can now
  fault a file under `audit/`.
- Not built here: a typed "difference" relation rendered as its own block. A new section on a domain page needs the
  steward's presentation contract; recorded as the next form in audit/edition_2/EDITION_2_LOG.md.

## 2026-10-04 — Two negative controls re-aimed after E2-2

CI on `8377b7a`: two content-parity controls ("a domain answer drops a governed sentence", "a page prints an ungoverned
number") changed nothing, because their selectors named the two-decimal Findex text E2-2 replaced ("a gap of 12.55
percentage points", "19.53%"). They now name the current text ("12.5", "19.5%"); both are caught again. No gate
changed.

## 2026-10-04 — E2-3, E2-3b: one same-source context row beside Yemen's account ownership (edition 2, candidate c)

Master `39d06c358abd…` → `f6e15a16851f…` (E2-3) → `1c107148bd9268b279f5f522b02260c2b3a7737e6c5cda0343534e8fb88273f5`
(E2-3b, the independent bilingual and adversarial review folded in) through `run_stage.py`
(`audit/edition_2/e2_3_findex_context.py`, `audit/edition_2/e2_3b_review_fixes.py`). Closes REOPEN-INTL.
- "Missing input: the owner should supply Findex aggregates" was not true: the World Bank publishes them in the Global
  Findex Database 2025 file, linked from the page CLM-001 already cites. The row "Low income", 2021 wave, account
  ownership is 0.351821646573129; reproduced twice (this session and the reviewer, independently) as the
  adult-population-weighted mean of the 19 low-income economies surveyed in that wave, Yemen's 2022 observation among
  them (Yemen weighs 6.6%; without Yemen 36.8%).
- CLM-001 (summary, method, limitations) and /people/ section 2, English and Arabic: "For context, the World Bank's
  figure for the same survey wave across the 19 low-income economies surveyed in it, Yemen among them, is 35.2%", with
  "context, not a benchmark, a target or a ranking", what it averages, the classification named by its source, and
  that Yemen's own figure covers only the areas surveyed. One row only; the income group rather than the region
  (reasons in the transaction). Data row WB-FINDEX-CTX-2021-LIC in 25_FINDEX_BASELINE with the file's locator.
- Gate E2-CTX: every block a reader sees with the figure names what it averages (low-income, 19), and it never reaches
  Home. Two negative controls, both caught.

## 2026-10-04 — E2-2, E2-2b: one display precision for every Global Findex figure (edition 2, candidate b)

Master `51a7f1930fcd…` → `d0bd9324c18e…` (E2-2) → `39d06c358abdfb06ef350014e6a3407e7a91871918f7af1e5a2b105ea183f514`
(E2-2b, the independent review folded in) through `run_stage.py` (`audit/edition_2/e2_2_findex_precision.py`,
`audit/edition_2/e2_2b_review_fixes.py`). Finding R-11 of the independent review of `70398d1` (X-ESC-D3-03b).
- **The rule** (/methodology/ section 7, English and Arabic): every Global Findex share prints to one decimal place,
  rounded from the World Bank's unrounded values, and a gap is the difference of the printed shares. One decimal
  matches the World Bank's own Yemen table (The Little Data Book on Financial Inclusion 2015, p. 159); the page says it
  is a display convention, not a claim of accuracy to a tenth of a point.
- **Values** from the Global Findex Database 2025 file (unrounded, read on 4 October 2026): women 5.4, men 18.3 (the
  old 18.35 was itself a rounding of 18.345; rounding it again would have given 18.4), primary or less 7.0, secondary
  or more 19.5, ages 15–24 5.0, ages 25+ 16.1; gaps 12.9, 12.5, 11.1, 9.0. 31 text cells in 02, 03, 06, 10 and 11, six
  values in 25_FINDEX_BASELINE, the VIS-FINDEX-GAPS guards in `controlled_inputs/visual_design_contract.json`.
  "About 9.0" lost its hedge (the gap is exact under the rule); Arabic «نقطة» after a decimal.
- **Intervals:** none is published for Yemen's 2022 survey and the microdata needs a login, so none is computed; the
  limitations already say so. Owner input: the microdata file (audit/edition_2/EDITION_2_LOG.md).
- **Renderer:** VIS-FINDEX-GAPS prints every value at the panel's published precision (7.0, not 7), in the bars and the
  table (`scripts/yfie/visuals.py`). P3-G02 compares values with trailing zeros dropped (7.0 = 7).
- **Gate E2-PREC** (validator) asserts what a reader sees: no Findex share or gap with two decimals on any Findex
  record, /people/ or the gender-gap Reading; no two-decimal number within 0.05 of a Findex share or gap on any page;
  every drawn Findex value at one decimal. Three negative controls, all caught. The home and /people/ numeric
  signatures read 12.9.

## 2026-10-04 — E2-1, E2-1b: FPS and RTGS at 31 August 2025 (edition 2, first transaction)

Master `90014e3bd271…` → `594abed998bb…` (E2-1) → `51a7f1930fcd21e514d608785abdb2a8887eeb6d4e2d591629477b87ebb7da75`
(E2-1b, the independent review folded in) through `run_stage.py` (`audit/edition_2/e2_1_payment_rails_isr.py`,
`audit/edition_2/e2_1b_review_fixes.py`; ledgers and reports in `audit/edition_2/runs/`). Branch `code/edition-2`.
- VIS-PAYMENT-RAILS, CLM-018 and section 3 of CWR-009 said "no later operational state is recorded" while
  VIS-PAYMENT-RAILS cites the World Bank's ISR sequence 2 (8 April 2026), which reports FPS and RTGS "developed and
  operational: No" at 31 August 2025 (pp. 3–4) and the RTGS tender launched, the FPS tender expected shortly (p. 2).
  The boundaries now say so, with "the day before the project became effective" so the status is not read as a stall;
  "no later operational state" stays. CLM-018 gains the ISR as a source.
- Gate RC-A1 keeps day-precise dates of undrawn steps out of a chain figure's text alternative, so the dated state sits
  in the figure's boundary and the text alternative says it without a date.
- The Arabic of CWR-009 section 3 names the fast payment system «نظام الدفع السريع», as every other cell does.
- Four social images regenerated (CLM-018, VIS-PAYMENT-RAILS, both languages).

## 2026-10-04 — RC-19: the fix batch from the independent review of 70398d1

Master `c700dc52bf81…` → `90014e3bd27133c34b8435090230cf5b28a3301dec9f366c6fedf047b5ea2838` through `run_stage.py`
(`audit/release_candidate/rc_19_independent_review.py`; ledger and report in `audit/release_candidate/runs/RC-19_*`).
Owner message of 4 October 2026, about 00:10 Aden (the freeze lifted for this batch only), and the owner decision of
3 October 2026, 23:54 Aden. English and Arabic changed together.
- **R-01, the FMIIP dates.** "Started in July 2025" came from the UNDP project page, which refuses automated requests
  and was never read here. The World Bank's ISR (sequence 2, SRC-WB-FMIIP-ISR2-2026-001, read on 4 October 2026; the
  same in sequence 1) gives Board approval 17 June 2025, signing 26 June 2025 and effectiveness 1 September 2025, and no
  start date. The prose of VIS-PAYMENT-RAILS and RV-CWR-009 now gives approval and effectiveness. The event
  REF-PAY-002 is "FMIIP effective", 2025-09-01; the three components are dated 2025-06-17, labelled "approved with the
  project". All four are bound to the ISR. The access component carries the ISR's name ("support for access to and use
  of the payment infrastructure"); "access-point database" and the IRG-areas qualifier, which only the UNDP page gave,
  are dropped from the public text.
- **X-ESC-RC17-01, owner decision of 3 October 2026, 23:54 Aden.** /evidence/NEG-EW-011/ is no longer published as its
  own record: its 02 and 06 rows are removed, with its design-intent entry and its route in the navigation contract
  (steward patch under the owner's decision). Its address leads to CLM-015 through a page that is never indexed, names
  CLM-015 as canonical, says why in two governed labels and moves on without JavaScript
  (`site-src/hosting/moved_routes.json`, `render.moved_page`). Its two social images are removed. The circular's names
  stay non-public lineage in 22_PROVIDERS_DATA, where RC-NAMES reads them. No other published per-entity record has an
  ID equal to an item number of a document it links (PSE-011's ID is the programme's own). Counts: 142 page specs, 109
  Evidence Records, 438 search records, 284 social images.
- **R-08, /privacy/ section 3.** It now says what is decided: hosted on DigitalOcean App Platform, reached through
  causewaygrp.com, which receives each request (and the corporate cookie, if the browser holds it) and passes it on.
  Which details are kept, for what purpose, for how long and by whom stays open. Runbook step 9a re-confirms it.
- **R-05, no JavaScript.** The language switch is a link to the same route in the other edition; the menu is a link to
  the footer, which carries every navigation and trust link; the runtime enhances both. The note now names exactly what
  needs JavaScript (search, Compare, the copy and print buttons). New browser test `scripts/tests/test_no_javascript.py`
  with its own negative control; in CI.
- **R-10.** Only the first sentence's figures are emphasised (`render.fig_emph`): the 23% coverage figure on Home is set
  like the text around it.
- **R-04.** `deploy.yml` starts only after the workflow "Verify" has succeeded on a push to `main`, and deploys the
  commit Verify proved; a manual run calls the reusable Verify first.
- **R-07.** `scripts/do_deploy.py` changes only the image tag of the app's live specification, and refuses to deploy
  while a rollback is pinned.
- **R-09.** `scripts/tests/test_corporate_proxy.py` runs the runbook's forwarding middleware, extracted from the runbook,
  in a pinned Nitro 2.13.4 harness (`scripts/hosting/corporate_proxy_harness/`) in front of our nginx block: every page
  under the header test, no corporate header or cookie, the cookie never upstream, with a negative control. It found
  that the bare-path 301 still carried the corporate headers; the runbook's middleware now removes them there too.
  Not in CI (it installs from npm). The runbook's step 8 adds the web administrator's check of where those headers
  originate.
- **R-17.** The App Platform image is pinned to `nginx:1.24.0-alpine@sha256:77e5d4a6…`, the nginx version the gates
  prove; `test_digitalocean_hosting.py --image` runs every header check against that image, in CI.
- **Gate RC-19** (`scripts/validate.py`), with six negative controls, 6 of 6 caught: FMIIP never dated to July 2025;
  the retired address (page, links, search, social image); the switch and the menu are links; first-sentence emphasis;
  the deploy gating and the digest pin are asserted too. The header test waits for a page that moves on.
- **Records.** The owner decision of 23:54 recorded verbatim; the 13:00 note, whose quotation was empty (R-03),
  appended as a dated erratum; R-02's three section-5 reasons, R-13, R-14 and the next-edition items (R-11, R-15, R-16,
  the unprojected sheets) appended to `OPEN_ITEMS_DISPOSITION.md`; X-ESC-RC17-01 closed in `design/ESCALATIONS.md`;
  runbook step 2 rewritten (R-12).
- **Reviews.** One bilingual reviewer read the changed pairs, Arabic first: four NOT ACCEPTABLE with replacements, all
  folded; it then re-read the three pairs the adversarial review changed (the Reading's FMIIP clause, the component
  labels, /privacy/) and returned three more exact replacements ("development", as the World Bank says, not
  "establishing"; «ملف تعريف الارتباط»; the bank's house name), all folded. The adversarial reviewer read the FMIIP
  dates, NEG-EW-011 and /privacy/; its findings are folded, except two recorded in the pull request with their reasons.
  The transaction was then run once, from the committed state.

## 2026-10-03 — B16: every open item dispositioned; G0 in the browser; 4.3 and 4.4 to the next edition

- `audit/release_candidate/OPEN_ITEMS_DISPOSITION.md` (new, with an `audit/INDEX.md` row) is built by
  `audit/release_candidate/b16/make_disposition.py`. It has 221 items: 93 DONE, 18 RELEASE, 88 NEXT EDITION and 22
  REJECTED, with none undecided.
  - It adds the owner note of 11:15 (4.1–4.6 and G0), section 5's seven topics with one line each (correspondent
    banking, de-risking, SWIFT, liquidity, hawala, G2P, guarantees), the three rejections reopened for challenge, and
    the G0 findings.
  - Commit placeholders are resolved against the live ancestry. POST-LAUNCH is printed as NEXT EDITION.
  - One earlier DONE is corrected: Dataset structured data was never prepared, and F6-G04 still forbids it, so it is
    NEXT EDITION.
- **4.3 (Findex waves): NEXT EDITION.** No governed contract takes the three waves, and RV-CWR-004's people lane is
  governed as 2022–23 fieldwork; adding 2011 and 2014 would widen it. The record already prints all three
  observations, with the 2011 definition limit and the 2022 coverage, on /people/.
- **4.4 (the two ladders): NEXT EDITION.** The B12 inputs are still missing: the recipients' reference period, a data
  projection, and governed Arabic step labels.
- **G0.** 22 views at 390 px in Arabic and 1440 px in English. There is no release defect beyond the inline-figure box
  already fixed. CWR-005 is bounded. The regulation path names the instrument, the authority, the date and the stage
  the evidence reaches. 29 of 30 ordinary searches land right ("ID" is next edition). The guided paths resolve.
- Each item's own record gains one dated, append-only block pointing here: `design/ESCALATIONS.md`,
  `FINAL_OPEN_ITEMS_REGISTER.md` and `design/DESIGN_DEBT.md`.

## 2026-10-03 — RC-1115: the inline-figure defect fixed and the presentation gate; 4.6 records; DigitalOcean hosting

**B.0, a release defect from RC-18 (`f7deaac`).** RC-18 emphasised inline figures as `<b class="fig">`, but `.fig` is
the figure frame in the stylesheet (background, padding, margin, a 3 px top border). Every emphasised figure therefore
rendered as a padded box that covered the line above it: on Home at 390 px in Arabic, the 5.44% box hid «الرجال» and
the 23% box overprinted «البنك الدولي 2022)»; on CLM-001 at 1440 px in English, the 11.9% box covered "ownership". The
browser suites passed, because nothing tested for it.
- **Reproduced first.** `audit/tranche_c/checks/viewport_acceptance.py` now fails when an inline `<b>` in `<main>`
  carries box styling, or an emphasised figure is taller than its line. On the unfixed build: 18 of 168 page-width
  checks failed, on Home and CLM-001, in both languages and at all four widths.
- **Fixed in its owning layer** (no Master change): the renderer emphasises a figure with its own class, `b.fnum`
  (`scripts/yfie/render.py`), and the stylesheet styles that class with weight and size only
  (`scripts/yfie/theme.py`). The `.fig` frame rules are untouched. 168 of 168 pass, and Home in Arabic at 390 px and
  CLM-001 in English at 1440 px were checked by eye.

**RC-1115, the presentation gate** (`scripts/validate.py`), with one negative control per assertion
(`scripts/tests/test_gate_negative_controls.py`; 8 of 8 caught):
1. `b.fnum` carries no padding, margin, border, background or container type; no element except a `<figure>` carries
   the `.fig` class (the B.0 regression); the first sentence of Home's first figure group opens its figures with an
   emphasised one, in English and Arabic. The handoff's assertion of `<b class="fig">` would have locked the defect in,
   so it was replaced.
2. Every Evidence Record with a q3 section names FOR WHOM in its head, before the h1, with the same label and value.
3. Home section 6 links `/evidence/VIS-PAYMENT-RAILS/`.
4. Every HTML page has exactly one icon link, to `/assets/logo/CauseWay_logo_32.png`.
5. `CauseWay_Master_Logo.png` is not in `dist/`.
6. `/measurement/` prints `data-ma-dimensions` on the same cards in English and Arabic, with equal item counts.

**4.6, current-state records.**
- `OPENAI_REENTRY_CHECKPOINT.md` §7: the tag command for `checkpoint/design-handoff-ready` printed the *current*
  Master hash, which is wrong for that commit and which every rebind rewrites. It now reads the hash from the tagged
  commit itself (`git show "$C":authority/…xlsx | sha256sum`) and says what to expect (`17db032b15da…`). No 64-hex
  literal is added, so the P4-G04 gate and `scripts/rebind_authority.py` need no lineage entry. The lineage entry that
  the handoff planned is therefore not added: once nothing prints that hash, nothing needs to whitelist it.
- `authority/YFI_CURRENT_PROJECT_CONTEXT.json`: `programme_state` names pull request #8 ("code: the production runtime —
  EAD-01 to EAD-11") as merged into `main` at `38a9a97` on 2 October 2026, and pull request #9 as the release
  candidate. It no longer says that the runtime "is pull request #8".
- `README.md`: the present-state rows (Now, Next, Owner actions; six merged branches).

**Hosting: DigitalOcean** (owner decision of 3 October 2026, 22:36 Aden; recorded in
`audit/OWNER_DECISIONS_2026-10-02.md`).
- Verified again with one read-only request: `causewaygrp.com` is not on App Platform. It resolves to the single
  DigitalOcean address `206.189.57.121` and sends no Cloudflare edge headers. An App Platform static-site component
  cannot send our security headers. So the route is our own App Platform app running an nginx **service**, reached
  through the corporate site's proxy middleware, which was already adversarially tested.
- `scripts/hosting_nginx.py` writes the nginx server block from the published site's `_headers`, so the header
  contract stays one file. `scripts/tests/test_digitalocean_hosting.py` runs that block in a real nginx and loads
  every page through `test_security_headers.py --base`: 288 pages, 0 problems. It also checks the relative 301s,
  every `Cache-Control`, the sitemap's type and a 404 outside the path, and its negative control (X-Frame-Options
  removed) is caught. It runs in CI's browser job.
- `site-src/hosting/digitalocean/` holds the Dockerfile and the app specification. `scripts/do_deploy.py` and
  `.github/workflows/deploy.yml` are retargeted from Cloudflare Pages to the DigitalOcean Container Registry and App
  Platform. The workflow is still inactive until the owner switches it on, and still refuses a null origin or an
  unconfirmed licence text.
- `docs/RELEASE_RUNBOOK.md`: DigitalOcean is route 1. The same nginx block on the corporate Droplet is route 2. The
  rejected static-site component is recorded with its reason. A subdomain on the same app is the fallback. Cloudflare
  Pages is removed.
- The stale `_headers` rule for the master logo, which is no longer shipped, is removed.

## 2026-10-03 — CI: the negative controls split across six runners; the validator 38 s → 25 s; one control re-aimed

The first CI run of the parallel harness (run 37117577689, on `f7deaac`) did not go green:
- "Gate negative controls" was cancelled at its new 30-minute limit after 54 of 70 controls. The other two jobs
  passed.
- On that 2-CPU runner, one validator run took 30.5 s in the gates job, but two faults side by side took 65 s per
  pair. Workers on one runner gain nothing there.
- One control was NOT CAUGHT: "a governed first-load field is dropped".

Fixed, without weakening anything:
- **Six runners** (`.github/workflows/verify.yml`). A matrix of six shards, `--shard K/6 --jobs 1`, each on its own
  runner. Shard K runs every sixth control from the K-th, so together the shards run each control exactly once. An
  aggregate job, still named "Gate negative controls", is green only when every shard passed. The required check
  keeps its name, and a skipped or cancelled shard turns it red. Each shard's limit is 20 minutes.
- **A faster validator, with the same results** (`scripts/validate.py`):
  - The search mirror's token test checks the literal first: every token pattern contains its token, so a text
    without it cannot match.
  - The secret scan is split. Its case-sensitive key forms each start with a fixed literal. Its case-insensitive
    assignment needs one of its keywords; the keyword test covers the four non-ASCII letters Python folds under
    IGNORECASE. A text holding neither is not searched.
  - Planted secrets of both kinds (an AKIA key, `PassWord = "…"`) are still reported.
  - 38 s → 25 s locally.
- **The uncaught control was the control's fault, not the gate's.** Since RC-18, a record's head prints the universe
  (FOR WHOM) as well as its third answer. So blanking `#q3` no longer removed that field from the first screen, and
  S04.1 rightly stayed silent. The control now blanks the definition (`#q2`), which is printed once, and S04.1
  catches it ("… /evidence/CLM-002/ en definition").
- **Local proof:** the six shards in turn, 70 of 70 caught (12, 12, 12, 12, 11 and 11 per shard, about 110 s each on 4 local workers).

## 2026-10-03 — RC-18: figure first inside D7; /corrections/ invites source institutions; citizen aliases; dimensions; favicon

Master `433f38bf…` → `c700dc52bf81966939c6d6ec53afe494d1bf699389c04850f74b9dec436ea7e4` through `run_stage.py` (script
`audit/release_candidate/rc_18_figure_first.py`; ledger and report in `audit/release_candidate/runs/RC-18_*`). Owner
note of 3 October 2026, about 11:15, sections 4.1, 4.2 and 4.5. English and Arabic changed together.
- **4.1, figure first, inside D7.** D7's Design Intent Lock forbids lifted figures and stat tiles, and keeps Home's
  product statement first. So the figure leads where D7 allows it, rather than as the separate key-figure field the
  triage first proposed:
  - Home's product statement is two sentences.
  - Home's first figure group opens with its figure ("11.9% of adults aged 15 and over …, according to the latest
    representative population measure: …").
  - Every figure in Home's paced groups, and in a record's first answer, is set in the figure weight inside its own
    sentence (`fig_emph` in `scripts/yfie/render.py`; dates, identifiers, ranges and isolated values left alone).
  - A record's head now gives WHEN and then FOR WHOM ("Who or what does it apply to?") before its title.
- **4.2.**
  - /corrections/ invites the institutions whose documents or data are used to request corrections by the same route
    as any reader.
  - Three aliases cover words citizens type that landed wrong or nowhere: 031 «قرض / قروض / سلفة» → /finance/ and
    /people/; 032 transfers abroad → /remittances/, with a boundary note that the evidence covers money sent to and
    within Yemen, not money sent abroad; 033 «كاش», cash-out → /payments/.
  - /measurement/ prints each priority's governed dimensions after a new label, UI-MA-DIMENSIONS ("Dimensions it would
    cover:" / «الأبعاد التي سيغطيها القياس:»).
  - Home's section 6 links the drawn payment-rails chain (VIS-PAYMENT-RAILS) first.
- **4.5.** Every page declares the 32 px logo derivative as its icon, so the console 404 and the request outside the
  base path are gone. `scripts/build.py` no longer copies the unreferenced 9.6 MB master logo into `dist/`; it stays in
  the repository, unchanged.
- **Reviews.** One bilingual reviewer read only the changed pairs and returned NOT ACCEPTABLE with exact replacements.
  All are folded:
  - the dimensions label;
  - alias 032's extra Arabic terms and its boundary note;
  - Home's first sentence ("For each figure, … when and for whom the figure applies") and «تثبته»;
  - "according to the latest …";
  - «سلفة»;
  - alias 033's terms.
  The script records why «كاش» is safe as a search term: RC-NAMES matches the circular's names only with their other
  words.
- **A checker fix.** The first run rolled back on RP-G06 (CLM-043). The figure tag, stripped to a space, left a double
  space, and the Arabic «مليار دولار» rule then read a false "1". `audit/tranche_c/checks/bilingual_invariance.py` now
  collapses whitespace after stripping tags; with that fix, 0 pairs differ.
- **Gates.** Every gate passes:
  - validator; content parity (286); bilingual invariance (143 pairs); literal audit (13,410, 0 unresolved);
    determinism; lineage; diagrams; social images; logo derivatives; exports;
  - public tools 35/36 (1 not applicable); viewport 168/168; security headers (2,712 responses); base path (644
    requests, no favicon request at the domain root).
  The runbook's favicon line is updated. A gate of its own for these presentation rules (RC-1115) is still to come;
  see the pull request's RESUME POINT.

## 2026-10-03 — The base-path work after its adversarial verification: runbook route 1, release checks, counsel step

The adversarial verification of the base-path and noindex commits found the build side sound. `dist/` is
byte-identical apart from the noindex meta; there are no escapes; the controls fail for the right reason. It found the
hosting runbook not ready. Every major finding and every minor one is folded in here. Code, gates and records only:
no Master change, and no public page changes.
- **Route 1 is one server middleware, not `routeRules`** (`docs/RELEASE_RUNBOOK.md`). The verifier ran the earlier
  snippet in a real Nitro 2.13.4 server and found three faults:
  - the bare-path redirect also matched the address with its slash, so the release address redirected to itself;
  - a route-rule proxy cannot strip the corporate `session` cookie, `x-robots-tag` or `x-powered-by`;
  - it follows our host's redirects itself.
  The verified middleware replaces it, with the nginx equivalent. The `script-src 'self'` sentence is corrected: under
  route 1, `'self'` is the corporate origin, and the unchanged body is the guarantee. A service-worker check is added
  for the web administrator.
- **A one-page "Deploy and verify"** at the top of the runbook, written for a stranger:
  - prerequisites;
  - each command with the last line it must print;
  - the ten-minute check (a curl list over eight addresses, the bare address, the slashless redirect, the noindex
    count, the sitemap, the header and tool tests);
  - rollback in three lines.
- **The release check now proves absence** (`scripts/tests/test_security_headers.py`). Every response is read with
  all its headers, through `all_headers()`, because Playwright's `headers` leaves cookies out. The test fails on:
  - any `Set-Cookie`, `X-Robots-Tag` or `X-Powered-By`;
  - any cookie the browser holds after the walk;
  - with `--base`, a missing page that does not answer 404, and a bare address that does not answer one permanent
    redirect (301 from the route, 308 from Pages) to the address with its slash.
  Injecting a `Set-Cookie` into the local server's headers makes it fail, as it must.
- **Counsel before the first deploy.**
  - New runbook step 7a.
  - `site-src/deployment.json` gains `licence_text_confirmed: false`, with its rule. The deploy workflow refuses to
    publish until it is true, because the first deploy makes /rights/ public at the Pages address. RC-B14 requires it
    to be a boolean.
  - `docs/DEPLOYMENT.md` says the same.
- **Addresses built by concatenation are now seen** (`scripts/base_path.py`, `scripts/tests/test_base_path.py`). After
  the runtime patches, every slash-leading string literal outside the base path must be a listed route key, at its
  listed count (`JS_ROUTE_KEYS`: 16 in `app.js`, 1 in `lang-redirect.js`). That covers single, double and back quotes,
  templates included. Anything else stops the build, and the sweep applies the same rule. The verifier had shown that
  `'/'+lang+'/about/'` and `` `/${lang}/about/` `` passed the earlier rule ("a literal naming a top-level folder"). A
  second negative control appends `'/'+'en'+'/about/'` to the runtime, and the sweep must report it.
- **Minor.**
  - Route 2: edge caching cannot be turned off for static sites.
  - Route 3: add the custom domain to Pages before the CNAME (otherwise error 522), and give the 301 in middleware form.
  - The noindex covers pages only; the sitemap, search data and images are accepted without an `X-Robots-Tag`, with
    the reason recorded.

## 2026-10-03 — CI: the negative controls run side by side on isolated copies; owner note of 13:00 recorded

- **The controls job could not go green** (owner note of 3 October 2026, 13:00, point 1). "Gate negative controls"
  was cancelled at its 45-minute limit on `da63bfb`: one full validator run per control, run one after another. The
  validator was already cut from 83 s to 38 s (`d06f8bd`). The harness now runs the controls in parallel, each on its
  own copy of the tree (`scripts/tests/test_gate_negative_controls.py`):
  - **Isolated copies.** It makes one full copy of the work tree per worker: every file Git tracks or would track,
    `dist/` included, copied rather than hard-linked. A fault is written and its gate run only inside one copy, so
    no fault can reach another or the repository.
  - **Workers.** There is one worker per CPU (`--jobs N`). `--shard K/N` splits the controls for a job matrix, with
    nothing dropped.
  - **Stronger than before.** Before any fault, every gate a control relies on runs once on the clean copies and must
    pass. No control's expected message may already appear in that clean output: a message the clean tree prints
    would prove nothing. The old harness checked neither.
  - **CI.** `.github/workflows/verify.yml` runs the controls with `--jobs "$(nproc)"`, inside the same single job, so
    the required check keeps its name and no runner minutes go on extra jobs. Its timeout goes from 45 to 30 minutes.
  - **Local proof.** On 4 CPUs, all 67 controls of `80da278` ran on 4 copies: 67 of 67 caught in 11 min 41 s of wall-clock time (39 min of CPU), against about 42 minutes run one after
    another; the clean copies passed first. The full run of this head,
    70 controls, is in the pull-request log.
- **`providers_data.json` is non-public lineage, and RC-NAMES would catch a renderer that printed it** (13:00, point
  3). Confirmed:
  - `site-src/content/data/providers_data.json` is the generator's projection of the Master sheet 22_PROVIDERS_DATA.
  - It is read only by the generator's tests, the handoff inventory, the validator (RC-NAMES takes its patterns from
    the lineage labels) and these controls. No renderer, export or social-image script reads it, and `scripts/build.py`
    copies only `search_index.json` and `search_aliases.json` into `static-data/`.
  - The NEG-EW-011 name occurs in no other file under `site-src/` (one English and one Arabic label in this file).
  - Three controls now prove the second half, so it no longer rests on reading the code:
    - a renderer that prints NEG-EW-011's English lineage label, escaped as a page would print it, is caught;
    - so is one that prints the Arabic label;
    - a build that copies the whole projection into `static-data/` is caught.
    The third control first appended the projection to an existing JSON file. That made the file invalid, the
    validator stopped before RC-NAMES ran, and the harness reported the control NOT CAUGHT, which is its job.
    A control may now add a file the build never writes (`static-data/providers_data.json`); the file is removed
    afterwards.
- **Records.** The owner note of 13:00 is recorded verbatim, append-only, in `audit/OWNER_DECISIONS_2026-10-02.md`,
  with the owner's acceptance of the /about/ wording "against the sources it names".

## 2026-10-03 — Owner B3: every page says noindex, nofollow until release

Crawlers ignore a `robots.txt` that sits under a path, so until release the pages say it themselves (owner decision B3).
- **The flag.** `site-src/deployment.json` gains `"pre_release": true`, with its rule. `scripts/discovery.py` gives
  one robots meta. While the flag is true, every page carries `<meta name="robots" content="noindex, nofollow">` in
  its head: the 286 localized pages, the root entry and the 404, whose `noindex` becomes `noindex, nofollow`.
  `dist/` changes by exactly that meta in each of its 288 HTML files, and in nothing else (checked file by file).
- **Release.** At release the flag goes false: the meta disappears and the 404 keeps its own `noindex`. The runbook's
  step 13 now does this after the owner's acceptance, together with the web administrator's sitemap step. Step 3
  keeps the flag true. `docs/DEPLOYMENT.md` states it, and the deploy workflow prints it.
- **Gate RC-NOINDEX** (`scripts/validate.py`). `pre_release` must be a boolean. While it is true, every built page
  carries exactly one robots meta, the pre-release one, in its head. Once it is false, no page but the 404 says
  noindex. F6-G05 accepts either form of the 404's noindex. The new negative control, "a page loses its pre-release
  noindex", is caught.

## 2026-10-03 — Owner B1, B2, B5: the site under https://causewaygrp.com/financial-inclusion-evidence/

Code, gate and runbook; no Master change and no public page changes. `dist/` was built before and after and all 598
files keep their sha256.
- **The origin may carry a path** (B1). `scripts/discovery.py` accepts `https://<host>` with an optional path of
  lowercase segments of a-z, 0-9 and "-", with no trailing slash, query or fragment, and derives the base path from it.
  `public_origin` stays null (B8); `site-src/deployment.json` states the rule.
- **The published site honours the base path.** `scripts/build.py --out DIR [--origin URL]` writes the site as it is
  published, without touching `site-src/deployment.json` or `dist/`. After the pages are written,
  `scripts/base_path.py` moves every root-absolute reference under the path:
  - links, images, srcset, the stylesheet and font preloads, and the root entry's refresh;
  - the stylesheet's `url()`;
  - the runtime's two fetches, its language prefix (search results, Compare, corrections) and the language switch;
  - the root redirect and its stored choice;
  - the `_headers` path patterns.
  Each runtime address is listed and must occur as often as stated, or the build stops. Canonical, hreflang, `og:url`,
  `og:image`, structured data, the sitemap and the printed canonical addresses already carry the path through the
  origin. Under a path, `robots.txt` says that crawlers read only the domain's own file.
- **`dist/` stays the review build.** Its links stay root-relative, so every gate keeps reading it at a server root.
  This was checked: a scratch run of the validator on a base-path `dist/` reported 1,870 errors. On the same build with
  root-relative links it reported only S04.1's language-alternate check, which expected root-relative `hreflang` for
  any origin. That check now uses discovery's address; its result is unchanged while the origin is null.
- **Gate (B2).** `scripts/tests/test_base_path.py` builds the decided origin into a temporary directory and serves it
  under `/financial-inclusion-evidence/`, with its own `_headers` applied by full path and a 404 page at any depth.
  - (a) It sweeps 296 files and 22,025 addresses.
  - (b) In Chromium, at 390 and 1440 px in both languages, it loads the root entry, Home, /payments/, a record, /data/,
    the three-measure Compare and a deep 404. It uses search, Compare, Copy citation, Share, print and the language
    switch, and records every request (60 page loads, 584 requests).
  - (c) It checks every discovery address.
  - Its negative control injects `href="/en/about/"` into one page: the sweep and the browser both report it.
  - It runs once, in CI's "Browser acceptance" job. Against a build left unrelocated it fails at once.
  - Noted, not failed: browsers ask the domain root for `/favicon.ico` because no page declares an icon.
- **Live runs under a path.** Three `test_public_tools.py` tests join server-relative links to the base correctly. The
  live run bypasses the page policy, which `test_security_headers.py` tests; under the strict policy, Playwright's
  evaluated waits were refused. Both suites pass against the base-path build served under the path: 35 of 36 tools,
  one not applicable, and 288 pages under the relocated headers.
- **Deploy.** `.github/workflows/deploy.yml` (still inactive) publishes `scripts/build.py --out` and sweeps it under its
  path. Its publish root holds the site under the path and `_headers` at the root.
- **Runbook (B4, B5).** `docs/RELEASE_RUNBOOK.md` "Hosting" is rewritten around the owner's three routes, with the B4
  facts confirmed by one read-only request and a DNS lookup:
  - preferred: our Pages project behind a Nitro `routeRules` proxy, which is guidance for CauseWay's frontend repository;
  - App Platform: a static-site component cannot send custom response headers, so the proxy route stands;
  - fallback: `evidence.causewaygrp.com` with a 301.
  Each route states how the headers survive, that no corporate robots header, script or cookie reaches our responses,
  and how it rolls back. It adds the web administrator's sitemap step, and the warning that HSTS is a whole-domain
  decision. `docs/DEPLOYMENT.md` and CONTRIBUTING §5 follow.

## 2026-10-03 — The validator in half the time; the negative-control job back inside its limit

CI's "Gate negative controls" job was cancelled at its 45-minute limit on `ab380cf`. It runs the full validator once per
control (66 controls). The validator had grown to 83 s locally.
- **RC-NAMES** (hardened in RC-17) ran 122 patterns over every built text and social frame: 76,000 regex searches,
  about 36 s. Each pattern now carries a literal needle, its core word, and its regex runs only on texts that contain
  it. Every match of a pattern contains its needle; for the circular's patterns this is proved on their own lineage
  labels at each run. Results are unchanged: 37 of 37 variants caught, 13 of 13 ordinary-vocabulary strings clean, 0
  hits on the site.
- **The search-smoke mirror** normalised the same texts again for each of its 102 queries. `_r4norm` and `_r4re`, both
  pure functions, are now cached, and the digit mapping is one `str.translate` with the same result.
- **Result:** 83 s to 38 s locally, still PASS. The five search controls and the seven name controls are caught. The
  job's limit is unchanged.

## 2026-10-03 — Owner note of 11:15 recorded; the B16 inputs and the session's check scripts made safe

Records only (the owner's note of 3 October 2026, about 11:15 Cairo, section 0):
- `audit/OWNER_DECISIONS_2026-10-02.md`: the note recorded verbatim, append-only. The session's reading follows it. One
  part is flagged to the owner: the single truth change in the /about/ pair (3.5) stands, with the one-cell way back.
- `audit/release_candidate/b16/`: the B16 disposition generator and its inputs.
  - The read-only extraction at `c055abc`: 126 open items.
  - The updates since then, and the items B16 adds.
  - The head and tail text.
  Until now these lived only in the session. Running `python3 audit/release_candidate/b16/make_disposition.py`
  rebuilds the disposition table.
- `audit/release_candidate/checks/`: the session's browser checks.
  - `check_menu.py` and `reach.py`: the opened mobile menu at 320 and 390 px.
  - `g0_shots.py`: the presentation pass's screenshots and first-screen text.
  - `rc_names_variants.py`: the hardened RC-NAMES matcher on 50 variant and ordinary-vocabulary strings.

## 2026-10-03 — "How numbers are presented" once; the citation in two lines; the exports carry the licence

Code, from the owner's instructions of 3 October 2026, 09:50 (C5 and E), plus one presentation fix found on the way.
- **C5.** The reading rule ("How numbers are presented" and its governed sentence) was a block under every domain
  heading. It is now printed once, on /methodology/, as its first section (#how-numbers). Each domain answer links to
  it once from its spine, under the governed "Methodology" heading. The domain head keeps its two governed actions.
- **The citation in two lines (E1; Addendum 2 lesson).** A record's short citation now previews and copies as two lines:
  - first, this resource: the title, the product, the record, CauseWay, the edition and the page address;
  - second, the original sources: publisher, title, year and link.
  The public tools test reads the clipboard and checks both lines.
- **Arabic citations (presentation).**
  - Record IDs no longer break at their hyphen; "-CLM … 001" is gone.
  - Each URL is its own left-to-right block, so a wrapped address reads in order.
- **Exports (E3).** When the switch is on, the exports carry the licence: LICENCE.txt holds the governed /rights/ licence
  section verbatim in both languages, and MANIFEST.json names CC-BY-4.0. `public_downloads` stays false; the switch
  waits on counsel's confirmation of the CC BY 4.0 text.
- **E4.** "The licence decision" is replaced in the owner's open list by "counsel confirms the CC BY 4.0 text": README,
  roadmap §2, DEPLOYMENT.md, the RC-B14 message and the frames docstring. The runbook and deployment.json follow with
  the hosting work.
- **Gates.**
  - **RC-0950:** the reading rule is printed on /methodology/ only and linked once from each domain answer; every record
    citation that names a source is two lines, with the page address ending the first.
  - **Negative controls:** two new ones.
  - **test_exports:** checks the licence.

## 2026-10-03 — Steward patch: About, the trust links and "Cite this page" in the opened mobile menu (A-12, C-6, C-8)

One patch to the controlled contract `site-src/content/content/navigation_interaction.json`, by this session as
designated programme steward for that patch only (owner decisions of 3 October 2026, 09:05 point 3 and 09:50 A.3).
- **Contract.** One key, `mobile_menu`, appended in the file's own JSON style; every earlier byte is unchanged. It names
  the decision, the scope (below 900 px), the order (the trust links as listed, About first; then the utilities' cite
  control) and the rule: existing governed labels only, and the header unchanged.
- **Renderer** (`render.py`, `content.py`, `theme.py`). The opened menu carries the trust links under the footer's
  governed group label ("Trust and responsible use"), then the cite control. Both are hidden from 900 px, where the bar
  and the footer already show them.
- **Checked in a browser:**
  - 320 and 390 px, English and Arabic, on Home and a record: 7 links, About first.
  - The cite control is reachable by scrolling, because the header is static.
  - No horizontal overflow.
  - Header heights are unchanged: 100, 68, 68 and 66 px.
- **Gate RC-NAV.** Every built page's opened menu carries the contract's trust links, About first, and the governed
  cite control, and the header's controls are unchanged. A negative control drops About from one Arabic record and is
  caught.
- **All gates pass:**
  - the validator, content parity, public tools 35/36 (one not applicable), viewport 168/168;
  - security headers, the projection check, bilingual invariance, social images.

## 2026-10-03 — Release candidate RC-17: names withheld; Addendum 2 governed improvements; who publishes this; CC BY 4.0

One Master transaction (e24fe737… → 433f38bf…, 150 cells; `audit/release_candidate/rc_17_addendum2.py`), with its
code. It covers Owner Addendum 2's improvements that were still open and the governed parts of the owner's decisions of
3 October 2026 (`audit/OWNER_DECISIONS_2026-10-02.md`): 09:05, points 1 and 2, and the consolidated note of 09:50,
recorded verbatim, which governs (A.1–A.2, C1–C4, D, E and B7). English and Arabic change together.
- **Who publishes this (09:50 D).**
  - /about/, in "CauseWay's role", carries the owner's paragraph on what CauseWay is, before the funding paragraph,
    which is byte-identical. "CauseWay" stays in Latin script in Arabic.
  - One truth change was made, and is recorded in the decisions file: records are checked "against the sources it
    names", because seventeen records have no single original source.
- **Licence (09:50 E).**
  - /rights/ opens with the licence. A new last section states it: CC BY 4.0 for the content CauseWay owns, with the
    logo excluded.
  - It does not cover third-party material, which stays under its publishers' terms; the resource hosts no copies of
    their files.
  - CauseWay asks for a two-line credit: this resource, then the original source the record names.
  - It makes no claim of rights clearance.
  - /terms/ points to it and gives the same citation rule.
  - `public_downloads` stays false.
  - The public-literal audit allows the licence version, "4.0", on those two routes only, as an identifier.
- **/payments/ headline (09:50 C2).** The title, og title and search title is now short: "Payments: reported POS
  terminals rose between March 2025 and June 2026; how many people use them is not measured". The full sentence, with
  561 → 1,651 and the reporting scope, opens the page as its lead.
- **/privacy/ (09:50 B7).** One sentence, in both languages: the resource sets no cookies. At its public address on
  causewaygrp.com, browsers may also send a cookie that the causewaygrp.com website sets for all its pages, and the
  resource does not read it. The runbook makes the proxy strip that cookie in both directions.
- **Names withheld (points 1 and 2).**
  - All twelve names of the June 2024 e-wallet circular are withheld alike.
    - NEG-EW-011 keeps its ID, route and count of 12, its date boundary, its "does not establish" text and its link to
      the circular. It now reads as one wallet service among twelve; its page description changes the same way.
    - The search empty state carries one governed sentence: names from the regulator's lists and enforcement
      decisions are not reproduced here, and the originals are linked from Data & sources.
  - No governed field now allows an enforcement-decision name:
    - every status event's `public_use`;
    - the `public_claim_rule` and note of the 30 enforcement-subject rows;
    - the provider-status passport's display requirement;
    - the status events' own text, which now names each subject by its entity ID.
  - CLM-015's method and /providers/ section 6 now say that the names are kept in internal source records and are not
    reproduced.
- **RC-NAMES, hardened.**
  - **One normaliser:** tags, entities, percent and \u escapes, NFKC, Arabic marks and letter forms, hyphens and
    no-break spaces.
  - **Matching:** each name is matched on its distinctive core, with an optional Arabic prefix, whether spaced or
    joined. Ordinary vocabulary is matched only beside its class word.
  - **Coverage:** branch rows, every text file in the built site and every social-image frame. Failures name the record
    ID, never the name.
  - **Negative controls:** four new ones (a short form, a joined spelling, an Arabic prefix, «محفظة» with a one-word
    name) on top of the earlier three.
- **Regulatory findability (improvement 1).**
  - The circular is typed as an instruction/circular, and the 2025 e-money amendment as a regulatory decision.
  - The search alias "decision" / «قرار» targets regulatory decisions.
  - /reforms/ names the amendment as Governor's Decision No. 4 of 2025.
  - VIS-PAYMENT-RAILS names the 26 June 2024 rule as Governor's Decision No. 23 of 2024, binding exchange companies,
    exchange establishments and money-transfer agents to the unified network only. Both were read in the signed scans.
  - /data/'s regulatory group is in document-date order, newest first. "Verify it yourself" on /reforms/ and
    /providers/ opens it.
- **Search (improvement 2).** New aliases for Findex / «فيندكس» and PSP / «مزوّد خدمات الدفع». Alias 007 says that
  «محفظة» means both an e-wallet and a loan portfolio. A whole-phrase ranking bonus was built, then withdrawn: it lifted
  records above the governed primary routes in the search smoke tests. It is now post-launch.
- **Compare presets (improvement 5).** /evidence/compare/ and /remittances/ offer a preset comparison, with governed
  link labels.
- **Copy, counts, currentness (improvements 9–11, a lesson).**
  - The /payments/ title is shorter and makes the same claim within the same scope.
  - The self-description counts are taken from the sheets: 165 sources and 97 payment observations, stored as numbers.
  - "resolve … resolve" on Home and Explore is gone.
  - Four 2021-wave records say that the Global Findex 2025 edition adds no newer Yemen observation.
- **Gates.** RC-ADD2 is new, with checks for date order, the regulatory link, the presets, alias 002 and the
  empty-state sentence.
- **Review.** Two rounds, each folded into the one rerun.
  - **First round:**
    - **Bilingual reviewer:** ACCEPTABLE with nine minor findings, all folded.
    - **Adversarial reviewer (entity and regulatory statements):** NOT ACCEPTABLE. Its findings were folded: the gates,
      the remaining governed fields, the related public text and the decision's scope.
  - **Second round, on the 09:50 copy:**
    - **Bilingual reviewer:** NOT ACCEPTABLE. It found that "does not host" third-party data was false, and that
      «عنوان الصفحة» reads as "page title". It also flagged the Creative Commons Arabic name, «ملفات البيانات المُصدَّرة»,
      a URL bidi glitch, the internal-records term, and a connective.
    - **Hostile reviewer:** NOT ACCEPTABLE. It found that "as each record's citation does" was false, that the logo was
      inside the grant, that /providers/ claimed every decision is recorded where it shows a selection, and that the
      owner copy's "its original source" was not true of every record. It also asked for a dated headline and for the
      cookie stripping and release check, which are in the runbook.
    - All were fixed.
  - **Escalated:** NEG-EW-011's ID is the circular's own item number, so withholding the name does not withhold the
    identity. This goes to the owner (`design/ESCALATIONS.md`, raised at RC-17).
- **Records.**
  - In `design/ESCALATIONS.md`, RC-8, B-2, C-10, B-7, the exports item and C-6 are closed by dated lines pointing to the
    decisions file.
  - The domain strip is in `docs/ROADMAP_V1_1.md` as item 27.

## 2026-10-03 — Release candidate RC-16: no undated "latest"; survey coverage stated; one base disclosed

One Master transaction (ebfb929c… → e24fe737…, 38 cells; `audit/release_candidate/rc_16_as_of.py`). It applies two
"lessons from comparable products" of Owner Addendum 2, where governed fields exist, and closes two items. English and
Arabic change together.
- **No undated "latest".** A label that calls a measure "the latest" goes stale silently the day a newer one appears.
  - Record titles and /people/ headings now name the wave: for example, "Account ownership: the representative measure
    from the Global Findex 2021 wave".
  - Page descriptions that keep the claim now say when it was checked ("As checked on 3 October 2026, …"), as CLM-017's
    already did.
  - A new gate, RC-LATEST, with a negative control, fails any title, description or h1 that says "latest" without a
    check date. A denial of a single latest year still passes.
- **Coverage.** Four 2021-wave indicator records now name the areas the survey excluded (about 23% of the population),
  in CLM-025's governed words.
- **B15 condition, VIS-MFI-SPINE.** The title no longer promises a view of gaps it does not draw.
- **Register item, VIS-FIRM-FINANCE-SEVERITY.** The World Bank diagnostic, read again at p. 145, introduces its
  tabulation "when asking for the reasons of not applying". The base may therefore be narrower than the record said.
  The record's measurement limitation now says so, and that the base is not established
  (`ORIGINAL_SOURCE_VERIFICATION.md` §9).
- **Short citation.** It gives each original source's year when the source's title does not.
- **Review.** One bilingual reviewer, NOT ACCEPTABLE at the first run:
  - "When each function was last measured" was false: saving and borrowing were measured in 2021, but have no weighted
    values yet.
  - The vintage ladder's description, without "latest", changed its claim.
  Both were corrected, with the minor findings, in one rerun.

## 2026-10-03 — B15 d: figures print governed precision and link their record by name, never to themselves

Code only (`scripts/yfie/visuals.py`, `render.py`, `theme.py`), from the product challenge (`PRODUCT_CHALLENGE.md`).
- **A-9, A-10, C-16.** A difference drawn in a figure prints at the precision of the published values it is calculated
  from, as the governed text prints it. The gender-gap chart read "9" and "11.1" where the text reads "9.0" and "11.10";
  it now reads 9.0 and 11.10, which also settles the Arabic «9 نقطة مئوية».
- **A-17, C-9.** On screen, a figure's foot links its record with the governed label "Open evidence record" /
  «افتح سجل الدليل», instead of a raw left-to-right path in Arabic text. A figure on its own record page, or a Reading's
  own figure, carries no link to itself. In print and detached frames, "Full record:" with the path is kept.
- **Gates.** RC-B15 now also fails a figure that links its own record page, with a negative control. The visual contract
  checks pass (2,850 assertions, 133 print checks, 0 failures).

## 2026-10-03 — Release candidate RC-15: the product challenge's governed copy and data, the short citation, sharing a record

One Master transaction (4282c50b… → ebfb929c…, 44 cells; `audit/release_candidate/rc_15_b15_copy.py`). It carries the
changes the B15 red team allowed, ranked in `audit/release_candidate/PRODUCT_CHALLENGE.md`, and the code that renders
their bindings. English and Arabic change together. One bilingual reviewer and one adversarial reviewer both returned
NOT ACCEPTABLE at the first run; every finding was folded into one rerun.
- **B-1, truth.** CLM-019, CLM-009, VIS-PROVIDER-TIME and the site-map description said the 2026 decisions "are matched"
  with the roster. The Master marks every subject not yet reconciled. They now say the matching with the roster would
  have to be done and has not been; each decision stays attached to the entities it names.
- **A-8, B-5.** Home lists, under its gaps section, the three priorities bound to it (MA-001, MA-003, MA-005) by their
  governed titles, with a line saying a link is not a claim to close or explain a gap. Explore shows every P0 priority
  and says so. /measurement/ lists P0 then P1, each in ID order.
- **B-6.** CLM-026 (32 measures specified; estimates not yet published) is bound to /measurement/.
- **C-1.** CLM-002 links the two World Bank series it subtracts, on its source card.
- **C-2, OWN-04.** An Evidence Record previews and copies a short citation: title, record ID, CauseWay, edition, then
  each original source as publisher, title and locator, then the record's address. The long form stays one disclosure
  away and copies on its own. A citation isolates each URL as it isolates identifiers.
- **U1, game-changer.** "Share this record" sends the title, period, population and what not to conclude, verbatim,
  with the link. It uses Web Share where the device offers it and copies the same text elsewhere; the Arabic text
  isolates its dates and identifiers.
- **Copy.**
  - B-3: CLM-007 "gives a higher value", not "shows materially higher".
  - B-10: CLM-015 says Decision No. 23 of 2024 is a separate instrument of the same date and lists it as a context source.
  - B-12: /payments/ says what the transaction series does support, and the POS chart note no longer asserts one
    reporting scope.
  - C-3: Compare's description names the rows it shows.
- **Search.** Alias 026 gains "cash assistance" / «المساعدات النقدية». A new alias 028 maps internet to connectivity.
- **Not done.** Surfacing CWR-010 on /payments/ was not done: an answer page carries at most two Readings. That is in
  the roadmap.
- **Records.** `PRODUCT_CHALLENGE.md` (new, indexed); `docs/ROADMAP_V1_1.md` §3 filled; seven escalations to the steward
  and the owner in `design/ESCALATIONS.md`.
- **Gates.** RC-B15 checks Home, Explore, the /measurement/ order, the matching wording (the withdrawn first wording is
  banned too), the short and long citations, the share control and CLM-002's series. A negative control checks that
  Home keeps its bound priorities. The browser test for a record's citation now copies the short form and the long form;
  a new test shares a record.

## 2026-10-03 — B15 d: search matches numbers whole, Arabic words from their start, and governed aliases

From the product challenge, these were ranked first by the red team (`PRODUCT_CHALLENGE.md`). All are code only, in
`site-src/app.js`, mirrored in `scripts/validate.py`, whose search smoke tests and canonical probe still pass.
- **C-5, numbers.** "6,245", "6245" and «٦٬٢٤٥» are now the same query. A decimal point stays inside a number, and a
  number matches only as a whole number. Before, "6245" found nothing, "6,245" was searched as "245", and "11.9%"
  surfaced an enforcement decision before the Findex records.
- **A-2, words.** A word matches from the start of a word, after the Arabic proclitics و ف ب ل ك and the article. A
  word of three letters or fewer matches only whole. Identifiers still match inside references (TOOL-10).
  - «تعز» no longer returns «تعزيز…».
  - «الريف» returns 1 result instead of 131.
- **A-3, aliases.** A query that is a term of a governed alias group also finds the group's other terms, ranked below
  literal hits. «المرأة» now returns 15 results, CLM-002 among them, instead of 2.
- A browser test covers all three, and public tools pass 34/35 (1 n/a).

## 2026-10-03 — B15 d, first improvements: search recovers after a failed load; two layout fixes

From the product challenge's panel findings (`audit/release_candidate/PRODUCT_CHALLENGE.md`, written once the red team
reports):
- **A-1.** If the search index or the aliases fail to load once (a dropped connection), the failure is no longer kept.
  The next search tries again. Before, search stayed broken until the page was reloaded.
- **A-15, C-16.** The search input no longer overruns its dialog's padding (`box-sizing`).
- **C-4.** At 1,200 px and wider, the Compare tool uses its section's full width. A four-record table now fits its
  region (840 px) instead of scrolling inside a 584 px column. The scrolling region stays for narrower screens.

## 2026-10-03 — Roadmap for version 1.1, first draft (B15 f)

`docs/ROADMAP_V1_1.md` puts first, as the brief asks, international context from same-source aggregates, with Yemen's
coverage caveats, and then public downloads after the licence decision. It lists the items Owner Addendum 2 sends to the
roadmap, the inputs that would complete the 17 text-first visuals, and the library and currentness items. The product
challenge's deferred findings are added after B15 d.

## 2026-10-03 — Release candidate RC-14: first screens and drawn figures re-read; one date corrected

Transaction `audit/release_candidate/rc_14_bank_list_date.py` through `run_stage.py` (Master `6568e6e6fcbb` →
`4282c50b9bbd`; 27 cells).
- **The re-read.** A reader who wrote none of this work re-read 65 first-screen and drawn numbers in their originals:
  Findex, the CBY-Aden annual reports, the H1 2025 payment report, the provider matrix, the dated events, and the
  /finance/, /reforms/ and /access/ leads.
  - 42 match. Every English and Arabic first screen prints the same numbers.
  - One date did not match: the provider matrix printed the bank list as "26 · 2026-09-07". The list carries no
    printed date and was re-read on 3 October 2026, so the universe count and the 26 bank rows now carry 2026-10-03.
    The count is unchanged. RC-8 had missed this ISO-format field.
  - 22 values (IMF tables, RPW, UNDP dates, one SFD figure) cannot be read from here today. They are recorded for a
    person with a browser at release: `ORIGINAL_SOURCE_VERIFICATION.md` §8 and the register.

## 2026-10-03 — Six reverse traces (Owner Addendum 2, before B16)

`audit/release_candidate/REVERSE_TRACES.md` traces six public objects to their locators: Home's headline claims,
VIS-FINDEX-GAPS, VIS-POS-VALUE, RV-CWR-001, the /reforms/ chain and IMF-attributed event YSC-014. Each goes from public
object to record, to source, to locator, and each locator was requested.
- Six of six are unbroken, so nothing needed fixing.
- The one locator not verifiable from here is the UNDP project page, whose CDN refuses automated requests.

## 2026-10-03 — B14 e and f: the currentness re-run as one command; the release runbook

- **Currentness re-run (B14 e).** `scripts/currentness_rerun.py` reads every watch point in its original and compares it
  with what the Master holds: CBY-Aden's POS releases, its decisions and its regulation page, the World Bank's FMIIP
  status reports, Global Findex for Yemen, and the hosts that refuse automated requests. `--append` adds the dated
  result to `audit/FINAL_CURRENTNESS_CUTOFF.md`; it was run on 3 October 2026.
  - Nothing newer: POS releases to June 2026, decisions to No. 18, the ISR of 8 April 2026, and Findex's 2022 data year.
  - IMF, Remittance Prices Worldwide and the CBY Sana'a host are "check by hand".
  - Nine CBY-Aden regulatory documents on its regulation page are not held. The /data/ group already says it is not a
    complete register. They go to B16 (register).
  - The signed-scan dates were RC-13.
- **Release runbook (B14 f).** `docs/RELEASE_RUNBOOK.md` gives fourteen steps from "the owner has a hosting account and
  a domain" to "live", each naming who does it: origin, currentness at the release date, every gate, credentials, the
  inactive deploy switch, HTTPS and HSTS, the live checks, optional cookieless counts behind the Privacy page, open items,
  the owner's acceptance and the tag.
  - Cloudflare Pages is recommended, with Netlify as the alternative and the reasons stated. Neither has been tested
    from inside Yemen, and the runbook says so.
  - `test_security_headers.py --base` and `YFIE_BASE_URL` for `test_public_tools.py` run the same checks against the
    live host.

## 2026-10-03 — Fix: the header test no longer counts a navigation's aborted requests

CI's browser job failed once on `4a90371`, in `scripts/tests/test_security_headers.py`. Six `net::ERR_ABORTED` font
requests were listed as failures of three Evidence Records. They were the previous page's font preloads, still in flight
when the next page started loading, and the test credited them to the page that followed. The next head passed, which
does not make it a flake.

The test now ignores `ERR_ABORTED` only. A request the policy blocks reports `ERR_BLOCKED_BY_CSP` and still fails the
test, and violations are caught by their own event. All 288 pages pass.

## 2026-10-03 — B14 c and d: an inactive deploy workflow; the performance budget

- **Deploy workflow (B14 c).** `.github/workflows/deploy.yml` deploys `dist/` to Cloudflare Pages. It runs only when the
  owner sets the repository variable `YFIE_DEPLOY_ENABLED` to `true`; until then every run is skipped. It refuses a
  build whose `public_origin` is null, runs CI's gates, proves `dist/` is a fresh build, then deploys with a pinned
  `wrangler`. Secrets and variables are named in the file; the host choice and the steps go to the runbook (B14 f).
- **Performance budget (B14 d).** `scripts/performance_budget.py` serves `dist/` as a host would under `dist/_headers`
  (gzip and the cache rules). It loads the twelve page families in English and Arabic, cold and warm, on Lighthouse's
  mobile profile: 150 ms RTT, 1.6 Mbit/s, CPU ×4.
  - A cold page transfers 227–304 KB in 7 requests. First paint is 0.78–2.3 s and load 1.4–2.9 s.
  - A second visit transfers 0 bytes.
  - Without compression a page would be about 370 KB; the 10 MB pages of 29 September went with the logo derivatives.
  - The largest remaining cost is the three canonical font faces of the page's script (71–87 %). They are not changed.
  - A provisional budget is recorded in `docs/SUSTAINABILITY_IMPLEMENTED_RUNTIME.json` (`release_candidate_b14d`):
    350 KB, 8 requests, LCP 2.5 s, load 3 s. Every family meets it.
  - Gate RC-PERF holds the byte part on every build, from the files themselves; its negative control is caught.
    Nothing here is an operational or carbon figure.

## 2026-10-03 — Release candidate RC-13: the signed-scan dates of the 2026 enforcement decisions (B14 e)

Transaction `audit/release_candidate/rc_13_decision_dates.py` through `run_stage.py` (Master `efb5a7c2ce38` →
`6568e6e6fcbb`; 32 cells).
- **Decisions read.** The twelve 2026 decisions whose dates came from CBY-Aden's news pages were checked against the
  signed scan each page links. Ten match.
- **Two corrected.** Decision No. 13 was signed on 5 August 2026 and Decision No. 14 on 19 August 2026, each the day
  before its news page. Both sources (titles in English and Arabic, document dates) and their status events (PSE-003,
  PSE-004) now carry the instrument's date, as Decision No. 10 has since RC-8.
- **Scans recorded.** Every decision records its scan as an additional locator, with the check date.
- **Records.** `ORIGINAL_SOURCE_VERIFICATION.md` §7 holds every reading. The register item is closed.

## 2026-10-03 — B14 a and b: data exports prepared and switched off; host headers

- **Exports (B14 a).** `scripts/exports.py` writes the Evidence Records (110), public claims (60), sources (156), visual
  rows (130), chronology (24) and Measurement Agenda (10) to `build/exports/`, never to `dist/`. Each is CSV (UTF-8 with a
  BOM) and JSON, with a bilingual codebook and provenance on every row: record ID, source IDs, public locators and the
  Master's SHA-256. A source without a public locator is never named.
  - `scripts/tests/test_exports.py` checks every value against the projections by a separate path, and proves itself on
    a planted wrong value.
  - CI attaches the files as the artefact `yfie-data-exports`; `/build/` is ignored.
  - Publishing is the switch `public_downloads` in `site-src/deployment.json`. It stays `false` until the owner's licence
    decision; `build.py` copies the exports only when it is true.
  - The codebook's wording is a draft, to be reviewed bilingually before the switch is turned on.
- **Host headers (B14 b).** `site-src/hosting/_headers` is copied unchanged to `dist/_headers`, read by Cloudflare Pages
  and Netlify. It carries the policy of `docs/DEPLOYMENT.md`: CSP with `frame-ancestors 'none'`, `nosniff`,
  Referrer-Policy, Permissions-Policy, COOP and `X-Frame-Options`. Cache rules are short for HTML and search data, an
  hour for unfingerprinted assets and thirty days for the canonical fonts. HSTS stays commented out until HTTPS is
  confirmed on the release domain. GitHub Pages cannot set headers, and the deployment page says so.
  - `scripts/tests/test_security_headers.py` serves `dist/` under those headers and loads all 288 pages in headless
    Chromium: 0 policy violations, 0 failed requests, 0 script errors. CI's browser job runs it.
- **Gate RC-B14.** `dist/_headers` matches its source, and `public_origin` and `public_downloads` stay off.

## 2026-10-03 — Release candidate RC-12: B12 text-first tables, B13 research library and link check, two reviews

Transaction `audit/release_candidate/rc_12_b12_b13.py` through `run_stage.py` (Master `36a61f8d5429` → `efb5a7c2ce38`;
65 cells). `rc_12_stage_inputs.py` binds the two tables in the contract.

- **RC-11's review (RC-11b), NOT ACCEPTABLE on one string; all applied.**
  - The /payments/ frame note no longer gives OBS-00036 a half-year period, which its caveat leaves open. It no longer
    calls consecutive months comparable without qualification either: three releases' displayed percentages contradict
    the published totals, and the note now says that each mismatch is recorded as a discrepancy within the source.
  - Arabic «الحلقة» for the chain's step column.
  - "Group or gap" and "Date or period" headings.
  - The landscape's empty-row label names what is empty.
  - A governed "Source" corner label for the source-comparison table, replacing the prefix "Source:".
- **B12.** The two text-first contracts whose rationale describes a table now render it from governed rows inside the
  text frame:
  - VIS-TARGET-RESULT-STATE shows baseline, target, and a result row saying "No observed result is held in the evidence
    base — not zero". The World Bank ISR's placeholder "0" is not bound.
  - VIS-FIRM-FINANCE-PATH shows each base as a row group ("Out of 328 formal establishments surveyed", "Out of 18 valid
    loan-source responses"), with a governed marker: it is not established that the 18 come from the 31.

  The generator gains `_vdc_text_table`: governed rows only, `must_equal` guards, governed headings and row headers, and
  only on the text-first tiers. A new gate, RC-B12, checks every row header and every number on both record pages.
  `audit/release_candidate/B12_TEXT_FIRST_DISPOSITIONS.md` disposes all 23 text-only contracts: 2 bound, 4 complete as
  designed, and 17 with the missing Master input named.
- **B13 a–c, the research library on /data/.**
  - Filters by document type, publisher, document year and the domain page that uses the source, plus an order by
    document date.
  - The state travels in the URL (`?type=&publisher=&year=&domain=&sort=&q=`), so a filtered list can be shared.
  - The controls appear only when the runtime runs, so without JavaScript the full list is unchanged.
  - Each source lists the Evidence Readings that use it, besides its records.
  - The methods and international references shelf is addressable and in the page index.

  Two filters the brief names cannot be offered. The language of a source is not a governed field. Every listed source
  already has a public original, because the publication firewall lists no other. Gate RC-B13 checks the filters, the
  keys and the archived labels; a browser test checks filtering, the shared URL and clearing.
- **B13 d, the link check** (`audit/release_candidate/LINK_CHECK.md`): all 156 public locators were requested.
  - 129 OK.
  - Five SFD newsletters had moved to the publisher's new file names; each was read and holds the values the Master
    cites, and its locator now points to the new address.
  - Four have no current address. Their locator is now the web.archive.org copy of the original address, and the site
    labels it "Open archived copy (web.archive.org)".
  - Issue 62's current file is another edition, with different table totals: a register item.
  - 14 are refused by the publisher's CDN, which is not a broken link.
  - One is unresolved, one host is down, one has a TLS failure and one needs sign-in.
- **RC-12's own review, NOT ACCEPTABLE on two strings; folded in before commit.**
  - The frame note's last sentence names the published monthly totals.
  - The 18 responses keep the governed Arabic term «استجابة».
  - Three Arabic should-fix items.
- Negative controls added for RC-B12 (one) and RC-B13 (two); each is caught.

## 2026-10-03 — B10 closed: the full-site accessibility audit record, the keyboard walk, one corner label

- **Audit record (B10 c).** `scripts/accessibility_audit.py --all` over 143 routes × English and Arabic × 1,440 and
  390 px (286 pages, 572 page-widths), axe-core 4.10.2. Results:
  - 0 axe rules violated, and 0 contrast failures.
  - 18,966 targets measured; 302 are under 24 × 24 px, of which 284 meet the inline exception and 18 the spacing
    exception, so 0 meet neither.
  - No unnamed interactive element, landmark or control; one `h1` per page; no heading jumps; no image without `alt`;
    nothing wider than the viewport.

  `docs/ACCESSIBILITY_AUDIT.md` and `.json` are an audit record and claim no conformance. Screen-reader passes and every
  human judgement stay outstanding. The JSON now keeps each page's target count and only its targets under 24 px; every
  measured target would take 3.7 MB. The summary line counts routes and pages exactly.
- **The last empty corner cell.** The year column of the source-comparison tables on the Reading "Same year, different
  number" is now headed by the governed period label (`visuals.rv001_tables`).
- **Keyboard walk (B10 c).** `scripts/tests/test_public_tools.py` gains a browser test in both languages. Search, the
  language switch, print, cite, the source filter and Compare are each reached by Tab and work from the keyboard.
  Public tools: 32/33 pass (1 not applicable to the current data).
- **Negative controls.**
  - RC-LAND's control is caught.
  - RC-B6's control was not caught: the priority card links MA-006 twice, and the control removed only the first link.
    It now removes both, and the fault is caught. The gate itself was not changed.

## 2026-10-03 — Release candidate RC-11: B10 accessibility, B11 /payments/ note, RC-10's review

Transaction `audit/release_candidate/rc_11_b10_b11.py` through `run_stage.py` (Master `ed004282e057` → `36a61f8d5429`;
30 cells). `rc_11_stage_inputs.py` binds the B11 frame note in the contract.

- **B10 a.** Each edge group in the verification spine is now named by its own heading plus the page's `h1`. It no longer
  shares the name "Continue from here" with the page's next-actions landmark. axe `landmark-unique` had flagged this on
  44 page-widths.
- **B10 b (NCC-02).** Every fallback table now names its row-header column with a governed label: period, group,
  corridor and amount, what is counted, step, dimension, date or item. axe `empty-table-header` had flagged 128 nodes on
  76 page-widths.
- **B10 c.** The axe audit runs over all 286 documents at 1440 and 390 px (`--all`), with the record in
  `docs/ACCESSIBILITY_AUDIT.md`. A new browser test walks search, language switch, print, cite, source filter and Compare
  from the keyboard in both languages. No conformance is claimed.
- **B11.** VIS-POS-TRANSACTIONS gains one frame note, written only from governed fields. It names the withheld
  first-half-2025 POS-transaction total and says why the monthly series is shown beside it.
- **RC-10b** (RC-10's review was ACCEPTABLE; all eleven should-fix items applied):
  - Arabic terms «الجنس» and «النشط».
  - Payment infrastructure states its scope.
  - Remittances received by people, not households.
  - Programmes for MSMEs.
  - Evidence types now match the linked records; CLM-015, CLM-054 and the FMIIP baseline are linked.
  - «قد» in the column heading.
  - A governed label replaces a lone "·".
  - No doubled punctuation.
  - VIS-EVIDENCE-FRESHNESS lists its member records, so its verification reads as a composite of linked records.

## 2026-10-03 — Accessibility audit over every page (B10 c, tooling)

`scripts/accessibility_audit.py` gains `--all`, which audits every route of the built site in both languages instead of
one page per route class (Part B B10 c asks for all pages). It also gains `--json`, which writes the raw axe findings
with the page and a node sample for each. No page changes.

## 2026-10-03 — Release candidate RC-10: the evidence landscape; RC-9's review; long time axes

Transaction `audit/release_candidate/rc_10_evidence_landscape.py` through `run_stage.py` (Master `26a97c34d517` →
`ed004282e057`), with `rc_10_stage_inputs.py` declaring the new 00_MASTER block in `master_structure.json`.

- **Evidence landscape** (Owner Addendum 2, improvement 3, for VIS-EVIDENCE-FRESHNESS).
  - The 34 dimensions of `audit/INDICATOR_COVERAGE_MATRIX.csv` are governed rows of a new 00_MASTER block, "EVIDENCE
    LANDSCAPE".
  - They render as a table inside the VIS-EVIDENCE-FRESHNESS frame (its record page and /evidence/), grouped by the
    eight domains, with five columns: dimension; latest evidence in this base, with its period (the linked records'
    titles and periods); evidence type; coverage; where to verify and what would change it (the domain page and the
    Measurement Agenda priority).
  - Every cell is governed text or a categorical label. There are no colour ramps, totals, roll-ups or process notes.
  - A row with nothing says "No evidence in this base".
  - Differences from the audit matrix: Education and Age are sufficient for their question (their gaps are on /people/
    since RC-1), and Income links VIS-FINDEX-GAPS.
  - Gate RC-LAND has a negative control. Links in the table meet the 24 px target.
- **RC-9's independent review (RC-9b).**
  - CWR-001 → MA-001 is removed: balance-of-payments inflows are not MA-001's domestic household receipt. CWR-001 is
    recorded as a gap in `MEASUREMENT_LINKS.md`.
  - Reading pages say what a link to a priority means.
  - Four Arabic fixes in the priorities' decision lists.
- **Roster total completed.** The provider matrix's limit label and INS-016 said 429; they now say 442, the roster
  total since RC-8b. `design/reference/check_visuals.py` found it (values_printed).
- **Long time axes.** Since RC-8 the POS panels have sixteen months, and their month and value labels collided at
  every width in both languages (`check_visuals.py`, labels_clear; that check is not in CI). A series longer than
  twelve periods now:
  - labels alternate months only;
  - prints value labels for its landmarks only: first, last, flagged months and the series high;
  - lets the table name every value.

  The label placer also allows for the wider digits of the Arabic font.

## 2026-10-03 — Release candidate RC-9: Part B item B6, measurement linkage

Transaction `audit/release_candidate/rc_9_b6_measurement.py` through `run_stage.py` (Master `d52dfc53cef8` → `26a97c34d517`;
8 cells). Every link is justified in `audit/release_candidate/MEASUREMENT_LINKS.md` (new; INDEX row), quoting both sides
in both languages.

- Five Reading → priority bindings added (CWR-001 → MA-001; CWR-003 → MA-002; CWR-006 → MA-005; CWR-007 → MA-007;
  CWR-009 → MA-006), and the seven existing ones kept. CWR-002 stays unlinked: no priority covers reconciling a restated
  official series, and the gap is recorded rather than filled.
- Each Reading page now shows its priorities under "Related measurement priorities" (`scripts/yfie/content.py`,
  `render.py`). Every priority, MA-009 included, is reachable from a Reading or from a domain page.
- /measurement/ shows each priority's governed `decisions_unlocked` (as a list) and `blocked_evidence`, under two new
  labels (`UI-MA-DECISIONS`, `UI-MA-BLOCKED`). MA-010's Arabic now spells «تاليًا».
- Gate RC-B6 in `scripts/validate.py` checks that every binding is linked on its Reading page in both languages, and that
  each priority's decision list has the same number of items in both languages. It has a negative control.
- P1-G06 (no repeated sentence on a flagship page) now treats the "This gap is examined in" link list like the other link
  lists it already sets aside, because one Reading can now serve two priorities. Nothing else in the gate changes.
- The Findex 2025 non-coverage and the Findex exclusions (about 23% of the population) were checked for this item: both
  are already stated (MATCH).

## 2026-10-03 — Release candidate RC-8b: the independent reviews of RC-8, in one rerun

Transaction `audit/release_candidate/rc_8b_review_fixes.py` through `run_stage.py` (Master `8385ede6ebd9` → `d52dfc53cef8`;
86 cells), with `rc_8b_stage_inputs.py` installing the contract change. Findings and the originals re-read are in
`audit/release_candidate/ORIGINAL_SOURCE_VERIFICATION.md` §5.

- **POS value unit (blocking).** RC-8 said the series is read in YER million "because only that reading reconciles with the
  printed changes". That reason was false, because a percentage change cannot tell millions from billions. The releases
  write the decimal mark as a comma. From January 2026 they give the value in billions: "1,262" billion is 1.262 billion,
  i.e. YER 1,262 million. The disclosure now says so in both languages, in the summaries, chart note, passport and
  observation caveats.
- **Exchange and remittance roster (blocking).** CBY-Aden replaced the roster file. The one linked on 3 October 2026
  (created 22 September 2026) lists 100 companies, 231 establishments and 111 remittance agents (442 rows), where the
  19 August file listed 98, 225 and 106 (429). Counts, copy, contract pins, the validator's /providers/ signature and the
  locator follow the new file. CLM-009 says the file has been replaced during 2026.
- **CLM-019 (blocking).** The method no longer says names come "from the signed decisions"; only Decisions 10 and 18 have
  scans.
- **Should-fix.**
  - "Payments page" is used consistently.
  - The reporting-scope boundary appears where 1,651 is printed.
  - The site's "Data & sources" page is named correctly.
  - The evidence base holds "no law as a source document".
  - The English uses "do not yield".
  - The February percentage differences are "under 0.1 point, recorded, not flagged".
  - The bank list has "no printed date".
  - The value rows' `source_value_as_reported` carries «مليار».
- **New open item.** The other 2026 decision dates are news-page dates; their signed scans are to be read at B14e
  (`FINAL_OPEN_ITEMS_REGISTER.md`).

## 2026-10-03 — Gate RC-NAMES: no enforcement-decision entity name is published

`scripts/validate.py` gains gate RC-NAMES (owner note of 3 October 2026, point 1). It reads every provider row known only
from a CBY-Aden status event (`PRV-*-E*`, 31 rows, English and Arabic) and fails if any core name appears in a built page,
data file or script under `dist/`. It passes on the current build: no name appears in any of 295 files. Negative control
"an enforcement-decision entity name is published" added to `scripts/tests/test_gate_negative_controls.py`. The bilingual
review of RC-8 suggested this gate; no Master or page change.

## 2026-10-03 — Release candidate RC-8: truth and currentness (A1, A2, POS to June 2026, Decisions 10 and 18, locators, edition)

One merged transaction, as the owner's note of 3 October 2026 allows: `audit/release_candidate/rc_8_truth_currentness.py`
(with `rc_8_pos_copy.py` for the POS copy) through `run_stage.py` (Master `5c0688d3d29d` → `8385ede6ebd9`; ledger and run
report in `audit/release_candidate/runs/`), with `rc_8_stage_inputs.py` installing the contract change. Every original is
recorded in `audit/release_candidate/ORIGINAL_SOURCE_VERIFICATION.md` §4.

- **POS series to June 2026.** The February–June 2026 releases of CBY-Aden are listed on its Arabic payments page only;
  the 26 September check had read the English page, which still ends at January 2026. Fifteen observations
  (OBS-00083..00097), five source records, and every surface that named the January endpoint: Home, /access/,
  /payments/, CLM-003, CLM-017, the three POS panels, the Readings and the chain figure RV-CWR-009 (contract and
  `scripts/yfie/visuals.py` move to the June rows; `scripts/validate.py` pins 1,651). The May release contradicts itself
  (+2.4% terminals, +9.9% transactions against totals that do not give them): per the owner, the totals and the
  displayed percentages are printed, no change is derived for that month, and the chart marks May like January. The
  YER value tile is labelled «مليار» from January 2026; the series stays in YER million, disclosed.
- **A1** (Owner Addendum 2): the text alternative and record answer of VIS-PAYMENT-RAILS no longer name two steps the
  drawing lacks; new gate RC-A1 in `scripts/validate.py` with a negative control.
- **A2**: the search alias for "law" / «قانون» carries a boundary note; the /data/ regulatory scope line names the
  issuer and says that the evidence base holds no laws.
- **Decision No. 10** (EXT-02 closed): dated 8 June 2026 on the signed instrument; PSE-012 and the source record follow.
- **Decision No. 18** (EXT-03 closed): the four entity names are non-public lineage only, printed nowhere; PSE-015 prints
  as the other decisions; CLM-019 states the rule; the class label reads "Exchange company, establishments and
  remittance agent". The five other status events whose governed `public_use` still allows a subject are escalated
  (`design/ESCALATIONS.md`); nothing prints a name.
- **Locators and edition.** The licensed-bank list moves to the newer Arabic file (July 2026; 26 banks, names
  unchanged), checked 3 October 2026; the POS publication-page record lists the Arabic POS page; the January re-issue
  is listed. The edition moves to 3 October 2026 (`audit/FINAL_CURRENTNESS_CUTOFF.md`, appended); all 286 social images
  are regenerated because each carries the edition label. README counts follow (165 source records, 440 search records).

## 2026-10-03 — Release candidate RC-7: Part A items 3 and 6 on Path A (originals read)

Transaction `audit/release_candidate/rc_7_path_a.py` through `run_stage.py` (Master `97f37eccc1a9` → `5c0688d3d29d`;
180 cells; ledger and run report in `audit/release_candidate/runs/`), with `rc_7_stage_inputs.py` installing the VIS-FIRM-CONSTRAINTS contract change. Every
check is recorded in `audit/release_candidate/ORIGINAL_SOURCE_VERIFICATION.md`.

- **Item 3, IMF Country Report No. 26/80** (read in full from the IMF eLibrary). YSC-008 confirmed. YSC-014's values
  are confirmed against the staff report's text and now attributed to it as the banking sector's ratios, ending at
  2.5; a note says the report's FSI table gives other values and that neither states a unit or the ratios' coverage.
  YSC-015 takes the report's wording; YSC-017 reads US$350 million (not "about"), with a note that the report's debt
  sustainability analysis dates the same amount to June 2025. The four "not yet checked" notes are removed; EXT-01 is
  closed in the register.
- **Item 6, World Bank, Yemen Financial Sector Diagnostics (2024), Table 8.** All sixteen values match; rows 9–16 are
  drawn with eight new labels in the source's item wording, and the partial-list note is gone. The survey is named as
  the source names it, "the 2022 Yemen Enterprise Survey" ("custom" is not the source's word), in both languages.
  The method cites Table 8, discloses that Figure 108 and the source's other tabulations (Figure 83; p. 145) differ,
  and names the formal-firm sample; the boundary against the "biggest obstacle" indicator rests on the indicator and is
  stated on CLM-005 too. The report's Arabic title is written one way.
- Independent reviews before commit: one reviewer (ACCEPTABLE, ten should-fix) and a three-lens workflow with
  adversarial checks (English and Arabic lenses NOT ACCEPTABLE before fixes); every blocking and should-fix finding
  applied (ledger `independent_review`).
- `audit/OWNER_DECISIONS_2026-10-02.md` gains the owner's note of 3 October 2026, 03:10 (Decision 18 names withheld;
  POS update conditions; review depth and order by release value), verbatim, append only.

## 2026-10-03 — Release candidate RC-6: Part B item B4, Arabic credit lines

Transaction `audit/release_candidate/rc_6_arabic_credits.py` through `run_stage.py` (Master `2b609e1928f8` → `97f37eccc1a9`;
9 cells; ledger and run report in `audit/release_candidate/runs/`), with `rc_6_stage_inputs.py` installing the new `34_EVIDENCE_PASSPORTS` column
`publisher_ar` in `scripts/projection/master_structure.json`. Every drawn figure's credit line now prints in the page's
language: the Arabic edition gives the institutions' Arabic names, taken from the forms the Master already uses, with
a product name that Arabic writes in English (Global Findex, Remittance Prices Worldwide) in parentheses. The generator
(`scripts/projection/derived.py`) credits each institution once. A bare institution name folds into one of its
products only when its source's governed title names that product; otherwise the bare name is printed once. The Arabic
detached caption credits in Arabic too. Independent bilingual review: NOT ACCEPTABLE as first staged (blocking: the
World Bank's FMIIP record was credited to the Global Findex on RV-CWR-004), every finding applied and re-reviewed
ACCEPTABLE. The survey behind VIS-FIRM-CONSTRAINTS is credited as its source names it, "World Bank 2022 Yemen
Enterprise Survey" (read in the original); `design/reference/check_visuals.py` checks each credit in its own language
and direction.

## 2026-10-02 — Release candidate: Arabic dates isolated, systemically (owner request after RC-5)

The Arabic reviewer's blocking finding in RC-5 (ISO dates displayed reversed) treated as a class. Every Arabic page was
swept (`audit/release_candidate/ARABIC_DATE_ISOLATION_SWEEP.md`): 114 digit-hyphen-digit runs on 44 pages were printed
without left-to-right isolation (26 in prose, 42 in citations, 8 in tables, 2 in titles, 36 in meta content), and the
runtime wrote 16 such text nodes into search results and Compare. All are fixed; no governed word changed.

- `scripts/yfie/text.py`: `NUM_RANGE` isolates a range at the end of a sentence and a range of thousands, and neither it
  nor `ISO_DATE` starts inside an identifier; a new `ID_RUN` isolates identifiers (citations use it in place of a
  prefix list); in a right-to-left document the title and the displayed meta content take the Unicode isolates.
- `site-src/app.js`: `iso()` uses the renderer's revised `LTR_RUN` and isolates identifiers with the same `ID_RUN`.
- B2c: no ISO date is left in Arabic running prose; ISO stays, isolated, in tables, data cells, citations and the
  governed period lines.
- Gate `RC-DATES` in `scripts/validate.py`, a browser test for the runtime, and three negative controls (each caught).
  Ten social images regenerated (their frame text holds such a run); 276 unchanged.

## 2026-10-02 — Release candidate: Owner Addendum 2 saved

`audit/release_candidate/INSTRUCTIONS_ADDENDUM_2026-10-02.md` (with its `audit/INDEX.md` row) holds the owner's second
addendum to the release-candidate brief, verbatim from its BEGIN to its END marker. It adds release defects A1
(VIS-PAYMENT-RAILS: the text alternative names a step its drawing and table lack) and A2 (search for "law" / «قانون»
needs a boundary note; the B5 scope line names what is not held), improvements 1–11 inside B15d, and items for B12,
B13d, B14e and B16. Nothing is applied in this commit; the pull request's checklist carries the items under "Addendum 2".

## 2026-10-02 — Release candidate RC-5: Part B editorial passes B2 (Arabic) and B3 (English)

Transaction `audit/release_candidate/rc_5_editorial.py` through `run_stage.py` (Master `0fb6c16de6db` → `2b609e1928f8`;
454 cells; ledger and run report in `audit/release_candidate/runs/`), with `rc_5_stage_inputs.py` installing the Arabic
period mappings of the provider matrix in the visual design contract. Every change is listed with FROM, TO and reason in
`audit/release_candidate/ARABIC_EDITORIAL_LEDGER.md` (B2: 122 applied) and `ENGLISH_EDITORIAL_LEDGER.md` (B3: 150 applied,
135 with their Arabic pair); no number, unit, period, universe or limit changed. Independent review before commit, Arabic
and English: both NOT ACCEPTABLE before fixes (Arabic: 1 blocking, ISO period cells displayed reversed on `/ar/providers/`;
English: 1 blocking, governorates called districts), every blocking and should-fix finding applied; English finding 15
(a gloss for "P0") is deferred to B15.

- **B2 a–e:** the Arabic observations recorded in `design/ESCALATIONS.md`; one Arabic term per concept; ISO dates in
  Arabic prose; one form of the Findex fieldwork window; further defects on the main pages.
- **B2 f (A3 escalation):** accessible summaries that restated their figure's boundary drop the restating sentence.
- **B2 g, h:** the provider matrix prints Arabic periods and states (new `22_PROVIDERS_DATA` columns
  `reference_state_ar`, `reference_period_ar`) and a governed context lead-in (UI-VIS-MATRIX-CONTEXT, "Context:" / «السياق:»).
- **B3:** the English pass — plain register, consistent terms, and meta descriptions written as sentences of 155
  characters or fewer.
- Renderer: the matrix's Arabic dates (`date_ar`) and context lead-in; the citation preview wraps long isolated identifiers at 320 px.
  13 social images regenerated (their frame text changed); the rest stay byte-identical.

## 2026-10-02 — Release candidate RC-4: Part B items B5, B7, B8, B9

Transaction `audit/release_candidate/rc_4_partb_strings.py` through `run_stage.py` (Master `3c6c66beddedb` → `0fb6c16de6db`;
ledger and run report in `audit/release_candidate/runs/`). Every string is the brief's wording, English and Arabic; one
governed citation line (UI-CITE-PAGE-LINE) re-uses the record line's words. Independent review: NOT ACCEPTABLE before fixes
(1 blocking, 4 should-fix), all applied before commit (ledger `independent_review`).

- **B5 /data/:** "Rules, decisions and official lists" groups the 23 sources whose governed type is an enforcement decision,
  circular or instruction, regulatory decision, regulation, or official list (the one curated card linked, not duplicated),
  with its scope line; sources with no governed type show "Document type not recorded" (EAD-07).
- **B7 Compare:** the "selected set" sentence in the intro and under the "record not available for comparison" error.
- **B8 /data/:** the reuse terms stated once above the source list; the older directory paragraph drops its closing
  reuse clause (each card keeps its label).
- **B9 every page:** a visible citation preview (the record's governed citation, or the page title and UI-CITE-PAGE-LINE,
  with the canonical address), "Copy citation" copying exactly that text, and "Print this page". In Arabic the record and
  source identifiers and the publisher's name are isolated left-to-right (the review's blocking finding); no "?." after a
  question title; the Compare intro keeps its paragraphs.
- Validator RC-GB, two negative controls and a browser test hold all four.

## 2026-10-02 — Release candidate Part B, B1: method text on the 13 table-only records

`scripts/yfie/content.py` no longer suppresses the governed method text of the 13 `NO_GOVERNED_CONTRACT__TABLE_ONLY`
records (owner decision A4 / C6 revised): each record page, and each frame that prints its record's method, shows it in
both languages. All 13 were read in full and are reader-facing method statements; none was withheld. Validator PB-0401,
which forbade the text as a "draft encoding note", now requires it like every other record's method (negative control
added). Register EAD-12 carries a dated line; table rows for the 13 stay post-launch.

## 2026-10-02 — Release candidate Part B, B0: the owner's Part B decisions recorded

`audit/OWNER_DECISIONS_2026-10-02.md` gains the dated section "Addendum — 2 October 2026 (Part B)" (append only): A4 / C6
revised (the 13 table-only records' method text is rendered), the human accessibility audit replaced by the extended
automated audit (no conformance claimed), the Part B steward and editor designation, the static architecture, the Arabic
default at the neutral root, the unchanged product name, and the owner rules on numbers, pages and closed decisions,
verbatim.

## 2026-10-02 — Release candidate G5: records reconciliation

`audit/RECORDS_RECONCILIATION_2026-10-02.md` (with its `audit/INDEX.md` row): one row per item of the brief's G5 list —
`implementation_target.ui` names the Python renderer (C9); the context's sustainability pointer names the implemented-runtime
measurement (C9); DEBT-008 reclassified as not blocking release (C8, A8); checkpoint §4 no longer names Design as next;
EAD-07's label request raised; historical ledgers left as they are, register §8 governing; the master logo's byte count
corrected in `docs/SUSTAINABILITY_METHOD.md`; `site-src/deployment.json` state `PRE_RELEASE_PRODUCTION_RUNTIME`
(`public_origin` still null); README's IBM Plex lines checked against the shipped fonts (no change); README status for
after this pull request. The four files inside the runner's snapshot went through `run_stage.py --install`
(`audit/release_candidate/g5_stage_records.py`). C1–C5 confirmed still holding.

**Erratum to the entry of 29 September 2026 (EAD-01, "Every gate keeps its assertion …").** That entry says it "corrects the
planning appendix of 29 September". No such appendix is in the repository: it was the implementing session's working plan
and was never committed. The statement being corrected — that Explore's clusters "already come governed, through the
handoff inventory's `question_groups`" — is described in the EAD-11 escalation in `design/ESCALATIONS.md`. The entry
itself is left as written.

## 2026-10-02 — Release candidate G4 (part 2): EAD-03 — the logo's web-size derivatives

Owner decision EAD-03 (`audit/OWNER_DECISIONS_2026-10-02.md`). `scripts/logo_derivatives.py` writes eight pure Lanczos
resamples of the unchanged master to `site-src/assets/logo/` (32, 40, 48, 64, 72, 80, 96, 144 px; 36,699 bytes in all) and its
`--check` compares each one's pixels with a fresh resample (new CI step; CONTRIBUTING.md §5; Pillow 11.3.0 pinned in
`requirements.txt`). `render.logo()` serves them with `srcset`/`sizes` on the product bar, the institutional band and the
404 head; the export identity line uses 32/64; the social-image template keeps the master, so the 286 images are unchanged.
Validator RC-G4 fails a page that loads the master or names a missing derivative (negative control added). Cold page weight,
EAD-10 method: 10.31–10.71 MB before, 0.30–0.69 MB after (`audit/release_candidate/page_weight/PAGE_WEIGHT_EAD-03.md`).
DEBT-016 closed; `design/08_ASSET_MAP.md` §1 and the register carry dated lines.

## 2026-10-02 — Release candidate G4 (part 1): search, A3, A5, shipped features, Arabic counts

Code only; no Master or contract change. Every behaviour has a validator check (RC-G4, P2-G02) with a negative control, and
the browser suite covers the tools.

- **Search** (item 1, A6 / C7; EAD-06): when the dialog caps its ten hits, the status gives the true total
  (UI-JS-SEARCH-RESULTS-OF, "Showing 10 of {m} results") and a link carries the query to the Evidence directory filtered to
  evidence records (`/evidence/?q=…&type=evidence`); the directory shows every match. A result-type filter
  (UI-JS-SEARCH-TYPE-FACET / -ALL, the governed type labels) narrows both searches; on the directory it is URL-addressable.
- **A3 / C3, the double boundary** (item 4): on the page a figure's text alternative — and the Compare standfirst — is the
  governed accessible summary; the boundary prints once, in the foot. Export frames keep the full alt text (`_detached`).
  `check_visuals.py` boundary_once_in_foot and `check_site.py` boundary_once_per_frame now count the visible text
  alternative too; they report eight frames whose governed summary restates its boundary (escalated for the Part B
  editorial pass in `design/ESCALATIONS.md`).
- **A5 / C4, the retired frame** (item 5): the RETIRE_FROM_DESIGN tier is excluded from the domain depth frames;
  `/reforms/` no longer shows VIS-CAPITAL-CONTEXT and keeps its record link; `never_drawn` rejects a text frame;
  `design/06_VISUAL_TABLE_SYSTEM.md` §1 records the removal.
- **Shipped features** (item 6): every link that opens a new tab carries UI-EXTERNAL-NEW-TAB (visually hidden, or at the end
  of its aria-label); fallback tables whose rows carry different units head the value column with
  UI-VIS-VALUE-UNIT-PER-ROW (VIS-FINDEX-GAPS); the Compare prompt ("Select at least two records.") stands beside the
  controls and shows only while fewer than two records are selected; the Compare status is in label-value form (RC-3).
- **Arabic counts in visuals** (item 7): a count printed with its unit noun reads «العدد: 561», «شركات الصرافة: 98».
- Item 3 (every remaining code FAIL / CONDITION of `audit/PR8_INDEPENDENT_ACCEPTANCE.md`) is A3, A5 and A6, all above.

## 2026-10-02 — Release candidate G3: EAD-11 — the question sets move into the presentation contract

Steward patch by owner decision (`audit/OWNER_DECISIONS_2026-10-02.md`, EAD-11), installed through `run_stage.py`
(`audit/release_candidate/g3_stage_presentation.py`; Master unchanged). The two entries recorded under EAD-11 in
`design/ESCALATIONS.md` — Home's four starting questions and Explore's four groups — sit, values unchanged, under
`question_sets` in `site-src/content/presentation_priority.json`. The generator rejects an unknown question or heading and a
missing or repeated question (`derived.presentation_contract`; unit test `test_question_sets_guards`); the renderer
(`scripts/yfie/content.py`) and the handoff inventory read the sets there, and `scripts/yfie/question_sets.py` is deleted.
Home and Explore are byte-identical before and after in both languages, as is the handoff inventory (hashes in
`audit/release_candidate/runs/G3-EAD-11_RUN_REPORT.json`). EAD-11 closed in the register and in `design/ESCALATIONS.md`.

## 2026-10-02 — Release candidate RC-3: governed interface strings (items 11, 12, 18, 19, 20)

Transaction `audit/release_candidate/rc_3_interface_strings.py` through `run_stage.py` (Master `ecc228beec41` → `3c6c66beddedb`;
ledger and run report in `audit/release_candidate/runs/`). Every label is the brief's own wording, English and Arabic together.

- **New strings** (04): UI-JS-SEARCH-RESULTS-OF (item 11); the five provider-matrix headings and UI-VIS-CAT-PRV-CLASS-PSO
  (item 18); UI-JS-SEARCH-TYPE-FACET, UI-JS-SEARCH-TYPE-ALL, UI-JS-SEARCH-SEE-ALL-EVIDENCE, UI-EXTERNAL-NEW-TAB and
  UI-VIS-VALUE-UNIT-PER-ROW (item 19). Their runtime and renderer use ships in G4.
- **Changed strings**: UI-JS-COMPARE-SELECTED in label-value form, "Records selected: {n}" / «السجلات المختارة: {n}», with the
  Compare status line in `site-src/app.js` filling it (item 19); UI-VIS-UNIT-PP Arabic «نقطة مئوية» (item 20); four source
  records' resource category "Measurement methods and international references" / «مناهج القياس ومراجع دولية» (item 12).
- **Provider observability matrix** (VIS-PROVIDER-OBSERVABILITY, /providers/ and its record): drawn now that its six labels
  are governed (DL-D7-001). The payment-system-operators row prints UNKNOWN in every dimension, the three institution
  events following as context in the status cell and its fallback table (the contract's `known_gap`; `scripts/yfie/visuals.py`).
- **Independent review**: ACCEPTABLE. Two findings need governed content and are escalated in `design/ESCALATIONS.md`: Arabic
  text for four English-only period values the Arabic matrix now shows, and a lead-in marking the operators' context events.

## 2026-10-02 — Release candidate RC-2: trust copy (items 9, 10, 13, 14, 15)

Transaction `audit/release_candidate/rc_2_trust_copy.py` through `run_stage.py` (Master `ebf03d6fe4cf` → `ecc228beec41`;
ledger and run report in `audit/release_candidate/runs/`), with `rc_2_stage_inputs.py` staging the public inventory contract,
the projection manifest and `README.md` (`--install`). Independent bilingual review: ACCEPTABLE; its two should-fix findings
applied before commit (below), two owner-wording notes recorded in the ledger.

- **/about/** §6: the owner-approved funding paragraph, verbatim, after "CauseWay’s role" (item 9; OWN-01).
- **/corrections/** "How history works": the edition statement, cut-off 26 September 2026 (item 10; UI-CONTENT-VERSION unchanged).
- **YSC-012** cites the two 26 June 2024 CBY-Aden instruments; the public count *chronology_events* follows its definition
  ("Dated events") through the new generator rule `count_where_not_in` — 23, YSC-020 (the analytical rule) excluded — with the
  same rule in the validator's recount, `scripts/rebind_authority.py` and the generator unit test (item 13).
- **Sheets 00 and 37**: count statements set to the derived values; the seven COUNTA formula cells keep their formulas and only
  their cached results change (`rc_lib.set_formula_cache`), so the 37 READY/REVIEW checks still compare a live count (item 14).
- **Publisher name**: no Arabic transliteration of CauseWay in any Master cell (item 15; no write).

## 2026-10-02 — Release candidate RC-1: Master truth fixes (items 1–8, 16, 17)

Transaction `audit/release_candidate/rc_1_truth_fixes.py` through `run_stage.py` (Master `17db032b15da` → `ebf03d6fe4cf`;
ledger and run report in `audit/release_candidate/runs/`), with `rc_1_stage_inputs.py` staging the visual design contract and
`master_structure.json` (`--install`). English and Arabic together; an independent bilingual review (1 blocking, 6 should-fix,
8 optional) was applied before commit, its deferrals recorded in the ledger.

- **/people/** §3–4 extend to the education and age gaps that VIS-FINDEX-GAPS draws (item 1); the VIS-SOURCE-COMPARISON
  summaries take the brief's wording (item 2).
- **Methodology and EXT-01, Path B** (item 3): no source host is reachable from this session; the lead sentence is replaced and
  YSC-008/014/015/017 print a verification note (new 14 columns `verification_note_en/_ar`). EXT-01 stays open.
- **Units** (items 4, 17): VIS-POS-VALUE displays whole YER million; remittance prose in USD million; YSC-004, the CBY-Aden rate
  and the SFD savers count in one notation. Sweep and dispositions: `audit/release_candidate/FOUR_DIGIT_UNIT_CHECK.md`.
- **CBY-Aden scope** on the RV-CWR-004 lane and RV-CWR-009 rows (item 5); **VIS-FIRM-CONSTRAINTS** partial-list note, Path B
  (item 6); the disagreement legend, CLM-003 and the POS summaries describe only what is drawn (item 7).
- **Firewall adjudications** (item 8): RV-CWR-009 OPERATION KEEP; VIS-REMITTANCE-COST rpw MEASURED → REPORTED; RV-CWR-001
  IMF staff path KEEP.
- **use_rule pointers** to `scripts/yfie/content.py` (item 16; PR #8 acceptance A7 item 8 / C9).
- **Code**: the renderer prints the chronology verification note and the POS scope; `firm_constraints` prints frame labels.
- **Gates**: `scripts/tests/test_content_parity.py` is the standing content gate (CI step, two negative controls); the cutover
  parity test exits 2 ("pinned") once the Master moves past its oracle. Validator S05.1 signature updated for the Reading's new
  unit. Methodology social images regenerated.
- **Register**: dated EXT-01 and VIS-FIRM-CONSTRAINTS lines in `FINAL_OPEN_ITEMS_REGISTER.md` §3.

## 2026-10-02 — Release candidate G1: the owner's decisions recorded under the register rows they affect

`FINAL_OPEN_ITEMS_REGISTER.md` (append only, per its §9 rule): one dated "owner decision, see `audit/OWNER_DECISIONS_2026-10-02.md`"
line under OWN-01, OWN-02, OWN-03, OWN-04 and OWN-05 (§5), under EAD-11 and for D7 (§1; EAD-03 already had its line from the
before-merge commit), and the new item **EAD-12** for A4 / C6 — the 13 `NO_GOVERNED_CONTRACT__TABLE_ONLY` records; post-launch;
no change in this edition. No Master, projection, `dist/` or controlled-contract byte changes.

## 2026-10-02 — Release candidate: start (G0)

Branch `code/release-candidate-fixes` from `main` at `38a9a97` (pull request #8 merged; its before-merge conditions met). Baseline
green: checksums current, `WEBSITE REPOSITORY VALIDATION PASS`; Production Master SHA-256 `17db032b…8690b`, Page Specs
`d4574804…b69aa`, both as found. This commit saves the owner's brief verbatim as `audit/release_candidate/INSTRUCTIONS.md`
(indexed in `audit/INDEX.md`; the folder is classed `CURRENT_PROGRAMME_RECORD`) and changes nothing else. The pull request
description carries the checklist of every Part A and Part B item and the progress log.

Not declared: PUBLIC RELEASE READY. Not claimed: WCAG conformance.

## 2026-10-02 — Pull request #8: the before-merge conditions C1–C5 met, in records only

`audit/PR8_INDEPENDENT_ACCEPTANCE.md` returned MERGE AFTER CONDITIONS on the production runtime (head `74d79a1`). This commit
meets its five before-merge conditions and makes the one-line record fixes it listed. No code, test, gate, generator,
Master byte, projection, `dist/` file or controlled contract changes: `git diff 74d79a1..HEAD -- site-src scripts dist
design/reference authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx` is empty.

- **Owner decisions recorded.** `audit/OWNER_DECISIONS_2026-10-02.md` (indexed in `audit/INDEX.md`): OWN-01 (the funding and
  relationships paragraph, EN and AR), the publisher name, OWN-04 (licence deferred; link-and-citation launch), OWN-03,
  **D7 — the owner's final visual acceptance of the Design package**, the social images, OWN-05, OWN-02, EAD-03 (export
  approved, master file unchanged), relationships, the steward delegation for the EAD-11 patch, and the dispositions of
  A3 / C3, A5 / C4 and A4 / C6. Recorded, not applied: the Master-first and runtime changes belong to the release-candidate
  pull request.
- **C2 — the premise settled.** `design/00_DESIGN_README.md` and `design/10_ACCEPTANCE_CHECKLIST.md` record the owner's
  acceptance of 2 October 2026 and keep the 28 September "withheld" status as dated history; `design/COVERAGE.csv` writes
  `ACCEPTED` on its 1,415 `VERIFIED` rows (18 `DESIGNED` unchanged). Code no longer "waits": `README.md`,
  `handoff/CLAUDE_CODE_MASTER_PROMPT.md` (its first line keeps the literal gate R86-G01 reads, as dated history),
  `handoff/README_FIRST.md`, `authority/YFI_CURRENT_PROJECT_CONTEXT.json` `design_prompt_status` (programme state, edited
  directly — `scripts/rebind_authority.py` owns only its hashes and counts) and `OPENAI_REENTRY_CHECKPOINT.md`. `fca7bf1` is
  named as what it is — the last commit of pull request #7, landed on `main`, not a merge commit.
- **C1 — the pull request's records say one thing.** `README.md` rows Next, Claude Code and Working gate carry the EAD
  states as `FINAL_OPEN_ITEMS_REGISTER.md` §1 has them; `design/09_CODE_HANDOFF.md`: the "Not claimed" row states EAD-02's
  true split (automated audit done, two failures fixed, no conformance claimed; the human audit open, release-time), the
  duplicate EAD-11 row is removed, and the test-hooks row reads the measured 27/28 with `scripts/tests/test_public_tools.py`
  modified (two tests added at EAD-06); the register carries a dated correction to its EAD-01 cell.
- **C3 — the double boundary, as a general finding.** `design/ESCALATIONS.md`: every frame prints its boundary twice because
  `scripts/projection/derived.py:1324` ends all 36 contracts' `alt_text` with the prohibited inference while the frame foot
  prints it again; owner the steward; the two per-contract escalations (VIS-INCLUSION-TRANSMISSION, VIS-SOURCE-COMPARISON)
  are marked as narrower statements of the same cause; the register carries a pointer; the decision is the owner's A3 / C3 row.
- **C4 — the `/reforms/` text frame.** `design/06_VISUAL_TABLE_SYSTEM.md` §1 no longer claims the baseline had such a frame
  (it did not): this build shows it, and the owner decided to exclude the RETIRE tier from the domain depth frames (A5 / C4);
  the same note sits on the D7 checklist's "RETIRE never drawn" line.
- **C5 — the register's append rule restored.** A dated erratum in `FINAL_OPEN_ITEMS_REGISTER.md` §9 records the in-place
  rewrite of the eleven "Where it shows today" cells and the class-count cell on 29 September 2026, each previous text
  verbatim with the commit that replaced it; the current cells stand.
- **One-line record fixes** from the acceptance: `README.md` ("The rest are open"; DEBT-008 does not block release and waits
  on the steward and Design, not the owner — A8; the quick start no longer calls `dist/` "the governed baseline");
  `CONTRIBUTING.md` §2 and §4 (`site-src/styles.css` no longer exists); the register's EAD-11 item names
  `scripts/yfie/question_sets.py`; `handoff/CLAUDE_DESIGN_MASTER_PROMPT.md` and `handoff/ENGINEERING_HANDOFF_EXPECTATIONS.md`
  point to `date_words` in `scripts/yfie/content.py`. `interface_copy.json` and `handoff/IMPLEMENTATION_MANIFEST.json` are
  governed and untouched (fixed in the release-candidate pull request).

Not declared: PUBLIC RELEASE READY. Not claimed: WCAG conformance.

## 2026-09-29 — EAD-02: the implemented site audited; two real failures found and fixed

`scripts/accessibility_audit.py` audits what a machine can decide about the runtime: 24 pages — one per route class,
both languages — at 1440 and 390 px, a 320 px reflow pass (400 % of a 1280 px window), reduced motion, images off and
a keyboard walk, with a pinned general ruleset (axe-core, WCAG 2.0/2.1/2.2 A and AA plus best practice) and the eleven
outcomes of the accessibility contract measured rather than asserted. The record is `docs/ACCESSIBILITY_AUDIT.md` and
`.json`, and it includes the text-alternative table for every drawn visual that the register asks for.

**Two failures against outcomes the contract itself states were found, and fixed.**

- **1.4.3 contrast.** The institutional band's fine print measured **4.42:1** where 4.5:1 is required — on all 288
  pages, in both languages, since D1. `--mute` moved two points darker, `#66717B` → `#646F79`: 4.56:1 on the band,
  5.13:1 on paper. The role is unchanged, the change is imperceptible, and it is the smallest value that meets the
  rule the design published. `design/02_TOKENS.json` regenerated.
- **2.5.8 target size.** Of 129 targets under 24 × 24 px, 117 met one of the criterion's own exceptions — inline, or
  24 px spacing — which is why a bare count would have meant nothing. Twelve met neither: the band's group links, the
  disclosure summaries and the record list inside one, all 22–23 px tall with neighbours closer than 24 px. The design
  already had a rule for exactly this case; it was extended to the three families it had missed.

After the fixes: **0 WCAG violations from the ruleset, 0 contrast failures, 0 targets failing 2.5.8, 0 unnamed
controls or landmarks, 0 unlabelled controls, 0 reflow overflow at 320 px, 0 heading-level jumps, 0 images without
`alt`, and no keyboard trap.**

**Two findings were not fixed, because neither is Code's to decide.** Two navigation landmarks carry the same governed
name — the page's next-actions section and the spine's first edge group — so a screen-reader landmark list shows it
twice; which one changes, and to what, is a composition and naming decision, escalated with three options. And a
figure table's empty corner cell is DEBT-013's recorded preference, which needs a governed label.

**Nothing here claims conformance, at any level.** Screen readers in Arabic and English, whether each heading
describes its section, whether each visual's text alternative carries the same analytical point as the picture, voice
control and switch access, and forced colours judged by eye are all listed as outstanding for the auditor. The
Accessibility page continues to say the resource is designed against WCAG 2.2 and is still to be tested.

## 2026-09-29 — EAD-10: the implemented runtime measured, and what EAD-03 now costs

The pre-design baseline was measured before there was a design. The runtime is measured now, with the same script and
the same twelve route classes in both languages, so the two records compare like with like:
`docs/SUSTAINABILITY_IMPLEMENTED_RUNTIME.json`, with the table in `docs/SUSTAINABILITY_METHOD.md`.

A cold page transfers 9.83–10.19 MB. **94–97 % of that is the canonical logo.** Everything else on the page together —
the document, the stylesheet, the script and the type — is 285–656 KB. A warm page transfers nothing. Opening Search
loads the local index once, about 321 KB with gzip, and only then. The page makes no external request of any kind.

The only increase over the baseline is about 200 KB of self-hosted type, and it buys correctness rather than costing
it: the baseline named IBM Plex and shipped no font file, so a reader without it installed read the product in a
fallback face — Arial, or Tahoma for Arabic. The runtime ships the six faces the stylesheet declares and preloads the
two a first paint needs in the reader's language. HTML is comparable and slightly smaller at the top end; the social
images cost a page nothing, because a platform fetches one when a link is shared and the page never does.

**This sharpens EAD-03 rather than closing it.** The logo's share is no longer an estimate from a pre-design build; it
is measured on the site that would ship. The derivative sizes are listed and the export is one command, but a
derivative of the mark is the owner's to approve, so Code does not run it and the master stays untouched.

**No budget is set and no carbon figure is computed**, and none may be: the release host is not chosen (OWN-03), so
its compression and caching are unmeasured. That half of EAD-10 is release work, and the method says so.

## 2026-09-29 — EAD-06: the search query is URL-addressable; what the facet still waits on

`handoff/ENGINEERING_HANDOFF_EXPECTATIONS.md` §2 requires that tool state which matters — Compare records, filters,
the search query — be URL-addressable, reloadable and able to survive a language switch. Compare already met it; the
search did not. The Evidence directory's own search now writes its query to `?q=`, reads it back on load, restores
both the field and the results, carries across the switch to the other edition, and clears the address when the field
is cleared. A query that arrives from the URL is rendered as text and never as markup.

Only the page's own search owns the page address. The dialog floats over whatever page the reader is on, so rewriting
that page's address as they type would change what they would share; a gate and a negative control hold that line in
both directions.

**Two of EAD-06's four parts turned out to be already shipped**, by the accepted design, at the cutover: entry into
Compare from exactly the thirteen comparable records with that record pre-selected, and the mobile form of the
four-column comparison, which stacks below 640 px with every row a block and each cell numbered in the inline-start
gutter. They are recorded rather than rebuilt.

**The result-type facet is blocked, and that is worth stating plainly rather than leaving it to look undone.** Its
option labels are governed (`UI-JS-TYPE-PAGE` … `UI-JS-TYPE-SOURCE-LOCATOR`), but the facet's own accessible name and
the label for the state where no type is chosen are not, and Code does not author a label. The source directory's
control cannot stand in: it says "Find a source by title". Escalated as `NEEDS_CONTROLLED_CONTENT`. The search status
total ("10 of 79" rather than "10 results shown") remains blocked on the governed `{n} of {m}` form escalated at D7 —
a query matching 79 records still reads as a corpus of ten, and no amount of engineering fixes that without the form.

## 2026-09-29 — The D6 runtime defect fixed: governed dates no longer reverse in the Arabic tools

Design found this at D6 on the printed Arabic Compare page and escalated it to Code, because it never edits the
runtime: `site-src/app.js` wrote each record's governed period into a table cell as plain text, and after Arabic
letters the two ISO dates rendered with their parts reversed — "07-11-2022 إلى 09-01-2023" for a period that runs
2022-11-07 to 2023-01-09. The date a reader saw was not the date the record holds.

Every page already isolates those runs in its own text layer. The runtime now uses **the same expression**, character
for character — `scripts/yfie/text.py` `LTR_RUN`, covering ISO dates, numeric ranges and signed values — through one
helper, so a value a tool writes into a page reads the same way as one the page was rendered with. It is applied
wherever governed record text reaches an Arabic page, not only in the cell the lens happened to read: the Compare
table's cells and column heads, the boundary paragraphs beneath it, the record links, and the search results' titles,
summaries and period line.

Two things keep it from drifting back. `scripts/validate.py` fails if the runtime's expression is not the renderer's,
or if the helper is gone; and `scripts/tests/test_gate_negative_controls.py` proves both of those still fail, on the
source file rather than on a built page — the suite now accepts controls on either.

## 2026-09-29 — EAD-05: the Method & Measurement navigation group

Design owned this decision and had made it; it is recorded here as shipped rather than as work. The group is a named
`role="group"` whose governed label is a non-link `glabel`. At 900 px and above a hairline sets it off from the other
destinations and its label sits on the links' baseline; inside the opened menu below that width it stacks under a
quieter label. Both labels and both destinations are unchanged and governed, and the same holds in Arabic.

## 2026-09-29 — EAD-09: the governed social images, and `og:image`

`scripts/social_images.py` rasterises the design's own social templates — one 1200 x 630 frame per route and language,
filled only with governed text (`design/08_ASSET_MAP.md` §4) — into 286 PNGs, and `scripts/build.py` copies them into
`dist/assets/social/`. Every page now carries `og:image` (root-relative before the owner sets a public origin, absolute
after, like every other URL in the discovery contract), its declared size, `og:image:alt` (the page's own title) and
the `summary_large_image` card type. No new text: the templates print what the page already prints.

**Two assertions written for the state before the images existed moved with the feature rather than being dropped.**
Gate F6-G01 asserted that no page carried an `og:image`; it now asserts that each page carries its *own* governed
image, at the declared size, present in the build, described by its own title. `check_acceptance.py`'s `no_og_image`
criterion is repointed the same way. `scripts/tests/test_gate_negative_controls.py` gains two controls that prove both
still fail: an `og:image` naming an image the build does not ship, and one that loses its declared size.

**Why the images are committed rather than made during the build.** Rasterising needs a browser; `scripts/build.py`
must stay standard library only and finish in seconds, because it runs inside every Master transaction and in a CI job
with no Chromium. So they are build inputs, regenerated by one documented command and committed — the same promise
`dist/` makes, that the reviewed bytes are the served bytes. Staleness is caught without rendering anything:
`scripts/social_images.py --check` rebuilds every template in pure Python and compares its SHA-256 with the one
recorded when the image was made, so a governed string changing anywhere fails the check and names the routes to
regenerate. Comparing rendered bytes instead would make a Chromium version bump look like a content change.

**The cost, stated plainly: 17.1 MB of generated PNG, committed.** That is a real addition to the repository, for a
feature that only takes effect once a link to the site is shared publicly. It is recorded in
`FINAL_OPEN_ITEMS_REGISTER.md` with the three steps that reverse it, so the owner can decide otherwise without
archaeology. Git stores the content once even though the files appear both as inputs and inside `dist/`.

## 2026-09-29 — EAD-01 on `claude/hopeful-mccarthy-jgip83`: one production runtime; the replaced renderer removed

The accepted Design implementation becomes the repository's renderer. `design/reference/yfie/` moves to
`scripts/yfie/` (by `git mv`, so its history follows it) and `scripts/build.py` becomes a thin driver over it, writing
the complete static site a host serves: 288 documents in both languages, the neutral root entry, the bilingual 404,
`robots.txt`, and `sitemap.xml` once the owner sets an origin. The 1,643 lines of baseline page composition are
deleted, and `site-src/styles.css` with them. `design/reference/` keeps its harness and its six checks and now builds
**through** the production package, so those checks protect the code that ships; it holds no renderer of its own.
There is one production renderer, reached by one production entry point.

No governed value, wording, unit, universe, period, evidence state, source relationship, limitation or Arabic term
changes, and nothing under `authority/`, `audit/`, the projections or the two controlled contracts is touched.

**EAD-04 closes with it, by construction.** The recolouring of the logo (`brightness(0) invert(1)`) lived only in the
baseline stylesheet, which no longer exists or ships; the accepted stylesheet contains no filter, blend or mask.
**EAD-08 narrows**: the build ships the six IBM Plex faces the stylesheet declares, with their licence, instead of all
twenty-four, and the two first-paint faces stay preloaded per language.

**Parity is proved, not asserted.** The pre-design renderer's own answer was frozen before it was removed:
`scripts/tests/baseline_content_oracle.json` holds, for all 286 documents, the normalised number multiset of `<main>`
and its rendered text as that renderer gave them at `2f9a93c`, with the SHA-256 of every projection it was derived
from. `scripts/tests/test_cutover_parity.py` holds the new output to it at `design/reference/check_content.py`'s
strength — no governed number lost, none gained ungoverned, no governed sentence lost — and reports 286 documents, 0
differing. It was proved in both directions before it was trusted: it fails when a governed paragraph is dropped from
one record and when one governed number is altered.

**The cutover found a real defect, and it is fixed here.** Explore's four question clusters were not governed:
`scripts/handoff_inventory.py` recovered them by scraping the baseline renderer's own HTML out of `dist/`, and the
accepted renderer read them back from that inventory — a build that was an input to itself. Removing the baseline
renderer emptied the scrape, the inventory recorded four empty clusters, and `/explore/` rendered with no questions at
all. The R8.4A sets (Home's four starting questions and Explore's four clusters) now live in one named place,
`scripts/yfie/question_sets.py`; the inventory reads them from there and parses no markup; and the regenerated
inventory is byte-identical to the accepted one at `2f9a93c`, so the selection is provably unchanged. EAD-11 stays
open — the sets belong in a governed contract, which is the steward's to land — but nothing is recovered from rendered
markup any more. This corrects the planning appendix of 29 September, which recorded that Explore's clusters "already
come governed, through the handoff inventory's `question_groups`": they came from the baseline's markup.

**Every gate keeps its assertion and changes only how it finds things.** Built into `dist/`, the accepted design
raised 2,332 validator failures, all of them selectors written against the baseline's class names and attribute order;
all are re-pointed and the validator is green. Two were outright regex faults the new markup exposed rather than
selector drift: `\bid="` also matched `data-record-id="`, so every record page reported a duplicate DOM id, and
`<th(?!…scope=)` also matched `<thead>`, so every table reported a header cell without scope. Where the accepted
design repeats governed text by design — a clock-first object carries its own period, universe and summary — P1-G06
keeps the scope it always had, the page's authored prose, and a duplicated authored paragraph still fails it.

**P3-G02 is replaced, not deleted.** It asked that the pre-design baseline draw nothing. It now checks each drawn
visual against its contract: only a contract the renderer's own registry may draw is drawn, a contract that binds rows
must print every one of its governed row values, its tier must be one that plots, its governed title and the grammar
label of every state and marker it carries must be printed, it must carry the ordered-text fallback and a captioned
value table with a column header, a contract that binds no rows may draw governed structure but no value scale, a
graphic outside a governed figure fails, and every drawable contract must reach both editions.

**Every re-pointed gate is proved to still catch its own fault.** `scripts/tests/test_gate_negative_controls.py`
breaks one thing in the built site at a time — an `aria-current` removed, a breadcrumb dropped, a governed row value
rounded, a question dropped from Explore, a decorative graphic added — and requires the gate to say so. A re-pointed
selector that silently matches nothing would pass the suite and fail these.

Nothing here declares PUBLIC RELEASE READY, and no WCAG conformance is claimed: the EAD-02 audit is still to be done.

## 2026-09-28 — Design D7 closure on `claude/dreamy-archimedes-e8qx5v`: every recorded blocker settled, the product judged by independent lenses; ready for independent acceptance

The closure the owner asked for after withholding acceptance at the technical checkpoint below. It changes the built
product, not the governed content: no governed value, wording, unit, universe, period, evidence state, source
relationship, limitation or Arabic term is touched, and no interface copy is authored.

The one blocker is closed. **DEBT-019** — `/explore/` rendered its governed section 5 twice, the second time as an
answer with no questions under it, and the rubric ordinals disagreed with the page index. The section now renders once,
at the top, as the answer that holds the clusters it introduces (its governed role as the rubric, its governed heading
as the `h2`, its body as the clusters' introduction, the interface lead kept so text parity holds), and a section
rubric's ordinal is now its position in the spine index in every family renderer, which also closed the same latent
mismatch on `/people/`, `/evidence/`, Compare and `/data/` (DL-D7-007).

The four visual debts are settled. **DEBT-016**: the lockup carries the publisher's name in type — the mark plus
**CauseWay** (semibold, the ochre role) above the governed product name, in the product bar of every page, the export
identity line, the social head and the print head, as an isolated left-to-right run in Arabic; the name is the proper
name the governed strapline, citation lines and © line already print, so nothing is authored, and the publisher is now
named on twelve of twelve measured entry screens. The debt stays open on the 10 MB master file alone, which blocks
release, not the gate (DL-D7-008). **DEBT-014/015**: every composed page renders the strip where its phone reader first
needs the map and the foot spine keeps only the edge groups; the governed statement is neither split nor shortened, and
the phone head's rhythm brings the first figure group onto Home's first screen in both languages (DL-D7-009).
**DEBT-007**: decided as restraint, with the reasoning recorded; no motif, border, map, image or new palette.
**DEBT-011 is the closure's recorded no.** Closing both `/data/` dependency groups by default cut the page 44 %
(50,291 → 28,004 px EN, 54,555 → 29,012 px AR at 1440 px) and every design check passed (DL-D7-010), but the full gate
suite then caught that the supporting group is the only place a locator-only source appears: closing it put the
governed "cite a source by its reference and locator" path behind a disclosure and `scripts/tests/test_public_tools.py`
fell from 25/26 to 24/26. Design does not edit a repository test so its own change can pass, so the change was
reverted and the debt left open, with the measured prize and the constraint recorded for whoever takes it next and a
new `check_site.py` assertion (`locator_only_source_reachable`) so the next attempt meets that wall inside the design
checks rather than at the repository gate (DL-D7-013).

The product was judged by three independent lenses on the built pages — an Arabic-first reader, a cold reader arriving
on one Evidence Record, and a phone reader — each writing its report into the repository as it went
(`design/evidence/d7/cold_read/lens-*-closure.md`). Four interface defects they found are fixed (DL-D7-011, DL-D7-012):
the governed source intro promised "Open the source record here" on the ten records that render no source card and was
denied by the next sentence, and now prints only where a source card exists (20 documents affected, 0 remain); the
flagship same-year figure now repeats its governed unit in the axis row, so a hostile crop carries it (the marker that
prevents the figure reading as a fall already survived every such crop); the phone strip on Compare moved from 71 % of
the scroll to 8 %; and every Arabic section heading, which rendered 30 % smaller than the prose it introduced because
the English uppercase-and-tracking device cannot transfer to a script without case, is now sized against its body.

Recorded rather than claimed, each with its measurement: two first-screen shortfalls (the Arabic record's limit index
entry 3 px below the fold at exactly 390 × 844; the Reading's phone screen whose only forward link is the breadcrumb,
because the governed boundary rightly displaces the strip), `/data/` still long on a phone, in-flow targets at
30–33 px against the recorded 24 px minimum, and the percent sign's two individually-correct sides in Arabic. Escalated
as content (`design/ESCALATIONS.md`): the Compare contract's governed `alt_text` ends with its governed
`prohibited_inference` verbatim, so two sentences print twice; CLM-039 carries no values or dates for its central
comparison; and the magnitude notation, strengthened with the closure's evidence — two independent trained readers in
two sessions have now misread a governed value by a factor of a thousand from it alone.

The three reader walks are recorded with what was clumsy, the 18 catalogue-only coverage rows are settled with the
reason each cannot be proved without inventing an evidence record, and the bar of the closure brief is answered surface
by surface in `design/10_ACCEPTANCE_CHECKLIST.md` §K.5. All 73 acceptance lines are met and no design debt is flagged
"blocks D7"; DEBT-008 and DEBT-016 remain open as release items. Records: `design/00_DESIGN_README.md` (status and
DL-D7-007…012), `design/10_ACCEPTANCE_CHECKLIST.md` (§K.4 adjudications updated, §K.5 new),
`design/04_PAGE_FAMILY_COMPOSITIONS.md`, `design/08_ASSET_MAP.md`, `design/09_CODE_HANDOFF.md`,
`design/DESIGN_DEBT.md`, `design/COVERAGE.csv`, `design/ESCALATIONS.md`, `design/evidence/d7/`, and the README's
design-programme section and programme tracker. **D7 is not declared accepted and nothing is declared PUBLIC RELEASE
READY:** the owner's visual acceptance, and the content and runtime items escalated to the steward and to Code, remain.

## 2026-09-28 — Design D7 technical checkpoint on `claude/dreamy-archimedes-e8qx5v`: every check green, the technical criteria evidenced; final visual acceptance withheld by the owner

Branch `claude/dreamy-archimedes-e8qx5v` (from the accepted `main` `0ccdf01`, the merge of pull request #6). D7 is the
acceptance of the runnable, fully populated bilingual reference site (`design/reference/`: 288 documents, every tool and
state, both languages, four widths) against `handoff/DESIGN_ACCEPTANCE_CRITERIA.md`. At this checkpoint every D1–D6
check, the three repository suites and the new D7 check pass on the tree, and the technical criteria are evidenced line
by line in `design/10_ACCEPTANCE_CHECKLIST.md` (new); the owner has withheld the final visual acceptance, so D7 is not
declared met, the Design package is not declared accepted, `design/COVERAGE.csv` keeps its rows at `VERIFIED`, and the
README is not reconciled. The D7 check `design/reference/check_acceptance.py` (new) asserts what no earlier check did —
strict CSP on every document and frame, the discovery head byte-equal with `dist/` on every edition page, one `h1`, the
skip link, the language switch, the trust layer, no download or bundled document, the nine no-locator sources never
named, the CLM-044 value never printed, every external locator with its cue, the shipped fonts and licences (14,248
static assertions) — and drives the last-ten-percent surfaces of the brief in EN and AR with evidence (59 assertions;
`design/evidence/d7/`). Fixed at the checkpoint: the provider matrix (VIS-PROVIDER-OBSERVABILITY) is unshipped until its
six labels are governed and renders as its contract's text frame, so no `⟦NCC:…⟧` placeholder ships and the device is
removed (DL-D7-001); the structured data the baseline writes (WebSite, BreadcrumbList, Article) is restored in the
reference head through the one discovery implementation (DL-D7-002); the two critical faces of each page's language
are preloaded (DL-D7-005). An attempt to render Explore's governed section 5 once dropped its governed heading and was
reverted (DL-D7-003; DEBT-019).
DEBT-017 closed by measurement (DL-D7-004); DEBT-002 and DEBT-013 closed. Two independent cold readers (EN, AR) read
the checkpoint tree: their reports are in `design/evidence/d7/cold_read/`, every finding is adjudicated in the checklist
§K.4; two verified design findings stay open and block the acceptance until the resumption (DEBT-018, a governed signed
value in Arabic prose outside the text layer's isolate; DEBT-019, Explore's repeated section 5 and its rubric ordinals
against its index), and the
content findings are escalated to the steward (`design/ESCALATIONS.md`, D7 — among them the `/people/` education
sentence against the FINDEX contract). Records: `design/05_RESPONSIVE_RTL_LTR.md` (new), `design/09_CODE_HANDOFF.md`
(the D7 table), `design/DESIGN_DEBT.md`, `design/ESCALATIONS.md`, `design/03`/`04`/`06`/`08` for the waiting matrix,
`design/00_DESIGN_README.md` (status, plan, DL-D7-001…005). No governed content, projection, contract, `dist/` file,
test suite or audit record changed. Not declared: D7 met, DESIGN accepted, PUBLIC RELEASE READY.

## 2026-09-28 — Design D6 accepted by the merge of pull request #5; present-state records reconciled; D7 next

Pull request #5 (`claude/bold-maxwell-r3o015`, head `125aa44`, D6 proved on that exact tree) was merged into `main` at
`f4739a5` by the repository's normal method (a merge commit) on the owner's instruction after the owner declared D6 met
on `125aa44`; Verify (Governance gates, Browser acceptance) is green on the merge commit. Post-merge checks on `main`:
`125aa44` is an ancestor of `f4739a5` and the merge tree is identical to it; `scripts/checksums.py --check`,
`scripts/repository_manifest.py --check` and `scripts/validate.py` pass; the Production Master (`17db032b…`) and the
Page Specs (`d4574804…`) match the fingerprints the checkpoint, the Context and the README record. The present-state
records that described D6 as pending the owner's merge are corrected in place — the README current-state row, the
Design README status, plan row and D6 sentence, `design/09_CODE_HANDOFF.md`, the process note in
`design/ESCALATIONS.md`. No historical entry is rewritten; no governed content, projection, contract, `dist/` file or
audit record changed. D7 (acceptance against `handoff/DESIGN_ACCEPTANCE_CRITERIA.md`) is the next gate and has not
begun. Not declared: DESIGN HANDOFF READY, PUBLIC RELEASE READY.

## 2026-09-28 — Design D6 met on `claude/bold-maxwell-r3o015` (pending the owner's merge of pull request #5): the visual system, portable frames and print system, proved on the final tree

Branch `claude/bold-maxwell-r3o015` (from `2effd8b`), draft pull request https://github.com/CausewayGrp/Financial-inclusion-/pull/5.
Every one of the 36 visual contracts now stands in its tier's form on every route that binds it: thirteen drawn (the
three D6 forms — the provider matrix, three dated lanes, bars from zero without ranks — beside the ten drawn at D1–D2),
twenty-two governed text frames (TABLE_TEXT_FIRST contracts without rows, the SUPPORTING contracts, the Compare tool's
own contract), and the one RETIRE contract asserted absent. Every figure carries the detached frame (title, question,
scope, the boundary once, the credit isolated left-to-right, the canonical link, the edition), a text alternative with
a named-column table in a named region, only the palette's colours, no two labels meeting, and fits 320 and 390 px;
one pass over every finished document (`yfie/text.py`) isolates every ISO date and numeric range left-to-right (in
Arabic a plain date renders reversed and a plain range swaps its ends), and governed English time boundaries print as
the Master holds them, isolated and marked. Portable evidence: export frames for the
thirteen drawn contracts (`out/_export/`, 26 documents; the export control designed, unshipped until OWN-04),
five social-image templates over the eleven families (`out/_social/`, 286 frames from governed text only; Code
rasterises), and the print system (chrome hidden, objects whole, figures with their boundary, a print-only provenance
block with the canonical URL and citation last on every page, the Reading as a document). Typography is authored at
three weights (Regular, Medium, SemiBold; emphasis at 600, never a browser default). Verified on the exact final tree:
`design/reference/check_visuals.py`, five phases (36 contracts × EN/AR on every binding route, 2,856 contract
assertions; 52 forced-colours and print checks on the drawn contracts; 26 export and 286 social frames;
133 print checks on the eleven family routes × EN/AR; 598 documents and frames scanned for a date or range outside
an isolate; 0 failures), the D1–D5 gates re-run (`check_content.py --text`, `check_binding.py`, `check_site.py --gate
d2|d3|d4`, `check_journeys.py`, `check_trio.py`, `tokens.py --check`) and the repository suites on the reference site;
the D4 gate caught one regression the first D6 text layer had introduced (an unbreakable identifier isolate overflowing
seven record pages at 320 px), fixed before the final run. Five red-team lenses (measurement and statistics,
information visualisation and editing, native Arabic editing, journalism with a hostile source owner, accessibility and
frontend engineering) reviewed the built output; every MUST-FIX is closed in the layer that owns it, every content or
authority observation is escalated, never fixed in design, and the one runtime defect found (the Compare table's
reversed Arabic dates, `site-src/app.js`) is recorded for Code with its patch (DL-D6-007, `design/ESCALATIONS.md`). Records:
`design/06_VISUAL_TABLE_SYSTEM.md` and `design/08_ASSET_MAP.md` (new), DL-D6-001…007, `design/COVERAGE.csv` (72 D6
rows `VERIFIED`, print and social rows added), `03`, `04`, `07`, `09`, `DESIGN_DEBT.md` (DEBT-010 and DEBT-012 closed,
DEBT-013 narrowed to the six placeholders, DEBT-017 opened), `design/evidence/d6/`. Six placeholders remain on the site until the
steward governs their labels (five matrix headings and the payment-system-operator class). Runtime, projections,
contracts and `dist/` untouched. Not declared: DESIGN HANDOFF READY, PUBLIC RELEASE READY.

## 2026-09-27 — Design D5 accepted by the merge of pull request #4; present-state records reconciled; D6 opened

Pull request #4 (`claude/epic-cori-60fpeb`, D2 met at `9c263ac`, D3 at `beecdbb`, D4 at `aee1e1b`, D5 at `8be8e22`) was
merged by the owner into `main` at `2effd8b`; Verify (Governance gates, Browser acceptance) is green on the merge commit.
The present-state records that still described D1 as the last accepted gate and D5 as pending the merge are corrected
in place — the README current-state row, the Design README status and plan table, `design/09_CODE_HANDOFF.md`,
`design/07_INTERACTION_ACCESSIBILITY.md` — and a process note records the D6 branch (`claude/bold-maxwell-r3o015`,
created at `2effd8b`). No historical entry is rewritten; no governed content, projection, contract, `dist/` file or
audit record changed. D6 (the remaining visual contracts, detached and export frames, social-image templates, print and
portable evidence) is the working gate. Not declared: DESIGN HANDOFF READY, PUBLIC RELEASE READY.

## 2026-09-27 — Design D5 (in progress): every tool state, technical state and journey proved by keyboard; the technical voice

Same branch and draft pull request (`claude/epic-cori-60fpeb`, https://github.com/CausewayGrp/Financial-inclusion-/pull/4;
D4 met at `aee1e1b`). `design/reference/check_journeys.py` walks the inventory's thirteen journeys by keyboard at 390 and
1440 px in English and Arabic (52 of 52 walks: a link the page offers takes focus, shows the outline, activates with
Enter; each landing asserted against the journey's success condition) and drives every technical state in both
languages (28 of 28: Compare's link errors and the same-record state, search no-match and index-unavailable, the
register's unknown deep link and no-match, record-context unknown/malformed/valid, the language switch with state, no
script). A third voice is designed for technical states — a dashed hairline, body ink, never the boundary's double rule,
the counter colour or an evidence-gap object (DL-D5-001) — and the same-record state no longer reads as an assessment.
`design/07_INTERACTION_ACCESSIBILITY.md` records the three voices, the keyboard paths, motion, zoom, forced colours, no
script and print, every technical state and journey, and the two verification states no record carries today (designed
with their governed copy, never on an invented record). Records: `design/COVERAGE.csv` (82 D5 rows `VERIFIED`, 4
`DESIGNED`), DL-D5-001…004, `design/03_COMPONENT_CATALOG.md`, `design/09_CODE_HANDOFF.md` (state at D5),
`design/DESIGN_DEBT.md` (DEBT-014 narrowed), `design/ESCALATIONS.md` (the external-link cue raised),
`design/evidence/d5/`. Runtime untouched. Not declared: DESIGN HANDOFF READY, PUBLIC RELEASE READY.

## 2026-09-27 — Design D4 (met at `aee1e1b`): every document bound and asserted; the binding proved

Same branch and draft pull request (`claude/epic-cori-60fpeb`, https://github.com/CausewayGrp/Financial-inclusion-/pull/4;
D3 met at `beecdbb`). Every evidence record is asserted against its own governed bundle — the seven questions, the
boundary on first load, the clock before the claim, source cards equal to the bundle's sources with public locators
only, the lineage state and members exactly where carried, the no-locator states, the trace chips, the Compare entry,
the own visual, the boundary once per frame — and the three remaining domain answers (`/firms/`, `/finance/`,
`/providers/`) against their contracts (`design/reference/check_site.py --gate d4`: 904 renders, 452 smoke tests, 3,822
hard-state assertions, 10 degraded renders, all pass; the neutral root entry asserted). `design/reference/check_binding.py`
proves the binding from the inventory's projection roles (every RENDER and CONTRACT projection read by the one content
path; no REFERENCE or VIA_SPEC projection read; 286 edition pages + root + 404; no copied content model) and the one
deviation it found — `public_claims.json` loaded and unused — is removed. Records: `design/COVERAGE.csv` (841 D4 rows
`VERIFIED`; every route row of the ledger is now `VERIFIED`), decision log DL-D4-001…004, `design/09_CODE_HANDOFF.md`
(state at D4), `design/04_PAGE_FAMILY_COMPOSITIONS.md`, `design/DESIGN_DEBT.md`, `design/evidence/d4/` (42 PNG). Not
declared: DESIGN HANDOFF READY, PUBLIC RELEASE READY.

## 2026-09-27 — Design D3 (met at `beecdbb`): the synthesis pages composed and proved; the Home cold-reader test run and acted on

Same branch and draft pull request as D2 (`claude/epic-cori-60fpeb`, https://github.com/CausewayGrp/Financial-inclusion-/pull/4;
D2 met at `9c263ac`, not yet merged — process note in `design/ESCALATIONS.md`). The Reading index, the ten Readings,
Measurement, Methodology, the eight trust pages and the bilingual 404 are reviewed in both languages at 390 and 1440 px
and asserted on the rendered DOM (`design/reference/check_site.py --gate d3`: 168 renders, 84 smoke tests, 252 hard-state
assertions — the Reading's boundary-before-essay, clocks, trace and measure; Measurement's ten equal, unnumbered,
deep-linkable priorities; About in plain language; Contact and Corrections with the report path — and 18 degraded renders,
all pass; the measure assertion corrected from a guessed width to the measure property, DL-D3-004). Four fresh cold
readers (English and Arabic, 390 and 1440 px) read only the rendered Home page; their reports are kept verbatim in
`design/evidence/d3/cold_read/` (DL-D3-001). The design findings are corrected within the Lock (DL-D3-002): the governed
product statement and its two actions open the page before the first figure (the baseline's order); one link per compact
evidence object, named by the action and the title; the figure's boundary printed once, in the foot, under the governed
"What not to conclude" label; a text frame shows its description as its body; the framing record sits in the section it
frames; the boundary's double rule spans the column; the primary-nav group set off by a hairline; the Arabic rubric 14 px
(`design/02_TOKENS.json` regenerated). The content findings (date forms, precision, jargon, the alt text that restates
its boundary, the text-first label, the publisher's legibility, Arabic calques) are escalated, none filled with authored
copy. `check_site.py` gains the Home assertions and the Orientation hooks. Records: `design/COVERAGE.csv` (164 D3 rows
`VERIFIED`), `design/DESIGN_DEBT.md` (DEBT-014…016), `design/ESCALATIONS.md`, `design/09_CODE_HANDOFF.md` (state at D3),
`design/04_PAGE_FAMILY_COMPOSITIONS.md`, `design/03_COMPONENT_CATALOG.md`, `design/evidence/d3/` (38 PNG). Not declared:
DESIGN HANDOFF READY, PUBLIC RELEASE READY.

## 2026-09-27 — Design D2 (met at `9c263ac`): the hard families built and proved; every document renders; the D1 residuals reconciled

Branch `claude/epic-cori-60fpeb` from the accepted `main` (`851f496`, the merge of pull request #3), landing through
draft pull request #4 (https://github.com/CausewayGrp/Financial-inclusion-/pull/4). The one content
path now loads every family (`design/reference/yfie/content.py`), `families.py` composes Explore, the domain answers,
the Evidence directory, Compare and Data & sources in the T4 grammar (and the Reading index, Measurement and trust pages
by the family rule until D3), `visuals.py` draws VIS-FINDEX-GAPS, VIS-REMITTANCE-MACRO, the POS small multiple,
VIS-PAYMENT-ANATOMY, VIS-REMITTANCE-COST and the payment chain per contract with the evidence-state grammar, and
`build.py` writes all 288 documents plus the root entry, the 404 and `robots.txt`. `check_site.py` asserts each §9.2
hard state on the rendered DOM (168 renders, 84 smoke tests, 157 assertions, 20 degraded renders, all pass); the two
repository browser suites (25/26, 168/168), bilingual invariance (0 of 143) and `check_content.py --text` (288
documents; its number rule is bundle-scoped and its text rule inline-tag-safe) pass on the reference site; a rounding
fault in the number formatter was found and fixed. The five D1 residuals are reconciled by their true authority
(DL-D2-002): the Arabic credit line (the contract's own language note; isolated left-to-right), the in-page navigation
name (`aria-labelledby` from governed text; DEBT-006 closed) and Home's order (brief §4.5) are closed; the pacing
marker and the IMF lane state stay open for the steward. Records: `04_PAGE_FAMILY_COMPOSITIONS.md` and
`03_COMPONENT_CATALOG.md` created; `COVERAGE.csv` — 190 D2 rows `VERIFIED` (176) or `DESIGNED` with the gap explained
(14), 1,001 D3/D4 rows `BUILT`; `DESIGN_DEBT.md` (DEBT-004, -006, -009 closed; DEBT-011…013 opened); `ESCALATIONS.md`
(two raised: fallback-table column labels; rows for VIS-TARGET-RESULT-STATE and VIS-MFI-DIVERGENCE);
`09_CODE_HANDOFF.md` state at D2; `02_TOKENS.json` regenerated; `design/evidence/d2/` (60 PNG). README current-state
row updated. No governed content changed; no projection, contract, `dist/` file or audit record edited.

## 2026-09-27 — Design D1 hand-back: second independent pass; residuals closed; verdict recorded

Same branch and pull request; the D1 hand-back is posted on the pull request. A second, fresh repository-only reviewer
confirmed every MUST-FIX of the final review closed and returned "D1 DESIGN COMPLETE — OWNER MERGE REQUIRED"
(`design/exploration/d1_canvas/review/second_pass.md`; `design/01_FOUNDATIONS.md` §6; DL-D1-008). Its residuals are
closed here: the eight verified grammar rows' note field repaired in `design/COVERAGE.csv`; no empty "Source:" line on
a figure without a credit; a round tick step derived once from the data (0 / 2,000 / 4,000 / 6,000); the 320 px table
measurement corrected to 23–80 px (DEBT-010, `01_FOUNDATIONS.md` §2.5, §3.4, §4.4); the lens reports' path corrected;
three overstated sentences corrected (what the checks cover; a selector that matched nothing; the attribution of the
text and degraded checks in README); 24 px hit areas on every non-inline link and button in `main`, asserted by
`check_trio.py` together with a forced-colours emulation; the foot spine's edges kept in print; PNG evidence
regenerated. README current-state row updated. No governed content changed; D1 exit is the owner's merge decision.

## 2026-09-27 — Design D1: independent final review adjudicated; corrections; evidence committed

Same branch and pull request. A repository-only final review (`design/exploration/d1_canvas/review/final_review.md`)
returned NOT ACCEPTED with eight MUST-FIX items; all are closed and re-verified (`design/01_FOUNDATIONS.md` §6, §4.4;
decision DL-D1-008): the Home system visual renders through its contract frame (boundary, scope, credit, link); one
verification spine at any width with the index at the foot on phones; readable fallback tables at 320 px; forced
colours keep chart text; the record's disclosure content prints; the F6 attributes the validator requires are
carried; every governed kicker, label and gloss the baseline prints is rendered and `check_content.py --text` proves
text-block parity; `02_TOKENS.json` is generated and checked by `design/reference/tokens.py`; `check_trio.py` gains a
keyboard-only path, degraded-state checks and the committed PNG evidence (`design/evidence/d1/`, 18 files); records
corrected (`01_FOUNDATIONS.md` status and stub, `09_CODE_HANDOFF.md` rows, DEBT-003 closed, DEBT-010 re-measured,
grammar-state ledger rows reconciled); the nine lens reports and the review committed. Two items recorded rather
than changed (Home section order for steward confirmation; navigation without JavaScript below 900 px). No governed
content changed.

## 2026-09-27 — Design D1 (in progress): reference implementation of the stress trio; Design Intent Lock; tokens

Same branch and pull request. `design/reference/yfie/render.py` (composition of the converged direction with every
brief §19 hook), `theme.py` (the one stylesheet, extracted once from the converged composer; print, focus, reduced
motion and forced colours included) and `visuals.py` (RV-CWR-001 drawn with percentage coordinates, no inline style)
render Home, `/evidence/CLM-003/` and `/readings/same-year-different-number/` in both languages; `check_trio.py`
applies the viewport suite's conditions, the hooks and an interaction smoke test with the baseline runtime (24 renders,
12 smoke tests, all pass); content parity and bilingual invariance pass; `check_content.py` now excludes axis tick
labels. The rendered pages were placed on the canvas as row R beside T4 for the drift review — no drift
(`design/01_FOUNDATIONS.md` §4.4). Written from what renders: the Design Intent Lock (§4: MUST PRESERVE / MAY IMPLEMENT
DIFFERENTLY / MUST ESCALATE), the foundational grammar (§5) and `design/02_TOKENS.json`. Records: decision DL-D1-007,
`COVERAGE.csv` (28 stress-trio rows `VERIFIED`, `code_handoff` YES), `DESIGN_DEBT.md` (DEBT-002 updated; DEBT-009,
DEBT-010 opened), `09_CODE_HANDOFF.md` (implementation, print, runtime, temporary vs intended). No governed content
changed. Not yet: the independent final D1 review; D1 is not exited.

## 2026-09-27 — Design D1 (in progress): convergence on T4 · Instrument after the nine-lens critique

Same branch and pull request. Nine independent critique lenses (evidence researcher, Arabic/RTL director,
accessibility, data visualisation, frontend architect, product-design critic, journalist, source institution,
informed Yemeni reader) reviewed the same renders of T1–T4 under one brief (`design/exploration/d1_canvas/LENS_BRIEF.md`);
their findings, the adjudication, the corrections applied to T4 (composer and canvas version 5), the adversarial
tests and the convergence decision are in `design/01_FOUNDATIONS.md` §3 and decision DL-D1-006
(`design/00_DESIGN_README.md`). T4 converges as the D1 direction on two rendered behaviours (a same-year restatement
that cannot read as a fall; a number never met without its clock and bound). Records: `DESIGN_DEBT.md` (DEBT-005
closed; DEBT-006…008 opened), `ESCALATIONS.md` (four D1 items raised: Arabic credit line, Home pacing marker, IMF lane
state question, in-page navigation label), `COVERAGE.csv` (28 stress-trio rows `DESIGNED`; nothing `BUILT`),
`09_CODE_HANDOFF.md` (D1 implications). No governed content changed; one shared renderer formatting fault
("6245" without a separator in fallback tables) fixed in the composers. Still to come in D1: the Design Intent Lock,
`02_TOKENS.json`, the reference implementation of the trio, the Design and independent reviews.

## 2026-09-27 — Design D1 (in progress): thesis exploration recorded — neutral harness, four canvas propositions

First D1 milestone on `claude/practical-cray-sr26c5` (base `8bf19ef`, D0 accepted; the branch name is a process note
in `design/ESCALATIONS.md`). Nothing outside `design/` changed except this changelog, one row in the README status
table, one ignored output folder in `.gitignore`, the manifest and checksums; Master `17db032b…`, Page Specs
`d4574804…`, projections, contracts and `dist/` unchanged. Added: `design/01_FOUNDATIONS.md` (the baseline critique,
thesis hypotheses T1 Register / T2 Argument / T3 Strata and the second-generation T4 Instrument, the exploration
protocol, the benchmark result — every product site NOT INSPECTED — the sequencing process note, the designer's own
critique; comparison, Lock and grammar not yet written); `design/reference/` (the one content path from
`site-src/content/**`, an unstyled harness with every brief §19 hook, a content-parity check against `dist/`);
`design/exploration/d1_canvas/` (the composers that regenerate the four propositions on the Claude Design canvas from
the harness bundle; outputs git-ignored). Updated: decision log DL-D1-001…005, `DESIGN_DEBT.md` (DEBT-003…005),
`COVERAGE.csv` (the 28 stress-trio rows `REVIEWED` with evidence; nothing beyond `REVIEWED`), `09_CODE_HANDOFF.md`
(state at D1). No thesis chosen, no Design Intent Lock, no design system; not PUBLIC RELEASE READY. Gates run for this
commit: `checksums.py --check`, `generate_projections.py --check`, `validate.py`, `repository_manifest.py --check`,
`design/reference/check_content.py`; the browser suites run in CI against `dist/`, which did not change.

Same day, later push: T4 revised after a native-size inspection at 320–1440 px in both languages (four design defects
fixed — the illegible signature panel, the 900–1200 px grid, the mobile question strip, dropped SVG value labels —
recorded in `design/01_FOUNDATIONS.md` §2.5); inspection, tiling and crop tooling added under
`design/exploration/d1_canvas/`; a paper scaling test of the candidate grammar against the fixed sitemap (§2.6). No
thesis chosen; the lens critique is the next step.

## 2026-09-27 — Design D0: steward verification recorded in the Design README

`design/00_DESIGN_README.md` still read "awaiting steward landing" and left direct authority verification to the
steward after D0 landed (`7c9b8a1`). Its status line, a steward verification note under §2 (direct Master and Page
Specs SHA-256, both matching; every `CONTRIBUTING.md` §5 gate green) and a steward line under DL-D0-001 now record
this, in line with DEBT-001 (CLOSED). Claude Design's own statements and reasoning are unchanged. No file outside
`design/` changed except this changelog, the manifest and checksums.

## 2026-09-27 — Design D0: orientation records landed

Claude Design's D0 hand-back, landed by the steward on `design/d0-orientation` (base `6d954c1`) because the Design
environment cannot write to the repository (its statement: `design/00_DESIGN_README.md` §7). Files, as delivered:
`design/00_DESIGN_README.md` (authority, no supplied visual board, dependency map, D0 comprehension, plan D1–D7 with three
named theses — Register, Argument, Layers — and the decision log DL-D0-001…003), `design/COVERAGE.csv` (1,389 rows, all
`NOT_STARTED`, each with its planned gate), `design/DESIGN_DEBT.md`, `design/ESCALATIONS.md` (none raised),
`design/09_CODE_HANDOFF.md`. Steward additions only: DEBT-001 closed with the gate evidence (direct Master and Page Specs
hashes match; every `CONTRIBUTING.md` §5 gate green) and a confirmation of the start commit in the escalations' process
notes. No file outside `design/` changed except the manifest and checksums.

## 2026-09-27 — Design-enablement control pass (directive D9)

The last repository-control pass before Claude Design, on top of `937bf80` (post-F9 correction). Commit subject
`docs(handoff): design-enablement control pass — kernel, loop, memory, debt, review tests`; the checkpoint tag
`checkpoint/design-handoff-ready` belongs on that commit — the state Claude Design starts from. No Master, projection,
contract or public-page change: Master `17db032b…` and Page Specs `d4574804…` unchanged; `dist/` unchanged. Second
addendum in `audit/FINAL_CLEAN_ROOM_ACCEPTANCE.md`.

The handoff was checked against a quality doctrine for a cold Design recipient. Where it already held, it was kept;
where it was partial or absent, it was strengthened in place — one start file, one brief, no second programme:
- **Brief §0:** a re-readable kernel; a nine-step loop (orient, question, explore, challenge, decide, prototype, test,
  persist, continue); the repository as memory (what to re-read at every gate start, what to update, test, commit and
  push at every gate end); the Code recipient test that closes every gate.
- **Brief §1, §4.6, §5, §6:** a public evidence service, not a generic website; the connected evidence system from bound
  relationships only; two firewall additions (infrastructure ≠ outcome; one lineage repeated ≠ independent
  corroboration) and a rule that layout must protect the distinctions; states that must not collapse; the full list of
  design freedoms and who owns what (Design, Code, owner, release, the Master).
- **Brief §7:** tone; a wider avoid-list; motion, imagery (with a provenance and rights checklist) and dark-mode decision
  logic; four review tests (anti-template, source owner, screenshot misuse, portable evidence).
- **Brief §9:** the small surfaces; "a template applied is not a reviewed page"; twelve audience lenses; §9.4 outcomes
  per family, including a Home cold-reader test at about 30, 90 and 180 seconds.
- **Brief §10, §12, §13, §15:** search as a product; external links; reporting intents and a rule for every input
  (the site collects and submits nothing); per-object download formats, Arabic exports, the four kinds of material and
  data packages (all still disabled until OWN-04, REL-02); micro-interactions; interaction in visuals never
  hover-only; Arabic tested, not only viewed; low bandwidth and an optional, honest footprint note.
- **Brief §19–§20:** decision-log fields; the coverage ledger's status ladder (`REVIEWED` … `ACCEPTED`) with `checks`
  and `code_handoff`; the design-debt register `design/DESIGN_DEBT.md`; four layers kept apart; what a hostable static
  site contains; gates with entry, work, exit evidence and stop conditions; the last-10-percent audit at D7.
- **Criteria, contract, start file:** acceptance section K (review tests, last 10 percent, Code recipient test) and
  matching lines in B–J; the Design-to-Code contract maps design debt and names the four layers; the Code prompt reads
  the debt register, ledger and escalations; README_FIRST points to the kernel and memory rule.
- **Independent cold-reader audit** (a fresh agent, read-only): verdict that a cold Design agent can run D0–D7 from the
  repository alone, every doctrine area present; its defects fixed here — evidence is committed as PNG, never PDF (gate
  F6-G07); a NOT RUN rule when an environment cannot install Chromium; who counts as a cold reader; the hand-maintained
  Design-to-Code flow diagram brought to D0–D7 (and its clipped label fixed); the manifest palette labelled a
  hypothesis; the identity constraints named; `docs/DEPLOYMENT.md` headings cited exactly; README_FIRST points to the
  brief's full freedoms list and says `design/**` is already classified.
- **Records:** directive D9 stored verbatim; README, checkpoint (tag target), Context, audit index and directives index
  updated.

## 2026-09-27 — Post-F9 correction: OWN-07, OWN-08, Design handoff tightened

One bounded correction on top of `03bd654` (F9), before Claude Design starts. Commit subject
`fix(handoff): post-F9 correction — OWN-07, OWN-08, handoff tightened in place`; the checkpoint tag
`checkpoint/design-handoff-ready` belongs on that commit. No Master change: Master `17db032b…` and Page Specs `d4574804…`
are unchanged. Addendum in `audit/FINAL_CLEAN_ROOM_ACCEPTANCE.md`.
- **OWN-07 closed.** `/remittances/` binds MA-001 but its presentation contract allowed zero Measurement cards; the limit
  is now 1, and the card renders in both languages with its household-receipt scope (receipt, channel, frequency), kept
  apart from the macro remittance evidence on the page.
- **OWN-08 closed.** `navigation_interaction.json` now matches the governed copy, the Page Specs and the tested
  behaviour: Report an issue opens Contact (`?record=`) with its `UI-*` label; a Reading's breadcrumb ends on its title;
  Compare names its six dimensions, four assessments, the same-record state and the outside-set error; the workbench and
  Compare take only public records and the governed comparable set (Evidence Passports are never rendered); the sparse
  state is `/evidence/CLM-004/`; the institutional and vintage states are stated as the pages show them; J10 runs record
  → Contact → Corrections.
- **Controlled contracts named.** The two hand-maintained contracts form their own manifest class, `CONTROLLED_CONTRACT`,
  with a maintenance rule in the file, in `AGENTS.md` rule 2 and in `CONTRIBUTING.md` §2: the steward changes them in a
  commit naming the finding; Design and Code escalate.
- **Handoff tightened in place** (one start file, one brief). D1 tests two or three materially different design theses
  on Home, `/evidence/CLM-003/` and the flagship Reading `/readings/same-year-different-number/`, in both languages,
  before anything is propagated; a decision log and a coverage ledger (`design/COVERAGE.csv`) are kept at every gate; D0
  records whether a visual board or mockup was actually supplied (nothing absent binds). D7 requires the runnable, fully
  populated bilingual reference site; a design source alone is an incomplete hand-back; `⟦NCC:…⟧` markers are for
  development only and every shipped label must be in the Master, or its feature stays unshipped.
- **Print and portable evidence.** Page and Reading print styles, contextual chart and table exports, provenance that
  survives detachment and a Reading print/PDF layout, in the brief, the acceptance criteria and the Design-to-Code
  contract; every CauseWay-content download or export ships disabled until the licence decision (OWN-04); reporting
  stays the static Contact route (no backend, address, SLA or form).
- **Fonts.** The loading wording now matches `vendor/fonts/README.md`: self-host the files as shipped, load efficiently,
  IBM's own pre-split subsets only through the steward, no self-made subset without the owner.
- **Records.** Register 47 items (OWNER_INPUT 6), zero DESIGN_BLOCKER; the checkpoint states that the external
  repository is deliberately untouched lineage (no sync owed) and why F9 reported 753 files and the delivered archive 754;
  README rewritten around the current state and the owner actions.

## 2026-09-26 — F9: DESIGN HANDOFF READY

Record `audit/FINAL_CLEAN_ROOM_ACCEPTANCE.md`. R8.6 is closed and directive D7 is complete. Three cold recipients found
no blocker; the archive, extracted into an empty directory, passes every gate; the register holds 49 items with zero
DESIGN_BLOCKER. The start file, the Design brief, `README.md`, the checkpoint, the Context and the handoff manifest now
read DESIGN HANDOFF READY (gate R86-G01); the Code prompt still waits for the accepted Design package. Not PUBLIC
RELEASE READY. The owner pushes the signed tag `checkpoint/design-handoff-ready`; the package is
`Yemen_Financial_Inclusion_Evidence_DESIGN_HANDOFF_READY.zip` (`git archive`, one root folder, never committed).

## 2026-09-26 — F9 (part 3): third cold-recipient run

A third fresh agent, on a clone of `b3c8e87`, asked whether it could carry Design from D0 to D7 without a question or an
invention; every command passed and it found no blocker, and 10 material points
(`audit/final_integration/inputs/F9_COLD_RECIPIENT_RUN3.md`). No Master change.
- **Fonts in the repository.** `vendor/fonts/`: the unchanged woff2 files and OFL licence of `@ibm/plex-sans@1.1.0` and
  `@ibm/plex-sans-arabic@1.1.0`, with provenance and the Reserved-Font-Name rule; class `VENDORED_FONTS`.
- **Visual contracts.** The POS charts' DISAGREEMENT note now comes from their own bilingual Evidence Records, not from a
  non-public passport.
- **Inventory 1.3.** Role STRUCTURE for the English-only relationships file; every question's destination (QE-001 lands
  on Home at `#system`).
- **Brief.** The Home evidence snapshot is Home section 3 as authored; governed text the baseline renders elsewhere
  (question-list introductions, the Reading thesis); the workbench keeps the embedded site search; every bound visual on a
  domain page has a place; chart-table and matrix headings and the matrix's English-only dated cells are pre-registered
  requests; full status and alert roles in the hook contract.
- **Register.** §7 restated precisely; three more items closed.

## 2026-09-26 — F9 (part 2): second cold-recipient run

A second fresh agent, on a clone of `3adf224`, passed every command, verified `YFIE_SITE_DIR` by planting defects, and
could start D0; it asked six questions and reported 9 material and 14 editorial points
(`audit/final_integration/inputs/F9_COLD_RECIPIENT_RUN2.md`). No Master change.
- **Page Specs.** The editorial rule now says governed wording is rendered exactly as authored; only the programme
  compresses it, Master-first (controlled input `page_spec_templates.json`).
- **Visual contracts.** A comparability flag no longer renders as an ungoverned UNKNOWN marker on two withheld values.
- **Inventory 1.2.** Home's starting questions and Explore's clusters, section counts per `section_order` with a flag for
  per-language rows, each domain route's verify destination in its next actions, and the visuals, grammar tokens and
  Readings at every hard-state route.
- **Brief, criteria, guides.** Where a visual lives (a `VIS-` record page is its canonical route); TABLE_TEXT_FIRST without
  rows; WITHHELD precedence; the full test-hook contract (suites are never edited by Design); the workbench without
  ungoverned facets; the vintage-conflict case; Reading labels quoted exactly; the domain Measurement rule; the Reading
  compare rule; Page Spec section structure; navigation labels' source; three more contract disagreements.
- **Tools.** In an archive without `.git`, the file walk honours `.gitignore`; the tools suite names the site directory
  it could not find; the architecture diagrams no longer name an external design tool or an analytics opt-in.
- **Register.** 49 items (EAD-11 added; EXT-10 and OWN-08 widened); seven items closed in F9.

## 2026-09-26 — F9 (part 1): clean-room corrections

A cold recipient (a fresh agent with only a clone of `main`) followed `handoff/README_FIRST.md`, passed every command and
could start D0 without asking; it reported 15 material and 10 editorial points where Design would have had to guess.
Record: `audit/FINAL_CLEAN_ROOM_ACCEPTANCE.md` (written at the close of F9).
- **Master (RF9).** The two language-switch labels still held in `scripts/build.py` moved unchanged into the governed
  interface copy (`UI-LANG-SWITCH-NAME`, `UI-LANG-SWITCH-ACTION`); the rendered site is byte-identical.
- **Inventory 1.1.** Collections of the index routes (comparable records, displayed and curated sources, chronology,
  Readings, Measurement, questions), each route's next actions, each Reading's bindings, the verification state each
  Evidence Record renders, the facts at every hard-state route, the presentation limit per domain route, and the role of
  every projection file (render, via Page Spec, contract, reference only). The runner now rewrites it after every build.
- **Visual grammar.** WITHHELD has a governed drawing rule; the narrow widths are 320 and 390 CSS px everywhere.
- **Brief and criteria.** Precedence Master → projections → the two hand-maintained contracts → baseline, with the five
  known contract disagreements and what to design to; the reference implementation builds to `design/reference/out/` and
  is tested with `YFIE_SITE_DIR`; the test hooks listed; Compare's governed dimensions, assessments and comparable set; the
  report path; the IBM Plex rule and packages; the date form; SUPPORTING visuals plot no values; named stress cases;
  labels Design is expected to request, with a placeholder convention; delivery without push access.
- **Tools.** The three suites take `YFIE_SITE_DIR`; the invariance check fails on an empty site directory; the repository
  manifest and the validator's file scan work from an extracted archive without `.git`.
- **Register.** 48 items (OWN-08 added for the navigation contract's stale fields); three items closed.

## 2026-09-26 — F8: R8.6 Design handoff freeze

Record `audit/R8_6_DESIGN_HANDOFF_FREEZE_CLOSURE.md`; no Master change. State: **R8.6 FREEZE CANDIDATE — PENDING FINAL
CLEAN-ROOM ACCEPTANCE**.
- **One start path.** `handoff/README_FIRST.md` → `handoff/CLAUDE_DESIGN_MASTER_PROMPT.md` (rewritten from the current
  repository; the 22 D7 requirements; gates D0–D7; deliverables `design/00`–`10`). The Code prompt waits for the accepted
  Design package. Three superseded drafts retired to `audit/prior-review-records/handoff-drafts-2026-09-26/`.
- **New handoff files.** `DESIGN_ACCEPTANCE_CRITERIA.md` (A–J), `ENGINEERING_HANDOFF_EXPECTATIONS.md`, and
  `ROUTE_CONTENT_AND_STATE_INVENTORY.json` generated by `scripts/handoff_inventory.py` (143 routes, 12 hard-state cases,
  14 technical states, 13 journeys).
- **Open items.** `FINAL_OPEN_ITEMS_REGISTER.md`: 47 items in six classes, zero DESIGN_BLOCKER, built from a sweep of every
  earlier open item against the current bytes; README and checkpoint now point to it.
- **Pre-freeze corrections.** Stale "partial lineage" rationale on VIS-PAYMENT-RAILS corrected in the controlled visual
  contract input; the Design prompt names the governed source-type field and forbids CSS recolouring of the logo.
- **Discovery.** Open Graph and Twitter summary metadata from governed titles and descriptions (no image).
- **Gates added:** R86-G01…G04 (one recipient-start state everywhere; inventory current; exact handoff file set; every
  path a handoff document names exists). `design/**` is classified `DESIGN_PACKAGE`.

## 2026-09-26 — F7: sustainability baseline and stewardship note

No Master change.
- **Baseline.** `audit/SUSTAINABILITY_PRE_DESIGN_BASELINE.json`, measured with `audit/final_integration/f7_measure_baseline.py`
  (headless Chromium, local static server, 12 route classes × 2 languages, cold and warm, plus the Search interaction).
  The master logo (10 MB PNG, never redrawn here) is 96–99 % of every cold page; without it a page is 0.09–0.45 MB in
  four requests; warm loads transfer nothing; the search index (about 2 MB) loads only when Search is opened.
- **Method.** `docs/SUSTAINABILITY_METHOD.md`: what is measured, the system boundary, what is deliberately not done (no
  carbon figure, budget, badge or comparison before Design) and when to remeasure.
- **Stewardship.** `handoff/SUPPORT_AND_PARTNERSHIP_READINESS.md` (not public, not a Design input): public-good proposition,
  editorial-independence covenant, conflict rules, cost categories, use and impact framework, partnership menu, rights
  boundary and a DPG gap assessment (not eligible today; nothing claimed).

## 2026-09-26 — F6: discovery, accessibility, rights, security and privacy (pre-Design)

Record `audit/F6_DISCOVERY_ACCESSIBILITY_RIGHTS_SECURITY_ACCEPTANCE.md`; no Master change.
- **Discovery.** `scripts/discovery.py` (one implementation for build and validator): self-canonical, reciprocal hreflang
  with `x-default` (the root entry route), `robots.txt` (pre-release: no crawling), sitemap derivation for when the owner
  sets `public_origin` in `site-src/deployment.json`, JSON-LD (`WebSite`, `BreadcrumbList`, `Article` for Readings) with
  governed fields only — no author, dates, image or `Dataset`. 404 is `noindex`.
- **Strict CSP possible.** Page data moved from inline scripts to JSON blocks; the root redirect is `assets/lang-redirect.js`;
  no inline style, handler, external resource or form. Header expectations for Code in `docs/DEPLOYMENT.md`.
- **Accessibility contract.** Eleven WCAG 2.2 outcomes with what the reference build does now and what Design and Code
  must deliver; no conformance claimed.
- **Gates added:** F6-G01…G08 (titles, descriptions, H1, lang; canonical and hreflang; robots and sitemap; structured
  data; public-build security; secrets; bundled documents; rights and card state).

## 2026-09-26 — F5: whole public corpus acceptance

Transactions RF5 and RF5b (Master `440614d7…` → `168a0ad8…` → `ed3c5796…`); record
`audit/F5_PUBLIC_CORPUS_ACCEPTANCE.md`; every finding and decision in `audit/F5_CORPUS_FINDINGS_LEDGER.csv`.
- **Review.** Eleven reviewers read every governed public text (pages, Evidence Records, visuals, questions, Measurement,
  chronology, sources, interface labels, Readings) as Arabic, as English and for parity: 667 findings, all 57 material
  applied; 34 applied with Lead wording, 26 rejected under two house rulings, 3 deferred as open evidence checks.
- **Corrections.** Arabic scope qualifiers restored (CBY-Aden reporting scope, FPS areas, OECD/INFE representativeness,
  SFD provider universe); firewall errors fixed (full go-live, not located ≠ non-existent, ownership ≠ access, responses
  ≠ firms, exposure ≠ use); three unsupported periods corrected from the records' own sources; control language
  ("held", "locator", "universe", "vintage", "content version") removed; house terms applied.
- **Structure.** Chronology in date order (YSC-018); duplicate source record `SRC-WB-RPW-KSA-YEM-2025Q3` retired (source
  records 160, public locators 151, search records 435); citation line reads "Edition of 26 September 2026".
- **Tooling.** `run_stage.py` rewrites the repository manifest before validating; the public stylesheet no longer names
  the design tool.

## 2026-09-26 — F4: R8.5 canonical repository subtraction

Transactions R85-A and R85-B (Master `69899ae2…` → `2a7fd52b…` → `440614d7…`); closure
`audit/R8_5_REPOSITORY_SUBTRACTION_CLOSURE.md`, 21-item ledger `audit/R8_5_SUBTRACTION_LEDGER.csv`.
- **Copy out of code.** 195 bilingual labels moved from `build.py`/`app.js` into the Master's governed interface copy
  (wording unchanged; 288 HTML identical apart from a JSON label block for `app.js`); Arabic Measurement domain labels
  moved to 10 `domain_ar`.
- **Copy corrections.** 404, corrections, answer-page disclosure, source-trace, data-directory and Compare wording
  rewritten without control language; the FMIIP crosswalk title no longer says "compared with".
- **Debt.** Duplicate reform events REF-PAY-010/007 merged into 006/013; `(1)` audit files resolved; P3-D02 labels
  fixed; Resource Library categories 16 → 6; Unicode NFC throughout the Master (32 cells).
- **Repository.** `FINAL_REPOSITORY_MANIFEST.json` classifies every tracked file (`scripts/repository_manifest.py`);
  `audit/INDEX.md` separates current records, standing policies and history; `docs/DEPLOYMENT.md` rewritten.
- **Gates added:** R85-G01…G09 (copy ownership, placeholder parity, NFC, authoring tokens, internal codes, private
  locators, Latin months on Arabic pages, manifest and index).

## 2026-09-26 — F3: five bounded Resource Library decisions

Transactions RL-F3 and RL-F3b (Master `caabff47…` → `69899ae2…`); record `audit/F3_RESOURCE_DECISIONS.md`.
- **Included (curated resource):** the September 2026 FinDev Gateway paper on supervising Yemen's microfinance banks
  (authors from Al-Amal Microfinance Bank; provenance and boundary stated on the card; no figures, no evidence binding).
- **Deferred:** IFAD *Sending Money Home 2026* (no verified Yemen figure; reopen only for a documented Yemen estimate, as a
  secondary lineage) and the World Bank Joint Food Security Monitor — Yemen (verified version 3 August 2026; its
  exchange-rate series need a governed record before any use beside nominal rial values).
- **Rejected:** the CPMI-IOSCO FMI cyber-resilience toolkit (consultative global guidance; no Reading or priority depends
  on it) and the Uzbekistan financial-inclusion index method (a composite index conflicts with the product's first principle).
- Counts: curated cards 28, source records 161 (152 with a public original locator), search records 436.

## 2026-09-26 — F2: Evidence Readings portfolio integrated (directive D7, sessions F0–F2)

OpenAI accepted the Tranche C checkpoint (recipient verification 31/31) and supplied the independent ten-Reading package.
F0 confirmed the verified entry state without re-running the handover programme. F1 adjudicated the package against the
Master and sources (`audit/READING_PORTFOLIO_FINAL_ADJUDICATION.md`, 60-row `audit/READING_PORTFOLIO_CHANGE_LEDGER.csv`).
F2 applied it in one Master-first transaction, RP-F2 (Master `f0150122…` → `caabff47…`; 494 cell writes and row deletions;
run report `audit/reading_integration/runs/RP-F2_RUN_REPORT.json`).
- **Readings.** Ten essays with new titles, standfirsts and bodies (4–7 sections each, the opening may run on without a
  heading), each ending "What would change this reading? / ما الذي قد يغيّر هذه القراءة؟", then the evidence path
  ("Trace the evidence / تتبّع الأدلة") and one or two related Readings. One signature visual per Reading. CWR-006's title
  changed to "What exactly do we mean by microfinance growth?" (the asserted growth failed the detached-quotation test).
- **Master structure.** 08 retires `domain_context_routes` (now `related_readings`) and adds `measurement_bindings`,
  `evidence_period_en/ar`, `last_reviewed` and `featured`; the generator checks every relation once
  (`derived.reading_relations`). A Reading's primary question now comes from 08, not from a shadow copy in the design-intent input.
- **Propagation.** Readings index (programme-owner definition, one featured Reading, editorial list — no card wall); Home
  featured Reading; Explore "Go deeper"; at most two Readings per answer page; Evidence Records "Used in these Evidence
  Readings"; Measurement Agenda "This gap is examined in"; search, meta and page specs regenerated; twelve new governed labels (04).
- **BIL-05 closed.** Every English/Arabic page pair prints the same numbers (6 held pairs → 0). The CI step no longer
  carries a held list; `audit/tranche_c/checks/bilingual_invariance.py` exits 1 on any difference.
- **Permanent gates RP-G01…G06** (validator): Reading ending and page order, one visual and no numbered template, one
  featured Reading everywhere, at most two Readings per answer page and "Used in" on bound records, retired Reading copy
  never reappears, bilingual invariance.
- **Gates.** Generator check and 21/21 tests; build 288 HTML from 143 Page Specs; literal audit 12,741 / 0 unresolved and
  deterministic under eight seeds; lineage 8/8; diagrams current; validator PASS 0/0; public tools 25/26 (1 n/a);
  viewport 168/168.
- **Status:** READING PORTFOLIO INTEGRATED — TRANCHE C ACCEPTANCE PRESERVED. Not DESIGN HANDOFF READY; not PUBLIC RELEASE READY.

## 2026-09-26 — Canonical Git repository

The repository moved from a Drive folder and ZIP checkpoints to Git on GitHub (`CausewayGrp/Financial-inclusion-`,
branch `main`). No governed content changed: the Master, the projections and the public site are identical to the
Tranche C checkpoint, and no existing audit record was modified.
- **Baseline.** The first content commit is the exact tree of the ZIP under OpenAI review (SHA-256 `63612dea…`), tagged
  `checkpoint/tranche-c-complete-reading-hold` (signed); `sha256sum -c SHA256SUMS.txt` passes on the tagged tree.
- **CI.** `.github/workflows/verify.yml` runs every gate on each push to `main` and each pull request, including two new
  drift checks: the checksum manifest must list every tracked file, and the committed `dist/` and literal closure must
  equal a fresh build. `.github/workflows/checkpoint.yml` packages each signed `checkpoint/*` tag as a verified ZIP.
- **Owners.** `scripts/checksums.py` now writes and checks `SHA256SUMS.txt`; `requirements.txt` pins the Python 3.11
  toolchain; `.gitattributes` keeps every file byte-exact (CRLF ledgers included).
- **Protocol.** `CONTRIBUTING.md` (change protocol, branches, commit trailers, checkpoints, session sync, known pitfalls,
  repository settings), `AGENTS.md` and `CLAUDE.md` (agent rules). `docs/PRODUCTION_REPOSITORY_PROTOCOL.md` now records
  the move; `authority/AUTHORITY.json` names the canonical repository; the checkpoint names the reviewed tag.
- **Directives.** The programme directives D0–D6 are stored verbatim in `audit/directives/` (D6 current and binding).
- **Carried to R8.6:** the Design and Code prompts in `handoff/` must name the Git repository and the branch and pull-request
  protocol when they are finalised.
- **Status unchanged:** TRANCHE C COMPLETE — READING PROSE HELD FOR THE INDEPENDENT READING PACKAGE. R8.5 and R8.6 not
  started. Not DESIGN HANDOFF READY; not PUBLIC RELEASE READY.

## 2026-09-26 — Tranche C: whole-product adversarial acceptance

Ten Master-first transactions (TC-S1, TC-A…TC-I) through the transactional runner; closure in
`audit/TRANCHE_C_FINAL_ACCEPTANCE.md`, ledger in `audit/TRANCHE_C_FINDINGS_LEDGER.csv`, currentness cut-off (26 September
2026) in `audit/FINAL_CURRENTNESS_CUTOFF.md`.
- **Panel.** 224 findings from nine lenses plus 5 from the bilingual-invariance test; all 9 BLOCKERs closed; 212 FIX,
  8 NARROW, 2 evidence frontiers, 3 release-only dependencies, 3 scheduled for R8.5, 1 held for the Reading package.
- **Bilingual parity.** 28 page-section pairs re-authored to the accepted content (TC-H); chronology dates now render in
  the page language (TC-I); the Arabic /payments/ title now gives the answer.
- **New checks.** `audit/tranche_c/checks/viewport_acceptance.py` (168/168) and `bilingual_invariance.py`.
- **Status:** TRANCHE C COMPLETE — READING PROSE HELD FOR THE INDEPENDENT READING PACKAGE. R8.5 and R8.6 not started.
  Not DESIGN HANDOFF READY; not PUBLIC RELEASE READY.

## 2026-09-26 — Pre-Tranche-C P5: independent-acceptance corrections

The P1–P4 hand-back was independently accepted with three narrow corrections, all closed
(`audit/P5_INDEPENDENT_ACCEPTANCE_CORRECTIONS.md`):
- **P5.1, deterministic literal audit.** Reading-bound records are taken in governed binding order with ordered
  de-duplication; a regression test runs the audit under eight `PYTHONHASHSEED` values and requires identical bytes.
- **P5.2, REF-PAY-001.** New source record `SRC-CBY-DEC-23-2024-001` for CBY Governor's Decision No. 23 of 2024 on
  domestic money-transfer activity. VIS-PAYMENT-RAILS is bound to it and the RV-CWR-009 release blocker is removed. The
  record is a rule, not evidence of implementation, use or outcome.
- **P5.3, RV-CWR-001 panel 2.** The CBY Annual Report 2025 remittance values for 2021–2023 were added Master-first as
  their own publication vintage. The panel shows the CBY and IMF paths indexed to 2021 = 100 as two separate lanes, with a
  generator guard, and is no longer blocked on data.
- **Controls.** The transactional runner now also snapshots and restores the checkpoint and the architecture diagrams,
  and checks the diagrams. A current-state source-lineage truth test was added. The acceptance matrix now also runs the
  seed-determinism test, the lineage truth test and the diagram check.
- **Status:** PRE-TRANCHE-C ACCEPTED — READY FOR TRANCHE C. Tranche C not started. Not DESIGN HANDOFF READY; not PUBLIC
  RELEASE READY.

## 2026-09-26 — Tranche B execution and Pre-Tranche-C maturation (P1–P4)

- **Tranche B.** The Master-first patch specification was executed in five transactional stages (`audit/TRANCHE_B_EXECUTION_CLOSURE.md`).
- **P1, public truth and editorial integrity** (`audit/P1_PUBLIC_TRUTH_EDITORIAL_CLOSURE.md`):
  - inventory counts are now derived;
  - duplication was removed;
  - a public-identifier policy was set;
  - Reading verification paths were added;
  - held additions were disposed;
  - chronology assurance was completed.
- **P2, tools and discovery** (`audit/P2_TOOL_DISCOVERY_CLOSURE.md`):
  - Compare has URL state;
  - governed search aliases and a canonical probe (60/60) were added;
  - the tool contract sweep was completed;
  - an accessibility baseline was set (no conformance claim);
  - 26 browser behaviour tests were added.
- **P3, visual design readiness** (`audit/P3_VISUAL_DESIGN_READINESS.md`):
  - all 36 visual contracts are tiered;
  - a semantic visual grammar was defined, with 33 governed labels;
  - data contracts exist for the SIGNATURE and CORE visuals;
  - contract truth corrections were made Master-first.
- **P4, canonical handoff alignment** (`audit/P4_CANONICAL_HANDOFF_ALIGNMENT.md`):
  - one current-state story;
  - one Reading truth: the Reading index holds no copy, and the generator stops if text is written into it;
  - a bilingual boundary structure (does not establish | limits of the measure);
  - design-prompt drift corrected, with the prompt still DRAFT;
  - hygiene;
  - two independent verification rounds resolved Master-first:
    - the publication firewall now covers producer names, withheld values and shipped payloads;
    - 109 governed bilingual chart labels and in-frame lines;
    - text-first visuals no longer describe drawings;
    - Arabic terminology and grammar corrections;
    - architecture diagrams derived from the navigation contract.
- **Status:** PRE-TRANCHE-C MATURATION COMPLETE — READY FOR INDEPENDENT ACCEPTANCE. Not DESIGN HANDOFF READY; not PUBLIC RELEASE READY.

## 2026-09-23 — S06 recipient acceptance + deterministic handoff freeze

- Closed S06.3 and completed independent recipient-side S06 acceptance: **S06_WINDOW_ACCEPTED**.
- Detected a newer live Production Master revision during acceptance and treated it as a concurrency event rather than restoring an older hash.
- Source-owner adjudication retained the newer `21_MFI_DATA` treatment for SFD Q4-2011: end-Dec-2011 narrative (~64,000 borrowers; 87,000 savers; YER 4,030m portfolio) versus a table headed end-Dec-2010 (63,568; 87,615; YER 3,853m). The portfolio/time-series point is now a preserved conflict, not a clean 2011 anchor.
- Regenerated the affected MFI local shard and rebound all 141 Page Specs to current Master SHA-256 `f94f1f91084b01964a3bb7b3847fd68a19555cc901ab6078146a187efe17e860`. New Page Specs SHA-256 `4e8a0d8f0cf58f78389360c69cf04f3bf0d24f1ba9b3e4ef10ebe93461e69f1a`; no public 2011 microfinance claim/copy changed.
- Reconciled stale S06 aggregate fields in the existing control stack and updated validator expectations to the accepted S06 boundary.
- Strengthened and froze the existing `handoff/` only; no parallel final package was created. Claude Design remains first recipient; Claude Code starts after a repository-backed design package exists.
- S07/S08 remain not started. `R-042`, remote webfonts and final named assistive-technology/deployed-runtime acceptance remain later release gates.

All material repository edits are recorded here. Evidence semantics are not changed directly in the website repository; any such change must originate in the Production Master and be regenerated.

## 2026-09-23 — Deterministic Claude Design → Claude Code handoff

- Added `handoff/` as a **non-authoritative** implementation handoff layer. The Production Master remains the sole semantic/evidence/source/rights/publication authority; Page Specs remain its controlled implementation projection.
- Added eight raw repository files: handoff entry/read order, Claude Design master prompt, design starting tokens, design-to-code contract, Claude Code master prompt, static-runtime/API contract, implementation manifest and acceptance checklist.
- Bound the handoff manifest to the live Production Master SHA-256 `d3b0421104d63f830cf40d2b1749dc88f302f54e4d79a6c6faf63abc5ad28d9e` and Page Specs SHA-256 `453bde9026c2a30f2c0c2125c0e950cd6e468a9540577318e1896c98e61959da`.
- Specified Claude Design as the first recipient and Claude Code as the implementation recipient after a repository-backed `design/` package exists; screenshots/chat history are not implementation authority.
- Defined one React static pre-render/export target with the accepted 141-route × 2-language + root + 404 = 284-document baseline and no required runtime Drive/database/CMS/API dependency.
- Identified one implementation gap in the current baseline: `styles.css` imports webfonts remotely. The final code handoff requires packaging approved fonts locally before the static runtime can be called fully local.
- First-hand local reconstruction found one checksum-control drift: `docs/POST_BUILD_REVIEW_PROGRAM.md` had been modified after the prior `SHA256SUMS.txt`. The manifest is refreshed only after the complete handoff/control integration so one coherent checksum state is written.
- Final staged reconstruction after handoff/control integration: Python syntax PASS; JavaScript syntax PASS; 284 HTML built from 141 Page Specs; validator `ERRORS=0`, `WARN=0`; checksum coverage expanded to 78 canonical files.
- No evidence value, claim, source state, rights state, publication state or controlled public wording was changed by this handoff work. S06.1 remains not started.

## 2026-09-22 — S00/S01 opening integration

| Area | Edit | Why it changed | Authority impact | Verification |
|---|---|---|---|---|
| Repository control | Added `POST_BUILD_REVIEW_PROGRAM.md`, `REVIEW_LEDGER.json` and this log. | Make the post-build work finite, inspectable and repository-local. | None. | Files present; included in checksums. |
| Authority documentation | Corrected repository metadata so it no longer claims the Production Master workbook is bundled when the repository only carries its hash and frozen projections. | Previous metadata contradicted the actual ZIP contents. | None; Master authority strengthened. | Repository file inventory checked. |
| Handoff state | Replaced stale “design/implementation not started” state with actual static-first implementation state and remaining acceptance boundary. | The prior handoff state was inherited from an earlier package and no longer described this repository. | None. | Metadata compared with generated `dist/`. |
| Mobile navigation | Corrected the small-screen CSS/interaction conflict that hid the mobile menu button at ≤640px; added explicit open/close state and `aria-expanded`. | At phone width the nav was hidden and the control that should reopen it was also hidden. | None. | Static CSS/JS review + validator assertions. |
| Global search | Added an accessible global search dialog available from every page while retaining the Evidence-hub search. | Search was described as a global utility but the header button only routed to the Evidence page. | None; public search index remains the only search payload. | Search controls and public-index checks added. |
| Governed object rendering | De-duplicated governed objects by stable ID; correctly reads public `summary_*` and `limitations_*` fields; suppresses empty evidence cards; adds “Open evidence record” links when a controlled detail route exists. | The generator was dumping overlapping reference arrays, producing duplicate IDs and many empty public cards despite the Page Spec rule that governed arrays are reference payloads, not blocks to dump verbatim. | None; render-only correction. | Post-build HTML density/duplicate/empty-card audit. |
| Compare UX | Added localized comparison field labels and horizontal scroll containment for narrow screens. | Improve comprehension and mobile usability without changing comparison semantics. | None. | Static generation and route smoke checks. |
| Focus/touch behavior | Added visible `:focus-visible`, 44px control minimums and accessible dialog behavior. | Keyboard/mobile usability baseline. | None. | Validator + manual DOM/CSS review. |

## 2026-09-22 — Canonical Drive folder conversion

- Established a single non-ZIP Google Drive production repository and a separate non-production reference/archive inbox.
- Added `docs/PRODUCTION_REPOSITORY_PROTOCOL.md` to define production authority, editing, handover and release rules.
- Consolidated the 141 Page Render Specifications into `site-src/content/page_specs.json` to keep the Drive repository first-hand, clean and practical for other developers/AIs while preserving all controlled specifications.
- Updated build and validation scripts to consume the consolidated Page Specs deterministically.
- Rebuilt the site and re-ran validation: 284 HTML files generated; `ERRORS=0`, `WARN=0`.
- ZIP handoff files moved out of the production root into the sibling non-production archive; ZIPs are no longer the working repository.

## 2026-09-22 — S01 deep review and reference challenge

| Area | Edit | Why it changed | Authority impact | Verification |
|---|---|---|---|---|
| Drive structure | Moved production and reference folders out of the superseded archive path so both now sit directly under `My Drive / Ready`. | The active repository should not live beneath a folder named superseded. | None. | Drive parent IDs checked after move. |
| Source journey | Added a bilingual Data source directory and query-aware focus for `/data/?source=<ID>`. | Global search previously resolved source results without taking the user to the named source. | None; uses only current `source_reference_map.json`. | 148 public-addressable source records rendered per locale from a 149-record controlled map; the one no-public-locator dependency is suppressed; every source search result maps to an existing source anchor. |
| Source metadata firewall | Full cards are limited to the 6 controlled display-ready sources; 142 locator-only entries with a public URL expose only stable source ID and original locator; the one controlled dependency without a public locator is suppressed. | Prevent bibliography/publisher/licence invention for locator-only records. | None; render policy tightened. | Validator blocks internal source-state leakage and checks source anchors. |
| Search UX | Added localized result-type labels, live loading/result/error status and focus return on dialog close. | Improve first-use comprehension and keyboard behavior. | None. | JS syntax + validator assertions. |
| Search result quality | De-duplicated identical title+route results before the top-ten limit, preferring the substantive non-page record when the index contains both a Page Spec and its evidence object. | The controlled index legitimately contains multiple object types, but the UI should not show the same public destination twice. | None; index remains unchanged. | Deterministic search stress test documented in `S01_TASK_STRESS_TEST.md`. |
| Navigation semantics | Added `aria-current="page"`, Escape-to-close and resize reset for mobile navigation. | Improve assistive-technology and keyboard navigation state. | None. | Validator checks active top-level nav; JS syntax PASS. |
| Error recovery | Replaced the minimal English-only 404 with a calm bilingual recovery page linking Home, Explore and Evidence and exposing search. | Avoid dead ends from stale/shared links. | None. | Validator checks bilingual 404 recovery controls. |
| Arabic public language | Replaced the homepage phrase `ساعات أدلة مختلفة` with `اختلاف توقيت القياس`. | Use natural public Arabic rather than backend/evidence-management jargon. | None; wording preserves meaning. | Generated Home inspected. |
| Reference archive | Added `S01_REFERENCE_CHALLENGE.md`; inventoried new archive additions and adjudicated high-leverage drafts by cohort. | Use old work objectively without allowing recency/version labels to become authority. | None. | Material dispositions and authority collision logged. |
| Authority collision control | Quarantined the archive workbook named `...Master_FINAL.xlsx` after its hash (`91ed...`) did not match the production authority hash (`d8db...`). | A “FINAL” filename must not override the controlled Master identity. | None; production authority protected. | SHA-256 comparison recorded in review ledger. |

- Added `docs/S01_TASK_STRESS_TEST.md` to record first-use search/navigation/source-completion tests and the limits of static acceptance.

- **Generated-output tracking:** `dist/` remains reproducible deployment output and is not a canonical tracked source in Drive. `npm run verify` regenerates it from first-hand inputs; repository checksums cover tracked source/control inputs only.

## 2026-09-22 — S01 final reconciliation and closure

- Re-opened the latest live Drive source files before writing so the S01 closure did not overwrite newer repository work.
- Added the missing first-hand controls `docs/S01_REFERENCE_CHALLENGE.md` and `docs/S01_TASK_STRESS_TEST.md`; the validator had already named them, so their absence was a repository-truth defect.
- Completed objective disposition of the newly populated `99_REFERENCE_ARCHIVE_INBOX__NON_PRODUCTION`: implementation-safe lessons integrated; stale route/runtime/design authority rejected; factual/source/rights candidates quarantined for Master-led review.
- Preserved the current 149-record controlled source-map model and 148 publicly addressable source records rather than replacing it with a parallel source payload.
- Strengthened Arabic search normalization, stable-ID search weighting, keyboard search access, and mobile-menu dismissal behavior.
- Replaced the public English phrase `Different evidence clocks` with `Different measurement dates`; retained the approved Arabic `اختلاف توقيت القياس`.
- Added validator regression checks for prohibited backend Arabic wording and ZIP-as-working-repository language.
- S01 remains an implementation/first-use milestone, not a live-release certification.
- Removed the stale Drive `dist/` tree from canonical storage. `dist/` is deterministic generated output and must be rebuilt from first-hand source with `npm run verify`; this prevents source/build drift inside the Drive repository.

## 2026-09-22 — S01 archive refresh and control cleanup

- Re-inventoried archive additions uploaded after the initial S01 pass, including two authoritative-looking workbooks, the critical evidence review, corpus inventory, evidence-synthesis delta, citizen-journey prototype, universal/master build prompts and predecessor frontend/system-architecture specifications.
- Hashed both archive workbooks and confirmed neither matches the controlled Production Master; recorded the collision in `REVIEW_LEDGER.json` and `S01_REFERENCE_CHALLENGE.md`.
- Explicitly quarantined new factual/literature propositions for S06 rather than changing production semantics from the archive.
- Retained useful challenge principles (question-first hierarchy, screenshot-safe scope, negative-search discipline, source no-invention) without importing predecessor factual claims or architecture.
- Removed the redundant `REFERENCE_ARCHIVE_REVIEW_S01.md` control and consolidated the archive review into the single authoritative S01 review document `S01_REFERENCE_CHALLENGE.md`.
- Rewrote `S00_S01_REVIEW_REPORT.md` to remove stale source-index/deep-link statements and align counts with the current controlled source-map implementation.
- Restored and tightened `PRODUCTION_REPOSITORY_PROTOCOL.md` in the first-hand source tree; generated `dist/` remains noncanonical and reproducible with `npm run verify`.
- Updated `FINAL_RELEASE_VERIFICATION.md` so it no longer implies that S01 equals a final live-release decision.

## 2026-09-22 — S01 exhaustive archive disposition and single-source closure

- Completed a point-in-time review of all **70** current top-level items in `99_REFERENCE_ARCHIVE_INBOX__NON_PRODUCTION`.
- Added `S01_ARCHIVE_DISPOSITION_REGISTER.json` so every archive item has an explicit non-production disposition and rationale.
- Added `S06_ARCHIVE_EVIDENCE_CHALLENGE_QUEUE.md` to isolate potentially valuable factual/source propositions from implementation work; all entries remain candidate-only until original-source and Production Master adjudication.
- Inspected `evidence.zip`: 330 entries, CRC clean; classified as generated predecessor output rather than source.
- Verified the archived CauseWay logo is byte-identical to the production asset; no asset change required.
- Explicitly rejected synthetic econometric/model payloads, obsolete route manifests, blanket-rights assumptions and old implementation PASS manifests as production inputs.
- Strengthened the validator so the S01 archive register/queue are required and public HTML fails on broader legacy architecture/vendor leakage (`YFSI`, `BAYAN`, old framework terms).
- Logged the remaining Drive cleanup defect: generated `dist/` must be removed from canonical Drive storage after first-hand source synchronization.

## 2026-09-22 — S01 Drive canonical-state verification

- Deleted the stale generated `dist/` folder from the Google Drive production repository; the canonical Drive root now contains only `README.md`, `package.json`, `SHA256SUMS.txt`, `docs/`, `scripts/` and `site-src/`.
- Removed duplicate Drive copies of the S01/S06 control set (`S01_REFERENCE_CHALLENGE.md`, `S01_TASK_STRESS_TEST.md`, `S01_ARCHIVE_DISPOSITION_REGISTER.json`, `S06_ARCHIVE_EVIDENCE_CHALLENGE_QUEUE.md`), leaving one canonical instance of each.
- Re-listed the reference archive after reconciliation and confirmed the S01 point-in-time baseline remains **70 top-level items** with no unreviewed delta.
- Recorded binary checks for `evidence.zip` (330 entries; CRC PASS), both authority-looking archive workbooks, and the CauseWay logo match.

## 2026-09-22 — S02 audience journeys and information architecture

- Added `docs/PROGRESS_INVENTORY.json` as the single programme-progress and archive-delta monitor.
- Added `docs/S02_AUDIENCE_JOURNEYS_AND_IA.md` with the audience/task tests, IA decisions and counterfactual deletion logic.
- Closed the S01 70-item reference archive baseline: baseline materials are not re-reviewed by default; only new/modified items or a specific defect-triggered challenge are reopened.
- Added a reviewed-baseline marker folder in the non-production archive for point-in-time control.
- Differentiated Home from Explore: Home now orients by five common tasks and four common direct questions; Explore retains all 11 controlled questions grouped by user job.
- Kept the six-item global navigation unchanged; rejected persistent audience-specific menus because they would duplicate routes and increase maintenance.
- Added S02 validator checks so Home cannot silently return to a full duplicate Explore grid and Explore cannot lose any of the 11 controlled entry questions.
- No archive-derived factual claim, source state or rights assumption was promoted into production semantics.

## 2026-09-22 — S02 verification closure

- Rebuilt all 141 controlled Page Specs into 284 generated HTML documents after the IA changes.
- Validation: `ERRORS=0`, `WARN=0`.
- Verified 5 Home task starts + 4 compact questions per language and all 11 Explore questions + 4 groups per language.
- S02 closed; S03 becomes the active review session.
## 2026-09-22 — Bounded-session execution protocol

- Added `docs/SESSION_EXECUTION_PROTOCOL.md` as the single detailed execution control for the remaining post-build programme.
- Split the remaining work into **16 finite sessions**, from S03.1 through S08.2, each with one exact achievement, one owner, no more than two challenger lenses and explicit exit evidence.
- Made end-of-session rationalization mandatory: what became more true, what became simpler/more usable, new complexity introduced, what can be removed/merged, and the smallest next material intervention.
- Added an explicit boundary decision at every session close: PROCEED, REVISE, ESCALATE_TO_MASTER or STOP.
- Reconciled `README.md` and `PROGRESS_INVENTORY.json` so **S03.1 — People + Access composition** is the only next active unit and **S08.2 — Final repository closure** is the programme end.
- No evidence, claim, source, rights or publication-state semantics changed in this control session.

## 2026-09-22 — S03.1 orientation control reconciliation

- Reconciled `docs/HANDOFF_STATE.json` with the already-controlled S02 closure: S00–S02 are complete and S03.1 is the only next active unit.
- Removed the stale `docs/SESSION_EXECUTION_MAP.md` reference from the post-build programme; `docs/SESSION_EXECUTION_PROTOCOL.md` is the single bounded-session control.
- Detected one post-S01 archive delta, the `Old drafts` pointer to the high-fidelity mobile-review mockups; reviewed it once and classified it **DESIGN_REFERENCE_ONLY**.
- Moved that pointer into `04_DESIGN_REFERENCES__REVIEWED`; no archive-derived fact, number, route, source state, rights state or evidence meaning was promoted into production.
- Confirmed `01_NEW_INPUTS__UNREVIEWED` is empty after the delta check.
- No Production Master correction was required by these control repairs.


## 2026-09-22 — S03.1 People + Access composition CLOSED

- Rebuilt `/people/` and `/access/` through an answer-first domain renderer in `scripts/build.py`, with route-specific density rather than mechanical page symmetry.
- Added the restrained S03 domain composition layer in `site-src/styles.css`: strongest-answer hero, adjacent scope/inference boundary, selected evidence/visual, progressive disclosure, Measurement Next and a deliberate Verify surface.
- Reduced the People route from a repeated 33-card evidence wall to three primary analytical sections plus progressive verification depth; preserved direct controlled evidence-record links for `CLM-001`, `CLM-002` and `CLM-025`.
- Made Access's missing national geography an intentional epistemic state: unknown is not zero, rosters/infrastructure are not operating access, and Measurement Next states what evidence would resolve the question.
- Preserved `site-src/content/page_specs.json` as the frozen semantic projection; no Production Master fact, denominator, universe, source, rights or publication state changed.
- Reviewed Arabic 390px/1440px and English 390px/1440px rendered composition; full browser/a11y acceptance remains correctly assigned to later sessions.
- Final S03.1 build: 284 HTML files from 141 controlled page specs. Validator: `HTML=284 ERRORS=0 WARN=0` / `WEBSITE REPOSITORY VALIDATION PASS`.
- Refreshed `SHA256SUMS.txt` for the accepted S03.1 source/control state and removed stale `scripts/__pycache__` checksum entries that did not correspond to files in canonical Drive.
- Boundary decision: **PROCEED** to S03.2.


## 2026-09-22 — S03.2 Firms + Finance composition CLOSED

- Extended the established answer-first domain renderer to `/firms/` and `/finance/` without changing controlled evidence semantics.
- Firms now keeps formal-firm survey scope, governorate coverage, variable-specific denominators and programme KPI/reach boundaries adjacent to the interpretation; programme evidence is not styled as representative firm prevalence.
- Finance now keeps stock/flow, nominal/real, valuation/source-vintage, provider/system-state and inclusion-outcome distinctions visible before deeper historical context.
- Added route-specific controlled visual placement so Firms and Finance share one product grammar without false visual equivalence.
- Arabic 390px/1440px then English 390px/1440px composition inspection found no horizontal overflow and preserved verification paths.
- Reference archive check: **NO NEW ARCHIVE DELTA**. No factual/source/rights proposition was promoted and no Master escalation was required.
- Final S03.2 build: 284 HTML files from 141 controlled page specs. Validator: `HTML=284 ERRORS=0 WARN=0` / `WEBSITE REPOSITORY VALIDATION PASS`.
- Boundary decision: **PROCEED** to S03.3. S03 remains ACTIVE; S03.4 plus the full eight-route closure gate are still required.


## 2026-09-22 — S03.3 Payments + Remittances composition CLOSED

- Extended the answer-first domain renderer to `/payments/` and `/remittances/` without changing the frozen semantic projection.
- Payments now foregrounds administrative-currentness, measurement-object distinctions and the infrastructure/use boundary; terminals, accounts, subscribers and transactions are not rendered as unique people or inclusion outcomes.
- Selected `VIS-PAYMENT-ANATOMY` because the object distinction prevents more misuse than another trend chart; POS contradiction/source-arithmetic evidence remains reachable through controlled verification.
- Remittances now foregrounds observed/estimate/projection state, same-year source revision, BOP/concept boundary and unresolved CBY↔IMF crosswalk; no universal conversion scalar is fabricated.
- Selected `VIS-REMITTANCE-MACRO`; did not invent a Measurement Next card because no governed measurement priority is bound to the current route.
- Arabic 390px/1440px then English 390px/1440px rendering showed no horizontal overflow; representative Arabic mobile and English desktop pages were visually inspected.
- Reference archive check: **NO NEW ARCHIVE DELTA**. No Master escalation.
- Final S03.3 build: 284 HTML files from 141 controlled page specs. Validator: `HTML=284 ERRORS=0 WARN=0` / `WEBSITE REPOSITORY VALIDATION PASS`.
- Boundary decision: **PROCEED** to the Window-1 independent recipient-side acceptance gate. **S03 remains incomplete** until S03.4 and the full eight-route S03 closure test pass.

## 2026-09-22 — Window 1 recipient-side acceptance — ACCEPTED

- Independently re-opened the live canonical implementation for S03.1–S03.3 rather than relying on session reports. Confirmed route configurations and generated composition for `/people/`, `/access/`, `/firms/`, `/finance/`, `/payments/` and `/remittances/` in Arabic and English.
- Rebuilt all 141 controlled Page Specs into 284 HTML documents and re-ran repository validation: `HTML=284 ERRORS=0 WARN=0` / `WEBSITE REPOSITORY VALIDATION PASS`; Python and JavaScript syntax checks also passed.
- Added a compact cumulative S03 regression set to `scripts/validate.py`: six-route answer-first structure, three-item scope/boundary band, selected visual, progressive disclosure, Verify surface, no return to `answer-card` governed-array dumping, AR/EN structural parity, and presence of every localized Page Spec narrative section in the generated route.
- Ran an independent deterministic render harness across 24 route/language/viewport combinations (six routes × Arabic/English × 390px/1440px). No horizontal overflow or structural parity defect was found. This is not a claim of final deployed-browser, assistive-technology, security or privacy acceptance; those remain assigned to later sessions.
- Confirmed the six-route composition retains complete narrative meaning while reducing first-load burden: all Page Spec narrative sections remain present either at first load or in explicit progressive depth; no semantic projection, evidence, source, rights or publication-state field changed.
- Reconciled control drift: `README.md`, `REPOSITORY_BUILD_SUMMARY.json`, `PROGRESS_INVENTORY.json`, `HANDOFF_STATE.json`, `SESSION_EXECUTION_PROTOCOL.md` and `REVIEW_LEDGER.json` now state one current position. R-005/R-006 are explicitly partial rather than falsely closed: the six accepted routes pass; Providers/Reforms remain S03.4 work.
- Confirmed canonical Drive root remains first-hand (`README.md`, `package.json`, `SHA256SUMS.txt`, `docs/`, `scripts/`, `site-src/`) with no stored `dist/`; the reference archive unreviewed inbox remains empty.
- No Production Master escalation was required. Master hash remains `d8db3b4ee7ffbba0ca1cfb2843949a2ee323ac0a8a5396c273ebf4a4cc427fee`.
- Boundary decision: **WINDOW_1_ACCEPTED**. S03.4 is next but **not started**; S03 remains incomplete until Providers + Reforms and the full eight-route closure gate pass.
- Final recipient-side acceptance audit confirmed every localized Page Spec narrative section remains present across all 12 accepted route editions; no generated substantive number was introduced outside the controlled route specification.
- Added validator checks that the core control stack agrees on shared Production Master hash, Page Spec count and generated HTML count, and that `REPOSITORY_BUILD_SUMMARY.json` / `SESSION_EXECUTION_PROTOCOL.md` remain required first-hand controls.
- Final verification after reconciliation: `npm run verify` built 284 HTML files from 141 Page Specs with `ERRORS=0 WARN=0`; Python/JavaScript syntax passed; deterministic render harness passed 24 route/language/viewport combinations with zero horizontal overflow; local HTTP smoke returned 200 for Arabic Home, English People, Arabic Payments, English Data and 404 recovery.
- Final integrity recheck found one stale manifest entry for the live frozen `site-src/content/page_specs.json`: the manifest still carried the predecessor projection hash while the live Drive file and S03 controls consistently resolved to `1319433fed3503cd7ad98203179db5a4a8438906e3e95464b80f36327497b41e`. The live projection was not changed; the checksum manifest was corrected and the finding closed as R-032.
- `SHA256SUMS.txt` was refreshed after control reconciliation; generated `dist/` remains excluded by policy.


## 2026-09-22 — S03.4 Providers + Reforms + full Domain Answer closure — CLOSED

- Rebuilt `/providers/` and `/reforms/` through the established answer-first Domain Answer grammar in Arabic and English.
- Providers now foregrounds authority, dated status and operation uncertainty; the 98 exchange companies, 225 individual exchange establishments and 106 remittance agents remain separate source-defined categories rather than a fabricated deduplicated current operating-provider total.
- Reforms now foregrounds the rule/funding → implementation/institution → operation → access → use → quality/protection → outcome chain and the furthest evidenced state; missing downstream evidence is not rendered as failure.
- Replaced the hard-coded six-route presentation hierarchy with one renderer-consumed `site-src/content/presentation_priority.json` contract covering all eight Domain Answer routes. The contract controls presentation depth only and cannot override Page Specs or the Production Master.
- Extended `scripts/validate.py` to enforce eight-route mapping, governed references, presentation-tier completeness, always-visible boundaries, direct Evidence Record resolution, AR/EN structural parity, narrative retention and renderer/contract binding.
- Counterfactual deletion / visual-economy decision: kept `VIS-PROVIDER-OBSERVABILITY`; added no first-load Reforms visual because the existing controlled visuals would privilege one reform subclass or imply false comparability.
- Arabic mobile review detected and fixed an unlocalized English visual-metadata leak; raw unlocalized English metadata no longer appears as Arabic UI.
- Render inspection covered Providers/Reforms at 390px, 768px and 1440px in Arabic and English. Clean build: 284 HTML documents; validator `ERRORS=0 WARN=0`; Python and JavaScript syntax PASS.
- Reference archive inbox: EMPTY. Master escalation: NONE.
- Boundary decision: **PROCEED** to S04.1. **S03 is CLOSED.**

## 2026-09-22 — S03.4 presentation-contract direct-consumption cleanup

- Removed the temporary derived `DOMAIN_CONFIG` compatibility layer after the eight-route contract migration; `build.py` now consumes `site-src/content/presentation_priority.json` through `PRESENTATION_ROUTES` directly.
- Strengthened `validate.py` to fail if `DOMAIN_CONFIG` reappears and to verify that contract-promoted governed objects are eligible for the route recorded in the controlled Page Spec projection.
- Rebuilt 284 HTML documents from 141 Page Specs and re-ran repository validation: `ERRORS=0`, `WARN=0`, PASS. No semantic/evidence/source/rights/publication change and no Master escalation.


## 2026-09-22 — S04.1 Evidence records + discovery / verification journey — CLOSED

- Replaced generic evidence-detail card rendering with a distinct Evidence Record page family driven by the existing canonical presentation contract. First load now exposes evidence identity, what it establishes, definition, universe, period/currentness, material limitation and source/verification action; method/change-trigger/verification guidance remains progressively available.
- Connected all four required entry paths: Domain → Evidence → Source → interpretation; Global Search → Evidence; direct Evidence deep link; and Data/source → dependent Evidence Record. No stable-ID knowledge is required to navigate the journey.
- Extended the existing Data/source directory only with dependent Evidence Record links; DISPLAY_READY/LOCATOR_ONLY behavior remains bounded and the one no-public-locator dependency remains suppressed.
- Extended `scripts/validate.py` across 108 Evidence Records for contract/renderer binding, governed-object/source resolution, first-load boundary, source-publication filtering, related/backtrack targets, AR/EN parity, search/deep-link resolution and Data/source dependencies.
- Hard-case verification passed across representative population survey, bounded firm survey, programme KPI, administrative payments, provider roster/status, reform/regulatory evidence, remittance observation/estimate/projection states and a derived visual object.
- S04.1 exposed a controlled Arabic public-language defect in CLM-060 (`وثائق المقام`). It was **escalated to the Production Master**, corrected to `وثائق قاعدة الاحتساب` at `06_EVIDENCE_OBJECTS!I112`, and the affected Page Spec/search projections were regenerated. Production Master SHA-256 changed from `d8db3b4e…` to `6c0f8f18…`.
- Clean build: 284 HTML documents from 141 Page Specs; validator `ERRORS=0 WARN=0`; Python/JavaScript syntax PASS; local HTTP smoke PASS. Browser screenshot automation was blocked by the execution environment, so S04.1 does not claim deployed-browser/accessibility acceptance; that remains in S05/S08.
- Reference archive unreviewed inbox: EMPTY. Boundary decision: **PROCEED to S04.2**; S04.2 has not started.

## 2026-09-22 — S04.2 Compare + publication/trust closure — CLOSED; Window 2 ACCEPTED

- Added a distinct `Comparison` family to the existing Canonical Presentation Contract and made Compare compatibility-first: governed definition/universe/geography/unit/period/method/source/currentness fields are assessed before a verdict; missing required metadata fails closed; no numeric values, averages, midpoints, preferred numbers or invented conversion scalars are produced.
- Closure regression found that the first Compare renderer exposed only two selectors while the controlled Page Spec permits 2–4 records. The renderer/client now provide two required plus two optional selections and one N-way compatibility verdict; validator enforcement was added.
- Removed the redundant generic governed-object card wall from Compare; the controlled object set remains available through the selector and Evidence Records.
- Added detached Evidence Record citation context carrying record ID, period, population/base, material boundary and public source IDs; added source-reference trace to Data/source.
- Added source citation controls and an explicit rights boundary separating public citation/factual use from redistribution. Current object-level/unspecified rights state is not promoted into permission.
- Added correction/current-record context without inventing correction/version events not governed by the controlled Corrections Page Spec.
- Fixed an indirect publication-filtering defect: `SRC-MOPIC-YSEU-2023-080`, which has no public locator, was visible as a source ID on a Reading sidebar. Shared source rendering now uses the public-source filter and the validator rejects any no-public-locator source ID in public HTML/search.
- Extended `scripts/validate.py` for Comparison contract/renderer binding, forced-reconciliation prohibition, detached citation safety, source rights/download gating, correction context, Source Reference Closure samples, DISPLAY_READY/LOCATOR_ONLY/NO_PUBLIC_LOCATOR behavior and global publication filtering.
- Clean build: 284 HTML documents from 141 controlled Page Specs; validator `ERRORS=0 WARN=0`; Python/JavaScript syntax PASS; six-route S04.2 HTTP smoke PASS; AR/EN 390px/1440px render harness PASS with no horizontal overflow; independent recipient task harness **143/143 PASS**.
- Page Specs and Production Master semantics were unchanged in S04.2. Master SHA-256 remains `6c0f8f18325b4f117de82e8ac8396c70adf0b3f1871878cf614ed01833ea40fd`.
- Reference archive unreviewed inbox: EMPTY. **Window 2 decision: ACCEPTED. S05.1 is next and has not started.**
- Canonical Drive reconciliation completed in place after Window 2 acceptance; build/validator sources, presentation contract, control stack and closure artifact were written to the existing production repository without creating a parallel copy. Production Master ID/hash were reverified and generated `dist/` remains excluded from canonical Drive state.
- Window 2 permission check found the canonical production folder is shared as anyone-with-link writer. Recorded as open release blocker `R-042`; no concurrent overwrite was observed, but final release certification is blocked until S07 restricts and re-verifies write access.

## 2026-09-22 — S05.1 Arabic/English semantic + typographic QA — CLOSED

- Closed bilingual semantic/typographic QA on a 21-route representative sample spanning Orientation, five Domain Answers, eight hard-case Evidence Records, Compare, Reading, Measurement, Data, Methodology and Corrections.
- Added explicit bidi isolation for stable Latin IDs/source locators and automatic/plaintext direction for mixed-script source metadata; Arabic RTL no longer relies on ambient direction for those tokens.
- Localized Measurement Agenda domain taxonomy in Arabic as an implementation UI label layer while leaving the controlled classification unchanged.
- Removed English-only visual metadata pills from Arabic Reading cards when no governed Arabic equivalent exists; localized governed accessible summaries and prohibited-inference text remain the semantic carrier.
- Extended `scripts/validate.py` for bilingual title/section parity, one-sided localized public fields, representative numeric signatures, Arabic Reading visual-metadata leakage, Measurement taxonomy localization, stable-ID bidi isolation and language-switch route/query/hash preservation.
- Render harness: **21 routes × 2 languages × 2 viewports (390px/1440px) = 84 cases**, all with one `h1`, correct RTL/LTR state and no page-level horizontal overflow.
- Clean build: **284 HTML documents from 141 controlled Page Specs**; validator `ERRORS=0 WARN=0`; Python and JavaScript syntax PASS.
- Production Master and `page_specs.json` unchanged in S05.1. Master hash remains `6c0f8f18325b4f117de82e8ac8396c70adf0b3f1871878cf614ed01833ea40fd`; Page Specs remain `c5a39b072aaea7438c5146476e6923411503d066acb75e2dbf88bd8b99222fb1`. No Master escalation.
- Reference archive `01_NEW_INPUTS__UNREVIEWED`: **EMPTY**.
- `R-007` remains open for S05.2/S08 accessibility runtime acceptance; `R-042` remains an S07 release-security blocker.
- Boundary decision: **S05_1_PROCEED_TO_S05.2**.

## 2026-09-23 — S05.2 Mobile + keyboard + zoom + screen-reader structure — CLOSED

- Fixed a reproducible 320px Home overflow caused by an inline three-column CTA grid; the Home CTA now uses a responsive class and no tested 320/400/640 route produces page-level horizontal overflow.
- Added keyboard-reachable mobile citation/report utilities, focus transfer into the opened mobile nav, Escape return to the menu trigger, and localized copy-success live feedback.
- Hardened Compare assistive structure with a table caption, row/column header scopes, a named focusable horizontal-scroll region and a concise live verdict status instead of making the full result live.
- Added explicit target-language naming/direction to the language control while preserving the existing equivalent-route/query/hash behavior.
- Extended `scripts/validate.py` for main/skip-link/heading/details structure, menu/search semantics, mobile utility reachability, Data focus, correction origin, Compare table/live-region architecture and first-load boundary ordering.
- Local Chromium runtime QA: **84/84 explicit assertions PASS**, including menu/search focus behavior, global search results, progressive Domain/Evidence detail, Reading source control, Compare 2/3/4 records, citation copy feedback, Data/source query focus, correction backtracking, 320/400px bilingual reflow, 640px 200%-reflow-equivalent checks and browser accessibility-tree landmarks/names.
- Clean build: **284 HTML documents from 141 controlled Page Specs**; validator `ERRORS=0 WARN=0`; Python and JavaScript syntax PASS.
- Production Master, Page Specs and Canonical Presentation Contract unchanged. No Master escalation.
- Actual named screen-reader application/browser-chrome zoom and final contrast/deployed-environment acceptance remain explicitly open for S08.1; `R-042` remains an S07 release-security blocker.
- Reconciled the canonical Drive repository in place after acceptance: existing file IDs preserved, `docs/S05_2_MOBILE_KEYBOARD_ZOOM_SCREENREADER_CLOSURE.md` added under the existing docs folder, generated `dist/` excluded, and the control stack now agrees on S05.2 CLOSED / S05.3 NEXT.
- Fixed a control-state lag where `REVIEW_LEDGER.json` and `PROGRESS_INVENTORY.json` still summarized S05.1 after S05.2 had passed; validator checks now protect the current-session/next-session summary.
- Boundary decision: **S05_2_PROCEED_TO_S05.3**.


## 2026-09-23 — Canonical repository hygiene reconciliation after S05.3

- Re-read the live canonical Drive repository before writing and confirmed that `authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx` is the sole Master inside the production repository; `98_TEMPORARY__NONAUTHORITATIVE/` is empty.
- Recomputed the live Production Master SHA-256 as `d3b0421104d63f830cf40d2b1749dc88f302f54e4d79a6c6faf63abc5ad28d9e` and the current Page Specs SHA-256 as `453bde9026c2a30f2c0c2125c0e950cd6e468a9540577318e1896c98e61959da`. Page Specs carry the live Master hash throughout.
- Found and repaired a cross-window partial-integration defect: S05.3 closure prose and validator expectations had advanced, but `build.py` still emitted the earlier `data-visual-fallback="text"` structure and current controls still recorded the S05.2 hash/boundary.
- Repaired the visual renderer so every rendered governed visual carries ordered analytical fallback text, image-independence and non-colour semantics without changing evidence meaning.
- Hardened `validate.py` to hash the actual bundled canonical Master, verify Page Specs against the live Master, verify the raw Page Specs hash against current controls, and reject any workbook copied into public `dist/`.
- Reconciled current controls to S05.3 CLOSED / Window 3 ACCEPTED / S06.1 NEXT_NOT_STARTED. Historical closure files retain the hashes and states that were true when those earlier sessions closed.
- Preserved `R-042` as the only known release-security blocker: anyone-with-link writer access remains open and must be restricted/reverified in S07 before release certification.

### 2026-09-23 — Repository hygiene close

- Replaced the stale `FINAL_RELEASE_VERIFICATION.md` baseline with the live S05.3 / Window 3 accepted authority state and current Master/Page Specs hashes.
- Clarified `DEPLOYMENT.md`: the authority Master is retained inside the canonical repository for governance but must never enter the public `dist/` bundle; the initial product remains fully static/local with future API integration behind controlled adapters.
- Closed the repository-hygiene reconciliation after deterministic build/validator and structural audits passed. The only known repository-level release blocker retained is `R-042` (anyone-with-link writer permission), owned by S07 security/release control.
- Refreshed the checksum-manifest state. `SHA256SUMS.txt` is regenerated last from canonical first-hand files, excluding itself, generated `dist/`, caches and temporary working output.
- Hardened `scripts/validate.py` so current release controls, the S05.3 closure, deployment guidance and checksum manifest are mandatory; the checksum manifest must exactly cover canonical first-hand files and match their bytes, while excluding generated `dist/`, caches and the explicit temporary workspace.
- Added an authority-directory invariant: exactly one canonical `.xlsx` Production Master may exist under `authority/`.

## 2026-09-23 — Independent live-state handoff verification and reference-folder registration

- Reconstructed the current canonical repository from first-hand Google Drive files and verified every path in `SHA256SUMS.txt`; all canonical checksums passed before modification.
- Ran a clean deterministic `npm run verify`: **284 HTML documents from 141 controlled Page Specs; ERRORS=0; WARN=0; PASS**. This independently confirms the current S05.3 / Window 3 accepted repository baseline rather than relying on closure prose.
- Rechecked the live Production Master against its immediately previous Drive revision. The changed block contains bounded Arabic terminology corrections only (including replacement of `مقامات شرطية صغيرة` with `قواعد احتساب شرطية صغيرة`, and `بسط ومقام` with `البسط وقاعدة الاحتساب`); no value, unit, universe, geography, period, source, rights/publication state or claim strength change was identified in that revision comparison.
- Registered Google Drive folder `1tFewVNnzpNXG9tsNyFpoWHnobaKsoRho` as the current **external predecessor/reference folder** for S06 challenge work only. Moving old drafts there is treated as storage organization, not as production-state change and not as a competing source of truth.
- Removed the temporary Drive write-test scratch artifact from `98_TEMPORARY__NONAUTHORITATIVE/`; future scratch remains confined to that excluded workspace and all durable QA/handoff work remains inside the canonical production repository.

## 2026-09-23 — Reference-archive consolidation and canonical-repository hygiene hardening

- Consolidated the user-supplied `Other drafts and sources` folder into the existing non-production reference archive rather than allowing a second sibling reference repository. It now sits under `99_REFERENCE_ARCHIVE_INBOX__NON_PRODUCTION/01_NEW_INPUTS__UNREVIEWED/` as `2026-09-23_SUPPLEMENT__OLD_DRAFTS_AND_SOURCES__UNREVIEWED__NONAUTHORITATIVE` (Drive ID `1tFewVNnzpNXG9tsNyFpoWHnobaKsoRho`).
- Preserved every predecessor/source file in place; no predecessor workbook was promoted, renamed into authority or used to overwrite the Production Master. The canonical Master remains Drive ID `1xAbdDHJd5bYo0Pzo_a6dR6HsZ056LzJU` under `authority/`.
- Removed the temporary `__drive_write_test.txt` scratch file. `98_TEMPORARY__NONAUTHORITATIVE/` is empty again.
- Updated current control state so the reference inbox is no longer incorrectly reported as empty. The new supplement is registered as `UNREVIEWED__S06_PENDING__NOT_PRODUCTION_TRUTH`; S06.1 remains `NEXT_NOT_STARTED`.
- Hardened repository validation so a closed hygiene state fails if temporary scratch remains, and so any canonical `.xlsx` outside the single `authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx` is rejected.
- No semantic/evidence/publication change was made. `R-042` remains open because the Drive repository still carries anyone-with-link writer access; this cannot be certified closed until sharing is restricted and re-verified.



## 2026-09-23 — S06.1 World Bank / Findex + Firms source-owner challenge — CLOSED

- Challenged Yemen Findex and the 2022 custom enterprise survey against original World Bank source-owner surfaces.
- Confirmed current public Findex wave/fieldwork, adult-universe, coverage/exclusion, weighting and raw-case-count boundaries; no public Findex value or claim changed.
- Confirmed the firm survey's seven-governorate scope, 328 formal-enterprise sample, 191 account holders, 31 line-of-credit cases, 18 lender-source responses, and the 50% electricity / 46% fuel / 22% access-to-finance challenge table.
- Found one internal Master control defect: a legacy `Uploaded Findex microdata codebook` block contained unverified/inconsistent pseudo-codebook statements. `24_FINDEX_CODEBOOK!A121` now quarantines rows 122 onward as research/lineage only and directs production use to the verified source-extracted DDI architecture in rows 4–117.
- Production Master SHA-256 is now `ee001adede94642ba001f3ffd9c4dbdb7b8ca30050bb9cc478636fbf71a79ba4`. Controlled Page Specs were rebound to the new Master hash without changing public semantics; Page Specs SHA-256 is `28c247c4d55be0bb0b69aa854d3fdb0caa68f16e23657452afb5e5e1b1dac02b`. Presentation Contract remains `93d9d23c33a0d8a3f1cc65d9260596dc44f84143194a955f3729987fe1c17266`.
- S06.1 CLOSED / PASS. S06.2 is next and NOT STARTED. R-042 remains open; S07/S08 were not executed.

## 2026-09-23 — S06.2 — CBY payments / providers / reforms source-owner challenge — CLOSED

- Rechecked current original CBY monthly payment, Banking Supervision, regulatory and dated enforcement surfaces against the admitted payments/providers/reforms evidence.
- Confirmed the monthly payment index remains bounded through January 2026; preserved terminal ≠ merchant, transaction ≠ person, subscriber ≠ active user, administrative trend ≠ population prevalence and missing ≠ zero.
- Confirmed bank and exchange/remittance rosters remain source-defined listing/licensing universes rather than deduplicated current operating-provider counts.
- Confirmed the unified transfer-network decision, e-money amendment, national QR/e-wallet/FPS decisions and consumer-protection instructions are regulatory/institutional evidence and are not promoted into adoption or outcome claims.
- Found one material currentness defect: official CBY Decision No. 17 of 17 September 2026 suspends the licence of Al-Buraq Exchange and Transfers Company and closes its premises. Integrated it Master-first as a dated status overlay and new source `SRC-CBY-ENF-17-2026`; did not mechanically subtract it from the annual roster.
- Regenerated provider/source/closure/catalog/Page Spec/search projections in place. Controlled source-reference records advanced 149→150; publicly addressable 148→149; locator-only 142→143; public search records 417→418; controlled Page Specs remain 141.
- Current Master SHA-256: `cfe4599e26026f9ca377b9ac4b9b1120781678b981e09bb0f439091483a37dfe`. Current Page Specs SHA-256: `5b5601c043a4857314a4f483db3bf8d8f39a07a838cbac8500324e7f463ba708`. Presentation Contract unchanged at `93d9d23c33a0d8a3f1cc65d9260596dc44f84143194a955f3729987fe1c17266`.
- R-042 remains open and owned by S07. S07/S08 were not executed.
- Boundary decision: **S06.2 CLOSED / PASS. S06.3 NEXT_NOT_STARTED.**
