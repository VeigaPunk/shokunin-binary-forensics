# R73Source083 — round 73, v2 — S083 AutoDecompiler (arXiv 2606.16162v2) reopen audit

**Seat:** R73Source083 (leaf reviewer; lane-internal; no dispatch). **Date:** 2026-10-30.
**Axes:** coverage; source accuracy. **Assigned row only:** S083. Read-only; no new source
admission; no superseding row proposed (S083 is not one of the routed S071/S082 defect rows;
see routing status below).

## Verdict: AGREE with source disposition (ADMIT / mined, tier A)

No contradiction found on independent reopening. The located quote is verbatim under
markup-only normalization, the v2 revision date matches, scope/tier/used-by all hold, and no
rejection flip is triggered. Round-72 spotcheck agreement
(`corpus/lessons/round-72-verifier-spotcheck.md:73`) is confirmed by my own fetch.

## Located quote (≤25 words), access date, URL

- Quote: **"feedback-driven multi-turn binary decompilation"** — 5 words.
- Row's declared access date: 2026-10-27 (original mining). My reopen access date: **2026-10-30**.
- URL: `https://arxiv.org/abs/2606.16162v2` — fetched HTTP 200, 44,662 bytes,
  sha256 `9fb9682e27a53cf8eef9239b5859540966279dc48c371d3624f43462b7fd4d3e` (receipt below).

## Evidence (my own reopening)

### 1. Fetch receipt (observation)

- `GET https://arxiv.org/abs/2606.16162v2` → HTTP 200, final URL identical (no redirect),
  44,662 bytes, sha256 `9fb9682e27a53cf8eef9239b5859540966279dc48c371d3624f43462b7fd4d3e`,
  fetched 2026-10-30. Page is the arXiv abs page for v2 specifically.

### 2. Verbatim comparison, normalizing markup only (observation)

- `<title>`: `[2606.16162v2] Binary Decompilation LLM with Feedback-Driven Multi-Turn Refinement`;
  `citation_title` meta identical. Matches the row title; the abstract names the model
  "AutoDecompiler", matching the row's parenthetical.
- Submission history block: `[v1] Mon, 15 Jun 2026 03:25:05 UTC (1,297 KB)`;
  `[v2] Sat, 3 Oct 2026 15:12:18 UTC (1,663 KB)`. Matches the row's "last revised 2026-10-03".
- The quoted string occurs verbatim 3 times (og:description meta, citation_abstract meta,
  rendered abstract block). Containing sentence (abstract, tag-stripped):
  "This paper presents AutoDecompiler, a decompilation-specialized LLM trained with
  reinforcement learning for feedback-driven multi-turn binary decompilation."
- The phrase is plain text with no embedded markup, so normalization is tag-stripping only;
  the located quote is a true verbatim substring, not a paraphrase (contrast the routed
  S071 paraphrase defect).

### 3. Scope check (observation + inference)

- Row scope: "The arXiv v2 abstract's proposed compile/execute/I-O feedback training method
  and reported evaluation, not independent replication."
- Abstract (tag-stripped, normalized whitespace): presents "an iterative refinement process,
  where the model revises generated code based on compilation, execution, and input/output
  testing feedback"; "decompilation-specific rewards that capture code validity,
  recompilability, execution consistency, and semantic fidelity"; "stage-aware diagnostic
  feedback from compiler errors, execution failures, and failed test cases"; and "We train
  the AutoDecompiler family and evaluate it…". This is exactly a compile/execute/I-O feedback
  training method plus a reported evaluation: **matches**. The abstract's results are the
  paper's own benchmarks; the row explicitly excludes independent replication: **matches**.

### 4. Tier check (inference)

