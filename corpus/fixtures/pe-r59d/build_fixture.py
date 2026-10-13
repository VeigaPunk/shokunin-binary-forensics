#!/usr/bin/env python3
"""Build the pe-r59d PE32+ resource fixture deterministically.

Reuses the pe-r55 header bytes [0:512] verbatim, patches the resource
data-directory size field, and emits a resource tree that adds ONE new
top-level branch: a *named* type key "REVTEST" (kind=name at type level),
something no prior authored fixture exercises. The r55 RT_ICON(3) ids 1/2,
named RT_GROUP_ICON(14) "A😀B!" with two ordered image records, and all
three original payload byte strings are preserved unchanged.

Layout (file offsets; resource section base 512, RVA base 0x2000):
  512  root dir header (named=1, id=2) + 3 entries (528,536,544)
  552  type-3 name dir (id=2), entries 568->langA, 576->langB
  592  type-14 name dir (named=1), entry 608->langC (name str @800)
  616  "REVTEST" name dir (id=1), entry 632->langD
  640/664/688/712  four language dirs (id=1 each), lang entries 656/680/704/728
  736..799  four data entries (icon1, icon2, group, named-type leaf)
  800  group name string u16len+"A😀B!" (12 bytes)
  812  type name string u16len+"REVTEST" (16 bytes)
  832  icon1 payload 48B; 880 icon2 48B; 928 group 34B; 968 named leaf
Writes fixture.exe and truth.json next to this script. No PE execution.
"""
import hashlib
import json
import struct
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE.parent / "pe-r55" / "fixture.exe"
BASE = 512          # resource section file offset
RVA_BASE = 0x2000   # resource section RVA
FILE_SIZE = 1536


def rel(off):
    return off - BASE


def u16(v):
    return struct.pack("<H", v)


def u32(v):
    return struct.pack("<I", v)


def dir_hdr(named, ids):
    return u32(0) + u32(0) + u16(0) + u16(0) + u16(named) + u16(ids)


def entry(key, target):
    return u32(key) + u32(target)


def subdir(off):
    return 0x80000000 | rel(off)


def data_entry(rva, size):
    return u32(rva) + u32(size) + u32(0) + u32(0)


