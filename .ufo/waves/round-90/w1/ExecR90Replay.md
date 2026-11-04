# ExecR90Replay — independent cross-implementation of both frozen truth rules (round 90, w1)

Freeze commit `c7767789fe9e96bcc0d50656ad4bdce69ba3a3a9` (`git log` head at start: `c776778 round-90: freeze …`).
Python 3.14.8 (system). No tools were installed or upgraded. `lxml` 6.1.3 was available, but I used `xml.dom.minidom`, so
the parser family differs from v2's `xml.etree.ElementTree`. Scratch dir
`/fast/scratch/hyaku/revenger-r90/ExecR90Replay`, with TMPDIR set to it. Receipts are in
`/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-90/w1/ExecR90Replay/receipts/`.

## Independence

- `receipts/my_oracle.py` was written from the seat spec alone. It does not import or copy `oracle_check2.py`. I looked at
  v2 lines 130–139 only after my verdicts were in, to explain the probe results.
- `receipts/my_sm6.py` was written from the claims.md C1 predicate and the `sm6_battery.py` docstring. It does not import
  `self_assessment_check*.py`. `drive_sm6.py` gets the CASES tuple by `ast.literal_eval` on the frozen battery file and
  rebuilds the trees with the documented row format.
- The frozen instruments were run only through their own CLIs. One exception: `sm6_probes.py` loads v1 and v2 `sm6()` to
  read their verdicts on the extra probes.

## C2 — oracle battery (9 frozen cases)

Commands (logs are in `receipts/logs/`):
- `python3 -B receipts/my_oracle.py reports/round-90/oracle-battery-cases/*.json` → `oracle-mine.log`
- `TMPDIR=<scratch> python3 -B reports/round-90/oracle_battery.py --oracle corpus/fixtures/apk-r65/oracle_check2.py --write <scratch>/regen`
  → `oracle-frozen-v2.log`: `ORACLE_MISCLASS=0/9`, exit 0
- `diff -r reports/round-90/oracle-battery-cases <scratch>/regen` → `oracle-cases-regen-diff.log`: exit 0. The committed case
  bytes are identical to what the battery generates.
- v2 run directly on each committed case → `oracle-v2-direct-on-committed-cases.log`

| case | frozen label | my label | frozen v2 verdict | agree? |
|---|---|---|---|---|
| P1-real-r89-record | accept | accept | accept (22/22) | agree |
| P2-hand-written-content-accurate | accept | accept | accept (22/22) | agree |
| F1-xml-comment-fragments-fabricated-root | reject | reject (root package com.attacker.fabricated; versions only inside the comment) | reject | agree |
| F2-fabricated-package-everywhere | reject | reject (root package) | reject | agree |
| F3-minimal-three-key | reject | reject (no manifest text) | reject | agree |
| F4-versions-smuggled-into-child | reject | reject (root versionCode=[]) | reject | agree |
| F5-conflicting-duplicate-versionCode | reject | reject (root versionCode=['1','2']) | reject | agree |
| F6-unparseable-text-with-fragments | reject | reject (not well-formed) | reject | agree |
| F7-root-package-disagrees-with-package_name | reject | reject (root package com.example.r66) | reject | agree |

**Disagreements: 0/9.** The frozen labels, my checker and frozen v2 all agree on every case.

### Producer runs (`receipts/logs/producer-runs.log`, observed 2026-11-04T22:04:26Z)

| file (sha256) | my checker | frozen v2 |
|---|---|---|
| `.ufo/waves/round-90/w1/ExecR90Producer/run1.json` (`9d665ffb…`) | accept | ORACLE OK 22/22, rc 0 |
| `.ufo/waves/round-90/w1/ExecR90Producer/run2.json` (`214094fb…`) | accept | ORACLE OK 22/22, rc 0 |

The evidence ids differ between the two runs: run1 is `ev_affae0e5…`, run2 is `ev_d4a34332…`. The manifest text is identical
to the r89 GOOD_TEXT. In both runs `version_code` and `version_name` are `None`.

### Extra probes (not frozen, not part of any kill rule)

