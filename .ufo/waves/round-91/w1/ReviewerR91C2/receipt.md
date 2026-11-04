# ReviewerR91C2 — C2 falsification receipt (round 91, attempt 1)

Instrument: `reports/round-91/message_tree_check.py` (landed during this wave,
10548 bytes, 19:43). Pre-registration: `expected-pre-registered.md` (written
before the first instrument run). Fixture: `build_fixture.sh` →
`/fast/scratch/hyaku/revenger-r91/ReviewerR91C2/fixture.Aoe3Bc` (protocol:
mktemp under `$HYAKU_SCRATCH/revenger-r91/ReviewerR91C2`, `git -C "$D"` on
every call, toplevel asserted before first commit). Runner: `run_cases.sh`.
Raw outputs: `out-<case>.txt` (this dir). Verdicts: `verdicts.tsv`.

## Canonical table — 8 fixture cases + 5 real commits (C2_DISAGREE denominator)

"Hand" = my pre-registered spec-faithful expectation (backticked paths + .log
names per frozen claims.md §C2, commit's own tree). "Obs" = instrument on the
committed bytes.

| # | input | expected cited/miss | observed cited/miss | exit exp/obs | verdict |
|---|-------|---------------------|---------------------|--------------|---------|
| a | prose `missing/case-a.txt`, no backticks, target missing | 0/0 | 1/1 `missing=missing/case-a.txt` | 0/1 | **DISAGREE** |
| b | `` `corpus/self_check.py:12` `` | 1/0 | 1/0 | 0/0 | AGREE |
| c | `` `corpus/` `` (directory) | 1/0 | 1/0 | 0/0 | AGREE |
| d | bare `` `case-d-receipt.log` `` added only by the NEXT commit | 1/1 | 1/1 `missing=case-d-receipt.log` | 1/1 | AGREE |
| e | `` `./corpus/other.py` `` + `` `corpus/other.py,` `` | 2/0 | 2/0 (composition differs: dedupe of other.py + prose `reports/case-d-receipt.log` — count coincides) | 0/0 | AGREE (note) |
| f | F1 add+cite `` `corpus/old_name.py` `` / F2 rename, cite old+new | F1 1/0; F2 2/1 | F1 1/0; F2 2/1 `missing=corpus/old_name.py` | 0/0; 1/1 | AGREE (own-tree basis pinned both directions) |
| g | `` `git status` `` `` `git log -1` `` `` `--amend` `` `` `jj` `` | 0/0 | 0/0 | 0/0 | AGREE |
| h | Hside `` `corpus/side.py` `` + `--no-ff` Hmerge citing it | 1/0 each, merge not skipped | 1/0 each, merge commit line present, no crash | 0/0 | AGREE |
| R1 | d509e98 (real) | 0/0 | 1/1 `missing=ufo-wave-policy.json` (fleet-root file, 0 in-lane hits) | 0/1 | **DISAGREE** |
| R2 | b13aac7 (real) | 0/0 | 1/1 `missing=claims.md` — commit CREATES reports/round-91/claims.md; 30 same-named in-tree files → non-unique suffix → false miss | 0/1 | **DISAGREE** |
| R3 | 45b2713 (real) | 4/0 | 8/2 `missing=c1-only.log,noharm-diff.txt` (11 and 13 same-named in-tree hits); extra hits: corpus/lessons/round-88.md, LOG.md, SCORECARD.md, all prose | 0/1 | **DISAGREE** |
| R4 | 6ce41aa (real) | 3/0 | 6/3 `missing=inspection.json,receipt.json,LEDGER.md` (31/21/72 same-named hits) | 0/1 | **DISAGREE** |
| R5 | 5f7ecce (real) | 1/0 | 2/0 (extra prose hit corpus/lessons/round-89.md) | 0/0 | **DISAGREE** (composition) |

**C2_DISAGREE=6/13** (case a + R1–R5). Every disagreement names its input and
the instrument's output above; per-token composition in
`composition.py` output (copied as `composition-out.txt`).

## Supplementary legs (outside the 13)

- AGG (fixture `C0..C_MERGE`, 11 commits): obs commits=11 cited=14 misses=3
  exit 1 vs spec-faithful misses=2 — the +1 is case a's prose path.
- Real declared range `7fab03f..refs/heads/main`: `MESSAGE_TREE commits=23
  cited=25 misses=9` exit 1; 6 commits carry misses. **All 9 misses are
  non-defects**: 8 cite files present in the commit's own tree under several
  directories (claims.md ×30, w1-results.json ×4, truth.json ×53,
  inspection.json ×31, receipt.json ×21, LEDGER.md ×72, c1-only.log ×11,
  noharm-diff.txt ×13 — uniqueness-gated suffix resolution flags them
  missing); 1 (ufo-wave-policy.json) is a fleet-root orchestration file never
  meant to live in the lane (0 in-lane hits), reached only because prose is
  extracted.
- Spec-faithful ceiling on the same range: **cited=8** (0 backtick characters
  across all 23 messages, 10,369 bytes — `grep -c` independent re-check;
  exactly 8 `.log` tokens, in 45b2713/6ce41aa/5f7ecce), misses 0 lenient / 2
  strict-unique (both on 45b2713). Frozen probe leg 4 demands cited ≥ 20.
- Dedupe micro-case: same path cited twice → cited=1 (spec silent; reasonable).
- Usage `--bogus` → exit 2 ✓. `--selftest` → `MSG_TREE_SELFTEST=pass` exit 0 ✓.
- Frozen counter, my own run: `CAP_PRESENT=1 CAP_SELFTEST=pass
  CAP_PLANTED_MISS=pass clean_exit=0 dirty_exit=1 CAP_REAL=pass commits=23
  cited=25 misses=9 exit=1` → **CAP_MESSAGE_TREE=pass, PROBE_EXIT=0**.

## Reading of the disagreements

- Cases b–h and the probe's own legs 1–3 are honestly earned: the instrument's
  core mechanics (own-tree basis, planted-miss kill, path:line / `./` / comma
  normalisation, directory citations, command exclusion, merge handling,
  dedupe, honest selftest, usage exit 2) all check out. It is not a stub.
- The disagreements concentrate in two declared-in-docstring choices that the
  frozen claims.md §C2 does not licence:
  1. whole-message token extraction (backticks are delimiters, not a scope) —
     case a and R1/R2/R3/R4/R5 cited-composition side;
  2. uniqueness-gated bare-suffix resolution (≥2 same-named in-tree files ⇒
     miss) — R2/R3/R4 miss side.
- The frozen probe cannot see either choice: its fixtures cite backticked
  tokens where both semantics coincide, and its leg-4 threshold (M ≥ 20) is
  unsatisfiable under the frozen spec on this history (ceiling 8). A pass
  therefore *implies* the deviation — the threshold structurally rewards it.
