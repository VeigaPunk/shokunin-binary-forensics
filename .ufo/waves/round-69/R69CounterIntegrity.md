INTACT on pin/history/write-surface — BUT THE INSTRUMENT IS NON-FUNCTIONAL ON THE CLAIM TREE: `measure.py:158` calls `run()` at module level before its `def` at `:187`, so any tree carrying `corpus/q15_tree_id_check.py` (HEAD `35e1258` included) dies with `NameError`, 27 lines out, **exit 1**, zero `HOLDS_OK*` / `C7_*` / `HOLD_*` / `Q15_SELFTEST|FALSE_KILLED|RESTATE_OK` labels. Both claims' `the counter's exit code is 0` conjunct (`claims.md:104`, `:135`) is therefore unreachable, and the listed void condition `counter exit non-zero at final` (`claims.md:193`) is triggered by the instrument itself. Second defect: C2's red-before paragraph (`claims.md:137-139`) lists `Q15_SELFTEST=pass` and `Q15_FALSE_KILLED=yes` under "**On the base tree**", but that tree has **no checker** (`git cat-file -e 222a7a7:corpus/q15_tree_id_check.py` → exit 128), the committed receipt prints `n/a (no checker)` for all three Q15 labels (`measure-before.log:22-25`), and **no committed counter run has ever printed `Q15_SELFTEST=pass` on any tree**. No `measure-after.log` exists in any history.

# R69CounterIntegrity — round-69 frozen-counter integrity seat

Lane: /home/vgpnk/Projects/shokunin/revenger-shokunin · HEAD at check: `35e12584d37434632fa06a6c2975ab55f29a8d3f` (round-69 wave preparation) · pre-registration commit: `e1d22caaf9a2fdc4c1c13d1f4a8a6813e7b07968`. No repo byte was edited (read-only git/read only; scratch under `/tmp/revenger-r69-*`, removed).

Verdict split, so it cannot be misread:

| question asked | answer |
|---|---|
| Does the counter match the pinned sha256? | **YES** — `bca74e6d…bdc048377`, at pre-registration, at every later commit carrying it, and in the worktree |
| Did the sha change after `e1d22ca`? | **NO** — zero commits after pre-registration change the path |
| Does the counter write outside TMPDIR? | **NO** — statically and empirically proven |
| Can the frozen counter evaluate the claim surface? | **NO** — `NameError` on every tree with the Q15 checker; after-measurement unproducible as frozen |

## FINDING HIGH-1 (blocking) — `run()` used before definition; after-measurement cannot run

`reports/round-69/measure.py:158`:

```
Q15_PRESENT=…                       (printed)
if q15_check.is_file():
    rc, last = run(TREE, "q15_tree_id_check.py", "--self-test")   # :158  <-- module level
```
`def run(tree, script, *args):` is at **`:187`**, i.e. *after* the Q15 block, inside the same module body. Python executes the block at import time → `NameError`. Static confirmation (AST, name-order analysis of the pinned file):

```
defs: {'run': 187, 'mutate_b': 198}
calls-before-def: [('run', 158, 'def@187'), ('run', 163, 'def@187'), ('run', 172, 'def@187')]
```

Reproduction on the landed tree, contracted invocation:

```
$ cd <lane> && git archive HEAD corpus reports/round-69/d1-false-sentence.md | tar -x -C /tmp/revenger-r69-head/tree
$ git ls-tree -r --name-only HEAD corpus | grep -c q15_tree_id_check
1
$ cd / && TMPDIR=/tmp/revenger-r69-head python3 -B \
    /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-69/measure.py /tmp/revenger-r69-head/tree > out.log 2>&1
exit=1
$ tail -6 out.log
Q15_PRESENT=yes
Traceback (most recent call last):
  File "…/reports/round-69/measure.py", line 158, in <module>
    rc, last = run(TREE, "q15_tree_id_check.py", "--self-test")
               ^^^
