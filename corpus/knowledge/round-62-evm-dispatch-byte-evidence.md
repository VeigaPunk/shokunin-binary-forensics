source: S028 — https://github.com/ethereum/execution-specs/tree/v2.20.0/src/ethereum/forks/osaka/vm
(tag v2.20.0, commit 2004296f2ffcbcebcd00f41152d33e8dfda0922a) — opcode byte
values and the valid-jump-destination scan, at
`src/ethereum/forks/osaka/vm/instructions/__init__.py` lines 55, 104, 106, 109,
118, 121, 122, 125, 153 and `src/ethereum/forks/osaka/vm/runtime.py` lines 22, 28,
29-30, 64, quoted under `## Source facts`; S031 (this lane's own work — the seven
authored fixtures `corpus/fixtures/evm-r19`, `evm-r21`…`evm-r26` and their
decoded bytes); S026 (the seven saved `inspect_evm_interface` records
`corpus/live/runs/round-19/inspection.json` and `round-21`…`round-26`, reopened
independently for this entry — the recorded metadata and identifiers below are
that row's scope, not S031's)
verified-at: 2026-10-21, lane base a3498e25ad87bf756288812d0ea7c474b09433c7; the
tag, commit, file paths and line anchors above are recorded source facts read
read-only on 2026-10-21, and the fixtures/records were read from the lane tree
at that base
recheck: save the `## Reproduce` block as `readout.py` and run
`python3 -B readout.py <archive-root>`; it reads the seven fixtures and the seven
saved records, executes no bytecode, opens no chain and calls no producer. The
`## Provenance` section is the exact stdout of the recorded run
coverage-map: C09
admission-status: admitted — recorded round-62 Gate decision in
`corpus/lessons/round-62.md`; the evidence body passed exact-hash fresh
reviews before the README coverage transition.

# EVM dispatch byte evidence on seven authored fixtures — derived bytes versus saved candidate fields

This entry compares two things kept apart everywhere below: the **authored
bytes** of seven fixture files, and the **saved candidate fields** in the seven
`inspect_evm_interface` records for those files. Each byte/record value asserted
as derived is printed in `## Provenance` and mapped by `## Evidence inventory`;
specification facts and run metadata are explicitly labeled recorded. It is not a statement about deployed contracts,
any chain, the provider's internal method, present producer capability, or the
meaning of the `bytecodeOffset` field for any carrier other than these seven
files. No bytecode was executed, no chain or RPC was queried, no producer was
called, and no saved record was modified.

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

1. **Seven cases; the counts kept apart.** `total_cases` 7
   (`summary.total_cases`); 4 reported candidate observations — r19 one, r21 one,
   r22 two (`summary.reported_candidate_observations`) — over 3 distinct
   `(selector, bytecode_offset)` pairs (`summary.distinct_candidate_pairs`,
   `summary.distinct_pairs`); the raw and normalized function lists carry the
   same pair counts (`summary.raw_and_normalized_pair_counts_equal`).

2. **The carrier's own bytes decide how it is decoded.** r19's carrier is
   classified `ascii_hex_text` (`r19.carrier.carrier_form`), prefix bytes
   `[48, 120]`/`3078` (`r19.carrier.carrier_prefix_bytes`,
   `r19.carrier.carrier_prefix_hex`), trailer byte `[10]`/`0a`
   (`r19.carrier.carrier_trailer_bytes`, `r19.carrier.carrier_trailer_hex`),
   decode body slice `[2, 38]` (`r19.carrier.decode_body_slice`) and three
   passing decode checks (`r19.carrier.decode_checks`). The other six carriers
   are `raw_bytes` with decode body slice `[0, length]`
   (`r21.carrier.carrier_form`, `r24.carrier.carrier_form`).

3. **Carrier bytes and decoded bytes differ, and each digest names its
   referent.** r19: carrier 39 B (`r19.carrier.bytes`, `r19.carrier.sha256`),
   decoded 18 B (`r19.decoded.bytes`, `r19.decoded.sha256`); subject and
   artifact digests cover the **carrier file**, the bytecode digest covers the
   **decoded bytes** (`r19.digest_scopes.subject`, `r19.digest_scopes.artifact`,
   `r19.digest_scopes.bytecode`). r21: one byte string for all three
   (`r21.digest_scopes.subject`, `r21.digest_scopes.artifact`,
   `r21.digest_scopes.bytecode`, `r21.carrier.sha256`).

4. **What the saved records record.** The r19 record names its operation
   (`r19.recorded.operation`), provider id and version (`r19.recorded.provider_id`,
   `r19.recorded.provider_version`), evidence id (`r19.recorded.evidence_id`),
   `authority` and `confidence` (`r19.recorded.authority`,
   `r19.recorded.confidence`) and the artifact fields
   (`r19.recorded.artifact.bytes`, `r19.recorded.artifact.encoding`); the
   record file's own digest is `r19.record.sha256`. Across all seven records the
   distinct values are printed once each (`summary.distinct_evidence_kind_values`,
   `summary.distinct_discovery_completeness_values`,
   `summary.distinct_runtime_execution_values`,
   `summary.distinct_provider_version_values`,
   `summary.distinct_bytecode_kind_values`,
   `summary.distinct_bytecode_hardfork_values`,
   `summary.distinct_bytecode_deployment_authenticity_values`,
   `summary.distinct_artifact_encoding_values`). These are **recorded** fields
   of the saved files: this entry does not authenticate them and claims no
   origin, completeness or authenticity from them.

5. **Instruction walk, JUMPDEST set, raw byte offsets.** r19: 11 instruction
   tuples of (offset, opcode, immediate bytes) (`r19.instructions`,
   `r19.instruction_opcode_counts`), JUMPDEST set `[16]`
   (`r19.valid_jumpdest_offsets`), raw `0x63` offsets `[6]`, raw `0x5b` offsets
   `[16]` (`r19.raw_0x63_offsets`, `r19.raw_0x5b_offsets`), JUMPI at 14 preceded
   by a PUSH1 whose operand byte is 16, in the JUMPDEST set
   (`r19.jumpi_with_preceding_push1`). r22: JUMPDEST set `[30, 32]`, raw
   `0x63` `[7, 17]`, raw `0x5b` `[30, 32]` (`r22.valid_jumpdest_offsets`,
   `r22.raw_0x63_offsets`, `r22.raw_0x5b_offsets`), pairs `0xaaaaaaaa`@30 and
   `0xbbbbbbbb`@32 (`r22.candidate_pairs_normalized`). r23: raw `0x63` `[0]`,
   empty JUMPDEST set (`r23.raw_0x63_offsets`, `r23.valid_jumpdest_offsets`).

6. **The four records that report no pair:** `r23.candidate_pairs_normalized`,
   `r24.candidate_pairs_normalized`, `r25.candidate_pairs_normalized`,
   `r26.candidate_pairs_normalized` are all empty.

