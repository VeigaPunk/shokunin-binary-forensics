# R64ReviewEntryScope — Q03/Q10 admission review of the C07 candidate

Seat `revenger-r64.R64ReviewEntryScope` (reviewer; not the candidate author).
Read-only seat: no production/spec/registry/sibling edit, no git/jj mutation, no commit or
push, no producer/counter/gate run, no tool installed or upgraded (pacman not used). Scratch
is this seat's own `/tmp/revenger-r64-entryscope/`; this report is the only lane file written.

## Axes

- **Q03 (independent derivation):** are the entry's expected values obtained from the fixture
  bytes alone, independent of `truth.json`?
- **Q10 (scope):** do the entry's sentences confine the finding to the observed input,
  operation and version, with no universal clause, and is cross-lane contested scope
  reported rather than absorbed?
- **Admission:** PASS/FAIL for Q03 and Q10 on the reviewed artifact.

## Reviewed artifact

`/tmp/revenger-r64-entry/candidate.md` — the briefed draft path — `sha256
e86a5b1c9f382c186818fe55c78eed1537aa907151853e81f6aef80d4ff86cc9`, 455 lines, at the 01:28
re-check. The draft changed once during this review (`824bb00c…` at 01:21 → `e86a5b1c…` at
01:28); the second snapshot was re-checked and its `### Code` block is unchanged
(`2abe0c13…`), its values and line numbers match those reviewed, and its Q10 gap is
identical, so the verdicts below apply to `e86a5b1c…`. The integration path
`/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-64-firmware-region-byte-evidence.md`
was still absent at 01:28 (`ls corpus/knowledge/ | grep 64` prints nothing), so this review is
of the scratch draft L1 will integrate; any further post-review edit needs a re-run.

## Verdict

