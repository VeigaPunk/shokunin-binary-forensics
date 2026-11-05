source: S491 — ECMA-335, 6th edition (CLI) — https://ecma-international.org/wp-content/uploads/ECMA-335_6th_edition_june_2012.pdf (spec, tier A, opened 2026-11-05) — anchors: §II.24.2.1 Metadata root, §II.24.2.2 Stream header, §II.24.2.6 `#~` stream, §II.25.1, §II.25.3.3 CLI header, §II.25.3.3.1 Runtime flags — grounds the metadata-root signature, the five stream kinds, the `#~` stream's table-row array, the rule that locates the CLI header, and the il-only runtime flag
source: S492 — ECMA-335, 5th edition (CLI) — https://ecma-international.org/wp-content/uploads/ECMA-335_5th_edition_december_2010.pdf (spec, tier A, opened 2026-11-05) — anchors: §24.2.1 Metadata root, §24.2.2 Stream header, §24.2.6 `#~` stream — the same three metadata-layout facts at the previous edition, opened and quoted separately
source: S493 — PE Format (Microsoft Learn) — https://learn.microsoft.com/en-us/windows/win32/debug/pe-format (docs, tier A, opened 2026-11-05) — anchor: "Optional Header Data Directories (Image Only)" table, CLR Runtime Header row — grounds that a PE image locates its CLR runtime header through one optional-header data-directory entry
source: S494 — System.Reflection.Metadata.Ecma335.MetadataRootBuilder (Microsoft Learn) — https://learn.microsoft.com/en-us/dotnet/api/system.reflection.metadata.ecma335.metadatarootbuilder?view=net-10.0 (docs, tier A, opened 2026-11-05) — anchor: Remarks — grounds the .NET implementation's own statement of the metadata root's stream set
source: own-work records (not registry rows) — `corpus/live/runs/round-76/{inspection.json,receipt.json,LEDGER.md}`; `corpus/live/runs/round-85/inspect-managed-artifact/{inspection.json,receipt.json,oracle.log,LEDGER.md}`; `corpus/live/runs/round-85/inspect-managed-members/{inspection.json,receipt.json,oracle.log,LEDGER.md}`; `corpus/live/runs/round-85/inspect-managed-native-boundaries/{inspection.json,receipt.json,oracle.log,LEDGER.md}`; fixtures `corpus/fixtures/managed-r76/{fixture.dll,truth.json,oracle_check.py}` and `corpus/fixtures/managed-r85/{fixture.dll,truth.json,oracle_check.py}`
verified-at: 2026-11-05 at lane commit `9402183a` (`git rev-parse 9402183a^{commit}` prints `9402183a9492428fa0064d250746c62a0a2d9ca5`; `git diff --quiet 9402183a -- corpus` is silent, so the corpus tree read here is byte-identical at that commit)
recheck: `python3 -B corpus/fixtures/managed-r85/oracle_check.py corpus/fixtures/managed-r85/truth.json corpus/live/runs/round-85/inspect-managed-members/inspection.json corpus/fixtures/managed-r85/fixture.dll` from the lane root — exit 0 with `ORACLE OK (47/47 checks)` as its last stdout line; the three sibling commands in the unnumbered `## Reproduce` section re-derive the rest of this entry's numbers the same way
coverage-map: C03 (`corpus/README.md`, managed (.NET/CLI) assemblies) — the ground this entry covers is the two authored inert fixtures `corpus/fixtures/managed-r76/fixture.dll` and `corpus/fixtures/managed-r85/fixture.dll` and the four saved producer records named above; no other managed surface is claimed
admission-status: admitted

# Managed (.NET/CLI) assembly metadata in two authored PE/CLI fixtures, checked against four saved producer records — C03

Scope. One provider, one CLI-metadata format family, two authored inert fixtures, and the four saved
records the lane's own producer wrote for them. The analysis is **manual**: the lane's two committed
oracle scripts parse the fixture bytes with their own PE → COR20 → metadata-root → stream → `#~`-row
→ heap path and compare what they parsed against what the saved record says. Nothing was loaded,
executed or decompiled; no producer was invoked for this entry; no network call was made; no
credential material appears in this entry or in the records it reads.

The two fixtures are `corpus/fixtures/managed-r76/fixture.dll` and
`corpus/fixtures/managed-r85/fixture.dll`. The four saved records are
`corpus/live/runs/round-76/inspection.json` and the three
`corpus/live/runs/round-85/inspect-managed-{artifact,members,native-boundaries}/inspection.json`
records, whose operations are `inspect_managed_artifact` (twice, once per fixture),
`inspect_managed_members` and `inspect_managed_native_boundaries`.

## 1. Observation

**Reading rule for the blocks below.** Each block is one command's verbatim stdout. Every line is
`OK ` or `FAIL ` plus a check name, the value the script read, and — only on a failure — the value it
expected. The value printed after `got=` is the value the script read from the side the check name
names: `subject.sha256` and `fixture.sha256==truth` read the record's subject digest and the digest
the script computed over the fixture file's bytes respectively; every other line reads the record's
own field. The `OK` verdict on a line is the script's comparison of that value against the
expectation the §5 table names for that check — a value the script re-derived from the fixture bytes,
or a value fixed outside the record under test (the authored premise file `truth.json`, whether it
holds a pin or a pre-registered hypothesis), or a literal in the script. The two sides are not printed
as two numbers; the verdict is what carries the comparison. The item numbers below are this entry's
own and are not identifiers in any file.

**Locator-only citations** (source lines this entry names that the commands do not print):
`corpus/fixtures/managed-r85/oracle_check.py:28` (the optional-header data-directory entry the script
reads) and `corpus/fixtures/managed-r85/oracle_check.py:33` (the assertion on the metadata-root
signature).

**1. The r85 fixture's identity, and the artifact record made on it.**


