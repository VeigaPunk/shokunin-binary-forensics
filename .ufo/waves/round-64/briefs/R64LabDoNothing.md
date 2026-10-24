# Round-64 seat brief — R64LabDoNothing

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
Independent do-nothing re-derivation: `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive 666ea84b6be2eec2b0359f556ba2429fc9044c36 corpus | tar -x -C /tmp/revenger-r64-donothing/` then `cd / && TMPDIR=/tmp/revenger-r64-donothing python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/measure.py /tmp/revenger-r64-donothing`; diff the label lines against the committed reports/round-64/measure-before.log — every frozen label value must match (K 7/14, STRICT 7/14, MISMATCH 1, C4 0/2, holds green, exit 0). Report the diff.

Report: .ufo/waves/round-64/R64LabDoNothing.md — every Report: trailer path is relative to /home/vgpnk/Projects/shokunin/revenger-shokunin; write it at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/R64LabDoNothing.md
