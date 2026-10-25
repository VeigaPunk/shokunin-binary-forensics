SURVIVORS — gate kills 4/6 entry mutants, but embedded-line deletion (M2) and a corrupted-flag command whose output is a superset of the embedded lines (M5) both exit 0; two unguarded clauses located in `corpus/check_embedded_outputs.py`.

Seat: R70W1GateMutants · wave 1 (advisory pre-gate, not a kill-rule input) · 2026-10-25

## Setup

- Scratch: `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive aa1842fac199aa524930e5565ed3715de5f84c6d corpus | tar -x -C /tmp/revenger-r70-R70W1GateMutants` (deleted before return).
- Detector: `python3 -B corpus/check_embedded_outputs.py --entry <mutated>` run from the scratch root, exactly as the entry's embedded commands assume (`corpus/...` relative).
- Pristine baseline (conclusiveness precondition): `checked_blocks=22 problems=0`, exit 0.
- Bytes under test: entry `0913f6515e93889a7a4204a613f52a3ff8d505742038dfa0d46443a79b088368`, gate `79cff2fa0ebdfe82ac6f66c5cb7027b29e1c8c2f620efc65a0eea4f1253fb57b` — lane working tree verified identical to the archived candidate before and after the probe.
- Tooling: Python stdlib only; no packages installed, no pacman transactions (host pause respected).

## Mutants (each on a fresh copy of the pristine entry)

| # | Mutant (file:line) | Detector output (last lines) | Exit | Verdict |
|---|---|---|---|---|
| M1 | entry:34 `"parsed_entries": 3` → `4` | `drift entry:34 embedded output line not in recheck stdout: {"…parsed_entries": 4, …}` · `checked_blocks=22 problems=1` | 1 | KILLED |
| M2 | entry:159 deleted `MATCH eocd.total_entries: … u16(apk, eocd + 10) present=True` | `checked_blocks=22 problems=0` | 0 | **SURVIVED** |
| M3 | entry:47 `payload_first16_hex` `"4d61…"` → `"4d16…"` (chars 3–4 swapped) | `drift entry:47 embedded output line not in recheck stdout: {…"4d166e…"…}` · `problems=1` | 1 | KILLED |
| M4 | entry:160 `MATCH eocd.cd_size:` → `MISMATCH eocd.cd_size:` | `drift entry:160 embedded output line not in recheck stdout: MISMATCH eocd.cd_size: …` · `problems=1` | 1 | KILLED |
| M5 | entry:26 `--fact archive` → `--fakt archive` | `checked_blocks=22 problems=0` | 0 | **SURVIVED** |
| M6 | entry:37 appended `eocd total_entries cross-check: 3 entries verified ok` (not printed by `entry_checks.py --eocd`) | `drift entry:37 embedded output line not in recheck stdout: eocd total_entries cross-check: …` · `problems=1` | 1 | KILLED |

Mutant after-hashes (before-hash all six = pristine `0913f651…`): m1 `4d317558…`, m2 `2a541678…`, m3 `97ea0cb2…`, m4 `369558ae…`, m5 `175f5081…`, m6 `44c4acd3…`.
Gate self-test during the same session: `--self-test` exit 0.

## Located defects (why the two survive)

1. **One-directional verbatim comparison — M2 clause: deleting embedded output is invisible.**
   `corpus/check_embedded_outputs.py:113-115` — `drift()` returns problems only for embedded lines absent from recheck stdout; `:140` (`problems += drift(lines, stdout_set, lineno)`) never asks the converse, and `:141` counts blocks, not lines. Deleting entry:159 leaves 15 embedded lines that are all still members of the 16-line stdout set → `problems=0`, exit 0. Degenerate case included: a block whose entire output block is deleted still checks (`drift([])` is empty) with `checked_blocks` unchanged.
2. **No command-identity or stdout-superset check — M5 clause: a broken command that prints a superset passes.**
   Direct reproduction from the scratch root: `python3 -B corpus/fixtures/apk-r65/readout.py --fakt archive` exits 0 and prints **all 15 facts** (first line is exactly the embedded archive line). Cause: `corpus/fixtures/apk-r65/readout.py:43` — `ONLY = sys.argv[sys.argv.index("--fact") + 1] if "--fact" in sys.argv else None`; any argv without a literal `--fact` (typo'd flag included) silently degrades to the full dump. The gate's only command-health check is `rc != 0` (`check_embedded_outputs.py:136-138`); stdout lines with no embedded counterpart are never flagged (same one-directional gap as M2), so the corrupted command is scored clean.

## Advisory for the pre-declaration repair (wave-1 only)

C3's kill rule freezes the registered C7 line `check_embedded_outputs.py:140` byte-identical, so the repair must sit **beside** it, not rewrite it: a converse check (recheck stdout lines not covered by embedded output, or a per-block embedded-line-count pin) closes M2 and also the superset half of M5; closing M5's command-identity half needs the command to be re-derived/pinned, not merely re-executed — e.g. refusing argv that is not a known-good spelling per block, or a fixture-side strict-arg mode (`readout.py` erroring on unknown flags would convert M5 into a killed rc!=0 mutant without touching line 140). Recorded as a coverage finding only; per seat discipline I did not judge, integrate, or modify any contract.

## Restoration / hygiene evidence

- All six mutants were applied to scratch copies only; the pristine scratch entry re-hashed `0913f651…` after all runs.
- Lane entry before probe: `0913f651…`; after probe: `0913f651…` (identical, `sha256sum` on `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-70-apk-axml-byte-evidence.md`).
- Lane gate `79cff2fa…` and fixture `readout.py 92e347c3…` verified identical to the tested scratch bytes; no lane file was written, no git/jj mutating command run anywhere.
- Scratch `/tmp/revenger-r70-R70W1GateMutants` deleted (`ls`: No such file or directory).
