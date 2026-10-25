REJECT — every substantive figure reproduces against a fresh fetch and a fresh probe I ran myself today (digest pin still matches), but the draft carries located Q02 and Q11 defects: four stale item cross-references (header/Scope point the probe at items 4–5; the commands are items 6–7), three values stated without in-entry derivation (line numbers 59 and 97, and the line-5 lede quote) with a Q11 decision row that over-claims their derivations, and one false registry sentence ("no SWGDE row exists in `corpus/SOURCES.md`" — S003 and S005 are SWGDE rows).

Seat: R70W2AssimGateA (assimilation gate, addendum section 10, reviewer A) · 2026-10-25
Candidate: `.ufo/waves/round-70/w1/R70W1AssimDraft.draft-entry.md` (107 lines; judged as text; provisional ids S048/S049 noted below, not judged)
Bar applied: `corpus/QUALITY.md` Q01–Q15 · `PROVINCE.md` scope · `corpus/README.md` C07 (deepening of a held row)

## 1. What I re-derived myself (all commands run by this seat, 2026-10-25)

### 1.1 Fresh fetch — the digest pin still holds

Re-ran item 1's command (fresh `urllib` fetch of `https://raw.githubusercontent.com/onekey-sec/unblob/main/README.md`, bytes saved to my scratch):

```
bytes 7580
lines 235
sha256 6544d60f22f7b521f8705b3bba5d47a50e428ccbd3359542708dbd009ccf3716
```

Identical to the draft's item 1 (draft line 15). The recheck's precondition ("require the printed sha256 to equal `6544d6…` before reading items 2 and 3") is satisfied today, so the quotes were re-located against the pinned bytes.

### 1.2 Every located quote and anchor verifies byte-for-byte

From the fetched bytes (1-based lines):

```
L5   'unblob parses unknown binary blobs for **78+ archive, compression, and file-system formats**, …'
L20  '## Features'
L22  '- **78+ supported formats** — archives, compression streams, and file systems including SquashFS, JFFS2, UBI/UBIFS, ext, CPIO, ZIP, 7-Zip, gzip, XZ, LZMA, LZ4, and many more. See the [full list](https://unblob.org/formats/).'
L35  '## Installation'
L37  '### pip (recommended for most users)'
L46  'sudo apt install android-sdk-libsparse-utils e2fsprogs p7zip-full unar zlib1g-dev liblzo2-dev lzop lziprecover libhyperscan-dev zstd lz4'
L59  'unblob --show-external-dependencies'
L91  '### From source'
L97  'uv run unblob --show-external-dependencies'
L100 'Requires Python ≥ 3.10, [uv](https://docs.astral.sh/uv/), and a Rust toolchain (for the compiled extensions).'
L161 '  --show-external-dependencies    List required external tools and their status.'
```

Counts re-derived with item 3's parsing: `named_families 11` (SquashFS JFFS2 UBI/UBIFS ext CPIO ZIP 7-Zip gzip XZ LZMA LZ4), `apt_packages 11`, `flag_occurrences 3` — all three match item 3's printed output. Item 4's locator is also correct: line 100 is the `### From source` subsection's last content line (line 101 blank, line 102 `---`, then `## Usage`).

### 1.3 Fresh probe — items 6–7 reproduce exactly

`/home/vgpnk/.local/bin/unblob` (pre-existing on this host; no install performed by this seat):

```
unblob_version 26.6.4 | rc 0
deps_exit 1
deps_rows 15
deps_found 5
deps_missing 10
deps_names 7z debugfs fsck.erofs jefferson lz4 lziprecover lzop partclone.restore sasquatch sasquatch-v4be simg2img ubireader_extract_files ubireader_extract_images unar zstd
missing_names fsck.erofs jefferson lziprecover lzop partclone.restore sasquatch sasquatch-v4be ubireader_extract_files ubireader_extract_images unar
```

Identical to draft items 6 (lines 47–56) and 7 (lines 58–63), including the found/missing split.

### 1.4 Provenance and registry checks

