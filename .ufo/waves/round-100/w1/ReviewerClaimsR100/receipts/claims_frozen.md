# Round 100 — declared claims (FROZEN before any wave seat scores anything)

Lane: revenger. Base (round start, lane head): `0350014d30e91da411ee624025d8d1bb7afc6ccf` (the r99 closure
spot-check tip). This file and `controls/` are frozen by the claims-freeze commit recorded in the report.
Predicates, targets, counting commands and kill rules below are not edited after the freeze. A change made
after any scoring is a new claim, not this one.

**Axis choice.** Owned criteria at base: K 14/15 (9.33), F4 11/11, M 3/3, A1v2 5/5, every one above the
saturation line 7.0 (`SCORECARD.md` §Saturation); the last capability entered the table at round 91, more
than N = 3 rounds ago. The stagnation nudge therefore applies (AXES.md *The stagnation nudge*): the
lowest-axis obligation is waived and the round makes a capability move (C2). C1 is calibration.
Two claims on two distinct axes, causally separable: C1 is scored only on the r99 holdout fixture trees
(built from pinned inputs by the frozen `build_fresh99.py`; they never read `corpus/fixtures/apk-r65`, the
capability table or any round-100 source row); C2 is scored only on `corpus/fixtures/apk-r65/` and the
`## Capabilities` table and never runs the admission counter.

Ordering contract, enforced by the L1:
(a) this file and `controls/` are committed (the claims freeze);
(b) wave seats build `reports/round-100/c1_k_admit_counter9.py` (+ self-test), the harness
    `reports/round-100/forge_reach9.py`, and the capability probe `reports/round-100/cap_apk_probe.py`;
    no seat scores the C1 target run or the C2 target run;
(c) the L1 commits the frozen instrument bytes (the instrument freeze) and writes
    `.ufo/waves/round-100/w1/FROZEN` naming that commit;
(d) only after (c): the controls below, then the target runs, then attack seats' re-runs and the fresh
    round-100 holdout (reported, never a target).

## C1 — calibration: the admission counter's reach over the round-99 fresh holdout

- **Surface moved:** the admission counter (new file `reports/round-100/c1_k_admit_counter9.py`, a byte
  copy of frozen v8 plus new legs). Frozen v8 (`reports/round-99/c1_k_admit_counter8.py`, sha256
  `620dfca9…3581`, unchanged since `01266760`) accepts **12/12** of the round-99 fresh holdout vectors
  (c02 N1–N6, c14 N1–N6) with both honest controls `control-ok`:
  `reports/round-99/controls/post-freeze/holdout99-v8-c02.log` (`HOLDOUT99 accepted=6/6`) and
  `…/holdout99-v8-c14.log` (`HOLDOUT99 accepted=6/6`). This is the do-nothing control: an unchanged
  counter (v8 copied as v9) is exactly those receipts.
- **Instrument:** `reports/round-100/forge_reach9.py --counter <counter.py> --work <scratch>` stages the
  frozen builder `.ufo/waves/round-99/w1/CriticR99/fresh/build_fresh99.py` (sha256 pinned in the harness,
  bytes unchanged), runs it with `--profile c02` and `--profile c14` against the given counter, and prints
  one `R100_VECTOR <name> accepted|refused legs=<failing legs>` line per vector, then
  `R100_ACCEPTED=<n>/12`, `R100_CONTROL_C02=control-ok|control-bad`, `R100_CONTROL_C14=…`,
  `R100_STUB_SELFTEST=ok|bad` (a stub counter that prints `C1_VERDICT=pass` for every tree must score
  12/12 accepted and a stub that fails every tree must break both controls), and last
  `R100_VERDICT=met|not-met`.
- **Frozen predicate (one sentence, the same in the harness):** C1 is met when `forge_reach9.py` run on
  the frozen v9 counter prints `R100_ACCEPTED=0/12`, both controls `control-ok` and
  `R100_STUB_SELFTEST=ok`, which it reports as `R100_VERDICT=met`.
- **No-regression conjuncts (part of C1, all on the frozen v9 bytes):**
  (1) `python3 -B reports/round-100/c1_k_admit_counter9.py --self-test` → rc 0;
  (2) `python3 -B reports/round-99/forge_reach8.py --counter reports/round-100/c1_k_admit_counter9.py
      --work <scratch>` → `C2_ACCEPTED=0/12`, both controls `control-ok` (the r98 holdout stays refused);
  (3) the real lane tree positive: `python3 -B reports/round-100/c1_k_admit_counter9.py --profile c14r99
      --tree <git archive of the instrument-freeze commit>` → `C1_K_HELD_BACKED=14/15`, `C1_VERDICT=pass`,
      rc 0 (blanket refusal is not a gain).
