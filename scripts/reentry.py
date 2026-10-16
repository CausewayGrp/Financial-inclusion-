"""Lightweight repository re-entry inspection tool.

Provides a read-only view useful for an agent or human returning to the repository: local HEAD and branch,
working-tree cleanliness, remote-main reference (where available), basic divergence/ancestor checks (best-effort),
and a short recommended next action.

Usage:
  python3 scripts/reentry.py
  python3 scripts/reentry.py --json
  python3 scripts/reentry.py --base <commit-sha>
  python3 scripts/reentry.py --offline

Technical constraints:
 - Does not run 'git fetch' or change refs.
 - Uses 'git ls-remote' with a short timeout to read remote heads when network access is available.
 - Explicitly reports UNKNOWN for information that cannot be determined safely.
"""
from __future__ import annotations
import argparse
import json
import shutil
import subprocess
import sys
import textwrap
from datetime import datetime


def run(cmd, timeout=5):
    try:
        p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False, timeout=timeout, text=True)
        return p.returncode, p.stdout.strip(), p.stderr.strip()
    except (subprocess.SubprocessError, FileNotFoundError) as e:
        return 127, "", str(e)


def in_git_repo():
    rc, out, err = run(["git", "rev-parse", "--git-dir"])
    return rc == 0


def git_head():
    rc, out, err = run(["git", "rev-parse", "HEAD"])
    if rc != 0:
        return None
    return out


def git_branch():
    rc, out, err = run(["git", "symbolic-ref", "--quiet", "--short", "HEAD"])
    if rc != 0:
        # Detached or unknown
        rc2, out2, err2 = run(["git", "describe", "--all", "--exact-match", "HEAD"])
        return out2 or "(detached)"
    return out


def git_status_porcelain():
    rc, out, err = run(["git", "status", "--porcelain"])
    if rc != 0:
        return "UNKNOWN"
    return out


def remote_main_sha(remote_name="origin", branch_name="main"):
    # Use git ls-remote to read remote refs without fetching.
    rc, out, err = run(["git", "ls-remote", remote_name, f"refs/heads/{branch_name}"], timeout=8)
    if rc != 0 or not out:
        return None
    return out.split()[0]


def local_has_object(sha):
    if not sha:
        return False
    rc, out, err = run(["git", "cat-file", "-t", sha])
    return rc == 0


def is_ancestor(ancestor, descendant):
    if not ancestor or not descendant:
        return None
    # git merge-base --is-ancestor returns 0 if ancestor is ancestor of descendant
    rc, out, err = run(["git", "merge-base", "--is-ancestor", ancestor, descendant])
    if rc == 0:
        return True
    if rc == 1:
        return False
    return None


def recommended_next_action(state):
    # Simple heuristic
    if not state.get("in_git_repo"):
        return "Start from a clone of origin/main and run scripts/reentry.py there."
    if state.get("dirty"):
        return "Stash or commit local changes before attempting branch operations."
    remote_sha = state.get("remote_main_sha")
    head = state.get("local_head")
    if remote_sha is None:
        return "Remote main unreachable; check network or credentials."
    if remote_sha == head:
        return "Working on an up-to-date main; create an isolated branch for changes."
    # If remote is unknown locally
    if not state.get("remote_known_locally"):
        return "Remote main commit not present locally; fetch or inspect PRs before assuming ancestry."
    # Diverged
    return "Branch and remote differ; examine merge-base and consider rebase or merge per project policy."


def build_state(args):
    state = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "in_git_repo": False,
        "local_head": None,
        "branch": None,
        "dirty": None,
        "remote_main_sha": None,
        "remote_known_locally": None,
        "head_is_ancestor_of_remote": None,
        "remote_is_ancestor_of_head": None,
        "notes": [],
    }
    if not shutil.which("git"):
        state["notes"].append("git not available in PATH")
        return state
    if not in_git_repo():
        state["notes"].append("not a git repository")
        return state
    state["in_git_repo"] = True
    state["local_head"] = git_head()
    state["branch"] = git_branch()
    status = git_status_porcelain()
    state["dirty"] = bool(status) and status != "UNKNOWN"
    if args.base:
        state["provided_base"] = args.base
    # Remote inspection unless offline
    if not args.offline:
        sha = remote_main_sha()
        state["remote_main_sha"] = sha
        if sha:
            state["remote_known_locally"] = local_has_object(sha)
            if state["remote_known_locally"] and state["local_head"]:
                state["head_is_ancestor_of_remote"] = is_ancestor(state["local_head"], sha)
                state["remote_is_ancestor_of_head"] = is_ancestor(sha, state["local_head"])
        else:
            state["notes"].append("remote main not readable via ls-remote; credentials or network may be required")
    else:
        state["notes"].append("offline mode: remote checks skipped")
    state["next_step"] = recommended_next_action(state)
    return state


def main(argv=None):
    p = argparse.ArgumentParser(description="Repository re-entry inspection tool: read-only checks to resume work safely.")
    p.add_argument("--json", action="store_true", help="Output machine-readable JSON")
    p.add_argument("--base", help="A baseline commit SHA to compare against (no fetch)")
    p.add_argument("--offline", action="store_true", help="Skip remote checks (safe for offline use)")
    args = p.parse_args(argv)
    state = build_state(args)
    if args.json:
        print(json.dumps(state, ensure_ascii=False, indent=2))
        return
    # Human-readable summary
    lines = []
    lines.append(f"Timestamp: {state['timestamp']}")
    if not state.get("in_git_repo"):
        lines.append("Repository: NOT A GIT REPOSITORY (or git not available)")
        lines.extend(state.get("notes", []))
        print("\n".join(lines))
        return
    lines.append(f"Local HEAD: {state.get('local_head') or 'UNKNOWN'}")
    lines.append(f"Branch: {state.get('branch') or 'UNKNOWN'}")
    lines.append(f"Working tree: {'dirty' if state.get('dirty') else 'clean'}")
    if 'remote_main_sha' in state:
        lines.append(f"Remote main (ls-remote): {state.get('remote_main_sha') or 'UNREADABLE'}")
        if state.get('remote_main_sha') and not state.get('remote_known_locally'):
            lines.append("Note: remote main SHA not present locally; ancestry cannot be confirmed without fetch")
        if state.get('head_is_ancestor_of_remote') is True:
            lines.append("Ancestry: local HEAD is an ancestor of remote main (likely behind)")
        elif state.get('remote_is_ancestor_of_head') is True:
            lines.append("Ancestry: remote main is an ancestor of local HEAD (local commits ahead)")
    if state.get('notes'):
        lines.append("Notes:")
        lines.extend(" - " + n for n in state.get('notes'))
    lines.append("")
    lines.append("Next safe action: %s" % state.get('next_step'))
    print("\n".join(lines))


if __name__ == '__main__':
    main()
