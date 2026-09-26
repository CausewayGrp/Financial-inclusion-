# Search and discovery closure

**Status:** `VERIFIED_BY_CLAUDE_TEAM` · `SPEC_PENDING_EXECUTION` · `INDEPENDENT_OPENAI_ACCEPTANCE_REQUIRED`

Search may help people **discover** evidence. It may never make two things equivalent in meaning: an alias routes a query, it does not equate concepts.

## 1. Method

The probe uses the validator's own scoring (`scripts/validate.py` lines 1284–1326: token match on stable ID, title, summary and search text, with Arabic normalisation of hamza and alef forms and diacritics) against the built `dist/static-data/search_index.json`. It ran 28 terms in each language. The result for a term is:
- **PASS** if an expected route is in the top 3;
- **WEAK** if it is in the top 10;
- **FAIL** otherwise.

The number in brackets is the rank of the first expected route.

**Result today:** English 13 PASS / 9 WEAK / 6 FAIL; Arabic 11 PASS / 10 WEAK / 7 FAIL. The earlier specialist wave reported 18/8/2 (EN) and 16/9/3 (AR) on a different term list; the two lists are not directly comparable.

## 2. Probe results (28 terms × 2 languages)

| Term | EN query | EN | AR query | AR | Expected route(s) |
|---|---|---|---|---|---|
| account ownership | `account ownership` | PASS (1) | `امتلاك الحساب` | PASS (1) | /people/, /evidence/CLM-001/ |
| gender gap | `gender gap` | PASS (1) | `الفجوة بين الرجال والنساء` | PASS (1) | /people/, /readings/gender-gap-measured-causes-open/ |
| income gap | `income` | FAIL (—) | `الدخل` | FAIL (—) | /people/ |
| financial literacy | `financial literacy` | FAIL (—) | `الثقافة المالية` | WEAK (7) | /people/, /reforms/ |
| microfinance | `microfinance` | PASS (1) | `التمويل الأصغر` | FAIL (—) | /finance/, /readings/microfinance-structural-divergence/ |
| credit | `credit` | WEAK (5) | `الائتمان` | WEAK (4) | /finance/, /firms/ |
| deposits | `deposits` | PASS (2) | `الودائع` | PASS (2) | /finance/ |
| SME finance | `SME finance` | WEAK (10) | `تمويل المنشآت الصغيرة` | PASS (2) | /firms/ |
| POS | `POS terminals` | FAIL (—) | `نقاط البيع` | FAIL (—) | /payments/ |
| e-wallet | `e-wallet` | WEAK (4) | `المحافظ الإلكترونية` | WEAK (10) | /payments/, /providers/ |
| RTGS | `RTGS` | PASS (3) | `التسوية الإجمالية الفورية` | WEAK (6) | /payments/, /reforms/ |
| remittances | `remittances` | WEAK (5) | `الحوالات` | FAIL (—) | /remittances/ |
| remittance cost | `remittance cost` | PASS (2) | `تكلفة التحويل` | WEAK (7) | /remittances/ |
| exchange companies | `exchange companies` | WEAK (4) | `شركات الصرافة` | PASS (3) | /providers/, /access/ |
| licensed banks | `licensed banks` | WEAK (5) | `البنوك المرخصة` | PASS (1) | /providers/ |
| CBY Aden | `Aden` | PASS (1) | `عدن` | WEAK (5) | /providers/, /data/ |
| Sanaa | `Sanaa` | PASS (1) | `صنعاء` | PASS (1) | /providers/, /data/ |
| CBY decision | `decision` | FAIL (—) | `قرار` | FAIL (—) | /data/, /providers/, /reforms/ |
| law | `law` | FAIL (—) | `قانون` | PASS (1) | /data/, /reforms/ |
| regulation | `regulation` | WEAK (6) | `لائحة` | FAIL (—) | /data/, /reforms/ |
| consumer protection | `consumer protection` | WEAK (7) | `حماية المستهلك` | WEAK (7) | /reforms/ |
| complaints | `complaints` | PASS (3) | `الشكاوى` | WEAK (4) | /reforms/ |
| FMIIP | `FMIIP` | WEAK (7) | `FMIIP` | WEAK (7) | /reforms/, /payments/ |
| cash transfer | `cash transfer` | PASS (1) | `التحويل النقدي` | PASS (3) | /readings/after-transfer-persistence/, /payments/ |
| identity KYC | `KYC` | PASS (1) | `اعرف عميلك` | PASS (1) | /payments/, /people/, /measurement/ |
| access points | `access points` | PASS (1) | `نقاط الوصول` | PASS (3) | /access/ |
| exchange rate | `exchange rate` | FAIL (—) | `سعر الصرف` | WEAK (7) | /finance/, /data/ |
| measurement agenda | `measurement` | PASS (1) | `القياس` | FAIL (—) | /measurement/ |

