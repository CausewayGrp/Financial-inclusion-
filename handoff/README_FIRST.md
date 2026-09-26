> STATUS: **DESIGN HANDOFF READY.** Start here. R8.6 closed on 26 September 2026 after a clean-room acceptance by three cold recipients (`audit/FINAL_CLEAN_ROOM_ACCEPTANCE.md`). Not a public release.

# Read this first — Yemen Financial Inclusion Evidence · أدلة الشمول المالي في اليمن

This folder is the one start path for the design of this product. Everything you need is inside this repository; you do
not need any earlier conversation, handover, ZIP or prompt, and you must not use one.

## 1. What this is

A bilingual public evidence resource, built and maintained by CauseWay, that helps people **understand, compare and
verify** the evidence on financial inclusion in Yemen. Arabic and English are co-authoritative editions. It clarifies
evidence for human decisions; it makes no regulatory, political, business or funding decision for anyone.

It moves a reader from a question to the strongest defensible answer, what it means, what it does not establish, the
system context, what remains unknown, what should be measured next — and then to the evidence record, the method and
the original source. The public site already exists as a complete, tested reference build with a deliberately plain baseline style, in
`dist/` (288 static HTML documents). You are designing the final product from that governed baseline.

## 2. Your role

**Claude Design** designs the whole product and delivers a **runnable, fully populated reference implementation** plus a
repository-backed design package, so that **Claude Code** can then build the production runtime without guessing. You
own the visual and interaction solution. You do not own the truth: facts, wording of controlled meaning, evidence states,
sources and rights come from the Production Master and cannot be changed by design.

## 3. Where truth lives

```
authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx      the only authority (never parsed by the browser)
  → scripts/generate_projections.py                           deterministic, byte-for-byte
  → site-src/content/**                                       the projections you design from (never edit by hand)
  → scripts/build.py                                          the reference renderer
  → dist/                                                     the public reference build (never edit by hand)
```

Production Master SHA-256 `17db032b15da16fc4b5b3c3b49f19aebf2ecb4ec46634613fe8505d0f038690b`; Page Specs
(`site-src/content/page_specs.json`) SHA-256 `d45748046ea56fd0e67fdf112f9888de65b3fe7fab46ce6f51de3a80824b69aa`. If the
repository shows other hashes, the repository is right — re-read it; never restore a hash from a document.

A content defect is never fixed in a page, a JSON file or a component. It is escalated (§10) and fixed in the Master by
the programme.

## 4. Start path — read in this order

| # | File | Why |
|---|---|---|
| 1 | this file | orientation, rules, protocol |
| 2 | [`CLAUDE_DESIGN_MASTER_PROMPT.md`](CLAUDE_DESIGN_MASTER_PROMPT.md) | **the executable brief** — everything you must design, build, test and deliver |
| 3 | [`ROUTE_CONTENT_AND_STATE_INVENTORY.json`](ROUTE_CONTENT_AND_STATE_INVENTORY.json) | every route with its family, bindings, hard states; every evidence, visual and technical state (derived) |
| 4 | [`DESIGN_ACCEPTANCE_CRITERIA.md`](DESIGN_ACCEPTANCE_CRITERIA.md) | how your work is accepted — test against it as you go |
| 5 | [`DESIGN_TO_CODE_CONTRACT.md`](DESIGN_TO_CODE_CONTRACT.md) | what you must record for Code, continuously |
| 6 | [`VISUAL_DESIGN_CONTRACT.md`](VISUAL_DESIGN_CONTRACT.md) with `site-src/content/visuals/visual_design_contracts.json` | how every chart may and may not be drawn |
| 7 | [`ENGINEERING_HANDOFF_EXPECTATIONS.md`](ENGINEERING_HANDOFF_EXPECTATIONS.md) | what Code will need from you, and the runtime rules your design must respect |
| 8 | [`../FINAL_OPEN_ITEMS_REGISTER.md`](../FINAL_OPEN_ITEMS_REGISTER.md) | what is still unknown or owner-dependent (none blocks Design) |
| 9 | `dist/en/` and `dist/ar/` in a browser (`python3 -m http.server 4173 --directory dist`) | the working baseline: every route, tool and state |

Do **not** start from `audit/`. It is the programme's memory; open a record only when a specific question needs its
reasoning (`audit/INDEX.md` says which record answers what).

## 5. What cannot change (frozen)

Factual content and every number; evidence relationships and bindings; public-state distinctions (observed, estimated,
projected, historical, withheld, missing, contradictory …); each route's purpose; required behaviours and actions;
Arabic–English equality; the accessibility outcomes; visual semantics and prohibited inferences; the canonical CauseWay
logo (`site-src/assets/CauseWay_Master_Logo.png`, SHA-256 `5830163d…` (full hash: `logo_sha256` in `FINAL_REPOSITORY_MANIFEST.json`)
— never redrawn, recoloured, distorted, cropped or regenerated); the IBM Plex family requirement; citation and source
behaviour; rights constraints; and the rule that no internal or repository language reaches the public.

## 6. What you own (free)

