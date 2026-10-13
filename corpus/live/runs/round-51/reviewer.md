# Round 51 — independent byte review

**PASS (bounded):** Independently decoded the 1,024-byte fixture, enumerated all reachable resource directories/entries, and matched both resource leaves and the saved `inspection.raw.json`. This is static artifact/record consistency, not PE execution or authentication of the producer.

- PE at `0x40`: AMD64 `0x8664`, one section, optional header `0x20b` (PE32+), `.rsrc` RVA `0x2000` → file offset `512`. PE32+ data-directory slot at file offset `216` declares resource RVA `0x2000`, length **240** (`0xf0`) at offset `220`. The PE32 source r34 has optional magic `0x10b`; r41 has `0x20b`. r51 header `[0:512]` equals r41 except byte `220` (`0xa0` → `0xf0`). r51 resource region `[512:1024]` equals r34 exactly.
- Reachable directories (absolute offset, size, named, numeric): `(512,24,0,1)`, `(536,32,1,1)`, `(568,24,0,1)`, `(592,24,0,1)`. Five traversed entries yield exactly two leaves, no other reachable directories or paths. Named type 10 entry at `528` routes through name entry `552`, language `1036` entry `584`, and data entry `616`: its name structure at `736:748` contains length `5`, UTF-16LE `41003dd800de42002100` (`A😀B!`, valid `D83D DE00` surrogate pair); payload RVA `0x20a0`/file `672:687`, 15 bytes, SHA-256 `071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229`. Numeric name `3` entry `560` routes to language `1033` entry `608` and data entry `632`; payload RVA `0x20c0`/file `704:719`, 15 bytes, SHA-256 `cc29ca16da56975bf9fb034fbc010e377076ada5df6395622c8ffd9fed19f67e`. The saved success reports these same paths, locations, hashes, and `complete` coverage (five entries/two resources).
- Failed input `attempt-directory160.exe` differs from successful r51 only at byte `220` (`0xa0` vs `0xf0`); its resource bytes and all pointers match. Its declared interval `[512,672)` excludes the resource-name pointer target `736`, whereas corrected `[512,752)` includes it. Saved `attempt-directory160.json` states `invalid_format` / “Resource directory offset leaves the declared resource interval.” **Byte-supported attribution:** the short declared interval is sufficient to explain that refusal for this fixture; no competing byte difference exists. The saved refusal/receipt alone cannot authenticate who produced the output or prove the internal decision path. `producer-receipt.json` hashes match the fixture and saved raw JSON, and its evidence ID matches, but it is only a local consistency receipt. No PE execution, loader behavior, or Unicode behavior beyond this literal was tested.

Read-only verifier (Python 3; prints PASS or raises `AssertionError`):

