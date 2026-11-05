author: hyaku closure (non-author integrator, @m_zfl)

# revenger round 99 — non-author verifier spot-check (closure)

Lane round: revenger r99 (hyaku run 15, attempt 1). Base `3d054a98e3fa768e63b631665a2372fadb51a77a`,
lane tip `3c707c8af83020f9a9bd5491efe70be3d5456230`. Report `.ufo/reports/round-99/revenger.md`.
Driver digest (copied from `.ufo/watchdog.log`):
`2026-11-05T18:40:20-03:00 launch revenger round=99 pgid=1373837 driver=hyaku-inline attempt=1`;
`2026-11-05T19:35:23-03:00 complete revenger round=99; hyaku-inline attempt=1`.

Outcome: **status ok, admitted**. C1 (coverage K 13/15 → 14/15) and C2 (calibration, r98 holdout
v7 9/12 → v8 0/12, development set) both verify. No axis harmed.

## 1. Step-1 conformance

| check | command | observed | result |
|---|---|---|---|
| report attribution | `git log --format='%an <%ae> %H %cI' -- .ufo/reports/round-99/revenger.md` (fleet) | `revenger-shokunin <revenger@shokunin.local> 1174ffbc… 2026-11-05T19:35:10-03:00` (before the 19:35:23 completion line) | ok |
| SHONEN heading | `grep -c '^## SHONEN' <report>`; `grep -cE '^- \[' SHONEN.md` (lane) | 1 heading; 4 `[~]` lines in the report = 4 boxes in SHONEN.md | ok |
| cited commits are ancestors of `main` | `git cat-file -t <h>` + `git merge-base --is-ancestor <h> main` for 3d054a98, 7e6edd4d, 61e27feb, 9ddd38ac, 01266760, 250dd8f3, 3c707c8a | all 7 `commit`, all ancestors | ok |
| lane pushed, clean | `scripts/hyaku/jj-lane.sh state …/revenger-shokunin` | `branch=main local=3c707c8a… remote=3c707c8a… ahead=0 behind=0 head=detached tracked=0 untracked=0` | ok |
| leftovers | `git status --porcelain \| wc -l` (lane) | `0` | ok |
| round commits | `git log --format='%h %an' 3d054a98..3c707c8a` | 6 commits, all `revenger-shokunin` | ok |
| prompt fidelity | `diff templates/round-prompt.md <(sed -n '1,140p' .ufo/prompts/revenger-round-99.md)` | only placeholder lines differ (`{{LANE}}`, `{{ROUND}}`, `{{FLEET_ROOT}}`, `{{AXES}}`); §6 hyaku addendum at prompt line 141, §7 scratch discipline at 677 | ok |
| gate/probe registry home | `sed -n '636,664p' SKILL.md` | rows for `c1_k_admit_counter8`, `forge_reach8`, `deriv_check`, `mutate8` (name, kind, entry command, pinned-value path, owner) | ok |

Conformance notes (status-neutral):
- The report's round-end census line reads "21 × W01, 0 E-codes" and omits the 13 W04 warnings its
  own `census-round-end.log` records (and my re-run shows: 21 W01, 13 W04, rc 0).
- The C1 do-nothing control ran on `61e27feb` (Amendment A) while `claims.md` names "the
  claims-freeze commit" (`7e6edd4`); the registry row records `FREEZE_REV 61e27feb`. The control
  still refuses (rc 1), and `61e27feb` only adds the S505 grounding, so the deviation makes the
  control harder to refuse, not easier. Recorded, not harm.
- The L1's `git mv -k` slip is self-disclosed; the lane state shows no index/jj residue.

## 2. Claims — re-measured vs evidence-verified

### C1 — coverage, K 13/15 → 14/15 (C14 `partial → held`)

Re-measured (plain counts over committed bytes):
- `git show <c>:corpus/README.md | grep -E '^\| C[0-9]+ ' | awk -F'|' '{s=$(NF-1)…}'` →
  `3d054a98`: `held=13 partial=1 uncovered=1`; `3c707c8a`: `held=14 uncovered=1`.
