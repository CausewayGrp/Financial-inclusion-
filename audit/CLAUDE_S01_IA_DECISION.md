# CLAUDE S01 — INFORMATION-ARCHITECTURE DECISION (Tranche A · A1)
# قرار بنية المعلومات

**Session:** Tranche A / A1 — Independent IA decision
**Date:** 2026-09-25 (Africa/Cairo)
**Mode:** READ-ONLY analysis + Team-Lead decision. No routes, labels or copy were edited in Tranche A. Execution is sequenced (see §8): this record decides intent and maps consequences; a half-transition is explicitly avoided.
**Method:** Hub-and-spoke. Three independent challengers were convened in parallel (all read-only, grounded in the actual `navigation_interaction.json`, `questions.json`, `source_library.json`, `page_specs.json`): Specialist A (IA & user-journey), Specialists H+I (native Arabic + English label editors), Specialist K (hostile-but-fair red team, 10 stakeholder lenses). The Team Lead adjudicated.

---

## 1. DECISION

**Winner: OPTION B (adjudicated) — a label-and-prominence change on the existing six-family skeleton, with NO route changes, and with two evidence-driven refinements over the raw Option-B proposal.**

Final global navigation — **five primary items + a prominent secondary Trust layer**:

| # | Route | English (decided) | Arabic (decided) | Change vs current |
|---|---|---|---|---|
| 1 | `/explore/` | Explore | استكشف | keep |
| 2 | `/evidence/` | Evidence | الأدلة | keep |
| 3 | `/readings/` | **Evidence Readings** | قراءات الأدلة | **EN relabelled** (was "Readings"); AR unchanged |
| 4 | `/data/` | **Data & sources** | البيانات والمصادر | **EN+AR relabelled** (was "Data / البيانات"); adopts the label the footer already uses |
| 5 | (family) | **Method & Measurement** | المنهج والقياس | **new primary family** → two equal children: Methodology (`/methodology/`) + Measurement Agenda (`/measurement/`) |
| — | Trust layer | About · Corrections · Rights & reuse · Accessibility · Privacy · Terms · Contact | عن الموقع · التصحيحات · الحقوق وإعادة الاستخدام · إتاحة الوصول · الخصوصية · الشروط · التواصل | **About demoted** from primary to a *prominent* secondary Trust layer (persistent affordance, not buried) |

**Not chosen:** Option A (indefensible as-is — see §3); a standalone Option C (Specialist A demonstrated any minimal-correction "C" collapses into B, since B already keeps every route — so C would only add a competing mental model).

---

## 2. THE TWO REFINEMENTS OVER RAW OPTION B (Team-Lead adjudication, not rubber-stamp)

Raw Option B proposed "**Analysis**" and "**Sources & Data**." The independent evidence moved me off both exact strings:

**2a. Item 3 → "Evidence Readings" (EN), NOT "Analysis."**
- The demonstrated defect is narrow and specific: **bilingual parity is broken** — English "Readings" is genuinely ambiguous (meter readings / a reading list), while Arabic "قراءات الأدلة" already means "Evidence Readings" and is bounded and clear. Co-authority requires the two editions to carry equal meaning; today they do not. That is a real, confirmed defect (both language editors), not a hypothesis.
- "Analysis / التحليل" fixes ambiguity but introduces three new problems the red team documented and I find decisive: (i) it is the single most generic, overloaded word in this exact expert domain (every IMF Article IV / World Bank staff report is "analysis"), erasing the one signal that this is a **governed, evidence-anchored** object class (`BOUNDED_CROSS_SOURCE_SYNTHESIS`, each Reading bound to named Evidence Records); (ii) mild **overclaim** against a product whose north star is epistemic restraint ("we clarify evidence, we do not conclude for you"; every Reading carries a `prohibited_inference`); (iii) it would create a **new** nav-label ≠ page-identity mismatch. There is no measured user-harm evidence behind preferring "Analysis."
- **"Evidence Readings / قراءات الأدلة"** fixes the actual defect (English ambiguity + parity) with the *minimal* change, achieves **perfect bilingual parity**, and **preserves** the differentiating governed identity. The only cost raised was an "Evidence / Evidence Readings" adjacency in a short header — but that adjacency already exists and is accepted in Arabic ("الأدلة" then "قراءات الأدلة"), passed R4 and the S05.2 mobile/RTL suite, and the shared root correctly signals a parent→child relationship (verification directory → analytical syntheses over that evidence) rather than a collision. **Documented fallback:** if downstream usability testing shows the adjacency confuses first-time users, revert item 3 to "Analysis / التحليل" with "Evidence Readings / قراءات الأدلة" retained as the in-page family H1.

