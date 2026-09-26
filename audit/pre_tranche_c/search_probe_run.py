# -*- coding: utf-8 -*-
"""Run the canonical search probe (scripts/search_canonical_probe.json) against one or two content states.

  python3 audit/pre_tranche_c/search_probe_run.py [<before_content_dir>] [--out <file.json>]

Scoring uses the Tranche B browser-scoring mirror (audit/tranche_b_execution/post_execution_acceptance.search), which is
independent of the validator's mirror (scripts/validate.py _r4search, gate P2-G01). Importing that module does not run
it. Grades follow the probe's own rule: PASS = first expected destination at rank 1-3; WEAK = rank 4-10; FAIL = absent.
With a before directory the same probe is applied to both states, so the comparison measures the index, not the probe.
"""
import json, os, sys
from collections import Counter, OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "audit", "tranche_b_execution"))
from post_execution_acceptance import search, PROBE as LEGACY_PROBE  # noqa: E402  (mirror only; main() is not executed)


def load(content_dir, name):
    d = json.load(open(os.path.join(content_dir, "content", name), encoding="utf-8"))
    return d if isinstance(d, list) else (d.get("records") or d.get("items") or [])


def grade(content_dir, probe):
    recs, aliases = load(content_dir, "search_index.json"), load(content_dir, "search_aliases.json")
    rows, tally = [], Counter()
    for it in probe["intents"]:
        row = OrderedDict([("query_en", it["query_en"]), ("query_ar", it["query_ar"]), ("expected", it["expected"])])
        for lang in ("en", "ar"):
            got = search(recs, aliases, it["query_" + lang], lang)
            ranks = [i + 1 for i, r in enumerate(got) if r in it["expected"]]
            best = ranks[0] if ranks else None
            g = "PASS" if best and best <= 3 else ("WEAK" if best else "FAIL")
            tally[g] += 1
            row[lang] = OrderedDict([("grade", g), ("best_rank", best), ("top3", got[:3])])
        rows.append(row)
    return OrderedDict([("grades", dict(tally)), ("search_records", len(recs)), ("aliases", len(aliases)), ("intents", rows)])


def legacy(content_dir):
    """The Tranche B 28-term probe, whose expected sets name only explanatory pages: kept to show ranking movement."""
    recs, aliases = load(content_dir, "search_index.json"), load(content_dir, "search_aliases.json")
    tally, weak = Counter(), []
    for en, ar, exp in LEGACY_PROBE:
        for lang, q in (("en", en), ("ar", ar)):
            got = search(recs, aliases, q, lang)
            ranks = [i + 1 for i, r in enumerate(got) if r in exp]
            best = ranks[0] if ranks else None
            g = "PASS" if best and best <= 3 else ("WEAK" if best else "FAIL")
            tally[g] += 1
            if g != "PASS":
                weak.append([lang, q, best])
    return OrderedDict([("grades", dict(tally)), ("not_pass", weak)])


def main():
    args = sys.argv[1:]
    out = None
    if "--out" in args:
        i = args.index("--out"); out = args[i + 1]; del args[i:i + 2]
    probe = json.load(open(os.path.join(ROOT, "scripts", "search_canonical_probe.json"), encoding="utf-8"))
    rep = OrderedDict([("probe", "scripts/search_canonical_probe.json"), ("rule", probe["rule"]),
                       ("mirror", "Tranche B browser-scoring mirror (independent of validate.py)")])
    if args:
        rep["before"] = grade(args[0], probe)
    rep["after"] = grade(os.path.join(ROOT, "site-src", "content"), probe)
    rep["legacy_28_term_probe"] = OrderedDict(([("before", legacy(args[0]))] if args else []) + [("after", legacy(os.path.join(ROOT, "site-src", "content")))])
    if args:
        changed = []
        for b, a in zip(rep["before"]["intents"], rep["after"]["intents"]):
            for lang in ("en", "ar"):
                if b[lang]["grade"] != a[lang]["grade"] or b[lang]["best_rank"] != a[lang]["best_rank"]:
                    changed.append(OrderedDict([("query", b["query_" + lang]), ("lang", lang), ("before", [b[lang]["grade"], b[lang]["best_rank"]]),
                                                ("after", [a[lang]["grade"], a[lang]["best_rank"]])]))
        rep["changed"] = changed
    for k in ("before", "after"):
        if k in rep:
            print(k, rep[k]["grades"], "records", rep[k]["search_records"], "aliases", rep[k]["aliases"])
    print("legacy 28-term probe", {k: v["grades"] for k, v in rep["legacy_28_term_probe"].items()})
    if out:
        with open(out, "w", encoding="utf-8") as f:
            json.dump(rep, f, ensure_ascii=False, indent=1)
    sys.exit(1 if rep["after"]["grades"].get("FAIL") else 0)


if __name__ == "__main__":
    main()
