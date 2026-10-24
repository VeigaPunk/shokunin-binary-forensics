# R63SimplifierProbe — frozen counter vs frozen contract drift review

Seat: revenger-r63.R63SimplifierProbe · 2026-10-23 · Round 63 attempt 1 (hyaku)
Method: static side-by-side read of the frozen pair. Nothing executed (no-target-execution rule; also unnecessary — `measure-before.log` is the red-before artifact). No tool installed (none needed; pacman paused, unneeded). Tree mutated only by this granted report file.

Frozen inputs:
- Contract: `reports/round-63/claims.md` (frozen at lane commit 54ab973c021cc62ca65dcbe2cbfabe3235d5ee38; claim base 55bcb6e1aeb4d42923a4e98db6580f67142b41ac)
- Counter: `reports/round-63/measure.py` (183 lines, frozen at pre-registration)
- Receipt: `reports/round-63/measure-before.log`
- External anchors referenced by the probe's own comments: `SCORECARD.md` `:45-57` (command F), `:133` (K command), `:134` (freshness), `:199` (backed definition); round-61 probe `reports/round-61/measure.py` (113 lines, "same definitions" reference)

## Verdict

**MATCHES with one flagged drift (D1)** — every frozen predicate in claims.md is implemented in the probe exactly as the contract sentence states it, the do-nothing control values all reproduce in `measure-before.log`, and there is no dead code, no claimed-but-unprinted label. The one drift: `HOLDS_OK` is **not** the round-61 definition — it adds three conjuncts. Direction is strictly conservative (can only turn holds red, never green); base outcome is identical under both definitions, so the red-before receipt is unaffected. Listed below for L1 adjudication; both files are frozen, so this is a recorded observation, not a fix.

## Mapping table

