# Re-verification of P4 fixes V-D1 to V-D16 (hostile-but-fair, read-only)

- **Scope:** read-only. Repository state is as of 04:45–05:05 EEST on 2026-09-26.
- **Hashes (actual bytes):**
  - Master: `3acea612…3935244`.
  - Page Specs: `09174897…c8c3`.
- **Gates run** (all with `PYTHONDONTWRITEBYTECODE=1`):
  - `generate_projections.py --check`: PASS (40 outputs, 0 differences).
  - `validate.py`: `HTML=288 ERRORS=0 WARN=0`, PASS.
  - Unit tests: 21/21 OK.
  - `architecture_diagrams.py --check`: CURRENT.
  - Internal link check: 13,009 links, 0 broken.
- The team's `dist/` was built after the current Master, and no cache directories are present.

## Verdict table

| # | Item | Verdict |
|---|---|---|
| D1 | CCY / 7.4 / completeness claim | **CONFIRMED FIXED on every public surface.** **DEFECT REMAINS in the Design-facing projections** (R1). |
| D2 | Current-state story and gates | Hashes, counts, navigation and diagrams: **CONFIRMED FIXED**. Closure, checksums and acceptance matrix: **DEFECT REMAINS** (R2). |
| D3 | Navigation labels everywhere | **CONFIRMED FIXED** |
| D4 | Arabic part-B limitations | Connectives and the 5 parity records: **CONFIRMED FIXED**. Restatement and editorial quality: **DEFECT REMAINS** (R7). |
| D5 | Bilingual labels on SIGNATURE/CORE printed values | printed_fields: **CONFIRMED FIXED**. In-frame text and encoding-only fields: **DEFECT REMAINS** (R5). Arabic label quality: see R6. |
| D6 | VIS-MFI-DIVERGENCE | **CONFIRMED FIXED** |
| D7 | Rendering overstatement | TRANSMISSION and CAPITAL summaries: **CONFIRMED FIXED**. Record method/measure fields and the other text-first visuals: **DEFECT REMAINS** (R3). |
| D8 | CLM-007 reported history | **CONFIRMED FIXED** |
| D9 | Arabic grammar labels | The listed items: **CONFIRMED FIXED**. "Micro" dropped elsewhere: **DEFECT REMAINS** (R9). New label problem: N5. |
| D10 | Home eyebrow/heading repeat | **CONFIRMED FIXED** |
| D11 | Arrow direction | **CONFIRMED FIXED** |
| D12 | Repetition and overstated copy | /payments/, /data/, CWR-001 and the /evidence/ lead: **CONFIRMED FIXED**. /remittances/ "The chart": **DEFECT REMAINS** (R4). |
| D13 | Handoff doc conflicts | **CONFIRMED FIXED** |
| D14 | Arabic copy items | The listed strings: **CONFIRMED FIXED**. The number-agreement class persists: **DEFECT REMAINS** (R8). |
| D16 | 09 as index; derived reading_sections | **CONFIRMED FIXED**, with one minor caveat (R10). |
| New | Regressions and other findings | **NEW DEFECTS** N1–N6 |

### What was confirmed

**D1**
- "CCY", "Cash Consortium of Yemen" and «ائتلاف النقد» appear in 0 public HTML pages and 0 times in `dist/static-data/search_index.json` and `search_aliases.json`.
- "7.4" appears 0 times on `/{en,ar}/evidence/CLM-044/` and `/{en,ar}/readings/same-year-different-number/`, and the Compare payload carries no value either.
- The Reading path status in both languages now reads: "Every figure… traces… to a named source. Where a record also rests on material with no public original locator, that material is not listed and no figure from it is shown."
- CLM-044's verification text says "no source is listed or linked here". The "listed on this page" wording is gone.

