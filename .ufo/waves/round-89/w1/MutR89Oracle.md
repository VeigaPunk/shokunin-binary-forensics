# MutR89Oracle — round-89 W1 mutation probe (frozen apk oracle)

Axes: **coverage** (does removing each named oracle leg let its targeted tamper pass?) and **calibration** (does the bounded detector reject the frozen oracle's bad inputs before any mutant is scored, and do the mutants still accept clean inputs?). Scope: C2 only. No lane oracle edit, no commit, no push, no mutating git/jj, no `.ufo/state`, `.scratch`, `MANIFEST.json`, or sibling-repo write.

## Verdict

- 5 of 5 requested legs were mutated in isolated scratch copies.
- **Load-bearing (killed) for their named tamper: package_name, subject_digest, class_count, evidence_id regex, member_digest (premise tamper in truth.json).**
- **Redundant for record tampering: member_digest.** Removing the premise member-digest check does not change any verdict on a tampered producer record, because that check reads only the fixture bytes and `truth.json`, never `rec`. Its only load-bearing role is premise validation (catching a changed `truth.json` digest against the fixture bytes). It cannot be shown load-bearing against a record tamper.
- Scope note (not a mutant result): the oracle's expected package name and manifest attributes come from `truth.json` `axml_declared.strings`, not from decoding `AndroidManifest.xml`. The oracle does not check that the AXML bytes actually contain those strings. This means the declaration legs are only as strong as `truth.json`. `ReviewerR89C2` reports a fixed-truth contradiction (`com.attacker.fabricated`, versionCode 999 inside an XML comment) that passes 19/19 on their side. I did not reproduce that run; it is their finding.

## Pins and detector

- Freeze commit `c84339c`: `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin show c84339c:corpus/fixtures/apk-r65/oracle_check.py | sha256sum` = `44fd1505d171c4e37d5d36ecd4a8aa5aff30229538840692bd0dc9cffde68a53`. Working-tree oracle `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/apk-r65/oracle_check.py` has the same hash and was not edited.
- Authored APK `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/apk-r65/fixture.apk` = `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e`.
- Truth `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/apk-r65/truth.json` = `27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173`.
- Producer record `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-89/inspection.json` = `01af3141d79027a3bae53b6482779d3e9c89446ab6ca09b408a6cb266f321c76`. Read-only, copied to scratch before any mutation. `ExecR89Record` reports these are the exact current-producer stdout bytes (rea 6.7.0 / jadx 0.7.1).
- Runtime: Python 3.14.8, `python3 -B <oracle.py> <truth.json> <record.json>`, `TMPDIR=/fast/scratch/hyaku/revenger-r89/MutR89Oracle`, 10 s timeout per invocation, no timeouts.
- Tool installs or upgrades: **none**. Preinstalled Python only. No package-manager transaction (pacman is paused host-wide and was not touched).

## Results

| mutant (one leg removed or weakened in a scratch copy) | tamper (applied to scratch copy of the record or truth) | frozen oracle verdict | mutant verdict | leg shown load-bearing |
|---|---|---|---|---|
| `package_name` (delete check, lines 108–109) | `normalized_result.package_name` → `com.example.other` | exit 1, `ORACLE FAIL (18/19 checks)`; `check FAIL: package_name 'com.example.other' != authored 'com.example.r65'` | exit 0, `ORACLE OK (18/18 checks)` | **load-bearing (killed)** |
| `subject_digest` (delete check, lines 100–102) | `subject.digest.sha256` → 64 × `0` | exit 1, `ORACLE FAIL (18/19 checks)`; `check FAIL: subject digest != the fixture bytes` | exit 0, `ORACLE OK (18/18 checks)` | **load-bearing (killed)** |
| `class_count` (delete DEX check, lines 118–120) | `normalized_result.class_count` 0 → 1 | exit 1, `ORACLE FAIL (18/19 checks)`; `check FAIL: class_count 1 != DEX class_defs_size 0` | exit 0, `ORACLE OK (18/18 checks)` | **load-bearing (killed)** |
| `evidence_id` (weakened: `re.fullmatch(r"ev_[0-9a-f]{64}")` → `re.match(r"ev_")`, line 97) | `evidence_id` → `ev_` | exit 1, `ORACLE FAIL (18/19 checks)`; `check FAIL: evidence_id 'ev_'` | exit 0, `ORACLE OK (19/19 checks)` | **load-bearing (killed)** — the weakened regex accepts the short id, so the shape leg alone is what rejects it |
| `member_digest` (delete check, lines 72–76), premise tamper | `truth.members[0].sha256` (AndroidManifest.xml) → 64 × `0`; record unchanged (exact producer bytes) | exit 1, `ORACLE FAIL (18/19 checks)`; `check FAIL: a member digest disagrees with truth.json or is unrecorded` | exit 0, `ORACLE OK (18/18 checks)` | **load-bearing for premise validation (killed)** |
| `member_digest` (delete check), record tamper | `normalized_result.package_name` → `com.example.other`; truth unchanged | exit 1, `ORACLE FAIL (18/19 checks)`; `check FAIL: package_name 'com.example.other' != authored 'com.example.r65'` | exit 1, `ORACLE FAIL (17/18 checks)`; same package FAIL line | **redundant for record tampering (survived)** — the member-digest leg never reads `rec` |

Count note: each mutant deletes one check, so its clean-run denominator is 18, not 19. The weakened `evidence_id` mutant keeps its check (19/19).

## Controls

- Frozen oracle + exact producer record + unchanged truth: exit 0, `ORACLE OK (19/19 checks)` (`frozen-clean.json`). The detector is not broken by the input.
- Every scratch mutant + exact producer record + unchanged truth: exit 0 (`mutated-clean-*.json`). Each mutant still accepts the clean record, so the rejections in the table are caused by the removed or weakened leg, not by a broken copy.
- Frozen oracle on each tamper: exit 1, `18/19`, with exactly the FAIL line shown above (`frozen-*.json`). The baseline is therefore not inconclusive.
- Restoration: after the mutant runs, each scratch copy was overwritten with the frozen bytes; SHA-256 re-derived = `44fd1505…68a53` for all five (`restoration-hashes.json`). Re-running the frozen detector and the tampered inputs against the restored copies produced byte-identical exit/stdout/stderr to the pristine runs (`restored-*.json`, `results.json` `restored_outputs_exactly_match_pristine: true`).

## Legs

- package_name: load-bearing against a package rewrite (only check that rejects it).
- subject digest: load-bearing against a subject digest that does not match the fixture bytes.
- DEX class_count: load-bearing against a class count that does not equal DEX `class_defs_size`.
- evidence_id shape: load-bearing against a short id; weakening the regex lets it through.
- member digest: load-bearing for premise validation (a truth.json digest change). **Redundant for record tampering.**

## Receipts

Copied to `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-89/w1/MutR89Oracle/`: `pins-before.json`, `pins-after.json`, `input-manifest.json`, `mutations.json` (before/after SHA-256 and unified diffs), `results.json`, `restoration-hashes.json`, `frozen-*.json`, `pristine-*.json`, `mutated-*.json`, `restored-*.json`, the scratch inputs `record-*.json`, `truth-member_digest.json`, and the five mutant copies `mutant-*.py`. Scratch `/fast/scratch/hyaku/revenger-r89/MutR89Oracle` deleted after copy.

Report: .ufo/waves/round-89/w1/MutR89Oracle.md
