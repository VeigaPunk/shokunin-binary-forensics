GRADE: HOLDS — C09 Reproduce walk detects the three assigned one-byte fixture mutations by Provenance comparison
Axes: mutation-class coverage; stdout-versus-exit sensitivity; exact restoration. Scope: only this bounded mutation probe, not admission of C1 generally.
Revision: `ab580698212258a55e43e9bb9bf6ac78c91eae2a` (observed `git rev-parse` output). Python 3.14.8; no REA producer, bytecode, fixture JavaScript, network or service execution.
Archive command executed: `mkdir -p /tmp/revenger-r61w3-W3EvmWalkMutant && git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive --format=tar ab580698212258a55e43e9bb9bf6ac78c91eae2a | tar -x -C /tmp/revenger-r61w3-W3EvmWalkMutant`.
Expected detector: `corpus/knowledge/evm-saved-interface-candidates.md:3` requires comparing stdout with Provenance; lines 105–137 supply the exact Python block and 146–159 its expected 14 lines. It is not an exit-status gate.
Executed: `python3 -B /tmp/revenger-r61w3-W3EvmWalkMutant-probe.py`; three independent full archive copies `/tmp/revenger-r61w3-W3EvmWalkMutant-r{22,26,24}`, three concurrent workers, 15-second timeout per block invocation. Only one raw fixture byte changed per worker.
Block SHA-256: `9c64f619c6d74931b17196f7dee7e439c2d42d2853343ad01bd3c327e4eccfeb`; expected stdout SHA-256: `0480a2f78af46082b6cb82f51a6816965fef4b0e3f86cbda6e1bb8a38c722d49`.
For EACH of the three cases, actual harness output was:
`baseline: exit=0 equals_provenance=True lines=14 stderr=''`
`mutant: exit=0 equals_provenance=False lines=14 stderr=''`
`restored: exit=0 equals_provenance=True lines=14 stderr=''`
No baseline failed; no inconclusive case. Below are the exact two changed stdout lines per mutant; the other twelve lines matched baseline.

M1 — `corpus/fixtures/evm-r22/fixture.raw`, offset 30, `5b→00` (JUMPDEST→STOP). Expected: destination 30 loses validity; saved subject digest no longer binds fixture. KILLED by comparison.
`r22 bytes=34 sha256=a3f7d31001df69a9 push4=[(7, 'aaaaaaaa'), (17, 'bbbbbbbb')] raw_0x63=[7, 17] jumpi(at,dest,valid)=[(15, 30, False), (25, 32, True)] jumpdest=[32] entry_op=0x60`
`   saved ev_24fe0001213ec58a file_sha256=c55f69727ce2e627 functions=[('0xaaaaaaaa', 30), ('0xbbbbbbbb', 32)] kind=inferred completeness=unknown runtime=not-performed subject_eq_bytes=False`
SHA-256 before=restored: `94c1790f966b78a9a5cc61bdc9ad4b805aaea6989e37773f66ff433deeb1dbe2`; mutated: `a3f7d31001df69a950ee1cf41c3e13ea2e574f54eb386b315bc78572111220c0`.

M2 — `corpus/fixtures/evm-r26/fixture.raw`, offset 14, `11→10` (destination 17→16). Expected: target changes from valid JUMPDEST to STOP, contradicting entry lines 35–37 and 53–56 if left unnoticed. KILLED by comparison.
`r26 bytes=19 sha256=2d87a4e203ebf590 push4=[(7, 'deadbeef')] raw_0x63=[7] jumpi(at,dest,valid)=[(15, 16, False)] jumpdest=[17] entry_op=0x00`
`   saved ev_482e41e68b6c5f35 file_sha256=bf2b2337b83f694f functions=[] kind=inferred completeness=unknown runtime=not-performed subject_eq_bytes=False`
SHA-256 before=restored: `ebe2d6757a7acd4c5b9de82441f66e70561350267114e445a2d6b8d037f8e97d`; mutated: `2d87a4e203ebf590beab57cf7318ccf93c92035d7929d0bc16e6850433f5e8f7`.

M3 — `corpus/fixtures/evm-r24/fixture.raw`, offset 0, `7f→7e` (PUSH32→PUSH31). Expected: entry opcode changes; embedded 0x63 remains immediate data, so no new executable PUSH4 is expected. KILLED by comparison.
`r24 bytes=35 sha256=5f10e5ca300cda91 push4=[] raw_0x63=[1] jumpi(at,dest,valid)=[] jumpdest=[] entry_op=0x7e`
`   saved ev_50d5ffb1fdbd17c4 file_sha256=ec9e147db2b042f4 functions=[] kind=inferred completeness=unknown runtime=not-performed subject_eq_bytes=False`
SHA-256 before=restored: `b69834e0ef786e3c001b2c833c8c0388acc017de14d06110cfa85d4948685d93`; mutated: `5f10e5ca300cda91aca4eb0106d10ea7e50deabd6188390692a0b6c6e2b6a8a6`.

Restoration evidence: each worker reported `restored_exactly=True manifest_entries=613`; every relative-path/full-SHA-256 manifest entry before mutation equaled its restored counterpart, including saved records and entry. Single-byte differences were exactly `[30]`, `[14]`, `[0]`, respectively. Original extracted archive was never mutated.
Raw nine-run outputs and complete before/after manifests remain in `/tmp/revenger-r61w3-W3EvmWalkMutant-results/r{22,26,24}.json`; reproducible detector/mutation recipe below avoids relying solely on temporary logs (run only after the archive command above):
```python
import subprocess, sys
from pathlib import Path
root = Path('/tmp/revenger-r61w3-W3EvmWalkMutant')
entry = (root/'corpus/knowledge/evm-saved-interface-candidates.md').read_text()
block = entry.split('```python\n', 1)[1].split('```', 1)[0]
expected = entry.split('## Provenance (Q11)', 1)[1].split('```text\n', 1)[1].split('```', 1)[0]
def run():
    p = subprocess.run([sys.executable, '-B', '-c', block], cwd=root, text=True, capture_output=True, timeout=15)
    print(p.returncode, p.stdout == expected, repr(p.stderr)); print(p.stdout, end='')
for r, offset, old, new in [(22,30,0x5b,0),(26,14,0x11,0x10),(24,0,0x7f,0x7e)]:
    target = root/f'corpus/fixtures/evm-r{r}/fixture.raw'
    saved = target.read_bytes(); assert saved[offset] == old
    run()
    try:
        changed = bytearray(saved); changed[offset] = new; target.write_bytes(changed); run()
    finally:
        target.write_bytes(saved)
    run(); assert target.read_bytes() == saved
```
VERDICT: 3/3 killed, 0/3 survived under the entry's required stdout/Provenance comparison; all 3/3 survive an exit-code-only detector because every mutant still exits 0. This bounds the guard to comparison, not automatic rejection; no contradiction of the stated recheck was found. Installs/updates: none.
