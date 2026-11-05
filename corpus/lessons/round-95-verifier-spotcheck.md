author: hyaku closure (non-author integrator, @m_zfl)
round: 95 (revenger, lane_round 95)
checked-against: revenger-shokunin@00c4ac2b6774d9ce385e14bd92fffc4cfd217ccb
base: cb5c26f73c99af268bc71e9f7417bfd7e7738d83 · freeze: 6e0bf15fed58f357b7fa0c881371ac7616a116f7
report: .ufo/reports/round-95/revenger.md

# Round 95 — non-author verifier spot-check

Scope: step 1 conformance, step 2 claim re-check, step 3 discernment spot-check. Commands are run by the
integrator on committed bytes; the lane's own counter and battery were not executed (PROTOCOL §Gate standard,
Closure consequence). Status of each claim is marked **re-measured** (integrator ran a plain count) or
**evidence-verified** (integrator checked the committed evidence and its revision, did not re-execute).

## 1. Conformance (step 1)

| check | command | observed | result |
|---|---|---|---|
| report attribution | `git log --format='%an %H' -- .ufo/reports/round-95/revenger.md` | `revenger-shokunin 60495efbb520f0aaa0cd21565a6a5b0c0e3220e5` | pass (lane identity) |
| SHONEN heading | `grep -c '^## SHONEN' .ufo/reports/round-95/revenger.md` | 1; four `[~]` lines, no `[x]` | pass |
| cited commits are ancestors of branch | `git -C revenger-shokunin merge-base --is-ancestor <h> main` for cb5c26f, 6e0bf15, c0401d2, 00c4ac2 | all four exit 0 | pass |
| helper state | `scripts/hyaku/jj-lane.sh state …/revenger-shokunin` | `branch=main local=00c4ac2… remote=00c4ac2… ahead=0 behind=0 tracked=0 untracked=0`, rc 0 | pass |
| lane worktree | `git -C revenger-shokunin status --porcelain` | empty | pass |
| remote tip | `git -C revenger-shokunin ls-remote origin refs/heads/main` | `00c4ac2b6774d9ce385e14bd92fffc4cfd217ccb refs/heads/main` | pass |
| lane commit identity | `git log --format='%h %an <%ae>' cb5c26f..00c4ac2` | three commits, all `revenger-shokunin <revenger@shokunin.local>` | pass |
| prompt contract | `.ufo/prompts/revenger-round-95.md` §1–§5 vs `templates/round-prompt.md` | claims, frontier step, L2 floor, report contract, commit/push/L0 items present verbatim; §6 hyaku addendum | pass |
| dispatch digest | `.ufo/watchdog.log` (copied here, log is mutable) | `2026-11-05T13:58:31-03:00 launch revenger round=95 pgid=40092 driver=hyaku-inline attempt=1`; `2026-11-05T15:00:00-03:00 complete revenger round=95; hyaku-inline attempt=1` | termination evidence present |
| census (integrator duty) | `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger` | rc 0; `ok corpus/SOURCES.md`; W-codes only (W01 tierC rows with used-by; W04 duplicate URLs across scopes) | pass (warnings status-neutral) |

Status: `ok`. The report is real, its cited hashes exist and are ancestors of the branch, and the tree is clean and pushed.

Conformance defects (status-neutral, routed in §5): the lesson's `## Gate` calls lane-dispatched votes "non-author"; seat final texts were not retained after the orchestrator kernel restart (disclosed in the report; seat files are the evidence).

## 2. Claim re-check (step 2)

### C1 — coverage K (lowest non-retired axis) — **re-measured**

Command (plain awk over committed `corpus/README.md`, coverage-map rows `| C## |`, last cell = status):

    git show <rev>:corpus/README.md | awk -F'|' '/^\| *C[0-9]+ *\|/ {s=$(NF-1); gsub(/^ +| +$/,"",s); n[s]++; t++} END{printf "total=%d ", t; for(k in n) printf "%s=%d ", k, n[k]; print ""}'

