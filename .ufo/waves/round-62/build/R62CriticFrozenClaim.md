RESULT: COMPLETE

# R62CriticFrozenClaim — attack on frozen `reports/round-62/claims.md` (C1)

Revision: `a3498e25ad87bf756288812d0ea7c474b09433c7` (lane HEAD; archive at `/fast/scratch/hyaku/revenger-r62/R62CriticFrozenClaim/tree`). Corpus tree `cb7677ab…` is identical at base `5bd4a90` and at the frozen commit (`git rev-parse <rev>:corpus`). Neither candidate entry exists yet (`ls corpus/knowledge/` has no `round-62-*`), so this attacks the contract, the probe and the reserved sources. README stays uncovered. Nothing is admitted or credited.

## Counterexample: the K probe cannot tell an admission from a flip of the README text
Script `…/R62CriticFrozenClaim/k_counterexamples.py` (sha256 `e17e0fce…`) runs frozen `measure.py` lines 1–34 **unchanged** against edited README copies in scratch. Output `k_counterexamples.out` (sha256 `20f8518b…`):
```text
A_frozen:                               K_HELD=4/14 | C04 uncovered | C09 uncovered | K_HELD_BACKED=4/14
B_C04_held_old_rejected_file:           K_HELD=5/14 | C04 held                       | K_HELD_BACKED=5/14
C_C04_held_new_file_marked_rejected:    K_HELD=5/14 | C04 held                       | K_HELD_BACKED=5/14
D_nontarget_C02_held:                   K_HELD=5/14 | C04/C09 uncovered              | K_HELD_BACKED=5/14
E_C04_held_new_file_absent:             K_HELD=5/14 | C04 held                       | K_HELD_BACKED=4/14
F_C09_held_dash_col3:                   K_HELD=5/14 | C09 held                       | K_HELD_BACKED=4/14
G_C04_held_new_plus_C01_demoted:        K_HELD=4/14 | C04 held                       | K_HELD_BACKED=4/14
H_added_row_C15_held:                   K_HELD=5/15 |                                | K_HELD_BACKED=5/15
```
Impacted axes: coverage (false 5/14) and discernment. B shows that the retained rejected file (`admission-status: rejected`, `commonjs-destructured-require-edges.md:5`) still backs a held row. C shows that a new file carrying a reject marker counts. D shows a non-target flip reaching 5/14. G shows a real admission hidden by a lost held row.

