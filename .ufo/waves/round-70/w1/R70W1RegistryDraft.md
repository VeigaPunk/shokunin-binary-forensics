DRAFT-READY — exact registry text for two gates + one pre-flight is drafted below at current line numbers, but the copy already landed in the working tree (`SKILL.md` `M`, mtime 18:08:34) carries five defects that must be repaired before wave 2 reads it: a stale gate count (`:31-32`), a two-kind verdict map that the pin rule makes three (`:279`), an unmeasured `problems 7 → 0` after-value stated as fact (`:286`), an exit-2 precondition naming a file the checker never requires (`:292-293`), and a lint blind-spot list that omits three of its four silent skips (`:306`).

Seat: `R70W1RegistryDraft` · lane `/home/vgpnk/Projects/shokunin/revenger-shokunin` · target commit `aa1842fac199aa524930e5565ed3715de5f84c6d` (lane tip `aa1842f`) · no lane file edited by this seat · no tool installed (pacman paused host-wide; nothing needed).

## Axes (godspeed)

1. **Operability** — can a reader run each instrument from the row alone and predict its exit? (Rows below are written against the bytes, not the docstrings.)
2. **Calibration** — does every number in a row resolve to a command that printed it? (One violation found: F3.)

## State and provenance (why the draft is "amend", not "insert")

The registry rows for `self_assessment_check` and `lint_entry` and the `pin rule (round 70)` row already exist in the **working tree** at `SKILL.md:286-308`; they are **not** in the candidate commit:

```
$ git -C …/revenger-shokunin show aa1842f:SKILL.md | grep -n "self_assessment_check\|lint_entry\|pin rule"
(no output)
$ git status --porcelain
 M SHONEN.md
 M SKILL.md
 M corpus/README.md
 M corpus/self_assessment_check.py
$ ls -l --time-style=+%H:%M:%S SKILL.md
-rw-r--r-- 1 vgpnk vgpnk 54975 18:08:34 SKILL.md
```

So a sibling wrote rows into a file this seat may not edit; this report therefore supplies **corrected, copy-pasteable text at working-tree line numbers** plus the defects that motivated each correction. All line numbers below are the working-tree numbering as of that mtime (the candidate-commit registry was `272-285`, one table only).

## Draft text (verbatim)

### D1 — REPLACE `SKILL.md:279` (verdict map; third finding kind)

```
| verdict map | `0` clean (≥1 block checked, every embedded output line verbatim) · `1` failed (three finding kinds: `drift entry:N …` — an embedded output line the entry's own command does not print; `drift entry:N command exited RC: <cmd>`; `drift entry:N pinned historical script digest mismatch: <pinned path>` — a pin whose digest does not match, a finding and never a fallback to the current script) · `2` could-not-evaluate (no `$ cmd` blocks / unsupported command) · `64` usage (no arguments or an unrecognised form; PROTOCOL §Gate standard requires it declared) |
```

### D2 — APPEND to the end of `SKILL.md:280` (self-test; keep every existing byte of the round-68 rewrite)

```
 **Round 70 (C3) added a fifth leg:** the self-test also asserts that a digest-verified pin replaces the script argument (`corpus/check_embedded_outputs.py:186-189`) and that a one-byte tamper of the pinned copy is killed *and attributed* — `apply_pin` returns `pinned historical script digest mismatch: <use>` (`:107-108`), and the failure branch prints `pinned historical script digest mismatch not raised` **as the last line** then exits 1 (`:191-195`). Final line on success: `SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired, pinned script verified by digest` (`:196`). Measured at `aa1842f`: exit 0.
```

### D3 — REPLACE `SKILL.md:286` (pin rule; drop the unmeasured after-value, state the full finding form)

```
| pin rule (round 70) | an entry named as a top-level key in `corpus/embedded_output_pins.json` re-derives each pinned script argument against a digest-pinned earlier revision (`corpus/derive_axml_anchors_r68.py`, sha256 `bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249`, the S046 row's digest at `corpus/SOURCES.md:60`), verified by sha256 before use; a missing or mismatching copy is a finding, never a fallback (`corpus/check_embedded_outputs.py:99-109`; finding form `drift entry:N pinned historical script digest mismatch: <pinned path>`, exit 1 via `:129-132`). The pin is keyed on the script argument exactly as the command writes it and applies only to the entry whose file name is the key (`:86-95`); an absent pin file means no pin (`:92-94`). The registered comparison line (`problems += drift(lines, stdout_set, lineno)`) stays byte-identical (claims.md §C3 kill rule). Credited for: the round-68 retained candidate's embedded block re-deriving against the pinned script — before value `EMB_R68=checked_blocks=17 problems=7 exit=1` (`reports/round-70/measure-before.log:21`); the after value is read only at the round's final tip and no `reports/round-70/measure-after.log` exists at `aa1842f`. NOT credited for any entry not named in the pin file, and a pin does not make an old script current |
```

