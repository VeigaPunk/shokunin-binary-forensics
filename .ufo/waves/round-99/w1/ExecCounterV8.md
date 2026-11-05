# ExecCounterV8 — round 99, wave w1 — findings

Seat: ExecCounterV8 (executor, leaf). Lane: /home/vgpnk/Projects/shokunin/revenger-shokunin.

## Deliverable

- `reports/round-99/c1_k_admit_counter8.py`
  - **final sha256 `620dfca9959572449638cab203485555c5d45f5a8e89c5b68121ffc2d3023581`**
  - Built as a byte copy of frozen v7 (`reports/round-98/c1_k_admit_counter7.py`, sha256 `59c9930a…`, not edited) and then edited in place.
  - Superseded WIP shas, for the record: `a8a64ee1…` (before c14r99 pin check), `c7a9a2c2…` (before host-only case).

## What v8 adds

- **Profiles.** `--profile {c02|c14|c14r99}`. `c02` and `c14` keep the v7 constants. `c14r99` = v7 c14 constants except:
  - `VOTES_DIR = reports/round-99/votes`
  - `WAVE_DIR = .ufo/waves/round-99`
  - `REGISTRY_REL = .ufo/waves/round-99/w1/swarm-registry.json`
  - `FREEZE_REV = 61e27feb4e8099af7f9bf41fbf69e223354f691e` (Amendment A commit per `claims.md`; the contract text said 7e6edd4, which Amendment A supersedes. README bytes are identical at both.)
  - `ARCHIVE_PATHS` = c14 list + `reports/round-99`, `.ufo/waves/round-99`
  - `PINNED_SEATS` = the round-99 map from the contract
  - Two per-profile constants, `ROUND_RECORD_DIR` (round-96 for c02; round-98 for both c14 profiles, since the scored entry is round-98) and `FIXTURE_VOTE_SEATS`. `C14_FAMILY = (c14, c14r99)` replaces the old `PROFILE == "c14"` tests.
  - Scratch root: `revenger-r99/c1v8`.
- **Nine new legs.** Each is a `new_checks()` entry, so it is wired into `C1_VERDICT` and prints `C1_<LEG>=` and `<LEG>_WHY=`. All apply in all three profiles.

| Leg | Check | Survivor killed |
|---|---|---|
| `C1_VOTES_GLOB` | every regular file in VOTES_DIR is `[A-Za-z0-9_-]+\.json` | c02 V01 |
| `C1_NA_REASON` | every n/a reason has ≥6 tokens that are not Q-ids or bare punctuation | c02 V02 |
| `C1_RECHECK_CMD` | each `recheck:` value has a backticked command (≥3 chars) or a re-verify verb plus path/URL | c02 E01 |
| `C1_HEX_CLAUSES` | Q14 generalised: each N-byte count (N≤32) matches the nearest backticked hex run; truncated runs carry no count; 40/64/128-digit runs excluded | c02 E02 |
| `C1_COVMAP_ROW` | `coverage-map:` id == TARGET_ROW, exactly one such header | c02 E03 |
| `C1_ROW_IDS` | every README row whose first cell is `C\d+\w*` is exactly C01..C15 | c14 R01 |
| `C1_DECISION_KEYS` | every vote's decisions keys == Q01..Q17 | c14 V02 |
| `C1_OWNWORK_ROUND` | own-work source rows of NEW_ROW_IDS point only into ROUND_RECORD_DIR | c14 O01 |
| `C1_FETCHLOG_DATE` | a date in the fetch-log header line 1 equals each RECEIPT_ROW_IDS `fetched_at`; no date in header → pass | c14 L01 |

- **Self-test.** `SELFTEST_C1V8=OK legs=98`, rc 0.
  - v7 cases run in all three profiles.
  - Each of the nine new legs has a red delta (`_v8_delta`) run in all three profiles.
  - **Host-only case V27b** (`_host_only_delta`, requested by MutationR99): only the first receipt's `fetch_url` host changes. Expects `C1_RECEIPTS=fail` and `check_receipts` WHY exactly `S502:host:'dlang.org'` (c14 family: `S506`). Verified in the c02 receipt log.
  - Honest trees pass in all three profiles. The do-nothing archive fails in all three.
  - **Pin check** for c14r99 `VOTES_DIR`, `WAVE_DIR`, `REGISTRY_REL`, `FREEZE_REV`, `PINNED_SEATS`, so a constant flip fails the self-test (honest fixtures are built from the same constants and would otherwise not catch it).
- **Fixture changes.** `_fixture` seats come from `FIXTURE_VOTE_SEATS`. The S505 correction is c14-only (at the Amendment-A commit S505 is mined with a round-97 used-by). The v7 `C1_VOTE_NOTES` delta targets `FIXTURE_VOTE_SEATS[0]`.

## Verification (exit codes observed, final bytes `620dfca9…`)

- `python3 -B reports/round-99/c1_k_admit_counter8.py --self-test --work <S>/st --receipts-dir <S>/rc` → **rc 0**, `SELFTEST_C1V8=OK legs=98`. Receipts: `.ufo/waves/round-99/w1/ExecCounterV8/selftest/`.
  - Each red delta logs `C1_VERDICT=fail` with its own leg `=fail`.
  - Honest logs `c02`, `c14`, `c14r99` → `C1_VERDICT=pass`.
  - Do-nothing logs → `C1_VERDICT=fail`.
