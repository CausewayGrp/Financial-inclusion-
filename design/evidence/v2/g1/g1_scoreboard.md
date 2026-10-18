# G1 scorecard — 18 October 2026 (round 1: five candidates, three blind judges)

Judges: three AI reviewers (Fable 5.1, high effort), each reading 30 rendered views labelled P–T in random order with no rationale attached; the mapping (judge_mapping.json) was decoded only after all three had reported. Scores are 1–5 per criterion; the table sums the three judges (max 15). Ranks are each judge's overall order (Arabic phone reader · statistician-journalist · IFI data professional).

| Candidate | first screen | boundary | provenance | source path | long text | Arabic | calm tone | simplicity | distinct | Total | Ranks |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A Register | 12 | 11 | 13 | 12 | 12 | 12 | 13 | 14 | 9 | **108** | 2 · 1 · 1 |
| B Argument | 10 | 11 | 13 | 12 | 13 | 10 | 14 | 11 | 12 | **106** | 1 · 4 · 2 |
| C Compact | 15 | 13 | 12 | 9 | 10 | 11 | 12 | 13 | 7 | **102** | 3 · 3 · 3 |
| D Incumbent | 9 | 11 | 12 | 12 | 12 | 10 | 9 | 9 | 9 | **93** | 5 · 5 · 5 |
| E Argument-compact | 12 | 11 | 12 | 11 | 12 | 9 | 12 | 10 | 13 | **102** | 4 · 2 · 4 |

## Measured columns (AR 390 unless stated; D is the incumbent on main 8c78fa0e)

| Candidate | Home screens | first answer (screens) | /payments/ screens | CLM-001 screens | first answer | /data/ screens | AR cold bytes Home | AR cold bytes /data/ | EN cold bytes Home | font files AR |
|---|---|---|---|---|---|---|---|---|---|---|
| A Register | 9 | 1 | 19.7 | 10.2 | 0.9 | 18.6 | 266 KB | 322 KB | 238 KB | 3 |
| B Argument | 9.8 | 1 | 20.3 | 10.4 | 0.9 | 19 | 304 KB | 360 KB | 261 KB | 4 |
| C Compact | 8.1 | 0.7 | 18.1 | 8.8 | 0.7 | 16.6 | 266 KB | 322 KB | 238 KB | 3 |
| D Incumbent | 9.5 | 1.2 | 20.4 | 10.4 | 0.9 | 18.8 | 265 KB | 321 KB | 237 KB | 3 |
| E Argument-compact | 8.7 | 0.8 | 18.6 | 9 | 0.8 | 16.9 | 304 KB | 360 KB | 262 KB | 4 |

Disqualifiers (charter §10.3), every candidate: HTML and app.js byte-identical to dist/ (no governed content changed, no JavaScript added); no governed region at zero height at AR 390 (boundary sections, record units, the edition strip, the page tools, the topics block and the phone index all rendered); no horizontal overflow at 390 or 320-equivalent; the analytical form of every visual unchanged (the SVG and table markup is untouched). Source-owner test (charter §3.5) on the five records in both editions: PASS for every candidate (sourceowner.json — the value, the two clocks, the boundary, the source rows with publisher roles and links, and CauseWay's separate citation block are all present and visible). Byte delta: B and E add one heading file per edition (Markazi Text 600, 37 KB subset; IBM Plex Serif 600, 24 KB Latin-1 subset); AR /data/ reaches 360 KB against the W4F target of 350 KB, which the G2 weight decision (whether the Medium text weight, 74 KB, still earns its file) resolves.

## Round 2 — the pairing question isolated (A against F; labels V and W, decoded after the reports)

F is A's grammar unchanged plus the heading pairing with the two defects the first round named corrected (the Latin inside an Arabic heading set from the same Markazi file through a second `@font-face` scoped by `unicode-range` and reduced with `size-adjust: 84%`; the serif deck never larger than its section heading). Five views each (Home, CLM-001 and /payments/ at AR 390; Home and CLM-001 at EN 1440); five criteria; the same three judges. Mapping: A = V, F = W.

| Candidate | first screen | long text | Arabic | calm tone | distinct | Total | Preferred by |
|---|---|---|---|---|---|---|---|
| A Register (V) | 12 | 12 | **12** | 13 | 9 | **58** | all three judges |
| F Register + pairing (W) | 12 | 12 | 9 | 14 | 12 | 59 | none |

Every judge preferred A and gave the same reason: the Arabic record title (CLM-001 AR 390) reads as a heading imported from the English page once the serif pairing is in it, and the answer sits lower on the phone; F's gain is on the English desktop views. The computed font and a 2× crop of the title (`h1` in Markazi Text 600, loaded with the Arabic unicode range) confirm the serif did render the Arabic; the verdict is therefore about how the pairing reads, not a rendering fault.

## The Arabic heading weight (item 21, 600 against 700)

Blind crops of the specimen (X = 600, Y = 700, decoded after the report), scored by the Arabic phone reader: 600 readability 4 and distinction 4; 700 readability 3 and distinction 5; preferred 600 ("the 700 weight clots the counters and diacritics of المُبلَّغ and the dots of القياس, and makes the Latin line heavier than its Arabic neighbours"). The 600 weight stays; no Bold file is added.
