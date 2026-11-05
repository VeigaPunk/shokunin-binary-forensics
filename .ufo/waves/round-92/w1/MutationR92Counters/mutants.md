# Round-92 counter mutation report — seat MutationR92Counters (revenger r92, attempt 1)

Mutation test of the two frozen counters at lane commit `9402183a`
(`reports/round-92/c1_k_admit_counter.py`, `reports/round-92/c2_legend_counter.py`).
All mutants were built from copies in seat scratch; the frozen files, `claims.md` and
`controls/*` were never modified.

## 1. Harness validation (pristine baseline)

Control trees were rebuilt in scratch from the freeze commit — `git archive 9402183a corpus
reports/round-66 reports/round-92`, extracted into a scratch `mirror/` tree; the counter copies
were placed at `mirror/reports/round-92/` so `LANE` (=`__file__`.parents[2]) resolves inside
scratch, pointing lint's `--lane`, the round-66 probe path and the archive root at frozen
scratch copies instead of the live lane. `run_controls.py`'s edit functions (`sub_row`,
`c08_held`, `c08_uncovered`, `c08_deleted`, `c03_held_stub`) were replicated byte-for-byte by
`build_trees.py`; no control receipts were rewritten.

Pristine copies are hash-identical to the frozen files
(`c1 fe766d90011e42f60ad6ade89fa66ec9c2ae0cbbe7b14c6770dacdaf471860f5`,
`c2 47fa19d872909960a682631d43e56560275ab304a03cff50eee9329d41d62943`), and their runs over
the rebuilt trees reproduce **all six frozen control logs byte-for-byte** (`diff` empty):
`c1-do-nothing`, `c1-junk-stub`, `c2-do-nothing`, `c2-positive`, `c2-junk-held`,
`c2-junk-deleted` — exits match (fail×5 = exit 1, `c2-positive` = exit 0).

**Kill rule (verdict level, per seat spec):** a mutant is KILLED iff a must-fail control's
`C*_VERDICT` flips `fail→pass`, or the must-pass `c2-positive` flips `pass→fail`. Leg-level
output changes are recorded as secondary "leg-detected" evidence. The C1 positive does not
exist pre-READY (claims.md), so C1 mutants ran over the do-nothing and junk-stub trees only.

Controls used: `base-do-nothing` (must fail), `c1-junk-stub` (must fail), `c2-positive` (must
pass), `c2-junk-held` (must fail), `c2-junk-deleted` (must fail).

## 2. C1 mutants — 21 built, 1 KILLED, 20 SURVIVED

