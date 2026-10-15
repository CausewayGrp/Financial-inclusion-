# Stage A material adjudications — 15 October 2026

Authority: owner's Stage A reconciliation assignment and clarification. Research-package IDs below are leads, not approved edits or a parallel Production Master. No S11A ZIP was required or treated as missing authority.

## Baseline and physical authority

Starting main: `a2ad120784822ce068aacc5fd638b69429612b73`, clean tree, no open PRs. Verify `38718968732` passed. GitHub's contents API reports Master Git blob `6d86df8fc64f0c32c3ee1874682de3045985dd0f`, exactly the blob in fetched origin/main. Its physical SHA-256 is `87dafc6f18837ff61f032f1c93a7668c9affe9638aa104ab6ad50a2c05512975`, agreeing with AUTHORITY and Context. The different Drive-recorded lineage hash is not replacement authority.

STAGE-A-FINAL changes 49 exact-value-guarded cells. Final Master SHA-256: `580d2dc19054658d906585104b957a0fe9f4f3ce4758e6bc19b1cae28fb28bc8`. The runner reports COMMITTED; see the cell plan, Master ledger and run report in this directory. No historical observation, ratio, reporting-universe field, provider identity, source permission, or data-download/deployment flag is changed. The numerical-date changes concern the website edition and its public correction record, not the observation clock.

## Q-H01 / S10E-TR-01/02 / S11-T01 — chronology: correct

`04_NAV_UX!B256:C256` still described an edition of 3 October and rows 592–593/597 described a universal source-check cutoff. But `SRC-IMF-YEM-SMP-2026-APPROVAL` records publication 7 October and retrieval 10 October; WDI products record an 8 October update. CLOSE-2B onward, through CLOSE-6G and PR #46's 14 October merge, integrated later material. PR #47 reconciled operational documentation on 15 October. These facts disprove the universal 3 October claim; they do not establish that every source was reviewed on any later single day.

The governed pre-release edition is now 15 October. `UI-EDITION-CHECKED-DATE` explicitly points to each source record, and strip/colophon labels say checking is record-specific. `/corrections/` section 3 distinguishes publication, observation, retrieval, substantive review, edition and this correction event. Current-edition analytical classification descriptions in VIS-EVIDENCE-FRESHNESS, CLM-014, VIS-EVIDENCE-GAPS and VIS-EVIDENCE-CLASS-LADDER no longer freeze themselves to the obsolete edition date; real dated source checks, observation dates and historical licence/owner decisions remain unchanged. CS-01 now enforces EN/AR edition identity, correction binding, no source publication after the edition, and no universal checking cutoff. E2-DATES recognizes the Master-governed edition as a product event, with its own CS-01 checks; it does not recast it as a source observation. Negative controls exercise the two distinct chronology faults.

## CWR-011 / S10C-ED-12 / S11-M02 — IMF zeros: correct interpretation only

The existing original-read record `audit/close_out/w0/A2_imf_yem.md`, CR-08, quotes Country Report 26/80 Table 5 (printed p.31/PDF p.36), including the early NPL ratios printed 0.0, and identifies the sole table note as “Source: Yemeni Authorities; IMF Staff Calculations”. It also records compilation/quality cautions (¶35, Annex V). That note does not establish a missing-value code. The same audit row's conclusion “0.0 ... = not reported (matches brief)” is an interpretation, not an original-source explanation.

`03_PAGE_SECTIONS!E103/G104` (Finance) and `E374/G374` (CWR-011 alternatives) asserted “reads as not reported”. Replace it in both languages with the explicit uncertainty: the available table note does not explain whether the printed entries are measured zeros or unavailable observations, and this resource classifies them as neither. Preserve values and the qualification that the table does not state its banking/area perimeter. No historical series is revised, drawn or newly generalized.

