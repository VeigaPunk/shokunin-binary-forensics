# MutationR93 — one dropped-leg mutant per leg, both round-93 v2 counters

Lane commit under test: `02050cb2a6758e3bd9cec696ff0e42df6f23511a` (freeze).
Instruments: `reports/round-93/c1_k_admit_counter2.py` (13 legs + verdict gate),
`reports/round-93/c2_legend_counter2.py` (6 legs + verdict gate). Frozen bytes
were never modified: originals ran from their lane paths, mutants from
scratch copies at `$HYAKU_SCRATCH/revenger-r93/MutationR93/reports/round-93/`
(same directory depth, so `parents[2]` keeps resolving; that scratch root is a
throwaway `git init` repo whose `.git/objects/info/alternates` borrows the
lane's objects read-only, which is what the C2 probe-archive and
`base_statuses` calls need). Scratch removed after the runs; harness, raw logs
and `results.json` are committed beside this file (`harness.py`, `logs/`,
`results.json`).

Result: **21 mutants — 20 KILLED, 1 EQUIVALENT (`C2_NO_NEW`), 0 SURVIVED.**
Every kill below is single-leg isolated: the pristine counter's only failing
leg on the deciding tree is the mutated leg (plus the `*_VERDICT` echo), and
each mutant still passes the honest positive fixture (`mut_on_pos=pass`), so
no kill rides on a broken counter.

## 1. Method

- Deciding trees were built in scratch from `git archive
  281a5bad66e844190a570cb35d257c6974749993` (freeze base) `corpus`, plus
  hand-built `reports/round-93/{votes,opens.json,quote-receipts}` and
  `.ufo/waves/round-93/w1/{swarm-registry.json,SeatA,SeatB}` fixture bytes.
  Tree-building patterns mirror the counters' own self-tests and
  `forge_battery.py`'s `forge_c1_tree`/`edit_c08` (copied, not imported).
- Honest positive fixtures first: both frozen counters print
  `C1_VERDICT=pass` / `C2_VERDICT=pass` on them (`logs/sanity-*-positive-original.log`),
  and both print `fail` on the bare base tree (`logs/sanity-*-donothing-original.log`),
  matching `controls/*-do-nothing.log`.
- Each mutant = exactly one line replaced (pattern asserted unique before
  patching): the leg assignment `legs["…"] = <expr>` → `legs["…"] = True`
  (leg dropped), or the gate `ok = all(legs.values())` → `ok = True`.
- Deciding tree per leg: pristine counter must fail **only** on the mutated
  leg; mutant must pass. Gate mutants: do-nothing tree must flip fail → pass.

## 2. C1 (`c1_k_admit_counter2.py`) — 13 legs + gate

