# MutationR97 — scoped findings (round 97, wave 1)

Role: mutation-tester (leaf seat). Axis: calibration (C2). Milestone: mutation harness for the admission counter, instrument check for C2.
Item: build `reports/round-97/mutants/mutate.py` (the L1 runs it on the frozen v6 after the freeze) and prove it on the frozen v5. v6 was NOT run, and no counter was run on any candidate landing tree.

## Deliverables

- `reports/round-97/mutants/mutate.py` (stdlib only; `python3 -B`; sha256 `9867a3c4fa2f7626575d9d7c35e88066e46a6ecc1ef3b19b89af8a542e566095`).
- `.ufo/waves/round-97/w1/MutationR97/kill-v5.log`: `MUTANT_KILL_V5=81/117`, `MUTANT_SELFTEST_V5=110/117`, `MUTANT_KILL_V5_UNION=110/117`, `rc=0`, survivor lists.
- `.ufo/waves/round-97/w1/MutationR97/mutate-run-v5.out`: full run output (every `MUTANT` line with its unified-diff hunk, every `KILL_TREE` and `KILL_SELFTEST` line).
- `.ufo/waves/round-97/w1/MutationR97/manifest-v5.json`, `unmutated-v5-pinned.py`: site table and pinned baseline.
- `.ufo/waves/round-97/w1/MutationR97/mutants-v5-table.md`: the 117-row verdict table (copied below).
- `.ufo/waves/round-97/w1/MutationR97/receipts-<survivor>/`: per-delta self-test receipts (31 per run) for the 7 self-test survivors; all 31 show `decide=true`, i.e. the survivor is real and not a harness artifact.

Tooling: no tool was installed or upgraded. I read `~/.omp/agent/RULES.md`; every run used the system `python3` and the frozen counter, and git was used read-only (`archive`, `rev-parse`, `show`).

## Harness (what the L1 runs)

    python3 -B reports/round-97/mutants/mutate.py --counter reports/round-97/c1_k_admit_counter6.py --out <scratch> \
        --kill-tree <base-or-tree> --selftest --jobs 8 --label V6