7. **The template: derived once from r19, searched as raw bytes elsewhere.**
   Derived once from r19's own instruction boundaries and then searched as a raw
   byte string in every file: `63deadbeef14601057`, 9 bytes
   (`summary.template_hex`, `summary.template_length`); in r19 one occurrence,
   span 6-14 (`r19.template.template_occurrence_count`,
   `r19.template.template_inclusive_spans`); in r24 one occurrence at start 1,
   span 1-9 (`r24.template.template_occurrence_count`,
   `r24.template.template_occurrence_starts`,
   `r24.template.template_inclusive_spans`). r24's instruction tuples are at
   offsets 0, 33, 34 (`r24.instructions`) with opcode counts one `0x7f`, one
   `0x50`, one `0x00` (`r24.instruction_opcode_counts`), so the occurrence lies
   inside the PUSH32 immediate: at r24 file offset 7 — template index 6
   (`r24.template.template_push1_byte_offset`,
   `r24.template.template_push1_template_index`) — the byte is `0x60`
   (`r24.template.template_push1_byte_value`) but is **not** an instruction
   opcode (`r24.template.template_push1_byte_is_instruction_opcode`); the
   enclosing instruction is the PUSH32 at 0
   (`r24.template.template_enclosing_instruction`), and the occurrence start is
   not an instruction boundary
   (`r24.template.template_occurrence_start_is_instruction_boundary`). The
   template operand byte is at offset 8 with value 16
   (`r24.template.template_operand_byte_offset`,
   `r24.template.template_operand_byte_value`); the byte at that operand's
   value, offset 16, is `0x00` and is not a raw `0x5b` byte
   (`r24.template.template_target_offset`, `r24.template.template_target_byte`,
   `r24.template.template_target_is_raw_0x5b`).

8. **r25 and r26.** r25's JUMPI operand is 16, not in its JUMPDEST set `[17]`
   (`r25.jumpi_with_preceding_push1`, `r25.valid_jumpdest_offsets`); r26's is
   17, in its JUMPDEST set `[17]` (`r26.jumpi_with_preceding_push1`,
   `r26.valid_jumpdest_offsets`); both report no pair
   (`r25.candidate_pairs_normalized`, `r26.candidate_pairs_normalized`).

## Inference

- In each non-empty saved result in this sample (r19, r21, r22) the reported
  offset coincides with the operand of the PUSH1 preceding a JUMPI, and the byte
  there is `0x5b` on an instruction boundary (`r19.jumpi_with_preceding_push1`,
  `r21.jumpi_with_preceding_push1`, `r22.jumpi_with_preceding_push1`). The
  other four records report no pair, so no offset is available there. This is an
  observation about these bytes, not a definition of the field for any other
  carrier, and not a claim that the field *is* a jump destination in general.
- A digest binds the bytes it hashed and nothing further: not provenance,
  acquisition completeness, producer origin or deployment authenticity
  (`summary.distinct_bytecode_kind_values`,
  `summary.distinct_bytecode_hardfork_values`,
  `summary.distinct_bytecode_deployment_authenticity_values`).

## Unknown

- Why r23, r24, r25 and r26 report no pair. This entry states the emptiness and
  the byte facts around it, proposes **no** rule that would produce it, and
  asserts no cause.
- Whether an empty pair list means the file has no callable interface: every
  record carries `discovery_completeness=unknown`
  (`summary.distinct_discovery_completeness_values`), so an empty list is not
  read as absence.
- The recorded `evidence_id` values (`r19.recorded.evidence_id`): this entry
  does not address, recompute or authenticate them and claims no formula for
  them, reading them as recorded identifiers only.
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
  this entry is by digest (`r19.digest_scopes.subject`). The record's own
  `artifact.encoding` is a recorded label (`r19.recorded.artifact.encoding`),
  not a statement about how the bytes were decoded; the decode boundaries are
  the ones derived from the carrier bytes (Observation 2).
- **No verifier is credited as a guard for any value in this entry.**
  `corpus/verify_evm_evidence.py` is not cited as support, and every clause of
  this entry is unguarded by it: the carrier and decoded digests and their
  scopes, the carrier form and decode boundaries, the instruction walk, the
  JUMPDEST set, the raw `0x63` and `0x5b` offsets, the template occurrences,
  spans, operand, target byte and boundary flags, the two candidate counts, and
  every inventory row. The block in `## Reproduce` is a manual comparison
  against the saved records; it is **not** claimed to be deletion-sensitive.
  Input-drift probes do not establish clause-deletion guard coverage.
- The seven records and the seven fixtures were read only; no file under
  `corpus/fixtures/` or `corpus/live/` was modified, and the retained round-61
  rejected candidates were not edited.

## Cross-lane scope note (Q10)

