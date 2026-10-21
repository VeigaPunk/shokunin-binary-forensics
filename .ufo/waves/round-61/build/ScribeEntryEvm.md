# ScribeEntryEvm — round 61, C09 draft (EVM PUSH4 selector candidates)

Seat: ScribeEntryEvm (leaf, read-only on the lane). Base read: `e0a4b0c4348ef1fade46539f520e94fa140c4d8a`.
Wrote: this report only. Nothing in `corpus/` was written. No verifier was run; the EVM check
results below come from the lane's recorded `measure-before.log` and are cited as recorded.
Installs: none. Derivations were stdlib `python3 -B` reads of fixture bytes and saved JSON (2026-10-21).

## Status

Draft entry ready below. NOT admissible yet: Q01 fails until an opened, tier-A SOURCES row covers
EVM opcode values and the PUSH4/JUMPDEST rule. S001–S015 contain no EVM row (checked
`corpus/SOURCES.md:15-30`). C1 prediction K_HELD=6/14 therefore does not follow from this draft alone.

## Findings (path:line or command + output)

1. Fixture identities match `truth.json` for all seven fixtures (walk output, Reproduce step 2).
   r19 carrier 39 bytes, decoded 18; r21 = r19 decoded; r22 34; r23 7; r24 35; r25 19; r26 19.
2. r19 decoded byte walk: PUSH4 at 6, immediate `deadbeef` at 7–10, EQ at 11, PUSH1 0x10 at 12–13,
   JUMPI at 14, STOP at 15, JUMPDEST at 16. The saved candidate `bytecode_offset=16` is the JUMPDEST,
   not the PUSH4 (6) or immediate (7). No opcode or immediate offset field exists in any saved record
   (key scan of `corpus/live/runs/round-*/inspection.json`, only `bytecode_offset` carries "offset").
3. Positive set, saved vs bytes: r19 `ev_0ad0097e…` and r21 `ev_4810eda7…` give one candidate
   `0xdeadbeef@16`; r22 `ev_24fe0001…` gives `0xaaaaaaaa@30` and `0xbbbbbbbb@32`, matching JUMPDEST at 30 and 32.
4. Negatives: r23 (`PUSH4 c0ffee00`, POP, STOP; no compare/jump) and r24 (PUSH32 whose immediate
   contains `63deadbeef14601057`) both give `functions: []`. In r24 the only 0x63 byte is at offset 1,
   inside the PUSH32 immediate, so a naive byte scan would hit where the walk finds no instruction.
5. Falsifier pair: r25 = `00` followed by the r19 decoded bytes (leading STOP). Its operand 0x10 now
   points at STOP (16). Saved output `functions: []`. r26 changes byte 14 from 0x10 to 0x11, so the
   operand reaches JUMPDEST at 17. Saved output is still `functions: []`.
6. `corpus/fixtures/evm-r24/truth.json` `embedded_pattern_offsets: [1, 9]`. Byte search finds the
   9-byte pattern once, at 1; byte 9 is 0x57 inside it. The second entry is inconsistent with the
   bytes (finding for the lane; not edited).
7. `corpus/verify_evm_evidence.py:10-11` loads only `evm-r19` and `live/runs/round-19/inspection.json`.
   The recorded base log (`reports/round-61/measure-before.log`) reports `HOLD verify_evm_evidence.py
   exit=0 NEGATIVE REJECTED candidate destination mismatch`. r21–r26 have no verifier.

## Draft entry — `corpus/knowledge/evm-push4-selector-candidates.md`

```text
source: S### TBD — EVM opcode values (STOP 0x00, PUSH1 0x60, PUSH4 0x63, PUSH32 0x7f, EQ 0x14, JUMPI 0x57,
  JUMPDEST 0x5b) and the PUSH immediate-length rule. No SOURCES row opened in round 61 yet; the
  opcode-spec scouts' rows are pending. Entry is not admissible until this row exists (Q01).
source: S### TBD — own-work saved REA records `corpus/live/runs/round-19/inspection.json`,
  `round-21`…`round-26` (`inspect_evm_interface`, provider `evmole-interface` `evmole@0.9.3`, via
  `rea-agents@6.4.0` per `round-19/LEDGER.md`). Needs its own SOURCES row (analog of S013).
verified-at: 2026-10-21 (lane base e0a4b0c); fixture bytes and saved JSON re-derived by the Reproduce block
recheck: `python3 -B -` on the `## Reproduce` code blocks, from the lane root (stdlib only, read-only)
coverage-map: C09

