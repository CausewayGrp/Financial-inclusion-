# CLAUDE TRANCHE B — CONTINUATION HANDOVER TO NEXT WINDOW
# تسليم استمرارية المرحلة (ب) إلى النافذة التالية

**Product:** Yemen Financial Inclusion Evidence / أدلة الشمول المالي في اليمن
**Programme phase:** R8.4 · Tranche B (bilingual · analytical · visual · search · trust maturation, + Economic/Benchmark Enrichment Addendum)
**Handover written:** 2026-09-25, ~19:20 Africa/Cairo, by the Tranche B Team Lead (Claude)
**Handover reason:** context-window continuation. The next window must resume Tranche B **exactly** from this point and carry it to closure.
**Allowed final programme status (unchanged, hard constraint):** `CLAUDE MATURATION HAND-BACK READY`. Tranche-level target: `TRANCHE B COMPLETE — READY FOR INDEPENDENT REVIEW`. **Never** declare `DESIGN HANDOFF READY` or `PUBLIC RELEASE READY`. **Do not** start Tranche C.

> This is a working continuation document, not a closure. It supersedes no Tranche A audit lineage. When Tranche B closes, the closure lives in `audit/CLAUDE_TRANCHE_B_CLOSURE.md`; this file is the bridge to get there.

---

## 0. HOW TO RESUME (READ THIS FIRST — 10-MINUTE PROTOCOL)

Do these, in order, before touching anything:

1. **Re-verify authority bytes.** Run:
   ```bash
   cd /home/claude/work/Yemen_Financial_Inclusion_Evidence
   sha256sum authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx site-src/content/page_specs.json
   ```
   Expect **Master** `e69804106e04d093098688f2d01cea51e13191f255d774a090f3e5dd8dec9bc7` and **Page Specs** `ff2b0f559cde5fede3fe31d7dfb2539a00921e8b00b816c2863790cd9de49007`. If either differs: **stop semantic execution, diagnose, record actual state** (brief §1). Do NOT restore the expected hashes; determine the true current authority.
