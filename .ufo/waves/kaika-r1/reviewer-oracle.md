# Reviewer oracle — C1 saved-ledger runnability (base `8bbcb4e`)

Scope: `corpus/verify_icon_languages.py` and `corpus/verify_multi_icon_states.py`.
Written by reviewer L2; no verifier, fixture, or saved record was edited.

Provenance of every number below:
- Base text: `git show 8bbcb4e:<path>`.
- Base run: `git archive 8bbcb4e corpus` extracted to `/tmp/revoracle/base` (outside the lane); unmodified scripts run with `python3 -B`.
- Probes: `/tmp/revoracle/tools/count_dynamic.py`, `hist_table.py`, `apply_artifact_only.py` (edits only a `/tmp` copy).
- Working-tree check: `git diff --stat 8bbcb4e -- corpus/verify_* corpus/fixtures corpus/live` printed nothing (no drift at time of writing).

## 1. Assertion inventory (base, static)

Counted with an AST walk over the base file (`require(` call sites and `raise` sites).

| script | `require(` call sites | by function | `raise` sites | total assertion-raising sites |
|---|---|---|---|---|
| verify_icon_languages.py | 28 | check 12, decode 4, file_offset 1, main 4, walk 7 | 3 (helper L11, file_offset L30, main L159) | 31 |
| verify_multi_icon_states.py | 25 | check 9, decode 4, file_offset 1, main 4, walk 7 | 3 (helper L11, file_offset L30, main L159) | 28 |

Line-level sites (base line numbers):

verify_icon_languages.py:
- decode L15 `DOS magic`, L17 `PE signature`, L20 `PE32+ optional header`, L80 `group icon header or record bounds`.
- file_offset L28 `truncated RVA`.
- walk L38 `resource directory cycle`, L40 `directory outside declared region`, L43 `entry table outside region`, L52 `this fixture must use numeric IDs`, L57 `unexpected resource depth`, L60 `leaf must have type/name/language`, L62 `data entry outside directory`.
- check L124 `file identity`, L125 `evidence`, L126 `subject`, L127 `artifact`, L129 `{field}` (loop over 7 decoded fields), L131 `coverage`, L132 `resource identities`, L134 `distinct payloads`, L136 `group shape`, L138 `candidates`, L139 `selection`, L140 `receipt`.
- main L149 `exact delta`, L150 `intact icons`, L151 `three distinct selections`, L155 `forged selection`, L159 raise `forged selection accepted`.

verify_multi_icon_states.py:
- decode L15, L17, L20, L80 (same messages as icon).
- file_offset L28; walk L38, L40, L43, L52, L57, L60, L62 (same messages as icon).
- check L127 `fixture digest`, L128 `Evidence identity`, L129 `subject digest`, L130 `artifact`, L132 `{key}` (loop over 7 decoded keys), L133 `coverage`, L135 `group shape`, L138 `state`, L139 `receipt`.
- main L148 `byte delta`, L149 `first image`, L150 `distinct states`, L155 `forged selective match`, L159 raise `forged second match accepted`.

Dynamic counts at base (unmodified scripts, probe wraps `require`):
- verify_icon_languages.py: outcome `AssertionError: r47: artifact`; 44 `require` evaluations; first failure L127. [observed]
- verify_multi_icon_states.py: outcome `AssertionError: r42: artifact`; 49 `require` evaluations; first failure L130. [observed]

Both match the ledger claim in `SCORECARD.md` (`r47: artifact`, `r42: artifact`).

Dynamic counts after ONLY the artifact-path pin (temp copy, `apply_artifact_only.py`):
- verify_icon_languages.py: `PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED`; 180 `require` evaluations, 69 distinct messages; sole failing evaluation is `forged selection` (the expected rejection). [observed]
- verify_multi_icon_states.py: `PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED`; 248 `require` evaluations, 76 distinct messages; sole failing evaluation is `forged selective match`. [observed]

## 2. Forged-claim rejections (no-weakening baseline)

Base exercises exactly one forged-claim rejection per script. Each must survive any landing.

