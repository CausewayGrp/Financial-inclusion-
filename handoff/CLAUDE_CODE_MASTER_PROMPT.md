> STATUS: SUPERSEDED (10 October 2026) — not for execution. See `handoff/README_FIRST.md`; design is executed in the repository under audit/close_out/BRIEF.md (W4).
>
> Until 10 October 2026 the status line of this file read, verbatim: "STARTED — CODE NO LONGER WAITS. The Design package in `design/` is accepted: the owner recorded the final D7 visual acceptance on 2 October 2026 (`audit/OWNER_DECISIONS_2026-10-02.md`, row D7) and `design/10_ACCEPTANCE_CHECKLIST.md` carries its evidence; the production runtime is pull request #8 and the EAD states are in `FINAL_OPEN_ITEMS_REGISTER.md` §1. History: until 2 October 2026 this line read "WAITING FOR THE DESIGN PACKAGE" with the instruction not to start until the package was accepted against `handoff/DESIGN_ACCEPTANCE_CRITERIA.md`; that literal stays on this line because gate R86-G01 (`scripts/validate.py`) reads it here, and the gate is not changed by a record. This file is not for Claude Design." It is kept here as history; nothing in this file is executed.

# Claude Code — implementation brief (started 29 September 2026; the package accepted 2 October 2026)

## When you start

The accepted Design package is in `design/` (with `design/09_CODE_HANDOFF.md` and the runnable `design/reference/`),
and `design/10_ACCEPTANCE_CHECKLIST.md` is complete with evidence. Read, in order:

1. `handoff/README_FIRST.md` — authority, rules, repository protocol.
2. `handoff/ENGINEERING_HANDOFF_EXPECTATIONS.md` — what you must deliver and the rules you may not break.
3. `design/00_DESIGN_README.md` and `design/09_CODE_HANDOFF.md` — the design you implement; then `design/DESIGN_DEBT.md`,
   `design/COVERAGE.csv` and `design/ESCALATIONS.md` — what is temporary, what was proved and what is still open.
4. `handoff/DESIGN_TO_CODE_CONTRACT.md` — what the design guarantees you.
5. `docs/DEPLOYMENT.md` — discovery, headers and privacy contract.
6. `FINAL_OPEN_ITEMS_REGISTER.md` — owner and release items (do not fill them).

## Your job

Productionise the accepted design as **one** static, local-first public runtime rendered from `site-src/content/**`,
keeping every behaviour and gate that exists today, and removing the replaced renderer once parity is proven. You do not
redesign, you do not author content, and you do not change the Master. Design gaps go back to Design as recorded
questions; truth gaps go to the Master as `ESCALATE_TO_MASTER` or `NEEDS_CONTROLLED_CONTENT`.

## Done means

Every gate in `CONTRIBUTING.md` §5 is green on the new runtime; the Design acceptance criteria still hold on the
implemented site; the deployment contract is implemented; and nothing claims public release readiness, WCAG conformance,
legal review, rights clearance or security guarantees.
