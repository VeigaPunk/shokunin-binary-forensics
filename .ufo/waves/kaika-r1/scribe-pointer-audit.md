# Scribe pointer audit — revenger `M01–M19` / `Q01–Q10`

- Round: kaika continuation, fleet round 1; audit date 2026-10-19.
- Lane worktree: `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/revenger-shokunin` (`HEAD` `8bbcb4e`; `corpus/lessons/round-1.md` is modified in the worktree and `corpus/QUALITY.md` / `corpus/README.md` are untracked).
- Inputs: `corpus/lessons/round-1.md:27-59`; `corpus/QUALITY.md:13-22`; the evidence pointers as written; fleet-root `MANIFEST.json:2782`; fleet-repo `.ufo/waves/kaika-w1/revenger-art.md:21-22,45` at `5b471e4`.
- Method: read-only. Every cited range was opened at the stated file and line; no REA producer call, no live target, no install, no commit. This report is the only file written.

## M rows — verdicts

`ok` = cited lines say what the class claims. `line-off` = right file, incomplete/off range; corrected range given. `wrong` = cited pointer cannot support the class (absent section, out-of-range file, or wrong report).

| id | cited evidence (as written) | verdict | what the cited lines actually say / correction |
|---|---|---|---|
| M01 | `LOG.md:26-30`; `corpus/lessons/2026-10-12-r1-provider-gap.md:3` | **ok** | `LOG.md:26` “Round 1 result … claim unmet”; line 28 native `analyze` exit 1 `provider_unavailable`; line 29 “no opened native session”; line 30 “Do not promote native readiness”. `provider-gap.md:3` records CLI acquired, provider unavailable. Caveat: no cited line records readiness being *accepted* as a pass; the range records the honest unmet claim. |
| M02 | `LOG.md:97-100` | **ok** | Line 99: comparison-tool target detection 0/1; the 1/1 static manual difference is “separately labeled”, “not the declared comparison-tool result”. |
| M03 | `LOG.md:189-192`, `LOG.md:211-214` | **ok** | r15 collision is `nonretryable` (`LOG.md:191`); r17 Wakaru is `capability_unavailable` (`LOG.md:212`). Both sections halt progression (`LOG.md:192`, `214`). Caveat: no identical retry is recorded; the class is the halt-rule lesson, not an observed retry. |
| M04 | `LOG.md:299-300` | **ok** | Line 300: `STOP` prepend shifted `JUMPDEST` to 17 while copied `PUSH1 0x10` still pointed at 16 (`STOP`), so the “valid jump destination” premise was false. |
| M05 | `LOG.md:614`, `LOG.md:625` | **ok** | Line 614: “Claim's stated 160-byte constant was wrong”, failed input retained. Line 625: r52 initial fixture changed the name key “without updating owning resource directory entry-count fields”, refusal retained. |
| M06 | `LOG.md:700-703` | **ok** | Line 700: comparison “substitutes the saved `entry_locations` rather than verifying byte-derived paths”; line 703 records the initial verifier exit 1 and the repair. |
| M07 | `LOG.md:711-716`; `reports/round-59/r59d-adjudicator.md:27-28` | **wrong** | First pointer is correct: line 711 records the successful REA call and `A=\ude00B!`; line 715 repeats the accepted JSON/hex. Second pointer is invalid: `reports/round-59/r59d-adjudicator.md` is **24 lines** (`wc -l`), and it adjudicates the r60/devin round, not the r59 refusal (it only says at line 24 that “r59 falsification stands unreversed”). Corrected pointer for the r59 review: `corpus/live/runs/round-59/reviewer.md:5,7` (“Declared calibration claim unmet”, accepted `A=\ude00B!`). |
| M08 | `LOG.md:720` | **ok** | Line 720: author said 7/7 directories; verifier’s own byte oracle found 8/8 and the correction was adopted. |
| M09 | `LOG.md:224` | **ok** | Line 224: the reviewer caught an initial wrong seed ID that referred to the `rot13(input)` line; the ledger was corrected and the typo retained as telemetry. |
| M10 | `LOG.md:383` | **ok** | Line 383: reviewer found the boundary checklist mislabel — `556` is the name child-directory pointer, not a data-entry pointer — corrected with attribution. |
| M11 | `LOG.md:458` | **ok** | Line 458: saved JSON was reformatted; its byte SHA `74a45d…` differs from the receipt’s raw-output SHA `8c8d96…`; the receipt does not bind the saved JSON. |
| M12 | `LOG.md:475` | **ok** | Line 475: the second refusal’s stated interval cause was not independently reproduced; neither refusal is used to promote a calibration claim. |
| M13 | `corpus/lessons/round-1.md:16`; `LOG.md:704` | **ok** | `round-1.md:16` rejects equating saved receipt hashes or Evidence IDs with authenticated producer origin/native readiness. `LOG.md:704`: historical producer origin cannot be authenticated by saved receipt hashes. |
| M14 | `corpus/lessons/round-1.md:8`; `SCORECARD.md:20-21` | **line-off** | `round-1.md:8` is correct (saved PE artifact path is historical identity, not an input locator). `SCORECARD.md:20` only says the language and numeric multi-image verifiers fail at original artifact-path assertions; line 21 is the coverage-F taxonomy, not M14. Corrected pointer: `SCORECARD.md:9,19-20` (named r55–r57 verifier exit 1 → 0; language/numeric artifact-path failures) and the exact strings at `reports/round-1/baseline.txt:14,17-18` (`r47`, `r42`, `r55: artifact`). |
| M15 | `LOG.md:720`; `SCORECARD.md:135`; `MANIFEST.json:2782` | **ok** | `LOG.md:720` states the path-sensitive observation and the false universal `ev = f(content, path, params)`. `SCORECARD.md:135` still carries the unscoped “evidence_id confirmed path-sensitive (content+path+params)” claim (the mistake being recorded). `MANIFEST.json:2782` is the fleet-root kaidoku adjudication: the verifier family is path-sensitive, while analyze/inspect are content+params-keyed; the false universal was removed. |
| M16 | `corpus/lessons/round-1.md:15` | **ok** | Line 15 rejects counting the predecessor’s nine-member batch, a validated/rendered plan, or a live interactive process as a verified completed round. |
| M17 | fleet repo `.ufo/waves/kaika-w1/revenger-art.md:22,45` at `5b471e4` | **line-off** | Line 22 says “Tier A: **25**”; line 45 says “Only catalog/abstract pages were read, not the full standards.” The denominator is line 21 (“Sources opened and listed: **25**”), so the 25/25 claim needs `:21-22,45`. See finding F4: the count is asserted but not reproducible from this blob. |
| M18 | `corpus/knowledge/seed.md:1-3`; `corpus/knowledge/2026-10-12-rea-readiness-checklist.md:1-3` | **ok** | Both openings are title/blank/heading; `grep` finds no `source:`, `verified-at:` or `recheck:` in either file. The knowledge directory contains exactly 2 entries (`ls`), matching “2/2”. |
| M19 | `corpus/knowledge/2026-10-12-rea-readiness-checklist.md:8-13`; “re-probe in this file's `## Gate — kaika continuation`” | **wrong** | Checklist lines 8-12 cover `rea` absent, node/npm, MCP not registered, ghidra/ida absent, jadx/binwalk/unblob absent; line 13 is archive tools. The cited range does **not** contain the REA skill version/tool count, which is `corpus/knowledge/seed.md:5` (“version 37, tool_count 170 declared”). The second pointer is dangling: `round-1.md` has only `## Gate` at line 12 (`grep -n "^## Gate"`), and lines 12-19 contain Gate candidates, no re-probe. Corrected evidence: `checklist:8-12` + `seed.md:5`; no re-probe section exists at audit time, and “went stale” is not shown — only the 2026-10-12 probe date is. |

