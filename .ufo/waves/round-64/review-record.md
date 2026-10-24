# Round-64 saved-record verification — round-63 REA firmware record (C1 support)

Seat: `revenger-r64.R64ReviewRecord` (leaf, no dispatch). Lane:
`/home/vgpnk/Projects/shokunin/revenger-shokunin`, tip
`a3d063f29b93ad1f0b7eab78652c552685b84d89`. All commands below were run with cwd
`/home/vgpnk/Projects/shokunin/revenger-shokunin` unless a different cwd is stated.
Method: round-63 `W2VerifyC2Record.md` (`.ufo/waves/round-63/falsify/W2VerifyC2Record.md`).
No git/jj mutation was run (only read-only `git log`, `git status`, `git rev-parse`).
Every command and its actual output is reproduced after each step.

Targets:

- `corpus/live/runs/round-63/inspection.json` (saved REA record, 3904 B)
- `corpus/live/runs/round-63/receipt.json` (receipt, 492 B)
- `corpus/live/runs/round-63/stdout.raw` (3904 B), `stderr.txt` (0 B)
- `corpus/fixtures/firmware-r63/firmware-r63.bin` (2048 B), `truth.json`, `generator.py`
- Producer: `rea-agents@6.5.0`, cached at
  `/home/vgpnk/.npm/_npx/ad9a3fdbcad992c6/node_modules/rea-agents`

**Verdict: the record, receipt and fixture bindings all verify.** Evidence ID re-derives
to the recorded value from the shipped 6.5.0 package; `stdout_sha256` binds `stdout.raw`
bytes (which are byte-identical to `inspection.json`); `fixture_sha256` binds
`firmware-r63.bin`. No HIGH/MEDIUM finding. Two carried verification LOWs
(replay-env gap; content-bound-not-provenance ID), one dependency finding (C1 entry not
landed at verification time) and the ordinary assembled-record residual are stated at the
end.

## V1 — bytes, cleanliness, provenance of the artifacts

Command and output:

```
$ sha256sum corpus/fixtures/firmware-r63/firmware-r63.bin \
            corpus/live/runs/round-63/inspection.json \
            corpus/live/runs/round-63/stdout.raw \
            corpus/live/runs/round-63/receipt.json \
            corpus/fixtures/firmware-r63/truth.json \
            corpus/live/runs/round-63/stderr.txt \
            corpus/live/runs/round-63/oracle_check.py
bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be  corpus/fixtures/firmware-r63/firmware-r63.bin
f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9  corpus/live/runs/round-63/inspection.json
f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9  corpus/live/runs/round-63/stdout.raw
e930a549db16a180d4ab05307e073cd71599a3317b9f3d15a0d97843d5c6b94d  corpus/live/runs/round-63/receipt.json
9663f90b2b9f29c5beb621e554ed7584eedf5e77d4785f26a453e70dbd5a65e6  corpus/fixtures/firmware-r63/truth.json
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  corpus/live/runs/round-63/stderr.txt
d0dfd7a1cd105485e47bf52446056a2636fb803c05a404ce56da597f36ce0512  corpus/live/runs/round-63/oracle_check.py
```

```
$ git status --porcelain corpus/live corpus/fixtures
(empty)
$ git rev-parse HEAD
a3d063f29b93ad1f0b7eab78652c552685b84d89
$ git log --diff-filter=M --oneline -- \
    corpus/live/runs/round-63/inspection.json corpus/live/runs/round-63/receipt.json \
    corpus/live/runs/round-63/stdout.raw corpus/fixtures/firmware-r63/firmware-r63.bin
(empty)
$ git log --diff-filter=A --oneline -- \
    corpus/live/runs/round-63/inspection.json corpus/live/runs/round-63/receipt.json \
    corpus/live/runs/round-63/stdout.raw corpus/fixtures/firmware-r63/firmware-r63.bin
2a34e45 round-63: build state - firmware fixture+REA record+oracle+ledger, ...
```

Reading: the four artifacts were added in `2a34e45` and have **never been modified after
add**; working tree clean on both directories at round-64 tip. The receipt file SHA-256
`e930a549…c6b94d` equals the pin cited in `LEDGER.md` row "Receipt" (including its
2026-10-24 correction note); `stdout.raw`/`inspection.json` SHA-256 equals the LEDGER's
"Saved stdout" pin; `truth.json` is `9663f90b…a65e6` — the digest round-63's
reproducible-build check recorded for this file (not re-run by this seat).

