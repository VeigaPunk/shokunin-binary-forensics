# Round 38 independent PE resource leaf review — PASS

I decoded the PE headers, section mapping, resource tree, data entries, payload digests, and RT_GROUP_ICON record directly from `pe-r38/fixture.exe` bytes; `truth.json` and REA were not used to derive the expected tree. Comparing `pe-r36/fixture.exe` gives exactly one changed byte: file offset **846**, the low byte of the group icon `dwBytesInRes` field, **48 → 47**. Both files are 1024 bytes. The RT_ICON type 3 / ID 1 / language 1033 payload remains at offset 768, length 48, with SHA-256 `d7aaca7bc7951c9249a7798838189374fa953d3def03aebb375ee731768e5003`.

The decoded RT_GROUP_ICON type 14 / ID 1 / language 1033 payload is offset 832, length 20, SHA-256 `8ba4474bfc0b4b9f569f3ee752d44f0f4b741b662064b9b413667e4150db4977`. Its sole image record is at offset 838, length 14, references icon ID 1, and declares 47 bytes. Candidate resource indices = `[0]`; same-language resource index = `0`; `size_matches = false`. Thus a missing-reference report would be false: the icon exists, but its declared size differs from the intact 48-byte payload. The five directory locations, six entry locations, two data-entry locations, both leaf identities/locations/digests, the directory header and coverage fields, and the icon record match `inspection.raw.json` exactly. The receipt exit code, fixture digest, evidence ID, and saved stdout SHA-256 also match. No REA execution was performed in this review.

## Exact read-only verifier

Run from any directory as `python - <<'PY'`, paste the code below, then close with `PY`. It reads four files and does not write files; it does not read `truth.json` or execute REA.

