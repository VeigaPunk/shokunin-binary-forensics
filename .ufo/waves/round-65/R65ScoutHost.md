CLEAN — all three environment claims verified; the only jadx-presence citation found (corpus/README.md:69, pre-existing, frontier route note) records presence without crediting capability — reported below as a borderline finding for adjudication.

Seat: R65ScoutHost (scout, coverage). Scope: re-verify the round's environment claims used in the entry/lesson — `python3 --version`, readout uses no network / opens only `fixture.apk` beside it, and `jadx 1.5.6` presence is NOT cited as capability (Q05 fence). Read-only; no production edits.

## 1. `python3 --version` → verified

Host fact, run 2026-10-24:

```text
$ python3 --version
Python 3.14.8
$ python3 -c 'import sys; print(sys.executable)'
/usr/bin/python3
```

Citations checked against this observation:

- `corpus/knowledge/round-65-apk-axml-byte-evidence.md:4` — "regeneration from `generator.py` in a scratch copy reproduced `fixture.apk` byte-for-byte on this host, Python 3.14.8". Match.
- `corpus/knowledge/round-65-apk-axml-byte-evidence.md:121` — "(Python 3.14.8)". Match.
- `corpus/fixtures/apk-r65/truth.json:67` — `"python_version": "3.14.8"` (oracle-recorded build metadata, written by `generator.py:219` via `platform.python_version()`). Match.
- `corpus/SOURCES.md:55` (S041 row) — "regeneration in a scratch copy reproduced the fixture byte-for-byte on Python 3.14.8". Match.

Every 3.14.8 citation in the round-65 artifacts agrees with the observed interpreter. No version claim falsified.

## 2. Readout needs no network / opens only `fixture.apk` → verified

Claims: entry `:11` ("no producer is called, no network is used, and no verifier source is read"), `:15`, `:125` ("runs with the Python standard library only"), `:162` ("reads only `fixture.apk` beside it").

Static audit of `corpus/fixtures/apk-r65/readout.py` (all 256 lines read):

- Imports (`:13-18`): `hashlib, json, struct, sys, zlib, pathlib.Path` — standard library only; no `socket`, `urllib`, `http`, `requests`, `subprocess`, `os`, `zipfile`, `exec`/`eval`.
- Only file opened: `readout.py:20-21` `ROOT = Path(__file__).resolve().parent; APK = ROOT / "fixture.apk"`, read once at `:44` `apk = APK.read_bytes()`. No `open()`, `Path.write_*`, or other filesystem touch. Everything downstream operates on the in-memory `apk` bytes (`u16`/`u32` struct reads `:33-38`).
- Dynamic run confirms: `python3 -B corpus/fixtures/apk-r65/readout.py` from the lane root printed 15 lines; `sha256sum` of stdout = `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` — identical to the digest claimed in the entry header `recheck:` (`:5`) and §Reproduce (`:162`). No network capability exercised.

## 3. jadx 1.5.6 presence-as-capability → CLEAN; one borderline pointer

Host fact: `command -v jadx` → `/usr/bin/jadx`; `jadx --version` → `1.5.6`. jadx IS present.

Sweep for `jadx` (case-insensitive) across the lane, classified:

| File:line | Class | Assessment |
|---|---|---|
| `corpus/knowledge/round-65-apk-axml-byte-evidence.md:2` (S039 source line) | doc-scope | cites "separately supplied JADX prerequisite" as what S039 *documents*; no host-presence or capability claim. Clean — this is the fence working. |
| `corpus/knowledge/round-65-apk-axml-byte-evidence.md:135` (§Cross-lane scope note Q10) | doc-scope | "(JADX prerequisites) is documented scope from S039 only; this lane ran no provider and makes no readiness claim (Q05 fence)". Explicit non-claim. Clean. |
| `corpus/SOURCES.md:53` (S039 row) | doc-scope | "separately supplied JADX MCP JAR 0.7.1 and Java 17 prerequisite); not provider execution on this host". Documents a prerequisite; explicitly disclaims host execution. Clean. |
| `.ufo/waves/round-65/source-snapshots/rea-android-applications.md:16-19,27` | doc-scope | quoted source bytes (REA_JADX_MCP_JAR / Java 17 / REA_JADX_HEAP_MIB requirements); documentation content, not a lane claim. Clean. |
| `corpus/README.md:69` | **borderline — reported** | "C05 Android — REA `inspect_android_package`; jadx 1.5.6 is present; needs an authored APK fixture." The only sentence anywhere in the round-65 surface that states jadx *host presence*. It does NOT credit jadx with a result — the same sentence names the actual blocker ("needs an authored APK fixture"), and the sibling C07 line `:65-66` says "Presence is not readiness". Pre-existing: `git log -S 'jadx 1.5.6 is present'` → introduced at commit `35b2e8b` (2026-10-19, round-1 re-verification), unchanged by this round (README untouched since `cab8085` round-64). Not an entry/lesson sentence; it is the frontier row's route note. Reported as a finding per seat brief — adjudicators decide whether "is present" in a route-status note counts as presence-as-capability; this seat's judgment: it does not (presence stated, capability neither claimed nor exercised; the C05 gate was manual byte readout). |
| `corpus/knowledge/seed.md:64`, `corpus/knowledge/2026-10-12-rea-readiness-checklist.md:40` | historical census | re-verification rows recording jadx 1.5.6 presence as a STALE-flagged census fact — these are the readiness record itself, not capability credit. Pre-existing, out of round-65 diff. |
| `corpus/lessons/round-1.md:56`, `LOG.md:775`, `PROVINCE.md:16`, `.ufo/waves/kaika-r1/*`, `.ufo/waves/round-64/scout-readme.md:21`, `considerthese/2026-10-20.md:75` | historical | prior-round records; kaika-r1/planner.md:76 even sets the precedent "`jadx` presence is not an APK record". No new citation by round 65. |

Negative results (targeted sweeps): no `jadx` anywhere in `corpus/fixtures/apk-r65/`, `reports/round-65/`, or `corpus/lessons/round-65.md`. The candidate entry's §Q-map Q05 row (`:145`) and §Limitations (`:131`) make no tool-availability claim.

## Remaining unknowns

- Whether adjudicators treat `corpus/README.md:69`'s "jadx 1.5.6 is present" as a violation of the Q05 fence — this seat judges it a pre-existing route-status note (presence ≠ capability, per the lane's own C07 wording "Presence is not readiness"), reported for their call.
- The README C05 row is still `frontier` (`:69`); consistent with the frozen admission order (flip is L1's, post Q-decisions).

Commands run (all read-only): `python3 --version`, `python3 -c 'import sys; print(sys.executable)'`, `python3 -B corpus/fixtures/apk-r65/readout.py` (2 runs: `| wc -l` → 15, `| sha256sum` → `507d79f8…247`), grep sweeps for `jadx`/network modules over the lane, `git log -S`/`-3` on `corpus/README.md`, `command -v jadx; jadx --version`. No installs performed; no tooling changes.
