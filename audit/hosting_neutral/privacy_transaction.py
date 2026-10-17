"""HOST-NEUTRAL: exact-value bilingual privacy correction, owner 16 October 2026.

Consumers: privacy HTML, page specs, full-copy projections and Search. No evidence/source changes.
Arguments: input Master, staged Master, ledger, scratch directory.
"""
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "close_out"))
from close_lib import Session, TxError


def main():
    src, out, ledger, work = sys.argv[1:5]
    if hashlib.sha256(Path(src).read_bytes()).hexdigest() != "580d2dc19054658d906585104b957a0fe9f4f3ce4758e6bc19b1cae28fb28bc8":
        raise TxError("Inspect/replay against current Master; do not overwrite another transaction")
    session = Session(src, work)
    plan = json.loads(Path(__file__).with_name("PRIVACY_CELL_PLAN.json").read_text())
    for cell in plan:
        session.set_section("HOST-NEUTRAL", cell["route"], cell["section"], cell["lang"],
                            cell["field"], cell["new"], cell["old"])
    report = session.save(out, ledger, {"transaction": "HOST-NEUTRAL", "decision": "audit/OWNER_DECISIONS_2026-10-16.md"})
    print(json.dumps({k: report[k] for k in ("cells_written", "input_master_sha256", "output_master_sha256")}))


if __name__ == "__main__":
    main()
