PRESENT — C7 gate is real and line-exact (catches never-printed, hand-drifted, trailing-space and truncated lines) but 2 of the 3 crafted forgeries are FALSE-CLEAN (exit 0): a pure reordering of real output lines and a duplicated-line substitution both pass; only the line that stdout never printed is caught. Recorded limitation, C7 contract untouched.

# R67MutC7Surface — adversarial entries against `corpus/check_embedded_outputs.py --entry`

seat: R67MutC7Surface (mutation-tester, leaf) · date: 2026-10-24 · contract read:
`reports/round-67/claims.md` (C2 §frozen predicate, §Bounds, §Void conditions)
gate under attack: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/check_embedded_outputs.py`
sha256 `19007bebeb4d60dafd826df108584933ebb3f2b1e6ab112925ea6c6cab3e697d` (169 lines)

## 1. What the gate actually checks (source reading, not inference)

`corpus/check_embedded_outputs.py:100-101`:

```python
        stdout_set = set(stdout.splitlines())
        problems += drift(lines, stdout_set, lineno)
```

`drift()` at `:79-81` is `[f"drift entry:{n} …" for l, n in lines if l not in stdout_set]`.

So the admitted predicate is **`set(embedded_lines) ⊆ set(stdout_lines)`** — a one-directional
per-line membership test over a `set`. By construction it is blind to (i) order, (ii) multiplicity,
(iii) omission. It still catches every line the command never prints, which is the M39 class and is
what the docstring (`:3-5`, `:15-19`) literally promises. The limitation is therefore a boundary of
the word "verbatim", not a code defect — I am **not** asking for a contract change.

## 2. Crafted entries and the detector run

Temp tree (my only write surface outside this report):

```
/tmp/revenger-r67-atk/reader.py            # c22a37a8…  facts a=1, b=2, c=3; no --fact prints a,b,c in order
/tmp/revenger-r67-atk/lane-root/           # cwd for --entry (lane-root-like: reader.py resolves relative)
/tmp/revenger-r67-atk/entries/{a..h}.md
/tmp/revenger-r67-atk/lane-root-real/      # copy of corpus/fixtures/apk-r65 + corpus/knowledge (real-surface probes)
```

Detector invocation, verbatim, for every case (cwd = the temp lane root):

```sh
cd /tmp/revenger-r67-atk/lane-root
python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/check_embedded_outputs.py --entry <entry.md>
```

Reader stdout (ground truth): `{"fact": "a", "v": 1}` / `{"fact": "b", "v": 2}` / `{"fact": "c", "v": 3}`;
`--fact a` prints only line a.

### (a) right lines in the WRONG ORDER — FALSE-CLEAN

entry sha256 `3ea6f606a0332ace44c525f101ab6048d05dda621d9e44e02ceba826d7447f64`

```
$ python3 -B reader.py
{"fact": "c", "v": 3}
{"fact": "b", "v": 2}
{"fact": "a", "v": 1}
```

actual: `checked_blocks=1 problems=0`, **exit 0**. Expected for a true "reproduces its own command"
gate: exit 1. Verdict: **false-clean**.

### (b) correct line DUPLICATED, one line replaced by another stdout line of the same command — FALSE-CLEAN

entry sha256 `148af07efb6e92e89de28153ad42dd4c1d19cac945599fea32dc2ff923bbeb41`

```
$ python3 -B reader.py
{"fact": "a", "v": 1}
{"fact": "b", "v": 2}
{"fact": "b", "v": 2}
```

(stdout is a,b,c: line c was replaced by a second copy of b.) actual: `checked_blocks=1 problems=0`,
**exit 0**. Verdict: **false-clean**.

### (c) EXTRA line absent from stdout but valid JSON from a DIFFERENT fact — CAUGHT

entry sha256 `c6cf1491ba3f19eee77b489a8db5952877c58e04434c8f6f52d807aace1981b2`

```
$ python3 -B reader.py --fact a
{"fact": "a", "v": 1}
{"fact": "b", "v": 2}
```

actual **exit 1**:

```
drift entry:4 embedded output line not in recheck stdout: {"fact": "b", "v": 2}
checked_blocks=1 problems=1
```

Verdict: **caught**, correctly attributed to the offending entry line. The gate is not dead.

### Controls (detector liveness, all caught)

| control | entry sha256 | actual |
|---|---|---|
| (d) hand-drifted value `{"fact":"a","v":9}` | `49deb546…f0452` | exit 1, `drift entry:3 … {"fact": "a", "v": 9}` |
| (e) correct line + one trailing space | `549d3473…66807` | exit 1, `drift entry:3 … {"fact": "a", "v": 1} ` |
| (h) truncated line `{"fact": "a"` | `521993a8…59e399` | exit 1, `drift entry:3 … {"fact": "a"` |

### Supplementary boundary probes (same `set` construction)

| probe | entry sha256 | exit | reading |
|---|---|---|---|
| (f) omission: only 1 of 3 stdout lines embedded | `aff4905e…e7307` | **0** | false-clean — subset check is one-directional |
| (g) pure duplication: a,a,b vs stdout a,b,c | `1bd46378…0838a` | **0** | false-clean — `set` has no multiplicity |

## 3. Same forgeries on the REAL admission surface (copy of the v2 entry)

Source left untouched; bytes copied into `/tmp/revenger-r67-atk/lane-root-real/` with
`corpus/fixtures/apk-r65/` copied alongside; cwd = that temp root.

- **Pristine control copy** `170df17d82452fef310749e43d7d11661a943e2185594ad1de8c8446d33d968a`
  (byte-identical to the committed v2 entry) → `checked_blocks=16 problems=0`, exit 0.
- **Mutant A — transpose the first two output lines of the entry's own full-run block**
  (header `round-67-apk-axml-byte-evidence.md:171`, output lines 172-186, 15 lines; first two
  swapped, nothing added or removed) → sha256 `b56efae9c090cf226393b21352fe42573289a0e2ad7c89b8be1cb3eea6f766dc`,
  actual **exit 0**, `checked_blocks=16 problems=0`. A real transposition of two facts in the
  richest block of the landed candidate passes the gate.
- **Mutant C — insert the `eocd` fact line into the `--fact archive` block** (same real bytes,
  different command) → sha256 `b8a581e4d9b3a657c5c94edf7739f7aaec64b1a2fb837971fd863d7242642245`,
  actual **exit 1**, `drift entry:25 … {"cd_end_equals_eocd_offset": true, … "fact": "eocd", …}`,
  `checked_blocks=16 problems=1`. Caught and attributed.

Exact reproduction of the false-clean (any reader can re-run it):

```sh
cp -r /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/apk-r65 /tmp/revenger-r67-atk/lane-root-real/corpus/fixtures/
cp /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-67-apk-axml-byte-evidence.md \
   /tmp/revenger-r67-atk/lane-root-real/corpus/knowledge/mutA_order.md
# swap lines 172 and 173 of that copy (the archive fact and the spec_derived_struct_widths fact)
cd /tmp/revenger-r67-atk/lane-root-real
python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/check_embedded_outputs.py \
        --entry corpus/knowledge/mutA_order.md
# actual: checked_blocks=16 problems=0   exit 0
```

## 4. Live anchors on committed bytes (detector as-shipped, lane root cwd, read-only)

| entry | sha256 | actual |
|---|---|---|
| `corpus/knowledge/round-67-apk-axml-byte-evidence.md` (v2 candidate) | `170df17d…d968a` | exit 0, `checked_blocks=16 problems=0` → `C7_V2_CLEAN=yes` behaviour confirmed independently |
| `corpus/knowledge/round-65-apk-axml-byte-evidence.md` (retained REJECTED) | `cf42cc20…4d05a` | exit 1, `drift entry:41 embedded output line not in recheck stdout: {"cd_index": 2, …, "payload_first16_hex": "4d616e696673742d56657273696f6e", …`, trailer `checked_blocks=15 problems=1` |
| `--self-test` | — | `SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired`, exit 0 |

The r65 red is exactly the committed M39 surface (`entry:41`, 15-byte `4d616e696673742d…`), matching
`reports/round-67/claims.md` §C2 red-before statement — no re-construction needed.

## 5. Named limitation (the finding, stated for the record)

**Recorded limitation: the C7 gate detects "a line the command never printed", not "this block
reproduces the command's output".** Concretely, all of the following pass with exit 0 —
order permutation (a), duplicate-substitution (b), dropped line (f), duplicated line (g), and a
transposition inside the landed v2 entry's 15-line full-run block (§3 mutant A). Anything that keeps
the embedded set a subset of stdout is accepted. This bounds the meaning of `C7_V2_CLEAN=yes`: it
certifies no fabricated/never-printed output line in the v2 entry, and nothing about line order,
multiplicity or completeness.

Cost of closing it, if a later round wants it (proposal only — not a change this round, and not a
change to the frozen predicate): compare `collections.Counter(stdout.splitlines())` against a
`Counter` of the block's output lines, or compare the two line lists directly. Either is a one-line
change at `:100-101` and would have turned (a), (b), (f), (g) into drift findings. Adopting it
belongs to a later round with a fresh pre-registration; round-67's frozen C7 predicate must not be
edited after this wave.

Cosmetic observation (not a defect claim, no verdict attached): `:99-102` `continue`s past a block
whose command exits non-zero without incrementing `checked`, so the trailer counts only blocks that
ran clean — a reader may read `checked_blocks=16 problems=1` on a 17-block entry as "16 checked".
`problems=1` keeps the receipt honest.

## 6. Restoration / non-mutation evidence

- Lane source was never edited. Gate sha256 before the first probe and after every probe:
  `19007bebeb4d60dafd826df108584933ebb3f2b1e6ab112925ea6c6cab3e697d` — identical.
- Frozen fixture tree `corpus/fixtures/apk-r65/` (4 files) hashed before and after all runs:
  `434e062f96f34abbcdd9c69e4887bc36379132bc7af237777950298cdbddf44f` — identical (void condition
  "changed corpus/fixtures bytes" not triggered).
- `round-67-apk-axml-byte-evidence.md` `170df17d…d968a` and `round-65-apk-axml-byte-evidence.md`
  `cf42cc20…4d05a`: unchanged after every run (re-hashed post-run).
- Every mutation lived in `/tmp/revenger-r67-atk/` (scratch declared disposable by the brief); no
  write to `corpus/`, `reports/`, `README`, `SOURCES`, `SKILL.md`, jj/git state, or any sibling path.
  Outside this report the only file I created is `/tmp/revenger-r67-atk/**`.
- Tool installs/upgrades: none (no package manager transaction run).

## 7. Calibration summary

Expected vs actual, per the assignment's three cases: (a) set-membership predicted to accept a
reorder — **false-clean observed**; (b) predicted to accept duplicate-substitution — **false-clean
observed**; (c) predicted to be the case membership must reject — **caught**. Detector is not
vacuous (three positive controls fire). The gate survives as a real M39-class probe; its surface is
narrower than "verbatim reproduction", and that narrowing is now documented with a two-command
reproduction on the actual candidate bytes rather than on a toy entry.
