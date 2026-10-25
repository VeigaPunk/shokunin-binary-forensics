DEFECT — C1's target is real and byte-derivable, but C1 cannot be scored on the tree its own build produces: the frozen counter dies with `NameError` at `measure.py:158` (any tree carrying `corpus/q15_tree_id_check.py`), C1's build step breaks the retained v3 candidate's C7 gate (`HOLDS_OK_V6=no`) which `claims.md:193` makes a void condition, and the do-nothing control's "AND an all-pass wave" leg is measured by nothing (a one-line README flip with the entry still `admission-status: candidate` reproduces every counter label of the predicate plus exit 0).

# Session
- Lane `/home/vgpnk/Projects/shokunin/revenger-shokunin` at `35e1258` (build `da02261`, pre-reg `e1d22ca`, base `222a7a7`). Read-only on the lane; all experiments ran on `git archive` copies under `/tmp/revenger-r69-c1/`.
- No installs, no upgrades (pacman paused host-wide; nothing needed).
- Counter under test: `reports/round-69/measure.py` sha256 `bca74e6d8b5010aee79886521474f072257ee22ec7ccc24e4186666bdc048377` (matches `measure-before.log` and `claims.md`).

# Check 1 — "one concrete value, one command, committed bytes": PARTIAL
`K_HELD_BACKED=9/14` is printed by the frozen counter over the archived `corpus/` (one command, committed bytes). But:
- It is **not row-pinned**. `C02` (partial→held) alone reaches the same value with C05 untouched:
  - `/tmp/revenger-r69-c1/tree4` = HEAD + `| C02 … | held |`, no other edit →
    `K_HELD=9/14  K_HELD_BACKED=9/14  K_HELD_BACKED_STRICT=9/14  K_ROW C05 status=uncovered  C05_SINGLE_V4=no`.
  - So the headline number is a generic count; only the conjunction (`K_ROW C05 status=held` + `C05_SINGLE_V4=yes`) actually pins C05. The claim text presents one number as *the* target (`claims.md:95`); the real target is a 10-label conjunction.
- It is **not evaluable as C1 states it**: the predicate's `C7_V4_CLEAN=yes` (`claims.md:98`) and "the counter's exit code is 0" (`claims.md:103`) are printed **after** the crash site, so they are unreachable. See Check 3.

# Check 2 — do-nothing control cannot reach it "without the new entry AND an all-pass": FALSE (second conjunct)
`claims.md:116` asserts "The control cannot reach 9/14 without the new entry **and** the all-pass wave". The counter cannot see an all-pass, an admission, or the entry's `admission-status`. Tree `/tmp/revenger-r69-c1/tree2` = HEAD with **only** the C05 row's cell 3 set to the v4 path and cell 5 to `held`:

```
K_HELD=9/14 score=6.4
K_ROW C05 status=held
K_HELD_BACKED=9/14
K_HELD_BACKED_STRICT=9/14
C05_SINGLE_V4=yes
C05_STATUS=held
README_TOKEN_LEGEND_MISMATCH=0 rows=[]
HOLDS_C2_V4=yes
```
while that tree's entry still reads `admission-status: candidate — the round-69 fourth-pass candidate` (`corpus/knowledge/round-69-apk-axml-byte-evidence.md:11`). No wave, no Q decision, no spot-check. With the `run()` name error hoisted out (diagnostic copy, see Check 3), the same tree also prints `C7_V4_CLEAN=yes exit=0` and exits **0** — i.e. every counter label in C1's predicate at target, from a one-line README edit. The "cannot reach without … an all-pass" leg is a prose obligation, not a measured control.
- The "without the new entry" leg *does* hold: `K_HELD_BACKED` requires the named file to exist (measure.py backed-row test), so a flip naming an absent file stays 8/14.

# Check 3 — counterexample: the instrument cannot evaluate the tree the claim builds
`reports/round-69/measure.py` calls `run(...)` at `:158` but defines `def run` at `:187`. The round-68 counter defined it at `:146`, before its first use at `:405` (`git show 222a7a7:reports/round-68/measure.py | grep -n 'def run\|run(TREE'`); the round-69 edit inserted the Q15 block above the definition. Runtime consequence, HEAD tree copied by the documented invocation (`git archive HEAD corpus`):

