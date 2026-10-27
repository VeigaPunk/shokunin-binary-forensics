# CoreS064Review — round-72 w1 · S064 (WerWolv/ImHex) + linked entry text

Seat: CoreS064Review · Date: 2026-10-27 · Lane: revenger-shokunin · Leaf member, read-only.
Axes: coverage, source accuracy.

## Assigned scope

Review only S064 and its linked entry text. Reopen the pinned WerWolv/ImHex README; verify the quote/anchor and documented scope. Check that the entry does not imply analysis of a target or a tool run.

Objects reviewed (lane tracked files, read-only):
- `corpus/SOURCES.md:78` — registry row S064 (verbatim, full row quoted below).
- `corpus/lessons/round-72.md` Gate table row S064 (line 23 of that file's table block).
- `corpus/knowledge/round-72-tool-landscape.md:25` — the entry row that cites `ImHex S064`.
External: the pinned GitHub README (public source page), reopened as data.

## Verdict: SUPPORT, with one minor locator revision

S064's quote, source identity, tier/status/used-by wiring, and the entry's ImHex claim all check out against the pinned README bytes. One defect found: the registry row's locator anchor is wrong (`"Features"`; the quoted tagline lives in the README introduction block, above `## Features`). This is a Q02-class locator-precision defect (M61 family) that does not change tier, status, used-by, or any C15 counting leg — hand to L1 for a registry-anchor correction; it does not falsify C1.

## Evidence

### 1. Pinned commit resolves; receipt

- `https://raw.githubusercontent.com/WerWolv/ImHex/fddad83966128b96dc1a8c9d55ba0ccd0721e276/README.md` → HTTP 200, 21,423 bytes, sha256 `8f4c89c636606543b6396cbca436a7586bd662ef52eb365a00bc8b2f88ad5e97` (computed twice, identical). GitHub raw only serves existing commit objects, so commit `fddad83966128b96dc1a8c9d55ba0ccd0721e276` exists in `WerWolv/ImHex`.
- Drift: current `master` README is byte-identical to the pinned revision (`diff` empty, same size/hash pipeline). No drift affects the quote as of 2026-10-27.

### 2. Quote and anchor

Lesson Gate row S064 (`corpus/lessons/round-72.md`): `README introduction: "A Hex Editor for Reverse Engineers, Programmers and people who value their retinas when working at 3 AM."`

- Verbatim in the pinned README at line 10, exactly 1 occurrence (`grep -cF` → 1). Word count 18 ≤ 25.
- Structure: line 10 sits inside a centered `<p align="center">` block immediately after the `ImHex` h1 title block (lines ~4–11), before the badge rows and before the `## Features` heading at line 62. **"README introduction" is the correct anchor.**
- Registry row (`corpus/SOURCES.md:78`) quotes the same tagline truncated to `"A Hex Editor for Reverse Engineers, Programmers"` — a verbatim prefix, acceptable — but anchors it as `README.md "Features"`. **That anchor is wrong**: the quoted string is not under `## Features`; it precedes the section. The Features section itself (pinned lines 62–144+) contains the feature claims the registry's scope line describes ("Featureful hex view", "Custom C++-like pattern language for parsing highlighting a file's content" at line 93, "Loading data from many different data sources" at line 144) — so the row's scope text and its quote are individually accurate, but the locator pairs the tagline with the wrong heading. Minor; fix is an anchor string change to the introduction block (or move the registry quote to a Features-section string).

### 3. Documented scope vs the entry's claim

Entry (`corpus/knowledge/round-72-tool-landscape.md:25`): "ImHex describes a hex editor with a custom pattern language and multiple data sources." Supported by the pinned README:
- hex editor: line 10 tagline; Features bullet "Featureful hex view".
- custom pattern language: line 93 "Custom C++-like pattern language for parsing highlighting a file's content"; lines 312–314 `## Pattern Language` / "The Pattern Language is the completely custom programming language developed for ImHex."
- multiple data sources: line 144 "Loading data from many different data sources" (Local Files, Raw Disks, …); line 206 "Compare data of different data sources".

The paraphrase is attributive ("describes") and matches only what the README itself states; no correctness, performance, or parity claim is made. The registry scope cell ("The project's own hex-editor, pattern-language and data-source feature descriptions; not format-validation evidence") and its caveat ("a displayed interpretation still needs independent ground truth") are consistent with the source.

### 4. No target-analysis or tool-run implication

- Entry row boundary: "A parser/pattern display is an observation to check against a separate specification and bytes; it is not an oracle by itself." No target named.
- Entry scope header: "Dynamic-process and traffic tools are named only to identify their documented scope; none was run." Observation/Inference/Unknown section: "no tool was installed or run" and "no conclusion is made about any actual game, binary, app, website or traffic target."
- Lesson decision cell: "ADMIT, tier A for the project's own purpose description; no parser correctness claim."
- Registry caveat: "The project advertises byte inspection and custom pattern parsing; a displayed interpretation still needs independent ground truth."
- Conclusion: the entry documents the project's own declared scope only; nothing in the S064-linked text implies a run against a target or any executed analysis.

### 5. C15 predicate leg (S064 slice)

Registry row S064 (`corpus/SOURCES.md:78`, verbatim): tier `A`, status `mined`, opened/rechecked `2026-10-27`, recheck policy `on-release`, `used-by` = `corpus/knowledge/round-72-tool-landscape.md`. The entry's selection table cites `ImHex S064` (entry line 25) and the entry-mapping line `corpus/SOURCES.md:123` covers S054–S070+S073 (includes S064). All counting-predicate legs that pass through S064 are present; only the anchor string is imprecise (§2).

## Findings by severity

1. **Minor — registry locator imprecision (REVISE item).** `corpus/SOURCES.md:78` anchors the tagline quote at `README.md "Features"`; the pinned bytes put it at line 10 in the introduction block, `## Features` starts at line 62. Same-source anchor conflict with the lesson Gate's "README introduction" (which is correct). Q02/M61-family; does not change admission tier, status, used-by, or the frozen C15 predicate outcome. Suggested fix (lane-side, not by this seat): registry anchor → `README.md introduction`.
2. **No other defect found in scope.** Quote verbatim and unique; scope paraphrase supported; no run/target implication; pinned revision exists and matches current master; 18-word quote within the ≤25-word Gate rule.

## Uncertainty and verification gaps

- GitHub's commit-metadata API (`/repos/WerWolv/ImHex/commits/<sha>`) returned HTTP 403 (unauthenticated rate limit), so the pinned commit's author/timestamp metadata was not read. Commit existence is established by the raw content URL serving at that exact SHA; the registry row for S064 makes no commit-date claim, so nothing in the row depends on the missing metadata.
- Mechanical quote audit receipt (`reports/round-72/source-quotes-check.log`) checks lesson-Gate quote parseability/word count, not source attribution — attribution re-derived here independently, per the lesson's own note.
- External README bytes are untrusted data; treated strictly as evidence text, no embedded instruction followed, nothing installed or executed from it.

## Bounds compliance

Read-only access to this lane's tracked files plus the assigned public source page; writes limited to this report at `.ufo/waves/round-72/w1/CoreS064Review.md`. No scratch dir (no mutation-test item), no git/jj mutations, no tool installs or updates, no subagent dispatch, no messages to other lanes. Commands ran from the fleet root `/home/vgpnk/Projects/shokunin` without creating files there.
