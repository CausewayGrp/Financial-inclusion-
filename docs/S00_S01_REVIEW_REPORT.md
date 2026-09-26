# S00–S01 Review Report

**Date:** 2026-09-22  
**State:** integrated into the production repository  
**Scope:** repository truth, navigation, global search, first-use UX, public-rendering hygiene, source-result completion and non-production archive challenge

## Executive finding

The controlled evidence system was materially stronger than the first public rendering. S00–S01 therefore treated a successful build as a baseline, not proof of a finished public product. The review found implementation defects that could impede a first-time user even when the underlying evidence remained correct.

**No Production Master evidence semantics were changed in S00–S01.**

## Material defects closed

1. **Repository truth:** authority metadata no longer claims that the Production Master workbook is bundled in the website repository; the Master remains external authority identified by filename/hash.
2. **Stale handoff state:** implementation status now reflects the actual static-first bilingual build and the remaining release gates.
3. **Phone navigation:** the CSS/JS conflict that could hide both primary navigation and its menu control was corrected; menu state is explicit and keyboard dismissible.
4. **Global search:** the header search control now opens a bilingual site-wide search instead of merely routing to Evidence.
5. **Public rendering hygiene:** overlapping reference arrays are de-duplicated by stable ID, empty evidence cards are suppressed, and the correct public summary/limitation fields are used.
6. **Source-result completion:** source search results that resolve to `/data/?source=<ID>` now land on the named controlled source record rather than a generic Data page.
7. **Arabic search:** diacritics and common alef/alif-maqsura variants are normalized for matching without altering the controlled search payload.
8. **Error recovery:** the 404 route is a bilingual recovery surface with routes back to the evidence journey.
9. **Public-language firewall:** implementation-authored Arabic no longer uses backend phrases such as `ساعات أدلة مختلفة`; the validator now rejects a controlled list of prohibited backend expressions in public HTML.
10. **Repository controls:** two S01 control documents referenced by the validator/changelog but absent from Drive were created and made first-hand repository files.

## Before/after rendering audit

Baseline generated-site audit before the first rendering correction:

- Pages containing an empty answer-card paragraph: **238**
- Pages containing duplicate stable-ID answer cards: **20**
- `/people/`: **47** answer cards, including **27** empty cards and **14** duplicated stable IDs

After correction:

- Pages containing an empty answer-card paragraph: **0**
- Pages containing duplicate stable-ID answer cards: **0**
- `/people/`: **33** non-empty answer cards

The remaining People/domain density is **not** treated as solved by deletion. It is deliberately carried into S03 for route-level composition and progressive disclosure.

## First-use improvements integrated

- `aria-current="page"` for current top-level navigation.
- Search modal with live status, bounded result summaries, result-type labels and focus return.
- `Ctrl/Cmd+K` and `/` global search shortcuts outside typing controls.
- Search de-duplication for records that resolve to the same public destination.
- Stable-ID search weighting for evidence/source verification tasks.
- Escape, outside-click and desktop-resize closure for mobile navigation.
- Localized Compare labels and narrow-screen containment.
- Visible keyboard focus and minimum interactive target sizing.
- Bilingual Data source directory built from the current controlled source-reference map.
- Source metadata firewall: **6** display-ready cards, **142** locator-only public records, and **1** no-public-locator dependency withheld from standalone rendering.

## Reference archive challenge

The newly populated `99_REFERENCE_ARCHIVE_INBOX__NON_PRODUCTION` was inventoried and challenged rather than promoted. Narrative dispositions are in `docs/S01_REFERENCE_CHALLENGE.md`; the exhaustive 70-item file register is `docs/S01_ARCHIVE_DISPOSITION_REGISTER.json`; substantive candidates are isolated in `docs/S06_ARCHIVE_EVIDENCE_CHALLENGE_QUEUE.md`.

Useful implementation principles were recovered where they did not change controlled meaning. Old route/runtime/design authorities were rejected. Factual/source/rights candidates were quarantined for Master-led challenge rather than copied into production.

Two newly uploaded archive workbooks were explicitly prevented from becoming accidental authority:

- `Yemen_Financial_Inclusion_Evidence_Master_FINAL.xlsx` → SHA-256 `91ed6906e46a3fe85c65b07b5068af067e510aff693d4fcb2d7cda354a8d5a26`
- `YFSI_Master_Enterprise_Suite_v7.0_Ultimate.xlsx` → SHA-256 `125112029a60c3b03e09614aa0cb9ff8cf4ef850f87932bc7b9ec0b00178d64e`

Neither matches the controlled Production Master hash `d8db3b4ee7ffbba0ca1cfb2843949a2ee323ac0a8a5396c273ebf4a4cc427fee`; both remain non-production challenge/lineage material.

### Archive completeness baseline

- Current archive top-level items reviewed: **70**.
- Two authority-looking workbooks fail the controlled Master hash check and are quarantined.
- Generated `evidence.zip` inspected: **330 entries; CRC clean; lineage only**.
- Archived CauseWay logo matches the production asset byte-for-byte.
- Synthetic econometric/route payloads are explicitly rejected as production input.
- New research/source propositions are queued for S06 and **did not change S01 public content**.

## Verification after final S01 reconciliation

- Controlled Page Specs: **141**
- Generated HTML documents: **284**
- Public search records: **417**
- Controlled source-reference records: **149**
- Publicly addressable source records: **148**
- Display-ready source cards: **6**
- Locator-only public records: **142**
- No-public-locator dependencies: **1**
- Repository validator: **ERRORS=0 · WARN=0**
- JavaScript syntax: **PASS**
- Python syntax: **PASS**
- Local HTTP smoke: **PASS**
- Prohibited public-Arabic regression scan: **0 hits**
- Production Master authority hash: **unchanged**
- Canonical Drive root contains no generated `dist/` tree and no duplicate S01 controls.

## Open issues carried forward

- **S02:** audience journeys, sitemap/route-purpose challenge and Counterfactual Deletion Test.
- **S03:** domain-page density, page-family composition and progressive disclosure.
- **S04:** citation/rights/download/corrections experience and source-reference closure from the user perspective.
- **S05/S08:** real-browser RTL/mobile, zoom/reflow, keyboard, screen-reader and accessibility acceptance.
- **S06:** source-owner/Master adjudication of factual candidates surfaced by the archive, including new literature-synthesis claims that conflict with or go beyond current controlled state.
- **S07:** external-font/network dependency, performance, privacy/security and deployment acceptance.

## Decision

**S00 COMPLETE. S01 COMPLETE. Next: S02 — Audience Journeys & Information Architecture.**

S01 improves the implementation baseline; it does **not** certify the live public release.
