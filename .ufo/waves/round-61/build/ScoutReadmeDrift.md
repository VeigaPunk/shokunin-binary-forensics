# ScoutReadmeDrift — corpus/README.md vs repo (r61, READ-ONLY)

Base observed: `git rev-parse HEAD` → `e0a4b0c4348ef1fade46539f520e94fa140c4d8a`. No clone used; only this report written.

## Drift (path:line + exact replacement)

D1 `corpus/README.md:9` says `Q01–Q10`; `corpus/QUALITY.md:23` defines `| Q11 | Supersedes Q08. ...`. `SCORECARD.md:181` already writes "`QUALITY.md` Q01–Q11". Replace with:
```
- `QUALITY.md` — admission criteria Q01–Q11, each citing its mistake class.
```

D2 `corpus/README.md:12` lessons index omits `corpus/lessons/round-1-verifier-spotcheck.md` (exists, 1878 B). `git log --oneline -1 -- corpus/lessons/round-1-verifier-spotcheck.md` → `cf02419 2026-10-19 round-1 verifier spot-check`; `git merge-base --is-ancestor cf02419 35b2e8b` → NOT ancestor, and README last changed at `35b2e8b`, so the index was never updated after the file landed. Replace with:
```
- `lessons/` — `2026-10-12-r1-provider-gap.md`; `round-1.md` (fleet round-1 gates and the mined `## Mistakes` table); `round-1-verifier-spotcheck.md` (non-author admit/reject sample and adjudication).
```

D3 `corpus/README.md:15` presents every `verify_*.py` as a `--self-test` verifier. `grep -c -- '--self-test'` → 0 for `verify_icon_languages.py`, `verify_icon_states.py`, `verify_multi_icon_states.py`, `verify_named_multi_icon_states.py`; those four never read `sys.argv` and end `if __name__=='__main__': main()` (`:165`, `:168`, `:165`, `:99`). The six that branch on the flag: `verify_evm_evidence.py:66`, `verify_js_graph_delta.py:69`, `verify_pe_resources.py:60`, `verify_saved_evidence.py:130`, `verify_semantic_trace.py:89`, `verify_shape_evidence.py:112`. `SCORECARD.md:37` passes `--self-test` to all ten, so for the four the flag is inert. Replace with:
```
- `verify_*.py` — saved-ledger replay verifiers: six branch on `--self-test` (evm, js-graph-delta, pe-resources, saved-evidence, semantic-trace, shape-evidence); four (`verify_icon_languages.py`, `verify_icon_states.py`, `verify_multi_icon_states.py`, `verify_named_multi_icon_states.py`) take no arguments and ignore it. Census command in `SCORECARD.md` (C).
```

D4 `corpus/README.md:40` (C14) says "re-verified 2026-10-19"; the entry's own header says `2026-10-12-rea-readiness-checklist.md:2` "3 of 6 rows stale", and `:37`, `:38`, `:40` mark K02, K03, K05 STALE. Replace with:
```
| C14 | host readiness for REA routes | `knowledge/2026-10-12-rea-readiness-checklist.md` (re-probed 2026-10-19: 3/6 rows stale — K02, K03, K05 — pre-contract, not re-gated) | `.ufo/waves/kaika-r1/scout-freshness.md` | partial |
```

D5 `corpus/README.md:11` calls all six `knowledge/` files "admitted domain entries". `grep -cE '^\| Q[0-9]{2} '` → 10 admission rows each for the four gated entries, 0 for `seed.md` and `2026-10-12-rea-readiness-checklist.md`; `README.md:49-52` itself calls those two pre-contract and not re-gated. Replace with:
```
- `knowledge/` — domain entries (the map below names each one); `seed.md` and `2026-10-12-rea-readiness-checklist.md` remain pre-contract (Known gaps).
```

D6 `corpus/README.md:14` says "per historical round"; `git ls-files corpus/live/runs` shows no `round-2`/`round-3`, three `20261012T*` capture dirs, and four review files at the root (`review-r1-r3.md`, `promotion-review-r5.md`, `round-4-verification.md`, `round-5-review.md`). Replace with:
```
- `live/runs/` — saved REA outputs and receipts; `round-*/` per round where records exist (none for rounds 2–3), three `20261012T*` captures, and non-author reviews at the directory root.
```

D7 `corpus/README.md:13` fixtures line names only `fixtures/REPLAY.md`; `grep -n 'checksum-r1\|replay_fixtures' corpus/README.md` → no hits, though `fixtures/checksum-r1/` is the round-1 native fixture (`fixtures/replay_fixtures.py:10`; `live/runs/20261012T163909Z/LEDGER.md:5`) and `fixtures/replay_fixtures.py` is the replay driver. Replace with:
```
- `fixtures/` — authored known-truth inputs (byte-oracle fixtures; `fixtures/REPLAY.md`, replay driver `fixtures/replay_fixtures.py`, native source fixture `fixtures/checksum-r1`).
```

## Checked, consistent (no edit)

- Row count: `grep -cE '^\| C[0-9]+ ' corpus/README.md` → 14; `a7acc20` exists and `git diff a7acc20 -- corpus/README.md` shows only the admissions plus the `SOURCES.md` line, matching `README.md:42-43`.
- Every knowledge file is named by the map; coverage headers: `pe-resource-directory-layout.md:6` C01, `seed.md:4` C02/C10/C12/C14, `utf16-...:7` C11, `tool-validation-...:6` C12, `digest-scope-...:7` C13, checklist `:4` C14/C02.
- Every verifier is reached: line 15 glob plus C01 (`verify_*icon*.py`, `verify_pe_resources.py`), C04 (three), C09, C10. No unindexed verifier.
- Frontier rows C03/C05/C07/C08 hold: `grep -rl '"operation": "<op>"' corpus/live/runs` → 0 files for `inspect_managed_artifact`, `inspect_android_package`, `inspect_firmware_regions`, `inspect_web_page`, `capture_browser_scenario`, `observe_web_session`. C04/C09 `uncovered` consistent (`analyze_javascript_application` files=2; no `inspect_evm_interface` record).
- Row dependencies resolve: `seed.md:21` §Verification discipline, `seed.md:30` §Calibration strategy, checklist `:18` archive-tool row, `reports/round-1/` present, `.ufo/waves/kaika-r1/scout-freshness.md` present and tracked; `tool-validation-...:58` cites `corpus/README.md:37`, which is the C12 row at `a7acc20` (verified).
- Known-gaps claims: `SKILL.md`/`AGENTS.md` absent (`ls` errors) and named at `SCORECARD.md:109,124`; no gate-registry file; `8bbcb4e` heads of seed/checklist carry no `source:` header (verified).
- C12 "authored fixtures carrying `truth.json`": `find corpus/fixtures -name truth.json | wc -l` → 40 over 44 fixture dirs; the four without are `checksum-r1`, `js-r3`, `js-r7-v2`, `shapes-r12` — true as written.

VERDICT: 7 index drifts at `README.md:9,11,12,13,14,15,40`; row statuses otherwise match entries and saved records; no unindexed knowledge entry or verifier. Installs: none.
