DRAFT-READY — the README index repair zeroes SM1 (1→0) and SM2 (4→0) on the frozen base tree with index-line changes only, and every added line is shown load-bearing (deleting any one of them re-raises SM2 to 1). No lane file was edited; the proof runs on `git archive 3f5edbc` copies in `/tmp/revenger-r70-R70W1ReadmeIndex` (deleted before return).

## 1. Target identity (frozen)

| object | sha256 |
|---|---|
| `corpus/README.md` at `3f5edbc206351232a3d2d801334dd930499ccaf5` | `70a5d7c510239337bb76b355e2e64e4c2e0c5a4c91371c2149fc638b113c6752` |
| `corpus/README.md` at `aa1842fac199aa524930e5565ed3715de5f84c6d` (C05 v5 candidate commit) | `70a5d7c510239337bb76b355e2e64e4c2e0c5a4c91371c2149fc638b113c6752` (identical — the candidate commit does not touch the index) |
| `corpus/self_assessment_check.py` committed at `aa1842f` | `6a24baa158ec168e3d4315d91c8a9e35481976c065bb8323b5a61f4b665c90fb` |
| `corpus/self_assessment_check.py` in the lane **working tree** (modified by a sibling while I ran) | `ae1c62aa9879f9de426beb20a09dbf2973ec841a501d364cb3e83eb119bbe282` |

My measurements are identical under both checker revisions (both rows reproduced below), so the draft does not depend on the in-flight checker edit.

## 2. Reproduction of the before state (SM1=1, SM2=4)

```
$ git -C <lane> archive 3f5edbc corpus SHONEN.md SCORECARD.md SKILL.md | tar -x -C /tmp/revenger-r70-R70W1ReadmeIndex/base
$ python3 -B <lane>/corpus/self_assessment_check.py --root /tmp/revenger-r70-R70W1ReadmeIndex/base --lane <lane>
SM1=1
SM2=4
SM3=2
SM4=1
SM5=1
SM6=0
SELF_MISMATCH=9          (exit 1)
```

Same numbers with the committed checker bytes (`/tmp/.../committed/self_assessment_check.py`, sha256 `6a24baa1…`): `SM1=1 SM2=4 … SELF_MISMATCH=9`. This matches the pre-registered `SELF_MISMATCH=9` (`reports/round-70/before-treated-tools-on-base.log`).

Located causes:

- **SM1** — `corpus/README.md:9` says `` `QUALITY.md` — admission criteria Q01–Q13 `` while the criteria table runs to `Q15` (`corpus/QUALITY.md:27`: `| Q15 | A stated git object id or tree identity is re-derived …`; max id parsed from `^\| Q(\d+) \|` = 15). Checker regex: `self_assessment_check.py:57` `re.search(r"`QUALITY\.md` — admission criteria Q01[–-]Q(\d+)", readme)`.
- **SM2** — base archive top level (`ls /tmp/.../base/corpus`): `check_embedded_outputs.py`, `derive_axml_anchors.py`, `q15_tree_id_check.py` and `snapshots/` are the four items that appear nowhere in the base README; `verify_*.py` is covered by the literal glob on `corpus/README.md:17`; `fixtures/`, `knowledge/`, `lessons/`, `live/` are covered (`live/` by `live/runs/`). Checker: `self_assessment_check.py:62-72`.

## 3. The draft (unified diff against `3f5edbc:corpus/README.md`, lines 7-17 block)

Four independent hunks; the C2 hunk is the deliverable of this seat, the other three are labelled per the frozen per-claim ownership.

### Hunk C2 (this seat) — Q-range + the four old names + the checker's own name

```diff
--- a/corpus/README.md
+++ b/corpus/README.md
@@ -6,15 +6,20 @@
 
 ## Index
 
-- `QUALITY.md` — admission criteria Q01–Q13 (Q11 supersedes Q08), each citing its mistake class.
+- `QUALITY.md` — admission criteria Q01–Q15 (Q11 supersedes Q08), each citing its mistake class.
 - `SOURCES.md` — where the lane learns: tiered, opened sources with study paths and search log (contract v1).
 - `knowledge/` — admitted domain entries (the map below names each one); also
   retains clearly marked rejected candidates (each carries an
   `admission-status: rejected` header), which are evidence, not admitted knowledge.
 - `lessons/` — `2026-10-12-r1-provider-gap.md`; `round-1.md` (fleet round-1 gates and the mined `## Mistakes` table); `round-1-verifier-spotcheck.md` (integrator-written outside check of round 1); `round-61.md` (round-61 gate, mistakes and source changes).
 - `fixtures/` — authored known-truth inputs (byte-oracle fixtures; `fixtures/REPLAY.md`).
