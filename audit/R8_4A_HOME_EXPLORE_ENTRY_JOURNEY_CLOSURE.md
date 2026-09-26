# R8.4A — Home + Explore + Governed Question Entry Journey Closure

**Status: CLOSED / PASS**  
**Parent programme:** R8.4 — Public corpus + user-journey acceptance (**still active**)  
**Scope boundary:** Home, Explore, the 11 governed entry questions, visible About navigation label, and the runtime/validation path needed to keep those surfaces subordinate to the Production Master. No Reading, Measurement priority, evidence value, claim, source relationship, rights state, route family, or visual contract was added or removed.

## 1. Entry state

Live authority was re-read before work and again immediately before promotion.

- Production Master SHA-256 before: `054484e8403b017885e74d61a03ed4abe3bbb51e77ef718f788d499f1eb1c59c`
- Page Specs SHA-256 before: `8e4603964d8741ce5578a385a17ca0bbdc08f8d40e172b8f69b6b12e497dcc8a`
- Live Drive bytes were unchanged at the pre-promotion concurrency check.
- No final Claude H1–H5 hand-back was present; this was therefore executed as a bounded OpenAI-owned R8.4 sub-session after the user stated Claude had stopped.

## 2. Why this scope was chosen

Home + Explore is the highest-leverage public surface because every audience passes through the same orientation problem before reaching a domain, Reading, Evidence Record or source. The test was not “is the copy attractive?” but whether a first-time user can:

1. understand what the product is;
2. start from a real question rather than a dataset taxonomy;
3. see the strongest bounded evidence without false comparability;
4. understand a material limit early;
5. move to deeper evidence and verification without learning internal architecture.

## 3. Material defects found

### A. Competing entry taxonomies
The runtime rendered a five-task Home orientation layer in addition to the governed 11-question system. That created two competing mental models for the same product.

**Decision:** remove the parallel task taxonomy. Home now exposes four common governed questions; Explore is the one complete 11-question surface.

### B. Runtime factual duplication outside the Master
Home hard-coded its three evidence signals and a conceptual chain in `build.py` even though the current Page Spec already contains governed Home claims/visuals. This created drift risk.

**Decision:** remove those hard-coded facts. Home now renders the current Page Spec sections and governed `VIS-INCLUSION-TRANSMISSION` visual through the same generic governed-visual fallback used elsewhere.

### C. Internal IDs exposed to readers
Question cards displayed `QE-00x` identifiers. They support traceability but do not help a public user and became especially confusing when questions were grouped thematically.

**Decision:** stable IDs remain as non-visible `data-question-id` attributes only. No question number/ID is shown to the reader.

### D. Product-team/meta prose on Explore
Arabic Explore contained public copy describing what “the page asks the user to do” and referred unnecessarily to the product as a system. This was product-design language, not reader-facing economic/editorial language.

**Decision:** rewrite Arabic and English natively around the decision question, evidence relevance, limits, unknowns and verification.

### E. Residual overstatement in the microfinance entry question
`QE-006` still used `MICROFINANCE_TRANSFORMATION` and “institutional transformation/change” framing although R8.3 had already narrowed the underlying analytical Reading away from presupposing transformation.

**Decision:** replace it with a multi-metric diagnosis: borrower reach, savers/depositors, nominal portfolio and provider structure remain separate measures rather than one inclusion measure.

### F. Unnecessarily interpretive digital-finance wording
`QE-004` framed the alternative as a “transactional workaround.” That language can suggest a conclusion before current durable-use evidence exists.

**Decision:** ask the observable question instead: whether durable use is emerging or the available evidence still mainly measures infrastructure and transactions.

## 4. Master-first change ledger

### `02_SITE_MAP`
- Row 121 `title_en`: `Start with the question.` → `Start with the question, not the dataset.`
- Row 121 `full_copy_en`: rewritten to remove product-system/meta framing and duplicate question summaries; preserves the six public evidence questions, comparability boundary, unknown state and 11-question entry.
- Row 121 `full_copy_ar`: native Arabic rewrite; removes “بدل أن تطلب من المستخدم...” and product-team narration.
- Row 124 `full_copy_en` and `full_copy_ar`: regenerated from the cleaned Home sections so the monolithic projection no longer carries the duplicate entry narrative.

