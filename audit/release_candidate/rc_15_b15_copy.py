# -*- coding: utf-8 -*-
"""Release-candidate transaction RC-15: the governed copy and data allowed by the B15 product challenge's red team
(audit/release_candidate/PRODUCT_CHALLENGE.md; Part B B15 d). English and Arabic change together.

  python3 rc_15_b15_copy.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

B-1   CLM-019, CLM-009, VIS-PROVIDER-TIME and the VIS-PROVIDER-TIME meta description said the 2026 decisions "are matched"
      with the roster entity by entity. The Master's own provider rows say otherwise: every decision subject is
      STATUS_EVENT_CONFIRMED__BASE_ROSTER_MEMBERSHIP_NOT_YET_RECONCILED, the roster's names are not in the Master, and
      /providers/ lists the reconciliation as an open question. The text now says the matching with the roster would
      have to be done and has not been; each decision stays attached to the entities it names (the two limitation fields
      say so, after the adversarial review). No count is added.
A-8   Home names three gaps (an access-point map, a current population rate, a causal explanation) with no route to the
B-5   priorities that would supply them. MA-003 and MA-005 are bound to "/" beside MA-001, so Home can list all three
      by their governed titles, with a note that a link is not a claim the priority would close or explain the gap.
      Explore showed five of the eight P0 priorities and omitted MA-002, MA-009 and MA-010 without saying why; they are
      bound to "/explore", so Explore shows every P0 item, and a governed line says so.
A-7   Search alias 026 gains "cash assistance" / «المساعدات النقدية». Surfacing the Reading "The payment arrived. What
      happened next?" (CWR-010) on /payments/ is not done here: an answer page carries at most two Readings (the
      generator's rule) and /payments/ already carries CWR-005 and CWR-009; which one gives way is an editorial choice,
      listed in docs/ROADMAP_V1_1.md. /payments/ reaches CWR-010 through MA-009, whose card it carries.
B-6   CLM-026 (32 demand-side measures specified; estimates not yet published) is bound to /measurement/, among the
      records that revealed the gaps, beside MA-001.
B-3   CLM-007 (allowed part): "shows materially higher remittance inflows" becomes "gives a higher value for remittance
      inflows". The red team blocked relabelling the IMF history as model-based.
B-10  CLM-015: Governor's Decision No. 23 of 2024 on domestic money-transfer activity carries the same date as the
      e-wallet circular; the record now says they are separate instruments and that it establishes no link between them,
      and lists the decision among its sources in the context role (no source is named publicly without its locator).
B-12  /payments/ s2: one sentence on what the POS transaction series does support (the reported totals are higher in
      June 2026 than in March 2025, but did not rise steadily and fell in several months), with the scope-continuity
      boundary the record carries. No change is computed, so the April-to-May 2026 contradiction is untouched. The chart
      note UI-VIS-NOTE-POS-H1-WITHHELD (RC-11b) said each release reports "within the same reporting scope"; it now says
      that continuity across the July 2025 change of format has not been verified, as the record does.

Reviews: one bilingual reviewer (Arabic first) and one adversarial reviewer (regulatory statements); both NOT
ACCEPTABLE at the first run, every finding folded into this one rerun (PRODUCT_CHALLENGE.md §4).
A-4   Search alias 028: "internet; connectivity" / «الإنترنت; الانترنت; الاتصال», so a search for the internet reaches
      the records that name connectivity.
C-1   CLM-002 (the account-ownership gap) is computed from the World Bank's male and female series, but its only
      locator was the total. Its source links now carry both series' locators, which the source library already holds.
C-2   Owner decision OWN-04 launches with a short citation. Two governed strings: the long form's label and its copy
      action.
C-3   Compare's description and first section promised geography and unit rows that Compare does not show; they now name
      the rows it shows (definition, population or base, period, method, source, currentness) and send the reader to
      each record for its geography and unit.
U1    The citizen's game-changer (B15 e): "Share this record" on every Evidence Record — one governed label.
"""
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rc_lib import Session, Table, TxError, insert_ui_rows, ui_block_end  # noqa: E402

