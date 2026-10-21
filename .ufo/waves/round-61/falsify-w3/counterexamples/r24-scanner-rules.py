# Scratch: which simple selector-candidate rules yield an empty output on r24 (and r19 as positive control).
# Reads the archived fixtures only; executes no bytecode.
import sys
from pathlib import Path
A = Path('/tmp/revenger-r61w3-W3EvmR24Immediate/landed/corpus/fixtures')
def load(name):
    if name == 'r19':
        raw = (A/'evm-r19/fixture.hex').read_bytes(); return bytes.fromhex(raw[2:-1].decode())
    return (A/f'evm-{name}/fixture.raw').read_bytes()
def walk(d):
    i, out = 0, []
    while i < len(d):
        op = d[i]; n = op-0x5f if 0x60 <= op <= 0x7f else 0
        out.append((i, op, d[i+1:i+1+n])); i += 1+n
    return out
def rule_walk_skip_jd(d):            # PUSH-skipping walk; PUSH4,EQ,PUSH1,JUMPI in instruction stream; target must be JUMPDEST in walk
    ins = walk(d); jd = {i for i, op, _ in ins if op == 0x5b}; res = []
    for k in range(len(ins)-3):
        a, b, c, e = ins[k:k+4]
        if a[1] == 0x63 and b[1] == 0x14 and c[1] == 0x60 and e[1] == 0x57:
            t = c[2][0]
            if t in jd: res.append((a[0], t))
    return res
def rule_walk_skip_nojd(d):          # same walk, no JUMPDEST requirement
    ins = walk(d); res = []
    for k in range(len(ins)-3):
        a, b, c, e = ins[k:k+4]
        if a[1] == 0x63 and b[1] == 0x14 and c[1] == 0x60 and e[1] == 0x57: res.append((a[0], c[2][0]))
    return res
def rule_raw_nojd(d):                # no PUSH skipping, raw 4-byte pattern, no JUMPDEST requirement
    res = []
    for i in range(len(d)-8):
        if d[i] == 0x63 and d[i+5] == 0x14 and d[i+6] == 0x60 and d[i+8] == 0x57: res.append((i, d[i+7]))
    return res
def rule_raw_rawjd(d):               # no PUSH skipping, raw pattern, target byte must be raw 0x5b
    return [(i, t) for i, t in rule_raw_nojd(d) if d[t:t+1] == b'\x5b']
for name in ['r19', 'r24']:
    d = load(name[1:] if name == 'r19' else 'r24') if False else (load('r19') if name == 'r19' else load('r24'))
    print(name, 'len', len(d))
    for f in [rule_walk_skip_jd, rule_walk_skip_nojd, rule_raw_nojd, rule_raw_rawjd]:
        print(f'  {f.__name__:20s} {f(d)}')
