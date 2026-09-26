# Independent verification — P2/P3/P4 claims (hostile-but-fair)

This report is read-only and carries no authority. Repository state is as of about 03:38–03:52 EEST on 2026-09-26. README.md and validate.py were modified at 03:35 by the parallel P4 work. Master `904630fe…` and Page Specs `a5cea97a…` match README.md, the Context and the manifest.

## Verdicts

| # | Area | Verdict |
|---|---|---|
| 1 | Check scripts | **CONFIRMED.** `--check`: PASS, 40 outputs, 0 differences. Unit tests: 20/20. Build: 288 HTML from 143 specs. Literal audit: 8,296 records, 0 unresolved (it rewrites `audit/PUBLIC_LITERAL_CLOSURE.json`). Validator: `ERRORS=0 WARN=0`. Browser tests: 26/26, but the "+" compare test passes by SKIP. |
| 2 | Stale facts | **DEFECT FOUND** (D2, D3) |
| 3 | Public pages (24+ sampled) | **DEFECT FOUND.** The P4.3 rendering is confirmed: the A label shows on all 110 records; the B label shows on exactly the 38 records that have one, in both languages; no `' \| '` or template token appears; no right-pointing arrow sits between numbers in Arabic; 13,009 internal links, 0 broken. |
| 4 | Visual contracts | **DEFECT FOUND** (D5, D6). All 36 visuals are tiered 3/12/12/8/1. All 98 S/C values equal their raw rows; I hand-checked 11 contracts, including both withheld POS/accounts values, and the objects (26 banks; 98/225/106; 817/1,021). Gaps 12.91 and 9.0 are correct. The 33 grammar labels and the S/C captions exist in EN and AR. Both blockers are stated honestly. |
| 5 | Arabic quality | **DEFECT FOUND** (D4, D9, D14) |
| 6 | Reading ownership | **CONFIRMED with caveat** (D16). `reading_sections.json` equals the owners on all 90 rows, both languages. |
| 7 | Other | **DEFECT FOUND** (D1, D7, D8) |

## Defects

**D1 — MATERIAL (possibly a release BLOCKER). A source with no public locator and unassessed rights is named, and its figure is published.**
- `SRC-CCY-REMIT-ESTIMATE-2025` is `USER_PROVIDED_FILE`, `rights_state NOT_ASSESSED`.
- `/{en,ar}/evidence/CLM-044/` and `/{en,ar}/readings/same-year-different-number/` print "CCY estimates at least USD 7.4 billion", "CCY (Cash Consortium of Yemen)" and «ائتلاف النقد في اليمن (CCY)».
- This contradicts FINDINGS_LEDGER P1-L02 ("Lead rejected naming locator-less sources"), HANDOFF_ACCEPTANCE_CHECKLIST L25, and CLM-044's own text ("only where the rights permit").
- CLM-044 is the only CLM record excluded from the 60 claims in 07, yet it keeps a public route.
- Its method field reads "User-provided report" / «تقرير قدمه المستخدم».
- The Reading says "Every figure in this Reading traces… to a named source". That is false for CLM-044, whose row says "Also draws on…" with nothing else listed.

**D2 — MATERIAL. Current-state facts are stale, and the gates cannot catch them.**
- `OPENAI_REENTRY_CHECKPOINT.md`. README.md calls it current, and the HISTORICAL_LINEAGE docs point to it.
  - L14: "P4 in progress".
  - L19: Master `49cbfe33…`. L20: Page Specs `8c142f2e…`.
  - L25: 8,230 records. L29: "18 of 18".
- `navigation_interaction.json`:
  - L269: Evidence Record `route_count: 108`; families sum to 141, not 143;
  - Measurement is `CONTEXTUAL_FOOTER`, although it is now in primary navigation.
- `design/architecture/*.svg` (manifest L725–728):
  - the site map shows the global shell "Explore · Evidence · Readings · Data · Methodology · About", "141 controlled Page Specs" and "Evidence Records ×108";
  - the family map shows "108 routes" and "158 public locators";
  - the architecture diagram shows "Page Specs ×141".
