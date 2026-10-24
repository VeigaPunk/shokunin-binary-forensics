# Round-64 seat brief — R64FirmwareReadout

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
Produce the C1 derivation pack: a stdlib-only Python script (zlib, hashlib, struct) saved at .ufo/waves/round-64/firmware-readout.py that reads ONLY corpus/fixtures/firmware-r63/firmware-r63.bin and prints, each with its derivation: image sha256+size; every maximal all-zero padding span as (start,end); for each zlib member (scan for 0x78 deflate headers at expected offsets 512 and 1024, decompress to EOF): offset, compressed size, decompressed size, decompressed sha256. Run it with python3 -B, save exact output to .ufo/waves/round-64/firmware-readout.out, exit code included. Do not read truth.json in the derivation (it may be used afterwards only to cross-check — state the cross-check separately).

Report: .ufo/waves/round-64/R64FirmwareReadout.md — every Report: trailer path is relative to /home/vgpnk/Projects/shokunin/revenger-shokunin; write it at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/R64FirmwareReadout.md