The shipped-artifact reverse-engineering overlap between this lane and a
sibling lane is recorded as unresolved in this round's own intake and lesson
material — `corpus/lessons/round-62.md` ("ADJ-06 sibling arbitration … Operator-
owned and unresolved; new entries do not declare ownership or a ruling") and
`.ufo/waves/round-62/build/R62DebtExistingFiles.md` (section 4) — and this entry
declares no ownership and no ruling. It cites no sibling corpus file and adds
no unsupported sibling-ownership attribution; the primary saved-record source
S026 was reopened independently for this entry, and every byte and record fact
above comes from this entry's own readout.

## Q01-Q13 decisions (proposed by the author; not self-admission)

| Q | proposed | basis in this entry |
|---|---|---|
| Q01 | author-proposed pass; final independent decisions in the round-62 lesson | Load-bearing claims rest on S028 (opcode byte values and the jump-destination scan, quoted under `## Source facts` with its exact URL and file:line anchors, tier A for that scope), S031 (the authored fixtures and their decoded bytes) and S026 (the seven saved records, reopened independently for this entry, whose recorded metadata and identifiers are quoted in Observation 4). All three rows are written in `corpus/SOURCES.md`; no rejected row is cited. |
| Q02 | pass | `source:`, `verified-at:`, `recheck:` and `coverage-map: C09` headers are present. |
| Q03 | pass | Expected offsets and counts come from the byte walk; the saved records supply the reported fields, never the expected ones. The template is derived once from r19's own instruction boundaries. |
| Q04 | pass | The provider is named with its recorded id and version and its own explicit output fields; the walk is labeled manual, and the entry's own stdlib Python run and the corpus verifier it names (as a non-credited comparison) are tools it names, not tools it credits. |
| Q05 | pass (past tense) | No current capability is claimed; the records were not re-run. |
| Q06 | pass | Every fixture premise is re-derived from the built bytes by the block in `## Reproduce`, including the carrier form and the decode boundaries. |
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
| template bytes and length | `summary.template_hex` | 63deadbeef14601057 |
| template length | `summary.template_length` | 9 |
| distinct evidence_kind values over the seven records | `summary.distinct_evidence_kind_values` | ["inferred"] |
| distinct discovery_completeness values over the seven records | `summary.distinct_discovery_completeness_values` | ["unknown"] |
| distinct runtime_execution values over the seven records | `summary.distinct_runtime_execution_values` | ["not-performed"] |
| distinct provider_version values over the seven records | `summary.distinct_provider_version_values` | ["evmole@0.9.3"] |
| distinct bytecode kind values over the seven records | `summary.distinct_bytecode_kind_values` | ["unknown"] |
| distinct bytecode hardfork values over the seven records | `summary.distinct_bytecode_hardfork_values` | ["unknown"] |
| distinct bytecode deployment_authenticity values over the seven records | `summary.distinct_bytecode_deployment_authenticity_values` | ["unknown"] |
| distinct artifact encoding values over the seven records | `summary.distinct_artifact_encoding_values` | ["hex","raw"] |
| r19 carrier form | `r19.carrier.carrier_form` | ascii_hex_text |
| r19 carrier bytes | `r19.carrier.bytes` | 39 |
| r19 carrier sha256 | `r19.carrier.sha256` | 294e6fd2e041d5bea0558a26c1e399eddccf71bc0d279d398a4c0e915517b827 |
| r19 carrier is ASCII text | `r19.carrier.carrier_is_ascii_text` | true |
| r19 carrier prefix bytes | `r19.carrier.carrier_prefix_bytes` | [48,120] |
| r19 carrier prefix hex | `r19.carrier.carrier_prefix_hex` | 3078 |
| r19 carrier trailer bytes | `r19.carrier.carrier_trailer_bytes` | [10] |
| r19 carrier trailer hex | `r19.carrier.carrier_trailer_hex` | 0a |
| r19 decode body slice | `r19.carrier.decode_body_slice` | [2,38] |
| r19 decode checks | `r19.carrier.decode_checks` | {"ascii_prefix_is_0x":true,"body_is_even_length_hex":true,"trailer_is_lf":true} |
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
| r19 artifact bytes | `r19.recorded.artifact.bytes` | 39 |
| r19 artifact encoding | `r19.recorded.artifact.encoding` | hex |
| r19 bytecode bytes | `r19.recorded.bytecode.bytes` | 18 |
| r19 instruction tuples (offset, opcode, immediate) | `r19.instructions` | [[0,96,"00"],[2,53,""],[3,96,"e0"],[5,28,""],[6,99,"deadbeef"],[11,20,""],[12,96,"10"],[14,87,""],[15,0,""],[16,91,""],[17,0,""]] |
| r19 instruction opcode counts | `r19.instruction_opcode_counts` | {"0x0":2,"0x14":1,"0x1c":1,"0x35":1,"0x57":1,"0x5b":1,"0x60":3,"0x63":1} |
| r19 valid JUMPDEST offsets | `r19.valid_jumpdest_offsets` | [16] |
| r19 raw 0x63 offsets | `r19.raw_0x63_offsets` | [6] |
| r19 raw 0x5b offsets | `r19.raw_0x5b_offsets` | [16] |
| r19 JUMPI with preceding PUSH1 | `r19.jumpi_with_preceding_push1` | [[14,16,true]] |
| r19 candidate pairs (normalized) | `r19.candidate_pairs_normalized` | [["0xdeadbeef",16]] |
| r19 candidate pairs (raw) | `r19.candidate_pairs_raw` | [["deadbeef",16]] |
| r19 template occurrence count | `r19.template.template_occurrence_count` | 1 |
| r19 template inclusive spans | `r19.template.template_inclusive_spans` | [[6,14]] |
| r21 carrier form | `r21.carrier.carrier_form` | raw_bytes |
| r21 decode body slice | `r21.carrier.decode_body_slice` | [0,18] |
| r22 carrier form | `r22.carrier.carrier_form` | raw_bytes |
| r22 decode body slice | `r22.carrier.decode_body_slice` | [0,34] |
| r23 carrier form | `r23.carrier.carrier_form` | raw_bytes |
| r23 decode body slice | `r23.carrier.decode_body_slice` | [0,7] |
| r25 carrier form | `r25.carrier.carrier_form` | raw_bytes |
| r25 decode body slice | `r25.carrier.decode_body_slice` | [0,19] |
| r26 carrier form | `r26.carrier.carrier_form` | raw_bytes |
| r26 decode body slice | `r26.carrier.decode_body_slice` | [0,19] |
| r21 carrier sha256 (= r19 decoded) | `r21.carrier.sha256` | d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723 |
| r21 subject digest scope | `r21.digest_scopes.subject` | carrier_and_decoded_same_byte_string |
| r21 artifact digest scope | `r21.digest_scopes.artifact` | carrier_and_decoded_same_byte_string |
| r21 bytecode digest scope | `r21.digest_scopes.bytecode` | carrier_and_decoded_same_byte_string |
| r21 valid JUMPDEST offsets | `r21.valid_jumpdest_offsets` | [16] |
| r21 raw 0x5b offsets | `r21.raw_0x5b_offsets` | [16] |
| r21 JUMPI with preceding PUSH1 | `r21.jumpi_with_preceding_push1` | [[14,16,true]] |
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
| r24 carrier form | `r24.carrier.carrier_form` | raw_bytes |
| r24 instruction tuples | `r24.instructions` | [[0,127,"63deadbeef146010570000000000000000000000000000000000000000000000"],[33,80,""],[34,0,""]] |
| r24 instruction opcode counts | `r24.instruction_opcode_counts` | {"0x0":1,"0x50":1,"0x7f":1} |
| r24 valid JUMPDEST offsets | `r24.valid_jumpdest_offsets` | [] |
| r24 raw 0x63 offsets | `r24.raw_0x63_offsets` | [1] |
| r24 raw 0x5b offsets | `r24.raw_0x5b_offsets` | [] |
| r19 template byte at the PUSH1 position | `r19.template.template_push1_byte_value` | 96 |
| r19 that template byte is an instruction opcode | `r19.template.template_push1_byte_is_instruction_opcode` | true |
| r19 template byte offset of the PUSH1 position | `r19.template.template_push1_byte_offset` | 12 |
| r19 enclosing instruction of that byte | `r19.template.template_enclosing_instruction` | [[12,96]] |
| r21 template occurrence count | `r21.template.template_occurrence_count` | 1 |
| r21 template inclusive spans | `r21.template.template_inclusive_spans` | [[6,14]] |
| r22 template occurrence count | `r22.template.template_occurrence_count` | 0 |
| r23 template occurrence count | `r23.template.template_occurrence_count` | 0 |
| r25 template occurrence count | `r25.template.template_occurrence_count` | 1 |
| r26 template occurrence count | `r26.template.template_occurrence_count` | 0 |
| r24 template byte at the PUSH1 position | `r24.template.template_push1_byte_value` | 96 |
| r24 template index of the PUSH1 position | `r24.template.template_push1_template_index` | 6 |
| r24 template occurrence count | `r24.template.template_occurrence_count` | 1 |
| r24 template occurrence starts | `r24.template.template_occurrence_starts` | [1] |
| r24 template inclusive spans | `r24.template.template_inclusive_spans` | [[1,9]] |
| r24 template byte at the PUSH1 position | `r24.template.template_push1_byte_value` | 96 |
| r24 that template byte is an instruction opcode | `r24.template.template_push1_byte_is_instruction_opcode` | false |
| r24 template byte offset of the PUSH1 position | `r24.template.template_push1_byte_offset` | 7 |
| r24 enclosing instruction of that byte | `r24.template.template_enclosing_instruction` | [[0,127]] |
| r24 template operand byte offset | `r24.template.template_operand_byte_offset` | 8 |
| r24 template operand byte value | `r24.template.template_operand_byte_value` | 16 |
| r24 template target offset | `r24.template.template_target_offset` | 16 |
| r24 byte at the template target | `r24.template.template_target_byte` | 0 |
| r24 template target is a raw 0x5b byte | `r24.template.template_target_is_raw_0x5b` | false |
| r24 template occurrence start is an instruction boundary | `r24.template.template_occurrence_start_is_instruction_boundary` | false |
| r24 candidate pairs (normalized) | `r24.candidate_pairs_normalized` | [] |
| r25 JUMPI with preceding PUSH1 | `r25.jumpi_with_preceding_push1` | [[15,16,false]] |
| r25 valid JUMPDEST offsets | `r25.valid_jumpdest_offsets` | [17] |
| r25 candidate pairs (normalized) | `r25.candidate_pairs_normalized` | [] |
| r26 JUMPI with preceding PUSH1 | `r26.jumpi_with_preceding_push1` | [[15,17,true]] |
| r26 valid Jumpdest offsets | `r26.valid_jumpdest_offsets` | [17] |
| r26 candidate pairs (normalized) | `r26.candidate_pairs_normalized` | [] |

## Reproduce

Save this block as `readout.py` and run `python3 -B readout.py <archive-root>`.
It reads the seven fixtures and the seven saved records, executes no bytecode,
opens no chain, calls no producer, writes nothing; stdout is one JSON object
per case then one summary object.

```python
#!/usr/bin/env python3
"""Manual EVM byte/dispatch readout over seven authored fixtures and their saved
`inspect_evm_interface` records.  Usage: python3 -B readout.py <root>
One JSON object per case on stdout (one line each), then one summary object.
Read-only; no bytecode, chain, RPC or producer; no file written; stdlib only.
"""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(sys.argv[1])
FIX = ROOT / "corpus" / "fixtures"
RUNS = ROOT / "corpus" / "live" / "runs"
CASES = [(19, "fixture.hex"), (21, "fixture.raw"), (22, "fixture.raw"),
         (23, "fixture.raw"), (24, "fixture.raw"), (25, "fixture.raw"),
         (26, "fixture.raw")]
# Opcode bytes and the PUSH-N rule are RECORDED from S028 (execution-specs tag v2.20.0,
# commit 2004296f2ffcbcebcd00f41152d33e8dfda0922a): instructions/__init__.py :55 EQ=0x14,
# :104 STOP=0x00, :106 JUMPI=0x57, :109 JUMPDEST=0x5B, :118 POP=0x50, :121 PUSH0=0x5F,
# :122 PUSH1=0x60, :125 PUSH4=0x63, :153 PUSH32=0x7F; runtime.py:22-69.
P1, P4, P32 = 0x60, 0x63, 0x7F
JUMPI, JD = 0x57, 0x5B
HEXD = set(b"0123456789abcdefABCDEF")
def sha(d):
    return hashlib.sha256(d).hexdigest()
def walk(code):
    """Instruction tuples (offset, opcode, immediate hex); PUSH-N immediates are
    skipped, so a 0x5B byte inside immediate data is not an instruction."""
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
def decode_carrier(raw):
    """Derive the decode boundaries from the carrier bytes themselves.  A carrier
    is an ASCII hex text only when its own bytes show the ASCII prefix 0x, a
    trailing newline and an even-length hex body; a carrier that starts with
    those two ASCII bytes but is not a hex text is refused, not decoded."""
    text = all(b < 0x80 for b in raw)
    chk = {"ascii_prefix_is_0x": None, "trailer_is_lf": None, "body_is_even_length_hex": None}
    info = {"carrier_prefix_hex": None, "carrier_prefix_bytes": None, "carrier_trailer_hex": None,
            "carrier_trailer_bytes": None, "carrier_is_ascii_text": text,
            "decode_body_slice": [0, len(raw)], "decode_checks": chk}
    if not (text and raw.startswith(b"0x")):
        info["carrier_form"] = "raw_bytes"
        return raw, info
    if not raw.endswith(b"\n"):
        raise ValueError("hex-text carrier has no trailing newline: %r" % raw[-4:])
    body = raw[2:-1]
    if len(body) % 2 or not all(c in HEXD for c in body):
        raise ValueError("hex-text carrier body is not an even-length hex string")
    info.update(carrier_prefix_hex=raw[:2].hex(), carrier_prefix_bytes=list(raw[:2]),
                carrier_trailer_hex=raw[-1:].hex(), carrier_trailer_bytes=list(raw[-1:]),
                carrier_form="ascii_hex_text", decode_body_slice=[2, len(raw) - 1],
                decode_checks={"ascii_prefix_is_0x": True, "trailer_is_lf": True,
                                "body_is_even_length_hex": True})
    return bytes.fromhex(body.decode("ascii")), info
def derive_template(code):
    """The dispatch-like template, derived once from r19's own instruction
    boundaries: from the PUSH4 opcode offset through the JUMPI opcode offset.
    The PUSH1 position inside the template is that instruction's own offset."""
    ins = walk(code)
    p4 = [i for i, op, _ in ins if op == P4]
    ji = [i for i, op, _ in ins if op == JUMPI]
    p1 = [i for i, op, _ in ins if op == P1]
    if not (p4 and ji):
        raise ValueError("r19 has no PUSH4 and JUMPI instruction pair")
    start, end = p4[0], ji[0]
    push1 = [i for i in p1 if start < i < end]
    if not push1:
        raise ValueError("r19 has no PUSH1 instruction between its PUSH4 and JUMPI")
    return code[start:end + 1], push1[0] - start
def template_block(code, template, push1_rel, ins):
    """The template is a raw byte string searched in each file; the offsets below
    are template byte positions in that file, not instruction offsets."""
    starts, spans, i = [], [], code.find(template)
    while i != -1:
        starts.append(i)
        spans.append([i, i + len(template) - 1])
        i = code.find(template, i + 1)
    at = {o for o, _, _ in ins}
    b = {"template_hex": template.hex(), "template_length": len(template),
         "template_occurrence_count": len(starts), "template_occurrence_starts": starts,
         "template_inclusive_spans": spans, "template_push1_byte_offset": None,
         "template_push1_byte_value": None, "template_push1_byte_is_instruction_opcode": None,
         "template_push1_template_index": None,
         "template_operand_byte_offset": None, "template_operand_byte_value": None,
         "template_target_offset": None, "template_target_byte": None,
         "template_target_is_raw_0x5b": None, "template_enclosing_instruction": None,
         "template_occurrence_start_is_instruction_boundary": None}
    for s in starts:
        po = s + push1_rel
        oo, ov = po + 1, code[po + 1]
        tb = code[ov] if ov < len(code) else None
        b.update(template_push1_byte_offset=po, template_push1_byte_value=code[po],
                 template_push1_byte_is_instruction_opcode=(po in at),
                 template_push1_template_index=push1_rel,
                 template_operand_byte_offset=oo, template_operand_byte_value=ov,
                 template_target_offset=ov, template_target_byte=tb,
                 template_target_is_raw_0x5b=(tb == JD),
                 template_enclosing_instruction=[[o, op] for o, op, im in ins
                                                if o <= po < o + 1 + len(im) // 2],
                 template_occurrence_start_is_instruction_boundary=(s in at))
    return b
def main():
    template, push1_rel = derive_template(decode_carrier(
        (FIX / "evm-r19" / "fixture.hex").read_bytes())[0])
    obs, pairs, same, per_case = 0, set(), True, []
    for r, name in CASES:
        carrier = (FIX / ("evm-r%d" % r) / name).read_bytes()
        code, cinfo = decode_carrier(carrier)
        rb = (RUNS / ("round-%d" % r) / "inspection.json").read_bytes()
        rec = json.loads(rb.decode("utf-8"))
        nr = rec["normalized_result"]
        art, bc, sub = nr["artifact"], nr["bytecode"], rec["subject"]["digest"]["sha256"]
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
               "carrier": dict(cinfo, file="corpus/fixtures/evm-r%d/%s" % (r, name),
                               bytes=len(carrier), sha256=sha(carrier)),
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
                                "hardfork": bc["hardfork"], "deployment_authenticity": bc["deployment_authenticity"]}},
               "digest_scopes": {"subject": referent(sub, carrier, code),
                                 "artifact": referent(art["sha256"], carrier, code),
                                 "bytecode": referent(bc["sha256"], carrier, code)},
               "instructions": [[i, op, h] for i, op, h in ins],
               "instruction_opcode_counts": counts, "valid_jumpdest_offsets": jd,
               "raw_0x63_offsets": [i for i, b in enumerate(code) if b == P4],
               "raw_0x5b_offsets": [i for i, b in enumerate(code) if b == JD],
               "jumpi_with_preceding_push1": ji, "candidate_pairs_normalized": norm,
               "candidate_pairs_raw": raw, "template": template_block(code, template, push1_rel, ins)}
        per_case.append(out)
        print(json.dumps(out, sort_keys=True, separators=(",", ":")))
    agg = {}
    paths = {"evidence_kind": ("recorded", "evidence_kind"),
             "discovery_completeness": ("recorded", "discovery_completeness"),
             "runtime_execution": ("recorded", "runtime_execution"),
             "provider_version": ("recorded", "provider_version"),
             "bytecode_kind": ("recorded", "bytecode", "kind"),
             "bytecode_hardfork": ("recorded", "bytecode", "hardfork"),
             "bytecode_deployment_authenticity": ("recorded", "bytecode", "deployment_authenticity"),
             "artifact_encoding": ("recorded", "artifact", "encoding")}
    for key, path in paths.items():
        vals = set()
        for c in per_case:
            node = c
            for k in path:
                node = node[k]
            vals.add(node)
        agg["distinct_" + key + "_values"] = sorted(vals)
    print(json.dumps(dict(agg, total_cases=len(CASES), reported_candidate_observations=obs,
                          distinct_candidate_pairs=len(pairs), distinct_pairs=sorted(list(pairs)),
                          raw_and_normalized_pair_counts_equal=same,
                          template_hex=template.hex(), template_length=len(template)),
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
{"candidate_pairs_normalized":[["0xdeadbeef",16]],"candidate_pairs_raw":[["deadbeef",16]],"carrier":{"bytes":39,"carrier_form":"ascii_hex_text","carrier_is_ascii_text":true,"carrier_prefix_bytes":[48,120],"carrier_prefix_hex":"3078","carrier_trailer_bytes":[10],"carrier_trailer_hex":"0a","decode_body_slice":[2,38],"decode_checks":{"ascii_prefix_is_0x":true,"body_is_even_length_hex":true,"trailer_is_lf":true},"file":"corpus/fixtures/evm-r19/fixture.hex","sha256":"294e6fd2e041d5bea0558a26c1e399eddccf71bc0d279d398a4c0e915517b827"},"case":"r19","decoded":{"bytes":18,"hex":"60003560e01c63deadbeef14601057005b00","sha256":"d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723"},"digest_scopes":{"artifact":"carrier_file_bytes_only","bytecode":"decoded_bytecode_bytes_only","subject":"carrier_file_bytes_only"},"instruction_opcode_counts":{"0x0":2,"0x14":1,"0x1c":1,"0x35":1,"0x57":1,"0x5b":1,"0x60":3,"0x63":1},"instructions":[[0,96,"00"],[2,53,""],[3,96,"e0"],[5,28,""],[6,99,"deadbeef"],[11,20,""],[12,96,"10"],[14,87,""],[15,0,""],[16,91,""],[17,0,""]],"jumpi_with_preceding_push1":[[14,16,true]],"raw_0x5b_offsets":[16],"raw_0x63_offsets":[6],"record":{"bytes":4175,"file":"corpus/live/runs/round-19/inspection.json","sha256":"e892dd18ff219f71ce2644a3f5a3e3ad3479d2ca46df9e2a7c260e7b33f15948"},"recorded":{"artifact":{"bytes":39,"encoding":"hex","sha256":"294e6fd2e041d5bea0558a26c1e399eddccf71bc0d279d398a4c0e915517b827"},"authority":"shipped-artifact","bytecode":{"bytes":18,"deployment_authenticity":"unknown","digest_algorithm":"sha256","hardfork":"unknown","hex":"60003560e01c63deadbeef14601057005b00","kind":"unknown","sha256":"d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723"},"confidence":"inferred","discovery_completeness":"unknown","evidence_id":"ev_0ad0097eb137ff9196b29ac3fb6109d8f72ee0761e2655fa1fca594295cf6f42","evidence_kind":"inferred","operation":"inspect_evm_interface","predicate_type":"rea.analysis","provider_id":"evmole-interface","provider_name":"REA EVM interface adapter","provider_version":"evmole@0.9.3","runtime_execution":"not-performed"},"template":{"template_enclosing_instruction":[[12,96]],"template_hex":"63deadbeef14601057","template_inclusive_spans":[[6,14]],"template_length":9,"template_occurrence_count":1,"template_occurrence_start_is_instruction_boundary":true,"template_occurrence_starts":[6],"template_operand_byte_offset":13,"template_operand_byte_value":16,"template_push1_byte_is_instruction_opcode":true,"template_push1_byte_offset":12,"template_push1_byte_value":96,"template_push1_template_index":6,"template_target_byte":91,"template_target_is_raw_0x5b":true,"template_target_offset":16},"valid_jumpdest_offsets":[16]}
{"candidate_pairs_normalized":[["0xdeadbeef",16]],"candidate_pairs_raw":[["deadbeef",16]],"carrier":{"bytes":18,"carrier_form":"raw_bytes","carrier_is_ascii_text":false,"carrier_prefix_bytes":null,"carrier_prefix_hex":null,"carrier_trailer_bytes":null,"carrier_trailer_hex":null,"decode_body_slice":[0,18],"decode_checks":{"ascii_prefix_is_0x":null,"body_is_even_length_hex":null,"trailer_is_lf":null},"file":"corpus/fixtures/evm-r21/fixture.raw","sha256":"d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723"},"case":"r21","decoded":{"bytes":18,"hex":"60003560e01c63deadbeef14601057005b00","sha256":"d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723"},"digest_scopes":{"artifact":"carrier_and_decoded_same_byte_string","bytecode":"carrier_and_decoded_same_byte_string","subject":"carrier_and_decoded_same_byte_string"},"instruction_opcode_counts":{"0x0":2,"0x14":1,"0x1c":1,"0x35":1,"0x57":1,"0x5b":1,"0x60":3,"0x63":1},"instructions":[[0,96,"00"],[2,53,""],[3,96,"e0"],[5,28,""],[6,99,"deadbeef"],[11,20,""],[12,96,"10"],[14,87,""],[15,0,""],[16,91,""],[17,0,""]],"jumpi_with_preceding_push1":[[14,16,true]],"raw_0x5b_offsets":[16],"raw_0x63_offsets":[6],"record":{"bytes":4175,"file":"corpus/live/runs/round-21/inspection.json","sha256":"395c4f48e7efd7eafb07cc8c4b82c0fcea4e7a060885a97ee463da0faafdb7d7"},"recorded":{"artifact":{"bytes":18,"encoding":"raw","sha256":"d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723"},"authority":"shipped-artifact","bytecode":{"bytes":18,"deployment_authenticity":"unknown","digest_algorithm":"sha256","hardfork":"unknown","hex":"60003560e01c63deadbeef14601057005b00","kind":"unknown","sha256":"d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723"},"confidence":"inferred","discovery_completeness":"unknown","evidence_id":"ev_4810eda7b540fbf2d4265c0f9deb3886dc009945cb77276b980f5502112cfc85","evidence_kind":"inferred","operation":"inspect_evm_interface","predicate_type":"rea.analysis","provider_id":"evmole-interface","provider_name":"REA EVM interface adapter","provider_version":"evmole@0.9.3","runtime_execution":"not-performed"},"template":{"template_enclosing_instruction":[[12,96]],"template_hex":"63deadbeef14601057","template_inclusive_spans":[[6,14]],"template_length":9,"template_occurrence_count":1,"template_occurrence_start_is_instruction_boundary":true,"template_occurrence_starts":[6],"template_operand_byte_offset":13,"template_operand_byte_value":16,"template_push1_byte_is_instruction_opcode":true,"template_push1_byte_offset":12,"template_push1_byte_value":96,"template_push1_template_index":6,"template_target_byte":91,"template_target_is_raw_0x5b":true,"template_target_offset":16},"valid_jumpdest_offsets":[16]}
{"candidate_pairs_normalized":[["0xaaaaaaaa",30],["0xbbbbbbbb",32]],"candidate_pairs_raw":[["aaaaaaaa",30],["bbbbbbbb",32]],"carrier":{"bytes":34,"carrier_form":"raw_bytes","carrier_is_ascii_text":false,"carrier_prefix_bytes":null,"carrier_prefix_hex":null,"carrier_trailer_bytes":null,"carrier_trailer_hex":null,"decode_body_slice":[0,34],"decode_checks":{"ascii_prefix_is_0x":null,"body_is_even_length_hex":null,"trailer_is_lf":null},"file":"corpus/fixtures/evm-r22/fixture.raw","sha256":"94c1790f966b78a9a5cc61bdc9ad4b805aaea6989e37773f66ff433deeb1dbe2"},"case":"r22","decoded":{"bytes":34,"hex":"60003560e01c8063aaaaaaaa14601e578063bbbbbbbb14602057000000005b005b00","sha256":"94c1790f966b78a9a5cc61bdc9ad4b805aaea6989e37773f66ff433deeb1dbe2"},"digest_scopes":{"artifact":"carrier_and_decoded_same_byte_string","bytecode":"carrier_and_decoded_same_byte_string","subject":"carrier_and_decoded_same_byte_string"},"instruction_opcode_counts":{"0x0":6,"0x14":2,"0x1c":1,"0x35":1,"0x57":2,"0x5b":2,"0x60":4,"0x63":2,"0x80":2},"instructions":[[0,96,"00"],[2,53,""],[3,96,"e0"],[5,28,""],[6,128,""],[7,99,"aaaaaaaa"],[12,20,""],[13,96,"1e"],[15,87,""],[16,128,""],[17,99,"bbbbbbbb"],[22,20,""],[23,96,"20"],[25,87,""],[26,0,""],[27,0,""],[28,0,""],[29,0,""],[30,91,""],[31,0,""],[32,91,""],[33,0,""]],"jumpi_with_preceding_push1":[[15,30,true],[25,32,true]],"raw_0x5b_offsets":[30,32],"raw_0x63_offsets":[7,17],"record":{"bytes":4437,"file":"corpus/live/runs/round-22/inspection.json","sha256":"c55f69727ce2e62707ae0f9203c338efe57e6aeadc7fb5f5cd939bee3f9b3a33"},"recorded":{"artifact":{"bytes":34,"encoding":"raw","sha256":"94c1790f966b78a9a5cc61bdc9ad4b805aaea6989e37773f66ff433deeb1dbe2"},"authority":"shipped-artifact","bytecode":{"bytes":34,"deployment_authenticity":"unknown","digest_algorithm":"sha256","hardfork":"unknown","hex":"60003560e01c8063aaaaaaaa14601e578063bbbbbbbb14602057000000005b005b00","kind":"unknown","sha256":"94c1790f966b78a9a5cc61bdc9ad4b805aaea6989e37773f66ff433deeb1dbe2"},"confidence":"inferred","discovery_completeness":"unknown","evidence_id":"ev_24fe0001213ec58a588d086e0fe55677d749f3eb6998afe6ee6095ff9dc4af4b","evidence_kind":"inferred","operation":"inspect_evm_interface","predicate_type":"rea.analysis","provider_id":"evmole-interface","provider_name":"REA EVM interface adapter","provider_version":"evmole@0.9.3","runtime_execution":"not-performed"},"template":{"template_enclosing_instruction":null,"template_hex":"63deadbeef14601057","template_inclusive_spans":[],"template_length":9,"template_occurrence_count":0,"template_occurrence_start_is_instruction_boundary":null,"template_occurrence_starts":[],"template_operand_byte_offset":null,"template_operand_byte_value":null,"template_push1_byte_is_instruction_opcode":null,"template_push1_byte_offset":null,"template_push1_byte_value":null,"template_push1_template_index":null,"template_target_byte":null,"template_target_is_raw_0x5b":null,"template_target_offset":null},"valid_jumpdest_offsets":[30,32]}
{"candidate_pairs_normalized":[],"candidate_pairs_raw":[],"carrier":{"bytes":7,"carrier_form":"raw_bytes","carrier_is_ascii_text":false,"carrier_prefix_bytes":null,"carrier_prefix_hex":null,"carrier_trailer_bytes":null,"carrier_trailer_hex":null,"decode_body_slice":[0,7],"decode_checks":{"ascii_prefix_is_0x":null,"body_is_even_length_hex":null,"trailer_is_lf":null},"file":"corpus/fixtures/evm-r23/fixture.raw","sha256":"8047ddff11234c2d36bd134cfb4aec669efa3ff89ed35a922552d44ebfe22f5a"},"case":"r23","decoded":{"bytes":7,"hex":"63c0ffee005000","sha256":"8047ddff11234c2d36bd134cfb4aec669efa3ff89ed35a922552d44ebfe22f5a"},"digest_scopes":{"artifact":"carrier_and_decoded_same_byte_string","bytecode":"carrier_and_decoded_same_byte_string","subject":"carrier_and_decoded_same_byte_string"},"instruction_opcode_counts":{"0x0":1,"0x50":1,"0x63":1},"instructions":[[0,99,"c0ffee00"],[5,80,""],[6,0,""]],"jumpi_with_preceding_push1":[],"raw_0x5b_offsets":[],"raw_0x63_offsets":[0],"record":{"bytes":3923,"file":"corpus/live/runs/round-23/inspection.json","sha256":"ce9fe51536af461ef2deb19b8cf8ff3582dba736abc2747b07ab845d3aaac2af"},"recorded":{"artifact":{"bytes":7,"encoding":"raw","sha256":"8047ddff11234c2d36bd134cfb4aec669efa3ff89ed35a922552d44ebfe22f5a"},"authority":"shipped-artifact","bytecode":{"bytes":7,"deployment_authenticity":"unknown","digest_algorithm":"sha256","hardfork":"unknown","hex":"63c0ffee005000","kind":"unknown","sha256":"8047ddff11234c2d36bd134cfb4aec669efa3ff89ed35a922552d44ebfe22f5a"},"confidence":"inferred","discovery_completeness":"unknown","evidence_id":"ev_296e7ed723c7356b1cfbeee5dadc11283e5efe74535d544114ebf3b692f77201","evidence_kind":"inferred","operation":"inspect_evm_interface","predicate_type":"rea.analysis","provider_id":"evmole-interface","provider_name":"REA EVM interface adapter","provider_version":"evmole@0.9.3","runtime_execution":"not-performed"},"template":{"template_enclosing_instruction":null,"template_hex":"63deadbeef14601057","template_inclusive_spans":[],"template_length":9,"template_occurrence_count":0,"template_occurrence_start_is_instruction_boundary":null,"template_occurrence_starts":[],"template_operand_byte_offset":null,"template_operand_byte_value":null,"template_push1_byte_is_instruction_opcode":null,"template_push1_byte_offset":null,"template_push1_byte_value":null,"template_push1_template_index":null,"template_target_byte":null,"template_target_is_raw_0x5b":null,"template_target_offset":null},"valid_jumpdest_offsets":[]}
{"candidate_pairs_normalized":[],"candidate_pairs_raw":[],"carrier":{"bytes":35,"carrier_form":"raw_bytes","carrier_is_ascii_text":false,"carrier_prefix_bytes":null,"carrier_prefix_hex":null,"carrier_trailer_bytes":null,"carrier_trailer_hex":null,"decode_body_slice":[0,35],"decode_checks":{"ascii_prefix_is_0x":null,"body_is_even_length_hex":null,"trailer_is_lf":null},"file":"corpus/fixtures/evm-r24/fixture.raw","sha256":"b69834e0ef786e3c001b2c833c8c0388acc017de14d06110cfa85d4948685d93"},"case":"r24","decoded":{"bytes":35,"hex":"7f63deadbeef1460105700000000000000000000000000000000000000000000005000","sha256":"b69834e0ef786e3c001b2c833c8c0388acc017de14d06110cfa85d4948685d93"},"digest_scopes":{"artifact":"carrier_and_decoded_same_byte_string","bytecode":"carrier_and_decoded_same_byte_string","subject":"carrier_and_decoded_same_byte_string"},"instruction_opcode_counts":{"0x0":1,"0x50":1,"0x7f":1},"instructions":[[0,127,"63deadbeef146010570000000000000000000000000000000000000000000000"],[33,80,""],[34,0,""]],"jumpi_with_preceding_push1":[],"raw_0x5b_offsets":[],"raw_0x63_offsets":[1],"record":{"bytes":3981,"file":"corpus/live/runs/round-24/inspection.json","sha256":"ec9e147db2b042f4d991816fa2a02fe95373de31956730fd1eb4cce5763742cd"},"recorded":{"artifact":{"bytes":35,"encoding":"raw","sha256":"b69834e0ef786e3c001b2c833c8c0388acc017de14d06110cfa85d4948685d93"},"authority":"shipped-artifact","bytecode":{"bytes":35,"deployment_authenticity":"unknown","digest_algorithm":"sha256","hardfork":"unknown","hex":"7f63deadbeef1460105700000000000000000000000000000000000000000000005000","kind":"unknown","sha256":"b69834e0ef786e3c001b2c833c8c0388acc017de14d06110cfa85d4948685d93"},"confidence":"inferred","discovery_completeness":"unknown","evidence_id":"ev_50d5ffb1fdbd17c4896409ca4cc8b20d7ed344ef4011029bea4aa474b7f0ab9e","evidence_kind":"inferred","operation":"inspect_evm_interface","predicate_type":"rea.analysis","provider_id":"evmole-interface","provider_name":"REA EVM interface adapter","provider_version":"evmole@0.9.3","runtime_execution":"not-performed"},"template":{"template_enclosing_instruction":[[0,127]],"template_hex":"63deadbeef14601057","template_inclusive_spans":[[1,9]],"template_length":9,"template_occurrence_count":1,"template_occurrence_start_is_instruction_boundary":false,"template_occurrence_starts":[1],"template_operand_byte_offset":8,"template_operand_byte_value":16,"template_push1_byte_is_instruction_opcode":false,"template_push1_byte_offset":7,"template_push1_byte_value":96,"template_push1_template_index":6,"template_target_byte":0,"template_target_is_raw_0x5b":false,"template_target_offset":16},"valid_jumpdest_offsets":[]}
{"candidate_pairs_normalized":[],"candidate_pairs_raw":[],"carrier":{"bytes":19,"carrier_form":"raw_bytes","carrier_is_ascii_text":false,"carrier_prefix_bytes":null,"carrier_prefix_hex":null,"carrier_trailer_bytes":null,"carrier_trailer_hex":null,"decode_body_slice":[0,19],"decode_checks":{"ascii_prefix_is_0x":null,"body_is_even_length_hex":null,"trailer_is_lf":null},"file":"corpus/fixtures/evm-r25/fixture.raw","sha256":"2d87a4e203ebf590beab57cf7318ccf93c92035d7929d0bc16e6850433f5e8f7"},"case":"r25","decoded":{"bytes":19,"hex":"0060003560e01c63deadbeef14601057005b00","sha256":"2d87a4e203ebf590beab57cf7318ccf93c92035d7929d0bc16e6850433f5e8f7"},"digest_scopes":{"artifact":"carrier_and_decoded_same_byte_string","bytecode":"carrier_and_decoded_same_byte_string","subject":"carrier_and_decoded_same_byte_string"},"instruction_opcode_counts":{"0x0":3,"0x14":1,"0x1c":1,"0x35":1,"0x57":1,"0x5b":1,"0x60":3,"0x63":1},"instructions":[[0,0,""],[1,96,"00"],[3,53,""],[4,96,"e0"],[6,28,""],[7,99,"deadbeef"],[12,20,""],[13,96,"10"],[15,87,""],[16,0,""],[17,91,""],[18,0,""]],"jumpi_with_preceding_push1":[[15,16,false]],"raw_0x5b_offsets":[17],"raw_0x63_offsets":[7],"record":{"bytes":3949,"file":"corpus/live/runs/round-25/inspection.json","sha256":"4f677a209d08c3f9e531191aea9cdc58533898b9f9ed2394b3db63a0b8d448cf"},"recorded":{"artifact":{"bytes":19,"encoding":"raw","sha256":"2d87a4e203ebf590beab57cf7318ccf93c92035d7929d0bc16e6850433f5e8f7"},"authority":"shipped-artifact","bytecode":{"bytes":19,"deployment_authenticity":"unknown","digest_algorithm":"sha256","hardfork":"unknown","hex":"0060003560e01c63deadbeef14601057005b00","kind":"unknown","sha256":"2d87a4e203ebf590beab57cf7318ccf93c92035d7929d0bc16e6850433f5e8f7"},"confidence":"inferred","discovery_completeness":"unknown","evidence_id":"ev_23a9464bf2d8c3de3614176efa53016f002ddade19f1ae842b4325ba2d095579","evidence_kind":"inferred","operation":"inspect_evm_interface","predicate_type":"rea.analysis","provider_id":"evmole-interface","provider_name":"REA EVM interface adapter","provider_version":"evmole@0.9.3","runtime_execution":"not-performed"},"template":{"template_enclosing_instruction":[[13,96]],"template_hex":"63deadbeef14601057","template_inclusive_spans":[[7,15]],"template_length":9,"template_occurrence_count":1,"template_occurrence_start_is_instruction_boundary":true,"template_occurrence_starts":[7],"template_operand_byte_offset":14,"template_operand_byte_value":16,"template_push1_byte_is_instruction_opcode":true,"template_push1_byte_offset":13,"template_push1_byte_value":96,"template_push1_template_index":6,"template_target_byte":0,"template_target_is_raw_0x5b":false,"template_target_offset":16},"valid_jumpdest_offsets":[17]}
{"candidate_pairs_normalized":[],"candidate_pairs_raw":[],"carrier":{"bytes":19,"carrier_form":"raw_bytes","carrier_is_ascii_text":false,"carrier_prefix_bytes":null,"carrier_prefix_hex":null,"carrier_trailer_bytes":null,"carrier_trailer_hex":null,"decode_body_slice":[0,19],"decode_checks":{"ascii_prefix_is_0x":null,"body_is_even_length_hex":null,"trailer_is_lf":null},"file":"corpus/fixtures/evm-r26/fixture.raw","sha256":"ebe2d6757a7acd4c5b9de82441f66e70561350267114e445a2d6b8d037f8e97d"},"case":"r26","decoded":{"bytes":19,"hex":"0060003560e01c63deadbeef14601157005b00","sha256":"ebe2d6757a7acd4c5b9de82441f66e70561350267114e445a2d6b8d037f8e97d"},"digest_scopes":{"artifact":"carrier_and_decoded_same_byte_string","bytecode":"carrier_and_decoded_same_byte_string","subject":"carrier_and_decoded_same_byte_string"},"instruction_opcode_counts":{"0x0":3,"0x14":1,"0x1c":1,"0x35":1,"0x57":1,"0x5b":1,"0x60":3,"0x63":1},"instructions":[[0,0,""],[1,96,"00"],[3,53,""],[4,96,"e0"],[6,28,""],[7,99,"deadbeef"],[12,20,""],[13,96,"11"],[15,87,""],[16,0,""],[17,91,""],[18,0,""]],"jumpi_with_preceding_push1":[[15,17,true]],"raw_0x5b_offsets":[17],"raw_0x63_offsets":[7],"record":{"bytes":3949,"file":"corpus/live/runs/round-26/inspection.json","sha256":"bf2b2337b83f694ff9c7f9dfafbd9074de9b3310c52609fb41c993d9c782fc3c"},"recorded":{"artifact":{"bytes":19,"encoding":"raw","sha256":"ebe2d6757a7acd4c5b9de82441f66e70561350267114e445a2d6b8d037f8e97d"},"authority":"shipped-artifact","bytecode":{"bytes":19,"deployment_authenticity":"unknown","digest_algorithm":"sha256","hardfork":"unknown","hex":"0060003560e01c63deadbeef14601157005b00","kind":"unknown","sha256":"ebe2d6757a7acd4c5b9de82441f66e70561350267114e445a2d6b8d037f8e97d"},"confidence":"inferred","discovery_completeness":"unknown","evidence_id":"ev_482e41e68b6c5f358fe660bc70eaf55f69c7b487fd61774e1a443571aecec090","evidence_kind":"inferred","operation":"inspect_evm_interface","predicate_type":"rea.analysis","provider_id":"evmole-interface","provider_name":"REA EVM interface adapter","provider_version":"evmole@0.9.3","runtime_execution":"not-performed"},"template":{"template_enclosing_instruction":null,"template_hex":"63deadbeef14601057","template_inclusive_spans":[],"template_length":9,"template_occurrence_count":0,"template_occurrence_start_is_instruction_boundary":null,"template_occurrence_starts":[],"template_operand_byte_offset":null,"template_operand_byte_value":null,"template_push1_byte_is_instruction_opcode":null,"template_push1_byte_offset":null,"template_push1_byte_value":null,"template_push1_template_index":null,"template_target_byte":null,"template_target_is_raw_0x5b":null,"template_target_offset":null},"valid_jumpdest_offsets":[17]}
{"distinct_artifact_encoding_values":["hex","raw"],"distinct_bytecode_deployment_authenticity_values":["unknown"],"distinct_bytecode_hardfork_values":["unknown"],"distinct_bytecode_kind_values":["unknown"],"distinct_candidate_pairs":3,"distinct_discovery_completeness_values":["unknown"],"distinct_evidence_kind_values":["inferred"],"distinct_pairs":[["0xaaaaaaaa",30],["0xbbbbbbbb",32],["0xdeadbeef",16]],"distinct_provider_version_values":["evmole@0.9.3"],"distinct_runtime_execution_values":["not-performed"],"raw_and_normalized_pair_counts_equal":true,"reported_candidate_observations":4,"template_hex":"63deadbeef14601057","template_length":9,"total_cases":7}
```
