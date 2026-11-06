#!/usr/bin/env python3
"""ReviewerCapR100 independent minimal AXML parser (own code, not readout.py).

Parses the ZIP local entry for AndroidManifest.xml, then the AXML string pool,
resource map, START_NAMESPACE and START_ELEMENT attribute records directly from
bytes with struct. Prints JSON facts; exit 0 iff package/versionCode/versionName
match the --expect triple.
"""
import json
import struct
import sys
import zlib

NO_INDEX = 0xFFFFFFFF


def u16(b, o):
    return struct.unpack_from("<H", b, o)[0]


def u32(b, o):
    return struct.unpack_from("<I", b, o)[0]


def local_member(apk, name):
    """Return (payload_bytes) of a STORED local entry found by scanning local headers."""
    with open(apk, "rb") as f:
        data = f.read()
    off = 0
    while off < len(data) - 4:
        if u32(data, off) != 0x04034B50:
            break
        nlen = u16(data, off + 26)
        elen = u16(data, off + 28)
        mname = data[off + 30: off + 30 + nlen].decode()
        csize = u32(data, off + 18)
        method = u16(data, off + 8)
        payload_off = off + 30 + nlen + elen
        payload = data[payload_off: payload_off + csize]
        if mname == name:
            if method == 0:
                return payload
            return zlib.decompress(payload, -15)
        off = payload_off + csize
    raise SystemExit(f"member not found: {name}")


def parse_string_pool(b, chunk_off):
    hdr_size = u16(b, chunk_off + 2)
    string_count = u32(b, chunk_off + 8)
    style_count = u32(b, chunk_off + 12)
    flags = u32(b, chunk_off + 16)
    strings_start = u32(b, chunk_off + 20)
    is_utf8 = bool(flags & 0x100)
    offsets = [u32(b, chunk_off + hdr_size + 4 * i) for i in range(string_count)]
    strings = []
    for so in offsets:
        p = chunk_off + strings_start + so
        if is_utf8:
            # lengths are u8 units; high bit => 2-byte big-endian long form
            def declen(pp):
                n = b[pp]
                if n & 0x80:
                    return ((n & 0x7F) << 8) | b[pp + 1], pp + 2
                return n, pp + 1
            nchars, p = declen(p)
            nbytes, p = declen(p)
            strings.append(b[p: p + nbytes].decode("utf-8"))
            assert len(strings[-1]) == nchars, (strings[-1], nchars)
        else:
            n = u16(b, p)
            p += 2
            strings.append(b[p: p + 2 * n].decode("utf-16-le"))
    return {
        "string_count": string_count,
        "style_count": style_count,
        "flags": flags,
        "utf8": is_utf8,
        "strings": strings,
    }


def main():
    apk = sys.argv[1]
    expect = json.loads(sys.argv[2])  # {"package":..,"versionCode":..,"versionName":..}
    axml = local_member(apk, "AndroidManifest.xml")
    facts = {"member_len": len(axml)}
    # walk chunks after the 8-byte ResXMLTree header
    off = 8
    pool = None
    resmap = None
    ns_start = None
    elem = None
    while off < len(axml):
        ctype = u16(axml, off)
        chdr = u16(axml, off + 2)
        csize = u32(axml, off + 4)
        if ctype == 0x0001:
            pool = parse_string_pool(axml, off)
        elif ctype == 0x0180:
            resmap = [u32(axml, off + 8 + 4 * i) for i in range((csize - 8) // 4)]
        elif ctype == 0x0100:  # START_NAMESPACE
            ns_start = {"prefix_idx": u32(axml, off + 16), "uri_idx": u32(axml, off + 20)}
        elif ctype == 0x0102:  # START_ELEMENT
            ns_idx = u32(axml, off + 16)
            name_idx = u32(axml, off + 20)
            attr_start = u16(axml, off + 24)
            attr_size = u16(axml, off + 26)
            attr_count = u16(axml, off + 28)
            attrs = []
            for i in range(attr_count):
                a = off + 16 + attr_start + i * attr_size
                ans = u32(axml, a)
                aname = u32(axml, a + 4)
                araw = u32(axml, a + 8)
                a_size = u16(axml, a + 12)
                a_res0 = axml[a + 14]
                a_type = axml[a + 15]
                a_data = u32(axml, a + 16)
                val = None
                if a_type == 0x03 and araw != NO_INDEX:
                    val = pool["strings"][araw]
                elif a_type == 0x10:
                    val = str(a_data)
                elif araw != NO_INDEX:
                    val = pool["strings"][araw]
                attrs.append({
                    "ns_idx": ans,
                    "ns": None if ans == NO_INDEX else pool["strings"][ans],
                    "name": pool["strings"][aname],
                    "name_idx": aname,
                    "raw_value_idx": araw,
                    "data_type": a_type,
                    "data": a_data,
                    "value": val,
                    "res_id": (resmap[aname] if resmap and aname < len(resmap) else None),
                })
            elem = {
                "name": pool["strings"][name_idx],
                "ns_idx": ns_idx,
                "attrs": attrs,
            }
        off += csize
    facts["pool"] = pool
    facts["resmap_nonzero"] = {pool["strings"][i]: hex(r) for i, r in enumerate(resmap or []) if r}
    facts["start_namespace"] = ns_start and {
        "prefix": pool["strings"][ns_start["prefix_idx"]],
        "uri": pool["strings"][ns_start["uri_idx"]],
    }
    facts["element"] = elem
    got = {}
    for a in (elem or {}).get("attrs", []):
        if a["name"] == "package":
            got["package"] = a["value"]
        if a["name"] == "versionCode":
            got["versionCode"] = a["value"]
        if a["name"] == "versionName":
            got["versionName"] = a["value"]
    facts["extracted"] = got
    ok = all(got.get(k) == v for k, v in expect.items())
    facts["MATCH"] = ok
    print(json.dumps(facts, indent=1, sort_keys=True))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
