# R69 Q15 checker run — end-to-end

CHECKER-AS-SPECIFIED — all three assigned invocations return the specified exit codes and outputs; but the end-to-end gate is BROKEN by the frozen counter (`measure.py:158` `NameError: name 'run' is not defined`), so `Q15_SELFTEST`/`Q15_FALSE_KILLED`/`Q15_RESTATE_OK` can never be printed on any tree that contains the checker. C2's frozen predicate is therefore unattainable under the frozen instrument (evidence below; the C2 disposition is the L1's call, not this seat's).

Seat: `L1Revenger69.R69Q15CheckerRun`. Read-only run; no repo writes.

## 1. The three assigned runs (verbatim)

cwd for all three: `/home/vgpnk/Projects/shokunin/revenger-shokunin`, checker `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/q15_tree_id_check.py`.

### 1a. `--self-test` — required exit 0 → **EXIT=0** (PASS)

```
$ python3 -B .../corpus/q15_tree_id_check.py --self-test
Q15_SELFTEST=pass (true sentence verified; false sentence killed)
EXIT=0
```

### 1b. `--scan reports/round-69/d1-false-sentence.md --lane <lane>` — required non-zero → **EXIT=1** (PASS, false sentence killed)

```
$ python3 -B .../corpus/q15_tree_id_check.py --scan \
    .../reports/round-69/d1-false-sentence.md --lane .../revenger-shokunin
Q15_FALSE_KILLED: all false-sentence pairs failed (defect receipt)
EXIT=1
```

The fixture (`reports/round-69/d1-false-sentence.md`, sha256 `637278b2a3bec105f967892155f06779658cb3ca833ab2516c63076b06da2466`) carries exactly one pair, the D1 lie `1c34603:corpus` = `51894d15…`; it resolves to `ddc6a4f6…`, so it is killed. The fixture has no `tree-identity restatement:` line, which is why the run prints the `restate_count == 0` branch (see §4, nit N2).

### 1c. Scratch true-pairs + false-sentence — required exit 0 → **EXIT=0** (PASS)

Scratch file `/tmp/revenger-r69-q15checker/true-plus-false.md` (sha256 `dede722fc3b441bbf237bc639dead4cb2d34839d9edecad971ac391366c302ef`; deleted after the run, content reproduced verbatim):

```
Q15 scratch: TRUE restatement pairs plus the D1 false sentence.

tree-identity restatement: `1c34603:corpus` = `ddc6a4f6aea51ef34e0b7669832ff1a9cb2023f7`
tree-identity restatement: `dddf147:corpus` = `51894d153a6e69487da2a273680d014abd240f61`
tree-identity false-sentence: `1c34603:corpus` = `51894d153a6e69487da2a273680d014abd240f61`
```

```
$ python3 -B .../corpus/q15_tree_id_check.py --scan /tmp/.../true-plus-false.md --lane .../revenger-shokunin
Q15_RESTATE_OK=yes (every restatement pair re-derived; false-sentence pair killed)
EXIT=0
```

**No deviation from the assignment on any of the three.**

## 2. The two true identities were re-derived, not trusted

Q15 discipline applied to its own inputs — the claims doc's values were re-derived read-only:

```
$ git -C <lane> rev-parse 1c34603:corpus
ddc6a4f6aea51ef34e0b7669832ff1a9cb2023f7
$ git -C <lane> rev-parse dddf147:corpus
51894d153a6e69487da2a273680d014abd240f61
$ git -C <lane> rev-parse 1c34603 dddf147
1c3460336d14e9bbe64778f826a07bdd996ce39b
dddf1479ad7ba4e4124b02c0a0e32edf399e4c95
```

Both match the assignment and claims.md. Lane HEAD during this run: `35e12584d37434632fa06a6c2975ab55f29a8d3f`.

## 3. Adversarial controls (extra, cheap — separability of the checker)

| scratch input | observed | exit | expected |
|---|---|---|---|
| two true pairs + failing false-sentence | `Q15_RESTATE_OK=yes` | 0 | 0 |
| true pairs only, **no** false-sentence line | `Q15_RESTATE_BAD: no false-sentence pair failed (quote does not demonstrate the class)` | 1 | 1 |
| one true + one **wrong** restatement + failing false-sentence | `Q15_RESTATE_BAD line 2: `dddf147:corpus` claimed ddc6a4f6… resolved 51894d15…` | 1 | 1 |

