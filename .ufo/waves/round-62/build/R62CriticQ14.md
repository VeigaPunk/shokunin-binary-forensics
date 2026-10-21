RESULT: COMPLETE

# R62CriticQ14 — would a factual-value inventory enforce Q11 or offer an easier second method?

Frozen revision `a3498e25ad87bf756288812d0ea7c474b09433c7` (git archive to
`/fast/scratch/hyaku/revenger-r62/R62CriticQ14/`; all checks ran with cwd=/).
Proposal artifact: `/fast/scratch/hyaku/revenger-r62/R62CriticQ14/R62CriticQ14-proposal.md`.

## Verdict
As a rule, Q14 is redundant with Q11. If it is applied mechanically (by value
presence), it becomes an easier second method. Q11 (`corpus/QUALITY.md` Q11 row) already requires each count,
identifier, offset and digest to carry an in-entry command and its output, and
already rejects underived values and recorded values presented as re-derived.
History: M20 (`lessons/round-1.md:131`) introduced Q11 for this same class, and
M26 (`lessons/round-61.md:128`) recurred under Q11 because the author's
one-line "Q11 pass | every count... carries the command" self-attestation was
accepted (rejected entries' QUALITY tables, C09:193, C04:206). An author-made
inventory is the same self-attestation at a finer grain. The failure was in
enforcement, so another criterion does not address it.

## Counterexample (strongest): the proposed triage tool is silent on Q11 rejects
Target: `R62Q11InventoryRule/q14_inventory.py`, sha256 `6d56aeed00a826e8ec320e72fff22e1282de8a59c03734a61d0fc02d02948562`.
Mutants are single-replacement copies of the frozen entries (`make_mutants.py`, asserted count 1):
```text
frozen C09: OUTPUT-ABSENT-HEX=2 (0x10, 0x5B @L63) GAP-NO-DERIVATION=1 ('289') GAP-CLASS=2
m1 target 0x10->16:          OUTPUT-ABSENT-HEX=1   (0x10 flag gone; '16' matched r19/r21/r25 output lines)
m2 r24 values into a table:  counts unchanged      (table values 0x10, 0, 1..9 never scanned)
m3 add "(fixture recorded in truth.json)": 0x10, 0x5B -> RECORDED-LABELLED
frozen C04: GAP-CLASS-NOT-DERIVED=1 ('span' @L80)
m4 code comment "# edge spans": summary empty (0 findings)
grep "one PUSH32|three named|four seats" in all outputs: 0
```
In my own scan (`inventory_scan.py`), `'37' output_substring=True whole_token=False` and
`'9' output_substring=True whole_token=False`: the frozen "none of 37" and "[1, 9]"
values pass substring matching because the digits occur inside hex digests.
Byte readout of r24: `len=35 op0=0x7f pattern_starts=[1] span=[[1, 9]]
raw_0x5b_count=0 raw_0x7f_count=1 embedded_push1_operand=0x10=16`. `truth.json`
has no 0x5B-count or target field, so m3's recorded label is false provenance,
and a premise taken from authoring intent also fails Q06.

## Second counterexample: correct output, wrong derivation
`R62InventoryRedExemplar/fix-c09-block.py` computes `target_is_jumpdest` as
`target in (0x5b,) or (starts[0]+7) in jd`, which tests offset 8 rather than target 16:
```text
frozen   target,checked_offset,expr,byte_at_target_is_5b = (16, 8, False, False)
byte16=5b target,checked_offset,expr,byte_at_target_is_5b = (16, 8, False, True)
```
The output equals the expected `False` on the frozen bytes, so matching outputs would
accept it. This is M26 again ("successful output mistaken for derivation").
Both owners were messaged.

## Impacted axes
- coverage: a value-presence Q14 pass on an underived entry would replay the
  round-61 provisional K 6/14 followed by rollback to 4/14. C1 is admitted only after
  the fresh falsify wave; none is claimed here.
- calibration/discernment: duplicate authority. If Q14 and Q11 wordings drift
  apart, reviewers may score the weaker one. QUALITY's supersession rule expects new rows
  to name the row they replace.
- None for README: C04/C09 stay uncovered. This seat makes no held or admission claim.

## Smallest safe correction (details and exemplars E1–E7, R1–R4 in the proposal)
Add no Q14 row. Record a non-author Q11 audit method in the round-62 lesson
`## Gate` with four rules:
1. Enumerate values from all entry text, including tables, headers, blockquotes, word
   numerals and "block carries X" claims.
2. Link each value to a printed output line from the same record and method;
   code or comments never count.
3. A recorded label requires a located field that holds the value, and is never
   used for a Q03 expected value or a Q06 premise.
4. Triage-tool silence is not evidence.
If L1 adopts Q14 anyway, it must state "Q14 pass never implies Q11 pass" and
carry these four rules. This is a fixable defect, not a tradeoff.

## Unknowns
- Whether L1 intends `q14_inventory.py` as more than advisory. It always
  exits 0. My attack is on any reliance on its silence.
- Whether the new round-62 candidate entries exist yet: neither was present in
  the frozen tree or in live `corpus/knowledge`, so E1–E7 target round-61 text and mutants.
- Side note: the tool also gave a false positive, flagging 'location' at C09:31,
  which is a negated statement. Noise like this trains reviewers to ignore class gaps.

## Scope kept
Read-only on frozen copies and the sibling's script. No fixture JS or EVM was run, no producers,
no corpus/live, fixtures or README edits. Prior rejected entries and counterexamples are unchanged.

Installs: none.

## Addendum — re-check of the sibling's E7 correction (appended; text above unchanged)
The sibling reported fixing E7 in `R62InventoryRedExemplar/fix_c09_block.py`
(sha256 `a2dc2d44f827b8d4fabadf60405422e81436db7fc22bdc81d5fed9549b6a57dc`), with test
`test-fix-c09.py` (`4b78be85f5d35d495e059065f0f22b4c6051cea6efdaf6a2cfa5138d8be96aa4`).
Run from the frozen archive root with that directory on PYTHONPATH:
```text
M0 baseline: OK [(1, 9)] 0x10 False
M1 byte16=0x5b -> ... target_position_is_jumpdest=True  OK
M2a byte8=0x11 (pattern byte) -> occurrence_count=0 inclusive_spans=[]  OK
AssertionError at line 49 (M2b)                      exit=1
M3 actual 2 [(0, 8), (10, 18)]      (test asserts [(0, 8), (1, 9)])
M2b actual target None tpos -1 flag False
M1 flag True push32_spans [(0, 1, 33)] instruction_starts [0, 33, 34] valid_jumpdest(S016) [] 16_is_valid False
```
Status: not fixed.
1. The test exits 1 at M2b, and M3's expected spans are wrong. The sibling's summary
   ("M2 target 0x11, position 17") matches neither the file nor the run.
2. `target_position_is_jumpdest` is computed as "byte at target == 0x5B". In M1,
   byte 16 lies inside the PUSH32 immediate, so S016 makes it not a valid JUMPDEST,
   yet the test asserts True. That is the raw-vs-instruction confusion the claims
   ask candidates to make explicit (claims.md C09 bullet).
Fix: rename the field to `byte_at_target_is_0x5b`, or compute validity over instruction
starts. Sibling messaged. This supports rule 2 of the correction: link a value to
output from the same method, and don't trust a reported test result without running it.

## Addendum 2 — re-check of the second revision (appended; text above unchanged)
`fix_c09_block.py` `2e95f1c45362e4e5e217e834229a7fc206e963dae81c651e7ac014c1293aaaab` and
`test-fix-c09.py` `f74f5a9fe8ddbed404e65294ad668a1b5c4ca6ec6ff7b7e571f1588eef2c2ee3`:
both exit 0 from the frozen root, and the printed r24 values match the sibling's
message. The raw-byte and instruction-level fields are now separate. My own mutants:
```text
X1 len 17 offsets [0, 5, 6, 8, 9, ..., 16] valid [16] emb_valid True jumpi [(8, 16, True)]
X2 raw_5b [16] byte_at_target_is_5b True valid [] emb_valid False
r19 decoded len 18 pattern_in_r19_at [6]
```
X1 puts the pattern in executable code with a JUMPDEST instruction at 16. X2 hides a
0x5B at 16 inside a PUSH2 immediate. Both give the S016-correct result, so E7 is
resolved as a scratch exemplar. It is not admission evidence, and no corpus file changed.
Two gaps remain for any candidate that uses this block:
- `PATTERN` is a constant taken from truth.json `embedded_pattern_hex`. The entry must
  label it a recorded search key; only the counts and spans are derived from it.
- C09:39 "immediate contains the r19 pattern" is still underived in-block, because the
  script never reads r19. My check finds the pattern at decoded r19 offset 6, but that
  result must be printed in-entry or the wording dropped.

## Addendum 3 — re-attack of the Q14 helper v2 (appended; text above unchanged)
Target: `R62Q11InventoryRule/q14_inventory.py` v2, sha256
`39d37fc372c81010fda0812114d414840d4d9733b7ea048c1d2100fdcbad7111`; proposal
`R62Q11InventoryRule/Q14-proposal.md`. Builder `make_mutants_v2.py`, outputs `out2-*.txt`.
My original mutants m1–m4 and the 37/9 cases now produce findings, as claimed.
Controls: the v0 inventory row flags `0x10` at :63, a6c flags plain `16`, and
frozen C04 gives GAP-COVERAGE=2. New silent Q11 rejects:
```text
a3  honest r19 row "dest=16" + r24 target written 16   -> no :63 '16' finding (one global token set)
a1  untagged laundering row "embedded JUMPI target 16" -> only ROW-NOT-IN-CODE-PRINT 'dest', identical to honest v0
a6b "embedded JUMPI target (fixture.raw:16)"           -> '16' dropped as a locator (a6c plain 16: flagged)
a5  "(S016)" added to the r24 sentence                 -> 0x10, 0x5B downgraded to SOURCE-QUOTED
a7b "embedded target 0x10 | recorded: LOG.md"          -> silent; LOG.md holds 0x10 only in r19 notes
a7  truth.json recorded row                            -> flagged only for 'r24' in the path, not for the value 0
a8  C04 "block carries" -> "entry covers"              -> GAP-COVERAGE 2 -> 0
a9  C04 "edge spans" -> "edge positions"               -> GAP-COVERAGE 2 -> 0
```
Also, §6 of the proposal skips the header block and the QUALITY table "by design",
which contradicts rule 1 as adopted in §3: C09:195 "0/37" is never enumerated.
Assessment: v2 matches tokens against the author's own inventory and against whole
record files. That re-creates E1 (any row anywhere vouches for a token) and E6
(a record holds the token in an unrelated field). This confirms the main verdict: a
lexical helper can only triage, and its silence is not evidence (rule 4). If Q14 lands,
§6 must list these classes as known-silent and drop or state the header/QUALITY-table
exception. Owner messaged. No corpus edit; C04/C09 stay uncovered.

## Addendum 4 — re-attack of the helper v3 (appended; text above unchanged)
v3 sha256 `db367ef4c879888724426eb156c285a7b890a62fb03e5f7e9d8d0a06a6e4c500`.
All of m1–m4 and a1–a9 now produce findings at the target lines (`out3-*.txt`).
New silent Q11 rejects (`make_mutants_v3.py`, `mutants-v3/`):
```text
b3  row "r22 bytes 30 | bytes=30" (output: r22 bytes=34)    -> no finding; 30 sits in jumpdest=[30, 32] on the same line
b1  r24 sentence adds "unlike r19" + honest r19 row 16    -> r24 '16' at :63 silent (tag union)
b4  "raw 0x5B count 0 | recorded: truth.json field count" -> silent; 'count' substring-matches executable_push4_count: 0
b6  C04 print('edge spans: carried by the saved records') -> GAP-COVERAGE 2 -> 0
```
b3 is a plain mismatch, the case the proposed row text names as a reject, so it is a
helper bug rather than a known-silent class. In three successive rounds, every
named mutant was closed and new silent ones appeared. That pattern is the evidence
for the main verdict: the helper is triage, and the non-author Q11 audit stays the
only admission condition. I stopped attacking at this point. Owner messaged.

## Addendum 5 — v4 regression check only (appended; no new mutant round)
v4 sha256 `55d9439c3dbba9568a380ec9904b37eb6d85e2e50dab12a0915dab8ce43e20b8`; proposal
sha256 `6610ccaa2c7eb5ddabbfb1f744c6b5f26abc3a2f2c1a31200318205ab81eace8`.
All 19 targets produce findings at the target lines: m1–m4; v0; a1, a3, a5, a6b, a7,
a7b, a8, a9; b1, b3, b4, b6; frozen C04 and C09 (`out4-*.txt`). The honest v0 control
shows 0 false ROW-NOT-IN-CODE-PRINT findings. The proposal carries "Q14 never implies a
Q11 pass; Q14 rejects whenever Q11 rejects" in the row (:63) and in §6 item 10, and §2
records the no-row position verbatim.
Final verdict unchanged: the preferred outcome is no Q14 row and the non-author Q11
audit in the round-62 lesson's Gate section. If L1 adds a Q14 row, it is acceptable
only with that condition and the ten known-silent classes in §6. Not checked: new
mutants beyond v3's set, which the owner agrees stay open. C04/C09 stay uncovered;
README is not marked held.

## Addendum 6 — closing check (appended)
Verified digests: proposal `d2bca232f4686c997867d04b508b5820b4b0da5077bfe2981f733eecae1dc926`,
owner report `24df50771c2d3d7532da82322f57d322c9eec0a881f4c9d1d7f355459da3bc7f` (55 lines),
helper unchanged `55d9439c…`. Proposal §2 now says the mutant findings are command
coverage, **not** an endorsement of the row, and records "prefer no Q14 row". The §5.4
heading says "command coverage, not row validation". The owner report states "not a
validation of the row" and "only with the conditional". Both sides are closed.
