# ScribeLesson — round 97, wave w1, attempt 1 — scoped findings

Seat: `ScribeLesson` (role `scribe`, registry `.ufo/waves/round-97/w1/swarm-registry.json`).
Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`. **Drafting seat — no lane file was written,
edited or deleted.** The only writes are this report and three drafts, all inside this seat's wave
dir `.ufo/waves/round-97/w1/ScribeLesson/`. Scratch root
`/fast/scratch/hyaku/revenger-r97/ScribeLesson/` — created, used, **deleted** before yield; receipts
were copied into the wave dir first. No tool was installed (nothing was needed beyond `python3 -B`,
`git` read-only, `awk`, `grep`, `sha256sum`, all preinstalled). No network fetch was made by this
seat. No git/jj mutation was run anywhere (`git archive`, `git show`, `git status`, `git diff` only).

**Deliverables (drafts for the L1 to paste after measurement):**

| file | what it is |
|---|---|
| `.ufo/waves/round-97/w1/ScribeLesson/lesson-round-97.md` | the round-97 lesson draft: `## Gate` (Q01–Q17 pointer + located-quote placeholders + the Assimilation line), `## Mistakes` (M5, M8, M9), `## Frontier` (census before at `7d380ce` + the rows touched), `## considerthese` (proposal 1 mined) |
| `.ufo/waves/round-97/w1/ScribeLesson/S505.row.md` | the S505 superseding-row draft in the 11-column schema, with the awk column proof and the four L1 constraints |
| `.ufo/waves/round-97/w1/ScribeLesson/SCORECARD-r97.md` | the SCORECARD round-97 section draft (C1 + C2 rows) with the r96 mismatch correction line **appended**, and the L1 notes kept outside the pasted section |

