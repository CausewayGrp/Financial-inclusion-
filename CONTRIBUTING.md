# Working on this repository

This is the change protocol for everyone who writes to the repository: the steward session, Claude Code, Claude Design,
independent reviewers and people. It owns the *how*. What the product is and where it stands are in `README.md`; the
durable rules are in `authority/CORE_CONSTITUTION.md`.

## 1. The rule underneath everything

The Production Master (`authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx`) is the only authority for facts,
meaning, units, universes, periods, sources, rights, status and controlled public copy. Everything else is derived from it
or implements it. A content defect is fixed in the Master first:

```text
SOURCE → VERIFY → ADJUDICATE → MASTER FIRST → REGENERATE → SEMANTIC PARITY → PUBLIC ACCEPTANCE
```

GitHub `main` is the only current state of the repository. Work that exists only in a chat, a ZIP, a Drive folder or an
unpushed clone does not exist yet. ZIPs are *outputs* of checkpoint tags (§6), never working copies.

## 2. Who owns what, and how it changes

| Path | Role | How it changes |
|---|---|---|
| `authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx` | Authority | Only through a transaction and the runner (§4) |
| `authority/CORE_CONSTITUTION.md` | Durable principles | Rarely, by explicit decision; never mutable state |
| `authority/AUTHORITY.json`, `authority/YFI_CURRENT_PROJECT_CONTEXT.json` | Current-state pointers | Hashes and counts by `scripts/rebind_authority.py` (the runner calls it); programme state by the steward |
| `site-src/content/**` | Controlled projections | Never by hand; `scripts/generate_projections.py` writes them from the Master |
| `dist/**` | Generated static site | Never by hand; `scripts/build.py`; committed so every public change is reviewable |
| `audit/PUBLIC_LITERAL_CLOSURE.json` | Generated audit | Never by hand; `scripts/audit_public_literals.py` |
| `scripts/`, `site-src/app.js`, `site-src/styles.css` | Generator, build, gates, runtime | Directly, with the full gate run |
| `handoff/` | Design → Code recipient package | DRAFT until R8.6; changed only by the programme |
| `design/architecture/` | Derived diagrams | `scripts/architecture_diagrams.py` |
| `audit/`, `docs/` | Lineage and records | Append; never rewrite a historical record (add an addendum or erratum) |
| `FINAL_REPOSITORY_MANIFEST.json` | Classification of every tracked file | `python3 scripts/repository_manifest.py` after adding, moving or deleting a file |
| `SHA256SUMS.txt` | Checksum manifest | `python3 scripts/checksums.py` after every change (after the repository manifest) |

## 3. Branches, commits and history

- **`main` is always green and always a coherent governed state.** Each commit is one atomic session: a Master transaction
  with its regenerated outputs, or one self-contained code or documentation change. Never commit half a transaction.
- **Never rewrite `main` or a `checkpoint/*` tag.** No force-push, no amend or rebase of pushed commits. Mistakes are fixed
  by a new commit.
- **Branches** for work that is reviewed before it lands, or that runs in parallel with an open review:

  | Branch | Use |
  |---|---|
  | `tx/<id>-<slug>` | A Master transaction or a set of them, e.g. `tx/tc-j-openai-corrections` |
  | `review/<reviewer>-<slug>` | Intake of an external review or package, e.g. `review/reading-package` |
  | `r8.5/<slug>`, `r8.6/<slug>` | Programme stages |
  | `design/<gate>-<slug>` | Claude Design gates D1–D7 |
  | `code/<slug>` | Claude Code implementation after the Design package is accepted |

  The Master is a binary file and cannot be merged. When two branches both change it, the later one is **replayed**: its
  transaction scripts run again on the new `main` (they are exact-value-guarded, so a conflict fails loudly instead of
  merging silently).
