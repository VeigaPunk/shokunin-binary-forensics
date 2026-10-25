PASS — 7 deletions identified (812 bytes, 2 of 273 lines), none of them a `$` block, a header key, a §Q-map row, or a clause any §Q-map row cites; the cut copy re-runs `checked_blocks=22 problems=0` (exit 0) and `LINT_QMAP=0; LINT_Q14=0; LINT_Q15=0; LINT_HEADER=0` (exit 0), so the frozen C1 conjuncts (`checked_blocks>=17`, lint exit 0) are untouched.

Seat: R70W1Simplify · round 70 wave 1 · target bytes = lane commit `aa1842fac199aa524930e5565ed3715de5f84c6d:corpus/knowledge/round-70-apk-axml-byte-evidence.md`
(`sha256sum` of the extracted copy = `0913f6515e93889a7a4204a613f52a3ff8d505742038dfa0d46443a79b088368`, 273 lines, 30350 bytes; the working-tree file hashed identical, so no drift during the run).

## Axes named
1. **Attack surface** — prose clauses that no command derives (each is a place a reviewer can plant a Q11/Q14/Q01 finding).
2. **Claim retention** — every clause a §Q-map row or the C1 predicate needs.
3. **Mechanical safety** — gate block count, lint classes, header keys, generator re-run.

## Method (cheap, in parallel, then measured once)
- Extracted the candidate bytes with `git show aa1842f:…` into `/tmp/revenger-r70-R70W1Simplify/`; all edits happened on `entry-cut.md` only.
- Baseline on the untouched copy, run from the lane root:
  `python3 -B corpus/check_embedded_outputs.py --entry /tmp/revenger-r70-R70W1Simplify/entry.md` → `checked_blocks=22 problems=0`, exit 0;
  `python3 -B corpus/lint_entry.py --entry …` → `LINT_QMAP=0 / LINT_Q14=0 / LINT_Q15=0 / LINT_HEADER=0`, exit 0.
- Applied the 7 deletions to `entry-cut.md` (`sha256 c0fb3013a038bb161fc0d4b1574146aca22f46cabf1804141f7597e83c52f147`, 271 lines, 29538 bytes) and re-ran both, same output as baseline; `grep -c '^\$ ' entry-cut.md` = **22** (no command removed; the frozen `C1_GATE … checked_blocks>=17` has 5 blocks of margin and loses none).

## Deletion list

**1. `entry:4` and `entry:152` — the APPNOTE *line-number* pointers (delete the numbers, keep the § numbers).**
Delete from `entry:4`: `(snapshot lines 387-398)` / `(lines 511-531)` / `(lines 632-646)`; delete from `entry:152`: `the layouts are APPNOTE snapshot lines 387-398, 511-531 and 632-646`.
Reason: these numbers are prose typed by hand, no command prints them, and **two of the three are wrong** (defect D-A/D-B below). The claim they serve — "the layouts are recorded from S032/S034, the widths manually transcribed, item 12 prints the sums" — is carried by `entry:4`'s remaining text (`the field widths are MANUALLY transcribed in corpus/fixtures/apk-r65/entry_checks.py and the item-12 command sums them`), by `entry:5` (S034 scope), by `entry:152`'s remaining `**manually transcribed** … The widths are recorded, the sums and the presence checks are derived:`, and by the item-12 block itself (lines 155-173, 14 `MATCH` lines). §4.3.7 / §4.3.12 / §4.3.16 plus the item-14 digest of `APPNOTE.TXT` remain an exact anchor for Q01/Q02.
Safety measured: gate 22/0, lint 0/0/0/0 on the cut copy.

**2. `entry:54`, second sentence (drop it; keep `…the table below is what it printed.`)**
`The numeric \`type\` values are decimal here: 1 is \`0x0001\`, 384 is \`0x0180\`, 256 is \`0x0100\`, 258 is \`0x0102\`, 259 is \`0x0103\` and 257 is \`0x0101\`:`
Reason: six hand-typed hex constants with no deriving command — the one place in the entry that contradicts `entry:1`'s own anchor clause `every S038 line number and enum value this entry states is printed by the item-11 command, none is typed by hand`. All six values are already printed by item 11 (`entry:132` `0x0001`, `:134` `0x0100`, `:136` `0x0101`, `:137` `0x0102`, `:138` `0x0103`, `:139` `0x0180`), and the type↔enum correspondence is carried as a *labeled inference* at `entry:234` (a). Deleting strengthens `entry:1` instead of weakening any Q row (Q01 cites S038, not this sentence; Q11 does not need prose arithmetic).

