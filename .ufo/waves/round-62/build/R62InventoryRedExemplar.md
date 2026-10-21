RESULT: COMPLETE

# R62InventoryRedExemplar — manual Q11 statement-to-output audit (old C04 edge-span, old C09 r24 count/span)

Scope: review aid only. No corpus byte, fixture byte, README row, coverage-map status, source row or lesson was written by this seat; no gate script was added to the corpus; no admission is claimed; README stays uncovered. Verbatim transcripts: scratch `q11-red-before-exemplar.md`.

## Frozen inputs and evidence hygiene
- Revision `a3498e25ad87bf756288812d0ea7c474b09433c7`, extracted read-only via `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive a3498e25…` into `/fast/scratch/hyaku/revenger-r62/R62InventoryRedExemplar/`. Audited committed text: `corpus/knowledge/commonjs-destructured-require-edges.md` (C04), `corpus/knowledge/evm-saved-interface-candidates.md` (C09); both still `admission-status: rejected`.
- Prior evidence read, not re-run: `.ufo/waves/round-61/falsify-w3/W3JsOverclaimCritic.md:5-7,39`, `.ufo/waves/round-61/falsify-w3/W3EvmR24Immediate.md:16-21`, `corpus/lessons/round-61-verifier-spotcheck.md`, `corpus/QUALITY.md:23` (Q11, unchanged). Not executed: `reports/round-61/measure.py`, any gate/probe, fixture JavaScript, EVM bytecode, REA producers, chain/RPC. Only committed bytes and stdlib Python readouts were used.

## Red-before 1 — old C04: "this entry's block carries … edge spans" (entry :80-83)
```
$ python3 -B sweep.py corpus/knowledge/commonjs-destructured-require-edges.md Reproduce C04 'location' 'start' 'span' 'column' 'offset' 'line'
C04: file=commonjs-destructured-require-edges.md section="Reproduce" block_lines=53 block_bytes=3588
C04: token='location' count=0 | 'start' 0 | 'span' 0 | 'column' 0 | 'offset' 0 | 'line' 0 | TOTAL_MATCHING_LINES=0   (counts condensed; verbatim in scratch)
```
The spans exist in the primary record but the block never reads them: the saved JSON carries `evidence.location.value = {kind: source-range, source, start:{line,column}, end:{line,column}}` (raw saved file: `location` 223, `start` 298, `column` 596 occurrences). The Limitations bullet claims the block carries edge spans; it carries none.

## Red-before 2 — old C09 r24: count, span, embedded target (entry :39, :65-66, :94-96)
```
$ python3 -B sweep.py corpus/knowledge/evm-saved-interface-candidates.md Reproduce C09 'pattern' 'occurrence' 'span' 'embedded' '.find(' '.count(' '0x5b' '0x10' 'deadbeef'
C09: file=evm-saved-interface-candidates.md section="Reproduce" block_lines=33 block_bytes=1975
C09: 'pattern'=0 'occurrence'=0 'span'=0 'embedded'=0 '.find('=0 '.count('=0 'deadbeef'=0 '0x10'=0   (counts condensed; verbatim in scratch)
C09: token='0x5b' count=1 -> block_line=19: valid = [i for i, op, _ in ins if op == 0x5b]   # valid JUMPDEST set (S016/S017)
```
Statement→output pairing (`python3 -B statement_to_output.py corpus/knowledge/evm-saved-interface-candidates.md`): `'0x5B' in_block=True in_output=False BLOCK_ONLY` (that one `0x5b` is the *instruction-level* set, not the raw byte count the prose asserts), `'0x10' UNSUPPORTED`, `'[1, 9]' UNSUPPORTED`. So "one PUSH32" (:39), "its immediate contains the r19 pattern" (:39), the "[1, 9]" span (:94-96), "the file has no 0x5B byte" (:66) and the "embedded JUMPI target (0x10)" (:65) have no in-entry derivation.

## Why correct external byte values do not repair the entry
`corpus/QUALITY.md:23` (Q11, unchanged) rejects "a value is correct when re-derived but the entry carries no derivation". The round-61 closure's byte search (`len(raw)=35`, start `[1]`, inclusive span `[1,9]`) is an **external** reviewer check living in no entry block, so it cannot discharge Q11 for the entry, and it does not cover the other two missing derivations (raw `0x5B` count, embedded target `0x10`). Editing the rejected entries is barred by `reports/round-62/claims.md` ("Candidates are NEW files, not edits to rejected round-61 evidence"). The only lawful repairs are: derive inside the entry's own block, or label the value "recorded, not re-derived".

