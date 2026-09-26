#!/usr/bin/env python3
"""P5.1 regression test: the public-literal audit is a function of the repository alone.

  python3 scripts/tests/test_literal_audit_determinism.py

Runs scripts/audit_public_literals.py in fresh processes under several PYTHONHASHSEED values, each writing to a temporary
file, and requires, for every run:
  - identical bytes of the literal-closure file, and therefore an identical SHA-256;
  - identical record ordering (route, surface, field, token, context);
  - identical source_object attribution per record;
  - equality with the committed audit/PUBLIC_LITERAL_CLOSURE.json (same canonical repository -> same file).
Exit 1 on any difference.
"""
import hashlib
import json
import os
import subprocess
import sys
import tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SEEDS = ["0", "1", "2", "3", "7", "42", "1234", "99991"]
COMMITTED = os.path.join(ROOT, "audit", "PUBLIC_LITERAL_CLOSURE.json")


def run(seed, out):
    env = dict(os.environ, PYTHONHASHSEED=seed, PYTHONDONTWRITEBYTECODE="1")
    r = subprocess.run([sys.executable, "scripts/audit_public_literals.py", "--out", out], cwd=ROOT, env=env, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(f"seed {seed}: audit failed: {(r.stdout + r.stderr)[-400:]}")
    return open(out, "rb").read()


def main():
    failures = []
    runs = {}
    with tempfile.TemporaryDirectory() as d:
        for seed in SEEDS:
            runs[seed] = run(seed, os.path.join(d, f"closure_{seed}.json"))
    shas = {s: hashlib.sha256(b).hexdigest() for s, b in runs.items()}
    ref_seed = SEEDS[0]
    ref = json.loads(runs[ref_seed])
    order = [(r["route"], r["surface"], r["field"], r["token"], r["context"]) for r in ref["records"]]
    attrib = [r.get("source_object") for r in ref["records"]]
    for seed, b in runs.items():
        doc = json.loads(b)
        if b != runs[ref_seed]:
            failures.append(f"seed {seed}: bytes differ from seed {ref_seed}")
        if [(r["route"], r["surface"], r["field"], r["token"], r["context"]) for r in doc["records"]] != order:
            failures.append(f"seed {seed}: record ordering differs")
        if [r.get("source_object") for r in doc["records"]] != attrib:
            failures.append(f"seed {seed}: source_object attribution differs")
    committed = open(COMMITTED, "rb").read() if os.path.exists(COMMITTED) else b""
    if committed != runs[ref_seed]:
        failures.append("committed audit/PUBLIC_LITERAL_CLOSURE.json differs from the audit output (re-run scripts/audit_public_literals.py)")
    for seed in SEEDS:
        print(f"seed {seed:>6}  sha256 {shas[seed]}")
    print(f"records {len(ref['records'])}; unresolved {ref['unresolved_substantive_count']}")
    if failures:
        for f in failures:
            print("FAIL", f)
        print("LITERAL AUDIT DETERMINISM FAIL")
        sys.exit(1)
    print(f"LITERAL AUDIT DETERMINISM PASS: {len(SEEDS)} hash seeds, one SHA-256 {shas[ref_seed]}")


if __name__ == "__main__":
    main()
