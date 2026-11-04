# ScoutR90Producer — rea android producer surface (round 90, w1)

Scope: read-only reconnaissance. No lane file was written except this report directory. No tools were installed or upgraded.
Freeze consulted: `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-90/claims.md`, `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-90/norm_eq.py` (V1–V4 docstring), `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-90/c2_counter.py` (K4/K6 lines only).
LSP: none applies (bundled JS plus a Java source file in an npm global), so the trace below uses text search over the installed files. Every claim is either quoted from the source or measured in the receipts.

## 1. Installed producer (observed)

- `command -v rea` → `/run/user/1000/fnm_multishells/1981588_1793727763382/bin/rea` → resolves to `/home/vgpnk/.local/share/fnm/node-versions/v24.21.0/installation/lib/node_modules/rea-agents/scripts/rea.mjs`. `package.json` gives `"name": "rea-agents"`, `"version": "6.7.0"`.
- The CLI path loads the bundle `dist/cli-runtime/cli.js` (`scripts/rea.mjs:73` `await import("../dist/cli-runtime/cli.js")`). The unbundled `dist/android/*.js` and `dist/domain/*.js` hold the same code, but the citations below use the bundle that actually runs.
- In this report, `$R` means `/home/vgpnk/.local/share/fnm/node-versions/v24.21.0/installation/lib/node_modules/rea-agents`.

### Runtime temp dir (V2 source)
- `$R/dist/cli-runtime/cli.js:16114`: `createJadxWorkspaceRoot = () => process.platform === "win32" ? WindowsJadxWorkspaceRoot.create() : PrivateRuntimeRoot.create({ prefix: "rea-android-" });`
- `$R/dist/cli-runtime/PrivateRuntimeRoot-Cd23u6jd.js:274`: `const path = await mkdtemp(join(options.parent ?? tmpdir(), options.prefix ?? "rea-provider-"));` The parent is `os.tmpdir()`, which is `$TMPDIR`. The suffix comes from mkdtemp: 6 random characters from `[A-Za-z0-9]`. Measured suffixes were `CQUh6p`, `BiY2wz`, `0X9WDq` and `yp6Fag`. All of them match norm_eq's `[A-Za-z0-9_]+`.
- `$R/dist/cli-runtime/cli.js:16126`: `const snapshot = join(root, "target.apk");`. Lines 17382–17385 create the root and the snapshot for each process.
- `$R/dist/cli-runtime/cli.js:16842-16847`: `load_apk` receives `{ path: snapshot, threads: 1, resources: "full" }`. The parsed reply is stored as `loaded`, and the code asserts `loaded.apk_path === snapshot`.
- `$R/dist/cli-runtime/cli.js:16859-16865`: `rawResult: { server, bridge_sha256, jar_sha256, loaded, calls: this.#observedCalls }`. As a result, the runtime path reaches three leaves: `raw_result.loaded.apk_path`, `raw_result.calls[1].input.path` and the JSON text in `raw_result.calls[1].response.content[0].text`.
- Windows uses a different variant, `rea-android-[a-f0-9]{32}` (`$R/dist/android/JadxWorkspaceRoot.js:102`). This host does not reach it.

### load_duration_ms (V4 source)
- `$R/bridge/android/ReaJadxBridge.java:77`: `reply.put("load_duration_ms", loaded.getLoadDurationMs());`. The reply is a `LinkedHashMap` (`:71`), so its key order is fixed.
- The node side parses that reply with `jadxLoadSchema` (`cli.js:16264-16271`), a non-strict `z.object` with keys `state, apk_path, class_count, resource_count, threads, resources`. Unknown keys are stripped, so `load_duration_ms` is absent from `raw_result.loaded`. It survives only inside the verbatim response text of `calls[1]`. norm_eq handles it there by applying V3 (parse the text) and then V4 (drop the key).

### JVM status key order (V3 source)
- `$R/bridge/android/ReaJadxBridge.java:329-334`: `if (name.equals("rea_jvm_status")) return json(Map.of("engine_reported_version", …, "max_heap_bytes", Runtime.getRuntime().maxMemory(), "available_processors", Runtime.getRuntime().availableProcessors(), "java_version", System.getProperty("java.version"), "metadata_scope", "parsed_members"));`
- `Map.of` iterates in a per-JVM randomized (salted) order. In the measurement, runs 1 and 3 had the same order, while runs 2 and 4 each had a different one (`receipts/run*.json`).

