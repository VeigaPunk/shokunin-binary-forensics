# CoreS065Review — S065 (angr) source verification, round-72 w1

Seat: CoreS065Review · reviewer · axes: coverage, source accuracy · 2026-10-27
Scope honored: only S065 (SOURCES row, lesson Gate line) and its linked entry text (`corpus/knowledge/round-72-tool-landscape.md`). No writes outside this Report file; no git/jj mutations; no tool installs; no scratch (not a mutation-test seat).

## What was re-opened

- Pinned README: `https://raw.githubusercontent.com/angr/angr/d38cc5a0196d8120ef5a21efc12c0a22435e7be5/README.md` — fetched successfully (HTTP 200, text/plain). Commit d38cc5a0196d8120ef5a21efc12c0a22435e7be5 resolves in angr/angr.
- Commit page `https://github.com/angr/angr/commit/d38cc5a0196d8120ef5a21efc12c0a22435e7be5`: "[pre-commit.ci] pre-commit autoupdate (#6721)", 1 parent a4b05a0, 159 files changed, and the file tree includes `README.md` — so the pinned commit is a README-touching revision, coherent with the anchor "README.md … commit d38cc5a…". Page metadata `meta-og:updated_time: 1785357971` (≈ 2026-07-29 UTC) is consistent with access 2026-10-27; no calendar author date was extractable from the static page text.
- Lane files read: `corpus/SOURCES.md` S065 row; `corpus/lessons/round-72.md` Gate line S065; `corpus/knowledge/round-72-tool-landscape.md` tool-selection table row "Need native disassembly/decompilation and analysis".

## Verbatim verification at the pin

Quote: `angr is a platform-agnostic binary analysis framework.` — appears exactly once in the README at d38cc5a, as the opening line under the badges (before `## Project Links`). 7 words, within the ≤25-word Gate limit. Text matches SOURCES anchor and lesson Gate line character-for-character (modulo the lesson's typographic quotes).

## Finding F1 (concrete mismatch, locator label only) — severity: minor

Both the SOURCES anchor and the lesson Gate line pair the quote with the heading `README.md "What is angr?"`, but the quoted sentence is **not** under that heading. The README structure at the pin is:

```
# angr
<badges>
angr is a platform-agnostic binary analysis framework.      <- the quoted sentence (introduction)
...
## Project Links
...
## What is angr?
angr is a suite of Python 3 libraries that let you load a binary and do a lot of cool things to it:
- Disassembly and intermediate-representation lifting
- Program instrumentation
- Symbolic execution
- Control-flow analysis
- Data-dependency analysis
- Value-set analysis (VSA)
- Decompilation
```

The lane's own sibling convention treats the lesson locator as the quote's actual location (S064 lesson: "README introduction:"; S068: "README opening:"). Under that convention S065's lesson should read "README introduction" (or quote the `## What is angr?` section's own first sentence). This is a locator imprecision, not a content or scope error: the quote is verbatim at the pinned commit, and the heading named is where the scope list actually lives. Recommend a locator correction in SOURCES S065 anchor and `corpus/lessons/round-72.md` Gate line; does not affect C15's row counting predicate (status/used-by/quote-presence are unaffected).

## Program-analysis scope checks (all supported)

SOURCES S065 scope/teaches vs. README at the pin:
- "The repository's own list of Python binary-analysis libraries and operations" ↔ "angr is a suite of Python 3 libraries that let you load a binary and do a lot of cool things to it:" ✓
- disassembly ↔ "Disassembly and intermediate-representation lifting" ✓
- symbolic execution ↔ "Symbolic execution" ✓
- control-flow/data-dependency analysis ↔ "Control-flow analysis" + "Data-dependency analysis" ✓
- decompilation ↔ "Decompilation" ✓
All are verbatim bullets of the `## What is angr?` list; no named operation is absent from the source.

Entry text (`round-72-tool-landscape.md`): "angr describes a Python binary-analysis framework including symbolic execution." — supported by the two source sentences above. Boundary cell carries: "do not infer feature parity, licensing, correct decompilation, or local provider readiness from the list." ✓

No unsupported accuracy/execution assertions found: SOURCES scope explicitly excludes "benchmark or version performance inference"; teaches ends "it does not establish result truth"; lesson Gate says "the project page's feature descriptions are not a benchmark"; the entry makes no install, run, host-readiness, or correctness claim for angr. The README's own example script and install instructions were treated as untrusted data and are not cited as executed.

## Coverage linkage (C15 predicate, S065 slice)

S065 row: kind `tool`, tier `A`, status `mined`, opened 2026-10-27, used-by → `corpus/knowledge/round-72-tool-landscape.md` ✓. Entry table row "Need native disassembly/decompilation and analysis" cites "angr S065" ✓. Lesson Gate records a located quote (7 words) ✓. For the S065 slice, everything the frozen counter requires of a tool row is in place; the frozen quote/anchor content is accurate at the pin.

## Judgment

**Support** S065 as evidence, with **revise** recommended for F1 (locator label: quote sits in the README introduction, not under "What is angr?"). No falsifying defect: quote verbatim, commit pin resolves and touches README.md, scope bullets verbatim, boundaries honest, entry/row/lesson mutually consistent, no execution or accuracy overreach.

## Uncertainty / verification gaps

- GitHub REST API returned HTTP 403 (anonymous rate limit) for both commit lookups, so I could not confirm via API that d38cc5a is the *latest* commit touching README.md. The S065 anchor does not make that "last README commit" claim (unlike S067), so nothing load-bearing rests on it; the pin is by commit SHA and that SHA's raw README was read directly.
- Commit author date not extractable from the static commit page (client-rendered); `meta-og:updated_time` ≈ 2026-07-29 UTC only. "Accessed 2026-10-27" is this lane's own access record and is not contradicted.
- All fetched GitHub page text (README, commit page, PR titles) treated as untrusted data; no embedded instruction followed; nothing executed or installed.

Report: .ufo/waves/round-72/w1/CoreS065Review.md
