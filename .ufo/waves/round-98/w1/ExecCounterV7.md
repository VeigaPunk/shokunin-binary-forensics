# ExecCounterV7 — round 98 w1

Axes: coverage and calibration. Scoped implementation complete; development-set evidence only.
No landing tree was built/scored, no lane corpus/status/README was edited, and no git mutation was used.

## Implementation

New counter: `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/c1_k_admit_counter7.py`
SHA256: `59c9930ae864ce826e9f468b4b76bdef33de7ae5e6760eda4d88db4eab2e8548`.
Started from all frozen v6 bytes, retaining inherited checks and c02 constants; v6 was not edited.
CLI requires `--profile c02|c14` outside `--self-test` (missing profile observed exit 2).
Eight new checks emit named WHY lines; verdict remains the last output line.
C14 profile pins all twelve seats, the supplied freeze, source rows, paths and held target.

Amendment A implemented: used-by grounding is scoped to c02 S502/S503/S504 or c14
S505/S506/S507; PASS-note length/style/uniqueness applies to c14 only; both profiles
refuse Q09 n/a on an entry with a 64-hex digest claim. C14 derivation checks independently
rehash the ZIP fixture, S506 body and every saved record's 8-hex prefix. C02 one-row rule
is unchanged (no C14 exemption).

Amendment B implemented in the c14 honest fixture: copy the current real entry, with its
L1-added Q-map, rather than synthesize one. Candidate normalized digest observed:
`73f1d7e044df04373a36c1f94f7e7216a7a513043ef769d5567a98cb53dd80e7`.
README baseline remains 9d49002a3804de48d365b7d32849ada06745d64f.

All 28 admission legs (plus final C1_VERDICT):
- `C1_ROWS_TOTAL`
- `C1_TARGET_HELD`
- `C1_TARGET_CITES`
- `C1_ONLY_TARGET`
- `C1_DERIV_TABLE`
- `C1_ADMITTED_WS`
- `C1_ADMITTED`
- `C1_TRIO`
- `C1_REGISTRY`
- `C1_VOTES`
- `C1_RECEIPTS`
- `C1_PYCACHE`
- `C1_ADMITTED_UNION`
- `C1_LINT`
- `C1_EMBEDDED`
- `C1_EMBED_NONVACUOUS`
- `C1_SIDS`
- `C1_SOURCES`
- `C1_QUOTES`
- `C1_K_HELD_BACKED`
- `C1_ROWSET`
- `C1_ENTRY_BYTES`
- `C1_HEADER_POSITION`
- `C1_VERIFIED_AT`
- `C1_VOTE_NOTES`
- `C1_OWNWORK_PATHS`
- `C1_QUOTE_BYTES`
- `C1_USEDBY_GROUNDED`

## Required outputs and exits

`python3 -B <counter> --self-test --work <seat-scratch> --receipts-dir <v7-dev>/selftest-cases`
printed `SELFTEST_C1V7=OK legs=55`, exit **0**. Cases are both honest profiles, eight
new-leg deltas in each, every inherited v6 negative delta in c02, three independent c14
derivation digest mutations, and both do-nothing freeze controls. Honest c14 is a
DEVELOPMENT FIXTURE, not a landing measurement: synthetic registry/votes and fixture-only
S505 queued/no-used-by correction. Its admission/coverage flip exists only in scratch.

R97 builder copied into seat scratch, preserving every mutator. Only COUNTER, explicit
work arguments, and c02 invocation/logging arguments changed. Frozen builder was not edited.

- v6 builder exit 0: `BUILD_OK=True vectors=15 accepted=5`.
- v7 builder exit 0: `BUILD_OK=True vectors=15 accepted=0`.
- No `forge_reach7.py` harness or landing scoring was run by this seat.

