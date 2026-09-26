# S03.2 — Firms + Finance composition review

**Session:** S03.2  
**Decision owner:** Editorial / product lead  
**Challenger lenses:** firm-finance / private-sector evidence specialist; financial-system analyst  
**Authority:** Production Master SHA256 `d8db3b4ee7ffbba0ca1cfb2843949a2ee323ac0a8a5396c273ebf4a4cc427fee`  
**Routes:** `/firms/`, `/finance/` in Arabic and English  
**Decision:** **PROCEED**

## ORIENT

S03.2 inherited the closed S03.1 answer-first domain grammar rather than reopening composition architecture. The live reference-archive unreviewed folder was checked and was empty: **NO NEW ARCHIVE DELTA**. The Production Master and frozen controlled publication projections remained unchanged.

The session objective was not visual uniformity. It was to make two unlike evidence families understandable without creating false equivalence: bounded formal-firm survey/programme evidence on Firms, and historical/system balance-sheet and microfinance evidence on Finance.

## CHALLENGE → DECIDE

The route grammar remains shared at the reasoning level:

**strongest answer → reading rule → scope/currentness + dangerous inference → selected evidence/analysis → deeper controlled context → measurement next where governed → verify**.

The component density is deliberately non-uniform. Firms foregrounds denominator and evidence-class distinctions. Finance foregrounds stock/flow, valuation/currentness and system-state boundaries. Similar-looking percentages and balances are not styled as directly comparable merely for consistency.

## BUILD — first-hand production source

Implemented in `scripts/build.py` by extending the established `DOMAIN_CONFIG` and renderer rather than creating a second page system:

- `/firms/`: `bounded-survey-programme` family; survey context and denominator boundaries remain adjacent to the answer; four selected primary sections; one controlled firm-constraint visual; two governed measurement-next items; direct controlled claim verification links.
- `/finance/`: `system-history` family; historical-series and unresolved-currentness boundaries remain adjacent to the answer; four selected primary sections; one controlled microfinance divergence visual; two governed measurement-next items; direct controlled claim verification links.
- Route-specific `visual_after` placement prevents the same visual rhythm from being mechanically imposed on both routes.

No controlled fact, number, universe, denominator, source identity, evidence class, rights state or publication state was edited.

## Public-page burden — before vs after

| Route | Baseline | S03.2 accepted composition | Material effect |
|---|---:|---:|---|
| EN `/firms/` | 18,974 bytes; 11 repeated answer cards | 15,411 bytes; 4 selected primary analytical sections; 1 progressive disclosure group; 1 selected visual; 2 measurement-next items; no answer-card dump | Firm constraints, finance severity, credit path and programme evidence read as different bounded evidence objects rather than one KPI wall. |
| AR `/firms/` | 27,486 bytes; same repeated-card pattern | 20,863 bytes; same accepted hierarchy | Arabic retains the bounded-survey/programme distinctions without inheriting unnecessary card density. |
| EN `/finance/` | 29,591 bytes; 21 repeated answer cards | 17,294 bytes; 4 selected primary analytical sections; 1 progressive disclosure group; 1 selected visual; 2 measurement-next items; no answer-card dump | System history, nominal balances, microfinance reach and balance-sheet context are separated before verification depth. |
| AR `/finance/` | 42,793 bytes | 23,929 bytes; same accepted hierarchy | Arabic gains materially faster decision comprehension while keeping system-state boundaries visible. |

## Semantic protections verified

### Firms

- The 2022 business survey remains a **formal-firm, seven-governorate, N=328** evidence object, not a national enterprise-prevalence estimate.
- The 22% access-to-finance challenge share and the 91.84% finance-severity result remain different questions/bases, not competing estimates of the same rate.
- The line-of-credit result remains `31/328`; the loan-source description remains bounded to the **18 valid responses**.
- SMEPS reach/disbursement figures remain programme-delivery measures.
- The 19% / 15% KPI remains a source-reported programme KPI with incomplete metric-specific denominator detail; it is not national MSME prevalence.
- Programme reach ≠ population reach and target ≠ result.

### Finance

- Borrowers, savers, deposits, balances and portfolios remain distinct units/states.
- Stock ≠ flow; nominal portfolio growth ≠ real credit deepening.
- Historical/pointer-only/missing observations are not converted into a continuous annual series.
- Same-year source restatement / valuation-basis change is not presented as economic change.
- Banking-sector and microfinance system measures are not presented as household/firm inclusion prevalence.
- Provider listing/state and external-support financial states are not converted into observed access/use/outcome.

## Hostile tests

