# ExecControlsR100 findings — revenger round 100, wave w1

Seat: ExecControlsR100 (builder: C2 control recipe + M21 census-line check). Lane commit at work start: 05e854ce (claims freeze). No tools installed or upgraded; no pacman transactions; no writes outside assigned paths, wave dir, and scratch.

## Files built (both final, BUILT sent)

| file | sha256 |
|---|---|
| `reports/round-100/controls_c2.sh` | `479f690e6aeb4d43eab64edba2df4429ed2be9cb5dafc843ea1065c2f31ee408` |
| `reports/round-100/census_line_check.py` | `c3b754aa0e136e88195c3381da0f3f32672ce2b49ea70fe294668013aa0a949f` |

## (a) controls_c2.sh — C2 control recipe

`controls_c2.sh <probe.py> <outdir>` (rc 0 both controls refused, 1 a control accepted, 2 usage/setup; scratch `${HYAKU_SCRATCH:-${TMPDIR:-/tmp}}`, removed on exit; stdout exactly `C2_CTRL_STUB=`, `C2_CTRL_FLIP=`, last `C2_CONTROLS=`).

- STUB leg: PATH shims `androguard`/`apktool` in scratch (forges; ignore input, hardcoded TRUE manifest `com.example.r65`/`1`/`1.0`, well-formed XML with namespaced attrs, plausible version lines `androguard, version 4.1.4` / `3.0.3` — the exact real formats observed on this host). Shim argv coverage matches ExecApkProbe's fixed decoder design: `[and, axml, apk]` stdout XML + `--version`; `[apktool, d, -f, -s, -o, DIR, apk]` → `DIR/AndroidManifest.xml` + `--version`.
- FLIP leg: `cp -a` of the fixture dir, then one byte of the copy's `fixture.apk` flipped — the versionCode `Res_value.data` low byte (INT_DEC 1→2), located by the readout.py struct walk (ZIP local header → stored AXML payload → chunk walk → string pool → START_ELEMENT attrExt → attr name `versionCode` → data u32 at +16). Observed offset in the fixture: **393**.
- refused := probe rc 1 AND `CAP_APK_VERDICT=fail` (per claims §C2 controls ii/iii).

**Development run (disclosed; the scored control run is the L1's after FROZEN).** Probe bytes: `reports/round-100/cap_apk_probe.py` as written by ExecApkProbe at 19:50 (their pre-BUILT WIP; interface confirmed by them in writing before my run). Command: `HYAKU_SCRATCH=<scratch> bash controls_c2.sh reports/round-100/cap_apk_probe.py <wave dir>`.

```
C2_CTRL_STUB=refused
# flipped versionCode data byte at apk offset 393 (1 -> 2)
C2_CTRL_FLIP=refused
C2_CONTROLS=control-ok
rc=0
```

- `control-stub.log`: CAP_FIXTURE_SHA=pass; shim version lines recorded; CAP_ANDROGUARD=pass, CAP_APKTOOL=pass (shims echo truth); **CAP_TAMPER_DETECTED=fail** — probe: "androguard echoed the truth value" (shim reported `1.0` where tampered `1.1` required); CAP_APK_VERDICT=fail; probe_rc=1.
- `control-flip.log`: **CAP_FIXTURE_SHA=fail** (digests printed); CAP_ANDROGUARD=fail (decoded versionCode '2' vs expected '1'); CAP_APKTOOL=pass (see nuance); CAP_TAMPER_DETECTED=fail (probe's tamper builder refuses the CRC-broken zip: "Bad CRC-32"); CAP_APK_VERDICT=fail; probe_rc=1; `# CAP_FIXTURE_SHA=fail present` marker appended.

Both logs + `controls-dev.log` saved in the wave dir.

**Observed decoder nuance (disclosed, not a probe bug):** on the flipped fixture, real apktool 3.0.3 still renders `versionCode="1"` — it prefers the AXML raw string-pool value (`raw_value_idx → "1"`), while androguard reads the typed data value (→ '2'). Verified directly: `apktool d -f -s` on a flipped copy, rc 0, `n0:versionCode="1"` in its manifest. The claims-pinned byte is the data byte, so this is per spec; the control refuses for the required reasons regardless (CAP_FIXTURE_SHA=fail + CAP_APK_VERDICT=fail via sha + androguard + tamper legs). Recorded so nobody reads `CAP_APKTOOL=pass` in the flip log as a control failure.

## (b) census_line_check.py — M21 census-line check

`--report <md> --log <census log>`; counts `\tW04\t`-style tab-delimited `[WE]\d\d` fields in the log, finds report lines mentioning `census` that carry count tokens (`<n> × CODE`, `×` also as x/X/*, plus `<n> CODE-codes`), and requires **every** such census line to name every nonzero log class with exactly its count (self-contained-summary semantics; a wrong count counts as missing). Prints `CENSUS_LINE_CHECK=pass|fail missing=<classes>` (`none` on pass); rc 0/1 (fail)/2 (usage or unreadable input).

Shown able to fail and pass (both run logs in the wave dir):

| run | report | log | output | rc |
|---|---|---|---|---|
| fail (expected) | `/home/vgpnk/Projects/shokunin/.ufo/reports/round-99/revenger.md` | `reports/round-99/controls/census-round-end.log` (21 × W01, 13 × W04 records) | `CENSUS_LINE_CHECK=fail missing=W04` | 1 |
| pass (expected) | synthetic (wave dir `census-synth-report.md`) | synthetic (wave dir `census-synth-input.log`, 2 × W01 + 3 × W04) | `CENSUS_LINE_CHECK=pass missing=none` | 0 |

The fail case reproduces the r99 closure finding: the report's after-census line ("21 × W01, 0 E-codes") omitted `13 × W04`. The before-census line on the same report does name W04; per-line semantics means it cannot rescue the after line — this is the documented behavior choice, matching the failure mode the check exists for.

## Interface facts (from ExecApkProbe, in writing)

Decoder argv + version-line formats as listed above; tampered versionName value `1.1`; CAP_FIXTURE_SHA=fail does not short-circuit (probe prints all contract lines, verdict fail, rc 1; rc 2 reserved for usage/missing-decoder/broken-fixture-dir) — my refused predicate (`rc 1` + verdict line) is safe against rc 2 on the CRC-broken flip leg. Confirmed truth.json is read from the handed `--fixture` dir, so my flipped-copy leg shape (original truth.json + flipped fixture.apk) is the intended one.

## Risks / notes for the L1

- My controls are dev-verified against the 19:50 probe bytes. If the frozen probe bytes change the contract line spellings (e.g. `CAP_APK_VERDICT=` wording) or rc semantics, re-run `controls_c2.sh` against the FROZEN probe before scoring; the script greps only the frozen contract strings and probe rc.
- `CENSUS_LINE_CHECK` requires each census line to be self-contained (see above). A future report splitting counts across multiple census lines would fail — intended strictness, documented in the tool docstring.
- Flip offset 393 is computed at run time from the bytes, never hardcoded; the helper asserts name/method/data-type/data value before flipping and aborts rc 2 if the fixture changes shape.
- apktool debug run may have touched `~/.local/share/apktool` (explicitly allowed).
