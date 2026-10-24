# R64ReviewEntryQ11 — Q11/Q08 admission review of the C07 candidate

Seat: R64ReviewEntryQ11 (reviewer, independent leaf). Round contract:
`reports/round-64/claims.md`. Brief: `.ufo/waves/round-64/briefs/R64ReviewEntryQ11.md`.

## Artifact reviewed (pinned)

- Candidate draft: `/tmp/revenger-r64-entry/candidate.md`
  sha256 `0a3730a1a03b19ef134930a8eb180147be8b6e503fbd7040fdd7617eafed0a22`
  (48334 bytes, 459 lines), readout `/tmp/revenger-r64-entry/readout.py`
  sha256 `2abe0c130ae29de27ae194511e3b4e5061364818cf94d8d8671c3019eafabae1`.
- Lane path `corpus/knowledge/round-64-firmware-region-byte-evidence.md` was
  **absent** at review time (`ls` → no match); the draft is still scribe scratch.
  See D1. The draft changed twice while this review ran
  (`824bb00c…` → `e86a5b1c…` → `0a3730a1…`); on the final hash all seven
  `--fact` blocks, the §Code block and the §Stdout block still match my runs
  exactly (re-checked after each change).

## Verdict: **FAIL** — narrow and correctable

The byte evidence is sound and every one of the five required re-derivations
matches exactly. The entry fails Q11 on two of the criterion's own defect
clauses — recorded values labelled re-derived (F1) and three sizes that are
correct but carry no in-entry derivation (F3) — and carries one claim about the
saved record that the record's own bytes falsify (F2). All three are mechanical
fixes; none invalidates the derived layout.

## Five re-derivations (run by me, from the in-entry commands)

Repo root `/home/vgpnk/Projects/shokunin/revenger-shokunin`, script copied from
the entry's §Code block. All seven facts exit 0.

1. **Image sha256 + size** — `python3 -B readout.py <repo-root> --fact 'image'`
   ```
   {"fact": "image", "path": "corpus/fixtures/firmware-r63/firmware-r63.bin", "sha256": "bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be", "size": 2048}
   ```
   Matches entry item 1 byte-for-byte; `sha256sum corpus/fixtures/firmware-r63/firmware-r63.bin`
   independently prints `bdfe9f46…510be`, `stat` 2048 bytes. **PASS**
2. **Both member offsets and compressed sizes** — `--fact 'members'`
   ```
   {"fact": "members", "members": [{"adler32_computed_hex": "7b3b1d2d", …, "compressed_size": 79, …, "end_offset": 591, …, "offset": 512}, {"adler32_computed_hex": "11bf252c", …, "compressed_size": 90, …, "end_offset": 1114, …, "offset": 1024}]}
   ```
   (full line identical to entry item 5). Offsets **512 / 1024**, compressed
   **79 / 90**, ends **591 / 1114**. **PASS**
3. **Decompressed digests** — same fact: member A 78 bytes
   `a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86`,
   member B 97 bytes
   `2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9`;
   Adler-32 trailers equal the recomputed values for both. **PASS**
4. **Padding span** — `--fact 'regions'`
   ```
   {"contiguous_from_zero": true, "covered_bytes": 2048, "fact": "regions", "image_size": 2048, "padding_all_zero": true, "regions": [{"all_zero": true, "fill_hex": "00", "kind": "padding", "offset": 0, "size": 512}, … {"offset": 591, "size": 433}, … {"offset": 1114, "size": 934}]}
   ```
   Spans **[0,512) 512**, **[591,1024) 433**, **[1114,2048) 934**; partition
   contiguous over 2048 bytes. **PASS**
5. **Recheck pin** — `python3 -B readout.py <repo-root>` → 7 lines, exit 0,
   `sha256sum` of stdout =
   `aa353251f7529a00c4336f9bf8cae6634838b8d10bd20e24b7340d94cf1314ae`,
   exactly the `recheck:` pin in the header. §Code block is byte-identical to
   `readout.py` (sha256 `2abe0c13…`, 10018 bytes), and stdout contains no
   absolute path (`grep -c '/home/'` = 0). **PASS**