**Diagnosis:**
- **Legal and regulatory discovery fails.**
  - "law" returns **no results** in English, and «لائحة» returns none in Arabic.
  - "decision" / «قرار» never reach a decision record in the top 10.
  - Cause: 132 source records are `LOCATOR_ONLY` and unindexed, one source (`SRC-MOPIC-YSEU-2023-080`) is missing from the index (158 of 159), and there is no document-type facet.
- **Domain pages rank below their own records.**
  - "POS terminals" and «نقاط البيع» never reach /payments/ in the top 10.
  - «الحوالات» never reaches /remittances/.
  - Cause: evidence records carry the term in their title and summary more densely than the domain page does.
- **Arabic morphology.** «التمويل الأصغر» fails where "microfinance" passes, and «القياس» fails where "measurement" passes. There is no light stemming: the definite article and prefixes are not normalised.
- **Evidence the page does not yet state.** "income" / «الدخل» fail because /people/ does not yet mention the income gap. PB-0302/0303 add it.

**Smoke tests.** The repository's 9 bilingual smoke tests pass under the validator's rule, which accepts a test if **any** expected route is in the top 10. Under an **all-expected-routes** rule, two fail in both languages: "POS terminals" / «نقاط البيع» and "Fast Payment System" / «نظام الدفع السريع». That reconciles the specialist finding "2 of 9 fail". The ANY rule is too weak to catch a missing answer page.

## 3. Fixes (R1–R13) and their patches

| R | Fix | Patch |
|---|---|---|
| R1 | Index all 159 sources (add `SRC-MOPIC-YSEU-2023-080`) | PB-0490 |
| R2 | Surface the 132 `LOCATOR_ONLY` records with publisher and document type, **only after** the publisher and rights fields exist (otherwise the defect multiplies) | PB-0490 after PB-0390 |
| R3 | Index `does_not_prove_*` and `prohibited_inference_*` as a separate low-weight field, so boundary queries ("does not prove", «لا يثبت») find the limit | PB-0491 |
| R4 | English light stemming (singular/plural, -ies/-y) | PB-0491 |
| R5 | Arabic normalisation: the definite article «ال», the prefixes «و/ب/ل/ف», ta marbuta and ha, alef forms | PB-0491 |
| R6 | A domain page whose title or primary question contains the query term ranks first for that term | PB-0493(a) |
| R7 | 12 governed bilingual discovery aliases (law, decision, circular, regulation, remittance, exchange company, wallet, POS, microfinance, exchange rate, measurement agenda, financial literacy), held in the Master (04_NAV_UX) | PB-0492 |
| R8 | **Rejected:** a broad issuer-only alias ("CBY" → every CBY document). It would flood every query with CBY material and make "CBY" mean nothing | PB-0491/0492 (recorded) |
| R9 | **Caveated:** financial literacy ↔ financial education is discovery-only. The result shows "financial-education activity is not literacy, capability or behaviour" (semantic firewall) | PB-0492 |
| R10 | Document-type facet for sources (law · decision · circular · regulatory instruction · report · survey · dataset), kept distinct from **evidence role** | PB-0493(b) |
| R11 | Result cards show evidence state and observation/publication date, so historical records are not read as current | PB-0493(c) |
| R12 | Smoke tests: keep the 9, add 12 from this probe; the primary route must be in the top 3 | PB-0494 |
| R13 | Arabic-first vocabulary: Arabic queries succeed without English IDs («صرافة», «حوالة», «محفظة»), through R5 and R7 | PB-0491/0492 |

**Acceptance after regeneration:**
- all 28 probe terms reach an expected route in the top 3, in both languages;
- the 21 smoke tests pass under the top-3 rule;
- "law" and «قانون» return legal instruments;
- no alias result claims equivalence.

## 4. Term-list note

The Tranche B brief's §37 term list is not in the handed repository. The 28 terms above were chosen to cover:
- every domain;
- the legal and regulatory vocabulary;
- the firewall-sensitive pairs (literacy and education, accounts and people);
- the terms users type in both languages.

The list becomes the regression suite through PB-0494.
