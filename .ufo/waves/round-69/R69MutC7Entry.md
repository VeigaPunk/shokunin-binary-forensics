GATE-CATCHES-DRIFT — the registered embedded-output gate (`corpus/check_embedded_outputs.py`) kills a one-line byte-count drift in the v4 candidate's item-1 block (`947` → `948`): exit 1, `drift entry:27 …`, `problems=1`; the unmodified candidate is exit 0, `checked_blocks=17 problems=0`.

# R69MutC7Entry — C7 gate mutant on the C05 v4 candidate

- seat: L1Revenger69.R69MutC7Entry (mutation-tester, leaf)
- date: 2026-10-25
- target claim surface: C1 (coverage, C05 v4 re-gate) frozen predicate conjunct `C7_V4_CLEAN=yes` — "the candidate is clean under the registered gate — exit 0" (`reports/round-69/claims.md` §C1, frozen predicate)
- lane repo: `/home/vgpnk/Projects/shokunin/revenger-shokunin` (READ-ONLY for this seat; commits `35e1258` tip, build at `da02261`)
- scratch: `/tmp/revenger-r69-mutc7entry/` (deleted on return)

## Artifacts and hashes (before/after)

| artifact | pristine sha256 | mutated sha256 |
|---|---|---|
| `corpus/knowledge/round-69-apk-axml-byte-evidence.md` | `c1e7eaac9dba4c77e578c788755dec3e3499fd8795ad0e479c51b5be7deb11d5` | `f90fa0788fe9dbf8d184cae62fe27793a80470659845bb179fb22cb49d945bc9` |
| `corpus/check_embedded_outputs.py` (detector, unmodified) | `b89183bec2fd3b94f5b0acc828a0d3fe16f6a98dde1d7752616da85d08a8e0ca` | unchanged |

The pristine hash equals the lane file's hash (`sha256sum /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-69-apk-axml-byte-evidence.md` → `c1e7eaac…`), so the scratch copy was byte-faithful.

Scratch copy: `rm -rf /tmp/revenger-r69-mutc7entry && mkdir -p … && cp -a corpus /tmp/revenger-r69-mutc7entry/corpus` from the lane root (5.7M, 23 files / 11 dirs).

## The mutant

ONE embedded output line, item 1's archive fact block (`round-69-apk-axml-byte-evidence.md:26-27`):

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact archive
{"bytes": 947, ...}
```

`947` → `948` in the **second** line only (the embedded output at file line 27); the prose sentence at line 23 ("The archive is **947 bytes**") and item 11's independent re-embed at line 200 were left untouched, so exactly one gated line changed:

```
line27 before: {"bytes": 947, "fact": "archive", "path": "corpus/fixtures/apk-r65/fixture.apk", "sha256": "05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e"}
line27 after : {"bytes": 948, "fact": "archive", "path": "corpus/fixtures/apk-r65/fixture.apk", "sha256": "05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e"}
```

Defect class exercised: M39 — a transcribed command-output line the entry's own declared command does not print.

## Expected detector

`python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-69-apk-axml-byte-evidence.md` run with cwd = scratch tree root. Per the script's contract (`check_embedded_outputs.py:17-22,79-83,152-160`): it re-parses fenced `$ <cmd>` blocks, runs each exact argv (no shell), and requires each embedded line to appear verbatim in that command's stdout; exit 0 clean / 1 drift / 2 not evaluable. Expected: exit 1 with one `drift entry:<lineno> embedded output line not in recheck stdout: …` line and `problems=1`.

## Actual output — MUTATED copy

```
$ cd /tmp/revenger-r69-mutc7entry && python3 -B corpus/check_embedded_outputs.py \
    --entry corpus/knowledge/round-69-apk-axml-byte-evidence.md; echo "EXIT=$?"
drift entry:27 embedded output line not in recheck stdout: {"bytes": 948, "fact": "archive", "path": "corpus/fixtures/apk-r65/fixture.apk", "sha256": "05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e"}
checked_blocks=17 problems=1
EXIT=1
```

Named entry line: **`corpus/knowledge/round-69-apk-axml-byte-evidence.md:27`** (the gate's 1-based `entry:27` is the exact mutated line).

## Actual output — UNMODIFIED v4 candidate (baseline, same scratch tree)

```
$ sha256sum corpus/knowledge/round-69-apk-axml-byte-evidence.md
c1e7eaac9dba4c77e578c788755dec3e3499fd8795ad0e479c51b5be7deb11d5  corpus/knowledge/round-69-apk-axml-byte-evidence.md
$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-69-apk-axml-byte-evidence.md
checked_blocks=17 problems=0
EXIT=0
```

Matches the frozen predicate's `C7_V4_CLEAN=yes` requirement (exit 0). 17 blocks were re-executed, so the clean result is not vacuous (a zero-block entry would exit 2 per `:152-156`).

Self-test (detector's own forge control) also passes in the scratch tree:

```
$ python3 -B corpus/check_embedded_outputs.py --self-test
SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired
SELFTEST_EXIT=0
```

## Verdict

**GATE-CATCHES-DRIFT (mutant KILLED).** The gate is not a rubber stamp on this surface: one digit in one embedded output line flips exit 0 → 1, pins the mutated line (`entry:27`), and leaves the 17-block checked count intact (so the kill is a drift verdict, not a could-not-evaluate). This corroborates `C7_V4_CLEAN=yes` for the v4 candidate at `da02261`/`35e1258`.

## Restoration evidence

```
$ cp pristine-entry.bak corpus/knowledge/round-69-apk-axml-byte-evidence.md
$ sha256sum corpus/knowledge/round-69-apk-axml-byte-evidence.md
c1e7eaac9dba4c77e578c788755dec3e3499fd8795ad0e479c51b5be7deb11d5  corpus/knowledge/round-69-apk-axml-byte-evidence.md
$ cmp pristine-entry.bak corpus/knowledge/round-69-apk-axml-byte-evidence.md && echo CMP_IDENTICAL
CMP_IDENTICAL
$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-69-apk-axml-byte-evidence.md
checked_blocks=17 problems=0
EXIT=0
```

Post-restore hash equals both the pre-mutation hash and the lane file's hash; the restored bytes re-gate clean (exit 0). The lane tree was never written: `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin status --porcelain corpus/ .ufo/` shows only `?? .ufo/waves/round-69/assimilation/` (a sibling seat's untracked output), no `corpus/` entry.

## Coverage observations (findings, not contract changes)

1. **Gate scope is fenced-block output only.** `parse_blocks` collects lines solely between a `$ ` line and the next fence/`$ ` inside a fence (`check_embedded_outputs.py:44-63`). Thus item 1's prose claim "The archive is **947 bytes**" (`:23`) and item 11's narrative numbers outside fenced blocks are ungated — a prose-only drift of the same value would survive. The assigned mutant is inside a fenced block and was caught; the prose half of the M39 class is outside this gate's predicate.
2. **Membership, not position.** `drift()` compares against `set(stdout.splitlines())` (`:83-85`), so a duplicated stdout line makes a transposed or mis-ordered embed pass. Not exercised here (the archive fact is a single-line stdout), recorded as a calibration residual.
3. The gate re-runs each block's command in the entry's own declared argv form only when `argv[0]` is a python interpreter (`:76-79`); any non-python command makes the run exit 2 (not evaluable), which is honest but means a future entry that quotes shell-only output cannot be gated by this tool.

## Tooling

No package installs or upgrades were performed (host pacman transactions are paused; nothing needed beyond the existing `python3`).

Scratch `/tmp/revenger-r69-mutc7entry/` removed before return.