Blind corroboration (Q03): a decoder I wrote before reading the entry's script
(`zlib.decompressobj` over every offset, member ranges subtracted before
zero-run detection) produced the same image digest, the same two offsets and
compressed sizes, the same two decompressed digests, and the same three padding
spans; whole-file zero runs are `(0,512) (591,433) (1098,1) (1114,934)`, so the
entry's O9 claim that the one-byte run at 1098 sits inside member B's
`[1024,1114)` and is deliberately not padding is true (`byte@1098 == 0x00`).

Other values I re-derived and confirmed: all six base-commit digests in item 2
(`git show 666ea84b…:<path> | sha256sum` = working-tree `sha256sum` for fixture,
generator, oracle, record, receipt, ledger); generator replay in scratch prints
the entry's item-3 lines and both digests; snapshot
`.ufo/waves/round-64/source-snapshots/rea-firmware-guide.md` = 10695 bytes,
sha256 `e422b481…93609`, with the quoted lines 3, 56, 83-85, 91-96 present as
quoted; record `extractions` = `{}`, `coverage` `signature_scan`, `confidence`
`observed`, `authority` `shipped-artifact`.

## Findings

### F1 — HIGH (Q11 defect clause: recorded values presented as re-derived)

`readout.py:fact_record` builds six comparison checks whose `derived` side is a
literal copied from the record, and two more that compare an expression to
itself:

| field | `derived` in printed output | source |
|---|---|---|
| `operation` | `"inspect_firmware_regions"` | literal in `fact_record` |
| `provider.version` | `"3.1.0"` | literal |
| `record@512.signature`, `record@1024.signature` | `"zlib"` | literal |
| `record@512.size_basis`, `record@1024.size_basis` | `"provider_reported_validation_unknown"` | literal |
| `record@512.present`, `record@1024.present` | `true` | `"stated": r is not None, "match": r is not None` — same expression both sides |

So of the 13 checks the entry reports as "All **13** compared fields match"
(candidate item 8, line 107), only **5** are independent byte-derived
comparisons (`subject.digest.sha256`, `normalized_result.input_size`,
`region_count`, both `reported_size`). The same class appears in
`fact_oracle`: 9 of 25 `derived` sides are literals — `image.path`
(`"firmware-r63.bin"`), the three `padding@*.kind` (`"padding"`), the three
`padding@*.fill_hex` (`"00"`, hard-coded while `all_zero` is checked
separately), and both `zlib@*.kind` — leaving **16** independent derivations
under "All **25**".

Precedent in the admitted corpus: `corpus/knowledge/round-63-zip-central-directory-evidence.md`
item 13 labels the analogous record fields **recorded** — "Its recorded fields —
read from the file, not re-derived — are … operation `inspect_artifact`,
provider id …, provider version `1`" — and its saved-field facts use
`saved_*` / `*_equals_derived_*` keys rather than a `derived` key. The
candidate's printed evidence therefore presents record values as re-derived,
which is exactly Q11's second defect clause.

Fix: rename the constant checks (e.g. `recorded`/`asserted`) or drop them from
the comparison lists, and state the counts honestly (16 byte-derived oracle
comparisons + 9 recorded/structural assertions; 5 byte-derived record
comparisons + 6 recorded assertions + 2 presence checks). No derived value
changes.

### F2 — HIGH (falsified claim about the saved record's text)

Candidate line 125: "the second scanner named in the REA route (Unblob)
**appears nowhere in it**." The record does name it:

```
$ grep -c unblob corpus/live/runs/round-63/inspection.json
0
$ grep -c Unblob corpus/live/runs/round-63/inspection.json
1
$ grep -o 'Unblob[^"]*' corpus/live/runs/round-63/inspection.json
Unblob's default sandbox and skip rules remain enabled. …
```

The claim is true only for the case-sensitive lowercase token the ledger's own
O11 row used (`grep -c unblob` = 0); the record's `limitations[2]` boilerplate
names Unblob. The accurate statement is: Unblob is named only in the record's
limitation boilerplate, never as an executed provider, and `extractions` is
`{}`. This is a content claim about the record's bytes and must be re-derived,
not inherited from a case-sensitive grep.

### F3 — MEDIUM (Q11 defect clause: correct value, no derivation)

Three sizes in the source rows carry no in-entry command or output:

- `S037` line 2: `generator.py … (5532 bytes)` — no command prints this size
  (`--fact 'digests'` covers only fixture/oracle/record/ledger).
- `S037` line 2: `receipt.json … (492 bytes)` — same gap.
- `S036` line 1: snapshot `10695 bytes` — no command prints it.