### D4 — REPLACE `SKILL.md:292` (self_assessment entry command / tree requirement)

```
| entry command | `python3 -B corpus/self_assessment_check.py --root <tree> [--lane <repo>]`; `<tree>` is a `git archive <commit> corpus SHONEN.md SCORECARD.md SKILL.md` extraction or the lane root, and must hold the four files `required()` tests — `corpus/README.md`, `corpus/QUALITY.md`, `SHONEN.md`, `SCORECARD.md` (`corpus/self_assessment_check.py:153-155`); `SKILL.md` is read by SM3 but its absence is not exit 2 |
```

### D5 — REPLACE `SKILL.md:293` (self_assessment verdict map)

```
| verdict map | `0` `SELF_MISMATCH=0` (SM1..SM6 each printed) · `1` `SELF_MISMATCH>0` (one `SMn=<n>` line per class, then the total) · `2` could-not-evaluate (one of the four `required()` files missing, `corpus/self_assessment_check.py:236-238`) · `64` usage |
```

### D6 — REPLACE `SKILL.md:295` (self_assessment: what a green run does NOT establish)

```
| what a green run does NOT establish | that the self-assessment is true beyond the six named classes. SM1 reads only the `QUALITY.md` index range against the highest `| Qnn |` row; SM2 accepts the literal glob `verify_*.py` as naming any `verify_` file (`corpus/self_assessment_check.py:64-73`); SM3 counts only `N bytes` preceded by a non-word, non-hyphen char (`:98`) and a `sha256 `hex…`` prefix in a SHONEN box for a file that box names in backticks — a stale digest quoted in prose outside a box is invisible; SM4 recognises only `revenger-rNN.Name` / `RNNName`; SM5 sees only a hex token introduced by `pre-registration`, `base`, `tip` or `commit` from `## Round 61` on, and an `erratum:` line excuses it; SM6 compares one integer on one SCORECARD line. A tree without `SKILL.md` is scored, not refused (D4) |
```

### D7 — REPLACE `SKILL.md:306` (lint: what it cannot see — the seat's core deliverable)

```
| what a clean run does NOT establish | nothing about Q01-Q13: a clean lint never substitutes a Q decision. Q14 skips any clause that is not exactly one hex run plus exactly one count (`corpus/lint_entry.py:70-73` — two runs or two counts in one `;`/`. `-split clause are silently skipped), ignores odd-length tokens and the digest lengths 40/64/128, ignores counts above 32, and reads prose only — a hex run inside a fenced block is never measured (`:41-49`). Q15 resolves only a token introduced by `commit`, `base`, `tip`, `since` or `at` on a prose line and skips a token followed by `…` (`:78-80`). QMAP checks that each QUALITY.md `| Qnn |` row appears with a non-empty decision cell — never that the decision or its basis is true. HEADER checks only the presence of the four keys in the first 40 lines (`:83-86`); it never checks a value, and `admission-status:` is not among the four. The criterion list is the lint's own `corpus/QUALITY.md` beside the script, not the `--lane` tree's (`:157`) |
```

### D8 — REPLACE `SKILL.md:307` (lint write scope / QUALITY.md provenance)

```
| write scope | read-only; reads the entry, its own `corpus/QUALITY.md` beside the script (not the `--lane` tree's), and runs `git cat-file -e` in `--lane` (default: `corpus/`'s parent) |
```

### D9 — REPLACE `SKILL.md:31-32` (scope: the registry's own count is stale)

```
- **Registry is the only admission instrument.** §Gate registry below registers two committed gates
  (`check_embedded_outputs` and `self_assessment_check`, kind `gate`) and one declared non-gate
  pre-flight (`lint_entry`, kind `pre-flight`); the ten `verify_*.py` scripts and every
  other self-test are replay evidence, not admission, and a green `--self-test` is not a verdict
