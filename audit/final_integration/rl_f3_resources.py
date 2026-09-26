# -*- coding: utf-8 -*-
"""Transaction RL-F3 — the five bounded Resource Library decisions of Session F3 (directive D7).

  python3 rl_f3_resources.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Only one of the five candidates is written to the Master (INCLUDE AS CURATED RESOURCE); the four others are recorded as
DEFER or REJECT in audit/F3_RESOURCE_DECISIONS.md and create no row. The new row is a curated card in 15_SOURCE_LIBRARY:
it binds no Evidence Record and changes no Yemen claim.
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "tranche_c"))
from tc_lib import Session, Table, TxError  # noqa: E402

S15 = "15_SOURCE_LIBRARY"
ROW = {
    "source_id": "SRC-AMB-MFB-SUPERVISION-2026",
    "primary_url": "https://www.findevgateway.org/paper/2026/09/beyond-financial-soundness-rebuilding-supervisory-framework-for-microfinance-banks-in",
    "datasets_or_use": "RESOURCE_LIBRARY_ONLY__YEMEN_MFB_SUPERVISION",
    "row_count": 0,
    "display_title": "Beyond Financial Soundness: Rebuilding the Supervisory Framework for Microfinance Banks in Yemen (2026)",
    "display_title_ar": "ما بعد السلامة المالية: إعادة بناء الإطار الإشرافي لبنوك التمويل الأصغر في اليمن (2026)",
    "publisher": "Al-Amal Microfinance Bank (published on FinDev Gateway)",
    "publisher_ar": "بنك الأمل للتمويل الأصغر (منشور على منصة FinDev Gateway)",
    "resource_category": "Yemen analytical literature and sector context",
    "resource_category_ar": "الأدبيات والتحليلات القطاعية الخاصة باليمن",
    "why_it_matters": "A paper by authors from Al-Amal Microfinance Bank on how Yemen’s microfinance banks are supervised. It argues that supervision should assess social and developmental performance alongside financial soundness, which makes it a useful starting point for regulators and providers asking how licensing and supervision relate to inclusion outcomes.",
    "why_it_matters_ar": "ورقة أعدها مؤلفون من بنك الأمل للتمويل الأصغر حول الإشراف على بنوك التمويل الأصغر في اليمن، وتدعو إلى أن يقيّم الإشراف الأداء الاجتماعي والتنموي إلى جانب السلامة المالية. وهي نقطة انطلاق مفيدة للجهات الرقابية ومقدمي الخدمة عند النظر في علاقة الترخيص والإشراف بنتائج الشمول.",
    "does_not_establish": "A proposal written by staff of a regulated microfinance bank: it is not a statement by the regulator or an independent assessment, it does not show how microfinance banks are supervised in practice or whether any institution is operating, and it provides no sector figures used by this resource.",
    "does_not_establish_ar": "مقترح كتبه موظفون في بنك تمويل أصغر خاضع للرقابة: فهو ليس بيانًا صادرًا عن الجهة الرقابية ولا تقييمًا مستقلًا، ولا يبين كيف يجري الإشراف على بنوك التمويل الأصغر فعليًا أو ما إذا كانت أي مؤسسة تعمل، ولا يقدم أرقامًا عن القطاع يستخدمها هذا المورد.",
    "public_card_state": "FULL_PUBLIC_CARD",
    "issuer": "Al-Amal Microfinance Bank",
    "hosting_platform": "FinDev Gateway",
    "rights_state": "NOT_ASSESSED",
    "retrieval_date": "2026-09-26",
    "document_label": "Research or policy paper",
    "document_label_ar": "ورقة بحثية أو سياساتية",
    "document_date": "2026-09",
}


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    head = s.header(S15, 4)
    t15 = Table(s, S15)
    if ROW["source_id"] in t15.rows:
        raise TxError("source already present")
    if any(r.get("primary_url") == ROW["primary_url"] for r in []):
        raise TxError("duplicate locator")
    g = s.grid(S15)
    for r in g[4:]:
        if r and ROW["primary_url"] in [str(x) for x in r if x]:
            raise TxError("locator already held by another source")
    last = max(t15.rows.values())
    vals = {head.index(k) + 1: v for k, v in ROW.items()}
    s.ed.insert_rows(S15, last + 1, [vals])
    for k, v in ROW.items():
        s.ledger.append({"finding": "RL-F3:FINDEV-2026", "sheet": S15, "row": last + 1, "col": head.index(k) + 1, "field": k, "old": None, "new": v})
    rep = s.save(out, ledger, {"transaction": "RL-F3", "summary": "F3: one curated resource added (FinDev Gateway, Sept 2026, MFB supervision); four candidates deferred or rejected without Master rows"})
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