Cases are in `receipts/oracle-probe-cases/` and results in `receipts/logs/probes-compare.log`. The labels are mine, applying
the battery docstring rule: `reject` means the record misstates the fixture's manifest or identity.

| probe | my intended truth | my checker | frozen v2 | note |
|---|---|---|---|---|
| X01 structured `version_code="2"`, `version_name="9.9"`, `min_sdk`/`target_sdk`=99, manifest text untouched | reject | accept | **accept** | **shared blind spot** |
| X02 structured `version_code=7` | reject | accept | **accept** | **shared blind spot** |
| X03 `p:package=` (prefixed root package) | accept | accept | accept | v2's docstring says "attribute `package`", but the code matches package by local name (`rsplit("}")`). Harmless, but the docstring and code disagree. |
| X04 DTD internal entity `&v;` → "1" | accept | accept | accept | content is accurate after expansion |
| X05 DTD entity forging the package | reject | reject | reject | — |
| X06 `versionCode=" 1"` | reject | reject | reject | — |
| X07 root `<evil:manifest xmlns:evil="urn:evil">` | reject | accept | **accept** | shared blind spot: both match the root by local name only. Weak case. |
| X08 forged `permissions` | reject | accept | reject | my checker is narrower by spec; v2 is correct |
| X09 duplicate versionName (prefixed and unprefixed) | reject | reject | reject | — |
| X10 `manifest.status="truncated"` | reject | accept | reject | my checker is narrower by spec; v2 is correct |

Finding C2-a: oracle v2 never checks `normalized_result.version_code`, `version_name`, `min_sdk` or `target_sdk`. A record
whose structured fields claim versionCode 2 or 7 passes 22/22. This is not a kill under the frozen claim, because kill rule
(a) covers only the 9 battery cases and none of them varies these fields. It does mean the "record states the fixture's
true identity" reading of `accept` holds only for the manifest-text legs. Proposal for a later round, not to be applied to
the frozen instruments: add a leg requiring each structured version field to be either `None` or equal to the root
attribute, and add an X01-style case to the next battery.

## C1 — SM6 battery (14 frozen cases)

Commands:
- `git -C <lane> archive c7767789… corpus SHONEN.md SCORECARD.md SKILL.md | tar -x -C <scratch>/tree`
- `python3 -B receipts/drive_sm6.py <scratch>/tree <scratch>/sm6work` → `sm6-mine.log`
- `TMPDIR=<scratch> python3 -B reports/round-90/sm6_battery.py --impl corpus/self_assessment_check2.py --real <scratch>/tree`
  → `sm6-frozen-v2.log`: `SM6_MISCLASS=0/14`, exit 0
- The same with `--impl corpus/self_assessment_check.py` (do-nothing control) → `sm6-frozen-v1.log`: `SM6_MISCLASS=7/14`,
  exit 1. This matches the red in claims.md: the misjudged cases are B01, B02, B07, B10, B11, R1 and R2.

My rule: map rows are lines matching `^\| C\d+ \|`; a row is held when its last cell is `held`. The K statement is the last
SCORECARD line containing the word-bounded token `K_HELD_BACKED`. The current side is the segment after the token up to the
next `·`, `;`, `|` or `K_*` token, then the first N/D after the last `→`. Label 0 iff current N/D = held/rows.

| case | frozen label | my label (rows, held, current) | frozen v2 got | v1 got | agree (frozen = mine = v2)? |
|---|---|---|---|---|---|
| B01 | 0 | 0 (15, 8, 8/15) | 0 | 1 | agree |
| B02 | 1 | 1 (15, 8, 8/14) | 1 | 0 | agree |
| B03 | 1 | 1 (15, 8, 9/15) | 1 | 1 | agree |
| B04 | 0 | 0 (15, 8, 8/15) | 0 | 0 | agree |
| B05 | 1 | 1 (15, 8, 8/14) | 1 | 1 | agree |
| B06 | 0 | 0 (14, 8, 8/14) | 0 | 0 | agree |
| B07 | 1 | 1 (14, 8, 8/15) | 1 | 0 | agree |
| B08 | 0 | 0 (15, 8, 8/15) | 0 | 0 | agree |
| B09 | 1 | 1 (15, 8, none) | 1 | 1 | agree |
| B10 | 0 | 0 (16, 9, 9/16) | 0 | 1 | agree |
| B11 | 0 | 0 (15, 8, 8/15) | 0 | 1 | agree |
| B12 | 1 | 1 (15, 7, 8/15) | 1 | 1 | agree |
| R1-real-tree | 0 | 0 (15, 8, line 693 → 8/15) | 0 | 1 | agree |
| R2-forged-8-of-14 | 1 | 1 (15, 8, line 1647 → 8/14) | 1 | 0 | agree |

