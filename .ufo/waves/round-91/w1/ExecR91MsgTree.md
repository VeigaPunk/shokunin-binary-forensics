# ExecR91MsgTree — C2 operability capability: commit-message ↔ tree conformance

Seat: ExecR91MsgTree (leaf, round 91, attempt 1). Claim: `reports/round-91/claims.md` §C2.
Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin` @ `d509e98` (range tip `refs/heads/main`), freeze `b13aac7`.

## Deliverable

`reports/round-91/message_tree_check.py` (new, 319 lines, read-only over the lane).
Frozen interface implemented: `--lane REPO --range A..B`, `--selftest`, `--json`; empty `A` (`..B`) means all history of `B`.

For each commit in `git rev-list A..B`: read `git log -1 --format=%B <c>`, extract every token that looks like a repo-relative path, and check each against that commit's own tree with `git -C REPO cat-file -e <c>:<path>`. Output per commit `COMMIT <h> cited=<n> misses=<k> [missing=<p>,…] [bare=<p>,…]`, then `MESSAGE_TREE commits=<N> cited=<M> misses=<K>`. Exit 0 iff K=0, 1 if K>0, 2 on usage.

Declared extraction rule (stated in the module docstring, sent to ReviewerR91C2 before her expectations were fixed):

- Tokens come from the whole message; backticks and surrounding punctuation are delimiters, so backticked and plain-prose citations are read alike (the lane writes commit messages without backticks — 0 backticks across all 713 commits on all refs — so a backtick-only reader would measure nothing on this history).
- Per token: strip trailing `.,;:!?*'"`, strip a `:NN`/`:NN-MM` line suffix, strip leading quotes, strip repeated leading `./`; a trailing `/` marks a directory citation (checked as a tree).
- Path-like: listed extension (`.py .md .json .log .txt .sh .mjs .yml .yaml .toml .cfg .ini`), or explicit directory (`corpus/`), or a slash token with a dotted segment (`corpus/v1.2/x`). Slash-only prose (`red/green`, `admit/reject`, `0/1/2/64/selftest`) is not a citation.
- Rejected: whitespace, `*`/`?` globs, chars outside `[A-Za-z0-9._/-]`, absolute paths, URLs, `..` segments (so `A..B` revision ranges are not paths), pure-numeric ratios, and a bare extension token (`.log`).
- Dedupe per commit, first-seen order.
- Resolution: `cat-file -e <c>:<path>` (blobs and trees); a path without `/` that does not resolve is retried as a unique suffix of `ls-tree -r --name-only <c>` and counts as resolved-bare only on exactly one match, reported as `bare=`; zero or several matches is a miss (frozen rule).

`--selftest` builds its own throwaway fixture under `$HYAKU_SCRATCH/revenger-r91/ExecR91MsgTree` (`mktemp -d`, `git -C "$D"` on every call, toplevel asserted equal to `$D` before the first commit): a clean commit citing `a.txt`, a planted commit citing `missing/r91.txt`, and a `.log` leg (`reports/probe.log` plus the bare `probe.log`, which must resolve by unique suffix). It prints `MSG_TREE_SELFTEST=pass` and exits 0 only if the clean range exits 0, the planted range exits 1 naming `missing/r91.txt`, and the `.log` leg exits 0 with `bare=probe.log`. The fixture is removed in a `finally`.

## Retained evidence

All under `.ufo/waves/round-91/w1/ExecR91MsgTree/`:

- `probe.log` — frozen counter, tail:

```
CAP_PRESENT=1 path=/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-91/message_tree_check.py
CAP_SELFTEST=pass exit=0
CAP_PLANTED_MISS=pass clean_exit=0 dirty_exit=1
CAP_REAL=pass commits=23 cited=25 misses=9 exit=1
LEGS present=pass selftest=pass planted=pass real=pass
CAP_MESSAGE_TREE=pass
probe_exit=0
```

- `selftest.log` — `MSG_TREE_SELFTEST=pass`, exit 0.
- `real-range.log` — full 23-commit run; summary line:

```
MESSAGE_TREE commits=23 cited=25 misses=9
```

- `grep -n '/tmp' reports/round-91/message_tree_check.py` → empty (exit 1). Scratch fallback is `$HYAKU_SCRATCH`, then `/fast/scratch/hyaku`, then `tempfile.gettempdir()`; no literal path is written in the file.

Command (acceptance): `cd /home/vgpnk/Projects/shokunin/revenger-shokunin && PYTHONUTF8=1 python3 -B reports/round-91/cap_probe.py --lane . --range 7fab03f..refs/heads/main` → `CAP_MESSAGE_TREE=pass`, exit 0, all four legs pass.

## Semantics check (own fixture, scratch only, deleted)

Built a 9-commit fixture exercising the reviewer's cases; measured behaviour:

| case | fixture citation | result |
|---|---|---|
| (a) plain prose, no backticks, absent | `missing/plain.txt` | exit 1, `missing=missing/plain.txt` |
| (b) `path:line`, `./path`, `path,` | `dir/file.py:12`, `./dir/file.py`, `dir/file.py,` | dedupe to 1 cited, resolves, exit 0 |
| (c) backticked directory | `sub/logs/` | resolves as tree |
| (d) bare `.log` landing later | `later.log` | miss at citing commit; `bare=later.log` after it lands |
| (f) rename | `old/name.py` → `new-name.py` | each hit in its own commit |
| (g) commands/flags/word | `git status`, `git log -1`, `--amend`, `jj` | cited=0, exit 0 |
| (h) `--no-ff` merge | `merged.txt` landed by the merge | hit |
| empty A | `--range ..<tip>` | all history listed |
| usage | bad range / no args | exit 2 |

## Findings on the real range (measured, not inferred)

`commits=23 cited=25 misses=9`, instrument exit 1. The nine misses:

- absent at the citing commit: `ufo-wave-policy.json` (d509e98, 0 same-named files in that tree).
- ambiguous bare citations (the frozen rule resolves a bare name only when exactly one suffix matches; the counts are same-named files at that commit): `claims.md` (30), `w1-results.json` (4), `truth.json` (53), `inspection.json` (31), `receipt.json` (21), `LEDGER.md` (72), `c1-only.log` (11), `noharm-diff.txt` (13).

Eight of nine are therefore "cited without its directory, and the basename is not unique" — a real hygiene signal of the same class the claim names (the message names a file the tree carries, but not at a locatable path), distinct from a fabricated citation. Reported separately rather than folded into "absent".

## Limitations (declared, not hidden)

1. An extension-less directory written without a trailing `/` (`corpus/live/runs/round-89`, `reports/round-89/rejected-android-record` at bd575ca) is not read; writing it as `corpus/live/runs/round-89/` makes it measurable. This costs two genuine directory citations on this range.
2. Slash-only prose is deliberately not a citation; the price is that a real extension-less, dot-less path is skipped too.
3. Ambiguous bare names count as misses by the frozen rule; `missing=` does not distinguish "absent" from "ambiguous".
4. A cited path that exists only as a directory prefix of a cited file is not separately checked (each token is checked as written).

## Risks

- `cited=25` clears the frozen `M ≥ 20` leg with a margin of 5 on the declared range; the count is deterministic for a fixed range, but a range with many extension-less directory citations would under-count.
- The real range legitimately exits 1 (K=9); the probe's leg 4 does not require K=0, and the instrument is not claimed to make the lane's history clean.

## Hygiene

- No mutating git/jj command in the lane; read-only `git log/show/rev-parse/ls-tree/cat-file/rev-list` only.
- Every fixture used `D=$(mktemp -d)` + `git -C "$D" init -q` with the toplevel asserted before the first commit; fixtures lived under `$HYAKU_SCRATCH/revenger-r91/ExecR91MsgTree` and were removed (`trap`/`finally`).
- No tool installed or upgraded; pacman not touched. Lane writes: `reports/round-91/message_tree_check.py` and this wave directory only.