## V2 — Evidence ID re-derived from the shipped rea-agents@6.5.0 package

Method (round-63 A2.1): the shipped package authenticates an Evidence envelope by
recomputing `ev_ + digestCanonicalValue(semanticProjection(evidence), "Evidence")`
(`dist/domain/evidence.js:135,156-182`, `dist/domain/canonicalDigest.js:8`) and
rejecting a mismatch. Two independent paths were used against the committed bytes:

1. **Package-native authentication.** `parseEvidence(record)` — the package's own
   exported parser, which internally calls the non-exported `computeEvidenceId`.
2. **Independent re-derivation.** A literal transcription of `semanticProjection`
   (subject digest/format/architecture, provider, analysis_profile, predicate_type,
   operation, parameters, raw_result, normalized_result, confidence, authority,
   environment, limitations, relationship_coverage when non-null, locations,
   evidence_links) hashed with the package's exported `digestCanonicalValue`.
3. **Sensitivity controls.** Semantic mutations of the committed record must move the
   recomputed ID and be rejected by `parseEvidence`; mutations that are re-IDed with the
   same package function show what the ID does and does not authenticate.

Script: `/tmp/revenger-r64-review/rederive_id.mjs` (imports only from the cached package;
no package byte changed). Command and full output:

```
$ cd /tmp/revenger-r64-review && node rederive_id.mjs
S1 PARSE_OK evidence_id=ev_aae7529fd55b90cd55804cd45bff0fecd837dfaca3e2a132fbe9d161080ed259
S2 RECORDED=ev_aae7529fd55b90cd55804cd45bff0fecd837dfaca3e2a132fbe9d161080ed259
S2 RECOMPUTED=ev_aae7529fd55b90cd55804cd45bff0fecd837dfaca3e2a132fbe9d161080ed259
S2 MATCH=true
S3 M1 subject.digest: id_changed=false derived_id_equals_recorded=false parseEvidence=REJECT
S3 M2 raw_result.file_map offset: id_changed=false derived_id_equals_recorded=false parseEvidence=REJECT
S3 M3 normalized_result.input_size: id_changed=false derived_id_equals_recorded=false parseEvidence=REJECT
S3 M4 evidence_id last hex: id_changed=false derived_id_equals_recorded=true parseEvidence=REJECT
S3 M5 raw mutation re-IDed (control): id_changed=true derived_id_equals_recorded=false parseEvidence=ACCEPT
S3 M6 region size semantics re-IDed (control): id_changed=true derived_id_equals_recorded=false parseEvidence=ACCEPT
S4 projection_keys=analysis_profile,authority,confidence,environment,evidence_links,limitations,locations,normalized_result,operation,parameters,predicate_type,provider,raw_result,subject
S4 subject_in_projection={"digest":{"sha256":"bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be"},"format":"file","architecture":null}
```

Reading:

- S1/S2: the recorded ID `ev_aae7529f…80ed259` is exactly the ID the shipped 6.5.0
  identity function computes over the committed record's own semantic fields. Any
  post-hoc edit of a projected field breaks the binding (S3 M1–M3), and an edited ID is
  rejected even when the semantics are intact (S3 M4).
- S3 M5/M6 are honest controls: a record whose ID is recomputed over mutated semantics
  is accepted. The Evidence ID authenticates **content self-consistency**, not
  provenance — it cannot distinguish "producer created this" from "someone assembled
  this and recomputed the ID". That is the LEDGER's U4 and is not a defect of the record.
- The projection excludes `subject.name`/`subject.local_path` (display fields); the
  digest, format and architecture are bound. `relationship_coverage` is `null` here and
  therefore omitted, as the package does.
- Because `raw_result` is inside the projection, the ID binds the producer's raw report
  **including its mkdtemp temp path**; an independent re-run can never reproduce the same
  ID (V5). The ID is content-bound to this saved run, not a cross-run identifier.

## V3 — `receipt.stdout_sha256` binds `stdout.raw` bytes

