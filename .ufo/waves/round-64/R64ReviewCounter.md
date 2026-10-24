# R64ReviewCounter — counter/contract drift review

Seat scope: read `reports/round-64/claims.md` against `reports/round-64/measure.py`
side by side; verify each frozen label computes the sentence it is bound to;
reproduce the red-before values from a committed base archive. No lane file was
edited; all mutation work happened under `/tmp/revenger-r64-reviewcounter-*`.
No tool was installed or updated (no pacman, no uv/npx).

## Axes (godspeed)

1. **Predicate identity** — does every frozen label compute exactly the
   registered sentence (regex, map, attribution token, hold formulas)?
2. **Red-before fidelity** — does the counter on `git archive 666ea84b corpus`
   reproduce `measure-before.log` byte-for-byte and exit 0?
3. **Post-claim dynamics** — does C4 land `2/2` attributed, and does C07 walk
   both registered branches (`→held` admit, `→uncovered` fallback) without
   moving any other label?
4. **Evidence provenance** — do claimed after-state pins match final bytes?

## Verdict

Red-before is **exact** (empty diff, exit 0); the C4 fix on final bytes yields
`C4_RECEIPT_KILLED_ATTRIBUTED=2/2` with the frozen endswith token; both C07
branches move `README_TOKEN_LEGEND_MISMATCH` to 0 as registered. Two medium
drifts found (HOLDS_OK_V2 definition; a stale after-state pin caused by an
editing-window transient) and four low drifts. No drift changes a promised
red-before value.

## Verified conformance (evidence)

| Claim in `claims.md` | Observation |
|---|---|
| frozen counter at pre-registration | `reports/round-64/measure.py` sha256 `b8e68d326c28690274be98ac35a518970d84aa8b9892b5736450a776210b9168`; introduced by `3bb430f`; worktree clean at HEAD `a3d063f` |
| round-63 probe and pinned SHA untouched | `reports/round-63/measure.py` sha256 `3b7fba2d5243bbe0b723a99a53085130ff97010e23c8a59a8027f5f8992c5908`, identical to `git show 666ea84b:reports/round-63/measure.py` |
| do-nothing control values (`:103-106`) | `git archive 666ea84b corpus` → `/tmp/revenger-r64-reviewcounter-base`; probe run from `cwd=/`; **output diff vs `measure-before.log` is empty**, exit 0. Printed: `K_HELD=7/14`, `K_ROW C07 status=frontier`, `K_HELD_BACKED=7/14`, `K_HELD_BACKED_STRICT=7/14`, `SAVED_RECORDS=59`, `README_TOKEN_LEGEND_MISMATCH=1 rows=['C07']`, `F_COVERAGE=5/8`, `FRESH_ROWS=18/18`, `C2_*` 2/2 (raw and attributed), `C3_*` 2/2, `C4_CONTROLS_PASS=2/2`, `C4_RECEIPT_KILLED_ATTRIBUTED=0/2`, `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`, `HOLDS_OK=yes`, `HOLDS_OK_V2=no` |
| `K_HELD_BACKED` "same regex as round-63" (`:87`) | byte-identical expressions: `\| held \|$`, `knowledge/[\w.-]+\.md` over `l.split("|")[3]` (README header confirms column 3 = knowledge entries); 14 rows counted |
| C4 mutation sentence and attribution token (`:73-75`, `:61-67`) | `C4_CLAUSE` measure.py:212 is `receipt\['stdout_sha256'\]\s*==\s*H\(raw_bytes\)`, deleted with one connecting `and`, exactly-one-match guard; attribution at :247 is `last.endswith("forged receipt stdout accepted")` — observed last lines `AssertionError: r47: forged receipt stdout accepted` / `r42: …` |
| C4 fix shape, existing controls stay (`:57-84`) | final diff vs `666ea84b` is **additive-only** (+3 lines each); existing forged-command require retained (one occurrence of `forged receipt command accepted` per script); new token occurs once per script; clause occurs once per script and inside `receipt_ok` (:120/:123) |
| C2 red-before 0/2 → attributed 2/2 at final | counter on current tree: `C2_RECEIPT_B_KILLED=2/2`, `C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2`, `C4_CONTROLS_PASS=2/2`, `C4_RECEIPT_KILLED_ATTRIBUTED=2/2`, `HOLDS_OK=yes`, exit 0 |
| C07 `frontier→held` on admission, K ≥ 8/14 (`:39-51`) | scratch admit tree (new knowledge file + README C07 held): `K_HELD=8/14 score=5.7`, `K_HELD_BACKED=8/14`, `K_HELD_BACKED_STRICT=8/14`, `README_TOKEN_LEGEND_MISMATCH=0 rows=[]`, `HOLDS_OK_V2=yes`, exit 0 |
| C07 `frontier→uncovered` fallback | scratch uncovered tree (C07 status `uncovered`): `README_TOKEN_LEGEND_MISMATCH=0 rows=[]`, `K_HELD=7/14`, exit 0 |
| `HOLDS_OK` round-63 semantics (`:98`) | expression at measure.py:264-267 is byte-identical to round-63 measure.py:178-181; base labels equal `reports/round-63/measure-after.log` |
| `FRESH_ROWS` routed wording (`:96-97`) | comment updated to "byte survival, not current-host truth"; counting code unchanged |

