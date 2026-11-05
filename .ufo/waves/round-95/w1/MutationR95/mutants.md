# MutationR95 — per-leg mutant audit of the frozen v4 counter (revenger round-95, w1)

Seat: MutationR95 (mutation-tester). Target: `reports/round-95/c1_k_admit_counter4.py`
at freeze commit `6e0bf15fed58f357b7fa0c881371ac7616a116f7` (frozen bytes `fbbec26cf1bcedea4117bff6d46be33d87dae426d76d1c44612efbcff039b6d9`).
Frozen bytes were never edited: every mutant is a scratch copy. Raw per-leg self-test
logs are in `receipts/` (17 leg logs + `BASELINE-selftest.log`).

## Method

1. `git clone --no-hardlinks` of the lane into scratch, `checkout --detach 6e0bf15…`
   (clone toplevel asserted: `/fast/scratch/hyaku/revenger-r95/MutationR95/mirror`).
   Mirror counter and mirror entry byte-identical to the frozen lane bytes
   (counter `fbbec26c…`, entry `476edc36d89ffdcf8cdafabc9cac4fc5dd49f68efe307d05c7db79a919479fb9`).
   `LANE` resolves to the mirror, so all counter git reads (`archive`/`cat-file -e` at
   FREEZE_REV `cb5c26f…`) and fixture entry reads run inside the clone; no lane write path
   is ever exercised.
2. Baseline: pristine mirror counter, `PYTHONUTF8=1 python3 -B … --self-test` with
   `HYAKU_SCRATCH=$SCRATCH/env/base` → `rc=0`, `SELFTEST_C1V4=pass legs=24`. Green
   baseline recorded before any mutant ran (a baseline failure would be inconclusive).
3. Per leg: one copy `mut_<LEG>.py`, ONE line mutated to constant pass (anchor table
   below), same self-test with its own `HYAKU_SCRATCH=$SCRATCH/env/<LEG>` subdir.
4. Verdict: self-test `rc=1` / `SELFTEST_C1V4=fail` ⇒ **KILLED** (the leg's forged delta
   or the do-nothing control is discriminating); self-test still green ⇒ **SURVIVED**
   (coverage finding, not a contract change).
5. Working-tree entry digest binding checked before start: normalized
   `admission-status: candidate` digest `476edc36d89ffdcf8cdafabc9cac4fc5dd49f68efe307d05c7db79a919479fb9`
   equals both the working-tree file sha256 and `git show 6e0bf15…:corpus/knowledge/round-95-evidence-ledger-discipline.md`.
   Every seat Python call used `python3 -B`.

## Verdicts: 11 KILLED / 6 SURVIVED

| Leg | Verdict | Discriminating forged delta (self-test FAIL lines) |
|---|---|---|
| C1_ROWS_TOTAL | **SURVIVED** | none — no forged delta targets row-count |
| C1_C10_HELD | **KILLED** | do-nothing control: `do-nothing base did not fail: rc=1` |
| C1_C10_CITES | **KILLED** | V07-legacy-path, V08-entry-pending |
| C1_ONLY_C10 | **KILLED** | ONLY-C10-second-row |
| C1_ADMITTED | **KILLED** | H1-indent-dup-status, F10-dup-status-fenced |
| C1_TRIO | **SURVIVED** | none |
| C1_REGISTRY | **KILLED** | V03-dup-json-keys-registry, M6-forged-registry-seat |
| C1_VOTES | **KILLED** | V04, V18, F17, F20, F12, F13, F15 (all seven) |
| C1_RECEIPTS | **KILLED** | V10-stale-fetched-at, V27-fabricated-body-foreign-host |
| C1_PYCACHE | **KILLED** | M5-pycache-planted |
| C1_LINT | **SURVIVED** | none |
| C1_EMBEDDED | **SURVIVED** | none |
| C1_EMBED_NONVACUOUS | **KILLED** | F18-ws-output, F18b-tilde-fence |
| C1_SIDS | **KILLED** | V19-sid-suffix-spaced, F16-unresolved-body-sid |
| C1_SOURCES | **KILLED** | F19-stale-new-row |
| C1_QUOTES | **SURVIVED** | none |
| C1_K_HELD_BACKED | **SURVIVED** | none |

