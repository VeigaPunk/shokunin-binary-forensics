# R65ReviewEntryQ05 — Q05 (readiness / capability) on the C05 candidate entry

**ADMIT (Q05 PASS)** — the entry and the lesson make no readiness/capability claim and the provider route is fenced to S039 documentation scope; one flip-time README defect (F1) must be corrected in the same commit as the C05 flip, and one S039 anchor is misnumbered (F2).

Reviewed revision: `8214e4d` (round-65 verifier spot-check). Working tree clean except another seat's untracked `R65ExecCensusProbe.md`; `git diff --stat HEAD -- corpus/README.md` empty.

Criterion (`corpus/QUALITY.md:17`): "A readiness or capability claim carries a probe against the real surface: its command, date and observed exit, output or Evidence ID. Presence, configuration or acquisition is not capability. | the claim rests on a configured value, an install, or an unrechecked older probe | M01, M19".

## Surface and digests

| file | sha256 / lines |
|---|---|
| `corpus/knowledge/round-65-apk-axml-byte-evidence.md` (entry, `admission-status: candidate`) | `e173e6436e9b8cce2ddd9f318b914fde6fd9bdfaf18335f5a873ac60fa3cdfb7`, 162 lines |
| `corpus/lessons/round-65.md` | `f55e34110a8b384d98db9b43faba04be94ec516e2f7dc7a8ccdb952fa6531626` |
| `corpus/README.md` | `9fc7eb3fe326dda0cfa2390699af536aa880f684d80cbd92bf85814309d0349f`, 74 lines |
| `.ufo/waves/round-65/source-snapshots/rea-android-applications.md` (S039) | `412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c`, 34 lines (matches entry:2 and lesson:13) |
| `corpus/SOURCES.md` (rows S038–S041 at lines 52–55) | `ef839dcbe2e3aeb64820adfd6b3b8db569a9d3b0eea716c51a48fcb8ea70d38e` |

Build state at HEAD is committed: `git ls-tree HEAD` shows `corpus/knowledge/round-65-apk-axml-byte-evidence.md` and `corpus/fixtures/apk-r65/{fixture.apk,generator.py,readout.py,truth.json}` (commit `c7b7cf9`); HEAD `8214e4d` adds only `corpus/lessons/round-65-verifier-spotcheck.md`.

## Findings

### F1 — Medium — README `## Frontier` C05 bullet is a stray presence-as-progress claim and becomes stale at the flip

`corpus/README.md:69-70` (pre-existing; added by `35b2e8b`, round 1 — not authored by round 65):

```
69  - C05 Android — REA `inspect_android_package`; jadx 1.5.6 is present; needs an
70    authored APK fixture.
```

Three defects, all inside the C05 surface this round flips:

1. **Presence/configuration standing in for capability.** The adjacent C07 bullet states the file's own rule — "Presence is not readiness" (`README:65-66`) — and requires a fixture probe. The C05 bullet names a bare presence with no command, date, exit or Evidence ID and no caveat, and names fixture authorship as the *only* remaining need. The fixture now exists at HEAD, so the bullet reads as "the provider route is one artifact away" — the M01/M19 pattern Q05 names.
2. **It omits the S039-documented real prerequisite.** Snapshot lines 16–20: "The provider requires a separately supplied headless JADX MCP JAR 0.7.1 and Java 17 or newer. `REA_JADX_MCP_JAR` selects the absolute JAR path; `JAVA_HOME` can select Java. REA setup does not install or configure that JAR, and doctor provider scopes cover Hopper/Ghidra rather than JADX." Host probe confirms this is configuration, not capability: `/usr/bin/jadx` → `1.5.6`; `REA_JADX_MCP_JAR=/home/vgpnk/.local/opt/jadx-headless-mcp/jadx-headless-mcp-0.7.1-all.jar`. No `inspect_android_package` call is recorded anywhere in the round — the entry states "this lane ran no provider" (entry:135) and "no producer is called" (entry:11), and the lesson contains no provider run.
3. **Post-flip contradiction.** `README:61` defines the section as "Ground being explored and not yet held"; `claims.md:25-28` flips C05 → held. Leaving 69–70 makes the README assert C05 both held and not held, and keeps a provider-presence claim alive for a surface the entry explicitly excludes (entry:6, entry:135). The frozen probe cannot see this: `K_ROW C05` keys on the table row only, so the counter prints `held` with the defect still in the file.

