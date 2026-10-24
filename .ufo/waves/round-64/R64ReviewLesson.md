# R64ReviewLesson — review of the drafted round-64 lesson

Seat `revenger-r64.R64ReviewLesson`, 2026-10-24. Target: `/tmp/revenger-r64-lesson/round-64.md`
(213 lines, sha256 `1fec003279bfc7176ff9431533a5e5c2e2eed2b9040f62cff46f2b3510f88550`; reviewed as written at 01:20). Contract:
`reports/round-64/claims.md`; counter: `reports/round-64/measure.py`; red-before:
`reports/round-64/measure-before.log`. This review recommends; it admits nothing.

## Verdict

**FAIL as written — one must-fix (F1), everything else in the deliverable passes.**

The four required elements are present: M36 carries class/evidence/captured-by/fix with the
fix shown able to fail; the Gate has a placeholder block for each new row (S036, S037); the
routed-debt table dispositions claims.md inputs 1–7 and adds the required S036 id-note row;
frontmatter is complete and its counter sha256 matches the file. F1 is a false commit
attribution inside the red-before/M36 evidence — the M95/M36 citation class this lesson
itself records — and is a one-line fix (exact wording supplied). After F1 the lesson is
PASS on the ticket's criteria; F2–F7 are should-fix/low/NIT precision items, none blocking.

## Findings (severity order)

### F1 — MUST FIX — red-before receipt is attributed to the claim base, where it does not exist

`/tmp/revenger-r64-lesson/round-64.md:24` — “Red-before receipt, committed at the claim base:
`reports/round-64/measure-before.log`.” and `:182` (M36 evidence) — “`README_TOKEN_LEGEND_MISMATCH=1
rows=['C07']` at base commit `666ea84b`, committed in `reports/round-64/measure-before.log`”.

Evidence: the receipt, the contract and the counter are **not** in the claim base. At lane
commit `666ea84b` the path is absent (`git cat-file -e 666ea84b:reports/round-64/measure-before.log`
→ “path … exists on disk, but not in '666ea84b'”; the same holds for `reports/round-64/measure.py`
and `reports/round-64/claims.md`, both first committed at `3bb430f`).
They are committed at `3bb430f` (“round-64: frozen claims + counting probe + red-before
do-nothing control”), whose parent is `666ea84b`; claims.md itself says the control was
“committed with pre-registration”, not at the claim base. A closure seat following `:24`
literally hits a fatal git error — exactly the M95 citation class M36 documents, reproduced
in the lesson that records it.

Fix: `:24` → “Red-before receipt, committed at the pre-registration commit `3bb430f` and
measured on the `666ea84b` tree: `reports/round-64/measure-before.log`.” At `:182` make the
same split explicit: the value is measured on the claim-base tree, the log is committed at
`3bb430f`. Also add the freezing commit to frontmatter `:8` (`contract: reports/round-64/claims.md
(frozen at lane commit 3bb430f)`) so the frontmatter and body agree.

The substantive evidence itself is sound (independently re-derived, not just quoted):
at `666ea84b`, `corpus/README.md:36` ends `frontier` and `corpus/live/runs/round-63/inspection.json`
carries `"operation":"inspect_firmware_regions"`; `measure.py:55-78` maps that operation to
C07 (`ROW_OPS`) and flags `frontier` rows with a matching saved record. The value 1 is real.

### F2 — SHOULD FIX — the M36 fix is a diagnostic that does not gate the probe's exit

`/tmp/revenger-r64-lesson/round-64.md:182` — the fix column says the label “is shown able to
**fail** at base with value 1 and is required **0** at round end” and “is cleared only by a
token consistent with evidence that exists”.

Two precision problems, both material to honest saturation claims:
1. The label is consumed only by `HOLDS_OK_V2` (`reports/round-64/measure.py:268-271`,
   `len(mismatch) == 0`); the probe's exit status uses the round-63 `holds_ok`
   (`:264-266`; `sys.exit` at `:273`) and does **not** contain `mismatch`. A round that leaves C07 `frontier`
   can still exit 0 (the base receipt proves `HOLDS_OK=yes` and `HOLDS_OK_V2=no`; by
   `measure.py:264-273` that exits 0). The lesson
   should say “required 0 at round end and machine-reported through `HOLDS_OK_V2`; the exit
   code does not consume it” — the same warning the lesson already gives for
   `HOLDS_OK`/C4 at `:158`. Closure must read `HOLDS_OK_V2=yes` and
   `README_TOKEN_LEGEND_MISMATCH=0`, not just exit 0.
2. “cleared only by a token consistent with evidence that exists” overstates the label:
   any non-`frontier` token clears it (including `partial`, or `held` with an empty
   knowledge column). Consistency with admitted knowledge is carried by
   `K_HELD_BACKED`, not by this label. Replace with “cleared by any token other than
   `frontier`; a `held` token without a cited admitted entry leaves `K_HELD_BACKED` at
   7/14, so the label and the backed count must both move”.

### F3 — SHOULD FIX — S036 id-note provenance: the build file's note says S034, not S036

