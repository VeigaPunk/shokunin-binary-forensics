**HERMETIC** — `python3 -B corpus/check_embedded_outputs.py --self-test` ran three times with exit `0`/`0`/`0` and byte-identical stdout (sha256 `bcd32f26…`), is invariant to hash seed, locale, cwd, PATH and TMPDIR, and all 12 of its mutating syscalls land inside `TMPDIR` with 0 network calls, 0 lane-tree writes and 0 residue.

# R68C7Hermetic — is the repaired C7 gate hermetic and deterministic?

Verdict: **HERMETIC**. `corpus/check_embedded_outputs.py --self-test` is byte-for-byte deterministic across repeats, hash seeds, locales, cwd, PATH and TMPDIR, and its entire write footprint (12 mutating syscalls, syscall-traced) lands inside `TMPDIR`, with zero network syscalls, zero repo-tree writes and zero residue. Two scoped nits (docstring wording, cwd-relative `--entry`) and one consumer-side tree artifact in §5; none breaks the claim.

Seat: L1Revenger68.R68C7Hermetic · lane `/home/vgpnk/Projects/shokunin/revenger-shokunin` · tip `4232235` (gate blob `b89183be…`, sha256 of file `b89183bec2fd3b94f5b0acc828a0d3fe16f6a98dde1d7752616da85d08a8e0ca`) · date 2026-10-25.
No tool installed or upgraded. No file edited except this report.

## 1. Three consecutive self-tests (determinism)

`cd /home/vgpnk/Projects/shokunin/revenger-shokunin` then, for i in 1..3,
`TMPDIR=/tmp/r68c7-hermetic-probe/tmp python3 -B corpus/check_embedded_outputs.py --self-test`

| run | exit | stdout len | stdout sha256 | stderr | TMPDIR after run |
|---|---|---|---|---|---|
| 1 | 0 | 81 | `bcd32f26ad4ec7e9683b3512d305a57fc69d3419b98f72d126d1bc5925cccf1d` | (empty) | `[]` |
| 2 | 0 | 81 | `bcd32f26ad4ec7e9683b3512d305a57fc69d3419b98f72d126d1bc5925cccf1d` | (empty) | `[]` |
| 3 | 0 | 81 | `bcd32f26ad4ec7e9683b3512d305a57fc69d3419b98f72d126d1bc5925cccf1d` | (empty) | `[]` |

stdout, all three runs, verbatim:

```
SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired
```

`ALL_STDOUT_BYTE_IDENTICAL: True`. Exit codes 0/0/0 — matching the frozen `C7_SELFTEST=pass` predicate in `reports/round-68/claims.md`.

Determinism holds under ambient perturbation (same gate file, 8 environments):

| env | exit | stdout sha256[0:16] |
|---|---|---|
| baseline | 0 | `bcd32f26ad4ec7e9` |
| `PYTHONHASHSEED=0` / `=12345` | 0 | `bcd32f26ad4ec7e9` (both) |
| `LC_ALL=C LANG=C` | 0 | `bcd32f26ad4ec7e9` |
| cwd `/` (not the lane root) | 0 | `bcd32f26ad4ec7e9` |
| `PATH=/tmp/r68c7-empty-path` | 0 | `bcd32f26ad4ec7e9` |
| cwd `/tmp/r68c7-decoy` holding a hostile `reader.py` | 0 | `bcd32f26ad4ec7e9` |
| `TMPDIR=""` (unset) | 0 | `bcd32f26ad4ec7e9` |

`ENV_STDOUT_IDENTICAL: True | exits: [0]`. Structural reasons, from the source: `_self_test` writes its fixtures into `tempfile.TemporaryDirectory` (`corpus/check_embedded_outputs.py:155`) and evaluates every fixture with `cwd=tmp` (`evaluate(<entry>, tmp)` at `:132`, `:135`, `:146`; `_self_test` at `:110`), `run_cmd` rewrites `argv[0]` to `sys.executable` so PATH and the `python3` spelling are irrelevant (`:72-80`, allowlist `:76`, rewrite `:78`), and the pass line is a constant with no path/timestamp/random in it (`:149`). The decoy and empty-PATH cells are the adversarial versions of those two claims and both are inert.