**Disagreements: 0/14.** My R1 inputs (15 rows, 8 held, SCORECARD:693) match `reports/round-90/c1-real-label.log`.

Working-tree snapshot (`sm6-worktree-snapshot.log`): a sibling seat has uncommitted edits to `corpus/README.md` (+1 line)
and `SKILL.md`. On a copy of those, my label is still 0 (15/8, line 693) and v2 still gives `SM6_MISCLASS=0/14`.

### Extra SM6 probes (not frozen; `receipts/logs/sm6-probes.log`)

| probe | hand truth | mine | v1 | v2 | finding |
|---|---|---|---|---|---|
| S01 `K_HELD_BACKED 8 / 15` | 0 | 0 | 1 | **1** | v2 regex `(\d+)/(\d+)` rejects a spaced fraction, so a true statement is flagged |
| S02 later prose line `old K_HELD_BACKED was 8/14` | 1 | 1 | 0 | 1 | v2 correct |
| S03 `K_HELD_BACKED 8/15` then a separate later line `K_HELD_BACKED_STRICT 7/15` | 0 | 0 | 1 | **1** | **v2 false positive**: the last line *containing* the substring is the STRICT line; `head` before `_STRICT` is empty, so no statement is found and v2 returns 1 |
| S04 `K_HELD_BACKED 7/14 → 8/14 → 8/15` | 0 | 0 | 0 | **1** | v2 reads only the first arrow pair (8/14) |
| S05 `8/14 → 8/15; F4 10/11 → 11/11` | 0 | 0 | 0 | 0 | — |
| S06 token without a fraction | 1 | 1 | 1 | 1 | — |
| S07 ASCII `8/14 -> 8/15` | 0 | **1** | 0 | 0 | **my own bug** (I split only on `→`); v2 handles `->`. No frozen case uses `->` |
| S08 extra `held` cell in a non-status column | 0 | 0 | 1 | 0 | v2 is correct (it anchors on the last cell) |

Finding C1-a: v2's SM6 has three false-positive shapes the frozen battery does not cover: S01, S03 and S04. S03 matters
most. SCORECARD already has diagnostics rows that name only `K_HELD_BACKED_STRICT`, for example SCORECARD:387. If a future
row like that is appended after the main K row, v2 will report SM6=1 even though the K statement is true. None of these
shapes appears in the frozen battery or in the frozen real tree (the last token line is 693, and it has no `_STRICT`), so
the claim's `0/14` stands. Proposal for a later round: select the last line with a word-bounded `K_HELD_BACKED`, take the
last arrow side, and allow whitespace around `/`.

## Verdict

VERDICT: 0/9 and 0/14 disagreements. The frozen labels, my independent rules and the frozen v2 instruments agree on every
frozen case, so I found no shared blind spot inside either battery. Off-battery, I found one shared blind spot in oracle v2
(structured `version_code`/`version_name` are never checked; X01/X02 pass 22/22) and three SM6 v2 false-positive shapes
(S01, S03, S04). Neither kills a frozen claim. Both are routed as proposals.

## Risks / limits

- My SM6 implementation mishandles `->`, as S07 shows. It agreed on all frozen cases only because they use `→` exclusively.
- The X07 and S-probe truths are my own hand labels and have not been adjudicated.
- Producer runs were observed in the wave dir at 22:04Z; they are not the committed landing tree.