## Q rows — verdicts

All ten Q rows cite existing M rows, and every cited M row’s `captured-by` cites that Q back. The `lesson` citations are substantively apt; notes mark policy text that extends the cited M row rather than being directly evidenced by it.

| id / line | `lesson` column | verdict | motivation check |
|---|---|---|---|
| Q01 / `QUALITY.md:13` | M17 | **ok** | M17 is the abstract-tiered-A class; Q01’s “tier A for that claim’s scope” is exactly M17. Notes: the “opened in the round that wrote it” and “tier-C never sole support” clauses extend M17; and `corpus/SOURCES.md`, the criterion’s operational referent, is absent (finding F5). |
| Q02 / `:14` | M18 | **ok** | M18’s class is the missing `source:`/`verified-at:`/`recheck:` headers; M18’s fix also names the coverage-map row that Q02 requires. `corpus/README.md` exists (untracked). |
| Q03 / `:15` | M06, M14 | **ok** | M06 = copied saved `entry_locations`; M14 = saved path used as both identity and locator. Both directly motivate independent derivation. |
| Q04 / `:16` | M02 | **ok** | M02 = manual reading vs the tool’s explicit 0/1 output; Q04 scores the tool’s own output and labels manual work. |
| Q05 / `:17` | M01, M19 | **ok** | M01 = readiness/acquisition conflated with capability; M19 = unrechecked old probes. Q05 requires a real-surface probe with command/date/exit or Evidence ID. |
| Q06 / `:18` | M04, M05 | **ok** | M04 = stale copied operand after a byte shift; M05 = wrong construction constant/count. Q06 requires byte verification and retention of failed inputs. |
| Q07 / `:19` | M07, M12 | **ok** | M07 = falsified refusal prediction; M12 = unreproduced refusal cause. Q07 requires pre-registered hypotheses and independent reproduction of causes. |
| Q08 / `:20` | M08, M09, M10 | **ok** | M08 = count/command and non-author supersession; M09 = identifier checked against the request; M10 = offset role from the decoded structure. Q08 maps one clause to each. |
| Q09 / `:21` | M11, M13 | **ok** | M11 = digest binds only the bytes hashed / byte-preserve saved records; M13 = receipt hashes and Evidence IDs do not prove producer origin or readiness. Q09 states both. |
| Q10 / `:22` | M15 | **ok** | M15 is the family-scoped evidence-ID correction adjudicated by kaidoku; Q10 requires family/operation/version/input scope and reporting contested cross-lane scope. |

