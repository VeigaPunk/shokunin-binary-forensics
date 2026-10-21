# R62EvmCandidatesOracle — independent raw vs normalized reader over the seven archived EVM records

RESULT: COMPLETE

Seat `RevengerR61-2.R62EvmCandidatesOracle` (leaf, no dispatch). Frozen base `a3498e25ad87bf756288812d0ea7c474b09433c7`. Scope: read-only comparison of `raw_result.functions` vs `normalized_result.functions` in all seven saved `inspect_evm_interface` records, plus byte-level facts with raw-byte and instruction-level scopes kept as separate labelled fields. No provider call, no bytecode execution, no network, no README or corpus byte touched.

**Artifacts** (scratch, lane-owned, `/fast/scratch/hyaku/revenger-r62/R62EvmCandidatesOracle/`): `read_evm_raw_vs_normalized.py` (SHA-256 `7eceb4b4e998e13af89421413a0fd6235b08151448b2c8519270562d9304eb32`); `reader-stdout.txt` (611 lines, complete output; SHA-256 `0a6252b0e380708a90b4e468bf3d6df251d57a9475dd5034255cd04f50df02cc`); `reader-evidence-extract.md` (all digests, per-fixture byte facts, canon lists, mutant check; SHA-256 `6476cde7cd9267b7002a3ac43ee3c3315c55ae9c4e28937cc5a9b63d334b3386`); `reader_core.py` (SHA-256 `47dbb071d944173b457fee9cd484edb95d15e45615374097a885ebd6197673b6`) + `reader_core-stdout.txt` (SHA-256 `e4baf888ccf84e1bd345ba68cd0192ca58dd9b0142b88b7b7688877af4a13227`) — the condensed in-entry block for the C09 candidate (236 lines, stdlib, read-only, no write/exec/network; prints 65 sha256 lines covering every fixture and record digest). Extraction `git -C <repo> archive a3498e2 | tar -x -C …/R62EvmCandidatesOracle`; all runs on that copy, cwd = extracted root; the repo tree was never written.

## Command and output

`python3 -B read_evm_raw_vs_normalized.py .` → exit 0, stderr empty (611 lines in `reader-stdout.txt`; two runs byte-identical). Discovery is by record content, not name: every `corpus/live/runs/**/*.json` with `operation == "inspect_evm_interface"` → `records_discovered=7` (rounds 19, 21–26). A sweep of all `corpus/**/*.json` returns the same seven (`total_op_records_in_corpus=7`); none exists outside `corpus/live/runs/`. Fixture dirs are exactly `evm-r19, evm-r21…evm-r26` (7, no `evm-r20`); `fixture_dirs_without_record=[]`, `records_without_fixture_dir=[]` — 1:1 coverage.

**Every selector/offset pair, per record** (raw spelling vs normalized spelling):

```text
r19 raw ["deadbeef@16"]                normalized ["0xdeadbeef@16"]                pair_count=1
r21 raw ["deadbeef@16"]                normalized ["0xdeadbeef@16"]                pair_count=1
r22 raw ["aaaaaaaa@30","bbbbbbbb@32"] normalized ["0xaaaaaaaa@30","0xbbbbbbbb@32"] pair_count=2
r23 raw []  normalized []  pair_count=0     r24 raw []  normalized []  pair_count=0
r25 raw []  normalized []  pair_count=0     r26 raw []  normalized []  pair_count=0
```

**Counts of observations and distinct pairs** (same run):

```text
raw_observations=4  normalized_observations=4  observations_total_both_views=8
raw_distinct_pairs=3  normalized_distinct_pairs=3
canonical_distinct_pairs_raw=3  canonical_distinct_pairs_normalized=3
canonical_distinct_pairs_equal_across_views=True
canonical_distinct_pairs_list=[["aaaaaaaa",30],["bbbbbbbb",32],["deadbeef",16]]
```

`deadbeef@16` occurs in two records (r19 hex carrier, r21 raw carrier): 4 observations collapse to 3 distinct canonical pairs. The normalized view only adds the `0x` prefix; after canonicalisation the two views agree on every pair. Independent agreement: sibling `R62ReviewPairCounts.md` reports the same SET_B=4 observations / SET_C=3 distinct pairs.

**Cross-view correspondence:** `paired_field_comparisons_equal=12`, `paired_field_comparisons_disagree=0` (3 field pairs × 4 observations: `dispatch`, `arguments`/`inferred_arguments`, `stateMutability`/`inferred_state_mutability`); `records_with_raw_normalized_length_mismatch=[]`; whole-list canonical equality `records_with_canon_list_equal=7`, `canon_list_equal_all_seven=True`.

