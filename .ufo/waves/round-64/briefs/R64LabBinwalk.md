# Round-64 seat brief — R64LabBinwalk

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
Binwalk cross-oracle: run binwalk (and binwalk -R for raw scan if useful) on corpus/fixtures/firmware-r63/firmware-r63.bin read-only; compare detected signatures and offsets against truth.json regions; confirm the entry wording that binwalk sees the two zlib members at 512 and 1024 and nothing else (M33 mechanism). Save the exact command outputs to .ufo/waves/round-64/lab-binwalk.md.

Report: .ufo/waves/round-64/R64LabBinwalk.md — every Report: trailer path is relative to /home/vgpnk/Projects/shokunin/revenger-shokunin; write it at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/R64LabBinwalk.md