## Summary counts (with commands)

M-row count and `captured-by` split, exactly the command on `round-1.md:58`:

```sh
$ awk -F'|' '/^\| M[0-9]+ /{n++; if ($5 ~ /none/) z++} END{print n, n-z, z}' corpus/lessons/round-1.md
19 17 2
```

The file’s line 58 says “Classes 19; captured by a criterion 17; `none` 2”. The command reproduces it; exit 0. The `none` rows are M03 and M16, both with the stated process-rule reason.

IDs are contiguous `M01`–`M19`:

```sh
$ awk -F'|' '/^\| M[0-9]+ /{gsub(/ /,"",$2); print $2}' corpus/lessons/round-1.md | tr '\n' ' '
M01 M02 M03 M04 M05 M06 M07 M08 M09 M10 M11 M12 M13 M14 M15 M16 M17 M18 M19
```

Q-row count:

```sh
$ grep -c '^| Q[0-9][0-9] ' corpus/QUALITY.md
10
```

Bidirectional citation check (17 M rows carry a Q; every Q `lesson` resolves; zero missing back-citations):

```sh
$ python3 - <<'PY'
import re, pathlib
L = pathlib.Path('corpus/lessons/round-1.md').read_text()
Q = pathlib.Path('corpus/QUALITY.md').read_text()
m = {x[0]: x[3] for x in ([c.strip() for c in l.strip('|').split('|')]
     for l in L.splitlines() if re.match(r'\| M\d\d \|', l))}
q = {x[0]: x[3] for x in ([c.strip() for c in l.strip('|').split('|')]
     for l in Q.splitlines() if re.match(r'\| Q\d\d \|', l))}
print('M rows', len(m), 'Q rows', len(q))
print('M->Q', sum(1 for v in m.values() for x in re.findall(r'Q\d\d', v)))
for qid, les in q.items():
    for mid in re.findall(r'M\d\d', les):
        assert mid in m, (qid, mid)
        assert qid in m[mid], (qid, mid)
print('unresolved/back-citation mismatches', 0)
PY
M rows 19 Q rows 10
M->Q 17
unresolved/back-citation mismatches 0
```

Verdict tally (analyst column, not a command): **15 ok, 2 line-off (M14, M17), 2 wrong (M07, M19)**.

M17 count reproducibility check against the cited blob:

```sh
$ git -C /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-ledger show 5b471e4:.ufo/waves/kaika-w1/revenger-art.md | grep -cE '^\| S[0-9]{3} '
0
$ git -C /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-ledger show 5b471e4:.ufo/waves/kaika-w1/revenger-art.md | awk -F'|' '/^\| S[0-9]{3} / {gsub(/ /,"",$5); n[$5]++} END {print n["A"]+0}'
0
```

M07 pointer file length:

```sh
$ wc -l reports/round-59/r59d-adjudicator.md
24 reports/round-59/r59d-adjudicator.md
```

## Findings

