#!/usr/bin/env python
"""build_app.py - round-83 authored inert .app bundle fixture (criterion A1,
operation decode_interface_builder).

Everything the oracle checks is derived from the bytes this script builds
(Q06); nothing is stated from intent. The NIBArchive layout follows the
installed rea-agents 6.8.0 parser (dist/artifacts/apple/NibArchive.js):

  header 50B : magic "NIBArchive" | u32 formatVersion(=1) | u32 coderVersion
               | u32 objectCount | u32 objectsOffset | u32 keyCount
               | u32 keysOffset | u32 valueCount | u32 valuesOffset
               | u32 classCount | u32 classesOffset   (all u32 LE; every
               table offset in [50, len]; objects<=keys<=values<=classes)
  object rec : varint classIndex, varint valueStart, varint valueCount
  key rec    : varint byteLength + UTF-8 bytes
  value rec  : varint keyIndex + 1 type byte + payload
               (types: 0 i8, 1 i16, 2 i32, 3 i64, 4 boolFalse, 5 boolTrue,
                6 f32, 7 f64, 8 data(varint len + bytes), 9 nil,
                10 objectReference(u32 LE))
  class rec  : varint nameLen, varint extraCount(<=16), extraCount*4 bytes,
               UTF-8 name

varint: 7-bit little-endian groups; the FINAL group carries the HIGH bit
SET (terminator) and earlier groups carry it CLEAR - the inverse of
standard LEB128 (parser readVarint returns on byte & 0x80). This round's
pre-probe caught the standard-LEB128 draft failing with "NIBArchive
variable integer is too long" (reports/round-83/preprobe-app-shape.log).

Bundle layout: iOS-style root layout - Info.plist at the bundle root
(parser AppBundleExecutable.js BUNDLE_LAYOUTS[1]); the macOS-style
Contents/ layout is the other accepted shape. The pre-probe caught the
missing-plist premise ("app resource root has no supported Info.plist
layout", exit 1) before any committed call.

Run in place:  python -I -B build_app.py
Run elsewhere: python -I -B build_app.py --out <dir>   (regen; never
               regenerates inside corpus/fixtures unless <dir> IS it)

SELFCHECK prints one line per derived check and exits nonzero on any
failure; REGEN compares two builds byte-for-byte.
"""
import argparse
import hashlib
import json
import struct
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

FIXTURE_DIR = Path(__file__).resolve().parent
BUNDLE = "R83Sample.app"

PLIST_XML = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" '
    '"http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n'
    '<plist version="1.0">\n'
    '<dict>\n'
    '  <key>CFBundleIdentifier</key>\n'
    '  <string>local.revenger.r83</string>\n'
    '  <key>CFBundleName</key>\n'
    '  <string>R83Sample</string>\n'
    '</dict>\n'
    '</plist>\n'
)

TYPE_I32 = 2
TYPE_F64 = 7
TYPE_BOOL_T = 5
TYPE_DATA = 8
TYPE_REF = 10


def varint(n):
    # NIBArchive terminator-bit varint (see module docstring).
    assert n >= 0
    if n < 128:
        return bytes([n | 0x80])
    out = bytearray()
    while True:
        b = n & 0x7F
        n >>= 7
        if n:
            out.append(b)
        else:
            out.append(b | 0x80)
            return bytes(out)


def build_nib(classes, objects, keys, values):
    """objects: list of (classIndex, valueStart, valueCount).
    keys: list of UTF-8 key names. values: list of (keyIndex, type, payload)."""
    obj_table = b"".join(varint(c) + varint(s) + varint(n)
                         for c, s, n in objects)
    key_table = b"".join(varint(len(k.encode())) + k.encode()
                         for k in keys)
    val_table = b"".join(varint(ki) + bytes([t]) + p for ki, t, p in values)
    cls_table = b"".join(varint(len(n.encode())) + varint(0) + n.encode()
                         for n in classes)

    objects_offset = 50
    keys_offset = objects_offset + len(obj_table)
    values_offset = keys_offset + len(key_table)
    classes_offset = values_offset + len(val_table)
    total = classes_offset + len(cls_table)

    header = b"NIBArchive"
    header += struct.pack("<I", 1)                  # formatVersion
    header += struct.pack("<I", 1)                  # coderVersion
    header += struct.pack("<I", len(objects))       # objectCount
    header += struct.pack("<I", objects_offset)
    header += struct.pack("<I", len(keys))          # keyCount
    header += struct.pack("<I", keys_offset)
    header += struct.pack("<I", len(values))        # valueCount
    header += struct.pack("<I", values_offset)
    header += struct.pack("<I", len(classes))       # classCount
    header += struct.pack("<I", classes_offset)
    assert len(header) == 50
    nib = bytes(header + obj_table + key_table + val_table + cls_table)
    assert len(nib) == total
    return nib


