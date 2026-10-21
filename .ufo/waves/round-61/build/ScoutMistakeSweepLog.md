# Scout — mistake sweep for round 61 (read-only, 2026-10-21)

Scope: mine candidate mistake classes **not** already in `corpus/lessons/round-1.md` M01–M20, from `LOG.md:720-791`, `.ufo/waves/kaika-r1/` (15 files), `corpus/lessons/round-1-verifier-spotcheck.md`, and fleet `.ufo/waves/hyaku/jj-w1/reports/JjAuditRevenger.md`. Lane base `cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97`. Read-only: no lane/jj/git mutation, no REA producer call, no bytecode execution, no target probe, no installs. Evidence below is observed unless marked `[INFERENCE]`; the row's own falsifier outcome is marked where I did not run it.

## Sweep commands run (observed)

- Regex sweep `surviv|vacuous|untracked|discard|not attributable|mislabel|wrong|stale|contradict|initially|no control|invisible` over `.ufo/waves/kaika-r1`, the spotcheck, and `JjAuditRevenger.md` → 40+ hits, all triaged below; no hit was left uncited.
- `grep -nE 'vacuous|seven-family|eight-family|L2 22/22|substitutes the saved' LOG.md` → `:700,:736,:772,:784`.
- `grep -cE '^\| .*\| killed \|$'` / `survived` on `mutation-post.md` → `10` / `2`; `grep -cE '^\| [LM]-[A-Z][0-9]+ '` and `… killed \|$` on `mutation-post-l2.md` → `22` / `22`.
- `wc -l reports/round-59/r59d-adjudicator.md` → `24`; `git cat-file -e 5b471e4^{commit}` → does not resolve; same for `f27b5f1`.
- `git ls-files | awk -F/ '{print $1}' | sort | uniq -c` → `466 corpus`, `27 .ufo`, `26 reports`, 5 root docs; no `tools`, `scripts`, `verifiers`.
- `grep -cE 'argv|argparse'` on `corpus/verify_icon_languages.py` and `verify_multi_icon_states.py` → `0`, `0` (only `if __name__=='__main__': main()` at `:165`).
- Freshness rows: `grep -cE '^\| F[0-9]+ ' corpus/knowledge/seed.md` → `12`; `'^\| K[0-9]+ '` on the checklist → `6`.
- `TZ=America/Sao_Paulo date -d '2026-10-19 00:00:00' +%s` = `1792378800`; `TZ=UTC …` = `1792368000`; delta `3` h.
- `git cat-file -e HEAD:.ufo/waves/kaika-r1/scout-freshness.md` → rc `0` now (the reviewer's `:119` untracked observation is historical).

## Candidates

| id | class | evidence (path:line) | captured-by | proposed fix / how it can be shown to fail |
|---|---|---|---|---|
| N01 | self-test blind spot: an in-script check with no in-script falsifier, so deleting the check leaves the script green | `.ufo/waves/kaika-r1/mutation-post.md:15,21,30-33`; before-state `reports/round-61/measure-before.log:6,9` (`b exit=0 pass`) | none (propose Q12) | every check carries an in-memory forged input in the same run; kill measured by the script's own exit. Falsifier: delete `receipt['command']==…` → exit 0 today (observed); with the control, nonzero expected (the round-61 C2 prediction, not yet observed) |
| N02 | rejection control accepts any `AssertionError`, so an unrelated fault is printed as REJECTED | `.ufo/waves/kaika-r1/reviewer-oracle.md:52-53,63`; `.ufo/waves/kaika-r1/reviewer-post.md:118` | none (propose Q12) | match the expected finding message inside `except`. Falsifier `[INFERENCE]`: raise an unrelated assert before the intended field compare in the forged branch → still `REJECTED`/exit 0 today; message-matched form exits nonzero |
| N03 | unattributed falsification: a kill or absence claimed without isolating the cause | `mutation-post-l2.md:67` (plain path rewrite also trips `stdout_sha256`; only the rehashed probe isolates); `reviewer-post.md:68` (the no-HIST control failed on a string compare, not on an `open` event, and was discarded) | none (propose Q13) | record the isolation control with every kill/absence; a failure in another channel is inconclusive. Falsifier: plain probe kills pristine and L-C4 alike; rehashed probe gives pristine 1 / L-C4 0 — only that attributes the kill |
| N04 | kill ratios from non-identical mutant sets/detectors quoted side by side | `LOG.md:772` (`L2 22/22`; `L1 10/12`); same mutant, opposite verdicts: `mutation-post.md:15` survived vs `mutation-post-l2.md:38` killed via probe | Q08 partial (count command, not comparability) | one canonical table keyed (file, mutant) with detector and probe; ratios never merged. Falsifier: mutant b is exit 0 on its own run and exit 1 on the external probe; a merged 32/34 is undefined |
| N05 | landing/cleanliness evidence reads `HEAD`/index in a jj-colocated repo | `JjAuditRevenger.md:87-88` (class-A `HEAD` idioms in `reports/round-1/scribe.md:42`, `LOG.md:318`), `:164-173` (`HEAD` 997e954 vs `main` 3b2a998, clean status), `:221-223` (risks 1 and 3) | none (propose Q16) | explicit refs (`git cat-file -e <h>^{commit}`, `merge-base --is-ancestor <h> refs/heads/main`) + `jj status/diff`; cite only the helper's `pushed` hash. Falsifier: sandbox shows `git status --porcelain \| wc -l` = 0 while `cat-file -e HEAD:…` yes and `main:…` no |
| N06 | cited pointer (path, line range, commit) not resolved before publication | `scribe-pointer-audit.md:20,32,100,120-124` (M07/M19 wrong, M14/M17 incomplete: 15 ok/2 line-off/2 wrong); `JjAuditRevenger.md:90` (two hashes absent); `reviewer-post.md:119` (untracked cited path) | none (propose Q14) | resolver gate over every pointer at the landing commit; full hashes only. Falsifier: `wc -l` = 24 < cited `:27-28`; both hashes do not resolve; the cited wave path was untracked at gate time |
| N07 | proxy population changed between measurements, so the score is recomputed on a different denominator | `LOG.md:736`; `SCORECARD.md:9,19-22` (`inherited 3/7 = 4.29`); `reports/round-1/counting-commands.json:5` (8-family dict) | Q08 partial | pin the member list inline with its derivation; record old→new list. Falsifier: the same saved records score `3/7 = 4.29` or `4/8 = 5.0`; only the family list differs |
| N08 | duplicate assertions counted as distinct facts | `seed.md:56-67` (12 F rows) + checklist `:36-41` (6 K rows); `reviewer-post.md:10,106`; `spotcheck.md:17` ("18 stored assertions") | Q08 partial | unique fact key plus a dedupe map; count distinct. Falsifier: K01–K05 reuse seed probes F04/F06/F07/F08/F09–F12 → 13 distinct, not 18 |
| N09 | two probes of one fact reached opposite verdicts; the later verdict was silently adopted | `scout-freshness.md:12` (F03 STALE) vs `seed.md:58` and `reviewer-post.md:89` (F03 holds); unresolved debt named at `spotcheck.md:17` | none (propose Q15) | record the conflict, run a third probe or exclude the row from the tally. Falsifier: F03 counts as `holds` in the 18-row tally while the scout's tally counts it STALE (5/8 of 13) |
| N10 | score-bearing prose not cut over with the landing | `reviewer-post.md:110-114`; `SCORECARD.md:9` (says 5.0), `:19` (says both verifiers still fail), `:63` | none (propose Q16) | landing runs a grep of every doc-quoted score against the command output. Falsifier: command C prints 10.0 while `:9` says 5.0 and `:19-20` says the failures remain |
| N11 | documented mode flag ignored by the tool | `exec-lang-ledger.md:34`; `exec-multi-ledger.md:31`; static `argv\|argparse` = 0 in both verifiers | Q04 partial | gate asserts the invoked mode exists (or drops the flag) and probes an unknown flag for nonzero exit. Falsifier: plain and `--self-test` produce identical exit/output (exec rows A1/A2 and 3/4); with no argv read, any flag is ignored `[INFERENCE]` |
| N12 | lesson row written as an observed event when the cited lines record only a near-miss | `scribe-pointer-audit.md:125` (F6); rows `round-1.md:38-40` (M01–M03) | none (propose Q17) | label occurrence vs pre-adopted rule, as the M03/M16 `none` rows do. Falsifier: cited `LOG.md:26-30` records the claim unmet, not readiness accepted; no cited line records a retry |
| N13 | timezone-naive validator date compare, plus a vacuous `ok` when the parser fails | `LOG.md:784`; current fix `scripts/sources-census.sh:90` (`date -u +%F`), `:160-161` (UTC-in-Sao-Paulo selftest) | none (propose Q16) | one UTC clock; fail closed on parse error; print counted findings. Falsifier: local-midnight epoch 1792378800 vs UTC 1792368000 flips a same-day row to E08; a gawk parse error must exit nonzero, not print ok |
| N14 | dispatch brief assumed artifacts absent from the lane | `JjAuditRevenger.md:33-40` (`ls -d tools scripts verifiers` → 3 errors; no `SKILL.md`); inventory command above | none (dispatch process, like M03/M16) | derive the scope file list from `git ls-files`; a zero-hit declared path is a brief defect. Falsifier: `ls -d tools scripts verifiers` fails; the first-level inventory has only corpus/.ufo/reports/root docs |

## Considered, not added (already captured or honest)

- L1 mutation seat death and L1 running the probe author-side: transparently labeled (`mutation-post.md:3-6`); the substantive debt is N01, not a new class.
- `duration_seconds` hazard: predicted (`reviewer-oracle.md:139`) and avoided (`:84`); a near-miss with no defect.
- M07/M19 pointer errors and M17's unreproducible count: already M07/M17/M19; only the general pointer-resolution class (N06) is new.
- Universal `f(content, path, params)`: already M15.

## Reading and gaps

- 14 candidates, none duplicating M01–M20: 13 lane-side, 1 dispatch-side. Suggested criteria: Q12 (N01,N02,N11), Q13 (N03), Q14 (N06), Q15 (N04,N08,N09), Q16 (N05,N10,N13), Q17 (N12); N07 needs a population-pinning clause in Q08/Q11; N14 stays process.
- Observed falsifier outcomes: N01 (exit 0 today), N04 (10/2 vs 22/22), N05 (sandbox), N06 (24 lines; both hashes absent), N07 (3/7 vs 4/8 text), N08 (12+6 rows), N11 (static 0 argv), N13 (3 h delta). The rest are `[INFERENCE]` from the cited code/text and are marked in-row.
- Gap: this report does not judge round-61 C1/C2, does not reopen the sources, and does not add any class to `corpus/lessons/round-1.md`; admission is L1's.

VERDICT: 14 new candidate mistake classes mined and grounded (13 lane-side, 1 dispatch-side); strongest calibration value N01 (already round-61 C2's target), N03, N04, N06.
Installs: none.
