# S06 Recipient-Side Acceptance — SOURCE-OWNER WINDOW ACCEPTED

**Date:** 2026-09-23  
**Decision:** **S06_WINDOW_ACCEPTED**  
**Next review session:** S07.1 is **QUEUED / NOT STARTED**. S07 and S08 are not opened by this acceptance.  
**Handoff boundary:** the existing `handoff/` may now be frozen and strengthened for **Claude Design → Claude Code**. No parallel handoff package is permitted.

## Authority at acceptance

- Production Master: `authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx`
- Drive ID: `1xAbdDHJd5bYo0Pzo_a6dR6HsZ056LzJU`
- Production Master SHA-256: `f94f1f91084b01964a3bb7b3847fd68a19555cc901ab6078146a187efe17e860`
- Controlled Page Specs SHA-256: `4e8a0d8f0cf58f78389360c69cf04f3bf0d24f1ba9b3e4ef10ebe93461e69f1a`
- Semantic/evidence/source/rights/publication authority: Production Master only.

## Recipient-side method

Acceptance was performed as a new recipient rather than as the author of S06. The test was:

**PROMISED SOURCE-OWNER RESULT → FIRST-HAND CURRENT MASTER / PROJECTION → PUBLIC OBJECT / SOURCE CLOSURE → PUBLICATION / RIGHTS FILTER → EN/AR / REGRESSION → CURRENT REPOSITORY STATE.**

The owner was the evidence/release acceptance lead. Challenger lenses were (1) source-librarian/rights and (2) skeptical recipient/reproducibility reviewer.

## S06.1–S06.3 acceptance

| Bounded source-owner session | Recipient result | Acceptance basis |
|---|---|---|
| S06.1 — World Bank / Findex / Firms | **PASS** | Findex wave/fieldwork/universe/exclusions, weighted aggregates and firm-survey universes remain bounded; the legacy pseudo-codebook block is quarantined in the Master rather than allowed to contaminate public evidence. |
| S06.2 — CBY Payments / Providers / Reforms | **PASS** | Administrative units remain distinct; missing remains missing; licensed/listed ≠ operating; regulation/decision ≠ implementation/outcome. CBY Decision 17/2026 is integrated as a dated provider-status event without rewriting the annual roster universe. |
| S06.3 — IMF / Remittances / Microfinance / Programme / Humanitarian | **PASS AFTER CONCURRENCY RECONCILIATION** | Observed/estimated/projected remittances remain distinct; BOP ≠ settlement ≠ informal-hawala volume; SMEPS KPI remains programme evidence; OCHA/UCT/FSP material remains bounded; rejected archive arithmetic has not leaked. A newer Master revision corrected the 2011 SFD microfinance treatment and was adjudicated rather than rolled back. |

## Concurrency event discovered during acceptance

The live Production Master was newer than the S06.3 closure snapshot. This was treated as a **CONCURRENCY EVENT**, not as a reason to restore the older file.

A first-hand workbook/ZIP comparison isolated the material semantic delta to `21_MFI_DATA` around the SFD Q4-2011 evidence. The official newsletter itself contains two non-identical representations:

- narrative explicitly referring to end-December 2011 and reporting about **64,000 active borrowers**, **87,000 active savers** and **YER 4,030m** outstanding portfolio;
- a table headed **end of December 2010** reporting **63,568 borrowers**, **87,615 savers** and **YER 3,853m** portfolio.

The current Master therefore does the more defensible thing: it preserves both primary-source statements, removes the false clean `2011-12-31` anchor from the table row, marks the portfolio as a within-source value conflict and prevents the row from joining a continuous time series. No single settled 2011 portfolio value is asserted.

**Decision:** retain the newer current Master. Do not restore the predecessor “clean” 2011 anchor.

## Projection and public-use consequence

The Master correction does **not** alter a current public claim, Reading headline or public numeric card: the 2011 microfinance figures are not present in the controlled Page Specs. The required subordinate work was therefore:

1. regenerate `site-src/content/data/mfi_data.json` from the current Master for the affected rows;
2. rebind all 141 Page Specs to the current Master SHA without changing their substantive public copy;
3. refresh control/handoff hashes;
4. rebuild and revalidate the public product;
5. preserve the source conflict as a backend/evidence boundary for any future use.

## Source Reference Closure and publication filtering

Recipient acceptance rechecked the S06 evidence families against the existing closure architecture:

**PUBLIC OBJECT → canonical claim/evidence → lineage/dependency → Source Library → original locator/authority → rights/publication state → Evidence Record/Passport → public citation.**

Acceptance requires all of the following and they remain true in the current controlled state:

- public URLs are not treated as redistribution permission;
- locator-only records do not acquire invented titles, publishers, licences or reuse rights;
- the no-public-locator dependency remains withheld from standalone public rendering;
- rejected/deferred archive candidates do not enter Page Specs, public HTML, search or downloads;
- programme reach/beneficiaries/payment sites are not converted into population financial-inclusion prevalence or durable-use outcomes;
- CBY↔IMF raw-level remittance crosswalk remains unresolved rather than forced.

## Bilingual and regression result

The concurrency correction does not change public EN/AR copy. Page Specs retain the same public content and route set; only their authority hash is rebound. The accepted S03–S05 semantic boundaries remain mandatory and are rechecked by the repository validator, including:

- people ≠ accounts;
- access ≠ use;
- infrastructure ≠ outcome;
- target ≠ result;
- programme KPI ≠ national prevalence;
- licence/listing ≠ operation;
- observed ≠ estimated ≠ projected;
- missing ≠ zero;
- RTL/LTR structure, keyboard/reflow safeguards and visible non-colour/image-independent visual fallbacks.

## What became more true

The 2011 SFD microfinance evidence no longer looks cleaner than its source. The product now preserves an internal primary-source date/value contradiction rather than selecting whichever number creates the smoothest historical series.

## What became more complex

One historical microfinance point is now intentionally a conflict object rather than a normal year-end observation. That complexity is evidence, not noise, and should remain visible if the point is ever promoted to a public analytical surface.

## What can now be removed

- any claim that the SFD Q4-2011 table is an unambiguous exact 2011 year-end aggregate;
- any use of YER 3,853m or YER 4,030m as the sole settled 2011 portfolio value;
- the stale repository summaries that described S06.2 or S06.3 as still pending;
- stale handoff hashes/counts from the pre-S06 state.

## Open boundaries deliberately not closed here

- `R-042`: anyone-with-link writer access remains a release blocker for S07 security/release control.
- Remote webfont runtime dependency remains to be removed in final code implementation / S07 technical acceptance.
- Named screen-reader application, browser UI zoom, final contrast and deployed-runtime acceptance remain later gates.
- Live public release approval remains **false**.

## Boundary decision

**S06_WINDOW_ACCEPTED.**

Freeze and strengthen the existing `handoff/` only. Claude Design receives the controlled repository first; Claude Code starts only after a repository-backed design package exists. If a required controlled field is absent or contradictory, the recipient must return `NEEDS_CONTROLLED_CONTENT` / `ESCALATE_TO_MASTER`, never invent it.
