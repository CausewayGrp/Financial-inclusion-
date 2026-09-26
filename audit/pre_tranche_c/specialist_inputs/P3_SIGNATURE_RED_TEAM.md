# Signature visuals: red team (K, with E and H lenses)

Read-only; no authority; Team Lead decides. Personas without a material attack are omitted.

## Verdicts

| Candidate | Verdict | Decisive reason |
|---|---|---|
| RV-CWR-001 | **KEEP SIGNATURE** | Heads off the likeliest false headline ("remittances fell 45%"); drawable. |
| VIS-PROVIDER-OBSERVABILITY | **KEEP SIGNATURE** (conditional) | "Whose list, what date, what it proves", no score. Condition: issuing authority in frame. |
| RV-CWR-009 | **KEEP SIGNATURE**; propose as **Home signature** | Drawable, vertical, mobile-native; already Home's argument. |
| VIS-EVIDENCE-FRESHNESS | **KEEP SIGNATURE, BLOCKED** | Undrawable: 97 free-text period strings, no structured dates, empty `source_dependencies`. |
| VIS-REMITTANCE-MACRO | **DOWNGRADE → CORE** | Scope not in frame; a crop reads "Yemen remittances US$1.86bn". |
| VIS-FINDEX-GAPS | **DOWNGRADE → CORE** | Truthful standard bars; title and period defects. |
| VIS-POS-TERMINALS / -TRANSACTIONS / -VALUE | **DOWNGRADE → CORE** (one 3-panel small multiple) | Standard lines; the contradiction as headline reads as a gotcha against the source. |
| VIS-PAYMENT-ANATOMY | **CORE, card-first** | Big-number cards invite dashboard reading and division by population. |
| VIS-INCLUSION-TRANSMISSION | **DOWNGRADE → SUPPORTING, text-first** | Undrawable: route-to-route links, 21 of 26 with `evidence_refs: null`, no evidence state; "transmission" implies causality. |

## Cross-cutting findings

- **C1: crop-proof frame.** Inside the frame: a title that states the finding, the unit, the universe including the issuing authority, the period, the publisher and document, one prohibited inference, and any break, missing or contradiction marker. Never a SRC-ID as the credit line.
  - *Blocker:* `publisher` is null for SRC-CBY-POS-\*, SRC-CBY-PAYREPORT-\*, SRC-IMF-AIV-2025-STAFF/SUPP-001 and SRC-WB-FINDEX-AGG-2022. Fix in the Master first.
- **C2: Arabic crops lose scope.** visual_library has no Arabic unit, universe or period fields. The Arabic text alternatives on Home, Providers, People and Payments drop the "Scope and time" line that English shows.
- **C3: bidirectional-text defects.** Arrows are not mirrored in right-to-left text (U+2192 is class ON, mirrored=0).
  - VIS-POS-TERMINALS `what_it_shows_ar` "1,357→1,473" and CLM-010 "7→9→8" render with the arrow pointing against the reading order. Write «من … إلى …».
  - Isolate +11%, US$, YER and IDs with `<bdi>` or LRI; dist/ar has none.
  - Keep Western digits; percentage points are «نقطة مئوية», never "%".
- **C4: one time-axis rule (Lead).** Recommend unmirrored numeric time axes, because bilingual crops circulate side by side and a mirrored rise reads as a fall. Mirror text and legends. Label the first and last year and value directly. Chains run top to bottom in both languages.
- **C5: carriers.** Line style, marker fill and a word carry state. No red-amber-green, and no fading by age (that encodes "old = invalid").

## Per-candidate findings

**RV-CWR-001.**
- *Journalist:* bars 6.245 then 3.42 read as a collapse. Place both at the same x (reference year 2024), keyed by publication.
- *Researcher/IMF:* the 2021=100 panel alone reads "CBY and IMF agree"; print "index, not level" inside it.
- *Source owner:* page copy's "does not establish … manipulation" insinuates. Remove it in the Master.
- *Title:* "baselines" contradicts "no single series is the correct level"; use "values".
- EN: "2024 remittances, one year, two numbers: CBY-Aden's 2024 annual report published US$6.245bn; its 2025 report restated 2024 at about US$3.42bn — a revision, not a fall."
- AR: «حوالات 2024 برقمين: نشر التقرير السنوي 2024 للبنك المركزي – عدن 6.245 مليار دولار، وأعاد تقرير 2025 عرض السنة نفسها عند نحو 3.42 مليار؛ مراجعة إحصائية لا هبوط.»
- Prohibited inference: "Not a year-on-year collapse; no series is the correct level." / «ليست تراجعًا سنويًا، ولا سلسلة تمثل وحدها المستوى الصحيح.»

