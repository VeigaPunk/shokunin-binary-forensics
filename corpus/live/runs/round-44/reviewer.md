# Round 44 independent PE32+ review

**PASS.** Read-only verification of the fixture, r42 baseline, saved REA JSON, and producer receipt. Run the verifier below with `python3` (standard library only); it neither executes the PE nor invokes REA, and writes nothing.

- Both files are 1,536 bytes. Sole changed byte: file offset **924**, `0x30` (48) → `0x2f` (47), in the second group-icon record's declared image size.
- Independent traversal found PE32+ AMD64; resource directory RVA `0x2000`, file offset 512, declared length 208; six reachable directories, eight entries, and exactly three leaves: `(RT_ICON,1,1033)`, `(RT_ICON,2,1033)`, `(RT_GROUP_ICON,1,1033)`. The icon leaves retain identities, locations and payload SHA-256 hashes; the group remains at offset 896, length 34, with only its payload hash changed by that byte.
- Group record 1: ID 1, candidates `[0]`, same-language index 0, declared 48, actual 48, `size_matches=true`. Record 2: ID 2, candidates `[1]`, same-language index 1, declared 47, actual 48, `size_matches=false`. There are no absent candidates. All independently decoded reachable fields match the saved REA normalized result; the fixture digest, raw JSON digest, evidence ID, path and exit code match the receipt.
- **Limitations:** Static resource-tree comparison only. The icon bytes were hashed, not decoded or rendered; Windows language fallback, shell/window icon choice, and executable behavior were not observed. The producer command's actual past invocation cannot be authenticated beyond its saved receipt and matching output hash.

## Exact runnable read-only verifier

