# CLOSE-6C: how each review finding on CWR-012 was handled

- **Inputs:** `REDTEAM_6C.md` (verdict HOLD on B1, B2, B3) and `ARABIC_6C.md` (verdict PASS with M1–M6), both on review bundle v1.
- **Where the changes are:**
  - the Reading: `audit/close_out/close_6c_text.py`, exact edits, each matched once, plus a guard that the removed phrasings are gone;
  - the two records: `audit/close_out/close_6c_records.py`;
  - the text as applied: review bundle v2.
- **Confirmation pass:** the same two reviewers checked v2, and their verdicts are appended at the end of this file.

## Red-team (exchange-company, central-bank and methods readers)

| Id | How it was handled |
|---|---|
| B1 | **Applied.** s4's hypothesis is now about "transfers from relatives and friends", and the Thesis and s1 say "money sent between people". "Informal" no longer describes anything that passes through a licensed provider. It stays in two places only: the formal-products limit in s6, and the CCY "loans from informal networks". |
| B2 | **Applied.** The Question, Thesis, s1 and s4 are now comparative: "more through exchange companies and other money-transfer providers than through accounts". s4 gives the bound CLM-030 values (31.1% and 2.0% of 2014 recipients) instead of "about three in ten", and says the profile does not show how the others received money. The s9 falsification test is comparative to match. |
| B3 | **Applied.** s6 now reads "In the balance of payments …" and ends "… and the territory these values cover has not been mapped here." |
| S1 | **Applied.** s5 is retitled "Other explanations and limits". It opens with a new "Other routes" bullet (by hand, travellers, other providers, recipients among the 11.9% with an account). The Thesis now separates rival explanations (other routes, humanitarian cash) from limits (coverage, currency, meaning). The questionnaire wording about "brought yourself" was not verified, so it is not used. |
| S2 | **Applied.** The s3 heading is "… providers are listed, not measured". s7's "a larger exchange network" is now "more exchange outlets", so it cannot be read as the unified network that s3 now names. |
| S3 | **Applied.** s3 has a new paragraph on the 26 June 2024 rule, which post-dates the fieldwork and is not evidence of flows. VIS-PAYMENT-RAILS is bound (claim, evidence and verification bindings), and SRC-CBY-DEC-23-2024-001 is bound (source and direct-source bindings). The evidence period lists the rule. |
| S4 | **Applied.** s3 states the roster's scope: CBY-Aden licensing, no list from Sana'a held, not a count for all of Yemen. |
| S5 | **Applied in both records.** They now say "that the study places in areas under the internationally recognized government" (AR «تقول إنها تقع في مناطق الحكومة المعترف بها دوليًا»). |
| S6 | **Applied.** ISP says "three areas the study calls sub-districts" (AR «ثلاث مناطق تسميها الدراسة عُزلًا»), then "areas". SAM says "Ad-Dali … and Ja'ar …, which the study calls sub-districts" (AR «منطقتي الضالع … وجعار …، وتسميهما الدراسة عزلتين»). Reading s5 AR says «ثلاث مناطق». The source titles keep the studies' own words. |
| S7 | **Applied.** The ranking follows ISP p. 9: loans second in two of the three areas, and gifts the smallest share in all three. |
| S8 | **Applied.** "Money received by 'hawala' (the study's word)", "in the other study's sample, in selected villages of Ad-Dali and Ja'ar". AR «ما تلقوه عن طريق «الحوالة» (بتعبير الدراسة)». |
| S9 | **Applied.** "The study reports that, on average, 61% of the households assessed named …". "On average" is the study's own phrase (p. 12). |
| S10 | **Applied.** SAM now leads with the income sources and is retitled "Income sources reported by cash-assistance households, with a multiplier estimate, …". It stays on /remittances/ because the Reading binds it for its income-source and hawala points. The multiplier keeps its limits. |
| S11 | **Applied.** SAM meta: "… of activity, the aid itself included, …". |
| S12 | **Applied, in the safer form.** The ISP method no longer relies on the Figure 4 labels: "Values and rankings are those printed in the report's text (p. 9), not the data labels on its figure, and the shares are not summed". The "100%" clause and its value state are removed, so nothing printed depends on the image read. |
| S13 | **Applied.** s6 names both corridors: the UAE at 7.53%, lifted by a single high quote (VIS-REMITTANCE-COST). |
| S14 | **Applied.** R5 is committed at `audit/close_out/addendum/R5_ccy_isp_sam.md` in the same change, so every `loc` resolves. |
| S15 | **Not applied here: site-wide decision.** «تحالف النقد في اليمن» is in 89 governed cells, so changing it in one Reading would leave two names on the site. The Arabic editor (S14) concurs. Recorded in the W3f register as a terminology decision for the owner, with the cover's own name «اتحاد المساعدات النقدية في اليمن». The Latin gloss "(Cash Consortium of Yemen)" identifies the organisation at first mention. |
| N1 | **Applied.** "11.9% of adults in those areas". |
| N2 | **Applied.** "from its own question or, for 'either', from the two combined". |
| N3 | **Not applied.** The 12-month recall wording was not verified from the questionnaire, so no unverified period is printed. Recorded in the W3f register. |
| N4 | **Applied.** «أورد … قيمة الحوالات … عند». |
| N5 | **Applied in s8 and s4.** "a roster entry shows a licence listed for 2026; it does not by itself show that the provider operates now". |
| N6 | **Applied.** "published figures, from exchange companies, remittance agents or their supervisor, …". |
| N7 | **Not applied.** The class is internal and not rendered. 06 has no estimate class (CLAIM, VISUAL, TEMPORAL_OBSERVATION, DATASET, STATUS_EVENT, CROSSWALK_OBJECT, QUALITATIVE, PAIRED_CHRONOLOGY). Recorded in the W3f register. |
| N8 | **Applied.** "the largest assistance share of the three areas (68%)". |
| N9 | **Applied.** The governed text written here uses "Ad-Dali" ("Qa'tabah in Ad-Dali"). The studies' own spellings stay in their source titles. |
| N10 | **Applied, in the Arabic editor's house form (S6).** |
| N11 | **Applied.** CLM-016's wording: "World Bank estimates of entities, including exchange firms and microfinance institutions". |
| N12 | **At promotion.** The steward's D9 entries for the Reading and the two record routes come at promotion. The build regenerates the `/remittances/` search counts. |

