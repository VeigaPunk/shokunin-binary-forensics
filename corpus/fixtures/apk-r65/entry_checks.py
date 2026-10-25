#!/usr/bin/env python3
"""Derivations the round-70 C05 entry embeds (every value it states that the readout
does not print itself). Standard library only; read-only; writes nothing.

Run from the lane root (or a `corpus`-only archive extraction):

    python3 -B corpus/fixtures/apk-r65/entry_checks.py --pins
        sha256 and size of every file the entry pins, recomputed from bytes.
    python3 -B corpus/fixtures/apk-r65/entry_checks.py --eocd
        the four bytes at the end-of-central-directory offset, read from the archive.
    python3 -B corpus/fixtures/apk-r65/entry_checks.py --oracle
        the readout's facts compared field by field with truth.json (one line per field).
    python3 -B corpus/fixtures/apk-r65/entry_checks.py --zip-layout
        APPNOTE record offsets summed from MANUALLY TRANSCRIBED field widths, each compared
        with the literal offset the readout source uses.
    python3 -B corpus/fixtures/apk-r65/entry_checks.py --container
        general-purpose flags and compression method of every local and central record, read from the bytes.
    python3 -B corpus/fixtures/apk-r65/entry_checks.py --axml-layout
        AXML field offsets summed from MANUALLY TRANSCRIBED struct widths (cross-checked against the readout's own
        printed width table) and compared with the literal offsets the readout source uses.
    python3 -B corpus/fixtures/apk-r65/entry_checks.py --stdout-digest
        line count and sha256 of the readout's full stdout.
    python3 -B corpus/fixtures/apk-r65/entry_checks.py --spec-quotes
        each quoted spec phrase located in its committed snapshot copy (tags stripped,
        whitespace folded) with the raw line its first words start on.

Exit 0 when the printed comparisons all hold, 1 when any `MISMATCH` line was printed.
"""
import hashlib
import json
import re
import struct
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CORPUS = HERE.parents[1]
APK = HERE / "fixture.apk"
PINS = (
    "corpus/fixtures/apk-r65/fixture.apk",
    "corpus/fixtures/apk-r65/truth.json",
    "corpus/fixtures/apk-r65/generator.py",
    "corpus/fixtures/apk-r65/readout.py",
    "corpus/fixtures/apk-r65/entry_checks.py",
    "corpus/derive_axml_anchors.py",
    "corpus/snapshots/ResourceTypes.h",
    "corpus/snapshots/APPNOTE.TXT",
    "corpus/snapshots/dex-format.html",
    "corpus/snapshots/rea-android-applications.md",
)

# Manual transcription of APPNOTE.TXT 6.3.10 field widths in bytes, in record order
# (snapshot lines 387-399 section 4.3.7, 511-538 section 4.3.12, 632-646 section 4.3.16).
LOCAL_HEADER = [("signature", 4), ("version_needed", 2), ("flags", 2), ("method", 2), ("time", 2),
                ("date", 2), ("crc32", 4), ("compressed_size", 4), ("uncompressed_size", 4),
                ("name_length", 2), ("extra_length", 2)]
CENTRAL_HEADER = [("signature", 4), ("version_made_by", 2), ("version_needed", 2), ("flags", 2),
                  ("method", 2), ("time", 2), ("date", 2), ("crc32", 4), ("compressed_size", 4),
                  ("uncompressed_size", 4), ("name_length", 2), ("extra_length", 2),
                  ("comment_length", 2), ("disk_start", 2), ("internal_attrs", 2),
                  ("external_attrs", 4), ("local_header_offset", 4)]
EOCD = [("signature", 4), ("disk_number", 2), ("cd_disk", 2), ("entries_this_disk", 2),
        ("total_entries", 2), ("cd_size", 4), ("cd_offset", 4), ("comment_length", 2)]

