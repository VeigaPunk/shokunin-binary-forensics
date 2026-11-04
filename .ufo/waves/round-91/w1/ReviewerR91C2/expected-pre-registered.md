# ReviewerR91C2 — C2 falsification set: pre-registered expectations

Written BEFORE the first instrument run. Fixture script: `build_fixture.sh`
(this dir); runner: `run_cases.sh`. Fixture repo built under
`/fast/scratch/hyaku/revenger-r91/ReviewerR91C2/fixture.Aoe3Bc` per protocol
(`mktemp -d` under `$HYAKU_SCRATCH/revenger-r91/ReviewerR91C2`, `git -C "$D"`
on every call, toplevel asserted equal to `$D` before the first commit).

## Grounded git semantics (probed before fixture build)

`git cat-file -e <c>:<path>`:
- `corpus` and `corpus/` (directory, with or without trailing slash) → exit 0 (tree object exists)
- `./corpus/self_check.py` (leading `./`) → exit 0 (git normalizes it)
- `corpus/self_check.py:12` → exit 128 (an anchor is not part of a path)
- missing file/dir → exit 128

## Expected semantics (from frozen claims.md §C2 spec)

The instrument extracts every **backticked** repo-relative path and every
`.log` filename cited in each message, and checks each against **that
commit's own tree** (`git cat-file -e`); bare filenames resolve by suffix
match, reported as `bare`; per commit `COMMIT <hash> cited=<n> misses=<k>
[missing=…]`; summary `MESSAGE_TREE commits=N cited=M misses=K`; exit 0 iff
K=0, 1 if K>0, 2 usage.

Where the spec is silent, the spec-consistent readings pre-registered here
(fixed before any run) are:
1. plain-prose path mentions (no backticks) are **not** citations;
2. a `path:line` anchor is stripped and the path checked;
3. a backticked directory is a citation and exists iff the tree has the dir;
4. a comma inside the backticks is punctuation, stripped;
5. tokens containing whitespace (commands like `git status`) are not paths;
6. a merge commit is processed like any commit (its own tree; not skipped,
   no crash).

## Fixture cases → expectations (frozen here)

Fixture tip hashes are in `cases.env`; every case range is a single commit
except AGG (11 commits). Tree states verified by `git cat-file -e` before
registration: case-d log ABSENT at C5_D / PRESENT at C6_E; old_name PRESENT
at C7 / ABSENT at C8 (new_name PRESENT); side.py PRESENT in both the side
commit and the merge tree; merge has two parents; Hside range = 1 commit.

| # | case | range | expected cited | expected misses | expected exit | why |
|---|------|-------|----------------|-----------------|---------------|-----|
| a | A: prose path `missing/case-a.txt`, no backticks, target missing | C1..C2_A | 0 | 0 | 0 | non-backticked prose is out of scope |
| b | B: `` `corpus/self_check.py:12` `` | C2_A..C3_B | 1 | 0 | 0 | strip `:12`; path exists |
| c | C: `` `corpus/` `` | C3_B..C4_C | 1 | 0 | 0 | dir is a tree object; cat-file -e accepts |
| d | D: bare `` `case-d-receipt.log` `` added only by the NEXT commit | C4_C..C5_D | 1 | 1 (bare) | 1 | checked vs commit's OWN tree; absent here |
| e | E: `` `./corpus/other.py` `` + `` `corpus/other.py,` `` | C5_D..C6_E | 2 | 0 | 0 | `./` git-native; comma = punctuation |
| f1| F1: adds+cites `` `corpus/old_name.py` `` | C6_E..C7_F1 | 1 | 0 | 0 | own tree has it (catches HEAD-tree bug) |
| f2| F2: renames it, cites old+new | C7_F1..C8_F2 | 2 | 1 | 1 | own tree lacks old name after rename |
| g | G: `` `git status` `` `` `git log -1` `` `` `--amend` `` `` `jj` `` | C8_F2..C9_G | 0 | 0 | 0 | commands/flags/bare words are not path citations (jj = advisory, weakest row) |
| h1| Hside: side commit cites `` `corpus/side.py` `` | C9_G..C_SIDE | 1 | 0 | 0 | own tree carries it |
| h2| Hmerge: `--no-ff` merge cites `` `corpus/side.py` `` | C_SIDE..C_MERGE | 1 | 0 | 0 | merge processed, not skipped; no crash |
| — | AGG: whole range | C0..C_MERGE | commits=11 | 2 (D + F2) | 1 | exactly two misses; 11 COMMIT lines |

A HEAD-tree-instead-of-own-tree bug is pinned from both sides: it false-flags
F1 (file gone at HEAD) and false-clears D (log present at HEAD).

## Hand count on 5 sampled real lane commits (7fab03f..refs/heads/main)

Hand-counted from `git log -1 --format=%B`; the whole range's messages
(10,369 bytes) contain **zero backtick characters** and exactly **8** `.log`
tokens (independently re-grepped), all 8 resolving in their own trees:

| commit | cited (hand) | misses (hand) | citations |
|--------|--------------|---------------|-----------|
| d509e98 | 0 | 0 | none (no backticks, no .log) |
| b13aac7 | 0 | 0 | none |
| 45b2713 | 4 | 0 | sweep-green.log, mutant-kill-after.log, sweep-probe-after.log, c1-only.log (all bare; suffix-resolve: round-88 ×2, round-83/84/85 (multi-hit), round-78/79/80 (multi-hit)) |
| 6ce41aa | 3 | 0 | environment.log, c1-after.log, c2-after.log (bare → reports/round-89/*) |
| 5f7ecce | 1 | 0 | reports/round-89/c1-after.log (full path) |

Expected real-range summary for a spec-faithful instrument (as of d509e98):
`MESSAGE_TREE commits=23 cited=8 misses=0`, exit 0.
**Note:** frozen probe leg 4 demands `cited ≥ 20` on this range; the
spec-faithful ceiling today is 8. Threshold reachability depends on future
landing commits adding `.log` citations — see report.

Scoring: C2_DISAGREE counts the 8 canonical cases (a–h; f = f1∧f2, h =
h1∧h2) + 5 real commits = 13; a case disagrees iff any of its rows deviates
from this table (count, miss set, exit code, or missing COMMIT line).
