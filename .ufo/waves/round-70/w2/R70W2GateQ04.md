FAIL — Q04, two located v5 sentences describe a command's output as something it does not print (entry:119 "prints the raw line…" and entry:152 "the last three lines print…"), each contradicted by the command's own stdout that the entry itself embeds.

Seat `R70W2GateQ04` · fresh wave-2 seat (no wave-1 seat's report read before this verdict was formed; the w1 cross-check is at the end, after the decision) · criterion in scope: **Q04 only**.

## Bytes judged (pinned)

- Lane commit `17ee7f87ea8ee72a427af0fd8e7586d09bad99cd`, entry `corpus/knowledge/round-70-apk-axml-byte-evidence.md`
  — blob `6b8f05e8af9d458713d20f4e3d1e89f97f7fd9da`, sha256 `819efcb8e2f6065c6b73456ed24502fe0b4e9751c94366e5a6c3f3b4990b4c31`, 322 lines,
  `admission-status: candidate` (entry:9).
- Frozen counters re-verified: `sha256sum reports/round-70/measure.py` → `488f95aa1d502cbb20b7303e1d773f0101397a0bd45cee69c9fb389651c88c76`;
  `reports/round-70/measure-a1.py` → `96feeaa048f0f2b8ab0f3bb183c714a57ff41e951d4221c09806b6acf2e87191` (both as frozen).
- Extraction: `git -C …/revenger-shokunin archive 17ee7f87… | tar -x -C /tmp/revenger-r70-R70W2GateQ04` (scratch).
  No lane file was written, edited or mutated; every command below ran read-only against that extraction.

## Reproduction of every credited command (ground for the decision)

Parsed all `$` blocks independently from the extracted bytes and re-ran each command from the extraction root:
**17 fenced groups / 24 distinct commands, 24/24 exit 0, every embedded output line present verbatim in the actual stdout, zero missing, zero extra.**
Independent cross-checks:

- item 15: `python3 -B corpus/fixtures/apk-r65/readout.py` → `15` lines, sha256 `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` = the embedded line at entry:238.
- item 12 output ordering: `python3 -B corpus/fixtures/apk-r65/entry_checks.py --zip-layout | nl | tail -6`
  ```
      15	MATCH local.extra_length: spec offset 28, readout.py literal `u16(apk, lh_off + 28)` present=True
      16	MATCH APPNOTE 4.3.7: heading line 387, transcribed field lines 389-399
      17	MATCH APPNOTE 4.3.12: heading line 511, transcribed field lines 522-538
      18	MATCH APPNOTE 4.3.16: heading line 632, transcribed field lines 634-646
      19	MATCH central.fixed_part: spec width 46, readout.py literal `cursor + 46` present=True
      20	MATCH local.fixed_part: spec width 30, readout.py literal `lh_off + 30` present=True
  ```
  (`wc -l` = 20 lines.)
- gate/lint on the extracted entry: `python3 -B corpus/check_embedded_outputs.py --entry …` → `checked_blocks=24 problems=0`, exit 0;
  `python3 -B corpus/lint_entry.py --entry …` → `LINT_QMAP=0 / LINT_Q14=0 / LINT_Q15=0 / LINT_HEADER=0`, exit 0.

## Located defects (Q04)

### D1 — entry:119 (item 11) credits `entry_checks.py --spec-quotes` with printing a raw snapshot line; it prints a line **number** and the author-supplied **phrase**

Entry:119, verbatim tail: "The second command locates each quoted spec phrase (S038's `attributeStart` comment, S049's route sentence, four S048 phrases) in its committed snapshot copy, tags stripped and whitespace folded, and prints the raw line the phrase's first words start on:"

Actual output (item 11 block, entry:143-148), first line:

```
MATCH ResourceTypes.h: first line 686, folded phrase present=True: Byte offset from the start of this structure where the attributes start
```

- The printed artifact after `present=True:` is the `phrase` variable, not a snapshot line: `corpus/fixtures/apk-r65/entry_checks.py:292` is
  `print(f"… first line {line}, folded phrase present={present}: {phrase}")`, and `phrase` comes from the module's own `SPEC_QUOTES` table (author text).
- The raw line it claims to print is different bytes: `sed -n '686p' corpus/snapshots/ResourceTypes.h` →
  `    // Byte offset from the start of this structure where the attributes start.` (leading spaces, `//`, trailing period — none of which appear in the printed text).
- What the command does print, correctly, is the *number* of the raw line whose folded text contains the phrase's first three words (`first = " ".join(phrase.split()[:3])`, `entry_checks.py:290-291`), plus the folded-presence boolean.

So a tool is credited with an output it did not produce (a raw snapshot line), and author-supplied phrase text is presented as snapshot output — the M02 class Q04 cites (`corpus/lessons/round-1.md:39`).

**Smallest safe correction** (no value changes; entry:119 tail): "…in its committed snapshot copy, tags stripped and whitespace folded, and prints, for each phrase, the number of the raw snapshot line whose folded text contains the phrase's first three words, the folded-presence boolean, and the phrase it searched for:".

### D2 — entry:152 (item 12) says the "last three lines" print the snapshot record-layout positions; the last three lines are APPNOTE 4.3.16 plus two fixed-part lines

Entry:152, verbatim: "…and each is compared with the literal in the readout source; the last three lines print where each record layout sits in the snapshot (heading line and the first and last transcribed field lines)."

Actual `--zip-layout` output is 20 lines (above): the three APPNOTE layout lines are output lines **16-18**; the last three lines are **18** (APPNOTE 4.3.16), **19** (`central.fixed_part`), **20** (`local.fixed_part`). Two of the three "last three lines" do not print a record-layout position. The entry's own embedded block contradicts the sentence at entry:171-175, so no re-run is needed to see it.

**Smallest safe correction** (entry:152 clause): "…and each is compared with the literal in the readout source; the three APPNOTE lines (output lines 16-18 of 20) print where each record layout sits in the snapshot (heading line and the first and last transcribed field lines), and the final two lines print each record's fixed-part width:".

## What holds under Q04 (so the FAIL is scoped to D1/D2 only)

- **Item 3** (entry:39): "record widths and field offsets are **recorded** from APPNOTE and checked against the readout source by item 12, not derived from the archive" — label present and true (`entry_checks.py:53-64` are literal field-width tuples; item 12 prints `present=True` per literal).
- **Item 5** (entry:63): "a **manual transcription** of S038's struct field lists (`readout.py:51-58`), labeled manual and not read from `ResourceTypes.h` at run time" — true: `readout.py:51` is `w8, w16, w32 = 1, 2, 4` and `:52-58` the hand-written width dict; the Limitations paragraph (entry:296) additionally flags the readout's own misleading comment at `readout.py:49-50` and disclaims it. The r68 Q04-F2 defect (widths presented as derived) is repaired.
- **Item 16** (entry:244): "read from the archive bytes and compared with the oracle's declared method" — true: `entry_checks.py:252-270` unpacks flags/method with `struct.unpack_from` from the archive and prints `oracle method 0` per member.
- **Item 17** (entry:253): "compared with sums of a second manual transcription of S038's struct widths" — true: `AXML_WIDTHS` is labelled `MANUAL second transcription` (`entry_checks.py:202`) and offsets come from the running-sum helper `offsets()` (`:97-103`), whose printed offsets match the readout's literals.
- **Item 13** (entry:178): "`truth.json`, which `generator.py` emits" — independently reproduced: copied `generator.py` alone into scratch and ran it → `fixture.apk 947 bytes sha256 05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e`; resulting `fixture.apk` `05d2280f…` and `truth.json` `27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173` equal the item-14 pins.
- **Script credits are bounded**: item 11's derivation credit ("bounded to exactly the lines it prints") holds — every S038 line number and enum value the entry states (six type↔hex correspondences, `attributeStart` comment 686 / field 687) appears in the printed 20-line derivation; the recheck line credits the gate only for "every embedded line in its stdout" (verified: `checked_blocks=24 problems=0`) and `verified-at` credits `build-entry.py` with pasting stdout, which that script does (`subprocess.run` + paste, `.ufo/waves/round-70/build-entry.py:25-37`).
- **Manual labels**: the Scope paragraph (entry:19) labels the analysis manual; no third-party tool is credited with any result; no version/function is generalized (Limitations, entry:296).

## Residuals (advisory, not part of this FAIL)

1. The interpreter is named only as `python3`; no version is printed. All reproductions above ran on **Python 3.14.8**. The three own-work scripts are digest-pinned (item 14), which is stronger than a version label for byte identity, but Q04's letter asks for "version".
2. `generator.py:8` is cited for "not a valid dex program" (entry:296); the phrase is on `generator.py:10` (the `classes.dex` bullet spans `:8-10`). Locator start, not a false result.
3. The §Q-map Q04 row (entry:301) says "no tool claim" — contradicted by D1/D2's existence, but a §Q-map row is never evidence for this criterion and was not used here.

## Cross-check with wave 1 (read only after the verdict above was fixed)

`R70W1PreQ04Q13.md` reviewed the **pre-repair** bytes `aa1842fac199…` (22 blocks) and passed Q04 with an advisory D1 of its own: the item-12/S032 APPNOTE ranges `387-398` and `511-531` did not cover the transcribed fields. In the landed bytes those ranges are gone (entry:152 states none) — but the repair replaced them with D2's false "last three lines" sentence, and v5 added D1's false "raw line" sentence. Both of my defects are therefore v5-introduced, not inherited from v4 (`corpus/knowledge/round-69-apk-axml-byte-evidence.md` has neither sentence; item 11 there carried only the derivation). Its other check (28 MATCH lines in item 13) is consistent with my count of 34 oracle lines on the landed bytes.

## Kill-rule status

Per `reports/round-70/claims.md` §C1: "Any wave-2 Q FAIL carrying a located defect (path:line + the deriving command's output) falsifies C1." D1 and D2 each carry a path:line, the command whose output shows it, and a corrected sentence; both are inside the items my mandate names (item 12 explicitly, item 11 as a script credit). Under the frozen landing order the C05 row stays `uncovered` and the entry takes `admission-status: rejected` with every other byte kept — unless the L1 shows by command that the cited text is absent from the landed bytes **and** a second fresh reviewer seat concurs in writing (entry:119 and entry:152 are present verbatim, so that path is closed on the bytes I judged).

## Environment / tooling

Python 3.14.8 stdlib only (`python3 -B`), GNU coreutils `sha256sum`, `git show`/`git archive` read-only. No package installed or upgraded, no pacman transaction attempted, no `uv`/`npx` install. Scratch `/tmp/revenger-r70-R70W2GateQ04` deleted before return; the only file written is this report.
