SURVIVED — prose overclaim and deleted embedded output line pass both registered pre-gate detectors.

# R71W1EntryMutants

## Frozen scope and baseline

Read `reports/round-71/claims.md` and `reports/round-71/pre-registration.txt` before probing. Scratch corpus only; no lane source changed. Fixture: `/fast/scratch/hyaku/revenger-r71/R71W1EntryMutants/corpus`.

Baseline command (run from scratch root):
`python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-71-apk-axml-byte-evidence.md`
Output: `checked_blocks=24 problems=0`; exit 0.

Baseline lint command:
`python3 -B corpus/lint_entry.py --entry corpus/knowledge/round-71-apk-axml-byte-evidence.md --lane /home/vgpnk/Projects/shokunin/revenger-shokunin`
Output: `LINT_QMAP=0`, `LINT_Q14=0`, `LINT_Q15=0`, `LINT_HEADER=0`; exit 0.

## Mutations and outcomes

1. **Q04 prose overclaim** — scratch entry line 302 replaced its calibrated wording with “the checker verifies that the archive parser implements the full Android ZIP specification.” The registered gate remained `checked_blocks=24 problems=0` (exit 0); lint remained all zero (exit 0). **Survived**: neither tool evaluates prose truth or claim scope. This is a coverage finding, not a contract change.

2. **Remove Q16 row** — deleted the Q16 row from the scratch entry’s §Q-map. Gate remained clean (24/0, exit 0); lint printed `LINT_QMAP=1 ['Q16']` and other classes 0 (exit 1). **Killed by lint**.

3. **Delete an embedded output line** — removed the archive JSON line at scratch entry line 28 while retaining its command fence. Gate still reported `checked_blocks=24 problems=0` (exit 0); lint remained all zero (exit 0). **Survived**: the registered gate verifies embedded-line inclusion in stdout, not stdout completeness. This matches Q13’s expressly named limitation.

The prescribed falsely-claim-locator-compared and alternate in-tree echo-script attacks were not executed; no verdict is asserted for those mutants.

## Restoration evidence

Pristine source entry before probe SHA-256: `778af93bac4cca16f8ad38e2af3cb4fd984a2054c65ad4dcba513f1f392ea3bf`.
Restored scratch entry SHA-256: `778af93bac4cca16f8ad38e2af3cb4fd984a2054c65ad4dcba513f1f392ea3bf`; `cmp -s` against lane entry returned exit 0. Every mutation was confined to scratch. Scratch was removed after preserving this report.

Report: `.ufo/waves/round-71/w1/R71W1EntryMutants.md`
