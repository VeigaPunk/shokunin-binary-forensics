# R64ReviewEntryQ06 — fixture-premise byte verification

Seat: reviewer (independent leaf). Scope: the **premises** the C07 candidate must
stand on — image size 2048 and sha256 `bdfe9f46…` against the *built* bytes; zlib
members at offsets 512 and 1024 with compressed sizes 79 and 90; three all-zero
padding spans 0–512, 591–1024, 1114–2048 (round-63 LEDGER). All commands were run
by me from lane root `/home/vgpnk/Projects/shokunin/revenger-shokunin`; the
premise derivation used my own stdlib code only. The candidate landed mid-review,
after which I also ran its embedded readout verbatim from the lane root. Stdlib
only; nothing installed; no repo state touched.

## Verdict

**PASS — every premise reproduces byte-exact, and the landed candidate's
commands reproduce its printed values exactly** (embedded script `2abe0c13…`,
stdout pin `aa353251…`, 7/7 fact lines identical, 6/6 base and 6/6 working-tree
digests identical, 25/25 oracle and 13/13 record field checks). Details and raw
outputs below.

## Premise 1 — image size 2048, sha256 bdfe9f46… (built bytes)

```
$ sha256sum corpus/fixtures/firmware-r63/firmware-r63.bin
bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be  corpus/fixtures/firmware-r63/firmware-r63.bin

$ stat -c '%s bytes' corpus/fixtures/firmware-r63/firmware-r63.bin
2048 bytes

$ git cat-file -p HEAD:corpus/fixtures/firmware-r63/firmware-r63.bin | sha256sum
bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be  -
```

Working-tree bytes equal the committed blob; `git status --porcelain corpus/knowledge corpus/fixtures`
is empty (no uncommitted fixture drift). **Rebuild check** in lane-owned scratch
`/tmp/revenger-r64-q06/` (generator + truth copied out; nothing written under `corpus/`):

```
$ python3 -B generator.py
wrote firmware-r63.bin sha256=bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be size=2048
region offset=0 size=512 kind=padding
region offset=512 size=79 kind=zlib
region offset=591 size=433 kind=padding
region offset=1024 size=90 kind=zlib
region offset=1114 size=934 kind=padding

$ cmp /tmp/revenger-r64-q06/firmware-r63.bin corpus/fixtures/firmware-r63/firmware-r63.bin
IDENTICAL
```

Host build environment matches the recorded recipe exactly: `python 3.14.8`,
`zlib` compile `1.3.2`, runtime `1.3.2`. `truth.json` `image.sha256`/`image.size`
agree with the derived values; `truth.json` blob hash is `9663f90b…` (`1933` B),
`generator.py` `4e5d5975…` (`5532` B), matching the round-63 LEDGER pins.

## Premise 2 — members at 512 / 1024, compressed sizes 79 / 90

Derived by stdlib `zlib.decompressobj` over the exact windows, with stream-end
checks (so "compressed size" is the true stream length, not a hoped-for one):

| member | offset | window size | zlib eof | unused_data | decompressed size | decompressed sha256 | truth match |
|---|---|---|---|---|---|---|---|
| diagnostic-note | 512 | 79 | True | 0 | 78 | `a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86` | yes (truth 78 / `a5718481…`) |
| component-note | 1024 | 90 | True | 0 | 97 | `2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9` | yes (truth 97 / `2d0d86aa…`) |

Both windows decode to the exact `build_recipe.members` `payload_utf8` strings.
Both streams end exactly at their reported size (offset+size = 591 and 1114), so
`zlib.decompress` over `image[512:591]` / `image[1024:1114]` consumes the whole
window with zero trailing bytes. Framing also checks out (independent of the
saved record): `cmf=0x78 flg=0xda`, FCHECK `%31 == 0`, FLEVEL 3, FDICT 0, and the
stored Adler-32 trailers equal the computed ones (`0x7b3b1d2d`, `0x11bf252c`).

## Premise 3 — three all-zero padding spans 0–512, 591–1024, 1114–2048

Per-span byte scan of the fixture (`set(span) == {0}`):

