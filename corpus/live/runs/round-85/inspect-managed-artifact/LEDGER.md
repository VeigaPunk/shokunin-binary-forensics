# round-85 managed-artifact producer run — evidence ledger

- **Trigger**: round-85 C1 (coverage, criterion M registration). The r76
  `inspect_managed_artifact` record (`corpus/live/runs/round-76/`) is real
  but predates the oracle-receipt gate — its receipt carries no `oracle`
  field, so under criterion M's registered definition (A1v2's
  oracle-checked-record gate, unchanged) the operation counts UNRECORDED
  on the round base: the red instrument prints `M_RECORDED=0/3`
  (`mg-red.log`), not 1/3. This run refreshes the operation with a real
  oracle-checked record on the same authored fixture as the other two
  records, so all three operations carry same-round, oracle-checked
  evidence.
- **Action**: one bounded run, cwd = lane root:
  `rea inspect-managed-artifact corpus/fixtures/managed-r85/fixture.dll
  --format json` (exact stdout saved as `inspection.json`, 3190 bytes,
  sha256 in `receipt.json`; exit 0; stderr 0 bytes; `receipt.json`).
- **Outcome**: Evidence
  `ev_0eea92d75cd2bb0d69be542825a96f9f2a98ea359ffdf607fd7cb910dbf796e2`
  (form `ev_<64hex>`), operation `inspect_managed_artifact`, provider
  `rea-dotnet-static`; `ORACLE OK (20/20 checks)` — BYTE checks
  re-derive subject sha == fixture sha, byte length 1048, metadata
  table row counts, module MVID from the #GUID bytes, assembly
  name/version, and the classification evidence rows' file offsets
  (512 = the COR20 header start, 528 = the CLI flags field — both
  re-derived from the image layout); HYP checks are the pre-registered
  Q07 hypotheses (classification `managed`/`cil`/`anycpu`, stream
  names, coverage `complete`), recorded as predicted.
- **Pointer**: `corpus/live/runs/round-85/inspect-managed-artifact/
  {inspection.json, receipt.json, LEDGER.md, oracle.log, stderr.txt}`;
  fixture `corpus/fixtures/managed-r85/`; oracle + regen re-run over
  `git archive` bytes at adjudication.

## Q10 scope note

Same authored inert 1048-byte IL-only PE/CLI image as the sibling
records (one fixture, three bounded static runs — the artifact
operation is the identity/PE surface of the same provider). The record
demonstrates the built-in provider's static PE/CLI classification of
this one authored image; the provider's own limitation (nothing loaded,
no dependency resolution, no decompilation) is recorded as observed.
The r76 record remains in place untouched as historical evidence; this
run does not re-grade it (no in-place rewrite of r76 evidence).

## Admission status

Candidate record for round-85 C1; admission is the round's own VERIFY
conditions (claims.md) plus the non-author closure. This file records
the run; it does not self-admit.
