GRADE: HOLDS — held input bytes (corpus/live + corpus/fixtures) unchanged at frozen d97761952be256d145d298022de03091de91d358 vs base 5bd4a90fc1a34caa94496601b60537b3aab12301

Frozen: commit d97761952be256d145d298022de03091de91d358, tree 45c4c5da82aae8ca2e44f6e3ed874a33533f54b9, parent/prereg a3498e25ad87bf756288812d0ea7c474b09433c7; claim base 5bd4a90fc1a34caa94496601b60537b3aab12301. Candidate hashes at frozen (`git cat-file -p <rev>:<path> | sha256sum`; worktree clean): `round-62-commonjs-require-name-evidence.md` 42096e9676d33e25c3b6092e60fbd0fdacd699435ed9dc9db59ce24a1ceaaba3 (blob 480f62c4); `round-62-evm-dispatch-byte-evidence.md` 6a1d394ad92fcaa5344069d1225e428988f1397e80c8968745d7b48bf43fed6e (blob 3e58a91f). Scratch: `/fast/scratch/hyaku/revenger-r62/R62FHoldInputBytes/{frozen,base,tmp}`.

## Observation — assigned attack (tree/hash preservation)
1. `git rev-parse <rev>:corpus/live <rev>:corpus/fixtures` returned a35d30717a00250b0e8a884fd5ae402674609bea and c6287377454103866adea5b309850bf301279cc9 at base 5bd4a90, a3498e25 and frozen d977619: identical tree IDs.
2. `git diff --raw --no-renames 5bd4a90 d977619 -- corpus/live corpus/fixtures` printed nothing: no added, deleted or mode-changed entry. The same diff base→a3498e25 also printed nothing.
3. Full-file hashes: both revisions extracted by `git archive`; `find corpus/live corpus/fixtures -type f -print0 | sort -z | xargs -0 sha256sum`. 443 files each side (345 live, 98 fixtures); `cmp frozen.inputs.sha256 base.inputs.sha256` exit 0; both manifests sha256 52fb481ca8fb03182b51c6df3914b3f7f38be1f0d8fb448cfd1dfa7bd2dd8a5d.
4. Modes identical (`find -printf '%m %p'` | `cmp`, exit 0); 0 symlinks and 113 directories per side.
5. `git ls-tree -r <rev> -- corpus/live | sha256sum` = cf231e7426d9d2cfa9d943b539863744fa6eb48edbdf1038f1ccec88c389a5af; fixtures = ca1a1d038d422504ad20593152d8503ebd5d0bf13e701ac8c534bf4d0c5f3278; same at all three revisions.
6. Build `.ufo/waves/round-62/preservation/manifest.tsv` carries the same 443 rows; after extraction, `cmp manifest.inputs.sha256 frozen.inputs.sha256` exit 0.
7. `git status --porcelain -- corpus/live corpus/fixtures` empty (HEAD = frozen).
8. Entry code is read-only: `round-62-commonjs-require-name-evidence.md:117` `open(..., "rb")`; `round-62-evm-dispatch-byte-evidence.md:361,365,367` `.read_bytes()`; neither code contains write/unlink/rename/chmod/subprocess.