- base `cb5c26f`: `total=15 partial=3 held=11 uncovered=1`
- head `00c4ac2`: `total=15 partial=2 held=12 uncovered=1`
- row diff: C10 `partial` → `held`; no other row changed status (C02 and C14 stay `partial`, C05 stays `uncovered`).
- C10 row cites `knowledge/round-95-evidence-ledger-discipline.md`; that file exists at head with `admission-status: admitted`. The superseded `knowledge/2026-10-29-rea-evidence-ledger-discipline.md` is `admission-status: rejected` at head.
- Score arithmetic: 11/15 = 7.3 → 12/15 = 8.0 (SCORECARD line 1843).
- Not re-run: the lane's "backed" test over the other 11 held rows. That leg rests on the committed counter log `reports/round-95/controls/c1v4-landing.log` (`C1_K_HELD_BACKED=12/15`, `C1_VERDICT=pass`) — evidence-verified only. The do-nothing control `c1v4-do-nothing.log` (`C1_K_HELD_BACKED=11/15`, `C1_C10_HELD=fail`, rc 1) agrees with my base count.

Harm check: `git diff --numstat cb5c26f 00c4ac2 -- SCORECARD.md` adds 35 lines, deletes 0; `git diff --stat cb5c26f 00c4ac2 -- PROVINCE.md corpus/QUALITY.md` is empty. No prior row was edited. **Verdict: improved.**

### C2 — calibration (counter reach over the eleven named vectors) — **evidence-verified**

Frozen bytes: `git diff --stat 6e0bf15 00c4ac2 -- reports/round-95/c1_k_admit_counter4.py reports/round-95/forge_battery4.py reports/round-95/claims.md reports/round-95/controls/` lists only `c1v4-landing.log` and `census-round-end.log` (both added after freeze). The counter, battery, and claims are byte-identical to the freeze commit.

Committed verdicts, read from the logs (not re-executed):

- `controls/battery4-full-at-freeze.log`: `V4_KILLS=10/10`, `MUTANT_V4_REGISTRY_KILLED=pass`, `POS_C1V4=pass`, `DO_NOTHING_C1V4=fail-as-required`, `HOLD_R94_BATTERY=pass`, `BATTERY4_VERDICT=pass`.
- `controls/battery4-red-v3.log`: `V3_REACH_NEW=10/10`, `MUTANT_V3_REGISTRY_SURVIVES=pass`, `RED_V3_VERDICT=pass`. The red stage shows the v3 counter kills none of the eleven named vectors.
- Wave reproductions `.ufo/waves/round-95/w1/ExecBattery/full.log` and `red-v3.log`: the verdict lines match the committed logs (compared by reading the printed text).

Scope limit: the eleven vectors are the lane's own forgeries. The measure is reach over the lane's own predicate. It does not show discrimination against forgeries the counter's author did not write. Routed in §5. **Verdict: improved** on the frozen predicate.

### Other axes

- depth, freshness, operability, adjacency: **unchanged**. No claim; SKILL.md gains two registry rows; no prior scorecard row changed; PROVINCE.md and corpus/QUALITY.md byte-unchanged.

Claims: both verify (C1 re-measured, C2 evidence-verified). No axis harmed. **Admission: true.**

## 3. Discernment spot-check (step 3)

Sources re-opened by the integrator on 2026-11-05 (`curl -sSL`, raw.githubusercontent at REA revision `12f6e0974cc0db0b3a9b86246accc76556837222`):

- S500 `src/domain/evidence.ts`: HTTP 200, 17010 B, sha256 `69fe22454e4dd4721aeba2c697dc8cf414f3be4630c3d41db491821f39465b8f` — equals the committed `reports/round-95/quote-receipts/raw/S500.body`.
- S501 `src/application/investigation/EvidenceLedger.ts`: HTTP 200, 18784 B, sha256 `f7add697322f37d7a7d69fde5e8e2c3d625344b67fb1ca32dc52dbe6bb103dac` — equals the committed `raw/S501.body`.

