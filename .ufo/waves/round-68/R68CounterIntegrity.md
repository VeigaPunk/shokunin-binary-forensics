INTACT — reports/round-68/measure.py hashes to the pinned 0de4eb6f…f7766, no commit after the pre-registration f505526 touched it (blob 4f6b6398 identical at f505526, HEAD and worktree), every write site is inside `tempfile.TemporaryDirectory`, and a full replay mutated 0 of 505 corpus files with 0 TMPDIR residue.

# R68CounterIntegrity — counter integrity (C1/C2 frozen instrument)

Seat: leaf, read-only except this file. No tool installs (no tool needed; nothing installed or upgraded).
Scope: the frozen counter `reports/round-68/measure.py` only — pin, history, write containment, replay of the red-before receipt. Claims/entry/registry review belongs to sibling seats and is not judged here.

## 1. Pin check — MATCH

```
$ sha256sum /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-68/measure.py
0de4eb6f34bdb906fb69fdd173aaac9bcef629e6ff1d4c67f5ba8c91093f7766  .../reports/round-68/measure.py
```
Pin sources, both exact and identical to the computed value:
- `reports/round-68/claims.md:7` — ``counter: `reports/round-68/measure.py` sha256 `0de4eb6f…f7766` ``
- `reports/round-68/measure-before.log:102` — `counter: reports/round-68/measure.py sha256 0de4eb6f…f7766 (never edited after pre-registration)`

File metadata: 24360 bytes, mtime `2026-10-24 23:22:17`, mode `-rw-r--r--`, owner `vgpnk:vgpnk`. The mtime precedes the pre-registration commit (`2026-10-24 23:22:41`), i.e. the file on disk is the file that was committed.

## 2. Commit history — no post-registration change

```
$ git log --format='%H %s' -- reports/round-68/measure.py
f505526f7ecf4ac1ad51d99aa2d1dd5c57c0bae0 round-68: pre-registration — … frozen counter 0de4eb6f, red-before receipt on base f165908
```
Exactly one commit in this repository's reachable history bears this path. `git log --follow --name-status` shows the path was a **rename/copy forward** each round (`C084 reports/round-67/measure.py reports/round-68/measure.py` at f505526, `C075` r66→r67, `C079` r65→r66, `C074` r64→r65, `C060` r63→r64, `C053` r61→r63, then `M`/`A` at r61), so each round legitimately repins a new sha (round-67's pin was `7933c060…bc07e`); the round-68 pin is the freeze of *this* revision, not a claim that the bytes are unchanged since r67.

Post-registration range, empty — nothing after the freeze touched it, including the build commit `4232235`:

```
$ git log --format='%H %s' f505526…..HEAD -- reports/round-68/measure.py
(empty)
```

Content identity, three ways (all equal ⇒ the frozen bytes are the committed bytes at the measured tip):

```
f505526:4f6b6398156a1ba0e38ee9cd33c59700a231898d
HEAD:   4f6b6398156a1ba0e38ee9cd33c59700a231898d
worktree:4f6b6398156a1ba0e38ee9cd33c59700a231898d   (git hash-object)
```
`git merge-base --is-ancestor f505526 HEAD` → **YES**: the pinned pre-registration commit is an ancestor of HEAD `4232235723cf8d4731a1e7e78ca098b8af953a57`, so the pin is not a dangling/orphaned object and history was not rewritten out from under it. `git check-attr -a reports/round-68/measure.py` → no attributes (no smudge/CRLF filter that could make worktree ≠ blob).

The one post-freeze corpus change is the **C1 build** itself: `4232235` (2026-10-24 23:22:51) touches `corpus/check_embedded_outputs.py`. That is the declared build state, not an instrument change.

## 3. Write containment — static audit

```
$ grep -n "open(\|write_text\|write_bytes\|mkstemp\|mkdtemp\|tempfile\|TMPDIR\|shutil\|os\.remove\|unlink\|rmtree" measure.py
25:import shutil        26:…      28:import tempfile
172/223/262/306/358/410/472: with tempfile.TemporaryDirectory(prefix="rev-r65-mut-"|"rev-r65-c3-"|"rev-r65-c4-"|"rev-r65-c5-"|"rev-r66-c6-"|"rev-r67-c7-"|"rev-r68-c7neg-") as tmp:
174/225/264/308/360/412/474: shutil.copytree(TREE / "corpus", work / "corpus", symlinks=True)
182/233/272/316/368/420/487: target.write_text(...)     187: receipt.write_text(...)
```

