# Round 76 claims — pre-registration (freeze)

Base: `6f3a646c691017f92012fc4cf928d9e946838b84` (r75 tip + integrator spot-check).
Two claims, distinct axes (coverage, calibration), causally separable, neither
exploratory. Probes frozen before any after-run:

| instrument | sha256 |
|---|---|
| `reports/round-76/f_probe.py` | `e15a43af56f453479681b49e063741bb008245ed758af7fc2d685aa5e64f39ed` |
| `reports/round-76/receipt_probe.sh` | `9315f8d8a2440feaca9d943b95b3eb7247a4635c0e113ee6c4101799d4bd5a11` |

## C1 — coverage, selected-family record presence (criterion F)

Author `corpus/fixtures/managed-r76/`: an inert minimal managed PE/CLI
(i386, IL-only DLL, COR20 header + BSJB metadata v4.0.30319, streams
`#~ #Strings #US #GUID #Blob`; module `r76-managed.dll`, assembly
`r76-managed` version 1.2.3.4, types `<Module>` + `R76Probe.Probe`), with a
generator that re-derives every declared premise from the built bytes
(self-check; regen byte-identical; sha256 pinned in `truth.json`). Run the
installed `rea inspect-managed-artifact <fixture> --format json` (rea 6.8.0,
built-in provider `rea-dotnet-static`, no external engine) ONCE, saving the
producer-emitted stdout bytes at `corpus/live/runs/round-76/inspection.json`
with an L1 receipt (`receipt.json`: command, exit_code, fixture_sha256,
stdout_sha256, evidence_id, duration) and `stderr.txt`. Admission condition
(all must hold): record `operation == "inspect_managed_artifact"`;
`normalized_result` non-null with `classification.status == "managed"`;
producer-derived module/assembly identity equal to the authored truth
(module name, assembly name + version, stream-name set); subject digest equal
to the fixture sha256; regen of the fixture byte-identical.

- **Before (red, committed `f-before.log`):** `PYTHONUTF8=1 python -B reports/round-76/f_probe.py <git-archive 6f3a646c corpus>` → `F_COVERAGE=5/8 score=6.25`, `F_FAMILIES=['archives', 'evm', 'firmware', 'javascript', 'native-static']` (exit 0).
- **After (target):** same command over the landing commit's archive → `F_COVERAGE=6/8 score=7.50`, `F_FAMILIES` including `managed`; probe exit 0.
- **Falsifier:** F stays 5/8, or any admission condition above fails, or the fixture regen is not byte-identical.
- **Boundary (disclosed):** F is presence-only (`routed-debt`, r63); the claim text — a real current-producer record on a real managed artifact with byte-derived identity — is the gate, not the counter alone. No coverage-map (K) row moves; no admission of a knowledge entry is claimed. `F_FAMILIES` base list matches SKILL.md's round-66 table (`5/8`, same five).

Counting command: `PYTHONUTF8=1 python -B reports/round-76/f_probe.py <tree/corpus>`.

## C2 — calibration, record-vs-reality receipt fidelity (new bounded criterion R)

Carries non-author carry-in item 1. S444's anchor aggregates two producer
legs into one number ("`grep -cE 'inspect_'` over the full manifest prints 0");
the per-leg re-run on this host shows the `--llms` leg prints **2**
(`inspect_macho`, `inspect_signature` — Hopper-wrapper manifest rows) and the
`rea doctor` leg prints **0**. Land a superseding registry row **S445**
(correction, `supersedes S444`) recording the exact per-leg counts
(`llms=2 (inspect_macho, inspect_signature)` / `doctor=0`) plus what the
re-open established: the manifest declares kebab-case equivalents of the F
families (`inspect-managed-artifact`, `inspect-android-package`,
`capture-browser-scenario`, `inspect-web-page`, `observe-web-session`,
`inspect-firmware-regions`, `inspect-artifact`, `inspect-evm-interface`,
`analyze-javascript-application`), and the producer's own payloads carry the
frozen snake_case names (`details.operation` in the android/firmware
provider-gate errors; the saved record's `operation` field).

Probe `reports/round-76/receipt_probe.sh` re-runs both legs on this host and
checks: (1) llms leg == 2 with exactly those two names; (2) doctor leg == 0;
(3) the S445 row records those exact values; (4) negative control — the base
S444 row's single-number record is flagged as contradicted.

- **Before (red, committed `receipt-before.log`, exit 1):** LEG3 FAIL (S445 absent); LEG4 fires (`S444_MISMATCH_FLAGGED`, base row records `prints 0`, actual llms leg 2).
- **After (target):** exit 0; `RECEIPT_LEG1=pass`, `RECEIPT_LEG2=pass`, `RECEIPT_LEG3=pass`, `RECEIPT_LEG4=S444_MISMATCH_FLAGGED`, `RECEIPT_VERDICT=green`.
- **Falsifier:** any leg disagrees at the after-run, or the negative control fails to fire (probe passes on the uncorrected base row).

Counting command: `bash reports/round-76/receipt_probe.sh` (needs `rea` on PATH; host-bound by design — criterion R is a this-host record-vs-reality check).

## Carry-in item 2 — F-counter amendment: resolved by evidence, NOT executed

The carry-in sanctioned a frozen-F-counter revision on the premise that "the
frozen F counter's operation names no longer exist in the rea 6.8.0
producer". Direct producer evidence refutes the premise:

1. `rea --llms` (6.8.0) declares kebab-case equivalents for every F family (list above; S445).
2. The producer's own provider-gate error payloads carry `details.operation: inspect_android_package` / `inspect_firmware_regions` — snake_case, the frozen names (scratch probes, 2026-11-01).
3. A real 6.8.0 record writes `operation: inspect_managed_artifact` into the exact field the frozen predicate reads (C1's saved record).

The frozen counter's name space is therefore still the producer's record
vocabulary; F was provider-gated per family (android: caller-supplied
`REA_JADX_MCP_JAR`; firmware 6.8.0 route: Linux + caller-supplied
`REA_BINWALK_COMMAND`; browser: caller-supplied CDP endpoint; managed: works
via built-in `rea-dotnet-static`), not name-drifted. Under the lane's
frozen-instrument discipline (r69: revise only on evidence; M50) no revision
is executed: predicate unchanged, families unchanged, counter bytes
unchanged. The amendment discipline's red-before duty is honored by
`f-before.log`. If the closure judge disagrees, the revision remains one
commit away; nothing in this round depends on the refuted premise.

## Separability

C1 verifies from `corpus/fixtures/managed-r76/` + `corpus/live/runs/round-76/`
alone (F probe over a tree containing them, S445 not required); C2 verifies
from `corpus/SOURCES.md` S445 + the live producer alone (receipt probe; the
fixture/run not required). Single-claim trees are demonstrated in
`f-separability.log` / `r-separability.log` at the after-measurement.

## §9 sizing

Do-nothing control at base: F stays 5/8 (no new records) and S444's wrong
single-number record stands (receipt probe red) — neither claim is reachable
without the work.