## Observation — entries checked against those bytes (supporting cross-check, not a Q11 audit)
9. JS file claims match `sha256sum`: js-r3 `index.js` 274 B f7d8bf470bb37d5eacedd7d571705bc80cc365195069ce1b7c6d4a24ae869fd7, `package.json` 85 B 92ef8e3d5d3af1c34282669efb259661ac0739e8630aca5972c92c03ea1096d7, `transform.js` 379 B cd9f3f633355d38c77dd0a26550d13b944b2502d4b0748f19607e36caa7fa345; js-r7-v2 `index.js` 209 B b53d96d432c120f6217a2da2ea3ed592308a3a23ef1a01745a22fd335ac4c42a plus the same 85 B / 379 B files; records 193573 B 7c3ba8c15673a7e48600bba3f42a6ca3935dbd75e30832569a631979e31ed452 and 171150 B 331ec252aefdc7715e49f039d7443736ff9560565f208f35b4c972bfe45d564e.
10. Saved JS import edges read back as claimed: `normalized_result.graph.edges` carry start/end.column 6/50, 28/50 (js-r3) and 6/40, 18/40 (js-r7-v2); line-1 text at those columns reproduces the entry's `span_text_from_fixture` strings.
11. EVM sizes/digests match `sha256sum` on fixture.hex/fixture.raw: r19 39 B 294e6fd2e041d5bea0558a26c1e399eddccf71bc0d279d398a4c0e915517b827; r21 18 B d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723; r22 34 B 94c1790f966b78a9a5cc61bdc9ad4b805aaea6989e37773f66ff433deeb1dbe2; r23 7 B 8047ddff11234c2d36bd134cfb4aec669efa3ff89ed35a922552d44ebfe22f5a; r24 35 B b69834e0ef786e3c001b2c833c8c0388acc017de14d06110cfa85d4948685d93; r25 19 B 2d87a4e203ebf590beab57cf7318ccf93c92035d7929d0bc16e6850433f5e8f7; r26 19 B ebe2d6757a7acd4c5b9de82441f66e70561350267114e445a2d6b8d037f8e97d. r19 record 4175 B e892dd18ff219f71ce2644a3f5a3e3ad3479d2ca46df9e2a7c260e7b33f15948.
12. Independent byte walk (my own script; no bytecode/fixture execution) reproduces entry items 4/6/7: r19 JUMPDEST [16], raw 0x63 [6], raw 0x5b [16], JUMPI at 14 operand 16 in set; r22 JUMPDEST [30,32], raw 0x63 [7,17], pairs 0xaaaaaaaa@30 / 0xbbbbbbbb@32; r23 raw 0x63 [0], JUMPDEST []; r24 counts {0x7f:1,0x50:1,0x0:1}, JUMPDEST [], pattern 63deadbeef14601057 once at offset 1 (span 1–9), PUSH1 opcode 7 / operand 8 = 16 / target byte offset 16 = 0x00 (not 0x5b); r25 JUMPI operand 16 not in [17]; r26 operand 17 in [17].
13. [Outside the assigned axis; observed, not adjudicated.] JS entry lines 34–35, 37 and inventory rows 264–265 attribute `span_1based_inclusive` / `span_text_from_fixture` to the saved edges ("all saved fields" at :264). The saved `location.value` objects hold only kind/source/start.column/end.column; `grep -c` for both names over both records returned 0. The readout synthesizes them at entry:146,148. Values have in-entry derivation/output; saved-vs-derived labelling is a Q11-seat question, no held byte affected.

## Inference
[INFERENCE] Items 1–5 mean the entries' claimed base a3498e25 and frozen d977619 cite/retain the same input bytes; the frozen delta adds only entry text, lesson, S028–S031 rows and wave/report material.
[INFERENCE] From the static code audit (item 8), neither readout can modify held inputs on its normal path; not demonstrated by executing their scripts.

## Unknown
- Q01–Q13 admission for either candidate: not asserted here; fresh Q seats and L1 decide.
- Reproduction stdout (JS claim `58b63dd9…`; EVM declares no stdout hash) was not re-run; reproduction seats own that check.
- Whether item 13's labelling is treated as a Q11 defect: unresolved here.

## VERDICT
HOLDS on the assigned attack: tree IDs, 443-file SHA-256 manifests, modes, symlink/dir counts and absence of add/delete/mode changes all match base 5bd4a90 at a3498e25 and frozen d977619; the new entries modify no `corpus/live` or `corpus/fixtures` byte. No Q failed on this axis. Not an admission and no coverage-map move; K remains 4/14 unless independent gates admit C04/C09.

Installs: none (no tool, package or version change).