```
$ python3 -B reports/round-69/measure.py /tmp/revenger-r69-c1/tree
…
Q15_PRESENT=yes
Traceback (most recent call last):
  File "…/reports/round-69/measure.py", line 158, in <module>
    rc, last = run(TREE, "q15_tree_id_check.py", "--self-test")
NameError: name 'run' is not defined
RC=1
```
Nothing after `Q15_PRESENT` prints: no `Q15_*` verdicts, no `C7_*`, no C2–C6 mutants, no `HOLD_CALIBRATION`/`HOLD_REPLAY`, no `HOLDS_OK*`. The base-tree receipt is unaffected only because `222a7a7` has no Q15 checker, so the red-before run took the `else: print("…=n/a (no checker)")` branch — the freeze pins a counter whose Q15 branch was never executed before it was frozen.
- Diagnostic (scratch only, never in the lane): `/tmp/revenger-r69-c1/measure-hoisted.py` (sha256 `165896562d8342cdd060b75526c0db7decbb8a2f2a6a19d4d976cdec41b24645`) = the frozen file with the same `def run` block inserted before the Q15 comment. Same trees then run to completion: flipped tree `RC=0`, `C7_V4_CLEAN=yes exit=0`; unflipped HEAD `RC=0`, `K_HELD_BACKED=8/14`. The counter's remaining machinery is sound; only the definition order is broken.

# Check 4 — build step voids the round under the claims' own void list: DEFECT
`claims.md:193` voids the round when `HOLDS_OK_V4/V5/V6` is not yes. `HOLDS_OK_V6` includes `c7_v3_clean`, and C1 item 1 rewrites `corpus/derive_axml_anchors.py` **in place** (`bce497d6…`, 17 lines → `74d4c0d9…`, 20 lines). The retained v3 candidate embeds the old 7 `enum … : N` lines, which the extended script now prints with ` = 0x…` appended:

```
$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-68-apk-axml-byte-evidence.md
drift entry:137 embedded output line not in recheck stdout: enum RES_STRING_POOL_TYPE : 239
… entry:138/:139/:140/:141/:142/:143 …
checked_blocks=17 problems=7
RC=1
$ (same command on the 222a7a7 corpus copy)   checked_blocks=17 problems=0   RC_BASE=0
```
hence on the build tree `C7_V3_CLEAN=no` and `HOLDS_OK_V6=no` (hoisted run, `measure-before.log` had `C7_V3_CLEAN=yes`/`HOLDS_OK_V6=yes`). Second, sharper harm: v3's `source: S046` line (`corpus/knowledge/round-68-apk-axml-byte-evidence.md:4`) attaches sha256 `bce497d6…` to `corpus/derive_axml_anchors.py`; re-deriving that path now prints `74d4c0d9…` — the round created a **new M46/M47-class false identity sentence in a file the void list forbids editing**, inside the repair bundle that exists to remove that class. Byte-stability of the three prior candidates is intact (`round-65 cf42cc20…`, `round-67 057a1826…`, `round-68 ef7f0232…` identical at `222a7a7` and HEAD) — the decay is in the shared path they name, which the void condition does not cover.

# Check 5 — kill rule reserves the flip and forbids re-targeting: MOSTLY HOLDS, with an unguarded exit
Text is unambiguous (`claims.md:106-110`): Q FAIL or spot-check REJECT → row stays `uncovered`, entry marked `rejected`, C1 FALSIFIED, "no re-target, no repaired acceptance condition". Kill conditions that are **not** covered:
- "counter not evaluable" (Check 3) is not a kill condition and not a named falsification; it lands in the void list, and the claims give no void→falsified / void→re-register rule. The only exit from void is a **post-freeze counter edit** — exactly the repaired-acceptance-condition path the kill rule forbids in spirit. `claims.md` says the counter "is never edited after this revision" but names no pre-scoring re-freeze (new sha + fresh red-before) as the legitimate route.
- Self-fulfilling Q clause (`claims.md:101-102`): "every **applicable** Q01–Q15 decision … is PASS (n/a only with the entry's named reason)". *Applicable* is undefined and the n/a reasons are authored by the entry under test. The v4 entry's `§Q-map` (`round-69-apk-axml-byte-evidence.md:177-184`) enumerates **8 of 15** — Q03, Q06, Q08, Q09, Q10, Q12, Q15 are absent and carry no named n/a reason, against `corpus/QUALITY.md` §Admission procedure step 1 ("Apply every criterion. A criterion marked `n/a` names why it cannot apply"). So the "all-pass" is claimable over whichever subset the wave chooses to score, and the author supplies the exemption text.
- And Q15 **is** applicable to the v4 entry: line 8 states a git object id (`… unchanged since \`c7b7cf98\``). It resolves (`git rev-parse --verify c7b7cf98` → `c7b7cf98ddeecbd5464e47396f224e6384b78905`, type `commit`; all four fixture hashes match at that commit), but the sentence carries no deriving command — Q15's first reject leg verbatim. So C1's all-pass leg depends on C2's brand-new criterion being satisfied by C1's own entry, in the same wave that introduces it. Nothing in `claims.md` acknowledges this C1→C2 dependency.