### evidence_id derivation
- `$R/dist/cli-runtime/reconstructionObligationLedgerSchemas-Bi6sect1.js:609-613`: `createEvidence = (target, provider, observation) => { … evidence_id: computeEvidenceId(normalized) }`
- Same file, `:570`: `computeEvidenceId = (evidence) => \`ev_${digestCanonicalValue(semanticProjection(evidence), "Evidence")}\`;`. `:39` defines `digestCanonicalValue`, which takes a sha256 over canonical JSON.
- Same file, `:549-569`: `semanticProjection` = `subject{digest,format,architecture}`, `provider`, `analysis_profile`, `predicate_type`, `operation`, `parameters`, `raw_result`, `normalized_result`, `confidence`, `authority`, `environment`, `limitations`, `relationship_coverage`, `locations`, `evidence_links`. It excludes `subject.name` and `subject.local_path`. The unbundled twin is `$R/dist/domain/evidence.js:159-183` and `:235-240`.
- The id is checked on read. `$R/dist/domain/evidence.js:136-144` (`authenticatedEvidenceSchema`) rejects a record whose `evidence_id` is not the digest of its own content: "Evidence semantic identifier does not match its record".

## 2. evidence_id: content-derived (reproducible) or random?

**Content-derived. It is not minted at random.** The source is `computeEvidenceId` (bundle `:570`; `dist/domain/evidence.js:183`), a sha256 over the semantic projection. The rea source has no randomness on this path. The ids differ between runs only because `raw_result` contains three volatile values: the mkdtemp runtime path (V2), the `Map.of` key order inside the JSON text (V3) and `load_duration_ms` (V4).

I measured this with rea's own `parseEvidence` (`receipts/verify_id.mjs`, output in `receipts/receipts.log`):

| Input | Result |
|---|---|
| run1–4 and the r89 record, as produced | `ID_CONSISTENT` |
| Same records with `evidence_id` forged to `ev_bbb…` | `REJECTED` |
| Same records with only `load_duration_ms` edited | `REJECTED` |
| Same records with `subject.local_path`/`name` edited | `ID_CONSISTENT` (these fields are outside the digest) |

Consequences for the frozen claims (inference from the facts above):
- claims.md says the producer "mints per-run ids". That is imprecise: the id is a pure function of content, and it differs per run because the content differs. In practice V1 is redundant given V2–V4. It still does no harm.
- K6 (distinct ids) holds because each run gets a random mkdtemp suffix. If two runs ever had identical raw_result content they would get the same id, but the 6-character random suffix makes that negligible. The r89 id is unreachable from new runs because its content contains the path `/fast/scratch/hyaku/revenger-r89/ExecR89Record/rea-android-ugg7mp`.
- Proposal only (the instrument is frozen, so nothing was edited): claims.md says "hand-edited distinct ids would pass K6". K6 could instead require each run's id to match a recomputed digest, using `parseEvidence` or a Python port of `digestCanonicalValue`. That rejects pasted or forged ids. Anyone holding the digest code can still recompute a matching id, so this adds integrity, not provenance.

## 3. Fields that can vary between two runs on the same input and host

### Measured
I ran `TMPDIR=<scratch> rea inspect-android-package /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/apk-r65/fixture.apk --format json` four times from the scratch directory. Each run exited 0 with 0 stderr bytes and printed 4360 bytes, and the four sha256 values all differ. Only five leaves differ across the four runs (`receipts/receipts.log`):

| Varying leaf | Cause | Frozen class | norm_eq |
|---|---|---|---|
| `$.evidence_id` | content digest of the leaves below | V1 | normalized |
| `$.raw_result.calls[0].response.content[0].text` | `Map.of` key order | V3 | normalized |
| `$.raw_result.calls[1].input.path` | mkdtemp suffix | V2 | normalized |
| `$.raw_result.loaded.apk_path` | mkdtemp suffix | V2 | normalized |
| `$.raw_result.calls[1].response.content[0].text` | mkdtemp suffix plus `load_duration_ms` (640/463/390/514) | V2 + V3 + V4 | normalized |

norm_eq returned `NORM_EQ=identical` with exit 0 on all 6 pairs. No leaf varied outside V1–V4.

### Not seen, but able to vary (from code reading)
None of these change between runs with the same invocation, cwd and environment. They change when the invocation, cwd or environment changes, which matters if run1 and run2 are made by different seats or shells. For each one, the norm_eq column says whether norm_eq would flag a difference:

