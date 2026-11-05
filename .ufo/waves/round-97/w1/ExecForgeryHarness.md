# ExecForgeryHarness — round-97 w1 findings (C2 calibration instrument)

## Files written

- `reports/round-97/forgeries/manifest.json` — 19 delta names in order.
- `reports/round-97/forgeries/<name>/builder.py` — 19 directories, each holding
  the exact file mutations for one vector. The builder function body was copied
  verbatim (AST-verified, 19/19 byte-identical to the source segment) from
  `.ufo/waves/round-96/w1/CriticR96/receipts/drv.py`; only a local harness
  binding (`mod`, `VOTES_DIR`, `WAVE_DIR`, `SEATS`, `repin`/`entry_read`/
  `entry_write` helpers) was added around it. The frozen r96 module is never
  imported by the new harness.
- `reports/round-97/forge_reach6.py` — args `--counter <path> --deltas <dir>
  --work <scratch dir>`; builds each honest fixture with the counter's own
  `_fixture` (counter loaded read-only via importlib), applies each delta's
  `builder.py`, runs `python3 -B <counter> --tree <root>` with `TMPDIR=<work>`,
  prints `DELTA <name> verdict=<pass|fail> legs=<comma list>` per vector and
  `C2_ACCEPTED=<n>/19` (accepted = `C1_VERDICT=pass`). Exit 0 on completion,
  exit 2 on harness error. Also supports `--self-test [--work <dir>]`.
- `reports/round-97/controls/c2-v5-reproduced.log` — v5 reproduction run
  (full stdout, final line `rc=0`).
- `reports/round-97/controls/c2-stub-selftest.log` — stub self-test run
  (full stdout, final line `rc=0`).

## Delta-name → builder-function mapping (source: drv.py FORGERIES)

| Delta directory | Builder function in drv.py |
|---|---|
| FG01-shadow-decorated-admitted | fg01_shadow_decorated |
| FG02-shadow-nested-dir | fg02_shadow_nested |
| FG03-shadow-uppercase-ext | fg03_shadow_upper_ext |
| FG04-shadow-non-utf8 | fg04_shadow_non_utf8 |
| FG05-vote-html-comment-artifact | fg05_html_comment_artifact |
| FG06-vote-symlink-alias | fg06_symlink_alias |
| FG07-sid-double-space-evade | fg07_sid_double_space |
| FG08-loose-pyc-file | fg08_loose_pyc |
| FG09-receipt-quote-irrelevant | fg09_receipt_irrelevant_quote |
| FG10-sources-url-drift | fg10_sources_url_drift |
| FG11-table-lie-fixture-swap | fg11_table_lie_fixture_swap |
| FG12-tab-status-digest-invariant | fg12_tab_status |
| FG13-status-below-window | fg13_status_below_window |
| FG14-trio-line-shift | fg14_trio_shift |
| FG15-qmap-extra-row | fg15_qmap_extra_row |
| FG16-nbsp-status-fork | fg16_nbsp_status |
| FG18-usedby-dot-slash-alias | fg18_usedby_dot_slash |
| FG19-merged-fetch-log-line | fg19_merged_fetch_log |
| FG20-prose-status-mention | fg20_prose_status_mention |

FG17 absent (per frozen claims). `manifest.json` lists the 19 names in the
order above, matching `summary.json` order exactly.

## Self-test (exit 0)

Command: `TMPDIR=/fast/scratch/hyaku/revenger-r97/ExecForgeryHarness python3 -B
reports/round-97/forge_reach6.py --self-test --work <scratch>/selftest`

Result lines:

- stub-always-pass: `C2_ACCEPTED=19/19`
- stub-always-fail: `C2_ACCEPTED=0/19`
- `SELFTEST stub-pass accepted=19/19 stub-fail accepted=0/19`
- `SELFTEST verdict=OK`, `rc=0`

Stubs have no `_fixture`: the harness falls back to a minimal temp tree and
applies builders best-effort (builders that need honest-tree files log a
`builder note` on stderr and no-op; the stub verdict decides the score either
way). Full output in `reports/round-97/controls/c2-stub-selftest.log`.

## v5 reproduction against frozen r96 counter (exit 0)

Command: `TMPDIR=<scratch> PYTHONUTF8=1 python3 -B
reports/round-97/forge_reach6.py --counter
reports/round-96/c1_k_admit_counter5.py --deltas reports/round-97/forgeries
--work <scratch>/v5run`

Result: `C2_ACCEPTED=14/19`, `rc=0`. Full output:
`reports/round-97/controls/c2-v5-reproduced.log` (19 `DELTA` lines).

Per-delta verdicts vs committed
`.ufo/waves/round-96/w1/CriticR96/receipts/summary.json` `observed_verdict`:

- Accepted by v5 (14): FG01, FG02, FG03, FG04, FG05, FG06, FG07, FG08, FG09,
  FG10, FG11, FG12, FG15, FG19.
- Rejected by v5 (5): FG13 (`C1_ADMITTED,C1_VERDICT`), FG14
  (`C1_TRIO,C1_LINT,C1_VERDICT`), FG16 (`C1_ADMITTED,C1_VERDICT`), FG18
  (`C1_SOURCES,C1_VERDICT`), FG20 (`C1_ADMITTED,C1_VERDICT`).
- **Per-delta diff: NONE — match.** The accepted set is identical to the
  committed `summary.json` (14 `observed_verdict=pass` rows), consistent with
  the frozen claims' recorded 14-vs-13 mismatch (claims.md §C2 Before).

## Notes / risks

- The counter under test is imported only for `_fixture` + constants
  (`ENTRY`, `VOTES_DIR`, `RECEIPTS_DIR`, `FETCH_LOG_REL`, `digest`). The
  builders re-derive the rest; they do not import the r96 `drv.py` module.
- No git mutation, no scoring of the candidate landing tree, no edit of
  frozen claims or frozen r96/r93–r95 bytes. Scratch under
  `/fast/scratch/hyaku/revenger-r97/ExecForgeryHarness/` was deleted before
  yield (receipts copied into `controls/` first).
- No tooling installs were needed (system python3 3.14.8 used; no pacman/uv
  installs).

## Open questions

- None blocking. The L1 owns scoring v6 on these 19 vectors after the freeze.