| Vector | v6 exit | v7 exit | v7 new refusing leg |
|---|---:|---:|---|
| FR00-honest-control | 0 | 0 | positive: C1_VERDICT=pass |
| FR02-entry-leading-bom | 0 | 1 | C1_ENTRY_BYTES |
| FR06-row-dup-held-over-held | 1 | 1 | C1_ROWSET |
| FR07-row-dup-target-over-held | 1 | 1 | C1_ROWSET |
| FR08-headers-in-fence | 0 | 1 | C1_HEADER_POSITION |
| FR09-verified-at-stale | 0 | 1 | C1_VERIFIED_AT |
| FR10-na-boilerplate-on-pass | 0 | 1 | C1_VOTE_NOTES (Q09 applicability) |
| FR12-own-work-dangling | 0 | 1 | C1_OWNWORK_PATHS |

V6 FR06/FR07 failed only incidentally via C1_ADMITTED_UNION. V7 explicitly refuses both
via C1_ROWSET. FR10's actual mutator changes ReviewerGate Q09 PASS to n/a, not a PASS
note; the applicability rule is the named mechanism.

Isolated grounding controls: the freeze archive has exactly one failing scoped pair,
S505 → corpus/knowledge/round-96-native-analysis-sessions.md (entry does not cite S505),
probe process exit 1. Changing only scratch S505 used-by to — and status to queued makes
that leg pass, exit 0. The base34 S505-only probe independently gives exits 1 then 0;
it intentionally does NOT assert registry-wide validation after Amendment A.
C1_QUOTE_BYTES positives explicitly check S505 and S507 byte anchors in c14.

Full c14 on the unchanged claims-freeze archive (C14 partial), exit 1, fails:
- `C1_TARGET_HELD`
- `C1_TARGET_CITES`
- `C1_ONLY_TARGET`
- `C1_ADMITTED`
- `C1_REGISTRY`
- `C1_VOTES`
- `C1_LINT`
- `C1_K_HELD_BACKED`
- `C1_VOTE_NOTES`
- `C1_USEDBY_GROUNDED`
- `C1_VERDICT`

## Retained receipts (absolute paths, actual process/case exits)