## Findings

### M1 — `HOLDS_OK_V2` computes more (and less) than its registered definition
Contract (`claims.md:98-101`): "`HOLDS_OK_V2` (routed-counter fix: uses the
attributed counts — `C2_RECEIPT_B_KILLED_ATTRIBUTED`,
`C3_RECEIPT_KILLED_ATTRIBUTED`, `C4_RECEIPT_KILLED_ATTRIBUTED` — instead of raw
kills)."
Counter (`measure.py:268-271`): the same formula **plus `len(mismatch) == 0`**,
and it **omits `c4_controls == 2`** even though `C4_CONTROLS_PASS` is printed.
Demonstrated: on the current tree every named attributed count is 2/2 and all
round-63 conjuncts hold, yet `HOLDS_OK_V2=no` — caused solely by
`README_TOKEN_LEGEND_MISMATCH=1` (C07 still `frontier`). Flipping only C07
(either `held` or `uncovered`) in scratch turns V2 to `yes`. So a C4/C2 receipt
taken before C1 integration prints `no` although every calibration predicate the
contract names passes; a reader of the contract mispredicts the label.
Recommendation: register the mismatch conjunct (erratum/registration) and add
`c4_controls == 2`, or drop the unregistered conjunct and keep M36 in its own
label. Do not silently leave the sentence and code out of step.

### M2 — after-state pin in `R64MutC4.md` is a transient mid-edit file, not final bytes
`R64MutC4.md` pins patched `corpus/verify_icon_languages.py` at
`2e9e56e8bd8d55ba56c91c87454c0768a66ac87cbe4ee02943cf1916a26d7d15`. Final bytes
are `a2fd347e6379bee4d794d008aa0d1ea8b7823a1c0557775318a22a80f9239aa3`
(mtime 01:18:25). Its retained scratch
`/tmp/revenger-r64-mutc4/patched/corpus/verify_icon_languages.py` (01:17:28)
still carries `2e9e56e8…`; I reproduced that hash **exactly** by deleting the
existing requirement `require(not receipt_ok(forged,…), f'r{r}: forged receipt
command accepted')` from the final file — i.e. the tested "patched" tree was the
editing-window state missing the contract-mandated existing forged-command
control. The C4 kill conclusion survives (the added stdout control exists in
both states, and the frozen counter on final bytes independently prints
`C4_RECEIPT_KILLED_ATTRIBUTED=2/2`), and the multi-icon pin `9345cb8c…` matches
final bytes. But its "patched base green" control and its hash pin do not
describe final bytes; a receipt citing `2e9e56e8…` is stale.
Corroborating live observation: my counter run inside that window printed
`C2_RECEIPT_B_KILLED=1/2`, `HOLDS_OK=no`, exit 1; after 01:18:25 the same command
prints 2/2, `HOLDS_OK=yes`, exit 0. L1 must generate the final receipt on a
quiesced tree and cite counter output, not a seat's intermediate pin.

### L1 — `K_HELD_BACKED_STRICT` marker scan is capped at 2000 bytes
Contract (`claims.md:88-90`): cited entries "carrying an
`admission-status: rejected` marker" do not back a row. Counter
(`measure.py:38-41`) checks only the first 2000 characters. Current rejected
files carry the marker at byte 853 (`commonjs-destructured-require-edges.md`)
and 707 (`evm-saved-interface-candidates.md`), and both are cited only in held
rows' **work-evidence** column, so base `STRICT=7/14` is legitimate. A rejected
candidate whose marker falls after 2000 bytes inside a held row's knowledge
column would be silently counted as backing — the label's exact purpose defeated.

### L2 — mismatch evidence is a looser "record" than the contract's saved-record semantic; ROW_OPS content is not in the contract
`measure.py:61-69` treats any JSON dict with `operation` as a saved record,
while the F-coverage block (`:83-89`) requires `evidence_id` **and**
`normalized_result`. Equal at base (59 = 59), so no value drift, but a record
without evidence fields could raise `README_TOKEN_LEGEND_MISMATCH` on evidence
the contract's own F definition would not call a saved record (and inflate
`SAVED_RECORDS`). Separately, `claims.md:94` delegates the ROW_OPS content to
"the probe's frozen ROW_OPS map" without enumerating it; `measure.py:55-60`
covers only C03/C05/C07/C08, so a frontier row absent from the map can never
mismatch. All four frontier rows at base are covered and the counter prints the
map (`ROW_OPS=…`), so this is a contract-completeness gap, not a wrong value.

