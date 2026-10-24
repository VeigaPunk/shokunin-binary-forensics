#!/usr/bin/env python3
"""Byte-derived verifier for authored r55-r57 PE fixtures only."""
from pathlib import Path
from hashlib import sha256
from struct import unpack_from
import copy, json
ROOT=Path(__file__).resolve().parent
# Historical producer corpus; identity for saved artifact paths/receipt commands only, never read through it.
HIST=Path('/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus')
N=0
def req(ok,msg):
 global N
 N+=1
 if not ok: raise AssertionError(msg)

def receipt_ok(receipt, command, digest, eid, raw):
 return receipt['command']==command and receipt['exit_code']==0 and receipt['fixture_sha256']==digest and receipt['evidence_id']==eid and receipt['stdout_sha256']==H(raw) and isinstance(receipt['duration_seconds'],(float,int)) and receipt['duration_seconds']>=0

def H(b): return sha256(b).hexdigest()
def decode(d):
 u16=lambda o:unpack_from('<H',d,o)[0]; u32=lambda o:unpack_from('<I',d,o)[0]
 req(d[:2]==b'MZ','MZ'); pe=u32(60); req(d[pe:pe+4]==b'PE\0\0','PE')
 machine,ns=unpack_from('<HH',d,pe+4); opt=pe+24; req(u16(opt)==0x20b and u16(pe+20)>=240,'PE32+')
 st=opt+u16(pe+20); secs=[unpack_from('<8sIIIIIIHHI',d,st+40*i) for i in range(ns)]
 def fo(r,n):
  for _,vs,va,rs,ro,*_ in secs:
   if va<=r and r+n<=va+rs:
    o=ro+r-va; req(o+n<=len(d),'RVA bounds'); return o
  raise AssertionError('unmapped RVA')
 dd=opt+128; rva,size=unpack_from('<II',d,dd); start=fo(rva,size); dirs=[]; resources=[]
 def walk(rel,path,entry_path,anc):
  req(rel not in anc,'cycle'); at=start+rel; req(at+16<=start+size,'directory bounds')
  chars,ts,maj,mi,named,ids=unpack_from('<IIHHHH',d,at); count=named+ids; req(at+16+8*count<=start+size,'entries bounds')
  dirs.append(dict(location=dict(offset=at,bytes=16+8*count),characteristics=chars,timestamp=ts,major_version=maj,minor_version=mi,named_entries=named,id_entries=ids))
  for i in range(count):
   ea=at+16+8*i; ident,target=unpack_from('<II',d,ea)
   if ident&0x80000000:
    no=start+(ident&0x7fffffff); req(no+2<=start+size,'name length bounds')
    nb=2*u16(no); req(no+2+nb<=start+size,'name bytes bounds')
    raw_name=d[no+2:no+2+nb]
    key=dict(kind='name',name=raw_name.decode('utf-16le'),utf16le_hex=raw_name.hex(),location=dict(offset=no,bytes=2+nb))
   else: key=dict(kind='id',id=ident)
   route=path+[key]; entries=entry_path+[dict(offset=ea,bytes=8)]
   if target&0x80000000: walk(target&0x7fffffff,route,entries,anc|{rel}); continue
   req(len(route)==3,'leaf depth'); la=start+target; req(la+16<=start+size,'data entry bounds')
   pr,ps,cp,res=unpack_from('<IIII',d,la); po=fo(pr,ps)
   resources.append(dict(index=len(resources),type=route[0],name=route[1],language=route[2],entry_locations=entries,data_entry_location=dict(offset=la,bytes=16),code_page=cp,reserved=res,payload=dict(rva=pr,location=dict(offset=po,bytes=ps),sha256=H(d[po:po+ps]))))
 walk(0,[],[],set())
 groups=[]
 for x in resources:
  if x['type']!={'kind':'id','id':14}: continue
  off=x['payload']['location']['offset']; length=x['payload']['location']['bytes']; z,t,count=unpack_from('<HHH',d,off)
  req((z,t)==(0,1) and length==6+14*count,'group records')
  images=[]
  for i in range(count):
   at=off+6+14*i; w,h,c,res,pl,bits,decl,rid=unpack_from('<BBBBHHIH',d,at)
   cand=[q['index'] for q in resources if q['type']=={'kind':'id','id':3} and q['name']=={'kind':'id','id':rid}]
   same=next((j for j in cand if resources[j]['language']==x['language']),None)
   images.append(dict(location=dict(offset=at,bytes=14),width=w,height=h,color_count=c,reserved=res,planes=pl,bit_count=bits,declared_bytes=decl,resource_id=rid,candidate_resource_indices=cand,same_language_resource_index=same,size_matches=(resources[same]['payload']['location']['bytes']==decl) if same is not None else None))
  groups.append(dict(resource_index=x['index'],images=images))
 return dict(format='pe32-plus',machine=machine,directory=dict(rva=rva,location=dict(offset=start,bytes=size),data_directory_location=dict(offset=dd,bytes=8)),directories=dirs,resources=resources,icon_groups=groups,coverage=dict(status='complete',examined_entries=sum(x['named_entries']+x['id_entries'] for x in dirs),resources=len(resources)))
