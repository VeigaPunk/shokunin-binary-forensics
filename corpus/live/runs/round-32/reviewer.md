# Round 32 independent byte review

**Verdict: PASS for this fixture, with bounded scope.** Independent static PE parsing of `pe-r32/fixture.exe` (not `truth.json`, and not the REA producer) finds exactly two resource leaves. Both appear in `inspection.json` under Evidence ID `ev_dcc2411a94ff88169c18f1db3d70ad0792bbccb059dec89bec0df3a578ef653d` with matching type/name/language, directory and entry locations, data-entry location, payload RVA/file range/SHA-256, and code page/reserved fields. The artifact SHA-256 and 1,024-byte length also match. Precision **2/2 = 100%**, recall **2/2 = 100%** on resource identities, with **0 mismatches** on compared byte locations and digests. This is a fixture-level result, not a general PE-parser accuracy estimate.

## Independent observations

- DOS `e_lfanew` at `0x3c` points to PE header `0x40`; machine `0x014c`, optional magic `0x010b` (PE32). Resource data-directory entry at file offset `0xc8` is RVA `0x2000`, size `0xf0`. The sole `.rsrc` section maps RVA `0x2000` to file `0x200`, hence the resource tree starts at file `0x200`.
- Resource directories occupy `(offset,length,named,id)` = `(0x200,24,0,1)`, `(0x218,32,1,1)`, `(0x238,24,0,1)`, `(0x250,24,0,1)`. There are five tree-entry records across these directories (`1+2+1+1`), and two terminal payloads. The observed directory and leaf counts agree with the report's `coverage.status=complete`, `examined_entries=5`, `resources=2` **for this bounded tree**.
- Leaf 0: type ID `10`, name **ALPHA**, language ID `1036`; entry record offsets `0x210,0x228,0x248` (8 bytes each); data entry `0x268` (16 bytes); payload RVA `0x20a0`, file offset `0x2a0`, 15 bytes, SHA-256 `071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229`; code page/reserved both zero. At `0x228`, high bit of name word selects the name record at `0x2e0`: a **2-byte little-endian UTF-16 code-unit count of 5**, then 10 bytes `41004c00500048004100`, decoding to `ALPHA`. The name's complete length-prefixed range is `[0x2e0,0x2ec)` (12 bytes), as reported; those ten bytes alone are the report's `utf16le_hex`. No NUL terminator is part of the counted name.
- Leaf 1: type ID `10`, numeric name ID `3`, language ID `1033`; entry record offsets `0x210,0x230,0x260`; data entry `0x278`; payload RVA `0x20c0`, file offset `0x2c0`, 15 bytes, SHA-256 `cc29ca16da56975bf9fb034fbc010e377076ada5df6395622c8ffd9fed19f67e`; code page/reserved zero. The report correctly does **not** mistake ID 3 for a string name.
- `pe-r31/fixture.exe` is independently SHA-256 `714369ff1bfcd2e04a5f6c32f938778b38c6c455ae6a019b51e6c2d702510b47` (also 1,024 bytes). Its first leaf is numeric name ID `2`, not `ALPHA`; the second leaf's identity and both payload digests are unchanged. Exactly 12 bytes differ at offsets `0xcc,0x140,0x224,0x226,0x228,0x22b,0x2e0,0x2e2,0x2e4,0x2e6,0x2e8,0x2ea`: the resource section virtual size and resource data-directory size grow `0xd0→0xf0`; type directory named/id counts change `0/2→1/1`; first name entry changes from ID 2 to high-bit string-reference `0x800000e0`; the new length-prefixed name occupies previously zero bytes at `0x2e0`. These are **shipped fixture byte differences**, not a claim about unprovided fixture-generation source code (`pe-r32` contains only `fixture.exe` and `truth.json`).

## Reproduce without producer, oracle, or target execution

Save the following as `/tmp/check-pe-r32-review.py` and run `python /tmp/check-pe-r32-review.py`; it reads the two PE files and round-32 inspection JSON. It never reads `truth.json` or invokes REA. The decoder follows data-directory and section mapping rather than using fixed resource offsets.

