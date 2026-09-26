# R5 — Evidence Utilization + Resource Library Closure

Status: CLOSED

Production Master SHA-256: `ce552bdbd0e0070866098b28145f9b1dad43f0015679d12cb9235b13d14abf7d`
Page Specs SHA-256: `4e84434436d78c7026c2860409e2564254205c449c156528b4f0065ebaebcce8`

## Material decisions

- Final canonical-consistency pass reconciled the Data route full copy with the reader-facing section copy in the Production Master, removing the last Master↔projection semantic mismatch before Drive synchronization.
- During rendered-page verification, removed an implementation instruction from the public Data chronology copy, replaced internal-looking section labels with reader-facing labels, and restored an Arabic Evidence Hub introduction that had been displaced by stale chronology text. These corrections were made in the Production Master first and then regenerated into projections.
- Corrected the Data route's bilingual count/state rows in the Production Master before regenerating projections.
- Expanded the curated Resource Library only where a source adds a distinct public job: current Yemen strategy/economy/project context, payment-system implementation method, G2P/cash-transfer digitisation, MSME/microfinance programme context, or measurement method.
- Added the World Bank/G2Px Yemen UCT digital-payment pilot as direct Yemen evidence for the intermediate **financial exposure** stage: eight districts, 45,460 recipients, fully functional accounts/recipient choice. The public reading explicitly preserves the boundary: pilot reach/account exposure ≠ persistent active use ≠ national financial-inclusion outcome.
- Added the pilot to the system chronology at its actual 2024 position and linked it to the after-transfer persistence Reading/Evidence Record without widening the claim.
- Current resource scale: 159 source records; 158 public locators; 26 curated public report/reference cards; 24 chronology events; 427 public search records.

## Integrity verification note

Before canonical integration, a final authority-versus-projection check exposed an intermediate workbook defect in which chronology rows had been duplicated while the already-regenerated chronology projection contained the intended 24-event sequence. The projection was not allowed to overrule the Master. The chronology, affected Data/Evidence copy and count fields were repaired in the Production Master first, then the projections were regenerated/reconciled and rebound. The current hash above is the post-repair canonical state; earlier intermediate R5 workbook hashes are superseded and are not valid production authorities.

## Counterfactual deletion decisions

A generic donor-project portal, country-comparison dashboard, or literature catalogue was **not** created. Resources are admitted only where deleting them would remove a distinct interpretation/verification/implementation value. Global references remain method/context references and do not become Yemen evidence merely by inclusion in the library.

## Remaining boundary

R5 closes evidence utilization and curated resource-library composition. It does not certify live runtime release. Final design/static implementation, clean-room repository pruning, runtime/security/privacy/accessibility acceptance and named release approval remain later acceptance work.


## Verification

- Production Master SHA-256: `ce552bdbd0e0070866098b28145f9b1dad43f0015679d12cb9235b13d14abf7d`.
- Controlled Page Specs SHA-256: `4e84434436d78c7026c2860409e2564254205c449c156528b4f0065ebaebcce8`.
- Static build: 141 Page Specs → 282 localized route documents → 284 HTML documents including root and 404.
- Validator: `ERRORS=0`, `WARN=0`, `WEBSITE REPOSITORY VALIDATION PASS`.
- Final controlled counts: 108 Evidence Records; 59 public claims; 55 Evidence Passports; 10 Readings; 10 Measurement Agenda priorities; 36 visual contracts; 159 source records; 158 public source locators; 26 curated resource cards; 24 chronology events; 427 public-search records.

## Next bounded session

R6 — Information design + technical architecture. Convert the now-settled product logic into an inspectable page-family/state/interaction architecture for Claude Design without creating a second semantic authority. Explicitly decide which public tools are static-local, which are progressive enhancement, which visual/state contracts need design prototypes, and what a production-equivalent static handoff must prove before clean-room handoff.
