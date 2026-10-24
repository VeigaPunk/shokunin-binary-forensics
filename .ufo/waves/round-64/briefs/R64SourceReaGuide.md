# Round-64 seat brief — R64SourceReaGuide

Round contract (read first): /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/claims.md
Frozen counter: /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/measure.py
Red-before receipt: /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/measure-before.log
Lane repo: /home/vgpnk/Projects/shokunin/revenger-shokunin — ABSOLUTE paths only (tools start at fleet root /home/vgpnk/Projects/shokunin).
Bounds: never run git/jj mutations; never commit or push; never edit .ufo/waves spec/registry files, MANIFEST.json, fleet repo files, sibling lanes, lane jj state or the lane Git index; write only the exact lane paths this brief names; /tmp scratch lane-owned under /tmp/revenger-r64-*.
Tooling authorization (operator, 2026-10-19): you may install/upgrade tools via official channels only (uv tool / npx / official binaries in ~/.local/bin); PACMAN IS PAUSED HOST-WIDE — no pacman transactions, ever; record any install (tool, version, channel, reason) in your report.
Time-box: return within 15 minutes with your best findings+evidence; partial results are acceptable.
You are an independent leaf: never block on or wait for another seat; if a needed artifact is absent, record the dependency as a finding and return.
Every Report: trailer path is relative to /home/vgpnk/Projects/shokunin/revenger-shokunin — write it at /home/vgpnk/Projects/shokunin/revenger-shokunin/<that path>.

# Deliverable
Open the REA firmware-analysis guide at the PINNED tag that produced the round-63 record: fetch https://raw.githubusercontent.com/morluto/rea/rea-agents-6.5.0/docs/firmware-analysis.md (record HTTP status, content-length, sha256; if the tag path 404s, list tags via the GitHub API and fetch the nearest 6.5.x tag, recording exactly what you opened). Save the byte-exact snapshot to .ufo/waves/round-64/source-snapshots/rea-firmware-guide.md plus a provenance sidecar (URL, access date 2026-10-24, status, sha256). Extract located quotes (each <=25 words, with line numbers) covering: what inspect-firmware-regions does, the binwalk 3.1.x and unblob 26.6.x version requirement, and any entropy/signature-scan statement the C07 entry may rely on.

Report: .ufo/waves/round-64/R64SourceReaGuide.md — every Report: trailer path is relative to /home/vgpnk/Projects/shokunin/revenger-shokunin; write it at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/R64SourceReaGuide.md