**3. `entry:61` — whole paragraph (2 sentences, plus its blank line).**
`Item 11 prints the S038 enum lines carrying those same hexadecimal values … It is an inference from matching values, labeled so in the inference section.`
Reason: pure restatement of inference (a) at `entry:234`, which is the labeled form of the same claim (`a printed chunk \`type\` value equals the value of the S038 enum line item 11 prints for the named constant`). The byte evidence is item 4's table (lines 57-59) and item 11's enum block (lines 132-139). The paragraph also carries a *coverage claim about item 11's output* ("prints … the start and end namespace types, the start and end element types") that goes stale if that block ever changes — deleting removes a maintenance coupling. No §Q-map row cites `entry:61` (checked by grep for `matching values`).

**4. `entry:86`, final sentence (drop it; the paragraph then ends `…at \`readout.py:22\` resolves to null).`).**
`The start-namespace chunk is printed as a separate fact and the readout does not consult it when resolving attribute namespaces:`
Reason: a *negative* code-behaviour claim that no command prints, and the weakest of the three D-candidates — Q07's basis (`entry:255`, `the namespace sentence in item 8 describes how this readout resolves this fixture, by the cited source lines`) is satisfied by the preceding sentence, whose pointer I verified: `grep -n 'strings\[ans\]' corpus/fixtures/apk-r65/readout.py` → `211:            "ns_index": ans, "ns": None if ans == NO_INDEX else strings[ans],` and `grep -n 'NO_INDEX = '` → `22:NO_INDEX = 0xFFFFFFFF`. The positive statement (direct pool indexing by `ns_index`) is the one that describes *how*; the deleted sentence only says what the readout ignores.

**5. `entry:15`, final sentence.**
`Nothing is extracted to disk, executed or fetched at recheck time, and no producer is called.`
Reason: the runtime-behaviour fence is already carried twice — `entry:235` (`the fixture is inert and no producer was called`) and `entry:243` (`this lane ran no provider and makes no readiness claim (Q05 fence)`); Q05's basis (`entry:253`) cites the S043-scope fence, not this sentence. The `**manual**` label that Q04 needs stays in the same paragraph.

**6. `entry:273` — delete the numeral `five` (`The five derivation flags are` → `The derivation flags are`).**
Reason: the list that follows has **six** flags — a false count in prose (defect D-C). The list itself is complete and every flag is exercised by a block (`--eocd` item 2, `--spec-quotes` item 11, `--zip-layout` item 12, `--oracle` item 13, `--pins` item 14, `--stdout-digest` item 15). Note `entry:9`'s `the five \`entry_checks.py\` flags named in items 11-15` is **correct** (5 in items 11-15; `--eocd` is item 2) — do not touch `entry:9`.

**7. (optional, lowest value) `entry:30`, clause `the second command reads those four bytes back from the archive at the printed offset`.**
Reason: the command line and its own output (`eocd signature bytes at offset 925: 504b0506 (4 bytes)`) are self-describing, and the eocd derivation Q11 needs is item 2's readout fact (`eocd_offset: 925`, `cd_end_equals_eocd_offset: true`), which stays. Safe but small: keep it if the author prefers the read-back command to be introduced in prose.

## Located defects found while testing the deletions (advisory, wave-1)
Both are the "prose pointer" class that killed v1-v4; the fix for D-A/D-B is deletion #1, which is why the two are listed together.