1. `$.parameters.path`: the literal path argument. It is inside the digest. I measured this: run1 (absolute path) against the r89 record (relative path) gives `NORM_EQ=DIFFER` / `DIFF $.parameters.path`. **norm_eq flags it.** Both runs must use the identical argument string.
2. `$.subject.local_path` and `$.subject.name`: the resolved absolute path of the target, so they depend on how the target is named. They are outside the digest. **norm_eq flags them.** Same cwd plus same argument keeps them stable. The measured run1 and the r89 record resolve to the same absolute path, so they match.
3. `max_heap_bytes` in `calls[0]` text and `$.normalized_result.engine.heap_limit_mib` (`cli.js:16855`, `Math.floor(runtime.max_heap_bytes / (1024*1024))`). They are set by `REA_JADX_HEAP_MIB` → `-Xmx` (`JebMcpEndpoint-BEalGZh9.js:635-656`, `resolveJvmArguments`), `JAVA_TOOL_OPTIONS`, `_JAVA_OPTIONS` or `JDK_JAVA_OPTIONS`, or by JVM ergonomics over RAM and the cgroup memory limit. **norm_eq flags them.** Measured here: 8124366848 / 7748 in every run.
4. `available_processors` in `calls[0]` text. It is set by `REA_JADX_ACTIVE_PROCESSOR_COUNT` → `-XX:ActiveProcessorCount=`, CPU affinity (taskset) or the cgroup CPU quota. **norm_eq flags it.** Measured here: 32.
5. `java_version` in `calls[0]` text. It follows `JAVA_HOME` or the `java` found on `PATH`. **norm_eq flags it.** Measured here: 21.0.13.
6. `$.raw_result.jar_sha256`, `bridge_sha256`, `provider.version` and `normalized_result.engine.*`. They follow `REA_JADX_MCP_JAR` and the rea install. **norm_eq flags them.** They are stable unless rea or the jar is upgraded between runs.
7. The `TMPDIR` prefix of the runtime path. The V2 regex `[^"\s]*/rea-android-[A-Za-z0-9_]+` rewrites the whole prefix, so two runs can differ in `TMPDIR` and still pass. It only works if the prefix has no whitespace or `"`. With a space in `TMPDIR`, the part before the space is left unnormalized, which is harmless when both runs share the same `TMPDIR`.
8. Array element order of `permissions` (from upstream `get_app_info`, `cli.js:16418`, `jadxAppSchema` `permissions: z.array(z.string())`). V3 sorts only object keys, not arrays, so **norm_eq would flag it.** This fixture has `permissions: []`, so it cannot vary here. For a non-empty APK, the upstream jar's ordering was not inspected. [INFERENCE] It is a latent risk only for other fixtures.
9. Timestamps, hostnames and pids: none. The record has no time, host or pid field. Top-level keys are `evidence_id, subject, provider, analysis_profile, predicate_type, operation, parameters, raw_result, normalized_result, confidence, authority, environment (null), limitations, relationship_coverage (null), locations, evidence_links ([])`. The `calls` array order is set by sequential awaits (`cli.js:16839`, `16842`, `16418-16419`), so it is deterministic. `limitations` is a constant array.

EXTRA_VOLATILE: none (for two runs on the same input, host, invocation string, cwd and environment, which is what I measured across 4 runs and 6 pairs). Conditionally volatile when the invocation or environment differs, and **norm_eq flags all of these**: `parameters.path`, `subject.local_path`/`subject.name`, `max_heap_bytes`/`heap_limit_mib`, `available_processors`, `java_version`, `jar_sha256`/`bridge_sha256`/engine version, and the order of a non-empty `permissions` array.

Advice for the producer seat: run both invocations from the lane root with the identical relative argument `corpus/fixtures/apk-r65/fixture.apk`, in the same shell environment, with the same `TMPDIR` containing no whitespace. Do not set or change `REA_JADX_*`, `JAVA_*` or `PATH` between runs.

## Receipts (`/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-90/w1/ScoutR90Producer/receipts/`)
- `run1.json` … `run4.json`: the four producer stdouts. They are scout probes made from the scratch cwd with an absolute path, not candidate records.
- `receipts.log`: sha256 values, norm_eq on all 6 pairs and on run1 against r89, the `parseEvidence` legs and stderr.
- `verify_id.mjs`: the id-consistency probe, which imports rea's `dist/domain/evidence.js` `parseEvidence`.

Environment: rea-agents 6.7.0 (fnm node v24.21.0), openjdk 21.0.13, nproc 32, `REA_JADX_MCP_JAR=/home/vgpnk/.local/opt/jadx-headless-mcp/jadx-headless-mcp-0.7.1-all.jar`. No `REA_JADX_HEAP_MIB`, `REA_JADX_ACTIVE_PROCESSOR_COUNT`, `JAVA_TOOL_OPTIONS`, `_JAVA_OPTIONS` or `JDK_JAVA_OPTIONS` was set.

Remaining unknowns: the source of the upstream jadx-headless-mcp `get_app_info` permissions ordering, and whether `get_android_manifest` text is byte-stable across jadx versions. Both are outside this fixture and this host.

VERDICT: evidence_id is a content digest (`computeEvidenceId`, bundle `:570`), not random. With the same invocation and environment, only V1–V4 vary (4 runs, 6 pairs `NORM_EQ=identical`). EXTRA_VOLATILE: none. Invocation or environment drift (`parameters.path`, `subject.local_path`, JVM heap, CPU count or java version) is flagged by norm_eq.
