# Round-71 counter amendment A1 — timeout fixture path only

Date: 2026-10-27, before any wave-2 seat scores. This is a harness correction, not a predicate, target, kill-rule or C1 vote-source change.

- Frozen claim bytes remain the pre-registration copy: SHA-256 `1febae1279fdeca323f5e8beffeb0a8ac2f26256158f7000bb0b2eff8321c3f5`.
- Counter bytes measured after this correction: SHA-256 `fbd81050930657375f7314123ef468e66337b69adee12ce8416bb5dc98cff8f5` (`sha256sum reports/round-71/measure.py`).
- Only source delta from frozen counter `d0d59b79652dae9d65796493f703470dc4d4998ec607cb25a41aed939f38d06c`: the timeout probe entry's command changes from `$ python3 -B sleeper_r71.py` to `$ python3 -B corpus/sleeper_r71.py`. The probe writes the sleeper under `TREE/corpus/`; with the old relative path the gate ran from `TREE` and returned drift (`command exited 2`) before reaching the timeout. Sentinel `R71W1Sentinel` reproduced that defect in `.ufo/waves/round-71/w1/R71W1Sentinel.md` §F1.
- Frozen predicate remains `C2_TIMEOUT_EXIT2=1/1` only when the declared command actually reaches the gate's production 120-second timeout and exits 2 with the registered text/no traceback. C1 still binds four unique per-seat JSON vote files in `.ufo/waves/round-71/w2-votes/`; the counter continues to require exact assigned-Q sets and `path.stem == seat`.
- Counter red-before is re-run against base `b7abcd875c84f4e1d6c8df966b6bd20f4154c53f` and replaces the prior receipt before any wave-2 scoring. The target remains red on base; C1 and C2 predicates/kill rules are unchanged.
## Corrected red-before receipt

The re-run is `reports/round-71/measure-before.log` at counter SHA `fbd81050930657375f7314123ef468e66337b69adee12ce8416bb5dc98cff8f5`, measured on the base tree hash in `pre-registration.txt`. Exit 0; C1 no (`K_HELD_BACKED=8/14`, zero vote files), C2 no (`C2_MISSING_ENTRY_EXIT2=0/1`, `C2_TIMEOUT_EXIT2=0/1`, both traceback=yes), `HOLD_REPLAY=10/10`, `HOLDS_OK_V8=yes`. All ten individual `HOLD` lines remain in the receipt.
`git show HEAD:reports/round-71/measure-before.log | diff -u - reports/round-71/measure-before.log` shows exactly one changed cell: `C2_TIMEOUT_EXIT2` retains 0/1 and rc=1, while `stderr_traceback` changes `no → yes`; all other labels, including C1, `HOLDS_C2_V1=no`, and the ten HOLD lines, are unchanged.