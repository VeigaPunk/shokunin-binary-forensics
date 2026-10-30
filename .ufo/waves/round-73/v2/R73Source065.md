# R73Source065 — S065 source audit (round-73 v2 wave, lane revenger-shokunin)

Seat: `R73Source065` · role: source-audit reviewer (round-72 source set) · leaf member, no dispatch.
Lane root: `/home/vgpnk/Projects/shokunin/revenger-shokunin`. Claim context: frozen C10
(`reports/round-73/claims.md`, counter `reports/round-73/measure.py`, pin
`reports/round-73/candidate-pin.json`). S065 is **not** in the C10 required source set
(`source_ok` checks S096–S109 only); this seat is one of the 42 round-72 source audits and has
no effect on the frozen predicate either way.

## Assigned row under review

Locator: `corpus/SOURCES.md:79` (registry row S065; exactly one S065 row in the registry, no
duplicate id), Gate wording `corpus/lessons/round-72.md:24`, used-by entry
`corpus/knowledge/round-72-tool-landscape.md:24`.

Row content (verbatim from the registry, 11 columns): source `angr — https://github.com/angr/angr`;
kind `tool`; tier `A`; scope "The repository's own list of Python binary-analysis libraries and
operations; no benchmark or version performance inference"; anchor `README.md "What is angr?",
commit d38cc5a0196d8120ef5a21efc12c0a22435e7be5, accessed 2026-10-27; "angr is a platform-agnostic
binary analysis framework."`; teaches "The README names disassembly, symbolic execution,
control-flow/data-dependency analysis and decompilation as framework functions; it does not
establish result truth"; status `mined`; opened 2026-10-27; recheck `on-release`; used-by
`corpus/knowledge/round-72-tool-landscape.md`.

Round-72 Gate decision (`corpus/lessons/round-72.md:24`): "ADMIT, tier A for declared framework
scope; the project page's feature descriptions are not a benchmark."

## Primary re-open (my own fetch)

- URL: `https://raw.githubusercontent.com/angr/angr/d38cc5a0196d8120ef5a21efc12c0a22435e7be5/README.md`
- Access date: **2026-10-30** (fetch at 2026-10-30T15:52:09Z). HTTP 200, 2638 bytes,
  sha256 `fb2cc79a308bd478c3420db0bb54d38df5c9f4c1c1db1405515849a50b1ba4a4`.
- Located quote found at **line 8**, verbatim, exact full source line, no markup normalization
  needed (plain text, byte-for-byte match including the trailing period):

  > angr is a platform-agnostic binary analysis framework.

- Section structure of the fetched README: line 7 `# angr` H1 (after the badge block), line 8 the
  quoted sentence, line 20 `## What is angr?`, lines 24–30 the operations bullet list:
  "Disassembly and intermediate-representation lifting", "Program instrumentation",
  "Symbolic execution", "Control-flow analysis", "Data-dependency analysis",
  "Value-set analysis (VSA)", "Decompilation".

## Located quote returned (≤25 words)

> "angr is a platform-agnostic binary analysis framework."

7 words (`wc -w`). Access date 2026-10-30. URL `https://github.com/angr/angr` (README at commit
`d38cc5a0196d8120ef5a21efc12c0a22435e7be5`, raw file sha256 above). No markup normalization was
needed: the quoted span is plain text and matches byte-for-byte.

## Verbatim comparison and field checks