**D3**
- Every anchor to `/readings/`, `/data/`, `/methodology/` and `/measurement/` across 288 pages uses:
  - EN: "Evidence Readings", "Data & sources", "Methodology", "Measurement Agenda";
  - AR: «قراءات الأدلة», «البيانات والمصادر», «المنهجية», «أجندة القياس».
- The group label is "Method & Measurement" / «المنهج والقياس».
- The footer lists Methodology before Measurement Agenda.
- The breadcrumb reads "Evidence Readings /…" (EN) and «قراءات الأدلة /…» (AR).
- The stale variants ("Sources & data", "Data & Sources", «المصادر والبيانات» as a label, "Method and measurement") occur 0 times. The only remaining «المصادر والبيانات» is inside the /rights/ page title «حقوق المصادر والبيانات», which is acceptable.

**D4**
- 38 records carry part B in both languages. No Arabic B begins with و, ف or كما.
- Parity checks pass for all five named records:
  - CLM-018: reliability, adoption and transaction coverage are present in both languages.
  - CLM-029 and CLM-030: '..' and the conditional denominators are present in both languages.
  - CLM-037: aligned.
  - CLM-051: aligned.

**D6**
- Each value has a unique id `row#lane` and a unit with a bilingual label.
- NOMINAL is on all three portfolio values.
- BREAK_UNIVERSE is on all three 2023 values.
- The 2015 portfolio value is REPORTED with a DISAGREEMENT marker.

**D8**
- CLM-007 now reads "Reported history 2018–2024 (staff calculations)" and «قيم تاريخية».
- Its currentness names 2024 as the latest reported value and says the estimate and projections are not observations.

**D10**
- The Home section eyebrow is "What we still do not know" and the heading is now "The gaps the evidence cannot yet close" / «فجوات لا تستطيع الأدلة سدّها بعد».

**D11**
- There is no "→" on any Arabic page and no "←" on any English page.
- In the RTL trace, the Arabic record reads `CLM-001 ← SRC`.

**D12**
- /payments/ shows the July 2025 high of 27,187 in both languages, and contains no "chart" or «الرسوم».
- /data/ promises no facets it lacks. On downloads it says honestly that "no source file for download".

**D13**
- No handoff document has duplicate section numbers. Section 8C was renumbered.
- The same IBM Plex default-with-rationale rule appears in the design prompt §6, MASTER_IMPLEMENTATION_PROMPT, README_FIRST and the manifest.
- There is no "ready for" in README_FIRST and no reference to `98_TEMPORARY` in the checklist.

**D16**
- 09_READING_SECTIONS has empty copy cells on all 90 rows and empty titles on orders 2–9.
- `reading_sections.json` equals 08 (thesis) and 03 (heading and body) on 90/90 rows, in both languages.

**D2 (fixed parts)**
- README, the checkpoint, `YFI_CURRENT_PROJECT_CONTEXT.json`, `IMPLEMENTATION_MANIFEST.json` and `navigation_interaction.json` all carry the actual hashes.
- Every count equals `public_inventory.json`: 143 / 110 / 60 / 55 / 10 / 10 / 11 / 36 / 159 / 150 / 26 / 24 / 423.
- The page families sum to 143. Evidence Record has 110 routes, and Measurement is `PRIMARY_CHILD`.
- The SVGs and the regenerated PNGs show the current navigation and counts.

## Remaining defects

**R1 — MATERIAL (D1 residual). The withheld producer and value survive in Design-facing projections that have a public route.**
- File: `site-src/content/evidence/evidence_passports.json[41]` (from Master `34_EVIDENCE_PASSPORTS`).
- `EP-CCY-REMIT-RESIDUAL-MODEL-K04` carries:
  - object: "CCY at-least-USD7.4bn 2024 remittance residual estimate";
  - publisher: "Cash Consortium of Yemen / Crisis Analysis";
  - method: "User-provided report";
  - route: `/remittances/`;
  - display requirement: "expose equation, assumptions and sensitivity".