2. **Confirm the repo is green.** `python3 scripts/build.py && python3 scripts/validate.py` → expect `HTML=284 ERRORS=0 WARN=0 … VALIDATION PASS`. `sha256sum -c SHA256SUMS.txt` → expect `58/58 OK` (see §3 note on manifest scope).
3. **Read the three governing inputs** in this repo/project (they are binding, in this precedence): the Tranche A constitution (project description), the Tranche B brief (`/root/.claude/uploads/455962bf-22d3-55fd-b377-b99b7b279118/52a566bf-attachment.txt`), and the **Economic/Benchmark Enrichment Addendum** (`/root/.claude/uploads/455962bf-22d3-55fd-b377-b99b7b279118/1f13592f-attachment.txt`). The addendum "consolidates and supersedes any earlier methodology/indicator-enrichment note" and must be integrated **before** Tranche B closure.
4. **Read this whole file.** §7 (adjudication ledger) and §8 (remaining scope) are the actual work list. §9 gives you verified ground-truth so you do not have to re-discover it (spot-check, don't blindly trust).
5. **Do not re-run analysis waves.** All 11 red-team personas and 10 specialist reviews are complete (§6). Your job is Lead integration → write artifacts → patch spec → validate → ZIP → Arabic hand-back. Only re-open a finding if you find a *material* error in it.

**The single most important rule of this whole programme:** the Master→projection **generation pipeline is absent** from the repository. You therefore **cannot** safely install semantic edits. You perform the full intellectual maturation and capture every semantic change as an **execution-grade Master-first patch** (`audit/MASTER_FIRST_PATCH_SPEC.csv` + narrative) while keeping the **live repository green and unchanged** at the semantic layer. See §4.

---

## 1. WHAT THIS PRODUCT IS (ORIENTATION)

A mature, governed, bilingual (Arabic/English co-authoritative) **public evidence product** about financial inclusion in Yemen. Architecture you must not casually dismantle:
- **One Production Master** (`.xlsx`) = sole semantic authority over facts, claim meaning, unit, universe, denominator, geography, period, fieldwork/currentness, method, evidence state, source authority, rights/publication state, provider status, controlled public copy, measurement meaning. Everything else (page specs JSON, content JSON, search records, built HTML, diagrams, prompts) is a **subordinate projection**.
- **Controlled scale (verify from repo; inventory facts, not quality):** ~141 page specs · 11 governed entry questions · 108 evidence objects · 59 public claims · 55 evidence passports · 10 Evidence Readings · 10 Measurement Agenda priorities · 36 governed visual contracts · 159 source records (158 publicly addressable) · 26 curated resource cards · 427 search records · 284 built HTML.
- **North Star journey:** QUESTION → STRONGEST DEFENSIBLE ANSWER → WHAT IT MEANS → WHAT IT DOES NOT ESTABLISH → SYSTEM CONTEXT → WHAT REMAINS UNKNOWN → WHAT SHOULD BE MEASURED NEXT → EVIDENCE → METHOD → SOURCE. Model: **UNDERSTAND → EXPLORE → VERIFY**.
- **Eight domain routes:** `/people/ /firms/ /finance/ /providers/ /payments/ /remittances/ /access/ /reforms/`.
- **Semantic firewall (never collapse):** people ≠ households ≠ firms ≠ accounts ≠ active accounts ≠ customers ≠ transactions ≠ terminals ≠ agents ≠ providers ≠ beneficiaries; access ≠ ownership ≠ registration ≠ adoption ≠ active use ≠ frequency ≠ persistence ≠ quality ≠ outcome; infrastructure ≠ use; target ≠ result; programme KPI ≠ national prevalence; licence/listing ≠ operation; observed ≠ estimated ≠ projected; missing ≠ zero; chronology ≠ causality; source-owner analysis ≠ independently established impact.

---

## 2. BINDING GOVERNING INPUTS & PRECEDENCE

Three documents govern, in this precedence (later corrections override earlier defaults where they conflict):
1. **Tranche A constitution** (58 sections; the project description). Establishes authority model, one-Master rule, master-first correction chain, multi-agent safety rule, semantic firewall, status vocabulary, IA options.
2. **Tranche B brief** (`52a566bf-attachment.txt`, 61 sections). Accepts Tranche A "with narrow corrections"; sets Tranche B scope, the Master-first patch-package mandate (§44), change types (§45), before/after rule (§46), status vocabulary (§57), red-team panel (§52), the 12 required artifacts (§54), ZIP naming (§59), Arabic hand-back (§60), stop condition (§58).
3. **Economic/Benchmark Enrichment Addendum** (`1f13592f-attachment.txt`, 26 sections). Expands scope: economic-function lens, targeted benchmark review, signature system map, evidence clock, evidence coverage matrix, methodology completeness, source-admission policy, source-narrative extraction, economic-context policy, financial-health/quality/cost/identity/G2P dispositions, country-comparator policy, OECD/INFE method integrity, indicator-library role, design-aware content contract, signature-visual candidates, and **7 additional required artifacts** (§24). Adds to the expanded Definition of Done (§26): "**MORE EXPLANATORY WITHOUT BECOMING MORE SPECULATIVE.**"

**Cold-start rule (Tranche A §1):** do not trust prior conversations/memory/ZIPs/names. Only what exists in the supplied repository and survives current-authority review is real. A file named FINAL/MASTER/DESIGN/HANDOFF/PROMPT/CLOSURE is not current merely because of its name.

---

## 3. REPOSITORY STATE AT HANDOVER (VERIFIED)

- **Root:** `/home/claude/work/Yemen_Financial_Inclusion_Evidence/` (single clean root; no nested repo).
- **Master SHA-256:** `e69804106e04d093098688f2d01cea51e13191f255d774a090f3e5dd8dec9bc7` ✓ matches expected.
- **Page Specs SHA-256:** `ff2b0f559cde5fede3fe31d7dfb2539a00921e8b00b816c2863790cd9de49007` ✓ matches expected.
- **Validator:** `WEBSITE REPOSITORY VALIDATION PASS` — HTML=284, ERRORS=0, WARN=0. Public-literal closure: 7309 records, 0 unresolved.
- **Manifest:** `SHA256SUMS.txt` → 58/58 OK.
- **Semantic authority UNCHANGED in Tranche B.** No semantic edit has been installed. The only executed changes in the whole programme remain the **S00 validator-blocker fix** (Tranche A: a projection re-bind of 4 recipient-facing handoff files + their manifest lines to the already-correct current Master — master-first compliant because the Master was already correct). Recorded as CHG-0001..0006 in `audit/CLAUDE_FIELD_LEVEL_CHANGE_LEDGER.csv`.
- **Build/validate tooling (safety-scanned):** `scripts/build.py` reads only `site-src/content/*` JSON and writes only `dist/` (`shutil.rmtree(DIST)` then rebuild); **it never parses the `.xlsx`** — this is the concrete proof the generator is absent. `scripts/validate.py` validates the built `dist/` + authority binding; it hashes the workbook but does not read its cells. `scripts/audit_public_literals.py` does public-literal closure. **Important build.py facts:** the footer strapline (line ~65) and the evidence-record "How can I verify it?" block (label at line ~716) are **generated in build.py**, i.e. they live *outside* the Master authority chain — fixing them has both a Master-registration dimension and a build.py dimension (see LEAD-B04, LEAD-B05, LEAD-M07).
- **Manifest scope caveat:** `SHA256SUMS.txt` covers 58 canonical files. New `audit/*.md` and `audit/*.csv` decision artifacts are **not** in the manifest, so adding them does not break `58/58 OK` and does not require a manifest refresh. Only refresh the manifest if you re-bind a file that is already in it. Do not add audit artifacts to the manifest.

---

## 4. THE PIPELINE CONSTRAINT — HOW SEMANTIC WORK MUST BE DELIVERED (NON-NEGOTIABLE)

**Correct status wording (use verbatim; Tranche B brief §2):**
> The Master→projection generation pipeline is absent from the handed repository and must be recovered or deterministically rebuilt before semantic patch execution.

**Do NOT** say "OpenAI holds the generator" (this was a Tranche A error, corrected by the user). **Do NOT:** write semantic changes into JSON projections while leaving the Master unchanged; create a second semantic authority; mirror Master-intended changes downstream "for preview"; edit public projections and call them final.

**You MUST:** fully perform the intellectual/editorial maturation; write exact **Master-first** changes with before/after; produce an **execution-grade Master patch package**; keep the live governed repository internally green; leave semantic patch execution *pending* the restored/rebuilt generation pipeline.

**Correction chain for any semantic change:** SOURCE → VERIFY → ADJUDICATE → MASTER FIRST → REGENERATE → SEMANTIC PARITY → PUBLIC ACCEPTANCE. Never correct only a JSON / webpage / English sentence / Arabic sentence / caption / Reading / prompt. If the semantic source is wrong, fix the Master (as a patch spec here).

**Validation split (brief §56):** CURRENT REPOSITORY VALIDATION (must stay green — you are not installing semantic edits) vs PROPOSED PATCH VALIDATION (each patch states what must be tested *after* OpenAI applies it Master-first and regenerates). Never claim "final public corpus validated" — nothing semantic is installed.

**Status vocabulary (brief §57 — use exactly; never `PASS` for a proposal):** `EXECUTED` · `VERIFIED_BY_CLAUDE_TEAM` · `SPEC_PENDING_EXECUTION` · `PRIMARY_SOURCE_PENDING` · `INDEPENDENT_OPENAI_ACCEPTANCE_REQUIRED` · `EXTERNAL_HUMAN_CERTIFICATION_NOT_PERFORMED`.

**Change types (brief §45):** `EDITORIAL_NO_SEMANTIC_CHANGE` · `BOUNDARY_TIGHTENING` · `SOURCE_CURRENTNESS_UPDATE` · `IA_LABEL_CHANGE` · `CROSS_LINK_CHANGE` · `MEASUREMENT_SCOPE_REFINEMENT` · `READING_THESIS_REFINEMENT` · `VISUAL_CONTRACT_REFINEMENT` · `RESOURCE_METADATA_UPDATE` · `TRUST_COPY_REFINEMENT`. Never call a substantive claim change "editorial."

---

## 5. BINDING TRANCHE A CORRECTIONS (FROM OPENAI/USER — CARRY INTO ALL TRANCHE B OUTPUT)

These are binding and already reflected in the adjudications in §7. Do not regress them:
1. **Generator framing:** use the §4 wording; never "OpenAI holds the generator."
2. **`/finance/` mission is broader — formal finance AND microfinance** (brief §18). Do **not** redefine `/finance/` as a microfinance page. (My Tranche A CHG-0015 wrongly framed tightening-to-microfinance as the fix; corrected.)
3. **`/reforms/` FMIIP Jan-2025 zeros are historical project baseline observations** (brief §22). Do **not** write "baseline zero → reform has not translated into use." Structure: HISTORICAL BASELINE → later implementation → currently observed operational → currently measured access/use/quality/outcome → remaining unknown.
4. **`/access/`** — do **not** call the exchange/remittance roster "Yemen's largest physical cash-access channel." Acceptable: "official source lists document a substantial exchange/remittance provider presence relevant to the access question." (I used the prohibited phrase in `DOMAIN_CORPUS_EDITORIAL_CLOSURE.md`; it must not reappear.)
5. **Cross-domain:** do **not** use "absence of a functioning formal credit/deposit channel." Prefer the §24 measured-survey formulation.
6. **`/people/`** — do **not** foreground the 3.37× ratio; prefer female level / male level / 12.91pp (brief §15). Education 6.98% is a **level**, not a gap; state `PARTIAL_HOLD_FOR_COMPLETE_PAIR` (brief §14).
7. **`/remittances/`** — no automatic MA-011; first extend MA-001 (brief §21).
8. **Domain→Reading:** `governed_readings=[]` is real but NOT permission to populate all eight mechanically; apply per-pair RELEVANCE/ADDITIONAL-VALUE/NON-DUPLICATION/USER-BENEFIT/DELETION tests → SURFACE / CONTEXTUAL LINK / NO LINK (brief §25).
9. **MA-003:** a measured income-group *comparison* does not establish income as a *causal mechanism* (brief §16). (Note: current MA-003 text already handles the causal side correctly; the real defect is the *omitted measured income-level gap* — see LEAD-M03.)

---

## 6. WHAT HAS BEEN DONE IN TRANCHE B SO FAR

**Multi-agent review is COMPLETE. Do not re-run it.** Executed as hub-and-spoke; specialists proposed, Lead adjudicates. Waves completed:

**Specialist waves (10 reports received & incorporated):**
- **Readings:** 9 KEEP + CWR-009 KEEP-with-boundary-tightening; 0 MERGE/RETIRE/NEW. MATERIAL projection defect: CWR-010 missing its only direct-source paragraph (G2Px pilot, "45,460 recipients / eight districts"). Systematic "the system"/«المنظومة» self-reference drift. CWR-001 leaks internal jargon (E&O, CCY 7.4bn, 1.838, 33%). Confirmed Readings contain **no** "baseline zero → reform has not translated into use" phrasing.
- **Measurement:** 8 KEEP; **MA-003 REWRITE** (add measured income-group difference; keep causal firewall); **MA-001 REWRITE** (extend scope to remittance receipt/channel/frequency; bind `/remittances/`); **no MA-011** (fails deletion test). Flag: no CLM exists for the income-group gap though FSG-0004 is `PUBLIC_SAME_WAVE_GAP_READY`.
- **Visuals:** 24 KEEP / 12 REFINE / 0 MERGE / 0 RETIRE; 17 execution specs (R1–R17). VIS-FINDEX-GAPS accessible summary omits the income gap (detached-use failure). Surface finding: 13 orphaned ungoverned visual pages at `/evidence/<id>/` with `public_route_list: []`; and `governed_visual_contracts=[]` on the 24 *governed* visual pages too (binding failure larger than the 13 orphans).
- **Arabic:** canonical terminology matrix delivered; «المنظومة» used as product self-referent (206 built instances, 108 of them one boilerplate line — see §9); four competing self-referents; calques («كائن», «عنصر», «صف مصرفي», «منزوَع الازدواج»); primary-nav AR labels not migrated while footer is. KEEP Tier-1 native: the 11 questions, 10 reading titles, 10 measurement titles, home hero.
- **English:** "in the system" backend voice inside the flagship 11.9% sentence across ≥5 routes; "report-specific finance-filtered base"; "object exposed"; privacy subtitle. MATERIAL: `accessible_summary_en` for RV-CWR-002…010 are drawing instructions, not reader prose — 9 rewrites supplied.
- **Search:** 18 PASS / 8 WEAK / 2 FAIL (EN); 16/9/3 (AR). `SRC-MOPIC-YSEU-2023-080` missing from index (159 vs 158); 132 LOCATOR_ONLY records invisible; `does_not_establish` never reaches search ("law" = 0 hits); no stemming; 2 of the repo's 9 smoke tests fail at top-10. R1–R13 fixes; **rejected** a broad issuer-only alias; **caveated** the education↔literacy alias.
- **Trust:** F-01 `/evidence/compare/` Arabic lists fewer compatibility dimensions than English (parity break; EN carries universe/unit/period/method/evidence-type/denominator/geography); F-02 "incompatible" not stated as a valid result; F-03 one byte-identical boilerplate across all 108 evidence records; F-04 `limitations` pipe-merges prohibited-inference with measurement-limitation; F-05 `/data/` claims line missing its count (59); F-06 unit-less vintage figures; F-07 `/data/` chronology duplicated; F-08/F-09 editorial. **No CauseWay over-claim found.**

**Red-team panel (brief §52) — 11 personas across 3 agents, COMPLETE.** Raised BLOCKER candidates that contradicted my Tranche A §5 "no BLOCKER misstatement and no false public number." **I (Lead) have since independently verified every load-bearing candidate against repository bytes** — see §7 and §9. The Tranche A "no BLOCKER" statement is **overturned by verified evidence** and must be reconciled honestly in `CLAUDE_TRANCHE_B_CLOSURE.md` (do not delete the Tranche A record; annotate that Tranche B's deeper `dist/`-level + FX-deflated audit found defects the domain-skeleton pass did not).

**Lead verification performed this session (bytes checked, not taken on trust):** finance sign-reversal + deflator + missing benchmark; remittances evidence-state; CLM-008 EN/AR asymmetry; source-closure mechanism; 9.00 precision inputs; accessibility artifacts; FMIIP baselines held-but-unpublished; findex parallel block; global_navigation schema + header component; strapline & meta-description build.py lines. All confirmed (§9).

**Not yet done (the remaining work):** writing the Tranche B artifacts (§8), building the patch spec, integrating the addendum's 7 new artifacts + scope, validating, ZIP, Arabic hand-back.

---

## 7. LEAD ADJUDICATION LEDGER (VERIFIED SEVERITIES + DISPOSITIONS + EXECUTION-GRADE BEFORE/AFTER)

Every item below is **VERIFIED_BY_CLAUDE_TEAM** against repository bytes unless marked otherwise. Disposition + change_type are the Lead decision. All are `SPEC_PENDING_EXECUTION` (Master-first) unless noted; none is installed. IDs are Tranche B patch anchors (use `PB-####` in the CSV; the `LEAD-*` tags here map to them).

### BLOCKERS (verified false/misleading public content or broken verification mechanism)

**LEAD-B01 — `/finance/` nominal microfinance comparison is a sign-reversal. [BLOCKER]**
- Object: `/finance/` `full_copy_en` + section copy (**live in `dist/en/finance/index.html`**), mirrored in Reading **CWR-006** (`/readings/microfinance-structural-divergence/`) and claim **CLM-054** (`claim_type: BOUNDED_DIRECTIONAL_DIVERGENCE`).
- Current (verbatim, shipped): *"That source also reports 3.3 million active savers and about YER 44 billion in nominal portfolio in 2023, compared with verified 2020 anchors of 1.611 million savers/depositors and YER 33.379 billion."* → reads as +31.8% growth.
- Verified: the deflator is in the product's own governed `site-src/content/data/cby_monetary.json`, `YER_USD_MARKET_RATE` (`SRC-CBY-001`): 2020-12 = **792.69**, 2023-12 = **1,529.40** (+92.9% depreciation). Deflated: 33.379bn ÷ 792.69 = US$42.1m → 44bn ÷ 1,529.40 = US$28.8m = **−31.7%**. The sign reverses. CWR-006 itself says "Interpreting nominal portfolio growth as real deepening requires an explicit price/FX treatment" — and none is supplied.
- Disposition: **BOUNDARY_TIGHTENING / claim-state change.** Never publish the 33.379→44 pair without a stated deflator and **both** directions (nominal +32% / FX-deflated −32%, deflator named + limits). Delete "active" from savers (metric MFM-002 is "voluntary depositors/savers"; "active" unsupported). Replace "fell from 93,118 … to 88,445 …" harmonized-trend wording with the anchor formulation already in `full_copy_en` ("Verified anchors record…"). Downgrade **CLM-054** from `BOUNDED_DIRECTIONAL_DIVERGENCE` to four bounded anchors until a provider-universe bridge exists (CLM-054 body already concedes the universes are not reconciled). Master-first; regenerate CWR-006 + CLM-054 + `/finance/` from Master.
- Note the binding correction: keep `/finance/` as **formal finance AND microfinance** — do not solve this by narrowing the page.

**LEAD-B02 — `/finance/` leaked authoring instruction, shipped to the public. [BLOCKER-editorial]**
- Object: `dist/en/finance/index.html`, under `<h3>An evidence-based chronology of the financial system</h3>` (source: `/finance/` `full_copy_en`/section, id ~FIN-06).
- Current (verbatim, shipped): *"Use the documented system chronology as contextual navigation around Finance rather than as a long narrative block. Show only the events that materially help explain funding, liquidity, exchange-rate conditions, intermediation or payment infrastructure, and let users open the dated event record for source and limitations."*
- Disposition: **EDITORIAL_NO_SEMANTIC_CHANGE** (removal of non-public authoring copy). Strip the instruction from the Master field; regenerate.

**LEAD-B03 — `/finance/` publishes no formal-credit benchmark though the Master holds it. [MATERIAL→BLOCKER for the page's core question]**
- Verified: `cby_monetary.json` holds `BANK_CREDIT_PRIVATE_SECTOR_BN_YER` 2023 = **1,679bn**; the string `1,679`/`1679` appears **0 times** in `dist/`. Microfinance book ≈ 2.6% of formal private-sector credit — the sizing the page exists to give.
- Disposition: **BOUNDARY_TIGHTENING / claim-add.** Publish a formal-credit magnitude alongside the microfinance book, each with its own universe/unit firewall, so formal finance and microfinance are related without being collapsed (brief §18).

**LEAD-B04 — Meta description renders a forbidden `*_internal` field; Arabic pages get English descriptions. [BLOCKER, cheapest fix]**
- Object: `scripts/build.py:1224` — `desc=(spec.get('primary_user_question_internal') or '')[:180]`. Verified: `<meta name="description">` on **141/141 EN and 141/141 AR** pages is the raw `primary_user_question_internal` (English) verbatim, e.g. `dist/ar/index.html` → *"What can we responsibly say about financial inclusion in Yemen, and where should I start?"*. Two breaches: (a) every spec's `frontend_render_policy.never_render_directly` lists `"*_internal"`; (b) Arabic edition has zero Arabic in its most public string (search snippets, social unfurls).
- Disposition: **build.py fix (projection-layer, integrity-safe) + governance note.** `title` already resolves per-language via `locv(spec,'title',lang)`; `desc` must too — add a governed, per-language `meta_description_en/ar` field to the Master and render that; the one-line build fix (stop rendering `*_internal`) may be applied to the live repo as a projection fix **only if** it does not change semantic authority. Recommended: register `meta_description_*` in Master (semantic, patch-spec) AND correct build.py to consume it. Until then, the honest interim is to render the localized `title` as description rather than an `*_internal` field.

**LEAD-B05 — Arabic footer strapline «الادعاء» is ungoverned and reads forensic. [BLOCKER, Arabic-only]**
- Object: `scripts/build.py:65` (generated, **outside** the Master). Current (verbatim): «طوّرتها وتديرها CauseWay. **مورد عام يربط الادعاء بالدليل والمصدر**.» (EN counterpart: "A public resource linking claims to evidence and source.")
- Verified concerns: (a) EN plural "claims" → AR singular «الادعاء»; (b) «الادعاء» collocated with «عام»/«الدليل» reads in the forensic/prosecutorial register ("linking the *allegation* to the *proof*"); (c) it is generated in build.py, i.e. the product's Arabic self-definition sits outside the one-authority chain. Note: the token «ادعاء/ادعاءات» for "claim" is **pervasive across governed content** (page_specs, questions.json, /data/ category «ادعاءات عامة مسندة بالأدلة», the 10 «افتح الادعاءات» routes) — so this is a **corpus-wide terminology decision**, not only a build.py line.
- Disposition: **register the strapline in the Master as controlled public copy** (must not live in build.py) and choose a neutral evidentiary noun; the Arabic terminology ledger must decide corpus-wide whether to keep «ادعاء» (defensible in some registers) or move to «العبارات المسندة» / «الإفادات المسندة». This is a **VERIFIED_BY_CLAUDE_TEAM** editorial recommendation, **EXTERNAL_HUMAN_CERTIFICATION_NOT_PERFORMED**. Sweep must cover the strapline, `/data/` category label, and the 10 evidence-route lines together.

**LEAD-B06 — `/remittances/` publicly upgrades evidence state to "observed history" and splices two IMF vintages as one line. [BLOCKER]**
- Object: `evidence_objects.json` → `VIS-REMITTANCE-MACRO`; mirrored in `/remittances/` `full_copy_en` and `dist/{en,ar}/remittances/`, `dist/{en,ar}/evidence/VIS-REMITTANCE-MACRO/`.
- Current (verbatim):
  - `title_en` = "Remittances — observed history vs outlook"; `title_ar` = «الحوالات: تاريخ مرصود مقابل التوقعات»
  - `summary_en` = "The series treats 2018–2024 as observed history, including US$1,861.7 million in 2024; 2025 is an estimate at US$1,977 million, while 2026–2030 are projections rising from US$2,159 million to US$3,110 million…"
  - `method_en` = "Line with observed, estimate and projection states visibly distinct by label and line treatment."
- Verified against `site-src/content/data/remittances.json`: 2018–2024 rows carry `period_state = HISTORICAL_REPORTED` (**not** OBSERVED) + `calculation_state = SOURCE_REPORTED__IMF_STAFF_CALCULATIONS`, `series_vintage = 2025_ARTICLE_IV_STAFF_REPORT`; 2025 + 2026–2030 rows carry `series_vintage = 2025_ARTICLE_IV_SUPPLEMENTARY_REVISION`, `comparability_state = LATEST_ARTICLE_IV_REVISION_FOR_FORECAST_HORIZON`. Two documents, two vintages, drawn as one line; the word "supplementary" appears nowhere public.
- Disposition: **BOUNDARY_TIGHTENING.** Replace public rendering of `HISTORICAL_REPORTED` with a stated term — EN "IMF-reported history (staff calculations)", AR «تاريخ وفق تقديرات خبراء الصندوق» — and **delete "observed"/«مرصود»** from the visual title/summary/method and the `/remittances/` heading/body. Render the 2024→2025 join as an explicit **vintage break** (both document labels), exactly as the product already renders the e-money universe break — or drop the forecast segment until the supplement's restated history is ingested. Add `series_vintage` to the visual's inputs + accessible summary. Define or retire the orphan term `HISTORICAL_REPORTED` in the methodology glossary. Master-first.

**LEAD-B07 — Source-verification layer is hollow: object-level lineage empty, closure certified over nothing, route-union rendered as lineage. [BLOCKER, structural — breaks VERIFY]**
- Verified: `evidence_objects.json` → `source_dependencies` empty on **108/108**; `source_links` empty on **80/108**. `public_object_source_closure.json` closure_state counts: `NO_SOURCE_EXPECTED` = **75**, `CLOSED_TO_SOURCE_ID` = 40, and `CLOSED_VIA_CONTROLLED_DEPENDENCIES` stamped on **108/108** — i.e. closure is asserted "via controlled dependencies" while the dependency field is empty on every object. Rendered "Source verification path" is a **route-level source union**, not object lineage (red team verified: `VIS-REMITTANCE-MACRO` shows two WB RPW corridor sources for an IMF macro chart; `VIS-REMITTANCE-COST` shows the two IMF docs for a corridor-price chart; `CLM-008` — a claim about the bank list — binds 13 exchange/remittance enforcement decisions; `VIS-POS-TERMINALS` bound to the two `BREAK_IN_SERIES` publications). The panel boilerplate even says "Missing bibliography is not filled by assumption" while it is filled by the union.
- Disposition: **BOUNDARY_TIGHTENING + schema change (Master-first).** (1) Split `NO_SOURCE_EXPECTED` into `SOURCE_NOT_YET_BOUND` (open gap, rendered as such) vs a genuinely sourceless class reserved for interpretive framing objects that assert no fact; re-run closure — the pass rate will fall, and that fall is the honest number. (2) Bind sources at **object** level; render only bound sources; until bound, render "source not yet bound," not the route union. (3) De-bundle the four known contaminations. (4) Make **rights** a real field (see LEAD-M13). This is the defect that manufactures false comfort behind the others; the current closure "PASS" measures the wrong thing.

### MATERIAL (verified; high user/truth value)

**LEAD-M01 — CLM-008 EN/AR firewall asymmetry (co-authority parity break). [MATERIAL; BLOCKER for a CBY/counterparty reader]**
- Verified (`public_claims.json`, CLM-008):
  - `does_not_prove_en` = "Do not infer active branches, products, market share or rail participation."
  - `does_not_prove_ar` = «لا يجوز استنتاج الفروع العاملة أو المنتجات أو الحصة السوقية أو المشاركة في أنظمة الدفع. الظهور في القائمة يثبت الإدراج/الترخيص في المصدر فقط، **ولا يثبت التشغيل أو جميع الفروع أو المشاركة أو التغطية الوطنية خارج نطاق سلطة المصدر**.»
- The Arabic carries a stronger authority-scope firewall ("…outside the scope of the source's authority") that English lacks entirely — on the most politically loaded object.
- Disposition: **BOUNDARY_TIGHTENING.** Port the AR clause into `does_not_prove_en` and into the page-level `prohibited_inferences`; bring EN up to AR (co-authority: neither mimics the other, but semantic parity is mandatory). Master-first.

**LEAD-M02 — `/providers/` presents CBY-Aden roster as *the* national universe; divided supervisory authority undisclosed. [MATERIAL]**
- Verified: EN uses "The official CBY 2026 roster" (unqualified); AR «القائمة الرسمية للبنك المركزي» with **no عدن** qualifier; «عدن» appears only 2× on the AR page. All 26 bank rows carry `regulator_scope = CBY_ADEN_SUPERVISION_LIST` with Aden compliance addresses; 4 banks are HQ'd outside Aden's territorial control (Sana'a/Taiz). The corpus holds three `SRC-CBY-SANAA-*` instruments, surfaced on no provider page. The "two central-bank authorities" fact lives only in the `/data/` and `/finance/` chronology.
- Disposition: **BOUNDARY_TIGHTENING.** Qualify every authority reference as **CBY-Aden / البنك المركزي اليمني – عدن** (no bare "official CBY roster" in either language). Add one governed paragraph (both languages): supervisory authority is divided; this product's provider evidence derives from CBY-Aden instruments only; status under any other authority is **not established** (universe definition, not a political statement); **absence ≠ unlicensed**, **presence ≠ permitted to operate in all territory**. Add `issuing_authority` and `territorial_scope` as first-class fields. Master-first. **Preserve** 429 = source-listed rows across three source categories (not firms/providers/access points).

**LEAD-M03 — MA-003 omits the measured income-level gap. [MATERIAL]**
- Verified current `current_evidence_en`: "A 12.91 percentage-point gender gap is measured within the same survey wave. Comparable current inclusion differences by age group and displacement status are not established … and the contribution of identity, device, income, geography, trust and household constraints to any measured disparity is not established." (The causal side is already correct — do **not** record a contradiction; the red team's "MA-003 lists income among not established" was over-stated and I reject that framing.)
- The real defect: the **measured** richest-60/poorest-40 difference (15.5% vs 6.5% = **9.0pp**, `FSG-0004 = PUBLIC_SAME_WAVE_GAP_READY`) is not stated.
- Disposition: **MEASUREMENT_SCOPE_REFINEMENT.** Proposed `current_evidence_en` (illustrative, finalize with statistician caveats): "Within the same survey wave, account ownership differs by 12.91 percentage points between men (18.35%) and women (5.44%), and by about **9.0** percentage points between the richest 60% (15.5%) and the poorest 40% (6.5%) of adults. Comparable current differences by age group and displacement status are not established in the controlled evidence, and the contribution of identity, device, income, geography, trust and household constraints to any measured disparity is not established." **Precision rule (LEAD-M04): 9.0, never 9.00.** Mirror in `current_evidence_ar`. Keep `guardrail_en/ar` ("Do not turn an unmeasured subgroup into a measured gap…"). Add a public CLM for the income-group gap (currently none exists though FSG-0004 is ready).

**LEAD-M04 — Derived-precision + uncertainty discipline. [MATERIAL; "9.00 pp" is BLOCKER-if-shipped]**
- Verified: findex inputs are 1-decimal ("6.5", "15.5"); "9.00" appears **0×** in `dist/` and 0× in findex_baseline — it exists **only in my Tranche A plan**, so it is catchable before it ships. 15.5−6.5 = 9.0 (one decimal); "9.00" manufactures a digit. Also verified: strings `confidence interval / standard error / margin of error / design effect / 95% / ±` occur **0×** across page_specs, passports, claims, codebook — zero uncertainty quantification anywhere, against a documented design (n=1,000; ~23% population excluded; >¼ PSUs replaced).
- Disposition: **BOUNDARY_TIGHTENING.** Cap derived precision at input precision (gender gap 12.91 is the product's own derivation from WB's 5.44/18.35; income gap **9.0**). Publish base-n and an interval (or a stated indicative band) with every derived subgroup gap. State in copy that the gender and income gaps are **not statistically distinguishable** from each other (difference ≈3.91pp, SE≈2.78pp, p≈0.16). Record the statistical reason the 3.37× ratio is dropped (95% CI on the ratio ≈ [2.24, 5.08] by delta method) — this defends the brief §15 decision on evidence, not taste. Also render `US$3.42216 billion` (6 s.f. BOP estimate) as **US$3.42bn**.

**LEAD-M05 — `/people/` ships gap-only; levels absent. [MATERIAL]**
- Verified: `12.91` appears 8× in `dist/en/people/`; `5.44`/`18.35` appear **0×** in any English prose site-wide. A pp gap with no levels understates severity (12.91pp reads like 50↔63, not 5.44↔18.35).
- Disposition: **BOUNDARY_TIGHTENING** (execute Tranche A CHG-0012 with §15 presentation). Lead with female level (5.44%), male level (18.35%), 12.91pp difference; ratio retained deeper only if justified; add the 9.0pp income gap and the 6.98% primary-or-less **level** (labelled a level, `PARTIAL_HOLD_FOR_COMPLETE_PAIR`, never an "education gap"). Master-first; also fix VIS-FINDEX-GAPS accessible summary to include the income gap.

**LEAD-M06 — Evidence-record "How can I verify it?" is builder-facing boilerplate on 108/108. [MATERIAL]**
- Verified: label generated in build.py (~line 716). Body (per red team) is an imperative to producers ("Show the definition…", "…rather than inferring or inventing it"), identical on all 108, and answers no reader's verification question. The "rather than inferring or inventing it" clause volunteers, 108×, that the product might invent sources.
- Disposition: **BOUNDARY_TIGHTENING (Master-first) + build.py.** Replace with a **per-record verification path** built from fields the record holds (source ID, original locator, publication state, reproduction step); where a record genuinely has no independent path, state that as a fact about the record (tie to the LEAD-B07 `SOURCE_NOT_YET_BOUND` split), not as an instruction. Delete "rather than inferring or inventing it" from all public surfaces (internal control, not reader copy).

**LEAD-M07 — Accessibility conformance flag is false-as-shipped. [MATERIAL→BLOCKER if anyone claims the a11y/hard-state suite passed]**
- Verified in `dist/`: `<svg>`=0, `<figure>`=0, `<table>`=1; yet `accessibility_requirements.tables_or_text_alternative_for_quantitative_visuals: true` on **141/141** and `visuals_must_expose_accessible_summary: true` on 141/141 (trivially unfalsifiable with no visuals). `hard_state_acceptance` states requiring tables/controls/maps cannot have been executed.
- Disposition: **BOUNDARY_TIGHTENING (honest-state now) + Design contract (specify).** De-assert the flag to an honest pending state now (this is a legitimate patch: an over-claim → honest state). Specify the text-alternative **`<table>` contract** for every record carrying ≥3 quantities (caption, scoped headers, unit/universe/period column) — this is the text alternative, required **independently of Design**. Re-label the 13 orphan `/evidence/VIS-*/` `closure_state` (NO_SOURCE_EXPECTED is false for Findex/MFI/CBY-derived visuals → unresolved lineage per LEAD-B07). Bind `prohibited_inferences` + `governed_visual_contracts` to the 37 `/evidence/VIS-*/` routes (the contract does not currently reach its own evidence surface).

**LEAD-M08 — FMIIP active-account baselines held but unpublished; publish as dated baseline, never as current status. [MATERIAL]**
- Verified: `reforms_regulation.json` holds `FMIIP-RF-013` active bank accounts = **1,062,441**, RF-015 active e-wallet = **375,252**, RF-014 female-owned active bank = **200,898**, RF-004 access points = **817** (2030 target **1,021**); none appears in `dist/`. The only public FMIIP number is the 2030 target 1,021 (on `/evidence/XW-FMIIP-005/`, `public_routes: []`).
- Disposition: **BOUNDARY_TIGHTENING (SUPPORTING DISCLOSURE, not MAIN NARRATIVE).** Promote RF-004/012/013/014/015/017/018 as **dated FMIIP-universe baseline observations** with their own firewall (project-defined universe; accounts ≠ people; active-account definition not reconciled with CBY totals). **Never publish 1,021 without 817.** Apply the red team's sub-rule to the Jan-2025 zeros: classify each as `MEASURED_ZERO_STATE` (publishable: RF-006/007/008/010/011/019/020) vs `CHANGE_METRIC_ORIGIN` (zero by construction: RF-001/005) vs `NOT_YET_INSTRUMENTED` (RF-021/022/023/024 satisfaction/grievance — publishing these as "0" reads as "0% satisfied", defamatory-grade) — **publish only the first class**. **Do NOT** write "baseline zero → reform has not translated into use" (binding correction #3). Respect the §22 structure.

**LEAD-M09 — IA "Method & Measurement" is unbuildable as specified; live header/footer "Data" contradiction. [MATERIAL]**
- Verified: `navigation_interaction.json` `global_navigation` = 6 entries, schema `{route,label_en,label_ar}`, **no `children`**; live labels still Option-A ("Readings","Data","Methodology","About") — AR `/readings/` already «قراءات الأدلة» but EN still "Readings" (asymmetric). `aria-haspopup` = **0** across `dist/`; header is a flat 6-anchor nav. `/measurement/` has `entry_modes:[deep_link,footer,search]` (no global_navigation), `navigation_prominence: CONTEXTUAL_FOOTER`. Footer already renders "Data & sources"; header renders "Data" — live contradiction. Footer group `method_measure` contains `/about/`.
- Disposition: **IA_LABEL_CHANGE + schema change; define the interaction contract (brief §5) — do not leave a dead heading.** Adopt the mechanism that survives the product's own `mobile_rule: "no hover-only meaning"` and "zero route changes": **"Method & Measurement" resolves to `/methodology/` with `/measurement/` as a visible inline sibling link** in header and drawer (no popup, no hover, no new route). Concretely: (i) extend `global_navigation` schema with `children[]` and require every primary node resolve to a route; (ii) add `global_navigation` to `/measurement/` `entry_modes` and change its `navigation_prominence` **in the same commit** as the `/about/` demotion (so demotion cannot ship without promotion — else About is lost and Measurement gains nothing); (iii) migrate EN labels to "Evidence Readings" and "Data & sources" (AR already «قراءات الأدلة» / footer «البيانات والمصادر»); (iv) fix the header/footer "Data" contradiction and move `/about/` out of footer `method_measure` **regardless** of the IA change (defect today); (v) give `/measurement/` a breadcrumb parent (currently only Evidence Record + Reading have parents); (vi) define the Trust affordance concretely (not a 6th hidden-drawer duplicate) and re-run the 320–400px suite before claiming mobile/RTL. Full interaction contract belongs in `CLAUDE_TRANCHE_B_CLOSURE.md`.

**LEAD-M10 — Publish a reconciliation of the three incompatible magnitudes + an adult denominator. [MATERIAL]**
- Verified: 11.9% account ownership (Findex 2022, `/people/`), 3.3m microfinance savers (2023, `/finance/`), and 1,062,441+375,252 ≈ 1.44m FMIIP active accounts (Jan-2025) are published (or withheld) with no reconciliation; "population ages 15+" occurs once as a unit label — no adult denominator anywhere.
- Disposition: **BOUNDARY_TIGHTENING.** Add one explicit reconciliation block (on `/people/` or `/evidence/compare/`) naming 11.9% / 3.3m / 1.44m side by side and stating **precisely why they cannot be added, subtracted or ranked** (different universes, units, clocks, evidence classes — respect the firewall; do not imply equivalence). Publish an adult-population denominator with its source. This is exactly the Compare-first-compatibility discipline (brief §39).

**LEAD-M11 — Quarantine the contradictory "not verified" Findex block from the active product-input dir. [MATERIAL, latent]**
- Verified: `findex_baseline.json` contains a block "Attached analytical inputs — not verified public Findex aggregates" with unsourced narrative ("Telecom top-ups…", ">71%…") and a parallel Yemen Findex set that contradicts the published headline figures. Verified **not** in `dist/` today, but it sits in `site-src/content/data/` feeding the `/data/` route.
- Disposition: **EXCLUDE / quarantine.** Move the block out of `site-src/content/` (or delete it), with lineage recorded. Highest-variance latent risk: one careless export makes the product's own headline figures contestable using the product's own file. This is integrity-safe to do now (it is not a public projection and not the Master), but record it as a patch/decision and confirm the build stays green.

**LEAD-M12 — `/firms/` ordinal ranking overclaims; the Tranche A audit hardened it. [MATERIAL]**
- Verified concern: `/firms/` publishes an 8-item constraint ranking (electricity 50% … access to finance 22% … informal competition 17%) with no n on that question, adjacent 1–5pp gaps not separable at n≈545, shares summing to 242% (multi-response) without saying respondents could cite more than one; `DOMAIN_CORPUS_EDITORIAL_CLOSURE.md` then hardened this into "access to finance ranks 6th (22%)".
- Disposition: **BOUNDARY_TIGHTENING.** State the multi-response base and n; present constraints as grouped bands, not a strict ordinal rank; drop "ranks 6th". Keep the genuinely strong firm evidence (69.12% internal funds / 0.56% banks; 73.48% money changers / 24.39% commercial banks as **multiple-response intermediary-used**, not market share; the "91.84% is not the share of all firms" guard). Correct my own audit's over-claim in the closure.

**LEAD-M13 — Rights layer does not project; `/data/` promises per-record rights no field can hold. [MATERIAL]**
- Verified (red team): `source_reference_map.json` `rights_display_state = OBJECT_LEVEL_OR_UNSPECIFIED` for **159/159**; `publisher` null for **133/159** (incl. both IMF Article IV records and `SRC-CBY-001`); `/data/` makes ≥4 per-record rights promises ("Rights travel with the data", "reuse conditions with it", "under its state and rights", + open-the-record-to-check-rights) — all confirmed present in `dist/en/data/`. Master `28_METHODS_RIGHTS` holds a real rights layer (WB Open Data CC BY 4.0, Microdata terms, Findex confidentiality) that projects into no public object.
- Disposition: **RESOURCE_METADATA_UPDATE + schema.** Add `rights_state`/`licence`/`attribution_requirement`/`retrieval_date` to the source register and evidence objects; project `28_METHODS_RIGHTS`; replace the single `OBJECT_LEVEL_OR_UNSPECIFIED` with an assessed per-source state; populate `publisher` for all 159 **before** surfacing any LOCATOR_ONLY records in the library (else the defect multiplies). Until fields exist, either deliver the promise or remove the four `/data/` rights promises. Add the §20 statement: "A source's inclusion in the Library does not mean CauseWay endorses its analysis/conclusions."

### Analytical dispositions (Readings / Measurement / Visuals — from specialist waves, Lead-accepted)

- **Readings (10):** KEEP CWR-001..010 with these edits — CWR-006 folded into LEAD-B01; **CWR-010** add the missing G2Px direct-source paragraph (45,460 recipients / eight districts) [MATERIAL projection defect, `READING_THESIS_REFINEMENT`]; **CWR-001** strip leaked internal jargon (E&O, CCY 7.4bn, 1.838, 33%) [EDITORIAL]; sweep "the system"/«المنظومة» as unnecessary grammatical subject across all ten [EDITORIAL, ties to Arabic ledger]. No MERGE/RETIRE/NEW.
- **Measurement (10):** 8 KEEP; **MA-003** REWRITE (LEAD-M03); **MA-001** REWRITE — extend `affected_route_list` from `['/people/','/','/explore/']` to add `/remittances/`, and extend `current_evidence`/`missing_evidence` to include current remittance receipt/channel/frequency as part of the people-side baseline (brief §21); **no MA-011**. P0/P1 is evidence sequencing, not policy/donor ranking.
- **Visuals (36):** 24 KEEP / 12 REFINE / 0 MERGE / 0 RETIRE (R1–R17 execution specs already drafted in the specialist wave — re-capture them into `VISUAL_CONTRACT_CLOSURE.md`). Plus the addendum's **signature visual candidates** (§8 below) to be evaluated against these 36, preferring refine/merge over proliferation.

### Search / Trust dispositions (Lead-accepted)
- **Search:** apply R1–R13. Add `SRC-MOPIC-YSEU-2023-080` to the index (159 vs 158). Surface the 132 LOCATOR_ONLY records. Route `does_not_establish` into search. Add stemming. Fix the 2 failing smoke tests. **Reject** the broad issuer-only alias; **caveat** the education↔literacy alias (search may aid discovery, may not create factual equivalence — brief §37).
- **Trust:** F-01 bring AR compare dimensions to EN parity; F-02 state "incompatible" as a valid Compare result; F-03 replace the 108-identical evidence-record boilerplate (ties to LEAD-M06); F-04 split `limitations` into prohibited-inference vs measurement-limitation; F-05 add the 59 count on `/data/`; F-06 add units to vintage figures; F-07 de-duplicate the `/data/` chronology.

### REJECTED / RE-SEVERED (Lead adjudications — do not regress)
- **Reject** narrowing `/finance/` to microfinance (binding #2).
- **Reject** "baseline zero → reform has not translated into use" (binding #3).
- **Reject** "Yemen's largest physical cash-access channel" (binding #4).
- **Reject** "absence of a functioning formal credit/deposit channel" (binding #5).
- **Reject** automatic MA-011 (binding #7); MA-001 extension instead.
- **Reject** mechanical population of all 8 domain readings (binding #8); per-pair test.
- **Re-sever** the red team's "MA-003 lists income among not established" as over-stated — MA-003's causal framing is correct; only the missing income-*level* gap is the defect (LEAD-M03).
- **Re-sever** my own Tranche A "ranks 6th (22%)" as over-claim (LEAD-M12).
- **Foreground** female/male levels over the 3.37× ratio (binding #6); drop ratio with the statistical reason (LEAD-M04).

---

## 8. REMAINING SCOPE — THE ACTUAL WORK LIST (WHAT THE NEXT WINDOW MUST PRODUCE)

Nothing below is written yet. Produce all of it, then validate → ZIP → Arabic hand-back → STOP (no Tranche C).

### 8A. Required Tranche B artifacts (brief §54) — 12 files
1. `audit/CLAUDE_TRANCHE_B_CLOSURE.md` — master closure. Must include: the Method & Measurement **interaction contract** (LEAD-M09, brief §5, full desktop/mobile/keyboard/RTL/focus/first-child/equal-prominence/direct-click spec); the honest reconciliation that Tranche A §5 "no BLOCKER" is overturned; per-surface review sign-offs; validation split; exact status.
2. `audit/MASTER_FIRST_PATCH_SPEC.csv` — **core deliverable.** 22 columns exactly: `patch_id, session, sheet, stable_object_id, row_locator_if_needed, field, current_value, proposed_value, language, change_type, semantic_change_yes_no, source_basis, reason, evidence_boundary_preserved, downstream_projections, search_impact, IA_impact, visual_impact, rights_impact, priority, validation_required, Claude_status`. One row per discrete Master-first change. Every semantic row needs before/after (brief §46) — the load-bearing before/afters are already captured verbatim in §7 and §9 of this file. Change types from brief §45; statuses from §57.
3. `audit/MASTER_FIRST_PATCH_NARRATIVE.md` — grouped-edit explanations not safe from CSV alone (esp. LEAD-B01 finance package, LEAD-B07 source-closure schema, LEAD-M09 IA, LEAD-B05 Arabic terminology sweep).
4. `audit/BILINGUAL_EDITORIAL_CLOSURE.md` — semantic-invariance checks across number/unit/universe/denominator/geography/period/currentness/method/evidence-state/authority/certainty/limitation/rights/measurement-next (brief §30). Feature CLM-008 (LEAD-M01) as the exemplar parity break.
5. `audit/ARABIC_TERMINOLOGY_AND_STYLE_LEDGER.md` — canonical term matrix (brief §43 list); the «ادعاء» decision (LEAD-B05); «المنظومة» self-referent cleanup; calque list; Tier-1 native KEEP list. Label `VERIFIED_BY_CLAUDE_TEAM`, `EXTERNAL_HUMAN_CERTIFICATION_NOT_PERFORMED`.
6. `audit/ENGLISH_EDITORIAL_CLOSURE.md` — "in the system" backend voice; RV-CWR accessible-summary rewrites (drawing-instructions → reader prose); filler/causal-overstatement sweep (brief §29).
7. `audit/READINGS_MEASUREMENT_CLOSURE.md` — all 10 Readings + all 10 Measurement, each reconstructed per brief §31/§33; dispositions per §7 above.
8. `audit/VISUAL_CONTRACT_CLOSURE.md` — all 36 reviewed per brief §34 (question/inputs/unit/universe/period/why-visual/family/boundary/caption/alt-text/table-fallback/detached-use/RTL/mobile) + KEEP/REFINE/MERGE/RETIRE; R1–R17; plus addendum signature-visual verdicts.
9. `audit/SEARCH_DISCOVERY_CLOSURE.md` — bilingual behavior for the brief §37 term list; R1–R13; alias decisions.
10. `audit/EVIDENCE_COMPARE_TRUST_CLOSURE.md` — Evidence-record readability (brief §38); Compare-first-compatibility (brief §39); Methodology (brief §40); About (brief §41); Trust surfaces (brief §42); F-01..F-09.
11. `audit/TRANCHE_B_RED_TEAM.md` — consolidate all 11 personas + the Lead byte-verifications + adjudications (§7). No consensus theatre.
12. `audit/TRANCHE_B_UNRESOLVED_QUEUE.md` — **short.** Only genuinely unresolved material items, each with object/field/issue/why-material/dependency/next-action/can-OpenAI-resolve/external-verification-needed/blocks-Tranche-C. Candidates: CBY Decision 18/2026 entity names (`PRIMARY_SOURCE_PENDING`); the generator pipeline itself; any addendum benchmark that could not be retrieved with source closure.

Also **update** `OPENAI_REENTRY_CHECKPOINT.md` (do not overwrite Tranche A lineage).

### 8B. Additional addendum artifacts (addendum §24) — 7 files
13. `audit/ECONOMIC_SYSTEM_AND_EVIDENCE_REVIEW.md` — economic-function lens (addendum §3), classify each people/firm function CURRENTLY MEASURED / HISTORICAL / PARTIAL / PROGRAMME-SPECIFIC / CONTEXT ONLY / NO CURRENT YEMEN EVIDENCE; signature system map decision (§4); evidence-clock decision (§5); financial-health/quality/cost/identity/G2P dispositions (§11–14); apply the deletion test throughout.
14. `audit/INDICATOR_COVERAGE_MATRIX.csv` — the whole-product coverage matrix (addendum §6): rows = the ~30 dimensions listed (ownership/access, active use, savings, credit, payments, remittances, provider presence, geography, affordability, reliability, consumer protection, literacy, digital capability, financial health, gender, income, education, age, rural/urban, displacement, disability, identity/KYC, digital safety, firms/MSME, insurance, pensions, regulatory implementation, payment infrastructure); each classified CURRENT OBSERVATION / DATED-HISTORICAL / ADMINISTRATIVE ONLY / PROGRAMME ONLY / PARTIAL / MEASUREMENT GAP / NO CURRENT EVIDENCE. **Do not fill gaps with global data.**
15. `audit/METHODOLOGY_COMPLETENESS_CLOSURE.md` — `/methodology/` completeness against the addendum §7 checklist + §19 conflict-affected measurement + source-admission policy (§8). Progressive disclosure; not a description of internal controls.
16. `audit/BENCHMARK_AND_COMPARATOR_POLICY.md` — targeted benchmark lessons (addendum §2: WB/G20, Findex 2025, PAFI, G2Px, ID4D, CGAP 2026, FinNeeds/AFI, FinAccess Kenya, UNCDF IDES, UNHCR, Data360) as **method/context only**; the three comparator types (STATISTICAL / STRUCTURAL / MEASUREMENT EXEMPLAR, §15); every comparator tagged "BENCHMARK / METHOD REFERENCE — NOT YEMEN EVIDENCE". No league table.
17. `audit/SOURCE_NARRATIVE_EXTRACTION.md` — for high-value admitted Yemen sources, extract four layers (SOURCE OBSERVATION / SOURCE INTERPRETATION / CAUSEWAY SYNTHESIS / NOT ESTABLISHED), attributed, paraphrased not reproduced (addendum §9, §47).
18. `audit/ECONOMIC_CONTEXT_USAGE_POLICY.md` — macro/conflict context only where it changes FI interpretation; every insertion must answer "Why does this change interpretation of this FI evidence?" (addendum §10, §48). CONFLICT CONTEXT ≠ CAUSAL PROOF.
19. `audit/SIGNATURE_VISUAL_CANDIDATES.md` — evaluate (do not auto-add) the 6 candidates (addendum §22: system+evidence map; evidence clock; coverage matrix; rule/rail→operation→access→use→quality→outcome ladder; transfer→persistent-use pathway; financial-needs/function lens) against unique value / evidence availability / overclaim risk / overlap with existing 36 / mobile-RTL / maintenance / deletion test. Include the design-aware visual-semantics contract (addendum §21) for MEASURED/DERIVED/HISTORICAL/ADMINISTRATIVE/PROGRAMME/ESTIMATED/PROJECTED/PARTIAL/UNKNOWN + evidence-clock/universe/currentness/transmission-stage/source-role/measurement-gap.

**All accepted semantic/public-copy changes from the addendum work must also land in the patch spec + narrative** (addendum §24). Also address addendum §16 (OECD/INFE item-level integrity — mark reconstructed items NON-PUBLIC, strip "Verbatim" unless transcribed; the red team flagged `28_METHODS_RIGHTS` rows 43–68 / `29_OECD_BENCHMARKS`) and §17 (`17_INDICATOR_LIBRARY` role — either specify Master-first additions of verified public Yemen measures, or rewrite its "single master table" purpose accurately). Honor the §23 "what not to create" list (no composite score, ranking, scorecard, league table, forecast model, unverified operating-provider map, conflict heat map, auto AI insights).

### 8C. Currentness (brief §9–10, carried from Tranche A)
- CBY **Decision 17/2026** — present; verify, do not duplicate.
- CBY **Decision 18/2026 (24 Sep 2026)** — primary event VERIFIED at `cby-ye.com/news/975` (number/date/action/authority/scope); **exact entity names `PRIMARY_SOURCE_PENDING`** (in the signed PDF; do not promote secondary names — Yemen Monitor 180277 actually concerns Decision 15). Treat via Source Library + Provider Status Events + regulatory-instrument discovery; **do not** auto-add every enforcement decision to the macro chronology. Enforcement decisions 7/8/12/16 have no recorded status — flag in the unresolved queue.
- Five 2026 candidate sources — Tranche A role classifications are provisional; do **not** create final public metadata until the named source/version is retrieved and verified (publisher/title/date/version/URL/retrieval-date/role/establishes/does-not-establish).

### 8D. Resource Library (brief §8, §36; Tranche A A3 accepted)
Keep ONE governed register + MULTIPLE discovery views/facets (no CBY/Law/Report/Education corners). Keep DOCUMENT TYPE distinct from EVIDENCE ROLE (do not collapse). Surface LOCATOR_ONLY regulatory instruments as filterable (issuer/doc-type/date/status) **after** publisher+rights exist (LEAD-M13). Facet spec is in `audit/RESOURCE_LIBRARY_CLOSURE.md` (Tranche A).

---

## 9. VERIFIED GROUND-TRUTH (SPOT-CHECK, DON'T RE-DISCOVER)

Commands + results confirmed this session (Master `e69804…`, Page Specs `ff2b0f…`):
- **Finance:** `dist/en/finance/index.html` contains "3.3 million active savers" and "about YER 44 billion in nominal portfolio in 2023, compared with verified 2020 anchors of … 33.379 billion" (live). `cby_monetary.json`: `YER_USD_MARKET_RATE` present (792.69 present; 1,529.40 present); `BANK_CREDIT_PRIVATE_SECTOR` present with `1679`; `1,679`/`1679` in `dist/` = **0**. Leaked instruction "Use the documented system chronology…" live in `dist/en/finance/`.
- **Remittances:** `dist/en/remittances/` "observed history" ×4; `remittances.json` `HISTORICAL_REPORTED` ×7, `SOURCE_REPORTED__IMF` ×7. VIS-REMITTANCE-MACRO current title/summary/method captured verbatim in §7 LEAD-B06.
- **Providers:** EN "official CBY 2026 roster" (unqualified); AR «القائمة الرسمية للبنك المركزي» (no عدن); «عدن» on AR providers page = 2.
- **CLM-008:** EN vs AR does_not_prove captured verbatim in §7 LEAD-M01 (AR carries «خارج نطاق سلطة المصدر», EN does not).
- **Source closure:** 108 evidence objects; `source_dependencies` empty 108/108; `source_links` empty 80/108; closure_state `NO_SOURCE_EXPECTED`=75, `CLOSED_TO_SOURCE_ID`=40, `CLOSED_VIA_CONTROLLED_DEPENDENCIES`=108.
- **Precision:** findex_baseline "6.5" ×1, "15.5" ×1; "9.00" in dist = 0; `confidence interval/standard error/95%/±` across specs+passports+claims+codebook = 0. `5.44` ×1, `18.35` ×1 in findex_baseline; `12.91` in findex_baseline = 0 (product-derived).
- **findex parallel block:** "Attached analytical inputs" ×1, "not verified public Findex" ×1, "Telecom top-ups" ×1, ">71%"/"71%" ×1 in findex_baseline.json; not in `dist/`.
- **Accessibility:** `dist/` `<svg>`=0, `<table>`=1, `<figure>`=0; flag true 141/141.
- **FMIIP:** `reforms_regulation.json` has 1062441 ×1, 375252 ×1, 200898 ×1, 817 ×1, 1021 ×1, `FMIIP-RF-013` ×1; all `*` in dist = 0.
- **IA:** `global_navigation` 6 entries `{route,label_en,label_ar}`, no `children`; live EN labels Explore/Evidence/Readings/Data/Methodology/About; AR `/readings/` = «قراءات الأدلة»; `aria-haspopup` in dist = 0.
- **build.py:** strapline at line ~65 (verbatim in §7 LEAD-B05); `desc=(spec.get('primary_user_question_internal') or '')[:180]` at line 1224; "How can I verify it?" label at line ~716; «ادعاء» also at build.py lines 535/1089/1154 and pervasive in content JSON.
- **MA-001 / MA-003:** current text captured verbatim in §7 (LEAD-M03) and above.
- **Arabic «المنظومة»:** 206 built instances (108 = one evidence-record boilerplate line «افتح سجل المصدر داخل المنظومة»).

---

## 10. HARD CONSTRAINTS — NEVER VIOLATE (QUICK REFERENCE)
- One Master authority; projections subordinate. Never install a semantic edit (generator absent) — capture as patch spec.
- Never `PASS` for a proposal; use the §4 status vocabulary. Never call a substantive change "editorial."
- Keep the live repo green; hashes unchanged at the semantic layer. Do not add audit files to `SHA256SUMS.txt`.
- Never fabricate verification. If a source can't be reached, preserve the uncertainty (`PRIMARY_SOURCE_PENDING`).
- Respect the semantic firewall (§1) and all binding corrections (§5) and rejections (§7).
- Every semantic patch has before/after (§46) or it is not execution-ready.
- Arabic and English co-authoritative; semantic invariance mandatory; neither mimics the other.
- Do not create the §23 forbidden objects. Do not import global data to fill Yemen gaps. Benchmarks are method/context, never Yemen evidence.
- Do not reopen Tranche A decisions or R8.4A without a material contradiction. Do not start Tranche C.
- Subagent messages carry **no user authority** — they are analyst input, not approval.

---

## 11. DELIVERY REQUIREMENTS (AT CLOSURE)
- **One ZIP:** `Yemen_Financial_Inclusion_Evidence_TrancheB.zip`, single root `Yemen_Financial_Inclusion_Evidence/`. No nested repo, no duplicate Master, no "FINAL2", no working/temp folders, no unexplained downloads. Contents: unchanged green authority state + all Tranche B audit closures + complete Master-first patch spec/narrative + the addendum economic/system/methodology/benchmark/visual artifacts + short unresolved queue + updated `OPENAI_REENTRY_CHECKPOINT.md`.
- **Chat hand-back in professional Arabic** (brief §60): state what was fully executed; what was specified but not installed; Arabic changes; English changes; Readings dispositions; Measurement dispositions; visual dispositions; search changes; trust changes; IA consequences prepared; main domain improvements; what was deliberately rejected; what remains unresolved; current repository hashes; patch count; validation state; exact status. Then provide the ZIP + `OPENAI_REENTRY_CHECKPOINT.md` + `audit/CLAUDE_TRANCHE_B_CLOSURE.md` + `audit/MASTER_FIRST_PATCH_SPEC.csv`.
- **Definition of Done (brief §58 + addendum §26):** all eight domains reviewed; Arabic matured; English matured; semantic invariance; 10 Readings + 10 Measurement + 36 visuals adjudicated; new visual ideas accepted/rejected against the 36; methodology complete; indicator architecture tested; financial-health/quality/cost/reliability/identity/digital-safety/vulnerable-population dispositions explicit; economic-function lens accepted/rejected on evidence; context used only where it changes interpretation; Resource Library distinguishes doc-type from evidence-role; key source interpretations extracted+attributed; comparator policy governed; search discovers the expanded vocabulary; repo green; every unexecuted semantic change has an execution-grade patch; a future designer need not invent substantive meaning. Standard: **MORE EXPLANATORY WITHOUT BECOMING MORE SPECULATIVE.** Then STOP.
- **Final quality question (brief §61):** if OpenAI applies these patches Master-first, regenerates, and hands the result to an exceptional designer — will they get the strongest defensible bilingual public evidence product the current Yemen evidence supports, or still need to invent analysis / repair language / infer hierarchy / decide what evidence matters? If the latter, Tranche B is not done.

---

## 12. EXACT NEXT ACTIONS (START HERE)
1. Run the §0 resume protocol (verify hashes, green, read the three inputs + this file).
2. Build `audit/MASTER_FIRST_PATCH_SPEC.csv` from §7 (before/after already captured for the load-bearing patches). This is the spine; the closures reference it.
3. Write the 12 §54 artifacts + 7 §24 addendum artifacts (§8A/§8B). Reuse the specialist-wave detail summarized in §6 and the R1–R17 / R1–R13 specs.
4. Do the addendum analytical work (economic-function lens, coverage matrix, benchmark policy, source-narrative extraction, signature-visual verdicts, methodology completeness) — deletion test throughout; no new facts; no global data in gaps.
5. Re-run build + validate (must stay green); confirm manifest 58/58; confirm hashes unchanged.
6. Produce the ZIP; deliver the Arabic §60 hand-back + the four required files.
7. STOP. Do not begin Tranche C.

*End of continuation handover. The repository is green, the authority is unchanged, the analysis is complete, and the adjudications are verified. The remaining work is disciplined writing + the patch package + the addendum integration, then close.*