```
$ python3 -B corpus/fixtures/managed-r85/oracle_check.py corpus/fixtures/managed-r85/truth.json corpus/live/runs/round-85/inspect-managed-artifact/inspection.json corpus/fixtures/managed-r85/fixture.dll
OK  op: got='inspect_managed_artifact'
OK  provider.id: got='rea-dotnet-static'
OK  subject.sha256==bytes: got='94429fa428893dd78ed4b7f26a919232d5f05cc9cdc84d256954db5b0a286760'
OK  bytes.len: got=1048
OK  classification.status: got='managed'
OK  classification.implementation: got='cil'
OK  classification.managed_architecture: got='anycpu'
OK  classification.evidence.codes: got=['cli-header-observed', 'managed-architecture-derived']
OK  classification.evidence.file_offsets: got=[512, 528]
OK  metadata.status: got='complete'
OK  metadata.stream_names: got=['#Blob', '#GUID', '#Strings', '#US', '#~']
OK  metadata.table_row_counts: got={'Module': 1, 'TypeDef': 2, 'MethodDef': 2, 'ModuleRef': 1, 'ImplMap': 1, 'Assembly': 1}
OK  module.name: got='r85-managed.dll'
OK  module.mvid: got='13121110-1514-1716-1819-1a1b1c1d1e1f'
OK  assembly.name: got='r85-managed'
OK  assembly.version: got='2.0.1.5'
OK  coverage.state: got='complete'
OK  confidence: got='observed'
OK  authority: got='shipped-artifact'
OK  evidence_id.form: got=True
ORACLE OK (20/20 checks)
```
The two identity lines are `subject.sha256==bytes` — the record's subject digest, compared with the
digest the script computed over `corpus/fixtures/managed-r85/fixture.dll`'s bytes — and `bytes.len`,
the record's byte length compared with the length of those bytes. The fixture file's own length is
1048: the `bytes.len` line carries the record's byte length, and its OK verdict is the comparison of
that field with the length the script measured in the file. The record's classification evidence
names the two file offsets the producer read, 512 and 528, and the record's own `pe.cli` block (a
**recorded** field of the saved file, not printed by any command here) gives `header_offset` 512,
`header_size` 72, `runtime_version` "4.0", `flags` 1 with `flag_names` ["il-only"], `metadata_rva`
4224 and `metadata_size` 400.

**2. The r76 fixture's identity, and the artifact record made on that other fixture.**


```
$ python3 -B corpus/fixtures/managed-r76/oracle_check.py corpus/fixtures/managed-r76/truth.json corpus/live/runs/round-76/inspection.json corpus/fixtures/managed-r76/fixture.dll
OK  operation: got='inspect_managed_artifact'
OK  classification.status: got='managed'
OK  classification.implementation: got='metadata-only'
OK  module.name: got='r76-managed.dll'
OK  assembly.name: got='r76-managed'
OK  assembly.version: got='1.2.3.4'
OK  metadata.stream_names: got=['#Blob', '#GUID', '#Strings', '#US', '#~']
OK  subject.sha256: got='25ece37da2e0effbe313662d81469371d59a1de4c610ed081b8a68bcdd75733c'
OK  fixture.sha256==truth: got='25ece37da2e0effbe313662d81469371d59a1de4c610ed081b8a68bcdd75733c'
OK  evidence_id present: got=True
ORACLE OK (10/10 checks)
```
The `fixture.sha256==truth` line carries the digest the script computed over
`corpus/fixtures/managed-r76/fixture.dll`'s bytes, and the `subject.sha256` line carries the record's
subject digest; the two are the same 64-character string. The first line compares the fixture bytes'
digest with the authored premise file's pinned digest, and the second compares the record's subject
digest with the fixture bytes' digest. The r76 record's `artifact.byte_length` (924) and its `pe.cli`
block (`header_offset` 512, `header_size` 72, `flags` 1, `metadata_rva` 4224, `metadata_size` 284) are
**recorded** fields of that saved file; the r76 script prints no byte length, so 924 is a recorded
value here and not a re-derived one.

**3. The members record: method rows, an IL body, a signature blob and one user string.**


```
$ python3 -B corpus/fixtures/managed-r85/oracle_check.py corpus/fixtures/managed-r85/truth.json corpus/live/runs/round-85/inspect-managed-members/inspection.json corpus/fixtures/managed-r85/fixture.dll
OK  op: got='inspect_managed_members'
OK  provider.id: got='rea-dotnet-static'
OK  subject.sha256==bytes: got='94429fa428893dd78ed4b7f26a919232d5f05cc9cdc84d256954db5b0a286760'
OK  bytes.len: got=1048
OK  module.name: got='r85-managed.dll'
OK  module.mvid: got='13121110-1514-1716-1819-1a1b1c1d1e1f'
OK  assembly.name: got='r85-managed'
OK  assembly.version: got='2.0.1.5'
OK  metadata.table_row_counts: got={'Module': 1, 'TypeDef': 2, 'MethodDef': 2, 'ModuleRef': 1, 'ImplMap': 1, 'Assembly': 1}
OK  metadata.status: got='complete'
OK  methods.count: got=2
OK  m0.token: got='0x06000001'
OK  m0.name: got='SayHello'
OK  m0.rva: got=4624
OK  m0.row_offset: got=834
OK  m0.flags: got=145
OK  m0.impl_flags: got=0
OK  m0.body.status: got='present'
OK  m0.body.format: got='tiny'
OK  m0.body.file_offset: got=1040
OK  m0.body.il_size: got=6
OK  m0.body.il_sha256: got='f8205533128770ef09040d0056a7758b86ae252af6e307cae5dd06dc6e989346'
OK  m0.body.opcode_counts: got={'ldstr': 1, 'ret': 1}
OK  m0.anchor0: got=[0, 'ldstr', '0x70000001']
OK  m0.anchor1: got=[5, 'ret']
OK  m0.sig.raw_length: got=3
OK  m0.sig.raw_sha256==bytes: got='7654e92fcd606089e218382991601eea77b70226c9ee308320f38cd03c6297eb'
OK  m0.sig.parse_status: got='decoded'
OK  m0.sig.conv: got='default'
OK  m0.sig.params: got=0
OK  m0.sig.return: got='string'
OK  m1.token: got='0x06000002'
OK  m1.name: got='RunNative'
OK  m1.rva: got=0
OK  m1.flags: got=4241
OK  m1.impl_flags: got=5
OK  m1.body.status: got='absent'
OK  us.state: got='complete'
OK  us.literals.count: got=1
OK  us.lit.value: got='Fixture Hello'
OK  us.lit.token: got='0x70000001'
OK  us.lit.offset: got=981
OK  us.issues: got=[]
OK  coverage.state: got='complete'
OK  confidence: got='observed'
OK  authority: got='shipped-artifact'
OK  evidence_id.form: got=True
ORACLE OK (47/47 checks)
```
The script unpacked the `#~` stream's rows out of the image, read the method body out of the image
at the offset it derived, hashed the IL bytes it found there and hashed the signature bytes it found
in the `#Blob` heap; the `m0.body.il_sha256` and `m0.sig.raw_sha256==bytes` lines are the record's
fields compared with those two digests. The `m0.sig.return` line is the record's decoded return type
compared with the value the script decoded from the signature byte it read, and the `us.lit.value`
line is the record's literal compared with the string the script decoded from the `#US` heap at the
offset it derived.

**4. The native-boundaries record: one ModuleRef row and one P/Invoke declaration.**


