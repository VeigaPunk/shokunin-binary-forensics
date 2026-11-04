#!/usr/bin/env python3
"""ForgeryR90Probe: craft manifest forgeries from P1 and score them with oracle_check2."""
import copy, json, subprocess, sys
from pathlib import Path

L = Path("/home/vgpnk/Projects/shokunin/revenger-shokunin")
P1 = L / "reports/round-90/oracle-battery-cases/P1-real-r89-record.json"
ORACLE = L / "corpus/fixtures/apk-r65/oracle_check2.py"
TRUTH = L / "corpus/fixtures/apk-r65/truth.json"
OUT = L / ".ufo/waves/round-90/w1/ForgeryR90Probe/cases"
rec = json.loads(P1.read_text(encoding="utf-8"))
GOOD = rec["normalized_result"]["manifest"]["text"]
DECL = '<?xml version="1.0" encoding="utf-8"?>\n'
NS = 'xmlns:android="http://schemas.android.com/apk/res/android"'
VERS = ' xmlns:ns1="android" ns1:versionCode="1" xmlns:ns2="android" ns2:versionName="1.0"'


def T(text, pkg=None, **nr):
    r = copy.deepcopy(rec)
    r["normalized_result"]["manifest"]["text"] = text
    if pkg is not None:
        r["normalized_result"]["package_name"] = pkg
    r["normalized_result"].update(nr)
    return r


def raw_app_info(pkg):
    r = copy.deepcopy(rec)
    for c in r["raw_result"]["calls"]:
        if c["operation"] == "get_app_info":
            c["response"]["content"][0]["text"] = json.dumps({"package": pkg, "version_name": "9.9", "version_code": "99", "min_sdk": "", "target_sdk": "", "permissions": []})
    return r