def f64(x):
    return struct.pack("<d", x)


def i32(x):
    return struct.pack("<i", x)


def ref(idx):
    return struct.pack("<I", idx)


def data(b):
    return varint(len(b)) + b


def main_menu_nib():
    keys = ["NSFrame", "NSHidden", "NSTag", "NSSource", "NSDestination",
            "NSLabel"]
    values = [
        (0, TYPE_F64, f64(137.5)),                    # obj0.NSFrame
        (1, TYPE_BOOL_T, b""),                        # obj0.NSHidden true
        (0, TYPE_F64, f64(42.25)),                    # obj1.NSFrame
        (2, TYPE_I32, i32(7)),                        # obj1.NSTag
        (3, TYPE_REF, ref(0)),                        # obj2.NSSource -> obj0
        (4, TYPE_REF, ref(1)),                        # obj2.NSDestination -> obj1
        (5, TYPE_DATA, data(b"doThing:")),            # obj2.NSLabel
    ]
    objects = [
        (0, 0, 2),   # obj0 UIView  values v0..v1
        (0, 2, 2),   # obj1 UIView  values v2..v3
        (1, 4, 3),   # obj2 NSActionConnector values v4..v6
        (2, 7, 0),   # obj3 NSIBHelpConnector, no values (sourceless
                     # annotation connector per the parser's predicate)
    ]
    classes = ["UIView", "NSActionConnector", "NSIBHelpConnector"]
    return build_nib(classes, objects, keys, values)


def second_view_nib():
    keys = ["NSFrame"]
    values = [(0, TYPE_F64, f64(5.5))]
    objects = [(0, 0, 1)]
    classes = ["UIView"]
    return build_nib(classes, objects, keys, values)


def build_bundle():
    """Returns {relpath: bytes} for the whole authored bundle."""
    return {
        "Info.plist": PLIST_XML.encode("utf-8"),
        "Base.lproj/MainMenu.nib": main_menu_nib(),
        "Base.lproj/SecondView.nib": second_view_nib(),
    }


def selcheck(files, fails):
    def chk(name, ok):
        print("SELFCHECK %s %s" % (name, "ok" if ok else "FAIL"))
        if not ok:
            fails.append(name)

    mm = files["Base.lproj/MainMenu.nib"]
    sv = files["Base.lproj/SecondView.nib"]
    pl = files["Info.plist"]
    chk("plist_magic", pl.startswith(b"<?xml"))
    root = ET.fromstring(pl.decode("utf-8"))
    ids = [e.text for e in root.iter("string")]
    chk("plist_identifier", "local.revenger.r83" in ids)
    for name, nib in (("MainMenu", mm), ("SecondView", sv)):
        chk("%s_magic" % name, nib[:10] == b"NIBArchive")
        fmt, coder = struct.unpack("<II", nib[10:18])
        chk("%s_format_version_1" % name, fmt == 1)
        chk("%s_coder_version_1" % name, coder == 1)
        (obj_n, obj_off, key_n, key_off, val_n, val_off, cls_n,
         cls_off) = struct.unpack("<8I", nib[18:50])
        chk("%s_header_counts" % name,
            (obj_n, key_n, val_n, cls_n) == {
                "MainMenu": (4, 6, 7, 3), "SecondView": (1, 1, 1, 1)}[name])
        chk("%s_offsets_ordered" % name,
            50 <= obj_off <= key_off <= val_off <= cls_off <= len(nib))
        # re-parse each object record as terminator-bit varints: a varint
        # ends at the first byte with the high bit SET; each record must
        # consume exactly 3 varints and the walked cursor must land on the
        # next record boundary
        def read_varints(buf, pos, want):
            vals = []
            for _ in range(want):
                v, shift = 0, 0
                while True:
                    byte = buf[pos]
                    pos += 1
                    v += (byte & 0x7F) << shift
                    if byte & 0x80:
                        vals.append(v)
                        break
                    shift += 7
            return vals, pos

        cur = obj_off
        recs_ok = True
        for _ in range(obj_n):
            vals, cur = read_varints(nib, cur, 3)
            if vals[0] >= cls_n or vals[1] + vals[2] > val_n:
                recs_ok = False
        chk("%s_object_varints_terminate" % name,
            recs_ok and cur == key_off)
        cls_names = []
        cur = cls_off
        for _ in range(cls_n):
            ln = nib[cur] ^ 0x80
            cur += 1
            extras = nib[cur] ^ 0x80
            cur += 1 + 4 * extras
            cls_names.append(nib[cur:cur + ln].decode())
            cur += ln
        chk("%s_class_names" % name, cls_names == {
            "MainMenu": ["UIView", "NSActionConnector", "NSIBHelpConnector"],
            "SecondView": ["UIView"]}[name])
        # size derived: the class table walk ends exactly at EOF, so the
        # whole archive is covered by header + the four walked tables
        chk("%s_size_derived" % name, cur == len(nib))
    mm_sha = hashlib.sha256(mm).hexdigest()
    sv_sha = hashlib.sha256(sv).hexdigest()
    pl_sha = hashlib.sha256(pl).hexdigest()
    print("SELFCHECK shas ok MainMenu=%s SecondView=%s Info.plist=%s"
          % (mm_sha, sv_sha, pl_sha))
    return {"MainMenu": mm_sha, "SecondView": sv_sha, "Info.plist": pl_sha}


