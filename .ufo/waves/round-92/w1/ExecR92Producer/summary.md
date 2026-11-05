# ExecR92Producer — r85 managed-artifact producer re-run (round 92 w1)

Seat: ExecR92Producer (leaf). Lane: revenger-shokunin. Scratch used:
`/fast/scratch/hyaku/revenger-r92/ExecR92Producer/` (deleted before yield).

## 1. Tool, version, channel, reason

- r85 records were produced by **rea 6.8.0** (`receipt.json` `host_env.rea=6.8.0`, PROVINCE host);
  this host's `rea --version` is **6.7.0** — version mismatch, so the re-run used 6.8.0.
- Used: **`npx -y rea-agents@6.8.0`** — official npm registry channel; package version 6.8.0
  (confirmed by `npx -y rea-agents@6.8.0 --version` → `6.8.0`, exit 0).
- Reason: reproduce the committed records with the same producer version as the receipts record.
- Host guard note (recorded defect D2): rea-agents@6.8.0 declares engines
  `^22.23.4 || ^24.22.1 || >=26.12.1`; host node is `v24.21.0` (npm 11.19.0) → npm prints
  `EBADENGINE` warnings; the CLI ran correctly anyway (all runs exit 0). Formally unsupported
  combination, observed working.
- No tools installed via pacman (paused host-wide); nothing else installed.

## 2. Fixture

- Built artifact the generator writes: `generator.py` main() → `fixture.dll`
  (`out = Path(sys.argv[1]) ... default Path("fixture.dll")`; `out.write_bytes(image)`).
- Committed `corpus/fixtures/managed-r85/fixture.dll`: 1048 bytes, sha256
  `94429fa428893dd78ed4b7f26a919232d5f05cc9cdc84d256954db5b0a286760` — equals
  `receipt.json` `fixture_sha256`.
- Fixture dir copied (`cp -a`) to scratch, NOT regenerated in place. Extra determinism check in
  scratch only: `python3 generator.py regen-fixture.dll` → "self-check OK", 1048 bytes, sha256
  `94429fa4...` — byte-identical regen.

## 3. Producer runs (2×, on the scratch copy)

cwd = scratch root with the lane's relative layout (`corpus/fixtures/managed-r85/fixture.dll`
under it); `PYTHONUTF8=1`; `rea` = the `rea-agents` npm bin:

```
npx -y rea-agents@6.8.0 inspect-managed-artifact corpus/fixtures/managed-r85/fixture.dll --format json
```

(same command shape as `receipt.json` `command`; the `--format json` arg and relative fixture
path preserved; run against the scratch copy per seat spec.)

| run | exit | stdout bytes | stdout sha256 | stderr bytes |
|-----|------|--------------|---------------|--------------|
| run1 (`run1.json`) | 0 | 3064 | `7a722d3ab93eb003d204b414bc521a07e9502d8b8e5fdb8c8c85365f2dbf9878` | 0 (`run1.stderr.txt`) |
| run2 (`run2.json`) | 0 | 3064 | `7a722d3ab93eb003d204b414bc521a07e9502d8b8e5fdb8c8c85365f2dbf9878` | 0 (`run2.stderr.txt`) |

Committed record `inspection.json`: 3190 bytes, sha256
`90440ec14937849b60fe11d4eda26a51a504529ac31d6678da0be592a586dfc4` (= `receipt.json`
`stdout_sha256`; verified against the committed bytes).

## 4. Comparison verdicts (receipt: `comparison.txt`, sha256 `e7d86f7e3219ff76c7817e2036e7d372f458cbb5be89ef7be32f612da1ce1912`)

- byte equality: run1 == run2 **TRUE**; run1 == committed **FALSE**; run2 == committed **FALSE**.
- Raw field diffs run1 vs committed — exactly 3:
  1. `subject.local_path`: `C:\Users\jpvei\.zcode\...\shokunin-binary-forensics\corpus\fixtures\managed-r85\fixture.dll` (Windows PROVINCE host) vs `/fast/scratch/.../corpus/fixtures/managed-r85/fixture.dll` (this host).
  2. `normalized_result.artifact.path`: same two absolute paths.
  3. `evidence_id`: committed `ev_0eea92d75cd2bb0d69be542825a96f9f2a98ea359ffdf607fd7cb910dbf796e2` vs re-run `ev_3991d5a7b5aa1c629135d07e11068a963b7517e9a551462580d0ecc39f4245a6`.
