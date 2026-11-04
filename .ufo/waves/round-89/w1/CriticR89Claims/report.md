# CriticR89Claims — falsification of round-89 frozen claims (C1, C2)

Seat: CriticR89Claims (leaf critic, godspeed). Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.
Freeze: `c84339c`; base `2b017fa3c616a84b7b491e3312029fa8a8c076e6`.
Scope: read-only. No lane file edited. No git/jj mutation. No MANIFEST/.ufo/state/.scratch touched. No tool installed or upgraded (zero installs; nothing needed).
Scratch `/fast/scratch/hyaku/revenger-r89/CriticR89Claims` (TMPDIR passed explicitly); receipts copied to `.ufo/waves/round-89/w1/CriticR89Claims/receipts/` and scratch deleted before yield.

## Verdicts

| claim | verdict | one-line reason |
|---|---|---|
| C1 freshness (`CENSUS_STALE_UNFLAGGED` 10 -> 0) | **FAIL** | Target 0 is unreachable by any truthful row text on this host: K04 demands `ghidra` = present-without-absent and `ida` = absent-without-present in the same scored text. Truthful minimum = 1 finding; pure append = 2. Reaches 0 only when host PATH is faked. |
| C2 coverage (F4 10/11 -> 11/11 + ORACLE OK 19/19) | **FAIL** | Both counters pass a fabricated record (19/19 + F4 11/11). Frozen kill rule (c) byte-identity is NOT met as measured (`cmp` differs at byte 20). |
| Separability | **PASS** (numeric) | C1-only tree: F4 stays 10/11. C2-only tree: census stays 10. The leak is in the target, not the separation. |
| No-work control | **PASS** | Untouched base: census 10 (exit 1), F4 10/11 (exit 0). |

Round not admissible on these two claims as frozen.

## C1 — census counter (`corpus/census_reprobe.py`, sha256 `c3127ffc…648b`, matches `reports/round-89/instrument-pins.log`)

Pin check: `sha256sum` over the freeze-commit copy reproduces `c3127ffc18a54f85f01e2fb88f50b5db694484588e5b7467ae5567ffdd3b648a` (oracle `44fd1505…` and f_probe4 `4d871971…` also match the pins).

Live values (`live()` on this host):
- K04 `ghidra`: `['present']`, forbidden `['absent']`
- K04 `ida`: `['absent']`, forbidden `['present']`

Measured:

```
$ python3 -B freeze/corpus/census_reprobe.py --root base
CENSUS_ROWS=18  ... (10 mismatch lines) ...  CENSUS_STALE_UNFLAGGED=10   EXIT=1      # base red reproduced
$ python3 -B freeze/corpus/census_reprobe.py --root c2-only      (base + record + oracle)
CENSUS_STALE_UNFLAGGED=10   EXIT=1                                                  # separability leg holds
$ python3 -B freeze/corpus/census_reprobe.py --root c1-only      (base + truthful append, K04 both halves)
CENSUS_MISMATCH K04 presence:ghidra states 'absent' against the live value
CENSUS_MISMATCH K04 presence:ida states 'present' against the live value
CENSUS_STALE_UNFLAGGED=2   EXIT=1
$ python3 -B freeze/corpus/census_reprobe.py --root k04-minimum  (K04 = "ghidra present; ida off PATH")
CENSUS_MISMATCH K04 presence:ida does not state live value 'absent'
CENSUS_STALE_UNFLAGGED=1
$ python3 -B freeze/corpus/census_reprobe.py --root shim-cheat  (c1-only + last-occurrence K04 row "ghidra present; ida present")
... CENSUS_STALE_UNFLAGGED=1  (no shim: ida row fails on "present")
$ env PATH=<scratch>/shimbin:$PATH python3 -B freeze/corpus/census_reprobe.py --root shim-cheat
CENSUS_ROWS=18
CENSUS_STALE_UNFLAGGED=0
```

Note on exit code: the no-shim `shim-cheat` line was run with `|| true`, so the shell printed `EXIT=0` for it; the counter's own exit path is 1 when the count is >0, and the stdout count is the evidence.

