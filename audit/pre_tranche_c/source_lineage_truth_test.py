# -*- coding: utf-8 -*-
"""Source-lineage truth test — current state (Pre-Tranche-C P5).

  python3 audit/pre_tranche_c/source_lineage_truth_test.py

Recomputes, from the current projections, the lineage and closure counts and truth assertions that Tranche B recorded in
audit/tranche_b_execution/SOURCE_LINEAGE_TRUTH_TEST.json (that file is historical lineage and is not rewritten), and adds
the P5 assertions:
  - every event locator a SIGNATURE/CORE data contract credits resolves to a source record (no locator without a record);
  - REF-PAY-001 resolves to its source record and VIS-PAYMENT-RAILS is closed to source IDs;
  - no data contract carries a release blocker unless it is listed below as open.
Writes audit/pre_tranche_c/SOURCE_LINEAGE_TRUTH_TEST.json. Exit 1 if an assertion fails.
"""
import json
import os
import re
import sys
from collections import Counter, OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
C = os.path.join(ROOT, "site-src", "content")
OUT = os.path.join(HERE, "SOURCE_LINEAGE_TRUTH_TEST.json")
OPEN_RELEASE_BLOCKERS = {}          # visual_id -> reason; empty once P5.2 and P5.3 closed


def L(p):
    return json.load(open(os.path.join(C, p), encoding="utf-8"))


def main():
    failures = []

    def check(name, ok, detail=None):
        if not ok:
            failures.append(name)
        return OrderedDict([("check", name), ("result", "PASS" if ok else "FAIL")] + ([("detail", detail)] if detail is not None else []))

    clo = L("sources/public_object_source_closure.json")
    eo = L("evidence/evidence_objects.json")
    lib = {r["source_id"]: r for r in L("sources/source_library.json")}
    vdc = L("visuals/visual_design_contracts.json")
    reforms = L("data/reforms_regulation.json")

    by_type = OrderedDict()
    for c in clo:
        by_type.setdefault(c["object_type"], Counter())[c["closure_state"]] += 1
    lin = Counter(o.get("lineage_state") for o in eo)
    asserts = []
    asserts.append(check("no BOUND_CANDIDATE state remains", not any("CANDIDATE" in str(o.get("lineage_state")) for o in eo)))
    asserts.append(check("every resolved source is declared on the record and exists in 15",
                         all(s in c["dependency_ids"] and s in lib for c in clo if c["object_type"] == "evidence_object" for s in c["resolved_source_ids"])))
    asserts.append(check("CLOSED_TO_SOURCE_ID only with no open input",
                         all(not c["unresolved_dependency_ids"] for c in clo if c["closure_state"] == "CLOSED_TO_SOURCE_ID")))
    # A DS-/numeric token that is itself an Evidence Record ID (e.g. DS-FINDEX-PUBLIC-HISTORY) is a listed member record, resolved
    # through resolved_via_object_ids; every other dataset token must stay an open input and is never expanded into sources.
    record_ids = {o["object_id"] for o in eo}
    ds_tokens = sorted({t for c in clo if c["object_type"] == "evidence_object" for t in c["dependency_ids"] if re.match(r"^(DS-|\d+(_|$))", t)})
    member_refs = sorted({f"{c['object_id']} -> {t}" for c in clo if c["object_type"] == "evidence_object" for t in c["dependency_ids"]
                          if re.match(r"^(DS-|\d+(_|$))", t) and t in record_ids})
    asserts.append(check("dataset tokens appear only as open inputs (never expanded); record IDs among them are listed members",
                         all((t in c["unresolved_dependency_ids"]) or (t in record_ids and t in c["resolved_via_object_ids"])
                             for c in clo if c["object_type"] == "evidence_object" for t in c["dependency_ids"] if re.match(r"^(DS-|\d+(_|$))", t)),
                         {"dataset_tokens_on_records": ds_tokens, "member_record_references": member_refs}))

    # P5 assertions
    urls = {}
    for s in lib.values():
        for u in [s.get("primary_url")] + [x.strip() for x in re.split(r'[|,\[\]"]', str(s.get("additional_urls") or "")) if x.strip()]:
            if u and str(u).startswith(("http://", "https://")):
                urls.setdefault(str(u).strip(), s["source_id"])
    rows = reforms.get("rows") or []
    hdr_i = next(i for i, r in enumerate(rows) if r and r[0] == "event_id")
    hdr = rows[hdr_i]
    events = OrderedDict()
    for r in rows[hdr_i + 1:]:
        if not r or not r[0] or r[0] == "event_id":
            break
        rec = dict(zip(hdr, r))
        events[rec["event_id"]] = rec
    ref1 = events.get("REF-PAY-001") or {}
    ref1_src = urls.get(str(ref1.get("source_url") or ""))
    asserts.append(check("REF-PAY-001 locator resolves to a source record with that public locator", bool(ref1_src),
                         {"locator": ref1.get("source_url"), "source_id": ref1_src,
                          "display_title": (lib.get(ref1_src) or {}).get("display_title"), "rights_state": (lib.get(ref1_src) or {}).get("rights_state")}))
    rails = [c for c in clo if c["object_id"] == "VIS-PAYMENT-RAILS"]
    asserts.append(check("VIS-PAYMENT-RAILS is closed to source IDs (record and visual)",
                         rails and all(c["closure_state"] == "CLOSED_TO_SOURCE_ID" and not c["unresolved_dependency_ids"] for c in rails),
                         {c["object_type"]: c["closure_state"] for c in rails}))
    credited_urls = []
    for v in vdc["visuals"]:
        con = v.get("contract") or {}
        for o in con.get("objects") or []:
            for rec in o.get("records") or []:
                if str(rec.get("source") or "").startswith(("http://", "https://")):
                    credited_urls.append((v["visual_id"], rec["id"], rec["source"]))
    orphan = [f"{vid} {rid}: {u}" for vid, rid, u in credited_urls if u not in urls]
    asserts.append(check("every locator a data contract credits resolves to a source record", not orphan, {"orphans": orphan}))
    blockers = OrderedDict((v["visual_id"], v["contract"]["blockers"]) for v in vdc["visuals"] if v.get("contract") and v["contract"].get("blockers"))
    asserts.append(check("no release blocker outside the declared open list", set(blockers) <= set(OPEN_RELEASE_BLOCKERS),
                         {"blockers": blockers, "declared_open": OPEN_RELEASE_BLOCKERS}))
    open_records = OrderedDict((c["object_id"], OrderedDict([("state", c["closure_state"]), ("open_inputs", c["unresolved_dependency_ids"]),
                                                             ("members", c["resolved_via_object_ids"])]))
                               for c in clo if c["object_type"] == "evidence_object" and c["closure_state"] != "CLOSED_TO_SOURCE_ID")
    rep = OrderedDict([("rule", clo[0]["rule"]), ("as_of", "Pre-Tranche-C P5"),
                       ("evidence_record_lineage_state_counts", dict(lin)),
                       ("closure_state_counts_by_object_type", {k: dict(v) for k, v in by_type.items()}),
                       ("records_not_closed_to_source", open_records), ("assertions", asserts),
                       ("historical_baseline", "audit/tranche_b_execution/SOURCE_LINEAGE_TRUTH_TEST.json (Tranche B; not rewritten)")])
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(rep, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    for a in asserts:
        print(f"{a['result']:4}  {a['check']}")
    print(f"SOURCE LINEAGE TRUTH TEST {'PASS' if not failures else 'FAIL'}: {len(asserts) - len(failures)}/{len(asserts)}")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
