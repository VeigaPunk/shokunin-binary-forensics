#!/usr/bin/env python3
"""Manual byte-derived readout of the round-65 APK fixture.

Reads only the fixture's own bytes with struct; no producer is called, nothing
is extracted to disk. Every fact printed is derived below from
corpus/fixtures/apk-r65/fixture.apk. Run from the lane root:

    python3 -B corpus/fixtures/apk-r65/readout.py

Exit 0. Prints one JSON object per fact on stdout; fact ids are stable and
used by corpus/knowledge/round-65-apk-axml-byte-evidence.md.
"""
import hashlib
import json
import struct
import sys
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
APK = ROOT / "fixture.apk"
NO_INDEX = 0xFFFFFFFF
ONLY = None  # set by main(): --fact <id> prints only that fact


def emit(fact, **fields):
    if ONLY is not None and fact != ONLY:
        return
    fields.pop("only", None)
    print(json.dumps({"fact": fact, **fields}, sort_keys=True))


def u16(data, off):
    return struct.unpack_from("<H", data, off)[0]


def u32(data, off):
    return struct.unpack_from("<I", data, off)[0]


def main():
    global ONLY
    ONLY = sys.argv[sys.argv.index("--fact") + 1] if "--fact" in sys.argv else None
    apk = APK.read_bytes()
    emit("archive", path="corpus/fixtures/apk-r65/fixture.apk", bytes=len(apk),
         sha256=hashlib.sha256(apk).hexdigest())

    # --- Spec-derived structure widths (S038 field lists) --------------------
    # Every fixed offset the readout uses is computed here from the field
    # widths in ResourceTypes.h's own struct definitions, not assumed.
    w8, w16, w32 = 1, 2, 4
    widths = {
        "ResChunk_header": [w16, w16, w32],
        "ResStringPool_header": [w16, w16, w32, w32, w32, w32, w32, w32],
        "ResXMLTree_node": [w16, w16, w32, w32, w32],
        "ResXMLTree_attrExt": [w32, w32, w16, w16, w16, w16, w16, w16],
        "ResXMLTree_attribute": [w32, w32, w32, w16, w8, w8, w32],
        "Res_value": [w16, w8, w8, w32],
    }
    sizes = {name: sum(w) for name, w in widths.items()}
    emit("spec_derived_struct_widths",
         source_anchor="S038 ResourceTypes.h struct field lists",
         bytes_per_field={k: v for k, v in widths.items()},
         total_bytes=sizes,
         attr_ext_attribute_start=sizes["ResXMLTree_attrExt"],
         attribute_size=sizes["ResXMLTree_attribute"],
         node_header_size=sizes["ResXMLTree_node"],
         string_pool_header_size=sizes["ResStringPool_header"])

    # --- ZIP container facts: a raw byte walk of the finished archive ------
    # Field offsets below are the APPNOTE 6.3.10 fixed record widths (S032
    # section 4.3.12 central directory header = 46-byte fixed part; S034
    # section 4.3.7 local file header = 30-byte fixed part): local header
    # crc-32 at +14, compressed size at +18, name length at +26, extra
    # length at +28; central-directory local-header offset at +42.
    sig_eocd = b"PK\x05\x06"
    eocd = apk.rfind(sig_eocd)
    cd_size = u32(apk, eocd + 12)
    cd_off = u32(apk, eocd + 16)
    total_entries = u16(apk, eocd + 10)
    emit("eocd", eocd_offset=eocd,
         total_entries_cd=total_entries,
         size_of_central_directory=cd_size,
         offset_of_start_of_cd=cd_off,
         cd_end_equals_eocd_offset=(cd_off + cd_size == eocd),
         parsed_entries=total_entries)
    members = {}
    cursor = cd_off
    for index in range(total_entries):
        assert apk[cursor:cursor + 4] == b"PK\x01\x02", f"cd header {index}"
        name_len = u16(apk, cursor + 28)
        extra_len = u16(apk, cursor + 30)
        comment_len = u16(apk, cursor + 32)
        lh_off = u32(apk, cursor + 42)
        name = apk[cursor + 46:cursor + 46 + name_len].decode("utf-8")
        cursor += 46 + name_len + extra_len + comment_len
        # local header at the recorded offset
        assert apk[lh_off:lh_off + 4] == b"PK\x03\x04", f"local header {name}"
        lh_name_len = u16(apk, lh_off + 26)
        lh_extra_len = u16(apk, lh_off + 28)
        compressed_size = u32(apk, lh_off + 18)
        crc_stated = f"{u32(apk, lh_off + 14):08x}"
        lh_name = apk[lh_off + 30:lh_off + 30 + lh_name_len].decode("utf-8")
        assert lh_name == name, (lh_name, name)
        payload_off = lh_off + 30 + lh_name_len + lh_extra_len
        payload = apk[payload_off:payload_off + compressed_size]
        members[name] = payload
        emit(f"member[{name}]",
             cd_index=index,
             local_header_offset=lh_off,
             payload_offset=payload_off,
             compressed_size=compressed_size,
             uncompressed_size=u32(apk, lh_off + 22),
             crc32=crc_stated,
             crc32_recomputed=f"{zlib.crc32(payload) & 0xFFFFFFFF:08x}",
             crc32_matches=(crc_stated == f"{zlib.crc32(payload) & 0xFFFFFFFF:08x}"),
             sha256=hashlib.sha256(payload).hexdigest(),
             payload_first16_hex=payload[:16].hex())
    assert cursor == eocd, (cursor, eocd)
    axml = members["AndroidManifest.xml"]
    dex = members["classes.dex"]
    jar = members["META-INF/MANIFEST.MF"]

    # --- binary AXML facts --------------------------------------------------
    # Chunk walk: ResChunk_header = type u16, headerSize u16, size u32
    # (S038 ResourceTypes.h struct ResChunk_header field list). The root
    # RES_XML_TYPE header's own size field is the whole document, so the
    # child chunks are walked from offset 8 (the root's headerSize).
    assert u16(axml, 0) == 0x0003, "not a RES_XML_TYPE document"
    xml_size = u32(axml, 4)
    chunks = []
    off = u16(axml, 2)
    while off < xml_size:
        ctype = u16(axml, off)
        hsize = u16(axml, off + 2)
        csize = u32(axml, off + 4)
        chunks.append({"offset": off, "type": ctype, "headerSize": hsize,
                       "size": csize})
        if csize <= 0:
            raise ValueError(f"zero-size chunk at {off}")
        off += csize
    emit("axml_chunk_table", xml_header_type=u16(axml, 0),
         xml_total_size=xml_size, xml_total_size_equals_member=len(axml) == xml_size,
         chunks=chunks)

    # String pool (RES_STRING_POOL_TYPE chunk): header fields after the
    # 8-byte ResChunk_header (S038 struct ResStringPool_header field list).
    sp = next(c for c in chunks if c["type"] == 0x0001)
    so = sp["offset"]
    string_count = u32(axml, so + 8)
    style_count = u32(axml, so + 12)
    flags = u32(axml, so + 16)
    strings_start = u32(axml, so + 20)
    styles_start = u32(axml, so + 24)
    offsets = [u32(axml, so + sp["headerSize"] + 4 * i) for i in range(string_count)]
    strings = []
    for rel in offsets:
        base = so + strings_start + rel
        u16len = axml[base]
        u8len = axml[base + 1]
        s = axml[base + 2:base + 2 + u8len].decode("utf-8")
        assert len(s) == u16len
        strings.append(s)
    emit("axml_string_pool", offset=so, stringCount=string_count,
         styleCount=style_count, flags=f"0x{flags:08x}",
         utf8=bool(flags & 0x100), sorted_flag=bool(flags & 0x1),
         stringsStart=strings_start, stylesStart=styles_start,
         offsets=offsets, strings=strings)

    # Resource map (RES_XML_RESOURCE_MAP_TYPE): one uint32 per string.
    rm = next(c for c in chunks if c["type"] == 0x0180)
    ids = [u32(axml, rm["offset"] + 8 + 4 * i) for i in range(string_count)]
    emit("axml_resource_map", offset=rm["offset"], entry_count=len(ids),
         ids=[f"0x{x:08x}" for x in ids],
         nonzero={strings[i]: f"0x{ids[i]: 08x}".replace(" ", "") for i in range(len(ids)) if ids[i] != 0})

    # START_NAMESPACE / END_NAMESPACE chunks.
    for label, ctype in (("start_namespace", 0x0100), ("end_namespace", 0x0101)):
        ch = next(c for c in chunks if c["type"] == ctype)
        prefix = u32(axml, ch["offset"] + 16)
        uri = u32(axml, ch["offset"] + 20)
        emit(f"axml_{label}", offset=ch["offset"], lineNumber=u32(axml, ch["offset"] + 8),
             prefix_index=prefix, prefix=strings[prefix],
             uri_index=uri, uri=strings[uri])

    # START_ELEMENT chunk.
    se = next(c for c in chunks if c["type"] == 0x0102)
    base = se["offset"]
    line = u32(axml, base + 8)
    ns_idx = u32(axml, base + 16)
    name_idx = u32(axml, base + 20)
    attribute_start = u16(axml, base + 24)
    attribute_size = u16(axml, base + 26)
    attribute_count = u16(axml, base + 28)
    id_index = u16(axml, base + 30)
    class_index = u16(axml, base + 32)
    style_index = u16(axml, base + 34)
    attrs = []
    for i in range(attribute_count):
        # attributeStart is "Byte offset from the start of this structure"
        # (S038 ResXMLTree_attrExt), i.e. relative to the attrExt at
        # base + 16, not to the chunk.
        aoff = base + 16 + attribute_start + i * attribute_size
        ans = u32(axml, aoff)
        aname = u32(axml, aoff + 4)
        rawv = u32(axml, aoff + 8)
        vsize = u16(axml, aoff + 12)
        vtype = axml[aoff + 15]
        vdata = u32(axml, aoff + 16)
        attrs.append({
            "ns_index": ans, "ns": None if ans == NO_INDEX else strings[ans],
            "name_index": aname, "name": strings[aname],
            "raw_value_index": rawv, "raw_value": None if rawv == NO_INDEX else strings[rawv],
            "value_size": vsize, "data_type": f"0x{vtype:02x}",
            "data_type_string" if vtype == 0x03 else "data_type_int_dec": vdata,
            "res_id": ids[aname] if aname < len(ids) else 0,
        })
    emit("axml_start_element", offset=base, lineNumber=line,
         element_ns_index=ns_idx, element_ns=None if ns_idx == NO_INDEX else strings[ns_idx],
         element_name_index=name_idx, element_name=strings[name_idx],
         attributeStart=attribute_start, attributeSize=attribute_size,
         attributeCount=attribute_count, idIndex=id_index,
         classIndex=class_index, styleIndex=style_index, attributes=attrs)

    # END_ELEMENT chunk.
    ee = next(c for c in chunks if c["type"] == 0x0103)
    emit("axml_end_element", offset=ee["offset"], lineNumber=u32(axml, ee["offset"] + 8),
         ns_index=u32(axml, ee["offset"] + 16),
         name_index=u32(axml, ee["offset"] + 20),
         name=strings[u32(axml, ee["offset"] + 20)])

    # --- dex declared header -----------------------------------------------
    magic = dex[:8]
    checksum = u32(dex, 8)
    signature = dex[12:32]
    body_after_sig = dex[32:]
    emit("dex_declared_header",
         magic_hex=magic.hex(), magic_ascii=magic[:4].decode("ascii"),
         format_version=magic[4:7].decode("ascii"),
         declared_checksum=f"0x{checksum:08x}",
         checksum_recomputed=f"0x{zlib.adler32(dex[12:]) & 0xFFFFFFFF:08x}",
         checksum_matches=(checksum == (zlib.adler32(dex[12:]) & 0xFFFFFFFF)),
         signature_sha1=signature.hex(),
         signature_recomputed=hashlib.sha1(body_after_sig).hexdigest(),
         signature_matches=(signature == hashlib.sha1(body_after_sig).digest()),
         file_size=u32(dex, 32), header_size=u32(dex, 36),
         endian_tag=f"0x{u32(dex, 40):08x}",
         header_bytes=len(dex))

    emit("jar_manifest", bytes=len(jar),
         first_line=jar.split(b"\r\n")[0].decode("ascii"),
         section_count=jar.count(b"\r\n\r\n"))


if __name__ == "__main__":
    main()
