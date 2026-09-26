# Design acceptance criteria

How the Design package and its reference site are accepted at D7. Copy this list into
`design/10_ACCEPTANCE_CHECKLIST.md` and complete every line with **evidence** — a screenshot path, a test output, a file
and line, or a note. A line without evidence is not met. Acceptance requires the runnable, fully populated bilingual
reference site (brief §19): a design source without it is an incomplete hand-back and is not accepted as complete.
Nothing here is a WCAG conformance claim.

## A. Truth and authority

- [ ] No file under `authority/`, `site-src/content/`, `dist/`, `audit/` was edited by hand; all gates in
      `CONTRIBUTING.md` §5 pass on the final commit.
- [ ] Every number, label, date, source name and sentence of controlled meaning on every screen comes from
      `site-src/content/**`; no copied or hand-written content model exists in the reference implementation.
- [ ] Every new interface label needed was requested as `NEEDS_CONTROLLED_CONTENT` in `design/ESCALATIONS.md`, not authored.
- [ ] The accepted reference site contains no `⟦NCC:…⟧` placeholder and no invented wording: every label it shows is in
      the Master and regenerated into `interface_copy.json`, and every optional feature whose labels are not yet governed
      is unshipped and listed as an exception in `design/09_CODE_HANDOFF.md`.
- [ ] The withheld CLM-044 value never appears; the nine sources without a public locator are never named or linked;
      no third-party document is bundled or offered for download.
- [ ] Evidence Records show the boundary as two labelled parts (does not establish · limits of the measure) where the
      record has both, part A alone where it has no measurement limitation, and never print the internal delimiter.
- [ ] No internal ID, enum, field name or repository term is shown as prose (stable IDs used as citation references are
      allowed and bidi-isolated).

## B. Coverage (both languages; 1440, 640, 390, 320 CSS px)

- [ ] Global shell: header, primary navigation with the Method & Measurement family, trust layer, footer, language switch,
      search entry, cite and report utilities, skip link, breadcrumbs.
- [ ] Home · Explore · all eight domain routes · Evidence index · Evidence Record (dense CLM-003, thin single-source
      CLM-015, conflicted CLM-037, composite with members CLM-031, composite without listed members CLM-014, partial
      CLM-039, framing CLM-004, withheld CLM-044) · Compare · Readings index · the Reading stress cases named in the brief
      §9.1 · Data/sources/Resource Library with the chronology · Measurement · Methodology · About and every trust route ·
      corrections/report journey · 404.
- [ ] Every route in `handoff/ROUTE_CONTENT_AND_STATE_INVENTORY.json` renders in the reference implementation in both
      languages (the same 288 documents as `dist/`), bound through its page-family rules.
- [ ] The twelve hard-state cases (`hard_state_acceptance`, read as the brief §9.2 states) each have evidence that the
      "must prove" sentence holds, plus the withheld, composite, partial and framing records; every verification state in
      the inventory (`verification_states`) that has records is shown on one of them, and the two with none today
      (`SOURCE_NOT_YET_BOUND`, `NO_SOURCE_RECORD`) are designed as states in the component catalogue with their governed
      copy — never on an invented record.
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
- [ ] Compare: 2–4 records from the comparable set, URL state, the six governed dimensions and the boundary row before
      values, the four governed assessments and the separate same-record state, technical errors (including a real record
      outside the set), language switch keeps the comparison, mobile form, entry from each comparable record's page.
- [ ] Sources: register and curated library distinct; deep links focus the card; unknown reference is an announced link
      error; filtering by governed category only.
- [ ] Cite, report an issue, language and download (pattern with disabled/enabled states) behave as the brief §10 states;
      any richer reporting intent is client-side composition into the existing mail action — no backend, form element,
      new address or promised response time.
- [ ] No CauseWay-content download or export is enabled before the owner's licence decision (OWN-04); no third-party
      document is offered.
- [ ] `scripts/tests/test_public_tools.py` and `audit/tranche_c/checks/viewport_acceptance.py` pass against the reference
      implementation (`YFIE_SITE_DIR=design/reference/out …`), unedited, with every test hook kept (brief §19).

## E. Readings

- [ ] Title, standfirst and evidence tension first; governed metadata only; the essay ends with "What would change this
      reading?"; the prohibited inference is visible; at most one signature visual; the evidence trace and one or two
      related Readings follow.
