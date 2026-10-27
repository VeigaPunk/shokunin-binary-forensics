# CoreS057Review — round 72, w1 — S057 mrexodia/ida-pro-mcp

Seat: reviewer (leaf, no dispatch). Axes: coverage, source accuracy. Scope: S057 and its linked entry text only.

## Judgment: SUPPORT

No contradiction found. The S057 source row, the round-72 knowledge entry, and the round-72 lesson row are all consistent with the pinned README revision, quote is verbatim, the recommendation to the official Hex-Rays server is confirmed in the repository's own words, and nothing in the chain infers use, installation, or host readiness.

## Evidence

### 1. Pinned README reopened at the recorded revision

Fetched `https://raw.githubusercontent.com/mrexodia/ida-pro-mcp/c133c3853faa111a9b00ee615c013b720d0c4acd/README.md` (SHA-addressed, immutable — fetch succeeded, so commit c133c3853faa111a9b00ee615c013b720d0c4acd exists and this is its content).

README lines 1–5 (verbatim, untrusted external text quoted as data only):

```
# IDA Pro MCP

> [!IMPORTANT]
> **I recommend using the [Official Hex-Rays IDA MCP Server](https://github.com/HexRaysSA/ida-mcp) instead!**
>
> See the [announcement blog post](https://hex-rays.com/blog/hex-rays-ida-mcp-server) for more information.
```

- Rendered callout text: "I recommend using the Official Hex-Rays IDA MCP Server instead!" — exact character match with the row/lesson quote. 10 words, within the ≤25-word gate.
- The repository does itself recommend the official Hex-Rays server: it is the first content of the README, links `HexRaysSA/ida-mcp`, and points to the Hex-Rays announcement blog post. Confirmed, not inferred.
- Introduction (next line of body): "Simple [MCP Server](https://modelcontextprotocol.io/introduction) to allow vibe reversing in IDA Pro." — this is the repository's own IDA-facing MCP description the row's scope cites.
- Prerequisites section exists at this revision: Python 3.11+, IDA Pro 8.3+ (9 recommended), "IDA Free is not supported" — setup constraints only, consistent with the row's exclusion "not IDA capability on this host".
- The same revision still documents ida-pro-mcp's own installation, transports and tools at length, i.e. the repository simultaneously documents its own server and recommends the official alternative at top. The row's summary ("documents an IDA-facing MCP option but itself recommends the official Hex-Rays server") captures exactly this dual state.

### 2. Source row (corpus/SOURCES.md, line 71)

`| S057 | ida-pro-mcp — https://github.com/mrexodia/ida-pro-mcp | tool | A | The repository's own IDA Pro MCP description and its stated current alternative recommendation; not IDA capability on this host | README.md introduction and "Prerequisites", commit c133c3853faa111a9b00ee615c013b720d0c4acd, accessed 2026-10-27; "I recommend using the Official Hex-Rays IDA MCP Server instead!" | This repository documents an IDA-facing MCP option but itself recommends the official Hex-Rays server; the entry does not endorse installing or using either | mined | 2026-10-27 | on-release | corpus/knowledge/round-72-tool-landscape.md |`

- Commit SHA matches the pin I reopened. Quote matches verbatim. Status A, mined, used-by names the round-72 entry — satisfies the C15 linkage predicate for this row.

### 3. Knowledge entry (corpus/knowledge/round-72-tool-landscape.md, row "Need native disassembly/decompilation and analysis")

- Cites `IDA Pro MCP S057` in the repositories column.
- Statement: "The IDA-MCP README recommends the official Hex-Rays MCP server." — faithful paraphrase; the README's exact product name is "Official Hex-Rays IDA MCP Server" linking HexRaysSA/ida-mcp, same referent.
- Boundary column: "do not infer feature parity, licensing, correct decompilation, or local provider readiness from the list" — no use/readiness claim. No endorsement of installing or using either server anywhere in the entry.

### 4. Lesson Gate (corpus/lessons/round-72.md, line 16)

`| S057 | https://github.com/mrexodia/ida-pro-mcp | 2026-10-27 | README introduction: "I recommend using the Official Hex-Rays IDA MCP Server instead!" | ADMIT, tier A for this project's own recommendation and role; note the repository directs users to the official alternative. |`

- Located quote ≤25 words, present. Admission limited to the project's own recommendation/role; no capability, execution, or installation claim.

## Notes (non-blocking)

1. Locator imprecision, trivial: the quote sits in a `[!IMPORTANT]` callout at the very top of README.md, immediately above the introduction sentence; the README has no heading literally named "Introduction". "README introduction" resolves unambiguously to the README head, so the locator is a fair simplification, not a mismatch.
2. The entry's phrase "official Hex-Rays MCP server" drops the word "IDA" from the product name; referent unchanged (HexRaysSA/ida-mcp).

## Uncertainty / verification gaps

- I verified content at the SHA-pinned raw URL; I did not check whether c133c3853… is the repository's current HEAD. Not required: the row pins a specific revision, and the quote/recommendation hold at that pin, which is what C15 needs.
- "Accessed 2026-10-27" is the row's declared access date; my reopening is 2026-10-27 and matches. I cannot retro-verify the original access session itself.
- Per seat bounds I did not run the frozen counter or inspect other rows' internals; S057-side predicate facts (used-by link, entry citation, mined status, Gate quote) are all directly observed above.
