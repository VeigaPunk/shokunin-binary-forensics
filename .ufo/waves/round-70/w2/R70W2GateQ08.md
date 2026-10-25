PASS — the landed entry applies Q11 (its only Q08 reference is the truthful `n/a` supersession row), every embedded command reproduces its embedded output exactly (24/24 segments, 0 missing / 0 extra lines), and the only values Q08's older rule would have judged differently are precisely the labeled recorded/manual transcriptions that Q11 was written to permit.

# Seat R70W2GateQ08 — Q08 (superseded by Q11) gate decision, wave 2, landed bytes

Target: `corpus/knowledge/round-70-apk-axml-byte-evidence.md` at lane commit `17ee7f87ea8ee72a427af0fd8e7586d09bad99cd` (`admission-status: candidate`). Criterion: Q08 — superseded by Q11 — verify the entry applies Q11 (not Q08) and that its Q08 `n/a` row names the supersession truthfully; list any value Q08's older rule would have judged differently.

## Byte identity of what I judged

- Extracted `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive 17ee7f87ea8ee72a427af0fd8e7586d09bad99cd` to `/tmp/revenger-r70-R70W2GateQ08` and cross-checked against `git show`:
  `sha256sum corpus/knowledge/round-70-apk-axml-byte-evidence.md` → `819efcb8e2f6065c6b73456ed24502fe0b4e9751c94366e5a6c3f3b4990b4c31`;
  `git show 17ee7f87…:corpus/knowledge/round-70-apk-axml-byte-evidence.md | sha256sum` → `819efcb8e2f6065c6b73456ed24502fe0b4e9751c94366e5a6c3f3b4990b4c31` (identical).
- `diff <(git show 17ee7f87…:corpus/QUALITY.md) corpus/QUALITY.md` → clean; `QUALITY_LANDED_MATCHES_WORKTREE`. All QUALITY.md citations below are the landed bytes.

## 1. The supersession is real and the `n/a` row names it truthfully