UI_ROWS = [
    ("UI-HOME-GAPS-NOTE",
     "Each priority below describes evidence that is still missing for one of these gaps. Listing it here does not claim that collecting that evidence would close the gap or explain it.",
     "تصف كل أولوية أدناه أدلةً ما زالت مفقودة تتصل بإحدى هذه الفجوات. ولا يعني إدراجها هنا أن جمع تلك الأدلة سيسدّ الفجوة أو يفسّرها.",
     "RC-15 (Part B B15 d, A-8). Home: the line under the measurement priorities bound to the gaps section."),
    ("UI-EXPLORE-MA-BASIS",
     "These are the priorities the Measurement Agenda marks P0. The full agenda, including its P1 items, is on the Measurement Agenda page.",
     "هذه هي البنود المصنفة P0 في أولويات القياس. وتعرض صفحة أولويات القياس القائمة الكاملة، بما فيها البنود المصنفة P1.",
     "RC-15 (Part B B15 d, B-5). Explore: the line under 'What the evidence cannot yet answer'; the gate RC-B15 keeps the set equal to the P0 items."),
    ("UI-EVID-SERIES-USED", "Series this record uses", "السلاسل التي يستخدمها هذا السجل",
     "RC-15 (Part B B15 d, C-1). Evidence Record source card: the record's own series locators, where they differ from the source's main locator."),
    ("UI-CITE-LONG-FORM", "Long form, with the period, population and limits", "الصيغة المطوّلة، مع الفترة والمجتمع والحدود",
     "RC-15 (Part B B15 d, C-2; OWN-04). Evidence Record: the disclosure that holds the long citation under the short one."),
    ("UI-JS-COPY-LONG-CITATION", "Copy long form", "انسخ الصيغة المطوّلة",
     "RC-15 (Part B B15 d, C-2). Evidence Record: copies the long citation."),
    ("UI-JS-SHARE-RECORD", "Share this record", "شارك هذا السجل",
     "RC-15 (Part B B15 e, U1). Evidence Record: shares the record's title, period, population, what not to conclude and its link — Web Share where the device offers it, otherwise the same text is copied."),
]

