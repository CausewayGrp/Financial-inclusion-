# S04.2 — Compare + Data/source + citation/rights/corrections/publication closure

**Session state:** CLOSED / PASS  
**Window 2 recipient-side decision:** ACCEPTED  
**Production Master:** `Yemen_Financial_Inclusion_Evidence_Master.xlsx`  
**Production Master SHA-256:** `6c0f8f18325b4f117de82e8ac8396c70adf0b3f1871878cf614ed01833ea40fd`  
**Semantic/evidence authority:** Production Master + controlled Page Specs.  
**Presentation implementation authority:** `site-src/content/presentation_priority.json` only for order/depth/prominence/linkage/mobile priority.

## Exact achievement

S04.2 turns Compare, Evidence Records, Data/source, citation, source reuse boundaries and Corrections into one coherent public trust path without creating a new source registry or rights authority.

- Compare now begins with **comparison legitimacy**, not a value table. It consumes the existing Canonical Presentation Contract as a distinct `Comparison` page family, uses only governed objects bound to `/evidence/compare/`, checks controlled dimensions before a comparison verdict, fails closed when required fields are missing, and does not compute averages, midpoints, preferred numbers or conversion scalars. The final renderer implements the controlled Page Spec range of **2–4 records**: two required selections plus an optional third and fourth record, assessed through one N-way compatibility judgment.
- The prior generic governed-object card dump on Compare was removed. The same governed object set remains available through the selector and Evidence Records, so no evidence was lost while first-load duplication was eliminated.
- Evidence-record citation now carries record ID, period, population/base, material inference boundary and public source IDs so detached use is less likely to become a different claim.
- Data/source and Evidence Record source controls separate **citation** from **redistribution**. All 149 controlled source records currently have object-level or unspecified redistribution state; the interface therefore makes no permission claim and directs users to source-specific terms.
- Corrections preserves the originating Evidence Record through `?record=<ID>` and returns to the current public record. Because the controlled Corrections Page Spec contains no separately governed correction-event objects, the interface explicitly does **not** invent release/correction history.
- Source Reference Closure is traversable from sampled public objects through controlled dependencies/passports, source records, permitted locators, Evidence Records and detached citation context.
- Publication filtering was strengthened across public HTML, not only Evidence/Data. One indirect `NO_PUBLIC_LOCATOR` leak was found in a Reading source sidebar and removed by making the shared source renderer use the same public-locator filter as Evidence Records/Data. The validator now rejects any no-public-locator source ID in any public HTML or public search payload.

## User tasks solved

A recipient can now answer, without internal-ID knowledge:

- **Can these 2–4 pieces of evidence actually be compared?** The comparison verdict appears before any numeric interpretation and explains material field differences or missing compatibility information across the full selected set.
- **Where did this evidence come from?** Evidence Record → Source Reference Closure trace → Data/source → original public locator where publication state permits.
- **Can I cite it?** Evidence Records expose copyable detached-use citation context; Data/source exposes source-reference copy controls.
- **Can I redistribute the original source/table?** The product does not equate a public locator with redistribution permission; current controlled rights state does not establish republication permission.
- **Was this record corrected or superseded?** The current Corrections surface preserves the originating record and publishes only governed correction/version events; none are invented when absent.
- **Can I get back to the interpretation?** Evidence Records retain related Domain/interpretation routes and Data/source exposes dependent Evidence Records.

## Files changed

- `scripts/build.py`
- `scripts/validate.py`
- `site-src/app.js`
- `site-src/styles.css`
- `site-src/content/presentation_priority.json`
- existing control stack listed below
- `SHA256SUMS.txt`
- this closure artifact

No controlled semantic payload or Page Spec content changed in S04.2. `site-src/content/page_specs.json` remains byte-identical to the S04.1 projection (`c5a39b072aaea7438c5146476e6923411503d066acb75e2dbf88bd8b99222fb1`).

## What became more true / usable

**More true**

- Visual similarity no longer implies comparability.
- Missing compatibility metadata does not silently become compatibility.
- A public source URL no longer implies redistribution permission.
- A source dependency without a public locator cannot appear indirectly on a Reading or other generated public page.
- Citation carries material scope and inference boundary with the evidence record.
- Absence of controlled correction events remains absence, not synthetic history.

**More usable**

- Compare gives a direct verdict (`not direct`, `unresolved`, `qualified`, structurally aligned, or same record) and opens each selected Evidence Record.
- Source cards offer both original locator and Data/source focus where allowed.
- Evidence Records link to their correction/version context and provide detached citation text.
- Data/source retains S01 source focus while adding source citation/reuse controls and dependent Evidence navigation.

## Removed / demoted / merged

- Removed generic governed-object cards below the Compare tool because they duplicated the same comparison pool and added no material task value.
- Removed indirect rendering of source dependencies that have no public locator.
- No second source registry, rights registry, correction registry or comparison-semantic authority was created.

