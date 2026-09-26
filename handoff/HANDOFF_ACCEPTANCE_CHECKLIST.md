# Handoff Acceptance Checklist

Use this checklist as a gate, not as narrative documentation.

## Authority and concurrency

- [ ] Production Master path/ID/hash re-read from live repository before design/code start.
- [ ] Page Specs hash re-read and embedded authority hash matches current Master.
- [ ] No predecessor workbook or external draft treated as production truth.
- [ ] No temporary, scratch or unreviewed artifact (outside `authority/`, `site-src/`, `scripts/`, `handoff/` and `design/`) is being relied on.

## Product identity and institutional posture

- [x] Home and About use one stable public definition of the product.
- [x] Decision support is bounded to clarifying evidence; the product does not choose policy or simulate outcomes.
- [x] CauseWay is presented as developer/maintainer/synthesiser, not regulator, statistical authority or source owner.
- [x] No public positioning uses sovereign architecture, institutional-authority proof, exclusive-capability or neutrality claims.

## Content completeness

- [ ] Every controlled Page Spec is present (143 at the time of writing; `page_specs.json` decides).
- [ ] All public copy is consumed from controlled local projections; no hand-authored shadow copy in components.
- [ ] Every Evidence Record remains addressable (110 at the time of writing).
- [ ] 10 Readings and 10 Measurement priorities remain represented.
- [ ] 160 source records remain controlled; 151 expose a public original locator, and the 9 without one are never named or linked on public pages (validator S04.1/S04.2).
- [ ] 27 curated report/reference cards remain distinct from the full source-locator register; third-party reports are not republished without controlled redistribution permission.
- [ ] 24 chronology events remain presented as dated system context/state, never as an automatic causal chain.
- [ ] Search index remains local (435 controlled public-search records at the time of writing), all public results resolve, and the canonical probe (`scripts/search_canonical_probe.json`) still passes.

## Design handoff

- [ ] `design/00_DESIGN_README.md` through `design/10_ACCEPTANCE_CHECKLIST.md` exist.
- [ ] Final tokens are machine-readable.
- [ ] Every major component has anatomy, states, inputs, accessibility and RTL/LTR behavior.
- [ ] Every page family has deterministic module order/composition rules.
- [ ] 320, 390/400, 640 and 1440 behavior is specified.
- [ ] Visual/table fallback and non-colour behavior is specified.
- [ ] Every SIGNATURE/CORE visual follows its data contract in `site-src/content/visuals/visual_design_contracts.json` (tier, bound rows, grammar states and markers, governed legend labels, detached frame, RTL/mobile form); TABLE_TEXT_FIRST and RETIRE_FROM_DESIGN visuals are not drawn; open release blockers are listed there.
- [ ] Evidence Records show the boundary as two labelled parts (does not establish · limits of the measure) and never print the internal delimiter.
- [ ] No consequential decision exists only in a screenshot/Figma frame.

- [ ] The 11 page families are explicitly mapped to reusable composition rules rather than bespoke per-route layouts.
- [ ] Search, Evidence discovery, Compare, Source/Resource filtering, Cite, Language and Correction have default/loading/empty/error/focus/shareable-state behavior.
- [ ] Compare encodes 2–4 evidence IDs in shareable URL state and shows comparability boundaries before values.
- [ ] A technical failure state cannot be mistaken for missing/zero evidence.
- [ ] Hard-state acceptance covers dense, sparse, conflicted, revised, long-form, source-scale and Arabic-mobile cases.

## Bilingual invariance

- [ ] Arabic and English are generated from the same stable objects and release state.
- [ ] Number, unit, universe/denominator, geography, period/currentness, method, authority, certainty, limitation, rights and measurement-next meaning do not drift between editions.
- [ ] Arabic is natively composed; no mechanical visual mirroring or English syntax dependency.
- [ ] Stable IDs, source IDs, URLs, Latin acronyms, dates and numbers remain readable in RTL through bidi isolation.
- [ ] No internal-control terminology or unintended English prose leaks into Arabic public copy.
- [ ] Language switching preserves route/object/query/hash state.

## Missing controlled content

- [ ] Missing/contradictory substantive fields produce `NEEDS_CONTROLLED_CONTENT` with stable IDs rather than invented copy/data.
- [ ] Semantic defects produce `ESCALATE_TO_MASTER`; no JSX/JSON/CSS shadow truth is introduced.

## Code handoff / implementation

- [ ] One final React static runtime; no competing production renderer remains.
- [ ] Two localized route documents per Page Spec (286) + root + 404 are generated.
- [ ] Core runtime requires no Drive/database/CMS/API.
- [ ] Final fonts are bundled locally; no required Google Fonts/CDN request.
- [ ] Production Master is absent from public output.
- [ ] Internal links, deep links, language switch and search resolve.
- [ ] Arabic RTL and English LTR are structurally correct.
- [ ] Keyboard/focus/menu/search/Compare/table-scroll paths pass.
- [ ] Visual meaning survives image-off and colour loss.
- [ ] Source/citation/rights/publication filters pass.
- [ ] Validator and syntax/test suites pass with zero unexplained errors.
- [ ] `SHA256SUMS.txt` covers every canonical repository file and excludes generated `dist/` and temporary scratch.

## Release boundary

- [ ] Handoff completion is not mislabeled as public release readiness.
- [ ] R-042 permission blocker is closed before release certification.
- [x] S06 source-owner challenge and recipient-side acceptance are disposed (`S06_WINDOW_ACCEPTED`).
- [ ] S07 technical/security/privacy/release engineering is disposed.
- [ ] S08 named assistive-technology/adversarial final acceptance is disposed.
