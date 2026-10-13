from pathlib import Path
import hashlib, json, struct

root = Path('/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus')
p52 = root / 'fixtures/pe-r52/fixture.exe'
p53 = root / 'fixtures/pe-r53/fixture.exe'
run = root / 'live/runs/round-53'
raw_path = run / 'inspection.raw.json'
receipt_path = run / 'producer-receipt.json'
sha = lambda blob: hashlib.sha256(blob).hexdigest()
a, b = p52.read_bytes(), p53.read_bytes()
raw_bytes = raw_path.read_bytes()
record, receipt = json.loads(raw_bytes), json.loads(receipt_path.read_bytes())
assert len(a) == len(b) == 1024
assert [(i, a[i], b[i]) for i in range(len(b)) if a[i] != b[i]] == [(850, 1, 2)]
assert sha(a) == '9297adec215ef401538dad04f06e249a41d3747e14b996a837164a2dde3d070d'
assert sha(b) == '9802fb978930d7539f9fd2e64b25d2e7de3895c9988d8118c0cd3bdc2ab65b5e'

# All offsets here are decoded from the PE header/section table and .rsrc directory entries.
def decode(blob):
    u16 = lambda off: struct.unpack_from('<H', blob, off)[0]
    u32 = lambda off: struct.unpack_from('<I', blob, off)[0]
    assert blob[:2] == b'MZ'
    pe = u32(0x3c)
    assert blob[pe:pe+4] == b'PE\0\0'
    machine, nsections = u16(pe+4), u16(pe+6)
    opt = pe + 24
    assert u16(opt) == 0x20b # PE32+
    section_off = opt + u16(pe+20)
    sections = []
    for i in range(nsections):
        s = section_off + 40*i
        sections.append((u32(s+12), u32(s+8), u32(s+20), u32(s+16)))
    def mapped(rva, size):
        matches = [p + rva - v for v, virtual_size, p, raw_size in sections
                   if v <= rva and rva + size <= v + min(virtual_size, raw_size)]
        assert len(matches) == 1 and matches[0] + size <= len(blob)
        return matches[0]
    data_dir = opt + 112 + 8*2 # optional-header resource data directory
    root_rva, root_size = struct.unpack_from('<II', blob, data_dir)
    base = mapped(root_rva, root_size)
    directories, resources = [], []
    def traverse(relative, path, entries):
        off = base + relative
        assert base <= off and off + 16 <= base + root_size
        fields = struct.unpack_from('<IIHHHH', blob, off)
        count = fields[-2] + fields[-1]
        assert off + 16 + 8*count <= base + root_size
        directories.append(dict(location=dict(offset=off, bytes=16+8*count),
                                characteristics=fields[0], timestamp=fields[1],
                                major_version=fields[2], minor_version=fields[3],
                                named_entries=fields[4], id_entries=fields[5]))
        for i in range(count):
            entry = off + 16 + i*8
            key, target = struct.unpack_from('<II', blob, entry)
            if key & 0x80000000:
                noff = base + (key & 0x7fffffff)
                units = u16(noff)
                assert base <= noff and noff + 2 + 2*units <= base + root_size
                encoded = blob[noff+2:noff+2+2*units]
                ident = dict(kind='name', name=encoded.decode('utf-16-le'),
                             utf16le_hex=encoded.hex(), location=dict(offset=noff, bytes=2+2*units))
            else:
                ident = dict(kind='id', id=key)
            next_entries = entries + [dict(offset=entry, bytes=8)]
            if target & 0x80000000:
                assert len(path) < 2
                traverse(target & 0x7fffffff, path+[ident], next_entries)
            else:
                assert len(path) == 2
                de = base + target
                assert base <= de and de + 16 <= base + root_size
                rva, size, page, reserved = struct.unpack_from('<IIII', blob, de)
                poff = mapped(rva, size)
                resources.append(dict(index=len(resources), type=path[0], name=path[1],
                                      language=ident, entry_locations=next_entries,
                                      data_entry_location=dict(offset=de, bytes=16),
                                      code_page=page, reserved=reserved,
                                      payload=dict(rva=rva, location=dict(offset=poff, bytes=size),
                                                   sha256=sha(blob[poff:poff+size]))))
    traverse(0, [], [])
    groups = []
    for res in resources:
        if res['type'] != dict(kind='id', id=14):
            continue
        loc = res['payload']['location']; off = loc['offset']; size = loc['bytes']
        reserved, kind, count = struct.unpack_from('<HHH', blob, off)
        assert reserved == 0 and kind == 1 and 6+14*count == size
        images = []
        for i in range(count):
            e = off+6+14*i
            width, height, colors, pad, planes, bits, length, rid = struct.unpack_from('<BBBBHHIH', blob, e)
            candidates = [r['index'] for r in resources
                          if r['type'] == dict(kind='id', id=3) and r['name'] == dict(kind='id', id=rid)]
            same = next((j for j in candidates if resources[j]['language'] == res['language']), None)
            images.append(dict(location=dict(offset=e, bytes=14), width=width, height=height,
                               color_count=colors, reserved=pad, planes=planes, bit_count=bits,
                               declared_bytes=length, resource_id=rid,
                               candidate_resource_indices=candidates,
                               same_language_resource_index=same,
                               size_matches=None if same is None else resources[same]['payload']['location']['bytes'] == length))
        groups.append(dict(resource_index=res['index'], images=images))
    return dict(format='pe32-plus', machine=machine,
                directory=dict(rva=root_rva, location=dict(offset=base, bytes=root_size),
                               data_directory_location=dict(offset=data_dir, bytes=8)),
                directories=directories, resources=resources, icon_groups=groups)