# EVM PUSH4 selector candidates and JUMPDEST destinations — authored fixtures r19–r26

Narrow claims on seven authored, inert EVM byte fixtures (`corpus/fixtures/evm-r19`, `evm-r21`…`evm-r26`;
no `evm-r20`). Every offset below was re-derived from fixture bytes on 2026-10-21 by the Reproduce
block, not taken from the saved record (Q03/Q08).

## Observation

1. Fixture identity. r19 `fixture.hex`: 39 carrier bytes, decoded 18 bytes; r21 `fixture.raw` = those
   18 decoded bytes. Digests are in `## Provenance`.
2. Linear walk of r19 decoded bytes (manual decode, skipping PUSH immediates):
   `0 PUSH1 00; 2 CALLDATALOAD; 3 PUSH1 e0; 5 SHR; 6 PUSH4 deadbeef (immediate 7–10); 11 EQ;
   12 PUSH1 10; 14 JUMPI; 15 STOP; 16 JUMPDEST; 17 STOP`.
3. Saved record r19 (`ev_0ad0097eb137ff9196b29ac3fb6109d8f72ee0761e2655fa1fca594295cf6f42`): one
   function, selector `0xdeadbeef`, `bytecode_offset` 16, `dispatch` abi, `evidence_kind` inferred,
   `discovery_completeness` unknown, `runtime_execution` not-performed. Offset 16 = the JUMPDEST in item 2.
   The record has no PUSH4 or immediate offset field.
4. Saved record r21 (`ev_4810eda7…`, raw carrier of the same bytes): the same candidate at 16.
5. Saved record r22 (`ev_24fe0001…`, two branches): `0xaaaaaaaa@30` and `0xbbbbbbbb@32`. Byte walk:
   PUSH4 at 7 and 17, JUMPDEST at 30 and 32.
6. Saved record r23 (`ev_296e7ed7…`, PUSH4 `c0ffee00` then POP and STOP, no compare or jump): `functions: []`.
7. Saved record r24 (`ev_50d5ffb1…`, `PUSH32` immediate containing `63deadbeef14601057`): `functions: []`.
   Byte 0x63 occurs once in the file, at offset 1, inside the PUSH32 immediate.
8. Saved record r25 (`ev_23a9464b…`): r25 = `00` || r19 decoded bytes. Leading STOP at 0;
   PUSH4 at 7; operand 0x10 points at STOP 16, not JUMPDEST 17. `functions: []`.
9. Saved record r26 (`ev_482e41e6…`): r25 with byte 14 changed 0x10 → 0x11, so the operand points at
   JUMPDEST 17. `functions: []`.

## Inference

- In r19, r21 and r22 the reported `bytecode_offset` equals the JUMPDEST that the PUSH1/JUMPI pair
  reaches. That the provider derives candidates from this shape is inference; its mechanism is not observed.
- In r22 the two candidate selectors are the two PUSH4 immediates, one for one. No wider mapping is inferred.
- A decoder that treats every 0x63 byte as PUSH4 would report a PUSH4 at offset 1 in r24 that is not an
  instruction. The record reports no candidate there, so r24 is a falsifier for naive byte scanning.
- Across r19 (one candidate), r25 and r26 (none each), the outcome tracks the leading STOP in these three
  records, not the destination byte. Only three records vary this way; no single-variable control exists.

