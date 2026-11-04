# round-89 run ledger — android family record through the current producer

> **STATUS (post-L1 directive): C2 NOT ADMITTED by this evidence.** The frozen
> two-run byte-identity kill rule is **FAILED** on measured evidence (`cmp`
> DIFFER, char 20). This retained record is evidence of producer
> non-determinism under rea 6.7.0 + jadx-headless-mcp 0.7.1 — not admitted
> coverage; the ORACLE OK (19/19) verdict and any F4 count do not cure the
> failed equality leg.

One bounded, passive, non-executing producer observation of an authored inert
local APK, saved as producer-emitted bytes:

- fixture: `corpus/fixtures/apk-r65/fixture.apk` — 947 bytes, sha256
  `05d2280f847497cf…`, members `AndroidManifest.xml`,
  `META-INF/MANIFEST.MF`, `classes.dex`; the committed bytes are the source of
  truth. Nothing was installed, updated or fetched this round; no external
  network surface; the APK is never executed.
- producer: `rea --version` → 6.7.0 (exit 0); `jadx --version` → 1.5.6
  (exit 0); `rea` on PATH via the node/rea-agents install, `jadx` at
  `/usr/bin/jadx`; `REA_JADX_MCP_JAR` set on this host (name recorded here,
  value in the record-free routing evidence of `reports/round-89/claims.md`).
  Provider read from the record itself: `jadx` / "JADX headless" / 0.7.1.
- record: `inspection.json` = the exact stdout bytes of
  `rea inspect-android-package corpus/fixtures/apk-r65/fixture.apk --format
  json` run from the lane root, exit 0, 2.464 s, stderr 0 bytes, stdout
  sha256 `01af3141d79027a3bae53b6482779d3e9c89446ab6ca09b408a6cb266f321c76`,
  `operation: inspect_android_package`, Evidence
  `ev_387c9e9c410dc40fb6a19524fcdda49a3186c4597c20e9c4a9625b3b99a588e4`;
  receipt in `receipt.json`. The landed bytes were `cmp`-checked against the
  captured stdout: identical.
- two-run reproducibility — measured, **not byte-identical**: a second
  independent invocation from the same cwd exited 0 (2.276 s, stderr 0 bytes)
  with stdout sha256
  `5bbdd189cd19dd1b181b4850b95fe07d077bc4031c70b25fec5006ca0d72ce00`;
  `cmp` differs at char 20. A full JSON-tree walk (both outputs 4303 bytes)
  shows the delta set is exactly four producer-side volatile sources, nothing
  else: (1) `evidence_id` (per run); (2) the private runtime directory
  `rea-android-XXXXXX` (mkdtemp-style, per run — appears in
  `raw_result.calls[1].input.path`, that run's `apk_path`, and
  `raw_result.loaded.apk_path`); (3) JVM map key ordering inside
  `raw_result.calls[0]` (same five system-fact keys, different order);
  (4) `load_duration_ms` (175 vs 170). `normalized_result` — everything the
  oracle derives against — is identical across the two runs. No producer knob
  pins these: the command takes only `<path>`, the global options are
  format/filter only, and a grep of the `rea-agents` scripts shows no
  environment pin for the android private runtime directory. The frozen
  byte-identity leg is therefore measured UNMET under rea 6.7.0 +
  jadx-headless-mcp 0.7.1; reproducibility here is oracle-verdict
  reproducibility, not byte reproducibility (the same volatility class the
  round-77 browser ledger disclosed).
- environment audit: the record's `environment` field is `null` — it embeds
  no environment variable VALUES; no key needed dropping, and the landed
  bytes remain exact stdout. Narrow reading (per the SentinelR89 ruling):
  `environment: null` means no environment-variable map; it does NOT mean no
  host-derived facts. The record does carry JVM/host metadata in
  `raw_result.calls[0]` (max_heap_bytes 8124366848, available_processors 32,
  java_version 21.0.13) and `normalized_result.engine.heap_limit_mib` 7748 —
  disclosed here as low-sensitivity metadata and classified in the sentinel's
  own report.
