# Round 49 independent byte review

**PASS (saved-evidence consistency).** I independently parsed PE32+ headers, section RVA mapping, resource-directory entries and payload bytes from `pe-r49/fixture.exe`, compared r47, and matched every reachable directory, entry path, data entry, payload location and SHA-256 against `inspection.raw.json`. The only changed byte is offset 664 (`0c` → `09`): RT_GROUP_ICON name ID 1 language 1036 → 1033. RT_ICON name ID 1 remains at languages 1033 and 1036 with distinct, unchanged 48-byte payloads. The group image ID 1 has candidate indices `[0, 1]`, same-language index `0`, and a true declared-size match. Coverage is 7 entries, 5 directories, 3 leaves. Receipt fixture hash, saved-JSON-byte hash, evidence ID, command and exit status agree internally.

**Limits:** The receipt hash confirms consistency with the saved JSON bytes, not provenance or producer authentication; the original process stdout is not separately retained. No REA invocation, PE execution, Windows loader/fallback, icon decoding/rendering, or general PE validation was performed. All file input is read-only; only this reviewer document was written.

Run the independent, read-only verifier with `python - <<'PY'` followed by this complete code and `PY`:

```python
from pathlib import Path
import hashlib, json, struct
C = Path('/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus')
a_path = C/'fixtures/pe-r49/fixture.exe'
b_path = C/'fixtures/pe-r47/fixture.exe'
run = C/'live/runs/round-49'
a, b = a_path.read_bytes(), b_path.read_bytes()
raw_bytes = (run/'inspection.raw.json').read_bytes()
record = json.loads(raw_bytes)
receipt = json.loads((run/'producer-receipt.json').read_bytes())
H = lambda data: hashlib.sha256(data).hexdigest()
u16 = lambda off: struct.unpack_from('<H', a, off)[0]
u32 = lambda off: struct.unpack_from('<I', a, off)[0]
loc = lambda off, n: {'offset':off, 'bytes':n}
assert len(a) == len(b) == 1536
assert [(i, b[i], a[i]) for i in range(len(a)) if a[i] != b[i]] == [(664, 12, 9)]
assert a[:2] == b'MZ'
pe = u32(0x3c)
assert a[pe:pe+4] == b'PE\0\0'
assert u16(pe+4) == 0x8664
sections_count, optional_size = u16(pe+6), u16(pe+20)
opt = pe + 24
assert u16(opt) == 0x20b and u32(opt+108) >= 3
resource_dd = opt+112+2*8
base_rva, resource_size = struct.unpack_from('<II', a, resource_dd)
sections = []
for i in range(sections_count):
    s = opt+optional_size+40*i
    name = a[s:s+8].split(b'\0',1)[0]
    virt_size, virt_rva, raw_size, raw_off = struct.unpack_from('<IIII',a,s+8)
    sections.append((virt_rva, max(virt_size, raw_size), raw_off, raw_size, name))
def rva_file(rva, size):
    matches = [off+rva-start for start, span, off, raw_size, _ in sections
               if start <= rva and rva+size <= start+raw_size and rva+size <= start+span]
    assert len(matches) == 1
    result = matches[0]
    assert result >= 0 and result+size <= len(a)
    return result
resource_start = rva_file(base_rva,resource_size)
assert (base_rva, resource_size, resource_start) == (8192, 208, 512)
def rloc(rel, size):
    assert rel >= 0 and rel+size <= resource_size
    return loc(resource_start+rel,size)

directories, resources = [], []
seen_dirs = set()
examined = 0
def walk(rel, names=(), entries=()):
    global examined
    assert rel not in seen_dirs and len(names)<3
    seen_dirs.add(rel)
    off = rloc(rel,16)['offset']
    characteristics, timestamp, major, minor, named, ids = struct.unpack_from('<IIHHHH',a,off)
    count = named+ids
    rloc(rel,16+8*count)
    directories.append({'location':rloc(rel,16+8*count),
                        'characteristics':characteristics,'timestamp':timestamp,
                        'major_version':major,'minor_version':minor,
                        'named_entries':named,'id_entries':ids})
    assert named == 0 and ids <= 4096
    for i in range(count):
        examined += 1
        entryoff = off+16+8*i
        ident, target = struct.unpack_from('<II',a,entryoff)
        assert ident < 0x80000000
        path = names+(ident,)
        entry_path = entries+(loc(entryoff,8),)
        if len(path)<3:
            assert target & 0x80000000
            walk(target & 0x7fffffff,path,entry_path)
        else:
            assert not (target & 0x80000000)
            de = rloc(target,16)
            payload_rva, payload_size, code_page, reserved = struct.unpack_from('<IIII',a,de['offset'])
            payload_off = rva_file(payload_rva,payload_size)
            resources.append({'index':len(resources),
                'type':{'kind':'id','id':path[0]},
                'name':{'kind':'id','id':path[1]},
                'language':{'kind':'id','id':path[2]},
                'entry_locations':list(entry_path),'data_entry_location':de,
                'code_page':code_page,'reserved':reserved,
                'payload':{'rva':payload_rva,'location':loc(payload_off,payload_size),
                           'sha256':H(a[payload_off:payload_off+payload_size])}})
walk(0)
assert examined == 7 and len(resources) == 3 and len(directories) == 5
assert [(r['type']['id'],r['name']['id'],r['language']['id']) for r in resources] == [(3,1,1033),(3,1,1036),(14,1,1033)]
assert [(r['entry_locations'],r['data_entry_location']) for r in resources] == [
    ([loc(528,8),loc(560,8),loc(616,8)],loc(672,16)),
    ([loc(528,8),loc(560,8),loc(624,8)],loc(688,16)),
    ([loc(536,8),loc(592,8),loc(664,8)],loc(704,16))]
assert [(r['payload']['rva'],r['payload']['location']) for r in resources] == [
    (8448,loc(768,48)),(8512,loc(832,48)),(8576,loc(896,20))]
assert [r['payload']['sha256'] for r in resources] == [
    'd7aaca7bc7951c9249a7798838189374fa953d3def03aebb375ee731768e5003',
    '2f503cace29956c75acd5356de2f8fa98485b01edd654daf0f81a739b44c82ae',
    'cc3745185dc1ae877dff5b3561df1162b7487fe78af6761a85649989979a3d01']
assert a[768:816] != a[832:880] and a[768:816] == b[768:816] and a[832:880] == b[832:880]
assert u32(664) == 1033 and struct.unpack_from('<I',b,664)[0] == 1036

group = resources[2]
goff = group['payload']['location']['offset']
assert struct.unpack_from('<HHH',a,goff) == (0,1,1)
width,height,colors,reserved,planes,bits,declared,image_id = struct.unpack_from('<BBBBHHIH',a,goff+6)
candidates = [r['index'] for r in resources if r['type']['id']==3 and r['name']['id']==image_id]
same = [i for i in candidates if resources[i]['language']['id']==group['language']['id']]
assert (candidates,same,declared) == ([0,1],[0],48)
assert group['payload']['location']['bytes']==6+14
image = {'location':loc(goff+6,14),'width':width,'height':height,
         'color_count':colors,'reserved':reserved,'planes':planes,'bit_count':bits,
         'declared_bytes':declared,'resource_id':image_id,
         'candidate_resource_indices':candidates,'same_language_resource_index':same[0],
         'size_matches':declared==resources[same[0]]['payload']['location']['bytes']}
assert image['size_matches'] is True
n = record['normalized_result']
for key, expected in [('format','pe32-plus'),('machine',0x8664),
    ('artifact',{'path':str(a_path),'sha256':H(a),'bytes':len(a)}),
    ('directory',{'rva':base_rva,'location':loc(resource_start,resource_size),
                  'data_directory_location':loc(resource_dd,8)}),
    ('directories',directories),('resources',resources),
    ('icon_groups',[{'resource_index':2,'images':[image]}]),
    ('coverage',{'status':'complete','examined_entries':examined,'resources':len(resources)})]:
    assert n[key] == expected, key
assert record['operation']=='inspect_pe_resources' and record['subject']['digest']['sha256']==H(a)
assert record['subject']['local_path']==str(a_path)
assert receipt == {'command':'npx -y rea-agents@6.4.0 inspect-pe-resources '+str(a_path)+' --format json',
                   'exit_code':0,'stdout_sha256':H(raw_bytes),
                   'fixture_sha256':H(a),'evidence_id':record['evidence_id']}
print('PASS r49: sole offset 664 mutation; 7 entries, 5 directories, 3 leaves; intact icons; first-candidate same-language index 0; exact saved structures and receipt internal hashes')
```
