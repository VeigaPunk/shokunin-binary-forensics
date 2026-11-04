# SentinelR90 — sensitivity review of the round-90 android producer record

Round 90, attempt 1, wave w1. Read-only review: no lane bytes changed except this report dir and the `Report:` trailer file. No tools installed or upgraded.

## Inputs (sha256 measured this seat)
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-90/w1/ExecR90Producer/run1.json`: 4309 B, `9d665ffbc8674d41675b164f8d4cc70457e00a0b94eee2de9ab4d6b010249e12`
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-90/w1/ExecR90Producer/run2.json`: 4309 B, `214094fbe04883e1f1879f5d314397899cdbf43a66d92607b9a0f560ec322f38`
- Baseline: `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-89/rejected-android-record/receipt.json` and its `inspection.json`.
- Precedent: the landed records under `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/`.

## Method
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-90/w1/SentinelR90/scan.py` walks every JSON leaf and key. It also re-parses string leaves that hold JSON text, such as the `raw_result.calls[*].response.content[0].text` payloads, so those are scanned too. It checks each value for:
  - home paths and `/run/user` paths
  - the username `vgpnk`
  - IPv4 and IPv6 addresses, URL hosts and internal FQDNs
  - AWS, GitHub, Slack, OpenAI and Anthropic key shapes, JWTs and PEM blocks
  - `secret=`/`token:` key-value shapes, `VAR=value` assignments and emails
  - the host nodename
  - the seat's own environment-variable values (6 characters or longer)
  - every absolute path outside `/fast/scratch/hyaku/revenger-r90/`

  Output is in `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-90/w1/SentinelR90/scan-receipt.log`.
- Literal counts were run against values from the producer's own `env.log`: the `fnm_multishells` PATH entry, `/run/user`, the `REA_JADX_MCP_JAR` jar path, `.local/opt`, `REA_`, `JAVA_HOME`, `PATH=`, nodename `plazir27`, `localhost`, `127.0.0.1` and the fnm PID `1981588`. Every one counted 0 in both runs.
- Each run was diffed leaf-by-leaf against the r89 record. The key sets are identical: no new or dropped key. The only changed leaves are the evidence id, the `rea-android-*` runtime directory (3 sites), the order of the JVM-map keys and `load_duration_ms` (620 in run1, 643 in run2).
- `reports/round-90/norm_eq.py run1.json run2.json` printed `NORM_EQ=identical` on scratch copies.

## Findings

| # | Finding | Where (run1 = run2) | Class | Baseline (r89) / precedent |
|---|---|---|---|---|
| 1 | The OS username and home path appear in the absolute fixture path `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/apk-r65/fixture.apk` | `$.subject.local_path` (only `/home/` and `vgpnk` occurrence: 1 each) | low | Same leaf in r89 `inspection.json`, and r89 `receipt.json` `cwd`. Already landed in `corpus/live/runs/` with `/home/vgpnk/...` (e.g. round-10 `extraction.json`, `20261012T16*`), and other records carry `C:\Users\jpvei\...` |
| 2 | Host JVM facts: `max_heap_bytes` 8124366848, `available_processors` 32, `java_version` 21.0.13, and the derived `heap_limit_mib` 7748 | `$.raw_result.calls[0]...text`, `$.normalized_result.engine.heap_limit_mib` | low | Identical values in r89, which r89's receipt disclosed and SentinelR89 classed low. Hardware sizing plus a public JDK version, no identifier |
| 3 | Scratch runtime path with the seat name: `/fast/scratch/hyaku/revenger-r90/ExecR90Producer/rea-android-{2CB2xW,9xcZqQ}/target.apk` | `$.raw_result.loaded.apk_path`, `calls[1].input.path`, `calls[1]...text.apk_path` | none | Inside the sanctioned scratch path. It is the declared volatile V2 (r89 had `revenger-r89/ExecR89Record`) |
| 4 | Environment-variable values | `$.environment` is `null`; no value from `env.log` appears anywhere | none | Same as r89 (`record_environment_field: null`) |
| 5 | Tokens, keys, credentials, JWT, PEM, emails | none | none | none in r89 |
| 6 | Hostnames and IPs | none (nodename absent). The only URL host is the public XML namespace `schemas.android.com` (4 hits per run, in manifest text) | none | same namespace in r89 |
| 7 | Public provenance: `jar_sha256`, `bridge_sha256`, `source_revision` 5844800a…, `evidence_id` | engine and raw_result fields | none | Same class in r89. These are content digests or ids, not secrets |
| 8 | (Outside the record) The producer's wave `env.log` carries `/run/user/1000/fnm_multishells/1981588_.../bin/rea` and `/home/vgpnk/.local/opt/jadx-headless-mcp/...jar` | `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-90/w1/ExecR90Producer/env.log` | low | Not part of the record and does not affect landing. If it is committed it adds a UID and a fnm PID, nothing secret |

Encoding: both runs are ASCII-only, with no control bytes outside `\t\n\r`.

Compared with the baseline, the round-90 record adds no new sensitivity class. Every non-"none" item (1 and 2) is the same leaf with the same value class that r89 already disclosed and that earlier landed records already carry.

## Proposed (not applied; the record must land byte-exact or not at all)
- Optional, for the receipt only: restate finding 1 and finding 2 in the round-90 receipt as r89 did. That is disclosure, not redaction. Any edit to the record bytes would break kill rule (c), which requires the landed record to be run1's exact stdout.

LAND_OK: yes — the record has only low-class disclosures that r89 already disclosed and earlier landed records already carry: the home path and username in `subject.local_path`, and host JVM sizing. It has no environment values, tokens, keys, credentials, hostnames or IPs, so run1.json may land byte-exact and unmodified.

VERDICT: LAND_OK yes — the r90 android record (run1 sha256 9d665ffb…, run2 214094fb…) carries only low-class disclosures (home path/username, JVM sizing), both identical to the r89 baseline; nothing medium or high.