prior, current = decode(a), decode(b)
assert current == {k: record['normalized_result'][k] for k in current}
assert prior['directory'] == current['directory']
assert prior['directories'] == current['directories']
assert prior['resources'][0] == current['resources'][0]
assert prior['resources'][1]['name'] == current['resources'][1]['name']
assert prior['resources'][1]['language'] == current['resources'][1]['language'] == dict(kind='id', id=1033)
assert prior['resources'][1]['payload']['location'] == current['resources'][1]['payload']['location']
assert prior['icon_groups'][0]['images'][0]['resource_id'] == 1
assert current['icon_groups'][0]['images'][0]['resource_id'] == 2
assert current['resources'][1]['name'] == dict(kind='name', name='A😀B!',
    utf16le_hex='41003dd800de42002100', location=dict(offset=736, bytes=12))
assert current['resources'][1]['entry_locations'] == [dict(offset=o, bytes=8) for o in (536, 584, 632)]
assert current['resources'][0]['payload'] == dict(rva=8448, location=dict(offset=768, bytes=48),
    sha256='d7aaca7bc7951c9249a7798838189374fa953d3def03aebb375ee731768e5003')
assert current['resources'][1]['payload'] == dict(rva=8512, location=dict(offset=832, bytes=20),
    sha256='3a05333329e38ad829edf1753f7e12de8a4ee0a9a63143d1da49203808ae6f76')
assert current['icon_groups'] == [dict(resource_index=1, images=[dict(
    location=dict(offset=838, bytes=14), width=1, height=1, color_count=0,
    reserved=0, planes=1, bit_count=32, declared_bytes=48, resource_id=2,
    candidate_resource_indices=[], same_language_resource_index=None, size_matches=None)])]
assert record['normalized_result']['artifact'] == dict(path=str(p53), sha256=sha(b), bytes=len(b))
assert record['normalized_result']['coverage'] == dict(status='complete', examined_entries=6, resources=2)
assert record['subject']['digest']['sha256'] == sha(b)
assert record['subject']['local_path'] == str(p53)
assert record['operation'] == 'inspect_pe_resources'
assert record['parameters']['path'] == str(p53)
assert receipt['command'] == f'npx -y rea-agents@6.4.0 inspect-pe-resources {p53} --format json'
assert receipt['exit_code'] == 0
assert receipt['stdout_sha256'] == sha(raw_bytes)
assert receipt['fixture_sha256'] == sha(b)
assert receipt['evidence_id'] == record['evidence_id']
print('PASS: static PE resource decode, sole byte delta, saved result and receipt hashes')
