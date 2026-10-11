#!/usr/bin/env python3
"""Run the public-literal audit without writing the committed closure (the gate negative controls use it).

  python3 scripts/tests/literal_audit_check.py

Exit code and output are the audit's; audit/PUBLIC_LITERAL_CLOSURE.json is left untouched.
"""
import os
import subprocess
import sys
import tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

with tempfile.TemporaryDirectory() as d:
    r = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "audit_public_literals.py"), "--out", os.path.join(d, "closure.json")],
                       cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    sys.stdout.write(r.stdout + r.stderr)
    sys.exit(r.returncode)