```python
from pathlib import Path
import hashlib, struct
root = Path("/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/fixtures")
def decode(path):
    b = path.read_bytes()
    u16 = lambda o: struct.unpack_from("<H", b, o)[0]
    u32 = lambda o: struct.unpack_from("<I", b, o)[0]
    pe = u32(0x3c)
    assert b[pe:pe+4] == b"PE\0\0"
    coff = pe+4
    machine, nsects, optsize = u16(coff), u16(coff+2), u16(coff+16)
    opt = coff+20
    magic = u16(opt)
    assert magic in (0x10b, 0x20b)
    dd = opt+(96 if magic == 0x10b else 112)+2*8
    rva, size = u32(dd), u32(dd+4)
    sections = []
    for i in range(nsects):
        s = opt+optsize+40*i
        sections.append((b[s:s+8].rstrip(b"\0").decode(),u32(s+12),u32(s+8),u32(s+20),u32(s+16)))
    def fileoff(r):
        matches = [(p+r-v,n) for n,v,vs,p,rs in sections if v <= r < v+max(vs,rs) and r-v < rs]
        assert len(matches) == 1, (r, matches)
        return matches[0][0]
    base = fileoff(rva)
    directories = []
    leaves = []
    def walk(rel, ancestors, entries):
        off = base+rel
        named, numeric = u16(off+12),u16(off+14)
        directories.append((off, 16+8*(named+numeric),named,numeric))
        for i in range(named+numeric):
            e = off+16+8*i
            raw, dest = u32(e),u32(e+4)
            if raw & 0x80000000:
                no = base+(raw & 0x7fffffff)
                count = u16(no)
                name_bytes = b[no+2:no+2+count*2]
                assert len(name_bytes) == count*2
                identity = ("name",name_bytes.decode("utf-16le"),name_bytes.hex(),no,2+count*2)
            else:
                identity = ("id",raw)
            path = ancestors+[identity]
            refs = entries+[e]
            if dest & 0x80000000:
                walk(dest & 0x7fffffff,path,refs)
            else:
                de = base+dest
                data_rva,data_size,codepage,reserved = struct.unpack_from("<IIII",b,de)
                start=fileoff(data_rva)
                payload=b[start:start+data_size]
                assert len(path) == 3 and len(payload) == data_size
                leaves.append(dict(identity=path,entry_offsets=refs,data_entry=de,
                    payload_rva=data_rva,payload_offset=start,payload_bytes=data_size,
                    payload_sha256=hashlib.sha256(payload).hexdigest(),code_page=codepage,reserved=reserved))
    walk(0,[],[])
    return dict(path=str(path),size=len(b),sha256=hashlib.sha256(b).hexdigest(),
        pe=pe,machine=machine,optional_magic=hex(magic),data_directory_offset=dd,
        resource_rva=rva,resource_size=size,resource_offset=base,sections=sections,
        directories=directories,leaves=leaves)
for v in ("pe-r31", "pe-r32"):
    print(v, decode(root/v/"fixture.exe"))

import json
r = decode(root/"pe-r32"/"fixture.exe")
old = decode(root/"pe-r31"/"fixture.exe")
report_path = root.parent/"live/runs/round-32/inspection.json"
inspection = json.loads(report_path.read_text())
n = inspection["normalized_result"]
assert inspection["evidence_id"] == "ev_dcc2411a94ff88169c18f1db3d70ad0792bbccb059dec89bec0df3a578ef653d"
assert n["artifact"]["sha256"] == r["sha256"] and n["artifact"]["bytes"] == r["size"]
assert n["machine"] == r["machine"] and n["format"] == "pe32"
assert n["directory"] == {"rva":r["resource_rva"],"location":{"offset":r["resource_offset"],"bytes":r["resource_size"]},"data_directory_location":{"offset":r["data_directory_offset"],"bytes":8}}
assert [(x["location"]["offset"],x["location"]["bytes"],x["named_entries"],x["id_entries"]) for x in n["directories"]] == r["directories"]
assert len(r["leaves"]) == len(n["resources"]) == 2
for leaf, rec in zip(r["leaves"],n["resources"]):
    for part,key in zip(leaf["identity"],("type","name","language")):
        expect = {"kind":part[0],("name" if part[0]=="name" else "id"):part[1]}
        if part[0] == "name": expect.update(utf16le_hex=part[2],location={"offset":part[3],"bytes":part[4]})
        assert rec[key] == expect, (key,rec[key],expect)
    assert rec["entry_locations"] == [{"offset":o,"bytes":8} for o in leaf["entry_offsets"]]
    assert rec["data_entry_location"] == {"offset":leaf["data_entry"],"bytes":16}
    assert rec["payload"] == {"rva":leaf["payload_rva"],"location":{"offset":leaf["payload_offset"],"bytes":leaf["payload_bytes"]},"sha256":leaf["payload_sha256"]}
    assert rec["code_page"] == leaf["code_page"] and rec["reserved"] == leaf["reserved"]
assert old["leaves"][0]["identity"][1] == ("id",2)
assert r["leaves"][0]["identity"][1] == ("name","ALPHA","41004c00500048004100",736,12)
assert old["leaves"][1] == r["leaves"][1]
assert [x["payload_sha256"] for x in old["leaves"]] == [x["payload_sha256"] for x in r["leaves"]]
print("PASS: two independently decoded leaves; all identity/location/digest fields match")
```

**Scope and limits:** This is passive static inventory, not executable behavior, string use, locale fallback, icon selection, or payload interpretation; both blobs remain opaque. The result establishes no general precision/recall on other PEs, malformed trees, Unicode edge cases, or repeated names. `coverage.status=complete` is supported only for the parsed fixture tree. Evidence ID identifies the producer record; the independent byte observations above are separate corroboration and do not turn producer claims into runtime observations.
