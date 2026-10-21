GRADE: PARTIAL — corpus/lessons/round-62.md learning/intake and M27 fix demonstration (Q11-class; no BROKEN contradiction)
Seat RevengerR61-2.R62FCriticLearning (critic, leaf). Frozen d97761952be256d145d298022de03091de91d358 (claimbase 5bd4a90fc1a34caa94496601b60537b3aab12301, prereg a3498e25ad87bf756288812d0ea7c474b09433c7), `git -C …/revenger-shokunin archive d977619… | tar -x` into /fast/scratch/hyaku/revenger-r62/R62FCriticLearning/tree, cwd=/, TMPDIR=…/R62FCriticLearning/tmp. Live-tree files cmp-identical to the archive.
SHA-256: lesson round-62.md cf0339ebe9baa95124da3b7f4345f8c8abf8c5b35541d3b9ace1b22a0449d6ae; C04 candidate 42096e9676d33e25c3b6092e60fbd0fdacd699435ed9dc9db59ce24a1ceaaba3; C09 candidate 6a1d394ad92fcaa5344069d1225e428988f1397e80c8968745d7b48bf43fed6e; claims.md 41cc8b7312969ee72b2470f0cdf9fecf89f4dd9bb8386b5144d68a99d6571c02.

## Q1. Outside Q11 disagreement learned, without claiming outside endorsement for the new drafts: HOLDS
- Intake source: lesson:10 cites `round-61-verifier-spotcheck.md:206-218`. All four routed groups (1 derive/label, 2a–2g, 3, 4) map to rows at lesson:14-29 with corrected, avoided, or unresolved dispositions. Row :16 says "Closure prose is not substituted for the derivation", which matches spotcheck:210 "Do not treat this closure's byte checks as missing in-entry derivations."
- No endorsement claim. Lesson:114-118 says "Not yet performed for round62 … Prior outside decisions are recorded above, not reused as current admission." `rg -i "outside|closure|spot-?check|hyaku|CloseMori|endors|non-author"` over both candidates, the lesson and claims.md finds only intake/source/non-reuse lines; the only candidate hit is C09:152 "outside this entry's claim". Neither candidate cites the closure or the rejected entries as support (C04:67 item 29; C09:182-183). The LOG round-62 declaration cites the outside lesson only for round-61 C1 falsification and routed debt.
- What was learned: the closure's disagreement with the initial C04 admit (spotcheck:143) is now captured as "Q11 already existed; admission failed to enforce it" (lesson:35). The process fix is that the author/corrector can't supply the admission recommendation (lesson:108-112).

## Q2. M27 red-before: HOLDS (independently reproduced)
Command: my `audit.py`. It extracts fenced blocks from the retained, byte-unchanged rejected entries (`git diff 5bd4a90 d977619` on both old entries, QUALITY.md and both round-61 lessons prints 0 lines). Output:
```
OLD commonjs-destructured-require-edges sha256 690db9f17ac2e64b35efeb90392fae3401ae8e14c843a1ac4eac6f240ef2a6f3
 pyblock ## Reproduce L97-149 53 lines; span-token lines 0 ; pattern-search tokens 0
  prose 83 entry's block carries those values.
OLD evm-saved-interface-candidates … pyblock ## Reproduce L111-143 33 lines; … pattern-search tokens 0
 outblock ## Provenance (Q11) r24: 'r24 bytes=35 sha256=b69834e0ef786e3c push4=[] raw_0x63=[1] jumpi(at,dest,valid)=[] jumpdest=[] entry_op=0x7f'
```
- The lesson:35 claims "zero location/start/span/column tokens" (C04) and "did not print r24 raw count/span/target" (C09) are true on the bytes.
- The evidence pointers resolve: `W3JsOverclaimCritic.md` 5-7 = BROKEN B1, 39 = "Q11 pass: FAILS"; `W3EvmR24Immediate.md` 16-21 = Q11 a–d plus self-check overstated; spotcheck 70-80 = the C04/C09 bullets.

## Q3. New green: the old-red values are now actually derived, not dropped from the prose, and no criterion is weakened (HOLDS for those values)
- QUALITY.md diff 5bd4a90→d977619: 0 lines (Q01–Q13, including the Q11 row at QUALITY.md:23, unchanged). No Q14 was added (lesson:93).
- Each readout block was extracted and run once on the archive:
  `c04 exit=0 stderr_bytes=0 lines=25 sha=58b63dd9d7c7ae4a0311ff33f12317345f7e5b7c9e8f204cfb13d1d599f0c416` (equals the C04:80 claim; block sha 31dac211…02ac equals the stated value); `c09 exit=0 stderr_bytes=0 lines=8 sha=aff3efda2691cb95ed7146292f602ba5dc5c40794e5c64efda3aaa7275f235bf`. Both stdouts are byte-identical to the embedded output. Equality alone isn't the pass basis; the semantic audit follows.