# Check 6 — no acceptance condition repairable after scoring: HOLDS textually, undermined by Checks 3/5
The predicate, counter sha and target are frozen before scoring; nothing in C1 permits a re-opened acceptance condition. But "the counter was broken, here is v2" is a permitted-looking repair with no declared discipline, and Check 2 shows the all-pass conjunct has no measured carrier.

# Check 7 — separable from C2 (C1 labels must not depend on Q15 artifacts): LABEL-SEPARABLE, PREDICATE-DEPENDENT
- Labels: `K_*`, `K_ROW`, `C05_SINGLE_V4`, `HOLDS_C2_V4`, `README_TOKEN_LEGEND_MISMATCH` are computed before the Q15 block and read only `corpus/README.md` + `corpus/knowledge/*` + legend rows. Clean.
- Predicate: not separable. (a) Exit-0 and `C7_V4_CLEAN` are unreachable in any tree carrying `corpus/q15_tree_id_check.py` (Check 3) — i.e. across all of C2's own artifacts; C1 only becomes evaluable by **deleting C2's checker**, which falsifies C2. (b) `C7_V4_CLEAN` is computed by the C7 gate over the v4 entry, which is fine, but sits behind the crash. (c) The all-pass leg drags in Q15 itself (Check 5).
- Cross-check note for the C2 owner (not scored here): under the documented invocation (`git archive <commit> corpus`), `TREE/reports/round-69/d1-false-sentence.md` is never present, so `Q15_FALSE_KILLED` reads `n/a (no d1 fixture)` in every contract-conformant measured tree — C2's `Q15_FALSE_KILLED=yes` is unreachable as written.

# Axes
- coverage: at target only by a README edit; C1's pass predicate is unreachable, so the axis cannot move.
- calibration: the freeze's own void list is triggered by C1's build step; the D1/M46 class is re-created in v3's S046 line by the same bundle.
- instrument integrity: frozen counter is not executable on the round's final tree; `HOLDS_OK` (V1, exit-bearing) is `yes` while `HOLDS_OK_V6` is `no`, so pass-predicate and void list contradict each other on the same bytes.

# Smallest safe correction (none of these re-targets C1)
1. **Pre-scoring counter re-freeze (v2)**, before any seat scores: move the existing `def run` block above the Q15 block (mechanical; verified `RC=0` on the same three trees), pin the new sha256 in a `claims.md` revision, re-run `measure-before.log` on `222a7a7` with v2, and record "no seat scored under `bca74e6d…`". This repairs Checks 1/3/7(a) and harms no axis.
2. **Do not rewrite the shared derivation script in place.** Add `corpus/derive_axml_anchors_v2.py` (new sha + 20 lines, S047 anchor on that path) and leave `corpus/derive_axml_anchors.py` byte-identical to `bce497d6…`; point the v4 `recheck:` at the new path. Then `C7_V3_CLEAN=yes`, `HOLDS_OK_V6=yes`, and v3's S046 sha stays true. Repairs Check 4.
3. **Make the target row-pinned**: name `HOLDS_C2_V4=yes` (already a label) as the headline target instead of `K_HELD_BACKED` alone, or add a label counting C05's contribution. Repairs Check 1 and makes Check 2's counterexample a genuine red.
4. **Close the Q clause**: require a full 15-row `§Q-map` with named `n/a` reasons, and add Q15's entry-side derivation (`git cat-file -e c7b7cf98…`, or drop the `c7b7cf98` provenance sentence — the sha256s already carry identity). Otherwise Q15 fails the v4 entry on its first leg and C1 is falsified through C2's unproven criterion.
5. **Name the void→adjudication rule** (`void ⇒ no claim scored, counter revision required, no seat scored`) so a broken instrument cannot silently become a repaired acceptance condition.

Scratch `/tmp/revenger-r69-c1/` removed before return.