- **Commit messages** follow Conventional Commits, `type(scope): summary`, with types `fix`, `feat`, `docs`, `refactor`,
  `test`, `ci`, `build`, `chore` and scopes such as `master`, `generator`, `build`, `runtime`, `gates`, `handoff`,
  `design`, `audit`, `repo`. A commit that changes the Master ends with trailers, so the whole authority chain can be read
  from `git log`:

  ```text
  fix(master): TC-J close the OpenAI Tranche C findings

  <what changed and why, in a few lines>

  Transaction: TC-J
  Master-Before: f0150122895d
  Master-After: <first 12 hex of the new Master>
  Findings: OAI-C-01, OAI-C-02
  ```

  The whole Master chain, newest first:

  ```bash
  git log --grep='^Master-After:' --date=short --format='%h %ad %(trailers:key=Transaction,valueonly,separator=) %(trailers:key=Master-Before,valueonly,separator=) → %(trailers:key=Master-After,valueonly,separator=)'
  ```

  Transactions before the move to Git (TC-S1 … TC-I and earlier) are recorded in their run reports under `audit/`.

## 4. Changing the Master

1. Write the transaction script under the current stage's audit folder (pattern: `audit/tranche_c/tc_*.py`, built on
   `audit/pre_tranche_c/ptc_lib.py` `Session` and `audit/tranche_c/tc_lib.py`). Every cell write states the value it expects
   to replace.
2. Stage outside the repository and commit through the runner, which snapshots, installs, regenerates, rebinds, builds,
   audits, redraws the diagrams, validates and checks the generator — and rolls everything back on any failure:

   ```bash
   STAGE=$(mktemp -d)
   PYTHONDONTWRITEBYTECODE=1 python3 audit/<stage>/tc_x_name.py \
       authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx "$STAGE/master.xlsx" "$STAGE/ledger.json" "$STAGE/work"
   PYTHONDONTWRITEBYTECODE=1 python3 audit/tranche_b_execution/run_stage.py TC-X "$STAGE/master.xlsx" "$STAGE/snap" \
       "$(date -u +%Y-%m-%dT%H:%M:%SZ)" audit/<stage>/runs/TC-X_RUN_REPORT.json [--install "$STAGE/file=repo/relative/path" ...]
   cp "$STAGE/ledger.json" audit/<stage>/runs/TC-X_MASTER_LEDGER.json
   ```
3. Run the remaining gates (§5), then `git add -A && python3 scripts/repository_manifest.py && python3 scripts/checksums.py`, add a `docs/CHANGELOG.md` entry and commit with the
   trailers above.

During a transaction, files inside the runner's snapshot (authority, `site-src/content`, `handoff`, README, checkpoint,
`dist`, the literal closure, `master_structure.json`, `projection_manifest.json`, `controlled_inputs`,
`design/architecture`) change only via `--install`. Code outside it (`build.py`, `app.js`, `styles.css`, `derived.py`, `families.py`, `validate.py`, the literal
allowances) is edited directly and survives a rollback.

## 5. The gates

CI (`.github/workflows/verify.yml`) runs all of these on every push to `main` and every pull request. Run them locally
before you commit; together they take about a minute.

```bash
python3 -m pip install -r requirements.txt && python3 -m playwright install chromium    # once
export PYTHONDONTWRITEBYTECODE=1
python3 scripts/checksums.py --check                   # manifest lists every tracked file with its current hash
python3 scripts/generate_projections.py --check        # the Master regenerates every projection byte for byte
python3 -m unittest discover -s scripts/projection/tests -t .
python3 scripts/build.py && python3 scripts/audit_public_literals.py   # then `git status` must be clean
python3 scripts/validate.py                            # WEBSITE REPOSITORY VALIDATION PASS (incl. R85-G*, RP-G*, F6-G*)
python3 scripts/repository_manifest.py --check         # every tracked file classified
python3 scripts/tests/test_literal_audit_determinism.py
python3 audit/pre_tranche_c/source_lineage_truth_test.py
python3 scripts/architecture_diagrams.py --check
python3 audit/tranche_c/checks/bilingual_invariance.py # 0 differing English/Arabic page pairs (exit 1 otherwise)
python3 scripts/tests/test_public_tools.py             # browser
python3 audit/tranche_c/checks/viewport_acceptance.py  # browser
```

## 6. Checkpoints and packages

A checkpoint is a governed state handed to an independent reviewer or to Design. Create it as a signed, annotated tag
on a green `main` commit and push the tag:

```bash
git tag -s checkpoint/<lower-kebab-state> -m "<one-line state>" -m "<hashes, programme state, what is held>"
git push origin checkpoint/<lower-kebab-state>
```

`.github/workflows/checkpoint.yml` re-runs every gate on the tag, builds
`Yemen_Financial_Inclusion_Evidence_<STATE>.zip` (one root folder, no nested ZIP), verifies it from an empty extraction
and attaches it with its SHA-256 to a pre-release. The same ZIP can be built anywhere, byte for byte:

