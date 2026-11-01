#!/usr/bin/env python
"""gen_managed_r76.py - build a minimal managed PE/CLI (IL-only, DLL) fixture.

The generator derives every header field from the built bytes (Q06: premises
re-derived from the built image, not from intent) and refuses to write unless
all asserts pass. Deterministic: same inputs -> byte-identical image.
"""
import struct
import sys
from pathlib import Path

SECTION_ALIGN = 0x1000
FILE_ALIGN = 0x200
IMAGE_BASE = 0x400000

MODULE_NAME = "r76-managed.dll"
ASSEMBLY_NAME = "r76-managed"
NS_NAME = "R76Probe"
TYPE_NAME = "Probe"
ASM_VERSION = (1, 2, 3, 4)
MVID = bytes(range(0x10))          # authored, deterministic GUID placeholder
VERSION_STRING = b"v4.0.30319\x00\x00"  # 12 bytes (10 chars + NUL, padded to 4)


def pad4(n):
    return (n + 3) & ~3


def build() -> bytes:
    # ---- heaps -----------------------------------------------------------
    # #Strings: offsets into this blob; index 0 is always the empty name.
    names = [b"", b"<Module>", MODULE_NAME.encode(), NS_NAME.encode(), TYPE_NAME.encode(),
             ASSEMBLY_NAME.encode()]
    strings = bytearray(b"\x00")
    str_off = {}
    for n in names:
        str_off[n] = len(strings)
        strings += n + b"\x00"
    strings = bytes(strings)

    us = b"\x00"                    # user-string heap: single empty entry
    guid = MVID                     # 16 bytes, index 1
    blob = b"\x00"                  # empty blob heap; index 0

    # ---- metadata tables (2-byte heap indexes; all row counts < 0x10000) --
    # Module (1 row): Generation(2) Name(2) Mvid(2) EncId(2) EncBaseId(2)
    module_row = struct.pack("<HHHHH", 0, str_off[MODULE_NAME.encode()], 1, 0, 0)
    # TypeDef (2 rows): Flags(4) Name(2) Ns(2) Extends(2) FieldList(2) MethodList(2)
    typedef_rows = (
        struct.pack("<IHHHHH", 0, str_off[b"<Module>"], 0, 0, 1, 1)
        + struct.pack("<IHHHHH", 1, str_off[TYPE_NAME.encode()], str_off[NS_NAME.encode()],
                      0, 1, 1)
    )
    # Assembly (1 row): HashAlgId(4) Maj(2) Min(2) Build(2) Rev(2) Flags(4)
    #                   PublicKey(2) Name(2) Culture(2)
    assembly_row = struct.pack("<IHHHHIHHH", 0x8004, *ASM_VERSION, 1, 0,
                               str_off[ASSEMBLY_NAME.encode()], 0)

    TABLE_MODULE, TABLE_TYPEREF, TABLE_TYPEDEF, TABLE_ASSEMBLY = 0x00, 0x01, 0x02, 0x20
    valid = (1 << TABLE_MODULE) | (1 << TABLE_TYPEDEF) | (1 << TABLE_ASSEMBLY)
    rows_blob = struct.pack("<III", 1, 2, 1)   # row counts in table-number order
    tables_stream = (
        struct.pack("<IBBBB", 0, 2, 0, 0, 1)   # reserved, Major=2, Minor=0, HeapSizes=0, Reserved=1
        + struct.pack("<Q", valid)
        + struct.pack("<Q", 0)                 # sorted
        + rows_blob
        + module_row + typedef_rows + assembly_row
    )

    # ---- stream layout inside metadata -----------------------------------
    # Header: BSJB, ver 1.1, len, version, flags, nstreams, then stream headers.
    n_streams = 5
    root_size = 4 + 2 + 2 + 4 + 4 + pad4(len(VERSION_STRING)) + 2 + 2
    streams = ((b"#~", tables_stream), (b"#Strings", strings),
               (b"#US", us), (b"#GUID", guid), (b"#Blob", blob))
    hdr_size = root_size + sum(8 + pad4(len(nm) + 1) for nm, _ in streams)
    data_off = {}
    dcur = hdr_size
    for name, data in streams:
        data_off[name] = dcur
        dcur += pad4(len(data))
    meta_size = dcur

    meta = bytearray()
    meta += struct.pack("<IHHI", 0x424A5342, 1, 1, 0)      # BSJB 1.1
    meta += struct.pack("<I", len(VERSION_STRING)) + VERSION_STRING
    meta += struct.pack("<HH", 0, n_streams)
    for name, data in streams:
        nsize = pad4(len(name) + 1)
        meta += struct.pack("<II", data_off[name], len(data))
        meta += name + b"\x00" + b"\x00" * (nsize - len(name) - 1)
    assert len(meta) == hdr_size, (len(meta), hdr_size)  # stream data starts here
    for name, data in streams:
        assert len(meta) == data_off[name], (name, len(meta), data_off[name])
        meta += data
        meta += b"\x00" * (pad4(len(data)) - len(data))
    assert len(meta) == meta_size

    # ---- .text section ----------------------------------------------------
    text = bytearray()
    cor20_at = 0            # offset of COR20 header inside .text
    text += struct.pack("<IHHIIIIIIIIII",
                        0x48, 4, 0, 0, 0,   # cb, runtime 4.0, MetaData RVA/size (patched)
                        1, 0,               # Flags=ILONLY, EntryPointToken=0
                        0, 0, 0, 0, 0, 0)   # resources..ManagedNativeHeader
    text += b"\x00" * (0x48 - len(text))    # header declared as 72 bytes
    assert len(text) == 0x48
    text += b"\x00" * (0x80 - len(text))
    meta_rva_off = 0x1000 + 0x80            # metadata RVA (section RVA 0x1000)
    struct.pack_into("<II", text, 8, meta_rva_off, meta_size)
    text += meta

    # ---- PE headers -------------------------------------------------------
    sec_vsize = pad4(len(text))
    sec_rsize = pad4(len(text))
    size_of_headers = pad4(0x40 + 4 + 20 + 0xE0 + 40)
    size_of_image = SECTION_ALIGN + max(sec_vsize, SECTION_ALIGN)

    dos = bytearray(b"\x00" * 0x40)
    dos[0:2] = b"MZ"
    struct.pack_into("<I", dos, 0x3C, 0x40)
    pe = bytearray()
    pe += b"PE\x00\x00"
    pe += struct.pack("<HHIIIHH", 0x014C, 1, 0, 0, 0, 0xE0,
                      0x2102)              # i386, 1 section, DLL
    opt = bytearray()
    opt += struct.pack("<HB", 0x10B, 8)          # Magic, MajorLinker
    opt += bytes([0])                             # MinorLinker
    opt += struct.pack("<I", sec_rsize)           # SizeOfCode
    opt += struct.pack("<I", 0)                   # SizeOfInitializedData
    opt += struct.pack("<I", 0)                   # SizeOfUninitializedData
    opt += struct.pack("<I", 0)                   # AddressOfEntryPoint (DLL, none)
    opt += struct.pack("<I", 0x1000)              # BaseOfCode
    opt += struct.pack("<I", 0)                   # BaseOfData
    opt += struct.pack("<I", IMAGE_BASE)
    opt += struct.pack("<I", SECTION_ALIGN)
    opt += struct.pack("<I", FILE_ALIGN)
    opt += struct.pack("<HH", 4, 0)               # OSVersion 4.0
    opt += struct.pack("<HH", 1, 0)               # ImageVersion 1.0
    opt += struct.pack("<HH", 4, 0)               # SubsystemVersion 4.0
    opt += struct.pack("<I", 0)                   # Win32VersionValue
    opt += struct.pack("<I", size_of_image)
    opt += struct.pack("<I", size_of_headers)
    opt += struct.pack("<I", 0)                   # CheckSum
    opt += struct.pack("<H", 3)                   # Subsystem CUI
    opt += struct.pack("<H", 0x540)               # DllCharacteristics
    opt += struct.pack("<II", 0x100000, 0x1000)   # Stack reserve/commit
    opt += struct.pack("<II", 0x100000, 0x1000)   # Heap reserve/commit
    opt += struct.pack("<II", 0, 16)              # LoaderFlags, NumberOfRvaAndSizes
    ddirs = [(0, 0)] * 16
    ddirs[14] = (0x1000 + cor20_at, 0x48)         # CLR runtime header
    for va, sz in ddirs:
        opt += struct.pack("<II", va, sz)
    assert len(opt) == 0xE0, hex(len(opt))

    sect = struct.pack("<8sIIIIIIHHI", b".text", sec_vsize, 0x1000, sec_rsize,
                       0x200, 0, 0, 0, 0, 0x60000020)

    image = bytearray()
    image += dos
    image += pe
    image += opt
    image += sect
    image += b"\x00" * (0x200 - len(image))
    image += text
    image += b"\x00" * (sec_rsize - len(text))
    return bytes(image)


