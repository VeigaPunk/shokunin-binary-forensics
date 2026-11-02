# round-84 artifact-extraction producer run — evidence ledger

- **Trigger**: round-84 C1 (coverage, criterion A1v2 registration) — the
  rea 6.8.0 `rea-artifact-graph` provider reports `extract_artifact`
  `available: true` on this host (S466, group re-probed 2026-11-02); the
  operation is the second archive-side operation the r81/r82 scorecards
  name "available-but-unrecorded"; the same authored inert zip archive
  makes the operation's first real record manufacturable.
- **Action**: one bounded run, cwd = lane root:
  `rea extract-artifact corpus/fixtures/arc-r84/R84Sample.zip
  --format json` (exact stdout saved as `inspection.json`, 3930 bytes,
  sha256 in `receipt.json`; exit 0; stderr 0 bytes; `receipt.json`).
  The producer's declared effects (`launches_process`,
  `may_write_filesystem`) are its own extraction output under the host
  temp area (`output_root`); nothing is written inside the lane repo and
  nothing from the archive is executed.
- **Outcome**: Evidence `ev_07e34a9493848c91095a3355069907df24449999088c87a558b45f8d33c77467`
  (form `ev_<64hex>`), operation `extract_artifact`, provider
  `rea-artifact-graph`; `ORACLE OK (31/31 checks)` — the byte-derived
  checks compare the record against facts re-derived from the built
  fixture bytes (per-entry `relative_path`/`sha256`/`bytes_written`,
  `manifest.root_sha256` == fixture sha, root format zip, `created`
  true, output root outside the fixture directory), never from the
  record (Q06/Q03); the HYP checks are the pre-registered Q07
  hypotheses frozen in `truth.json` BEFORE the committed run (from
  `reports/round-84/preprobe-arc-shape.log`), recorded as predicted
  (node/edge counts = entries+1 / entries, `containment_verified` true,
  `integrity_contradictions` empty, cleanup
  `{attempted: false, verified: true, residual_paths: []}`, coverage
  `container-entries`/`complete`, authority `shipped-artifact`,
  id forms `ev_`/`aex_`/`agm_` hex64).
- **Pointer**: `corpus/live/runs/round-84/extract-artifact/
  {inspection.json, receipt.json, LEDGER.md, oracle.log, stderr.txt}`;
  fixture `corpus/fixtures/arc-r84/`; oracle + regen re-run over
  `git archive` bytes at adjudication.

## Q10 scope note

The same authored inert 508-byte ZIP_STORED archive as the sibling
inspection record (three stored entries). The extraction record
demonstrates the producer's regular-contents extraction of that one
archive into a host-temp directory (DMG extraction is unavailable per
the provider's own declared surface; PKG remains root-hash-only per the
shared limitations — neither surface is claimed). No general
archive-format claim, no nested-container claim (the shared limitation
records that other nested containers are only "recorded"), nothing
executed. The producer's cleanup/containment semantics are recorded as
observed, not explained (Q07).

## Admission status

Candidate record for round-84 C1; admission is the round's own VERIFY
conditions (claims.md) plus the non-author closure. This file records
the run; it does not self-admit.
