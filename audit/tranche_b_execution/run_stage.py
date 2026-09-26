# -*- coding: utf-8 -*-
"""Commit one execution stage to the canonical repository, or roll it back.

  python3 run_stage.py <stage_id> <staged_master.xlsx> <snapshot_dir> <timestamp> <report.json> [--allow-validator-errors REGEX]
                       [--install STAGED_FILE=REPO_RELATIVE_PATH ...]   (contract files installed after the snapshot)

Steps: snapshot current state (outside the repository) -> install staged Master -> regenerate every projection
(scripts/generate_projections.py) -> rebind current-state control files (scripts/rebind_authority.py) -> build ->
public-literal audit -> architecture diagrams -> handoff inventory (F9) -> repository manifest -> validator -> generator
idempotence check (--check). Any failure restores the snapshot. New files must be tracked (git add) before the run so
that the manifest classifies them.
"""
import hashlib, json, os, re, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
STATE = ["authority", "site-src/content", "handoff", "README.md", "audit/PUBLIC_LITERAL_CLOSURE.json", "dist",
         "scripts/projection/master_structure.json", "scripts/projection/projection_manifest.json", "scripts/projection/controlled_inputs",
         # P5: files the rebind and the diagram step also write, so that a rollback restores them too
         "OPENAI_REENTRY_CHECKPOINT.md", "design/architecture",
         # F5: the repository manifest records the Master and page-spec hashes, so a Master change rewrites it
         "FINAL_REPOSITORY_MANIFEST.json"]


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def run(cmd):
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr)


def snapshot(dst):
    os.makedirs(dst, exist_ok=True)
    for rel in STATE:
        src = os.path.join(ROOT, rel)
        d = os.path.join(dst, rel)
        if os.path.isdir(src):
            if os.path.exists(d):
                raise SystemExit(f"snapshot target exists: {d}")
            shutil.copytree(src, d)
        else:
            os.makedirs(os.path.dirname(d), exist_ok=True)
            shutil.copy2(src, d)


def restore(src):
    for rel in STATE:
        s = os.path.join(src, rel)
        d = os.path.join(ROOT, rel)
        if os.path.isdir(s):
            # replace directory contents file by file (no recursive delete of the canonical root)
            for dp, dn, fn in os.walk(d, topdown=False):
                for f in fn:
                    rp = os.path.relpath(os.path.join(dp, f), d)
                    if not os.path.exists(os.path.join(s, rp)):
                        os.remove(os.path.join(dp, f))
            for dp, dn, fn in os.walk(s):
                for f in fn:
                    rp = os.path.relpath(os.path.join(dp, f), s)
                    os.makedirs(os.path.dirname(os.path.join(d, rp)), exist_ok=True)
                    shutil.copy2(os.path.join(dp, f), os.path.join(d, rp))
        else:
            shutil.copy2(s, d)


def main():
    stage, staged, snap, ts, report = sys.argv[1:6]
    allow = None
    if "--allow-validator-errors" in sys.argv:
        allow = re.compile(sys.argv[sys.argv.index("--allow-validator-errors") + 1])
    installs = [a.split("=", 1) for a in sys.argv[6:] if "=" in a and not a.startswith("--")]
    rep = {"stage": stage, "staged_master_sha256": sha(staged), "installed": [d for _, d in installs], "steps": []}
    snapshot(snap)
    ok = True
    try:
        shutil.copy2(staged, os.path.join(ROOT, "authority", "Yemen_Financial_Inclusion_Evidence_Master.xlsx"))
        for src, dst in installs:
            os.makedirs(os.path.dirname(os.path.join(ROOT, dst)), exist_ok=True)
            shutil.copy2(src, os.path.join(ROOT, dst))
        for name, cmd in [("generate", ["python3", "scripts/generate_projections.py"]),
                          ("rebind", ["python3", "scripts/rebind_authority.py", "--timestamp", ts]),
                          ("build", ["python3", "scripts/build.py"]),
                          ("public_literal_audit", ["python3", "scripts/audit_public_literals.py"]),
                          ("architecture_diagrams", ["python3", "scripts/architecture_diagrams.py"]),   # P5: derived diagrams follow the inventory
                          ("handoff_inventory", ["python3", "scripts/handoff_inventory.py"]),           # F9: the Design recipient's route and state map follows the build
                          ("repository_manifest", ["python3", "scripts/repository_manifest.py"]),       # F5: manifest follows the new authority hashes
                          ("validate", ["python3", "scripts/validate.py"]),
                          ("generator_idempotence", ["python3", "scripts/generate_projections.py", "--check"])]:
            code, out = run(cmd)
            tail = out.strip().splitlines()[-6:]
            step = {"step": name, "exit": code, "tail": tail}
            if name == "validate" and code != 0 and allow:
                errs = [l for l in out.splitlines() if l.startswith("FAIL")]
                if errs and all(allow.search(l) for l in errs):
                    step["allowed_errors"] = errs
                    code = 0
            rep["steps"].append(step)
            if code != 0:
                ok = False
                break
    except Exception as exc:
        ok = False
        rep["exception"] = str(exc)
    if not ok:
        restore(snap)
        rep["result"] = "ROLLED_BACK"
    else:
        rep["result"] = "COMMITTED"
        rep["master_sha256"] = sha(os.path.join(ROOT, "authority", "Yemen_Financial_Inclusion_Evidence_Master.xlsx"))
        rep["page_specs_sha256"] = sha(os.path.join(ROOT, "site-src", "content", "page_specs.json"))
    json.dump(rep, open(report, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps({k: v for k, v in rep.items() if k != "steps"}, indent=1))
    for s in rep["steps"]:
        print(s["step"], s["exit"], "|", " / ".join(s["tail"][-2:])[:300])
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
