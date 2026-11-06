# CriticR100 findings: round 100, wave w1 (critic, leaf)

Lane: revenger, round 100 attempt 1. Frozen instrument commit `173abe91a80d79336ca9228643c63d41e0e7635c`
(the `FROZEN` file names it). Scoring of the C1 target run and the C2 target run is the L1's; the runs below
are attack re-runs and the milestone fresh holdout, reported and not targets.

## Scope and what was built

- Builder (pre-FROZEN, build-only, no counter run before FROZEN):
  `.ufo/waves/round-100/w1/CriticR100/fresh/build_fresh100.py`, sha256 `6f6b923e137a2dbaacab538aa9070fd69537a271ecdd9d3dd64d5e4101e38112`.
  Modelled on the frozen r99 builder; same table, `HOLDOUT100_CONTROL=`, `HOLDOUT100 accepted=<n>/<m>`.
- Eight new forgery classes, four per profile, each with one honest control per profile. Classes are not
  r96 FG01-FG20, r97 FR01-FR12, r98 holdout or r99 N1-N6. Vectors were not shown to any builder seat; I sent no messages (no BUILT line, since this seat builds no instrument).
- Frozen bytes used for every run: `git archive 173abe91` extracted to scratch, then a scratch `git init`
  fixture whose object store is the lane's via `objects/info/alternates` (read-only use of the lane; no
  clone, checkout, commit or reset). The counter reads `LANE` from its own location, so the frozen bytes must
  sit in a git repo for `base_readme` to work (see the invalid first run below).
  - v8 `reports/round-99/c1_k_admit_counter8.py` sha256 `620dfca9959572449638cab203485555c5d45f5a8e89c5b68121ffc2d3023581` (matches claims.md).
  - v9 `reports/round-100/c1_k_admit_counter9.py` sha256 `8e2eafc80726789aafa2ee491123de8b46ac63945692edaed6c474540e9885e8`.
  - `reports/round-97/c1_k_admit_counter6.py` (fixture maker) byte-identical to the frozen commit's copy (`80c1f10b…f2f4`).

## Fresh holdout results (milestone; reported, not a target)

| vector | class (what the lie is) | v8 verdict (legs) | v9 verdict (legs) |
|---|---|---|---|
| CONTROL-honest c02 | honest v6 fixture | pass (K 13/15), control-ok | pass (K 13/15), control-ok |
| C02-P1-recheck-listing-only | `recheck:` header names `ls corpus/live/runs/round-96/`, which re-verifies no digest | **ACCEPTED** (none) | **ACCEPTED** (none) |
| C02-P2-source-header-main-pin | S502 source-header URL pins branch `main`; SOURCES row and receipt keep 12f6e09 | **ACCEPTED** | **ACCEPTED** |
| C02-P3-fetchlog-404-receipt-200 | fetch log says HTTP 404 for S502; the receipt written by the lane says 200 | **ACCEPTED** | **ACCEPTED** |
| C02-P4-record-overwritten-digest-stale | saved `codeable-decompiled.c` changed `return 0x2a;` to `0x2b;`; entry and digest rows stale | **ACCEPTED** | **ACCEPTED** |
| CONTROL-honest c14 | honest landing-candidate tree (9ddd38ac + landing edits) | pass (K 14/15), control-ok | pass (K 14/15), control-ok |
| C14-P1-templated-pass-notes | three seats' PASS notes are one template with the seat and Q id substituted | **ACCEPTED** | **ACCEPTED** |
| C14-P2-pass-note-out-of-scope | ReviewerGate Q14 PASS; note says outside scope and nothing was checked (no n/a token) | **ACCEPTED** | **ACCEPTED** |
| C14-P3-pass-note-other-criterion | ReviewerBlind Q05 PASS note is the Q06 decision text | **ACCEPTED** | **ACCEPTED** |
| C14-P4-record-digest-prefixes-transposed | host-probes and rea-doctor prefixes swapped in the record-digest row | refused (`C1_DERIV_TABLE`) | refused (`C1_DERIV_TABLE`, `C1_DERIV_RERUN`) |

Counts (strict verdict; exit 0 with `C1_VERDICT=pass` = ACCEPTED, exit 1 with `fail` = refused; NO-VERDICT 0 in every run):

