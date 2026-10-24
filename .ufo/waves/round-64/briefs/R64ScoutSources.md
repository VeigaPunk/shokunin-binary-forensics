# Round-64 seat brief — R64ScoutSources

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
Registry id-space recon: confirm the next unused S-id is S036 (grep the registry and corpus/lessons); reconcile the round-63 routed note that reserved S036 for a future zipfile-docs row (.ufo/waves/round-63/build/R63SourceZipfileDocs.md) with this round's claims.md opening S036 for the REA firmware guide — determine from the registry contract whether an unopened lead can reserve an id (read the Leads section rule: a lead is not evidence and never a row) and report the first-use-wins disposition. Save to .ufo/waves/round-64/scout-sources.md.

Report: .ufo/waves/round-64/R64ScoutSources.md — every Report: trailer path is relative to /home/vgpnk/Projects/shokunin/revenger-shokunin; write it at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/R64ScoutSources.md
