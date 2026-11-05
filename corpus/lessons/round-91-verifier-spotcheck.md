# round-91 verifier spot-check — revenger (non-author closure)

author: hyaku closure (non-author integrator, @m_zfl)

Closed 2026-11-04 (UTC `2026-11-05T00:00Z`) against lane head
`ed2d9f14fc07d23511b8ee9743b227287f5a8f0f` (= `git ls-remote origin
refs/heads/main`); base `f6356ffb8b665bddc5ee2cfac81443c1300b59bf`. I did not
author this round and did not improve it: every number below is a re-derivation
over committed bytes or a plain probe I ran myself. Lane repo
`/home/vgpnk/Projects/shokunin/revenger-shokunin`; fleet root
`/home/vgpnk/Projects/shokunin`. No `jj` command was run in the lane except
through `scripts/hyaku/jj-lane.sh state` (pure git, read-only).

## Step-1 conformance — PASS (defects below are status-neutral)

- **Report landed by the lane identity, last.** `git -C <fleet> log
  --format='%an <%ae> %H %ci' -- .ufo/reports/round-91/revenger.md` →
  `revenger-shokunin <revenger@shokunin.local> 0b1c7fdafa1d6ef1d7ea344ee40d15a9af1ab5a6
  2026-11-04 20:00:47 -0300`. Lane tip `ed2d9f1` is dated 19:59:34, so the
  report was written after the last lane commit. Commit subject names the
  round's real verdict (`C1 contested on a skip-work-reachable counter, C2 NOT
  VERIFIED; hardened successors landed unclaimed`).
- **Substantive report, not a marker.** 210 lines; sections present in order:
  work performed (claims named first), landed changes (each row tied to the
  `LOG.md` round-91 entry and a commit), before → after measurements, sources &
  frontier, trend verdicts, `## SHONEN`, round notes.
- **`SHONEN` heading.** `grep -c '^## SHONEN'` = 1; `grep -c '^- \['` = 4, one
  line per box of `SHONEN.md`, all `[~]` with pointers, none `[x]`.
  `SHONEN.md`, `PROVINCE.md` and `corpus/QUALITY.md` are absent from
  `git diff --name-status f6356ff ed2d9f1`.
- **Cited lane commits exist and are ancestors of the branch ref** (never
  `@{u}`; the repo is jj-colocated, `HEAD` detached). `git merge-base
  --is-ancestor <hash> main` → true for all six: base `f6356ff`, freeze
  `b13aac7`, wave evidence `d509e98`, landing `d3f4e6c`, receipts `c517dba`,
  tip `ed2d9f1`.
- **Lane pushed, no uncommitted round work.** `jj-lane.sh state` →
  `branch=main local=ed2d9f1… remote=ed2d9f1… ahead=0 behind=0 head=detached
  tracked=0 untracked=1`; `git -C <lane> status --porcelain` prints exactly
  `?? reports/round-91/__pycache__/` (python bytecode, mtime 20:39 — not round
  work; D8).
- **Prompt carries the template contract.** `.ufo/prompts/revenger-round-91.md`
  §1–§5 are `templates/round-prompt.md` rendered with the revenger
  substitutions (mission/axes binding, 1–3 falsifiable claims, frontier step,
  L2 floor, report contract, commit/push/L0), plus the hyaku §6 addendum; the
  L2 floor is quoted as ≥8 in one batched call, matching `MISSION.md` §L2
  concurrency, and the prompt's routing-split section is the run-15 operator
  ruling. Five child-lane items all present: report path, commit-before-report
  ordering, `SHONEN` heading, commit-hash citation, lane write scope.
- **Dispatch/complete digest** (`.ufo/watchdog.log`, mutable — copied here):
  `2026-11-04T19:33:00-03:00 launch revenger round=91 pgid=3412088
  driver=hyaku-inline attempt=1`; `2026-11-04T20:01:03-03:00 complete revenger
  round=91; hyaku-inline attempt=1`.
