#!/usr/bin/env python3
"""Blind (independent) PE/CLI managed-assembly metadata parser.

Written from the ECMA-335 partition II (metadata) and partition III/PE layout
knowledge by the reviewer seat; it does not import or consult any lane script,
record, or fixture truth file. It reads only the fixture bytes given on the
command line and prints what it derives.
"""
import hashlib
import struct
import sys

TABLE_NAMES = {
    0x00: "Module", 0x01: "TypeRef", 0x02: "TypeDef", 0x03: "FieldPtr",
    0x04: "Field", 0x05: "MethodPtr", 0x06: "MethodDef", 0x07: "ParamPtr",
    0x08: "Param", 0x09: "InterfaceImpl", 0x0A: "MemberRef", 0x0B: "Constant",
    0x0C: "CustomAttribute", 0x0D: "FieldMarshal", 0x0E: "DeclSecurity",
    0x0F: "ClassLayout", 0x10: "FieldLayout", 0x11: "StandAloneSig",
    0x12: "EventMap", 0x13: "EventPtr", 0x14: "Event", 0x15: "PropertyMap",
    0x16: "PropertyPtr", 0x17: "Property", 0x18: "MethodSemantics",
    0x19: "MethodImpl", 0x1A: "ModuleRef", 0x1B: "TypeSpec", 0x1C: "ImplMap",
    0x1D: "FieldRVA", 0x1E: "ENCLog", 0x1F: "ENCMap", 0x20: "Assembly",
    0x21: "AssemblyProcessor", 0x22: "AssemblyOS", 0x23: "AssemblyRef",
    0x24: "AssemblyRefProcessor", 0x25: "AssemblyRefOS", 0x26: "File",
    0x27: "ExportedType", 0x28: "ManifestResource", 0x29: "NestedClass",
    0x2A: "GenericParam", 0x2B: "MethodSpec", 0x2C: "GenericParamConstraint",
}

CODED_GROUPS = {
    "TypeDefOrRef": [0x02, 0x01, 0x1B],
    "HasConstant": [0x04, 0x08, 0x17],
    "HasCustomAttribute": [0x06, 0x04, 0x01, 0x02, 0x08, 0x09, 0x0A, 0x00,
                           0x0E, 0x17, 0x14, 0x11, 0x1A, 0x1B, 0x20, 0x23,
                           0x26, 0x27, 0x28, 0x2A, 0x2C, 0x2B],
    "HasFieldMarshal": [0x04, 0x08],
    "HasDeclSecurity": [0x02, 0x06, 0x20],
    "MemberRefParent": [0x02, 0x01, 0x1A, 0x06, 0x1B],
    "HasSemantics": [0x14, 0x17],
    "MethodDefOrRef": [0x06, 0x0A],
    "MemberForwarded": [0x04, 0x06],
    "Implementation": [0x26, 0x23, 0x27],
    "CustomAttributeType": [None, None, 0x06, 0x0A, None],
    "ResolutionScope": [0x00, 0x1A, 0x23, 0x01],
    "TypeOrMethodDef": [0x02, 0x06],
}

