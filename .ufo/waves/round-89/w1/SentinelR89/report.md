# SentinelR89 — round-89 security review (credentials and host-sensitive values)

Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`. Scope: the producer record,
its receipts, the two new instruments, and the r89 reports. Read-only. No commit,
push, or mutating git/jj command. No tool installed or upgraded. Scratch
`/fast/scratch/hyaku/revenger-r89/SentinelR89` deleted after the receipt copy.

## Verdict

- **Credential material: none found** in any scanned file (pattern set in §4).
- **Record bytes** `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-89/inspection.json`
  (sha256 `01af3141…21c76`, 4303 B, matches `receipt.json`) **can land as-is.** Editing
  it to scrub paths would break the byte pin the frozen claim and receipt name, so no must-fix edit is recommended.
- **Landing condition (text only, not a blocker to the bytes):** `LEDGER.md` and
  `receipt.json` must add one disclosure sentence naming the host-derived values in
  §2 (SEC-01, SEC-02, SEC-09). The current `LEDGER.md` environment paragraph covers
  only `environment: null` and the JVM facts. It does not name `subject.local_path`
  (username `vgpnk`) or the scratch `apk_path`. The owner's narrow-reading edit
  (`receipt.json:42`, `LEDGER.md:51-59`) is accepted; this is the one remaining gap.
- **Instruments (`census_reprobe.py`, `oracle_check.py`) can land as-is.** Neither
  prints env values, neither hardcodes a host path, and the census gate reads only
  `mcpServers → rea → args`.

## 1. Inspection record: field-by-field (`inspection.json`, single line)

| field (JSON path) | value class | ruling |
|---|---|---|
| `environment` | `null` (confirmed by `json.load`) | harmless |
| `subject.local_path` | absolute checkout path containing OS username `vgpnk` | acceptable with disclosure (SEC-01) |
| `raw_result.loaded.apk_path`, `raw_result.calls[1].input.path`, `raw_result.calls[1].response` text | seat scratch path `/fast/scratch/hyaku/revenger-r89/ExecR89Record/rea-android-ugg7mp/target.apk`; reveals seat name and a per-run mkdtemp dir; dangles after scratch deletion | acceptable with disclosure (SEC-02) |
| `raw_result.calls[0]` response: `max_heap_bytes` 8124366848, `available_processors` 32, `java_version` 21.0.13; `normalized_result.engine.heap_limit_mib` 7748, `worker_count` 1 | host hardware and JVM facts | acceptable with disclosure (SEC-03); already disclosed in `LEDGER.md:51-59` and `receipt.json:42` |
| `raw_result.server`, `raw_result.bridge_sha256`, `raw_result.jar_sha256`, `evidence_id`, `subject.digest.sha256`, `normalized_result.engine.artifact_sha256`, `normalized_result.engine.source_revision` | 64-hex and 40-hex hashes and identifiers (token-shaped by length, not credentials) | harmless (SEC-06) |
| `parameters.path`, `locations[0].path`, `analysis_profile`, `evidence_links` | relative paths or null; no host path | harmless |
| `raw_result.calls[2..3]` (`get_app_info`, `get_android_manifest`) | fixture-authored AXML content (`com.example.r65`, version attrs) | harmless |
| `limitations` | producer prose | harmless |

No env-var value, token, or key-shaped string appears in the record.

## 2. Findings table

Rule IDs: SEC-nn. Paths absolute. "Ruling" is one of: must-fix before landing,
acceptable with disclosure, harmless.

| Rule | file:line (or JSON path) | value class | ruling |
|---|---|---|---|
| SEC-01 | `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-89/inspection.json:1` `subject.local_path` | absolute lane path with OS username `vgpnk` | **acceptable with disclosure.** Exact producer bytes are pinned (receipt `landed_bytes_exact`, freeze byte-identity). The same path already sits in the frozen `reports/round-89/claims.md:4,21`, and `carry-in.md:10`. The oracle never reads it. **Condition:** name it in LEDGER. |
| SEC-02 | `inspection.json:1` `raw_result.loaded.apk_path`, `raw_result.calls[1].input.path`, `raw_result.calls[1].response` | seat scratch path including seat name `ExecR89Record` and mkdtemp dir `rea-android-ugg7mp` | **acceptable with disclosure.** Per-run volatile; already in `receipt.json` `volatile_field_set`. Path dangles after scratch deletion. **Condition:** name in LEDGER. |
| SEC-03 | `inspection.json:1` `raw_result.calls[0]`; `normalized_result.engine.heap_limit_mib` | JVM heap size, CPU count, Java version | **acceptable with disclosure.** Host hardware and runtime fingerprint, not a secret. Disclosed in LEDGER:51-59 and receipt:42. |
| SEC-04 | `inspection.json:1` `environment` | would be an env-var map | **harmless.** `null`; owner's narrow reading ("no env map, not no host facts") is correct and adopted. |
| SEC-05 | `inspection.json:1` `locations`, `parameters.path` | relative paths only | **harmless.** |
| SEC-06 | `inspection.json:1` `evidence_id`, `*sha256`, `source_revision`, `bridge_sha256`, `jar_sha256` | hash and revision identifiers, token-shaped by length | **harmless.** Content hashes, not credentials. Note: the generic 32+-char token regex matches these by design; they were classified manually. |
| SEC-07 | `receipt.json:5` `cwd` | absolute lane path with username | **acceptable with disclosure.** Same class as SEC-01. **Condition:** name in LEDGER. |
| SEC-08 | `.ufo/waves/round-89/w1/ExecR89Record/run1.json`, `run2.json` (retained raw producer bytes) | same paths as SEC-01/02 | **acceptable with disclosure.** Not record bytes. Retained by the seat as evidence; no change recommended. |
| SEC-09 | `.ufo/waves/round-89/w1/ExecR89Record/invocation-driver-transcript-excerpt.md:14,20,22` | `cd /home/vgpnk/...`; `REA_JADX_MCP_JAR=[/home/vgpnk/.local/opt/.../jadx-headless-mcp-0.7.1-all.jar]` (env value printed verbatim); `ls -l` listing with owner `vgpnk` and mtime | **acceptable with disclosure.** The only place an env-var value is printed. It is a tool path, not a credential, and the same value is in `reports/round-89/claims.md:21`. Largest disclosure surface of the set. **Condition:** LEDGER must say the transcript carries the jar path and listing. |
| SEC-10 | `reports/round-89/claims.md:4,21` | lane path; jar install path with username | **acceptable with disclosure.** Frozen at `c84339c`; must not be rewritten. |
| SEC-11 | `reports/round-89/carry-in.md:10` | fleet-root command with username | **acceptable with disclosure.** Frozen content from the census command. |
| SEC-12 | `corpus/live/runs/round-89/LEDGER.md:13` | `/usr/bin/jadx` tool location | **harmless.** |
| SEC-13 | `corpus/live/runs/round-89/LEDGER.md:124-128` | producer error payload sha256 `4d0e6ea5…` | **harmless.** Hash; the payload is not in the record. |
| SEC-14 | `corpus/census_reprobe.py:51` `MCP_JSON = Path.home() / ".omp/agent/mcp.json"` | location of a file that may hold env secrets | **harmless.** Location only, no value. |
| SEC-15 | `corpus/census_reprobe.py:107-120` `mcp_spec()` | reads whole `mcp.json` into memory, then only `mcpServers`→`rea`→`args` | **harmless.** Verified by `mcp-disclosure-probe.log` (§3). No env, no other server's args leave the function. |
| SEC-16 | `corpus/census_reprobe.py:325-332` (`--json` and text output) | prints only `rea-agents@<version>` and row ids | **harmless.** Verified: no env marker appears in stdout or stderr. |
| SEC-17 | `corpus/census_reprobe.py:80-86` `first_line()` plus `:139-143` and `:210-213` | latent echo: a version command's first stderr line that does not match `\d+(\.\d+)+` becomes the printed `does not state live value` token | **harmless today, latent hardening.** The four fixed version commands (`node --version`, `npm --version`, `unzip -v`, `zipinfo -v`) all match, so nothing echoes now. Fixing it would edit a frozen predicate, so it is routed to a future round, not this one. |
| SEC-18 | `corpus/census_reprobe.py:145-152` import probe | `sys.executable -c "import <fixed>"`; no output captured or printed | **harmless.** |
| SEC-19 | `corpus/fixtures/apk-r65/oracle_check.py:48-51, 88-128` | prints input paths the caller passed, plus record fields it already checks | **harmless.** Reads no env and writes nothing. |
| SEC-20 | `reports/round-89/*.log` (`census-red`, `census-selftest`, `junk-control`, `f4-red`, `oracle-design`, `oracle-tamper-control`, `instrument-pins`) | check names, row ids, counts, sha256 pins | **harmless.** `junk-control.log` names skill reference filenames only. |

Nothing in the table is **must-fix before landing**.

## 3. Instrument receipt: MCP isolation (`census_reprobe.py` `mcp` probe)

Probe: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-89/w1/SentinelR89/mcp_disclosure_probe.py`
(sha256 `24f99c14…b6b0`), output `…/w1/SentinelR89/mcp-disclosure-probe.log`, exit 0.
It imports `census_reprobe.py` (sha256 `c3127ffc…648a`, matches the pin in
`reports/round-89/instrument-pins.log`) and replaces `MCP_JSON` with synthetic
documents that contain marker strings, so it never opens the live
`~/.omp/agent/mcp.json`.

- Five synthetic configurations (wrapped, flat, env-only pin, other-entry-only pin, missing `rea`): all pass. Returned version matches expectations, and no marker reaches the output.
- Field-access guard: only `document.mcpServers`, `servers.rea`, `rea.args` were read.
- Full `main()` run, text and `--json`, exit 1 as designed, output contains `rea-agents@6.7.0` and no marker.

Caveat for the closure: the log line `LIVE_MCP_CONFIG_OPENED=no` is a **literal**
printed by the probe, not a measured value. The probe replaced `MCP_JSON` before
every call, so the live file was not opened by construction. I did not `strace`
the live run. The live gate was not executed by this seat.

## 4. Scan patterns and results

- Credential shapes (`sk-`/`rk-`, `ghp_`/`gho_`…/`github_pat_`, `AKIA`/`ASIA`, `xox*-`, `AIza`, JWT `eyJ…`, PEM private key, `api_key`, `access_token`, `authorization`, `bearer`, `password`, `secret`, `credential`, `1password`, `op://`, `.env`, `codex`): **no matches** in `corpus/census_reprobe.py`, `corpus/fixtures/apk-r65/oracle_check.py`, `reports/round-89/`, `corpus/live/runs/round-89/`, and `.ufo/waves/round-89/w1/ExecR89Record/` (final rescan after the owner's edit).
- Host-path and env disclosure (`/home/`, `/fast/`, `/usr/`, `/Users/`, `local_path`, `environment`, `raw_result`, `mcp.json`): hits listed in §2. No hit in `census_reprobe.py` other than the `~/.omp/agent/mcp.json` location (SEC-14).
- The 64-hex strings in the record are hashes and evidence ids (SEC-06), not credentials.

## 5. Not verified (stated, not claimed)

- The live `mcp.json` contents were not read. The gate's read-set is shown structurally, not against the live file.
- Derivation of `evidence_id` was not examined. Only its per-run variance was observed, by the producer.
- The oracle and the census gate were not rerun by this seat. Verification is the main agent's job.
- No tool was installed or upgraded. No pacman transaction was run (host guard).

## 6. Recommendation for the L1

1. Land the record bytes, `census_reprobe.py`, and `oracle_check.py` as they are.
2. Before landing `LEDGER.md` and `receipt.json`, add one sentence naming SEC-01, SEC-02, SEC-07, and SEC-09 as host-derived values, disclosed and not secrets.
3. Route SEC-17 (census token echo) to a future calibration round. Do not edit the frozen predicate this round.