| mutant (diff line, `old` → `new`) | deciding tree | pristine verdict / failing legs | mutant verdict | class |
|---|---|---|---|---|
| `legs["C1_ROWS_TOTAL"] = len(cov) == 15` → `True` | c1-rows: held row C02 edited to 4 cells → `cov`=14; K_HELD_BACKED unchanged (C02 not held) | fail / `C1_ROWS_TOTAL` | pass | **KILLED** |
| `legs["C1_C08_HELD"] = bool(c08) and c08[4] == "held"` → `True` | c1-c08held: C08 left `uncovered` but still citing the entry; C15 `uncovered`→`held` (its cited `round-72-tool-landscape.md` exists) keeps K_HELD_BACKED=10 | fail / `C1_C08_HELD` | pass | **KILLED** |
| `legs["C1_C08_CITES"] = … ENTRY_REL in c08[2] …` → `True` | c1-c08cites: C08 cite cell → `knowledge/seed.md` (entry file still exists, so digest/votes stay valid) | fail / `C1_C08_CITES` | pass | **KILLED** |
| `legs["C1_ADMITTED"] = bool(re.search(…admitted…))` → `True` | c1-admitted: entry `admission-status: candidate`; votes still match because `digest()` normalises the status line | fail / `C1_ADMITTED` | pass | **KILLED** |
| `legs["C1_TRIO"] = all(any(l.startswith(k)…))` → `True` | c1-trio: `recheck:` line removed from the entry header (votes rewritten to the new bytes) | fail / `C1_TRIO` | pass | **KILLED** |
| `legs["C1_VOTES"] = len(votes_ok) >= 2` → `True` | c1-votes: `SeatB.json` deleted (1 distinct seat) | fail / `C1_VOTES` | pass | **KILLED** |
| `legs["C1_LINT"] = lint.returncode == 0` → `True` | c1-lint: **real** `corpus/lint_entry.py` restored; entry drops its `coverage-map:` line → lint HEADER finding, exit 1 (embedded checker stubbed to isolate) | fail / `C1_LINT` | pass | **KILLED** |
| `legs["C1_EMBEDDED"] = emb.returncode == 0` → `True` | c1-embedded: **real** `corpus/check_embedded_outputs.py` restored; entry embeds the true oracle command with a drifted output line `ORACLE OK (16/17 checks)` → drift, exit 1 | fail / `C1_EMBEDDED` | pass | **KILLED** |
| `legs["C1_EMBED_NONVACUOUS"] = not vacuous` → `True` | c1-nonvac: entry embeds a `$ python3 -B corpus/fixtures/browser-r77/oracle_check.py …` fence with zero output lines (embedded checker stubbed so only the counter-level vacuous check decides) | fail / `C1_EMBED_NONVACUOUS` | pass | **KILLED** |
| `legs["C1_SOURCES"] = src_ok` → `True` | c1-sources: S495 row `opened` cell `2026-11-05` → `2026-11-04` | fail / `C1_SOURCES` | pass | **KILLED** |
| `legs["C1_QUOTES"] = q_ok` → `True` | c1-quotes: entry header adds `source: S500 — https://…` + matching external S500 SOURCES row, no receipt → `audit_source_quotes.py verify` exit 1 | fail / `C1_QUOTES` | pass | **KILLED** |
| `legs["C1_OPENS"] = o_ok` → `True` | c1-opens: `opens.json` `oracle_tail` → `ORACLE OK (16/17 checks)` | fail / `C1_OPENS` | pass | **KILLED** |
| `legs["C1_K_HELD_BACKED"] = held_backed == 10` → `True` | c1-khb: `knowledge/utf16-unpaired-surrogates-in-resource-names.md` deleted (backing of held row C11) → held_backed=9 | fail / `C1_K_HELD_BACKED` | pass | **KILLED** |
| `ok = all(legs.values())` → `ok = True` (gate) | bare base tree (do-nothing) | fail / 11 legs (`ADMITTED, C08_CITES, C08_HELD, EMBEDDED, EMBED_NONVACUOUS, K_HELD_BACKED, LINT, OPENS, SOURCES, TRIO, VOTES`) | pass | **KILLED** |

Raw logs: `logs/c1-*-original.log`, `logs/c1-*-mutant.log`,
`logs/c1-*-mutant-positive.log`.

## 3. C2 (`c2_legend_counter2.py`) — 6 legs + gate

