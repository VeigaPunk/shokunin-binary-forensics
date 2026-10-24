#!/usr/bin/env python3
"""Build the inert round-65 APK fixture deterministically.

The fixture is a ZIP container holding three members:
  AndroidManifest.xml  - a hand-built binary AXML (compiled XML) document;
  classes.dex          - a dex *declared header* only (checksum and signature
                         are computed over the header's own bytes; the file
                         contains no classes and is not a valid dex program);
  META-INF/MANIFEST.MF - a plain-text jar manifest.

Nothing is executable; no tool other than this script and the Python standard
library is used. All truth.json measurements (offsets, sizes, digests, the
AXML chunk table) are derived from the finished bytes, not copied from the
layout declarations below.

Determinism: fixed members, fixed DOS date-time, ZIP_STORED (no compressor
dependency), no randomness. Byte-for-byte reproducible with the recorded
Python version.
"""
import hashlib
import json
import platform
import struct
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
APK_PATH = HERE / "fixture.apk"
TRUTH_PATH = HERE / "truth.json"
DOS_DATE_TIME = (2026, 10, 24, 12, 0, 0)
PADDING_NOTE = "R65 inert synthetic APK fixture; no executable content.\n"

# ---------------------------------------------------------------------------
# Binary AXML (compiled XML) member
# ---------------------------------------------------------------------------
# String pool order (UTF-8, UTF8_FLAG set):
STRINGS = [
    "android",                                    # 0  namespace prefix
    "http://schemas.android.com/apk/res/android", # 1  namespace uri
    "manifest",                                   # 2  element name
    "package",                                    # 3  attribute name
    "com.example.r65",                            # 4  package raw value
    "versionCode",                                # 5  attribute name
    "versionName",                                # 6  attribute name
    "1",                                          # 7  versionCode raw value
    "1.0",                                        # 8  versionName raw value
]
NO_INDEX = 0xFFFFFFFF
# Attribute table of the single <manifest> element:
#   (name_idx, ns_idx, raw_value_idx, data_type, data)
# data_type 0x03 = TYPE_STRING, 0x10 = TYPE_INT_DEC (frameworks/base
# ResourceTypes.h Res_value::Type enum).
ATTRIBUTES = [
    (3, NO_INDEX, 4, 0x03, 4),   # package="com.example.r65"
    (5, 0,        7, 0x10, 1),   # android:versionCode = 1
    (6, 0,        8, 0x03, 8),   # android:versionName = "1.0"
]
# Resource map: one uint32 per string; 0 means "no resource id" (AOSP
# ResXMLTree::getAttributeNameResID returns the entry or 0). android.R.attr
# ids: versionCode = 0x0101021b, versionName = 0x0101021c.
RESOURCE_IDS = [0, 0, 0, 0, 0, 0x0101021B, 0x0101021C, 0, 0]


def chunk(chunk_type, header_size, payload):
    return struct.pack("<HHI", chunk_type, header_size, header_size + len(payload)) + payload


def node_chunk(chunk_type, payload):
    """An XML node chunk: 8-byte ResChunk_header plus lineNumber/comment are
    inside headerSize (16); only the extended payload follows."""
    return struct.pack("<HHI", chunk_type, 16, 8 + len(payload)) + payload


def build_string_pool():
    payloads = []
    offsets = []
    cursor = 0
    for s in STRINGS:
        encoded = s.encode("utf-8")
        assert len(s) < 0x80 and len(encoded) < 0x80
        body = bytes([len(s), len(encoded)]) + encoded + b"\x00"
        offsets.append(cursor)
        payloads.append(body)
        cursor += len(body)
    data = b"".join(payloads)
    header_size = 28
    strings_start = header_size + 4 * len(STRINGS)
    header = struct.pack(
        "<HHI", 0x0001, header_size, strings_start + len(data)
    ) + struct.pack(
        "<IIII", len(STRINGS), 0, 0x100, strings_start
    ) + struct.pack("<I", 0)  # stylesStart
    assert len(header) == header_size
    return header + b"".join(struct.pack("<I", o) for o in offsets) + data


def build_resource_map():
    payload = b"".join(struct.pack("<I", r) for r in RESOURCE_IDS)
    return chunk(0x0180, 8, payload)


