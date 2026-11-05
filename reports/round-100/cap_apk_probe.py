#!/usr/bin/env python3
"""Round-100 C2 capability probe: APK binary-manifest cross-decode.

Decodes the binary AndroidManifest.xml of corpus/fixtures/apk-r65/fixture.apk
with two independent third-party decoders (androguard ``axml`` and apktool
``d -s``), compares package / versionCode / versionName against the values
recorded in the fixture's truth.json AXML string pool and attribute records
(never hardcoded), then tampers the versionName string-pool value in a
scratch copy (same-length replacement, ZIP CRCs repaired in both the local
header and the central directory) and requires both decoders to report the
tampered value. A decoder (or PATH shim) that echoes the truth values for
any input fails the tamper leg.

Contract (reports/round-100/claims.md §C2):

    PYTHONUTF8=1 python3 -B reports/round-100/cap_apk_probe.py \
        --fixture corpus/fixtures/apk-r65 --work <scratch>

prints, in this order and nothing else on stdout:

    CAP_FIXTURE_SHA=pass|fail
    CAP_DECODER androguard version=<first line of `androguard --version`>
    CAP_DECODER apktool version=<first line of `apktool --version`>
    CAP_ANDROGUARD=pass|fail
    CAP_APKTOOL=pass|fail
    CAP_TAMPER_DETECTED=pass|fail
    CAP_APK_VERDICT=pass|fail            (last)

rc 0 iff pass, 1 if any leg fails, 2 on usage error or a decoder binary that
is neither on PATH nor given via --androguard/--apktool. A fixture-sha
mismatch does not short-circuit: every leg still runs and the verdict fails.

Decoder paths are resolved via PATH so shims can be tested; --androguard and
--apktool override. Scratch: --work wins, then $HYAKU_SCRATCH, then TMPDIR
(tempfile.mkdtemp). Everything the probe creates under scratch is removed on
exit; diagnostics go to stderr, stdout carries only the contract lines.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import shutil
import struct
import subprocess
import sys
import tempfile
import zipfile
import zlib
import xml.etree.ElementTree as ET
from pathlib import Path

NO_INDEX = 0xFFFFFFFF
UTF8_FLAG = 0x100
RES_STRING_POOL_TYPE = 0x0001
FIELDS = ("package", "versionCode", "versionName")
SUB_TIMEOUT = 120


def local_name(qname: str) -> str:
    return qname.rsplit("}", 1)[-1]


def truth_values(truth: dict) -> dict:
    """package/versionCode/versionName from truth.json's AXML records.

    Attribute records: name_idx indexes the string pool for the attribute
    name; a data_type of 0x03 (TYPE_STRING) takes its value from
    raw_value_idx in the pool; other types (0x10 = TYPE_INT_DEC, ...) print
    the `data` field in decimal.
    """
    decl = truth["axml_declared"]
    strings = decl["strings"]
    out: dict[str, str] = {}
    for attr in decl["attributes"]:
        name_idx = attr["name_idx"]
        if not 0 <= name_idx < len(strings):
            continue
        raw_idx = attr.get("raw_value_idx", NO_INDEX)
        if attr.get("data_type") == 0x03 and 0 <= raw_idx < len(strings):
            value = strings[raw_idx]
        else:
            value = str(attr.get("data", ""))
        out[strings[name_idx]] = value
    return out


def run_quiet(cmd: list[str], cwd: str | None = None) -> subprocess.CompletedProcess | None:
    try:
        return subprocess.run(
            cmd, capture_output=True, text=True, timeout=SUB_TIMEOUT, cwd=cwd
        )
    except (OSError, subprocess.TimeoutExpired):
        return None


def decoder_version(path: str, cwd: str | None = None) -> str:
    proc = run_quiet([path, "--version"], cwd=cwd)
    if proc is None:
        return "unknown"
    text = (proc.stdout or "").strip() or (proc.stderr or "").strip()
    return text.splitlines()[0].strip() if text else "unknown"


def decode_androguard(binary: str, apk: Path, cwd: str | None = None):
    """Returns (xml_text, None) or (None, why)."""
    proc = run_quiet([binary, "axml", str(apk)], cwd=cwd)
    if proc is None:
        return None, "androguard axml failed to run"
    if proc.returncode != 0 or not proc.stdout.strip():
        return None, f"androguard axml rc={proc.returncode}: {proc.stderr.strip()[:200]}"
    return proc.stdout, None


def decode_apktool(binary: str, apk: Path, outdir: Path, cwd: str | None = None):
    """Returns (xml_text, None) or (None, why)."""
    if outdir.exists():
        shutil.rmtree(outdir)
    outdir.mkdir(parents=True)
    proc = run_quiet([binary, "d", "-f", "-s", "-o", str(outdir), str(apk)], cwd=cwd)
    manifest = outdir / "AndroidManifest.xml"
    if proc is None:
        return None, "apktool d failed to run"
    if proc.returncode != 0 or not manifest.is_file():
        return None, f"apktool d rc={proc.returncode}: {(proc.stderr or proc.stdout).strip()[:200]}"
    return manifest.read_text(encoding="utf-8"), None


def manifest_attrs(xml_text: str) -> dict:
    """Attribute local names regardless of the decoded prefix.

    This fixture binds the attribute namespace URI "android" (a quirk of the
    authored string pool: the prefix string itself sits in the namespace
    slot), so androguard renders ns0:versionCode and apktool n0:versionCode;
    ElementTree hands those over as {android}versionCode.
    """
    root = ET.fromstring(xml_text)
    return {local_name(key): value for key, value in root.attrib.items()}


def leg_ok(attrs: dict, expected: dict) -> bool:
    return all(field in attrs and attrs[field] == expected.get(field) for field in FIELDS)


def bump_last(value: str) -> str | None:
    """A same-length, different value (e.g. "1.0" -> "1.1")."""
    for i in range(len(value) - 1, -1, -1):
        char = value[i]
        if char.isdigit() and char != "9":
            return value[:i] + str(int(char) + 1) + value[i + 1:]
        if char.isalpha():
            repl = "z" if char.lower() != "z" else "q"
            return value[:i] + (repl.upper() if char.isupper() else repl) + value[i + 1:]
    return None


def pool_encoding(manifest: bytes) -> str | None:
    chunk_type, _, _ = struct.unpack_from("<HHI", manifest, 8)
    if chunk_type != RES_STRING_POOL_TYPE:
        return None
    # Pool chunk header: type(2) headerSize(2) size(4) stringCount(4)
    # styleCount(4) flags(4) stringsStart(4) stylesStart(4) -> flags at +16.
    flags = struct.unpack_from("<I", manifest, 8 + 16)[0]
    return "utf-8" if flags & UTF8_FLAG else "utf-16"


def pool_patch(manifest: bytes, old: str, new: str):
    """Replace the string-pool entry for `old` with same-length `new`.

    Returns (patched_bytes, None) or (None, why). Short-pool entries are
    u8 utf16-length, u8 byte-length, payload, NUL (UTF-8 flag) or u16
    utf16-length twice, UTF-16LE payload, u16 NUL otherwise.
    """
    encoding = pool_encoding(manifest)
    if encoding is None:
        return None, "first AXML chunk is not a string pool"
    if len(new) != len(old):
        return None, f"replacement length differs ({len(old)} -> {len(new)})"
    if encoding == "utf-8":
        old_b, new_b = old.encode("utf-8"), new.encode("utf-8")
        if len(old) >= 0x80 or len(new) >= 0x80:
            return None, "string too long for u8 pool lengths"
        if len(new_b) != len(old_b):
            return None, "replacement utf-8 byte length differs"
        pattern = bytes([len(old), len(old_b)]) + old_b + b"\x00"
        repl = bytes([len(new), len(new_b)]) + new_b + b"\x00"
    else:
        if len(old) >= 0x8000:
            return None, "string too long for u16 pool lengths"
        pattern = struct.pack("<HH", len(old), len(old)) + old.encode("utf-16-le") + b"\x00\x00"
        repl = struct.pack("<HH", len(new), len(new)) + new.encode("utf-16-le") + b"\x00\x00"
    hits = manifest.count(pattern)
    if hits != 1:
        return None, f"pool pattern occurs {hits} times, expected 1"
    return manifest.replace(pattern, repl), None


def patch_apk_member(apk_bytes: bytes, member: str, new_data: bytes):
    """Swap a ZIP_STORED member's bytes in place and fix both CRC-32s."""
    buf = bytearray(apk_bytes)
    with zipfile.ZipFile(io.BytesIO(apk_bytes)) as archive:
        info = archive.getinfo(member)
    loff = info.header_offset
    name_len, extra_len = struct.unpack_from("<HH", buf, loff + 26)
    data_off = loff + 30 + name_len + extra_len
    old = bytes(buf[data_off:data_off + info.compress_size])
    if len(new_data) != len(old):
        return None, "member size changed; stored layout would break"
    crc = zlib.crc32(new_data) & 0xFFFFFFFF
    buf[data_off:data_off + len(old)] = new_data
    buf[loff + 14:loff + 18] = struct.pack("<I", crc)  # local header
    fixed = 0
    pos = 0
    while True:
        pos = buf.find(b"PK\x01\x02", pos)
        if pos < 0:
            break
        name_len = struct.unpack_from("<H", buf, pos + 28)[0]
        name = bytes(buf[pos + 46:pos + 46 + name_len])
        if name == member.encode("utf-8"):
            buf[pos + 16:pos + 20] = struct.pack("<I", crc)  # central directory
            fixed += 1
        pos += 4
    if fixed != 1:
        return None, f"patched {fixed} central-directory entries, expected 1"
    return bytes(buf), None