- Package entry exists: `/home/vgpnk/Projects/shokuknow/merge/revenger/knowledge/corpus/knowledge/digest-scope-versus-provenance-amendment-2026-10-23.md` (campaign tree, read-only). Its claims 3, 4, 5 are the unblob format-count, implementation-language and external-extractor claims the draft retains; its claims 1, 2 are the SWGDE half (12-F-003-2.0 competency framework; 18-F-002 "should" vs 18-F-003 "shall"). The draft's retention set matches the source.
- Claim 1's SWGDE document (12-F-003-2.0, Core Competencies for Mobile Device Forensics) has no row in the lane registry: `grep '12-F-003|Core-Competencies' corpus/SOURCES.md` → no matches.
- The two superseded figures have no lane rows: `grep 'FSTM|300\+|以上' corpus/SOURCES.md` → no matches. The draft's no-supersede rationale (Unknown, 4th bullet) verifies.
- C07 row confirmed: `corpus/README.md:43` — `C07 | firmware images | knowledge/round-64-firmware-region-byte-evidence.md … | held`. The draft's coverage-map (line 5: deepening, not a flip, no status change) is consistent with the frozen claims.md assimilation section ("never as a README flip").
- PROVINCE scope: unblob is a named host engine (`PROVINCE.md` "Binwalk/Unblob"); firmware-extraction tooling bearing on the shipped-artifact evidence ledger is in province. In scope.
- Registry ids: S048 and S049 are already taken (`corpus/SOURCES.md:62` DEX spec re-fetch, `:63` REA android-applications reference), so the draft's "next unused after S047" parenthetical is false about this lane — per the assignment these ids are renumbered by document at admission, so I judge the text, not the ids; recorded, not scored.
- Snapshot: `corpus/snapshots/` holds APPNOTE.TXT, dex-format.html, rea-android-applications.md, ResourceTypes.h — no `unblob-README.md`. The draft discloses this and makes it a landing requirement (Limitation, 1st bullet; recheck, last sentence); recorded as a landing condition, not a draft defect.

## 2. Failing criteria — located defects

### Q02 — FAIL (header anchors/recheck do not locate the evidence)

The S049 anchor, verified-at, recheck and Scope all point the probe at items 4 and 5; items 4 and 5 are prose claims with no command and no stdout. The probe commands are items 6 (draft lines 47–56) and 7 (lines 58–63) — as the draft's own Q01/Q03/Q04/Q05 rows correctly say ("items 6-7", draft lines 89, 91, 92, 93). Four located instances:

- draft line 2 (S049 `source:`): "anchor: the two commands and their full stdout are items 4 and 5" — items 4/5 contain neither.
- draft line 3 (`verified-at:`): "item 4-5 ran the locally installed tool" — the tool ran in items 6–7.
- draft line 4 (`recheck:`): "item 4's command re-runs `unblob --version` and `unblob --show-external-dependencies`" — item 4 has no command; the executable recheck pointer is broken for the probe half.
- draft line 10 (Scope): "plus one probe of one locally installed unblob 26.6.4 on the same date (items 4 and 5)".

Q02 requires an exact anchor; an anchor that names prose items as the carrier of the commands and stdout does not locate the evidence. The S048 anchor (draft line 1) has a second, narrower instance: "every quote is located by item 2" — item 2 prints lines 22, 100, 46, 161 only, so the line-5 lede quote (draft line 33) is not located by item 2.

### Q11 — FAIL (values carried by prose only; decision row over-claims)

- Line numbers **59** and **97** are stated in item 5 (draft line 45: "as the command at line 59, as `uv run unblob --show-external-dependencies` at line 97") with no deriving command anywhere in the entry: item 2's output prints only (20, 35, 37, 91) and (22, 100, 46, 161); item 3's output prints no line numbers. Both values are correct (§1.2), so Q11's reject condition "a value is correct when re-derived but the entry carries no derivation" is met.
- The line-5 lede quote and its line number (draft line 33: "The same figure appears once more in the lede at line 5 (`78+ archive, compression, and file-system formats`)") likewise carry no derivation; I verified L5's text matches (§1.2).
- The Q11 decision row (draft line 99) then asserts: "every number carries its command and output inside the entry: … line numbers 20, 22, 35, 37, 46, 59, 91, 97, 100, 161 …" — false for 59 and 97 (no command prints them), and it omits line 5 entirely while the entry states it. A recorded value presented as command-derived.

