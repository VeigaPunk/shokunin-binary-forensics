#!/usr/bin/env python3
"""Identity oracle for the browser-r77 fixture and its saved inspect_web_page record.

Usage:
    python -B oracle_check.py truth.json <record.json>

The fixture files (index.html, app.js) are read from this script's directory.
Every oracle run first re-verifies the fixture bytes against truth.json (Q06:
premises come from the built bytes, never intent), then checks the saved
producer record's identity fields against expectations derived from those same
bytes (Q03: independent derivation). Volatile fields listed in
truth.json .volatile_not_compared are never compared.

Prints one line per check and a final verdict line:
    ORACLE OK (n/n checks)   -> exit 0
    ORACLE FAIL (k/n checks) -> exit 1 (each failing check printed)
"""
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def fail(msg):
    print("check FAIL: " + msg)
    return False


def ok(msg):
    print("check ok: " + msg)
    return True


def main(argv):
    if len(argv) != 3:
        print(__doc__)
        return 64
    truth = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
    record = json.loads(Path(argv[2]).read_text(encoding="utf-8"))

    index_bytes = (HERE / "index.html").read_bytes()
    app_bytes = (HERE / "app.js").read_bytes()
    index_text = index_bytes.decode("utf-8")

    checks = []

    # --- premise leg: fixture bytes vs truth (Q06) ---
    for name, blob in (("index.html", index_bytes), ("app.js", app_bytes)):
        want = truth["files"][name]
        good = (
            hashlib.sha256(blob).hexdigest() == want["sha256"]
            and len(blob) == want["byte_length"]
        )
        checks.append(
            ok(f"fixture {name} sha256+len match truth.json")
            if good
            else fail(f"fixture {name} bytes do not match truth.json")
        )

    # --- authored anchors derived from the fixture bytes (Q03) ---
    m_title = re.search(r"<title>(.*?)</title>", index_text, re.S)
    scripts = re.findall(r"<script([^>]*)>(.*?)</script>", index_text, re.S)
    inline_bodies = [body for attrs, body in scripts if "src=" not in attrs]
    external_srcs = [
        re.search(r'src="([^"]+)"', attrs).group(1)
        for attrs, body in scripts
        if "src=" in attrs
    ]
    if m_title and len(inline_bodies) == 1 and len(external_srcs) == 1:
        static_title = m_title.group(1)
        suffix_m = re.search(r'"([^"]*)"', inline_bodies[0])
        inline_len = len(inline_bodies[0])
        if suffix_m:
            expected_title = static_title + suffix_m.group(1)
            checks.append(ok("authored anchors derived from index.html bytes"))
        else:
            expected_title = None
            checks.append(fail("no string literal in inline script"))
    else:
        expected_title = None
        inline_len = -1
        checks.append(
            fail("index.html does not show exactly one inline + one external script")
        )
    app_len = len(app_bytes)
    app_rel = "/" + truth["authored"]["external_script_path"].lstrip("/")

    n = record.get("normalized_result") or {}
    target = n.get("target") or {}

    # --- record identity vs producer expectations ---
    checks.append(
        ok(f"operation == {truth['producer_expected']['operation']}")
        if record.get("operation") == truth["producer_expected"]["operation"]
        else fail(f"operation {record.get('operation')!r}")
    )
    checks.append(
        ok("provider.id == rea-cdp-browser")
        if (record.get("provider") or {}).get("id") == truth["producer_expected"]["provider_id"]
        else fail("provider.id mismatch")
    )
    checks.append(
        ok("evidence_id shape ev_<64hex>")
        if re.fullmatch(r"ev_[0-9a-f]{64}", record.get("evidence_id") or "")
        else fail("evidence_id shape")
    )
    checks.append(
        ok(f"target.url == {truth['run_pin']['page_url']}")
        if target.get("url") == truth["run_pin"]["page_url"]
        else fail(f"target.url {target.get('url')!r}")
    )
    checks.append(
        ok(f"target.origin == {truth['run_pin']['http_origin']}")
        if target.get("origin") == truth["run_pin"]["http_origin"]
        else fail(f"target.origin {target.get('origin')!r}")
    )
    checks.append(
        ok(f"target.title == derived {expected_title!r}")
        if expected_title is not None and target.get("title") == expected_title
        else fail(f"target.title {target.get('title')!r} != derived expectation")
    )
    frames = n.get("frames") or []
    checks.append(
        ok("target.type page and frames[0].url == page_url")
        if target.get("type") == truth["producer_expected"]["target_type"]
        and frames
        and frames[0].get("url") == truth["run_pin"]["page_url"]
        else fail("target.type/frames[0].url")
    )

    dom_urls = [u for u in (n.get("metadata") or {}).get("dom_urls", [])]
    checks.append(
        ok("metadata.dom_urls == exactly the app.js src")
        if len(dom_urls) == 1
        and dom_urls[0].get("url") == truth["run_pin"]["http_origin"] + app_rel
        and dom_urls[0].get("attribute") == "src"
        else fail(f"metadata.dom_urls {dom_urls!r}")
    )

    items = (n.get("scripts") or {}).get("items") or []
    urls = {i.get("url") for i in items}
    checks.append(
        ok("scripts.items count == 2 with page + app.js urls")
        if len(items) == truth["producer_expected"]["script_count"]
        and urls == {truth["run_pin"]["page_url"], truth["run_pin"]["http_origin"] + app_rel}
        else fail(f"scripts items/urls {sorted(urls)!r}")
    )
    app_item = next((i for i in items if (i.get("url") or "").endswith(app_rel)), None)
    checks.append(
        ok(f"app.js script length == {app_len} and reconciliation exact")
        if app_item
        and app_item.get("length") == app_len
        and (app_item.get("resource_reconciliation") or {}).get("status") == "exact"
        else fail("app.js script length/reconciliation")
    )
    inline_item = next(
        (i for i in items if (i.get("url") or "") == truth["run_pin"]["page_url"]), None
    )
    checks.append(
        ok(f"inline script length == {inline_len} (from index.html bytes)")
        if inline_item and expected_title is not None and inline_item.get("length") == inline_len
        else fail("inline script length")
    )
    checks.append(
        ok("app.js cdp_hash == sha256(committed app.js bytes)")
        if app_item and app_item.get("cdp_hash") == hashlib.sha256(app_bytes).hexdigest()
        else fail("app.js cdp_hash binding")
    )
    checks.append(
        ok("inline script cdp_hash == sha256(inline text from index.html bytes)")
        if inline_item
        and len(inline_bodies) == 1
        and inline_item.get("cdp_hash")
        == hashlib.sha256(inline_bodies[0].encode("utf-8")).hexdigest()
        else fail("inline script cdp_hash binding")
    )

    resources = n.get("resources") or []
    checks.append(
        ok(
            "resources == 1 app.js entry, content_size %d, %s"
            % (app_len, truth["producer_expected"]["resource_mime"])
        )
        if len(resources) == truth["producer_expected"]["resource_count"]
        and resources
        and resources[0].get("url", "").endswith(app_rel)
        and resources[0].get("content_size") == app_len
        and resources[0].get("mime_type") == truth["producer_expected"]["resource_mime"]
        else fail(f"resources {resources!r}")
    )

    passed = sum(1 for c in checks if c is True)
    total = len(checks)
    if passed == total:
        print(f"ORACLE OK ({total}/{total} checks)")
        return 0
    print(f"ORACLE FAIL ({passed}/{total} checks)")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
