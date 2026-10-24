# R64EntryCommands report

## Initial check (before integration)

At the initial check, no derivation commands were run because the candidate was absent from both locations specified by the seat brief. The follow-up below records execution after the entry arrived.

## Evidence

- `/tmp/revenger-r64-entry/candidate.md` — read returned `Path ... not found`.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-64-firmware-region-byte-evidence.md` — read returned `Path ... not found`.
- Commands extracted: 0. Per-command MATCH/MISMATCH: not applicable; no expected outputs were available to compare.

## Axes

- Derivation reproducibility: unmeasured (candidate absent).
- Scope safety: preserved; no commands were run and no corpus file was changed.
This initial check was blocked until the candidate was supplied; the dependency was resolved by the follow-up below.

No tool was installed and no source file was changed during the initial check.

## Follow-up — entry arrived and commands rerun

The integrated entry was present at `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-64-firmware-region-byte-evidence.md`; its observed SHA-256 is `9bf21e5057b77f17a8406af9d006fb4594dd2da54c6d0920f4ca842cfa3e0ebf`. I ran the Observation commands and the Reproduce stdout commands from the lane root, replacing the documented `<repo-root>` placeholder with that root and invoking the saved scratch script as `/tmp/revenger-r64-entry/readout.py`. Scratch outputs stayed under `/tmp/revenger-r64-entry/`.

All **24 commands MATCH** their printed outputs; diffs are none.

| # | Entry command | Result | Diff / observed evidence |
|---:|---|---|---|
| 1 | Item 1: readout `--fact 'image'` | MATCH | None; 2048 bytes, SHA-256 `bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be`. |
| 2 | Item 2: `git show …:corpus/fixtures/firmware-r63/firmware-r63.bin \| sha256sum` | MATCH | None; `bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be  -`. |
| 3 | Item 2: `git show …:corpus/fixtures/firmware-r63/generator.py \| sha256sum` | MATCH | None; `4e5d5975e3cf6362f6fd430f2147d42f75d011978f7d6b5ec86d224c77793db4  -`. |
| 4 | Item 2: `git show …:corpus/fixtures/firmware-r63/truth.json \| sha256sum` | MATCH | None; `9663f90b2b9f29c5beb621e554ed7584eedf5e77d4785f26a453e70dbd5a65e6  -`. |
| 5 | Item 2: `git show …:corpus/live/runs/round-63/inspection.json \| sha256sum` | MATCH | None; `f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9  -`. |
| 6 | Item 2: `git show …:corpus/live/runs/round-63/receipt.json \| sha256sum` | MATCH | None; `e930a549db16a180d4ab05307e073cd71599a3317b9f3d15a0d97843d5c6b94d  -`. |
| 7 | Item 2: `git show …:corpus/live/runs/round-63/LEDGER.md \| sha256sum` | MATCH | None; `25a4a18b76a2a55f3b7ea397ee23bba948be3f1c1a3e13a3194c0f057bb1e1a6  -`. |
| 8 | Item 2: working-tree `sha256sum` of the six listed files | MATCH | None; all six observed digest lines match the entry. |
| 9 | Item 3: `cp corpus/fixtures/firmware-r63/generator.py /tmp/revenger-r64-entry/gen/` | MATCH | None; no stdout, as printed. |
| 10 | Item 3: `cd /tmp/revenger-r64-entry/gen && python3 -B generator.py` | MATCH | None; fixture digest/size and all five region lines match. |
| 11 | Item 3: `sha256sum firmware-r63.bin truth.json` in `gen/` | MATCH | None; both observed digests match the printed output. |
| 12 | Runtime probe: `python3 -V` | MATCH | None; `Python 3.14.8`. |
| 13 | Runtime probe: Python zlib version command | MATCH | None; `1.3.2 1.3.2`. |
| 14 | Item 4: readout `--fact 'regions'` | MATCH | None; exact printed JSON, including contiguous 2048-byte coverage and the three padding spans. |
| 15 | Item 5: readout `--fact 'members'` | MATCH | None; exact printed JSON for both zlib members. |
| 16 | Item 6: readout `--fact 'payloads'` | MATCH | None; exact printed JSON and UTF-8 payloads. |
| 17 | Item 7: readout `--fact 'oracle'` | MATCH | None; exact printed JSON; `all_match: true` and all 25 checks match. |
| 18 | Item 8: readout `--fact 'record'` | MATCH | None; exact printed JSON; `all_match: true` and all 13 checks match. |
| 19 | Item 9: readout `--fact 'digests'` | MATCH | None; exact printed JSON for the four files. |
| 20 | Item 10: `wc -c` for generator, receipt and guide snapshot | MATCH | None; observed `5532`, `492`, `10695`, total `16719`. |
| 21 | Item 10: `sha256sum` for generator, receipt and guide snapshot | MATCH | None; all three observed digest lines match the printed output. |
| 22 | Item 11: saved-record Python inspection command | MATCH | None; observed dictionary exactly matches the printed fields and values. |
| 23 | Reproduce: full seven-fact readout piped through `tee /tmp/revenger-r64-entry/all.txt` | MATCH | None; seven JSON lines match the printed stdout. |
| 24 | Reproduce: `sha256sum /tmp/revenger-r64-entry/all.txt` | MATCH | None; `aa353251f7529a00c4336f9bf8cae6634838b8d10bd20e24b7340d94cf1314ae`, exactly the printed checksum. |

The exact full-output checksum corroborates the seven full JSON lines (including the long `members`, `oracle`, and `record` lines). The repo fixture/evidence files were only read; the generator's writes and the readout capture were confined to the assigned `/tmp` scratch. No tools were installed.

Report: `.ufo/waves/round-64/R64EntryCommands.md`
