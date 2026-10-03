#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Data exports, prepared and switched off (Part B B14 a).

  python3 scripts/exports.py                 # writes build/exports/ (never dist/)
  python3 scripts/exports.py --out DIR       # writes DIR instead

Writes CSV (UTF-8 with a byte-order mark, so spreadsheet software reads the Arabic) and JSON for six datasets — the
Evidence Records, the public claims, the sources, the rows the visual contracts draw, the system chronology and the
Measurement Agenda — with a bilingual codebook (field, meaning, unit, allowed values) and provenance on every row:
the record ID, the source IDs and their public locators, and the Production Master's SHA-256.

Every value is copied from the governed projections under `site-src/content/`; nothing is computed, rounded or
re-worded. The publication firewall holds: a source without a public locator is never named, and a non-display-ready
source carries no title. `scripts/tests/test_exports.py` proves every exported value against the projections.

Publishing is one switch, `public_downloads` in `site-src/deployment.json`, which stays false until the owner's licence
decision (FINAL_OPEN_ITEMS_REGISTER.md; docs/RELEASE_RUNBOOK.md). While it is false, nothing here reaches `dist/`, and
the validator fails if a download is found there. The codebook's wording is a draft: it needs the bilingual review that
governed copy receives before the switch is turned on.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
C = ROOT / "site-src" / "content"
MASTER = ROOT / "authority" / "Yemen_Financial_Inclusion_Evidence_Master.xlsx"
OUT = ROOT / "build" / "exports"
PROV = ["record_id", "source_ids", "locators", "master_sha256"]
JOIN = "; "


def load(rel: str):
    return json.loads((C / rel).read_text(encoding="utf-8"))


def master_sha() -> str:
    return hashlib.sha256(MASTER.read_bytes()).hexdigest()


class Sources:
    """The public sources: only a source with a public original locator may be named (the publication firewall)."""

    def __init__(self) -> None:
        self.lib = {s["source_id"]: s for s in load("sources/source_library.json")}

    def locator(self, sid: str) -> str:
        u = str((self.lib.get(sid) or {}).get("primary_url") or "").strip()
        return u if u.lower().startswith(("http://", "https://")) else ""

    def public(self, sids) -> list[str]:
        return [s for s in dict.fromkeys(str(x).strip() for x in sids or []) if s and self.locator(s)]

    def prov(self, rid: str, sids, sha: str) -> OrderedDict:
        pub = self.public(sids)
        return OrderedDict([("record_id", rid), ("source_ids", JOIN.join(pub)), ("locators", JOIN.join(self.locator(s) for s in pub)),
                            ("master_sha256", sha)])


def text(v) -> str:
    if v is None:
        return ""
    if isinstance(v, (list, tuple)):
        return JOIN.join(text(x) for x in v)
    return str(v)


def evidence_records(src: Sources, sha: str) -> list[OrderedDict]:
    F = ["object_id", "object_class", "title_en", "title_ar", "summary_en", "summary_ar", "definition_en", "definition_ar",
         "period_en", "period_ar", "universe_en", "universe_ar", "method_en", "method_ar", "limitations_en", "limitations_ar",
         "does_not_establish_en", "does_not_establish_ar", "currentness_en", "currentness_ar", "public_routes"]
    out = []
    for o in load("evidence/evidence_objects.json"):
        if not o.get("public_routes"):
            continue
        row = OrderedDict((f, text(o.get(f))) for f in F)
        row.update(src.prov(o["object_id"], o.get("source_dependencies"), sha))
        out.append(row)
    return out


def public_claims(src: Sources, sha: str) -> list[OrderedDict]:
    objs = {o["object_id"]: o for o in load("evidence/evidence_objects.json")}
    F = ["claim_id", "theme", "claim_type", "headline_en", "headline_ar", "copy_en", "copy_ar", "evidence_inputs",
         "does_not_prove_en", "does_not_prove_ar", "public_routes"]
    out = []
    for c in load("evidence/public_claims.json"):
        row = OrderedDict((f, text(c.get(f))) for f in F)
        # a claim's sources are those of its Evidence Record (the record that carries the claim's ID)
        row.update(src.prov(c["claim_id"], (objs.get(c["claim_id"]) or {}).get("source_dependencies") or [], sha))
        out.append(row)
    return out


def sources(src: Sources, sha: str) -> list[OrderedDict]:
    out = []
    for sid, s in src.lib.items():
        if not src.locator(sid):
            continue                                  # never named: no public locator
        ready = s.get("metadata_state") == "DISPLAY_READY"
        row = OrderedDict([("source_id", sid)]
                          + [(f, text(s.get(f)) if ready else "") for f in ("display_title", "display_title_ar", "publisher", "publisher_ar",
                                                                              "document_label", "document_label_ar", "document_date")]
                          + [("primary_url", src.locator(sid)), ("rights_state", text(s.get("rights_state"))), ("retrieval_date", text(s.get("retrieval_date")))])
        row.update(src.prov(sid, [sid], sha))
        out.append(row)
    return out


def visual_rows(src: Sources, sha: str) -> list[OrderedDict]:
    """The governed values the visual contracts draw (series values) and the numbers of the text-first tables."""
    out = []
    for v in load("visuals/visual_design_contracts.json")["visuals"]:
        for s in (v.get("contract") or {}).get("series") or []:
            for x in s.get("values") or []:
                if x.get("y") is None:
                    continue
                row = OrderedDict([("visual_id", v["visual_id"]), ("series_id", s["id"]), ("row_id", text(x.get("id"))),
                                   ("x", text(x.get("x"))), ("value", text(x.get("y"))), ("unit", text(x.get("unit"))),
                                   ("state", text(x.get("grammar_state") or s.get("state"))), ("lane", text(x.get("lane")))])
                row.update(src.prov(text(x.get("id")), [x.get("source")] if x.get("source") else [], sha))
                out.append(row)
        for r in (v.get("table") or {}).get("rows") or []:
            cells = r.get("cells") or ([r["group"]] if "group" in r else [])
            for c in cells:
                if "number" not in c:
                    continue
                oid, rid, fld = c["ref"].split(".", 2)
                row = OrderedDict([("visual_id", v["visual_id"]), ("series_id", oid), ("row_id", rid), ("x", fld),
                                   ("value", text(c["number"])), ("unit", text((c.get("unit") or {}).get("en"))), ("state", ""), ("lane", "")])
                row.update(src.prov(rid, [], sha))
                out.append(row)
    return out


