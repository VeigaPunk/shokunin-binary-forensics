# ScribeLessonR99 — findings (revenger round 99, wave w1)

Seat: `ScribeLessonR99` (scribe). Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.
Scratch: `/fast/scratch/hyaku/revenger-r99/ScribeLessonR99/` (receipts copied to the wave dir, scratch deleted).

**Tools installed or upgraded: none.** No `pacman`, no `uv tool`, no `npx`, no binary download. Read-only
probes only: `rea --version` (rc 0, `6.7.0`), `rea --llms` with `PYTHONUTF8=1` (rc 0, 153 rows), `binwalk
--version` (`binwalk 3.1.0`), `unblob --version` (`26.6.4`). `rea doctor` and `rea setup` were not run.

**Git:** read-only only (`git diff`, `git show`). No commit, stage, stash, reset or checkout.

## Files written

- `.ufo/waves/round-99/w1/ScribeLessonR99/round-99-lesson-draft.md` — the lesson draft for the L1 to copy
  to `corpus/lessons/round-99.md`. Sections: `## Gate`, `## Mistakes` (M16–M18), `## Frontier`,
  `## considerthese`. Placeholders `<<L1: …>>` only for vote, score and census outcomes. The L1 copies it;
  nothing under `corpus/` was written.
- `.ufo/waves/round-99/w1/ScribeLessonR99/candidate-diff-r98-to-r99.diff` — the entry diff (`3d054a98..7e6edd4`).
- `.ufo/waves/round-99/w1/ScribeLessonR99/m18-seat-name-collision.txt` — M18 command and output.
- `.ufo/waves/round-99/w1/ScribeLessonR99/proposal4-measurements.txt` — considerthese proposal 4 measurements.
- `.ufo/waves/round-99/w1/ScribeLessonR99/rea-llms-6.7.0-host.txt` — the installed manifest (`rea --llms`, 153 rows).
- `.ufo/waves/round-99/w1/ScribeLessonR99.md` — this file.

## Counting commands and outputs (observed)