| # | Contract sentence (claims.md) | Probe predicate (measure.py) | Status |
|---|---|---|---|
| 1 | Frozen counter command `python3 -B reports/round-63/measure.py TREE` on `git archive <commit> corpus` tree, cwd=/ (§Counting) | Docstring `:4-6`; `run()` `cwd="/"` `:63-67`; usage gate `:20-22` | MATCH |
| 2 | K: held coverage-map rows, denominator 14 (§Lowest axis, §Harms "14 rows") | rows `^\| C[0-9]+ ` + held `\| held \|$` on `corpus/README.md` `:24-28`; composed equivalent of SCORECARD `:133` `grep -cE '^\| C[0-9]+ .*\| held \|$'` | MATCH |
| 3 | `K_ROW C06` (§Counting label list; §C1 "README C06 flips partial → held") | loop over `("C06",)`, prints second-to-last pipe cell or `absent` `:29-31`; log shows `K_ROW C06 status=partial` | MATCH |
| 4 | `K_HELD_BACKED` (§Counting; do-nothing control "must print K_HELD_BACKED 6/14") | held rows whose field[3] names `knowledge/[\w.-]+\.md` AND every named file exists under TREE/corpus `:32-34` — identical expression to r61 `:38-40`; matches SCORECARD `:199` "regex as :133 plus entry-file existence"; denominator len(rows)=14 | MATCH |
| 5 | F families set — 8 frozen members; `firmware` = `inspect_firmware_regions`; F 4/8 → 5/8 iff firmware present (§C2) | `families` dict `:45-49`: exactly 8 keys — native-static{inspect_pe_resources}, managed{inspect_managed_artifact}, javascript{analyze_javascript_application}, android{inspect_android_package}, archives{inventory_artifact, inspect_artifact}, firmware{inspect_firmware_regions}, browser-runtime{inspect_web_page, capture_browser_scenario, observe_web_session}, evm{inspect_evm_interface} — byte-identical set to SCORECARD `:54`; presence `v.intersection(counter)` `:50` | MATCH |
| 6 | F record: carries `evidence_id` and `normalized_result` with `operation == "inspect_firmware_regions"` (§C2 a) | gate `isinstance(x,dict) and x.get("evidence_id") and x.get("normalized_result") is not None`, counted by `operation` (default "unknown") `:37-44` — identical to SCORECARD `:53`; scans `corpus/live/runs` rglob `*.json` (round-63/ subdir included); malformed JSON skipped | MATCH |
| 7 | `C2_*` labels "same definitions as the round-61 probe" (§Counting) | `SCRIPTS`/`CLAUSE`/`mutate_b`/`run()`/d2 forgery/MUTANT print/4 prints `:69-122` vs r61 `:51-96`: IDENTICAL predicates (d2 = `producer-receipt.json` `command += " --forged"`; b-attribution `last.endswith("forged receipt command accepted")` = r61 Amendment 2026-10-21). Only cosmetic diffs: tempdir prefix, comment placement | MATCH |
| 8 | C3 frozen mutation: named deletes `receipt['command']==command` (§C3 bullet 1) | `C3_SCRIPTS["verify_named_multi_icon_states.py"] = re.compile(r"receipt\['command'\]==command")` `:126` — literal, char-for-char the claims sentence (no whitespace tolerance) | MATCH |
| 9 | C3 frozen mutation: icon_states deletes `receipt['fixture_sha256'] == expected_hash` (§C3 bullet 2) | `C3_SCRIPTS["verify_icon_states.py"] = re.compile(r"receipt\['fixture_sha256'\]\s*==\s*expected_hash")` `:127` — matches the claims sentence spelling; whitespace-tolerant superset (see O2) | MATCH |
| 10 | "delete exactly one receipt-identity conjunct and its connecting `and`, then run `--self-test` on a fresh tree copy"; "the probe's mutant must match exactly one site in the final files" (§C3) | `mutate_c3` `:130-138`: requires exactly 1 findall hit, deletes `\s*and\s+CLAUSE` or `CLAUSE\s+and\s+`; miss → `could-not-evaluate` print + `evaluable=False` → exit 2 `:150-153`; mutants run in TemporaryDirectory copytree, never writing TREE `:143-154` | MATCH |
| 11 | Attribution rule: "exits non-zero and its last output line contains `forged receipt`; a crash or an unrelated assertion is not attributed" (§C3) | `c3_attributed += rc != 0 and "forged receipt" in last.lower()` `:161`; `last` = last line of stdout+stderr `:63-67` | MATCH (exact) |
| 12 | Red-before: "both mutants exit 0" at base; C3 0/2 (§C3) | log: both c3 mutants `exit=0 pass`, `C3_CONTROLS_PASS=2/2`, `C3_RECEIPT_KILLED_ATTRIBUTED=0/2` — mutation applied (no could-not-evaluate), so both frozen clauses match exactly once in the base verifiers | MATCH |
| 13 | `C3_CONTROLS_PASS`, `C3_RECEIPT_KILLED_ATTRIBUTED` printed (§Counting) | `:162-163`, both `/2` | MATCH |
| 14 | Existing `HOLD_*`/`HOLDS_OK` (§Counting); HOLD_CALIBRATION ≥4/4, HOLD_REPLAY ≥10/10 (§Harms); "ten-verifier census count stays 10" (§C3) | census glob `verify_*.py`, HOLD detail lines, `names` = the same 4 calibration verifiers, `HOLD_CALIBRATION={ok}/{len(names)}`, `HOLD_REPLAY={replay}/{len(results)}` `:165-176` — code identical to r61 `:97-110`; denominators dynamic (probe measures; the 10-count is adjudicated from the printed value; base log 10/10) | MATCH |
| 15 | Probe exit non-zero at final is void (§Harms) | `sys.exit(2 if not evaluable else 0 if holds_ok else 1)` `:181`; docstring `:7-9` documents 0/1/2 exactly as implemented | MATCH |
| 16 | Do-nothing control: base must print K_HELD_BACKED 6/14, F_COVERAGE 4/8, C3_RECEIPT_KILLED_ATTRIBUTED 0/2 (§Counting) | log reproduces all three plus K_HELD 6/14 score=4.3, K_ROW C06 partial, FRESH_ROWS 18/18, C2 block 2/2 ×4, HOLDS_OK=yes, PROBE_EXIT=0 | MATCH |
| 17 | Freshness label `FRESH_ROWS`; SCORECARD `:134` definition | regex `^\| [FK][0-9]+ .*\| (holds\|STALE)` over seed.md + 2026-10-12-rea-readiness-checklist.md `:55-60` — identical to SCORECARD `:134`; new in r63 (r61 probe has no freshness block), claims.md lists it outside the "same definitions" parenthetical | MATCH |
| 18 | "The probe never writes inside TREE" (probe docstring; consistent with §Harms corpus preservation) | all mutation/forge writes under TemporaryDirectory work copies `:88-103`, `:143-154`; zero writes to TREE paths | MATCH |