# column spec: (name, kind); kind is 'u1'|'u2'|'u4'|'S'|'G'|'B'
# | ('T', table_id) simple index | ('C', coded_group)
SCHEMAS = {
    0x00: [("Generation", "u2"), ("Name", "S"), ("Mvid", "G"), ("EncId", "G"), ("EncBaseId", "G")],
    0x01: [("ResolutionScope", ("C", "ResolutionScope")), ("TypeName", "S"), ("TypeNamespace", "S")],
    0x02: [("Flags", "u4"), ("TypeName", "S"), ("TypeNamespace", "S"), ("Extends", ("C", "TypeDefOrRef")),
           ("FieldList", ("T", 0x04)), ("MethodList", ("T", 0x06))],
    0x03: [("Field", ("T", 0x04))],
    0x04: [("Flags", "u2"), ("Name", "S"), ("Signature", "B")],
    0x05: [("Method", ("T", 0x06))],
    0x06: [("RVA", "u4"), ("ImplFlags", "u2"), ("Flags", "u2"), ("Name", "S"), ("Signature", "B"),
           ("ParamList", ("T", 0x08))],
    0x07: [("Param", ("T", 0x08))],
    0x08: [("Flags", "u2"), ("Sequence", "u2"), ("Name", "S")],
    0x09: [("Class", ("T", 0x02)), ("Interface", ("C", "TypeDefOrRef"))],
    0x0A: [("Class", ("C", "MemberRefParent")), ("Name", "S"), ("Signature", "B")],
    0x0B: [("Type", "u1"), ("Padding", "u1"), ("Parent", ("C", "HasConstant")), ("Value", "B")],
    0x0C: [("Parent", ("C", "HasCustomAttribute")), ("Type", ("C", "CustomAttributeType")), ("Value", "B")],
    0x0D: [("Parent", ("C", "HasFieldMarshal")), ("NativeType", "B")],
    0x0E: [("Action", "u2"), ("Parent", ("C", "HasDeclSecurity")), ("PermissionSet", "B")],
    0x0F: [("PackingSize", "u2"), ("ClassSize", "u4"), ("Parent", ("T", 0x02))],
    0x10: [("Offset", "u4"), ("Field", ("T", 0x04))],
    0x11: [("Signature", "B")],
    0x12: [("Parent", ("T", 0x02)), ("EventList", ("T", 0x14))],
    0x13: [("Event", ("T", 0x14))],
    0x14: [("EventFlags", "u2"), ("Name", "S"), ("EventType", ("C", "TypeDefOrRef"))],
    0x15: [("Parent", ("T", 0x02)), ("PropertyList", ("T", 0x17))],
    0x16: [("Property", ("T", 0x17))],
    0x17: [("Flags", "u2"), ("Name", "S"), ("Type", "B")],
    0x18: [("Semantics", "u2"), ("Method", ("T", 0x06)), ("Association", ("C", "HasSemantics"))],
    0x19: [("Class", ("T", 0x02)), ("MethodBody", ("C", "MethodDefOrRef")),
           ("MethodDeclaration", ("C", "MethodDefOrRef"))],
    0x1A: [("Name", "S")],
    0x1B: [("Signature", "B")],
    0x1C: [("MappingFlags", "u2"), ("MemberForwarded", ("C", "MemberForwarded")), ("ImportName", "S"),
           ("ImportScope", ("T", 0x1A))],
    0x1D: [("RVA", "u4"), ("Field", ("T", 0x04))],
    0x1E: [("Token", "u4"), ("FuncCode", "u4")],
    0x1F: [("Token", "u4")],
    0x20: [("HashAlgId", "u4"), ("MajorVersion", "u2"), ("MinorVersion", "u2"), ("BuildNumber", "u2"),
           ("RevisionNumber", "u2"), ("Flags", "u4"), ("PublicKey", "B"), ("Name", "S"), ("Culture", "S")],
    0x21: [("Processor", "u4")],
    0x22: [("OSPlatformID", "u4"), ("OSMajorVersion", "u4"), ("OSMinorVersion", "u4")],
    0x23: [("MajorVersion", "u2"), ("MinorVersion", "u2"), ("BuildNumber", "u2"), ("RevisionNumber", "u2"),
           ("Flags", "u4"), ("PublicKeyOrToken", "B"), ("Name", "S"), ("Culture", "S"), ("HashValue", "B")],
    0x24: [("Processor", "u4"), ("AssemblyRef", ("T", 0x23))],
    0x25: [("OSPlatformID", "u4"), ("OSMajorVersion", "u4"), ("OSMinorVersion", "u4"),
           ("AssemblyRef", ("T", 0x23))],
    0x26: [("Flags", "u4"), ("Name", "S"), ("HashValue", "B")],
    0x27: [("Flags", "u4"), ("TypeDefID", "u4"), ("TypeName", "S"), ("TypeNamespace", "S"),
           ("Implementation", ("C", "Implementation"))],
    0x28: [("Offset", "u4"), ("Flags", "u4"), ("Name", "S"), ("Implementation", ("C", "Implementation"))],
    0x29: [("NestedClass", ("T", 0x02)), ("EnclosingClass", ("T", 0x02))],
    0x2A: [("Number", "u2"), ("Flags", "u2"), ("Owner", ("C", "TypeOrMethodDef")), ("Name", "S")],
    0x2B: [("Method", ("C", "MethodDefOrRef")), ("Instantiation", "B")],
    0x2C: [("Owner", ("T", 0x2A)), ("Constraint", ("C", "TypeDefOrRef"))],
}


