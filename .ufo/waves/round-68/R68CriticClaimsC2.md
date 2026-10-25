DEFECT — C2's frozen pass branch is not separable from C1 (`HOLDS_OK_V6` is a C1-owned label, claims.md:121) and its 9/14 do-nothing control is reachable with a stub entry plus a README edit and no all-pass wave (claims.md:135-137), so the target is the flip's output rather than the admission evidence.

Read-only seat. No production file touched; only this report written. No tool installed or upgraded (system Python 3 only).

# Scope

Attack surface: `reports/round-68/claims.md` §C2 (:92-139), `corpus/measure.py` = `reports/round-68/measure.py` (sha256 `0de4eb6f…7766`, verified), `corpus/knowledge/round-68-apk-axml-byte-evidence.md` (sha256 `107e2d7483e57e64476ead408f2eb793f41e3eea5e3c96407763eadca6dfea5b`), `corpus/README.md`, `corpus/derive_axml_anchors.py` (sha256 `bce497d6…1e249`, verified), `corpus/snapshots/ResourceTypes.h` (sha256 `56b88bc4…c56f`, verified), `reports/round-68/measure-before.log`. Lane tip at review: `4232235` (build) on pre-registration `f505526`; base claim tree `f165908`.

# Five assigned checks

| # | check | verdict | pointer |
|---|---|---|---|
| 1 | target is one concrete value re-derivable with one command over committed bytes | **PASS for the number, DEFECT for the predicate** | `K_HELD_BACKED=9/14` re-derived by `measure.py` alone (evidence B); but two of the pass-branch conjuncts are not in that command's reach: `HOLDS_OK_V6` is another claim's artifact, the Q all-pass lives outside the measured tree |
| 2 | do-nothing control cannot reach 9/14 without the new entry AND an all-pass | **DEFECT** | claims.md:135-137. Counterexample B: stub + README edit ⇒ `K_HELD_BACKED=9/14`, `HOLDS_C2_V3=yes`, `C7_V3_CLEAN=yes`, `HOLDS_OK_V6=yes`, exit 0 — no all-pass, no evidence |
| 3 | kill rule reserves the flip to an all-criteria pass and forbids re-targeting | **PARTIAL** | claims.md:126-129 reserves and forbids, but the fail branch names 2 of 10 pass conjuncts; a mechanical miss (evidence C) has no prescribed disposition |
| 4 | no acceptance condition repairable after scoring | **DEFECT** | claims.md:122-123 "applicable" + "n/a only with the entry's named reason" is an in-predicate repair valve, already exercised by the entry (:179, :183, :184) |
| 5 | separable from C1 (C1's labels not in C2's predicate) | **DEFECT** | claims.md:121 `HOLDS_OK_V6=yes`; measure.py:521-526 makes it transitively require `C7_MUTANT_KILLED_ATTRIBUTED=1/1`, i.e. the C1 file repair. claims.md:34-38's separability paragraph is contradicted |

# Counterexample A — C2 can be complete and still fail on C1's artifact

Counterfactual = base tree `f165908` (C1 not repaired) + the complete C2 surface from `4232235` (v3 entry, derive script, pinned snapshot) + the README knowledge-column flip:

```
git archive f165908aaffcf14798de53405fe788986bd33ff9 corpus | tar -x -C TMP/d
# copy corpus/knowledge/round-68-apk-axml-byte-evidence.md, corpus/derive_axml_anchors.py, corpus/snapshots/ResourceTypes.h
# README C05 row: knowledge column = `knowledge/round-68-apk-axml-byte-evidence.md`, status = held
cd / && TMPDIR=/tmp python3 -B reports/round-68/measure.py TMP/d
```
```
K_HELD=9/14 score=6.4
K_HELD_BACKED=9/14
K_HELD_BACKED_STRICT=9/14
C05_SINGLE_V3=yes
C05_STATUS=held
HOLDS_C2_V3=yes
C7_V3_CLEAN=yes exit=0 :: checked_blocks=17 problems=0
C7_MUTANT_KILLED_ATTRIBUTED=0/1
C7_NEG_SPOOF_KILLED=1/1
C7_NEG_SPOOF_KILLED_ATTRIBUTED=0/1
HOLDS_OK_V6=no
counter_exit=0
```
Every C2-owned conjunct reads at target; the branch fails only on `HOLDS_OK_V6`, which is C1's file (`measure.py:521-526`: `holds_ok_v6 = holds_ok_v5 and …`, and `holds_ok_v5 = holds_ok_v4 and c7_targets`, `c7_targets` requires `c7_mut_attributed == 1`). The coupling is one-way: on the landed build with C05 still `uncovered`, variant A' (plain `HEAD`) reads `HOLDS_OK_V6=yes` / `HOLDS_OK_V5=yes` / `C7_MUTANT_KILLED_ATTRIBUTED=1/1`, i.e. C1's label is satisfied by C1 alone. So including it in C2's predicate makes a perfect C05 admission unfalsifiable-or-failed by a file C2 does not touch.

