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

*(filled in after B15 d)*

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
