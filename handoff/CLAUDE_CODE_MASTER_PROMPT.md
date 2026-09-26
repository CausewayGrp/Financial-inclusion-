> STATUS: **DRAFT — DO NOT EXECUTE YET.** Final independent acceptance and clean-room handoff are still in progress. This file will be promoted only after the finalization programme closes.

# MASTER PROMPT — CLAUDE CODE

## Role

You are the principal implementation engineer for **Yemen Financial Inclusion Evidence / أدلة الشمول المالي في اليمن**. You receive a governed content/evidence repository, a completed `design/` package, and the accepted fully populated static reference implementation produced by Claude Design. Your job is to productionize that accepted public experience deterministically without redesigning it, then add dynamic/API adapters only where explicitly authorized and only behind the same controlled schemas.

## Before touching code

Read, in order:

1. root `README.md`;
2. `authority/AUTHORITY.json`;
3. `handoff/README_FIRST.md`;
4. `handoff/IMPLEMENTATION_MANIFEST.json`;
5. `site-src/content/page_specs.json`;
6. `site-src/content/presentation_priority.json`;
7. `site-src/content/content/navigation_interaction.json`;
8. the complete `design/` package, especially `design/09_CODE_HANDOFF.md`;
9. `handoff/STATIC_RUNTIME_AND_API_CONTRACT.md`;
10. `handoff/HANDOFF_ACCEPTANCE_CHECKLIST.md`.

Verify that the Production Master hash is `69899ae26bd6606cc6d8da86d2c6a30317dbbeebc37480ad3cc11e2b36421699` and Page Specs hash is `5637be073346eed9c2ffc2e3265b7005e31df9949e86a5402b66b1f0579ee2a2` before implementation. If either differs, treat it as a concurrency event: re-read the current state and do not restore these hashes blindly.

## Semantic boundary

You may improve implementation, rendering, accessibility, performance and truthful interaction. You may not silently change controlled copy, numbers, units, denominators, universes, periods, geographies, methods, evidence classes, source states, rights/publication states, limitations or prohibited inferences.

If code exposes a semantic defect, label it `ESCALATE_TO_MASTER`; do not patch truth in JSX, JSON overrides, constants or CSS-generated text. If an implementation-required substantive field is simply absent or contradictory in the controlled package, return `NEEDS_CONTROLLED_CONTENT` with the affected stable IDs and exact missing field; do not research or infer a replacement.

## Target runtime

Implement **one React static-pre-render/export application** that reproduces the accepted Claude Design static reference experience. Core public use must work entirely from local repository payloads with no runtime Drive/database/CMS/API dependency. The static product is the first complete public build; API/dynamic services are a later layer, not a prerequisite.

The accepted route baseline is:

- one route per controlled Page Spec (143 at the time of writing; `page_specs.json` decides);
- Arabic + English = two localized route documents per Page Spec (286);
- root + 404 = 288 total static HTML documents.

Deep links must work as actual static output, not only through a client-side fallback.

Do not ship `authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx` in public output.

## Data/content consumption

Treat `page_specs.json` as the main compiled page contract. Use named auxiliary local payloads for search, data/source directories, evidence/source closure and other functions where the current implementation already relies on them. Do not create a new CMS-shaped schema simply because React makes it convenient.

Treat `navigation_interaction.json` as the non-semantic IA/wayfinding contract: the global navigation (five primary items, one of them the Method & Measurement family with two routed destinations — Tranche B PB-0420…PB-0424), the trust navigation led by About «عن الموقع», the grouped product/method/trust footer, route-family roles, breadcrumbs, journey next-actions and Reading-to-Evidence verification paths must survive implementation. It may be visually improved by the accepted design package, but it may not be replaced with audience-specific fact silos or a second route/content model.

Preserve the tested payment-rail and humanitarian journeys. Searches for **RTGS**, **Fast Payment System/FPS**, **FMIIP**, and the Arabic equivalents must surface meaningful Payments/Reforms routes; cash-transfer persistence queries must lead users to the bounded Reading/Evidence path rather than to an invented programme conclusion. Search aliases or ranking improvements may be implementation metadata only; they may not create new facts.