## 2. Write footprint — nothing outside its own temp dirs

Fresh probe dir `/tmp/r68c7-hermetic-probe/tmp`; marker file written, 1.05 s sleep for mtime separation, then the three runs:

```
LANE_FILES_NEWER_THAN_MARKER: 0
```

`find /home/vgpnk/Projects/shokunin/revenger-shokunin -newer <marker> -not -path '*/.git/*'` → empty. After the runs the probe TMPDIR contained nothing (`tmp_leftover: []`, all three runs): the gate creates its own `rev-r67-c7-selftest-*` directory and removes it.

Syscall-level, `strace -f` over `open/openat/openat2/creat/truncate/utimensat/mkdir/mkdirat/rmdir/unlink/unlinkat/rename*/symlink*/link*/chmod/fchmodat/chown*/mknod*/connect/sendto/bind/memfd_create`, `TMPDIR=/tmp/r68c7-sweep`:

```
SWEEP exit 0 | stdout SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired
WRITE_OPS 12
  openat  /tmp/r68c7-sweep/imrwvenf                                  O_RDWR|O_CREAT|O_EXCL|O_NOFOLLOW|O_CLOEXEC, 0600
  unlink  /tmp/r68c7-sweep/imrwvenf
  mkdir   /tmp/r68c7-sweep/rev-r67-c7-selftest-w4scossy              0700
  openat  .../rev-r67-c7-selftest-w4scossy/reader.py                 O_WRONLY|O_CREAT|O_TRUNC
  openat  .../rev-r67-c7-selftest-w4scossy/clean.md                  O_WRONLY|O_CREAT|O_TRUNC
  openat  .../rev-r67-c7-selftest-w4scossy/drifted.md                O_WRONLY|O_CREAT|O_TRUNC
  openat  .../rev-r67-c7-selftest-w4scossy/full.md                   O_WRONLY|O_CREAT|O_TRUNC
  unlinkat 3 "reader.py"/"clean.md"/"drifted.md"/"full.md"            (dirfd-relative)
  rmdir   /tmp/r68c7-sweep/rev-r67-c7-selftest-w4scossy
OUTSIDE_TMPDIR []
NETWORK 0
TMPDIR_REMAINDER: ['t.log']        # only my own strace output file
```

Every target is under `TMPDIR`. The four `unlinkat(3, …)` calls are dirfd-relative (`/tmp/r68c7-strace/trace.log:374-377`) and remove exactly the four fixture files the gate had just written into its own `rev-r67-c7-selftest-*` directory; the directory itself is then `rmdir`-ed in the same parent process. `connect`/`sendto`/`bind`/`socket`/`memfd_create`: **0 occurrences** in either trace.

Read side: of 145 distinct paths opened read-only, the lane tree contributes exactly two — `corpus/check_embedded_outputs.py` itself and the `corpus` directory entry (`READS_IN_LANE`). The self-test therefore cannot be influenced by lane content, only by its own code.

## 3. Repo tree unchanged — before/after `git status --porcelain`

BEFORE any run (tip `4232235`):

```
?? .ufo/waves/round-68/build-wave-spec.py
?? .ufo/waves/round-68/wave-spec.json
```

AFTER the runs (measured 2026-10-25T03:29:10-03:00):

```
?? .ufo/waves/round-68/R68CounterReplay.md
?? .ufo/waves/round-68/R68FixtureHold.md
?? .ufo/waves/round-68/R68SnapshotFidelity.md
?? .ufo/waves/round-68/build-wave-spec.py
?? .ufo/waves/round-68/wave-spec.json
```

