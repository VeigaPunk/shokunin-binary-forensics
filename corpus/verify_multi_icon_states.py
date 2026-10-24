"""Read-only PE32+ multi-image icon-link comparison on four authored fixtures."""
from pathlib import Path
from hashlib import sha256
from struct import unpack_from
import copy
import json

root = Path(__file__).resolve().parent
# Historical producer corpus; identity for saved artifact paths/receipt commands only, never read through it.
HIST = Path('/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus')
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
    42: ('3ab5008b436eb4facd3966767a507fa4b1625160532585a09a6af2f752b38941',
         'ev_6e055332b6fc4cb1a047db769eb5896c73aff9d1ce1bad18105e6559b152dc3d',
         None, ((1,48,(0,),0,True),(2,48,(1,),1,True))),
    43: ('146bdde3ec3ce9f23b75b31f7a9d2fc0cbc8826f2a5d239a83fd82694f4c31a2',
         'ev_c9f9127a4617806bc1d133354dc7a70de0089d6c67ec4b895ae4903fbfbff60f',
         (928,2,3), ((1,48,(0,),0,True),(3,48,(),None,None))),
    44: ('bb2680c1ceaa3ce6e4921e078e2548f06f164d9598da2bff6c895890b73bc5fb',
         'ev_7915751e9f33b07a866efadfa65263e967a3d00f186e094ed1532c6d34007dd2',
         (924,48,47), ((1,48,(0,),0,True),(2,47,(1,),1,False))),
    45: ('1d526ab14ba29a133cafd720395920b0067d8d00c40a5e1216e097272c176669',
         'ev_4949e51a450f63160d8e81c8b3bde0957479419a5594bc30a91571579cc1f3c4',
         (640,9,12), ((1,48,(0,),0,True),(2,48,(1,),None,None))),
}

def receipt_ok(receipt,command,expected_hash,evidence_id,raw_bytes):
    return (receipt['command']==command and receipt['exit_code']==0 and receipt['fixture_sha256']==expected_hash and
            receipt['evidence_id']==evidence_id and receipt['stdout_sha256']==H(raw_bytes))

def check(round_id):
    expected_hash, evidence_id, _, expected_state = EXPECTED[round_id]
    fixture = root / f'fixtures/pe-r{round_id}/fixture.exe'
    hist = HIST / f'fixtures/pe-r{round_id}/fixture.exe'
    raw_bytes = (root / f'live/runs/round-{round_id}/inspection.raw.json').read_bytes()
    report = json.loads(raw_bytes)
    receipt = json.loads((root / f'live/runs/round-{round_id}/producer-receipt.json').read_text())
    data = fixture.read_bytes()
    decoded = decode(data)
    require(len(data)==1536 and H(data)==expected_hash, f'r{round_id}: fixture digest')
    require(report['evidence_id']==evidence_id and report['operation']=='inspect_pe_resources', f'r{round_id}: Evidence identity')
    require(report['subject']['digest']['sha256']==expected_hash, f'r{round_id}: subject digest')
    require(report['normalized_result']['artifact']==dict(path=str(hist),sha256=expected_hash,bytes=len(data)), f'r{round_id}: artifact')
    for key, expected in decoded.items():
        require(report['normalized_result'][key]==expected, f'r{round_id}: {key}')
    require(decoded['coverage']==dict(status='complete',examined_entries=8,resources=3), f'r{round_id}: coverage')
    groups=decoded['icon_groups']
    require(len(groups)==1 and groups[0]['resource_index']==2 and len(groups[0]['images'])==2, f'r{round_id}: group shape')
    state=tuple((im['resource_id'],im['declared_bytes'],tuple(im['candidate_resource_indices']),
                 im['same_language_resource_index'],im['size_matches']) for im in groups[0]['images'])
    require(state==expected_state, f'r{round_id}: state')
    command = f'npx -y rea-agents@6.4.0 inspect-pe-resources {hist} --format json'
    require(receipt_ok(receipt, command, expected_hash, evidence_id, raw_bytes), f'r{round_id}: receipt')
    forged = copy.deepcopy(receipt)
    forged['command'] += ' --forged'
    require(not receipt_ok(forged, command, expected_hash, evidence_id, raw_bytes), f'r{round_id}: forged receipt command accepted')
    forged_stdout = copy.deepcopy(receipt)
    forged_stdout['stdout_sha256'] = H(b'')
    require(not receipt_ok(forged_stdout, command, expected_hash, evidence_id, raw_bytes), f'r{round_id}: forged receipt stdout accepted')
    return data, report, decoded, state

def main():
    rows={r:check(r) for r in EXPECTED}
    baseline=rows[42][0]
    for r in (43,44,45):
        data=rows[r][0]
        require([(i,x,y) for i,(x,y) in enumerate(zip(baseline,data)) if x!=y]==[EXPECTED[r][2]], f'r{r}: byte delta')
        require(rows[r][2]['icon_groups'][0]['images'][0]==rows[42][2]['icon_groups'][0]['images'][0], f'r{r}: first image')
    require(len({rows[r][3] for r in EXPECTED})==4, 'distinct states')
    forged=copy.deepcopy(rows[45][1])
    forged['normalized_result']['icon_groups'][0]['images'][1]['same_language_resource_index']=1
    expected=rows[45][2]['icon_groups']
    try:
        require(forged['normalized_result']['icon_groups']==expected,'forged selective match')
    except AssertionError:
        print('PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED')
    else:
        raise AssertionError('forged second match accepted')

if __name__=='__main__':
    main()
