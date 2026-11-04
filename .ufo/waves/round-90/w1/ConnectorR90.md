# ConnectorR90: sibling-overlap scan and proposal mapping (round 90, w1)

Seat ConnectorR90 (connector, leaf). The scan read sibling lanes only; probes ran in `/fast/scratch/hyaku/revenger-r90/ConnectorR90` with TMPDIR set to that dir. Frozen claims read first: `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-90/claims.md` (freeze `c7767789fe9e96bcc0d50656ad4bdce69ba3a3a9`). Lane HEAD at probe time: `5bdcd5a628c4063dabf0dc3858ecd41df46d1760`. No tools were installed or upgraded. No lane byte outside this file and `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-90/w1/ConnectorR90/` was written.

Axes judged: **calibration** (C1, SM6) and **coverage** (C2, android record under the v2 oracle plus norm-eq).

## Method

- Scope: the 20 sibling lanes `/home/vgpnk/Projects/shokunin/*-shokunin`, excluding `revenger-shokunin`. Skipped directories: `.git`, `.jj`, `node_modules`, `.venv`, `__pycache__`, `.scratch`, `.cache`, `target`, `dist`, `build`, `.godot`, `Library`.
- Pass 1 (code): every `*.py|*.sh|*.mjs|*.js|*.ts|*.jq` file, including `.ufo/` and gitignored files, searched with these regexes:
  - android: `AndroidManifest|manifest-element|versionCode`
  - xmletree: `xml\.etree`
  - selfassess: `self_assessment|K_HELD_BACKED`
  - denominator: `denominator` (case-insensitive)
- Hit counts per class (files):
  - android: 1
  - xml.etree: 1024. Almost all are kake/kagi wave-control copies; 9 lie outside `.ufo`.
  - self_assessment or K_HELD_BACKED: 9
  - denominator: 813. Most are vendored three/cannon copies under game-dev-3d `corpus/live/runs/*/scratch`.
- Pass 2 (prose):
  - Every non-`.ufo` `SOURCES*.md` file (31 of them) was searched for `ElementTree|xml.etree|pyexpat|manifest-element|guide/topics/manifest|AndroidManifest|versionCode|TreeBuilder|insert_comments`. **0 hits.**
  - Sibling `corpus/**/*.md` and top-level `*.md` were searched for ElementTree/defusedxml.
  - kaidoku `corpus/`, `PROVINCE.md` and `SCORECARD.md` were searched for the android producer verbs.
- `K_HELD_BACKED` has **0 hits in any sibling lane**. It does hit at the fleet root (`/home/vgpnk/Projects/shokunin/MANIFEST.json`, `/home/vgpnk/Projects/shokunin/.ufo/reports/round-*/revenger.md`), but those are revenger's own closures, so they were not counted as sibling overlap.

## Overlap table

Classes used below:
- **duplicate**: the same instrument or claim already exists in a sibling.
- **complementary**: a different lane holds the same defect class, prior art, or a hardening this round should cite.
- **unrelated**: the terms match but the subject differs.

