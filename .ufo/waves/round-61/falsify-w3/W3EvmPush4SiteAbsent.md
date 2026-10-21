GRADE: HOLDS — C09 Observation 2 final sentence "The PUSH4 locations themselves appear in no record field" (corpus/knowledge/evm-saved-interface-candidates.md:30-31)

Seat RevengerR61-2.W3EvmPush4SiteAbsent. Archive ab580698212258a55e43e9bb9bf6ac78c91eae2a (`rev-parse` confirmed) in `/tmp/revenger-r61w3-W3EvmPush4SiteAbsent`. No REA call, no bytecode or fixture execution, no chain/RPC.

## Method
- Recursive walk of every key/value in the seven saved records `corpus/live/runs/round-{19,21,22,23,24,25,26}/inspection.json`: 376 scalar leaves (326 strings, 22 numbers, 7 bools, 21 nulls). `raw_result` keys = `["functions"]` in all seven; `inspection.stderr` is 0 bytes in all seven.
- PUSH4 offsets re-derived from fixture bytes with an independent walk (PUSH-N immediates skipped): r19 6; r21 6; r22 7 and 17; r23 0; r24 none (its only 0x63 byte is at 1, inside the PUSH32 immediate); r25 7; r26 7.
- Record identity: all seven file sha256 prefixes equal the entry's Provenance (`corpus/knowledge/evm-saved-interface-candidates.md:146-159`) — e892dd18ff219f71 / 395c4f48e7efd7ea / c55f69727ce2e627 / ce9fe51536af461e / ec9e147db2b042f4 / 4f677a209d08c3f9 / bf2b2337b83f694f — and each record's `bytecode.hex` equals the fixture decoded bytes.
- Targets {6, 7, 17, 0} matched against every numeric leaf (exact), every string leaf (whole-string decimal and hex forms `0x6/0x06/0x07/0x11/0x00/06/07/11/00`), and word-boundary/literal-hex regexes; two implementations (Python scalar walk; jq `paths(scalars)`), plus a sensitivity control.

## Findings
- Exact numeric hits for {0,6,7,17} across all seven records: only r23 `normalized_result.artifact.bytes`=7 and `normalized_result.bytecode.bytes`=7. Both are the byte length of a 7-byte fixture, not a location; r23's own PUSH4 offset is 0. The 7 equals r22/r25/r26's PUSH4 offset only as a cross-record coincidence — no field of those three records holds 7.
- Exact string hits: none. No field is `"6"`, `"7"`, `"17"`, `"0"`, `"0x06"`, `"0x07"`, `"0x11"`, or `"0x00"`.
- Schema: the only offset-bearing keys are `raw_result.functions[].bytecodeOffset` and `normalized_result.functions[].bytecode_offset` = 16 (r19, r21), 30 and 32 (r22); absent in r23-r26 (empty `functions`). The complete numeric inventory is 22 fields: those offsets plus `artifact.bytes`/`bytecode.bytes` = 39/18, 18/18, 34/34, 7/7, 35/35, 19/19, 19/19.
- False-positive classes (reported so a raw grep is not mistaken for carriage): `$.provider.version` = `"evmole@0.9.3"` (all seven) matches `\b0\b`; r23 `bytecode.hex` = `63c0ffee005000` contains `00` at char 8 (last immediate byte, byte 4) and char 12 (STOP, byte 6), never at char 0 where the 0x63 sits; 64-hex `evidence_id` digests contain `6`/`7`/`17` substrings (r25 index 23, r26 index 46 for `17`) that are not tokens.
- For r19/r21/r22 the PUSH4 opcode sits at `bytecode.hex` char 12/12/14 and 34 and `functions[].selector` (`0xdeadbeef`, `0xaaaaaaaa`, `0xbbbbbbbb`) is the immediate — both are exactly what lines 29-30 already name; neither field states the offset.
- Sensitivity control: injecting `normalized_result.functions[0].push4_offset = 6` into an in-memory r19 copy was detected by the same filter, so the zero result is not vacuous.
- Entry block check: extracted `## Reproduce` (entry:105-137) runs `python3 -B` exit 0 on the archive and diffs byte-identical to `## Provenance` (entry:146-159), incl. `push4=[(6,'deadbeef')]`, `push4=[(7,'aaaaaaaa'),(17,'bbbbbbbb')]`, `push4=[(0,'c0ffee00')]`, `push4=[(7,'deadbeef')]`, `push4=[]`.

## Scope note (not a defect)
- The offsets are stated in round-directory prose, outside the record: `corpus/live/runs/round-19/reviewer.md:9` ("PUSH4 opcode `63` at **6**"), `round-22/reviewer.md:13-14` ("at 7"/"at 17"), `round-25/reviewer.md:9` ("opcode **7**"), and fixture `truth.json` `push4_opcode_offset` (r19 6, r22 7/17, r23 0, r25 7). These are lane notes/fixture truth, not REA record fields; the entry's subject is the record (`:1-7`, "saved REA outputs"), so no contradiction.
- Optional tightening only if the owner wants it sharper: after `:31` add "(no field states the offset; `bytecode.hex` and `functions[].selector` carry the code and the immediate)". Not needed for admission.

## Impact
- coverage: none lost; no harm trigger — records and fixtures unmodified (archive only), no hold lost, statement not over-claimed. Q11 for offsets 6/7/17 is met by the printed block; the negative half is confirmed by this out-of-entry exhaustive walk.

VERDICT: HOLDS — no field of any of the seven records states that record's PUSH4 offset (6; 7,17; 0; 7; 7); the only exact numeric hits are r23's byte-length 7s and every other hit is a non-locating coincidence (version string, hex byte pairs, digest substrings).
Installs: none (python3 3.14.8; `jq` resolves to jaq 3.1.1). Scratch: /tmp/revenger-r61w3-W3EvmPush4SiteAbsent.
