# Economic system and evidence review (addendum)

> **Execution-state correction (Tranche B execution, 2026-09-26).** The firms/exchangers link is stated in the accepted wording; its public section (PB-0520) is held at execution.


**Status:** `VERIFIED_BY_CLAUDE_TEAM` · `SPEC_PENDING_EXECUTION` (for the patches named) · `INDEPENDENT_OPENAI_ACCEPTANCE_REQUIRED`

**Standard:** *more explanatory without becoming more speculative.*

Every proposal in the addendum was classified as one of four things:
- **ALREADY ADEQUATE** → preserve;
- **PARTIAL** → strengthen;
- **MATERIAL GAP** → resolve or specify;
- **NO MATERIAL VALUE** → reject.

Each was then put through the deletion test: if it were absent, would a reader lose something the evidence supports? No new fact is introduced here. Every value cited already exists in the Master (`INDICATOR_COVERAGE_MATRIX.csv` gives the basis for each).

## 1. Economic-function lens — what people and firms use finance *for*

The lens asks whether the evidence tells us how Yemeni people and firms **receive income, pay, save, borrow, send and receive money, and cope with shocks**. The account-ownership rate alone does not answer that.

| Function | Yemen evidence state | Class |
|---|---|---|
| Receive income (wages, government transfers, agricultural payments) | 2021 survey variables specified; weighted compute required | PARTIAL |
| Pay (digital payments; merchant payments) | People side: 2021 variables, compute required. System side: POS and e-wallet counts (administrative, 2024–2026) | PARTIAL / ADMINISTRATIVE ONLY |
| Save | 2014 published; 2021 held but not estimated | HISTORICAL |
| Borrow (people) | 2014: 65.9% borrowed any money, 51.7% from family or friends, 0.4% from a financial institution | HISTORICAL |
| Send / receive (domestic remittances) | 2014: 18.3% of adults received | HISTORICAL |
| Receive international remittances (households) | Not measured; macro series only | NO CURRENT YEMEN EVIDENCE (household) |
| Cope with shocks (emergency funds; financial worry) | 2021 variables specified; compute required | PARTIAL |
| Firms: finance working capital | 2022 seven-governorate survey: 69.12% internal, 0.56% banks (formal firms) | HISTORICAL (sample-bounded) |
| Firms: transact and move money | 73.48% use money exchangers, 24.39% banks (multiple response) | HISTORICAL (sample-bounded) |
| Firms: access programme finance | SMEPS KPI 19% (2024), 15% (2021–2024), supported firms only | PROGRAMME-SPECIFIC |
| Households under humanitarian programmes | G2Px pilot: 45,460 recipients in eight districts; persistence not measured | PROGRAMME-SPECIFIC |
| Macro and conflict conditions (currency division, liquidity) | Chronology and monetary series | CONTEXT ONLY |

**Decision: PARTIAL → strengthen within existing pages. No new "financial lives" page.**

The lens is already latent in the product: the demand-vintage ladder, CLM-031, MA-001 and the /firms/ page. It is strengthened in three ways:
- the /firms/ behavioural evidence (PB-0520) and the /payments/ subscriber series (PB-0521) are published;
- MA-001 is extended to remittance receipt (PB-0325–0330);
- the /methodology/ coverage statement (PB-0611) tells readers which functions are current, historical or computed-but-withheld.

A new page would repeat CLM-031 and VIS-DEMAND-VINTAGE-LADDER and fail the deletion test.

## 2. System transmission — ALREADY ADEQUATE, with its links now visible

The product's system view runs from rules and rails, through providers, access and use, to quality and outcome (VIS-INCLUSION-TRANSMISSION, CWR-009, MA-010). It is sound. What was missing was the connection *from the domain pages* to that view. Two changes supply it:
- **Domain → Reading links** by per-pair test (PB-0426): /payments/, /access/ and /reforms/ surface CWR-009.
- **Provider and access facts on the pages where the question is asked:** the exchange and remittance roster and the bank list move onto /access/ (PB-0522), and provider structure onto /finance/ (PB-0524).

**The strongest cross-domain link.** Among the surveyed formal firms (2022, seven governorates), money exchangers were the most frequently reported intermediary in that multiple-response item (73.48% named an exchange store or money exchanger; firms could name more than one, so these are not market shares). That ties /firms/ to the exchange and remittance sector on /providers/ and /access/. The /firms/ section that states it (PB-0520) is held at execution by the literal-closure rule, so it is not yet public. No causal arrow is drawn.

## 3. Evidence clocks — ALREADY ADEQUATE, made explicit

"Several evidence clocks can be true at once" is already the second section of /methodology/, and VIS-EVIDENCE-FRESHNESS is the clock visual. Three changes make it explicit:
- PB-0611 names each clock in one paragraph (current: provider status, monetary statistics, remittance prices; latest-representative: 2022–23 fieldwork; historical: 2014; computed-but-withheld: 2021 variables);
- /people/ gets a title that carries the same thesis in both languages (PB-0526);
- undated historical titles get their year (PB-0572–0574).

## 4. Dispositions for the addendum's named topics

| Topic | Evidence | Disposition |
|---|---|---|
| Financial health and resilience | 2021 variables specified, not computed | **PARTIAL.** Keep VIS-FINDEX-RESILIENCE as a table-only record (PB-0401). No composite resilience score. Gap stated on /methodology/ (PB-0611). Measurement: MA-001. |
| Quality, reliability, affordability, cost | Remittance prices are current (2025 Q3). Service reliability: none. Account affordability: one barrier variable, not computed. | **MATERIAL GAP → specified, not filled.** Remittance cost is KEEP. Reliability and quality belong to MA-010 (latency, failure, cost dimensions). The gap is stated publicly (PB-0611). |
| Identity, KYC, onboarding | Rules documented; "lack of documentation" barrier variable held; no journey data | **PARTIAL.** Remains MA-007. No identity page: rules would be read as outcomes. |
| Humanitarian and G2P persistence | G2Px pilot (45,460 recipients, eight districts); no follow-up | **ALREADY ADEQUATE in concept (CWR-010, MA-009); PARTIAL in execution.** The G2Px paragraph is restored (PB-0360/0361). |
| Consumer protection | Framework documented; outcomes open | **ALREADY ADEQUATE** (CLM-011, VIS-FCP-REDRESS-PATH, MA-006). FCP reference 589 added (PB-0480/0481). |
| Displacement, disability, age | No comparable measures (age held) | **MATERIAL GAP → stated** (PB-0611; MA-003). No proxy is imported. |
| Digital safety and fraud | Only a dated negative list (2024) | **MATERIAL GAP → stated.** A negative list is not an incidence measure. |
| Insurance and pensions | None | **NO MATERIAL VALUE now.** Stated as absent (PB-0611). No measurement priority is added: neither changes a governed decision question today, so they fail the deletion test for a new MA. |

## 5. The signature system map

The addendum proposed a system + evidence map. **Decision: ALREADY ADEQUATE — VIS-INCLUSION-TRANSMISSION is that map**, with an evidence state on each link and no score. Its English description is rewritten as a description (PB-0465). See `SIGNATURE_VISUAL_CANDIDATES.md` for all six candidates.

## 6. What was deliberately not done

- No page, framework or indicator was added where an existing object answers the question.
- No global value fills a Yemen gap.
- No composite score, ranking, forecast model, conflict heat map or operating-provider map.
- Conflict is used only where it changes interpretation (`ECONOMIC_CONTEXT_USAGE_POLICY.md`).