- **No `open(` call exists in the file at all.** There are exactly 8 write calls, all `Path.write_text`.
- Every one is inside a `with tempfile.TemporaryDirectory(...) as tmp:` block and every target is derived from `work = pathlib.Path(tmp)`:
  - `target = work / "corpus" / <script>` (182, 233, 272, 316, 368, 420, 487)
  - `receipt = work / f"corpus/live/runs/round-{round_id}/producer-receipt.json"` (184–187)
- `shutil` is used only for `copytree(TREE/corpus → work/corpus)` — source read-only. `tempfile.TemporaryDirectory` resolves through `gettempdir()`, which honours `TMPDIR`; the counter reads no environment variables itself (`grep -n "os.environ\|getenv"` → empty) and contains **no absolute path literals** (`grep -n "/home/\|/tmp/"` → empty), so `TREE` is the only input path.
- No `rmtree`/`unlink`/`os.remove`: destruction is `TemporaryDirectory.__exit__` only.
- Measured-tree executions exist (`run(TREE, …)` at 405/429/434/441; `subprocess.run(..., cwd=TREE)` at 497) but all are read-only by construction: `-B` on every interpreter invocation (lines 147, 497) ⇒ no `__pycache__`/`.pyc` writes; `verify_*.py` contain **zero** write calls (`grep -n "open(\|write_text\|write_bytes\|os\.replace\|shutil\.copy\|mkdir" verify_*.py` → no matches across all 10 files); and `check_embedded_outputs.py` writes only inside its own `TemporaryDirectory` (`_self_test(tmp)`, `check_embedded_outputs.py:110-112,123-129,154-157`), while `--entry` mode only reads and exits (`:160-166`). So the `run(TREE, …)` legs cannot write into the measured tree.
- `copytree(symlinks=True)` is not an escape surface here: `find corpus -type l` → **count=0**, so no symlink in the corpus can redirect a temp-copy write back to a lane path.

## 4. Write containment — empirical

Decisive test: extract HEAD `corpus` into a scratch tree, hash all files, run the pinned counter exactly as the claims' invocation contract specifies with a private `TMPDIR`, re-hash.

```
$ git archive HEAD corpus | tar -x -C $T          # 505 files, 5.6M
$ (cd $T && find . -type f -print0 | sort -z | xargs -0 sha256sum) > before
$ cd / && TMPDIR=$X python3 -B …/reports/round-68/measure.py $T > run.log; echo exit=$?
counter_exit=0            (2.63 s)
$ diff before after
(empty)  → IDENTICAL 505 files
$ find $X -mindepth 1 | wc -l
0                        → TMPDIR empty after run (all rev-* dirs removed)
```
Lane untouched by the run: `find $LANE/corpus $LANE/SKILL.md -type f -mmin -10` → no matches; `find corpus -name __pycache__ -o -name '*.pyc'` → none; `git --no-optional-locks status --porcelain` shows only sibling seats' untracked `.ufo/waves/round-68/*` files, no tracked modification.

HEAD replay output (build state, exit 0):
```
C7_MUTANT_KILLED_ATTRIBUTED=1/1
C7_NEG_SPOOF_KILLED=1/1        C7_NEG_SPOOF_KILLED_ATTRIBUTED=0/1
C7_V3_CLEAN=yes exit=0 :: checked_blocks=17 problems=0
C05_STATUS=uncovered   C05_SINGLE_V3=no   HOLDS_C2_V3=no   K_HELD_BACKED=8/14
HOLDS_OK=yes … HOLDS_OK_V5=yes   HOLDS_OK_V6=yes
```
This is consistent with the declared build state: the C7 repair and the round-68 candidate are live and clean, while the C05 README row is **not** flipped (`C05_STATUS=uncovered`), so the coverage claim's target is still unreached by design.

## 5. Red-before receipt reproducibility — reproduced

Replayed the pinned instrument on base `f165908aaffcf14798de53405fe788986bd33ff9` (`git archive f165908 corpus` → scratch tree, private TMPDIR):

