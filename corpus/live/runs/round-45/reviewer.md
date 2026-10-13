# Round 45 independent LEAF review

**Verdict: PASS (static resource-table observation).** Independent byte decoding of the PE32+ fixture matches the saved REA normalized result exactly for the resource directory, all six directory headers, all eight directory entries, all three leaf identities/entry paths/data-entry locations/payload locations and SHA-256 hashes, and both RT_GROUP_ICON image records. Against round 42, the only changed byte is file offset 640, `09 → 0c` (little-endian RT_ICON ID 2 language `0x0409`/1033 → `0x040c`/1036). Both icon payloads and the group payload are unchanged. Group image ID 1 retains candidate `[0]`, same-language index `0`, and `size_matches: true`. Group image ID 2 retains candidate `[1]`, while same-language index and size match are both `null`; there is no false missing candidate and no suppression of the first link.

**Read-only verifier:** Run the following exact command from any directory. It reads the two fixture files, saved REA JSON and producer receipt, and writes nothing; it does not run the PE or invoke REA.

```sh
python - <<'PY'
from pathlib import Path
import hashlib, json, struct
root = Path('/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus')
new = root/'fixtures/pe-r45/fixture.exe'
old = root/'fixtures/pe-r42/fixture.exe'
run = root/'live/runs/round-45'
a, b = new.read_bytes(), old.read_bytes()
e = json.loads((run/'inspection.raw.json').read_text())
receipt = json.loads((run/'producer-receipt.json').read_text())
U16 = lambda p, x: struct.unpack_from('<H', p, x)[0]
U32 = lambda p, x: struct.unpack_from('<I', p, x)[0]
sha = lambda x: hashlib.sha256(x).hexdigest()
loc = lambda x, n: {'offset': x, 'bytes': n}
assert len(a) == len(b) == 1536
assert [(i, b[i], a[i]) for i in range(len(a)) if a[i] != b[i]] == [(640, 9, 12)]
assert a[641:] == b[641:] and a[:640] == b[:640]
pe = U32(a, 0x3c)
assert a[:2] == b'MZ' and a[pe:pe+4] == b'PE\0\0'
coff, opt = pe+4, pe+24
assert U16(a, coff) == 0x8664 and U16(a, coff+2) == 1
assert U16(a, opt) == 0x20b and U16(a, coff+16) == 240
sec = opt + U16(a, coff+16)
assert a[sec:sec+5] == b'.rsrc'
virtual_size, virtual_rva, raw_size, raw_ptr = struct.unpack_from('<IIII', a, sec+8)
assert (virtual_size, virtual_rva, raw_size, raw_ptr) == (1024, 8192, 1024, 512)
resource_dd = opt+112+8*2
root_rva, dir_bytes = U32(a, resource_dd), U32(a, resource_dd+4)
assert (root_rva, dir_bytes, resource_dd) == (8192, 208, 216)
def file_offset(rva, size):
    assert virtual_rva <= rva and rva+size <= virtual_rva+raw_size
    off = raw_ptr + rva - virtual_rva
    assert off+size <= len(a)
    return off
base = file_offset(root_rva, dir_bytes)
assert base == 512
folders, entries, leaves = [], [], []
def walk(rel, trail=(), path=()):
    off = base+rel
    assert off not in path and base <= off < base+dir_bytes
    characteristics, timestamp, major, minor, named, ids = struct.unpack_from('<IIHHHH', a, off)
    count = named+ids
    assert off+16+8*count <= base+dir_bytes
    folders.append({'location':loc(off,16+8*count), 'characteristics':characteristics,
                    'timestamp':timestamp, 'major_version':major, 'minor_version':minor,
                    'named_entries':named, 'id_entries':ids})
    for j in range(count):
        eo = off+16+8*j
        ident, child = U32(a, eo), U32(a, eo+4)
        assert j >= named and ident < 0x80000000
        entries.append((eo, ident, child))
        if child & 0x80000000:
            walk(child & 0x7fffffff, trail+((ident, eo),), path+(off,))
        else:
            assert len(trail) == 2
            de = base+child
            assert de+16 <= base+dir_bytes
            rva, n, code_page, reserved = struct.unpack_from('<IIII', a, de)
            payload_off = file_offset(rva, n)
            ids3 = [t[0] for t in trail]+[ident]
            leaf = {'index':len(leaves), 'type':{'kind':'id','id':ids3[0]},
                    'name':{'kind':'id','id':ids3[1]},
                    'language':{'kind':'id','id':ids3[2]},
                    'entry_locations':[loc(t[1],8) for t in trail]+[loc(eo,8)],
                    'data_entry_location':loc(de,16), 'code_page':code_page,
                    'reserved':reserved,
                    'payload':{'rva':rva,'location':loc(payload_off,n),
                               'sha256':sha(a[payload_off:payload_off+n])}}
            leaves.append(leaf)
walk(0)
assert [x['location']['offset'] for x in folders] == [512,544,600,624,576,648]
assert entries == [(528,3,0x80000020),(560,1,0x80000058),(616,1033,0xa0),
                   (568,2,0x80000070),(640,1036,0xb0),(536,14,0x80000040),
                   (592,1,0x80000088),(664,1033,0xc0)]
assert [(x['type']['id'],x['name']['id'],x['language']['id'],
         x['payload']['location']['offset'],x['payload']['location']['bytes']) for x in leaves] == [
         (3,1,1033,768,48),(3,2,1036,832,48),(14,1,1033,896,34)]
assert [(x['data_entry_location']['offset'],x['payload']['rva'],x['payload']['sha256']) for x in leaves] == [
    (672,8448,'d7aaca7bc7951c9249a7798838189374fa953d3def03aebb375ee731768e5003'),
    (688,8512,'2f503cace29956c75acd5356de2f8fa98485b01edd654daf0f81a739b44c82ae'),
    (704,8576,'45eb70319667352d8bfea3249f7fb30166c6835d2cf564b5ec303bf2d716c17a')]
assert all(a[s:t] == b[s:t] for s,t in [(768,816),(832,880),(896,930)])
group = leaves[2]
go = group['payload']['location']['offset']
assert struct.unpack_from('<HHH',a,go) == (0,1,2)
images = []
for k in range(2):
    entry = go+6+14*k
    w,h,colors,reserved,planes,bits,size,rid = struct.unpack_from('<BBBBHHIH',a,entry)
    candidates = [x['index'] for x in leaves if x['type']['id'] == 3 and x['name']['id'] == rid]
    same = next((ix for ix in candidates if leaves[ix]['language']['id'] == group['language']['id']),None)
    images.append({'location':loc(entry,14),'width':w,'height':h,'color_count':colors,
                   'reserved':reserved,'planes':planes,'bit_count':bits,'declared_bytes':size,
                   'resource_id':rid,'candidate_resource_indices':candidates,
                   'same_language_resource_index':same,
                   'size_matches':None if same is None else size == leaves[same]['payload']['location']['bytes']})
assert [(x['resource_id'],x['candidate_resource_indices'],x['same_language_resource_index'],x['size_matches']) for x in images] == [
       (1,[0],0,True),(2,[1],None,None)]
n = e['normalized_result']
assert n['format'] == 'pe32-plus' and n['machine'] == 0x8664
assert n['artifact'] == {'path':str(new),'sha256':sha(a),'bytes':len(a)}
assert n['directory'] == {'rva':root_rva,'location':loc(base,dir_bytes), 'data_directory_location':loc(resource_dd,8)}
assert n['directories'] == folders and n['resources'] == leaves
assert n['icon_groups'] == [{'resource_index':2,'images':images}]
assert n['coverage'] == {'status':'complete','examined_entries':len(entries),'resources':len(leaves)}
assert receipt['fixture_sha256'] == sha(a) == e['subject']['digest']['sha256']
assert receipt['evidence_id'] == e['evidence_id']
assert receipt['command'] == 'npx -y rea-agents@6.4.0 inspect-pe-resources '+str(new)+' --format json'
assert receipt['exit_code'] == 0
assert receipt['stdout_sha256'] == sha((run/'inspection.raw.json').read_bytes())
assert e['authority'] == 'shipped-artifact' and e['confidence'] == 'observed'
print('PASS: independent PE32+ tree, 6 directories, 8 entries, 3 leaves, 2 group links, one-byte delta, saved REA comparison; receipt fields internally consistent')
PY
```

**Evidence/provenance limits:** The receipt records REA command/version, exit 0, fixture digest and evidence ID; its stdout digest equals the saved raw JSON file digest. These checks establish internal consistency of the *saved* producer evidence, not independent proof that the recorded command actually ran. This review did not call REA or execute the PE. Resource candidates and same-language links are static table relationships only; language fallback, payload image decoding, and actual shell/window icon loading remain unobserved. The three payload hashes and locations are checked against artifact bytes, not inferred from the receipt.