Composition, grid, hierarchy, rhythm, spacing; palette within contrast and identity constraints; component form; chart
form where several forms satisfy a visual contract; interaction choreography; micro-motion; responsive expression;
editorial pacing. `DESIGN_STARTING_TOKENS.json` is a starting hypothesis, not a constraint.

## 7. What is unknown

Nothing that blocks Design. The open items — the release domain, contact-mailbox confirmation, CauseWay's identity and
funding statement, the content licence that gates downloads, web-size logo derivatives, two maintainer decisions on the
hand-maintained contracts (whose known disagreements the brief §2 resolves for you), eleven source checks that leave
today's text unchanged until the source is read, and eight known evidence frontiers — are listed with their class, where
they show and who owns them in `FINAL_OPEN_ITEMS_REGISTER.md`. Design the honest state each page already has; never fill
one.

## 8. How to test

```bash
python3 -m pip install -r requirements.txt && python3 -m playwright install chromium
python3 scripts/checksums.py --check && python3 scripts/generate_projections.py --check
python3 scripts/build.py && python3 scripts/audit_public_literals.py && python3 scripts/validate.py
python3 scripts/tests/test_public_tools.py && python3 audit/tranche_c/checks/viewport_acceptance.py
python3 audit/tranche_c/checks/bilingual_invariance.py
```

Every command must pass before and after your work (CI runs them on every pull request). `CONTRIBUTING.md` §5 lists all
gates and what each protects. Your own acceptance tests are in `DESIGN_ACCEPTANCE_CRITERIA.md`; the browser suites and
the invariance check run on your reference implementation with `YFIE_SITE_DIR=design/reference/out` (brief §19). The
commands work from a clone and from the handoff archive alike.

## 9. Working in the repository

- Canonical repository: GitHub `CausewayGrp/Financial-inclusion-`, branch `main` (always green).
- Work on branches named `design/<gate>-<slug>` (gates D0–D7 in the brief, §20); open one pull request to `main` per
  gate, each leaving a runnable state; merge only when **Verify** (Governance gates + Browser acceptance) is green. Never
  force-push; never rewrite `main` or a `checkpoint/*` tag.
- Put the design package in `design/` (see the brief, §19); never edit `authority/`, `site-src/content/`, `dist/` or
  anything under `audit/` (outputs the scripts regenerate are not edits), and never edit the test suites.
- Without push access, or starting from the handoff archive: `git init -q && git add -A && git commit -qm "import handoff"`,
  work locally, and deliver each gate as a git bundle or patch series (brief §21); the steward lands it through the same
  gates.
- Commit messages follow Conventional Commits (`CONTRIBUTING.md` §3). Before each commit, classify any new file in
  `scripts/repository_manifest.py` and regenerate `FINAL_REPOSITORY_MANIFEST.json` and `SHA256SUMS.txt`
  (`CONTRIBUTING.md` §7 and §8).

## 10. If something looks wrong

Record it in `design/ESCALATIONS.md` and keep designing:

- `ESCALATE_TO_MASTER — <route/object> — <defect> — <design impact>` when the controlled truth looks wrong;
- `NEEDS_CONTROLLED_CONTENT — <route/object> — <field> — <design impact>` when a field you need does not exist.

Never invent copy, numbers, labels, dates, authors or sources to fill a gap, and never search the web to fill one. The
steward (the programme owner of this repository) answers escalations Master-first and appends lasting ones to
`FINAL_OPEN_ITEMS_REGISTER.md`; the labels you are expected to request are listed in the brief §10.

## 11. What Code receives after you

This repository with your `design/` package, the runnable reference implementation, and a Design-to-Code contract that
maps tokens, components, states, routes, content bindings, visual contracts, responsive rules and accessibility
behaviour. `CLAUDE_CODE_MASTER_PROMPT.md` waits until then.

## 12. Files in this folder

| File | Role |
|---|---|
| `README_FIRST.md` | this start file |
| `CLAUDE_DESIGN_MASTER_PROMPT.md` | the one executable Design brief |
| `ROUTE_CONTENT_AND_STATE_INVENTORY.json` | derived route, content and hard-state map (`scripts/handoff_inventory.py`) |
| `DESIGN_ACCEPTANCE_CRITERIA.md` | acceptance tests for the design package and reference implementation |
| `DESIGN_TO_CODE_CONTRACT.md` | what the design must specify for Code |
| `VISUAL_DESIGN_CONTRACT.md` | reading guide to the governed visual contracts |
| `ENGINEERING_HANDOFF_EXPECTATIONS.md` | runtime, discovery, security, performance and release rules for Code (and the constraints they put on Design) |
| `DESIGN_STARTING_TOKENS.json` | starting token hypotheses (palette, type, spacing) — replace freely with a documented system |
| `IMPLEMENTATION_MANIFEST.json` | machine-readable summary: authority hashes, counts, routes, navigation, prohibitions (rebound on every Master change) |
| `CLAUDE_CODE_MASTER_PROMPT.md` | waits for the Design package; not for Design |
| `SUPPORT_AND_PARTNERSHIP_READINESS.md` | CauseWay stewardship note — **not public and not a Design input**; ignore it |
