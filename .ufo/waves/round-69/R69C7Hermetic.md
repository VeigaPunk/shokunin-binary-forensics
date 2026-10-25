HERMETIC — 3/3 self-test runs exit 0 with byte-identical stdout (sha256 `bcd32f26…ccf1d`), the temp tree appears only under the caller's fresh `TMPDIR` and is removed, and a syscall-level trace shows **zero** mutating operations outside `TMPDIR` on the lane tree; the lane is byte-clean across every run window, with the concurrent `git status` churn attributable to sibling seats by mtime and excluded by path-level snapshots.

Seat: `L1Revenger69.R69C7Hermetic` (leaf, no subagents, no peer messages) · lane `/home/vgpnk/Projects/shokunin/revenger-shokunin` · HEAD `35e12584d37434632fa06a6c2975ab55f29a8d3f` · gate `corpus/check_embedded_outputs.py`, 6791 B, sha256 `b89183bec2fd3b94f5b0acc828a0d3fe16f6a98dde1d7752616da85d08a8e0ca` (identical before and after all probes) · python3 3.14.8 (GCC 16.2.1) · no packages installed or upgraded (host pacman paused); `strace` was already present, nothing was fetched.

## 1. The three required runs

Invocation (cwd = lane root, each with its own freshly created `TMPDIR`, `PYTHONDONTWRITEBYTECODE` unset so `-B` alone is responsible):

```
TMPDIR=<fresh> python3 -B corpus/check_embedded_outputs.py --self-test
```

| run | TMPDIR | exit | stdout | sha256(stdout) | wall |
|---|---|---|---|---|---|
| 1 | `/tmp/revenger-r69-hermetic/TMPDIR1` | **0** | `SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired` | `bcd32f26ad4ec7e9683b3512d305a57fc69d3419b98f72d126d1bc5925cccf1d` | 0.056 s |
| 2 | `…/TMPDIR2` | **0** | identical | `bcd32f26…ccf1d` | 0.057 s |
| 3 | `…/TMPDIR3` | **0** | identical | `bcd32f26…ccf1d` | 0.055 s |

- stdout is exactly 81 bytes including the trailing `\n`; stderr empty on every run.
- **Byte-identical across all three runs: yes** (single unique sha, `len(set)==1`).
- Determinism is structural, not accidental: the only output path is the literal `print` at `corpus/check_embedded_outputs.py:146`; no temp path, no random suffix, no timing value reaches stdout. The random temp-root suffix (`f1_7al5j`, `bziz5f04`, `7ionprg9`) is therefore invisible to the receipt, which is what makes the receipt stable.

## 2. What appeared in the fresh TMPDIR (and what was left behind)

A 3 ms poller sampled each `TMPDIR` for the whole run:

- transient: `<TMPDIR>/rev-r67-c7-selftest-<8 randoms>` — the `tempfile.TemporaryDirectory(prefix="rev-r67-c7-selftest-")` root from `:143`.
- **remaining after exit: `[]` on all three runs** (0 entries).

Content of that transient dir, resolved from the strace run (`TMPDIR4`):

| path | bytes | syscall |
|---|---|---|
| `<tmp>/reader.py` | 258 | `openat(…, O_WRONLY\|O_CREAT\|O_TRUNC\|O_CLOEXEC, 0666)` |
| `<tmp>/clean.md` | 62 | idem |
| `<tmp>/drifted.md` | 62 | idem |
| `<tmp>/full.md` | 75 | idem |
| `<TMPDIR>/edfd71q4` (probe) | 4 (`"blat"`) | `openat(…, O_RDWR\|O_CREAT\|O_EXCL\|O_NOFOLLOW\|O_CLOEXEC, 0600)` |

The `"blat"` probe is CPython `tempfile._get_default_tempdir`'s writability check, and it lands **inside `TMPDIR`**, so the temp root really is taken from `TMPDIR` (default-env run in §5 confirms the `/tmp` variant). Fully cleaned: `unlink` ×4 + `unlinkat` ×4, `rmdir` ×1, probe `unlink` ×1.

## 3. Did anything appear in the lane?

`git -C /home/vgpnk/Projects/shokunin/revenger-shokunin status --porcelain`:

- before run 1: `?? .ufo/waves/round-69/assimilation/`
- after run 1, 2 and 3 (identical string each time): `?? .ufo/waves/round-69/R69SpotcheckDiscern.md` + `?? .ufo/waves/round-69/assimilation/`
- at the last snapshot of my probes (07:16): 8 `??` lines, all under `.ufo/waves/round-69/`; churn continued after that sample — the same directory now holds 37 seat reports plus my own `R69C7Hermetic.md` (38 lines at 07:17:31).

Under a 64-seat wave `git status` is **not** a sufficient instrument (untracked, gitignored and transient files are invisible or unattributable), so attribution used two stronger instruments:

1. **Path-level inventory** of the whole lane excluding `.git` — 3035 files keyed by `(relpath → [size, mtime_ns])` — snapshotted immediately before and immediately after each run (±~150 ms).
   Result: **diff = `{}` for all three runs** (no file created, modified or deleted, including under `.ufo/`).
2. **Syscall trace** of a fourth run (`strace -f -e trace=%file,write,pwrite64,clone,execve`, 1253 lines):
   `awk '/O_CREAT|O_WRONLY|O_RDWR|mkdir|unlink|rename|rmdir|chmod|symlink/'` yields exactly **12 unique mutating operations, every one under `/tmp/revenger-r69-hermetic/TMPDIR4`** (listed in §2). Writes are only `fd 1` (10 × stdout) and `fd 3` (5 × the temp files/probe); nothing to stderr, nothing to a lane path. Lane accesses are read-only: `openat(…/corpus/check_embedded_outputs.py, O_RDONLY)`, `openat(…/corpus, O_RDONLY|O_DIRECTORY)`, `newfstatat`, `getcwd`, `readlink` only.
3. `find corpus -name '__pycache__' -o -name '*.pyc'` → **empty**, so `-B` suppressed bytecode writes.

**Attribution of the `git status` churn:** in the 07:16 sample the then-present sibling files carry mtimes `07:15:04`–`07:16:02` (`R69SpotcheckDiscern` 07:15:04, `R69MutC7Entry` 07:15:19, `R69Item10` 07:15:23, `R69MutC7Kill` 07:15:29, `R69Item9` 07:15:32, `R69Item1` 07:15:41, `R69Item3` 07:15:50, `R69CounterReplay` 07:15:57, `R69Item4` 07:15:57, `R69ReviewEntryQ07` 07:16:02) — each is a distinct peer report, and each landed **between** run windows where the path-level diff was empty. No lane write is attributable to the gate.

## 4. Harder controls (all exit 0, stdout sha `bcd32f26…ccf1d`)

| control | why it matters | result |
|---|---|---|
| cwd = `/` (`os.access("/", W_OK)` = **False**) | the counter runs the gate with `cwd=TREE` (`reports/round-69/measure.py:187-191`), so cwd-write freedom must be real | exit 0, identical stdout, no residue |
| cwd = `chmod 0555` dir | decisive: an unwritable cwd cannot absorb a stray write | exit 0, identical stdout, cwd empty, `TMPDIR` empty |
| 8 concurrent runs, 8 fresh `TMPDIR`s | the wave may run the gate from many seats at once | 8/8 exit 0, **one** unique stdout sha (equal to the single-run sha), stderr empty, all 8 `TMPDIR`s empty |
| `TMPDIR` unset (ambient `/tmp`, 36 418 entries) | the default path most callers take | exit 0, identical stdout, **0 new `/tmp` entries** (snapshot before/after), no `rev-r67-c7-selftest-*` residue |
| stdlib shadowing of `sys.path[0]` = `corpus/` | this is the M45 shadowing class; the gate imports `json, shlex, subprocess, sys, tempfile, pathlib` | none of `corpus/*.py` (13 files) collides with any imported module name — no shadowing on this tree |
| claims base ancestry | supports the Q15 identity framing this wave turns on | `222a7a7` **is** an ancestor of HEAD; 3 commits ahead (`e1d22ca` pre-registration, `da02261` build, `35e1258` wave prep) — no discrepancy |

## Findings

No HIGH or MEDIUM finding. The gate's `--self-test` behaviour is hermetic and deterministic on this host as measured. Three LOW findings and one nit remain, all outside the lane tree:

