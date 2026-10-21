GRADE: HOLDS — source-snapshots manifest + S028/S029 entry source facts
Frozen target d97761952be256d145d298022de03091de91d358 (claim base
5bd4a90fc1a34caa94496601b60537b3aab12301; pre-registration
a3498e25ad87bf756288812d0ea7c474b09433c7). Extracted with
`git archive d9776195… | tar -x -C /fast/scratch/hyaku/revenger-r62/R62FSnapshotAuthority`;
all checks on archived copies (TMPDIR under seat scratch). Candidate hashes at target:
`round-62-evm-dispatch-byte-evidence.md` `6a1d394ad92fcaa5344069d1225e428988f1397e80c8968745d7b48bf43fed6e`,
`round-62-commonjs-require-name-evidence.md` `42096e9676d33e25c3b6092e60fbd0fdacd699435ed9dc9db59ce24a1ceaaba3`
(both equal `git cat-file -p target:<path> | sha256sum`; live tree identical).
`manifest.json` sha256 `cd26810aeecf4ea7f0824f5ef88e16176541c439eedcde8fe2cf36f67c057c4b`,
git blob `b94042e680aa027927270bee8cc8232d729f1b7a` (`rev-parse target:…` ==
`hash-object` live path; not self-declared).

## Observation (commands + exact output)

1. Manifest self-consistency, cwd=archived `source-snapshots`: a `python3` loop over
`manifest.json` prints `size_ok True sha_ok True` for all 4 entries — instructions
10700 B `49dd6155…b63724`; runtime 1971 B `a2801c41…09aef8`; statements 956160 B
`a23fc93c…5fc8813e`; scripts 1033596 B `a5444406…6b136d4`. All declared hashes equal
`sha256sum` of stored files; no fifth file.
2. URL identity at 2026-10-21 (read-only public re-open; fetched bytes not executed,
not the fixture base): execution-specs raw endpoints returned `runtime_http=200
size=1971`, `instr_http=200 size=10700`; `cmp` → `RUNTIME_BYTES_IDENTICAL`,
`INSTR_BYTES_IDENTICAL`. tc39 multipage endpoints returned `stmt_http=200
size=956160`, `scripts_http=200 size=1033596`; `cmp` → `STMT_IDENTICAL`,
`SCRIPTS_IDENTICAL`. Live re-fetch equals frozen snapshot bytes.
3. Source identity: `git ls-remote --tags` →
`67f038c8c3fced0b388cfdcaed5c4a52d5fad2fd refs/tags/v2.20.0` and
`2004296f2ffcbcebcd00f41152d33e8dfda0922a refs/tags/v2.20.0^{}` — the S028/candidate
"tag v2.20.0, commit 2004296f…" pair is the dereferenced tag, not the tag object.
4. S028 quotes vs stored bytes (`strip()` equality): runtime.py 22, 28, 29, 30, 64 →
`EXACT` ×5; instructions `__init__.py` 55,104,106,109,118,121,122,125,153 → `EXACT`
×9. The entry's `:29-30` two-line rendering matches bytes; the lesson's one-line
quote is a line-join with bullet marker omitted (13 words, no word changed).
5. S029 vs stored chapter bytes: `Set value to ? GetV(value, propertyName).` is step 3
of production `SingleNameBinding : BindingIdentifier Initializeropt` under
`14.3.3.3 Runtime Semantics: KeyedBindingInitialization` (printed steps: 1 `Let
name…`, 2 `ResolveBinding`, 3 `GetV`, … 11 `InitializeReferencedBinding`).
`[[ImportName]]` sentence occurs twice; the "name under which the desired binding is
exported" instance at raw 812117 lies in `<emu-table caption="ImportEntry Record
Fields">` captioned `Table 54`; the other at 819346 is `Table 56` ExportEntry.
Headings `14.3.1.3 Runtime Semantics: BindingEvaluation`, `16.2.1.7 Source Text
Module Records` (contains Table 54), `16.2.2 Imports` present; ids
`sec-runtime-semantics-keyedbindinginitialization` and
`table-importentry-record-fields` each found once.
6. Version recorded vs derived: live `https://tc39.es/ecma262/` returned 7629271 B,
sha256 `06db92a8331aa452b0d4de8c8938f4b7559b72417769b57d0032002398f27d7f` — exactly
the S029 row and C04 header value — and contains `Draft ECMA-262 / October 16, 2026`.
The two stored chapter files are titled `ECMAScript® 2027 Language Specification`
and contain zero `Draft`/`October` strings (only `© Ecma International 2026`).

## Inference

- Every declared manifest hash/size/URL and every S028/S029 quoted section or line is
  verified against stored frozen bytes and independently against live endpoints; no
  declared hash or quote mismatch exists in this scope.
- Version facts are recorded, not re-derived by the entries: S028 tag/commit is
  recorded and tag resolution confirms it; the ECMA draft date is a recorded header
  value derived from the single-page URL by the opener, not from either stored chapter.
- The manifest stores the two multipage chapters, not the single-page document whose
  digest S029 records; that is a representation-scope distinction (chapter bytes cover
  every quoted clause), not a contradiction — no manifest declaration claims the
  chapters hash to `06db92a8…`.
- Candidate citation `SingleNameBinding : BindingIdentifier` omits the grammar's
  optional `Initializeropt`; the quoted step is still that production's step 3, so
  this is shorthand, not a denied fact.

## Unknown

- No stored snapshot of the single-page document exists here; its byte identity rests
  on live re-open at 2026-10-21 plus the opener's recorded fetch, not on the four files.
- The `origin` sentence ("copied byte-exact by L1") cannot be verified from bytes; byte
  equality to opener-declared digests and live URLs is consistent with it. Opener
  scratch copies were absent, so file-to-file copy comparison was impossible.
- Nothing here admits either candidate; Q11/Q01 decisions remain other seats' and L1's.

VERDICT: HOLDS. The four snapshot files, their declared hashes/sizes/URLs, the S028
commit/tag and all 5+9 cited source lines, and the S029 §14.3.3.3 and Table 54 quotes
are exact; version claims are recorded and independently matched. No repair indicated.
Installs: none.