- [ ] One Featured Reading on Home, one on Explore; at most two on a domain page; Evidence Records list the Readings that
      use them; Measurement priorities link where their gap is examined. No carousel, no card wall.
- [ ] A Reading prints — and saves as PDF from the browser — in its designed document layout, in each language: title
      block with edition and evidence period, essay, framed signature visual with fallback, "What would change this
      reading?", "What not to conclude", the evidence trace and the citation.

## F. Visuals

- [ ] SIGNATURE and CORE_ANALYTICAL visuals follow their data contracts; SUPPORTING visuals plot no values (governed text,
      or a non-quantitative diagram built only from governed words and `UI-VIS-*` labels); TABLE_TEXT_FIRST and
      RETIRE_FROM_DESIGN visuals are not drawn as charts.
- [ ] Legends and labels come only from `UI-VIS-*` and `<field>_label`; colour is never the only carrier; no
      red/amber/green; nothing fades with age; breaks, gaps and disagreements are drawn.
- [ ] Each visual has its analytical alt text and a table or ordered-text fallback; the detached frame travels with any
      export; RTL and narrow forms follow the contract.

## F2. Print and portable evidence

- [ ] Every page family has a print style: chrome hidden; title, edition, canonical URL and language kept; each figure
      printed with period, population, unit and boundary; "What not to conclude" on the same page as its claim; charts
      never split from caption and fallback; Arabic prints right to left; no meaning by colour (evidence: print
      previews of Home, an Evidence Record and a Reading in both languages).
- [ ] Contextual chart and table exports carry the full detached frame (title, period, population, unit, credit,
      prohibited inference, markers, canonical link, edition); they are designed and ship disabled until OWN-04.
- [ ] Any fragment that can leave the page — print, export, citation, social image — keeps provenance and limits.

## G. Arabic and English

- [ ] Arabic is natively composed (own type scale, line height, rhythm, order), not mirrored English.
- [ ] Mixed-script runs are isolated; digits are Western; dates and units follow the governed forms.
- [ ] `YFIE_SITE_DIR=design/reference/out python3 audit/tranche_c/checks/bilingual_invariance.py` reports 0 differing
      page pairs on the reference implementation.
- [ ] Dates follow the governed form (day, month name, year; the governed Arabic month names; Western digits).
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
- [ ] IBM Plex Sans and IBM Plex Sans Arabic, self-hosted from `vendor/fonts/` with the licence shipped, files as
      shipped; any other IBM Plex family member has its written rationale; no other typeface.
- [ ] No third-party resource; fonts loaded efficiently from `vendor/fonts/` — only the weights used, the critical faces
      preloaded, a deliberate `font-display`, IBM's own pre-split subsets where useful — with no self-made modified subset
      unless the owner approved one; no decorative imagery; per-family page weight recorded with the method in
      `docs/SUSTAINABILITY_METHOD.md`; no green claim.
- [ ] Head elements kept: title, description, canonical, hreflang (en, ar, x-default), Open Graph without image,
      JSON-LD as today; the social-image templates cover all eleven page families (shared templates allowed).
- [ ] Strict-CSP compatible: no inline executable script, inline style, inline handler, external resource or form; data
      in JSON blocks; escaped rendering.

## J. Package and handoff

- [ ] `design/00`–`10`, `design/ESCALATIONS.md`, `design/COVERAGE.csv` and the runnable `design/reference/` exist, and
      `design/00_DESIGN_README.md` says how to build and run the site.
- [ ] D0 recorded whether an approved visual board or homepage mockup was supplied; nothing absent from the repository
      was treated as binding.
- [ ] D1 tested two or three materially different theses on Home, `/evidence/CLM-003/` and
      `/readings/same-year-different-number/` in both languages before propagation, and `design/01_FOUNDATIONS.md` records
      them and why one was chosen.
- [ ] The decision log has entries for every gate D0–D7; the coverage ledger shows every route × language × width and
      every hard, verification and technical state `VERIFIED`, or explains each gap.
- [ ] `design/09_CODE_HANDOFF.md` maps tokens, components, states, routes, content bindings, visual contracts,
      responsive rules, accessibility behaviour and every exception (`handoff/DESIGN_TO_CODE_CONTRACT.md`).
- [ ] No consequential decision exists only in an image or an external design file.
- [ ] Every open escalation is listed with its design impact; none is silently worked around.