The three added paths are **sibling seat reports**, not gate output: mtimes `03:28:15`, `03:28:20`, `03:28:29` -0300 (after the three §1 runs, whose fingerprint window is empty), all under `.ufo/waves/round-68/`. Attribution is settled by a fingerprint diff taken strictly around one gate run — `(path, st_mtime_ns, st_size)` for every file in the lane excluding `.git`/`.jj`, snapshotted immediately before and after a single `--self-test` invocation:

```
{"exit": 0, "stdout": "SELFTEST OK: ...", "added": [], "removed": [], "changed": []}
```

`git diff --stat -- corpus/check_embedded_outputs.py corpus/derive_axml_anchors.py` → empty (working tree == HEAD for both). `find corpus -name '__pycache__' -o -name '*.pyc'` → nothing **at the time of the runs**; at `03:29:00.558` a different seat's in-process `import check_embedded_outputs` (without `-B`) created `corpus/__pycache__/check_embedded_outputs.cpython-314.pyc` (9356 B, untracked, not gitignored) — consumer-side, not gate output; attribution in §5.3. `git status --porcelain --ignored` adds only pre-existing `!! .jj/` and `!! .ufo/interactive-sessions/`.

## 4. Real-use path also deterministic (corroborating)

`python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-68-apk-axml-byte-evidence.md`, two fresh TMPDIRs:

```
run1 exit=0   run2 exit=0
089f663dcf6a8b5dded1fb8b94331390fa8c0f2a7317cfdddff142bd7648a16f  /tmp/r68c7-entry-1.out
089f663dcf6a8b5dded1fb8b94331390fa8c0f2a7317cfdddff142bd7648a16f  /tmp/r68c7-entry-2.out
--- entry stdout: checked_blocks=17 problems=0
```

Byte-identical; `checked_blocks=17 problems=0` matches the `C7_V3_CLEAN` expectation (17 blocks, 0 problems) in `reports/round-68/claims.md`. No file left in either TMPDIR.

Failure path is deterministic too (applied to **copies** in `/tmp/r68c7-mut/`, stop condition `reports/round-68/claims.md` §C1 "Frozen mutant", never to the repo file): the single-comparison substitution matches exactly once (`mutant occurrences replaced: 1`) and

```
MUTANT x3: [[1, "b815145160093708", "drifted entry output accepted"],
            [1, "b815145160093708", "drifted entry output accepted"],
            [1, "b815145160093708", "drifted entry output accepted"]]
MUTANT_DETERMINISTIC: True
```

`MUTANT exit 1 | last line: 'drifted entry output accepted'` and `last_endswith_marker: True`. Spoof control (`MARKER = "... (spoofed)"`): `exit 1`, last line `'drifted entry output accepted (spoofed)'`, `last_endswith_marker: False`. So the repaired marker at `corpus/check_embedded_outputs.py:142-145` is reachable and is the **last** output line of a failed run, and the attribution rule is not satisfied by a spoofed marker. (That conjunct belongs to `R68MutC7Kill`/`R68ReviewC7Gate`; recorded here only as hermeticity/determinism evidence, not as my verdict on the claim.)

## 5. Observations (none falsify HERMETIC)

