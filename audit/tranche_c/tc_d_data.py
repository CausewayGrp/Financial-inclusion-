# -*- coding: utf-8 -*-
"""Tranche C transaction TC-D — data rows, source bindings and passports (Master-first).

  python3 tc_d_data.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Lead decisions carried out here (finding in brackets):
  * [VER-01, BLOCKER] 26_FINDEX_HISTORY: the unsourced block "Uploaded 2014–2022 longitudinal inputs" (14 rows: values
    that contradict the governed Findex series, e.g. a 2022 account rate of 9.6% against the verified 11.9%, a 28.5%
    "emergency resilience" value the product says is not yet produced, and policy recommendations) is removed. It has
    no source ID and no public use; every removed cell is archived in the ledger.
  * [PAY-02/VER-17, VER-24, PAY-17] bindings: CLM-003 += SRC-CBY-POS-2025-12 (the December 2025 base it prints);
    CLM-018 += SRC-WB-FMIIP-P180708 (the FMIIP baseline it states); CLM-019 += SRC-CBY-ENF-18-2026 (status event).
  * [TRUST-23] PSE-011 and PRV-REM-E001: the subject is an individual; the personal name is removed from the Master.
  * [PAY-16] PAYCUR-001 records the 26 September 2026 recheck; PAYCUR-006 uses the governed YPCC name.
  * [VIS-09] OBS-00079 / OBS-00082 (POS value): the source's internal percentage contradiction concerns terminals and
    transactions, not value; the value rows no longer carry it (no disagreement marker without a second figure).
  * [currentness] 23_REMITTANCES gains the CBY-Aden Annual Report 2025 value for 2025 (3,614.05 USD million), read from
    the same table as the governed 2021–2024 values; LIBRARY/CONTEXT ONLY — not part of the indexed comparison.
  * [VER-11, PAY-10, VER-24, PAY-08] passports: residual-model withholding reason; "Workers'" removed; provider-status
    period and limit; BOP↔IIP limit; CBY-Aden naming.
  * [JRN-01] CLM-051: the method says that the type-level values behind each group are not reproduced here
    (EXPLICIT EVIDENCE FRONTIER; the row-to-group mapping is not held in the Master).
"""
import json, os, sys
from collections import OrderedDict
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from tc_lib import Session, Table, TxError, norm  # noqa: E402

F = "TC-D"


