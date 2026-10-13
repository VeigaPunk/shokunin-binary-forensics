from pathlib import Path
import hashlib, json, struct
base = Path('.shokunin/revenger/corpus')
run = base/'live/runs/round-35'
record = json.loads((run/'inspection.json').read_text())['normalized_result']
def sha(raw): return hashlib.sha256(raw).hexdigest()
def parse(path):
    b = path.read_bytes()
    def u16(o): return struct.unpack_from('<H', b, o)[0]
    def u32(o): return struct.unpack_from('<I', b, o)[0]
    def loc(o,n):
        assert 0 <= o <= len(b) and 0 <= n <= len(b)-o, (o,n)
        return {'offset':o,'bytes':n}
    assert b[:2] == b'MZ'
    pe = u32(60); assert b[pe:pe+4] == b'PE\0\0'
    machine, count, optsize = u16(pe+4), u16(pe+6), u16(pe+20)
    opt = pe+24; magic = u16(opt)
    assert magic in (0x10b,0x20b)
    nrva = u32(opt+(92 if magic == 0x10b else 108))
    assert nrva >= 3 and (96 if magic == 0x10b else 112)+nrva*8 <= optsize
    dd = opt+(96 if magic == 0x10b else 112)+2*8
    rva, size = u32(dd),u32(dd+4)
    sections=[]
    for i in range(count):
        s=opt+optsize+i*40; loc(s,40)
        virtual_size, virtual_addr, raw_size, raw_ptr = [u32(s+j) for j in (8,12,16,20)]
        sections.append((virtual_addr, virtual_size, raw_size, raw_ptr))
    def fileoff(r,n):
        candidates=[raw_ptr+r-addr for addr,vs,rs,raw_ptr in sections if addr<=r and r+n<=addr+rs and r+n<=addr+max(vs,rs)]
        assert len(candidates)==1, (r,n,candidates)
        loc(candidates[0],n)
        return candidates[0]
    root=fileoff(rva,size)
    directories=[]; resources=[]; seen=set(); edge_count=0
    def identity(word):
        if not word & 0x80000000: return {'kind':'id','id':word}
        o=root+(word&0x7fffffff); length=u16(o); n=length*2
        raw=b[o+2:o+2+n]; loc(o,2+n)
        return {'kind':'name','name':raw.decode('utf-16-le'), 'utf16le_hex':raw.hex(),'location':loc(o,2+n)}
    def walk(rel, labels, edges, depth):
        nonlocal edge_count
        assert depth < 3 and rel not in seen
        seen.add(rel)
        d=root+rel; loc(d,16)
        a,btime,major,minor,named,ids=struct.unpack_from('<IIHHHH',b,d)
        n=named+ids; loc(d,16+8*n)
        directories.append({'location':loc(d,16+8*n),'characteristics':a,'timestamp':btime,'major_version':major,'minor_version':minor,'named_entries':named,'id_entries':ids})
        for i in range(n):
            e=d+16+8*i; word,target=u32(e),u32(e+4)
            assert bool(word & 0x80000000)==(i<named), (e,named,ids)
            edge_count+=1
            labels2=labels+[identity(word)]; edges2=edges+[loc(e,8)]
            if depth<2:
                assert target & 0x80000000, e
                walk(target&0x7fffffff,labels2,edges2,depth+1)
            else:
                assert not target & 0x80000000
                data=root+target; loc(data,16)
                prva,nbytes,cp,res=struct.unpack_from('<IIII',b,data)
                po=fileoff(prva,nbytes)
                resources.append({'index':len(resources),'type':labels2[0], 'name':labels2[1], 'language':labels2[2], 'entry_locations':edges2,'data_entry_location':loc(data,16), 'code_page':cp,'reserved':res,'payload':{'rva':prva,'location':loc(po,nbytes),'sha256':sha(b[po:po+nbytes])}})
    walk(0,[],[],0)
    return {'artifact':{'path':str(path.resolve()),'sha256':sha(b),'bytes':len(b)},'format':'pe32' if magic==0x10b else 'pe32+', 'machine':machine,'directory':{'rva':rva,'location':loc(root,size),'data_directory_location':loc(dd,8)},'directories':directories,'resources':resources,'icon_groups':[] if all(r['type'] != {'kind':'id','id':14} for r in resources) else 'NOT_EVALUATED','coverage':{'status':'complete','examined_entries':edge_count,'resources':len(resources)}}
current=parse(base/'fixtures/pe-r35/fixture.exe')
for key, expected in current.items():
    assert record[key]==expected, (key, record[key], expected)
assert set(record)==set(current)|{'limitations'}, set(record)^set(current)
old=parse(base/'fixtures/pe-r34/fixture.exe')
print('PASS every independently derived normalized_result field except prose limitations')
print('round-34/35 edges, resources:',old['coverage'],current['coverage'])
print('round-34/35 directory range:',old['directory'],current['directory'])
print('round-34/35 resource identities:',[(r['name'],r['language']) for r in old['resources']],[(r['name'],r['language']) for r in current['resources']])