## Unknown
- Fork scope (declared): opcode constants (0x14, 0x57, 0x60, 0x63, 0x5b) are read from the execution-specs table at Osaka `v2.20.0` (source id TBD, row pending). The destination-validity rule (eqs. (160)–(161)) is read from the Yellow Paper at Shanghai `efc5f9a` (source id TBD, row pending). `0x5b` is the only constant cross-covered by both. The entry uses no opcode introduced after Shanghai (no PUSH0 0x5f, no MCOPY, no TLOAD). Not a single-fork claim.
- PUSH4 width (0x63 → 4-byte immediate): derived from bytes by the Reproduce walk (advances 5 bytes across it), a consistency check on the fixtures. It presupposes the `PUSH_n = 0x5f+n` rule, which is itself the unsourced table row, so it is not an independent source. Do not cite the paper for it; the paper elides the row.

- Why the candidate disappears when a leading STOP is present (r25, r26). The mechanism is not
  reproduced; no cause is asserted (Q07).
- Whether empty output means no callable dispatch. The record's own limitation says it does not:
  "Empty results do not prove the absence of callable dispatch."
- The numeric opcode values and the JUMPDEST validity rule, pending the source row (S### TBD).
- `discovery_completeness` (recorded `unknown`), selector names, argument types, mutability beyond the
  provider's `payable` inference, deployed status and hardfork (recorded `unknown`).
- Why `truth.json` for r24 lists embedded-pattern offset 9 (author error or intent).

## Peer-reported source constraints (not verified by this seat)

Reported by SrcYellowPaperJumpdest (`.ufo/waves/round-61/build/SrcYellowPaperJumpdest.md`, sha256 `fee85ea0…f90c`). This seat did not open the Yellow Paper; the S### id stays TBD until the main agent merges and opens the row.

- Jump-destination definition: eqs. (160)–(162), p.15 (section 9.4.3). A 0x5b inside PUSH1..PUSH32 immediate data is not a destination.
- JUMPI guard: eq. (158), p.15. An invalid destination is exceptional only when the condition word is nonzero. A not-taken JUMPI does not validate its target.
- The paper does not print the 0x63 / PUSH4 row (the table elides between PUSH2 and PUSH32). Selector role, PUSH4 width and selector-to-destination mapping are [INFERENCE].
- The valid-destination set scans the whole code array with no metadata carve-out. A valid-but-unreached JUMPDEST is still a valid destination; keep "valid/candidate" distinct from "taken/reachable" ([INFERENCE] for the trailer case).
- Anchors the peer names for the entry's `source:` citation: §9.4.2 eq. (158); §9.4.3 eqs. (160)–(162); App. H §H.2 rows 0x56/0x57 p.35 and 0x5b p.36; sha256 pin `d67c009c…77fa9`. Row registration is L1's action; the peer says its row is round-61-authored with opened=2026-10-21, so Q01 is round-scoped, not seat-scoped. This seat has not confirmed the row in `corpus/SOURCES.md`, so Q01 stays open until it does.
- Trailer case: the paper's scan has no metadata or data-section carve-out. A boundary-aligned 0x5b in a metadata trailer is in the destination set by definition ([INFERENCE]). "Taken" remains unproven, so the entry must not label the trailer case as excluded.

## Limitations

- Seven authored inert fixtures; one provider version (evmole@0.9.3 via rea-agents@6.4.0). Scope is these bytes.
- No execution, no chain or RPC lookup, no ABI semantics. The `bytecode_offset` is the provider's
  destination field, not an opcode location.
- Saved records are compared by bytes and hash, not re-run (Q03/Q09).
- `verify_evm_evidence.py` checks r19 only (`verify_evm_evidence.py:10-11`).
- Scope boundary (peer ConnectorKasegiEvm note, corrected 2026-10-21): "A PUSH4 immediate followed by 0x14, 0x57 (JUMPI) and a 0x5b destination is the shape on which this family's only saved candidates occur (r19/r21/r22); it is not sufficient — r26 carries that shape with a valid JUMPDEST destination 17 and an empty saved record, so pattern-only (r25, r26) and pattern-plus-valid-JUMPDEST (r26) are both refuted and the acceptance rule is not established" — a candidate shape in a supplied byte string, read by linear sweep from the declared entry — not a deployed-contract function, ABI signature, reachability or claimability observation.
- Name the instruction-stream position, never the raw pattern: `63deadbeef14601057` is a dispatch-like instruction at evm-r19 offset 6 and inert inside a PUSH32 immediate at evm-r24 offset 1 (`executable_push4_count: 0`). Derivation (re-run 2026-10-21): `d[6:15]` and `r[1:10]` both equal `63deadbeef14601057` (True); `d[16]=0x5b`, `r[0]=127` (PUSH32).
- Deployed-bytecode identity, source pins and claimability are outside this entry.

## Reproduce

Step 1 (stdlib, read-only; run from the lane root):

```python
import hashlib
NAMES = {0x00:'STOP',0x14:'EQ',0x1c:'SHR',0x35:'CALLDATALOAD',0x50:'POP',0x57:'JUMPI',0x5b:'JUMPDEST',0x60:'PUSH1',0x63:'PUSH4',0x7f:'PUSH32',0x80:'DUP1'}
CASES = [('evm-r19','fixture.hex','hex'),('evm-r21','fixture.raw','raw'),('evm-r22','fixture.raw','raw'),('evm-r23','fixture.raw','raw'),('evm-r24','fixture.raw','raw'),('evm-r25','fixture.raw','raw'),('evm-r26','fixture.raw','raw')]
def decoded(path, enc):
    raw = open(path, 'rb').read()
    return bytes.fromhex(raw[2:-1].decode('ascii')) if enc == 'hex' else raw
def walk(d):
    out, i = [], 0
    while i < len(d):
        op = d[i]
        if 0x60 <= op <= 0x7f:
            n = op - 0x5f; out.append((i, f'PUSH{n}', d[i+1:i+1+n].hex())); i += 1 + n
        else:
            out.append((i, NAMES.get(op, f'0x{op:02x}'), '')); i += 1
    return out
for name, f, enc in CASES:
    raw = open(f'corpus/fixtures/{name}/{f}', 'rb').read()
    d = decoded(f'corpus/fixtures/{name}/{f}', enc)
    print(name, len(raw), hashlib.sha256(raw).hexdigest(), len(d), hashlib.sha256(d).hexdigest())
    print('  ', ' '.join(f'{o}:{n}' + (f'={im}' if im else '') for o, n, im in walk(d)))
```

Step 2 (saved record, read-only):

```python
import json
for r in (19, 21, 22, 23, 24, 25, 26):
    d = json.load(open(f'corpus/live/runs/round-{r}/inspection.json'))
    print(r, d['evidence_id'], d['raw_result']['functions'])
```

Step 3 (embedded-pattern check, r24):

```python
d = open('corpus/fixtures/evm-r24/fixture.raw', 'rb').read(); p = bytes.fromhex('63deadbeef14601057')
print([i for i in range(len(d)-len(p)+1) if d[i:i+len(p)] == p])
```

## Provenance (Q11, derived 2026-10-21 at lane base e0a4b0c)

- Step 1 output, sizes and digests (observed):
  - r19 `fixture.hex` 39 bytes `294e6fd2e041d5bea0558a26c1e399eddccf71bc0d279d398a4c0e915517b827`; decoded 18 bytes `d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723`
  - r21 `fixture.raw` 18 bytes `d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723`
  - r22 34 bytes `94c1790f966b78a9a5cc61bdc9ad4b805aaea6989e37773f66ff433deeb1dbe2`
  - r23 7 bytes `8047ddff11234c2d36bd134cfb4aec669efa3ff89ed35a922552d44ebfe22f5a`
  - r24 35 bytes `b69834e0ef786e3c001b2c833c8c0388acc017de14d06110cfa85d4948685d93`
  - r25 19 bytes `2d87a4e203ebf590beab57cf7318ccf93c92035d7929d0bc16e6850433f5e8f7`
  - r26 19 bytes `ebe2d6757a7acd4c5b9de82441f66e70561350267114e445a2d6b8d037f8e97d`
  - All seven equal the `truth.json` values (`carrier_sha256`/`decoded_sha256`, `raw_sha256`, `sha256`).
- Step 1 walk output (observed): r19 `0:PUSH1=00 2:CALLDATALOAD 3:PUSH1=e0 5:SHR 6:PUSH4=deadbeef 11:EQ 12:PUSH1=10 14:JUMPI 15:STOP 16:JUMPDEST 17:STOP`; r22 `… 30:JUMPDEST 31:STOP 32:JUMPDEST 33:STOP` with PUSH4 at 7 and 17; r25 `0:STOP … 7:PUSH4=deadbeef 12:EQ 13:PUSH1=10 15:JUMPI 16:STOP 17:JUMPDEST 18:STOP`; r26 as r25 with `13:PUSH1=11`.
- Step 2 output (observed): r19 `[{'selector': 'deadbeef', 'bytecodeOffset': 16, 'dispatch': 'abi', ...}]`; r23–r26 `[]`.
- Step 3 output (observed): `[1]`.
- Saved file digests (`sha256sum`): r19 `e892dd18ff219f71ce2644a3f5a3e3ad3479d2ca46df9e2a7c260e7b33f15948`; r22 `c55f69727ce2e62707ae0f9203c338efe57e6aeadc7fb5f5cd939bee3f9b3a33`; r21 `395c4f48e7efd7eafb07cc8c4b82c0fcea4e7a060885a97ee463da0faafdb7d7`. Digests cover these bytes only, not origin (Q09).

## QUALITY check

| Q | verdict | basis |
|---|---|---|
| Q01 | FAIL (pending) | No opened tier-A SOURCES row for opcode values or PUSH4/JUMPDEST rules; S### TBD |
| Q02 | pending | headers present; `S###` ids unfilled |
| Q03 | pass | expected values from bytes and `truth.json` (fixed by the author), not from the saved record |
| Q04 | pass | provider `evmole-interface`, version `evmole@0.9.3`, operation `inspect_evm_interface`; the walk is labelled manual |
| Q05 | n/a | no readiness or capability claim |
| Q06 | pass | every fixture re-derived by the walk on 2026-10-21 |
| Q07 | pass | r25/r26 empty results recorded; cause not stated |
| Q08 | pass | all counts/offsets re-derived by command |
| Q09 | pass | digests only for hashed bytes; record digests not claimed as origin |
| Q10 | pass | scoped to seven authored fixtures, one provider version |
| Q11 | pass | derivations and outputs inside the entry |

## Falsifiers (observed; not yet pre-registered)

- S-F1 (saved-record observation, 2026-10-21): naive 0x63 scan on r24 → false instruction at 1; record reports zero candidates.
- S-F2 (saved-record observation, 2026-10-21): r19 → r25 (prepend STOP) → one candidate becomes zero.
- S-F3 (saved-record observation, 2026-10-21): r25 → r26 (operand 0x10 → 0x11, reaching JUMPDEST) → still zero.
- S-F4 (saved-record observation, 2026-10-21): r22 → two candidates matching two PUSH4 immediates; a stronger mapping would be falsified by any mismatch.

## Hand-off (main agent)

- Run once after landing: `python3 -B` steps 1–3 of `## Reproduce` from the lane root (no verifier run here).
- Blockers to admission: the S### TBD rows (opcode spec, saved-record own-work row), and Q07 for r25/r26
  if the lane wants a prediction. Plus `truth.json` r24 offset `[1, 9]` (not edited).
- C1 count: C04 and C09 stay `uncovered` until a sourced entry passes Q01.
- PUSH4 (0x63) cannot rest on the Yellow Paper alone: the peer reports Appendix H elides that row. Peer-reported execution-specs row `SrcExecsSpecsOpcodes.md:62` (`instructions/__init__.py:125`) must be opened and merged before Q01 can pass for the selector claim. Not verified by this seat.
- Any C/L fact from `ExecEvmOracleR25` §5 is post hoc and must be labelled so; it is never the acceptance rule for this entry.

VERDICT: C09 draft is complete and byte-verified, but not admissible until a tier-A EVM opcode SOURCES row is opened; K_HELD stays 4/14 from this seat.
