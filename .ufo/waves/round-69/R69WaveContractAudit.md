CONTRACT-OK — 64 seats, 1 batched taskCall of 64 tasks, attack 45/64 = 70.31% (lane predicate) and 41/64 = 64.06% (prompt §2 v2 floor), all six required role classes present, `planner` rejected by the validator (exit 1); no padding seat. Two non-voiding caveats: the plan-envelope is only reproducible with `UFO_CONFIG_PATH` pointed at the lane v2 policy **and** `UFO_FLEET_ALLOW_EXTERNAL_TOOLS=1`, and the builder's 64-seat/25%-attack invariants are printed, not enforced.

# Scope

Audited against the frozen contract `reports/round-69/claims.md` §Wave contract (:187-196 region, read in full) and the wave spec `revenger-shokunin/.ufo/waves/round-69/wave-spec.json`. Read-only; nothing edited. Lane-root-relative paths below resolve under `/home/vgpnk/Projects/shokunin/revenger-shokunin`.

Artifact pins (sha256, `sha256sum`):

| artifact | sha256 |
|---|---|
| `.ufo/waves/round-69/wave-spec.json` | `224119d8616e0b08fba2e841d81eddb6be96b801ee135caedd686e0638838d9b` |
| `.ufo/waves/round-69/build-wave-spec.py` | `0555d1268f174453210b6c92d81a7b935fb9d74357f86d7989fea900dbc10b48` |
| `.ufo/waves/round-69/dispatch/dispatch.json` | `248da5766e12d35d10b16fd99192a6abfe790805eef21de46f86f9c99f23d7e2` |
| `.ufo/waves/round-69/dispatch/plan-validated.json` | `248da5766e12d35d10b16fd99192a6abfe790805eef21de46f86f9c99f23d7e2` (byte-identical to `dispatch.json`) |
| `/home/vgpnk/Projects/shokunin/scripts/hyaku/ufo-wave-policy-v2.json` | `f12e1d6dfeae81a4a1ff805f8de50ec8386b3a16ae7f40b171f54c5236812fff` |

# 1. Exactly 64 seats — PASS

`python3` over the spec:

```
items: 64
roles: {'connector': 1, 'critic': 17, 'executor': 11, 'mutation-tester': 3,
        'revenger': 1, 'reviewer': 21, 'scout': 5, 'scribe': 2, 'sentinel': 3}
unique names 64
```

Sum = 64. Registry agrees: `python3 -c` over `dispatch/dispatch.json` → `registry.members == 64`, `counts == {'spawn': 64, 'resume': 0, 'total': 64}`, kinds `{'spawn': 64}` (`swarm-registry.json` likewise 64 members). No resume lanes, so no hub-send path is in play.

# 2. One batched dispatch call — PASS at packet level (issuance not independently observable)

`dispatch/dispatch.json` carries a single `taskCall` object:

```
taskCall keys ['context','tasks']   context=str len 3364   tasks=list len 64
resumeSends []
note: "Issue exactly one batched task call with taskCall ({context, tasks}); never split a wave
       into multiple task calls (one-swarm-per-wave). ..."
```

- 64 tasks in one call, 1:1 with the 64 spec seats (see §6 distinctness).
- `dispatch.json` and `plan-validated.json` are byte-identical (`248da576…`), i.e. one dispatch record, not two.
- Only one `round-69` dispatch directory exists (`.ufo/waves/` holds round-65…round-69); no second round-69 dispatch artifact.
- Commit `35e1258` "round-69: wave preparation — 64-seat v2 spec + builder, validated plan (exit 0), dispatch taskCall (64 tasks), swarm registry, slot acquire receipt (D2)".

Evidence limit (not a violation): the lane tree records the *payload* of exactly one call; the count of actual `task` invocations is attested by the L1 record, not derivable from the tree. The 64 seat reports landing under `.ufo/waves/round-69/` from one wave window (first seat reports at 07:15, all matching dispatched names) is consistent with a single call.

# 3. Attack share ≥ 25% under BOTH predicates — PASS

Predicates as frozen: lane predicate = reviewer/critic/mutation-tester/sentinel/revenger (`build-wave-spec.py:322-323`); prompt §2 v2 floor = reviewer/critic/mutation-tester/labrat (`build-wave-spec.py:324-325`).

| predicate | roles counted | count | share of 64 | floor | result |
|---|---|---|---|---|---|
| lane (`build-wave-spec.py`) | 21 reviewer + 17 critic + 3 mutation-tester + 3 sentinel + 1 revenger | **45** | **70.31%** | 25% | PASS |
| prompt §2 v2 floor | 21 reviewer + 17 critic + 3 mutation-tester + **0 labrat** | **41** | **64.06%** | 25% | PASS |