+- `snapshots/` — pinned spec bytes the entries and derivations search (`ResourceTypes.h`, `dex-format.html`, `APPNOTE.TXT`, `rea-android-applications.md`), so an anchor resolves against committed bytes, not the network.
 - `live/runs/` — saved REA outputs, receipts and non-author reviews per historical round.
 - `verify_*.py` — saved-ledger replay verifiers (`--self-test`); census command in `SCORECARD.md` (C).
+- `check_embedded_outputs.py` — embedded-output gate (C7): re-runs an entry's declared derivation and counts quoted-output drift; the pinned historical-script rule is read from `embedded_output_pins.json`.
+- `derive_axml_anchors.py` — current AXML anchor derivation: prints the `ResourceTypes.h` line numbers and enum values an entry cites, from the pinned snapshot.
+- `q15_tree_id_check.py` — Q15 tree-identity checker: verifies every `tree-identity restatement:` pair a lesson states with `git rev-parse <hex>:corpus`, and requires at least one quoted false-sentence pair to fail.
+- `self_assessment_check.py` — SM1–SM6 mismatch counter over this index, `SHONEN.md` and `SCORECARD.md`; registered gate.
 
 ## Coverage map
 
```

### Hunk C1 (owner: C1) — `lint_entry.py`, `entry_checks.py`

```diff
@@ -15,6 +15,8 @@
 - `fixtures/` — authored known-truth inputs (byte-oracle fixtures; `fixtures/REPLAY.md`).
 - `live/runs/` — saved REA outputs, receipts and non-author reviews per historical round.
 - `verify_*.py` — saved-ledger replay verifiers (`--self-test`); census command in `SCORECARD.md` (C).
+- `lint_entry.py` — mechanical entry pre-flight: Q14 hex/count, §Q-map completeness, Q15 object ids, header trio.
+- `fixtures/apk-r65/entry_checks.py` — the C05 entry's own derivations (`--pins`, `--eocd`, …), so every value the entry states re-derives from the fixture bundle.
 
 ## Coverage map
```

### Hunk C3 (owner: C3) — `derive_axml_anchors_r68.py`, `embedded_output_pins.json`

```diff
@@ -15,6 +15,8 @@
 - `fixtures/` — authored known-truth inputs (byte-oracle fixtures; `fixtures/REPLAY.md`).
 - `live/runs/` — saved REA outputs, receipts and non-author reviews per historical round.
 - `verify_*.py` — saved-ledger replay verifiers (`--self-test`); census command in `SCORECARD.md` (C).
