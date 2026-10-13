# Round 31 independent non-author review — static PE resource inventory

**Result: PASS for the declared, fixture-scoped coverage claim.** I did not invoke REA, execute the PE, or rely on `truth.json` for the oracle. The corrected on-disk fixture independently decodes to exactly two authored resources; all independently derived source identities and byte locations match saved Evidence ID `ev_dd2627a0bc00b597eeecd066ada29a6b20e86d8d2dc19b7bf2aa517465595a24`. Full-resource precision **2/2** and recall **2/2**, with no extra or conflated entry. This supports a narrow coverage improvement over round 30's single resource; it is not proof of general PE parser correctness, runtime behavior, or native provider readiness.

## Reproducible commands and byte-level oracle

Run from the repository root (read-only; `python3` standard library only):

```bash
sha256sum .shokunin/revenger/corpus/fixtures/pe-r{30,31}/fixture.exe
python3 - <<'PY'
import hashlib, json, struct
from pathlib import Path
root = Path('.shokunin/revenger/corpus')
f = root/'fixtures/pe-r31/fixture.exe'
b = f.read_bytes()
e = json.loads((root/'live/runs/round-31/inspection.json').read_text())
rd = lambda fmt, off: struct.unpack_from('<'+fmt, b, off)
pe, = rd('I', 0x3c)
assert b[:2] == b'MZ' and b[pe:pe+4] == b'PE\0\0'
machine, sections, _, _, _, opt_size, _ = rd('HHIIIHH', pe+4)
opt = pe+24
assert rd('H', opt)[0] == 0x10b
rva, resource_size = rd('II', opt+96+8*2)
sec = opt+opt_size
name, virtual_size, va, raw_size, raw_off, *_ = rd('8sIIIIIIHHI', sec)
assert sections == 1 and name.rstrip(b'\0') == b'.rsrc'
def off(r):
    assert va <= r < va+min(virtual_size, raw_size)
    return raw_off+r-va
base = off(rva)
folders, rows = [], []
def walk(rel, path=(), entry_offsets=()):
    d = base+rel
    _, _, _, _, named, ids = rd('IIHHHH', d)
    folders.append((d, 16+8*(named+ids), named, ids))
    for i in range(named+ids):
        entry = d+16+i*8
        key, child = rd('II', entry)
        assert key < 0x80000000
        if child & 0x80000000:
            walk(child & 0x7fffffff, path+(key,), entry_offsets+(entry,))
        else:
            data = base+child
            payload_rva, size, code_page, reserved = rd('IIII', data)
            location = off(payload_rva)
            payload = b[location:location+size]
            assert len(path) == 2 and len(payload) == size
            rows.append((path+(key,), entry_offsets+(entry,), data,
                         payload_rva, location, size, hashlib.sha256(payload).hexdigest(),
                         code_page, reserved))
walk(0)
n = e['normalized_result']
saved = [((r['type']['id'],r['name']['id'],r['language']['id']),
          tuple(x['offset'] for x in r['entry_locations']),
          r['data_entry_location']['offset'],r['payload']['rva'],
          r['payload']['location']['offset'],r['payload']['location']['bytes'],
          r['payload']['sha256'],r['code_page'],r['reserved']) for r in n['resources']]
assert len(rows) == len(saved) == 2 and set(rows) == set(saved)
assert n['artifact']['sha256'] == e['subject']['digest']['sha256'] == hashlib.sha256(b).hexdigest()
assert n['artifact']['bytes'] == len(b) == 1024
assert n['directory'] == {'rva':rva,'location':{'offset':base,'bytes':resource_size},'data_directory_location':{'offset':opt+112,'bytes':8}}
assert [(x['location']['offset'],x['location']['bytes'],x['named_entries'],x['id_entries']) for x in n['directories']] == folders
assert all(x['bytes'] == 8 for r in n['resources'] for x in r['entry_locations'])
assert all(r['data_entry_location']['bytes'] == 16 for r in n['resources'])
assert n['coverage'] == {'status':'complete','examined_entries':5,'resources':2} and n['icon_groups'] == []
print('header', hex(pe), hex(machine), 'resource',rva,base,resource_size,virtual_size)
print('file',len(b),hashlib.sha256(b).hexdigest())
print('folders',folders)
print('resources',rows)
print('precision 2/2 recall 2/2, all locations and digests agree')
PY
python3 - <<'PY'
import json
from pathlib import Path
p=Path('.shokunin/revenger/corpus/live/runs')
a=json.loads((p/'round-31/attempt-invalid.json').read_text())
r30=json.loads((p/'round-30/inspection.json').read_text())['normalized_result']
print('refusal:',a['code'],a['details']['issues'][0]['message'])
print('r30 resource count:',len(r30['resources']), 'directory bytes:',r30['directory']['location']['bytes'])
PY
```

