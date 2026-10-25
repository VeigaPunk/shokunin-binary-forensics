# R69CriticSeparability — C1/C2 separability audit

VERDICT: NOT-SEPARABLE (instrument level) — the label *graph* is disjoint, but every C1 label printed after `measure.py:158` is unproduced on any tree that carries C2's `corpus/q15_tree_id_check.py`: the frozen counter dies with `NameError` and rc=1 there, and the pin-pinned `counter exit code` conjunct is shared by both predicates. Smallest safe correction is a 5-line hoist, not a redesign.

Seat: `L1Revenger69.R69CriticSeparability` (leaf, read-only on the lane). No repo/git/jj mutation, no installs, no subagents. Base tree `35e1258` (`git log --oneline -3`: `35e1258` wave-prep, `da02261` build, `e1d22ca` pre-registration); counter sha256 `bca74e6d8b5010aee79886521474f072257ee22ec7ccc24e4186666bdc048377` (matches the pin and `measure-before.log`).

## Method

Built corpus-only archives (`git archive HEAD corpus | tar -x -C …`, the frozen invocation in `reports/round-69/claims.md` §Frozen counter — the same shape round 68 used, `.ufo/waves/round-68/R68CounterIntegrity.md:70`) into `/tmp/revenger-r69-sep/{A,B,C,D,E,F,G,B2}`, varied only the claim-owned artifacts, and ran (i) the pinned counter and (ii) a *diagnostic* copy that only hoists `def run` above the Q15 block (`sha256 ee17e4292e9db3a347fd90137aaad543eb4f0621044844c29d254e049150884e`, byte-length delta 0). The diagnostic copy exists solely to read labels past the crash; all verdicts about the frozen instrument come from the pinned file.

| var | tree content |
|---|---|
| A | build as committed (`35e1258`) — v4 candidate, QUALITY Q15 row, q15 checker, README C05 **unflipped** |
| B | A + README C05 flipped `held` naming `knowledge/round-69-apk-axml-byte-evidence.md` (simulated post-adjudication, knowledge column = raw-split index 3) |
| C | A − QUALITY Q15 row − `corpus/q15_tree_id_check.py` (C2 artifacts absent) |
| D | B + C2 artifacts + `corpus/lessons/round-69.md` (one `tree-identity restatement:` + one `tree-identity false-sentence:` line) |
| E | D + `reports/round-69/d1-false-sentence.md` (full-repo-shaped tree) |
| F | D with the C7 clause `problems += drift(...)` deleted from the gate (C1-side damage probe) |
| G | D with README C05 reverted to build row (C2 only) |
| B2 | B − QUALITY Q15 row − checker (C1 only) |

## Label matrix (diagnostic hoisted run, complete runs, rc from process)

```
var  K_HELD_BACKED K_STRICT C05_STATUS C05_SINGLE_V4 HOLDS_C2_V4 C7_V4_CLEAN Q15_PRESENT Q15_SELFTEST Q15_FALSE_KILLED        Q15_RESTATE_OK   rc
A    8/14          8/14     uncovered  no            no          yes         yes         pass         n/a (no d1 fixture)      n/a (no lesson)  0
B    9/14          9/14     held       yes           yes         yes         yes         pass         n/a (no d1 fixture)      n/a (no lesson)  0
C    8/14          8/14     uncovered  no            no          yes         no          n/a          n/a (no checker)         n/a              0
D    9/14          9/14     held       yes           yes         yes         yes         pass         n/a (no d1 fixture)      yes              0
E    9/14          9/14     held       yes           yes         yes         yes         pass         yes exit=1               yes              0
G    8/14          8/14     uncovered  no            no          yes         yes         pass         n/a (no d1 fixture)      yes              0
B2   9/14          9/14     held       yes           yes         yes         no          n/a          n/a (no checker)         n/a              0
F    9/14          9/14     held       yes           yes         yes         yes         pass         n/a (no d1 fixture)      yes              **2**
```

Reading: each claim's labels move only with that claim's own artifacts (B vs B2, D vs G). No label value reads the other claim's files. The cross-claim failures are all instrument-level (below).

## F1 — BLOCKER (the referred question): the frozen counter aborts on C2's checker, before any C1 label

