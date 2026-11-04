# ScoutR91Surfaces — every lane surface the v3 + message-tree integration must touch

Read-only recon at lane worktree state: HEAD `d509e98` + untracked
`corpus/self_assessment_check3.py` (22395 B, built by `ExecR91Sm6V3`;
`reports/round-91/message_tree_check.py` absent at recon time). No lane file
was edited by this seat. Scratch tree used for the one measurement below lived
under `/fast/scratch/hyaku/revenger-r91/ScoutR91Surfaces` and was deleted.

## 1. Greps that produced the map (one per class)

```
# class A — the checker file names, live surfaces only (wave history excluded)
grep -rn "self_assessment_check2" --exclude-dir=.git --exclude-dir=.jj --exclude-dir=.ufo .
grep -rn "self_assessment_check3" --exclude-dir=.git --exclude-dir=.jj --exclude-dir=.ufo .
grep -rn "self_assessment_check\.py"  --exclude-dir=.git --exclude-dir=.jj --exclude-dir=.ufo .

# class B — the SM6 / SELF_MISMATCH vocabulary
grep -rni "sm6"          --exclude-dir=.git --exclude-dir=.jj --exclude-dir=.ufo .
grep -rn  "SELF_MISMATCH" --exclude-dir=.git --exclude-dir=.jj --exclude-dir=.ufo .

# class C — the gate registry and its counting command
grep -rn "Gate registry\|gate registry" --exclude-dir=.git --exclude-dir=.jj --exclude-dir=.ufo .
sed -n '/^## Gate registry/,/^## [^G]/p' SKILL.md | grep -cE '^\| name \|'      # -> 15 now

# class D — scripts that import or invoke a checker
grep -rn "self_assessment_check" --include=*.py --exclude-dir=.ufo .
grep -rln "SELF_MISMATCH\|\"SM1\"\|'SM1'" --include=*.py --exclude-dir=.ufo .
grep -rn "Gate registry" --include=*.sh --include=*.py --exclude-dir=.ufo .   # -> docstrings only

# class E — the C2 capability surface
grep -rn "capabilities\|## Capabilities" SCORECARD.md
grep -rn "message_tree" --exclude-dir=.git --exclude-dir=.jj --exclude-dir=.ufo .
```

## 1.5 Live state at recon close (worktree, HEAD `d509e98` + untracked)

```
M  corpus/README.md              # +1 line: the v3 index line (line 30) — the load-bearing edit, landed
?? corpus/self_assessment_check3.py         # 22395 B; sm6():210, self_test():298, main():407
?? reports/round-91/message_tree_check.py   # appeared during recon (was absent at 19:42)
?? reports/round-91/__pycache__/            # not mine (my runs used -B)
?? reports/round-91/holds.log
?? .ufo/waves/round-91/{assimilation/,w1/,w1-validate.err,w1.ready,w1.ready.dispatched}
```

Measured at that state: `python3 -B corpus/self_assessment_check3.py --root . --lane .`
→ `SM1=0 SM2=0 SM3=0 SM4=0 SM5=0 SM6=0 SELF_MISMATCH=0 exit=0`;
`--self-test` → exit 0, last line `SELFTEST OK: clean 0; six planted defects each
scored exactly their class; twenty-four tightened-class probes … scored as declared …`.
So the C1 blocker in §4.1 is closed in the worktree; the documentation sites
(§3: SKILL/SCORECARD/LOG) are still open.

## 2. The two row formats, quoted verbatim

### 2.1 `SCORECARD.md` §Capabilities row (header `SCORECARD.md:165`, separator `:166`)

```
| Capability | What it can now do | Evidence pointer | First-working round |
|---|---|---|---|
```

Last row, `SCORECARD.md:169` (the row a new capability is appended after):

