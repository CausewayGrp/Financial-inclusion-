# Owner decisions — 17 October 2026 (takeover brief, Part 1)

Recorded verbatim from the owner's takeover brief of 17 October 2026 (`audit/close_out/TAKEOVER_BRIEF_2026-10-17.md`), under its Part 1 instruction: "In PR-C (Part 5), commit Part 1 verbatim as `audit/OWNER_DECISIONS_2026-10-17.md`." Sending the brief is the owner's dated decision. Nothing below is rewritten; later decisions are appended as dated sections.

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

## Appended 17 October 2026, 18:10 Asia/Riyadh — OD-1017-14: prospective hosting selection and the public-address convention

Recorded by the steward from the owner's decision given in conversation on 17 October 2026 (17:33–18:10 Riyadh), after
PR #57 merged at `ce4ae5c8`. This decision is **prospective**: nothing in the build, `site-src/deployment.json`, the
workflows or DNS changes under it. Implementation is Stage C work (BRIEF W8, `docs/RELEASE_RUNBOOK.md`) and happens
only when that stage reaches it. The directive's final-line condition (`audit/OWNER_DIRECTIVE_2026-10-17.md`, §13) is
unchanged.

**OD-1017-14(a) — Host.** Production hosting is DigitalOcean: the Droplet that already serves `causewaygrp.com`,
managed through EasyPanel. This supersedes, prospectively, the 16 October "hosting unselected" decision
(`audit/OWNER_DECISIONS_2026-10-16.md`). It re-selects DigitalOcean but **not** the 3 October route: no App Platform
app, no corporate proxy, no subpath. The applicable shape is the runbook's Route 3: the product on its own subdomain
at the root, our nginx serving the header contract of `_headers` (`scripts/hosting_nginx.py`,
`site-src/hosting/digitalocean/Dockerfile`, proven by `scripts/tests/test_digitalocean_hosting.py` and
`test_security_headers.py --base`), TLS terminated by the Droplet's front proxy, and nothing set or served by the
corporate application.

**OD-1017-14(b) — Public origin.** `https://yemen-financial-inclusion.causewaygrp.com`, with no path.
`public_origin` stays `null`, `pre_release` stays `true` and `public_downloads` stays `false` until the Stage C release
steps set them under the runbook. The name is decided now so that no Stage B or Stage C work designs for a subpath,
and so that social cards, canonical URLs and citation strings have one target.

**OD-1017-14(c) — Convention for CauseWay evidence products.** Every evidence product is its own static site on its
own subdomain at the root, named `<country>-<topic>.causewaygrp.com`: lowercase English words, hyphenated, no
acronyms, no internal project names. One repository, one site, one origin; origins are never shared between products.
`evidence.causewaygrp.com` is reserved for a later static index of the family and is used by no product. A product's
name is fixed before its `public_origin` is set and is never changed after its first external citation, because the
cite tool and every published citation depend on it.

**OD-1017-14(d) — DNS.** The owner holds an A record `yfie.causewaygrp.com` pointing at the Droplet. It is to be
replaced by `yemen-financial-inclusion.causewaygrp.com` at the owner's convenience, before Stage C. `yfie` is an
internal acronym and appears in no public copy, metadata or address.

**OD-1017-14(e) — F-06.** With DigitalOcean selected, the owner disconnects the Cloudflare "Workers Builds" app from
the repository in the Cloudflare dashboard. Until then the check stays ignored and is never made required.

**OD-1017-14(f) — Precondition for Stage C, for the web administrator.** The corporate application's `session`
cookie must be host-only (no `Domain=.causewaygrp.com` attribute). A parent-domain cookie would be sent by browsers
to the evidence subdomain, which sets no cookie and promises none on its privacy page. This is checked before the
first deployment.

**OD-1017-14(g) — Corporate CMS.** The corporate content system on the same Droplet is outside this product. The
Production Master remains the sole authority; no CMS sits in the publication path.

**Not decided here:** repository visibility (F-12, OD-1017-13), public downloads, release timing. These remain open
owner items and are repeated in each phase report.

## Appended 18 October 2026 — OD-1018: presentation interlude before Stage C (the canvas "Yemen FI Evidence Home")

