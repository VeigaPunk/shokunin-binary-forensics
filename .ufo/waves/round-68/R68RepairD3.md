COUNT-CONFIRMED — lesson quote = **19** whitespace tokens (lesson states 18, off by one), `SOURCES.md` row's own shorter variant = **14**; both ≤ 25, so both are conformant and the defect is a count typo only, not a quote-length violation.

seat: `L1Revenger68.R68RepairD3` · role: scribe/critic (read-only) · round 68 · lane `revenger-shokunin`
lane HEAD at audit: `4232235723cf8d4731a1e7e78ca098b8af953a57` · both audited files clean in `git status --porcelain`
axes named: **count correctness** (a checkable field, Q08/Q11 class) and **correction-landing compliance** (append-only). No move below writes outside this file; no corpus/report/LOG byte was modified; no install performed (see §7).

---

## 1 · The routed defect, as filed

`corpus/lessons/round-67-verifier-spotcheck.md:234-235` (§7 item 3), verbatim:

```
3. **S045 quote length is mis-stated.** The lesson says 18 words; the quote is 19 words by
   whitespace count (both ≤ 25, so the row is conformant). Trivial, but the count is a checkable
   field.
```

The spotcheck's own §5 restates the same numbers ("19 words, ≤ 25" / "the `SOURCES.md` row's
shorter 14-word variant"). So the routed defect already carries the numbers I independently
re-count in §2 — **the defect statement itself is accurate**; what is wrong is the lesson it points at.

## 2 · Exact strings counted, and their counts

Both strings read from the committed bytes at the lane HEAD above (file sha256s in §6).

### 2a · The lesson's located quote — `corpus/lessons/round-67.md:74-75`

Filed across a line wrap (line 74 ends `… of the`, line 75 begins `file (everything …`); joined with
a single space, the quoted string is:

```
adler32 checksum of the rest of the file (everything but magic and this field); used to detect file corruption
```

Token list (whitespace split, in order):

| # | tok | # | tok | # | tok |
|---|---|---|---|---|---|
| 1 | adler32 | 8 | file | 15 | to |
| 2 | checksum | 9 | (everything | 16 | detect |
| 3 | of | 10 | but | 17 | file |
| 4 | the | 11 | magic | 18 | corruption |
| 5 | rest | 12 | and | 19 | — |
| 6 | of | 13 | this | | |
| 7 | the | 14 | field); | | |

**19 words.** `≤ 25` → **yes, conformant.**

The lesson prints `(18 words)` on `corpus/lessons/round-67.md:75` — one too few. Both counting
conventions agree, so the 18 is not a punctuation artefact: whitespace-split = 19,
punctuation-stripped (`[A-Za-z0-9_]+`) = 19. The quote's own framing line,
`corpus/lessons/round-67.md:73`, already declares the rule it is scored by: `Located quote (≤25 words),`.

### 2b · The `SOURCES.md` row's own shorter variant — `corpus/SOURCES.md:59` (`anchor` column)

The S045 row does not carry the full lesson quote; it carries the checksum clause only:

```
adler32 checksum of the rest of the file (everything but magic and this field)
```

**14 words** (whitespace-split 14; punctuation-stripped 14). `≤ 25` → **yes, conformant.**
Tokens: adler32, checksum, of, the, rest, of, the, file, (everything, but, magic, and, this, field).

The row's two other quoted fragments on the same line are not the located quote and are not counted
as one: `must be 0x70 (112) bytes (v40 or earlier)` (7 tokens) and
`ENDIAN_CONSTANT = 0x12345678` (3 tokens); neither is offered as the located quote, and the ≤25 rule
applies per located quote, so no stacked-length issue arises.

## 3 · Reproduction command (actual output)

```py
q = "adler32 checksum of the rest of the file (everything but magic and this field); used to detect file corruption"
v = "adler32 checksum of the rest of the file (everything but magic and this field)"
len(q.split()), len(re.findall(r"[A-Za-z0-9_]+", q))   # (19, 19)
len(v.split()), len(re.findall(r"[A-Za-z0-9_]+", v))   # (14, 14)
```
Observed: `lesson count= 19 chars= 110 <=25: True` · `sources-row count= 14 chars= 78 <=25: True`.
Contiguity of the lesson quote across the wrap confirmed from the raw lines:
`quote occurrences in 74-75: True`.

