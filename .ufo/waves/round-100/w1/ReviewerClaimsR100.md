# ReviewerClaimsR100 — findings (round 100 w1, claims frozen at 05e854ce31a6ad997a28544b4edd104aaff1be81)

Scope: do-nothing/skip-work reachability per claim, predicate↔instrument identity, C1/C2 causal
separability, sourced-claim validity (axis choice). All paths under
/home/vgpnk/Projects/shokunin/revenger-shokunin/. Scratch:
/fast/scratch/hyaku/revenger-r100/ReviewerClaimsR100/ (claims_frozen.md = the frozen blob).

## §1 Frozen-input verification (all verified against bytes)

- claims.md working tree == `git show 05e854c:reports/round-100/claims.md` (cmp: IDENTICAL;
  blob sha256 817023ec533199cb…). Frozen before any scoring (commit 05e854c "claims freeze …
  + pre-freeze do-nothing controls + census start").
- Frozen v8 `reports/round-99/c1_k_admit_counter8.py` sha256
  `620dfca9959572449638cab203485555c5d45f5a8e89c5b68121ffc2d3023581` ✓ matches claims "620dfca9…3581";
  last commit touching it is 0126676 ("round-99: v8 freeze"), blob there identical → "unchanged since
  01266760" holds.
- Frozen builder `.ufo/waves/round-99/w1/CriticR99/fresh/build_fresh99.py` sha256
  `22dddf3d683719c38772f7f65716196f2eabd641e8368791e9575430e79984ec` ✓ matches claims "22dddf3d…84ec".
- `corpus/fixtures/apk-r65/fixture.apk` sha256 `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e`
  == `truth.json:image.sha256` ✓ (claims "05d2280f…d03e").
- r99 holdout receipts exist: `reports/round-99/controls/post-freeze/holdout99-v8-c02.log`
  (HOLDOUT99 accepted=6/6, CONTROL control-ok, rc=0) and `…/holdout99-v8-c14.log` (6/6, control-ok,
  rc=0) ✓ — the claims' C1 "Before" 12/12 is receipt-backed. Their sha256s match the ones recorded in
  `reports/round-100/controls/c1-do-nothing-v8.log` (45c8d2db…, c1f76e2e…).
- Decoders present at the claimed pinned versions: `~/.local/bin/androguard --version` →
  `androguard, version 4.1.4`; `~/.local/bin/apktool --version` → `3.0.3` (both on PATH via
  ~/.local/bin) ✓.
- C2 base control `reports/round-100/controls/c2-base-capability-rows.log`: rows=4 at 0350014d,
  probe absent (cat-file rc=128), no `apk-manifest-cross-decode` string — matches claims
  "Before: 4 rows; probe absent".

## §2 Axis-choice premise — recomputed (claim: valid)

Recomputed from SCORECARD.md, not taken from the claims:

- K at base 0350014d: `git show 0350014d:corpus/README.md | grep -cE '^\| C[0-9]+ .*\| held \|$'` → **14**
  of 15 C-rows (C05 `uncovered`, all others `held`) → 10×14/15 = **9.33** > 7.0 ✓.
- F4 11/11 (r92–r99 rows, unchanged holds), M 3/3 (10.00), A1v2 5/5 (10.00) — recorded per-round holds
  (r92/r96/r98 rows); all above the line ✓.
- Capability table at base: 4 rows; first-working rounds fleet-round-1 (kaika), round-75, round-80,
  round-91 → last capability entered at **round 91**; rounds 92–99 each record "Capabilities: none
  added" → 8 rounds > N = 3 ✓.
- `SCORECARD.md` §Saturation declares line **7.0** and window **N = 3** as cited. `AXES.md` §The
  stagnation nudge: "When every axis the lane owns sits at or above the lane's saturation line and no
  capability has entered the table within the lane's stagnation window … the lowest-axis obligation is
  waived: the round should be a frontier/capability move." Both conjuncts hold at base → **the nudge is
  correctly invoked**; C2 is the capability move, C1 is a second claim on a distinct axis (calibration),
  satisfying "1–3 claims, distinct axes" (AXES.md §Working the axes).

Observation (not a defect): §Saturation's prose still says "The nudge does not apply now: coverage
criteria sit at 5.0 and 2.9, and a capability entered this round" — fleet-round-1-era text superseded by
the later round sections under the lane's append-supersede convention. The claims cite §Saturation only
for the line and N, which it does declare. No action needed; noted as cosmetic staleness.

## §3 C1 — do-nothing / skip-work reachability (pre-freeze instrument review)

Instrument bytes reviewed: `reports/round-100/forge_reach9.py` (ExecHarness9 WIP, present pre-freeze).

- **Do-nothing blocked.** v8 copied as v9 is exactly the r99 receipts: 12/12 accepted (6/6 c02 +
  6/6 c14), both controls control-ok → `R100_ACCEPTED=12/12` → `R100_VERDICT=not-met`. Pre-freeze
  control log `controls/c1-do-nothing-v8.log` transcribes those receipts with their sha256 pins and
  records `C1_DO_NOTHING accepted=12/12 … verdict=not-met`. The frozen predicate sentence ("met when
  … R100_ACCEPTED=0/12, both controls control-ok, R100_STUB_SELFTEST=ok") cannot be reached unchanged.
- **Predicate ↔ instrument identity holds.** forge_reach9 `evaluate()` met-iff is exactly the frozen
  sentence: 12/12 rows parsed, accepted == 0, both controls control-ok, stub self-test ok. Fail-closed:
  missing, duplicated, malformed-legs, wrong-expected or unclean builder rows count as **accepted**
  (`classify()`), a crashed/timed-out builder run leaves all rows missing → all accepted → not-met;
  the builder summary line must agree with the table. Output order matches the contract
  (R100_VECTOR ×12 → R100_ACCEPTED → R100_CONTROL_C02 → R100_CONTROL_C14 → R100_STUB_SELFTEST=ok|bad →
  [R100_REASON…] → R100_VERDICT last); rc 0 iff met, 2 on usage/pin error (builder sha256 mismatch
  fails closed). Stub semantics match the claims: stub-pass must be accepted-with-control-ok on every
  vector; stub-fail must be refused with control-bad; and both stub runs must reproduce the main run's
  honest-tree manifest and per-vector changed/removed file sets with per-file sha256s ("same built
  trees"), else `R100_STUB_SELFTEST=bad`.
- **Builder integrity.** The harness stages a byte copy of build_fresh99.py (pinned sha, staged-copy
  sha re-checked; the committed builder is never edited or executed in place) — matches the claims'
  "bytes unchanged". Scratch discipline honoured: `--work` wins, else HYAKU_SCRATCH/forge9-work, else
  TMPDIR; everything under `<work>/forge9/`; nothing written to the lane tree.
- **Skip-work reachability.** The cheap cheats are structurally blocked or disclosed:
  (a) blanket refusal dies on no-regression conjunct (3) (c14r99 14/15 on the real tree);
  (b) v8+12 hardcoded refusals keyed to the twelve known vectors would pass everything — this is the
  **development-set exposure the claims pre-register** ("the twelve vectors are known to the builders,
  so 0/12 is a development-set result"), mitigated by CriticR100's post-freeze fresh holdout (reported,
  not a target). Whether v9's added legs are general rules or byte fingerprints is judged in §5 after
  FROZEN. A further cheat class the stub self-test cannot see: a counter keying on the `--tree` argv
  path (the builder names vector trees `<work>/<profile>/trees/<vector-name>` while the honest control
  tree and the real lane tree carry no vector name). §6 greps the frozen v9 for argv/tree-name
  inspection.

## §4 C1/C2 causal separability (pre-freeze) — holds so far

- The r99 builder reads only: the v6 fixture maker (`reports/round-97/c1_k_admit_counter6.py`
  helpers), `git archive` of rev 9ddd38ac (full) + `corpus/live/runs/round-96` (partial), and writes
  only under its `--work`. grep for `apk|SCORECARD|Capabilities|round-100|sources` over the builder →
  only `corpus/SOURCES.md` S505/S507 row edits. No apk-r65, no capability table, no round-100 rows ✓
  (matches the claims' separability sentence for C1's surface).
- forge_reach9 writes nothing to the lane and never reads SCORECARD/capabilities; the C2 counting
  command reads only SCORECARD.md. The C2 probe must (and per contract does not) run the admission
  counter — checked against the frozen probe bytes in §5.
- No-regression conjunct (3) runs `--profile c14r99` on the **instrument-freeze** archive, which
  predates the landing's SOURCES/SCOREBOARD additions → no coupling through the round-100 source rows.

## §5 WIP instruments reviewed pre-freeze (v9 counter still pending at time of writing)

### F1 — RETRACTED (was: forge_reach9 stub self-test can never pass for c02)

My 19:5x message to RevengerR100 claimed the 19:50 edit broke the stub self-test by dropping the
fx-prefix normalization from per-vector fingerprints. **Wrong**: I had misread where build_fresh99 keys
its manifests. Empirical resolution (two `--profile c02 --build-only` runs of the pinned builder in my
scratch):

- the builder's `manifest_of(honest)` keys are relative to the `fx-<rand>/t` fixture root itself
  (`build_c02_honest` returns the fixture root), so `vector.json:changed` rels are **prefix-free**
  (observed: `changed[0]: reports/round-96/votes/ReviewerGate.json` in both runs);
- the random directory name differs across runs (`fx-cn8_itwq` vs `fx-my6l_0le`,
  `tempfile.mkdtemp(prefix="fx-")` at `reports/round-97/c1_k_admit_counter6.py:653`), and the honest
  tree contents are byte-identical across runs (full-tree sha256 of both manifests:
  `b8b2700afa16d617` twice);
- therefore the frozen harness's design — anchor the honest manifest at the discovered `fx-*/t` root
  (prefix-free keys) and use raw prefix-free vector rels — is **self-consistent**, and the *old*
  380-line WIP (norm() raising ForgeError on prefix-free rels) was the broken variant. The 19:50 edit
  was a fix. The frozen harness sha 3acdd3a9 is correct as frozen.

The frozen probe (b2c9d189) differs from the 19:50 WIP I first read only by line-buffered `emit()`,
a hardened zip re-validation, and `cwd=` parameters on the decoder subprocess helpers — reviewed; no
contract impact.

## §6 After FROZEN (freeze commit 173abe91a80d79336ca9228643c63d41e0e7635c)

FROZEN file contents: `173abe91a80d79336ca9228643c63d41e0e7635c` (commit message: "instrument freeze
(v9 counter 8e2eafc8, forge_reach9 3acdd3a9, cap_apk_probe b2c9d189, controls_c2.sh 479f690e,
census_line_check c3b754aa)"). `claims.md` at 173abe9 is byte-identical to the 05e854c claims freeze
(cmp: CLAIMS_IDENTICAL). Working-tree instruments are byte-identical to the frozen blobs (counter
8e2eafc8, probe b2c9d189, harness 3acdd3a9 — no post-freeze edits). Extracted to scratch
`frozen/` via `git archive 173abe9 | tar -x`.

### v9 counter vs the claims (c1_k_admit_counter9.py, 8e2eafc8)

- **v8 kept byte-for-byte.** diff(frozen v8, frozen v9): 3 lines removed (docstring header line, one
  self-test fixture-write line, `SELFTEST_C1V8` print), 422 added. The only scored-path change is the
  docstring; the fixture-write line (role added to synthetic self-test evidence) and the
  `SELFTEST_C1V8→C1V9` rename are self-test-only. Output contract confirmed on real runs: per-leg
  `C1_<LEG>=pass|fail` lines, `C1_K_HELD_BACKED=<n>/15`, `<LEG>_WHY=` lines, `C1_VERDICT` last;
  rc 0 pass / 1 fail observed; `--self-test` prints `SELFTEST_C1V9=…` (result in the attack receipts
  below).
- **Twelve new legs, one per holdout class, all stated as rules** (`V9_LEGS`, counter :1671+):
  C1_PASS_NOTE_FLOOR (PASS notes ≥ 6 tokens), C1_VOTER_PRESENT (pinned voter with a candidate-naming
  artifact must have a vote), C1_QMAP_POINTER (PASS Q-map rows may not carry the QUALITY.md n/a
  pointer), C1_EVIDENCE_RESOLVES (every entry Evidence ID occurs in the saved records),
  C1_SECTIONS (c02; required sections present once, non-blank), C1_SURFACE_TEXT (target row's
  description cell states no vote outcome/replication), C1_NA_SHARE (c14 family; a voter marks at most
  half the criteria n/a), C1_ARTIFACT_COPY (c14 family; no artifact equals another role's artifact
  after seat-name replacement), C1_DERIV_RERUN (c14 family; declared verbatim-stdout derivation rows
  re-run in the tree to their printed values), C1_RECORD_PINNED (c14 family; the three saved round-98
  record files equal pinned lane bytes), C1_BODY_DIGEST (registry body length/sha citations match the
  named bytes), C1_ANCHOR_VERBATIM (new own-work anchor quotes appear verbatim in the entry).
- **No builder fingerprinting.** grep over the frozen counter: no `C02-N`/`C14-N` vector-name
  literals in code (one comment names the class source), no `--tree` argv inspection (sole `sys.argv`
  is `main`), no reads of builder outputs; `LANE` reads are v8's inherited FREEZE_REV base-snapshot
  mechanism, unchanged. Stronger evidence: the counter's own `--self-test` applies each leg's delta to
  the **v6 fixture world** (its own synthetic deltas, not the builder's bytes) and requires the same
  legs to fire there — the legs are rule-based, not byte-matched.
- **Honest worlds and the real tree pass under all twelve legs** (attack runs, post-freeze, counter
  run from its lane path so `base_readme`'s `git archive FREEZE_REV corpus/README.md` resolves; runs
  against scratch copies made from the pinned builder at rev 9ddd38ac and from `git archive 173abe9`):
  - c02 honest fixture → `C1_K_HELD_BACKED=13/15`, `C1_VERDICT=pass`, rc 0; all six applicable v9 legs
    `ok` (PASS notes 20 tokens, votes complete, no PASS+pointer rows, Evidence IDs resolve, sections
    present, surface cell clean);
  - c14 honest fixture → `14/15`, pass, rc 0; six applicable v9 legs `ok` incl.
    `C1_DERIV_RERUN_WHY=DERIV_ROWS=29 DERIV_MISMATCH=0`, RECORD_PINNED/BODY_DIGEST/ANCHOR_VERBATIM ok;
  - **c14r99 on the frozen tree (173abe9) → `14/15`, pass, rc 0** — the no-regression conjunct (3)
    precondition holds on the exact frozen bytes (receipts: `v9b-c14r99.out` in my wave dir).
  - Run-shape note: running the counter from a scratch copy fails `C1_ONLY_TARGET` with
    `C1_ONLY_TARGET_DIFFS=none` because `base_readme` resolves `LANE` from the counter's own location
    (`parents[2]`) — an artifact of my first attempt, not a counter defect; the scored runs pass the
    lane-path counter.

### Frozen probe and C2 controls (cap_apk_probe.py b2c9d189, controls_c2.sh 479f690e)

- Probe-vs-contract: verified clause by clause (detail in the §7 appendix, updated for the frozen bytes) — truth-derived
  expectations only, both decoders actually spawned via PATH with overrides, tamper leg requires both
  decoders to report the same-length `1.0→1.1` value and rejects truth-echoes, `CAP_APK_VERDICT` last,
  rc 0/1/2 semantics, scratch-only writes. **No path found by which the probe passes without both
  decoders decoding the genuine bytes**: decode failure, truth-echo, or wrong value fails the verdict;
  the fixture digest leg binds the scored bytes (verified 05d2280f… == truth.json in §1).
- Residual (accepted scope, named): the claims' stub control only forges echo-shims; a shim wrapping
  the *other* real decoder would satisfy both legs — "two independent decoders" is not mechanically
  provable beyond the echo-forgery class the claims freeze.
- Controls driver read: STUB (PATH-shimmed echo forgeries, plausible version lines) must be refused
  via the tamper leg; FLIP (one flipped versionCode data byte via the readout.py struct walk) must
  print `CAP_FIXTURE_SHA=fail` and fail; `C2_CONTROLS=control-ok` iff both refused. Matches the
  claims' controls (ii)/(iii).
- Attack runs (probe, self-test, controls) — results recorded with the receipts below.


## §7 Appendix — probe WIP review detail (pre-freeze 369-line bytes; frozen b2c9d189 adds emit() buffering, zip re-validation hardening, cwd= on decoder helpers only)

Reviewed `reports/round-100/cap_apk_probe.py` (369 lines, mtime 19:50) clause by clause:

- (a) `CAP_FIXTURE_SHA`: sha256(fixture.apk) vs `truth.json:image.sha256`; fail does not short-circuit
  (all legs still run, verdict fails) ✓. The claims' "(or, if truth.json records none …)" fallback is
  not implemented — the probe fails when truth has no digest, which is stricter than the predicate and
  equivalent on this fixture (truth records the digest, verified in §1). No self-referential path exists.
- (b) version lines printed for both decoders; resolution via `shutil.which` (PATH, so shims are
  testable) with `--androguard`/`--apktool` overrides; missing decoder → contract lines printed, rc 2 ✓.
- (c) expected values derived generically from `truth.json` `axml_declared` (data_type 0x03 →
  `strings[raw_value_idx]`, else `str(data)`); no package/versionCode/versionName literal anywhere ✓;
  both decoders actually spawned (`androguard axml <apk>`, `apktool d -f -s -o <scratch>`), failures →
  leg fail ✓; `CAP_ANDROGUARD`/`CAP_APKTOOL` compare all three fields ✓ (local-name normalization
  handles the fixture's `ns0:`/`n0:` prefix quirk, documented in-probe).
- (d) tamper leg: same-length `1.0 → 1.1` (`bump_last`), string-pool entry patched with
  length-prefixed unique pattern, ZIP_STORED member swapped in place with CRC-32 fixed in **both** the
  local header and the central directory, container validated with `testzip`, then **both** decoders
  must report exactly the tampered value on the tampered APK; echoing the truth value fails the leg ✓
  — this is the echo-shim killer the claims' control (ii) relies on.
- (e) `CAP_APK_VERDICT` last; rc 0 iff pass, 1 fail, 2 usage/missing decoder ✓; output order matches
  the contract exactly ✓.
- Coupling: the probe reads only `<fixture>/truth.json` + `fixture.apk` and writes only under scratch
  (`--work` → `$HYAKU_SCRATCH` → TMPDIR, cleaned on exit) ✓; it never runs or reads the admission
  counter ✓ — C2 stays causally separable as claimed.
- Minor notes (not defects): `apktool d` may create `~/.local/share/apktool` framework cache — the one
  outside-scratch write the wave rules allow; decoder subprocess timeout 120 s each.

## §8 Attack-run receipts (all post-FROZEN attacks on the frozen bytes, run by this seat in scratch;
## the L1's scored runs are its own)

1. **forge_reach9 + frozen v9** (`receipts/forge-attack.out`): twelve `R100_VECTOR … refused` lines —
   each vector refused by exactly the leg designed for its class (C02-N1→C1_PASS_NOTE_FLOOR,
   N2→C1_VOTER_PRESENT, N3→C1_QMAP_POINTER, N4→C1_EVIDENCE_RESOLVES, N5→C1_SECTIONS,
   N6→C1_SURFACE_TEXT, C14-N1→C1_NA_SHARE, N2→C1_ARTIFACT_COPY, N3→C1_DERIV_RERUN,
   N4→C1_RECORD_PINNED, N5→C1_BODY_DIGEST, N6→C1_ANCHOR_VERBATIM) — then `R100_ACCEPTED=0/12`,
   `R100_CONTROL_C02=control-ok`, `R100_CONTROL_C14=control-ok`, `R100_STUB_SELFTEST=ok`,
   `R100_VERDICT=met`, **rc 0**. The refusals fired on the *builder's* independent implementations of
   the twelve classes while the counter's `--self-test` fires the same legs on the counter's own
   synthetic deltas — the legs are rules over the tree, not byte fingerprints, now proven behaviorally
   as well as by grep. The stub self-test's six builder re-runs also confirm tree determinism.
2. **v9 `--self-test`** (`receipts/selftest.out`): rc 0, `SELFTEST_C1V9=OK legs=128` — no-regression
   conjunct (1) holds.
3. **c14r99 on the frozen tree** (`receipts/v9b-c14r99.out`): `C1_K_HELD_BACKED=14/15`,
   `C1_VERDICT=pass`, rc 0 on a `git archive 173abe9` extract — no-regression conjunct (3)'s
   precondition holds on the exact freeze bytes.
4. **forge_reach8 + frozen v9** (`receipts/forge8-v9.out`) — no-regression conjunct (2):
   `C2_ACCEPTED=0/12` on the r98 holdout (all twelve refused by the inherited v8 legs; c14-V01
   additionally refused by the new C1_PASS_NOTE_FLOOR), `C2_CONTROL_C02=control-ok`,
   `C2_CONTROL_C14=control-ok`, `C2_STUB_SELFTEST=ok`, `C2_VERDICT=met`, **rc 0**. No regression.
5. **Frozen probe on the real fixture** (`receipts/probe.out`): `CAP_FIXTURE_SHA=pass`,
   `CAP_DECODER androguard version=androguard, version 4.1.4`,
   `CAP_DECODER apktool version=3.0.3`, `CAP_ANDROGUARD=pass`, `CAP_APKTOOL=pass`,
   `CAP_TAMPER_DETECTED=pass`, `CAP_APK_VERDICT=pass`, **rc 0**.
6. **C2 controls** (`receipts/summary.out`, `control-stub.log`, `control-flip.log`):
   STUB echo-shims pass the honest legs but fail the tamper leg (`CAP_TAMPER_DETECTED=fail` →
   `CAP_APK_VERDICT=fail`, probe rc 1) → `C2_CTRL_STUB=refused`; FLIP → `CAP_FIXTURE_SHA=fail`,
   `CAP_APK_VERDICT=fail`, probe rc 1 → `C2_CTRL_FLIP=refused`; `C2_CONTROLS=control-ok`, rc 0.
   Observation (no claim impact): on the flipped fixture androguard reports the flipped versionCode
   while apktool still matches truth — the frozen control (iii) requires only the digest leg + verdict
   fail, both observed; decoder disagreement on the flip is not a frozen requirement.

## §9 Verdicts

- **C1 (calibration, v9 vs the r99 fresh holdout): `sound` as frozen.** The do-nothing tree is
  blocked (v8-as-v9 is receipt-identical 12/12 accepted → not-met); the predicate sentence and
  forge_reach9's met-iff compute the same condition; all three no-regression conjuncts verified on the
  frozen bytes (1: self-test rc 0; 2: see §8 item 4; 3: 14/15 pass on the freeze tree); the twelve
  added legs are general rules with no builder fingerprinting (grep + behavioral double-fire). The
  pre-registered development-set disclosure stands: 0/12 is a development-set result, and
  CriticR100's fresh holdout (reported, not a target) is the generalization check.
- **C2 (capability, apk-manifest-cross-decode): `sound` as frozen.** The probe's pass requires both
  decoders to decode the genuine bytes (digest-bound), agree with truth.json-derived values, and
  report the tampered value; no pass-without-decoding path found; both frozen controls refuse
  (`C2_CONTROLS=control-ok`); the probe attack passes rc 0. Causally separable from C1 (probe reads
  only the fixture dir; counter/harness/builder never touch apk-r65, SCORECARD or the capability
  table).
- **Axis choice: `sound`.** Nudge premise recomputed from SCORECARD.md at base (K 14/15 = 9.33,
  F4 11/11, M 3/3, A1v2 5/5 — all above the 7.0 line; last capability round-91, 8 rounds > N=3);
  invocation matches AXES.md §The stagnation nudge; the round makes the capability move (C2) plus a
  second-axis claim (C1, calibration), causally separable as required.
- My only defect report during the wave (F1, harness stub fingerprinting) was **mine to retract** —
  retracted above with the empirical resolution; the frozen harness is correct. No open defect
  remains against the frozen instruments.


## §10 Residual risks / verification gaps

1. RESOLVED: the stub self-test's cross-run tree determinism — exercised by my forge_reach9 attack
   (six builder re-runs, fingerprints equal, `R100_STUB_SELFTEST=ok`) and by the byte-identical honest
   manifests (`b8b2700afa16d617` twice). No gap remains.
2. `controls/c1-do-nothing-v8.log` is a sha-pinned transcription of the r99 receipts, not a fresh
   v8-through-forge_reach9 run. Consistent with the claims' own wording ("an unchanged counter is
   exactly those receipts"); my forge_reach9 attack run against v8's legs-as-v9 behavior is covered by
   the r99 receipts plus the frozen-v9 run above.
3. Hygiene: a stray untracked file `corpus/fixtures/apk-r65/androguard.log` (androguard loguru stderr,
   created 2026-11-05 19:39 during this wave) sits inside the frozen corpus/ tree. Scored fixture
   bytes unchanged (sha verified in §1); the file must not be swept into any landing commit (r93 M4
   class). The frozen probe itself writes only under `--work` (verified); apktool's
   `~/.local/share/apktool` framework cache is the one allowed outside-scratch write.
4. Development-set disclosure (pre-registered in the claims): the twelve refused vectors are known to
   the builders, so C1's 0/12 is a development-set result. The generalization check is CriticR100's
   fresh round-100 holdout — reported, not a target; until it lands, v9's reach beyond the twelve
   classes is unmeasured.
5. C2's "two independent decoders" is enforced against echo-forgery only (the frozen control class);
   a shim wrapping the other real decoder would satisfy both decoder legs. Mechanical independence
   beyond that class is out of the frozen predicate's scope.
6. `SCORECARD.md` §Saturation prose still carries the stale fleet-round-1 sentence "The nudge does not
   apply now…" (superseded by the later round sections; the claims cite §Saturation only for the 7.0
   line and N=3, which hold). Cosmetic staleness only.
7. Observation, no claim impact: on the versionCode-flipped fixture, apktool still matches truth
   while androguard reports the flip (§8 item 6) — the two decoders evidently resolve the INT_DEC
   versionCode attribute differently after the flip; the frozen control requires only the digest leg
   plus verdict fail.

