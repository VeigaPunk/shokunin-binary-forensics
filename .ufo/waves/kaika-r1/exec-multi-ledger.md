# exec-multi-ledger — C1 fix: corpus/verify_multi_icon_states.py

Lane: `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/revenger-shokunin` — 2026-10-19

## Change applied (7c3ce19 ROOT/HIST pattern)
`HIST = Path('/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus')` added after `root`
(now line 9-10). `hist` supplies the saved artifact-path identity (line 133) and the receipt-command
identity (new line 142-144); bytes still read from `root` (line 123-126). No assertion weakened;
the receipt check was *strengthened* — `receipt['command']==command` was added because the previous
line never compared the saved command against anything (drift risk). Receipts carry only
`command/exit_code/fixture_sha256/stdout_sha256/evidence_id` keys (no `duration_seconds` here,
unlike the named file).

## Commands and results
All run with `python3 -B`. Before = base commit state; after = this edit.

| # | cwd | command | exit | last output line |
|---|-----|---------|------|------------------|
| 1 | lane root | `python3 -B corpus/verify_multi_icon_states.py --self-test` (before) | 1 | `AssertionError: r42: artifact` |
| 2 | lane root | `python3 -B corpus/verify_multi_icon_states.py` (before) | 1 | `AssertionError: r42: artifact` |
| 3 | lane root | `python3 -B corpus/verify_multi_icon_states.py --self-test` (after) | 0 | `PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED` |
| 4 | lane root | `python3 -B corpus/verify_multi_icon_states.py` (after) | 0 | same PASS line |
| 5 | `/` | `python3 -B <abs lane path>/corpus/verify_multi_icon_states.py` | 0 | same PASS line |
| 6 | `/` | `python3 -B <abs lane path>/corpus/verify_multi_icon_states.py --self-test` | 0 | same PASS line |
| 7 | `/tmp` | copy `corpus` → `/tmp/revenger çopy w2/corpus` (space + non-ASCII `ç`), run `--self-test` | 0 | same PASS line |
| 8 | `/tmp` | same copy, plain run | 0 | same PASS line |
| 9 | `/tmp` | probe 1: forge `normalized_result.artifact.path` to current copy path, run `--self-test` | 1 | `AssertionError: r42: artifact` |
| 10 | `/tmp` | probe 2: forge `producer-receipt.json` `command` to current copy path, run `--self-test` | 1 | `AssertionError: r42: receipt` |
| 11 | `/tmp` | probe 3: forge `icon_groups[0].images[1].resource_id` 2→99, run `--self-test` | 1 | `AssertionError: r42: icon_groups` |

Copy dir and all probe copies deleted after the runs. `--self-test` has no dedicated flag path in
this script — both modes run `main()` identically (observed: identical output/exit in rows 3 vs 4).

## Input SHA-256 table — before ≡ after (identical)
| file | sha256 |
|------|--------|
| fixtures/pe-r42/fixture.exe | 3ab5008b436eb4facd3966767a507fa4b1625160532585a09a6af2f752b38941 |
| fixtures/pe-r43/fixture.exe | 146bdde3ec3ce9f23b75b31f7a9d2fc0cbc8826f2a5d239a83fd82694f4c31a2 |
| fixtures/pe-r44/fixture.exe | bb2680c1ceaa3ce6e4921e078e2548f06f164d9598da2bff6c895890b73bc5fb |
| fixtures/pe-r45/fixture.exe | 1d526ab14ba29a133cafd720395920b0067d8d00c40a5e1216e097272c176669 |
| live/runs/round-42/inspection.raw.json | 7163c758c776f8aa71543ae16be671d28e241abf9a310afd0a5ca846121d4b9c |
| live/runs/round-42/producer-receipt.json | 05bf8bf6dd33719a3db6f6d9ff29a894d8191c627e14c7e746611f7c882119de |
| live/runs/round-43/inspection.raw.json | d84d8db6351c690918ae1b35fde4c8a099a46f375758930aa3438d468cf48d49 |
| live/runs/round-43/producer-receipt.json | 7178a0721a1e9df6dc6e92a3336c3fe4329e7a5c3d4d3a4f8a2534bbbe6b9315 |
| live/runs/round-44/inspection.raw.json | 2a14dc2af922b6ba0645087782f7eab5fac4b300954b3a25625cbf1b4d5e2e19 |
| live/runs/round-44/producer-receipt.json | bddd2faac42e6475cb613a7d187f3178a9d3ad334b5ef96aca8e10354401be7f |
| live/runs/round-45/inspection.raw.json | 20fd361deef320f3e57036a850d34f2fb5e711de317e816b40b4a50f60a01ec7 |
| live/runs/round-45/producer-receipt.json | ef67f2a1080e9e80d4b745f49090b011bc0d4c55e9e6bb258b145ad436fa4beb |

Command: `sha256sum corpus/fixtures/pe-r4{2,3,4,5}/fixture.exe corpus/live/runs/round-4{2,3,4,5}/{inspection.raw.json,producer-receipt.json}` run before and after; tables byte-identical.

## Diff (`git diff -- corpus/verify_multi_icon_states.py`)
```
+# Historical producer corpus; identity for saved artifact paths/receipt commands only, never read through it.
+HIST = Path('/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus')
...
+    hist = HIST / f'fixtures/pe-r{round_id}/fixture.exe'
...
-    require(... artifact==dict(path=str(fixture),...)
+    require(... artifact==dict(path=str(hist),...)
...
+    command = f'npx -y rea-agents@6.4.0 inspect-pe-resources {hist} --format json'
+    require(receipt['command']==command and receipt['exit_code']==0 and ...)
```
6 insertions, 2 deletions.

## Residuals
- No other failures after the path fix: positive run reaches the final PASS line including the
  in-script forged-second-match rejection.
- Forged-claim rejections retained: probes 9–11 each exit 1 with a distinct AssertionError.
- Note: persistent-shell `cd` hook (`__fnmcd`) failed once on the non-ASCII temp path; reran with
  explicit paths/cwd — no effect on the script under test.
