# Round 33 independent raw-byte PE resource review

**Verdict: PASS, bounded to this fixture.** Static raw-byte parsing of both PE files found exactly two resource leaves each. Round 33's saved `inspection.json` agrees with both leaves, all five tree entries, directory positions/counts, name bytes/location, payload offsets/lengths/digests, artifact identity, and the independently decoded PE header. No extra resource entries were found. Precision = 2/2 = **1.00**; recall = 2/2 = **1.00** for full resource identities and payloads in this authored fixture. No PE binary was executed; the REA producer was not rerun.

## Evidence and observations

- **OBSERVATION**: Direct SHA-256 of `corpus/fixtures/pe-r32/fixture.exe` = `5169ac55c0b145b41c58b72848f694111c325d2c084266ef9d6c8763ce99adbd`; `pe-r33/fixture.exe` = `997089c388e1e3a686f736bcd459288ea4422f86c50ec45ad1cb4ca05c876cc8`. Both are 1024 bytes. Those hashes match the respective authored truths and subjects/artifacts in inspection records. Both records have `operation=inspect_pe_resources`, `provider.id=rea-pe-resources`, and absolute subject paths resolving to the two files. Saved r32 Evidence ID: `ev_dcc2411a94ff88169c18f1db3d70ad0792bbccb059dec89bec0df3a578ef653d`; saved r33 Evidence ID: `ev_50a1273217e51aa8f8f1c204f759582b840dfb8a455e8758ca2f1ba413db90bc`. An Evidence ID labels the saved record; it is not a cryptographic authentication claim.
- **OBSERVATION**: Comparing the full 1024-byte files yields *exactly* five differences: offsets `738: 0x41→0x43`, `740: 0x4c→0x41`, `742: 0x50→0x46`, `744: 0x48→0xc9`, `746: 0x41→0x21`. Odd-position high bytes remain zero. At name-length field offset 736 the unmodified little-endian value is five UTF-16 code units; raw name bytes at `[738,748)` change from `41004c00500048004100` (`ALPHA`) to `430041004600c9002100` (`CAFÉ!`). The name record starts at offset 736 and occupies 12 bytes; the name tree entry is at 552. The r33 authored `changed_offsets`, name and hex agree.
- **OBSERVATION**: Both PE32 headers say machine 332; resource data-directory field is at offset 200 and specifies RVA 8192, size 240. Section RVA mapping resolves this resource directory to file offset 512. Four reachable directory records appear at `(offset, named, numeric) = (512,0,1), (536,1,1), (568,0,1), (592,0,1)`. Their sizes are 24, 32, 24, 24 bytes, respectively. The directory entry traversal counts **five** entries, ending at exactly two leaves; this matches each inspection's `coverage.examined_entries=5`, `coverage.resources=2`, and `coverage.status=complete`.
- **OBSERVATION**: The first r33 resource resolves type ID **10**, name **`CAFÉ!`**, language ID **1036** through tree entry offsets **528, 552, 584**. Data-entry offset **616** gives payload RVA **8352**, mapped file offset **672**, length **15**, SHA-256 `071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229`. The r32 leaf has the same tree/data/payload identity except its name `ALPHA` and hex. The second resource in both versions resolves type ID **10**, numeric name ID **3**, language ID **1033**, tree entries **528, 560, 608**, data entry **632**, payload RVA **8384**, offset **704**, length **15**, SHA-256 `cc29ca16da56975bf9fb034fbc010e377076ada5df6395622c8ffd9fed19f67e`. Data-entry `code_page` and `reserved` are zero. All these raw-byte findings match both saved inspections and corresponding truth JSON.
- **INFERENCE**: The saved REA parser output is accurate for this one Unicode resource-name change. Since the raw files differ only in these five bytes, unchanged payload and tree metadata are attributable to the unchanged bytes, not inferred behavior.
- **UNKNOWN / limits**: The reproducibility check does not establish the genuine provenance of the saved REA JSON/Evidence IDs or verify a producer invocation. It does not test arbitrary Unicode, surrogate pairs, malformed PE structures, overlapping resources, Windows loader behavior, resource content semantics, target execution, or coverage of bytes outside the traversed resource directory. Resource recall is against this exact reachable PE resource tree, not arbitrary undocumented embedded data. No REA producer or PE binary was executed in this review.

## Executable reproducer

Run from repository root: copy the fenced code to a Python file and run `python3 <file>`. It uses only Python's standard library, independently decodes PE headers/section RVA translation/resource directory pointers and bytes, then compares derived values with both authored truths and the two saved inspection records.