```
$ python3 -B corpus/fixtures/managed-r85/oracle_check.py corpus/fixtures/managed-r85/truth.json corpus/live/runs/round-85/inspect-managed-native-boundaries/inspection.json corpus/fixtures/managed-r85/fixture.dll
OK  op: got='inspect_managed_native_boundaries'
OK  provider.id: got='rea-dotnet-static'
OK  subject.sha256==bytes: got='94429fa428893dd78ed4b7f26a919232d5f05cc9cdc84d256954db5b0a286760'
OK  bytes.len: got=1048
OK  module_refs.count: got=1
OK  mr.name: got='native.dll'
OK  mr.token: got='0x1a000001'
OK  mr.row_offset: got=862
OK  pi.count: got=1
OK  pi.mapping_flags: got=258
OK  pi.import_name: got='RunNative'
OK  pi.import_scope_name: got='native.dll'
OK  pi.member_token: got='0x06000002'
OK  pi.member_kind: got='method'
OK  pi.member_name: got='RunNative'
OK  pi.char_set: got='ansi'
OK  pi.call_convention: got='winapi'
OK  pi.no_mangle: got=False
OK  pi.supports_last_error: got=False
OK  pi.verification: got='managed-declaration-only'
OK  ni.count: got=1
OK  ni.token: got='0x06000002'
OK  ni.name: got='RunNative'
OK  ni.rva: got=0
OK  ni.flags: got=4241
OK  ni.impl_flags: got=5
OK  ni.boundary_kind: got='pinvoke'
OK  ni.code_type: got='native'
OK  ni.managed_kind: got='unmanaged'
OK  ni.pinvoke_declared: got=True
OK  summary.module_refs: got=1
OK  summary.pinvokes: got=1
OK  summary.native_impls: got=1
OK  cli_native.il_only: got=True
OK  metadata.status: got='complete'
OK  coverage.state: got='complete'
OK  confidence: got='observed'
OK  authority: got='shipped-artifact'
OK  evidence_id.form: got=True
ORACLE OK (39/39 checks)
```
The script unpacked the ImplMap row out of the image and decoded the bits of the mapping-flags
value it read; the `pi.mapping_flags` line is the record's field compared with the value the script
read, and the `pi.char_set` and `pi.call_convention` lines are the record's decoded values compared
with the two decodings the script made from the bits of that same value. The `pi.import_name` and
`pi.import_scope_name` lines are the record's two names compared with the two strings the script read
from the `#Strings` heap at the indices the row gave it.

**5. The metadata root's five streams.** The artifact record names five streams, and ECMA-335
§II.24.2.2 names exactly five kinds of streams (the count is the item's carried quote below; the
name list is read from the §II.24.2.2 section body — the anchor section, not a carried quote) and
lists the same five names; the .NET implementation's own API page states the same set for a
metadata root.


