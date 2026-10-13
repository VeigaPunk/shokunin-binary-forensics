# r59-devin non-author verifier report — named type key `REVTEST` leg

Host: devin. Verifier did **not** author this round. Scope: independent
re-derivation, independent byte oracle (own parser, not the author's
`verify.py`/`truth.json`), REA rerun, and forge challenges of
`corpus/fixtures/pe-r59d/` + `corpus/live/runs/round-59/devin-author/`.
No commits, no LOG/SCORECARD writes, no verdict marking, no author
artifacts modified. All scratch work under `/tmp/r59v/`.

## Commands run

1. `mkdir /tmp/r59v/fixtures/{pe-r55,pe-r59d}`; copied `pe-r55/fixture.exe`
   and `pe-r59d/build_fixture.py` into the scratch tree (script reads
   `../pe-r55/fixture.exe` relative to itself), then
   `python3 build_fixture.py` → `wrote fixture.exe sha256=99bebcf1… size=1536
   dir_size=320`.
2. `cmp` rebuilt `/tmp` fixture vs `corpus/fixtures/pe-r59d/fixture.exe` →
   **BYTE-IDENTICAL**; `diff` of regenerated `truth.json` → identical.
   Deterministic rebuild confirmed. (Note: `devin-author/` contains no
   `fixture.exe`; the fixture lives in `corpus/fixtures/pe-r59d/` — the
   dispatch prompt's mention of a `devin-author/` fixture.exe resolves to
   that path.)
3. Own decoder `/tmp/r59v/my_oracle.py` (stdlib struct only, written from
   the PE/COFF spec, separate code path from the author's oracle):
   MZ/PE32+ magic 0x20B, machine 34404, resource data-directory @216 =
   rva 8192 / size 320 → file base 512; full three-level traversal.
4. `python3 …/devin-author/verify.py` → exit 0:
   `PASS: 22 positive checks; 3/3 forged claims rejected`.
5. `npx -y rea-agents@6.4.0 inspect-pe-resources <path> --format json` on
   (a) my `/tmp` copy and (b) the original fixture path (read-only inspect).
6. Three controlled one-byte mutants in `/tmp` + REA/oracle on each.

## Byte facts (independently derived, agreeing with author)

- Fixture: 1536 B, sha256
  `99bebcf14c462075e63d6504c97a45267063f33e05f215c1235f89d666b5c0f3` ✓
- Root dir @512/40: `named_entries=1, id_entries=2` — the ONLY authored
  fixture with a named root entry. Verified across all 29 `pe-r*` fixtures
  (16 PE32+ + 13 PE32; every other root has `named_entries=0`). Coverage
  novelty claim holds.
- 4 leaves, exactly as claimed:
  - idx0: type `{"kind":"name","name":"REVTEST"}` utf16le
    `5200450056005400450053005400` @812/16; name id 1; lang 1033; entries
    [528,632,728]; data entry @784; payload rva 8648 @**968**/23 B, sha
    `d069b3846e5c…91da6` ✓
  - idx1: type 3, id 1, lang 1033; @**832**/48 B, sha `d7aaca7b…` ✓
  - idx2: type 3, id 2, lang 1033; @**880**/48 B, sha `2f503cac…` ✓
  - idx3: type 14, name `A😀B!` utf16le `41003dd800de42002100` @800/12;
    @**928**/34 B, sha `45eb7031…` ✓
- icon_groups[0]: resource_index 3; images id1→candidates [1], id2→[2],
  same-language [1,2], size_matches [true,true]; named-type leaf idx0 is
  never a candidate. 2/2 links, zero false links ✓
- Directories: **8** byte-derived (root + 3 type/name-level + 4
  language-level: @512,616,712,552,640,664,592,688) — agrees with REA's
  saved 8-entry array and verify.py's full-array compare.
- coverage field: `complete`, examined_entries 11 (= 3+1+2+1+4 entries) ✓

## REA rerun / evidence_id

- Original path rerun: evidence_id **`ev_8efa2368e77f…` reproduced
  exactly**; stdout byte-identical to saved `inspection.raw.json`
  (sha256 `e04b14ef…` = receipt claim). normalized_result, subject,
  provider, parameters all equal — the saved evidence is fully
  reproducible under the recorded command.
- **Correction to the "content-addressed" framing**: same bytes at a
  different path (`/tmp/r59v/…`) yield a *different* evidence_id
  (`ev_50038b96556f…`). The id is deterministic over content **and**
  path/parameters, not over content alone. Author's claims did not assert
  path-independence, so no author claim is falsified — but "content-
  addressed" should be read as "command-input-addressed".

## Forge-checks (independent of author's verify.py)

- Author `verify.py` rerun: exit 0, 22 positive checks, 3/3 in-memory
  forgeries rejected (REVTEST-as-icon-candidate, numeric type-id 24,
  forged payload digest).
- Mutant A (my copy, byte 814 `R`→`X`): REA exit 0 reports leaf0 name
  `"XEVTEST"`; my oracle independently decodes `"XEVTEST"`; a forged
  `"REVTEST"` claim and the saved normalized_result both reject. New
  evidence_id `ev_97b6e141…`.
- Mutant B (byte 968 payload flip): REA exit 0 reports payload sha
  `76c4c981…` ≠ saved `d069b384…`; forged saved-sha claim rejected. New
  evidence_id `ev_6c1ab6df…`.
- Mutant C (byte 812 name length 7→200, string would overrun the declared
  resource interval): REA **refuses**, exit 1, `invalid_format`:
  "Resource directory offset leaves the declared resource interval."
  This resolves one of the author's own UNKNOWNs for this case: REA does
  bounds-check name strings against the directory interval.

## Disagreements / notes

1. **Minor prose error in author report**: "Directories 7/7 byte-derived"
   — the actual count is **8/8** (8 directories in fixture bytes and in
   REA's saved array; verify.py compares all 8 and passes). Precision of
   the underlying comparison is unaffected; only the reported count is
   off by one.
2. evidence_id is path-sensitive (see above) — not a falsification of the
   author, but worth recording against the "content-addressed" shorthand.
3. No `fixture.exe` exists under `devin-author/` (dispatch wording);
   fixture is at `corpus/fixtures/pe-r59d/fixture.exe`.

Everything else — determinism, all leaf offsets/sizes/digests, REVTEST
name-keyed type dir, group links, receipt/stdout hashes, coverage
novelty, and verify.py exit 0 — **agrees** with the author.

## UNKNOWNs (verifier's own, not re-litigated from author)

- Named type keys with other type ids, duplicate/overlong-but-in-bounds
  names, name-level (level-2) named keys under a named type, non-ASCII
  type names; Windows loader semantics; PE32 (non-plus) named-type
  behavior; producer authentication (receipt proves saved-file
  consistency only, per standing doctrine); whether REA's interval check
  covers all overlong-name placements beyond offset 812.