| id | script (base lines) | forgery | expected rejection message | base acceptance check |
|---|---|---|---|---|
| F1 | verify_icon_languages.py:152-159 | copies saved r48 record, sets `icon_groups[0].images[0].same_language_resource_index = 0` (decoded value is None; group language 1041 has no same-language candidate) | `forged selection` (L155) | `except AssertionError` (L156) prints PASS; no message match |
| F2 | verify_multi_icon_states.py:151-159 | copies saved r45 record, sets `icon_groups[0].images[1].same_language_resource_index = 1` (decoded value is None) | `forged selective match` (L155) | `except AssertionError` (L156) prints PASS; no message match |

Tamper-rejection controls on saved records (each a `require` that rejects a changed record or receipt):
- icon: file identity L124, evidence L125, subject L126, artifact L127, every decoded field L129, coverage L131, candidates L138, selection L139, receipt L140 (`exit_code`, `fixture_sha256`, `evidence_id`, `stdout_sha256 == H(raw)`).
- icon cross-row: exact one-byte delta L149, intact icons L150, three distinct selections L151.
- multi: fixture digest L127, Evidence identity L128, subject digest L129, artifact L130, every decoded key L132, coverage L133, state L138, receipt L139 (`exit_code`, `fixture_sha256`, `evidence_id`, `stdout_sha256 == H(raw)`).
- multi cross-row: byte delta L148, first image stable L149, distinct states L150.

Base gaps (not weakenings; do not remove existing controls to "match"):
- Base receipt check does NOT pin `receipt['command']`. The 7c3ce19 pattern adds it.
- Base `except AssertionError` accepts any assertion as a forged-claim rejection. A landing may tighten this to a message match (7c3ce19 pattern). Loosening it would be a weakening.

## 3. Historical identity (HIST table)

Root (shared by both scripts; pinned in 7c3ce19 as `HIST=Path('/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus')`):
`/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus`

Saved-record identity per script input (observed by `hist_table.py` on base snapshot; all true):

| round | read by | saved `normalized_result.artifact.path` | saved `subject.local_path` | saved receipt `command` path | receipt keys |
|---|---|---|---|---|---|
| r42 | multi | HIST + `/fixtures/pe-r42/fixture.exe` | same | HIST path, `npx -y rea-agents@6.4.0 inspect-pe-resources … --format json` | command, evidence_id, exit_code, fixture_sha256, stdout_sha256 |
| r43 | multi | HIST + `/fixtures/pe-r43/fixture.exe` | same | same pattern | same |
| r44 | multi | HIST + `/fixtures/pe-r44/fixture.exe` | same | same pattern | same |
| r45 | multi | HIST + `/fixtures/pe-r45/fixture.exe` | same | same pattern | same |
| r47 | icon | HIST + `/fixtures/pe-r47/fixture.exe` | same | same pattern | same |
| r48 | icon | HIST + `/fixtures/pe-r48/fixture.exe` | same | same pattern | same |
| r49 | icon | HIST + `/fixtures/pe-r49/fixture.exe` | same | same pattern | same |

Observed: 7/7 artifact paths under HIST; 7/7 subject paths under HIST; 7/7 receipt commands equal the HIST form; 7/7 `receipt.stdout_sha256 == sha256(inspection.raw.json)`; 7/7 `receipt.fixture_sha256 == sha256(fixture.exe)`; 7/7 `receipt.exit_code == 0`; 7/7 receipt `evidence_id` equals record `evidence_id`.

Receipts carry NO `duration_seconds` key (7/7). The 7c3ce19 receipt clause requires `receipt['duration_seconds']`; copying that clause verbatim would not be a clean pass (see §5).

Current-tree fixture paths the scripts read: `ROOT/fixtures/pe-rNN/fixture.exe` and `ROOT/live/runs/round-N/{inspection.raw.json,producer-receipt.json}`. Bytes come from ROOT; expected path strings come from HIST only. Do not copy expected values from the saved field under test.

Oracle pins (copy the full literals from base; they must remain byte-identical after landing):