B1 = [  # (sheet, key, field, old substring, new substring)
    ("06_EVIDENCE_OBJECTS", "CLM-019", "summary_en",
     "but these decisions are matched with it entity by entity and are not subtracted from it to produce a count of providers operating now.",
     "but these decisions are not subtracted from it to produce a count of providers operating now: each would first have to be matched with the roster entity by entity, and that matching has not been done."),
    ("06_EVIDENCE_OBJECTS", "CLM-019", "summary_ar",
     "لكن هذه القرارات تُطابَق معها جهةً جهة، ولا تُطرح منها لاستخراج عدد لمقدمي الخدمات العاملين حاليًا.",
     "لكن هذه القرارات لا تُطرح منها لاستخراج عدد لمقدمي الخدمات العاملين حاليًا: إذ يلزم أولًا مطابقة كل قرار مع القائمة جهةً جهة، ولم تُجرَ هذه المطابقة بعد."),
    ("06_EVIDENCE_OBJECTS", "CLM-019", "limitations_en",
     "so each decision is matched to named entities one by one, without assuming whether the roster already reflects it.",
     "so each entity a decision names would have to be matched with the roster one by one, without assuming whether the roster already reflects the decision, and that matching has not been done."),
    ("06_EVIDENCE_OBJECTS", "CLM-019", "limitations_ar",
     "لذلك يُطابَق كل قرار مع الجهات المسماة جهةً جهة، من دون افتراض أن القائمة تعكسه أو لا تعكسه.",
     "لذلك يلزم مطابقة كل جهة يسميها القرار مع القائمة جهةً جهة، من دون افتراض أن القائمة تعكس القرار أو لا تعكسه، ولم تُجرَ هذه المطابقة بعد."),
    ("06_EVIDENCE_OBJECTS", "CLM-009", "summary_en",
     "are matched with the roster entity by entity, because a decision may or may not already be reflected in it.",
     "would have to be matched with the roster entity by entity, since a decision may or may not already be reflected in it; that matching has not been done."),
    ("06_EVIDENCE_OBJECTS", "CLM-009", "summary_ar",
     "ولأن القائمة لا تذكر تاريخ صدورها، تُطابَق قرارات البنك المركزي في عدن الصادرة خلال 2026 (بين يناير وسبتمبر 2026) بتعليق تراخيص جهات مسماة أو سحبها أو بإغلاق مقارها مع القائمة جهةً جهة، إذ قد يكون أثر القرار منعكسًا فيها وقد لا يكون.",
     "ولأن القائمة لا تذكر تاريخ صدورها، يلزم مطابقتها جهةً جهة مع قرارات البنك المركزي في عدن الصادرة خلال 2026 (بين يناير وسبتمبر 2026) بتعليق تراخيص جهات مسماة أو سحبها أو بإغلاق مقارها، إذ قد يكون أثر القرار منعكسًا فيها وقد لا يكون؛ ولم تُجرَ هذه المطابقة بعد."),
    ("06_EVIDENCE_OBJECTS", "VIS-PROVIDER-TIME", "summary_en",
     "they are kept separate from the roster and matched to it entity by entity, because the roster's issue date is not stated.",
     "they are kept separate from the roster, and, because the roster's issue date is not stated, each would have to be matched to it entity by entity; that matching has not been done."),
    ("06_EVIDENCE_OBJECTS", "VIS-PROVIDER-TIME", "summary_ar",
     "وتبقى هذه القرارات منفصلة عن القائمة وتُطابَق معها جهةً جهة، لأن القائمة لا تذكر تاريخ صدورها.",
     "وتبقى هذه القرارات منفصلة عن القائمة، ولأن القائمة لا تذكر تاريخ صدورها، يلزم مطابقة كل قرار معها جهةً جهة؛ ولم تُجرَ هذه المطابقة بعد."),
    ("06_EVIDENCE_OBJECTS", "VIS-PROVIDER-TIME", "limitations_en",
     "The 2026 decisions are matched to named entities one by one, without assuming whether the roster already reflects them, because the roster does not state its issue date;",
     "Each decision is attached to the entities it names. Because the roster does not state its issue date, those entities would have to be matched with the roster one by one, without assuming either way whether it already reflects the decisions; that matching has not been done, and"),
    ("06_EVIDENCE_OBJECTS", "VIS-PROVIDER-TIME", "limitations_ar",
     "وتُطابَق قرارات 2026 مع الجهات المسماة جهةً جهة، من دون افتراض أن القائمة تعكسها أو لا تعكسها، لأن القائمة لا تذكر تاريخ صدورها؛",
     "ويُربط كل قرار بالجهات التي يسميها. ولأن القائمة لا تذكر تاريخ صدورها، يلزم مطابقة هذه الجهات مع القائمة جهةً جهة، من دون افتراض أن القائمة تعكس القرارات أو لا تعكسها؛ ولم تُجرَ هذه المطابقة بعد."),
    ("02_SITE_MAP", "/evidence/VIS-PROVIDER-TIME/", "meta_description_en",
     "is kept apart from dated 2026 Governor's decisions, matched entity by entity.",
     "is kept apart from dated 2026 Governor's decisions, which have not yet been matched to it entity by entity."),
    ("02_SITE_MAP", "/evidence/VIS-PROVIDER-TIME/", "meta_description_ar",
     "منفصلة عن قرارات المحافظ المؤرخة في 2026، وتُطابَق معها جهةً جهة.",
     "منفصلة عن قرارات المحافظ المؤرخة في 2026، ولم تُطابَق معها جهةً جهة بعد."),
]

