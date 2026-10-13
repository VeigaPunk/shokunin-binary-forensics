from pathlib import Path
import hashlib, json, struct

base = Path('/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus')
fixture = base / 'fixtures/pe-r42/fixture.exe'
run = base / 'live/runs/round-42'
b = fixture.read_bytes()
raw = json.loads((run / 'inspection.raw.json').read_text())
receipt = json.loads((run / 'producer-receipt.json').read_text())
r = raw['normalized_result']
def h(data): return hashlib.sha256(data).hexdigest()
def U16(o): return struct.unpack_from('<H', b, o)[0]
def U32(o): return struct.unpack_from('<I', b, o)[0]
def loc(o,n): return {'offset':o,'bytes':n}
def ident(n): return {'kind':'id','id':n}
assert b[:2] == b'MZ' and len(b) == 1536
pe = U32(0x3c)
assert pe == 0x40 and b[pe:pe+4] == b'PE\0\0'
co = pe+4; opt = co+20
assert U16(co) == 0x8664 and U16(co+2) == 1 and U16(co+16) == 240
assert U16(opt) == 0x20b and U32(opt+108) == 16
sh = opt+240
assert b[sh:sh+8] == b'.rsrc\0\0\0'
virtual_size, section_rva, raw_size, raw_start = struct.unpack_from('<IIII',b,sh+8)
assert (virtual_size,section_rva,raw_size,raw_start) == (1024,8192,1024,512)
assert raw_start+raw_size <= len(b)
dd = opt+112+8*2
root_rva, dir_size = struct.unpack_from('<II',b,dd)
assert (root_rva,dir_size) == (8192,208)
def mapped(rva,n):
    assert section_rva <= rva and rva+n <= section_rva+min(virtual_size,raw_size)
    off = raw_start+rva-section_rva
    assert off+n <= len(b)
    return off
root = mapped(root_rva,dir_size)
assert (root,root+dir_size) == (512,720)
assert r['format'] == 'pe32-plus' and r['machine'] == U16(co)
assert r['directory'] == {'rva':root_rva,'location':loc(root,dir_size),'data_directory_location':loc(dd,8)}
assert r['artifact'] == {'path':str(fixture),'sha256':h(b),'bytes':len(b)}
assert raw['subject']['digest']['sha256'] == h(b)
assert receipt['fixture_sha256'] == h(b)
assert receipt['evidence_id'] == raw['evidence_id']
assert receipt['exit_code'] == 0
assert receipt['command'] == f'npx -y rea-agents@6.4.0 inspect-pe-resources {fixture} --format json'
assert len(receipt['stdout_sha256']) == 64 # saved stdout unavailable: digest not independently checked

dirs=[]; leaves=[]; entries=[]; visited=set()
def in_tree(o,n):
    assert root <= o and o+n <= root+dir_size
    return o
def walk(rel,path,trail):
    o = in_tree(root+rel,16)
    assert o not in trail and o not in visited
    visited.add(o)
    characteristics,timestamp,maj,minr,n_named,n_id = struct.unpack_from('<IIHHHH',b,o)
    count=n_named+n_id
    in_tree(o,16+8*count)
    d={'location':loc(o,16+8*count),'characteristics':characteristics,
       'timestamp':timestamp,'major_version':maj,'minor_version':minr,
       'named_entries':n_named,'id_entries':n_id}
    dirs.append(d)
    for i in range(count):
        e=o+16+8*i
        name,target=struct.unpack_from('<II',b,e)
        assert i >= n_named and name < 0x80000000 # all expected entries are numeric IDs
        entries.append((e,name,target))
        node=(name,)
        edge_paths[path+node] = edge_paths[path] + [e]
        if target & 0x80000000:
            walk(target & 0x7fffffff,path+node,trail|{o})
        else:
            de=in_tree(root+target,16)
            assert len(path)==2
            payload_rva,size,codepage,reserved=struct.unpack_from('<IIII',b,de)
            payload=mapped(payload_rva,size)
            leaves.append({'index':len(leaves),'type':ident(path[0]),'name':ident(path[1]),
              'language':ident(name),'entry_locations':[loc(x,8) for x in path_entries(path+node)],
              'data_entry_location':loc(de,16),'code_page':codepage,'reserved':reserved,
              'payload':{'rva':payload_rva,'location':loc(payload,size),'sha256':h(b[payload:payload+size])}})
# Entry offsets are reconstructed from the traversed edges.
edge_paths={():[]}
def path_entries(path): return edge_paths[path]
walk(0,(),set())
assert len(dirs)==6 and len(entries)==8 and len(leaves)==3
assert sorted(dirs,key=lambda d:d['location']['offset']) == sorted(r['directories'],key=lambda d:d['location']['offset'])
expected=[
 (3,1,1033,[528,560,616],672,8448,768,48,'d7aaca7bc7951c9249a7798838189374fa953d3def03aebb375ee731768e5003'),
 (3,2,1033,[528,568,640],688,8512,832,48,'2f503cace29956c75acd5356de2f8fa98485b01edd654daf0f81a739b44c82ae'),
 (14,1,1033,[536,592,664],704,8576,896,34,'45eb70319667352d8bfea3249f7fb30166c6835d2cf564b5ec303bf2d716c17a')]
for leaf, (typ,name,lang,edge,deo,prva,po,n,digest) in zip(leaves,expected):
    assert (leaf['type'],leaf['name'],leaf['language']) == (ident(typ),ident(name),ident(lang))
    assert leaf['entry_locations'] == [loc(o,8) for o in edge]
    assert leaf['data_entry_location'] == loc(deo,16)
    assert leaf['payload'] == {'rva':prva,'location':loc(po,n),'sha256':digest}
    assert (leaf['code_page'],leaf['reserved']) == (0,0)
assert leaves == r['resources']
assert r['coverage'] == {'status':'complete','examined_entries':8,'resources':3}
group = leaves[2]; go=group['payload']['location']['offset']; gn=group['payload']['location']['bytes']
assert (U16(go),U16(go+2),U16(go+4)) == (0,1,2)
assert gn == 6+2*14
images=[]
for i,(id_expected,candidate_expected,width_expected) in enumerate(((1,0,1),(2,1,2))):
    pos=go+6+14*i
    width,height,colors,reserved,planes,bits,declared,rid=struct.unpack_from('<BBBBHHIH',b,pos)
    assert (width,height,colors,reserved,planes,bits,declared,rid)==(width_expected,width_expected,0,0,1,32,48,id_expected)
    candidates=[x['index'] for x in leaves if x['type']==ident(3) and x['name']==ident(rid)]
    same=[idx for idx in candidates if leaves[idx]['language']==group['language']]
    assert candidates == [candidate_expected] and same == [candidate_expected]
    assert declared == leaves[candidate_expected]['payload']['location']['bytes']
    images.append({'location':loc(pos,14),'width':width,'height':height,'color_count':colors,
      'reserved':reserved,'planes':planes,'bit_count':bits,'declared_bytes':declared,'resource_id':rid,
      'candidate_resource_indices':candidates,'same_language_resource_index':same[0], 'size_matches':True})
assert r['icon_groups']==[{'resource_index':2,'images':images}]
print('PASS: PE32+ headers, section/RVA mapping, 6 directories, 8 entries, 3 exact leaves, ordered icon references and 48-byte equality match saved REA.')