**Inferred flags / version metadata across the seven** (each `distinct_values=1` unless noted): `evidence_kind=inferred`; `discovery_completeness=unknown`; `runtime_execution=not-performed`; `bytecode.kind=unknown`; `bytecode.hardfork=unknown`; `bytecode.deployment_authenticity=unknown`; `bytecode.digest_algorithm=sha256`; `provider.id=evmole-interface`; `provider.name=REA EVM interface adapter`; `provider.version=evmole@0.9.3`; `parameters.encoding=[hex,raw]` (2 values). Each record also carries `authority=shipped-artifact`, `confidence=inferred`, `predicate_type=rea.analysis`, 6 `normalized_result.limitations` in all seven (`normalized_limitations_count_uniform=True`), `diagnostics` keys `stdout,stderr,truncated` with `truncated=False` in all seven. `rea-agents@6.4.0` does **not** occur in any of the seven record bytes (False ×7) while `evmole@0.9.3` does (True ×7): the producer package version is in the ledgers only.

**Search key derived from r19 fixture bytes** (not copied from `truth.json`): `search_key_derived_from_r19_bytes_hex=63deadbeef14601057`, `search_key_length_bytes=9`, source = "r19 fixture bytes: PUSH4 start to JUMPI end".

**Raw-byte vs instruction-level facts, separate labelled fields** (raw counts ignore the PUSH-data rule; instruction positions apply it). r24, the decoy fixture:

```text
r24_raw_byte_count_0x5b=0  r24_raw_byte_offsets_0x63=[1]
r24_instruction_valid_jumpdest_positions=[]  r24_instruction_count=3  r24_raw_byte_count=35
r24_raw_0x63_offsets_inside_push_immediate=[1]
r24_search_key_occurrence_count=1  r24_search_key_inclusive_spans=[[1,9]]
r24_search_key_starts_inside_push_immediate=[1]
r24_embedded_jumpi_target_operand_value=16  r24_embedded_target_byte_in_fixture=0x00
r24_embedded_target_is_valid_jumpdest=False  r24_embedded_target_is_raw_0x5b_byte=False
```

All seven fixtures carry the same field set (`raw_byte_count_0x5b`, `raw_byte_offsets_0x5b`, `raw_byte_offsets_0x63`, `instruction_valid_jumpdest_positions`, `instruction_count`, `raw_byte_count`, `search_key_occurrence_count`, `search_key_inclusive_spans`, `search_key_starts_inside_push_immediate`, `embedded_jumpi_target_operand_value`, `embedded_target_byte_in_fixture`, `embedded_target_is_valid_jumpdest`, `embedded_target_is_raw_0x5b_byte`) — full per-fixture values in `reader-evidence-extract.md`. The r19/r21 occurrence span is `[[6,14]]` while r24's is `[[1,9]]`: the same 9-byte sequence sits at different offsets, and only r24's starts inside a PUSH immediate. The JUMPI operand is an absolute program counter, so the embedded destination is the operand value itself (16) — in r19/r21 that byte is `0x5b` (valid jumpdest), in r24 it is `0x00` (not). Independent agreement: sibling `R62RevenR26Boundary.md` reports r26 with 12 instructions, jumpdest `[17]`, operand 17 — matching my `r26_instruction_valid_jumpdest_positions=[17]`, `r26_instruction_count=12`.

**In-memory scope-separation self-check** (no file written): a `0x5b` placed at r24 offset 5, inside the PUSH32 immediate, gives `M1_mutated_raw_byte_count_0x5b=1`, `M1_mutated_raw_byte_offsets_0x5b=[5]`, `M1_mutated_instruction_valid_jumpdest_positions=[]`, `M1_raw_and_instruction_scopes_differ=True` — the raw count rises while the instruction set stays empty. Breaking the first selector immediate byte gives `M2_broken_selector_search_key_occurrence_count=0` against `M2_original_r19_search_key_occurrence_count=1`.

**Saved digests vs authored fixture bytes:** `artifact_sha256_equals_fixture_bytes_all=True`, `bytecode_sha256_equals_decoded_all=True`, `bytecode_hex_equals_decoded_all=True`, `subject_digest_in_fixture_or_decoded_all=True`, `digest_rows=7`. Fixture file SHA-256 and bytes: r19 `294e6fd2…7b827`/39, r21 `d1086bce…0e723`/18, r22 `94c1790f…dbe2`/34, r23 `8047ddff…2f5a`/7, r24 `b69834e0…5d93`/35, r25 `2d87a4e2…8f7`/19, r26 `ebe2d675…97d`/19; record file SHA-256 `e892dd18…`, `395c4f48…`, `c55f6972…`, `ce9fe515…`, `ec9e147d…`, `4f677a20…`, `bf2b2337…` (full values and evidence IDs in `reader-evidence-extract.md`). Evidence IDs are read from the records and are **recorded identifiers**, not re-derived.