Recorded by the Claude Code run from the owner's written direction of 18 October 2026, which is the source; this entry
restates it and decides nothing beyond it. **Scope:** how the site looks, on every page family, after the visual
direction of the owner's Claude Design canvas "Yemen FI Evidence Home" (three boards — Arabic at 1440 and 390, English at
1440 — and a handoff sheet; the canvas draws Home only). **Unchanged:** every governed word and number, the Production
Master, the information structure, the tools, the routes, the IDs and `data-*` hooks, every gate, the publication flags,
`public_origin` and the disabled deployment. The boards are a look, not content: every string and number comes from the
generator; a string that is not already governed goes Master-first in both languages or is left out. One pull request;
the run does not merge, deploy or begin Stage C. Draft PR #63 (the Folio proof) is superseded; its fonts and subset
recipe are reused, its treatment is not, and its branch stays as lineage.

DL-V2-001 (G1, 18 October 2026) chose A · Register. **This decision replaces A · Register's visual language and keeps
its information hierarchy; it is an owner decision, not a G1 result.**

**OD-1018 D1 — Visual language, site-wide.** The canvas's tokens, type scale, spacing, radii, header, footer, buttons,
search field, eyebrows, cards and bands replace A · Register's styling on every family. The information hierarchy, the
order rules and the evidence unit's composition are unchanged.

**OD-1018 D2 — Type.** Noto Naskh Arabic 600 (the subset without Latin) for Arabic display and IBM Plex Serif 600 for
English display; IBM Plex Sans and IBM Plex Sans Arabic for body text and the interface. Only the display face of the
page's edition is loaded; the canvas's Source Serif 4 and Naskh 700 are not used. Figures use Western tabular digits from
a face already loaded on the page, with no extra font file; at most four font files per page. The upstream versions, the
reproducible subset recipe, the hashes and the licences are recorded, #63's outdated font README is reconciled, and glyph
coverage is verified for every generated heading in both editions.

**OD-1018 D3 — Colour.** Every canvas colour maps to its nearest shipped V1 token; no new literals. The only new tokens
are the eight hub tints, used on Home's topic cards and on each domain page's masthead band, never on data and never
carrying meaning. Every text pair passes the existing contrast gate.

**OD-1018 D4 — Home.** The canvas composition, with every governed section kept. At phone widths the three figures come
before the topic grid, in matching DOM and visual order (a necessary adaptation of the canvas). Sections 05 and 06 stay
below the fold as generated. Topic cards use the hub short theses (governed S11 text) as blurbs. Owner exceptions to
directive §5, for Home only: the 4 × 2 topic cards with one inline stroke icon each; the figure cards; the hero
illustration as inline SVG, `aria-hidden`, with recorded provenance. At Arabic 390 the illustration is dropped if it
pushes the first evidence unit below the first screen.

**OD-1018 D5 — Extension to the families the canvas did not draw.** The canvas's header and footer on every page. The
evidence unit everywhere (domain pages, records, Compare) takes the anatomy of the canvas figure card, with value,
scope, period, limit and verification link together. Every "what this does not establish" block takes the canvas
caution band; every source and verification block takes the canvas verify band. Questions hub items take the canvas
question cards; the Readings index and Reading heads take the canvas reading row. Section labels take the canvas
eyebrows; body measure, rhythm and type scale come from the canvas tokens, with an interior heading scale one step
below Home's. Anything with no canvas analogue takes the nearest canvas component, never a new pattern; before building,
one line per family names the components it uses (design record §9).

**OD-1018 D6 — Logo.** Existing approved assets only; nothing from the canvas runtime, its export or its logo crop ships.

**Held by this decision, unchanged:** B1's structure rules S1–S13; B2's tools (search, Compare, cite, report an error,
facet counts); no-JavaScript behaviour; print; lists stay lists (/data/, the evidence directory, Measurement and every
other long list keep rule-separated rows, never card grids); every figure keeps its governed visual contract and
source-reference closure, and where the canvas's drawing differs from a contract (the POS figure) the contract wins.
**Not decided here:** F-12 (repository visibility) and F-06 (the Workers check) remain open owner items.
