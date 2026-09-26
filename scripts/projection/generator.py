# -*- coding: utf-8 -*-
"""Canonical Master -> projection generator.

  python3 scripts/generate_projections.py                 # regenerate site-src/content in place
  python3 scripts/generate_projections.py --out DIR       # write to another directory (baseline tests)
  python3 scripts/generate_projections.py --check         # regenerate in memory; exit 1 on any difference

Outputs, their owning sheets, rules and dependencies are declared in projection_manifest.json.
Nothing is skipped silently: an unknown structure, a missing controlled input, a dangling stable ID
or an undeclared output raises GenerationError.
"""
import hashlib
import json
import os
from collections import OrderedDict

from .master_reader import Workbook
from .structure import StructureError
from . import families as F
from . import derived as D

HERE = os.path.dirname(os.path.abspath(__file__))


class GenerationError(Exception):
    pass


def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh, object_pairs_hook=OrderedDict)


def serialize(obj, trailing_newline):
    return json.dumps(obj, ensure_ascii=False, indent=2) + ("\n" if trailing_newline else "")


class Context:
    """Everything a family builder may read: the Master, the structure contract and controlled inputs."""

    def __init__(self, master_path, repo_root):
        self.repo = repo_root
        self.wb = Workbook(master_path)
        self.contract = load_json(os.path.join(HERE, "master_structure.json"))
        F.validate_structure(self.wb, self.contract)
        self.manifest = load_json(os.path.join(HERE, "projection_manifest.json"))
        self.inputs = {}
        for key, rel in self.manifest["controlled_inputs"].items():
            p = os.path.join(repo_root, rel["path"])
            if not os.path.exists(p):
                raise GenerationError(f"controlled input missing: {rel['path']}")
            self.inputs[key] = load_json(p)
        self.out = OrderedDict()   # path -> python object (filled in dependency order)

    @property
    def master_sha256(self):
        return self.wb.sha256


def build_all(ctx):
    order = ctx.manifest["outputs"]
    for entry in order:
        path = entry["path"]
        kind = entry["kind"]
        rule = entry["rule_id"]
        fn = getattr(D, rule, None) or getattr(F, rule, None)
        if fn is None:
            raise GenerationError(f"{path}: no builder for rule {rule!r}")
        obj = fn(ctx, entry)
        if obj is None:
            raise GenerationError(f"{path}: builder {rule} returned nothing")
        ctx.out[path] = obj
    return ctx.out


def generate(master_path, repo_root, out_dir=None, check=False):
    ctx = Context(master_path, repo_root)
    build_all(ctx)
    content_root = os.path.join(repo_root, "site-src", "content")
    target = out_dir or content_root
    diffs, written = [], []
    for entry in ctx.manifest["outputs"]:
        text = serialize(ctx.out[entry["path"]], entry.get("trailing_newline", True))
        dest = os.path.join(target, entry["path"])
        if check:
            cur = None
            if os.path.exists(os.path.join(content_root, entry["path"])):
                with open(os.path.join(content_root, entry["path"]), encoding="utf-8") as fh:
                    cur = fh.read()
            if cur != text:
                diffs.append(entry["path"])
            continue
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        written.append(entry["path"])
    report = OrderedDict([
        ("generator", ctx.manifest["generator"]),
        ("master_sha256", ctx.master_sha256),
        ("outputs", len(ctx.manifest["outputs"])),
        ("written" if not check else "differences", written if not check else diffs),
        ("output_sha256", OrderedDict((e["path"], hashlib.sha256(serialize(ctx.out[e["path"]], e.get("trailing_newline", True)).encode("utf-8")).hexdigest()) for e in ctx.manifest["outputs"])),
    ])
    return report