## C1_REGISTRY — the r94 lesson M6 close, confirmed by mutation

The M6 code mutant (registry gate muted to constant pass) **DIES on v4**:
`rc=1`, `SELFTEST_C1V4=fail legs=24`, both registry-class vectors recorded:

```
SELFTEST FAIL: V03-dup-json-keys-registry: expected fail on C1_REGISTRY, got rc=0 failing=[]
SELFTEST FAIL: M6-forged-registry-seat: expected fail on C1_REGISTRY, got rc=0 failing=[]
```

In v3 the registry check had no own leg (r94 MutationR95 predecessor's SURVIVED
finding); v4's split makes the same mutation self-test-fatal. This is the round's
headline mutation result.

## Anchor table (the exact mutated line per leg; line numbers from the frozen bytes)

| Leg | Ln | Before (frozen) | After (mutant) |
|---|---|---|---|
| C1_ROWS_TOTAL | 440 | `    legs["C1_ROWS_TOTAL"] = len(cov) == 15` | `    legs["C1_ROWS_TOTAL"] = True  # MUTANT: constant pass` |
| C1_C10_HELD | 442 | `    legs["C1_C10_HELD"] = bool(crow) and crow[4] == "held"` | `    legs["C1_C10_HELD"] = True  # MUTANT: constant pass` |
| C1_C10_CITES | 444 | `    legs["C1_C10_CITES"] = (bool(crow) and fileset == [ENTRY_REL]` | `    legs["C1_C10_CITES"] = True or (bool(crow) and fileset == [ENTRY_REL]  # MUTANT: constant pass` |
| C1_ONLY_C10 | 454 | `        legs["C1_ONLY_C10"] = (not diffs and crow is not None` | `        legs["C1_ONLY_C10"] = True or (not diffs and crow is not None  # MUTANT: constant pass` |
| C1_ADMITTED | 463 | `    legs["C1_ADMITTED"] = (len(st_idx) == 1 and st_idx[0] < HEAD_WINDOW` | `    legs["C1_ADMITTED"] = True or (len(st_idx) == 1 and st_idx[0] < HEAD_WINDOW  # MUTANT: constant pass` |
| C1_TRIO | 465 | `    legs["C1_TRIO"] = all(any(l.startswith(k) for l in head)` | `    legs["C1_TRIO"] = True or all(any(l.startswith(k) for l in head)  # MUTANT: constant pass` |
| C1_REGISTRY | 470 | `    legs["C1_REGISTRY"] = reg_ok` | `    legs["C1_REGISTRY"] = True  # MUTANT: constant pass` |
| C1_VOTES | 472 | `    legs["C1_VOTES"] = v_ok` | `    legs["C1_VOTES"] = True  # MUTANT: constant pass` |
| C1_RECEIPTS | 474 | `    legs["C1_RECEIPTS"] = r_ok` | `    legs["C1_RECEIPTS"] = True  # MUTANT: constant pass` |
| C1_PYCACHE | 476 | `    legs["C1_PYCACHE"] = p_ok` | `    legs["C1_PYCACHE"] = True  # MUTANT: constant pass` |
| C1_LINT | 483 | `        legs["C1_LINT"] = lint.returncode == 0` | `        legs["C1_LINT"] = True  # MUTANT: constant pass (if-branch; else-branch unreachable in fixtures)` |
| C1_EMBEDDED | 488 | `        legs["C1_EMBEDDED"] = emb_ok` | `        legs["C1_EMBEDDED"] = True  # MUTANT: constant pass` |
| C1_EMBED_NONVACUOUS | 490 | `        legs["C1_EMBED_NONVACUOUS"] = nv_ok` | `        legs["C1_EMBED_NONVACUOUS"] = True  # MUTANT: constant pass` |
| C1_SIDS | 497 | `    legs["C1_SIDS"] = s_ok` | `    legs["C1_SIDS"] = True  # MUTANT: constant pass` |
| C1_SOURCES | 499 | `    legs["C1_SOURCES"] = src_ok` | `    legs["C1_SOURCES"] = True  # MUTANT: constant pass` |
| C1_QUOTES | 501 | `    legs["C1_QUOTES"] = q_ok` | `    legs["C1_QUOTES"] = True  # MUTANT: constant pass` |
| C1_K_HELD_BACKED | 508 | `    legs["C1_K_HELD_BACKED"] = held_backed == HELD_TARGET` | `    legs["C1_K_HELD_BACKED"] = True  # MUTANT: constant pass` |

