# Session Closure Quality Standard

**Status:** Current operational standard for R8 and all subsequent controlled maturation/release sessions.

This standard governs **how a session is judged**, not what the evidence says. The Production Master remains the sole semantic, evidence, source, rights, controlled-product-state and publication-state authority. Where this standard conflicts with the Master, the Master governs content and the conflict is escalated.

## 1. Governing principle

A session is not complete because the planned checklist is exhausted, files changed, a validator is green, or the prose looks polished. A session is complete only when the consequential questions in scope are understood well enough that **additional investigation is unlikely to materially change the important conclusions or the next decision**.

Effort is allocated asymmetrically: settled, low-consequence facts receive proportionate verification; consequential uncertainty, contradictions, causal claims, source disagreements, high-reuse public numbers and publication/rights risks receive deeper investigation.

## 2. Mandatory session questions

At ORIENT and again before closure, answer explicitly for the material issues in scope:

1. What do we currently believe?
2. Why do we believe it?
3. What original evidence supports it?
4. What evidence, observation or changed condition could make it wrong?
5. What remains unknown, contradictory, assumed or dependent on another fact?
6. What has changed recently enough to affect interpretation or currentness?
7. What adjacent system, institution, incentive, measurement process or conflict condition could explain what we observe?
8. Which source, literature item, dataset, original document or investigation now has the highest information value?
9. What would the relevant specialist disciplines say, and where do they genuinely disagree?
10. What is the strongest technically sound narrative that survives those tests without exceeding the evidence?

The answers may change the session plan. New findings are allowed to overturn earlier conclusions.

## 3. Living reasoning model

Maintain, at the level appropriate to the session, a living model of:

- **knowns** — directly supported facts and controlled states;
- **unknowns** — material unanswered questions, never silently converted to zero or failure;
- **contradictions** — source-internal and cross-source disagreements that affect interpretation;
- **assumptions** — explicit, testable and never presented as observations;
- **dependencies** — source, method, rights, technical and institutional dependencies;
- **causal hypotheses** — clearly separated from measured associations or sequence;
- **evidence strength and independence** — including common underlying datasets/projects so repeated publication is not mistaken for independent corroboration;
- **changing conditions / evidence clocks** — what date the evidence describes versus publication/retrieval/review dates; and
- **decision consequence** — what would actually change for a user if the uncertainty were resolved.

## 4. Source and research gate

For every material public claim or conclusion in scope:

- prefer the **original/primary authoritative evidence** for the factual statement when available;
- use secondary synthesis for context, interpretation or discovery, not as a substitute for a better primary source;
- trace the exact version, date, universe/denominator, geography, method, unit, calculation base and publication/rights state;
- triangulate when one source cannot resolve a consequential issue;
- deliberately seek disconfirming evidence for consequential interpretations;
- distinguish five reports based on one underlying evidence lineage from five independent observations;
- for material negative claims such as “not located” or “no newer measurement found”, preserve enough of the search universe/date/routes to make the absence claim auditable where practical;
- do not use a literature item merely because it is prestigious, recent or interesting; apply the user-value and deletion tests; and
- if original evidence does not support the statement, narrow, relabel, hold or remove the statement.

### Literature admission test

A literature/report/tool/best-practice item is promoted only when it has a defined job such as:

- Yemen factual evidence;
- Yemen system/context evidence;
- measurement/method reference;
- implementation or monitoring reference;
- international diagnostic lens that improves a Yemen question without becoming a Yemen fact; or
- public user resource with clear “for whom / for what” value.

Otherwise it remains research lineage or is rejected.

## 5. Financial-inclusion and system-reasoning gate

Every session must preserve the semantic firewall:

**people ≠ households ≠ firms ≠ accounts ≠ active accounts ≠ customers ≠ transactions ≠ terminals ≠ agents ≠ providers ≠ beneficiaries**

**access ≠ ownership ≠ registration ≠ adoption ≠ active use ≠ depth/frequency/persistence ≠ quality ≠ outcome**