No `labrat` seat exists, so the floor predicate's margin comes entirely from reviewer/critic/mutation-tester — both counts are computed here, which discharges routed repair D3's "name the predicate" requirement for the wave record.

# 4. Role mix — PASS

Required classes all present (counts above): connector 1 (`R69ConnectorOverlap`), executor 11, scribe 2 (`R69SpotcheckDiscern`, `R69LessonCheck`), scout 5 (`R69AnchorBlind`, `R69QuarA-D`), reviewer 21, critic 17. Not required but present: sentinel 3, mutation-tester 3, revenger 1. No `simplifier`, `planner`, `distiller`, or `labrat` seat.

# 5. §3 planner seat held by the L1; validator rejects `planner` — PASS

Bare command as assigned, from the lane root:

```
$ node /home/vgpnk/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs plan \
    --spec /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-69/wave-spec.json
EXIT=0
schema ufo-swarm-wave-v1 wave revenger-r69-v2
counts {'spawn': 64, 'resume': 0, 'total': 64}
dispatch {'calls': 1, 'kind': 'task', ...}
policy {'source': 'config', 'maxLanes': 256, 'minLanes': 32, 'waveMinLanes': 32,
        'waveMaxLanes': 256, 'hardCeiling': 256, ...}
compaction {'applied': False, ...}
lanes kinds {'spawn': 64}   registry members 64
stderr: (empty)
```

Ability-to-reject probe (scratch copy, lane spec untouched): `/tmp/revenger-r69-planner-probe.json`, seat 0 role rewritten to `planner`:

```
$ node .../ufo-swarm-wave.mjs plan --spec /tmp/revenger-r69-planner-probe.json
EXIT=1
{"schema":"ufo-swarm-wave-error-v1","code":"unknown_role",
 "message":"items[0].role \"planner\" is not a swarm role"}
```

So the validator would reject a planner seat, and the spec contains none — the §3 planner role is held by the L1 itself, as the contract states. (Probe file deleted with the rest of the scratch.)

# 6. Every seat a distinct concrete work item serving C1/C2/frontier/D-repairs — PASS, no padding

Distinctness is mechanical and per-seat:

- 64 unique seat names; 64 dispatch tasks whose `task` strings are pairwise distinct.
- 64 report trailers, 64 distinct paths (`Report: write your scoped findings to .ufo/waves/round-69/<seat>.md`), no duplicate.
- Every seat prompt carries a seat-unique token even after boilerplate removal (minimum 1, mean 10.0) — the low-count seats are the readout seats, whose discriminator is the `--fact` argument.

Work-item content, by group (all resolvable to a concrete artifact/command):

