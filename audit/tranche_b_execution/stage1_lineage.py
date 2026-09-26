# -*- coding: utf-8 -*-
"""Stage 1 — object-level source lineage and verification integrity (Master-first).

Roots: PB-0001 (06 lineage_state), PB-0006/PB-0008 (04 governed interface copy), PB-0007/PB-0007A (06 verification
text from the lineage state), PB-0010…PB-0069 (per-object bindings) and the execution check of the
BOUND_CANDIDATE bindings, plus the re-adjudication of the 48 pre-populated dependency cells that PB-0001 requires
("BOUND_EXACT unless re-checked"). Generator/build roots PB-0002…PB-0005 are code changes in the same stage.

  python3 stage1_lineage.py <in_master.xlsx> <out_master.xlsx> <ledger.json>

Every write checks the exact current cell value. The adjudication (state, dependency tokens, basis) is read from
STAGE1_LINEAGE_ADJUDICATION.json next to this script; rows it does not list keep their dependency cell and are
classified by rule (only source IDs -> BOUND_EXACT; anything else -> abort, nothing is inferred).
"""
import hashlib, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "scripts"))
from projection.master_reader import Workbook               # noqa: E402
from projection.master_writer import MasterEditor           # noqa: E402

S06, S04 = "06_EVIDENCE_OBJECTS", "04_NAV_UX"
BOILER_EN = ("Show the definition, population or group covered, calculation base where relevant, period, geography, method, limitations, "
             "source and reuse conditions. If a value or source link is unavailable, say so explicitly rather than inferring or inventing it.")
BOILER_AR = ("يُعرض التعريف، والمجتمع أو النطاق الذي ينطبق عليه الدليل، وقاعدة الاحتساب عند الحاجة، والفترة، والجغرافيا، والطريقة، والحدود، "
             "والمصدر، وشروط إعادة الاستخدام. وإذا كانت قيمة أو وصلة مصدر غير متاحة، يُذكر ذلك صراحةً بدل استنتاجها أو اختلاقها.")
VERIFY_EXCEPTIONS = {"CLM-019"}          # PB-0007: all rows except CLM-019 (record-specific verification text is kept)