# (record, field, readout.py literal that must appear)
READOUT_USES = [
    ("eocd", "total_entries", "u16(apk, eocd + {})"),
    ("eocd", "cd_size", "u32(apk, eocd + {})"),
    ("eocd", "cd_offset", "u32(apk, eocd + {})"),
    ("central", "name_length", "u16(apk, cursor + {})"),
    ("central", "extra_length", "u16(apk, cursor + {})"),
    ("central", "comment_length", "u16(apk, cursor + {})"),
    ("central", "local_header_offset", "u32(apk, cursor + {})"),
    ("local", "crc32", "u32(apk, lh_off + {})"),
    ("local", "compressed_size", "u32(apk, lh_off + {})"),
    ("local", "uncompressed_size", "u32(apk, lh_off + {})"),
    ("local", "name_length", "u16(apk, lh_off + {})"),
    ("local", "extra_length", "u16(apk, lh_off + {})"),
]

SPEC_QUOTES = (
    ("corpus/snapshots/rea-android-applications.md",
     "Start with `inspect_android_package` on the caller's APK path for package identity, "
     "manifest declarations, coverage, and inline Evidence."),
    ("corpus/snapshots/dex-format.html",
     "adler32 checksum of the rest of the file (everything but magic and this field)"),
    ("corpus/snapshots/dex-format.html",
     "SHA-1 signature (hash) of the rest of the file (everything but magic, checksum, and this field)"),
    ("corpus/snapshots/dex-format.html", "must be 0x70 (112) bytes (v40 or earlier)"),
    ("corpus/snapshots/dex-format.html", "uint ENDIAN_CONSTANT = 0x12345678;"),
    ("corpus/snapshots/ResourceTypes.h",
     "Byte offset from the start of this structure where the attributes start"),
)


def offsets(fields):
    out, pos = {}, 0
    for name, width in fields:
        out[name] = pos
        pos += width
    return out, pos


def rel(path):
    return CORPUS.parent / path


def pins():
    for p in PINS:
        b = rel(p).read_bytes()
        print(f"sha256 {hashlib.sha256(b).hexdigest()} {len(b)} bytes {p}")
    return 0


def eocd():
    apk = APK.read_bytes()
    pos = apk.rfind(b"PK\x05\x06")
    print(f"eocd signature bytes at offset {pos}: {apk[pos:pos + 4].hex()} (4 bytes)")
    return 0


def oracle():
    truth = json.loads((HERE / "truth.json").read_text(encoding="utf-8"))
    out = subprocess.run([sys.executable, "-B", str(HERE / "readout.py")], capture_output=True, text=True,
                         cwd=str(CORPUS.parent), check=True).stdout
    facts = {}
    for line in out.splitlines():
        obj = json.loads(line)
        facts[obj["fact"]] = obj
    bad = 0

    def cmp(label, got, want):
        nonlocal bad
        ok = got == want
        bad += not ok
        print(f"{'MATCH' if ok else 'MISMATCH'} {label}: readout={got!r} oracle={want!r}")

    cmp("image.sha256", facts["archive"]["sha256"], truth["image"]["sha256"])
    cmp("image.size", facts["archive"]["bytes"], truth["image"]["size"])
    for m in truth["members"]:
        f = facts[f"member[{m['name']}]"]
        cmp(f"{m['name']}.local_header_offset", f["local_header_offset"], m["local_header_offset"])
        cmp(f"{m['name']}.compressed_size", f["compressed_size"], m["compressed_size"])
        cmp(f"{m['name']}.uncompressed_size", f["uncompressed_size"], m["uncompressed_size"])
        cmp(f"{m['name']}.crc32", f["crc32"], m["crc32"])
        cmp(f"{m['name']}.sha256", f["sha256"], m["sha256"])
    cmp("axml.strings", facts["axml_string_pool"]["strings"], truth["axml_declared"]["strings"])
    cmp("axml.resource_ids", facts["axml_resource_map"]["ids"], truth["axml_declared"]["resource_ids"])
    for i, a in enumerate(truth["axml_declared"]["attributes"]):
        got = facts["axml_start_element"]["attributes"][i]
        cmp(f"axml.attribute[{i}].name_index", got["name_index"], a["name_idx"])
        cmp(f"axml.attribute[{i}].ns_index", got["ns_index"], a["ns_idx"])
        cmp(f"axml.attribute[{i}].raw_value_index", got["raw_value_index"], a["raw_value_idx"])
        cmp(f"axml.attribute[{i}].data_type", int(got["data_type"], 16), a["data_type"])
        cmp(f"axml.attribute[{i}].data", got.get("data_type_string", got.get("data_type_int_dec")), a["data"])
    return 1 if bad else 0



