# R73Source067 — S067 reopen audit (dnSpy archived original)

**Seat:** R73Source067 (leaf reviewer, lane-internal). **Date:** 2026-10-30.
**Axes:** coverage; source accuracy. **Assigned row only:** S067. No superseding row proposed (S067 is not one of the routed S071/S082 defect rows; those belong to their own seats).

## Located quote (verbatim, markup-normalized)

> "This repository was archived by the owner on Dec 21, 2020. It is now read-only."

- Words: 15 (≤25). **URL:** https://github.com/dnSpy/dnSpy — **Access date: 2026-10-30** (fresh fetch, HTTP 200).
- The sentence occurs verbatim in the fetched page HTML; no markup normalization needed beyond tag stripping.

## Independent reopen evidence

- Repo page `https://github.com/dnSpy/dnSpy` (HTTP 200, fetched 2026-10-30): archive banner string above present exactly once; page labels the project a public archive. **[OBSERVATION]**
- Pinned README `https://raw.githubusercontent.com/dnSpy/dnSpy/45716aff73eb4a3047def20fa6006d156a7e25bb/README.md` (HTTP 200): opening "dnSpy is a debugger and .NET assembly editor."; features "Debug .NET and Unity assemblies", "Edit .NET and Unity assemblies". Matches the row's "historical .NET/Unity debugger and assembly editor" characterization. **[OBSERVATION]**
- Pin currency: GitHub API `commits?path=README.md` (HTTP 200 this session) lists `45716aff73eb` (2020-11-11, "Rename files, classes, remove Core from .NET Core") as the newest commit touching README.md — the row's "last README commit" claim holds. (Round-72 review recorded a 403 on the API then; the API answered 200 today.) **[OBSERVATION]**

## Comparison against row, lesson, entry

- `corpus/SOURCES.md:81` (S067): quote, pinned commit, archived 2020-12-21 date, "no current support claim", tier A, scope `tool`, disposition mined, on-release 2026-10-27, used-by `corpus/knowledge/round-72-tool-landscape.md` — all confirmed against my reopen. **[OBSERVATION]**
- `corpus/lessons/round-72.md:26` (S067): quotes the same banner; ADMIT tier A "for historical README features plus the platform's observed archive notice; explicitly not a current supported tool" — consistent with evidence. **[OBSERVATION]**
- `corpus/knowledge/round-72-tool-landscape.md:27` ("Need managed assembly inspection"): uses S067 only as a historical descriptor; states the archive notice "is current GitHub repository metadata, not a claim of support"; explicitly declines C03 assembly-analysis knowledge from these docs. No current-maintenance inference. **[OBSERVATION]**
- Disposition check: S067 was **ADMITTED**, not rejected; no flip condition applies. Scope (historical tool documentation), tier A (project's own README + platform metadata), and used-by link are all accurate as recorded. Round-72 spotcheck (`corpus/lessons/round-72-verifier-spotcheck.md`) routes defects for S071/S082 only; S067 is not flagged. **[OBSERVATION]**

## Verdict

**AGREE** with the source disposition: ADMIT, tier A, bounded to historical README features plus the observed archive notice; correctly barred from any current-support or maintenance claim. No correction, erratum, or superseding row warranted for S067.

## Failures / uncertainty

- None network-side: all three fetches (repo HTML, pinned README, commits API) succeeded. No target execution performed, none implied by the row.

## Tooling

- No installs/updates this seat; `curl` (system, existing) used for fetches. Pacman pause honored; no host changes.
