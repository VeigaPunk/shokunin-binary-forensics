# MutationR94 — one-per-leg mutants of the frozen v3 counter (C2 support)

Target instrument: `reports/round-94/c1_k_admit_counter3.py`, frozen bytes, sha256
`de2815be742737cb66ffc5249aa61b25173cec138b8e4b958eb2e171175d799e` — byte-identical
before and after the probe (`cmp` clean against the start-of-run pristine copy); every
mutant lived only in scratch (`/fast/scratch/hyaku/revenger-r94/MutationR94/mut/`,
deleted on exit).

## Method

Each leg got exactly one behavior-bearing mutation (invert its comparison or drop/disable
its check) in a scratch copy. Per mutant, the bounded behavioral detector was run as the
counter's own self-test sequence — POS honest fixture, the 12 frozen `EXPECT_FAIL` forged
deltas each on its frozen expected leg, and the do-nothing FREEZE_REV control — plus a
full honest `--tree` run over a fixture built by importing the ORIGINAL module's
`_fixture`. Runs are in-process against the mutant module with `mod.LANE` injected: a
scratch-resident copy derives `LANE` from `__file__` (`parents[2]` → scratch), which would
pass a bogus `--lane` to `corpus/lint_entry.py`, run `git -C <scratch> archive` in
`base_readme` (breaking `C1_ONLY_C15`) and miss the entry in `_fixture` — i.e. fail every
run for harness reasons, not mutation reasons. The shipped subprocess `--self-test` of the
PRISTINE frozen path was also run: `SELFTEST_C1V3=pass legs=14`, rc 0, and the in-process
pristine replica agrees on every leg, validating the replication. Full outputs:
`logs/<LEG>.log`, `logs/baseline.log`, driver: `logs/driver.py`.

Baseline anchors: honest fixture `C1_VERDICT=pass` with candidate digest
`01d51059fb29a5184342b2815e643695aa269b384c04d005f69556816f291bd3`; the frozen
`--rev 060a8e87d6de6b31f91b58524ab0fcad88ae5431` run prints the SAME digest
(vote-binding digest cross-check) and `C1_VERDICT=fail` at the freeze tip, as frozen.

Verdicts: **12 KILLED / 2 SURVIVED / 0 EQUIVALENT.**

## Verdict table

| leg | one-point mutant | verdict | killed by |
|---|---|---|---|
| C1_ROWS_TOTAL | `len(cov) == 15` → `!= 15` | KILLED | honest fixture fails |
| C1_C15_HELD | `c15[4] == "held"` → `!= "held"` | KILLED | honest fails AND do-nothing control inverts |
| C1_C15_CITES | `ENTRY_REL in c15[2]` → `not in` | KILLED | honest fixture fails |
| C1_ONLY_C15 | drop `not diffs and` | KILLED | detector: second-row class moves off its frozen leg |
| C1_ADMITTED | `len(st_lines) == 1` → `>= 1` | KILLED | detector: F10 moves off its frozen leg |
| C1_TRIO | `all(...)` → `not all(...)` | KILLED | honest fixture fails |
| C1_VOTES | `legs["C1_VOTES"] = v_ok` → `= True` | KILLED | 6 forged classes pass outright |
| C1_REGISTRY | drop `if not reg_ok: return` gate | SURVIVED | self-test fully green (redundancy finding) |
| C1_LINT | `lint.returncode == 0` → `!= 0` | KILLED | honest fixture fails |
| C1_EMBEDDED | drop exit-2 no-`$`-blocks clause | KILLED | honest fixture fails |
| C1_EMBED_NONVACUOUS | tilde guard `if any(...)` → `if False:` | KILLED | detector: F18b moves off its frozen leg |
| C1_SOURCES | `legs["C1_SOURCES"] = s_ok` → `= True` | KILLED | F19 passes outright |
| C1_QUOTES | `legs["C1_QUOTES"] = q_ok` → `= True` | SURVIVED | self-test fully green (coverage finding) |
| C1_K_HELD_BACKED | `held_backed == 11` → `!= 11` | KILLED | honest fixture fails |

## Per-leg detail (deciding runs quoted from logs)

### C1_ROWS_TOTAL — KILLED
- diff: `legs["C1_ROWS_TOTAL"] = len(cov) == 15` → `legs["C1_ROWS_TOTAL"] = len(cov) != 15`
- deciding run (honest --tree): `C1_ROWS_TOTAL=fail` … `C1_VERDICT=fail` (pristine: pass, rc 0). Log: `logs/C1_ROWS_TOTAL.log`.