**infrastructure ≠ use · target ≠ result · programme reach/KPI ≠ national prevalence · regulation ≠ implementation ≠ experienced outcome · licence/listing ≠ operation · missing ≠ zero**

Context must explain rather than excuse. Conflict, institutional fragmentation, infrastructure, market incentives, humanitarian delivery, regulation and macro conditions may be relevant adjacent systems, but chronology or co-occurrence is not causality. Avoid blame or institutional motive attribution unless a reliable source directly establishes the point and the attribution is necessary.

## 6. Bilingual editorial gate — original in both languages

Arabic and English are co-authoritative original public editions over the same controlled facts. Neither is treated as a literal translation of the other.

For every changed public passage:

- independently edit the Arabic as natural professional Arabic and the English as natural professional English;
- preserve number, unit, denominator/universe, geography, period/currentness, method, authority, certainty, limitation, rights and measurement-next meaning;
- remove generic AI cadence, repetitive scaffolding, unnatural parallel syntax, empty intensifiers, backend vocabulary and explanatory padding;
- allow necessary proper names, source acronyms and stable IDs in Arabic, with bidi-safe rendering and explanation on first use where needed;
- prefer precise plain language over consultant jargon;
- preserve specialist terminology where precision requires it; and
- read changed passages in isolation and in page context so that neither edition sounds translated or machine-composed.

“No AI traces” is an editorial outcome, not a cosmetic rewrite: the prose must be specific to the evidence, proportionate to uncertainty, internally coherent and free of formulaic filler.

## 7. Public-product gate

For each affected route, Reading, visual or utility ask:

- What user job does this solve?
- What is the strongest defensible answer?
- What material limitation must be visible before reuse or inference?
- What is the appropriate depth for a citizen, journalist, regulator, provider, researcher or development practitioner without giving them different facts?
- Does the evidence passport/reference layer support verification without becoming the subject of the page?
- Would removing this section, visual or object lose material user value, evidence integrity, safety, rights or implementation determinism? If not, remove or merge it.
- Does detached reuse of the headline/chart/number preserve the period, universe and critical caveat?
- Is an unknown rendered as an evidence state rather than a software error, zero or implied failure?

Do not create a universal score/dashboard or causal visual simply because heterogeneous numbers exist.

## 8. Rights, ethics and conflict-sensitivity gate

- Public availability is not redistribution permission.
- Citation, factual use and redistribution are separate permissions.
- Do not infer licence, endorsement, authority, neutrality, independence, motive or institutional position.
- Preserve source-specific institutional/geographic scope using neutral, source-faithful nomenclature.
- Apply privacy, statistical disclosure, safety and sensitive-geography constraints before increasing granularity.
- CauseWay synthesis/derivation must remain distinguishable from the original publisher’s evidence.

## 9. Engineering and reproducibility gate

Every material Master change follows:

**Master first → deterministic regeneration → semantic parity check → public build → validators → rendered hard-state inspection → hash/checksum refresh.**

Before session PASS:

- current Master and projection hashes are re-read from the live repository;
- no shadow truth is introduced in JSX/JSON/CSS/copy;
- source/publication/rights filters remain intact;
- every new deterministic gate introduced by the session is reproducible;
- technical failure/loading/empty search cannot masquerade as evidence absence;
- Arabic/RTL/mobile/accessibility behavior affected by the change is checked; and
- obsolete or duplicate artifacts created unnecessary by the change are identified for removal or immediate removal when safe.

## 10. Adversarial five-reviewer test

Before closing a consequential session, ask independently what each of these reviewers would discover that the work failed to understand:

1. the most knowledgeable Yemeni practitioner in the affected domain;
2. a leading international financial-sector/financial-inclusion specialist;
3. a regulator/supervisor familiar with the underlying administrative reality;
4. a data scientist/statistician/methodologist; and
5. a hostile but technically fair peer reviewer.

A material weakness identified by this test is a defect to investigate, not a rhetorical exercise.

## 11. Session role discipline

