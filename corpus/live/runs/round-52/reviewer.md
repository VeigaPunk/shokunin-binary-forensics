# Round 52 independent byte review

**Verdict: pass, bounded to static PE bytes and saved evidence consistency.** The read-only verifier below independently walks all five reachable resource directories and six entries (two leaves); no additional reachable entries occur. It checks the PE32+ header and `.rsrc` mapping, resource data-directory length 240 (baseline 160), RT_GROUP_ICON name counts 1/0, the length-prefixed `A😀B!` UTF-16LE wire at offset 736 (12 bytes including length), ID 1 RT_ICON payload and group language 1033, the first/only group image link to candidate resource index 0, same-language index 0, and 48-byte declared/actual size. Both payloads retain the baseline bytes at offsets 768–815 and 832–851, with independently computed hashes. The bad fixture differs only at count fields 580/582: it says zero named/one ID while its first entry still has the name high bit set; this independently accounts for count refusal.

Assumptions: PE resource RVA is section-relative within the single `.rsrc` section; `RT_ICON=3`, `RT_GROUP_ICON=14`; UTF-16LE decoding follows Python's strict decoder; candidate indexing follows resource traversal order. Receipt verification establishes only internal consistency of the saved command, stdout hash, fixture hash, evidence ID, and exit status; it cannot authenticate an actual REA invocation, its stdout provenance, or external runtime behavior. The saved `attempt-count.json` refusal matches the malformed byte pattern, but the refusal's producer is not independently verified. This does not decode the icon image or test shell/window rendering or fallback language rules.

Run from any working directory (read-only):

