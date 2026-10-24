# Round 64 preservation baseline

## Capture evidence

- Axis: `corpus/live` + `corpus/fixtures` preservation (path inventory and SHA-256 capture).
- Capture command: `find corpus/live corpus/fixtures -type f | sort | xargs sha256sum`.
- Manifest: `.ufo/waves/round-64/preservation-base.sha256` — 452 SHA-256 records.
- Current inventory: 351 files in `corpus/live` and 101 in `corpus/fixtures`, 452 total.
- Round-63 receipt (`.ufo/waves/round-63/build/R63Preservation.md`) records 345 live + 98 fixture files, 443 total. Current delta: **+9 files**.

## Path-set comparison

Compared the sorted current inventory with path names from the round-63 preservation manifest. The current inventory has these nine paths absent from that manifest:

- `corpus/fixtures/firmware-r63/firmware-r63.bin`
- `corpus/fixtures/firmware-r63/generator.py`
- `corpus/fixtures/firmware-r63/truth.json`
- `corpus/live/runs/round-63/LEDGER.md`
- `corpus/live/runs/round-63/inspection.json`
- `corpus/live/runs/round-63/oracle_check.py`
- `corpus/live/runs/round-63/receipt.json`
- `corpus/live/runs/round-63/stderr.txt`
- `corpus/live/runs/round-63/stdout.raw`

The reverse difference contained only the prior manifest's 12 supplemental references (`corpus/README.md`, `corpus/SOURCES.md`, and the 10 `corpus/verify_*.py` files), which are outside this live/fixtures inventory. No path from the round-63 live/fixtures baseline was missing. Thus the 443-file claim reconciles to 452 current files as 443 baseline paths plus these nine round-63 additions.

## Scope and limitations

This is a working-tree snapshot, not a check against a committed round-64 tree or a claim that later changes preserve these hashes. No tests, build, lint, or formatter were run. No tools were installed.

Report: .ufo/waves/round-64/R64Preservation.md
