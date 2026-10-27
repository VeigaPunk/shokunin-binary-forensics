# R71W1FreshSweep — embedded-output gate sweep over every knowledge entry

**Verdict: PASS-ADVISORY, no lane edits.** At an archived round-71 tip (`git archive HEAD` = `18200a4`), the registered gate is clean on the v6 candidate and all six apk-family entries (`round-71`: `checked_blocks=24 problems=0 exit=0`, ≥17-block conjunct satisfied) and the retained r65 M39 label reproduces exactly (`exit=1`, `drift entry:41`); but 3 **admitted** entries (`round-62-commonjs`, `round-63`, `round-64`) carry 76 declared `$` blocks that the gate never evaluates (`exit=2`), and a forged line inside those blocks passes unremarked (probe below) — a coverage hole in the pre-gate surface, not a C1/C2 predicate change.

Date 2026-10-27. Read-only over lane source: all runs executed against a `git archive HEAD` extraction in scratch. No new external source rows opened this round, so no access-date/quote rows are added by this seat.

## 1. Method (reproducible, read-only)

```
S=/fast/scratch/hyaku/revenger-r71/R71W1FreshSweep
git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive HEAD | tar -x -C $S/archive
cd $S/archive && for f in corpus/knowledge/*.md; do
  python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/$(basename $f); echo rc=$?; done
```

Archive provenance: `git log -1` → `18200a4 round-71: build v6 candidate and gate exit-2 cases`; `git diff --stat HEAD -- corpus/knowledge/` empty, so the archive equals the working-tree candidate bytes.

```
cf42cc20…c4d05a  corpus/knowledge/round-65-apk-axml-byte-evidence.md   # == measure.py R65_SHA
ef7f0232…830798e  corpus/knowledge/round-68-apk-axml-byte-evidence.md   # == measure.py R68_SHA
778af93b…92ea3bf  corpus/knowledge/round-71-apk-axml-byte-evidence.md   # working tree identical
05afff8b…f938f8   corpus/check_embedded_outputs.py                     # working tree identical
```

Gate self-test at the same tip: `SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired, pin and confinement checks passed, missing-entry and timeout legs passed` (`SELFTEST_RC=0`). Missing-entry leg: `could-not-evaluate: entry not found: corpus/knowledge/round-71-missing-entry.md`, `MISSING_RC=2`, no traceback.

## 2. Per-entry sweep (all 18 knowledge entries)

`blocks` = the gate's own `parse_blocks` count (fenced `$ ` commands); `checked`/`problems` from the CLI receipt.

| entry | status | blocks | checked | problems | exit | note |
|---|---|---|---|---|---|---|
| 2026-10-12-rea-readiness-checklist.md | none | 0 | — | — | 2 | no `$ cmd` blocks |
| commonjs-destructured-require-edges.md | rejected | 0 | — | — | 2 | no blocks |
| digest-scope-versus-provenance.md | none | 0 | — | — | 2 | no blocks |
| evm-saved-interface-candidates.md | rejected | 0 | — | — | 2 | no blocks |
| pe-resource-directory-layout.md | none | 0 | — | — | 2 | no blocks |
| round-62-commonjs-require-name-evidence.md | **admitted** | 11 | 0 | — | **2** | refused: first block `sha256sum …` (non-`python3`) |
| round-62-evm-dispatch-byte-evidence.md | **admitted** | 0 | — | — | 2 | no blocks |
| round-63-zip-central-directory-evidence.md | **admitted** | 41 | 0 | — | **2** | refused: `git`/`printf`/`wc`/`tr` blocks + `readout.py` absent at lane root |
| round-64-firmware-region-byte-evidence.md | **admitted** | 24 | 0 | — | **2** | refused: first block runs `readout.py` (absent at lane root; lives at `.ufo/waves/round-64/firmware-readout.py`) |
| round-65-apk-axml-byte-evidence.md | rejected (retained) | 15 | 15 | **1** | **1** | **expected r65 M39 reproduced** (below) |
| round-67-apk-axml-byte-evidence.md | rejected | 16 | 16 | 0 | 0 | clean |
| round-68-apk-axml-byte-evidence.md | rejected | 17 | 17 | 0 | 0 | clean, incl. digest pin `bce497d6…` (== measure.py S046_SHA) |
| round-69-apk-axml-byte-evidence.md | rejected | 17 | 17 | 0 | 0 | clean |
| round-70-apk-axml-byte-evidence.md | rejected | 24 | 24 | 0 | 0 | clean |
| **round-71-apk-axml-byte-evidence.md** | **candidate** | **24** | **24** | **0** | **0** | C1_GATE conjunct green at this tip |
| seed.md | none | 0 | — | — | 2 | no blocks |
| tool-validation-by-function-and-version.md | none | 0 | — | — | 2 | no blocks |
| utf16-unpaired-surrogates-in-resource-names.md | none | 0 | — | — | 2 | no blocks |

