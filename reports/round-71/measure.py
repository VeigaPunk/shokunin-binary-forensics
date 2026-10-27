#!/usr/bin/env python3
"""Round-71 frozen counter. Usage: measure.py TREE (git archive corpus snapshot).
Reads TREE, lane git objects and committed round-71 vote JSON under the lane's `.ufo/`;
scratch is rooted under HYAKU_SCRATCH. Exit 0 = prior holds green, 1 = named hold red,
2 = could not evaluate.
"""
import hashlib, json, os, re, shutil, subprocess, sys, tempfile, traceback
from pathlib import Path
LANE=Path('/home/vgpnk/Projects/shokunin/revenger-shokunin')
V6='knowledge/round-71-apk-axml-byte-evidence.md'
R68_SHA='ef7f0232edb74baecc2754e6671f00914ec02e077606fcb7f21880de0830798e'
R65_SHA='cf42cc2059e454027685a59a2a35a190f6ba981f95645f41e407c47c01c4d05a'
S046_SHA='bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249'
PIN_MARKER='pinned historical script digest mismatch'
TIMEOUT=120

def run(tree, script, *args, cwd=None, timeout=300):
    p=subprocess.run([sys.executable,'-B',str(Path(tree)/'corpus'/script),*args],cwd=str(cwd or tree),capture_output=True,text=True,timeout=timeout)
    return p.returncode,p.stdout,p.stderr

def last_line(s):
    a=[x for x in s.strip().splitlines() if x.strip()]; return a[-1] if a else ''
def read(p): return Path(p).read_text(encoding='utf-8',errors='ignore')
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def rows(tree): return [x for x in read(tree/'corpus/README.md').splitlines() if re.match(r'^\| C[0-9]+ ',x)]
def backed(rows_,tree):
    out=[]
    for row in rows_:
        if not re.search(r'\| held \|$',row): continue
        paths=re.findall(r'knowledge/[\w.-]+\.md',row.split('|')[3])
        if paths and all((tree/'corpus'/x).is_file() for x in paths): out.append(row)
    return out

def emb(tree,rel):
    rc,out,err=run(tree,'check_embedded_outputs.py','--entry',str(tree/'corpus'/rel),cwd=tree)
    m=re.search(r'checked_blocks=(\d+) problems=(\d+)',out)
    return rc,(int(m.group(1)),int(m.group(2))) if m else (None,None),out,err

def gate_cli(tree,*args,timeout=150):
    return subprocess.run([sys.executable,'-B',str(tree/'corpus/check_embedded_outputs.py'),*args],cwd=tree,capture_output=True,text=True,timeout=timeout)

EXPECTED_VOTES={
    'R71W2Q01Q04':('Q01','Q02','Q03','Q04'),
    'R71W2Q05Q08':('Q05','Q06','Q07','Q08'),
    'R71W2Q09Q12':('Q09','Q10','Q11','Q12'),
    'R71W2Q13Q16':('Q13','Q14','Q15','Q16'),
}

def q_votes():
    root=LANE/'.ufo/waves/round-71/w2-votes'; seen={}
    if not root.is_dir(): return 0
    for path in root.glob('*.json'):
        try: data=json.loads(path.read_text(encoding='utf-8'))
        except (OSError,ValueError,UnicodeError): return 0
        seat=data.get('seat'); expected=EXPECTED_VOTES.get(seat)
        decisions=data.get('decisions')
        if expected is None or path.stem!=seat or not isinstance(decisions,dict) or set(decisions)!=set(expected): return 0
        for q in expected:
            value=decisions[q]
            if value not in ('PASS','n/a') or q in seen: return 0
            seen[q]=value
    return len(seen) if set(seen)=={f'Q{i:02d}' for i in range(1,17)} else 0


def main(tree):
    scratch=Path(os.environ.get('HYAKU_SCRATCH','/fast/scratch/hyaku'))/'revenger-r71'/'counter'
    scratch.mkdir(parents=True,exist_ok=True)
    try: return body(tree,scratch)
    finally: shutil.rmtree(scratch,ignore_errors=True)