`/tmp/revenger-r64-lesson/round-64.md:126` — “left a forward note that ‘a future zipfile-docs
row takes **S036**’ (`.ufo/waves/round-63/falsify/routed-debt.md:156`, from
`.ufo/waves/round-63/build/R63SourceZipfileDocs.md:251-256`)”.

`routed-debt.md:156` does say S036, but the cited build range says **S034** (after an
earlier S033 in the same file, §9a). The falsify seat's line 156 is itself the “note moved
twice” re-derivation. As written, “from” sends a reader to a file that names a different id.
Fix: “`.ufo/waves/round-63/falsify/routed-debt.md:156` (the note had moved S033 → S034 →
S036; the build template `.ufo/waves/round-63/build/R63SourceZipfileDocs.md:251-256` names
S034)”. The disposition (first-use-wins) is unaffected and correct.

### F4 — SHOULD FIX — the registry-contract citation is not resolvable from the lane repo

`/tmp/revenger-r64-lesson/round-64.md:117` — “(`.ufo/waves/kaika/SOURCES-CONTRACT-v1.md:22`)”.

That path does not exist in `revenger-shokunin`; the file is at the **fleet** root
`/home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md`. The quoted rules are
correct and at the cited lines (`:22` “`id` — `S` + 3 or more digits, the next unused; never
reused”; `:16` “a lead is not evidence and never a row”), so only the path needs qualifying:
prefix it as the fleet-repo absolute path, or state “fleet repo”. Every other citation in the
lesson is lane-relative and resolves.

### F5 — SHOULD FIX — routed-debt row (6) has a dangling source pointer

`/tmp/revenger-r64-lesson/round-64.md:202` — source cell “claims.md routed input 6;
`.ufo/waves/round-63/…` routed wording”. The ellipsis names no file. The frozen source is
`reports/round-64/claims.md` routed input 6 (with the freshness-hold semantics sentence);
cite that, and drop the dangling fragment or replace it with the round-63 lesson/claims line
that carries the wording. Disposition text itself matches claims.md.

### F6 — NIT — the S036 quote placeholder asks for an “entropy” sentence the snapshot lacks

`/tmp/revenger-r64-lesson/round-64.md:90` — the `S036_QUOTES` filler instruction says to cover
“any entropy/signature-scan sentence the C07 entry relies on”. The pinned snapshot
`.ufo/waves/round-64/source-snapshots/rea-firmware-guide.md` contains **0** occurrences of
“entropy” (case-insensitive); the signature sentence exists (snapshot lines 85–86 per
`gate-quotes.md`). “Any” keeps the instruction conditional, but the filler may hunt for a quote that
cannot exist. Drop “entropy/” or say “any signature-scan sentence”.

### F7 — LOW — the S036 gate block's signature-UUID quote pointer is off by one line

`.ufo/waves/round-64/gate-quotes.md` (S036 block) — the quote “Binwalk signature UUIDs and
Unblob blob IDs are producer-local identities; compare content hashes and source ranges across
runs.” is attributed to snapshot lines **85–86**, but it begins on line **84** (line 84 ends
“… version and limitations. Binwalk signature UUIDs”; the quote runs 84–86). I checked every
other pointer in the artifact by joining exactly the cited line range and matching the quote
(12 of 13 exact; this is the only miss). If the lesson fills `S036_QUOTES` from this artifact
verbatim it inherits the wrong pointer, and the filler instruction at `:90` requires “snapshot
line numbers”. Fix the artifact to 84–86 instead of copying 85–86.

## What passes, with evidence

- **M36 shape** (`:178-182`): columns class/evidence/captured-by/fix all populated and match
  `briefs/R64LessonDraft.md:14`. Captured-by is `none` with the reason (no committed check
  compared tokens to evidence). The base receipt line
  `README_TOKEN_LEGEND_MISMATCH=1 rows=['C07']` is verbatim in
  `reports/round-64/measure-before.log` (line 6), and the value is independently derivable
  at `666ea84b` (F1 evidence above). The fix is shown able to fail at base with value 1 —
  the ticket's demonstration requirement is met.
- **Red-before block fidelity** (`:28-42`, `:56-61`): all 13 label lines and all 4 mutant
  lines are byte-verbatim members of `measure-before.log` (checked line-by-line, not by
  eyeball). The reading note at `:46-52` is correct: the log has no exit-code line, and
  `HOLDS_OK_V2=no` at base is the attributed-count consequence (measure.py `:268-271`).
- **Gate coverage for both new rows**: S036 block (`:73-91`) names URL/tier/owner and carries
  seven fill tokens (URL, HTTP, bytes, sha256, snapshot, provenance, quotes); S037 block
  (`:93-108`) carries six digest tokens for the full claims.md bundle
  (bin/truth/generator/inspection/receipt/LEDGER). Placeholders are explicitly declared
  non-landable until filled (`:69-71`), which is honest and satisfies “placeholders or
  quotes for every new row”.
