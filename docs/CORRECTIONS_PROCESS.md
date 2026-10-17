# Corrections process

How an error report about the Yemen Financial Inclusion Evidence resource is received, triaged, fixed and logged.
Linked from the public page `/corrections/` (Stage B, B2 T, 17 October 2026; BRIEF W4 T). The public rules it rests on
are on `/corrections/` (what counts as a material correction, how history works) and `/terms/`; this document adds the
steps and the times.

## 1. How a report arrives

- **The form.** Every record, figure and Reading carries "Report an error", which opens `/contact/#report` pre-filled
  with the page address, the record or figure ID, the section, the language and the edition. The form prepares an
  e-mail to the monitored contact address stated on `/contact/` in a fixed `key: value` format under a reference code
  `YFIE-ERR-<record or PAGE>-<yyyymmdd-hhmm>` (UTC). Nothing is sent until the reporter sends it from their mail app;
  webmail users copy the report instead. Without JavaScript the page offers a pre-addressed e-mail with the same field
  list as instructions.
- **No server.** The site is static and hosting-neutral: no form data is posted to any endpoint, and no third-party
  service is called. A first-party POST endpoint with spam control is a hosting-stage option, off by default; if it is
  ever switched on, `/privacy/` states the retention first, Master-first, on the same day.
- **Plain e-mail** to the contact address with the same fields is treated the same way.

## 2. Triage, within ten working days of receipt

1. **Acknowledge** to the reporter, if they gave an address, with the reference code.
2. **Classify** the report as one of:
   - **Material** — a public value, definition, period, universe, supporting evidence, source link, derivation,
     reuse condition or interpretation would change (the `/corrections/` rule);
   - **Editorial** — wording, layout or translation that does not change meaning;
   - **Not an error** — the resource says what the evidence supports; reply with the reason and the record's
     "Does not establish" line;
   - **Out of scope** — a question about the evidence itself, a request for data the resource does not hold, or a
     rights or privacy matter, each routed as `/contact/` describes.
3. **Record** the classification and the reference code in `audit/close_out/PROGRESS.md` (an appended, dated line;
   the reporter's name and address are never written to the repository).

## 3. The fix, Master-first

- Content changes are made only in the Production Master
  (`authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx`) through a recorded transaction run with
  `audit/tranche_b_execution/run_stage.py`, EN and AR together; the projections, pages, literal closure and manifest
  are regenerated, never hand-edited (`AGENTS.md`, `CONTRIBUTING.md` §4–5).
- A material fix carries its evidence: the corrected value is bound to a public source locator, or the value is
  withdrawn and its absence stated. No number is changed on a reporter's word alone.
- Every gate runs before the change is merged (validator, literal audit, content parity, bilingual invariance,
  browser suites). The transaction's ledger names the reference code of the report that caused it.

## 4. The public log

- A material correction is logged on `/corrections/` against the stable evidence ID and the edition, with the date,
  what changed and why, so an earlier citation can still be understood. The entry is Master content (the correction
  ledger), not a page edit.
- An editorial fix is not logged as a correction (the `/corrections/` rule); it appears in `docs/CHANGELOG.md`.
- The record's "Corrections and release history" link reaches the entries that concern it.

## 5. Reply to the reporter

- If the reporter gave an address, they receive the outcome: the classification, the correction entry or the reason
  no change was made, and the edition in which the change is or will be published. Reports without an address are
  handled the same way, without a reply.
- Addresses are used only for that reply and are not stored beyond the mailbox (`/privacy/`).

## 6. Times

| Step | Within |
|---|---|
| Acknowledgement (when an address is given) | 10 working days |
| Classification recorded | 10 working days |
| Material fix published, or the reason it is not | the next edition, and no later than 60 days |
| Reply with the outcome | with the fix, or at 60 days with the state |

These are the resource's own commitments; `/contact/` states that no response time has been published for the general
contact channel, and that remains true for matters outside this process.
