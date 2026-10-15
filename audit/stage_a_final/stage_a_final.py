"""STAGE-A-FINAL: exact-value Master reconciliation, owner mandate 15 October 2026.

Arguments: input Master, staged Master, ledger, scratch directory.
The recorded cell plan is reviewable and guarded against the physical Production Master.
"""
import hashlib
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'close_out'))
from close_lib import Session, TxError, refresh_self_counts


def main():
    src, out, ledger, work = sys.argv[1:5]
    if hashlib.sha256(Path(src).read_bytes()).hexdigest() != '87dafc6f18837ff61f032f1c93a7668c9affe9638aa104ab6ad50a2c05512975':
        raise TxError('STAGE-A-FINAL: unexpected Production Master; inspect/replay, never merge the binary')
    s = Session(src, work)
    for x in json.loads(Path(__file__).with_name('STAGE_A_FINAL_CELL_PLAN.json').read_text(encoding='utf-8')):
        s.set(x['finding'], x['sheet'], x['row'], x['col'], x['new'], x['old'],
              f"{x['sheet']}!R{x['row']}C{x['col']}")
    counts = refresh_self_counts(s, 'STAGE-A-FINAL:self-counts')
    rep = s.save(out, ledger, {'transaction': 'STAGE-A-FINAL', 'summary': 'Separate edition and checking clocks; withdraw unsupported IMF missing-value and World Bank publisher-contradiction interpretations, EN/AR together. No historical values or reporting universes changed.', 'self_counts': counts})
    print(json.dumps({k: rep[k] for k in ('input_master_sha256', 'output_master_sha256', 'cells_written')}))


if __name__ == '__main__':
    main()