```python
from pathlib import Path
import hashlib, json, struct
B=Path('.shokunin/revenger/corpus')
def sha(b): return hashlib.sha256(b).hexdigest()
def decode(path):
    b=path.read_bytes()
    def u16(o): return struct.unpack_from('<H',b,o)[0]
    def u32(o): return struct.unpack_from('<I',b,o)[0]
    pe=u32(0x3c)
    assert b[:2]==b'MZ' and b[pe:pe+4]==b'PE\0\0'
    coff=pe+4; machine=u16(coff); nsec=u16(coff+2); opt=coff+20
    assert u16(opt)==0x10b # PE32 fixture
    dd=opt+96+2*8; rva,sz=struct.unpack_from('<II',b,dd)
    sections=[]
    for i in range(nsec):
        s=opt+u16(coff+16)+40*i
        sections.append((u32(s+12),u32(s+8),u32(s+20),u32(s+16)))
    def fileoff(v,n=1):
        match=[raw+(v-va) for va,virt,raw,rsz in sections if va<=v and v+n<=va+rsz and v+n<=va+max(virt,rsz)]
        assert len(match)==1 and match[0]+n<=len(b), (v,n,match)
        return match[0]
    base=fileoff(rva,sz)
    dirs=[]; resources=[]; total=0
    def key(k):
        if not k&0x80000000: return {'kind':'id','id':k}
        o=base+(k&0x7fffffff); units=u16(o); raw=b[o+2:o+2+units*2]
        assert len(raw)==units*2
        return {'kind':'name','name':raw.decode('utf-16le'),'utf16le_hex':raw.hex(),'location':{'offset':o,'bytes':2+len(raw)}}
    def walk(rel, ancestors, locations):
        nonlocal total
        o=base+rel
        named,ids=u16(o+12),u16(o+14)
        assert o+16+8*(named+ids)<=base+sz
        dirs.append({'location':{'offset':o,'bytes':16+8*(named+ids)}, 'named_entries':named,'id_entries':ids,'characteristics':u32(o),'timestamp':u32(o+4),'major_version':u16(o+8),'minor_version':u16(o+10)})
        for j in range(named+ids):
            total+=1; e=o+16+8*j; k,target=struct.unpack_from('<II',b,e)
            assert bool(k&0x80000000)==(j<named)
            path=ancestors+[key(k)]; loc=locations+[{'offset':e,'bytes':8}]
            if target&0x80000000:
                assert len(path)<3
                walk(target&0x7fffffff,path,loc)
            else:
                assert len(path)==3
                d=base+target; prva,n,cp,res=struct.unpack_from('<IIII',b,d)
                po=fileoff(prva,n)
                resources.append({'type':path[0],'name':path[1],'language':path[2], 'entry_locations':loc,'data_entry_location':{'offset':d,'bytes':16},'code_page':cp,'reserved':res,'payload':{'rva':prva,'location':{'offset':po,'bytes':n},'sha256':sha(b[po:po+n])}})
    walk(0,[],[])
    return b, {'sha256':sha(b),'bytes':len(b),'format':'pe32','machine':machine,'directory':{'rva':rva,'location':{'offset':base,'bytes':sz},'data_directory_location':{'offset':dd,'bytes':8}},'directories':dirs,'resources':resources,'examined_entries':total}
old, a=decode(B/'fixtures/pe-r32/fixture.exe')
new, z=decode(B/'fixtures/pe-r33/fixture.exe')
assert len(old)==len(new)==1024
changes=[{'offset':i,'before':x,'after':y} for i,(x,y) in enumerate(zip(old,new)) if x!=y]
assert changes==[{'offset':738,'before':65,'after':67},{'offset':740,'before':76,'after':65},{'offset':742,'before':80,'after':70},{'offset':744,'before':72,'after':201},{'offset':746,'before':65,'after':33}]
assert new[736:738]==b'\x05\x00' and new[738:748].hex()=='430041004600c9002100'
for label,raw,ind in [('r32',old,a),('r33',new,z)]:
    t=json.loads((B/f'fixtures/pe-{label}/truth.json').read_text())
    insp=json.loads((B/f'live/runs/round-{label[1:]}/inspection.json').read_text())
    nr=insp['normalized_result']
    assert t['sha256']==ind['sha256']==insp['subject']['digest']['sha256']==nr['artifact']['sha256']
    assert insp['subject']['local_path']==str((B/f'fixtures/pe-{label}/fixture.exe').resolve())
    assert insp['operation']=='inspect_pe_resources' and insp['provider']['id']=='rea-pe-resources'
    assert nr['artifact']['bytes']==ind['bytes'] and nr['format']==ind['format'] and nr['machine']==ind['machine']
    assert nr['directory']==ind['directory'] and nr['directories']==ind['directories']
    assert len(ind['resources'])==len(t['resources'])==len(nr['resources'])==2
    assert ind['examined_entries']==nr['coverage']['examined_entries']==5
    assert nr['coverage']['resources']==2 and nr['coverage']['status']=='complete'
    for i,(item,truth,report) in enumerate(zip(ind['resources'],t['resources'],nr['resources'])):
        assert report['index']==i
        for field in ('type','name','language','entry_locations','data_entry_location','code_page','reserved','payload'):
            assert item[field]==report[field],(label,i,field,item[field],report[field])
        assert item['type']=={'kind':'id','id':truth['type_id']}
        assert item['language']=={'kind':'id','id':truth['language_id']}
        assert item['name']['name' if 'name' in truth else 'id']==truth.get('name',truth.get('name_id'))
        assert item['payload']['location']=={'offset':truth['payload_file_offset'],'bytes':truth['payload_bytes']}
        assert item['payload']['sha256']==truth['payload_sha256']
    print(label,'sha256',ind['sha256'],'size',len(raw),'resource_data_directory',ind['directory'],'directories',[(x['location']['offset'],x['named_entries'],x['id_entries']) for x in ind['directories']],'entry_count',ind['examined_entries'])
    for item in ind['resources']:
        print(' resource',item['type'],item['name'],item['language'],'entries',[v['offset'] for v in item['entry_locations']],'data_entry',item['data_entry_location']['offset'],'payload',item['payload'])
    print(' evidence_id',insp['evidence_id'],'identity_match',True)
assert json.loads((B/'fixtures/pe-r33/truth.json').read_text())['changed_offsets']==changes
assert a['resources'][0]['name']['name']=='ALPHA' and z['resources'][0]['name']['name']=='CAFÉ!'
assert a['resources'][0]['name']['location']==z['resources'][0]['name']['location']=={'offset':736,'bytes':12}
assert z['resources'][0]['name']['utf16le_hex']=='430041004600c9002100'
assert [{k:v for k,v in r.items() if k!='name'} for r in a['resources']]==[{k:v for k,v in r.items() if k!='name'} for r in z['resources']]
assert a['resources'][1]==z['resources'][1] and a['directories']==z['directories']
print('changed_offsets',changes)
print('VERDICT matched resources 2/2, extra 0, missed 0, precision 2/2=1.00, recall 2/2=1.00')
```

