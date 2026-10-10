# OpenAI re-entry checkpoint — Yemen Financial Inclusion Evidence

**Current state, 4 October 2026.** Non-design v1 product complete. Current phase: design / presentation integration. C1, C2 and C3 are post-v1 owner decisions, not release blockers. Public release is not declared. The active front door is `README.md`. The text below is the September checkpoint and is history.

**Rights, 10 October 2026.** Reuse rights are decided and the question is closed: CC BY 4.0 covers the content CauseWay owns in this resource (adopted 3 October 2026, closed 10 October 2026 — `audit/OWNER_DECISIONS_2026-10-10.md`). The one remaining release step is CauseWay's counsel confirming the CC BY 4.0 text (`docs/RELEASE_RUNBOOK.md` step 7a); `licence_text_confirmed` and `public_downloads` stay `false` until then. A reuse licence is not regulatory licensing: CauseWay is not a licensed financial institution and claims no such status. The repository's software code is outside the CC BY 4.0 licence and no code licence is decided. No rights clearance, legal review or certification is claimed.


**Programme:** Final integration to the Design handoff — directive D7 (`audit/directives/`), sessions F0–F9.
**Position (current):** OpenAI accepted the Tranche C checkpoint on 26 September 2026 (recipient verification 31/31) and
supplied the independent ten-Reading package with directive D7. Sessions F0–F9 are closed: the Reading portfolio is
integrated (F2), the Resource Library decisions are made (F3), R8.5 repository subtraction is closed (F4), the whole
public corpus is accepted (F5), the discovery, accessibility, rights and security contract is in place (F6), the
sustainability baseline is recorded (F7), the Design handoff is frozen (F8) and accepted clean-room (F9). A bounded
post-F9 correction (27 September 2026) closed the two remaining maintainer items and tightened the handoff in place; a
design-enablement control pass the same day (directive D9) strengthened the Design brief, criteria and contract in place
so that a cold Design recipient can run D0–D7 from the repository alone.

**Status: DESIGN HANDOFF READY.**

