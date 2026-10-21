GRADE: HOLDS — round-62 candidate `corpus/knowledge/round-62-evm-dispatch-byte-evidence.md` (r23 slice: bytewalk, raw scan, empty record functions, flags/identifiers)

Frozen revision d97761952be256d145d298022de03091de91d358 (tree 45c4c5da82aae8ca2e44f6e3ed874a33533f54b9); claimbase 5bd4a90fc1a34caa94496601b60537b3aab12301; pre-registration a3498e25ad87bf756288812d0ea7c474b09433c7.
Candidate file sha256 6a1d394ad92fcaa5344069d1225e428988f1397e80c8968745d7b48bf43fed6e — byte-identical between the worktree and `git cat-file -p d9776195…:corpus/knowledge/round-62-evm-dispatch-byte-evidence.md`.
Seat scope: r23 only (bytewalk, raw 0x63/0x5b scan, empty saved functions, flags/identifiers). No repair, no admission.

## Observation

1. The candidate's own printed stdout is intact and reproducible. `corpus/knowledge/round-62-evm-dispatch-byte-evidence.md:291-423` is the `## Reproduce` fenced block; saved as `readout.py` (131 lines, sha256 740f321e97e28d7f11b4a58e106f054447a284519c59487398752bc87cd37eeb) and run against the extracted frozen archive — exit 0, stderr empty, Python 3.14.8:
   `python3 -B tmp/readout.py /fast/scratch/hyaku/revenger-r62/R62FEvmR23Empty` → 8 stdout lines.
   `diff` of that output against the entry's `## Provenance` block (file lines 442-449) → **0 bytes of difference** (diff exit 0). So the printed output is the recorded run's output at the frozen revision, not a claim about it.

2. r23 stated facts each carry an in-entry field (file `:445`, the r23 stdout line). My parser of the entry's own stdout block (`tmp/check_inentry.py`) resolves every cited path:
   - `:89-90` "r23 has raw `0x63` offset `[0]` and an empty JUMPDEST set" → `r23.raw_0x63_offsets` = `[0]`, `r23.valid_jumpdest_offsets` = `[]` (both present in that line).
   - `:92-93` "r23 … carry an empty normalized pair list" → `r23.candidate_pairs_normalized` = `[]`; the same line also carries `r23.candidate_pairs_raw` = `[]`.
   - Inventory rows `:259-261` (`[0]`, `[]`, `[]`) equal the in-entry values exactly.
   - All 34 inventory rows across the whole entry match the in-entry printed values (0 mismatches); all 35 cited `case.field` paths resolve inside the printed block. The single path my checker reported as absent is the template string `summary.field` in the inventory preamble, not a claim.

3. Independent re-derivation of r23 (my own walker, my own raw scan, my own record read; `tmp/indep_r23.py`, no reuse of the entry's code) from the archived fixture `corpus/fixtures/evm-r23/fixture.raw` (7 bytes, `63c0ffee005000`, sha256 8047ddff11234c2d36bd134cfb4aec669efa3ff89ed35a922552d44ebfe22f5a) and `corpus/live/runs/round-23/inspection.json` (sha256 ce9fe51536af461ef2deb19b8cf8ff3582dba736abc2747b07ab845d3aaac2af; identical in the frozen archive and the worktree):
   - instructions `[[0,99,"c0ffee00"],[5,80,""],[6,0,""]]`, opcode counts `{"0x0":1,"0x50":1,"0x63":1}`;
   - raw 0x63 offsets `[0]`, raw 0x5b offsets `[]`, valid JUMPDEST set `[]`, `jumpi_with_preceding_push1` `[]`;
   - saved record: `normalized_result.functions` = `[]` and `raw_result.functions` = `[]` (0 functions both sides);
   - flags `evidence_kind=inferred`, `discovery_completeness=unknown`, `runtime_execution=not-performed`;
   - identifiers `operation=inspect_evm_interface`, `provider_id=evmole-interface`, `provider_version=evmole@0.9.3`, `authority=shipped-artifact`, `confidence=inferred`, `evidence_id=ev_296e7ed723c7356b1cfbeee5dadc11283e5efe74535d544114ebf3b692f77201`, `bytecode.kind/deployment_authenticity/hardfork` = `unknown`/`unknown`/`unknown`.
   Every one of these equals the corresponding value in the entry's own printed r23 line. r23's record-level values are *in* the printed output (`r23.recorded.*`), so the entry's blanket "each record" statements (`:36-46`) are checkable in-entry for r23 as well, not only for the inventoried r19 rows.

4. Opcode constants and the jump-destination rule used by the r23 walk are as cited, re-opened read-only at the pinned tag (v2.20.0 → commit 2004296f2ffcbcebcd00f41152d33e8dfda0922a, confirmed via the GitHub refs API): `src/ethereum/forks/osaka/vm/instructions/__init__.py:55 EQ = 0x14`, `:104 STOP = 0x00`, `:106 JUMPI = 0x57`, `:109 JUMPDEST = 0x5B`, `:118 POP = 0x50`, `:121 PUSH0 = 0x5F`, `:122 PUSH1 = 0x60`, `:125 PUSH4 = 0x63`, `:153 PUSH32 = 0x7F`; `runtime.py:22 def get_valid_jump_destinations(code: Bytes) -> Set[Uint]:`, `:28` "The jump destination should have the `JUMPDEST` opcode (0x5B).", `:29-30` PUSH-N data exclusion, `:64 push_data_size = current_opcode.value - Ops.PUSH1.value + 1`. All nine opcode lines and all four runtime lines match the entry's `## Source facts` verbatim in value and line number.

5. Frozen-vs-base drift: `diff -r` of `corpus/fixtures/` and of `corpus/live/runs/` between the frozen archive (d9776195…) and the entry's stated lane base (a3498e25…) → both exit 0, empty. The r23 fixture and r23 record are byte-identical frozen/worktree. So the entry's `verified-at` base and the frozen candidate revision agree on the r23 inputs.

## Inference

- The r23 slice holds Q11 as the lane defines it: every r23 value asserted in prose is a field of the entry's own printed stdout, the printed stdout is byte-reproducible from the entry's own `## Reproduce` block on the frozen archive, and my independent bytewalk/raw scan/record read reaches the same values without borrowing the entry's code. No r23 value depends on external rederivation alone, and no token-presence substitute was used.

## Unknown

- Not mine to decide: whether the `## Unknown` list's omission of r24 from "Why r23, r25 and r26 report no pair" (`:139`) versus Observation 5's "four records that report no pair" (`:92`) is a wording gap or an intentional scope split. It touches no r23 value; the r24 slice has other seats. Flagged in-report only, no L1 message.
- Admission status, coverage-K counting and the README row remain L1's; this seat neither flips nor assumes them.

## VERDICT

HOLDS for the r23 slice of the frozen candidate: r23 bytewalk, raw 0x63/0x5b offsets, empty JUMPDEST set, empty saved functions, flags and identifiers are all present as in-entry printed output and independently reproduced on the frozen archive. No repair proposed; no admission assumed.

Installs: none (no package installed or updated; only read-only `curl` fetches of the pinned public spec files into own scratch, and stdlib-only Python).
Scratch: `/fast/scratch/hyaku/revenger-r62/R62FEvmR23Empty/` (archive extract + `tmp/readout.py`, `tmp/indep_r23.py`, `tmp/check_inentry.py`, `tmp/check_flags.py`, spec copies, stdout diffs). Only the assigned report was written.