### C1_C15_HELD — KILLED
- diff: `c15[4] == "held"` → `c15[4] != "held"`
- deciding runs: honest `C1_C15_HELD=fail`/`C1_VERDICT=fail`; AND the do-nothing control
  inverts — base (C15 `uncovered`) now satisfies the inverted leg, so the frozen control
  assertion `C1_C15_HELD=fail on do-nothing` no longer holds. Log: `logs/C1_C15_HELD.log`.

### C1_C15_CITES — KILLED
- diff: `ENTRY_REL in c15[2]` → `ENTRY_REL not in c15[2]`
- deciding run: honest `C1_C15_CITES=fail`/`C1_VERDICT=fail`. Log: `logs/C1_C15_CITES.log`.

### C1_ONLY_C15 — KILLED (detector-level; class still verdict-rejected)
- diff: `legs["C1_ONLY_C15"] = not diffs and c15 is not None and …` → `= c15 is not None and …` (the `diffs` term dropped)
- deciding run (ONLY-C15-second-row delta): `C1_K_HELD_BACKED=10/15`, `C1_ONLY_C15=pass`,
  `C1_K_HELD_BACKED=fail`, `C1_VERDICT=fail` — the class is still rejected, but via
  `C1_K_HELD_BACKED` (the C07 held→partial flip drops the held count) instead of its
  frozen leg; the frozen expected-leg assertion breaks, so the mutated `--self-test` fails.
- load-bearing nuance: the backstop only exists because the frozen class moves a *held*
  row; a second-row move on a non-held row has no backstop and would pass outright under
  this mutant. The leg is verdict-load-bearing for that shape; the frozen class exercises
  only the held-row shape. Log: `logs/C1_ONLY_C15.log`.

### C1_ADMITTED — KILLED (detector-level; class still verdict-rejected)
- diff: `legs["C1_ADMITTED"] = (len(st_lines) == 1 and …` → `(len(st_lines) >= 1 and …` (uniqueness comparison dropped)
- deciding run (F10-dup-status delta): `C1_ADMITTED=pass`, `C1_VOTES=vote digest mismatch
  for CriticR94 digest=5d2bbed1d33eff2a84317b2ba300934b003e55d9442c0a22d6418d76fa279307`,
  `C1_VERDICT=fail` — status-line normalization canonicalizes values, not count, so the
  duplicate line still changes the normalized bytes (5d2bbed1… vs candidate 01d51059…)
  and the digest-bound vote leg rejects the class; the frozen C1_ADMITTED leg assertion
  breaks. The uniqueness check is diagnostic deepening on top of a real vote-digest
  backstop. Log: `logs/C1_ADMITTED.log`.

### C1_TRIO — KILLED
- diff: `legs["C1_TRIO"] = all(any(...))` → `not all(any(...))`
- deciding run: honest `C1_TRIO=fail`/`C1_VERDICT=fail`. Log: `logs/C1_TRIO.log`.

### C1_VOTES — KILLED (verdict-level; strongest finding)
- diff: `legs["C1_VOTES"] = v_ok` → `legs["C1_VOTES"] = True`
- deciding runs: F11 `C1_VOTES=pass`/`C1_VERDICT=pass`; likewise F12-case-dup-seat,
  F13-role-mismatch, F14-empty-artifact, F15-traversal, F17-vacuous-na — six frozen
  forgery classes pass the whole counter outright. The vote leg is the sole
  verdict-load-bearing enforcement for all of them (pinned-seat check, canonical
  uniqueness, role match, artifact binding/traversal, n/a reasons). Log: `logs/C1_VOTES.log`.

### C1_REGISTRY — SURVIVED (defect/coverage finding)
- diff: dropped `if not reg_ok: return False, f"registry: {reg_reason}"` from `check_votes`
- deciding runs: POS honest passes; all 12 deltas keep their overall verdicts; self-test
  green. Observable delta: F11's failure reason moves from pristine
  `registry: registry!=pinned missing=[] extra=['FabA'] rolemismatch=[]` to
  `seat not in pinned registry: 'FabA' (FabA.json)` — the pinned-seat vote subcheck
  catches F11 independently (defense-in-depth).
- coverage finding: a REGISTRY-ONLY forgery (members map altered from the pinned map, all
  votes cast by valid pinned seats) is not among the frozen twelve; under this mutant such
  a tree passes v3 outright, and the dropped gate is its only enforcement point. No frozen
  test kills the gate's removal → routable r95 class (registry-only, no rogue vote).
  Log: `logs/C1_REGISTRY.log`.

### C1_LINT — KILLED
- diff: `legs["C1_LINT"] = lint.returncode == 0` → `!= 0`
- deciding run: honest `C1_LINT=fail`/`C1_VERDICT=fail` (REAL `corpus/lint_entry.py` in the
  loop). Log: `logs/C1_LINT.log`.

