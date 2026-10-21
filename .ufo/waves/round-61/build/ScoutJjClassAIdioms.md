# ScoutJjClassAIdioms — class-A HEAD idioms in the lane at e0a4b0c

READ-ONLY seat: nothing written except this report; no git/jj mutation, no clone, no install.
State observed: `git rev-parse HEAD` = `e0a4b0c4348ef1fade46539f520e94fa140c4d8a` =
`git rev-parse refs/heads/main`; `git rev-parse --abbrev-ref HEAD` prints `HEAD`;
`git symbolic-ref -q HEAD` prints nothing, exit 1; jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5.

## 1. Do the audit's two class-A idioms still exist? YES — both, verbatim

- `reports/round-1/scribe.md:42` (whole line): `   closure is a conformance defect (`git merge-base --is-ancestor <hash> HEAD`).`
- `LOG.md:318` (whole line): `- BEFORE: no PE-resource verifier and no `inspect_pe_resources` route at `f27b5f1a92af4f05081e7992925e30d621fff1c0`. `git cat-file -e HEAD:.shokunin/revenger/corpus/verify_pe_resources.py` fails. Prior routes are EVM `inspect_evm_interface`, ZIP inventory/extraction, ELF saved-proof, and JS graph/shape. The r26 pause line stays; this dispatch is a new operator round, not a rewrite of that line.`
- `grep -rnF -e 'merge-base --is-ancestor' -e 'cat-file -e HEAD' --include='*.md' --include='*.json' --include='*.py' .` → exactly those two hits, no third (re-run after this report landed adds only this file's own quotes). `grep -rn 'HEAD' reports/round-61/ | wc -l` → `0`.

## 2. Why it is live, not historical

- Both idioms give the *right* answer today only because HEAD == main: `git merge-base --is-ancestor 7c3ce197341b0babe0046b1d9cbb59f1ba43f54e HEAD` → exit 0, and with `refs/heads/main` → exit 0. Re-running them cannot expose the defect.
- The divergence object already exists. `jj --ignore-working-copy log -r '@'` → `b19244899607626b2fae5c142f3102b26118dee8 bookmarks= empty=true`; `-r '@-'` → `e0a4b0c4348e… bookmarks=main`. `git cat-file -t b19244899607` → `commit`; `git merge-base --is-ancestor b19244899607 refs/heads/main` → exit 1. The next `jj commit` makes git HEAD name that empty, unbookmarked commit — the audit observed precisely this (`JjAuditRevenger.md:164-170`, incl. `$ git cat-file -e HEAD:corpus/unbookmarked-probe.txt -> yes` / `main:… -> no`).
- Direction of harm: with HEAD ahead of main, `scribe.md:42` **false-accepts** an unbookmarked commit's ancestry and `LOG.md:318` **false-reports presence** of paths not on the branch; with main ahead, both **false-reject** landed work. [INFERENCE for in-lane trajectory, from the two observed facts above]
- `LOG.md:318` is also stale in a second way: `.shokunin/revenger/corpus/verify_pe_resources.py` is absent at *both* revisions (`git cat-file -e` → `fatal: path … does not exist`, exit 128 at HEAD and at `refs/heads/main`), while `git cat-file -e refs/heads/main:corpus/verify_pe_resources.py` → exit 0. Its "fails" is a historical-layout artifact; reused today as a BEFORE probe it reports a false absence of a verifier that is on the branch.

## 3. jj-safe replacement, with controls showing the fix can fail

Closure / ancestry (`scribe.md:42`), git form — 40-hex `<h>`:
`git cat-file -e "$h^{commit}" && git merge-base --is-ancestor "$h" refs/heads/main`
- true ancestor `7c3ce197…`: cat-file exit 0, is-ancestor exit 0.
- not on branch `b19244899607…`: cat-file exit 0 (object exists), is-ancestor exit **1**.
- missing object `f27b5f1a…`: cat-file `fatal: Not a valid object name`, exit **128** (distinct from 1).

jj form — exit status is useless, the test must be non-empty output:
`test -n "$(jj --ignore-working-copy log -r "$h & ::main" --no-graph -T 'commit_id ++ "\n"')"`
- true ancestor: output length 40, predicate exit 0. Not on branch: length 0, predicate exit **1**.
- bare `jj … log -r '<not-on-main> & ::main'` exits **0** on an empty set (observed), so an exit-status wrapper is vacuous; `-T 'commit_id'` without `++ "\n"` also gives `wc -l` = 0 for a true ancestor (observed) — use `test -n`.
- missing hash: jj prints `Error: Revision … doesn't exist`, exit 1 — same code as "not on branch", hence the `git cat-file -e` guard first when the two must be distinguished.

Path presence (`LOG.md:318`):
`git cat-file -e refs/heads/main:<path>` (0 present / 128 absent) or
`jj --ignore-working-copy file show -r main <path> >/dev/null` (0 present / 1 absent — both observed with `corpus/verify_pe_resources.py` and a non-existent path).

**Falsified published fix.** `JjAuditRevenger.md:87` recommends `jj --ignore-working-copy log -r '::<hash> & heads(bookmarks(main))'`. Positive control fails: for the true ancestor 7c3ce197… the intersection is empty (length 0); it is non-empty only for the main tip itself (e0a4b0c… → length 40). The operands are reversed — it asks "is the branch head an ancestor of `<hash>`". Correct form: `<hash> & ::main`.

## 4. Mistake row draft (for `corpus/lessons/round-1.md`; NOT written — L1/scribe owns the file)

| id | class | evidence | captured-by | fix |
|---|---|---|---|---|
| M21 | class A — a committed conformance/presence command defaults its revision to `HEAD`, which under jj colocation is `@-`/an unbookmarked commit, so the check can both false-accept unlanded work and false-report paths absent | `reports/round-1/scribe.md:42`; `LOG.md:318`; mechanism observed `JjAuditRevenger.md:164-170` | none — process rule (revision addressing), like M03/M16; nearest is Q03 ("a pin fixed outside the record under test") but no knowledge entry is involved, so claiming Q03 would overstate | pin the branch and prove the pin fails: `git cat-file -e "$h^{commit}" && git merge-base --is-ancestor "$h" refs/heads/main` (0 / 1 / 128 as above); jj: `test -n "$(jj --ignore-working-copy log -r "$h & ::main" --no-graph -T 'commit_id ++ "\n"')"`; path: `git cat-file -e refs/heads/main:<path>` |

Row id M21 follows the M01–M20 count in `corpus/lessons/round-1.md`; placing it there is an edit this read-only seat did not make.

## 5. Remaining unknowns

- No in-lane mutation was run, so the false-accept/ false-reject cases rest on the existing unbookmarked commit object plus the audit's sandbox observation, not a fresh in-lane reproduction. [INFERENCE]
- `file show -r main` presumes one `main` bookmark target; a conflicted bookmark was not exercised (jj would error rather than choose).
- Adjacent, not class A: `.ufo/waves/kaika-r1/planner.md:3,116` use `git rev-parse HEAD` to record observed state; under jj that records `@-`, so a cited "worktree HEAD" is not branch tip (class D).

VERDICT: Both class-A idioms persist verbatim at `reports/round-1/scribe.md:42` and `LOG.md:318`; they pass today only because HEAD == main == e0a4b0c, the next `jj commit` names the existing unbookmarked commit b192448 (not on main), the audit's own jj-form fix is falsified by its positive control, and the correct replacements are `git cat-file -e "$h^{commit}" && git merge-base --is-ancestor "$h" refs/heads/main` / `test -n "$(jj --ignore-working-copy log -r "$h & ::main" --no-graph -T 'commit_id ++ "\n"')"` — controls: true 0, off-branch 1, missing 128.
Installs: none.
