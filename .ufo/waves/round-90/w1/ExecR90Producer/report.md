# ExecR90Producer — round 90 w1, C2 android producer runs

Lane: /home/vgpnk/Projects/shokunin/revenger-shokunin (frozen claims at c7767789fe9e96bcc0d50656ad4bdce69ba3a3a9, read first).
Seat dir: /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-90/w1/ExecR90Producer/

## Environment pin (/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-90/w1/ExecR90Producer/env.log)
- rea /run/user/1000/fnm_multishells/1981588_1793727763382/bin/rea, `rea --version` 6.7.0 (path is an fnm per-shell shim dir)
- jadx /usr/bin/jadx 1.5.6; java /usr/bin/java OpenJDK 21.0.13+9
- REA_JADX_MCP_JAR set, file path /home/vgpnk/.local/opt/jadx-headless-mcp/jadx-headless-mcp-0.7.1-all.jar
- Linux 7.2.11-arch1-1; env pinned 2026-11-04T22:01:54Z; TMPDIR=/fast/scratch/hyaku/revenger-r90/ExecR90Producer

## Runs (cwd lane root, `rea inspect-android-package corpus/fixtures/apk-r65/fixture.apk --format json`, TMPDIR explicit)
| label | utc_start | utc_end | exit | stderr B | wall s | stdout B | stdout sha256 |
|---|---|---|---|---|---|---|---|
| run1 | 2026-11-04T22:02:20.690Z | 2026-11-04T22:02:27.728Z | 0 | 0 | 7.038 | 4309 | 9d665ffbc8674d41675b164f8d4cc70457e00a0b94eee2de9ab4d6b010249e12 |
| run2 | 2026-11-04T22:02:27.728Z | 2026-11-04T22:02:34.515Z | 0 | 0 | 6.786 | 4309 | 214094fbe04883e1f1879f5d314397899cdbf43a66d92607b9a0f560ec322f38 |

- run1.json / run2.json are the exact stdout bytes: `cmp` against scratch copies passed (CMP_OK); `sha256sum` of both files equals receipt.json `stdout_sha256`.
- Evidence ids: run1 ev_affae0e5ae0fb1ef295975485048faa4721ee620c99a0d72603dfaaedef1e6c5, run2 ev_d4a34332e3ca12df700b7698de453f75066ec7bfcfc79c03c21e5e013de81b37 — distinct, and neither is the r89 id ev_387c9e9c410dc40fb6a19524fcdda49a3186c4597c20e9c4a9625b3b99a588e4 (grepped from reports/round-89/rejected-android-record/).
- Provider from record: id jadx, name "JADX headless", version 0.7.1.
- Disclosure: a first pair of runs (attempt0, both exit 0, stderr 0, 4309 B each; sha 5a20c0a0…f99c / 0529afc8…0ca3) was discarded before any copy or scoring because the host `date` (uutils 0.8.0) ignored `%3N` (printed 8–9 digit fractions) and `bc` is absent, so wall seconds were not recorded. Its timing line is kept at /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-90/w1/ExecR90Producer/discarded-attempt0-timing.log. The kept pair was timed by Python (monotonic wall, UTC ms stamps). run2's start equals run1's end to the ms (sequential, separate processes).

## Information-only checks
- norm-eq.log: `NORM_EQ=identical`, exit 0. Raw diff between runs was only: evidence_id (V1), rea-android-<suffix> runtime dir in 3 strings (V2), key order in the rea_jvm_status text payload (V3), load_duration_ms 620 vs 643 (V4). Nothing outside V1–V4.
- oracle2.log: `ORACLE OK (22/22 checks)`, exit 0 on run1 (run2 also 22/22, scratch-only check).

## Audit: environment field and strings (record not edited)
- `environment` is `null` in both records.
- 49 strings per record scanned for every current env-var value (len ≥ 6) and credential patterns (token/secret/password/bearer/api key/oauth/authorization/ghp_/sk-/AKIA/PEM): no credential pattern matches.
- Env-var VALUES do appear as path substrings: TMPDIR value (/fast/scratch/hyaku/revenger-r90/ExecR90Producer) in $.raw_result.loaded.apk_path, $.raw_result.calls[1].input.path and calls[1].response.content[0].text; HOME value (/home/vgpnk) inside $.subject.local_path (absolute fixture path; OLDPWD also matched it only because it was the lane root). These are host paths (username disclosure), not secrets. Also carried: host facts available_processors=32, max_heap_bytes=8124366848, java_version 21.0.13.
- Proposal only (no frozen instrument touched): if the lane wants records free of host paths, land with a neutral TMPDIR or record this as a known limitation; V2 already normalises the runtime dir for norm-eq.

## Tooling
No installs or upgrades. Noted absent: `bc`; host date is uutils 0.8.0.

## Scratch
/fast/scratch/hyaku/revenger-r90/ExecR90Producer deleted after copying receipts.

VERDICT: two independent android producer runs, both exit 0, exact stdouts with matching receipt digests and distinct non-r89 evidence ids; norm-eq identical, oracle v2 22/22 (information only).
