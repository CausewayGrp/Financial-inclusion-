# -*- coding: utf-8 -*-
"""G3 — EAD-11 steward patch (audit/release_candidate/INSTRUCTIONS.md, Part A, G3), staged for the runner's --install.

  python3 g3_stage_presentation.py <stage_dir>

Writes, from the repository's current files, the two files inside the runner's snapshot that EAD-11 changes:
  * site-src/content/presentation_priority.json — the two entries recorded under EAD-11 in design/ESCALATIONS.md, values
    unchanged, under a new top-level key "question_sets" beside the other presentation decisions (they cannot sit in
    "routes": that list is the eight Domain Answer routes, which the validator's S03 coverage check and the generator's
    tier check read). A one-line "question_sets_rule" states what the entries decide and what validates them.
  * scripts/projection/projection_manifest.json — the presentation contract's dependencies gain the question and
    interface-copy projections, which the generator now checks every named question and heading against.
The contract's formatting is kept (two-space indent, no trailing newline); the manifest's likewise (trailing newline).
"""
import json, os, sys
from collections import OrderedDict

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))

# design/ESCALATIONS.md, EAD-11, "The change, exactly." — the values, unchanged
QUESTION_SETS = [
    OrderedDict([("route", "/"), ("page_family", "Orientation"),
                 ("starting_question_ids", ["QE-002", "QE-003", "QE-005", "QE-011"])]),
    OrderedDict([("route", "/explore/"), ("page_family", "Question Entry"),
                 ("question_groups", [
                     OrderedDict([("heading_ui_id", "UI-QUESTIONS-UNDERSTAND-THE-WIDER-PICTURE"), ("question_ids", ["QE-001", "QE-003"])]),
                     OrderedDict([("heading_ui_id", "UI-QUESTIONS-PEOPLE-USE-AND-FLOWS"), ("question_ids", ["QE-002", "QE-004", "QE-007", "QE-009"])]),
                     OrderedDict([("heading_ui_id", "UI-QUESTIONS-FIRMS-INSTITUTIONS-AND-PROVIDERS"), ("question_ids", ["QE-005", "QE-006", "QE-008"])]),
                     OrderedDict([("heading_ui_id", "UI-QUESTIONS-VERIFY-AND-DECIDE-WHAT-TO"), ("question_ids", ["QE-010", "QE-011"])]),
                 ])]),
]
RULE = ("EAD-11 (steward, 2 October 2026): which governed questions Home starts from and how Explore groups all of them. "
        "Selection and grouping only: every question, cluster heading (UI-QUESTIONS-*) and destination is governed in the Master; "
        "the generator fails on an unknown question ID or heading label, and the renderer reads these sets from here.")


def load(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return json.load(fh, object_pairs_hook=OrderedDict)


def main():
    stage = sys.argv[1]
    os.makedirs(stage, exist_ok=True)
    pp = load("site-src/content/presentation_priority.json")
    if "question_sets" in pp:
        raise SystemExit("presentation_priority.json already holds question_sets")
    out = OrderedDict()
    for k, v in pp.items():
        out[k] = v
        if k == "family_contracts":
            out["question_sets_rule"] = RULE
            out["question_sets"] = QUESTION_SETS
    if "question_sets" not in out:
        raise SystemExit("family_contracts key not found")
    with open(os.path.join(stage, "presentation_priority.json"), "w", encoding="utf-8") as fh:
        fh.write(json.dumps(out, ensure_ascii=False, indent=2))

    pm = load("scripts/projection/projection_manifest.json")
    e = next(o for o in pm["outputs"] if o["path"] == "presentation_priority.json")
    if e["dependencies"] != ["content/page_sections.json", "visuals/visual_library.json"]:
        raise SystemExit(f"presentation contract dependencies not as expected: {e['dependencies']}")
    e["dependencies"] = ["content/questions.json", "content/interface_copy.json", "content/page_sections.json", "visuals/visual_library.json"]
    old = "and every referenced visual against 11, and fails otherwise."
    if old not in e["transformation"]:
        raise SystemExit("presentation contract transformation text not as expected")
    e["transformation"] = e["transformation"].replace(old, "every referenced visual against 11, and every question set (EAD-11) against the governed questions and the UI-QUESTIONS-* headings, and fails otherwise.")
    with open(os.path.join(stage, "projection_manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(pm, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("staged:", os.path.join(stage, "presentation_priority.json"), os.path.join(stage, "projection_manifest.json"))


if __name__ == "__main__":
    main()