**VIS-PROVIDER-OBSERVABILITY.**
- *Payment provider and Sana'a-aware regulator:* the CBY-Aden circular of 26 June 2024 names 12 wallets. A cropped "negative authority: 12" cell becomes "illegal wallets"; status depends on the issuing authority.
- *MFI/MFB:* the 26 listed banks include 12 microfinance banks; keep non-bank MFIs separate.
- *Exchange provider:* date every (reversible) 2026 suspension cell.
- *Wallet count:* sources give 7, 8, 9 and >9; the cell reads "counts disagree".
- *Form:* class level, no entity names; words, not filled dots (a hidden score); one card per class on mobile.
- EN: "What CBY-Aden lists and decisions (2024–2026) establish about each provider class: a dated formal status, not operation."
- AR: «ما تثبته قوائم البنك المركزي – عدن وقراراته (2024–2026) عن كل فئة من مقدمي الخدمات: وضع رسمي مؤرخ، لا تشغيل فعلي.»
- Prohibited inference: "CBY-Aden status only: absence is not unlicensed elsewhere; listing is not operation." / «وضعٌ وفق البنك المركزي – عدن وحده: عدم الإدراج لا يعني عدم الترخيص لدى جهة أخرى، والإدراج لا يثبت التشغيل.»

**RV-CWR-009.**
- *Donor/CBY:* filled versus open nodes read as a progress bar. No percentage and no gradient; open means "not measured" (SL-015).
- *Payment provider:* "transactions are use". The thesis cites "activity", but the chain has no activity node; the Lead places it before drawing.
- *Researcher:* mixing FPS, POS and wallet evidence fabricates one reform's progress. One row per rail, with dated nodes.
- EN: "From rail to result: evidence reaches rules, implementation and activity; access, use, quality and outcome remain unmeasured."
- AR: «من البنية إلى النتيجة: تصل الأدلة إلى القواعد والتنفيذ والنشاط، وتبقى حلقات الوصول والاستخدام والجودة والنتيجة بلا قياس.»
- Prohibited inference: "Missing downstream evidence does not mean the reform failed." / «غياب الدليل على الحلقات اللاحقة لا يعني أن الإصلاح فشل.»

**VIS-EVIDENCE-FRESHNESS.**
- *Journalist:* a skyline by domain works as a ranking, and "gap" badges are gap indicators.
- *Researcher:* the Findex period appears three different ways.
- *Form:* a dot strip per domain; marker shape shows evidence class, fill versus outline shows observation versus publication.
- EN: "Evidence dates differ by domain and class: 'latest' means latest for that measure, not for Yemen as a whole."
- AR: «تتفاوت تواريخ الأدلة بحسب المجال ونوع الدليل: "الأحدث" يعني الأحدث لذلك المقياس، لا لليمن كله.»
- Prohibited inference: the governed EN/AR text, unchanged.

**VIS-REMITTANCE-MACRO.**
- *Journalist/humanitarian:* CLM-036/042 place the series in an "IRG analytical" scope, and CWR-001 cites a 33% population share the IMF used for Aden-administered areas. Yet the universe and geography say "Yemen", beside CBY's US$3.42–6.245bn and CCY's ≥US$7.4bn. Adjudicate the scope in the Master.
- *IMF:* near-constant 5.6–6.0%/yr growth 2018–24; label "staff calculations".
- *Currentness:* "bounded to 2018–2030" treats projections as current.
- *Carriers:* solid line and filled dots for reported values; one hollow dot for the estimate; dashed line and hollow dots for projections; a labelled gap reading "document changes".
- EN: "IMF staff figures: reported history 2018–2024 (US$1,861.7m in 2024); the 2025 estimate and 2026–2030 projections come from a later, separate supplement."
- AR: «أرقام خبراء صندوق النقد: تاريخ مبلغ عنه 2018–2024 (1,861.7 مليون دولار في 2024)، أما تقدير 2025 وتوقعات 2026–2030 فمن ملحق لاحق مستقل.»
- Prohibited inference: "Estimates and projections are not observations; not informal hawala volume." / «التقديرات والتوقعات ليست مشاهدات، ولا تقيس السلسلة الحوالات غير الرسمية.»