## Blockers to fix before implementation or gating (each with the smallest safe correction)
1. **Which number is K.** `claims.md:12-13` says "K to at least 5/14", but the probe prints both `K_HELD` and `K_HELD_BACKED`, and cases E and F diverge (5 versus 4). Fix: K counts only when `K_HELD_BACKED == K_HELD ≥ 5`.
2. **Existence-only metric** (B, C, D, G; `claims.md:41-44`; `measure.py:32-34`). Fix: the final record adds three outputs. (a) A 14-row status diff from base to final in which only C04/C09 change. (b) Column 3 of each flipped row names only its `round-62-*.md` file, and the old rejected file stays in column 4. (c) The named file has no `admission-status: rejected` line, and the lesson `## Gate` has a per-file admit row checking all of Q01–Q13.
3. **HOLDS_OK leaves out the attributed b kills** (`measure.py:111`: controls, d2, calibration, replay; `attributed_b` is absent). `claims.md:57-59` requires attributed kills at 2/2. Fix: read `C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2` as its own line. Treat a probe exit of 1, or 2 (could-not-evaluate, `measure.py:8,113`), as no admission (C1 falsified), never as indeterminate.
4. **The HOLD_REPLAY denominator is a glob** (`measure.py:99,110`). It finds 10 `corpus/verify_*.py` files at the frozen commit. Any new verifier turns the frozen 10/10 into 11/x, and H shows that row denominators drift the same way. Fix: candidates add no `corpus/verify_*.py` and no README row. Their recheck is the in-entry stdlib block.
5. **Probe identity and scratch location.** `measure-before.log:2` ran the live-path probe, not the archived one. Live and frozen `measure.py` currently share sha256 `ada7a9c9…bdd0b50d2`, so the after-log must record that hash. `tempfile` resolves to `/tmp` here (`TMPDIR` is unset; `gettempdir()` printed `/tmp`; `measure.py:67`). This conflicts with `claims.md:40`. Fix: run the after-measurement with `TMPDIR=/fast/scratch/hyaku/revenger-r62/<seat>/tmp` and record it. [INFERENCE] The before-run's mutant copies went to `/tmp`, because the log does not record `TMPDIR`.
6. **The independence of the Gate is not defined** (`claims.md:42-44`). L1 is planner and sole integrator, and also writes the source rows and the lesson. Precedent: the round-61 Gate admitted C09 on "Reproduce re-run by L1, output identical" (`lessons/round-61.md:77`), and the outside closure overturned it (`round-61-verifier-spotcheck.md:144-145`). Fix: the seat that records each Gate decision is neither the entry author nor the corrector, and its ID is logged. The Q11 decision cites a per-value inventory (every count, offset, digest and identifier mapped to an output line or to a `recorded` label), never output equality.
7. **The post-falsify correction route contradicts the wave cap** (`claims.md:47-50` against `:73`, which allows two waves and no replacements). A re-reviewer spawned after the falsify wave would be a third dispatch. Fix: the re-review reuses a seat already in the falsify wave, woken by message. The sha256 of the admitted bytes equals that of the bytes the wave attacked, or the re-review names the hash of the diff between them.
8. **One admit out of two proposals** (`claims.md:12-14`). Passing with one of two is pre-registered, so it is not a loophole. However, "6/14 if both" is accounting, not a second target. Fix: the report states admitted/proposed (for example 1/2) and the failing Q IDs of the rejected candidate. It never calls 5/14 "C04+C09" progress or two claims.
9. **Narrower wording than Q11** (`claims.md:30`, "value used in prose", against `QUALITY.md:23`, "each count, identifier, offset and digest in an entry"). Round 61 failed on a value stated in Limitations (`spotcheck:70-74`). Fix: Q11 covers headers, tables, Limitations, code comments, S-IDs, Evidence IDs and commit hashes.
10. **"At least one mined tier-A row supports each admission"** (`claims.md:33`) is weaker than Q01's "each load-bearing claim" (`QUALITY.md:13`). Q01 governs.
11. **Q11 could be weakened through supersession.** `QUALITY.md:5-6` supersedes by naming the replaced row, so a new row that names Q11 retires it. Fix: the new row names no replaced row. The Q11 row (line 23, sha256 `6a866579…0606756`) stays byte-identical. The new row lands before the falsify wave, so it is not a post-hoc goalpost.
12. **Duplicate authorities.** The reserved S028–S031 rows re-cover sources that already have rows, and every one of those rows lists the rejected entries as its citers (`SOURCES.md:30,36,40,41`): S016 (execution-specs v2.20.0, osaka vm), S022 (ECMA-262 draft), S026 (the seven saved EVM records) and S027 (the js-r3/js-r7-v2 graphs). Fix: each new row states its narrower scope and leaves the old row byte-unchanged, or the old→new change is logged (`claims.md:65-66`). Expect census W04 warnings for duplicate URLs, as with S024 (`measure-before.log:33`), and report them rather than hiding them. Cite one authority per scope.
13. **"Dispatch" is a role label with no tier-A source.** The truth files say "dispatch-like comparison only" (r19), "two dispatch-like branches" (r22) and "no dispatch syntax" (r23), found by grepping `truth.json`. S016's scope is opcode byte values, and S018 defines selectors from signatures, not a dispatcher layout. Fix: the entry records "dispatch-like" as the fixture author's label, marked recorded and not re-derived (Q08/Q11 role labels). It derives only byte boundaries from S028.
14. **Fixture count.** There are 7 EVM directories: `evm-r19`, `evm-r21` to `evm-r26`, with no `evm-r20` (`ls -d corpus/fixtures/evm-*`). The JS fixtures are `js-r3` and `js-r7-v2`. Fix: any "seven" in an entry needs its own in-entry `ls` and output.
15. **Tradeoff for the source seats, not a defect fix.** S029/S022 point to a moving draft at `tc39.es/ecma262`. A Gate quote needs a dated snapshot or a published edition so the quote can be reproduced.

## Preservation reference (sha256 at the frozen commit, for the final byte-identity check)
```text
690db9f17ac2e64b35efeb90392fae3401ae8e14c843a1ac4eac6f240ef2a6f3  corpus/knowledge/commonjs-destructured-require-edges.md
3e17b88fff8cfa1c98db72a212a134e1c56fcb8b84e75573a00041cc16969361  corpus/knowledge/evm-saved-interface-candidates.md
c83f2d29f7b0b72d5eb30c24d55aa6285128beda1b85fa7261cbc951444665d2  corpus/lessons/round-61-verifier-spotcheck.md
da59f8d93d873c3884c7b96a1ceefbd67d6691aab4154475c91b83844bdcce1f  corpus/lessons/round-61.md
428e903cfdbfae267b6e6faef0bf7e8ce0fbcb50ac5cef408eefa24fa9ee3c08  reports/round-61/claims.md
017f7fc7edb730cbcc2420b8b8d4c65609eaca88796d20d421b4abd54df45cbe  reports/round-61/measure-after.log
60cc3b639efdb81db8df4b4f14f9ca42b8a34ad81b731ba735ddd1960645840c  reports/round-61/measure-before.log
ada7a9c97bba394f6539ce6f158ee81a8c342a42fa861d634933226bdd0b50d2  reports/round-61/measure.py
git rev-parse a3498e2:corpus/live      -> a35d30717a00250b0e8a884fd5ae402674609bea
git rev-parse a3498e2:corpus/fixtures  -> c6287377454103866adea5b309850bf301279cc9
```
Command: `cd <archive> && sha256sum <paths>`, cwd = the archive.

## Unknowns
- Whether L1 intends the Gate seat to be L1 itself.
- Whether execution-specs v2.20.0 is still the tag the S028 seat opens (that seat's scope; not opened here).

Proposed changes: blockers 1–7 as admission-procedure text in the round-62 lesson or report, and blocker 13 as entry wording. Scratch artifacts: `k_counterexamples.py` and `.out`. No production edits.

Installs: none.