A fresh request to the IMF PDF was refused by the session's network proxy. This ruling withdraws an unsupported certainty; it does not claim a new original reading or solve the historical coding question. To classify the early entries later requires original IMF/authority reporting metadata explicitly explaining their codes and perimeter.

## CWR-012 / S10D-ED-01/02 / S11-M01 — contradiction: withdraw overclaim, keep Reading

`audit/close_out/v5_reads/V1_findex.md` §§1–2 records the questionnaire/variable documentation and API metadata. The variable `fin29_1` asks recipients about receiving using a bank/mobile-money account; its catalogue frequencies are unweighted and conditional on recipients. The public API `fin29` describes receipt into an account as a percentage of all adults 15+, with a different denominator; it is not a weighted channel distribution among recipients. The API's Yemen data are dated 2022 for the Global Findex 2021 wave, and the recorded source vintage is 6 October 2025. Survey fieldwork is November 2022–January 2023. Naming the wave is not changing the observation date.

The internal read records a literal API zero and positive catalogue responses, but does not supply the matched construction code, filtering/eligibility rules, response-weight treatment and vintage reconciliation needed to establish that the two published representations must yield the same estimand. The printed API value alone cannot establish a zero receipt-channel share. No current independent re-fetch was possible (World Bank hosts proxy-blocked). Do not promote the superseded S10C-ED-13/15 cards or infer a numerical replacement.

Replace the contradiction claim in `08_READINGS!H16:I16`, `03_PAGE_SECTIONS!E379:G379` (EN and AR body cells), `06_EVIDENCE_OBJECTS!P45:Q45`, and the paired VIS-FINDEX-FLOW-CHANNELS visual boundary. State only that no verified weighted channel distribution is held here, document the unweighted-response limit, and name the matching requirements. Retain 31.9%/11.9% surveyed-adult facts, the explicitly CauseWay-derived overlap bound and its limits, historical 2014 recipient shares, alternative explanations and the legitimate hypothesis. No national market share, household prevalence or new channel distribution is inferred. The unresolved construction question remains an evidence frontier, not a publisher error.

## S10F-UX-01 / S11-U01 — four record self-links: remove misleading action

VIS-MFI-DIVERGENCE, VIS-CBY-MONETARY-SNAPSHOT and VIS-YER-MARKET-RATE are governed at `/finance/`; VIS-ACCESS-EVIDENCE-LAYER at `/access/`. None has an entry in the Master-derived Evidence Object collection or a published Passport route. The visual projection correctly located each on its domain but the renderer called that domain URL “Open evidence record”/“Full record”, including detached captions.

Fix the implementation gap: a domain location alone no longer receives record actions/caption URLs; existing governed Reading destinations retain their behavior. The domain location remains available for citation; the four figures, tables/text alternatives, boundaries and existing domain evidence navigation remain. No new Passport or controlled navigation-contract entry is fabricated. `test_stage_a_reconciliation.py` exercises each figure EN/AR at 390/1440px, disclosure opening, absence of misleading links, real domain-to-record navigation and browser return; it is added to Browser acceptance. SA-LINK and a planted self-link negative control guard the defect.

## Verification and controlled history

PR #43 merged `eac94b9c`; #44 `ca8fabd2`; #45 `612ec146`; #46 `e46ff9eb`; #47 `a2ad1207`. The original Stage A final report remains historical; this record adds adjudications rather than inventing earlier approval. Its appendix acceptance checks still apply, alongside the corrections here. Existing FRONTIER/rights/release limits remain disclosed.

Four runner attempts rolled back before the committed run: strict strip-placeholder mismatch; missing local Playwright cache variable; the new edition product date lacking explicit E2-DATES recognition; visual boundary parity and missing audit-index entry. Their reports are preserved, not represented as successful transactions. The final run's generation, rebind, build, literal audit (19,737 records, zero unresolved/open/problems), diagrams, inventory, validator and generator idempotence passed. Remaining full verification and prospective acceptance are recorded separately; nine green jobs are required before normal merge.