Clause: claims.md:121 (`HOLDS_OK_V6=yes` in the C2 pass branch) and its do-nothing row claims.md:135 (lists `C7_V3_CLEAN=n/a` but silently inherits `HOLDS_OK_V6`).

# Counterexample B — 9/14 and every mechanical conjunct without an all-pass

`HEAD` (C1 repaired) + README knowledge-column flip + the v3 entry replaced by a 5-line stub whose only content is one true line of the derive table:

```
# TMP/e = git archive HEAD corpus
# README C05 row: knowledge column = `knowledge/round-68-apk-axml-byte-evidence.md`, status = held
cat TMP/e/corpus/knowledge/round-68-apk-axml-byte-evidence.md
```
```
# stub

```
$ python3 -B corpus/derive_axml_anchors.py
enum RES_XML_START_NAMESPACE_TYPE : 245
```
```
cd / && TMPDIR=/tmp python3 -B reports/round-68/measure.py TMP/e
```
```
K_HELD=9/14 score=6.4
K_HELD_BACKED=9/14
K_HELD_BACKED_STRICT=9/14
C05_SINGLE_V3=yes
C05_STATUS=held
HOLDS_C2_V3=yes
C7_V3_CLEAN=yes exit=0 :: checked_blocks=1 problems=0
HOLDS_OK_V6=yes
counter_exit=0
```
This is every pass-branch conjunct that `measure.py` can see. `C7_V3_CLEAN` is the only content-sensitive one, and the gate passes on **one** matching line in **one** block (`check_embedded_outputs.py:57-65` collects non-empty lines, :88-108 compares membership only; `checked_blocks=1` here vs `17` on the real entry). No APK evidence, no oracle agreement, no Q decision, no wave. Hence claims.md:135-137 ("cannot reach 9/14 without the new entry **and** the all-pass wave") is false as a property of the control: 9/14 is reachable from a README token plus a filename.

The deeper shape problem is circularity: `K_HELD_BACKED` moves only when the claimant performs the flip, and the flip is exactly what the all-pass is supposed to license (claims.md:129 "The flip and the Gate decision land in the same revision"). So `9/14` is the *output* of the admission decision, not evidence for it; the only non-circular evidence in the predicate is the Q table, which is outside the measured tree (below).

# Counterexample C — a plausible mechanical miss has no fail branch

Flip the status token only, leaving the knowledge column at `—` (the state the build is in today):

```
# TMP/b = git archive HEAD corpus, C05 row status only: uncovered -> held
cd / && TMPDIR=/tmp python3 -B reports/round-68/measure.py TMP/b
```
```
K_HELD_BACKED=8/14
C05_SINGLE_V3=no
C05_STATUS=held
HOLDS_C2_V3=no
C7_V3_CLEAN=yes exit=0 :: checked_blocks=17 problems=0
```
Pass branch: not met (`8/14`). Kill rule claims.md:126-129: triggers only on "Any Q FAIL on the v3 bytes, or a spot-check REJECT" — neither holds. The claim is then neither PASS nor FALSIFIED, which is the repair/re-target opening the same sentence forbids. Contrast C1's kill rule (claims.md:72-79), which enumerates its mechanical conjuncts (`HOLDS_OK_V4` no, `HOLD_CALIBRATION` < 4/4, `HOLD_REPLAY` < 10/10, `FRESH_ROWS` != 18/18). Clause: claims.md:126-129.

# Counterexample D — the all-pass conjunct is not testable from the measured bytes

`measure.py` has no Q label at all (`grep -nE 'Q0[1-9]|Q1[0-3]' reports/round-68/measure.py` → no match; the only Q text is the docstring). The counting command extracts `corpus/` only (`git archive <commit> corpus | tar -x`), and `HEAD` tracks exactly one file under the wave dir:

```
git ls-tree -r --name-only HEAD | grep -c '^.ufo/waves/round-68'
1
git ls-tree -r --name-only HEAD | grep '^.ufo/waves/round-68'
.ufo/waves/round-68/build-r68.py
```
`git status` additionally shows `.ufo/waves/round-68/{build-wave-spec.py,wave-spec.json}` untracked. So the seat decisions that the predicate depends on are in neither the measured tree nor a committed one at scoring time.

The clause is also self-relaxing: "every **applicable** Q01–Q13 … is PASS (n/a only with the entry's named reason)" (claims.md:122-123) lets the adjudicator decide applicability and accept the entry's own n/a reason — after scoring. The entry already uses that valve: `:179` Q08 "superseded by Q11", `:183` Q12 "n/a", `:184` Q13 "n/a by construction". A Q FAIL can therefore be re-labelled n/a with the entry's reason, which is the repaired acceptance condition claims.md:11-13 and :129 forbid.

# What I checked and cleared (false-positive I discarded)

I first suspected `C05_SINGLE_V3`/`K_HELD_BACKED` read the wrong README column. Cleared: for `| row | surface | knowledge entries | work evidence | status |`, `split("|")[3]` **is** the knowledge-entries column; the C05 row's knowledge column is `—` at build, its work-evidence column holds the retained r65 candidate. So the counter is column-correct, and the flip must add a knowledge-column ref (not only a status token) — see Counterexample C.

Also verified as true: `C7_V3_CLEAN=yes` on the landed entry with `checked_blocks=17 problems=0` (matches claims.md:120); `derive_axml_anchors.py` exit 0 and `RES_XML_START_NAMESPACE_TYPE : 245`, `comment attributeStart : 686`, `field attributeStart : 687` confirmed against the snapshot bytes (`sed -n '244,245p;686,687p'` → `RES_XML_FIRST_CHUNK_TYPE` / `RES_XML_START_NAMESPACE_TYPE` / comment / `uint16_t attributeStart;`); README remains `uncovered` at `4232235` (`git diff f165908 HEAD -- corpus/README.md` empty), so admission order step 1 holds.

# Impacted axes

- **separability / duplicate authority** (claims.md:34-38 vs :121): C2 inherits C1's calibration state; a C1 regression voids C2 even with a perfect C05 admission.
- **evidence provenance of the target**: 9/14 measures a README token, not admission; the load-bearing evidence (Q decisions) is uncommitted and out of the counting command's reach.
- **falsifiability**: two of ten pass conjuncts (all-pass, n/a applicability) are author-adjudicated; the fail branch does not close over the predicate.
- **fixture/live surface**: clean — `git diff f165908 HEAD` touches no `corpus/live` or `corpus/fixtures` path.

# Smallest safe corrections (shape only; no byte of the counter or entry changes)

1. **Drop `HOLDS_OK_V6=yes` from the C2 pass branch** (claims.md:121) and from the C2 do-nothing row, or restate it as `VOID`-if-C1-fails with the C1 labels named. C1 already owns that conjunct; leaving it in C2 is what falsifies "causally separable". Keep `C7_V3_CLEAN=yes` only if claims.md:34-38 declares it as a named one-way read of the C1-owned gate file.
2. **Rewrite the do-nothing row** (claims.md:135-137) to its measured truth: "the control reads 8/14 with C05 `uncovered`; 9/14 is a README-token count reachable by the flip plus any file of that name (demonstrated: a 1-block stub scores `K_HELD_BACKED=9/14`, `HOLDS_C2_V3=yes`, `C7_V3_CLEAN=yes`), therefore 9/14 is the flip's output — the admission evidence is the frozen Q decision table, not the count."
3. **Close the kill rule over the predicate** (claims.md:126-129): add "or any of `K_HELD_BACKED`/`K_HELD_BACKED_STRICT` != 9/14, `C05_STATUS` != held, `C05_SINGLE_V3` != yes, `README_TOKEN_LEGEND_MISMATCH` != 0, `HOLDS_C2_V3` != yes, `C7_V3_CLEAN` != yes, counter exit != 0 → C2 FALSIFIED (VOID only for a label declared C1-owned)".
4. **Freeze the Q applicability now** and put the seat decisions at a committed path the counter's extraction reaches (or extend the counting invocation to the wave report path), so "all-pass" is re-derivable by one command over committed bytes without an author decision after scoring.
5. Operational: the flip recipe must write the round-68 path into the C05 **knowledge** column *and* the status (a status-only flip reads 8/14 — Counterexample C).

# Out-of-axis dependency (for the Q11 seat, not my verdict)

The entry's §Reproduce/`:recheck` says the derivation prints "17 lines, one per cited symbol"; actual stdout is 17 lines = 1 sha256 header + **16** symbol lines (7 structs + 7 enums + 2 `attributeStart`). The "17 lines" count is right, "one per cited symbol" is off by one. Flagged for the Q11 reviewer; I did not adjudicate Q01–Q13.