## New complexity

- `Comparison` is now a populated family in the existing Canonical Presentation Contract.
- The renderer has bounded helpers for citation context, source-reference trace, source trust controls and correction-origin context.
- `validate.py` now owns deterministic S04.2 publication, comparison, citation, rights and closure invariants.

This complexity is implementation-only. It does not carry production facts or rights decisions.

## Compare acceptance

The generated Compare surface uses the controlled `/evidence/compare/` Page Spec and 11 governed comparison objects. It evaluates the contract-driven dimensions `definition`, `universe`, `geography`, `unit`, `period`, `method`, `source_reference` and `currentness` before a verdict. Geography/unit remain missing where the controlled objects do not provide structured values; that absence causes a fail-closed result rather than an invented match.

A closure regression found that the first S04.2 renderer exposed only two selectors even though the controlled Page Spec explicitly permits **2–4 records**. The implementation was corrected without changing the Page Spec or Master. Arabic and English now each render two required plus two optional selectors, and the client assesses all selected records together.

Hard-case interaction / deterministic test:

- `CLM-032` (same reference year, different published value) vs `CLM-033` (valuation-method break) → **NOT A DIRECT COMPARISON** in Arabic and English.
- repeated selection of the same Evidence Record is identified as a duplicate/same-record condition rather than independent evidence.
- all 11 governed records are available in each selector; two records are required and records three/four are optional.
- across all unique 2-, 3- and 4-record combinations (55 + 165 + 330 = 550), the current governed metadata yields **NOT DIRECT** because at least one hard compatibility field differs. The firewall is not weakened merely to manufacture a positive comparison.
- no numeric-value field is included in the Compare client payload.
- no auto-average, midpoint, preferred-number or conversion-scalar logic exists.

## Source Reference Closure sample

| Evidence class | Public object | Controlled dependency/passport path | Source state outcome |
|---|---|---|---|
| Population | `CLM-001` | Findex controlled dependencies / `EP-FINDEX-2022-ACCOUNT` | public LOCATOR_ONLY sources retained; scope/boundary in citation |
| Firms | `CLM-005` | `EP-FIRM-2022` and controlled firm dataset lineage | resolved public source IDs |
| Programme KPI | `CLM-060` | `EP-SMEPS-FINACCESS-KPI` | resolved SMEPS public locator |
| Payments | `CLM-003` | `EP-CBY-POS-MONTHLY` | monthly CBY public locators; discrepancies retained |
| Remittances | `CLM-007` / `CLM-032` | IMF macro passport / CBY vintage passport | LOCATOR_ONLY and DISPLAY_READY paths both exercised |
| Providers | `CLM-009` / `CLM-055` | exchange roster / bank-roster passport | official roster/status sources remain distinct from operation |
| Reforms | `CLM-011` | `EP-CBY-FCP-REDRESS-2024` | complaint architecture source, not performance evidence |
| Derived / visual | `VIS-EVIDENCE-CLASS-LADDER` | controlled visual dependencies | visual closure resolves through controlled sources |
| No-public-locator suppression | `CLM-056` dependency `SRC-MOPIC-YSEU-2023-080` | controlled closure retains dependency internally | source ID/locator suppressed from all public HTML/search |

## Methodology ↔ implementation ↔ test trace

| Controlled methodological principle | Implementation surface | Deterministic evidence |
|---|---|---|
| Analytical objects remain distinct | Compare compatibility-first family; Evidence Record boundaries | Compare payload contains governed records without numeric forced merge; validator rejects forced reconciliation logic |
| Evidence clocks remain distinct | Compare period/currentness rows; Evidence Record currentness | validator checks period/currentness and CLM-032 vintage/currentness hard case |
| Derived evidence remains reproducible | Evidence Record method/verification progressive depth | S04.1 evidence-family regression retained; Source Reference Closure dependencies remain visible where public |
| Compare only when compatible | comparison verdict before interpretation | contract/renderer drift test + hard-dimension fail-closed client logic |
| Evidence/publication states affect behavior | source publication filtering and Data/source rendering | DISPLAY_READY/LOCATOR_ONLY tests; global NO_PUBLIC_LOCATOR suppression test |
| Correction belongs to the evidence trail | Corrections origin context + current-record backtrack | `?record=<ID>` binding; validator requires correction transparency block and does not invent events |
| Users can challenge the answer | citation, original locator, Evidence Record, report/correction path | record/source links resolve; detached-use citation and related/backtrack regression |

No controlled Methodology statement required amendment in S04.2.

## Build / validation / human inspection