UI_BLOCK_TITLE = "Governed interface copy"
UI_HEADER = ["ui_id", "label_en", "label_ar", "use_rule"]
UI_ROWS = [
    ("UI-VERIFY-BOUND",
     "This record is drawn from the source(s) listed on this page. Open a source record to reach the original document, and check that the definition, period, population and geography match what is stated here.",
     "يستند هذا السجل إلى المصدر أو المصادر المدرجة في هذه الصفحة. افتح سجل المصدر للوصول إلى الوثيقة الأصلية، وتحقق من تطابق التعريف والفترة والمجتمع والنطاق الجغرافي مع ما يرد هنا.",
     "PB-0008. 06 verification text when lineage_state = BOUND_EXACT."),
    ("UI-VERIFY-PARTIAL",
     "Some figures in this record are drawn from the source(s) listed on this page; other inputs have not yet been linked to a specific original source. Check each figure against a listed source before reuse, and treat any figure you cannot match as unverified.",
     "تستند بعض أرقام هذا السجل إلى المصدر أو المصادر المدرجة في هذه الصفحة، ولم تُربط مدخلات أخرى بعدُ بمصدر أصلي محدد. فطابِق كل رقم مع أحد المصادر المدرجة قبل إعادة استخدامه، وعامِل الرقم الذي لا تجد له مقابلًا على أنه غير متحقق منه.",
     "Stage 1 Lead addition (BOUND_PARTIAL). 06 verification text and evidence-page source statement when some inputs are bound and others are open."),
    ("UI-VERIFY-COMPOSITE",
     "This view assembles other evidence records. Check each linked record against its own source.",
     "يجمع هذا العرض سجلات أدلة أخرى، فتحقق من كل سجل مرتبط مقابل مصدره الخاص.",
     "PB-0008. 06 verification text and evidence-page statement when lineage_state = COMPOSITE_OF_OBJECTS and member records are listed."),
    ("UI-VERIFY-COMPOSITE-UNLISTED",
     "This view summarises other evidence records, which are not yet linked individually here. Before reusing a figure, open the evidence record that reports it and check that record against its own source.",
     "يلخص هذا العرض سجلات أدلة أخرى لم تُربط بعدُ هنا كلٌّ على حدة. وقبل إعادة استخدام أي رقم، افتح سجل الدليل الذي يورده وتحقق منه مقابل مصدره الخاص.",
     "Stage 1 Lead addition. 06 verification text and evidence-page statement when lineage_state = COMPOSITE_OF_OBJECTS and no member record is listed in the Master."),
    ("UI-EVID-UNBOUND",
     "This record has not yet been linked to a specific original source. Treat its figures as unverified for reuse until the link is added.",
     "لم يُربط هذا السجل بعدُ بمصدر أصلي محدد، فلا تُعامل أرقامه على أنها صالحة لإعادة الاستخدام إلى أن يُضاف هذا الربط.",
     "PB-0006. 06 verification text and evidence-page statement when lineage_state = SOURCE_NOT_YET_BOUND."),
    ("UI-EVID-FRAMING",
     "This record sets out a rule for measuring or reading the evidence. It does not report a figure from a source, so there is no original source to check.",
     "يحدد هذا السجل قاعدة لقياس الأدلة أو قراءتها، ولا يورد رقمًا مأخوذًا من مصدر، ولذلك لا يوجد مصدر أصلي يُتحقق منه.",
     "Stage 1 Lead addition. 06 verification text and evidence-page statement when lineage_state = FRAMING_NO_FACT."),
    ("UI-EVID-MEMBERS-HEADING",
     "Evidence records assembled in this view",
     "سجلات الأدلة التي يجمعها هذا العرض",
     "Stage 1. Heading of the member-record list on a COMPOSITE_OF_OBJECTS evidence page."),
]
TEMPLATE_FOR = {"BOUND_EXACT": "UI-VERIFY-BOUND", "BOUND_PARTIAL": "UI-VERIFY-PARTIAL", "COMPOSITE_OF_OBJECTS": "UI-VERIFY-COMPOSITE",
                "COMPOSITE_UNLISTED": "UI-VERIFY-COMPOSITE-UNLISTED", "SOURCE_NOT_YET_BOUND": "UI-EVID-UNBOUND", "FRAMING_NO_FACT": "UI-EVID-FRAMING"}