| # | item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|---|
| 1 | `knowledge/round-95-evidence-ledger-discipline.md` (C10 admitted) | admit | S500 + S501 bodies (above) | agree (sourcing only) | The two rows the entry cites for vocabulary and idempotent record/conflict rules are present in the re-opened bodies. I did not adjudicate the full Q01–Q17 map; that rests on the lint output and the lane-dispatched votes. |
| 2 | S500 row quote | admit (row) | `grep -n` on S500 body | agree | "Source authority vocabulary owned by Evidence and reused by its consumers." 11 words, verbatim at line 121. ≤25 words. |
| 3 | S501 row quote | admit (row) | `grep -n` on S501 body | agree | "Record evidence idempotently; conflicting content is rejected." 7 words, verbatim at line 58. ≤25 words. |
| 4 | a seventh C05 Android candidate | reject | `git diff cb5c26f 00c4ac2 -- corpus/SOURCES.md`: only S500/S501 added (REA schema, no APK/AXML); the six prior `knowledge/round-65…71-apk-axml-byte-evidence.md` all `admission-status: rejected` at head | agree | No new primary APK/AXML byte source was opened, so re-gating repeats a known failure. The stated reason holds. |
| 5 | re-admitting the 2026-10-29 C10 candidate in place | reject | `knowledge/2026-10-29-rea-evidence-ledger-discipline.md` at head: `admission-status: rejected`, bytes preserved | agree | The successor is a new file, as the CORPUS corrections rule requires. |
| 6 | round-94 correction C-r95-1 (S499 "13 words") | correction (not a gate call) | S499 quote from `corpus/lessons/round-94.md` line 36 | agree | "Setup previews configuration changes and asks for approval before applying them." = 11 words. The correction is right. |

Discernment sample: one admit, two rejects (items 1, 4, 5), all re-checked. The gate agreed with the outside check on every admit and every reject.

## 4. Per-axis and trend verdicts

Per-axis (claims and non-claims):

| axis | verdict | evidence |
|---|---|---|
| coverage | improved | §2 C1 (re-measured: held 11→12/15; C10 partial→held) |
| calibration | improved | §2 C2 (evidence-verified: 0 of 11 named vectors killed by v3 → 11 of 11 by v4, frozen predicate) |
| depth | unchanged | no claim; SKILL.md registry rows only |
| freshness | unchanged | no claim; SCORECARD r94 erratum re-grades to `unchanged` (append-only) |
| operability | unchanged | no claim; no harm observed |
| adjacency | unchanged | no claim; PROVINCE.md byte-unchanged |

Trends (LEARNING.md):

- **expansion: improved** — admitted entry moves C10 coverage from `partial` to `held`, citing two tier-A rows opened this round (S500, S501) and mined rows (S096–S109). Caveat: the ground is the same ground a rejected 2026-10-29 candidate held; the admission is a superseding successor, not new breadth.
- **quality: improved** — the 2026-10-29 candidate is superseded by a full entry (old file kept `rejected`, bytes preserved). The entry's recheck (re-open the two raw URLs, compare sha256) passes for S500 and S501 today. Scope: only the entry's two anchored rows and its provenance trio were re-checked here.
- **discernment: improved** — §3 items 1, 4, 5: the spot-check agrees with the gate on the admit and on both rejects.

## 5. Routed defects (lane-owned unless noted; for round 96)

1. **Lesson wording (correct by appended erratum, not rewrite).** `corpus/lessons/round-95.md` line 29 says "The non-author votes (ReviewerGate, ReviewerBlind, CriticR95) decide the admission." Those seats were lane-dispatched (`w1`). LEARNING.md §Discernment: "A subagent the lane dispatched is still the lane." Relabel as lane-internal votes in an appended correction.
2. **Open survivors (confirmed; not admission-blocking under the frozen predicate).** Critic A3-both and A4 survive the v4 counter. Six C1 legs (`C1_ROWS_TOTAL`, `C1_TRIO`, `C1_LINT`, `C1_EMBEDDED`, `C1_QUOTES`, `C1_K_HELD_BACKED`) have no discriminating forged delta. `C1_PYCACHE` covers one directory. The 22-delta receipt set is partial, and there is no stub-prints-the-pass-line control.
3. **Calibration scope (advisory).** The vectors are the lane's own. Calibration beyond the lane's predicate needs vectors authored outside the counter's author, in the next freeze.
4. **Open follow-up closed by this check.** The round's listed non-author re-fetch of S500/S501 is done here (HTTP 200; sha256 equal to the committed bodies). The lane may cite this file for it in round 96.
5. **Census warnings (status-neutral).** W01 (tierC mined rows with used-by) and W04 (duplicate URLs across scopes) do not block; rc 0.

Operator note (not a decision): no SHONEN box was assessed to box level in this pass. Box 1 (SKILL.md decision tables) and box 3 (self-containment) were not verified; promotion is operator-owned. Nothing here is a `[x]` claim.