```

### D10 — INSERT after `SKILL.md:460` (§3 Frozen counter: one line, only because the section exists today and is otherwise stale)

```
Round 70's registered counter is `reports/round-70/measure.py`, sha256
`488f95aa1d502cbb20b7303e1d773f0101397a0bd45cee69c9fb389651c88c76` (`reports/round-70/claims.md:7-8`,
recomputed: `sha256sum reports/round-70/measure.py`); the round-66 instrument below is preserved
history and none of its labels is this round's predicate.
```

Same family, one line each, if the L1 wants §6.1 non-stale: `SKILL.md:174` and `:177` hardcode `/tmp/revenger-r66-*` and the round-66 path as "as the contract requires" while `reports/round-70/claims.md` requires the round-70 counter; replace `reports/round-66/measure.py` → `reports/round-70/measure.py` and `revenger-r66-*` → `revenger-r70-*` in those two lines only (the quoted round-63 record at `:475-478` is history and stays).

### D11 — INSERT after `SKILL.md:540` (§4a census observations: OPTIONAL — the section is date-stamped and self-disclaiming, so it is incomplete rather than false)

```
Round-70 pre-wave `validate` → exit 0 with the same four disclosed W04s (S024/S028/S029/S034);
that receipt carries no `census` row counts (`.ufo/waves/round-70/census-before.txt`: four `W04`
lines, one `ok` line, `CENSUS_EXIT=0`). The after-run is read at the round's final tip.
```

### D12 — OPTIONAL INSERT after `SKILL.md:308` (the row the brief assumed already existed; it does not — F8)

```
| field | value |
|---|---|
| name | `q15_tree_id_check` |
| kind | checker (NOT a gate: round-69 C2 calibration checker; documented at `corpus/README.md:19`, not an admission instrument) |
| entry command | `python3 -B corpus/q15_tree_id_check.py --scan <file.md> [--lane <repo>]` (cwd = lane root; pass `--lane` from an archived tree) |
| verdict map | `0` every `tree-identity restatement:` pair resolves and ≥1 `tree-identity false-sentence:` pair fails · `1` otherwise · `64` usage |
| self-test | `python3 -B corpus/q15_tree_id_check.py --self-test` (fixed true/false fixtures; exit 0 iff both scored correctly) |
| write scope | read-only; runs `git rev-parse` |
| owner | revenger |
```

## Findings (advisory; each has a located defect + the command that shows it)

- **F1 — the registry's own self-description is stale.** `SKILL.md:31-32` says "registers exactly one committed gate"; after D1-D8 the registry carries two gates plus a pre-flight. Evidence: `git show aa1842f:SKILL.md | sed -n '31,32p'` and the landed rows at `:290`/`:301`. Repair: D9. This is an SM-class defect the new checker does **not** catch (SM1 range, SM2 README naming only).
- **F2 — verdict map undercounts finding kinds.** `SKILL.md:279` says "two finding kinds"; the pin path appends a third: `corpus/check_embedded_outputs.py:108` `PIN_MARKER = "pinned historical script digest mismatch"` and `:131` `problems.append(f"drift entry:{lineno} {pin_problem}")` → exit 1 at `:213`. Repair: D1.
- **F3 — unmeasured after-value asserted as fact (calibration).** Landed row `SKILL.md:286` states "(`EMB_R68` problems 7 → 0 …)". Only the before exists: `ls reports/round-70/` → `before-treated-tools-on-base.log build-controls.py claims.md controls measure-before.log measure.py` (no `measure-after.log`); `measure-before.log:21` `EMB_R68=checked_blocks=17 problems=7 exit=1`. A wave-1 row that reports the round's own outcome before the round measures it is the M34/M48 class. Repair: D3.
- **F4 — exit-2 precondition names a file the checker never requires.** `SKILL.md:292` lists `SKILL.md` in the tree; `corpus/self_assessment_check.py:153-155` `required()` tests only `corpus/README.md`, `corpus/QUALITY.md`, `SHONEN.md`, `SCORECARD.md`, and `:237` prints exactly those four. Consequence: a tree missing `SKILL.md` is **scored** (SM3 then counts the quoted `SKILL.md` digests as mismatches) rather than refused — a wrong verdict, not a crash. Repair: D4/D6.
- **F5 — the amended self-test row is silent on the new legs.** `SKILL.md:280` still describes only "clean+full-run exit 0 and that the drifted case is caught", while `corpus/check_embedded_outputs.py:186-196` now carries the pin-replacement leg, the tamper leg and the `PIN_MARKER` attribution branch, and `:196` enumerates five legs. Measured: `python3 -B corpus/check_embedded_outputs.py --self-test` → `SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired, pinned script verified by digest`, `rc=0`. Repair: D2.
- **F6 — the lint's blind-spot row omits three of its four silent skips.** `corpus/lint_entry.py:70-73` `if len(runs) != 1 or len(counts) != 1 or int(counts[0]) > 32: continue` (a clause with two hex runs is skipped entirely); `:41-49` `prose_lines` excludes fenced blocks, so a hex run inside a fence is never measured; `:83-86` `lint_header` checks key presence in the first 40 lines only — `admission-status:` is not one of the four keys, so a wrong admission status is invisible. The landed row `:306` names only the length/count exclusions. Repair: D7.
- **F7 — QUALITY.md provenance is ambiguous in the write-scope row.** `SKILL.md:307` "reads the entry, `corpus/QUALITY.md`" while `corpus/lint_entry.py:157` reads `(HERE / "QUALITY.md")` — the lint's own directory, never the `--lane` tree's. A reader auditing an archived TREE would believe the tree's criterion set is used. Repair: D8.
- **F8 — the brief's premise "existing rows for … `q15_tree_id_check.py`" is false.** `grep -n "q15_tree_id_check" SKILL.md` → no output (both at `aa1842f` and in the working tree). The checker is documented only at `corpus/README.md:19` and cited at `SCORECARD.md:566`. Either D12 registers it as a non-gate, or the registry should say in one line that checkers live in `corpus/README.md`. Silence is the current third option and is the weakest.
- **F9 — §3 "the round's registered counting probe" points at round 66.** `SKILL.md:457-459` names `reports/round-66/measure.py` sha `a59914e9…` as the round's counter; the round's counter is `reports/round-70/measure.py` sha `488f95aa1d502cbb20b7303e1d773f0101397a0bd45cee69c9fb389651c88c76` (`reports/round-70/claims.md:7-8`; recomputed: `sha256sum reports/round-70/measure.py` → `488f95aa…  reports/round-70/measure.py`). Repair: D10.
- **F10 — the checker bytes moved mid-wave, contrary to the brief's stability list.** `git status --porcelain` → ` M corpus/self_assessment_check.py`; `git diff` is one line: `sm3` size regex `r"(\d[\d,]*) bytes"` → `r"(?<![\w-])(\d[\d,]*) bytes"` (hunk `@@ -98,7 +98,7 @@`). The docstring (`:1-40`) still describes SM3 without that guard, so the registry row D6 must describe the guard (it does) and the docstring is now the stale artifact. No row text in this report depends on the pre-diff behaviour.

## Verification log (every command run, with its output)

```
$ python3 -B corpus/self_assessment_check.py --self-test
SELFTEST OK: clean 0; six planted defects each scored exactly their class; erratum excuses only a resolving correction
rc=0
$ python3 -B corpus/lint_entry.py --self-test
SELFTEST OK: clean 0; four planted defects each scored exactly their class; truncated-run-with-count flagged
rc=0
$ python3 -B corpus/check_embedded_outputs.py --self-test
SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired, pinned script verified by digest
rc=0
$ sha256sum reports/round-70/measure.py
488f95aa1d502cbb20b7303e1d773f0101397a0bd45cee69c9fb389651c88c76  reports/round-70/measure.py
$ sha256sum corpus/derive_axml_anchors_r68.py | cut -c1-16
bce497d6c0f5767f      # == embedded_output_pins.json "sha256" prefix and the S046 row (corpus/SOURCES.md:60)
$ grep -n "EMB_R6" reports/round-70/measure-before.log
19:EMB_R65=checked_blocks=15 problems=1 exit=1
20:EMB_R67=checked_blocks=16 problems=0 exit=0
21:EMB_R68=checked_blocks=17 problems=7 exit=1
22:EMB_R69=checked_blocks=17 problems=0 exit=0
```

All three self-tests were run from the lane root with `TMPDIR=/tmp/revenger-r70-RegistryDraft-tmp` (hermetic; the scripts write only their own temp dirs). Scratch deleted: `rm -rf /tmp/revenger-r70-RegistryDraft-tmp`; `ls -d /tmp/revenger-r70-RegistryDraft*` → no match.

## Out of scope / dependencies

- **Not measured, deliberately:** whether the counter's `EMB_PIN_MUTANT_KILLED_ATTRIBUTED=1/1` holds end-to-end (that is the counter's after-run, wave 2 / final tip), and whether the pin rule leaves `EMB_R65 problems=1` visible (same). D3 states only the before value for exactly that reason.
- **Dependency recorded:** `SKILL.md` is being written by a sibling while this seat reads it (mtime 18:08:34, rows appearing between two of my reads). Line numbers in D1-D12 are valid for that mtime only; if a sibling inserts above `:272`, shift by the inserted count (the anchors — the `family note` row, the `## 7. Cited sources` heading, the `read from the run, not from this page.` sentence — are stable text, so insert relative to them).
- **Assimilation / frontier step:** nothing in this seat's slice bears on `merge/revenger/` or the `## Mistakes` line; no README flip is proposed here, and D9 does not touch a coverage row.
- **Tool installs:** none. No package was queried or installed; every command above used an existing `python3`/`git`/`sha256sum`.