**2b. Item 4 → "Data & sources / البيانات والمصادر" (the existing footer label), NOT a new "Sources & Data / المصادر والبيانات" third variant.**
- The demonstrated defect: global "Data / البيانات" **undersells and contradicts** the route's own footer label, `page_family` ("Data & Source"), `unique_value_role` (`SOURCE_AND_DATA_DIRECTORY`) and contents (159 sources incl. CBY enforcement decisions `SRC-CBY-ENF-*`, bank lists, laws/regulation, 26 curated cards, indicator library, datasets). A user hunting a CBY decision would not click "Data."
- The repository **already carries** "Data & sources / البيانات والمصادر" in the footer. Adopting that as the single canonical label sitewide (a) fixes the undersell, (b) resolves the header-vs-footer contradiction by making the header match the footer, (c) introduces **zero new strings** and (d) honours the source-owner stability objection (the red team's #10: avoid renaming a source's home a *third* time). Introducing "Sources & Data" would be a third variant for marginal source-primacy emphasis. Rejected on churn/stability grounds. (One consequence remains: standardise casing/ampersand/order across nav + footer + breadcrumbs — see §7.)

**Both refinements make the change *smaller and more defensible*, not larger** — every decided label now either is unchanged or matches a string already present in the repository (the Arabic Readings label; the footer Data label).

---

## 3. WHY OPTION A IS NOT DEFENSIBLE AS-IS

Four repo-confirmed defects, none a matter of taste:
1. **Untruthful label:** global "Data / البيانات" contradicts its own footer ("Data & sources / البيانات والمصادر"), family name and contents — a live semantic contradiction the product's own rules forbid.
2. **Ambiguous label + parity break:** English "Readings" is ambiguous and does not carry the bounded meaning its Arabic co-edition "قراءات الأدلة" already carries.
3. **Priority inversion:** the Measurement Agenda — a governed entry question (QE-010), the terminal step of the product's north star ("…what should be measured next"), and the most differentiated asset for expert audiences — is `CONTEXTUAL_FOOTER` (footer-only), while non-task **About** holds a `GLOBAL_PRIMARY` slot. This is the single clearest IA mis-weighting.
4. **Mis-grouping:** About is duplicated (global primary **and** footer) and, in the footer, filed under "Method and measurement" — a group that has nothing to do with institutional purpose/stewardship (which is what /about actually contains).

R4 previously re-affirmed the six-item bar, but that affirmation did not independently challenge these four specific label/prominence defects, which this session's independent challenge surfaced with evidence. Keeping A would mean shipping a known internal contradiction — precisely the semantic drift the constitution forbids. A is not kept for inertia.

---

## 4. CRITERIA ASSESSMENT (B-adjudicated vs A)

- **First-click comprehension / general-user:** improved (truthful "Data & sources"; unambiguous "Evidence Readings"). 
- **Expert efficiency / differentiation:** improved vs raw-B (retaining "Evidence Readings" keeps the governed-object signal experts rely on; "Analysis" would have hurt this).
- **Arabic naturalness:** item 3 unchanged (already idiomatic); item 4 adopts an AR label already in live use; family label "المنهج والقياس" already the footer heading. Net: natural, low-novelty.
- **English clarity:** items 3 and 4 both clearer and truthful.
- **Question-first integrity:** preserved — the 8 domain answers remain `CONTEXTUAL` (reached via the 11 questions); global nav stays the lateral verify/reference/analysis layer, not a competing task taxonomy.
- **Evidence-vs-Source distinction:** preserved at nav level; **note** an object-level seam exists below nav (some `DS-*` source-flavoured records sit under `/evidence/`) — logged for Tranche C, not fixed by relabeling.
- **Visibility of Measurement Agenda:** materially improved (footer-only → primary family child, equal weight).
- **Find CBY decisions/laws; find datasets/surveys:** improved (truthful "Data & sources"; A3 library model reinforces).
- **Discover analytical Readings:** preserved/improved (clearer EN label).
- **Mobile header load / RTL:** 5 primary items + a Trust affordance is *lighter* than 6; but the Method & Measurement **family** and any compound labels **reopen the S05.2 320–400px assertion suite** → mandatory re-test (see §7).
- **Competing mental models / route churn / deep-link preservation:** **zero route changes** — all 108 `/evidence/`, 10 `/readings/`, 8 domain and trust deep links survive; no citation/deep-link breakage.
- **Maintenance / semantic-drift risk:** reduced (resolves the existing Data header/footer contradiction; consolidates About).

---

## 5. MEASUREMENT AGENDA — PROMOTE (as family child, not 7th item)