def tamper_leg(apk_bytes: bytes, expected: dict, scratch: Path, decoders: dict):
    """Both decoders must report the tampered versionName on a valid ZIP."""
    truth_name = expected.get("versionName")
    tampered = bump_last(truth_name or "")
    if not truth_name or not tampered or tampered == truth_name:
        return False, f"cannot derive same-length tampered value from {truth_name!r}"

    try:
        with zipfile.ZipFile(io.BytesIO(apk_bytes)) as archive:
            manifests = [n for n in archive.namelist()
                         if n.split("/")[-1] == "AndroidManifest.xml"]
            if len(manifests) != 1:
                return False, f"manifest members found: {manifests!r}"
            manifest = archive.read(manifests[0])
    except (zipfile.BadZipFile, OSError, ValueError) as exc:
        return False, f"cannot read manifest from fixture zip: {exc}"
    member = manifests[0]

    patched, why = pool_patch(manifest, truth_name, tampered)
    if patched is None:
        return False, f"string-pool patch: {why}"
    new_apk, why = patch_apk_member(apk_bytes, member, patched)
    if new_apk is None:
        return False, f"zip patch: {why}"

    tampered_apk = scratch / "tampered.apk"
    tampered_apk.write_bytes(new_apk)
    try:
        with zipfile.ZipFile(tampered_apk) as archive:
            bad = archive.testzip()
    except (zipfile.BadZipFile, OSError, ValueError) as exc:
        return False, f"tampered zip invalid: {exc}"
    if bad is not None:
        return False, f"zipfile.testzip reported a bad member: {bad}"

    why = (f"decoders did not report tampered versionName {tampered!r} "
           f"(truth {truth_name!r}): ")
    for label, decode in decoders.items():
        xml, err = decode(tampered_apk)
        if xml is None:
            return False, why + f"{label} decode failed: {err}"
        try:
            attrs = manifest_attrs(xml)
        except ET.ParseError as exc:
            return False, why + f"{label} XML parse failed: {exc}"
        got = attrs.get("versionName")
        if got == truth_name:
            return False, why + f"{label} echoed the truth value"
        if got != tampered:
            return False, why + f"{label} reported {got!r}"
    return True, ""


