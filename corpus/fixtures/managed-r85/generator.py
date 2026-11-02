#!/usr/bin/env python
"""gen_managed_r85.py - build a minimal managed PE/CLI (IL-only, DLL) fixture
with a real method body (ldstr + ret) and a P/Invoke import declaration, so
`rea inspect-managed-members` and `rea inspect-managed-native-boundaries` have
non-empty collections to report.

Every header field is re-derived from the built bytes by self_check() (Q06:
premises re-derived from the built image, not from intent); the generator
refuses to write unless all asserts pass. Deterministic: same inputs ->
byte-identical image. truth.json is derived from the built bytes (BYTE facts)
plus pre-registered Q07 hypotheses authored here, frozen BEFORE any committed
producer run.
"""
import hashlib
import json
import struct
import sys
from pathlib import Path

SECTION_ALIGN = 0x1000
FILE_ALIGN = 0x200
IMAGE_BASE = 0x400000

MODULE_NAME = "r85-managed.dll"
ASSEMBLY_NAME = "r85-managed"
NS_NAME = "R85Probe"
TYPE_NAME = "Probe"
METHOD_IL_NAME = "SayHello"        # has an IL body: ldstr + ret
METHOD_PINV_NAME = "RunNative"     # P/Invoke declaration, no IL body
PINV_DLL = "native.dll"
LITERAL = "Fixture Hello"
ASM_VERSION = (2, 0, 1, 5)
MVID = bytes(range(0x10, 0x20))    # authored, deterministic GUID placeholder
VERSION_STRING = b"v4.0.30319\x00\x00"  # 12 bytes (10 chars + NUL, padded to 4)

IL_BODY = bytes([0x1A,                       # tiny header (6 bytes IL)<<2|0x02
                 0x72, 0x01, 0x00, 0x00, 0x70,  # ldstr 0x70000001
                 0x2A])                      # ret
assert len(IL_BODY) == 7 and IL_BODY[0] == ((len(IL_BODY) - 1) << 2) | 0x02


def pad4(n):
    return (n + 3) & ~3


def us_heap():
    # #US: entry 0 = empty; entry 1 = LITERAL (compressed len = 2*chars+1 < 0x80;
    # terminal flag 0x00 per ECMA-335 II.24.2.4 — the producer flags 0x01)
    payload = LITERAL.encode("utf-16-le") + b"\x00"
    prefix = bytes([len(payload)])           # len(payload) = 2*13+1 = 27 = 0x1B
    assert len(payload) < 0x80
    return b"\x00" + prefix + payload


def heaps():
    names = [b"", b"<Module>", MODULE_NAME.encode(), NS_NAME.encode(),
             TYPE_NAME.encode(), ASSEMBLY_NAME.encode(),
             METHOD_IL_NAME.encode(), METHOD_PINV_NAME.encode(), PINV_DLL.encode()]
    strings = bytearray(b"\x00")
    str_off = {}
    for n in names:
        str_off[n] = len(strings)
        strings += n + b"\x00"
    # #Blob entries are compressed-length-prefixed:
    #   [0]=empty; sig_sayhello at 1: 03 | DEFAULT 0 params String(0x0E);
    #   sig_runnative at 5: 03 | DEFAULT 0 params Void(0x01)
    sig_il = bytes([0x03, 0x00, 0x00, 0x0E])
    sig_pinv = bytes([0x03, 0x00, 0x00, 0x01])
    blob = b"\x00" + sig_il + sig_pinv
    return bytes(strings), str_off, us_heap(), blob


