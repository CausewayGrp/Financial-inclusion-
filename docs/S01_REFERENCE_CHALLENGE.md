# S01 Reference Archive Challenge

**Archive:** `99_REFERENCE_ARCHIVE_INBOX__NON_PRODUCTION`  
**Decision owner:** current website production repository  
**Authority rule:** nothing in the archive becomes production truth because it is newer, technically richer, visually stronger, or labelled “FINAL”, “Ultimate”, “Master” or “Flagship”. The Production Master identified in `docs/AUTHORITY.json` remains the sole semantic, evidence, source, rights and publication-state authority.

## What was reviewed

The full current top-level archive inventory was reviewed: **70 items** spanning predecessor workbooks, research syntheses, source/custody audits, JSON data shards, visual contracts, prompts, old implementation/code, generated outputs, design tokens, trust/legal drafts, QA files, diagrams and prior ZIP handoffs. The file-by-file decision record is `docs/S01_ARCHIVE_DISPOSITION_REGISTER.json`.

The review did not use filename recency as a quality signal. Each item was tested for: user value; implementation/design value; semantic conflict; source/rights risk; duplication; and whether production would still work if the archive disappeared.

## Authority-collision results

Two authoritative-looking archive workbooks were hashed and explicitly quarantined:

| Archive workbook | SHA-256 | Decision |
|---|---|---|
| `Yemen_Financial_Inclusion_Evidence_Master_FINAL.xlsx` | `91ed6906e46a3fe85c65b07b5068af067e510aff693d4fcb2d7cda354a8d5a26` | Not current authority. |
| `YFSI_Master_Enterprise_Suite_v7.0_Ultimate.xlsx` | `125112029a60c3b03e09614aa0cb9ff8cf4ef850f87932bc7b9ec0b00178d64e` | Not current authority. |

Controlled Production Master SHA-256: `d8db3b4ee7ffbba0ca1cfb2843949a2ee323ac0a8a5396c273ebf4a4cc427fee`.

Several archived launcher/build prompts also point to stale package paths or a different Master hash. They therefore cannot operate the current repository even when individual principles are sensible.

## What S01 actually took from the archive

Only implementation-safe lessons were re-authored, never copied as authority:

- Arabic-aware search normalization;
- deny-by-default/no-invention source rendering for locator-only records;
- meaningful bilingual 404 recovery;
- the distinction between implementation-handoff readiness and live-release readiness;
- screenshot/quotation safety as a review lens;
- first-use hierarchy: answer/question first, deeper verification progressively disclosed;
- anti-dashboard/card-wall challenge; and
- the principle that a negative evidence finding is only as strong as the documented places searched.

The current repository does **not** depend on archived code, JSON shards, prompts, ZIPs or generated HTML.

## Valuable material deferred — not promoted

Three research/custody documents are materially useful as challenge inputs: `Financial Inclusion in Yemen — A Critical Review of the Evidence 1995–2026`, `YFSI Evidence Synthesis v1.1 — Session 2 Delta`, and `YFSI Corpus Inventory v1.0 — 46 items A–Z`. They surface candidate questions about Findex precision and routing, OECD/INFE coverage, exchange-rate construction, humanitarian payment rails, banking-series coverage, duplicates, publisher identity and rights.

Those candidates are now isolated in `docs/S06_ARCHIVE_EVIDENCE_CHALLENGE_QUEUE.md`. **No public number, claim, rights state, source identity or evidence wording changed from them in S01.**

The citizen-journey prototypes and older design prompts also contain useful UX ambitions — plain-language user tasks, calm progression, differentiated page families and Arabic-first composition — but their facts, calculators, old route model, palette and framework assumptions are not imported. They remain S02/S03/S05 challenge material.

## Material explicitly rejected

The review rejected as current production input:

- the obsolete 29-route / Next.js / Tailwind architecture;
- the old Citizen/Expert global-mode architecture;
- old navy/teal/gold + Cairo/Inter visual tokens as design authority;
- universal KPI-card page templates;
- `econometric_models_spec.json` synthetic indices/causal outputs;
- `routes_manifest.json` and archive shards containing non-current or unsupported metrics;
- blanket CC BY treatment that conflicts with source-level rights distinctions; and
- predecessor implementation PASS manifests as evidence of current browser/accessibility/runtime acceptance.

## Generated/archive package result

`evidence.zip` was inspected as a generated predecessor output: **330 ZIP entries, CRC clean**, dominated by generated Evidence routes and macOS metadata. It is not a source tree and is not needed by production. Prior website/handoff ZIPs and `site-data.js` are also lineage/regression material only.

The archived CauseWay logo was independently checked and is byte-identical to the current production asset; no asset replacement is required.

## Counterfactual deletion test

If the entire `99_REFERENCE...` folder disappeared, the production repository would still build and retain every accepted S01 improvement. That is intentional. The archive can challenge production; production never depends on the archive.

## S01 decision

**REVIEWED — NO BLIND PROMOTION.** Archive review is complete for the current 70-item top-level inventory. S01 integrates implementation-safe lessons, quarantines substantive candidates for S06, and rejects stale/unsafe architecture and analytics. The archive remains available for future challenge without becoming a parallel source of truth.
