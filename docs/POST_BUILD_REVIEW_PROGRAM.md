# Post-Build Review Program

## Purpose

This is a finite product-maturation program for the **Yemen Financial Inclusion Evidence / أدلة الشمول المالي في اليمن** website repository. It does not reopen the evidence architecture and does not create a second source of truth. The Production Master identified by the authority hash remains the sole semantic, evidence, source, rights and publication-state authority. Repository changes may improve rendering, navigation, explanation, accessibility, performance and verification behavior, but may not widen or reinterpret a controlled claim.

## Operating method

Each session follows **ORIENT → CHALLENGE → DECIDE → BUILD → VERIFY → INTEGRATE → HANDOVER**. One decision owner is used throughout. Each session uses at most two adversarial lenses so challenge remains useful rather than becoming committee theatre. Every material edit is recorded in `docs/CHANGELOG.md`; open defects and dispositions are recorded in `docs/REVIEW_LEDGER.json`. Changes are made directly in this single Google Drive repository folder. No ZIP is used as the working repository; verified edits are written back to the same production folder and logged there.

## Bounded execution from S03 onward

S00–S06, Window 3 and S06 recipient acceptance are closed. The S03–S08 programme is defined as **16 small micro-sessions**; **4 remain from S07.1 through S08.2** with one outcome and explicit exit tests each. The binding sequence and stop rule are in `docs/SESSION_EXECUTION_PROTOCOL.md`. A micro-session cannot close merely because review occurred; it closes only when its acceptance tests pass or an explicit no-change decision is documented. After each micro-session the next session is re-justified against the remaining defects and user value, without silently expanding scope.

## Small-session control

The high-level S00–S08 programme is executed through bounded micro-sessions defined in `docs/SESSION_EXECUTION_PROTOCOL.md`. A high-level session may contain several micro-sessions, but only one micro-session is active at a time. Every micro-session must end with a written rationalization, explicit exit evidence, and a decision to proceed, revise, stop or escalate to the Production Master.

## Small-session execution control

The S00–S08 programme is executed through the bounded sessions in `docs/SESSION_EXECUTION_PROTOCOL.md`. Only one bounded session is active at a time. Each session has one exact achievement, one owner, at most two challenger lenses, explicit exit evidence, and a written closure decision before the next session starts. The protocol is the detailed execution authority; this file remains the high-level maturation map.

## Finite session plan

| Session | Decision owner | Challenger lenses | Primary work | Exit evidence |
|---|---|---|---|---|
| **S00 — Repository truth & baseline** | Product/evidence lead | Release engineer; skeptical recipient | Verify repository state, authority references, build reality, stale documentation, generated-route structure and baseline defects. | Clean build; integrity metrics; review ledger; authority/status docs aligned to actual repository. |
| **S01 — Navigation, search & first-use UX** | Information architect | Citizen/mobile user; senior decision-maker | Global navigation, mobile menu, global search, language switching, first-click clarity, page density and progressive disclosure. | Keyboard/mobile-safe navigation; global search; no dead-end first-use paths; route hierarchy review. |
| **S02 — Audience journeys & information architecture** | Product strategist | CBY/technical user; journalist/researcher | Test task journeys for citizen, journalist, PhD researcher, CBY governor/technical team, financial institution, development partner, humanitarian actor and general public. Challenge sitemap and route purpose using actual user jobs. | Journey matrix; route keep/merge/change decisions; Counterfactual Deletion Test. |
| **S03 — Home, Explore & domain-page editorial system** | Editorial/product lead | Financial-inclusion specialist; bilingual editor | Refine Home and Explore; make domain pages answer-first; reduce repetition; bind visuals/evidence intentionally rather than dumping governed arrays. Preserve unit/universe/period boundaries. | Page grammar implemented; duplicate/empty modules eliminated; answer → meaning → boundary → unknown → verify rhythm. |
| **S04 — Evidence verification, citation & source experience** | Evidence lead | Source librarian; reproducibility reviewer | Evidence Hub, Passports, Compare, source locators, citation, rights/download behavior, corrections/versioning and source-reference closure. | Claim-to-source path test; comparison legitimacy; citation behavior; withheld/non-redistributable content non-leakage. |
| **S05 — Visuals, bilingual UX & accessibility** | Information-design lead | Accessibility specialist; Arabic/RTL specialist | Visual contracts, tables/fallbacks, typography, long Arabic labels, RTL order, mobile reflow, keyboard/focus, zoom, reduced motion, non-colour semantics. | WCAG-oriented static checks; visual fallback matrix; AR/EN semantic parity sample; mobile/RTL acceptance evidence. |
| **S06 — Source-owner & external benchmark challenge** | Evidence/product lead | Source-owner lens; conflict/Yemen lens | Check how the product represents WB/Findex, IMF, CBY, SFD/SMED/SMEPS, provider/regulatory material, humanitarian/cash-transfer sources, OCHA/ReliefWeb and other admitted sources. External research is challenge-only unless the Production Master is amended first. | Source-usage findings; framing/currentness/locator/rights issues either fixed in the Master or explicitly left unchanged. |
| **S07 — Technical quality, performance, privacy & release engineering** | Technical lead | Security/privacy reviewer; low-bandwidth/mobile reviewer | Static architecture, asset weight, caching, SEO metadata, link checking, CSP/headers guidance, privacy surface, error states, 404, low-bandwidth path and deploy reproducibility. | Repeatable build; expanded validator; performance/security/deployment checklist; zero public restricted-object leakage. |
| **S08 — Blind-reader red team & release-candidate integration** | Release owner | Blind reader; adversarial QA | Cold-recipient test across roles, factual regression, bilingual regression, route/task completion, final deletion/merge pass and correction/version behavior. | Finite defect disposition; regenerated repository; checksums; release-candidate statement limited to tests actually passed. |

## User-role stress set

The review will explicitly test tasks from the perspectives of: a Yemeni citizen; journalist; PhD student/researcher; CBY governor/senior decision-maker; CBY technical analyst; bank/MFB/MFI/PSP/exchange/remittance provider; SFD/SMED/SMEPS practitioner; World Bank/IFC team; IMF team; KfW/DFI/donor; UN/humanitarian/social-protection/cash-transfer actor; and a general public reader.

The product will **not** create audience-specific facts. The test is whether one controlled evidence truth can serve these users at different depths.

## Non-negotiables

- People ≠ accounts; access ≠ use; infrastructure ≠ outcome; target ≠ result; programme KPI ≠ national prevalence; licensing/listing ≠ operation; missing ≠ zero.
- Public claims do not widen beyond unit, universe, denominator, geography, period, method, authority or evidence class.
- External facts discovered during challenge do not enter production directly. Material evidence corrections go to the Production Master first and are then regenerated into the repository.
- Rights to cite, use facts and redistribute source files are treated separately.
- Arabic and English remain co-authoritative.
- A route/component survives only if removing it would lose material user value.
- Repository readiness is not called live-release readiness until browser/runtime, RTL/mobile, accessibility, publication filtering, security/privacy, correction/version behavior and named release approval have actually passed.


## Current boundary — 2026-09-23

**S06_WINDOW_ACCEPTED.** The existing implementation handoff is frozen for Claude Design → Claude Code. S07.1 is queued but not started; S07/S08 release gates remain open.
