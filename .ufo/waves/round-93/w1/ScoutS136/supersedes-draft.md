# Round 93 — routed defect 4: the S136 supersedes correction row (seat ScoutS136)

One new SOURCES row for the L1 to append to `corpus/SOURCES.md` (append-only; the
L1 alone writes that file). I do not edit `corpus/SOURCES.md` myself.

**Id: S497.** Current registry maximum is S494 (`grep -oE '^\| S[0-9]+'
corpus/SOURCES.md | tail -1` → `S494`). `claims.md` reserves **S495** (the saved
round-77 CDP record) and **S496** (Chrome DevTools Protocol) for the sibling
scout seat ScoutRecord, which it confirmed by message; **S497** is therefore the
first free id after the two reserved ones. No id is reused or duplicated.

This row opens the ECMA-335 addendum that S136's scope cell records as
"unopened — see LEADS", in the SOURCES rule-2 correction form: a new row whose
`teaches` opens `supersedes S136 —`. S136's own cells stay byte-frozen (only
`status`, `recheck` and `used-by` may change in place).

## The row (11 columns, no `|` inside any cell)

```
| S497 | .NET runtime ECMA-335 addendum (Ecma-335-Augments.md) — https://raw.githubusercontent.com/dotnet/runtime/b22bfee2010118c58ae143c3b8a1aaee3d0c8c4c4/docs/design/specs/Ecma-335-Augments.md (docs, tier A, opened 2026-11-05) | docs | A | the .NET runtime team's own document of the additions and edits it proposes to ECMA-335 at this commit — proposed heap-size limits for the #String and #Blob heaps, the metadata-merging and metadata-logical-format spec-bug findings, and the module-initializer rules — mixing definite spec errors with implementation quirks; not the ECMA-335 standard text itself, not any runtime behaviour, and not evidence that any proposal was adopted | ECMA-335 CLI Specification Addendum (title) and preamble paragraph (line 3); commit b22bfee2010118c58ae143c3b8a1aaee3d0c8c4c4 (2026-10-18); blob 6a929a15f286e5c0f95e92050d7eece7e819fddf; body 69577 bytes sha256 1e6e225aa41cd1ccf957b3c13ec4682fc6be2265327c3632f2e8fa01279b0828 — "This is a list of additions and edits to be made in ECMA-335 specifications." | supersedes S136 — S136's scope cell records the .NET runtime addendum as unopened; this row opens it and scopes it to the runtime team's own proposals and spec-bug findings, so the standard text and the vendor's proposed departures stay separable | mined | 2026-11-05 | 180d | — |
```

Cell values, one by one:

| cell | value |
|---|---|
| id | `S497` (first free id after the reserved S495/S496) |
| source | `.NET runtime ECMA-335 addendum (Ecma-335-Augments.md)` — the raw URL **pinned at commit** `b22bfee2010118c58ae143c3b8a1aaee3d0c8c4c4` |
| kind | `docs` (a design/spec prose document in the runtime repo, not the ECMA-335 standard itself) |
| tier | `A` — scoped to the addendum's own scope only: the .NET runtime team's own statement of what it proposes to change in ECMA-335. Not tier A for the CLI metadata layout (that stays with S136/S491/S492). |
| scope | the addendum's own content: proposed `#String`/`#Blob` heap-size limits, the metadata-merging and metadata-logical-format spec-bug findings, the module-initializer rules; excludes the standard text, runtime behaviour, and adoption of any proposal |
| anchor | document title + preamble paragraph (line 3) + the pinned commit + blob sha + body length/sha256, then the located quote |
| teaches | opens exactly `supersedes S136 —` and states the change: the addendum is opened and its content scoped |
| status | `mined` (opened and read this round; the located quote and receipt below) |
| opened | `2026-11-05` |
| recheck | `180d` |
| used-by | `—` (nothing cites it yet) |

## Fetch receipt (this round)

- **URL fetched:** `https://raw.githubusercontent.com/dotnet/runtime/b22bfee2010118c58ae143c3b8a1aaee3d0c8c4c4/docs/design/specs/Ecma-335-Augments.md`
- **HTTP status:** `200`
- **Fetched at:** 2026-11-05 (this round)
- **Body sha256:** `1e6e225aa41cd1ccf957b3c13ec4682fc6be2265327c3632f2e8fa01279b0828`
- **Body length:** `69577` bytes (69490 characters after UTF-8 decode)
- **Blob sha at the pinned commit** (GitHub trees API, `docs/design/specs/Ecma-335-Augments.md`): `6a929a15f286e5c0f95e92050d7eece7e819fddf` — matches the blob sha recorded by the r92 scout, so the pinned bytes are the same document the r92 scout read.
- **Pinned commit metadata** (commits API): `b22bfee2010118c58ae143c3b8a1aaee3d0c8c4c4`, authored 2026-10-18T00:55:49Z ("ilverify: allow ldsflda of initonly static fields outside the cctor (#135994)") — the last commit touching this path, per the path history.
- **Body saved as evidence:** `.ufo/waves/round-93/w1/ScoutS136/Ecma-335-Augments.md` (and the identical copy at `.ufo/waves/round-93/w1/ScoutS136/quote-receipts/raw/S497.body`), both sha256 `1e6e225a…`.
- **Cross-check:** the same path fetched from `…/main/…` this round returns a byte-identical body (same sha256), and the bytes are identical to the r92 snapshot `.ufo/waves/round-92/w1/ScoutR92Managed/snapshots/Ecma-335-Augments.md` (sha256 `1e6e225a…`).

