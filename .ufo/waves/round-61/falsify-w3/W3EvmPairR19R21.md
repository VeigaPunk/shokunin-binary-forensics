GRADE: HOLDS — C09 Observation 2 (r19/r21 hypothesis) at landed ab580698
Seat RevengerR61-2.W3EvmPairR19R21. Archive ab580698212258a55e43e9bb9bf6ac78c91eae2a (rev-parse checked), extracted to /tmp/revenger-r61w3-W3EvmPairR19R21. Static only: no EVM execution, no REA call, no chain. Scratch: /tmp/revenger-r61w3-W3EvmPairR19R21-work/{walker.py,xcheck_pyevmasm.py,entry_reproduce.py}.

## Method
- Own walker (scratch walker.py): linear sweep plus bounded abstract stack walk (PUSH, CALLDATALOAD, SHR, EQ, JUMPI, DUP, SWAP, POP). Not the entry's code.
- pyevmasm 0.2.3 via `uv run --no-project --with pyevmasm` (uv 0.13.0; PyPI). Its pcs match the walker: 0,2,3,5,6,11,12,14,15,16,17.
- The entry's `## Reproduce` run from the archive root: stdout equals `## Provenance` exactly (exit 0).
- `git diff --stat e0a4b0c… ab580698… -- corpus/fixtures corpus/live/runs` is empty: fixtures and saved records unchanged since base.

## Sub-claims (entry lines 25-31; offsets are decoded bytes)
| Sub-claim | Verdict | Evidence |
|---|---|---|
| hex carrier decodes to the raw r21 bytes | HOLDS | carrier 39 B sha 294e6fd2…; decoded 18 B sha d1086bce… = fixture.raw |
| exactly one function per record | HOLDS | r19 and r21: raw_result and normalized_result functions each length 1 |
| selector 0xdeadbeef | HOLDS | normalized `0xdeadbeef`, raw `deadbeef`; PUSH4 immediate at 7-10 = de ad be ef |
| bytecode_offset 16 | HOLDS | raw `bytecodeOffset` 16, normalized `bytecode_offset` 16 |
| PUSH4 at 6 | HOLDS | only 0x63 byte is pc 6 (sweep and raw scan); pyevmasm (6, PUSH4, 5) |
| 16 is a JUMPDEST on an instruction boundary | HOLDS | sweep JUMPDEST [16]; raw 0x5b [16]; not inside push data; pyevmasm (16, JUMPDEST, 1) |
| 16 reached via the PUSH1 operand of a JUMPI | HOLDS | JUMPI@14, immediate predecessor PUSH1 0x10 (pc 12, operand 13); abstract dest 0x10 valid; cond EQ(0xdeadbeef,SHR(0xe0,calldata[0x0])); jump edge 14->16 |
| no record field holds a PUSH4 location | HOLDS | int-valued fields: bytes 39/18 and bytecode offset 16 only; no pc, push, jump or opcode keys |

## Attacks that did not break it
A. Rival meanings of 16. In r19/r21, 16 also equals the PUSH1 operand value, EQ+5, PUSH4+10, JUMPI+2, fallthrough+1 and the end of the STOP-terminated block after the dispatch, so these two records cannot separate them. r22 can (offsets 30/32, JUMPIs at 15/25, PUSH1 operands 0x1e/0x20, JUMPDESTs at 30/32): EQ+5, PUSH4+10, JUMPI+2 and fallthrough+1 all give 17, and end-of-block gives 27. Only the taken JUMPI target survives.
B. Upstream, evmole 0.9.3 `evmole.pyi` (https://raw.githubusercontent.com/cdump/evmole/0.9.3/evmole.pyi, accessed 2026-10-21): "Starting byte offset within the EVM bytecode for the function body." Consistent with the Inference (lines 49-52); the entry cites no upstream definition. The record's "terminal metadata" limitation maps to `Contract.metadata` ("Terminal CBOR metadata"), which these fixtures lack; it is not a PUSH4 source.
C. Validity of 16 does not depend on the PUSH-data rule: the only 0x5b byte is pc 16, outside every immediate, so naive scan and sweep agree. r19/r21 do not exercise that clause (r24 does).

## Findings (PARTIAL; none breaks the hypothesis)
P1. Observation 4, line 40 ("each record's subject digest equals the fixture bytes' SHA-256") holds for r19 only with the 39-byte carrier: r19 subject.digest.sha256 = 294e6fd2…. Provenance line 146 prints r19 `sha256=d1086bce…` (decoded). Reproduce line 137 tests `in (sha(raw), sha(d))`, so `subject_eq_bytes=True` (line 147) cannot show which identity matched.
P2. Adjacent, outside the entry: round-21/LEDGER.md:5 calls "PUSH4 opcode offset 6 and immediate 7-10" fixture truth. r21 truth.json keys are destination_offset, note, raw_bytes, raw_sha256, selector, source_hex_fixture; the PUSH4 keys (push4_opcode_offset 6, selector_immediate_offset 7, length 4) exist only in r19 truth.json.
P3. Scope note, not a defect: line 28 "the offset is the PUSH1 operand" is a value identity (16 = 0x10); the semantic reading sits in ## Inference and is labeled.

## Census (Observation 4 context)
Rounds 19 and 21-26: all seven inferred / unknown / not-performed; subject is the carrier only for r19.

Installs: pyevmasm 0.2.3 via uv run (uv cache). None other.
Not relied on: sibling reports under .ufo/waves/round-61 (grep hits only); a third-party web summary from search.
VERDICT: Observation 2 holds for r19/r21 on all eight sub-claims; defects are P1 (subject-digest check, lines 40/137) and the adjacent P2 (r21 ledger line 5).
