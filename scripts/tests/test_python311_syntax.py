# -*- coding: utf-8 -*-
"""Every tracked Python file must parse on the Python the CI workflow pins (3.11), not only on the newer interpreter a
local virtual environment may use.

  python3 scripts/tests/test_python311_syntax.py            (exit 0 = clean, 1 = a file needs the older syntax)
  python3 scripts/tests/test_python311_syntax.py --list     (print the files it reads)

Why this gate exists (Stage B B2, 17 October 2026). `scripts/yfie/families.py` was written with quote escapes inside
f-string expression parts — `f'{g(" a=\\"b\\"")}'`. PEP 701 made that legal in 3.12, so the local interpreter compiled
it and the full local gate set passed; the CI build, on 3.11, failed with "f-string expression part cannot include a
backslash", and every job that depends on the build was skipped. `CONTRIBUTING.md` §9 already named the rule; nothing
enforced it. Checking it with `ast.parse(..., feature_version=(3, 11))` does **not** work: that argument does not
re-impose the old f-string restrictions. So this gate reads the f-strings itself.

What it rejects, per f-string expression part (the text inside `{}`):
  1. a backslash anywhere in the part — illegal before 3.12;
  2. a nested string quoted with the same character as the enclosing f-string — illegal before 3.12.
Both are PEP 701 relaxations, and both are what a renderer that builds HTML attributes reaches for first.

The check is textual on purpose: the newest interpreter parses these files happily, so it cannot be asked whether an
older one would. Where a real 3.11 interpreter is available, `python3.11 -m compileall -q scripts site-src` is the
stronger check and this gate is a cheap stand-in for it.
"""
import io
import subprocess
import sys
import tokenize
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def tracked_python_files() -> list[Path]:
    """Every Python file Git tracks or would track, so a new file is covered before it is committed."""
    try:
        out = subprocess.run(["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
                             cwd=ROOT, capture_output=True, check=True).stdout
        names = [p for p in out.decode("utf-8").split("\0") if p.endswith(".py")]
        return sorted(ROOT / n for n in names if (ROOT / n).is_file())
    except (OSError, subprocess.CalledProcessError):
        return sorted(p for p in ROOT.rglob("*.py") if ".git" not in p.parts)


def _delimiter(text: str) -> str:
    """The quote that delimits a string or f-string token: three characters for a triple-quoted one, otherwise one.
    `f\"\"\"` is delimited by `\"\"\"`, so a single `\"` inside its expression parts is legal on 3.11; `f\"` is not."""
    if not text:
        return ""
    q = text[-1] if text[-1] in "\"'" else text.lstrip("rbfuRBFU")[:1]
    if not q:
        return ""
    return q * 3 if text.lstrip("rbfuRBFU").startswith(q * 3) else q


def offences(src: str) -> list[tuple[int, str, str]]:
    """(line, kind, excerpt) for every f-string expression part that needs 3.12. Empty when the file is 3.11-clean."""
    found: list[tuple[int, str, str]] = []
    try:
        toks = list(tokenize.generate_tokens(io.StringIO(src).readline))
    except (tokenize.TokenError, SyntaxError, IndentationError):
        return found                       # a file that does not even tokenise is the build's problem, not this gate's
    # 3.12 tokenises an f-string as FSTRING_START, literal FSTRING_MIDDLE pieces, ordinary tokens for each expression
    # part, then FSTRING_END. On 3.11 the whole f-string arrives as one STRING token, which this loop skips.
    start = getattr(tokenize, "FSTRING_START", None)
    if start is None:
        return found                       # running on 3.11 already: the interpreter itself enforces the rule
    stack: list[str] = []                  # the delimiter of each open f-string: one quote, or three
    for tok in toks:
        if tok.type == start:
            stack.append(_delimiter(tok.string))
            continue
        if tok.type == tokenize.FSTRING_END:
            if stack:
                stack.pop()
            continue
        if not stack or tok.type == tokenize.FSTRING_MIDDLE:
            continue                       # outside an f-string, or a literal piece of one: both are fine
        text = tok.string
        if "\\" in text:
            found.append((tok.start[0], "backslash in an f-string expression part", text.strip()[:70]))
        elif tok.type == tokenize.STRING and _delimiter(text.lstrip("rbfuRBFU")) == stack[-1]:
            # only the same delimiter clashes: inside f\"\"\"…\"\"\" a single \" is legal on 3.11
            found.append((tok.start[0], "nested string reuses the f-string's own delimiter", text.strip()[:70]))
    return found


def main() -> int:
    files = tracked_python_files()
    if "--list" in sys.argv:
        for f in files:
            print(f.relative_to(ROOT).as_posix())
        return 0
    bad = 0
    for f in files:
        try:
            src = f.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            print(f"PYTHON 3.11 SYNTAX: cannot read {f.relative_to(ROOT).as_posix()}: {exc}")
            bad += 1
            continue
        for line, kind, excerpt in offences(src):
            print(f"FAIL {f.relative_to(ROOT).as_posix()}:{line} {kind}: {excerpt}")
            bad += 1
    target = f"{sys.version_info.major}.{sys.version_info.minor}"
    if bad:
        print(f"PYTHON 3.11 SYNTAX: FAIL — {bad} place(s) need 3.12; CI pins 3.11 (.github/workflows/verify.yml). "
              "Hoist the fragment into a local and interpolate the local (CONTRIBUTING.md §9).")
        return 1
    if sys.version_info < (3, 12):
        # Running on the pinned interpreter: it rejects these f-strings itself, so this gate read nothing and proves
        # nothing here. `compileall` is the check that matters on this interpreter; say so rather than claim a pass.
        print(f"PYTHON 3.11 SYNTAX NOT APPLICABLE: running on {target}, which enforces the rule itself; "
              "compileall is the check on this interpreter. This gate is for a 3.12 or newer environment.")
        return 0
    print(f"PYTHON 3.11 SYNTAX PASS: {len(files)} tracked Python files hold no f-string expression part that needs 3.12 "
          f"(read on {target}, which would otherwise accept them; CI pins 3.11)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
