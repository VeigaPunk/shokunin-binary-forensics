# round-90 run ledger — android family record through the current producer

One bounded, passive, non-executing producer observation of the authored inert
APK `corpus/fixtures/apk-r65/fixture.apk` (947 bytes; never installed or run),
saved as producer-emitted bytes. Claim C2 of round 90
(`reports/round-90/claims.md`, frozen at `c7767789fe9e96bcc0d50656ad4bdce69ba3a3a9`
before this run).

- producer: `rea inspect-android-package corpus/fixtures/apk-r65/fixture.apk --format json`
  from the lane root, `rea --version` 6.7.0, provider read from the record
  `jadx` / "JADX headless" / 0.7.1; `jadx` 1.5.6, OpenJDK 21.0.13
  (`reports/round-90/android-env.log`). Run by wave seat `ExecR90Producer`.
- record: `inspection.json` here = run1's exact stdout (sha256
  `9d665ffbc8674d41675b164f8d4cc70457e00a0b94eee2de9ab4d6b010249e12`, 4309
  bytes, exit 0, stderr 0 bytes); Evidence
  `ev_affae0e5ae0fb1ef295975485048faa4721ee620c99a0d72603dfaaedef1e6c5`.
- second run: `reports/round-90/android-run2.json` (sha256
  `214094fbe04883e1f1879f5d314397899cdbf43a66d92607b9a0f560ec322f38`, exit 0),
  Evidence `ev_d4a34332e3ca12df700b7698de453f75066ec7bfcfc79c03c21e5e013de81b37`.
  The runs differ only in the frozen volatile set V1–V4 of
  `reports/round-90/norm_eq.py` (`NORM_EQ=identical`).
- receipt: `reports/round-90/android-receipt.json` (UTC start/end, exit,
  stderr bytes, wall seconds, stdout bytes and sha256 per run).
- disclosure: a first pair of runs was discarded unscored because the host
  `date` ignored `%3N` and wall time was not captured
  (`.ufo/waves/round-90/w1/ExecR90Producer/discarded-attempt0-timing.log`).
- what this record does NOT establish: provenance (a hand-written
  content-accurate record would pass the oracle; Q09), Android runtime
  behaviour, or any fixture other than apk-r65. Sensitivity: home path in
  `subject.local_path`, scratch path in the runtime fields, host JVM sizing —
  low class, same as round 89 (`.ufo/waves/round-90/w1/SentinelR90/report.md`).