- Sheet 34 has no publication-state column.
- The handoff tells Design and Code to ship the passports and let users inspect them:
  - `STATIC_RUNTIME_AND_API_CONTRACT.md` L11: "…passports used by the site";
  - `CLAUDE_DESIGN_MASTER_PROMPT.md` §8C / L402: "evidence passport".
- Validator S04.3 scans only HTML and the search payload.
- In addition, `page_specs.json` (CLM-044) `source_reference_closure` says `lineage_state BOUND_EXACT`, with `direct_source_ids ["SRC-CCY-REMIT-ESTIMATE-2025"]` and `public_routes ["/remittances/","/evidence/compare/"]`. This conflicts with `evidence_objects.json` (`public_routes []`) and with the governed BOUND_UNLISTED text. Acceptance row 4 counts CLM-044 among 92 BOUND_EXACT.
- Consequence: a Design build that follows the handoff could republish the figure and the producer on /remittances/.

**R2 — MATERIAL (D2 residual). The current-state story still contradicts itself.**
1. The P4 closure is missing.
   - `audit/P4_CANONICAL_HANDOFF_ALIGNMENT.md` does not exist.
   - README, checkpoint §2–§4 and acceptance rows 12, 13, 14, 15 and 18 all cite it.
2. `SHA256SUMS.txt` is stale.
   - It is dated 00:22, and `sha256sum -c` fails for 57 of 156 entries. The failures include the Master, README, AUTHORITY, Context, manifest, build.py and validate.py.
   - Checkpoint §6 tells the reader to run this command, and acceptance row 18 is marked PASS on "checksum manifest verified".
3. Acceptance row 15 is FAIL, yet the checkpoint says "No caches" and "MATURATION COMPLETE".
   - `audit/PRE_TRANCHE_C_ACCEPTANCE_MATRIX.csv` (04:45) records row 15 as **FAIL** ("21 cache paths").
   - No cache exists now, so the matrix was not re-run after the clean-up.

**R3 — MATERIAL (D7 class). Public records and cards still describe drawings that the tiering says will not exist.**
- VIS-CAPITAL-CONTEXT (RETIRE_FROM_DESIGN), `/en/evidence/VIS-CAPITAL-CONTEXT/`:
  - "What does it measure? A visual summary of the evidence";
  - "How was it produced? Relationship graph with flow-class and state badges".
- VIS-INCLUSION-TRANSMISSION: the record's method is "Ordered list of documented relationships grouped by system layer; each item names its relationship type…". That list does not exist on `/` or on the record.
  - The AR universe on Home and the record ends «…التي تغطيها الأدلة المرتبطة بالشكل» ("…linked to the figure"). The EN has no such phrase.
- TABLE_TEXT_FIRST visuals are still written as drawn:
  - on `/evidence/`: VIS-EVIDENCE-FRESHNESS ("The visual places…", method "Skyline/dot bands") and VIS-MECHANISM-METRIC-BRIDGE ("The visual starts…", "Edges labeled…");
  - on `/measurement/`: VIS-EVIDENCE-GAPS ("The visual groups…", "Matrix/timeline");
  - VIS-FIRM-FINANCE-SEVERITY (method "Stacked bar…");
  - VIS-OECD-FCP-TIMELINE ("The timeline separates…").
- Fix Master-first in 06 method and 11 alt text.

**R4 — EDITORIAL (D12 residual).**
- `/en/remittances/` reads "The chart breaks the line where the source document changes…". The AR reads «وينقطع الخط في الرسم».
- No chart is drawn: the page has 0 `<svg>` or `<canvas>`. This is the same defect that was fixed on /payments/.

**R5 — MATERIAL (D5 residual). Some required in-frame text has no governed bilingual copy.**
- VIS-PAYMENT-ANATOMY:
  - the contract requires "each card… what the object counts and what it is not", with a fallback column "what it is not";
  - no per-object text exists in either language;
  - the values carry only an English `caveat`.
