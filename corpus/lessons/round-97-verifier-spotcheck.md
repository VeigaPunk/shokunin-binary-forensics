author: hyaku closure (non-author integrator, @m_zfl)
round: 97 (revenger, lane_round 97)
checked-against: revenger-shokunin@e95e2fd5b841ec50196cb0e03269298ecca02ef9
base: 7d380ce2c75d3dfd24dfb7759d04f207eeeb1a68 · claims freeze: 3b4b4e5c1d123d5fc5337ad59015b4752366854a · v6 freeze: 85a2c7eb0a980413a62cd9330ffd5b7e9005c332 · landing: 47e4f6c9425c0d74e256991dd29dfa1d98001f22
report: .ufo/reports/round-97/revenger.md

# Round 97 — non-author verifier spot-check

Scope: step 1 conformance, step 2 claim re-check, step 3 discernment spot-check. The integrator ran every
command below on committed bytes on 2026-11-05. The lane's own counter (`c1_k_admit_counter6.py`), harness
(`forge_reach6.py`) and mutation tool (`mutants/mutate.py`) were NOT executed (PROTOCOL §Gate standard,
Closure consequence). Each claim is marked **re-measured** (the integrator ran a plain count over committed
bytes) or **evidence-verified** (the integrator checked the committed gate output, its predicate and the
revision it measured, without re-executing it).

Lane verdict of record: **C1 improved on the frozen counter (admission pending non-author closure); C2 met on
its frozen predicate, contested (development set).**
Integrator verdict: **admitted.** Both claims verify; no axis is harmed; lane status `ok`. This closure is
also the non-author admission of the C02 entry `corpus/knowledge/round-96-native-analysis-sessions.md`, which
round 96 and round 97 left pending.

Driver digest, copied from `.ufo/watchdog.log`, which is mutable:
`2026-11-05T16:33:07-03:00 launch revenger round=97 pgid=2735252 driver=hyaku-inline attempt=1` ·
`2026-11-05T17:38:58-03:00 complete revenger round=97; hyaku-inline attempt=1`.

## 1. Conformance (step 1)

| check | command | observed | result |
|---|---|---|---|
| report attribution | `git log --format='%an <%ae> %H %cI' -- .ufo/reports/round-97/revenger.md` (fleet) | `revenger-shokunin <revenger@shokunin.local> 48a349bec939f417fcdfb4cdcd430ca13b4329e6 2026-11-05T17:36:07-03:00`, which is after the lane's last commit (17:34:38) and before the driver completion (17:38:58) | ok |
| SHONEN heading | read of the report | `## SHONEN` with four `[~]` lines, one per box | ok |
| cited hashes exist and are ancestors | `git cat-file -t <h> && git merge-base --is-ancestor <h> main` for 7d380ce, 3b4b4e5, 85a2c7e, 47e4f6c, e95e2fd | all `commit`, all ancestors of `main` | ok |
| lane pushed and clean | `scripts/hyaku/jj-lane.sh state revenger-shokunin`; `git status --porcelain` | `branch=main local=e95e2fd… remote=e95e2fd… ahead=0 behind=0 head=detached tracked=0 untracked=0`; porcelain empty | ok |
| remote tip | `git ls-remote origin refs/heads/main` | `e95e2fd5b841ec50196cb0e03269298ecca02ef9` | ok |
| prompt fidelity | `.ufo/prompts/revenger-round-97.md` (committed 1b8ed56, 16:33:05) lines 1–140 diffed against `templates/round-prompt.md` (byte-identical to the kimi-shokunin template, `cmp` exit 0) | 34 diff lines, all `{{LANE}}`/`{{ROUND}}`/`{{FLEET_ROOT}}`/`{{AXES}}` substitutions; §1–§5 present; hyaku addendum §6 at line 141 | ok |
| lane commits in range | `git log 7d380ce..e95e2fd` | 4 commits (3b4b4e5, 85a2c7e, 47e4f6c, e95e2fd), all authored by `revenger-shokunin` | ok |