```bash
python - <<'PY'
from pathlib import Path
import hashlib, json, struct
root = Path('/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus')
new = (root/'fixtures/pe-r52/fixture.exe').read_bytes()
old = (root/'fixtures/pe-r41/fixture.exe').read_bytes()
run = root/'live/runs/round-52'
bad = (run/'attempt-count.exe').read_bytes()
raw_bytes = (run/'inspection.raw.json').read_bytes()
raw = json.loads(raw_bytes)
receipt = json.loads((run/'producer-receipt.json').read_bytes())
refusal = json.loads((run/'attempt-count.json').read_bytes())
u16 = lambda data, off: struct.unpack_from('<H', data, off)[0]
u32 = lambda data, off: struct.unpack_from('<I', data, off)[0]
sha = lambda data: hashlib.sha256(data).hexdigest()
assert len(new) == len(old) == len(bad) == 1024
assert sha(new) == '9297adec215ef401538dad04f06e249a41d3747e14b996a837164a2dde3d070d'
assert sha(old) == '501584bd0fd439d8c0e904394adb575a9d94a71f151c2ff6389c4053ba36394c'
assert {i for i in range(1024) if new[i] != old[i]} == {220,580,582,584,587,736,738,740,741,743,744,746}
assert {i for i in range(1024) if bad[i] != new[i]} == {580,582}

def pe(data):
    assert data[:2] == b'MZ'
    hdr = u32(data, 60)
    assert data[hdr:hdr+4] == b'PE\0\0'
    assert u16(data,hdr+4) == 0x8664 and u16(data,hdr+6) == 1
    opt = hdr+24
    assert u16(data,opt) == 0x20b and u16(data,hdr+20) == 240
    dd = opt+112+2*8  # IMAGE_DIRECTORY_ENTRY_RESOURCE
    rva, length = struct.unpack_from('<II',data,dd)
    sec = opt+u16(data,hdr+20)
    name,vsize,vrva,rsize,rptr = struct.unpack_from('<8sIIII',data,sec)
    assert name.rstrip(b'\0') == b'.rsrc' and rva == vrva == 8192
    assert rsize == 512 and rptr == 512 and vsize == 400
    assert rptr + rsize <= len(data)
    def off(r):
        assert vrva <= r < vrva + min(vsize,rsize)
        return rptr+r-vrva
    assert off(rva) == 512
    return dd,rptr,length,off

dd,base,length,rva_off = pe(new)
_,old_base,old_length,_ = pe(old)
assert (dd,base,length,old_base,old_length) == (216,512,240,512,160)

def walk(data, base):
    dirs, leaves, seen = [], [], set()
    def visit(relative, path, locations):
        pos = base+relative
        assert pos not in seen and base <= pos and pos+16 <= base+length
        seen.add(pos)
        named, ids = struct.unpack_from('<HH',data,pos+12)
        assert pos+16+8*(named+ids) <= base+length
        dirs.append((pos,named,ids,16+8*(named+ids)))
        for i in range(named+ids):
            entry = pos+16+8*i
            identity, target = struct.unpack_from('<II',data,entry)
            if i < named:
                assert identity & 0x80000000
            else:
                assert not identity & 0x80000000
            if identity & 0x80000000:
                name_pos=base+(identity & 0x7fffffff)
                chars=u16(data,name_pos)
                wire=data[name_pos+2:name_pos+2+2*chars]
                assert len(wire)==2*chars and name_pos+2+2*chars <= base+length
                ident=('name',wire.decode('utf-16le'),name_pos,2+2*chars,wire.hex())
            else:
                ident=('id',identity)
            if target & 0x80000000:
                visit(target & 0x7fffffff,path+(ident,),locations+(entry,))
            else:
                leaf=base+target
                assert base <= leaf and leaf+16 <= base+length
                payload_rva,size,cp,res=struct.unpack_from('<IIII',data,leaf)
                payload=rva_off(payload_rva)
                assert payload+size <= len(data)
                leaves.append((path+(ident,),locations+(entry,),leaf,payload,size,cp,res,sha(data[payload:payload+size])))
    visit(0,(),())
    return dirs,leaves

dirs,leaves=walk(new,base)
assert dirs == [(512,0,2,32),(544,0,1,24),(592,0,1,24),(568,1,0,24),(616,0,1,24)]
assert len(leaves)==2 and sum(n+i for _,n,i,_ in dirs)==6
assert [tuple(x[:2] for x in leaf[0]) for leaf in leaves] == [(("id",3),("id",1),("id",1033)),(("id",14),("name","A😀B!"),("id",1033))]
icon,group=leaves
assert icon[1:7] == ((528,560,608),640,768,48,0,0)
assert group[1:7] == ((536,584,632),656,832,20,0,0)
assert group[0][1] == ('name','A😀B!',736,12,'41003dd800de42002100')
assert new[736:748] == bytes.fromhex('050041003dd800de42002100')
assert icon[7] == 'd7aaca7bc7951c9249a7798838189374fa953d3def03aebb375ee731768e5003'
assert group[7] == 'cc3745185dc1ae877dff5b3561df1162b7487fe78af6761a85649989979a3d01'
assert old[768:816] == new[768:816] and old[832:852] == new[832:852]
g=struct.unpack_from('<HHH',new,832)
entry=struct.unpack_from('<BBBBHHIH',new,838)
assert g == (0,1,1) and entry == (1,1,0,0,1,32,48,1)
assert entry[-1] == icon[0][1][1] and group[0][2][1] == icon[0][2][1] == 1033
assert entry[-2] == icon[4]  # RT_GROUP_ICON candidate[0], same language, size
assert raw['normalized_result']['directory'] == {'rva':8192,'location':{'offset':512,'bytes':240},'data_directory_location':{'offset':216,'bytes':8}}
n=raw['normalized_result']
assert [(d['location']['offset'],d['named_entries'],d['id_entries'],d['location']['bytes']) for d in n['directories']] == dirs
assert len(n['resources'])==2 and n['coverage']=={'status':'complete','examined_entries':6,'resources':2}
for i, leaf in enumerate(leaves):
    row=n['resources'][i]
    assert row['index']==i and row['entry_locations']==[{'offset':x,'bytes':8} for x in leaf[1]]
    assert row['data_entry_location']=={'offset':leaf[2],'bytes':16}
    assert row['payload']=={'rva':8192+leaf[3]-512,'location':{'offset':leaf[3],'bytes':leaf[4]},'sha256':leaf[7]}
    assert row['code_page']==leaf[5] and row['reserved']==leaf[6]
assert n['resources'][0]['type']=={'kind':'id','id':3}
assert n['resources'][0]['name']=={'kind':'id','id':1}
assert n['resources'][1]['type']=={'kind':'id','id':14}
assert n['resources'][1]['name']=={'kind':'name','name':'A😀B!','utf16le_hex':'41003dd800de42002100','location':{'offset':736,'bytes':12}}
assert all(r['language']=={'kind':'id','id':1033} for r in n['resources'])
assert n['icon_groups']==[{'resource_index':1,'images':[{'location':{'offset':838,'bytes':14},'width':1,'height':1,'color_count':0,'reserved':0,'planes':1,'bit_count':32,'declared_bytes':48,'resource_id':1,'candidate_resource_indices':[0],'same_language_resource_index':0,'size_matches':True}]}]
assert n['artifact']['sha256']==raw['subject']['digest']['sha256']==sha(new)
assert receipt['fixture_sha256']==sha(new) and receipt['stdout_sha256']==sha(raw_bytes)
assert receipt['evidence_id']==raw['evidence_id'] and receipt['exit_code']==0
assert receipt['command'].endswith(str(root/'fixtures/pe-r52/fixture.exe')+' --format json')
assert refusal['code']=='invalid_request' and refusal['category']=='invalid_input'
assert refusal['details']['operation']=='inspect_pe_resources'
assert refusal['details']['issues'][0]['reason']=='invalid_format'
assert 'counts disagree' in refusal['details']['issues'][0]['message']
assert u16(bad,580)==0 and u16(bad,582)==1
assert u32(bad,584)&0x80000000  # named count is zero but entry is named
print('PASS: independent PE walk, two preserved payloads, group link, bad count; saved JSON/receipt internally consistent')
PY
```