- `verify_icon_languages.py` `EXPECTED`, base L104-114: 47 → fixture sha256 `cc02c78b44883f2217b7a8f82fa6fafc990ae6d0ca71f0eab8a3fbc4f2ba44ba`, evidence `ev_8ed889836291b900a28c7e3816167392cc5042301e069cb2a647b6a98e8d4421`, group language 1036, selected index 1; 48 and 49 likewise (group languages 1041 and 1033; selected None and 0).
- `verify_multi_icon_states.py` `EXPECTED`, base L104-117: 42–45 → fixture sha256 and evidence IDs as written at base L105-116, plus the expected four-field state tuples at base L107, L110, L113, L116.

Full literals are not repeated here on purpose: abbreviated hashes are easy to mistype. Compare against `git show 8bbcb4e:corpus/<script>` directly.

## 4. Input SHA table (base `8bbcb4e`, `git show 8bbcb4e:<path> | sha256sum`)

Each script reads only the files below (plus its own source). Check: none overlap between the two scripts.

| path | sha256 | read by |
|---|---|---|
| corpus/verify_icon_languages.py | 84d2a5afee724a33afe949ba37584a4561ee4865fbbdbeef58b67a406c8eb1ca | (script itself) |
| corpus/verify_multi_icon_states.py | 5fec3e2b1440cba468c1bf42b894eda635a869aaba6b7b1209c0e99e27401803 | (script itself) |
| corpus/fixtures/pe-r42/fixture.exe | 3ab5008b436eb4facd3966767a507fa4b1625160532585a09a6af2f752b38941 | multi |
| corpus/fixtures/pe-r43/fixture.exe | 146bdde3ec3ce9f23b75b31f7a9d2fc0cbc8826f2a5d239a83fd82694f4c31a2 | multi |
| corpus/fixtures/pe-r44/fixture.exe | bb2680c1ceaa3ce6e4921e078e2548f06f164d9598da2bff6c895890b73bc5fb | multi |
| corpus/fixtures/pe-r45/fixture.exe | 1d526ab14ba29a133cafd720395920b0067d8d00c40a5e1216e097272c176669 | multi |
| corpus/fixtures/pe-r47/fixture.exe | cc02c78b44883f2217b7a8f82fa6fafc990ae6d0ca71f0eab8a3fbc4f2ba44ba | icon |
| corpus/fixtures/pe-r48/fixture.exe | dc6483a985f12dbc0da4122db64565ed76c14a5e76ea8758658b4a54c35bc129 | icon |
| corpus/fixtures/pe-r49/fixture.exe | d26b165ee497da494e1b5605a72877597030de53f94eba674c905bffbb079114 | icon |
| corpus/live/runs/round-42/inspection.raw.json | 7163c758c776f8aa71543ae16be671d28e241abf9a310afd0a5ca846121d4b9c | multi |
| corpus/live/runs/round-43/inspection.raw.json | d84d8db6351c690918ae1b35fde4c8a099a46f375758930aa3438d468cf48d49 | multi |
| corpus/live/runs/round-44/inspection.raw.json | 2a14dc2af922b6ba0645087782f7eab5fac4b300954b3a25625cbf1b4d5e2e19 | multi |
| corpus/live/runs/round-45/inspection.raw.json | 20fd361deef320f3e57036a850d34f2fb5e711de317e816b40b4a50f60a01ec7 | multi |
| corpus/live/runs/round-47/inspection.raw.json | e12ff95b78b57fde1bdc4ec7acf8142b2e4d242c2bfa7ae82307760be260e65c | icon |
| corpus/live/runs/round-48/inspection.raw.json | 3a21b0e9ff72140360f72229810f0787265e07b86ec9af5148708128ade53325 | icon |
| corpus/live/runs/round-49/inspection.raw.json | 202e95f029461ffd8dd092114bcdcc88f654b85cbee226036dd309fb96e4830a | icon |
| corpus/live/runs/round-42/producer-receipt.json | 05bf8bf6dd33719a3db6f6d9ff29a894d8191c627e14c7e746611f7c882119de | multi |
| corpus/live/runs/round-43/producer-receipt.json | 7178a0721a1e9df6dc6e92a3336c3fe4329e7a5c3d4d3a4f8a2534bbbe6b9315 | multi |
| corpus/live/runs/round-44/producer-receipt.json | bddd2faac42e6475cb613a7d187f3178a9d3ad334b5ef96aca8e10354401be7f | multi |
| corpus/live/runs/round-45/producer-receipt.json | ef67f2a1080e9e80d4b745f49090b011bc0d4c55e9e6bb258b145ad436fa4beb | multi |
| corpus/live/runs/round-47/producer-receipt.json | 3b5d3bdaad18cf7ab0c34643851e205353a979dff08133f48f54f0617e558ac5 | icon |
| corpus/live/runs/round-48/producer-receipt.json | 7499a494eff905e2e3636f4a266ba23aec3e352f629d5de59bd4d1a2978a9e19 | icon |
| corpus/live/runs/round-49/producer-receipt.json | 7e6f14bb3bee90524d042c4d75b0de63e952e835f99b81d5b399165351985e15 | icon |