## Arabic editor

| Id | How it was handled |
|---|---|
| M1 | **Applied.** «أي قيمة لقنوات الحوالات», inside the B2 rewrite of the Thesis and s1. |
| M2 | **Applied,** together with red-team N2. |
| M3 | **Applied.** «ما قد يبلغه حجم هذا الطريق», together with red-team S7 and S8. |
| M4 | **Applied,** with «ثلاث مناطق». |
| M5 | **Applied,** together with O6. |
| M6 | **Applied.** |
| S1 | **Applied.** Restructured with red-team S9 and S10 (income sources first), using «خلال 30 يومًا» and «التحويل النقدي نفسه». |
| S2 | **Applied.** The rule of June 2024 is added. |
| S3 | **Applied,** with B3: «وفي ميزان المدفوعات، تعطي …». |
| S4 | **Applied.** |
| S5 | **Applied.** |
| S6 | **Applied.** |
| S7 | **Applied,** with red-team S5, S6 and N8. |
| S8 | **Applied.** «لا القيم المدوّنة على الشكل البياني»; the clause relying on the image was removed (O7). |
| S9 | **Applied.** |
| S10 | **Applied.** Also reordered to lead with income sources (red-team S10). |
| S11 | **Applied.** |
| S12 | **Applied.** |
| S13 | **Applied.** Also «بما فيه المساعدات نفسها» (red-team S11). |
| S14 | **Register: site-wide naming decision.** See red-team S15. |
| N1–N4 | **Applied.** |
| N5–N7 | **No change**, as the editor advised. |
| O1 | **Superseded** by red-team S7, which was applied. |
| O2 | **Applied.** "a single social accounting matrix for each locality". |
| O3 | **Applied.** "in selected villages of Ad-Dali and Ja'ar". |
| O4 | **Applied.** "monthly or bi-monthly" removed. |
| O5 | **Applied.** |
| O6 | **Applied.** |
| O7 | **Applied.** The clause was removed. |

