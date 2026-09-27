# Architecture package

These diagrams are implementation/design aids. They do **not** create a parallel source of truth. The Production Master remains the sole semantic, evidence, source, rights and publication authority.

- `YFIE_PUBLIC_SITE_MAP.svg` — primary navigation, trust layer, public domains, verify/analyse/measure routes and the unseen public-service layers.
- `YFIE_PAGE_FAMILY_STATE_MAP.svg` — the page families with their route counts, navigation prominence and job, the hard states, and the static/local-enhancement boundaries used for Design handoff.
- `YFIE_FULL_STACK_SYSTEM_ARCHITECTURE.svg` — source/reference closure through Master, projections, design/compiler, static runtime and correction loop.
- `YFIE_DESIGN_TO_CODE_FLOW.svg` — finite Claude Design -> Claude Code -> release acceptance sequence.

**Derived, not hand-maintained (Pre-Tranche-C P4).** The site map and the page-family map are drawn by
`scripts/architecture_diagrams.py` from the navigation contract (`site-src/content/content/navigation_interaction.json`) and
the public inventory (`site-src/content/content/public_inventory.json`); the full-stack diagram takes its counts from the
same inventory. `python3 scripts/architecture_diagrams.py` rewrites the SVGs and their PNG previews;
`python3 scripts/architecture_diagrams.py --check` fails if a committed SVG no longer matches the current state, and the
validator runs that check (P4-G05). The design-to-code flow carries no count or navigation and is not regenerated: it is hand-maintained to match the
Design gates D0–D7 of `handoff/CLAUDE_DESIGN_MASTER_PROMPT.md` §20 (updated 27 September 2026); if they ever differ,
the brief is right.

The SVG files are the inspectable vector artifacts; the PNG files are previews.
