# Page family compositions

> STATUS: **D2 — the hard families composed and proved; the other families bound by the family rule.** Deterministic
> module order and composition rules for all eleven families, from the Page Spec and the two controlled contracts;
> the first-screen contract per family; what may be disclosed later; next actions; head metadata. Written from the
> reference implementation (`design/reference/yfie/families.py`, `render.py`), never from a picture. Families marked
> *family rule* build every route through these rules today but are composed and reviewed on their own ledger rows at
> D3; nothing in them is a design decision yet beyond the shared page object.

Depth and first-load exclusions for the Domain Answer, Evidence Record and Comparison families come from
`site-src/content/presentation_priority.json`; for the other eight the Page Spec's section order is the content order
and the rules below decide depth — never by route (`handoff/DESIGN_TO_CODE_CONTRACT.md` §2).

## 1. The page object every family shares (the T4 grammar, `01_FOUNDATIONS.md` §4–§5)

| Module | What it carries | Rule |
|---|---|---|
| Head | crumb (where governed), rubric, the governed question (`p.q`, where the page answers one), `h1#page-title`, the statement (the heading-less first section) | Clock before claim on every bound object; the `h1` names the in-page navigation |
| Answers | each governed section as `section.qa`: rubric = section role with its ordinal, `h2` = heading, body paragraphs (one per authored line) | Numbered only where the reader can use the order; limits never numbered |
| Boundary | every section whose role is a limit ("does not establish", "still do not know", coverage) as `section.bnd` in the boundary voice | Double rule, governed label, weight, counter colour; never behind a disclosure |
| Figures | every bound visual as a framed object (`03_COMPONENT_CATALOG.md` §2) | At most one in the first screen (the contract's `after_primary`); the rest in depth |
| Objects | bound records, Readings and priorities as clock-first compact objects (`.objs`) | Never a card wall; a list with hairlines |
| Depth | progressive sections in one `details.more` whose summary is the governed "more evidence" gloss | Nothing that changes a headline goes there |
| Next | the governed next actions (`route_next_actions`) as a labelled `nav.actions` | Only governed destinations |
| Foot | the page's own actions (cite, report) at the object's foot | Reachable at every width |
| Spine | index of the page's own sections (named by the `h1`) and the edges (each named by its governed heading) | One visible spine at any width |

## 2. Families

### Orientation `/` (D1, unchanged at D2)
Head (product rubric, `h1`) → the governed "three figures" paced as figure groups each followed by its bounded record →
the remaining bound records → boundary (section 4) → product statement and actions (section 1) → questions (section 9,
four starting questions as a numbered list) → sections 5–8 with the system visual at `#system` → featured Reading.
Order is composition, not the Page Spec's `section_order` (brief §4.5); the `#system` anchor is kept.

### Question Entry `/explore/` (D2)
Head (flow rubric, `h1`, lead) → **the questions** as the first answer: rubric "Questions that lead into the evidence",
`h2` "Find the question closest to your decision", section 5's body as the introduction, the governed sentence on what
every answer keeps, then the four governed clusters (inventory `question_groups`, headings `UI-QUESTIONS-*`, each with
its count) as numbered hairline lists — question link and its "what you get" line → sections 2 (answer), 3 and 4 (boundary
voice) → "What the evidence cannot yet answer" (the bound priorities as compact objects: current evidence, evidence
needed, the decision it would strengthen) → "Go deeper" (the featured Reading, then the link to all Readings).
First screen: the product's job and the first cluster. Lower intensity than Home; no cards, no pills, no imagery.

### Domain Answer (8 routes; D2 proves `/people/`, `/access/`, `/payments/`, `/remittances/`, `/reforms/`)
Order from `presentation_priority.json`: head (rubric "The question this page answers", the governed question as the
framing line, `h1` = the answer, lead = section 1) → the governed reading rule as the head's fine print with the two
governed actions (Explore questions; Open evidence → `primary_verify_destination`) → **the band**: the contract's
supporting sections, in the boundary voice, before the answers (the contract's `mobile_priority` puts them before
`primary 1`) → the primary sections in contract order as numbered answers, the first-screen visual after `after_primary`,
and the visuals placed beside a primary section (§3) → the depth figures under "Another view of the evidence" (the POS
small multiple; every bound visual not placed beside a primary section) → progressive sections in one disclosure →
the chronology (`/finance/` only, JRN-09) → Readings on this question (≤ 2) → related questions (governed relationships,
with the governed note that a link is not a causal claim) → "What measurement would change the decision?" (the first
`measurement_limit` priorities) → "Verify it yourself" (the contract's verification records as compact objects, the
three governed links, the disclosure of every bound record — JRN-03). Intensity varies with `presentation_family`: the
sparse page (`/access/`) opens on two limits and one text frame; the dense page (`/people/`) opens on the bars; the
admin page (`/payments/`) carries seven measurement objects first and the small multiple in depth; the transmission
page (`/reforms/`) carries the chain beside the section on the payment-infrastructure reform.

### Evidence Directory `/evidence/` (D2)
Head → **search** as the first answer (`#global-search`, its status and results regions, the Compare link) → section 1
(how to search, inspect and compare) → "Start here: selected evidence records" (the bound claims and objects as compact
objects with their reference) → the three bound visuals as text frames → related measurement priorities → **all
evidence records, by question** (JRN-17): one disclosure per answer question with its count, each record a row with its
title and its clock → next actions. 110 rows never become noise: they are grouped by the question they answer and each
carries only its title and period.

### Evidence Record (110; D2 proves the §9.1 set)
As at D1: head (crumb, rubric, clock, `h1`, lead) → the seven governed questions as `h2` answers in governed order,
the strip after the first answer on narrow screens → the boundary as question 5 (parts A and B) → question 6: the
source cards, or — for a framing rule, a composite or a partial record — the governed lineage statement **as the
answer in the body voice**, never an empty or error state; the governed intro is printed unless the record is a
framing rule with no source to open; a record without a public locator states so in the body voice → question 7 as a
disclosure → the util block: reference, cite, **Compare** (the 13 comparable records), reuse, history, report. A `VIS-`
record draws its own visual under the first answer: the record page is the visual's canonical route.

### Comparison `/evidence/compare/` (D2)
Head (flow rubric, `h1`, lead) → **the tool** as the first answer: the governed intro as rubric, "Can these records
actually be compared?" as `h2`, the governed comparison statement, **the boundary before the controls** (the visual's
prohibited inference in the boundary voice), the four `<select>` slots with their governed labels, "Copy link", the
governed no-averaging sentence, then the runtime's output: the verdict first (styled as the boundary voice), the table
inside a named region, the boundaries, the record links → section 2 → next actions. At 320–639 px the table recomposes
without changing the runtime: each dimension row becomes a block — the dimension name, then the cells numbered 1–4 in
slot order (the slot labels are governed: first, second, third, fourth record), then the assessment label.

