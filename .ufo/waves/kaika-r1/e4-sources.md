# e4-sources — proposed corpus/SOURCES.md rows (ExecFormatKnowledge)

Eleven-column format per `SOURCES-CONTRACT-v1.md`. Temp ids `T4-N` map onto
real `S` ids at integration. Every row opened 2026-10-19 by this executor;
quotes and locations in `## Gate`.

## Proposed rows

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| T4-1 | PE Format — Microsoft Learn — https://learn.microsoft.com/en-us/windows/win32/debug/pe-format | spec | A | PE .rsrc field layouts: directory table/entry/string/data-entry | `The .rsrc Section` and its four subsections; ms.date 2026-09-10, git_commit_id 55e845e9f3a6a3261f59a2f460f61edc25ffcdd5 | exact offsets, sizes, high-bit flag semantics and the Type/Name/Language tree rule needed to decode a resource tree | mined | 2026-10-19 | 180d | corpus/knowledge/pe-resource-directory-layout.md, corpus/knowledge/utf16-unpaired-surrogates-in-resource-names.md |
| T4-2 | The Unicode Standard 18.0.0 core specification chapter 3 — https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-3/ | spec | A | UTF-16 well-formedness, surrogate definitions, ill-formed sequences | sections 3.8 Surrogates, 3.9 Unicode Encoding Forms, 3.9.2 UTF-16 (D71–D91, Table 3-5, C10); page meta-revision b734c94a21cc49b89c2e1823d65129189a40bf28 | the exact definitions that make a lone surrogate code unit ill-formed and let one classify observed name bytes | mined | 2026-10-19 | on-release | corpus/knowledge/pe-resource-directory-layout.md, corpus/knowledge/utf16-unpaired-surrogates-in-resource-names.md |
| T4-3 | codecs — Codec registry and base classes, Python 3.15.0 documentation — https://docs.python.org/3/library/codecs.html | docs | A | Python codec error-handler semantics: strict default, surrogatepass | `Error Handlers` table, surrogatepass row; 3.4 change note | which documented decode mode rejects versus preserves a lone surrogate, matching observed parser-like behavior | mined | 2026-10-19 | on-release | corpus/knowledge/utf16-unpaired-surrogates-in-resource-names.md |
| T4-4 | Portable Executable — Wikipedia — https://en.wikipedia.org/wiki/Portable_Executable | community | C | PE .rsrc layout or surrogate validity | article lede and Technical details; article accessed 2026-10-19, no revision id recorded | REJECTED: no .rsrc or resource-directory section at all; the lede mentions only "resource management data", so nothing citable beyond T4-1; flip: article grows a field-level resource-tree section or a reproducible byte walkthrough | rejected | 2026-10-19 | — | — |

## Gate

- T4-1 — https://learn.microsoft.com/en-us/windows/win32/debug/pe-format —
  opened 2026-10-19 — §`The .rsrc Section`: "Resources are indexed by a
  multiple-level binary-sorted tree structure."
- T4-2 — https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-3/ —
  opened 2026-10-19 — §3.9.2, bullet under D91: "isolated UTF-16 code units
  in the range D800..DFFF are ill-formed." (subscript hex in source;
  Unicode 18.0.0 index marks the release a preliminary draft — definitions
  cited are stable wording, but the anchor records the draft status.)
- T4-3 — https://docs.python.org/3/library/codecs.html — opened 2026-10-19 —
  Error Handlers table, surrogatepass row: "Allow encoding and decoding
  surrogate code point (U+D800 - U+DFFF) as normal code point."
- T4-4 — https://en.wikipedia.org/wiki/Portable_Executable — opened
  2026-10-19 — lede: "The PE format supports storing the data required to
  load and start an operating system process" — screened and rejected; no
  resource-tree coverage anywhere in the article.

## Search log

Question: what is the on-disk layout of the PE resource directory tree, and
is a lone UTF-16 surrogate inside a resource directory string well-formed?
Where searched: canonical primary sources only — Microsoft Learn PE Format
page (TOC → `The .rsrc Section`), unicode.org `/versions/latest/` (redirects
to 18.0.0; a direct `Unicode17.0.0/ch03.pdf` URL returned 404 and was
excluded unopened), docs.python.org codecs page, and one community screen
(Wikipedia). Date: 2026-10-19. Identified 4 / screened 4 / included 3 /
excluded 1 (T4-4, no .rsrc coverage). Stop rationale: the two primary specs
cover every load-bearing claim in both entries; further secondaries would
add citations without new authority (contract rule 4, no row quota).
Negative sweep for the refusal claim: no source found asserting that any
PE resource parser must reject ill-formed name strings — the C11 entry
records that absence under `## Unknown`.

## Paths

- `decoding a resource name field` — T4-1 → T4-2 → T4-3: learn where the
  name field and its "Unicode strings" claim live in the PE spec, judge the
  bytes' validity against Unicode definitions, reproduce decoder behavior
  with Python's documented error handlers.
