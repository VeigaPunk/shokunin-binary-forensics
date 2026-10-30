# R73Source087 — S087 source audit (round-73 v2 wave, lane revenger-shokunin)

Seat: `R73Source087` · role: source-audit reviewer (round-72 source set) · leaf member, no dispatch.
Lane root: `/home/vgpnk/Projects/shokunin/revenger-shokunin`. Claim context: frozen C10
(`reports/round-73/claims.md`, counter `reports/round-73/measure.py`, pin
`reports/round-73/candidate-pin.json`). S087 is **not** in the C10 required source set
(`source_ok` checks S096–S109 only); this seat is one of the 42 round-72 source audits and has
no effect on the frozen predicate either way.

## Assigned row under review

Locator: `corpus/SOURCES.md:101` (registry row S087), Gate wording
`corpus/lessons/round-72.md:46`, used-by entry `corpus/knowledge/round-72-tool-landscape.md:46`.

Row content (verbatim from the registry, 11 columns): source `REA Gems —
https://github.com/sqwu/rea-gems`; kind `community`; tier `C`; scope "This unofficial gallery's
own description of its collected case links; individual case claims require their original
sources"; anchor `README.md "Disclaimer", commit 71c1e0952286b6f278456936127c5456731e21a1,
accessed 2026-10-27; "All case links point to their original authors."`; teaches "A discovery
lead only; this lane checked the official case destinations it actually cites and does not trust
gallery labels as evidence"; status `mined`; opened 2026-10-27; recheck `90d`; used-by
`corpus/knowledge/round-72-tool-landscape.md`.

## Primary re-open (my own fetch)

- URL: `https://raw.githubusercontent.com/sqwu/rea-gems/71c1e0952286b6f278456936127c5456731e21a1/README.md`
- Access date: **2026-10-30**. HTTP 200, 19213 bytes, sha256
  `7b0fb68189f9e1de29ff5604bd8c61b19c4e41f9cf6838106ade7da3b67e1c0b`.
- Located quote found at **line 30**, verbatim, inside the `<details>` block whose summary is
  `<strong>Disclaimer</strong>` (summary at line 27). Full Disclaimer body (lines 29–34):

  > This repository is an unofficial community project and is not affiliated with
  > the REA team. All case links point to their original authors. Reverse
  > engineering may be restricted by local law, software licenses or terms of
  > service — always respect them. Content is indexed for research and educational
  > purposes.

- Commit metadata: GitHub commits API reports `71c1e095…` committed 2026-10-27T08:59:21Z,
  message "chore: daily case refresh (2026-10-27)" — consistent with the row's "accessed
  2026-10-27" (the row records access, not authorship; both hold).

## Located quote returned (≤25 words)

> "All case links point to their original authors."

**8 words.** Access date 2026-10-30. URL `https://github.com/sqwu/rea-gems` (README.md
"Disclaimer" section at commit `71c1e0952286b6f278456936127c5456731e21a1`, raw file sha256
above). No markup normalization was needed: the quoted sentence sits on a single line as plain
text and matches byte-for-byte.

## Verbatim comparison and field checks

