# Design → Code contract

Claude Design owns visual and interaction decisions. Claude Code owns implementation decisions. Neither owns semantic
truth, which stays in the Production Master. This contract says what Design must record — continuously, in
`design/09_CODE_HANDOFF.md` and the files it references — so that Code never has to infer a decision.

## 1. Every component answers

- Which governed inputs does it consume (Page Spec field, projection file and key, `UI-*` label IDs)? Which are
  required, conditional or not applicable, and what renders when a conditional field is absent?
- What are its states: default, hover, focus, active, visited, loading, empty, error (technical), evidence-gap (not an
  error), disabled, expanded/collapsed, selected?
- What happens at 320, 390, 640 and 1440 CSS px and at 400 % zoom?
- What changes between Arabic RTL and English LTR (order, alignment, isolation, icons, chart direction)?
- What is its keyboard order, focus entry and return, accessible name and description, role and announcements?
- What survives when colour is removed, when images do not load, and in forced-colours mode?
- For quantitative meaning: what is the table or ordered-text fallback?
- Which source, citation or verification affordance must it expose?
- Which limitation must stay visible and may never move into a disclosure?

## 2. Every page family answers

Module order and composition rules (deterministic, from the Page Spec), the first-screen contract, what may be disclosed
later, next actions (inventory `next_action_policy` and `next_actions` — the listed destinations plus each domain
route's `primary_verify_destination`; where a route lists none, its policy and the family rules decide), breadcrumbs and
head metadata. All 11 families; every route bound through them (`handoff/ROUTE_CONTENT_AND_STATE_INVENTORY.json`). For
the Domain Answer, Evidence Record and Comparison families, depth and first-load exclusions come from
`site-src/content/presentation_priority.json`; for the other eight, the Page Spec's section order is the content order
and the family rules in `design/04_PAGE_FAMILY_COMPOSITIONS.md` decide depth — never by route.

## 3. Required mapping in `design/09_CODE_HANDOFF.md`

| Map | Content |
|---|---|
| Tokens | Every token in `design/02_TOKENS.json` → its use; language-specific type scales; breakpoints |
| Components | Component → governed inputs → states → tokens → accessibility behaviour → tests that cover it |
| Routes | Route pattern → page family → component sequence → data bindings |
| Content bindings | Field path in the projection → where it renders → formatting rule (dates, numbers, bidi isolation) |
| Visual contracts | Visual ID → tier → form → data-contract rows → grammar states → labels → fallback → detached frame |
| Responsive rules | Per family and component, with the Arabic variants |
| Accessibility | WCAG 2.2 outcome → how each component meets it → how it is tested |
| Tools | Search, Compare, sources, Cite, report, language, download: states, URL contracts, errors |
| Print | The print stylesheet per page family; the Reading print/PDF layout in each language; page-break rules; what is hidden and what must stay with each figure |
| Portable evidence | Chart and table export frames (title, period, population, unit, credit, prohibited inference, markers, canonical link, edition); which exports exist; their disabled state until the licence decision (OWN-04) |
| Test hooks | The IDs, `data-*` attributes, classes and JSON block IDs the suites use (brief §19), kept or each exception with its replacement |
| Assets | Logo placements and derivative sizes, fonts and subsets, icons, social-image templates |
| Exceptions | Every place where the design departs from a default, with the reason |

## 4. Rules

- **No screenshot inference.** An image may illustrate a decision; it cannot be the decision. Code never estimates
  spacing, guesses hidden states, infers mobile order or invents Arabic behaviour.
- **Content immutability.** Design may propose presentation; it may not change public wording or values. A needed label or
  field is `NEEDS_CONTROLLED_CONTENT`; a wrong one is `ESCALATE_TO_MASTER` (both in `design/ESCALATIONS.md`).
- **One runtime.** Parity work may use a branch; the repository ends with one production renderer.
- **Local-first.** No tool may need a network call; tool state that changes what is viewed is URL-addressable.
- **Technical ≠ evidence.** A technical failure never looks like missing or zero evidence, and an evidence gap never
  looks like a failure.
- **No placeholder ships.** A label pending as `NEEDS_CONTROLLED_CONTENT` is governed before acceptance or its feature is
  unshipped and listed in the exceptions map; Code never fills one.
- **Portable evidence keeps its provenance.** Anything that can leave a page carries source credit, period, population,
  boundary, canonical link and edition; no CauseWay-content download is enabled before the licence decision, and no
  third-party document is ever offered.
- **Records.** The decision log (`design/00_DESIGN_README.md`) and the coverage ledger (`design/COVERAGE.csv`) are part of
  the contract: Code reads why a decision was made and what was proved before changing anything.
- **Strict-CSP output.** No inline executable script or style; data in JSON blocks; escaped rendering.

## 5. Acceptance

The contract is met when every section of `handoff/DESIGN_ACCEPTANCE_CRITERIA.md` is complete with evidence on the
runnable, fully populated bilingual reference site, and a reader of `design/09_CODE_HANDOFF.md` can implement any
component, page family, tool, print style or export frame without opening a chat, a screenshot or an external design
file.