Quote-vs-source accuracy was also re-checked (not the assignment, one line of evidence so the count
is not read as a faithfulness claim): the 281 157-byte snapshot
`.ufo/waves/round-67/source-snapshots/dex-format.html` is present, sha256
`c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4` (matches the lesson `:73` and the
row's `anchor` column), and **both** strings are present after whitespace-normalised tag-stripping
(`present-normalised: True` for each; not byte-contiguous in the raw markup — the rendered-document
quote is accurate, exactly as the spotcheck §5 recorded).

## 4 · Rule the counts are scored against

| rule | pointer | text |
|---|---|---|
| located quotes are ≤ 25 words | `corpus/SOURCES.md:8` | `access dates and ≤25-word quotes are in` (`lessons/round-1.md` `## Gate — kaika continuation`); the S045 line restates it locally at `corpus/lessons/round-67.md:73` |
| rows are append-only | `corpus/SOURCES.md:5-7` | `Rows are append-only: only `status`, `recheck` and `used-by` change in place, each change logged old→new in the round lesson.` |
| criteria are superseded, never rewritten | `corpus/QUALITY.md:5-6` | `Criteria are superseded by new rows that name the row they replace, never rewritten (LEARNING.md §Files the path writes).` |

Note the interaction the correction must respect: the word count is **not** one of the three mutable
`SOURCES.md` fields, and the 14-word variant sits in the immutable `anchor` column — which is why
nothing in `SOURCES.md` needs touching at all (14 ≤ 25 already).

## 5 · What a correction must say, and where it must land

**Content (exactly this, and nothing stronger):**

> S045 located quote word count, corrected: the lesson says 18 words; the quote
> "adler32 checksum of the rest of the file (everything but magic and this field); used to detect file
> corruption" is **19** words by whitespace count (19 by punctuation-stripped count as well). The
> `SOURCES.md:59` row's own shorter variant, "adler32 checksum of the rest of the file (everything but
> magic and this field)", is **14** words. Both are ≤ the 25-word limit, so the row is conformant and
> the tier/scope/anchor decision stands — only the printed count was wrong.

It must state the number (19), that the row's variant is 14, and that **both are conformant** — it
must not imply a quote-length violation, a scope change, a tier change, or a re-gate of S045.

**Placement (append-only; three constraints, all grounded):**

1. **Never an in-place rewrite.** `corpus/lessons/round-67.md:75` keeps `(18 words)` as filed bytes.
   Round lessons are historical records; the lane's own precedents are explicit:
   `corpus/lessons/round-62.md:37` — `## M25 attribution and capture correction (append-only)`;
   `corpus/lessons/round-63.md:250` — `Reconciliation, append-only: … logged here per the
   append-only rule rather than rewriting the counts above.` The same shape applies verbatim here.
2. **Lands as an appended reconciliation note in the round-68 lesson**, i.e.
   `corpus/lessons/round-68.md` `## Gate` — the round that is doing the repair appends the note that
   names the round-67 file and line it corrects. That file **does not exist yet** at audit time
   (`ls corpus/lessons/round-68*` → no match), so the note is created by this round's Gate, not
   retro-fitted into round-67.
3. **Logged once in `LOG.md`** as the round-68 entry's correction line (old→new), matching
   `corpus/SOURCES.md:5-7`'s "each change logged old→new in the round lesson" convention; the
   `SOURCES.md:59` row itself needs **no** edit (14 ≤ 25, and the count is not a mutable field).

If the round instead prefers to correct the spotcheck's own phrasing, note it is already correct
(§1) — the only wrong byte in the chain is `round-67.md:75`'s `18`, and it is corrected by
append, not by edit.

## 6 · Provenance of the audited bytes

| file | sha256 | state |
|---|---|---|
| `corpus/SOURCES.md` | `fa81a6148c89e47d8032c8b026ee7455f3df684e44829bf77b6862fcb5ff61f6` | clean at HEAD `42322357` |
| `corpus/lessons/round-67.md` | `8d3c8115a5b61fa53dcb12d551f9f30decfee033d8c4488ba3e2663eea3aaf93` | clean at HEAD `42322357` |
| `corpus/lessons/round-67-verifier-spotcheck.md` | `822ec5997b24a8da422ee17905e368b73c1e7dc67bb2fa80c4f4b01e25d56de1` | clean at HEAD |
| `corpus/QUALITY.md` | `811ebf73179a86e0adff18874d0abf2d22e5161ac73c6a04ab3cf21fb51c45d1` | clean at HEAD |
| `.ufo/waves/round-67/source-snapshots/dex-format.html` | `c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4`, 281 157 B | matches lesson `:73` + row anchor |

## 7 · Bounds and tooling

- Files written: **this report only**. Everything else read-only; no edit to `corpus/`, `reports/`,
  `LOG.md`, `SKILL.md`, `SCORECARD.md`, `SHONEN.md`; no git/jj mutation (read-only `rev-parse`/`status`
  only); no subagent; no peer message; no `/home/vgpnk/Projects/shokuknow` access; no
  `corpus/live/` or `corpus/fixtures/` touch.
- Tool installs: **none** (no package or tool needed; counting done with the preinstalled `python3`).

## 8 · Findings / residual

1. **F1 (confirmed, trivial):** `corpus/lessons/round-67.md:75` prints `(18 words)` where the
   whitespace count is 19. Both strings ≤ 25 → conformant. Fix by appended reconciliation (§5), not
   by rewriting the line.
2. **F2 (freshness):** the routed defect §7 item 3 and §5 of the same spotcheck already state
   19 / 14 correctly, so no downstream text propagates the wrong number; the error is one file deep.
3. **F3 (not in scope, noted):** spotcheck §7 item 4 (S045 `used-by` → retained-rejected candidate)
   is a separate routed defect and is untouched here.
4. **Out-of-scope / unresolved dependency:** `corpus/lessons/round-68.md` does not exist yet, so the
   append target is prospective; this seat cannot land the correction (read-only seat, lane bounds).
   Recorded as a hand-off item, not a blocker for the count verdict.
