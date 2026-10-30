# R73Source080 — S080 source audit (round-73 v2 wave, lane revenger-shokunin)

Seat: `R73Source080` · role: source-audit scout · leaf member, no dispatch, no vote file assigned.
Lane root: `/home/vgpnk/Projects/shokunin/revenger-shokunin`. Claim context: frozen C10
(`reports/round-73/claims.md`, counter `reports/round-73/measure.py`, pin
`reports/round-73/candidate-pin.json`). S080 is **not** in the C10 required source set
(`source_ok` checks S096–S109 only); this seat is one of the round-72 source audits and has no
effect on the frozen predicate either way. Read-only seat: no corpus, shared-source, sibling or
fleet writes; only this report and my own scratch.

## Assigned row under review

Locators: registry row `corpus/SOURCES.md:94` (S080); Gate wording `corpus/lessons/round-72.md:39`;
used-by entry `corpus/knowledge/round-72-tool-landscape.md:41` (entry header lines 1–10 carry the
S-source list; `:41` is the table row that uses S080).

Registry row S080, 11 cells, verbatim:

| cell | value |
|---|---|
| id | `S080` |
| source | Decomperson: How Humans Decompile and What We Can Learn From It — `https://www.usenix.org/conference/usenixsecurity22/presentation/burk` |
| kind / tier | `paper` / `A` |
| scope | "The published 2022 study's stated research question and sampled data, not all reverse engineers or all workflows" |
| anchor | "USENIX Security 22 abstract, proceedings pages 2765–2782, 2022; \"Over 150 people participated, and we collected more than 35,000 code submissions.\"" |
| teaches | "A study of a particular competition dataset provides human-process research evidence but not a universal benchmark for RE tool performance" |
| status / opened / recheck | `mined` / 2026-10-27 / `on-release` |
| used-by | `corpus/knowledge/round-72-tool-landscape.md` |

Lesson Gate row (`corpus/lessons/round-72.md:39`), verbatim:
"S080 | https://www.usenix.org/conference/usenixsecurity22/presentation/burk | 2026-10-27 | Abstract: "Over 150 people participated, and we collected more than 35,000 code submissions." | ADMIT, tier A for the published study's reported sample only; not all analysts."