Selftest: `python3 -B freeze/corpus/census_reprobe.py --selftest` -> `CENSUS_SELFTEST=pass`, exit 0 (9 legs, as in `reports/round-89/census-selftest.log`; reproduced).

Findings:
1. **K04 is unsatisfiable on any truthful text.** `check_rows` scores one string per row and tests every probe of that row against it. `ghidra` forbids `absent`; `ida` forbids `present`. Any K04 line that mentions both states fails one half. Any K04 line that omits one state fails the other half's required token. Measured floor on an otherwise-corrected tree: 1 finding (the wording "off PATH" avoids the word "absent" and still fails the `ida` token rule). Zero is unreachable by wording. Only deletion of the K04 row (`row-absent`, counted as a finding) or changing the frozen `ROWS` dict prevents the single residual.
2. **Counting unit is probe-findings, not rows.** `findings` is appended per probe spec, so the target counts findings. Base's 10 is 10 findings over 10 rows only by coincidence (reviewer reports base under `env -i PATH=...` = 16 findings/14 rows; not reproduced by me).
3. **Target reachable by faking the host (not blocked by any frozen kill rule).** `shutil.which` reads PATH. With `ghidra` and `ida` stubs on PATH, K04 `ghidra present; ida present` scores 0 and the whole census reaches `CENSUS_STALE_UNFLAGGED=0`, exit 0. The frozen rules check selftest, junk-token control and base-tree-10 on the real host; none detects an environment-faked presence. This is the cheapest cheat that reaches the frozen target.
4. The census check is lexical (substring of two cells). It verifies wording agreement with a live probe at the moment of run; it records no observation time, command, or evidence. Naming: this is calibration-of-wording on the freshness axis, not freshness evidence.
5. Blocked cheats (verified): deleting the census rows -> `row-absent` findings (18); deleting the census files -> `could-not-evaluate`, exit 2. Blind-token junk control: `reports/round-89/junk-control.log` scores 7 (receipt, not re-run by me).

## C2 — coverage (F4 + oracle)

Pins: `reports/round-81/f_probe4.py` `4d871971…`, `corpus/fixtures/apk-r65/oracle_check.py` `44fd1505…` (match `instrument-pins.log`).

Measured on the frozen-candidate trees (`c2-only` = base + ExecR89Record `run1.json` + frozen oracle):

```
$ python3 -B freeze/reports/round-81/f_probe4.py base/corpus          -> F4_COVERAGE=10/11 score=9.09    EXIT=0   (no-work control holds)
$ python3 -B freeze/reports/round-81/f_probe4.py c2-only/corpus       -> F4_COVERAGE=11/11 score=10.00   EXIT=0
$ python3 -B freeze/corpus/fixtures/apk-r65/oracle_check.py truth.json c2-only/.../android.json
ORACLE OK (19/19 checks)   EXIT=0
```

Cheats that pass both nominal counters:

