#!/usr/bin/env python3
"""Build claim-specific skip-work controls from the frozen base and run the frozen counter."""
import os, pathlib, shutil, subprocess, sys
LANE=pathlib.Path('/home/vgpnk/Projects/shokunin/revenger-shokunin')
BASE='b7abcd875c84f4e1d6c8df966b6bd20f4154c53f'
ROOT=pathlib.Path('/fast/scratch/hyaku/revenger-r71/controls')
COUNTER=LANE/'reports/round-71/measure.py'
V6='knowledge/round-71-apk-axml-byte-evidence.md'

def archive(name):
    d=ROOT/name; shutil.rmtree(d,ignore_errors=True); d.mkdir(parents=True)
    data=subprocess.run(['git','-C',str(LANE),'archive',BASE,'corpus','SHONEN.md','SCORECARD.md','SKILL.md'],check=True,capture_output=True).stdout
    import tarfile,io
    with tarfile.open(fileobj=io.BytesIO(data),mode='r:') as tf: tf.extractall(d)
    return d

def run(name,mutate):
    d=archive(name); mutate(d)
    env=os.environ.copy(); env['HYAKU_SCRATCH']='/fast/scratch/hyaku'
    p=subprocess.run([sys.executable,'-B',str(COUNTER),str(d)],cwd='/',env=env,capture_output=True,text=True,timeout=360)
    out=p.stdout+p.stderr+f'CONTROL={name} EXIT={p.returncode}\n'
    target=LANE/'reports/round-71/controls'/f'{name}.log'; target.write_text(out,encoding='utf-8')
    shutil.rmtree(d,ignore_errors=True)
    print(name,'exit',p.returncode,'C1',next((x for x in out.splitlines() if x.startswith('HOLDS_C1_V6=')),'missing'),'votes',next((x for x in out.splitlines() if x.startswith('C1_W2_Q_VOTES=')),'missing'))

def flip(d,entry=None):
    p=d/'corpus/README.md'; text=p.read_text(encoding='utf-8'); lines=text.splitlines()
    for i,line in enumerate(lines):
        if line.startswith('| C05 '):
            c=line.split('|'); c[3]=f' `{V6}` ' if entry else ' — '; c[-2]=' held ' if entry else ' held '; lines[i]='|'.join(c); break
    p.write_text('\n'.join(lines)+'\n',encoding='utf-8')

def b(d): flip(d,False)
def c(d): flip(d,True)
def dcontrol(d):
    flip(d,True)
    src=LANE/'corpus/knowledge/round-70-apk-axml-byte-evidence.md'
    dst=d/'corpus'/V6; dst.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(src,dst)
    text=dst.read_text(encoding='utf-8').replace('admission-status: rejected','admission-status: admitted',1)
    marker='| Q15 | pass | this entry states no git object id; identity statements are file digests printed by item 14. |'
    assert marker in text
    text=text.replace(marker,marker+'\n| Q16 | pass | counter-forged statement; not independently checked |',1)
    dst.write_text(text,encoding='utf-8')

if __name__=='__main__':
    ROOT.mkdir(parents=True,exist_ok=True)
    controls=[('B-C1-readme-flip-only',b),('C-C1-admitted-stub',c),('D-C1-v5-copy-with-q16',dcontrol)]
    selected=set(sys.argv[1:])
    for name,mutate in controls:
        if not selected or name in selected: run(name,mutate)
