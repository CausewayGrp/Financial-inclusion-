# S04.1 — Evidence Records + Discovery / Verification Journey — CLOSED

## Exact achievement

Evidence Records are now a deliberate bilingual verification page family rather than generic governed-object cards. The closed journey is:

**Domain Answer → selected Evidence Record → original source / Data source record → related interpretation**, with equivalent entry from Global Search, a cold direct deep link, and Data/source.

## User task solved

An unfamiliar user can establish, on first reading where controlled: what the evidence is, what it establishes, definition, universe/base, period/currentness, material limitation, original-source path, and where to return for interpretation. Method, change-trigger and verification guidance remain progressively available without hiding a material boundary.

## Files / routes changed

- `scripts/build.py`
- `scripts/validate.py`
- `site-src/styles.css`
- `site-src/content/presentation_priority.json`
- `site-src/content/page_specs.json` — regenerated controlled projection after Master correction
- `site-src/content/content/search_index.json` — regenerated affected search projection after Master correction
- Existing controls reconciled: `README.md`, `docs/AUTHORITY.json`, `docs/HANDOFF_STATE.json`, `docs/PROGRESS_INVENTORY.json`, `docs/REPOSITORY_BUILD_SUMMARY.json`, `docs/REVIEW_LEDGER.json`, `docs/SESSION_EXECUTION_PROTOCOL.md`, `docs/CHANGELOG.md`
- `SHA256SUMS.txt`
- All 108 `/evidence/<object>/` routes in Arabic and English use the Evidence Record family.

## Canonical Presentation Contract

The existing `site-src/content/presentation_priority.json` was extended, not duplicated. `populated_families` now includes **Domain Answer** and **Evidence Record**. The Evidence Record family contract contains controlled **field references only** for PRIMARY / SUPPORTING / PROGRESSIVE / LINKED / UTILITY depth. It contains no evidence numbers, claim prose, universes, denominators, source authority, rights or publication-state semantics.

`build.py` consumes the Evidence Record family contract directly. `validate.py` rejects contract/renderer divergence and any unsupported field promoted into the presentation contract.

## What became more true

- A public Evidence Record is no longer a generic card dump.
- Scope/currentness and limitation travel with the evidence before progressive detail.
- Source navigation respects the existing S01 publication-state firewall.
- Data/source surfaces expose dependent public Evidence Records without exposing no-public-locator dependencies.
- The Production Master remains semantic/evidence authority.

## What became more usable

- No internal-ID knowledge is required to move through the four verification entry paths.
- Domain verification links lead to records that can be understood cold.
- Search evidence results resolve directly to the same bilingual record family.
- Source records now provide progressive links to dependent Evidence Records.
- Related interpretation/backtracking is explicit on each Evidence Record.

## Removed / demoted / merged

- Removed the Evidence Record dependency on generic `governed_blocks()` presentation.
- Evidence Record Page Spec reading guidance is no longer rendered as an equal first-load section; it sits under native progressive disclosure.
- No new source directory, registry, citation system or second presentation authority was created.

## New complexity

One additional page-family renderer and CSS family were added. Complexity is bounded by the existing canonical presentation contract and validator checks. No new runtime dependency was added.

## Hard-case acceptance sample

All eight sampled live objects passed **ENTRY → COMPREHENSION → SCOPE → BOUNDARY → SOURCE → RELATED CONTEXT → BACKTRACK → AR/EN EQUIVALENCE**:

| Evidence class | Live object | Route |
|---|---|---|
| Representative population survey | `CLM-001` | `/evidence/CLM-001/` |
| Bounded / denominator-sensitive firm survey | `CLM-005` | `/evidence/CLM-005/` |
| Programme KPI | `CLM-060` | `/evidence/CLM-060/` |
| Administrative payments series | `CLM-003` | `/evidence/CLM-003/` |
| Provider roster / status | `CLM-009` | `/evidence/CLM-009/` |
| Reform / regulatory state | `CLM-011` | `/evidence/CLM-011/` |
| Remittance observation / estimate / projection state | `CLM-007` | `/evidence/CLM-007/` |
| Derived / visual evidence object | `VIS-EVIDENCE-CLASS-LADDER` | `/evidence/VIS-EVIDENCE-CLASS-LADDER/` |

## Four entry paths

1. **Domain start — PASS:** People, Firms, Payments, Providers, Reforms and Remittances sampled verification links resolve to the intended Evidence Record; the record links back to its governed public interpretation route.
2. **Global Search start — PASS:** all 108 Evidence Record routes remain discoverable through the controlled public search payload; sampled records resolve in Arabic and English.
3. **Cold deep link — PASS:** first-load DOM order is identity/establishes → definition/universe/period/currentness → material limitation → source/verification → related interpretation; method/verification detail follows progressively.
4. **Data/source start — PASS:** public source records expose dependent Evidence Records; Evidence Records link to the focused `/data/?source=<ID>#source-<ID>` record and original locator when permitted.

## Source / publication safety

- DISPLAY_READY behavior remains bounded to controlled display metadata.
- LOCATOR_ONLY records expose only the controlled stable source reference and original locator; no bibliography was invented.
- The single source dependency without a public locator remains absent as a public source link and receives no Data/source dependent-navigation block.
- Internal source-state and rights-state labels remain absent from public Evidence Record HTML.

## Master escalation — RESOLVED IN SESSION

S04.1 first-load rendering exposed a controlled Arabic public-language defect in `CLM-060`: the governed `definition_ar` contained the prohibited backend-style term `المقام`.

The defect was not patched in `build.py` or the presentation contract. It was repaired **Master-first** in:

`Yemen_Financial_Inclusion_Evidence_Master.xlsx` → `06_EVIDENCE_OBJECTS!I112`

from:

`وثائق المقام`

to:

`وثائق قاعدة الاحتساب`

The affected Page Spec and public-search projections were regenerated. Production Master SHA-256 changed from:

`d8db3b4ee7ffbba0ca1cfb2843949a2ee323ac0a8a5396c273ebf4a4cc427fee`

to:

`6c0f8f18325b4f117de82e8ac8396c70adf0b3f1871878cf614ed01833ea40fd`

The Drive file ID remains `1xAbdDHJd5bYo0Pzo_a6dR6HsZ056LzJU`.

## Regression / validation

- 141 controlled Page Specs → 284 HTML documents.
- Validator: `ERRORS=0`, `WARN=0`, PASS.
- Python syntax: PASS.
- JavaScript syntax: PASS.
- S03 eight-route regression remains PASS.
- All 108 Evidence Record AR/EN routes resolve.
- First-load boundary, source filtering, backtrack targets, search routes and Data/source dependency links are machine-checked.
- Local HTTP smoke: PASS on representative Evidence, Data/source and Domain routes.
- Reference archive unreviewed inbox: EMPTY / NO NEW DELTA.

Browser screenshot automation was blocked by the execution environment administrator. S04.1 therefore does **not** claim deployed-browser, screen-reader, zoom/reflow, contrast or final accessibility acceptance; those remain later S05/S08 gates. The S04.1 AR/EN acceptance is based on generated first-hand HTML hierarchy/content parity, deterministic route/source tests and local HTTP smoke.

## Open defects / boundary decision

No unresolved S04.1 material defect. No S04.2 work was executed. Full Compare legitimacy, citation/rights/redistribution, correction/version and complete Source Reference Closure acceptance remain assigned to S04.2.

**Boundary decision: PROCEED to S04.2.**