```
| cited-evidence orphan sweep | Enumerate every lane-repo path cited by the closed round reports and lessons, classify each against HEAD and the working tree (committed / orphan / orphan-dir / absent-fleet / absent), and exit 1 naming any landable orphan (on-disk, never committed); hermetic `--selftest` (no git/network/live-tree write) with a planted-orphan vector and an attributed mutant kill | `PYTHONUTF8=1 python -B reports/round-80/orphan_sweep.py --lane <lane> --fleet <fleet-root>` → `CITED=344 COMMITTED=330 LANDABLE_ORPHANS=0 ABSENT=14`, exit 0 (`reports/round-80/sweep-real-after.log`) | round-80 |
```

Admission rule immediately after the table, `SCORECARD.md:171`:

```
Rows enter only through a round that demonstrates the capability running (`AXES.md` §Capabilities).
```

### 2.2 `SKILL.md` §Gate-registry row (block form; `self_assessment_check2` block, `:314-324`)

```
| field | value |
|---|---|
| name | `self_assessment_check2` (round 90 C1; supersedes `self_assessment_check` above for SM6 only — v1 bytes stay as the r70 instrument) |
| kind | gate (committed, re-runnable verdict script this lane owns) |
| entry command | `python3 -B corpus/self_assessment_check2.py --root <tree> --lane <repo>` (same tree shape as v1) |
| verdict map | `0` `SELF_MISMATCH=0` · `1` at least one of SM1-SM6 non-zero · `2` could-not-evaluate (a required file is missing) · `64` usage |
| self-test | `python3 -B corpus/self_assessment_check2.py --self-test` — v1's legs plus six SM6 denominator legs (…) |
| measured-against | frozen battery `reports/round-90/sm6_battery.py` (14 hand-labelled cases …) |
| what a green run does NOT establish | v1's limits stand for SM1–SM5; SM6 reads only the LAST line naming `K_HELD_BACKED` … |
| write scope | read-only over TREE; runs `git cat-file -e` in the lane repo; writes nothing outside its own temp dirs |
| owner | revenger |
```

(Field order used by every block in the section: `name`, `kind`, `entry
command`, `verdict map`, `self-test`, optional `measured-against` /
`pinned-value path` / `declared scan contract`, `what a green run does NOT
establish`, `write scope`, `owner`. Blocks are separated by one blank line.
`measured-against` exists only where a frozen battery backs the row.)

## 3. Required edit sites — `path:line — what must change`

### corpus/README.md (4 sites; 1 is load-bearing, 1 is a forbidden change)

- `corpus/README.md:29` — after the v2 index line (`- \`self_assessment_check2.py\` — v2 of the above (round 90 C1): …`) append one index line naming `self_assessment_check3.py` (v3: SM6 reads the stated before→after cell of the last SCORECARD `K_HELD_BACKED` row; SM1–SM5 unchanged). **Status at recon close: already landed in the worktree by a sibling seat as line 30** (`git diff corpus/README.md` = 1 insertion; live `SM1=0 SM2=0 … SELF_MISMATCH=0 exit=0`). It remains listed because it is load-bearing and must survive any later README rewrite. **Load-bearing**: SM2 (`corpus/self_assessment_check3.py:86`, same rule as v2 `:73-88`) counts every top-level `corpus/*.py` and `corpus/*/` and requires the README to name it. Measured (scratch tree, v3 `--root <tree> --lane <lane>`): without the line `SM2=1 SELF_MISMATCH=1 exit=1`; with the line `SM2=0 SELF_MISMATCH=0 exit=0`; removing the line again restores `SM2=1` (kill/restore control).
- `corpus/README.md:70-72` — "Known gaps" sentence `\`SKILL.md\` exists and carries a \`## Gate registry\` (rows for \`check_embedded_outputs\`, \`self_assessment_check\` and the pre-flight \`lint_entry\`)` must name the v3 row and the message-tree row (it already undercounts: the registry carries 15 `| name |` rows).
- `corpus/README.md:28` — the v1 index line stays byte-unchanged (v1 remains the r70 instrument).
- `corpus/README.md:63` — `Rows 15 — \`grep -cE '^\| C[0-9]+ ' corpus/README.md\` (2026-10-27, observed 15).` **MUST NOT change**: this is SM6's denominator `D`, and a new index line does not touch the `^\| C<n> ` population (re-derived: 15 map rows, 8 `held`).
- No index line is required for `reports/round-91/message_tree_check.py`: `grep -c source_path_check corpus/README.md` → 0, i.e. the r90 precedent keeps `reports/`-resident instruments out of the corpus index (and SM2 never scans `reports/`).

