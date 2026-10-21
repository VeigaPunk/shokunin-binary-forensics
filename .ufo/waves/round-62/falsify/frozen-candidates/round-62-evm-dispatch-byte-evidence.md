source: S028 (ethereum/execution-specs, tag v2.20.0, commit
2004296f2ffcbcebcd00f41152d33e8dfda0922a) — opcode byte values and the
valid-jump-destination scan, quoted below; S031 (this lane's own work — the seven
authored fixtures `corpus/fixtures/evm-r19`, `evm-r21`…`evm-r26` and the seven
saved `inspect_evm_interface` records `corpus/live/runs/round-19/inspection.json`
and `round-21`…`round-26`)
verified-at: 2026-10-21, lane base a3498e25ad87bf756288812d0ea7c474b09433c7; the
two specification files were read read-only at that tag on 2026-10-21 and the
fixtures/records were read from the lane tree at that base
recheck: save the `## Reproduce` block as `readout.py` and run
`python3 -B readout.py <archive-root>`; it reads the seven fixtures and the seven
saved records, executes no bytecode, opens no chain and calls no producer. The
`## Provenance` section is the exact stdout of the recorded run
coverage-map: C09
admission-status: candidate — round-62 build wave, not admitted. Admission
requires the fresh falsify wave and the L1 gate; nothing here flips a coverage
row, and no README target row is held by this file.

# EVM dispatch byte evidence on seven authored fixtures — derived bytes versus saved candidate fields

This entry compares two things kept apart everywhere below: the **authored
bytes** of seven inert fixture files, and the **saved candidate fields** in the
seven `inspect_evm_interface` records for those files. Every value in the prose
is a field of the printed output in `## Provenance`; the `## Evidence inventory`
table names that field for each claim. It is not a statement about deployed
contracts, any chain, the provider's internal method, present producer
capability, or the meaning of the `bytecodeOffset` field for any carrier other
than these seven files. No bytecode was executed, no chain or RPC was queried, no
producer was called, and no saved record was modified.

## Source facts (recorded)

Recorded from S028 at tag v2.20.0, commit
`2004296f2ffcbcebcd00f41152d33e8dfda0922a`, read read-only on 2026-10-21. These
are recorded source facts, not values this entry re-derives; the readout uses
them as constants and reads no specification file.

- `src/ethereum/forks/osaka/vm/instructions/__init__.py:55` `EQ = 0x14`; `:104` `STOP = 0x00`; `:106` `JUMPI = 0x57`; `:109` `JUMPDEST = 0x5B`; `:118` `POP = 0x50`; `:121` `PUSH0 = 0x5F`; `:122` `PUSH1 = 0x60`; `:125` `PUSH4 = 0x63`; `:153` `PUSH32 = 0x7F`
- `src/ethereum/forks/osaka/vm/runtime.py:22` — `def get_valid_jump_destinations(code: Bytes) -> Set[Uint]:`
- `src/ethereum/forks/osaka/vm/runtime.py:28` — `* The jump destination should have the `JUMPDEST` opcode (0x5B).`
- `src/ethereum/forks/osaka/vm/runtime.py:29-30` — `* The jump destination shouldn't be part of the data corresponding to` / `  `PUSH-N` opcodes.`
- `src/ethereum/forks/osaka/vm/runtime.py:64` — `push_data_size = current_opcode.value - Ops.PUSH1.value + 1`

## Observation

1. **Seven cases, and the counts kept apart.** `total_cases` is 7
   (`summary.total_cases`). The saved records report 4 candidate observations
   (`summary.reported_candidate_observations`: r19 one, r21 one, r22 two) over 3
   distinct `(selector, bytecode_offset)` pairs
   (`summary.distinct_candidate_pairs`, `summary.distinct_pairs`); the raw
   (upstream) and normalized lists carry the same pair counts
   (`summary.raw_and_normalized_pair_counts_equal`).

2. **Carrier bytes and decoded bytecode bytes are different strings, and each
   saved digest is labelled with the one it covers.** r19's carrier is a
   39-byte `0x`-prefixed ASCII hex file (`r19.carrier.bytes`,
   `r19.carrier.sha256`) and its decoded bytecode is 18 bytes
   (`r19.decoded.bytes`, `r19.decoded.sha256`); the subject and artifact
   digests cover the **carrier file** and the bytecode digest covers the
   **decoded bytes** (`r19.digest_scopes.subject`, `r19.digest_scopes.artifact`,
   `r19.digest_scopes.bytecode`). For r21 the carrier file *is* the raw
   bytecode, so all three digests name the same byte string
   (`r21.digest_scopes.subject`, `r21.carrier.sha256`).

3. **What each saved record records.** Each names its operation
   (`r19.recorded.operation`), provider id and version
   (`r19.recorded.provider_id`, `r19.recorded.provider_version`), evidence id
   (`r19.recorded.evidence_id`), `authority` and `confidence`
   (`r19.recorded.authority`, `r19.recorded.confidence`) and the three flags
   `evidence_kind`, `discovery_completeness`, `runtime_execution`
   (`r19.recorded.evidence_kind`, `r19.recorded.discovery_completeness`,
   `r19.recorded.runtime_execution`); the record file's own digest is
   `r19.record.sha256`. Those are **recorded** fields of the saved file: this
   entry does not authenticate them and claims no origin, completeness or
   authenticity from them.

4. **Instruction walk, JUMPDEST set and raw byte offsets.** For r19 the walk
   gives 11 instruction tuples of (offset, opcode, immediate bytes)
   (`r19.instructions`, `r19.instruction_opcode_counts`); the JUMPDEST set on
   instruction boundaries is `[16]` (`r19.valid_jumpdest_offsets`); the raw
   `0x63` byte offsets are `[6]` and the raw `0x5b` byte offsets are `[16]`
   (`r19.raw_0x63_offsets`, `r19.raw_0x5b_offsets`); the JUMPI at 14 is preceded
   by a PUSH1 whose operand byte is 16, in the JUMPDEST set
   (`r19.jumpi_with_preceding_push1`). r22's walk gives the JUMPDEST set
   `[30, 32]`, raw `0x63` offsets `[7, 17]` and raw `0x5b` offsets `[30, 32]`
   (`r22.valid_jumpdest_offsets`, `r22.raw_0x63_offsets`,
   `r22.raw_0x5b_offsets`), and its two reported pairs are
   `0xaaaaaaaa`@30 and `0xbbbbbbbb`@32 (`r22.candidate_pairs_normalized`).
   r23 has raw `0x63` offset `[0]` and an empty JUMPDEST set
   (`r23.raw_0x63_offsets`, `r23.valid_jumpdest_offsets`).

