# Round-71 post-freeze corrections (recorded, not hidden)

The claims file remains byte-identical to the pre-registration SHA `1febae1279fdeca323f5e8beffeb0a8ac2f26256158f7000bb0b2eff8321c3f5`. The following supporting-evidence changes landed after W2 topology freeze `c6e284c6583fa3502754361f411b66646880ba02`; they do not alter C1/C2 targets, predicates or vote assignments.

## `a16e6cbe24c51e6952e973d6b47560b49311420` — source/lesson cross-reference correction

This commit modified only `corpus/SOURCES.md` and `corpus/lessons/round-71.md`, after the W2 `.ready` file was dispatched. It records S052 `used-by` from `corpus/knowledge/round-71-apk-axml-byte-evidence.md` to that entry plus `corpus/lessons/round-71.md`; changes S053 `used-by` from `—` to the lesson path; and corrects S053 `format-layout` to `format/layout`. The need is CORPUS.md's `used-by` path semantics and the lesson's source Gate; the before→after cells are logged in the lesson. This was a documentation/provenance correction, not a predicate/measurement change. W2 seats whose source/lesson observations cite the earlier `c6e284` bytes must be read as scoped to that earlier snapshot, not the final row values; the final source registry is re-censused at exit 0.

## Pre-freeze route-pin correction (build commit `18200a4b18e8dfce291a74028a9012ce4401ca10`)

`git show b7abcd875c84f4e1d6c8df966b6bd20f4154c53f:PROVINCE.md` line 19 contained `rea-agents@6.4.0`; the build commit updates it to `6.5.0`, consistent with S049's pinned 6.5.0 reference and the round-63–70 records. W1 `R71W1ProvincePin.md` read only the post-fix tree and therefore does not establish the before/after; the source-based reason and commit are recorded here. No readiness claim is made.

## A3 vote-input hardening

`reports/round-71/measure-amendment-A3.md` records the symlink and unhashable-seat defects identified by W2 Sentinel and the strict counter correction. The final counter hash and regression receipts are recorded there and in the post-A3 measure-before receipt. This is a fail-closed enforcement of the existing per-seat committed-file predicate, not a changed target. W2 reports that exercised the pre-A3 counter must be interpreted as a pre-amendment parser probe; the final C1 measurement uses A3.
