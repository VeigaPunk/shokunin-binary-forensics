# ExecControls findings — round 98, wave w1

Seat: ExecControls (executor). Freeze rev: `9d49002a3804de48d365b7d32849ada06745d64f`.
Scratch: `/fast/scratch/hyaku/revenger-r98/ExecControls/` (deleted before yield;
receipts copied into `.ufo/waves/round-98/w1/ExecControls/` first).

## Files written

- `reports/round-98/controls/make_c1_controls.sh` (new, executable, sha256
  `ecd2ad3e…f0e`). `make_c1_controls.sh <out-dir>` builds `do-nothing/` and
  `junk-row/` from `git archive 9d49002…`, prints `diff -r`, exits 0, runs no
  counter. It also asserts (its own Python check) that the only differing file
  is `corpus/README.md`, exactly one line changed, C14 `partial → held`.
- `reports/round-98/controls/skip-work-table-r98.md` (new, sha256 `2410af33…670`).
- `reports/round-98/controls/s505-usedby-fix.diff` (new; the exact one-line
  diff, sha256 `28e4287a…2d5`). Cells verified: only columns status
  (`mined → queued`) and used-by (`corpus/knowledge/round-96-native-analysis-sessions.md → —`)
  changed on line 522 (S505).
- `reports/round-98/controls/s505-census.log` (new; exit 0 — warnings only,
  `file … ok` final line; sha256 `354f19fa…3438`).
- `reports/round-98/controls/s505-v6-counter6.log` (new; frozen v6 on the
  corrected copy, **exit 1**; sha256 `303b2bb7…378`).
- `reports/round-98/controls/s505-freeze-baseline-v6.log` (new; frozen v6 on
  the untouched freeze tree, **exit 0**; sha256 `ff1e0707…2d5`).
- `reports/round-98/controls/s505-ungrounded-count.txt` (new; stdlib one-off
  output, sha256 `934f75d3…f796`).

Receipts in `.ufo/waves/round-98/w1/ExecControls/`: `make-c1-controls.log`,
`s505-census.log`, `s505-v6.log`, `freeze-v6.log`, `ungrounded-count.txt`,
`s505-usedby-fix.diff`. (A duplicate `make-controls.log` is a byte-identical
copy of `make-c1-controls.log`.)

## Counting-command outputs (exact)

`make_c1_controls.sh` run (exit 0):
```
diff -r …/ctl/do-nothing/corpus/README.md …/ctl/junk-row/corpus/README.md
61c61
< | C14 | … | partial |
> | C14 | … | held |
make_c1_controls: exactly one changed cell (README line 61, C14 partial -> held)
```
Only the C14 status cell differs; file sets identical otherwise.

Census on S505 copy: exit 0, output ends `file\tok\t<…>/s505copy/corpus/SOURCES.md`
(33 W-lines, no E-codes). Full log saved.

Frozen v6, corrected copy: exit **1** (`C1_VERDICT=fail`),
`C1_SOURCES_WHY=S504:terminal-mined-expected:S505:queued`; `C1_K_HELD_BACKED=13/15`.
Frozen v6, freeze baseline: exit **0** (`C1_VERDICT=pass`), all legs pass,
`C1_K_HELD_BACKED=13/15`, `C1_SOURCE_IDS=S002,S502,S503,S504`.

Registry-wide ungrounded used-by count (stdlib one-off, freeze tree):
```
registry rows parsed (## Registry): 507
mined-with-usedby rows: 471 (grounded 470, ungrounded 1)
rows with no citation in any used-by file:
  S505 used-by=['corpus/knowledge/round-96-native-analysis-sessions.md']
```

## Verdict / key finding (S505 mirror)

The S505 correction does **not** keep frozen v6 passing: it makes v6 fail with
exit 1. Cause (read from v6 source, `check_sources`): S505's teaches cell starts
`supersedes S504`, so v6's `terminal()` maps S504 → S505 and demands the terminal
row be `mined`; the correction sets S505 `queued`, so `S504:terminal-mined-expected:S505:queued`.
S505 is not in v6 `NEW_ROW_IDS`, but the supersedes chain exposes it anyway.
Census is unaffected (exit 0 — it checks path existence/enums, not supersedes).
The diff is logged, not landed (corpus/ is frozen). The v7
`C1_USEDBY_GROUNDED` leg will supersede this: on the base registry it must fail
on exactly S505 (confirmed: 470/471 grounded, only S505 ungrounded), and on the
landed S505 correction it must pass. Counting caveat recorded: 8 per-file
ungrounded pairs exist (e.g. `S480` vs `reports/round-89/claims.md`), but each
of those rows has another used-by file that cites it; only S505 has none.
If C1_USEDBY_GROUNDED is implemented per-file rather than per-row, it will
false-fail 8 rows — flagging for ExecCounterV7.

## Retained evidence

- `s505-usedby-fix.diff` (one-line diff, byte-copied from the scratch diff).
- Census + both v6 logs with exit codes in the fixes above (exact outputs above).
- Uncounted command: `git show 9d49002…:corpus/SOURCES.md` line 522 confirms the
  freeze bytes match the working tree (no local drift; `git diff 9d49002… HEAD`
  on `SOURCES.md`/`README.md` is empty).
- v7 counter does not exist yet in the lane (`reports/round-98/c1_k_admit_counter7.py`
  not found); per the freeze order, no counter was run on any landing tree,
  and `make_c1_controls.sh` runs no counter (L1 scores after the v7 freeze).

## Risks / open questions

- New control files placed under `reports/round-98/controls/` sit beside the
  frozen claims dir; they are new paths (not edits of frozen bytes), per my
  write scope. The L1 confirms they join the v7-freeze commit, not the claims
  freeze.
- `C1_USEDBY_GROUNDED` per-row vs per-file definition (above) needs the counter
  seat's decision.
- No tools were installed; no live peers were messaged.

## Checks for the main agent

1. `bash -n reports/round-98/controls/make_c1_controls.sh` (ran clean).
2. Re-run: `bash reports/round-98/controls/make_c1_controls.sh <scratch>/ctl`
   and confirm `diff -r` shows only README line 61.
3. Census on the S505-corrected copy (exit 0) and frozen v6 on the same copy
   (exit 1) — receipts in `.ufo/waves/round-98/w1/ExecControls/`.