def sub(t, finding, key, field, old, new):
    cur = t.get(key, field)
    if not isinstance(cur, str) or cur.count(old) != 1:
        raise TxError(f"{finding}: {t.sheet} {key}.{field}: {0 if not isinstance(cur, str) else cur.count(old)} x {old!r}")
    t.set(finding, key, field, cur.replace(old, new), cur)


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)

    # ---- 06 bindings and CLM-051 method ------------------------------------------------------------
    t06 = Table(s, "06_EVIDENCE_OBJECTS")
    t06.set(F + ":VER-17", "CLM-003", "source_dependencies", "SRC-CBY-POS-2025-03; SRC-CBY-POS-2025-12; SRC-CBY-POS-2026-01",
            "SRC-CBY-POS-2025-03; SRC-CBY-POS-2026-01")
    links = json.loads(t06.get("CLM-003", "source_links"))
    t15 = Table(s, "15_SOURCE_LIBRARY")
    url = t15.get("SRC-CBY-POS-2025-12", "primary_url")
    if not url:
        raise TxError("SRC-CBY-POS-2025-12 has no locator")
    links = [links[0], {"source_id": "SRC-CBY-POS-2025-12", "url": url, "audit_state": "PASS_AUTHORITY_OR_PROVIDER_LOCATOR"}] + links[1:]
    t06.set(F + ":VER-17", "CLM-003", "source_links", json.dumps(links, ensure_ascii=False, separators=(",", ":")), t06.get("CLM-003", "source_links"))
    cur = t06.get("CLM-018", "source_dependencies")
    t06.set(F + ":PAY-17", "CLM-018", "source_dependencies", cur + "; SRC-WB-FMIIP-P180708", cur)
    cur = t06.get("CLM-019", "source_dependencies")
    t06.set(F + ":VER-24", "CLM-019", "source_dependencies", cur + "; SRC-CBY-ENF-18-2026", cur)
    cur = t06.get("CLM-019", "source_use_roles")
    t06.set(F + ":VER-24", "CLM-019", "source_use_roles", cur + "; SRC-CBY-ENF-18-2026=status event", cur)
    for L, add in (("en", " The type-level values from Table 8 that make up each group are not reproduced in this resource."),
                   ("ar", " ولا يعرض هذا المورد قيم أنواع المعاملات في الجدول 8 التي تتكون منها كل مجموعة.")):
        cur = t06.get("CLM-051", "method_" + L)
        t06.set(F + ":JRN-01", "CLM-051", "method_" + L, cur.rstrip() + add, cur)

    # ---- 22 providers ---------------------------------------------------------------------------------
    g22 = s.grid("22_PROVIDERS_DATA")
    rows = {r[0]: i for i, r in enumerate(g22, 1) if r and r[0] in ("PSE-011", "PRV-REM-E001", "PAYCUR-001", "PAYCUR-006")}
    r = rows["PSE-011"]
    s.set(F + ":TRUST-23", "22_PROVIDERS_DATA", r, 5, "One remittance agent (an individual named in the decision) — Lahj/Tuban",
          "Iyad Al-Saadi — remittance agent — Lahj/Tuban", "PSE-011.event_scope")
    s.set(F + ":TRUST-23", "22_PROVIDERS_DATA", r, 8,
          "Governor Decision No. 9 of 2026 suspends the licence of a remittance agent in Lahj/Tuban and closes the premises; the agent is an individual and is not named in this resource.",
          "Governor Decision No. 9 of 2026 suspends the licence of Iyad Al-Saadi remittance agent in Lahj/Tuban and closes the premises.", "PSE-011.normalized_event")
    s.set(F + ":TRUST-23", "22_PROVIDERS_DATA", r, 10, "May show the dated event; the subject is an individual and is not named.",
          "May show the exact dated event and subject.", "PSE-011.public_use")
    r = rows["PRV-REM-E001"]
    s.set(F + ":TRUST-23", "22_PROVIDERS_DATA", r, 2, "Remittance agent named in Governor's Decision No. 9 of 2026 (an individual) - Lahj/Tuban",
          "Iyad Al-Saadi - remittance agent - Lahj/Tuban", "PRV-REM-E001.canonical_name_en")
    s.set(F + ":TRUST-23", "22_PROVIDERS_DATA", r, 3, "وكيل حوالة مسمى في قرار المحافظ رقم 9 لسنة 2026 (فرد) - لحج/تبن",
          "أياد السعدي - وكيل حوالة - لحج/تبن", "PRV-REM-E001.canonical_name_ar")
    r = rows["PAYCUR-001"]
    for col in (3, 5, 7):
        cur = s.ed.get_value("22_PROVIDERS_DATA", r, col)
        if "2026-09-09" not in cur:
            raise TxError(f"PAYCUR-001 c{col}")
        s.set(F + ":PAY-16", "22_PROVIDERS_DATA", r, col, cur.replace("2026-09-09", "2026-09-26"), cur, f"PAYCUR-001.c{col}")
    r = rows["PAYCUR-006"]
    s.set(F + ":PAY-17", "22_PROVIDERS_DATA", r, 2, "Yemeni Payments and Clearing Company", "Yemen Payments and Clearing Company", "PAYCUR-006.object_family")

    # ---- 19 POS value rows ----------------------------------------------------------------------------
    g19 = s.grid("19_PAYMENTS_DATA")
    for oid in ("OBS-00079", "OBS-00082"):
        i = [k for k, x in enumerate(g19, 1) if x and x[0] == oid][0]
        s.set(F + ":VIS-09", "19_PAYMENTS_DATA", i, 14, "DIRECTLY_COMPARABLE", "DIRECTLY_COMPARABLE_WITH_SOURCE_INTERNAL_PERCENT_CONTRADICTION", oid + ".comparability_state")

    # ---- 23 remittances: AR2025 value for 2025 (context only) -------------------------------------------
    g23 = s.grid("23_REMITTANCES")
    last = [k for k, x in enumerate(g23, 1) if x and x[0] == "RMO-CBY-2023-AR2025"][0]
    if any(x and x[0] == "RMO-CBY-2025-AR2025" for x in g23):
        raise TxError("23 already has RMO-CBY-2025-AR2025")
    base = list(g23[last - 1])
    base[0], base[5], base[10] = "RMO-CBY-2025-AR2025", "2025", 3614.05
    base[19] = "LATEST_YEAR_AR2025_VINTAGE__CONTEXT_ONLY"
    base[20] = ("AR2025 publication vintage; latest year in the table. Recorded for context only: it is not part of the 2021–2024 "
                "indexed comparison, and its raw level is not comparable with the IMF series (CLM-037).")
    base[21] = ("نسخة النشر في التقرير السنوي 2025؛ وهي آخر سنة في الجدول. مسجلة للسياق فقط: ليست جزءًا من مقارنة المسارين المؤشَّرين "
                "للفترة 2021–2024، ولا يقارن مستواها الخام بسلسلة صندوق النقد (CLM-037).")
    s.ed.insert_rows("23_REMITTANCES", last + 1, [{i + 1: v for i, v in enumerate(base) if v is not None}])
    s.ledger.append(OrderedDict([("finding", F + ":currentness"), ("sheet", "23_REMITTANCES"), ("row", None), ("col", None),
                                 ("field", "RMO-CBY-2025-AR2025"), ("old", None), ("new", "2025 = 3614.05 USD million (AR2025 vintage)")]))

    # ---- 26: remove the unsourced uploaded block (rows 86..101) -------------------------------------------
    g26 = s.grid("26_FINDEX_HISTORY")
    title = [k for k, x in enumerate(g26, 1) if x and x[0] == "Uploaded 2014–2022 longitudinal inputs"]
    if len(title) != 1 or title[0] != 88 or len(g26) != 101 or any(v not in (None, "") for v in g26[85] + g26[86]):
        raise TxError("26 block not where expected")
    archived = [[v for v in g26[k - 1]] for k in range(88, 102)]
    s.ed.delete_rows("26_FINDEX_HISTORY", 86, 101)
    s.ledger.append(OrderedDict([("finding", F + ":VER-01"), ("sheet", "26_FINDEX_HISTORY"), ("row", "86-101"), ("col", None),
                                 ("field", "Uploaded 2014–2022 longitudinal inputs (removed; unsourced)"), ("old", archived), ("new", None)]))

    # ---- 34 passports ----------------------------------------------------------------------------------
    t34 = Table(s, "34_EVIDENCE_PASSPORTS")
    t34.set(F + ":VER-24", "EP-CBY-PROVIDER-STATUS-2026", "object",
            "CBY-Aden 2026 licence suspension, withdrawal and closure events for exchange and remittance providers",
            "CBY 2026 exchange/remittance licence suspension/withdrawal events")
    t34.set(F + ":VER-24", "EP-CBY-PROVIDER-STATUS-2026", "reference_period", "1 January to 24 September 2026", "2026-01 to 2026-08")
    t34.set(F + ":EN-07", "EP-CBY-PROVIDER-STATUS-2026", "critical_limit",
            "Later enforcement events are not subtracted mechanically from the 2026 annual roster. A current count of operating providers would require entity-by-entity reconciliation, a defined status date and a clear operating criterion. Silence about another provider does not establish that it is active or compliant.",
            "Do not subtract later enforcement events mechanically from the 2026 annual roster. A current operating-provider count requires entity-by-entity reconciliation, a defined status date and a clear operating criterion. Silence about another provider does not establish that it is active or compliant.")
    t34.set(F + ":VER-11", "EP-CCY-REMIT-RESIDUAL-MODEL-K04", "object",
            "Residual-model remittance estimate, 2024 (producer and value withheld: no public locator)",
            "Residual-model remittance estimate, 2024 (producer and value withheld: no public locator; reuse rights not assessed)")
    t34.set(F + ":VER-11", "EP-CCY-REMIT-RESIDUAL-MODEL-K04", "publisher", "Withheld — no public locator",
            "Withheld — no public locator; reuse rights not assessed")
    t34.set(F + ":VER-11", "EP-CCY-REMIT-RESIDUAL-MODEL-K04", "display_requirements",
            "Never replace official baselines. The value and the producer are not shown until the material has a public locator (Master-first).",
            "Never replace official baselines. Do not show the value or name the producer until the material has a public locator and a rights assessment (Master-first).")
    t34.set(F + ":PAY-10", "EP-CBY-REMITTANCE-VINTAGE-K04", "object", "Remittances across CBY-Aden annual-report vintages",
            "Workers' remittances across CBY annual-report vintages")
    t34.set(F + ":EN-27", "EP-YEM-BOP-IIP-RECON-K04", "critical_limit",
            "The reconciliation specification is defined; Yemen IIP input positions and a reconciliation table are not yet available in the public evidence base.",
            "Specification is operational; Yemen IIP input positions/reconciliation table are not yet available in the current public evidence base.")
    sub(t34, F + ":PAY-01", "EP-CBY-FCP-REDRESS-2024", "metric_or_scope", "escalation window to CBY", "escalation window to CBY-Aden")

    rep = s.save(out, ledger, {"transaction": "TC-D", "summary": "bindings, PSE-011 name, PAYCUR, POS value markers, AR2025 2025 value, 26 block removed, passports"})
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