The checker is content-discriminating and line-addressed: a subtly wrong restatement is caught and named with its line number, and a file that lacks the ability-to-fail receipt cannot pass. Good.

## 4. BLOCKING end-to-end finding: the frozen counter cannot evaluate Q15

The counter is pinned by claims.md at sha256 `bca74e6d…`; the file on disk matches:

```
$ sha256sum reports/round-69/measure.py
bca74e6d8b5010aee79886521474f072257ee22ec7ccc24e4186666bdc048377  reports/round-69/measure.py
$ git rev-parse e1d22ca:reports/round-69/measure.py  →  85a80f7a6b1f779dd619d3d02617e5ba608896c9
$ git rev-parse HEAD:reports/round-69/measure.py      →  85a80f7a6b1f779dd619d3d02617e5ba608896c9   (identical since the claims revision)
```

**Use before definition.** The round-69 Q15 block was inserted *above* the `run()` helper:

- `reports/round-69/measure.py:158` — first `run(...)` call (Q15 self-test), module level.
- `reports/round-69/measure.py:163`, `:172` — the two scan calls, also module level.
- `reports/round-69/measure.py:187` — `def run(tree, script, *args):` (the only definition; `grep -n "def run"` returns exactly this line).

By contrast the round-68 counter is clean: `reports/round-68/measure.py:146` defines `run`, first use at `:405`. The defect was introduced with the round-69 Q15 block, which is present already in the claims revision `e1d22ca` (`git show e1d22ca:reports/round-69/measure.py` → Q15 comment at `:151`, `def run` at `:187`).

**Observed failure.** Tree built exactly per the frozen invocation contract (`git archive HEAD corpus | tar -x -C tree`), counter run from `/`:

```
K_HELD=8/14 score=5.7
...
FRESH_ROWS=18/18
Q15_PRESENT=yes
Traceback (most recent call last):
  File ".../reports/round-69/measure.py", line 158, in <module>
    rc, last = run(TREE, "q15_tree_id_check.py", "--self-test")
               ^^^
NameError: name 'run' is not defined
COUNTER_EXIT=1
```

The three Q15 labels — and the whole hold block below `:184` — are never emitted. `Q15_SELFTEST`, `Q15_FALSE_KILLED`, `Q15_RESTATE_OK` are *absent from stdout*, not `n/a`; the script dies inside the `if q15_check.is_file():` branch.

**Why it did not show up in the red-before receipt.** `reports/round-69/measure-before.log:22-25` reads `Q15_PRESENT=no`, `Q15_SELFTEST=n/a (no checker)`, `Q15_FALSE_KILLED=n/a (no checker)`, `Q15_RESTATE_OK=n/a (no checker)`, because the before-tree `222a7a7` predates the checker (added at `e1d22ca`). The control therefore exercised only the else-branch, and the crash is invisible until the checker lands — i.e. on every candidate after-tree, including the final measured one.

**Three consequences worth naming.**