- `git diff 3d054a98 3c707c8a -- corpus/README.md` → one row changed (C14), C02 row untouched.
- Entry header `admission-status`: `candidate` at `3d054a98`, `admitted` at `3c707c8a`.
- Q11 re-derived myself: `grep '^    paths\[3\]: ' corpus/live/runs/round-98/rea-doctor-r98.txt | sed … | tr ',' '\n' | grep -c .` → `3` (entry row `:97` cell `3`).

Evidence-verified (lane-owned v8 counter; not executed by me):
- Counter bytes `sha256sum reports/round-99/c1_k_admit_counter8.py` → `620dfca9…3581`; `git diff --quiet 01266760 3c707c8a -- <counter> <forge_reach8>` → unchanged since the v8 freeze.
- `post-freeze/landing-archive-c14r99.log`: header names `git archive 250dd8f3…` (landing commit), `C1_K_HELD_BACKED=14/15`, `C1_VERDICT=pass`, votes digest `246d09a8…`.
- `post-freeze/c1-controls.out`: do-nothing rc 1, junk-row rc 1, `control-ok (both refused)`.
- `post-freeze/selftest-v8-frozen.log`: clone at `01266760`, `SELFTEST_C1V8=OK legs=98`, rc 0.
- Votes `reports/round-99/votes/*.json`: `grep -ohE '"(PASS|FAIL|n/a)"' | sort | uniq -c` → 33 PASS, 18 n/a, 0 FAIL (= 10+11+12 PASS, 7+6+5 n/a as reported).
- `post-freeze/landing-archive-deriv-check.log`: `DERIV_ROWS=29 DERIV_MISMATCH=0`, rc 0.

Verdict: **verified** — reported 13/15 → 14/15 matches.

### C2 — calibration, r98 holdout: v7 accepts 9/12 → v8 0/12

Evidence-verified (lane-owned harness; not executed by me):
- Before: `controls/c2-do-nothing-v7-holdout98-c02.log` `HOLDOUT98 accepted=5/6`, `…-c14.log` `accepted=4/6`, both `HOLDOUT98_CONTROL=control-ok` → 9/12.
- After: `post-freeze/c2-v8-frozen.log` — twelve `C2_VECTOR … refused legs=…` lines, each naming a v8 leg; `C2_ACCEPTED=0/12`, `C2_CONTROL_C02=control-ok`, `C2_CONTROL_C14=control-ok`, `C2_STUB_SELFTEST=ok`, `C2_VERDICT=met`, rc 0. Harness sha256 `0a393136…bb67`, unchanged since `01266760`.
- No regression: `post-freeze/noreg-forge7-v8-c02.log` (0/5 kept) and the self-test above.
- Generalization: `post-freeze/holdout99-v8-c14.log` `HOLDOUT99 accepted=6/6` (and c02 6/6) — the gain is a development-set gain, as the claim itself pre-registered.

Verdict: **verified** on its frozen predicate (development set; fresh r99 holdout not refused).

### No-harm (owned axes)

- `git diff 3d054a98 3c707c8a -- SCORECARD.md`: one appended `## Round 99` section; no earlier row edited.
- `git diff 3d054a98 3c707c8a -- PROVINCE.md corpus/QUALITY.md SHONEN.md | wc -l` → `0`.
- C02: README row byte-identical; the A1 diagnostic rule as written is not met (v8 `c02` also fails
  `C1_K_HELD_BACKED`, K 14 vs pinned 13 — the flip itself), but the landing tree with only the two C14
  flip lines reverted passes v8 and v7 `c02` (`post-freeze/landing-c14unflipped-c02{,-v7}.log`). The
  lane disclosed this as M19. I rule C02 unharmed; the diagnostic rule needs re-deriving (routed).
- Sources: rows 507 → 507 (census row count at both commits); my census re-run rc 0, 0 E-codes.

### Per-axis verdicts

| axis | verdict | basis |
|---|---|---|
| coverage | improved | C1 re-measured 13 → 14 held; gate evidence verified |
| calibration | improved | C2 evidence verified (9/12 → 0/12, dev set; fresh holdout 12/12, no generalization) |
| depth | unchanged | not claimed |
| freshness | unchanged | not claimed (S506/S507 re-opens support C1, not a freshness claim) |
| operability | unchanged | not claimed |
| adjacency | unchanged | not claimed |