Placeholder tokens the L1 fills (each draft lists its own; the L1 should also list them in the
lesson's own placeholder index):

- lesson draft: `[[RG-Q01]]`…`[[RG-Q17]]` (the parallel ReviewerGate seat's verdicts),
  `[[S502-QUOTE]]`, `[[S503-QUOTE]]`, `[[S504-QUOTE]]`, `[[C1-VERDICT]]`, `[[C1-K-AFTER]]`,
  `[[C2-ACCEPTED]]`, `[[CENSUS-AFTER-RC]]`.
- S505 row draft: `[[S504-QUOTE]]` (the byte-verbatim span the row's anchor cell carries).
- SCORECARD draft: `[[R97-HEADLINE]]`, `[[C1-K-AFTER]]`, `[[C1-C02-STATUS]]`, `[[C1-VERDICT-LINE]]`,
  `[[C1-EXIT]]`, `[[C1-MEASURED-COMMIT]]`, `[[C1-VERDICT]]`, `[[C2-ACCEPTED-AFTER]]`, `[[C2-EXIT]]`,
  `[[C2-MEASURED-COMMIT]]`, `[[C2-VERDICT]]`, `[[SOURCES-ROWS-AFTER]]`, `[[CENSUS-AFTER-RC]]`.

---

## 1. Behaviour actually executed (read-only over committed bytes)

| # | check | observed |
|---|---|---|
| 1 | `reports/round-97/claims.md` read in full; freeze commit `3b4b4e5c1d123d5fc5337ad59015b4752366854a` confirmed | claims frozen, untouched |
| 2 | census over the fleet root, lane `revenger`: `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger` | **exit 0**; 21 × W01, 13 × W04, **0 E-codes**; last line `revenger ok …/corpus/SOURCES.md` (receipt `receipts/census-before.log`) |
| 3 | census over the **base tree** `7d380ce` extracted with the recipe `git archive --format=tar 7d380ce corpus reports .ufo \| tar -x -C <scratch>/tree` (+ the base `SCORECARD.md`, `LOG.md`, `SKILL.md`, `README.md`, `PROVINCE.md`) | **exit 0**, same profile: 21 W01, 13 W04, 0 E-codes (receipt `receipts/census-base-tree-7d380ce.log`) — the round-start census profile is the base profile |
| 4 | `git show 7d380ce:corpus/SOURCES.md \| sha256sum` vs `sha256sum corpus/SOURCES.md` | identical `db18d1fd…977e`; same for `corpus/README.md` (`d3dd5ab6…1936`) → the census run in (2) **is** the census at `7d380ce` |
| 5 | registry size / tier / status histogram over `corpus/SOURCES.md` | 504 rows (S001–S504); tier A 455 / B 21 / C 28; status mined 468 / queued 16 / rejected 20 |
| 6 | base S5xx row count: `git show 7d380ce:corpus/SOURCES.md \| grep -c '^| S5'` | 5 (S500–S504) — S502/S503/S504 are **already in the base registry** |
| 7 | **S505 draft row** column count: `awk -F'|' '{print NF-2, "cells"}' S505.row` | `11 cells`; `awk -F'|' '{print NF}' S505.row` → `13` (what the census' `gawk -F'|'` sees). Row stored at `receipts/S505.row` |
| 8 | S505 draft row **inserted into a scratch copy** of the base tree (inside `## Registry`, after the S504 row, before `## Paths`) and the census re-run | **exit 0**, 21 W01, 13 W04, **0 E-codes** — byte-identical finding profile to the base tree; **no new finding of any kind from S505** (diff of the two logs: only the `ok` line's path differs) (receipt `receipts/census-tree-with-S505.log`) |
| 9 | `reports/round-90/source_path_check.py --root` over the base tree and over the tree with S505 | both **exit 0**, `SOURCE_PATH_DEAD=0`, `SOURCE_PATH_MALFORMED=0`, `SOURCE_PATH_EXCUSED=1` — the S505 row adds no dead path (receipts `source-path-check-base.log`, `source-path-check-with-S505.log`) |
| 10 | S504 quote defect: `grep -c -F 'undefined8 entry(void) { return 0x2a; }' corpus/live/runs/round-96/codeable-decompiled.c` | **0**, exit 1 — the r96 lesson's one-liner is absent from the saved bytes (the file holds the five-line block at lines 6–10) |
| 11 | S504 byte layout: `sed -n '1,12p'` / a byte-offset read of `codeable-decompiled.c` | 170 bytes, sha256 `d717b491…fc9d`; entry block = chars/bytes 101–142 = `undefined8 entry(void)\n\n{\n  return 0x2a;\n}` (6 whitespace-separated words); the token `return 0x2a;` is at line 9 (bytes 129–140) |
| 12 | S502/S503 located quotes: `grep -c -F` of each receipt quote against the committed body | 1 and 1 (exit 0) — both quotes are byte-verbatim present; S502's receipt quote equals `body[26309:26411]` exactly (the receipt's leading-backtick difference vs the lesson quote is the r96 ScoutReopen seat's documented delta) |
| 13 | candidate digest: the counter's own normalization (status line rewritten to `candidate`) applied to `corpus/knowledge/round-96-native-analysis-sessions.md` | `2f7d4c1b754d812102563869b511a746c7c49750d8cc42859b2a6466d776d923` — equals the frozen vote digest, and is **unchanged** when the status line is flipped to `admission-status: admitted (round-97 gate, two reviewer votes)` |
| 14 | r96 vote decisions: the three committed `reports/round-96/votes/*.json` | identical decision sets across the three seats (11 PASS, 6 n/a) |
| 15 | where the "13" of the r96 mismatch actually lives | `SCORECARD.md` (r96 calibration row, "found 13 counter PASSES"), `corpus/lessons/round-96-verifier-spotcheck.md`, `.ufo/waves/round-96/w1/CriticR96/findings.md` — **not** in `corpus/lessons/round-96.md`, whose only "13" is `C1_K_HELD_BACKED` at 13/15 |
| 16 | the committed receipts recount: `summary.json` → 19 rows, 14 with `observed_verdict=pass` (FG01–FG12, FG15, FG19) | matches `reports/round-97/controls/c2-v5-reach-from-r96-receipts.txt` (`C2_V5_ACCEPTED 14 / 19`) and `reports/round-97/controls/c2-count-audit.log` (`accepted 14/19`) |
| 17 | **the frozen C2 counting command, run verbatim** | `PYTHONUTF8=1 python3 -B reports/round-97/forge_reach6.py --counter reports/round-97/c1_k_admit_counter6.py --deltas reports/round-97/forgeries` → **exit 2**, argparse usage error (`--counter, --deltas and --work are required`), **no `C2_ACCEPTED=` line** (receipt `receipts/claims-c2-command-as-written-rc2.log`) — see finding F-S1 |
| 18 | the v6 counter's used-by normalizer and new-row checks (source read, no run): `reports/round-97/c1_k_admit_counter6.py` | `ub_norm` strips a leading `corpus/` at `:426` and compares to `ENTRY_REL` at `:427`; the new-row loop at `:405-428` requires `status=="mined"` (`:410`), `opened==ROUND_DATE` (`:412`), `tier=="A"` (`:414`), cite-back (`:416`), used-by exclusivity (`:427`) for every row of `NEW_ROW_IDS = ("S502","S503","S504")`; the supersede chain map is built at `:379-381` and the terminal row must be `mined` (`:403-404`) |
| 19 | the v6 counter's own base do-nothing and red-before logs (read, not re-run by this seat) | `base-v6.log` → `C1_VERDICT=fail`, `C1_K_HELD_BACKED=12/15`, rc 1; `red-v5-corpus-prefix.log` → `C1_SOURCES=fail` rc 1; `green-v6-corpus-prefix.log` → `C1_SOURCES=pass`, `C1_VERDICT=pass` rc 0; `red-v5-decorated.log` → v5 `C1_ADMITTED_UNION=pass`, `C1_VERDICT=pass` rc 0; `green-v6-decorated.log` → v6 `C1_VERDICT=fail` rc 1 |
| 20 | the harness's own logs (read, not re-run by this seat) | `c2-v5-reproduced.log` → `C2_ACCEPTED=14/19` rc 0; `c2-stub-selftest.log` → stub-pass 19/19 accepted, stub-fail 0/19 accepted, `SELFTEST verdict=OK` rc 0 |
| 21 | assimilation: `wc -l` on `.ufo/waves/round-97/assimilation/{collisions,staged-ids,reg-ids}` + a set test | 155 / 155 / 504; **all 155 staged ids are present in `reg-ids`** → 155/155 collide, nothing adopted |
| 22 | `git status --porcelain` at finish | only untracked round-97 artefacts (other seats' files and this seat's wave dir) — no tracked lane file modified |

## 2. Gates this seat did not cross

- **No lane write.** `corpus/` (incl. `SOURCES.md`, `README.md`, `QUALITY.md`, `lessons/`,
  `knowledge/`), `reports/round-96..97/`, `SCORECARD.md`, `LOG.md`, `SKILL.md`, `MANIFEST.json`,
  `considerthese/` — all untouched by this seat.
- **No git/jj mutation** anywhere: `git archive`, `git show`, `git status`, `git diff` only.
- **No counter scored on the candidate landing tree.** The v6 counter was **not** run by this seat at
  all; the counter's behaviour was read from source (item 18) and from the executor seat's committed
  control logs (item 19). The harness was run only to the extent of the argparse check in item 17,
  which produced no measurement.
- **No README flip, no entry flip, no `SOURCES.md` append** — all three are the L1's, on the landing
  tree, after the freeze.
- **No subagent dispatch** (leaf member).
- **Scratch deleted** before yield; receipts copied into the wave dir first.

## 3. Findings

### F-S1 — BLOCKING for the C2 count: the frozen C2 counting command in `claims.md` cannot be run verbatim

`claims.md` §C2 gives the counting command as

```
PYTHONUTF8=1 python3 -B reports/round-97/forge_reach6.py --counter reports/round-97/c1_k_admit_counter6.py --deltas reports/round-97/forgeries
```

The harness built this wave (`reports/round-97/forge_reach6.py:144-145`) requires `--work` as well and
errors out otherwise. Observed (item 17): **exit 2**, `error: --counter, --deltas and --work are
required (or use --self-test)`, **no `C2_ACCEPTED=` line printed**. The L1 must either append
`--work <scratch>` to the command it runs (the SCORECARD draft already prints it that way) or give the
harness a default `--work`. The claims file is frozen and was not edited by this seat. The C1
counting command needs no such repair — `c1_k_admit_counter6.py:1048-1049` accepts `--tree`.

### F-S2 — the S504 row must keep `status=mined`, so the supersede is a `teaches` relation, not a status flip

The v6 counter's `C1_SOURCES` leg requires **every** row of `NEW_ROW_IDS = ("S502","S503","S504")` to
be `mined` (`reports/round-97/c1_k_admit_counter6.py:405-428`). Older superseded rows in the registry
carry `rejected`/`queued` statuses, so the obvious way to "close" S504 would turn that leg red with
`S504:new-status:…`. The S505 draft therefore supersedes S504 **by `teaches`** (the prefix the
census' chain reader and the counter's own chain map both recognise:
`corpus/audit_source_quotes.py` `supersedes_map`, `re.match(r"^supersedes (S\d{3,})\b", cells[6])`)
while S504 stays `mined`, `opened=2026-11-05`, tier A, with its used-by cell unchanged. The counter
resolves the entry's cited S504 to its terminal and requires the terminal row to be `mined`
(`:403-404`) — S505 is `mined`, so the chain is consistent.

### F-S3 — the r96 "13" is not where the frozen claim says it is

`claims.md` §C2 says "the r96 SCORECARD and lesson state 13 accepted". Measured (item 15): the "13"
is in `SCORECARD.md` (r96 calibration row), in `corpus/lessons/round-96-verifier-spotcheck.md` and in
`.ufo/waves/round-96/w1/CriticR96/findings.md`; the r96 round lesson `corpus/lessons/round-96.md`
carries **no** accepted-vector count (its only "13" is `C1_K_HELD_BACKED` at 13/15). The substance of
the mismatch is confirmed — 14 `observed_verdict=pass` rows in the committed receipts vs 13 in the
prose — but the attribution in the frozen claim is imprecise. Recorded in the lesson's M8 row and in
the SCORECARD correction line; **not** corrected in the frozen claims (they are frozen).

### F-S4 — the S505 draft row is census-clean and path-clean (measured on scratch copies)

Inserting the drafted row into a scratch copy of the base tree and re-running the census gives
**exit 0** with the identical 21 W01 / 13 W04 / 0 E-code profile and **no new finding attributable to
S505** (item 8); `source_path_check.py` stays at `SOURCE_PATH_DEAD=0` (item 9). The row splits into
**exactly 11 cells** on unescaped `|` (`awk -F'|' '{print NF-2}'` → 11; `NF` → 13), which is what the
census' `gawk -F'|'` requires. Placement matters: a row outside the `## Registry` section draws
`E12 row outside Registry section` — the draft says to insert it after the S504 row and before
`## Paths`.

### F-S5 — ADVISORY: the r96 S504 "3 lines" descriptor is a second inaccuracy in the same sentence

The saved entry block is **five** lines (6–10, line 7 blank), not the three the r96 lesson's
descriptor claims, and the one-liner quote is absent from the bytes (items 10–11). The S505 anchor
cell states the line range 6–10 and the byte range 101–142 so the descriptor cannot drift again.

### F-S6 — ADVISORY: the v6 counter's default scratch root still carries the round-96 token

`reports/round-97/c1_k_admit_counter6.py:45` defaults its work root to
`… / "revenger-r96" / "c1v5"` under `gettempdir()` when neither `--work` nor `HYAKU_SCRATCH` is set.
The L1's landing-tree run should pass `--work` (or `HYAKU_SCRATCH`) so it does not write under the
shared `/tmp` default. This is an executor-side nit, not a predicate change.

## 4. Out-of-scope items (not this seat's call)

- The admission itself: the README C02 flip, the entry's `admission-status` flip and the `SOURCES.md`
  append are the L1's landing edits, after the v6 counter is committed. This seat drafted them; it
  did not make them.
- The C1/C2 verdicts — every measurement in the drafts is a placeholder for the L1 to fill from the
  landing-tree run.
- The Q01–Q17 verdicts — the parallel `ReviewerGate` seat's file; this seat left a pointer and did
  not copy its verdicts.
- The D1 quote defect in the frozen `corpus/lessons/round-96.md` — frozen bytes; the correction route
  proposed here is the round-97 lesson's `[[S504-QUOTE]]` plus the S505 row.
- Whether the v6 counter's `C1_QUOTES` leg is extended to own-work rows (the r96 spot-check's D1 asks
  for it) — the executor's scope; this seat did not run or score v6.

## 5. Artifact paths (all inside this seat's wave dir)

- `.ufo/waves/round-97/w1/ScribeLesson/lesson-round-97.md`
- `.ufo/waves/round-97/w1/ScribeLesson/S505.row.md`
- `.ufo/waves/round-97/w1/ScribeLesson/SCORECARD-r97.md`
- `.ufo/waves/round-97/w1/ScribeLesson/receipts/census-before.log`
- `.ufo/waves/round-97/w1/ScribeLesson/receipts/census-base-tree-7d380ce.log`
- `.ufo/waves/round-97/w1/ScribeLesson/receipts/census-tree-with-S505.log`
- `.ufo/waves/round-97/w1/ScribeLesson/receipts/source-path-check-base.log`
- `.ufo/waves/round-97/w1/ScribeLesson/receipts/source-path-check-with-S505.log`
- `.ufo/waves/round-97/w1/ScribeLesson/receipts/claims-c2-command-as-written-rc2.log`
- `.ufo/waves/round-97/w1/ScribeLesson/receipts/S505.row`
- this report: `.ufo/waves/round-97/w1/ScribeLesson.md`