```
$ sha256sum corpus/live/runs/round-63/stdout.raw
f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9  corpus/live/runs/round-63/stdout.raw
$ python3 -c "import json;print('receipt.stdout_sha256='+json.load(open('corpus/live/runs/round-63/receipt.json'))['stdout_sha256'])"
receipt.stdout_sha256=f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9
$ cmp corpus/live/runs/round-63/stdout.raw corpus/live/runs/round-63/inspection.json && echo CMP_IDENTICAL
CMP_IDENTICAL
$ python3 -c "b=open('corpus/live/runs/round-63/stdout.raw','rb').read();print('bytes',len(b),'newlines',b.count(b'\n'),'ends_0a',b.endswith(b'\n'),'single_line',b.count(b'\n')==1)"
bytes 3904 newlines 1 ends_0a True single_line True
$ wc -c < corpus/live/runs/round-63/stderr.txt
0
$ python3 -c "import os;s1=os.stat('corpus/live/runs/round-63/stdout.raw');s2=os.stat('corpus/live/runs/round-63/inspection.json');print('same_inode=',s1.st_ino==s2.st_ino)"
same_inode= False
```

Producer serialization parity: the shipped CLI emits `` `${JSON.stringify(value)}\n` ``
(`dist/cliOutput.js:129`), matching the saved `stdout.raw` (one line, 3904 B, trailing
`0x0a`). `stdout.raw` and `inspection.json` are distinct inodes with identical bytes, so
the receipt binds the record's actual stdout bytes, not a post-edited copy of the record.
Receipt `exit_code` = 0 and the saved stderr is 0 bytes (`e3b0c442…b855`).

## V4 — `receipt.fixture_sha256` binds `firmware-r63.bin`

```
$ sha256sum corpus/fixtures/firmware-r63/firmware-r63.bin
bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be  corpus/fixtures/firmware-r63/firmware-r63.bin
receipt.fixture=bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be
record.subject=bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be
truth.image=bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be
receipt.evidence_id=ev_aae7529fd55b90cd55804cd45bff0fecd837dfaca3e2a132fbe9d161080ed259
record.evidence_id=ev_aae7529fd55b90cd55804cd45bff0fecd837dfaca3e2a132fbe9d161080ed259
$ python3 - <<'PY'
import json, os
fix='/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/firmware-r63.bin'
r=json.load(open('corpus/live/runs/round-63/receipt.json'))
i=json.load(open('corpus/live/runs/round-63/inspection.json'))
print('command_contains_fixture_abs=', fix in r['command'])
print('parameters.path_equals_fixture=', i['parameters']['path']==fix)
print('subject.local_path_equals_fixture=', i['subject']['local_path']==fix)
print('subject.name=', i['subject']['name'], 'basename(fixture)=', os.path.basename(fix))
print('receipt_keys=', sorted(r.keys()))
print('receipt_exit=', r['exit_code'], 'duration=', r['duration_seconds'])
print('fixture_size_on_disk=', os.path.getsize(fix))
PY
command_contains_fixture_abs= True
parameters.path_equals_fixture= True
subject.local_path_equals_fixture= True
subject.name= firmware-r63.bin basename(fixture)= firmware-r63.bin
receipt_keys= ['command', 'duration_seconds', 'evidence_id', 'exit_code', 'fixture_sha256', 'stdout_sha256']
receipt_exit= 0 duration= 1.296587134
fixture_size_on_disk= 2048
PY
```

Reading: four independent sources (fixture on disk, receipt, record subject, oracle truth)
agree on the digest; the receipt command, record `parameters.path` and
`subject.local_path` all name the same absolute fixture path; fixture size 2048 equals
`normalized_result.input_size`; `receipt.evidence_id` equals the record ID.

## V5 — producer reproducibility (corroboration, not the deliverable)

