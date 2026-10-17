"""Regression tests for the read-only agent re-entry tool.

Run with python3 scripts/tests/test_reentry.py (standard-library unittest).
Synthetic repositories use local bare remotes: no network, no production writes.
"""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

TOOL = Path(__file__).resolve().parents[1] / "reentry.py"
spec = importlib.util.spec_from_file_location("yfie_reentry", TOOL)
reentry = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reentry)


def git(repo: Path, *args: str, check=True) -> str:
    p = subprocess.run(["git", *args], cwd=repo, capture_output=True, text=True)
    if check and p.returncode:
        raise AssertionError(f"git {args}: {p.stderr}")
    return p.stdout.strip()


class ReentryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.bare = self.root / "remote.git"
        git(self.root, "init", "--bare", "--initial-branch=main", str(self.bare))
        self.repo = self.root / "checkout"
        git(self.root, "clone", str(self.bare), str(self.repo))
        git(self.repo, "config", "user.name", "Fixture Tester")
        git(self.repo, "config", "user.email", "fixture@example.invalid")
        (self.repo / "README.md").write_text("initial\n", encoding="utf-8")
        git(self.repo, "add", "README.md")
        git(self.repo, "commit", "-m", "initial")
        git(self.repo, "push", "-u", "origin", "main")
        self.initial = git(self.repo, "rev-parse", "HEAD")

    def add_commit(self, filename="change.txt", content="changed\n"):
        (self.repo / filename).write_text(content, encoding="utf-8")
        git(self.repo, "add", filename)
        git(self.repo, "commit", "-m", "test change")
        return git(self.repo, "rev-parse", "HEAD")

    def test_clean_main_and_no_mutation(self):
        before = git(self.repo, "show-ref")
        report = reentry.inspect(self.repo)
        after = git(self.repo, "show-ref")
        self.assertEqual(before, after)
        self.assertEqual(report["worktree"], "CLEAN")
        self.assertEqual(report["main_comparison"]["state"], "IDENTICAL")
        self.assertEqual(report["remote_main"]["source"], "LIVE_REMOTE")
        self.assertEqual(report["authority_status"], "NOT_ASSESSED")

    def test_dirty_untracked_is_preserved(self):
        (self.repo / "untracked.txt").write_text("important data", encoding="utf-8")
        report = reentry.inspect(self.repo, offline=True)
        self.assertEqual(report["worktree"], "DIRTY")
        self.assertIn("Preserve", report["next_action"])
        self.assertEqual((self.repo / "untracked.txt").read_text(), "important data")

    def test_ahead_and_task_base_changes(self):
        git(self.repo, "switch", "-c", "feature")
        new = self.add_commit()
        report = reentry.inspect(self.repo, base=self.initial)
        self.assertEqual(report["head"], new)
        self.assertEqual(report["base"]["comparison"]["state"], "AHEAD")
        self.assertEqual(report["base"]["comparison"]["ahead"], 1)
        self.assertEqual(report["base"]["comparison"]["changed_files"], ["change.txt"])
        self.assertEqual(report["main_comparison"]["state"], "AHEAD")

    def test_old_feature_branch_behind_main(self):
        git(self.repo, "switch", "-c", "feature")
        git(self.repo, "switch", "main")
        self.add_commit()
        git(self.repo, "push", "origin", "main")
        git(self.repo, "switch", "feature")
        report = reentry.inspect(self.repo)
        self.assertEqual(report["main_comparison"]["state"], "BEHIND")
        self.assertIn("Main advanced", report["next_action"])

    def test_divergence(self):
        git(self.repo, "switch", "-c", "feature")
        self.add_commit("feature.txt")
        git(self.repo, "switch", "main")
        self.add_commit("main.txt")
        git(self.repo, "push", "origin", "main")
        git(self.repo, "switch", "feature")
        report = reentry.inspect(self.repo)
        self.assertEqual(report["main_comparison"]["state"], "DIVERGED")

    def test_already_integrated_by_ancestry(self):
        git(self.repo, "switch", "-c", "feature")
        old = self.add_commit()
        git(self.repo, "switch", "main")
        git(self.repo, "merge", "--ff-only", "feature")
        git(self.repo, "push", "origin", "main")
        git(self.repo, "switch", "feature")
        report = reentry.inspect(self.repo, base=self.initial)
        self.assertEqual(report["main_comparison"]["state"], "IDENTICAL")
        self.assertEqual(report["head"], old)
        self.assertEqual(report["pr"]["state"], "NOT_CHECKED")

    def test_offline_uses_explicitly_unverified_tracking_ref(self):
        report = reentry.inspect(self.repo, offline=True)
        self.assertEqual(report["remote_main"]["source"], "CACHED_UNVERIFIED")
        self.assertEqual(report["pr"]["state"], "NOT_CHECKED")

    def test_missing_base_unknown_not_complete(self):
        report = reentry.inspect(self.repo, base="f" * 40, offline=True)
        self.assertEqual(report["base"]["comparison"]["state"], "UNKNOWN")
        self.assertIn("Verify task baseline", report["next_action"])

    def test_reject_non_sha_base(self):
        report = reentry.inspect(self.repo, base="--help", offline=True)
        self.assertEqual(report["base"]["comparison"]["state"], "INVALID_BASE")

    def test_git_status_failure_stays_unknown(self):
        actual = reentry.git
        def fake_git(repo, *args, **kwargs):
            if args and args[0] == "status":
                return (128, "")
            return actual(repo, *args, **kwargs)
        with patch.object(reentry, "git", side_effect=fake_git):
            report = reentry.inspect(self.repo, offline=True)
        self.assertEqual(report["worktree"], "UNKNOWN")
        self.assertIn("stop", report["next_action"])

    def test_unavailable_remote_not_assumed_current(self):
        git(self.repo, "remote", "set-url", "origin", str(self.root / "missing.git"))
        report = reentry.inspect(self.repo)
        self.assertEqual(report["remote_main"]["source"], "CACHED_UNVERIFIED")
        self.assertNotEqual(report["remote_main"]["source"], "LIVE_REMOTE")

    def test_cached_state_cannot_be_called_live(self):
        git(self.repo, "remote", "set-url", "origin", str(self.root / "missing.git"))
        report = reentry.inspect(self.repo)
        self.assertEqual(report["remote_main"]["source"], "CACHED_UNVERIFIED")
        self.assertIn("unverified", report["next_action"])

    def test_divergence_lists_changes_from_both_tips(self):
        git(self.repo, "switch", "-c", "feature")
        self.add_commit("feature.txt")
        git(self.repo, "switch", "main")
        self.add_commit("main.txt")
        git(self.repo, "push", "origin", "main")
        git(self.repo, "switch", "feature")
        report = reentry.inspect(self.repo)
        self.assertEqual(report["main_comparison"]["state"], "DIVERGED")
        self.assertEqual(set(report["main_comparison"]["changed_files"]), {"feature.txt", "main.txt"})

    def test_detached_head(self):
        git(self.repo, "checkout", "--detach", "HEAD")
        report = reentry.inspect(self.repo, offline=True)
        self.assertEqual(report["branch"], "DETACHED")
        self.assertIn("authorized branch", report["next_action"])

    def test_no_git_repo_and_cli_json(self):
        report = reentry.inspect(self.root, offline=True)
        self.assertEqual(report["repository"], "NOT_A_GIT_REPOSITORY")
        p = subprocess.run([sys.executable, str(TOOL), "--repo", str(self.repo), "--offline", "--json"],
                           capture_output=True, text=True, timeout=10)
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertEqual(json.loads(p.stdout)["worktree"], "CLEAN")


if __name__ == "__main__":
    unittest.main()
