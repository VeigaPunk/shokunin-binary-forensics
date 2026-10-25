GATE-CATCHES-DRIFT — the registered gate, run in entry mode on the C05 v3 candidate, killed a one-byte drift at the exact line it was injected (exit 1, `drift entry:25 …`, `checked_blocks=17 problems=1`), and returned exit 0 / `checked_blocks=17 problems=0` on the same bytes unmutated.

Seat: L1Revenger68.R68MutC7Entry · round 68 · 2026-10-25 · read-only leaf (no lane writes; lane tree re-hashed after the probe).

## Axes named (godspeed)

1. **Calibration of the C1 artifact against the C2 artifact** — does the repaired `corpus/check_embedded_outputs.py` actually discriminate drift in the *real* v3 entry (not only in its hermetic self-test)?
2. **Attribution precision** — does the emitted message name the true entry line, so a kill is attributable and not merely "non-zero exit"?
3. **Coverage honesty** — what part of the entry's 47 quoted output lines the gate *does not* defend, so `C7_V3_CLEAN=yes` is not over-read.

## Probes (all in one disposable scratch tree, never the lane)

Scratch tree: `/tmp/r68mutc7-IISaEZ/corpus` (`cp -a` of the lane's `corpus/`, 505 files); pristine candidate copy `/tmp/r68mutc7.pristine.md`. Every run: `cd /tmp/r68mutc7-IISaEZ && python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-68-apk-axml-byte-evidence.md`.

| probe | mutation to the v3 candidate | detector output | exit | verdict |
|---|---|---|---|---|
| baseline | none (pristine) | `checked_blocks=17 problems=0` (last line) | 0 | clean, as required |
| **A (assigned)** | entry line 25, item-1 block: `"bytes": 947` → `"bytes": 948` | `drift entry:25 embedded output line not in recheck stdout: {"bytes": 948, …}` + `checked_blocks=17 problems=1` | 1 | **KILLED** |
| B | entry line 200, first line of the 15-line full-run block: `947` → `948` | `drift entry:200 …` + `problems=1` | 1 | KILLED |
| D | one bogus line *appended* to the item-1 block (`"sha256": "deadbeef"`) | `drift entry:26 …` + `problems=1` | 1 | KILLED |
| C | item-1 output line *deleted* from its block | `checked_blocks=17 problems=0` | 0 | **SURVIVED** (coverage gap, see F1) |
| E | full-run block line 200 replaced by a byte-for-byte duplicate of its own line 202 (the eocd line) | `checked_blocks=17 problems=0` | 0 | **SURVIVED** (coverage gap, see F2) |
| self-test | `--self-test` on the same bytes | `SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired` | 0 | pass |

Probe A is the assigned mutant verbatim; B, D, C, E are the same detector aimed at a different shape of the same surface.

**Probe A raw transcript** (mutated sha256 `2b23f301f2858f4436e3ccc4b62b9de9d000f0489fb9209dfbc579d53f131d93`):

```
drift entry:25 embedded output line not in recheck stdout: {"bytes": 948, "fact": "archive", "path": "corpus/fixtures/apk-r65/fixture.apk", "sha256": "05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e"}
checked_blocks=17 problems=1
MUT_RC=1
```

Named line check: `sed -n '25p'` of the mutated file is exactly the quoted `{"bytes": 948, …}` line — the message's `entry:25` is the line actually altered, not the enclosing `$ cmd` line (which is 24). Attribution is precise.

**Baseline raw transcript** (unmodified sha256 `107e2d7483e57e64476ead408f2eb793f41e3eea5e3c96407763eadca6dfea5b`):

```
checked_blocks=17 problems=0
BASE_RC=0
```

Exit 0 with 0 problems, and 17 is exactly the number of `^\$ ` block headers in the file (`grep -c '^\$ '` = 17), so no block was skipped and none silently failed to evaluate (an unevaluable command would exit 2 at `corpus/check_embedded_outputs.py:107-108`).

## Gate mechanics this exercises (pointers)

- `corpus/check_embedded_outputs.py:83-85` — `drift()` emits `drift entry:{out_lineno} …` where `out_lineno` is the output line's own number in the entry (`parse_blocks` records `j + 1`, `:56-63`), which is why A names 25 and not 24.
- `:104` — `stdout_set = set(stdout.splitlines())`: a **set**, per block, of that block's own command stdout. Line-granular and block-local: a drifted line can never be satisfied by another block's output, which is what makes A/B/D real kills.
- `:105` — the frozen mutant target of C1 sits here; this probe confirms the *unmutated* call is load-bearing on the real entry, i.e. the C1 mutant removal is a real behavioral loss and not a cosmetic one.
- `:140-145` — the round-68 attributed branch; the `--self-test` probe above walks it (`print(MARKER)` at `:144`, `MARKER` defined `:36`).

## Findings (coverage, not contract changes)

- **F1 — a deleted quoted line is invisible.** `drift()` only asks "is each embedded line in stdout?", so removing an embedded line removes the obligation (`:85`); probe C deleted item 1's output line and the run still exits 0 with `problems=0`. `C7_V3_CLEAN=yes` therefore means *"every quoted line is in stdout"*, not *"the entry quotes stdout completely"*. It cannot detect an omission-style drift (the M39 class is a transcription *change*, so the gate does cover the defect class it was built for; the omission variant is simply out of scope).
- **F2 — set, not multiset; a duplicate substitution survives.** Probe E replaced one line of the 15-line full-run block with an exact duplicate of another line of the same block; both are in `stdout_set`, so `problems=0` even though the block no longer quotes the archive line it claims to quote. A quoted block's line *count* and line *order* are unverified.
- Both F1 and F2 are narrow (they require an attacker who already controls the entry bytes) and neither touches the assigned question. Recorded so the wave does not read `C7_V3_CLEAN=yes` as a completeness claim: it is a verbatim-subset claim.

## Restoration evidence

| artifact | before probe | after probes |
|---|---|---|
| scratch candidate | `107e2d7483e57e64476ead408f2eb793f41e3eea5e3c96407763eadca6dfea5b` | `107e2d7483e57e64476ead408f2eb793f41e3eea5e3c96407763eadca6dfea5b` (`diff -q /tmp/r68mutc7.pristine.md` → **IDENTICAL**) |
| lane `corpus/knowledge/round-68-apk-axml-byte-evidence.md` | `107e2d7483e57e64476ead408f2eb793f41e3eea5e3c96407763eadca6dfea5b` | unchanged (same hash; `git status --porcelain corpus` empty) |
| lane `corpus/check_embedded_outputs.py` | `b89183bec2fd3b94f5b0acc828a0d3fe16f6a98dde1d7752616da85d08a8e0ca` | unchanged |
| lane `corpus/derive_axml_anchors.py` | `bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249` | unchanged (matches the S046 row sha256) |
| lane `corpus/snapshots/ResourceTypes.h` | `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f` | unchanged (86255 bytes claimed; hash matches the row) |

Restoration was `cp /tmp/r68mutc7.pristine.md` after every mutant and was re-verified by sha256 before the next mutant; the final hash equals the lane's own, and the lane tree was not written at any point (all writes went to `/tmp/r68mutc7-*` plus this report). No git/jj command with a mutating verb was run.

## Caveats

- The scratch tree is a worktree copy, not a `git archive` tree; it is byte-identical for the three files that matter (verified by sha256) and contains the same 505 files.
- `$`-block selection is fence-based (`:47-52`), so this probe says nothing about prose claims outside fences — item 1's prose "**947 bytes**" is unguarded by the gate even though the fenced line is guarded. That is consistent with the gate's declared scope (quoted output only).
- No tool installed or upgraded in this seat; no package-manager transaction was attempted.

## Environment observation (not mine, no action taken)

`git status --porcelain corpus` in the lane reports one entry: `?? corpus/__pycache__/` holding `check_embedded_outputs.cpython-314.pyc` (9356 bytes, mtime 2026-10-25 03:29:00 -0300). It is not mine: every Python invocation in this seat used `-B` and ran with `cwd=/tmp/r68mutc7-IISaEZ`, and that scratch tree contains **0** `.pyc` files (`find … -name '*.pyc' | wc -l` = 0). Something else in the concurrent wave imported `corpus/check_embedded_outputs` without `-B` from a lane-relative path. Recorded only — I did not delete it (corpus is read-only for this seat). It cannot contaminate the measured tree: `git archive <commit>` never emits untracked paths, so the counter's trees are unaffected; it does mean a lane-rooted `python3` run without `-B` is currently happening somewhere in the wave.