B3 = [
    ("06_EVIDENCE_OBJECTS", "CLM-007", "summary_en",
     "The history in the IMF 2025 Article IV staff report shows materially higher remittance inflows in 2024 than in 2018 (both values from the same document);",
     "The history in the IMF 2025 Article IV staff report gives a higher value for remittance inflows in 2024 than in 2018 (both values from the same document);"),
    ("06_EVIDENCE_OBJECTS", "CLM-007", "summary_ar",
     "تُظهر القيم التاريخية الواردة في تقرير خبراء صندوق النقد الدولي لمشاورات المادة الرابعة لعام 2025 أن التحويلات الواردة في ميزان المدفوعات كانت في 2024 أعلى بصورة جوهرية منها في 2018",
     "تورد السلسلة التاريخية في تقرير خبراء صندوق النقد الدولي لمشاورات المادة الرابعة لعام 2025 قيمةً للتحويلات الواردة في ميزان المدفوعات في 2024 أعلى منها في 2018"),
]

B3.append(("06_EVIDENCE_OBJECTS", "CLM-007", "summary_ar", "وهي نوع دليل مختلف.", "وهي تقدير وتوقعات، لا قيم مُبلَّغ عنها."))

B10 = [
    ("06_EVIDENCE_OBJECTS", "CLM-015", "summary_en",
     "Status under any other authority is not established here.",
     "Status under any other authority is not established here. Governor's Decision No. 23 of 2024 on domestic money-transfer activity carries the same date; the circular and the decision are separate instruments, and this record establishes no link between them."),
    ("06_EVIDENCE_OBJECTS", "CLM-015", "summary_ar",
     "ولا يثبت هذا الدليل وضعها لدى أي سلطة أخرى.",
     "ولا يثبت هذا الدليل وضعها لدى أي سلطة أخرى. ويحمل قرار المحافظ رقم (23) لسنة 2024 بشأن مزاولة نشاط التحويلات المالية الداخلية التاريخ نفسه؛ والتعميم والقرار أداتان منفصلتان، ولا يثبت هذا السجل أي صلة بينهما."),
]

B12 = [
    ("en", "none equals a person.",
     "none equals a person. The transaction series supports only a narrower reading: the totals CBY-Aden reports are higher in June 2026 than in March 2025, but they did not rise steadily and fell in several months; whether the reporting scope stayed the same, including across the change of release format in July 2025, has not been verified."),
    ("ar", "ولا يساوي أي منها شخصًا.",
     "ولا يساوي أي منها شخصًا. ولا تدعم سلسلة المعاملات إلا قراءة أضيق: فالإجماليات التي يُبلغ عنها البنك المركزي في عدن أعلى في يونيو 2026 منها في مارس 2025، لكنها لم ترتفع باطراد وانخفضت في عدة أشهر؛ ولم يُتحقق من استمرارية نطاق الإبلاغ، بما في ذلك عند تغيّر شكل الإصدار في يوليو 2025."),
]

MA_ROUTES = [  # A-8 / B-5
    ("MA-003", '["/people","/explore"]', '["/people","/","/explore"]'),
    ("MA-005", '["/access","/providers","/explore"]', '["/access","/providers","/","/explore"]'),
    ("MA-002", '["/payments","/people","/reforms"]', '["/payments","/people","/reforms","/explore"]'),
    ("MA-009", '["/payments","/people","/reforms"]', '["/payments","/people","/reforms","/explore"]'),
    ("MA-010", '["/reforms","/payments","/access","/people"]', '["/reforms","/payments","/access","/people","/explore"]'),
]

POS_NOTE = [
    (2, "because each reports POS transactions for one month within the same reporting scope, so their published totals can be read side by side.",
     "because each reports POS transactions for a single month, so their published totals can be read side by side; whether the reporting scope stayed the same across the change of release format in July 2025 has not been verified."),
    (3, "لأن كلًّا منها يذكر معاملات نقاط البيع لشهر واحد ضمن نطاق الإبلاغ نفسه، فيمكن قراءة إجمالياتها المنشورة جنبًا إلى جنب.",
     "لأن كلًّا منها يذكر معاملات نقاط البيع لشهر واحد، فيمكن قراءة إجمالياتها المنشورة جنبًا إلى جنب؛ ولم يُتحقق من استمرارية نطاق الإبلاغ عند تغيّر شكل الإصدار في يوليو 2025."),
]

