# R73Source070 — S070 source audit (round-73 v2 wave, lane revenger-shokunin)

Seat: `R73Source070` · role: source-audit reviewer (round-72 source set) · leaf member, no dispatch.
Lane root: `/home/vgpnk/Projects/shokunin/revenger-shokunin`. Claim context: frozen C10
(`reports/round-73/claims.md`, counter `reports/round-73/measure.py`). S070 is **not** in the
C10 required source set (`source_ok` checks S096–S109 only); this seat is one of the 42
round-72 source audits and has no effect on the frozen predicate either way.

## Assigned row under review

Locator: `corpus/SOURCES.md:84` (registry row S070), Gate wording `corpus/lessons/round-72.md:29`,
used-by entry `corpus/knowledge/round-72-tool-landscape.md:28`.

Row content (verbatim from the registry, 11 columns): source `RAD Debugger —
https://github.com/EpicGames/raddebugger`; kind `tool`; tier `A`; scope "The project's README-stated
local x64 Windows/Linux user-mode scope and alpha limitation; no remote/multi-machine claim";
anchor "README.md "The RAD Debugger Project", commit 62b715a30e5da6b8d7e02372a8e7458feab1df97,
accessed 2026-10-27; "It currently only supports local-machine x64 debugging on both Windows and
Linux""; decision cell: "The README explicitly bounds its current target/architecture surface and
calls Linux support early; no broader debugger capability is inferred"; status `mined`; opened
2026-10-27; recheck `on-release`; used-by `corpus/knowledge/round-72-tool-landscape.md`.

## Primary re-open (my own fetch)

- URL: `https://raw.githubusercontent.com/EpicGames/raddebugger/62b715a30e5da6b8d7e02372a8e7458feab1df97/README.md`
- Access date: **2026-10-30**. HTTP 200, 22146 bytes, sha256 `0909f149ea72e0fd49dd2438944c81674e2b77c75bfc636c4501b467a1c2d29c`.
- Located quote found verbatim at **README lines 10–11** (joining a hard line break, whitespace
  normalized only):

  > The RAD Debugger is a native, user-mode, multi-process, graphical debugger. It
  > currently only supports local-machine x64 debugging on both Windows and Linux
  > (although Linux support is still very early). We plan to expand support to
  > other architectures, and to implement remote and multi-machine debugging.

- Supporting sentences verified as exact byte substrings of the fetched file: "The debugger is
  currently in *ALPHA*." (line 15 — supports the scope cell's "alpha limitation");
  "(although Linux support is still very early)." (line 12 — supports "calls Linux support early");
  "to implement remote and multi-machine debugging." (lines 12–13 — remote/multi-machine is a
  stated future plan, so the scope cell's "no remote/multi-machine claim" is accurate for current
  capability).
- Commit metadata: GitHub API reports commit `62b715a…` committed 2026-10-17T02:04:28Z, message
  "update codebase readme w.r.t. linux" — consistent with the row's "accessed 2026-10-27" (the row
  records access, not authorship; both hold).

## Located quote returned (≤25 words)

> "It currently only supports local-machine x64 debugging on both Windows and Linux"

12 words. Access date 2026-10-30. URL
`https://github.com/EpicGames/raddebugger` (README at commit
`62b715a30e5da6b8d7e02372a8e7458feab1df97`, raw file sha256 above). Normalization: one hard line
break inside the quote (between "It" and "currently") collapsed to a single space; no markup
normalization needed — the span is plain text and matches byte-for-byte otherwise.

## Verbatim comparison and field checks

