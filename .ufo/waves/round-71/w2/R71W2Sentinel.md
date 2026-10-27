VERDICT — HOLD: two HIGH findings (a post-freeze rewrite of the committed evidence registry/lesson landed as commit `a16e6cb` while W2 was scoring, and a symlink hole that lets C1's 16/16 vote evidence live outside the measured commit); C05 itself is still correctly `candidate`/`uncovered` and no out-of-lane or fixture write occurred. No edits made by this seat.

Seat: `R71W2Sentinel` (scope/safety). Date 2026-10-27. Candidate `4c1eeae` (tree `b6f07f5`), freeze `c6e284c` (tree `cfae4cf`), current lane HEAD `a16e6cb` (committed 13:08:43 during this review), base `b7abcd8`. All commands run from the lane root unless stated; receipts below are the actual output lines.

## F1 [HIGH] Evidence registry + lesson rewritten after the freeze and committed as `a16e6cb` while W2 was scoring

Timeline observed directly in the lane (all times -0300, 2026-10-27):

1. `c6e284c 13:03:37` — wave-2 freeze commit; `w2.ready` dispatched 13:03:44; four reviewer seats and the critics start.
2. `13:05:39` `corpus/SOURCES.md` and `13:06:06` `corpus/lessons/round-71.md` are rewritten **in the worktree** (60512 B file stamped; both tracked). `git status --porcelain=v1` at 13:07 showed `M corpus/SOURCES.md`, `M corpus/lessons/round-71.md`.
3. `13:08:43` commit `a16e6cb "round-71: curate sources and record frontier mistakes"` lands exactly those two files (3 insertions / 3 deletions); `git diff --name-status c6e284c HEAD` = `M corpus/SOURCES.md`, `M corpus/lessons/round-71.md`, `git ls-tree -r HEAD | grep w2-votes` = nothing. HEAD-at-review `4c1eeae → c6e284c → a16e6cb`; frozen entry, counter and README are untouched.

`git diff c6e284c a16e6cb --word-diff=porcelain -- corpus/SOURCES.md` (exact, all three edits):

```
-corpus/knowledge/round-71-apk-axml-byte-evidence.md
+corpus/knowledge/round-71-apk-axml-byte-evidence.md, corpus/lessons/round-71.md      # S052 used-by
-format-layout
+format/layout                                                                        # S053 teaches
-—
+corpus/lessons/round-71.md                                                           # S053 used-by (rejected row)
```

`git show a16e6cb -- corpus/lessons/round-71.md` replaces the frozen sentence `New rows: S052 mined/90d/used-by v6; S053 rejected/on-release/used-by —.` with `New S052 … its used-by is — → …, corpus/lessons/round-71.md. New S053 is rejected/on-release; its used-by is — → corpus/lessons/round-71.md` and retargets the census pointer to `census-after.txt`. Blob identities: frozen `c6e284c` → `a426f9d6…` / `8ea8f355…`; current worktree = HEAD `a16e6cb` → `dc2e5b22…` / `38f06c03…`.

Evidence that this actually collided with scoring: W2 report `R71W2SpotcheckDraft.md` (13:06:00) states "My table and quotes describe the **committed HEAD** state (`c6e284c`), where S053 `used-by=—`" and cites `corpus/SOURCES.md:67 … used-by=—`. After `a16e6cb` that citation is false against the tip the votes will be bound to. The same report records the dirty delta verbatim and explicitly declines to apply it — i.e. the edit's authorship was already recognised as out of scope by a W2 seat (`R71W2SpotcheckDraft` also denies editing `SOURCES.md` in its own scope line). `R71W2LessonReview`'s task reads "Draft any missing section text but **do not edit**"; its transcript shows it diffing `corpus/lessons/ro…` in the working tree. Exact author is not provable from local evidence (a direct L1 edit is the other possibility), which is itself the defect: a seat-disallowed or unrecorded tracked-source rewrite became committed evidence during adjudication.

**Exploit path / impact.** Seats that re-derived Q01/Q02/source rows or reviewed the lesson before 13:08:43 scored one byte state, and seats after it score another; the commit is not the vote commit, so the eventual "final measured tip" will contain registry/lesson prose changes made after the frozen handoff, without a named located defect, without a pre-registration amendment, and with a commit message ("curate sources and record frontier mistakes") that does not describe the actual three-cell used-by/typo delta. No C1/C2 label moves because the counter never reads `SOURCES.md` or the lesson (`rows()` reads `corpus/README.md`), so the damage is adjudication provenance, not the frozen predicate arithmetic. `scripts/sources-census.sh validate … revenger` still exits 0 on the post-commit bytes (`revenger ok …/corpus/SOURCES.md`), and CORPUS rule 2 permits in-place `used-by` changes, so neither the validator nor the corpus rules will flag the timing.

**Smallest remediation (L1, before the vote commit).** Either (a) keep `a16e6cb` but record it explicitly in the round-71 receipts as a post-freeze registry/lesson correction with its located reason, and require every W2 report that cites `SOURCES.md`/lesson bytes to name `a16e6cb` as its base (the SpotcheckDraft table cites the superseded `c6e284c` bytes today); or (b) revert it with `git revert --no-edit a16e6cb` so the measured tip is byte-stable from the freeze. Either way, stage only `.ufo/waves/round-71/w2-votes/` and w2 reports for the vote commit and require `git status --porcelain -uno` empty plus `git diff c6e284c..HEAD -- corpus/` empty (or exactly the recorded curation) before archiving. No re-gate after the vote.

## F2 [HIGH, A2 provenance] `q_votes` follows symlinks — 16/16 without committed vote bytes

`reports/round-71/measure.py:65-84` tests only `root.is_dir()`, globs `*.json`, and `read_text()`s each path; there is no `is_symlink()`/regular-file check (A2 added `unique_object` and `isinstance(data,dict)` but not file identity). Probe in scratch (`import` of the committed counter, `m.q_votes(tree)`):

```
symlink_vote_count: 16        # R71W2Q01Q04.json -> /fast/…/outside/live-vote.json
is_symlink: True
dirlink_is_dir: True
dirlink_vote_count: 16        # w2-votes itself -> /fast/…/external/decoy
```

**Exploit path.** Commit (or let a seat create) `.ufo/waves/round-71/w2-votes` or one of its four `*.json` files as a symlink to a mutable path outside the repo. `git archive` recreates the link only (the target bytes are not in the commit), so the counter reads external, mutable content and can report `C1_W2_Q_VOTES=16/16` for a TREE whose committed bytes contain no vote decisions — the exact opposite of A2 §1 ("This makes the 16/16 evidence re-derivable from the measured commit") and of the claims' vote-file predicate. Re-derivation later at the same commit can also disagree if the target changes. Requires a link to be created/committed (visible in review), but the counter's own fail-closed checks cannot see it.

**Smallest remediation.** In `q_votes`, fail closed on non-regular files: `if root.is_symlink() or not root.is_dir(): return 0` and, per path, `if path.is_symlink() or not path.is_file(): return 0` (or `os.lstat` + `stat.S_ISREG`). Because predicates are frozen this must be treated as a pre-scoring measurement-hardening amendment, or recorded as a located defect on C1 — not a silent edit.

## F3 [MEDIUM] Unhashable `seat` aborts the counter instead of reporting 0/16

`EXPECTED_VOTES.get(seat)` runs before the stem/type checks and only `(OSError, ValueError, UnicodeError)` are caught. Probe:

```
unhashable_seat_raised: TypeError cannot use 'list' as a dict key (unhashable type: 'list')
dict_seat_raised: TypeError cannot use 'dict' as a dict key (unhashable type: 'dict')
extra_seat_file: 0
lowercase_pass: 0
valid_set: 16
```

A vote file `{"seat": [...], "decisions": {…}}` raises out of `q_votes`; the top-level handler prints a traceback plus `COUNTER_ERROR=uncaught exception (exit 2)` and emits **none** of the C1/C2 labels or the ten `HOLD` rows. That contradicts A2 §2's "returns 0/16 instead of raising and truncating the counter receipt" and the claims' "missing, malformed or failed votes keep `HOLDS_C1_V6=no`". Direction is fail-closed (never a false yes), so severity is medium. **Fix:** `if not isinstance(seat, str): return 0` before the dict lookup (or `EXPECTED_VOTES.get(seat) if isinstance(seat,str) else None`), and add `TypeError` to the except tuple.

## F4 [MEDIUM-LOW] Counter docstring vs actual reads: not hermetic to TREE

`measure.py:1-6` says "Reads only TREE and lane git objects". Actual live-lane reads: `lint_entry.py --entry <TREE path> --lane LANE` (line 96; `corpus/lint_entry.py:91-93` runs `git -C lane cat-file -e <h>^{commit}` — object store, defensible), `self_assessment_check.py --root TREE --lane LANE` (line 143, same object-store role), and `spec_from_file_location('r70measure', LANE/'reports/round-70/measure.py')` (line 143), which executes a **live worktree source file**. On a lane worktree that is not byte-identical to the measured commit — F1 shows HEAD moved mid-scoring and a seat edit sat uncommitted for ~3 minutes — `SELF_CLEAN_FIXTURE`/`SELF_MUTANTS_KILLED` (and any future lane-side edit to that file) change the receipt for the same measured commit. **Fix:** load that module from the measured commit (`git -C LANE show <tip>:reports/round-70/measure.py`) or pin its sha and fail closed; correct the docstring.

## F5 [LOW] Committed bytecode and untracked pycache

`reports/round-71/__pycache__/measure.cpython-314.pyc` is committed in the candidate (`A` in `git diff b7abcd8 HEAD`), 23171 B, magic matches, and `strings` shows embedded host paths (`/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-71/measure.py`, `/fast/scratch/hyakuz`). Untracked `corpus/__pycache__/check_embedded_outputs.cpython-314.pyc` and `reports/round-70/__pycache__/measure.cpython-314.pyc` exist. Reviewers read `.py`; the archive ships `.pyc`; `git add -A` would add more. **Fix:** delete the tracked pyc and the untracked pycache dirs before the vote commit; keep `-B`.

## F6 [LOW] PROVINCE pin change contradicted by its own W1 evidence report

Base `git show b7abcd8:PROVINCE.md` line 19 = `npx -y rea-agents@6.4.0`; HEAD = `6.5.0`; `grep -rn 6.4.0 PROVINCE.md SKILL.md corpus/README.md` now empty. But `.ufo/waves/round-71/w1/R71W1ProvincePin.md` concludes: "`PROVINCE.md:19` says: 'else `npx -y rea-agents@6.5.0`' … The current province pin is already 6.5.0 … So no PROVINCE correction is justified." The seat read the file after the edit, so its receipt cannot support the change, while `claims.md` cites it as "PROVINCE REA version-pin correction (6.4.0→6.5.0) and evidence". Doc-only; **fix:** keep the 6.5.0 value but rewrite that W1 receipt as a before/after observation (base 6.4.0 → tip 6.5.0, grounded on S049/S039/S043), or revert — do not cite the current report as support.

## Clean / verified (no finding)

- **Write scope.** 77 paths in `git diff --name-status b7abcd8 HEAD`, every one under the lane; modified files are exactly `PROVINCE.md`, `SKILL.md`, `corpus/README.md`, `corpus/SOURCES.md`, `corpus/check_embedded_outputs.py`; the rest are new `.ufo/`, `reports/round-71/`, `corpus/knowledge/round-71-…`, `corpus/lessons/round-71.md`. No fleet/sibling/route/config path appears in the diff.
- **Fixture preservation.** `git diff --stat b7abcd8 HEAD -- corpus/fixtures corpus/snapshots` → empty (no byte change to `apk-r65`, snapshots or pins).
- **Post-candidate commits.** `git diff --name-status 4c1eeae c6e284c` → only `.ufo/waves/round-71/w2-dispatch.json`, `w2-spec.json`, `w2/swarm-registry.json` (wave freeze; no source). Then `a16e6cb` (13:08:43, after the freeze and during W2) → only the F1 pair `corpus/SOURCES.md`, `corpus/lessons/round-71.md`; `git ls-tree -r a16e6cb --name-only | grep w2-votes` → nothing, so no vote file is committed at review time. `git status --porcelain=v1` now shows only untracked wave/report files and the two pycache dirs.
- **C05 still candidate.** README C05 row: "`knowledge/round-71-apk-axml-byte-evidence.md` (sixth-pass candidate; gate 24/24, Q16-aware lint 0/0/0/0; wave-2 votes pending, no coverage credit) … uncovered"; entry header `admission-status: candidate — … wave-2 Q01–Q16 decisions pending`; `SCORECARD.md`/`LOG.md` not modified by the round. Live re-run on the candidate: `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-71-apk-axml-byte-evidence.md` → `checked_blocks=24 problems=0`, exit 0; `lint_entry.py … --lane .` → `LINT_QMAP=0 LINT_Q14=0 LINT_Q15=0 LINT_HEADER=0`, exit 0.
- **Vote plumbing clean.** `.ufo/waves/round-71/w2-votes/` does not exist yet; `grep -rl '"decisions"' --include=*.json .` → no hits; dispatch names exactly `w2-votes/R71W2Q01Q04.json`, `R71W2Q05Q08.json`, `R71W2Q09Q12.json`, `R71W2Q13Q16.json`, and no other seat path; **all** dispatch report paths are `.ufo/waves/round-71/w2/*.md` and all scratch paths are `/fast/scratch/hyaku/revenger-r71/<seat>/`; no `/tmp`, `~/.local`, or `/etc` path in the dispatch.
- **Frozen bytes.** `sha256sum reports/round-71/claims.md` = `1febae1279fdeca323f5e8beffeb0a8ac2f26256158f7000bb0b2eff8321c3f5` (matches pre-registration); `measure.py` = `718daa96f34fa5c3435acdf031e2fe5099238e9092c36b845cb9258990fcca61`. At `a16e6cb` both are byte-identical (`git show a16e6cb:reports/round-71/measure.py | sha256sum` → `718daa96…`; claims → `1febae12…`), and the C05 entry blob is the same at `c6e284c` and `a16e6cb` (`671f55fc…`), so F1 does not touch the entry, counter or claims. Per-commit counter hashes: `63b560b`/`18200a4` = `d0d59b79…`, `da4f1ee` = `fbd81050…`, `4c1eeae` = `c6e284c` = `718daa96…`. `diff` build→A1 is exactly the one sleeper line (`$ python3 -B sleeper_r71.py` → `… corpus/sleeper_r71.py`); A1→A2 is exactly `unique_object` + `q_votes(tree)` + `isinstance(data,dict)` + docstring. No delta outside the two amendments.
- **Gate change containment.** `git diff … corpus/check_embedded_outputs.py` touches only the docstring, `CannotEvaluate`, `run_cmd(timeout=)`, `evaluate` pre-read/timeout raising, the self-test legs and `main`'s exit-2 print. `confined()`, `inside()`, `drift()`, the pin check and `problems += drift(...)` are byte-unchanged, so confinement/pin/verbatim behavior is unchanged.
- **Host/fleet.** Fleet root `git status --porcelain -uno` empty (only pre-existing untracked `.scratch/closure-mado-r50.json`, `kotoba-shokukin/`); `~/.omp/agent/*.json|md` mtimes 2026-10-19/25; `~/.local/bin` mtime 2026-10-27 05:26 (before the round); no tool installed. `kama-shokunin` and `kotoba-shokunin` worktrees show their own lanes' modifications; no revenger-71 artifact references writing them. No routing/model config touched.
- **Operational note for L1.** `git archive --format=tar HEAD .ufo/waves/round-71/w2-votes` currently exits **128** because the path is not in HEAD: archive only after the vote commit, and keep the vote directory in the path list, or `C1_W2_Q_VOTES` reads 0/16 regardless of the files.

Scratch `/fast/scratch/hyaku/revenger-r71/R71W2Sentinel/` (probe copies only) removed after the run; no lane source, fixture, counter, vote file or report outside `.ufo/waves/round-71/w2/R71W2Sentinel.md` was written.