- v8: **accepted 7/8** (c02 4/4, c14 3/4). Controls control-ok in both profiles.
- v9: **accepted 7/8** (c02 4/4, c14 3/4). Controls control-ok in both profiles. v9 adds 12 legs
  (`C1_ANCHOR_VERBATIM, C1_ARTIFACT_COPY, C1_BODY_DIGEST, C1_DERIV_RERUN, C1_EVIDENCE_RESOLVES, C1_NA_SHARE,
  C1_PASS_NOTE_FLOOR, C1_QMAP_POINTER, C1_RECORD_PINNED, C1_SECTIONS, C1_SURFACE_TEXT, C1_VOTER_PRESENT`); none
  fires on the seven accepted vectors. The only v9-only refusal signal on the fresh set is `C1_DERIV_RERUN` on
  C14-P4 (`DERIV_ROWS=29 DERIV_MISMATCH=1`), which v8 did not have.

Predictions were written to `receipts/predictions-before-run.txt` before the runs (from reading the v8 legs).
All eight verdicts matched the prediction. Calibration point: the 12 new v9 legs each refuse exactly one r99
dev-set class (the harness output maps N1..N6 per profile to one leg each), so the 0/12 dev-set result is
per-class fitting; on fresh classes v9 still accepts 7 of 8. The seven accepted classes are routed to **r101**:
the mechanisms are recorded above, and each is a plausible lie a careless lane could tell.

## Logs and exit codes (all under `receipts/`; first two entries are the valid frozen runs)

- `receipts/logs/holdout100-v8-c02.log`, `…-v8-c14.log`, `…-v9-c02.log`, `…-v9-c14.log`: builder rc **0** each
  (`receipts/logs/rc-summary.txt`); summary lines `HOLDOUT100 accepted=4/4`, `3/4`, `4/4`, `3/4`;
  `HOLDOUT100_CONTROL=control-ok`; `HOLDOUT100_NO_VERDICT=0`.
- Per-vector `counter.log` (with `# rc=`) under `receipts/run-<v8|v9>-<c02|c14>/vectors/`.
- Harness attack re-run, v9, unmodified frozen harness (`reports/round-100/forge_reach9.py --counter reports/round-100/c1_k_admit_counter9.py`):
  rc **0**, `R100_ACCEPTED=0/12`, `R100_CONTROL_C02=control-ok`, `R100_CONTROL_C14=control-ok`,
  `R100_STUB_SELFTEST=ok`, `R100_VERDICT=met` (`receipts/logs/forge_reach9-v9-attack.log`).
- **Invalid first run (disclosed, not scored):** `receipts/invalid-first-run/`. My first builder runs used the
  frozen counter from a plain archive directory with no `.git`; the counter's `base_readme` (a
  `git archive` of the freeze base) returned nothing, so `C1_ONLY_TARGET` failed on every honest control and
  every vector. Cause is my setup, not the counter. Fixed by the git-init fixture described above; the valid
  runs are the four logs listed.

## Attacks

### A1. C1 harness fails open on the exit code (confirmed; the L1 should not score C1 as met on this basis)

- Mechanism: `forge_reach9.py` pins `BUILDER_SHA256 = 22dddf3d…84ec` (`build_fresh99.py`), an r99 builder. That builder
  decides `ACCEPTED` from the first `C1_VERDICT=` line on stdout and never reads the exit code. A counter that prints
  `C1_VERDICT=fail` and exits **0** is therefore counted as refused. Under the frozen contract (exit 0 = pass,
  1 = fail), exit 0 is an acceptance.
- Reproduction: `receipts/attack-rc0/` holds the wrapper (`receipts/attacks/c1_k_admit_counter9_rc0.py`), which
  runs the frozen v9 unchanged and exits 0 always. Its output is the true v9 output. Result from the unmodified
  harness: `R100_ACCEPTED=0/12`, `R100_CONTROL_C02=control-ok`, `R100_CONTROL_C14=control-ok`,
  `R100_STUB_SELFTEST=ok`, **`R100_VERDICT=met`, rc 0**. Every refused forged tree in that run has
  `# rc=0` in its `counter.log` (e.g. `receipts/attack-rc0/counter-c02-N1-rc0-wrapper.log`,
  `…-c14-N1-…`). So all twelve dev-set trees exit 0 under this counter, and the harness reports them refused.
- Same wrapper through my strict builder (`receipts/attack-rc0/attack-rc0-mine-c02.log`): rc 0, control-ok, and the
  four c02 vectors ACCEPTED, which matches v9's real pass verdicts. Only a verdict/exit mismatch is NO-VERDICT in my
  builder; the r99 builder pinned by the harness would call a `fail`-with-rc-0 tree refused.