+- `derive_axml_anchors_r68.py` — the round-68 revision of the anchor script, digest-pinned for the round-68 entry (the S046 row's digest).
+- `embedded_output_pins.json` — entry → pinned-script map the gate reads, each pinned script sha256-verified before use.
 
 ## Coverage map
```

Landing note: the C1/C3 hunks are anchored on the base context (`verify_*.py` + blank + `## Coverage map`). Landed after C2 they insert at the same place but their context lines have shifted by the C2 block; only the anchor moves, no line content conflicts. The composed file (all four hunks) is section 4.

## 4. Composed final index block (all hunks, `README.md:7-26`)

```
 7  ## Index
 8
 9  - `QUALITY.md` — admission criteria Q01–Q15 (Q11 supersedes Q08), each citing its mistake class.
10  - `SOURCES.md` — where the lane learns: tiered, opened sources with study paths and search log (contract v1).
11  - `knowledge/` — admitted domain entries (the map below names each one); also
12    retains clearly marked rejected candidates (each carries an
13    `admission-status: rejected` header), which are evidence, not admitted knowledge.
14  - `lessons/` — `2026-10-12-r1-provider-gap.md`; `round-1.md` (fleet round-1 gates and the mined `## Mistakes` table); `round-1-verifier-spotcheck.md` (integrator-written outside check of round 1); `round-61.md` (round-61 gate, mistakes and source changes).
15  - `fixtures/` — authored known-truth inputs (byte-oracle fixtures; `fixtures/REPLAY.md`).
16  - `snapshots/` — pinned spec bytes the entries and derivations search (`ResourceTypes.h`, `dex-format.html`, `APPNOTE.TXT`, `rea-android-applications.md`), so an anchor resolves against committed bytes, not the network.
17  - `live/runs/` — saved REA outputs, receipts and non-author reviews per historical round.
18  - `verify_*.py` — saved-ledger replay verifiers (`--self-test`); census command in `SCORECARD.md` (C).
19  - `check_embedded_outputs.py` — embedded-output gate (C7): re-runs an entry's declared derivation and counts quoted-output drift; the pinned historical-script rule is read from `embedded_output_pins.json`.
20  - `derive_axml_anchors.py` — current AXML anchor derivation: prints the `ResourceTypes.h` line numbers and enum values an entry cites, from the pinned snapshot.
21  - `q15_tree_id_check.py` — Q15 tree-identity checker: verifies every `tree-identity restatement:` pair a lesson states with `git rev-parse <hex>:corpus`, and requires at least one quoted false-sentence pair to fail.
22  - `derive_axml_anchors_r68.py` — the round-68 revision of the anchor script, digest-pinned for the round-68 entry (the S046 row's digest).
23  - `embedded_output_pins.json` — entry → pinned-script map the gate reads, each pinned script sha256-verified before use.
24  - `lint_entry.py` — mechanical entry pre-flight: Q14 hex/count, §Q-map completeness, Q15 object ids, header trio.
25  - `fixtures/apk-r65/entry_checks.py` — the C05 entry's own derivations (`--pins`, `--eocd`, …), so every value the entry states re-derives from the fixture bundle.
26  - `self_assessment_check.py` — SM1–SM6 mismatch counter over this index, `SHONEN.md` and `SCORECARD.md`; registered gate.
```

Composed file sha256: `96818a2d5e816b8188699ad833bdf4e83f15e172a12ace38bc531f41afe750d8` (scratch path `/tmp/revenger-r70-R70W1ReadmeIndex/full/corpus/README.md`). Rows untouched: `grep -cE '^\| C[0-9]+ ' …/full/corpus/README.md` → `14` (`README_ROWS=14` holds) and `corpus/README.md:43` still ends the C05 row `| … | uncovered |` (diff above touches no `| C..` line, so `K_HELD_BACKED` and `C05_STATUS` are unaffected).

Prose in every added line is grounded in the bytes it names: `check_embedded_outputs.py:1-12` (gate, C7, reads the pin file), `corpus/embedded_output_pins.json` (entry→script map with `sha256`), `derive_axml_anchors.py:14-15` ("each cited enum's value"), `q15_tree_id_check.py:9-14` (`tree-identity restatement:`/`false-sentence:` pairs verified with `git rev-parse`, `--scan <lesson.md>`; the only such lines in the lane are `corpus/lessons/round-69.md:228,230`), `lint_entry.py:1-8` (the four lint classes, "pre-flight"), `fixtures/apk-r65/entry_checks.py:1-10` (`--pins`, `--eocd`), `SKILL.md:290` (`self_assessment_check` is a registered gate — so the word "gate" is used only for it and for `check_embedded_outputs`; `lint_entry` is deliberately called a pre-flight, matching `SKILL.md:301` and its own docstring).

## 5. Proof the draft reaches SM1=0 / SM2=0, per claim

Trees built as `git archive 3f5edbc` copies in scratch; the files the other claims land were copied in from the lane working tree so the census sees them (`self_assessment_check.py`, `lint_entry.py`, `derive_axml_anchors_r68.py`, `embedded_output_pins.json`, `fixtures/apk-r65/entry_checks.py`).

| tree | README variant | SM1 | SM2 | other SM | note |
|---|---|---|---|---|---|
| `full` (all four hunks) | section 4 | **0** | **0** | SM3=2 SM4=1 SM5=1 SM6=0 | C2's remaining legs are other seats' hunks |
| `c2` (C2 hunks only) | C2 | **0** | **0** | same | single-claim tree is green on its own labels |
| `c1` (C1 hunk only) | C1 | 1 | **4** | same | SM2 stays exactly at base value → no cross-claim rise |
| `c3` (C3 hunk only) | C3 | 1 | **4** | same | SM2 stays exactly at base value → no cross-claim rise |

Raw output (`full`, working-tree checker `ae1c62aa…`; identical with committed `6a24baa1…`):

```
SM1=0
SM2=0
SM3=2
SM4=1
SM5=1
SM6=0
SELF_MISMATCH=4
```

SM2 accounting (why C1/C3 do not raise it): `lint_entry.py` (added by C1) is named by C1's own hunk, so base 4 → 4; `derive_axml_anchors_r68.py` (added by C3) is named by C3's hunk, so 4 → 4; `fixtures/apk-r65/entry_checks.py` and `embedded_output_pins.json` are SM2-neutral by construction (`self_assessment_check.py:62-72` counts only top-level `corpus/*.py` and `corpus/*/`), named for index completeness only.

## 6. Falsification of the draft itself (every line is load-bearing)

Run on copies of `full`; only the named bullet/line was removed:

| mutation | SM1 | SM2 |
|---|---|---|
| remove `` - `snapshots/` `` bullet | 0 | **1** |
| remove `` - `check_embedded_outputs.py` `` bullet | 0 | **1** |
| remove `` - `derive_axml_anchors.py` `` bullet | 0 | **1** |
| remove `` - `q15_tree_id_check.py` `` bullet | 0 | **1** |
| remove `` - `self_assessment_check.py` `` bullet | 0 | **1** |
| `Q01–Q15` → `Q01–Q13` (line 9) | **1** | 0 |
| add `corpus/newdir/` (a directory not in the index) | 0 | **1** |

So neither SM1 nor SM2 can be satisfied by the draft while any of its lines is absent: the zero is not vacuous.

## 7. Advisory findings (calibration of the tool, not of the claim's verdict)

**F1 — SM2 accepts a path mention as "naming" (masking).** My first draft's `derive_axml_anchors.py` bullet said "printing every `snapshots/ResourceTypes.h` line …". With the `snapshots/` bullet deleted, SM2 stayed **0** — because `f"{p.name}/" in readme` (`self_assessment_check.py:71`) matched `snapshots/` inside that other bullet. Command and output:

```
$ <remove "- `snapshots/`" bullet from the first draft> ; python3 -B corpus/self_assessment_check.py --root mut3 --lane <lane>
SM1=0
SM2=0
```

Repair applied in the delivered draft: the `derive_axml_anchors.py` bullet now says "from the pinned snapshot" (no slash), and the same mutant now prints `SM2=1` (section 6). This is the only place where my draft could have leaned on incidental text; it no longer does.

**F2 — the same masking is structural for three directories in the base text.** `knowledge/`, `fixtures/` and `live/` are also mentioned as paths (`corpus/README.md:12` "under `knowledge/`" is not in the index, `fixtures/REPLAY.md`, `live/runs/`), so SM2 cannot distinguish an index entry from a path mention for those terms. A *new* directory is still killed (`corpus/newdir/` → SM2=1, section 6). Advisory for wave 2: the mutation set should include (a) a directory mutant and (b) a "path-mention-only" mutant, since the tool's own six mutants only plant `SM2` as a new `corpus/*.py` file (`self_assessment_check.py:186-193`). Not a predicate violation — `SM2`'s stated class is "must be named in the README", and a path mention does name it — but it is a looseness a wave-2 mutation-tester can legitimately probe.

**F3 — the lane working tree already carries a competing README repair; one variant must be chosen at landing.** While I ran, a sibling edited the live file: `git -C <lane> status --porcelain -- corpus SHONEN.md SCORECARD.md SKILL.md SOURCES.md` →

```
 M SHONEN.md
 M SKILL.md
 M corpus/README.md
 M corpus/self_assessment_check.py
```

Live `corpus/README.md` sha256 `c7b24f907a0e3f8d60a07d1faef3f9283aca071df5a130c10b84136a45450406`; the live tree scores

```
SM1=0
SM2=0
SM3=0
SM4=0
SM5=1
SM6=0
SELF_MISMATCH=1
```

so the live edit is equivalent on my two labels (SM5=1 remains — the unresolved pre-registration citation, another seat's hunk; C2 is not green yet). The two variants differ in ways Main should reconcile rather than stack:

- live orders the new bullets after `verify_*.py` and puts `snapshots/` last; mine keeps data dirs together (`snapshots/` after `fixtures/`);
- live **rewrites** `corpus/README.md:14` (the `lessons/` bullet) into a `round-N.md` … "for each N in 61–69" pattern, dropping the explicit `round-61.md` filename. I checked that sentence against bytes — `corpus/lessons/` holds both `round-N.md` and `round-N-verifier-spotcheck.md` for every N in 61..69 — so it is true, but it is a prose change outside the frozen SM repair;
- live has no index entry for `embedded_output_pins.json` (mentioned inside two other bullets) and none for `fixtures/apk-r65/entry_checks.py`; both are SM2-neutral, so this is presentation only;
- my draft keeps the base `lessons/` line byte-identical, so the only diff lines are the Q-range and the added bullets.

Also in flight: `corpus/self_assessment_check.py` is modified in the working tree (`ae1c62aa…`) relative to `aa1842f` (`6a24baa1…`). My before/after numbers are identical under both, so the draft is robust to that edit; but the wave-2 gate will score whatever bytes are final.

## 8. Residual risk for C2

`SM2` is a whole-tree census (`corpus/*.py` + `corpus/*/`), not a per-claim one. Any helper a later wave-1/2 seat drops at `corpus/` top level without an index line re-raises SM2 and falsifies C2 at the final tip. Re-run `python3 -B corpus/self_assessment_check.py --root <lane> --lane <lane>` after the last landing, not after this draft.

## 9. Scope compliance

No lane file written, no commit/stash/checkout/reset, no package install or upgrade, no `agent://all`, no subagent. All work ran on `git archive` copies under `/tmp/revenger-r70-R70W1ReadmeIndex` (now deleted); the only file written in the lane is this report. Commands used: `git archive | tar -x`, `python3 -B corpus/self_assessment_check.py --root … --lane …`, `diff -u`, `grep`, `sed -n`, `sha256sum`, `cp -r` in scratch.