## Actual observed output

`python3 -c <the above Python code>` exited 0 (the code was supplied verbatim as the `-c` argument). Its stdout:

```text
r32 sha256 5169ac55c0b145b41c58b72848f694111c325d2c084266ef9d6c8763ce99adbd size 1024 resource_data_directory {'rva': 8192, 'location': {'offset': 512, 'bytes': 240}, 'data_directory_location': {'offset': 200, 'bytes': 8}} directories [(512, 0, 1), (536, 1, 1), (568, 0, 1), (592, 0, 1)] entry_count 5
 resource {'kind': 'id', 'id': 10} {'kind': 'name', 'name': 'ALPHA', 'utf16le_hex': '41004c00500048004100', 'location': {'offset': 736, 'bytes': 12}} {'kind': 'id', 'id': 1036} entries [528, 552, 584] data_entry 616 payload {'rva': 8352, 'location': {'offset': 672, 'bytes': 15}, 'sha256': '071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229'}
 resource {'kind': 'id', 'id': 10} {'kind': 'id', 'id': 3} {'kind': 'id', 'id': 1033} entries [528, 560, 608] data_entry 632 payload {'rva': 8384, 'location': {'offset': 704, 'bytes': 15}, 'sha256': 'cc29ca16da56975bf9fb034fbc010e377076ada5df6395622c8ffd9fed19f67e'}
 evidence_id ev_dcc2411a94ff88169c18f1db3d70ad0792bbccb059dec89bec0df3a578ef653d identity_match True
r33 sha256 997089c388e1e3a686f736bcd459288ea4422f86c50ec45ad1cb4ca05c876cc8 size 1024 resource_data_directory {'rva': 8192, 'location': {'offset': 512, 'bytes': 240}, 'data_directory_location': {'offset': 200, 'bytes': 8}} directories [(512, 0, 1), (536, 1, 1), (568, 0, 1), (592, 0, 1)] entry_count 5
 resource {'kind': 'id', 'id': 10} {'kind': 'name', 'name': 'CAFÉ!', 'utf16le_hex': '430041004600c9002100', 'location': {'offset': 736, 'bytes': 12}} {'kind': 'id', 'id': 1036} entries [528, 552, 584] data_entry 616 payload {'rva': 8352, 'location': {'offset': 672, 'bytes': 15}, 'sha256': '071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229'}
 resource {'kind': 'id', 'id': 10} {'kind': 'id', 'id': 3} {'kind': 'id', 'id': 1033} entries [528, 560, 608] data_entry 632 payload {'rva': 8384, 'location': {'offset': 704, 'bytes': 15}, 'sha256': 'cc29ca16da56975bf9fb034fbc010e377076ada5df6395622c8ffd9fed19f67e'}
 evidence_id ev_50a1273217e51aa8f8f1c204f759582b840dfb8a455e8758ca2f1ba413db90bc identity_match True
changed_offsets [{'offset': 738, 'before': 65, 'after': 67}, {'offset': 740, 'before': 76, 'after': 65}, {'offset': 742, 'before': 80, 'after': 70}, {'offset': 744, 'before': 72, 'after': 201}, {'offset': 746, 'before': 65, 'after': 33}]
VERDICT matched resources 2/2, extra 0, missed 0, precision 2/2=1.00, recall 2/2=1.00
```