- Clean build: **284 HTML documents from 141 controlled Page Specs**.
- Validator: **ERRORS=0 / WARN=0 / PASS**.
- Python syntax: **PASS**.
- JavaScript syntax: **PASS**.
- Local HTTP smoke: `/en/evidence/compare/`, `/ar/evidence/CLM-001/`, `/en/data/`, `/ar/corrections/`, `/en/providers/`, `/ar/reforms/` all returned **200**.
- AR/EN local render harness at **390px and 1440px** for Compare, Data, Corrections and `CLM-001`: **one h1, no horizontal overflow, correct RTL/LTR structure**.
- Compare widget inspected in Arabic/English at mobile and desktop widths; compatibility verdict remains visible before the comparison table.
- Independent recipient-side content/task harness: **143 / 143 checks PASS**.
- Post-acceptance 2–4 selector regression: clean build/validator/syntax/local-HTTP checks PASS; generated AR/EN Compare structure has exactly two required and two optional selectors. The controlled semantic payload remained byte-identical.

The render harness uses current generated HTML/CSS/JS bytes. Direct Chromium navigation to localhost is blocked by the execution environment, so this is not claimed as deployed-host, screen-reader, 200% zoom, contrast, security or privacy acceptance. Those gates remain owned by S05/S07/S08.

## Defects found and dispositions

1. **Compare generic-object duplication** — FIXED. Governed comparison objects were redundantly rendered as generic cards below the compatibility tool. They are now represented once through the selector and linked Evidence Records.
2. **Indirect NO_PUBLIC_LOCATOR leak on a Reading source sidebar** — FIXED. Shared source rendering now uses publication-filtered source rows; the validator checks all public HTML/search for no-public-locator IDs.
3. **Controlled 2–4 Compare range under-implemented in the first renderer** — FIXED. The Page Spec was correct; implementation now exposes two required and two optional selectors and one N-way compatibility verdict.
4. **No semantic/evidence/source/rights defect found in the Production Master during S04.2** — no Master escalation.

## Archive delta

`99_REFERENCE_ARCHIVE_INBOX__NON_PRODUCTION/01_NEW_INPUTS__UNREVIEWED` was checked and is **EMPTY**. No S06 candidate was consumed early.

## Window 2 independent recipient-side acceptance

Acceptance was run after S04.2 authoring stopped, against the generated repository state and verified Master identity. The recipient harness covered Providers, Reforms, all eight Domain Answers, Evidence Records, search/source navigation, Compare, citation/reuse boundaries, Corrections, publication filtering, Source Reference Closure, AR/EN parity and Methodology behavior.

Realistic questions were answered without a materially wrong conclusion:

- Which providers are officially listed? **Source-defined categories/rosters are countable.**
- Does listing mean they operate? **No.**
- Is 429 a current operating-provider count? **No; the 98/225/106 category entries are not a deduplicated current operating universe.**
- What does a reform establish? **Only its furthest evidenced state; later operation/use/outcome stages remain open until measured.**
- Does a reform object prove an inclusion outcome? **No unless outcome evidence is separately governed.**
- Where did 11.9% account ownership come from? **World Bank Findex controlled sources, with the 2021 wave / 2022–23 Yemen fieldwork context.**
- Is it a 2026 rate? **No.**
- What population does it apply to? **Adults 15+ within survey coverage, with the controlled geographic/sampling limitation.**
- Why can remittance figures disagree? **Vintage, concept, method and territorial/source mappings can differ; Compare exposes those differences instead of forcing a common scale.**
- Can they actually be compared? **Only where the controlled compatibility fields support it; otherwise the result is qualified, not-direct or unresolved.**
- Can I cite this? **Yes, using the Evidence Record citation context and original source references.**
- Can I redistribute the original table? **The current source-rights records do not establish that permission; citation/factual use and redistribution remain separate.**
- Was this evidence corrected? **The Corrections surface publishes controlled events only; it does not manufacture history. Current-record context is preserved.**
- Can I return to the question I started from? **Yes through related interpretation/backtracking routes.**

## Boundary decision

**S04 is CLOSED. Window 2 is ACCEPTED. S05.1 is the next permitted session and has not started.**

## Canonical Drive reconciliation

Window 2 accepted state was integrated into the existing canonical Drive repository **in place**. Existing source/control file IDs were preserved; the S04.2 closure artifact was added under `docs/`; generated `dist/` remains non-canonical and is not stored in Drive. The Production Master was re-fetched from Drive ID `1xAbdDHJd5bYo0Pzo_a6dR6HsZ056LzJU` and re-hashed to `6c0f8f18325b4f117de82e8ac8396c70adf0b3f1871878cf614ed01833ea40fd`. No concurrent Master change was detected.

## Open release-boundary risk

A recipient-side Drive permission check found that the canonical production repository folder currently has an **anyone-with-link writer** grant. No concurrent overwrite was detected during Window 2 reconciliation, but technical single-writer control is therefore not established. This does **not** reopen S04 or change semantic authority; it is recorded as release/security risk `R-042` and assigned to S07 security/release control. Final release certification is prohibited until write access is restricted to authorized maintainers and integrity/release checks are rerun.