**Detachable-claim / screenshot:** PASS. Firm percentages retain denominator/universe context in adjacent scope/boundary treatment. Finance headline and selected evidence do not convert balances/savers into people-side inclusion.

**Cold deep-link:** PASS. Direct entrants see the answer, reading rule, scope/currentness and the most dangerous inference before deeper context.

**Quotation safety:** PASS. The shortest prominent sentences do not state a national firm prevalence rate or a system-balance measure as inclusion prevalence.

**Epistemic state:** PASS. Bounded sample, programme universe, historical series, missing/pointer-only observations and unresolved harmonization are intentional states rather than UI failure.

**Counterfactual Deletion:** PASS. Repeated governed-card walls were removed from the domain routes because the evidence/source surfaces carry verification depth. Four primary sections are retained on each route because removing any would erase a material distinction: constraint context, finance severity/credit path/programme relation for Firms; history, unit divergence, valuation/state and system connection for Finance.

## EN ↔ AR / viewport inspection

Inspection followed the required order: Arabic 390px → Arabic 1440px → English 390px → English 1440px, with intermediate structural checks. No horizontal overflow was detected at 390px or 1440px.

Representative inspection confirmed:

- Arabic headings and scope bands wrap without collision;
- RTL reading order remains coherent through answer, scope, selected evidence, progressive disclosure and verification;
- percentages, denominators and mixed Latin source/stable-ID strings remain legible;
- Firms and Finance share a recognizable product grammar without looking falsely equivalent;
- verification routes remain available in both languages.

## Machine verification after final S03.2 edits

- Build: `Built 284 HTML files from 141 controlled page specs.`
- Validator: `HTML=284 ERRORS=0 WARN=0`
- Result: `WEBSITE REPOSITORY VALIDATION PASS`
- Controlled semantic projection was not modified by S03.2.

## Friction / delay register

| Classification | What happened | What it delayed or affected | Resolution | Can recur? |
|---|---|---|---|---|
| DESIGN AMBIGUITY | Firm survey, programme KPI and finance-system evidence invite false equivalence if forced into one identical component pattern. | Selection and hierarchy decisions. | Used one reasoning grammar with route-specific section/visual placement and explicit denominator/state boundaries. | Yes; S03.3 must preserve the same non-mechanical rule. |
| IMPLEMENTATION COMPLEXITY | A fixed visual insertion point suited one route but weakened the other. | Page rhythm and decision compression. | Added route-specific `visual_after` configuration rather than a second renderer. | Low; configuration now supports route differences. |
| TOOL LIMITATION | Direct localhost/file browser navigation remains blocked in the current Chromium environment. | Browser-style inspection. | Used deterministic generated HTML plus viewport rendering/screenshot inspection; full browser/a11y release acceptance remains assigned to S05/S07. | Yes in this runtime. |
| REPOSITORY / ACCESS | Canonical Drive must be updated before S03.3 begins, not only at window end. | Session boundary discipline. | First-hand source, review/control files and checksum are synchronized at S03.2 closure before proceeding. | Preventable by repeating this gate. |

## Accepted implementation-safe lessons

- **Denominator-first safety** → implemented in `/firms/` scope/boundary composition through `scripts/build.py`.
- **Do not equalize unlike evidence classes through styling** → implemented through separate `family`, selected sections and visual placement for Firms vs Finance.
- **Progressive disclosure instead of governed-array dumping** → implemented in the shared domain renderer.
- **Verification one layer deeper but never hidden** → direct evidence-record + Evidence/Data/Methodology links remain on both routes.

No factual/source/rights proposition from reference material was promoted. No Production Master escalation was required.

## End-of-session rationalization

1. **What became more true?** Firm and finance findings now visibly preserve their survey/programme/system universes and states at the point a user can misuse them.
2. **What became more usable or simpler?** Both routes reach a defensible interpretation faster and remove repeated answer-card walls.
3. **What complexity was introduced?** Route configuration now supports different visual insertion points and evidence-family labels; the renderer remains single and bounded.
4. **What was removed/merged/retired?** Repeated domain answer-card presentation and redundant first-pass evidence blocks were removed from the route surface, not from governed evidence/source layers.
5. **What defects remain?** No material S03.2 defect. Full browser/accessibility/release tests remain correctly deferred to named later sessions.
6. **Production Master escalation?** No.
7. **Why is S03.3 next?** Payments and Remittances are the next deliberately different stress pair: high-frequency administrative infrastructure/transactions versus macro flow vintages, estimates/projections and conceptual disagreement.

## Boundary decision

**PROCEED — S03.2 is CLOSED. S03.3 is the only permitted next session.**
