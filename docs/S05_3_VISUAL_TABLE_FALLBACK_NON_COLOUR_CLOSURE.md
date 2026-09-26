# S05.3 — Visual/Table Fallback + Non-Colour Semantics Closure

**Decision owner:** Information-design lead  
**Challengers:** Accessibility specialist; data-visualization / skeptical analytical reader  
**Boundary:** `S05_3_PROCEED_TO_S05_ACCEPTANCE`  
**Independent Window 3 decision:** `WINDOW_3_ACCEPTED`

## 1. Authority reconciliation before implementation

S05.3 did not begin from the stale session-control hash. The live Production Master was re-read first. Its current SHA-256 is:

`d3b0421104d63f830cf40d2b1749dc88f302f54e4d79a6c6faf63abc5ad28d9e`

Revision comparison showed that the post-S05.2 Master changes were bounded Arabic terminology corrections around calculation base/denominator language. They did **not** change a value, unit, universe, geography, period, source, rights state, publication state or claim strength. The current live Master was therefore preserved rather than reverted. Dependent projections were synchronized to it before S05.3 acceptance.

The same Master Drive file ID was also found outside the canonical production repository. To remove cross-window ambiguity, that exact live file was moved in place into:

`authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx`

No predecessor workbook was promoted. The Master remains the sole production authority.

## 2. Visual population and Counterfactual Deletion Test

The controlled Page Specs contain **36 unique governed visual contracts**. All 36 carry bilingual title, analytical question, analytical accessible summary and prohibited-inference text.

The current presentation contract deliberately renders **17 unique public visual IDs**: seven domain visuals and ten Reading visuals. The other 19 controlled visual contracts are not forced onto public routes merely because they exist. This is the correct application of the Counterfactual Deletion Test: rendering the additional contracts would add interface burden without a demonstrated material user-value gain, while the contracts remain available to evidence/detail surfaces and future implementation decisions.

For every rendered visual, the public implementation now makes the governed analytical question and bilingual analytical text alternative visible in the document itself. The evidence meaning therefore does not depend on an image, canvas, SVG, hover state or colour encoding.

## 3. Non-colour and image-off semantics

Changes made in S05.3 are presentation/accessibility changes only:

- every rendered governed visual has `data-visual-id` plus a visible `data-visual-fallback="ordered-text"` block with `data-image-independent="true"` and `data-noncolour-semantic="text-structure-label-position"`;
- the fallback carries the governed analytical question, bilingual analytical summary, available scope/time metadata and prohibited-inference boundary as ordered text;
- forced-colours CSS preserves structural borders, focus, links, boundaries and comparison states using system colours;
- Compare states remain written as words and receive an additional non-colour symbol marker;
- status meaning therefore does not depend on teal/gold/background fills;
- removing images leaves the consequential evidence statement, scope, limitation and verification path intact.

No chart was invented merely to satisfy S05.3. The current product is text-led where that is the most truthful representation.

## 4. Table semantics

The material interactive comparison table retains:

- a table caption;
- column and row header scopes;
- a named, focusable horizontal-scroll region;
- a visible bilingual narrow-screen scroll instruction bound with `aria-describedby`;
- explicit textual comparison states (`same`, `different`, `missing`, qualified/unresolved equivalents in public language);
- boundaries shown outside the table so comparison cannot erase the source-specific limitation.

The table is intentionally allowed to scroll within its controlled region instead of being flattened into disconnected mobile cards.

## 5. Runtime acceptance

Local Chromium runtime acceptance was performed against first-hand generated output, not closure prose.

| Test | Coverage | Result |
|---|---:|---|
| Responsive route matrix | 9 representative routes × 2 languages × 4 widths (320, 390, 640, 1440) = **72 cases** | **72/72 PASS** |
| Forced-colours + image-off | People, Payments, Compare, Data × 2 languages = **8 cases** | **8/8 PASS** |
| Keyboard regression | Home search dialog + mobile-menu open/return path × 2 languages = **2 cases** | **2/2 PASS** |
| Total runtime cases | **82** | **82/82 PASS** |

