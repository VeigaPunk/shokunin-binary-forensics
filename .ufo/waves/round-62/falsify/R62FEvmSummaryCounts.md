GRADE: HOLDS — summary counts/arrays and every numerical word/range in `corpus/knowledge/round-62-evm-dispatch-byte-evidence.md` @ d97761952be256d145d298022de03091de91d358 (count slice only)

## Target / frozen state
- Frozen revision `d97761952be256d145d298022de03091de91d358`; claim base `5bd4a90fc1a34caa94496601b60537b3aab12301`; pre-registration `a3498e25ad87bf756288812d0ea7c474b09433c7`.
- Candidate sha256 `6a1d394ad92fcaa5344069d1225e428988f1397e80c8968745d7b48bf43fed6e`; worktree file and `git show d9776195:corpus/knowledge/round-62-evm-dispatch-byte-evidence.md` hash identically (both `6a1d394a…`).
- Extracted `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive d9776195…` into `/fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62FEvmSummaryCounts`; cwd=`<seat>`; TMPDIR=`<seat>/tmp` (created first); no bytecode/chain/RPC/producer execution.
- Evidence bytes unchanged base→frozen: `git diff --stat a3498e25 d977619 -- <7 evm fixture dirs> <7 round-19/21…26 record dirs>` empty, exit 0; all 14 fixture/record sha256 values identical in both extracted trees (e.g. r19 fixture `294e6fd2…b827`, r19 record `e892dd18…5948`).

