# round-83 interface-builder producer run — evidence ledger

- **Trigger**: round-83 C1 (coverage, criterion A1 completion) — the
  rea 6.8.0 `rea-artifact-graph` provider reports `decode_interface_builder`
  `available: true` on this host (S462, group re-probed 2026-11-01); the
  operation is the third and last unrecorded operation of the r81-recorded
  `artifact-graph` family; an authored inert two-document `.app` bundle
  makes the operation's first real record manufacturable.
- **Action**: one bounded run, cwd = lane root:
  `rea decode-interface-builder corpus/fixtures/app-r83/R83Sample.app
  --format json` (exact stdout saved as `inspection.json`, 9012 bytes,
  sha256 `28abc85e44d1c816756585cc1ad337a5dd709d18a8cd42fbae93de982f16e1fb`;
  exit 0; stderr 0 bytes; `receipt.json`).
- **Outcome**: Evidence `ev_260481425d1a43fbbc0327c2033aafda8d7a51599c520a74b9985c3c550610f8`
  (form `ev_<64hex>`), operation `decode_interface_builder`, provider
  `rea-artifact-graph`; `ORACLE OK (44/44 checks)` — the 26 byte-derived
  checks compare the record against facts derived from the built fixture
  bytes and the authored tree by `build_app.py` (18/18 self-checks, regen
  byte-identical), never from the record (Q06); the 18 HYP checks are the
  pre-registered Q07 hypotheses about the producer's declared Interface
  Builder vocabulary, frozen in `truth.json` BEFORE the committed run
  (from `reports/round-83/preprobe-app-shape.log` + the installed parser
  source), recorded as predicted (subject/target identity null, node/edge
  counts and relations, coverage facet statuses, truncated flag,
  confidence/authority).
- **Pointer**: `corpus/live/runs/round-83/{inspection.json, receipt.json,
  LEDGER.md, stderr.txt}`; fixture `corpus/fixtures/app-r83/`;
  oracle + regen re-run over `git archive` bytes at adjudication.

## Q10 scope note

One authored inert `.app` bundle (root-layout `Info.plist` 313 bytes +
two typed-NIBArchive documents, 213 + 79 bytes) and the directory layout
around them; the producer's own profile reads the decoded serialized
object graphs of that snapshot only. No general app-bundle claim, no
storyboard claim (no `.storyboardc` surface authored), no claim that any
UI framework class was instantiated or any code executed (nothing is
executed; the parsed class names are inert serialized strings). The
producer's facet semantics — `hierarchy: unsupported` for nib documents,
`connections`/`objects`/`classes` complete for the authored content, the
connection resolved as one `target_action` chain — are recorded as
observed, not explained (Q07: a cause only after independent
reproduction). The android family stays unrecorded.

## Admission status

Candidate record for round-83 C1; admission is the round's own VERIFY
conditions (claims.md) plus the non-author closure. This file records the
run; it does not self-admit.
