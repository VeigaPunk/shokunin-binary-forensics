# exec-lang-ledger — verify_icon_languages.py ROOT/HIST fix

Lane: `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/revenger-shokunin` (branch `kaika/round`, base `8bbcb4e`)
File changed: `corpus/verify_icon_languages.py` only. No fixture/saved-record bytes changed; no git mutation.
Pattern source: commit `7c3ce19` on `corpus/verify_named_multi_icon_states.py` — `ROOT` (`__file__`-relative) reads bytes; immutable `HIST` supplies expected artifact path and receipt-command identity.

## Change

- Added `HIST=Path('/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus')` after `root` (line 9-10), with the same provenance comment as `7c3ce19`.
- `check(r)`: added `hist=HIST/f'fixtures/pe-r{r}/fixture.exe'` (line 121). Bytes still read via `fixture=root/...`.
- Line 130: `artifact.path` expected value changed `str(fixture)` → `str(hist)`.
- Lines 143-145: receipt check now also requires `receipt['command']==f'npx -y rea-agents@6.4.0 inspect-pe-resources {hist} --format json'`. Previously the command field was not compared at all; this strengthens, not weakens.

Every other assertion untouched; the forged-selection rejection in `main()` is unchanged.

## Command log (exit code; last output line)

All `python3` runs used `-B`. Lane-root runs: `cd` = lane root above.

| # | Command (cwd) | Exit | Last output line |
|---|---|---|---|
| B1 | `python3 -B corpus/verify_icon_languages.py --self-test` (lane root) — BEFORE | 1 | `AssertionError: r47: artifact` |
| B2 | `python3 -B corpus/verify_icon_languages.py` (lane root) — BEFORE | 1 | `AssertionError: r47: artifact` |
| A1 | `python3 -B corpus/verify_icon_languages.py --self-test` (lane root) — AFTER | 0 | `PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED` |
| A2 | `python3 -B corpus/verify_icon_languages.py` (lane root) — AFTER | 0 | same PASS line |
| A3 | `cd / && python3 -B <abs>/corpus/verify_icon_languages.py` | 0 | same PASS line |
| A4 | `cd / && python3 -B <abs>/corpus/verify_icon_languages.py --self-test` | 0 | same PASS line |
| A5 | `cp -r corpus` → `/tmp/revenger probe Ω/corpus` (space + `Ω`), `python3 -B corpus/verify_icon_languages.py` (cwd copy) | 0 | same PASS line |
| A6 | same copy, `--self-test` | 0 | same PASS line |
| F1 | Temp copy: forge `round-47/inspection.raw.json` `normalized_result.artifact.path` → current copy path | 1 | `AssertionError: r47: artifact` |
| F2 | Temp copy: forge `round-47/producer-receipt.json` `command` → current copy path | 1 | `AssertionError: r47: receipt` |
| F3 | Temp copy: forge `round-47/inspection.raw.json` `resources[2].language.id` 1036→1033 | 1 | `AssertionError: r47: resources` |

Note: `--self-test` is not parsed by the script (no argparse); both modes execute `main()` identically. Observed identical behavior in both modes before and after — consistent with C1's recorded symptom.

All temp copies deleted: `ls -d "/tmp/revenger probe Ω" /tmp/forge-*` → `No such file or directory` for all four.

## Input SHA-256 table — before and after identical

Command (lane root): `sha256sum corpus/fixtures/pe-r4{7,8,9}/fixture.exe corpus/live/runs/round-4{7,8,9}/inspection.raw.json corpus/live/runs/round-4{7,8,9}/producer-receipt.json`

| File | SHA-256 (before = after, exit 0) |
|---|---|
| corpus/fixtures/pe-r47/fixture.exe | cc02c78b44883f2217b7a8f82fa6fafc990ae6d0ca71f0eab8a3fbc4f2ba44ba |
| corpus/fixtures/pe-r48/fixture.exe | dc6483a985f12dbc0da4122db64565ed76c14a5e76ea8758658b4a54c35bc129 |
| corpus/fixtures/pe-r49/fixture.exe | d26b165ee497da494e1b5605a72877597030de53f94eba674c905bffbb079114 |
| corpus/live/runs/round-47/inspection.raw.json | e12ff95b78b57fde1bdc4ec7acf8142b2e4d242c2bfa7ae82307760be260e65c |
| corpus/live/runs/round-48/inspection.raw.json | 3a21b0e9ff72140360f72229810f0787265e07b86ec9af5148708128ade53325 |
| corpus/live/runs/round-49/inspection.raw.json | 202e95f029461ffd8dd092114bcdcc88f654b85cbee226036dd309fb96e4830a |
| corpus/live/runs/round-47/producer-receipt.json | 3b5d3bdaad18cf7ab0c34643851e205353a979dff08133f48f54f0617e558ac5 |
| corpus/live/runs/round-48/producer-receipt.json | 7499a494eff905e2e3636f4a266ba23aec3e352f629d5de59bd4d1a2978a9e19 |
| corpus/live/runs/round-49/producer-receipt.json | 7e6f14bb3bee90524d042c4d75b0de63e952e835f99b81d5b399165351985e15 |

## Diff (`git -C <lane> diff -- corpus/verify_icon_languages.py`, exit 0)

```
corpus/verify_icon_languages.py | 8 ++++++--
1 file changed, 6 insertions(+), 2 deletions(-)
@@ -6,6 +6,8 @@
+# Historical producer corpus; identity for saved artifact paths/receipt commands only, never read through it.
+HIST=Path('/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus')
@@ -116,6 +118,7 @@ EXPECTED = {
+    hist=HIST/f'fixtures/pe-r{r}/fixture.exe'
@@ -124,7 +127,7 @@ def check(r):
-    require(record['normalized_result']['artifact']==dict(path=str(fixture),sha256=expected_hash,bytes=1536),f'r{r}: artifact')
+    require(record['normalized_result']['artifact']==dict(path=str(hist),sha256=expected_hash,bytes=1536),f'r{r}: artifact')
@@ -138,7 +141,8 @@ def check(r):
-            and receipt['stdout_sha256']==H(raw_bytes),f'r{r}: receipt')
+            and receipt['stdout_sha256']==H(raw_bytes)
+            and receipt['command']==f'npx -y rea-agents@6.4.0 inspect-pe-resources {hist} --format json',f'r{r}: receipt')
```

## Residual observations

- Sibling `corpus/verify_multi_icon_states.py` carries the same bug (`AssertionError: r42: artifact` per C1) and is assigned to a different ticket; `git status` shows it already `M` in this worktree — not touched here.
- No other failures surfaced after the path fix: PASS line asserts 3/3 states, 2/2 exact one-byte deltas, forged-selection rejection.
- HIST is compared-only; `check()` never calls `hist.read_bytes()` — verified by construction and by the relocated-copy run (HIST path does not exist under `/tmp`, yet PASS).
