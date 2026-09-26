# -*- coding: utf-8 -*-
"""Baseline-reproduction gate: regenerate every declared projection from a Master into memory and
compare it with the committed projection files.

  python3 -m projection.baseline_gate [--master PATH] [--json REPORT.json] [--classify CLASSIFICATION.json]

Each output is classified BYTE_IDENTICAL, JSON_EQUAL (serialisation only) or DIFFERENT. For DIFFERENT
outputs every differing JSON path is listed. A classification file may attach an explicit, reviewed
explanation to a (path, json-pointer-prefix); anything not covered is UNEXPLAINED. Exit 1 if any
output fails to build or any difference is UNEXPLAINED.
"""
import argparse
import json
import os
import re
import sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.dirname(HERE))

from projection.generator import Context, serialize  # noqa: E402
from projection import derived as D, families as F  # noqa: E402


def walk_diff(a, b, path="", out=None, limit=100000):
    out = [] if out is None else out
    if len(out) >= limit:
        return out
    if type(a) != type(b):
        out.append((path, a, b)); return out
    if isinstance(a, dict):
        for k in list(a.keys()) + [k for k in b.keys() if k not in a]:
            if k not in a or k not in b:
                out.append((f"{path}/{k}", a.get(k, "<absent>"), b.get(k, "<absent>")))
            else:
                walk_diff(a[k], b[k], f"{path}/{k}", out, limit)
        if list(a.keys()) != list(b.keys()) and set(a) == set(b):
            out.append((f"{path}/<key-order>", list(a.keys()), list(b.keys())))
    elif isinstance(a, list):
        if len(a) != len(b):
            out.append((f"{path}/<len>", len(a), len(b)))
        for i, (x, y) in enumerate(zip(a, b)):
            walk_diff(x, y, f"{path}/{i}", out, limit)
    elif a != b:
        out.append((path, a, b))
    return out


def run(master, classify=None):
    ctx = Context(master, ROOT)
    content = os.path.join(ROOT, "site-src", "content")
    cls = json.load(open(classify, encoding="utf-8")) if classify else {"explanations": []}
    results = OrderedDict()
    for e in ctx.manifest["outputs"]:
        p = e["path"]
        fn = getattr(D, e["rule_id"], None) or getattr(F, e["rule_id"], None)
        try:
            obj = fn(ctx, e)
            ctx.out[p] = obj
        except Exception as exc:  # recorded, never skipped silently
            msg = f"{type(exc).__name__}: {exc}"
            be = next((x for x in cls.get("build_errors", []) if x["path"] == p and re.search(x["error_regex"], msg)), None)
            results[p] = OrderedDict([("status", "BUILD_ERROR_CLASSIFIED" if be else "BUILD_ERROR"), ("error", msg)] + ([("class", be["class"]), ("finding", be["finding"])] if be else []))
            continue
        text = serialize(obj, e.get("trailing_newline", True))
        committed_path = os.path.join(content, p)
        cur = open(committed_path, encoding="utf-8").read() if os.path.exists(committed_path) else None
        if cur == text:
            results[p] = OrderedDict([("status", "BYTE_IDENTICAL")]); continue
        if cur is not None and json.loads(cur) == json.loads(text):
            results[p] = OrderedDict([("status", "JSON_EQUAL"), ("note", "serialisation only")]); continue
        diffs = walk_diff(json.loads(text), json.loads(cur) if cur else None)
        rows, unexplained = [], 0
        for dp, gen_v, com_v in diffs:
            ex = next((x for x in cls["explanations"] if x["path"] == p and (dp.startswith(x["pointer_prefix"]) if "pointer_prefix" in x else re.search(x["pointer_regex"], dp))), None)
            if ex is None:
                unexplained += 1
            rows.append(OrderedDict([("pointer", dp), ("generated", gen_v if not isinstance(gen_v, (dict, list)) else json.dumps(gen_v, ensure_ascii=False)[:300]),
                                     ("committed", com_v if not isinstance(com_v, (dict, list)) else json.dumps(com_v, ensure_ascii=False)[:300]),
                                     ("class", ex["class"] if ex else "UNEXPLAINED"), ("finding", ex["finding"] if ex else None)]))
        summary_rows = OrderedDict()
        for x in rows:
            k = (x["class"], x["finding"])
            summary_rows[k] = summary_rows.get(k, 0) + 1
        unexpl_rows = [x for x in rows if x["class"] == "UNEXPLAINED"]
        results[p] = OrderedDict([("status", "DIFFERENT"), ("difference_count", len(diffs)), ("unexplained", unexplained),
                                  ("differences_summary", [OrderedDict([("class", c), ("finding", f), ("count", n)]) for (c, f), n in summary_rows.items()]),
                                  ("differences", (unexpl_rows + [x for x in rows if x["class"] != "UNEXPLAINED"])[:200])])
    return ctx, results


