"""Host-independent regression tests for the production path identities and text writers.

Execute the actual path expressions from the validator/inventory with both pathlib
flavours. Do not import validate.py: it intentionally runs the whole repository gate.
"""
import ast
from contextlib import redirect_stdout
import io
from pathlib import Path, PurePosixPath, PureWindowsPath
import sys
import unittest
from unittest.mock import patch
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "scripts/tests"))
import test_release_parity as parity
import handoff_inventory as inventory
import test_public_tools as public_tools


def tree(name):
    return ast.parse((ROOT / "scripts" / name).read_text(encoding="utf-8"))


class PortabilityTests(unittest.TestCase):
    def test_share_assertion_accepts_native_newlines_but_rejects_changed_content(self):
        class Page:
            context = SimpleNamespace(grant_permissions=lambda *a, **k: None)
            def __init__(self, newline, corrupt=False):
                self.newline, self.corrupt = newline, corrupt
            def add_init_script(self, *a): pass
            def goto(self, url): self.lang = url.split("/")[-4]
            def get_attribute(self, *a): return "Title\nPeriod: 2021\nPopulation: adults\nBoundary: limited"
            def click(self, *a): pass
            def wait_for_function(self, *a): pass
            def evaluate(self, script):
                if "readText" in script:
                    value = self.get_attribute().replace("2021", "2022") if self.corrupt else self.get_attribute()
                    return (value + f"\nhttp://site/{self.lang}/evidence/CLM-002/").replace("\n", self.newline)
        for newline in ("\n", "\r\n"):
            public_tools.t_share_record(Page(newline), "http://site")
            with self.assertRaises(AssertionError):
                public_tools.t_share_record(Page(newline, corrupt=True), "http://site")

    def test_validator_relative_identities(self):
        # Every string path used by the validator must have the same identity for
        # Windows-native and POSIX paths, including E2's strict-set membership.
        expressions = [n.value for n in ast.walk(tree("validate.py"))
                       if isinstance(n, ast.Assign)
                       and any(isinstance(t, ast.Name) and t.id in ("rel", "_rel") for t in n.targets)
                       and isinstance(n.value, ast.Call)
                       and ast.unparse(n.value).endswith("relative_to(DIST).as_posix()")]
        self.assertGreaterEqual(len(expressions), 8)
        for cls, root in ((PureWindowsPath, "C:/repo/dist"), (PurePosixPath, "/repo/dist")):
            for lang in ("en", "ar"):
                dist = cls(root)
                path = dist / lang / "evidence" / "VIS-FINDEX-GAPS" / "index.html"
                for expr in expressions:
                    with self.subTest(flavour=cls.__name__, lang=lang, expression=ast.unparse(expr)):
                        rel = eval(compile(ast.Expression(expr), "validate.py", "eval"),
                                   {"DIST": dist, "f": path, "_f": path})
                        self.assertEqual(rel, f"{lang}/evidence/VIS-FINDEX-GAPS/index.html")
                        self.assertTrue(rel.startswith(("en/", "ar/")))
                        self.assertEqual("ar" if rel.startswith("ar/") else "en", lang)
                        self.assertEqual("/en/" in "/" + rel, lang == "en")
                        self.assertIn(rel, {f"{lang}/evidence/VIS-FINDEX-GAPS/index.html"})

    def test_inventory_identity_and_strict_classification(self):
        expr = next(n.value for n in ast.walk(tree("handoff_inventory.py"))
                    if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "have" for t in n.targets))
        for cls, root in ((PureWindowsPath, "C:/repo/content"), (PurePosixPath, "/repo/content")):
            class Content:
                def __init__(self, paths):
                    self.paths = paths
                def rglob(self, pattern):
                    return self.paths
            base = cls(root)
            def canonical(keys):
                paths = [base / k for k in keys]
                # relative_to accepts the original root; only rglob is supplied by the fake.
                expression = ast.unparse(expr).replace("C.rglob", "content.rglob")
                return eval(expression, {"C": base, "content": Content(paths)})
            have = canonical(inventory.PROJECTION_ROLES)
            self.assertEqual(have, sorted(inventory.PROJECTION_ROLES))
            unknown = canonical(["content/unclassified.json"])
            self.assertEqual([p for p in unknown if p not in inventory.PROJECTION_ROLES],
                             ["content/unclassified.json"])
            missing = canonical(k for k in inventory.PROJECTION_ROLES if k != "content/interface_copy.json")
            self.assertEqual([p for p in inventory.PROJECTION_ROLES if p not in missing],
                             ["content/interface_copy.json"])

    def test_parity_policy_never_accepts_real_failures(self):
        for content_rc, cutover_rc, expected in ((0, 0, 0), (0, 2, 0), (0, 1, 1), (0, 3, 3), (1, 2, 1)):
            with self.subTest(content=content_rc, cutover=cutover_rc):
                with patch.object(parity.content, "main", return_value=content_rc), patch.object(parity.cutover, "main", return_value=cutover_rc) as cutover:
                    with redirect_stdout(io.StringIO()):
                        self.assertEqual(parity.main(), expected)
                    if content_rc:
                        cutover.assert_not_called()

    def test_reference_binding_shipped_paths(self):
        parsed = ast.parse((ROOT / "design/reference/check_binding.py").read_text(encoding="utf-8"))
        expr = next(n.value for n in ast.walk(parsed) if isinstance(n, ast.Assign)
                    and any(isinstance(t, ast.Name) and t.id == "shipped" for t in n.targets))
        for cls, root in ((PureWindowsPath, "C:/site"), (PurePosixPath, "/site")):
            class Site:
                def rglob(self, pattern):
                    return [cls(root) / p for p in ("static-data/search_index.json", "_bundle/en.json", "extra.json")]
            expression = ast.unparse(expr).replace("site.rglob", "files.rglob")
            shipped = eval(expression, {"site": cls(root), "files": Site()})
            self.assertEqual(shipped, ["extra.json", "static-data/search_index.json"])
            self.assertEqual(set(shipped) - {"static-data/search_index.json"}, {"extra.json"})

    def test_generated_text_writers_explicitly_disable_native_newlines(self):
        files = ("build.py", "yfie/render.py", "audit_public_literals.py", "base_path.py",
                 "handoff_inventory.py", "repository_manifest.py", "logo_derivatives.py",
                 "social_images.py", "exports.py")
        count = 0
        for name in files:
            for call in ast.walk(tree(name)):
                if isinstance(call, ast.Call) and isinstance(call.func, ast.Attribute) and call.func.attr == "write_text":
                    count += 1
                    with self.subTest(file=name, line=call.lineno):
                        keywords = {kw.arg: kw.value for kw in call.keywords}
                        self.assertIn("newline", keywords)
                        self.assertEqual(ast.literal_eval(keywords["newline"]), "\n")
        self.assertGreaterEqual(count, 16)


if __name__ == "__main__":
    unittest.main()