| criterion | verdict | basis |
|---|---|---|
| Q03 | **PASS** | every stated layout value is reproduced from the image bytes by an independent scan (this seat's own script, below); the entry carries the deriving command and printed output for each value; `truth.json` is used only as a post-derivation comparison oracle; padding spans are defined as the complement of discovered member extents and the one-byte zero at 1098 is explicitly excluded (draft lines 14-17, 73-75, 158, O9) |
| Q10 | **FAIL** | the draft contains no cross-lane contested-scope sentence: zero occurrences of `ADJ-06`, `kaidoku`, `tsukuroi`, `sibling`, `absorb` anywhere in the 455 lines; the Q10 map row (line 177) answers **record provenance**, which is Q08/Q09 material, not Q10. A `held` C07 token is the first sentence a later handoff can quote as firmware ownership (`R64ConnectorOverlap.md`), and this draft does not fence it |
| admission | **FAIL** | `corpus/QUALITY.md` admits only when no criterion fails; Q10 fails, so C1 cannot be admitted on this artifact. Q03 needs no rework — the fix is additive text |

Q10 fails by **omission, not absorption**: the draft cites no sibling file, no kaidoku
Evidence ID (`ev_0388cb9a…`, `ev_4009f834…`), no GSP count and no README host-pin line
(`corpus/README.md:63-66`). Its confinement side is good; only the contest report is missing.

**Landed-artifact update (supersedes the Q10/overall rows for the integrated entry):** on
`corpus/knowledge/round-64-firmware-region-byte-evidence.md`, sha256
`9bf21e5057b77f17a8406af9d006fb4594dd2da54c6d0920f4ca842cfa3e0ebf`, the cross-lane fence is
present and Q10 **PASSES**; derived values/commands/outputs are unchanged and Q03 **PASSES**.
See §Addendum.

## Q03 evidence — bytes-only derivation, independent of truth.json and of the author's script

Copy (only the image; no `truth.json`, no `generator.py`, no saved record):

```
$ mkdir -p /tmp/revenger-r64-entryscope/bytes
$ cp /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/firmware-r63.bin \
     /tmp/revenger-r64-entryscope/bytes/
$ ls -la /tmp/revenger-r64-entryscope/bytes/
-rw-r--r-- 1 vgpnk vgpnk 2048 Oct 24 01:17 firmware-r63.bin
$ sha256sum /tmp/revenger-r64-entryscope/bytes/firmware-r63.bin
bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be  .../firmware-r63.bin
```

This seat's `/tmp/revenger-r64-entryscope/derive.py` (stdlib `hashlib`, `zlib`, `json`,
`pathlib`; reads only `bytes/firmware-r63.bin`) tries `zlib.decompressobj()` at **all 2048
offsets**, keeps offsets where EOF is reached, and defines padding as the zero-checked
complement of the discovered member extents. Observed output
(`/tmp/revenger-r64-entryscope/derive.out`; the author's script was not read before this ran):

```
image 2048 bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be
member 512 591 79 78 a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86 compressed_sha256 bf3dd2e42d36324ae17e81c66cb5d699ac74b1a017628fcfb4302846b1c7c352 adler32 7b3b1d2d trailer 7b3b1d2d
member 1024 1114 90 97 2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9 compressed_sha256 8c32fdb048dc29f3f47dd1fb1c8fe53790d239309e340e03bd486d8722d424ff adler32 11bf252c trailer 11bf252c
padding 0 512 512 all_zero True
padding 591 1024 433 all_zero True
padding 1114 2048 934 all_zero True
offsets_tried 2048 streams_found 2
naive_zero_runs [(0, 512), (591, 1024), (1098, 1099), (1114, 2048)]
```

| derived from bytes alone | value (matches draft item) |
|---|---|
| image size / sha256 | 2048 / `bdfe9f46…a8510be` (item 1) |
| zlib member offsets | 512 and 1024 — only two complete streams in 2048 attempts (items 4-5) |
| compressed member sizes | 79 and 90 (item 5) |
| decompressed sizes | 78 and 97 (items 5-6) |
| decompressed sha256 | `a5718481…df7b86`, `2d0d86aa…eeaba9` (item 5) |
| zero padding spans outside members | (0,512), (591,1024), (1114,2048) sizes 512/433/934 (item 4) |
| partition | 79+90+512+433+934 = 2048, no overlap, no gap (item 4) |

`truth.json` was opened only **after** the derivation, for comparison:

```
truth.image.size 2048 == derived 2048
truth.image.sha bdfe9f46…a8510be == derived
truth padding spans [(0,512),(591,433),(1114,934)] == derived True
truth zlib members [(512,79,78,a5718481…),(1024,90,97,2d0d86aa…)] == derived True
```

So the brief's "at least two derived values from fixture bytes alone" is satisfied several
times over, and the draft's values agree with a derivation that never saw its script or the
oracle. The 1098 counterexample (a `0x00` byte inside member `[1024,1114)`; `od -An -t x1
-j1095 -N7` prints `2e c2 79 00 76 8c d5`) is handled correctly and disclosed: draft lines
14-17 state the complement rule, line 158 states that a different rule yields a different
partition, and O9 records the excluded run. This resolves the precursor defect recorded in
`R64CriticCounts.md:12-46`.

Q11 consistency spot-checks on the draft (read-only):

- The `### Code` block (draft lines 186-441, 251 lines, sha256
  `2abe0c130ae29de27ae194511e3b4e5061364818cf94d8d8671c3019eafabae1`) is byte-identical to
  the scratch `readout.py`/`extracted.py` at that hash, so the "saved verbatim" claim holds.
- The 7-line full stdout block carries the pinned sha256
  `aa353251f7529a00c4336f9bf8cae6634838b8d10bd20e24b7340d94cf1314ae`, which is the observed
  sha256 of the actual 7-line run output (`wc -l` 7). The stdout block adds only the command
  and the `sha256sum` line around those 7 JSON lines.
- The readout's deriving facts (`image`, `regions`, `members`, `payloads`) load only
  `corpus/fixtures/firmware-r63/firmware-r63.bin`; `oracle` and `record` facts load the
  comparison documents. Derivation therefore does not read the oracle — Q03 is structural,
  not just stated.
- The record-comparison scope matches the saved record I read: `normalized_result.input_size`
  2048, regions `(512, reported_size 79, zlib)` and `(1024, 90, zlib)`,
  `size_basis: provider_reported_validation_unknown`, `coverage: signature_scan`,
  `extractions: {}`, no padding regions, no decompressed digests. The draft claims exactly
  that narrower agreement (items 8, 125) and attributes inflated sizes/digests to manual
  analysis — no provider credit is taken.

## Q10 findings

### HIGH (blocking for admission) — no cross-lane contested-scope report

The draft has no `## Cross-lane scope note (Q10)` and no sentence naming the contest. Grep
over all 455 lines of `e86a5b1c…`: `ADJ-06` 0, `kaidoku` 0, `tsukuroi` 0, `sibling` 0, `absorb` 0,
`ownership` 0. The requirement is concrete, not stylistic: `R64ConnectorOverlap.md` §Proposed
move supplies the tested sentence (ADJ-06 open at `.ufo/l0-questions.md:42`; kaidoku Core live
`inspect-firmware-regions`/`extract-firmware` and pin registry not absorbed; tsukuroi
driver/firmware health plane not absorbed), and the round-63 C06 generic line is explicitly
insufficient for C07 because this round creates the first `held` firmware token. Without it,
the entry's own Q10 row (draft line 177) substitutes record provenance — a Q08/Q09 answer —
so a fresh reader sees Q10 unattended.

**Fix (additive, no value moves):** insert the connector's sentence as a named
`## Cross-lane scope note (Q10)` section, and replace the Q10 map row with a pointer to it.
Carry the fence into the README C07 cell parenthetical on admission, and into a retained
rejected candidate if C1 falsifies (`R64ConnectorOverlap.md` §Proposed move; `claims.md`
"if C1 falsifies, L1 flips C07 `frontier → uncovered`").

### LOW (confinement side) — PASS as written; universal-clause scan clean

- Scope paragraph (line 10) names the one file, its size and digest, and states manual
  standard-library analysis with no extraction, execution, emulation or mount.
- Coverage-map header (line 5) and Limitations (157-163) enumerate the five contract
  disclaimers: no vendor/device image, no container/format or general "firmware region"
  behaviour, no extraction or execution, no provider-completeness claim, no authenticity
  claim. Unknown U2/U3/U4 repeat the same boundaries.
- No universal finding clause found: the only general sentence, "compressed bytes can
  themselves be `0x00`" (line 17), is a method justification instantiated by the 1098 byte in
  the same sentence, and every numbered claim is bounded to this image / this record /
  Binwalk 3.1.0. `FLEVEL` 3, Adlers, and member sizes are stated per member, not as format
  law. The digest disclaimer (line 127, Q09 row) prevents the comparison from being read as
  origin or authenticity.

### LOW — recorded-label discipline holds

Member labels `diagnostic-note`/`component-note` are explicitly marked generator/oracle
labels, not byte-derived (line 6, U1). This satisfies the Q03/Q11 labelling concern raised in
`R64CriticFixture.md` §3 and is repeated in §Correspondence (line 127).

## What L1 must do before the C1 gate

1. Add the `## Cross-lane scope note (Q10)` sentence (named ADJ-06 contest, kaidoku Core and
   pin registry, tsukuroi health plane — reported, not absorbed) and repoint the Q10 map row.
2. Integrate the draft at the target path; the reviewed hash changes, so re-run Q10 against
   the landed text. Q03 needs no rework: values, commands, outputs and padding rule are
   sound.
3. On admission, the README C07 cell must carry the connector's parenthetical; no other row
   changes. On falsification, C07 → `uncovered` and the fence stays in the retained file.
4. Do not add a sibling `SOURCES` row or a sibling-file citation to satisfy Q10 — the contest
   is reported, not sourced (`R64ConnectorOverlap.md` §Risks).

## Residual risk and verification gaps

- The Q10 FAIL is judged on the 01:28 scratch draft (`e86a5b1c…`); an edit made after this
  review invalidates it. The integration path did not exist at 01:28, so nothing here clears
  the landed entry.
- This seat ran no producer, counter, gate or judge and makes no K/C4 claim; Q01/Q02 and the
  other criteria belong to their own seats. My Q03 cross-check agrees with the independent
  derivation in `R64CriticCounts.md`; I did not rely on that report for any value.
- Authoring history is not observable: the PASS verifies the shipped readout's data flow
  (deriving facts load only the fixture) and reproduces every value from bytes with a
  different script. It does not prove no oracle value was ever seen while drafting.
- Install/upgrade record: none (no tool needed; pacman not used).
- Scratch `/tmp/revenger-r64-entryscope/` is lane-owned and can be removed on landing; the
  reviewed INPUT (`/tmp/revenger-r64-entry/`) is the scribe's, not mine.

Report: .ufo/waves/round-64/R64ReviewEntryScope.md

## Addendum — landed-artifact confirmation (`9bf21e50…`, 01:31)

Landed file read: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-64-firmware-region-byte-evidence.md`,
`sha256 9bf21e5057b77f17a8406af9d006fb4594dd2da54c6d0920f4ca842cfa3e0ebf`, 496 lines. This
addendum supersedes the draft verdicts for the integrated artifact.

### 1. Cross-lane fence (Q10) — present, named, citations verified

Lines 201-203 carry `## Cross-lane scope note (Q10)` with the paragraph beginning
"Reported, not absorbed." It states that the entry covers only the authored
`corpus/fixtures/firmware-r63/firmware-r63.bin` bytes against the saved
`inspect_firmware_regions` record; that a C07 `held` token does not settle ADJ-06; and that it
does not absorb kaidoku's live surface or tsukuroi's health plane. Every citation was read at
its target and matches:

| citation in fence | target line, observed |
|---|---|
| fleet `.ufo/l0-questions.md:42` remains open | line 42 is the tsukuroi round-1 question to "arbitrate the kaidoku/revenger shipped-artifact overlap before an ADJ-06 analysis is routed" |
| `tsukuroi-shokunin/PROVINCE.md:51` — "protocol integrator — kaidoku/revenger ownership unresolved" | line 51 is the ADJ-06 row and contains that exact recipient text |
| `kaidoku-shokunin/PROVINCE.md:50,76-79,125` | `:50` archive/package inventory; `:76-79` firmware pruned into Core ("firmware … each now held"); `:125` Firmware regions + extract row naming `inspect-firmware-regions`, `extract-firmware`, binwalk 3.1.0 / unblob 26.6.4 |
| `kaidoku-shokunin/PROVINCE.md:64-71` (pin registry) | `:64-71` "Cross-lane registry … never stands for that lane's current runtime capability" |
| `tsukuroi-shokunin/PROVINCE.md:3-4,11-13` | `:3-4` domain includes "drivers/firmware"; `:11-13` "driver/firmware plane" |

The fence ends "No ownership is declared and no other lane's file is cited as support for a
value here." The updated Q10 map row (line 218) points to the section. No sibling Evidence ID,
GSP count, or README host-pin line appears anywhere in the entry. **Q10 now PASSES.**

### 2. Delta `e86a5b1c…` → `9bf21e50…` changed no derived value, command or output

- `### Code` block (251 lines) hashes `2abe0c130ae29de27ae194511e3b4e5061364818cf94d8d8671c3019eafabae1`
  — byte-identical to the readout reviewed at `e86a5b1c…` and to the scratch `readout.py`
  (the landed entry and `/tmp/revenger-r64-entry/candidate.md` are now the same bytes).
- The stdout pin `aa353251f7529a00c4336f9bf8cae6634838b8d10bd20e24b7340d94cf1314ae` is
  present and still matches the 7-line run output.
- Value anchors intact: image sha `bdfe9f46…a8510be` (14 occurrences), inflated digests
  `a5718481…df7b86` and `2d0d86aa…eeaba9` (7 each), member offset/size and padding size keys
  present.
- This seat's blind derivation re-run against the unchanged bytes-only copy returns the same
  values: image 2048 / `bdfe9f46…`; streams at 512 and 1024; compressed 79 and 90; inflated 78
  and 97 with the same digests; complement padding `(0,512)`, `(591,1024)`, `(1114,2048)` =
  512/433/934. The naive maximal-zero-run view still shows the 1098 interior byte, which the
  entry's stated complement rule excludes.

**Q03 remains PASS on the landed artifact.** The delta is prose and table edits only.

### 3. Boundary

This addendum clears Q03 and Q10 only. Q01/Q02/Q04–Q13 and the admission decision belong to
their own seats and L1. The README C07 row was still `frontier` at review time
(`corpus/README.md:36`), consistent with the frozen order (flip only after adjudication). No
producer, counter, gate or judge was run; no tool installed or upgraded.

Report: .ufo/waves/round-64/R64ReviewEntryScope.md