## The same command, and what it must find in the NEW candidates
`python3 -B check_candidate.py <entry.md> <spec.json>` reads the entry's `## Reproduce` block and its `## Provenance` output and prints GREEN only when the block contains the derivation **and** the printed output carries the value. Scratch specs: `spec-c04.json` classes = named-import-edge-set, edge-span-derivation, require-call-span-from-bytes, record-digest; `spec-c09.json` classes = pattern-search-and-span, search-key-derived-not-copied, raw-byte-counts, embedded-target-derivation, instruction-vs-raw-scope, fixture-digest.
```
$ python3 -B check_candidate.py corpus/knowledge/commonjs-destructured-require-edges.md spec-c04.json
  class='edge-span-derivation' verdict=RED block_tokens_hit=[] output_regex_hit=[]
  class='require-call-span-from-bytes' verdict=RED block_tokens_hit=[] output_regex_hit=[]
  RESULT RED (2 red class(es))                                                          # exit 1
$ python3 -B check_candidate.py corpus/knowledge/evm-saved-interface-candidates.md spec-c09.json
  'pattern-search-and-span' RED | 'raw-byte-counts' RED | 'embedded-target-derivation' RED | 'instruction-vs-raw-scope' RED
  RESULT RED (5 red class(es))                                                          # exit 1
$ python3 -B check_candidate.py candidate-shape-c04.md spec-c04.json -> RESULT GREEN (0 red)  # exit 0
$ python3 -B check_candidate.py candidate-shape-c09.md spec-c09.json -> RESULT GREEN (0 red)  # exit 0
```
Required of `corpus/knowledge/round-62-commonjs-require-name-evidence.md` (C04): the block must read `evidence.location.value` and print start/end line+column per `imports` edge, plus a `require(` call offset derived from fixture bytes, and the Provenance output must carry those numbers. Required of `corpus/knowledge/round-62-evm-dispatch-byte-evidence.md` (C09): the block must derive the search key from the **r19 fixture bytes** (not copy `truth.json`'s recorded hex), search it in r24 and print occurrence count and inclusive span; print raw-byte facts (`raw_byte_count_0x5b`, `raw_byte_offsets_0x63`) and instruction-level facts (`instruction_valid_jumpdest_positions`, `embedded_target_is_valid_jumpdest`) as **separate labelled fields**; print the embedded target and its destination byte. Anything cited only to truth.json / LOG.md / another entry must be labelled "recorded, not re-derived".

## Tested fix (scratch, proposed, not corpus)
`fix_c04_block.py`, `fix_c09_block.py` (stdlib only) with `test-fix-c04.py`, `test-fix-c09.py` (in-memory mutants only; no corpus byte touched):
```
test-fix-c09.py: K0 derived key pattern_hex=63deadbeef14601057 push4_offset=6 jumpi_offset=14 len=9
M0 spans=[(1, 9)] inside_push32=[True] target=0x10 raw_0x5b=0 valid_jumpdest=[] target_is_valid_jumpdest=False
M1 byte16=0x5b -> raw_0x5b_count=1 offsets=[16] but valid_jumpdest=[] (scopes stay apart)
M2a byte8=0x11 -> occurrence_count=0 ; M2b synthetic PUSH1/JUMPI dest 17 valid flips ; M3 pattern prepended -> spans=[(0, 8), (10, 18)] ; ALL MUTANT CHECKS PASS
test-fix-c04.py: M0 call_offset=28 unnamed_span=(1:28-1:50) ; M1 record span moved -> 7:3-7:9 ; M2 location removed -> fields None ; M3 offset 28 -> 18 ; ALL MUTANT CHECKS PASS
```
Self-correction recorded: my first proposed C09 block conflated raw `0x5B` offsets with instruction-level JUMPDEST positions (caught by seat `RevengerR61-2.R62CriticQ14`, E7); block and mutant M1 now keep the two scopes separate.

## Addendum — candidate-seat C09 block re-verified after its fix (2026-10-21)
Seat `RevengerR61-2.R62EvmCandidatesOracle` supplied its block; I re-verified the bytes and re-ran the same checker (scratch shape built by `build_shape_from_seat.py`):
```
$ sha256sum $D/read_evm_raw_vs_normalized.py $D/reader-stdout.txt $D/reader-evidence-extract.md $D/reader_core.py $D/reader_core-stdout.txt
7eceb4b4…4eb32 read_evm_raw_vs_normalized.py | 0a6252b0…2cc reader-stdout.txt | 6476cde7…b3386 reader-evidence-extract.md
47dbb071…73b6 reader_core.py (236 lines) | e4baf888…3227 reader_core-stdout.txt (335 lines)
$ python3 -B check_candidate.py candidate-seat-c09.md spec-c09.json
  pattern-search-and-span GREEN | search-key-derived-not-copied GREEN | raw-byte-counts GREEN
  embedded-target-derivation GREEN | instruction-vs-raw-scope GREEN | fixture-digest GREEN
  RESULT GREEN (0 red class(es))
```
The digest gap is FIXED and independently confirmed: the block prints 65 `sha256` lines, and its `r24_fixture_file_sha256` (`b69834e0…8d93`), `r24_record_file_sha256` (`ec9e147d…42cd`) and `r19_decoded_sha256` (`d1086bce…723`) equal the digests I compute from the frozen copy. Key derivations still equal mine: search key `63deadbeef14601057` from r19 bytes; r24 `occurrence_count 1`, `inclusive_spans [[1, 9]]`, `raw_byte_count_0x5b 0`, `raw_byte_offsets_0x63 [1]`, `instruction_valid_jumpdest_positions []`, `embedded_jumpi_target_operand_value 16`, `target_byte_in_fixture 0x00`, `target_is_valid_jumpdest False`.
Two gaps of the same class found in the first pass are now closed and re-verified: the condensed block prints the scope-separation mutant itself (`M1_raw_and_instruction_scopes_differ True`, `M1_mutated_offset 5 mutated_offset_inside_push_immediate True`, stdout:328-335) and the corpus count (`total_op_records_in_corpus 7`, `records_outside_corpus_live_runs []`, `record_round_ids [...]`, stdout:2-5). Its key r24 values are unchanged and still equal mine (`raw_byte_count_0x5b 0`, `raw_byte_offsets_0x63 [1]`, `instruction_valid_jumpdest_positions []`, `search_key_occurrence_count 1`, `inclusive_spans [[1, 9]]`, `embedded_jumpi_target_operand_value 16`, `target_byte_in_fixture 0x00`), it prints 65 `sha256` lines, `grep` finds no write/exec/network call in `reader_core.py`, an independent extraction of the field labels quoted in the seat's own report found 0 labels absent from either stdout, my own re-run of `reader_core.py` exits 0 with stdout byte-identical to the saved 335-line stdout and empty stderr, and the seat's scratch `corpus/` copy is byte-identical to the frozen extraction (`diff -r -q` over the whole `corpus/` tree prints 0 lines), so the block's inputs are the committed bytes; independent spot checks of its discovery claims also hold (`records_discovered 7`, `raw_observations 4 normalized_observations 4`, no `evm-r20` fixture dir, and `6.4.0` absent from all seven record `inspection.json` files). Spec disclosure unchanged: `spec-c09.json` accepts `=`/whitespace and label alternatives, so a candidate's naming is not graded; the old entry still fails 5/6 classes and my stand-in still passes 6/6. This checks the candidate *block*, not the entry: the landed `corpus/knowledge/round-62-evm-dispatch-byte-evidence.md` must still be re-run through the checker.

## Residual risk and verification gaps
- The round-62 candidate files were still absent from `corpus/knowledge/` at audit time; the C09 candidate seat's proposed block was checked from scratch (above), the C04 candidate's block was not available; re-run `check_candidate.py` on both landed entries.
- `check_candidate.py` matches tokens/regexes: a class can pass on a token that is present but not load-bearing; the mutation tests are what show the derivations are real. The old entries stay rejected; the red-before is not a request to repair them.

## Proposed artifacts (scratch; for L1 lesson mining and candidate authors)
`/fast/scratch/hyaku/revenger-r62/R62InventoryRedExemplar/`: `q11-red-before-exemplar.md` (lesson-ready red-before + tested fix), `sweep.py`, `statement_to_output.py`, `check_candidate.py`, `spec-c04.json`, `spec-c09.json`, `fix_c04_block.py`, `fix_c09_block.py`, `test-fix-c04.py`, `test-fix-c09.py`, `build_fake_candidates.py`, `build_shape_from_seat.py`, `candidate-shape-c04.md`, `candidate-shape-c09.md`, `candidate-seat-c09.md`.

Installs: none (no tool installed or updated; python3 stdlib and read-only git only).