### `03_PAGE_SECTIONS`
Home:
- row 6 `body_en`; row 7 `body_ar`: direct answer→evidence→limits→source journey; removes “the system keeps...”.
- row 8 `body_en`; row 9 `body_ar`: keeps the same governed 11.9%, 12.91pp and POS evidence but removes unnecessary product-system subject language.
- row 12 `heading_en`: `The system moves on different clocks` → `Different evidence describes different moments.`
- row 14 `heading_en`: `From rule to result, no missing link is silently crossed` → `From rule to result, every link needs evidence.`
- rows 14–15 chain: inserts the explicit **implementation** stage, preserving `rule/investment → implementation → operation → access → use → quality/protection → outcome`.
- row 16 `heading_en`: `What the system still cannot tell you` → `What we still do not know`.
- rows 20–21 and 308–309: remove duplicate 11-question explanatory dumps; structured question cards now carry the questions themselves.

Explore:
- rows 301–309: native EN/AR rewrite of the entry logic, six evidence questions, comparability warning, unknown-state rule and 11-question introduction.

### `04_NAV_UX`
- row 11 `label_ar`: `عن المنظومة` → `عن الموقع`.
- row 11 navigation JSON Arabic label updated identically.
- row 34 `/about` Arabic surface label updated identically.

### `05_QUESTIONS`
- `QE-001` user outcome: removes internal “system view/evidence clocks” language in favor of different measurement dates and unmeasured links.
- `QE-002` user outcome: `population anchors` → `population measures`; Arabic rewritten natively.
- `QE-003` user outcome: `state-by-state` → `stage-by-stage`; Arabic: `تتبّع كل مرحلة من القاعدة إلى النتيجة`.
- `QE-004` question EN/AR: replaces “transactional workaround” with the observable infrastructure/transactions-versus-durable-use boundary.
- `QE-006` question, answer mode and user outcome: `MICROFINANCE_TRANSFORMATION` → `MICROFINANCE_MULTI_METRIC_DIAGNOSIS`; removes presupposed transformation.
- `QE-007` question EN/AR: moves from causal-sounding “connect” to “what do the flows tell us about the household connection”; user outcome tightened.
- `QE-010` user outcome: removes the technical phrase “plausible data holders” in favor of where the missing evidence may come from.

**Invariant:** the set of 11 governed questions and their primary routes did not change.

## 5. Runtime/implementation changes

`site-src` and scripts remain subordinate implementation only.

- Home shows **four common governed questions**, not a new taxonomy.
- Explore shows **all 11 governed questions**, grouped into four intelligible discovery clusters.
- Stable `QE-*` identifiers remain available for traceability in `data-question-id` and are not visible to readers.
- Visible question numbering was removed because thematic grouping made the internal number sequence jump and added no user value.
- Home factual signals are no longer hard-coded in `build.py`.
- Home renders `VIS-INCLUSION-TRANSMISSION` from the governed Page Spec with ordered-text, image-independent and non-colour semantics.
- Explore does not render a prose duplicate of the 11 questions before the structured cards.
- Arabic About navigation now reads `عن الموقع`.

## 6. Options explicitly rejected

1. **Turn Home into a dashboard** — rejected because the headline measures have different units, universes and evidence clocks and would invite false comparability.
2. **Show all 11 questions on Home and again on Explore** — rejected as duplication; Home is orientation, Explore is complete question discovery.
3. **Keep a separate five-task entry model** — rejected because it creates a parallel public taxonomy not governed by `05_QUESTIONS`.
4. **Keep hard-coded Home numbers/chain in runtime** — rejected because runtime must not become a second semantic authority.
5. **Expose stable question IDs/numbers** — rejected as internal apparatus with no decision value to the public reader.
6. **Add new routes/Readings/Measurement priorities** — rejected; no material user question was unserved by the existing architecture in this scope.

