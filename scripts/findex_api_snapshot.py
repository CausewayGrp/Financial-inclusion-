#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The dated snapshot of the open World Bank API behind gate CO-G04 (close-out U1).

  python3 scripts/findex_api_snapshot.py --check      # re-read every series in the latest snapshot; exit 1 on any drift
  python3 scripts/findex_api_snapshot.py --write      # also write audit/close_out/fixtures/findex_api_<today>.json

Reads only the open API (api.worldbank.org/v2, source 28, Yemen, date 2022): no key, no respondent-level data. The
gate compares the Master with the committed snapshot, never with the live API; this script is how a person (or the
monthly currentness workflow) learns that the World Bank has revised a value. A drift is a reviewed Master change,
never an automatic one: `--write` only records the new snapshot beside the old.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIX = ROOT / "audit" / "close_out" / "fixtures"


def fetch(url: str) -> dict:
    last = None
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=60) as fh:
                meta, recs = json.loads(fh.read().decode("utf-8"))
            rec = (recs or [{}])[0]
            return {"url": url, "label": (rec.get("indicator") or {}).get("value"), "date": rec.get("date"),
                    "value": rec.get("value"), "lastupdated": meta.get("lastupdated"), "sourceid": meta.get("sourceid")}
        except Exception as exc:   # network or API error: retried, then reported
            last = exc
            time.sleep(2 * (attempt + 1))
    return {"url": url, "error": repr(last)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    snaps = sorted(FIX.glob("findex_api_*.json"))
    if not snaps:
        print("FINDEX API SNAPSHOT: none committed")
        return 1
    old = json.loads(snaps[-1].read_text(encoding="utf-8"))
    new, drift, errs = {}, [], []
    for code, rec in old["series"].items():
        cur = fetch(rec["url"])
        new[code] = cur
        if "error" in cur:
            errs.append(code)
        elif cur.get("value") != rec.get("value") or cur.get("label") != rec.get("label"):
            drift.append((code, rec.get("value"), cur.get("value")))
    for code, a, b in drift:
        print(f"DRIFT {code}: snapshot {a} -> live {b}")
    for code in errs:
        print(f"UNREAD {code}: {new[code]['error']}")
    if args.write:
        out = FIX / f"findex_api_{date.today().isoformat()}.json"
        out.write_text(json.dumps({**{k: v for k, v in old.items() if k != "series"},
                                   "retrieved": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                                   "series": dict(sorted(new.items()))}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"WROTE {out.relative_to(ROOT)}")
    print(f"FINDEX API SNAPSHOT: {len(new)} series read against {snaps[-1].name}; {len(drift)} drifted, {len(errs)} unread")
    return 1 if (drift or errs) else 0


if __name__ == "__main__":
    sys.exit(main())