C3_SITE_MAP = [
    ("en", "meta_description", "Records are set side by side on definition, period, population, geography, unit and method;",
     "Records are set side by side on definition, population, period, method, source and currentness;"),
    ("ar", "meta_description", "تُعرض السجلات جنبًا إلى جنب من حيث التعريف والفترة والمجتمع والنطاق الجغرافي والوحدة والطريقة؛",
     "تُعرض السجلات جنبًا إلى جنب من حيث التعريف والمجتمع والفترة والطريقة والمصدر وحداثة الدليل؛"),
]
C3_SECTION = [
    ("en", "Compare definition, period, population or calculation base, geography, unit and method before comparing values.",
     "The table compares definition, population or calculation base, period, method, source and currentness; read each record for its geography and unit before comparing values."),
    ("ar", "قارن التعريف والفترة ومجتمع القياس أو قاعدة الاحتساب والنطاق الجغرافي والوحدة والطريقة قبل مقارنة القيم.",
     "يقارن الجدول التعريف ومجتمع القياس أو قاعدة الاحتساب والفترة والطريقة والمصدر وحداثة الدليل؛ واقرأ كل سجل لمعرفة نطاقه الجغرافي ووحدته قبل مقارنة القيم."),
]

FINDEX = "https://data.worldbank.org/indicator/{}?locations=YE"
C1_OLD = '[{"source_id":"SRC-WB-FINDEX-AGG-2022","url":"https://data.worldbank.org/indicator/FX.OWN.TOTL.ZS?locations=YE","audit_state":"PASS_AUTHORITY_OR_PROVIDER_LOCATOR"}]'
C1_NEW = json.dumps([{"source_id": "SRC-WB-FINDEX-AGG-2022", "url": FINDEX.format(c), "audit_state": "PASS_AUTHORITY_OR_PROVIDER_LOCATOR"}
                     for c in ("FX.OWN.TOTL.ZS", "FX.OWN.TOTL.MA.ZS", "FX.OWN.TOTL.FE.ZS")], separators=(",", ":"))

ALIAS_028 = ("SEARCH-ALIAS-028", "internet; connectivity", "الإنترنت; الانترنت; الاتصال; الاتصال بالإنترنت", "route:/measurement/ | route:/people/")