Conformance defects (status-neutral): none that bar status. See §6 for routed items.

## 2. Claims (step 2)

### C1 — coverage, K 12/15 → 13/15 (C02 `partial → held`). **re-measured + evidence-verified → improved**

Re-measured (plain count of coverage-map status cells, `corpus/README.md`):

```
git show <rev>:corpus/README.md | grep -E '^\| C[0-9]{2} \|' | awk -F'|' '{s=$6; gsub(/ /,"",s); print s}' | sort | uniq -c
7d380ce: 12 held · 2 partial · 1 uncovered   (15 rows)
e95e2fd: 13 held · 1 partial · 1 uncovered   (15 rows)
```

`git diff 7d380ce e95e2fd -- corpus/README.md` changes only the C02 row: the knowledge cell becomes
`knowledge/round-96-native-analysis-sessions.md`, the status `partial → held`. In the entry, the only change is
`admission-status: candidate → admitted`.

Committed counter evidence, not executed: `controls/measured-at-landing/c1-v6-landing-47e4f6c.log` prints
`C1_K_HELD_BACKED=13/15`, `C1_ONLY_C02=pass`, `C1_VERDICT=pass`. `controls/base-v6.log` and
`controls/c1-do-nothing-v5.log` print `12/15`, `C1_VERDICT=fail`. The red-before is
`controls/red-v5-corpus-prefix.log` (`C1_SOURCES=fail`, rc=1) against `green-v6-corpus-prefix.log` (`C1_SOURCES=pass`, rc=0).
`git diff --stat 85a2c7e e95e2fd -- reports/round-97/c1_k_admit_counter6.py reports/round-97/forge_reach6.py reports/round-97/forgeries`
is empty, so the counter bytes did not change after the freeze.

Non-author admission of the C02 entry. The integrator re-derived its derivation table from `git archive e95e2fd`:

| value | integrator command | observed | entry says | match |
|---|---|---|---|---|
| fixture sha256 | `sha256sum corpus/fixtures/pe-r75-headless-smoke/fixture.exe` | `fe060de1…afd72`, 1024 bytes | same | yes |
| entry bytes `B82A000000C3` | python `find(bytes.fromhex('B82A000000C3'))` | offset 512 | authored entry sequence | yes |
| Evidence ID | `grep -m1 evidence_id rea-decompile.raw.txt` | `ev_cc0b9d88…ffefe` | same | yes |
| provider | `grep -A3 '^provider:'` | `ghidra / Ghidra / 12.1.4` | same | yes |
| function count / entry line | `sed -n 3,4p codeable-decompiled.c` | `function_count=1` / `// ==== FUNC entry @ 140001000 ====` | same | yes |
| headless receipt | `grep -c 'INFO  REPORT' ghidra-headless-r96.log` | 6 | 6 | yes |
| record digests | `sha256sum corpus/live/runs/round-96/*` | `d717b491…`, `6ce217fa…`, `2fba7fbf…`, `6a1d18c3…` | same prefixes | yes |
| decompiled body | `sed -n 6,10p codeable-decompiled.c` | `undefined8 entry(void)` / blank / `{` / `  return 0x2a;` / `}`; `decompiled_ok=1` count 1 | lines 6–10 | yes |

The entry is scoped to one fixture, one host, one date and named tool versions. It states the absent engines
(Hopper, IDA) and keeps the doctor's `healthy: false` and exit 1. Its two external sources re-open
byte-identical (§3). **Integrator rules the entry admitted.**

### C2 — calibration, v5 reach 14/19 → v6 0/19 on the frozen vectors. **re-measured (before) + evidence-verified (after) → improved, contested**

- Before, re-measured from the committed receipts:
  `python3 -c 'import json;d=json.load(open(".ufo/waves/round-96/w1/CriticR96/receipts/summary.json"));print(sum(x["observed_verdict"]=="pass" for x in d),len(d))'`
  → `14 19`. `controls/c2-v5-reproduced.log` accepts the same 14 (FG01–FG12, FG15, FG19; `grep verdict=pass`).
