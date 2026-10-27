INCONCLUSIVE — pristine gate baseline failed before mutation, so no mutant can be classified as killed or surviving.

Candidate: `4c1eeaee88fd07e442f1bd546faf77be3957d390`. Scratch TREE was made with `git archive` into `/fast/scratch/hyaku/revenger-r71/R71W2EntryMutants/pristine` (35 MiB); candidate entry SHA-256 `671f55fceb64af27f99c00106f58f9bc2c8b5dc9af6028382ff218655008f092`, equal to the extracted entry bytes.

Expected detector: run embedded-output gate and Q-map lint on pristine, mutated, restored bytes; run counter on the same trees. Planned targets were Q04/Q16 prose, an embedded cited output line, the Q16 row, an Observation locator, and the forged-block/alternate in-tree echo-script case.

Actual baseline commands/output:

```text
python3 -B $TREE/corpus/check_embedded_outputs.py --entry $TREE/corpus/knowledge/round-71-apk-axml-byte-evidence.md
GATE_RC=1
checked_blocks=0 problems=24
```

The gate output reported all 24 embedded commands as `command exited 2`, including entry:27 `python3 -B corpus/fixtures/apk-r65/readout.py --fact archive`; entry:144 `entry_checks.py --spec-quotes`; and entry:254 `entry_checks.py --axml-layout`. Directly running the first command from `$TREE` succeeded (JSON stdout with archive digest; RC=0), so the discrepancy is in the gate invocation/environment and the pristine detector is inconclusive. The `set -e` baseline sequence stopped at the failing gate; lint and counter were not run. No mutation was applied; there are no killed/survived claims.

Restoration evidence: pristine entry hash remains `671f55fceb64af27f99c00106f58f9bc2c8b5dc9af6028382ff218655008f092`; untouched pristine tree retained until cleanup. Removed `/fast/scratch/hyaku/revenger-r71/R71W2EntryMutants` after capturing this report. Lane source, candidate, and vote files were not edited.

Report: `.ufo/waves/round-71/w2/R71W2EntryMutants.md`