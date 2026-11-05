# MutationR96 — scoped findings (round 96, wave 1)

Role: mutation-tester. Item: mutate the v5 counter
(`reports/round-96/c1_k_admit_counter5.py`, frozen `805ffb8a…a23ad19`); each mutant must
die on the frozen self-test. Full per-mutant record (exact edits, receipts, hashes):
`.ufo/waves/round-96/w1/MutationR96/mutants.md`. Detector: the counter's own frozen
harness (`--self-test --receipts-dir`), baseline first.

## Baseline

Pristine committed counter, run in place: `SELFTEST_C1V5=pass legs=33`, rc 0 — equal to
the frozen control `controls/selftest-c1v5.log`. All verdicts conclusive.

## Verdicts (run form: `PYTHONUTF8=1 HYAKU_SCRATCH=<scratch> python3 -B <mutant> --self-test --receipts-dir <scratch>/receipts-<tag>`)

| mutant | weakened point | rc | verdict | killing delta (expected_leg) |
|---|---|---|---|---|
| a-union | `C1_ADMITTED_UNION` → constant True | 1 | KILLED | `A4-shadow-admitted` (`C1_ADMITTED_UNION`) |
| b-usedby | used-by exclusivity in `check_sources` | 1 | KILLED | `A3-usedby-extra` (`C1_SOURCES`) |
| c-pycache | `C1_PYCACHE` scan narrowed to the exact v4 dir set | 1 | KILLED | `M8-pycache-frozen-dir` (`C1_PYCACHE`) |
| d-host | `C1_RECEIPTS` host allowlist accepts any host | 0 | **SURVIVED — finding** | none |
| e-heldback | `C1_K_HELD_BACKED` → constant True | 1 | KILLED | `KHELDBACK-broken-cell` (`C1_K_HELD_BACKED`) |

The three r95-routed closes carried as legs (A4 union, A3 used-by, M8 widened pycache)
are each singly discriminating: dropping exactly that behavior makes its frozen delta
pass outright (rc 0, `failing_legs=[]`), which the harness rejects. Mutant-e dies
through the harness's expected-leg strictness (the KHELDBACK delta still exits 1 via
`C1_ONLY_C02`, but not on `C1_K_HELD_BACKED`).

## Finding — mutant-d SURVIVES (coverage, sub-check level)

With the host allowlist sub-check removed, the self-test still passes 33/33: every
frozen receipts delta (`V10`, `V27`) fails on `C1_RECEIPTS` for reasons other than the
host. Concretely, V27's self-consistent fabrication is caught by the fetch-log sha
cross-check (`S502:fetch-log-line-missing`), not the allowlist. So no frozen delta
independently discriminates the host-allowlist sub-check; a receipt forged
end-to-end (fabricated body + matching receipt + matching fetch-log line) under a
non-allowlisted host would pass the whole leg today.

- Does not falsify the frozen predicates: leg-level coverage (the claims' accounting)
  is intact; `V4_SELFTEST_UNCOVERED`/`DELTA_RECEIPTS=31/31` are per leg and `C1_RECEIPTS`
  keeps two discriminating deltas.
- Routable to r97 per the kill rule (survivors are findings, never counter edits):
  vector design "self-consistent receipt+body+fetch-log line under a foreign host" —
  only the allowlist sub-check would fail it.
- Reported, not fixed; no frozen byte was touched.

## Restoration evidence

- Lane bytes before == after: counter `805ffb8a…a23ad19`, entry `2f7d4c1b…6d923`,
  claims `89fa1281…9a7a98`; all byte-equal to freeze commit `ff767436…e69a`
  (`git show … | sha256sum`); `git status --porcelain` over the three paths: empty.
- Mutants ran only on scratch copies (`/fast/scratch/hyaku/revenger-r96/MutationR96/`,
  deleted after evidence copy); no `__pycache__`/`*.pyc` in any audited surface (0
  hits); every invocation `python3 -B`.
- Candidate digest re-derived from the lane root at session start:
  `2f7d4c1b754d812102563869b511a746c7c49750d8cc42859b2a6466d776d923` — equals the
  frozen vote-binding digest.

## Artifacts

- `.ufo/waves/round-96/w1/MutationR96/mutants.md` — per-mutant exact edits, rc, killing
  deltas, analysis, restoration hashes.
- `.ufo/waves/round-96/w1/MutationR96/receipts-{pristine,a-union,b-usedby,c-pycache,d-host,e-heldback}/<delta>.json`
  — 31 per-delta receipts per run (6 × 31).
- `.ufo/waves/round-96/w1/MutationR96/mutant-{a-union,b-usedby,c-pycache,d-host,e-heldback}.py`
  — the exact mutant bytes as run.