Observed PE header: MZ, PE32 magic `0x10b`, machine `0x14c`, one `.rsrc` section; section RVA 8192, raw offset 512, virtual size 208 and raw size 512. PE resource data directory at file offset 200 is `(RVA 8192, size 208)`; its file bytes occupy `[512:720)`. Root directory `(512,24)` has one numeric type; type directory `(536,32)` has two numeric names; the two language directories `(568,24)` and `(592,24)` have one numeric language each. Five entry records total. The copied r30 baseline has one resource, resource-directory/virtual size 103, and source file SHA `b94d840aa7eb952474b30260bc70e092fb1db832b0aa1bc393936d8dc4ce661a`; r31 SHA is `714369ff1bfcd2e04a5f6c32f938778b38c6c455ae6a019b51e6c2d702510b47`. Both files are 1024 bytes. The r31 change is a tree rebuild, not a one-byte mutation; no claim that all nonheader bytes are unchanged.

| Source-decoded type/name/language | Entry offsets (8 bytes each) | Data entry (16 bytes) | Payload RVA / file range | Payload SHA-256 | Saved evidence |
|---|---|---|---|---|---|
| `10/2/1036` | `528,552,584` | `616` | `8352 / [672:687)` (15 bytes) | `071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229` | exact match |
| `10/3/1033` | `528,560,608` | `632` | `8384 / [704:719)` (15 bytes) | `cc29ca16da56975bf9fb034fbc010e377076ada5df6395622c8ffd9fed19f67e` | exact match |

Each payload SHA was computed from its raw 15-byte slice. In both records saved `code_page=0`, `reserved=0`; directory counts/locations, resource entry lengths, data-entry lengths, artifact format `pe32`, artifact SHA/size and both payload RVA→file mappings agree with the bytes. Distinct file ranges and hashes establish no swapped or conflated payload. `truth.json` describes the same identities but was not an input to the oracle or score. Precision is matching reported resources / all reported resources = 2/2; recall is matching reported resources / independently decoded resources = 2/2.

## Refusal and scope

`attempt-invalid.json` reports `invalid_request`, `invalid_format`, and “Resource range leaves its section's virtual size.” This first call is a **failed, unscored attempt** with no Evidence ID; the originally rejected fixture bytes are not retained, so its precise byte state and producer exit code cannot be verified independently. The corrected on-disk fixture has section virtual size 208 (r30 has 103), consistent with the documented repair, and `inspection.json` contains the successful saved record. Empty `inspection.stderr` is consistent with a clean second call but neither saved JSON nor empty stderr authenticates process exit status.

**Observation:** The source bytes, local hashes and saved static REA record agree on precisely two RCDATA (`type 10`) identities and their payload byte ranges. **Inference:** This parser distinguished two independently addressed resource entries in this one constructed PE32 file, beyond the r30 single-entry baseline. **Unknown:** PE execution/loader acceptance, language fallback, decoded semantics of opaque payloads, shell/window effects, native code behavior, untested PE formats, general parser accuracy and invocation provenance beyond the saved artifacts. The original r1 native-provider refusal is not repaired. Coverage improves only for the declared provider-neutral static two-resource fixture route; depth and calibration are not established as improved by this review.