For the four multi-line assignments (C10_CITES 444–445, ONLY_C10 454–455, ADMITTED
463–464, TRIO 465–466) the `True or` prefix on the first line forces the whole
expression true; the continuation line is byte-untouched. The LINT mutant mutates the
if-branch only; the else-branch (line 492, entry file absent) is unreachable in every
fixture, so within all self-test scenarios the leg is constant pass.

## Self-test tails (verbatim, per leg)

Baseline (pristine): `rc=0` → `SELFTEST_C1V4=pass legs=24`

```
C1_ROWS_TOTAL         rc=0  SELFTEST_C1V4=pass legs=24
C1_C10_HELD           rc=1  SELFTEST_C1V4=fail legs=24
                            SELFTEST FAIL: do-nothing base did not fail: rc=1
C1_C10_CITES          rc=1  SELFTEST_C1V4=fail legs=24
                            SELFTEST FAIL: V07-legacy-path: expected fail on C1_C10_CITES, got rc=1 failing=['C1_VERDICT']
                            SELFTEST FAIL: V08-entry-pending: expected fail on C1_C10_CITES, got rc=0 failing=[]
C1_ONLY_C10           rc=1  SELFTEST_C1V4=fail legs=24
                            SELFTEST FAIL: ONLY-C10-second-row: expected fail on C1_ONLY_C10, got rc=1 failing=['C1_VERDICT']
C1_ADMITTED           rc=1  SELFTEST_C1V4=fail legs=24
                            SELFTEST FAIL: H1-indent-dup-status: expected fail on C1_ADMITTED, got rc=1 failing=['C1_VOTES', 'C1_VERDICT']
                            SELFTEST FAIL: F10-dup-status-fenced: expected fail on C1_ADMITTED, got rc=1 failing=['C1_VOTES', 'C1_VERDICT']
C1_TRIO               rc=0  SELFTEST_C1V4=pass legs=24
C1_REGISTRY           rc=1  SELFTEST_C1V4=fail legs=24
                            SELFTEST FAIL: V03-dup-json-keys-registry: expected fail on C1_REGISTRY, got rc=0 failing=[]
                            SELFTEST FAIL: M6-forged-registry-seat: expected fail on C1_REGISTRY, got rc=0 failing=[]
C1_VOTES              rc=1  SELFTEST_C1V4=fail legs=24
                            SELFTEST FAIL: V04-dup-json-keys-vote / V18-na-letter-flood / F17-vacuous-na /
                                           F20-foreign-artifact-dir / F12-case-dup-seat / F13-role-mismatch /
                                           F15-traversal — all seven: expected fail on C1_VOTES, got rc=0 failing=[]
C1_RECEIPTS           rc=1  SELFTEST_C1V4=fail legs=24
                            SELFTEST FAIL: V10-stale-fetched-at / V27-fabricated-body-foreign-host — got rc=0 failing=[]
C1_PYCACHE            rc=1  SELFTEST_C1V4=fail legs=24
                            SELFTEST FAIL: M5-pycache-planted: expected fail on C1_PYCACHE, got rc=0 failing=[]
C1_LINT               rc=0  SELFTEST_C1V4=pass legs=24
C1_EMBEDDED           rc=0  SELFTEST_C1V4=pass legs=24
C1_EMBED_NONVACUOUS   rc=1  SELFTEST_C1V4=fail legs=24
                            SELFTEST FAIL: F18-ws-output: expected fail on C1_EMBED_NONVACUOUS, got rc=1 failing=['C1_VOTES', 'C1_EMBEDDED', 'C1_VERDICT']
                            SELFTEST FAIL: F18b-tilde-fence: expected fail on C1_EMBED_NONVACUOUS, got rc=1 failing=['C1_VOTES', 'C1_EMBEDDED', 'C1_VERDICT']
C1_SIDS               rc=1  SELFTEST_C1V4=fail legs=24
                            SELFTEST FAIL: V19-sid-suffix-spaced: expected fail on C1_SIDS, got rc=1 failing=['C1_VOTES', 'C1_SOURCES', 'C1_VERDICT']
                            SELFTEST FAIL: F16-unresolved-body-sid: expected fail on C1_SIDS, got rc=1 failing=['C1_VOTES', 'C1_SOURCES', 'C1_VERDICT']
C1_SOURCES            rc=1  SELFTEST_C1V4=fail legs=24
                            SELFTEST FAIL: F19-stale-new-row: expected fail on C1_SOURCES, got rc=0 failing=[]
C1_QUOTES             rc=0  SELFTEST_C1V4=pass legs=24
C1_K_HELD_BACKED      rc=0  SELFTEST_C1V4=pass legs=24
```

