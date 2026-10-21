GRADE: BROKEN — corpus/knowledge/round-62-commonjs-require-name-evidence.md (C04 candidate), scope/inference/unknown attack

Seat `RevengerR61-2.R62FJsScopeUnknown` (fresh falsify, not author/corrector). Frozen revision
`d97761952be256d145d298022de03091de91d358` (claimbase `5bd4a90fc1a34caa94496601b60537b3aab12301`,
pre-registration `a3498e25ad87bf756288812d0ea7c474b09433c7`), extracted with `git -C <lane> archive d977… | tar -x`
into `/fast/scratch/hyaku/revenger-r62/R62FJsScopeUnknown/tree`. Candidate SHA-256
`42096e9676d33e25c3b6092e60fbd0fdacd699435ed9dc9db59ce24a1ceaaba3`. cwd=/, TMPDIR=<scratch>/tmp.

## Reproduction (observation)
- Extracted the `readout.py` block: SHA-256 `31dac211…ee02ac` (matches entry :80). `python3 -B readout.py tree` → exit=0, 25 lines,
  stdout SHA-256 `58b63dd9…c0c416`; `cmp` against the entry's printed stdout block → `STDOUT_MATCH`.
- `git diff --stat a3498e25 d9776195 -- corpus/fixtures corpus/live` → empty (no fixture or record byte change).

## Finding 1 — BROKEN: a round-wide network claim contradicts the round's own read-only opens (Q11, Q10)
- Entry :66 (item 26): "The one network access this round was the read-only opening of the public ECMA-262 page for the S029 row".
  The inventory rows `23-30` say "no output claimed", so this factual sentence has no derivation. It is also false:
- `.ufo/waves/round-62/build/R62SourceEvmSpec.md:9-17`: round-62 S028 opens (2026-10-21, HTTP 200) of the GitHub tag, commit and API
  endpoints plus raw `instructions/__init__.py`, `runtime.py` and `control_flow.py`, each re-fetched at the tag ref. `corpus/lessons/round-62.md:62-65`
  logs S028 at raw.githubusercontent.com.
- S029 alone involved more than one page. `R62SourceEcma.md:15-22` lists the single page plus two multipage chapters
  (`…statements-and-declarations.html`, `…scripts-and-modules.html`), and `corpus/SOURCES.md:67` adds that
  "two guessed short-form mirror URLs returned 404".