- `corpus/QUALITY.md:23`: `| Q11 | Supersedes Q08. Each count, identifier, offset and digest in an entry carries, inside the entry, the command that derives it from the primary record (bytes, saved tool output) and that command's output. Constants such as header offsets are derived, not assumed. A value cited only to prose is labeled recorded, not re-derived. | …` — the newer row names the row it replaces, per QUALITY.md's own preamble rule ("Criteria are superseded by new rows that name the row they replace, never rewritten"). Q11's lesson set (M08, M09, M10, M20) is a superset of Q08's (M08, M09, M10).
- Entry line 305: `| Q08 | n/a | superseded by Q11 in `corpus/QUALITY.md`; the Q11 row below carries the decision. |` — pointer resolves to QUALITY.md:23, which says exactly that. Truthful.
- The entry applies Q11, not Q08: `grep -n "Q08" <entry>` returns only line 305 (the deferring `n/a` row); the operative decision is line 308 `| Q11 | pass | every count, offset, identifier and digest carries its deriving command and output in items 1-17; the recorded values (APPNOTE and AXML widths) are labeled manual where used; … |`. The Q-map holds all 15 rows Q01–Q15 (claims.md §C1's "full 15-row §Q-map").

## 2. Re-derivation — every embedded command run from the landed extraction

Script (`/tmp/revenger-r70-R70W2GateQ08/compare.py`, stdlib only) parsed all 17 fenced command blocks in the entry, ran each `$` command with `cwd` = the extraction root, and compared embedded lines with actual stdout:

```
command blocks found: 17
  [OK] python3 -B corpus/fixtures/apk-r65/readout.py --fact archive            (expected 1 lines, actual 1, extra 0)
  [OK] python3 -B corpus/fixtures/apk-r65/readout.py --fact eocd               (expected 1 lines, actual 1, extra 0)
  [OK] python3 -B corpus/fixtures/apk-r65/entry_checks.py --eocd               (expected 1 lines, actual 1, extra 0)
  [OK] ... member[AndroidManifest.xml] / member[classes.dex] / member[META-INF/MANIFEST.MF]  (1/1/1, extra 0)
  [OK] ... axml_chunk_table / spec_derived_struct_widths / axml_string_pool / axml_resource_map  (1 each, extra 0)
  [OK] ... axml_start_element / axml_start_namespace / axml_end_element / axml_end_namespace  (1 each, extra 0)
  [OK] ... dex_declared_header / jar_manifest                                  (1 each, extra 0)
  [OK] python3 -B corpus/derive_axml_anchors.py                                (expected 20 lines, actual 20, extra 0)
  [OK] python3 -B corpus/fixtures/apk-r65/entry_checks.py --spec-quotes        (expected 6 lines, actual 6, extra 0)
  [OK] ... --zip-layout (20/20)  --oracle (34/34)  --pins (10/10)  --stdout-digest (1/1)  --container (3/3)  --axml-layout (24/24)
TOTAL failing command segments: 0
```

24/24 command segments: every embedded line present in actual stdout **and** zero extra stdout lines — exact equality, not just the one-directional membership the gate checks (Q13's noted limit). Exit codes all 0.

Locator spot-checks (the entry's `readout.py:N` / `generator.py:8` citations), each read from the extraction: `readout.py:22` = `NO_INDEX = 0xFFFFFFFF` (item 8, entry line 86); `:49-50` = the "computed here … not assumed" comment (Limitations, entry line 288); `:51-58` = the `widths` dict (item 5); `:76` = `sig_eocd = b"PK\x05\x06"` (item 2); `:105` = `payload_off = lh_off + 30 + lh_name_len + lh_extra_len` (item 3); `:155-168` = string-pool decode with `:166` = `utf8=bool(flags & 0x100)` (item 6); `:203` = `aoff = base + 16 + attribute_start + i * attribute_size` and `:211` = `"ns": None if ans == NO_INDEX else strings[ans]` (item 8); `:233-248` = the dex header block (item 9); `generator.py:8` = "contains no classes and is not a valid dex program);" (Limitations). All ten accurate — no locator points at the wrong line.

## 3. Values Q08's older rule would have judged differently

Q08 (QUALITY.md, older row): "Every count, identifier and offset role is re-derived by command from its source record" — reject when "a count lacks its command, or an identifier or role label comes from memory." Q11 adds: a value cited only to prose is acceptable when **labeled recorded**, and adds digests to the list. The entry's recorded/manual values are exactly where the two rules diverge:

| # | Entry line | Value class | Q08 verdict | Q11 verdict (entry's) |
|---|---|---|---|---|
| a | 39 (item 3) | ZIP record widths and field offsets "**recorded** from APPNOTE … not derived from the archive" — the individual field widths behind the 30/46/22 sums and the spec offsets printed in item 12's MATCH lines (10, 12, 16, 28, 30, 32, 42; 14, 18, 22, 26, 28) | reject — each width/offset is a count/offset with no command deriving it from the APPNOTE snapshot bytes (item 12 sums transcribed values and prints line ranges; it does not derive the individual widths) | pass — labeled recorded |
| b | 63 (item 5) | S038 struct width lists (six structs, `readout.py:51-58`) — "**manual transcription** … labeled manual and not read from `ResourceTypes.h` at run time" | reject — the per-struct widths lack commands deriving them from the snapshot | pass — labeled manual |
| c | 152 (item 12) | "**manually transcribed** APPNOTE field widths"; "The widths are recorded, the sums, the line numbers and the presence checks are derived" | reject — same class as (a) | pass — recorded/derived split stated in the same sentence |
| d | 250 (item 17) | "a **second manual transcription** of S038's struct widths" | reject — same class | pass — labeled manual |

Secondary, arguable (listed for completeness; they turn on reading Q08's "identifier or offset role" broadly):

- `readout.py:N` line citations (76, 105, 51-58, 155-168, 166, 203, 211, 22, 233-248) and `generator.py:8` — line-number locators no command prints; entry line 282 says they are "source locators checked by reading the file". Under a broad Q08 reading these identifiers lack commands → would differ; under Q11 they are labeled locators (entry line 308) → pass. I verified all ten locators are accurate (§2), so the recorded label is honest either way.
- The `NO_INDEX` role label for `ns_index` 4294967295 (entry line 86, cited at `readout.py:22` — verified present). The value 4294967295 itself is command-printed (items 8, 13); only the sentinel's name is a locator-cited recorded label. Broad Q08 → role label not command-derived → would differ; Q11 → labeled locator → pass.

No value runs the other way (Q08 more lenient than Q11): Q11's addition of digests costs nothing here — every digest in the entry is command-printed (items 1, 3, 14, 15); none is prose-only.

## 4. No recorded value is presented as re-derived (Q11's reject clause)

Items 3, 5, 12, 17 each carry the recorded/manual label in the sentence that uses the values (lines 39, 63, 152, 250); the observation bullet (line 282) states the general rule and immediately carves out "Items 3, 5, 12 and 17 depend on manually transcribed widths, each labeled where it is used". Item 5's widths do appear inside a command's output, but the entry states their provenance honestly ("the readout prints the constants and their sums" — the readout's own hardcoded transcription, "not read from `ResourceTypes.h` at run time"), so the printed output is not mistaken for a derivation from the spec bytes.

## Verdict

**PASS** for criterion Q08-superseded-by-Q11 on the landed bytes: the entry applies Q11 (line 308 pass, line 305 truthful `n/a` deferral, no other Q08 use), the supersession pointer resolves to `corpus/QUALITY.md:23` which names Q08, and the divergence list (a)–(d) plus the two arguable locator/role-label cases is exactly the recorded-value class Q11 introduced — no value is mislabeled, no derivation is missing where Q11 requires one.

Residual risk: I judged only this criterion; the truth of the Q11 pass row's full sweep is the Q11 seat's decision (my §2 and §4 evidence supports it but does not replace that seat's independent sweep). The two arguable cases in §3 depend on how broadly "offset role" is read; under the narrow reading Q08 and Q11 agree everywhere and the list is (a)–(d) only.

Scratch `/tmp/revenger-r70-R70W2GateQ08` deleted before returning. No lane file was edited; no mutating git command was run.
