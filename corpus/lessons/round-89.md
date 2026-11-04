# Round-89 lesson — host drift is not a marker count; Android becomes reachable

Base `2b017fa3c616a84b7b491e3312029fa8a8c076e6`; freeze
`c84339c051443e13f6a546cf186cc8965649a932`. The original frozen predicates
and targets remain in `reports/round-89/claims.md`; no later finding changes
them. Two claims: C1 freshness (frozen census mismatch count 10 → target 0),
C2 coverage (F4 10/11 → target 11/11 together with the APK oracle 19/19).
This lesson is the lane's own evidence, not outside admission.

## Gate

### Fixed inputs and controls

- C1 source evidence: S480, the committed red receipt
  `reports/round-89/census-red.log`. Command:
  `PYTHONUTF8=1 python3 -B corpus/census_reprobe.py --root TREE`, where TREE
  contains the `2b017fa3` census-file archive. Observed `CENSUS_ROWS=18`,
  `CENSUS_STALE_UNFLAGGED=10`, exit 1. The frozen code counts findings, not
  deduplicated row ids; the base happens to produce one finding for each of
  ten ids. Do not generalize this equality to later inputs.
- The frozen C1 instrument is
  `c3127ffc18a54f85f01e2fb88f50b5db694484588e5b7467ae5567ffdd3b648a`.
  Its hermetic selftest prints nine leg results and `CENSUS_SELFTEST=pass`
  (`reports/round-89/census-selftest.log`). This is helper-level evidence;
  outside review must not read it as full public-interface conformance.
- C1 rejects the committed blind-token control: appending the live tokens
  indiscriminately still yields 7 findings, exit 1
  (`reports/round-89/junk-control.log`). This one finite control does not
  prove resistance to all lexical forgery.
- C2 source evidence: S481 and S482. The F4 mapping stays frozen at
  `reports/round-81/f_probe4.py`, digest
  `4d871971fa49131f65e951bba1061a00b16c9eee8c3dc7df007fff434566a3c7`.
  Base command `python3 -B reports/round-81/f_probe4.py TREE/corpus`
  prints `F4_COVERAGE=10/11 score=9.09`, exit 0
  (`reports/round-89/f4-red.log`). The APK fixture's saved bytes already
  existed; only a new producer record is intended coverage work.
- The C2 oracle is frozen at
  `44fd1505d171c4e37d5d36ecd4a8aa5aff30229538840692bd0dc9cffde68a53`.
  A scratch producer record passed 19/19; changing its package_name to
  `com.example.other` caused 18/19, exit 1
  (`reports/round-89/oracle-design.log`, `oracle-tamper-control.log`).
  The expected fixture digest, size and member digests come from the old
  truth.json; the DEX class_defs_size is read from bytes at 0x60. The oracle
  is fixture-specific and does not prove general format accuracy or origin.

### Admission boundary

C1's mixed-state K04 is a concrete problem with the frozen predicate: one
scored cell must describe ghidra present and ida absent. The shared-text
presence rule forbids either state word when checking the other tool.
Accurate prose must not be distorted to game this predicate. A residual is
a target miss, not permission to weaken the rule or replace the target.
The final measured receipts and wave findings below govern the verdict.

No new knowledge entry or coverage-map admission is made by this round.
Correcting the pre-contract census appends a new dated table; old tables
remain historical bytes. The record evidence concerns one inert APK and a
static producer call, not APK execution, Android runtime behavior, or
producer provenance.

### Carry-in

`reports/round-89/carry-in.md` records all four r88 outside-review notes,
the current-base precision correction, and the direct-jj procedural
deviation. Old missing draft receipts are not invented or backdated.
The literal source-census command now works on Linux (both round-start
forms exit 0); Windows-layout exit-2 history is not rewritten.

### Source openings

The new rows S480–S482 are own-work evidence, authoritative only for what
the quoted local artifacts print. The final source-opening table records
the exact path, access date, located quote and disposition. A lane wave
seat is still this lane; outside admit/reject spot-check remains pending.

### Latest considerthese proposal mined

Opened `considerthese/2026-11-04.md` this round (operator-authored input,
unchanged). Proposal 1 asks for new rows split by kind and tier and a flag
when external additions are zero. The bounded curation census at final
measurement implements exactly that reporting practice; it does not claim
external learning from own-work receipts. Other four proposals remain
unimplemented. No package from shokuknow is adopted: **Assimilation: none**.
No registry or campaign source tree outside this lane is written.