- Other harness observations (static reading of `forge_reach9.py`; not run):
  - `PROFILES = ("c02", "c14")`: the c14r99 no-regression positive (`K 14/15`) and the forge_reach8 conjunct sit outside
    the harness. The harness's `met` is necessary, not sufficient, for C1 as the claims describe it.
  - The harness pins the builder's bytes only. The fixture maker it imports, `reports/round-97/c1_k_admit_counter6.py`,
    and the lane git tree are unpinned; the lane is taken from the working tree (`LANE = HERE.parents[1]`).
  - Parse fail-closed checks I traced hold: missing, duplicate, malformed-leg and unclean rows all count as accepted;
    the stub self-test compares built-tree fingerprints. I found no parse gap that makes `met` true with an accepted
    tree whose verdict text says `pass`.
- Route: fix before scoring: require the exit code to agree with the verdict (rc 0 ⇔ pass), and pin the fixture maker
  and the lane commit. The L1 decides; I did not edit the frozen harness.

### A2. C2 probe accepts a decoder-free lookup-table shim (confirmed; C2's capability claim is not held by this probe)

- Mechanism: the probe's tamper leg writes a deterministic tampered APK (`bump_last("1.0")` = `1.1`, in-place string-pool
  and ZIP-CRC patch), so its SHA-256 is fixed. A PATH shim named `androguard` and `apktool` maps the input file's SHA-256
  to a precomputed manifest: the fixture digest returns the truth XML, the tampered digest returns the tampered XML, and
  the shim decodes nothing. Shim generator: `receipts/attacks/attack_c2_gen.py`; shims: `receipts/attacks/androguard`,
  `receipts/attacks/apktool`. The shim's `--version` lines are spoofed too.
- Result (frozen probe, `--fixture corpus/fixtures/apk-r65 --work <scratch>`, PATH with the shims first):
  `CAP_FIXTURE_SHA=pass`, both `CAP_DECODER` lines name the shims, `CAP_ANDROGUARD=pass`, `CAP_APKTOOL=pass`,
  `CAP_TAMPER_DETECTED=pass`, **`CAP_APK_VERDICT=pass`, rc 0** (`receipts/logs/cap-probe-shim.log`).
  Baseline with the real decoders: androguard 4.1.4 and apktool 3.0.3, rc 0, `CAP_APK_VERDICT=pass`
  (`receipts/logs/cap-probe-real.log`).
- Why the frozen controls do not catch it: control (ii) tests a stub that prints the truth for *any* input; this shim
  keys on the input digest, so it passes the tamper leg with the same output as a real decoder.
- [INFERENCE, not run] A shim that scrapes the versionName string from the raw AXML bytes would pass the same way; the
  probe checks output values, not the decoding method.
- Route to r101: draw the tamper value from a fresh random source each run (and check it against the decoder output),
  add a second tamper leg on a different attribute, and require decoders to decode at least one probe-built APK
  whose digest was not computed before the run. C2 is **not verified** under the claims' kill rule as written:
  "a control that passes" applies only to the stub the claims name; this shim passes the tamper leg as a real
  decoder would. The L1 decides how to score C2.

## Open questions for the L1

1. A1: score C1 on the frozen harness as written (`R100_VERDICT=met` on the rc-forcing wrapper too), or require the
   exit-code consistency fix first? I recommend the fix. The v9 instrument itself was not changed by this seat.
2. A2: whether the C2 row and the capability hold on the lookup-shim finding. I recommend holding C2 until the probe
   randomises its tamper and tests a fresh APK.
3. The seven accepted fresh classes (C02-P1..P4, C14-P1..P3) are routed to r101 with their mechanisms above.
4. The 12 new v9 legs each map to one dev-set class; a second holdout run on v9 is needed before any generalisation claim.

## Tools

None installed or updated. Used: `python3` (stdlib), `git` read-only (`archive`, `rev-parse`, `cat-file`, `show`),
`git init` of a scratch fixture with an `alternates` file (no commit, no lane mutation), `sha256sum`, `tar`. No pacman,
no `~/.local/bin` writes. No messages to other seats; no subagents; no tasks spawned.

## Cleanup

Receipts copied to `.ufo/waves/round-100/w1/CriticR100/receipts/` before yield; scratch
`/fast/scratch/hyaku/revenger-r100/CriticR100/` removed at the end of the run.