Required at admission (same commit as the row flip): delete the C05 bullet from `## Frontier`, or rewrite it with the C07 caveat, e.g. "C05 provider route — `inspect_android_package` requires a separately supplied JADX MCP JAR 0.7.1 and Java 17; the CLI/JAR are configured, but presence is not readiness: no provider call has been made." The bullet is not a table *row*, so this does not violate `claims.md:28` ("No other README row changes").

Note the presence statement itself is currently true (`jadx --version` → `1.5.6`); the finding is the implication and the now-false "needs an authored APK fixture", not a fabricated install.

### F2 — Medium-Low — S039 anchor "line 5" does not resolve; the quoted sentence starts at line 7

`entry:2`, `lesson:13` and `SOURCES.md:53` all record the S039 anchor as "line 5". In the 34-line snapshot, `sed -n '5p'` prints `older server.`; `grep -n "Start with"` prints `7:Start with \`inspect_android_package\` ...`; the quoted sentence runs lines 7–8. The fence sentence in `entry:135` and the registry row rest on this pointer, so an auditor following it lands on unrelated text. Correct to "lines 7–8" (content itself matches word-for-word). This is a pointer defect, not a claim defect, and does not by itself block Q05.

### F3 — Low — Q-map Q05 rationale is overbroad

`entry:145`: "no readiness or capability claim is made; §Cross-lane scope note fences the provider route to S039 documentation scope." The entry does make probed behavioural claims (the recheck: exit 0, 15 lines, stdout digest) and describes manual readout actions. Adopt the house phrasing used at `corpus/knowledge/round-64-firmware-region-byte-evidence.md:213` — "no tool, provider or host readiness, availability or capability" — so a later reader does not construe the row as "the entry contains no capability statements at all". Substance of the row is accurate; Q05 still passes.

## What passed

- **Entry body: no positive readiness/capability claim.** A term sweep (`ready|readiness|capab|availab|present|jadx|provider|install|execut|valid|works|supports|installed|on PATH`) over the entry returns only negative fences or required Q-map rows: entry:6 ("Not covered: … provider (`inspect_android_package`) readiness or output"), entry:11 ("no producer is called"), entry:127 ("nothing about install validity, signature blocks, dex program validity or any provider's behavior is claimed"), entry:131 ("Generalization to other APKs, other AXML producers or the `inspect_android_package` provider would need its own evidence"), entry:135. No sentence asserts a tool, provider or host is ready, available or capable.
- **§Cross-lane scope note does the required work.** Entry:133-135: "The provider route (`inspect_android_package`, JADX prerequisites) is documented scope from S039 only; this lane ran no provider and makes no readiness claim (Q05 fence)." Verified against the snapshot's documentation-only bytes (lines 3–20) and against `SOURCES.md:53` ("not provider execution on this host"). The coverage-map (entry:6) carries the same exclusion.
- **Lesson clean.** The only provider reference is the S039 documentation row (`lesson:13`); `lesson:21`'s "verified present" refers to Evidence IDs inside saved run bytes, not host capability. No readiness statement anywhere in the lesson.
- **No README change landed this round** (row still `frontier` at `README:34`; diff vs HEAD empty), so C1's "README not flipped" build state is honest.
- **The one behavioural claim in the entry was probed and reproduces exactly:**

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin && python3 -B corpus/fixtures/apk-r65/readout.py
exit=0
lines=15
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247  -
```

  This matches the header `recheck:` digest and §Reproduce (entry:5, entry:158-161). `python3 -V` → `Python 3.14.8`, matching `verified-at` (entry:4).

## Residual risk and verification gaps

- Provider readiness stays unprobed by design. My probe covers CLI/JAR/env presence only (`jadx 1.5.6`; `REA_JADX_MCP_JAR` set); I did not call `inspect_android_package`, which would be a provider probe outside this read-only lane and would need its own command/date/Evidence ID.
- F1 is invisible to the frozen counter (row-keyed), so only an explicit README edit at flip time prevents a self-contradicting README.
- F2 concerns only S039; S038/S032/S034 anchors were not re-verified here (Q01/Q11 lanes).
- Q05 is one of Q01–Q13; admission still requires the other fresh-seat decisions.

## Decision

Q05 on the entry: **PASS**. Recommendation: **ADMIT**, contingent on F1's README edit landing with the C05 flip and F2's anchor correction (F3 optional wording fix). No readiness or capability claim blocks the entry.

Tooling: nothing installed or upgraded; no pacman/jj/git mutation; the only write is this report.
