# ExecFrozen — revenger r94 w1 — do-nothing rerun, freeze-tip digest, registry pin

Seat: ExecFrozen (executor). Scope: run-only verification of the frozen C1 v3 counter at
two pinned revs plus the wave-registry pre-check. No lane file edited; no git/jj command
run; scratch deleted on exit.

## 1. Do-nothing rerun at base rev 9876cb38c5415fbc86336a26a68e05680c397fd5

Command: `PYTHONUTF8=1 python3 -B reports/round-94/c1_k_admit_counter3.py --rev 9876cb38c5415fbc86336a26a68e05680c397fd5`

- Exit code: 1 (required: nonzero).
- `C1_C15_HELD=fail` (required) and `C1_VERDICT=fail` (required).
- Receipt: `.ufo/waves/round-94/w1/ExecFrozen/do-nothing-rerun.log`.
- Fidelity check: my captured output is byte-for-byte identical to the frozen control
  receipt `reports/round-94/controls/c1v3-do-nothing.log`, including the same votes-digest
  `f97c0345cfa50e4fdca10f0329ed84dabac7d303f7a97ae9a923169936c0905c` and leg set
  (ROWS_TOTAL pass / C15_HELD fail / ONLY_C15 fail / ADMITTED fail / VOTES fail / LINT
  fail / SOURCES fail / QUOTES fail / K_HELD_BACKED fail).

## 2. Freeze-tip run at rev 060a8e87d6de6b31f91b58524ab0fcad88ae5431

Command: `PYTHONUTF8=1 python3 -B reports/round-94/c1_k_admit_counter3.py --rev 060a8e87d6de6b31f91b58524ab0fcad88ae5431`

- Exit code: 1; `C1_C15_HELD=fail` (C15 still uncovered at the freeze tip, as required) and
  `C1_VERDICT=fail`.
- The `C1_VOTES` line prints the vote-binding digest as required:
  `C1_VOTES=votes dir missing digest=01d51059fb29a5184342b2815e643695aa269b384c04d005f69556816f291bd3`
- **Candidate digest every wave vote must bind: `01d51059fb29a5184342b2815e643695aa269b384c04d005f69556816f291bd3`**
  (64 hex, sha256 over the entry bytes with every `admission-status:` line normalized to
  `admission-status: candidate`, per the counter's normalization).
- Full stdout saved to `.ufo/waves/round-94/w1/ExecFrozen/freeze-state-digest.txt`.
- At this rev `C1_LINT` passes (base rev: fail) because the freeze tip carries the
  re-grounded r72 entry with S498/S499 cited; `C1_SOURCES`/`C1_QUOTES` still fail there on
  the unlanded receipt rows (expected pre-landing state).

## 3. Registry pre-check (PINNED_SEATS vs live wave registry)

Extracted by importing `reports/round-94/c1_k_admit_counter3.py` as a module in scratch
(importlib, no lane mutation). Receipt: `.ufo/waves/round-94/w1/ExecFrozen/registry-pin.txt`.

- Module `PINNED_SEATS` (13 entries) — ScoutReopen/ScoutErrata=scout, ScribeLesson=scribe,
  ExecReceipts/ExecBattery/ExecCensus/ExecFrozen=executor, ReviewerGate/ReviewerBlind=reviewer,
  CriticR94=critic, MutationR94=mutation-tester, ConnectorOverlap=connector,
  SentinelScope=sentinel. `VOTE_ROLES=('reviewer','critic')`.
  Module `FREEZE_REV=9876cb38c5415fbc86336a26a68e05680c397fd5` (matches the claims base).
- Live registry `.ufo/waves/round-94/w1/swarm-registry.json` (revenger-r94-w1): all 13
  pinned names present, each role exactly equal to the pin. **Exact match, 13/13.**

## Retained evidence

- `.ufo/waves/round-94/w1/ExecFrozen/do-nothing-rerun.log`
- `.ufo/waves/round-94/w1/ExecFrozen/freeze-state-digest.txt`
- `.ufo/waves/round-94/w1/ExecFrozen/registry-pin.txt`

## Risks / notes

- None observed. Both counter runs failed exactly as the frozen kill rules require; the
  do-nothing receipt reproduces the frozen control byte-for-byte; the digest that votes
  bind is the freeze-tip value `01d51059…91bd3`, distinct from the base-rev value
  `f97c0345…9905c` (the entry gains S498/S499 cites at the freeze tip).
- Scratch `/fast/scratch/hyaku/revenger-r94/ExecFrozen` removed before yield; nothing
  installed; no network used.
