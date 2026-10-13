from pathlib import Path
import hashlib, json, struct

root = Path('.shokunin/revenger/corpus')
run = root / 'live/runs/round-34'

def decode(path):
    blob = path.read_bytes()
    def read(off, size):
        assert 0 <= off <= len(blob) and size >= 0 and off + size <= len(blob), (off, size)
        return blob[off:off+size]
    def unpack(fmt, off):
        return struct.unpack(fmt, read(off, struct.calcsize(fmt)))
    def loc(off, size):
        return {'offset': off, 'bytes': size}
    assert read(0, 2) == b'MZ'
    pe = unpack('<I', 0x3c)[0]
    assert read(pe, 4) == b'PE\0\0'
    machine, section_count, _, _, _, opt_size, _ = unpack('<HHIIIHH', pe+4)
    opt = pe+24
    assert unpack('<H', opt)[0] == 0x10b
    assert unpack('<I', opt+92)[0] >= 3  # number of data directories
    dd = opt+96+8*2
    rva, directory_size = unpack('<II', dd)
    sections = []
    for i in range(section_count):
        s = opt+opt_size+40*i
        name = read(s, 8).rstrip(b'\0').decode('ascii')
        virtual_size, virtual_address, raw_size, raw_offset = unpack('<IIII', s+8)
        sections.append((name, virtual_address, virtual_size, raw_offset, raw_size))
    def rva_to_off(addr, size):
        for _, va, vs, off, rs in sections:
            delta = addr-va
            if 0 <= delta and delta+size <= rs and delta+size <= max(rs, vs):
                read(off+delta, size)
                return off+delta
        raise ValueError(('unmapped RVA', addr, size))
    base = rva_to_off(rva, directory_size)
    directories, resources = [], []
    visited, examined = set(), 0
    def item(raw, level):
        if not raw & 0x80000000:
            return {'kind':'id', 'id':raw & 0xffff}
        offset = base+(raw & 0x7fffffff)
        count = unpack('<H', offset)[0]
        value = read(offset+2, 2*count)
        return {'kind':'name', 'name':value.decode('utf-16le'),
                'utf16le_hex':value.hex(), 'location':loc(offset, 2+len(value))}
    def walk(relative, trail, locations):
        nonlocal examined
        off = base+relative
        assert relative not in visited and len(trail) < 3
        visited.add(relative)
        _, timestamp, major, minor, named, ids = unpack('<IIHHHH', off)
        count = named+ids
        read(off, 16+8*count)
        directories.append({'location':loc(off, 16+8*count),
            'characteristics':unpack('<I', off)[0], 'timestamp':timestamp,
            'major_version':major, 'minor_version':minor,
            'named_entries':named, 'id_entries':ids})
        for i in range(count):
            e = off+16+8*i
            name_raw, target = unpack('<II', e)
            assert bool(name_raw & 0x80000000) == (i < named)
            component = item(name_raw, len(trail))
            examined += 1
            if target & 0x80000000:
                walk(target & 0x7fffffff, trail+[component], locations+[loc(e, 8)])
            else:
                assert len(trail) == 2
                de = base+target
                payload_rva, payload_size, code_page, reserved = unpack('<IIII', de)
                payload_off = rva_to_off(payload_rva, payload_size)
                resources.append({'index':len(resources), 'type':trail[0],
                    'name':trail[1], 'language':component,
                    'entry_locations':locations+[loc(e, 8)],
                    'data_entry_location':loc(de, 16), 'code_page':code_page,
                    'reserved':reserved, 'payload':{'rva':payload_rva,
                    'location':loc(payload_off, payload_size),
                    'sha256':hashlib.sha256(read(payload_off,payload_size)).hexdigest()}})
    walk(0, [], [])
    return {'artifact':{'path':str(path.resolve()),
        'sha256':hashlib.sha256(blob).hexdigest(), 'bytes':len(blob)},
        'format':'pe32', 'machine':machine,
        'directory':{'rva':rva,'location':loc(base,directory_size),
                     'data_directory_location':loc(dd,8)},
        'directories':directories, 'resources':resources,
        'icon_groups':[], 'coverage':{'status':'complete',
                           'examined_entries':examined,'resources':len(resources)}}

current = decode(root/'fixtures/pe-r34/fixture.exe')
previous = decode(root/'fixtures/pe-r33/fixture.exe')
saved = json.loads((run/'inspection.json').read_text())
saved33 = json.loads((root/'live/runs/round-33/inspection.json').read_text())
for label, decoded, record in [('r34',current,saved),('r33',previous,saved33)]:
    got = record['normalized_result']
    assert all(decoded[k] == got[k] for k in decoded), label
    assert decoded['coverage'] == {'status':'complete','examined_entries':5,'resources':2}
    print(label, decoded['artifact'], 'name', decoded['resources'][0]['name'])
a = (root/'fixtures/pe-r34/fixture.exe').read_bytes()
b = (root/'fixtures/pe-r33/fixture.exe').read_bytes()
changes = [(i,x,y) for i,(x,y) in enumerate(zip(b,a)) if x != y]
assert len(a) == len(b) == 1024
assert changes == [(738,67,65),(740,65,61),(741,0,216),(742,70,0),(743,0,222),(744,201,66)]
assert a[736:748].hex() == '050041003dd800de42002100'
assert b[736:748].hex() == '0500430041004600c9002100'
assert current['resources'][0]['name']['name'] == 'A\U0001f600B!'
assert previous['resources'][0]['name']['name'] == 'CAFÉ!'
assert current['resources'][1:] == previous['resources'][1:]
assert current['resources'][0]['payload'] == previous['resources'][0]['payload']
print('changed bytes', changes)
print('resources', json.dumps(current['resources'], ensure_ascii=False))
print('precision=2/2, recall=2/2 (exact identity, locations, payload digests); no mismatch')
