# round-85 managed-members producer run — evidence ledger

- **Trigger**: round-85 C1 (coverage, criterion M registration) — the
  rea 6.8.0 `rea-dotnet-static` provider reports `inspect_managed_members`
  `available: true` on this host (S469, probed 2026-11-02); the operation
  has NO saved record anywhere under `corpus/live/runs/` through r84
  ("available-but-unrecorded", the r81/r82 scorecard class). An authored
  inert managed PE/CLI image with a real method body makes the operation's
  first real record manufacturable.
- **Action**: one bounded run, cwd = lane root:
  `rea inspect-managed-members corpus/fixtures/managed-r85/fixture.dll
  --format json` (exact stdout saved as `inspection.json`, 6974 bytes,
  sha256 in `receipt.json`; exit 0; stderr 0 bytes; `receipt.json`).
- **Outcome**: Evidence
  `ev_e5d7a0b9864b61a963b76848fb927fdbbbba6333c85602dcefbfe6c58ae359f4`
  (form `ev_<64hex>`), operation `inspect_managed_members`, provider
  `rea-dotnet-static`; `ORACLE OK (47/47 checks)` — the BYTE checks
  compare the record against facts re-derived from the built fixture
  bytes by the oracle's own independent CLI-image parser (PE headers →
  COR20 → metadata root → streams → #~ rows → heaps), never from the
  record or the generator (Q03/Q06): subject sha == fixture sha, method
  row file offset 834, RVA 4624, body file offset 1040, il_size 6,
  il_sha256 over the built bytes, ldstr anchor token 0x70000001, blob
  signature entry length 3 and its sha over the built bytes, #US entry
  decode "Fixture Hello" at file offset 981, module MVID rendered from
  the #GUID bytes, table row counts {Module 1, TypeDef 2, MethodDef 2,
  ModuleRef 1, ImplMap 1, Assembly 1}. The HYP checks are the
  pre-registered Q07 hypotheses frozen in `truth.json` BEFORE the
  committed run, recorded as predicted (body `tiny`/`present`, opcode
  counts ldstr=1 ret=1, signature parse `decoded` return `string`
  params 0 conv `default`, us state `complete` with empty issues,
  coverage `complete`, confidence `observed`, authority
  `shipped-artifact`). Negative control demonstrated pre-run
  (`preprobe-managed-shape.log`): one mutated field flips the oracle to
  FAILED.
- **Pointer**: `corpus/live/runs/round-85/inspect-managed-members/
  {inspection.json, receipt.json, LEDGER.md, oracle.log, stderr.txt}`;
  fixture `corpus/fixtures/managed-r85/`; oracle + regen re-run over
  `git archive` bytes at adjudication.

## Q10 scope note

One authored inert 1048-byte IL-only PE/CLI image (two MethodDef rows,
one with a 7-byte tiny-header IL body `ldstr 0x70000001; ret`, one
P/Invoke declaration; six metadata tables; #US with one literal) and the
metadata structures the producer reads. The record demonstrates the
built-in provider's static metadata decode of this one authored image;
no general managed-format claim, no claim about .NET runtime behavior
(nothing is loaded or executed — the provider's own limitation lines
state this and are recorded as observed). Producer-internal conventions
(GUID rendering, signature decode vocabulary, body interpretation
fields) are pre-registered hypotheses recorded whichever way they fell
(Q07); the observed values are recorded, not explained.

## Admission status

Candidate record for round-85 C1; admission is the round's own VERIFY
conditions (claims.md) plus the non-author closure. This file records
the run; it does not self-admit.
