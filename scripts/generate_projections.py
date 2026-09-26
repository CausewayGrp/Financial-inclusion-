# -*- coding: utf-8 -*-
"""Repository command: regenerate the governed projection layer from the Production Master.

  python3 scripts/generate_projections.py [--master PATH] [--out DIR] [--check]

Default Master: authority/Yemen_Financial_Inclusion_Evidence_Master.xlsx. Default output: site-src/content.
--check regenerates in memory and exits 1 if any committed projection differs.
"""
import argparse, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from projection.generator import generate

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--master", default=os.path.join(ROOT, "authority", "Yemen_Financial_Inclusion_Evidence_Master.xlsx"))
    ap.add_argument("--out", default=None)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    rep = generate(a.master, ROOT, out_dir=a.out, check=a.check)
    print(json.dumps({k: (v if k != "output_sha256" else len(v)) for k, v in rep.items()}, ensure_ascii=False, indent=1))
    if a.check and rep["differences"]:
        print("PROJECTION CHECK FAIL"); sys.exit(1)
    print("PROJECTION CHECK PASS" if a.check else "PROJECTIONS GENERATED")

if __name__ == "__main__":
    main()
