# CoreS055Review — round 72 w1, item S055 (Ghidra README row)

Verdict: **SUPPORT** (row and linked entry text verified; two minor, non-load-bearing wording notes; no falsifying mismatch).

Seat: `CoreS055Review` · reviewer · axes: coverage, source accuracy · leaf member, read-only except this report.
Scope held: only S055 and the S055-linked text of `corpus/knowledge/round-72-tool-landscape.md`. The Ghidra Book row (S089) and all other tool rows are out of scope; identity separation in the entry is clean (every mention carries its own S-id).

## 1. Frozen-predicate slice checks

- Counter identity: `sha256sum reports/round-72/measure.py` → `9559b10d49690c4247a4100516bef94c8607fcd198dd77d274c770bdb6df48b3` — matches the freeze in `reports/round-72/claims.md`.
- Row shape: `corpus/SOURCES.md:69` is an 11-cell row starting `| S055 |`. Against the counter's per-row tests (`measure.py:49-56`): cells[2]=`tool` ✔, cells[3]=`A` ✔, cells[7]=`mined` ✔, cells[10] contains `corpus/knowledge/round-72-tool-landscape.md` ✔.
- Citation closure: the entry contains the token `S055` (`corpus/knowledge/round-72-tool-landscape.md:24`, "Ghidra S055"), so `S055 ∈ cited` ✔.
- Coverage-map status: `corpus/README.md:55` row `C15` points at the entry in its claims cell and its status cell currently reads `uncovered`. Consistent with pre-integration state; the `held` flip is L1's integration step. Observed, not judged here.

## 2. Pinned source reopened (fetch receipts, 2026-10-27)

- Raw README at the pin: `https://raw.githubusercontent.com/NationalSecurityAgency/ghidra/864999d7ca67cd3f533be600860f102e54370661/README.md` → HTTP 200, `text/plain`. Present at that exact revision:
  - Heading anchor: `# Ghidra Software Reverse Engineering Framework` (line 3 of the file) — matches the row's locator `README.md "Ghidra Software Reverse Engineering Framework"`.
  - Quote sentence: `Capabilities include disassembly, assembly, decompilation, graphing, and scripting, along with hundreds of other features.` — the row's quoted span is the first 10 words (≤25 ✔).
  - Platforms support for the row's "listed platforms": `...enable users to analyze compiled code on a variety of platforms including Windows, macOS, and Linux.`
- Revision existence: GitHub commit page `https://github.com/NationalSecurityAgency/ghidra/commit/864999d7ca67cd3f533be600860f102e54370661` → 200. Commit `864999d` = "GP-7366: Enabling support for Python 3.15" by ryanmkurtz, parent `1de7bd3`, 4 files changed; README.md's only change in it is the build-tools line `(version 3.9 to 3.14)` → `(version 3.9 to 3.15)`. Page `og:updated_time` epoch `1791892552` = 2026-10-13 11:55:52 UTC (derived from GitHub's meta field; approximate commit time).
- Freshness spot-check: `https://raw.githubusercontent.com/NationalSecurityAgency/ghidra/master/README.md` fetched 2026-10-27 is textually identical to the pinned revision (same heading, same capabilities sentence, same 3.9-to-3.15 line this commit introduced). The pin is current as of access; the located quote does not depend on this staying true.
- Access date: row anchor says `accessed 2026-10-27`; both fetches today returned the same bytes — consistent.
- Fetch-channel note (honesty record): `api.github.com/repos/.../commits/864999d...` returned HTTP 403 (rate-limited); commit existence was verified instead via the HTML commit page plus the raw fetch at the ref. No conclusion rests on the API alone.

## 3. Quote precision note (not a defect)

In the raw markdown bytes the capabilities sentence soft-wraps: `...Capabilities include disassembly, ` + newline + `assembly, decompilation, graphing, and scripting, ...`. A byte-exact single-space substring search for the row's quote therefore misses; the quote is exact in the rendered paragraph. The heading anchor + commit pin keep it re-derivable; same rendered-vs-raw distinction this registry already recorded for S052.

## 4. Scope, status, used-by

- Row scope: "The project README's own description of static SRE capabilities and listed platforms; no installation or host capability claim". Capabilities ✔ and platforms ✔ are README-backed (§2). Row notes add only: "release prerequisites and security advisories must be checked separately" — correctly declining to convert the README's Install/Security Warning sections into any readiness claim.
- Entry text (line 24, S055-linked): `Ghidra lists disassembly, assembly, decompilation, graphing and scripting.` — accurate to the README list (only the Oxford comma before "and scripting" is dropped). The boundary cell and the entry's Scope/Unknown sections explicitly disclaim installation, testing, host availability, and correctness; no tested-capability or host-readiness claim exists anywhere in the S055-linked text. No README-external claim found.
- Status/used-by: `mined` / `on-release` / used-by `corpus/knowledge/round-72-tool-landscape.md`, all present in the row and coherent with the entry.

## 5. Minor wording notes (revise-optional, non-load-bearing)

1. `static SRE capabilities` (row scope): the README never uses the word "static"; it says "software reverse engineering (SRE) framework" and "analyze compiled code". The listed capabilities are static-analysis operations and the README claims no dynamic capability, so the qualifier narrows rather than extends — an editorial characterization, not README vocabulary.
2. Entry grouping heading "Need native disassembly/decompilation and analysis" (line 24): "native" is likewise not README vocabulary (README: "analyze compiled code"). Guarded by the same cell's "do not infer ... from the list" boundary.

Neither note adds a capability, execution, or host-readiness claim; both are below the falsify bar.

## 6. Residual risk and gaps

- Whether commit `864999d` was the README tip at the 2026-10-27 access moment cannot be retro-proven without API history (403); immaterial because the row's locator is the pinned commit itself, and today's master README is identical.
- `untrusted data` handling: the fetched README/commit pages were read as data only; no embedded instruction was followed.
- Outside this seat: the other 17 rows, the entry's non-Ghidra claims, the C15 flip, and the counter's full-tree run on the final committed tree (judge/L1: `python3 reports/round-72/measure.py <tree>` must print `C15_HELD_BACKED=1/1`, `C15_TOOL_ROWS=18/18`, exit 0).
