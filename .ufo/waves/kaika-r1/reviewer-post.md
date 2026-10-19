# Reviewer post-landing verification — kaika r1, claims C1 and C3

Date: 2026-10-19. Lane: `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/revenger-shokunin`, base `8bbcb4e`, uncommitted working tree. No lane file was edited. Temp work lived in `/var/tmp/rev-Gie1` (copy of working-tree `corpus/`, a base extract from `git archive 8bbcb4e corpus`, and a throwaway HIST-control copy), deleted after this report. No commits, installs, or REA producer calls.

## Verdicts

| claim | verdict | basis |
|---|---|---|
| C1 — `verify_icon_languages.py` and `verify_multi_icon_states.py` landed with the ROOT/HIST split; SCORECARD command C prints `CALIBRATION 4 / 4` and `REPLAY 10 / 10` (was 2/4, 8/10) | **verified** | Command C reproduces 4/4 and 10/10 from lane cwd and from the `/var/tmp` copy; base reproduces 2/4 and 8/10; every oracle §6 check passes. One non-blocking doc defect, D1 (SCORECARD prose is stale). |
| C3 — headers plus `## Re-verification 2026-10-19` tables in `seed.md` and `2026-10-12-rea-readiness-checklist.md`; base bytes preserved; probes re-run | **verified** | Base bytes occur verbatim, once, contiguously in both files; no `-` lines in either diff; 0 of 18 F/K rows differ today. |

## C1 — oracle §6 checklist

**1. Input hashes (§4).** `git -C <lane> show 8bbcb4e:<p> | sha256sum` vs `sha256sum <lane>/<p>` for all 16 inputs: every pair equal (e.g. `pe-r47/fixture.exe` both `cc02c78b…ba44ba`; `round-49/producer-receipt.json` both `7e6f14bb…985e15`). Base scripts hash to `84d2a5af…1ca` (icon) and `5fec3e2b…1803` (multi), matching §4. Working-tree scripts differ as expected (`ed0ad166…bd95`, `5b75339c…49f8`). **PASS.**

**2. `require(` and `raise` counts (AST walk, base vs lane).**
```
verify_icon_languages.py   base require=28 {check 12, decode 4, file_offset 1, main 4, walk 7} raise=3
verify_icon_languages.py   lane require=28 (same)                                          raise=3
verify_multi_icon_states.py base require=25 {check 9, decode 4, file_offset 1, main 4, walk 7} raise=3
verify_multi_icon_states.py lane require=25 (same)                                          raise=3
```
`git diff` hunks touch only: the header comment, the `HIST` constant, the `hist=` line, the artifact `require` line, and the receipt `require` (adds `command` clause). No `require` line is removed or weakened. **PASS.**

**3. Forged-claim rejections F1 and F2 still exist and reject.** Lane `main()` still deep-copies the saved record, mutates the same field, and requires inequality against decoded truth:
- F1 icon: `forged[...]['images'][0]['same_language_resource_index']` None → 0 (`corpus/verify_icon_languages.py:156-159`). Probe output: `F1 REJECTED: forged selection`.
- F2 multi: `forged[...]['images'][1]['same_language_resource_index']` None → 1 (`corpus/verify_multi_icon_states.py:155-159`). Probe output: `F2 REJECTED: forged selective match`.
- The unmodified records are accepted by the same comparison (`sanity ... True True`). The `except AssertionError` remains (base form, unchanged, a looseness gap not a weakening). **PASS.**

**4. EXPECTED pins byte-identical to base.** AST source-segment comparison of the `EXPECTED = {...}` literal, base vs lane: icon `True` (547 chars), multi `True` (882 chars). **PASS.**

**5. Artifact expectation derived from HIST, not from the saved field.** Icon: `hist=HIST/f'fixtures/pe-r{r}/fixture.exe'` (`verify_icon_languages.py:121`), compared as `dict(path=str(hist),…)` (L130). Multi: `hist = HIST / …` (L124), compared at L133. The expected value is built from the module constant and pinned hash, never copied from `record['normalized_result']['artifact']`. **PASS.**