EXPECT={55:('41c0132a9ecd8274d9afcfc079fefc0c5beb14c1ae81bc7bfa0a2832e140572b','ev_db785aec4caaa20630a96a8a3b250ff3aae9c0fa454ff36abe4415725fa22e79'),56:('911f96b3c7cdf4b83ce49a75eadef9f6e77387578feab07605cc8dbcfaabe83b','ev_44be7fd71ca9e8028e71b2714bea44597bd8b25ee83922003747e03fd231342a'),57:('71d11fba01d4daa040e04e649a70c39bcdb475ce2e0a2801f6171a325db0494d','ev_068eb9b682385b760251b6d23ba70680ec57b0e55b95ce242921a3f021e1cd07')}
def compare_normalized(actual,tree,hist,digest,length,r):
 expected=dict(artifact=dict(path=str(hist),sha256=digest,bytes=length),**tree,limitations=[
  'Static PE32/PE32+ type/name/language resource inventory; payloads other than RT_GROUP_ICON remain opaque.',
  'Icon candidates are resource-table relationships. Language fallback, image decoding and actual shell/window loading are not observed.',
  'Exact shared byte ranges are retained; non-identical overlapping resource structures or payloads are rejected.'
 ])
 req(actual==expected,f'r{r} normalized result')
def check(r):
 digest,eid=EXPECT[r]; folder=ROOT/f'live/runs/round-{r}'; fixture=ROOT/f'fixtures/pe-r{r}/fixture.exe'; hist=HIST/f'fixtures/pe-r{r}/fixture.exe'; d=fixture.read_bytes(); raw=(folder/'inspection.raw.json').read_bytes(); report=json.loads(raw); receipt=json.loads((folder/'receipt.json').read_text()); tree=decode(d)
 req(len(d)==1536 and H(d)==digest,f'r{r} digest'); req(report['evidence_id']==eid and report['operation']=='inspect_pe_resources',f'r{r} Evidence ID'); req(report['subject']['digest']['sha256']==digest,f'r{r} subject')
 req(report['normalized_result']['artifact']==dict(path=str(hist),sha256=digest,bytes=len(d)),f'r{r} artifact')
 compare_normalized(report['normalized_result'],tree,hist,digest,len(d),r)
 command=f'npx -y rea-agents@6.4.0 inspect-pe-resources {hist} --format json'
 forged=copy.deepcopy(receipt)
 forged['command'] += ' --forged'
 req(not receipt_ok(forged, command, digest, eid, raw), f'r{r}: forged receipt accepted')
 req(receipt_ok(receipt, command, digest, eid, raw),f'r{r} receipt')
 req(len(tree['icon_groups'])==1 and tree['icon_groups'][0]['resource_index']==2 and len(tree['icon_groups'][0]['images'])==2,f'r{r} group shape')
 req(tree['resources'][2]['name']=={'kind':'name','name':'A😀B!','utf16le_hex':'41003dd800de42002100','location':{'offset':736,'bytes':12}},f'r{r} exact UTF-16 name')
 return d,report,tree
def main():
 rows={r:check(r) for r in EXPECT}; base=rows[55][0]
 states={55:((1,[0],0,True),(2,[1],1,True)),
         56:((1,[0],0,True),(3,[],None,None)),
         57:((1,[0],0,True),(2,[1],1,False))}
 for r,expected in states.items():
  images=rows[r][2]['icon_groups'][0]['images']
  actual=tuple((im['resource_id'],im['candidate_resource_indices'],im['same_language_resource_index'],im['size_matches']) for im in images)
  req(actual==expected,f'r{r} exact ordered image state')
 for r,expected in ((56,(928,2,3)),(57,(924,48,47))):
  other=rows[r][0]; req(len(base)==len(other),f'r{r} byte length')
  diff=[(i,a,b) for i,(a,b) in enumerate(zip(base,other)) if a!=b]; req(diff==[expected],f'r{r} one-byte delta')
 for r in (56,57):
  forged=copy.deepcopy(rows[r][1]); im=forged['normalized_result']['icon_groups'][0]['images'][1]
  if r==56: im['candidate_resource_indices']=[1]
  else: im['size_matches']=True
  req(forged['normalized_result']!=rows[r][1]['normalized_result'],f'r{r} mutation no-op')
  try:
   compare_normalized(forged['normalized_result'],rows[r][2],HIST/f'fixtures/pe-r{r}/fixture.exe',EXPECT[r][0],len(rows[r][0]),r)
  except AssertionError as error:
   req(str(error)==f'r{r} normalized result',f'r{r} unexpected rejection: {error}')
  else: raise AssertionError(f'r{r} forged claim accepted')
 print(f'PASS: {N} positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.')
if __name__=='__main__': main()