### L3 — `run()` cwd changed vs the round-63 probe under a "same definitions" promise
Round-63 executes mutant/hold runs with `cwd="/"`; round-64 uses `cwd=tree`
(`measure.py:111`), while `claims.md:96` promises "existing
`C2_*`/`C3_*`/`HOLD_*` (same definitions as the round-63 probe)". Observed
value-neutral: base labels exactly equal `round-63/measure-after.log`
(`C2_CONTROLS_PASS=2/2`, `C2_RECEIPT_B_KILLED=2/2`, `C2_D2_KILLED=2/2`,
`C3_RECEIPT_KILLED_ATTRIBUTED=2/2`, `HOLD_CALIBRATION=4/4`,
`HOLD_REPLAY=10/10`), because the verifiers anchor on
`Path(__file__).resolve().parent` and no verifier writes relative paths. Either
register the change or revert it; do not let the sentence and code diverge
silently.

### L4 — C4 clause is matched whole-file, not "inside `receipt_ok`"
The frozen mutation sentence says the conjunct is deleted "inside `receipt_ok`"
(`claims.md:61-67`); `measure.py:212-224` is a whole-file regex with an
exactly-one-match guard and whitespace-tolerant `\s*==\s*`. Current count is 1
and inside `receipt_ok` (`verify_icon_languages.py:120`,
`verify_multi_icon_states.py:123`). Safe failure mode: a second occurrence makes
the counter print `could-not-evaluate` and exit 2 (no silent pass); a unique
occurrence moved out of `receipt_ok` would simply fail to kill (0/2). No silent
false-positive path, but the scope is textual and unverified.

### L5 (informational) — exit code does not gate C1/C4/V2
`measure.py:273` exits 0/1 solely on round-63 `holds_ok` (`:264-267`). Base exit
0 coexists with `C4_RECEIPT_KILLED_ATTRIBUTED=0/2` and `HOLDS_OK_V2=no`, exactly
as contracted (`claims.md:104-106` expects exit 0). Therefore exit 0 must never
be cited as evidence for C1, C4 or V2; only the labels can.

## Residual risk

- **Editing-window race (demonstrated, currently resolved).** Between roughly
  01:17:28 and 01:18:25 the lane's `verify_icon_languages.py` lacked the
  existing forged-command require (hash `2e9e56e8…`); the frozen counter then
  printed `C2_RECEIPT_B_KILLED=1/2` and exit 1. Final bytes (`a2fd347e…`) are
  conformant and print 2/2/exit 0. Any final receipt captured while a script
  editor is in flight can carry wrong labels; run it after quiescence and note
  script hashes + mtimes in the receipt.
- **K measures existence, never quality.** A scratch stub entry with
  `admission-status: admitted` printed `K_HELD=8/14` and mismatch 0. Admission
  of the real C07 entry rests entirely on the Q01–Q13 seats and the README flip;
  the counter cannot detect a second backing entry or an unmarked rejected one.
- **Attribution stream semantics.** `last` is the last line of
  `stdout + stderr` concatenated (`measure.py:110-112`), not strictly the last
  stderr line. Correct for these scripts (traceback last), but the contract's
  "last output line" should be read with that implementation in mind.
- **V1/V2 divergence.** `HOLDS_OK=yes` and `HOLDS_OK_V2=no` coexist legitimately
  at base and mid-round; adjudicate the contract's void list (C2 attributed/d2,
  C3, C4, HOLD_*) rather than v1 alone.

## Verification gaps

- No `lsp` tool/device or language server is exposed in this session (tool
  inventory: Read/Bash/Edit/Eval/Glob/Grep/Task/Wait/WebSearch/Write;
  `command -v lsp` absent; `pygls` absent). Caller/definition checks were
  therefore execution- and byte-based, not semantic; recorded here rather than
  presented as semantic proof.
- Q01–Q13 admission decisions and the wider 64-seat wave were not re-run
  (outside this seat); C1 entry quality is unverified here.
- Scratch retained for L1: `/tmp/revenger-r64-reviewcounter-base`,
  `/tmp/revenger-r64-reviewcounter-admit`, `/tmp/revenger-r64-reviewcounter-uncov`,
  `/tmp/revenger-r64-reviewcounter-before.out`,
  `/tmp/revenger-r64-reviewcounter-worktree{,2}.out` (lane-owned, for removal on
  landing).

Report: `.ufo/waves/round-64/R64ReviewCounter.md`
