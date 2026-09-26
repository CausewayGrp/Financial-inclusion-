# S05.1 — Arabic/English semantic + typographic QA closure

**Session state:** CLOSED / PASS  
**Boundary decision:** S05_1_PROCEED_TO_S05.2  
**Production Master SHA-256:** `6c0f8f18325b4f117de82e8ac8396c70adf0b3f1871878cf614ed01833ea40fd`  
**Controlled Page Specs SHA-256:** `c5a39b072aaea7438c5146476e6923411503d066acb75e2dbf88bd8b99222fb1`

## Exact achievement

S05.1 verified and corrected the bilingual presentation layer so Arabic and English remain co-authoritative implementations of the same controlled evidence while preserving native RTL/LTR reading behavior. No fact, number, unit, universe, denominator, geography, period, source authority, rights state, evidence class or publication state was changed in website code.

The session changed only implementation/typographic behavior and deterministic bilingual validation. The Production Master and controlled Page Specs remain semantic/evidence authority and are unchanged in S05.1.

## User task solved

A reader can move between Arabic and English on the same route without losing route/query/hash context, read stable Latin identifiers and source locators without RTL reordering, and encounter Arabic public UI labels rather than accidental English implementation metadata. Material evidence numbers and safety boundaries remain present in both editions.

## Files changed

- `scripts/build.py`
- `scripts/validate.py`
- `site-src/styles.css`
- `README.md`
- `docs/CHANGELOG.md`
- `docs/PROGRESS_INVENTORY.json`
- `docs/HANDOFF_STATE.json`
- `docs/REPOSITORY_BUILD_SUMMARY.json`
- `docs/REVIEW_LEDGER.json`
- `docs/SESSION_EXECUTION_PROTOCOL.md`
- `docs/S05_1_BILINGUAL_SEMANTIC_TYPOGRAPHIC_CLOSURE.md`
- `SHA256SUMS.txt`

`site-src/app.js`, `site-src/content/page_specs.json`, the Canonical Presentation Contract and the Production Master were not changed.

## What became more true

1. **Mixed-script identifiers no longer depend on ambient RTL direction.** Evidence IDs, Reading IDs, measurement priority IDs, source IDs and source URLs are isolated as LTR tokens with bidi isolation.
2. **Arabic source metadata chooses its own bidi paragraph direction.** Mixed Arabic/English publisher and source-title strings use automatic/plaintext direction instead of inheriting a potentially misleading sequence.
3. **Arabic Measurement Agenda cards no longer expose English taxonomy labels as UI.** The existing controlled domain classification is rendered through a bounded Arabic interface-label map; the underlying controlled domain value is unchanged.
4. **Arabic Reading visuals no longer expose English-only implementation metadata pills when no governed Arabic equivalent exists.** The localized governed accessible summary remains the public carrier of material meaning; no translation or evidence value is invented in the renderer.
5. **Language switching preserves the equivalent route, query string and fragment.** This pre-existing behavior is now part of deterministic S05.1 regression.

## What became more usable / simpler

- Stable IDs remain visually readable inside RTL sentences and cards.
- Long mixed-script source titles and URLs are less likely to reorder punctuation or identifiers.
- Arabic Measurement cards read as Arabic rather than as Arabic content with English classification fragments.
- Reading visuals no longer present English-only metadata as though it were a native Arabic label.

No second bilingual content store, localization registry or semantic authority was created.

## Removed / demoted / merged

- Removed accidental first-load English visual metadata from Arabic Reading pages when no governed Arabic equivalent exists.
- Removed accidental English Measurement-domain UI labels from Arabic cards by rendering bounded Arabic UI labels from the existing classification.
- No controlled evidence content was removed.

## New complexity

A small implementation-only Arabic label map exists for Measurement Agenda domain taxonomy, and stable-ID bidi isolation is now explicit in generated markup/CSS. This does not carry facts or evidence semantics and is validator-enforced.

## Semantic-invariance sample

Representative live coverage included 21 routes spanning the active page families and hard evidence classes:

- Orientation: Home, Explore
- Domain Answer: People, Firms, Payments, Providers, Reforms
- Evidence Record: `CLM-001`, `CLM-005`, `CLM-060`, `CLM-003`, `CLM-009`, `CLM-011`, `CLM-032`, `VIS-EVIDENCE-CLASS-LADDER`
- Comparison: `/evidence/compare/`
- Reading: `/readings/same-year-different-number/`
- Measurement: `/measurement/`
- Reference / Trust: `/data/`, `/methodology/`, `/corrections/`

For the sample, checks covered numbers, period/currentness, universe/base, limitation/non-inference, evidence/source state where visible, and equivalent route structure. Representative numeric signatures are now validator-enforced for Home, People, Firms, Payments, Providers, population evidence, programme KPI evidence, remittance-vintage evidence and the hard-case Reading.

## Typography / RTL inspection

A local render harness inspected all 21 sampled routes in:

- Arabic 390px
- Arabic 1440px
- English 390px
- English 1440px

Total: **84 rendered route/language/viewport cases**.

Result:

- 84/84 one meaningful `h1`
- 84/84 correct `lang` + `dir`
- 84/84 no page-level horizontal overflow
- 0 unstable sampled identifier-direction findings
- Arabic source/ID and Measurement-label corrections visibly present

This is not S05.2 screen-reader/200%-zoom/keyboard acceptance. Those remain the next bounded session.

## Validator additions

`validate.py` now deterministically checks:

- bilingual page titles;
- AR/EN localized section-order parity;
- exactly one `h1` on every generated locale page;
- one-sided localized public fields across claims, evidence objects, visuals, Readings and measurement priorities;
- representative cross-language numeric signatures;
- no English-only visual implementation metadata leakage on Arabic Reading pages;
- no untranslated Measurement-domain classification in Arabic UI;
- LTR bidi isolation for stable identifiers;
- language switch preservation of equivalent route + query + fragment;
- presence of this S05.1 closure control.

Subjective editorial quality remains human-reviewed rather than encoded as a fake deterministic test.

## Build / regression result

- Clean build: **284 HTML documents from 141 controlled Page Specs**
- Validator: **ERRORS=0 / WARN=0 / PASS**
- Python syntax: **PASS**
- JavaScript syntax: **PASS**
- S03 eight-route Domain Answer regression: **PASS**
- S04 Evidence/Compare/source/citation/publication regression: **PASS**
- Controlled Page Specs: unchanged (`c5a39b072aaea7438c5146476e6923411503d066acb75e2dbf88bd8b99222fb1`)

## Archive delta

`99_REFERENCE_ARCHIVE_INBOX__NON_PRODUCTION/01_NEW_INPUTS__UNREVIEWED` was checked at S05.1 execution and was **EMPTY**. No archive material was promoted.

## Master escalation

**NONE.** No S05.1 finding required a semantic/evidence/source/rights/publication correction in the Production Master. Master hash remains `6c0f8f18325b4f117de82e8ac8396c70adf0b3f1871878cf614ed01833ea40fd`.

## Open defects / boundaries

- `R-007` remains open for S05.2/S08: actual keyboard, screen-reader, 200% zoom/reflow and full accessibility acceptance are not yet complete.
- `R-042` remains an open release blocker for S07: the canonical Drive folder still has an anyone-with-link writer grant. S05.1 does not change collaboration permissions.
- External web-font delivery remains a later S07 release/performance/privacy decision.

## Boundary decision

**S05_1_PROCEED_TO_S05.2**
