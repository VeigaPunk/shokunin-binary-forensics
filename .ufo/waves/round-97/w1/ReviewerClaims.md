# ReviewerClaims — revenger round-97 w1 — attacks on the frozen claims

Seat scope: claims text, controls, SCORECARD round-96 section, corpus/lessons/round-96.md (read-only), frozen v5 counter `reports/round-96/c1_k_admit_counter5.py` and `forge_battery5.py` (read-only), CriticR96 receipts. All commands run on my scratch copy of `git archive 7d380ce corpus reports .ufo`. Tools installed: none (no tool install or upgrade; no pacman usage).

## Verdict per attack

### C1 — coverage (K 12/15 → 13/15)

- (a) no-work / junk control: **survives.** No-work (base tree, no flip) cannot reach 13/15: the frozen v5 counter over the isolated base copy prints `C1_VERDICT=fail`, `C1_K_HELD_BACKED=12/15`, `C1_SOURCES=fail` (rc=1) — reproduced, matching the committed control `reports/round-97/controls/c1-do-nothing-v5.log` line for line. The only failing leg with the flip absent that the control receipt records is the used-by path-form leg; my reproduction additionally shows the artifacts/registry legs passing only with an isolated scratch (`HYAKU_SCRATCH`-free alias collision with another seat's leftover `revenger-r96` scratch; my isolated rerun matched the committed log exactly, see receipts). Junk edits to other rows are blocked by `C1_ONLY_C02` + `C1_ROWS_TOTAL=15` legs (18 legs enumerated from counter bytes: 18 `legs[...]` keys). A v6 that passes the base tree is declared wrong by the claims and correctly so.
- (b) predicate implementable without naming vectors: **survives.** The one-sentence C1 predicate decomposes into the 18 v5 legs plus a used-by normalizer change; no Forgery-vector name is needed for C1. The 18 legs enumerated from committed counter bytes: `['C1_ADMITTED', 'C1_ADMITTED_UNION', 'C1_C02_CITES', 'C1_C02_HELD', 'C1_EMBEDDED', 'C1_EMBED_NONVACUOUS', 'C1_K_HELD_BACKED', 'C1_LINT', 'C1_ONLY_C02', 'C1_PYCACHE', 'C1_QUOTES', 'C1_RECEIPTS', 'C1_REGISTRY', 'C1_ROWS_TOTAL', 'C1_SIDS', 'C1_SOURCES', 'C1_TRIO', 'C1_VOTES']`.
- (c) re-derivation of 12/15 from committed bytes: **confirmed.** Census at base 7d380ce:
  `grep -cE '^\| C[0-9]+ .*\| held \|$' <base>/corpus/README.md` → **12**; `grep -c '^| C[0-9]* ' corpus/README.md` → **15**. Counter-equivalent enumeration over the base copy (emulating `held_backed` logic from `c1_k_admit_counter5.py:531-536`) gives held rows C01,C03,C04,C06,C07,C08,C09,C10,C11,C12,C13,C15 = 12 backed (held+resolvable knowledge path), with C02 `partial`, C05 `uncovered`, C14 `partial`. After flip, C02 held + a resolvable entry gives exactly 13/15; the committed `reports/round-96/c1-tree-flip-diagnostic.log` confirms `C1_K_HELD_BACKED=13/15` and my corpus-prefixed flip fixture with used-by patched to the fixture form produced the same `C1_K_HELD_BACKED=13/15`, `C1_VERDICT=pass` from v5.
- (d) universal clauses — see table below.
- (e) r96 mismatch 13 vs 14: **confirmed for SCORECARD; partially wrong for the lesson** — see finding 2.

### C2 — calibration (v5 14/19 → v6 0/19)

- (a) no-work / junk control: **survives for no-work; flagged for refuse-everything** — see finding 1. No-work (frozen v5) does not reach 0/19: replaying the committed `drv.py` forgery builders against the frozen v5 on my scratch gives **v5 accepted 14/19** (`[FG01…FG12, FG15, FG19]`), identical to the committed receipt recount (finding 2). A printing stub is rejected by the r96 battery's STUB control (`forge_battery5.py:221-230`, `STUB_REJECTED=pass`), but the C2 counting command alone exposes no such check — finding 1.
- (b) predicate implementable: **survives.** C2's one-sentence predicate ("accepted = counter prints `C1_VERDICT=pass` on the tree carrying that delta") requires no vector names in the predicate; the harness enumerates the 19 committed vector dirs. Count of vectors in committed `drv.py` `FORGERIES`: **19**, FG17 absent (`FG01`–`FG16`, `FG18`–`FG20`).
- (c) recount of CriticR96 `summary.json`: **confirmed 14/19** — finding 2.
- (d) universal clauses — see table below.
- (e) mismatch: **confirmed** — finding 2.

## Findings by severity

### Finding 1 (calibration gap — C2 positive control is outside the frozen counting command) — survives as a wording gap, recommend L1 decide before scoring

The frozen C2 counting command is
`PYTHONUTF8=1 python3 -B reports/round-97/forge_reach6.py --counter reports/round-97/c1_k_admit_counter6.py --deltas reports/round-97/forgeries`
and the claims freeze only one output line, `C2_ACCEPTED=<n>/19`. A counter that refuses everything (blanket-fail) trivially scores 0/19 — that junk control DOES reach the target. The claims acknowledge this with the positive control ("the landing tree … is accepted by v6; a blanket-refusing stub is rejected by the battery's stub check"), but that stub/positive check lives outside the frozen counting line — the frozen output line cannot distinguish a refuse-everything v6 from a real v6. **Recommendation (wording edit for the L1, before any scoring): require the battery to print and freeze positive-control lines in the same run, e.g. `C2_LANDING_POSITIVE=pass` and `C2_STUB_REJECTED=pass`, and require both before `C2_ACCEPTED=0/19` counts.** No frozen rule forbids this addition now because the harness is uncommitted; after any scoring it would become a new claim, per the freeze order.

### Finding 2 (the r96 calibration mismatch confirmed; the claims' wording about the lesson is itself inaccurate) — falsified wording, honest correction needed

Recount from committed bytes (receipts dir `.ufo/waves/round-96/w1/CriticR96/receipts/summary.json`):

```
python3 -c 'import json;d=json.load(open(".ufo/waves/round-96/w1/CriticR96/receipts/summary.json"));print(sum(x["observed_verdict"]=="pass" for x in d),len(d))'
→ 14 19
```

Accepted ids: FG01–FG12, FG15, FG19. The SCORECARD r96 calibration row states "found 13 counter PASSES" (`SCORECARD.md` r96 section, calibration row; the row lists F1–F11 + F13/F14 minor). So the SCORECARD/minor count is 13 of the listed finding IDs while 14 pass rows exist in the committed receipts — the mismatch the claims describes is real **for the SCORECARD only**. But the r96 lesson (`corpus/lessons/round-96.md`) names no "13 accepted" anywhere (its only "13" token is `K at 13/15`, line 35) and does not state an accepted-vector count at all. The claims sentence "the r96 SCORECARD and lesson state **13** accepted" is therefore wrong about the lesson; the correction should name the SCORECARD alone. The frozen claims bytes cannot be edited; only the L1 can decide whether this second mismatch is recorded as a finding with a wording fix in the round-97 lesson.

### Finding 3 (C1 predicate clause "exactly once" is ambiguous between per-row and total) — wording gap

Frozen C1 predicate: "…the used-by exclusivity leg accepts the census form `corpus/knowledge/<entry>` as well as the fixture form `knowledge/<entry>`, for a used-by cell naming the admitted entry exactly once across the S502/S503/S504 rows." The v5 bytes implement per-row exclusivity: `set(ub) != {ENTRY_REL}` per row (`c1_k_admit_counter5.py:379-382`), so each of the three rows names the entry once — three times total. "Exactly once across the … rows" reads more naturally as exactly once total, which no implementation would meet (the hypotheses says "naming the admitted entry exactly once across" could mean per-row). **Recommendation: reword to "each of the S502/S503/S504 used-by cells names the admitted entry exactly once and nothing else."** Decidable by the L1 before scoring; the predicate text itself is frozen but the claims admit a wording change decision by the L1 for the frozen predicate only via a new claim, so this should be settled before the v6 counter is scored.

### Finding 4 (do-nothing control reproduction had a lane-scratch alias collision) — survives with an honesty note

The committed control receipt `reports/round-97/controls/c1-do-nothing-v5.log` reproduces exactly only when the scratch alias under `/fast/scratch/hyaku/revenger-r96/c1v5` is clean; my first reproduction run read leftover `swarm-registry.json`-missing state from a stale sibling of the default scratch lane and reported `C1_REGISTRY=pass` mismatch states; after redirecting `HYAKU_SCRATCH` to my own scratch and rerunning on an isolated `--tree` copy, the committed control receipts matched line for line:
`C1_K_HELD_BACKED=12/15`, `C1_VERDICT=fail`, `C1_SOURCES_WHY=S502:usedby-exclusivity:['corpus/knowledge/round-96-native-analysis-sessions.md']; S503:…; S504:…`, rc=1. The committed C2 control `c2-v5-reach-from-r96-receipts.txt` (19 vectors, 14 accepted, listing accepted FG01–…, FG15, FG19) matched my replay of the committed `drv.py` against the frozen v5 byte for byte in count and membership. Both formats of the controls therefore hold; no falsification.

### Finding 5 (census round start reproduced exit 0, warnings W01/W04 pre-existing confirmed)

`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --today 2026-11-05 --root /home/vgpnk/Projects/shokunin revenger` → rc=0 over the fleet root; the tally of warnings is 13×W04 + 21×W01, no E rows, matching `reports/round-96/controls/census-round-start.log` byte for byte (the file lists 35 lines). The claims' census-before statement holds.

## Universal-clause table (attack d)

| clause in claims.md | command enumerates the full set? |
|---|---|
| L24 "passes **every** leg of the r96 5-set" | yes — the C1 counting command runs the full counter and prints all 18 legs (`legs.py` enumeration over committed counter bytes: 18 legs listed above). |
| L59 "**every** vector rejected by at least one named failing leg" | partial — the frozen output line `C2_ACCEPTED=<n>/19` counts the set but does not print each vector's named failing leg; per-vector receipts exist in the battery's own receipts dir (like `drv`), so the full set is enumerated on disk but not in the frozen output line. Recommend the L1 add a per-vector output line (e.g. `C2_VECTORS=FG01:fail:C1_SOURCES;…`) if a print-only fix is wanted before scoring. |
| L82 "**all** 155 staged ids collide" | confirmed from committed bytes: `wc -l` of the two committed `assimilation/{staged-ids,reg-ids}` files → 155 and 504; `comm -12 <sort stage> <sort reg>` → 155 intersection; the committed `collisions` file (155 lines) matches my `comm` recount (`diff` silence). "All" is fully enumerated. |
| L90 "Godspeed leads **every** L2 prompt" | not machine-checkable by any command in the claims; it is a wave-spec observation (`w1-spec.json` all prompts carry `/skill:godspeed`). Unprovable from the claims alone; recorded as unprovable. |

## Attack (c) full command paste (committed bytes)

```
# K before (base 7d380ce), README census:
$ git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive --format=tar 7d380ce corpus reports .ufo | tar -x -C <base>
$ grep -cE '^\| C[0-9]+ .*\| held \|$' <base>/corpus/README.md
12
$ grep -c '^| C[0-9]* ' <base>/corpus/README.md
15
# v5 do-nothing over the isolated base copy:
$ (cd /home/vgpnk/Projects/shokunin/revenger-shokunin && PYTHONUTF8=1 python3 -B reports/round-96/c1_k_admit_counter5.py --tree <base-copy>)
C1_K_HELD_BACKED=12/15
C1_VERDICT=fail
# rc=1
# C2 recount from committed receipts:
$ python3 -c 'import json;d=json.load(open(".ufo/waves/round-96/w1/CriticR96/receipts/summary.json"));print(sum(x["observed_verdict"]=="pass" for x in d),len(d))'
14 19
# C2 control receipt command committed at reports/round-97/controls/c2-v5-reach-from-r96-receipts.txt also printed:
# vectors 19
# C2_V5_ACCEPTED 14 / 19
# my independent replay of committed drv.py builders vs frozen v5:
# v5 accepted 14/19 (ids FG01…FG12, FG15, FG19); undecided []
```

Additional verification: S502/S503 receipt bodies re-hashed from committed bytes reproduce the claims' digests (`c818ee34…24`, 38167 B; `b5f17fdf…cc`, 35095 B), matching the claims and the v5 RECEIPTS leg's inner re-hash requirement.

## Open questions for the L1

1. Finding 1: freeze the positive-control output lines inside `forge_reach6.py` before any scoring, so the C2 claim's own output line set defends against the refuse-everything shortcut.
2. Finding 2: the claims file says the lesson states 13 accepted — it does not. Record as a finding, not silently corrected (the claims' own freeze rule prohibits editing this clause; the correction lands in the round-97 lesson, not in the frozen bytes).
3. Finding 3: decide per-row vs total reading of "exactly once across the S502/S503/S504 rows" before the v6 counter's used-by normalizer is frozen; the v5 byte semantics is per-row.
4. Finding 4: the default scratch alias collision in the control receipt reproduction is cosmetic for this round (my isolated run matched the committed log) but the L1 may prefer a scratch-hygiene note so future seats don't reproduce the earlier mismatched state.
