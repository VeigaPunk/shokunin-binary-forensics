# R73Source062 — radare2 (S062) quote re-verification

Seat: R73Source062 (leaf, read-only). Report: `.ufo/waves/round-73/v2/R73Source062.md`.
Claim context: round-73 frozen C10 coverage admission; this seat audits only assigned row
**S062** of `corpus/SOURCES.md`. Judged axes: coverage, source accuracy.

## Re-opened primary source (my own fetch, this seat)

- **URL/pin:** `https://github.com/radareorg/radare2` → raw `README.md` at pinned commit
  `6ac96f50eafef46c1ac75a478a1460819968c66f`
  (`https://raw.githubusercontent.com/radareorg/radare2/6ac96f50eafef46c1ac75a478a1460819968c66f/README.md`).
- **Access date:** 2026-10-30 (row's original access 2026-10-27).
- **Result:** HTTP 200, 10,644 bytes, SHA-256 `dc86af03a0eb92735a59fa18e397520a90d593683abd504d5f85f4f80db1b7c9`
  — byte-identical to the fetch recorded in round-72 seat `.ufo/waves/round-72/w1/CoreS062Review.md`.
- **Pin existence:** GitHub API commit lookup succeeded today (no rate-limit): commit
  `6ac96f50…` "After release version bump" (pancake, 2026-10-12). Pin is real.
- **Network/source failures:** none for this seat. Both the raw fetch and the API call returned
  200. (The round-72 seat noted API rate-limit; it did not recur here.)

## Verbatim comparison (markup-normalized only)

Registry row `corpus/SOURCES.md:76` anchor+quote:

> README.md "Description", commit 6ac96f50eafef46c1ac75a478a1460819968c66f, accessed 2026-10-27;
> "Today, r2 is a full-featured low-level command-line hexadecimal editor"

Pinned README `### Description` (lines 16–18) actually reads:

> "The **radare** project started as a simple command-line hexadecimal editor
> focused on forensics. Today, r2 is a full-featured low-level command-line tool
> with support for scripting with the embedded Javascript interpreter or via r2pipe."

- **Observation:** the claimed string occurs 0 times in the pinned README — verified by
  direct `grep` (exit 1) and again after collapsing all newlines to spaces
  (`tr '\n' ' ' | tr -s ' '`, count 0). No markup normalization can produce it.
- **Diagnosis (observation):** the row's quote is a splice — "command-line hexadecimal editor"
  (end of line 16) joined to "Today, r2 is a full-featured low-level command-line tool"
  (line 17), reordering source text. Same defect class as the routed round-72 defects
  S071 (registry paraphrase) and S082 (misattributed quote) in
  `corpus/lessons/round-72-verifier-spotcheck.md`.

**Exact ≤25-word located quote (verbatim, 20 words) from the pinned source:**

> "Today, r2 is a full-featured low-level command-line tool with support for scripting with the embedded Javascript interpreter or via r2pipe."

## Scope, tier, used-by, flip

- **Scope:** row claims "the repository's own CLI analysis, hex editing, debugging and
  scripting description; no claim of version-specific output". **Supported** by the same
  Description section ("r2 can edit files on local hard drives, view kernel memory, and
  debug programs locally or via a remote gdb/windbg servers… analyze, emulate, debug,
  modify, and disassemble any binary"). No version-specific output is asserted.
- **Tier A:** correct — the claim is the project's own README description, bounded.
- **Used-by:** `corpus/knowledge/round-72-tool-landscape.md` — verified; S062 cited in the
  "native disassembly/decompilation" and "authored byte-level inspection" rows, with
  paraphrases ("describe command-line binary analysis", "list hex/format and scriptable
  inspection capabilities") that the README text supports, and cautions against inferring
  parity/licensing/readiness. Entry wording is sound.
- **Rejection flip:** none in row (admit); none needed — the defect is in quote evidence,
  not in admissibility of the source.

## Disposition

- **AGREE** with round-72 lesson Gate decision (`corpus/lessons/round-72.md:21`):
  ADMIT, tier A for the README's own CLI claim. Substance of the admission is sound and
  independently re-confirmed today.
- **DISAGREE** that the located-quote requirement is met: the S062 quote is not verbatim
  in the pinned source. Concur with round-72 seat `CoreS062Review.md` verdict REVISE on
  quote evidence.

## Proposed NEW superseding row (append-only; old row never edited)

Per the routed-defect handling pattern (supersede, don't edit), propose when the registry
next admits rows — id **S429** is the next free id (registry currently S001–S428, no
duplicates; S096–S109 exist for C10):

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S429 | radare2 — https://github.com/radareorg/radare2 | tool | A | the repository's own CLI analysis, hex editing, debugging and scripting description; no claim of version-specific output | README.md "Description", commit 6ac96f50eafef46c1ac75a478a1460819968c66f, accessed 2026-10-27; re-verified 2026-10-30: "Today, r2 is a full-featured low-level command-line tool with support for scripting with the embedded Javascript interpreter or via r2pipe." | A broad command-line surface is documented; edits/debugging are not part of the static-only work performed in this round | mined | 2026-10-27 | on-release | corpus/knowledge/round-72-tool-landscape.md |

The S062 row's status/recheck/used-by remain otherwise unchanged; the superseding row
carries the verbatim quote and the re-verification date. The round-72 lesson Gate row for
S062 should carry an erratum note in a future lesson, not a silent edit (lesson append-only
discipline is the integrator's call; this seat writes no corpus files).

## Impact on frozen C10 predicate

**Observation:** S062 is not in the frozen set S096–S109 that `reports/round-73/measure.py`
requires mined/linked/cited; the counter checks row presence, linkage and vote files, not
quote verbatim-ness. This defect therefore does not bear on the C10_HELD_BACKED predicate.
**Inference:** left unfixed, the S062 misquote remains an evidence-quality debt of the same
class the integrator already routed for S071/S082; the superseding row above clears it
without touching the frozen claim surface.

## Evidence classification

- Observation: fetched bytes, hash, grep counts, API commit record, row/lesson/entry text.
- Inference: defect classification (splice, same class as S071/S082); no impact on C10 counter.
- Unknown: nothing material; commit tree SHA `5df42d48…` seen in API response but tree
  contents beyond README not independently listed (raw fetch at full 40-char hash is
  sufficient pinning for this audit).

## Tooling record

No installs or updates this seat. Used preinstalled host tools only: `curl` (fetch),
`sha256sum`, `grep`/`awk`/`tr`/`wc` (checks). No pacman (host-wide pause honored), no
uv/npx/cargo needed. Scratch `/fast/scratch/hyaku/revenger-r73/r73source062/` removed
after this report was written; receipt facts (URL, pin, size, SHA-256, quote) are recorded
verbatim above.
