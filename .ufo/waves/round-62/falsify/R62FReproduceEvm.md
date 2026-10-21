GRADE: HOLDS — round-62 C09 candidate `corpus/knowledge/round-62-evm-dispatch-byte-evidence.md` reproduces byte-exactly on two distinct archive roots; no contradiction, no missing requirement.

Frozen revision under attack: d97761952be256d145d298022de03091de91d358 (claimbase 5bd4a90fc1a34caa94496601b60537b3aab12301, pre-registration a3498e25ad87bf756288812d0ea7c474b09433c7).
Target file sha256 6a1d394ad92fcaa5344069d1225e428988f1397e80c8968745d7b48bf43fed6e — archive copy and working-tree copy byte-identical (`sha256sum` both, no diff).

## Method (own scratch only)
Scratch root: /fast/scratch/hyaku/revenger-r62/R62FReproduceEvm (TMPDIR=…/tmp). Archived copies only:
`git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive d97761952be256d145d298022de03091de91d358 | sha256sum` → 4b52df49bbd6349d6ac8c45c4f7d73d9e7125c7f719950e89818cad21dc8cebc.
Extracted blocks from the frozen entry: `## Reproduce` python block = lines 292-422 → readout.py (sha256 740f321e97e28d7f11b4a58e106f054447a284519c59487398752bc87cd37eeb); `## Provenance` stdout block = lines 442-449 → provenance_stdout.txt (sha256 aff3efda2691cb95ed7146292f602ba5dc5c40794e5c64efda3aaa7275f235bf). No entry file was edited.

## Primary evidence — runs (cwd=/, python3 3.14.8, matching the entry's Provenance header)
| root | exit | stderr | stdout sha256 |
|---|---|---|---|
| r1 = scratch root (d977619 archive in place) | 0 | 0 bytes | aff3efda2691cb95ed7146292f602ba5dc5c40794e5c64efda3aaa7275f235bf |
| r2 = …/tmp/alt-root-aaa/bbb/archive-root (same archive, different path) | 0 | 0 bytes | aff3efda2691cb95ed7146292f602ba5dc5c40794e5c64efda3aaa7275f235bf |
| r3 = …/tmp/root3 (fresh extract, pristine) | 0 | 0 bytes | aff3efda2691cb95ed7146292f602ba5dc5c40794e5c64efda3aaa7275f235bf |
| r4 = …/tmp/minimal-root (only corpus/fixtures + corpus/live) | 0 | 0 bytes | aff3efda2691cb95ed7146292f602ba5dc5c40794e5c64efda3aaa7275f235bf |
| r5 = …/tmp/base-a3498e25 (archive of the entry's stated lane base) | 0 | 0 bytes | aff3efda2691cb95ed7146292f602ba5dc5c40794e5c64efda3aaa7275f235bf |
| r2 re-run under `unshare -rn` (no network namespace) | 0 | 0 bytes | aff3efda2691cb95ed7146292f602ba5dc5c40794e5c64efda3aaa7275f235bf |

`cmp run_root1.stdout provenance_stdout.txt` → identical (15556 bytes, 8 lines). `cmp run_root2.stdout provenance_stdout.txt` → identical. `diff run_root1.stdout run_root2.stdout` → identical. Root-path independence: reproduced stdout is byte-identical across r1…r5 (different path depths, different tree contents, different base revision), so no absolute path leaks into the output.

## Root-path independence / no missing external file dependency
- r4 contains only `corpus/fixtures/` and `corpus/live/` copied out of the archive; it reproduces the same sha256 → the readout's whole dependency set is inside `<root>/corpus/{fixtures,live}`.
- `strace -f -e trace=openat,open,socket,connect,execve` on the r3 run: `socket()`/`connect()` count = 0; distinct corpus paths opened = 14 (7 fixtures evm-r19/21/22/23/24/25/26 + 7 records round-19/21/22/23/24/25/26 `inspection.json`); corpus opens carrying O_WRONLY/O_RDWR/O_CREAT/O_TRUNC = 0. Static scan of readout.py: imports only `hashlib, json, sys, pathlib`; no socket/subprocess/eval/open-write.
- r3 tree manifest (path+size of every file) identical before and after the run (0b2f0e135b27b015f198f6b767698eae601b96be3a85c388063991c2556ec9b0 both) → the run wrote nothing.
- Entry's "no bytecode executed, no chain or RPC, no producer called" claim: consistent with the trace (0 sockets) and the code (byte walk only, no interpreter).

## Q11 spot-audit (values must have a true in-entry derivation + output, not just be printed)
- Machine check of the entry's own `## Evidence inventory` table against the reproduced stdout: 67 rows parsed, `MATCH=67 MISMATCH=0` (script: scratch `check_inventory.py`; each row's `case.field` path resolved in the reproduced JSON and compared to the stated value).
- Each inventory field is computed by the block, not copied: counts from `walk()`/`len(CASES)`, digests from `sha256()` over the actual bytes, scopes from `referent()`, pattern/spans/embedded offsets from `derive_pattern()`+`pattern_block()`, record fields read from the saved JSON.
- Prose cross-check (Observation §1-§7, Inference) against reproduced output: r19 instruction tuples = 11; per-case normalized pair counts {r19:1, r21:1, r22:2, r23..r26:0}; summary {total_cases 7, reported_candidate_observations 4, distinct_candidate_pairs 3, distinct_pairs [["0xaaaaaaaa",30],["0xbbbbbbbb",32],["0xdeadbeef",16]], raw_and_normalized_pair_counts_equal true, pattern_hex 63deadbeef14601057, pattern_length 9}; r24 pattern {occurrence_count 1, starts [1], spans [[1,9]], push1 opcode 7 / operand 8 / value 16, target offset 16, target byte 0, is_raw_0x5b false}; r24 opcode counts {0x0:1, 0x50:1, 0x7f:1}; r19 raw_0x5b [16], r22 raw_0x5b [30,32]; r25 jumpi [[15,16,false]], r26 jumpi [[15,17,true]]; r21.carrier.sha256 == r19.decoded.sha256; all seven records' bytecode kind/hardfork/deployment_authenticity == "unknown". All agree with the entry's prose and inventory.

