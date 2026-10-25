CONTRACT-OK — 64 seats, one batched dispatch (`dispatch.calls=1`, "Spawned 64 background agents"), 46/64 = 71.9% attack roles, every required role class present, `planner` correctly held by the L1 (validator code `unknown_role`); one thin redirect seat and one out-of-target seat named below, no measure-affecting padding.

# R68 wave-contract audit (sentinel, read-only)

Surface: `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-68/claims.md:185-196` (§Wave contract) against the wave registry. `swarm-registry.json` is **absent** from `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-68/` (`ls` shows only `assimilation/ build-r68.py build-wave-spec.py wave-spec.json`), so the spec is the registry per the seat brief — and per the validator's own planned registry path (`/tmp/r68-plan.json` → `registry.path: .ufo/waves/round-68/swarm-registry.json`, never persisted; finding F5).

Frozen clause text audited (`claims.md:187-196`): "ONE v2 wave of exactly 64 seats under `scripts/hyaku/ufo-wave-policy-v2.json` (band 64–128, `maxLanes` 256), validated (`plan` exit 0) and dispatched as exactly ONE batched call; ≥25% attack roles; build items … and attack items … together; the §3 planner seat is held by the L1 (the validator rejects `planner`; a bounded planning data-walk rides scout/connector items). The slot is acquired via `scripts/hyaku/wave-slot.sh acquire` immediately before dispatch and released only after settlement. Dead seats stay dead and are reported; no replacement seats."

## 1. Exactly 64 seats — HOLDS

