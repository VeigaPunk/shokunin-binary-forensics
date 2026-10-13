from pathlib import Path
import hashlib, json, struct

root = Path('/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus')
fixture = root / 'fixtures/pe-r47/fixture.exe'
run = root / 'live/runs/round-47'
b = fixture.read_bytes()
stdout = (run / 'inspection.raw.json').read_bytes()
saved = json.loads(stdout)
receipt = json.loads((run / 'producer-receipt.json').read_bytes())
n = saved['normalized_result']
sha = lambda data: hashlib.sha256(data).hexdigest()
def u16(pos): return struct.unpack_from('<H', b, pos)[0]
def u32(pos): return struct.unpack_from('<I', b, pos)[0]
def loc(offset, size):
    assert 0 <= offset and 0 <= size and offset + size <= len(b)
    return {'offset': offset, 'bytes': size}

assert b[:2] == b'MZ'
pe = u32(0x3c)
assert b[pe:pe+4] == b'PE\0\0'
assert u16(pe+4) == 0x8664  # AMD64
sections_count = u16(pe+6)
opt_size = u16(pe+20)
opt = pe+24
assert u16(opt) == 0x20b  # PE32+
assert opt_size >= 128 and u32(opt+108) >= 3
resource_rva, resource_size = struct.unpack_from('<II', b, opt+112+8*2)
section_table = opt+opt_size
sections = [struct.unpack_from('<8sIIIIIIHHI', b, section_table+40*i)
            for i in range(sections_count)]
def rva_offset(rva, size):
    for name, virtual_size, va, raw_size, raw_ptr, *_ in sections:
        if va <= rva and rva+size <= va+raw_size and rva+size <= va+max(virtual_size,raw_size):
            return loc(raw_ptr+rva-va, size)['offset']
    raise AssertionError(f'unmapped RVA {rva:#x} size {size}')
resource_base = rva_offset(resource_rva, resource_size)
assert n['format'] == 'pe32-plus' and n['machine'] == u16(pe+4)
assert n['directory'] == {'rva':resource_rva, 'location':loc(resource_base,resource_size),
                          'data_directory_location':loc(opt+112+8*2,8)}
dirs, leaves = [], []
seen = set()
def walk(relative, path, entries):
    assert relative not in seen, 'resource directory cycle or duplicate'
    seen.add(relative)
    off = resource_base+relative
    assert 0 <= relative <= resource_size-16
    chars, stamp, maj, minor, named, ids = struct.unpack_from('<IIHHHH',b,off)
    count = named+ids
    assert relative+16+8*count <= resource_size
    dirs.append({'location':loc(off,16+8*count),'characteristics':chars,
                 'timestamp':stamp,'major_version':maj,'minor_version':minor,
                 'named_entries':named,'id_entries':ids})
    for i in range(count):
        at=off+16+8*i
        key,target=struct.unpack_from('<II',b,at)
        assert not key & 0x80000000, 'fixture should have numeric identifiers'
        assert i >= named
        here = path+[{'kind':'id','id':key}]
        positions = entries+[loc(at,8)]
        rel=target & 0x7fffffff
        if target & 0x80000000:
            assert len(here)<3
            walk(rel,here,positions)
        else:
            assert len(here)==3 and rel+16<=resource_size
            de=resource_base+rel
            rva,length,code,reserved=struct.unpack_from('<IIII',b,de)
            payload_at=rva_offset(rva,length)
            leaves.append({'index':len(leaves),'type':here[0],'name':here[1],
                           'language':here[2],'entry_locations':positions,
                           'data_entry_location':loc(de,16),'code_page':code,
                           'reserved':reserved,'payload':{'rva':rva,
                            'location':loc(payload_at,length),
                            'sha256':sha(b[payload_at:payload_at+length])}})
walk(0,[],[])
assert len(leaves)==3 and len(dirs)==5
assert [(r['type']['id'],r['name']['id'],r['language']['id']) for r in leaves] == [
    (3,1,1033),(3,1,1036),(14,1,1036)]
assert [r['payload']['location']['bytes'] for r in leaves] == [48,48,20]
assert [r['payload']['location']['offset'] for r in leaves] == [768,832,896]
assert leaves[0]['payload']['sha256'] != leaves[1]['payload']['sha256']
assert dirs == n['directories'] and leaves == n['resources']
assert sum(d['named_entries']+d['id_entries'] for d in dirs)==7
assert n['coverage'] == {'status':'complete','examined_entries':7,'resources':3}
group=leaves[2]
start=group['payload']['location']['offset']
assert struct.unpack_from('<HHH',b,start)==(0,1,1)
width,height,colors,pad,planes,bits,declared,image_id=struct.unpack_from('<BBBBHHIH',b,start+6)
assert (width,height,colors,pad,planes,bits,declared,image_id)==(1,1,0,0,1,32,48,1)
candidates=[leaf['index'] for leaf in leaves if leaf['type']['id']==3 and leaf['name']['id']==image_id]
same=[i for i in candidates if leaves[i]['language']==group['language']]
assert candidates==[0,1] and same==[1]
assert leaves[same[0]]['payload']['location']['bytes']==declared
assert n['icon_groups']==[{'resource_index':2,'images':[{'location':loc(start+6,14),
    'width':width,'height':height,'color_count':colors,'reserved':pad,
    'planes':planes,'bit_count':bits,'declared_bytes':declared,'resource_id':image_id,
    'candidate_resource_indices':candidates,'same_language_resource_index':same[0],
    'size_matches':True}]}]
assert n['artifact']=={'path':str(fixture),'sha256':sha(b),'bytes':len(b)}
assert saved['subject']['digest']['sha256']==sha(b)
assert saved['evidence_id']==receipt['evidence_id']
assert receipt['fixture_sha256']==sha(b)
assert receipt['exit_code']==0
assert receipt['command']==f'npx -y rea-agents@6.4.0 inspect-pe-resources {fixture} --format json'
assert saved['subject']['local_path']==str(fixture)
assert saved['parameters']['path']==str(fixture)
assert receipt['stdout_sha256']==sha(stdout)
assert saved['operation']=='inspect_pe_resources'
print('PASS: independent PE32+ resource walk, 3 leaves/7 entries/5 directories, group relation, saved output SHA-256 and internal receipt')
