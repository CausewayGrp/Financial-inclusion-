<!-- Committed copy of the owner's takeover brief of 17 October 2026 (PR-C). One row, F-12, is redacted while the repository is public (OD-1017-13). Otherwise verbatim. -->

# YFIE — CLAUDE CODE TAKEOVER BRIEF · 17 October 2026

**Yemen Financial Inclusion Evidence · أدلة الشمول المالي في اليمن**
Repository: `CausewayGrp/Financial-inclusion-` (public), branch `main`.
Run with the strongest model available, at maximum reasoning. You are the lead and the only writer.

You are taking over from several agents: earlier Claude sessions, and two other agents (Codex and Grok) that committed
as "Maher" / "MaherFSF" and as "tech@causeway". **On 17 October 2026 the owner archived Codex and Grok. From now on
you are the only agent that writes to this repository.** You run locally, in the owner's VS Code, on a clone the
owner has just pulled; you push to GitHub yourself.

**You own the outcome.** Like a chef who walks back into a kitchen after a night away, you find work in progress:
some good, some half-done, some wrong. Taste everything before you serve it. This brief gives you the verified
situation and my recommendations. You may override any recommendation when the repository or the reader evidence
shows a better answer: record why in one line, and carry on. What you may not override are the hard rules (AGENTS.md,
and Part 10).

Your mission is to finish the product from where it stands:

- **Stage B:** structure, tools, design, visuals and footprint.
- **Stage C:** governance, README pair, SEO, editorial pass and acceptance.

You end on a main that is **hosting-ready in the host-neutral sense defined in Part 8**. Then you stop.

The allowed final status is **CLAUDE MATURATION HAND-BACK READY — ONLY HOSTING REMAINS**. Never declare DESIGN
HANDOFF READY or PUBLIC RELEASE READY. Never deploy.

This brief was written by the owner's advisor after an independent check of the live repository on 17 October 2026.
Everything in Part 2 was verified from bytes, GitHub and a local gate run on that date. Re-verify it; do not trust it.

---

## PART 0 — START HERE

1. Commit nothing until step 7.
2. Read, in order: `AGENTS.md`, `CLAUDE.md`, `README.md`, `CONTRIBUTING.md` (§4 Master transactions, §5 gates),
   `authority/CORE_CONSTITUTION.md`, `authority/YFI_CURRENT_PROJECT_CONTEXT.json`.
   Then read, for the stages you are about to run, `audit/close_out/BRIEF.md`:
   - the execution plan;
   - W4, W4F, W5, W6, W6S, W7, W8;
   - Appendices F, G, H, I.
   Read history only to answer a named question.
3. Run:
   ```bash
   python3 scripts/reentry.py --pr
   git fetch origin && git status
   python3 scripts/checksums.py --check && python3 scripts/generate_projections.py --check && python3 scripts/validate.py
   sha256sum authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx site-src/content/page_specs.json
   ```
4. Compare with Part 2.
   - Expected movement: main may have advanced because PR #52 or #53 merged. Reconcile that and continue.
   - **STOP and report** only if the Master hash changed through a commit that is not a recorded transaction, or if
     main contains commits touching `authority/` that Part 3 does not explain.