- README.md and the Context say "P1–P4 CLOSED", but:
  - the P4 closure is absent;
  - the acceptance matrix has row 9 `NOT_RUN`, rows 7 and 17 "browser not run" yet PASS, and VIS-PAYMENT-RAILS listed twice in row 4;
  - `sha256sum -c SHA256SUMS.txt` fails for 20+ files.
- Gate coverage:
  - P4-G01 only matches English prose in README.md, the checkpoint and `handoff/*.md`.
  - P4-G03 compares only the English top-level primary labels. It does not check Arabic, children, the trust layer, breadcrumbs, the footer, hashes, JSON or SVG.

**D3 — EDITORIAL (systemic; the brief requires propagation). Labels do not match the navigation.**
- The breadcrumb contract has Reading `parent_label_en "Readings"` against AR «قراءات الأدلة». It renders "Readings" on 10 EN Reading pages.
- The 8 EN domain pages say "Sources & data" and the 8 AR domain pages say «المصادر والبيانات»; the navigation says "Data & sources" / «البيانات والمصادر».
- Home says "Data & Sources".
- The footer says "Method and measurement" and lists Measurement before Methodology.

**D4 — MATERIAL. The P4.3 split is mechanical.**
- 11 of the 38 Arabic B parts start with a dangling connective:
  - CLM-001, 002 and 025: «ويستبعد»;
  - CLM-015: «وهي»; CLM-060: «ولا يوضح»; CLM-007: «فهذا»; CLM-012: «فالقواعد»; CLM-020: «فالتاريخان»;
  - CLM-027, 044 and 059: «كما».
- B repeats A instead of giving a limit of the measure. CLM-008 EN states the limitation twice, and its A-AR lacks the second sentence. The same happens in CLM-055, 015, 020 and 053.
- Meaning differs between EN and AR:
  - CLM-037: B-EN "Method reconstruction is strongly supported" vs «تطابق المسار بعد التطبيع قوي»;
  - CLM-029 and 030: the AR drops "remittance-channel denominators are conditional" and "'..' means no observation";
  - CLM-018: the AR drops reliability, adoption and transaction coverage.
- The parity test checks presence only.

**D5 — MATERIAL. Arabic charts cannot be built without Design authoring labels, which it is forbidden to do.** No category label has an Arabic form:
- FINDEX-GAPS: x = "total", "female", "poorest 40%";
- FIRM-FINANCE-PATH;
- FIRM-CONSTRAINTS;
- REMITTANCE-COST: "Saudi Arabia";
- PAYMENT-ANATOMY: x = `IND-0001`… (labels exist in English only);
- RV-CWR-009: event labels.

Other gaps:
- PROVIDER-OBSERVABILITY cells are raw enums (`LICENCE_SUSPENSION_AND_CLOSURE_EVENT`).
- Governed Arabic present in the raw rows is dropped: FMIIP-RF-004 «نقاط الوصول المالي», and the remittance `metric_label_ar`.
- TARGET-RESULT-STATE has no metric label in either language.

**D6 — MATERIAL. VIS-MFI-DIVERGENCE.**
- The 2015 portfolio value 6741 has `grammar_state: null`.
- None of the 9 values carries a unit.
- The promised BREAK_UNIVERSE and NOMINAL markers are absent from every value, so the detached frame will not carry them.
- The anchors reuse one id for three values.

**D7 — MATERIAL. VIS-INCLUSION-TRANSMISSION (Home).**
- P3 §3 says it "is rendered as the ordered list SL-001…010 and SL-022…026". There are 0 SL items on `/` and 0 on its record.
- The record's method describes that list.
- The summary still says "The map links…" / «يربط المخطط…» for a visual ruled not drawable.
- VIS-CAPITAL-CONTEXT (RETIRE) has the same problem: "The visual separates…".