**D-A — `entry:4` and `entry:152`: §4.3.7 cited as `snapshot lines 387-398` omits the field item 12 checks.**
```
$ awk 'NR>=387 && NR<=399 {printf "%d: %s\n", NR, $0}' corpus/snapshots/APPNOTE.TXT
387:    4.3.7  Local file header:
389:      local file header signature     4 bytes  (0x04034b50)
…
398:      file name length                2 bytes
399:      extra field length              2 bytes
```
The record's 11 fields are lines 389-399; the cited range stops at 398, i.e. it excludes `extra field length`, and `entry:155-173`'s `MATCH local.extra_length: spec offset 28` rests on exactly that field. Fix by deletion (#1) or by correcting the range to 387-399.

**D-B — `entry:4` and `entry:152`: §4.3.12 cited as `lines 511-531` omits seven of the seventeen fields.**
```
$ awk 'NR>=511 && NR<=538 {printf "%d: %s\n", NR, $0}' corpus/snapshots/APPNOTE.TXT
511:    4.3.12  Central directory structure:
520:      File header:
522:        central file header signature   4 bytes  (0x02014b50)
…
531:        uncompressed size               4 bytes
532:        file name length                2 bytes
533:        extra field length              2 bytes
534:        file comment length             2 bytes
538:        relative offset of local header 4 bytes
```
The 46-byte central header (the sum `entry:157` prints: `central fixed part: 46 bytes`) spans lines **522-538**. The cited range ends at `uncompressed size`, so it excludes `name_length`, `extra_length`, `comment_length` and `local_header_offset` — the four offsets item 12 prints as `MATCH central.*` (lines 162-165). Correct range if kept: 511-538 (or 522-538 for the record only).
Also in the frozen script, same false numbers: `corpus/fixtures/apk-r65/entry_checks.py:47` `# (snapshot lines 387-398 section 4.3.7, 511-531 section 4.3.12, 632-646 section 4.3.16).` — deletion #1 does not fix that comment; it needs its own two-number correction or the false pointer survives in the file a reviewer will open next to item 12. (EOCD `632-646` is correct: heading 632, fields 634-646.)

**D-C — `entry:273`: `The five derivation flags` lists six.**
`grep -n '"--pins"\|"--eocd"\|"--oracle"\|"--zip-layout"\|"--spec-quotes"\|"--stdout-digest"' corpus/fixtures/apk-r65/entry_checks.py` → `195:    cmds = {"--pins": pins, "--eocd": eocd, "--oracle": oracle, "--zip-layout": zip_layout,` / `196:            "--stdout-digest": stdout_digest, "--spec-quotes": spec_quotes}` = 6 keys. Deletion #6 removes the false numeral; the list is right.

Pointers checked and **correct** (recorded so nobody re-litigates them): `readout.py:22` (`NO_INDEX = 0xFFFFFFFF`), `:76` (`sig_eocd = b"PK\x05\x06"`), `:105` (`payload_off = lh_off + 30 + lh_name_len + lh_extra_len`), `:164-168` and `:166` (`utf8=bool(flags & 0x100)`), `:203` (`aoff = base + 16 + …`), `:211` (`strings[ans]`), `:233-248` (dex block), `:49-50` (the "computed here … not assumed" comment `entry:239` disarms), `:51-58` (the widths table; 51-58 contains all six struct rows the sentence cites). Item 11's `four S045 phrases` (`entry:119`) matches the four `dex-format.html` MATCH lines at `entry:145-148`; item 15's `15 lines` matches the 15 facts the readout emits.

## Considered and deliberately NOT dropped (each would lose a needed claim or harm an axis)
- `entry:233` second sentence (`Items 3, 5 and 12 depend on recorded or manually transcribed widths, each labeled where it is used.`) — it is the qualifier on the Observation bullet; deleting it makes that bullet claim every value in items 1-15 is "printed by the command above it", which is false for the recorded APPNOTE widths → new Q11 exposure.
- `entry:239` last sentence (`Generalization to other APKs … would need its own evidence.`) — duplicates `entry:10`'s "Not covered", but it is a scope *hedge*; deleting it widens the apparent scope (Q10 axis), and hedges are the cheap side of the trade.
- `entry:70` (`The summed attr_ext_attribute_start 20 and attribute_size 20 are the values the start-element chunk states in item 8.`) — the only cross-check tying the manual transcription to observed bytes; Q04/Q11 defence.
- The whole `## Reproduce` section — dropping it removes the false count with it, but r69's spot-check V5/V6 punished operability harm; keep the section, drop only the numeral (#6).
- `entry:5` (S034) — it reads as a scoped duplicate of `entry:4` (S032) for §4.3.7, but the frozen C1 claim names the `S032/S034 anchor pins` and the SOURCES `used-by` rows key on S034; deleting a `source:` row is a bookkeeping change, not a prose simplification.
- `entry:256` (`Q08 | n/a | superseded by Q11…`) and `entry:260` (`Q12 | n/a`) — mechanically required: `lint_qmap` wants a non-empty decision for every `| Qnn |` row of QUALITY.md, and C1's predicate requires the full 15-row map.
- `entry:101` trailing `and nothing about dex program validity follows` — scoping fence at the claim site; `entry:235` carries it too, but a local fence is cheaper than a reviewer finding.

## Operability caveat for whoever applies this list
The entry is **generated**: `.ufo/waves/round-70/build-entry.py:16` `OUT = ROOT / "corpus/knowledge/round-70-apk-axml-byte-evidence.md"`, written at `:191`. The same prose lives in that template — `:49` (entry:4), `:60` (entry:15), `:72` (entry:30), `:84` (entry:54), `:88` (entry:61), `:104` (entry:86), `:126` (entry:152), `:184` (entry:273). Editing the entry alone will be reverted by the next `build-entry.py` run; edit the template and regenerate. (Repairs are outside my write scope — reported, not applied.)

## Tradeoff
Deleting #2 and #3 moves the chunk-type↔enum correspondence out of the prose and leaves it only as inference (a). That is the honest form — the matching is a reader-side inference, not a derived value — but a reader who never reaches the inference section loses the decimal→hex crib; the item-11 block still prints every enum value in hex, so the information is present, one hop further.
Deleting #1 trades a wrong locator for a coarser one (§ numbers + pinned digest instead of line numbers). If the L1 prefers line numbers, the correct values are 387-399 and 511-538, and `entry_checks.py:47` must move with them.

## Tooling / hygiene
No package installed or upgraded (host pacman paused; nothing needed — Python stdlib + the lane's own scripts sufficed). Lane and fleet repos untouched: all edits were on `/tmp/revenger-r70-R70W1Simplify/{entry.md,entry-cut.md}`, now deleted. No mutating git command was run (`git show`, `git status --porcelain`, `git -C <lane> cat-file` only).
