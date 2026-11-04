#!/usr/bin/env python3
"""ExecR90Replay independent root-manifest checker (round-90 C2 cross-impl).

Written from the seat spec only; does not import or copy oracle_check2.py.
Usage: my_oracle.py <record.json> [...]
Prints `<file> accept|reject <reason>` per record. Rule:
  - record is a JSON object with normalized_result.manifest.text (str) and
    normalized_result.package_name (str);
  - text parses as XML (xml.dom.minidom); root element local name `manifest`;
  - ROOT attributes (xmlns declarations excluded), matched by local name with
    any prefix: exactly one `package` == 'com.example.r65', exactly one
    `versionCode` == '1', exactly one `versionName` == '1.0';
  - package_name == root package.
"""
import json
import sys
from xml.dom import minidom
from xml.parsers.expat import ExpatError

PKG, VC, VN = "com.example.r65", "1", "1.0"


def judge(rec):
    if not isinstance(rec, dict):
        return "reject", "not-object"
    nr = rec.get("normalized_result")
    if not isinstance(nr, dict):
        return "reject", "no-normalized_result"
    man = nr.get("manifest")
    text = man.get("text") if isinstance(man, dict) else None
    if not isinstance(text, str):
        return "reject", "no-manifest-text"
    try:
        doc = minidom.parseString(text.encode("utf-8"))
    except ExpatError as e:
        return "reject", f"unparseable:{e}"
    root = doc.documentElement
    if (root.localName or root.tagName) != "manifest":
        return "reject", f"root={root.tagName}"
    vals = {"package": [], "versionCode": [], "versionName": []}
    for i in range(root.attributes.length):
        a = root.attributes.item(i)
        if a.name == "xmlns" or a.name.startswith("xmlns:"):
            continue
        local = a.localName or a.name.split(":")[-1]
        if local in vals:
            vals[local].append(a.value)
    for key, want in (("package", PKG), ("versionCode", VC), ("versionName", VN)):
        if vals[key] != [want]:
            return "reject", f"root-{key}={vals[key]}"
    if nr.get("package_name") != vals["package"][0]:
        return "reject", f"package_name={nr.get('package_name')!r}"
    return "accept", "ok"


def main(argv):
    rc = 0
    for p in argv[1:]:
        try:
            rec = json.load(open(p, encoding="utf-8"))
            v, why = judge(rec)
        except (OSError, ValueError) as e:
            v, why = "reject", f"load:{e}"
        print(f"{p} {v} {why}")
    return rc


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
