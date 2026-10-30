# R73Source057 — round 73, v2 — S057 mrexodia/ida-pro-mcp re-admission audit

Seat: reviewer (leaf, no dispatch). Axes: coverage, source accuracy. Scope: SOURCES.md row S057, its round-72 lesson, and its round-72 entry wording only. Read-only; no new source admission; no superseding row proposed (S071/S082 defects are other seats' assignments).

## Verdict: AGREE with source disposition (ADMIT, tier A, mined)

No contradiction found on independent reopening. The located quote is verbatim under markup-only normalization, the pinned commit exists and is the revision that introduced the recommendation banner, scope/tier/used-by all match, and no rejection flip is triggered.

## Located quote (≤25 words), access date, URL

- Quote: **"I recommend using the Official Hex-Rays IDA MCP Server instead!"** — 10 words.
- Row's declared access date: 2026-10-27 (original mining). My reopen access date: **2026-10-30**.
- URL: `https://github.com/mrexodia/ida-pro-mcp` — README.md at pinned commit `c133c3853faa111a9b00ee615c013b720d0c4acd`.

## Evidence (my own reopening)

### 1. Fetch receipts (observation)

- `GET https://raw.githubusercontent.com/mrexodia/ida-pro-mcp/c133c3853faa111a9b00ee615c013b720d0c4acd/README.md` → HTTP 200, 20064 bytes, sha256 `52ba58c0203be594781db71b595585c15e0352f331d4aef2563602e0b151bf26`. Scratch copy since cleaned per seat rules; hash recorded here.
- `GET https://api.github.com/repos/mrexodia/ida-pro-mcp/commits/c133c3853faa111a9b00ee615c013b720d0c4acd` → 200; committer date 2026-09-26T15:42:10Z; message "Add banner to recommend using ida-mcp instead". The pinned revision is exactly the commit that added the recommendation banner, so the quote's presence is stable at and after this pin.

### 2. Verbatim comparison, normalizing markup only (observation)

README line 3 raw:

```
> **I recommend using the [Official Hex-Rays IDA MCP Server](https://github.com/HexRaysSA/ida-mcp) instead!**
```

- Raw literal substring `I recommend using the Official Hex-Rays IDA MCP Server instead!` is **absent** from the raw markdown (the product name is a link).
- Under markup-only normalization (markdown link → link text, `**` dropped), the quote is **present exactly once**, as the `[!IMPORTANT]` callout directly under the `# IDA Pro MCP` title: `> I recommend using the Official Hex-Rays IDA MCP Server instead!` This matches the seat rule "VERBATIM (normalizing markup only)" and matches the round-72 verifier-spotcheck disposition (corpus/lessons/round-72-verifier-spotcheck.md line 69: "Sentence exists, with the server name as a markdown link ... rendered text matches. agree").
- Next line: "See the announcement blog post for more information." (link to hex-rays.com) — corroborates that the repository itself directs users to the official alternative.

### 3. Scope check (observation + inference)

- Row scope: "The repository's own IDA Pro MCP description and its stated current alternative recommendation; not IDA capability on this host."
- README introduction (line 7 normalized): "Simple MCP Server to allow vibe reversing in IDA Pro." — the repository's own IDA-facing MCP description: **matches**.
- Recommendation banner: present, links `HexRaysSA/ida-mcp`: **matches** "stated current alternative recommendation".
- `## Prerequisites` section exists at this revision: Python 3.11+, IDA Pro 8.3+ (9 recommended), "IDA Free is not supported", plus a supported-MCP-client list. These are setup constraints only; nothing in the README is evidence of IDA capability on this host: **matches** the exclusion.
- The same revision documents ida-pro-mcp's own installation/transports/tools at length (sections: Installation (Claude Code/Codex/Kimi Code/GUI), Prompt Engineering, Transports & Headless MCP, Core Functions, ...). The row's summary "documents an IDA-facing MCP option but itself recommends the official Hex-Rays server" captures this dual state faithfully.

### 4. Tier check (inference)

Tier A is admission limited to the project's own self-description and recommendation. The row attributes only README-stated description/recommendation/prerequisites to the project and explicitly denies host capability: **consistent with tier A**. No capability, execution, installation, or readiness claim anywhere in the chain.

### 5. Used-by / entry wording check (observation)

- Row used-by cell: `corpus/knowledge/round-72-tool-landscape.md` — file exists; row "Need native disassembly/decompilation and analysis" cites `IDA Pro MCP S057` in the repositories column.
- Entry statement: "The IDA-MCP README recommends the official Hex-Rays MCP server." — faithful paraphrase of the banner (README's exact product name "Official Hex-Rays IDA MCP Server", same referent HexRaysSA/ida-mcp). Dropping "IDA" from the product name in the paraphrase does not change the referent (round-72 review noted the same, non-blocking).
- Entry boundary column: "do not infer feature parity, licensing, correct decompilation, or local provider readiness from the list. Review the exact source and current version before selecting one." — no use/readiness inference; no endorsement of installing or using either server: **matches row disposition**.

### 6. Rejection flip check (observation + inference)

No flip condition is triggered:
- Quote present at pin under permitted normalization (not fabricated, not paraphrased — contrast S071 registry defect).
- Quote correctly attributed to this repository at this revision (not misattributed from a sibling source — contrast S082 defect).
- Scope bounded to the project's own words; no overclaim.
- The "recommends the official alternative" fact does not undermine admission: the lesson Gate (corpus/lessons/round-72.md line 16) explicitly admits tier A "for this project's own recommendation and role; note the repository directs users to the official alternative." Recommendation is the admitted content, not a disqualifier.

## Row field-by-field comparison (SOURCES.md line 71)

| Field | Row value | Reopened evidence | Match |
|---|---|---|---|
| source | ida-pro-mcp — https://github.com/mrexodia/ida-pro-mcp | repo exists; README fetched at pin | yes |
| type | tool | project is an MCP server tool repo | yes |
| tier | A | own-words description/recommendation only | yes |
| scope | own description + alternative recommendation; not host capability | banner + intro + prerequisites verified; no host claim | yes |
| located quote | "I recommend using the Official Hex-Rays IDA MCP Server instead!", README intro/"Prerequisites", commit c133c385..., accessed 2026-10-27 | present once under markup-only normalization; pin verified to exist; quote sits in top callout above intro ("introduction" is a fair locator, README has no heading literally named Introduction); prerequisites section exists | yes |
| disposition | documents an IDA-facing MCP option but recommends official Hex-Rays; no endorsement of either | matches dual state of README | yes |
| status | mined | — (registry metadata, unverifiable from source) | n/a |
| accessed | 2026-10-27 | original session not retro-verifiable; my reopen 2026-10-30 re-verifies content at pin | consistent |
| pin class | on-release | commit exists, dated 2026-09-26 | yes |
| used-by | corpus/knowledge/round-72-tool-landscape.md | exists, cites S057, wording checked above | yes |

## Network / source failures

None. Both HTTPS fetches (raw README, commits API) succeeded on first attempt with HTTP 200.

## Uncertainty / verification gaps

- The original 2026-10-27 access session cannot be retro-verified; only content at the pinned revision is verifiable, and it matches (observation-limited claim).
- I verified content at the SHA-pinned raw URL; I did not check whether c133c385... is current HEAD (not required — the row pins a revision).
- Row status/accessed cells are registry metadata; agreement on them is by consistency, not by independent observation.
- Per seat bounds I did not run the frozen counter, inspect other rows, or touch any file outside my report path and scratch.

## Conclusion

**Agree** with the S057 disposition: ADMIT, tier A, mined, used-by `corpus/knowledge/round-72-tool-landscape.md`. Located quote (10 words, ≤25): "I recommend using the Official Hex-Rays IDA MCP Server instead!" — verbatim under markup-only normalization at commit `c133c3853faa111a9b00ee615c013b720d0c4acd`, reopened 2026-10-30, no network failures, no superseding row warranted for S057.