**D8 — MATERIAL. CLM-007 is not fixed in the way P3-F03 claims.**
- `definition_en` says "separates observed values, estimates and projections" (AR «المرصودة»), but the state is REPORTED.
- `currentness_en` says "Currentness is bounded to reported history 2018–2024…; projection 2026–2030".
- AR «تاريخ مبلغ عنه 2018–2024» reads as "a reported date".

**D9 — MATERIAL. Arabic grammar labels.**
- CHAIN-ACCESS «إتاحة الوصول» is the same string as the trust-navigation label *Accessibility*. Use «الوصول إلى الخدمات المالية».
- CHAIN-OUTCOME «الأثر» means impact. Use «النتيجة».
- RV-CWR-002 «لفترة الإسناد نفسها» should be «للفترة المرجعية».
- RV-CWR-008 «الصغيرة والمتوسطة» drops micro.
- Editorial:
  - REPORTED «مبلغ عنه» is a calque, also used in the POS titles;
  - MISSING «معتمدة» means approved, not verified;
  - NOMINAL «معدلة للأسعار» is a calque;
  - NOT-COMPARABLE is singular;
  - "observed" is «مشاهدة» in one label and «مرصودة» in another.
- «ما لا يثبته» differs from the preferred «ما الذي لا يثبته».
- The new titles for FINDEX-GAPS, RV-CWR-001, RV-CWR-006 and TRANSMISSION are sound.

**D10 — EDITORIAL.** Home repeats the eyebrow as the H2: "What we still do not know", and in Arabic «…نعرفه» / «…نعرفه؟». The P2-G03 regex needs the two to be adjacent, so it misses this.

**D11 — EDITORIAL. Arrows point the wrong way.**
- `build.py` L202 hard-codes "←" on the English "Continue from here" links (13 pages).
- On 95 Arabic records, "CLM → SRC" sits in an RTL flex and points back at the record.

**D12 — EDITORIAL. Repeated or overstated copy.**
- The CWR-001 lead is repeated in section 01; its "Do not infer…" block and scope line each appear twice.
- The `/evidence/` lead is repeated.
- `/payments/`:
  - it says "The charts keep…", but no chart is drawn;
  - AR «الرسوم» reads as "fees";
  - "8,015→24,026" hides the July 2025 high of 27,187 (P3-F04 fixed this only in the visual text).
- `/data/`:
  - it promises search by "period, geography, evidence type", but the filter does not support these;
  - it mentions "Downloads", but none exist.

**D13 — EDITORIAL. Handoff documents conflict.**
- The design prompt has two "## 8A." sections.
- Typography:
  - the design prompt says Plex is "not compulsory";
  - README_FIRST and the manifest make Plex mandatory;
  - MASTER_IMPLEMENTATION_PROMPT contradicts itself (L109 vs L149).
- The README_FIRST body says "ready for product design execution".
- The checklist L10 cites a non-existent `98_TEMPORARY__NONAUTHORITATIVE/`.

**D14 — EDITORIAL. Arabic copy.**
- «ما الذي يوضحه الدليل؟:» appears on 6 pages.
- «تشير… بأن» should be «إلى أن».
- «جغرافيا تمثل» should use «مناطق».
- «7.4 مليار» and «مليارات» are both used.
- Two curated cards (CGAP, OECD-Youth) have English-only Arabic titles.

**D15 — EDITORIAL.**
- The Findex 40%, 60% and primary-education locators lack `?locations=YE`.
- Captions end with a relative "/en/evidence/…" link.
- RV-CWR-004 plots Findex at x=2022, which collapses the fieldwork span.
- 86 of 110 currentness fields use the tautological template.
- The citation copy is hard-coded in `build.py`.

**D16 — EDITORIAL (claim precision). "One owner" is really two copies with an equality guard.**
- Editing an owner (03/08) alone also stops generation.
- Section-1 titles are owned by 09 alone and are never rendered.
- `test_one_reading_truth` mutates one cell. Together with the code, that proves the claim for 09-only edits.
