# Round 61 — independent kaika twelve-mutant reproduction
2026-10-21. Axes: calibration (rejection vs acceptance), operability (pristine/restored controls), preservation (exact bytes). No round-admission judgment.
Observed base: `git -C /tmp/revenger-r61-MutationKaika12Repro rev-parse HEAD` → `e0a4b0c4348ef1fade46539f520e94fa140c4d8a`.
Comparison target: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/kaika-r1/mutation-post.md:8-35`; no code from `reports/round-61/measure.py` was read or reused.
Archive command: `mkdir -p /tmp/revenger-r61-MutationKaika12Repro-archive && git -C /tmp/revenger-r61-MutationKaika12Repro archive --format=tar e0a4b0c4348ef1fade46539f520e94fa140c4d8a corpus | tar -x -C /tmp/revenger-r61-MutationKaika12Repro-archive` → exit 0.
Run: `python3 -B /tmp/revenger-r61-MutationKaika12Repro/r61-MutationKaika12Repro.py --archive /tmp/revenger-r61-MutationKaika12Repro-archive --scratch /tmp/revenger-r61-MutationKaika12Repro-cases --output /tmp/revenger-r61-MutationKaika12Repro-results.json` → exit 0; Python 3.14.8.
Detector in all three phases: `/usr/bin/python3 -B /tmp/revenger-r61-MutationKaika12Repro-cases/{icon,multi}-{mutant}/corpus/{verifier}`, `cwd=/`, 15-second timeout; two isolated cases concurrently. JSON retains actual executable/arguments and complete combined output.
Expected detector: plain verifier run rejects a/c/d1 at artifact, d2 at receipt, d3 at resources; kaika records b as undetected. A failed control or timeout is INCONCLUSIVE, never a kill.
Each of 12 cases received a fresh complete archive copy; each ran pristine → one mutation → exact restoration → restored detector. All 36 detector invocations completed.
I = `verify_icon_languages.py`; M = `verify_multi_icon_states.py`. The following are observed mutated exit codes and exact last lines.
| Verifier | Mutant | Exit | Last line | Result |
|---|---|---|---|---|
| I | a | 1 | `AssertionError: r47: artifact` | KILLED |
| I | b | 0 | `PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED` | SURVIVED |
| I | c | 1 | `AssertionError: r47: artifact` | KILLED |
| I | d1 | 1 | `AssertionError: r47: artifact` | KILLED |
| I | d2 | 1 | `AssertionError: r47: receipt` | KILLED |
| I | d3 | 1 | `AssertionError: r47: resources` | KILLED |
| M | a | 1 | `AssertionError: r42: artifact` | KILLED |
| M | b | 0 | `PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED` | SURVIVED |
| M | c | 1 | `AssertionError: r42: artifact` | KILLED |
| M | d1 | 1 | `AssertionError: r42: artifact` | KILLED |
| M | d2 | 1 | `AssertionError: r42: receipt` | KILLED |
| M | d3 | 1 | `AssertionError: r42: resources` | KILLED |
I pristine/restored (each 6/6): exit 0; last line `PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED`.
M pristine/restored (each 6/6): exit 0; last line `PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED`.
Runner output: `KILLED 10/12; SURVIVED 2/12; INCONCLUSIVE 0/12` — matches all twelve historical exit/finding classifications; both b survivors remain coverage findings.
## Exact sites and prose ambiguities
Paths below are inside each isolated case's `corpus/`; code sites were selected through Python AST, JSON edits preserved all bytes outside the declared field.
a: `verify_icon_languages.py:130`, `verify_multi_icon_states.py:133`: only artifact expectation `str(hist)` → `str(fixture)`. “Current path” lacks an exact expression; interpreted as the copied fixture's absolute path, not cwd.
b: I `:144-145`, M `:143`: delete the sole `receipt['command']==...` operand and one adjacent `and`; all other receipt conjuncts remain. No substantive ambiguity at this base.
c: both scripts `:10`: historical `HIST` assignment value → `root`. AMBIGUOUS “copy root”: chosen copied `corpus/`, not its enclosing case directory; no historical mutation patch was supplied.
d1: `live/runs/round-47/inspection.raw.json:1` for I, round-42 equivalent for M: only `normalized_result.artifact.path` → that case's copied `fixtures/pe-r{round}/fixture.exe` absolute path. AMBIGUOUS round selection/current-path wording; first checked round chosen.
d2: `live/runs/round-47/producer-receipt.json:2` for I, round-42 equivalent for M: only `command` → `forged-command-r61`. AMBIGUOUS forged value/round; first checked round chosen.
d3: each first-round `inspection.raw.json:1`: only `normalized_result.resources[0].name.id` 1 → 2. AMBIGUOUS “resources[0] id”: type/name/language all contain an id, and replacement value is unstated; name.id was chosen explicitly.
d1/d3 did not rehash receipts or alter fixture bytes; observed artifact/resources failures precede the receipt check (I `:130-145`, M `:133-144`). Outcomes reproduce the table, not an unknowable byte-identical historical mutant.
## Restoration and SHA-256 evidence
JSON output: all 12 before/restored target hashes equal; all 12 full-tree manifests equal; each mutation changed exactly one file; pristine/mutant detector runs themselves changed no files.
Archive and every restored copy contain 466 files; SHA-256 of canonical sorted `{relative_path:{bytes,sha256}}` manifest before/after = `ec3f1a19596dc89f961f5b32335ae786ee33170e446320d0f32f95ee03cb6a8b`; archive unchanged.
Before = restored hash aliases (the two phases' actual hashes are separately retained in JSON):
I (`verify_icon_languages.py:1`): `ed0ad16655e3e3c8989c80fb92c0fc35bf35dbb7dd1007f2b9d4be1d84c6bd95`.
M (`verify_multi_icon_states.py:1`): `5b75339c0b80ed619c08af1d87b73938e6d1a607ed0baebc89258cf6d17f49f8`.
IR (`live/runs/round-47/inspection.raw.json:1`): `e12ff95b78b57fde1bdc4ec7acf8142b2e4d242c2bfa7ae82307760be260e65c`.
IC (`live/runs/round-47/producer-receipt.json:1`): `3b5d3bdaad18cf7ab0c34643851e205353a979dff08133f48f54f0617e558ac5`.
MR (`live/runs/round-42/inspection.raw.json:1`): `7163c758c776f8aa71543ae16be671d28e241abf9a310afd0a5ca846121d4b9c`.
MC (`live/runs/round-42/producer-receipt.json:1`): `05bf8bf6dd33719a3db6f6d9ff29a894d8191c627e14c7e746611f7c882119de`.
| Case | Before/restored alias | Mutated SHA-256 |
|---|---|---|
| I/a | I | `82d5e168d76d42e5ee30677f076f04cf47440c3b90fbcf527782e44318433c07` |
| I/b | I | `4d72c3fb833be66227cef2dd799633e0b908dff75b45ed6328178287f51d4500` |
| I/c | I | `18d16790694455b6dab548bc28e8b808746ca02b2aca92f5740728563187fc38` |
| I/d1 | IR | `0d3da034a4b6eb8a3ccc64d27175815e8e0e3465ebf171b962cfe248b52cad6d` |
| I/d2 | IC | `ad2774e8805c20c071f094ed696915f5f2bf851ad0e47ec8a8f7dbc531937add` |
| I/d3 | IR | `c6acf1a55b820c7ceb86301699d1d775921ca9c6f3d0bfe0f99d9883132af376` |
| M/a | M | `3804d86c6265bae7c476fbb5c043ab5e6fe0255307e86dda93846242b51c821a` |
| M/b | M | `c0daa5cd40e20c05db46ddc6913278b11584c760464f57ea45f49c37bbd6a828` |
| M/c | M | `d227057c1953cd7ae7e46b89c92e1d1007382c1af89e2730b7c2da70f2f965e4` |
| M/d1 | MR | `87dee013113d2101e69c1f3e9044bdb0cc8ce8bffb3a836feb42dc3092422903` |
| M/d2 | MC | `c4a0b1f00e65d2cd115c8df2d1031d191b4aff9fd3a839c1a7aba14453294520` |
| M/d3 | MR | `7b776f5db88f0efa4fd4f4983666419aee1856707746597f7c6e6db88959d467` |
## Authored artifacts; probe-only, not an implementation patch
Clone file `/tmp/revenger-r61-MutationKaika12Repro/r61-MutationKaika12Repro.py` SHA-256 `64cf968d2084df0f54545d391fe8da030a0c1811dfeb942cae8b8d1fd224f6a0`.
Patch `/tmp/revenger-r61-MutationKaika12Repro/r61-MutationKaika12Repro.patch` SHA-256 `55398f870c90f414e6fcf8a668fcf02a86a571e25d273ad38c8ddd1b3a4ffe08`; produced by `git -C /tmp/revenger-r61-MutationKaika12Repro diff e0a4b0c4348ef1fade46539f520e94fa140c4d8a` after staging only the new runner in the private clone.
Complete phase outputs, commands, exact replacements and hashes: `/tmp/revenger-r61-MutationKaika12Repro-results.json` SHA-256 `0d41f7f9def3a378a35505f3628b217272dee29a4696cfdb29c8ed784511d178`.
Rerun the recorded runner with a fresh seat-owned `--scratch` path (existing roots are refused). Runner and patch are the only authored clone files; evidence/cases are seat-owned scratch. No live-lane changes except this report; no REA calls, bytecode execution, services, builds, lint, formatters, or additional probes.
VERDICT: Independent pinned-archive reproduction KILLED 10/12, SURVIVED 2/12 (receipt-command b in both verifiers), INCONCLUSIVE 0/12; exact bytes restored in all 12 cases; historical prose ambiguities explicitly bounded.
Installs/updates: none.
