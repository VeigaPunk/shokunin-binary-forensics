#!/usr/bin/env python3
"""Extra (non-frozen) probes derived from battery P1, my own labels by the
battery docstring rule (reject = record misstates the fixture's manifest/identity).
Writes cases to argv[1]; prints id + my intended label."""
import copy
import json
import sys
from pathlib import Path

P1 = Path("/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-90/oracle-battery-cases/P1-real-r89-record.json")
out = Path(sys.argv[1])
out.mkdir(parents=True, exist_ok=True)
rec = json.loads(P1.read_text(encoding="utf-8"))
GOOD = rec["normalized_result"]["manifest"]["text"]
NS = 'xmlns:android="http://schemas.android.com/apk/res/android"'


def mk(text=None, **nr):
    r = copy.deepcopy(rec)
    if text is not None:
        r["normalized_result"]["manifest"]["text"] = text
    r["normalized_result"].update(nr)
    return r


cases = [
    ("X01-structured-version-fields-forged", "reject",
     mk(version_code="2", version_name="9.9", min_sdk=99, target_sdk=99)),
    ("X02-structured-version_code-int-forged", "reject", mk(version_code=7)),
    ("X03-prefixed-root-package-attr", "accept",
     mk(GOOD.replace('    package="com.example.r65"', '    xmlns:p="x" p:package="com.example.r65"'))),
    ("X04-dtd-internal-entity-versionCode", "accept",
     mk('<?xml version="1.0"?>\n<!DOCTYPE manifest [<!ENTITY v "1">]>\n<manifest ' + NS +
        ' package="com.example.r65" xmlns:ns1="android" ns1:versionCode="&v;" xmlns:ns2="android" ns2:versionName="1.0"/>')),
    ("X05-dtd-entity-forges-package", "reject",
     mk('<?xml version="1.0"?>\n<!DOCTYPE manifest [<!ENTITY p "com.attacker.x">]>\n<manifest ' + NS +
        ' package="&p;" xmlns:ns1="android" ns1:versionCode="1" xmlns:ns2="android" ns2:versionName="1.0"/>',
        package_name="com.attacker.x")),
    ("X06-whitespace-versionCode", "reject", mk(GOOD.replace('ns1:versionCode="1"', 'ns1:versionCode=" 1"'))),
    ("X07-foreign-namespace-root-tag", "reject",
     mk(GOOD.replace("<manifest ", '<evil:manifest xmlns:evil="urn:evil" ').replace("/>", "></evil:manifest>"))),
    ("X08-permissions-forged", "reject", mk(permissions=["android.permission.INTERNET"])),
    ("X09-unprefixed-dup-plus-prefixed-versionName", "reject",
     mk(GOOD.replace('ns2:versionName="1.0"', 'ns2:versionName="1.0" versionName="1.0"'))),
    ("X10-manifest-status-partial", "reject", mk(manifest={**rec["normalized_result"]["manifest"], "status": "truncated"})),
]
for cid, lab, body in cases:
    (out / f"{cid}.json").write_text(json.dumps(body, indent=2) + "\n", encoding="utf-8")
    print(cid, lab)
