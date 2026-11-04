#!/usr/bin/env python3
"""Identity oracle v3 for the apk-r65 fixture and its saved
inspect_android_package record (round 90, UNCLAIMED post-freeze correction;
supersedes v2 `oracle_check2.py`, the frozen round-90 C2 instrument, whose
bytes stay unchanged). v3 changes only the parsed manifest legs: v2 matched
attribute and tag LOCAL names, so a root in a foreign namespace, `x:package`,
`android:package` or versions bound to another URI passed, and an internal
DOCTYPE could inject attribute defaults (seat ForgeryR90Probe, 7 in-scope
false greens). v3 (a) refuses any manifest text carrying a DOCTYPE, (b)
requires the root tag to be the un-namespaced `manifest`, and (c) checks every
authored root attribute in truth.json `axml_declared.attributes` by its EXACT
expanded name — namespace = strings[ns_idx], none for 0xFFFFFFFF — with the
authored value, and refuses any second root attribute sharing its local name.
Two adjacent legs: normalized `version_code`/`version_name` must be absent or
the authored value, and every raw `get_app_info` package must be the authored
package (ForgeryR90Probe N37/N38). Sources: S483 (Android `<manifest>` element reference: root element,
`package`, `android:versionCode`, `android:versionName`) and S484 (Python
ElementTree: the parser skips comments, PIs and DOCTYPE declarations — yet an
internal subset still applies ATTLIST defaults, hence the DOCTYPE refusal).
The v2 description below is kept for history.

v2 (round-90 C2; supersedes v1 `oracle_check.py`, round 89).

v2 changes the manifest declaration legs only. v1 tested substrings of
`manifest.text`, so a record whose root `<manifest package=...>` named another
package passed when the expected fragments sat in an XML comment (round-89
ReviewerR89C2). v2 parses `manifest.text` as XML (comments, processing
instructions and child elements are not root attributes) and checks the ROOT
element: local tag `manifest`, attribute `package` equal to the authored
package, exactly one attribute with local name `versionCode` and one with
`versionName` (any namespace prefix: the producer emits `ns1:`/`ns2:` bound to
the literal URI `android`) holding the authored values, and
`normalized_result.package_name` equal to the parsed root `package`. An
unparseable manifest fails every parsed leg.

Content accuracy only: a hand-written record that states the fixture's true
content passes by design. Provenance is not an oracle property (Q09); it is
carried by the run receipt and the two-run normalized-equality rule.

Usage:
    python -B oracle_check3.py truth.json <record.json>

Premise leg (Q06): re-hash the committed fixture bytes and re-derive the ZIP
member table from them; every value compared against truth.json must match.
Record leg (Q03): the saved producer record's identity and declaration fields
are compared with expectations derived from those same bytes, never copied
from the record. Volatile fields listed in truth.json
`.volatile_not_compared` are never compared.

Prints one line per check and a final verdict line:
    ORACLE OK (n/n checks)   -> exit 0
    ORACLE FAIL (k/n checks) -> exit 1 (each failing check printed)
Exit 2 when an input file is missing, 64 on usage.
"""
import hashlib
import json
import re
import struct
import xml.etree.ElementTree as ET
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
APK = HERE / "fixture.apk"
DEX_CLASS_DEFS_SIZE = 0x60  # class_defs_size, after 20 header fields (DEX spec)


def ok(msg):
    print("check ok: " + msg)
    return True


def fail(msg):
    print("check FAIL: " + msg)
    return False