APPNOTE_SECTIONS = (
    ("4.3.7", "4.3.7  Local file header:", "local file header signature", "extra field length"),
    ("4.3.12", "4.3.12  Central directory structure:", "central file header signature", "relative offset of local header"),
    ("4.3.16", "4.3.16  End of central directory record:", "end of central dir signature", ".ZIP file comment length"),
)


def appnote_lines():
    lines = rel("corpus/snapshots/APPNOTE.TXT").read_text(encoding="utf-8", errors="ignore").splitlines()
    bad = 0
    for tag, heading, first, last in APPNOTE_SECTIONS:
        h = next((i for i, l in enumerate(lines, 1) if heading in l), 0)
        a = next((i for i, l in enumerate(lines, 1) if i > h and first in l), 0) if h else 0
        b = next((i for i, l in enumerate(lines, 1) if i > a and last in l), 0) if a else 0
        ok = bool(h and a and b)
        bad += not ok
        print(f"{'MATCH' if ok else 'MISMATCH'} APPNOTE {tag}: heading line {h}, transcribed field lines {a}-{b}")
    return bad


def zip_layout():
    src = (HERE / "readout.py").read_text(encoding="utf-8")
    recs = {"local": offsets(LOCAL_HEADER), "central": offsets(CENTRAL_HEADER), "eocd": offsets(EOCD)}
    for name, (_, total) in recs.items():
        print(f"{name} fixed part: {total} bytes (sum of the transcribed field widths)")
    bad = 0
    for rec, field, template in READOUT_USES:
        want = recs[rec][0][field]
        literal = template.format(want)
        ok = literal in src
        bad += not ok
        print(f"{'MATCH' if ok else 'MISMATCH'} {rec}.{field}: spec offset {want}, readout.py literal `{literal}` present={ok}")
    bad += appnote_lines()
    for rec, literal in (("central", "cursor + 46"), ("local", "lh_off + 30")):
        want = recs[rec][1]
        ok = literal in src and f"{want}" in literal
        bad += not ok
        print(f"{'MATCH' if ok else 'MISMATCH'} {rec}.fixed_part: spec width {want}, readout.py literal `{literal}` present={literal in src}")
    return 1 if bad else 0


AXML_WIDTHS = {  # MANUAL second transcription of S038's struct field lists (bytes per field, in order)
    "ResChunk_header": [2, 2, 4],
    "ResStringPool_header": [2, 2, 4, 4, 4, 4, 4, 4],
    "ResXMLTree_node": [2, 2, 4, 4, 4],
    "ResXMLTree_attrExt": [4, 4, 2, 2, 2, 2, 2, 2],
    "ResXMLTree_attribute": [4, 4, 4, 2, 1, 1, 4],
}
POOL = ["type", "headerSize", "size", "stringCount", "styleCount", "flags", "stringsStart", "stylesStart"]
EXT = ["ns", "name", "attributeStart", "attributeSize", "attributeCount", "idIndex", "classIndex", "styleIndex"]
ATTR = ["ns", "name", "rawValue", "valueSize", "valueRes0", "valueDataType", "valueData"]
# (struct, field names, base expression in readout.py, template with {} for the offset, field index list)
AXML_USES = [
    ("ResStringPool_header", POOL, "so", "u32(axml, so + {})", ["stringCount", "styleCount", "flags", "stringsStart", "stylesStart"]),
    ("ResXMLTree_attrExt", EXT, "base", "u32(axml, base + {})", ["ns", "name"]),
    ("ResXMLTree_attrExt", EXT, "base", "u16(axml, base + {})", ["attributeStart", "attributeSize", "attributeCount", "idIndex", "classIndex"]),
]