(Full untruncated logs per leg in `receipts/<LEG>.log`; the C1_VOTES tail above is
compacted for width — the raw log carries one line per vector.)

## Coverage findings (survivors — route to r96, do NOT edit the frozen counter)

Six legs have no isolating forged delta in the frozen 22-vector battery; muting them to
constant pass leaves `SELFTEST_C1V4=pass legs=24` green:

1. `C1_ROWS_TOTAL` — no delta adds/removes a coverage row (row-count drift undetected).
2. `C1_TRIO` — no delta deletes the `source:`/`verified-at:`/`recheck:` header trio.
3. `C1_LINT` — no delta makes the real `corpus/lint_entry.py` fail.
4. `C1_EMBEDDED` — no delta makes the real `corpus/check_embedded_outputs.py` fail.
5. `C1_QUOTES` — no delta forges a quote/receipt mismatch that `audit_source_quotes.py verify` rejects.
6. `C1_K_HELD_BACKED` — no delta moves a held row's backing cell so the count leaves 12
   (the ONLY-C10-second-row delta does shift it 12→11 incidentally, but its pinned leg is C1_ONLY_C10).

Secondary observations:

- `C1_C10_HELD` is the only leg backstopped by the do-nothing control; every other
  killed leg dies purely on its `EXPECT_FAIL` leg assertion. Killing the do-nothing
  check would leave C10_HELD mutant-survivable.
- Killed legs with `got rc=0 failing=[]` (REGISTRY, VOTES×7, RECEIPTS×2, PYCACHE,
  SOURCES) are load-bearing with zero redundancy: once muted, the forged tree passes
  the WHOLE counter. Legs killed with a residual `failing=[...]` (C10_CITES/V07,
  ONLY_C10, ADMITTED, EMBED_NONVACUOUS, SIDS) at least fail the overall verdict
  elsewhere — mostly via `C1_VOTES` digest-binding (any entry-byte edit shifts the
  normalized digest and breaks vote `candidate_sha256` equality) — but the per-leg
  discrimination the self-test pins is still the only thing identifying the class.
- Restated for C2: the v4 self-test's expected-leg assertion is what kills these
  mutants; a hypothetical counter that only checked `C1_VERDICT` would leave
  C10_CITES/ONLY_C10/ADMITTED/EMBED_NONVACUOUS/SIDS mutant-survivable via the
  digest-binding side effect. The leg assertion is load-bearing, not cosmetic.

## Restoration evidence

- Lane `reports/round-95/c1_k_admit_counter4.py`: before `fbbec26cf1bcedea4117bff6d46be33d87dae426d76d1c44612efbcff039b6d9`,
  after the full run `fbbec26cf1bcedea4117bff6d46be33d87dae426d76d1c44612efbcff039b6d9` — unchanged.
- Lane `corpus/knowledge/round-95-evidence-ledger-discipline.md`: before/after `476edc36d89ffdcf8cdafabc9cac4fc5dd49f68efe307d05c7db79a919479fb9` — unchanged.
- Mirror baseline counter identical to frozen bytes throughout; all 17 mutants + the
  clone lived only under `/fast/scratch/hyaku/revenger-r95/MutationR95/`, deleted at
  seat exit (receipt logs copied to `receipts/` first).
- No lane files, no votes, no claims bytes touched; no git write commands against the
  lane (clone + checkout ran inside the scratch clone only, toplevel asserted).
