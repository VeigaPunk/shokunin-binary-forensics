# R64ScoutCensus

## Findings (high confidence)

- Ran `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger` exactly; captured exit **0**, all five stdout lines, and empty stderr.
- Source-row regex census: **35** rows, S001–S035, in `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md:15-49` (snapshot `C9EF`).
- Exactly the four disclosed W04s: **S024 / S028 / S029 / S034**.
- Brief typo/tooling distinction: literal `{{3,}}` pattern returned no matches; `{3,}` counted 35. Specialized grep was used instead of shell grep as required by tool policy.

Axes: validator validity, row cardinality, warning identity, output fidelity. No inference about source quality or future appended rows.

Complete receipt: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/scout-census.md`.

Remaining unknown: post-append census; S036/S037 were absent at observation. No dependency blocked this baseline census.

No production edits; no tool installs/upgrades; no git/jj mutations.

Report: .ufo/waves/round-64/R64ScoutCensus.md