5. **Local environment** (you set it up; the owner only pulled the repository):
   - Python 3.11 is what CI pins. Create a virtual environment with 3.11 if it is installed; otherwise use the
     available 3.12/3.13 and record it (the gates passed on 3.13 in the advisor's run).
   - `pip install -r requirements.txt`, then `python -m playwright install chromium`.
   - Node.js is optional (`npm run serve` only). nginx and Docker are not needed: hosting tests are optional.
   - Check `git config user.name` / `user.email` and that `git push` works. If push is refused, tell the owner the
     exact error and wait; nothing else in this brief can be done without it.
   - Run `gh auth status`. If `gh` is available and authenticated, use it for PRs, checks and merges. If not, push
     branches and ask the owner to open or merge the PR in the browser, giving the exact title, body and branch.
6. **Skills.** Precedence is: the owner's instruction (this brief) > AGENTS.md / CONTRIBUTING.md > any skill.
   - Load `multi-agent-m` (CLAUDE.md asks for it). **This brief is its SPEC and its intake: do not re-interview the
     owner and do not stop for "owner approves direction".** Its "foundations" phase means the repository's existing
     gates: add no new linter, formatter, type checker or framework. Use its model routing, delegation contract,
     verification ladder and token discipline.
   - `digital-experience-director` will probably auto-load in Stage B. **Use only its craft modules**:
     - `studio/epistemic-grammar-v2.md`, `studio/page-grammar-library.md`, `studio/interaction-data-patterns.md`;
     - `studio/unique-product-patterns.md`, `studio/typography-lab.md`, `studio/navigation-typography-rtl.md`;
     - `localization/arabic-editorial-review.md`, `localization/rtl-test-matrix.md`;
     - `assurance/preservation-and-qa.md`, and `scripts/compare_preservation.py` / `scripts/browser_snapshot.mjs`.

     **Ignore** its `projects/yfie-*` files (stale: wrong labels, "Evidence Passport" as a public term, no
     Master-first rule), its owner-approval gates, its "do not commit/branch" defaults, its templates and dossiers,
     and its WCAG "pass" vocabulary.
   - Do not load `impeccable`, `apple-design`, `theme-factory` or other design-direction skills. The direction is the
     charter (Appendix 1) plus the V1 tokens. `frontend-design`, `web-excellence` and `webapp-testing` are allowed for
     craft and testing.
   - Do not invoke `yfie-capability-architect`. Changing the agent operating layer is out of scope.
7. **Session plan.** This is several Claude Code sessions, not one. Plan them, and end each at a clean boundary:
   - **Session 1:** Phase 1 (PR-A, PR-B, PR-C, PR-D).
   - **Session 2:** G0, plus deciding the Part 6 hypotheses.
   - **Session 3:** S.
   - **Session 4:** T, then G1.
   - **Session 5:** G2.
   - **Session 6:** W4F and G3, then the Stage B report.
   - **Sessions 7–8:** Stage C and hosting readiness.

   At each boundary:
   - PROGRESS.md carries the state;
   - run `/compact` when context is heavy, or tell the owner "start a new session with the resume message" (Part 9).

   Keep CLAUDE.md as it is; put no run notes in it. Delegate any reading over about 20k tokens to subagents that
   return conclusions. Use plan mode only for the G1 decision and the Stage C README structure.
8. Execute Part 5 in order. After each phase, append to `audit/close_out/PROGRESS.md` and send the owner a short
   report. Then **continue without waiting**, unless a stop condition in Part 10 applies.

---

## PART 1 — OWNER DECISIONS CARRIED BY THIS BRIEF (17 October 2026)

The owner sends this brief. Sending it is the owner's dated decision.

In PR-C (Part 5), commit Part 1 verbatim as `audit/OWNER_DECISIONS_2026-10-17.md`. These decisions use new
identifiers, `OD-1017-nn`.

They do **not** recover or reuse D19–D22. Two incompatible "D16–D22" lineages exist (finding F-01): an advisor message
of 10 October used D16–D22 for different things than the repository's D16–D18. Never cite D19–D22 again.

**OD-1017-01 — Stage B entry is authorized now.** The SB-01 conditions are met:
1. Stage A content acceptance is effective. The dated decision comment is on PR #49: accepted main `19384b27`,
   Master `580d2dc1…`.
2. D19–D22 are neutralized (PR #52).
3. This decision is the separate owner entry instruction.

Stage B scope:
- `audit/close_out/BRIEF.md`: W4 (G0 → S → T → G1 → G2 → W4F → G3), Appendix F (S1–S13, CR-S12) and Appendix G.
- The Stage B Design Charter v3.2 in Appendix 1, as the operative charter. Commit it as
  `audit/close_out/STAGE_B_DESIGN_CHARTER_v3_2.md`.

To the 15 October prospective charter (`audit/close_out/STAGE_B_DESIGN_CHARTER.md`), append one dated line pointing
to v3.2 and to this decision. Rewrite nothing in it.

Its substantive constraints remain in force:
- SB-02: no new CWR-012 channel visual on current evidence;
- CWR-013 stays reserved;
- the two-Reading domain rule and the CWR-011 placement stay;
- no new route families, no new Reading, no new research section.

**OD-1017-02 — Stage C entry is authorized to follow Stage B without a further owner message.** Scope: BRIEF W5, W6,
W6S, W7 and W8, as amended in Part 7.

**OD-1017-03 — Steward scope for this run.** D14 is extended to this run for the following edits:
- `navigation_interaction.json`: the edits required by S rules, CR-S12/D8 and recorded DL-V2 decisions;
- `presentation_priority.json`: the TOC tiers and caps (S5, S10).

Each such edit is its own commit, names its finding, and runs every gate.

**OD-1017-04 — Provisions re-adopted under new IDs.** These were drafted by the advisor on 10 October and never
entered the repository. They are re-adopted prospectively as follows:
- **(a) Cite tool.** Formats: plain text, APA 7, Chicago, BibTeX and RIS. Each carries the record ID, the edition and
  the access date. A test parses the BibTeX and the RIS. Stage B, T.
- **(b) SDG correspondence.**
  - Name an SDG indicator only where the record's indicator is definitionally identical to the UN metadata, with the
    UN metadata locator in the record's method note. Today that means 8.10.2 on CLM-001, and 10.c.1 where it is
    already stated.
  - On CLM-001, state what the World Bank's 8.10.2 value for Yemen covers. Establish this by SOURCE → VERIFY:
    - the DDI/fixture shows valid=0 only for some mobile-money usage variables (`fin13a`, `fin17a1`, `fin34b`,
      `fin39b`, `fin43b`), while `fin5` has 153 valid cases;
    - CO-G04 allows "did not ask" only where DDI valid==0 for that variable;
    - CLM-001 already says no mobile-money value is published.

    Write the sentence the evidence supports. Do not use a pre-decided text.
  - 8.10.1: record in the Measurement Agenda's access dimension that no value is held after 2015 (missing ≠ zero),
    after verifying it against the IMF FAS / WDI series. A 2015 value appears only as dated history.
  - Master-first, EN and AR. Stage B, S.
- **(c) README pair.** `README.ar.md` is written first, as Arabic, in the 17-section order of Part 7. `README.md`
  follows the same order, written for English readers. Stage C, W6.
- **(d) Social cards.**
  - Add a template fingerprint (frame CSS, font files, logo bytes) to the social-image index, compare it in
    `--check`, and add one negative control.
  - Generation becomes incremental; `--all` forces a full redraw.
  - Redraw stale cards in the same commit that made them stale.
  - Full redraws happen only at the Stage B freeze (G3) and at hosting. Record the repository size before and after
    each.
- **(e) Audience task suite.** Ten persona walkthroughs on the final build, in Playwright, AR and EN, at 390 and 1440,
  recording success, clicks, time and a screenshot. A failed task is a finding. Stage C, W8. Personas and tasks are
  in Part 7.
- **(f) CODEOWNERS.** Notification only. `REPOSITORY_SETTINGS.md` must never require code-owner review: with a single
  maintainer, that would block every merge.

**OD-1017-05 — Hosting stays unselected.** The owner decision of 16 October 2026 (`audit/OWNER_DECISIONS_2026-10-16.md`,
in PR #53) stands.
- No deployment, cloud account, registry, DNS change, purchase or corporate-site change.
- `public_origin` stays null, `pre_release` stays true, `public_downloads` stays false.
- "Hosting-ready" means Part 8.

**OD-1017-06 — Merge authority.** You may merge a PR yourself by a normal merge, only when all of these hold:
- exact-head Verify shows all nine required jobs green;
- the PR body carries the scope review and the gate list;
- nothing is overridden or weakened.

You may never use an admin override, never merge another agent's PR without the review in Part 3, and never merge a
PR whose Verify jobs are red, pending or cancelled.

**If GitHub CI cannot run** (billing refused, F-13), the evidence for a merge is a full local gate run, recorded in
the PR body with each command's last line:
- CONTRIBUTING §5;
- all negative controls (`test_gate_negative_controls.py` without `--only`);
- the browser suites.

Tell the owner once. Re-run CI on `main` when it is available again, and fix forward if anything fails. Working
locally and pushing a branch when its gates pass is the normal rhythm: pushing is how work becomes safe.

**Only Verify's nine jobs count.** The external "Workers Builds: financial-inclusion" check fails on every commit (F-06).
It is not required. Ignore it. If the platform refuses the merge, comment "READY TO MERGE — exact head
<sha>, Verify 9/9", tell the owner, and continue with work that does not depend on it.

**OD-1017-07 — Dispositions of other agents' work.** As set out in Part 3.

PR #52 edits two audit records in place: the D19–D22 rows of `AMENDMENTS_D16_D22.md`, and the status line and
condition 2 of the 15 October charter. The owner accepts those in-place edits as the owner's own act of 17 October
2026, an explicit exception to append-only. Record that in `audit/OWNER_DECISIONS_2026-10-17.md`. No other record is
rewritten.

**OD-1017-08 — Plain-language page leads (repository D18).** Delivered in Stage B S, through Master transactions, with
the persona checks in G0/G3. Not a new route or layer.

**OD-1017-09 — Owner defaults that stay in force unless the owner says otherwise:**
- the Cash Consortium of Yemen keeps its qualified current Arabic name (ADD3-O1 stays OWNER-OPTIONAL);
- downloads off and request counts off;
- no analytics or cookies;
- D16 aggregates stay unpublished without an approved aggregate input;
- the FRONTIER evidence states are retained;
- cosmetic font work deferred;
- manual AR/EN accessibility acceptance stays release work.

**OD-1017-10 — Stops are only those in Part 10.** Stage reports are informational; the owner can veto after the fact.

**OD-1017-14 — Decide; do not ask.** When a question arises, answer it in this order of priority:
1. truth and evidence safety (the semantic firewall, Master-first);
2. the reader's success on the task;
3. reversibility;
4. the smallest change that achieves it.

Then record the decision in one line and proceed. Never ask the owner something the repository, this brief or a
dated owner decision answers. Ask only the Part 10 owner-only items, each with your recommended default.

**OD-1017-11 — Single writer.** Codex and Grok are archived (17 October 2026). Claude Code, run by the owner locally,
is the only agent that writes to the repository.

Divergence means **a commit on `main` or an open PR that this session did not create**. Authorship cannot tell writers
apart: all agents used the owner's identities. Exceptions:
- **Dependabot PRs** are not divergence. Close them with a one-line note, or merge them after Verify if they only bump
  pinned Actions.
- The owner's own merges of your PRs are not divergence.

**OD-1017-12 — Stage A residue is authorized.** The verified content defects in Appendix 2 that are still true on
main are corrected by Master transactions before Stage B's G0. This is not a reopening of Stage A: each fix is an
adjudicated defect with evidence, EN and AR together, and the Stage A acceptance scope otherwise stands.

**OD-1017-13 — Repository visibility and CI economy.** The repository is public. The owner is told that this exposes
material held non-public (F-12), and decides visibility in the GitHub settings. CI billing failed on 16 October (F-13).
- **If the repository is private when you start** (`gh repo view --json visibility`, or ask the owner):
  - The owner's preferred fix is to repair billing or the spending limit. Then CI stays exactly as it is.
  - If the owner instead asks you to cut CI cost, the only acceptable change keeps every control before `main` moves:
    - the negative-control shards run on non-draft PRs and on `main`;
    - draft PR pushes run Governance and Browser only;
    - `controls-result` treats "skipped because draft" as neutral **only on draft events**;
    - add a negative control proving a ready PR cannot pass with skipped shards.
  - Work in draft PRs until ready, run `test_gate_negative_controls.py` locally first, paste the result line into the
    PR body, then mark it ready.
  - `verify.yml` already has a `concurrency` block; keep it.
  - Record the change in CONTRIBUTING §5.
- **If it stays public:** CI is free. Leave the workflow as it is, keep working, and repeat F-12 in each phase report
  until the owner decides.

---

## PART 2 — VERIFIED STATE AT HANDOVER (17 October 2026, about 03:30 UTC)

| Item | Value |
|---|---|
| `main` | `274583df616a38d516b2d0f78178167235b7f755`: PR #50 (agent continuity, public-path correction), 16 Oct |
| Production Master SHA-256 | `580d2dc19054658d906585104b957a0fe9f4f3ce4758e6bc19b1cae28fb28bc8` (= the accepted Stage A Master) |
| Page Specs SHA-256 | `8dd600e940f26213c658c5f3188e8e63e16201e2e588d7379bb1db6d46b9068e` |
| CI on `main` | Verify 9/9 (governance, browser, six negative-control shards and their aggregate) |
| External check | **"Workers Builds: financial-inclusion" fails on every commit** (Cloudflare app). Not required, not ours to fix in code: F-06 |
| Repository | **Public** (made public around 16 Oct, after private-repository Actions billing failed; F-12, F-13). No tags exist on GitHub. 47 branches besides `main` |
| CI billing | On 16 Oct 17:41 UTC a job was refused: "recent account payments have failed or your spending limit needs to be increased". One full Verify run costs about two runner-hours (six negative-control shards of 13–25 min each) |
| Open PRs | #51 draft, homepage editorial pilot, head `64dca58b`, Verify green. #52 ready, D19–D22 neutralization, head `d5f78137`, Verify green. #53 draft, hosting-neutral + privacy transaction, head `6fa672f3`, Governance and Browser green, shards were finishing |
| PR #53 Master | Verified cell by cell: exactly 4 cells change: `03_PAGE_SECTIONS` rows 212–213, `/privacy/` §3 and §4, `body_en` and `body_ar`. Master after = `620f3368…` |
| Inventory (generator) | 151 Page Specs → 306 HTML; 116 Evidence Records; 60 public claims; 55 passports; 12 Readings; 10 measurement priorities; 11 entry questions; 31 dated events; 42 visual contracts; 206 sources (191 with a public locator); 28 curated resources; 522 search records |
| Live register | 299 items: CLOSED 92 · HOSTING 9 · FRONTIER 47 · OWNER-OPTIONAL 12 · DECIDED 139 |
| Stage A | Accepted on PR #49 (comment of 15 Oct 12:39 UTC) at main `19384b27`, within `audit/stage_a_final/ACCEPTANCE_SCOPE_2026-10-15.md` |
| Stage B / C | **Not started.** None of these exist: `design/DESIGN_INTEGRATION_V2.md`, `design/exploration/v2/`, `README.ar.md`, `SECURITY.md`, `CITATION.cff`, `LICENSE.md`, `docs/REPOSITORY_SETTINGS.md`, `docs/CORRECTIONS_PROCESS.md`, `docs/REPOSITORY_MAP.md`, `.github/workflows/housekeeping.yml`, `.github/workflows/currentness.yml`, `audit/close_out/QA_CHECKLIST.md`, `.github/CODEOWNERS`. The cite tool has no BibTeX or RIS. No public page names SDG 8.10.2. Social images have no template fingerprint |

**Local gate run on `274583df`, advisor sandbox, Python 3.13, Playwright Chromium.** All PASS:
- reentry;
- checksums;
- projections `--check`;
- generator unit tests;
- test_reentry;
- test_public_path_documentation;
- build (tree clean after);
- literal audit;
- validate.py (`HTML=306 ERRORS=0 WARN=0`);
- manifest `--check`;
- literal determinism;
- source-lineage truth test;
- diagrams, social and logo `--check`;
- bilingual invariance;
- content parity;
- test_stage_a_reconciliation;
- test_public_tools;
- viewport_acceptance;
- test_security_headers;
- test_base_path;
- test_no_javascript.

Not run locally: negative controls (CI ran them green), nginx/Docker hosting, exports, cutover parity (expected exit 2, "pinned").

**Phone-length baseline (your G0 starts from this; re-measure it yourself).** Chromium, `scrollHeight` divided by the
viewport height.

| Route | AR 390×844 screens | EN 390 | EN 1440×900 | Brief target / note |
|---|---|---|---|---|
| Home | 8.5 | 8.4 | 5.5 | P1 first screen; shorter |
| /explore/ | 14.5 | 14.1 | 11.4 | — |
| /people/ | 20.1 | 18.8 | 13.4 | domain −25% or better |
| /payments/ | 26.8 | 25.7 | 17.7 | −25%; **TOC has 13 entries** (S10: ≤6); H1 4 lines AR, 5 lines EN desktop (S11) |
| /remittances/ | 24.4 | 22.0 | 15.0 | −25% |
| /evidence/ | 29.5 | 29.1 | 25.1 | EN ≤14 |
| /evidence/CLM-001/ | 9.0 | 8.4 | 4.8 | P1 holds best here today |
| /readings/how-money-reaches-households/ | 37.2 | 35.6 | 23.6 | reduce chrome and tables only; governed prose untouched |
| /data/ | **70.5** | 68.1 | 53.9 | **≤20**. It was "about 55" when the brief was written: it got worse |
| /methodology/ | 25.5 | 25.4 | 18.9 | TOC ≤6 |
| /measurement/ | **44.7** | 43.5 | 29.1 | −40% |
| /finance/ | 17.0 | 16.3 | 10.9 | — |
| /evidence/compare/ | 11.0 | 10.3 | 6.2 | — |
| /about/ | 6.6 | 7.2 | 4.1 | — |

No horizontal overflow at these widths.

On /data/ and /measurement/, the in-page tab strip is cut off at the phone edge. That is the intended scroller, but it
reads as clipped: judge it in G0.

---

## PART 3 — WHAT THE OTHER AGENTS DID, AND WHAT YOU DO WITH IT

**Status: Codex and Grok are archived (17 Oct); nothing more will come from them.**

**Attribution.** After Claude's last merged PR (#46, CO-G07/CLOSE-6G, merged 14 Oct at `e46ff9eb`), commits came from
agents committing under the owner's identities ("Maher", "MaherFSF", "tech@causeway"). The bytes do not say which tool
was which. Judge the work, not the author.

**Overall verdict.** The work is careful, honest in its claims, and every claim I checked held: PR #53's four cells,
main's gates, the Stage A acceptance record. Its weakness is proportion. In six days, it produced one privacy text and
one homepage pilot as reader-visible change, and a great deal of governance prose. Your job is the product. Keep their
discipline; do not continue their paperwork.

| Item | What it is | Its state | Your disposition |
|---|---|---|---|
| #47 `1fedcf8d`/`6b8e3286` | Post-PR46 baseline and count reconciliation (docs) | Merged | Keep |
| #48 `4f7221cc` | CI export containment: artifact uploads suspended | Merged | Keep. Note F-05 |
| #49 `bbf919b7` | STAGE-A-FINAL Master transaction (`87dafc6f` → `580d2dc1`, 49 cells): edition and checking chronology separated; unsupported IMF missing-value and Findex-contradiction claims withdrawn; four domain-figure record actions removed | Merged; Stage A accepted on it | Keep; this is your accepted content baseline |
| #50 `62b23f7e`…`29075c47` | `scripts/reentry.py`, `test_reentry.py`, PR template, public-path doc test; README and AGENTS.md rewrite. One CI failure on the way (`fb27efee`, validator), fixed | Merged at `274583df` | Keep. Use `reentry.py` every session |
| #52 `d5f78137` | Neutralizes D19–D22 (owner, 17 Oct): docs, Context, charter wording | Open, ready, Verify green | **Merge first** (PR-A) |
| #53 `18ed4f3f`…`6fa672f3` | Hosting-neutral: deploy workflow disabled; nginx/DO tests moved to an optional workflow; new portable `test_http_contract.py`; `_headers` and `deployment.json` neutral; owner decision of 16 Oct; Master transaction on /privacy/ (4 cells, verified) | Draft; check Verify on its head | **Review, then merge** (PR-B). Check items are below |
| #51 `13730a75`…`64dca58b` | Homepage-only editorial pilot: scoped `.home-editorial` CSS in `theme.py`, `render.py` changes, `test_homepage_editorial.py`, before/after proof. Two CI failures on the way (manifest/checksum order; negative controls), fixed | Draft, Verify green | **Do not merge.** Use it as challenger evidence in G1; see below |
| `improve/ci-gov-20261016` `24af5442` | verify-fast and verify-full workflows, CODEOWNERS, issue and PR templates, SECURITY, Dependabot changes; badges "pending" | No PR; based on the old main `19384b27` | Do not merge. W5 does governance properly. Archive and delete via Housekeeping |
| `work/privacy-runtime-notice-20261015` `7e2cf997` | A push-triggered workflow that tarred every tracked file except `dist/` and uploaded it as an Actions artifact (1-day retention). **It ran successfully twice on 15 Oct**, after #48 had suspended artifact distribution | No PR | Do not merge. Record F-05. Archive and delete via Housekeeping |
| ~40 older branches (`close-out/*`, `code/*`, `claude/*`, `design/*`) | Merged or superseded work | — | Housekeeping (W5): archive tags, then deletion by the owner's run |

**PR #53 review checklist.** Every item must pass before you merge:
1. The Master diff is exactly the 4 privacy cells. Re-run the cell diff yourself.
2. No required gate is lost: the Verify job list must not shrink without a replacement of equal strength. Check that
   `test_http_contract.py` really rejects a missing header (its negative control).
3. No public page still asserts DigitalOcean, App Platform or the causewaygrp.com route as current. The docs may
   mention them only as history.
4. `README.md`, `docs/DEPLOYMENT.md` and `docs/RELEASE_RUNBOOK.md` say "unselected" consistently.
5. Exact-head Verify is 9/9.

As the branch stands, item 4 fails: `README.md` (about line 101) still lists the DigitalOcean account and the
corporate proxy route as hosting blockers, and the runbook still holds the full DigitalOcean procedure. Commit
`18ed4f3f` also changes the Master without the `Transaction` / `Master-Before` / `Master-After` trailers that
CONTRIBUTING §3 requires.

So: do not edit the other agent's branch.
1. Create `pr/hosting-neutral-finish` from `6fa672f3`.
2. Fix README and runbook wording. The runbook's DigitalOcean procedure moves under a dated "historical adapter"
   heading.
3. Record the missing trailers in the PR body and the merge commit message (`Transaction: HOSTING-NEUTRAL-PRIVACY`,
   `Master-Before: 580d2dc19054`, `Master-After: 620f3368eaf3`).
4. Open it as the PR to merge, and close #53 pointing to it.

**Conflicts between #52, #53 and #51** (`SHA256SUMS.txt`, `FINAL_REPOSITORY_MANIFEST.json`, `docs/CHANGELOG.md`,
`dist/**`): never hand-resolve generated files. Take either side, then:
- rebuild;
- regenerate the manifest, then the checksums;
- merge CHANGELOG entries by hand, keeping both.

**PR #51 handling.** Its judgement is good:
- each homepage observation carries its exact bound limitation sentence, period, universe and record link in one
  reading unit;
- the domain links sit in the main content;
- card fills, decorative numbering and the competing sidebar are removed.

But it lengthens the phone homepage (AR 7,190 → 8,570 px, EN 7,117 → 8,882 px). The owner's main complaint is long,
heavy phone pages. It also commits homepage-only CSS before G1 has chosen a direction.

So:
- in G1, treat it as evidence for candidate (b) editorial-interpretive;
- copy its proof folder reference into DL-V2-001;
- after DL-V2-001 is recorded, close #51 with a comment saying which of its ideas the chosen direction adopted.

Do not delete its branch yourself; Housekeeping archives it.

---

## PART 4 — FINDINGS LEDGER AT HANDOVER

Add these to your findings ledger, in `design/DESIGN_INTEGRATION_V2.md` for design items and the live register for the
rest. Close each one or record its state.

| ID | Severity | Finding | Action |
|---|---|---|---|
| F-01 | MATERIAL | Two incompatible "D16–D22" lineages. The advisor message of 10 Oct used D16 for stops, D17 for the charter, D18 for the propagation gate, D19 for publisher practices, D20 for the README pair, D21 for social cards and D22 for the audience suite. The repository uses D16 for Findex aggregates, D17 for Readings and D18 for plain language. This collision is why SB-01 could not be verified | Resolved by OD-1017-*. Record the explanation once in `audit/OWNER_DECISIONS_2026-10-17.md`. Never reuse D19–D22 |
| F-02 | MATERIAL | The full Stage B charter (v3.2) was never committed; the repository holds only a 19-line prospective charter | Commit Appendix 1 (PR-C) |
| F-03 | MATERIAL | Phone pages are long and getting longer (Part 2 table) | Stage B S and G2 targets |
| F-04 | MATERIAL | PR #51 adds phone length and pre-empts G1 | Part 3 handling |
| F-05 | MATERIAL (governance) | An unreviewed workflow on a branch distributed source tarballs as Actions artifacts after the 15 Oct export containment | Append a dated line to `audit/close_out/STAGE_A_EXPORT_CONTROL_2026-10-15.md`. In `docs/REPOSITORY_SETTINGS.md`, recommend restricting workflows on non-default branches to PR-only, or requiring approval. The branch goes via Housekeeping |
| F-06 | MATERIAL (ops) | The Cloudflare Workers check fails on every commit. Account-side retirement is blocked without the owner's Cloudflare access. A permanently red check trains everyone to ignore red | Owner action: retire the Workers project or disconnect the repository in Cloudflare. In code: document it in `REPOSITORY_SETTINGS.md`; never make it required |
| F-07 | MATERIAL | No tags on GitHub, although README and the checkpoint name `checkpoint/2026-10-10-content-complete` | Docs say "created by the owner-run Housekeeping workflow" until it runs (W5) |
| F-08 | EDITORIAL | README current-state rows are stale ("Content: Complete on main, 10 October 2026"; "Public inventory (11 October 2026)") | W6 rewrite |
| F-09 | MATERIAL | Front doors (AGENTS.md, README, Context `programme_state.stage_b`, `OPENAI_REENTRY_CHECKPOINT.md` line 8) say Stage B is BLOCKED | Update all of them together in PR-C. Check `test_public_path_documentation.py`, validator phrases and R86-G01 for hard-coded wording; change tests only to reflect the new truth, never to weaken them |
| F-10 | EDITORIAL | Domain H1s repeat the lead's first sentence. /payments/ H1 is 4–5 lines | S11 |
| F-11 | MATERIAL | The design records are incomplete: `design/DESIGN_INTEGRATION_V2.md` absent; `design/ESCALATIONS.md` and `design/DESIGN_DEBT.md` have open items | G0 creates V2; G3 resolves or decides every escalation |
| F-12 | **BLOCKER (owner)** | The repository is public, and material held non-public is exposed; owner decision pending (OD-1017-13). *(Redacted in the committed copy while the repository is public: the original describes the material; the owner holds the full text.)* | Owner decides visibility (OD-1017-13). Never rewrite history. If it stays public, propose (do not execute) a projection that keeps non-public rows out of tracked projections, as an owner decision |
| F-13 | MATERIAL (ops) | Private-repository CI was refused for billing on 16 Oct | OD-1017-13 |
| F-14 | MATERIAL | Verified defects still true on main (Appendix 2) | PR-D (Stage A residue), then S and T |
| F-15 | MATERIAL (IA) | Desktop has no direct route to the eight topics: the header is Questions · Evidence · Readings · Sources · Method and measurement; topics live in the phone menu and footer; Home does not list them in its main content | G0 first-click test ("find the payments evidence"); fix in S/G2 (Part 6) |
| F-16 | MATERIAL (product) | Compare can never return a positive verdict: all 91 pairs of its 14 records are "not a direct comparison" | T (Part 6, item 16) |
| F-17 | EDITORIAL | SB-01 sits in the OWNER-OPTIONAL section of both register files; only its cell text said BLOCKED (PR #52 rewords it) | PR-C: SB-01 → CLOSED by OD-1017-01 in both files, counts updated, same commit |
| F-18 | MATERIAL (truth of the repository) | Diagrams and checks state 304 documents (`validate.py` uses 2n+2; the site-map SVG; `handoff/IMPLEMENTATION_MANIFEST.json`) while the build makes 306; the full-stack diagram calls the renderer a "React static compiler"; `architecture_diagrams.py` regex-edits its own previous SVG; `design/architecture/README.md` presents a Design→Code sequence as current | Fix at the generator in W6 (diagrams generated from the code, not from the previous picture); `handoff/` stays historical |
| F-19 | EDITORIAL | Installed skill `digital-experience-director` holds stale YFIE facts and approval loops | Handled by Part 0 step 6; report one line of suggested skill edits at the end |

---

## PART 5 — EXECUTION PROGRAMME (phases, PRs, done criteria)

One branch and one PR per row. Each PR follows CONTRIBUTING §4 and §5, regenerates the manifest and then the checksums
(in that order), and merges under OD-1017-06. After merge, verify main, append to PROGRESS.md, then go on.

### Phase 1 — Integrate (target: same day)

| PR | Content | Done when |
|---|---|---|
| PR-A | Merge #52 as it is (re-run Verify if main moved) | Merged; main green |
| PR-B | Finish #53 per the checklist in Part 3: merge main into it normally, resolve, re-verify | Merged; the Master is the 4-cell privacy transaction and nothing else |
| PR-C | **Takeover inputs.** This brief → `audit/close_out/TAKEOVER_BRIEF_2026-10-17.md`; Part 1 → `audit/OWNER_DECISIONS_2026-10-17.md`; Appendix 1 → `audit/close_out/STAGE_B_DESIGN_CHARTER_v3_2.md`; an appended pointer line in the 15 Oct charter and in `AMENDMENTS_D16_D22.md`; front doors updated (F-09); F-05 line; SB-01 moved OWNER-OPTIONAL → CLOSED in `FINAL_OPEN_ITEMS_REGISTER.md` and `OPEN_ITEMS_STATES.json` together (counts, total and the Context `open_items` string updated in the same commit). **Open findings do not go into the register** (CO-G06 allows only CLOSED, HOSTING, FRONTIER, OWNER-OPTIONAL and DECIDED): they live in `design/DESIGN_INTEGRATION_V2.md` (design) and PROGRESS.md (the rest), and enter the register only when CLOSED or DECIDED. **Rule amendments, explicitly:** AGENTS.md rule 2 (OD-1017-03 steward scope) and rule 7 (V2 may now be created); CONTRIBUTING §2 (steward scope), §8 (Stage B authorized; V2 allowed) and §10 (visibility as it actually is); `scripts/reentry.py` guidance names the v3.2 charter. **Keep intact** every string R86-G01, P4-G01 and P4-G04 pin: `\| **Position** \| **DESIGN HANDOFF SUPERSEDED**` in README; `**Status: DESIGN HANDOFF SUPERSEDED` in the checkpoint; the handoff first lines; Context `handoff_readiness == "SUPERSEDED"`; both current hashes and no other 64-hex string; "single production repository" and "sole semantic". **While the repository is public, commit the brief redacted:** F-12 reduced to "material held non-public is exposed; owner decision pending", with no description of the provider rows. Classify everything in the manifest | Merged; validator and docs tests green; the front doors agree: "Stage B authorized 17 October 2026 (OD-1017-01)" |
| PR-D | **Stage A residue (OD-1017-12).** One Master transaction for the Appendix 2 items marked *Master*; one code commit for the items marked *code*. Each item re-verified in the original before change; propagation sweep (CO-G07) for retired wording; social cards redrawn in the same commit | Merged; Appendix 2 items each CLOSED or recorded with the reason they stay |

### Phase 2 — Stage B (BRIEF W4 plus Appendix 1, with Part 6 deltas)

| PR | Content | Done when |
|---|---|---|
| B0 | **G0 baseline** (read-only code). `design/DESIGN_INTEGRATION_V2.md` §G0; metrics JSON under `design/evidence/v2/g0/`; screenshots at 320/390/768/1440, AR and EN, in every state the brief lists; six-persona reader-job audit; top-10 frictions; the visual and diagram audit of all 42 contracts | Committed; numbers reproducible by a script you commit |
| B1 | **S — structure.** S1–S13 and CR-S12; OD-1017-04(b) SDG; OD-1017-08 plain-language leads. Master transactions for copy (S9, S10 labels, S11 H1s, S13 period text if needed); KEY_MIGRATION rows; the ID and data-hook preservation check (against `2ddbfb61`, deliberate changes listed) | Part 2 targets met or each miss recorded with its reason; all gates green |
| B2 | **T — tools.** Search (normalisation, aliases, ranking, typed groups, scope line, zero-result help, query-set gate); Compare (shareable URL, one-sentence verdict reason, print and copy, mobile order); /data/ facets with live counts, URL state and "cited by"; the structured Report-an-error form on /contact/#report with mail and copy transport and a no-JS fallback; `docs/CORRECTIONS_PROCESS.md`; cite formats OD-1017-04(a) | Every tool behaviour tested in a real browser; gates added with negative controls |
| B3 | **G1 — direction challenge.** Three candidates (official-statistical, editorial-interpretive, compact source-first) under `design/exploration/v2/`, on Home, /payments/, CLM-001 and /data/, AR 390 and EN 1440. Disqualifiers first; three independent judge subagents; source-owner test; phone screens and bytes measured. DL-V2-001 recorded. PR #51 assessed as evidence | DL-V2-001 committed with scorecard and screenshots; owner informed (veto window, not a stop) |
| B4a | **G2 — shell, Home, one domain** | Two refinement passes recorded per family; P1 measured on AR 390 |
| B4b | **G2 — Evidence Record, /data/, one Reading, Methodology** | Same |
| B4c | **G2 — propagation** to every remaining family; superseded CSS removed; `design/02_TOKENS.json` regenerated | No family left on the old composition; no dead rules |
| B5 | **W4F — footprint** (Appendix G) | Per-page transfer and estimate for 5 representative pages; footer line Master-first |
| B6 | **G3 — verify and freeze.** Rendered-visibility gate with negative controls (one hidden boundary, one clamped paragraph); drift report; performance threshold gate (/ar/data/ ≤350 KB cold, ≤4 font files) with a negative control; social fingerprint and full redraw (OD-1017-04(d)); the redundancy scan; accessibility record (axe if installable, keyboard, reflow, zoom, forced colours, reduced motion, no-JS); bidi checks; print and copy-a-number tests; the P9 bilingual certainty check; G0 re-run; ESCALATIONS resolved | **STAGE B REPORT** sent (BRIEF format, item 6 filled); main green |

### Phase 3 — Stage C (BRIEF W5–W8 with Part 7 deltas)

| PR | Content |
|---|---|
| C1 | W5 governance and housekeeping |
| C2 | W6 README pair, diagrams, README gate, cleanliness sweep, `REPOSITORY_MAP.md`, cold-reader tests |
| C3 | W6S SEO and metadata, host-neutral |
| C4 | W7 editorial pass, red team and Arabic house-style lint gates |
| C5 | W8 acceptance, audience suite, Appendix I QA, CR-17 edition date, hosting-readiness package (Part 8) |

End with the **FINAL REPLY** (Part 11).

---

## PART 6 — STAGE B: DELTAS TO BRIEF W4 AND THE CHARTER

1. **Order.** BRIEF W4's order stands: G0 → S → T → G1 → G2 → W4F → G3. The design direction is chosen on the
   final structure and tools, not before.
2. **No owner stop at G1** (charter §10.5, v3.1). Inform the owner and continue. The old "stop after G1" in the
   10 Oct message is void.
3. **Hosting-neutral.** Anything in W4 or the charter that names DigitalOcean, App Platform or a fixed public address
   is read as "the future host". Do not add host-specific code.
4. **The baseline is Part 2's table, re-measured.** Report before and after for every row. The biggest single win is
   /data/ (S1, S2, S9); the second is /measurement/ (S8).
5. **Governed prose is never trimmed by design.** Phone length comes down through structure: disclosures (S2, S3,
   S8), caps (S5), teasers (S7), link lists (S6), TOC rules (S10), short thesis H1s (S11) and record-head order (S12).
   Any wording change is a Master transaction, EN and AR together.
6. **P1 on AR 390** (answer, clock, boundary cue, verification link in the first screen) is the main test for
   domain and record pages. Record measured exceptions; never shrink Arabic to pass it.
7. **Arabic first.** Build and judge AR 390 first; EN 1440 is a sibling composition.
8. **Palette and type** stay V1 (charter §6). Token changes are class C, with measured contrast.
9. **SB-02 holds:** no CWR-012 channel chart. An empty `visual_bindings` is not a defect.
10. **Visual contracts.** The count is 42 today, not 36. Audit all of them in G0. Fill or justify every withheld or
    "no values yet" state with a reason that is true today.
11. **The navigation.** D8 is a recorded owner decision that has not been executed.
    - **Execute it in B1 (S),** by a 04_NAV_UX Master transaction plus the steward edit: remove the hub numerals 01–05,
      and make "Method and measurement" one link to `/methodology/`.
    - The resulting masthead is the baseline. Any further label or grouping change (for example a topics entry,
      item 14) is a DL-V2 decision with first-click evidence, Master-first.
12. **Port from `code/navbar-disclosures-integration`** only the three items BRIEF W4 S lists, credited in the
    CHANGELOG.

### Product direction: what would make this site exceptional

These are the advisor's strongest hypotheses after reading every draft, mockup and diagram the other agents produced
and checking them against the live site. They are not orders.

**Order.**
- Test each against real reader tasks in **G0**, and decide it (adopt, adapt or drop, as a DL-V2 entry) **before
  B1**.
- Structural and copy changes are then implemented in S, so S and T are never redone after G1.
- G1 decides the visual direction, not the structure.

**Constraints.**
- D9: Home and /explore/ keep the R8.4A model, with no new task taxonomy. A topic grouping is navigation to existing
  routes, not a taxonomy, and must be argued as such or dropped.
- D13: prose may be replaced by a link only where identical text exists at the target.
- Any record → measurement-priority relation is a Master field, never renderer logic.
- All new visible wording goes Master-first.

13. **The signature unit: Known · Not established · What would settle it.**
    - **What it is.** One evidence unit that puts three things side by side:
      - what the evidence shows: value, unit, universe, period and publisher;
      - what it does not establish: the governed limit;
      - which measurement priority would settle the open question, with a link.
    - **Why.** It is the product's thesis made visible, and it serves the CBY, the World Bank, the IMF, KfW, the
      OECD, journalists and citizens equally.
    - **Where it comes from.** An owner-supplied Arabic mockup, not in the repository, proposed the first two halves
      for POS: «ما نعرفه» (561 → 1,651, CBY-Aden) and «ما لا نعرفه بعد» (users and regular use not measured), with
      source, scope and date underneath. Add the third part from the Measurement Agenda.
    - **Use it where it fits:** Home (one or two units), domain answers, and the head of records with a value.
    - **Rules:** never red or green semantics (no red "minus" for the unknown); shape and word only; the scope line
      uses the governed reporting-scope wording, never a territorial label.
    - **The test.** This is SIG-1 + SIG-4 done as one pattern. Prove it on three families before going global.
14. **Topics reachable in one step** (F-15).
    - The same mockup grouped the eight domains into four families on Home: people & access; payments & remittances;
      firms & finance; providers & reforms.
    - Test against the current flat eight, and decide whether desktop needs a topics entry in the header (a D8/CR-S12
      steward change, Master-first labels).
    - Routes do not change. Run a first-click test in AR and EN before and after.
15. **"What the numbers do not say" on Home.**
    - Five common misreadings, each a short pair (the tempting reading → what the evidence supports), each linked to
      its record:
      - survey coverage (11.9% of adults in surveyed areas only);
      - infrastructure ≠ use (POS 561 → 1,651);
      - revision ≠ decline (the 2024 remittance restatement);
      - delivery ≠ durable use (45,460 pilot recipients);
      - listing ≠ operation (the provider rosters).
    - This replaces repeated system-context prose rather than adding length.
    - New copy goes Master-first. Keep each pair only if its record already states the limit.
16. **An honest Compare** (F-16).
    - Present it for what it is: a comparability checker that explains why two figures cannot be read side by side.
    - Then test whether the Master already supports one legitimately qualified pair: for example, Findex account
      ownership across the 2011, 2014 and 2021 waves (same definition; coverage differs). Admit it only by a
      transaction with its verdict reason.
    - Never loosen the rules to manufacture a positive result.
17. **Faster verification for professionals.**
    - Source links to the exact indicator page where the publisher has one (World Bank per-indicator locators;
      Master-first).
    - BibTeX and RIS (OD-1017-04(a)).
    - Print, copied figures and shared cards keep scope and limit (P5).
18. **The phone is the product.** The owner's main complaint is long, heavy Arabic pages. Part 2's table is the
    scoreboard; every structural decision reports its phone-screen effect.
19. **The first visit must make sense to someone who has never heard of us.** Today's Home is sound but dense:
    - about 1,760 visible English words;
    - the first figure paragraph runs 109 words;
    - "composite" and "not a single score" each appear three times;
    - system context is said three ways;
    - topics are not visible.

    The Home contract:

    | Time | The visitor has |
    |---|---|
    | 10 s | understood what this is (the thesis, one line), that evidence has different clocks, and where to begin (a question, a topic, or "verify a figure") |
    | 60 s | read one bounded answer: the Known · Not established · What would settle it unit |
    | 3 clicks | reached an original source |

    Test it in G0 and G3 with these first-visit journeys, AR 390 first, then EN 1440:

    | Visitor | Lands on Home wanting… | Success means |
    |---|---|---|
    | Yemeni citizen (AR, phone) | to know if people use banks or wallets | finds 11.9% with "surveyed areas, 2022–23 fieldwork" attached; understands it is not today's number |
    | Journalist | a quotable figure | copies a sentence that keeps scope and limit; finds the correction route |
    | CBY (Aden or Sana'a) analyst | what is said about payments and rules | reaches /payments/ or /reforms/ in one step; sees issuance ≠ implementation; neutral naming of both banks |
    | World Bank / IMF / KfW / OECD officer | definitions, comparability, SDG mapping | reaches the method and Compare's verdict; finds the per-indicator source link |
    | WFP / UNDP / humanitarian analyst | cash and remittance channels | reaches CWR-012 and its geographic limits; programme KPI ≠ prevalence |
    | Researcher | sample, interval method, citation | CLM-001's method and CR-22 within three clicks; BibTeX |
    | Bank / MFI / exchange company | their sector's evidence | finds it without any ranking; licence ≠ operation |
    | Source owner | their figure as published | exact value, locator, edition; how to request a correction |

20. **International practice as a quality lens, never a badge.** Use these to sharpen what already exists:
    - the IMF Data Quality Assessment Framework and revision-policy practice: /corrections/, editions, CWR-001
      "same year, different number";
    - the UN Fundamental Principles of Official Statistics (impartiality; analysis kept separate from advocacy): tone
      and CauseWay's positioning;
    - FAIR and the W3C Data on the Web Best Practices: stable IDs, metadata, versioning and citation;
    - SDG metadata (8.10.1, 8.10.2, 10.c.1);
    - ONS and UK Analysis Function chart guidance, and WHO data design principles: visual contracts and accessible
      tables;
    - GOV.UK, USWDS and the Saudi/UAE design systems: forms, language switch, Arabic-first patterns.

    Rules:
    - Cite them in DL-V2 decisions where they changed a decision.
    - Never claim conformance or endorsement.
    - A machine-readable indicator dictionary (definitions and metadata only, CauseWay's own content) is high value
      for statisticians. Prepare it, but publish only on a separate owner decision: downloads are off (D4).
21. **Premium typography, measured.** IBM Plex Sans Arabic and Plex Sans stay the text faces.
    - G1 may test **one** additional OFL-licensed display face for headings (Arabic first; for example a Naskh-style
      face), self-hosted, as a class-C candidate within the 4-font-files-per-page budget.
    - Adopt it only if Arabic heading quality improves visibly in the judges' scores at no performance cost.
    - Titles get the same care: short thesis H1s (S11), sentence case, no widows, no "Evidence Passport" or other
      internal terms in public copy.

22. **Explicitly rejected (the drafts proposed them; do not build):**
    - dashboards, KPI scorecards, maps of access points, a provider directory;
    - an AI assistant;
    - per-institution portals;
    - a 13th Reading or a CWR-012 channel chart;
    - a homepage carousel, stock or hero imagery, decorative charts;
    - side-by-side bilingual pages;
    - a separate Claude Design / mockup track: G1 candidates are built on the real renderer with real Arabic.
      Claude Code in VS Code has no design canvas. Mockups have twice drifted from the governed content in this
      project's history, and the charter judges real pages.

---

## PART 7 — STAGE C: DELTAS TO BRIEF W5–W8

**W5 — Governance and housekeeping.**

`housekeeping.yml` follows the brief: the owner runs it, `dry_run` defaults to true, the confirm phrase is required,
and no tag is ever moved. Its archive list adds:
- `improve/ci-gov-20261016`;
- `work/privacy-runtime-notice-20261015`;
- `design/homepage-editorial-gateway`, after #51 is closed;
- `pr/hosting-neutral-20261016`, after it merges;
- `docs/neutralize-d19-d22-20261017`, after it merges;
- every branch that is not an ancestor of main.

It creates:
- `checkpoint/2026-10-10-content-complete` at the content-complete commit the docs name, only if that commit exists;
  otherwise it records the absence;
- `checkpoint/<date>-hosting-ready` at the SHA the owner enters.

The other W5 items:
- `currentness.yml`: monthly plus manual; opens one issue; never edits.
- `docs/REPOSITORY_SETTINGS.md`. Include F-05 and F-06, plus:
  - rulesets;
  - auto-delete head branches;
  - read-only default workflow permissions;
  - private vulnerability reporting;
  - CodeQL default setup;
  - secret-scanning push protection.
- `SECURITY.md` (no guarantees claimed).
- `CITATION.cff`.
- **One root `LICENSE.md` in two parts:** CC BY 4.0 for CauseWay's own content (third-party sources excluded); the
  code all rights reserved (D3). Not a separate LICENSE-CODE.
- `.github/CODEOWNERS`, notification only (OD-1017-04(f)).
- Issue forms in EN and AR ("Report an evidence error", "Report a site defect", "Suggest a source") and `config.yml`:
  blank issues off; a warning never to post personal or respondent-level data.
- **`deploy.yml` stays disabled** as PR #53 left it. Drop the brief's "refusal step": with deployment disabled it has
  nothing to refuse. Stage D re-enables a host adapter by its own reviewed change.
- Stale-doc closing notes and front-door headers, as the brief lists.

**W6 — README pair.**

Gates you must satisfy:
- `test_public_path_documentation.py` requires a `## Public path` section in `README.md`, before `![Public path]`,
  containing every domain label, the eight search-family phrases and "does not validate". Keep it, as part of
  section 4 or 5 below.
- New root files (`README.ar.md`, `SECURITY.md`, `CITATION.cff`, `LICENSE.md`, issue forms) need classification
  rules in `scripts/repository_manifest.py` (CURRENT_DOCUMENT), or `--check` fails.
- F-18 means changing the count rule in `validate.py` (`2*n+2` → the true formula) and the site-map SVG generator.
  `handoff/IMPLEMENTATION_MANIFEST.json` is regenerated by its own tool; that is not an edit of history.

`README.ar.md` is written first, as Arabic, then `README.md`. Both follow this order:
1. in two lines;
2. why the resource exists;
3. who it is for, as a table with "start here" and "what you will find" for each of: citizens; journalists; the two
   central banks and supervisors (neutral naming per `audit/naming/`); banks, MFBs, payment providers and exchange
   companies; researchers; the World Bank, the IMF and DFIs; UN and humanitarian agencies; donors and programme
   teams; source owners;
4. how to read it (افهم ← استكشف ← تحقّق);
5. a site map, generated;
6. the financial-inclusion system, mapped to the eight domains;
7. one number traced: CLM-001, with CR-01 and CR-22;
8. the firewall table;
9. what the resource does not claim;
10. how a change reaches the public: a generated flowchart with the live negative-control count;
11. reporting an error;
12. citing and reuse;
13. the footprint method;
14. for developers and reviewers;
15. the repository map;
16. status and what remains, which is hosting only;
17. CauseWay, funding and independence (D1).

Also:
- Counts and diagrams are generated by `scripts/architecture_diagrams.py` and gate-checked. Nothing is typed by hand.
- Keep every phrase and hash that `validate.py` reads.
- Harvest from Mohammed Waleed's README draft as the brief lists, credited.
- An independent Arabic-editor subagent judges `README.ar.md` as Arabic. Cold-reader tests run in both languages.

**W6S — SEO, host-neutral.** Prepare everything:
- titles ≤60 characters, descriptions ≤155;
- reciprocal hreflang and x-default;
- canonical, sitemap and robots, gated behind `public_origin`;
- JSON-LD only where true, with the F6-G04 extension as a deliberate gate change and a negative control.

Prove the origin switch with a reserved test origin (`https://example.org/financial-inclusion-evidence`): absolute
canonicals, sitemap and robots appear only then. `noindex` stays on everything until hosting.

**W7 — Editorial and red team.**
- English editor, then the Arabic economic editor (Arabic first), on every string Stage B or C added or changed.
- Red team in the 12 roles.
- The Arabic house-style lint across all public Arabic. Its mechanical rules become gates with negative controls.
- `NEW_ARABIC_SINCE_2ddbfb61.csv`; `KEY_MIGRATION.csv` finalised.

**W8 — Acceptance.** The brief's W8, plus:
- **The audience task suite (OD-1017-04(e))**, ten personas and their tasks:
  1. Citizen, Arabic, phone: what financial inclusion means here; the one number with its limit.
  2. Journalist: a quotable sentence for 11.9% with scope and non-establishment; whom to write to about an error.
  3. Official at either central bank: the latest instruments; issuance distinguished from implementation; the
     neutral naming of both banks; payment evidence and its limits.
  4. Bank, MFB, payment provider or exchange company: their sector's evidence; licence ≠ operation; no ranking.
  5. Researcher: CLM-001's definition, sample, interval method (CR-22) and original locator within three clicks; a
     BibTeX citation.
  6. World Bank, IMF or DFI professional: the SDG correspondence; a Compare verdict between two sources.
  7. UN or humanitarian worker: the cash and remittance channel evidence and its geographic limits.
  8. Donor or programme team: what remains unknown and the measurement priority that would close it; programme KPI ≠
     national prevalence.
  9. Source owner (World Bank Findex, CBY, Sana'a Center, CCY): their figure exactly as published, with locator and
     edition; how to request a correction.
  10. Low-bandwidth reader: Home and one record on a throttled 3G profile; transfer checked against the footprint
      method.
- **CR-17.** The edition date is set to the final content edition, and "Sources checked up to" to the date of the
  last original actually re-read. Master-first, EN and AR.
- **FRONTIER cards.** Make one dated re-attempt on each FRONTIER card whose human step a browser can now do
  (WebFetch/WebSearch only, never around a block). Change a state only on evidence.
- **The acceptance package** as the brief lists it, named after the final SHA and built in scratch. Never commit a
  ZIP. Add `docs/ACCEPTANCE_PACKAGE.md`.

---

## PART 8 — "HOSTING-READY", HOST-NEUTRAL: THE DEFINITION OF DONE

Main is hosting-ready when **all** of the following are true. Record each as PASS / FAIL / NOT RUN, with evidence, in
`docs/HOSTING_READINESS.md` (new; the release runbook links to it).

1. Stages B and C are merged; main is 9/9 green; every negative control is caught.
2. One reserved origin, `https://yfie.example/financial-inclusion-evidence` (the one `test_base_path.py` and
   `test_http_contract.py` already use).
   - `python3 scripts/build.py --origin <it> --out <dir>` produces a site that passes:
     - `test_base_path.py`;
     - `test_http_contract.py`;
     - `test_no_javascript.py`, with `YFIE_SITE_DIR=<dir>`;
     - `test_security_headers.py`, after you give it a site-directory parameter (it reads only `dist/` today; a gate
       change, with a negative control);
     - the SEO origin-switch gate, which you build in W6S, with a negative control.
   The review build (`dist/`, origin null) stays byte-identical to a fresh build.
3. `site-src/hosting/_headers` is the single portable response policy. A host adapter translates it; nothing else
   defines headers.
4. **`docs/RELEASE_RUNBOOK.md` is rewritten host-neutrally.** Its first step is "owner names host and origin". Every
   later step names its gate. The Stage D prompt in it covers exactly these:
   - set `public_origin`;
   - the /privacy/ host-facts Master transaction (prepare the cell plan and its bilingual text skeleton now, unapplied,
     in `audit/hosting_ready/PRIVACY_STAGE_D_PLAN.json`);
   - full social redraw (OD-1017-04(d));
   - currentness re-run and edition date;
   - build `--out`;
   - the host adapter;
   - the live checks (headers, HTTPS, an in-country phone check in Arabic);
   - owner acceptance, then `pre_release` false.
5. **A comparison of candidate hosts** for a static bilingual site with custom headers under a sub-path, in
   `docs/HOSTING_READINESS.md`, for the owner's decision. Facts only, each with a dated source; no purchase; no
   recommendation presented as a decision. At minimum: Cloudflare Pages/Workers static assets, a DigitalOcean static
   site or App Platform, Netlify, GitHub Pages (no custom headers: state the consequence), and nginx on any VPS. State
   what each needs from the corporate causewaygrp.com route if a sub-path is kept.
6. The live register shows nothing open except HOSTING items and the explicitly retained FRONTIER and
   OWNER-OPTIONAL states. Each HOSTING item names the runbook step that closes it.
7. Nothing in content, design, tools, docs or governance waits on anything except the owner's host choice and the
   live-only checks.

---

## PART 9 — WORKING METHOD

**Team (hub and spoke).** You lead, decide and write. Subagents read, test and challenge; they never write to the
repository:
- an Arabic editorial typographer and RTL specialist;
- an information designer and data-visualisation specialist;
- an accessibility and front-end engineer;
- an Arabic economic editor;
- an English evidence editor;
- the red team;
- three G1 judges: an Arabic first-time phone reader, a sceptical statistician-journalist, and a World Bank/IMF data
  professional;
- the ten audience personas.

Give each subagent the files and the exact question. Ask for a findings list, not prose. Route mechanical scans to
smaller models and judgement to the strongest.

**Look at the pages, economically.**
- Judge the decisive views yourself: first screens at AR 390 and EN 1440 of the proving pages.
- Delegate wider screenshot review to subagents that return findings only.
- Numbers before pictures.

**Repository size budget.** The repository is about 320 MB of history and cannot be rewritten.
- Commit only the screenshots a decision rests on (G0 baseline set, G1 candidates, before/after for the proving
  pages), as compressed PNG or WebP. At most about 10 MB of images per PR.
- Keep all other captures in scratch, outside the repository.
- Social-card full redraws happen only twice (OD-1017-04(d)). Record the size before and after each.

**Proportion.**
- No document for its own sake. `design/DESIGN_INTEGRATION_V2.md` and PROGRESS.md are the records.
- A memo states the decision, its evidence and its cost in a few lines.
- Do not open new review groups to re-review settled Stage A content.

**Lessons from this repository's own failures.** Do not repeat them:
- **Regenerate the manifest, then the checksums.** The reverse order failed CI on PR #51 (`69efb757`).
- **Run every gate locally before pushing.** `fb27efee` failed CI on the validator.
- **Redraw social cards in the same commit as the text change.** Missing cards rolled back CLOSE-6E (F6-G01).
- **Read a `run_stage.py` rollback message; it names the gate.** CLOSE-6F rolled back twice (CO-G04, CO-G06) before
  committing.
- **Negative controls are slow** (six shards, 35 min each in CI). Locally use `--only <pattern>` for the gates you
  touched; let CI run all of them.
- **`test_cutover_parity.py` exit 2 means "pinned"** and is expected. Standing content parity is the live gate.
- **If the pinned Playwright browser cannot download, use the installed Chromium,** and record the substitution. CI
  supplies the pinned browser.
- **An Arabic-editor subagent run was once lost to a rate limit.** Re-run it; never skip it.
- **Never touch `handoff/` prompts. Never run `post_execution_acceptance.py`.** Never store Findex microdata, a
  respondent file or an API key; the repository is public.

**Context and continuity.** This is a long run.
- After every merged PR, PROGRESS.md carries one dated line: PR, SHA, what closed, what is next.
- If your context compacts, or a new window starts, resume with:
  ```
  Resume the YFIE takeover from the repository, not from memory. Read AGENTS.md, audit/close_out/TAKEOVER_BRIEF_2026-10-17.md
  (Parts 0, 1, 5 and the part for the current phase), the last 40 lines of audit/close_out/PROGRESS.md and, in Stage B,
  audit/close_out/STAGE_B_DESIGN_CHARTER_v3_2.md. State in five lines where you are, what is merged, what is open and
  the next PR; then continue. Same rules, same stops.
  ```

---

## PART 10 — STOP ONLY FOR THESE

1. **Authority divergence.** The Master or the authority files changed outside your transactions or Part 3's
   explanation, or any commit or PR appears from an agent other than you (OD-1017-11).
2. **An owner-only action.**
   - Cloud accounts, DNS, billing or credentials.
   - Running Housekeeping or deleting branches or tags.
   - Repository settings.
   - The Cloudflare retirement.
   - The host choice.
   - Legal, rights-clearance or licence questions beyond the recorded decisions.
   - Publishing downloads or analytics.
3. **A decision that cannot be undone and could reasonably go either way.**
4. **A gate that cannot pass without being weakened.** Report the gate, the fault and the options.

In each case: finish the preparatory work, set out the decision with your recommended default, send it to the owner,
and continue with every independent piece of work meanwhile.

**Never:**
- force-push, rewrite `main` or a tag, or commit a ZIP, cache, screenshot outside `design/evidence/`, secret or
  respondent file;
- hand-edit `site-src/content/**`, `dist/**` or `PUBLIC_LITERAL_CLOSURE.json`;
- change a value, claim, universe, period, source relation, rights or publication state except by a Master
  transaction, EN and AR together;
- add a tracker, cookie, third-party script, font CDN or chart library;
- claim WCAG conformance, legal review, rights clearance, native-language certification, security guarantees, live
  performance or release readiness;
- declare DESIGN HANDOFF READY or PUBLIC RELEASE READY.

---

## PART 11 — REPORTS

**After each phase**, send a message of 15 lines or fewer. For Stage B and Stage C, use BRIEF.md's STAGE REPORT
format, sent through the messaging tool so the owner can read it on a phone. It covers:
- PRs and merge SHAs;
- what closed;
- the measurements (phone screens before → after; DL-V2-001 scores);
- what is open;
- at most three owner questions, each with a default;
- the next PR.

**FINAL REPLY** (50 lines or fewer):
- every PR and merge SHA;
- structure and design: phone screens before → after per family, and DL-V2-001 with the G1 scores;
- the tools added and their gates;
- footprint for 5 pages;
- the audience-suite and cold-reader results;
- cleanliness, BLOCKERs first;
- the live register by state;
- the Part 8 checklist, item by item;
- the owner's exact next steps:
  1. retire the Workers check;
  2. apply `REPOSITORY_SETTINGS.md`;
  3. run Housekeeping (dry run, then real) with the final SHA as `hosting_ready_sha`;
  4. send the acceptance package for independent review (advisor, then OpenAI);
  5. choose host and origin, then open a fresh window with the Stage D prompt in the runbook.

Last line, exactly: **CLAUDE MATURATION HAND-BACK READY — ONLY HOSTING REMAINS**

---
---

## APPENDIX 1 — STAGE B DESIGN CHARTER v3.2 (operative under OD-1017-01)

Commit this appendix verbatim, from the next line to the end of the appendix, as
`audit/close_out/STAGE_B_DESIGN_CHARTER_v3_2.md`. It was written on 10–11 October and not committed until now.

Read it with these amendments of 17 October 2026, which prevail:
1. **G1 →** BRIEF W4 order (G1 after S and T).
2. **Hosting is neutral** (Part 6, item 3).
3. **The visual-contract count is 42.**
4. **The 15 October prospective charter's constraints remain** (SB-02, CWR-013 reserved, two-Reading rule, CWR-011
   placement).
5. **"AMENDMENTS_D16_D22.md" in §0 means that file as amended by PR #52**, plus `audit/OWNER_DECISIONS_2026-10-17.md`.
   D19–D22 confer nothing.
6. **"brief W4 G0" in §13** means BRIEF W4 G0, re-run on the final build.
7. **The charter's own line "Commit it as audit/close_out/STAGE_B_DESIGN_CHARTER.md" is superseded.** Its path is
   `audit/close_out/STAGE_B_DESIGN_CHARTER_v3_2.md`, and the 15 October file stays where it is with an appended
   pointer.

```text
STAGE B DESIGN CHARTER — v3.2 — Yemen Financial Inclusion Evidence / أدلة الشمول المالي في اليمن

For Claude Code, Stage B (W4).
- Commit it as audit/close_out/STAGE_B_DESIGN_CHARTER.md.
- v3.2 makes seven amendments to v3.1, marked [v3.2] in place and listed in §15.
- v3.1 superseded v3 and v1. It changes v3 in four places: G1 follows D7 with no owner stop (§10.5); the
  social-card blind spot is spelled out (§12.3); earlier design work enters as challenger evidence (§10.1); and the
  ambition and challenge clause is added (§1).
- v3 superseded v1. It keeps v1's ambition and adopts the structure of the OpenAI review (v2). It corrects four points
  in that review against the repository bytes; §15 lists every change.
- Read it with BRIEF.md (v5) and AMENDMENTS_D16_D22.md. Where this charter cites a structure rule of the brief, it
  writes "brief S3", "brief S10" and so on.

══════════════════════════════════════════════════════════════════════
0. AUTHORITY: THIS CHARTER DECIDES PRESENTATION ONLY
══════════════════════════════════════════════════════════════════════
1. The Production Master decides facts, claims, copy, evidence states, sources, rights and publication. The
   projections follow it.
2. The controlled contracts are in force as they stand:
   - navigation_interaction.json, presentation_priority.json, the page-family and visual contracts, and the
     accessibility contracts.
   - They change only through a path the brief or an owner decision authorises: a Master transaction (D8 through
     04_NAV_UX; brief S11's domain titles through 02_SITE_MAP), or a D14 steward edit inside D14's scope, with every
     gate run.
3. BRIEF.md, the owner decisions and AMENDMENTS direct the work, through those paths.
4. This charter decides presentation choices inside all of the above. It never changes a value, claim, question,
   route, evidence state, source relationship, rights state, the analytical form of a governed visual, or a publication
   state.
5. Any new visible string (a label, a caption, a colophon line, a state word) goes Master-first, in EN and AR.

══════════════════════════════════════════════════════════════════════
1. AMBITION
══════════════════════════════════════════════════════════════════════
Most evidence portals make the number prominent and the conditions for reading it secondary. YFIE does the reverse
without becoming heavy: the answer is clear because its scope, clock, source and limit are clear.

The rhythm every consequential figure keeps:
- Answer: large, confident, uncluttered.
- Clock: visibly attached.
- Scope: immediately understandable.
- Boundary: quiet but impossible to miss.
- Source: always one step away.
- Unknown: designed with as much care as the known.
- Whitespace: it carries the intellectual hierarchy.

The quality test:
- A source institution recognises its evidence as faithfully represented.
- An independent reader finds the scope and the limit unusually easy to verify.
- CauseWay's position comes from restraint, traceability and editorial quality, never from promotional copy.

The test is the pages, not the paperwork. The aim is measurably better pages and journeys, above all Arabic on a
phone; a larger design dossier is not the aim. The site should have the seriousness of an official statistical
product and the clarity of excellent editorial design. It is distinctive because it explains complex evidence better
than conventional interfaces, not because of badges, cards or repeated metadata. Ask of every pattern: without the
CauseWay logo, would this page still show a distinctive way of handling evidence? If a pattern adds a layer instead of
removing one, drop it.

Use your strongest available capabilities where they serve the page: frontend and design skills, real-browser
screenshots read back, data visualisation, an Arabic editor and an accessibility review. Do not multiply agents or
documents for their own sake. Challenge this charter: where the live renderer or the evidence shows a better answer,
take it and record why in one DL-V2 line.

Tone: calm, formal, exact, readable. A public evidence instrument with editorial intelligence. Never a dashboard, a
consultancy site, a template, a data dump or a campaign page.

══════════════════════════════════════════════════════════════════════
2. THREE CLASSES OF DESIGN DECISION
══════════════════════════════════════════════════════════════════════
A. Governed invariants: never redesigned.
   - Copy, values, units, universes and periods.
   - Routes, the question architecture, and the semantics of Search and Compare.
   - Evidence–source relationships, rights and publication states.
   - The analytical form of the visual contracts, and the correction and version behaviour.
   - A defect here is fixed Master-first.
B. Required patterns: implemented wherever the controlled state supports them.
   - SIG-1 the figure grammar; SIG-4 absence; SIG-5 the verdict in Compare; SIG-7 print.
   - Detached-use safety.
   - The visible boundary beside every figure (brief S3).
C. Candidates: they must prove themselves before global use.
   - SIG-2 evidence-class marks; SIG-3 the clock strip; SIG-6 the two clocks.
   - The masthead treatment, the desktop TOC presentation, compact source rows and display-scale changes.
   - A candidate becomes global only after it passes on three page families in G1 or G2. Record the decision as a
     DL-V2 entry, with its evidence.

══════════════════════════════════════════════════════════════════════
3. WORKING PROTOCOL: AGAINST MECHANICAL WORK
══════════════════════════════════════════════════════════════════════
3.1 Intent before styling. Before each page family, write a memo in design/DESIGN_INTEGRATION_V2.md:
- the one thing the page must make obvious;
- the reader's first three questions;
- the current failure, with a screenshot or a measurement;
- the options considered;
- your choice, its class (A, B or C) and its cost;
- what becomes more true, what becomes more complex, and what can be removed.
Think hard at each memo and at the G1 decision. [v3.2] Keep memos short: record material decisions, their evidence and
their trade-offs in DESIGN_INTEGRATION_V2.md; do not write prose for its own sake.

3.2 Build → look → critique → refine.
- Render AR 390 first, then EN 1440.
- Open every screenshot with the Read tool and judge it as an editor would. Metrics confirm judgement; they do not
  replace it.
- Refine Home, one domain page, one dense Evidence Record, /data/ and one Reading, in both languages, until their
  criteria are demonstrated. [v3.2] A pass ends when its criteria are met, not when a set number of reviews is done.

3.3 Arabic first, not English mirrored.
- Judge AR 390 first. English is a sibling composition.
- Never shrink Arabic to match English height. Never force English line breaks onto Arabic.
- Never mirror quantitative axes, and never translate IDs.
- Never rewrite governed Arabic in presentation code.

3.4 Three families before a global rule. Test every rule on Home or Orientation, an Evidence Record, and a dense
reference or data page. If it helps one family and harms another, specialise it.

3.5 The source-owner test. Use five figures. [v3.2] Resolve each from its current Master record when the test runs (value, unit, universe,
period and publication state); the list names the objects, not fixed values:
- 11.9% account ownership;
- the latest POS terminal count;
- the 2024 remittance restatement;
- the bank balance-sheet composition;
- one microfinance panel figure.
For each, check seven things: value; unit; universe; period; the publisher's role; that the limit is visible; that
CauseWay's attribution is kept separate from the source's authority. Any failure blocks visual acceptance.

3.6 Counterfactual deletion: for interface chrome and duplicated explanation only, never for governed content.

══════════════════════════════════════════════════════════════════════
4. PRINCIPLES, EACH WITH A TEST
══════════════════════════════════════════════════════════════════════
P1 Answer, clock, boundary and verification path travel together.
- Test: on AR 390, every domain and record page shows, within its first screen (390×844), the answer, its clock, a
  boundary cue and a visible link to the evidence or source.
- The full source title and the full boundary text may follow below.
- [v3.2] This is the target outcome, never a reason to shrink, clip or compress Arabic. Where a long governed title
  or an accessible size makes the target unreachable, record the page, the measured position and why the composition
  is still the clearest available.
P2 Provenance is visible.
- Test: no consequential figure needs a hover to show its evidence role, period or source path.
P3 Absence has weight.
- Test: nothing missing looks like zero or like a rendering failure. Use the governed state vocabulary.
- In dense tables, use one compact accessible label plus a table note, not a sentence in every cell.
P4 Calm authority.
- Hierarchy comes from type, space, rules and alignment, not from card walls, shadows, gradients, animation or brand
  colour.
- Test: at 25% zoom the reading order is still obvious.
P5 Detached use stays safe.
- Test: a crop, a copied figure, a print or a shared card keeps enough scope and source to prevent material misuse.
P6 Performance is part of design.
- Tests:
  - the existing budget gate (scripts/performance_budget.py) passes;
  - a before/after report covers Home, one domain, CLM-001, /data/ and one Reading, in AR and EN: cold-load bytes and
    the JS, font and image deltas;
  - every persistent byte added names its reader benefit;
  - the first screen renders with system fallbacks and no layout jump.
- No font CDN, decorative imagery, animation framework, icon framework or unnecessary chart library.
- Speed on Yemeni networks is release-stage evidence; W4 claims nothing about it.
P7 Every new pattern earns repetition. A new global component serves a repeated reader job on at least three routes,
unless one governed family uniquely needs it.
P8 Two languages, one truth. The same facts, limits, order of meaning and verification path, in different
compositions where the scripts require it.
P9 Semantic invariance is proven, not promised. The standing gates already prove the text: content parity (no
governed sentence lost, no ungoverned number), the projection check, bilingual invariance and the literal audit. W4
adds what they cannot see (§12).
- [v3.2] They do not prove that EN and AR carry the same certainty and causal limits. Before G3, an Arabic editor and
  an English editor read a sample of high-risk statements side by side, as rendered: CLM-001, a Compare verdict, two
  Reading theses and the two-clocks text on Home. They report any difference in hedging, causality or scope. This is
  a targeted check of the changed presentation, not a second whole-corpus gate.

══════════════════════════════════════════════════════════════════════
5. SIGNATURE PATTERNS (SIG-n, so they cannot be confused with the brief's S-rules)
══════════════════════════════════════════════════════════════════════
SIG-1 Figure grammar (required where a consequential quantitative figure exists). One visual unit made only of
controlled fields:
- value and unit; universe; period; publisher;
- the evidence class, where SIG-2 is accepted;
- one material "does not establish" line;
- the record or source path.
A record with no value (a framing or method rule) keeps its own governed record form and never shows an empty plate.
It must survive copy, print, screenshot and sharing.

SIG-2 Evidence-class marks (candidate; a mapping audit comes first).
- Map every proposed mark to a class that already exists: VIS-EVIDENCE-CLASS-LADDER and the records' governed
  classes. Report the coverage and the records that have no safe mapping.
- No mapping means no mark. Never create a second taxonomy.
- Shape plus word, with accessible text, and never colour alone.
- /methodology/ defines the classes. Link to it once per section, not from every mark.

SIG-3 Clock strip (candidate; a date-coverage audit comes first).
- Observed (fieldwork or reference period) → published (by the source). Use only dates the Master holds.
- Keep "source link last checked" out of the evidence clock. It belongs with the source line, worded as a link check,
  so that it can never read as currentness of the measurement.
- Say "not stated" only where the absence is material.
- Do not force a strip onto a record whose chronology is simple.

SIG-4 Absence (required).
- One structural treatment with explicit words for the absence states.
- [v3.2] Use only states that are publicly eligible and already in the controlled vocabulary. Publication filtering
  comes first: the component never reveals the existence or metadata of an internal-only object. "Withheld" and
  "no public locator" appear only where controlled public copy already states them.
- It applies in tables, charts, the subgroup table and the Measurement Agenda.

SIG-5 Comparability verdict (required in Compare; elsewhere only where two figures are actually juxtaposed for
comparison). Use the controlled verdicts only: directly comparable; comparable with qualification; not comparable;
unresolved. Each has a shape, its word and its one controlled reason.

SIG-6 Two clocks (candidate). On Home, where the controlled content already contrasts the people-side evidence
(fieldwork 2022–23) with newer system evidence. In a domain only where that contrast is material. Attach the clocks to
the evidence objects before inventing any visual. Never imply that newer system data update an older measurement of
people.

SIG-7 Print (required). [v3.2: replaces the mandatory evidence-sheet page.]
- Every printed page is intelligible on its own: limits, sources, the page URL and the edition print, and navigation
  does not (brief, Print).
- Records print complete, with nothing cut (D13). The first printed page carries the figure grammar or its
  non-value equivalent, with its boundary.
- A separate evidence-sheet page is used only where testing shows that it helps a dense record, and never where it
  merely duplicates.

SIG-8 Reading page (required where the controlled structure supports it).
- An editorial measure, with figures as governed evidence objects.
- Definitions appear as margin notes on wide screens, and inline on phone, only where definition objects exist.
- No rhetorical pull quotes.
- A "how to use this" block only where the Reading's controlled content supports one.

══════════════════════════════════════════════════════════════════════
6. VISUAL LANGUAGE
══════════════════════════════════════════════════════════════════════
6.1 Palette: the baseline is the shipped V1 system. Do not import another.
- The live tokens (scripts/yfie/theme.py; design/02_TOKENS.json; decision DL-V1-001):
  - surfaces: paper #F7F5F0, white #FFFFFF;
  - one green: green-700 #005A44, also the counter or boundary voice, and green-900 #0C3B2E;
  - sage: 100 #E7ECE4, 400 #8A9A82, 600 #5F7357;
  - brass and ochre: brass-300 #B8975A, which is also the ochre line, brass-700 #7A5A1D, gold-300 #D6B86A;
  - ink #17212B, ink-2 #3D4954, mute #646F79;
  - rules: rule #D8DDE2, rule-2 #AEB7BF.
- DL-V1-001 retired the teal #1E5650 and #F5F1E9. They stay retired.
- The palette proposed in the OpenAI review (#13291F, #1C3D32, #C9A24B, #F6F2E9) appears nowhere in the repository.
  It is not used.
- The two layers already exist in V1. Keep them distinct:
  - institutional layer: the canonical logo, the green-900 colophon band and gold-300 group headings;
  - evidence layer: ink, rules, ochre and the green counter voice.
- Semantics:
  - brand gold is never chart data;
  - green never means "good";
  - evidence states are shown by shape and word;
  - there is one interactive accent.
- A token change is a candidate (class C). It needs a DL-V2 entry, a token diff and measured contrast: at least
  4.5:1 for text and 3:1 for UI, on the real surface.
- G1 tests a white surface against the paper surface for figures.

6.2 Type.
- Two faces only: IBM Plex Sans Arabic and IBM Plex Sans.
- Keep the proven Arabic sizes and leading unless browser evidence shows a defect.
- A modular ratio (about 1.2–1.25) is guidance, never a rule that overrides tested role sizes.
- G1 tests the Arabic heading weight at 600 against 700.
- Figure numerals are tabular, with the unit set smaller beside them.
- Small labels are in sentence case.

6.3 Structure.
- An 8-point rhythm; a 12-column desktop grid where useful; one reading column on phone.
- Rules and space before boxes; small radii or none.
- The TOC follows brief S10 (at most six entries; none on pages under six phone screens; the tiers in
  presentation_priority.json). Sticky on desktop only where the page is long and the evidence column is not crowded.
  Phone gets a simpler, non-sticky equivalent.

6.4 Charts: the governed contracts, with their analytical form unchanged.
- Direct labels and units; breaks annotated, never smoothed; no 3D and no gradients.
- Arabic bidi and axis integrity; the limit attached.
- The data table follows brief S3: in a disclosure, and still present in print and in screen-reader order.

6.5 Motion: state changes only, under 200 ms, and reduced motion respected.

══════════════════════════════════════════════════════════════════════
7. PAGE-FAMILY OUTCOMES: the one thing each page must make obvious
══════════════════════════════════════════════════════════════════════
- Home, in ten seconds:
  - the thesis;
  - that different evidence has different clocks;
  - the strongest starting evidence;
  - where to begin.
  Never promise that Home summarises everything known.
- Explore: find the question.
- Domain: the strongest bounded answer, its main limit, the evidence path and the next depth.
- Evidence Record: exactly what the evidence is, what it is not, its source, and its method and reproducibility.
- Compare: whether comparison is legitimate, before any difference is read as meaningful.
- Readings: a bounded argument, with its evidence inspectable.
- Measurement: which missing evidence matters for decisions, and what new measurement would change.
- Sources (/data/): the original document, and its relation to the public evidence, fast.
- Methodology: how evidence is accepted, compared, derived, corrected and bounded.
- Trust pages: CauseWay's role, corrections, accessibility, rights, the footprint and accountability.

══════════════════════════════════════════════════════════════════════
8. CAUSEWAY'S PRESENCE
══════════════════════════════════════════════════════════════════════
- Visible through: the canonical mark, the institutional layer, a disciplined colophon, and stewardship language that
  is already controlled.
- Never through: service offers, client logos, lead-generation language, promotional claims or self-congratulatory
  benchmarking.
- Colophon lines (stewardship, licence, edition, corrections, footprint, funding and independence) must already be
  controlled copy, or go Master-first before use.

══════════════════════════════════════════════════════════════════════
9. DETAIL PASS (every family, AR and EN, before G3)
══════════════════════════════════════════════════════════════════════
- Arabic: «،» «؛» «؟» and «…»; no letter-spacing, justification or hyphenation; never kashida for layout; long
  titles readable.
- Bidi and numbers:
  - Latin names and IDs isolated;
  - Western digits, per the house style;
  - numeric and time axes left to right;
  - ranges and percentages verified.
- Dates follow brief S13: human dates in all reader-facing text and clocks. ISO stays only in machine contexts:
  datetime attributes, BibTeX and RIS exports, IDs and data files.
- Headings: no widows where avoidable.
  - Domain H1s become short theses through brief S11, Master-first.
  - Elsewhere, "at most three phone lines" is a goal, never permission to shrink or rewrite governed copy outside a
    transaction.
- Links: a visible focus ring and link affordance everywhere. External-link wording comes from controlled UI copy.
- Tables: caption, units and alignment; a responsive strategy and an accessible fallback.
- Forms (the error report): labels, hints, inline errors, keyboard use, and a success state in words.
- Portable forms: print, social cards and export frames checked separately in AR and EN; nothing clipped.
- States: the empty, error and loading states of Search, Compare and the filters keep their governed technical voice.

══════════════════════════════════════════════════════════════════════
10. G1: THE DIRECTION CHALLENGE
══════════════════════════════════════════════════════════════════════
10.1 Three candidates, built outside the shipped stylesheet (design/exploration/v2/), each as a token and CSS delta
over V1, with a recorded token diff:
- (a) quiet official-statistical;
- (b) editorial-evidence;
- (c) compact source-first.
They must differ in information hierarchy and reading order, not only in colour or decoration.
- Use earlier work as challenger evidence, not as decisions. That includes the T4 "Instrument" compositions; its
  palette stays retired under DL-V1-001.
- Recover from the older V3 skin prompt only its regression checks: existing components, small visual choices,
  first-screen editorial quality and cross-page consistency. Take them only where W4 does not already cover them.
  Never revive a standalone skin or a separate design track.

10.2 Scope: the high-leverage surfaces only. Do not build Stage B three times.
- Home: the masthead; the thesis; one people-side figure; one infrastructure figure; a boundary; the question entry.
- CLM-001: the first answer; scope and clock; the boundary; source and verification.
- /data/: one curated source; one ordinary source row; the filter shell.
- One domain: payments, unless the visual contracts make another the better stress test.

10.3 Disqualifiers, applied before any scoring. A candidate is out if it:
- changes governed content;
- hides a material boundary;
- changes a visual's analytical form;
- fails AR 390;
- breaks detached use;
- adds unjustified JS;
- worsens performance without reader value;
- weakens source closure.

10.4 Scoring of the survivors, 1–5. Evidence comprehension and Arabic quality weigh more than novelty.
- Three judges: an Arabic first-time phone reader; a sceptical statistician-journalist; a World Bank or IMF data
  professional.
- Criteria: first-screen comprehension; boundary comprehension; provenance; source path; long-text readability;
  Arabic quality; calm and formal tone; implementation simplicity; distinctiveness without decoration.
- Measured columns:
  - phone screens to the first answer and in total, at AR 390, before and after (the owner's main complaint is long,
    heavy phone pages);
  - the byte delta.
- Then run the source-owner test on CLM-001 for each survivor.

10.5 The decision (D7: a recorded, criteria-based choice; the owner can veto, but approval does not block).
- Choose one direction and record it as DL-V2-001: the scorecard with its measured columns, your reasons, what was
  rejected and why, and one honest sentence on what each candidate sacrifices.
- Commit under design/evidence/v2/:
  - AR 390 and EN 1440 screenshots of Home and CLM-001 for all three candidates;
  - the /data/ and domain proofs.
- Link them from the PR so the owner can veto. Then continue to G2 without waiting.
- Roll out only the chosen direction. Delete nothing in design/exploration/v2/: it is lineage.

══════════════════════════════════════════════════════════════════════
11. G2: IMPLEMENT THE WINNER
══════════════════════════════════════════════════════════════════════
Order: shell on the proving pages → Home → domain → Evidence Record → /data/ → Reading → Methodology → propagation to
the remaining families.
- Two refinement passes on each proving family.
- Do not custom-design every route.
- Decide each class-C candidate explicitly: accepted or rejected, with its evidence.

══════════════════════════════════════════════════════════════════════
12. GATES W4 ADDS (the standing gates keep running)
══════════════════════════════════════════════════════════════════════
1. Rendered visibility (new; Playwright; AR and EN; 390 and 1440).
   - Every governed string that content parity finds in the HTML must be visible, or sit inside a native disclosure
     with a descriptive accessible label.
   - The answer, the clock, the scope, the boundary and the verification link are never inside a closed disclosure.
   - No line-clamp, overflow clip or text-overflow truncation on governed text.
   - Intentional screen-reader-only text is allowed only from a listed set, each item with its reason.
   - Add negative controls: one hidden boundary and one clamped paragraph.
   This closes the one gap W4 opens: the stylesheet can hide what the HTML still contains.
2. Drift report (new; cheap): across the W4 range, site-src/content/** and the route list are unchanged except by
   listed transactions. Any unexplained difference is a FAIL.
3. Social cards and portable frames.
   - `scripts/social_images.py --check` hashes only each card's frame HTML, not the stylesheet, fonts or logo it
     loads. A redesign would therefore pass the check while every card still shows the old design.
   - Add a template fingerprint (the frame CSS, the font files and the logo bytes) to INDEX.json, compare it in
     `--check`, and add one negative control.
   - [v3.2] Order: stabilise the design, let the fingerprint mark the stale cards, regenerate them, and check the
     actual AR and EN output, all before G3 acceptance. Do not regenerate on every iteration.
4. The performance before/after report (P6).

══════════════════════════════════════════════════════════════════════
13. DONE FOR STAGE B
══════════════════════════════════════════════════════════════════════
- DL-V2-001 is recorded and one direction is implemented.
- Every family has its memo. The proving pages have had two refinement passes. The Arabic-first detail pass is done.
- The required patterns are implemented wherever the controlled state supports them. Every candidate has an explicit
  accept or reject decision, with the SIG-2 and SIG-3 audits reported.
- [v3.2] G0's six-persona reader-job audit (brief W4 G0) is re-run on the final build. These are simulated
  walkthroughs with browser measurements; human and specialist acceptance stays with the later release gates.
- On AR 390, P1 passes on every domain and record page, or each exception is recorded. Phone screens are reported for each family, before and after.
- Green: content parity, visibility, drift, detached use, the tools and the error form, accessibility (recorded),
  browser, the budget, and every standing gate.
- design/DESIGN_INTEGRATION_V2.md tells the story in one place:
  - decisions and trade-offs;
  - the before/after gallery and the G1 scorecard;
  - what became more true, what became more complex, and what was removed;
  - what remains release-only.
- Never claim accessibility conformance, live performance or release readiness.
- Stage B ends with the stage report. Release dependencies (live host, rights, live testing in Yemen, human
  accessibility review, owner acceptance) are not Stage B blockers, and Stage B is not release approval.

══════════════════════════════════════════════════════════════════════
14. RELEASE BOUNDARY
══════════════════════════════════════════════════════════════════════
Completing Stage B is not release readiness. The live-host, rights, security, correction and named-owner gates of the
runbook still apply.

══════════════════════════════════════════════════════════════════════
15. CHANGE RECORD: v1 → v3, with the OpenAI review (v2) adjudicated against the repository
══════════════════════════════════════════════════════════════════════
Adopted from the review, where v1 was weaker:
- the charter decides presentation only;
- the three classes (A, B, C);
- the faithful-representation test replaces v1's "more carefully than their own releases";
- marks only with a class mapping;
- "checked" taken out of the evidence clock, and "not stated" only where material;
- two clocks made conditional;
- print as page 1 plus the full record: v1's single A4 page contradicted D13;
- the type ratio as guidance;
- G1 reduced to the high-leverage surfaces, with disqualifiers before scoring;
- the performance delta, and the release-stage boundary for live speed;
- compact absence labels in dense tables;
- the SIG-n names, which end the S3 / S-3 ambiguity.

Changed in v3.2 (second owner review, 11 October):
- P1 is a target outcome, with evidenced exceptions.
- SIG-7 requires independently intelligible print; the evidence-sheet page is optional.
- SIG-4 shows only publicly eligible states.
- Source-owner figures are resolved from the Master when the test runs.
- P9 adds a targeted bilingual certainty check.
- The social-card regeneration order is fixed before G3.
- G0's reader-job audit is re-run on the final build.
- Memos and refinement passes end on criteria, not on counts.

Changed in v3.1 (owner review of 11 October):
- G1 no longer stops for the owner. v3's stop conflicted with D7.
- The social-card blind spot is stated in the charter itself.
- T4 and the V3 skin prompt enter as challenger evidence and regression ideas only.
- The ambition and challenge clause is added.

Corrected in the review, from repository bytes:
1. Palette. v1 did not introduce colours: it named the live V1 tokens (theme.py, DL-V1-001). The review's "CauseWay
   shell" colours exist nowhere in the repository. Its "existing evidence palette" revives #1E5650 and #F5F1E9, which
   DL-V1-001 retired. Following it would create the third palette the review warns against.
2. Authority. The review placed the current contracts above the brief, which would block owner-authorised changes
   made through governed paths (D8, D14, brief S11). Its order is replaced by §0.
3. Dates. Brief S13 already scopes the rule: human dates in reader text; ISO in machine fields. The rule stays, as
   the owner asked.
4. Invariance. Content parity, the projection check, bilingual invariance and the literal audit already prove the
   text. The new gate targets the real W4 risk, visibility (§12.1), rather than duplicating them. The review also
   dropped a measurable P1 and phone-length reporting; both are restored.
```

*End of Appendix 1.*

---

## APPENDIX 2 — VERIFIED DIGEST OF THE OTHER AGENTS' DRAFTS (do not import the drafts)

Five independent reviewers read the drafts the other agents left on 14–16 October:
- the field journal, the institutional examination, the technical reference and the remediation specification (all
  OpenAI field-study work, written against `e46ff9eb`);
- the S11A register, the idea census, the Arabic/English copy note, the "Level 2" pilots, and two Arabic strategy
  chats;
- an Excalidraw minimum-change plan.

About 2.9 MB in all. Every claim was checked against main `274583df`. Their own ID systems (OBS/NEG/FIX/Q-H/S-nn) are
not imported.

**Already fixed on main (do not redo):**
- the edition date ("Edition of 15 October 2026"; per-record check dates);
- the four "Open evidence record" self-links;
- the CWR-012 publisher-contradiction claim;
- CWR-011's IMF 0.0 reading;
- the CWR-009 FPS/RTGS wording;
- the DEPLOYMENT.md counts;
- the public-path diagram.

Internal links: 0 broken in about 22,000.

**Refuted (do not act):** the claim that the CBY roster PDF has 12 pages. `pdfinfo` reports 20, so "20-page roster"
is right.

**Still true on main. Re-verify each in the original, then fix (PR-D unless marked S/T):**

| # | Item | Kind | Note |
|---|---|---|---|
| 1 | CWR-010 opening presents 45,460 recipients without saying it is programme-reported | Master (08) | Attribute to the programme material |
| 2 | Arabic «أجرى … مدفوعة رقمية» is unidiomatic | Master (03, 06, visual library) | e.g. «أجرى … دفعة رقمية» or «عملية دفع رقمية»; Arabic editor decides; 7 pages |
| 3 | CWR-012 Arabic: stray «و» in «وعلى نحو منفصل، ويسجل» | Master (Reading sections) | — |
| 4 | Reforms row "Operation — activity recorded … signal of unified-network activity" can read as FPS/RTGS operating | Master (04_NAV_UX) | Keep the event; remove the implied operation |
| 5 | CLM-006 `universe` drops the filtered denominator behind 91.84% (firms that did not need a loan are excluded) | Master (06) | The scope line already says it; the universe field must too |
| 6 | VIS-POS-TRANSACTIONS derives the January change (13.87%) but withholds May | Master (06 method) | Derive both or neither under one stated rule. The May PDF is image-only: read it, or withhold both |
| 7 | Methodology says every figure "is checked against the source" (overclaim) | Master (03) | State what is checked and how |
| 8 | Terms say no item-level reuse terms are recorded, while source cards show an assessment state | Master (03) | Align the two statements; no rights promotion without evidence |
| 9 | The RPW remittance-cost sources carry no licence although the catalogue states CC BY 4.0 | Master (15), only if verified at the publisher | Rights promotion needs the dated locator |
| 10 | People → CWR-012 and Finance → CWR-011 are not linked (blockers now removed) | Master (route bindings), under the two-Reading domain rule | Swap only if the new Reading serves the domain question better; record why |
| 11 | Mobile-menu language link drops query and anchor (`data-menu-lang` lacks `data-lang`; `app.js` binds only `[data-lang]`) | code (S) | Test: Compare selection survives a language switch |
| 12 | Menu control ignores the Space key | code (S) | It is the ported Waleed item |
| 13 | Search empty state always appends the regulator-names note | code (T) | Show it only when the query looks like an institution name |
| 14 | Explore: the eight measurement previews take about 2/3 of the page and bury the 11 questions | S (S7) | Title list linking to /measurement/ |
| 15 | Compare never returns a positive verdict (91/91) | T | Part 6 item 16 |
| 16 | Per-indicator World Bank locators missing (People values link to the general page) | Master (15) | Verification speed for professionals |
| 17 | Diagram and count truth: 304 vs 306, "React static compiler", self-editing diagram generator | W6 | F-18 |

**Ideas from the drafts worth adopting** (in addition to Part 6 items 13–22):
- a detachability test for every headline figure (screenshot and copy keep population, period, limit);
- the persona scripts (governor, CBY technical team, payment provider, a woman reader, MSME researcher,
  humanitarian analyst, journalist, DFI officer, auditor, Arabic phone reader) merged into the W8 audience suite;
- "Is this source fit for this question?" shown from existing passport fields (labels Master-first);
- one link between CWR-001 and /corrections/ for revisions across editions;
- the exact editorial register for every copy change (old → new, locale, Master cell, proof, test), which
  `KEY_MIGRATION.csv` and `NEW_ARABIC_SINCE_2ddbfb61.csv` already provide.

**Ideas from the drafts to reject:**
- turning unweighted counts into rates (19.9%, 39/393);
- filling the barriers chart;
- summing provider categories into "442 providers";
- subtracting enforcement subjects from rosters;
- treating MFI 2015/2020/2023 as a trend;
- a 2024 remittance "fall";
- FMIIP progress percentages;
- FPS/RTGS go-live inferred from notices;
- one global "checked to" date;
- a privacy notice written around the temporary preview host;
- importing the drafts' apparatus.

*End of brief.*
