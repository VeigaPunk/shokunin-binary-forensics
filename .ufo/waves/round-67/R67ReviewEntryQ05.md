Q05 PASS — no readiness/capability claim stands without a probe: the provider route is fenced to S043 documentation scope, and the entry's one capability-bearing claim (its own readout's behavior) carries a probe this seat re-ran green.

# Scope

Criterion Q05 per `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/QUALITY.md:17`:
"A readiness or capability claim carries a probe against the real surface: its command, date and
observed exit, output or Evidence ID. Presence, configuration or acquisition is not capability."
Reject trigger: "the claim rests on a configured value, an install, or an unrechecked older probe."

Entry under test (committed bytes, fresh seat — not the author):
`/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-67-apk-axml-byte-evidence.md`

# Q05 findings

## 1. Provider readiness/capability: fenced, not claimed

- `round-67-apk-axml-byte-evidence.md:2` — S043 cited for "route-scope sentences only: what the
  `inspect_android_package` family is documented to take and return per rea-agents-6.5.0; **not
  provider execution** and not the fixture bytes".
- `round-67-apk-axml-byte-evidence.md:7` (coverage-map) — "Not covered: install/signature
  verification, dex validity or execution, **provider (`inspect_android_package`) readiness or
  output**, general AXML or ZIP-parser behavior beyond this fixture."
- `round-67-apk-axml-byte-evidence.md:134` (Limitations) — "Generalization to other APKs, other
  AXML producers or the `inspect_android_package` provider would need its own evidence."
- `round-67-apk-axml-byte-evidence.md:138` (§Cross-lane scope note) — "The provider route
  (`inspect_android_package`, JADX prerequisites) is documented scope from S043 only; **this lane
  ran no provider and makes no readiness claim (Q05 fence)**."
- `round-67-apk-axml-byte-evidence.md:130` (Unknown) — "nothing about install validity, signature
  blocks, dex program validity or **any provider's behavior** is claimed".
- Anchor quote verified: `.ufo/waves/round-65/source-snapshots/rea-android-applications.md` raw
  lines 7-8 do read "Start with `inspect_android_package` on the caller's APK path for package
  identity, manifest declarations, coverage, and inline Evidence." — a documentation statement the
  entry uses as documentation scope, never as a run probe. No `Evidence` ID, exit code, or observed
  provider output is asserted anywhere.

## 2. Capability claims that ARE made all carry probes

- `round-67-apk-axml-byte-evidence.md:6` (recheck) claims the readout "exits 0 and prints 15
  stdout lines whose SHA-256 is `507d79f8…dad247` (re-derived 2026-10-24)". This is the entry's
  only load-bearing capability claim, and it is a probe (command + date + observed exit/output).
  This seat re-ran it on the committed bytes:

  ```
  $ cd /home/vgpnk/Projects/shokunin/revenger-shokunin && python3 -B corpus/fixtures/apk-r65/readout.py | sha256sum; wc -l
  507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247  -
  15   (exit 0)
  ```

  Matches entry:6 exactly — the probe is current, not stale.
- `--fact '<id>'` capability (entry:6) is itself probed: items 1–10 embed the actual
  `$ python3 -B corpus/fixtures/apk-r65/readout.py --fact …` commands with observed stdout
  (entry:23–24, 30–31, 37–42, 52–53, 61–62, 70–71, 77–78, 84–85, 91–92, 98–101, 109–110, 118–119).
- "The stdout carries only repo-relative paths" (entry:6): consistent with observed output —
  the only path literal in stdout is `"path": "corpus/fixtures/apk-r65/fixture.apk"` (entry:24/172).
- Pinned own-work bytes verified: `sha256sum` gives fixture `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e`,
  readout.py `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976`,
  truth.json `27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173` — all equal entry:4.

## 3. Reject-trigger sweep

- No claim rests on a configured value or an install: the only environment named is "Python
  standard library" used as the reader (entry:12, 128), never credited with a produced result.
- Older-probe clause: entry:124 discloses "Regenerating the fixture from `generator.py` … was
  round-65 evidence (S041) and is **not re-run** by this entry; the committed bytes are hash-pinned."
  Nothing load-bearing rests on that older probe — the claims rest on hash-pinned bytes plus the
  re-derived readout (§2). The trigger ("rests on … an unrechecked older probe") is not met.
- Method assertions "no producer is called", "the fixture is inert" (entry:12, 130) are scope
  statements about what was NOT done — the opposite of a readiness claim.

# OFF-criterion observations (informational, not scored here)

- OFF: entry:5's provenance sentence ("every output line below was captured from the named
  command's actual stdout at build time") is an M39-repair claim; the round-65 candidate's retained
  drift is confirmed at `corpus/knowledge/round-65-apk-axml-byte-evidence.md:41`
  (`payload_first16_hex` `4d616e696673742d56657273696f6e` = "Manifst-Version", 15 bytes) versus
  the v2 entry's corrected 16-byte `4d616e69666573742d56657273696f6e` (entry:42) — verbatim
  agreement is the new C7 gate's problem (`corpus/check_embedded_outputs.py`), not Q05's.
- OFF: entry:148's Q-map self-assessment ("Q05 | pass") is the author's row, not this seat's
  decision; consistent with admission order §2 (claims.md:117-120) that named fresh seats decide.

No installs or updates performed; all checks read-only (readout run + sha256sum).
Report: .ufo/waves/round-67/R67ReviewEntryQ05.md