## Preservation checks (no harm)

- `git -C <repo> diff --name-only a3498e2 -- corpus/live corpus/fixtures corpus/README.md corpus/QUALITY.md corpus/SOURCES.md` → empty: no corpus, fixture, README, QUALITY or SOURCES byte changed by this seat. All seven record files and all seven fixture files are byte-identical between the frozen commit and the extracted copy (per-file SHA-256 compare, all MATCH). The M1/M2 checks mutate byte strings in memory only; no fixture was written.
- README C04 and C09 rows still read `uncovered`; held-row count still 4. **No README flip, no admission, no pre-credit.** No `corpus/knowledge/round-62-*.md` candidate file was created by this seat (the entry writer owns that path).

## Proposed artifact for the C09 candidate (Q11 in-entry derivation)

`reader_core.py` is a self-contained stdlib block the entry can inline in `## Reproduce`; output `reader_core-stdout.txt` (exit 0). It re-derives in-entry: discovery count (7), every raw and normalized selector/offset pair, per-record canonical list equality, observation counts (4/4/8), distinct-pair counts (3/3/3), the pair list, the seven flags, the version metadata, the r19-derived search key, and per-fixture raw-byte vs instruction-level fields (occurrence count, inclusive span, starts-inside-immediate, embedded target value/byte/validity). It also prints every fixture and record digest it derives (per-record `*_fixture_file_sha256`, `*_decoded_sha256`, `*_record_file_sha256`, `*_saved_artifact_sha256`, `*_saved_bytecode_sha256`, `*_saved_subject_digest_sha256` and the four equality checks), so a digest quoted in the entry is backed by the inlined block's own output rather than by prose; 65 sha256 lines in `reader_core-stdout.txt`. It also prints `total_op_records_in_corpus` (7), `records_outside_corpus_live_runs` ([]), `record_round_ids`, `fixture_dirs`, the per-record
`*_raw_pairs`/`*_normalized_pairs`/`*_pair_count` rows, and the in-memory scope-separation mutant lines (`M1_original_r24_*`, `M1_mutated_*`,
`M1_raw_and_instruction_scopes_differ=True`), so the "seven saved records" count and the raw-vs-instruction scope separation are also derived by the
inlined block rather than asserted in prose. Values that stay **recorded** (not re-derived) and must be labelled so in the entry: the evidence IDs, `rea-agents@6.4.0` (ledgers only), the `dispatch`/`arguments`/`stateMutability` semantics, and `truth.json`'s `embedded_pattern_hex`/`embedded_pattern_offsets` (my key and span are derived from bytes and agree with them, but `truth.json` itself is not the source). Constraints relayed from sibling read-only seats for the entry writer: `R62ConnectKasegi` — omit kasegi entirely or use verbatim `PROVINCE.md:3` (domain) plus `:42` ("Sibling lanes are reported, not absorbed:"); `PROVINCE.md:25` is the round-61 false cite; r24 is an authored decoy (raw `0x63` offset `[1]`, `executable_push4_count` 0), not evidence about a real package. `R62ConnectEvmPrior` — do not write "the reported offset is the JUMPDEST" unqualified; label kaidoku numbers as recorded; do not cite the rejected round-61 revenger entry as support. `R62InventoryRedExemplar` — the rejected entry's missing `pattern`/`occurrence`/`span`/`embedded` tokens are covered above by derived fields.

## Unknowns / limits

- Why r23–r26 report no candidate is not answered here; no cause asserted (Q07).
- The byte facts are raw-byte counts and instruction-boundary positions under the PUSH-data rule; they are not a validity or reachability rule for the provider's candidate list, and per `R62ConnectEvmPrior` the candidate must not state the reported offset *is* a JUMPDEST unqualified.
- No provider was called, so nothing here is a current capability or freshness claim (Q05); the records are dated 2026-10-12 and were not re-probed. Digests bind bytes only; no producer origin, completeness or authenticity claimed (Q09).
- `verify_evm_evidence.py` is not credited as a guard by this reader (round-61: its own run detected 0/37 single-conjunct deletions); Q13 rests on the inline block only.

## Installs / updates

None. No package, tool or system change; the reader uses the host's Python 3.14.8 stdlib.
