# Methodology completeness closure (addendum §7, §8, §19)

> **Execution-state correction (Tranche B execution, 2026-09-26).** Source roles are relationship-level and multi-valued, document type stays separate, no quality score (correction E); publisher and rights follow correction F.


**Status:** `VERIFIED_BY_CLAUDE_TEAM` · `SPEC_PENDING_EXECUTION` · `INDEPENDENT_OPENAI_ACCEPTANCE_REQUIRED`

`/methodology/` explains the public evidence method: the rules a reader needs in order to judge a number. It does not describe internal controls. It stays short, and detail is available by opening each section.

## 1. Completeness check

| Element a reader needs | Present today | Disposition |
|---|---|---|
| What is being measured (people ≠ accounts ≠ providers ≠ transactions …) | s2 "Start with the object being measured" | ADEQUATE |
| Evidence clocks (different dates can all be true) | s3 | ADEQUATE; made concrete by PB-0611 |
| **Coverage: what the evidence covers and what it does not** | absent | **MATERIAL GAP → PB-0611** |
| **Source admission and evidence role** | absent (partly on /data/) | **MATERIAL GAP → PB-0612** |
| Derived values are reproducible | s4 | ADEQUATE |
| **Precision and uncertainty** | applied on /people/ (PB-0311) but not stated as a rule | **PARTIAL → PB-0614** (no manufactured intervals; precision follows the inputs; small differences are not a ranking) |
| Comparability comes before comparison | s5 | ADEQUATE ("not comparable" as a valid result is added on /evidence/compare/, PB-0370/0371) |
| Public evidence states (observed, derived, historical, bounded …) | s6 | ADEQUATE. The orphan state "HISTORICAL_REPORTED" is now rendered as "reported history (staff calculations)" (PB-0170–0196). |
| What the method does not claim | s7 | ADEQUATE |
| Correction and revision | s8 | ADEQUATE |
| Challenge the answer / verification path | s9 | ADEQUATE; the per-record verification path is fixed (PB-0007/0008) |
| Composite scores and survey-round rules | s10 | ADEQUATE (OECD/INFE item-level prompts marked as reconstructed, PB-0110) |
| **Conflict-affected measurement** | spread across pages | **MATERIAL GAP → PB-0613** (divided authority; rial valuation by monetary area; incomplete survey coverage; programme universes; conflict is context, not cause) |
| Benchmarks and comparators | implicit | Stated in PB-0612 (global references inform method, never stand in for Yemen evidence). Full policy in `BENCHMARK_AND_COMPARATOR_POLICY.md`. |
| Rights and reuse | /data/ | Handled on /data/ (PB-0380–0390); not duplicated here |

**Result:** four sections are added (PB-0611–0614) and nothing is rewritten for style. /methodology/ grows from 10 to 14 sections. Each new section is one paragraph in each language.

## 2. Source-admission policy (the rule behind PB-0612)

1. **Admit** a source when its original locator and date can be recorded and its content can be checked against the source itself; its publisher, issuer and reuse terms are recorded when they have been confirmed (never inferred from a URL host; acceptance correction F).
2. **Record evidence roles per use** (acceptance correction E) — the role belongs to the source→record relationship (06 source_use_roles), and a source can hold several roles across uses (15 evidence_roles):
   - primary factual evidence;
   - dated status event;
   - Yemen analytical literature;
   - global method reference;
   - context.

   The vocabulary is shared with the Resource Library facet (PB-0493). Document type (15 document_type) is recorded separately and never collapsed into role. No numerical source-quality score is assigned. Values are populated only where the Master states the kind or the use; the rest stay unassigned.
3. **Figures:**
   - Primary evidence and status events support public figures directly.
   - A **secondary** figure appears only when it is attributed and labelled (e.g. the 2023 "active savers" figure via EP-MFB-SAVERS-2023-K04).
   - A figure that **cannot be verified** against its stated source is withheld (e.g. the OECD 2026 review figures, PB-0165; the OECD/INFE 2023 Yemen scores were withheld until verified and are now published survey-scoped, acceptance correction A).
4. **Currentness and revision.**
   - Each record keeps its observation, fieldwork, publication and retrieval dates separately.
   - A later vintage never silently overwrites an earlier one. Same-year revisions are shown as revisions (CWR-001, CLM-032).
5. **Context.** A context source (macro, humanitarian, conflict) may explain the setting of a figure. It never becomes the figure (`ECONOMIC_CONTEXT_USAGE_POLICY.md`).

## 3. Conflict-affected measurement (the rule behind PB-0613)

These are features of the measurement environment, stated once, on the method page:
- **Divided authority since 2016.** Lists, decisions and statistics carry their issuer's scope, CBY-Aden for this corpus. Absence from a CBY-Aden list is not "unlicensed elsewhere" (PB-0216).
- **Currency division.** Nominal rial values can differ between monetary areas. A nominal series is read with its valuation basis where the source records it. **An exchange-rate conversion is not a real-value adjustment** (directive correction A; LEAD-B01).
- **Incomplete coverage.** The latest Findex wave excluded areas holding about 23% of the population, and more than a quarter of sampling units were replaced (CLM-025).
- **Programme universes.** Programme and project figures describe their own populations (SMEPS, FMIIP, G2Px).
- **Causal discipline.** Conflict is context for interpretation, never an established cause of an observed result (ECONOMIC_CONTEXT_USAGE_POLICY).

## 4. Language

The four sections are written natively in both languages. Every number in them traces to the Master:
- 2016 → 14_SYSTEM_CHRONOLOGY;
- about 23% and "more than a quarter" → CLM-025;
- 15.5, 6.5 and 9.0 → 25_FINDEX_BASELINE.

They add no new fact.
