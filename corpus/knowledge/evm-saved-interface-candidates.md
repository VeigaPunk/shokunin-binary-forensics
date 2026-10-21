source: S026 (saved `inspect_evm_interface` records, rounds 19 and 21–26); S016 execution-specs v2.20.0 `instructions/__init__.py` lines 55, 106, 109, 125 and `runtime.py` lines 22-69; S017 Yellow Paper Shanghai efc5f9a §9.4.3 eqs. (160)-(162), p.15; S018 Solidity v0.8.37 ABI §Function Selector; S019 Solidity §Encoding of the Metadata Hash in the Bytecode
verified-at: 2026-10-21, lane base e0a4b0c4348ef1fade46539f520e94fa140c4d8a; fixture bytes and saved records re-derived by `## Reproduce`
recheck: save the `## Reproduce` block as a file and run `python3 -B <file>` from the lane root (stdlib only, reads fixtures and saved JSON, executes no bytecode); compare with `## Provenance`
coverage-map: C09

# Saved EVM interface records on seven authored fixtures — reported candidates and empty outputs

This entry is about what seven saved REA outputs (`rea-agents@6.4.0` per the
round ledgers, provider `evmole-interface` `evmole@0.9.3` inside the records)
report for the lane's seven authored, inert byte fixtures, checked against an
independent byte walk. It is not a statement about deployed contracts, about
REA's current release (the host skill now names `rea-agents@6.7.0`, S002), or
about the provider's internal method. No bytecode was executed and no chain
was queried.

## Observation

Values come from the `## Reproduce` output below.

