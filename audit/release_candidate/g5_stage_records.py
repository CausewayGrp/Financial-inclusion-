# -*- coding: utf-8 -*-
"""G5 — records reconciliation (audit/release_candidate/INSTRUCTIONS.md, Part A, G5): the four files inside the runner's
snapshot, staged for audit/tranche_b_execution/run_stage.py --install. Everything else G5 changes is outside the
snapshot and edited in place (audit/RECORDS_RECONCILIATION_2026-10-02.md lists both).

  python3 g5_stage_records.py <stage_dir>

  * handoff/IMPLEMENTATION_MANIFEST.json — implementation_target.ui names the shipped renderer (C9, A7 item 3).
  * authority/YFI_CURRENT_PROJECT_CONTEXT.json — the sustainability pointer names the implemented-runtime measurement;
    only the host remains (C9, A7 item 12).
  * OPENAI_REENTRY_CHECKPOINT.md §4 — the next work is no longer Claude Design's.
  * README.md — the status names what the release-candidate pull request changes, the remaining open items as
    release-time only once it lands, and DEBT-016 as closed.
Every replacement states the text it expects to find, exactly once.
"""
import json, os, sys
from collections import OrderedDict

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def swap(text, old, new, where):
    if text.count(old) != 1:
        raise SystemExit(f"{where}: expected text found {text.count(old)} times: {old[:80]!r}")
    return text.replace(old, new)


def main():
    stage = sys.argv[1]
    os.makedirs(stage, exist_ok=True)

    him = json.loads(read("handoff/IMPLEMENTATION_MANIFEST.json"), object_pairs_hook=OrderedDict)
    if him["implementation_target"]["ui"] != "React static pre-render/export":
        raise SystemExit(f"implementation_target.ui not as expected: {him['implementation_target']['ui']!r}")
    him["implementation_target"]["ui"] = ("Python production renderer in scripts/yfie (driven by scripts/build.py): static, "
                                         "pre-rendered HTML for every controlled route, with the one runtime site-src/app.js")
    with open(os.path.join(stage, "IMPLEMENTATION_MANIFEST.json"), "w", encoding="utf-8") as fh:
        fh.write(json.dumps(him, ensure_ascii=False, indent=2) + "\n")

    ctx = json.loads(read("authority/YFI_CURRENT_PROJECT_CONTEXT.json"), object_pairs_hook=OrderedDict)
    old = "docs/SUSTAINABILITY_METHOD.md; audit/SUSTAINABILITY_PRE_DESIGN_BASELINE.json (pre-design reference build; remeasure after Design and deployment)"
    if ctx["programme_state"]["tranche_c"]["sustainability"] != old:
        raise SystemExit("context sustainability pointer not as expected")
    ctx["programme_state"]["tranche_c"]["sustainability"] = (
        "docs/SUSTAINABILITY_METHOD.md; audit/SUSTAINABILITY_PRE_DESIGN_BASELINE.json (pre-design reference build); "
        "docs/SUSTAINABILITY_IMPLEMENTED_RUNTIME.json (the implemented runtime, remeasured 29 September 2026; the logo "
        "derivatives' effect in audit/release_candidate/page_weight/PAGE_WEIGHT_EAD-03.md); only the host remains to be measured")
    with open(os.path.join(stage, "YFI_CURRENT_PROJECT_CONTEXT.json"), "w", encoding="utf-8") as fh:
        fh.write(json.dumps(ctx, ensure_ascii=False, indent=2) + "\n")

    cp = read("OPENAI_REENTRY_CHECKPOINT.md")
    cp = swap(cp, "- **Sessions:** none open. D7 is complete; the next work is Claude Design's (gates D0–D7 in the brief).",
              "- **Sessions:** the Design programme is complete (D7 accepted by the owner, 2 October 2026) and the production "
              "runtime is merged (pull request #8). The release-candidate pull request (#9) implements the owner's decisions of "
              "2 October 2026; the work after it is release-time only (`FINAL_OPEN_ITEMS_REGISTER.md` §2: hosting and public "
              "origin, live security headers, the currentness re-run at the release date, the owner's release acceptance).",
              "checkpoint §4")
    with open(os.path.join(stage, "OPENAI_REENTRY_CHECKPOINT.md"), "w", encoding="utf-8") as fh:
        fh.write(cp)

    rd = read("README.md")
    lines = rd.split("\n")
    def row(label, value):
        i = [k for k, l in enumerate(lines) if l.startswith(f"| **{label}** |")]
        if len(i) != 1:
            raise SystemExit(f"README row {label!r} found {len(i)} times")
        lines[i[0]] = f"| **{label}** | {value} |"
    row("Now", "**The release candidate.** Pull request #9 (branch `code/release-candidate-fixes`) implements the owner's "
               "decisions of 2 October 2026 ([`audit/OWNER_DECISIONS_2026-10-02.md`](audit/OWNER_DECISIONS_2026-10-02.md)) and "
               "the after-merge conditions of pull request #8: three Master transactions (RC-1 truth fixes, RC-2 trust copy, RC-3 "
               "governed interface strings), the question sets in the presentation contract (EAD-11), the logo's web-size "
               "derivatives (EAD-03; cold pages from about 10.3 MB to under 0.7 MB), each figure's boundary printed once (A3), "
               "the retired frame removed from `/reforms/` (A5), the search status with its true total and a result-type filter "
               "(A6), and these records reconciled ([`audit/RECORDS_RECONCILIATION_2026-10-02.md`](audit/RECORDS_RECONCILIATION_2026-10-02.md)); "
               "Part B of the same pull request finishes, challenges and hardens the product. The brief: "
               "[`audit/release_candidate/INSTRUCTIONS.md`](audit/release_candidate/INSTRUCTIONS.md). The Design programme is "
               "complete (D0–D7, pull request #7; the owner's D7 acceptance of 2 October 2026) and the production runtime is "
               "merged (pull request #8) — see [Design programme](#design-programme--current-state)")
    row("Next", "Independent review of pull request #9. Once it lands, the open items that remain are release-time only "
                "([`FINAL_OPEN_ITEMS_REGISTER.md`](FINAL_OPEN_ITEMS_REGISTER.md) §2): hosting and the public origin, live "
                "security headers, the currentness re-run at the release date, and the owner's release acceptance; the "
                "post-launch items carry their dispositions in the register")
    rd = "\n".join(lines)
    rd = swap(rd, "**DEBT-016** (the logo's file weight) blocks release and waits on the owner (EAD-03; approved 2 October 2026, applied in the release-candidate pull request);",
              "**DEBT-016** (the logo's file weight) closed on 2 October 2026 in the release-candidate pull request (EAD-03: pure resamples of the unchanged master on every surface);",
              "README What remains")
    rd = swap(rd, "the Code brief, started on the accepted Design package (owner's acceptance recorded 2 October 2026); the production runtime is pull request #8",
              "the Code brief, started on the accepted Design package (owner's acceptance recorded 2 October 2026); the production runtime is merged (pull request #8) and the release candidate is pull request #9",
              "README start-here row")
    with open(os.path.join(stage, "README.md"), "w", encoding="utf-8") as fh:
        fh.write(rd)
    print("staged:", ", ".join(sorted(os.listdir(stage))))


if __name__ == "__main__":
    main()
