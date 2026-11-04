# Draft — round-90 lesson `## Mistakes` rows for r89 routed D1–D3

Format follows the current convention (`corpus/lessons/round-73.md:21` …
`corpus/lessons/round-89.md:88`): `| class | evidence pointer | captured-by | fix |`.
Paths are lane-relative inside the table (as in every prior lesson); lane root
`/home/vgpnk/Projects/shokunin/revenger-shokunin`.

```
| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| reference-drift / relocation not swept (D1): the r89 adjudication `bd575ca` moved the android record to `reports/round-89/rejected-android-record/` but left two live pointers at the old path | `corpus/SOURCES.md:498` (S481 `source` and anchor `corpus/live/runs/round-89/receipt.json`); `corpus/knowledge/2026-10-12-rea-readiness-checklist.md:67`; red probe `.ufo/waves/round-90/w1/ScribeR90Quality/d1-dead-path-probe.log` (`SOURCE_PATH_DEAD_PROBE=2`, both S481 cells) | non-author r89 spot-check (`lessons/round-89-verifier-spotcheck.md:168,211-218`); no criterion caught it before — Q17 added this round | new SOURCES row whose `teaches` opens `supersedes S481 —` citing `reports/round-89/rejected-android-record/receipt.json` (:6, :20, :31 byte-verbatim); appended `Correction (round 90):` paragraph in the checklist (no rewrite); Q17 with `reports/round-90/source_path_check.py` `SOURCE_PATH_DEAD=0`, red 2 at the freeze |
| attribution / asserted-but-absent table (D2): the r89 lesson's `## Gate` says "The final source-opening table records the exact path, access date, located quote and disposition" but carries no such table; it exists only in a wave seat file | `corpus/lessons/round-89.md:69-74` (no table under `### Source openings`); the table at `.ufo/waves/round-89/w1/ScribeR89Sources.md` | non-author r89 spot-check (`lessons/round-89-verifier-spotcheck.md:219-224`) against CORPUS rule 1 (every new row: URL/path, access date, ≤25-word located quote in the lesson's `## Gate`); existing Q16 class (a sentence describing content the artifact does not hold) | the round-90 lesson's `## Gate` carries the source-opening table inline for every new row (including the S481-superseding row and the two C2 `<manifest>` / ElementTree rows, `reports/round-90/claims.md:90-95`); r89 lesson stays as filed, this row is the correction pointer |
| number-drift / un-receipted count (D3): the r89 report quoted "`self_assessment_check.py` SM2 drops 1 → 0" with no counting command or receipt file | fleet `.ufo/reports/round-89/revenger.md:78`; `SCORECARD.md:1635` ("SM2 fixed this round, 1 → 0"); receipt now `.ufo/waves/round-90/w1/ScribeR90Quality/sm2-receipt.log`: base `2b017fa3` → `SM2=1`, `SELF_MISMATCH=2`, exit 1; tip `c8cc585c` → `SM2=0`, `SELF_MISMATCH=1`, exit 1 (checker sha256 `82e59fce…35cc`, byte-equal at both revs) | non-author r89 spot-check (`lessons/round-89-verifier-spotcheck.md:225-230`); existing Q11 (count carries its command and output) — the report, not an entry, so admission did not gate it | the value holds (1 → 0 re-derived); land the receipt under `reports/round-90/` with the commands, and keep the rule: every quoted count in a report names its receipt file |
```

Count line (for the lesson, after landing):
`awk -F'|' '/^\| (reference-drift|attribution|number-drift)/{n++} END{print n}'` over the
`## Mistakes` block → 3. Captured by a new criterion: 1 (D1 → Q17); by an existing criterion
not enforced at report/lesson level: 2 (D2 → Q16/CORPUS rule 1, D3 → Q11).

Note on D3 scope: the receipt shows SM2 1 → 0 and that SM6 stays 1 at both ends; SM6's `/14`
hard-code is C1's surface (`reports/round-90/claims.md:24-33`), not D3's. Both runs exit 1
because `SELF_MISMATCH` is non-zero at both revisions — the r89 report did not claim the gate
went clean, so there is no conflict.