1. **Fabricated minimal record (`forged.json`).** Hand-written JSON with `evidence_id` = `ev_` + 64 zeros, `provider` jadx 0.0.0, subject sha256 = fixture digest, `normalized_result` = `package_name com.example.r65`, `manifest.text` = `versionCode="1" versionName="1.0"`, `class_count` 0, `resource_count` 3, `permissions` [], `signature_verification` `not_performed`. Result: `F4_COVERAGE=11/11`, `ORACLE OK (19/19)`, exit 0. No `raw_result`, no `engine`, no producer run. The frozen claim text itself says "F4 alone is not the claim ... a fabricated record would move it", and the oracle has no check that binds `evidence_id` to producer output. Not blocked by kill (a) (which tests only a `package_name` rewrite).
2. **Contradictory manifest text (XML-comment forgery).** `manifest.text` = `<manifest package="com.attacker.fabricated" versionCode="999" versionName="999"><!-- versionCode="1" versionName="1.0" --></manifest>` with `package_name` = `com.example.r65`. Result: `ORACLE OK (19/19)`, F4 11/11. Manifest checks at `oracle_check.py:110-114` are raw substring `in` tests on the text; they never parse XML and never check attribute values against each other. Reviewer `ReviewerR89C2` reports the same result independently.
3. **Truth co-edit.** Editing `truth.json` `axml_declared.strings` (package -> `com.example.not_in_apk`, versions -> `999` / `9.9`) with a matching record gives `ORACLE OK (19/19)`. The expectations come from `truth.json`, not from parsing `fixture.apk`; the premise leg checks only member digests and sizes, not `axml_declared`. The frozen claim says expectations are "derived from the bytes"; this check is not. (Reviewer treats the fixed-truth variant, #1–2, as the stronger control; both fail.) I confirmed `readout.py --fact axml_string_pool` reproduces the same strings from the bytes, so the honest path is consistent, but the oracle does not read them.
4. **Kill rule (c) byte-identity: NOT MET (measured).** Two independent producer runs (ExecR89Record, `rea inspect-android-package corpus/fixtures/apk-r65/fixture.apk --format json`):

```
$ cmp .../ExecR89Record/run1.json .../ExecR89Record/run2.json
.../run1.json .../run2.json differ: byte 20, line 1          EXIT=1
01af3141d79027a3bae53b6482779d3e9c89446ab6ca09b408a6cb266f321c76  run1.json
5bbdd189cd19dd1b181b4850b95fe07d077bc4031c70b25fec5006ca0d72ce00  run2.json
```

ExecR89Record's delta enumeration (exact stdout, 4303 bytes each): `evidence_id`; the random `rea-android-XXXXXX` runtime dir in three paths; JVM HashMap key order in `calls[0]`; `load_duration_ms` 175 vs 170. `normalized_result` identical. I did not reproduce the enumeration field by field; the cmp result is my measurement.

Blocked (verified/receipted): oracle tamper control `package_name` rewrite -> `ORACLE FAIL (18/19)`, exit 1 (`reports/round-89/oracle-tamper-control.log`, receipt not re-run).

Naming: C2 is coverage in the sense that `inspect_android_package` moves from absent to present in the operation census (F4 10->11 is real measured surface movement on the counter). The "recorded" surface is a presence check on keys (`evidence_id` shape, `normalized_result`) plus substring checks, so the coverage is of an unauthenticated record, not of a verified producer output.

## Reported by peers, not reproduced by me

- ReviewerR89C1: `--selftest` has no coverage of the forbidden-opposite branch (mutation with `bad=[]` stays green); a `main()` that always prints 0 passes selftest (mutation battery in `.ufo/waves/round-89/w1/ReviewerR89C1/receipts/`).
- ReviewerR89C1: base census under `env -i PATH=/usr/local/bin:/usr/bin:/bin` = 16 findings / 14 rows (environment-dependent score).
- ReviewerR89C2: strict fixed-truth XML-comment forgery and three package/class/digest one-field forgeries rejected at 18/19 (their receipts).

## Cheats not blocked by frozen kill rules (ranked by cheapness)

1. Stub `ghidra` and `ida` on PATH -> census 0. (Measured.)
2. Add a `shutil`-visible `ida` binary only (the `K04` text then needs only `present`), same mechanism. (Same class as 1.)
3. Fabricated record with 19/19 fields and no producer run -> F4 11/11 and oracle 19/19. (Measured.)
4. XML-comment or substring-contradictory manifest -> 19/19. (Measured.)
5. Edit `truth.json` `axml_declared` strings together with the record -> 19/19. (Measured.)
6. Edit the frozen `ROWS` dict or the counter itself -> the frozen predicate changes; blocked only by the sha pin at closure, not by any counter-internal kill rule.

Blocked: row deletion (row-absent), census-file deletion (exit 2), junk-token padding (7), package_name tamper (18/19), `--selftest` regressions (pass/fail is checked).

## Recommended

Any round that wants these claims to hold needs: (a) C1 — rescope to rows whose verdict depends on one probe each, or let a K04 row state its two probes on separate lines with a per-probe scope; pin PATH or record `which` paths in the receipt; (b) C2 — the oracle must parse the manifest and check `evidence_id` against a producer run, and the byte-identity leg must be restated as a volatile-field-normalized equality (a frozen-claim change, so an L1 decision, not this seat's).