Promote from `CONTEXTUAL_FOOTER` to the primary layer **as the second child of the Method & Measurement family**, at zero extra header-item cost. Justification by user function: it is a governed entry question (QE-010); it is the north star's terminal step; the analytical layer already routes into it (`/readings/` next-action → `/measurement/`); and it is the highest-value asset for CBY/DFI/donor/researcher users. **Hard condition:** the family must resolve to **two distinct destinations**, each keeping its own route, label and H1 — Methodology (`/methodology/`, "Methodology / المنهجية") and **Measurement Agenda** (`/measurement/`, "Measurement Agenda / أجندة القياس", retaining "Agenda / أجندة" which the group label drops). It must **never** be a merged page or a flat single link that re-subordinates Measurement under "Method" (the semantic firewall keeps method ≠ measurement). The presentation mechanism (dropdown / mega-menu / two-card hub landing) is a Design choice; its acceptance test is "both children equally weighted, each independently reachable."

---

## 6. ABOUT — DEMOTE BUT DO NOT BURY

Move About out of the primary five into a **prominent** secondary Trust layer, grouped with its true siblings (Corrections, Rights & reuse, Accessibility, Privacy, Terms, Contact) and removed from the "Method and measurement" footer group. "Secondary" must **not** mean "buried": expose the Trust layer via a persistent affordance (e.g. top-right utility) so a journalist under deadline can reach "who published this / can I trust it" in one obvious click, and so CauseWay institutional accountability (there is a CauseWay Institutional Profile) stays visible. Freeing this primary slot is what lets Measurement rise without a seventh header item. (Arabic label refinement "عن الموقع" → "عن المنصة/من نحن" is an editorial item deferred to Tranche B.)

---

## 7. CONSEQUENCE MAP (must be propagated coherently — NOT a menu rename)

Because nav labels are **controlled public semantic copy**, the change is Master-first, then regenerate. Every downstream area:

1. **Production Master** — register final EN+AR labels ("Evidence Readings/قراءات الأدلة" EN side only; "Data & sources/البيانات والمصادر"; "Method & Measurement/المنهج والقياس" family; About→Trust) as controlled semantic copy; then regenerate `page_specs.json` (141) + dependent JSON.
2. **`navigation_interaction.json` → `global_navigation`** — relabel `/readings` (EN) and `/data` (EN+AR); introduce the Method & Measurement family (children `/methodology`, `/measurement`); remove `/about` from global primary.
3. **`navigation_prominence` fields** — `/measurement` `CONTEXTUAL_FOOTER`→primary (family child); `/about` `GLOBAL_PRIMARY`→secondary Trust. Update matching `page_families` entries + route records.
4. **Footer** — the "method_measure" group now largely mirrors the primary family: reconcile (repurpose/drop; do not duplicate). Move About into "trust_use". Standardise the Data label to the single canonical "Data & sources / البيانات والمصادر" (already there) and fix casing/ampersand/order so nav and footer agree.
5. **Breadcrumbs** — document the deliberate rule: page identity vs nav label. (`/readings` page H1 = "Evidence Readings / قراءات الأدلة" = nav label now, so no split; `/measurement` breadcrumb = "Measurement Agenda / أجندة القياس".)
6. **Search taxonomy** (`search_index.json`, 427 records) + facets — rename any "Readings"/"Data" facet to match; surface Measurement as a primary facet.
7. **Intro/landing copy** (Home, `/explore`) and any prose enumerating the nav or naming "Readings"/"Data" — rewrite in **both** EN and AR (co-authority; Arabic reviewed independently, not back-translated). → **This is Tranche B work.**
8. **Resource-Library section intro** inside `/data` — confirm its 26-card category copy matches the new "Data & sources" parent (routing unaffected).
9. **Mobile/RTL** — **re-run the S05.2 320–400px assertion suite** for the changed header (compound label "Data & sources / البيانات والمصادر"; the Method & Measurement family expansion; the 5-item + Trust-affordance layout). Do not claim mobile/RTL pass on the new header until re-tested.
10. **Design handoff** — encode 5 primary items + the Method & Measurement family (two equal children) + a prominent, non-buried secondary Trust layer; preserve all deep links (no route changes).

---

## 8. SEQUENCING (no half-transition)

Per the user's tranche staging ("do not perform final corpus-wide language rewriting yet" in A4; "settle IA before bilingual rewriting"), the IA change is **decided in Tranche A but executed atomically at the start of Tranche B**, where the bilingual intro-copy and search-facet propagation naturally live. Tranche A does **not** begin partial relabeling (that would be the forbidden half-transition). The execution is a single Master-first operation: Master → regenerate → `navigation_interaction.json` + prominence fields → footer/breadcrumbs/search → bilingual intro copy → rebuild → validate → re-run mobile/RTL → refresh manifest.

**Honest status labels:** IA decision = **EXECUTED (decision) / VERIFIED BY CLAUDE TEAM** via three independent challengers. Propagation = **SCHEDULED (Tranche B)**. Mobile/RTL re-acceptance on the new header = **PENDING**. Independent OpenAI acceptance = **REQUIRED**.

*End of S01 IA decision.*