def build():
    strings, str_off, us, blob = heaps()
    guid = MVID

    # row sizes are fixed, so the layout is computable with a placeholder RVA
    def tables_stream(method_il_rva):
        module_row = struct.pack("<HHHHH", 0, str_off[MODULE_NAME.encode()], 1, 0, 0)
        typedef_rows = (
            struct.pack("<IHHHHH", 0, str_off[b"<Module>"], 0, 0, 1, 1)
            + struct.pack("<IHHHHH", 1, str_off[TYPE_NAME.encode()],
                          str_off[NS_NAME.encode()], 0, 1, 1)
        )
        method_rows = (
            struct.pack("<IHHHHH", method_il_rva, 0x0000, 0x0091,
                        str_off[METHOD_IL_NAME.encode()], 1, 1)
            + struct.pack("<IHHHHH", 0, 0x0005, 0x1091,
                          str_off[METHOD_PINV_NAME.encode()], 5, 1)
        )
        moduleref_row = struct.pack("<H", str_off[PINV_DLL.encode()])
        implmap_row = struct.pack("<HHHH", 0x0102, (2 << 1) | 1,
                                  str_off[METHOD_PINV_NAME.encode()], 1)
        assembly_row = struct.pack("<IHHHHIHHH", 0x8004, *ASM_VERSION, 1, 0,
                                   str_off[ASSEMBLY_NAME.encode()], 0)
        valid = ((1 << 0x00) | (1 << 0x02) | (1 << 0x06)
                 | (1 << 0x1A) | (1 << 0x1C) | (1 << 0x20))
        rows_blob = struct.pack("<IIIIII", 1, 2, 2, 1, 1, 1)
        return (
            struct.pack("<IBBBB", 0, 2, 0, 0, 1)
            + struct.pack("<Q", valid)
            + struct.pack("<Q", 0)
            + rows_blob
            + module_row + typedef_rows + method_rows
            + moduleref_row + implmap_row + assembly_row
        )

    n_streams = 5
    root_size = 4 + 2 + 2 + 4 + 4 + pad4(len(VERSION_STRING)) + 2 + 2
    streams = ((b"#~", tables_stream(0)), (b"#Strings", strings),
               (b"#US", us), (b"#GUID", guid), (b"#Blob", blob))
    hdr_size = root_size + sum(8 + pad4(len(nm) + 1) for nm, _ in streams)
    data_off = {}
    dcur = hdr_size
    for name, data in streams:
        data_off[name] = dcur
        dcur += pad4(len(data))
    meta_size = dcur

    # method body sits in .text right after the metadata; the metadata root is
    # placed at text offset 0x80 (after the 0x48-byte COR20 header, padded)
    body_foff = 0x200 + 0x80 + meta_size
    body_rva = SECTION_ALIGN + 0x80 + meta_size

    tables = tables_stream(body_rva)
    assert len(tables_stream(0)) == len(tables)  # placeholder had the same size

    meta = bytearray()
    meta += struct.pack("<IHHI", 0x424A5342, 1, 1, 0)
    meta += struct.pack("<I", len(VERSION_STRING)) + VERSION_STRING
    meta += struct.pack("<HH", 0, n_streams)
    real_streams = ((b"#~", tables), (b"#Strings", strings),
                    (b"#US", us), (b"#GUID", guid), (b"#Blob", blob))
    for name, data in real_streams:
        nsize = pad4(len(name) + 1)
        meta += struct.pack("<II", data_off[name], len(data))
        meta += name + b"\x00" + b"\x00" * (nsize - len(name) - 1)
    assert len(meta) == hdr_size
    for name, data in real_streams:
        assert len(meta) == data_off[name], (name, len(meta), data_off[name])
        meta += data
        meta += b"\x00" * (pad4(len(data)) - len(data))
    assert len(meta) == meta_size

    text = bytearray()
    text += struct.pack("<IHHIIIIIIIIII",
                        0x48, 4, 0, 0, 0,
                        1, 0,
                        0, 0, 0, 0, 0, 0)
    text += b"\x00" * (0x48 - len(text))
    text += b"\x00" * (0x80 - len(text))
    meta_rva_off = 0x1000 + 0x80
    struct.pack_into("<II", text, 8, meta_rva_off, meta_size)
    text += meta
    assert len(text) == 0x80 + meta_size
    body_at = len(text)
    text += IL_BODY
    assert 0x200 + body_at == body_foff

    sec_vsize = pad4(len(text))
    sec_rsize = pad4(len(text))
    size_of_headers = pad4(0x40 + 4 + 20 + 0xE0 + 40)
    size_of_image = SECTION_ALIGN + max(sec_vsize, SECTION_ALIGN)

    dos = bytearray(b"\x00" * 0x40)
    dos[0:2] = b"MZ"
    struct.pack_into("<I", dos, 0x3C, 0x40)
    pe = bytearray()
    pe += b"PE\x00\x00"
    pe += struct.pack("<HHIIIHH", 0x014C, 1, 0, 0, 0, 0xE0, 0x2102)
    opt = bytearray()
    opt += struct.pack("<HB", 0x10B, 8)
    opt += bytes([0])
    opt += struct.pack("<I", sec_rsize)
    opt += struct.pack("<I", 0)
    opt += struct.pack("<I", 0)
    opt += struct.pack("<I", 0)
    opt += struct.pack("<I", 0x1000)
    opt += struct.pack("<I", 0)
    opt += struct.pack("<I", IMAGE_BASE)
    opt += struct.pack("<I", SECTION_ALIGN)
    opt += struct.pack("<I", FILE_ALIGN)
    opt += struct.pack("<HH", 4, 0)
    opt += struct.pack("<HH", 1, 0)
    opt += struct.pack("<HH", 4, 0)
    opt += struct.pack("<I", 0)
    opt += struct.pack("<I", size_of_image)
    opt += struct.pack("<I", size_of_headers)
    opt += struct.pack("<I", 0)
    opt += struct.pack("<H", 3)
    opt += struct.pack("<H", 0x540)
    opt += struct.pack("<II", 0x100000, 0x1000)
    opt += struct.pack("<II", 0x100000, 0x1000)
    opt += struct.pack("<II", 0, 16)
    ddirs = [(0, 0)] * 16
    ddirs[14] = (0x1000 + 0, 0x48)
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