Totals: 9 entries with blocks; 113 blocks verified clean, 1 verified drift (r65), 76 blocks never evaluated. 9 entries declare no blocks (honest n/a, but see risk 3).

### 2.1 Retained r65 M39 — reproduced exactly as expected

```
$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-65-apk-axml-byte-evidence.md
drift entry:41 embedded output line not in recheck stdout: {"cd_index": 2, …, "fact": "member[META-INF/MANIFEST.MF]", … "payload_first16_hex": "4d616e696673742d56657273696f6e", …}
checked_blocks=15 problems=1
rc=1
```

The gate prints `4d616e69666573742d…`-class output; entry:41 records `4d616e696673742d…` (`Manifst-` vs `Manifest-`), matching the r65 `admission-status: rejected` marker verbatim (Q02 FAIL). Retained, not re-opened.

### 2.2 C1 gate conjunct, independently reproduced

`round-71` receipt `checked_blocks=24 problems=0` with `rc=0` ≥ 17 blocks — the `HOLDS_C1_V6` gate conjunct holds at `18200a4` in a scratch extraction (independent of the counter's own run). r65's `exit=1` is a *rejected* entry and does not enter `C1_GATE` (counter restricts it to the v6 path, `measure.py:84`).

## 3. Two located gate defects (advisory; frozen predicates untouched)

### 3.1 Exit 2 masks drift in mixed-command entries — proven with a forgery probe

`corpus/check_embedded_outputs.py:185` returns `None, None` as soon as **any** block's command is unsupported, discarding problems already accumulated from the supported blocks; `:302` then prints the single conflation line. Probe on a scratch copy of the archived r63 entry with line 24 (first output line of the first `python3` block) replaced by `{"forged": "line that the command never prints"}`:

```
$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-63-zip-central-directory-evidence.md
could-not-evaluate: no `$ cmd` blocks or unsupported command
R63_FORGE_RC=2
```

Minimal reproduction (two blocks: drifting `python3` block, then `sha256sum`):

```
$ python3 -B check_embedded_outputs.py --entry entry.md
could-not-evaluate: no `$ cmd` blocks or unsupported command
MASK_PROBE_RC=2
```

Consequence: the 76 blocks of the three **admitted** retained entries are outside the gate's reach and can drift/forge silently. Repair options (L1's call, no predicate change): (a) re-scope those blocks to `python3 -B corpus/…` snapshot scripts with declared pins, as r65+ already do; or (b) have `evaluate` report supported-block problems alongside the refused-block classification.

### 3.2 Uncaught `shlex` error violates the exit contract — latent, currently masked by block order

`corpus/check_embedded_outputs.py:175` (`pargv = shlex.split(cmd)`) raises `ValueError: No closing quotation` for an unbalanced-quote `$` line; it is not wrapped, so the CLI exits **1 with a traceback** — indistinguishable from "drift found" and contrary to the documented 0/1/2 contract (`:17-18`). Probe (`reader.py` + clean block, then `$ printf '%s`):

```
Traceback (most recent call last):
  File "…/check_embedded_outputs.py", line 297, in main
  File "…/check_embedded_outputs.py", line 175, in evaluate
    pargv = shlex.split(cmd)
ValueError: No closing quotation
QUOTE_PROBE_RC=1
```

Reachable in principle today: `round-62` block 3 (`$ printf '%s`, line 95) and `round-64` (`python3 -c 'import json` block, line 147) both hold unbalanced quotes, but are only shielded because an earlier block already returns `None, None` (r62: `sha256sum` first; r64: `readout.py` missing at lane root). Any future entry with supported blocks first hits the crash path. Minimal fix at :175 is a `try/except ValueError` → `CannotEvaluate`.

## 4. Risks / blockers

1. **Coverage (medium, pre-existing):** 3 of 4 admitted entries with declared commands have 0 gate coverage; the gate's admitted-entry coverage is `r62-evm` (no blocks) plus none of r62-commonjs/r63/r64. Not a round-71 regression and not covered by the frozen C1/C2 predicates — record as a round-72 candidate, do not widen wave 2.
2. **Observability (low):** `:302` merges "no blocks" and "unsupported command"; receipts cannot distinguish `seed.md` (nothing declared) from r63 (declared but unevaluable).
3. **No C2 exposure:** the timeout leg was not exercised by this seat (production 120 s exceeds the time box); the hermetic 1 s leg passed inside `--self-test`. C2 wave-2 legs remain L1's.
4. No lane writes, no commits/jj, no scratch outside `/fast/scratch/hyaku/revenger-r71/R71W1FreshSweep/`; that scratch tree (archive copy, receipts, 2 probes) was deleted before returning. Receipts are transcribed verbatim above.

Report: `.ufo/waves/round-71/w1/R71W1FreshSweep.md`