```python
from pathlib import Path
from hashlib import sha256
from struct import unpack_from as u
import json

base = Path('/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus')
f = base/'fixtures/pe-r38/fixture.exe'
previous = (base/'fixtures/pe-r36/fixture.exe').read_bytes()
b = f.read_bytes()
raw_path = base/'live/runs/round-38/inspection.raw.json'
receipt = json.loads((base/'live/runs/round-38/producer-receipt.json').read_text())
raw_bytes = raw_path.read_bytes()
raw = json.loads(raw_bytes)
n = raw['normalized_result']
H = lambda data: sha256(data).hexdigest()
loc = lambda off, size: {'offset': off, 'bytes': size}
assert len(previous) == len(b) == 1024
assert [(i, previous[i], b[i]) for i in range(len(b)) if previous[i] != b[i]] == [(846, 48, 47)]
assert b[:2] == b'MZ'
pe = u('<I', b, 0x3c)[0]
assert b[pe:pe+4] == b'PE\0\0'
machine, sections = u('<HH', b, pe+4)
opt_size = u('<H', b, pe+20)[0]
opt = pe+24
magic = u('<H', b, opt)[0]
assert magic == 0x10b and machine == 332 and sections == 1
rva, dir_size = u('<II', b, opt+96+8*2)
sec = opt+opt_size
virtual_size, sec_rva, raw_size, raw_start = u('<IIII', b, sec+8)
def fileoff(address, size):
    assert sec_rva <= address and address+size <= sec_rva+min(virtual_size, raw_size)
    off = raw_start+address-sec_rva
    assert off+size <= len(b)
    return off
root = fileoff(rva, dir_size)
assert root == 512 and (rva, dir_size) == (8192, 160)
directories, leaves = [], []
queue = [(0, (), ())]  # relative directory offset, type/name/language IDs, entry locations
entry_count = 0
while queue:
    rel, ids, path = queue.pop(0)
    off = root+rel
    characteristics, timestamp, major, minor, named, count = u('<IIHHHH', b, off)
    assert named == 0 and len(ids) <= 2
    directories.append({'location':loc(off,16+8*count), 'characteristics': characteristics,
                        'timestamp': timestamp, 'major_version': major, 'minor_version': minor,
                        'named_entries': named, 'id_entries': count})
    children = []
    for i in range(count):
        ent = off+16+8*i
        identity, child = u('<II', b, ent)
        assert identity < 0x80000000
        entry_count += 1
        new_ids, new_path = ids+(identity,), path+(loc(ent,8),)
        if child & 0x80000000:
            children.append((child & 0x7fffffff,new_ids,new_path))
        else:
            assert len(new_ids) == 3
            data_off = root+child
            payload_rva, size, codepage, reserved = u('<IIII', b, data_off)
            payload_off = fileoff(payload_rva,size)
            leaves.append({'index':len(leaves),
                           'type':{'kind':'id','id':new_ids[0]},
                           'name':{'kind':'id','id':new_ids[1]},
                           'language':{'kind':'id','id':new_ids[2]},
                           'entry_locations':list(new_path),
                           'data_entry_location':loc(data_off,16),
                           'code_page':codepage, 'reserved':reserved,
                           'payload':{'rva':payload_rva,'location':loc(payload_off,size),
                                      'sha256':H(b[payload_off:payload_off+size])}})
    queue = children + queue
assert entry_count == 6 and len(leaves) == 2
assert [(x['type']['id'],x['name']['id'],x['language']['id']) for x in leaves] == [(3,1,1033),(14,1,1033)]
assert [(x['payload']['location']['offset'],x['payload']['location']['bytes']) for x in leaves] == [(768,48),(832,20)]
assert [(x['location']['offset'],x['location']['bytes']) for x in directories] == [(512,32),(544,24),(592,24),(568,24),(616,24)]
groups = []
for group in leaves:
    if group['type']['id'] != 14: continue
    payload_loc = group['payload']['location']
    start, length = payload_loc['offset'], payload_loc['bytes']
    reserved, kind, count = u('<HHH',b,start)
    assert reserved == 0 and kind == 1 and length == 6+14*count
    images = []
    for i in range(count):
        e = start+6+14*i
        width,height,colors,res,planes,bits,declared,icon_id = u('<BBBBHHIH',b,e)
        candidates = [x['index'] for x in leaves if x['type']['id']==3 and x['name']['id']==icon_id]
        same = next((idx for idx in candidates if leaves[idx]['language']==group['language']),None)
        images.append({'location':loc(e,14),'width':width,'height':height,
                       'color_count':colors,'reserved':res,'planes':planes,'bit_count':bits,
                       'declared_bytes':declared,'resource_id':icon_id,
                       'candidate_resource_indices':candidates,
                       'same_language_resource_index':same,
                       'size_matches':any(leaves[idx]['payload']['location']['bytes']==declared for idx in candidates)})
    groups.append({'resource_index':group['index'],'images':images})
assert groups[0]['resource_index']==1 and len(groups)==1 and len(groups[0]['images'])==1
image = groups[0]['images'][0]
assert image['resource_id']==1 and image['declared_bytes']==47 and image['candidate_resource_indices']==[0]
assert image['same_language_resource_index']==0 and image['size_matches'] is False
assert u('<I',previous,846)[0]==48 and u('<I',b,846)[0]==47
expected = {'artifact':{'path':str(f),'sha256':H(b),'bytes':len(b)},
            'format':'pe32','machine':machine,
            'directory':{'rva':rva,'location':loc(root,dir_size),
                         'data_directory_location':loc(opt+96+8*2,8)},
            'directories':directories,'resources':leaves,'icon_groups':groups,
            'coverage':{'status':'complete','examined_entries':entry_count,'resources':len(leaves)},
            'limitations':raw['limitations']}
assert n == expected, 'REA normalized fields differ from independently decoded PE bytes'
assert receipt['exit_code']==0 and receipt['fixture_sha256']==H(b)
assert receipt['stdout_sha256']==H(raw_bytes)
assert receipt['evidence_id']==raw['evidence_id']
assert raw['subject']['digest']['sha256']==H(b)
assert raw['subject']['local_path']==str(f)
assert raw['provider']=={'id':'rea-pe-resources','name':'REA PE resource parser','version':'1'}
assert raw['operation']=='inspect_pe_resources' and raw['parameters']['path']==str(f)
assert raw['limitations']==n['limitations']
print('PASS: byte delta, tree, leaf identity/location/digests, RT_GROUP_ICON link/mismatch, REA receipt')
```

Limitations: This is a static resource-table review, not image decoding, language fallback validation, or proof of Windows shell/window icon rendering. It compares the recorded JSON and receipt to saved bytes but does not attest to the provenance of the producer command. The decoded fixture contains only ID-based resource entries; the verifier is intentionally scoped to that observed structure rather than a general PE parser. The receipt's stdout hash is checked against saved `inspection.raw.json` bytes, not independently collected process stdout.