def build_xml():
    parts = [struct.pack("<HHI", 0x0003, 8, 0)]  # RES_XML_TYPE, size patched at end
    parts.append(build_string_pool())
    parts.append(build_resource_map())
    # START_NAMESPACE
    ns_ext = struct.pack("<II", 0, 1)
    parts.append(node_chunk(0x0100, struct.pack("<II", 1, NO_INDEX) + ns_ext))
    # START_ELEMENT <manifest ...>
    attr_ext = struct.pack(
        "<IIHHHHHH", NO_INDEX, 2, 20, 20, len(ATTRIBUTES), 0, 0, 0
    )
    attrs = b"".join(
        struct.pack("<III", ns, name, raw) + struct.pack("<HBBI", 8, 0, dtype, data)
        for name, ns, raw, dtype, data in ATTRIBUTES
    )
    parts.append(node_chunk(0x0102, struct.pack("<II", 1, NO_INDEX) + attr_ext + attrs))
    # END_ELEMENT </manifest>
    end_ext = struct.pack("<II", NO_INDEX, 2)
    parts.append(node_chunk(0x0103, struct.pack("<II", 1, NO_INDEX) + end_ext))
    # END_NAMESPACE
    parts.append(node_chunk(0x0101, struct.pack("<II", 1, NO_INDEX) + ns_ext))
    body = b"".join(parts)
    return struct.pack("<HHI", 0x0003, 8, len(body)) + body[8:]


# ---------------------------------------------------------------------------
# dex declared-header member (inert)
# ---------------------------------------------------------------------------
def build_dex_header():
    header_size = 112
    header = bytearray(header_size)
    header[0:8] = b"dex\n035\x00"
    struct.pack_into("<I", header, 32, header_size)        # file_size
    struct.pack_into("<I", header, 36, 0x70)               # header_size
    struct.pack_into("<I", header, 40, 0x12345678)         # endian_tag
    # checksum (adler32 of bytes 12..) and signature (sha1 of bytes 32..)
    # derived from the finished header bytes.
    struct.pack_into("<I", header, 8, 0)                    # checksum patched below
    header[12:32] = b"\x00" * 20                            # signature patched below
    sig = hashlib.sha1(bytes(header[32:])).digest()
    header[12:32] = sig
    checksum = __import__("zlib").adler32(bytes(header[12:])) & 0xFFFFFFFF
    struct.pack_into("<I", header, 8, checksum)
    return bytes(header)


# ---------------------------------------------------------------------------
# ZIP container
# ---------------------------------------------------------------------------
def build_apk():
    manifest = build_xml()
    dex = build_dex_header()
    jar_manifest = (
        "Manifest-Version: 1.0\r\n"
        "Created-By: revenger-r65 fixture generator\r\n"
        "\r\n"
    ).encode("utf-8")
    members = [
        ("AndroidManifest.xml", manifest),
        ("classes.dex", dex),
        ("META-INF/MANIFEST.MF", jar_manifest),
    ]
    import io
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_STORED) as zf:
        for name, data in members:
            info = zipfile.ZipInfo(name, date_time=DOS_DATE_TIME)
            info.compress_type = zipfile.ZIP_STORED
            info.external_attr = 0o644 << 16
            zf.writestr(info, data)
    return buffer.getvalue(), [(n, d) for n, d in members]


def parse_members(apk):
    """Measure member offsets and payload digests from the finished zip bytes."""
    measured = []
    with zipfile.ZipFile(__import__("io").BytesIO(apk)) as zf:
        infos = sorted(zf.infolist(), key=lambda i: i.header_offset)
        for info in infos:
            payload = zf.read(info.filename)
            measured.append({
                "name": info.filename,
                "local_header_offset": info.header_offset,
                "compressed_size": info.compress_size,
                "uncompressed_size": info.file_size,
                "crc32": f"{info.CRC:08x}",
                "method": info.compress_type,
                "sha256": hashlib.sha256(payload).hexdigest(),
            })
    return measured


def main():
    apk, members = build_apk()
    measured = parse_members(apk)
    APK_PATH.write_bytes(apk)
    truth = {
        "image": {
            "path": "fixture.apk",
            "sha256": hashlib.sha256(apk).hexdigest(),
            "size": len(apk),
        },
        "members": measured,
        "axml_declared": {
            "strings": STRINGS,
            "attributes": [
                {"name_idx": n, "ns_idx": ns, "raw_value_idx": raw,
                 "data_type": dtype, "data": data}
                for n, ns, raw, dtype, data in ATTRIBUTES
            ],
            "resource_ids": [f"0x{r:08x}" for r in RESOURCE_IDS],
        },
        "build_recipe": {
            "command": "python3 -B generator.py",
            "container": "zipfile.ZipFile(ZIP_STORED), fixed DOS date_time "
                         + "-".join(str(p) for p in DOS_DATE_TIME),
            "members": [{"name": n, "bytes": len(d)} for n, d in members],
            "python_version": platform.python_version(),
            "determinism": "Fixed members, fixed DOS date-time, ZIP_STORED; "
                           "no timestamps inside members, no randomness. "
                           "Byte-for-byte reproducible with the recorded "
                           "Python version.",
        },
    }
    TRUTH_PATH.write_text(json.dumps(truth, indent=2, sort_keys=True) + "\n")
    print(f"fixture.apk {len(apk)} bytes sha256 {truth['image']['sha256']}")
    for m in measured:
        print(f"member {m['name']} offset={m['local_header_offset']} "
              f"size={m['uncompressed_size']} crc32={m['crc32']}")


if __name__ == "__main__":
    main()