| # | Sibling file:line | What it holds | Round-90 surface touched | Class | Action |
|---|---|---|---|---|---|
| 1 | `/home/vgpnk/Projects/shokunin/kaidoku-shokunin/corpus/knowledge/2026-10-13-r4u-02-jadx-decode.md:137-156` (Candidate 5; last commit `b04b19e53aa105cdce8755511394e30f0a5de9ac`) | Measured on a real Godot APK on 2026-10-13. jadx `inspect-android-package` mints a fresh `evidence_id` on every run, `raw_result` embeds the mkdtemp staging path `/tmp/rea-android-{kuhLd2,xEWTq8,bRe4fH}` and `load_duration_ms`, and `normalized_result` is byte-identical across runs. Its words: "expect dedup-by-evidence-id to fail for this provider family". | C2: `reports/round-90/norm_eq.py:10-15` volatile items V1 (evidence_id), V2 (`/rea-android-<suffix>`) and V4 (`load_duration_ms`), plus K6 (distinct ids) | **complementary prior art** (three of the four frozen volatile items were independently observed 3 weeks earlier; V3, JVM key order inside text payloads, is revenger-only) | **cite.** The lane has 0 citations: a grep for `r4u-02|jadx-decode|kaidoku` over `corpus/SOURCES.md`, `reports/round-89`, `reports/round-90`, `corpus/lessons/round-89.md` and `round-90.md` found nothing. r89's byte-identity kill rediscovered a known sibling fact. |
| 2 | `/home/vgpnk/Projects/shokunin/kaidoku-shokunin/PROVINCE.md:58,136`; `/home/vgpnk/Projects/shokunin/kaidoku-shokunin/corpus/README.md:29` | `inspect-android-package` held on a 127 MB, 13-dex real APK with `REA_JADX_MCP_JAR` (jadx-headless-mcp 0.7.1, sha `6e5eacf5…`). Records have no oracle. | C2 producer path and considerthese proposal 2 (fixture realism) | complementary (real-APK breadth there vs. oracle-checked depth over a 1-member authored fixture here) | cite as the realism gap: the apk-r65 fixture cannot exercise multi-dex, `uses-sdk`, permissions or debuggable. |
| 3 | `/home/vgpnk/Projects/shokunin/kaidoku-shokunin/corpus/knowledge/2026-10-13-r3-apk-inventory.md:93-110` | Typed refusal `capability_unavailable` / `unsupported_provider` / provider `jadx` when `REA_JADX_MCP_JAR` is unset | considerthese carry-forward "F-android (`REA_JADX_MCP_JAR`, `jadx`)" | complementary | none needed (context only) |
| 4 | `/home/vgpnk/Projects/shokunin/kake-shokunin/scripts/sitemap_audit.py:424-438` (`_has_doctype`: expat `ParserCreate`, `StartDoctypeDeclHandler`, `XML_PARAM_ENTITY_PARSING_NEVER`), `:523-525` (doctype gate runs before the root gate), `:529` (`ElementTree.fromstring`), `:543-552` (exact root-tag dispatch); `/home/vgpnk/Projects/shokunin/kake-shokunin/corpus/lessons/round-39-verifier-spotcheck.md:100-102` ("refuses any DOCTYPE through an expat prescan *before* `ElementTree` parses (so no internal-entity expansion reaches the parser)") | A parser-grounded DOCTYPE refusal in front of an ElementTree root-identity reader, adjudicated by a non-author verifier in kake r39 | C2 oracle: v2 `corpus/fixtures/apk-r65/oracle_check2.py` has no DOCTYPE leg; the unclaimed v3 `corpus/fixtures/apk-r65/oracle_check3.py:152-154` refuses on the substring `"<!doctype" not in text.lower()` | **complementary, should cite** (sibling precedent for the v3 DOCTYPE leg; a parser-grounded form avoids v3's substring false-red, see probes P2) | cite in the v3 lesson or Gate; proposal below |
| 5 | `/home/vgpnk/Projects/shokunin/kake-shokunin/SCORECARD.md:2398` | kake priced an "ElementTree root-only reader" as a *control* (scores 5/24) | C2: v2 is itself a root-attribute ElementTree reader | complementary (method: a root-only reader is a named control class there) | optional cite |
| 6 | `/home/vgpnk/Projects/shokunin/kaidoku-shokunin/tools/round-65/coverage-recipe.py:4-14,28-34`; `/home/vgpnk/Projects/shokunin/kaidoku-shokunin/tools/round-66/coverage-selfcheck.py:4-33` | The same defect class as SM6. A self-assessment fraction whose numerator **and** denominator come from one filter silently drops population ("the recipe still prints a perfect score"; 142 of 144 files assessed). The repair adds a `population_dropped` leg and re-derives the cited `<mapped>/<files>` atom. | C1: `corpus/self_assessment_check2.py:183-186` (N and D both from the one regex `^\| C[0-9]+ `) | **complementary, should cite.** Not a duplicate: different lane and map. SM6 v2 carries the exact r65 hazard, demonstrated in probe P3. | cite plus the proposal below |
| 7 | `/home/vgpnk/Projects/shokunin/kengaku-shokunin/plans/round75_c1_index_parity.py:11-17` | Index-parity counter written because scorecards "kept claiming index parity for the narrower denominators it happened to count" | C1 (denominator drift) | complementary (same class, different atom) | optional cite |
| 8 | `/home/vgpnk/Projects/shokunin/mado-shokunin/.ufo/waves/round-23/c3/count.py:1-21,71` | A SHONEN box-4 self-assessment vs repo-state counter (PROVINCE tool rows) | C1 genre (self-assessment mismatch gate) | complementary genre, different atom; wave-local | none |
| 9 | `/home/vgpnk/Projects/shokunin/souji-shokunin/.ufo/waves/round-44/w1/S44reviewer61/audit.py:34` (mirrored at `/home/vgpnk/Projects/shokunin/souji-shokunin/census/round-44/waves/w1/S44reviewer61/audit.py:34`) | A `remaining_new_self_assessment_mismatches_under_Q76` tally | C1 genre | unrelated to SM6 (wave-local audit) | none |
| 10 | `/home/vgpnk/Projects/shokunin/kengaku-shokunin/plans/round52_c2_registry.py:44,106,137`; `/home/vgpnk/Projects/shokunin/kengaku-shokunin/plans/round74_c1_registry.py:12,56,148,177` | `self_assessment_files()`: a Gate-registry advertising scan | name collision only | unrelated | none |
| 11 | `/home/vgpnk/Projects/shokunin/kagi-shokunin/.ufo/waves/round-31/build/ConnOverlap.md:96` | Lists revenger `corpus/self_assessment_check.py` among sibling gates that read a SCORECARD | C1 (inbound reference to v1) | unrelated (inbound citation; no duplicate instrument) | none |
| 12 | `/home/vgpnk/Projects/shokunin/chousa-shokunin/tools/capture-text.py:72`; `/home/vgpnk/Projects/shokunin/chousa-shokunin/corpus/evidence/round56/battery/oracle-m8-unpinned.py:72`; `/home/vgpnk/Projects/shokunin/chousa-shokunin/corpus/evidence/round5{2,3,4}/build-spans.py:53-54` | ElementTree over OOXML (DOCX) text | — | unrelated | none |
| 13 | `/home/vgpnk/Projects/shokunin/kagi-shokunin/corpus/release-clock.py:21`; `/home/vgpnk/Projects/shokunin/kengaku-shokunin/plans/round66_c1_tensor_probe.py:53`, `/home/vgpnk/Projects/shokunin/kengaku-shokunin/plans/round67_c1_pipeline_probe.py:60` | ElementTree over release feeds / junit XML | — | unrelated | none |
| 14 | `/home/vgpnk/Projects/shokunin/kaidoku-shokunin/.ufo/waves/round-22/gen-wave1.py:47,201,238` | `versionCode` inside F-Droid APK URLs in a wave spec | — | unrelated | none |
| 15 | 31 sibling `SOURCES*.md` (non-`.ufo`) | no row for the Android `<manifest>` reference or the Python ElementTree docs | revenger S483/S484 (`corpus/SOURCES.md:500-501`) | **not duplicated** (S483/S484 are fleet-first) | none |

**Duplicates: 0.** No sibling holds an Android manifest oracle, an XML-parsing identity oracle over a producer record, or an `N/D` self-assessment denominator check over a coverage map.

Three overlaps are complementary and **should be cited** (#1, #4, #6):
- kaidoku r4u-02 is prior art for norm-eq V1/V2/V4.
- kake `_has_doctype` is precedent for the v3 DOCTYPE leg.
- kaidoku r65/r66 covers the denominator/population-drop class that SM6 v2 still carries.

## Probes (scratch, read-only against the lane; receipts copied)

Receipts are in `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-90/w1/ConnectorR90/receipts/`.

Environment and pins:
- Python 3.14.8, expat 2.9.0.
- `oracle_check2.py` sha256 `de2b2ad2…e666d`; `oracle_check3.py` sha256 `88d49c91…d089`; `self_assessment_check2.py` sha256 `0e73a90b…0227`.

**P1 — DTD cases vs v1/v2/v3** (`doctype_probe.py`, `doctype-probe.log`):

| Case | v1 | v2 | v3 |
|---|---|---|---|
| D1: ATTLIST default supplies `package`, no literal attribute | OK 19/19 | OK 22/22 | FAIL |
| D2: internal entity `&p;` gives the true package | OK | OK | FAIL |
| D3: ATTLIST default supplies `versionCode`, no literal attribute | **FAIL 18/19** | **OK 22/22** | FAIL |

- D3 is a monotonicity break: **v2 accepts a record that v1 rejects.**
- This duplicates (independently) ForgeryR90Probe N03/N04, already recorded at `corpus/lessons/round-90.md:34,62` and in `reports/round-90/oracle2-vs-forgery-probe.log`.
- New here: the v1 → v2 direction on D3.
- The frozen 9-case battery (`reports/round-90/oracle_battery.py`) has no DTD case, so `ORACLE_MISCLASS=0/9` for v2 is unaffected.

**P2 — v3 substring false-red** (`fr_probe.py`, `falsered-probe.log`):

| Case | v2 | v3 |
|---|---|---|
| FR0: the real r89 record, unchanged | OK 22/22 | OK 25/25 |
| FR1: the real record plus a comment `<!-- no <!DOCTYPE here -->` (the parser skips comments; no DTD exists) | OK | **FAIL 24/25** |

- v3's DOCTYPE leg reintroduces the substring-leg class that killed v1, here in the over-reject direction.
- A parser-grounded check (kake `sitemap_audit.py:424-438`) would accept FR1 and still reject D1–D3.

**P3 — SM6 v2 population drop** (`sm6-population-drop.log`, `tree16-readme-rows.txt`):
- TREE is `git archive HEAD corpus SHONEN.md SCORECARD.md SKILL.md`.

| Tree | rows matching `^\| C[0-9]+ ` | rows matching `^\|\s*C[0-9]+\s*\|` | SM6 | SELF_MISMATCH |
|---|---|---|---|---|
| base | 15 | 15 | 0 | 0 |
| plus a 16th row written `\|C16 \| … \| uncovered \|` | 15 | **16** | **0** | 0 |
| plus a well-formed 16th row `\| C16 \| … \|` (control) | 16 | 16 | 1 | 1 |

- SM6 v2 cannot see a map row whose first cell lacks the leading space. The stale `8/15` statement then reads true: this is kaidoku r65's `population_dropped` hazard (#6).
- This is outside the frozen battery: B01–B12, R1 and R2 all use well-formed rows. So `SM6_MISCLASS` over the battery is unaffected, and **C1 is not falsified by this**.

## Proposal mapping — `/home/vgpnk/Projects/shokunin/revenger-shokunin/considerthese/2026-11-04.md`

| Proposal (line) | Implemented by round 90? | Evidence |
|---|---|---|
| 1. Own-work vs external ratio per window (:33) | **No** (no ratio report). Partially *served*: round 90's rows S482–S487 are 3 docs (S483, S484, S485), 1 community (S487) and 2 own-work (S482, S486), so external rows are non-zero this window. | `corpus/SOURCES.md:499-504` |
| 2. Fixture-realism gap list (:34) | **No.** C2 deepens the tiny-fixture pattern: one more oracle-checked record over the authored apk-r65 fixture. kaidoku #2 (real 13-dex Godot APK) is the ready external comparison for the android row of such a list. | `claims.md:54-60,86-89`; kaidoku `PROVINCE.md:58` |
| 3. Verify novelty claims on João's curated notes (:35) | **No / unrelated.** | — |
| 4. Message-vs-tree check on window commits (:36) | **No.** Adjacent only: C2's K5 (receipt stdout digests equal the run files) checks receipt vs file, not commit message vs tree. | `claims.md:72-73` |
| 5. Catch-up reflection file (:37) | **No / unrelated** (bot's own gap). | — |
| Carry-forward: F-android operator-blocked (`REA_JADX_MCP_JAR`, jadx) (:42) | **Yes, addressed.** C2 is the android family's first current-producer record (F4 10/11 → 11/11), with provider `jadx` (`oracle_check2.py` "provider id jadx" leg). | `claims.md:54-57` |
| Carry-forward: K L0 r74 operator-blocked (:42) | Acknowledged, not moved (`claims.md:19-22`). C1 changes the *gate's verdict fidelity* about K, not K. | `claims.md:51-52` |

## Proposed move (one, bounded; propose only, nothing edited)

**Population-guard synthesis for the next SM6 revision (calibration; harms no axis).**

The proposal:
- In a *new* frozen revision (v2 stays byte-unchanged), add a `population_dropped` leg modelled on kaidoku `tools/round-65/coverage-recipe.py:28-34`.
- It counts README lines matching the loose form `^\|\s*C[0-9]+\s*\|` that the strict `^\| C[0-9]+ ` regex misses.
- SM6 is then a mismatch iff the N/D statement is wrong **or** `population_dropped > 0`.
- Freeze before scoring, with the P3 `tree16` case pre-labelled `1` as a new battery case and the base tree as `0`.

Cite:
- kaidoku r65/r66 (#6) as the precedent for the defect class.
- On the C2 side of the same "filter defines the population" shape: kake `sitemap_audit.py:424-438` (#4) for the parser-grounded DOCTYPE leg that should replace `oracle_check3.py:152-154`'s substring test (P2), and kaidoku r4u-02 (#1) as independent prior art for norm-eq V1/V2/V4.

Affected axes:
- Calibration: SM6 can no longer be blinded by row formatting; the v3 DOCTYPE leg loses a false-red.
- Coverage: unchanged.
- Harm: none. SM1–SM5 are untouched, and the base tree stays `SM6=0` (P3 row 1).

Risks:
- The loose regex may also match a non-map table elsewhere in README that starts with `| C<n>`. The leg must be scoped to the `## Coverage map` section, as kaidoku scopes its map tokens (`coverage-recipe.py:22-26`).
- Any v3 battery addition must be labelled before scoring, unlike `oracle_check3.py`, which the lesson marks "fitted, not held out" (`corpus/lessons/round-90.md:62`).

Verification:
- `python3 -B reports/round-90/sm6_battery.py --impl <v3> --real TREE` must keep 0/14 on the frozen battery.
- The new tree16 case must score `SM6=1`, and the base TREE `SM6=0`.
- For the oracle: FR0/FR1 accept, D1–D3 reject, and the frozen 9-case battery stays 0/9.

## Contradictions stated, not smoothed

- `oracle_check2.py`'s docstring says it checks "the ROOT element" attributes. D1 and D3 show that attributes absent from the root element's literal text are accepted when a DTD defaults them (P1). The content-accuracy label in `claims.md:86-89` arguably admits D1/D2, which are true after XML processing. Read that way it is not a misjudgement under the frozen labels, but it is a v1 → v2 regression on D3.
- v3 fixes D1–D3 with a substring test, which is the same leg class the round killed v1 for (`claims.md:58-59`), now over-rejecting (P2).

VERDICT: no sibling duplicates; three complementary overlaps should be cited (kaidoku r4u-02 jadx per-run ids → norm-eq V1/V2/V4; kake `_has_doctype` → v3 DOCTYPE leg; kaidoku r65/r66 population drop → SM6, demonstrated blind to a malformed 16th row); of the considerthese 2026-11-04 items, round 90 implements only the F-android carry-forward.