**6. Receipt check.** `grep -n duration` over both lane scripts: no match. Icon L143-145 and multi L142-144 keep `exit_code==0`, `fixture_sha256==expected_hash`, `evidence_id==eid`, `stdout_sha256==H(raw_bytes)`, and add `command==f'npx -y rea-agents@6.4.0 inspect-pe-resources {hist} --format json'`. **PASS.**

**7. Direct run in the landed lane.**
```
python3 -B corpus/verify_icon_languages.py
PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED   (rc=0)
python3 -B corpus/verify_multi_icon_states.py
PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED   (rc=0)
```
**PASS.**

**8. Saved records and fixtures unchanged.** `git -C <lane> diff --stat 8bbcb4e -- corpus/fixtures corpus/live` printed nothing (rc=0). `git status --short -- corpus/fixtures corpus/live` printed nothing. No `__pycache__` under `corpus/`. **PASS.**

## C1 — SCORECARD command C

Command C was run verbatim from SCORECARD.md:35-42 (`python3 -B -c '…'`, which runs each `corpus/verify_*.py --self-test`).

**Lane cwd** (`/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/revenger-shokunin`):
```
verify_icon_languages.py exit=0 PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
verify_icon_states.py exit=0 PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
verify_multi_icon_states.py exit=0 PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
verify_named_multi_icon_states.py exit=0 PASS: 139 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). …
(remaining 6 replay scripts all exit=0)
CALIBRATION 4 / 4 score= 10.0
REPLAY 10 / 10
rc=0
```
**Copy** (`/var/tmp/rev-Gie1/corpus`, cwd `/var/tmp/rev-Gie1`): identical output, `CALIBRATION 4 / 4 score= 10.0`, `REPLAY 10 / 10`.

**Base** (`git archive 8bbcb4e corpus`, cwd `/var/tmp/rev-Gie1/base`): `verify_icon_languages.py exit=1 AssertionError: r47: artifact`; `verify_multi_icon_states.py exit=1 AssertionError: r42: artifact`; `CALIBRATION 2 / 4 score= 5.0`; `REPLAY 8 / 10`. This reproduces the claimed "was" values. **PASS.**

**HIST is never used to read bytes.** Two independent checks:
- Static: `HIST` appears only in the constant (icon L10, multi L10), in `hist=` path construction (icon L121, multi L124), in the artifact string compare (icon L130, multi L133), and in the receipt command string (icon L145, multi L142). All `read_bytes`/`read_text` calls use `root/` (fixtures and `live/runs/round-N/`).
- Runtime: `sys.addaudithook` on `open` events while `runpy`-executing each lane verifier. Opens were limited to `<lane>/corpus/verify_*.py`, `fixtures/pe-rNN/fixture.exe`, `live/runs/round-NN/{inspection.raw.json,producer-receipt.json}`. HIST-prefixed opens: **0** in each. A first no-HIST control replaced the HIST string and failed on string comparison, so it tested nothing about byte reads. I discarded it.

## C3 — base-byte preservation

Python check, `git -C <lane> show 8bbcb4e:<p>` searched in the current file:

| file | base bytes | current bytes | base occurrences | base offset (header prefix) | appended suffix |
|---|---|---|---|---|---|
| corpus/knowledge/seed.md | 2370 | 5236 | 1 (contiguous, verbatim) | 663 | 2203 |
| corpus/knowledge/2026-10-12-rea-readiness-checklist.md | 1484 | 3071 | 1 (contiguous, verbatim) | 442 | 1145 |

`git diff -- <both>` hunks contain only `+` lines plus context; no base line is removed or altered. **PASS.**

## C3 — F/K probes re-run today

