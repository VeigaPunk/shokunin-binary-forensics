GAP — C1: `C7_V4_CLEAN=yes` (and, secondarily, `C05_SINGLE_V4=yes` and `K_ROW C05 status=held`/`K_HELD_BACKED(_STRICT)=9/14`) have no kill-rule counterpart, and each is reachable with every registered counter hold green and counter exit 0; C2 is CLOSED over its four mechanical labels.

# R69KillRuleClosure — kill-rule closure over the pass branches (D5 item 3)

scope: verdict only, no edits. Method: enumerate every mechanical conjunct of
`reports/round-69/claims.md` §C1/§C2 pass branches, map each to the text of its
kill rule (`claims.md:106-109`, `claims.md:144-147`), then map each to the
counter label that produces it (`reports/round-69/measure.py`, sha256
`bca74e6d8b5010aee79886521474f072257ee22ec7ccc24e4186666bdc048377`) and to any
void condition. Reachability was tested by construction, not argued.

## C1 — the ten conjuncts

Predicate: `claims.md:93-104`. Kill rule: `claims.md:106-109` ("Any Q FAIL on the
v4 bytes, or a spot-check REJECT → … C1 is reported **FALSIFIED**").

| # | conjunct (claims.md) | counter label | kill counterpart | void counterpart | verdict |
|---|---|---|---|---|---|
| 1 | `K_HELD_BACKED=9/14` (:96) | `measure.py:45` | **none** | "a lost baseline held row" (`:187`) cannot fire — C05 was not held at baseline, no baseline row is lost | **REAL GAP** |
| 2 | `K_HELD_BACKED_STRICT=9/14` (:96) | `measure.py:66` | **none** | same void clause, cannot fire | **REAL GAP** |
| 3 | `K_ROW C05 status=held` (:97) | `measure.py:41-42` | the kill rule states the *outcome* ("the C05 row stays `uncovered`") but names no reading that selects it | none | **REAL GAP** (same axis as 1/2: the flip did not register) |
| 4 | `C05_SINGLE_V4=yes` (:98) | `measure.py:79-81` | **none** | none | **REAL GAP** (different axis: right bytes, wrong citation) |
| 5 | `HOLDS_C2_V4=yes` (:99) | `measure.py:123-125` | none | none | not a gap: derived label — it is *exactly* conjuncts 1,2,3,4,6 conjoined (`measure.py:123-124`), so it has no independent failure mode |
| 6 | `README_TOKEN_LEGEND_MISMATCH=0` (:100) | `measure.py:104-112` | none | void via `HOLDS_OK_V4/V5/V6` (`measure.py:561-564` carries `len(mismatch) == 0`) | not an independent gap; base reads `0` (`measure-before.log:16`) |
| 7 | `C7_V4_CLEAN=yes` (:101) | `measure.py:489-495` | **none** | **none** | **REAL GAP — primary; demonstrated below** |
| 8 | every applicable Q01–Q15 decision PASS, `n/a` only with the entry's named reason (:102) | no counter label at all | covers `Q FAIL` only (`:106`) | none | **REAL GAP (third reading)**: a missing decision or a bare `n/a` is neither PASS nor FAIL → neither branch |
| 9 | spot-check not REJECT (:103) | no counter label | covered (`:106`) | n/a | closed |
| 10 | counter exit 0 (:104) | `measure.py:577` (`holds_ok` only) | none in the kill rule | void "counter exit non-zero at final" (`:193`) | not a gap — registered void resolves it |

Eight of the ten conjuncts have no kill-rule counterpart; three of those eight are
real off-target holes for this round's claim surface (1+2+3 fuse into one axis).

**Why 7 is the primary hole, not a theoretical one.** `C7_V4_CLEAN` is the
embedded-output verbatim gate applied to the v4 entry. C1's build (§C1 item 11)
re-embeds a 20-line derivation output, so "the gate went red on one reflowed line"
is the most probable build failure of this claim — and the gate is deliberately
*verbatim*: a drift that preserves every value is caught by C7 and by no Q
criterion. `c7_v4_clean` is computed at `measure.py:492` and printed at `:493`,
and appears in **no** hold expression: `holds_ok_v5` uses `c7_v2_clean`
(`:570-571`), `holds_ok_v6` uses `c7_v3_clean` (`:574-575`), and the exit code is
`holds_ok` alone (`:577`). So a v4 entry that drifts one embedded line leaves
`HOLDS_OK_V6=yes`, exit 0, no void condition fired, and no Q FAIL unless a seat
happens to catch a value-neutral drift — C1 is then neither PASS nor FALSIFIED.

**Counterexample B (value-preserving verbatim drift).** Scratch tree
`/tmp/revenger-r69-krc/B_verbatim_only` = base `222a7a7` corpus + C05 row flipped
to `held` citing `knowledge/round-69-apk-axml-byte-evidence.md` + a v4 entry that
is the round-68 entry with `admission-status: candidate` and one JSON key order
swapped in the `--fact archive` block (`{"bytes": 947, "fact": "archive", …}` →
`{"fact": "archive", "bytes": 947, …}`). Every printed value is unchanged, so no
Q04/Q06/Q11 reading has anything to fail on. Actual counter output (exit 0):

```
K_HELD_BACKED=9/14
K_HELD_BACKED_STRICT=9/14
K_ROW C05 status=held
C05_SINGLE_V4=yes
HOLDS_C2_V4=yes
README_TOKEN_LEGEND_MISMATCH=0 rows=[]
C7_V4_CLEAN=no exit=1 :: checked_blocks=17 problems=1
HOLDS_OK=yes
HOLDS_OK_V6=yes
```

Seven of the eight counter-visible conjuncts green (conjuncts 8 and 9 — Q verdicts and the spot-check — have no counter label), the only red is `C7_V4_CLEAN`, exit 0, kill rule silent → neither.

**Counterexample A (semantic drift, same topology).** Same construction with
`"bytes": 947` → `948`: identical label set, `C7_V4_CLEAN=no exit=1
checked_blocks=17 problems=1`, `HOLDS_OK_V6=yes`, exit 0.

**Counterexample C (right entry on disk, wrong citation).** C05 row flipped to
`held` but the knowledge column names the round-68 entry; v4 entry present and
clean. Actual counter output (exit 0):

```
K_HELD_BACKED=9/14
K_HELD_BACKED_STRICT=8/14
K_ROW C05 status=held
C05_SINGLE_V4=no
HOLDS_C2_V4=no
C7_V4_CLEAN=yes :: checked_blocks=17 problems=0
HOLDS_OK=yes
HOLDS_OK_V6=yes
```

This trips conjuncts 2/4 (and 5, their derived conjunction) while `K_HELD_BACKED` stays at target and the kill rule stays silent — the
second independent "neither" state, reachable by a one-word README edit.

**Third reading (conjunct 8).** The pass branch requires every *applicable* Q
decision to be PASS, or `n/a` **with the entry's named reason**. The kill rule
only fires on a `Q FAIL`. A seat that returns nothing, or returns `n/a` without
the entry's named reason, fails the pass branch and matches no kill clause. This
is policy-reachable by construction: `claims.md:208` — "Dead seats stay dead and
are reported; no replacement seats." Round-68's audit found no actual dead seat
(`.ufo/waves/round-68/R68WaveContractAudit.md:106`), so this is reachable, not
observed. Note also that no counter label aggregates Q verdicts (`grep -n "Q0[0-9]|Q1[0-5]"`
over `measure.py` returns only the `Q15_*` build labels), so conjuncts 8 and 9
have no mechanical receipt at all — they are adjudication-only.

Note on `:107-108`: the fail branch ends "The flip and the Gate decision land in
the same revision", while the same sentence says the row "stays `uncovered`".
Read literally the sentence asserts a flip in the branch that has none. Ambiguity
only; the explicit "stays `uncovered`" plus the void clause on non-C05 status
changes (`:187-188`) makes it non-load-bearing, but it should read "the row's
restatement and the Gate decision".

## C2 — CLOSED

Predicate `claims.md:127-135`; kill rule `:144-147` ("If `Q15_PRESENT` is not
yes, or `Q15_SELFTEST` is not pass, or `Q15_FALSE_KILLED` is not yes, or
`Q15_RESTATE_OK` is not yes … FALSIFIED"). All four mechanical labels
(`measure.py:151-178`) appear in the kill rule by name, and the "is not yes"
phrasing also absorbs the `n/a` readings the counter can print
(`measure.py:169,178`). The fifth conjunct, `counter exit 0`, has no kill
counterpart but is resolved by the registered void condition "counter exit
non-zero at final" (`:193`). No conjunct is left off-target: C2 has a closed
two-valued branch.

## Secondary findings (outside the closure verdict; for the C2 owners)

1. **C2 is unreachable under the frozen invocation.** The only `TREE/reports`
   read in the counter is `measure.py:161`
   (`d1 = TREE / "reports/round-69/d1-false-sentence.md"`), while the frozen
   invocation is `git archive <commit> corpus | tar -x -C <tree>`
   (`claims.md:156-160`). Verified: `git -C <lane> archive HEAD corpus | tar -t |
   grep -c "reports/"` → `0`, and a corpus-only tree carries no copy of the
   fixture (`find corpus -name "*d1*" -o -name "*false-sentence*"` → empty). So
   on the measured tree the counter prints `Q15_FALSE_KILLED=n/a (no d1 fixture)`,
   which under the kill rule's "is not yes" is **FALSIFIED** regardless of the
   criterion's quality. Closure holds; implementability does not. The
   ability-to-fail fixture must live inside the archived path (e.g.
   `corpus/lessons/` or a `corpus/` q15 fixture directory) or the invocation
   must archive `reports/round-69/` too — the latter changes the frozen receipt,
   so the former is the smaller move.
2. **Do-nothing control misstatement.** `claims.md:137-140` states the red-before
   reads `Q15_SELFTEST=pass` and `Q15_FALSE_KILLED=yes` on the base tree; the
   committed receipt reads `Q15_SELFTEST=n/a (no checker)` and
   `Q15_FALSE_KILLED=n/a (no checker)` (`reports/round-69/measure-before.log:23-24`,
   sha256 `e1cf90f357a94da84ab65ee4ef6d17bc0dc034f95b5458c735d3cce21edd6f29`).
   The prose contradicts its own record — the D1/M46-M47 class the round is
   mining, one axis over.

## Smallest safe correction

One appended sentence per claim, tighten-only (it can move a "neither" reading to
FALSIFIED and can never turn a non-pass into a pass, so it does not repair the
acceptance condition):

> **C1 kill rule (add):** *or* any label named in the pass branch reads other than
> its target on the final measured tree — `K_HELD_BACKED=9/14`,
> `K_HELD_BACKED_STRICT=9/14`, `K_ROW C05 status=held`, `C05_SINGLE_V4=yes`,
> `HOLDS_C2_V4=yes`, `README_TOKEN_LEGEND_MISMATCH=0`, `C7_V4_CLEAN=yes` — *or*
> any applicable Q01–Q15 decision reads neither PASS nor an `n/a` carrying the
> entry's named reason (a dead, silent or unexplained-`n/a` seat is such a
> reading) → C1 **FALSIFIED**.

C2 needs no addition for closure; it needs finding 1 fixed (fixture inside
`corpus/`) or it will falsify on the artefact path, not on the criterion.

Owner note: `claims.md:12-14` freezes the rule set "before any seat scores
anything"; this addendum must therefore be an append-only, dated addendum landed
before adjudication, and the adjudication must say it was read against the
addendum. Without it, C1's only honest reading on a C7-red / citation-wrong /
dead-seat tree is a third state, and this round has no third state.

## Tooling

No installs, no upgrades, no package manager use. Scratch trees under
`/tmp/revenger-r69-krc/` (base archive + A/B/C synthetics), deleted before return.
Read-only git used: `git rev-parse`, `git ls-tree`, `git archive` (extraction only,
no worktree mutation).