| Check | Result | Evidence |
|---|---|---|
| Quote verbatim in cited source at cited pin | **PASS** | Exact substring, line 8 of fetched pinned README (sha256 above); whole-line match. |
| Quote word count ≤25 | **PASS** | 7 words. |
| Section anchor `README.md "What is angr?"` | **OFFSET (minor)** | The quoted sentence is at line 8, in the lede directly under the `# angr` H1, **before** the `## What is angr?` H2 at line 20. The anchor's section label is ~12 lines off; the quote itself is verbatim at the cited commit. Observation, not a quote defect (contrast S071 paraphrase / S082 misattribution below). |
| Scope column supported | **PASS** | Line 22 ("angr is a suite of Python 3 libraries that let you load a binary and do a lot of cool things to it:") plus lines 24–30 operations list — the row's "own list of Python binary-analysis libraries and operations" is verbatim-backed; the README makes no benchmark or version-performance claim. |
| Teaches column supported | **PASS** | Lines 24–30 name Disassembly, Symbolic execution, Control-flow analysis, Data-dependency analysis and Decompilation verbatim; no result-truth/benchmark statement appears in the README. |
| Tier A appropriate | **AGREE** | Primary project repository's own README; tier A for declared framework scope only is the registry convention. |
| used-by | **CONSISTENT** | `round-72-tool-landscape.md:24` cites "angr S065" and describes "angr describes a Python binary-analysis framework including symbolic execution" — within the row's scope; no other used-by claims (S065 absent from the C10 candidate and all other knowledge files). |
| Rejection flip | **N/A — none claimed, none needed** | Row is `mined`, tier A; Gate decision matches the row's scope and teaches cells; no rejected status to flip. |
| Lesson Gate vs registry wording | **CONSISTENT** | Both carry the identical quoted string; the Gate adds only the "README "What is angr?"": locator label, which carries the same minor offset noted above. |
| Round-72 spotcheck precedent | **CONSISTENT** | `corpus/lessons/round-72-verifier-spotcheck.md` routes only S071 and S082 as quote defects; S065 is not among them, and this re-open finds S065's quote verbatim. |

## Disposition

**AGREE** with the source disposition: ADMIT (status `mined`), tier A, scope limited to the
repository's own declared framework and operations list; no benchmark or version-performance
inference. The quote is verbatim at the pinned commit, the scope and teaches cells are
verbatim-backed by the `## What is angr?` bullet list, and the used-by entry matches. One minor
observation recorded: the anchor's `What is angr?` section label sits ~12 lines below the actual
quote position (lede under the H1); this is a locator-label offset only and does not change any
disposition field. No defect of the S071/S082 class (paraphrase/misattribution) found for S065;
no superseding row proposed for this row.

## S071/S082 routed quote defects (context, not my admission)

Observation: `corpus/lessons/round-72-verifier-spotcheck.md` routes two defects — S071's registry
quote is a paraphrase ("Each repo is read and security-graded" vs the pinned README's "each one
read and security-graded", spotcheck line 71) and S082's quote is misattributed (the
"readable/compilable but deviates" sentence belongs to AutoDecompiler S083, not LLM4Decompile,
spotcheck line 72). Append-only superseding rows already exist in the registry: **S427**
(`corpus/SOURCES.md:442`, supersedes S071, verbatim "each one read and security-graded", tier C
rejected retained) and **S428** (`corpus/SOURCES.md:443`, supersedes S082 with the LLM4Decompile
v3 abstract's own motivation sentence), with primary re-opens recorded in
`corpus/lessons/round-73.md` Gate (2026-10-30). Old rows were not edited. Per the claim freeze
("New source admission is a separate Q review") and my seat bound ("report only your assigned
row"), this seat proposes **no additional row** and admits nothing; S427/S428 verification
belongs to their own assigned seats.

## C10 predicate impact

None. `measure.py source_ok` requires S096–S109 only; S065 is outside that set and does not
appear in the C10 candidate `corpus/knowledge/2026-10-29-rea-evidence-ledger-discipline.md`
(grep: no hits). S065's only used-by is the round-72 tool-landscape entry, not this round's
claim surface.

## Failure statement

No network or source failures. The remote fetch succeeded on first attempt
(raw README HTTP 200). No tool installs or updates this seat (curl/sha256sum/grep pre-existing;
nothing installed, nothing in `~/.local/bin` or any PATH directory touched; pacman pause
respected — no transaction attempted).

## Observation / inference / unknown

- **Observation:** quote verbatim at pinned commit d38cc5a0 (line 8, sha256 above, 7 words);
  operations list at lines 24–30; registry/lesson/entry fields mutually consistent; single S065
  row, no duplicate registry id.
- **Inference:** none needed for disposition; every checked field is directly evidenced by the
  cited bytes. (Minor: the anchor's section label points to `## What is angr?` while the quote
  sits in the H1 lede — inferred to be a locator-label offset because the quote is an exact
  whole-line match 12 lines above that H2.)
- **Unknown:** nothing material for this row. (Non-material: whether the angr README changed at
  commits after d38cc5a0 — the row's `recheck: on-release` already schedules that re-check.)

Scratch `/fast/scratch/hyaku/revenger-r73/R73Source065/` (one downloaded README) removed after
receipts (sha256, byte count, line numbers, access dates) were copied into this report.