**LOW-1 — SIGKILL leaves the temp tree behind (temp-only residue).** Killed at 20 ms and 35 ms after spawn (both alive at kill, `rc=-9`), the run left `<TMPDIR>/rev-r67-c7-selftest-2erv2q__` and `…-ba7y_595` containing `reader.py` 258 B, `clean.md` 62 B, `drifted.md` 62 B, `full.md` 75 B — 2/2 probes. `tempfile.TemporaryDirectory` cleanup is a `__exit__`/atexit path, so `SIGKILL` cannot run it (`corpus/check_embedded_outputs.py:143`). No lane write occurs; under this wave's dead-seat conditions dead gates will dribble 4 small files per kill into `/tmp`. Cleanup: the dir is safe to `rm -rf`; nothing in the lane depends on it.

**LOW-2 — a bogus `TMPDIR` degrades silently to `/tmp`, and the receipt cannot show which root was used.** With `TMPDIR=/tmp/revenger-r69-hermetic/NOPE-does-not-exist` (never created) the run still exits **0** and the temp root becomes `/tmp`: `mkdir("/tmp/rev-r67-c7-selftest-nindwcbc")`, after a failed probe at `<bogus>/v8hxk5eq` (ENOENT); no dir was created under the bogus path. Because the self-test's stdout names no paths (§1), a committed "fresh TMPDIR" receipt is unfalsifiable from its own bytes. This bites the sanctioned counter recipe, which sets `TMPDIR=/tmp/revenger-r69-counter-XXXX` (`reports/round-69/claims.md`, §Frozen counter ↔ invocation contract) while `run()` at `measure.py:187-191` passes **no `env=`** — so the counter's `C7_SELFTEST` inherits whatever `TMPDIR` the operator actually created; if that `mkdir` was skipped, `C7_SELFTEST=pass` would still print. Fix shape (not applied, no edit authority): have `--self-test` echo its resolved temp root, or assert `Path(tempfile.gettempdir())` equals `$TMPDIR` when it is set. Janitorial: the probe/`/tmp` fallback left nothing behind (verified: 0 new `/tmp` entries).

**LOW-3 — hermeticity is claimed in the docstring but not asserted by the self-test (calibration gap).** `corpus/check_embedded_outputs.py:30-31` states "it writes nothing outside its own temp dirs", yet `_self_test` calls `evaluate(entry, tmp)` with `cwd=tmp` (`:126`, `:133`, `:138`), so a regression that wrote into cwd or the lane would write *inside the temp tree* and still print `SELFTEST OK`. The round-68 forged control covers only the drift branch (marker `drifted entry output accepted`, `:141-146`); there is no marker for the no-write property. Consequence for this wave: `C7_SELFTEST` (exit-code-only, `measure.py:446-448`) **cannot** falsify a hermeticity regression — my HERMETIC verdict rests on the external `strace` + 3035-file snapshot evidence above, not on the gate's own self-test. A cheap repair would be a snapshot of a sentinel dir (or an atexit assertion that `Path.cwd()` is unmodified) with its own attributed marker.

**NIT — `-B -B` reaches the child.** `run_cmd` prepends `-B` and the fixture command string already contains it, so the trace shows `execve("/usr/bin/python3", ["/usr/bin/python3","-B","-B","reader.py","--fact","a"])`. Behaviourally inert; noted only so a future reader of a trace does not suspect a doubled-flag defect.

## Residual risk and verification gaps

- Scope is `--self-test` only. I did **not** run `--entry` against `corpus/knowledge/round-69-apk-axml-byte-evidence.md`; that is `R69ReviewC7Gate`'s item, and `C7_V4_CLEAN` is not adjudicated here.
- Determinism was measured on one interpreter (python3 3.14.8, `/usr/bin/python3`). The temp-root probe and `tempfile` fallback semantics are CPython-version-sensitive; a different minor could change the probe's syscall shape (not the stdout).
- `git status` observed at three points only; the stronger path-level inventory is a `(size, mtime_ns)` snapshot, so a write whose size and mtime both alias an existing file between the two samples would be missed. `strace` covers that gap for the traced run, and the trace shows no `utimensat`/`truncate` at all.
- The 12-mutation set was established by `awk` over the trace, not by a semantic parser: a mutating syscall outside `%file,write,pwrite64` (e.g. `ftruncate`, `setxattr`) would not appear. `write`/`pwrite64` were traced explicitly and only touched fds 1 and 3.

Scratch (`/tmp/revenger-r69-hermetic/`) was created only for these probes and removed after the report was written; nothing outside this report file and that scratch path was written.