1. **Opcode ground truth.** S016 defines `PUSH4 = 0x63`, `EQ = 0x14`,
   `JUMPI = 0x57`, `JUMPDEST = 0x5B`, and its valid-destination scan skips
   PUSH-N immediate data ("The jump destination shouldn't be part of the data
   corresponding to `PUSH-N` opcodes", `runtime.py`). S017 states the same rule
   for the Shanghai revision. The walk below applies exactly that rule.
2. **Reported candidates (three records).** r19 and r21 (the same 18 decoded
   bytes, hex and raw carriers) each report one function, selector
   `0xdeadbeef`, `bytecode_offset` 16. r22 reports `0xaaaaaaaa`@30 and
   `0xbbbbbbbb`@32. In each case the offset is the PUSH1 operand of a JUMPI
   whose target byte is a valid JUMPDEST (16; 30 and 32), and the selector is
   the immediate of the PUSH4 at 6 (r19/r21) or at 7 and 17 (r22). The PUSH4
   locations themselves appear in no record field.
3. **Empty outputs (four records).** r23 (`PUSH4 c0ffee00`, POP, STOP; no JUMPI,
   no JUMPDEST), r24 (one PUSH32 whose immediate contains the r19 pattern; the
   only 0x63 byte is at offset 1, inside that immediate; no executable PUSH4),
   r25 (entry STOP, then a PUSH4/EQ/JUMPI whose target 16 is a STOP, not the
   JUMPDEST at 17) and r26 (r25 with the operand changed to 17, so the target
   is a valid JUMPDEST) all report `functions: []`.
4. **Common flags.** All seven records carry `evidence_kind: inferred`,
   `discovery_completeness: unknown` and `runtime_execution: not-performed`,
   and each record's subject digest equals the fixture bytes' SHA-256.
5. **Selectors are authored constants.** No fixture `truth.json` declares a
   function signature (round-61 seat report `.ufo/waves/round-61/build/ExecSelectorKeccak.md`).
   S018 defines a selector as the first four bytes of the Keccak-256 hash of a
   canonical signature, so `deadbeef`, `aaaaaaaa`, `bbbbbbbb` and `c0ffee00`
   are test constants, not derived selectors.

## Inference

- Where a candidate was reported (r19, r21, r22), `bytecode_offset` equals the
  JUMPI target, a valid JUMPDEST, not the PUSH4 site. Kaidoku holds the same
  reading for its own records (cross-lane note below); here it is observed on
  three more authored records only.
- r26 is the strongest negative: a statically valid PUSH4 → EQ → PUSH1 → JUMPI
  → JUMPDEST pattern sits behind an entry STOP and is not reported. "The
  provider reports every statically valid selector/JUMPDEST pattern" is
  therefore false for this provider version on this input.
- r24 shows that a raw byte search for `0x63` would find a non-instruction at
  offset 1 where the provider reports nothing. r24 does **not** show that the
  provider excludes PUSH data: its embedded JUMPI target (0x10) is not a
  JUMPDEST and the file has no 0x5B byte, so several simpler rules also yield
  an empty output.

## Unknown

- Why r25 and r26 are empty. Two post-hoc rules fit all seven outputs (only
  code reachable from pc 0 is considered; the scan stops at the first STOP);
  neither is validated, and no fixture separates them. No cause is asserted (Q07).
- Whether an empty output means no callable interface. Every record marks
  `discovery_completeness: unknown`, so an empty list is not read as absence.
- Behavior on compiled bytecode: dispatchers using binary search, PUSH2
  destinations, short selector pushes, fallbacks, proxies, and the CBOR
  metadata tail that solc appends by default (S019). None is in these fixtures.
- Whether the saved `evidence_id` values can be recomputed; four seats tried
  canonical-JSON forms without a match. They are recorded identifiers here.
- `payable`, `dispatch: abi` and empty-argument labels are the provider's own
  inferences and have no truth counterpart in the fixtures.

## Limitations

- Seven authored fixtures, two distinct positive byte strings (r19 = r21),
  three reported pairs; one fixture per negative class. No rate is quoted.
- One provider version, run 2026-10-12 and not re-run this round. The records'
  `authority: shipped-artifact` label describes a file class, not origin, and
  their locator paths point into an older checkout (identity is by digest, Q09).
- `corpus/verify_evm_evidence.py` reads r19 only, and its own run detects none
  of 37 single-conjunct deletions (round-61 `MutantEvmVerifier.md`), so under
  Q13 it is not credited as a guard; all seven fixtures rest on this entry's
  walk. `corpus/fixtures/evm-r24/truth.json` lists embedded-pattern offsets
  `[1, 9]`; the bytes contain the pattern only at 1 (fixture left unchanged).

## Cross-lane contest (Q10)

Kaidoku holds the JUMPDEST reading of `bytecodeOffset`
(`kaidoku-shokunin/corpus/knowledge/2026-10-13-r3-evm-interface.md:151-153`,
EVM row `kaidoku-shokunin/PROVINCE.md:54`); it is cited here as prior art, not
re-claimed. This entry's own ground is the negative and decoy fixtures above.
Kasegi owns deployed-code identity and claimability
(`kasegi-shokunin/PROVINCE.md:25`); nothing here bears on either. The
kaidoku/revenger split (ADJ-06) remains with the operator.

## Reproduce

```python
import hashlib, json
from pathlib import Path
F, R = Path('corpus/fixtures'), Path('corpus/live/runs')
CASES = {19: 'fixture.hex', 21: 'fixture.raw', 22: 'fixture.raw', 23: 'fixture.raw',
         24: 'fixture.raw', 25: 'fixture.raw', 26: 'fixture.raw'}
sha = lambda b: hashlib.sha256(b).hexdigest()
def code(r, name):
    raw = (F / f'evm-r{r}' / name).read_bytes()
    return raw, (bytes.fromhex(raw[2:-1].decode()) if name.endswith('.hex') else raw)
def walk(d):  # instruction starts; PUSH1..PUSH32 (0x60..0x7f) skip their immediates (S016 runtime.py)
    i, out = 0, []
    while i < len(d):
        op = d[i]; n = op - 0x5f if 0x60 <= op <= 0x7f else 0
        out.append((i, op, d[i + 1:i + 1 + n])); i += 1 + n
    return out
for r, name in CASES.items():
    raw, d = code(r, name)
    ins = walk(d)
    valid = [i for i, op, _ in ins if op == 0x5b]           # valid JUMPDEST set (S016/S017)
    push4 = [(i, imm.hex()) for i, op, imm in ins if op == 0x63]
    jumpi = []                                               # PUSH1 <dest> immediately before JUMPI
    for k, (i, op, _) in enumerate(ins):
        if op == 0x57 and k and ins[k - 1][1] == 0x60:
            t = ins[k - 1][2][0]; jumpi.append((i, t, t in valid))
    raw63 = [i for i, b in enumerate(d) if b == 0x63]
    rec = json.loads((R / f'round-{r}/inspection.json').read_text())
    nr = rec['normalized_result']
    fn = [(f['selector'], f['bytecode_offset']) for f in nr['functions']]
    print(f'r{r} bytes={len(d)} sha256={sha(d)[:16]} push4={push4} raw_0x63={raw63} '
          f'jumpi(at,dest,valid)={jumpi} jumpdest={valid} entry_op=0x{d[0]:02x}')
    print(f'   saved {rec["evidence_id"][:19]} file_sha256={sha((R / f"round-{r}/inspection.json").read_bytes())[:16]} '
          f'functions={fn} kind={nr["evidence_kind"]} completeness={nr["discovery_completeness"]} '
          f'runtime={nr["runtime_execution"]} subject_eq_bytes={rec["subject"]["digest"]["sha256"] in (sha(raw), sha(d))}')
```

## Provenance (Q11)

Observed output of the block above, run from the lane root on 2026-10-21 at
base `e0a4b0c`, exit 0 (the walk is a manual reproduction, not a REA call):

```text
r19 bytes=18 sha256=d1086bce32141782 push4=[(6, 'deadbeef')] raw_0x63=[6] jumpi(at,dest,valid)=[(14, 16, True)] jumpdest=[16] entry_op=0x60
   saved ev_0ad0097eb137ff91 file_sha256=e892dd18ff219f71 functions=[('0xdeadbeef', 16)] kind=inferred completeness=unknown runtime=not-performed subject_eq_bytes=True
r21 bytes=18 sha256=d1086bce32141782 push4=[(6, 'deadbeef')] raw_0x63=[6] jumpi(at,dest,valid)=[(14, 16, True)] jumpdest=[16] entry_op=0x60
   saved ev_4810eda7b540fbf2 file_sha256=395c4f48e7efd7ea functions=[('0xdeadbeef', 16)] kind=inferred completeness=unknown runtime=not-performed subject_eq_bytes=True
r22 bytes=34 sha256=94c1790f966b78a9 push4=[(7, 'aaaaaaaa'), (17, 'bbbbbbbb')] raw_0x63=[7, 17] jumpi(at,dest,valid)=[(15, 30, True), (25, 32, True)] jumpdest=[30, 32] entry_op=0x60
   saved ev_24fe0001213ec58a file_sha256=c55f69727ce2e627 functions=[('0xaaaaaaaa', 30), ('0xbbbbbbbb', 32)] kind=inferred completeness=unknown runtime=not-performed subject_eq_bytes=True
r23 bytes=7 sha256=8047ddff11234c2d push4=[(0, 'c0ffee00')] raw_0x63=[0] jumpi(at,dest,valid)=[] jumpdest=[] entry_op=0x63
   saved ev_296e7ed723c7356b file_sha256=ce9fe51536af461e functions=[] kind=inferred completeness=unknown runtime=not-performed subject_eq_bytes=True
r24 bytes=35 sha256=b69834e0ef786e3c push4=[] raw_0x63=[1] jumpi(at,dest,valid)=[] jumpdest=[] entry_op=0x7f
   saved ev_50d5ffb1fdbd17c4 file_sha256=ec9e147db2b042f4 functions=[] kind=inferred completeness=unknown runtime=not-performed subject_eq_bytes=True
r25 bytes=19 sha256=2d87a4e203ebf590 push4=[(7, 'deadbeef')] raw_0x63=[7] jumpi(at,dest,valid)=[(15, 16, False)] jumpdest=[17] entry_op=0x00
   saved ev_23a9464bf2d8c3de file_sha256=4f677a209d08c3f9 functions=[] kind=inferred completeness=unknown runtime=not-performed subject_eq_bytes=True
r26 bytes=19 sha256=ebe2d6757a7acd4c push4=[(7, 'deadbeef')] raw_0x63=[7] jumpi(at,dest,valid)=[(15, 17, True)] jumpdest=[17] entry_op=0x00
   saved ev_482e41e68b6c5f35 file_sha256=bf2b2337b83f694f functions=[] kind=inferred completeness=unknown runtime=not-performed subject_eq_bytes=True
```

Full Evidence IDs (recorded, not recomputed): r19
`ev_0ad0097eb137ff9196b29ac3fb6109d8f72ee0761e2655fa1fca594295cf6f42`, r21
`ev_4810eda7b540fbf2d4265c0f9deb3886dc009945cb77276b980f5502112cfc85`, r22
`ev_24fe0001213ec58a588d086e0fe55677d749f3eb6998afe6ee6095ff9dc4af4b`, r23
`ev_296e7ed723c7356b1cfbeee5dadc11283e5efe74535d544114ebf3b692f77201`, r24
`ev_50d5ffb1fdbd17c4896409ca4cc8b20d7ed344ef4011029bea4aa474b7f0ab9e`, r25
`ev_23a9464bf2d8c3de3614176efa53016f002ddade19f1ae842b4325ba2d095579`, r26
`ev_482e41e68b6c5f358fe660bc70eaf55f69c7b487fd61774e1a443571aecec090`.
Provider string `evmole@0.9.3` is read from the r19 record; `rea-agents@6.4.0`
is recorded in the round ledgers only.

## QUALITY check

| Q | verdict | basis |
|---|---|---|
| Q01 | pass | opcode values and the PUSH-data rule rest on S016/S017 (tier A for that scope, opened 2026-10-21); selector definition on S018; saved outputs on S026 (own-work, tier A for what they contain) |
| Q02 | pass | `source:`, `verified-at:`, `recheck:` and `coverage-map: C09` headers |
| Q03 | pass | expected offsets and validity come from the byte walk and the S016 rule, not from the saved records |
| Q04 | pass | provider and version named as recorded; only the provider's explicit fields are scored; the walk is labeled manual |
| Q05 | pass (past tense) | no current capability claim; outputs are dated 2026-10-12 and not re-probed |
| Q06 | pass | every fixture premise re-derived from the built bytes by the block above |
| Q07 | pass | r25/r26 causes left unknown; post-hoc rules named as unvalidated |
| Q08 | superseded by Q11 | — |
| Q09 | pass | digests bind bytes only; locator paths and the `shipped-artifact` label are not read as origin |
| Q10 | pass | scoped to seven fixtures and one provider version; kaidoku and kasegi ground reported, not absorbed |
| Q11 | pass | every count, offset and digest carries the command above and its output |
| Q12 | n/a | no rejected source row is cited as support |
| Q13 | pass | `verify_evm_evidence.py` is not credited as a guard (0/37 single-conjunct deletions detected by its own run); every value rests on this block |