| id | exact one-line diff (old → new) | base-do-nothing | c1-junk-stub | verdict |
|----|--------------------------------|-----------------|--------------|---------|
| m01_rows_total_true | `legs["C1_ROWS_TOTAL"] = len(cov) == 15` → `= True` | output byte-identical | output byte-identical | **SURVIVED** (undetected; no C1 control deletes/adds rows) |
| m02_rows_total_14 | `== 15` → `== 14` | leg pass→fail | leg pass→fail | **SURVIVED** (leg-detected; killed only by a post-READY 15-row positive) |
| m03_c03_held_true | `legs["C1_C03_HELD"] = bool(c03) and c03[4] == "held"` → `= True` | leg fail→pass, verdict fail | unchanged | **SURVIVED** (leg-detected; C03_HELD=false co-fails the K leg on every reachable tree) |
| m04_c03_cites_true | `legs["C1_C03_CITES"] = bool(c03) and …` → `= True` | leg fail→pass, verdict fail | unchanged | **SURVIVED** (leg-detected) |
| m05_admitted_true | `legs["C1_ADMITTED"] = bool(re.search(…))` → `= True` | leg fail→pass, verdict fail | unchanged | **SURVIVED** (leg-detected) |
| m06_trio_true | `legs["C1_TRIO"] = all(any(…))` → `= True` | leg fail→pass, verdict fail | unchanged | **SURVIVED** (leg-detected) |
| m07_votes_true | `legs["C1_VOTES"] = len(votes_ok) >= 2` → `= True` | leg fail→pass, verdict fail | leg fail→pass, verdict still fail (LINT/EMBEDDED/SOURCES) | **SURVIVED** (leg-detected) |
| m08_votes_sha_drop | `and v.get("candidate_sha256") == want` → `and True` | byte-identical | byte-identical | **SURVIVED** (undetected — votes dir absent at freeze, sub-check never executes) |
| m09_votes_role_drop | `and v.get("role") in ("reviewer", "critic")` → `and True` | byte-identical | byte-identical | **SURVIVED** (undetected) |
| m10_votes_distinct_drop | `v["seat"] not in seen` → `True` | byte-identical | byte-identical | **SURVIVED** (undetected) |
| m11_votes_qset_drop | `and set(ds) >= set(QS)` → `and True` | byte-identical | byte-identical | **SURVIVED** (undetected; on any votes-bearing tree with partial decisions it **crashes**: `KeyError: 'Q02'`, exit 1, no verdict line — the intact Q-verdict guard then iterates missing keys; pristine's Q-set guard short-circuits first) |
| m11b_votes_qset_tauto (variant) | `and set(ds) >= set(QS)` → `and set(ds) >= {q for q in QS if q in ds}` | byte-identical to pristine | byte-identical to pristine | **SURVIVED** (undetected; same KeyError crash on partial votes) |
| m11c_qset_qverdict_codrop (variant) | both guard lines → `and True` / `and True)` | byte-identical | byte-identical | **SURVIVED** (undetected on frozen controls; demo votes control flips `C1_VOTES` fail→pass cleanly — §4) |
| m12_votes_qverdict_drop | `and all(ds[q] in ("PASS", "n/a") for q in QS))` → `and True)` | byte-identical | byte-identical | **SURVIVED** (undetected) |
| m13_lint_true | `legs["C1_LINT"] = lint.returncode == 0` → `= True` | unchanged | leg fail→pass, verdict still fail | **SURVIVED** (leg-detected) |
| m14_embedded_true | `legs["C1_EMBEDDED"] = emb.returncode == 0` → `= True` | unchanged | leg fail→pass, verdict still fail | **SURVIVED** (leg-detected) |
| m15_sources_date_drop | `if not r or r[7] != "mined" or r[8] != ROUND_DATE or ENTRY not in r[10]:` → `if not r or r[7] != "mined" or ENTRY not in r[10]:` | byte-identical | byte-identical | **SURVIVED** (undetected — the stub's S999 is unregistered, so the row-existence conjunct masks the opened-date conjunct) |
| m16_sources_true | `legs["C1_SOURCES"] = src_ok` → `= True` | leg fail→pass, verdict fail | leg fail→pass, verdict fail | **SURVIVED** (leg-detected) |
| m17_k_target_8 | `legs["C1_K_HELD_BACKED"] = held_backed == 9` → `== 8` | K leg fail→pass, verdict fail | K leg pass→fail, verdict fail | **SURVIVED** (leg-detected both ways; no pre-READY tree fails only-K) |
| m18_ok_gate_true | `ok = all(legs.values())` → `ok = True` | verdict fail→**pass** | verdict fail→**pass** | **KILLED** (decided by base-do-nothing; also c1-junk-stub) |
| m19_digest_norm_drop | `norm = re.sub(r"^admission-status: (…)$", "admission-status: candidate", text, flags=re.M)` → `norm = text` | unchanged | `C1_VOTE_SEATS … digest=` line changes (un-normalised digest), verdict fail | **SURVIVED** (leg-detected) |

C1 pattern: the do-nothing tree fails 10 legs and the junk-stub tree fails 4 at once
(VOTES, LINT, EMBEDDED, SOURCES), so no single-leg drop can flip a verdict — only the
conjunction-gate mutant (m18) is killed. Every admission leg is defended by the frozen kill
rule ("any leg fails ⇒ not verified") but is *isolated* by no pre-freeze control.

## 3. C2 mutants — 7 built, 4 KILLED, 3 SURVIVED

| id | exact one-line diff | base-do-nothing | c2-positive | c2-junk-held | c2-junk-deleted | verdict |
|----|--------------------|-----------------|-------------|--------------|-----------------|---------|
| n01_rows_total_true | `"C2_ROWS_TOTAL": n_rows == 15,` → `: True,` | fail | pass | fail | **pass** (flipped) | **KILLED** (decided by c2-junk-deleted) |
| n02_rows_total_14 | `n_rows == 15` → `n_rows == 14` | fail | **fail** (flipped) | fail | **pass** (flipped) | **KILLED** (decided by c2-positive AND c2-junk-deleted — double kill) |
| n03_c08_clear_true | `"C2_C08_CLEAR": "C08" not in rows,` → `: True,` | leg fail→pass, verdict fail | pass | fail | fail | **SURVIVED** — provably verdict-equivalent: C08 flagged ⟹ C08∉{C03} ⟹ `C2_NO_NEW` also fails, so no tree can flip the verdict through this leg alone. `C2_C08_CLEAR` is redundant with `C2_NO_NEW` at verdict level (informational leg only). |
| n04_no_new_true | `"C2_NO_NEW": set(rows) <= {"C03"},` → `: True,` | leg fail→pass, verdict fail (masked by C08_CLEAR) | pass | fail | fail | **SURVIVED** (leg-detected; verdict-level kill demo exists — §4 demo C) |
| n05_no_unbacked_true | `"C2_NO_UNBACKED": held_tok == held_backed,` → `: True,` | fail | pass | **pass** (flipped) | fail | **KILLED** (decided by c2-junk-held) |
| n06_ok_gate_true | `ok = all(legs.values())` → `ok = True` | **pass** | pass | **pass** | **pass** | **KILLED** (decided by base-do-nothing; also c2-junk-held, c2-junk-deleted) |
| n07_labels_missing_exit0 | `return 1` → `return 0` in the `reason=probe-labels-missing` branch | byte-identical | byte-identical | byte-identical | byte-identical | **SURVIVED** (undetected — no control breaks the probe; violates the documented exit contract `exit 0 iff pass` on the probe-crash path; demo in §4 demo D) |

## 4. Routed suggestions — smallest controls that would kill the survivors

Built and demo-verified in scratch only; **not** added to the frozen controls.

- **Demo A (kills m15's blindness):** junk stub citing a *registered* source — planted
  SOURCES row `S901` (status `mined`, opened `2026-10-01`, used-by naming the entry) + stub
  header `source: S901`. Output: pristine `C1_SOURCES=fail` vs m15 `C1_SOURCES=pass`
  (verdicts both fail — leg-level isolation of the opened-date conjunct).
- **Demo B (kills m08–m12):** junk stub + `reports/round-92/votes/*.json` with one defect
  each, everything else unchanged. Outputs (pristine vs mutant `C1_VOTES`):
  wrong `candidate_sha256`: fail→pass (m08); `role: executor`: fail→pass (m09); same seat
  twice: fail→pass (m10); decisions missing Q02+: pristine `fail`, m11/m11b **crash**
  (`KeyError 'Q02'`, exit 1, no verdict line — detection by crash), m11c `pass`;
  a `FAIL` decision: fail→pass (m12). Sanity: a fully valid pair scores `C1_VOTES=pass` on
  pristine. Adoption note: if these controls land, m11-style one-line Q-set drops should be
  expected to fail loudly (crash), which still denies `C1_VERDICT=pass`.
- **Demo C (kills n04 at verdict level):** `c2-positive` tree + C07 `held→frontier` + planted
  saved record `{"operation": "inspect_firmware_regions", …}` under `corpus/live/runs/` —
  the probe flags C07 (frontier, record-op intersection per `ROW_OPS`), so `C2_NO_NEW` is the
  only failing leg: pristine `C2_VERDICT=fail` vs n04 `C2_VERDICT=pass`.
- **Demo D (kills n07):** probe-crash tree (`corpus/README.md` as a directory) — pristine
  exits 1 (`reason=probe-labels-missing`), n07 exits 0. A control asserting "probe emits no
  labels ⇒ counter exits nonzero" kills it.
- **Post-READY positives** (the wave's own run) automatically kill m02 and m17 (a 15-row,
  9-backed positive fails under `==14` / `==8`); positive-derived variants each isolate one
  more leg: a 14-row positive kills m01; positive minus the `admission-status: admitted`
  line kills m05 (votes still match — the digest normalises that line); positive minus the
  `source:/verified-at:/recheck:` lines kills m06; positive with the C03 token mangled kills
  m03 (and K); a lint-passing stub with drifting embedded outputs kills m14; a stub failing
  only lint kills m13; a stub failing only SOURCES kills m16.
- **Redundancy (n03):** `C2_C08_CLEAR` cannot be verdict-killed by any control — it is
  logically implied by `C2_NO_NEW`. Keep as informational or drop; there is no missing
  control to add.

## 5. Counts

| counter | mutants | killed | survived | undetected on frozen controls |
|---------|---------|--------|----------|-------------------------------|
| C1 (`c1_k_admit_counter.py`) | 21 (19 one-per-leg + 2 Q-set-leg variants) | 1 (m18) | 20 | 9 (m01, m08, m09, m10, m11, m11b, m11c, m12, m15) |
| C2 (`c2_legend_counter.py`) | 7 | 4 (n01, n02, n05, n06) | 3 (n03 verdict-equivalent, n04, n07) | 1 (n07) |
| **total** | **28** | **5** | **23** | 10 |

## 6. Integrity / restoration evidence

- Frozen files untouched: lane `reports/round-92/c1_k_admit_counter.py` and
  `c2_legend_counter.py` sha256 identical before and after every run
  (`fe766d9…0f5`, `47fa19d…943`); `claims.md` and `controls/*` never written.
- Mutant copies lived only in seat scratch with sha256 recorded pre/post per run
  (`results.json`, unchanged throughout).
- All trees, demos and outputs lived under
  `/fast/scratch/hyaku/revenger-r92/MutationR92Counters/` (deleted after the run);
  the only lane writes by this seat are this wave dir and the seat report file.
- Observation (not this seat's): the lane working tree showed `M SKILL.md` before this seat
  started and `M .gitignore` appeared during the run; this seat made no lane writes outside
  its wave dir.
- Tooling: none installed (uv/npx/binary channels unused); stock `python3` + `git` read-only
  (`archive`, `rev-parse`, `ls-tree`, `status`, `log`).