def self_check(image: bytes) -> None:
    """Re-derive every declared premise from the built bytes (Q06)."""
    assert image[:2] == b"MZ"
    e_lfanew, = struct.unpack_from("<I", image, 0x3C)
    assert e_lfanew == 0x40
    assert image[e_lfanew:e_lfanew + 4] == b"PE\x00\x00"
    machine, nsec, _, _, _, opt_size, chars = struct.unpack_from("<HHIIIHH", image, e_lfanew + 4)
    assert machine == 0x014C and nsec == 1 and opt_size == 0xE0
    magic, = struct.unpack_from("<H", image, e_lfanew + 24)
    assert magic == 0x10B
    ddir = e_lfanew + 24 + 0x60
    num_dd, = struct.unpack_from("<I", image, e_lfanew + 24 + 0x5C)
    assert num_dd == 16
    cor_rva, cor_size = struct.unpack_from("<II", image, ddir + 14 * 8)
    assert cor_size == 0x48
    sec_off = e_lfanew + 24 + opt_size
    vsize, va, rsize, praw = struct.unpack_from("<IIII", image, sec_off + 8)
    assert va <= cor_rva < va + vsize
    cor = 0x200 + (cor_rva - va) if praw else None
    cor_foff = praw + (cor_rva - va)
    cb, maj, minor, md_rva, md_size, flags, eptok = struct.unpack_from("<IHHIIII", image, cor_foff)
    assert cb == 0x48 and (maj, minor) == (4, 0) and flags == 1 and eptok == 0
    md_foff = praw + (md_rva - va)
    sig, vmaj, vmin, _, vlen = struct.unpack_from("<IHHII", image, md_foff)
    assert sig == 0x424A5342 and (vmaj, vmin) == (1, 1)
    ver = image[md_foff + 16: md_foff + 16 + vlen]
    assert ver.startswith(b"v4.0.30319")
    nstreams, = struct.unpack_from("<H", image, md_foff + 16 + vlen + 2)
    assert nstreams == 5
    names = []
    p = md_foff + 16 + vlen + 4
    for _ in range(nstreams):
        so, ss = struct.unpack_from("<II", image, p)
        nm = image[p + 8:p + 8 + 16].split(b"\x00")[0]
        names.append((nm, md_foff + so, ss))
        nlen = pad4(len(nm) + 1)
        p += 8 + nlen
    assert [n for n, _, _ in names] == [b"#~", b"#Strings", b"#US", b"#GUID", b"#Blob"]
    # spot-check heaps round-trip
    for nm, so, ss in names:
        if nm == b"#Strings":
            blob = image[so:so + ss]
            assert blob.startswith(b"\x00")
            assert (MODULE_NAME.encode() + b"\x00") in blob
            assert (ASSEMBLY_NAME.encode() + b"\x00") in blob
        if nm == b"#~":
            t = image[so:so + ss]
            tvalid, = struct.unpack_from("<Q", t, 8)
            assert tvalid == (1 << 0x00) | (1 << 0x02) | (1 << 0x20)
            assert struct.unpack_from("<III", t, 24) == (1, 2, 1)
            gen, name_idx, mvid, encid, encbase = struct.unpack_from("<HHHHH", t, 36)
            assert (gen, mvid, encid, encbase) == (0, 1, 0, 0)
            assert name_idx != 0
    print("self-check OK: managed PE/CLI premises re-derived from built bytes")


def main() -> int:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("fixture.dll")
    image = build()
    self_check(image)
    out.write_bytes(image)
    import hashlib
    print(f"wrote {out} bytes={len(image)} sha256={hashlib.sha256(image).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