All three are correct (`stat -c '%s'` / `ls -l`: 5532, 492, 10695; snapshot
sha256 matches), but Q11 requires the command *and its output* inside the
entry. Fix: add `generator.py`, `receipt.json` and the snapshot to
`--fact 'digests'` (or print one `wc -c` block). Contrast the four sizes that
are covered: 2048, 1933, 22671, 3904 all appear in the `digests` output.

### F4 — LOW (interpretation wording)

Item 5: "FLEVEL is 3 (maximum compression, matching the oracle's level 9)".
`FLEVEL` is a 2-bit hint: zlib level 9 ⇒ FLEVEL 3, but FLEVEL 3 does not imply
level 9. The value `flevel: 3` is correctly derived (`flg >> 6`); only the
"matching … level 9" gloss overstates it. Suggest "consistent with the oracle's
recorded level 9".

### D1 — DEPENDENCY (not a candidate defect)

The lane deliverable path is absent; the review binds to the scratch bytes
above. If L1 lands different bytes, this verdict does not transfer: the pinned
`recheck` sha256 (`aa353251…`) must be re-derived from the landed §Code block,
because it is a hash of the readout's stdout and any script edit changes it.

## Residual risk

- The oracle `truth.json` is authored by the same generator that writes the
  fixture; my derivation proves bytes ↔ oracle ↔ record correspondence for this
  fixture, nothing about provenance (the entry disclaims this under Q09).
