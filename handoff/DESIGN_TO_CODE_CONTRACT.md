# Design → Code Contract

## Purpose

Claude Design owns **visual and interaction decisions**. Claude Code owns **implementation decisions**. Neither owns semantic truth.

## The handoff is complete only when each component/page family answers

- What controlled data/copy inputs does it consume?
- Which fields are required, conditional or not applicable?
- What are the default, hover, focus, active, loading, empty, error, disabled and expanded states where relevant?
- What happens at 320, 390/400, 640 and 1440 widths?
- What changes between Arabic RTL and English LTR?
- What is keyboard order and focus-return behavior?
- What is the accessible name/description and structural role?
- What survives when colour disappears?
- What survives when an image cannot be seen?
- What is the table/text fallback for quantitative meaning?
- What source/citation/verification affordance is required?
- Which evidence limitation must remain visible and cannot be collapsed into disclosure?

## No screenshot inference

A screenshot may illustrate a decision; it cannot be the decision. Claude Code must not have to estimate spacing, infer hidden states, guess mobile order or invent Arabic behavior from a desktop image.

## Required implementation mapping

`design/09_CODE_HANDOFF.md` must map each design component to:

- controlled content fields in `page_specs.json` or named local payloads;
- route/page-family use;
- design token names;
- accessibility requirements;
- interaction behavior;
- acceptance tests.

## Content immutability

Design may propose presentation edits. It may not change public evidence wording or values. Any proposed copy/content change is an escalation to the Production Master workflow.

## Single-runtime rule

Claude Code may use a temporary branch/worktree for parity work, but the final repository must contain one active public runtime. Do not leave the accepted legacy renderer and a new React renderer as two competing production implementations.

## R6 page-family and tool architecture

The production design is one system with **11 page families**, not one bespoke composition per route. Claude Design must prove the system first on hard states, then bind all routes through reusable family rules.

### Page-level first-screen contract

Before secondary content, every reader-facing page must establish:

1. **what job this page solves;**
2. **the strongest supported answer or orientation;**
3. **the evidence clock/scope where a number or state could be misread;**
4. **a material limitation when it changes interpretation;**
5. **the primary next action** — explore deeper, verify, compare, inspect source, or report/correct.

Progressive disclosure may hide density. It may **not** hide a limitation that changes the meaning of the headline claim.

### Tool-state contract

The design/code handoff must specify and implement these as first-class local tools:

| Tool | Required first complete build | State rule |
| --- | --- | --- |
| Global search | Yes | local index; failure is technical-unavailable, never evidence-absence |
| Evidence discovery/workbench | Yes | facets/search may be shareable in URL |
| Compare | Yes | 2–4 evidence IDs encoded in URL; compatibility before values |
| Source / Resource Library | Yes | source/category filtering; original-publisher outbound links |
| Cite | Yes | governed citation + canonical route |
| Language switch | Yes | preserve route/object/query/hash |
| Correction path | Yes | preserve originating route/evidence/source ID |
| Analytics | No | disabled/no-op by default |
| Remote data/API | No | absent by default; later adapter only |

### Hard-state acceptance

Do not sign off a component because its default state looks good. At minimum prove:

- dense demand-side evidence (`/people/`);
- sparse/unknown geography (`/access/`);
- institutional-state sequencing (`/payments/`);
- revised/forecast-vintage evidence (`/remittances/`);
- a dense/conflicted Evidence Record;
- a sparse/no-source-expected Evidence Record;
- unlike-record Compare;
- the full Data/Source scale with the curated resource cards;
- long-form Reading;
- Measurement Agenda without policy-ranking semantics;
- About/Trust plain-language use;
- Arabic mobile at 320–400px.

The machine-readable details live in `site-src/content/content/navigation_interaction.json`.

### URL and deep-link invariants

Search, source filtering and Compare may use query parameters. Any such state must survive a language switch where the equivalent object exists. Evidence and Reading routes remain stable canonical verification/synthesis URLs. Do not create a client-only state that cannot be reloaded or shared when it materially changes what the user is viewing.