Self-test case exit is the evaluated counter verdict mapped to 0/1 in-process;
all other numbered exits below are observed subprocess exits. JSON files are data.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/c02-record-supplement.json` — data.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/c14-claims-freeze.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/harness-v6.log` — exits not recorded (diagnostic log).
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/self-test-first-run.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/self-test-pre-amendment-B.log` — exits 0.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/self-test.log` — exits 0.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-A3-usedby-extra.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-A4-shadow-admitted.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-C1_ENTRY_BYTES.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-C1_HEADER_POSITION.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-C1_OWNWORK_PATHS.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-C1_QUOTE_BYTES.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-C1_ROWSET.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-C1_USEDBY_GROUNDED.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-C1_VERIFIED_AT.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-C1_VOTE_NOTES.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-DECOR-shadow-admitted.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-EMBEDDED-fake-fence.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-F10-dup-status-fenced.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-F12-case-dup-seat.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-F13-role-mismatch.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-F15-traversal.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-F16-unresolved-body-sid.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-F17-vacuous-na.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-F18-ws-output.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-F18b-tilde-fence.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-F19-stale-new-row.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-F20-foreign-artifact-dir.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-H1-indent-dup-status.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-KHELDBACK-broken-cell.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-LINT-qmap-missing-row.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-M5-pycache-planted.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-M6-forged-registry-seat.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-M8-pycache-frozen-dir.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-ONLY-C10-second-row.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-QUOTES-mutated-body.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-ROWS-total-extra-row.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-TRIO-missing-recheck.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-V03-dup-json-keys-registry.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-V04-dup-json-keys-vote.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-V07-legacy-path.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-V08-entry-pending.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-V10-stale-fetched-at.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-V18-na-letter-flood.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-V19-sid-suffix-spaced.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-V27-fabricated-body-foreign-host.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-do-nothing.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c02-honest.log` — exits 0.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c14-C1_ENTRY_BYTES.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c14-C1_HEADER_POSITION.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c14-C1_OWNWORK_PATHS.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c14-C1_QUOTE_BYTES.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c14-C1_ROWSET.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c14-C1_USEDBY_GROUNDED.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c14-C1_VERIFIED_AT.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c14-C1_VOTE_NOTES.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c14-DERIV-body.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c14-DERIV-fixture.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c14-DERIV-record.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c14-do-nothing.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/selftest-cases/c14-honest.log` — exits 0.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/usage-no-profile.log` — exits 2.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/usedby-base34.log` — exits 1, 0.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/usedby-freeze.log` — exits 1, 0.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/v6-FR00-honest-control.log` — exits 0.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/v6-FR02-entry-leading-bom.log` — exits 0.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/v6-FR06-row-dup-held-over-held.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/v6-FR07-row-dup-target-over-held.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/v6-FR08-headers-in-fence.log` — exits 0.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/v6-FR09-verified-at-stale.log` — exits 0.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/v6-FR10-na-boilerplate-on-pass.log` — exits 0.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/v6-FR12-own-work-dangling.log` — exits 0.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/v6-builder.log` — exits 0.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/v6-results.json` — data.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/v7-FR00-honest-control.log` — exits 0.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/v7-FR02-entry-leading-bom.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/v7-FR06-row-dup-held-over-held.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/v7-FR07-row-dup-target-over-held.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/v7-FR08-headers-in-fence.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/v7-FR09-verified-at-stale.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/v7-FR10-na-boilerplate-on-pass.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/v7-FR12-own-work-dangling.log` — exits 1.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/v7-builder.log` — exits 0.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-98/controls/v7-dev/v7-results.json` — data.

## Fixture record supplement (L1-approved)

The 2875b9c c02 freeze predates its cited round-96 record. V7 _fixture copies these real
unchanged committed record bytes into scratch; builder mutations stay intact.

- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-96/codeable-decompiled.c` — `d717b49156faa1a627a5577a35ab7c158b103bd6adf31ee7ab5428abae3afc9d`.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-96/ghidra-headless-r96.log` — `6ce217fa48a0b4426e55de550b29f6d259abbe3c89fa8dd603265708d033f0f6`.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-96/rea-decompile.raw.txt` — `2fba7fbfc4439cacc0991e1c22e9ac74cbba526e2980ae791289cd2d1df07b41`.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-96/rea-doctor-r96.txt` — `6a1d18c3497f3d4560c581906184aa96f6f71188ab491d9a75d937df65cdc80f`.

## Other retained files

- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-98/w1/ExecCounterV7/development-builder-v6.txt` — exact copied development driver, data.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-98/w1/ExecCounterV7/development-builder-v7.txt` — exact copied development driver, data.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-98/w1/ExecCounterV7/receipt-manifest.sha256` — full receipt checksum inventory.
- This findings file: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-98/w1/ExecCounterV7.md`.

## Findings, risks, boundaries

Initial self-test exit 1 exposed missing c02 fixture record bytes and the real frozen c14
candidate's absent Q-map. Exact candidate diagnostic was `LINT_QMAP=17 ['Q01', 'Q02',
'Q03', 'Q04', 'Q05', 'Q06', 'Q07', 'Q08', 'Q09', 'Q10', 'Q11', 'Q12', 'Q13', 'Q14',
'Q15', 'Q16', 'Q17']; LINT_Q14=0; LINT_Q15=0; LINT_HEADER=0`.
L1 approved the fixture supplement and corrected the candidate under Amendment B; I did not
edit it. Original failure receipt retained. The original claims-freeze deliberately remains
an expected failure. No result here proves real admission, non-author closure, or unseen
holdout discrimination; L1 owns freeze and post-integration gates. All forgery results here
are disclosed development-set measurements.

No packages installed or updated. No LSP tool was mounted in this seat, so supported-symbol
navigation/refactor service was unavailable; text inspection was used (not a cold empty LSP
response). No build, formatter, general linter suite, host configuration change or external
substrate mutation was run. Only the requested counter/self-test/builder/probes ran; inherited
counter legs invoke their own lint/embedded/quote checkers.

Self-evaluation: accuracy 4 (observed rc/logs, but no independent holdout); completeness 4
(scoped deliverables complete, real admission intentionally unscored); clarity 4 (exhaustive
receipt inventory is long); actionability 4 (L1 still must freeze/run integration gates);
conciseness 4 (full paths required). Mean 4.0. Highest-impact next action belongs to L1:
freeze these bytes before any landing/holdout scoring. User agreement check: development
success is explicitly separated from real C14 admission.

Scratch cleanup EXIT trap completed with process exit 0.