- Generator replay byte-identity holds on this host only (Python 3.14.8, zlib
  1.3.2 — the recipe's own versions); the entry already bounds this.
- The record is a signature scan (`size_basis=provider_reported_validation_unknown`);
  the entry correctly refuses to treat `reported_size` as measurement, and I did
  not re-run Binwalk.

## Verification gaps

- No `lsp` device was exposed to this seat (`read xd://lsp` → "No such tool:
  xd://lsp. Mounted devices: ast_edit, debug"), so no semantic diagnostics for
  `readout.py`; diagnostics were established by executing it (exit 0) and by
  byte-for-byte comparison of its stdout against every quoted block.
- The draft was mutating during review; F1-F4 are cited against hash
  `0a3730a1…` and line numbers in that file. Any later edit needs the block
  comparison and the five re-derivations re-run.
- Disclosure: I ran `corpus/fixtures/firmware-r63/generator.py` once from a
  scratch cwd, but the script writes next to itself, so it rewrote
  `firmware-r63.bin` and `truth.json` in place at 01:17:37. Both are
  byte-identical to the index (`git status --porcelain corpus/fixtures
  corpus/live` → empty; fixture sha256 `bdfe9f46…510be`, oracle `9663f90b…5e6`),
  only mtimes changed. No frozen byte moved. All later replays were done on a
  copy under `/tmp/revenger-r64-review-q11/gen/`.

## Tooling

No install or upgrade was performed (nothing was needed; pacman untouched).
Scratch: `/tmp/revenger-r64-review-q11/` (copies of `readout.py`, seven fact
outputs, full stdout, generator replay, my independent `derive.py`) — lane-owned
and removable on landing.

## Re-review (landed bytes)

Artifact: `corpus/knowledge/round-64-firmware-region-byte-evidence.md`,
**53098 bytes**, sha256
`9bf21e5057b77f17a8406af9d006fb4594dd2da54c6d0920f4ca842cfa3e0ebf`.
`diff -q` against the scribe draft: identical, so the re-review is of the landed
text. The earlier sections of this report remain the history of the
`0a3730a1…` draft.

### Verdict: **PASS**

### Derivations unchanged (prose-only edits confirmed)

- Extracted the §Code block **from the landed file**, saved it as
  `landed_readout.py` (identical to `readout.py`, sha256 `2abe0c13…`), ran it
  from the lane root: exit 0, stdout byte-identical to my earlier run
  (`cmp landed_full.out full.out` → identical), sha256
  `aa353251f7529a00c4336f9bf8cae6634838b8d10bd20e24b7340d94cf1314ae` = the
  entry's `recheck:` pin.
- All seven `--fact` blocks (`image`, `regions`, `members`, `payloads`,
  `oracle`, `record`, `digests`) compare equal to my pinned outputs, including
  the five required re-derivations of the first review: image
  `bdfe9f46…510be` (2048 B); offsets **512/1024**, compressed **79/90**, ends
  591/1114; decompressed `a5718481…df7b86` (78 B) and `2d0d86aa…eeaba9`
  (97 B); padding **512 / 433 / 934** over `[0,512) [591,1024) [1114,2048)`,
  contiguous 2048; stdout pin as above.
- The seven-line §Stdout block is still present verbatim and matches my run.

### Findings resolved

- **F1 resolved.** Item 7 now states 25 = **16 byte-derived + 9 recorded
  constants** and item 8 states 13 = **5 byte-derived + 8 recorded fields**,
  matching my enumeration exactly; both explain that the JSON `derived` key is
  the check's left side and label the constants **recorded, not re-derived**.
- **F2 resolved.** The Unblob sentence is gone. The record paragraph now says
  no Unblob provider run appears (`grep -c unblob` = 0 on the lowercase provider
  id), that the single `Unblob` mention is `limitations[2]` sandbox/skip
  boilerplate, and rewords the record's producer as **recorded provenance**
  with "no digest establishes that attribution". I ran the new item-11 command
  verbatim: `unblob_lower: 0, unblob_upper: 1` — output identical to the entry.
- **F3 resolved.** Item 10 prints `wc -c` and `sha256sum` for the three
  previously underived sizes; my runs print exactly `5532`, `492`, `10695`
  (total 16719) and `4e5d5975…`, `e930a549…`, `e422b481…` — identical to the
  entry.
- **F4 resolved.** Item 5 now reads "`FLEVEL` is 3 (a maximum-compression hint,
  consistent with the oracle's level 9)".

### A–H fix list confirmed

- Recorded-vs-derived labels and honest counts (16+9 / 5+8): confirmed above.
- Unblob sentence + recorded-provenance rewording: confirmed above.
- New items 10–11: confirmed by running both blocks verbatim — item 11 prints
  `{'region_count': 2, …, 'names_present': False,
  'decompressed_digest_present': False, 'extractions': {}, 'unblob_lower': 0,
  'unblob_upper': 1}`, identical to the entry.
- Q-map rows: Q01/Q02/Q03/Q04/Q06/Q09/Q11/Q13 answer their criteria; Q05, Q07,
  Q12 are marked `n/a` with reasons that hold (no readiness claim, no predicted
  parser behaviour, no rejected source row); Q08 is marked superseded by Q11.
- FLEVEL wording: confirmed.
- U6 same-author unknown: present and correct (the generator wrote both image
  and oracle; the 25 comparisons are internal consistency, not independent
  confirmation).
- Host runtime command + output: `python3 -V` → `Python 3.14.8`; `python3 -c
  'import zlib; print(zlib.ZLIB_VERSION, zlib.ZLIB_RUNTIME_VERSION)'` →
  `1.3.2 1.3.2` — my run reproduces both lines exactly.
- Cross-lane citations spot-checked and present/on-topic: fleet
  `.ufo/l0-questions.md:42`; `tsukuroi-shokunin/PROVINCE.md:3-4,11-13,51`;
  `kaidoku-shokunin/PROVINCE.md:50,64-71,76-79,125`.
- Block audit: 24 command blocks, 23 carry printed output; the one without
  output is the `cp` setup line (silent by design). No `TODO`/`TBD`/
  `placeholder` markers.

### Integration warning (L1's, not a candidate defect)

Lane HEAD `671e3a1` ("… C07 candidate entry …") committed the **pre-correction**
draft: `git show HEAD:corpus/knowledge/round-64-firmware-region-byte-evidence.md`
= sha256 `0a3730a1…`, 48440 bytes, and the index holds the same blob
(`git ls-files -s` → `5fa82661…` → `0a3730a1…`). The reviewed bytes
`9bf21e50…` are **worktree only** (`git status` → ` M`). L1 must stage and
commit the reviewed bytes; a counter run on `git archive HEAD` would otherwise
read the version this report first failed. I made no git/jj mutation.

### Residual risk and gaps (unchanged)

Authored oracle written by the same generator (U6 now states it); replay
identity is host-bounded (Python 3.14.8 / zlib 1.3.2); the record is a
signature scan and was not re-run. No `lsp` device is exposed to this seat
(`xd://lsp` → "No such tool"), so diagnostics came from executing the landed
§Code block (exit 0) and byte-exact stdout comparison.
