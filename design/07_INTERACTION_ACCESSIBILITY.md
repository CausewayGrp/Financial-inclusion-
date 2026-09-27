# Interaction and accessibility

> STATUS: **D5 — met at this commit, pending the owner's merge.** Every tool state, every technical state and the thirteen
> journeys, by keyboard, on mobile and desktop, in both languages, on the rendered reference site: 52 journey walks and 28
> technical-state drives pass (`check_journeys.py`). What is asserted is asserted by
> `design/reference/check_journeys.py` (journeys and technical states) and `design/reference/check_site.py` (hooks,
> target size, named navigation, the interaction smoke test, degraded renders); what is a design decision is recorded
> here and in the decision log (`00_DESIGN_README.md`, DL-D5-*). No conformance is claimed (AGENTS.md rule 10): WCAG 2.2
> AA outcomes are the target the checks are written against.

## 1. The three voices

The interface speaks in three voices, and a reader can tell them apart without colour:

| Voice | Where | Rule | Never |
|---|---|---|---|
| Body | answers, records, Readings | hairline rules, body ink | — |
| Boundary | every limit of the evidence (`section.bnd`, a figure's foot, the Compare verdict) | double rule, governed label, weight, the counter colour | behind a disclosure; dashed |
| **Technical** (D5) | every announced status, every technical error, the no-script note: the Compare link errors (`.compare-url-error`), the same-record state (`[data-compare-verdict=same-record]`), search and register statuses (`.search-status`), no-match states (`[data-search-empty]`, `[data-source-no-results]`), record-context link errors (`[data-correction-error]`), `.noscript` | **a dashed hairline**, body ink, the governed technical title where the runtime writes one | the double rule; the counter colour; the plaster surface (reserved for figures); an evidence-gap object (`[data-lineage-state]`, `[data-evidence-source-unavailable]`) |

Technical ≠ evidence (`handoff/DESIGN_TO_CODE_CONTRACT.md`): a technical failure never looks like missing or zero
evidence, and an evidence gap never looks like an error. `check_journeys.py` asserts the dashed rule on every technical
state and that none sits inside a boundary section or an evidence-gap object.

## 2. Keyboard

- **Focus is visible everywhere:** `:focus-visible` is a 3 px double outline in the counter colour, offset 3 px (6 px on a
  focusable table wrapper), on every link, button, input, select, summary and `tabindex="-1"` target.
- **The first Tab lands on the skip link** on every page (asserted per render by `check_site.py`).
- **The menu (< 900 px):** the button carries `aria-controls="primary-nav"` and `aria-expanded`; Enter opens it and moves
  focus to its first link; Escape closes it and returns focus to the button; focus leaving the menu closes it (runtime
  TOOL-04). Asserted by the interaction smoke test at 390 px.
- **Search:** the dialog opens from the product bar with focus on the input, closes on Escape with focus returned to the
  opener; results are announced through `[data-search-status]`; Arabic input is normalised by the runtime. On
  `/evidence/` the same tool is inline (`#global-search`) with its own status and results regions.
- **Compare:** four native `<select>` slots in reading order, each labelled by its governed slot label; the verdict is
  written before the table; the table sits in a named, focusable region (`role="region"`, `aria-label`, `tabindex="0"`).
- **Deep links:** `?source=` on `/data/`, `#MA-00n` on `/measurement/` and `?record=` on Contact and Corrections move
  focus to the target object (`tabindex="-1"`), without scrolling it out of view.
- **Every in-page navigation is named** (the index and strip by the page's `h1`, each edge group by its governed
  heading); every link and button in `#main` meets the 24 px target size (asserted per render).
- **Journeys:** each of the thirteen journeys is walked with the keyboard only — from every page of the path, a link the
  page itself offers takes focus, shows the outline, sits in the viewport and activates with Enter; on a phone a
  primary-nav link is reached by opening the menu with the keyboard first (§5).

## 3. Motion, zoom, forced colours, no script, no stylesheet, print

- **Reduced motion:** `prefers-reduced-motion: reduce` removes every transition and animation and forces
  `scroll-behavior: auto`; nothing in the product depends on motion to convey state (there is no motion to begin with:
  the disclosures, dialog and menu change state without animation).
- **Zoom and reflow:** the 320 px renders stand for 400 % zoom of a 1280 px window and the 640 px renders for 200 %:
  no horizontal page scroll, nothing wider than the viewport outside a scrollable table wrapper, the strip and the
  foot spine in place of the side spine below 900 px (asserted per render at 320/390/640/1440).
- **Forced colours:** every rule, frame, chart mark and line takes `CanvasText`; state is never carried by colour alone
  (marks by shape, lines by dash, the break by a double rule, labels by text) — the forced-colours renders of every gate
  are in `design/reference/out/_review/degraded/`.
- **No script:** the governed no-script note in the technical voice at the top of every page; every answer, record,
  boundary and source stays readable; the tools' shells state their state honestly (the search dialog and Compare need
  the runtime; the register filter degrades to the full register).
- **No stylesheet / images off:** the document order is the reading order (`h1` inside `main`, the boundary before the
  depth, the text alternative under every figure); no image carries evidence.
- **Print:** figures kept whole with their boundary, controls and record actions removed, the foot spine's edges kept,
  external locators printed after their link text.

## 4. Technical states (the ledger's `technical:*` rows)