1. **C2 unattainable as frozen.** The C2 pass predicate requires `Q15_SELFTEST=pass`, `Q15_FALSE_KILLED=yes`, `Q15_RESTATE_OK=yes` **and** counter exit 0. No tree containing `corpus/q15_tree_id_check.py` can print those labels, and claims.md pins the counter sha256 and states it "is never edited after this revision". C2 therefore reads **FALSIFIED by instrument** unless the L1 explicitly rules a counter repair admissible (not this seat's call — recorded, not decided).
2. **Exit-code conflation.** Python's traceback exit code is `1`, which the frozen contract defines as *"a hold failed"*, not `2` = *"not evaluable"*. A crash is thus indistinguishable from a genuine hold failure by exit code alone; only the missing `Q15_*`/hold lines and the traceback reveal it. Any consumer reading exit codes only will misattribute.
3. **Archive-scope mismatch (independent latent defect).** Even with `run` hoisted, the D1 fixture is read from `TREE / "reports/round-69/d1-false-sentence.md"` (`measure.py:161`), while the frozen invocation archives only `corpus/`. On a contract-shaped tree that file does not exist (`test -f` → NO) → `Q15_FALSE_KILLED=n/a (no d1 fixture)` → `:168 q15_false_killed = False` → predicate fails again. The fixture must either be archived into the measured tree or read from the lane. (`Q15_PRESENT` works because it reads `TREE/corpus/QUALITY.md`; `Q15_RESTATE_OK` reads `TREE/corpus/lessons/round-69.md`, which is **ABSENT at HEAD** — the lesson is still to be written this round, and `corpus/QUALITY.md:27` already names `M48 (lessons/round-69.md)` as the captured-by, so that pointer currently dangles.)

## 5. Nits in the checker itself (non-blocking, no exit-code deviation)

- **N1 — `--self-test` never touches git.** `self_test()` uses a fixed in-memory fake resolver (`:56-58`) and ignores `lane`. That is deliberate per the docstring ("the algorithm is what is under test"), but it means `Q15_SELFTEST=pass` alone does **not** evidence the live `git rev-parse` path; only the `--scan` runs do. The counter's `run(TREE, "q15_tree_id_check.py", "--self-test")` therefore also runs with `lane_root()` resolving to the archive tree — harmless only because the fake resolver short-circuits.
- **N2 — docstring vs implementation on the empty-restatement case.** The docstring says "exit 0 iff every restatement pair resolves and at least one false-sentence pair fails"; literally, a file with zero restatement lines and one failing false pair would be vacuously fine. The implementation (`:99-102`) instead fails when `restate_count == 0`. The implementation is the one the round-69 predicate needs (`q15_false_killed = rc != 0` on the d1 fixture) — but the docstring should state the extra conjunct, and the failure message is prefixed `Q15_FALSE_KILLED:` while it is a *failure*, which is misleading to any label-grep. (The counter reads the exit code, not the label — verified at `measure.py:165-166` — so there is no live misread today.)
- **N3 — short-hash ambiguity is folded into "bad".** `resolve()` returns `None` on any `git rev-parse` error (`:39-43`) and the pair is counted bad. Correct for a 7-hex ambiguous prefix, but the output then reads `resolved None` rather than "ambiguous"; acceptable.

Read-only confirmed: `git status --porcelain` shows only a sibling seat's untracked `.ufo/waves/round-69/assimilation/`; HEAD unchanged at `35e1258`.

## 6. Pins

| artifact | pin |
|---|---|
| `corpus/q15_tree_id_check.py` | blob `6829573435e707bc6fdad9123d590841501f721c` (HEAD, e1d22ca, worktree all identical); sha256 `7d074f98cb7f9ff2be4c17e6b97e60ac8d660c827a32009d85a35df50639d276` |
| `reports/round-69/measure.py` | blob `85a80f7a6b1f779dd619d3d02617e5ba608896c9`; sha256 `bca74e6d8b5010aee79886521474f072257ee22ec7ccc24e4186666bdc048377` = pinned |
| `reports/round-69/d1-false-sentence.md` | sha256 `637278b2a3bec105f967892155f06779658cb3ca833ab2516c63076b06da2466` |
| `corpus/QUALITY.md` Q15 row | present at `:27` (names `M48`, `lessons/round-69.md`) |
| lane HEAD | `35e12584d37434632fa06a6c2975ab55f29a8d3f` |

Tooling: no installs, no upgrades (host pacman paused; nothing needed beyond `python3` and `git`). Scratch under `/tmp/revenger-r69-q15checker/` deleted after the runs.

## 7. What the L1 should decide (not decided here)

1. `measure.py:187` `run` must be hoisted above `:151` (or the Q15 block moved below `:187`) — but the counter is sha256-pinned and declared never-edited, so this needs an explicit L1 ruling rather than a silent repair.
2. `measure.py:161` must read the D1 fixture from a path that exists in the measured tree (archive `reports/round-69/d1-false-sentence.md`, or resolve it from `LANE`).
3. `corpus/lessons/round-69.md` must exist at the final measured commit for `Q15_RESTATE_OK` to be evaluable at all.
