# R73Source061 — S061 source audit (ILSpy)

Seat: R73Source061 · lane: revenger-shokunin · axes: coverage, source accuracy · date: 2026-10-30
Assignment: reopen SOURCES.md row S061, its round-72 lesson Gate row and linked entry wording; compare located quote verbatim, scope, tier, used-by, rejection flip. Report only this row. Read-only; no edits to any registry/lesson/entry file.

## Located quote (return value)

- **Quote (10 words, ≤25):** "ILSpy is the open-source, cross-platform .NET assembly browser and decompiler."
- **URL:** https://github.com/icsharpcode/ILSpy — pinned README at commit `91f0373e48b41945ca1aec6355c7be59567635c1` (raw: `https://raw.githubusercontent.com/icsharpcode/ILSpy/91f0373e48b41945ca1aec6355c7be59567635c1/README.md`)
- **Access date:** re-opened 2026-10-30 (UTC 15:48Z) by this seat; row records original access 2026-10-27.
- **Locator in source:** README line 3 (immediately under the `# ILSpy` title); README line 7 carries the cited second section `Decompiler Frontends`.

## Disposition: AGREE (support the admission as recorded)

S061 is **ADMIT, tier A** for declared UI/decompiler scope only. Independent re-open confirms every load-bearing element. No superseding row is proposed for S061; no quote defect attaches to this row.

## Evidence — verbatim comparison (markup-normalized)

- **Observation.** Re-fetched the pinned raw README: HTTP 200, 7929 bytes, sha256 `b686abd0b649f47197e7e2c88e9a36028468aed90a212ca2cf96620ac1519b03` — identical to the hash recorded in the round-72 seat review `.ufo/waves/round-72/w1/CoreS061Review.md`. Pin is immutable-content stable.
- **Observation.** README line 3 reads: `ILSpy is the open-source, cross-platform .NET assembly browser and decompiler. The desktop UI runs on Windows, Linux, and macOS (built on Avalonia).` The row's located quote is an exact contiguous prefix substring, character-for-character after stripping the trailing sentence; no markup normalization was even required (plain text, no markdown inside the quoted span). Matches the lesson Gate row (`corpus/lessons/round-72.md`, S061 line) verbatim as well.
- **Observation.** Cited sections exist: `# ILSpy` (line 1) and `Decompiler Frontends` (line 7). The frontends list (lines 10–18) names Visual Studio 2022/2026 built-in decompilation, the VS marketplace extension, the VS Code extension, `ILSpyCmd` (dotnet tool for Linux/Mac/Windows), C#-for-VS Code decompilation, the `ICSharpCode.Decompiler`/`ILSpyX` NuGet packages, and Linux/Mac/Windows PowerShell cmdlets — supporting the row scope's "and listed frontends".

## Evidence — scope, tier, used-by, flip

- **Scope (observation).** Row scope: "The repository's cross-platform .NET assembly browser/decompiler and listed frontends; not quality or host support testing." README line 3 states the desktop UI runs on Windows, Linux, and macOS, so "cross-platform" is supported for the stated desktop UI; the row does not claim every frontend runs on every platform. The disclaimer ("not quality or host support testing") is honored — no install or run is asserted anywhere in the row, lesson, or entry. The row boundary ("an output remains decompiled evidence rather than original source") matches the lesson Gate ("output is not source identity").
- **Tier (observation + inference).** Tier A is appropriate: primary first-party repository README at an exact pinned commit. Not a catalog, not secondary.
- **Used-by (observation).** Row `used-by` = `corpus/knowledge/round-72-tool-landscape.md`; entry line 27 ("Need managed assembly inspection" row) names "ILSpy S061" and characterizes it as "describes a cross-platform .NET assembly browser/decompiler" — consistent with the README and the row. Citation relationship holds.
- **Rejection flip (observation).** Not applicable — S061 was admitted, not rejected; the lesson Gate records no flip condition for it. The round-72 spot-check's routed quote defects attach only to S071 (paraphrase) and S082 (misattribution); the round-73 lesson erratum supersedes those with append-only rows S427/S428 (`corpus/lessons/round-73.md` Gate lines 13–14). S061 is outside that defect set; I verified its quote independently rather than inheriting the round-72 count.

## Network / source failures

- None for this row. Single HTTPS fetch, HTTP 200, no rate-limit, no redirect off-githubusercontent.
- Historical (not re-encountered by this seat): the round-72 review notes the GitHub commit-API metadata lookup was rate-limited then; commit identity is instead evidenced here by the immutable raw-URL content hash matching the round-72 receipt.

## Uncertainty

- Unknown: commit `91f0373e…` authorship/date metadata (not queried this seat; content-pin equivalence is established by hash, which is what the row cites).
- Inference: tier A correctness follows from first-party pinned-README status, matching the lane's SOURCES rules as applied to sibling rows.

## Constraint compliance

Read-only on production (only this report written). No registry/lesson/entry edits; no new source admission (none warranted for S061); no tool installs; no git/jj actions; scratch at `/fast/scratch/hyaku/revenger-r73/R73Source061/` removed after this report was written. No seat is an outside discernment verifier; this is a lane-internal review record.
