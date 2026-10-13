"""Read-only cross-record check for four authored PE icon-reference states."""
from pathlib import Path
from hashlib import sha256 as _sha256
import copy
import hashlib
import json
import struct

root = Path(__file__).resolve().parent
sha = lambda blob: hashlib.sha256(blob).hexdigest()
loc = lambda offset, size: {'offset': offset, 'bytes': size}
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


EXPECTED = {
    36: ('a10b1289edc59df08ccc9a3b6cf1e81f803a8041fa414fc1c6375a1d017eca96',
         'ev_71a46cb021e0f657859b13c2e95e4bb39508ec441851dcc0b91bea490d0b5922',
         None, (1, 48, 1033, (0,), 0, True)),
    37: ('917d909cbb205293dd3020e24d3c33b0d6b3cfed3553dd6fbc86b5a56f40dc85',
         'ev_f4a84eba2ceb19f9af6de5c061c6b147e1023136fdf21960851219e23e90ba50',
         (850, 1, 2), (2, 48, 1033, (), None, None)),
    38: ('bf6cd6935ced0d3942d80dd2e1d834e4df4c2207113dbbe7a8877a063f20d6ed',
         'ev_e1d4ee6634880000941c45f3b0c86afc649d8b8bcdd57b01e0c98e141275374c',
         (846, 48, 47), (1, 47, 1033, (0,), 0, False)),
    39: ('73432e0ce2524e12970bb0155d478214736bf97e0a173a5a87b7d5aeb810ed97',
         'ev_f7ce61a5f70a94527373f4385ca8f0172e90daaa27367a48b8d4e3d4632b1910',
         (608, 9, 12), (1, 48, 1036, (0,), None, None)),
}

def check_saved(round_id):
    expected_hash, evidence_id, _, expected_state = EXPECTED[round_id]
    fixture = root / f'fixtures/pe-r{round_id}/fixture.exe'
    raw_path = root / f'live/runs/round-{round_id}/inspection.raw.json'
    raw_bytes = raw_path.read_bytes()
    record = json.loads(raw_bytes)
    data, decoded = parse(fixture)
    assert sha(data) == expected_hash
    assert record['evidence_id'] == evidence_id
    assert record['operation'] == 'inspect_pe_resources'
    assert record['subject']['digest']['sha256'] == expected_hash
    reported = record['normalized_result']
    assert reported['artifact']['sha256'] == expected_hash
    assert reported['artifact']['bytes'] == len(data)
    for key in decoded:
        assert reported[key] == decoded[key], f'r{round_id}: {key}'
    image = decoded['icon_groups'][0]['images'][0]
    assert len(decoded['resources']) == 2 and len(decoded['icon_groups']) == 1
    actual_state = (image['resource_id'], image['declared_bytes'],
                    decoded['resources'][0]['language']['id'],
                    tuple(image['candidate_resource_indices']),
                    image['same_language_resource_index'], image['size_matches'])
    assert actual_state == expected_state, f'r{round_id}: state'
    receipt = json.loads((root / f'live/runs/round-{round_id}/producer-receipt.json').read_text())
    assert receipt['exit_code'] == 0 and receipt['fixture_sha256'] == expected_hash
    assert receipt.get('stdout_sha256', receipt.get('raw_output_sha256')) == sha(raw_bytes)
    if round_id != 36:
        assert receipt['evidence_id'] == evidence_id
    return data, record, actual_state

def main():
    rows = {r: check_saved(r) for r in EXPECTED}
    baseline = rows[36][0]
    for r in (37, 38, 39):
        current = rows[r][0]
        assert len(current) == len(baseline) == 1024
        assert [(i, x, y) for i, (x, y) in enumerate(zip(baseline, current)) if x != y] == [EXPECTED[r][2]]
    assert len({rows[r][2] for r in EXPECTED}) == 4
    forged = copy.deepcopy(rows[37][1])
    forged['normalized_result']['icon_groups'][0]['images'][0]['candidate_resource_indices'] = [0]
    try:
        _, expected = parse(root / 'fixtures/pe-r37/fixture.exe')
        assert forged['normalized_result']['icon_groups'] == expected['icon_groups']
    except AssertionError:
        pass
    else:
        raise AssertionError('forged candidate accepted')
    print('PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED')

if __name__ == '__main__':
    main()
