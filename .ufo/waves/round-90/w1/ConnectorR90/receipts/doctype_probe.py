#!/usr/bin/env python3
"""ConnectorR90 read-only probe: DOCTYPE-bearing manifest texts vs oracle v2.
Not a frozen instrument; labels are this seat's, not the round's."""
import copy, json, subprocess, sys
from pathlib import Path
LANE = Path("/home/vgpnk/Projects/shokunin/revenger-shokunin")
SRC = LANE / "reports/round-89/rejected-android-record/inspection.json"
TRUTH = LANE / "corpus/fixtures/apk-r65/truth.json"
ORACLES = {"v1": LANE / "corpus/fixtures/apk-r65/oracle_check.py",
           "v2": LANE / "corpus/fixtures/apk-r65/oracle_check2.py"}
OUT = Path(sys.argv[1])
NS = 'xmlns:android="http://schemas.android.com/apk/res/android"'
VER = '\n    xmlns:ns1="android" \n    ns1:versionCode="1"\n    xmlns:ns2="android" \n    ns2:versionName="1.0"'
cases = {
    # package never written on the element: supplied by a DTD default attribute
    "D1-attlist-default-package":
        '<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE manifest [<!ATTLIST manifest package CDATA "com.example.r65">]>\n'
        '<manifest ' + NS + VER + '/>',
    # package value hidden behind an internal entity
    "D2-internal-entity-package":
        '<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE manifest [<!ENTITY p "com.example.r65">]>\n'
        '<manifest ' + NS + '\n    package="&p;"' + VER + '/>',
    # versionCode supplied only by a DTD default (element text carries no versionCode)
    "D3-attlist-default-versionCode":
        '<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE manifest [<!ATTLIST manifest x:versionCode CDATA "1">]>\n'
        '<manifest ' + NS + ' xmlns:x="android"\n    package="com.example.r65"\n    xmlns:ns2="android" \n    ns2:versionName="1.0"/>',
}
rec = json.loads(SRC.read_text(encoding="utf-8"))
OUT.mkdir(parents=True, exist_ok=True)
for cid, text in cases.items():
    r = copy.deepcopy(rec)
    r["normalized_result"]["manifest"]["text"] = text
    p = OUT / f"{cid}.json"
    p.write_text(json.dumps(r, indent=2) + "\n", encoding="utf-8")
    for name, o in ORACLES.items():
        cp = subprocess.run([sys.executable, "-B", str(o), str(TRUTH), str(p)], capture_output=True, text=True)
        last = (cp.stdout.strip().splitlines() or ["<no stdout>"])[-1]
        print(f"CASE {cid} oracle={name} rc={cp.returncode} {last}")