def _streams_of(image, md_foff):
    sig, vmaj, vmin, _, vlen = struct.unpack_from("<IHHII", image, md_foff)
    nstreams, = struct.unpack_from("<H", image, md_foff + 16 + vlen + 2)
    out = []
    p = md_foff + 16 + vlen + 4
    for _ in range(nstreams):
        so, ss = struct.unpack_from("<II", image, p)
        nm = image[p + 8:p + 8 + 16].split(b"\x00")[0]
        out.append((nm, md_foff + so, ss))
        p += 8 + pad4(len(nm) + 1)
    return out


def self_check(image):
    """Re-derive every declared premise from the built bytes (Q06)."""
    assert image[:2] == b"MZ"
    e_lfanew, = struct.unpack_from("<I", image, 0x3C)
    assert image[e_lfanew:e_lfanew + 4] == b"PE\x00\x00"
    machine, nsec, _, _, _, opt_size, chars = struct.unpack_from(
        "<HHIIIHH", image, e_lfanew + 4)
    assert machine == 0x014C and nsec == 1 and opt_size == 0xE0
    cor_rva, cor_size = struct.unpack_from(
        "<II", image, e_lfanew + 24 + 0x60 + 14 * 8)
    assert cor_size == 0x48
    praw, va = 0x200, 0x1000
    cor_foff = praw + (cor_rva - va)
    cb, maj, minor, md_rva, md_size, flags, eptok = struct.unpack_from(
        "<IHHIIII", image, cor_foff)
    assert cb == 0x48 and (maj, minor) == (4, 0) and flags == 1 and eptok == 0
    md_foff = praw + (md_rva - va)
    streams = dict((nm, (so, ss)) for nm, so, ss in _streams_of(image, md_foff))
    assert set(streams) == {b"#~", b"#Strings", b"#US", b"#GUID", b"#Blob"}

    t, tsize = streams[b"#~"]
    tvalid, = struct.unpack_from("<Q", image, t + 8)
    want_valid = ((1 << 0x00) | (1 << 0x02) | (1 << 0x06)
                  | (1 << 0x1A) | (1 << 0x1C) | (1 << 0x20))
    assert tvalid == want_valid, hex(tvalid)
    counts = struct.unpack_from("<IIIIII", image, t + 24)
    assert counts == (1, 2, 2, 1, 1, 1), counts
    # rows start after the 24-byte header + six 4-byte row counts
    rows = t + 48
    module_row = rows
    typedef_rows = rows + 10
    method_rows = typedef_rows + 28
    il_rva, il_impl, il_flags, il_name, il_sig, il_par = struct.unpack_from(
        "<IHHHHH", image, method_rows)
    pn_rva, pn_impl, pn_flags, pn_name, pn_sig, pn_par = struct.unpack_from(
        "<IHHHHH", image, method_rows + 14)
    assert pn_rva == 0 and pn_impl == 0x0005 and pn_flags == 0x1091
    assert pn_par == 1 and il_par == 1
    body_foff = praw + (il_rva - va)
    assert image[body_foff:body_foff + len(IL_BODY)] == IL_BODY, "IL body bytes"
    # IL decodes: tiny header 6 bytes; ldstr token 0x70000001; ret
    hdr = image[body_foff]
    assert (hdr & 0x03) == 0x02 and (hdr >> 2) == 6
    tok, = struct.unpack_from("<I", image, body_foff + 2)
    assert tok == 0x70000001, hex(tok)
    assert image[body_foff + 6] == 0x2A
    # ImplMap row (ModuleRef 0x1B sits before ImplMap 0x1D in table order)
    moduleref_rows = method_rows + 28
    implmap_rows = moduleref_rows + 2
    mapping, fwd, imp_name, imp_mod = struct.unpack_from("<HHHH", image, implmap_rows)
    assert (mapping, fwd, imp_mod) == (0x0102, 5, 1), (mapping, fwd, imp_mod)
    mr_name, = struct.unpack_from("<H", image, moduleref_rows)
    # heap resolutions
    s, ssize = streams[b"#Strings"]

    def cstr(idx):
        end = image.index(b"\x00", s + idx)
        return image[s + idx:end].decode()

    assert cstr(pn_name) == METHOD_PINV_NAME
    assert cstr(mr_name) == PINV_DLL
    assert cstr(il_name) == METHOD_IL_NAME
    # #US entry 1 decodes to the literal
    u, usize = streams[b"#US"]
    ulen = image[u + 1]
    lit = image[u + 2:u + 2 + ulen - 1]
    assert lit.decode("utf-16-le") == LITERAL
    assert image[u + 2 + ulen - 1] == 0x00
    # #Blob signatures
    b, bsize = streams[b"#Blob"]
    assert image[b + 1:b + 5] == bytes([0x03, 0x00, 0x00, 0x0E])
    assert image[b + 1:b + 5] == bytes([0x03, 0x00, 0x00, 0x0E])
    assert image[b + 5:b + 9] == bytes([0x03, 0x00, 0x00, 0x01])
    assert il_sig == 1 and pn_sig == 5
    print("self-check OK: managed PE/CLI premises re-derived from built bytes")
    print(f"  method_rows@file={method_rows:#x} il_rva={il_rva:#x} "
          f"body_foff={body_foff:#x} ldstr_tok={tok:#010x}")
    print(f"  implmap mapping={mapping:#06x} fwd={fwd} import={cstr(imp_name)!r} "
          f"module={cstr(mr_name)!r}")
    print(f"  us[1]={LITERAL!r} ({ulen})  tables={counts}")