- VIS-REMITTANCE-COST: the annotation requires the quoted English sentence "'average of quotes for this amount, not the cost of all remittances' in frame". It has no UI-VIS id and no Arabic.
- `display_label_rule` refers to "fields listed as encoding_only", but `visual_design_contracts.json` carries no `encoding_only_fields`. They exist only in the controlled input.
  - As a result, RV-CWR-004 and RV-CWR-009 records expose unlabelled `class` enums (NETWORK_RULE, YPCC…).
  - Design cannot tell that these are not printed.

**R6 — Arabic label quality in the visual contracts, judged as a senior Arab economic editor.**
- **MATERIAL:**
  - `UI-VIS-CAT-PRV-LIMIT-EWALLETS` reads «…ولا تزال القائمة الحالية المسماة للمحافظ… مفتوحة». «مفتوحة» reads as "the list is open", for example to applicants, and is a calque of "remains open". Use «ولا تتوافر بعد قائمة حالية بأسماء المحافظ ومقدمي خدمات الدفع المرخصين».
  - `UI-VIS-STATE-REPORTED` reads "Reported by the source (official statistics)" / «وارد في المصدر (إحصاءات رسمية)». See N5.
- **EDITORIAL:**
  - `PRV-STATUS-NAMED-UNLICENSED` «مسمّى غير مرخص في تاريخ المصدر»: ungrammatical. Use «ورد اسمه بوصفه غير مرخص في تاريخ المصدر».
  - `PRV-STATUS-PROHIBITED` «يُحظر التعامل»: the present tense asserts a current ban. Use «حظر التعامل — غير مرخص في تاريخ المصدر».
  - `PRV-COUNT-CURRENT-LIST` "current official list" / «القائمة الرسمية الحالية»: an undated "current" inside a detached frame. Name the list date instead.
  - `UI-VIS-UNIT-YER-MILLION` «مليون ريال يمني (اسمية)»: an agreement error. Use «(بالقيمة الاسمية)».
  - `PRV-LIMIT-MFI` «مجموعة وطنية مكتملة» and `PRV-NAMED-PARTIAL` «المجموعة الخاضعة للتنظيم»: «المجموعة» is a calque for "universe".
  - `PRV-EVENTS-WALLETS` «للوضع الترخيصي»: use «لحالة الترخيص».
  - `UI-VIS-NOMINAL` «لم تُعدَّل وفق الأسعار»: use «لأثر التضخم».
  - `EVT-NETWORK-COMPANY`: has no subject (restructuring of what?) in either language.

**R7 — EDITORIAL (D4 residual).**
- Part B still restates part A instead of giving a limit of the measure:
  - CLM-016: B-EN "Historical predecessor only. Not 2026 membership, current operation, branch footprint…"; B-AR opens with «إنه»;
  - CLM-051 and CLM-012;
  - CLM-008 and CLM-050 in part.
- Arabic:
  - CLM-037 B-AR «يتبع المساران مسارين متطابقين تقريبًا» is tautological;
  - one EN sentence, "Reconstruction production is verified" (itself unclear English), is rendered «إنتاج إعادة البناء» in CLM-036 but «حدث إعادة البناء» in CLM-040;
  - CLM-051 A-AR «الاستدامة» ≠ "durable inclusion".
- English:
  - CLM-033 and CLM-038 B-EN lack a final full stop;
  - CLM-045 B-EN "Evidence is meaningful through several intermediate links" is unclear.

**R8 — EDITORIAL (D14 class).**
- «مليار/مليارات» after decimals is still inconsistent, within single sentences:
  - «6.245 مليارات دولار… 3.42 مليار دولار» (CLM-032, CWR-001);
  - «7.117 مليارات… 3.614 مليارات» (/remittances/);
  - «6.741 مليارات ريال» against «1.262 مليار» and «33.379 مليار».
- Only the withheld 7.4 figure was fixed, not the class.