## Confirmation pass (review bundle v2; `REDTEAM_6C_CONFIRM.md`, `ARABIC_6C_CONFIRM.md`)

- **Red-team:** B1, B2 and B3 are CLOSED in both languages, and every new change was checked against its bound record. One new blocker was found, outside the v1 bundle:

  | Id | Finding | Outcome |
  |---|---|---|
  | NB1 | The route description said "the channel is not measured". The channel values exist and are published for all adults (VIS-FINDEX-FLOW-CHANNELS: "restricted does not mean missing"). | **Applied** verbatim: "no channel value for that wave is held here". |
  | NS1 | The June 2024 rule needed its scope and tense. | **Applied:** "On 26 June 2024 … required … under its supervision" (AR «ألزم … الخاضعين لرقابته»). |
  | NN1 | ISP's "Ad-Dali" could be read as the study area. | **Applied:** "Qa'tabah in Ad-Dali governorate". |
  | NN2 | The SAM meta should lead with the income share. | **Applied.** |
  | NS2 | The final check found NN2 had dropped "in selected villages". | **Applied.** |

- **Arabic editor:** M1–M6 and S1–S13 LANDED. Nine further items were applied:

  | Id | Change |
  |---|---|
  | C-S1 | «قرار» in place of «قاعدة» in the evidence period. |
  | C-S2 | «أيضًا» and «كان لديهم حساب». |
  | C-S3, C-S4 | «المناطق الخاضعة للحكومة المعترف بها دوليًا»; the SAM summary reordered. |
  | C-N1–C-N5 | Merged with NS1 where they overlap. |
  | F-S1 | «المشمولة» in place of «المقيَّمة». |

- **Numeral parity:** 0 value drift across 37 EN–AR pairs.
- **Final verdicts:** red-team **VERDICT: PROMOTE**; Arabic **ARABIC: PASS**. Under the owner's rule ("promote if there is no blocker"), CWR-012 is promoted in CLOSE-6C.

## Search alias 001 (separate finding in this transaction; found while closing CLOSE-6B)

- **The defect.** The alias's boundary note, shown with search results for "law" or "laws", said the evidence base "holds no law as a source document". That was false: the base holds SRC-CBY-DIL-21-2008, on the Bank Deposit Insurance Institution, which the /data/ scope line already names.
- **Red-team:** the new English is true and attributes neutrally (VERDICT: PROMOTE). NS3: the Arabic must change in the same transaction. **Met**, because both fields are written by `ALIAS001` in `close_6c_text.py`.
- **Arabic editor:** the meaning matches (ARABIC: PASS). A-S1: use the house form for the Sana'a bank. **Applied in both languages:** "Central Bank of Yemen in Sana'a" and «البنك المركزي اليمني في صنعاء».

## Gate-driven wording (after both verdicts; meaning unchanged)

- **RP-G06 (bilingual numeric invariance)** failed on the replica for /evidence/CCY-SAM-2024/. The English printed "USD 1" as a digit, while the Arabic writes «دولار أمريكي واحد» / «لكل دولار» in words, which the Arabic editor accepted.
- **The fix:** the English summary now says "each US dollar of the assistance" and the meta says "per aid dollar" (F6-G01 caps a description at 200 characters). The trivial value state "1" is dropped. No value, hedge or attribution changed.