- Holdout (frozen builder via scratch copy with `parity-patch.diff` applied, `--lane` = lane root, final v8 bytes). Logs under `red-before/v8/`.
  - v8 `--profile c02` → rc 0, `HOLDOUT98_CONTROL=control-ok`, `accepted=0/6`.
  - v8 `--profile c14` → rc 0, `HOLDOUT98_CONTROL=control-ok`, `accepted=0/6`.
  - Total v8: 0/12.
  - v7 (earlier run, unchanged frozen bytes): c02 5/6 and c14 4/6, total 9/12, both `control-ok`; logs `red-before/v7/`.
- Red-before per vector (v7 → v8):

  | Vector | v7 | v8 refusing leg(s) |
  |---|---|---|
  | c02 V01 | ACCEPTED | C1_VOTES_GLOB |
  | c02 V02 | ACCEPTED | C1_NA_REASON |
  | c02 E01 | ACCEPTED | C1_RECHECK_CMD |
  | c02 E02 | ACCEPTED | C1_HEX_CLAUSES |
  | c02 E03 | ACCEPTED | C1_COVMAP_ROW |
  | c02 R01 | refused (C1_ONLY_TARGET, C1_ADMITTED_UNION) | same |
  | c14 R01 | ACCEPTED | C1_ROW_IDS |
  | c14 V01 | refused (C1_VOTE_NOTES) | same |
  | c14 V02 | ACCEPTED | C1_DECISION_KEYS |
  | c14 Q01 | refused (C1_QUOTES) | same |
  | c14 O01 | ACCEPTED | C1_OWNWORK_ROUND |
  | c14 L01 | ACCEPTED | C1_FETCHLOG_DATE |

- C2 harness, `reports/round-98/forge_reach7.py --counter reports/round-99/c1_k_admit_counter8.py --profile c02` → **rc 0**, `C2_ACCEPTED=0/5`, both positives pass, stub ok, `C2_VERDICT=met`. Receipt: `forge_reach7-v8-c02.out`. `C1_ROW_IDS` also fires on the FR06/FR07 ROWSET harness deltas, which v7 already refused via `C1_ROWSET`; no calibration harm.
- `reports/round-99/forge_reach8.py --counter reports/round-99/c1_k_admit_counter8.py --work <S>/fr8` → **rc 0**, `C2_ACCEPTED=0/12`, `C2_CONTROL_C02=control-ok`, `C2_CONTROL_C14=control-ok`, `C2_STUB_SELFTEST=ok`, `C2_VERDICT=met`. Receipt: `forge_reach8-final.out`.
  - Note: ExecHarness8 reported 9/12 on WIP sha `6db14795…`, which is not the current file; on current bytes the result is 0/12. I told them.
- No-false-positive check, in-process calls to the nine leg functions on real `reports/round-96/votes`, `reports/round-98/votes`, both knowledge entries, README and round-98 SOURCES/receipts: all return ok, including `C1_NA_REASON` on every r98 n/a note. No counter run on any tree for this check.

## Disclosures and open questions for the L1

1. **c14r99 on synthesized trees with C14 held.** The self-test runs c14r99 on fixtures synthesized from the claims-freeze archive, where C14 is held. The contract requires an honest c14r99 fixture to pass; v7 self-tests c14 the same way. I did not run c14r99 on any real landing tree. Please rule on whether this self-test use is acceptable under "no counter on a C14-held tree". The c14 holdout trees (profile c14, frozen v7 constants) are also C14-held development fixtures.
2. **FREEZE_REV** is the Amendment A commit 61e27feb, not 7e6edd4. Please confirm.
3. **C1_FETCHLOG_DATE** parses only line 1 of the fetch log; a header with no date passes (the c02 fixture header is `# fetch log (fixture)`). Removing a date rather than changing it is not caught.
4. **ConnectorR99 R-a…R-i.** Adopted: R-a (lowercase `.json` extension; mixed-case stems allowed, since honest files are `ReviewerGate.json`), R-c, R-d, R-e (as coverage-map == TARGET_ROW, not a README binding), R-f, R-g, R-h, R-i. R-b: I used the contract's literal rule (≥6 non-Q-id, non-punctuation tokens) without the stopword list. The stopword list would be stricter but the contract does not require it.
5. **Residual debt.** `check_c14_digests` still hard-codes `corpus/live/runs/round-98`, identical to `ROUND_RECORD_DIR` for both c14 profiles. Left as is.
6. **Constant mutants.** `FREEZE_REV` variants that leave README and entry bytes identical are indistinguishable to every leg; only the pin check in self-test catches them. MutationR99 should confirm that detector.

## Tools

No tools installed or updated. No pacman, uv, npm or cargo actions.

## Coordination

- Leg names agreed with ExecHarness8 and MutationR99 (no objections).
- Final sha sent to MutationR99, ExecHarness8 and ExecControlsR99.
- Subagents: none spawned; no labrat probe used.

## Checks for the main agent after integration

- `python3 -B reports/round-99/c1_k_admit_counter8.py --self-test` → expect rc 0, `SELFTEST_C1V8=OK legs=98`.
- `forge_reach7.py --counter reports/round-99/c1_k_admit_counter8.py --profile c02` → expect `C2_ACCEPTED=0/5`, `C2_VERDICT=met`.
- `forge_reach8.py --counter reports/round-99/c1_k_admit_counter8.py` → expect `C2_ACCEPTED=0/12`, both controls and stub ok, `C2_VERDICT=met`.
- Freeze-order steps for c14r99 (do-nothing and junk-row controls, then landing) are the L1's, after the v8 commit.
