# S03.1 — People + Access composition review

**Session:** S03.1  
**Decision owner:** Editorial / product lead  
**Challenger lenses:** people-side evidence specialist; first-time non-specialist reader  
**Authority:** Production Master SHA256 `d8db3b4ee7ffbba0ca1cfb2843949a2ee323ac0a8a5396c273ebf4a4cc427fee`  
**Routes:** `/people/`, `/access/` in Arabic and English  
**Decision:** **PROCEED**

## ORIENT

The live `docs/AUTHORITY.json` and the current Production Master hash were re-verified before composition work. `site-src/content/page_specs.json` remains the frozen controlled publication projection; S03.1 does not alter evidence semantics. The baseline build reproduced 284 HTML files from 141 controlled page specs and passed the repository validator with `HTML=284 ERRORS=0 WARN=0`.

The reference-archive delta check found `01_NEW_INPUTS__UNREVIEWED` empty. One new top-level pointer, `Old drafts`, linked to a high-fidelity mobile-review mockup folder. It was reviewed once for composition lessons only, classified `DESIGN_REFERENCE_ONLY`, and moved to `04_DESIGN_REFERENCES__REVIEWED`. No factual, source, rights or evidence proposition was promoted.

## CHALLENGE → DECIDE

The dense People route and sparse Access route were deliberately treated as different stress cases. The accepted product grammar is shared at the reading level, not mechanically at the component-count level:

**question / strongest answer → reading rule → scope + inference boundary → selected evidence/analysis → explicit unknowns → measurement next → verify**.

Accepted implementation-safe reference lessons were answer-first hierarchy, typographic adjacency of scope/boundaries, selected evidence rather than a governed-object dump, progressive disclosure, and cold-deep-link comprehension. No archive number, claim, route architecture or source state was copied.

## BUILD — first-hand production source

Implemented in:

- `scripts/build.py`
  - `DOMAIN_CONFIG` for `/people/` and `/access/`;
  - `domain_hero`, `domain_scope_band`, `domain_page`, selected visual rendering, progressive `domain_more`, `domain_measurement_next`, and route-specific `domain_verify`;
  - normal non-domain routes remain on the existing renderer.
- `site-src/styles.css`
  - the `S03 domain composition` block establishes answer-first editorial composition, restrained evidence states, progressive disclosure, verification treatment, mobile behavior and RTL-aware layout;
  - direct evidence-record links carry readable titles plus stable IDs without exposing backend jargon as page content.

No controlled fact, number, universe, denominator, source identity, rights state or publication state was edited.

## Public-page burden — before vs after

| Route | Baseline | S03.1 accepted composition | Material effect |
|---|---:|---:|---|
| EN `/people/` | 36,083 bytes; 10 H2; 33 answer cards; 11 generic sections | 16,954 bytes; 1 H1; 3 primary domain sections; 1 progressive disclosure group holding 7 deeper sections; 1 selected visual; 2 measurement-next cards; 0 answer-card dump | Dense route becomes answer-first while deeper governed material remains reachable. |
| AR `/people/` | 50,717 bytes; same card/section pattern | 22,966 bytes; same accepted grammar | Arabic no longer inherits desktop-English density as a visual burden. |
| EN `/access/` | 11,812 bytes; 7 H2; 2 answer cards; 8 generic sections | 13,637 bytes; 1 H1; 3 primary domain sections; 1 progressive disclosure group holding 4 deeper sections; 1 selected visual; 2 measurement-next cards | Sparse evidence is intentionally composed as an evidence-gap state instead of padded to mimic People. |
| AR `/access/` | 16,382 bytes | 18,445 bytes; same accepted sparse grammar | Unknown geography and measurement need read as substantive states, not missing UI. |

The Access byte count rises slightly because the route gains explicit scope/inference/verification structure; this is intentional decision compression rather than filler.

## Semantic anchors preserved

### People

- Account ownership remains a **population survey measure**, not a count of accounts or active users.
- The latest representative account-ownership observation remains attached to the Findex wave / Yemen fieldwork timing; it is not presented as a 2026 prevalence rate.
- Gender and income findings remain same-wave subgroup measures, not causal explanations.
- Geographic exclusion / sampling limitations remain adjacent to the People interpretation rather than being relegated to a distant methodology page.
- Direct verification links expose controlled evidence records for `CLM-001`, `CLM-002` and `CLM-025`, plus Evidence, Data/Sources and Methodology.

### Access

- The absence of a defensible national access-point map is presented as a **known evidence limitation**, not zero access and not a broken page.
- Infrastructure, rosters and provider counts are not rendered as proof of operating access, use or outcomes.
- Unknown geography remains unknown; no subnational knowledge is invented.
- The current controlled access visual remains visible because it carries material analytical value not replaced by a separate evidence-detail route.
- Measurement Next is framed as the evidence needed to answer the access question, not as existing evidence.

## Hostile tests

### Detachable-claim / screenshot test
**PASS.** Consequential People claims travel with scope/currentness and inference boundaries in the first composition blocks. Access does not expose a headline pseudo-number that could be detached from an unknown-state qualifier.

### Cold deep-link test
**PASS.** On both routes, a direct entrant encounters route title, strongest answer, reading rule, scope/currentness and the major inference boundary before deeper evidence. Verification is reachable without knowing a stable ID.