`reports/round-69/measure.py:151-182` is the Q15 block; it calls `run(...)` at `:158`; `def run` is at `:187`. Python resolves the name at call time and the definition has not executed yet → `NameError`. The check is `q15_check = TREE / "corpus/q15_tree_id_check.py"` (`:156`), so the crash fires on **any** tree containing the round-69 checker — i.e. every after-tree, because the checker is committed at `e1d22ca`/HEAD in `corpus/`.

Pinned counter, variant D (all of C1's build + C2's build):

```
$ python3 -B …/reports/round-69/measure.py /tmp/revenger-r69-sep/D
…
Q15_PRESENT=yes
Traceback (most recent call last):
  File "…/reports/round-69/measure.py", line 158, in <module>
    rc, last = run(TREE, "q15_tree_id_check.py", "--self-test")
NameError: name 'run' is not defined
rc=1
```

Same crash on A, B, E, F (each log: `Q15_PRESENT=yes` then the traceback). On C (checker removed) the pinned counter completes, `exit=0`. So `C7_V4_CLEAN`, `HOLDS_C2_V4`, `K_HELD_BACKED*`, `C05_SINGLE_V4`, `README_TOKEN_LEGEND_MISMATCH` — every C1 label produced at `:81`…`:493` after `:158` except the three printed before it — are **unproduced** on the final measured tree.