Entry wording (`corpus/knowledge/round-72-tool-landscape.md:41`), verbatim:
"| Decomperson S080 | The USENIX paper describes its participant dataset and defines a measurable form of exact decompilation for that study. | Study evidence is bounded to its cohort/task, not every analyst or tool. |"
(The entry is `admission-status: candidate`, coverage-map C15 — not this round's claim surface.)

## Primary re-open (my own fetch, 2026-10-30)

| artifact | URL | bytes | sha256 |
|---|---|---|---|
| presentation page (abstract) | `https://www.usenix.org/conference/usenixsecurity22/presentation/burk` | 39 719 | `f52b83545c8ff7329620513eafe704b8951918caf3aa913715f7c632bad8a295` |
| proceedings PDF (open access) | `https://www.usenix.org/system/files/sec22-burk.pdf` | 2 690 165 | `c1921fb62c31230b042fc71a71050bc165bca926f66459d55bbf8c7ddba071c9` (19 pages) |

Page-range claim "proceedings pages 2765–2782, 2022" — **confirmed three ways**: HTML metadata
`meta-citation_firstpage: "2765"`, `meta-citation_lastpage: "2782"`, `meta-citation_publication_date:
"2022"`, `meta-citation_isbn: 978-1-939133-31-1`; BibTeX block `pages = {2765--2782}`; and PDF text
footers "USENIX Association 31st USENIX Security Symposium" with `2765` on the first article page
(pdftotext line 123) and `2782` on the last (line 2322).

Sample/population context located in the paper (PDF §4 "DECOMPETITION" and §8): the data comes from
"an online competition called DECOMPETITION, which we designed and ran in November 2020", "A total
of 425 users and 238 teams registered … but only a fraction of those played. A total of 188 users
and 139 teams made source code submissions; 159 users and 114 teams submitted source code that
could be compiled." and §8: "the majority of participants were either students or hobbyists, and
only a few worked in a position where they were paid as reverse engineers."

## Located quote returned (≤25 words)

> "Over 150 people participated, and we collected more than 35,000 code submissions, the largest manual reverse engineering dataset to date."

20 words. Access date **2026-10-30**. URL
`https://www.usenix.org/conference/usenixsecurity22/presentation/burk` (same string verbatim in the
PDF abstract, `https://www.usenix.org/system/files/sec22-burk.pdf`, page 2 "Abstract"). No markup
normalization was needed; the span is plain text in both artifacts.

Minimal form matching the registry cell (12 words), also verbatim:
> "Over 150 people participated, and we collected more than 35,000 code submissions"

## Verbatim comparison and field checks

| check | result | evidence |
|---|---|---|
| Quote verbatim in cited source | **PASS with one punctuation-level deviation** | My own substring test (scratch `quote_check.py`, HTML-stripped and raw text, whitespace/markup/quote-normalized): registry quote *with* terminal "." → **MISS**; same 12 words *without* the period → **FOUND**; the 20-word full abstract sentence → **FOUND** (page and PDF). The source reads "…code submissions**,** the largest manual reverse engineering dataset to date." — the registry (and the Gate row) close the clause with "." where the source has a comma-continuation. Every word is verbatim; only the sentence-final punctuation differs. This is **not** a paraphrase and **not** a misattribution. |
| Quote word count ≤25 | **PASS** | 12 words as registered; 20 words in the full-sentence form. |
| Scope column supported | **PASS** | The abstract states the study's framing ("Existing studies of human reversers and the processes they follow are limited in size …"), its metric ("we reframe the problem of reverse engineering binaries as the problem of *perfect decompilation* … This gives us a quantitative measure of understanding"), and its sample ("Over 150 people participated, and we collected more than 35,000 code submissions"). The bound "not all reverse engineers or all workflows" is backed by the competition-cohort population above (§4/§8) and by §1 "Over 150 people participated—twice as many as the next-largest study". |
| tier A appropriate | **AGREE** | Peer-reviewed conference paper in the USENIX Security 22 proceedings, open-access PDF, ISBN 978-1-939133-31-1, pages 2765–2782 — tier A for the paper's own stated scope, per the registry's convention. |
| `teaches` cell supported | **PASS** | "A study of a particular competition dataset provides human-process research evidence but not a universal benchmark for RE tool performance" — the paper's own §1–§2 claim is a human-process metric study ("the largest manual reverse engineering dataset to date"; "perfect decompilation"), and it reports no RE-tool benchmark. Consistent. |
| used-by | **CONSISTENT** | `corpus/knowledge/round-72-tool-landscape.md:41` is the only knowledge entry citing S080; a corpus-wide grep for `S080` returns only `corpus/SOURCES.md:94`, `corpus/lessons/round-72.md:39`, `corpus/lessons/round-72-verifier-spotcheck.md:73`, that entry's table row, and round-72/73 wave-spec files. |
| Rejection flip | **N/A — none claimed, none needed** | S080 is `mined` with no REJECTED marker; the Gate decision is "ADMIT, tier A for the published study's reported sample only; not all analysts." Admit rows carry no flip condition in this registry, so there is no flip text to verify. |
| Lesson Gate vs registry wording | **CONSISTENT, same defect in both** | Both carry the identical 12-word string, so the Gate row inherits the same trailing-period deviation; the Gate adds only the "Abstract:" locator label, which matches the quote's position in the page abstract. |
| Round-72 spotcheck precedent | **CONSISTENT, independently reproduced** | `corpus/lessons/round-72-verifier-spotcheck.md:73` recorded "agree" for S080 (quote found verbatim) on the same URL. My re-open reproduces the substantive finding and adds the punctuation detail the earlier check did not test for. |

### Round-73 fetch/substring audit run by this seat

I ran the lane's own audit script (the check `claims.md` lists as a round-73 supporting duty) over
the rows around mine, writing only into my scratch:

```
python3 -B reports/round-73/verify_quotes.py --ids S071-S083 --out <scratch>/s071-s083.json
  rows=13 {'FAIL': 4, 'OK': 9}
  FAIL S071 quote-not-found      FAIL S077 HTTPError: HTTP Error 404: Not Found
  FAIL S080 quote-not-found      FAIL S082 quote-not-found
python3 -B reports/round-73/verify_quotes.py --ids S427-S428 --out <scratch>/s427-s428.json
  rows=2 {'OK': 2}
```

The script's `norm()` collapses whitespace/markup/quotes but **does not normalize punctuation**, so
S080's trailing-period deviation is reported as FAIL even though every word is verbatim. S077's
404 belongs to seat `R73Source077` and is out of my scope (recorded here only as an observation).

## Disposition

**AGREE** with the source disposition: ADMIT (status `mined`), tier A, scope limited to the
published 2022 study's stated research question and reported sample; not all analysts, not all
workflows, not a tool benchmark. The quote is verbatim in the cited source (modulo one terminal
punctuation mark), the scope and `teaches` cells are backed by the paper's own abstract and
sections 1, 2 and 4, and the used-by entry's boundary sentence ("bounded to its cohort/task, not
every analyst or tool") matches the paper's population description.

**Minor recorded defect (not a source-accuracy failure):** the located quote in `SOURCES.md:94`
and in `corpus/lessons/round-72.md:39` terminates a comma-continuation clause with "." instead of
",". Attribution is intact; the strict substring audit flags it anyway. Two remediation options for
the integrator, neither requiring an edit of the old row:

- **Option A (recommended, no new row):** leave S080 as is; the strict-audit FAIL for S080 is a
  punctuation artifact, and a superseding row for a soundly-attributed row adds registry noise.
- **Option B (append-only, only if the S054–S095 audit must be green):** append the row below. It
  uses a scope string distinct from S080's (so the census scope key differs → at most a W04
  duplicate-URL warning, which does not fail validation, cf. `scripts/sources-census.sh:645-646`)
  and its `teaches` cell contains "supersedes S080" (which suppresses E04 outright; the E04
  condition is at `scripts/sources-census.sh:647-650`, its `teaches !~ /supersedes S[0-9]{3}/`
  test at line 649). Old rows are never edited.

  `| S429 | Decomperson: How Humans Decompile and What We Can Learn From It — https://www.usenix.org/conference/usenixsecurity22/presentation/burk | paper | A | The 2022 study's reported competition-cohort sample and its perfect-decompilation metric, as stated in the abstract | USENIX Security 22 abstract, proceedings pages 2765–2782, 2022; "Over 150 people participated, and we collected more than 35,000 code submissions, the largest manual reverse engineering dataset to date." | supersedes S080 — the study's reported sample and its own perfect-decompilation metric; not a population estimate for analysts generally and not a tool benchmark | mined | 2026-10-30 | on-release | corpus/knowledge/round-72-tool-landscape.md |`

  (id is a placeholder: the integrator must allocate the next free id; S429 is free only if no
  other seat claims it. I wrote nothing to `corpus/`.)