```
$ python3 -B corpus/fixtures/managed-r85/oracle_check.py corpus/fixtures/managed-r85/truth.json corpus/live/runs/round-85/inspect-managed-artifact/inspection.json corpus/fixtures/managed-r85/fixture.dll
OK  op: got='inspect_managed_artifact'
OK  provider.id: got='rea-dotnet-static'
OK  subject.sha256==bytes: got='94429fa428893dd78ed4b7f26a919232d5f05cc9cdc84d256954db5b0a286760'
OK  bytes.len: got=1048
OK  classification.status: got='managed'
OK  classification.implementation: got='cil'
OK  classification.managed_architecture: got='anycpu'
OK  classification.evidence.codes: got=['cli-header-observed', 'managed-architecture-derived']
OK  classification.evidence.file_offsets: got=[512, 528]
OK  metadata.status: got='complete'
OK  metadata.stream_names: got=['#Blob', '#GUID', '#Strings', '#US', '#~']
OK  metadata.table_row_counts: got={'Module': 1, 'TypeDef': 2, 'MethodDef': 2, 'ModuleRef': 1, 'ImplMap': 1, 'Assembly': 1}
OK  module.name: got='r85-managed.dll'
OK  module.mvid: got='13121110-1514-1716-1819-1a1b1c1d1e1f'
OK  assembly.name: got='r85-managed'
OK  assembly.version: got='2.0.1.5'
OK  coverage.state: got='complete'
OK  confidence: got='observed'
OK  authority: got='shipped-artifact'
OK  evidence_id.form: got=True
ORACLE OK (20/20 checks)
```
The five names on the `metadata.stream_names` line are the record's own field, compared with the
five names fixed in the authored premise file's hypothesis block. The specification's own words for
this are S491's "Both logical tables and heaps are stored in streams. There are five possible kinds of streams."
(§II.24.2.2), the same sentence located independently in the previous edition (S492, §24.2.2), and
the implementation's own statement is S494's "Metadata root constitutes of a metadata header followed
by metadata streams ( #~ , #Strings , #US , #Guid and #Blob )." — note that the .NET page spells the
GUID heap `#Guid` while ECMA-335 (per its §II.24.2.2 section body — not a carried quote) and the
records spell it `#GUID`; this entry does not normalise the two spellings and reports the records'
spelling as it stands.

**6. The metadata root's magic signature.** S491's "Magic signature for physical metadata : 0x424A5342."
(§II.24.2.1) fixes the four bytes at the start of the metadata root, and the same sentence is located
independently in the previous edition (S492, §24.2.1). The r85 oracle script reads those four bytes at
the metadata-root offset it derives and asserts the value `0x424A5342` before it compares anything
else (`corpus/fixtures/managed-r85/oracle_check.py:33`); the assertion is silent when it holds, so the
evidence that it held for this fixture is the run in item 3 reaching its `ORACLE OK (47/47 checks)`
summary line and exiting 0. The r76 fixture's authored premise file records the same signature under
the name `BSJB` (`corpus/fixtures/managed-r76/truth.json`, `authored.metadata.signature`); that is a
**recorded** field of the authored file, not a byte reading made by any command in this entry.

**7. The `#~` stream's table-row counts.** S491's "The Rows array contains the number of rows for
each of the tables that are present." (§II.24.2.6) is the rule, located independently at the previous
edition in S492 (§24.2.6). The record prints the per-table counts and the script derived them from
the `#~` stream's `Valid` bit vector and its `Rows` array, so the two sides are independent readings
of the same stream.


```
$ python3 -B corpus/fixtures/managed-r85/oracle_check.py corpus/fixtures/managed-r85/truth.json corpus/live/runs/round-85/inspect-managed-artifact/inspection.json corpus/fixtures/managed-r85/fixture.dll
OK  op: got='inspect_managed_artifact'
OK  provider.id: got='rea-dotnet-static'
OK  subject.sha256==bytes: got='94429fa428893dd78ed4b7f26a919232d5f05cc9cdc84d256954db5b0a286760'
OK  bytes.len: got=1048
OK  classification.status: got='managed'
OK  classification.implementation: got='cil'
OK  classification.managed_architecture: got='anycpu'
OK  classification.evidence.codes: got=['cli-header-observed', 'managed-architecture-derived']
OK  classification.evidence.file_offsets: got=[512, 528]
OK  metadata.status: got='complete'
OK  metadata.stream_names: got=['#Blob', '#GUID', '#Strings', '#US', '#~']
OK  metadata.table_row_counts: got={'Module': 1, 'TypeDef': 2, 'MethodDef': 2, 'ModuleRef': 1, 'ImplMap': 1, 'Assembly': 1}
OK  module.name: got='r85-managed.dll'
OK  module.mvid: got='13121110-1514-1716-1819-1a1b1c1d1e1f'
OK  assembly.name: got='r85-managed'
OK  assembly.version: got='2.0.1.5'
OK  coverage.state: got='complete'
OK  confidence: got='observed'
OK  authority: got='shipped-artifact'
OK  evidence_id.form: got=True
ORACLE OK (20/20 checks)
```
Six tables are present in the r85 fixture — Module, TypeDef, MethodDef, ModuleRef, ImplMap and
Assembly — with the row counts the `metadata.table_row_counts` line carries. The r76 record's own
`metadata.table_row_counts` names three tables (Module, TypeDef, Assembly) with one row each; that
is a **recorded** field of that saved file, and the r76 oracle script does not re-derive table counts
from the r76 bytes, so no command in this entry compares the r76 counts with the r76 bytes.
**8. Where the CLI header sits.** S493's "208/224 8 CLR Runtime Header The CLR runtime header address
and size." is the PE-format data-directory row for the CLR runtime header, and S491's "The CLI
header (§II.25.3.3) is found using CLI Header directory entry in the PE header." (§II.25.1) states
the rule: the CLI header is reached through one optional-header data-directory entry, and the CLI
header in turn carries the address and size of the metadata. The r85 artifact record's classification
evidence names the two file offsets the producer read there — 512 and 528 — and the r76 record's
authored premise file records `cor20.data_directory_index` 14, `cor20.cb` 72,
`cor20.flags` "COMIMAGE_FLAGS_ILONLY (1)" and `cor20.entrypoint_token` 0; those are **recorded**
fields of the saved files. The r85 oracle script's own path through the image reads that same
directory entry (`corpus/fixtures/managed-r85/oracle_check.py:28`), and the il-only runtime flag the
record's `pe.cli` block carries as `flags` 1 is the flag ECMA-335 §II.25.3.3.1 fixes as
"COMIMAGE_FLAGS_ILONLY 0x00000001 Shall be 1." (S491). The two evidence offsets are the CLI header
and one of its fields: ECMA-335 §II.25.3.3 places the header's `Flags` field at offset 16 —
"16 4 Flags Flags describing this runtime image." (S491) — and 512 + 16 is the 528 the record names,
while the record's second evidence row is the one whose detail reads "Managed architecture anycpu is
derived from PE machine and CLI flags.
**9. Coverage, confidence, authority and the producer's own stated limits.** All four runs carry the
same three lines — `coverage.state` `complete`, `confidence` `observed`, `authority`
`shipped-artifact` — and an `evidence_id.form` line that checks only that the record's Evidence ID
has the `ev_`-prefixed form. The record's own `limitations` array reads "Static inspection did not
load the assembly, resolve dependencies through a CLR, decompile C#, or execute target code." — a
**recorded** field of the saved record. The `verification` value `managed-declaration-only` on the
P/Invoke record is the producer's own declared verification semantics.

## 2. Inference

10. [INFERENCE, scoped to these two fixtures and these four records] The producer's static metadata
decode agrees with an independent byte-level reading of the same fixture bytes for every field whose
expectation the script re-derived from those bytes: the fixture digest and length, the six table-row
counts, the module MVID, the assembly name and version, the method row offsets, RVAs, flags and
implementation flags, the IL body offset, length and digest, the signature blob length and digest,
the decoded signature convention and return type, the user-string literal and its offset, the
ModuleRef row, the ImplMap mapping flags and the two names they point at, and the native
implementation row's fields. Basis: the `OK` verdicts on the lines named for those checks in the §5
table, across the blocks of items 1–4 and 7.

11. [INFERENCE, scoped to these two fixtures] The CLI header the producer located sits where the PE
data-directory rule and ECMA-335's §II.25.1 say it must, and its second evidence offset is the
header's flags field: the record's classification evidence names file offsets 512 and 528, 512 is the
CLI header and 512 + 16 is the flags field §II.25.3.3 places at offset 16, the r85 oracle script
reaches the metadata root through that same directory entry and finds the `0x424A5342` root signature
there (item 6), and the record's own `pe.cli` block gives the header size 72 and the il-only flag
value 1 that §II.25.3.3 and §II.25.3.3.1 fix. Basis: items 1, 4, 6 and 8 with S491 and S493.

12. [INFERENCE, scoped to these two fixtures] The five stream names the records print are the five
stream kinds the specification names — the name list rests on the §II.24.2.2 and §24.2.2 section
bodies (the anchor sections, not a carried quote) — and the same set the .NET implementation states
for a metadata root; the records' `#GUID` spelling is the specification's own spelling as its
section body spells it, and differs only in letter case from the implementation page's `#Guid`.
Basis: item 5, S491 §II.24.2.2, S492 §24.2.2 and S494.

13. [INFERENCE, scoped to the r85 fixture] The P/Invoke row is a declaration and nothing more: the
record's own `verification` value says `managed-declaration-only`, the imported name `native.dll` is a
string in the `#Strings` heap of an inert image, and no library, export or thunk exists anywhere in
this entry's ground. Basis: item 4 and the fixture's authored premise file.

14. [INFERENCE] Each digest in this entry binds exactly the bytes it was computed over: the fixture
digests bind the two fixture files, the IL digest binds the IL bytes at the derived offset, the
signature digest binds the signature bytes, and the digests in the receipts bind the saved stdout
files. A digest match is not evidence of origin, completeness or authenticity. Basis: the digest
lines of items 1–4.

## 3. Unknown

15. Whether the producer's decode is correct or complete for any managed assembly other than these
two authored fixtures is **unknown**. This entry examines two inert images and four records.

16. Whether the metadata-root signature `0x424A5342` appears in any other producer's output is
**unknown**; this entry checks it only where its own parser asserts it.

17. Why the metadata root's version string is `v4.0.30319` — a **recorded** field of the r85 record,
also the value the .NET API page calls "The metadata version." (S494) — while ECMA-335 §II.24.2.1
states a version-string requirement for a conforming file, carried here only as the partial sentence "The Version string shall be “Standard CLI 2005” for any file that is intended to be executed on any conforming"
(S491; cut at the source PDF's line wrap, the requirement's remainder not quoted) is **unknown**.
This entry reports the divergence and does not explain it.

18. Whether `native.dll`, the module the P/Invoke row names, exists as a library anywhere is
**unknown**. Nothing was built, resolved or loaded.

19. Whether the four saved records are complete, correct in general, or authentic is **unknown**.
They are read as saved bytes; the digests bind bytes only.

20. Whether a .NET runtime would load, verify or execute either fixture is **unknown**; nothing was
loaded and no runtime was involved.

## 4. Limitations

21. **Fixture-scoped.** Two authored inert PE/CLI images — one of 924 bytes (a **recorded** length, from
the r76 premise file and the r76 record; the r76 script prints no byte length) and one of 1048 bytes
(the `bytes.len` line's value) — and four saved records of one built-in provider. Nothing here is a
claim about .NET, about the CLI format family at large, or about any assembly that was not authored
here.

22. **No producer readiness claim.** No producer was invoked for this entry, on this host or at this
time. The four records are saved files whose `receipt.json` files record the producer runs that wrote
them — recorded per `receipt.json`: `rea` 6.8.0, provider `rea-dotnet-static`, exit 0, stderr 0
bytes and the stdout digest are recorded fields of those receipt files, cited as saved and not
re-derived by any command in this entry;
this entry makes no claim that the producer is installed, available or usable now.

23. **No execution, no loading, no decompilation, no dependency resolution, no network.** The fixture
bytes were parsed by the lane's own scripts; the producer's own `limitations` line says the same of
its run.

24. **Which side of each comparison is a byte reading.** Every check the entry leans on compares
the record's field with an expectation, and the expectation has one of three sides. The table below
names the check names per side, per run; a check name that appears in one column appears in no other
column of that run.

| run | expectation re-derived from the fixture bytes | expectation fixed in the premise file (`truth.json`) | expectation a literal in the script |
|---|---|---|---|
| r85 artifact (20 checks) | `subject.sha256==bytes`, `bytes.len`, `metadata.table_row_counts`, `module.mvid`, `assembly.name`, `assembly.version` | pin: `module.name`; hypothesis: `op`, `provider.id`, `classification.status`, `classification.implementation`, `classification.managed_architecture`, `classification.evidence.codes`, `classification.evidence.file_offsets`, `metadata.status`, `metadata.stream_names`, `coverage.state`, `confidence`, `authority` | `evidence_id.form` |
| r85 members (47 checks) | `subject.sha256==bytes`, `bytes.len`, `metadata.table_row_counts`, `module.mvid`, `assembly.name`, `assembly.version`, `m0.name`, `m0.rva`, `m0.row_offset`, `m0.flags`, `m0.impl_flags`, `m0.body.file_offset`, `m0.body.il_size`, `m0.body.il_sha256`, `m0.sig.raw_length`, `m0.sig.raw_sha256==bytes`, `m0.sig.conv`, `m0.sig.params`, `m0.sig.return`, `m1.name`, `m1.rva`, `m1.flags`, `m1.impl_flags`, `us.lit.value`, `us.lit.token`, `us.lit.offset` | pin: `module.name`; hypothesis: `op`, `provider.id`, `metadata.status`, `m0.body.status`, `m0.body.format`, `m0.body.opcode_counts`, `m0.sig.parse_status`, `us.state`, `us.literals.count`, `coverage.state`, `confidence`, `authority` | `methods.count`, `m0.token`, `m0.anchor1`, `m1.token`, `m1.body.status`, `us.issues`, `evidence_id.form` |
| r85 boundaries (39 checks) | `subject.sha256==bytes`, `bytes.len`, `mr.name`, `mr.row_offset`, `pi.mapping_flags`, `pi.import_name`, `pi.import_scope_name`, `pi.member_token`, `pi.member_name`, `pi.char_set`, `pi.call_convention`, `pi.no_mangle`, `pi.supports_last_error`, `ni.name`, `ni.rva`, `ni.flags`, `ni.impl_flags` | hypothesis: `op`, `provider.id`, `pi.verification`, `ni.boundary_kind`, `ni.code_type`, `ni.managed_kind`, `summary.module_refs`, `summary.pinvokes`, `metadata.status`, `coverage.state`, `confidence`, `authority` | `module_refs.count`, `mr.token`, `pi.count`, `pi.member_kind`, `ni.count`, `ni.token`, `ni.pinvoke_declared`, `summary.native_impls`, `cli_native.il_only`, `evidence_id.form` |
| r76 (10 checks) | `subject.sha256` | pin: `operation`, `classification.status`, `classification.implementation`, `module.name`, `assembly.name`, `assembly.version`, `metadata.stream_names`, `fixture.sha256==truth` | `evidence_id present` |

Two checks need their printed value and their expectation told apart. On the r76 line
`fixture.sha256==truth` the printed value is the script's own digest of the fixture bytes and the
expectation it is compared with is the premise file's pin, so that line sits in the pin column; on
the r76 line `subject.sha256` the printed value is the record's field and the expectation is the
script's own digest of the fixture bytes, so that line sits in the bytes column. One check is mixed:
`m0.anchor0` compares the record's anchor against a literal offset and opcode with a byte-derived
token, so it is named in neither the bytes column nor the literals column of the members row. An `OK`
verdict on a pin or hypothesis line shows agreement with a value fixed in advance, not with an
independent parse.

25. **The record-file digests are recorded, not re-hashed here.** The `stdout_sha256` and
`stdout_bytes` values in the four `receipt.json` files are **recorded** fields of those saved files;
no command in this entry re-hashes a saved record.

26. **No guard credit.** The recheck command in the header re-derives the numbers below and exits
non-zero when a comparison fails; it detects no deletion of a clause, of a table row, or of a
sentence in this entry, and it is not credited as guarding any statement here.

27. **The parser is the lane's own.** The byte-level readings come from the lane's two committed
oracle scripts, which are lane code, not an independent third-party reader, and which read the same
two fixtures the records were made from.

## 5. Provenance (Q11)

Every count, identifier, offset and digest printed above is carried by one of the four commands, and
the line that carries it is named here, together with the side the script compared it against.

| # | what it states | command | the stdout line that carries it | the expectation side |
|---|---|---|---|---|
| 1 | r85 fixture digest and length; the record's classification and its two evidence offsets; the five stream names; the six table-row counts; the module MVID; the assembly name and version | r85 artifact oracle | `subject.sha256==bytes`, `bytes.len`, `classification.*`, `metadata.stream_names`, `metadata.table_row_counts`, `module.mvid`, `assembly.name`, `assembly.version` | the check names and their sides are listed per run in item 24 |
| 2 | the r76 fixture's digest as the script computed it over the fixture bytes, and the record's subject digest; the r76 identity fields | r76 oracle | `fixture.sha256==truth`, `subject.sha256`, `operation`, `classification.*`, `module.name`, `assembly.name`, `assembly.version`, `metadata.stream_names` | `subject.sha256` compares the record's field with the script's own digest of the fixture bytes; `fixture.sha256==truth` compares that same byte-derived digest with the premise file's pin; the identity fields compare the record's fields with the premise file's pins |
| 3 | method rows, the IL body, the signature blob, the user string | r85 members oracle | `m0.*`, `m1.*`, `us.*` lines | the check names and their sides are listed per run in item 24 |
| 4 | the ModuleRef row, the P/Invoke declaration, the native implementation | r85 boundaries oracle | `mr.*`, `pi.*`, `ni.*` lines | the check names and their sides are listed per run in item 24 |
| 5 | the five stream names, and their agreement with the specification and the .NET page | r85 artifact oracle (and the r76 oracle) | `metadata.stream_names` | the premise file's hypothesis block (the r85 run) and the premise file's pin (the r76 run); the specification and the .NET page are cited for the format fact, not for the record's field |
| 6 | the metadata-root signature value and where the script read it | the r85 members oracle run of item 3 | the run's `ORACLE OK (47/47 checks)` summary line (the assertion at `corpus/fixtures/managed-r85/oracle_check.py:33` is not printed) | the script's own reading of the fixture bytes, enforced by an assertion that is silent when it holds |
| 7 | the six table-row counts and the rule that produces them | r85 artifact oracle | `metadata.table_row_counts` | the script's own reading of the fixture bytes |
| 8 | the CLI header's location rule, the offsets the producer read, the il-only flag value | the r85 artifact oracle (offsets) and the r85 boundaries oracle | `classification.evidence.file_offsets`, `cli_native.il_only` | the premise file's hypothesis block; the PE-format row and the ECMA-335 clauses are cited for the format fact |
| 9 | coverage state, confidence, authority, Evidence ID form | all four runs | `coverage.state`, `confidence`, `authority`, `evidence_id.form` lines | the premise file's hypothesis block, except `evidence_id.form`, which is a script literal |


```
$ python3 -B corpus/fixtures/managed-r85/oracle_check.py corpus/fixtures/managed-r85/truth.json corpus/live/runs/round-85/inspect-managed-artifact/inspection.json corpus/fixtures/managed-r85/fixture.dll
OK  op: got='inspect_managed_artifact'
OK  provider.id: got='rea-dotnet-static'
OK  subject.sha256==bytes: got='94429fa428893dd78ed4b7f26a919232d5f05cc9cdc84d256954db5b0a286760'
OK  bytes.len: got=1048
OK  classification.status: got='managed'
OK  classification.implementation: got='cil'
OK  classification.managed_architecture: got='anycpu'
OK  classification.evidence.codes: got=['cli-header-observed', 'managed-architecture-derived']
OK  classification.evidence.file_offsets: got=[512, 528]
OK  metadata.status: got='complete'
OK  metadata.stream_names: got=['#Blob', '#GUID', '#Strings', '#US', '#~']
OK  metadata.table_row_counts: got={'Module': 1, 'TypeDef': 2, 'MethodDef': 2, 'ModuleRef': 1, 'ImplMap': 1, 'Assembly': 1}
OK  module.name: got='r85-managed.dll'
OK  module.mvid: got='13121110-1514-1716-1819-1a1b1c1d1e1f'
OK  assembly.name: got='r85-managed'
OK  assembly.version: got='2.0.1.5'
OK  coverage.state: got='complete'
OK  confidence: got='observed'
OK  authority: got='shipped-artifact'
OK  evidence_id.form: got=True
ORACLE OK (20/20 checks)
```

## §Q-map

| criterion | decision | basis |
|---|---|---|
| Q01 | pass | each load-bearing format fact rests on a tier-A row opened this round: S491 (ECMA-335 6th ed., §II.24.2.1, §II.24.2.2, §II.24.2.6, §II.25.1, §II.25.3.3, §II.25.3.3.1) for the metadata-root signature, the five stream kinds, the `#~` Rows array, the CLI-header location rule, the flags field's offset and the il-only flag; S492 (ECMA-335 5th ed., §24.2.1, §24.2.2, §24.2.6) for the same three layout facts at the previous edition; S493 (PE Format) for the CLR-runtime-header data-directory row; S494 (MetadataRootBuilder) for the implementation's own stream-set statement. Each quote is located in the fetched text (items 5, 6, 7, 8, 17). No tier-C row is cited and no claim rests on one. |
| Q02 | pass | the header carries `source:` (four registry rows with URL and anchor, plus the own-work record paths), `verified-at:` (the lane commit, the command that resolves it and the date), `recheck:` (one runnable command and the stdout line it must end with), and `coverage-map: C03` naming the row this entry fills. |
| Q03 | pass | the expected values come from the fixture bytes (the oracle scripts' own parse of the image) or from values fixed outside the record under test (the authored premise file's pins and its pre-registered hypotheses); no expected value is copied out of the record being checked, and the reading rule in §1 names the side of every comparison the entry leans on. |
| Q04 | pass | the analysis is manual byte reading by the lane's own committed scripts; the entry credits those scripts only with the lines their own stdout prints, and the producer only with the existence and literal fields of the four saved records. |
| Q05 | n/a | the entry makes no readiness or capability claim: no producer was invoked, and the `receipt.json` fields that record the earlier runs are labelled recorded, not re-verified. |
| Q06 | pass | the fixture premises are byte-verified by the scripts themselves: each computes the fixture file's own digest, and the r85 script its length, before comparing (items 1 and 2). |
| Q07 | pass | no parser behaviour is predicted here; the hypothesis side of the oracle is named as such in item 24 and in the §5 table, and the recorded outcome is reported whichever way it fell. |
| Q08 | superseded | QUALITY.md Q11 supersedes Q08; Q11 below is the operative criterion. |
| Q09 | pass | every digest is claimed only for the bytes it hashed (item 14); no origin, completeness or authenticity claim is made, and the record digests are labelled recorded (item 25). |
| Q10 | pass | the scope is one provider, one format family, two authored fixtures and four saved records; no cross-lane surface is absorbed and no general .NET claim is made (items 21 and 23). |
| Q11 | pass | every count, identifier, offset and digest above is carried by a named stdout line of a named command, and the §5 table names the expectation side of that line; the values that are only recorded are labelled recorded (items 1, 2, 6, 7, 8, 9 and 25). |
| Q12 | n/a | the entry cites no rejected source row and makes no reject/flip claim. |
| Q13 | pass | the recheck command is credited only with re-deriving the numbers it prints; the clauses it cannot detect are named: deleting a clause, a table row or a sentence of this entry, and the hypothesis side of any oracle check (items 24 and 26). |
| Q14 | pass | no prose hex run carries a byte count or an ASCII rendering; the counted byte values are command output inside fenced blocks, not prose literals. |
| Q15 | pass | the one git object id in this entry, `9402183a`, is named with the command that resolves it (`git rev-parse 9402183a^{commit}`) in the `verified-at:` header line, and the corpus tree's byte-identity at that commit is stated with the command that shows it. |
| Q16 | pass | each coverage statement names only what the named command prints: the item blocks quote the commands' own stdout lines, the reading rule in §1 states which side each printed value comes from, and the §5 table maps each statement to the line that carries it and to the expectation side. The `ORACLE OK (n/n checks)` summary lines are credited only as the run's own count of its checks. |
| Q17 | pass | no cited artifact was relocated in this round; every path this entry names resolves in the tree at the stated commit. |

## Sources

- **S491** (spec, tier A, opened 2026-11-05) — ECMA-335, 6th edition (CLI),
  <https://ecma-international.org/wp-content/uploads/ECMA-335_6th_edition_june_2012.pdf>. Anchors:
  §II.24.2.1 "Metadata root", §II.24.2.2 "Stream header", §II.24.2.6 "`#~` stream", §II.25.1,
  §II.25.3.3 "CLI header", §II.25.3.3.1 "Runtime flags"; the edition marker is the document's own
  "6th edition, June 2012". Located quotes used here, each verbatim in the fetched text and each 25
  words or fewer:
  - §II.24.2.1: "Magic signature for physical metadata : 0x424A5342." (7 words) — item 6.
  - §II.24.2.2: "Both logical tables and heaps are stored in streams. There are five possible kinds of streams."
    (16 words) — item 5.
  - §II.24.2.6: "The Rows array contains the number of rows for each of the tables that are present."
    (16 words) — item 7.
  - §II.25.1: "The CLI header (§II.25.3.3) is found using CLI Header directory entry in the PE header."
    (15 words) — item 8.
  - §II.25.3.3.1: "COMIMAGE_FLAGS_ILONLY 0x00000001 Shall be 1." (5 words) — item 8.
  - §II.25.3.3: "16 4 Flags Flags describing this runtime image." (8 words) — item 8.
  - §II.24.2.1: "The Version string shall be “Standard CLI 2005” for any file that is intended to be executed on any conforming"
    (20 words; a partial sentence cut at the source PDF's line wrap, not the full requirement) — item 17.
  Scope: the CLI metadata physical layout and the CLI-header location and runtime-flag rules, for the
  facts this entry states. Not cited for ZIP, PE resource layouts, CIL semantics, or any provider's
  behaviour.
- **S492** (spec, tier A, opened 2026-11-05) — ECMA-335, 5th edition (CLI),
  <https://ecma-international.org/wp-content/uploads/ECMA-335_5th_edition_december_2010.pdf>. Anchors:
  §24.2.1 "Metadata root", §24.2.2 "Stream header", §24.2.6 "`#~` stream"; the edition marker is the
  document's own "5th edition, December 2010". Located quotes used here, each 25 words or fewer:
  - §24.2.1: "Magic signature for physical metadata : 0x424A5342." (7 words) — item 6.
  - §24.2.2: "Both logical tables and heaps are stored in streams. There are five possible kinds of streams."
    (16 words) — item 5.
  - §24.2.6: "The Rows array contains the number of rows for each of the tables that are present."
    (16 words) — item 7.
  Scope: the same three metadata-layout facts at the previous edition, so that the values this entry
  states are not a reading of one edition only. This row is a different document from S491, with its
  own URL and its own digest, opened and quoted on its own.
- **S493** (docs, tier A, opened 2026-11-05) — PE Format (Microsoft Learn),
  <https://learn.microsoft.com/en-us/windows/win32/debug/pe-format>. Anchor: "Optional Header Data
  Directories (Image Only)", the CLR Runtime Header row; the page's own revision marker is its
  `ms.date` 2026-09-10. Located quote used here:
  - "208/224 8 CLR Runtime Header The CLR runtime header address and size." (12 words) — item 8.
  Scope: the optional-header data-directory entry that locates a PE image's CLR runtime header, for
  this one page. Not cited for the data-directory count, for any other section layout, or for any
  metadata-format question.
- **S494** (docs, tier A, opened 2026-11-05) — System.Reflection.Metadata.Ecma335.MetadataRootBuilder
  (Microsoft Learn),
  <https://learn.microsoft.com/en-us/dotnet/api/system.reflection.metadata.ecma335.metadatarootbuilder?view=net-10.0>.
  Anchor: "Remarks"; the page's own revision marker is its `ms.date` 2025-07-01. Located quotes used
  here, each 25 words or fewer:
  - "Metadata root constitutes of a metadata header followed by metadata streams ( #~ , #Strings , #US , #Guid and #Blob )."
    (22 words) — item 5.
  - "The metadata version." (3 words) — item 17.
  Scope: the .NET implementation's own statement of a metadata root's stream set and of the metadata
  version property. Not cited for the file format itself (that is S491/S492), for any runtime
  behaviour, or for the spelling of the GUID heap in the records.
- **Own-work records (not registry rows).** The four saved producer records with their receipts and
  ledgers, and the two fixtures with their authored premise files and oracle scripts, are named in the
  `source:` header line. They are the lane's own bytes and carry no registry id in this round.

## Reproduce

From the lane root, with the lane's committed scripts and the committed fixture bytes (no producer, no
network, nothing written):


```
$ python3 -B corpus/fixtures/managed-r76/oracle_check.py corpus/fixtures/managed-r76/truth.json corpus/live/runs/round-76/inspection.json corpus/fixtures/managed-r76/fixture.dll
OK  operation: got='inspect_managed_artifact'
OK  classification.status: got='managed'
OK  classification.implementation: got='metadata-only'
OK  module.name: got='r76-managed.dll'
OK  assembly.name: got='r76-managed'
OK  assembly.version: got='1.2.3.4'
OK  metadata.stream_names: got=['#Blob', '#GUID', '#Strings', '#US', '#~']
OK  subject.sha256: got='25ece37da2e0effbe313662d81469371d59a1de4c610ed081b8a68bcdd75733c'
OK  fixture.sha256==truth: got='25ece37da2e0effbe313662d81469371d59a1de4c610ed081b8a68bcdd75733c'
OK  evidence_id present: got=True
ORACLE OK (10/10 checks)
```

```
$ python3 -B corpus/fixtures/managed-r85/oracle_check.py corpus/fixtures/managed-r85/truth.json corpus/live/runs/round-85/inspect-managed-artifact/inspection.json corpus/fixtures/managed-r85/fixture.dll
OK  op: got='inspect_managed_artifact'
OK  provider.id: got='rea-dotnet-static'
OK  subject.sha256==bytes: got='94429fa428893dd78ed4b7f26a919232d5f05cc9cdc84d256954db5b0a286760'
OK  bytes.len: got=1048
OK  classification.status: got='managed'
OK  classification.implementation: got='cil'
OK  classification.managed_architecture: got='anycpu'
OK  classification.evidence.codes: got=['cli-header-observed', 'managed-architecture-derived']
OK  classification.evidence.file_offsets: got=[512, 528]
OK  metadata.status: got='complete'
OK  metadata.stream_names: got=['#Blob', '#GUID', '#Strings', '#US', '#~']
OK  metadata.table_row_counts: got={'Module': 1, 'TypeDef': 2, 'MethodDef': 2, 'ModuleRef': 1, 'ImplMap': 1, 'Assembly': 1}
OK  module.name: got='r85-managed.dll'
OK  module.mvid: got='13121110-1514-1716-1819-1a1b1c1d1e1f'
OK  assembly.name: got='r85-managed'
OK  assembly.version: got='2.0.1.5'
OK  coverage.state: got='complete'
OK  confidence: got='observed'
OK  authority: got='shipped-artifact'
OK  evidence_id.form: got=True
ORACLE OK (20/20 checks)
```

```
$ python3 -B corpus/fixtures/managed-r85/oracle_check.py corpus/fixtures/managed-r85/truth.json corpus/live/runs/round-85/inspect-managed-members/inspection.json corpus/fixtures/managed-r85/fixture.dll
OK  op: got='inspect_managed_members'
OK  provider.id: got='rea-dotnet-static'
OK  subject.sha256==bytes: got='94429fa428893dd78ed4b7f26a919232d5f05cc9cdc84d256954db5b0a286760'
OK  bytes.len: got=1048
OK  module.name: got='r85-managed.dll'
OK  module.mvid: got='13121110-1514-1716-1819-1a1b1c1d1e1f'
OK  assembly.name: got='r85-managed'
OK  assembly.version: got='2.0.1.5'
OK  metadata.table_row_counts: got={'Module': 1, 'TypeDef': 2, 'MethodDef': 2, 'ModuleRef': 1, 'ImplMap': 1, 'Assembly': 1}
OK  metadata.status: got='complete'
OK  methods.count: got=2
OK  m0.token: got='0x06000001'
OK  m0.name: got='SayHello'
OK  m0.rva: got=4624
OK  m0.row_offset: got=834
OK  m0.flags: got=145
OK  m0.impl_flags: got=0
OK  m0.body.status: got='present'
OK  m0.body.format: got='tiny'
OK  m0.body.file_offset: got=1040
OK  m0.body.il_size: got=6
OK  m0.body.il_sha256: got='f8205533128770ef09040d0056a7758b86ae252af6e307cae5dd06dc6e989346'
OK  m0.body.opcode_counts: got={'ldstr': 1, 'ret': 1}
OK  m0.anchor0: got=[0, 'ldstr', '0x70000001']
OK  m0.anchor1: got=[5, 'ret']
OK  m0.sig.raw_length: got=3
OK  m0.sig.raw_sha256==bytes: got='7654e92fcd606089e218382991601eea77b70226c9ee308320f38cd03c6297eb'
OK  m0.sig.parse_status: got='decoded'
OK  m0.sig.conv: got='default'
OK  m0.sig.params: got=0
OK  m0.sig.return: got='string'
OK  m1.token: got='0x06000002'
OK  m1.name: got='RunNative'
OK  m1.rva: got=0
OK  m1.flags: got=4241
OK  m1.impl_flags: got=5
OK  m1.body.status: got='absent'
OK  us.state: got='complete'
OK  us.literals.count: got=1
OK  us.lit.value: got='Fixture Hello'
OK  us.lit.token: got='0x70000001'
OK  us.lit.offset: got=981
OK  us.issues: got=[]
OK  coverage.state: got='complete'
OK  confidence: got='observed'
OK  authority: got='shipped-artifact'
OK  evidence_id.form: got=True
ORACLE OK (47/47 checks)
```

```
$ python3 -B corpus/fixtures/managed-r85/oracle_check.py corpus/fixtures/managed-r85/truth.json corpus/live/runs/round-85/inspect-managed-native-boundaries/inspection.json corpus/fixtures/managed-r85/fixture.dll
OK  op: got='inspect_managed_native_boundaries'
OK  provider.id: got='rea-dotnet-static'
OK  subject.sha256==bytes: got='94429fa428893dd78ed4b7f26a919232d5f05cc9cdc84d256954db5b0a286760'
OK  bytes.len: got=1048
OK  module_refs.count: got=1
OK  mr.name: got='native.dll'
OK  mr.token: got='0x1a000001'
OK  mr.row_offset: got=862
OK  pi.count: got=1
OK  pi.mapping_flags: got=258
OK  pi.import_name: got='RunNative'
OK  pi.import_scope_name: got='native.dll'
OK  pi.member_token: got='0x06000002'
OK  pi.member_kind: got='method'
OK  pi.member_name: got='RunNative'
OK  pi.char_set: got='ansi'
OK  pi.call_convention: got='winapi'
OK  pi.no_mangle: got=False
OK  pi.supports_last_error: got=False
OK  pi.verification: got='managed-declaration-only'
OK  ni.count: got=1
OK  ni.token: got='0x06000002'
OK  ni.name: got='RunNative'
OK  ni.rva: got=0
OK  ni.flags: got=4241
OK  ni.impl_flags: got=5
OK  ni.boundary_kind: got='pinvoke'
OK  ni.code_type: got='native'
OK  ni.managed_kind: got='unmanaged'
OK  ni.pinvoke_declared: got=True
OK  summary.module_refs: got=1
OK  summary.pinvokes: got=1
OK  summary.native_impls: got=1
OK  cli_native.il_only: got=True
OK  metadata.status: got='complete'
OK  coverage.state: got='complete'
OK  confidence: got='observed'
OK  authority: got='shipped-artifact'
OK  evidence_id.form: got=True
ORACLE OK (39/39 checks)
```

Each command exits 0 and prints one line per check plus a summary line: `ORACLE OK (10/10 checks)`,
`ORACLE OK (20/20 checks)`, `ORACLE OK (47/47 checks)` and `ORACLE OK (39/39 checks)` respectively.
The stdout line counts are 11, 21, 48 and 40.