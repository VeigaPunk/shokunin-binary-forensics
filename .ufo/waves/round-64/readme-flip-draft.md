# README flip draft — C07 firmware row (round 64)

DRAFT ONLY. This file does not edit `corpus/README.md`; integration belongs to
L1 (`revenger-r64`). Every line below is relative to the lane root
`/home/vgpnk/Projects/shokunin/revenger-shokunin`.

Source row at base (corpus/README.md line 36, byte-exact, em dash U+2014):

```
| C07 | firmware images | — | — | frontier |
```

Column shape preserved in both replacements: five cells
`| C07 | firmware images | <knowledge entries> | <work evidence> | <status> |`.

## (1) Post-admission row — use only when C1 passes all Q01–Q13

C07 flips `frontier → held`; the knowledge column names only the new entry and
the parenthetical bounds it to the single authored fixture; the work-evidence
column stays `—` (brief: unchanged).

```
| C07 | firmware images | `knowledge/round-64-firmware-region-byte-evidence.md` (manual byte-derived readout of `fixtures/firmware-r63/firmware-r63.bin` only; no general firmware-format, extraction/execution, provider-completeness or authenticity claim) | — | held |
```

## (2) Falsification-fallback row — use only if C1 falsifies

C07 flips `frontier → uncovered` (work evidence exists, no admitted knowledge);
the knowledge column reverts to `—` and the work-evidence column now carries the
existing fixture and saved round-63 record.

```
| C07 | firmware images | — | `fixtures/firmware-r63` (`firmware-r63.bin`, `generator.py`, `truth.json`); `live/runs/round-63` (`inspection.json` `inspect_firmware_regions`, `oracle_check.py`, `receipt.json`, `LEDGER.md`; observation layer only) | uncovered |
```

## (3) Legend text

The legend text needs no change: it defines the four status tokens generically
(`held` = at least one admitted knowledge entry covers the ground; `uncovered` =
work evidence exists but no admitted knowledge entry; `frontier` = no knowledge
and no saved record) and contains nothing C07-specific, so both flips are pure
data-token corrections against an unchanged legend.

## Frozen-counter expectations for each row (measured, not asserted)

- Admission row on a tree where
  `corpus/knowledge/round-64-firmware-region-byte-evidence.md` exists and is not
  marked `admission-status: rejected`: `K_HELD 8/14`, `K_HELD_BACKED 8/14`,
  `K_HELD_BACKED_STRICT 8/14`, `K_ROW C07 status=held`,
  `README_TOKEN_LEGEND_MISMATCH=0`.
- Fallback row on a tree without that entry: `K_HELD 7/14`,
  `K_HELD_BACKED 7/14`, `K_ROW C07 status=uncovered`,
  `README_TOKEN_LEGEND_MISMATCH=0`.
- No other row changes; denominator stays 14 rows / 8 families.

## Adjacent surface L1 must decide (not part of this draft's required rows)

`corpus/README.md` `## Frontier` prose still opens with the C07 bullet
("an authored known-truth firmware fixture is the next probe", lines 63–66).
After either flip that prose is stale, but it is prose, not a coverage-map row;
the round contract only flips the row ("No other README row changes"). This
draft deliberately leaves it untouched — the decision and any wording belong to
L1.