```
$ mkdir -p /tmp/revenger-r64-review/tmp /tmp/revenger-r64-review/rerun
$ cd /tmp/revenger-r64-review/rerun && \
  TMPDIR=/tmp/revenger-r64-review/tmp REA_BINWALK_COMMAND=/usr/bin/binwalk \
  npx -y rea-agents@6.5.0 inspect-firmware-regions \
    /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/firmware-r63.bin \
    --format json > rerun.json 2> rerun.err
EXIT=0
3976 rerun.json
   0 rerun.err
$ cd /tmp/revenger-r64-review && node compare_rerun.mjs
R1 committed_parse=ACCEPT
R2 rerun_parse=ACCEPT
R3 rerun_evidence_id=ev_00f5ba295aa857f0688c681c0b6460743deda33cfa487b3943a8659c84326a24
R4 committed_evidence_id=ev_aae7529fd55b90cd55804cd45bff0fecd837dfaca3e2a132fbe9d161080ed259
R5 structural_equal(evidence_id excluded, tmp path+UUID normalized)=true
R6 regions_equal=true
R7 engine_equal=true
R8 input_size 2048 vs 2048
$ node diff_rerun.mjs   # pre-normalization diff, to show the only differences
DIFF_COUNT=4
DIFF $.evidence_id: "ev_aae7529f..." vs "ev_00f5ba29..."
DIFF $.raw_result.execution.args[5]: "/tmp/rea-firmware-XXX/report.json" vs "/tmp/revenger-r64-review/tmp/rea-firmware-XXX/report.json"
DIFF $.raw_result.execution.args[6]: "/tmp/rea-firmware-XXX/firmware.bin" vs "/tmp/revenger-r64-review/tmp/rea-firmware-XXX/firmware.bin"
DIFF $.raw_result.report[0].Analysis.file_path: "/tmp/rea-firmware-XXX/firmware.bin" vs "/tmp/revenger-r64-review/tmp/rea-firmware-XXX/firmware.bin"
```

Reading: a fresh run of the receipt's pinned producer command reproduces the committed
record's semantics exactly (all fields equal after excluding `evidence_id` and
normalizing mkdtemp paths and provider_id UUIDs). The fresh output is itself accepted by
the package's `parseEvidence`. The two IDs differ solely because `raw_result` records the
producer's temp staging path — consistent with V2's projection analysis, not a
reproducibility defect.

Package identity re-checked at verification time:

```
$ cat ~/.npm/_npx/ad9a3fdbcad992c6/node_modules/rea-agents/package.json \
  | python3 -c 'import json,sys; d=json.load(sys.stdin); print(d.get("name"), d.get("version"), d.get("bin"))'
rea-agents 6.5.0 {'rea': 'scripts/rea.mjs', 'rea-agents': 'scripts/rea.mjs'}
$ sed -n '60,75p' dist/cliCommandNames.js
    inspectRustBinary: "inspect-rust-binary",
    inspectPeResources: "inspect-pe-resources",
    inspectAnalysisView: "inspect-analysis-view",
    listFridaDevices: "list-frida-devices",
    listFridaProcesses: "list-frida-processes",
    instrumentWithFrida: "instrument-with-frida",
    inspectEvidenceBundle: "inspect-evidence-bundle",
    inspectFirmwareRegions: "inspect-firmware-regions",
    extractFirmware: "extract-firmware",
    inspectAndroidPackage: "inspect-android-package",
    inspectPcapClient: "inspect-pcap-client",
    inspectPcapCapture: "inspect-pcap-capture",
    identifyFlutterBuild: "identify-flutter-build",
    inspectDartAot: "inspect-dart-aot",
    inspectApktoolClient: "inspect-apktool-client",
$ node -e 'import("./dist/cliCommandNames.js").then(m=>console.log(Object.keys(m).sort().join("\n")))'
CLI_COMMANDS
CLI_COMMAND_ALIASES
CLI_COMMAND_NAMES
CLI_COMMAND_TOOL_ALIASES
MCP_TOOLS_WITHOUT_DEDICATED_CLI
$ node -e 'import("./dist/cliCommandNames.js").then(m=>console.log("inspectFirmwareRegions=", JSON.stringify(m.CLI_COMMANDS.inspectFirmwareRegions)))'
inspectFirmwareRegions= "inspect-firmware-regions"
```

Engine re-checked live:

```
$ sha256sum /usr/bin/binwalk
5fc19aac1f357a66a47e8b20a8038a84cb93971cb5d331bd4503b02fcc0a40d6  /usr/bin/binwalk
$ binwalk --version
binwalk 3.1.0
```

Both equal the record's `normalized_result.engine.executable_sha256` and
`raw_result.version_execution.stdout.text` (`binwalk 3.1.0\n`, args `["--version"]`).