### Quotation-safety test
**PASS.** The prominent People sentence identifies the evidence clock and does not convert the population measure into a current 2026 rate. The Access headline states that the evidence is not yet a national map rather than implying coverage.

### Epistemic-state test
**PASS.** Historical/currentness limits and unobserved geography are intentionally styled evidence states. Unknown is not rendered as `N/A` or zero.

### Counterfactual Deletion Test
**PASS.** Removed the generic answer-card wall and repeated payloads from the domain route because verification depth already exists in controlled evidence/source surfaces. Retained only three primary sections plus the selected visual that materially change first-pass understanding on each route; deeper controlled material remains under progressive disclosure.

## EN ↔ AR / viewport inspection

Inspection order followed the session rule: Arabic 390px, Arabic 1440px, English 390px, English 1440px. Representative rendered output was inspected using screen-mode static rendering because the environment's Chromium instance blocks local/file navigation by administrator policy.

Accepted checks:

- long Arabic People and Access headings wrap without collision;
- RTL reading order is coherent in the hero, reading rule, scope band, evidence blocks and actions;
- English and Arabic retain the same semantic hierarchy and verification destinations;
- mixed Latin stable IDs appear only where verification legitimately benefits from them;
- mobile composition preserves the strongest answer before deeper evidence;
- desktop composition uses negative space and scope adjacency rather than a KPI/card wall.

This is S03 composition acceptance, not the final browser/a11y release acceptance owned by S05/S07.

## Machine verification after final S03.1 edits

- Build: `Built 284 HTML files from 141 controlled page specs.`
- Validator: `HTML=284 ERRORS=0 WARN=0`
- Result: `WEBSITE REPOSITORY VALIDATION PASS`
- Checksum manifest reconciled to canonical first-hand files; stale local `__pycache__` references removed.
- EN/AR target pages: one H1 each; no target route contains the prior answer-card dump.
- Direct People evidence-record links resolve to controlled generated routes.
- The frozen `page_specs.json` hash is unchanged during S03.1: `1319433fed3503cd7ad98203179db5a4a8438906e3e95464b80f36327497b41e`.

## Friction / delay register

| Classification | What happened | What it affected | Resolution | Can recur? |
|---|---|---|---|---|
| REPOSITORY / ACCESS | Drive folder responses can be truncated, making direct discovery of a named control unreliable. | Initial authority/control reopening. | Located the canonical control IDs once and verified the live Authority directly. | Yes; next window should reuse canonical IDs and verify by ID rather than broad rediscovery. |
| TOOL LIMITATION | Headless Chromium blocks localhost/file navigation in this environment. | Live-browser visual inspection. | Used screen-mode rendered PDFs/PNGs plus HTML structure checks; left full browser/a11y acceptance to its named later sessions. | Yes in this runtime. |
| BUILD DEFECT / SELF-CREATED REWORK | An intermediate route-dispatch edit temporarily removed the hero from non-domain routes, producing 276 missing-H1 validator failures. | Global build validity during S03.1. | Restored non-domain hero dispatch and reran the global build/validator to zero errors. | Preventable: always run global validator after every domain-dispatch change. |
| SELF-CREATED REWORK | A duplicate S03 CSS block was temporarily appended during reconciliation. | Source cleanliness. | Removed the duplicate; one S03 composition block remains. | Preventable through targeted patching plus duplicate-selector check. |
| DESIGN AMBIGUITY | Dense People and sparse Access cannot safely be forced into identical visual density. | Domain grammar decision. | Kept one coherent reading grammar with route-specific selected evidence and disclosure depth. | Expected, but now the established S03 pattern. |
| ARCHIVE DISTRACTION | One new `Old drafts` pointer appeared after the S01 archive baseline. | S03.1 orientation only. | Reviewed once, dispositioned design-only and moved to the reviewed-design archive; no blanket re-review. | Delta-only control prevents recurrence as broad archive work. |

## End-of-session rationalization

1. **What became more true?** Scope, time, geography and non-inference boundaries now travel with the strongest answer instead of depending on later cards or methodology context.
2. **What became more usable or simpler?** People is substantially less burdensome; Access is shorter in cognitive terms and treats missing national geography as a deliberate evidence state. Both expose a clear verification path.
3. **What complexity was introduced?** A domain-answer renderer and route configuration now sit alongside the generic renderer. The complexity is bounded and explicit.
4. **What was removed / merged / retired?** Repeated answer-card walls and generic section repetition were removed from these public domain routes; controlled evidence remains in the evidence/source layers.
5. **What defects remain?** No material S03.1 composition defect. Full live-browser, keyboard, zoom, screen-reader and release-level RTL testing remain intentionally assigned to S05/S07.
6. **Production Master escalation?** **No.** No semantic/evidence/source/rights/publication defect was found.
7. **Why is S03.2 next?** The grammar now needs a harder denominator/evidence-class test: formal-firm survey evidence plus programme KPIs, and finance-system evidence with different stocks/flows/clocks.

## Boundary decision

**PROCEED** — S03.1 passes its exit criteria. S03.2 may begin only after this accepted implementation and its control state are synchronized to the canonical Google Drive repository.
