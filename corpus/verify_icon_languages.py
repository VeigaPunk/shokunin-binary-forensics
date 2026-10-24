"""Verify three authored PE32+ group-language states against saved REA records."""
from pathlib import Path
from hashlib import sha256
from struct import unpack_from
import copy
import json

root = Path(__file__).resolve().parent
# Historical producer corpus; identity for saved artifact paths/receipt commands only, never read through it.
HIST=Path('/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus')
def H(data): return sha256(data).hexdigest()
def require(ok, why):
    if not ok: raise AssertionError(why)
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


EXPECTED = {
  47: ('cc02c78b44883f2217b7a8f82fa6fafc990ae6d0ca71f0eab8a3fbc4f2ba44ba',
       'ev_8ed889836291b900a28c7e3816167392cc5042301e069cb2a647b6a98e8d4421',
       None, 1036, 1),
  48: ('dc6483a985f12dbc0da4122db64565ed76c14a5e76ea8758658b4a54c35bc129',
       'ev_6fbaf25df632a32d7264905eeb0e2ecc64adcdd23e5ddf08e377145e68150f4b',
       (664,12,17), 1041, None),
  49: ('d26b165ee497da494e1b5605a72877597030de53f94eba674c905bffbb079114',
       'ev_01789c2e316115394bcd7e13f90471766eeac4f108e9ff939390995f952a2ec0',
       (664,12,9), 1033, 0),
}

def receipt_ok(receipt,command,expected_hash,evidence_id,raw_bytes):
    return (receipt['command']==command and receipt['exit_code']==0 and receipt['fixture_sha256']==expected_hash and
            receipt['evidence_id']==evidence_id and receipt['stdout_sha256']==H(raw_bytes))

def check(r):
    expected_hash,eid,_,group_language,selected=EXPECTED[r]
    fixture=root/f'fixtures/pe-r{r}/fixture.exe'
    hist=HIST/f'fixtures/pe-r{r}/fixture.exe'
    data=fixture.read_bytes()
    decoded=decode(data)
    raw_bytes=(root/f'live/runs/round-{r}/inspection.raw.json').read_bytes()
    record=json.loads(raw_bytes)
    receipt=json.loads((root/f'live/runs/round-{r}/producer-receipt.json').read_text())
    require(len(data)==1536 and H(data)==expected_hash,f'r{r}: file identity')
    require(record['evidence_id']==eid and record['operation']=='inspect_pe_resources',f'r{r}: evidence')
    require(record['subject']['digest']['sha256']==expected_hash,f'r{r}: subject')
    require(record['normalized_result']['artifact']==dict(path=str(hist),sha256=expected_hash,bytes=1536),f'r{r}: artifact')
    for field,val in decoded.items():
        require(record['normalized_result'][field]==val,f'r{r}: {field}')
    resources=decoded['resources']
    require(decoded['coverage']==dict(status='complete',examined_entries=7,resources=3),f'r{r}: coverage')
    require(len(resources)==3 and [(x['type']['id'],x['name']['id'],x['language']['id']) for x in resources]
            == [(3,1,1033),(3,1,1036),(14,1,group_language)],f'r{r}: resource identities')
    require(resources[0]['payload']['sha256']!=resources[1]['payload']['sha256'],f'r{r}: distinct payloads')
    images=decoded['icon_groups']
    require(len(images)==1 and images[0]['resource_index']==2 and len(images[0]['images'])==1,f'r{r}: group shape')
    image=images[0]['images'][0]
    require(image['resource_id']==1 and image['declared_bytes']==48 and image['candidate_resource_indices']==[0,1],f'r{r}: candidates')
    require(image['same_language_resource_index']==selected and image['size_matches']==(True if selected is not None else None),f'r{r}: selection')
    command=f'npx -y rea-agents@6.4.0 inspect-pe-resources {hist} --format json'
    require(receipt_ok(receipt,command,expected_hash,eid,raw_bytes),f'r{r}: receipt')
    forged=copy.deepcopy(receipt)
    forged['command']+=' --forged'
    require(not receipt_ok(forged,command,expected_hash,eid,raw_bytes),f'r{r}: forged receipt command accepted')
    forged_stdout=copy.deepcopy(receipt)
    forged_stdout['stdout_sha256']=H(b'')
    require(not receipt_ok(forged_stdout,command,expected_hash,eid,raw_bytes),f'r{r}: forged receipt stdout accepted')
    return data,record,decoded

def main():
    rows={r:check(r) for r in EXPECTED}
    baseline=rows[47][0]
    for r in (48,49):
        changed=[(i,x,y) for i,(x,y) in enumerate(zip(baseline,rows[r][0])) if x!=y]
        require(changed==[EXPECTED[r][2]],f'r{r}: exact delta')
        require(rows[r][2]['resources'][:2]==rows[47][2]['resources'][:2],f'r{r}: intact icons')
    require({rows[r][2]['icon_groups'][0]['images'][0]['same_language_resource_index'] for r in EXPECTED}=={0,1,None},'three distinct selections')
    forged=copy.deepcopy(rows[48][1])
    forged['normalized_result']['icon_groups'][0]['images'][0]['same_language_resource_index']=0
    try:
        require(forged['normalized_result']['icon_groups']==rows[48][2]['icon_groups'],'forged selection')
    except AssertionError:
        print('PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED')
    else:
        raise AssertionError('forged selection accepted')

if __name__=='__main__':
    main()