```python
from pathlib import Path
import hashlib, json, struct

base = Path('/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus')
run = base / 'live/runs/round-51'
r34, r41, r51 = (base / f'fixtures/pe-{r}/fixture.exe' for r in ('r34', 'r41', 'r51'))
a, c, x = (p.read_bytes() for p in (r34, r41, r51))
bad = (run / 'attempt-directory160.exe').read_bytes()
raw_bytes = (run / 'inspection.raw.json').read_bytes()
raw = json.loads(raw_bytes)
refusal = json.loads((run / 'attempt-directory160.json').read_bytes())
receipt = json.loads((run / 'producer-receipt.json').read_bytes())
sha = lambda v: hashlib.sha256(v).hexdigest()
U16 = lambda v, i: struct.unpack_from('<H', v, i)[0]
U32 = lambda v, i: struct.unpack_from('<I', v, i)[0]
assert len(a) == len(c) == len(x) == len(bad) == 1024
assert sha(x) == 'c890961ecfa1602b943ffbcbc03aa46af3d257effbf5eaa66483d0df6d0e32cf'
assert x[512:1024] == a[512:1024]
assert all(x[i] == c[i] for i in range(512) if i != 220)
assert [(i, bad[i], x[i]) for i in range(1024) if bad[i] != x[i]] == [(220, 160, 240)]
assert U16(a, U32(a, 60) + 24) == 0x10b
for blob in (x, bad):
    pe = U32(blob, 60)
    opt = pe + 24
    assert blob[:2] == b'MZ' and blob[pe:pe+4] == b'PE\0\0'
    assert U16(blob, pe+4) == 0x8664 and U16(blob, pe+6) == 1
    assert U16(blob, pe+20) == 240 and U16(blob, opt) == 0x20b
    assert U32(blob, opt+108) == 16 and opt+112+2*8 == 216
    assert U32(blob, 216) == 0x2000
    section = opt+240
    assert section == 328 and blob[section:section+8] == b'.rsrc\0\0\0'
    assert tuple(U32(blob, section+i) for i in (8, 12, 16, 20)) == (400, 0x2000, 512, 512)
assert U32(x, 220) == 240 and U32(bad, 220) == 160
# RVA translation follows this fixture's single resource section.
raw_offset = lambda rva: 512 + rva - 0x2000
assert raw_offset(U32(x, 216)) == 512
assert 512+240 == 752 and 736+12 <= 752 and 736+12 > 512+160
assert x[736:748].hex() == '050041003dd800de42002100'
assert U16(x, 736) == 5
assert x[738:748].decode('utf-16le') == 'A😀B!'
assert tuple(U16(x, 738+i) for i in (0, 2, 4, 6, 8)) == (0x41, 0xd83d, 0xde00, 0x42, 0x21)

# Walk every reachable directory entry, not only the two expected leaf paths.
visited, entries, leaves, dirs = set(), 0, [], []
def walk(offset, path=(), locations=()):
    global entries
    assert offset not in visited and 512 <= offset < 752
    visited.add(offset)
    characteristics, stamp, major, minor, named, ids = struct.unpack_from('<IIHHHH', x, offset)
    assert (characteristics, stamp, major, minor) == (0, 0, 0, 0)
    assert offset + 16 + 8*(named+ids) <= 752
    dirs.append((offset, named, ids, 16+8*(named+ids)))
    for j in range(named+ids):
        entry = offset+16+8*j
        name_word, target = struct.unpack_from('<II', x, entry)
        entries += 1
        if j < named:
            assert name_word & 0x80000000
            name_offset = 512+(name_word & 0x7fffffff)
            n = U16(x, name_offset)
            assert name_offset+2+2*n <= 752
            label = x[name_offset+2:name_offset+2+2*n].decode('utf-16le')
        else:
            assert name_word <= 0xffff
            label = name_word
        target_offset = 512+(target & 0x7fffffff)
        if len(path) < 2:
            assert target & 0x80000000
            walk(target_offset, path+(label,), locations+(entry,))
        else:
            assert not target & 0x80000000 and target_offset+16 <= 752
            rva, size, codepage, reserved = struct.unpack_from('<IIII', x, target_offset)
            payload_offset = raw_offset(rva)
            assert 512 <= payload_offset and payload_offset+size <= 1024
            assert (codepage, reserved) == (0, 0)
            leaves.append((path+(label,), locations+(entry,), target_offset, payload_offset, size,
                           sha(x[payload_offset:payload_offset+size])))
walk(512)
assert sorted(dirs) == [(512,0,1,24),(536,1,1,32),(568,0,1,24),(592,0,1,24)]
expected = [((10,'A😀B!',1036),(528,552,584),616,672,15,
             '071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229'),
            ((10,3,1033),(528,560,608),632,704,15,
             'cc29ca16da56975bf9fb034fbc010e377076ada5df6395622c8ffd9fed19f67e')]
assert sorted(leaves, key=lambda leaf: leaf[2]) == expected
assert entries == 5 and len(leaves) == 2 and len(visited) == 4
n = raw['normalized_result']
assert n['format'] == 'pe32-plus' and n['machine'] == 0x8664
assert n['artifact'] == {'path':str(r51),'sha256':sha(x),'bytes':1024}
assert n['directory'] == {'rva':8192,'location':{'offset':512,'bytes':240},
                          'data_directory_location':{'offset':216,'bytes':8}}
assert [(d['location']['offset'],d['location']['bytes'],d['named_entries'],d['id_entries'])
        for d in n['directories']] == [(i, size, named, ids) for i, named, ids, size in sorted(dirs)]
assert len(n['directories']) == 4 and len(n['resources']) == 2
for index, (resource, (path, locations, data_at, payload_at, size, digest)) in enumerate(zip(n['resources'], expected)):
    assert resource['index'] == index and resource['type'] == {'kind':'id','id':path[0]}
    assert resource['name'] == ({'kind':'name','name':path[1],
        'utf16le_hex':'41003dd800de42002100','location':{'offset':736,'bytes':12}}
        if index == 0 else {'kind':'id','id':3})
    assert resource['language'] == {'kind':'id','id':path[2]}
    assert resource['entry_locations'] == [{'offset':i,'bytes':8} for i in locations]
    assert resource['data_entry_location'] == {'offset':data_at,'bytes':16}
    assert (resource['code_page'],resource['reserved']) == (0,0)
    assert resource['payload'] == {'rva':0x2000+payload_at-512,
       'location':{'offset':payload_at,'bytes':size},'sha256':digest}
assert n['coverage'] == {'status':'complete','examined_entries':5,'resources':2}
assert n['icon_groups'] == []
assert raw['subject']['digest']['sha256'] == sha(x)
assert receipt['fixture_sha256'] == sha(x)
assert receipt['stdout_sha256'] == sha(raw_bytes)
assert receipt['evidence_id'] == raw['evidence_id'] and receipt['exit_code'] == 0
assert refusal['code'] == 'invalid_request'
assert refusal['details']['operation'] == 'inspect_pe_resources'
assert refusal['details']['issues'] == [{'path':['path'],'reason':'invalid_format',
    'message':'Resource directory offset leaves the declared resource interval.'}]
print('PASS: fixture byte topology, full resource traversal, saved success and refusal/receipt consistency')
```
