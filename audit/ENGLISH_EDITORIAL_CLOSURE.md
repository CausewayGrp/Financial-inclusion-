# English editorial closure

**Status:** `VERIFIED_BY_CLAUDE_TEAM` · `SPEC_PENDING_EXECUTION` · `INDEPENDENT_OPENAI_ACCEPTANCE_REQUIRED`

## 1. Standard

The English should read as the work of a senior research editor:
- precise and economical;
- analytically mature;
- clear about scope and uncertainty;
- free of consultancy filler, template cadence and repository vocabulary.

It is co-authoritative with the Arabic. Where the Arabic carried a limit that the English lacked, the English was brought up to it (see `BILINGUAL_EDITORIAL_CLOSURE.md`).

## 2. Self-referent rule (PB-0415)

**Rule.** "The system", "the product" and "in the system" are not used for this resource.
- Grammatical subject: "This resource" / "this resource".
- Locative: "available here" / "here".
- "The system's evidence" → "The evidence here".
- "The system" is kept only for the financial system; "the product" only for a financial product.

**Why.** The /about/ page itself uses "the system" for the financial system ("The system the evidence is trying to describe"). Using the same word for the resource makes sentences such as "The system does not plot 7→9→8…" ambiguous.

**Execution.** 122 substitutions by per-cell rows. 11 financial-system or financial-product uses are kept, listed in `TERMINOLOGY_SWEEP_KEEP_REGISTER.csv`:
- "The system the evidence is trying to describe";
- "the system link";
- "freezing the system at";
- "matter to the system";
- "Do not call the system effective";
- "launched the product";
- "parts of the system are current".

**Flagship sentence.** "The latest representative measure in the system reports 11.9%…" becomes "The latest representative survey measure reports 11.9%…" (PB-0306/0307, 7–8 cells).

## 3. Instruction voice → reader prose

Design instructions had been stored in reader-facing fields, so they reached the public site.

| Where | Before (example) | After (example) | Rows |
|---|---|---|---|
| /finance/ chronology | "Use the documented system chronology as contextual navigation…" | removed (authoring text) | PB-0150/0151 |
| /measurement/ list | "Present them as filterable or expandable items rather than one long paragraph. Each item should expose…" | "Each item sets out the current evidence anchor, …"; the display rule moves to a non-public design note | PB-0514–0516 |
| Reading visuals, `what_it_shows_en` ×10 and `accessible_summary_en` ×9 | "Show the same 2022 banking positions as published across vintages…" | "The visual compares the same 2022 banking positions as they appear in different publication vintages… a same-year restatement does not show a boom in credit, deposits or assets, or a change in solvency." | PB-0430–0448 |
| 13 ungoverned VISUAL records, `summary_en` (renders on /evidence/VIS-*/) | "Show valid n, sysmiss/invalid n, conditional-universe note and a permanent banner…" | "The number of valid and of missing or invalid cases for each question… not a population estimate." | PB-0500–0512 |
| 12 core visuals, `what_it_shows_en` (not rendered today) | "Plot evidence vintage by domain/evidence class… The visual should make vintage asymmetry impossible to miss." | "Evidence vintage by domain and evidence class, with badges… so that differences in currentness are plain." | PB-0458–0469 |
| Evidence-record "How can I verify it?" (107 records) | "Show the definition… rather than inferring or inventing it." | per-record path from bound sources (UI-VERIFY-BOUND / COMPOSITE / UNBOUND) | PB-0007/0008 |

**Accessible summaries.** An accessible summary is what a screen-reader user, or someone who meets a cropped screenshot, receives *instead of* the chart. It must describe the chart and carry its limit. A drawing instruction does neither.

## 4. Backend vocabulary

| Before | After | Rows |
|---|---|---|
| "The system controls a 26-row current CBY-Aden licensed-bank source list" | "The current CBY-Aden list of licensed banks names 26 banks." | PB-0200 |
| "January 2026 is the latest monthly POS object exposed on the reviewed CBY page" | "January 2026 is the latest monthly POS release on the CBY-Aden page reviewed" | PB-0580–0582 |
| "Within the report-specific finance-filtered base," / "…finance-relevant filtered denominator," / "In the report-specific group used for the finance-severity question," | "Among the firms in the report's finance-obstacle tabulation, which excludes firms that said they did not need a loan," — Arabic twins aligned (PB-0583A–D) | PB-0583/0584 |
| "Official CBY objects report…"; "the primary 2023 SFD/SMED object" | "Official CBY-Aden publications report…"; "the primary 2023 SFD/SMED source document" | PB-0585–0588, PB-0120 |
| "generated from the stable MA-001…MA-010 measurement objects" | "built from the ten measurement items MA-001 to MA-010" | PB-0589 |
| "bounded directional signals" | "separate bounded anchors" | PB-0145 and variants |
| "USD 3.42216 billion" | "about US$3.42 billion" | PB-0313–0315 |

"Measurement object" is **kept** where it means the thing being measured. It is the method's own defined term (/methodology/: "Start with the object being measured"). It is replaced only where it means a document, a release or a record.

## 5. Precision and causal discipline

- **Precision.** A derived value carries the precision of its inputs: 15.5 − 6.5 = **9.0**, never 9.00. A six-significant-figure balance-of-payments estimate is rounded to 3 s.f. with "about".
- **Levels before differences.** "5.44% of women and 18.35% of men have an account, a difference of 12.91 percentage points." The ratio is not foregrounded.
- **No manufactured precision.** No confidence interval, p-value or standard error is stated, because the evidence base holds none. The limitation is said plainly: about 23% of the population lives in excluded areas, and more than a quarter of PSUs were replaced (PB-0311/0312).
- **Causal discipline.** Chronology is described as sequence, never as cause. "Points to a divergence" / "structural divergence" (CWR-006, CLM-054) becomes "separate bounded anchors". The Tranche A "ranks 6th" is withdrawn.
- **Filler sweep.** No generic consultancy filler ("leverage", "robust ecosystem", "key insights", "unlock value") was found in governed public copy. The recurring risk was repository voice (§2–4), not filler.

## 6. Headlines and titles

- **Titles that carry a thesis must carry its date when the evidence is historical:**
  - "In 2014, borrowing was widespread — but its sources are not slices of one pie" (PB-0572);
  - "Domestic remittances in 2014 — …" (PB-0573);
  - "Microfinance in 2014 — two comparable quarters, not a long trend" (PB-0574).
- **Headings name the evidence state, not an upgraded one:** "Reported history, estimates and projections are different evidence states" (PB-0188).
- **Nav label:** "Readings" becomes "Evidence Readings", and "Data" becomes "Data & sources" (PB-0420/0421).