Spec: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-68/wave-spec.json` `items` length **64**; 64 unique `name`s; 64 unique report paths, all under `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-68/` (script check: `unique paths: 64`, `dup paths: []`).

Validator plan (`node ~/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs plan --spec …/wave-spec.json`, exit **0**):
`counts {"spawn": 64, "resume": 0, "total": 64}`; `policy {"maxLanes": 256, "minLanes": 16, "waveMinLanes": 64, "waveMaxLanes": 128, "declaredMaxLanes": null}` — 64 is inside the 64–128 band.

On disk: exactly **64** seat transcripts — `ls …/2026-10-25T06-15-52-413Z_01a171b3-…/L1Revenger68/*.jsonl | wc -l` → `64` (the 44 `.md` files in the same directory are seat *outputs*, not agents). Live registry (`read history://`, `grep -c 'L1Revenger68\.R68'` → **64** rows, `grep` for non-`R68` children returns only the `L1Revenger68` row itself). No replacement/extra seats: 64 distinct names, no `…Q01b`-style spawn.

## 2. Exactly ONE batched dispatch call — HOLDS

Dispatch is not a `task` tool call in the L1 transcript; it is one `eval` that performs one `await tool.task({… 'tasks': plan['tasks']})`:

- `/home/vgpnk/.omp/agent/sessions/-Projects-shokunin/2026-10-25T06-15-52-413Z_01a171b3-835d-7667-b875-b75970c45a2a/L1Revenger68.jsonl:109` — toolCall `eval`, title `"Dispatch revenger r68 v2 wave"`, code `plan = json.load(open('/tmp/r68-plan.json')) … r = await tool.task({'i': …, 'context': plan['context'], 'tasks': plan['tasks']})`.
- Same file `:111` — its toolResult text, verbatim first two lines: `seats 64 calls 1` and `{"text": "Spawned 64 background agents using reviewer, critic, executor, scout, mutation-tester, simplifier, sentinel, connector, revenger, scribe.\n- \`L1Revenger68.R68ReviewEntryQ01\` (job …`.
- Of the L1's three `eval` calls (`:109`, `:137`, `:140`), **only `:109` contains `tool.task`**; the other two are `wait` barriers. Zero direct `task` toolCalls anywhere in `L1Revenger68.jsonl`. One spawn result text in the whole transcript (`spawn result texts: 1`).
- `/tmp/r68-plan.json`: `dispatch {"calls": 1, "kind": "task", "note": "Issue exactly one batched task call carrying every spawn lane, plus one hub send per resume lane. Never split a wave into multiple task calls (one-swarm-per-wave)."}`; `len(tasks)=64`; `names match spec order: True`; `role mismatches: []`.

## 3. Attack-role share ≥ 25% — HOLDS (71.88%)

Counted over the 64 spec items (`role` per item; same counts in the plan registry):

| role | count |
|---|---|
| reviewer | 25 |
| critic | 15 |
| mutation-tester | 3 |
| sentinel | 2 |
| revenger | 1 |
| **attack total** | **46 = 71.88%** |
| executor | 12 |
| scribe | 3 |
| scout | 1 |
| connector | 1 |
| simplifier | 1 |

All ten `SWARM_ROLES` of `ufo-swarm-wave.mjs:265-276` are represented; required minimum mix is fully covered (connector 1, executor 12, scribe 3, scout 1, reviewer 25, critic 15).

## 4. Seat items — distinct, concrete; two thin seats, no measure-affecting padding

Partition of all 64 seats onto the four declared targets (checked to be a strict partition: `sum 64`, `missing []`, `unknown []`, `duplicate assignment 0`):

| target | seats | count |
|---|---|---|
| C1 (C7 attribution repair + gate surface) | MutC7Kill, MutC7Spoof, ReviewC7Gate, CriticC7Claim, CriticC7Surface, SimplifierGate, C7Hermetic, ReviewSkillRegistry, CriticClaimsC1 | 9 |
| C2 (C05 v3 candidate, anchors, Q01–Q13) | Q01–Q13, AnchorDerive, AnchorBlind, SnapshotFidelity, AnchorCritic, MutC7Entry, DeriveCritic, CriticEntryDeps, CriticEntryScope, CriticClaimsC2, ReviewSourcesS046, SpotcheckDiscern, Item1–Item10, OracleCorrespondence, QmapSelfCheck, HeaderCheck, ReadmeFlipCheck, CorpusPathHygiene, ConnectorOverlap | 40 |
| claim surface / controls | CounterReplay, CounterIntegrity, HoldSweep, FixtureHold, SentinelScope, CriticSeparability | 6 |
| r67 repairs D1–D4 (+ ledger) | RepairD1, RepairD2, RepairD3, RepairD4, RevengerLedger | 5 |
| frontier step | CensusReplay, LessonCheck | 2 |
| wave contract | WaveContractAudit | 1 |
| outside the four targets | ReviewSkillRefresh | 1 |

Distinctness verified by diffing the templated families: the 13 Q seats differ **only** in `Your criterion: Qxx — …` plus their own report path (e.g. `Q02→Q06`, `Q02→Q10`, `Q01→Q13` diffs are one criterion line each); `Item1…Item10` differ by fact and entry item (`Item2` = `--fact eocd`, `Item6` = `--fact axml_string_pool`, `Item10` = `--fact jar_manifest`), and each maps to an existing numbered item in `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-68-apk-axml-byte-evidence.md:21,28,35,50,59,68,75,82,107,116` (item 11, line 125, is covered by AnchorDerive/AnchorCritic/DeriveCritic/SpotcheckDiscern). Byte-similar prompts (Jaccard 0.89–0.90 for Item2–Item10) are a template artifact, not duplicated work.

**Padding seat (named, per the brief).** `R68ReviewSkillRefresh` (reviewer, axes `['depth','operability']`) is the only seat whose item serves none of C1, C2, the frontier step or the r67 repairs: its item is a SHONEN box-1 audit of all of `SKILL.md`, and its own text records that "the box stays `[~]` unless a non-lane reviewer says otherwise" — a lane seat cannot move it. 1/64 = 1.6%. It is concrete (reads the file, resolves every citation against files + `corpus/SOURCES.md`) but contributes no decision to either frozen predicate.

**Duplicated-decision seat (named).** `R68ReviewEntryQ08`'s criterion line is `Q08 — superseded by Q11 — apply Q11 and say so`; its body then says "a value that the command does not print is a FAIL for Q11 and a FAIL for the criterion that carries it". It therefore yields an `n/a`-by-supersession, not an independent Q08 verdict, and Q11 already has its own seat. This is defensible (`QUALITY.md:23` Q11 says "Supersedes Q08", and C2's predicate allows `n/a` only with a named reason), but the wave's "Q01–Q13 decisions" is in substance 12 substantive decisions + 1 recorded supersession.

**Calibration defect in the Q seats (F2, the most consequential finding here).** Every Q seat restates its criterion as an abridgement of `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/QUALITY.md:13-25`, not verbatim (`verbatim matches: 0/13`; Q13 differs only by a full stop). Six abridgements drop a clause on which the criterion can FAIL:

- Q02 seat drops `verified-at:` "(date or commit)" and `recheck:` "(the command or citation that re-verifies it)" (QUALITY.md:14) — and adds "every anchor it states is the right line", which is not in Q02.
- Q05 seat drops "acquisition" from "presence, configuration or acquisition is not capability" (QUALITY.md:17).
- Q07 seat drops "(accept, refuse, cause)" and the whole sentence "A cause is stated only once independently reproduced." (QUALITY.md:19).
- Q09 seat drops "Saved records stay byte-preserved." (QUALITY.md:22).
- Q11 seat drops "A value cited only to prose is labeled recorded, not re-derived." (QUALITY.md:23).
- Q12 seat drops "(a successor or revision)" (QUALITY.md:24).

Impact: C2's pass branch requires "every applicable Q01–Q13 decision … is PASS"; a seat that cannot record a FAIL on the omitted clause is a weaker gate than the frozen criterion, so an all-PASS wave is strictly less informative than an all-PASS under `QUALITY.md`. Smallest remediation: put the QUALITY.md row text verbatim in each seat's criterion line (or cite `QUALITY.md:<row>` as the operative text and keep the paraphrase as gloss). This is a seat-item defect, not a measurement defect: no frozen counter label reads the seat prompts.

## 5. §3 planner seat held by the L1 — HOLDS

The spec has **no** `planner` item (roles are the 10 `SWARM_ROLES` only), and the validator rejects the role. Quoted from the validator itself, by calling its exported planner in memory over this exact spec with `items[0].role` set to `planner` (`node --input-type=module`, `planSwarmWave` from `/home/vgpnk/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs`):

```
CODE: unknown_role
MESSAGE: items[0].role "planner" is not a swarm role
```

Source of the rule: `ufo-swarm-wave.mjs:263-264` "Swarm lanes are the ten proposal roles. planner/distiller/labrat/Main are frozen-topology seats and can never be swarm lanes." and `:988-989` `if (typeof raw.role !== "string" || !SWARM_ROLES.has(raw.role)) fail("unknown_role", `items[${index}].role ${JSON.stringify(raw.role)} is not a swarm role`)`. Running `plan` on the real spec prints nothing about `planner` and exits `0` (stdout = the plan JSON, stderr empty).

Planning is L1-owned in fact: `build-wave-spec.py` (45 926 bytes, L1-authored, mtime 03:25) is run by the L1 at `L1Revenger68.jsonl:92` with `PLAN_EXIT=0`; the bounded data-walk rides `R68AnchorBlind` (scout) and `R68ConnectorOverlap` (connector).

## 6. Slot acquisition / release — HOLDS (with a naming residue, F4)

`~/.local/state/shokunin-hyaku/wave-slots:68` → `1792909550 64 revenger round-68-w1`; `L1Revenger68.jsonl` toolResult: `granted lane=revenger wave=round-68-w1 seats=64 live=66 pending=0 cap=256` with `ACQUIRE_EXIT=0`, logged at `2026-10-25T03:25:50-03` — **12 s before** the dispatch eval at `2026-10-25T06:26:02.111Z` (= 03:26:02-03). The ledger line is still present now, i.e. no release happened before settlement, as the clause requires (`release` removes the row: `wave-slot.sh:91-96`).

## Findings (severity · evidence · impact · smallest remediation)

- **F1 · MEDIUM · calibration.** Q-seat criteria are abridged, not the frozen text (`verbatim matches: 0/13`; six clauses dropped, list in §4). Impact: a wave all-PASS is weaker than an all-PASS under `QUALITY.md:13-25`, and the C2 predicate consumes exactly those decisions. Fix: replace each `Your criterion:` line with the verbatim `QUALITY.md` row.
- **F2 · MEDIUM · calibration/provenance.** `R68ReviewEntryQ08` yields no independent verdict (criterion "superseded by Q11 — apply Q11 and say so"). Impact: 1 of 13 criteria is decided by another seat's criterion. Fix: if the seat is kept, make it record the supersession explicitly as `n/a — QUALITY.md:23 Q11 supersedes Q08` plus the Q11-row quote, and have the adjudication count 12 substantive + 1 named n/a.
- **F3 · LOW · coverage.** `R68ReviewSkillRefresh` is out-of-target (padding by the brief's definition, 1/64) and self-declares it cannot flip box 1. Fix: drop the seat, or re-point it at the `## Gate registry` row that C1/repaired D2 actually owns.
- **F4 · LOW · operability.** The reservation is keyed lane+wave as `round-68-w1`, while the spec/registry wave is `revenger-r68-v2`. `release` deletes by exact `(lane, wave)` (`wave-slot.sh:93`), so a release issued with the spec's wave string leaves the row behind. Impact is bounded: `pending()` only counts rows newer than 120 s (`wave-slot.sh:67`), so no permanent seat leak — but `status` keeps a stale line. Fix: record the exact acquire string in the round report and release with `revenger round-68-w1`.
- **F5 · LOW · provenance.** The validator's planned registry was never persisted (`/tmp/r68-plan.json` → `registry.path: .ufo/waves/round-68/swarm-registry.json`; the file does not exist), and this round has no committed dispatch receipt — r67 committed `plan-validated.json`, `dispatch-envelope.json`, `dispatch-run{,-2}.log`, `dispatch-start*.txt` under `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/`, r68 has none. Impact: "exactly one batched call" is re-derivable only from live session state (`~/.omp/agent/sessions/…/L1Revenger68.jsonl:109,111`) and volatile `/tmp` files, not from committed lane bytes — the same provenance class the round's own Q09/Q13 posture rejects. Fix: commit the plan's `dispatch` block plus the spawn result text as `.ufo/waves/round-68/dispatch-envelope.json` in the settlement revision.
- **F6 · INFO · legibility.** 10 seats declare axes outside the wave's declared axis list (`coverage, calibration, depth, freshness, adjacency`): `operability` ×5 (AnchorDerive, C7Hermetic, CounterReplay, ReviewSkillRefresh, CorpusPathHygiene), `freshness` ×4 (SnapshotFidelity, CensusReplay, FixtureHold, RepairD3), `adjacency` ×1 (ConnectorOverlap). The validator only checks axes *shape*, not membership (`ufo-swarm-wave.mjs:609-619`), so wave-level axis accounting under-counts. No fix required unless per-axis roll-ups are used.

## Not verified (out of this seat's surface)

Dead-seat accounting / replacement-seat behaviour ("dead seats stay dead and are reported") is not checkable from committed bytes: all 64 seats have transcripts and none appears twice under a second name, and the registry shows all 64 rows, but per-seat `stopReason` records live only in the session transcripts. No replacement seat was observed in the 64-name set.

## Tool installs / updates

None. No pacman transaction was run (host-wide pause respected); no `uv`/`npm`/`cargo` install was needed.