def name_str(text):
    raw = text.encode("utf-16-le")
    return u16(len(raw) // 2) + raw


def rva(off):
    return RVA_BASE + rel(off)


def main():
    src = SRC.read_bytes()
    assert len(src) == FILE_SIZE and src[:2] == b"MZ"
    # r55 payload bytes, lifted verbatim by their known offsets.
    icon1 = src[768:816]
    icon2 = src[832:880]
    group = src[896:930]
    named_payload = b"REV59-NAMED-TYPE-LEAF!!"  # 23 opaque bytes, type REVTEST

    blob = bytearray(src[:FILE_SIZE])
    blob[512:] = b"\x00" * (FILE_SIZE - 512)

    out = bytearray()

    def place(off, data):
        assert len(data) == len(bytes(data))
        blob[off:off + len(data)] = data

    # offsets per plan
    ROOT, T3, T14, TN = 512, 552, 592, 616
    LANG_A, LANG_B, LANG_C, LANG_D = 640, 664, 688, 712
    DE1, DE2, DE3, DE4 = 736, 752, 768, 784
    GSTR, TSTR = 800, 812
    P_ICON1, P_ICON2, P_GROUP, P_LEAF = 832, 880, 928, 968

    place(ROOT, dir_hdr(1, 2)
          + entry(0x80000000 | rel(TSTR), subdir(TN))   # named type "REVTEST" first
          + entry(3, subdir(T3))                        # RT_ICON
          + entry(14, subdir(T14)))                     # RT_GROUP_ICON
    place(T3, dir_hdr(0, 2)
          + entry(1, subdir(LANG_A))
          + entry(2, subdir(LANG_B)))
    place(T14, dir_hdr(1, 0)
          + entry(0x80000000 | rel(GSTR), subdir(LANG_C)))
    place(TN, dir_hdr(0, 1)
          + entry(1, subdir(LANG_D)))
    place(LANG_A, dir_hdr(0, 1) + entry(1033, rel(DE1)))
    place(LANG_B, dir_hdr(0, 1) + entry(1033, rel(DE2)))
    place(LANG_C, dir_hdr(0, 1) + entry(1033, rel(DE3)))
    place(LANG_D, dir_hdr(0, 1) + entry(1033, rel(DE4)))
    place(DE1, data_entry(rva(P_ICON1), len(icon1)))
    place(DE2, data_entry(rva(P_ICON2), len(icon2)))
    place(DE3, data_entry(rva(P_GROUP), len(group)))
    place(DE4, data_entry(rva(P_LEAF), len(named_payload)))
    place(GSTR, name_str("A\U0001F600B!"))
    place(TSTR, name_str("REVTEST"))
    place(P_ICON1, icon1)
    place(P_ICON2, icon2)
    place(P_GROUP, group)
    place(P_LEAF, named_payload)

    dir_size = 832 - BASE          # directory region ends at 832
    assert TSTR + 16 <= 832
    struct.pack_into("<I", blob, 220, dir_size)  # resource data-directory size

    out_path = HERE / "fixture.exe"
    out_path.write_bytes(blob)
    digest = hashlib.sha256(blob).hexdigest()
    truth = {
        "source_fixture": "../pe-r55/fixture.exe",
        "source_sha256": "41c0132a9ecd8274d9afcfc079fefc0c5beb14c1ae81bc7bfa0a2832e140572b",
        "sha256": digest,
        "size": FILE_SIZE,
        "construction": ("PE32+ rebuild of r55 resource tree plus one new top-level "
                         "named type key 'REVTEST' (kind=name at type level) holding a "
                         "numeric name-id 1 / lang 1033 leaf with 23 opaque bytes. Root "
                         "gains named_entries=1, id_entries stays 2; all interior offsets "
                         "re-laid; r55 icon/group payloads byte-identical. No execution."),
        "resource_directory": {"rva": 8192, "file_offset": 512, "bytes": dir_size},
        "named_type": {"value": "REVTEST", "utf16le_hex": "REVTEST".encode("utf-16-le").hex(),
                       "location": [TSTR, TSTR + 16]},
        "group_name": {"value": "A\U0001F600B!",
                       "utf16le_hex": "A\U0001F600B!".encode("utf-16-le").hex(),
                       "location": [GSTR, GSTR + 12]},
        "resources": [
            {"type_name": "REVTEST", "name_id": 1, "language_id": 1033,
             "payload_offset": P_LEAF, "payload_bytes": len(named_payload),
             "sha256": hashlib.sha256(named_payload).hexdigest()},
            {"type_id": 3, "name_id": 1, "language_id": 1033,
             "payload_offset": P_ICON1, "payload_bytes": 48,
             "sha256": hashlib.sha256(icon1).hexdigest()},
            {"type_id": 3, "name_id": 2, "language_id": 1033,
             "payload_offset": P_ICON2, "payload_bytes": 48,
             "sha256": hashlib.sha256(icon2).hexdigest()},
            {"type_id": 14, "name_id": None, "language_id": 1033,
             "payload_offset": P_GROUP, "payload_bytes": 34,
             "sha256": hashlib.sha256(group).hexdigest()},
        ],
        "ordered_group_icon_ids": [1, 2],
        "expected": ("static inspect_pe_resources enumerates 4 leaves incl. named-type "
                     "'REVTEST' leaf byte-exact; icon-group ordered links intact; no "
                     "false link onto the named-type leaf; no PE execution"),
    }
    (HERE / "truth.json").write_text(json.dumps(truth, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {out_path} sha256={digest} size={FILE_SIZE} dir_size={dir_size}")


if __name__ == "__main__":
    main()