- Normalized equality (scrubbing those 2 path fields): run1 == run2 **TRUE**; run1 vs committed
  **FALSE** — only `evidence_id` still differs.

### Why (proven, receipt: `ev-derivation.txt`, sha256 `3a12673639d7942faca041f2ce0de013fc74905300fcd80ee78660634833bdef`)

- rea 6.8.0 source (`dist/cli-runtime/javascriptFeatureTraceSchemas-machBq68.js` lines
  681/702, npx cache copy): `evidence_id = ev_ + sha256(canonical JSON of
  evidenceSemanticContent(e))`; the projection includes `normalized_result` (hence
  `artifact.path`, the absolute path) but reduces `subject` to `{digest, format,
  architecture}` — `subject.local_path` is outside the identity.
- My Python replica of that canonicalization recomputes exactly: committed →
  `ev_0eea92d7...` (match), run1/run2 → `ev_3991d5a7...` (match).
- Decisive control: substituting ONLY the committed `normalized_result.artifact.path` value
  into run1 flips the recomputed id to exactly the committed `ev_0eea92d7...` (match=True).
  ⇒ the sole semantic-content difference between the committed record and my re-runs is the
  machine-specific absolute artifact path; all managed-format facts (classification,
  metadata tables, MVID, assembly name/version, offsets) are identical, and the producer is
  deterministic (run1 == run2 byte-for-byte).

## 5. Committed oracle re-runs (step 5; cwd = lane root; exact receipt commands; `PYTHONUTF8=1`)

`python -I -B corpus/fixtures/managed-r85/oracle_check.py corpus/fixtures/managed-r85/truth.json corpus/live/runs/round-85/<op>/inspection.json corpus/fixtures/managed-r85/fixture.dll`

| operation | verdict | exit | receipt |
|-----------|---------|------|---------|
| inspect-managed-artifact | `ORACLE OK (20/20 checks)` | 0 | `oracle-inspect-managed-artifact.log` sha256 `3d29b071dd7792713cad4e4451678b3bb87faa3e9b56c0941f40ce4f39db6ab9` |
| inspect-managed-members | `ORACLE OK (47/47 checks)` | 0 | `oracle-inspect-managed-members.log` sha256 `414b5c3d43f044238b67cbd79642c155fce27e2dbf344439e78da56eb4ef5657` |
| inspect-managed-native-boundaries | `ORACLE OK (39/39 checks)` | 0 | `oracle-inspect-managed-native-boundaries.log` sha256 `9974445e618914c81a89a969bc1e0c44892679dd59d065932e32b2a60d6402ca` |

Bonus: the same committed oracle over my re-run (`run1.json`): `ORACLE OK (20/20 checks)`,
exit 0 (`oracle-run1-bonus.log`, sha256 `3d29b071...` — byte-identical output to the
committed-record run, since none of the oracle's 20 checks touch the 3 differing fields).
Oracle stderr files: 0 bytes each.

## 6. Defects

- **D1 (record gap):** the r85 `LEDGER.md` (artifact op) documents no volatile-field /
  normalization section (grep over r85+r76 records for `volatile|local_path|normalized` finds
  nothing outside the JSONs themselves). Consequence: byte-identical re-derivation of this
  record on a different host/path is impossible by construction (the identity digest covers
  `normalized_result.artifact.path`), and the ledger's pointer "oracle + regen re-run over
  `git archive` bytes" holds for the fixture, not for the record's own bytes. Any C1 entry
  wording should claim per-host determinism + semantic identity, not cross-host byte equality.
- **D2 (environment, non-blocking):** `rea-agents@6.8.0` engines exclude host node v24.21.0
  (EBADENGINE warning); runs succeeded. Flagged so the L1 knows the version used.

## 7. Bounds

Writes: only this wave dir (`run1.json`, `run2.json`, `run1.exit`, `run2.exit`,
`run1.stderr.txt`, `run2.stderr.txt`, `comparison.txt`, `ev-derivation.txt`,
`oracle-*.log`, `oracle-*.stderr.txt`, `summary.md`) plus the report
`.ufo/waves/round-92/w1/ExecR92Producer.md`. No mutating git/jj command; lane reads only;
nothing written under `corpus/`, `reports/round-92/`, or any other lane path.
