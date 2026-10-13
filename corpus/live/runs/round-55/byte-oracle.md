# Round 55 PE byte-oracle review

**Independent result:** the bytes agree with the round-55 truth for the PE32+ resource directory, the named group key, all three leaf payloads, and the ordered group-image candidates. I found no mismatch. This review parses bytes directly; it does not use the truth JSON to locate structures, does not use REA output, and does not execute the PE.

## Reproduction method

From the repository root, run the following with Python 3. The paths are fixed to the checked-in fixtures. It reads the PE header, maps the resource RVA through section headers, walks the resource directory entries, reads each data entry, hashes payload bytes, then decodes the group-icon records and matches their declared byte sizes to RT_ICON leaves. The truth files are read only at the end for comparisons.

```python
from pathlib import Path
import hashlib, json, struct
root = Path(".shokunin/revenger/corpus/fixtures")
p = root / "pe-r55/fixture.exe"
b = p.read_bytes()
b42 = (root / "pe-r42/fixture.exe").read_bytes()
t = json.loads((root / "pe-r55/truth.json").read_text())
t42 = json.loads((root / "pe-r42/truth.json").read_text())
u16 = lambda o: struct.unpack_from("<H", b, o)[0]
u32 = lambda o: struct.unpack_from("<I", b, o)[0]
pe = u32(0x3c)
assert b[:2] == b"MZ" and b[pe:pe+4] == b"PE\0\0"
machine, nsec = struct.unpack_from("<HH", b, pe+4)
optsz = struct.unpack_from("<H", b, pe+20)[0]
opt = pe + 24
assert u16(opt) == 0x20b                 # PE32+
rva, declared = struct.unpack_from("<II", b, opt+112+16) # data directory 2
secs=[]
for i in range(nsec):
    s=opt+optsz+40*i
    name=b[s:s+8].rstrip(b"\0")
    vs, va, rawsz, raw = struct.unpack_from("<IIII", b, s+8)
    secs.append((name,va,vs,raw,rawsz))
def map_rva(x):
    for name,va,vs,raw,rawsz in secs:
        if va <= x < va+max(vs,rawsz): return raw+x-va
    raise ValueError(f"unmapped RVA {x:#x}")
base=map_rva(rva)
def directory(rel):
    o=base+rel
    named, ids=struct.unpack_from("<HH",b,o+12)
    result=[]
    for i in range(named+ids):
        e=o+16+8*i
        key,val=struct.unpack_from("<II",b,e)
        if key>>31:
            no=base+(key&0x7fffffff); n=u16(no)
            k=("name", b[no+2:no+2+2*n].decode("utf-16le"), no, n)
        else: k=("id",key,None,None)
        result.append((k,val))
    return result
leaves=[]
for typ, child in directory(0):
    assert child>>31
    for name, langptr in directory(child&0x7fffffff):
        assert langptr>>31
        for lang, dataptr in directory(langptr&0x7fffffff):
            assert not dataptr>>31
            de=base+(dataptr&0x7fffffff)
            data_rva,size,cp=struct.unpack_from("<III",b,de)
            off=map_rva(data_rva); payload=b[off:off+size]
            leaves.append((typ,name,lang,off,size,hashlib.sha256(payload).hexdigest(),payload))
print("PE",len(b),hashlib.sha256(b).hexdigest(),hex(machine),"resource",hex(rva),base,declared)
for typ,name,lang,off,size,digest,_ in leaves:
    print("leaf",typ,name,lang,off,size,digest)
group=next(x for x in leaves if x[0][:2]==("id",14))
g=group[-1]
reserved,typid,count=struct.unpack_from("<HHH",g,0)
records=[struct.unpack_from("<BBBBHHIH",g,6+14*i) for i in range(count)]
print("group records",records)
icons=[x for x in leaves if x[0][:2]==("id",3)]
for rec in records:
    group_id=rec[-1]; size=rec[-2]
    candidates=[(i,x[1][1],x[4],x[5]) for i,x in enumerate(icons) if x[4]==size]
    print("group id",group_id,"declared size",size,"same-language icon candidates",candidates)
print("truth checks",len(b)==t["size"],hashlib.sha256(b).hexdigest()==t["sha256"],
      len(b42)==t42["size"],hashlib.sha256(b42).hexdigest()==t["source_sha256"])
print("byte deltas",[(i,x,y) for i,(x,y) in enumerate(zip(b42,b)) if x!=y])
```

## Observations from bytes

- File is 1,536 bytes; SHA-256 `41c0132a9ecd8274d9afcfc079fefc0c5beb14c1ae81bc7bfa0a2832e140572b`. `e_lfanew=0x40`, signature `PE\0\0`, machine `0x8664` (AMD64), optional-header magic `0x20b` (PE32+), one `.rsrc` section (RVA `0x2000`, virtual size `1024`, raw offset `512`, raw size `1024`).
- Optional-header resource data-directory entry gives RVA `8192 (0x2000)`, declared size `240`. Mapping through `.rsrc` gives file offset `512`. Directory entries actually walk to type IDs 3 and 14. Type 3 contains numeric name IDs 1 and 2, each with language 1033. Type 14 has one **named** key, UTF-16LE `A😀B!`, then language 1033. Its length prefix is 5 UTF-16 code units; the encoded bytes at file offsets `[736,748)` are `41003dd800de42002100` (the supplementary character is the surrogate pair `3dd8 00de`). The group payload itself is named, so its name ID is null—not numeric ID 1.
- Independently traversed data entries point to three payloads: RT_ICON name 1/lang 1033 offset 768 length 48 SHA-256 `d7aaca7bc7951c9249a7798838189374fa953d3def03aebb375ee731768e5003`; RT_ICON name 2/lang 1033 offset 832 length 48 SHA-256 `2f503cace29956c75acd5356de2f8fa98485b01edd654daf0f81a739b44c82ae`; and RT_GROUP_ICON named `A😀B!`/lang 1033 offset 896 length 34 SHA-256 `45eb70319667352d8bfea3249f7fb30166c6835d2cf564b5ec303bf2d716c17a`. Hashes are over the exact bytes at the located file ranges.
- Group payload parses as reserved=0, type=1, count=2. Its two records, in order, name icon IDs 1 then 2 and declare byte sizes 48 then 48. Both icon leaves are language 1033; size matching therefore yields ordered candidate indices `[[0],[1]]` with both size matches true. Matching is by declared size and language here; the group’s image ID supplies the corresponding icon name ID.
- Compared bytewise to r42: same file size (1,536); r42 SHA-256 is `3ab5008b436eb4facd3966767a507fa4b1625160532585a09a6af2f752b38941`. Exactly 12 byte offsets differ: `(220,208→240)`, `(588,0→1)`, `(590,1→0)`, `(592,1→224)`, `(595,0→128)`, `(736,0→5)`, `(738,0→65)`, `(740,0→61)`, `(741,0→216)`, `(743,0→222)`, `(744,0→66)`, `(746,0→33)`. The resource data-directory size grows 208→240; group directory count/name pointer and the name string change. All three payload hashes match the independently parsed r42 payload hashes, and the group payload bytes match r42. Truth source SHA, file SHA/size, resource coordinates and size, name/value bytes, leaves, ordered IDs, and candidate expectations all agree with observations.

## Mismatches and limits

No truth-vs-bytes mismatch observed. The independent parser is purpose-built for this fixture: it assumes PE32+ directory layout and a straightforward section RVA mapping, and does not validate every PE structural constraint, malformed input behavior, checksums, or Windows loader semantics. Resource-tree traversal and hashes are byte-derived, not assertions about how a particular OS or icon API will display/render these icon images. No executable code was run.
