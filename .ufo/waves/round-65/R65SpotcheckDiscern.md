# R65SpotcheckDiscern — outside-discernment spot-check (round 65)

REJECT the candidate `corpus/knowledge/round-65-apk-axml-byte-evidence.md` at its current bytes — Q11 fails on line 41: the embedded `payload_first16_hex` for `META-INF/MANIFEST.MF` is not the readout's output (`4d616e696673742d…` = "Manifst-Version", 15 bytes, vs the real `4d616e69666573742d…` = "Manifest-Version", 16 bytes); one corrected line + a re-run clears it. AGREE that `corpus/knowledge/commonjs-destructured-require-edges.md` and `corpus/knowledge/evm-saved-interface-candidates.md` stay rejected (their round-61 Q11 causes are still present in the file bodies).

Seat: `R65SpotcheckDiscern` (read-only). Everything below was run from
`/home/vgpnk/Projects/shokunin/revenger-shokunin` unless an absolute path is shown.
No tool was installed or upgraded (nothing needed; all checks used `python3`,
coreutils and the lane's own committed scripts). No measurement is claimed: the
wave has no committed after-tree, and measurements belong to committed trees only.

## Basis read before scoring

- Frozen contract `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-65/claims.md` (kill rule, predicate, admission order).
- Frozen counter `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-65/measure.py`; red-before `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-65/measure-before.log`.
- Gate: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/QUALITY.md` (Q01–Q13 + Admission procedure), `/home/vgpnk/Projects/shokunin/revenger-shokunin/SKILL.md:118-160`, `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/lessons/round-61.md:95-131` (the erratum that rejected the two retained candidates).
- Outside-discernment requirement: `/home/vgpnk/Projects/shokunin/LEARNING.md` §"Discernment is checked from outside" (at least one admit and one reject sampled).

## F1 (HIGH, blocks admission) — a carried output line is not the deriving command's output (Q11)

QUALITY.md Q11 demands that each value in an entry carry, inside the entry, the
command and **that command's output**. One of the fifteen embedded objects is not
the output of the committed readout.

Command and actual output:

```
$ sha256sum corpus/fixtures/apk-r65/readout.py
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  corpus/fixtures/apk-r65/readout.py   # = entry header digest
$ python3 -B corpus/fixtures/apk-r65/readout.py > /tmp/r65read.out; echo exit=$?; wc -l /tmp/r65read.out; sha256sum /tmp/r65read.out
exit=0
15 /tmp/r65read.out
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247  /tmp/r65read.out   # = entry `recheck:` digest
```

Field-level comparison of the entry's embedded objects against that stdout
(strict JSON equality per fact) gave 14/15 MATCH and one DIFF:

```
FIELD payload_first16_hex:
  entry  = '4d616e696673742d56657273696f6e'
  actual = '4d616e69666573742d56657273696f6e'
```

Entry pointer: `corpus/knowledge/round-65-apk-axml-byte-evidence.md:41`
(`grep -n 4d616e696673742d56657273696f6e` matches only that line). The entry
value decodes to `b'Manifst-Version'` (15 bytes) while the payload's real first
16 bytes decode to `b'Manifest-Version'` — and the same item 10 of the entry
independently states `first_line: "Manifest-Version: 1.0"`, so the entry's own
two values contradict each other. `truth.json` carries no `payload_first16_hex`
field, so the bad value was hand-transcribed, not copied from the oracle.

Why this is the admission-blocking class rather than a typo to wave through:
the entry's §Reproduce states "the same lines appear in the full 15-line stdout
reproduced there", which is false for this line, and QUALITY.md
"Admission procedure" step 2 admits only when **no** criterion fails. This is the
same Q11/M26 shape that rejected both round-61 candidates
(`corpus/lessons/round-61.md:105-106`, `:128`). Fix: replace the field with
`4d616e69666573742d56657273696f6e`, re-run
`python3 -B corpus/fixtures/apk-r65/readout.py` and re-confirm the 15-line
digest `507d79f8…`; nothing else in the entry depends on that field.

## F2 (MEDIUM, needs a lane ruling) — Q01 reuse of rows opened in an earlier round

Entry §Observation item 3 and the `Q01` cell of the entry's §Q-map rest the
container walk on `S032` (central-directory 46-byte fixed part) and `S034`
(local-header 30-byte fixed part), both mined in round 63. Q01's text
(`corpus/QUALITY.md`) requires a row "tier A **for that claim's scope** and was
opened in the round that wrote it". The entry discloses the reuse ("already mined
as S032/S034"), so this is not silent absorption, but under the literal criterion
the widths are load-bearing and were not opened this round. Precedent points the
other way: the round-64 admitted entry's Q01 row says "No other source is used"
(`corpus/knowledge/round-64-firmware-region-byte-evidence.md:209`), i.e. the lane
has previously avoided exactly this reuse. Note that `S040` (CPython zipfile docs,
`status=queued` per `awk -F'|' '/^\| *S040 *\|/{print $9,$10}' corpus/SOURCES.md`
→ `queued 2026-10-24`) would not close the gap either — its own scope defers the
format to S032/S034.

## F3 (MEDIUM, anchor precision) — the cited enum range does not contain `0x0180` (Q02)

Entry item 4 says the six chunk types "are the values S038's chunk-type enum
names at lines 239-250". Checked against the frozen snapshot
(`.ufo/waves/round-65/source-snapshots/ResourceTypes.h`,
sha256 `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f`, matching
the lesson's recorded digest):

```
$ sed -n '236,258p' .ufo/waves/round-65/source-snapshots/ResourceTypes.h
239: RES_STRING_POOL_TYPE 0x0001   241: RES_XML_TYPE 0x0003
245: RES_XML_START_NAMESPACE_TYPE 0x0100   246: END_NAMESPACE 0x0101
247: RES_XML_START_ELEMENT_TYPE 0x0102     248: END_ELEMENT 0x0103
253: RES_XML_RESOURCE_MAP_TYPE 0x0180      <-- outside 239-250
```

The resource-map type `0x0180` — load-bearing for entry item 4 and item 7 — is at
line 253, outside the cited range; the same truncated range is inherited by the
registry row (`corpus/SOURCES.md:52`, `chunk-type enum :239-250`). The other
S038 anchors do verify exactly: `struct ResChunk_header` :218,
`struct ResStringPool_header` :461, `struct ResXMLTree_header` :612,
`struct ResXMLTree_node` :621, `struct ResXMLTree_attrExt` :677,
`struct ResXMLTree_attribute` :707, `struct Res_value` :287,
`UTF8_FLAG = 1<<8` :480 (so the entry's `flags 0x00000100` reading is anchored),
and the derived 28-byte pool header is the struct's own 8 + 5×4.

## F4 (LOW, bookkeeping) — Q08 row absent; no same-author caveat on the oracle

The §Q-map carries Q01–Q07 and Q09–Q13 but no Q08 row; the round-64 entry keeps a
row reading "Superseded by Q11" (`round-64-firmware-region-byte-evidence.md:216`).
`SKILL.md:118-160` says applying Q08 instead of Q11 is a Q11 failure, so the
omission is defensible, but the admission procedure says to apply every criterion
and mark `n/a` with its reason. Separately, truth.json and generator.py are
same-author with the entry; the entry labels the comparison honestly
("Comparison with the authored oracle") but carries no same-author caveat of the
kind the round-64 entry records in its §Unknown (U6). Both are wording, not
substance: I re-built the fixture and got byte identity, so Q06's premise holds.

Positive checks that passed on independent command:

```
$ python3 -B generator.py    # in a fresh /tmp scratch copy of generator.py
gen_exit=0; fixture.apk 947 bytes sha256 05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e
cmp -s $T/fixture.apk corpus/fixtures/apk-r65/fixture.apk -> BYTE-IDENTICAL
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact eocd   # single-fact form works, exit 0
```

Registry rows exist and are tier A: `S038`, `S039`, `S040`, `S041` present;
census `rows=41` (claims said 37 → 41). `S039` quote anchored at snapshot line 5
("Start with `inspect_android_package` on the caller's APK path for package
identity, manifest declarations, coverage, and inline Evidence."), snapshot
sha256 `412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c`.
Entry header carries `source:`, `verified-at:`, `recheck:`, `coverage-map: C05`,
`admission-status: candidate` (marker at byte 3777 — past the old 2000-byte
window, which is why the registered whole-file scan matters for future markers).
README C05 is **not** flipped, as the build state and admission order require:

```
$ sed -n '34p' corpus/README.md
| C05 | Android packages (APK) | — | — | frontier |
```

## Retained rejected candidates — AGREE (both must stay rejected)

I re-ran the rejected-marker check myself rather than trusting the probe:

```
commonjs-destructured-require-edges.md  13371 bytes  marker_offset= 859  "admission-status: rejected — round-61 fresh falsify wave on ab58069"
evm-saved-interface-candidates.md       13249 bytes  marker_offset= 712  "admission-status: rejected — round-61 fresh falsify wave on ab58069"
```

- **commonjs** — the round-61 Q11 cause is still in the body: line 81-83 says
  "this entry's block carries those values" for "the v2 digests, edge spans or the
  unnamed edge", while the `## Reproduce` block prints no edge span, column or
  location field at all (`grep -n "span\|column\|line_start"` matches only lines
  81 and 208, both prose). The Q13 row (`:208`) also still credits the two JS
  verifiers "pass". Keeping the marker and the `Admission warning` block is the
  correct disposition; re-admission would have to be a new entry with the
  derivations, never a marker flip.
- **evm** — the refuted cross-lane citation is still present (`:105`
  `kasegi-shokunin/PROVINCE.md:25`; `:192` Q10 "pass"), and the r24-in-derivation
  Q11 failure the round-61 erratum names is not repaired in the body. Marker at
  byte 712.

Neither marker is inside the old `[:2000]` window, so the registered counter
repair cannot move `K_HELD_BACKED_STRICT` at base — consistent with
`claims.md` and with `measure-before.log`
(`K_HELD_BACKED=8/14`, `K_HELD_BACKED_STRICT=8/14`,
`STRICT_REJECT_WINDOW_SELFTEST=pass old_window_miss=True`). `HOLDS_OK_V3=no` in
the red-before log is the expected do-nothing result (C5 0/2 at base).

## Agreement with the lane's own gate so far

| lane decision | my verdict | reason |
|---|---|---|
| C1 entry left `candidate`, README C05 left `frontier` | **agree with the process**, **disagree with the entry's self-Q11 pass** | admission order step 1 forbids the flip before fresh decisions — correct; but the entry's own §Q-map marks Q11 `pass` on bytes that fail Q11 (F1), so the draft verdict cannot be carried into L1's adjudication unchanged |
| C2 verifier controls landed, frozen C5 mutant 2/2 attributed | **agree** (independently reproduced) | see below |
| Counter repair registered, not scored; counts unchanged | **agree** | markers at 859/712 confirm window-independence; selftest `pass` |
| Retained rejects kept rejected | **agree** | causes still in the bodies (above) |

C2 reproduction — I rebuilt the frozen mutation shape from
`reports/round-65/measure.py:266-274` (single regex match, delete the conjunct
plus its connecting `and`) on a fresh corpus copy per variant, ran
`--self-test` with `cwd` = that copy's parent:

```
verify_icon_languages.py control exit=0 last=[PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED]
verify_icon_languages.py c5  clause matches= 1 ; exit=1 last=[AssertionError: r47: forged receipt evidence accepted]
verify_multi_icon_states.py control exit=0 last=[PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED]
verify_multi_icon_states.py c5  clause matches= 1 ; exit=1 last=[AssertionError: r42: forged receipt evidence accepted]
```

Both kills are attributed by the frozen predicate (exit non-zero **and** last
line ends `forged receipt evidence accepted`) → `C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2`
reproduced independently. Controls present at the landed bytes:
`corpus/verify_icon_languages.py:157` and `corpus/verify_multi_icon_states.py:156`.
The transplanted IDs are real foreign IDs, not invented: `ev_6e055332…` is
present in `corpus/live/runs/round-42/` (producer-receipt.json, inspection.raw.json)
and `ev_8ed88983…` in `corpus/live/runs/round-47/`, matching the claims'
direction (languages ← round-42 ID, multi ← round-47 ID).

## Residual risk and verification gaps

1. **No measurement run.** My seat is read-only and the wave has no committed
   after-tree, so I did not run `reports/round-65/measure.py` over an archive and
   claim no after-state label. `K_HELD=9/14` / `K_ROW C05 status=held` remain
   unproduced by definition (README not flipped); when L1 flips C05 it must name
   only the new entry and land the flip in the same revision as the SCORECARD row.
2. **Single judgment.** This is one non-author opinion; the gate needs the named
   fresh-seat Q01–Q13 decisions, not this file substituting for them. My reject is
   on the entry as written, not on the fixture or on C05 as a ground.
3. **F1 is the only blocking item and costs one line.** If L1 edits entry line 41
   and re-runs the readout, F1 clears; F2 and F3 still need a decision (F2 a ruling
   on registry-row reuse, F3 a widened anchor range `239-253` in both the entry and
   `SOURCES.md:52`).
4. **Scope of my checks.** I verified the byte-level statements that the entry's
   own commands print and the S038 anchors it cites; I did not independently
   re-derive every AXML field by hand outside those commands, and I make no claim
   about AXML producers, install/signature validity, dex validity or the
   `inspect_android_package` provider — the entry fences those too.