# (id, misstates?, note, record)   misstates: "yes" | "no" | "strict" (misstates only under Android namespace semantics)
C = [
    # DOCTYPE / entities
    ("N01-doctype-entity-true-pkg", "no", "internal entity &p; expands to the true package",
     T(DECL + '<!DOCTYPE manifest [<!ENTITY p "com.example.r65">]>\n<manifest ' + NS + ' package="&p;"' + VERS + '/>')),
    ("N02-doctype-entity-fabricated-pkg", "yes", "entity expands to com.attacker.x; package_name true",
     T(DECL + '<!DOCTYPE manifest [<!ENTITY p "com.attacker.x">]>\n<manifest ' + NS + ' package="&p;"' + VERS + '/>')),
    ("N03-attlist-default-package-no-literal-attr", "strict", "no package attribute in the tag; DTD ATTLIST default supplies it (Android/aapt does not process DTDs)",
     T(DECL + '<!DOCTYPE manifest [<!ATTLIST manifest package CDATA "com.example.r65">]>\n<manifest ' + NS + VERS + '/>')),
    ("N04-attlist-default-versions-unnamespaced", "yes", "root declares no versions literally; DTD defaults inject unnamespaced versionCode/versionName",
     T(DECL + '<!DOCTYPE manifest [<!ATTLIST manifest versionCode CDATA "1" versionName CDATA "1.0">]>\n<manifest ' + NS + ' package="com.example.r65"/>')),
    ("N05-attlist-fixed-overrides-nothing-fabricated-literal", "yes", "literal package fabricated; DTD #FIXED says true (expat reports literal)",
     T(DECL + '<!DOCTYPE manifest [<!ATTLIST manifest package CDATA #FIXED "com.example.r65">]>\n<manifest ' + NS + ' package="com.attacker.x"' + VERS + '/>')),
    ("N06-external-entity-pkg", "yes", "package from an unresolvable SYSTEM entity",
     T(DECL + '<!DOCTYPE manifest [<!ENTITY p SYSTEM "file:///etc/hostname">]>\n<manifest ' + NS + ' package="&p;"' + VERS + '/>')),
    # whitespace
    ("N07-pkg-surrounding-spaces", "yes", 'package=" com.example.r65 "',
     T(GOOD.replace('package="com.example.r65"', 'package=" com.example.r65 "'))),
    ("N08-pkg-raw-newline", "yes", "package value with raw trailing newline (normalised to space)",
     T(GOOD.replace('package="com.example.r65"', 'package="com.example.r65\n"'))),
    ("N09-pkg-charref-newline", "yes", "package value with &#10; (kept as LF)",
     T(GOOD.replace('package="com.example.r65"', 'package="com.example.r65&#10;"'))),
    ("N10-pkg-and-package_name-spaces", "yes", "both root package and package_name carry a trailing space",
     T(GOOD.replace('package="com.example.r65"', 'package="com.example.r65 "'), pkg="com.example.r65 ")),
    ("N11-versionCode-surrounding-space", "yes", 'ns1:versionCode=" 1"',
     T(GOOD.replace('ns1:versionCode="1"', 'ns1:versionCode=" 1"'))),
    # char refs
    ("N12-charref-pkg", "no", "&#99;om.example.r65 decodes to the true package",
     T(GOOD.replace('package="com.example.r65"', 'package="&#99;om.example.r65"'))),
    ("N13-charref-hex-versions", "no", "versionCode=&#x31; versionName=1&#46;0",
     T(GOOD.replace('ns1:versionCode="1"', 'ns1:versionCode="&#x31;"').replace('ns2:versionName="1.0"', 'ns2:versionName="1&#46;0"'))),
    # processing instructions / second root
    ("N14-pi-true-fabricated-root", "yes", "PI carries the true manifest, root fabricated",
     T(DECL + '<?manifest package="com.example.r65" versionCode="1" versionName="1.0"?>\n<manifest ' + NS + ' package="com.attacker.x"/>')),
    ("N15-pi-fabricated-true-root", "no", "true root; PI after it states a fabricated manifest",
     T(GOOD + '\n<?manifest package="com.attacker.x" versionCode="9"?>')),
    ("N16-second-root-element", "yes", "true root followed by a second root element (not well-formed)",
     T(GOOD + '\n<manifest package="com.attacker.x"/>')),
    # namespaced package
    ("N17-x-package-only", "yes", "package only as x:package in urn:evil; no unprefixed package attribute",
     T(GOOD.replace('package="com.example.r65"', 'xmlns:x="urn:evil" x:package="com.example.r65"'))),
    ("N18-android-package-only", "yes", "package only as android:package (schema URI)",
     T(GOOD.replace('package="com.example.r65"', 'android:package="com.example.r65"'))),
    ("N19-x-package-plus-fabricated", "yes", "plain package fabricated + x:package true",
     T(GOOD.replace('package="com.example.r65"', 'package="com.attacker.x" xmlns:x="urn:evil" x:package="com.example.r65"'))),
    # BOM
    ("N20-bom-prefixed-text", "no", "U+FEFF before the XML declaration",
     T("\ufeff" + GOOD)),
    ("N21-bom-in-pkg-value", "yes", "package value prefixed with U+FEFF; package_name same",
     T(GOOD.replace('package="com.example.r65"', 'package="\ufeffcom.example.r65"'), pkg="\ufeffcom.example.r65")),
    ("N22-zwsp-in-pkg-value", "yes", "package value with trailing U+200B, package_name same",
     T(GOOD.replace('package="com.example.r65"', 'package="com.example.r65\u200b"'), pkg="com.example.r65\u200b")),
    # CDATA
    ("N23-cdata-true-fabricated-root", "yes", "CDATA child holds the true manifest; root fabricated",
     T(DECL + '<manifest ' + NS + ' package="com.attacker.x"><![CDATA[<manifest package="com.example.r65" versionCode="1" versionName="1.0"/>]]></manifest>')),
    ("N24-cdata-fabricated-true-root", "no", "true root; CDATA child text fabricated",
     T(GOOD[:-2] + '><![CDATA[package="com.attacker.x"]]></manifest>')),
    # manifest in a namespace
    ("N25-manifest-prefixed-urn-evil", "yes", "root element x:manifest in urn:evil (not the Android <manifest>)",
     T(DECL + '<x:manifest xmlns:x="urn:evil" ' + NS + ' package="com.example.r65"' + VERS + '/>')),
    ("N26-manifest-default-ns-urn-evil", "yes", "root manifest in default namespace urn:evil",
     T(DECL + '<manifest xmlns="urn:evil" ' + NS + ' package="com.example.r65"' + VERS + '/>')),
    ("N27-manifest-in-android-ns", "yes", "root android:manifest",
     T(DECL + '<android:manifest ' + NS + ' package="com.example.r65"' + VERS + '/>')),
    # versions namespace / values
    ("N28-versionCode-01", "yes", "versionCode 01",
     T(GOOD.replace('ns1:versionCode="1"', 'ns1:versionCode="01"'))),
    ("N29-versionCode-hex-0x1", "yes", "versionCode 0x1",
     T(GOOD.replace('ns1:versionCode="1"', 'ns1:versionCode="0x1"'))),
    ("N30-versions-unnamespaced", "strict", "versionCode/versionName with no namespace (fixture AXML binds them to URI 'android'; Android ignores unnamespaced)",
     T(DECL + '<manifest ' + NS + ' package="com.example.r65" versionCode="1" versionName="1.0"/>')),
    ("N31-versions-urn-evil", "yes", "versionCode/versionName bound to urn:evil",
     T(DECL + '<manifest ' + NS + ' xmlns:e="urn:evil" package="com.example.r65" e:versionCode="1" e:versionName="1.0"/>')),
    ("N32-versions-android-schema-uri", "strict", "android:versionCode with the schema URI (fixture binds literal 'android')",
     T(DECL + '<manifest ' + NS + ' package="com.example.r65" android:versionCode="1" android:versionName="1.0"/>')),
    # case variants
    ("N33-case-Manifest-tag", "yes", "<Manifest>",
     T(GOOD.replace("<manifest", "<Manifest"))),
    ("N34-case-Package-attr", "yes", "Package=",
     T(GOOD.replace('package="', 'Package="'))),
    ("N35-case-versioncode-attr", "yes", "ns1:versioncode",
     T(GOOD.replace("ns1:versionCode", "ns1:versioncode"))),
    ("N36-case-pkg-value", "yes", "com.Example.r65 in root and package_name",
     T(GOOD.replace("com.example.r65", "com.Example.r65"), pkg="com.Example.r65")),
    # record fields outside the manifest text (adjacent to the hypothesis)
    ("N37-nr-version-fields-fabricated", "yes", "manifest text true; normalized_result.version_code='99', version_name='9.9'",
     T(GOOD, version_code="99", version_name="9.9")),
    ("N38-raw-app-info-fabricated", "yes", "manifest/normalized true; raw_result get_app_info states com.attacker.x 9.9/99",
     raw_app_info("com.attacker.x")),
    ("N39-nested-manifest-child-fabricated", "no", "true root; nested child <manifest package=com.attacker.x versionCode=9>",
     T(GOOD[:-2] + '><manifest package="com.attacker.x" versionCode="9"/></manifest>')),
    ("N40-xml-decl-utf16-label", "no", "XML declaration says UTF-16 while bytes are UTF-8",
     T(GOOD.replace('encoding="utf-8"', 'encoding="utf-16"'))),
]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    for cid, mis, note, r in C:
        p = OUT / f"{cid}.json"
        p.write_text(json.dumps(r, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        cp = subprocess.run([sys.executable, "-B", str(ORACLE), str(TRUTH), str(p)], capture_output=True, text=True)
        verdict = {0: "ACCEPT", 1: "REJECT"}.get(cp.returncode, f"ERR{cp.returncode}")
        last = cp.stdout.strip().splitlines()[-1] if cp.stdout.strip() else cp.stderr.strip()[-120:]
        fails = [l[len("check FAIL: "):] for l in cp.stdout.splitlines() if l.startswith("check FAIL")]
        fg = "FALSE-GREEN" if verdict == "ACCEPT" and mis in ("yes", "strict") else ("false-red" if verdict != "ACCEPT" and mis == "no" else "ok")
        if fg == "FALSE-GREEN" and mis == "strict":
            fg = "FALSE-GREEN(strict)"
        rows.append((cid, mis, verdict, fg, last, "; ".join(fails)[:160], note))
        (OUT / f"{cid}.oracle.log").write_text(cp.stdout + cp.stderr, encoding="utf-8")
    for r in rows:
        print("\t".join(r))


main()
