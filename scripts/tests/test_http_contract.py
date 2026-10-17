#!/usr/bin/env python3
"""Portable response acceptance, no hosting account, DNS or external origin.

Reuses the base-path server and the full security-header browser acceptance.
The negative control strips a required response header and must be rejected.
"""
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request
from pathlib import Path

import test_base_path as base


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def response(url):
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())
    try:
        r = opener.open(url, timeout=10)
    except urllib.error.HTTPError as error:
        r = error
    with r:
        return r.status, {k.lower(): v for k, v in r.headers.items()}


def inspect(port, site):
    host = f"http://127.0.0.1:{port}"
    rules = base.HEADERS.parse_headers((site.root / "_headers").read_text())
    paths = [site.base + "/", site.base + "/en/", site.base + "/ar/",
             site.base + "/en/payments/", site.base + "/404.html",
             site.base + "/assets/app.js", site.base + "/assets/yfie.css",
             site.base + "/assets/fonts/ibm-plex-sans/IBMPlexSans-Regular.woff2",
             site.base + "/assets/logo/CauseWay_logo_32.png",
             site.base + "/static-data/search_index.json", site.base + "/robots.txt",
             site.base + "/sitemap.xml", site.base + "/en/missing/"]
    errors = []
    for path in paths:
        status, headers = response(host + path)
        expected_status = 404 if path.endswith("/missing/") else 200
        if status != expected_status:
            errors.append(f"{path}: status {status}")
        if "/" in headers.get("server", ""):
            errors.append(f"{path}: server version disclosed")
        for key in base.HEADERS.SECURITY:
            if key.lower() not in headers:
                errors.append(f"{path}: missing {key}")
        for key in base.HEADERS.NEVER:
            if key in headers:
                errors.append(f"{path}: forbidden {key}")
        expected_cache = base.HEADERS.headers_for(rules, path).get("Cache-Control")
        if headers.get("cache-control") != expected_cache:
            errors.append(f"{path}: cache mismatch")
        if path.endswith(".xml") and headers.get("content-type") != "application/xml":
            errors.append("sitemap MIME mismatch")
    status, headers = response(host + site.base)
    if status not in (301, 308) or headers.get("location") != site.base + "/":
        errors.append("bare path must redirect once with a relative Location")
    status, headers = response(host + site.base + "/en/payments")
    if status != 301 or headers.get("location") != site.base + "/en/payments/":
        errors.append("directory path must redirect with a relative Location")
    if response(host + "/outside/")[0] != 404:
        errors.append("outside path must be 404")
    return errors


def main():
    with tempfile.TemporaryDirectory(prefix="yfie-http-") as directory:
        root = Path(directory) / "site"
        subprocess.run([sys.executable, str(base.ROOT / "scripts/build.py"), "--origin", base.ORIGIN,
                        "--out", str(root)], check=True)
        site = base.Site(root, base.ORIGIN)
        server = base.serve(site)
        try:
            port = server.server_address[1]
            errors = inspect(port, site)
            run = subprocess.run([sys.executable, str(base.ROOT / "scripts/tests/test_security_headers.py"),
                                  "--base", f"http://127.0.0.1:{port}{site.base}"], check=False)
            if errors or run.returncode:
                raise AssertionError(errors or "full header browser acceptance failed")
        finally:
            server.shutdown()
            server.server_close()
        header_path = root / "_headers"
        header_path.write_text("\n".join(line for line in header_path.read_text().splitlines()
                                         if "X-Frame-Options:" not in line) + "\n")
        server = base.serve(site)
        try:
            faults = inspect(server.server_address[1], site)
            assert any("missing X-Frame-Options" in error for error in faults), faults
        finally:
            server.shutdown()
            server.server_close()
    print("PORTABLE HTTP CONTRACT PASS: full browser sweep; missing-header negative control caught")


if __name__ == "__main__":
    main()