def rva_to_off(sections, rva):
    for va, vsize,praw, rsize in sections:
        span = max(vsize, rsize)
        if va <= rva < va + span:
            return rva - va + praw
    return None


def u16(b, o): return struct.unpack_from("<H", b, o)[0]
def u32(b, o): return struct.unpack_from("<I", b, o)[0]


def parse(path):
    out = []
    p = out.append
    data = open(path, "rb").read()
    p(f"file: {path}")
    p(f"file_size: {len(data)} bytes")
    p(f"file_sha256: {hashlib.sha256(data).hexdigest()}")

    if data[:2] != b"MZ":
        p("!! not MZ"); return out
    e_lfanew = u32(data, 0x3C)
    p(f"dos_e_lfanew: 0x{e_lfanew:x} ({e_lfanew})")
    if data[e_lfanew:e_lfanew + 4] != b"PE\x00\x00":
        p("!! no PE signature"); return out
    pe = e_lfanew + 4
    machine = u16(data, pe)
    nsec = u16(data, pe + 2)
    size_opt = u16(data, pe + 16)
    chars = u16(data, pe + 18)
    mach = {0x014C: "I386", 0x8664: "AMD64", 0xAA64: "ARM64", 0x01C0: "ARM",
            0x01C4: "ARMNT", 0x0200: "IA64"}.get(machine, f"0x{machine:04x}")
    p(f"coff_machine: {mach} (0x{machine:04x})")
    p(f"coff_number_of_sections: {nsec}")
    p(f"coff_size_of_optional_header: {size_opt}")
    p(f"coff_characteristics: 0x{chars:04x}")

    opt = pe + 20
    magic = u16(data, opt)
    magic_name = {0x10B: "PE32 (0x10b)", 0x20B: "PE32+ (0x20b)"}.get(magic, f"0x{magic:04x}")
    p(f"optional_header_magic: {magic_name}")
    is_pe32p = magic == 0x20B
    ndir_off = opt + (108 if is_pe32p else 92)
    dd_off = opt + (112 if is_pe32p else 96)
    ndir = u32(data, ndir_off)
    p(f"number_of_rva_and_sizes: {ndir}")
    dd_names = ["Export", "Import", "Resource", "Exception", "Certificate", "BaseReloc",
                "Debug", "Architecture", "GlobalPtr", "TLS", "LoadConfig", "BoundImport",
                "IAT", "DelayImport", "CLR", "Reserved"]
    dirs = {}
    for i in range(ndir):
        va = u32(data, dd_off + 8 * i)
        sz = u32(data, dd_off + 8 * i + 4)
        if va or sz:
            dirs[dd_names[i]] = (va, sz)
            p(f"data_dir[{i}] {dd_names[i]}: rva=0x{va:x} size=0x{sz:x}")

    secoff = opt + size_opt
    sections = []
    for i in range(nsec):
        o = secoff + 40 * i
        name = data[o:o + 8].rstrip(b"\x00").decode("ascii", "replace")
        vsize, va, rsize, praw = struct.unpack_from("<IIII", data, o + 8)
        sections.append((va, vsize, praw, rsize))
        p(f"section[{i}] {name!r}: va=0x{va:x} vsize=0x{vsize:x} raw=0x{praw:x} rawsize=0x{rsize:x}")

    if "CLR" not in dirs:
        p("!! no CLR runtime header directory: not a managed image")
        return out
    clr_rva, clr_size = dirs["CLR"]
    cli_off = rva_to_off(sections, clr_rva)
    p(f"cli_header_present: yes")
    p(f"cli_header_rva: 0x{clr_rva:x}")
    p(f"cli_header_file_offset: 0x{cli_off:x} ({cli_off})")
    p(f"cli_directory_size: 0x{clr_size:x} ({clr_size})")
    cb = u32(data, cli_off)
    mjr, mnr = u16(data, cli_off + 4), u16(data, cli_off + 6)
    md_rva, md_size = u32(data, cli_off + 8), u32(data, cli_off + 12)
    flags = u32(data, cli_off + 16)
    ep = u32(data, cli_off + 20)
    p(f"cli_header_cb: 0x{cb:x} ({cb})")
    p(f"cli_runtime_version: {mjr}.{mnr}")
    p(f"cli_flags: 0x{flags:08x}")
    p(f"cli_entrypoint_token: 0x{ep:08x}")
    md_off = rva_to_off(sections, md_rva)
    p(f"metadata_rva: 0x{md_rva:x}")
    p(f"metadata_file_offset: 0x{md_off:x} ({md_off})")
    p(f"metadata_size: 0x{md_size:x} ({md_size})")

    sig = u32(data, md_off)
    p(f"metadata_root_signature: 0x{sig:08x} ({data[md_off:md_off+4]!r})")
    m_maj, m_min = u16(data, md_off + 4), u16(data, md_off + 6)
    vlen = u32(data, md_off + 12)
    ver = data[md_off + 16: md_off + 16 + vlen].rstrip(b"\x00").decode("ascii", "replace")
    p(f"metadata_version: {m_maj}.{m_min}")
    p(f"metadata_version_string_len: {vlen}")
    p(f"metadata_version_string: {ver!r}")
    o = md_off + 16 + vlen
    md_flags, nstreams = u16(data, o), u16(data, o + 2)
    o += 4
    p(f"metadata_flags: 0x{md_flags:04x}")
    p(f"metadata_stream_count: {nstreams}")
    streams = {}
    for i in range(nstreams):
        so, ss = u32(data, o), u32(data, o + 4)
        o += 8
        nstart = o
        while data[o] != 0:
            o += 1
        name = data[nstart:o].decode("ascii", "replace")
        o += 1
        o = nstart + ((o - nstart + 3) & ~3)
        streams[name] = (so, ss)
        p(f"stream[{i}] {name!r}: offset_from_metadata_root=0x{so:x} ({so}) size=0x{ss:x} ({ss})")

    if "#~" not in streams and "#-" not in streams:
        p("!! no #~ or #- table stream")
        return out
    tname = "#~" if "#~" in streams else "#-"
    t_off = md_off + streams[tname][0]
    u32(data, t_off)  # reserved
    t_maj, t_min = data[t_off + 4], data[t_off + 5]
    heapsz = data[t_off + 6]
    valid = struct.unpack_from("<Q", data, t_off + 8)[0]
    sortedm = struct.unpack_from("<Q", data, t_off + 16)[0]
    p(f"table_stream: {tname} at file offset 0x{t_off:x}")
    p(f"table_stream_version: {t_maj}.{t_min}")
    p(f"heap_sizes_byte: 0x{heapsz:02x} (strings4={bool(heapsz&1)} guid4={bool(heapsz&2)} blob4={bool(heapsz&4)})")
    s_idx = 4 if heapsz & 1 else 2
    g_idx = 4 if heapsz & 2 else 2
    b_idx = 4 if heapsz & 4 else 2
    p(f"valid_mask: 0x{valid:016x}")
    p(f"sorted_mask: 0x{sortedm:016x}")
    present = [t for t in range(64) if valid >> t & 1]
    rows = {}
    ro = t_off + 24
    for t in present:
        rows[t] = u32(data, ro)
        ro += 4
    for t in present:
        p(f"rowcount[{TABLE_NAMES.get(t, f'table_{t:#04x}')} (0x{t:02x})]: {rows[t]}")

    def col_size(kind):
        if kind == "u1": return 1
        if kind == "u2": return 2
        if kind == "u4": return 4
        if kind == "S": return s_idx
        if kind == "G": return g_idx
        if kind == "B": return b_idx
        if kind[0] == "T":
            return 2 if rows.get(kind[1], 0) < (1 << 16) else 4
        grp = CODED_GROUPS[kind[1]]
        bits = max(1, (len(grp) - 1).bit_length())
        mx = max(rows.get(t, 0) for t in grp if t is not None)
        return 2 if mx < (1 << (16 - bits)) else 4

    table_data = {}
    for t in present:
        size = sum(col_size(k) for _, k in SCHEMAS[t])
        table_data[t] = (ro, size)
        if rows[t]:
            ro += size * rows[t]
    p("table_row_sizes:")
    for t in present:
        p(f"  {TABLE_NAMES.get(t, hex(t))} (0x{t:02x}): {table_data[t][1]} bytes/row at 0x{table_data[t][0]:x}")

    def get_str(idx):
        s = md_off + streams["#Strings"][0] + idx
        e = s
        while data[e] != 0:
            e += 1
        return data[s:e].decode("utf-8", "replace")

    def read_row(t, i):
        base = table_data[t][0] + i * table_data[t][1]
        vals, off = {}, base
        for name, kind in SCHEMAS[t]:
            n = col_size(kind)
            raw = data[off:off + n]
            if kind == "u1": vals[name] = raw[0]
            elif kind in ("u2", "u4"):
                vals[name] = int.from_bytes(raw, "little")
            else:
                vals[name] = int.from_bytes(raw, "little")
            vals["_" + name + "_hex"] = raw.hex()
            off += n
        return vals

    if rows.get(0x00):
        m = read_row(0x00, 0)
        mvid_idx = m["Mvid"]
        g0 = md_off + streams["#GUID"][0]
        gsize = g_idx
        gbytes = data[g0 + (mvid_idx - 1) * 16: g0 + mvid_idx * 16] if mvid_idx else b""
        p(f"module[1]: generation={m['Generation']} name={get_str(m['Name'])!r} mvid_index={mvid_idx} mvid_guid={gbytes.hex()}")
    if rows.get(0x20):
        a = read_row(0x20, 0)
        p(f"assembly[1]: hash_alg_id=0x{a['HashAlgId']:08x} version={a['MajorVersion']}.{a['MinorVersion']}.{a['BuildNumber']}.{a['RevisionNumber']} flags=0x{a['Flags']:08x}")
        p(f"assembly_name: {get_str(a['Name'])!r}")
        p(f"assembly_culture: {get_str(a['Culture'])!r}")
    if rows.get(0x02):
        for i in range(rows[0x02]):
            td = read_row(0x02, i)
            ns = get_str(td["TypeNamespace"])
            nm = get_str(td["TypeName"])
            full = f"{ns}.{nm}" if ns else nm
            p(f"typedef[{i+1}]: {full!r} flags=0x{td['Flags']:08x} field_list={td['FieldList']} method_list={td['MethodList']}")
    if rows.get(0x06):
        for i in range(rows[0x06]):
            md = read_row(0x06, i)
            p(f"methoddef[{i+1}]: rva=0x{md['RVA']:x} name={get_str(md['Name'])!r} implflags=0x{md['ImplFlags']:04x} flags=0x{md['Flags']:04x}")
    if rows.get(0x01):
        for i in range(rows[0x01]):
            tr = read_row(0x01, i)
            ns = get_str(tr["TypeNamespace"])
            nm = get_str(tr["TypeName"])
            full = f"{ns}.{nm}" if ns else nm
            p(f"typeref[{i+1}]: {full!r}")
    if rows.get(0x1A):
        for i in range(rows[0x1A]):
            mr = read_row(0x1A, i)
            p(f"moduleref[{i+1}]: name={get_str(mr['Name'])!r}")
    if rows.get(0x1C):
        for i in range(rows[0x1C]):
            im = read_row(0x1C, i)
            mf_tag, mf_idx = im["MemberForwarded"] & 1, im["MemberForwarded"] >> 1
            mf = f"{'MethodDef' if mf_tag == 1 else 'Field'},{mf_idx}"
            sc = im["ImportScope"]
            p(f"implmap[{i+1}]: mapping_flags=0x{im['MappingFlags']:04x} member_forwarded=({mf}) import_name={get_str(im['ImportName'])!r} import_scope=moduleref[{sc}]")
    return out


def main():
    lines = []
    for path in sys.argv[1:]:
        lines.extend(parse(path))
        lines.append("=" * 72)
    text = "\n".join(lines)
    print(text)


if __name__ == "__main__":
    main()
