# round-85 managed-native-boundaries producer run — evidence ledger

- **Trigger**: round-85 C1 (coverage, criterion M registration) — the
  rea 6.8.0 `rea-dotnet-static` provider reports
  `inspect_managed_native_boundaries` `available: true` on this host
  (S469, probed 2026-11-02); the operation has NO saved record anywhere
  under `corpus/live/runs/` through r84 ("available-but-unrecorded").
  The authored fixture's ImplMap row (P/Invoke declaration) gives the
  operation a real boundary to report.
- **Action**: one bounded run, cwd = lane root:
  `rea inspect-managed-native-boundaries
  corpus/fixtures/managed-r85/fixture.dll --format json` (exact stdout
  saved as `inspection.json`, 3982 bytes, sha256 in `receipt.json`;
  exit 0; stderr 0 bytes; `receipt.json`).
- **Outcome**: Evidence
  `ev_2115d335dfdbe362fd4979099713275b2637394ebe73501614fad779063890ba`
  (form `ev_<64hex>`), operation `inspect_managed_native_boundaries`,
  provider `rea-dotnet-static`; `ORACLE OK (39/39 checks)` — the BYTE
  checks re-derive every compared fact from the built fixture bytes
  (Q03/Q06): the ImplMap row unpacked from the image (mapping flags
  0x0102, MemberForwarded coded index 5 → MethodDef row 2,
  import name `RunNative`, scope `native.dll`), the char_set
  (`ansi`) / call_convention (`winapi`) / no_mangle / supports_last_error
  decodes derived from those authored bits, the ModuleRef row's file
  offset 862 and name, the native-implementation row's method fields
  (token 0x06000002, RVA 0, flags 4241, impl_flags 5). The HYP checks
  are the pre-registered Q07 hypotheses frozen in `truth.json` BEFORE
  the committed run, recorded as predicted (verification
  `managed-declaration-only`, boundary_kind `pinvoke`, code_type
  `native`, managed_kind `unmanaged`, summary counts 1/1/1,
  cli_native il_only true, coverage `complete`). An authoring defect
  was caught and fixed BEFORE the committed runs: the ImplMap
  MemberForwarded initially coded row 1 (SayHello — which carries an IL
  body, semantically inconsistent with a P/Invoke declaration); the
  preprobe record exposed `member_token 0x06000001` +
  `native_implementation_count 2`, the coded index was corrected to row
  2, and the class is mined in `corpus/lessons/round-85.md`.
- **Pointer**: `corpus/live/runs/round-85/
  inspect-managed-native-boundaries/{inspection.json, receipt.json,
  LEDGER.md, oracle.log, stderr.txt}`; fixture
  `corpus/fixtures/managed-r85/`; oracle + regen re-run over
  `git archive` bytes at adjudication.

## Q10 scope note

One authored inert 1048-byte IL-only PE/CLI image whose P/Invoke row
declares (but does not perform) an import from `native.dll`. The
provider's own limitation is recorded as observed: "P/Invoke rows prove
managed import declarations only; this inspection does not verify that
a native library, export, thunk, or provider-qualified function
exists." No native library exists or is built; `native.dll` is a
string in the #Strings heap. Nothing is executed, nothing is loaded,
no general managed/native-interop claim is made (Q07: the
`managed-declaration-only` verification value is the producer's own
declared verification semantics, pre-registered and recorded).

## Admission status

Candidate record for round-85 C1; admission is the round's own VERIFY
conditions (claims.md) plus the non-author closure. This file records
the run; it does not self-admit.
