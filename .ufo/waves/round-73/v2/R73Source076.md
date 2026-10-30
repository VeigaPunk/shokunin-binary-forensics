# R73Source076 — S076 source audit (round-73 v2 wave, lane revenger-shokunin)

Seat: `R73Source076` · role: source-audit reviewer (round-72 source set) · leaf member, no dispatch.
Lane root: `/home/vgpnk/Projects/shokunin/revenger-shokunin`. Claim context: frozen C10
(`reports/round-73/claims.md`, counter `reports/round-73/measure.py`). S076 is **not** in the
C10 required source set (`source_ok` checks S096–S109 only); this seat is one of the 42
round-72 source audits and has no effect on the frozen predicate either way.

## Assigned row under review

Locator: `corpus/SOURCES.md:90` (registry row S076), Gate wording `corpus/lessons/round-72.md:35`,
used-by entry `corpus/knowledge/round-72-tool-landscape.md:3,37`.

Row content (verbatim from the registry, 11 columns): kind `docs`; tier `A`; scope "The prompts
contract for optional guidance, tool calls, and untrusted argument data in this pinned REA
snapshot"; anchor "Guided MCP prompts and completion" and "Lifecycle and safety", commit
b675073b731dc3209f59578fad5ca8fe85b104cc, accessed 2026-10-27; "Requested prompt arguments and
completion choices are rendered as untrusted selection data, not instructions or authorization.";
teaches "Prompt content and selections are not authorization; RE data and strings from binaries
must remain untrusted inputs, not agent instructions"; status `mined`; opened 2026-10-27; recheck
`on-release`; used-by `corpus/knowledge/round-72-tool-landscape.md`. No rejection flip is claimed
or needed for this row.

## Primary re-open (my own fetch)

- URL: `https://raw.githubusercontent.com/morluto/rea/b675073b731dc3209f59578fad5ca8fe85b104cc/docs/mcp-prompts.md`
  (registry URL is the blob view of the same commit and path).
- Access date: **2026-10-30**. HTTP 200, 8137 bytes, sha256
  `56acd853077ba8935e9dd7bab7785ecae225a8af7749f9c92666545d0ece351f`.
- Commit metadata: GitHub API reports commit `b675073b…` committed 2026-10-26T11:50:12Z —
  consistent with the row's "accessed 2026-10-27" (access date, not authorship) and with the
  used-by entry's "last file revision 2026-10-26".
- Located quote found spanning **lines 29–30** (soft line wrap inside the sentence), after
  whitespace-only normalization, with surrounding context:

  > The prompts also ask agents to keep observations, inferences, and unknowns distinct. Requested
  > prompt arguments and completion choices are rendered as untrusted selection data, not
  > instructions or authorization. Tool results include their Evidence inline.

- Both anchor headings are present: `# Guided MCP prompts and completion` (line 1) and
  `## Lifecycle and safety` (line 135). The quote sits in the prompt-inventory prose under the
  first heading; the "suggestions are starting points, not tool calls" contract sits under
  "Lifecycle and safety" (lines 141–144), supporting the teaches cell's second clause.
- Byte-exact substring check without wrap normalization fails **only** because the source wraps
  the sentence across two source lines; after collapsing whitespace (markup/wrap normalization
  only, no word changes) the quote is an exact substring. No words differ.

## Located quote returned (≤25 words)

> "Requested prompt arguments and completion choices are rendered as untrusted selection data,
> not instructions or authorization."

16 words. Access date 2026-10-30. URL
`https://github.com/morluto/rea/blob/b675073b731dc3209f59578fad5ca8fe85b104cc/docs/mcp-prompts.md`
(raw file sha256 above, 8137 bytes). Normalization: one soft line-wrap collapsed to a single
space; all sixteen words, order, and punctuation verbatim.

## Verbatim comparison and field checks

