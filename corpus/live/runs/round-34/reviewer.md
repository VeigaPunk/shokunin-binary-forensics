# Round 34 independent PE byte review

**Verdict: PASS — exact resource precision 2/2 and recall 2/2.** Against an independent parse of the shipped fixture's bytes, the saved REA result has two matching resource records, zero false positives and zero omissions. This is a static inventory verdict for this fixture, not a runtime/Unicode-generalization claim. Evidence ID: `ev_93770df76abe2cec23c8c0708cda054d3ad2a3fb6bb495d267703d0afd136bd3` (`inspect_pe_resources`, saved `inspection.json`); baseline Evidence ID: `ev_50a1273217e51aa8f8f1c204f759582b840dfb8a455e8758ca2f1ba413db90bc`.

## Independent observations and comparison

- Artifact: `.shokunin/revenger/corpus/fixtures/pe-r34/fixture.exe`, 1024 bytes, SHA-256 `28182338af9da23b7dc0d6c1b64b325bb635a25f8b336c1d278884ffa88f2e85`. The saved subject name `fixture.exe`, subject format `pe`, null architecture, absolute local path, artifact path/size/digest, provider `rea-pe-resources` version `1`, operation `inspect_pe_resources`, confidence `observed`, authority `shipped-artifact`, null analysis profile/environment/raw result, and artifact-path location agree with this static file and the saved record; provider attribution, operation and confidence are *saved metadata*, not independently provable from bytes.
- DOS `MZ`, PE signature at file offset 64, COFF machine 332 (`0x14c`), one section, PE32 optional magic `0x10b` at offset 88, optional-header size 224. Resource data-directory location `[200,208)`: RVA 8192 (`0x2000`), size 240; `.rsrc` RVA 8192 maps to raw file offset 512 with raw size 512. Normalized directory location `[512,752)` matches.
- Normalized resource directories: `[512,536)` has named/ID entries 0/1; `[536,568)` has 1/1; `[568,592)` has 0/1; `[592,616)` has 0/1. Each independently parsed directory has characteristics/timestamp/major/minor all zero. All directory offsets, lengths and counts match REA.
- Resource index 0: type ID 10; name `A😀B!` from UTF-16LE bytes `41003dd800de42002100` (five code units including surrogate pair) at name-field `[736,748)`; language ID 1036. Entry locations `[528,536)`, `[552,560)`, `[584,592)`; data entry `[616,632)`; code page/reserved 0/0. Payload RVA 8352 (`0x20a0`) maps to `[672,687)` (15 bytes), SHA-256 `071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229`. All normalized identity, name hex/location, entry/data locations, RVA/file location, length and digest match.
- Resource index 1: type ID 10, name ID 3, language ID 1033. Entry locations `[528,536)`, `[560,568)`, `[608,616)`; data entry `[632,648)`; code page/reserved 0/0. Payload RVA 8384 (`0x20c0`) maps to `[704,719)` (15 bytes), SHA-256 `cc29ca16da56975bf9fb034fbc010e377076ada5df6395622c8ffd9fed19f67e`. Every normalized field matches.
- `icon_groups` is empty; neither resource is a group-icon type. Normalized coverage is `{"status":"complete","examined_entries":5,"resources":2}`; the independent traversal confirms five entries and two leaves for this tree. This does not establish completeness for other binaries.
- Baseline r33 file: 1024 bytes, SHA-256 `997089c388e1e3a686f736bcd459288ea4422f86c50ec45ad1cb4ca05c876cc8`. Its independently decoded name is `CAFÉ!` (`430041004600c9002100` at `[738,748)`), with the same five-code-unit length and all other tree/payload fields unchanged. Exactly six changed file bytes: `(offset, r33, r34)` = `(738,67,65)`, `(740,65,61)`, `(741,0,216)`, `(742,70,0)`, `(743,0,222)`, `(744,201,66)`. This independently agrees with authored `pe-r34/truth.json`; truth was not used as the byte oracle. Both normalized r33/r34 results agree with the respective byte decodes.
- Saved normalized limitations and top-level limitations are identical: “Static PE32/PE32+ type/name/language resource inventory; payloads other than RT_GROUP_ICON remain opaque.” “Icon candidates are resource-table relationships. Language fallback, image decoding and actual shell/window loading are not observed.” “Exact shared byte ranges are retained; non-identical overlapping resource structures or payloads are rejected.” The decoder below confirms this one valid fixture; it does **not** test parser behavior on malicious/overlapping inputs.

## Runnable independent reproducer

Run from the repository root with `python3 - <<'PY'` followed by the code below and a closing line `PY`, or save the code as a temporary script and run `python3 script.py`. Standard library only. This parses PE headers, section RVA mapping, resource directory entries, UTF-16LE name and payload bytes directly; it does not consult truth JSON or invoke REA. It asserts equality for every decoded normalized field of both saved records, checks exact r33→r34 byte differences and prints the verdict.

```python
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
```

**Limits:** No target execution, Windows loader/shell observation, resource content interpretation, authentication of saved REA producer metadata, arbitrary Unicode generalization, malformed surrogate behavior, or broad malformed-PE parser testing. The payload bytes are hashed and located, not semantically decoded. The independent decoder is scoped to a PE32 file with resource section RVA mapping and this three-level type/name/language tree; it is not claimed as a general-purpose PE validator.
