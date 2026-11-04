# ExecR91RealRun — C2 real-history receipt (round 91, w1)

Seat: executor ×1 (real-range receipt). Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.
Read-only over the lane tree; the only writes are this report and
`.ufo/waves/round-91/w1/ExecR91RealRun/{real-run.log,real-run-table.md}`.

## Numbers (pinned run)

| quantity | value |
|---|---|
| range | `7fab03f..refs/heads/main` |
| `git rev-list --count` | **23** commits (range base `7fab03f32e…`, head `d509e982844d…`) |
| `MESSAGE_TREE commits=` | **23** (acceptance floor N ≥ 20 met) |
| `cited=` (M) | **25** |
| `misses=` (K) | **9** |
| commits with ≥ 1 miss | **6** (d509e98, b13aac7, b280719, e0fbf2e, 6ce41aa, 45b2713) |
| **genuine message/tree mismatches** | **1** (d509e98 cites `ufo-wave-policy.json`) |
| instrument exit | 1 (K > 0, as specified) |

Summary line, verbatim from the log:

```
MESSAGE_TREE commits=23 cited=25 misses=9
```

## Artefacts

- `real-run.log` — instrument sha256, range, `--json` run, text run, both exits, sha256 after.
  Path: `.ufo/waves/round-91/w1/ExecR91RealRun/real-run.log`.
- `real-run-table.md` — every one of the 9 misses with verdict + proving read-only command.
  Path: `.ufo/waves/round-91/w1/ExecR91RealRun/real-run-table.md`.

Instrument bytes were pinned: `reports/round-91/message_tree_check.py`
sha256 `4e45c2898b15b0170613a4725a2f3dfb243536c6a670faf7edaff42dc7a018be`,
11836 bytes / 320 lines, unchanged before and after both runs (`STABLE: yes`).

## Miss classification (9)

1 genuine mismatch, 8 ambiguous bare filenames, 0 renames-in-parent in the pinned run.

- **Genuine (1): d509e98 `ufo-wave-policy.json`.** `git cat-file -e d509e98:ufo-wave-policy.json`
  fails; `git ls-tree -r --name-only d509e98 | grep -c 'ufo-wave-policy'` = 0; the parent
  `b13aac7` does not carry it either; `git log --all --oneline -- '*ufo-wave-policy.json'` is empty,
  so the path was never tracked in this repo's history. The artefact the message means exists only
  at fleet-root `scripts/hyaku/ufo-wave-policy.json`, outside the lane repo — i.e. the message cites
  a repo-relative path its own tree does not carry. This is exactly the commit-hygiene class the
  claim is built on, and the instrument catches it.
- **Ambiguous bare names (8):** `claims.md`@b13aac7, `w1-results.json`@b280719, `truth.json`@e0fbf2e,
  `inspection.json`/`receipt.json`/`LEDGER.md`@6ce41aa, `c1-only.log`/`noharm-diff.txt`@45b2713.
  Each has 4–72 suffix candidates in the same commit's tree, so `resolve()`'s unique-suffix rule
  returns `miss`. For each, the intended path is present in that commit's own tree
  (e.g. `b13aac7:reports/round-91/claims.md`, `6ce41aa:corpus/live/runs/round-89/LEDGER.md`,
  `45b2713:reports/round-88/c1-only.log`). These are instrument precision limits on bare filenames,
  **not** message/tree mismatches. Per-miss counts and commands are in `real-run-table.md`.
- **Renames / exists-in-parent (0 in the pinned run).** The one real instance in this range is
  `bd575ca`, whose message cites `corpus/live/runs/round-89` (carried by its parent `6ce41aa`, moved
  by that commit to `reports/round-89/rejected-android-record/`; `git diff --name-status -M bd575ca^
  bd575ca` shows `R095`/`R100`). The pinned extraction rule does not read extension-less directory
  tokens without a trailing `/` (declared in `path_shaped`'s docstring), so `bd575ca` reports
  `cited=0` and the rename class is unexercised here. Recorded as a declared limitation, not counted
  as a miss.

## C2 counter (context, not my counter command)

`PYTHONUTF8=1 python3 -B reports/round-91/cap_probe.py --lane . --range 7fab03f..refs/heads/main`
on the same pinned bytes: `CAP_PRESENT=1`, `CAP_SELFTEST=pass exit=0`,
`CAP_PLANTED_MISS=pass clean_exit=0 dirty_exit=1`,
`CAP_REAL=pass commits=23 cited=25 misses=9 exit=1`, `CAP_MESSAGE_TREE=pass`, exit 0.
Leg 4 requires only N ≥ 20 and M ≥ 20, so K = 9 does not break the predicate; the instrument's
nonzero exit is the specified K > 0 behaviour.

## Honest disclosures

- The instrument was still being edited when I first ran it. A `--json` run at 19:43:23 hit
  sha256 `1645f88…`/11445 B and reported `cited=43 misses=25`; a text run minutes later hit a newer
  revision and reported `cited=25 misses=9`. That 43/25 vs 25/9 gap is **cross-version, not
  mode-dependent**: on the pinned `4e45c28…` bytes both modes print the identical
  `commits=23 cited=25 misses=9`. The discarded early runs are not in `real-run.log`; the log records
  only the pinned pair plus before/after hashes.
- Scope: every statement above is about the 23 commits in `7fab03f..refs/heads/main`. No claim is
  made about commits outside that range.
- No mutating git command was run in the lane repo; all evidence is `cat-file`, `ls-tree`, `log`,
  `diff --name-status -M`, `rev-list`, `rev-parse`. No fixture repo was needed. Scratch dir
  `$HYAKU_SCRATCH/revenger-r91/ExecR91RealRun` was created and removed; nothing was installed.

## Verification the parent should run

1. `cd /home/vgpnk/Projects/shokunin/revenger-shokunin && PYTHONUTF8=1 python3 -B reports/round-91/cap_probe.py --lane . --range 7fab03f..refs/heads/main` → `CAP_MESSAGE_TREE=pass`, exit 0.
2. `grep -n 'MESSAGE_TREE' .ufo/waves/round-91/w1/ExecR91RealRun/real-run.log` → `MESSAGE_TREE commits=23 cited=25 misses=9`.