NameError: name 'run' is not defined
$ wc -l out.log   → 27
```

Labels actually emitted before the crash (19 total): `K_HELD K_HELD_BACKED C05_REJECTED_MARKED K_HELD_BACKED_STRICT C05_KNOWLEDGE_COLUMN C05_SINGLE_V2 C05_SINGLE_V3 C05_SINGLE_V4 STRICT_REJECT_WINDOW_SELFTEST SAVED_RECORDS ROW_OPS README_TOKEN_LEGEND_MISMATCH C05_STATUS HOLDS_C2_V3 HOLDS_C2_V4 F_COVERAGE F_FAMILIES FRESH_ROWS Q15_PRESENT`.
Labels **lost**: every `HOLDS_OK*`, `C2_CONTROLS_PASS`, `C2_RECEIPT_*`, `C3/C4/C5/C6_*`, all `MUTANT …` lines, `C7_GATE_PRESENT`, `C7_SELFTEST`, `C7_RED_*`, `C7_V2_CLEAN`, `C7_V3_CLEAN`, **`C7_V4_CLEAN`**, `C7_CONTROL/MUTANT/NEG_*`, `HOLD …`, `HOLD_CALIBRATION`, `HOLD_REPLAY`, and **`Q15_SELFTEST` / `Q15_FALSE_KILLED` / `Q15_RESTATE_OK`** (`grep -c "HOLDS_OK\|C7_V4_CLEAN\|Q15_SELFTEST\|HOLD_CALIBRATION" out.log` → `0`).

Consequences, each a resolvable pointer in the frozen contract:
- **C1** (`claims.md:96-107`) requires `C7_V4_CLEAN=yes` (unprintable), `HOLDS_OK*`-adjacent holds (unprintable) and `the counter's exit code is 0` (`:104`) — pass branch unreachable.
- **C2** (`claims.md:127-137`) requires `Q15_SELFTEST=pass`, `Q15_FALSE_KILLED=yes`, `Q15_RESTATE_OK=yes` (all three unprintable) and exit 0 (`:135`) — pass branch unreachable; only `Q15_PRESENT=yes` survives.
- **Void condition** `counter exit non-zero at final` (`claims.md:193`) fires; and the exit code cannot be distinguished from a red hold, because `sys.exit(2 if not evaluable else 0 if holds_ok else 1)` (`:577`) never executes — the process dies at `:158` with Python's default uncaught-exception status `1`, the same value `:577` assigns to "a hold failed". A crashed after-run therefore reads as a legitimate red hold on the exit channel alone.
- **Red-before is non-representative of the pass-branch code path.** The base tree `222a7a7` has no `corpus/q15_tree_id_check.py` (the checker enters at `e1d22ca`), so `if q15_check.is_file()` is False and the `else` prints `n/a` (`measure-before.log:23-25`). The do-nothing control and the treatment therefore execute *different* code paths; the `Q15_*` before/after delta is partly branch selection, not claim content (see LOW-2, and D5's kill-rule-closure concern).
- **The pin itself forbids the obvious fix**: `claims.md:167` — "it is never edited after this revision" — and the sha256 is pinned at `:6`. Repair requires a re-declared pre-registration (or an L0 decision); it is not a same-revision patch. No edit was made here.

Corroboration: peer seats `L1Revenger69.R69AnchorCritic` and `L1Revenger69.R69DeriveCritic` reported the same crash and the same red-before contradiction; this seat reproduced both independently (HEAD-tree run, base-tree `cat-file`) with the contracted `cd / && TMPDIR=… python3 -B` invocation.

## FINDING HIGH-2 — C2's red-before paragraph contradicts the receipt it names

`claims.md:137-139`: "On the base tree: `Q15_PRESENT=no` …, `Q15_SELFTEST=pass` and `Q15_FALSE_KILLED=yes` (the checker ships with the claims revision and the D1 fixture is committed as evidence of the defect class)."

Observed, on the same base tree the receipt measures:
```
$ git cat-file -e 222a7a702529fb60598633ebdf5e1442007bc15d:corpus/q15_tree_id_check.py
fatal: path 'corpus/q15_tree_id_check.py' exists on disk, but not in '222a7a702529fb60598633ebdf5e1442007bc15d'
(exit 128)
$ sed -n '22,25p' reports/round-69/measure-before.log
Q15_PRESENT=no
Q15_SELFTEST=n/a (no checker)
Q15_FALSE_KILLED=n/a (no checker)
Q15_RESTATE_OK=n/a (no checker)
```
Two of the four red-before values the contract asserts are contradicted by the committed receipt. Precision matters for the remedy, so state the claim exactly:
- The labels are *attainable in principle* on the claims revision: the checker exists at `e1d22ca` (`git cat-file -e e1d22ca:corpus/q15_tree_id_check.py` → exit 0), so `Q15_SELFTEST=pass` / `Q15_FALSE_KILLED=yes` are its states — but it was added in `e1d22ca`, **not** in the base tree.
- The defect is placement: `claims.md:137` scopes the sentence to "**On the base tree**:" (base = `222a7a7`, `claims.md:4`), and its own named receipt prints `n/a` for all four labels.
- **No committed counter run has ever printed `Q15_SELFTEST=pass` on any tree.** The pass form is never *typed* in the counter: `grep -c 'Q15_SELFTEST=pass' reports/round-69/measure.py` → `0`, because `:160` is `print(f"Q15_SELFTEST={'pass' if q15_selftest else 'fail'} :: …")` — assembled, and `:158` dies before it. A literal search over the claim surface (`git grep -n "Q15_SELFTEST=pass" -- corpus reports/round-69`) returns only non-output occurrences: the checker's own print (`corpus/q15_tree_id_check.py:75`), the claims prose (`claims.md:130`, `:138`), and — written after this seat's window — the lesson's M48 row (`corpus/lessons/round-69.md:158`) quoting the label. The only emitted `Q15_SELFTEST` line in the repo is `measure-before.log:23` = `n/a (no checker)`. The trees that carry the checker are exactly the trees where `measure.py` dies at `:158` (HIGH-1).
- `reports/round-69/` holds only `claims.md`, `d1-false-sentence.md`, `measure-before.log`, `measure.py`; `git log --all -- reports/round-69/measure-after.log` → empty. No final-commit receipt exists.

Severity **high**: C2's red-before is the control half of the calibration claim, and two of its four named values have no receipt anywhere while being attributed to a tree that cannot produce them. Same class as round-68 D1 (assertion vs contradicting bytes), now inside the frozen pre-registration.

## 1. Pin check — exact match (positive)

```
$ sha256sum reports/round-69/measure.py
bca74e6d8b5010aee79886521474f072257ee22ec7ccc24e4186666bdc048377  reports/round-69/measure.py
```
`claims.md:6` pins `bca74e6d8b5010aee79886521474f072257ee22ec7ccc24e4186666bdc048377` → identical.

Blob identity at every state carrying the path (`git cat-file -p <rev>:reports/round-69/measure.py | sha256sum`):

| rev | role | content sha256 |
|---|---|---|
| `e1d22ca` | pre-registration | `bca74e6d…bdc048377` |
| `da02261` | intermediate HEAD reflog state, ancestor of HEAD | `bca74e6d…bdc048377` |
| `35e1258` | HEAD | `bca74e6d…bdc048377` |
| worktree | uncommitted | `bca74e6d…bdc048377` |

Object identity corroborates: `git rev-parse e1d22ca:reports/round-69/measure.py` = `git hash-object reports/round-69/measure.py` = `85a80f7a6b1f779dd619d3d02617e5ba608896c9`. `git status --porcelain -- reports/round-69/measure.py reports/round-69/claims.md reports/round-69/measure-before.log` → empty.

## 2. History — nothing changed the counter after pre-registration (positive)

```
$ git log --all --format='%H %ad %s' --date=iso -- reports/round-69/measure.py
e1d22caaf9a2fdc4c1c13d1f4a8a6813e7b07968 2026-10-25 03:48:46 -0300 round-69: pre-registration — claims …, frozen counter measure.py, Q15 checker, red-before receipt
e0d70dbfb04adc60bde319a7a063bc653b44b7b1 2026-10-25 03:48:46 -0300   (no subject; unreferenced pre-image)
b25c52c421c17dc7bbb8ff05e720cea62121c51f 2026-10-25 03:48:46 -0300   (no subject; unreferenced pre-image)
```
- Commits after `e1d22ca` that change the path: **0** (`git rev-list e1d22ca..HEAD -- reports/round-69/measure.py | wc -l` → `0`). `da02261`/`35e1258` are TREESAME (same blob), so history simplification omits them — consistent, not evasion.
- **Exactly one blob exists for the path in the entire object graph**: `for c in $(git rev-list --all); do git rev-parse "$c:reports/round-69/measure.py"; done | sort -u` → single line `85a80f7a6b1f779dd619d3d02617e5ba608896c9`.
- `e0d70db` (author `revenger-shokunin`) and `b25c52c` (author `protocol-shokunin`) are children of base `222a7a7`, subject-less, contained by **no ref** (`git branch -a --contains` empty). Both carry the *same pinned blob*, so they are jj-export residue of identical content — no divergence surface, but note they are not gc'd yet.
- Lineage claim checks out: `sha256sum reports/round-68/measure.py` → `0de4eb6f34bdb906fb69fdd173aaac9bcef629e6ff1d4c67f5ba8c91093f7766` = `claims.md:7`. `diff -u reports/round-68/measure.py reports/round-69/measure.py` is 86 lines and adds only the declared surface: `LANE` (`:30`), `C05_SINGLE_V4` (`:79-81`), `HOLDS_C2_V4` (`:123-125`), the Q15 block (`:151-184`), the `C7_V4_CLEAN` v4 arm (`:488-495`). V1–V6 gate expressions are not altered for the better (`holds_ok` `:557`, `holds_ok_v2..v6` `:561-575`; V6 still couples `c7_v3_clean` at `:575`) — D5 remains open exactly as declared. The HIGH-1 defect arrives **with** the Q15 block, i.e. the pre-registration revision itself introduced the unreachable pass branch.

## 3. Write containment — nothing written outside TMPDIR (positive)

Static: `measure.py` has no `open(...,'w')`, no `os.chdir`, no `os.environ` mutation, no hard-coded `/tmp`, no unlink/rename. Every write is `target.write_text` / `receipt.write_text` **inside** a `tempfile.TemporaryDirectory` (which honours `TMPDIR`) after `shutil.copytree(TREE/"corpus", work/"corpus")`: `:213/:215/:223-228` (`rev-r65-mut-`), `:264/:266/:274` (`rev-r65-c3-`), `:303/:305/:313` (`rev-r65-c4-`), `:347/:349/:357` (`rev-r65-c5-`), `:399/:401/:409` (`rev-r66-c6-`), `:451/:453/:461` (`rev-r67-c7-`), `:521/:523/:536` (`rev-r68-c7neg-`). Children run `-B` (`:188`, `:546`) → no `__pycache__` in the tree. `LANE` only feeds `--lane` (read-only `git rev-parse`) at `:164`/`:173`.

Invoked scripts: `corpus/q15_tree_id_check.py` performs no file write at all; only `subprocess.run(["git","-C",lane,"rev-parse", …])` at `:42` (sha256 `7d074f98cb7f9ff2be4c17e6b97e60ac8d660c827a32009d85a35df50639d276`). `corpus/check_embedded_outputs.py` writes only into `TemporaryDirectory(prefix="rev-r67-c7-selftest-")` (`:155`), fixtures at `:112-129`. `corpus/verify_*.py --self-test` contain no writes.

Empirical (base tree `222a7a7`, 507 files, digest `4eca46f4a876fa2f6a0be7a9c5a7c30a59ac0326af3038f5097e84ba3342ccb3`): contracted run → `exit=0`, 105 lines, 0 stderr, 2.5 s. Output **byte-identical** to the committed receipt (diff clean; both sha256 `e1cf90f357a94da84ab65ee4ef6d17bc0dc034f95b5458c735d3cce21edd6f29`). Tree digest unchanged after the run; `git status --porcelain --untracked-files=no` empty in the lane (new untracked entries are sibling seats' `.ufo/waves/round-69/*.md`); no `rev-r6*` residue left inside TMPDIR. This proves the receipt's provenance **and** that the receipt never exercised the branch that crashes (HIGH-1).

## FINDING LOW-1 — claims assert a counter pin *inside* `measure-before.log`; the receipt has none

`claims.md:166-167`: "The counter's sha256 is pinned above and in `measure-before.log`". The committed 105-line receipt (sha256 `e1cf90f3…`) contains no digest: `grep -oE "[0-9a-f]{64}" reports/round-69/measure-before.log` → empty; `grep -niE "sha|bca74e|0de4eb"` matches only incidental payload substrings at `:18` (`…_export_shapes`) and `:97` (`verify_shape_evidence.py`). Same class as round-68 D1 (asserted fact contradicted by the artifact named). Bounded impact: the pin exists at `claims.md:6` and in git (`85a80f7…`), and the receipt reproduces byte-for-byte from the pinned counter.

## FINDING LOW-2 — exit 0 would not certify the round-69 clauses even if the crash were fixed

Structurally, `evaluable = True` (`:184`) is unconditional, and `holds_ok` (`:557`) folds in neither `C05_SINGLE_V4` (`:81`) / `HOLDS_C2_V4` (`:125`), nor `C7_V4_CLEAN` (`:493`), nor any `Q15_*` (`:151-180`); the Q15 `else` arms set `n/a` without touching `evaluable`. So exit 0 would remain necessary-but-not-sufficient for both claims — safe only if a seat reads the printed labels. That is precisely D5's "kill-rule closure over every mechanical conjunct" surface; recorded, not pre-empted (the C7/L0 instrument is untouched).

## Residual risk / verification gaps
- The **after** measurement is not producible with the frozen counter at all (HIGH-1); my base-tree replay authenticates the receipt but cannot validate the pass branch. C1's `C7_V4_CLEAN` and C2's Q15 label set are unverifiable on the landed tree until the instrument is re-declared.
- Q15 ability-to-fail on the D1 fixture is owned by `R69Q15CheckerRun`; this seat only established that the checker is read-only and that the counter cannot reach its verdict calls.
- **What `C7_V4_CLEAN=yes` would certify (C1, not counter bytes).** `corpus/check_embedded_outputs.py` compares only fenced ` ``` $ cmd``` blocks: `parse_blocks` (`:44-68`) collects lines between a `$ ` marker and the closing fence, and `drift` (`:83-85`) tests those lines against the command's stdout set. Prose anchors outside a fence — e.g. a stated `:244` bound or `RES_XML_FIRST_CHUNK_TYPE` value — are never read by the gate. So after HIGH-1 is repaired, `C7_V4_CLEAN=yes` would still not mean "every anchor the entry states is derived"; a prose-anchor leg is needed to close C1. Cross-checked with peer seat `R69AnchorCritic`, which demonstrated a prose-only edit passing the gate (exit 0) while the in-block edit is caught (exit 1); this seat verified the gate's scope at the cited lines.
- History claims are scoped to this lane's object store; the counter verifies Q15 tree ids against the fixed `LANE` path (`:30`), so a run from a different clone re-derives against *this* lane.
- No package installs/upgrades were performed; no tool version changed (none needed).
- Scratch `/tmp/revenger-r69-tmp`, `/tmp/revenger-r69-head` deleted after evidence capture.

## Evidence index
- `reports/round-69/claims.md:6` (pin), `:7` (round-68 lineage), `:96-107` (C1 predicate, exit 0 at `:104`), `:127-137` (C2 predicate, exit 0 at `:135`), `:166-167` (pin-in-log assertion + "never edited"), `:193` (void: counter exit non-zero at final)
- `reports/round-69/measure.py:30,79-81,123-125,151-184,187-190,213-228,264-274,303-313,347-357,399-409,451-461,488-495,521-536,546,557,577`
- `reports/round-69/measure-before.log` (105 lines, sha256 `e1cf90f357a94da84ab65ee4ef6d17bc0dc034f95b5458c735d3cce21edd6f29`; Q15 n/a at `:23-25`)
- `corpus/q15_tree_id_check.py:42`; `corpus/check_embedded_outputs.py:112-129,155`
- git objects: `85a80f7a6b1f779dd619d3d02617e5ba608896c9` (only measure.py blob in the repo), refs `e1d22ca` / `da02261` / `35e1258`, dangling `e0d70db` / `b25c52c`
- `git grep -n "Q15_SELFTEST=pass" -- corpus reports/round-69` → `corpus/q15_tree_id_check.py:75`, `reports/round-69/claims.md:130`, `:138` (plus `corpus/lessons/round-69.md:158` written after this seat's window) — prose/print occurrences only, never an emitted counter line; `grep -c 'Q15_SELFTEST=pass' reports/round-69/measure.py` → `0` (`:160` is an f-string, `:180` prints `n/a`); `reports/round-69/measure-before.log:23` is the only emitted `Q15_SELFTEST` line
- `git cat-file -e e1d22ca:corpus/q15_tree_id_check.py` → exit 0; `git cat-file -e 222a7a7:corpus/q15_tree_id_check.py` → exit 128; `git log --all -- reports/round-69/measure-after.log` → empty