- R8.4: CLOSED / PASS, Reading prose included (F2). R8.5: CLOSED (F4). R8.6: CLOSED (F8, F9).
- This is not PUBLIC RELEASE READY.
- Claude Design starts at `handoff/README_FIRST.md`. **The Design programme is closed** (D7 accepted at `fca7bf1`,
  the last commit of pull request #7, landed on `main` 28 September 2026 — an ordinary commit, not a merge commit; the
  owner's final visual acceptance recorded 2 October 2026, `audit/OWNER_DECISIONS_2026-10-02.md`) and Code has started on the eleven EAD items: EAD-01 landed the
  one production runtime on 29 September 2026 — `dist/` is the accepted design rendered by `scripts/yfie`, the
  replaced renderer is removed, parity with the pre-design build is proved against a frozen oracle, and EAD-04
  closed with it. This changes no governed content and no programme status: still DESIGN HANDOFF READY, still not
  PUBLIC RELEASE READY.
- Checkpoint tags are not on GitHub yet: this session's git access refuses tag pushes (HTTP 403), so the owner creates and
  pushes them (§7).

**Date:** 2026-09-27.

## 1. Authority state (verify first)

| Item | Value |
|---|---|
| Production Master | `authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx` — SHA-256 `cf5254825da8b06e8812ee0c033382270b731e1001c40bf6ad929f843f27278a` |
| Page Specs | `site-src/content/page_specs.json` — SHA-256 `f0816b90ec014dc255b5f58a580c0445844ad10b1337a6c9331c56fda5e242dd` |
| Entry state recorded with the Drive IDs (lineage, not current) | Master `e69804106e04d093098688f2d01cea51e13191f255d774a090f3e5dd8dec9bc7`; Page Specs `ff2b0f559cde5fede3fe31d7dfb2539a00921e8b00b816c2863790cd9de49007` |
| Master lineage in D7 | `f0150122…` (entry) → `caabff47…` (RP-F2) → `0e8730c2…` / `69899ae2…` (RL-F3, RL-F3b) → `2a7fd52b…` / `440614d7…` (R85-A, R85-B) → `168a0ad8…` / `ed3c5796…` (RF5, RF5b) |
| Canonical repository | GitHub `CausewayGrp/Financial-inclusion-`, branch `main` — the only working copy. The last state OpenAI reviewed is commit `f726bda` (tree byte-identical to `…TRANCHE_C_COMPLETE_READING_HOLD.zip`, SHA-256 `63612dea…`); its tag and the Design-handoff tag are owner actions (§7) |
| Other copies | None is current. The pre-GitHub Drive folder and the ZIPs exchanged before 26 September 2026 are lineage: they were deliberately left as they were — neither updated nor deleted — and are never synchronised from here. `EXTERNAL_REPOSITORY_SYNC_PENDING` in `authority/AUTHORITY.json` records exactly that state; it is not a sync that is owed |
| Generator | `scripts/generate_projections.py`; `PROJECTION CHECK PASS`; 21 of 21 unit tests |
| Build | 286 HTML documents from 142 Page Specs (284 localized + root + 404), and the two pages at the retired address /evidence/NEG-EW-011/ (RC-19) |
| Public-literal audit | 12,760 records, 0 unresolved; identical bytes under 8 `PYTHONHASHSEED` values |
| Source-lineage truth test | 8 of 8 |
| Validator | `WEBSITE REPOSITORY VALIDATION PASS`, 0 errors, 0 warnings (gates through R85-G09, RP-G06, F6-G08 and R86-G04) |
| Browser behaviour tests | `scripts/tests/test_public_tools.py` — 25 passed, 1 not applicable to the current data |
| Viewport acceptance | `audit/tranche_c/checks/viewport_acceptance.py` — 168 of 168 |
| Bilingual numeric invariance | `audit/tranche_c/checks/bilingual_invariance.py` — 0 page pairs differ (CI fails on any difference) |
| Current counts | `site-src/content/content/public_inventory.json` (derived from the Master; the only source for counts) |

The Master and Page Specs hashes in this file, `README.md`, `authority/AUTHORITY.json`, the Context and the handoff
manifest are rebound by `scripts/rebind_authority.py`; validator gate P4-G04 fails if any of them diverges.

## 2. What happened since Tranche C

Every Master change was a transaction committed through `audit/tranche_b_execution/run_stage.py` (regenerate, rebind,
build, literal audit, diagrams, repository manifest, validate, generator check; rollback on any failure).

- **Evidence Readings (F1, F2).** The independent ten-Reading package was adjudicated against the Master and its sources
  (`audit/READING_PORTFOLIO_FINAL_ADJUDICATION.md`, 60-row change ledger) and integrated Master-first (RP-F2). BIL-05
  closed: every English/Arabic page pair prints the same numbers.
- **F3 Resource Library.** Five bounded decisions: one curated card added, two deferred, two rejected
  (`audit/F3_RESOURCE_DECISIONS.md`).
- **F4 · R8.5.** Public copy moved out of `build.py` and `app.js` into the Master's governed interface copy; one path from
  authority to recipient; `FINAL_REPOSITORY_MANIFEST.json` classifies every tracked file; `audit/INDEX.md`; permanent
  gates R85-G01…G09 (`audit/R8_5_REPOSITORY_SUBTRACTION_CLOSURE.md`).
- **F5 public corpus.** Eleven reviewers read every governed public text in Arabic, English and for parity: 667 findings,
  all 57 material applied, 26 rejected under two house rulings, 3 deferred as source checks; scope qualifiers restored in
  Arabic, firewall errors fixed, three unsupported periods corrected from the records' own sources, control language
  removed, one duplicate source record retired, the chronology put in date order (`audit/F5_PUBLIC_CORPUS_ACCEPTANCE.md`,
  `audit/F5_CORPUS_FINDINGS_LEDGER.csv`).
- **F6 discovery, accessibility, rights, security.** Self-canonical, reciprocal hreflang with `x-default`, pre-release
  `robots.txt`, sitemap derivation for when the owner sets the public origin, JSON-LD with governed fields only; a strict
  Content-Security-Policy is now possible (no inline script or style); eleven WCAG 2.2 outcomes specified for Design and
  Code; gates F6-G01…G08 (`audit/F6_DISCOVERY_ACCESSIBILITY_RIGHTS_SECURITY_ACCEPTANCE.md`, `docs/DEPLOYMENT.md`).
- **F7 sustainability and stewardship.** Measured baseline of the reference build (`audit/SUSTAINABILITY_PRE_DESIGN_BASELINE.json`):
  the 10 MB master logo is 96–99 % of every cold page (release-only derivatives, TOOL-02); without it 0.09–0.45 MB in
  four requests. Method in `docs/SUSTAINABILITY_METHOD.md` (no carbon figure, budget or badge before Design). Non-public
  stewardship note `handoff/SUPPORT_AND_PARTNERSHIP_READINESS.md` (independence covenant, DPG gap assessment).
- **F8 · R8.6 handoff freeze.** One start file (`handoff/README_FIRST.md`) with a single reading order; one Design prompt
  (22 requirements, 24 sections, deliverables `design/00`–`10`); the Code prompt waited for the Design package (it no
  longer waits: the package is accepted and Code has started, 2 October 2026, `audit/OWNER_DECISIONS_2026-10-02.md`); the
  route, content and state inventory (`handoff/ROUTE_CONTENT_AND_STATE_INVENTORY.json`, 142 routes, 12 hard-state cases,
  13 journeys, 14 technical states) generated by `scripts/handoff_inventory.py`; `handoff/DESIGN_ACCEPTANCE_CRITERIA.md`;
  the Design → Code contract; `handoff/ENGINEERING_HANDOFF_EXPECTATIONS.md`; three superseded drafts retired to
  `audit/prior-review-records/handoff-drafts-2026-09-26/`; Open Graph metadata; gates R86-G01…G04; open items classed in
  `FINAL_OPEN_ITEMS_REGISTER.md` with zero DESIGN_BLOCKER (`audit/R8_6_DESIGN_HANDOFF_FREEZE_CLOSURE.md`).
- **F9 · clean-room acceptance.** Three fresh agents, each with only a clone of `main`, acted as Claude Design in a dry
  run; none found a blocker, every command passed, and their 34 material points were fixed or given explicit rules
  (RF9 moved the last two interface labels out of code; inventory 1.3; precedence and contract-disagreement table; the
  reference implementation's location and `YFIE_SITE_DIR` test path; the test-hook contract; fonts vendored in
  `vendor/fonts/`). The archive, extracted into an empty directory without `.git`, passes every gate
  (`audit/FINAL_CLEAN_ROOM_ACCEPTANCE.md`). File counts: the checksum and manifest counts cover every tracked file except
  `SHA256SUMS.txt` itself. That record's archive test ran on `2922449` and counted 753 (754 tracked); the final F9 commit
  `03bd654` added the record itself, so its manifests count 754 (755 tracked). Both are correct for their commits; the
  record is not rewritten (its addendum explains the difference). The post-F9 correction adds the D8 directive (755); the control pass adds the D9 directive (756).
- **Post-F9 correction (27 September 2026;** directive `audit/directives/D8_POST_F9_CORRECTION_2026-09-27.txt`**).** OWN-07 closed: `/remittances/` now shows its bound Measurement card
  (MA-001, people-side; household remittance receipt) in both languages, distinct from the macro series. OWN-08 closed:
  the stale descriptive fields of `navigation_interaction.json` corrected against governed copy, Page Specs and tests
  (report path, Reading breadcrumb, Compare dimensions and comparable set, workbench — Evidence Passports stay non-public
  — three hard-state sentences, journey J10). The two hand-maintained contracts are classed `CONTROLLED_CONTRACT` with
  their edit rule in the file, `AGENTS.md` and `CONTRIBUTING.md`. The Design handoff was tightened in place: competing
  theses at D1 on Home, a dense Evidence Record and the flagship Reading before propagation; a decision log and coverage
  ledger across D0–D7; the runnable, fully populated bilingual reference site as the D7 completion requirement, with no
  placeholder in the accepted site; print and portable-evidence requirements; font loading without an unapproved subset;
  a D0 statement on whether any visual board or mockup was supplied. No Master change.
- **Design-enablement control pass (27 September 2026;** directive
  `audit/directives/D9_DESIGN_ENABLEMENT_CONTROL_PASS_2026-09-27.txt`**).** The handoff was checked against a quality
  doctrine for a cold Design recipient and strengthened in place — one start file, one brief, no second programme: a
  re-readable kernel, a nine-step working loop, a gate-start re-read and gate-end commit rule and the Code recipient test
  (brief §0); the connected evidence system (§4.6); the firewall's lineage and layout rules (§5); explicit freedoms and
  ownership (§6); tone, motion, imagery, dark-mode logic and four review tests (§7); audience lenses and per-family
  outcomes including a Home cold-reader test (§9.3–§9.4); search, inputs, reporting intents, per-object export formats,
  third-party rights, data packages and micro-interactions (§10); interactive visuals (§12); Arabic testing (§13); low
  bandwidth and footprint (§15); decision-log fields, a coverage ledger with a status ladder and checks, a design-debt
  register, the four layers and the hostable static site (§19); gates with entry, exit and stop conditions and a
  last-10-percent audit (§20). The acceptance criteria (new section K), the Design-to-Code contract and the Code reading
  order match. No Master, projection, contract or public-page change. Second addendum in
  `audit/FINAL_CLEAN_ROOM_ACCEPTANCE.md`.

Tranche C itself is recorded in `audit/TRANCHE_C_FINAL_ACCEPTANCE.md` and `audit/TRANCHE_C_FINDINGS_LEDGER.csv`.
Currentness cut-off: 26 September 2026 (`audit/FINAL_CURRENTNESS_CUTOFF.md`); release-candidate recheck of 3 October 2026 appended there (edition of 3 October 2026).

## 3. House rulings carried forward

Recorded in `audit/F5_PUBLIC_CORPUS_ACCEPTANCE.md` §3 and binding on later editing: «فريد / الفريدين» for unique counts;
«التحويلات» for remittances as a macro flow and «الحوالة / الحوالات» for individual transfers, their prices, domestic
person-to-person remittances and the exchange-and-remittance sector; "the evidence base holds no …" (missing here is not
non-existent); «أول تعامل مع …» for first contact; «مستمر» for durable use; «قاعدة الاحتساب»; one Arabic name for the
OECD; CBY-Aden's full name at first mention; "edition", not "content version"; Evidence Record and visual twins stay
identical.

## 4. Open items carried forward (not defects of this state)

Every item, with its class, where it shows, what closes it and its owner, is in `FINAL_OPEN_ITEMS_REGISTER.md`
(47 items: 11 engineering after Design, 4 release-only, 11 external evidence dependencies, 8 known evidence frontiers,
6 owner inputs, 7 rejected / no action; **zero DESIGN_BLOCKER**). F8 built it from a sweep of every earlier record that
left an item open and checked each against the current bytes; the items closed since are listed there so they are not
reopened (among them OWN-07 and OWN-08, closed on 27 September 2026).

- **Sessions:** the Design programme is complete (D7 accepted by the owner, 2 October 2026) and the production runtime is merged (pull request #8). The release-candidate pull request (#9) implements the owner's decisions of 2 October 2026; the work after it is release-time only (`FINAL_OPEN_ITEMS_REGISTER.md` §2: hosting and public origin, live security headers, the currentness re-run at the release date, the owner's release acceptance).

## 5. Re-run

```
python3 scripts/checksums.py --check
python3 scripts/generate_projections.py --check
python3 -m unittest discover -s scripts/projection/tests -t .
python3 scripts/build.py && python3 scripts/audit_public_literals.py && python3 scripts/validate.py
python3 scripts/tests/test_literal_audit_determinism.py
python3 audit/pre_tranche_c/source_lineage_truth_test.py
python3 scripts/tests/test_public_tools.py                 # needs Python Playwright + Chromium
python3 audit/tranche_c/checks/viewport_acceptance.py       # needs Python Playwright + Chromium
python3 audit/tranche_c/checks/bilingual_invariance.py
python3 scripts/architecture_diagrams.py --check
python3 scripts/repository_manifest.py --check
python3 scripts/handoff_inventory.py --check
```

## 6. Boundaries kept

- One authority. Every content change went into the Master first through the runner. No generated projection was
  edited by hand; the two controlled contracts (`presentation_priority.json`, `navigation_interaction.json`) were
  corrected in place by the steward, as their maintenance rule allows, and validated by the generator.
- Nothing closed earlier in the programme was reopened without a recorded finding.
- **Not claimed:** native Arabic certification, legal review, WCAG conformance, rights clearance, security guarantees,
  service levels.
- No repository other than the canonical GitHub repository was written to: the pre-GitHub Drive copies were left
  untouched as lineage.

## 7. Owner actions

- **Push the checkpoint tags** (this session's git access refuses tag pushes). From a clone with signing set up:

  ```bash
  git fetch origin
  git tag -s checkpoint/tranche-c-complete-reading-hold f726bdaf305f21930b5fb7dfb8a649ad102e089c \
      -m "Tranche C complete — Reading prose held for the independent Reading package" \
      -m "Tree byte-identical to Yemen_Financial_Inclusion_Evidence_TRANCHE_C_COMPLETE_READING_HOLD.zip (SHA-256 63612dea…; full value in audit/directives/D7_FINAL_INTEGRATION_TO_DESIGN_HANDOFF_2026-09-26.md)"
  C=$(git log origin/main -1 --format=%H -F --grep='docs(handoff): design-enablement control pass')
  git show -s --format='%H %s' "$C"            # check it before tagging: 6d954c17…
  M=$(git show "$C":authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx | sha256sum | cut -c1-64)
  echo "$M"                                     # check it: the Master bound at that commit begins 17db032b15da
  git tag -s checkpoint/design-handoff-ready "$C" \
      -m "DESIGN HANDOFF READY — R8.6 closed; post-F9 correction and design-enablement control pass applied" \
      -m "Master $M"
  git push origin checkpoint/tranche-c-complete-reading-hold checkpoint/design-handoff-ready
  ```

  The design-handoff tag goes on the commit Claude Design starts from: the design-enablement control-pass commit
  (subject `docs(handoff): design-enablement control pass …`, recorded in `docs/CHANGELOG.md` and in the second addendum
  to `audit/FINAL_CLEAN_ROOM_ACCEPTANCE.md`), whose parent `937bf80` is the post-F9 correction commit — not on whatever
  `main` has become since; never move an existing checkpoint tag. The tag names the Master bound at that commit, read from the
  commit itself, never the current Master: a Master transaction since then must not change what the tag records. `.github/workflows/checkpoint.yml` then rebuilds and verifies the archive and attaches it to a
  pre-release.
- **The owner and release items** in `FINAL_OPEN_ITEMS_REGISTER.md` (OWNER_INPUT and RELEASE_ONLY).