## V6 — oracle agreement of the saved record

```
$ python3 -B corpus/live/runs/round-63/oracle_check.py
REGION name=padding kind=padding offset=0 size=512 record=not-expected padding=OK
REGION name=diagnostic-note kind=zlib offset=512 size=79 offset=OK size=OK signature=OK decompressed_sha256=OK (a5718481…df7b86)
REGION name=padding kind=padding offset=591 size=433 record=not-expected padding=OK
REGION name=component-note kind=zlib offset=1024 size=90 offset=OK size=OK signature=OK decompressed_sha256=OK (2d0d86aa…eeaba9)
REGION name=padding kind=padding offset=1114 size=934 record=not-expected padding=OK
ORACLE OK
ORACLE_EXIT=0
```

Reading: the record's two reported regions agree with `truth.json` on offset, size,
signature and decompressed content digest; padding regions are correctly
`not-expected` under `coverage=signature_scan` (the record reports no false-positive
padding region).

Independent byte re-derivation (my own `zlib.decompressobj`, not the committed checker):

```
$ python3 - <<'PY'
import hashlib, json, zlib
img = open('corpus/fixtures/firmware-r63/firmware-r63.bin','rb').read()
truth = json.load(open('corpus/fixtures/firmware-r63/truth.json'))
print('image_bytes', len(img), 'sha256', hashlib.sha256(img).hexdigest())
for truth_r in truth['regions']:
    if truth_r.get('kind') != 'zlib':
        continue
    off = truth_r['offset']
    d = zlib.decompressobj()
    out = d.decompress(img[off:]); out += d.flush()
    consumed = len(img[off:]) - len(d.unused_data)
    print('offset', off, 'consumed', consumed, 'eof', d.eof,
          'unused', len(d.unused_data), 'decompressed_bytes', len(out),
          'decompressed_sha256', hashlib.sha256(out).hexdigest(),
          'truth_key', truth_r.get('name'))
    print('  next_byte_after_member', img[off+consumed:off+consumed+1].hex())
for p in [r for r in truth['regions'] if r.get('kind') == 'padding']:
    span = img[p['offset']:p['offset']+p['size']]
    print('padding', p['offset'], p['size'], 'all_zero', set(span) <= {0})
PY
image_bytes 2048 sha256 bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be
offset 512 consumed 79 eof True unused 1457 decompressed_bytes 78 decompressed_sha256 a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86 truth_key diagnostic-note
  next_byte_after_member 00
offset 1024 consumed 90 eof True unused 934 decompressed_bytes 97 decompressed_sha256 2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9 truth_key component-note
  next_byte_after_member 00
padding 0 512 all_zero True
padding 591 433 all_zero True
padding 1114 934 all_zero True
```

Reading: the record's `reported_size` 79 and 90 are exactly the compressed member
lengths consumed by zlib (both `eof=True`, next byte `0x00`), the decompressed digests
match `truth.json`, and the three padding spans are all-zero — consistent with
`coverage=signature_scan` reporting only signature regions.

## V7 — census / counter parity

```
$ python3 - <<'PY'
import json, pathlib
root = pathlib.Path('/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs')
hits = []
for p in sorted(root.rglob('*.json')):
    try: d = json.loads(p.read_text())
    except Exception: continue
    if isinstance(d, dict) and d.get('operation') == 'inspect_firmware_regions':
        hits.append((str(p.relative_to(root)), bool(d.get('evidence_id')),
                     d.get('normalized_result') is not None))
print('count=', len(hits)); [print(h) for h in hits]
PY
count= 1
('round-63/inspection.json', True, True)     # (path, has evidence_id, has non-null normalized_result)
```

Exactly one counted saved record for this surface operation, at the round-63 path, with
`evidence_id` and non-null `normalized_result` — the predicate the frozen counter uses
for C07's `ROW_OPS` and the `firmware` family. Red-before receipt
(`reports/round-64/measure-before.log`) prints `SAVED_RECORDS=59`, `K_ROW C07
status=frontier`, `README_TOKEN_LEGEND_MISMATCH=1 rows=['C07']`; `corpus/README.md:36`
still reads `| C07 | firmware images | — | — | frontier |`. Record evidence exists, so
the mismatch is genuine and the token is stale by the legend's own definition until C1
lands; no candidate knowledge entry was present at verification time
(`ls corpus/knowledge/round-64-*` → no such file), so the citation inside the C1 entry
cannot yet be checked from this seat.

