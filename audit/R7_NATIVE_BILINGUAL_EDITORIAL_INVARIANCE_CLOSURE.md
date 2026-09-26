# R7 — Native Bilingual Editorial Invariance Closure

Status: **CLOSED / PASS**

## Owner and challenge lenses

Owner: Arabic/English editorial lead. Challengers: quantitative editor; RTL/accessibility reviewer.

## Scope actually checked

- 141 Page Specs: title, full public copy, section-order language coverage, route identity and shared governed bindings.
- 10 Readings and 90 Reading sections.
- 10 Measurement Agenda priorities.
- 59 public claims.
- 36 visual contracts and their accessible summaries / prohibited-inference text.
- 24 chronology events.
- 26 curated bilingual Resource Library cards.
- Representative rendered Arabic/English output, including dense Payments and Evidence Record states.

## Results

- Missing required bilingual title/full-copy fields in Page Specs: **0**.
- Section-order groups missing one language: **0**.
- Paired bilingual-field gaps in Readings, Reading sections, Measurement Agenda, public claims, visual contracts and chronology: **0**.
- Curated Resource Library cards missing bilingual title/category/value/boundary copy: **0**.
- Public Arabic leakage of internal-control terms such as Production Master, Page Spec, governed/backend/payload or obsolete Arabic control vocabulary: **0**.
- Unintended multiword English prose leakage in Arabic public copy: **0**. English strings retained in Arabic are deliberate names/identifiers or requested email subject identifiers (for example the product name).
- Numeric/date representation differences flagged heuristically were reviewed as formatting/language forms (for example `2022–23` versus `2022–2023`, `55,000` versus `55 ألفًا`, quarter/stage labels written as words) rather than semantic drift. No material number/unit/universe/period widening was identified.
- Current generated baseline confirms `lang="ar" dir="rtl"` and `lang="en" dir="ltr"`; stable/source identifier styling retains bidi isolation in RTL.

## Editorial invariance rule carried forward

Arabic and English may differ syntactically and compositionally. They may not differ in:

**number · unit · universe/denominator · geography · period/currentness · method · source authority · certainty · limitation · rights boundary · target/result state · unknown state · measurement-next meaning**.

Preferred public Arabic language remains reader-facing rather than internal-control language, including `سجل الدليل`, `المجتمع الذي ينطبق عليه الرقم`, `قاعدة الاحتساب`, `حداثة الأدلة`, `طريقة الاحتساب`, `ما الذي لا يثبته هذا الدليل`, `ما الذي ما زلنا لا نعرفه` and `ما القياس الذي سيغير القرار`.

## What became more true

The handoff no longer asks Claude Design to infer what “bilingual” means. It now inherits a tested semantic-invariance contract plus explicit RTL/mixed-script behavior.

## What became more complex

No semantic complexity was added. The only added complexity is explicit acceptance of native Arabic composition and bidi behavior rather than a visually mirrored English template.

## What can now be removed later

R8 can remove or isolate old bilingual QA prompts/checklists that do not carry unique lineage value. The final recipient only needs the current Master/Page Specs, the current bilingual design contract and the clean handoff package.

## Production authority

No semantic/evidence correction was required in R7. The Production Master remains unchanged and authoritative at SHA-256 `ce552bdbd0e0070866098b28145f9b1dad43f0015679d12cb9235b13d14abf7d`.

## Verification

Current static baseline revalidated after R6/R7 handoff changes:

- 141 Page Specs
- 282 localized route documents
- 284 HTML documents including root and 404
- `ERRORS=0`
- `WARN=0`
- `WEBSITE REPOSITORY VALIDATION PASS`

## Next bounded session

**R8 — Clean-room handoff.** Audit every repository folder and filename, isolate/remove obsolete recipient-facing material and active-folder duplicates, promote the actual start files, re-hash/re-validate, and finalize the single Claude Design launch prompt so an unfamiliar recipient can build the fully populated static product without chat history or repository archaeology.
