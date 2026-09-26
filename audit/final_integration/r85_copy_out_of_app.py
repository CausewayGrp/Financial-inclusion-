# -*- coding: utf-8 -*-
"""R8.5 copy-out-of-code, part 2: the bilingual interface copy held in site-src/app.js moves to the Master's governed
interface copy (04), IDs UI-JS-*. The build writes the page language's UI-JS-* labels into each page as
<script type="application/json" id="yfie-ui">; app.js reads them with T(id) / TF(id, values).

  python3 r85_copy_out_of_app.py <interface_copy.json> <rows_out.json> [--apply]

Every replacement is an exact, counted text substitution; the run stops if a snippet is not found exactly once.
Lineage only; not part of the build.
"""
import json, re, sys, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
APP = os.path.join(ROOT, "site-src", "app.js")

SIMPLE = [  # (id, old snippet, new snippet, en, ar)
    ("UI-JS-COPIED", "(isAr?'تم النسخ':'Copied')", "T('UI-JS-COPIED')", "Copied", "تم النسخ"),
    ("UI-JS-CURRENT-RECORD", "(isAr?'الرابط الحالي: ':'Current record: ')", "T('UI-JS-CURRENT-RECORD')", "Current record: ", "الرابط الحالي: "),
    ("UI-JS-COPY-CITATION", "isAr?'انسخ الاستشهاد':'Copy citation'", "T('UI-JS-COPY-CITATION')", "Copy citation", "انسخ الاستشهاد"),
    ("UI-JS-COPY-SOURCE-REFERENCE", "isAr?'انسخ مرجع المصدر':'Copy source reference'", "T('UI-JS-COPY-SOURCE-REFERENCE')", "Copy source reference", "انسخ مرجع المصدر"),
    ("UI-JS-SEARCH-NO-RESULT", "(isAr?'لا توجد نتيجة تطابق هذا البحث. ولا يعني ذلك غياب الأدلة عن الموضوع؛ جرّب كلمات أخرى أو ابدأ من الأسئلة.':'No result matches this search. This does not mean there is no evidence on the topic; try other words or start from the questions.')",
     "T('UI-JS-SEARCH-NO-RESULT')", "No result matches this search. This does not mean there is no evidence on the topic; try other words or start from the questions.",
     "لا توجد نتيجة تطابق هذا البحث. ولا يعني ذلك غياب الأدلة عن الموضوع؛ جرّب كلمات أخرى أو ابدأ من الأسئلة."),
    ("UI-JS-SEARCHING", "isAr?'جارٍ البحث…':'Searching…'", "T('UI-JS-SEARCHING')", "Searching…", "جارٍ البحث…"),
    ("UI-JS-SEARCH-ZERO", "isAr?'0 نتيجة معروضة':'0 results shown'", "T('UI-JS-SEARCH-ZERO')", "0 results shown", "0 نتيجة معروضة"),
    ("UI-JS-SEARCH-RESULTS", "isAr?`عدد النتائج المعروضة: ${scored.length}`:(scored.length===1?'1 result shown':`${scored.length} results shown`)",
     "TF(scored.length===1?'UI-JS-SEARCH-RESULT-ONE':'UI-JS-SEARCH-RESULTS',{n:scored.length})", "{n} results shown", "عدد النتائج المعروضة: {n}"),
    ("UI-JS-SEARCH-UNAVAILABLE-COPY", "(isAr?'تعذر تحميل البحث الآن. يمكنك متابعة التصفح من الأقسام الرئيسية.':'Search could not be loaded. You can continue from the main sections.')",
     "T('UI-JS-SEARCH-UNAVAILABLE-COPY')", "Search could not be loaded. You can continue from the main sections.", "تعذر تحميل البحث الآن. يمكنك متابعة التصفح من الأقسام الرئيسية."),
    ("UI-JS-SEARCH-UNAVAILABLE", "isAr?'تعذر تحميل البحث':'Search unavailable'", "T('UI-JS-SEARCH-UNAVAILABLE')", "Search unavailable", "تعذر تحميل البحث"),
    ("UI-JS-SOURCES-SHOWN", "isAr?`عدد المصادر والمراجع المعروضة: ${shown}`:(shown===1?'1 source or reference shown':`${shown} sources or references shown`)",
     "TF(shown===1?'UI-JS-SOURCES-SHOWN-ONE':'UI-JS-SOURCES-SHOWN',{n:shown})", "{n} sources or references shown", "عدد المصادر والمراجع المعروضة: {n}"),
    ("UI-JS-SOURCE-LINK-UNKNOWN", "isAr?'لم يُعثر في دليل المصادر على مرجع المصدر الوارد في هذا الرابط. هذه مشكلة في الرابط، وليست معلومة عن الأدلة؛ تُعرض المصادر كلها أدناه.':'The source reference in this link was not found in the source directory. This is a problem with the link, not information about the evidence; all sources are shown below.'",
     "T('UI-JS-SOURCE-LINK-UNKNOWN')", "The source reference in this link was not found in the source directory. This is a problem with the link, not information about the evidence; all sources are shown below.",
     "لم يُعثر في دليل المصادر على مرجع المصدر الوارد في هذا الرابط. هذه مشكلة في الرابط، وليست معلومة عن الأدلة؛ تُعرض المصادر كلها أدناه."),
]
EXTRA = [  # rows used by TF alternatives (English singulars; Arabic uses one form)
    ("UI-JS-SEARCH-RESULT-ONE", "1 result shown", "عدد النتائج المعروضة: 1"),
    ("UI-JS-SOURCES-SHOWN-ONE", "1 source or reference shown", "عدد المصادر والمراجع المعروضة: 1"),
]
OBJECTS = [  # (prefix, table name, start marker)
    ("UI-JS-TYPE", "TYPE_LABEL_UI", "  const labels=isAr?{page:"),
    ("UI-JS-COMPARE", "COMPARE_LABEL_UI", "  const labels=isAr?{\n    definition:"),
    ("UI-JS-COMPARE-LINK", "COMPARE_ERROR_UI", "  const errorText=isAr?{"),
]
PAIR = re.compile(r"(\w+):'((?:\\.|[^'\\])*)'")
HELPERS = ("const isAr=document.documentElement.lang==='ar';\n"
           "// R8.5: interface copy is governed in the Master (04, IDs UI-JS-*); the build writes this page's labels as JSON.\n"
           "const UI=(()=>{try{return JSON.parse(document.getElementById('yfie-ui')?.textContent||'{}');}catch(e){return {};}})();\n"
           "const T=k=>(k in UI?UI[k]:k);\n"
           "const TF=(k,o)=>T(k).replace(/\\{(\\w+)\\}/g,(m,n)=>(n in o?String(o[n]):m));\n"
           "const labelsFrom=table=>Object.fromEntries(Object.entries(table).map(([k,v])=>[k,T(v)]));\n")