### Reading Index `/readings/` — family rule (D3)
Head (flow rubric) → the featured Reading (compact object) → all Readings as clock-first compact objects (title,
question) → next actions.

### Reading (10) — D1 renderer; family rule until D3 review
As at D1.

### Data & Source `/data/` (D2)
Head (flow rubric, `h1`, lead) → **the register** as the first answer: the governed intro and rights note, the filter
(`data-source-filter`, its status), then three groups — *Curated reports and references* (28 cards grouped by
`resource_category`, each with its kind line, reference, why it matters, boundary, open original, copy reference,
reuse state, dependent records), *Sources supporting the evidence now published* (open by default; citation cards
by governed title, locator-only sources by reference and locator, never a title), *Additional original references*
(closed) — and the no-match state → sections 2–7 (limits in the boundary voice) → section 8 as the inventory list →
section 9 with the chronology (24 dated events as compact objects: period, fact, relevance, what it does not
establish, public sources) → section 10 → next actions. The nine sources without a public locator are never named.

### Measurement `/measurement/` — family rule (D3)
Head → sections 2–9 → section 10 introduces the agenda → the ten priorities as page objects (`id` = the governed
reference, focusable for deep links): priority and domain as the clock, title, current evidence, missing evidence,
the decision it would strengthen, where the gap is examined, reference, a disclosure with the governed guardrail,
feasibility, basis and what would change; **no ordinal numbering** (measurement_nonranking, proved at D3) → the
revealing records and the gaps visual → next actions.

### Reference / Trust (8) — family rule (D3)
Head (flow rubric, `h1`, lead) → sections as numbered answers → bound records (Methodology) → next actions. `/contact/`
carries the report path (the originating record, the mail action revealed only for a known record) and `/corrections/`
the current-record context; both keep the runtime's hooks.

### 404 and root
The bilingual 404 in the shell's page object (Arabic first, every word governed, the search dialog and runtime only);
the neutral root entry redirects to the chosen edition (else Arabic) without inline script.

## 3. Where a bound visual sits (DL-D2-003)

| Route | First screen (contract) | Beside a primary section | In depth |
|---|---|---|---|
| `/people/` | VIS-FINDEX-GAPS after primary 2 | — | VIS-FL-EVIDENCE-LADDER (its section, 9, is progressive) |
| `/access/` | VIS-ACCESS-EVIDENCE-LAYER after primary 3 (text frame) | — | — |
| `/payments/` | VIS-PAYMENT-ANATOMY after primary 2 | VIS-E-MONEY-RULE-STACK beside section 6 | the POS small multiple (terminals, transactions, value) |
| `/remittances/` | VIS-REMITTANCE-MACRO after primary 1 | VIS-REMITTANCE-COST beside section 5 | — |
| `/reforms/` | none (contract) | VIS-FCP-REDRESS-PATH beside 3; VIS-PAYMENT-RAILS and VIS-TARGET-RESULT-STATE beside 6; VIS-OECD-FCP-TIMELINE beside 11 | — (VIS-CAPITAL-CONTEXT is never drawn) |
| `/firms/`, `/finance/`, `/providers/` | the contract's visual | — | the remaining bound visuals (D4) |

A visual beside a progressive section goes to the depth group, never inside the disclosure.

## 4. What a family rule does not do

A route built by a family rule is `BUILT` in `COVERAGE.csv`, not `REVIEWED`: every route is still looked at in both
languages on its own row at its gate, and its composition may change there within the Lock.
