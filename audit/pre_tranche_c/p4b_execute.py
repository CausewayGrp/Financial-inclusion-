# -*- coding: utf-8 -*-
"""P4-B — English 'limits of the measure' written as reader prose (Master-first).

  python3 p4b_execute.py <in_master.xlsx> <out_master.xlsx> <ledger.json> <work_dir>

Part B of 06 limitations_en was appended from passport shorthand (34 critical_limit): ">1/4 PSUs replaced", "E&O", "IIP",
"negative-authority state". Once P4.3 shows part B under its own label, that shorthand is public copy. The English is
rewritten as prose with the same content; the Arabic part B (already prose) fixes the meaning. Passports keep their
internal shorthand. Part A and the delimiter are untouched.
"""
import sys
from ptc_lib import Session, TxError
from projection.master_reader import Workbook

S06 = "06_EVIDENCE_OBJECTS"
FINDEX = ("Approx. 23% population geography excluded; >1/4 PSUs replaced",
          "The survey frame excludes areas holding about 23% of the population, and more than a quarter (1/4) of primary sampling units were replaced.")
FIRM = ("Not national; some tables have small conditional denominators; obstacle tabulation has filtered denominator",
        "The survey is not national; some tables rest on small conditional bases, and the finance-obstacle table uses a filtered base.")
NEW_B = {
    "CLM-001": FINDEX, "CLM-002": FINDEX, "CLM-025": FINDEX, "CLM-005": FIRM, "CLM-006": FIRM,
    "CLM-007": ("Not payment-system settlement throughput and not directly measured hawala volume",
                "This is an external-sector macro concept, not payment-system settlement throughput and not a direct measure of informal hawala volume."),
    "CLM-015": ("A dated negative-authority state only. Do not carry status to 2026, infer current operation, or derive the positive licensed universe.",
                "This is a dated list of names declared unlicensed on the source date only. It cannot be carried to 2026, and it shows neither current operation nor which wallets are licensed."),
    "CLM-018": ("Institutionalization/implementation-state evidence only. Does not prove system go-live, universal participation, reliability, adoption, transaction coverage or inclusion outcomes.",
                "This is evidence of institutional and implementation states only; it does not prove system go-live, universal participation, reliability, adoption, transaction coverage or inclusion outcomes."),
    "CLM-042": ("Component-specific comparability only; sign/scope/method differences remain material.",
                "Comparability is component-specific only; differences of sign, scope and method remain material."),
    "CLM-043": ("E&O is a net balancing residual and cannot identify a missing component or gross offsetting errors.",
                "Errors and omissions is a net balancing residual; it cannot identify a missing component or gross offsetting errors."),
    "CLM-044": ("Errors in other BOP components and the E&O assumption load into the remittance residual; informal remittances are not directly observed.",
                "Errors in other balance-of-payments components, and the assumption made about errors and omissions, flow into the remittance residual; informal remittances are not directly observed."),
    "CLM-047": ("Specification is operational; Yemen IIP input positions/reconciliation table are not yet available in the current public evidence base.",
                "The specification is operational, but Yemen's international investment position inputs and reconciliation table are not yet in the current public evidence base."),
    "CLM-050": ("Accounts are not unique people or automatically active; 23% is a source average, not provider-specific/current.",
                "Accounts are not unique people and are not automatically active; the 23% is a source-wide average, not a provider-specific or current rate."),
    "CLM-051": ("Transaction value is not unique users, merchant adoption, welfare or durable inclusion; grouping is CauseWay-derived, not source-native.",
                "Transaction value is not unique users, merchant adoption, welfare or durable inclusion; the grouping is this resource's own, not the source's classification."),
    "CLM-052": ("Not national adult prevalence; not current geography; not comparable to Findex without universe/method bridge; 611-user survey has different sample composition.",
                "This is not national adult prevalence and not current geography; it is not comparable with Findex without a bridge between their populations and methods, and the 611-user survey has a different sample composition."),
    "CLM-053": ("Primary 2023 source object and universe bridge are not yet available for direct verification; cannot be treated as 2026 or as population prevalence",
                "The primary 2023 source and the bridge between provider coverage across periods are not yet available for direct verification; the figure cannot be treated as a 2026 level or as population prevalence."),
}


def main():
    src, out, ledger, work = sys.argv[1:5]
    s = Session(src, work)
    g = Workbook(src).grid(S06)
    col = [str(x) for x in g[3]].index("limitations_en") + 1
    for oid, (old, new) in NEW_B.items():
        r = next(i for i, x in enumerate(g, 1) if x and x[0] == oid)
        cur = g[r - 1][col - 1]
        if " | " + old not in cur or not cur.endswith(old):
            raise TxError(f"{oid}: part B is not {old[:50]!r}")
        s.replace("P4-E02", S06, r, col, " | " + old, " | " + new, f"{oid}.limitations_en[B]")
    rep = s.save(out, ledger, [("transaction", "P4-B"), ("scope", "P4.3 English part-B prose for passport shorthand")])
    print(f"P4-B staged: {rep['cells_written']} changes; Master {rep['output_master_sha256']}")


if __name__ == "__main__":
    main()
