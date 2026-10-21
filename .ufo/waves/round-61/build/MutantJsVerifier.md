# Round 61 — MutantJsVerifier

Axes: calibration (guard-deletion sensitivity), coverage (C04 recheck scope), operability (bounded replay), byte preservation (no fixture/record edits).
Observed base: `git -C /tmp/revenger-r61-MutantJsVerifier-10 rev-parse HEAD` → `e0a4b0c4348ef1fade46539f520e94fa140c4d8a`.
Target `F=corpus/verify_js_graph_delta.py`; line numbers below refer to that base. Only authored synthetic fixtures and saved local records were read; no REA calls, target execution, network, builds, lint, or formatters.
Isolation: cloned the registered base, then `cp -a --reflink=auto /tmp/revenger-r61-MutantJsVerifier-10/corpus /tmp/revenger-r61-MutantJsVerifier-10-mNN` for NN=01…09; each detector ran with its own copied corpus as cwd.
Mutation rule: replace exactly one Python `require(condition, message)` condition with `True`, retaining its message and every other guard. Compound conditions were disabled as one call-site mutant, not separate conjunct mutants. All nine call sites were exercised independently.
Detector D(NN): `python3 -B /tmp/revenger-r61-MutantJsVerifier-10-mNN/verify_js_graph_delta.py --self-test`, with a 30-second subprocess deadline; identical command/cwd on pristine, mutated, restored bytes.
Expected detector: pristine/restored exit 0; weakened-guard mutant exit nonzero if the self-test detects that defect. A failing baseline or timeout is inconclusive, not killed.
All nine pristine and nine restored D runs: exit 0, empty stderr, exact stdout below; no timeout. Matrix total: 27 runs.
```text
POSITIVE saved parent graphs: removed checksum 1/1; stable rot13 and package-main; static inference only
NEGATIVE REJECTED saved graph disagrees with source truth
```

| Mutant | Disabled guard at F:line | Mutated exit | Actual last output line | Verdict |
|---|---|---:|---|---|
| M01 | 24: source import expression/`./transform` | 0 | `NEGATIVE REJECTED saved graph disagrees with source truth` | SURVIVED |
| M02 | 31: operation `analyze_javascript_application` | 0 | `NEGATIVE REJECTED saved graph disagrees with source truth` | SURVIVED |
| M03 | 33–34: coverage `complete` and omitted_count zero | 0 | `NEGATIVE REJECTED saved graph disagrees with source truth` | SURVIVED |
| M04 | 37–42: specifier, resolved_path, resolution_status, inferred evidence state, index.js source location | 0 | `NEGATIVE REJECTED saved graph disagrees with source truth` | SURVIVED |
| M05 | 44: duplicate named imports | 0 | `NEGATIVE REJECTED saved graph disagrees with source truth` | SURVIVED |
| M06 | 47–48: one package-main edge, inferred state, resolved status | 0 | `NEGATIVE REJECTED saved graph disagrees with source truth` | SURVIVED |
| M07 | 53–55: saved parent evidence IDs | 0 | `NEGATIVE REJECTED saved graph disagrees with source truth` | SURVIVED |
| M08 | 58: both graph tuples equal source-derived names/main | 1 | `AssertionError: altered v2 graph was accepted` (stderr) | KILLED |
| M09 | 59–62: removed checksum, stable rot13, package-main index.js delta | 0 | `NEGATIVE REJECTED saved graph disagrees with source truth` | SURVIVED |

All surviving mutants printed the same two stdout lines as pristine and empty stderr. M08 printed only the POSITIVE line on stdout; traceback terminates at F:79 with the AssertionError above (not an input/runtime failure).
Restoration: captured original call-site bytes were restored after the mutant runs. `sha256sum` over every pristine/restored copied verifier returned H=`77700f8eb63389f93d1414c965420fdcfab5f196a6fe872dc988490bd7e43aeb` (9/9 exact); restored D runs are recorded above.
| Mutant | SHA-256 while mutated (before=H; restored=H for every row) |
|---|---|
| M01 | `19618d85ce8a0688194769354f3607f82f7c11a4ec6a1d77e2d54b7a6b028469` |
| M02 | `92dd28c2c7710a5323e72dafd97815296283e44d0bc92f162debb44964749eaa` |
| M03 | `793ff5437a8ab01b43a513ae9ec635dd3a183534d465f65345ce8d9a2ce5e3aa` |
| M04 | `22cdb3b4c417d1762c17eddc69d1d0787bead70bca5f2dbd21610ed653cef4ff` |
| M05 | `ad98cdd358ad9e33d6b7f14af2b7ccd10229e680c0999e5ac336e243c847712c` |
| M06 | `8fe463d2864bd0fa324f2aa82abfb10728e4949abc821245b3265b076d5324d7` |
| M07 | `48f0abfedf11fa232422c7b2a4520cd3a858e7dd1d945f1a51e668228facd2b7` |
| M08 | `3a3613f817f3628a77ed811d2d1d95a2f9af39da5752c5b9cc39ac702cbc5b8f` |
| M09 | `3990f3bf124e544af712b916a9c4b68b6e082853e179542528fec927ac5da481` |

Input preservation command: `tar --sort=name --mtime=@0 --owner=0 --group=0 --numeric-owner -cf - -C /tmp/revenger-r61-MutantJsVerifier-10/corpus fixtures live | sha256sum` → `b4a787be9c7fb94cd8387e8bcbb7a20c47c3c92cb7f31103e994f9238f3ddc15` before; same digest after for the clone and each of nine scratch corpora. This proves fixity relative to copied bytes, not producer origin/authenticity.
C04 scope finding (F:69–79): the sole negative control rewrites right-graph `rot13` to `checksum`; it demonstrates the F:58 graph/source equality guard. Eight other guard removals survive this detector. A green recheck checks the saved positive records but must not be described as independent negative-control coverage of operation, completeness, static provenance, duplicates, package-main validity, IDs, or source-delta guards.
No production source/fixture/record changes or contract changes; only this assigned report was written in the lane. The private clone was not edited; mutation files existed only in the nine scratch copies and are restored. No production patch is proposed.
VERDICT: KILLED 1/9; SURVIVED 8/9; INCONCLUSIVE 0/9; pristine/restored controls 9/9 each and exact-byte restoration 9/9.
Installs: none; detector runtime was preinstalled Python 3.14.8.
