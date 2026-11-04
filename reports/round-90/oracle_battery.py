#!/usr/bin/env python3
"""Frozen forgery/positive battery for the apk-r65 oracle (round-90 C2).

Usage:
    python3 -B reports/round-90/oracle_battery.py --oracle <oracle.py> [--write DIR]

Every case is derived from the retained round-89 producer record
`reports/round-89/rejected-android-record/inspection.json` (a real, content-
accurate record) and labelled by hand BEFORE any oracle is scored on it:
`reject` = the record misstates the fixture's manifest/identity; `accept` =
the record states the fixture's true content (a content-accurate hand-written
record is `accept` by design: the oracle checks content, not provenance, Q09).

Each case is written to a JSON file and the oracle is run through its public
CLI (`python3 -B <oracle> truth.json <case>`); exit 0 = accepted, exit 1 =
rejected, anything else = an error that counts as a misclassification.
Prints one `CASE <id> label=<l> verdict=<v> <ok|MISCLASS>` line per case and
`ORACLE_MISCLASS=<n>/<cases>`. Exit 0 iff n == 0, 1 otherwise, 64 on usage.
--write keeps the case files in DIR (default: a TMPDIR-honouring temp dir).
"""
import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path

LANE = Path(__file__).resolve().parents[2]
SRC = LANE / "reports/round-89/rejected-android-record/inspection.json"
TRUTH = LANE / "corpus/fixtures/apk-r65/truth.json"
NS = 'xmlns:android="http://schemas.android.com/apk/res/android"'
GOOD_TEXT = ('<?xml version="1.0" encoding="utf-8"?>\n<manifest ' + NS + '\n    package="com.example.r65"\n'
             '    xmlns:ns1="android" \n    ns1:versionCode="1"\n    xmlns:ns2="android" \n    ns2:versionName="1.0"/>')


def with_text(rec, text, pkg=None):
    r = copy.deepcopy(rec)
    r["normalized_result"]["manifest"]["text"] = text
    if pkg is not None:
        r["normalized_result"]["package_name"] = pkg
    return r


def cases(rec):
    assert rec["normalized_result"]["manifest"]["text"] == GOOD_TEXT, "source record drifted"
    hand = copy.deepcopy(rec)
    hand["evidence_id"] = "ev_" + "0" * 64
    hand.pop("raw_result", None)
    return [
        ("P1-real-r89-record", "accept", rec),
        ("P2-hand-written-content-accurate", "accept", hand),
        ("F1-xml-comment-fragments-fabricated-root", "reject", with_text(rec,
            '<?xml version="1.0" encoding="utf-8"?>\n<manifest ' + NS + '\n    package="com.attacker.fabricated">'
            '<!-- versionCode="1" versionName="1.0" --></manifest>')),
        ("F2-fabricated-package-everywhere", "reject", with_text(rec,
            GOOD_TEXT.replace("com.example.r65", "com.attacker.fabricated"), pkg="com.attacker.fabricated")),
        ("F3-minimal-three-key", "reject", {"evidence_id": rec["evidence_id"],
                                             "operation": "inspect_android_package", "normalized_result": {}}),
        ("F4-versions-smuggled-into-child", "reject", with_text(rec,
            '<?xml version="1.0" encoding="utf-8"?>\n<manifest ' + NS + ' package="com.example.r65">'
            '<uses-sdk xmlns:ns1="android" ns1:versionCode="1" ns1:versionName="1.0"/></manifest>')),
        ("F5-conflicting-duplicate-versionCode", "reject", with_text(rec, GOOD_TEXT.replace(
            '    ns2:versionName="1.0"/>', '    ns2:versionName="1.0"\n    xmlns:ns3="other" ns3:versionCode="2"/>'))),
        ("F6-unparseable-text-with-fragments", "reject", with_text(rec,
            'package="com.example.r65" versionCode="1" versionName="1.0" <manifest')),
        ("F7-root-package-disagrees-with-package_name", "reject", with_text(rec,
            GOOD_TEXT.replace("com.example.r65", "com.example.r66"))),
    ]


def main(argv):
    if "--oracle" not in argv:
        print(__doc__, file=sys.stderr)
        return 64
    oracle = Path(argv[argv.index("--oracle") + 1]).resolve()
    keep = Path(argv[argv.index("--write") + 1]) if "--write" in argv else None
    rec = json.loads(SRC.read_text(encoding="utf-8"))
    tmp = None
    if keep is None:
        tmp = tempfile.TemporaryDirectory(prefix="rev-r90-battery-")
        keep = Path(tmp.name)
    keep.mkdir(parents=True, exist_ok=True)
    mis = 0
    cs = cases(rec)
    for cid, label, body in cs:
        p = keep / f"{cid}.json"
        p.write_text(json.dumps(body, indent=2) + "\n", encoding="utf-8")
        rc = subprocess.run([sys.executable, "-B", str(oracle), str(TRUTH), str(p)],
                            capture_output=True, text=True).returncode
        verdict = {0: "accept", 1: "reject"}.get(rc, f"error-rc{rc}")
        good = verdict == label
        mis += not good
        print(f"CASE {cid} label={label} verdict={verdict} {'ok' if good else 'MISCLASS'}")
    print(f"ORACLE_MISCLASS={mis}/{len(cs)}")
    if tmp:
        tmp.cleanup()
    return 0 if mis == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
