# CoreS068Review — S068 dnSpyEx scoped review (round 72, w1)

Axes: coverage, source accuracy. Scope honored: S068 and its linked entry text only.

## Judgment: REVISE (narrow — quote text only)

Scope, freshness bounds, locator, tier, and maintenance posture all hold against the reopened primary source. One defect: the recorded quote is not verbatim at the cited revision.

## Evidence

1. Lane records (read-only):
   - `corpus/SOURCES.md:82` (S068): scope "The fork's own README feature scope and self-description; not evidence of current maintenance cadence or target compatibility"; locator `README.md "dnSpyEx", commit de5a83051161e0becc70f32834c2596db6239fbd, accessed 2026-10-27`; quote recorded as "dnSpyEx is an unofficial continuation of the well known .NET debugger and assembly editor, dnSpy"; caveat "no claim of active maintenance is made because the README revision is from 2023"; `mined`, used-by `corpus/knowledge/round-72-tool-landscape.md`.
   - `corpus/knowledge/round-72-tool-landscape.md:27` ("Need managed assembly inspection"): "dnSpyEx calls itself an unofficial continuation and describes similar .NET/Unity functions."; boundary: "dnSpyEx's own README was last revised in 2023 in the opened history; active maintenance is not asserted."
   - `corpus/lessons/round-72.md:27` (Gate): quote "dnSpyEx is an unofficial continuation of the well known .NET debugger and assembly editor, dnSpy." ADMIT tier A; "the latest README revision shown was 2023, so active maintenance is not asserted."
2. Primary source reopened at the pinned revision (`https://raw.githubusercontent.com/dnSpyEx/dnSpy/de5a83051161e0becc70f32834c2596db6239fbd/README.md`, accessed 2026-10-27):
   - Verbatim opening: "dnSpyEx is an unofficial continuation of the [dnSpy](https://github.com/dnSpy/dnSpy) project which is a debugger and .NET assembly editor."
   - Feature scope: "Debug .NET and Unity assemblies", "Edit .NET and Unity assemblies"; Debugger / Assembly Editor / Hex Editor sections; "edit and debug assemblies even if you don't have any source code available".
   - The string "well known" appears nowhere in the pinned README.
3. Commit page `https://github.com/dnSpyEx/dnSpy/commit/de5a83051161e0becc70f32834c2596db6239fbd`: "Typo fix in README.md (#257)", 1 file changed (+1-1, README.md only), changing "a unofficial" → "an unofficial"; parent b93fe21; `meta-og:updated_time` 1699216494 (= 2023-11-05 UTC).
4. README freshness (`https://github.com/dnSpyEx/dnSpy/commits/master/README.md.atom`, accessed 2026-10-27): the most recent README.md commit on master is exactly the pin de5a830 at **2023-11-05T20:34:54Z**; previous README commits 2023-08-20 (e9a57f0), 2023-06-22 (81e9c2e), 2022-03-26 (3d8a34d). Master README (`raw .../master/README.md`) carries the identical opening wording — no post-2023 README change.
5. Repository page `https://github.com/dnSpyEx/dnSpy` (accessed 2026-10-27): About line — "Unofficial revival of the well known .NET debugger and assembly editor, dnSpy". Public fork of dnSpy/dnSpy; no archived/read-only banner; 11.4k stars.

## Findings

- **F1 — source accuracy — quote not verbatim at the pin (the revise trigger).** The recorded quote in `SOURCES.md:82` and `lessons/round-72.md:27` splices the README's "unofficial continuation" with the repository About line's "the well known .NET debugger and assembly editor, dnSpy" — a wording that exists in neither artifact as one sentence, and the About line itself says "revival", not "continuation". Semantic content is preserved (unofficial continuation of dnSpy; debugger and .NET assembly editor), and the locator (README.md heading "dnSpyEx", commit SHA, access date) is otherwise accurate, so this is a revise, not falsify. Concrete fix: replace the quote in both files with the verbatim pinned sentence — "dnSpyEx is an unofficial continuation of the dnSpy project which is a debugger and .NET assembly editor." (17 words; satisfies the claim's ≤25-word located-quote rule). If the About line is ever cited, it must be quoted separately as repository metadata with its own verb ("revival").
- **F2 — coverage — entry scope supported.** The entry's characterization ("calls itself an unofficial continuation and describes similar .NET/Unity functions") and the row's placement under "Need managed assembly inspection" are supported by the pinned README's self-description and its Debug/Edit .NET and Unity assemblies feature list. No installation, execution, correctness, or parity claim is made anywhere in the S068-linked text; the entry's blanket no-install/no-run disclaimer covers this row.
- **F3 — freshness — no assertion exceeds evidence.** All three records disclaim maintenance cadence and anchor the 2023 README revision. Independently confirmed: de5a830 is the latest README.md revision (2023-11-05T20:34:54Z), so "README revision is from 2023" / "last revised in 2023 in the opened history" / "latest README revision shown was 2023" are each accurate. The records also correctly do not treat the non-archived status or star count as maintenance evidence.
- **F4 — minor observation.** The fork is public and not archived (unlike S067's original), which the records neither claim nor rely on; consistent. No action.

## Uncertainty / gaps

- `api.github.com/repos/dnSpyEx/dnSpy/commits/de5a830...` returned HTTP 403 (unauthenticated rate limit); the commit date rests on the Atom feed and the page's `og:updated_time` (1699216494 = 2023-11-05), which agree.
- External pages are point-in-time (accessed 2026-10-27); a README revision after access would require recheck per the entry's own `recheck` line.
- Per seat bounds I did not run the frozen counter or touch any tracked file; predicate-level judgment stays with L1. Nothing here indicates the S068 row would fail its `TREE` predicates: row is `mined`, names the entry in used-by, and the corrected quote satisfies the Gate rule.