**R9 — MATERIAL (D9 residual; "micro" dropped).**
- The Measurement P0 priority on `/ar/measurement/` and `/ar/firms/` translates:
  - "Representative firm/MSME survey" as «مسح ممثل للمنشآت الصغيرة والمتوسطة»;
  - "MSME finance baseline" as «…تمويل المنشآت الصغيرة والمتوسطة».
- Three Arabic terms for "micro" are in use: «الصغرى», «متناهية الصغر» and «الأصغر».

**R10 — EDITORIAL (D16 caveat).**
- 09 still holds 20 section-1 title cells ("What the evidence supports" / «ما الذي تسنده الأدلة») that are never rendered.
- The page uses "Bounded thesis" / «الخلاصة المقيدة بالأدلة», which is hard-coded in `build.py` L1423.
- Checkpoint §2 calls 09 "a pure section index".

## New defects (possibly regressions)

- **N1 — EDITORIAL. Section numbering starts at "02" on 24 pages.**
  - Pages: about, accessibility, contact, corrections, data, compare, explore, measurement, methodology, privacy, rights and terms, in both EN and AR.
  - Cause: `build.py sections()` skips the heading-less first section, which becomes the hero lead, but keeps `i+1`.
- **N2 — EDITORIAL (accessibility).** An empty `<h2></h2>` appears in section 06 of `/en/terms/` and `/ar/terms/`. A heading-less non-first section is rendered with an empty heading.
- **N3 — EDITORIAL (from the D7 text-first rewrite).** Home repeats the system enumeration in two adjacent sections, in both languages:
  - the enumeration: "people and capability, firms and income, providers, payment rails, remittance and capital flows, regulation and consumer protection, and enabling constraints";
  - the follow-on: "context, dependency or plausible mechanisms… not causal arrows / composite score";
  - the two sections: "System context" and the TRANSMISSION text alternative.
- **N4 — EDITORIAL (information architecture; blurs Evidence ≠ Sources).**
  - The `/evidence/` H1 "Inspect the evidence behind the answer" is immediately followed by the H2 "Find the evidence behind the answer". The adjacency became visible after the lead was removed.
  - The `/data/` H1 is "Find the evidence behind the answers…". In Arabic, the `/data/` H1 is the same as the `/evidence/` H2: «اعثر على الدليل وراء الإجابة».
  - The `/ar/data/` H2 «ماذا يتضمن دليل البيانات؟» uses «دليل» ("evidence") to mean "catalogue".
- **N5 — MATERIAL (semantic firewall).** The REPORTED state is labelled "(official statistics)" in both languages, but it is applied to:
  - the IMF staff-report "staff calculations" in VIS-REMITTANCE-MACRO;
  - SFD newsletter figures in VIS-MFI-DIVERGENCE.

  IMF staff calculations and a programme agency's reports are not official national statistics. Drop the parenthetical or split the state.
- **N6 — EDITORIAL (low).** On `/ar/readings/microfinance-structural-divergence/`, the governed 08 `prohibited_inference_ar` no longer appears, because the note-dropping decision is made on the English text (`build.py` L1425).
  - Section 04 carries the same meaning in a different Arabic wording, so nothing is lost.
  - It does mean the Master holds two Arabic formulations of one governed sentence.

## Minor observations (not counted)

- The CLM-044 AR page uses three renderings of "canonical baseline" («الحاكم» / «المرجعي» / «المعتمد») and both «التحويلات» and «الحوالات».
- The CLM-044 AR universe adds "not an official observed value", which the EN lacks.
- 133 of 159 sources have no `display_title` and render as raw IDs, e.g. `SRC-IMF-D4D-YEM-ESS-2025` in the CWR-001 verify list. This is pre-existing (PID-1).
- The Home H2 differs in meaning between languages: EN "Three signals. Three different evidence states." against AR «إشارات من أوقات مختلفة — وليست رقمًا واحدًا».
- `/ar/methodology/` H2 «ابدأ بما الذي يجري قياسه» is ungrammatical.