- **The source artifact the placeholders will consume is already sound** (verified by
  recomputation, so the filler can paste rather than re-derive):
  `.ufo/waves/round-64/gate-quotes.md` — 13 quotes, each 9–20 words (limit 25), every quote a
  verbatim substring of the whitespace-normalized snapshot, 12 of 13 line pointers matching
  the quote's exact line range (the 13th is F7, off by one start line); snapshot sha256
  `e422b481…93609`, 10695 bytes, 213 lines, matching
  the artifact; all six S037 digests match my independent `sha256sum` at the working tree
  (`bdfe9f46…8510be`, `9663f90b…a65e6`, `4e5d5975…93db4`, `f6997835…71f9`, `e930a549…b94d`,
  `25a4a18b…e1a6`) and the sizes match `stat`.
- **Registry claims in the Gate** (`:111-124`): at `666ea84b` the registry has exactly 35
  rows ending `S035`, `S036` occurs 0 times; at review time the working tree still has 35
  rows and 0 S036 hits. The id-allocation conclusion (S036 next unused, S036+S037 contiguous)
  is correct.
- **Routed debt vs claims.md** (`:193-204`): inputs 1–7 match claims.md dispositions
  one-for-one (counter labels incl. STRICT/mismatch/V2; C2 as M35; C07 flip either way;
  transplant-corollary owner + check shape + Q09 disclaimers; r58/59 quotes unedited with the
  139→142 non-reproduction and owner; freshness wording frozen; SHONEN box checklist-only),
  and row (8) fulfils the S036 reconciliation the ticket requires. The 142 non-reproduction
  is verbatim in the base log (`HOLD verify_named_multi_icon_states.py` line).
- **Candidate-status honesty** (`:139-142`): C1 is “not landed, not admitted”; C2 is
  “working-tree edits present — attributed tally is a final-gate measurement”. Verified:
  the forged-stdout require sits at `corpus/verify_icon_languages.py:154` (command control
  `:151`) and `corpus/verify_multi_icon_states.py:153` (command control `:150`); the string
  occurs 0 times in both files at `666ea84b`; `git status` shows both modified;
  `R64C4LangPatch.md` reports its self-test passed, `R64C4MultiPatch.md` reports it was not
  run — the lesson states exactly that, without inflating it. The admission-order section
  (`:144-160`) restates claims.md and admits nothing.
- **Frontmatter** (`:1-12`): round/date/author/claims/lane/claim_base/contract/counter+sha256/status
  all present; counter sha256 `b8e68d32…b9168` matches `reports/round-64/measure.py` exactly;
  claim base matches claims.md.
- **C2 disposition wording vs code**: `receipt_ok` in both scripts ends with
  `receipt['stdout_sha256']==H(raw_bytes)` (`verify_icon_languages.py:118-120`,
  `verify_multi_icon_states.py:121-123`), so the frozen mutation sentence in row (2) names
  the real conjunct.

## Residual risk

1. **The round's exit code does not consume the M36 fix or the attributed counts** — only
   `HOLDS_OK_V2` does (measure.py `:264-273`). Void conditions name “probe exit non-zero at
   final”; a clean exit is therefore compatible with a stale C07 token and a missed C4
   attribution. Closure must read `HOLDS_OK_V2=yes`, `README_TOKEN_LEGEND_MISMATCH=0`,
   `C4_RECEIPT_KILLED_ATTRIBUTED=2/2` as printed lines. Recommend adding that sentence to the
   lesson's admission-order step 4 (it already carries the `HOLDS_OK`/C4 half).
2. **Gate fill is still pending**: the lesson is not landable until the 13 fill tokens and
   `<<R64_SEARCH_LOG_NOTE>>` are replaced. The values exist (gate-quotes.md), so this is
   mechanical, but a token left in the landed file would ship a placeholder as evidence.
3. **S036 quote selection is the entry's burden, not the lesson's**: the gate block covers
   route scope only; whether the C07 entry's load-bearing sentences map to those quotes is
   another seat's Q01 decision. Nothing here certifies it.

## Verification gaps

- The frozen counter was **not** re-run by this seat (reviewer role; red-before is ground
  truth). The label logic was read at `measure.py:55-78` and `:264-273` and cross-checked
  against the committed receipt.
- **LSP device unavailable**: `xd://lsp` returns “No such tool”; mounted devices are
  `ast_edit` and `debug`. No symbol-level definition/reference checks were possible, and for
  a Markdown lesson none apply. Commit-presence claims (F1) were checked with
  `git cat-file -e` exit status and content reads (`git show`), not with grep; the base
  zero-occurrence counts are literal `grep -c` over `git show` output and are labelled as
  such.
- The final Gate text could not be reviewed because it is still tokens; I reviewed the
  artifact it will be filled from.
- Working-tree C4 edits remain uncommitted; the attributed tally is parent-owned.
- Later closure artifacts (README flip, SOURCES rows) are correctly stated as not-yet-landed
  and were not treated as landed.

## Tooling record

No tool installed, upgraded, or downloaded. No `pacman` transaction (host pause honored).
Scratch used: none beyond reads; this report is the only write.

## Report

`.ufo/waves/round-64/R64ReviewLesson.md`
