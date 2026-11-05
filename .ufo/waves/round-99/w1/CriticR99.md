# CriticR99 findings: round 99 wave w1

Lane: revenger, round 99 attempt 1. Frozen claims at 7e6edd4; amended candidate audited at 9ddd38ac (Amendment B, digest `246d09a8cf6523ab380f88f7945f220338c27e31f8b43ba876bbd0a9a8d746da`). Scratch deleted before yield; receipts copied under `.ufo/waves/round-99/w1/CriticR99/`.

## 1. Critic audit and vote on the C14 candidate

- Audit: `.ufo/waves/round-99/w1/CriticR99/critic-audit-246d09a8.md`, sha256 `f8945bfbf52e97c088c42e06e1e271544a440ae83b06463fc90b9567c8fe3a97`.
- Vote: `reports/round-99/votes/CriticR99.json`, `candidate_sha256` = 246d09a8…, `artifact_sha256` = f8945bfb…. Self-checked with a scratch script that mirrors the v7 vote rules (strict JSON, key set, notes vocabulary, PASS-note distinctness across all votes in the directory, artifact sha, seat and digest named in the artifact). Result: `ALL_OK True`, `dup PASS notes: []`.
- Decisions: PASS on Q01–Q06, Q09–Q11, Q14–Q16; n/a on Q07, Q08, Q12, Q13, Q17 (each note names its Q id). No FAIL decision. C1_VOTES is not failed by this seat on the current bytes.
- Mechanised derivation check: `.ufo/waves/round-99/w1/CriticR99/verify_amend_b.py` run from a `git archive 9ddd38ac` extract. Output (`verify_amend_b.log`): `ROWS 29`, every row `EXACT`, `BAD_ROWS 0`, last line `rc=0`. The one row that exits 1 (`doctor binwalk or unblob checks`, grep on zero matches) is annotated in the entry itself.
- Lint on the extract: `corpus/lint_entry.py --entry corpus/knowledge/round-98-rea-host-readiness.md --lane .` prints `LINT_QMAP=0 LINT_Q14=0 LINT_Q15=0 LINT_HEADER=0`; the lint's own exit code was not captured (the run was piped to `tail`), so the printed zero counts are the evidence.
- Composition checks: 13 failing scope checks = 3 missing engines + 9 registration states (8 missing, 1 stale) + `skill:identity`. Version strings in the transcript (6.7.0, 1.5.6, 21.0.13, 3.1.0, 26.6.4) each followed by `rc=0`; 12.1.4 credited to the doctor record. Quotes: S506 lines 22, 26, 34 match; receipt span `[7126:7202]` equals the quote; body sha and length match.
- Defects found on 36cc6ac2 and sent to RevengerR99 before Amendment B (all in the amendment; verified fixed on 9ddd38ac):
  1. "scope-check classes" stdout carried `classification: ` prefixes; recorded output omitted them (Q16).
  2. S507 SOURCES `teaches` cell said the doctor record contains "exit 1"; the record has 0 lines with "exit" (Q16 / registry).
  3. "ghidra … 8 of 8" denominator not printed by its row (now a separate row).
  4. `inventory_artifact` status row not tied to the substep operation (now `grep -A1 'operation: inventory_artifact'`).
  5. Member labels and root digest not derived by any row (now rows).
  6. Causal "because the headless launcher is not on PATH" stated as observation (removed).
- Minor, non-blocking, not fixed: the S506 SOURCES anchor says "body bytes 7126-7202" without a base convention (receipt uses 0-based half-open). `reports/round-99/controls/deriv_check.py` and `amendB-deriv-check.log` were added after the claims-freeze commit; no counter depends on them.
- Verified, not defects: the K05 correction is accurate (checklist line 40 sits under `## Re-verification 2026-10-19`, which records `pwntools import fails`); the S506 quote is a verbatim line (line 34) and a verbatim substring at lines 22 and 26.

## 2. Fresh round-99 holdout builder (run on frozen v7 only)

