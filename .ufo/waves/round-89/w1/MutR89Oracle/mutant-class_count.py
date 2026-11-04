#!/usr/bin/env python3
"""Identity oracle for the apk-r65 fixture and its saved inspect_android_package
record (round-89 C2 coverage record).

Usage:
    python -B oracle_check.py truth.json <record.json>

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
        print("usage: oracle_check.py truth.json <record.json>", file=sys.stderr)
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
    for attr, val in ((code_name, code_val), (name_name, name_val)):
        frag = f'{attr}="{val}"'
        checks.append(ok(f"manifest declares {frag}") if frag in text
                      else fail(f"manifest text does not declare {frag}"))
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
