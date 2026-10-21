RESULT: COMPLETE
# R62 source scout — S029 ECMA-262 proposal (frozen a3498e25)
Scope: one proposed tier-A source row for the round-62 C04 candidate. No live
file was edited; no README row held, no gate run, no admission claimed.

## Frozen check
- `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive a3498e25ad87bf756288812d0ea7c474b09433c7 corpus reports/round-62 | tar -x -C frozen` EXIT=0.
- `find frozen -name 'round-62-*.md'` → no output: neither round-62 entry exists at the frozen revision.
- `frozen/corpus/README.md:33` (C04) and `:38` (C09) are `uncovered`; frozen/corpus/SOURCES.md has 27 `S###` rows, `grep -c S029` = 0.
- `git status --porcelain -- corpus reports` in the live lane prints nothing (no live edit by this seat).

## Opened (public spec, read-only)
- https://tc39.es/ecma262/ — HTTP/2 200, `date: Wed, 21 Oct 2026 18:00:24 GMT`,
  `last-modified: Mon, 19 Oct 2026 16:26:55 GMT`, etag `"6ad644cf-7469d7"`, 7,629,271 B,
  sha256 `06db92a8331aa452b0d4de8c8938f4b7559b72417769b57d0032002398f27d7f`.
- multipage chapters (same build): `ecmascript-language-statements-and-declarations.html`
  last-modified 16:26:52Z, sha256 `a23fc93cf4a31708bd9dc4b89c1b66c6150fff41f7198d5c6f91819e5fc8813e`, 956,160 B;
  `ecmascript-language-scripts-and-modules.html` last-modified 16:26:55Z,
  sha256 `a544440624a11661a35e9b75934fe916a86078b9a94f7b6b25ea239b66b136d4`, 1,033,596 B.

## Draft identity and clauses (derived from those bytes)
`python3 -B s029_derive.py` (scratch; reads only the three fetched files) prints:
```text
version-line: Draft ECMA-262 / October 16, 2026
title-line: ECMAScript® 2027 Language Specification
single 14.3.3.3: Runtime Semantics: KeyedBindingInitialization
single 16.1: Scripts / single 16.2: Modules / single 16.2.2: Imports
single 16.2.2.2: Static Semantics: ImportEntries
table54-caption: Table 54: ImportEntry Record Fields
```
`16.2.2` is confirmed as `Imports` under `16.2 Modules`; `16.2.2.2` is the
static-semantics operation returning ImportEntry Records. Same headings in the
multipage chapters.

## Quotes (verbatim, ≤25 words)
Q1 §14.3.3.3: "Set value to ? GetV(value, propertyName)." — 6 words (whitespace split);
  caveat: the same step also occurs in §13.15.5.3/§13.15.5.6, so it is clause-sliced.
Q2 §16.2.1.7 Table 54 `[[ImportName]]`: "The name under which the desired binding is
  exported by the module identified by [[ModuleRequest]]." — 15 words.

## Proposed row (status queued; not written live)
| S029 | ECMAScript 2027 Language Specification (draft) — https://tc39.es/ecma262/ | spec | A | the draft's language-level semantics only: the property-read step of object destructuring binding initialization and the static ImportEntry name fields; no engine, loader, parser, bundler or graph-producer behaviour | §14.3.3.3 `#sec-runtime-semantics-keyedbindinginitialization`; §16.2.1.7 Table 54 `#table-importentry-record-fields`; §16.2.2 `#sec-imports`; §16.2.2.2 `#sec-imports-static-semantics-importentries`; single-page SHA-256 `06db92a8331aa452b0d4de8c8938f4b7559b72417769b57d0032002398f27d7f`, 7,629,271 bytes, fetched 2026-10-21T18:00:24Z | Object destructuring initialization sets the bound value from `GetV(value, propertyName)` on the already-evaluated value; an ImportEntry's `[[ImportName]]` is the export name under which the requested module exports the binding, produced by static semantics over module code. | queued | 2026-10-21 | on-release | — |

## Row validated on the frozen copy (no live write)
`…/scripts/sources-census.sh validate --file corpus/SOURCES-s029.md --today 2026-10-21`
run from `frozen/`:
```text
file	W04	S029 duplicate url tc39.es/ecma262 across scopes
file	ok	…/frozen/corpus/SOURCES-s029.md        EXIT=0
```
Baseline frozen registry (no S029): only the pre-existing S024 W04, EXIT=0. A variant
copying S022's exact scope returns `E04 … duplicate url tc39.es/ecma262 within scope …`,
EXIT=1 — the distinct scope keeps S029 a warning, not an error.

## Scope boundary
- S022 already cites this URL for "evaluation of destructuring binding patterns and the
  separation of ImportDeclaration from scripts". The contract lets only status/recheck/
  used-by change in place, so its scope cannot be widened; S029 names the two name-level
  facts (`GetV` property read, ImportEntry `[[ImportName]]` meaning) and nothing else.
- Tier A only for those language-semantic statements. This row cannot support Node,
  CommonJS detection, Electron, parser/producer behaviour, or any saved-field
  correspondence; S023/S027 must carry those separately.
- Query "does the draft equate a destructuring binding name with an import name?" — no opened text does; the roles sit in different clauses with different origins.
- If no new W04 is wanted, the multipage chapter URL is the same build and would avoid
  the warning; not proposed, because the canonical single page is what was opened.

## Unknowns
- No source commit id on the page: binding is version line + Last-Modified + SHA-256; a
  living draft (2027 edition, version line 2026-10-16), recheck `on-release`.
- Q1 is not document-unique (assignment-destructuring clauses repeat the step).
- Nothing here establishes that a saved import field came from source or corresponds to
  a destructuring name; that remains the entry's own observation and inference.
## Artifacts (scratch only)
/fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62SourceEcma/
- `s029-row-proposal.md` (row, field rationale, validation, do-not list, variant)
- `s029-quotes.md` (Gate quote log: dates, anchors, quotes, word counts, limits)
- `s029_derive.py`, `s029-derivation.txt`, `SOURCES-s029.md`, `frozen/` (archive a3498e25),
  fetched bytes and `headers-*.txt` for all three URLs

No installs or updates. No live corpus/report edit, no README hold flip, no admission.
