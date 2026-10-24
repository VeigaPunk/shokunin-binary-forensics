# W2AttackEntryQ01 — C1 §Q01 attack (attempt 1)

Seat: `revenger-r63.W2AttackEntryQ01` · lane tip attacked: **db55bd6488e24e956df5818ae34c2a043d7ddc12** (committed bytes; claim file and `corpus/SOURCES.md` are unmodified in the worktree — `git diff --stat HEAD` empty for both).
Claim under attack: `corpus/knowledge/round-63-zip-central-directory-evidence.md` (C1, C06 archives).
Frozen rule: `corpus/QUALITY.md:13` — Q01: each load-bearing claim rests on a `corpus/SOURCES.md` row that is tier A **for that claim's scope** and was opened in the round that wrote it; failure mode "the claim exceeds what the cited text states".
Frozen contract: `reports/round-63/claims.md:19-40`.

## Verdict

**Q01 FAIL as committed.** The ten §Sources quotes are each present verbatim (word-sequence) in the cited APPNOTE sections of the pinned snapshot — quotes pass. The row grounding fails: two load-bearing scopes are outside the committed rows.

1. **Blocking — S032 row scope omits the local file header (§4.3.7), which the entry uses load-bearingly and claims the row covers.** `corpus/SOURCES.md:46` scope: "central directory file header and end-of-central-directory record field layout for one authored ZIP archive: signature values, field order, length fields, CRC-32 and local-header offset"; anchors: `§4.3.3, §4.3.12, §4.3.16, §4.4.7, §4.4.10-4.4.12, §4.4.16, §4.4.21-4.4.22` — **no §4.3.7**. The entry:
   - line 1 asserts S032 scope is "the local file header, central directory file header and end-of-central-directory record field layout" with anchor "§4.3.7 (local file header, fixed field-width list)";
   - item 5 (line 67) derives the **30-byte** local-header fixed part and name/extra-length offsets **26/28** expressly "S032 §4.3.7";
   - items 8/9 use those widths for payload offsets **42** and **2750**, and the readout bakes the §4.3.7 table in (line 471 "offsets COMPUTED from the §4.3.7 widths"; line 616 `"source_anchor": "APPNOTE 6.3.10 §4.3.7, §4.3.12 and §4.3.16 field tables (S032)"`);
   - line 221 (limitation 31), line 655 (§Sources) and line 697 (the entry's own Q01 decision) all say S032's scope is "the three fixed records' field layout". The committed row says two records plus a CD field ("local-header offset" = §4.4.16, not LFH layout).
   The frozen contract agrees with the row, not the entry: `reports/round-63/claims.md:33-34` describes S032 as "central directory / EOCD field layout". So item 5's LFH trio, items 8/9's payload offsets and item 17's inference basis rest on a section outside the row's declared scope and anchor list, and the entry's description of its own row is false as committed. This is exactly Q01's failure mode (cited authority narrower than the claim). The APPNOTE text itself is present and correct (see below), so the fix is a row amendment, not an entry rewrite.
2. **Medium — S033 row source list omits `LEDGER.md`, which the entry cites as S033 and prints a digest for.** `corpus/SOURCES.md:47` source column lists only `fixture.zip`, `truth.json`, `artifact-inspection.json`; added scope is "central-directory-to-oracle-to-saved-record correspondence". The entry line 2, the §Sources bullet (line 656) and item 2 (lines 35/44) include `corpus/live/runs/20261012T164246Z/LEDGER.md` (sha256 `05042a55…e6cb`) as an S033 source; limitation 29 (line 217) credits the run via that ledger. No other row covers it (`grep LEDGER corpus/SOURCES.md` → only unrelated S013). The ledger byte-identity assertion therefore rests on no row.
3. **Corroborating integrity defect (not the Q01 basis, Q11-adjacent).** In §Reproduce (lines 284-308) the claimed exact output for `printf '%s\n' "local file header signature 4 bytes (0x04034b50)" | wc -w` is **8** (line 292); re-run actual is **7**. The other nine of ten counts match (7/21/10/8/23/24/20/23/12). The block does contain ten invocations as the Q11 inventory (line 685) says, but that one printed output is false; it does not breach the ≤25-word bound.

If L1 amends `corpus/SOURCES.md:46` to add §4.3.7 / "local file header field layout" to scope and anchors, adds `LEDGER.md` to S033's source list (or drops LEDGER from the entry's S033 line/item 2/limitation 29), and fixes the one wc output, Q01's grounding defects are closed; the quote layer needs no change. Amended bytes must be re-attacked.