## Mistakes

| class | evidence pointer | captured-by | fix / outcome |
|---|---|---|---|
| Source-field confusion in the first APK oracle: build_recipe.members records names and byte lengths, not member sha256; the first check fetched missing digests from the wrong section | final oracle lines 71–76 and `reports/round-89/oracle-design.log`; actual initial run printed `ORACLE FAIL (18/19 checks)` before freeze | Q03 and the premise run against the real fixture | Before freeze, use the top-level truth.json members digest table and require every expected member to have a digest. Final positive control passes; the package-name forgery remains red. The initial failing output was not saved as a file, so it is observed transcript history, not a durable red receipt for this fix. |
| Case-fold disagreement in listing phantom detection: lowercased names compared with mixed-case live names falsely called SKILL.md absent | frozen `corpus/census_reprobe.py` uses live_l case-folding; actual prefreeze red initially named `skill.md` absent | Hand-reading the red finding against the directory listing | Before freeze, case-fold both sets. Current red correctly names missing HOST-CONTRACT.md instead. The initial failing output was not saved; no claim of durable before/after proof for this repair. |
| Clean fixture contradicted its own live state: observed `absent` alongside verdict `present` | actual initial selftest printed `CENSUS_SELFTEST_clean=FAIL`; final `reports/round-89/census-selftest.log` | Frozen selftest's clean control | Before freeze, correct the synthetic observed cell. Final selftest is green. This exposes the later mixed-state K04 limitation rather than fixing it. |
| Row-wide state conflation for multiple tools | K04 in the frozen instrument and census; `reports/round-89/claims.md` target 0 | Read-through of the frozen rule and fresh review | Preserve correct per-tool states and report the miss. No post-score instrument repair; a future counter must scope states to individual tools and pass a mixed-state public-path negative. |
| Helper-only state repair bypass | `reports/round-89/carry-in.md` Commit-helper deviation; freeze commit c84339c | Helper rejected a non-tip working-copy base | The author used one direct jj new despite the prohibition. Recorded as conformance defect, not justified as an authorized workaround; no further direct VCS mutation. |

## Outside verification

No `[x]` promotion mark and no non-author discernment credit is asserted.
The closure integrator must sample a new source admit and a rejected
claim/forgery, reopen the source, and re-derive the frozen counters.

## Final measurements (adjudication, this commit)

Environment: `reports/round-89/environment.log` (HOME `/home/vgpnk`,
fnm-multishell PATH). Commits: base `2b017fa3`, freeze `c84339c`, landing
`6ce41aa`, adjudication = this commit.

| counter | base | landed | frozen target | verdict |
|---|---|---|---|---|
| `CENSUS_STALE_UNFLAGGED` (findings) | 10 (10 rows, lane PATH) | **2** (1 row: K04) | 0 | **MISS** |
| `F4_COVERAGE` | 10/11 (9.09) | 10/11 (9.09) — the rejected record is outside the counted surface | 11/11 | **MISS / KILLED** |
| `ORACLE OK` over the preserved record | n/a | 19/19 | 19/19 | nominal only; does not authenticate |
| producer two-run byte identity | n/a | **differs at byte 20** | identical | **FAIL** |
| separability (C1-only / C2-only) | — | F4 stays 10/11 / census stays 10 | isolated | PASS |
| no-work control (untouched base) | 10, F4 10/11 | — | cannot reach either target | PASS |

Wave: 12 seats, one v1 wave — 3 scribe, 2 executor, 1 scout, 2 reviewer,
1 critic, 2 mutation-tester, 1 connector, 1 sentinel (5 attack seats, 42 %).
Seats `ScribeR89Rows` and `ScribeR89Registry` stalled after prototyping; the
L1 executed both items directly (census tables and the registry/README edits)
and their wave dirs are retained as evidence. No seat wrote outside its
declared files; no seat died with a lane-file write.

Admission: **not admitted.** C1's target is unreachable under the frozen
rules; C2's kill rules fire. The round lands the correction, the preserved
rejected evidence, the registry limits and the lesson, and reports the miss.

The mined mistake table above stays as written before the landing; the two
later findings (K04 residual 2, producer non-determinism) were reported by
`ReviewerR89C1`/`CriticR89Claims`/`ReviewerR89C2` and are recorded in the
Gate section rather than retro-added as mistakes.
