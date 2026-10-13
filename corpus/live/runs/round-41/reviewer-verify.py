import hashlib, json, struct
from pathlib import Path
F = Path('/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/fixtures')
L = Path('/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/live/runs/round-41')
a, b = (F/'pe-r41/fixture.exe').read_bytes(), (F/'pe-r36/fixture.exe').read_bytes()
raw_bytes = (L/'inspection.raw.json').read_bytes()
r, receipt = json.loads(raw_bytes), json.loads((L/'producer-receipt.json').read_bytes())
h = lambda x: hashlib.sha256(x).hexdigest()
u16 = lambda x, o: struct.unpack_from('<H', x, o)[0]
u32 = lambda x, o: struct.unpack_from('<I', x, o)[0]
loc = lambda o, n: {'offset':o, 'bytes':n}
expected_sha = '501584bd0fd439d8c0e904394adb575a9d94a71f151c2ff6389c4053ba36394c'
assert len(a) == len(b) == 1024 and h(a) == expected_sha
assert a[512:1024] == b[512:1024]
assert h(b) == 'a10b1289edc59df08ccc9a3b6cf1e81f803a8041fa414fc1c6375a1d017eca96'
assert a[:2] == b'MZ'
pe = u32(a, 0x3c); assert pe == 0x40 and a[pe:pe+4] == b'PE\0\0'
coff, opt = pe+4, pe+24
assert (u16(a,coff), u16(a,coff+2), u16(a,coff+16)) == (0x8664,1,240)
assert u16(a,opt) == 0x20b and u32(a,opt+108) == 16
assert opt+112+2*8 == 216  # PE32+ resource data-directory entry #2
assert (u32(a,216),u32(a,220)) == (8192,160)
sec = opt+240
assert a[sec:sec+8] == b'.rsrc\0\0\0'
assert tuple(u32(a,sec+i) for i in (8,12,16,20)) == (400,8192,512,512)
assert u32(a,sec+36) == 0x40000040
rva_to_file = lambda rva: 512+rva-8192 if 8192 <= rva < 8192+400 else None
assert rva_to_file(8192) == 512 and rva_to_file(8448) == 768 and rva_to_file(8512) == 832
assert a[512+160:768] == b'\0'*(768-672)  # no hidden table entries in padding

def directory(relative, lineage=()):
    assert relative not in lineage
    o = 512+relative
    assert 512 <= o and o+16 <= 672
    assert (u32(a,o),u32(a,o+4),u16(a,o+8),u16(a,o+10)) == (0,0,0,0)
    named, ids = u16(a,o+12),u16(a,o+14)
    assert named == 0 and o+16+8*ids <= 672
    entries = []
    for i in range(ids):
        e = o+16+8*i
        ident, target = u32(a,e),u32(a,e+4)
        assert ident < 0x80000000  # no named/string entries
        entries.append((ident,target,loc(e,8)))
    assert [x[0] for x in entries] == sorted(set(x[0] for x in entries))
    return loc(o,16+8*ids), entries

dirs, leaves, visited = [], [], set()
def walk(relative, path=(), entry_locations=()):
    assert relative not in visited
    visited.add(relative)
    d, entries = directory(relative,tuple(visited-{relative}))
    dirs.append(d)
    for ident, target, entry in entries:
        newpath = path+(ident,)
        if len(newpath)<3:
            assert target & 0x80000000
            walk(target & 0x7fffffff,newpath,entry_locations+(entry,))
        else:
            assert not (target & 0x80000000)
            off = 512+target
            assert 512 <= off and off+16 <= 672
            rva, size, codepage, reserved = struct.unpack_from('<IIII',a,off)
            payload_off = rva_to_file(rva)
            assert payload_off is not None and payload_off+size <= len(a)
            leaves.append((newpath,entry_locations+(entry,),loc(off,16),rva,loc(payload_off,size),h(a[payload_off:payload_off+size]),codepage,reserved))
walk(0)
assert sorted(visited) == [0,32,56,80,104]
assert dirs == [loc(512,32),loc(544,24),loc(592,24),loc(568,24),loc(616,24)]
assert leaves == [
    ((3,1,1033),(loc(528,8),loc(560,8),loc(608,8)),loc(640,16),8448,loc(768,48),'d7aaca7bc7951c9249a7798838189374fa953d3def03aebb375ee731768e5003',0,0),
    ((14,1,1033),(loc(536,8),loc(584,8),loc(632,8)),loc(656,16),8512,loc(832,20),'cc3745185dc1ae877dff5b3561df1162b7487fe78af6761a85649989979a3d01',0,0),
]
# RT_GROUP_ICON's 6-byte header and single 14-byte image record reference RT_ICON ID 1.
assert struct.unpack_from('<HHH',a,832) == (0,1,1)
width,height,colors,reserved,planes,bits,size,icon_id = struct.unpack_from('<BBBBHHIH',a,838)
assert (width,height,colors,reserved,planes,bits,size,icon_id) == (1,1,0,0,1,32,48,1)
assert leaves[0][0] == (3,icon_id,leaves[1][0][2]) and leaves[0][4]['bytes'] == size
n = r['normalized_result']
assert (n['format'],n['machine'],n['coverage']) == ('pe32-plus',0x8664,{'status':'complete','examined_entries':6,'resources':2})
assert n['artifact'] == {'path':str(F/'pe-r41/fixture.exe'),'sha256':h(a),'bytes':len(a)}
assert n['directory'] == {'rva':8192,'location':loc(512,160),'data_directory_location':loc(216,8)}
assert [d['location'] for d in n['directories']] == [loc(512,32),loc(544,24),loc(592,24),loc(568,24),loc(616,24)]
assert [(d['named_entries'],d['id_entries']) for d in n['directories']] == [(0,2),(0,1),(0,1),(0,1),(0,1)]
assert all(all(d[k]==0 for k in ('characteristics','timestamp','major_version','minor_version')) for d in n['directories'])
assert len(n['resources']) == 2
for i, leaf in enumerate(leaves):
    path, entries, data_loc, rva, payload_loc, digest, cp, reserved = leaf
    resource = n['resources'][i]
    assert resource == {'index':i,'type':{'kind':'id','id':path[0]},'name':{'kind':'id','id':path[1]},'language':{'kind':'id','id':path[2]},'entry_locations':list(entries),'data_entry_location':data_loc,'code_page':cp,'reserved':reserved,'payload':{'rva':rva,'location':payload_loc,'sha256':digest}}
assert n['icon_groups'] == [{'resource_index':1,'images':[{'location':loc(838,14),'width':width,'height':height,'color_count':colors,'reserved':reserved,'planes':planes,'bit_count':bits,'declared_bytes':size,'resource_id':icon_id,'candidate_resource_indices':[0],'same_language_resource_index':0,'size_matches':True}]}]
assert r['provider'] == {'id':'rea-pe-resources','name':'REA PE resource parser','version':'1'}
assert r['operation'] == 'inspect_pe_resources' and r['predicate_type'] == 'rea.analysis'
assert r['subject']['digest']['sha256'] == h(a) and r['subject']['local_path'] == str(F/'pe-r41/fixture.exe')
assert r['parameters']['path'] == str(F/'pe-r41/fixture.exe')
assert receipt == {'command':'npx -y rea-agents@6.4.0 inspect-pe-resources '+str(F/'pe-r41/fixture.exe')+' --format json','exit_code':0,'stdout_sha256':h(raw_bytes),'evidence_id':r['evidence_id'],'fixture_sha256':h(a)}
print('PASS: independent PE32+ headers, unchanged raw section, exact two resource leaves/icon relation, saved REA record and receipt consistency')