## Observation
1. The entry's `## Provenance` stdout is genuinely exact, complete and untruncated (the "…" truncations seen by a naive reader are a display artifact of the reading tool; the file's lines 442-449 are 1970-2459 chars and are reproduced byte-for-byte).
2. The entry's stated provenance parameters (lane base a3498e25, Python 3.14.8, cwd `/`, exit 0, stderr empty) are all confirmed; output is additionally invariant under the frozen d977619 base.
3. The `## Reproduce` block is complete and self-contained: extracted it parses (ast.parse OK), runs stdlib-only, and needs nothing outside the archive root.

## Inference
- The C09 candidate's values are derived in-entry, not merely printed: the reproduced run re-derives every inventory row from the fixture bytes and the saved records, and the derived values coincide with the recorded ones. Q11 therefore is not failed by this candidate on the reproduce axis; nothing observed here contradicts its Observation/Inference/Unknown text.
- No coverage row, README row, or admission status was flipped by this seat; the entry remains `admission-status: candidate` and the L1 gate decides.

## Unknown
- Whether the saved records' own fields (provider id/version, evidence_id, authority, confidence) are authentic remains outside this entry's claim and outside this reproduce check — I read them, I did not authenticate them.
- Whether `valid_jumpdest_offsets` matches the upstream spec function `get_valid_jump_destinations` exactly was not re-derived here (the entry itself labels the walk as manual and does not claim spec-function identity).
- I did not re-verify the S028 source-row quotes (external read-only spec) — out of this seat's assignment.

## Installs
None. No package install or update was needed or performed; system state unchanged (no pacman transaction, no service action).

## VERDICT
HOLDS. The C09 candidate's `## Reproduce` block, run read-only on archived copies of the frozen revision at two distinct archive-root paths (plus three additional roots: fresh extract, minimal corpus-only tree, and the entry's own stated base a3498e25), exits 0 with empty stderr and produces stdout byte-identical to the in-entry `## Provenance` block (sha256 aff3efda2691cb95ed7146292f602ba5dc5c40794e5c64efda3aaa7275f235bf, 15556 bytes, 8 lines). No missing external file dependency (0 sockets, 14 read-only corpus paths, minimal-tree reproduction), no write side effects, and all 67 evidence-inventory rows plus every prose value in Observation/Inference re-derive from the archived bytes/records. No correction needed; no repair attempted. Focused transcript: /fast/scratch/hyaku/revenger-r62/R62FReproduceEvm/transcript.txt.