5. **The four records that report no pair.** r23, r24, r25 and r26 each carry
   an empty normalized pair list (`r23.candidate_pairs_normalized`,
   `r24.candidate_pairs_normalized`, `r25.candidate_pairs_normalized`,
   `r26.candidate_pairs_normalized`).

6. **r24 in full.** Its opcode counts are one `0x7f`, one `0x50` and one `0x00`
   (`r24.instruction_opcode_counts`), its JUMPDEST set is empty
   (`r24.valid_jumpdest_offsets`), its raw `0x63` offset is `[1]` and its raw
   `0x5b` offsets are empty (`r24.raw_0x63_offsets`, `r24.raw_0x5b_offsets`).
   The dispatch-like pattern — derived from the files' own bytes, from a PUSH4
   opcode through a JUMPI opcode inclusive — is `63deadbeef14601057`, 9 bytes
   (`summary.pattern_hex`); in r24 it occurs once, at start offset 1, so its
   inclusive span is 1-9 (`r24.pattern.occurrence_count`,
   `r24.pattern.occurrence_starts`, `r24.pattern.inclusive_spans`). Inside that
   occurrence the PUSH1 opcode byte is at offset 7 and its operand byte at
   offset 8 has value 16 (`r24.pattern.embedded_push1_opcode_offset`,
   `r24.pattern.embedded_push1_operand_offset`,
   `r24.pattern.embedded_push1_operand_value`); the byte at that operand's
   value, offset 16, is `0x00` and is not a raw `0x5b` byte
   (`r24.pattern.embedded_target_offset`, `r24.pattern.embedded_target_byte`,
   `r24.pattern.embedded_target_is_raw_0x5b`).

7. **r25 and r26, and what their JUMPI operands point at.** r25's JUMPI operand
   is 16, not in its JUMPDEST set `[17]` (`r25.jumpi_with_preceding_push1`,
   `r25.valid_jumpdest_offsets`); r26's is 17, in its JUMPDEST set `[17]`
   (`r26.jumpi_with_preceding_push1`, `r26.valid_jumpdest_offsets`). Both
   report no pair (`r25.candidate_pairs_normalized`,
   `r26.candidate_pairs_normalized`).

## Inference

- In each non-empty saved result in this sample (r19, r21, r22) the reported
  offset coincides with the operand of the PUSH1 that precedes a JUMPI, and the
  byte at that offset is `0x5b` on an instruction boundary
  (`r19.jumpi_with_preceding_push1`, `r22.jumpi_with_preceding_push1`). The
  other four records report no pair, so no offset is available there. This is an
  observation about these bytes; it is not a definition of the field for any
  other carrier, and it is not a claim that the field *is* a jump destination in
  general.
- The provider id, version, evidence id, authority and confidence are recorded
  fields of the saved files. A digest binds the bytes it hashed and nothing
  further: not provenance, acquisition completeness, producer origin or
  deployment authenticity; each record's own `kind`, `deployment_authenticity`
  and `hardfork` fields are `unknown` (`r19.recorded.bytecode.kind`).

## Unknown

- Why r23, r25 and r26 report no pair. This entry states the emptiness and the
  byte facts around it, proposes **no** rule that would produce it, and asserts no cause.
- Whether an empty pair list means the file has no callable interface: every
  record carries `discovery_completeness=unknown`
  (`r19.recorded.discovery_completeness`), so an empty list is not read as absence.
- The recorded `evidence_id` values (`r19.recorded.evidence_id`): this entry
  does not address, recompute or authenticate them and claims no formula for
  them, reading them as recorded identifiers only.
- The `dispatch`, argument and state-mutability labels in the saved records are
  the provider's own recorded values, not interpreted here.

- Compiled-bytecode behaviour — binary-search dispatch, PUSH2 destinations,
  short selector pushes, fallbacks, proxies, a compiler-appended metadata tail —
  is outside this entry's claim and is not examined here; whether the fixtures'
  selector constants correspond to any real function signature is not claimed.

## Limitations

- Seven authored fixtures, one recorded provider version, no rate or share
  quoted; no claim covers any carrier but these seven files.
- The provider id, version, evidence id, authority and confidence are recorded
  fields of the saved files, read here and not authenticated. `authority` is
  recorded and is **not read** as origin, custody or authenticity; identity in
  this entry is by digest (`r19.digest_scopes.subject`).
- **No verifier is credited as a guard for any value in this entry.**
  `corpus/verify_evm_evidence.py` is not cited as support, and every clause of
  this entry is unguarded by it: the carrier and decoded digests and their
  scopes, the instruction walk, the JUMPDEST set, the raw `0x63` and `0x5b`
  offsets, the r24 pattern occurrences, spans, embedded operand and target
  byte, the two candidate counts, and every inventory row. The block in
  `## Reproduce` is a manual comparison against the saved records; it is **not**
  claimed to be deletion-sensitive.
- The seven records and the seven fixtures were read only; no file under
  `corpus/fixtures/` or `corpus/live/` was modified, and the retained round-61
  rejected candidates were not edited.

## Cross-lane scope note (Q10)