- **Wave.** One batched call, 13 seats (`.ufo/waves/round-91/w1-validate.out`:
  `counts.spawn=13`, `policy.waveMinLanes=8`, `waveMaxLanes=16`); roles 4
  executor / 2 scribe / 1 scout / 2 reviewer / 1 critic / 1 mutation-tester /
  1 connector / 1 sentinel; attack seats 4 (2 reviewer + critic +
  mutation-tester) = 4/13 = 30.8 % ≥ 25 %.
- **Defects (status-neutral):** D1 the lane's main-repo commit swept
  `.ufo/l0-questions.md` in the same commit as the report (`git show --stat
  0b1c7fda` lists both files) instead of being pathspec-limited to its report;
  D4 frozen round shape says 12 seats while 13 ran; D5 report overstates the
  C2 control set; D9 dead `c2-after.log` pointer. All routed below.

## Per-claim re-check (re-measured by me, not evidence-verified)

Both claims are lane-owned gates/counters, so `PROTOCOL.md` §Gate standard
(Closure consequence) binds: I re-ran the *round's frozen counters* over
committed bytes and my own probes, and read the committed self-test tally —
I did not treat a sibling's green gate as a verdict.

### C1 — calibration, SM6 reads the stated cell: `SM6_MISCLASS` 5/22 → 0/22 — RE-MEASURED, **NOT VERIFIED** (control passes)

Tree under test: `git archive d3f4e6c | tar -x -C /tmp/<tmp>`; `--lane` = the
lane repo (SM5 resolves hashes there).

```
PYTHONUTF8=1 python3 -B reports/round-91/c1_counter.py \
  --impl corpus/self_assessment_check3.py --real <archive> --lane .
→ SM6_MISCLASS=0/22 · MUTANTS_KILLED=11/11 · IMPL_SELFTEST exit=0 ·
  REAL_SELF_MISMATCH=0 exit=0 · C1_VERDICT=pass · exit 0
--impl corpus/self_assessment_check2.py → SM6_MISCLASS=5/22
  (R03, R04, R05, R06, R08 — the five real-format rows) · C1_VERDICT=fail · exit 1
--impl corpus/self_assessment_check.py  → SM6_MISCLASS=11/22 · exit 1
```

The reported before → after reproduces exactly. **The frozen counter is not
discriminating**: the critic's skip-work control also passes it —

```
--impl .ufo/waves/round-91/w1/CriticR91Claims/receipts/impl_fit_hardcoded.py
→ SM6_MISCLASS=0/22 · MUTANTS_KILLED=11/11 · C1_VERDICT=pass · exit 0
```