- **F1 — M07 second pointer is wrong, not merely offset.** `reports/round-59/r59d-adjudicator.md` has 24 lines, so `:27-28` is out of range; its subject is r60/devin, not the r59 unpaired-surrogate refusal. Use `corpus/live/runs/round-59/reviewer.md:5,7`, which states “Declared calibration claim unmet” and records the accepted `A=\ude00B!`.
- **F2 — M14 range is incomplete.** `SCORECARD.md:20-21` names only the language/numeric multi-image artifact-path failures (r42/r47) and then the coverage-F taxonomy; the named r55 failure is `SCORECARD.md:9` (exit 1 → 0) and the exact `r55: artifact` string is `reports/round-1/baseline.txt:18`. Corrected pointer: `SCORECARD.md:9,19-20` + `reports/round-1/baseline.txt:14,17-18`.
- **F3 — M19 has a dangling section pointer and a missing fact.** `corpus/lessons/round-1.md` has `## Gate` at line 12, not `## Gate — kaika continuation`; lines 12-19 are Gate candidates and contain no re-probe. The REA skill version/tool count is not in `checklist:8-13`; it is `corpus/knowledge/seed.md:5`. The “went stale” outcome is unobserved at audit time — only the 2026-10-12 probe date is shown.
- **F4 — M17’s 25/25 is asserted, not reproducible.** Lines 21-22 state 25 sources and 25 tier-A; line 45 supports the ISO-abstract limitation. But the cited blob contains no `| S### |` rows: the same `grep -cE` at line 21 returns 0, and the tier `awk` returns 0. `revenger-state.md` has no source table either. The pointer is line-off for the denominator (`:21-22,45`), but the count itself is `[UNVERIFIED]`; if the registry exists elsewhere, cite it.
- **F5 — Q01’s operational referent is absent.** `QUALITY.md:7` and Q01 rely on `corpus/SOURCES.md`; it is absent in the worktree and at base `8bbcb4e` (`git cat-file -e` fails). This is a C2 dependency, not a lesson-citation defect; Q01’s M17 citation is still apt.
- **F6 — M01/M02/M03 class wording describes the near-miss, not an observed event.** The cited lines record the honest-stop boundary: claim unmet / no native session (M01), manual difference labeled separately (M02), nonretryable/halt (M03). No line records readiness taken as a pass, a manual result offered as the tool’s claim, or an identical retry. Treat these as lessons; no line correction is implied.
- **F7 — Q↔M mapping is clean.** All ten Q lessons resolve to existing M rows; all 17 M rows with a Q are cited back; M03/M16 are the only `none` rows. Q01’s “opened in the round” and “tier-C” clauses and Q02’s coverage-map clause are extensions carried by the M rows’ fix text, not by their class/evidence text.

## Gates

| gate | result | basis |
|---|---|---|
| count line `19 17 2` | **pass** | exact command above; matches `round-1.md:58` |
| IDs contiguous M01–M19 | **pass** | ID command above |
| every M pointer resolves | **fail** | M07, M19 dangling/wrong; M14, M17 incomplete |
| Q lessons motivate and back-cite | **pass** | 17/17, 0 mismatches |
| M17 count reproducible | **fail** | 0 source rows in cited blob |
| Q01 referent present | **blocked** | `corpus/SOURCES.md` absent (C2 dependency) |

## Touched surfaces / out of scope

- Written: only `.ufo/waves/kaika-r1/scribe-pointer-audit.md`.
- Not done: no edit to `corpus/lessons/round-1.md`, `corpus/QUALITY.md`, fixtures, saved records, or `SCORECARD.md`; no fix of the pointers; no C2 `SOURCES.md` creation; no C3 live re-probe; no REA producer or live-target execution; no install, commit, push, or sibling-lane write.

## Artifact paths

- Report: `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/revenger-shokunin/.ufo/waves/kaika-r1/scribe-pointer-audit.md`
- Audited: `corpus/lessons/round-1.md`; `corpus/QUALITY.md`; `LOG.md`; `SCORECARD.md`; `corpus/knowledge/seed.md`; `corpus/knowledge/2026-10-12-rea-readiness-checklist.md`; `corpus/lessons/2026-10-12-r1-provider-gap.md`; `reports/round-59/r59d-adjudicator.md`; `corpus/live/runs/round-59/reviewer.md`; `reports/round-1/baseline.txt`; fleet-root `MANIFEST.json`; fleet-repo `.ufo/waves/kaika-w1/revenger-art.md` at `5b471e4`.
