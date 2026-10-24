# R64ScoutFixtureBytes — findings

Axes: census completeness; digest-to-ledger agreement; evidence preservation.

## Observed (high confidence)

- Independently inventoried and SHA-256 hashed all **9 files** under `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/` (3) and `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/` (6).
- **8 files match their recorded ledger digests; 0 conflicting digests.** Full-digest searches and file-specific attribution use `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/LEDGER.md:15-28`.
- **1 unrecorded file:** `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/LEDGER.md` itself. Its computed SHA-256 is `25a4a18b76a2a55f3b7ea397ee23bba948be3f1c1a3e13a3194c0f057bb1e1a6`; searching that exact digest in the ledger returned no match.
- The checker digest currently matches line 28 despite that line's historical/non-pinned qualification. The receipt matches the corrected pin at line 26, ending `5c6b94d`.

Full nine-row table, exercised commands, and scope limits: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/scout-fixture-bytes.md`.

## Inference and unknowns

[INFERENCE] Absence of the ledger's self-digest alone is not evidence of payload drift. This is a point-in-time working-tree census, not a committed-archive comparison or authenticity/semantic validation. No dependency blocked the assignment; later concurrent changes remain outside the observation. No exported symbol contract was investigated, so LSP tracing was not applicable.

## Bounds

No existing source/evidence files were changed; only the two assigned report files were written. No git/jj operations, builds, tests, verifier executions, or scratch files. Tool installations/updates: none.

Report: .ufo/waves/round-64/R64ScoutFixtureBytes.md
