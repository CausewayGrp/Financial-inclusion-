# Design acceptance criteria

How the Design package and its reference implementation are accepted. Copy this list into
`design/10_ACCEPTANCE_CHECKLIST.md` and complete every line with **evidence** — a screenshot path, a test output, a file
and line, or a note. A line without evidence is not met. Nothing here is a WCAG conformance claim.

## A. Truth and authority

- [ ] No file under `authority/`, `site-src/content/`, `dist/`, `audit/` was edited by hand; all gates in
      `CONTRIBUTING.md` §5 pass on the final commit.
- [ ] Every number, label, date, source name and sentence of controlled meaning on every screen comes from
      `site-src/content/**`; no copied or hand-written content model exists in the reference implementation.
- [ ] Every new interface label needed was requested as `NEEDS_CONTROLLED_CONTENT` in `design/ESCALATIONS.md`, not authored.
- [ ] The withheld CLM-044 value never appears; the nine sources without a public locator are never named or linked;
      no third-party document is bundled or offered for download.
- [ ] Evidence Records show the boundary as two labelled parts (does not establish · limits of the measure) and never
      print the internal delimiter.
- [ ] No internal ID, enum, field name or repository term is shown as prose (stable IDs used as citation references are
      allowed and bidi-isolated).

## B. Coverage (both languages; 1440, 640, 390, 320 CSS px)

- [ ] Global shell: header, primary navigation with the Method & Measurement family, trust layer, footer, language switch,
      search entry, cite and report utilities, skip link, breadcrumbs.
- [ ] Home · Explore · all eight domain routes · Evidence index · Evidence Record (dense, sparse, conflicted, composite,
      framing, withheld) · Compare · Readings index · at least three Reading stress cases · Data/sources/Resource Library
      with the chronology · Measurement · Methodology · About and every trust route · corrections/report journey · 404.
- [ ] Every route in `handoff/ROUTE_CONTENT_AND_STATE_INVENTORY.json` renders in the reference implementation in both
      languages (the same 288 documents as `dist/`), bound through its page-family rules.
- [ ] The twelve hard-state cases (`hard_state_acceptance`) each have evidence that the "must prove" sentence holds, plus
      the withheld, composite and framing records.
- [ ] The thirteen journeys succeed by keyboard, on mobile and desktop, in both languages.
- [ ] Every technical state in the inventory (`technical_states`) is reachable and looks technical, never like
      "no evidence"; every evidence gap looks like evidence, never like an error.

## C. The semantic firewall in the interface

- [ ] Each distinction in brief §5 has a visible, non-colour-only treatment wherever it occurs; a cropped component
      still carries unit, population, period and boundary.
- [ ] No composite score, traffic light, ranked summary or synchronised "current state" panel exists anywhere.
- [ ] Measurement priorities read as sequencing within the agenda, never as national policy or spending priority.
- [ ] The chronology reads as context, never as a causal chain.

## D. Tools

- [ ] Search: as-you-type, Arabic normalisation, ranking (ID > title > summary > body), result types, shortcuts, focus
      management, announced results, no-match and unavailable states, Measurement anchors, lazy index load.
- [ ] Compare: 2–4 records, URL state, compatibility rows before values, the three verdicts, technical errors, duplicate
      state, language switch keeps the comparison, mobile form, entry from a record.
- [ ] Sources: register and curated library distinct; deep links focus the card; unknown reference is an announced link
      error; filtering by governed category only.
- [ ] Cite, report an issue, language and download (pattern with disabled/enabled states) behave as the brief §10 states.
- [ ] `scripts/tests/test_public_tools.py` and `audit/tranche_c/checks/viewport_acceptance.py` pass against the reference
      implementation.

## E. Readings

- [ ] Title, standfirst and evidence tension first; governed metadata only; the essay ends with "What would change this
      reading?"; the prohibited inference is visible; at most one signature visual; the evidence trace and one or two
      related Readings follow.
- [ ] One Featured Reading on Home, one on Explore; at most two on a domain page; Evidence Records list the Readings that
      use them; Measurement priorities link where their gap is examined. No carousel, no card wall.

## F. Visuals

- [ ] Every drawn visual is SIGNATURE, CORE_ANALYTICAL or SUPPORTING and follows its data contract; TABLE_TEXT_FIRST and
      RETIRE_FROM_DESIGN visuals are not drawn as charts.
- [ ] Legends and labels come only from `UI-VIS-*` and `<field>_label`; colour is never the only carrier; no
      red/amber/green; nothing fades with age; breaks, gaps and disagreements are drawn.
- [ ] Each visual has its analytical alt text and a table or ordered-text fallback; the detached frame travels with any
      export; RTL and narrow forms follow the contract.

## G. Arabic and English

- [ ] Arabic is natively composed (own type scale, line height, rhythm, order), not mirrored English.
- [ ] Mixed-script runs are isolated; digits are Western; dates and units follow the governed forms.
- [ ] `audit/tranche_c/checks/bilingual_invariance.py` reports 0 differing page pairs on the reference implementation.
- [ ] No English-only metadata disappears in Arabic; no internal vocabulary appears in either language.

## H. Accessibility outcomes (WCAG 2.2 target; brief §14)

- [ ] Keyboard access and order; no trap.
- [ ] Visible focus that sticky UI never obscures.
- [ ] Targets ≥ 24 × 24 CSS px (44 for primary touch controls).
- [ ] Reflow at 320 CSS px and 400 % zoom; tables scroll inside a named, focusable region.
- [ ] Names, roles, landmarks and one `<h1>` per page; headings describe sections.
- [ ] Labelled inputs; text errors; announced status.
- [ ] Contrast 4.5:1 (text) and 3:1 (UI, graphics); no meaning by colour alone.
- [ ] Analytical text alternatives for every visual.
- [ ] RTL focus and reading order.
- [ ] Reduced motion honoured; nothing needs motion.
- [ ] Single-pointer operation; no drag-only interaction.
- [ ] Forced-colours mode and image-off keep every meaning.

## I. Identity, performance, discovery, security

- [ ] The logo is the canonical file, unmodified, at specified sizes and clear space — no CSS filter, blend mode or mask
      changes its colours; required derivative sizes are listed for Code (`design/08_ASSET_MAP.md`).
- [ ] IBM Plex Sans and IBM Plex Sans Arabic, self-hosted; any departure has its written rationale.
- [ ] No third-party resource; fonts subset; no decorative imagery; per-family page weight recorded with the method in
      `docs/SUSTAINABILITY_METHOD.md`; no green claim.
- [ ] Head elements kept: title, description, canonical, hreflang (en, ar, x-default), Open Graph without image,
      JSON-LD as today; the social-image templates are designed for every family.
- [ ] Strict-CSP compatible: no inline executable script, inline style, inline handler, external resource or form; data
      in JSON blocks; escaped rendering.

## J. Package and handoff

- [ ] `design/00`–`10`, `design/ESCALATIONS.md` and the runnable `design/reference/` exist and say how to run.
- [ ] `design/09_CODE_HANDOFF.md` maps tokens, components, states, routes, content bindings, visual contracts,
      responsive rules, accessibility behaviour and every exception (`handoff/DESIGN_TO_CODE_CONTRACT.md`).
- [ ] No consequential decision exists only in an image or an external design file.
- [ ] Every open escalation is listed with its design impact; none is silently worked around.