Answer to the literal question ("does any C1 label depend on a Q15 artifact"): yes, operationally — the C1 predicate's `the counter's exit code is 0` (`claims.md:96-105`) is a function of the *presence* of `corpus/q15_tree_id_check.py`; remove it → rc 0, add it → rc 1. And the rest of C1's labels are not emitted at all in its presence. The dependence is one-way and content-free (the checker's bytes are never read before the crash).

Impacted axes: coverage (C1) not scoreable; calibration (C2) also not scoreable (`Q15_SELFTEST`/`Q15_FALSE_KILLED`/`Q15_RESTATE_OK` never print).

Smallest safe correction: hoist `def run` (`:187-191`) above `:151`, or inline `subprocess.run` in the Q15 block. Zero semantic delta (my hoisted copy: 0-byte length delta, sha256 `ee17e42…`). Because the counter is sha-pinned and frozen pre-scoring, this must land as a claims **revision r2 with a re-run red-before on the same base tree `222a7a7`** — never as a silent edit, and the pinned sha256 in `claims.md:14`/`measure-before.log` must be re-pinned. No after-measurement has been published yet (no `measure-after.log` in `reports/round-69/`), so r2 is legitimate.

## F2 — Named shared label: `counter exit code` (`measure.py:577`)

`sys.exit(2 if not evaluable else 0 if holds_ok else 1)`. `holds_ok` (`:557-561`) is computed from lane-wide mutants and holds (`C2/C3/C4/C5/C6/C7` control/kill counts, `HOLD_CALIBRATION`, `HOLD_REPLAY`, `FRESH_ROWS`) — it reads **no** Q15 label and **no** C05 label. So it is a shared *precondition*, not a shared measurement: a failure in an unrelated hold fails both predicates' "counter exit code is 0". Probe F: delete the C7 clause → `MUTANT check_embedded_outputs.py c7 could-not-evaluate (clause match count != 1)` → `evaluable=False` → **rc=2** while `Q15_SELFTEST=pass` and `Q15_RESTATE_OK=yes`. Read the exit code as a lane gate, never as evidence for either claim. Secondary defect: the F1 crash returns **1**, which the documented contract (`measure.py:19`, "2 = not evaluable / 1 = a hold failed") reserves for a failed hold — an aborted after-run is indistinguishable from a red hold.

## F3 — C2 label reads a path outside the frozen measurement surface

`measure.py:163`: `d1 = TREE / "reports/round-69/d1-false-sentence.md"`, but the invocation archives only `corpus/` (`claims.md` §Frozen counter). A corpus-only tree has no `reports/` (verified: `ls /tmp/revenger-r69-sep/A` → `corpus` only; `ls …/A/reports` → No such file or directory). Result: `Q15_FALSE_KILLED=n/a (no d1 fixture)` on A, B, D, F, G, B2; `yes exit=1` only on E where `reports/round-69/` was copied in. Under the frozen contract, C2's own kill rule (`claims.md:143-147`) therefore fires unconditionally → C2 FALSIFIED by construction. This is C2-internal, but it is the second reason the claim is not independently scoreable.

Smallest safe correction: move the fixture inside the archived surface (`corpus/fixtures/q15/d1-false-sentence.md`) and repoint `:163`; or widen the invocation to the whole commit and say so in `claims.md`. Either is an r2 change.

## F4 — Reverse direction is clean: no C2 label reads a C1 artifact

Q15 block inputs only: `corpus/QUALITY.md` (`:152-155`), `corpus/q15_tree_id_check.py` (`:156`), the D1 fixture (`:163`), `corpus/lessons/round-69.md` (`:171`). The checker itself reads only its argv file plus `git -C <lane> rev-parse <hash>:corpus` (`corpus/q15_tree_id_check.py:40-88`). No path to the v4 entry, `README.md`, `derive_axml_anchors.py`, or the gate. Empirically: A vs B (C1 flip on/off) → `Q15_PRESENT=yes`, `Q15_SELFTEST=pass` identical; D vs G (C1 flip on/off, C2 complete) → `Q15_PRESENT=yes`, `Q15_SELFTEST=pass`, `Q15_RESTATE_OK=yes`, `Q15_FALSE_KILLED=n/a` identical.

Two named caveats, neither of which is a shared label:
- **Non-hermetic resolution.** `:172-174` passes `--lane LANE` (absolute lane), so `Q15_RESTATE_OK` verifies archived lesson bytes against the *live* object store. A one-way sequencing dependency exists if the lesson restates the settlement tip's `corpus` tree id: that id embeds C1's README flip in the same revision, so the label can only pass at/after the C1 flip commit. Not required — D passes citing the pre-round-68 hashes (`git rev-parse 1c34603:corpus` → `ddc6a4f6aea51ef34e0b7669832ff1a9cb2023f7`; `git rev-parse dddf147:corpus` → `51894d153a6e69487da2a273680d014abd240f61`), both independent of C1.
- **The restate label also asserts the defect quote.** `scan()` returns False when no `tree-identity false-sentence:` pair fails (`q15_tree_id_check.py:99-102`), so the C2 lesson must carry a second, false sentence. Read `Q15_RESTATE_OK=yes` as "restatement re-derived AND a quoted false pair was killed", not only the restatement.

## F5 — C1 trips its own round's void condition, independently of C2: `C7_V3_CLEAN=no`

On the round-69 build tree, every variant that carries the round-69 `corpus/` (A, B, C, D, E) prints:

```
C7_V3_CLEAN=no exit=1 :: checked_blocks=17 problems=7
HOLDS_OK_V6=no
```

Base receipt for comparison: `measure-before.log:80` `C7_V3_CLEAN=yes … problems=0`, `:105` `HOLDS_OK_V6=yes`. Cause: the extended derivation now prints enum values —

```
$ python3 -B corpus/derive_axml_anchors.py     # sha256 74d4c0d9… as the S047 source line pins
enum RES_STRING_POOL_TYPE : 239 = 0x0001
```

— while the frozen v3 entry embeds the old form (`corpus/knowledge/round-68-apk-axml-byte-evidence.md:137-143`, e.g. `enum RES_STRING_POOL_TYPE : 239`). The gate requires verbatim membership of each embedded output line (`corpus/check_embedded_outputs.py:14-17,83-85`), and v3's `recheck:` names `python3 -B corpus/derive_axml_anchors.py` (`round-68…md:7`). `claims.md:192-193` voids the round on `HOLDS_OK_V4/V5/V6 not yes` → the build as landed trips the round's own void condition. Variant C (C2 artifacts deleted) still shows `C7_V3_CLEAN=no`, so this is C1-side only — it further proves the labels are disjoint.

Smallest safe correction: do not change the shared derivation's default stdout. Put the values behind a flag (`python3 -B corpus/derive_axml_anchors.py --enum-values`) or a second script so the v3 recheck command keeps printing the old 17 lines, and have v4's item 11 embed the 20-line form it declares (v4 already does: `corpus/knowledge/round-69-…md:139-148`, gate `problems=0`). Otherwise C1 needs an explicit claims amendment superseding `HOLDS_OK_V6` — a frozen-rule change, strictly more expensive.

## F6 — C2's red-before text contradicts the committed receipt

`claims.md:137-140` states, of the base tree, `Q15_SELFTEST=pass` and `Q15_FALSE_KILLED=yes` ("the checker ships with the claims revision and the D1 fixture is committed as evidence"). The committed receipt says otherwise:

```
reports/round-69/measure-before.log:22  Q15_PRESENT=no
reports/round-69/measure-before.log:23  Q15_SELFTEST=n/a (no checker)
reports/round-69/measure-before.log:24  Q15_FALSE_KILLED=n/a (no checker)
reports/round-69/measure-before.log:25  Q15_RESTATE_OK=n/a (no checker)
```

The base tree `222a7a7` predates the checker (it lands in `e1d22ca`, the claims revision itself), and a corpus-only archive cannot see `reports/round-69/` anyway (F3). The prose is a D1-class statement checked against bytes that contradict it. Minimal correction: restate to the receipt's actual values (`n/a`), keeping the sound part of the argument — no criterion row, no checker, no lesson at base, so `Q15_PRESENT` cannot be yes without the row.

## F7 — Label-name collision (false-provenance hazard)

`HOLDS_C2_V4` (`measure.py:119-125`) is the **round-68 coverage** aggregate — its own comment at `:114` says "C2 coverage aggregate (round-68)". It is C05 coverage evidence, not round-69 C2 (calibration). `claims.md:98` consumes it inside C1's predicate, which is correct, but a reviewer mapping "C2" to this round's C2 would read the claim as self-referential. Read it as: `HOLDS_C2_V4=yes` ⇔ C05 row held, backed 9/14 strict, knowledge column exactly the v4 entry, legend mismatch 0. Verified in B2: `HOLDS_C2_V4=yes` with all C2 artifacts absent.

## Verdict, precisely

- Under the literal test "does any C1 label read a Q15 artifact (or vice versa)": **SEPARABLE** — must be, since the second direction is empty (F4) and the first is only the exit code / non-emission (F1), never a content read. Evidence: B vs B2 and D vs G.
- Under the operative test "can each claim be scored PASS/FAIL on the one final measured tree without the other's build": **NOT-SEPARABLE** — the pinned counter aborts on the C2 checker's presence (F1, rc=1) and the exit conjunct is shared (F2).
- Reported: **NOT-SEPARABLE (instrument level), named shared label = `counter exit code`; the label graph itself is disjoint.**

Smallest safe correction bundle, in one pre-scoring revision r2 re-freeze (no after-measurement exists yet):
1. hoist `def run` above `measure.py:151` (pure move; 0-byte delta in the diagnostic copy) — restores every C1 label and makes F1 non-blocking;
2. place the D1 fixture inside `corpus/` and repoint `measure.py:163` (or widen the invocation) — makes `Q15_FALSE_KILLED` reachable under the frozen contract;
3. add `--enum-values` (or a second script) so the shared derivation's default stdout is unchanged — restores `C7_V3_CLEAN=yes` / `HOLDS_OK_V6=yes` and clears the round's own void trip (F5);
4. restate C2's red-before paragraph to the receipt values (F6).
Re-pin the counter sha256 and re-run the red-before on `222a7a7` before any after-run.

## Receipts

- pinned counter sha256: `bca74e6d8b5010aee79886521474f072257ee22ec7ccc24e4186666bdc048377` (`sha256sum reports/round-69/measure.py`, matches `claims.md:14`/`measure-before.log`)
- diagnostic hoisted copy sha256: `ee17e4292e9db3a347fd90137aaad543eb4f0621044844c29d254e049150884e` (byte-length delta 0; `/tmp` only, deleted)
- frozen-counter crash (D): `measure.py`, line 158 → `NameError: name 'run' is not defined`; rc=1. Frozen-counter full run (C, C2 artifacts absent): rc=0.
- gate on v3 in the build tree: `checked_blocks=17 problems=7`, drift lines `entry:137-143`; gate on v4: `checked_blocks=17 problems=0`; direct gate run on v3 exits **1** (`gate-v3 rc=1`), consistent with `C7_V3_CLEAN=no exit=1`.
- `git rev-parse 1c34603:corpus` → `ddc6a4f6aea51ef34e0b7669832ff1a9cb2023f7`; `git rev-parse dddf147:corpus` → `51894d153a6e69487da2a273680d014abd240f61` (the D1 contradiction is real).
- `corpus/derive_axml_anchors.py` sha256 `74d4c0d9…a83aa` in the tree matches the S047 source line.
- Tooling: nothing installed or upgraded (host pacman paused); no writes outside this report and `/tmp/revenger-r69-sep*` (removed).