- Writes `<scratch>/mutants/unmutated.py`, one `<name>.py` per site, `<scratch>/manifest.json`; prints each mutant's name, changed line, leg(s) and unified-diff hunk.
- Sites (117 on v5): comparison operators inverted (`cmp`), a boolean `not` deleted in a decision expression (`not`), `if` tests negated (`if`), and the MutationR96 `d-host` edit (the host-allowlist sub-check removed). Scope: every top-level function except the archive materialiser, `main`, `self_test` and the fixture builders.
- Excluded on purpose (7 sites, `EXCLUDED_MSG`): decisions that only select WHY text, i.e. element 1 of a `return` tuple (`"ok" if not X else ...`). They decide no leg, so they are not mutation sites.
- LANE pin: identical in baseline and every mutant, `LANE = Path(__file__).resolve().parents[2]` → `LANE = Path(<lane root>)`. Without it a scratch copy resolves LANE to a non-repo and `base_readme`'s `git archive` fails. Same convention as MutationR96.
- Detector 1 (`--kill-tree`, the spec's detector): the mutant runs `--tree <base>`. Killed when the verdict set (`C1_<LEG>=pass|fail|n/m`, `C1_VERDICT`) or the exit code differs from the unmutated run on the same tree; timeout counts as killed.
- Detector 2 (`--selftest`): the mutant's own frozen `--self-test`. Killed when it does not print `SELFTEST_C1V<n>=pass` with rc 0 (version-agnostic since the final run, so it also works on v6).
- Exit codes: 0 completed; 2 counter malformed (the pin anchor, or the `d-host` anchor `if host not in HOST_ALLOWLIST:` + following `fails.append(f"{sid}:host`, is missing or not unique); 3 a detector baseline did not reproduce.

## Baseline (proves the instrument before any mutant verdict)

- Unmutated frozen v5 on base `git archive 7d380ce corpus reports .ufo`: `rc=1`, 20 verdict lines; identical to `reports/round-97/controls/c1-do-nothing-v5.log` (`C1_K_HELD_BACKED=12/15`, `C1_VERDICT=fail`). Diff: none.
- Unmutated frozen v5 `--self-test`: `SELFTEST_C1V5=pass legs=33`, rc 0 (matches the r96 control).

## Results

| detector | killed | note |
|---|---|---|
| Detector 1: base archive 7d380ce (`MUTANT_KILL_V5`) | **81/117** | 81 verdict-set changes; 16 WHY-text-only; 20 no change |
| Detector 2: frozen self-test (`MUTANT_SELFTEST_V5`) | **110/117** | 7 survivors, causes below |
| Union (killed by either) | **110/117** | the base archive added zero kills beyond the self-test |

Survivor list (union, 7): `m011-cmp-check_registry-L190`, `m029-cmp-check_votes-L240`, `d-host`, `m059-cmp-check_sources-L341`, `m061-cmp-check_sources-L345`, `m064-cmp-check_sources-L357`, `m079-if-check_embed_nonvacuous-L407`.

Base-archive survivors (36) are not coverage findings by themselves: on the base tree C1_SOURCES, C1_ONLY_C02, C1_C02_HELD, C1_ADMITTED and the `legs[...]` leg already fail, so an inverted sub-check there can change only WHY text, and the receipt/entry branches are unreachable on base (no `S502.receipt.json`, no entry file). All 36 of those are killed by the self-test or are in the 7 survivors above.

## Survivors: leg it should catch, self-test coverage, cause

For each: the leg, whether a frozen self-test delta names that leg (`EXPECT_FAIL`), and whether any delta exercises the mutated sub-check.

1. **m011-cmp-check_registry-L190** (`!=` → `==`, in `roled = sorted(...)`). Leg: none. It builds only the `rolemismatch=` WHY text; C1_REGISTRY is decided by the unmutated `if got != {...}` on the line above. Leg covered (`V03`, `M6-forged-registry-seat`). **Classification: WHY-text-only, not a leg decision.** The structural exclusion did not catch it because it is a comprehension, not a return-tuple slot. I keep it in the denominator rather than move the goalposts after a run.

2. **m029-cmp-check_votes-L240** (`== "PASS"` → `!=` in `if not any(ds[q] == "PASS" for q in QS)`). Leg: **C1_VOTES**, sub-check "a vote has at least one PASS decision". The mutant accepts an all-`n/a` vote and rejects an all-PASS vote. C1_VOTES has seven deltas (`V04`, `V18`, `F12`, `F13`, `F15`, `F17`, `F20`) but every one keeps at least one PASS decision, so none exercises this sub-check. **Real coverage gap.** Would be caught by a vote whose decisions are all `n/a` with well-formed notes (the vocabulary check passes, so only this sub-check rejects it). Tree detector: base votes carry PASS, so not reachable there either.

3. **d-host** (MutationR96 d-host: host-allowlist sub-check removed from `check_receipts`). Leg: **C1_RECEIPTS**, sub-check "fetch_url host in HOST_ALLOWLIST". This reproduces the r96 finding; the receipt-delta side is unchanged: V27 (the only foreign-host delta) still fails C1_RECEIPTS, via `S502:fetch-log-line-missing`, so the allowlist is never the discriminator. V10 (fetched_at) is the other C1_RECEIPTS delta and does not touch the host. **Real coverage gap.** Routed-to-r97 vector per r96: a self-consistent receipt+body+fetch-log line under a non-allowlisted host. On base the host check is unreachable (no receipts), so the tree detector cannot see it.

4. **m059-cmp-check_sources-L341** (`not in sup` → `in sup`, supersedes map recording). Leg: **C1_SOURCES**, sub-check "terminal row of a superseded cited sid is mined". The registry has 36 `supersedes S…` rows, but none supersedes S002, S502, S503 or S504, the only sids the frozen entry cites (`C1_SOURCE_IDS`). So the chain code never runs for the frozen entry, and no delta cites a superseded sid. **Real coverage gap** (a supersedes chain with a non-mined terminal row would be the discriminator).

5. **m061-cmp-check_sources-L345** (`d < 10` → `d >= 10`, chain-follow loop). Leg: **C1_SOURCES** (same sub-check as 4). The loop never follows a supersede link, so the loop bound is untested. **Real coverage gap**, same cause as 4: no chain of depth ≥ 1 reaches a verdict-visible delta.

6. **m064-cmp-check_sources-L357** (`r[7] != "rejected"` → `==`, inside `if sid in REJECTED_OK:`). Leg: C1_SOURCES, rejected-expected sub-check. `REJECTED_OK = frozenset()` (line 45 of the counter), so the branch is unreachable for any input. **Equivalent mutant under the frozen constants**: no delta can kill it without changing a frozen constant. Finding: the counter carries one unreachable branch; it is not a missed attack.

7. **m079-if-check_embed_nonvacuous-L407** (negate `startswith("$") and not any(...)` in the fenced-block rule). Leg: **C1_EMBED_NONVACUOUS**, sub-check "a `$` command line inside a fence needs non-blank output after it". F18 (`$ cmd` + two whitespace-only lines) names the leg, but the mutant also flags the whitespace-only lines, so F18 still fails the leg. The honest entry has no fenced block, so POS cannot catch it either. **Real coverage gap**: needs a fence whose only content is a bare `$` line (must fail) or a `$` command followed by real output (must pass).

Net: four of the seven are real sub-check gaps (m029, d-host, m059/m061, m079); one is WHY-text-only (m011); one is equivalent under frozen constants (m064). Every leg in the survivor list has at least one self-test delta, so the gaps are sub-check gaps, not leg gaps.

## Harness gaps the L1 must know before scoring v6

- **C1_TRIO** has no comparison, `if` or `not`; it is `all(any(...))`. The harness reports `NO_SITE leg=C1_TRIO`. A delta exists (`TRIO-missing-recheck`), so the self-test covers it, but the mutation harness does not. Not added: a new mutation class would be a design choice outside the single-token-inversion scope.
- The WHY-text exclusion is structural (return-tuple slot only); m011 shows a WHY-only comparison can still get through. Treat WHY-only survivors as non-leg when reading v6 results.
- Anchors: v6 must keep the `LANE = Path(__file__).resolve().parents[2]` line and the `if host not in HOST_ALLOWLIST:` + host `fails.append` pair; otherwise the harness exits 2 (a deliberate refusal, not a silent pass).
- Function names drive attribution. Renamed `check_*` functions fall back to `UNATTRIBUTED` (counts unchanged, leg labels lost).
- The base archive detector is a weak instrument for sub-checks (see above). The self-test detector is the meaningful one; its strength is bounded by v6's own frozen self-test deltas, which the L1 must not edit after scoring.
- Fixtures: the counter's self-test builds fixtures from the lane's candidate entry bytes (candidate with `admission-status: admitted` substituted). That is a fixture, not the landing tree, and the claim is not scored here.

## Restoration and hygiene

- No lane file was edited. Mutants ran only in `/fast/scratch/hyaku/revenger-r97/MutationR97/` (deleted before yield after the receipts were copied). Every Python invocation used `python3 -B`; the counter's self-test scratch went to `HYAKU_SCRATCH=<scratch>/hyaku` (not the r96 path).
- No `git` mutation. Read-only only: `archive 7d380ce`, `rev-parse`, `cat-file`, `show`, `ls-tree`, `status --porcelain`.
- Counter bytes unchanged: `reports/round-96/c1_k_admit_counter5.py` sha256 `805ffb8aabbdbd451781dd831afce7ab41258979489d29ae789ae9fc1a23ad19` (checked before and after).

## Open questions for the L1

1. Use the self-test detector (union) as the calibration number; the base-archive count (81/117) is recorded as the spec's metric but is not the strength of the harness.
2. v6 should add a zero-PASS vote delta, a foreign-host self-consistent receipt delta (`d-host` vector), a superseded-cited-sid delta with a non-mined terminal row, and a bare-`$` fence delta, or the four real gaps above survive v6 too. Adding them changes the v6 self-test, so they must be in v6 before the freeze; I did not write them (scope: harness, not v6 deltas).

## Mutant verdicts (all 117; generated by the harness from the frozen v5)

"tree" = detector 1 on base archive (why: verdict-set = verdict line set changed; survived = no change; message-only = WHY text only). "self-test" = detector 2. "union" = killed by either.

| mutant | class | line | function | leg(s) | edit | tree (base 7d380ce) | self-test | union |
|---|---|---|---|---|---|---|---|---|
| m001-cmp-strict_json-L77 | cmp | 77 | strict_json | C1_RECEIPTS,C1_REGISTRY,C1_VOTES | `in -> not in` | verdict-set | KILLED | KILLED |
| m002-cmp-base_readme-L144 | cmp | 144 | base_readme | C1_ONLY_C02 | `!= -> ==` | survived | KILLED | KILLED |
| m003-if-base_readme-L153 | if | 153 | base_readme | C1_ONLY_C02 | `negate BoolOp test` | message-only | KILLED | KILLED |
| m004-cmp-base_readme-L153 | cmp | 153 | base_readme | C1_ONLY_C02 | `== -> !=` | survived | KILLED | KILLED |
| m005-not-parse_sources-L162 | not | 162 | parse_sources | C1_SIDS,C1_SOURCES | `delete `not`` | verdict-set | KILLED | KILLED |
| m006-if-parse_sources-L165 | if | 165 | parse_sources | C1_SIDS,C1_SOURCES | `negate if test` | verdict-set | KILLED | KILLED |
| m007-cmp-parse_sources-L167 | cmp | 167 | parse_sources | C1_SIDS,C1_SOURCES | `== -> !=` | verdict-set | KILLED | KILLED |
| m008-cmp-parse_sources-L168 | cmp | 168 | parse_sources | C1_SIDS,C1_SOURCES | `in -> not in` | verdict-set | KILLED | KILLED |
| m009-not-check_registry-L182 | not | 182 | check_registry | C1_REGISTRY | `delete `not`` | verdict-set | KILLED | KILLED |
| m010-cmp-check_registry-L187 | cmp | 187 | check_registry | C1_REGISTRY | `!= -> ==` | verdict-set | KILLED | KILLED |
| m011-cmp-check_registry-L190 | cmp | 190 | check_registry | C1_REGISTRY | `!= -> ==` | survived | survived | SURVIVED |
| m012-cmp-na_reason_ok-L197 | cmp | 197 | na_reason_ok | C1_VOTES | `>= -> <` | verdict-set | KILLED | KILLED |
| m013-cmp-na_reason_ok-L197 | cmp | 197 | na_reason_ok | C1_VOTES | `is not -> is` | verdict-set | KILLED | KILLED |
| m014-not-check_votes-L203 | not | 203 | check_votes | C1_VOTES | `delete `not`` | verdict-set | KILLED | KILLED |
| m015-not-check_votes-L211 | not | 211 | check_votes | C1_VOTES | `delete `not`` | verdict-set | KILLED | KILLED |
| m016-not-check_votes-L214 | not | 214 | check_votes | C1_VOTES | `delete `not`` | verdict-set | KILLED | KILLED |
| m017-if-check_votes-L214 | if | 214 | check_votes | C1_VOTES | `negate BoolOp test` | verdict-set | KILLED | KILLED |
| m018-cmp-check_votes-L214 | cmp | 214 | check_votes | C1_VOTES | `not in -> in` | verdict-set | KILLED | KILLED |
| m019-cmp-check_votes-L217 | cmp | 217 | check_votes | C1_VOTES | `in -> not in` | verdict-set | KILLED | KILLED |
| m020-cmp-check_votes-L220 | cmp | 220 | check_votes | C1_VOTES | `!= -> ==` | verdict-set | KILLED | KILLED |
| m021-cmp-check_votes-L222 | cmp | 222 | check_votes | C1_VOTES | `not in -> in` | verdict-set | KILLED | KILLED |
| m022-cmp-check_votes-L224 | cmp | 224 | check_votes | C1_VOTES | `!= -> ==` | verdict-set | KILLED | KILLED |
| m023-not-check_votes-L228 | not | 228 | check_votes | C1_VOTES | `delete `not`` | verdict-set | KILLED | KILLED |
| m024-cmp-check_votes-L228 | cmp | 228 | check_votes | C1_VOTES | `>= -> <` | verdict-set | KILLED | KILLED |
| m025-cmp-check_votes-L232 | cmp | 232 | check_votes | C1_VOTES | `== -> !=` | verdict-set | KILLED | KILLED |
| m026-cmp-check_votes-L234 | cmp | 234 | check_votes | C1_VOTES | `!= -> ==` | verdict-set | KILLED | KILLED |
| m027-not-check_votes-L237 | not | 237 | check_votes | C1_VOTES | `delete `not`` | verdict-set | KILLED | KILLED |
| m028-not-check_votes-L240 | not | 240 | check_votes | C1_VOTES | `delete `not`` | verdict-set | KILLED | KILLED |
| m029-cmp-check_votes-L240 | cmp | 240 | check_votes | C1_VOTES | `== -> !=` | survived | survived | SURVIVED |
| m030-not-check_votes-L245 | not | 245 | check_votes | C1_VOTES | `delete `not`` | verdict-set | KILLED | KILLED |
| m031-cmp-check_votes-L247 | cmp | 247 | check_votes | C1_VOTES | `in -> not in` | verdict-set | KILLED | KILLED |
| m032-not-check_votes-L252 | not | 252 | check_votes | C1_VOTES | `delete `not`` | verdict-set | KILLED | KILLED |
| m033-not-check_votes-L254 | not | 254 | check_votes | C1_VOTES | `delete `not`` | verdict-set | KILLED | KILLED |
| m034-if-check_votes-L257 | if | 257 | check_votes | C1_VOTES | `negate BoolOp test` | verdict-set | KILLED | KILLED |
| m035-cmp-check_votes-L257 | cmp | 257 | check_votes | C1_VOTES | `== -> !=` | verdict-set | KILLED | KILLED |
| m036-not-check_votes-L257 | not | 257 | check_votes | C1_VOTES | `delete `not`` | verdict-set | KILLED | KILLED |
| m037-not-check_votes-L259 | not | 259 | check_votes | C1_VOTES | `delete `not`` | verdict-set | KILLED | KILLED |
| m038-cmp-check_votes-L259 | cmp | 259 | check_votes | C1_VOTES | `== -> !=` | verdict-set | KILLED | KILLED |
| m039-cmp-check_votes-L262 | cmp | 262 | check_votes | C1_VOTES | `not in -> in` | verdict-set | KILLED | KILLED |
| m040-cmp-check_votes-L264 | cmp | 264 | check_votes | C1_VOTES | `not in -> in` | verdict-set | KILLED | KILLED |
| m041-if-check_votes-L266 | if | 266 | check_votes | C1_VOTES | `negate BoolOp test` | verdict-set | KILLED | KILLED |
| m042-cmp-check_votes-L266 | cmp | 266 | check_votes | C1_VOTES | `in -> not in` | verdict-set | KILLED | KILLED |
| m043-cmp-check_votes-L266 | cmp | 266 | check_votes | C1_VOTES | `in -> not in` | verdict-set | KILLED | KILLED |
| m044-cmp-check_votes-L271 | cmp | 271 | check_votes | C1_VOTES | `< -> >=` | verdict-set | KILLED | KILLED |
| m045-if-check_receipts-L280 | if | 280 | check_receipts | C1_RECEIPTS | `negate if test` | verdict-set | KILLED | KILLED |
| m046-cmp-check_receipts-L290 | cmp | 290 | check_receipts | C1_RECEIPTS | `!= -> ==` | verdict-set | KILLED | KILLED |
| m047-cmp-check_receipts-L292 | cmp | 292 | check_receipts | C1_RECEIPTS | `!= -> ==` | verdict-set | KILLED | KILLED |
| d-host | d-host | 295 | check_receipts | C1_RECEIPTS | `host allowlist sub-check removed (MutationR96 d-host)` | survived | survived | SURVIVED |
| m049-cmp-check_receipts-L295 | cmp | 295 | check_receipts | C1_RECEIPTS | `not in -> in` | verdict-set | KILLED | KILLED |
| m050-not-check_receipts-L298 | not | 298 | check_receipts | C1_RECEIPTS | `delete `not`` | verdict-set | KILLED | KILLED |
| m051-cmp-check_receipts-L301 | cmp | 301 | check_receipts | C1_RECEIPTS | `!= -> ==` | verdict-set | KILLED | KILLED |
| m052-cmp-check_receipts-L303 | cmp | 303 | check_receipts | C1_RECEIPTS | `in -> not in` | verdict-set | KILLED | KILLED |
| m053-cmp-check_receipts-L303 | cmp | 303 | check_receipts | C1_RECEIPTS | `in -> not in` | verdict-set | KILLED | KILLED |
| m054-not-check_receipts-L305 | not | 305 | check_receipts | C1_RECEIPTS | `delete `not`` | verdict-set | KILLED | KILLED |
| m055-not-check_receipts-L307 | not | 307 | check_receipts | C1_RECEIPTS | `delete `not`` | verdict-set | KILLED | KILLED |
| m056-cmp-check_sids-L328 | cmp | 328 | check_sids | C1_SIDS | `not in -> in` | verdict-set | KILLED | KILLED |
| m057-not-check_sids-L330 | not | 330 | check_sids | C1_SIDS | `delete `not`` | verdict-set | KILLED | KILLED |
| m058-if-check_sources-L341 | if | 341 | check_sources | C1_SOURCES | `negate BoolOp test` | verdict-set | KILLED | KILLED |
| m059-cmp-check_sources-L341 | cmp | 341 | check_sources | C1_SOURCES | `not in -> in` | survived | survived | SURVIVED |
| m060-cmp-check_sources-L345 | cmp | 345 | check_sources | C1_SOURCES | `in -> not in` | verdict-set | KILLED | KILLED |
| m061-cmp-check_sources-L345 | cmp | 345 | check_sources | C1_SOURCES | `< -> >=` | survived | survived | SURVIVED |
| m062-not-check_sources-L353 | not | 353 | check_sources | C1_SOURCES | `delete `not`` | message-only | KILLED | KILLED |
| m063-cmp-check_sources-L356 | cmp | 356 | check_sources | C1_SOURCES | `in -> not in` | message-only | KILLED | KILLED |
| m064-cmp-check_sources-L357 | cmp | 357 | check_sources | C1_SOURCES | `!= -> ==` | survived | survived | SURVIVED |
| m065-cmp-check_sources-L362 | cmp | 362 | check_sources | C1_SOURCES | `is -> is not` | message-only | KILLED | KILLED |
| m066-cmp-check_sources-L364 | cmp | 364 | check_sources | C1_SOURCES | `!= -> ==` | message-only | KILLED | KILLED |
| m067-not-check_sources-L368 | not | 368 | check_sources | C1_SOURCES | `delete `not`` | message-only | KILLED | KILLED |
| m068-cmp-check_sources-L371 | cmp | 371 | check_sources | C1_SOURCES | `!= -> ==` | message-only | KILLED | KILLED |
| m069-cmp-check_sources-L373 | cmp | 373 | check_sources | C1_SOURCES | `!= -> ==` | message-only | KILLED | KILLED |
| m070-cmp-check_sources-L375 | cmp | 375 | check_sources | C1_SOURCES | `!= -> ==` | message-only | KILLED | KILLED |
| m071-cmp-check_sources-L377 | cmp | 377 | check_sources | C1_SOURCES | `not in -> in` | message-only | KILLED | KILLED |
| m072-cmp-check_sources-L379 | cmp | 379 | check_sources | C1_SOURCES | `!= -> ==` | message-only | KILLED | KILLED |
| m073-cmp-check_sources-L380 | cmp | 380 | check_sources | C1_SOURCES | `!= -> ==` | verdict-set | KILLED | KILLED |
| m074-not-check_sources-L382 | not | 382 | check_sources | C1_SOURCES | `delete `not`` | verdict-set | KILLED | KILLED |
| m075-cmp-check_quotes-L386 | cmp | 386 | check_quotes | C1_QUOTES | `in -> not in` | verdict-set | KILLED | KILLED |
| m076-not-check_quotes-L387 | not | 387 | check_quotes | C1_QUOTES | `delete `not`` | verdict-set | KILLED | KILLED |
| m077-cmp-check_quotes-L392 | cmp | 392 | check_quotes | C1_QUOTES | `!= -> ==` | verdict-set | KILLED | KILLED |
| m078-cmp-check_quotes-L395 | cmp | 395 | check_quotes | C1_QUOTES | `not in -> in` | verdict-set | KILLED | KILLED |
| m079-if-check_embed_nonvacuous-L407 | if | 407 | check_embed_nonvacuous | C1_EMBED_NONVACUOUS | `negate BoolOp test` | survived | survived | SURVIVED |
| m080-not-check_embed_nonvacuous-L407 | not | 407 | check_embed_nonvacuous | C1_EMBED_NONVACUOUS | `delete `not`` | survived | KILLED | KILLED |
| m081-if-check_embed_nonvacuous-L411 | if | 411 | check_embed_nonvacuous | C1_EMBED_NONVACUOUS | `negate if test` | survived | KILLED | KILLED |
| m082-not-check_embed_nonvacuous-L413 | not | 413 | check_embed_nonvacuous | C1_EMBED_NONVACUOUS | `delete `not`` | verdict-set | KILLED | KILLED |
| m083-not-check_pycache-L422 | not | 422 | check_pycache | C1_PYCACHE | `delete `not`` | survived | KILLED | KILLED |
| m084-not-check_pycache-L426 | not | 426 | check_pycache | C1_PYCACHE | `delete `not`` | verdict-set | KILLED | KILLED |
| m085-if-check_admitted_union-L437 | if | 437 | check_admitted_union | C1_ADMITTED_UNION | `negate BoolOp test` | verdict-set | KILLED | KILLED |
| m086-cmp-check_admitted_union-L437 | cmp | 437 | check_admitted_union | C1_ADMITTED_UNION | `== -> !=` | verdict-set | KILLED | KILLED |
| m087-if-check_admitted_union-L443 | if | 443 | check_admitted_union | C1_ADMITTED_UNION | `negate if test` | survived | KILLED | KILLED |
| m088-if-check_admitted_union-L450 | if | 450 | check_admitted_union | C1_ADMITTED_UNION | `negate if test` | verdict-set | KILLED | KILLED |
| m089-cmp-check_admitted_union-L452 | cmp | 452 | check_admitted_union | C1_ADMITTED_UNION | `not in -> in` | verdict-set | KILLED | KILLED |
| m090-not-check_admitted_union-L455 | not | 455 | check_admitted_union | C1_ADMITTED_UNION | `delete `not`` | verdict-set | KILLED | KILLED |
| m091-cmp-evaluate-L465 | cmp | 465 | evaluate | C1_ROWS_TOTAL | `== -> !=` | verdict-set | KILLED | KILLED |
| m092-cmp-evaluate-L466 | cmp | 466 | evaluate | C1_ROWS_TOTAL | `== -> !=` | verdict-set | KILLED | KILLED |
| m093-cmp-evaluate-L467 | cmp | 467 | evaluate | C1_C02_HELD | `== -> !=` | verdict-set | KILLED | KILLED |
| m094-cmp-evaluate-L468 | cmp | 468 | evaluate | C1_C02_HELD | `== -> !=` | verdict-set | KILLED | KILLED |
| m095-cmp-evaluate-L470 | cmp | 470 | evaluate | C1_C02_CITES | `== -> !=` | verdict-set | KILLED | KILLED |
| m096-if-evaluate-L476 | if | 476 | evaluate | C1_ONLY_C02 | `negate if test` | survived | KILLED | KILLED |
| m097-if-evaluate-L478 | if | 478 | evaluate | C1_ONLY_C02 | `negate BoolOp test` | message-only | KILLED | KILLED |
| m098-cmp-evaluate-L478 | cmp | 478 | evaluate | C1_ONLY_C02 | `!= -> ==` | survived | KILLED | KILLED |
| m099-cmp-evaluate-L478 | cmp | 478 | evaluate | C1_ONLY_C02 | `!= -> ==` | message-only | KILLED | KILLED |
| m100-not-evaluate-L480 | not | 480 | evaluate | C1_ONLY_C02 | `delete `not`` | survived | KILLED | KILLED |
| m101-cmp-evaluate-L480 | cmp | 480 | evaluate | C1_ONLY_C02 | `is not -> is` | survived | KILLED | KILLED |
| m102-cmp-evaluate-L481 | cmp | 481 | evaluate | C1_ONLY_C02 | `!= -> ==` | verdict-set | KILLED | KILLED |
| m103-cmp-evaluate-L489 | cmp | 489 | evaluate | C1_ADMITTED | `== -> !=` | survived | KILLED | KILLED |
| m104-cmp-evaluate-L489 | cmp | 489 | evaluate | C1_ADMITTED | `< -> >=` | survived | KILLED | KILLED |
| m105-cmp-evaluate-L490 | cmp | 490 | evaluate | C1_ADMITTED | `== -> !=` | verdict-set | KILLED | KILLED |
| m106-if-evaluate-L506 | if | 506 | evaluate | C1_LINT | `negate if test` | verdict-set | KILLED | KILLED |
| m107-cmp-evaluate-L511 | cmp | 511 | evaluate | C1_LINT | `== -> !=` | verdict-set | KILLED | KILLED |
| m108-cmp-evaluate-L513 | cmp | 513 | evaluate | C1_EMBEDDED | `== -> !=` | survived | KILLED | KILLED |
| m109-cmp-evaluate-L513 | cmp | 513 | evaluate | C1_EMBEDDED | `== -> !=` | verdict-set | KILLED | KILLED |
| m110-cmp-evaluate-L514 | cmp | 514 | evaluate | C1_EMBEDDED | `in -> not in` | verdict-set | KILLED | KILLED |
| m111-not-evaluate-L515 | not | 515 | evaluate | C1_EMBEDDED | `delete `not`` | verdict-set | KILLED | KILLED |
| m112-if-evaluate-L534 | if | 534 | evaluate | C1_K_HELD_BACKED | `negate BoolOp test` | verdict-set | KILLED | KILLED |
| m113-cmp-evaluate-L534 | cmp | 534 | evaluate | C1_K_HELD_BACKED | `== -> !=` | verdict-set | KILLED | KILLED |
| m114-cmp-evaluate-L536 | cmp | 536 | evaluate | C1_K_HELD_BACKED | `== -> !=` | verdict-set | KILLED | KILLED |
| m115-if-_raw_line-L559 | if | 559 | _raw_line | C1_ONLY_C02 | `negate BoolOp test` | message-only | KILLED | KILLED |
| m116-cmp-_raw_line-L559 | cmp | 559 | _raw_line | C1_ONLY_C02 | `== -> !=` | message-only | KILLED | KILLED |
| m117-cmp-_raw_line-L559 | cmp | 559 | _raw_line | C1_ONLY_C02 | `== -> !=` | message-only | KILLED | KILLED |
