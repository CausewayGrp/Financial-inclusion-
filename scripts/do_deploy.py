#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Point the DigitalOcean App Platform app at one pushed image and wait until it is live (the release route,
docs/RELEASE_RUNBOOK.md, "Hosting"; owner decision of 3 October 2026). Run by .github/workflows/deploy.yml only, after
every gate and after the image has been pushed to the DigitalOcean Container Registry.

  DIGITALOCEAN_ACCESS_TOKEN=… python3 scripts/do_deploy.py --tag <commit> [--app-id <id>]

With --app-id it replaces the app's specification with site-src/hosting/digitalocean/app_spec.json, the image tag
set to --tag, which starts a deployment, and it waits for that deployment to become ACTIVE (it fails on ERROR,
CANCELED or after 15 minutes). Without --app-id it creates the app from the same specification and prints its id, for
the owner to store as the repository variable YFIE_DO_APP_ID. Standard library only; it sends nothing but the
specification. Rollback is App Platform's own (the app's Activity tab), or a run of the workflow on an earlier commit.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
API = "https://api.digitalocean.com/v2"


def call(method: str, path: str, token: str, body: dict | None = None) -> dict:
    req = urllib.request.Request(API + path, method=method, data=json.dumps(body).encode() if body is not None else None,
                                 headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read() or b"{}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", required=True)
    ap.add_argument("--app-id", default="")
    a = ap.parse_args()
    token = os.environ.get("DIGITALOCEAN_ACCESS_TOKEN", "")
    if not token:
        sys.exit("DIGITALOCEAN_ACCESS_TOKEN is not set")
    spec = json.loads((ROOT / "site-src/hosting/digitalocean/app_spec.json").read_text(encoding="utf-8"))
    for svc in spec["services"]:
        svc["image"]["tag"] = a.tag
    if not a.app_id:
        app = call("POST", "/apps", token, {"spec": spec})["app"]
        print(f"Created the app {app['id']}: store it as the repository variable YFIE_DO_APP_ID")
        app_id = app["id"]
    else:
        app_id = a.app_id
        call("PUT", f"/apps/{app_id}", token, {"spec": spec})
    deadline = time.time() + 900
    while time.time() < deadline:
        time.sleep(15)
        deps = call("GET", f"/apps/{app_id}/deployments?per_page=1", token).get("deployments") or []
        if not deps:
            continue
        d = deps[0]
        phase = d.get("phase")
        tags = {s.get("image", {}).get("tag") for s in (d.get("spec") or {}).get("services", [])}
        print(f"deployment {d.get('id')}: {phase}")
        if a.tag in tags and phase == "ACTIVE":
            app = call("GET", f"/apps/{app_id}", token)["app"]
            print(f"LIVE: {app.get('default_ingress', '')}/financial-inclusion-evidence/ serves {a.tag}")
            return 0
        if a.tag in tags and phase in ("ERROR", "CANCELED"):
            sys.exit(f"the deployment of {a.tag} ended {phase}; the previous deployment stays live")
    sys.exit("the deployment did not become ACTIVE within 15 minutes")


if __name__ == "__main__":
    raise SystemExit(main())
