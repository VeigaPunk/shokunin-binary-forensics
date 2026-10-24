# Round-64 seat brief — R64SentinelScope

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
Scope guard: run `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin status --porcelain` at your start and again just before returning; the only expected lane working-tree changes are: reports/round-64/*, .ufo/waves/round-64/**, corpus/verify_icon_languages.py, corpus/verify_multi_icon_states.py (and, after L1 integration only, corpus/knowledge/round-64-*, corpus/lessons/round-64.md, corpus/README.md, corpus/SOURCES.md, SKILL.md). Flag ANY other tracked-file modification with the file name and a one-line diff summary. Also verify no seat wrote into /home/vgpnk/Projects/shokunin (fleet root) — list offenders if any.

Report: .ufo/waves/round-64/R64SentinelScope.md — every Report: trailer path is relative to /home/vgpnk/Projects/shokunin/revenger-shokunin; write it at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/R64SentinelScope.md