**Correction to the task brief's background.** The brief says r92's scout opened
`https://github.com/dotnet/ecma-335/blob/main/docs/Ecma-335-Augments.md`
(HTTP 200, blob `6a929a15…`, commit `b22bfee2`, 2026-10-18). The repository
`github.com/dotnet/ecma-335` **does not exist** — `https://github.com/dotnet/ecma-335`
and its `/blob/main/docs/Ecma-335-Augments.md` both return **HTTP 404**, and the
GitHub API returns 404 for the repo, its commit `b22bfee2` and its tree. The blob
sha `6a929a15…` and commit `b22bfee2…` in the brief are real, but they belong to
**`dotnet/runtime`**, path `docs/design/specs/Ecma-335-Augments.md` — which is also
the URL the r92 scout actually recorded in
`.ufo/waves/round-92/w1/ScoutR92Managed/sources.md:176` and the URL S136's own
scope cell names. The row above uses the verified `dotnet/runtime` URL.

## Located quote (≤25 words, located in the saved bytes)

> "This is a list of additions and edits to be made in ECMA-335 specifications."

- **Location in the fetched body:** line **3** of
  `.ufo/waves/round-93/w1/ScoutS136/Ecma-335-Augments.md` (the preamble paragraph
  directly under the `# ECMA-335 CLI Specification Addendum` title).
- **Byte/char span:** characters **39–115** of the UTF-8-decoded body (byte-exact
  slice `body[39:115]` == the quote); the quote is 14 words.
- It is the anchor cell's **last** double-quoted segment, which is the quote
  `corpus/audit_source_quotes.py` extracts (`anchor_quote`).

Sections actually read in the fetched body (line numbers in the saved file):
`## Changes by feature area` (5, 23 feature-area bullets at lines 7–29),
`## Signatures` (31), `## Heap sizes` (316, "We propose the limit on #String and
#Blob heap size is 2^29 (0.5 GB)…" at 322), `## Metadata merging` (332, "The CLI
does not merge metadata." at 334), `## Metadata logical format` (357),
`## Module Initializer` (371, "A module initializer is defined as the type
initializer (§ II.10.5.3) of the `<Module>` type (§ II.10.8)." at 373).

## Self-check with the lane's own quote auditor (no lane file modified)

Receipt written to `.ufo/waves/round-93/w1/ScoutS136/quote-receipts/S497.receipt.json`
(schema `revenger-quote-audit-v1`, verdict `verified`, span 39–115, body
`quote-receipts/raw/S497.body`).

On a scratch copy of `corpus/SOURCES.md` with this row appended (the lane file
itself untouched):

```
$ python3 -B corpus/audit_source_quotes.py verify --sources <scratch copy> \
    --receipts .ufo/waves/round-93/w1/ScoutS136/quote-receipts --sid S497
S497 terminal=S497 state=verified (ok)
SUMMARY rows=1 verified=1 unreachable=0 unresolved=0          (exit 0)

$ python3 -B corpus/audit_source_quotes.py chains --sources <scratch copy> --range 130-140
S131 -> S441
S136 -> S497
TERMINALS=11/11
```

Registry census on the same scratch copy (SOURCES contract commands): rows
495 (494 + this row), malformed rows `0`, tier histogram `A=446 B=21 C=28`,
status histogram `mined=459 queued=16 rejected=20`, duplicate ids **none**,
enum violations **none**, mined rows with a missing `used-by` path **none**.

## Notes for the L1 (not defects in frozen files)

1. **Receipts live in wave dirs, the counter reads `reports/round-93/quote-receipts/`.**
   `c1_k_admit_counter2.py` runs `audit_source_quotes.py verify --receipts
   reports/round-93/quote-receipts --sid <sid>` for every external row the C08
   entry header cites. My receipt is at
   `.ufo/waves/round-93/w1/ScoutS136/quote-receipts/S497.receipt.json` (plus
   `raw/S497.body`); the sibling seat's S496 receipt is at
   `.ufo/waves/round-93/w1/ScoutRecord/quote-receipts/S496.receipt.json`. Both
   need copying into `reports/round-93/quote-receipts/` (with `raw/`) for the
   C1_QUOTES leg to see them. S497 itself is not cited by the C08 entry, so its
   receipt is not on the C1 critical path — but the S136 chain change below makes
   it worth landing.
2. **The chain re-points S136.** Because this row's `teaches` opens
   `supersedes S136 —`, `audit_source_quotes.py` now resolves S136's terminal to
   S497 (`chains` output above). No S136 receipt exists anywhere in the repo, so
   nothing regresses; but any future quote verification scoped to S136 will now
   look for `S497.receipt.json`. Landing the receipt alongside the row keeps
   that resolvable.
3. **`status: mined` with `used-by: —`.** The task specifies this, and it is the
   only such row in the registry today (every other `mined` row names a citing
   path). SOURCES rule 1 expects the round lesson's `## Gate` to record every new
   row's URL, access date and quote, so the round-93 lesson will cite S497; the
   L1 can set `used-by` to `corpus/lessons/round-93.md` when it lands that
   lesson (an in-place change, loggable as old→new), which also satisfies the
   census check "mined rows whose used-by paths do not exist". If the L1 prefers
   to keep `—`, the row is still consistent with the contract's enum checks.
4. **`kind: docs`, not `spec`.** The addendum is the .NET runtime team's own
   design document, not the ECMA-335 standard; the standard stays with S136/S491
   (spec, tier A). The row's scope cell says so explicitly, so the tier-A claim
   does not bleed into the standard's own authority.
