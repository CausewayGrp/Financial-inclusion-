# -*- coding: utf-8 -*-
"""Tranche C transaction TC-G — residual Master findings after the lens-by-lens transactions.

  python3 tc_g_residual.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

  * [VER-18] CLM-046 binds the three Saudi Press Agency announcements the library already holds (the 2018 and 2023
    deposits and the 2026 SAR 1.3 billion agreement); CLM-053 binds the identified SFD/SMED November 2023 page in a
    context role (the record says the figure is not yet verified against it).
  * [EN-07] CLM-046's summary states the rule declaratively ("are not added"), not as an instruction.
  * [PAY-11, NARROW] The three POS series records say that from July 2025 the monthly releases take the form of a one-page
    infographic (governed in 19_PAYMENTS_DATA source_locator) and that continuity of the reporting scope across that change
    has not been verified. The exchange-rate caveat is not added: it would need rounded rates that are not governed.
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from tc_lib import Session, Table, TxError  # noqa: E402

F = "TC-G"
POS_B_EN = ("From July 2025 the monthly releases take the form of a one-page infographic; continuity of the reporting scope "
            "across that change has not been verified.")
POS_B_AR = ("وابتداءً من يوليو 2025 تصدر الإصدارات الشهرية في صورة إنفوغرافيك من صفحة واحدة، ولم يُتحقق من استمرارية نطاق "
            "الإبلاغ عبر هذا التغير.")


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    t = Table(s, "06_EVIDENCE_OBJECTS")
    cur = t.get("CLM-046", "source_dependencies")
    spa = ["SRC-SPA-SAU-CBY-DEPOSIT-2018-001", "SRC-SPA-SAU-CBY-DEPOSIT-2023-001", "SRC-SPA-SAU-BUDGET-2026-001"]
    if any(x in cur for x in spa):
        raise TxError("CLM-046 already binds SPA")
    t.set(F + ":VER-18", "CLM-046", "source_dependencies", cur + "; " + "; ".join(spa), cur)
    roles = t.get("CLM-046", "source_use_roles")
    t.set(F + ":VER-18", "CLM-046", "source_use_roles",
          "; ".join([x for x in [roles] if x] + [f"{x}=primary factual evidence" for x in spa]), roles)
    t.set(F + ":EN-07", "CLM-046", "summary_en",
          "Saudi support is recorded by financial state. A pledge, commitment, signed agreement, deposited amount, amount made available, "
          "budget disbursement, FX-auction use, in-kind support and project cost are not interchangeable, and they are not added into a "
          "cumulative total here.",
          "Saudi support must be read by financial state. A pledge, commitment, signed agreement, deposited amount, amount made available, "
          "budget disbursement, FX-auction use, in-kind support and project cost are not interchangeable and must not be automatically "
          "added into a cumulative total.")
    t.set(F + ":EN-07", "CLM-046", "summary_ar",
          "يُسجَّل الدعم السعودي بحسب حالته المالية. فالتعهد والالتزام والاتفاق الموقّع والمبلغ المودع والمبلغ المتاح والصرف للموازنة "
          "والاستخدام في مزادات النقد الأجنبي والدعم العيني وتكلفة المشروع ليست حالات مترادفة، ولا تُجمع هنا في إجمالي تراكمي واحد.",
          "يجب قراءة الدعم السعودي بحسب حالته المالية. فالتعهد والالتزام والاتفاق الموقّع والمبلغ المودع والمبلغ المتاح والصرف للموازنة "
          "والاستخدام في مزادات النقد الأجنبي والدعم العيني وتكلفة المشروع ليست حالات مترادفة، ولا يجوز جمعها تلقائيًا في إجمالي تراكمي واحد.")
    cur = t.get("CLM-053", "source_dependencies")
    t.set(F + ":VER-18", "CLM-053", "source_dependencies", cur + "; SRC-SFD-SMED-LP-2023-NOV", cur)
    roles = t.get("CLM-053", "source_use_roles")
    t.set(F + ":VER-18", "CLM-053", "source_use_roles", "; ".join([x for x in [roles] if x] + ["SRC-SFD-SMED-LP-2023-NOV=context"]), roles)
    for vid in ("VIS-POS-TERMINALS", "VIS-POS-TRANSACTIONS", "VIS-POS-VALUE"):
        for L, b in (("en", POS_B_EN), ("ar", POS_B_AR)):
            cur = t.get(vid, "limitations_" + L)
            if " | " in cur:
                raise TxError(f"{vid} already has a measure limit")
            t.set(F + ":PAY-11", vid, "limitations_" + L, cur.rstrip() + " | " + b, cur)
    rep = s.save(out, ledger, {"transaction": "TC-G", "summary": "VER-18 bindings; CLM-046 declarative; PAY-11 POS release-form note"})
    print(json.dumps({k: rep[k] for k in ("input_master_sha256", "output_master_sha256", "cells_written")}))


if __name__ == "__main__":
    try:
        main()
    except TxError as ex:
        print("TX ERROR:", ex)
        sys.exit(2)
