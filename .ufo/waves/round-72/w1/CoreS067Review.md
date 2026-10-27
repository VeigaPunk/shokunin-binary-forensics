# CoreS067Review — dnSpy (archived original)

**Axes:** coverage; source accuracy.

**Judgment: SUPPORT.** The S067 source row and its linked entry text accurately describe the original dnSpy repository as historical, document its README scope, and do not represent it as currently maintained or supported. No actionable S067-specific correction found.

## Direct source evidence

- Original repository: <https://github.com/dnSpy/dnSpy> (opened 2026-10-27). The page displays the exact banner: “This repository was archived by the owner on Dec 21, 2020. It is now read-only.” It also labels the project “Public archive.” This supports the row's archive status/date and read-only wording; it is current GitHub page metadata, not evidence of support.
- Pinned README: <https://raw.githubusercontent.com/dnSpy/dnSpy/45716aff73eb4a3047def20fa6006d156a7e25bb/README.md>. Its opening says: “dnSpy is a debugger and .NET assembly editor” and lists “Debug .NET and Unity assemblies” and “Edit .NET and Unity assemblies.” This supports the bounded historical .NET/Unity debugger/editor characterization. The README additionally lists debugger, assembly-editor, and hex-editor functions; those are project-documented capabilities, not independently tested results.
- README history: <https://github.com/dnSpy/dnSpy/commits/master/README.md> lists commit `45716aff73eb4a3047def20fa6006d156a7e25bb` as the latest README-affecting entry, dated Nov 11, 2020. The commit page at <https://github.com/dnSpy/dnSpy/commit/45716aff73eb4a3047def20fa6006d156a7e25bb> resolves to the same commit and repeats the archive banner.

## Lane text checked

- `corpus/SOURCES.md`, S067: labels it “dnSpy (archived original),” specifies the README at the pinned commit and the archive banner, says “no current support claim,” and teaches not to present it as a current maintained option.
- `corpus/knowledge/round-72-tool-landscape.md`, “Need managed assembly inspection”: calls the original README a .NET/Unity debugger/editor, identifies the GitHub banner as archived/read-only, and explicitly says the archive notice is not a claim of support.
- `corpus/lessons/round-72.md`, S067: quotes the archive banner and says “explicitly not a current supported tool.”

These statements are consistent with the original repository's direct evidence. The linked entry does not infer installation, execution, current provider availability, or current maintenance. A corpus-wide literal search found these S067-related uses and the distinct dnSpyEx row; no contrary maintained/support claim for original dnSpy appeared in the inspected corpus results.

## Uncertainty / gaps

The GitHub REST API endpoint returned HTTP 403; the archive/date and README evidence were nevertheless directly visible on the GitHub HTML page and raw pinned README. No behavioral verification was performed or implied.
