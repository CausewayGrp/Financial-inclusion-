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