| mutant (diff line) | deciding tree | pristine verdict / failing legs | mutant verdict | class |
|---|---|---|---|---|
| `legs["C2_ROWS_TOTAL"] = len(five) == 15 and len(rows) == 15` → `True` | c2-rowskill: positive tree + appended 5-cell row `C16` (held, cites `knowledge/c16-stub.md`, created) → `rows`=16; probe stays quiet (held 11/11, mismatch 0, `ONLY_C08` walks base ids only) | fail / `C2_ROWS_TOTAL` | pass | **KILLED** |
| `legs["C2_C08_TOKEN"] = bool(c08) and c08[4] == "held" and entry_ok` → `True` | c2-seedtok: C08 `held` citing `knowledge/seed.md`, seed.md present, entry file absent. Refinement over battery F6 (which leaves seed.md absent, so `NO_UNBACKED` co-fires): with the file present the token leg is the **only** failure | fail / `C2_C08_TOKEN` | pass | **KILLED** |
| `legs["C2_C08_RECORD"] = rec.is_file() and sha256 == RECORD_SHA` → `True` | c2-recmut: record bytes appended `x` (the self-test's record-sha kill, now proving the leg is verdict-load-bearing) | fail / `C2_C08_RECORD` | pass | **KILLED** |
| `legs["C2_NO_NEW"] = labels["rows"] == []` → `True` | no deciding tree exists — see §4 | fail (on frontier trees) | fail | **EQUIVALENT** |
| `legs["C2_NO_UNBACKED"] = labels["held"] == labels["backed"]` → `True` | c2-unbacked: positive tree with held row C11's cited file deleted → probe held=10, backed=9; probe mismatch stays 0 (row not frontier) | fail / `C2_NO_UNBACKED` | pass | **KILLED** |
| `legs["C2_ONLY_C08"] = moved <= {"C08"}` → `True` | c2-c15held: positive tree + C15 `uncovered`→`held` (cited file exists) → probe quiet (held 11/11, mismatch 0) but `moved`={C08,C15} | fail / `C2_ONLY_C08` | pass | **KILLED** |
| `ok = all(legs.values())` → `ok = True` (gate) | bare base tree (do-nothing) | fail / `C2_C08_TOKEN` | pass | **KILLED** |

Raw logs: `logs/c2-*-original.log`, `logs/c2-*-mutant.log`,
`logs/c2-*-mutant-positive.log`.

## 4. `C2_NO_NEW` is verdict-equivalent (informational leg)

**Claim.** For every tree T: if the NO_NEW-dropped mutant prints
`C2_VERDICT=pass`, the pristine counter also prints `C2_VERDICT=pass`. No
single tree can flip the verdict through this leg alone (r92 n03 precedent
class: leg implied by its siblings at verdict level).

**Proof.** Mutant passes ⟹ `ROWS_TOTAL ∧ C08_TOKEN ∧ C08_RECORD ∧
NO_UNBACKED ∧ ONLY_C08`.

1. `ROWS_TOTAL` ⟹ `parse_map` yields exactly 15 coverage lines, all 5-cell,
   with 15 distinct row ids.
2. `ONLY_C08` compares every base row id r ≠ C08: `five[r][4] == base[r]`.
   A missing base id, or a substituted id, fails via the `"?"` default /
   missing key, so the 15 ids are exactly the base ids and only C08's status
   cell may differ.
3. Base statuses (PROBE_REV `corpus/README.md`, byte-verified this round):
   C01 held, C02 partial, C03 held, C04 held, C05 uncovered, C06 held, C07
   held, C08 uncovered, C09 held, C10 partial, C11 held, C12 held, C13 held,
   C14 partial, C15 uncovered — **no `frontier` cell** (consistent with
   `controls/c2v2-do-nothing.log`: mismatch 0 at base).
4. `C08_TOKEN` ⟹ C08's status cell is `held`.
5. The probe (`reports/round-66/measure.py`) flags a row iff its last cell is
   `frontier` AND `ROW_OPS[id] ∩ record_ops ≠ ∅`. By 2–4 no row is frontier,
   so `README_TOKEN_LEGEND_MISMATCH=0 rows=[]` regardless of any planted
   records ⟹ `NO_NEW` holds. ∎

**Empirical demonstrations** (mutant still fails wherever pristine fails):

| tree | pristine fails | NO_NEW-mutant fails |
|---|---|---|
| c2-frontier (kind `c07frontier`) and c2-posfrontier (kind `posfrontier`): two independent builds of the same construction: positive + C07 `held`→`frontier` + planted `live/runs/round-93-fw` record (`inspect_firmware_regions`) | `NO_NEW, ONLY_C08` (both) | `ONLY_C08` (both) |
| c2-f5partial: C08 `partial` | `C08_TOKEN` | `C08_TOKEN` |

On the honest positive tree `NO_NEW` already passes, so the mutant is
indistinguishable from pristine there — it is not a broken counter, it is a
redundant gate.

**Routing (no control needed).** `NO_NEW` becomes load-bearing only if a
future change loosens `ONLY_C08` or `ROWS_TOTAL`, or the frozen base ever
carries a `frontier` row whose operation has no saved record (then "plant a
record for that row without touching status cells" is a NO_NEW-only kill
tree). Keep it as belt-and-suspenders; there is no missing control to add
while the base is frozen and its siblings stay strict.

## 5. Survivors

None. 20/20 non-equivalent mutants killed; the 1 surviving mutant is the
proven-equivalent `C2_NO_NEW` above (coverage finding, not a counter defect:
the leg is defense-in-depth, exactly the role claims.md gives it).

## 6. Integrity / restoration evidence

- Frozen originals byte-identical before and after all runs
  (`logs/frozen-before.sha256`, `logs/frozen-after.sha256`, `diff` empty):
  - `2a5132d0620aa9400a4025d8c0587fa095441af033d5e76a85e5969fe6ea9211`  c1_k_admit_counter2.py
  - `fba5a58a1d2b728be40b9da13671cc513c81998829ab19668bff5f1b89b41ca8`  c2_legend_counter2.py
  - `d6e70e52e8a9af6a8d559a820db0fd92093230c478d45fb4bedef104e51811f2`  forge_battery.py
  - `2e980194eff31a60173780e480b3465c831be5bac09d82ebf085ed5da59197c9`  claims.md
- `git status --porcelain` before and after all runs: exactly
  `?? .ufo/waves/round-93/` (the pre-existing untracked wave dir; no other
  entry appeared). No frozen file was opened for write; no mutating git
  command touched the lane (`git init` + `alternates` live in scratch only).
- Scratch `$HYAKU_SCRATCH/revenger-r93/MutationR93/` (trees, mutants,
  counter tempdirs, scratch git repo) removed after the artifacts were
  copied into this wave dir.