Working-tree spot check (`sha256sum` in lane): both scripts, r42 and r47 fixtures, r47 raw and receipt match the table. `git diff --stat 8bbcb4e` over these paths is empty.

Not read by either script (do not count as inputs): `corpus/fixtures/pe-rNN/truth.json`, `live/runs/round-NN/LEDGER.md`, `reviewer-verify.py`, `reviewer.md`.

## 5. Prediction: first failing assertion after the artifact-path fix only

By reading [INFERENCE]:
- Pinning the expected artifact path to HIST (7c3ce19 pattern) clears L127 (icon) and L130 (multi), because all 7 saved artifact paths equal the HIST form.
- Every later `require` compares values the probe confirmed equal (fixture sha256, evidence_id, subject digest, decoded fields, coverage, receipt exit/sha/eid/stdout). No failure is expected.
- The receipt-command clause is not a blocker: 7/7 saved receipt commands match the HIST form.

Observed (temp copy only): artifact-only patch makes BOTH scripts PASS (§1). So no assertion fails first; the artifact-path fix alone is sufficient for CALIBRATION 2/4 → 4/4 for these two scripts, subject to the other two names in the scorecard set (`verify_icon_states.py`, `verify_named_multi_icon_states.py`), which this oracle does not cover.

Hazard for the landing [INFERENCE from reading + observed key absence]:
- If the landing copies the 7c3ce19 receipt clause verbatim, it adds `isinstance(receipt['duration_seconds'], …)`. Those keys are absent in all 7 receipts. The first failure would be a `KeyError` at the receipt line (icon L140 / multi L139), not an `AssertionError`, so the script would crash instead of reporting a named `receipt` failure. The landing must not add a `duration_seconds` requirement unless the saved receipts carry it, and must not alter saved receipts to add it.

## 6. Post-landing no-weakening checklist

Run from the landed lane (executor/main agent runs; reviewer does not execute):
1. Re-hash the 16 inputs and both scripts' base versions; every input hash must equal §4 (`git -C <lane> show 8bbcb4e:<path> | sha256sum` vs. `sha256sum <lane>/<path>`). Verifiers may change; inputs must not.
2. Count `require(` sites with the §1 AST probe: icon ≥ 28, multi ≥ 25; `raise` sites ≥ 3 each. Removals are weakenings.
3. Confirm F1 (`forged selection`) and F2 (`forged selective match`) still exist, still mutate the same field, and still reject. Tightening the `except` to a message match is allowed; removing the `except`/rejection is not.
4. Confirm §3 `EXPECTED` tuples (hashes, evidence IDs, group language, selected index, state) are byte-identical to base.
5. Confirm the artifact expectation is derived from HIST, not from `record['normalized_result']['artifact']` (no self-copy from the saved field under test).
6. Confirm the receipt check does not require `duration_seconds` (see §5) and does not weaken `exit_code`, `fixture_sha256`, `evidence_id`, or `stdout_sha256 == H(raw)`.
7. Re-run each verifier with `python3 -B corpus/<script>.py` in the landed lane; expect exit 0 and the PASS line. (Main agent runs; this is the only execution this document asks for.)
8. `git diff --stat 8bbcb4e -- corpus/fixtures corpus/live` must be empty (saved records and fixtures unchanged).
