# -*- coding: utf-8 -*-
"""Stage 5 — bilingual editorial roots (ENGLISH-VOICE, ARABIC-CALQUE) and the terminology sweeps PB-0413/PB-0414/PB-0415.

  python3 stage5_execute.py <in_master.xlsx> <spec.csv> <out_master.xlsx> <out_dir> <ledger.json>

Sweeps are executed per cell (the umbrella roots say so). Acceptance correction (D2 §PB-0413/0414): every sweep row is
re-adjudicated in context — «المنظومة» meaning the financial system stays; the product's self-reference is rendered by
context (هذا الموقع / قاعدة الأدلة / هنا / impersonal or passive voice), «المنصة» nowhere by default; «خلاصة» only where
the governed-claim sense is meant. Each row is APPLY (spec text), REVISE (Lead text below) or KEEP (with reason); a row whose
exact before-text is absent is reported as FAILED with its cause. No row is fuzzy-matched.
"""
import hashlib, json, os, re, sys
from collections import OrderedDict, Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from engine import Engine, RootFailure, LOC_SUBSTR, ROOT      # noqa: E402
from stage3_execute import leads, regenerate_full_copy         # noqa: E402

STAGE = "STAGE-5"
S5_LEADS = {"ENGLISH-VOICE", "ARABIC-CALQUE"}
HOLS = "هذا الموقع"
# ---- PB-0414: Lead re-adjudication (before-window -> revised after-window); keyed by the spec's exact before-text ----
R414 = OrderedDict([
    ("لماذا لا تعرض المنظومة خريطة كاملة الآن؟", "لماذا لا يعرض هذا الموقع خريطة كاملة الآن؟"),
    (" لذلك لا تعرضها المنظومة كسلسلة اتجاه قبل ", " لذلك لا تُعرض هنا كسلسلة اتجاه قبل "),
    ("تعامل المنظومة عامي 1997 و1998 ك", "يتعامل هذا الموقع مع عامي 1997 و1998 ك"),
    ("ة متصلة. وتحافظ المنظومة على النقاط الفصلي", "ة متصلة. ويحافظ هذا الموقع على النقاط الفصلي"),
    ("تحدد المنظومة لوحة من 32 مقياسً", "يحدد هذا الموقع لوحة من 32 مقياسً"),
    ("ي 2022. وتتعامل المنظومة معها كمراسي لموجا", "ي 2022. ويتعامل هذا الموقع معها كمراسي لموجا"),
    ("يخية الموثقة في المنظومة تُظهر أن حصة النم", "يخية الموثقة هنا تُظهر أن حصة النم"),
    ("عادة الإنتاج في المنظومة صياغة 91% كحصة من", "عادة الإنتاج هنا صياغة 91% كحصة من"),
    ("تلفة. لذلك تفصل المنظومة بينها قبل تفسير أ", "تلفة. لذلك يفصل هذا الموقع بينها قبل تفسير أ"),
    ("بلغ عنها. تحافظ المنظومة على هذه النقاط وا", "بلغ عنها. يحافظ هذا الموقع على هذه النقاط وا"),
    ("دية المعتمدة في المنظومة قراءةً لسياق المي", "دية المعتمدة هنا قراءةً لسياق المي"),
    ("ة؛ لذلك لا تصنع المنظومة إجماليًا تراكميًا", "ة؛ لذلك لا يصنع هذا الموقع إجماليًا تراكميًا"),
    ("وصول. لذلك تربط المنظومة التمويل بالمنشآت ", "وصول. لذلك يربط هذا الموقع التمويل بالمنشآت "),
    ("ما تزال المنظومة تفتقر إلى سلسلة م", "ما تزال قاعدة الأدلة تفتقر إلى سلسلة م"),
    ("لا تختزل المنظومة أهمية القرار وإمك", "لا يختزل هذا الموقع أهمية القرار وإمك"),
    ("لماذا القياس جزء من المنظومة؟", "لماذا القياس جزء من هذا الموقع؟"),
    ("بط القياس أجزاء المنظومة بعضها ببعض. فموجة", "بط القياس أجزاء هذا الموقع بعضها ببعض. فموجة"),
    ("تلفة. لذلك تفصل المنظومة تاريخ القياس أو ا", "تلفة. لذلك يفصل هذا الموقع تاريخ القياس أو ا"),
    ("عندما تحسب المنظومة فجوة أو حصة أو نس", "عندما يحسب هذا الموقع فجوة أو حصة أو نس"),
    ("ياس واحد، تتحقق المنظومة من التعريف والفتر", "ياس واحد، يُتحقَّق من التعريف والفتر"),
    ("ما تزال المنظومة تفتقر إلى قياس قا", "ما تزال قاعدة الأدلة تفتقر إلى قياس قا"),
    ("قاسة، ولا تفترض المنظومة أن المفاهيم متطاب", "قاسة، ولا يفترض هذا الموقع أن المفاهيم متطاب"),
    ("ف؛ لذلك لا تنسب المنظومة مستوىً سكانيًا في", "ف؛ لذلك لا ينسب هذا الموقع مستوىً سكانيًا في"),
    ("ة. لذلك لا تنسب المنظومة مستويات القدرات إ", "ة. لذلك لا ينسب هذا الموقع مستويات القدرات إ"),
    ("ل الدخول. وتحفظ المنظومة تفضيل اللغة في مت", "ل الدخول. ويحفظ هذا الموقع تفضيل اللغة في مت"),
    (" 2025. ولا تعرض المنظومة المسار 7←9←8 بوصف", " 2025. ولا يعرض هذا الموقع المسار 7←9←8 بوصف"),
    ("ملاء. لذلك تربط المنظومة حالة مقدم الخدمة ", "ملاء. لذلك يربط هذا الموقع حالة مقدم الخدمة "),
    ("ورة مكتملة داخل المنظومة.", "ورة مكتملة في قاعدة الأدلة."),
    ("لا تتوفر في المنظومة حاليًا قياسات وطن", "لا تتوفر في قاعدة الأدلة حاليًا قياسات وطن"),
    ("لا تحتوي المنظومة بعد على لوحة أولي", "لا تحتوي قاعدة الأدلة بعد على لوحة أولي"),
    ("لا تستطيع المنظومة حاليًا إثبات ما إ", "لا تستطيع قاعدة الأدلة حاليًا إثبات ما إ"),
    ("تفصل المنظومة بين القاعدة والتم", "يفصل هذا الموقع بين القاعدة والتم"),
    ("تستخدم المنظومة سلسلة انتقال واحد", "يستخدم هذا الموقع سلسلة انتقال واحد"),
    (" مناسب، لا تنسب المنظومة مستوى القدرة أو ت", " مناسب، لا ينسب هذا الموقع مستوى القدرة أو ت"),
    ("دة. لذلك تستخدم المنظومة تسميات للحالة حتى", "دة. لذلك يستخدم هذا الموقع تسميات للحالة حتى"),
    ("فسها. لذلك تفصل المنظومة هذه الأدلة وتُظهر", "فسها. لذلك يفصل هذا الموقع هذه الأدلة ويُظهر"),
    (" نصه. لذلك تفصل المنظومة بين صلاحية الدليل", " نصه. لذلك يفصل هذا الموقع بين صلاحية الدليل"),
    ("مقيدة، قد تحتفظ المنظومة بالبيانات الوصفية", "مقيدة، قد يحتفظ هذا الموقع بالبيانات الوصفية"),
    ("المصدر داخل هذه المنظومة حقوقًا إضافية.", "المصدر داخل هذا الموقع حقوقًا إضافية."),
    ("ل اليمني، وتربط المنظومة بالناشر الأصلي بد", "ل اليمني، ويربط هذا الموقع بالناشر الأصلي بد"),
    ("اء؛ ولا توجد في المنظومة سلسلة إدارية موثق", "اء؛ ولا توجد في قاعدة الأدلة سلسلة إدارية موثق"),
    ("يمن المعتمدة في المنظومة لموجة المؤشر العا", "يمن المعتمدة في قاعدة الأدلة لموجة المؤشر العا"),
    ("سبة +11%. تُبقي المنظومة الإجماليات المنشو", "سبة +11%. يُبقي هذا الموقع الإجماليات المنشو"),
    ("سبة +11%. تُبقي المنظومة القيمتين ظاهرتين ", "سبة +11%. يُبقي هذا الموقع القيمتين ظاهرتين "),
    ("يمكن للمنظومة تحديث خط الأساس ا", "يمكن تحديث خط الأساس ا"),
    ("يمكن للمنظومة قياس التسرب من ال", "يمكن قياس التسرب من ال"),
    ("ونية موثقة، لكن المنظومة لا تملك دليلًا عل", "ونية موثقة، لكن قاعدة الأدلة لا تتضمن دليلًا عل"),
    ("تسمح للمنظومة بتحديد إلى أي مدى", "تسمح بتحديد إلى أي مدى"),
    ("دى اكتمال معرفة المنظومة بمقدمي الخدمة.", "دى اكتمال معرفة قاعدة الأدلة بمقدمي الخدمة."),
])
# ---- PB-0413: rows kept (ordinary 'assertion/fact-check' sense, not the governed-claim noun) ----
K413 = {"أظهر لي الدليل وراء الادعاء، واشرح الاختلافات،":
        "User-voiced question: «الادعاء» is the ordinary fact-checking sense (a claim met elsewhere), not the product's governed claim; «الخلاصة» would change the question."}