- **Before:** 12/12 accepted (v8, receipts above). **After (target):** 0/12, `R100_VERDICT=met`, all three
  no-regression conjuncts hold.
- **Kill rule:** any accepted vector, a `control-bad`, a stub self-test `bad`, or any failed
  no-regression conjunct means C1 is **not verified**; an honest miss is recorded, never narrowed.
- **Disclosure, pre-registered:** the twelve vectors are known to the builders, so 0/12 is a
  development-set result. CriticR100 builds a fresh round-100 holdout after the freeze; its acceptance
  count is reported, not a target.

## C2 — capability acquisition: APK binary-manifest cross-decode against authored truth

- **Surface moved:** `SCORECARD.md` `## Capabilities` table gains one row, `apk-manifest-cross-decode`,
  whose evidence pointer is the probe below; new probe `reports/round-100/cap_apk_probe.py`. Sources:
  the row and the probe cite round-100 SOURCES rows for androguard and apktool opened this round (the
  round's sourced claim).
- **Probe contract:** `PYTHONUTF8=1 python3 -B reports/round-100/cap_apk_probe.py --fixture
  corpus/fixtures/apk-r65 --work <scratch>`:
  (a) checks `fixture.apk` sha256 equals the digest recorded in `corpus/fixtures/apk-r65/truth.json`
      (or, if truth.json records none, the sha256 printed by the frozen probe and recorded in its
      registry row) and prints `CAP_FIXTURE_SHA=pass|fail`;
  (b) decodes the binary `AndroidManifest.xml` with two independent decoders, androguard
      (`androguard axml`) and apktool (`apktool d -s`), recording each decoder's version line;
  (c) compares `package`, `versionCode`, `versionName` (values read from `truth.json`'s AXML string
      pool and attribute records, never hardcoded) against each decoder's output and prints
      `CAP_ANDROGUARD=pass|fail`, `CAP_APKTOOL=pass|fail`;
  (d) tamper leg: writes a scratch copy of the APK whose `versionName` string-pool value `1.0` is
      replaced by a same-length value (and the ZIP CRC fixed so the container stays valid), decodes it
      with both decoders, and requires each decoder to report the tampered value and the probe's own
      comparison to flag `versionName` as a mismatch: `CAP_TAMPER_DETECTED=pass|fail`. A decoder (or
      shim) that echoes the truth values for any input fails this leg;
  (e) prints last `CAP_APK_VERDICT=pass|fail`; rc 0 iff pass, 1 if fail, 2 on usage error or a missing
      decoder.
- **Frozen predicate (one sentence, the same in the probe):** the capability holds when the frozen probe
  prints `CAP_APK_VERDICT=pass` with rc 0 on `corpus/fixtures/apk-r65`, which requires the fixture
  digest, both decoders' agreement with truth and the tamper leg to pass.
- **Counting command (table rows):**
  `awk '/^## Capabilities/{f=1;next} /^## /{f=0} f && /^\| / && !/^\| Capability/ && !/^\|---/' SCORECARD.md | wc -l`
  → before **4** at `0350014d` (`controls/c2-base-capability-rows.log`); after target **5**, with the new
  row naming `cap_apk_probe.py`.
- **Before:** 4 rows; probe absent (`controls/c2-base-capability-rows.log`). **After (target):** 5 rows and
  the probe passes on the landing tree (rc 0).
- **Controls (after the instrument freeze, before the target run):** (i) do-nothing: base tree has no
  probe and 4 rows (recorded pre-freeze in `controls/c2-base-capability-rows.log`); (ii) stub decoders:
  PATH-shimmed `androguard` and `apktool` that print the truth manifest for any input must make the probe
  print `CAP_APK_VERDICT=fail` (tamper leg); (iii) a byte-flipped fixture copy (versionCode data byte)
  must make the probe print `CAP_FIXTURE_SHA=fail` and `CAP_APK_VERDICT=fail`. Both (ii) and (iii) must
  refuse; if either passes, C2 is not verified.
- **Kill rule:** probe fail or rc ≠ 0 on the landing tree, a control that passes, rows ≠ 5, or a
  capability row that does not cite a round-100 opened source → C2 **not verified**.
- **Scope boundary:** this is a capability (two third-party decoders agree with authored truth on one
  authored inert fixture, and a tamper is detected). It is not a C05 knowledge admission, does not move K
  (C05 stays `uncovered`), and makes no claim about real-world APKs, DEX decoding or REA's
  `inspect_android_package` route.