```
padding 0    size 512  all_zero True  len 512     -> span 0–512
padding 591  size 433  all_zero True  len 433     -> span 591–1024
padding 1114 size 934  all_zero True  len 934     -> span 1114–2048
```

Span sizes 433 and 934 are the LEDGER/truth values; the span *endpoints* in the
brief (591–1024, 1114–2048) follow by arithmetic and are confirmed by the
disjoint/contiguous full-coverage check: spans
`[(0,512),(512,591),(591,1024),(1024,1114),(1114,2048)]` start at 0, end at 2048,
are pairwise adjacent, and cover all 2048 bytes. Non-zero bytes **outside** the
two member windows: **0**. So the three padding spans are genuinely all-zero and
no fourth non-zero region exists that a byte readout could miss.

**Must-define nuance (byte-falsifiable if omitted).** Maximal zero-byte runs of
the whole image are **four**, not three:

```
$ python3 -c '... groupby ...'   # run lengths of zero bytes, whole image
maximal zero runs: [512, 433, 1, 934]   # the size-1 run is at offset 1098
offset 1098 value 0 | inside member2 [1024,1114) = True
zero bytes total 1880 | zero bytes outside members 1879
```

Offset **1098** is a zero byte *inside* the second compressed member. The three
padding spans in the brief are therefore only correct under the definition
"padding = all-zero complement of the measured member extents". An entry
sentence that calls them "the image's all-zero spans/runs" without that
definition is false at offset 1098 and would be a byte-level defect. This
matches `R64LabBlind`'s independent finding (its window digests
`bf3dd2e4…`/`8c32fdb0…` also match my measurement of `image[512:591]` and
`image[1024:1114]`).

## Cross-check against the candidate's derivation data

`/tmp/revenger-r64-entry/all.txt` (derivation data, not the entry) carries the
same values — image digest/size, five-region span list, both members' offset/
compressed size/decompressed size/digest, padding all-zero flags, zlib header
`78 da`, `header_check_mod31_zero: true`, `adler32` `7b3b1d2d` / `11bf252c`,
`flevel: 3`, `fdict: 0`, end offsets 591/1114, and the pinned file digests
(`truth.json 9663f90b…`, `LEDGER.md 25a4a18b…`, `inspection.json f6997835…`).
I re-derived every one of those from the lane bytes without running that file;
all agree. The landed entry states exactly these premises, and its own commands
reproduce them byte-for-byte (next section).

## Entry verification (candidate landed at 01:20 during this review)

Key finding: `/tmp/revenger-r64-entry/candidate.md` appeared after my premise
checks. I extracted its embedded `### Code` block verbatim to
`/tmp/revenger-r64-q06/readout.py`, ran every command from the lane root, and
compared outputs to the entry's printed values. The author then edited the
scratch file once during this review (sha256 `824bb00c…` → `e86a5b1c…`); I
re-extracted and re-ran the current text and the results below hold for it
(script block and stdout pin unchanged, `§Reproduce` stdout still equal line by
line).

```
extracted block sha256   2abe0c130ae29de27ae194511e3b4e5061364818cf94d8d8671c3019eafabae1
author copy sha256       2abe0c130ae29de27ae194511e3b4e5061364818cf94d8d8671c3019eafabae1   (identical)
$ python3 -B readout.py /home/vgpnk/Projects/shokunin/revenger-shokunin
exit=0, stderr empty, 7 JSON lines, all parse, no absolute path in stdout
sha256(stdout)           aa353251f7529a00c4336f9bf8cae6634838b8d10bd20e24b7340d94cf1314ae
entry §Reproduce pin     aa353251f7529a00c4336f9bf8cae6634838b8d10bd20e24b7340d94cf1314ae   EXACT
diff vs entry stdout     STDOUT_EXACT_MATCH
```

Per-fact form `--fact '<id>'` for all seven ids (`image`, `regions`, `members`,
`payloads`, `oracle`, `record`, `digests`): exit 0, and each parsed JSON object is
**exactly equal** to the corresponding JSON line printed in the entry (7/7
`EXACT_JSON_MATCH`). Structural checks: `regions` has 5 contiguous regions
covering 2048 bytes; `members` reports `(512, 79, 78, 591)` and
`(1024, 90, 97, 1114)`; `oracle` = 25/25 checks match; `record` = 13/13 checks
match with `authority` `shipped-artifact` — the entry's stated "25" and "13"
counts are correct.

