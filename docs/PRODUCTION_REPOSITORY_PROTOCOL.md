# Production Repository Protocol

This Google Drive folder is the single working website repository for **Yemen Financial Inclusion Evidence / أدلة الشمول المالي في اليمن**.

## Authority

- The Production Master at `authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx`, identified in `docs/AUTHORITY.json` by Drive ID and SHA-256, remains the sole semantic, evidence, source, rights, controlled-product-state and publication-state authority.
- This repository is the sole website implementation workspace for the current review/build programme.
- The sibling `99_REFERENCE_ARCHIVE_INBOX__NON_PRODUCTION` (Drive ID `1kQwClKkfkl4FEsgk8YSb_5FPrcatRDby`) is challenge/recovery material only. Drafts, predecessor workbooks, mockups, old exports, research notes and prior AI/developer outputs do not become production truth because they are newer, larger, more detailed or labelled “final”.
- All new reference material must enter through `01_NEW_INPUTS__UNREVIEWED` (Drive ID `1lj5A9hrCDHo7hhQTlLOk-fmIQ7xCfcLs`). Do not create another sibling repository, archive or folder labelled `final`, `master` or `authoritative`. The current registered supplement is Drive folder `1tFewVNnzpNXG9tsNyFpoWHnobaKsoRho` and remains non-authoritative until S06 disposition.

## Editing rule

- Work directly in this repository. Do not create competing website repositories, numbered finals, parallel Drive branches or ZIP-based working copies.
- Every material repository edit must be recorded in `docs/CHANGELOG.md` and, where relevant, `docs/REVIEW_LEDGER.json`.
- Implementation, navigation, accessibility, performance and rendering may be improved here.
- Any material correction to evidence, claim meaning, source state, rights, denominator, geography, period, comparability or publication state must be fixed in the Production Master first and then regenerated into this repository.
- Completed review work is closed by inventory. Reference/archive items recorded in the S01 baseline are not re-reviewed by default; only new/modified archive items or a specific defect-triggered challenge reopen them.

## First-hand source rule

The canonical Drive repository stores the Production Master under `authority/` plus first-hand implementation inputs: source code, controlled projections, documentation, validation scripts, assets and checksums. `98_TEMPORARY__NONAUTHORITATIVE/` is scratch-only and must never become an authority or handoff dependency. `dist/` is deterministic generated output and is **not canonical Drive state**. Generate a fresh local deployment tree with `npm run verify` before preview or deployment.

## Handover rule

Other AIs, developers and reviewers should consume this folder first. They should not reconstruct the project from archive ZIPs, screenshots, old prompts or predecessor workbooks.

## Release rule

Do not call the product live or release-ready until browser/runtime, RTL/mobile, accessibility, publication filtering, security/privacy, correction/version behaviour and named release approval are complete for the claimed release state.

## Concurrency rule

Before every material write, re-read the live target. Any unexpected newer modification is a concurrency event: reconcile the newer state first and do not restore an older state merely to match a stale control hash.
