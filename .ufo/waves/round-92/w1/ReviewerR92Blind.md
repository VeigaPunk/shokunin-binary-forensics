# ReviewerR92Blind — round 92 wave 1 (final)

Role: blind derivation (Q03) of the managed fixture facts + non-author Q01–Q17 vote on the C1
entry. **Outcome: derivation complete, zero mismatches, vote cast — 15 PASS / 2 n/a / 0 FAIL.**

## Timeline note

The bounded wait for `ScribeR92Entry/READY` (40 × 30 s, ~09:54–10:14) timed out with no wave dir;
an interim report was written at that point. READY appeared later (sha256=
`2c96e633fc730d218560b9693b881ffdeb1244cad5ac77f5fb6626f494306fb6`), which I recomputed over the
entry's current bytes — **raw digest matches exactly** — and the comparison and vote then ran in
full.

## Blind derivation (fixture bytes only; own parser, no lane script/record/producer input)

Copies of `corpus/fixtures/managed-{r76,r85}/fixture.dll` were parsed by my own ECMA-335 parser
(`blind_parse.py`), written before the entry was read. Key derived facts, r85 (1048 bytes,
sha256 `94429fa4…86760`): machine I386 (0x014c), optional-header magic PE32 (0x10b); CLI header
present at file offset **512**, cb 72, runtime 4.0, flags 0x1, entrypoint 0; metadata root at file
offset **640 (0x280)**, signature **0x424a5342 (BSJB)**, version string `v4.0.30319`, size 400;
streams (offset from root/size) `#~` 0x6c/0x92, `#Strings` 0x100/0x54, `#US` 0x154/0x1d,
`#GUID` 0x174/0x10, `#Blob` 0x184/0x9 (the five ranges tile the metadata blob exactly);
`#~` Valid 0x0000000114000045 → row counts **Module 1, TypeDef 2, MethodDef 2, ModuleRef 1,
ImplMap 1, Assembly 1**; assembly **`r85-managed` 2.0.1.5**; module `r85-managed.dll`, Mvid bytes
10111213…1f; TypeDefs `<Module>`, `R85Probe.Probe`; MethodDefs `SayHello` (rva 0x1210, flags 0x91,
row at 0x342=834) and `RunNative` (rva 0, native); ModuleRef `native.dll` (row 0x35e=862); ImplMap
flags 0x102, import `RunNative` → `native.dll`, member MethodDef 2. Detail pass (`blind_detail.py`):
IL body at file offset 1040, tiny, 6 bytes `72010000702a`, sha256 `f82055…89346`, anchors
`[0,'ldstr','0x70000001'], [5,'ret']`; sig blob 3 bytes `00000e`, sha256 `7654e9…97eb`, conv
default, 0 params, return string; `#US` literal `Fixture Hello` at heap offset 981. r76 (924 bytes,
sha256 `25ece37…75733c`): same PE/CLI shape, root 640 BSJB, rows **Module 1, TypeDef 2,
Assembly 1**, assembly **`r76-managed` 1.2.3.4**, TypeDef `R76Probe.Probe`, Mvid 000102…0f.

## Comparison vs the entry — mismatches

**Zero.** Every fact the entry states that my derivation covers matched, including the deep ones
(row offsets 834/862, IL and signature digests, decoded signature, user string, mapping flags 258,
evidence offsets 512/528 = CLI header and its Flags field at +16). No mismatch to report.

## Independent verifications beyond the derivation

- All four `recheck:` commands run from the lane root: exit 0 each, summaries
  `ORACLE OK (10/10|20/20|47/47|39/39 checks)`, stdout line counts 11/21/48/40 as stated.
- All 11 embedded stdout blocks in the entry are **byte-identical** to the real command output.
- `git rev-parse 9402183a^{commit}` → `9402183a9492428fa0064d250746c62a0a2d9ca5` exactly as the
  entry states; `git diff --quiet 9402183a -- corpus` silent (Q15).
- Entry quotes located in ScoutR92Managed's fetched snapshots (ECMA-335 6th at :14205/:14221,
  PE-format CLR row at :618-621, MetadataRootBuilder page); S491–S494 drafted tier A
  `SOURCES.append.md`, opened 2026-11-05 (rows land in `corpus/SOURCES.md` at the L1's commit per
  the frozen claims; `C1_SOURCES` re-checks the landed tree).
- `reports/round-90/source_path_check.py --root <lane>` → `SOURCE_PATH_DEAD=0` (Q17).

## Vote

`reports/round-92/votes/ReviewerR92Blind.json` — `candidate_sha256`
`2c96e633fc730d218560b9693b881ffdeb1244cad5ac77f5fb6626f494306fb6` (recomputed, matches READY);
decisions Q01–Q17: **15 PASS, 2 n/a** (Q05: no readiness/capability claim made; Q08: superseded by
Q11), **0 FAIL**.

## Files

- `reports/round-92/votes/ReviewerR92Blind.json` — the vote.
- `.ufo/waves/round-92/w1/ReviewerR92Blind/blind_parse.py`, `blind_detail.py`,
  `blind_parse_output.txt` — my parser, detail pass, full outputs (both passes appended).
- This report.

No other lane file touched; no frozen file modified; scratch deleted; no tools installed (none
needed; pacman pause respected); no mutating git/jj command run.