def keyed_replace(s, finding, table, key, field, old, new):
    if key not in table.rows:
        raise TxError(f"{finding}: {table.sheet} has no row {key}")
    s.replace(finding, table.sheet, table.rows[key], table.col(field), old, new, f"{key}.{field}")


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    insert_ui_rows(s, "RC-15:UI", UI_ROWS)                # 04 interface copy (rows above the alias block move down)

    t06 = Table(s, "06_EVIDENCE_OBJECTS", 4)
    t02 = Table(s, "02_SITE_MAP", 4)
    for sheet, key, field, old, new in B1:
        keyed_replace(s, "RC-15:B-1", t06 if sheet == "06_EVIDENCE_OBJECTS" else t02, key, field, old, new)
    for _, key, field, old, new in B3:
        keyed_replace(s, "RC-15:B-3", t06, key, field, old, new)
    for _, key, field, old, new in B10:
        keyed_replace(s, "RC-15:B-10", t06, key, field, old, new)
    # the decision the new sentence names is listed among the record's sources, as context (adversarial review, rule 5)
    t06.set("RC-15:B-10", "CLM-015", "source_dependencies", "SRC-CBY-UNLICENSED-EWALLET-2024-001; SRC-CBY-DEC-23-2024-001",
            "SRC-CBY-UNLICENSED-EWALLET-2024-001")
    t06.set("RC-15:B-10", "CLM-015", "source_use_roles", "SRC-CBY-UNLICENSED-EWALLET-2024-001=status event; SRC-CBY-DEC-23-2024-001=context",
            "SRC-CBY-UNLICENSED-EWALLET-2024-001=status event")
    for lang, old, new in B12:
        s.replace_section("RC-15:B-12", "/payments/", 2, lang, "body", old, new)

    t10 = Table(s, "10_MEASUREMENT_AGENDA", 4)
    for key, old, new in MA_ROUTES:
        t10.set("RC-15:A-8", key, "affected_routes", new, old)

    t07 = Table(s, "07_PUBLIC_CLAIMS", 4)
    t07.set("RC-15:B-6", "CLM-026", "public_routes", '["/people","/methodology","/measurement"]', '["/people","/methodology"]')
    t06.set("RC-15:B-6", "CLM-026", "public_routes", "/people/ | /methodology/ | /measurement/", "/people/ | /methodology/")

    t06.set("RC-15:C-1", "CLM-002", "source_links", C1_NEW, C1_OLD)

    # the search-alias block (04, titled "Search aliases"): found by its header after the interface rows were inserted
    g = s.grid("04_NAV_UX")
    hdr = [i for i, r in enumerate(g, 1) if r and r[0] == "alias_id"]
    if len(hdr) != 1:
        raise TxError(f"RC-15:A-4: alias header found {len(hdr)} times")
    ta = Table(s, "04_NAV_UX", hdr[0])
    ta.set("RC-15:A-7", "SEARCH-ALIAS-026", "terms_en",
           "humanitarian; cash transfer; cash transfers; social protection; G2P; cash assistance",
           "humanitarian; cash transfer; cash transfers; social protection; G2P")
    ta.set("RC-15:A-7", "SEARCH-ALIAS-026", "terms_ar",
           "إنساني; المساعدات الإنسانية; التحويلات النقدية; الحماية الاجتماعية; مدفوعات الحكومة للأفراد; المساعدات النقدية",
           "إنساني; المساعدات الإنسانية; التحويلات النقدية; الحماية الاجتماعية; مدفوعات الحكومة للأفراد")
    last = max(ta.rows.values())
    if list(ta.rows)[-1] != "SEARCH-ALIAS-027" or (last < len(g) and any(c not in (None, "") for c in g[last])):
        raise TxError("RC-15:A-4: the alias block does not end at SEARCH-ALIAS-027 (followed by a blank row or the end of the sheet)")
    s.ed.insert_rows("04_NAV_UX", last + 1, [{1: ALIAS_028[0], 2: ALIAS_028[1], 3: ALIAS_028[2], 4: ALIAS_028[3]}])
    s.ledger.append(OrderedDict([("finding", "RC-15:A-4"), ("sheet", "04_NAV_UX"), ("row", last + 1), ("col", None),
                                 ("field", ALIAS_028[0]), ("old", None), ("new", " || ".join(ALIAS_028[1:]))]))

    _, ui = ui_block_end(s)
    for col, old, new in POS_NOTE:
        s.replace("RC-15:B-12", "04_NAV_UX", ui["UI-VIS-NOTE-POS-H1-WITHHELD"], col, old, new, "UI-VIS-NOTE-POS-H1-WITHHELD")
    for lang, field, old, new in C3_SITE_MAP:
        keyed_replace(s, "RC-15:C-3", t02, "/evidence/compare/", f"{field}_{lang}", old, new)
    for lang, old, new in C3_SECTION:
        s.replace_section("RC-15:C-3", "/evidence/compare/", 1, lang, "body", old, new)

    rep = s.save(out, ledger, OrderedDict([("transaction", "RC-15"), ("summary", "B15 d governed copy and data allowed by the red team"),
                                           ("items", OrderedDict([("B-1", len(B1)), ("B-3", len(B3)), ("B-10", len(B10)), ("B-12", len(B12)),
                                                                  ("A-8_B-5", len(MA_ROUTES)), ("A-7", 2), ("B-6", 2), ("C-1", 1),
                                                                  ("A-4", 1), ("C-3", len(C3_SITE_MAP) + len(C3_SECTION)), ("interface_rows", len(UI_ROWS))]))]))
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
