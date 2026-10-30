# R73Source072 — S072 source audit (Awesome Reverse Engineering)

Seat: R73Source072 · lane: revenger-shokunin · axes: coverage, source accuracy · date: 2026-10-30
Assignment: reopen SOURCES.md row S072, its round-72 lesson Gate row and linked entry wording; compare located quote verbatim (markup-normalized), scope, tier, used-by, rejection flip. Report only this row. Read-only; no edits to any registry/lesson/entry file.

## Located quote (return value)

- **Quote (13 words, ≤25):** "A curated starting point for understanding binaries, applications, firmware, file formats, and protocols."
- **URL:** https://github.com/morluto/awesome-reverse-engineering — README.md at pinned commit `8bfb44b3f6fdd796bf35fef23ddaf5f12213fc53` (raw: `https://raw.githubusercontent.com/morluto/awesome-reverse-engineering/8bfb44b3f6fdd796bf35fef23ddaf5f12213fc53/README.md`)
- **Access date:** re-opened 2026-10-30 (UTC ~15:53Z) by this seat; row records original access 2026-10-27.
- **Locator in source:** README.md line 7 of the pinned file — the standalone opening line after the title, featured-REA blockquote and social-preview image, immediately before the "Find a tool by the work you need to do." line and the `## Start here` table (line 11). This is the README opening, matching the row's anchor "README.md opening".

## Disposition: AGREE (support the rejection as recorded)

S072 is **REJECTED, tier C** (community catalog): a discovery lead, never sole support for a tool's behavior or quality. Independent re-open confirms every load-bearing element of the row. No quote defect attaches to S072; **no superseding row is proposed for S072**.

## Evidence — verbatim comparison (markup-normalized)

- **Observation.** Re-fetched the pinned raw README: HTTP 200, 395 lines, sha256 `2c4f8c8bf9202a0b9e1730d1f2639857a7293d96ced86611bfc31782982aae46`. `grep -c` over the exact quoted string returns exactly 1 hit (line 7). The row's located quote is character-for-character the source line; no markup normalization was required (plain text in both source and row; the lesson Gate row at `corpus/lessons/round-72.md` line 31 carries the identical string, so registry row and lesson agree with each other and with the source).
- **Observation.** The quoted sentence sits in the opening block and is a scope statement for the whole list, not evidence about any listed tool — consistent with what the rejection records.
- **Observation.** Commit-pin verified via GitHub commits API: `8bfb44b3f6fdd796bf35fef23ddaf5f12213fc53` exists, committer date 2026-10-25T10:22:34Z, message "Merge reviewed intakes and document expansion sources and constraints". The pin predates the row's recorded 2026-10-27 access by two days; pin/access chronology is coherent.

## Evidence — scope, tier, used-by, flip

- **Scope (observation).** Row scope: "Its own organization of broad tool/resource leads; never sole support for a tool's behavior or quality." The pinned README is organized as a task-to-section catalog: a `## Start here` table mapping ~16 investigation tasks (learn assembly, triage, deobfuscation, malware, Android/.NET, iOS/macOS, firmware, game RE, diffing, symbolic execution, AI-assisted…) to ~20 content sections (line 11 onward; `## Contents` at line 20). That is precisely "organization of broad tool/resource leads". No capability claim about any listed tool is made in the row, and none is needed.
- **Tier (observation + inference).** Tier C is appropriate: an Awesome-list catalog page (community curation), not a primary project artifact. Matches the sibling catalog rejection S071's tiering.
- **Used-by (observation).** Row `used-by` = `corpus/lessons/round-72.md`; the Gate row (line 31) is present with matching quote and reject reason. The entry `corpus/knowledge/round-72-tool-landscape.md` line 66 (Q12 PASS) mentions "catalog rejections S071/S072 are similarly recorded" — a provenance note about the rejection records themselves, not a capability citation of S072; consistent with rejected status. Registry history (`corpus/SOURCES.md` line 500) records S071–S072 as the 2 tier-C catalog rejection rows appended in the 2026-10-27 operator-directed pass. Nothing routes capability support through S072.
- **Rejection flip (observation).** Row flip: "a future claim specifically concerns the list's own curation policy and is re-checked against its documented selection process." Checkable: `CONTRIBUTING.md` at the same pin (HTTP 200, sha256 `a048a4c3fce3619159f0d159afd708b005a48f29266a707ebd24774695f73b11`) documents a concrete intake/selection process — canonical project links only, one-sentence task explanation, commercial licensing/host-tool/platform disclosure, experience or reproducible example in the PR, alphabetical format, "Star counts alone do not establish quality", relationship disclosure, and "Maintainer-owned projects follow the same criteria as other entries". The flip condition names a real, pinned, checkable process.
- **S071/S082 debt (observation, outside this row).** `round-72-verifier-spotcheck.md` routes quote defects only for S071 (registry paraphrase) and S082 (cross-attribution to S083). Both already carry append-only superseding rows S427/S428 in `corpus/lessons/round-73.md` Gate lines 13–14. S072 was re-opened in that spot-check's page sample but no defect was recorded against it; this seat's independent fetch/substring audit confirms the S072 quote verbatim, so no new superseding row is warranted.

## Network / source failures

- None for this row. Two HTTPS fetches (raw README, commits API) plus one CONTRIBUTING fetch: all HTTP 200, no rate-limit, no redirect off-github(-usercontent).
- Tools used: system `curl` only (pre-existing; version `curl 8.14.1` channel pacman/core, no install or update performed this seat). No packages installed; pacman pause honored.

## Uncertainty

- Unknown: whether the default branch HEAD has moved past the pin since 2026-10-27 (not queried; the row cites the immutable commit pin, which is what matters and was verified).
- Inference: tier C correctness follows from the catalog-page status and the lane's uniform treatment of the two Awesome-list rows (S071/S072 both tier C rejected).

## Constraint compliance

Read-only on production (only this report written, at the assigned path). No registry/lesson/entry edits; no new source admission; no git/jj actions; no builds/tests run; scratch at `/fast/scratch/hyaku/revenger-r73/R73Source072/` removed after this report was written. No seat is an outside discernment verifier; this is a lane-internal review record.
