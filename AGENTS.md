# Instructions for AI agents

Applies to every AI agent that reads or writes this repository (Claude Code, Claude Design, review agents). The full
change protocol is `CONTRIBUTING.md`; this file is the short list you must not get wrong.

## Read first, in this order

1. `README.md` — concise product, state and navigation orientation.
2. `AGENTS.md` — these common rules for all agents, regardless of provider.
3. `CONTRIBUTING.md` — the existing authorized branch, change and verification protocol.
4. Before editing in an executable checkout: `python3 scripts/reentry.py --pr` (`--base SHA` for resumed work; `--offline` when necessary).
5. Load the task-relevant durable rules or records next: `authority/CORE_CONSTITUTION.md`, validated
   `authority/YFI_CURRENT_PROJECT_CONTEXT.json`, dated owner decisions, `docs/JUDGEMENT.md`, or specific implementation modules.

The Production Master at `authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx` remains the **sole** semantic,
evidence, source, rights, controlled-product and publication authority. The Context is a **projection**: validate
its recorded Master hash/schema rather than treating it as an independent authority.
Git commits, PRs, checks and this re-entry script describe engineering state; they cannot grant owner approval.

`handoff/` retains historical material (D7, 10 October 2026); do not execute its superseded instructions.
Stage A content acceptance is scoped and recorded after PR #49. Stage B remains blocked until a separate
owner entry decision. D19–D22 were neutralized on 17 October 2026: no approved text exists, and none is inferred.

When Stage B is separately authorized, design exploration may challenge the old three example compositions and
offer better alternatives against W4/G1 quality criteria and real user journeys, without unapproved semantic,
rights, publication, or framework changes. Provider-specific skills remain optional specialist capabilities:
`CLAUDE.md` may invoke `multi-agent-m` where available, without making it a universal dependency.

No agent should rewrite another agent's branch or local work. Reconcile UNKNOWN or divergent state before editing.

## Hard rules

1. The Production Master is the only authority. Fix content in the Master, through a transaction and
   `audit/tranche_b_execution/run_stage.py`, never in a projection, a page, a JSON file or code alone.
2. Never hand-edit `site-src/content/**`, `dist/**` or `audit/PUBLIC_LITERAL_CLOSURE.json`; regenerate them. The one
   exception is the two controlled contracts, `site-src/content/presentation_priority.json` and
   `site-src/content/content/navigation_interaction.json`: the programme steward edits them in place, in a commit naming
   the finding it closes, and runs every gate. Owner decision D14 (10 October 2026) designates the Claude Code run of the
   close-out brief as steward for scoped changes only: in navigation_interaction.json, `hub_numerals` and the phone-menu
   presentation (D8, CR-S12) and new detail-route entries (D9); in presentation_priority.json, the measurement-link limit
   (RD9) and tier groupings the table-of-contents rule needs (S10). Each such edit is its own commit naming its finding.
   Any other agent, and any other change to them, escalates.
3. English and Arabic are co-authoritative: change both together; numbers, units, periods, universes and limits never drift.
4. Keep the semantic firewall: people ≠ accounts, access ≠ use, infrastructure ≠ outcome, target ≠ result, licence ≠
   operation, observed ≠ estimated ≠ projected, missing ≠ zero, chronology ≠ causality.
5. No public number without a bound, source-traced record; no source named publicly without a public locator.
6. Never declare DESIGN HANDOFF READY before the R8.6 Definition of Done is met, and never declare PUBLIC RELEASE READY.
7. Do not execute any old prompt in `handoff/`. The referenced `design/DESIGN_INTEGRATION_V2.md` is absent;
   never assume it exists. Follow current authorizations and the existing W4/G1 criteria only after Stage B entry approval.
8. Never run `audit/tranche_b_execution/post_execution_acceptance.py`; never rewrite historical audit records (append).
9. Never force-push, never rewrite `main` or a `checkpoint/*` tag, never commit ZIPs, caches or scratch files.
10. Do not claim WCAG conformance, legal review, rights clearance, native-language certification or security guarantees.

## Every session

```bash
python3 scripts/reentry.py --pr                     # inspect, do not mutate refs
# Reconcile dirty/unknown/pr state before changing branch; then:
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