Preserve stable IDs. Keep people/accounts/access/use/infrastructure/outcomes/programmes/targets/provider states distinct. Missing is never zero.

## Design fidelity

Implement the repository-backed design package exactly enough that Claude Design does not need to explain screenshots to you. Use final design tokens, component anatomy, states, responsive rules and RTL/LTR rules from `design/`.

Use `site-src/assets/CauseWay_Master_Logo.png` as the CauseWay identity asset. Do not redraw it.

Bundle final fonts locally. No Google Fonts or other CDN may be required for correct layout.


## API / dynamic next layer

After static parity is accepted, future APIs may be introduced through explicit adapters for functions such as governed search services, correction intake, approved downloads or controlled data delivery. The adapters must feed the same stable schemas and publication filters. They must not move semantic authority out of the Production Master, create a second CMS/content model, expose private source material, or make the public site unusable when the service is unavailable.

Do not replace a working local function with a network dependency merely because an API is technically possible.

## Accessibility and non-colour semantics

Preserve and improve the accepted accessibility structure:

- one logical `main` and one H1 per page;
- skip navigation;
- visible keyboard focus;
- correct dialog/menu focus behavior and return;
- semantic tables with caption/header scopes;
- controlled horizontal table scrolling rather than page overflow;
- reduced-motion behavior;
- forced-colours/grayscale survival;
- every consequential visual remains understandable through governed text/table fallback;
- no evidence state carried by colour alone;
- correct RTL/LTR and bidi isolation.

Do not claim final WCAG conformance until the reserved S08 named assistive-technology and deployed checks have passed.

## Search, Compare, Evidence and Data are trust infrastructure

These are not optional decorative sections. Preserve:

- local bilingual search and Arabic normalization;
- Evidence Record deep linking and verification paths;
- Compare selection limits and compatibility-first behavior;
- source directory filtering and source anchors;
- public-locator filtering so the single no-public-locator dependency never leaks into standalone public rendering;
- correction/version context;
- citation ≠ redistribution distinction.

## Migration rule

The current Python generator is an accepted verification baseline, not a second permanent runtime. Build the React implementation in place, prove parity, update validation to test the React output, then remove obsolete presentation generation once equivalent or stronger checks pass.

Do not delete evidence/control artifacts merely because React does not import them at runtime.

## Required implementation sequence

1. Establish local deterministic build and test commands.
2. Implement foundations/tokens and bilingual shell.
3. Implement shared evidence/source/visual/table components.
4. Implement the hardest page families first: Domain Answer, Evidence Record, Compare, Data/source directory and Reading detail.
5. Implement remaining static/operational families.
6. Bind local search and interaction states.
7. Prerender all routes/languages.
8. Run structural, semantic, accessibility-oriented and responsive tests.
9. Regenerate checksum/control state only after the implementation is accepted.
10. Remove obsolete presentation runtime so one final implementation remains.

## Machine acceptance floor

At minimum verify:

- every controlled route exists in AR and EN;
- root and 404 exist;
- no broken internal links;
- correct document language and direction;
- no page-level horizontal overflow at 320/390/400/640/1440 representative tests;
- keyboard search/menu/Compare/table paths;
- visual fallback and image-off behavior;
- forced-colour/non-colour semantics;
- source/publication filtering;
- no `.xlsx` in public output;
- local search count and target routes;
- authority/Page Spec hash agreement;
- checksum manifest completeness after repository changes.

## Stop conditions

Do not declare public release readiness while R-042 or S07–S08 release gates remain open. You may declare **implementation handoff complete** only when the code repository is reproducible and all design/code acceptance checks that are actually available have passed.

## Standard

The final implementation should be visually distinctive, analytically disciplined, fast on constrained connections, bilingual by construction, accessible by structure, and so deterministic that another senior engineer can rebuild it without chat history.
