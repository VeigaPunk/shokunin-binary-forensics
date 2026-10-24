# Round-64 seat brief — R64C4LangPatch

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
Apply the frozen C2/C4 fix to corpus/verify_icon_languages.py (working tree ONLY this file): inside check(), immediately AFTER the existing forged-command control (the lines `forged=copy.deepcopy(receipt)` / `forged['command']+=' --forged'` / `require(not receipt_ok(...),'r{r}: forged receipt command accepted')`), add one control per round r in EXPECTED (47,48,49): `forged_stdout=copy.deepcopy(receipt)`; `forged_stdout['stdout_sha256']=H(b'')`; `require(not receipt_ok(forged_stdout,command,expected_hash,eid,raw_bytes),f'r{r}: forged receipt stdout accepted')`. Do NOT alter receipt_ok or any other line. Then run `cd /home/vgpnk/Projects/shokunin/revenger-shokunin && python3 -B corpus/verify_icon_languages.py --self-test` — must exit 0 with the same PASS tail plus no new failures. Report the exact diff you applied and the observed self-test output.

Report: .ufo/waves/round-64/R64C4LangPatch.md — every Report: trailer path is relative to /home/vgpnk/Projects/shokunin/revenger-shokunin; write it at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/R64C4LangPatch.md
