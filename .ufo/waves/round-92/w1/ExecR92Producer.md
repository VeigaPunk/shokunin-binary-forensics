# ExecR92Producer — report (round 92 w1)

Full evidence: `.ufo/waves/round-92/w1/ExecR92Producer/summary.md` (commands, exit codes,
sha256s, comparison verdicts, defects). Receipts live in the same dir.

## What was done

1. Read the r85 `inspect-managed-artifact` LEDGER + receipt; command shape
   `rea inspect-managed-artifact corpus/fixtures/managed-r85/fixture.dll --format json`,
   cwd = lane root, producer rea **6.8.0** (receipt `host_env`). Built fixture file =
   `fixture.dll` (generator.py writes it; committed bytes 1048, sha256 `94429fa4...`,
   matches receipt; scratch regen byte-identical).
2. Tool/version/channel: `npx -y rea-agents@6.8.0` (official npm registry) — `--version` →
   `6.8.0`, exit 0. Reason: host `rea` is 6.7.0, records say 6.8.0; version parity required.
   Defect D2: package engines exclude host node v24.21.0 (EBADENGINE, ran fine).
3. Two producer runs on the scratch copy of the fixture (relative path preserved):
   run1 and run2 both exit 0, stdout 3064 bytes, stderr 0 bytes, byte-identical to each
   other (sha256 `7a722d3ab93eb003d204b414bc521a07e9502d8b8e5fdb8c8c85365f2dbf9878`) →
   producer deterministic.
4. Comparison vs committed `inspection.json` (3190 bytes, sha256 `90440ec1...`):
   byte equality run-vs-committed **FALSE**; exactly 3 fields differ:
   `subject.local_path`, `normalized_result.artifact.path` (Windows PROVINCE path vs this
   host's scratch path), `evidence_id` (`ev_0eea92d7...` vs `ev_3991d5a7...`).
   **Why, proven:** `evidence_id = ev_ + sha256(canonical JSON of evidenceSemanticContent)`
   (rea 6.8.0 dist source) — the projection includes `normalized_result.artifact.path` and
   excludes `subject.local_path`. A Python replica recomputes all three recorded ids exactly,
   and substituting ONLY the committed artifact path into run1 flips the id to the committed
   `ev_0eea92d7...` ⇒ the sole semantic difference is the machine-specific absolute path;
   all managed-format facts identical. Defect D1: the r85 LEDGER documents NO volatile-field
   normalization, so cross-host byte re-derivation of the record is impossible by
   construction — C1 entry wording must claim per-host determinism + semantic identity, not
   byte equality.
5. Committed oracle re-runs from lane root (exact receipt commands): artifact
   `ORACLE OK (20/20 checks)` exit 0; members `ORACLE OK (47/47 checks)` exit 0;
   native-boundaries `ORACLE OK (39/39 checks)` exit 0. Bonus: the committed oracle also
   passes over my re-run (`ORACLE OK (20/20 checks)`, exit 0).

## Files (wave dir)

`summary.md`, `run1.json`, `run2.json`, `run1.exit`, `run2.exit`, `run1.stderr.txt`,
`run2.stderr.txt`, `comparison.txt`, `ev-derivation.txt`, `oracle-inspect-managed-artifact.log`,
`oracle-inspect-managed-members.log`, `oracle-inspect-managed-native-boundaries.log`,
`oracle-run1-bonus.log` (+ `.stderr.txt` siblings, all 0 bytes).

## Bounds

No mutating git/jj command; nothing written under `corpus/`, `reports/round-92/`, or any
lane path besides this wave dir and this report; scratch
`/fast/scratch/hyaku/revenger-r92/ExecR92Producer/` deleted before yield.
