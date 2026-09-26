# S02 — Audience Journeys & Information Architecture

## Objective

Make the public product behave like a decision-and-verification service rather than a rendered backend. S02 changes implementation hierarchy and navigation only; it does not alter evidence semantics. The Production Master remains the sole authority for evidence, claims, source state, rights and publication state.

## Decision owner and challengers

- **Owner:** product / information architecture.
- **Challenger 1:** first-time public or mobile user who does not know the system structure.
- **Challenger 2:** expert verifier — regulator, researcher, journalist or development-partner analyst who must reach scope, source and caveat quickly.

## Cold-user findings

1. **Home and Explore were too similar.** Both exposed the same 11-question grid, so Explore did not add enough navigational value.
2. **The site was route-aware before it was task-aware.** The compact six-item global navigation is correct, but a first-time user still had to infer which domain route matched the task in front of them.
3. **Home carried too much discovery work.** Signals, the causal chain, all 11 questions and downstream calls-to-action were individually valid but collectively made the entry page denser than necessary.
4. **Audience-specific menus would be the wrong fix.** Citizen, journalist, CBY, donor and researcher labels are useful for testing, but permanent role silos would duplicate content and increase maintenance. The durable UI should organize around user tasks and questions.

## IA decision

### Global navigation — keep

Keep the six controlled top-level items exactly as the public navigation spine:

**Explore · Evidence · Readings · Data · Methodology · About**

Home remains accessible through product identity. Domain pages stay inside the question-led Explore architecture.

### Home — orient, do not catalogue

Home now performs five jobs in order:

1. establish what the product is;
2. show three different evidence signals without collapsing their units;
3. explain the rule → operation → access → use → quality → outcome chain;
4. offer **task-first starting points** for the most common jobs;
5. show only four common direct questions, with a clear path to all 11 questions on Explore.

This removes duplication without removing any controlled question from the product.

### Explore — complete question map

Explore remains the complete 11-question entry surface, but the questions are grouped by the job they serve:

- understand the system;
- people, use and flows;
- firms, institutions and providers;
- verify and decide what to measure.

The question wording, routes and `user_gets` statements remain exactly controlled by `questions.json`.

## Audience task tests

| Audience | Primary job | Expected shortest path | S02 acceptance condition |
|---|---|---|---|
| Citizen / student | Understand exclusion or practical access | Home → task/question → People or Access | Can reach a plain answer before methodology detail. |
| Journalist | Verify a quoted number | Search or Home task → Evidence → evidence record | Can see period/base/limit/source before reuse. |
| PhD student / researcher | Reconstruct and compare | Evidence → Compare/Data/Methodology | Can inspect definition, vintage, derivation and source without guessing. |
| CBY leadership | Understand system signal and implication | Home → Explore → relevant domain | Can distinguish infrastructure, access, use and outcome. |
| CBY technical team | Inspect a series/source and its status | Search/Data/Evidence | Can reach source locator and controlled evidence object quickly. |
| Bank / MFB / MFI / PSP | Understand market signal without overstating use | Explore → Payments/Providers/Finance | Infrastructure and provider status are not presented as adoption or operation. |
| World Bank / IMF / donor / DFI | Check evidence basis and comparability | Explore/Reading → Evidence/Data | Can trace claims and see non-comparability and evidence clocks. |
| Humanitarian / cash-transfer actor | Understand flows and household connection | Explore → Remittances/Payments/People | Can see what is measured versus what remains unobserved. |

## Counterfactual deletion test

- Removing the full 11-question grid from **Home** loses no material user value because Explore preserves it completely; therefore Home now uses a smaller common-question set.
- Removing **Explore** would lose the complete question map; it remains essential.
- Adding persistent audience-specific sections would largely duplicate existing routes; they are not added.
- No archive-derived factual proposition is promoted in S02.

## Build changes

- Added task-first Home orientation cards linking only to existing controlled routes.
- Reduced Home direct-question display from 11 to 4 representative starts.
- Kept all 11 questions on Explore and grouped them by task.
- Added responsive styling so the new orientation collapses cleanly from five columns to three and then one.
- Added validator assertions for Home/Explore differentiation, task-card count and full 11-question retention.

## S02 verification and closure

- Rebuilt all 141 controlled Page Specs into 284 generated HTML documents.
- Validator result: **ERRORS=0 · WARN=0**.
- Arabic and English Home each contain 5 task starts and 4 compact direct questions.
- Arabic and English Explore each retain all 11 controlled questions in 4 task groups.
- No controlled question, route, source or evidence object was deleted.

**S02 status: COMPLETE.** S03 now addresses the density and composition of individual domain routes.