def probe(args, scratch: Path) -> int:
    # Absolute: decoder subprocesses run with cwd=scratch (androguard writes
    # androguard.log into its cwd), so a relative --fixture must not be
    # resolved against their cwd.
    fixture = Path(args.fixture).resolve()
    truth_path = fixture / "truth.json"
    apk = fixture / "fixture.apk"
    if not fixture.is_dir() or not truth_path.is_file() or not apk.is_file():
        print(f"cap_apk_probe: --fixture needs truth.json and fixture.apk, got {fixture}",
              file=sys.stderr)
        return 2

    def emit(line: str) -> None:
        print(line, flush=True)

    truth = json.loads(truth_path.read_text(encoding="utf-8"))
    expected = truth_values(truth)

    digest = hashlib.sha256(apk.read_bytes()).hexdigest()
    want = (truth.get("image") or {}).get("sha256")
    sha_ok = bool(want) and digest == want
    emit(f"CAP_FIXTURE_SHA={'pass' if sha_ok else 'fail'}")
    if not sha_ok:
        print(f"sha256(fixture.apk)={digest} truth.image.sha256={want}", file=sys.stderr)

    androguard = args.androguard or shutil.which("androguard")
    apktool = args.apktool or shutil.which("apktool")
    emit(f"CAP_DECODER androguard version="
         f"{decoder_version(androguard, cwd=scratch) if androguard else 'missing'}")
    emit(f"CAP_DECODER apktool version="
         f"{decoder_version(apktool, cwd=scratch) if apktool else 'missing'}")
    if not androguard or not apktool:
        print(f"missing decoder: androguard={androguard!r} apktool={apktool!r}",
              file=sys.stderr)
        emit("CAP_ANDROGUARD=fail")
        emit("CAP_APKTOOL=fail")
        emit("CAP_TAMPER_DETECTED=fail")
        emit("CAP_APK_VERDICT=fail")
        return 2

    decoders = {
        "androguard": lambda target: decode_androguard(androguard, target, cwd=scratch),
        "apktool": lambda target: decode_apktool(apktool, target, scratch / "apktool-out",
                                                 cwd=scratch),
    }

    apk_bytes = apk.read_bytes()
    leg_ok_flags: list[bool] = []
    for label, decode in decoders.items():
        xml, err = decode(apk)
        ok = False
        detail = err
        if xml is not None:
            try:
                attrs = manifest_attrs(xml)
                ok = leg_ok(attrs, expected)
                detail = (f"decoded={ {f: attrs.get(f) for f in FIELDS} } "
                          f"expected={expected}")
            except ET.ParseError as exc:
                detail = f"XML parse failed: {exc}"
        leg_ok_flags.append(ok)
        emit(f"CAP_{label.upper()}={'pass' if ok else 'fail'}")
        if not ok:
            print(f"{label}: {detail}", file=sys.stderr)

    tamper_ok, why = tamper_leg(apk_bytes, expected, scratch, decoders)
    emit(f"CAP_TAMPER_DETECTED={'pass' if tamper_ok else 'fail'}")
    if not tamper_ok:
        print(f"tamper: {why}", file=sys.stderr)

    verdict = sha_ok and all(leg_ok_flags) and tamper_ok
    emit(f"CAP_APK_VERDICT={'pass' if verdict else 'fail'}")
    return 0 if verdict else 1


def main(argv: list[str]) -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(
        description="Round-100 C2 APK manifest cross-decode probe.")
    parser.add_argument("--fixture", required=True,
                        help="fixture dir holding fixture.apk and truth.json")
    parser.add_argument("--work", help="scratch dir (default: $HYAKU_SCRATCH, then TMPDIR)")
    parser.add_argument("--androguard", help="androguard binary (default: PATH)")
    parser.add_argument("--apktool", help="apktool binary (default: PATH)")
    args = parser.parse_args(argv)

    root = args.work or os.environ.get("HYAKU_SCRATCH")
    if root:
        scratch = Path(root) / f"probe-{os.getpid()}"
        scratch.mkdir(parents=True, exist_ok=True)
    else:
        scratch = Path(tempfile.mkdtemp(prefix="cap-apk-probe-"))
    try:
        return probe(args, scratch)
    finally:
        shutil.rmtree(scratch, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
