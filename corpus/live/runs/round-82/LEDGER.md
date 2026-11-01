# round-82 dylib-resolution producer run — evidence ledger

- **Trigger**: round-82 C1 (coverage, criterion A1 registration) — the
  rea 6.8.0 `rea-artifact-graph` provider reports `trace_dylib_resolution`
  `available: true` on this host (S459, group re-probed 2026-11-01); the
  operation sits in the r81-recorded `artifact-graph` family but is
  unrecorded; an authored inert two-image Mach-O tree makes the operation's
  first real record manufacturable.
- **Action**: one bounded run, cwd = lane root:
  `rea trace-dylib-resolution corpus/fixtures/macho-r82/image/main.dylib
  --format json` (exact stdout saved as `inspection.json`, 7364 bytes,
  sha256 `05142d7e1d4e4ca38482071bca7015c6e38de5b021f59304b3070649aae6e786`;
  exit 0; stderr 0 bytes; `receipt.json`).
- **Outcome**: Evidence `ev_851a74058ef2973352f214efbf3798b96f98de3d87a3d1e9340fb3ddc04d514a`
  (form `ev_<64hex>`), operation `trace_dylib_resolution`, provider
  `rea-artifact-graph`; `ORACLE OK (47/47 checks)` — the 37 byte-derived
  checks compare the record against facts derived from the built fixture
  bytes and the authored tree by `generator.py` (15/15 self-checks, regen
  byte-identical), never from the record (Q06); the 10 HYP checks are the
  pre-registered Q07 hypotheses about the producer's declared dyld
  vocabulary, recorded as predicted (outcome/resolution/coverage/
  confidence/authority).
- **Pointer**: `corpus/live/runs/round-82/{inspection.json, receipt.json,
  LEDGER.md, stderr.txt}`; fixture `corpus/fixtures/macho-r82/`;
  oracle + regen re-run over `git archive` bytes at adjudication.

## Q10 scope note

Two authored inert Mach-O images (304 + 80 bytes) and the tree layout
around them; the producer's own profile reads dyld load-path resolution
candidates and parse state of that snapshot only. No general Mach-O claim,
no app-bundle claim, no claim that any dyld ever loaded anything (nothing
is executed; the record's own limitation list names the unmodeled dyld
behaviors, and the producer's `coverage: partial` semantics are recorded
as observed, not explained — Q07: a cause only after independent
reproduction). `decode_interface_builder` and the android family stay
unrecorded.

## Admission status

Candidate record for round-82 C1; admission is the round's own VERIFY
conditions (claims.md) plus the non-author closure. This file records the
run; it does not self-admit.