| Check | Result | Evidence |
|---|---|---|
| Quote verbatim in cited source at cited pin | **PASS** | Exact substring, line 30 of fetched pinned README, inside the `<details><summary>Disclaimer</summary>` block; sentence boundary clean. |
| Quote word count ≤25 | **PASS** | 8 words (`wc -w` on the quoted span). |
| Scope column supported | **PASS** | Disclaimer lines 29–30: "This repository is an unofficial community project and is not affiliated with the REA team. All case links point to their original authors." — the row's "unofficial gallery" and "individual case claims require their original sources" are both verbatim-backed. |
| Tier C appropriate | **AGREE** | Self-described "unofficial community project" collecting third-party case links; a discovery lead, not primary evidence. Tier C matches the registry convention for catalogs/galleries. |
| used-by | **CONSISTENT** | `round-72-tool-landscape.md:46` table row "REA Gems S087; Awesome Reverse-Engineered S088": "Use only to find candidate originals; each claim must be reopened at the primary tool, spec, paper or publisher source. Neither catalog backs a tool capability claim." — exactly the tier-C lead-only scope; no other used-by claims. |
| Rejection flip | **N/A — none claimed, none needed** | Row is `mined`/admitted as tier C; the Gate decision "ADMIT as a tier-C discovery lead only; each case claim must be reopened at its original author" matches the registry scope and teaches cells. Unlike S071/S072/S074/S091/S093, no flip clause was recorded, and none is required: the disposition is a scope bound, not a rejection awaiting a condition. |
| Lesson Gate vs registry wording | **CONSISTENT** | Both carry the identical quoted string and locator (README "Disclaimer"); the registry adds the commit pin and access date, both re-verified here. |
| Round-72 spotcheck precedent | **CONSISTENT** | `round-72-verifier-spotcheck.md` Step-1 census records a disclosed W01 warning for S087 (tier-C mined); that warning is status-neutral and already disclosed — it is not a quote or disposition defect. |

## Disposition

**AGREE** with the source disposition: ADMIT (status `mined`), tier C, scoped to the gallery's
own description of its collected case links; a discovery lead only, with each case claim to be
reopened at its original author. The quote is verbatim at the cited commit, the scope bound is
verbatim-backed by the same Disclaimer block, the teaches cell ("does not trust gallery labels
as evidence") matches the entry's use, and the used-by entry applies it exactly within that
bound. **No defect found for S087; no superseding row proposed for S087.**

## S071/S082 routed quote defects (context, not my admission)

Observation: `round-72-verifier-spotcheck.md` routes two defects — S071's registry quote is a
paraphrase and S082's located quote is misattributed (that sentence belongs to AutoDecompiler,
S083). Append-only superseding rows already exist in the registry: **S427**
(`corpus/SOURCES.md:442`, supersedes S071, verbatim "each one read and security-graded", tier C
rejected retained) and **S428** (`corpus/SOURCES.md:443`, supersedes S082 with the LLM4Decompile
abstract's own motivation sentence, tier A mined), with primary re-opens recorded in
`corpus/lessons/round-73.md:13-14`. Old rows were not edited. Per the claim freeze ("New source
admission is a separate Q review") and my seat bound ("report only your assigned row"), this
seat proposes **no additional row** and admits nothing; S427/S428 verification belongs to their
own assigned seats.

## C10 predicate impact

None. `measure.py source_ok` requires S096–S109 only; S087 is outside that set. S087's only
used-by is the round-72 C15 candidate entry, which is not this round's claim surface and remains
`admission-status: candidate`.

## Failure statement

No network or source failures. Both remote fetches succeeded (raw README HTTP 200; GitHub
commits API HTTP 200, pin resolved and dated 2026-10-27). No tool installs or updates this seat
(curl/python3 pre-existing; nothing installed, no PATH directory touched, consistent with the
host-wide pacman pause — no pacman transaction attempted or needed).

## Observation / inference / unknown

- **Observation:** quote verbatim at pinned commit 71c1e095 (line 30, sha256 above); commit
  dated 2026-10-27T08:59:21Z; Disclaimer block also contains the "unofficial community project"
  sentence backing the scope cell; registry, lesson Gate and entry row are mutually consistent;
  S427/S428 superseding rows present at `corpus/SOURCES.md:442-443`.
- **Inference:** none needed; every checked field is directly evidenced by the cited bytes.
- **Unknown:** nothing material for this row. (Non-material: README content drift after the
  pinned commit was not checked, and the live gallery page `sqwu.github.io/rea-gems` was not
  fetched — the row is pinned to the README commit, which is what the locator cites.)

Scratch `/fast/scratch/hyaku/revenger-r73/R73Source087/` (one downloaded README, one commit
metadata JSON, one headers file) removed after receipts (sha256, byte count, line number, access
dates, commit metadata) were copied into this report.