# ---- PB-0415: revised rows ----
R415 = OrderedDict([
    ("The product can trace transmission across the system without turning s",
     "This resource can trace transmission across the system without turning s"),   # second 'system' = the financial system (KEEP)
])
BUILD = OrderedDict([
    ("PB-0413.B01", ("تحليل متعدد المصادر يبقى مربوطًا بالادعاءات والأدلة.", "تحليل متعدد المصادر يبقى مربوطًا بالخلاصات والأدلة.")),
    ("PB-0413.B02", ("وجودها في الدليل لا يرقّيها إلى نتيجة أو ادعاء.", "وجودها في الدليل لا يرقّيها إلى نتيجة أو خلاصة.")),
    ("PB-0413.B03", ("ابحث في الادعاءات والأدلة والقراءات...", "ابحث في الخلاصات والأدلة والقراءات…")),
    ("PB-0414.B01", ("افتح سجل المصدر داخل المنظومة أو انتقل إلى الرابط الأصلي عندما تسمح حالة النشر بذلك.", "افتح سجل المصدر هنا، أو انتقل إلى الرابط الأصلي حين تسمح حالة النشر بذلك.")),
    ("PB-0414.B02a", ("لا تنشئ المنظومة سجل إصدارات", "لا ينشئ هذا الموقع سجل إصدارات")),
    ("PB-0414.B02b", ("The product does not manufacture a release or correction history", "This resource does not manufacture a release or correction history")),
    ("PB-0415.B-EN", ("Open the source record in this system or follow the original locator when publication state allows it.", "Open the source record here, or follow the original locator when publication state allows it.")),
])