Tier A (source's own words) is correct: every row claim is bounded to the paper's own v2
abstract. No capability, replication, or tool-readiness claim is made anywhere in the chain.

### 5. Used-by / entry wording check (observation)

- Row used-by cell: `corpus/knowledge/round-72-tool-landscape.md` — file exists; line 43 cites
  "LLM4Decompile S082; AutoDecompiler S083; ALT4Decompile S084" as "distinct
  learned-decompilation techniques" reporting "their own benchmark results."
- Entry boundary column: "Do not compare across their different tasks, datasets and metrics
  from abstracts alone, or translate a paper result into tool readiness." — bounded use,
  consistent with the row's disposition note ("results remain scoped to its paper and
  benchmarks, not a guarantee for a candidate reconstruction"). No overclaim in the entry.
- Lesson Gate row (`corpus/lessons/round-72.md:42`): ADMIT, tier A "for the named paper
  method only; empirical results remain benchmark-scoped." — consistent with evidence.

### 6. Rejection flip check (observation + inference)

No flip condition applies: status is `mined` (admitted), quote is verbatim and correctly
attributed to this paper, scope is bounded, and the row was never rejected. The row's
7th-cell boundary note and the lesson Gate row agree.

### 7. Duplicate-authority check (observation)

Exactly one `| S083 |` registry row in `corpus/SOURCES.md` (line 97). The second S083 string
match in the file is S428's prose cross-reference ("the behavioral-deviation quote belongs to
AutoDecompiler S083"), not a duplicate row id. Measure.py's duplicate-id predicate is not
implicated by this row.

## Routed-defect corroboration (S071/S082 — other seats' rows)

- The sentence S082's row misattributes — "the generated code may appear readable or even
  compile successfully, yet still deviate from the behavior of the original binary" — is
  verbatim in this v2 abstract (sentence immediately preceding the AutoDecompiler
  introduction). My reopen independently confirms the round-72-verifier-spotcheck finding
  (`corpus/lessons/round-72-verifier-spotcheck.md:72`) that the quote belongs to S083.
- Routing status: S082 is already superseded by S428 (`corpus/SOURCES.md:443`, mined
  2026-10-30, this round); S071 is superseded by S427 (per the round-73 source-attribution
  erratum, `corpus/knowledge/round-72-tool-landscape.md` "Round-73 source-attribution
  erratum"). Both were handled append-only. S083 itself is correctly dispositioned, so no
  new superseding row is warranted from this seat; per the append-only rule I edited no row.

## Row field-by-field comparison (SOURCES.md line 97)

| Field | Row value | Reopened evidence | Match |
|---|---|---|---|
| source | Binary Decompilation LLM with Feedback-Driven Multi-Turn Refinement (AutoDecompiler) — arxiv.org/abs/2606.16162v2 | title and abstract confirmed at URL | yes |
| type | paper | arXiv paper abs page | yes |
| tier | A | bounded to paper's own abstract | yes |
| scope | v2 abstract's proposed compile/execute/I-O feedback training method and reported evaluation; not independent replication | abstract describes iterative refinement on compilation/execution/I-O feedback + own evaluation | yes |
| located quote | "feedback-driven multi-turn binary decompilation", last revised 2026-10-03 | verbatim ×3; [v2] dated 2026-10-03 | yes |
| disposition note | iterative refinement method; results scoped to its paper/benchmarks | matches abstract and entry boundary | yes |
| status | mined | registry metadata; consistent with Gate ADMIT | n/a |
| accessed | 2026-10-27 | original session not retro-verifiable; my 2026-10-30 reopen re-verifies content at the cited URL | consistent |
| pin class | on-release | v2 served today at the citation URL | yes |
| used-by | corpus/knowledge/round-72-tool-landscape.md | exists; cites S083 with bounded wording | yes |

## Network / source failures

None. The single HTTPS fetch succeeded on first attempt (HTTP 200). No target execution
performed, none implied by the row.

## Uncertainty / verification gaps

- The 2026-10-27 mining session cannot be retro-verified; only content at the cited URL as
  served today is verifiable, and it matches (observation-limited claim).
- I verified the abs page (abstract); I did not download the PDF — the row cites the
  abstract only, so the abstract is the correct surface.
- Whether a v3 exists is outside the row (row pins v2, and v2 remains the served revision at
  the citation URL today).
- Historical lesson files mention an older-generation S083 id (round-67/69 registries); the
  current registry's single S083 row is the round-72 one audited here. Noted, no action.

## Tooling

- No installs or updates this seat; system `curl` and `python3` (existing) used for fetch and
  markup-normalized extraction. Pacman pause honored; no host changes; no PATH writes.

## Conclusion

**Agree** with the S083 disposition: ADMIT, tier A, mined, used-by
`corpus/knowledge/round-72-tool-landscape.md`. Located quote (5 words, ≤25): "feedback-driven
multi-turn binary decompilation" — verbatim at `https://arxiv.org/abs/2606.16162v2`
([v2] 2026-10-03), reopened 2026-10-30, no network failures, no superseding row warranted
for S083.