## 7. Arabic and English result

Arabic and English were edited as co-authoritative editions rather than source/translation pairs.

- Arabic product-team/meta prose removed from Explore.
- `عن المنظومة` navigation changed to natural `عن الموقع` without altering the About route or its substantive content.
- Wording about unknowns is direct: the unknown remains unknown and becomes a measurement question rather than an undocumented estimate.
- English “system” references were removed where the reader only needs the evidence or resource.
- No number, unit, universe, period, source, certainty, rights boundary or measurement-next meaning was widened by the edits.

## 8. Verification

Final local production-equivalent build from the candidate authority state:

- `141` controlled Page Specs.
- `284` HTML documents built.
- `PUBLIC_LITERAL_CLOSURE`: `7,309` numeric/public-literal records; `0` unresolved substantive public numbers.
- Repository validator: `ERRORS=0`, `WARN=0`.
- Home: 4 compact governed question cards; 0 task cards; 0 visible QE IDs; governed Home visual present.
- Explore: 11 governed question cards; 4 thematic clusters; 0 task cards; 0 visible QE IDs.
- Arabic/English About navigation resolves correctly.
- `build.py` contains no hard-coded `11.9%`, `12.91`, `561 → 1,473`, `MICROFINANCE_TRANSFORMATION`, or `task_starts` literal/parallel taxonomy.

## 9. Five-reviewer challenge

- **Yemeni practitioner:** entry language is now less technical and does not make the user learn the repository model before the subject. PASS.
- **International FI specialist:** access/use/infrastructure/outcome and durable-use boundaries remain explicit; no composite/dashboard inference introduced. PASS.
- **Regulator/supervisor:** rule/implementation/operation/access/use/quality/outcome stages are explicit and no regulatory action is equated with population outcome. PASS.
- **Statistician/methodologist:** clocks, population/calculation base, unknown state and non-comparability remain visible; no metric was redefined. PASS.
- **Hostile fair reviewer / senior Arabic editor:** strongest objections found were duplicate entry taxonomies, runtime hard-coding, visible internal IDs and meta Arabic prose; all are closed in this scope. PASS.

## 10. Authority state after this sub-session

- Production Master SHA-256 candidate after: `e69804106e04d093098688f2d01cea51e13191f255d774a090f3e5dd8dec9bc7`
- Page Specs SHA-256 candidate after: `ff2b0f559cde5fede3fe31d7dfb2539a00921e8b00b816c2863790cd9de49007`

These hashes become production hashes only after the tested bytes are promoted in place to the existing Drive file IDs and read back successfully.

## 11. What became more true / simpler

**More true:** the public entry now follows the actual governed question system and the R8.3 analytical boundaries; microfinance and digital-finance questions no longer presuppose conclusions the evidence has not established.

**Simpler:** one entry model instead of two; four Home starting questions instead of an extra task taxonomy plus questions; one governed Home visual instead of a runtime parallel; no public stable-ID clutter.

**More complex:** nothing in the evidence model. The only added implementation discipline is that Home now consumes governed objects rather than literals.

## 12. Material issues deliberately left outside scope

- This does **not** close the rest of R8.4.
- The known Reading full-copy/stale-projection and public-language targets remain for a later bounded session.
- Provider/regulatory currentness remains time-varying. A primary CBY decision released after the current overlay must be adjudicated Master-first before provider status is treated as current.
- No claim is made that the product is `DESIGN HANDOFF READY` or `PUBLIC RELEASE READY` from this sub-session alone.

## 13. Next bounded session

**R8.4B — Provider/regulatory currentness + Resource Library integration.**

Reason: provider regulatory status is the clearest time-sensitive factual frontier now known, and the recent CBY decision sequence tests both the provider-status overlay and whether laws/decisions/reports/surveys can be discovered coherently through one Resource Library rather than new silo pages. This should be closed before final editorial freeze so the next language pass is performed against the latest accepted controlled truth.

After R8.4B, the next highest-value editorial sub-session is the 10 Readings + 10 Measurement Agenda cards, including the R8.3 wording/stale-full-copy targets.
