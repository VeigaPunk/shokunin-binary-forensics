# R73Source064 — round-73 v2 · S064 (WerWolv/ImHex) source re-audit

Seat: R73Source064 · Date: 2026-10-30 · Lane: revenger-shokunin · Leaf member, read-only.
Axes: coverage, source accuracy. Scope: assigned row S064 only. No new source admission proposed.

## Verdict: AGREE with source disposition (ADMIT, tier A) — one known minor anchor defect re-confirmed, no change to admission

S064's located quote is verbatim against the pinned README, scope/tier/status/used-by wiring is
consistent, no rejection flip applies, and current master is byte-identical to the pinned
revision. The round-72 flagged locator defect (`README.md "Features"` anchor) reproduces
against the pinned bytes; it does not change tier, status, used-by, or any counting leg.

## Located quote (exact, ≤25 words)

> A Hex Editor for Reverse Engineers, Programmers and people who value their retinas when working at 3 AM.

- Words: 18 (≤25). Occurrences in pinned README: exactly 1 (`grep -cF` → 1), at line 10.
- Registry row's stored quote is the verbatim prefix "A Hex Editor for Reverse Engineers,
  Programmers" of the same line — verbatim-prefix acceptable.
- Access date (this seat's independent reopen): 2026-10-30 (UTC).
- URL (primary, pinned): https://raw.githubusercontent.com/WerWolv/ImHex/fddad83966128b96dc1a8c9d55ba0ccd0721e276/README.md
  (registry URL https://github.com/WerWolv/ImHex, commit fddad83966128b96dc1a8c9d55ba0ccd0721e276).

## Evidence (independent reopen, 2026-10-30)

1. **Pinned commit resolves.** raw.githubusercontent at the pinned SHA → HTTP 200, 21,423
   bytes, sha256 `8f4c89c636606543b6396cbca436a7586bd662ef52eb365a00bc8b2f88ad5e97` — matches
   the round-72 CoreS064Review receipt byte-for-byte. GitHub raw serves only existing commit
   objects, so the pinned commit exists in WerWolv/ImHex. [observation]
2. **Quote verbatim and unique.** Line 10, inside `<p align="center">` intro block immediately
   after the h1 logo block; `grep -cF` full tagline → 1. Normalizing markup/indentation only,
   both the full tagline and the registry's truncated prefix match byte-exactly. [observation]
3. **Anchor defect re-confirmed (minor, known).** Registry row (`corpus/SOURCES.md:78`)
   anchors the quote at `README.md "Features"`; `## Features` starts at line 62 of the pinned
   README, and the quoted string sits at line 10 in the introduction block, before it. The
   lesson Gate row (`corpus/lessons/round-72.md:23`) anchors it "README introduction" — that is
   the correct anchor. Same-source locator conflict; Q02/M61-family. Suggested lane-side fix:
   registry anchor string → `README.md introduction`. Does not change quote, tier, status,
   used-by, or any C10/C15 counting leg. [observation]
4. **No drift.** Current `master` README fetched 2026-10-30 → byte-identical to the pinned
   revision (same size and sha256; `cmp` clean). The recheck policy `on-release` is satisfied
   as of this access. [observation]
5. **Scope supported.** Registry scope cell ("the project's own hex-editor, pattern-language
   and data-source feature descriptions") matches pinned lines: 65 "Featureful hex view";
   93 "Custom C++-like pattern language for parsing highlighting a file's content"; 144
   "Loading data from many different data sources"; 312 `## Pattern Language`. Entry
   (`corpus/knowledge/round-72-tool-landscape.md:25`) paraphrase "ImHex describes a hex editor
   with a custom pattern language and multiple data sources" is attributive and matches only
   what the README states. Caveat ("a displayed interpretation still needs independent ground
   truth") and entry boundary ("A parser/pattern display is an observation … not an oracle by
   itself") are consistent; nothing implies a tool run or target analysis. [observation]
6. **Disposition / flip check.** Lesson Gate: "ADMIT, tier A for the project's own purpose
   description; no parser correctness claim." Registry: tier A, status mined, rechecked
   2026-10-27, policy on-release, used-by `corpus/knowledge/round-72-tool-landscape.md`. No
   rejection and no flip condition applies to S064; round-72 spotcheck routed quote defects
   name only S071/S082. **I agree with ADMIT, tier A.** [observation]

## Network/source failures

None. Both pinned and master fetches returned HTTP 200 on 2026-10-30. (Round-72's GitHub
commit-metadata API 403 remains unretried; the row makes no commit-date claim, so nothing
depends on it.) [observation]

## Uncertainty

- GitHub commit author/date metadata for the pin was not read (unauthenticated API); commit
  existence is established by content serving at the SHA. [unknown, immaterial]
- External README bytes treated as untrusted data; no embedded instruction followed; nothing
  installed or executed. [observation]

## Bounds compliance

Read-only access to lane tracked files plus the assigned public source page; sole write is
this report. Scratch `/fast/scratch/hyaku/revenger-r73/R73Source064/` used for two fetched
README copies, receipts (HTTP codes, byte counts, sha256) copied inline above; scratch removed
before yield. No git/jj mutations, no installs (none needed; curl only), no pacman, no
subagent dispatch, no fleet-root writes.
