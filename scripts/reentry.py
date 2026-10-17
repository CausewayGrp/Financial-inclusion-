#!/usr/bin/env python3
"""Read-only Git re-entry report for humans and AI agents.

Run from anywhere: python3 scripts/reentry.py [--json] [--offline] [--base SHA] [--pr]
For synthetic tests: --repo PATH. Never fetches, checks out, changes refs or writes files.
Repository information is separate from the Production Master's programme authority.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GUIDANCE = ("README.md", "AGENTS.md", "CONTRIBUTING.md",
            "authority/CORE_CONSTITUTION.md", "authority/YFI_CURRENT_PROJECT_CONTEXT.json",
            "audit/close_out/STAGE_B_DESIGN_CHARTER_v3_2.md", "audit/OWNER_DECISIONS_2026-10-17.md",
            "audit/close_out/TAKEOVER_BRIEF_2026-10-17.md")
_SHA = re.compile(r"[0-9a-fA-F]{7,64}\Z")


def git(repo: Path, *args: str, timeout: int = 5) -> tuple[int | None, str]:
    """Return status/stdout; no stderr disclosure (remote errors can contain credentials)."""
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0", GCM_INTERACTIVE="never", GIT_OPTIONAL_LOCKS="0")
    try:
        p = subprocess.run(["git", *args], cwd=repo, env=env, capture_output=True,
                           encoding="utf-8", errors="replace", timeout=timeout, check=False)
        return p.returncode, p.stdout.strip()
    except (OSError, subprocess.TimeoutExpired):
        return None, ""


def commit(repo: Path, rev: str) -> str | None:
    code, out = git(repo, "rev-parse", "--verify", f"{rev}^{{commit}}")
    return out if code == 0 and _SHA.fullmatch(out) else None


def comparison(repo: Path, older: str | None, current: str | None) -> dict:
    result: dict = {"state": "UNKNOWN", "ahead": None, "behind": None, "changed_files": []}
    if not older or not current:
        return result
    code, counts = git(repo, "rev-list", "--left-right", "--count", f"{older}...{current}")
    if code != 0:
        return result
    try:
        behind, ahead = map(int, counts.split())
    except (TypeError, ValueError):
        return result
    result.update(ahead=ahead, behind=behind,
                  state="IDENTICAL" if ahead == behind == 0 else
                        "AHEAD" if behind == 0 else "BEHIND" if ahead == 0 else "DIVERGED")
    # Use two tips, not a triple-dot diff; suppress rename guessing so both paths survive.
    code, changed = git(repo, "diff", "--no-renames", "--name-only", "--no-ext-diff", older, current)
    if code == 0:
        result["changed_files"] = changed.splitlines() if changed else []
    return result


def pr_info(repo: Path, offline: bool, enabled: bool) -> dict:
    if offline or not enabled:
        return {"state": "NOT_CHECKED", "reason": "offline" if offline else "use --pr to query GitHub CLI"}
    if shutil.which("gh") is None:
        return {"state": "UNKNOWN", "reason": "GitHub CLI unavailable"}
    try:
        p = subprocess.run(["gh", "pr", "view", "--json", "number,url,state,isDraft,mergedAt,headRefOid,statusCheckRollup"],
                           cwd=repo, capture_output=True, text=True, timeout=8, check=False,
                           env=dict(os.environ, GH_PROMPT_DISABLED="1", GIT_TERMINAL_PROMPT="0"))
        if p.returncode:
            return {"state": "UNKNOWN", "reason": "No accessible PR or GitHub authentication unavailable"}
        obj = json.loads(p.stdout)
        checks = obj.get("statusCheckRollup") or []
        return {"state": obj.get("state") or "UNKNOWN", "number": obj.get("number"),
                "url": obj.get("url"), "draft": obj.get("isDraft"),
                "merged_at": obj.get("mergedAt"), "head_sha": obj.get("headRefOid"),
                "checks": [{"name": x.get("name") or x.get("context"),
                            "result": x.get("conclusion") or x.get("state") or "UNKNOWN"} for x in checks]}
    except (OSError, subprocess.TimeoutExpired, json.JSONDecodeError, TypeError):
        return {"state": "UNKNOWN", "reason": "GitHub PR lookup failed"}


def inspect(repo: Path, *, base: str | None = None, offline: bool = False, check_pr: bool = False) -> dict:
    info: dict = {"schema": "YFIE_REENTRY/1.0", "observed_at": datetime.now(timezone.utc).isoformat(),
                  "repository": "UNKNOWN", "branch": "UNKNOWN", "head": None,
                  "worktree": "UNKNOWN", "remote_main": {"sha": None, "source": "UNKNOWN"},
                  "base": {"requested": base, "resolved": None, "comparison": None},
                  "main_comparison": None, "pr": {"state": "NOT_CHECKED"},
                  "guidance": list(GUIDANCE), "authority_status": "NOT_ASSESSED", "next_action": "UNKNOWN"}
    if shutil.which("git") is None:
        info["next_action"] = "Git unavailable: use a repository-connected environment."
        return info
    c, inside = git(repo, "rev-parse", "--show-toplevel")
    if c != 0:
        info["repository"] = "NOT_A_GIT_REPOSITORY"
        info["next_action"] = "Select a Git checkout before inspecting task state."
        return info
    info["repository"] = "GIT"
    c, head = git(repo, "rev-parse", "--verify", "HEAD")
    if c == 0 and _SHA.fullmatch(head):
        info["head"] = head
    c, branch = git(repo, "symbolic-ref", "--quiet", "--short", "HEAD")
    if c == 0:
        info["branch"] = branch
    elif c == 1 and info["head"]:
        info["branch"] = "DETACHED"
    c, status = git(repo, "status", "--porcelain=v1", "--untracked-files=normal")
    if c == 0:
        info["worktree"] = "DIRTY" if status else "CLEAN"
    if base is not None:
        if _SHA.fullmatch(base):
            resolved = commit(repo, base)
            info["base"]["resolved"] = resolved
            info["base"]["comparison"] = comparison(repo, resolved, info["head"])
        else:
            info["base"]["comparison"] = {"state": "INVALID_BASE"}
    if offline:
        cached = commit(repo, "refs/remotes/origin/main")
        info["remote_main"] = {"sha": cached, "source": "CACHED_UNVERIFIED" if cached else "UNKNOWN_OFFLINE"}
    else:
        rc, value = git(repo, "ls-remote", "--heads", "origin", "refs/heads/main", timeout=6)
        sha = value.split()[0] if rc == 0 and value else None
        if sha and _SHA.fullmatch(sha):
            info["remote_main"] = {"sha": sha, "source": "LIVE_REMOTE"}
        else:
            cached = commit(repo, "refs/remotes/origin/main")
            info["remote_main"] = {"sha": cached, "source": "CACHED_UNVERIFIED" if cached else "UNKNOWN"}
    live_or_cached = info["remote_main"]["sha"]
    if live_or_cached:
        known = commit(repo, live_or_cached)
        info["main_comparison"] = comparison(repo, known, info["head"])
        if not known:
            info["main_comparison"]["reason"] = "Remote commit object unavailable locally; explicit fetch required."
    info["pr"] = pr_info(repo, offline=offline, enabled=check_pr)
    if info["worktree"] == "UNKNOWN":
        info["next_action"] = "Git status unknown: stop before modifying branch or worktree."
    elif info["worktree"] == "DIRTY":
        info["next_action"] = "Preserve and inspect uncommitted changes; never stash or reset automatically."
    elif info["branch"] in ("DETACHED", "UNKNOWN"):
        info["next_action"] = "HEAD is detached or branch unknown: inspect and select an authorized branch before writing."
    elif base is not None and info["base"]["comparison"]["state"] in ("INVALID_BASE", "UNKNOWN"):
        info["next_action"] = "Verify task baseline or fetch missing Git objects; do not infer completed work."
    elif info["remote_main"]["source"] != "LIVE_REMOTE":
        info["next_action"] = "Main is cached/unverified: confirm live GitHub state before modifying this branch."
    elif info["main_comparison"] is None or info["main_comparison"]["state"] == "UNKNOWN":
        info["next_action"] = "Explicitly fetch missing Git objects before assuming branch state."
    elif info["main_comparison"]["state"] == "IDENTICAL":
        info["next_action"] = "No branch difference against inspected main; check PR and task scope before editing."
    elif info["main_comparison"]["state"] == "BEHIND":
        info["next_action"] = "Main advanced; inspect changes and reconcile before writing."
    elif info["main_comparison"]["state"] == "AHEAD":
        info["next_action"] = "Local commits are ahead of inspected main; inspect existing PR/CI before continuing."
    else:
        info["next_action"] = "Branch diverged; compare with main and resolve deliberately before changes."
    return info


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=ROOT, help="Git checkout (primarily for fixture testing)")
    parser.add_argument("--json", action="store_true", help="Machine-readable JSON")
    parser.add_argument("--base", help="Explicit prior task commit SHA; never guessed")
    parser.add_argument("--offline", action="store_true", help="Skip all network access")
    parser.add_argument("--pr", action="store_true", help="Query PR and checks using GitHub CLI if connected")
    args = parser.parse_args(argv)
    info = inspect(args.repo.resolve(), base=args.base, offline=args.offline, check_pr=args.pr)
    if args.json:
        print(json.dumps(info, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        print(f"Repository: {info['repository']} | Branch: {info['branch']} | HEAD: {info['head'] or 'UNKNOWN'}")
        print(f"Worktree: {info['worktree']} | main: {info['remote_main']['sha'] or 'UNKNOWN'} ({info['remote_main']['source']})")
        if info['base']['comparison']:
            print(f"Task baseline: {info['base']['comparison']['state']} | ahead={info['base']['comparison'].get('ahead')} behind={info['base']['comparison'].get('behind')}")
        if info['main_comparison']:
            print(f"Against inspected main: {info['main_comparison']['state']} | changed files: {len(info['main_comparison']['changed_files'])}")
        print(f"PR: {info['pr']['state']} | Next: {info['next_action']}")
        print("Programme/owner authorization: NOT_ASSESSED — consult Master, Context and dated decisions.")
    return 0 if info["repository"] == "GIT" and info["head"] is not None else 2


if __name__ == "__main__":
    sys.exit(main())