def slug(key):
    return re.sub(r"([a-z])([A-Z])", r"\1-\2", key).replace("_", "-").upper()


def main():
    ui_path, rows_out = sys.argv[1:3]
    apply = "--apply" in sys.argv
    existing = {u["ui_id"] for u in json.load(open(ui_path, encoding="utf-8"))}
    src = open(APP, encoding="utf-8").read()
    rows = []
    for uid, old, new, en, ar in SIMPLE:
        if src.count(old) != 1:
            raise SystemExit(f"{uid}: snippet found {src.count(old)} times")
        src = src.replace(old, new)
        rows.append([uid, en, ar, "site-src/app.js"])
    for uid, en, ar in EXTRA:
        rows.append([uid, en, ar, "site-src/app.js (English singular; Arabic uses one form)"])
    for prefix, table, start in OBJECTS:
        i = src.index(start)
        j = src.index("};", src.index("}:{", i)) + 2
        block = src[i:j]
        ar_part, en_part = block.split("}:{", 1)
        a, e = dict(PAIR.findall(ar_part)), dict(PAIR.findall(en_part))
        keys = [k for k, _ in PAIR.findall(en_part)]
        if set(a) != set(e):
            raise SystemExit(f"{table}: keys differ {set(a) ^ set(e)}")
        ids = {}
        for k in keys:
            uid = f"{prefix}-{slug(k)}"
            ids[k] = uid
            rows.append([uid, e[k].replace("\\'", "'"), a[k].replace("\\'", "'"), f"site-src/app.js {table}['{k}']"])
        name = block.split("=", 1)[0].strip().replace("const ", "")
        src = src[:i] + f"  const {name}=labelsFrom({table});" + src[j:]
        src = src.replace(HELPERS.split("\n")[0] + "\n", HELPERS.split("\n")[0] + "\n", 1)
        src = src.replace("const isAr=document.documentElement.lang==='ar';\n",
                          "const isAr=document.documentElement.lang==='ar';\n" + f"const {table}={json.dumps(ids)};\n", 1)
    src = src.replace("const isAr=document.documentElement.lang==='ar';\n", HELPERS, 1)
    if src.count("isAr?'") or re.search(r"isAr\?`", src):
        left = re.findall(r"isAr\?['`][^'`]{0,60}", src)
        raise SystemExit(f"bilingual literals left in app.js: {left}")
    clash = [r[0] for r in rows if r[0] in existing]
    if clash:
        raise SystemExit(f"IDs already in 04: {clash}")
    json.dump(rows, open(rows_out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"app.js rows {len(rows)}")
    if apply:
        open(APP, "w", encoding="utf-8").write(src)


if __name__ == "__main__":
    main()
