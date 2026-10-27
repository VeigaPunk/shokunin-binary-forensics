# CoreS066Review — S066 mitmproxy

**Judgment: SUPPORT** for S066 as evidence in the C15 coverage entry. Axes reviewed: coverage and source accuracy. No actionable mismatch found.

## Evidence

- **Pinned source quote and locator:** The cited raw README at commit [`7458ea26ccec7d06ffdc434f878e8d92973aec7e`](https://raw.githubusercontent.com/mitmproxy/mitmproxy/7458ea26ccec7d06ffdc434f878e8d92973aec7e/README.md), introduction immediately after the title/badges, reads: “``mitmproxy`` is an interactive, SSL/TLS-capable intercepting proxy with a console interface for HTTP/1, HTTP/2, and WebSockets.” The S066 quote matches after removing README literal-markup backticks around the name and joining the wrapped line; it is 16 words (within the ≤25-word quote limit). The same sentence appears in current `main` README lines 9–10.
- **Registry metadata:** `corpus/SOURCES.md`, S066 row (round-72 row at line 80): source is the mitmproxy project repository; `kind=tool`, `tier=A`; scope explicitly says its declared HTTP/TLS/WebSocket interception purpose is “not authority to inspect any live traffic”; anchor records README introduction, the cited commit, and access date; status `mined`, opened `2026-10-27`, recheck `on-release`, and `used-by=corpus/knowledge/round-72-tool-landscape.md`. These are the 11 expected cells. The frozen counter requires this row be tool/A/mined, name the entry in `used-by`, and be cited in the entry; the row and entry satisfy those S066 checks.
- **Lesson Gate:** `corpus/lessons/round-72.md`, S066 row at line 25, identifies the README introduction and repeats the quote. Its decision is “ADMIT, tier A for documented network-interception role only; no traffic was intercepted.” This is a documentation admission, not a run claim.
- **Linked entry:** `corpus/knowledge/round-72-tool-landscape.md`, tool-selection row at line 29, cites “mitmproxy S066” and summarizes the README as an interactive TLS-capable proxy for HTTP/1, HTTP/2 and WebSockets. Its boundary states: “This is a live interception surface, not a passive claim about saved records. Do not point it at an undeclared or third-party target.” The entry Scope says traffic tools are named only for documented scope and “none was run”; its header says no tool was installed or executed. The row’s boundary and surrounding scope prevent reading the documentation as authorization or evidence of live-target activity. No run/interception claim is made.
- **Frozen counter identity:** `sha256sum reports/round-72/measure.py` returned `9559b10d49690c4247a4100516bef94c8607fcd198dd77d274c770bdb6df48b3`, matching the frozen claim’s hash.

The entry’s “TLS-capable” is a harmless compression of “SSL/TLS-capable”; omission of “intercepting” from its descriptive cell is compensated explicitly by its boundary (“live interception surface”). Neither changes the documented scope.

## Residual risk and verification gaps

The GitHub REST commit-metadata request was rate-limited, so the commit author date was not independently checked. The README at the exact pinned raw URL was accessible and contained the quote; current `main` contains the same sentence. No source or entry in this review asserts installation or execution. A quarantined round-67 binary also contains a `bridge/mitmproxy/test_capture.py` string; it is not S066 evidence and was not used in this judgment.

Report: .ufo/waves/round-72/w1/CoreS066Review.md