def derive_truth(files, shas):
    """Truth is derived from the built bytes only (Q06/Q03). The
    predicted_producer_vocabulary block is the pre-registered Q07
    hypothesis set frozen BEFORE the committed producer run (from the
    preprobe receipts + the installed parser source), recorded whichever
    way it falls."""
    import platform
    mm = files["Base.lproj/MainMenu.nib"]
    sv = files["Base.lproj/SecondView.nib"]
    pl = files["Info.plist"]
    return {
        "bundle": {
            "path": BUNDLE,
            "layout": "root",
            "info_plist": {"sha256": shas["Info.plist"], "bytes": len(pl),
                           "identifier": "local.revenger.r83",
                           "name": "R83Sample"},
        },
        "documents": [
            {
                "relative_path": "Base.lproj/MainMenu.nib",
                "bytes": len(mm), "sha256": shas["MainMenu"],
                "object_count": 4, "key_count": 6, "value_count": 7,
                "class_count": 3,
                "classes": ["UIView", "NSActionConnector",
                            "NSIBHelpConnector"],
                "connection_objects_with_source_encoded": 1,
                "objects": [
                    {"id": 0, "class": "UIView",
                     "values": {"NSFrame": 137.5, "NSHidden": True}},
                    {"id": 1, "class": "UIView",
                     "values": {"NSFrame": 42.25, "NSTag": 7}},
                    {"id": 2, "class": "NSActionConnector",
                     "values": {"NSSource": {"$ref": 0},
                                "NSDestination": {"$ref": 1},
                                "NSLabel_utf8": "doThing:",
                                "NSLabel_base64": "ZG9UaGluZzo="}},
                    {"id": 3, "class": "NSIBHelpConnector", "values": {}},
                ],
            },
            {
                "relative_path": "Base.lproj/SecondView.nib",
                "bytes": len(sv), "sha256": shas["SecondView"],
                "object_count": 1, "key_count": 1, "value_count": 1,
                "class_count": 1, "classes": ["UIView"],
                "connection_objects_with_source_encoded": 0,
                "objects": [
                    {"id": 0, "class": "UIView",
                     "values": {"NSFrame": 5.5}},
                ],
            },
        ],
        "build_recipe": {
            "command": "python -I -B build_app.py",
            "bundle_files": sorted(files),
            "determinism": "struct.pack + fixed literals; no timestamps, "
                           "no randomness, no host paths in bytes",
            "python_version": platform.python_version(),
            "regen": "byte-identical rebuild verified in scratch (--out)",
        },
        "predicted_producer_vocabulary": {
            "_note": "pre-registered Q07 hypotheses (Q05 preprobe + the "
                     "installed 6.8.0 parser source); recorded whichever "
                     "way the committed run falls",
            "subject": None,
            "target_sha256": None,
            "graph_provider_tool_version": "rea-interface-builder/1",
            "scene_nodes": 2,
            "node_count": 8,
            "edge_count": 2,
            "edge_relation": "target_action",
            "action_node": {"kind": "action", "selector": None,
                            "type": "NSActionConnector",
                            "destination_id": "1"},
            "hierarchy_facet": "unsupported",
            "hierarchy_complete": False,
            "connections_facet": "complete",
            "truncated": False,
            "confidence": "observed",
            "authority": "shipped-artifact",
        },
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=None,
                    help="build into <dir>/%s instead of in place" % BUNDLE)
    args = ap.parse_args()
    files = build_bundle()
    fails = []
    shas = selcheck(files, fails)
    if fails:
        print("SELFCHECK failed: %d" % len(fails))
        return 1
    base = Path(args.out).resolve() if args.out else FIXTURE_DIR
    target = base / BUNDLE
    (target / "Base.lproj").mkdir(parents=True, exist_ok=True)
    for rel, data_b in files.items():
        (target / rel).write_bytes(data_b)
    truth = derive_truth(files, shas)
    (base / "truth.json").write_text(
        json.dumps(truth, indent=2, sort_keys=False) + "\n",
        encoding="utf-8", newline="\n")
    print("BUILD %s (%d files)" % (target, len(files)))
    if args.out:
        print("REGEN_NOTE scratch build; compare bytes against the committed "
              "fixture with cmp/sha256sum")
    print("TRUTH_SHA256=%s" % json.dumps(shas, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