One role remains the **decision owner**. Up to two formal challenger lenses remain responsible for adversarial challenge. Additional specialist consultations may be activated when a material question requires them, but they do not create parallel decision authority or parallel evidence truth.

The role mix is chosen by the actual uncertainty: survey statistics, payments/remittances, banking/microfinance/MSME, consumer protection, FCV/humanitarian systems, qualitative research, data engineering, visualization, Arabic/English editorial, accessibility, rights/legal, security/privacy or frontend implementation.

## 12. Mandatory closure record

Every session closure records, in this order:

1. exact scope actually inspected;
2. what was believed at entry and what changed;
3. highest-information-value investigations performed;
4. disconfirming/alternative evidence tested where material;
5. decisions and rejected alternatives;
6. exact Master changes, if any;
7. Master hash before → after;
8. exact files changed/created/retired;
9. what became more true;
10. what became more useful/simpler;
11. what became more complex;
12. what can now be removed/merged;
13. native Arabic/English editorial result for changed public copy;
14. build and machine-validation results;
15. adversarial five-reviewer result;
16. only material residual risks/unknowns;
17. **PASS / REVISE / ESCALATE_TO_MASTER / HOLD / STOP**; and
18. one exact next bounded session and why it has the highest remaining information/product value.

## 13. Stop rule

Do not confuse completion with understanding. Continue investigation inside the bounded session while a plausible next source/test has a reasonable chance of materially changing the important conclusion. Stop when additional investigation is unlikely to do so.

Do not continue merely to accumulate sources, pages, metrics, diagrams, prose or review artifacts. The target is the **smallest, strongest, most defensible and most useful system** that the evidence can honestly support.


## 14. Mandatory pre-close checklist

A session may be marked PASS only when every applicable item below is explicitly satisfied or recorded as a bounded residual dependency:

- [ ] **Authority:** live Master/path/hash re-read; no predecessor or draft used as production truth.
- [ ] **Current belief:** the session states what it believes, why, and what changed from entry.
- [ ] **Original evidence:** consequential claims checked against the highest-authority original evidence available.
- [ ] **Disconfirmation:** at least one plausible falsifier/alternative explanation was actively tested for each consequential interpretation.
- [ ] **Information value:** effort concentrated on uncertainties capable of changing the conclusion, user decision or publication state.
- [ ] **Living model:** knowns, unknowns, contradictions, assumptions, dependencies, causal hypotheses, evidence independence and changing conditions updated.
- [ ] **Financial-inclusion semantics:** people/accounts/access/use/infrastructure/providers/programmes/targets/outcomes remain distinct.
- [ ] **Context and causality:** chronology, conflict, regulation, projects and co-occurrence are not converted into unsupported causal claims or blame.
- [ ] **Literature/resources:** relevant original literature, reports, tools and prior drafts were checked where they have realistic information value; each promoted item has a defined user job and source/rights state.
- [ ] **Bilingual originality:** changed Arabic and English are independently edited, natural, professional and semantically invariant; no formulaic or machine-like prose remains.
- [ ] **Public usefulness:** answer, scope, limitation, next action and verification path are proportionate and do not let passports/references crowd out the subject matter.
- [ ] **Detached-use safety:** material headline/number/chart remains defensible when quoted, screenshotted or reused outside page context.
- [ ] **Rights/ethics/safety:** citation, factual use and redistribution remain distinct; sensitive geography/privacy/SDC and source authority are respected.
- [ ] **Engineering parity:** Master-first regeneration, semantic parity, public build, deterministic gates, hard-state inspection and hashes/checksums pass.
- [ ] **Five-reviewer test:** Yemeni practitioner, international specialist, regulator, data scientist/methodologist and hostile fair peer reviewer have no uninvestigated material objection in scope.
- [ ] **Subtraction:** anything made redundant by the session is removed, merged or queued for the bounded repository-subtraction session.
- [ ] **Stop rule:** further investigation is unlikely to materially change the important conclusion; closure is based on understanding, not checklist exhaustion.
