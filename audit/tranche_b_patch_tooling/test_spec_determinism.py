# -*- coding: utf-8 -*-
"""Determinism gate for the Master-first patch spec.

Rebuilds the spec twice, in independent processes, from the same Production Master:
  run A: PYTHONHASHSEED=1, glob results in natural order
  run B: PYTHONHASHSEED=4242, glob results reversed (simulates a different filesystem order)
and requires byte-identical outputs for:
  MASTER_FIRST_PATCH_SPEC.csv, TERMINOLOGY_SWEEP_KEEP_REGISTER.csv, SOURCE_PUBLISHER_PROPOSALS.csv

Usage:  python3 test_spec_determinism.py <Master.xlsx> [--compare-to <dir with committed outputs>]
Work directories are created with tempfile (set TMPDIR to keep them outside the repository).
Exit code 0 = PASS; 1 = FAIL.
"""
import hashlib, os, subprocess, sys, tempfile, json

HERE = os.path.dirname(os.path.abspath(__file__))
OUTS = ["MASTER_FIRST_PATCH_SPEC.csv", "TERMINOLOGY_SWEEP_KEEP_REGISTER.csv", "SOURCE_PUBLISHER_PROPOSALS.csv"]

def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def run(master_json, out, seed, reverse):
    env = dict(os.environ, PYTHONHASHSEED=str(seed), YFI_MASTER_JSON=master_json)
    code = ("import glob,runpy,sys\n"
            + ("_g=glob.glob\nglob.glob=lambda *a,**k: list(reversed(_g(*a,**k)))\n" if reverse else "")
            + f"sys.argv=['build_spec.py',{out!r}]\nrunpy.run_path({os.path.join(HERE,'build_spec.py')!r},run_name='__main__')\n")
    r = subprocess.run([sys.executable, "-c", code], env=env, cwd=HERE, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stdout[-2000:], r.stderr[-4000:]); raise SystemExit(1)
    errs = [l for l in r.stdout.splitlines() if l.startswith("ERRORS:")]
    return errs[-1] if errs else "ERRORS: ?"

def main():
    master = sys.argv[1]
    cmp_dir = sys.argv[sys.argv.index("--compare-to") + 1] if "--compare-to" in sys.argv else None
    base = tempfile.mkdtemp(prefix="yfi_spec_det_")
    res = {}
    for tag, seed, rev in (("A", 1, False), ("B", 4242, True)):
        mj = os.path.join(base, f"master_{tag}"); out = os.path.join(base, f"out_{tag}")
        subprocess.run([sys.executable, os.path.join(HERE, "export_master.py"), master, mj], check=True, capture_output=True)
        e = run(mj, out, seed, rev)
        res[tag] = {"errors_line": e, **{f: sha(os.path.join(out, f)) for f in OUTS}}
    ok = all(res["A"][f] == res["B"][f] for f in OUTS) and res["A"]["errors_line"] == "ERRORS: 0" == res["B"]["errors_line"]
    report = {"master_sha256": sha(master), "runs": res, "identical": ok}
    if cmp_dir:
        committed = {f: sha(os.path.join(cmp_dir, f)) for f in OUTS if os.path.exists(os.path.join(cmp_dir, f))}
        report["committed"] = committed
        report["committed_matches_rebuild"] = all(committed.get(f) == res["A"][f] for f in OUTS)
        ok = ok and report["committed_matches_rebuild"]
    report["work_dir"] = base
    print(json.dumps(report, indent=1))
    print("SPEC DETERMINISM", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