def axml_layout():
    src = (HERE / "readout.py").read_text(encoding="utf-8")
    out = subprocess.run([sys.executable, "-B", str(HERE / "readout.py"), "--fact", "spec_derived_struct_widths"],
                         capture_output=True, text=True, cwd=str(CORPUS.parent), check=True).stdout
    printed = json.loads(out)["bytes_per_field"]
    bad = 0
    for name, widths in AXML_WIDTHS.items():
        same = printed.get(name) == widths
        bad += not same
        print(f"{'MATCH' if same else 'MISMATCH'} {name}: transcription {widths} readout-printed {printed.get(name)}")
    node = sum(AXML_WIDTHS["ResXMLTree_node"])
    print(f"ResXMLTree_node fixed part: {node} bytes; attrExt begins at chunk offset + {node}")
    for struct, names, _base, template, fields in AXML_USES:
        offs, _ = offsets(list(zip(names, AXML_WIDTHS[struct])))
        shift = node if struct == "ResXMLTree_attrExt" else 0
        for f in fields:
            want = offs[f] + shift
            literal = template.format(want)
            ok = literal in src
            bad += not ok
            print(f"{'MATCH' if ok else 'MISMATCH'} {struct}.{f}: spec offset {offs[f]} (+{shift}), readout.py literal `{literal}` present={ok}")
    offs, _ = offsets(list(zip(ATTR, AXML_WIDTHS["ResXMLTree_attribute"])))
    for f, template in (("ns", "u32(axml, aoff)"), ("name", "u32(axml, aoff + {})"), ("rawValue", "u32(axml, aoff + {})"),
                        ("valueSize", "u16(axml, aoff + {})"), ("valueDataType", "axml[aoff + {}]"),
                        ("valueData", "u32(axml, aoff + {})")):
        literal = template.format(offs[f]) if "{}" in template else template
        ok = literal in src
        bad += not ok
        print(f"{'MATCH' if ok else 'MISMATCH'} ResXMLTree_attribute.{f}: spec offset {offs[f]}, readout.py literal `{literal}` present={ok}")
    return 1 if bad else 0


def container():
    apk = APK.read_bytes()
    truth = json.loads((HERE / "truth.json").read_text(encoding="utf-8"))
    pos = apk.rfind(b"PK\x05\x06")
    n, cd_off = struct.unpack_from("<H", apk, pos + 10)[0], struct.unpack_from("<I", apk, pos + 16)[0]
    cursor, bad = cd_off, 0
    for _ in range(n):
        flags, method = struct.unpack_from("<HH", apk, cursor + 8)
        nlen, xlen, clen = struct.unpack_from("<HHH", apk, cursor + 28)
        lh = struct.unpack_from("<I", apk, cursor + 42)[0]
        name = apk[cursor + 46:cursor + 46 + nlen].decode("utf-8")
        lflags, lmethod = struct.unpack_from("<HH", apk, lh + 6)
        want = next(m["method"] for m in truth["members"] if m["name"] == name)
        same = (flags, method) == (lflags, lmethod) and method == want
        bad += not same
        print(f"{'MATCH' if same else 'MISMATCH'} {name}: local flags=0x{lflags:04x} method={lmethod}; central flags=0x{flags:04x} method={method}; "
              f"bit 3 (data descriptor) {'set' if flags & 8 else 'clear'}; oracle method {want}")
        cursor += 46 + nlen + xlen + clen
    return 1 if bad else 0


def stdout_digest():
    out = subprocess.run([sys.executable, "-B", str(HERE / "readout.py")], capture_output=True, text=True,
                         cwd=str(CORPUS.parent), check=True).stdout
    print(f"readout stdout: {len(out.splitlines())} lines, sha256 {hashlib.sha256(out.encode()).hexdigest()}")
    return 0


def fold(text):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", text)).strip()


def spec_quotes():
    bad = 0
    for path, phrase in SPEC_QUOTES:
        raw = rel(path).read_text(encoding="utf-8", errors="ignore")
        present = fold(phrase) in fold(raw)
        first = " ".join(phrase.split()[:3])
        line = next((i for i, l in enumerate(raw.splitlines(), 1) if first in fold(l)), 0)
        bad += not (present and line)
        print(f"{'MATCH' if present and line else 'MISMATCH'} {Path(path).name}: first line {line}, folded phrase present={present}: {phrase}")
    return 1 if bad else 0


def main():
    cmds = {"--pins": pins, "--eocd": eocd, "--oracle": oracle, "--zip-layout": zip_layout,
            "--stdout-digest": stdout_digest, "--spec-quotes": spec_quotes,
            "--container": container, "--axml-layout": axml_layout}
    if len(sys.argv) != 2 or sys.argv[1] not in cmds:
        print(__doc__)
        return 64
    return cmds[sys.argv[1]]()


if __name__ == "__main__":
    sys.exit(main())