1. **Docstring precision, LOW.** `corpus/check_embedded_outputs.py:26-27` says "it writes nothing outside its own temp dirs". Strictly, one transient file is created at `TMPDIR/<8 random chars>` — outside the `rev-r67-c7-selftest-*` directory — then unlinked at once (`/tmp/r68c7-strace/trace.log:144-145`). It is CPython's own `tempfile` directory-validation probe, not gate logic: reproduced with `TMPDIR=/tmp/r68c7-tftest python3 -B -c "import tempfile; print(tempfile.gettempdir())"` → `openat(..., "/tmp/r68c7-tftest/n_re2xhp", O_RDWR|O_CREAT|O_EXCL|O_NOFOLLOW|O_CLOEXEC, 0600)` then `unlink`, remainder `['t.log']`. Still inside `TMPDIR`, zero residue, name never printed, so determinism and hermeticity are unaffected; the wording ("temp dirs" → "TMPDIR") is the only thing that is imprecise.
2. **`--entry` verdict is cwd-relative, LOW/by design.** The docstring states "cwd = lane root" (`:13-15`) and `evaluate(args[1], Path.cwd())` (`:159`) runs the entry's commands in the caller's cwd. Verified fail-closed: `--entry` from `/` and from `/tmp` both exit `1` with `drift entry:24 command exited 2: python3 -B corpus/fixtures/apk-r65/readout.py --fact archive` (deterministic across the two). A mis-positioned invocation therefore cannot produce a false PASS — it degrades to exit 1, never 0. `--self-test` has no such dependency (decoy-cwd cell in §1).
3. **Consumer-import side effect in the tracked tree, INFO — not the gate's write.** `corpus/__pycache__/check_embedded_outputs.cpython-314.pyc` (9356 B) appeared at `03:29:00.558` -0300 while this wave ran. Provenance is settled three ways: (a) the pyc header stores source mtime/size `23:22:16` / `6791` B, matching `corpus/check_embedded_outputs.py` exactly; (b) the mechanism reproduces in an isolated copy — `python3 -B check_embedded_outputs.py --self-test` → no `__pycache__`, and the same **without** `-B` → still no `__pycache__` (a main script is never cached), while `python3 -B -c "import check_embedded_outputs"` → none and `python3 -c "import check_embedded_outputs"` → creates exactly that filename; (c) every invocation in this report executed the file as `__main__` with `-B`. So the pyc comes from a seat that **imported** the gate in-process without `-B`, not from any gate run. `git check-ignore corpus/__pycache__` exits `1` (`.gitignore` holds only `.ufo/interactive-sessions/`), so it is untracked-but-visible: invisible to the counter (which measures `git archive` of committed trees) and harmless to this verdict, but a `git add -A` would commit a compiled artifact into the measured corpus. Hygiene for the final commit: delete it, and import under `-B`/`PYTHONDONTWRITEBYTECODE=1` or ignore `__pycache__/`.

## 6. Residual risk / verification gaps

- The syscall sweep covers one invocation on this Python (`3.14.8`) and this stdlib; a different interpreter build could add its own probe files inside `TMPDIR`. The property tested — "no write outside TMPDIR, no network, no repo mutation" — is what is claimed, and it survived both strace and the fingerprint diff.
- The 3-file `git status` delta is sibling output; I attribute it by mtime order plus the empty fingerprint diff, not by kernel-level per-process attribution of those writes. The `corpus/__pycache__/*.pyc` attribution (§5.3) rests on pyc-header provenance plus a reproduction of the import mechanism, not on a trace of the other seat's process.
- `PYTHONPATH`-shadowing of stdlib modules was not exercised (the entry's own `reader.py`/fixture commands import stdlib only and run with `-B`); a poisoned `PYTHONPATH` would affect any Python gate equally and is outside the registered claim.
- Not checked here (other seats' surfaces, deliberately): whether the counter computes `C7_MUTANT_KILLED_ATTRIBUTED=1/1` from these bytes, the registry-row wording, and the C05 admission decision.

## 7. Evidence index

| artifact | pointer |
|---|---|
| gate source | `corpus/check_embedded_outputs.py` (sha256 `b89183be…`, `:36` MARKER, `:110-149` self-test + marker branch) |
| 3-run probe logs | `/tmp/r68c7-hermetic-probe/{run1,run2,run3}.out` (all sha256 `bcd32f26…`), `.err` files 0 bytes |
| strace sweep | `/tmp/r68c7-sweep/t.log` (382 lines; pids 1788313 + children 1788318/1788319/1788322) |
| first trace (probe file + dirfd) | `/tmp/r68c7-strace/trace.log` (377 lines; `:144-145` probe, `:374-377` unlinkat) |
| mutant/spoof copies | `/tmp/r68c7-mut/{mut.py,spoof.py}` |
| entry-mode runs | `/tmp/r68c7-entry-{1,2}.out`, sha256 `089f663d…` |
| stdlib probe reproduction | `/tmp/r68c7-tftest/t.log` |