## S071 / S082 routed quote defects — superseding-row proposal

Source of the routing: `corpus/lessons/round-72-verifier-spotcheck.md` (discernment table rows for
S071 and S082, plus routed defects 1 and 2). My own re-opens, with the same substring method:

| defect | cited source I re-opened | registry quote as written | verbatim? | what the source actually says |
|---|---|---|---|---|
| S071 paraphrase | `https://raw.githubusercontent.com/zhuyansen/awesome-ai-reverse-engineering/63900b2c9e2ae2dac61fc0db7553d4ce88ebb932/README.md` (pinned commit, as the row's anchor states) | "Each repo is read and security-graded" | **MISS** | "118 repos, each one read and security-graded by [Agent Skills Hub (agentskillshub.top)]" → the substring "each one read and security-graded" is **FOUND** |
| S082 misattribution | `https://arxiv.org/abs/2403.05286v3` (LLM4Decompile v3 abstract) | "The resulting code may appear readable or even compile successfully, yet still deviate from the behavior of the original binary." | **MISS** | the v3 abstract motivates the model with "traditional tools like Ghidra often produce results that are difficult to read and execute." (**FOUND**) and contains no "may appear readable" sentence |

**New observation the round-72 check did not record:** the round-72 spotcheck says the S082 quote
is "verbatim in the abstract of S083". Re-opening `https://arxiv.org/abs/2606.16162v2` **and**
`https://arxiv.org/abs/2606.16162v1` shows the AutoDecompiler abstract actually reads "the
**generated** code may appear readable or even compile successfully, yet still deviate from the
behavior of the original binary and mislead downstream analysis" — the registry quote says
"**The resulting** code …". The S082 string is therefore not byte-exact in either paper: it is a
misattribution **and** a one-word paraphrase of S083's sentence. S083's own registry quote
("feedback-driven multi-turn binary decompilation") is **FOUND** verbatim in v2, so S083's row needs
no correction; the defect lives only in S082's row.

**Append-only superseding rows already present in the registry**: `S427` (`corpus/SOURCES.md:442`,
supersedes S071, quote "each one read and security-graded", status `rejected`, tier C) and `S428`
(`corpus/SOURCES.md:443`, supersedes S082, quote
"traditional tools like Ghidra often produce results that are difficult to read and execute.",
status `mined`, tier A). I re-opened both quotes myself — **both FOUND verbatim** — and the lane's
own audit returns OK for both (`--ids S427-S428` → `rows=2 {'OK': 2}`). The round-73 lesson Gate
records both re-opens at `corpus/lessons/round-73.md:13-14`. Old rows S071 and S082 were not edited.
Timing note: when this seat audited them they were uncommitted working-tree bytes (`git status` then
showed `corpus/SOURCES.md` modified, `corpus/lessons/round-73.md` untracked); another actor
committed them during this seat's run at lane HEAD `d4ab332` ("round-73: honest stop (attempt 2) …").
This seat made no git/jj mutation. The S080 row itself is unchanged at HEAD (same 11 cells as
audited).

**My proposal (for the integrator; nothing written).** If the integrator wants the superseding rows
to carry this seat's re-open receipts rather than the in-tree S427/S428, the same two corrections
can be appended with fresh ids; the text below is independently re-opened by me and is
census-safe (unique id → no E03; distinct scope strings and `supersedes S0xx` in `teaches` → no
E04; at most a W04 duplicate-URL warning, which does not fail validation):

```
| S429 | Awesome AI Reverse Engineering — https://github.com/zhuyansen/awesome-ai-reverse-engineering | community | C | Catalog screening description at the pinned commit, not tool-function evidence | README introduction at commit 63900b2c9e2ae2dac61fc0db7553d4ce88ebb932, accessed 2026-10-30; "each one read and security-graded" | supersedes S071 — REJECTED as primary tool-function evidence: a catalog's own screening blurb establishes no tool capability; flip: evaluate the catalog's selection method against primary data. | rejected | 2026-10-30 | 90d | corpus/lessons/round-73.md |
| S430 | LLM4Decompile — https://arxiv.org/abs/2403.05286v3 | paper | A | The v3 abstract's stated motivation for the model (readability/executability of traditional tools), not behavioral-equivalence evidence | v3 abstract opening sentence, accessed 2026-10-30; "traditional tools like Ghidra often produce results that are difficult to read and execute." | supersedes S082 — the abstract motivates the authors' model by traditional tools' readability/executability limits; the "may appear readable or even compile successfully, yet still deviate" sentence belongs to AutoDecompiler (S083), whose wording reads "the generated code", not this paper's. | mined | 2026-10-30 | on-release | corpus/lessons/round-73.md |
```

**Recommendation:** append **one** row per defect, not both. If S427/S428 are committed as they
stand, my S429/S430 text is redundant and should be dropped (keeping the tree free of duplicate
correction rows); if the in-tree rows are dropped, append mine. My proposed S429 (S080 punctuation
fix) would then need the next free id as well. I admit nothing and edited no row: per the claim
freeze, "New source admission is a separate Q review", and per my seat bound, no other source
admission and no edit to any existing row.

## C10 predicate impact

**None.** `measure.py` computes `source_ok` from S096–S109 only (each `mined`, each naming the
candidate entry, each cited in it, with unique registry ids). S080 and the routed rows S071/S082/
S427/S428/S429/S430 are outside that set; no C10 row, README coverage row, candidate byte, vote
file or counter input is touched by this seat. The S080 used-by entry
(`corpus/knowledge/round-72-tool-landscape.md`) is `admission-status: candidate` on coverage-map
C15, which this round explicitly does not claim ("C15 stays uncovered").

## Failure statement

No network or source failures. All remote reads succeeded: USENIX presentation page (HTTP 200),
USENIX proceedings PDF (HTTP 200), arXiv 2403.05286v3, arXiv 2606.16162v2, arXiv 2606.16162v1, and
the pinned raw README on GitHub. The only non-200 encountered was in the *lane's own* audit
script's handling of S077's `tree` URL (HTTP 404 on its README candidates) — that row is not mine.

Tools used, all pre-existing, **no installs and no pacman transaction** (host-wide pacman pause
respected; nothing written to `~/.local/bin` or any PATH directory): `curl` 8.23.0, `pdftotext`
(poppler), `python3` 3.14.8, `sha256sum`, `git` (read-only `status`/`log`/`show`/`diff` only — no
mutation, no commit, no push), `pdfinfo`.

## Observation / inference / unknown

- **Observation:** fetched bytes/digests above; substring verdicts FOUND/MISS per quote variant;
  PDF page footers 2765 and 2782; HTML metadata and BibTeX page range; registry/Gate/entry cells
  quoted verbatim; audit verdicts `rows=13 {'FAIL': 4, 'OK': 9}` (S071, S077, S080, S082) and
  `rows=2 {'OK': 2}` (S427, S428); pinned README and both AutoDecompiler revisions read in full
  abstract.
- **Inference:** the source attribution of S080 is sound and its disposition (admit, tier A,
  sample-bounded) is supported by the paper's own text; the trailing-period deviation is a
  citation-style artifact rather than a paraphrase or a misattribution, and the strict
  quote-substring audit of this round will flag it unless Option B is taken.
- **Unknown:** whether the trailing-period style is a deliberate citation convention of this lane
  or a one-off slip — not decidable from the lane, so I do not classify it as a source-accuracy
  defect, only as a strict-audit artifact. Also unknown: whether
  prior-wave artifacts exist for S080 elsewhere (the round-72 wave directory contains 16 review
  files; I did not read them and credit nothing from them). Unreachable is not false: the only
  unreachable item in this seat's scope was S077's tree-URL README, which is not my row.

Scratch `/fast/scratch/hyaku/revenger-r73/R73Source080/` (one downloaded PDF, its text, the HTML
page, my quote-check script and the two audit JSON outputs) is removed after the receipts above
were copied into this report; no clone was made and nothing outside it was written.
