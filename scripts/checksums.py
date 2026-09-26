#!/usr/bin/env python3
"""SHA256SUMS.txt — the checksum manifest of this repository state.

  python3 scripts/checksums.py            # rewrite SHA256SUMS.txt from the current files
  python3 scripts/checksums.py --check    # fail if any file differs from, or is missing in, the manifest

The manifest lists every tracked file except itself, one `<sha256>  <path>` line per file, sorted by path in byte order,
the format `sha256sum -c SHA256SUMS.txt` reads. Inside a Git work tree the file set is `git ls-files`; in an extracted
checkpoint ZIP it is every file under the root except caches. Run it after any change and commit the result with it.
"""
import fnmatch
import hashlib
import os
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MANIFEST = "SHA256SUMS.txt"
SKIP_DIRS = {".git", "__pycache__", "node_modules", ".venv", "venv"}


def git_files():
    """The tracked files when ROOT is itself the top of a Git work tree; None otherwise (for example an extracted ZIP)."""
    try:
        top = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
        if os.path.realpath(top) != os.path.realpath(ROOT):
            return None
        out = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, check=True).stdout
        return [p for p in out.decode("utf-8").split("\0") if p]
    except (OSError, subprocess.CalledProcessError):
        return None


def _ignore_rules():
    """The repository's .gitignore as (anchored, directory_only, pattern) rules — the subset of Git's syntax it uses."""
    rules = []
    try:
        lines = open(os.path.join(ROOT, ".gitignore"), encoding="utf-8").read().splitlines()
    except OSError:
        return rules
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("!"):
            continue
        rules.append((line.startswith("/"), line.endswith("/"), line.strip("/")))
    return rules


def _ignored(rel, is_dir, rules):
    name = rel.rsplit("/", 1)[-1]
    for anchored, dir_only, pat in rules:
        if dir_only and not is_dir:
            continue
        if fnmatch.fnmatchcase(rel if anchored or "/" in pat else name, pat):
            return True
    return False


def tracked_files():
    """git ls-files inside a Git work tree; in an extracted archive, every file under the root that .gitignore does not
    exclude (so a locally built design/reference/out/ or a cache never enters the manifest)."""
    files = git_files()
    if files is not None:
        return files
    rules, files = _ignore_rules(), []
    for base, dirs, names in os.walk(ROOT):
        relbase = os.path.relpath(base, ROOT).replace(os.sep, "/")
        relbase = "" if relbase == "." else relbase + "/"
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not _ignored(relbase + d, True, rules)]
        for n in names:
            rel = relbase + n
            if not n.endswith(".pyc") and not _ignored(rel, False, rules):
                files.append(rel)
    return files


def manifest_text():
    lines = []
    for rel in sorted((p for p in tracked_files() if p != MANIFEST), key=lambda p: p.encode("utf-8")):
        h = hashlib.sha256()
        with open(os.path.join(ROOT, rel), "rb") as fh:
            for chunk in iter(lambda: fh.read(1 << 20), b""):
                h.update(chunk)
        lines.append(f"{h.hexdigest()}  {rel}\n")
    return "".join(lines)


def main():
    want = manifest_text()
    path = os.path.join(ROOT, MANIFEST)
    if "--check" in sys.argv[1:]:
        have = open(path, encoding="utf-8").read() if os.path.exists(path) else ""
        if have != want:
            a, b = set(have.splitlines()), set(want.splitlines())
            for ln in sorted(a - b)[:20]:
                print("  manifest:", ln)
            for ln in sorted(b - a)[:20]:
                print("  actual:  ", ln)
            print("CHECKSUM MANIFEST STALE: run python3 scripts/checksums.py and commit SHA256SUMS.txt")
            sys.exit(1)
        print(f"CHECKSUM MANIFEST CURRENT: {len(want.splitlines())} files")
        return
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(want)
    print(f"CHECKSUM MANIFEST WRITTEN: {len(want.splitlines())} files")


if __name__ == "__main__":
    main()