### C1_EMBEDDED — KILLED
- diff: `emb_ok = emb.returncode == 0 or (emb.returncode == 2 and "could-not-evaluate" … and not has_cmd_block)` → `emb_ok = emb.returncode == 0`
- deciding run: honest fixture (docs-only entry, no `$` blocks) — the REAL
  `corpus/check_embedded_outputs.py` exits 2 `could-not-evaluate`; pristine passes via the
  exit-2 clause (the finding-11 close), the mutant fails honest: `C1_EMBEDDED=fail`/
  `C1_VERDICT=fail`. Log: `logs/C1_EMBEDDED.log`.

### C1_EMBED_NONVACUOUS — KILLED (detector-level; class still verdict-rejected)
- diff: tilde-fence guard `if any(l.lstrip().startswith("$") for l in lines):` → `if False:`
- deciding run (F18b-tilde-fence delta): `C1_VOTES=vote digest mismatch … digest=2bc5f808…`,
  `C1_EMBEDDED=fail`, `C1_EMBED_NONVACUOUS=pass`, `C1_VERDICT=fail` — the class stays
  rejected via the vote-digest backstop AND via C1_EMBEDDED (the appended `~~~` `$ `-line
  satisfies `has_cmd_block`, disabling the exit-2 clause, so the real checker fails); the
  frozen leg assertion breaks. The ```-branch (F18 whitespace output) was left intact and
  still fires. Log: `logs/C1_EMBED_NONVACUOUS.log`.

### C1_SOURCES — KILLED (verdict-level)
- diff: `legs["C1_SOURCES"] = s_ok` → `legs["C1_SOURCES"] = True`
- deciding run (F19-stale-new-row delta): `C1_SOURCES=pass`, `C1_VERDICT=pass` — a stale
  new-row opened-date passes the whole counter: SOURCES.md is not digest-bound and no
  other leg reads it, so this leg is the sole line of defense for F19. Contrast: the
  F16 body-sid delta remains rejected (entry bytes change → vote digest mismatch), i.e.
  body-sid resolution is double-backed while new-row status/date/tier/cite-back is not.
  Log: `logs/C1_SOURCES.log`.

### C1_QUOTES — SURVIVED (defect/coverage finding)
- diff: `legs["C1_QUOTES"] = q_ok` → `legs["C1_QUOTES"] = True`
- deciding runs: POS honest passes (receipts present); no frozen delta flips; self-test
  green. Observable delta: the do-nothing base run now prints `C1_QUOTES=pass` where
  pristine prints `C1_QUOTES=fail` (verdict unchanged — other legs still fail the base).
- coverage finding: no frozen forged class targets the receipts leg (stale `fetched_at`,
  quote-not-in-body, wrong `fetch_sha256`, wrong span). The leg does real work on the
  honest path (it fails on the base tree, where S498/S499 rows and receipts are absent)
  but the battery never forges receipts, so nothing kills this mutant → routable r95
  class (forged/stale quote receipt). Log: `logs/C1_QUOTES.log`.

### C1_K_HELD_BACKED — KILLED
- diff: `legs["C1_K_HELD_BACKED"] = held_backed == 11` → `!= 11`
- deciding run: honest `C1_K_HELD_BACKED=fail`/`C1_VERDICT=fail`. Log: `logs/C1_K_HELD_BACKED.log`.

## Restoration evidence

- Frozen counter before/after: sha256 `de2815be742737cb66ffc5249aa61b25173cec138b8e4b958eb2e171175d799e`,
  `cmp` clean against the pristine copy taken at probe start. No lane file was written;
  no git/jj write command was run; no host sysctl touched; nothing installed.
- All mutant bytes and fixtures lived under `/fast/scratch/hyaku/revenger-r94/MutationR94/`
  and the tree was deleted after the receipts above were copied into this seat dir.

## Calibration read (C2 support)

Every frozen forged class keeps an enforcement point under any single-leg kill except
when `C1_VOTES` or `C1_SOURCES` is disabled — those two are the verdict-load-bearing legs
(six classes and F19 respectively pass outright). The remaining legs are either
honest-path-load-bearing (flip the honest verdict when broken: ROWS_TOTAL, C15_HELD,
C15_CITES, TRIO, LINT, EMBEDDED, K_HELD_BACKED) or diagnostic deepening on top of the
digest-binding vote backstop (ADMITTED, ONLY_C15, EMBED_NONVACUOUS — caught by the frozen
leg-specific detector assertions). The two survivors are coverage gaps in the frozen
class set (registry-only forgery; forged/stale quote receipt), not exploitable holes in
the frozen twelve.
