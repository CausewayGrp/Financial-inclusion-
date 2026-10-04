# Instructions for AI agents

Applies to every AI agent that reads or writes this repository (Claude Code, Claude Design, review agents). The full
change protocol is `CONTRIBUTING.md`; this file is the short list you must not get wrong.

## Read first, in this order

1. `README.md` — what the product is, where it stands, where everything lives.
2. `OPENAI_REENTRY_CHECKPOINT.md` — the current checkpoint and open items.
3. `authority/CORE_CONSTITUTION.md` — durable rules.
4. `CONTRIBUTING.md` — how changes are made, committed and synced.
5. `docs/JUDGEMENT.md` — one page on how to decide what to build, in what form, and when to stop.

Claude Design and Claude Code do not use this list: their start file is `handoff/README_FIRST.md`, with its own reading
order. The programme state lives in `README.md`, the checkpoint and `authority/YFI_CURRENT_PROJECT_CONTEXT.json`, which
agree.
Trust the repository bytes over any chat history, prompt, ZIP or earlier summary; if they disagree, diagnose and record
the difference.

## Hard rules

1. The Production Master is the only authority. Fix content in the Master, through a transaction and
   `audit/tranche_b_execution/run_stage.py`, never in a projection, a page, a JSON file or code alone.
2. Never hand-edit `site-src/content/**`, `dist/**` or `audit/PUBLIC_LITERAL_CLOSURE.json`; regenerate them. The one
   exception is the two controlled contracts, `site-src/content/presentation_priority.json` and
   `site-src/content/content/navigation_interaction.json`: the programme steward edits them in place, in a commit naming
   the finding it closes, and runs every gate. Claude Design and Claude Code never edit them; they escalate.
3. English and Arabic are co-authoritative: change both together; numbers, units, periods, universes and limits never drift.
4. Keep the semantic firewall: people ≠ accounts, access ≠ use, infrastructure ≠ outcome, target ≠ result, licence ≠
   operation, observed ≠ estimated ≠ projected, missing ≠ zero, chronology ≠ causality.
5. No public number without a bound, source-traced record; no source named publicly without a public locator.
6. Never declare DESIGN HANDOFF READY before the R8.6 Definition of Done is met, and never declare PUBLIC RELEASE READY.
7. Do not execute the prompts in `handoff/` until the first line of `handoff/README_FIRST.md` reads DESIGN HANDOFF READY.
8. Never run `audit/tranche_b_execution/post_execution_acceptance.py`; never rewrite historical audit records (append).
9. Never force-push, never rewrite `main` or a `checkpoint/*` tag, never commit ZIPs, caches or scratch files.
10. Do not claim WCAG conformance, legal review, rights clearance, native-language certification or security guarantees.

## Every session

```bash
git fetch origin && git status                      # start from origin/main or your branch rebased on it
python3 scripts/checksums.py --check && python3 scripts/validate.py
# … one atomic change (CONTRIBUTING.md §4 for the Master) …
# run the gates (CONTRIBUTING.md §5), then:
git add -A && python3 scripts/repository_manifest.py   # classify every tracked file
python3 scripts/checksums.py                        # regenerate SHA256SUMS.txt
git add -A && git commit                            # Conventional Commit; Master trailers when the Master changed
git push
```

Work that is not pushed does not exist for the next session.
