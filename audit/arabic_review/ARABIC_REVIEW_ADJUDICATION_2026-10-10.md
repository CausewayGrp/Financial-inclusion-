# Arabic editorial review — lead adjudication (10 October 2026)

**Input:** OpenAI "YFIE Arabic Editorial Decision Package" (11 files; SHA256SUMS verified).
**Adjudicator:** programme steward (advisor), for the owner. This is the only editorial decision on that package. Its
output is `YFIE_ARABIC_ACCEPTED_EDIT_REGISTER_2026-10-10.csv`. The raw package is lineage, not instructions.

## 1. Is the review current?
Yes. All 38 rows were checked by script against `main@2ddbfb611bb139d9597aec9b6b79153699cc4d94`:
- **38/38** `original_exact` strings match the projections byte for byte;
- **38/38** `original_sha256` values match;
- every row was located in the Production Master. 36 rows sit in `03_PAGE_SECTIONS` or `04_NAV_UX`; AR-042 and AR-062
  sit in `06_EVIDENCE_OBJECTS` (R5C7, R28C7).

The Master's SHA-256 was recomputed from the bytes: `58b8f3ec5ac1324dfafc7eb6b4015b88da0cb9c241078903be82fe0f6492421b`.
It equals AUTHORITY.json; OpenAI could not recompute it.

Two rationales (AR-026, AR-028) cite words that are not in the current text («تدفعنا», «فتح الحساب»). The proposed texts
are current; those two explanations were written loosely. Both rows were therefore judged on the text alone.

## 2. Decisions (39 rows: 38 reviewed + 1 added)

| Decision | Count | Rows |
|---|---|---|
| ACCEPT | 20 | AR-002, 005, 009, 010, 012, 013, 016, 019, 023, 029, 035, 037, 039, 043, 049, 053, 058, 060, 062, NEW-001 |
| REVISE (complete text given) | 10 | AR-003, 004, 008, 026, 031, 045, 056, 061, ED-035, ED-037 |
| REVISE_CONDITIONAL (source decides) | 5 | AR-001, AR-022, AR-042, ED-034, ED-036 |
| RETAIN | 3 | AR-028, AR-036, ED-038 |
| ADDED by adjudication | 1 | ADJ-RG-01 (the false "reuse terms not assessed for any source" sentence on /rights/ §2 and /data/ §5) |

## 3. Where the adjudication goes beyond the review
- **Findex definition (AR-001, AR-042).** OpenAI asks for the World Bank definition, which includes personal mobile-money
  use. The repository audit found more: in Yemen's study the mobile-money questions were not asked.
  - Open data show `fiaccount.t.d = account.t.d = 11.9` and `mobileaccount.t.d` null.
  - The public text must therefore say that 11.9% reflects financial-institution accounts. This is conditional on
    confirmation from public World Bank documentation.
- **Confidence intervals (ED-034).** OpenAI is right that "never narrower" overclaims. The audit adds that the World Bank
  likely publishes a Yemen margin of error and design effect. If so, that becomes the basis (Option A in the
  register).
- **Rights wording (AR-008, AR-056, ADJ-RG-01).**
  - Verified: 166 sources are NOT_ASSESSED and one (SRC-WB-FINDEX-001) is RESEARCH_LICENCE__AGGREGATE_STATISTICS_ONLY.
    So "for any source" is false, and OpenAI's own draft overstated what each card shows.
  - Fix: one consistent sentence, "for most sources".
- **Bank classification (AR-022, ED-036, ED-035).** "12 microfinance banks" must say whether the CBY-Aden list itself
  classifies them, or this resource infers it from their names. The list decides which wording is true. The check
  date is not an effective date.
- **Readings.**
  - CWR-007 keeps its analytical question (it asserts no cause) and drops the value-laden "إصلاح النساء".
  - CWR-011's opening becomes "shows where its funds go", not "whom it serves".
  - CWR-005's heading is retained, for vocabulary consistency with CWR-010.

## 4. House style
OpenAI's `03_ARABIC_HOUSE_STYLE_AND_TERMS_AR.md` is adopted as guidance under the Master terminology register. It is
committed as `audit/naming/ARABIC_HOUSE_STYLE.md`. Key rules:
- الحوالات / حوالات من الخارج / التحويلات النقدية (for programmes only);
- القراءات التحليلية;
- the navigation labels الأسئلة · الأدلة · القراءات التحليلية · المصادر · المنهج والقياس (confirmed; D8 closes);
- «هذا المورد» for legal and system self-reference, otherwise الصفحة / السجل / القراءة;
- البنك المركزي اليمني – عدن when attributing a document;
- digits 0–9 in data;
- narrative dates «7 نوفمبر 2022»; ISO only in technical fields, isolated with bdi;
- «نقطة مئوية» for differences between shares;
- مرخّص ≠ عامل; مسجّل ≠ نشط;
- no internal status words (HOLD) in public text;
- «غير معروف — ولا يعني صفرًا»;
- البنوك in prose, and the legal name exactly as the source gives it.

## 5. What the review did not cover (stated by OpenAI; recorded here)
- No human read of all 144 pages.
- No live-browser test.
- No independent statistical or legal review.

New Arabic written by the close-out brief is reviewed by the W7 editorial pass and listed in
`NEW_ARABIC_SINCE_2ddbfb61.csv`.

## 6. Application rules for Claude Code
- Apply only the accepted register. Match `master_cell` + `exact_old_ar` + `original_sha256` before writing; stop on
  any mismatch. No fuzzy or regex replacement.
- Rows with `apply_in = AR-1` go in one Master transaction, AR-1, right after CLOSE-1. Rows tied to a factual fix go in
  the same transaction as that fix (CLOSE-2, CLOSE-3 or CLOSE-5). There the exact-match check runs against the
  2ddbfb61 text recorded in the register, and the merge is documented.
- EN changes go in the same transaction as their AR row. Bilingual numeric invariance stays at 0. AR-001 adds "12" in
  both languages; ⟦CR-14⟧ is resolved from the source.
- Conditional rows follow their `condition` column; when the condition fails, they use `alt_new_ar` or the stated
  option.
