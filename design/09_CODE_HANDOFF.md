# Design → Code handoff (progressive)

Contract: `handoff/DESIGN_TO_CODE_CONTRACT.md`. Updated at every gate end; never back-filled.

## State at D0

| Area | Status | Notes |
|---|---|---|
| Tokens | NOT STARTED | `handoff/DESIGN_STARTING_TOKENS.json` is a hypothesis only; do not implement it |
| Components | NOT STARTED | Candidate component inventory in `00_DESIGN_README.md` §4 — not decisions |
| States | MAPPED, NOT DESIGNED | 9 verification, 20 grammar, 15 technical, 12 hard-state cases — see `COVERAGE.csv` |
| Routes | MAPPED | 288 documents; family per route in `COVERAGE.csv` |
| Content bindings | UNCHANGED | Render only from `site-src/content/**` per inventory `projection_roles` |
| Visual contracts | NOT STARTED | 36 contracts; tiers in `00_DESIGN_README.md` §4 |
| Responsive / RTL | NOT STARTED | Widths 320 / 390 / 640 / 1440 |
| Accessibility | NOT STARTED | WCAG 2.2 AA outcomes as target; no conformance claimed |
| Print / export | NOT STARTED | Downloads ship disabled until OWN-04 |
| Reference implementation | DOES NOT EXIST | DEBT-002 |

## State at D1 (in progress — updated at milestones, not back-filled)

| Area | Status | Notes |
|---|---|---|
| Content path | IMPLEMENTED (neutral) | `design/reference/yfie/content.py` reads `site-src/content/**` and gives every renderer the same structures (shell, page, evidence record, reading, visual, home); `design/reference/check_content.py` proves parity with `dist/`. Code inherits this path or an equivalent that binds the same projections; no copied content model |
| Test hooks | CARRIED by the neutral harness | `design/reference/yfie/neutral.py` emits every brief §19 hook unstyled: ids `main`, `global-search`, `search-dialog`, `search-results`, `utility-status`, `source-<ID>`; `data-search-open/close/input/status/results`, `data-menu`, `data-lang`, `data-cite`, `data-source-cite`, `data-evidence-source`; classes `skip` (first focusable), `evidence-cite-button`, `source-locator`, `table-wrap`; JSON block `yfie-ui`; meta `yfie-citation`; `<dialog id="search-dialog">` with input `global-search-dialog`; one `h1`; `lang` and `dir` on the document |
| Tokens | NOT DECIDED | Each canvas proposition carries its own token set (`design/exploration/d1_canvas/boards/t*.py`); none is a decision. `02_TOKENS.json` is written only from what the Lock proves |
| Components | PROPOSED, NOT DECIDED | Candidate object grammars on the canvas: register entry with marginalia (T1), passage with disclosed evidence (T2), labelled strata with a trail (T3), clock-first evidence object with a question index and a verification spine (T4) |
| Visual contracts | RV-CWR-001 DRAWN IN FOUR FORMS | All inside the contract (two 2024 markers keyed by publication, no joining line, zero-based axis; two indexed lanes, never one axis; note, boundary, credit, canonical link; fallback tables). Panel 1 as rows on a horizontal zero-based axis (T4) is under test as the form that cannot read as a fall |
| Responsive / RTL | UNDER TEST | Propositions composed at 1440 and 390 px in both languages; T4 mobile-first and Arabic-first. Numeric axes stay LTR in Arabic; IDs, units and index bases isolated with `bdi` |
| Strict CSP | CONSTRAINT NOTED | Canvas artboards use an inline `style` on their frame and, in places, inline styles for composition; the reference renderer must emit none (stylesheet only) |
| Reference implementation | HARNESS ONLY | `python3 design/reference/build.py --renderer neutral`; `--renderer accepted` fails until a thesis is chosen (DEBT-002) |

## Must not be reinterpreted (already fixed by the brief)

- Test hooks of brief §19 (IDs, `data-*` attributes, classes, JSON blocks, `<dialog id="search-dialog">`, `<select>`
  Compare slots, skip link class `skip`, `role="status"`/`role="alert"` regions).
- Strict CSP: no inline script/style/handlers, no external resources, no form; `yfie-lang` is the only preference.
- Logo never filtered, recoloured or inverted (EAD-04); fonts self-hosted, unchanged, with OFL.
- CLM-044 value never rendered anywhere; the 9 sources without a public locator never named or linked.

## Temporary vs intended

Nothing implemented by Design yet. Nothing in `dist/` or `site-src/styles.css` is a Design decision.

## Owner / release items that remain

OWN-01 identity and funding statement · OWN-04 content licence (gates downloads) · OWN-06 reversed logo · EAD-03 logo
derivatives · REL-01…04. See `FINAL_OPEN_ITEMS_REGISTER.md`.
