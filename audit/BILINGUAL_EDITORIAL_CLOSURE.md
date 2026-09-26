# Bilingual editorial closure — semantic invariance

**Status:** `VERIFIED_BY_CLAUDE_TEAM` · `SPEC_PENDING_EXECUTION` · `INDEPENDENT_OPENAI_ACCEPTANCE_REQUIRED`. Arabic rows also carry `EXTERNAL_HUMAN_CERTIFICATION_NOT_PERFORMED`.

Arabic and English are co-authoritative. Neither is a translation of the other, and neither may say more or less than the other about number, unit, universe, denominator, geography, period, currentness, method, evidence state, authority, certainty, limitation, rights or what to measure next.

Detailed language rules sit in two companion files:
- `ARABIC_TERMINOLOGY_AND_STYLE_LEDGER.md`, for the Arabic;
- `ENGLISH_EDITORIAL_CLOSURE.md`, for the English.

This file records the **invariance** test and its results.

## 1. Exemplar parity break — CLM-008 (LEAD-M01)

CLM-008 concerns the CBY-Aden list of licensed banks, the most politically loaded object in the product.

| | Before | After (PB-0200–0202) |
|---|---|---|
| `does_not_prove_en` | Do not infer active branches, products, market share or rail participation. | Do not infer active branches, products, market share or payment-rail participation. Appearing on the list establishes listing or licensing in that source only; it does not establish operation, all branches, participation, or national coverage **beyond the scope of the issuing authority**. |
| `does_not_prove_ar` | …ولا يثبت التشغيل أو جميع الفروع أو المشاركة أو التغطية الوطنية **خارج نطاق سلطة المصدر**. | unchanged (it was already the stronger text) |
| page body EN | The system controls a 26-row current CBY-Aden licensed-bank source list… | The current CBY-Aden list of licensed banks names 26 banks. Appearing on the list establishes listing or licensing in that source, not operation. |
| page body AR | …26 صفًا مصرفيًا… | …تضم 26 بنكًا… |

**Lesson.** The authority-scope limit existed in only one language. A CBY regulator or a counterparty reading the English would have found no statement that the list's reach ends at the issuing authority. The fix brings English up to the Arabic, not the reverse.

## 2. Mechanical invariance test (numbers)

**Method** (`audit/tranche_b_patch_tooling` companion, re-runnable):
- For every bilingual field pair in 02, 03, 05–11, extract the numbers from each language, normalising Arabic digits, thousands separators, year ranges and number words.
- Compare the two sets, before and after applying the whole spec.
- 750 field pairs carry numbers.

| | Pairs whose number sets differ |
|---|---|
| Before the spec | 46 |
| After the spec | 22 |

**Resolved by the spec (examples):**
- CLM-031: the Arabic claim omitted the claim itself (PB-0527/0528);
- the /evidence/CLM-007/ Arabic body still called the IMF series «الموثقة» and dropped "2026–2030" (PB-0195A);
- the RV-CWR-007 levels (PB-0449/0450);
- the three 2014 records whose English titles carried no year (PB-0572–0574);
- the /people/ title (PB-0526);
- the fieldwork dates «2022–2023» (PB-0529/0576).

**Remaining 22, all reviewed:**
- **10 are normalisation artefacts** of the test: ISO dates and month ranges such as "2026-01 to 2026-08" or "2026-09-10" against «من يناير إلى أغسطس 2026» or «10 سبتمبر 2026». Not differences.
- **12 field pairs are one-language-more-specific, not contradictory, in fields that do not render or render only as a method note:**
  - 11 r18/r23/r24/r25/r27/r28/r30/r32/r36 (`decision_value` / `what_it_shows`);
  - 06 r74/r75 (`method_ar` carries 18, 31, 328 and 91.84).

  These are recorded as P5 residual asymmetries. They do not change meaning.

## 3. Invariance by dimension — breaks found and their patches

| Dimension | Break found | Patch |
|---|---|---|
| Number | CLM-031 AR lacked the 2022/2014 thesis; CWR-007 thesis and RV-CWR-007 led with the gap only (both languages, with differently worded Arabic variants) | PB-0527/0528; PB-0590–0593; PB-0436/0445/0449/0450 |
| Unit | CWR-001 AR rendered CCY (Cash Consortium of Yemen) as «من العملة المحلية»; EN "CCY 7.4bn" unexplained | PB-0362/0363 |
| Universe | 12 ungoverned VISUAL records: `universe_en` is a placeholder, AR states the population | PB-0560–0571 |
| Denominator | /evidence/compare/ AR lists fewer compatibility dimensions than EN (F-01) | PB-0370 |
| Geography | RV-CWR-008 EN omitted "seven-governorate" (AR had it) | PB-0446 |
| Period | 2014 records untitled by year in EN; fieldwork «موجة 2022» vs "2022–23" | PB-0572–0574; PB-0529/0576 |
| Currentness | /people/ AR title asked a different question from the EN thesis | PB-0526 |
| Method | CWR-001 internal jargon (E&O, 1.838, 33%) in both languages | PB-0362/0363 |
| Evidence state | "observed history" / «تاريخ مرصود» for IMF-reported values; «الموثقة» on the CLM-007 AR variant | PB-0170–0196, PB-0195A |
| Authority | CLM-008 scope clause AR-only; «القائمة الرسمية للبنك المركزي» without «عدن»; VIS-PROVIDER-TIME AR | PB-0200–0216, PB-0513 |
| Certainty | OECD/INFE Yemen scores asserted in both languages without confirmation | PB-0101–0106 (both) |
| Limitation | RV-CWR accessible summaries: AR is prose, EN is drawing instructions (19 fields) and 13 record summaries | PB-0430–0448, PB-0500–0512 |
| Rights | /data/ rights promises in both languages exceed any field that exists | PB-0380–0389 (both) |
| Measurement-next | MA-003 omits the measured income gap (both); MA-001 lacks remittance receipt (both) | PB-0320/0321, PB-0325–0330 |

## 4. Two further parity items

**YPCC.** The Arabic names a "centre" («مركز اليمن للمقاصة وتسوية المدفوعات»); the entity is a company. PB-0230 renames it «الشركة اليمنية للمدفوعات والمقاصة» across 11 cells. The exact registered form is `PRIMARY_SOURCE_PENDING`.

**Compare dimensions (F-01).** The English lists universe, unit, period, method, evidence type, denominator and geography. PB-0370 brings the Arabic list to the same seven. PB-0371 adds to both languages that "not comparable" is a valid result.

## 5. Rule for the executor

- **Pairs execute together.** An English row and its Arabic partner are executed in the same regeneration.
- **Reciprocal patches.** When a patch changes meaning in one language, the partner patch is listed in the row's `reason` or `source_basis`. For example, PB-0202 → AR unchanged; PB-0527 ↔ PB-0528.
- **No lone rows.** A row never executes without its partner.
- **Re-run after regeneration.** The invariance test is repeated after regeneration. The expected result is 10 artefacts plus the 12 recorded asymmetries, or fewer.