```python
from pathlib import Path
from hashlib import sha256
from struct import unpack_from
import json

root = Path('/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus')
new_path = root / 'fixtures/pe-r44/fixture.exe'
old_path = root / 'fixtures/pe-r42/fixture.exe'
run = root / 'live/runs/round-44'
raw_bytes = (run / 'inspection.raw.json').read_bytes()
report = json.loads(raw_bytes)
receipt = json.loads((run / 'producer-receipt.json').read_bytes())
new, old = new_path.read_bytes(), old_path.read_bytes()
H = lambda data: sha256(data).hexdigest()
def require(ok, why):
    if not ok:
        raise AssertionError(why)

def decode(data):
    u16 = lambda at: unpack_from('<H', data, at)[0]
    u32 = lambda at: unpack_from('<I', data, at)[0]
    require(data[:2] == b'MZ', 'DOS magic')
    pe = u32(0x3c)
    require(data[pe:pe+4] == b'PE\0\0', 'PE signature')
    machine, section_count = unpack_from('<HH', data, pe+4)
    opt = pe+24
    require(u16(opt) == 0x20b and u16(pe+20) >= 240, 'PE32+ optional header')
    section_table = opt+u16(pe+20)
    sections = [unpack_from('<8sIIIIIIHHI', data, section_table+40*i)
                for i in range(section_count)]
    def file_offset(rva, length):
        for name, virtual_size, virtual_address, raw_size, raw_offset, *_ in sections:
            if virtual_address <= rva and rva+length <= virtual_address+raw_size:
                offset = raw_offset+rva-virtual_address
                require(offset+length <= len(data), 'truncated RVA')
                return offset
        raise AssertionError(f'unmapped RVA {rva:#x}+{length}')
    data_dir_at = opt+112+8*2
    rva, byte_count = unpack_from('<II', data, data_dir_at)
    start = file_offset(rva, byte_count)
    directories, resources = [], []
    examined = 0
    def walk(relative, path, entries, ancestors):
        nonlocal examined
        require(relative not in ancestors, 'resource directory cycle')
        at = start+relative
        require(at+16 <= start+byte_count, 'directory outside declared region')
        characteristics, timestamp, major, minor, named, ids = unpack_from('<IIHHHH', data, at)
        count = named+ids
        require(at+16+8*count <= start+byte_count, 'entry table outside region')
        directories.append(dict(location=dict(offset=at, bytes=16+8*count),
                                characteristics=characteristics, timestamp=timestamp,
                                major_version=major, minor_version=minor,
                                named_entries=named, id_entries=ids))
        examined += count
        for i in range(count):
            entry_at = at+16+8*i
            identifier, target = unpack_from('<II', data, entry_at)
            require(not identifier & 0x80000000, 'this fixture must use numeric IDs')
            key = dict(kind='id', id=identifier)
            route = path+[key]
            route_entries = entries+[dict(offset=entry_at, bytes=8)]
            if target & 0x80000000:
                require(len(route) < 3, 'unexpected resource depth')
                walk(target & 0x7fffffff, route, route_entries, ancestors | {relative})
            else:
                require(len(route) == 3, 'leaf must have type/name/language')
                leaf_at = start+target
                require(leaf_at+16 <= start+byte_count, 'data entry outside directory')
                payload_rva, payload_size, code_page, reserved = unpack_from('<IIII', data, leaf_at)
                payload_at = file_offset(payload_rva, payload_size)
                resources.append(dict(index=len(resources), type=route[0], name=route[1],
                                      language=route[2], entry_locations=route_entries,
                                      data_entry_location=dict(offset=leaf_at, bytes=16),
                                      code_page=code_page, reserved=reserved,
                                      payload=dict(rva=payload_rva,
                                                   location=dict(offset=payload_at, bytes=payload_size),
                                                   sha256=H(data[payload_at:payload_at+payload_size]))))
    walk(0, [], [], set())
    groups = []
    for res in resources:
        if res['type']['id'] != 14:
            continue
        offset = res['payload']['location']['offset']
        length = res['payload']['location']['bytes']
        reserved, group_type, count = unpack_from('<HHH', data, offset)
        require((reserved, group_type) == (0, 1) and 6+14*count == length,
                'group icon header or record bounds')
        images = []
        for i in range(count):
            at = offset+6+14*i
            width, height, colors, unused, planes, bits, declared, rid = unpack_from('<BBBBHHIH', data, at)
            candidates = [r['index'] for r in resources if r['type']['id'] == 3 and r['name']['id'] == rid]
            same = next((j for j in candidates if resources[j]['language'] == res['language']), None)
            images.append(dict(location=dict(offset=at, bytes=14), width=width,
                               height=height, color_count=colors, reserved=unused,
                               planes=planes, bit_count=bits, declared_bytes=declared,
                               resource_id=rid, candidate_resource_indices=candidates,
                               same_language_resource_index=same,
                               size_matches=(resources[same]['payload']['location']['bytes'] == declared)
                                            if same is not None else None))
        groups.append(dict(resource_index=res['index'], images=images))
    return dict(format='pe32-plus', machine=machine,
                directory=dict(rva=rva, location=dict(offset=start, bytes=byte_count),
                               data_directory_location=dict(offset=data_dir_at, bytes=8)),
                directories=directories, resources=resources, icon_groups=groups,
                coverage=dict(status='complete', examined_entries=examined,
                              resources=len(resources)))

new_tree, old_tree = decode(new), decode(old)
require(len(new) == len(old) == 1536, 'file length')
require([(i, old[i], new[i]) for i in range(len(new)) if old[i] != new[i]] == [(924, 48, 47)],
        'only byte 924 must change 48 -> 47')
require(H(new) == 'bb2680c1ceaa3ce6e4921e078e2548f06f164d9598da2bff6c895890b73bc5fb', 'new digest')
require(H(old) == '3ab5008b436eb4facd3966767a507fa4b1625160532585a09a6af2f752b38941', 'baseline digest')
require(new_tree['directory'] == old_tree['directory'] and
        new_tree['directories'] == old_tree['directories'], 'reachable directory change')
require(new_tree['coverage'] == dict(status='complete', examined_entries=8, resources=3), 'coverage')
require([(r['type']['id'], r['name']['id'], r['language']['id']) for r in new_tree['resources']]
        == [(3, 1, 1033), (3, 2, 1033), (14, 1, 1033)], 'leaf identities')
require(new_tree['resources'][:2] == old_tree['resources'][:2], 'icon leaves/locations/hashes')
require(new_tree['resources'][2]['entry_locations'] == old_tree['resources'][2]['entry_locations'] and
        new_tree['resources'][2]['data_entry_location'] == old_tree['resources'][2]['data_entry_location'] and
        new_tree['resources'][2]['payload']['location'] == old_tree['resources'][2]['payload']['location'],
        'group leaf topology/location')
require(new_tree['icon_groups'][0]['images'][0] == old_tree['icon_groups'][0]['images'][0], 'first group image')
require([(im['resource_id'], im['candidate_resource_indices'], im['same_language_resource_index'],
          im['declared_bytes'], im['size_matches']) for im in new_tree['icon_groups'][0]['images']]
        == [(1, [0], 0, 48, True), (2, [1], 1, 47, False)], 'group resolution/size')
require([(im['declared_bytes'], im['size_matches']) for im in old_tree['icon_groups'][0]['images']]
        == [(48, True), (48, True)], 'baseline group sizes')
normalized = report['normalized_result']
for key, expected in new_tree.items():
    require(normalized[key] == expected, f'REA normalized {key}')
require(normalized['artifact'] == dict(path=str(new_path), sha256=H(new), bytes=len(new)), 'artifact metadata')
require(report['subject']['digest']['sha256'] == H(new) and
        report['subject']['local_path'] == str(new_path) and
        report['parameters']['path'] == str(new_path), 'envelope digest/path')
require(report['operation'] == 'inspect_pe_resources', 'operation')
require(receipt['fixture_sha256'] == H(new) and
        receipt['stdout_sha256'] == H(raw_bytes) and
        receipt['evidence_id'] == report['evidence_id'] and
        receipt['exit_code'] == 0 and
        str(new_path) in receipt['command'], 'producer receipt consistency')
print('PASS: independent PE32+ tree, 3 leaves, 8 entries, icons, groups, baseline delta, saved REA and receipt')
```