- Impacted axes: Q11 (a factual statement with no derivation, which is also false) and Q10 (one seat's view stated as a round-wide fact).
- Smallest correction: scope the sentence to the readout ("the readout made no network access"), or state the actual read-only opens
  recorded in R62SourceEcma/R62SourceEvmSpec. Do not assert a round-wide count.

## Finding 2 — BROKEN: the source/saved line coordinate is printed but never derived or compared (Q11)
- Code (entry :148): `"span_text_from_fixture": line[start.get("column"):end.get("column")]`. `line` is the line the regex matched,
  not the line at the saved `start.line`. Entry :161-162 builds `line_number_1based` as the ordinal among **non-empty** lines, not the physical line.
- Mutation 1, on an archived copy only: I set every `imports` edge in the js-r3 record to `start.line=end.line=4`. Readout exit=0, and it printed
  `"span_1based_inclusive":[4,7,4,50],"span_text_from_fixture":"{ rot13, checksum } = require('./transform')"`. The "from fixture" text is
  unchanged at a wrong saved line, and nothing fails.
- Mutation 2: I prepended one blank line to the copy of js-r3 `index.js`. Readout exit=0 and still printed `"line_number_1based":1`
  (the physical line is now 2).
- Real data: `cat -A` shows both `index.js` files have 7 lines, none blank, so "line 1" and the saved line 1 are **correct values without
  an in-entry derivation**. Q11 text (`corpus/QUALITY.md:23`) says this fails: "a value is correct when re-derived but the entry carries no derivation".
  Items 3, 8, 9 and 11 ("The saved spans are the manual spans… the bytes read back at the saved columns") depend on this.
- Smallest correction: derive the physical line from unfiltered `text.split("\n")`, read the span text at the saved `start.line`/`end.line`, and
  print a line-equality check. Alternatively, label the saved line fields "recorded, not compared" and limit item 11 to columns.

## Finding 3 — derivation gap (Q11): the quote word count
- Entry :248 says the S029 quote is "— 8 words", with no derivation. `python3 -c` whitespace split of "Set value to ? GetV(value, propertyName)." → 6.
  The normalised HTML rendering → 10. The opener `R62SourceEcma.md:34` records 6. Correction: print the count or state 6 (whitespace split).

## Scope attack — holds (observation)
- Package `main`: `package.json` holds `"main":"index.js"`. The entry claims nothing about it ("No claim is made about package `main`", :10),
  and item 2 uses only `type`. HOLDS.
- Electron label: each saved record has 1 `electron-main` node (counted via `collections.Counter` over `graph.nodes[].kind`). The entry never
  names it. It disclaims "any role label" (:10), and item 21 leaves other nodes unexamined. "JavaScript/Electron packages" is the C04 row title
  quoted from `README.md:33`, not a claim. HOLDS.
- Loader behaviour: `resolved_path`/`state` are presented as fields the record "carries". The entry makes no resolution claim (item 16 and :10). HOLDS.
- Runtime unknown (item 18): this matches the sibling records `live/runs/20261012T164357Z/LEDGER.md:14` (UNKNOWN runtime ROT13/checksum) and
  `round-9/LEDGER.md:11`. No corpus record shows execution of js-r3. It is a genuine unknown, not a concealed known fact. HOLDS.
- Item 29 ("left byte-unchanged"): the blob is `df24b9ad…` at 5bd4a90, a3498e25 and d9776195. True, but not derived in the entry (nonfatal).

## Nonfatal wording (PARTIAL-level, would not alone break)
- Item 19 says "The export side of either module is **unknown**". Two known facts on the entry's own S030 inputs contradict "unknown":
  `transform.js:11` (`module.exports = { rot13, checksum };`) and `index.js:7` are in the hashed fixture bytes, and both records carry
  `exposes` edges (`module_link_kind:"commonjs-export"`, `exported_name:"default"`). Use "not examined here (out of scope)", as item 21 does.
- Item 18 says "the required module object", which presupposes loader semantics. Item 16's neutral "value of the `require(...)` call" is better.
- Item 16 says "not an ECMAScript module import", relying on §16.2.2 grammar, while the header and Sources say only the §14.3.3.3 text is used.
  The claim is evident from the leading `const`, but its authority is not quoted.
- Item 30 quotes the lesson as "ADJ-06 sibling arbitration: operator-owned and unresolved; …". The actual text is a table row
  (`lessons/round-62.md:29`), "| ADJ-06 sibling arbitration | Operator-owned and unresolved; …": cells joined and capitalisation changed.

## Inference / unknown
- [INFERENCE] Findings 1-2 are fixable in-entry without new sources. Neither changes a printed value. Both are Q11 derivation and scope
  defects that the round's unchanged Q11 rejects as written.
- Unknown: this seat did not re-audit S029's clause slicing or the §14.3.3.3 production name (other seats' scope).
  This seat made no network access.

VERDICT: BROKEN. Q11 fails (finding 2: line coordinate not derived, shown by mutation; finding 1: false, underived round-wide network
sentence; finding 3: underived count). Q10 is strained by finding 1. Package-main, Electron, loader and runtime scope hold.
Do not admit until corrected and focused re-review is done on the exact corrected bytes. No repair or admission by this seat.
Installs: none. Scratch: /fast/scratch/hyaku/revenger-r62/R62FJsScopeUnknown/ (tree, readout.py, out.txt, muttree, mut-out.txt).