## 3. Discernment spot-check (from `corpus/lessons/round-99.md` `## Gate`)

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| C14 entry `round-98-rea-host-readiness.md` (S506 quote) | admit | `curl` of the pinned S506 URL at `12f6e09` → http 200, 16650 bytes, sha256 `ce2d122b…2e50` = committed `S506.body`; `grep -c -F 'Static JavaScript and ordinary ZIP inventory need neither Hopper nor Ghidra.'` → 1 | agree | the sentence the route row rests on is live, verbatim, at the pinned revision (11 words, ≤ 25) |
| C14 entry (S507 record) | admit | `sha256sum corpus/live/runs/round-98/*.txt` → `94eaa6ff…`, `fb9a4824…`, `c373f656…` (equal to the r98 values); `head -c 41 rea-doctor-r98.txt` → `healthy: false` / `environment_healthy: false` | agree | the located quote and record digests match the registry row and entry |
| candidate digest `36cc6ac2…` (VoterGateR99 Q16 FAIL) | reject | ran the `7e6edd4` entry's "scope-check classes" command on the doctor record → `10 classification: config_drift` / `11 classification: healthy` / `3 classification: missing_analysis_engine`; the cell recorded `10 config_drift` / … | agree | the cell was not the command's stdout, contradicting the entry's own "verbatim stdout" preamble; the amended command (`sed 's/^classification: //' … sed 's/^ *//'`) prints exactly the amended cell |
| r98 S505 correction `mined → queued` | reject (replaced by Amendment A) | `grep -cw S505 corpus/lessons/round-97.md` → 3; S505 row `used-by` now `corpus/lessons/round-97.md` | agree | the lesson that introduced S505 cites it, so grounding by citation is true and keeps the C02 chain terminal-mined |

Registry row re-opened: S507 (`corpus/SOURCES.md:524`) — new `teaches` fragment says the exit code is
not a line of the record; `grep -c exit corpus/live/runs/round-98/rea-doctor-r98.txt` → 0. Agree.
S506 row quote ("Static JavaScript … Ghidra.", 11 words) re-checked above. No new rows this round.

Census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger` → rc 0;
`ok` 1, `W01` 21, `W04` 13, no E-codes.

## 4. Trend verdicts

- **expansion: improved** — C14 moves `partial → held` on an admitted entry citing mined S506/S507 (README held 13 → 14).
- **quality: improved** — the C14 row's pre-contract, not re-gated checklist is superseded by a gated entry whose 29 derivation rows `deriv_check` re-runs with 0 mismatches; the S507 `teaches` overclaim (exit 1) is corrected; S506 re-verified byte-identical today.
- **discernment: improved** — the spot-check agrees with the gate on both admits and both rejects; the gate refused the lane's own candidate on a real defect (re-derived above).

## 5. Routed defects (lane must fix in r100)

1. Fresh r99 holdout: v8 accepts 12/12 (`.ufo/waves/round-99/w1/CriticR99/fresh/`); add legs, including running `deriv_check.py` inside the counter (C14-N3).
2. Entry §Q-map Q13 rationale ("no verifier is credited") is stale against the Q11/Q16 rows that credit `deriv_check.py` — correct it with a new digest/re-vote or an appended correction.
3. Re-derive the C02 no-harm diagnostic rule for a K-moving flip (M19) before it is reused.
4. Report census lines must carry every warning class the log prints (r99 omitted 13 × W04).
5. Do-nothing control must run on the commit `claims.md` names, or the claims must name the amended commit.
6. Carried: `d-host` tree survivor; M4 `claude-red-re-bridge.md`; producer-attribution census; L0 assimilation 155/155 id collisions.

Operator note: the four SHONEN boxes are each `[~]` with lane-seat evidence only; this closure
re-ran C14 derivations (Q11, scope-check classes) and the S506/S507 re-opens from committed bytes, which
bears on boxes 2–3 as a non-author check. Promotion stays operator-owned.
