# Roadmap for version 1.1 — ranked by value to the reader

**Status, 3 October 2026:** a plan, not a commitment. Nothing here is built. Items are ranked by their value to the people
the product serves (the ten users of `audit/release_candidate/PRODUCT_CHALLENGE.md`). Each says what it needs: **data**
(a source to read and bind Master-first), **decision** (the owner's), **design** or **code**. Every item keeps the
programme's rules: the Production Master is the only authority, English and Arabic change together, and no number is
published without a bound, source-traced record.

## 1. International context from same-source aggregates

*Who gains:* the economist, the donor officer, the journalist, the policymaker (PRODUCT_CHALLENGE.md, game-changer test).

*What:* place Yemen's Global Findex values beside aggregates built on the same definition and in the same wave. Examples
are the Middle East and North Africa, low-income economies, and fragile and conflict-affected settings. A reader can then
see whether 11.9 % of adults with an account is low for the region and for similar economies.

*Caveats it must carry, in both languages:*
- Yemen's sample coverage: about 23 % of the population's geography was excluded, and more than a quarter of the
  primary sampling units were replaced.
- The wave, and Yemen's fieldwork dates (7 November 2022 to 9 January 2023), which differ from most comparators.
- That an aggregate is a weighted average of other countries and says nothing about Yemen's own path.
- That Findex 2025 does not cover Yemen.

*Needs:*
- Data: the aggregates from the Findex databank, read and bound Master-first with their universes.
- Design: a comparator row, in the table pattern; no rank.
- Code: none new.

## 2. Public downloads, after the licence decision

*Who gains:* the academic researcher, the economist, the journalist.

*What:* switch on the prepared exports. These are six datasets as CSV and JSON, with a bilingual codebook and provenance
on every row (`scripts/exports.py`; B14 a).

*Needs:*
- Decision: the owner's licence decision (`docs/RELEASE_RUNBOOK.md`, step 2).
- Copy: the codebook's bilingual review; the reuse terms stated on /data/, Master-first.
- Code: `public_downloads: true`.

## 3. From the product challenge

The ranked items found by the panel and the red team that were not built in B15 d are listed in
`audit/release_candidate/PRODUCT_CHALLENGE.md`, with the reason each was deferred. They are copied here in that ranking:

| # | Finding | Who gains | What it needs |
|---|---|---|---|
| 1 | C-7: page and table locators on source links (CLM-032's sources are 51- and 54-page PDFs) | Economist, academic, journalist | Data: each source read page by page; a locator field on source links, Master-first |
| 2 | A-7 (rest): the Reading "The payment arrived. What happened next?" on /payments/ | Humanitarian cash manager, citizen | Decision: an answer page carries at most two Readings, and /payments/ has CWR-005 and CWR-009; the editor chooses which gives way. Then one Master field (CWR-010 `domain_surface_routes`) |
| 3 | An inline link in governed prose (A-7's sentence to CWR-010; B-3's boundary to CLM-036) | Every reader | Design and code: a governed inline-link mechanism (governed prose holds no links today, only e-mail addresses) |
| 4 | B-6 (rest) and U9: each priority split into "analyse what exists" and "collect new" | Donor, policymaker | Copy: governed text per priority, both languages; the split keeps "requires authorised respondent-level data", with no feasibility upgrade and no ranking |
| 5 | B-2 (rest): parent records linked to their entity records (CLM-015 → NEG-EW-011; CLM-019 → its status events) | Supervisor, provider | Code; the naming rule waits on the owner (`design/ESCALATIONS.md`) |
| 6 | A-9 (rest): a boundary on each Home figure card | Citizen | Design: a short form of each boundary, governed; CLM-003's boundary alone is 96 words, and boundaries may not be collapsed |
| 7 | A-11: a short bilingual glossary («إطار المسح», «وحدات المعاينة الأولية», «نقطة مئوية»); CLM-001 linked to the access-and-use figure | Citizen, policymaker | Copy, Master-first; no new route |
| 8 | B-8: "same provider set: yes / no / unknown" on the microfinance observations | Strategy officer, economist | Data: read from each source; "unknown" is a valid value |
| 9 | B-9: one line comparing the 2025 and 2026 rosters, warning that the difference is not net market entry | Supervisor, journalist | Copy, Master-first; no computed difference |
| 10 | A-16: the page index collapsed at the top of long pages; a governed "back to top" | Citizen on a phone | Code and one governed label; only the index collapses, never evidence or boundaries |
| 11 | A-4 (rest): the evidence-landscape rows indexed for search; «ابدأ من الأسئلة» as a link | Citizen | Code (the generator's search records) |
| 12 | C-6 (rest): a "Who publishes and funds this" heading on /about/ | Journalist, donor | Copy, Master-first; the organisation's description from the owner |
| 13 | A-1 (rest): a «أعد المحاولة» / "Try again" button when the search index fails to load | Citizen on a weak connection | One governed label; code |
| 14 | A-5, A-6: search in the other language on zero hits; the search index split by language at build time | Citizen on a weak connection | Code |
| 15 | A-13: the report link keeps the record ID at 390 px; a governed Arabic e-mail subject; a body with no personal-data fields | Every reader | Code and copy |
| 16 | A-14: script-only controls hidden when JavaScript is off | Every reader | Code |
| 17 | A-17 (rest): Arabic month names in meta lines | Arabic reader | Code (the date-words helper exists) |
| 18 | C-2 (rest): the publisher in a source card's copied reference | Academic | Code (the publisher is governed) |
| 19 | B-11: "Issuing authority: Unknown — not zero" reworded; the Reading slug "microfinance-structural-divergence" renamed before launch | Strategy officer | Copy, Master-first; the slug only before launch |
| 20 | C-11, C-13, C-14: empty groups hidden when /data/ is filtered; Compare starts empty; the 404 follows the path's language | Every reader | Code; any hint text governed |
| 21 | C-12: /evidence/ "Start here" opens with the headline records | Every reader | Master data (the Page Spec's bound records) |
| 22 | C-15 (rest): a shorter Home opening | Citizen on a phone | Copy, Master-first; "Another view of the evidence" stays (red team) |
| 23 | B-4 (rest): search aliases from the three remittance gaps to MA-001 | Donor | Master data; no new priority (REJ-02) |
| 24 | U4: a dated rulebook and status timeline per provider class | Provider | A contract over the system chronology and the e-money rule stack; chronology ≠ causality; no names |
| 25 | /providers/: "some were issued before the roster and some after it" beside "the roster's issue date is not stated" (bilingual review of RC-15; predates the pull request) | Supervisor | Decision (steward): date the roster by its file (22 September 2026) or drop the before-and-after clause; Master-first |
| 26 | A coverage sentence on the three records that set several Findex waves side by side (CLM-031, VIS-DEMAND-VINTAGE-LADDER, DS-FINDEX-HISTORY-CROSSWALK), naming the 2021 wave alone (RC-16 review) | Economist, academic | Copy, Master-first; each already links CLM-025 through its wave |
| 27 | U8: a checklist for tracking whether transfer accounts stay in use | Humanitarian cash manager | Copy from CWR-010 and MA-009, keeping "cash-out is not failure"; as a file only after the licence decision |
| 28 | C-10: a domain strip across the eight domain answers | Every reader | Design: a new navigation element (owner decisions of 3 October 2026, 09:05 point 4 and 09:50 A.4: not in this release) |
| 29 | The system chronology on /reforms/, /payments/ and /remittances/, with an event-card variant (owner instructions of 3 October 2026, 09:50, C6) | Supervisor, journalist | Design: the chronology renders on /finance/ only, and an event card is a new component; the events' relevance text would need checking against each page's question, and chronology ≠ causality |
| 30 | A lighter /ar/data/ (09:50, C6) | Arabic reader on a phone | Code and design: the page is complete without JavaScript by rule (DL-D7-013), so lightening it means paging or splitting the source list, not hiding it |
| 31 | CWR-010 on /payments/ (09:50, C6) | Humanitarian cash manager | Master: the generator allows two Readings per answer page and /payments/ has two; a third needs a design decision on which one yields (RC-15) |

## 4. Named in Owner Addendum 2 (do not build now)

| Item | Needs |
|---|---|
| The Findex 2021 weighted subgroup computation (188 specified contracts) | Data: the Findex 2021 microdata file for Yemen (World Bank Microdata Library), under its terms; code: a reproducible computation with its weights and design effects; a reviewer |
| RV-CWR-004's people lane extended back to 2011, as rows, not as a new contract | Data: the 2011 and 2014 Findex rows for Yemen (the API holds 3.66 % and 6.45 %), bound Master-first with their universes |
| A "safe sentence" copy control: one-click copy of a governed sentence with its boundary | Design and code; copy is already governed |
| Inline dated source brackets in Readings | Design; the dates are governed |
| Versioned Readings (what changed, when, why) | Decision on the versioning rule; code |
| A domain search facet | Code: the search index already carries routes |
| Reading audiences (who a Reading is written for) | Data: the `audiences` field exists in the Readings projection; design |
| IOM DTM and VSLA documentation as context for MA-003 and MA-009 | Data: read and bind the documents as library sources, Master-first |
| CPMI-IOSCO as a method reference | Data: a library source on the methods shelf |

## 5. The inputs that would complete the text-first visuals (B12)

Seventeen contracts wait on a named Master input (`audit/release_candidate/B12_TEXT_FIRST_DISPOSITIONS.md`). In order of
reader value:
- the saver-definition crosswalk and the rial valuation for the microfinance anchors (VIS-MFI-DIVERGENCE, RV-CWR-006);
- the SMEPS 2024 KPI rows (RV-CWR-008, panel 3);
- the e-payment study's tables (RV-CWR-005);
- Arabic text and source references for the 13 system relationships (VIS-INCLUSION-TRANSMISSION);
- a typed gap field on the Measurement Agenda (VIS-EVIDENCE-GAPS);
- the rest as listed there.

## 6. Library and currentness

- The nine CBY-Aden regulatory documents linked on its regulation page and not yet held, among them Decision No. 7 of
  2026 and Circular No. 1 of 2026 (`FINAL_OPEN_ITEMS_REGISTER.md`, 3 October 2026). Each needs reading, titling in both
  languages, and adding Master-first.
- The 22 values whose hosts refuse automated requests are re-read by a person at release (`ORIGINAL_SOURCE_VERIFICATION.md`
  §8). After that, the currentness re-run (`scripts/currentness_rerun.py`) becomes a scheduled release check.