## Evidence — quote verification (PASS)

Snapshot identity: `.ufo/waves/round-63/source-snapshots/appnote.txt`, `sha256sum` = `0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6` (matches the pinned digest), `wc -c` = **174585**; tracked at HEAD (`git ls-files` lists it). Provenance: `appnote.provenance.json` access_date 2026-10-23, spec_version 6.3.10, spec_revised Nov 01 2022, status header lines 2-4 ("Version: 6.3.10 / Status: FINAL - replaces version 6.3.9 / Revised: Nov 01, 2022") — the entry's "version 6.3.10, FINAL, revised Nov 01 2022" is grounded.

Each quote was checked **inside its cited section** (section spans cut at heading→next heading; whitespace-normalized, since the snapshot is CRLF with column padding). 10/10 found:

| cited | section lines | words | quote (start) | result |
|---|---|---|---|---|
| §4.3.7 | 387-400 | 7 | local file header signature 4 bytes (0x04034b50) | PASS |
| §4.3.7 | 387-400 | 10 | file name length 2 bytes extra field length 2 bytes | PASS |
| §4.3.12 | 511-539 | 7 | central file header signature 4 bytes (0x02014b50) | PASS |
| §4.3.12 | 511-539 | 21 | crc-32 4 bytes compressed size 4 bytes … | PASS |
| §4.3.16 | 632-650 | 8 | end of central dir signature 4 bytes (0x06054b50) | PASS |
| §4.3.16 | 632-650 | 23 | total number of entries in the central directory on this disk … | PASS |
| §4.4.7 | 900-920 | 23 | If bit 3 of the general purpose flag is set, this field is set to zero … | PASS |
| §4.4.7 | 900-920 | 12 | value is put in the data descriptor and in the central directory. | PASS |
| §4.4.16 | 981-989 | 24 | This is the offset from the start of the first disk … local header SHOULD be found. | PASS |
| §4.3.3 | 348-351 | 20 | All values MUST be stored in little-endian byte order … | PASS |

Caveat on "verbatim": no multi-field quote is byte-contiguous in the raw snapshot (raw `str.count` = 0 for 7/7 tested) because APPNOTE pads columns and wraps lines; they are verbatim at the word-sequence level after whitespace normalization. This is the reading the entry's own ≤25-word framing implies, and it is not a Q01 defect.

Derivation cross-check (Q01 scope aside): §4.3.7 widths sum to 30 (4+2+2+2+2+2+4+4+4+2+2) with name length at 26 and extra at 28; §4.3.12 sums to 46 with crc at 16 and relative offset at 42; §4.3.16 sums to 22 with the two entry counts at 8 and 10. The numbers the entry attributes to the spec's tables are correct.

## What each finding attacks

- Finding 1 attacks **C1 coverage K / Q01** directly: the entry's own declared scope for S032 is wider than the committed row's, so the LFH-derived observations are ungrounded at row level even though the spec text exists.
- Finding 2 attacks **C1/Q01 provenance** for the ledger digest and limitation 29, one row short.
- Finding 3 attacks the **§Reproduce evidence layer** (the "command and exact output" claim), not Q01 grounding; it undermines confidence that quoted counts were re-run but leaves the quote set intact.

## Residual risk and verification gaps