def body(tree,scratch):
    rr=rows(tree); br=backed(rr,tree); strict=[x for x in br if not re.search(r'admission-status: rejected',read(tree/'corpus'/re.findall(r'knowledge/[\w.-]+\.md',x.split('|')[3])[0]))]
    c05=next((x for x in rr if x.startswith('| C05 ')),''); status=c05.rsplit('|',2)[-2].strip() if c05 else 'absent'
    paths=re.findall(r'knowledge/[\w.-]+\.md',c05.split('|')[3]) if c05 else []
    v6=tree/'corpus'/V6; txt=read(v6) if v6.is_file() else ''
    admitted=bool(re.search(r'^admission-status: admitted',txt,re.M)) and 'admission-status: rejected' not in txt
    print(f'K_HELD_BACKED={len(br)}/{len(rr)} score={10*len(br)/len(rr):.1f}')
    print(f'K_HELD_BACKED_STRICT={len(strict)}/{len(rr)}')
    print(f'C05_STATUS={status}')
    print('C05_KNOWLEDGE_COLUMN='+(' '.join(paths) if paths else '-'))
    print(f'C05_SINGLE_V6={"yes" if paths==[V6] else "no"}')
    print(f'V6_ENTRY_PRESENT={"yes" if v6.is_file() else "no"}')
    print(f'V6_ADMITTED_MARKED={"yes" if admitted else "no"}')
    gate_ok=lint_ok=False
    if v6.is_file():
        rc,(blocks,problems),_,_=emb(tree,V6); gate_ok=rc==0 and problems==0 and (blocks or 0)>=17
        print(f'C1_GATE=checked_blocks={blocks} problems={problems} exit={rc} ok={"yes" if gate_ok else "no"}')
        rc,out,_=run(tree,'lint_entry.py','--entry',str(v6),'--lane',str(LANE),cwd=tree)
        lint_ok=rc==0; print(f'C1_LINT={"; ".join(out.strip().splitlines())} exit={rc}')
    else: print('C1_GATE=n/a'); print('C1_LINT=n/a')
    votes=q_votes(); print(f'C1_W2_Q_VOTES={votes}/16')
    c1=len(br)==9 and len(strict)==9 and status=='held' and paths==[V6] and admitted and gate_ok and lint_ok and votes==16
    print(f'HOLDS_C1_V6={"yes" if c1 else "no"}')

    # C2 legs execute the actual CLI. Missing path should be a clean exit-2 classification.
    missing=gate_cli(tree,'--entry',str(tree/'corpus/knowledge/round-71-missing-entry.md'))
    miss_ok=missing.returncode==2 and 'could-not-evaluate: entry not found:' in missing.stdout and 'Traceback' not in missing.stderr
    print(f'C2_MISSING_ENTRY_EXIT2={int(miss_ok)}/1 rc={missing.returncode} stderr_traceback={"yes" if "Traceback" in missing.stderr else "no"}')
    # Isolated in-tree sleeper; the live CLI uses the production 120-second limit.
    d=scratch/'timeout-fixture'; shutil.rmtree(d,ignore_errors=True); shutil.copytree(tree/'corpus',d/'corpus')
    (d/'corpus/sleeper_r71.py').write_text('import time\ntime.sleep(300)\n',encoding='utf-8')
    slow=d/'corpus/knowledge/round-71-timeout-probe.md'; slow.parent.mkdir(parents=True,exist_ok=True)
    slow.write_text('```\n$ python3 -B corpus/sleeper_r71.py\nfinished\n```\n',encoding='utf-8')
    try:
        timed=gate_cli(d,'--entry',str(slow),timeout=TIMEOUT+30)
        timeout_ok=timed.returncode==2 and 'could-not-evaluate: command timed out after 120s:' in timed.stdout and 'Traceback' not in timed.stderr
        print(f'C2_TIMEOUT_EXIT2={int(timeout_ok)}/1 rc={timed.returncode} stderr_traceback={"yes" if "Traceback" in timed.stderr else "no"}')
    except subprocess.TimeoutExpired:
        timeout_ok=False; print('C2_TIMEOUT_EXIT2=0/1 outer_timeout=yes')
    grc,gout,gerr=run(tree,'check_embedded_outputs.py','--self-test',cwd=tree)
    selftest_ok=grc==0 and 'SELFTEST OK' in gout and 'missing-entry' in gout and 'timeout' in gout
    print(f'C2_GATE_SELFTEST={grc} named_legs={int("missing-entry" in gout and "timeout" in gout)}')
    print(f'HOLDS_C2_V1={"yes" if miss_ok and timeout_ok and selftest_ok else "no"}')

    # Round-70 instrument regression labels; deliberately printed individually.
    for tag,rel in (('R65','knowledge/round-65-apk-axml-byte-evidence.md'),('R67','knowledge/round-67-apk-axml-byte-evidence.md'),('R68','knowledge/round-68-apk-axml-byte-evidence.md'),('R69','knowledge/round-69-apk-axml-byte-evidence.md')):
        if (tree/'corpus'/rel).is_file():
            rc,(n,p),_,_=emb(tree,rel); print(f'EMB_{tag}=checked_blocks={n} problems={p} exit={rc}')
        else: print(f'EMB_{tag}=n/a')
    for label,rel,want in (('EMB_R68_BYTES_UNCHANGED','corpus/knowledge/round-68-apk-axml-byte-evidence.md',R68_SHA),('EMB_R65_BYTES_UNCHANGED','corpus/knowledge/round-65-apk-axml-byte-evidence.md',R65_SHA),('EMB_PINNED_SCRIPT_IS_S046','corpus/derive_axml_anchors_r68.py',S046_SHA)):
        p=tree/rel; ok=p.is_file() and sha(p)==want; print(f'{label}={"yes" if ok else "no"}')
    pins=tree/'corpus/embedded_output_pins.json'; r68=tree/'corpus/knowledge/round-68-apk-axml-byte-evidence.md'; killed=0
    if pins.is_file() and r68.is_file():
        q=scratch/'pin-mutant'; shutil.rmtree(q,ignore_errors=True); shutil.copytree(tree/'corpus',q/'corpus')
        for pin in json.loads(read(pins)).get(r68.name,{}).values():
            t=q/pin['use']
            if t.is_file(): t.write_bytes(t.read_bytes()+b'\n# tampered\n')
        rc,out,err=run(q,'check_embedded_outputs.py','--entry',str(q/'corpus/knowledge'/r68.name),cwd=q)
        killed=int(rc!=0 and PIN_MARKER in out)
    print(f'EMB_PIN_MUTANT_KILLED_ATTRIBUTED={killed}/1')

    # Existing calibration instrument hold.
    tool=tree/'corpus/self_assessment_check.py'; self_ok=False; mut=0
    if tool.is_file():
        rc,out,_=run(tree,'self_assessment_check.py','--root',str(tree),'--lane',str(LANE),cwd=tree)
        per=dict(re.findall(r'(SM\d)=(\d+)',out)); n=re.search(r'SELF_MISMATCH=(\d+)',out)
        for k in ('SM1','SM2','SM3','SM4','SM5','SM6'): print(f'{k}={per.get(k,"n/a")}')
        print(f'SELF_MISMATCH={n.group(1) if n else "n/a"} exit={rc}'); self_ok=bool(n) and int(n.group(1))==0 and rc==0
        # Preserve the previously registered fixture/mutant hold without an uncaught helper-order path.
        from importlib.util import spec_from_file_location,module_from_spec
        spec=spec_from_file_location('r70measure',LANE/'reports/round-70/measure.py'); mod=module_from_spec(spec); spec.loader.exec_module(mod)
        clean,mut=mod.self_check(tree,scratch); print(f'SELF_CLEAN_FIXTURE={int(clean)}'); print(f'SELF_MUTANTS_KILLED={mut}/6')
    else: print('SELF_MISMATCH=n/a'); print('SELF_MUTANTS_KILLED=n/a')
    # Retain all ten HOLD rows in the captured receipt.
    ps=sorted((tree/'corpus').glob('verify_*.py')); ok=0
    for p in ps:
        rc,out,err=run(tree,p.name,'--self-test',cwd=tree); ok+=rc==0; print('HOLD',p.name,f'exit={rc}',last_line(out+err)[:140])
    print(f'HOLD_REPLAY={ok}/{len(ps)}')
    frc=run(tree,'check_embedded_outputs.py','--self-test',cwd=tree)[0]
    print(f'GATE_SELFTEST=exit {frc}')
    families={'native-static':{'inspect_pe_resources'},'managed':{'inspect_managed_artifact'},'javascript':{'analyze_javascript_application'},'android':{'inspect_android_package'},'archives':{'inventory_artifact','inspect_artifact'},'firmware':{'inspect_firmware_regions'},'browser-runtime':{'inspect_web_page','capture_browser_scenario','observe_web_session'},'evm':{'inspect_evm_interface'}}
    seen=set()
    for p in sorted((tree/'corpus/live/runs').rglob('*.json')):
        try: x=json.loads(p.read_bytes())
        except (ValueError,UnicodeError): continue
        if isinstance(x,dict) and x.get('evidence_id') and x.get('normalized_result') is not None: seen.add(x.get('operation','unknown'))
    present=[k for k,v in families.items() if v & seen]; print(f'F_COVERAGE={len(present)}/{len(families)} score={10*len(present)/len(families):.1f}')
    fresh=0
    for rel in ('corpus/knowledge/seed.md','corpus/knowledge/2026-10-12-rea-readiness-checklist.md'):
        p=tree/rel
        if p.is_file(): fresh+=sum(1 for l in read(p).splitlines() if re.match(r'^\| [FK][0-9]+ .*\| (holds|STALE)',l))
    print(f'FRESH_ROWS={fresh}/18')
    holds=ok==len(ps)==10 and frc==0 and len(present)==5 and fresh==18
    print(f'HOLDS_OK_V8={"yes" if holds else "no"}')
    return 0 if holds else 1

if __name__=='__main__':
    a=sys.argv[1:]
    if len(a)!=1 or not (Path(a[0]).resolve()/'corpus').is_dir(): print('usage: measure.py TREE (TREE/corpus must exist)'); sys.exit(2)
    try: sys.exit(main(Path(a[0]).resolve()))
    except SystemExit: raise
    except BaseException:
        traceback.print_exc(); print('COUNTER_ERROR=uncaught exception (exit 2)'); sys.exit(2)
