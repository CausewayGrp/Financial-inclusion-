# Session Execution Protocol

> **HISTORICAL_LINEAGE (Pre-Tranche-C P4).** This protocol and the hashes in it describe the repository when it was written. Current state: `README.md`, `authority/YFI_CURRENT_PROJECT_CONTEXT.json` and `OPENAI_REENTRY_CHECKPOINT.md`.

> **CURRENT USE NOTICE — R8 FINALIZATION:** The 16-session schedule below is retained as build lineage. It no longer controls the current execution order. Current sequencing is governed by `audit/FINALIZATION_PROGRAM.md`, and every active/future session is governed by `docs/SESSION_CLOSURE_QUALITY_STANDARD.md`. The Production Master remains the sole content/evidence/source/rights authority. R8.5 may retire this historical schedule to `audit/` once no current dependency remains.


## Purpose

This protocol controls the remaining maturation work for **Yemen Financial Inclusion Evidence / أدلة الشمول المالي في اليمن**. The remaining work is deliberately split into **16 small, bounded sessions**. Only one session is active at a time.

The Production Master remains the sole semantic, evidence, source, rights, controlled-product-state and publication-state authority. A website session may improve implementation, presentation, navigation, verification behavior, accessibility, performance and release engineering. It may not silently change evidence meaning.

## Mandatory session method

Every session follows:

**ORIENT → CHALLENGE → DECIDE → BUILD → VERIFY → INTEGRATE → HANDOVER**

Each session has:
- one decision owner;
- at most two challenger lenses;
- one exact achievement;
- a finite scope;
- explicit exit evidence;
- a written end-of-session rationalization;
- one explicit next-session decision.

A session is **not** complete because files changed. It is complete only when the following are written down:

1. **What became more true?**
2. **What became more usable or simpler?**
3. **What new complexity did the change introduce?**
4. **What can now be removed, merged or retired?**
5. **What is the smallest next session that materially advances the product?**

Before the next session begins, update `docs/CHANGELOG.md`, `docs/PROGRESS_INVENTORY.json` and the session-specific review artifact.

## Remaining finite programme — 16 sessions

| Session | Exact achievement | Owner | Challenger lenses | Exit evidence |
|---|---|---|---|---|
| **S03.1 — People + Access composition** | Establish the answer-first domain grammar using one dense people route and one sparse access route; preserve population/geography/currentness boundaries while reducing public-page burden. | Editorial/product lead | People-side evidence specialist; first-time reader | EN/AR composition accepted; before/after density; no evidence loss; validator pass. |
| **S03.2 — Firms + Finance composition** | Apply the grammar to enterprise survey/programme evidence and financial-system evidence without collapsing denominators, programme KPIs or balance-sheet states. | Editorial/product lead | Firm-finance specialist; financial-system analyst | Two routes rebuilt; denominator/programme/state distinctions verified. |
| **S03.3 — Payments + Remittances composition** | Recompose high-frequency administrative payments and remittance evidence while preserving infrastructure≠use, BOP≠settlement throughput and vintage/state differences. | Editorial/product lead | Payments specialist; remittance/macro specialist | Two routes rebuilt; comparison and non-inference boundaries explicit. |
| **S03.4 — Providers + Reforms + domain-system closure** | Recompose Providers and Reforms, then close the entire eight-route Domain Answer presentation system. Establish one implementation-bound presentation-priority contract controlling visibility, ordering, prominence, progressive depth, linking and mobile priority without taking semantic authority from Page Specs/the Master or forcing unlike routes into one repeated template. | Product/editorial lead | Provider/regulatory specialist; information architect | Providers/Reforms accepted; one canonical machine-usable presentation-priority contract; eight-route PRIMARY/SUPPORTING/PROGRESSIVE/LINKED/UTILITY mapping; Counterfactual Deletion Test; full eight-route S03 regression pass; S03 closed. |
| **S04.1 — Evidence records + discovery journey** | Build and test search/domain → Evidence Hub → evidence record → scope/limitation/method → source → backtracking/related evidence for both a non-expert verifier and an expert reproducibility user. Stable IDs may support verification but must not be required knowledge. | Evidence UX lead | Journalist; reproducibility reviewer | Both verifier journeys work in the generated product; no dead ends; evidence-record hierarchy accepted. |
| **S04.2 — Compare + Data/source + citation/rights/corrections closure** | Build one coherent trust/verification system across Compare, Data/source navigation, source-query behavior, citation, factual use, redistribution rights, corrections, version behavior and publication filtering. Demonstrate Source Reference Closure on sampled public objects. | Evidence lead | Source librarian/rights reviewer; audit reviewer | Compare legitimacy; sampled public-object → evidence/claim → lineage → Source Library → original locator/authority → rights/publication state → evidence record → public citation closure; correction/version path; no rights overclaim. |
| **S05.1 — Arabic/English semantic + typographic QA** | Verify native Arabic, EN↔AR semantic invariance, RTL reading order, numerals, units, dates and typography on representative routes. | Bilingual information-design lead | Arabic editor; quantitative editor | Invariance sample; RTL/typography corrections; no meaning drift. |
| **S05.2 — Mobile + keyboard + zoom + screen-reader structure** | Test and correct interaction/accessibility behavior across representative routes and utilities. | Accessibility lead | Low-bandwidth mobile user; keyboard/screen-reader lens | 320–400px, 200% zoom, keyboard/focus/landmark evidence. |
| **S05.3 — Visual/table fallback + non-colour semantics** | Ensure every material visual remains truthful and usable without colour, wide viewport or image interpretation. | Information-design lead | Accessibility specialist; data-visualization reviewer | Visual fallback matrix; alt/summary/table/reflow acceptance. |
| **S06.1 — World Bank/Findex + firms source-owner challenge** | Test whether people/firm evidence is represented with the original source's universe, method, vintage, exclusions and limitations. | Evidence lead | Source-owner/editor lens; Yemen sampling/conflict lens | Adjudicated findings; any semantic correction routed through Production Master. |
| **S06.2 — CBY payments/providers/reforms source-owner challenge** | Challenge CBY material for authority, period, listing≠operation, infrastructure≠use and regulation≠implementation/outcome. | Evidence lead | CBY technical lens; skeptical independent analyst | Source-family disposition; no silent website correction. |
| **S06.3 — IMF/remittances + SFD/SMED/SMEPS + humanitarian challenge** | Challenge macro/remittance, microfinance/programme and humanitarian/cash-transfer framing; keep programme/BOP/prevalence/operational states separate. | Evidence lead | Original-publisher lens; conflict/humanitarian lens | Adjudicated source-use report; candidates either Master-integrated or rejected. |
| **S07.1 — Performance + low-bandwidth + discoverability** | Reduce avoidable payload, test static delivery/caching/asset weight and complete SEO/discoverability without degrading evidence. | Technical lead | Low-bandwidth user; search/performance reviewer | Reproducible build; payload budget; metadata/indexing checks. |
| **S07.2 — Security + privacy + deployment contract** | Complete CSP/header guidance, privacy surface, error behavior, publication filtering and deterministic deployment instructions. | Release engineer | Security/privacy reviewer; deployment reviewer | Deployment checklist; privacy/security disposition; clean rebuild. |
| **S08.1 — Blind-reader + final regression/deletion test** | Give unfamiliar readers real tasks; treat wrong answers/dead ends as defects; rerun factual, bilingual, rights and route regression; perform final deletion/merge pass. | Release owner | Blind reader; expert verifier | Finite defect disposition; zero unresolved material regression. |
| **S08.2 — Final repository closure** | Rebuild from first-hand source, run final validators, refresh checksums, remove obsolete build archaeology, freeze the clean repository and state exactly what is/is not release-approved. | Release owner | Recipient developer; adversarial QA | Clean canonical repository; final checksums; final handover state. **END.** |