**VIS-FINDEX-GAPS.**
- *Citizen:* "Who is being left behind?" is present tense on 2022–23 fieldwork.
- *Arabic editor:* «من تبقى خارج الوصول؟» turns ownership into access.
- *Period field:* "2022 observation" contradicts CLM-001 (fieldwork 7 Nov 2022 – 9 Jan 2023).
- *Researcher:* two-decimal gaps with no interval suggest false precision. The 6.98% figure has no comparator, so it gets no bracket. Findex 2025 has no Yemen observation; say so in the frame.
- EN: "Account ownership, ages 15+, Findex 2021 wave (Yemen fieldwork Nov 2022–Jan 2023): 11.9%; women 5.44%, men 18.35%. No newer Yemen observation."
- AR: «امتلاك الحساب لمن بلغوا 15 عامًا فأكثر، موجة Findex 2021 (ميدانيًا في اليمن: نوفمبر 2022 – يناير 2023): 11.9%؛ 5.44% للنساء و18.35% للرجال، ولا مشاهدة أحدث لليمن.»
- Prohibited inference: "The survey frame excludes areas holding about 23% of the population; not a 2026 rate, not a map." / «يستبعد الإطار مناطق تضم نحو 23% من السكان؛ ليست معدلًا لعام 2026 ولا خريطة.»

**POS trio.**
- *Sana'a-aware reader:* the geography code is GEO-YEM-NAT on a CBY-Aden scope with a null publisher, so a crop reads "Yemen: 1,473 POS".
- *Specialist E:* YER has no currency-zone field. The governed chronology shows the IRG-market rial moving about 2,900→1,600 per US$ in mid-2025, inside this window. The nominal line reads as real growth. Label it "nominal, unadjusted" and do not annotate the exchange-rate event.
- *Researcher:* "8,015 to 24,026" hides a July 2025 peak (27,187).
- *Source owner:* the +11%/≈8.55% annotation as headline is a gotcha, and June's +7.6%/≈7.91% is left unannotated. Use a dagger note.
- *Titles:* "Footprint/Usage Pulse" imply reach and people; use "Reported POS terminals/transactions".
- EN: "POS reported to CBY-Aden, Mar 2025–Jan 2026: terminals 561 to 1,473; transactions 8,015 to 24,026; nominal value YER 320m to YER 1.262bn (Sep 2025 missing)."
- AR: «نقاط البيع وفق البنك المركزي – عدن (مارس 2025 – يناير 2026): الأجهزة من 561 إلى 1,473، والمعاملات من 8,015 إلى 24,026، والقيمة الاسمية من 320 مليون إلى 1.262 مليار ريال، وقيمة سبتمبر 2025 غائبة.»
- Prohibited inference: "Devices and transactions are not people or merchants; nominal value is not real growth." / «الأجهزة والمعاملات ليست أشخاصًا ولا تجارًا، والقيمة الاسمية ليست نموًا حقيقيًا.»

**VIS-PAYMENT-ANATOMY.**
- Each card carries its "is not" line; no totals row.
- EN: "H1 2025 payment counts reported to CBY-Aden measure cards, accounts, subscribers, transactions and terminals — not people."
- AR: «أرقام المدفوعات للنصف الأول 2025 لدى البنك المركزي – عدن تقيس بطاقات وحسابات ومشتركين ومعاملات وأجهزة، لا أشخاصًا.»
- Prohibited inference: "No digital-inclusion score; no division by population." / «لا درجة شمول رقمي، ولا قسمة على السكان.»

**VIS-INCLUSION-TRANSMISSION.**
- A Home diagram reads as CauseWay's authoritative model, and the directed from/to pairs become arrows.
- A single "regulation" node erases the two central-bank authorities that have existed since 2016.
- *Arabic:* «منظومة انتقال» is weak; «يستخدم خريطة هادئة» leaks design-brief language.
- At 360px, use an ordered list.