def main(argv):
    if len(argv) != 3:
        print("usage: oracle_check3.py truth.json <record.json>", file=sys.stderr)
        return 64
    truth_p, record_p = Path(argv[1]), Path(argv[2])
    for p in (truth_p, record_p, APK):
        if not p.is_file():
            print(f"missing input: {p}", file=sys.stderr)
            return 2
    truth = json.loads(truth_p.read_text(encoding="utf-8"))
    rec = json.loads(record_p.read_text(encoding="utf-8"))
    apk = APK.read_bytes()
    checks = []

    # --- premise: the fixture bytes are the authored pin --------------------
    checks.append(ok("fixture sha256 " + hashlib.sha256(apk).hexdigest()[:16])
                  if hashlib.sha256(apk).hexdigest() == truth["image"]["sha256"]
                  else fail("fixture sha256 disagrees with truth.json image.sha256"))
    checks.append(ok(f"fixture size {len(apk)} bytes") if len(apk) == truth["image"]["size"]
                  else fail(f"fixture size {len(apk)} != truth.json {truth['image']['size']}"))
    with zipfile.ZipFile(APK) as z:
        members = {i.filename: z.read(i.filename) for i in z.infolist()}
    authored = {m["name"]: m for m in truth["build_recipe"]["members"]}
    checks.append(ok(f"member set {sorted(members)}") if sorted(members) == sorted(authored)
                  else fail(f"member set {sorted(members)} != authored {sorted(authored)}"))
    byte_ok = all(len(members[n]) == authored[n]["bytes"] for n in authored if n in members)
    checks.append(ok("member byte lengths match the build recipe") if byte_ok
                  else fail("a member's byte length disagrees with the build recipe"))
    digests = {m["name"]: m.get("sha256") for m in truth.get("members", [])}
    dig_ok = all(n in members and digests.get(n)
                 and hashlib.sha256(members[n]).hexdigest() == digests[n]
                 for n in authored)
    checks.append(ok("member digests match truth.json") if dig_ok
                  else fail("a member digest disagrees with truth.json or is unrecorded"))

    # --- expectations derived from the bytes, not from the record -----------
    decl = truth["axml_declared"]
    strings = decl["strings"]
    pkg = strings[4]
    code_name, code_val = strings[5], strings[7]
    name_name, name_val = strings[6], strings[8]
    dex = members.get("classes.dex", b"")
    class_defs = struct.unpack_from("<I", dex, DEX_CLASS_DEFS_SIZE)[0] if len(dex) >= 0x64 else None

    # --- record identity ----------------------------------------------------
    checks.append(ok("operation inspect_android_package")
                  if rec.get("operation") == "inspect_android_package"
                  else fail(f"operation {rec.get('operation')!r}"))
    prov = rec.get("provider") or {}
    checks.append(ok("provider id jadx") if prov.get("id") == "jadx"
                  else fail(f"provider id {prov.get('id')!r}"))
    checks.append(ok("provider version present") if re.fullmatch(r"\d+\.\d+\.\d+", str(prov.get("version")))
                  else fail(f"provider version {prov.get('version')!r}"))
    checks.append(ok("evidence_id shape ev_<64 hex>")
                  if re.fullmatch(r"ev_[0-9a-f]{64}", str(rec.get("evidence_id")))
                  else fail(f"evidence_id {rec.get('evidence_id')!r}"))
    subj = rec.get("subject") or {}
    checks.append(ok("subject digest == fixture sha256")
                  if (subj.get("digest") or {}).get("sha256") == truth["image"]["sha256"]
                  else fail("subject digest != the fixture bytes"))
    checks.append(ok("subject format apk") if subj.get("format") == "apk"
                  else fail(f"subject format {subj.get('format')!r}"))

    # --- record declaration fields vs the authored AXML ---------------------
    nr = rec.get("normalized_result") or {}
    checks.append(ok(f"package_name {pkg}") if nr.get("package_name") == pkg
                  else fail(f"package_name {nr.get('package_name')!r} != authored {pkg!r}"))
    text = (nr.get("manifest") or {}).get("text") or ""
    try:
        root = ET.fromstring(text.encode("utf-8"))
    except (ET.ParseError, ValueError):
        root = None
    local = lambda k: k.rsplit("}", 1)[-1]  # noqa: E731
    checks.append(ok("manifest text carries no DOCTYPE")
                  if "<!doctype" not in text.lower()
                  else fail("manifest text carries a DOCTYPE (internal DTD can inject attributes/entities)"))
    checks.append(ok("manifest parses; root tag is un-namespaced manifest")
                  if root is not None and root.tag == "manifest"
                  else fail(f"root tag {getattr(root, 'tag', None)!r} != 'manifest'"))
    attrib = dict(root.attrib) if root is not None else {}
    nil = 0xFFFFFFFF
    for a in decl["attributes"]:
        name, val = strings[a["name_idx"]], strings[a["raw_value_idx"]]
        key = name if a["ns_idx"] == nil else "{" + strings[a["ns_idx"]] + "}" + name
        same_local = [k for k in attrib if local(k) == name]
        checks.append(ok(f"root attribute {key}={val!r}, sole {name}")
                      if attrib.get(key) == val and same_local == [key]
                      else fail(f"root {name}: keys {same_local!r} value {attrib.get(key)!r} != {key}={val!r}"))
    checks.append(ok("package_name == parsed root package")
                  if attrib.get("package") is not None and nr.get("package_name") == attrib.get("package")
                  else fail(f"package_name {nr.get('package_name')!r} != parsed root {attrib.get('package')!r}"))
    # adjacent record fields (ForgeryR90Probe N37/N38): a stated value must not contradict the AXML
    nv = {"version_code": code_val, "version_name": name_val}
    bad_nv = {k: nr.get(k) for k, v in nv.items() if nr.get(k) not in (None, "", v)}
    checks.append(ok("normalized version fields absent or authored") if not bad_nv
                  else fail(f"normalized version fields contradict the AXML: {bad_nv!r}"))
    app = [c for c in ((rec.get("raw_result") or {}).get("calls") or []) if c.get("operation") == "get_app_info"]
    app_pkgs = []
    for c in app:
        for part in ((c.get("response") or {}).get("content") or []):
            try:
                app_pkgs.append(json.loads(part.get("text") or "").get("package"))
            except (ValueError, AttributeError):
                app_pkgs.append(None)
    checks.append(ok("raw get_app_info package absent or authored") if all(p == pkg for p in app_pkgs)
                  else fail(f"raw get_app_info packages {app_pkgs!r} != {pkg!r}"))
    checks.append(ok("manifest status complete")
                  if (nr.get("manifest") or {}).get("status") == "complete"
                  else fail(f"manifest status {(nr.get('manifest') or {}).get('status')!r}"))
    checks.append(ok("class_count == DEX class_defs_size (0)")
                  if class_defs is not None and nr.get("class_count") == class_defs
                  else fail(f"class_count {nr.get('class_count')!r} != DEX class_defs_size {class_defs!r}"))
    checks.append(ok(f"resource_count == {len(authored)} members")
                  if nr.get("resource_count") == len(authored)
                  else fail(f"resource_count {nr.get('resource_count')!r} != member count {len(authored)}"))
    checks.append(ok("permissions empty") if nr.get("permissions") == []
                  else fail(f"permissions {nr.get('permissions')!r}"))
    checks.append(ok("signature_verification not_performed")
                  if nr.get("signature_verification") == "not_performed"
                  else fail(f"signature_verification {nr.get('signature_verification')!r}"))

    good = sum(1 for c in checks if c)
    verdict = f"ORACLE {'OK' if good == len(checks) else 'FAIL'} ({good}/{len(checks)} checks)"
    print(verdict)
    return 0 if good == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