Commands: `ls`/`sed -n 1,8p`/`ls references/`, `command -v`, `npm view`, `node --version; npm --version`, `jadx|binwalk|unblob --version`, `python3 -c 'import pwn'`, `unzip -v`, `zipinfo -h`, and a key-only parse of `~/.omp/agent/mcp.json` (top-level keys, server keys, and `rea-agents@` tokens of the `rea` entry only).

| row | table verdict | observed today | matches? |
|---|---|---|---|
| F01 | holds | `SKILL.md`, `SKILL.md.rea.backup`, `references/` | yes |
| F02 | STALE → 42 / 207 | `metadata.version: "42"`, `tool_count: 207` | yes |
| F03 | holds (names) | same six names; 5 files mtime 2026-10-14 with `.rea.backup`; `android-applications.md` 2026-10-12 | yes |
| F04 | holds | `command -v rea` rc=1, no output | yes |
| F05 | STALE → 6.7.0 | `npm view rea-agents version` = 6.7.0; `rea-agents@6.4.0` still published; SKILL names `rea-agents@6.7.0` | yes |
| F06 | STALE → v24.21.0 / 11.19.0 | `v24.21.0` / `11.19.0` | yes |
| F07 | STALE (registered) | `mcpServers` has key `rea`, token `rea-agents@6.5.0` | yes |
| F08 | holds | `command -v ghidra` rc=1 | yes |
| F09 | STALE (present) | `jadx` 1.5.6 | yes |
| F10 | STALE (present) | `binwalk 3.1.0` | yes |
| F11 | STALE (present) | `26.6.4` | yes |
| F12 | holds | `ModuleNotFoundError: No module named 'pwn'` | yes |
| K01 | holds | `command -v rea` rc=1 | yes |
| K02 | STALE → v24.21.0 / 11.19.0 | same; npm 6.7.0 | yes |
| K03 | STALE (registered) | `rea` entry, `rea-agents@6.5.0` | yes |
| K04 | holds | ghidra and ida rc=1 | yes |
| K05 | STALE, 3 of 4 present | jadx, binwalk, unblob present; pwn fails | yes |
| K06 | holds | `UnZip 6.00`, `ZipInfo 3.00` | yes |

Rows whose observed value differs today: **none**. Header counts also agree: seed "7 of 12 census facts stale" (F02, F05, F06, F07, F09, F10, F11); checklist "3 of 6 rows stale" (K02, K03, K05). **PASS.**

## Defects and residual risk

**D1 (documentation, non-blocking for the C1 verifier claim).** `SCORECARD.md` was not updated by the landing and now contradicts command C:
- `SCORECARD.md:9` says `2.5 → 5.0 (10 × 1/4 → 10 × 2/4)`. Command C now prints `10.0` (4/4).
- `SCORECARD.md:19-20` says "The language and numeric multi-image verifiers still fail at their original artifact-path assertions." Both now exit 0.
- `SCORECARD.md:63` ("No additional verifier is changed in fleet round-1") is also contradicted by the two verifier edits.
- Fix: update `:9` to the measured after-state (`10 × 4/4 → 10.0`; replay `10/10`), rewrite `:19-20` to state the landed state with this run's command and output, and reconcile `:63`. Not edited by me.

**Residual risk (not defects).**
- Both verifiers pin an absolute host string (`/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus`). It is only compared as a string, so the check is host-independent. It is still a machine-specific identity.
- `except AssertionError` around the forged `require` is unchanged base behavior. It is loose but not weakened by this landing.
- C3 headers cite `.ufo/waves/kaika-r1/scout-freshness.md`, an untracked path. Provenance of the re-verification depends on that file being committed with the round.

## Hand-off for main agent

Nothing further needed to verify C1 or C3. Main agent may re-run `python3 -B corpus/verify_icon_languages.py` and `python3 -B corpus/verify_multi_icon_states.py` (both exit 0 here) and the SCORECARD command C block after the D1 edit.
