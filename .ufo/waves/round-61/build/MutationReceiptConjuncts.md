# Round 61 — other receipt-conjunct mutation probe

Axes: calibration (name detector blind spots); experimental integrity (passing baselines, isolated mutants, exact restoration).
Seat: `CloseChousa26.MutationReceiptConjuncts-10`; RUNS only, no production implementation or claim adjudication.
Observed base: `git -C /tmp/revenger-r61-MutationReceiptConjuncts-10 rev-parse HEAD` → `e0a4b0c4348ef1fade46539f520e94fa140c4d8a`.
Private clone created with the assigned `git clone -q --no-hardlinks` and base-pinned branch switch.
Extraction executed: `git -C /tmp/revenger-r61-MutationReceiptConjuncts-10 archive --format=tar e0a4b0c4348ef1fade46539f520e94fa140c4d8a corpus | tar -x -C /tmp/revenger-r61-MutationReceiptConjuncts-10-archive` (exit 0).

## Detector and mutation contract
`P=/tmp/revenger-r61-MutationReceiptConjuncts-10`; each case is a separate `cp -a ${P}-archive ${P}-${family}-${field}` tree.
`icon` means `script=verify_icon_languages.py`; `multi` means `script=verify_multi_icon_states.py`.
For each table row, the executed detector was `python3 -B ${P}-${family}-${field}/corpus/${script} --self-test`, with all variables expanded, `cwd=/`, and a 300-second timeout.
The same command/path ran on pristine, mutated, then restored bytes; independent cases ran concurrently within each phase.
Each mutant deletes ONLY the listed comparison and its adjacent `and`; all other comparisons, including `receipt['command']`, remain.
Expected kill: pristine exit 0, mutated nonzero, restored exit 0. A failed pristine detector is inconclusive, not a kill.

## Observed outputs
Every invocation had empty stderr. Every `icon` invocation printed exactly this line followed by a newline (output I):
```text
PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
```
Every `multi` invocation printed exactly this line followed by a newline (output M):
```text
PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
```
`exits` below is pristine / mutated / restored. Sites are base-relative under `corpus/`.

| family | field / removed comparison | base site | exits | output | mutated script SHA-256 | outcome |
|---|---|---|---|---|---|---|
| icon | `exit_code`: `receipt['exit_code']==0` | `verify_icon_languages.py:143` | 0 / 0 / 0 | I | `9fb561b7e8a979b1a43026b71c78d46179e03339fbcff8c753b5ba8e4dd05145` | survived |
| icon | `fixture_sha256`: `receipt['fixture_sha256']==expected_hash` | `verify_icon_languages.py:143` | 0 / 0 / 0 | I | `9c77837b43ccfcb9a40d9619bbcc8a32754bd3d913e6d55661a9b5c1f25b9b13` | survived |
| icon | `evidence_id`: `receipt['evidence_id']==eid` | `verify_icon_languages.py:143` | 0 / 0 / 0 | I | `b6f17457144a84be4c6f24962492775de5b7390e7a62b9683b5a96d3f8e7d0b1` | survived |
| icon | `stdout_sha256`: `receipt['stdout_sha256']==H(raw_bytes)` | `verify_icon_languages.py:144` | 0 / 0 / 0 | I | `19a16ceb3d8f3bd7dfc8e5b858ff4a8fdcd0b0028bb808ee413adb23afc102bb` | survived |
| multi | `exit_code`: `receipt['exit_code']==0` | `verify_multi_icon_states.py:143` | 0 / 0 / 0 | M | `cda2d42170893a0122268ae80ff47b6ed9f7e1062bd83ad212918e196cc5d137` | survived |
| multi | `fixture_sha256`: `receipt['fixture_sha256']==expected_hash` | `verify_multi_icon_states.py:143` | 0 / 0 / 0 | M | `e3ca2a7d3dee05ba8fde95464b36650af5b306840674abbfcca65ad140ac208b` | survived |
| multi | `evidence_id`: `receipt['evidence_id']==evidence_id` | `verify_multi_icon_states.py:144` | 0 / 0 / 0 | M | `dff9d5d4298a1ade8bed4aff76ec3d8fcac3a8cc5925bc989f84e2bedef7c12d` | survived |
| multi | `stdout_sha256`: `receipt['stdout_sha256']==H(raw_bytes)` | `verify_multi_icon_states.py:144` | 0 / 0 / 0 | M | `af9ebb49661e22b5c75382bbad8b39ecb608cb5971efe96c0c08d6ef92d02025` | survived |

## Restoration evidence
Before SHA-256 = restored SHA-256 for every `icon` case: `ed0ad16655e3e3c8989c80fb92c0fc35bf35dbb7dd1007f2b9d4be1d84c6bd95`.
Before SHA-256 = restored SHA-256 for every `multi` case: `5b75339c0b80ed619c08af1d87b73938e6d1a607ed0baebc89258cf6d17f49f8`.
Restoration ran in `finally`: `cp -p ${P}-archive/corpus/${script} ${P}-${family}-${field}/corpus/${script}` → exit 0, stdout/stderr empty in all eight cases.
`cmp -s ${P}-archive/corpus/${script} ${P}-${family}-${field}/corpus/${script}` → exit 0 in all eight cases (exact original bytes).
After restored detector runs, `diff -qr ${P}-archive/corpus ${P}-${family}-${field}/corpus` → exit 0, stdout/stderr empty in all eight cases: entire corpus, including saved records and fixtures, matches the archive.
Only this report was written in the live lane; verifier mutations were confined to private archive copies and restored. No production patch is supplied.

## Claim boundary
`reports/round-61/claims.md:42-62` claims a kill for receipt-command mutant b, not mutation sensitivity for every receipt field.
Observed residuals at the registered base: `exit_code`, `fixture_sha256`, `evidence_id`, and `stdout_sha256` deletions survive in BOTH scripts (8/8); none is covered by that named C2 mutant.
The controls at `corpus/verify_icon_languages.py:156-163` and `corpus/verify_multi_icon_states.py:155-163` forge decoded icon-selection values, not these receipt fields.
These are detector-coverage findings, not authorization to expand C2 or weaken its contract. Post-change behavior was not tested by this base-only assignment.
Totals from the 24 captured detector invocations: 8/8 pristine pass, 8/8 mutants survive, 8/8 restored pass; killed 0, inconclusive 0.
Installs/updates: none. No producer calls, external targets, bytecode execution, build/lint/formatters, or subagent dispatch.
VERDICT: All eight other receipt-conjunct deletion mutants survive at the registered base and lie outside C2's command-only claim; all scratch corpus bytes were restored exactly.