## Decision rule at every session boundary

At session close, choose exactly one:

- **PROCEED** — exit criteria passed and the next session is still the highest-value intervention.
- **REVISE** — the session's own change introduced a material defect; fix within the same session before moving on.
- **ESCALATE_TO_MASTER** — a semantic/evidence/source/rights/publication defect was found; repair the Production Master first, regenerate the projection, then resume.
- **STOP** — the planned next session would add no material user value or the final stop rule has been reached.

Do not skip forward because a later session looks more interesting. Do not reopen a closed session without a named defect, changed authoritative input or demonstrated regression.

## Final stop rule

The programme ends at **S08.2**. After S08.2 the repository is reopened only if one of these occurs:

- a named release-approval condition remains unmet;
- a reproducible defect is found;
- the Production Master changes;
- a source, rights, correction or version event materially changes a public object.

A new idea, a newer draft, or another AI's recommendation is not by itself sufficient to reopen the build.

## Current state marker — S05.3 closed / Window 3 accepted

- S03 and S04 remain **CLOSED** regression fixtures.
- S05.1 **Arabic/English semantic + typographic QA** remains **CLOSED / PASS**.
- S05.2 **Mobile + keyboard + zoom + screen-reader structure** remains **CLOSED / PASS**.
- S05.3 **Visual/table fallback + non-colour semantics** is **CLOSED / PASS**.
- Independent Window 3 acceptance is **ACCEPTED**.
- The current Production Master is stored at `authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx` and has SHA-256 `d3b0421104d63f830cf40d2b1749dc88f302f54e4d79a6c6faf63abc5ad28d9e`.
- Controlled Page Specs are bound to that same Master and have SHA-256 `453bde9026c2a30f2c0c2125c0e950cd6e468a9540577318e1896c98e61959da`.
- Actual named screen-reader application, browser-chrome zoom and final contrast/deployed-environment accessibility acceptance remain explicitly open for S08.1; no verified WCAG-conformance claim is made.
- `R-042` remains open for S07 release security: anyone-with-link writer access must be restricted and re-verified before release certification.
- **S06.1–S06.3 and S06 recipient-side acceptance are CLOSED / ACCEPTED.**
- Four bounded sessions remain from S07.1 through S08.2; **S07.1 is QUEUED / NOT STARTED**.