def derive_truth(image):
    """BYTE facts re-derived from the built bytes + pre-registered Q07 hypotheses."""
    t_find = None
    e_lfanew, = struct.unpack_from("<I", image, 0x3C)
    cor_rva, _ = struct.unpack_from("<II", image, e_lfanew + 24 + 0x60 + 14 * 8)
    md_rva, = struct.unpack_from("<I", image, 0x200 + (cor_rva - 0x1000) + 8)
    md_foff = 0x200 + (md_rva - 0x1000)
    streams = dict((nm, (so, ss)) for nm, so, ss in _streams_of(image, md_foff))
    t, _ = streams[b"#~"]
    method_rows = t + 48 + 10 + 28
    il_rva, il_impl, il_flags, il_name, il_sig, il_par = struct.unpack_from(
        "<IHHHHH", image, method_rows)
    pn_rva, pn_impl, pn_flags, pn_name, pn_sig, _pn_par = struct.unpack_from(
        "<IHHHHH", image, method_rows + 14)
    moduleref_rows = method_rows + 28
    implmap_rows = moduleref_rows + 2
    mapping, fwd, imp_name, imp_mod = struct.unpack_from("<HHHH", image, implmap_rows)
    mr_name, = struct.unpack_from("<H", image, moduleref_rows)
    mr_name, = struct.unpack_from("<H", image, moduleref_rows)
    s, _ = streams[b"#Strings"]

    def cstr(idx):
        end = image.index(b"\x00", s + idx)
        return image[s + idx:end].decode()

    body_foff = 0x200 + (il_rva - 0x1000)
    tok, = struct.unpack_from("<I", image, body_foff + 2)
    return {
        "sha256": hashlib.sha256(image).hexdigest(),
        "byte_length": len(image),
        "module_name": MODULE_NAME,
        # producer GUID rendering convention, pre-registered as a Q07 hypothesis:
        # groups 1-3 are little-endian, group 4+ are sequential (observed on the
        # r76 record for bytes 00..0f -> "03020100-0504-0706-0809-0a0b0c0d0e0f")
        "mvid": "%02x%02x%02x%02x-%02x%02x-%02x%02x-%02x%02x-%s" % (
            MVID[3], MVID[2], MVID[1], MVID[0], MVID[5], MVID[4],
            MVID[7], MVID[6], MVID[8], MVID[9],
            "".join("%02x" % b for b in MVID[10:])),
        "assembly_name": ASSEMBLY_NAME,
        "assembly_version": ".".join(str(x) for x in ASM_VERSION),
        "method_il": {
            "name": cstr(il_name),
            "token": "0x06000001",
            "rva": il_rva,
            "file_offset": body_foff,
            "flags": il_flags,
            "impl_flags": il_impl,
            "sig_blob_offset": il_sig,
            "sig_bytes": "0300000e",
            "ldstr_token": "0x%08x" % tok,
            "il_bytes_hex": image[body_foff:body_foff + len(IL_BODY)].hex(),
        },
        "method_pinvoke": {
            "name": cstr(pn_name),
            "token": "0x06000002",
            "rva": pn_rva,
            "flags": pn_flags,
            "impl_flags": pn_impl,
            "sig_blob_offset": pn_sig,
            "sig_bytes": "03000001",
        },
        "pinvoke": {
            "import_name": cstr(imp_name),
            "module_name": cstr(mr_name),
            "mapping_flags": mapping,
            "member_forwarded_coded": fwd,
        },
        "user_string": {
            "heap_offset": 1,
            "token": "0x%08x" % tok,
            "value": LITERAL,
        },
        "table_row_counts": {
            "Module": 1, "TypeDef": 2, "MethodDef": 2,
            "ModuleRef": 1, "ImplMap": 1, "Assembly": 1,
        },
        "hyp": {
            "members_operation": "inspect_managed_members",
            "boundaries_operation": "inspect_managed_native_boundaries",
            "provider_id": "rea-dotnet-static",
            "metadata_status": "complete",
            "coverage_state": "complete",
            "confidence": "observed",
            "authority": "shipped-artifact",
            "module_ref_count": 1,
            "pinvoke_import_count": 1,
            "user_string_literal_count": 1,
            "body_status": "present",
            "body_format": "tiny",
            "opcode_counts": {"ldstr": 1, "ret": 1},
            "sig_parse_status": "decoded",
            "us_state": "complete",
            "verification": "managed-declaration-only",
            "boundary_kind": "pinvoke",
            "code_type": "native",
            "managed_kind": "unmanaged",
            "artifact_operation": "inspect_managed_artifact",
            "classification_status": "managed",
            "implementation": "cil",
            "managed_architecture": "anycpu",
            "stream_names": ["#Blob", "#GUID", "#Strings", "#US", "#~"],
            "evidence_codes": ["cli-header-observed", "managed-architecture-derived"],
            "cor_header_file_offset": 512,
            "cor_flags_file_offset": 528,
        },
    }


def main() -> int:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("fixture.dll")
    write_truth = "--truth" in sys.argv
    image = build()
    self_check(image)
    out.write_bytes(image)
    print(f"wrote {out} bytes={len(image)} sha256={hashlib.sha256(image).hexdigest()}")
    if write_truth:
        truth_path = out.parent / "truth.json"
        truth_path.write_text(json.dumps(derive_truth(image), indent=1) + "\n",
                              encoding="utf-8")
        print(f"wrote {truth_path} bytes={truth_path.stat().st_size}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
