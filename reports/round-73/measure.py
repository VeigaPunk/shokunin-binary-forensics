#!/usr/bin/env python3
"""Round-73 frozen C10 coverage predicate; network-free over a committed archive."""
import argparse, hashlib, json, re
from pathlib import Path
ENTRY='corpus/knowledge/2026-10-29-rea-evidence-ledger-discipline.md'
GROUPS={f'R73Q{start:02d}': [f'Q{i:02d}' for i in range(start,start+4)] for start in (1,5,9,13)}
def digest(text):
    return hashlib.sha256(re.sub(r'^admission-status: (candidate|admitted|rejected)$','admission-status: candidate',text,flags=re.M).encode()).hexdigest()
def main():
    p=argparse.ArgumentParser(); p.add_argument('tree',type=Path); p.add_argument('--control-status-flip-only',action='store_true'); a=p.parse_args(); t=a.tree
    if not (t/'corpus/README.md').is_file() or not (t/'corpus/SOURCES.md').is_file(): print('could-not-evaluate: missing corpus inputs'); return 2
    rows={}; duplicate=False
    for line in (t/'corpus/SOURCES.md').read_text().splitlines():
        cells=[x.strip() for x in line.strip().strip('|').split('|')]
        if len(cells)==11 and re.fullmatch(r'S\d{3,}',cells[0]):
            duplicate |= cells[0] in rows; rows[cells[0]]=cells
    mapped=[]; c10=[]
    for line in (t/'corpus/README.md').read_text().splitlines():
        c=[x.strip() for x in line.strip().strip('|').split('|')]
        if len(c)==5 and re.fullmatch(r'C\d+',c[0]):
            mapped.append(c)
            if c[0]=='C10': c10=c
    text=(t/ENTRY).read_text() if (t/ENTRY).is_file() else ''
    expected=json.loads(Path(__file__).with_name('candidate-pin.json').read_text())['sha256']
    pinned=bool(text) and digest(text)==expected
    admitted=bool(re.search(r'^admission-status: admitted$',text,re.M))
    status='held' if a.control_status_flip_only else (c10[4] if c10 else 'absent')
    linked=bool(c10) and re.findall(r'knowledge/[\w.-]+\.md',c10[2])==[ENTRY.removeprefix('corpus/')]
    source_ok=all(s in rows and rows[s][7]=='mined' and ENTRY in rows[s][10] and s in text for s in (f'S{i:03d}' for i in range(96,110))) and not duplicate
    votes=0
    for seat,qs in GROUPS.items():
        v=t/'.ufo/waves/round-73/votes'/f'{seat}.json'
        try:
            obj=json.loads(v.read_text()); ds=obj['decisions']
            if obj['seat']==seat and obj['candidate_sha256']==expected and set(ds)==set(qs) and all(ds[q] in ('PASS','n/a') for q in qs): votes+=4
        except (OSError,ValueError,KeyError,TypeError): pass
    held=sum(c[4]=='held' and all((t/'corpus'/rel).is_file() for rel in re.findall(r'knowledge/[\w.-]+\.md',c[2])) and bool(re.findall(r'knowledge/[\w.-]+\.md',c[2])) for c in mapped)
    ok=len(mapped)==15 and held==9 and status=='held' and linked and pinned and admitted and source_ok and votes==16
    print(f'K_HELD_BACKED={held}/{len(mapped)}')
    print(f'C10_STATUS={status}'); print(f'C10_CANDIDATE_PIN={int(pinned)}/1'); print(f'C10_SOURCES={int(source_ok)}/1'); print(f'C10_Q_VOTES={votes}/16')
    print(f'C10_HELD_BACKED={int(ok)}/1'); print('HOLDS_C10='+('yes' if ok else 'no'))
    return 0
if __name__=='__main__': raise SystemExit(main())