- **No target execution** (wave rule): I did not run `readout.py`; numeric observations (2942/2828/114/2668/16160/…) are taken from the entry and only the *derivation* sums above were cross-checked against the spec tables. Q01 does not require re-execution; Q04/Q11-Q13 owners cover it.
- **Scope judgment is against committed bytes only.** `corpus/SOURCES.md` and the entry are clean versus HEAD; if L1 amends the rows, this verdict's basis changes and a fresh attack is required.
- **Contract/registry drift, flagged for L1 (outside the entry's Q01 basis):** `reports/round-63/claims.md:34` says S033 is "Python zipfile docs", while the committed registry S033 is the own-work archive/oracle/record row and the entry screens out the zipfile docs with "no row is needed". The entry is consistent with the registry; the frozen claim sentence is stale and should not be used to judge Q01.
- **Not checked here:** the lesson `## Gate`/Q01 sentence wording, Q02-Q13, S032/S033 byte re-opening (other seats: `W2ReopenS032`, `W2ReopenS033`, `W2ClaimsAdmission`), and the K probe count. Admission requires named Q01-Q13 passes; a Q01 FAIL blocks C1 admission until amended rows are re-reviewed.
- **Tooling:** no installs or updates. Used system `python3 3.14.8`, `git 2.56.0`, `sha256sum 0.8.0`, `wc`; no network, no pacman (host pause respected), no model arguments.

## Open decisions named by this seat

- **Q01: FAIL** (committed bytes db55bd6), grounds above. A later PASS requires: S032 row scope+anchors include §4.3.7/local file header; S033 source list includes `LEDGER.md` (or entry drops it); the one false wc output corrected; then re-attack of the amended bytes.

## Re-review at aaa0463 (corrected bytes) — Q01 PASS

Exact bytes attacked: lane tip **aaa046326d92ba983f3ae99341438c9b8509a6cc**; claim sha256 **285f641f4774a35f663c7ace731839e789c24d028cab1f455078df60fc9e56a1** (matches the handed digest); `corpus/SOURCES.md` sha256 `0605814564b8e522b3f7c5086646a7c1878acad6055c9f5bcf4b3ce1b2011514`; `git status --porcelain` empty for both files (worktree = HEAD).

Prior defects closed, each re-verified on the new bytes:

1. **§4.3.7 / local file header is now row-grounded.** `corpus/SOURCES.md:48` S034 — spec, tier A, scope "local file header record field layout", anchor §4.3.7, snapshot sha `0b9930…50cd6`, mined 2026-10-23. The entry line 2, item 5 (line 69), the readout comments (lines 363-364) and its `source_anchor` (lines 73, 256, 637-638) all cite **S034** for the LFH widths; S032 (SOURCES.md:46) is narrowed to CD/EOCD and matches its row; limitation 31 (line 223) splits the two. No §4.3.7 claim cites S032.
2. **LEDGER.md is now row-grounded.** `corpus/SOURCES.md:49` S035 — own-work, tier A, scope "recorded layer … cited for provenance only", sha `05042a55…e6cb`, 3959 bytes, mined 2026-10-23. Item 2 (line 28) and the §Sources bullet (line 681) cite S035; S033 (SOURCES.md:47) now matches the entry's fixture/oracle/record description.
3. **wc fix verified.** All ten printed `wc -w` outputs equal my re-run: 7/21/**7**/10/8/23/24/20/23/12 (former 8→7 at lines 306-309). No mismatch.
4. **New derived facts verified true.** `zipfile.html`: 139782 bytes, sha `9520a8cb…a270739` (lines 288-291) equals `wc -c`/`sha256sum`. `tr -d '\r' | head -5` (lines 297-303) matches the actual output byte-for-byte, including the trailing space after `Version: 6.3.10`. Item 2's four-file base-commit claim re-ran equal for all four files (`git show 55bcb6e1…:<path> | sha256sum` = worktree sha256 for fixture/truth/record/ledger).
5. **Quotes still pass.** 10/10 §Sources quotes are present in their cited sections of the pinned snapshot (in-section, whitespace-normalized); snapshot sha unchanged `0b9930…50cd6`, 174585 bytes.

**Verdict: Q01 PASS on these exact bytes.** Every load-bearing claim now rests on a tier-A row whose declared scope covers it; all four rows were opened 2026-10-23 (round 63). The §Sources quote set, the fixed counts and the new derived metadata are all reproducible as printed.

Residual lows (recorded; they do not overturn PASS):

- Entry lines 2 and 677 call S034 "superseding S032's narrower scope"; the landed S034 row says "Local-header layout scope **beside** S032". S032 remains cited for CD/EOCD, so "superseding S032" misdescribes the relation. Not load-bearing.
- Entry line 4 attributes S035's scope to "base commit 55bcb6e1…"; the landed S035 row pins "at commit db55bd6". I verified the ledger bytes are identical at both commits (`05042a…e6cb`, 3959 bytes), so no value is false — only the row description.
- Line 680 still says "Proposed registry row text for L1" for S034/S035 although both rows are landed at this tip, and it carries unresolved template tokens `{{R:spec_offsets}}`, `{{R:local_member_1}}`, `{{R:local_member_2}}`. Stale build artifact / publication defect, not source grounding.
- Payload offsets 42/2750 assume file data immediately follows the local header (§4.3.8 "Immediately following… SHOULD", not anchored in S034). The entry's own inflate + CRC-32 match confirms the boundary empirically, so the values do not rest on the unanchored clause.

Gap: I did not execute `readout.py`, so the new 17-line stdout digest `ccaffa322c49d1850fb7da86dc9221ea3bd73c8e3db81cc2ce9be6a1e5b40dc5` is taken as printed (Q04/Q13 owners re-run). No installs; tools unchanged.
