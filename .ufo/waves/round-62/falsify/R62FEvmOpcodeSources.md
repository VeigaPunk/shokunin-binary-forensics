GRADE: HOLDS — S028 opcode-source facts + source-snapshot manifest slice of corpus/knowledge/round-62-evm-dispatch-byte-evidence.md (C09 candidate)

Frozen target `d97761952be256d145d298022de03091de91d358` (claim base
`5bd4a90fc1a34caa94496601b60537b3aab12301`; pre-registration
`a3498e25ad87bf756288812d0ea7c474b09433c7`). Candidate SHA-256
`6a1d394ad92fcaa5344069d1225e428988f1397e80c8968745d7b48bf43fed6e` (worktree ==
archived tree). Archive: `git -C .../revenger-shokunin archive d9776195… | tar -x -C
/fast/scratch/hyaku/revenger-r62/R62FEvmOpcodeSources/rev`; all checks on archived copies,
cwd=<seat>/work, TMPDIR=<seat>/tmp. This report grades the source-fact slice only; it does
not decide whole-entry Q11 or admission.
## Observation (commands + exact output)
1. Pinned source bytes, read-only by commit on 2026-10-21:
   `curl .../execution-specs/2004296f2ffcbcebcd00f41152d33e8dfda0922a/src/ethereum/forks/osaka/vm/instructions/__init__.py`
   → 10700 B, sha256 `49dd6155c7560811a8f546ea9c5a29678e3a3da859216e2ee48cfacaa5b63724`, 367 lines.
   `.../vm/runtime.py` → 1971 B, sha256 `a2801c4169b806a9494707179a9df20170a37a1769596aac56013ddba509aef8`, 69 lines.
   The held snapshot copies are byte-identical; `.ufo/waves/round-62/source-snapshots/manifest.json`
   (sha256 `cd26810aeecf4ea7f0824f5ef88e16176541c439eedcde8fe2cf36f67c057c4b`) declares the same
   sizes/hashes/access date; `corpus/SOURCES.md:42` states the same pair "respectively".
2. Tag identity: `git ls-remote https://github.com/ethereum/execution-specs 'refs/tags/v2.20.0*'` →
   `67f038c8c3fced0b388cfdcaed5c4a52d5fad2fd refs/tags/v2.20.0`
   `2004296f2ffcbcebcd00f41152d33e8dfda0922a refs/tags/v2.20.0^{}`
   The header's "tag v2.20.0, commit 2004296f…" is the dereferenced commit, not the tag object.
3. All nine cited opcode lines, `sed -n '<n>p'` on the snapshot:
   `55 EQ = 0x14`; `104 STOP = 0x00`; `106 JUMPI = 0x57`; `109 JUMPDEST = 0x5B`;
   `118 POP = 0x50`; `121 PUSH0 = 0x5F`; `122 PUSH1 = 0x60`; `125 PUSH4 = 0x63`;
   `153 PUSH32 = 0x7F`. Exact.
4. Runtime anchors: `22 def get_valid_jump_destinations(code: Bytes) -> Set[Uint]:`;
   `28 * The jump destination should have the \`JUMPDEST\` opcode (0x5B).`;
   `29-30 * The jump destination shouldn't be part of the data corresponding to` /
   `  \`PUSH-N\` opcodes.`; `64 push_data_size = current_opcode.value - Ops.PUSH1.value + 1`.
   Exact; function span 22-69.
5. Enum check: `class Ops(enum.Enum)` with literal assignments; PUSH1..PUSH32 are contiguous
   0x60..0x7F at lines 122-153. The readout hardcodes 0x60/0x63/0x7F/0x57/0x5B and the
   `op - 0x5F` size arithmetic; it never constructs `Ops` or uses enum membership/ordering.
   The Source facts label the constants recorded; no gas, stack or jump-acceptance semantics
   is taken from the enum.
6. Manifest comparison: stored files re-hash to `49dd…`/`a280…`; manifest entries give the same
   sizes/hashes; the S028 row's two SHA-256 values match both. No mismatch.
7. Readout reproduction: extracted the `## Reproduce` block verbatim; `python3 -B readout.py ../rev`
   → exit 0, stderr 0 bytes, 8 stdout lines (15556 B); `diff -u provenance.txt stdout.txt` empty.
   Same run against the `a3498e25` extraction → exit 0, stderr 0, diff empty. The Provenance
   "exact, complete and untruncated" claim holds for this block.
8. Byte stability: `git diff --stat a3498e25 d9776195 -- corpus/fixtures/evm-r19 … evm-r26
   corpus/live/runs/round-19 … round-26` is empty for all seven fixture and seven run dirs;
   only `corpus/SOURCES.md` (+9) and the new knowledge file differ. r19 `fixture.hex` is
   literally `30 78` + 36 hex + `0a` (39 B), so "0x-prefixed ASCII hex" is byte-true.
9. Inventory aid: 67/67 rows in `## Evidence inventory` resolve in the printed stdout with
   identical values (parsed-row comparison to the 8 JSON lines). This is an aid, not the
   semantic audit; the item-by-item derivations were checked by hand against the block.

## Inference

- Every cited S028 opcode constant/line and runtime quote is exact at the claimed tag/commit;
  the file digests, sizes, snapshot manifest and S028 row agree with the upstream bytes.
  No enum assignment is used as execution semantics.
- Q11 for this slice: the source constants are explicitly labeled recorded (not re-derived),
  and the byte-derived values used here (instruction walk, raw 0x63/0x5b offsets, JUMPDEST
  sets, r24 occurrence/span/target) are produced by the in-entry readout and printed in
  `## Provenance`. No source-fact value in this slice is correct-but-underived.

## Unknown / outside this slice

- Whole-entry Q11 is not adjudicated here. I did not grade the r24 "PUSH1 opcode byte" role
  wording, the plural "files' own bytes" pattern-derivation scope, the unprinted
  dispatch/argument/state-mutability labels, or inventory rows that name one field for a
  multi-field claim; those are not source-fact values and a separate fresh-wave seat owns them.
- No producer, chain/RPC, EVM execution or fixture JS was used. No post-v2.20.0 release state
  was queried.

## Non-fatal observations (no value conflict)

- The readout's header comment names only EQ/JUMPI/JUMPDEST/PUSH4, while the walk also uses
  PUSH1/PUSH32; the `## Source facts` block lists both, so the constants are not smuggled.
- The manifest URL uses the mutable tag ref while the S028 row pins the commit; the tag peels
  to the pinned commit, and the commit fetch matches the stored snapshot.
- The manifest's origin sentence ("copied byte-exact by L1") is not byte-verifiable; byte
  equality to the commit fetch and to the S028 digests is confirmed.

VERDICT: HOLDS for the S028 opcode-source/manifest slice. No repair, no admission, no README
flip. Installs/updates: none; python3 3.14.8, git, curl, sha256sum, sed/awk pre-existing.