### SKILL.md (5 sites)

- `SKILL.md:325` — insert a new `| field | value |` block for `self_assessment_check3` between the v2 block (`:314-324`) and the `apk_identity_oracle2` block (`:326`): `name` must carry the supersession clause (`supersedes \`self_assessment_check2\` for SM6`), `entry command` `python3 -B corpus/self_assessment_check3.py --root <tree> --lane <repo>`, `verdict map` `0/1/2/64` as v2, `self-test` `--self-test`, `measured-against` the frozen battery `reports/round-91/sm6_battery_v3.py` + `reports/round-91/mutants.py` + `reports/round-91/c1_counter.py` with `SM6_MISCLASS=0/22`, `MUTANTS_KILLED=11/11`, and `what a green run does NOT establish` (the stated-cell rule reads only the last `K_HELD_BACKED` row's cell index 2).
- `SKILL.md:325` (same insertion point, second block) — new block for `message_tree_check` — `reports/round-91/message_tree_check.py`: `kind` gate, `entry command` `python3 -B reports/round-91/message_tree_check.py --lane <repo> --range <A>..<B>`, `verdict map` `0` `MESSAGE_TREE … misses=0` · `1` misses > 0 · `2` usage/not-a-repo, `self-test` **`--selftest`** (no hyphen — that is the spelling `reports/round-91/cap_probe.py:95` invokes), `measured-against` `reports/round-91/cap_probe.py` (`CAP_MESSAGE_TREE=pass`), `what a green run does NOT establish` (a commit message that cites no path is not evidence of hygiene; a `bare` match is a suffix match, not a location).
- `SKILL.md:37-38` — `§Gate registry below registers exactly one committed gate (\`check_embedded_outputs\`, kind \`gate\`)` is already false (15 `| name |` rows) and becomes falser with two more rows. Correct the sentence (or state the live count) in the same commit; leaving it is a fresh self-assessment-adjacent drift the lane's own M36 class names.
- `SKILL.md:469` — the new blocks must land before `## 7. Cited sources` (`:470`): the section's own counting command is `sed -n '/^## Gate registry/,/^## [^G]/p' SKILL.md | grep -cE '^\| name \|'` (prints **15** now; **17** after the two rows). Placement after the `Registry note (round 78)` paragraph (`:460-468`) also counts but breaks the section's reading order; insert after `:324`/`:458`.
- `SKILL.md:529` — §7's inventory row for `corpus/check_embedded_outputs.py` is the only corpus-gate §7 row; v1 and v2 have none, so no §7 row is required for v3 (optional, not load-bearing).

### SCORECARD.md (3 sites)

- `SCORECARD.md:169` — append one capability row after it (before the blank `:170` and the rule at `:171`), shape exactly as §2.1: `| commit-message ↔ tree conformance | <what it can now do> | \`PYTHONUTF8=1 python3 -B reports/round-91/message_tree_check.py --lane <lane> --range 7fab03f..refs/heads/main\` → \`MESSAGE_TREE commits=N cited=M misses=K\` (\`reports/round-91/cap_probe.py\` → \`CAP_MESSAGE_TREE=pass\`, \`reports/round-91/<receipt>.log\`) | round-91 |`.
- `SCORECARD.md:1670` (file end) — append the round section: header `## Round 91 (hyaku) — …`, a `Base …/freeze …/landing …` paragraph in the shape of `:1649-1655`, then the table with header exactly `| axis / criterion | before → after | counting command | measured commits | verdict |` (`:1657`) and one row per claim in the shape of `:1659-1663`, then `**Routed forward.**` (`:1665`).
- `SCORECARD.md:693` — **hazard, not an edit**: this is the last line containing `K_HELD_BACKED` (re-derived: `grep -n K_HELD_BACKED SCORECARD.md | tail -1`). SM6 v3 reads cell index 2 of that line and today gets `8/15` → `SM6=0` (measured). If the new round-91 row also carries the token `K_HELD_BACKED`, its **cell index 2** (the `before → after` cell) must state `8/15`; a K token parked in the counting-command cell (the `:693` shape, cell 3) would be invisible to v3 and a wrong `N/D` in cell 2 flips `SM6=1`.
- Historical rows `:201 … :693` stay byte-unchanged (append-only discipline).

### LOG.md (1 site)

- `LOG.md:1289` (file end) — append `## Round 91 (hyaku) — <headline>` with the r90 entry's bullet shape (`LOG.md:1261-1289`): `- **Freeze \`<hash>\`.**` … `- **Wave (one v1, N seats).**` … `- **Landing \`<hash>\`.**` … `- **After (\`git archive <hash>\`).**` … `- **Mistakes mined:** …`.

### No edit required (checked, with the evidence)

- `SHONEN.md` — `grep -n "SM\|gate\|registry\|self_assessment\|checker" SHONEN.md` → no matches (30 lines). Do **not** add `N bytes`, `sha256 \`hex\`` or a `[x]` box: SM3 (`corpus/self_assessment_check3.py:118`) attributes every quoted byte count / digest to the nearest preceding backticked file token in the box, and SM4 requires a `Named non-author verifier:` clause for every `[x]` box.
- `corpus/QUALITY.md` — `grep -n "self_assessment\|SM[0-9]\|gate registry\|checker" corpus/QUALITY.md` → no matches (56 lines). Q17 (`:29`) names only `reports/round-90/source_path_check.py`; no admission criterion names the self-assessment gate, and `message_tree_check` is not an admission criterion.
- `considerthese/2026-11-04.md` — a mined source (claims.md §C2 "grounded in … proposal 4 (mined, not edited)"); never edited.

### Scripts that import or invoke a checker (contract sites, not edits)

- `reports/round-91/c1_counter.py:60` `impl_mod = load(impl, "r91_impl")`, `:70/:76` `impl_mod.sm6(root)`, `:105` `--self-test`, `:111` `--root <TREE> --lane <LANE>`, `:113` regex `SELF_MISMATCH=(\d+)` — **v3 must expose a module-level `sm6(root)` taking exactly one positional argument** (v3 does: `corpus/self_assessment_check3.py:210`), plus `--self-test` exit 0 and the `SELF_MISMATCH=` line on the full run.
- `reports/round-91/sm6_battery_v3.py:134/:142` — same `mod.sm6(root)` contract (frozen).
- `reports/round-91/mutants.py:37-45` — frozen, self-contained (does not import the impl).
- `reports/round-91/cap_probe.py:31` `INSTR = HERE / "reports/round-91/message_tree_check.py"`; `:95` `--selftest`; `:108-111` `--lane <d> --range <c0>..<c1>`; `:125` summary regex `MESSAGE_TREE commits=(\d+) cited=(\d+) misses=(\d+)`; exit 0 clean / 1 dirty / 2 usage.
- `reports/round-70/measure.py:101,107,178,180`, `reports/round-70/measure-a1.py:117,122,129,134`, `reports/round-71/measure.py:143,145` — invoke `corpus/self_assessment_check.py` (v1) **by path**. Frozen historical counters: never repoint them at v3.
- `reports/round-90/sm6_battery.py:8` — historical, takes `--impl`; unchanged.
- `corpus/self_assessment_check2.py` — bytes stay: pinned `0e73a90b2de99a1a8de40b59dfd75c48ce4a6bbb3243d4d93be78e31028d0227` in `reports/round-90/instrument-pins.log:1`, and `reports/round-91/c1-red-v2.log` is the red receipt over exactly those bytes.
- `corpus/self_assessment_check3.py` — the new file (present, untracked at recon: 22395 B, `sm6` at `:210`, `self_test` at `:298`, `main` at `:407`).

## 4. What breaks if v3 simply replaces v2

1. **SM2 / README naming (measured, hard blocker today).** v3 `--root . --lane .` prints `SM1=0 SM2=1 SM3=0 SM4=0 SM5=0 SM6=0 SELF_MISMATCH=1 exit=1` because `corpus/README.md` does not name `self_assessment_check3.py`. C1's fourth leg (`c1_counter.py:111-115`) requires `SELF_MISMATCH=0`, so **without the README line `C1_VERDICT=fail`**. With the line (scratch copy, kill/restore control): `SM2=0 SELF_MISMATCH=0 exit=0`.
2. **SCORECARD last-K-line rule.** SM6 v3 reads cell index 2 of the *last* line containing `K_HELD_BACKED`. Appending a round-91 row that mentions the token in any other cell, or with a wrong `N/D` in cell 2, flips `SM6` 0→1 and kills the same leg. Safe shapes: put `K_HELD_BACKED 8/15 → 8/15` in cell 2, or omit the token from the new row entirely (the r90 "held criteria (no claim)" row at `:1663` does the latter and is invisible to SM6).
3. **C2 leg 4 is razor-thin on the declared range.** In `7fab03f..refs/heads/main` (23 commits now; 21 at the freeze) **no commit message contains a backtick at all**. Token census over the range: repo-relative path tokens (`corpus/|reports/|.ufo/|considerthese/`) = 9 occurrences; `.log` filenames = 8; extension-terminated filename tokens (`.md|.py|.json|.log|.sh`) = 23 occurrences / 21 distinct. `cap_probe.py:126` requires `cited=M ≥ 20`. An instrument implementing only the literal "backticked repo-relative path + `.log` filename" reads **M=8 → leg 4 fails**. It must also extract **bare** path/filename tokens (the claim's own "bare filenames resolve by suffix match and are reported as `bare`" clause) to reach M=21–23 — a margin of 1–3 tokens. Note leg 4 ignores the instrument's exit code, so a nonzero `misses=K` is tolerated by the counter, but must be reported honestly.
4. **Flag spelling.** `cap_probe` calls `--selftest` (no hyphen); `c1_counter` calls `--self-test`. An instrument that only accepts one spelling fails the other counter.
5. **`sm6(root)` arity.** A v3 whose `sm6` takes `(root, lane)` fails `c1_counter.py:70` with a TypeError before any case runs.
6. **Registry count drift.** `SKILL.md:37-38` already claims "exactly one committed gate"; after two new rows the counting command prints 17. Any SCORECARD/LOG text that repeats a registry count (e.g. `SCORECARD.md:871` "3 → 5", `LOG.md:1244`) is historical and must not be rewritten.
7. **v2 bytes are pinned.** Editing or deleting `corpus/self_assessment_check2.py` breaks `reports/round-90/instrument-pins.log:1` and the r90 receipts; the supersession must be by a new file (as claims.md §C1 requires).

## 5. Edit-site count by file

| file | required edit sites | notes |
|---|---|---|
| `corpus/README.md` | 2 (index line `:29`→now line 30, **landed**; Known-gaps `:70-72`, **open**) | `:63` must not change |
| `SKILL.md` | 4 (v3 block; message-tree block at `:325`; stale count `:37-38`; placement before `:470`) | `:529` optional |
| `SCORECARD.md` | 2 (capability row after `:169`; round section after `:1670`) | `:693` is a hazard, not an edit |
| `LOG.md` | 1 (round entry after `:1289`) | |
| `SHONEN.md` | 0 | do not add digests/`[x]` (SM3/SM4) |
| `corpus/QUALITY.md` | 0 | no criterion names the gate |
| **total** | **9** | + 1 hazard site (`SCORECARD.md:693`) |