def main():
    src, out, ledger = sys.argv[1:4]
    adj = json.load(open(os.path.join(HERE, "STAGE1_LINEAGE_ADJUDICATION.json"), encoding="utf-8"))
    wb = Workbook(src)
    g = wb.grid(S06)
    header = g[3]
    col = {h: j + 1 for j, h in enumerate(header) if h}
    if "lineage_state" in col:
        sys.exit("06 already carries lineage_state — refusing to re-apply Stage 1")
    lib = {r[0] for r in wb.grid("15_SOURCE_LIBRARY")[4:] if r and r[0]}
    ids06 = [r[0] for r in g[4:] if r and r[0]]
    ed = MasterEditor(src)
    new_col = len(header) + 1
    ed.set_cell(S06, 4, new_col, "lineage_state", expect=None)
    ui = {u[0]: u for u in UI_ROWS}
    rows_log, problems = [], []
    for i, r in enumerate(g[4:], start=5):
        oid = r[0]
        if not oid:
            continue
        cur_dep = r[col["source_dependencies"] - 1]
        if oid in adj:
            a = adj[oid]
            deps = a["source_dependencies"]
            state = a["lineage_state"]
            new_dep = "; ".join(deps) if deps else None
            if (cur_dep or None) != (new_dep or None):
                ed.set_cell(S06, i, col["source_dependencies"], new_dep, expect=cur_dep)
            if a.get("source_links_keep") is not None:
                links = json.loads(r[col["source_links"] - 1] or "[]")
                kept = [l for l in links if (l.get("source_id") if isinstance(l, dict) else l) in a["source_links_keep"]]
                ed.set_cell(S06, i, col["source_links"], json.dumps(kept, ensure_ascii=False), expect=r[col["source_links"] - 1])
            basis = a["basis"]
        else:
            toks = [t.strip() for t in (cur_dep or "").split(";") if t.strip()]
            if toks and all(t in lib for t in toks):
                deps, state, basis = toks, "BOUND_EXACT", "Pre-populated dependency cell holds only source IDs present in 15_SOURCE_LIBRARY; kept unchanged."
            else:
                problems.append(f"{oid}: not adjudicated and dependency cell is not source-ID-only: {cur_dep!r}")
                continue
        srcs = [t for t in deps if t in lib]
        bad = [t for t in deps if t.startswith("SRC-") and t not in lib]
        if bad:
            problems.append(f"{oid}: source IDs absent from 15_SOURCE_LIBRARY: {bad}")
        members = [t for t in deps if t in ids06]
        if state in ("BOUND_EXACT", "BOUND_PARTIAL") and not srcs:
            problems.append(f"{oid}: {state} without a bound source")
        if state not in ("BOUND_EXACT", "BOUND_PARTIAL") and srcs:
            problems.append(f"{oid}: {state} carries source IDs {srcs}")
        ed.set_cell(S06, i, new_col, state, expect=None)
        tkey = "COMPOSITE_UNLISTED" if state == "COMPOSITE_OF_OBJECTS" and not members else state
        if oid not in VERIFY_EXCEPTIONS:
            u = ui[TEMPLATE_FOR[tkey]]
            ed.set_cell(S06, i, col["verification_en"], u[1], expect=BOILER_EN)
            ed.set_cell(S06, i, col["verification_ar"], u[2], expect=BOILER_AR)
        rows_log.append({"excel_row": i, "object_id": oid, "lineage_state": state, "verification_template": None if oid in VERIFY_EXCEPTIONS else TEMPLATE_FOR[tkey],
                         "bound_source_ids": srcs, "member_object_ids": members, "source_dependencies_before": cur_dep,
                         "source_dependencies_after": "; ".join(deps) if deps else None, "basis": basis})
    if problems:
        sys.exit("Stage 1 adjudication problems:\n  " + "\n  ".join(problems))
    # 04: governed interface copy block after the last used row, separated by one blank row
    g4 = wb.grid(S04)
    last = max(i for i, r in enumerate(g4, 1) if any(c not in (None, "") for c in r))
    t = last + 2
    ed.set_cell(S04, t, 1, UI_BLOCK_TITLE, expect=None)
    for j, h in enumerate(UI_HEADER, 1):
        ed.set_cell(S04, t + 1, j, h, expect=None)
    for k, row in enumerate(UI_ROWS):
        for j, v in enumerate(row, 1):
            ed.set_cell(S04, t + 2 + k, j, v, expect=None)
    data = ed.save(out)
    after = Workbook(out)
    others = all(wb.grid(n) == after.grid(n) for n in wb.sheet_names if n not in (S06, S04))
    import collections
    rep = {"stage": "STAGE-1", "input_master_sha256": hashlib.sha256(open(src, "rb").read()).hexdigest(),
           "output_master_sha256": hashlib.sha256(data).hexdigest(), "cells_written": len(ed.log),
           "lineage_state_counts": dict(collections.Counter(r["lineage_state"] for r in rows_log)),
           "verification_template_counts": dict(collections.Counter(r["verification_template"] for r in rows_log)),
           "interface_copy_block": {"sheet": S04, "title_row": t, "header_row": t + 1, "rows": [u[0] for u in UI_ROWS]},
           "other_sheets_unchanged": others, "records": rows_log}
    json.dump(rep, open(ledger, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps({k: v for k, v in rep.items() if k != "records"}, ensure_ascii=False, indent=1))
    if not others:
        sys.exit("unexpected change outside 04/06")


if __name__ == "__main__":
    main()