| Check | Result | Evidence |
|---|---|---|
| Quote verbatim in cited source at cited pin | **PASS** | Exact substring after wrap normalization, pinned file lines 29–30 (sha256 above). |
| Quote word count ≤25 | **PASS** | 16 words. |
| Scope column supported | **PASS** | Pinned file: prompts are "optional starting points" (line ~27), "Suggestions are starting points, not tool calls" (lines 141–142), and the untrusted-selection-data sentence (lines 29–30) — exactly "optional guidance, tool calls, and untrusted argument data". |
| Tier A appropriate | **AGREE** | First-party project documentation at an exact commit pin; tier A for the documented contract only, not a run claim — registry convention. |
| used-by | **CONSISTENT** | `round-72-tool-landscape.md:3` (source header: "scope is prompt/data boundaries and generated workflow semantics") and `:37` (table row "REA MCP prompt contract S076": "prompt arguments are untrusted selection data, not instructions or authorization; prompts do not themselves invoke tools"). The second clause is backed by lines 141–142 ("Suggestions are starting points, not tool calls… selecting a suggestion does not execute it"). |
| Rejection flip | **N/A — none claimed, none needed** | Row is `mined`; Gate decision "ADMIT, tier A for the pinned prompt/data contract; used to bound this entry's source handling" matches the row's scope and teaches cells. |
| Lesson Gate vs registry wording | **CONSISTENT** | `round-72.md:35` carries the identical quoted sentence and the same "ADMIT, tier A" decision; only curly-vs-straight quotation marks differ (markup). |
| Round-72 spotcheck precedent | **CONSISTENT** | S076 is not mentioned in `corpus/lessons/round-72-verifier-spotcheck.md`; no routed defect exists for this row, unlike S071/S082. |
| Drift note (recheck = on-release) | **OBSERVED** | File at `main` differs from the pin (main sha256 `423b17523bb7cad4aef4e84a33f381ad52cfe5fecaa806247b7a74ddb474f422`) but the quoted sentence is still present on main. The read-only checkout `~/.local/share/rea` (HEAD `12f6e09…`, a different commit from the pin) also carries the sentence at its line 23. No quote-threatening drift observed. |
| Duplicate registry id | **PASS** | `grep -c "^| S076 "` over `corpus/SOURCES.md` = 1 (S071+S076 control count = 2). |

## Disposition

**AGREE** with the source disposition: ADMIT (status `mined`), tier A, scope limited to the pinned
REA snapshot's documented prompt/data contract; no runtime, coverage or authorization claim is
made or implied. The located quote is verbatim at the cited pin, the scope and teaches cells are
verbatim-backed, and the used-by entry matches. **No defect found for S076; no superseding row is
proposed for this row.**

## S071/S082 routed quote defects (context, not my admission)

Observation: `round-72-verifier-spotcheck.md` routes two defects — S071's registry quote is a
paraphrase of the pinned README and S082's quote is misattributed to S083. Append-only
superseding rows already exist in the registry: **S427** (`corpus/SOURCES.md:442`, correction of
the S071 catalog-screening quote, tier C retained) and **S428** (`corpus/SOURCES.md:443`,
correction of S082 source attribution to the v3 abstract's stated motivation). Old rows were not
edited. Per my seat bound ("report only your assigned row") and the claim freeze ("New source
admission is a separate Q review"), this seat proposes **no additional row** and admits nothing;
verification of S427/S428 belongs to their own assigned seats.

## C10 predicate impact

None. `measure.py source_ok` requires S096–S109 only; S076 is outside that set. S076's only
used-by is the round-72 C15 candidate entry, which is not this round's claim surface and remains
`admission-status: candidate` outside this round's edit authority.

## Failure statement

No network or source failures. All remote fetches succeeded (raw file HTTP 200; GitHub commits
API 200; raw main file HTTP 200). No tool installs or updates this seat (curl/python3/grep
pre-existing; nothing installed, no PATH directory touched, no pacman transaction attempted —
host-wide pacman pause respected).

## Observation / inference / unknown

- **Observation:** quote verbatim at the pinned commit (lines 29–30, sha256 above); commit date
  2026-10-26T11:50:12Z; both anchor headings present; sentence still present on `main` and in the
  local checkout at HEAD 12f6e09; registry/lesson/entry fields mutually consistent; single
  registry occurrence of S076.
- **Inference:** none needed; every checked field is directly evidenced by the cited bytes. The
  line-wrap split is a source-formatting artifact, not a quote defect (byte-exact match after
  collapsing the wrap).
- **Unknown:** nothing material for this row. (Non-material: full diff content between the pin
  and `main`; only presence of the quoted sentence on main was checked, not line-level identity.)

Scratch `/fast/scratch/hyaku/revenger-r73/R73Source076/` (two downloaded `mcp-prompts.md` copies,
pinned and main) removed after receipts (sha256s, byte count, line numbers, access dates) were
copied into this report.