- C04 old red (edge spans), code read: C04:136-148 reads `evidence.location.value.start/end` for every `imports` edge and slices the fixture line; C04:179-184 derives the call/pattern/assignment spans from bytes. The output carries [28,50), [18,40), [6,50), [6,40) and the readback texts.
- C09 old red, four values, code read:
  - one PUSH32: `r24.instruction_opcode_counts {"0x7f":1}` (C09:381-383).
  - pattern key derived from r19 bytes: `derive_pattern`, C09:333-338, 361-362.
  - occurrence/span: `find` loop C09:341-345 → `occurrence_count 1, inclusive_spans [[1,9]]`.
  - raw 0x5B: `raw_0x5b_offsets []` (C09:409).
  - embedded target: C09:351-357 → operand 16, byte 0, `is_raw_0x5b false`.
  So the round-61 red class is answered by real in-entry derivations, not by removing the "carries" prose or weakening a criterion.

## PARTIAL findings (nonfatal for the lesson, but they block crediting the M27 fix)
P1 — The M27 "fix / falsifiable demonstration" contains no green result.
- lesson:35 gives the red-before plus "Fresh attack reviewers must audit … This fix is not yet credited at build stage."
- claims.md:66-68 asks for "a red-before missing-derivation exemplar and a tested fix".
- The lesson doesn't cite the retained synthetic red/green data (`.ufo/waves/round-62/counterexamples/`; `rg counterexamples lesson` finds nothing), and that data is "bounded synthetic-data experiment" per provenance.json.
- So it's honest but untested at the frozen state. [INFERENCE] The fix can only be credited after the fresh wave, with per-value results bound to exact candidate hashes.

P2 — Same-class residuals in the new entries at the frozen bytes. This is the strongest counterexample to crediting M27's fix as complete: correct values without an in-entry derivation or a recorded label.
- (a) C09:56-57 "a 39-byte `0x`-prefixed ASCII hex file".
  - The code (C09:362, 366) slices `[2:-1]` and never checks or prints the prefix; no output field carries the carrier's first bytes.
  - The value is true (`od -c fixture.hex`: `0 x 6 0 …` … `\n`), but it isn't derived.
- (b) C04 item 8/9 output label `span_1based_inclusive [1,7,1,50]` presents the saved line as 1-based.
  - The code (C04:148) slices the regex-hit `line` and never indexes by the saved `start.line`. So only the column base is shown, as item 11 itself limits it to ("The column base is not assumed"); the line base is assumed.
- (c) Weak: the C04 header and §Sources (C04:1, 248) give the S029 single-page SHA-256 `06db92a8…` with neither a derivation nor a "recorded" label. Admitted C01 (`pe-resource-directory-layout.md:1`) uses the same header-metadata convention.
- (d) Weak: C09:428 "Python 3.14.8" is unlabelled run metadata.
- Failed Q: Q11 under claims.md:97-98 ("every asserted value throughout the entry"). Item (a) is entry-level and is routed to the entry all-criteria seats; it isn't graded here.

P3 — Duplicate learning authority risk.
- M27's class and evidence repeat M26 (round-61.md:128: same W3JsOverclaimCritic/W3EvmR24Immediate reports, same Q11 capture). The lesson labels it "M26's continuation, not a new taxonomy", which is acceptable, but any mistake/class census must count one class, not two.
- The evidence cell "round61 closure :70-80" has no path. It resolves only through lesson:10.

P4 — The lesson's Gate audit text (lesson:97-101) is softer than the critic it cites.
- `R62CriticQ14.md:61-70` rule 2 ("code or comments never count") and rule 3 ("A recorded label requires a located field that holds the value") aren't carried over.
- Q11 itself is unchanged, so this isn't a criterion weakening. But it is the gap through which P2(c) passes.

## Observation / inference / unknown
- Observed: everything above (archive bytes, the audit.py output, the two runs, code line reads, the `od` dump).
- Inference: P1's crediting precondition; P2 as evidence that the build-stage inventory still lets underived format/convention values through.
- Unknown: the fresh-wave entry seats' Q11 decisions and the final L1 adjudication. I made no admission or K assumption; README C04/C09 remain `uncovered` (README:33, :38).

## Smallest safe correction (not applied)
- Keep M27's fix uncredited until the fresh-wave per-value results (old-red value → new derivation → output field, with exact candidate hashes) are appended to the lesson append-only.
- In the candidates: print the carrier's first two bytes, or label "0x-prefixed" as recorded. Index the saved `start.line` into the physical lines, or label the line base assumed. Label the S029 page digest "recorded (S029 row)". Then do a focused re-review by an existing fresh seat on the corrected hash.
- No QUALITY change.

VERDICT: PARTIAL — the intake and outside learning hold with no endorsement claim; the red-before is real; the new entries genuinely derive every old-red value under unchanged Q01–Q13. But M27's fix has no green result yet, and same-class underived values (C09 "0x-prefixed", C04 saved line base) remain at d977619.
Installs: none. Tools: git (rev-parse/archive/diff/log, read-only), python3 stdlib, rg, od, sha256sum, cmp. No fixture JS/EVM execution, no REA/provider/network calls. Scratch: /fast/scratch/hyaku/revenger-r62/R62FCriticLearning/{audit.py,c04_*,c09_*,tree/}.
