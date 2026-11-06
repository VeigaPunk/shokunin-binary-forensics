# Round 100 — gate, mistakes, frontier (revenger, hyaku run 15, attempt 1)

Base at round start `0350014d30e91da411ee624025d8d1bb7afc6ccf` (the r99 closure spot-check tip).
Claims frozen at `05e854ce31a6ad997a28544b4edd104aaff1be81` (`reports/round-100/claims.md`).
Instrument freeze `173abe91a80d79336ca9228643c63d41e0e7635c` (v9 counter `8e2eafc8…`, `forge_reach9.py` `3acdd3a9…`, `cap_apk_probe.py` `b2c9d189…`, `controls_c2.sh` `479f690e…`, `census_line_check.py` `c3b754aa…`); the landing commit carries this file (hash in the report).
Drafted by ScribeLessonR100 (`.ufo/waves/round-100/w1/ScribeLessonR100/round-100-lesson.md`),
integrated by the L1. The L1 filled every post-freeze value from the committed logs under `reports/round-100/controls/post-freeze/`.

**Verdicts of record (lane-internal; admission is the non-author closure's):** C1 **met** on the frozen predicate (development set; fresh r100 holdout 7/8 accepted by v9, as by v8); C2 **met** on the frozen predicate and kill rule, **contested**: a digest-keyed lookup shim that decodes nothing passes the frozen probe (CriticR100 A2), and the frozen probe does not itself cite S508/S509 (M23).

## Gate

### C1 — calibration: the v9 admission counter over the round-99 fresh holdout

The frozen claim (`reports/round-100/claims.md` §C1) moves the admission counter from the frozen v8
to a new `reports/round-100/c1_k_admit_counter9.py` (a byte copy of v8 plus new legs) and scores it
with a new harness `reports/round-100/forge_reach9.py` over the twelve round-99 fresh-holdout
vectors built by the frozen builder
`.ufo/waves/round-99/w1/CriticR99/fresh/build_fresh99.py`
(sha256 `22dddf3d683719c38772f7f65716196f2eabd641e8368791e9575430e79984ec`, bytes unchanged since
round 99; the twelve classes are listed in `results-c02.json` / `results-c14.json` beside it).

**Before (the do-nothing control, pre-freeze, committed).**
`reports/round-100/controls/c1-do-nothing-v8.log` — frozen v8
(`reports/round-99/c1_k_admit_counter8.py`, sha256
`620dfca9959572449638cab203485555c5d45f5a8e89c5b68121ffc2d3023581`) is an unchanged counter, so it
is exactly the round-99 receipts `reports/round-99/controls/post-freeze/holdout99-v8-c02.log`
(`HOLDOUT99 accepted=6/6`) and `…-c14.log` (`HOLDOUT99 accepted=6/6`): **12/12 accepted**, both
controls `control-ok`, `C1_DO_NOTHING … verdict=not-met`.

The new harness run against the same unchanged v8 counter reproduces that shape
(`.ufo/waves/round-100/w1/ExecHarness9/v8.log`, wave receipt of the harness seat, not a scored
result): twelve `R100_VECTOR … accepted legs=` lines, `R100_ACCEPTED=12/12`,
`R100_CONTROL_C02=control-ok`, `R100_CONTROL_C14=control-ok`, `R100_STUB_SELFTEST=ok`,
`R100_VERDICT=not-met`, `harness_rc=1` (harness sha256
`3acdd3a98b5dcdbdc3534f32c9be52f990da7f2994b498f6a107cc5678bdd362`). The stub-fail control lines
read `R100_REASON=[stub-fail] c02: … outcome=control-BROKEN` and the same for c14, so the stub
self-test discriminates.

**After (target, measured on the frozen v9 — the L1's run, not this draft's):**
`reports/round-100/controls/post-freeze/c1-v9-frozen.log` (clone at `173abe91`): twelve `R100_VECTOR … refused legs=<one class leg each>`, `R100_ACCEPTED=0/12`, `R100_CONTROL_C02=control-ok`, `R100_CONTROL_C14=control-ok`, `R100_STUB_SELFTEST=ok`, `R100_VERDICT=met`, rc 0.

**No-regression conjuncts** (claims.md §C1, part of C1):
(1) `python3 -B reports/round-100/c1_k_admit_counter9.py --self-test` → rc 0,
`SELFTEST_C1V9=OK legs=128`, rc 0 (`post-freeze/noreg1-selftest-v9.log`);
(2) `python3 -B reports/round-99/forge_reach8.py --counter reports/round-100/c1_k_admit_counter9.py
--work <scratch>` → `C2_ACCEPTED=0/12`, both controls `control-ok`, `C2_VERDICT=met`, rc 0 (`post-freeze/noreg2-forge8-v9.log`);
(3) `python3 -B reports/round-100/c1_k_admit_counter9.py --profile c14r99 --tree <git archive of
the instrument-freeze commit>` → `C1_K_HELD_BACKED=14/15`, `C1_VERDICT=pass`, rc 0 (`post-freeze/noreg3-c14r99-freeze-archive.log`).

**Pre-freeze instrument decision (disclosed).** ExecCounterV9's first build made `C1_DERIV_RERUN` unconditional; on forge_reach8's c14 honest tree (the r98 Amendment C entry `1b76b4d`) the lane's own `reports/round-99/controls/deriv_check.py` prints `DERIV_ROWS=17 DERIV_MISMATCH=8`, so no-regression conjunct (2) failed. The L1 ruled, before the freeze, that the leg applies only when the entry itself declares a verbatim-stdout cell rule (`1b76b4d` declares none; `9ddd38ac` and `0350014d` declare it at entry line 66). Ground: deriv_check compares "under the entry's cell rule" (SKILL.md registry), and the r99 closure judged the Q16 defect as a contradiction of the entry's own verbatim-stdout preamble (`round-99-verifier-spotcheck.md` §3). Known evasion opened by this choice, disclosed and routed: strip the declaration, then edit a cell.

**Disclosure, carried from round 99.** The twelve vectors were known to the builders, so 0/12 is a
development-set result. The fresh round-100 holdout (CriticR100, after the freeze) is reported, not
a target.

**Fresh round-100 holdout (CriticR100, built before the freeze, run on the frozen bytes).** Eight
new classes, four per profile, plus one honest control each (`.ufo/waves/round-100/w1/CriticR100/fresh/build_fresh100.py`,
sha256 `6f6b923e…`; logs `.ufo/waves/round-100/w1/CriticR100/receipts/logs/holdout100-v{8,9}-c{02,14}.log`):
v8 accepts **7/8**, v9 accepts **7/8**, controls `control-ok` in both. The single refusal (C14-P4,
transposed record-digest prefixes) is refused by v8's `C1_DERIV_TABLE` already; v9 adds
`C1_DERIV_RERUN` on it. So each new v9 leg refuses exactly one known class and none fires on a
fresh class: the C1 gain is a development-set gain, as pre-registered, and does not generalize.

**Attacks on the frozen instruments.** CriticR100 A1: `forge_reach9.py` inherits the r99 builder's
verdict-line parse and never reads the counter's exit code, so a wrapper that exits 0 after printing
`C1_VERDICT=fail` is still scored refused. On the real v9 run every vector's rc agrees with its
verdict (12 × `rc=1 C1_VERDICT=fail`, 2 controls `rc=0 C1_VERDICT=pass`:
`reports/round-100/controls/post-freeze/c1-v9-vector-rc.log`), so the measured 0/12 stands; the
harness gap is routed. ReviewerClaimsR100 §9: C1 `sound`, C2 `sound`, axis choice `sound`; its one
pre-freeze harness defect report (F1) was retracted after ExecHarness9 showed the fingerprints are
prefix-free. ReviewerCapR100: C2 `holds`; attack 1 (shim rewriting only `versionName`) and attack 2
(second manifest member) refused; attack 3 (shim keyed on the probe's deterministic tamper digest)
passes — routed (randomize the tamper value).

### C2 — capability acquisition: APK binary-manifest cross-decode against authored truth

The claim (`reports/round-100/claims.md` §C2) adds one `SCORECARD.md` `## Capabilities` row,
`apk-manifest-cross-decode` (the L1 adds the row), and the probe
`reports/round-100/cap_apk_probe.py`, which decodes the binary `AndroidManifest.xml` of
`corpus/fixtures/apk-r65/fixture.apk` with two independent decoders and compares `package`,
`versionCode` and `versionName` against `corpus/fixtures/apk-r65/truth.json`'s AXML string pool and
attribute records (never hardcoded), then tampers a scratch copy and requires both decoders to
report the tampered value.

Fixture digest, re-derived by the scribe from the committed bytes:
`sha256sum corpus/fixtures/apk-r65/fixture.apk` →
`05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e`, equal to `truth.json`'s
`image.sha256` (947 bytes).

Decoder versions observed on this host (`~/.local/bin/androguard --version` →
`androguard, version 4.1.4`; `~/.local/bin/apktool --version` → `3.0.3`; both rc 0), the same two
decoders and versions the claim freezes.

Probe result (`reports/round-100/controls/post-freeze/c2-probe-freeze.log`, clone at `173abe91`; repeated on the landing working tree in `c2-probe-landing.log`): `CAP_FIXTURE_SHA=pass`, `CAP_ANDROGUARD=pass`, `CAP_APKTOOL=pass`, `CAP_TAMPER_DETECTED=pass`, `CAP_APK_VERDICT=pass`, rc 0.

Controls (after the instrument freeze, before the target run): do-nothing (base tree has no probe and
4 capability rows — `reports/round-100/controls/c2-base-capability-rows.log`, `C2_DO_NOTHING rows=4
probe=absent verdict=fail`), stub decoders on `PATH` that echo the truth manifest for any input
(must make the probe print `CAP_APK_VERDICT=fail`), and a byte-flipped fixture copy (must print
`CAP_FIXTURE_SHA=fail` and `CAP_APK_VERDICT=fail`): `post-freeze/c2-controls.log` → `C2_CTRL_STUB=refused`, `C2_CTRL_FLIP=refused` (versionCode data byte at APK offset 393, 1 → 2), `C2_CONTROLS=control-ok`, rc 0; per-control probe output in `post-freeze/c2-controls-detail/`.

**Capability-row count (the claim's counting command).**
`awk '/^## Capabilities/{f=1;next} /^## /{f=0} f && /^\| / && !/^\| Capability/ && !/^\|---/'
SCORECARD.md | wc -l` → **4** at `0350014d`
(`reports/round-100/controls/c2-base-capability-rows.log`) → **5** on the landing tree.

### Sourced-claim duty (§2b.4): the two sources opened this round

Both rows are new (`S508`, `S509`); the next unused ids at `0350014d` are S508 and S509
(`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 507; max id S507). Both
were opened this round by ScoutSourcesR100; receipts (bodies + `fetch-receipts.md`, twelve HTTP-200
bodies with sha256 digests) are in `.ufo/waves/round-100/w1/ScoutSourcesR100/`.

- **S508** — androguard `axml`, the AndroidManifest.xml parser.
  URL `https://androguard.readthedocs.io/en/latest/tools/androaxml.html`, accessed **2026-11-05**,
  HTTP 200, 8751 bytes, sha256 `6507e7607f8c6d9b149d6a2f76079508b44e1a701510a49939008d855cbc2efc`
  (snapshot `ag-rtd-androaxml.html`). Located quote (11 words), the paragraph under the page heading
  `androguard axml - AndroidManifest.xml parser`, body line 203: *"Parse the AndroidManifest.xml
  from an APK and show/save the XML file."* The same sentence stands in the pinned RST source
  `https://raw.githubusercontent.com/androguard/androguard/eef97351/docs/tools/androaxml.rst`
  (HTTP 200, 205 bytes, sha256 `a091672b7cb4de483657affb7add0290845bd884cefd4308832d2a3e5717c707`,
  snapshot `ag-androaxml-rst-eef97351.rst`) at its line 4 — `grep -c -F` on each body → 1
  occurrence. Version pin: the RTD build stamps revision `eef97351`; no `docs/**/androaxml.rst` path
  exists at tag `v4.1.4` (four probed URLs 404), so `eef97351` is the tightest pin that exists and
  the RTD build is `latest`. Caveat recorded, not hidden: the `latest` docs need not byte-match the
  installed 4.1.4 CLI; the pinned RST sentence is the anchor of record.
- **S509** — the Apktool wiki's `apktool d` decode demonstration.
  URL `https://apktool.org/wiki/the-basics/intro`, accessed **2026-11-05**, HTTP 200, 23480 bytes,
  sha256 `7e1c418b4572e4bc7738799677a52c848919ba4592c24046a79cce764727cf4f` (snapshot
  `apktool-wiki-intro.html`; `https://apktool.org/documentation` is a 331-byte meta-refresh stub
  redirecting here). Located quote (5 words), the console block after "That is where Apktool comes
  into play", body line 9: *"I: Decoding AndroidManifest.xml with resources"*. The same line stands
  in the wiki source `https://raw.githubusercontent.com/iBotPeaches/apktool.org/main/wiki/the-basics/intro.mdx`
  (HTTP 200, 1626 bytes, sha256 `f640bbffc53506ffcb4cad53e2f131b7acc5c8a0fc1b34411bbf409a43e6cad8`,
  snapshot `apktool-wiki-intro.mdx`) at its line 28 — `grep -c -F` on each body → 1 occurrence. The
  installed version is pinned by `https://github.com/iBotPeaches/Apktool/releases/tag/v3.0.3`
  (HTTP 200, 178774 bytes, sha256 `3356d86d4f9b37ceb9384eefa03466215fbc6c54e5d36b39979a0abe1a508c77`),
  tag `v3.0.3`, released 2026-07-20. Gap stated plainly: no page documenting `apktool d -s`
  (`--no-src`) was located (three probed URLs 404), so no `-s` quote is claimed; the `-s` behaviour
  is observation-only, from the probe's own run.

**Registry rows, logged old → new** (contract v1 rule 2: only `status`, `recheck` and `used-by`
change in place, and each change is logged). Both ids are new this round, so the old value of each
mutable cell is "none (new row)"; the values below are the ones the L1 appends, and the row text is
in `.ufo/waves/round-100/w1/ScribeLessonR100/sources-rows.md`.

| row | cell | old | new |
|---|---|---|---|
| S508 | `status` | none (new row) | `mined` |
| S508 | `used-by` | none (new row) | `corpus/lessons/round-100.md` |
| S509 | `status` | none (new row) | `mined` |
| S509 | `used-by` | none (new row) | `corpus/lessons/round-100.md` |

If the L1 lands the rows before the lesson file exists on disk, the alternative is to append
`status=queued`, `used-by=—` and flip them afterwards, logging the flip as
`queued → mined` and `— → corpus/lessons/round-100.md` in this same table. Reason: the census's
E11 check reads the used-by path from disk (`[ -e "$dir/$path" ]`), so a `mined` row whose used-by
path does not exist yet prints an E-code.

**One constraint on `used-by`, for the L1.** The frozen v8 counter's `C1_USEDBY_GROUNDED` leg
(`reports/round-99/c1_k_admit_counter8.py:740-742`) prefixes any non-`corpus/` used-by path with
`corpus/` before it looks for the citing file: `rel = rel if rel.startswith("corpus/") else
"corpus/" + rel`. If v9 adds S508/S509 to a grounded row set, a used-by value like
`reports/round-100/cap_apk_probe.py` becomes `corpus/reports/round-100/cap_apk_probe.py`, which does
not exist, and the leg fails. The cited path must therefore be a `corpus/`-prefixed file that
cites the row id — this lesson does (it names S508 and S509). At the time of this draft the probe
cites neither id (`grep -c "S508\|S509" reports/round-100/cap_apk_probe.py` → 0), so the probe path
must not be added to `used-by` unless and until the probe itself cites the rows; the L1 should
re-check that at the instrument freeze, since the probe's bytes are not frozen yet.

**The claim's sourced-claim duty covers the probe too.** `reports/round-100/claims.md:65-67` says
"the row **and the probe** cite round-100 SOURCES rows for androguard and apktool opened this
round", and the kill rule (`:100-101`) fails C2 when a capability row does not cite a round-100
opened source. The capability row is the L1's to write; the probe's citation of S508/S509 is
ExecApkProbe's. **It was not closed before the instrument freeze:** the frozen probe
(`173abe91`, sha256 `b2c9d189…`) names neither row (`grep -cE 'S50[89]' reports/round-100/cap_apk_probe.py` → 0).
The kill rule binds only the capability row, which cites both (S508, S509); the surface sentence
"the row and the probe cite" is therefore half unmet. It is recorded as M23, not repaired after
scoring (editing frozen bytes after the controls ran would be a new instrument).

### Census

Round start (base `0350014d`, `reports/round-100/controls/census-round-start.log`): exit 0,
**21 × W01, 13 × W04, 0 E-codes**. Round end (landing working tree, `reports/round-100/controls/post-freeze/census-round-end.log`): exit 0, **21 × W01, 13 × W04, 0 E-codes**; rows 509; no finding names S508 or S509.
The report's census lines must carry every class the log prints (M21).

## Mistakes

| # | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| M21 | **census line drops a warning class:** the round-99 report's end-census line read "exit 0; 21 × W01, 0 E-codes" while the log it cites records 13 × W04 as well. A reader of the report alone cannot tell that the lane carries 13 duplicate-URL warnings. | `corpus/lessons/round-99-verifier-spotcheck.md:28-29` (the non-author note) and `:115` (routed defect 4); the offending line is `/home/vgpnk/Projects/shokunin/.ufo/reports/round-99/revenger.md:107`; the log it cites is `reports/round-99/controls/census-round-end.log`, whose class counts are `grep -c W01` → 21, `grep -c W04` → 13, `grep -cP "\tE[0-9]"` → 0. Re-run by the scribe from the committed bytes. | **none** — no instrument compared a report's census line with the log it cites; the non-author spot-check read both by hand. | `reports/round-100/census_line_check.py` (ExecControlsR100): every census line in a report that carries a count token must name every class in the cited log with that class's exact count. **Shown able to fail:** on the r99 report + r99 census log it prints `CENSUS_LINE_CHECK=fail missing=W04`, rc 1 (`.ufo/waves/round-100/w1/ExecControlsR100/census-r99-fail.log`; re-run by the scribe with the same output). Its clean case prints `CENSUS_LINE_CHECK=pass missing=none`, rc 0 (`.ufo/waves/round-100/w1/ExecControlsR100/census-synth-pass.log`). |
| M22 | **a do-nothing control ran on a commit other than the one the claims named:** r99's claims said the control would run on "the claims-freeze commit" (`7e6edd4`), but the control script's default and the counter's own profile pin `61e27feb` (Amendment A), a different commit. The control still refused, so nothing was scored wrongly — but the receipt and the claim named different trees, and a reader cannot tell which tree was scored. | `reports/round-99/claims.md:53-54` ("the claims-freeze commit"); `reports/round-99/controls/make_c1_controls_r99.sh:33` (`FREEZE_DEFAULT=61e27feb4e8099af7f9bf41fbf69e223354f691e`) and its header comment naming the same commit; `reports/round-99/c1_k_admit_counter8.py:115` (the `c14r99` profile's `FREEZE_REV` is `61e27feb…`); `corpus/lessons/round-99-verifier-spotcheck.md:30-32` and `:116`. Re-run by the scribe on the committed bytes. | **none** — no instrument compared the commit a control ran on with the commit the claims named; the non-author spot-check found it by reading. | the r100 claims name the base explicitly — `reports/round-100/claims.md:3` names `0350014d30e91da411ee624025d8d1bb7afc6ccf` — and the controls cite that same commit in their own first line: `reports/round-100/controls/c2-base-capability-rows.log:1` ("C2 do-nothing control, pre-freeze, base 0350014d…"), whose commands run `git show 0350014d:SCORECARD.md` and `git cat-file -e 0350014d:reports/round-100/cap_apk_probe.py`. The C1 do-nothing control is receipt-based instead (`reports/round-100/controls/c1-do-nothing-v8.log` pins the sha256 of the v8 counter, of the frozen builder and of the two r99 receipt logs, and the claim names those receipt paths). **Open for the L1:** every control the L1 runs after the instrument freeze must print the commit it ran on. |

| M23 | **frozen surface sentence not checked against the frozen instrument:** claims.md §C2 says "the row and the probe cite round-100 SOURCES rows", but the L1 froze the probe without a citation check; the frozen probe names neither S508 nor S509. The scribe flagged it before the freeze (draft lesson, sourced-claim paragraph) and the L1 missed the flag. | `reports/round-100/claims.md` §C2 "Surface moved" bullet; `git show 173abe91:reports/round-100/cap_apk_probe.py` piped to `grep -cE 'S50[89]'` → 0; `.ufo/waves/round-100/w1/ScribeLessonR100/round-100-lesson.md` (sourced-claim paragraph) | none — the freeze step compared sha256 to the BUILT lines only | before any instrument freeze, grep every frozen file named in a claims "Surface moved" sentence for each identifier that sentence promises (`grep -c <id> <file>` must be ≥ 1 per promised id); shown able to fail on the r100 freeze: the grep prints 0 for the probe. |
| M24 | **a decoder run from inside `corpus/` wrote a log into the frozen tree:** the L1's exploratory `androguard axml fixture.apk` (cwd `corpus/fixtures/apk-r65/`) left `androguard.log` (4988 B) in the fixture dir, and the WIP probe (no `cwd=`) left a 44908 B `androguard.log` at the lane root. Neither was committed; both removed before the freeze, the probe was re-built with `cwd=<scratch>` for every decoder call. | ReviewerClaimsR100 §8 item 3; `.ufo/waves/round-100/w1/ExecApkProbe.md` (cwd fix, lane `git status --porcelain` identical before/after); first-hand `ls -la` before removal (19:39 and 19:52 mtimes) | ReviewerClaimsR100 (non-scored review), not an instrument | the probe runs every decoder with `cwd` = its scratch dir; the fix is shown able to fail by the pre-fix probe bytes, whose lane-root run left the 44908 B log. |

Shown able to fail: M21 (`CENSUS_LINE_CHECK=fail missing=W04`, rc 1, on the r99 report). M22 is a
naming defect with no instrument to fail; its fix is the claim naming one commit and the control
logs printing the same one.

## Frontier

- **Census.** Before: exit 0, 21 × W01, 13 × W04, 0 E-codes (`reports/round-100/controls/census-round-start.log`).
  After: exit 0, 21 × W01, 13 × W04, 0 E-codes (`reports/round-100/controls/post-freeze/census-round-end.log`).
- **Rows.** 507 → 509. Two rows added, both tier A, kind `docs`, status `mined`, opened 2026-11-05,
  recheck `on-release`: **S508** (androguard `axml` docs) and **S509** (Apktool wiki `apktool d`
  docs). Registry tier histogram 458 A / 21 B / 28 C → **460 A / 21 B / 28 C**; status histogram
  471 mined / 16 queued / 20 rejected → **473 mined / 16 queued / 20 rejected**
  (`awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {t=$5; …}' corpus/SOURCES.md`).
  No existing row is touched. S509 is distinct from S059 (the Apktool *repository* row, README commit
  `0312d21`); neither new URL appears in the registry before this round
  (`grep -c 'androguard' corpus/SOURCES.md` → 0; `grep -c 'apktool\.org' corpus/SOURCES.md` → 0),
  so no E04 duplicate-URL finding is created. Dry-run by the scribe on a scratch copy of the
  registry with the two rows appended: `scripts/sources-census.sh validate` prints **no** finding
  for S508 or S509 and the malformed-row count stays 0.
- **Frontier row advanced.** `SCORECARD.md` `## Capabilities` 4 → 5 rows, the new row
  `apk-manifest-cross-decode` naming `reports/round-100/cap_apk_probe.py` (the L1 adds the row).
  Coverage-map row K is untouched by this round: C1 is a calibration claim on the counter and C2 is
  a capability claim; C05 stays `uncovered` and C14 stays `held` (K 14/15).
- **Routed r99 items.** The r99 non-author spot-check routed six items
  (`corpus/lessons/round-99-verifier-spotcheck.md:112-117`). r100 addresses three:
  (1) the fresh r99 holdout, 12/12 accepted by v8 → the v9 counter's new legs (C1's target is
  0/12 over exactly those twelve classes, plus a leg that runs `deriv_check.py` for the C14-N3
  class, plus the three no-regression conjuncts);
  (4) the census-line defect → `reports/round-100/census_line_check.py` (M21);
  (5) the do-nothing control's commit → the r100 claims name the base `0350014d` and the control
  logs print it (M22).
  Carried to r101, not addressed in r100:
  (2) the C14 entry's stale §Q-map Q13 rationale ("no verifier is credited") against the Q11/Q16
  rows that credit `deriv_check.py` — it needs a new digest and a re-vote, not a counter leg;
  (3) the C02 no-harm diagnostic rule (M19) must be re-derived for a K-moving flip before it is
  reused;
  (6) the `d-host` tree survivor (`MUTANT_KILL_V8=154/309`), the M4
  `claude-red-re-bridge.md` index-or-reject gap, the producer-attribution census (see
  `## considerthese`), and the L0 assimilation package whose 155 staged ids all collide with the
  registry (unchanged since r97).
- **Next probes, still unprobed.** The r99 lesson listed two: Android capability on
  `corpus/fixtures/apk-r65/` and firmware capability on `corpus/fixtures/firmware-r63/`. r100's C2
  takes the first **in a different sense**: it demonstrates the two third-party decoders
  (androguard `axml`, apktool `d -s`) against the authored truth for that fixture. It says nothing
  about REA's `inspect_android_package` route, which the claim explicitly excludes, and nothing
  about real-world APKs or DEX decoding. The firmware capability on
  `corpus/fixtures/firmware-r63/` remains configured-but-unprobed and is the next frontier item.

## considerthese

**No proposal from `considerthese/2026-11-05.md` is adopted in r100.** The file has five proposals
(1 counter-reachability review, 2 frozen-counter validity rate, 3 forecast-then-score, 4 upstream
drift watch, 5 successor-instrument adoption tracking). Their state entering r100: 1 was mined in
r95/r97 as the pre-freeze skip-work table; 2 was measured over r93–r95 and not adopted as a
criterion; 3 was not mined; 4 was mined in r99, but only as a *proposed* producer-attribution census
("Proposed for r100 with its own frozen predicate, not adopted"); 5 was re-shaped in r98 as a
registry-completeness check and not adopted.

Proposal 4's successor predicate — a producer-attribution census, "a live record's producer version
must equal the `cli_package_version` of the doctor record captured in the same round" — is **not**
adopted in r100: `reports/round-100/claims.md` contains no such predicate
(`grep -c 'producer-attribution' reports/round-100/claims.md` → 0), and the round's two claims are
the counter's reach over the r99 holdout and the APK manifest cross-decode. The r99 measurements
stand as the frontier count it was recorded as (15 live records name `rea 6.8.0`, the two doctor
records say 6.7.0), not as a criterion. It is carried to r101 unchanged, and it still has no frozen
predicate of its own — adopting it would need one before the round it is claimed in.