| group | seats | distinct product |
|---|---|---|
| Q01–Q15 decisions on the v4 bytes | `R69ReviewEntryQ01..Q15` (15) | 15 distinct criteria; `Your criterion:` text differs seat-to-seat (diff Q01 vs Q02 shows Q01 = tier-A SOURCES backing, Q02 = header `source:`/`verified-at:`/`recheck:`/coverage-map). Q08 is the registered "superseded by Q11" criterion, not a duplicate of Q11. |
| entry item re-derivations | `R69Item1,2,3,4,6,8,9,10` (8) | 8 distinct `readout.py --fact` invocations (`archive`, `eocd`, `member[AndroidManifest.xml]`, `axml_chunk_table`, `axml_string_pool`, `axml_start_element`, `dex_declared_header`, `jar_manifest`). Items 5/7/11 are deliberately covered by Q04/Q11+Q07/AnchorDerive+Q13 — see the `DROP` rationale at `build-wave-spec.py:284-300`. |
| anchor derivation | `R69AnchorDerive`, `R69AnchorBlind`, `R69AnchorCritic`, `R69DeriveCritic` (4) | run the derivation; blind independent re-derive without the author's table (admission-order independence leg); attack the derivation; attack its failure behaviour in scratch corruptions. |
| C7 instrument (hold, not a claim) | `R69MutC7Kill`, `R69MutC7Spoof`, `R69MutC7Entry`, `R69ReviewC7Gate`, `R69CriticC7Claim`, `R69C7Hermetic` (6) | mutant; mutant+marker spoof; drift injected into the v4 entry; gate read; gameability falsification attempt; hermeticity (3× `--self-test`). |
| counter / holds | `R69CounterReplay`, `R69CounterIntegrity`, `R69HoldSweep`, `R69CriticSeparability`, `R69KillRuleClosure`, `R69RevengerLedger` (6) | replay on base tree; sha pin audit; 10 verifier self-tests + hold labels; C1/C2 separability; kill-rule closure over every conjunct (D5 item 3); adversarial ledger re-read of the claims. |
| claims/entry critiques | `R69CriticClaimsC1`, `R69CriticClaimsC2`, `R69CriticEntryDeps`, `R69CriticEntryScope`, `R69QmapSelfCheck`, `R69HeaderCheck`, `R69OracleCorrespondence` (7) | distinct attack surfaces (claim shape ×2, silent deps, limitation scope, Q-map table internal consistency, header per-field resolution vs `SOURCES.md`, oracle correspondence). |
| C2 / D1 / D4 | `R69Q15CheckerRun`, `R69D1RestateCheck`, `R69ShonenBox1` (3) | Q15 checker `--self-test` + `--scan` on the false fixture; D1 restatement specification via `git rev-parse` pairs; D4 SHONEN box-1 reconciliation. |
| registry / census / corpus hygiene | `R69ReviewSourcesS047`, `R69CensusReplay`, `R69FixtureHold`, `R69CorpusPathHygiene`, `R69ReadmeFlipCheck`, `R69SpotcheckDiscern` (6) | S047 row review; census validate; fixture/live byte hold vs `222a7a70`; added-path hygiene; README C05 status (must stay `uncovered`); outside-discernment spot-check on S047 (C1 predicate leg). |
| quarantine frontier | `R69QuarA`, `R69QuarB`, `R69QuarC`, `R69QuarD` (4) | disjoint row slices — A `S053,S054,S055,S058,S060,S061,S062,S063,S064`; B `S075,S081,S083,S085,S087,S089,S090,S092,S093`; C `S094,S095,S098,S099,S100,S107,S108,S111,S113`; D = any remaining revenger rows + full-register count check. |
| frontier / lesson | `R69LessonCheck` (1) | round-69 `## Mistakes` row + census before/after + S047 citation. |
| province / containment | `R69ConnectorOverlap`, `R69SentinelScope`, `R69MisrootSweep`, `R69WaveContractAudit` (4) | sibling-lane contention; lane/fleet/campaign write containment; fleet-root misroot attribution; this contract audit. |

**Padding: none.** All 64 seats resolve to an artifact or command that exists (26 absolute paths referenced across prompts; the only "missing" hit was a regex artifact on the possessive `q15_tree_id_check.py's`, and `corpus/q15_tree_id_check.py` exists, 5052 bytes). The builder already trimmed 12 redundant drafted seats with a recorded rationale (`build-wave-spec.py:284-300`).

One **partial overlap** to name honestly (not padding, distinct deliverable): `R69MisrootSweep` re-runs `git -C /home/vgpnk/Projects/shokunin status --porcelain` — the same command `R69SentinelScope` runs — but its product is per-file attribution ("is this untracked fleet-root file a revenger/round-69 seat note", verdict `NO-MISROOT`/`MISROOT`), which `SentinelScope`'s `CONTAINED`/`LEAK` verdict does not enumerate. Kept both; the fleet-root-write surface is a claims void condition, so duplicate coverage there is cheap insurance, not seat padding.

# 7. Reproducibility of "under `scripts/hyaku/ufo-wave-policy-v2.json` (band 64–128)" — PASS with a documented env requirement (finding F1, low)

The **bare** command in my assignment validates under a *different* policy envelope than the committed dispatch record: `minLanes 32 / waveMinLanes 32 / waveMaxLanes 256` (resolved from `ufo-fsd-alpha/config/ufo.json`) vs the v2 file's `minLanes 16 / waveMinLanes 64 / waveMaxLanes 128 / maxLanes 256`. The planner resolves policy from `UFO_CONFIG_PATH` (`ufo-swarm-wave.mjs:143`), not from the spec.

Reproduction with the policy pinned to the lane's v2 file:

```
$ UFO_FLEET_ALLOW_EXTERNAL_TOOLS=1 \
  UFO_CONFIG_PATH=/home/vgpnk/Projects/shokunin/scripts/hyaku/ufo-wave-policy-v2.json \
  node /home/vgpnk/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs plan \
  --spec /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-69/wave-spec.json
EXIT=0
policy {'source': 'config', 'maxLanes': 256, 'minLanes': 16, 'waveMinLanes': 64,
        'waveMaxLanes': 128, 'declaredMaxLanes': None, 'hardCeiling': 256, ...}
counts {'spawn': 64, 'resume': 0, 'total': 64}
dispatch {'calls': 1, 'kind': 'task', ...}
```