The representative routes covered People, Firms, Payments, Providers, a visual Evidence Record, a visual Reading, Compare, Data and Measurement. Tested pages retained one `main`, one H1, correct RTL/LTR direction, no page-level horizontal overflow and one visible text fallback for every rendered governed visual.

Forced-colours testing used Chromium's forced-colours emulation. Image-off acceptance removed image elements from the rendered test fixture and verified that evidence meaning and visual fallback remained. These tests do **not** replace the named screen-reader, browser-chrome zoom, final contrast or deployed-environment accessibility acceptance reserved for S08.1.

## 6. Deterministic regression protection

`validate.py` now fails when:

- the bundled canonical Production Master hash differs from `AUTHORITY.json`;
- Page Specs do not carry the current Master authority hash;
- the Page Spec raw hash differs from the build summary;
- any of the 36 governed visual contracts lacks its bilingual analytical question, summary or prohibited inference;
- a rendered visual lacks its visible ordered-text fallback or its image-independent/non-colour markers;
- forced-colour, non-colour Compare or table-scroll semantics disappear;
- stale pre-reconciliation Arabic calculation-base language or the stale Page Spec Master hash reappears;
- S05.3 / Window 3 controls regress to an earlier boundary.

S03, S04, S05.1 and S05.2 acceptance invariants remain regression dependencies rather than being reopened.

## 7. Independent S05 recipient acceptance

After S05.3 authoring stopped, S05.1–S05.3 were treated as an unfamiliar recipient would treat them: by testing the generated result, controls and machine invariants rather than trusting the session reports.

| Promised result | Implemented where | First-hand result | Machine/runtime proof |
|---|---|---|---|
| AR/EN semantic safety | Page Specs + build templates | current Master terminology propagated; no scope/value widening | validator authority/parity checks |
| RTL/LTR + narrow reflow | generated bilingual routes + CSS | no page overflow on representative 320/390/640/1440 cases | 72/72 responsive cases |
| Keyboard/focus | shell/search/menu/Compare | search/menu focus-return and focusable table region survive | 2/2 keyboard cases + validator |
| Progressive evidence boundary | Domain/Evidence families | material limitation remains outside optional disclosure | S05.2 regression checks retained |
| Compare table accessibility | `app.js` + CSS | caption/scopes/region/scroll instruction/text states present | DOM assertions + validator |
| Image independence | rendered visual cards | visual meaning carried by governed text summary and boundary | 8/8 image-off/forced-colour cases |
| Non-colour meaning | Compare, notes, states, forced-colour rules | state remains legible without palette | forced-colours runtime + validator |
| Visual economy | presentation contract | 17 useful public visual IDs rendered; 19 contracts not added as clutter | generated-output inventory |
| Canonical authority | `authority/` + controls | same live Master ID now inside canonical repo; projections tied to current hash | raw SHA-256 + Drive parent verification |

No material S05 regression was found after the fixes above. Therefore the independent decision is:

**`WINDOW_3_ACCEPTED`**

## 8. What became more true / simpler / complex / removable

**More true:** the site now explicitly survives non-colour and image-off use; the current Master, Page Specs and control stack point to the same authority state; the Master is physically inside the canonical repository.

**Simpler:** other windows no longer need to guess which workbook is canonical. Old masters and old “final” packages remain reference/challenge material and cannot become authority by proximity or naming.

**New complexity:** forced-colours behavior and visible text-fallback structure are now testable release invariants; the external prior-drafts folder is a registered S06 candidate source rather than an informal input.

**Can be removed/avoided:** parallel workbook copies, duplicate “final” folders and public rendering of every possible visual contract. Generated `dist/` remains disposable and non-canonical.

## 9. Remaining boundaries

- `R-042` remains OPEN: anyone-with-link writer access is a release blocker owned by S07 security/release control.
- Named screen-reader application testing, browser UI zoom, final contrast and deployed-environment accessibility remain S08.1 work.
- The user-supplied prior-drafts/research folder is **not production truth**. Candidate evidence from it is queued for S06 and must end as Master-integrated, rejected, no-change-required or explicitly deferred with owner.
- S06.1 has **not** started in this window.