## V8 — receipt self-sufficiency probe (carried LOW reconfirmed)

```
$ cd /tmp/revenger-r64-review/rerun && env -u REA_BINWALK_COMMAND \
  TMPDIR=/tmp/revenger-r64-review/tmp npx -y rea-agents@6.5.0 inspect-firmware-regions \
  <fixture> --format json > clean.json 2> clean.err
EXIT=1
--- stdout bytes: 514
{"code":"capability_unavailable","category":"unsupported_provider","message":"This integration requires Linux and an absolute REA_BINWALK_COMMAND path to the caller-supplied tool","retryable":false,...}
```

The receipt's command line alone does not record the environment variable the route
requires; the missing value is recoverable from the record
(`normalized_result.engine.executable_path=/usr/bin/binwalk`, version 3.1.0). Same
carried LOW as round-63 L2; contract C2(b)-shaped fields are unaffected because the
receipt is not claimed to be a standalone replay recipe.

## V9 — LSP availability record

No language server is applicable or mounted: `xd://lsp` is absent from this seat
(mounted devices: `ast_edit`, `debug`), and the targets are JSON data artifacts plus a
Python checker with no server configuration. All semantics above are byte re-derivation
and the shipped package's own parser, recorded as the semantic-proof substitute.

## Findings

**HIGH / MEDIUM: none.**

**LOW**

1. **Receipt is not a standalone replay recipe** (carried round-63 L2, reconfirmed V8):
   `REA_BINWALK_COMMAND` is required by the route but absent from the recorded command;
   the host currently exports it globally. Recoverable from the record's engine block.
2. **Evidence ID is content-bound, not provenance-bound** (V2 S3 M5/M6): a record whose
   ID is recomputed over assembled semantics is accepted by the shipped parser. The
   record's authenticity rests on independent re-run structural equality (V5), the
   live-engine hash match (V5) and the oracle (V6), not on the ID. C1 must keep its
   "observation layer only" wording; the ID must not be presented as cross-run identity
   (a re-run necessarily differs because `raw_result` embeds the temp staging path).
3. **Dependency, not a defect:** the round-64 C1 candidate entry is not landed at
   verification time; this seat certifies the record/receipt/fixture bindings only, not
   the candidate entry's citations. Admission still needs the entry plus its independent
   Q01–Q13 passes.

## Residual risk

- An assembled-but-self-consistent record (same package code recomputing the ID over
  fabricated semantics) is indistinguishable from a producer output by ID alone; the
  mitigations are the fresh re-run's structural equality, the hash-matched live engine,
  and the fixture-scoped oracle. LEDGER U4 stands and is correctly disclosed.
- The oracle is fixture-scoped: agreement proves this authored 2048-byte image against
  this binwalk 3.1.0 build and this route; it proves nothing about firmware inspection
  generally (LEDGER I1/I5/U1–U3/U6).
- The record's reported region sizes are provider-reported
  (`size_basis=provider_reported_validation_unknown`); the oracle confirms them for this
  fixture only.

## Verification gaps

- The original 1.2966 s producer invocation cannot be replayed; V5 is a fresh process
  under a scratch `TMPDIR`, not the original one.
- The frozen counter was not executed by this seat (other seats own measurement); the
  C07 `ROW_OPS`/family membership above is read from `reports/round-64/measure.py` and
  the committed red-before log.
- Candidate knowledge entry absent (V7), so entry-level citation integrity is unverified
  here.

## Tooling record

- No installs, no upgrades, no pacman (host pause respected). `npx -y rea-agents@6.5.0`
  resolved from the existing cache `/home/vgpnk/.npm/_npx/ad9a3fdbcad992c6`
  (`package.json` version 6.5.0); one producer re-run plus one clean-env failure probe.
- Scratch `/tmp/revenger-r64-review/` (scripts, re-run outputs; ~50 KB) is lane-owned;
  removal deferred to L1 landing per the round contract.
- Lane bytes: no git/jj mutation, no commit, no edit outside this file and the seat
  report; `corpus/live` and `corpus/fixtures` working trees observed clean.