```bash
git archive --format=zip --prefix=Yemen_Financial_Inclusion_Evidence/ -o Yemen_Financial_Inclusion_Evidence_<STATE>.zip checkpoint/<state>
```

The name `checkpoint/design-handoff-ready` (and so `Yemen_Financial_Inclusion_Evidence_DESIGN_HANDOFF_READY.zip`) is
reserved for the close of R8.6 and is used only after its Definition of Done is met.

## 7. Sessions: start, finish, stay in sync

Every session, whoever runs it:

1. **Start.** `git fetch origin` and work from `origin/main` (or your branch rebased on it). Run
   `python3 scripts/checksums.py --check` and the validator before the first change. If the state differs from what you
   were told to expect, diagnose first; never restore an older state because a document names an older hash.
2. **Work** in atomic sessions (§3, §4).
3. **Finish.** Gates green, `SHA256SUMS.txt` regenerated, changelog entry, commit, `git push`. For a state that leaves
   the repository (a review package, a Design handoff) push a checkpoint tag as well.

External inputs (a reviewer's findings, a Reading package, a Design package) enter on a `review/` or `design/` branch and
land through the same gates. Drive copies are lineage only (`EXTERNAL_REPOSITORY_SYNC_PENDING`); they are never
updated from here and never treated as current.

## 8. Claude Design and Claude Code

Until R8.6 closes, the prompts in `handoff/` are DRAFT and must not be executed. From R8.6 the single start path is
`handoff/README_FIRST.md` → `handoff/CLAUDE_DESIGN_MASTER_PROMPT.md`.

- **Claude Design** works on `design/<gate>-<slug>` branches, one pull request per gate (D1–D7), each leaving a runnable
  checkpoint. It owns visual and interaction decisions and writes its package under `design/`. It does not edit
  `authority/`, `site-src/content/`, `dist/` or `audit/`. Controlled truth that looks wrong is raised as
  `ESCALATE_TO_MASTER`; a missing semantic input as `NEEDS_CONTROLLED_CONTENT`. Both are fixed Master-first by the steward.
- **Claude Code** starts only from an accepted Design package, works on `code/<slug>` branches and implements; it does not
  redesign and does not create a second content model.

## 9. Known pitfalls (each one has already cost a session)

- Adding a column to a Master sheet also needs an updated `scripts/projection/master_structure.json` installed with
  `--install` (keep its one-space JSON indent), or generation fails the header contract.
- A new public number without a bound, source-traced record fails the literal audit and the runner rolls back. A product
  constant needs an entry in `scripts/literal_audit_allowances.json` with route, context and reason.
- `03_PAGE_SECTIONS` rows are split per language: the English and Arabic of one section are different rows (`section_row`).
- Substring replacements must match exactly once; an earlier edit can make a replacement apply twice.
- Python 3.11: an f-string cannot contain a backslash inside `{}`.
- README, the checkpoint and the handoff files may print only the current Master and Page Specs SHA-256 or the labelled
  Drive lineage pair; write any other hash as a short prefix.
- `scripts/rebind_authority.py` needs `--timestamp`.
- Never run `audit/tranche_b_execution/post_execution_acceptance.py`: it rewrites historical Tranche B audit files.
- Validator "first-load exclusions mismatch": `site-src/content/presentation_priority.json` must match the page's
  first-load sections (it is inside the runner snapshot; change it with `--install`). "Stale count": update the count
  phrase to the derived value in `site-src/content/content/public_inventory.json`.
- Guard every deletion: `rm -rf "${VAR:?}/…"`.

## 10. Repository settings (administrators)

Recommended settings, applied once in GitHub:

- **Ruleset on `main`:** block force pushes and deletion; require linear history; require the status checks
  `Governance gates` and `Browser acceptance`; require pull requests for everyone except the named steward session.
- **Ruleset on tags `checkpoint/*`:** block updates and deletion, so every reviewed state stays addressable.
- **Actions:** allow only actions created by GitHub; default workflow token read-only (the checkpoint job requests write for
  itself).
- **Security:** Dependabot alerts and security updates on; secret scanning on where available.
- **Visibility:** private. Audit records name withheld sources and material without a public locator; the repository must
  not become public without a publication review.
