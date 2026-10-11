# CLOSE-6D review pair — disposition (11 October 2026)

Two challenger lenses reviewed the staged CLOSE-6D texts before the transaction ran on the Master: the domain lens
(survey statistician and analytical-product red team for 6B-1 and 6B-5; MSME finance for 6B-2; central-bank
regulator / legal librarian for 6B-3; balance-of-payments statistician for 6B-4) and the Arabic-editor lens. Their
reports are REDTEAM_6D.md and ARABIC_6D.md beside this file. The review packets were drawn from the staged Master.

Verdicts on CWR-012: domain lens **KEEP, conditional on B1–B3** ("if B1–B3 are not fixed in CLOSE-6D, WITHDRAW");
Arabic lens **KEEP** (no blocker). B1–B3 were fixed in close_6d_text.py (the "Domain-lens revisions" block); a
confirmation pass on the revised texts is recorded at the end of this file.

## Domain lens

| ID | Finding | Disposition |
|---|---|---|
| B1 | Thesis lost its counterweight sentence and gained the bound | Applied: the bound leaves the thesis; "Other routes, such as cash carried by hand, and humanitarian cash fit the same numbers…" restored, both languages |
| B2 | Bound printed as an exact floor; "in surveyed areas" dropped | Applied: "Both shares are survey estimates, so the bound is an estimate too" and "in surveyed areas" wherever the bound is printed (s2, s4, s7, prohibited inference, VIS-FINDEX-FLOW-CHANNELS) |
| B3 | Bound arranged as support (s1 heading, s4 after the 2014 shares, s2 pointer; disclaimer about "travelled" while the question is receipt) | Applied: bound moved to the descriptive s2; s4 refers to it with "bears only on whether recipients could have received the money into such an account of their own; it does not establish the channel, and it neither confirms nor refutes the hypothesis"; 2014 shares follow, marked "Separately" and "do not describe the 2021 wave"; s1 heading changed (S4) |
| B4 | "through 12 partner institutions" (11 issued guarantees in 2022) | Applied: "and that it has 12 partner institutions" |
| B5 | Other surfaces may still print "did not ask" | Does not reproduce: the staged projections were grepped after the full pipeline (site-src/content and dist); the only survivor is CLM-001's method, where the three observed facts travel with it (6B-1(e)); 27_FINDEX_SUBGROUPS rows are non-public and are relabelled in CLOSE-6F (7c) |
| S1 | "no weighted estimate … is published" while fin29 = 0 is published | Applied: "no weighted estimate of the channel usable here is published or held"; the thesis names the printed zero and that it is not used |
| S2 | Halves out of order in s9; s8 implies the first half alone | Applied: s9 reordered; s8 carries both halves in order |
| S3 | The item asks about "a bank or mobile-money account" | Applied in the thesis and s3 |
| S4 | s1 heading over-promises | Applied: "What the evidence establishes, and what remains a hypothesis" / «ما الذي تثبته الأدلة، وما الذي يبقى فرضية؟». The title keeps the Arabic question mark (the Arabic lens judged it acceptable and consistent with the site) |
| S5 | The two routes overlap | Applied without the unverified remittance-network example: "The two routes are not mutually exclusive, and the evidence here does not separate them." |
| S6 | "includes Yemen itself" unsupported (V1: the pages do not say) | Applied, a challenge to the instruction's text: "under which Yemen is itself classed as low income" (Yemen's source-28 record: "Low income (FY24)") on /people/ and CLM-001 |
| S7 | Gender split compared across periods and terms | Applied: "the gender figures cover different periods and use different terms (women-led, men-owned), so they are not compared"; «ولا يُدمجان في سلسلة واحدة» kept |
| S8 | "CBY-Aden's supervision" puts words into the instrument | Applied: "apply, in their own words, to providers … in the Republic of Yemen under the supervision of 'the Central Bank', and to their agents: as CBY-Aden's instrument, they reach the providers CBY-Aden supervises" (CLM-011, VIS-FCP-REDRESS-PATH, VIS-OECD-FCP-TIMELINE, universe fields); MA-006 "the providers they cover" |
| S9 | ج and د: د refers back to ج | Applied everywhere the relation is stated |
| S10 | Deposit guarantee: search scope, the 2025 decision, the exclusions, the law-number conflict | Applied (a), (c), (d); (b) already recorded in YSC-028's fact (Law No. 21 in the copy CBY-Aden hosts; Decision No. 6 of 2025 cites No. 40) |
| S11 | "Neither ratio converts … for any component" is false for 1.838 in 2021–2024 | Applied, a challenge to the instruction's text: "Neither is a published conversion factor: 1.838 describes how the two remittance series relate in 2021–2024, not a rule for other years or components, and the 33% ratio is applied inside the IMF's own estimates" |
| S12 | IMF series basis is implied by its method, not labelled | Applied to CLM-007's summary |
| S13 | Postal Savings Fund | Applied; page cited (p. 16) |
| N1 | s5 "households" for recipients | Applied |
| N2 | CLM-001 method "were not asked" | Kept: 6B-1(e) keeps it where the three facts travel with it |
| N3 | /methodology/ "(round; …)" | Applied: "(the latest round; …)" |
| N4 | CLM-011 escalation ground 1 incomplete | Applied |
| N5 | USD / US$ mixed | Not changed: the US$ strings are in fields this transaction does not otherwise touch |
| N6 | /finance/ "would in any case use … different questions" unsupported | Applied: "Such figures would remain separate evidence rather than a harmonised series." |
| N7 | /reforms/ never carried "9 August 2023" | Noted for CO-G07: the e-money check asserts the sentence is unchanged, not the date string |
| N8 | "tell a different story" | Applied: "Guarantee data measure something else." |
| N9 | YLG pages 9 and 31 | Applied to the source note |

## Arabic lens

All should-fix items applied (SF-1 «المحمول»; SF-2 «ولا يُحتفظ به هنا»; SF-3 the Reading's own terms; SF-4 «موزونة»;
SF-5 a share, not a count; SF-6 «الـ12 شهرًا»; SF-7; SF-8 «خلال عام 2022 ما مجموعه»; SF-9; SF-10 «قديم العهد»; SF-11).
Nits applied in fields this transaction touches: N-1, N-4, N-5 (CLM-027 limitations only), N-8, N-9, N-11 (page cited).
Not applied: N-7's «وتختلف مجموعتا الأرقام» (it would break the required string «ولا يُدمجان في سلسلة واحدة»); N-2, N-3,
N-5 (other fields), N-6, N-7's other items (unchanged fields; the bilingual-invariance check normalises 2022–23 and the
dual); N-10 («الصفحة» is a recognised document reference; the OECD printed pages 33 and 36 are V2's reading, against the
instruction's p.35); N-12 accepted as is.