Base-commit and working-tree digests from the entry's item 2 (six paths,
`git show 666ea84b…:<path> | sha256sum` and `sha256sum <path>`; read-only
`git show`, no mutation):

| path | base | worktree | entry | match |
|---|---|---|---|---|
| fixtures/firmware-r63/firmware-r63.bin | `bdfe9f46…510be` | same | same | yes |
| fixtures/firmware-r63/generator.py | `4e5d5975…793db4` | same | same | yes |
| fixtures/firmware-r63/truth.json | `9663f90b…da65e6` | same | same | yes |
| live/runs/round-63/inspection.json | `f6997835…aa71f9` | same | same | yes |
| live/runs/round-63/receipt.json | `e930a549…c6b94d` | same | same | yes |
| live/runs/round-63/LEDGER.md | `25a4a18b…bb1e1a6` | same | same | yes |

The entry's item 3 generator replay is the one I ran independently in
`/tmp/revenger-r64-q06/` (identical bytes, same printed digest/size/regions);
item 5's `78 da` / FLEVEL 3 / FDICT 0 / mod-31 / Adler values are the ones I
derived in Premise 2. **The entry's premises are accurate as landed.**

## Findings by severity

- **No actionable finding remains in the reviewed premises.** The fixture bytes,
  the five-region partition, the two member extents, the three padding spans, the
  framing/Adler fields, and every command output the entry prints are verified
  true by commands I ran myself from the lane root.
- **P1 — padding definition: required and present (satisfied).** Maximal zero
  runs of the whole image are four (`512, 433, 1, 934` bytes; the size-1 run is
  at offset **1098 inside member 2**), so the three padding spans are only true
  under the complement rule. The entry states that rule explicitly (line 17,
  observation O9, and §Limitations) and excludes 1098 by name — the exact
  precision my premise check showed was required. Residual: the wording must
  survive integration verbatim.
- **P2 — entry identity is pinned only by scratch content (advisory).** The
  candidate is 47 KB of `/tmp` scratch and its author edited it mid-review
  (`824bb00c…` → `e86a5b1c…`). What makes the numbers checkable is the stable
  script block (`2abe0c13…`) and the replay pin (`aa353251…`), both re-verified
  after the edit. L1 should integrate the reviewed text (or re-run the recheck
  after any further edit) rather than a regenerated variant; a later edit changes
  the pinned stdout only if the script block or fixture changes.
- **P3 — scratch files mimic the entry path (informational).** Several `/tmp`
  trees hold files at `corpus/knowledge/round-64-firmware-region-byte-evidence.md`
  that are self-labelled stand-ins ("SEPARABILITY STAND-IN", "SIMULATED ADMISSION
  STUB — scratch only, not a corpus candidate") written to exercise the frozen
  counter. They carry no evidence and must never be integrated; nothing in the
  lane working tree contains them.

## Residual risk and verification gaps

- Scope is the authored fixture only. The saved binwalk/REA record layer
  (`inspection.json` region `offset`/`reported_size`/`signature`) was used here at
  most as a cross-reference; its own integrity is the record-review seats'
  scope. Provider-reported sizes coinciding with the true stream ends is a
  property of this fixture, not a general claim.
- Not run here (out of scope): the `npx -y rea-agents@6.5.0 inspect-firmware-regions`
  route (record already saved; would add a network/provider run, not needed to
  confirm bytes) and the unblob cross-check (round-63 LEDGER O11).
- Rebuild determinism is demonstrated on this host at Python 3.14.8 / zlib 1.3.2,
  the exact recipe versions; reproduction on other runtime versions is not
  established by this review (the entry's §Limitations says the same).
- This review does not adjudicate Q01–Q13 quality, source tiers, or scope
  language beyond the byte premises and their in-entry commands; those are the
  Q01/Q09/Q11 and critic seats' decisions.
- No tools installed or upgraded (pacman untouched).

Report: `.ufo/waves/round-64/R64ReviewEntryQ06.md`