| State | Route | What the reader sees | Asserted |
|---|---|---|---|
| compare_wrong_count | `/evidence/compare/?records=CLM-001` | the governed input error (title, detail, note) in the technical voice; no verdict, no table | announced (`role="alert"`), dashed rule, no `[data-compare-verdict]`, navigation works |
| compare_unknown_id | `…?records=CLM-001,NOT-A-RECORD` | the same, naming the unknown reference | same |
| compare_malformed | `…?records=,,` | the same | same |
| compare_not_comparable_record | `…?records=CLM-001,CLM-003` | the same: a real record outside the comparable set is a link error, not a verdict | same |
| compare_duplicate | `…?records=CLM-001,CLM-001` | the governed same-record state, in the technical voice, never one of the four assessments | visible, only `same-record`, dashed rule |
| search_no_match | any page, a string with no match | "no result matches" with the governed reminder that no match is not absence of evidence | status announced, `[data-search-empty]` in the technical voice, outside any boundary |
| search_index_unavailable | index fetch fails | the governed "could not be loaded" state; no hits invented | announced, no `.search-hit`, dashed rule |
| source_link_unknown | `/data/?source=SRC-NOT-A-SOURCE` | the governed link error as an alert; every source stays visible | `[data-source-link-error]` alert, all records visible, dashed rule |
| source_filter_no_match | `/data/`, a string with no match | the governed no-match line; the count reads 0 | status announced, `[data-source-no-results]` visible in the technical voice |
| record_context_unknown | `/contact/?record=CLM-999` | the governed link error; the report path still works | alert `unknown`, corrections link present, dashed rule |
| record_context_malformed | `/corrections/?record=%3Cx%3E` | the governed link error | alert `malformed`, dashed rule |
| record_context_valid | `/contact/?record=CLM-001` | the originating record carried into the report action | origin shown, mail action revealed with the record, no error |
| language_switch_state | Compare with records → other edition | same route, query and hash; the comparison kept | URL and table |
| not_found | `/404.html` | bilingual, Arabic first, noindex, routes back into the evidence | `check_site.py` (D3) |
| no_javascript | any page, script off | the governed note; the evidence readable; navigation works | note visible in the technical voice, `#q1/#q5/#q6` present |

## 5. Journeys (the inventory's thirteen, `handoff/ROUTE_CONTENT_AND_STATE_INVENTORY.json` → `journeys`)

Each journey is walked at 390 px (mobile) and 1440 px (desktop), in English and Arabic, by keyboard, and its success
condition is asserted on each landing (`check_journeys.py` → `SUCCESS`). Results and the per-step record are written to
`design/reference/out/_review_journeys.json`; the end screens of each desktop walk to `design/evidence/d5/`.

| Journey | Path | Success condition (inventory) | Asserted on the landings |
|---|---|---|---|
| J01 First-time public | `/` → `/explore/` → `/people/` → `/evidence/CLM-001/` | plain answer precedes method depth; the record exposes scope, period, limitation, source | statement then figures; the questions first; question → answer → boundary → verify; clock before claim, population, limitation on first load, source path, method in depth |
| J02 Journalist, number | `/evidence/CLM-001/` → `/data/` | clock, population, limitation and original-source path visible before reuse | as J01's record; the register with its filter and rights note |
| J03 Journalist, Reading → evidence | `/readings/gender-gap-…/` → `/evidence/CLM-002/` → `/data/` | direct links to the bound records | boundary before the essay; `[data-path-record]` links; the record; the register |
| J04 Researcher, comparability | `/evidence/` → `/evidence/compare/` | compatibility tested before values | search and the Compare entry; the boundary before the controls |
| J05 Regulator, reform chain | `/` → `/explore/` → `/reforms/` → `/evidence/CLM-011/` | rule, implementation and outcome separated; the verification route explicit | the domain page's two actions and verify objects; the record |
| J06 Technical, payments | `/payments/` → `/evidence/CLM-003/` → `/data/` | terminals, transactions, value, people, use not collapsed | domain, record, register |
| J07 Provider, market signal | `/explore/` → `/providers/` → `/evidence/CLM-009/` | listing and dated status visible; operation a separate question | questions; domain; record |
| J08 Development partner | `/people/` → `/evidence/CLM-001/` → `/methodology/` | one object at answer, record and method depth | domain; record; the records bound on Methodology |
| J09 Humanitarian flows | `/readings/after-transfer-…/` → `/evidence/CLM-045/` → `/payments/` → `/data/` | delivery separated from persistence; programme evidence bounded | Reading; record (some sources without locator, stated); domain; register |
| J10 Challenge / correction | `/evidence/CLM-001/` → `/contact/` → `/corrections/` | the report action carries the record; Contact links on to Corrections | the report link carries `?record=`; origin shown and mail revealed; the corrections context |
| J11 Reuse and rights | `/data/` → `/rights/` → `/terms/` | rights discoverable from source work, separate from citation | register; the trust sections |
| J12 Accessibility report | `/accessibility/` → `/contact/` | status and the report path discoverable | sections; the contact link; the report path |
| J13 Payment-rail explainer | `/payments/` → `/reforms/` → `/evidence/CLM-018/` → `/data/` | roles in plain language; states separated from observed use | domain; domain; record; register |

## 6. Verification states without records

`SOURCE_NOT_YET_BOUND` and `NO_SOURCE_RECORD` have no record today. They are designed as states of the record's question
6 with their governed copy (the unbound statement; the no-record statement), in the body voice like the other lineage
states (`03_COMPONENT_CATALOG.md` §1, Evidence Record), never on an invented record; the renderer carries the branch and
`check_site.py` will assert it the day a record carries the state.

## 7. What this gate does not claim

No WCAG conformance, no assistive-technology testing beyond the accessibility tree that the checks read, no
native-language certification. Screen-reader and switch-access sessions with people are an owner item (escalated as
anticipated at D0).