- After, evidence-verified: `controls/c2-v6-frozen.log` has 19 `DELTA … verdict=fail` lines, each naming a
  specific failing leg, then `C2_ACCEPTED=0/19`. `grep -c 'builder note'` = 0, so every delta applied.
- Positive control: `controls/c2-positive-landing-v6.log` → `C1_VERDICT=pass`. Stub check:
  `controls/c2-selftest-v6.log` → `stub-pass accepted=19/19 stub-fail accepted=0/19`, `SELFTEST verdict=OK`.
- Kill rule ("any vector accepted by v6 → not met"): no vector is accepted.
- Contest, disclosed by the lane and confirmed here: the 19 vectors are a development set (Amendment A5). The
  independent evidence is the A4 holdout. `.ufo/waves/round-97/w1/CriticR97/holdout-v6.log` (committed in
  47e4f6c) shows `accepted=5` of 12 named forgeries (FR02, FR08, FR09, FR10, FR12), down from 8 under v5. FR06
  and FR07 are refused only by `C1_ADMITTED_UNION`. The calibration gain is real but partial.
- Deviation from Amendment A2: A2 requires the three outputs `C2_ACCEPTED`, `C2_POSITIVE` and
  `C2_STUB_SELFTEST` "in one recorded run". The evidence is three logs, and the tokens `C2_POSITIVE` and
  `C2_STUB_SELFTEST` are never printed. The counter bytes are unchanged across the three runs, which the empty
  diff above shows. The integrator treats this as a conformance defect, not a falsified claim.

Mutation (reported, not a claim): `controls/mutate-v6-kill.out` → `MUTANT_KILL_V6=107/140`, `MUTANT_SELFTEST_V6=137/140`, and `d-host` is in `SURVIVORS_TREE`.

### Per-axis verdicts

`git diff 7d380ce e95e2fd -- SCORECARD.md` only appends the round-97 section, including the appended round-96
count correction. `git diff --stat 7d380ce e95e2fd -- PROVINCE.md corpus/QUALITY.md` is empty.

| axis | verdict | basis |
|---|---|---|
| coverage | improved | held 12 → 13 of 15 (re-measured); C02 entry re-derived and admitted here |
| calibration | improved | 14/19 → 0/19 frozen (development set), holdout 8/12 → 5/12; contested, partial |
| depth | unchanged | no SKILL decision-table change; three probe registry rows only |
| freshness | unchanged | S502/S503 re-opened byte-identical; no stale entry re-verified |
| operability | unchanged | new probes are measurement instruments, not domain operability |
| adjacency | unchanged | connector scan found no overlap; PROVINCE byte-unchanged |

## 3. Discernment spot-check (step 3)

| item | lane decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| C02 entry `round-96-native-analysis-sessions.md` | admit | S502 and S503 raw URLs at `12f6e09` (fetched 2026-11-05 by the integrator), plus the committed `corpus/live/runs/round-96/*` and fixture | agree | S502: 38167 bytes, sha256 `c818ee34…cc24`, quote "`rea decompile <path> --file-offset=0x... --provider ghidra` resolves the source byte offset internally" count 1 (12 words). S503: 35095 bytes, sha256 `b5f17fdf…6ccc`, quote "Use shipped-artifact … guide a reconstruction." count 1 (17 words). All 8 derivation values match (§2) |
| S504 r96 located quote `undefined8 entry(void) { return 0x2a; }` | reject (reworked as S505) | `git show e95e2fd:corpus/live/runs/round-96/codeable-decompiled.c` | agree | `grep -cF` → 0 (rc 1): the saved bytes are five lines with a blank line 7, so the one-line form is a reflow, not a quote |
| assimilation of `merge/revenger/` (155 staged rows) | reject (none adopted) | committed `.ufo/waves/round-97/assimilation/{staged-ids,reg-ids,collisions}` | agree (partial re-open) | `comm -12` of sorted staged and registry ids gives 155 of 155; registry 504 ids at the time. The staging dir `merge/revenger/` is no longer present at the fleet root, so the package itself could not be re-opened |