## Observation 1 — independent recount (my own implementation, not the entry's readout)
Command: `python3 -B audit.py .` → exit 0. Exact summary line:
`{"distinct_candidate_pairs":3,"distinct_pairs":[["0xaaaaaaaa",30],["0xbbbbbbbb",32],["0xdeadbeef",16]],"pattern_hex":"63deadbeef14601057","pattern_length":9,"raw_and_normalized_pair_counts_equal":true,"raw_distinct_pair_count":3,"raw_norm_semantically_equal":true,"reported_candidate_observations":4,"total_cases":7}`
Per case as `case norm,raw,jd,instr,carrier→decoded`:
`r19 1,1,[16],11,39→18`; `r21 1,1,[16],11,18→18`; `r22 2,2,[30,32],22,34→34`; `r23 0,0,[],3,7→7`; `r24 0,0,[],3,35→35`; `r25 0,0,[17],12,19→19`; `r26 0,0,[17],12,19→19`.
- Total cases = **7** (exactly the seven `evm-r19,r21…r26` fixture dirs; one carrier+record pair each).
- Candidate observations = **4** = r19 1 + r21 1 + r22 2; r23–r26 0.
- Distinct `(selector, bytecode_offset)` pairs = **3**; r19 and r21 report the same pair `("0xdeadbeef",16)`.
- Raw vs normalized: raw entries **4**, normalized entries **4**, per-record lengths equal `1,1,2,0,0,0,0` (`summary.raw_and_normalized_pair_counts_equal=true`); raw distinct after `0x`-strip = **3** and raw≡normalized semantically (`raw_norm_semantically_equal=true`, an extra check beyond the entry's length-only field).

## Observation 2 — printed output is derived, not replayed
Extracted the single ```python block verbatim to `readout.py`; `python3 -B readout.py <archive>` → exit 0, stderr empty, 8 stdout lines; `diff <(grep -v '^$' prov.txt) readout-out.txt` empty (`PROVENANCE_EXACT_MATCH`). I then deep-compared each of the 7 printed case objects against my independent objects: **7/7 DEEP_EQUAL**; the summary's 7 printed keys match. Every printed field (not just summary scalars) is reproduced by code sharing nothing with the entry's readout.

## Observation 3 — inventory table and prose numbers
`python3 -B compare.py <entry> audit-out.json` → `inventory_rows=67 mismatches=0`; `prose_checks=36 failed=0`.
- All 67 Evidence-inventory rows resolve in my recomputed objects and equal the table values exactly.
- Prose checks cover `:46-52` (7 cases, 4 observations, 3 distinct, raw/normalized equal), `:56-64` (39-byte `0x`+36 hex+`\n` carrier → 18 decoded), `:78-88` (11 tuples, JD `[16]`, raw `0x63` `[6]`, raw `0x5b` `[16]`, JUMPI@14 operand 16 in set), `:92-95` (r23–r26 empty), `:97-108` (r24 counts, raw `[1]`/`[]`, pattern 9 bytes, one occurrence at 1, span `[1,9]`, embedded 7/8/16/16/0/false), `:110-118` (r25 `[15,16,false]` vs JD `[17]`; r26 `[15,17,true]` vs JD `[17]`), `:217-224` (summary rows), `:449` (summary stdout).
- One provider version (`evmole@0.9.3`) and one operation (`inspect_evm_interface`) across all 7 records.

## Observation 4 — raw vs instruction counts (lesson-required distinction)
`case raw0x63/instrPUSH4 raw0x5b/instrJD raw0x57/instrJUMPI pairs`:
`r19 1/1 1/1 1/1 1`; `r21 1/1 1/1 1/1 1`; `r22 2/2 2/2 2/2 2`; `r23 1/1 0/0 0/0 0`; `r24 1/0 0/0 1/0 0`; `r25 1/1 1/1 1/1 0`; `r26 1/1 1/1 1/1 0`.
r24 is the only divergence: raw `0x63`@1 and raw `0x57`@9 are bytes inside the PUSH32 immediate (walk = PUSH32@0, POP@33, STOP@34), exactly as `r24.instruction_opcode_counts={"0x0":1,"0x50":1,"0x7f":1}` states. Every numerical word/range in `:46-118` and the table matches these definitions; no count, offset, span, digest, byte length or range contradicts its cited field.

## Non-numeric, out of this slice (not graded here; for L1 integration)
- The pattern template is derived from r19 only (`:362`), while `:101` says "derived from the files' own bytes" (plural); r22's own PUSH4..JUMPI run is `63aaaaaaaa14601e57` and template occurrences in r22 = 0. Derivation-scope wording, already a material Q11 finding in `R62FEvmQ11Inventory.md` (F2).
- r24 offsets 7/8/16 match `embedded_*` exactly as pattern-byte positions; the "PUSH1 opcode byte" executable-role wording is that seat's F1/F3, outside the numeric question.
- Inventory rows `:221` (claim "bytes and length", field only `summary.pattern_hex`) and `:241` (claim kind/authenticity/hardfork, field only `...kind`) name fewer fields than the claim spans; values are true and printed, but naming is imprecise (that seat's F4/F5). I did not re-adjudicate Q11.

## Inference
- The summary layer is not output-replay: an independent walk/search over the seven carriers and seven saved records reproduces every printed field deep-equal, and the recorded Provenance block is byte-identical to a fresh run at the frozen rev.
- The recorded lane-base run is valid for the frozen state because all 14 evidence files are byte-identical at `a3498e25` and `d977619`.
- Every numeric value asserted is correct under the printed field definitions and derivable in-entry from printed arrays/scalars; array-length-derived counts (11 tuples, 4 empty records, 1/1/2) are not token-presence claims.

## Unknown
- S028 opcode constants/line anchors were not re-opened by this seat (recorded labels, outside the count slice); the Q11 seat reports them verified against tag v2.20.0.
- No adjudication of Q01–Q13 or admission; no claim about producer internals, chain state or callable-interface completeness.

## VERDICT
HOLDS for the assigned count/summary-array/numerical-word slice at `d97761952be256d145d298022de03091de91d358`; no minimal correction is required by this slice. Whole-entry admission is not supported by this seat and remains blocked by the separate Q11 material findings (`R62FEvmQ11Inventory.md` F1–F3), which I did not repair, re-adjudicate or count.
Installs: none — `python3 3.14.8` pre-existing; no pacman/uv/cargo/npm action.