| Check | Result | Evidence |
|---|---|---|
| Quote verbatim in cited source at cited pin | **PASS** | Exact substring of whitespace-normalized pinned README (lines 10–11); boundary at sentence start/end. |
| Quote word count ≤25 | **PASS** | 12 words. |
| Scope column supported | **PASS** | "local-machine x64 debugging on both Windows and Linux" (lines 11), "user-mode" (line 10), "The debugger is currently in *ALPHA*." (line 15), remote/multi-machine only as future plan (lines 12–13). Every scope element is README-stated. |
| Teaches/decision cell supported | **PASS** | "calls Linux support early" ↔ "(although Linux support is still very early)." (line 12); "no broader debugger capability is inferred" ↔ "We plan to expand support to other architectures, and to implement remote and multi-machine debugging." (lines 12–13) marks broader capability as not-yet-present. |
| Tier A appropriate | **AGREE** | Primary project repository's own README at a pinned commit; tier A for declared scope only is the registry convention. |
| used-by | **CONSISTENT** | `round-72-tool-landscape.md:28` table row "RAD Debugger S070": "RAD Debugger describes local-machine x64 debugging on Windows and Linux, with Linux support described as early." — agrees with the README; no other used-by claims for S070 found. |
| Rejection flip | **N/A — none claimed, none needed** | Row status is `mined` (admit-as-scope), not rejected; no flip condition is asserted anywhere for S070. |
| Lesson Gate vs registry wording | **CONSISTENT, complementary** | Gate quote `round-72.md:29` "The RAD Debugger is a native, user-mode, multi-process, graphical debugger." is verbatim at line 10 (10 words); the registry quote is the separate scope-limiting sentence. Both verbatim; note "multi-process" (present) vs "multi-machine" (planned only) are distinct and both rows word them correctly. |
| Round-72 spotcheck precedent | **CONSISTENT** | `round-72-verifier-spotcheck.md` sampled S054–S093 but not S070; this re-open fills that gap with the same method (own fetch, verbatim substring check). |

## Disposition

**AGREE** with the source disposition: ADMIT-as-scope (status `mined`), tier A, scope limited to
the README-stated local x64 Windows/Linux user-mode surface with its alpha and early-Linux
limitations; no remote/multi-machine capability claimed or inferred. The located quote is verbatim
at the cited pin, the scope and teaches cells are each backed by exact source sentences, and the
used-by entry matches. **No defect found for S070; no superseding row proposed for this row.**

## S071/S082 routed quote defects (context, not my admission)

Observation: `round-72-verifier-spotcheck.md` routes two defects — S071's registry quote is a
paraphrase ("Each repo is read and security-graded" vs the pinned README's "each one read and
security-graded") and S082's quote is misattributed (the "readable/compilable but deviates"
sentence belongs to AutoDecompiler S083, not LLM4Decompile). Append-only superseding rows already
exist in the registry: **S427** (`corpus/SOURCES.md:442`, supersedes S071, verbatim "each one read
and security-graded", rejected tier C retained) and **S428** (`corpus/SOURCES.md:443`, supersedes
S082 with the LLM4Decompile abstract's own motivation sentence), recorded in
`corpus/lessons/round-73.md:96-98`. Old rows were not edited. Per the claim freeze ("New source
admission is a separate Q review") and my seat bound ("report only your assigned row"), this seat
proposes **no additional row** and admits nothing; S427/S428 verification belongs to their own
assigned seats.

## C10 predicate impact

None. `measure.py source_ok` requires S096–S109 only; S070 is outside that set. S070's only
used-by is the round-72 C15 candidate entry (`round-72-tool-landscape.md`), which is not this
round's claim surface and remains `admission-status: candidate`.

## Failure statement

No network or source failures. Both remote fetches succeeded (raw README HTTP 200;
GitHub commits API 200). No tool installs or updates this seat (curl/python3 pre-existing on host;
nothing installed, nothing in `~/.local/bin` or any PATH directory touched; pacman pause
observed — no pacman transaction attempted).

## Observation / inference / unknown

- **Observation:** quote verbatim at pinned commit (README lines 10–11, sha256 above); commit
  62b715a dated 2026-10-17T02:04:28Z "update codebase readme w.r.t. linux"; ALPHA line at :15;
  early-Linux and future-plans sentences at :12–13; registry (`SOURCES.md:84`), Gate
  (`round-72.md:29`) and entry (`round-72-tool-landscape.md:28`) fields mutually consistent;
  S427/S428 superseding rows already present for the routed S071/S082 defects.
- **Inference:** none needed for the verdict; every checked field is directly evidenced by the
  cited bytes.
- **Unknown:** nothing material for this row. (Non-material: whether the README changed at any
  commit after the pinned 62b715a; the row pins the commit, so later drift is out of scope.)

Scratch `/fast/scratch/hyaku/revenger-r73/R73Source070/` (one downloaded README) removed after
receipts (sha256, byte count, line numbers, access dates) were copied into this report.