def chronology(src: Sources, sha: str) -> list[OrderedDict]:
    F = ["event_id", "period_en", "period_ar", "event_class", "fact_en", "fact_ar", "system_implication_en", "system_implication_ar",
         "does_not_establish_en", "does_not_establish_ar", "linked_routes"]
    out = []
    for e in load("visuals/system_chronology.json"):
        row = OrderedDict((f, text(e.get(f))) for f in F)
        sids = e.get("source_ids") or []
        sids = sids if isinstance(sids, list) else [x.strip() for x in str(sids).replace(";", ",").split(",")]
        row.update(src.prov(e["event_id"], sids, sha))
        out.append(row)
    return out


def measurement_agenda(src: Sources, sha: str) -> list[OrderedDict]:
    F = ["measurement_id", "priority", "title_en", "title_ar", "domain", "domain_ar", "current_evidence_en", "current_evidence_ar",
         "missing_evidence_en", "missing_evidence_ar", "guardrail_en", "guardrail_ar", "decisions_unlocked_en", "decisions_unlocked_ar",
         "blocked_evidence_en", "blocked_evidence_ar", "affected_routes"]
    out = []
    for m in load("content/measurement_agenda.json"):
        row = OrderedDict((f, text(m.get(f))) for f in F)
        row.update(src.prov(m["measurement_id"], [], sha))
        out.append(row)
    return out


DATASETS = OrderedDict([("evidence_records", evidence_records), ("public_claims", public_claims), ("sources", sources),
                        ("visual_rows", visual_rows), ("chronology", chronology), ("measurement_agenda", measurement_agenda)])

# The codebook: what each field means, in both languages (draft wording; reviewed before the switch is turned on).
MEANING = {
    "record_id": ("The ID of the governed record this row comes from", "معرّف السجل المعتمد الذي يأتي منه هذا الصف"),
    "source_ids": ("The IDs of the public sources the record depends on", "معرّفات المصادر العامة التي يستند إليها السجل"),
    "locators": ("The public original locator of each source, in the same order", "رابط الأصل العام لكل مصدر، بالترتيب نفسه"),
    "master_sha256": ("The SHA-256 of the Production Master the row was generated from", "بصمة SHA-256 للملف المرجعي الذي وُلّد منه الصف"),
    "_en": ("English text, as published", "النص الإنجليزي كما يُنشر"),
    "_ar": ("Arabic text, as published", "النص العربي كما يُنشر"),
    "value": ("The governed value, as the source reports it or as the record states it was calculated", "القيمة المعتمدة كما يوردها المصدر أو كما يذكر السجل طريقة حسابها"),
    "unit": ("The unit of the value", "وحدة القيمة"),
    "state": ("The evidence state of the value (reported, measured, administrative, derived …)", "حالة الدليل للقيمة (مُبلَّغ عنها، مقيسة، إدارية، مشتقة …)"),
    "x": ("The period, group or field the value belongs to", "الفترة أو الفئة أو الحقل الذي تنتمي إليه القيمة"),
    "public_routes": ("The pages of the site that use the record", "صفحات الموقع التي تستخدم السجل"),
}
ENUMS = {"object_class", "claim_type", "theme", "event_class", "priority", "state", "rights_state", "domain", "unit", "document_label"}


def codebook(data: dict) -> list[OrderedDict]:
    rows = []
    for name, recs in data.items():
        fields = list(recs[0].keys()) if recs else []
        for f in fields:
            m = MEANING.get(f) or MEANING.get(f[-3:] if f.endswith(("_en", "_ar")) else "", ("", ""))
            vals = sorted({r[f] for r in recs if r[f]}) if f in ENUMS else []
            rows.append(OrderedDict([("dataset", name), ("field", f), ("meaning_en", m[0]), ("meaning_ar", m[1]),
                                     ("unit", "see the unit field" if f == "value" else ""),
                                     ("allowed_values", JOIN.join(vals) if 0 < len(vals) <= 40 else "")]))
    return rows


def write(out: Path, name: str, rows: list[OrderedDict]) -> None:
    (out / f"{name}.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    with (out / f"{name}.csv").open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()) if rows else [], lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def build(out: Path) -> dict:
    out.mkdir(parents=True, exist_ok=True)
    sha, src = master_sha(), Sources()
    data = OrderedDict((n, fn(src, sha)) for n, fn in DATASETS.items())
    for n, rows in data.items():
        write(out, n, rows)
    write(out, "codebook", codebook(data))
    manifest = OrderedDict([("schema", "YFIE_EXPORTS/1.0"), ("master_sha256", sha), ("published", False),
                            ("switch", "site-src/deployment.json public_downloads (false until the owner's licence decision)"),
                            ("datasets", OrderedDict((n, len(r)) for n, r in data.items()))])
    (out / "MANIFEST.json").write_text(json.dumps(manifest, indent=1) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(OUT))
    args = ap.parse_args()
    m = build(Path(args.out))
    print("EXPORTS WRITTEN (not published): " + ", ".join(f"{n} {k}" for n, k in m["datasets"].items()) + f" → {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
