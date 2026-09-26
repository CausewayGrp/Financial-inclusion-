# S05.2 — Mobile + keyboard + zoom + screen-reader structure closure

**Session state:** CLOSED / PASS  
**Boundary decision:** S05_2_PROCEED_TO_S05.3  
**Production Master SHA-256:** `6c0f8f18325b4f117de82e8ac8396c70adf0b3f1871878cf614ed01833ea40fd`  
**Controlled Page Specs SHA-256:** `c5a39b072aaea7438c5146476e6923411503d066acb75e2dbf88bd8b99222fb1`

## Exact achievement

S05.2 corrected constrained-screen and keyboard interaction defects and strengthened deterministic assistive structure without changing controlled evidence semantics. The Production Master, controlled Page Specs and Canonical Presentation Contract are unchanged.

## User task solved

A keyboard or narrow-screen reader can reach primary navigation, search, citation/report utilities, progressive evidence detail, comparison controls, Data/source focus, corrections backtracking and language switching without semantic content disappearing. Compare now exposes a concise live verdict status and a separately named keyboard-scrollable table region rather than announcing the whole result as a live region.

## Files changed

- `scripts/build.py`
- `scripts/validate.py`
- `site-src/app.js`
- `site-src/styles.css`
- `README.md`
- `docs/CHANGELOG.md`
- `docs/PROGRESS_INVENTORY.json`
- `docs/HANDOFF_STATE.json`
- `docs/REPOSITORY_BUILD_SUMMARY.json`
- `docs/REVIEW_LEDGER.json`
- `docs/SESSION_EXECUTION_PROTOCOL.md`
- `docs/S05_2_MOBILE_KEYBOARD_ZOOM_SCREENREADER_CLOSURE.md`
- `SHA256SUMS.txt`

No controlled content payload, Page Spec, presentation contract or Production Master file changed.

## What became more true / usable

1. Opening the mobile menu moves keyboard focus into the navigation; Escape closes it and returns focus to the menu control.
2. Citation and report actions remain reachable on narrow screens through explicit mobile-nav utilities even though compact header icons are hidden.
3. Citation/source-copy actions now produce a concise assistive live-status message after successful copying.
4. Language switching names the target language explicitly and retains bilingual direction metadata.
5. Compare uses table captions, row/column header scopes and a named focusable scroll region. The large comparison output is no longer an `aria-live` region; only a concise verdict status is live.
6. The Home three-card trust/verification CTA no longer forces a desktop three-column inline grid at phone widths; it now uses a responsive class. This removed the reproducible 320px page overflow found during S05.2.
7. Existing first-load Domain and Evidence boundaries remain before progressive detail.

## Browser/runtime evidence

A local Chromium harness loaded the generated HTML/CSS/JS directly without relying on deployment hosting. After fixes:

- **44/44** interaction/reflow/AX assertions passed across mobile menu, global search, Domain, Evidence, Data, Compare, Measurement, progressive disclosure and browser accessibility-tree landmarks.
- **20/20** focused keyboard/context/reflow assertions passed for skip-link behavior, citation copy feedback, Data/source query focus, correction backtracking, language-switch metadata and 200%-reflow-equivalent checks.
- **20/20** additional 400px bilingual route checks passed across Home, Explore, dense People, sparse Access, Evidence Record, Data, Compare, Corrections, Reading and Measurement.
- Total explicit S05.2 runtime assertions: **84/84 PASS**.

Reflow testing covered 320px, 390/400px and a 640px CSS viewport used as the reflow equivalent of a nominal 1280px viewport at 200% enlargement. No tested route produced page-level horizontal scrolling; Compare keeps its wide table inside an explicit scroll region.

Keyboard runtime checks proved the skip link, menu focus transfer/Escape return, search focus/close return, Domain/Evidence `<details>` operation, Reading source-control focus, Compare 2/3/4-record operation, mobile citation access, Data source-query focus and corrections backtracking.

Browser accessibility-tree inspection confirmed main/navigation landmarks, heading exposure and named search controls on a representative Evidence Record. This is structural evidence, not a claim that a specific screen-reader application has completed end-to-end acceptance.

## Validator additions

`validate.py` now enforces deterministic S05.2 invariants including:

- exactly one `main#main` and a skip link on every controlled locale page;
- heading levels that do not skip upward by more than one level;
- `details` / `summary` structural pairing;
- named primary navigation and menu state/control relationships;
- mobile fallback citation/report utilities;
- utility live-status feedback;
- named search dialog and live search status;
- Data/source query-focus implementation;
- correction-origin behavior;
- Compare caption, header scopes, named keyboard-scroll region and concise live-status architecture;
- no full Compare output `aria-live` region;
- first-load Domain/Evidence boundaries before progressive disclosure.

## Build / cumulative regression

- Clean build: **284 HTML documents from 141 controlled Page Specs**
- Validator: **ERRORS=0 / WARN=0 / PASS**
- Python syntax: **PASS**
- JavaScript syntax: **PASS**
- S03 Domain Answer regression: **PASS**
- S04 Evidence/Compare/source/citation/publication regression: **PASS**
- S05.1 bilingual semantic/typographic regression: **PASS**

## Defects found and disposition

- **Phone Home overflow:** the Home CTA grid had an inline three-column declaration that overrode responsive Reading-grid behavior. **FIXED** with a responsive `home-cta-grid`; no content change.
- **Mobile utility loss:** citation/report icon controls were intentionally hidden at small widths but had no equivalent reachable action. **FIXED** by adding full-text mobile-nav actions.
- **Menu keyboard path:** opening the mobile menu did not advance focus into the newly exposed navigation. **FIXED**.
- **Compare assistive semantics:** dynamically generated comparison tables lacked caption/header scopes/named scroll region and the entire output was live. **FIXED**.
- **Copy feedback:** clipboard success was visually signalled only by a glyph. **FIXED** with a live-status message.
- **Control-state lag:** the review/progress summary still named S05.1 as the active predecessor after S05.2 runtime closure. **FIXED** by reconciling the existing control stack; no new control document was created.

## Control / Drive reconciliation

The canonical Google Drive repository was updated **in place**, preserving existing first-hand file IDs. The new S05.2 closure artifact was added under the existing `docs/` folder; generated `dist/` and local QA harness outputs were not stored as canonical Drive state. `PROGRESS_INVENTORY.json`, `REVIEW_LEDGER.json`, `HANDOFF_STATE.json`, `REPOSITORY_BUILD_SUMMARY.json`, `SESSION_EXECUTION_PROTOCOL.md`, `README.md`, `CHANGELOG.md` and `SHA256SUMS.txt` now agree on **S05.2 CLOSED / S05.3 NEXT**. The Production Master and controlled Page Specs were not modified.

## Master escalation

**NONE.** No fact, number, unit, universe, denominator, geography, period, source authority, rights state, publication state or controlled semantic meaning changed.

## Archive delta

No S05.2 archive material was promoted. The existing S06 source-challenge queue remains untouched.

## Open boundaries

- An actual named screen-reader application was not available in this execution environment. S05.2 therefore closes **screen-reader structure**, not final assistive-technology certification; final blind-reader/assistive runtime acceptance remains in S08.1.
- Reflow was exercised at the 200%-equivalent CSS viewport rather than through browser-chrome zoom controls. Deployed-browser zoom confirmation remains part of final acceptance.
- Contrast/non-colour/visual fallback is owned by S05.3 and has not been pre-closed here.
- `R-042` remains an S07 release blocker: the canonical Drive production repository still permits anyone-with-link writing.

## Boundary decision

**S05_2_PROCEED_TO_S05.3**
