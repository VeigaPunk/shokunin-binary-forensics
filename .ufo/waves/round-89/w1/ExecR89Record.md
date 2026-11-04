# ExecR89Record — C2 android-family producer record (round 89, wave 1)

Seat: ExecR89Record. Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin` at freeze `2b017fa3…`/`c84339c` context. Scoped target: the C2 android-family producer record from the current REA provider on `corpus/fixtures/apk-r65/fixture.apk`, twice, byte-identically. Read `reports/round-89/claims.md` first; godspeed framing.

## Files changed (all inside my named scope)

- `corpus/live/runs/round-89/inspection.json` — 4303 bytes, the **exact stdout bytes** of run1 (`cmp`-checked against the captured stdout before landing; sha256 `01af3141d79027a3bae53b6482779d3e9c89446ab6ca09b408a6cb266f321c76`). No reformatting.
- `corpus/live/runs/round-89/receipt.json` — command line, cwd, rea version, provider id/name/version read from the record (`jadx` / "JADX headless" / `0.7.1`), exit codes (0/0), stderr bytes (0/0), wall times (2.464 s / 2.276 s), both stdout sha256 values, cmp verdict (DIFFER), the record's `evidence_id`, the volatile-field enumeration, and the oracle result.
- `corpus/live/runs/round-89/LEDGER.md` — one page in the `corpus/live/runs/round-77/LEDGER.md` shape: what was run, observed vs inferred vs unknown, the producer's verbatim `limitations` list, the Q09 statement (reproducible producer output, not provenance/authenticity), full oracle output, environment audit, and the pre-run env-gate observation.
- `.ufo/waves/round-89/w1/ExecR89Record/` — retained receipts (run1/run2 stdout+stderr bytes, receipt.json, oracle log).

No other lane byte touched. No git/jj command of any kind run. No `.ufo/state`, `.scratch`, `MANIFEST.json`, or sibling repo access. No tool installed or upgraded (nothing was needed; tooling-directive record: zero installs).

## What was run

1. `rea --version` → `6.7.0` exit 0; `jadx --version` → `1.5.6` exit 0; `command -v rea` → fnm node path; `command -v jadx` → `/usr/bin/jadx`; `REA_JADX_MCP_JAR` → set on this host (jar present, 42619858 bytes).
2. From the lane root, twice, stdout/stderr captured separately into `TMPDIR=/fast/scratch/hyaku/revenger-r89/ExecR89Record`: `rea inspect-android-package corpus/fixtures/apk-r65/fixture.apk --format json`.
3. run1: exit 0, 2.464 s, stderr 0 bytes, 4303 bytes, sha256 `01af3141…21c76`. run2: exit 0, 2.276 s, stderr 0 bytes, 4303 bytes, sha256 `5bbdd189…2ce00`. `cmp` differs at char 20.
4. run1's exact bytes landed as `inspection.json`; oracle re-run against the landed path.

## Acceptance status

- inspection.json is the exact stdout bytes — **MET** (cmp-verified).
- Oracle prints `ORACLE OK (19/19 checks)` exit 0 over the landed file — **MET** (run against `corpus/live/runs/round-89/inspection.json`, full 19-check output pasted in LEDGER.md and below).
- receipt.json carries every required field — **MET**.
- both runs identical — **NOT MET (measured producer property)**: the two stdouts are byte-non-identical. The complete delta set (full JSON-tree walk, equal 4303-byte outputs) is exactly four producer-side volatile sources: per-run `evidence_id`; the mkdtemp-style private runtime dir `rea-android-XXXXXX` (in `raw_result.calls[1].input.path`, that run's `apk_path`, and `raw_result.loaded.apk_path`); JVM map key ordering in `raw_result.calls[0]` (same five keys, different order); `load_duration_ms` (175 vs 170). `normalized_result` is identical across runs. No knob pins them: the command takes only `<path>`, globals are format/filter only, and the `rea-agents` scripts expose no environment pin for the android runtime dir. Nothing was normalized, retried-until-equal, or post-edited — the DIFFER verdict is recorded in receipt.json and LEDGER.md. Under rea 6.7.0 + jadx-headless-mcp 0.7.1, reproducibility is oracle-verdict reproducibility, not byte reproducibility (same volatility class the round-77 browser ledger disclosed).
- record carries no env values — **MET (narrow reading)**: the record's `environment` field is `null` — no environment-variable map, no key dropped, bytes remain exact stdout. It does carry host-derived JVM facts (`raw_result.calls[0]`: max_heap_bytes 8124366848, available_processors 32, java_version 21.0.13; `normalized_result.engine.heap_limit_mib` 7748), disclosed and classified low-sensitivity by SentinelR89.

## Full oracle output (over the landed file)

```
check ok: fixture sha256 05d2280f847497cf
check ok: fixture size 947 bytes
check ok: member set ['AndroidManifest.xml', 'META-INF/MANIFEST.MF', 'classes.dex']
check ok: member byte lengths match the build recipe
check ok: member digests match truth.json
check ok: operation inspect_android_package
check ok: provider id jadx
check ok: provider version present
check ok: evidence_id shape ev_<64 hex>
check ok: subject digest == fixture sha256
check ok: subject format apk
check ok: package_name com.example.r65
check ok: manifest declares versionCode="1"
check ok: manifest declares versionName="1.0"
check ok: manifest status complete
check ok: class_count == DEX class_defs_size (0)
check ok: resource_count == 3 members
check ok: permissions empty
check ok: signature_verification not_performed
ORACLE OK (19/19 checks)
```
(exit 0)

## Pre-run observation (env gate)

A first attempt pair in a non-interactive exec environment with `REA_JADX_MCP_JAR` unset failed exit 1 with the producer's `capability_unavailable` payload (`jar_configured: false`, 686 bytes, both attempts byte-identical, sha256 `4d0e6ea59823c97242bfa75b009952dfe8c1e9c63bc1793c09308d6482167330`). The r83–r88 android hard gate is real whenever the jar variable is unset; with it set (this host) it does not hold. These payloads are not part of the record.

## Post-yield L1 directive compliance (RevengerR89)

- Frozen equality kill treated as FAIL everywhere: receipt.json now carries `c2_admission_status: NOT ADMITTED`; LEDGER.md opens with a rejection status block; nothing was normalized and no identity was claimed.
- Both raw byte outputs retained in `.ufo/waves/round-89/w1/ExecR89Record/` (run1.json sha256 `01af3141…21c76`, run2.json sha256 `5bbdd189…2ce00`, both stderr 0 bytes) alongside `receipt.json` and `oracle-on-landed.log`.
- Timestamps: only wall durations were captured at run time (2.464 s / 2.276 s). Absolute start/end UTC stamps were not captured and are unrecoverable — the scratch mtimes went with the contract-mandated scratch deletion and the session transcript carries no timestamps. receipt.json discloses this explicitly; nothing reconstructed or estimated. PIDs likewise not captured.

## Risks / blockers

- The frozen C2 kill rule (c) text ("the two independent producer runs must be byte-identical") is not satisfiable by this producer version as measured; the L1 must decide whether the oracle-verdict reproducibility + volatile-field enumeration satisfies the claim or whether the round needs a producer-side determinism fix outside my scope. I did not rewrite any frozen predicate.
- `evidence_id` derivation was not examined (per-run variance only measured) — labeled unknown in the LEDGER.

## Coordination

Answered `CriticR89Claims` (final raw bytes preserved unnormalized; delta set enumerated). Paths delivered to `SentinelR89`, `MutR89Oracle`, and `ReviewerR89C2` for their audits. Scratch `/fast/scratch/hyaku/revenger-r89/ExecR89Record` deleted after receipts were copied into the wave dir.
