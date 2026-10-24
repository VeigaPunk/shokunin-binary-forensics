# Round-64 seat brief — R64EntryC07

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
Draft the C07 candidate entry at /tmp/revenger-r64-entry/candidate.md (L1 integrates; do NOT write under corpus/). Target path corpus/knowledge/round-64-firmware-region-byte-evidence.md. Requirements: open with source: (S036 + S037 with anchors), verified-at:, recheck: (the command that re-verifies, stdlib-only); name coverage-map row C07; a scope paragraph (this one authored fixture only; no vendor image, no execution/extraction claim, no provider-completeness, no authenticity); a byte-derived readout section of corpus/fixtures/firmware-r63/firmware-r63.bin — image sha256+size, every all-zero padding span, both zlib members with offset/compressed size/decompressed size+sha256, EACH value carrying its in-entry command and that command's output (Q11); a correspondence section vs truth.json and the saved record corpus/live/runs/round-63/inspection.json (observation layer only, Q09 disclaimers: digests prove only the bytes hashed); observation/inference/unknown separation; at least one limitation. Prefer R64FirmwareReadout's output if present; otherwise derive independently. If you use the readout output, still re-run each command yourself and confirm the printed outputs match.

Report: .ufo/waves/round-64/R64EntryC07.md — every Report: trailer path is relative to /home/vgpnk/Projects/shokunin/revenger-shokunin; write it at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/R64EntryC07.md