def counterfactual(master):
    """Rule-fidelity proof: rebuild every DERIVED output from the COMMITTED upstream projections.
    If the result equals the committed output, the derivation rule is exact and every difference seen in
    the real run is attributable to (already classified) upstream differences."""
    ctx = Context(master, ROOT)
    content = os.path.join(ROOT, "site-src", "content")
    for e in ctx.manifest["outputs"]:
        p = os.path.join(content, e["path"])
        if os.path.exists(p):
            ctx.out[e["path"]] = json.load(open(p, encoding="utf-8"), object_pairs_hook=OrderedDict)
    res = OrderedDict()
    for e in ctx.manifest["outputs"]:
        if e["kind"] != "DERIVED":
            continue
        fn = getattr(D, e["rule_id"], None) or getattr(F, e["rule_id"], None)
        try:
            obj = fn(ctx, e)
        except Exception as exc:
            res[e["path"]] = OrderedDict([("status", "BUILD_ERROR"), ("error", str(exc))]); continue
        com = json.load(open(os.path.join(content, e["path"]), encoding="utf-8"))
        gen = json.loads(json.dumps(obj, ensure_ascii=False))
        if gen == com:
            res[e["path"]] = OrderedDict([("status", "RULE_EXACT")]); continue
        diffs = walk_diff(gen, com)
        if e["path"] == "page_specs.json":
            fields = OrderedDict()
            for dp, _, _ in diffs:
                parts = dp.split("/")
                key = parts[3] if parts[1] == "page_specs" and len(parts) > 3 else "/".join(parts[:4])
                fields[key] = fields.get(key, 0) + 1
            res[e["path"]] = OrderedDict([("status", "RULE_DIFFERS_IN_FIELDS"), ("fields", fields)])
        else:
            res[e["path"]] = OrderedDict([("status", "RULE_DIFFERS"), ("difference_count", len(diffs)), ("sample", [d[0] for d in diffs[:20]])])
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--master", default=os.path.join(ROOT, "authority", "Yemen_Financial_Inclusion_Evidence_Master.xlsx"))
    ap.add_argument("--json", default=None)
    ap.add_argument("--classify", default=None)
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--counterfactual", action="store_true")
    a = ap.parse_args()
    if a.counterfactual:
        print(json.dumps(counterfactual(a.master), ensure_ascii=False, indent=1)); return
    ctx, res = run(a.master, a.classify)
    summary = OrderedDict((s, sum(1 for r in res.values() if r["status"] == s)) for s in ("BYTE_IDENTICAL", "JSON_EQUAL", "DIFFERENT", "BUILD_ERROR", "BUILD_ERROR_CLASSIFIED"))
    unexpl = sum(r.get("unexplained", 0) for r in res.values())
    report = OrderedDict([("master_sha256", ctx.master_sha256), ("summary", summary), ("unexplained_differences", unexpl), ("outputs", res)])
    if a.json:
        json.dump(report, open(a.json, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if not a.quiet:
        for p, r in res.items():
            line = f"{r['status']:15s} {p}"
            if r["status"] == "DIFFERENT":
                line += f"  ({r['difference_count']} diffs, {r['unexplained']} unexplained)"
            if r["status"].startswith("BUILD_ERROR"):
                line += f"  {r['error']}"
            print(line)
    print("SUMMARY", dict(summary), "UNEXPLAINED", unexpl)
    fidelity = summary["BUILD_ERROR"] == 0 and unexpl == 0
    integrity = summary["BUILD_ERROR_CLASSIFIED"] == 0
    print("GENERATOR FIDELITY", "PASS" if fidelity else "FAIL", "| ENTRY MASTER INTEGRITY", "PASS" if integrity else "FAIL (classified entry defect)")
    ok = fidelity and integrity
    print("BASELINE GATE", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