- Builder: `.ufo/waves/round-99/w1/CriticR99/fresh/build_fresh99.py`. Args `--counter --profile {c02,c14} --work --lane [--rev] [--build-only]`; honours TMPDIR and `--work`; never writes into the lane tree.
- Counter run: `reports/round-98/c1_k_admit_counter7.py` only. No v8 bytes were touched or run.
- Commands and exit codes: `python3 -B build_fresh99.py --counter <v7> --profile c02 --work <scratch>/run/c02 --lane <lane>` → rc 0; same with `--profile c14` → rc 0.
- Results (copies in `fresh/`: `holdout99-c02-v7.log`, `holdout99-c14-v7.log`, `results-c02.json`, `results-c14.json`, `MANIFEST-c02.sha256`, `MANIFEST-c14.sha256`, `v7-counter-logs/`):

| profile | honest control | vectors accepted by v7 | summary line |
|---|---|---|---|
| c02 (v6 fixture tree) | control-ok, K=13/15 | 6/6 | `HOLDOUT99 accepted=6/6` |
| c14 (9ddd38ac + landing edits) | control-ok, K=14/15 | 6/6 | `HOLDOUT99 accepted=6/6` |

- The c14 trees carry C14 held. They are development fixtures (synthetic votes, registry and artifacts; disclosed) run under frozen v7, which the seat spec allows. No landing tree was built or scored.
- The 12 new classes, none of them among the r96/r97/r98 classes I could identify:
  - c02: N1 one-token PASS note (the c02 profile does not read PASS notes); N2 pinned reviewer vote deleted, two remain; N3 entry Q-map claims PASS where every vote is n/a (votes re-bound); N4 Evidence ID in a derivation row replaced; N5 observation/inference/unknown and limitations sections cut (votes re-bound); N6 README C02 surface text asserts a replication no vote records.
  - c14: N1 one reviewer marks ten PASS decisions n/a with Q-id reasons (Q09 kept PASS); N2 another seat's audit renamed into this seat's artifact path; N3 derivation count output 14 → 15, no digest row touched; N4 saved doctor record gains an appended rerun line with its prefix re-derived; N5 pinned S506 body replaced by a self-consistent body (receipt, fetch log, digest and length rows re-derived); N6 S507 anchor re-pointed to a true record line that does not carry the claim.
- Structural limits, stated so the L1 does not read 0/12 as attainable by a tree-only counter: c14 N2, N4 and N5 change only bytes that a tree-only counter cannot pin (a renamed artifact has the same structure as the synthetic honest artifacts; a re-hashed record or source body is self-consistent unless a digest is pinned outside the tree). c02's fixture bodies and notes are themselves synthetic, so fabricated-source classes cannot be separated from honest on that profile and were not used.

## 3. Open questions for the L1

1. **The c02 honest fixture needs the committed round-96 record.** The v6 maker's freeze (2875b9c9) has no `corpus/live/runs/round-96/`. My first c02 run therefore failed the honest control on `C1_OWNWORK_PATHS` (log showed `S504:missing/empty corpus/live/runs/round-96/`). The builder now copies that committed directory from the lane rev (never invented), mirroring v7's own `_fixture_c02` supplement, and the control then passes. The r98 c2 receipt (`c2-do-nothing-v7-holdout98-c02.log`, CONTROL-honest K=13/15 pass) was produced with the same v6 maker, so the r98 honest tree must have carried those record bytes by some route I could not reproduce from the frozen maker. The C2 baseline (9/12) should be checked against the r98 honest tree before the v8 run is scored.
2. The fresh holdout (12 vectors) is now recorded under v7 only. It is for the L1's single run against the frozen v8, reported separately from the development set.

## 4. Tools

None installed or updated. Used system `python3`, `git` (read-only: `archive`, `rev-parse`, `ls-tree`, `log`), `tar`, `sha256sum`, `awk`, `sed`, `grep`. No pacman, no ~/.local/bin writes.

## 5. Process notes

- Vector list lives in `build_fresh99.py` inside this seat's wave directory. Not shared with ExecCounterV8 or MutationR99 by message; the file is readable on disk, so the L1 should keep it out of those seats' inputs if they read this directory.
- No messages sent to any seat other than RevengerR99. No task or subagent spawned. No files written outside the paths the seat spec names, and nothing committed, staged or reset.
- Scratch `/fast/scratch/hyaku/revenger-r99/CriticR99/` deleted (receipts above copied first).