The shipped-artifact reverse-engineering overlap between this lane and a
sibling lane is recorded as unresolved in this round's own intake and lesson
material — `corpus/lessons/round-62.md` ("ADJ-06 sibling arbitration … Operator-
owned and unresolved; new entries do not declare ownership or a ruling") and
`.ufo/waves/round-62/build/R62DebtExistingFiles.md` (section 4) — and this entry
declares no ownership and no ruling. It cites no sibling corpus file and reuses
no citation from the rejected round-61 candidate: the facts above come from
this entry's own readout.

## Q01-Q13 decisions (proposed by the author; not self-admission)

| Q | proposed | basis in this entry |
|---|---|---|
| Q01 | proposed pass, pending independent audit | Load-bearing claims rest on S028 (opcode byte assignments and static boundary scan, quoted under `## Source facts`, tier A only for that scope) and S031 (the authored fixture bytes and literal saved-record fields). Both opened rows are in `corpus/SOURCES.md`; no rejected row is cited. |
| Q02 | pass | `source:`, `verified-at:`, `recheck:` and `coverage-map: C09` headers are present. |
| Q03 | pass | Expected offsets and counts come from the byte walk; the saved records supply the reported fields, never the expected ones. The pattern is derived from the files' own bytes. |
| Q04 | pass | The only tool named is the provider, with its recorded id and version and its own explicit output fields; the walk is labeled manual. |
| Q05 | pass (past tense) | No current capability is claimed; the records were not re-run. |
| Q06 | pass | Every fixture premise is re-derived from the built bytes by the block in `## Reproduce`. |
| Q07 | pass | No cause is stated for any empty pair list and no rule is fitted to the seven outputs. |
| Q08 | superseded by Q11 | — |
| Q09 | pass | Each digest is labelled with the byte string it covers; no digest is offered as origin, completeness or authenticity. |
| Q10 | pass | Scoped to seven authored fixtures and one recorded provider version; the cross-lane question is reported, not decided. |
| Q11 | pass | Every claimed value is a field of the printed output, and `## Evidence inventory` names the field and the value for each claim. |
| Q12 | n/a | No rejected source row is cited as support. |
| Q13 | pass | No verifier is credited as a guard for any clause, and this entry's own block is not claimed to be deletion-sensitive (see `## Limitations`). |

These are the author's proposed readings of the criteria. They are not an
admission decision; admission belongs to the fresh falsify wave and the L1
gate, and this file asserts no admission.

## Evidence inventory

Each row names one claim, the output field that carries it, and that field's
value. A path is `case.field` for a case object or `summary.field` for the
summary object; both are lines of the `## Provenance` stdout.

| claim | output field | value |
|---|---|---|
| total cases | `summary.total_cases` | 7 |
| reported candidate observations (record x pair) | `summary.reported_candidate_observations` | 4 |
| distinct candidate pairs | `summary.distinct_candidate_pairs` | 3 |
| distinct pairs | `summary.distinct_pairs` | [["0xaaaaaaaa",30],["0xbbbbbbbb",32],["0xdeadbeef",16]] |
| raw and normalized pair counts equal | `summary.raw_and_normalized_pair_counts_equal` | true |
| pattern bytes and length | `summary.pattern_hex` | 63deadbeef14601057 |
| r19 carrier bytes | `r19.carrier.bytes` | 39 |
| r19 carrier sha256 | `r19.carrier.sha256` | 294e6fd2e041d5bea0558a26c1e399eddccf71bc0d279d398a4c0e915517b827 |
| r19 decoded bytes | `r19.decoded.bytes` | 18 |
| r19 decoded sha256 | `r19.decoded.sha256` | d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723 |
| r19 record file sha256 | `r19.record.sha256` | e892dd18ff219f71ce2644a3f5a3e3ad3479d2ca46df9e2a7c260e7b33f15948 |
| r19 subject digest scope | `r19.digest_scopes.subject` | carrier_file_bytes_only |
| r19 artifact digest scope | `r19.digest_scopes.artifact` | carrier_file_bytes_only |
| r19 bytecode digest scope | `r19.digest_scopes.bytecode` | decoded_bytecode_bytes_only |
| r19 operation | `r19.recorded.operation` | inspect_evm_interface |
| r19 provider id | `r19.recorded.provider_id` | evmole-interface |
| r19 provider version | `r19.recorded.provider_version` | evmole@0.9.3 |
| r19 evidence id | `r19.recorded.evidence_id` | ev_0ad0097eb137ff9196b29ac3fb6109d8f72ee0761e2655fa1fca594295cf6f42 |
| r19 authority | `r19.recorded.authority` | shipped-artifact |
| r19 confidence | `r19.recorded.confidence` | inferred |
| r19 evidence_kind | `r19.recorded.evidence_kind` | inferred |
| r19 discovery_completeness | `r19.recorded.discovery_completeness` | unknown |
| r19 runtime_execution | `r19.recorded.runtime_execution` | not-performed |
| r19 artifact bytes and encoding | `r19.recorded.artifact.bytes` | 39 |
| r19 bytecode bytes | `r19.recorded.bytecode.bytes` | 18 |
| r19 bytecode kind / authenticity / hardfork | `r19.recorded.bytecode.kind` | unknown |
| r19 instruction tuples (offset, opcode, immediate) | `r19.instructions` | [[0,96,"00"],[2,53,""],[3,96,"e0"],[5,28,""],[6,99,"deadbeef"],[11,20,""],[12,96,"10"],[14,87,""],[15,0,""],[16,91,""],[17,0,""]] |
| r19 instruction opcode counts | `r19.instruction_opcode_counts` | {"0x0":2,"0x14":1,"0x1c":1,"0x35":1,"0x57":1,"0x5b":1,"0x60":3,"0x63":1} |
| r19 valid JUMPDEST offsets | `r19.valid_jumpdest_offsets` | [16] |
| r19 raw 0x63 offsets | `r19.raw_0x63_offsets` | [6] |
| r19 raw 0x5b offsets | `r19.raw_0x5b_offsets` | [16] |
| r19 JUMPI with preceding PUSH1 (offset, operand, in dest set) | `r19.jumpi_with_preceding_push1` | [[14,16,true]] |
| r19 candidate pairs (normalized) | `r19.candidate_pairs_normalized` | [["0xdeadbeef",16]] |
| r19 candidate pairs (raw) | `r19.candidate_pairs_raw` | [["deadbeef",16]] |
| r21 carrier sha256 (= r19 decoded) | `r21.carrier.sha256` | d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723 |
| r21 subject digest scope | `r21.digest_scopes.subject` | carrier_and_decoded_same_byte_string |
| r21 candidate pairs (normalized) | `r21.candidate_pairs_normalized` | [["0xdeadbeef",16]] |
| r22 decoded sha256 | `r22.decoded.sha256` | 94c1790f966b78a9a5cc61bdc9ad4b805aaea6989e37773f66ff433deeb1dbe2 |
| r22 valid JUMPDEST offsets | `r22.valid_jumpdest_offsets` | [30,32] |
| r22 raw 0x63 offsets | `r22.raw_0x63_offsets` | [7,17] |
| r22 raw 0x5b offsets | `r22.raw_0x5b_offsets` | [30,32] |
| r22 candidate pairs (normalized) | `r22.candidate_pairs_normalized` | [["0xaaaaaaaa",30],["0xbbbbbbbb",32]] |
| r22 JUMPI with preceding PUSH1 | `r22.jumpi_with_preceding_push1` | [[15,30,true],[25,32,true]] |
| r23 raw 0x63 offsets | `r23.raw_0x63_offsets` | [0] |
| r23 valid JUMPDEST offsets | `r23.valid_jumpdest_offsets` | [] |
| r23 candidate pairs (normalized) | `r23.candidate_pairs_normalized` | [] |
| r24 decoded sha256 | `r24.decoded.sha256` | b69834e0ef786e3c001b2c833c8c0388acc017de14d06110cfa85d4948685d93 |
| r24 instruction opcode counts | `r24.instruction_opcode_counts` | {"0x0":1,"0x50":1,"0x7f":1} |
| r24 valid JUMPDEST offsets | `r24.valid_jumpdest_offsets` | [] |
| r24 raw 0x63 offsets | `r24.raw_0x63_offsets` | [1] |
| r24 raw 0x5b offsets | `r24.raw_0x5b_offsets` | [] |
| r24 pattern occurrence count | `r24.pattern.occurrence_count` | 1 |
| r24 pattern occurrence starts | `r24.pattern.occurrence_starts` | [1] |
| r24 pattern inclusive spans | `r24.pattern.inclusive_spans` | [[1,9]] |
| r24 embedded PUSH1 opcode offset | `r24.pattern.embedded_push1_opcode_offset` | 7 |
| r24 embedded PUSH1 operand offset | `r24.pattern.embedded_push1_operand_offset` | 8 |
| r24 embedded PUSH1 operand value | `r24.pattern.embedded_push1_operand_value` | 16 |
| r24 embedded target offset | `r24.pattern.embedded_target_offset` | 16 |
| r24 byte at embedded target | `r24.pattern.embedded_target_byte` | 0 |
| r24 embedded target is a raw 0x5b byte | `r24.pattern.embedded_target_is_raw_0x5b` | false |
| r24 candidate pairs (normalized) | `r24.candidate_pairs_normalized` | [] |
| r25 JUMPI with preceding PUSH1 | `r25.jumpi_with_preceding_push1` | [[15,16,false]] |
| r25 valid JUMPDEST offsets | `r25.valid_jumpdest_offsets` | [17] |
| r25 candidate pairs (normalized) | `r25.candidate_pairs_normalized` | [] |
| r26 JUMPI with preceding PUSH1 | `r26.jumpi_with_preceding_push1` | [[15,17,true]] |
| r26 valid JUMPDEST offsets | `r26.valid_jumpdest_offsets` | [17] |
| r26 candidate pairs (normalized) | `r26.candidate_pairs_normalized` | [] |

## Reproduce

Save this block as `readout.py` and run `python3 -B readout.py <archive-root>`.
It reads the seven fixtures and the seven saved records, executes no bytecode,
opens no chain, calls no producer, writes nothing; stdout is one JSON object
per case then one summary object.

```python
#!/usr/bin/env python3
"""Manual EVM byte/dispatch readout over seven authored fixtures and their saved
`inspect_evm_interface` records.  Usage: python3 -B readout.py <root>.  One JSON
object per case on stdout (one line each), then one summary object.  Read-only;
no bytecode, chain, RPC or producer; no file written; stdlib only."""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(sys.argv[1])
FIX = ROOT / "corpus" / "fixtures"
RUNS = ROOT / "corpus" / "live" / "runs"
CASES = [(19, "fixture.hex", "hex"), (21, "fixture.raw", "raw"), (22, "fixture.raw", "raw"),
         (23, "fixture.raw", "raw"), (24, "fixture.raw", "raw"), (25, "fixture.raw", "raw"),
         (26, "fixture.raw", "raw")]
# Opcode bytes and the PUSH-N rule are RECORDED from S028 (execution-specs tag v2.20.0,
# commit 2004296f2ffcbcebcd00f41152d33e8dfda0922a): instructions/__init__.py :55 EQ=0x14,
# :106 JUMPI=0x57, :109 JUMPDEST=0x5B, :125 PUSH4=0x63; runtime.py:22-69 get_valid_jump_destinations.
P1, P4, P32 = 0x60, 0x63, 0x7F
JUMPI, JD = 0x57, 0x5B
def sha(d):
    return hashlib.sha256(d).hexdigest()
def walk(code):
    """Instruction tuples (offset, opcode, immediate hex); PUSH-N immediates are skipped."""
    out, i = [], 0
    while i < len(code):
        op = code[i]
        n = op - 0x5F if P1 <= op <= P32 else 0
        out.append((i, op, code[i + 1:i + 1 + n].hex()))
        i += 1 + n
    return out
def referent(v, carrier, code):
    """Which exact byte string a saved digest covers."""
    if v == sha(carrier) == sha(code):
        return "carrier_and_decoded_same_byte_string"
    if v == sha(carrier):
        return "carrier_file_bytes_only"
    if v == sha(code):
        return "decoded_bytecode_bytes_only"
    return "no_local_byte_string"
def derive_pattern(code):
    """The dispatch-like pattern, from the file's own PUSH4..JUMPI bytes."""
    ins = walk(code)
    p4 = [i for i, op, _ in ins if op == P4]
    ji = [i for i, op, _ in ins if op == JUMPI]
    return code[p4[0]:ji[0] + 1] if p4 and ji else b""
def pattern_block(code, pattern):
    """Occurrences, inclusive spans, embedded PUSH1 operand and target byte."""
    starts, spans, i = [], [], code.find(pattern)
    while i != -1:
        starts.append(i)
        spans.append([i, i + len(pattern) - 1])
        i = code.find(pattern, i + 1)
    b = {"pattern_hex": pattern.hex(), "pattern_length": len(pattern),
         "occurrence_count": len(starts), "occurrence_starts": starts, "inclusive_spans": spans,
         "embedded_push1_opcode_offset": None, "embedded_push1_operand_offset": None,
         "embedded_push1_operand_value": None, "embedded_target_offset": None,
         "embedded_target_byte": None, "embedded_target_is_raw_0x5b": None}
    for s in starts:
        po = s + pattern.index(P1)
        oo, ov = po + 1, code[po + 1]
        tb = code[ov] if ov < len(code) else None
        b.update(embedded_push1_opcode_offset=po, embedded_push1_operand_offset=oo,
                 embedded_push1_operand_value=ov, embedded_target_offset=ov,
                 embedded_target_byte=tb, embedded_target_is_raw_0x5b=(tb == JD))
    return b

def main():
    r19 = (FIX / "evm-r19" / "fixture.hex").read_bytes()
    pattern = derive_pattern(bytes.fromhex(r19[2:-1].decode("ascii")))
    obs, pairs, same = 0, set(), True
    for r, name, enc in CASES:
        carrier = (FIX / ("evm-r%d" % r) / name).read_bytes()
        code = bytes.fromhex(carrier[2:-1].decode("ascii")) if enc == "hex" else carrier
        rb = (RUNS / ("round-%d" % r) / "inspection.json").read_bytes()
        rec = json.loads(rb.decode("utf-8"))
        nr = rec["normalized_result"]
        art, bc = nr["artifact"], nr["bytecode"]
        sub = rec["subject"]["digest"]["sha256"]
        ins = walk(code)
        jd = [i for i, op, _ in ins if op == JD]
        norm = [[f["selector"], f["bytecode_offset"]] for f in nr["functions"]]
        raw = [[f["selector"], f["bytecodeOffset"]] for f in rec["raw_result"].get("functions", [])]
        same = same and len(raw) == len(norm)
        obs += len(norm)
        pairs.update((s, o) for s, o in norm)
        ji = [[off, int(ins[k - 1][2], 16), int(ins[k - 1][2], 16) in jd]
              for k, (off, op, _) in enumerate(ins) if op == JUMPI and k and ins[k - 1][1] == P1]
        counts = {}
        for _, op, _ in ins:
            counts[hex(op)] = counts.get(hex(op), 0) + 1

        out = {"case": "r%d" % r,
               "carrier": {"file": "corpus/fixtures/evm-r%d/%s" % (r, name),
                           "bytes": len(carrier), "sha256": sha(carrier)},
               "decoded": {"bytes": len(code), "sha256": sha(code), "hex": code.hex()},
               "record": {"file": "corpus/live/runs/round-%d/inspection.json" % r,
                          "bytes": len(rb), "sha256": sha(rb)},
               "recorded": {
                   "operation": rec["operation"], "provider_id": rec["provider"]["id"],
                   "provider_name": rec["provider"]["name"], "authority": rec.get("authority"),
                   "provider_version": rec["provider"]["version"], "confidence": rec.get("confidence"),
                   "evidence_id": rec["evidence_id"], "predicate_type": rec.get("predicate_type"),
                   "evidence_kind": nr["evidence_kind"], "runtime_execution": nr["runtime_execution"],
                   "discovery_completeness": nr["discovery_completeness"],
                   "artifact": {"sha256": art["sha256"], "bytes": art["bytes"], "encoding": art["encoding"]},
                   "bytecode": {"sha256": bc["sha256"], "bytes": bc["bytes"], "hex": bc["hex"],
                                "digest_algorithm": bc["digest_algorithm"], "kind": bc["kind"],
                                "hardfork": bc["hardfork"],
                                "deployment_authenticity": bc["deployment_authenticity"]}},
               "digest_scopes": {"subject": referent(sub, carrier, code),
                                 "artifact": referent(art["sha256"], carrier, code),
                                 "bytecode": referent(bc["sha256"], carrier, code)},
               "instructions": [[i, op, h] for i, op, h in ins],
               "instruction_opcode_counts": counts, "valid_jumpdest_offsets": jd,
               "raw_0x63_offsets": [i for i, b in enumerate(code) if b == P4],
               "raw_0x5b_offsets": [i for i, b in enumerate(code) if b == JD],
               "jumpi_with_preceding_push1": ji, "candidate_pairs_normalized": norm,
               "candidate_pairs_raw": raw, "pattern": pattern_block(code, pattern)}

        print(json.dumps(out, sort_keys=True, separators=(",", ":")))
    print(json.dumps({"total_cases": len(CASES), "reported_candidate_observations": obs,
                      "distinct_candidate_pairs": len(pairs), "distinct_pairs": sorted(list(pairs)),
                      "raw_and_normalized_pair_counts_equal": same,
                      "pattern_hex": pattern.hex(), "pattern_length": len(pattern)},
                     sort_keys=True, separators=(",", ":")))
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

## Provenance

Recorded run: 2026-10-21, lane base `a3498e25ad87bf756288812d0ea7c474b09433c7`,
Python 3.14.8, cwd `/`, lane tree extracted read-only with `git -C
…/revenger-shokunin archive a3498e25…`; `readout.py` exited 0, stderr empty.
The output below is exact, complete and untruncated; every digest is full
length.

Command:

```text
python3 -B readout.py <archive-root>    # exit 0, stderr empty
```

Exact stdout of `readout.py`:

```text
{"candidate_pairs_normalized":[["0xdeadbeef",16]],"candidate_pairs_raw":[["deadbeef",16]],"carrier":{"bytes":39,"file":"corpus/fixtures/evm-r19/fixture.hex","sha256":"294e6fd2e041d5bea0558a26c1e399eddccf71bc0d279d398a4c0e915517b827"},"case":"r19","decoded":{"bytes":18,"hex":"60003560e01c63deadbeef14601057005b00","sha256":"d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723"},"digest_scopes":{"artifact":"carrier_file_bytes_only","bytecode":"decoded_bytecode_bytes_only","subject":"carrier_file_bytes_only"},"instruction_opcode_counts":{"0x0":2,"0x14":1,"0x1c":1,"0x35":1,"0x57":1,"0x5b":1,"0x60":3,"0x63":1},"instructions":[[0,96,"00"],[2,53,""],[3,96,"e0"],[5,28,""],[6,99,"deadbeef"],[11,20,""],[12,96,"10"],[14,87,""],[15,0,""],[16,91,""],[17,0,""]],"jumpi_with_preceding_push1":[[14,16,true]],"pattern":{"embedded_push1_opcode_offset":12,"embedded_push1_operand_offset":13,"embedded_push1_operand_value":16,"embedded_target_byte":91,"embedded_target_is_raw_0x5b":true,"embedded_target_offset":16,"inclusive_spans":[[6,14]],"occurrence_count":1,"occurrence_starts":[6],"pattern_hex":"63deadbeef14601057","pattern_length":9},"raw_0x5b_offsets":[16],"raw_0x63_offsets":[6],"record":{"bytes":4175,"file":"corpus/live/runs/round-19/inspection.json","sha256":"e892dd18ff219f71ce2644a3f5a3e3ad3479d2ca46df9e2a7c260e7b33f15948"},"recorded":{"artifact":{"bytes":39,"encoding":"hex","sha256":"294e6fd2e041d5bea0558a26c1e399eddccf71bc0d279d398a4c0e915517b827"},"authority":"shipped-artifact","bytecode":{"bytes":18,"deployment_authenticity":"unknown","digest_algorithm":"sha256","hardfork":"unknown","hex":"60003560e01c63deadbeef14601057005b00","kind":"unknown","sha256":"d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723"},"confidence":"inferred","discovery_completeness":"unknown","evidence_id":"ev_0ad0097eb137ff9196b29ac3fb6109d8f72ee0761e2655fa1fca594295cf6f42","evidence_kind":"inferred","operation":"inspect_evm_interface","predicate_type":"rea.analysis","provider_id":"evmole-interface","provider_name":"REA EVM interface adapter","provider_version":"evmole@0.9.3","runtime_execution":"not-performed"},"valid_jumpdest_offsets":[16]}
{"candidate_pairs_normalized":[["0xdeadbeef",16]],"candidate_pairs_raw":[["deadbeef",16]],"carrier":{"bytes":18,"file":"corpus/fixtures/evm-r21/fixture.raw","sha256":"d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723"},"case":"r21","decoded":{"bytes":18,"hex":"60003560e01c63deadbeef14601057005b00","sha256":"d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723"},"digest_scopes":{"artifact":"carrier_and_decoded_same_byte_string","bytecode":"carrier_and_decoded_same_byte_string","subject":"carrier_and_decoded_same_byte_string"},"instruction_opcode_counts":{"0x0":2,"0x14":1,"0x1c":1,"0x35":1,"0x57":1,"0x5b":1,"0x60":3,"0x63":1},"instructions":[[0,96,"00"],[2,53,""],[3,96,"e0"],[5,28,""],[6,99,"deadbeef"],[11,20,""],[12,96,"10"],[14,87,""],[15,0,""],[16,91,""],[17,0,""]],"jumpi_with_preceding_push1":[[14,16,true]],"pattern":{"embedded_push1_opcode_offset":12,"embedded_push1_operand_offset":13,"embedded_push1_operand_value":16,"embedded_target_byte":91,"embedded_target_is_raw_0x5b":true,"embedded_target_offset":16,"inclusive_spans":[[6,14]],"occurrence_count":1,"occurrence_starts":[6],"pattern_hex":"63deadbeef14601057","pattern_length":9},"raw_0x5b_offsets":[16],"raw_0x63_offsets":[6],"record":{"bytes":4175,"file":"corpus/live/runs/round-21/inspection.json","sha256":"395c4f48e7efd7eafb07cc8c4b82c0fcea4e7a060885a97ee463da0faafdb7d7"},"recorded":{"artifact":{"bytes":18,"encoding":"raw","sha256":"d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723"},"authority":"shipped-artifact","bytecode":{"bytes":18,"deployment_authenticity":"unknown","digest_algorithm":"sha256","hardfork":"unknown","hex":"60003560e01c63deadbeef14601057005b00","kind":"unknown","sha256":"d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723"},"confidence":"inferred","discovery_completeness":"unknown","evidence_id":"ev_4810eda7b540fbf2d4265c0f9deb3886dc009945cb77276b980f5502112cfc85","evidence_kind":"inferred","operation":"inspect_evm_interface","predicate_type":"rea.analysis","provider_id":"evmole-interface","provider_name":"REA EVM interface adapter","provider_version":"evmole@0.9.3","runtime_execution":"not-performed"},"valid_jumpdest_offsets":[16]}
{"candidate_pairs_normalized":[["0xaaaaaaaa",30],["0xbbbbbbbb",32]],"candidate_pairs_raw":[["aaaaaaaa",30],["bbbbbbbb",32]],"carrier":{"bytes":34,"file":"corpus/fixtures/evm-r22/fixture.raw","sha256":"94c1790f966b78a9a5cc61bdc9ad4b805aaea6989e37773f66ff433deeb1dbe2"},"case":"r22","decoded":{"bytes":34,"hex":"60003560e01c8063aaaaaaaa14601e578063bbbbbbbb14602057000000005b005b00","sha256":"94c1790f966b78a9a5cc61bdc9ad4b805aaea6989e37773f66ff433deeb1dbe2"},"digest_scopes":{"artifact":"carrier_and_decoded_same_byte_string","bytecode":"carrier_and_decoded_same_byte_string","subject":"carrier_and_decoded_same_byte_string"},"instruction_opcode_counts":{"0x0":6,"0x14":2,"0x1c":1,"0x35":1,"0x57":2,"0x5b":2,"0x60":4,"0x63":2,"0x80":2},"instructions":[[0,96,"00"],[2,53,""],[3,96,"e0"],[5,28,""],[6,128,""],[7,99,"aaaaaaaa"],[12,20,""],[13,96,"1e"],[15,87,""],[16,128,""],[17,99,"bbbbbbbb"],[22,20,""],[23,96,"20"],[25,87,""],[26,0,""],[27,0,""],[28,0,""],[29,0,""],[30,91,""],[31,0,""],[32,91,""],[33,0,""]],"jumpi_with_preceding_push1":[[15,30,true],[25,32,true]],"pattern":{"embedded_push1_opcode_offset":null,"embedded_push1_operand_offset":null,"embedded_push1_operand_value":null,"embedded_target_byte":null,"embedded_target_is_raw_0x5b":null,"embedded_target_offset":null,"inclusive_spans":[],"occurrence_count":0,"occurrence_starts":[],"pattern_hex":"63deadbeef14601057","pattern_length":9},"raw_0x5b_offsets":[30,32],"raw_0x63_offsets":[7,17],"record":{"bytes":4437,"file":"corpus/live/runs/round-22/inspection.json","sha256":"c55f69727ce2e62707ae0f9203c338efe57e6aeadc7fb5f5cd939bee3f9b3a33"},"recorded":{"artifact":{"bytes":34,"encoding":"raw","sha256":"94c1790f966b78a9a5cc61bdc9ad4b805aaea6989e37773f66ff433deeb1dbe2"},"authority":"shipped-artifact","bytecode":{"bytes":34,"deployment_authenticity":"unknown","digest_algorithm":"sha256","hardfork":"unknown","hex":"60003560e01c8063aaaaaaaa14601e578063bbbbbbbb14602057000000005b005b00","kind":"unknown","sha256":"94c1790f966b78a9a5cc61bdc9ad4b805aaea6989e37773f66ff433deeb1dbe2"},"confidence":"inferred","discovery_completeness":"unknown","evidence_id":"ev_24fe0001213ec58a588d086e0fe55677d749f3eb6998afe6ee6095ff9dc4af4b","evidence_kind":"inferred","operation":"inspect_evm_interface","predicate_type":"rea.analysis","provider_id":"evmole-interface","provider_name":"REA EVM interface adapter","provider_version":"evmole@0.9.3","runtime_execution":"not-performed"},"valid_jumpdest_offsets":[30,32]}
{"candidate_pairs_normalized":[],"candidate_pairs_raw":[],"carrier":{"bytes":7,"file":"corpus/fixtures/evm-r23/fixture.raw","sha256":"8047ddff11234c2d36bd134cfb4aec669efa3ff89ed35a922552d44ebfe22f5a"},"case":"r23","decoded":{"bytes":7,"hex":"63c0ffee005000","sha256":"8047ddff11234c2d36bd134cfb4aec669efa3ff89ed35a922552d44ebfe22f5a"},"digest_scopes":{"artifact":"carrier_and_decoded_same_byte_string","bytecode":"carrier_and_decoded_same_byte_string","subject":"carrier_and_decoded_same_byte_string"},"instruction_opcode_counts":{"0x0":1,"0x50":1,"0x63":1},"instructions":[[0,99,"c0ffee00"],[5,80,""],[6,0,""]],"jumpi_with_preceding_push1":[],"pattern":{"embedded_push1_opcode_offset":null,"embedded_push1_operand_offset":null,"embedded_push1_operand_value":null,"embedded_target_byte":null,"embedded_target_is_raw_0x5b":null,"embedded_target_offset":null,"inclusive_spans":[],"occurrence_count":0,"occurrence_starts":[],"pattern_hex":"63deadbeef14601057","pattern_length":9},"raw_0x5b_offsets":[],"raw_0x63_offsets":[0],"record":{"bytes":3923,"file":"corpus/live/runs/round-23/inspection.json","sha256":"ce9fe51536af461ef2deb19b8cf8ff3582dba736abc2747b07ab845d3aaac2af"},"recorded":{"artifact":{"bytes":7,"encoding":"raw","sha256":"8047ddff11234c2d36bd134cfb4aec669efa3ff89ed35a922552d44ebfe22f5a"},"authority":"shipped-artifact","bytecode":{"bytes":7,"deployment_authenticity":"unknown","digest_algorithm":"sha256","hardfork":"unknown","hex":"63c0ffee005000","kind":"unknown","sha256":"8047ddff11234c2d36bd134cfb4aec669efa3ff89ed35a922552d44ebfe22f5a"},"confidence":"inferred","discovery_completeness":"unknown","evidence_id":"ev_296e7ed723c7356b1cfbeee5dadc11283e5efe74535d544114ebf3b692f77201","evidence_kind":"inferred","operation":"inspect_evm_interface","predicate_type":"rea.analysis","provider_id":"evmole-interface","provider_name":"REA EVM interface adapter","provider_version":"evmole@0.9.3","runtime_execution":"not-performed"},"valid_jumpdest_offsets":[]}
{"candidate_pairs_normalized":[],"candidate_pairs_raw":[],"carrier":{"bytes":35,"file":"corpus/fixtures/evm-r24/fixture.raw","sha256":"b69834e0ef786e3c001b2c833c8c0388acc017de14d06110cfa85d4948685d93"},"case":"r24","decoded":{"bytes":35,"hex":"7f63deadbeef1460105700000000000000000000000000000000000000000000005000","sha256":"b69834e0ef786e3c001b2c833c8c0388acc017de14d06110cfa85d4948685d93"},"digest_scopes":{"artifact":"carrier_and_decoded_same_byte_string","bytecode":"carrier_and_decoded_same_byte_string","subject":"carrier_and_decoded_same_byte_string"},"instruction_opcode_counts":{"0x0":1,"0x50":1,"0x7f":1},"instructions":[[0,127,"63deadbeef146010570000000000000000000000000000000000000000000000"],[33,80,""],[34,0,""]],"jumpi_with_preceding_push1":[],"pattern":{"embedded_push1_opcode_offset":7,"embedded_push1_operand_offset":8,"embedded_push1_operand_value":16,"embedded_target_byte":0,"embedded_target_is_raw_0x5b":false,"embedded_target_offset":16,"inclusive_spans":[[1,9]],"occurrence_count":1,"occurrence_starts":[1],"pattern_hex":"63deadbeef14601057","pattern_length":9},"raw_0x5b_offsets":[],"raw_0x63_offsets":[1],"record":{"bytes":3981,"file":"corpus/live/runs/round-24/inspection.json","sha256":"ec9e147db2b042f4d991816fa2a02fe95373de31956730fd1eb4cce5763742cd"},"recorded":{"artifact":{"bytes":35,"encoding":"raw","sha256":"b69834e0ef786e3c001b2c833c8c0388acc017de14d06110cfa85d4948685d93"},"authority":"shipped-artifact","bytecode":{"bytes":35,"deployment_authenticity":"unknown","digest_algorithm":"sha256","hardfork":"unknown","hex":"7f63deadbeef1460105700000000000000000000000000000000000000000000005000","kind":"unknown","sha256":"b69834e0ef786e3c001b2c833c8c0388acc017de14d06110cfa85d4948685d93"},"confidence":"inferred","discovery_completeness":"unknown","evidence_id":"ev_50d5ffb1fdbd17c4896409ca4cc8b20d7ed344ef4011029bea4aa474b7f0ab9e","evidence_kind":"inferred","operation":"inspect_evm_interface","predicate_type":"rea.analysis","provider_id":"evmole-interface","provider_name":"REA EVM interface adapter","provider_version":"evmole@0.9.3","runtime_execution":"not-performed"},"valid_jumpdest_offsets":[]}
{"candidate_pairs_normalized":[],"candidate_pairs_raw":[],"carrier":{"bytes":19,"file":"corpus/fixtures/evm-r25/fixture.raw","sha256":"2d87a4e203ebf590beab57cf7318ccf93c92035d7929d0bc16e6850433f5e8f7"},"case":"r25","decoded":{"bytes":19,"hex":"0060003560e01c63deadbeef14601057005b00","sha256":"2d87a4e203ebf590beab57cf7318ccf93c92035d7929d0bc16e6850433f5e8f7"},"digest_scopes":{"artifact":"carrier_and_decoded_same_byte_string","bytecode":"carrier_and_decoded_same_byte_string","subject":"carrier_and_decoded_same_byte_string"},"instruction_opcode_counts":{"0x0":3,"0x14":1,"0x1c":1,"0x35":1,"0x57":1,"0x5b":1,"0x60":3,"0x63":1},"instructions":[[0,0,""],[1,96,"00"],[3,53,""],[4,96,"e0"],[6,28,""],[7,99,"deadbeef"],[12,20,""],[13,96,"10"],[15,87,""],[16,0,""],[17,91,""],[18,0,""]],"jumpi_with_preceding_push1":[[15,16,false]],"pattern":{"embedded_push1_opcode_offset":13,"embedded_push1_operand_offset":14,"embedded_push1_operand_value":16,"embedded_target_byte":0,"embedded_target_is_raw_0x5b":false,"embedded_target_offset":16,"inclusive_spans":[[7,15]],"occurrence_count":1,"occurrence_starts":[7],"pattern_hex":"63deadbeef14601057","pattern_length":9},"raw_0x5b_offsets":[17],"raw_0x63_offsets":[7],"record":{"bytes":3949,"file":"corpus/live/runs/round-25/inspection.json","sha256":"4f677a209d08c3f9e531191aea9cdc58533898b9f9ed2394b3db63a0b8d448cf"},"recorded":{"artifact":{"bytes":19,"encoding":"raw","sha256":"2d87a4e203ebf590beab57cf7318ccf93c92035d7929d0bc16e6850433f5e8f7"},"authority":"shipped-artifact","bytecode":{"bytes":19,"deployment_authenticity":"unknown","digest_algorithm":"sha256","hardfork":"unknown","hex":"0060003560e01c63deadbeef14601057005b00","kind":"unknown","sha256":"2d87a4e203ebf590beab57cf7318ccf93c92035d7929d0bc16e6850433f5e8f7"},"confidence":"inferred","discovery_completeness":"unknown","evidence_id":"ev_23a9464bf2d8c3de3614176efa53016f002ddade19f1ae842b4325ba2d095579","evidence_kind":"inferred","operation":"inspect_evm_interface","predicate_type":"rea.analysis","provider_id":"evmole-interface","provider_name":"REA EVM interface adapter","provider_version":"evmole@0.9.3","runtime_execution":"not-performed"},"valid_jumpdest_offsets":[17]}
{"candidate_pairs_normalized":[],"candidate_pairs_raw":[],"carrier":{"bytes":19,"file":"corpus/fixtures/evm-r26/fixture.raw","sha256":"ebe2d6757a7acd4c5b9de82441f66e70561350267114e445a2d6b8d037f8e97d"},"case":"r26","decoded":{"bytes":19,"hex":"0060003560e01c63deadbeef14601157005b00","sha256":"ebe2d6757a7acd4c5b9de82441f66e70561350267114e445a2d6b8d037f8e97d"},"digest_scopes":{"artifact":"carrier_and_decoded_same_byte_string","bytecode":"carrier_and_decoded_same_byte_string","subject":"carrier_and_decoded_same_byte_string"},"instruction_opcode_counts":{"0x0":3,"0x14":1,"0x1c":1,"0x35":1,"0x57":1,"0x5b":1,"0x60":3,"0x63":1},"instructions":[[0,0,""],[1,96,"00"],[3,53,""],[4,96,"e0"],[6,28,""],[7,99,"deadbeef"],[12,20,""],[13,96,"11"],[15,87,""],[16,0,""],[17,91,""],[18,0,""]],"jumpi_with_preceding_push1":[[15,17,true]],"pattern":{"embedded_push1_opcode_offset":null,"embedded_push1_operand_offset":null,"embedded_push1_operand_value":null,"embedded_target_byte":null,"embedded_target_is_raw_0x5b":null,"embedded_target_offset":null,"inclusive_spans":[],"occurrence_count":0,"occurrence_starts":[],"pattern_hex":"63deadbeef14601057","pattern_length":9},"raw_0x5b_offsets":[17],"raw_0x63_offsets":[7],"record":{"bytes":3949,"file":"corpus/live/runs/round-26/inspection.json","sha256":"bf2b2337b83f694ff9c7f9dfafbd9074de9b3310c52609fb41c993d9c782fc3c"},"recorded":{"artifact":{"bytes":19,"encoding":"raw","sha256":"ebe2d6757a7acd4c5b9de82441f66e70561350267114e445a2d6b8d037f8e97d"},"authority":"shipped-artifact","bytecode":{"bytes":19,"deployment_authenticity":"unknown","digest_algorithm":"sha256","hardfork":"unknown","hex":"0060003560e01c63deadbeef14601157005b00","kind":"unknown","sha256":"ebe2d6757a7acd4c5b9de82441f66e70561350267114e445a2d6b8d037f8e97d"},"confidence":"inferred","discovery_completeness":"unknown","evidence_id":"ev_482e41e68b6c5f358fe660bc70eaf55f69c7b487fd61774e1a443571aecec090","evidence_kind":"inferred","operation":"inspect_evm_interface","predicate_type":"rea.analysis","provider_id":"evmole-interface","provider_name":"REA EVM interface adapter","provider_version":"evmole@0.9.3","runtime_execution":"not-performed"},"valid_jumpdest_offsets":[17]}
{"distinct_candidate_pairs":3,"distinct_pairs":[["0xaaaaaaaa",30],["0xbbbbbbbb",32],["0xdeadbeef",16]],"pattern_hex":"63deadbeef14601057","pattern_length":9,"raw_and_normalized_pair_counts_equal":true,"reported_candidate_observations":4,"total_cases":7}
```
