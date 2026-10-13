# Round 39 — non-author LEAF review

**PASS** — independently parsed the PE32 headers, `.rsrc` directory, all six directory entries, both resource leaves, and the RT_GROUP_ICON structure directly from `fixture.exe`. Compared the saved REA JSON field-for-field for the parsed tree, checked the receipt’s internal hashes, and compared round 36 bytes. The only file change is offset 608: `0x09 → 0x0c`, changing RT_ICON ID 1 language 1033 → 1036. RT_GROUP_ICON ID 1 remains language 1033; its 20-byte group payload still declares the same 48-byte icon ID 1. The 48-byte RT_ICON payload is unchanged. Candidate `[0]` remains, while `same_language_resource_index` and `size_matches` are `null`. Resource-directory coverage is `complete`, six entries/two leaves.

The following read-only verifier uses Python 3 standard library. Run as `python3 - <<'PY'`, paste the block between the fences, then `PY`; it prints `PASS` or raises `AssertionError` on mismatch. It reads only the two fixtures, saved inspection and receipt.

```python
from pathlib import Path
import hashlib, json, struct

root = Path('/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus')
old = root / 'fixtures/pe-r36/fixture.exe'
new = root / 'fixtures/pe-r39/fixture.exe'
run = root / 'live/runs/round-39'
raw_path = run / 'inspection.raw.json'
receipt_path = run / 'producer-receipt.json'
sha = lambda data: hashlib.sha256(data).hexdigest()
loc = lambda offset, size: {'offset': offset, 'bytes': size}
expected_sha = {
    'r36': 'a10b1289edc59df08ccc9a3b6cf1e81f803a8041fa414fc1c6375a1d017eca96',
    'r39': '73432e0ce2524e12970bb0155d478214736bf97e0a173a5a87b7d5aeb810ed97',
    'raw': '8e3320a213318323eb771dc1e6f88e9383eedbf576d125e9499d487f98331058',
}

def parse(path):
    data = path.read_bytes()
    u16 = lambda o: struct.unpack_from('<H', data, o)[0]
    u32 = lambda o: struct.unpack_from('<I', data, o)[0]
    assert data[:2] == b'MZ'
    pe = u32(0x3c)
    assert data[pe:pe + 4] == b'PE\0\0'
    machine, sections, _, _, _, opt_size, _ = struct.unpack_from('<HHIIIHH', data, pe + 4)
    opt = pe + 24
    assert u16(opt) == 0x10b and opt_size == 224 and sections == 1
    directory_entry = opt + 96 + 8 * 2
    resource_rva, resource_size = struct.unpack_from('<II', data, directory_entry)
    section = opt + opt_size
    section_name, virtual_size, va, raw_size, raw_start = struct.unpack_from('<8sIIII', data, section)
    assert section_name.rstrip(b'\0') == b'.rsrc' and virtual_size <= raw_size
    def to_offset(rva, length):
        assert va <= rva and rva + length <= va + raw_size
        offset = raw_start + rva - va
        assert offset + length <= len(data)
        return offset
    base = to_offset(resource_rva, resource_size)
    def ref(rel, size):
        assert 0 <= rel and rel + size <= resource_size
        return base + rel
    directories, resources, group_records = [], [], []
    entry_count = 0
    def walk(relative, ancestry=(), hops=()):
        nonlocal entry_count
        assert relative not in hops
        offset = ref(relative, 16)
        char, stamp, major, minor, names, ids = struct.unpack_from('<IIHHHH', data, offset)
        total = names + ids
        ref(relative, 16 + 8 * total)
        directories.append({'location': loc(offset, 16 + 8 * total), 'characteristics': char,
                            'timestamp': stamp, 'major_version': major, 'minor_version': minor,
                            'named_entries': names, 'id_entries': ids})
        entry_count += total
        for j in range(total):
            entry = offset + 16 + 8 * j
            ident, target = struct.unpack_from('<II', data, entry)
            assert not ident & 0x80000000  # fixture has ID entries only
            assert (j >= names)  # no named entries in this fixture
            step = (ident, entry)
            if len(ancestry) < 2:
                assert target & 0x80000000
                walk(target & 0x7fffffff, ancestry + (step,), hops + (relative,))
            else:
                assert len(ancestry) == 2 and not target & 0x80000000
                record_offset = ref(target, 16)
                payload_rva, size, code_page, reserved = struct.unpack_from('<IIII', data, record_offset)
                payload_offset = to_offset(payload_rva, size)
                index = len(resources)
                keys = ancestry + (step,)
                resources.append({'index': index,
                    'type': {'kind': 'id', 'id': keys[0][0]},
                    'name': {'kind': 'id', 'id': keys[1][0]},
                    'language': {'kind': 'id', 'id': keys[2][0]},
                    'entry_locations': [loc(k[1], 8) for k in keys],
                    'data_entry_location': loc(record_offset, 16),
                    'code_page': code_page, 'reserved': reserved,
                    'payload': {'rva': payload_rva, 'location': loc(payload_offset, size),
                                'sha256': sha(data[payload_offset:payload_offset + size])}})
                if keys[0][0] == 14:
                    group_records.append((index, payload_offset, size))
    walk(0)
    groups = []
    for index, pos, size in group_records:
        assert size >= 6
        reserved, typ, count = struct.unpack_from('<HHH', data, pos)
        assert reserved == 0 and typ == 1 and size == 6 + count * 14
        images = []
        for k in range(count):
            at = pos + 6 + k * 14
            width, height, colors, unused, planes, bits, amount, rid = struct.unpack_from('<BBBBHHIH', data, at)
            candidates = [r['index'] for r in resources if r['type']['id'] == 3 and r['name']['id'] == rid]
            same = next((i for i in candidates if resources[i]['language'] == resources[index]['language']), None)
            matched = (resources[same]['payload']['location']['bytes'] == amount) if same is not None else None
            images.append({'location': loc(at, 14), 'width': width, 'height': height,
                           'color_count': colors, 'reserved': unused, 'planes': planes,
                           'bit_count': bits, 'declared_bytes': amount, 'resource_id': rid,
                           'candidate_resource_indices': candidates,
                           'same_language_resource_index': same, 'size_matches': matched})
        groups.append({'resource_index': index, 'images': images})
    return data, {'format': 'pe32', 'machine': machine,
                  'directory': {'rva': resource_rva, 'location': loc(base, resource_size),
                                'data_directory_location': loc(directory_entry, 8)},
                  'directories': directories, 'resources': resources,
                  'icon_groups': groups,
                  'coverage': {'status': 'complete', 'examined_entries': entry_count,
                               'resources': len(resources)}}

before, d36 = parse(old)
after, d39 = parse(new)
assert len(before) == len(after) == 1024
assert sha(before) == expected_sha['r36'] and sha(after) == expected_sha['r39']
assert [(i, x, y) for i, (x, y) in enumerate(zip(before, after)) if x != y] == [(608, 9, 12)]
assert d36['resources'][0]['language']['id'] == 1033
assert d39['resources'][0]['language']['id'] == 1036
assert d36['resources'][1]['language']['id'] == d39['resources'][1]['language']['id'] == 1033
assert before[:608] == after[:608] and before[609:] == after[609:]
assert d36['directories'] == d39['directories']  # directory count/layout/metadata preserved
assert [{**r, 'language': {'kind': 'id', 'id': 1036}} if i == 0 else r
        for i, r in enumerate(d36['resources'])] == d39['resources']
assert d39['directory'] == {'rva': 8192, 'location': loc(512, 160),
                            'data_directory_location': loc(200, 8)}
assert [d['location'] for d in d39['directories']] == [loc(o, n) for o, n in
                                                    [(512,32), (544,24), (592,24), (568,24), (616,24)]]
assert [r['type']['id'] for r in d39['resources']] == [3,14]
assert [r['name']['id'] for r in d39['resources']] == [1,1]
assert [r['entry_locations'] for r in d39['resources']] == [
    [loc(528,8), loc(560,8), loc(608,8)], [loc(536,8), loc(584,8), loc(632,8)]]
assert [r['data_entry_location'] for r in d39['resources']] == [loc(640,16), loc(656,16)]
assert [r['payload'] for r in d39['resources']] == [
    {'rva':8448, 'location':loc(768,48), 'sha256':'d7aaca7bc7951c9249a7798838189374fa953d3def03aebb375ee731768e5003'},
    {'rva':8512, 'location':loc(832,20), 'sha256':'cc3745185dc1ae877dff5b3561df1162b7487fe78af6761a85649989979a3d01'}]
assert d36['icon_groups'][0]['images'][0]['same_language_resource_index'] == 0
assert d36['icon_groups'][0]['images'][0]['size_matches'] is True
assert d39['icon_groups'] == [{'resource_index': 1, 'images': [{
    'location':loc(838,14), 'width':1, 'height':1, 'color_count':0,
    'reserved':0, 'planes':1, 'bit_count':32, 'declared_bytes':48,
    'resource_id':1, 'candidate_resource_indices':[0],
    'same_language_resource_index':None, 'size_matches':None}]}]
raw_bytes = raw_path.read_bytes()
assert sha(raw_bytes) == expected_sha['raw']
raw = json.loads(raw_bytes)
receipt = json.loads(receipt_path.read_bytes())
assert receipt == {'command': f'npx -y rea-agents@6.4.0 inspect-pe-resources {new} --format json',
                   'exit_code': 0, 'stdout_sha256': sha(raw_bytes),
                   'evidence_id': raw['evidence_id'], 'fixture_sha256':sha(after)}
assert raw['subject']['digest']['sha256'] == sha(after)
assert raw['subject']['local_path'] == str(new)
assert raw['subject']['format'] == 'pe'
assert raw['operation'] == 'inspect_pe_resources' and raw['provider']['id'] == 'rea-pe-resources'
assert raw['parameters']['path'] == str(new)
assert raw['normalized_result']['artifact'] == {'path':str(new), 'sha256':sha(after), 'bytes':len(after)}
for key, value in d39.items():
    assert raw['normalized_result'][key] == value, key
assert raw['normalized_result']['limitations'] == raw['limitations']
assert raw['normalized_result']['coverage'] == {'status':'complete','examined_entries':6,'resources':2}
print('PASS: independent PE32 tree, r36→r39 one-byte delta, all reported directory/resource/group fields, coverage, payload hashes, and receipt internal hashes')
```

Caveats: The receipt verifies internally against the *saved* inspection JSON byte digest and fixture, not an independently witnessed producer execution or a fresh REA run. The evidence ID is matched across saved records but is not independently rederived. `complete` describes the decoded resource tree under this fixture, not execution, language fallback, icon decoding, or shell/window icon selection. Opaque RT_ICON image bytes are hashed and sized, not decoded. No PE file was executed; no fixture or producer output was edited.