- host-path disclosure (SentinelR89 SEC-01/SEC-02/SEC-07/SEC-09): the landed
  record carries `subject.local_path` (absolute lane checkout path containing
  the OS username) and `raw_result.loaded.apk_path` /
  `raw_result.calls[1].input.path` (the producing seat's scratch path plus a
  per-run `rea-android-XXXXXX` directory that no longer exists). The receipt's
  `cwd` and the seat's invocation transcript carry the same class of path, and
  the transcript additionally prints the `REA_JADX_MCP_JAR` tool path. These
  are tool and checkout locations, not credentials; the bytes stay unedited
  because the receipt pins them.
- identity oracle — full output of
  `PYTHONUTF8=1 python3 -B corpus/fixtures/apk-r65/oracle_check.py
  corpus/fixtures/apk-r65/truth.json corpus/live/runs/round-89/inspection.json`
  (exit 0):

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

  The oracle re-hashes the committed fixture bytes against `truth.json`
  (premise leg) and derives every record expectation from those bytes —
  package name and the two declared version attributes from the authored AXML
  string table, `class_count` from the DEX header's own `class_defs_size` at
  0x60, `resource_count` from the authored member table — never from the
  record.
- producer's own limitations list (verbatim from the record's `limitations`
  field): "Static decompiler observations do not establish runtime behavior;
  the APK is never executed." / "Method signatures use provider display
  types; DEX prototypes come from frozen JADX metadata. Display names may be
  aliases, and overload indices are local to this engine and artifact." /
  "Class inventories use parsed metadata before code generation, including
  synthetic members that may be omitted from decompiled source. Source
  positions remain unknown." / "Incoming reference totals count JADX using
  nodes. Direct invoke entries within a using method report raw DEX
  code-unit offsets and method indexes, but coverage is limited to those
  nodes and directly matched invokes; it does not establish every possible
  dynamic or reflective call site." / "Manifest summary fields are extracted
  by the upstream engine; decoded XML is retained for verification. APK
  signatures, split APKs, native libraries and Android runtime capture are
  not verified by this provider."
- observation vs inference vs unknown: observed — the recorded version
  commands, both run outputs (exit codes, stderr sizes, wall times, stdout
  sha256 values), the `cmp` verdict, the field-level delta walk, the
  `environment: null` field, and the oracle verdict over the landed bytes.
  Inference (labeled): that no pair of runs under this producer version can
  be byte-identical is inferred from the runtime-directory construction plus
  per-run evidence id plus the measured jitter, backed by the source grep —
  it is not proven exhaustively. Unknown — whether the closure judge accepts
  the family move as honest coverage improvement (adjudicated externally),
  and how `evidence_id` is derived (its construction was not examined; only
  its per-run variance is measured).
- Q09: this is **reproducible producer output** — a passive, twice-invoked
  observation whose identity facts the frozen oracle re-derives from authored
  fixture bytes. It is **not** a provenance or authenticity claim about the
  APK, the fixture, or the producer.
- pre-run observation (env gate): a first attempt pair executed in a
  non-interactive exec environment where `REA_JADX_MCP_JAR` was unset failed
  with exit 1 and the producer's `capability_unavailable` payload
  (`details.diagnostics.jar_configured: false`, 686 bytes, both attempts
  byte-identical, sha256
  `4d0e6ea59823c97242bfa75b009952dfe8c1e9c63bc1793c09308d6482167330`). The
  r83–r88 "android hard gate" is real whenever the jar variable is unset;
  on this host with the variable set it does not hold. These error payloads
  are not part of the record; the landed bytes come only from the two exit-0
  runs described above.

- relocation (adjudication): this directory moved byte-identically from
  `corpus/live/runs/round-89/` to `reports/round-89/rejected-android-record/`
  (`cmp` 3/3 identical before the move). Reason: `reports/round-81/f_probe4.py`
  counts any `corpus/live/runs/**/*.json` carrying `evidence_id` +
  `normalized_result`, so a rejected record left there would read F4 11/11 —
  a false green. Rejected evidence is preserved, not counted.