| check | command | output | rc |
|---|---|---|---|
| base digest and freeze digest (v7 rule) | `python3 -c` over `git show 3d054a98:…` and the freeze file | `6d27c129…5330f` (base), `36cc6ac2…fce5` (freeze) | 0 |
| entry diff | `git diff --stat 3d054a98 7e6edd4 -- corpus/knowledge/round-98-rea-host-readiness.md` | 1 file, 17 insertions, 10 deletions | 0 |
| derivation rows base / freeze | python table diff | 17 / 21 (added 5, removed 1) | 0 |
| M16 old command | `grep -c '^    paths\[3\]: ' corpus/live/runs/round-98/rea-doctor-r98.txt` | `1` | 0 |
| M16 new command | `grep '^    paths\[3\]: ' … \| sed … \| tr ',' '\n' \| grep -c .` | `3` | 0 |
| M17 attribution | `grep -c -F <v>` on host-probes / doctor | `12.1.4` 0/17; `21.0.13` 3/3; `6.7.0` 1/11; `1.5.6` 1/0; `3.1.0` 1/0; `26.6.4` 1/0 | 0 |
| M18 collision | `for f in .ufo/waves/round-9*/w1/swarm-registry.json; do python3 …` | six registries (rounds 93–98) share `ReviewerGate` and/or `ReviewerBlind`; round 99 registry none | 0 |
| S506 body | `sha256sum`, `wc -c`, `grep -c -F` | `ce2d122b…2282e50`, 16650 bytes, quote count 1 | 0 |
| S506 span | `head -c 7202 … \| tail -c +7127` | the 76-byte sentence (11 words) | 0 |
| S507 span | `head -c 41 corpus/live/runs/round-98/rea-doctor-r98.txt \| wc -c` | 41 | 0 |
| S507 re-hash | `sha256sum corpus/live/runs/round-98/*` | `94eaa6ff…`, `fb9a4824…`, `c373f656…` (equal to r98) | 0 |
| C1 base rows | `grep -cE` over `corpus/README.md` for held rows | `13` | 0 |
| S505 citation | `grep -c S505` / `grep -c S504` on `corpus/knowledge/round-96-native-analysis-sessions.md` | `0` / `3` | 0 |
| M4 index | `grep -c claude-red-re-bridge corpus/README.md` | `0` | 0 |
| census (round-start receipt) | `tail -1` and `grep -c` on `reports/round-99/controls/census-round-start.log` | `# rc=0 base=3d054a98…`; W01 21, W04 13, E 0 | 0 |
| producer attribution (proposal 4) | `grep -rl 'rea 6\.8\.0' corpus/live/runs/ \| wc -l` | 15 (rounds 76–85) | 0 |
| producer attribution | `grep -rl 'cli_package_version: 6\.7\.0' corpus/live/runs/ \| wc -l` | 2 (r96, r98) | 0 |
| producer attribution | `grep -rl 'cli_commands: 175' corpus/live/runs/ \| wc -l` | 0 (S444 row at `corpus/SOURCES.md:459` records 175) | 0 |
| host version | `rea --version`; fnm `rea-agents/package.json` version | `6.7.0`; `6.7.0` (PROVINCE.md:22 says 6.8.0 installed on 2026-10-31) | 0 |
| operation census | python over `corpus/live/runs/` and the saved 6.7.0 manifest | 153 declared; 30 recorded operation names; 22 with a declared twin; 8 without (`current_document`, `get_android_manifest`, `get_app_info`, `inspect_pe_certificates`, `inventory_artifact`, `load_apk`, `open_binary`, `rea_jvm_status`); 131 declared with no recorded operation | 0 |
| pointer existence | `test -e` over every path the draft cites | all present; the one non-path entry `…:109`/`:78` was checked by `sed -n` and both lines carry the cited text | 0 |

## Findings the L1 must act on

1. **The draft's Gate is complete except for outcomes.** Only vote, v8 score, control and census results
   are `<<L1: …>>` placeholders. The digest, S506/S507 re-opens and C2 baseline are measured here.
2. **M16–M18 each carry a runnable pointer and a shown-able-to-fail row.** M18's fix (round-suffixed seat
   names) is what the r99 registry already uses; the collision check was not part of any lint.
3. **Producer-version drift is real in the lane's own bytes.** Fifteen live records (rounds 76–85) say
   `rea 6.8.0`; the two doctor records (r96, r98) and the host (`rea --version`, the fnm `rea-agents`
   package) say 6.7.0 with 153 commands. S444 (`corpus/SOURCES.md:459`) and PROVINCE.md:22 say 6.8.0. The
   committed bytes do not date the change, and I did not establish the cause. Not a claim; a Frontier item.
4. **S505 `used-by` is still ungrounded** (0 mentions in the cited knowledge file). The r99 frozen claims have
   no S505 leg, so any fix is a new claim for the L1.
5. **Proposal 4 of `considerthese/2026-11-05.md` is mined** (a counting predicate, not a daily tracker). It
   is proposed for r100 with its own frozen predicate, not adopted.

## Open questions for the L1

- Whether to freeze the producer-attribution census in r100 or keep it as a Frontier count.
- Whether the S505 citation fix goes into a superseding C02 entry revision.
- Assimilation re-check result is owed by `ScoutReopenR99`; I did not re-run it.
- The r98 mutate7 self-test baseline (exit 3) versus `selftest-v7-frozen.log` (OK, rc 0) is still unreconciled.

## Scratch

`/fast/scratch/hyaku/revenger-r99/ScribeLessonR99/` held two copies (`candidate.diff`, `llms.txt`). Both were
verified byte-identical in the wave dir (`cmp` rc 0), then the scratch directory was removed (`test -e` → gone).
