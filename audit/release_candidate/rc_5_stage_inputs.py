# -*- coding: utf-8 -*-
"""RC-5 staged controlled input (installed by audit/tranche_b_execution/run_stage.py with --install).

  python3 rc_5_stage_inputs.py <stage_dir>

scripts/projection/controlled_inputs/visual_design_contract.json — VIS-PROVIDER-OBSERVABILITY binds the Arabic period
columns RC-5 adds to 22_PROVIDERS_DATA (B2 item g): the universe object's date_ar from reference_state_ar and the wallet
counts' date_ar from reference_period_ar. The loader prints date_ar on the Arabic edition where it exists.
The JSON indent of the file is kept (one space).
"""
import json, os, sys
from collections import OrderedDict

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


def main():
    stage = sys.argv[1]
    os.makedirs(stage, exist_ok=True)
    p = os.path.join(ROOT, "scripts/projection/controlled_inputs/visual_design_contract.json")
    with open(p, encoding="utf-8") as fh:
        vdc = json.load(fh, object_pairs_hook=OrderedDict)
    v = next(x for x in vdc["visuals"] if x["visual_id"] == "VIS-PROVIDER-OBSERVABILITY")
    want = {"universe": ("reference_state", "reference_state_ar"), "wallet_counts": ("reference_period", "reference_period_ar")}
    for o in v["contract"]["objects"]:
        if o["id"] in want:
            en, ar = want[o["id"]]
            if o["fields"].get("date") != en or "date_ar" in o["fields"]:
                raise SystemExit(f"{o['id']}: fields not as expected: {dict(o['fields'])}")
            new = OrderedDict()
            for k, val in o["fields"].items():
                new[k] = val
                if k == "date":
                    new["date_ar"] = ar
            o["fields"] = new
    with open(os.path.join(stage, "visual_design_contract.json"), "w", encoding="utf-8") as fh:
        json.dump(vdc, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("staged:", os.path.join(stage, "visual_design_contract.json"))


if __name__ == "__main__":
    main()