a 21-entry lookup table that never reads the stated cell. Under the round's own
frozen §C1 control clause ("a control that meets the target means the battery
or target is wrong; then no data is collected") the claim does **not verify**.
The lane self-ruled the same (`claims.md` erratum 2, `SCORECARD.md:1692`,
`corpus/lessons/round-91.md`).

**Battery labels I re-derived by hand** from the frozen rule (last line naming
`K_HELD_BACKED` → stated cell = index 2 of a ≥5-cell row → truncate at
`_STRICT` → first `N/D` after the token, right side of `→`): R03 stated
`8/15 → 9/15` vs truth 8/15 ⇒ 1; R04 `8/15 → 8/15` ⇒ 0; R05 `8/15 → 8/14` ⇒ 1;
R06 scores-only stated cell ⇒ 1; R07 `4/14 → 8/15` ⇒ 0; R08 `9/15 → 9/15` ⇒ 1.
6/6 agree with the committed labels.

**Independent non-author probe** (my own cases, labels derived by me, not the
lane's battery; run from a scratch dir, re-runnable as written):

```sh
cat > /tmp/indep_sm6.py <<'PY'
import importlib.util, tempfile
from pathlib import Path
def load(p,n):
    s=importlib.util.spec_from_file_location(n,p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
v1=load("corpus/self_assessment_check.py","v1"); v2=load("corpus/self_assessment_check2.py","v2"); v3=load("corpus/self_assessment_check3.py","v3")
C=[(15,8,"| coverage — K | `K_HELD_BACKED` 8/15 (5.3) → 8/15 (5.3); C05 uncovered | probe (`K_HELD_BACKED=9/15`) | a → b | unchanged |",0),
   (15,8,"| coverage — K | `K_HELD_BACKED` 8/15 (5.3) → 9/15 (5.3); C05 uncovered | probe (`K_HELD_BACKED=8/15`) | a → b | improved |",1),
   (15,8,"| coverage — K | `K_HELD_BACKED` 8/15 (5.3) → 8/14 (5.3) | probe (`K_HELD_BACKED=8/15`) | a → b | improved |",1),
   (15,8,"| coverage — K | 5.3 → 5.3 | probe `K_HELD_BACKED` (`K_HELD_BACKED` 8/15 → 8/15) | a → b | unchanged |",1),
   (15,8,"| coverage — K | `K_HELD_BACKED` 8/14 (5.7) → 8/15 (5.3) | probe | a → b | improved |",0),
   (16,9,"| coverage — K | `K_HELD_BACKED` 9/16 (5.6) | probe (`K_HELD_BACKED=9/16`) | a → b | improved |",0),
   (14,6,"| coverage — K | `K_HELD_BACKED` 6/14 (4.3) | probe (`K_HELD_BACKED=6/14`) | a → b | improved |",0),
   (14,6,"| coverage — K | `K_HELD_BACKED` 7/14 (4.8) | probe (`K_HELD_BACKED=6/14`) | a → b | improved |",1)]
bad={"v1":0,"v2":0,"v3":0}
for rows,held,line,exp in C:
    d=Path(tempfile.mkdtemp()); (d/"corpus").mkdir()
    (d/"corpus/README.md").write_text("".join(f"| C{i:02d} | s | k | w | {'held' if i<=held else 'frontier'} |\n" for i in range(1,rows+1)),encoding="utf-8")
    (d/"SCORECARD.md").write_text("## R\n"+line+"\n",encoding="utf-8")
    for k,m in (("v1",v1),("v2",v2),("v3",v3)):
        bad[k]+= m.sm6(d)!=exp
print("INDEP_MISCLASS",bad,"of",len(C))
PY
PYTHONUTF8=1 python3 -B /tmp/indep_sm6.py
→ INDEP_MISCLASS {'v1': 3, 'v2': 5, 'v3': 0} of 8
```

So the *implementation* move is real and measurable on cases neither the lane's
battery nor its reviewer's set contains: v3 0/8, v2 5/8, v1 3/8. What fails is
the round's *frozen predicate*, not the artifact. The lane's unclaimed
successor reproduces the same split over run-time-generated cases:
`c1_counter2.py` → v3 `RANDOM_MISCLASS=0/40 seed=91091`, fitted table `18/40`,
exit 1.

### C2 — operability, message↔tree capability: `CAP_MESSAGE_TREE` fail → pass — RE-MEASURED, **NOT VERIFIED** (two stubs pass)

```
PYTHONUTF8=1 python3 -B reports/round-91/cap_probe.py --lane . \
  --range 7fab03f..refs/heads/main
→ CAP_PRESENT=1 · CAP_SELFTEST=pass · CAP_PLANTED_MISS=pass
  (clean_exit=0 dirty_exit=1) · CAP_REAL=pass commits=26 cited=26 misses=10
  exit=1 · CAP_MESSAGE_TREE=pass · exit 0
```

The before → after reproduces (base has no instrument: `CAP_PRESENT=0`,
`reports/round-91/c2-red-absent.log`). **The frozen probe is not
discriminating**: I copied `cap_probe.py` into a scratch dir with each critic
stub as `message_tree_check.py` (the probe resolves its instrument as a sibling
of itself, so the lane tree is untouched):

| stub | frozen probe | successor `cap_probe2.py` |
|---|---|---|
| `stubD` (no tree/filesystem lookup; prints `misses=99`) | `CAP_MESSAGE_TREE=pass`, exit 0 | `CAP2_VERDICT=fail`, exit 1 |
| `stubE` (worktree-only; prints `misses=1`) | `CAP_MESSAGE_TREE=pass`, exit 0 | `CAP2_VERDICT=fail`, exit 1 |
| `stubA` (constant pass line) | `CAP_MESSAGE_TREE=fail`, exit 1 | `CAP2_VERDICT=fail`, exit 1 |

Two of three stubs pass the frozen probe, matching the critic and the lane's
own self-ruling; the report's "three C2 stubs that pass the frozen probe"
overstates its own receipts (`probe-stubA.log` shows `fail`) — D5.

**The landed instrument does measure.** I built a throwaway repo in which
`a.txt` exists in the worktree but not in the commit under test
(`git init` → commit `add a.txt` → `git rm a.txt` → commit `remove a.txt but
cite a.txt` → restore `a.txt` in the worktree):

```
PYTHONUTF8=1 python3 -B reports/round-91/message_tree_check.py --lane . --range HEAD~1..HEAD
→ COMMIT 7aad7d9… cited=1 misses=1 missing=a.txt · MESSAGE_TREE commits=1 cited=1 misses=1 · exit 1
```

so it resolves against the commit tree, not the worktree. Real history
reproduces the reported shape (`commits=26 cited=26 misses=10` today vs
`commits=23 cited=25 misses=9` at landing — 3 more commits, +1 miss), and the
one genuine mismatch the round names is real: `git cat-file -e
d509e98:ufo-wave-policy.json` → `fatal: path 'ufo-wave-policy.json' does not
exist in 'd509e98'`.

### Unclaimed items I re-ran (context, not claims)

- `cap_probe2.py` on the landed instrument → `CAP2_VERDICT=pass`, exit 0
  (`CAP2_TREE_SCOPE=pass worktree_has_file=True`).
- `c1_counter2.py` → v3 `RANDOM_MISCLASS=0/40`, fitted control `18/40` (above).
- Reviewer held-out receipts (`ReviewerR91C1/heldout-{run,v2-comparison,
  reference-check}.log`) → `HELDOUT_MISCLASS=0/22` (v3), `5/22` (v2), `0/22`
  (reference) — consistent with my own 8-case probe.
- Coverage holds: `reports/round-73/measure.py .` → `K_HELD_BACKED=8/15`,
  `C10_HELD_BACKED=0/1`; `reports/round-81/f_probe4.py corpus` →
  `F4_COVERAGE=11/11 score=10.00` — identical at both ends.
- SKILL registry count: `grep -c '^| name |' SKILL.md` → 17 (15 at base), so
  the corrected "17 instrument blocks" sentence is true.
- `git diff f6356ff ed2d9f1 -- corpus/self_assessment_check2.py
  corpus/self_assessment_check.py` empty (v1/v2 bytes untouched); `SM1–SM5`
  function bodies identical between v2 and v3 (textual compare, 5/5).

## Per-axis verdicts

| axis | verdict | basis |
|---|---|---|
| calibration | **improved** | my own 8 hand-labelled real-format rows: v3 0/8 vs v2 5/8 vs v1 3/8; frozen counter reproduces 5/22 → 0/22 with 11/11 mutants killed. The claim is nonetheless unverified because its frozen counter also passes a lookup-table control. |
| operability | **improved** | a new runnable instrument exists, runs over 26 commits, and is tree-scoped by my own fixture test; its registry row says `probe` (not gate) and names what a green run does not establish. The claim's frozen probe admits two stubs, so the claim is unverified. |
| coverage | unchanged | `K_HELD_BACKED=8/15`, `C10_HELD_BACKED=0/1`, `F4_COVERAGE=11/11` at both ends; no claim was declared on the lowest non-retired axis, with the reason frozen pre-data in `claims.md` and a named r92 move. |
| depth | unchanged | `SKILL.md` gained two registry blocks and lost a stale count sentence; no depth claim, no entry weakened. |
| freshness | unchanged | no re-verification claim; three sources opened and dated this round. |
| adjacency | unchanged | `PROVINCE.md` byte-unchanged; ADJ-06 stays reported, not absorbed; connector scan found no sibling instrument. |

No axis is harmed: `PROVINCE.md`/`corpus/QUALITY.md` untouched, no
`corpus/knowledge/` change, v1/v2 instrument bytes preserved, coverage holds
identical.

## Discernment spot-check (LEARNING.md — checked from outside)

The round filed three source admits and no source-reject row; the reject
samples are the round's assimilation refusal and a registry reject row.

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S488 git-log `%B` | admit, docs tier A, `mined` | `https://git-scm.com/docs/git-log` (HTTP 200, 375,962 B, live fetch today) | **agree** | the pretty-formats table prints `%B` — "raw body (unwrapped subject and body)"; quote is exact, 7 words, anchor is a named table, and the instrument parses `--format` output |
| S489 `git cat-file -e` | admit, docs tier A, `mined` | `https://git-scm.com/docs/git-cat-file` (HTTP 200) | **agree** | DESCRIPTION prints "-e Exit with zero status if <object> exists and is a valid object." — exact, ≤25 words; it grounds the per-commit path test the instrument actually runs |
| S490 Conventional Commits 1.0.0 | admit, docs tier A, `mined` | `https://www.conventionalcommits.org/en/v1.0.0/` (HTTP 200) | **agree** | Specification prints "A description MUST immediately follow the colon and space after the type/scope prefix." — exact, ≤25 words; the scope cell correctly limits it to "message shape, not a rule this lane enforces" |
| assimilation package `merge/revenger/` | **reject** (nothing adopted) | `.ufo/waves/round-91/assimilation/{reg-ids,staged-ids,collisions}` | **agree** | `comm -12 <(sort reg-ids) <(sort staged-ids) \| wc -l` → **155** of 155 staged ids; `collisions` is 155 lines; mass id drift is not a per-row collision, and the guard proof (`indented_row_detected=1`) shows the check can fail |
| S025 EVM Codes (registry reject) | reject, community tier C | `https://www.evm.codes/` (HTTP 200) | **agree** | same build id `SnI4EiV4C4sZ8lujLV3M-` as the row's anchor and still no publication date on the page — "undated community reference" holds |

Census: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate
--root /home/vgpnk/Projects/shokunin revenger` → exit **0**, 21 W01 + 10 W04
warnings, last line `revenger ok …/corpus/SOURCES.md`; rows 487 → 490
(`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`), the
three new rows all `mined` with `used-by corpus/lessons/round-91.md`, which
exists.

Disagreement: none on the sampled decisions. The round's own gate, however,
did not exercise a *reject* of its own this round — the reject evidence is
inherited — and its record headings claim more than its gate ruled (D2).

## Trend verdicts

- **expansion: unchanged.** No `corpus/knowledge/` entry was admitted
  (`git diff --stat f6356ff ed2d9f1 -- corpus/knowledge/` empty) and no
  coverage row moved (`K_HELD_BACKED=8/15` both ends). Three tier-A source rows
  are curation, not expansion (`CORPUS.md` rule 4). Agrees with the lane.
- **quality: improved.** v3 supersedes v2's SM6 with a stronger instrument on
  evidence I generated myself (0/8 vs 5/8), the two non-discriminating
  instruments the round exposed are hardened by red/green successors I
  reproduced (fitted control 18/40 vs v3 0/40; stubD/stubE/stubA killed by
  `cap_probe2`), and a stale SKILL sentence is corrected to a countable 17
  blocks (verified). No admitted entry, instrument or criterion was weakened.
  Caveat routed as D9: the round's *record* cites a receipt path that does not
  exist, so the citation layer, not the corpus, is what degraded.
- **discernment: improved.** The lane refused both of its own claims on its own
  counters — C2 self-ruled NOT VERIFIED, C1 reported contested with the
  reproducing control named — and appended errata for two wrong numbers instead
  of restating them; my spot-check agrees with every sampled admit and reject.
  Partial offset (D2): `SCORECARD.md:1674` and the `LOG.md` round-91 heading
  still assert "(C1 verified)"/"(C2 capability, verified)" against the round's
  own body — a record contradiction, routed, not a gate-decision error.

## Routed defects for the lane's next round

1. **D9 — dead evidence pointer (new).** `reports/round-91/c2-after.log` is
   cited by `SCORECARD.md:171` (capability row), `SCORECARD.md:1686` (round-91
   receipts), `SKILL.md:346` (`measured-against`) and
   `corpus/lessons/round-91.md` (receipts line); the file does not exist
   (`git ls-files | grep c2-after` → round-89/round-90 only). The C2 after-run
   is inside `reports/round-91/c1-after.log` (`-- C2 frozen probe` section).
   Fix: r92 appends a correction naming the dead path and the real receipt (or
   commits the receipt); no in-place rewrite.
2. **D2 — record headings contradict the round's verdict.** `SCORECARD.md:1674`
   and the `LOG.md` "## Round 91" heading say "(C1 verified)"/"(C2 capability,
   verified)" while the report, the lesson and both SCORECARD rows say C1
   contested and C2 NOT VERIFIED. `LOG.md` is append-only: append a correction
   entry naming the superseded heading; `SCORECARD.md` appends a correction row.
3. **D5 — report overstates the C2 control set.** "three C2 stubs that pass the
   frozen probe" — `probe-stubA.log` shows `CAP_MESSAGE_TREE=fail`; two stubs
   (stubD, stubE) pass. Correct in r92's report/lesson.
4. **D4 — frozen round shape not reconciled.** `claims.md` "Round shape (fixed
   here)" says 12 seats / 4 attack = 33 %; 13 seats ran (ReviewerR91C2 added
   post-freeze), and `w1/swarm-registry.json` milestone strings still say
   "12-seat build+attack wave". Reconcile in r92 and fix the milestone text.
5. **SM6 v4 battery (carried from the round's own routed list, still open).**
   Add a 5-cell row and a row that names the STRICT metric so M03/M04 stop
   surviving, and kill M06/M07/M09/M17; also close rule-step-1's line-vs-row
   blind spot (a prose line naming the metric wins the slot — it scored 1 on
   this round's own SCORECARD before the sentence was reworded).
6. **r90 routed C2 predicate still open** (instrument pins + `parseEvidence` id
   consistency); named in `SCORECARD.md` but unworked this round.
7. **D4 (r89, census env pin) still open** — the census gate's frozen baseline
   pins inputs, not host state; re-flagged, unworked.
8. **Report pointer hygiene (r90 item 5) not applied** — lane-repo paths in
   the report are lane-relative; prefix them with `revenger-shokunin/` or state
   the root once.
9. **D8 — untracked build artefact** `reports/round-91/__pycache__/`
   (`mutants.cpython-314.pyc`, `sm6_battery_v3.cpython-314.pyc`) in the lane
   worktree; remove and gitignore `__pycache__/`.
10. **D1 — main-repo commit scope.** `0b1c7fda` carries the report *and*
    `.ufo/l0-questions.md`; the lane's main-repo commit is pathspec-limited to
    its own report file (`PROTOCOL.md` §Invariants). The L0 line itself is
    correct and now durable.

## Admission

C1 meets its frozen counter but that counter is reachable by a skip-work
control I reproduced, so the claim does not verify; C2's frozen probe is passed
by two stubs I reproduced, so it does not verify either. The lane self-ruled
both and filed the round as an honest stop. Under `AXES.md` a round is admitted
only if every claim verifies and no axis is harmed: **not admitted**, verdict
`rejected-honest-stop`; lane status `ok` (real, committed, pushed work with
resolvable hashes). Axis verdicts above stand on my own re-measurements and
agree with the entry appended to `MANIFEST.json` for this closure.
