# round-84 artifact-inspection producer run — evidence ledger

- **Trigger**: round-84 C1 (coverage, criterion A1v2 registration) — the
  rea 6.8.0 `rea-artifact-graph` provider reports `inspect_artifact`
  `available: true` on this host (S466, group re-probed 2026-11-02); the
  operation is one of the two archive-side operations the r81/r82
  scorecards name "available-but-unrecorded"; an authored inert zip
  archive makes the operation's first real record manufacturable.
- **Action**: one bounded run, cwd = lane root:
  `rea inspect-artifact corpus/fixtures/arc-r84/R84Sample.zip
  --format json` (exact stdout saved as `inspection.json`, 9481 bytes,
  sha256 in `receipt.json`; exit 0; stderr 0 bytes; `receipt.json`).
- **Outcome**: Evidence `ev_753cfca9daf92857826b62400bd2f4b09ba6cbb4670fd449e3250c246ca138ba`
  (form `ev_<64hex>`), operation `inspect_artifact`, provider
  `rea-artifact-graph`; `ORACLE OK (36/36 checks)` — the byte-derived
  checks compare the record against facts re-derived from the built
  fixture bytes by `build_zip.py` (17/17 self-checks, regen
  byte-identical) and the stdlib reader inside `oracle_check.py`, never
  from the record (Q06/Q03); the HYP checks are the pre-registered Q07
  hypotheses about the producer's declared inventory vocabulary, frozen
  in `truth.json` BEFORE the committed run (from
  `reports/round-84/preprobe-arc-shape.log`), recorded as predicted
  (root node `materialized`/zip with size == fixture size, entry nodes
  `embedded`, node/edge/occurrence counts = entries+1 / entries /
  entries+1, substep operation `inventory_artifact` completed, coverage
  `complete-within-substeps`, authority `shipped-artifact`, predicate
  `rea.analysis`, confidence `observed`, contradictions empty).
- **Pointer**: `corpus/live/runs/round-84/inspect-artifact/
  {inspection.json, receipt.json, LEDGER.md, oracle.log, stderr.txt}`;
  fixture `corpus/fixtures/arc-r84/`; oracle + regen re-run over
  `git archive` bytes at adjudication.

## Q10 scope note

One authored inert 508-byte ZIP_STORED archive (three stored entries:
`MANIFEST.txt` 90 bytes, `data/blob.bin` 48 bytes,
`data/nested/note.md` 32 bytes) and the central-directory structure the
producer reads. The inventory lists central-directory entries only (the
producer's own limitation line, recorded as observed). No general
archive-format claim, no claim about non-entry bytes (the limitation
names them explicitly), and nothing is executed by this lane or by the
producer (the inventory read is static; the extraction sibling record
writes only under the host temp area). The producer's facet semantics —
`content_state` embedded/materialized, `media_type`/`architecture`
nulls — are recorded as observed, not explained (Q07).

## Admission status

Candidate record for round-84 C1; admission is the round's own VERIFY
conditions (claims.md) plus the non-author closure. This file records
the run; it does not self-admit.
