#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Every exported value matches the governed projections (Part B B14 a).

  python3 scripts/tests/test_exports.py [--out DIR]   # builds the exports into DIR (default: a temporary folder)

Builds the exports with `scripts/exports.py`, then checks them by a separate path:
- every field of every row equals the projection's value for the same record (lists joined by "; ");
- the CSV and the JSON of each dataset hold the same rows;
- every row's provenance names the current Production Master's SHA-256, and each locator is its source's public
  original locator, in the same order as its source IDs;
- no source without a public locator is named anywhere, and a source that is not display-ready carries no title;
- the switch is off: `public_downloads` is false and `dist/` holds no download.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import exports as X  # noqa: E402

C = ROOT / "site-src" / "content"


def load(rel):
    return json.loads((C / rel).read_text(encoding="utf-8"))


def j(v) -> str:
    if v is None:
        return ""
    return "; ".join(j(x) for x in v) if isinstance(v, (list, tuple)) else str(v)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="")
    args = ap.parse_args()
    out = Path(args.out) if args.out else Path(tempfile.mkdtemp(prefix="yfie-exports-"))
    X.build(out)
    problems = check(out)
    # the checker is proved too: one planted wrong value (in both the JSON and the CSV) must be reported
    planted = Path(tempfile.mkdtemp(prefix="yfie-exports-planted-"))
    X.build(planted)
    rows = json.loads((planted / "evidence_records.json").read_text(encoding="utf-8"))
    rows[0]["summary_en"] += " (altered)"
    X.write(planted, "evidence_records", rows)
    if not any("evidence_records" in p and "summary_en" in p for p in check(planted)):
        problems.append("the checker did not report a planted wrong value")
    manifest = json.loads((out / "MANIFEST.json").read_text(encoding="utf-8"))
    counts = manifest["datasets"]
    # owner instructions of 3 October 2026, 09:50, E3: the exports carry the licence
    lic = (out / "LICENCE.txt").read_text(encoding="utf-8") if (out / "LICENCE.txt").exists() else ""
    if (manifest.get("licence") or {}).get("id") != "CC-BY-4.0" or "CC BY 4.0" not in lic or "creativecommons.org/licenses/by/4.0" not in lic:
        problems.append("exports: MANIFEST.json and LICENCE.txt must carry the CC BY 4.0 licence (owner instructions, 3 October 2026, E3)")
    for p in problems[:40]:
        print("FAIL", p)
    print(f"EXPORTS: {'PASS' if not problems else 'FAIL'} — " + ", ".join(f"{k} {v}" for k, v in counts.items())
          + f"; every value checked against the projections; a planted wrong value caught; not published ({len(problems)} problems)")
    return 1 if problems else 0


def check(out: Path) -> list[str]:
    problems: list[str] = []
    sha = hashlib.sha256((ROOT / "authority" / "Yemen_Financial_Inclusion_Evidence_Master.xlsx").read_bytes()).hexdigest()
    lib = {s["source_id"]: s for s in load("sources/source_library.json")}
    def loc(sid):
        u = str((lib.get(sid) or {}).get("primary_url") or "").strip()
        return u if u.lower().startswith(("http://", "https://")) else ""

    truth = {
        "evidence_records": ({o["object_id"]: o for o in load("evidence/evidence_objects.json")}, "object_id"),
        "public_claims": ({c["claim_id"]: c for c in load("evidence/public_claims.json")}, "claim_id"),
        "sources": (lib, "source_id"),
        "chronology": ({e["event_id"]: e for e in load("visuals/system_chronology.json")}, "event_id"),
        "measurement_agenda": ({m["measurement_id"]: m for m in load("content/measurement_agenda.json")}, "measurement_id"),
    }
    vis = {v["visual_id"]: v for v in load("visuals/visual_design_contracts.json")["visuals"]}
    for name in list(X.DATASETS) + ["codebook"]:
        rows = json.loads((out / f"{name}.json").read_text(encoding="utf-8"))
        with (out / f"{name}.csv").open(encoding="utf-8-sig", newline="") as fh:
            crows = list(csv.DictReader(fh))
        if crows != rows:
            problems.append(f"{name}: the CSV and the JSON differ")
        if name == "codebook":
            continue
        if not rows:
            problems.append(f"{name}: empty")
        for r in rows:
            rid = r["record_id"]
            if r["master_sha256"] != sha:
                problems.append(f"{name} {rid}: provenance names another Master")
            sids = [s for s in r["source_ids"].split("; ") if s]
            if [loc(s) for s in sids] != [u for u in r["locators"].split("; ") if u] or any(not loc(s) for s in sids):
                problems.append(f"{name} {rid}: a locator is not its source's public original")
            if name in truth:
                idx, key = truth[name]
                rec = idx.get(r[key])
                if rec is None:
                    problems.append(f"{name}: {r[key]} is not a governed record")
                    continue
                for f, val in r.items():
                    if f in X.PROV:
                        continue
                    if name == "sources":
                        want = (loc(r[key]) if f == "primary_url" else j(rec.get(f)) if (rec.get("metadata_state") == "DISPLAY_READY"
                                or f in ("source_id", "rights_state", "retrieval_date")) else "")
                    else:
                        want = j(rec.get(f))
                    if val != want:
                        problems.append(f"{name} {r[key]}.{f}: exported {val[:50]!r} != governed {want[:50]!r}")
            elif name == "visual_rows":
                v = vis.get(r["visual_id"]) or {}
                vals = [x for s in (v.get("contract") or {}).get("series") or [] if s["id"] == r["series_id"] for x in s.get("values") or []
                        if j(x.get("id")) == r["row_id"] and j(x.get("x")) == r["x"]]
                cells = [c for row in (v.get("table") or {}).get("rows") or [] for c in (row.get("cells") or ([row["group"]] if "group" in row else []))
                         if "number" in c and c["ref"] == f'{r["series_id"]}.{r["row_id"]}.{r["x"]}']
                if not any(j(x.get("y")) == r["value"] for x in vals) and not any(j(c["number"]) == r["value"] for c in cells):
                    problems.append(f"visual_rows {r['visual_id']} {r['row_id']} {r['x']}: {r['value']} is not a governed value")
        if name == "sources":
            named = {r["source_id"] for r in rows}
            if any(not loc(s) for s in named) or len(named) != sum(1 for s in lib if loc(s)):
                problems.append("sources: the firewall does not hold (a source without a public locator, or a public one missing)")
    dep = json.loads((ROOT / "site-src" / "deployment.json").read_text(encoding="utf-8"))
    if dep.get("public_downloads") is not False:
        problems.append("deployment.json: public_downloads must stay false until CauseWay's counsel confirms the CC BY 4.0 text")
    if (ROOT / "dist" / "downloads").exists():
        problems.append("dist/downloads exists while downloads are switched off")
    return problems


if __name__ == "__main__":
    raise SystemExit(main())
