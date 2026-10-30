# R73Source075 — S075 source audit (round-73 v2 wave, lane revenger-shokunin)

Seat: `R73Source075` · role: source-audit critic (round-72 source set) · leaf member, no dispatch.
Lane root: `/home/vgpnk/Projects/shokunin/revenger-shokunin`. Claim context: frozen C10
(`reports/round-73/claims.md`, counter `reports/round-73/measure.py`, pin
`reports/round-73/candidate-pin.json`). S075 is **not** in the C10 required source set
(`source_ok` checks S096–S109 only); this seat is one of the 42 round-72 source audits and has
no effect on the frozen predicate either way.

## Assigned row under review

Locator: `corpus/SOURCES.md:89` (registry row S075), Gate wording `corpus/lessons/round-72.md:34`,
used-by entry `corpus/knowledge/round-72-tool-landscape.md:2,36`.

Row content (verbatim from the registry, 11 columns): kind `docs`; tier `A`; scope "The project's
setup preview and approval statements only; not evidence of installation or readiness on this
host"; anchor "Installation and setup" and "Review setup changes", commit
0cd7ef456bf960da265e04b341e82a24b1e377d5, accessed 2026-10-27; "Setup previews configuration
changes and asks for approval before applying them."; teaches "A setup plan is described as
reviewable and approval-gated; this lane did not run setup or install any tool"; status `mined`;
opened 2026-10-27; recheck `on-release`; used-by `corpus/knowledge/round-72-tool-landscape.md`.
No rejection flip is claimed or needed for this row.

## Primary re-open (my own fetch)

- URL: `https://raw.githubusercontent.com/morluto/rea/0cd7ef456bf960da265e04b341e82a24b1e377d5/docs/installation.md`
  (registry URL is the blob view of the same commit and path).
- Access date: **2026-10-30**. HTTP 200, 105202 bytes, sha256
  `c4a16fa00f39d08267098dc56c688a008cc6455a0dc3024baf333b95770003ac`.
- Commit metadata: GitHub API reports commit `0cd7ef4…` committed 2026-10-27T17:13:17Z —
  consistent with the row's "accessed 2026-10-27" (access date, not authorship).
- Located quote found at **line 4** of the pinned file, exact single-line substring, no
  normalization needed:

  > Setup previews configuration changes and asks for approval before applying them.

- Both anchor headings are present: `# Installation and setup` (line 1) and
  `## Review setup changes` (line 36). The quote sits directly under the first heading; the
  second heading's section describes reviewing "the plan's exact paths and changes" and approving
  "before applying" (lines 51–52), backing the teaches cell.

## Located quote returned (≤25 words)

> "Setup previews configuration changes and asks for approval before applying them."

11 words. Access date 2026-10-30. URL
`https://github.com/morluto/rea/blob/0cd7ef456bf960da265e04b341e82a24b1e377d5/docs/installation.md`
(raw file sha256 above, 105202 bytes). Normalization: none — byte-exact single-line substring at
line 4 of the pinned file.

## Verbatim comparison and field checks

| Check | Result | Evidence |
|---|---|---|
| Quote verbatim in cited source at cited pin | **PASS** | Byte-exact substring, pinned file line 4 (sha256 above). No wrap, no word change, no markup delta. |
| Quote word count ≤25 | **PASS** | 11 words. |
| Scope column supported | **PASS** | Pinned file is entirely documentation of the approval-gated setup flow (preview/approve/`--dry-run` semantics throughout, e.g. lines 4, 36, 51, 273–296); it is not host-specific run evidence — matching "setup preview and approval statements only; not evidence of installation or readiness on this host". |
| Tier A appropriate | **AGREE** | First-party project documentation at an exact commit pin; tier A for the documented setup policy only, not a run claim — registry convention. |
| used-by | **CONSISTENT** | `round-72-tool-landscape.md:2` (source header: "scope is the documented approval boundary, not this lane's configuration") and `:36` (table row "REA setup docs S075": "The documented setup plan previews configuration changes and requires approval before applying them"). Both clauses are backed by the pinned file. |
| Rejection flip | **N/A — none claimed, none needed** | Row is `mined`; Gate decision "ADMIT, tier A for REA's own setup policy; no setup was run." matches the row's scope and teaches cells. |
| Lesson Gate vs registry wording | **CONSISTENT** | `round-72.md:34` carries the identical quoted sentence ("Setup previews configuration changes and asks for approval before applying them.") and the same ADMIT decision; only curly-vs-straight quotation marks and the added section-title prefix differ (markup). |
| Round-72 spotcheck precedent | **CONSISTENT** | S075 is not mentioned in `corpus/lessons/round-72-verifier-spotcheck.md`; no routed defect exists for this row, unlike S071/S082. |
| Drift note (recheck = on-release) | **OBSERVED** | File at `main` differs from the pin (main sha256 `67565c2fef10666b19183f01412102aaf8e1033fa140874087617e36ed453f2b`) but the quoted sentence is still present on main at line 4. The read-only checkout `~/.local/share/rea` (HEAD `12f6e09…`, a different commit from the pin) also carries the sentence at its line 4. No quote-threatening drift observed. |
| Duplicate registry id | **PASS** | `grep -c "^| S075 "` over `corpus/SOURCES.md` = 1. |

## Disposition

**AGREE** with the source disposition: ADMIT (status `mined`), tier A, scope limited to the pinned
REA snapshot's documented setup preview/approval policy; no installation, readiness, or coverage
claim is made or implied. The located quote is verbatim at the cited pin, both anchor headings
exist, the scope and teaches cells are verbatim-backed, and the used-by entry matches.
**No defect found for S075; no superseding row is proposed for this row.**

## S071/S082 routed quote defects (context, not my admission)

Observation: `round-72-verifier-spotcheck.md` routes two defects — S071's registry quote is a
paraphrase of the pinned README and S082's located quote is misattributed (the "readable but
deviates" sentence belongs to S083's source). Per my seat bound ("report only my assigned row")
and the claim freeze ("New source admission is a separate Q review"), this seat proposes **no
superseding row**; any superseding rows for S071/S082 belong to their own assigned seats
(append-only; old rows must never be edited). I did not re-verify S071/S082 myself.

## C10 predicate impact

None. `measure.py source_ok` requires S096–S109 only; S075 is outside that set. S075's only
used-by is the round-72 C15 candidate entry, which is not this round's claim surface and remains
`admission-status: candidate` outside this round's edit authority.

## Failure statement

No network or source failures. All remote fetches succeeded (raw pinned file HTTP 200; GitHub
commits API 200; raw main file HTTP 200). No tool installs or updates this seat (curl/python3/
grep pre-existing; nothing installed, no PATH directory touched, no pacman transaction attempted
— host-wide pacman pause respected).

## Observation / inference / unknown

- **Observation:** quote verbatim at the pinned commit (line 4, sha256 above); commit exists and
  is dated 2026-10-27T17:13:17Z; both anchor headings present (lines 1, 36); sentence still
  present on `main` (line 4) and in the local read-only checkout at HEAD 12f6e09 (line 4);
  registry/lesson/entry fields mutually consistent; single registry occurrence of S075.
- **Inference:** none needed; every checked field is directly evidenced by the cited bytes.
- **Unknown:** nothing material for this row. (Non-material: full diff content between the pin
  and `main`; only presence of the quoted sentence on main was checked, not line-level identity.)

Scratch `/fast/scratch/hyaku/revenger-r73/R73Source075/` (two downloaded `installation.md`
copies, pinned and main, plus `commit.json`) removed after receipts (sha256s, byte count, line
numbers, access dates) were copied into this report.