def main():
    master, spec, out_master, out_dir, ledger = sys.argv[1:6]
    os.makedirs(out_dir, exist_ok=True)
    eng = Engine(master, spec)
    wb, ed = eng.wb, eng.ed
    LEAD = leads()
    done = json.load(open(os.path.join(HERE, "ROOT_DISPOSITIONS.json"), encoding="utf-8"))
    from projection.master_reader import Workbook
    import tempfile

    def ed_grid(sheet):
        tmp = tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False, dir=out_dir)
        tmp.close()
        ed.save(tmp.name)
        try:
            return Workbook(tmp.name).grid(sheet)
        finally:
            os.remove(tmp.name)
    eng.ed_grid = ed_grid

    def substr(root):
        rows = eng.spec[root]
        keep = [r for r in rows if not (r["sheet"] == "02_SITE_MAP" and r["field"].startswith("full_copy"))]
        skipped = [r["patch_id"] for r in rows if r not in keep]
        eng.spec[root] = keep
        try:
            out = eng.apply_substr_rows(root) if keep else []
        finally:
            eng.spec[root] = rows
        if skipped:
            out.append("full_copy rows superseded by EXF-002 derivation: " + ", ".join(skipped))
        return out

    # 1. editorial SUBSTR roots
    for root, rows in eng.spec.items():
        if root in done and done[root]["disposition"] != "PENDING":
            continue
        if LEAD.get(root) in S5_LEADS:
            eng.run_root(root, substr, STAGE)
    # 2. sweeps, per cell
    rowlog = OrderedDict()
    counts = Counter()
    for root, revise, keep in (("PB-0413", {}, K413), ("PB-0414", R414, {}), ("PB-0415", R415, {})):
        for r in eng.spec[root]:
            pid = r["patch_id"]
            if not pid.startswith(root + ".S"):
                continue
            if r["sheet"] == "02_SITE_MAP" and r["field"].startswith("full_copy"):
                rowlog[pid] = ("SUPERSEDED", "full_copy row: 02 full_copy is derived from the rendered sections (EXF-002)"); counts["SUPERSEDED"] += 1
                continue
            before = r["current_value"]
            if before in keep:
                rowlog[pid] = ("KEEP", keep[before]); counts["KEEP"] += 1
                continue
            if root == "PB-0414" and before not in revise:
                rowlog[pid] = ("HELD_LANGUAGE_REVIEW", "No context-safe rendering adjudicated for this window."); counts["HELD_LANGUAGE_REVIEW"] += 1
                continue
            after = revise.get(before, r["proposed_value"])
            m = LOC_SUBSTR.match(r["row_locator_if_needed"])
            row, n = int(m.group(1)), int(m.group(2))
            col = eng.col(r["sheet"], r["field"])
            cur = ed.get_value(r["sheet"], row, col) or ""
            if pid == "PB-0415.S119" and cur.count(before) == 1 and n == 2:
                # Re-based on the AIR-001-restored cell (14 r28 = YSC-020): the spec counted the entry Master's corrupted rows.
                n = 1
            if cur.count(before) != n:
                rowlog[pid] = ("FAILED", f"before-text occurs {cur.count(before)}× in {r['sheet']}!r{row}.{r['field']} (expected {n}); the cell differs from the spec's post-patch basis"); counts["FAILED"] += 1
                continue
            ed.replace_in_cell(r["sheet"], row, col, before, after, count=n)
            tag = "REVISED" if before in revise else "APPLIED"
            rowlog[pid] = (tag, f"{r['sheet']}!r{row}.{r['field']}: {after}"); counts[tag] += 1
    # T01: 07 sheet title (claim noun)
    cur = ed.get_value("07_PUBLIC_CLAIMS", 1, 1)
    if cur == "Public analytical claims / الادعاءات التحليلية العامة":
        ed.set_cell("07_PUBLIC_CLAIMS", 1, 1, "Public analytical claims / الخلاصات التحليلية العامة", expect=cur)
        rowlog["PB-0413.T01"] = ("APPLIED", "07!A1 sheet title"); counts["APPLIED"] += 1
    else:
        rowlog["PB-0413.T01"] = ("FAILED", f"07!A1 is {cur!r}"); counts["FAILED"] += 1
    for root in ("PB-0413", "PB-0414", "PB-0415"):
        mine = {k: v for k, v in rowlog.items() if k.startswith(root)}
        c = Counter(v[0] for v in mine.values())
        eng.results[root] = OrderedDict([("disposition", "APPLIED"), ("stage", STAGE),
                                         ("detail", f"per-cell execution after Lead re-adjudication: {dict(c)}; row outcomes in STAGE5_SWEEP_ROW_LEDGER.csv")])
    eng.run_root("EXF-002", lambda r: regenerate_full_copy(eng, STAGE), STAGE)
    data = ed.save(out_master)
    # build strings (code, same commit) — written to out_dir as a patched copy of scripts/build.py
    b = open(os.path.join(ROOT, "scripts", "build.py"), encoding="utf-8").read()
    for pid, (old, new) in BUILD.items():
        n = b.count(old)
        if n < 1:
            rowlog[pid] = ("FAILED", "string not found in build.py"); counts["FAILED"] += 1
            continue
        b = b.replace(old, new)
        rowlog[pid] = ("REVISED" if pid in ("PB-0414.B02a",) else "APPLIED", f"scripts/build.py ×{n}: {new}"); counts["APPLIED"] += 1
    open(os.path.join(out_dir, "build.py"), "w", encoding="utf-8").write(b)
    import csv
    with open(os.path.join(out_dir, "STAGE5_SWEEP_ROW_LEDGER.csv"), "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.writer(fh, quoting=csv.QUOTE_ALL)
        w.writerow(["patch_id", "outcome", "detail"])
        for k, (o, d) in rowlog.items():
            w.writerow([k, o, d])
    rep = OrderedDict([("stage", STAGE), ("input_master_sha256", hashlib.sha256(open(master, "rb").read()).hexdigest()),
                       ("output_master_sha256", hashlib.sha256(data).hexdigest()), ("cells_and_ops", len(ed.log)),
                       ("sweep_row_outcomes", dict(counts)), ("results", eng.results)])
    json.dump(rep, open(ledger, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(Counter(v["disposition"] for v in eng.results.values()), dict(counts))
    for k, v in eng.results.items():
        if v["disposition"] != "APPLIED":
            print(k, v["disposition"], str(v["detail"])[:220])
    for k, (o, d) in rowlog.items():
        if o in ("FAILED", "HELD_LANGUAGE_REVIEW"):
            print(k, o, d[:200])
    print(rep["output_master_sha256"])


if __name__ == "__main__":
    main()
