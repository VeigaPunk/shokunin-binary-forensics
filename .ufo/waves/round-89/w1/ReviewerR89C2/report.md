# ReviewerR89C2 — attack on C2 (coverage: android family record, F4 10/11 -> 11/11 + ORACLE 19/19)

Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`. Frozen at `c84339c`; base `2b017fa3`.
Axes: coverage, calibration. Seat is read-only; no lane file was edited, nothing committed, no git mutation, no tool installed or upgraded.
Receipts (copies of every command log, the forged inputs, and the two driver scripts): `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-89/w1/ReviewerR89C2/receipts/`.

## Verdict

**C2 is KILLED, not admitted.** The nominal counters are met (F4 = 11/11, ORACLE OK 19/19 on the landed bytes), but both frozen kill rules that bind the record fail on measured evidence:

- **Kill (a), record-shaped forgery must not pass: FAILS.** A real producer record with only its `manifest.text` replaced (package, versionCode and versionName all contradicted; the expected fragments hidden in an XML comment) gives `F4_COVERAGE=11/11` and `ORACLE OK (19/19 checks)`, exit 0.
- **Kill (c), two independent producer runs byte-identical: FAILS.** The runs differ at char 20 (per-run `evidence_id`) and in three other volatile fields. ExecR89Record's own receipt says so (`NOT ADMITTED`).

**Do F4 and the oracle together admit a fabricated record? Yes.** Any record whose `normalized_result` is internally consistent with the fixture and whose manifest text contradicts it passes both. Separately, F4 alone admits any three-key JSON file (section 3).

## 1. Base re-derivation

`PYTHONUTF8=1 python3 -B reports/round-81/f_probe4.py <git archive 2b017fa3 corpus>` -> `F4_COVERAGE=10/11 score=9.09`, `F4_FAMILIES` without `android`, no `inspect_android_package` key. Log: `receipts/base-f4.log`. Base instrument byte-equal to the freeze (`4d871971…`).

## 2. Per-check provenance of the 19 oracle checks

Read line by line from `corpus/fixtures/apk-r65/oracle_check.py` (sha `44fd1505…`, equal to freeze). **No expectation is copied from the record.** Every expectation comes from fixture bytes, from `truth.json`, or is a constant written into the oracle. The record is only ever the right-hand side of a comparison.

| # | Check | Source of expectation | Classification |
|---|---|---|---|
| 1 | fixture sha256 == truth.image.sha256 | fixture bytes vs truth | derived-from-bytes (premise) |
| 2 | fixture size == truth.image.size | fixture bytes vs truth | derived-from-bytes (premise) |
| 3 | member set == truth recipe names | zip member table from bytes vs truth | derived-from-bytes (premise) |
| 4 | member byte lengths == recipe | zip bytes vs truth | derived-from-bytes (premise) |
| 5 | member digests == truth.members[].sha256 | member bytes vs truth | derived-from-bytes (premise) |
| 6 | operation == `inspect_android_package` | literal in oracle | constant |
| 7 | provider.id == `jadx` | literal in oracle | constant |
| 8 | provider.version matches `\d+\.\d+\.\d+` | regex only | format-only |
| 9 | evidence_id matches `ev_<64 hex>` | regex only | format-only |
| 10 | subject.digest.sha256 == truth.image.sha256 | truth (bytes-bound via check 1) | truth, transitively bytes-bound |
| 11 | subject.format == `apk` | literal | constant |
| 12 | package_name == `truth.axml_declared.strings[4]` | **truth.json, not AXML bytes** | truth, **unbound to AXML bytes** |
| 13 | manifest.text contains `versionCode="1"` | **substring of truth strings[5]/[7]** | truth, **unbound; substring not attribute** |
| 14 | manifest.text contains `versionName="1.0"` | **substring of truth strings[6]/[8]** | truth, **unbound; substring not attribute** |
| 15 | manifest.status == `complete` | literal | constant |
| 16 | class_count == DEX u32 at 0x60 of classes.dex | fixture bytes | **derived-from-bytes** |
| 17 | resource_count == len(truth recipe members) (=3) | truth; count bound to bytes via check 3 | truth, transitively bytes-bound |
| 18 | permissions == `[]` | literal (fixture has no uses-permission, not derived) | constant |
| 19 | signature_verification == `not_performed` | literal | constant |

Count: **6 of 19** directly derived from fixture bytes (1–5, 16). Checks 10 and 17 are bytes-bound only through the premise leg. Checks 12–14 take their expected values from `truth.json` and no byte leg binds `truth.axml_declared` to `AndroidManifest.xml`. The frozen wording "derives … from the authored AXML string table" is therefore **not what the code does**: it reads the string table from truth.json. I verified outside the oracle that the truth strings equal the byte-decoded string pool (`receipts/fixture-byte-readout.log` via `readout.py`), so the committed values are correct today; the oracle itself does not prove it.

Constant 6/7/11/15/18/19 are not copied from the record, but they are also not derived from anything.

## 3. Forgery results (commands and exit codes)

Command pattern: `python3 -B reports/round-81/f_probe4.py <corpus-copy>` and `python3 -B corpus/fixtures/apk-r65/oracle_check.py corpus/fixtures/apk-r65/truth.json <record>`. Logs in `receipts/`.

**A. One field of the real producer record changed per run** (base = landed `corpus/live/runs/round-89/inspection.json`, `receipts/landing-review-summary.json`, logs `receipts/producer-*`):

| Mutation | F4 | Oracle | Load-bearing check |
|---|---|---|---|
| package_name -> `com.example.fabricated` | 11/11, rc 0 | ORACLE FAIL 18/19, rc 1 | check 12 |
| class_count -> 1 | 11/11, rc 0 | ORACLE FAIL 18/19, rc 1 | check 16 |
| subject.digest.sha256 -> `ff…f` | 11/11, rc 0 | ORACLE FAIL 18/19, rc 1 | check 10 |
| manifest.text replaced with `package="com.attacker.fabricated" android:versionCode="999" android:versionName="999"` plus `<!-- android:versionCode="1" android:versionName="1.0" -->` | 11/11, rc 0 | **ORACLE OK 19/19, rc 0** | none — checks 13/14 are substring tests and the comment satisfies them |

The fourth row is the kill-(a) failure. ElementTree parse of the mutated text confirms the actual attributes are `package=com.attacker.fabricated`, `versionCode=999`, `versionName=999`.

**B. Handwritten records (no producer involved)** (`receipts/cases-*`, `receipts/review-summary.json`):

| Case | F4 | Oracle |
|---|---|---|
| Accurate hand-authored record | 11/11 | 19/19 OK |
| provider.version `9.9.9` | 11/11 | 19/19 OK (check 8 is format-only) |
| evidence_id `ev_fff…` | 11/11 | 19/19 OK (check 9 is format-only) |
| manifest contradiction (as in A) | 11/11 | 19/19 OK |
| truth.json strings co-edited to `com.example.fabricated` + record package to match | 11/11 | 19/19 OK (expectations are truth-sourced) |

The accurate hand-authored record passing is expected: the claim disclaims provenance (Q09). The co-edited truth case is not a fixed-truth falsifier, but it confirms check 12 reads truth.json.

**C. F4 gaming with no oracle at all** (`receipts/gaming-minimal-input.json`):
- Adding `live/runs/gaming-minimal.json` = `{"evidence_id":"ev_x","normalized_result":{},"operation":"inspect_android_package"}` to the base corpus gives `F4_COVERAGE=11/11`, rc 0.
- The same file run through the oracle gives `ORACLE FAIL (6/19)`, rc 1, so the oracle does catch it. F4 never reads it.

**Load-bearing counter.** F4 (`f_probe4.py` lines 41–42) counts a file when `evidence_id` is truthy, `normalized_result is not None`, and the `operation` string is in the family set. It never reads any value. F4 is gamed by presence, not content. The oracle is the only content check, so F4 + oracle is only as strong as the oracle, and the oracle's manifest leg is substring-only (case A).

## 4. Family mapping and scope

- `f_probe4.py` sha `4d871971…` equals base and freeze. Its `families` dict is unchanged; the only key that moves is `android`.
- Landing diff of `corpus/live/runs` (`receipts/landing-review-summary.json`): 406 -> 409 files; added = `LEDGER.md`, `inspection.json`, `receipt.json`; removed 0; modified 0. The only F4-counted addition is `inspection.json`, operation `inspect_android_package`, family `android`. No other family's record was added.
- Pins (working = freeze = base where applicable): `oracle_check.py` `44fd1505…`, `fixture.apk` `05d2280f…`, `truth.json` `27303bae…`, `f_probe4.py` `4d871971…`. All unchanged.
- Other edits in the working tree outside C2 scope: `corpus/SOURCES.md` (C1 scribe), untracked `corpus/lessons/round-89.md`, `reports/round-89/carry-in.md`, and an untracked `corpus/__pycache__/` I did not create (every command I ran used `-B` / `PYTHONDONTWRITEBYTECODE=1`).

## 5. Are the two producer runs independent?

Evidence used (all read, none re-run; I did not re-invoke the producer):

- ExecR89Record's driver transcript (`.ufo/waves/round-89/w1/ExecR89Record/invocation-driver-transcript-excerpt.md`, also `history://ExecR89Record`): one bash `for n in 1 2` loop, each iteration a separate `rea inspect-android-package … > runN.json 2> runN.stderr`, with separate wall-clock deltas.
- Retained bytes, which I re-hashed myself: `run1.json` `01af3141…`, `run2.json` `5bbdd189…`, landed `inspection.json` `01af3141…` (`cmp` identical to run1). Both stderr files are 0 bytes; the driver reports rc 0 for both `rea` calls (the driver's rc 1 comes from `cmp`).
- Independence markers present: each run created its own runtime directory (`rea-android-ugg7mp` vs `rea-android-y0GTra`) and its own load_duration (175 ms vs 170 ms); wall 2.464 s vs 2.276 s.
- Structural diff (`receipts/` plus my JSON walk of run1 vs run2): exactly these leaves differ — `evidence_id`; `raw_result.calls[0]` text (JVM map key order); `raw_result.calls[1]` input path and response text (runtime dir + load_duration); `raw_result.loaded.apk_path`. `normalized_result` is equal.

**Not verified:** UTC start/end timestamps and PIDs were not captured and cannot be reconstructed (ExecR89Record and the receipt say so). Temporal independence is therefore shown only by the separate-invocation shape and the per-run runtime directories, not by timestamps.

**Byte identity: FAILED** (`cmp` differs at char 20). The frozen kill (c) is not met, and nothing in the lane argues it was.

## 6. Summary of checks to re-run by the main agent (I did not run them)

- The C2 gate is only meaningful with the oracle reading AXML bytes or with kill (a) added as a frozen control. As frozen, the oracle + F4 admit case A.
- Re-run `python3 -B reports/round-81/f_probe4.py <corpus>` and `python3 -B corpus/fixtures/apk-r65/oracle_check.py corpus/fixtures/apk-r65/truth.json <record>` on the manifest-contradiction record in `receipts/` to reproduce section 3A.

## 7. Residual risk and gaps

- `evidence_id` derivation was never examined; only its per-run variance is observed. The oracle checks its shape only.
- Producer nondeterminism means no retained record is byte-reproducible under rea 6.7.0 + jadx-headless-mcp 0.7.1. The provider's own record also has `environment: null`, which is consistent with the receipt.
- `xd://lsp` is not available on this seat (`No such tool`), so no semantic/LSP references or diagnostics were used. All conclusions are from reading files and running the frozen scripts.
- I did not evaluate C1 (census). No C1 files were touched.

## Coordination

- ExecR89Record: evidence received, no producer re-run requested.
- CriticR89Claims and MutR89Oracle: told the manifest counterexample and the truth co-edit result; neither was treated as a substitute for a fixed-truth falsifier.
- RevengerR89: told kill (a) and kill (c) both fail; this report is the preserved evidence.
