"""B16: build OPEN_ITEMS_DISPOSITION.md and the dated blocks appended to the records, from the read-only extraction
(open_items.json, at c055abc) plus what changed since (B15, RC-15, RC-16) and the items B16 adds (the B15 escalations,
the Addendum 2 rejected list, its judged items). Writes into the repository only when run with --write."""
import json, sys, re
from collections import OrderedDict, Counter
from pathlib import Path

HERE = Path(__file__).parent
ROOT = Path(__file__).resolve().parents[3]
D = json.loads((HERE / "open_items.json").read_text(encoding="utf-8"))
DATE = "2026-10-03"

items = OrderedDict()
for i in D["open_items"]:
    items[i["id"]] = {"id": i["id"], "record": i["file"].split(";")[0].strip(), "where": i["file"], "item": i["description"],
                      "disp": i["suggested_disposition"], "why": i.get("evidence") or "", "section": i.get("section") or ""}

# --- updates since the extraction (c055abc) -----------------------------------------------------------------------
UPD = json.loads((HERE / "updates.json").read_text(encoding="utf-8")) if (HERE / "updates.json").exists() else {}
for k, v in UPD.items():
    items[k].update(v)

# --- items B16 adds ---------------------------------------------------------------------------------------------
ADDED = json.loads((HERE / "added.json").read_text(encoding="utf-8"))
for a in ADDED:
    items[a["id"]] = a

counts = Counter(i["disp"] for i in items.values())
undecided = [k for k, i in items.items() if i["disp"] not in ("DONE", "RELEASE", "POST-LAUNCH", "REJECTED")]
assert not undecided, undecided


def cell(s):
    return str(s).replace("|", "\\|").replace("\n", " ").strip()


ORDER = ["RELEASE", "DONE", "POST-LAUNCH", "REJECTED"]
TITLE = {"RELEASE": "RELEASE — what remains at release, and who does it",
         "DONE": "DONE — closed by a commit in this pull request",
         "POST-LAUNCH": "POST-LAUNCH — not needed for a link-and-citation launch, with the reason",
         "REJECTED": "REJECTED — decided, with the closed decision it rests on"}
out = [open(HERE / "head.md", encoding="utf-8").read().rstrip("\n"), "",
       "## Counts", "", "| Disposition | Items |", "|---|---|"]
for k in ORDER:
    out.append(f"| {k} | {counts.get(k, 0)} |")
out += [f"| **Total dispositioned** | **{sum(counts.values())}** |", "| Undecided | 0 |", "",
        f"By record: " + "; ".join(f"`{r}` {n}" for r, n in Counter(i['record'] for i in items.values()).most_common()) + ".", ""]
for k in ORDER:
    rows = [i for i in items.values() if i["disp"] == k]
    out += [f"## {TITLE[k]}", "", "| ID | Record | Item | Disposition and reason |", "|---|---|---|---|"]
    for i in rows:
        out.append(f"| {i['id']} | `{cell(i['record'])}` | {cell(i['item'])} | {cell(i['why'])} |")
    out.append("")
out.append(open(HERE / "tail.md", encoding="utf-8").read().rstrip("\n"))
text = "\n".join(out) + "\n"
(HERE / "OPEN_ITEMS_DISPOSITION.md").write_text(text, encoding="utf-8")
print(dict(counts), "total", sum(counts.values()))

# --- the dated blocks appended to each record --------------------------------------------------------------------
def line(i):
    return f"  - {i['id']} — **{i['disp']}** — {cell(i['item'])[:160]}{'…' if len(cell(i['item'])) > 160 else ''} → {cell(i['why'])}"

esc = [i for i in items.values() if i["record"] == "design/ESCALATIONS.md"]
reg = [i for i in items.values() if i["record"].startswith("FINAL_OPEN_ITEMS_REGISTER.md") or i["record"].startswith("audit/release_candidate/")]
debt = [i for i in items.values() if i["record"].startswith("design/DESIGN_DEBT.md")]
blocks = {"esc": esc, "reg": reg, "debt": debt}
(HERE / "blocks.json").write_text(json.dumps({k: [line(i) for i in v] for k, v in blocks.items()}, ensure_ascii=False, indent=1), encoding="utf-8")
print({k: len(v) for k, v in blocks.items()})