## Focused re-review (append-only; original report above preserved, SHA-256 before append `e415af8a…b597`)
RESOLUTION: HOLDS for this seat's scope — commit `47511b213bf556022869fa104a4bda9d7c9a3b95`, C04 entry SHA-256
`d4544c7012a52c0b877022009de6056d6beeda53cd78c2054361e732dce5cafe`. Extracted with `git archive 47511b2 | tar -x`, cwd=/, TMPDIR=<scratch>/tmp.
I made no repair and no admission. Diffs since d9776195 for fixtures, live records, `QUALITY.md` and `README.md` are all empty (C04 still `uncovered`).
- Reproduction: the corrected block `readout.py` has SHA-256 `78a51a73…6d14` and 142 lines, both matching the entry's §Reproduce. It exits 0 with 25 lines,
  stdout SHA-256 `3c62d57c…bcf`. `cmp` against the printed stdout gives STDOUT_MATCH_ENTRY. The stdout is the same when run on the d9776195 extract.
- Finding 1 (network) RESOLVED: item 26 now covers only the readout ("uses **no network**"). The S029 page open is "recorded in the source ledger",
  and the entry no longer claims a round-wide count. Nonfatal: it says "page" (singular), while R62SourceEcma.md:15-22 records the single page plus two chapter pages.
- Finding 2 (line coordinate) RESOLVED. The code now reads `all_lines[s_line - 1]` at the SAVED line, and `physical_line_number_1based` enumerates
  unfiltered `splitlines()`. It prints `saved_line_equals_physical_source_line` and `saved_start_line_equals_physical_source_line`, plus the
  call and assignment text-equality flags. Bounded mutants on archived copies (each exits 0, as a report and not a gate):
  - The saved line set to 4 on all 3 js-r3 edges: saved_line_text `'  const transformed = rot13(input);'`. lineEq, startEq, call and assign are all False.
  - The saved line set to 2 on ONE edge: only that edge flips (`"const defaultInput = 'amber';"`, all False). The other two edges stay True with their own
    span texts, so each edge reflects its own saved line.
  - The saved line set to 99: saved_line_text None and all flags False, so an out-of-range line is handled.
  - Saved start column 7 on the rot13 edge: line flags True, both text flags False (`" rot13, checksum } = …"`), so columns are compared independently of lines.
  - A blank line prepended to js-r3 `index.js`: phys 2, total 8, all 3 js-r3 edges False. js-r7-v2 is unchanged (phys 1, True).
    `grep|uniq -c` shows 3 false and 2 true, which is identical to the entry's own §Reproduce mutant block.
  - `'amber'`→`'ambér'` in js-r7-v2: `source_ascii_only` False with chars 209 and bytes 210. The new ASCII and column-convention fields respond to the input.
  Real data: each `index.js` has 7 LF, 0 CR and 0 other `splitlines()` breaks (VT/FF/FS/GS/RS/NEL). So "physical line" equals the LF line here.
  Nonfatal: the entry does not print this convention, but the saved-line equality flags establish line 1 either way.
- Finding 3 (word count) RESOLVED: §Reproduce has `printf … | wc -w` → `6`, and I reproduced it here. The S029 date, anchors and digest are now labelled
  "recorded from the S029 row, not derived" (header, §Sources, inventory H1/S1).
- Nonfatal notes: item 19 now reads "**not examined here**" (resolved). Item 18 now reads "the value of the `require(...)` call" (resolved).
  Item 16 now says "establishes no export binding and no module import" without the §16.2.2 grammar claim (resolved). Item 30 paraphrases
  the lesson without quotation marks (resolved). Item 29 "byte-unchanged" is still not derived in the entry, but it is true: blob `df24b9ad…` at 5bd4a90, a3498e25,
  d9776195 and 47511b2. This is nonfatal.
- Unchanged scope holds: package `main`, the Electron label (the `electron-main` node is not named), loader behaviour (`resolved_path` is only reported as a field the record
  carries) and the runtime unknown all hold as in the original report.
VERDICT (re-review): HOLDS on this seat's findings 1-3. This is not an admission; L1 adjudicates. Installs: none. Scratch: <scratch>/rr/.
