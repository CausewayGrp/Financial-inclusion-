> **HISTORICAL_LINEAGE — KEEP.** This baseline records the S00–S06 state of 2026-09-23 and is not current. Current state: `README.md`, `authority/YFI_CURRENT_PROJECT_CONTEXT.json`, `OPENAI_REENTRY_CHECKPOINT.md` (classification: `audit/P4_CANONICAL_HANDOFF_ALIGNMENT.md`).

# Website Repository Verification Baseline

## Current controlled baseline

- Product: **Yemen Financial Inclusion Evidence / أدلة الشمول المالي في اليمن**.
- Canonical repository: Google Drive folder `1iAxWukk1xeAXDPibmXXwGlaUXDcr_XvA`.
- Sole Production Master: `authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx` (Drive ID `1xAbdDHJd5bYo0Pzo_a6dR6HsZ056LzJU`).
- Production Master SHA-256: `f94f1f91084b01964a3bb7b3847fd68a19555cc901ab6078146a187efe17e860`.
- Controlled Page Specs SHA-256: `4e8a0d8f0cf58f78389360c69cf04f3bf0d24f1ba9b3e4ef10ebe93461e69f1a`.
- Runtime model: **static-first, fully local governed payloads**. The Master is retained in the repository as authority but is neither parsed by the browser nor copied into the public `dist/` bundle.
- Controlled public projection: **141 Page Specs**, generated in Arabic and English.
- Post-build maturation: **S00–S06 complete; Window 3 and S06 recipient-side acceptance are accepted; S07/S08 are NOT STARTED.**

## Current repository verification

A clean deterministic rebuild and validation after S06 recipient-side reconciliation establishes:

- **284 generated HTML documents** from the 141 controlled Page Specs.
- Repository validator: **ERRORS=0 · WARN=0**.
- JavaScript syntax: **PASS**.
- Python build/validator syntax: **PASS**.
- Public search records: **418**.
- Evidence objects: **108**.
- Controlled public claims: **59**.
- Evidence passports: **55**.
- Controlled visuals: **36**.
- Readings: **10**.
- Indicators: **216**.
- Controlled source-reference records: **150**; **149** publicly addressable; **6** display-ready; **1** no-public-locator dependency withheld from standalone public rendering.
- The only `.xlsx` under the canonical source repository is the authority Master; **no workbook is emitted into `dist/`**.
- S05.3 deterministic invariants require visible ordered-text fallbacks, image-independent meaning and non-colour semantics for governed visuals.
- Earlier S05 runtime evidence remains a regression record; named screen-reader application testing, browser-chrome zoom, final contrast and deployed-environment accessibility acceptance remain reserved for S08.1.

## Repository-truth reconciliation

The S05.3 hygiene pass detected and corrected a partial cross-window integration state: closure prose and validation expectations had advanced while `build.py` and several current controls still reflected the previous boundary. The current control stack, build generator, validator, Page Specs and live Master now point to one state. Historical closure records retain the hashes and session states that were true when those sessions closed and are not current authority.

## Open release boundary

This file verifies the **current repository baseline**, not final public-release certification. The following remain outside this baseline:

- **R-042:** the canonical Drive repository/authority currently has an anyone-with-link **writer** permission. This must be restricted and re-verified before release certification.
- S07 technical release/security/privacy/deployment acceptance.
- S08 named assistive-technology/adversarial final acceptance and named release approval.

No public release-ready claim is made until those gates close.
