# S03.4 — Providers + Reforms + Domain Answer system closure

**State:** CLOSED — S03 FULL EIGHT-ROUTE CLOSURE PASSED  
**Date:** 2026-09-22  
**Decision:** PROCEED TO S04.1

## Exact achievement

S03.4 completed the Domain Answer family by recomposing `/providers/` and `/reforms/` in Arabic and English and replacing the six-route hard-coded presentation hierarchy with one renderer-consumed machine-readable presentation-depth contract covering all eight Domain Answer routes.

The frozen Page Specs and Production Master remain semantic authority. `site-src/content/presentation_priority.json` controls only order, depth, prominence, linkage, mobile priority and first-load exclusions.

## User tasks solved

- **Providers:** identify which provider universe is evidenced, under whose authority/date/status, what can be counted, and why listing/licensing does not establish operation or a current national operating-provider denominator.
- **Reforms:** identify what changed, the furthest state the evidence establishes, what later state is still unmeasured, and why rule/funding/institution/implementation are not use, quality or outcome.

## Files / routes changed

- `scripts/build.py`
- `scripts/validate.py`
- `site-src/content/presentation_priority.json` — new presentation-only implementation contract
- `/providers/` — AR/EN Domain Answer composition
- `/reforms/` — AR/EN Domain Answer composition
- control-stack files updated at closure

No Page Spec, evidence, claim, source, rights or publication-state semantic content changed.

## What became more true

- One eight-route canonical presentation contract now exists; the renderer consumes its route entries directly, with no derived `DOMAIN_CONFIG` compatibility layer.
- Providers foregrounds authority/status/date and keeps listing ≠ operation visible.
- The 98 / 225 / 106 exchange-remittance categories remain separate source-defined categories; the route does not total them into a deduplicated current operating universe.
- Reforms now presents the transmission chain and preserves the furthest evidenced state without turning missing downstream evidence into reform failure.
- The validator now proves eight-route mapping, governed references, publication eligibility of promoted governed objects, narrative retention, AR/EN structural parity, verification reachability, first-load safety boundaries, absence of `DOMAIN_CONFIG`, and renderer/contract binding.

## What became more usable

Users reach answer, scope/boundary, dominant evidence and verification before the longer reference layer. Providers no longer reads as a directory wall. Reforms no longer reads as an undifferentiated project/document timeline.

## Removed / demoted / merged

- Removed the independently editable hard-coded six-route `DOMAIN_CONFIG` presentation decisions and the temporary derived `DOMAIN_CONFIG` compatibility layer; `build.py` now reads `PRESENTATION_ROUTES` directly from the canonical presentation contract.
- Historical provider structure, wallet-count comparability detail and secondary reform cases remain available in progressive depth rather than competing with the first-load question.
- No new reform chart was forced onto first load: none of the existing controlled visuals represented the heterogeneous reform portfolio better than the stage-based prose. `VIS-PROVIDER-OBSERVABILITY` remains the one first-load visual on Providers because it materially clarifies what is known by provider class.

## New complexity

One presentation-only JSON contract is now a tracked implementation dependency. Validation fails if its route coverage, references, safety boundaries or renderer binding drift.

## Eight-route domain matrix

| Route | Dominant analytical object | Primary | Supporting / always-visible | Progressive | First-load visual | Primary verification |
|---|---|---:|---:|---:|---|---|
| People | representative people evidence + subgroup gaps | 3 sections | 3 scope/boundary items | 7 | VIS-FINDEX-GAPS | CLM-001 |
| Access | geographic access observability | 3 | 3 | 4 | VIS-ACCESS-EVIDENCE-LAYER | Evidence hub |
| Firms | bounded firm survey + programme evidence | 4 | 3 | 3 | VIS-FIRM-CONSTRAINTS | CLM-005 |
| Finance | intermediation / microfinance evidence states | 4 | 3 | 7 | VIS-MFI-DIVERGENCE | CLM-022 |
| Payments | payment measurement objects + use boundary | 3 | 3 | 4 | VIS-PAYMENT-ANATOMY | CLM-003 |
| Remittances | concept / vintage / evidence state | 4 | 3 | 4 | VIS-REMITTANCE-MACRO | CLM-007 |
| Providers | authority / status / operation observability | 4 | 3 | 4 | VIS-PROVIDER-OBSERVABILITY | CLM-009 |
| Reforms | furthest evidenced reform state | 4 | 3 | 6 | none by design | CLM-011 |

## Counterfactual deletion / visual-economy decisions

- Removing the Providers observability visual would materially reduce the user's ability to distinguish named universe, authority, event state and operation evidence across provider classes: **KEEP**.
- Adding a generic Reforms first-load visual would privilege one reform subclass or make heterogeneous evidence states look commensurable: **DO NOT ADD**.
- Removing the always-visible boundary on Providers would make an operating-provider inference materially easier: **KEEP VISIBLE**.
- Removing the reform-state boundary would make rule/implementation/outcome stage-jumping materially easier: **KEEP VISIBLE**.
- Longer historical/context sections retain verification value but do not change the first answer: **PROGRESSIVE**.

## Regression tests

- Clean deterministic build: 284 HTML documents from 141 Page Specs.
- Repository validator: `ERRORS=0`, `WARNINGS=0`, PASS.
- Python syntax: PASS.
- JavaScript syntax: PASS.
- Providers/Reforms AR 390px, 768px, 1440px render inspection: PASS.
- Providers/Reforms EN 390px, 768px, 1440px render inspection: PASS.
- Full eight-route narrative-loss and structural parity checks: PASS.
- Contract references and public Evidence Record destinations: PASS.
- Archive delta check: unreviewed inbox EMPTY.
- Production Master escalation: NONE.

## Arabic / English result

The same section hierarchy, evidence boundaries, first-load visual decisions, progressive depth and verification records are used in both editions. An Arabic-only raw English visual metadata leak was detected during mobile inspection and removed from the renderer; language-neutral periods may remain, while unlocalized English metadata no longer appears as Arabic UI.

## Boundary decision

**PROCEED** — S03 is CLOSED. S04.1 is now the only permitted next bounded session.