| label | measure-before.log | my replay |
|---|---|---|
| `K_HELD_BACKED` | 8/14 | 8/14 |
| `C05_STATUS` | uncovered | uncovered |
| `HOLDS_C2_V3` | no | no |
| `C7_MUTANT_KILLED_ATTRIBUTED` | 0/1 | 0/1 |
| `C7_NEG_SPOOF_KILLED_ATTRIBUTED` | 0/1 | 0/1 |
| `C7_V3_CLEAN` | n/a (no v3 file) | n/a (no v3 file) |
| `HOLDS_OK_V5` / `V6` | no / no | no / no |
| counter exit | 0 | 0 |

The committed receipt is reproducible with the committed instrument. Note the exit-contract nuance, which is **not** a contradiction: `sys.exit(2 if not evaluable else 0 if holds_ok else 1)` (measure.py:528) tracks the V1 aggregate `holds_ok` only, so exit 0 co-exists with `HOLDS_OK_V5=no`/`V6=no`. `evaluable` is initialised at `measure.py:143` (`evaluable = True`), so the `not evaluable` branch cannot raise `NameError`; the red-before log's "counter exit code: 0 (the V1 holds hold; HOLDS_OK_V5=no …)" is an accurate parenthetical.

## 6. Informational (no action; the file is frozen)

1. `measure.py:2` still reads `"""Round-67 counting probe (frozen in reports/round-67/claims.md).` while this revision is frozen by `reports/round-68/claims.md`. Provenance-stale docstring only; `claims.md:151-153` correctly describes the file as "the round-67 counter plus the round-68 labels". Editing it would break the pin, so it must stay.
2. The only write-adjacent risk surface is the in-tree execution legs (405/429/434/441/497): containment there depends on the *tree's* gate/verifier scripts being read-only, which holds today (verified statically and by the 505-file hash identity) but is a property of those scripts, not of the counter. If a future gate starts writing beside itself, the counter would relay that write into the measured tree.
3. `/tmp/rev-r68-diag-tRwg` (created 2026-10-25 03:24:39, contains a `corpus/` copy) is **not** counter residue: the counter's only temp prefixes are `rev-r65-mut-`, `rev-r65-c3-`, `rev-r65-c4-`, `rev-r65-c5-`, `rev-r66-c6-`, `rev-r67-c7-`, `rev-r68-c7neg-` (measure.py:172,223,262,306,358,410,472). It is a sibling seat's diagnostic tree; left untouched.
4. **Untracked `corpus/__pycache__/check_embedded_outputs.cpython-314.pyc` appeared in the lane at 03:29:00** (9356 bytes) during this wave. Attribution: **not this seat and not the counter.** The pyc embeds `co_filename = /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/check_embedded_outputs.py` with source mtime `2026-10-24 23:22:16` / size `6791`, matching `corpus/check_embedded_outputs.py` (`6791` bytes, same mtime) — so a sibling process **imported the lane module without `-B`**. The counter never imports the gate (it only `subprocess`-invokes it, always with `-B`: measure.py:147, 497; main run also `-B`), so neither of my two replays could have produced it; static grep/read calls cannot either. Impact on measurement: **none** — the counting contract extracts `corpus` via `git archive`, so untracked working-tree files never enter the measured tree (my 505-file hash set is exactly the HEAD archive). Risk if unattended: a `git add -A` would commit the pyc into `corpus/`. It changes no `corpus/live` or `corpus/fixtures` byte, so the claims' void conditions are not triggered. Left in place: not mine to delete while the owning seat may still be running.

## 7. Verification gaps

- No `lsp` device is available in this seat's toolset, so the prescribed LSP references/definition/diagnostics passes were impossible; the brief's own method (grep + sha256 + commit history) was used, and no grep result is presented as semantic proof beyond the literal write/read sites cited with line numbers.
- Only the round-68 counter was audited; earlier rounds' counters (round-61…67 paths, reachable via the rename chain) were not re-verified — out of scope and irrelevant to this pin.
- Containment was proven by content hashing and process behaviour, not by syscall tracing (`strace`); a write to a path outside both `TREE` and `TMPDIR` that leaves no residue would not be caught by content hashing. No such path exists in the source (no absolute path literals, no `open(`), so this residual is theoretical.
- Replays used HEAD and `f165908`; the final measured tip may differ from HEAD, in which case the pin must be re-checked only if `measure.py` itself changes — it cannot, per §2.

Scratch dirs created by this seat under `/tmp/r68ci-*` were removed after the runs; nothing outside this report was written in the lane.
