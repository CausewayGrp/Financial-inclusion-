# -*- coding: utf-8 -*-
"""Write audit/close_out/SOURCE_UTILISATION_<date>.csv: every source record, how the public site uses it, from the
generated projections and the built /data/ page (Stage A addendum, item 3). Derived, never typed.

  python3 audit/close_out/source_utilisation.py 2026-10-11

Columns:
  source_id, use_state, data_group, card_state, document_label, document_date, host,
  evidence_records, public_claims, readings, visuals, measurement_priorities, chronology_events, card_text, note

use_state (one per source, first that applies):
  RETIRED            no public locator; its note starts RETIRED (merged into another record)
  WITHHELD           no public locator; its note starts NON_PUBLIC, or none
  USED_BY_RECORD     a public record, claim, Reading, visual or priority resolves to it
  CHRONOLOGY_SOURCE  cited by a dated chronology event only
  CONTEXT_CARD       listed in the directory with no dependent (a curated, regulatory or reference card)
data_group: the /data/ group the built page lists it in (curated, regulatory, regulatory-link, supporting, reference) or
none. card_text: Y when the card prints a governed "why it matters" or boundary.
"""
import csv, json, os, re, sys
from urllib.parse import urlparse

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
C = os.path.join(ROOT, "site-src", "content")


def load(rel):
    return json.load(open(os.path.join(C, rel), encoding="utf-8"))


def groups_on_data_page():
    """source_id -> data group, read from the built English /data/ page."""
    html = open(os.path.join(ROOT, "dist", "en", "data", "index.html"), encoding="utf-8").read()
    marks = [("curated", html.find('id="curated"')), ("regulatory", html.find('id="regulatory"')),
             ("supporting", html.find("source-supporting-details")), ("reference", html.find("source-reference-details"))]
    marks = sorted((p, g) for g, p in marks if p >= 0) + [(len(html), None)]
    out = {}
    for (start, g), (end, _) in zip(marks, marks[1:]):
        seg = html[start:end]
        for sid in re.findall(r'<article class="src[^"]*" id="source-([^"]+)"', seg):
            out.setdefault(sid, g)
        if g == "regulatory":
            for sid in re.findall(r'data-source-also[^>]*><a href="#source-([^"]+)"', seg):
                out.setdefault(sid + "#link", "regulatory-link")
    return out


def main():
    date = sys.argv[1] if len(sys.argv) > 1 else None
    if not date or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
        raise SystemExit("usage: source_utilisation.py YYYY-MM-DD")
    lib = load("sources/source_library.json")
    ref = {r["source_id"]: r for r in load("sources/source_reference_map.json")}
    chrono = {}
    for e in load("visuals/system_chronology.json"):
        for sid in [x.strip() for x in str(e.get("source_ids") or "").split("|") if x.strip()]:
            chrono.setdefault(sid, []).append(e.get("event_id"))
    groups = groups_on_data_page()
    rows = []
    for s in lib:
        sid = s["source_id"]
        r = ref.get(sid, {})
        n = {k: len(r.get(f) or []) for k, f in (("evidence_records", "linked_evidence_object_ids"), ("public_claims", "linked_claim_ids"),
                                                    ("readings", "linked_reading_ids"), ("visuals", "linked_visual_ids"),
                                                    ("measurement_priorities", "linked_measurement_ids"))}
        url = str(s.get("primary_url") or "")
        note = str(s.get("non_public_locator_note") or "")
        if not url.startswith(("http://", "https://")):
            state = "RETIRED" if note.startswith("RETIRED") else "WITHHELD"
        elif any(n.values()):
            state = "USED_BY_RECORD"
        elif chrono.get(sid):
            state = "CHRONOLOGY_SOURCE"
        else:
            state = "CONTEXT_CARD"
        group = groups.get(sid, "none")
        if group == "curated" and groups.get(sid + "#link"):
            group = "curated+regulatory-link"
        rows.append([sid, state, group, s.get("public_card_state") or "", s.get("document_label") or "", s.get("document_date") or "",
                     urlparse(url).netloc if url else "", n["evidence_records"], n["public_claims"], n["readings"], n["visuals"],
                     n["measurement_priorities"], len(chrono.get(sid, [])),
                     "Y" if (s.get("why_it_matters") or s.get("does_not_establish")) else "N",
                     note.split(":")[0][:60] if note and not url else ""])
    rows.sort(key=lambda x: x[0])
    out = os.path.join(ROOT, "audit", "close_out", f"SOURCE_UTILISATION_{date}.csv")
    with open(out, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["source_id", "use_state", "data_group", "card_state", "document_label", "document_date", "host", "evidence_records",
                    "public_claims", "readings", "visuals", "measurement_priorities", "chronology_events", "card_text", "note"])
        w.writerows(rows)
    tally = {}
    for x in rows:
        tally[x[1]] = tally.get(x[1], 0) + 1
    print(f"SOURCE UTILISATION WRITTEN: {len(rows)} sources -> {os.path.relpath(out, ROOT)}; " +
          ", ".join(f"{k} {v}" for k, v in sorted(tally.items())))


if __name__ == "__main__":
    main()