### Located defect outside the Q table — false registry sentence

Draft line 10: "no SWGDE row exists in `corpus/SOURCES.md` and none is opened here." False as written: `corpus/SOURCES.md:17` (S003, SWGDE Minimum Requirements for Testing Tools 18-Q-001-2.1, tier A, mined) and `:19` (S005, SWGDE Best Practices for Computer Forensic Acquisitions 17-F-002-2.1, tier A) are SWGDE rows. The narrower intended claim — no row for the document claim 1 cites (12-F-003-2.0) — is true (§1.4), so the drop rationale survives under a corrected sentence, but the sentence as written misstates the registry. No numbered criterion catches a registry-existence sentence directly; recorded as a located defect the revision must fix.

## 3. Criteria that pass on my own re-derivation (no re-work needed)

Q01 (both sources are the right tier for their scope — docs tier A for the project's own stated figures, own-work tier A for that one run; no claim exceeds its quoted line — each quote verified verbatim in §1.2); Q03 (expected values from fetched bytes and from running the tool, not copied); Q04 (tool, version 26.6.4 as the tool prints it, function, own exit 1 and 15/5/10 scored; manual analysis labeled manual); Q05 (probe with command, date, observed exit and full output; no capability claimed); Q06/Q07 n/a (no fixture, no parser prediction — correct); Q08 n/a (superseded by Q11 — correct per QUALITY.md); Q09 (digest claimed for the hashed bytes only, explicitly not origin/completeness/authenticity); Q10 (scoped to one document, one host, one version; deepening not widening); Q12 n/a (no rejected-source row written — correct); Q13 (recheck credited only for what its run prints — substance correct; only the item pointer is broken, scored under Q02); Q14 (only hex string is the digest, no length claim in its clause — verified); Q15 (no git object id or tree identity stated — verified).

## 4. Flip condition (REJECT → ADMIT)

A revised draft that makes exactly these repairs, with no substantive figure changes (every figure already reproduces against the still-matching pin `6544d60f…`):

1. Re-point all four probe cross-references (draft lines 2, 3, 4, 10) from "items 4 and 5" to items 6 and 7.
2. Discharge Q11 for line numbers 59 and 97 and the line-5 lede quote: extend a printed command to emit them (e.g., add 5, 59, 97 to item 2's tuples) or label them recorded, and correct the Q11 row's list to exactly what the commands print.
3. Fix the S048 anchor (draft line 1) so "every quote is located by item 2" covers the lede quote, or drop the lede mention.
4. Correct the Scope sentence (draft line 10) to name the specific document: no row exists for SWGDE 12-F-003-2.0 (S003/S005 are SWGDE rows and are not it).

## 5. Residual risk and verification gaps

- The pin matched today, so quote locations were verifiable; if `main` moves before landing, the draft's own protocol (re-locate, don't re-use) applies and this gate's quote checks go stale.
- I did not run the lane's mechanical gates (`lint_entry.py`, `check_embedded_outputs.py`) over the draft — out of my scope; the draft is not a landed corpus file and the C1 gate conjuncts concern the C05 candidate, not this assimilation draft.
- Tooling record: no package installed or updated (pacman paused host-wide; no `uv`/`npx` install either). Used the host's existing `python3` and the pre-existing `/home/vgpnk/.local/bin/unblob` 26.6.4. Scratch `/tmp/revenger-r70-R70W2AssimGateA/` deleted before return.
- No file in the lane was edited; the wave-1 record (`.ufo/waves/round-70/w1/` beyond the candidate) was not read before this verdict was formed.