and the fresh payload matches the committed `taskCall` field-for-field:

```
len 64 64
names eq True
agents eq True
tasks eq True
context eq True
policy equal: True   counts equal: True   registry equal: True
```

64 seats sit exactly on the v2 floor (64 ≤ 64 ≤ 128) and inside `maxLanes` 256, matching `claims.md` §Wave contract. Note the partial invocation also fails closed: with `UFO_CONFIG_PATH` set but without `UFO_FLEET_ALLOW_EXTERNAL_TOOLS=1`, the planner exits 1 with `{"code":"EXEC_PATH_OUTSIDE_ROOT","message":"UFO_CONFIG_PATH resolves outside the project root …"}` — so the committed record could not have been produced by a bare invocation; the env pair was in force at dispatch. **Finding F1 (low, evidence wording):** the claims/wave record should name the env pair it validated under (`lane-addendum.md:75` already prescribes `UFO_CONFIG_PATH`), otherwise a reader replaying the bare command sees a different band and cannot check "band 64–128" from the output alone.

# 8. D2 slot receipt — PASS (artifact committed); release still owed at settlement

`.ufo/waves/round-69/dispatch/slot-acquire.log` is git-tracked (`git ls-files` lists it) and holds the raw acquire line:

```
granted lane=revenger wave=round-69-w1 seats=64 live=66 pending=0 cap=256
```

Live slot ledger (`~/.local/state/shokunin-hyaku/wave-slots`) still shows `64 revenger round-69-w1` reserved, and `wave-slot.sh status` reports `live_estimate=66 recent_reservations=0 cap=256 cap_source=state`. That is the expected pre-settlement state (the wave is in flight); the contract's "released only after settlement" leg is an outstanding post-settlement check, not a defect at this point. Minor naming mismatch only: slot wave token `round-69-w1` vs spec wave `revenger-r69-v2`.

# 9. Finding F2 (low, builder hardening) — invariants printed, not enforced

`build-wave-spec.py:306-330` computes and prints both attack percentages but does not assert the 25% floor, and the seat-count check is a warning, not a failure:

```python
if len(items) != 64:
    print("WARNING: expected 64 seats", file=sys.stderr)
```

Rank-duplicate names do exit 1 (`sys.exit(1)` at :318), so the only hard check is name uniqueness. Today's spec passes every invariant (§1–§3), so this is not a contract violation; the smallest remediation is to convert the 64-seat and ≥25%-both-predicates conditions into `sys.exit(1)` asserts so a future edit cannot silently break the registered wave shape while still producing a spec.

# Commands run (all read-only; no lane/fleet/campaign writes)

1. `python3` counts over `wave-spec.json` (seats/roles/names/report trailers/uniqueness/attack arithmetic/path existence/similarity) — outputs quoted above.
2. `node /home/vgpnk/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs plan --spec …` (bare) → EXIT 0, policy 32/32/256.
3. Same with `UFO_FLEET_ALLOW_EXTERNAL_TOOLS=1 UFO_CONFIG_PATH=…/ufo-wave-policy-v2.json` → EXIT 0, policy 16/64/128/256; payload equals committed `taskCall`.
4. Same with `UFO_CONFIG_PATH` only → EXIT 1 `EXEC_PATH_OUTSIDE_ROOT` (fail-closed probe).
5. `plan` on a `/tmp` scratch copy with one seat role = `planner` → EXIT 1 `unknown_role` (ability-to-reject probe).
6. `sha256sum` on wave spec, builder, dispatch records, policy v2; `git ls-files` on the dispatch dir; `git log --oneline -3 -- .ufo/waves/round-69/`; `wave-slot.sh status` + ledger grep.

Scratch (`/tmp/revenger-r69-*`) deleted before return.

# Verdict

**CONTRACT-OK.** Exactly 64 seats; one batched `taskCall` of 64 tasks with 0 resume sends; attack share 70.31% under the lane predicate and 64.06% under the prompt §2 v2 floor (both ≥ 25%); connector + executors + scribe + scout + reviewers + critics all present; every seat a distinct concrete work item serving C1/C2/the frontier/the D-repairs, with no padding seat; `planner` is rejected by the validator (`unknown_role`, exit 1) and no seat claims it — the §3 planner seat is the L1's. Non-voiding: F1 (plan envelope reproducible only with the pinned `UFO_CONFIG_PATH` + `UFO_FLEET_ALLOW_EXTERNAL_TOOLS=1`; the bare assignment command validates under a 32–256 band) and F2 (builder prints rather than asserts the 64-seat/25%-attack invariants). Slot receipt D2 is committed; slot release is owed at settlement.