**D1 (drift): `HOLDS_OK` definition is not the round-61 definition.** r61 `:111`: `holds_ok = controls == 2 and killed_d2 == 2 and ok == len(names) and replay == len(results)`. r63 `:177-179` adds three conjuncts: `killed_b == 2`, `c3_controls == 2`, `fresh == 18`. claims.md §Counting says "existing `C2_*`/`HOLD_*`/`HOLDS_OK` (same definitions as the round-61 probe)" — strictly false for HOLDS_OK. Impact: strictly strengthening; at base every added conjunct is true, so HOLDS_OK=yes and exit 0 are identical under either definition (red-before unaffected); at final the additions can only newly fail holds, i.e. they align with the §Harms void "probe exit non-zero at final" but were never declared as hold extensions. None of the three additions can green-light a claim that the r61 definition would have failed. The C2_* and HOLD_* labels themselves ARE identical to r61.

## Observations (not drift)

- **O1 — unlabeled printed line:** `print(dict(sorted(counter.items())))` `:51` emits the per-operation census dict with no label; not named in claims.md's label list. It is the probe's analog of SCORECARD command F's own census print (`:56`), diagnostic only, feeds no hold.
- **O2 — C3 regex whitespace asymmetry:** the named-script clause regex is literal (`==command`, zero tolerance) while the icon_states clause regex is whitespace-tolerant (`\s*==\s*`). Both honor their frozen claims sentences exactly; both matched exactly once at base (red-before mutants applied, no could-not-evaluate). Asymmetry only; no semantic drift.
- **O3 — output lines not enumerated in claims.md:** `MUTANT …` detail lines and bare `HOLD <verifier> …` detail lines are existing round-61 output formats (byte-identical in r61), subsumed by "the round-61 probe … untouched" + "existing" wording; the usage-error path exits 1 with a stderr message (docstring documents exit 1 only as "a hold failed") — cosmetic.
- **O4 — FRESH_ROWS denominator is a literal `/18`** (count is dynamic); matches the SCORECARD `:134` two-file definition whose row count is 18 at base.
- **O5 — attribution rules differ per block by design:** C2 b uses the stricter r61 `endswith("forged receipt command accepted")`; C3 uses the claims-specified case-insensitive `contains "forged receipt"`. Both exactly as their respective frozen sentences state.

## Dead code / labels audit

- No dead code: all 8 imports used; `evaluable` is live (set True `:61`, set False at both could-not-evaluate sites `:96`, `:152`, read in exit `:181`); no unreachable branch. `for row_id in ("C06",)` is a 1-tuple loop (r61 used a 2-tuple) — stylistic only.
- Labels claimed in claims.md but not printed: none (all 15 enumerated labels/label-families print).
- Printed labels not in claims.md: only the unlabeled census dict (O1) and the two existing r61 detail-line formats (O3).

## Preservation

Read-only review except this file. No bash side effects, no fixture/`corpus/live` contact, no spec/registry/MANIFEST/sibling/lane-state writes. Scratch: none created (no /tmp/revenger-r63-* left behind). Sibling reports already in `build/` untouched.

## Tradeoff

None taken — deletions: none (nothing to delete; probe has no dead weight). The only judgment call: D1 reported as drift-under-strict-reading with its benign direction quantified, rather than silently accepted, because the freeze means the contract sentence and the counter cannot be reconciled post hoc — that call belongs to L1.
