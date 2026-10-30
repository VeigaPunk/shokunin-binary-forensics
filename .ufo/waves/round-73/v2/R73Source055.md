# R73Source055 — frozen C10 coverage admission, source audit S055 (Ghidra)

Seat: R73Source055 · reviewer role · axes: coverage, source accuracy · leaf member (no subagent dispatch).
Assignment scope: SOURCES.md row S055 only. No other source admission; no row edits anywhere
(S071/S082 routed defects are handled by append-only superseding rows per
`corpus/lessons/round-72-verifier-spotcheck.md` — not this seat's row, nothing written by me).
Read-only besides this report. Network: no failures this session (both fetches below succeeded).

## Located quote, pin, access

- Row: `corpus/SOURCES.md:69` — `| S055 | Ghidra — https://github.com/NationalSecurityAgency/ghidra | tool | A | … |`
- Cited primary URL: https://github.com/NationalSecurityAgency/ghidra
- Cited pin: commit `864999d7ca67cd3f533be600860f102e54370661` (row evidence cell: "accessed 2026-10-27")
- Re-opened by me: 2026-10-30 (access date), via
  `https://raw.githubusercontent.com/NationalSecurityAgency/ghidra/864999d7ca67cd3f533be600860f102e54370661/README.md` → HTTP 200, 7205 bytes.
- Pin existence confirmed 2026-10-30 via GitHub API
  (`/repos/NationalSecurityAgency/ghidra/commits/864999d7ca67cd3f533be600860f102e54370661` → 200;
  author Ryan Kurtz, dated 2026-10-13, message "GP-7366: Enabling support for Python 3.15"). Observation.

## Located quote (verbatim, 8 words, ≤25 ✔)

> "Capabilities include disassembly, assembly, decompilation, graphing, and scripting"

Verbatim comparison (normalizing markup only): **MATCH.**
In the pinned README raw markdown the sentence soft-wraps across lines 7–8:

```
variety of platforms including Windows, macOS, and Linux. Capabilities include disassembly,
assembly, decompilation, graphing, and scripting, along with hundreds of other features.
```

A byte-exact single-line substring search misses; normalizing only the soft-wrap line break
(rendering the paragraph), the quoted span is an exact prefix of the sentence, closed by
", along with hundreds of other features." The heading anchor
`# Ghidra Software Reverse Engineering Framework` (line 3) is also verbatim, matching the row's
locator. Observation; exact bytes preserved in seat scratch receipt (see Cleanup).

## Scope, tier, used-by, flip

- Scope (row): "The project README's own description of static SRE capabilities and listed
  platforms; no installation or host capability claim." Pinned README backs both halves:
  capabilities list (quote above) and platforms sentence ("analyze compiled code on a variety of
  platforms including Windows, macOS, and Linux."). No installation/host-readiness claim is made
  by the row or the entry. Agree. Minor note (non-defect, matches round-72 seat finding): the word
  "static" is editorial, not README vocabulary — it narrows rather than extends. Inference.
- Tier A: official National Security Agency maintainer repository. Agree. Observation.
- Used-by: `corpus/knowledge/round-72-tool-landscape.md:24` — "Ghidra S055 … Ghidra lists
  disassembly, assembly, decompilation, graphing and scripting." Accurate to the README list
  (Oxford comma dropped only); cited token S055 present in the entry. Agree. Observation.
- Rejection flip: none warranted. Quote verbatim at pin, scope bounded, tier and used-by coherent,
  lesson Gate row (`corpus/lessons/round-72.md:14`, ADMIT tier A / not readiness on this host)
  consistent with the registry row. **I agree with the source disposition (mined, on-release, ADMIT
  tier A).**

## Round-72 cross-references

- `reports/round-72/shortlink-dispositions.md:27`: t.co/P6Abt6uAoH → same Ghidra repository,
  re-opened, correctly recorded as duplicate of S055 with no duplicate row. Consistent with
  S055 being a singleton registry id (counter duplicate check unaffected).
- S071/S082 routed quote defects (`corpus/lessons/round-72-verifier-spotcheck.md`): out of this
  seat's scope; per assignment, any fix must be a NEW append-only superseding row, never an edit
  of the old row. No row written by me.

## Residual risk / unknowns

- Whether commit `864999d` was the README tip at the 2026-10-27 access moment is not re-proven
  here (unnecessary: the row's locator is the pinned commit itself, which exists). Unknown, immaterial.
- Fetched README/API JSON read as data only; no embedded instruction followed.

## Receipts and cleanup

Receipt bytes: pinned README fetch (7205 bytes) at seat scratch
`/fast/scratch/hyaku/revenger-r73/R73Source055/ghidra-README-864999d.md` — key lines reproduced
verbatim in this report (heading line 3; capabilities sentence lines 7–8); scratch directory
removed after this report was written. No builds/tests run (none requested). No installs this seat
(nothing needed; pacman paused host-wide).