New SOURCES row re-opened: **S505** (`corpus/SOURCES.md:522`, own-work, tier A, `mined`, opened 2026-11-05). Its
anchor is `codeable-decompiled.c` lines 6-10, 1-based bytes 101-142. `head -c 142 | tail -c +101 | od -c` gives
42 bytes: `undefined8 entry(void)\n\n{\n  return 0x2a;\n}`, which is byte-exact and well under 25 words. The row's
slash rendering (`undefined8 entry(void)` / `{` / `  return 0x2a;` / `}`) omits the blank line 7. The byte range
is authoritative and correct. `teaches` opens `supersedes S504 —` (contract rule 2).

Census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger` → rc 0, `ok`, 21 × W01,
13 × W04, 0 E-codes. This matches the report. Rows 504 → 505 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`).

## 4. Trend verdicts

- **expansion: improved.** One admitted entry on coverage-map ground that was only `partial` (C02). Its
  `source:` lines cite mined rows S502, S503 and S504. Held 12 → 13 (re-measured).
- **quality: unchanged.** No entry was superseded or re-verified beyond C02's own sources. S505 corrects a quote
  form and adds no knowledge.
- **discernment: improved.** The non-author spot-check agrees with the gate on the admit (C02) and on both
  rejects (S504 quote form, assimilation). The counter refuses 19/19 frozen vectors and 7/12 holdout forgeries.
  It is not fully discriminating: 5 holdout forgeries remain, and `d-host` survives.

## 5. SHONEN note for the operator

Box 2 (end-to-end domain task logged) is now non-author checkable: this closure re-derived the C02 session
record from committed bytes (§2). Boxes 1 and 3 have registry rows and committed run logs. The integrator did not
execute the lane's tools, so it does not certify them. Promotion is operator-owned. Nothing is written to
SHONEN.md.

## 6. Routed defects (lane fixes next round)

1. **S505 `used-by` is ungrounded.** It names `corpus/knowledge/round-96-native-analysis-sessions.md`, but that
   entry never cites S505: `grep -c S505` = 0, while it cites S504 three times. Either cite S505 through a
   superseding entry version or correct the `used-by` cell with a logged old→new change.
2. **Amendment A2 single-run requirement is unmet.** The three C2 outputs sit in three logs, and the
   `C2_POSITIVE` and `C2_STUB_SELFTEST` tokens are never printed. Fix: make forge_reach6 emit all three in one
   recorded run.
3. **The v6 self-test prints a stale label.** `c1_k_admit_counter6.py:1026` prints `SELFTEST_C1V5=…`. Rename it
   to v6 so logs identify their counter.
4. **The stub self-test does not apply its deltas.** `c2-selftest-v6.log` has 28 `builder note … No such file`
   lines because the stub fixtures lack the delta targets. The 19/19 and 0/19 tally holds only because the
   stubs ignore their input. Build stub runs on the full fixture.
5. **The lane wrote `admission-status: admitted` before non-author closure.** The flip came in 47e4f6c. It is
   ratified by this closure. Next time, land `admitted` only after closure, or record the flip as pending.
6. **Carried items, still open:** holdout FR02/FR08/FR09/FR10/FR12; a row-set leg so FR06/FR07 are refused by
   design; a byte-exact own-work quote leg (M9); `d-host` and the 33 v6 tree survivors; M4 index-or-reject for
   `claude-red-re-bridge.md`; D2, the M7 SCORECARD line from the r96 spot-check (not done).
7. **L0, operator:** the assimilation id collision (155/155). The staging package is gone from the fleet root, so
   the evidence is now only the committed id lists.
