# corpus — revenger index

What this corpus holds, which province surfaces its knowledge covers, and the
frontier it is working toward. Province: `PROVINCE.md`. Admission bar:
`QUALITY.md`. Where the lane learns: `SOURCES.md`.

## Index

- `QUALITY.md` — admission criteria Q01–Q13 (Q11 supersedes Q08), each citing its mistake class.
- `SOURCES.md` — where the lane learns: tiered, opened sources with study paths and search log (contract v1).
- `knowledge/` — admitted domain entries (the map below names each one); also
  retains clearly marked rejected candidates (each carries an
  `admission-status: rejected` header), which are evidence, not admitted knowledge.
- `lessons/` — `2026-10-12-r1-provider-gap.md`; `round-1.md` (fleet round-1 gates and the mined `## Mistakes` table); `round-1-verifier-spotcheck.md` (integrator-written outside check of round 1); `round-61.md` (round-61 gate, mistakes and source changes).
- `fixtures/` — authored known-truth inputs (byte-oracle fixtures; `fixtures/REPLAY.md`).
- `live/runs/` — saved REA outputs, receipts and non-author reviews per historical round.
- `verify_*.py` — saved-ledger replay verifiers (`--self-test`); census command in `SCORECARD.md` (C).

## Coverage map

Status: `held` — at least one admitted knowledge entry covers the ground;
`partial` — covered only by unsourced or pre-contract text; `uncovered` — work
evidence exists but no admitted knowledge entry (a rejected candidate retained
under `knowledge/` is clearly marked in the file and is not coverage); `frontier` — no knowledge and no saved
record. Work evidence is not knowledge: fixture and run records stay in `fixtures/`
and `live/runs/`.

| row | surface | knowledge entries | work evidence | status |
|---|---|---|---|---|
| C01 | native static: PE resource directory (`.rsrc`) | `knowledge/pe-resource-directory-layout.md` | `fixtures/pe-r27`…`pe-r59d`; `verify_*icon*.py`, `verify_pe_resources.py` | held |
| C02 | native analysis sessions (decompile/disassemble providers) | `knowledge/seed.md` (census), `knowledge/2026-10-12-rea-readiness-checklist.md` | `live/runs/20261012T163909Z/native-analyze.json` (`provider_unavailable`); `lessons/2026-10-12-r1-provider-gap.md` | partial |
| C03 | managed (.NET/CLI) assemblies | — | — | frontier |
| C04 | JavaScript/Electron packages | `knowledge/round-62-commonjs-require-name-evidence.md` (source names and saved call spans on authored directories only; no Electron/runtime/export-binding ground) | `fixtures/js-r3`, `js-r7-v2`, `shapes-r12`; `verify_js_graph_delta.py`, `verify_semantic_trace.py`, `verify_shape_evidence.py`; shape/semantic work is outside the new entry; retained rejected candidate `knowledge/commonjs-destructured-require-edges.md` | held |
| C05 | Android packages (APK) | — | `fixtures/apk-r65`; retained rejected candidate `knowledge/round-65-apk-axml-byte-evidence.md` (round-65 orchestrator-dispatched wave, falsified Q02/Q06/Q11, adjudicated round-66) | uncovered |
| C06 | archives (ZIP inventory) | `knowledge/round-63-zip-central-directory-evidence.md` (manual byte-derived central-directory readout of `fixtures/archive-r2/fixture.zip` only; no general ZIP-parser, trailing-bytes, provider-completeness or authenticity claim) | `fixtures/archive-r2`, `nested-r11`, `duplicate-r15` | held |
| C07 | firmware images | `knowledge/round-64-firmware-region-byte-evidence.md` (manual byte-derived readout of `fixtures/firmware-r63/firmware-r63.bin` only; no general firmware-format, extraction/execution, provider-completeness or authenticity claim) | — | held |
| C08 | browser/Electron runtime evidence | — | — | frontier |
| C09 | EVM bytecode interfaces | `knowledge/round-62-evm-dispatch-byte-evidence.md` (manual authored-byte/saved-field correspondence only) | `fixtures/evm-r19`, `evm-r21`…`evm-r26` (no `evm-r20`); `verify_evm_evidence.py`; retained rejected candidate `knowledge/evm-saved-interface-candidates.md` | held |
| C10 | evidence-ledger discipline (Evidence IDs; observation/inference/unknown) | `knowledge/seed.md` §Verification discipline | `verify_saved_evidence.py` | partial |
| C11 | text encodings inside artifacts (UTF-16 names, surrogates) | `knowledge/utf16-unpaired-surrogates-in-resource-names.md` | `fixtures/pe-r34`, `pe-r51`…`pe-r57`, `pe-r59` | held |
| C12 | tool and process validation against known truth | `knowledge/tool-validation-by-function-and-version.md`; `knowledge/seed.md` §Calibration strategy | authored fixtures carrying `truth.json` | held |
| C13 | fixity and provenance (digest scope, receipts versus origin) | `knowledge/digest-scope-versus-provenance.md`; `knowledge/seed.md` §Calibration strategy (fixture provenance fields only) | `lessons/round-1.md` gate, `reports/round-1/` | held |
| C14 | host readiness for REA routes | `knowledge/2026-10-12-rea-readiness-checklist.md` (re-verified 2026-10-19; pre-contract, not re-gated) | `.ufo/waves/kaika-r1/scout-freshness.md` | partial |

Rows 14 — `grep -cE '^\| C[0-9]+ ' corpus/README.md`. Statuses before the kaika
round's admissions are frozen at `a7acc20` (`git show a7acc20:corpus/README.md`);
statuses before round 61 at `cf02419` (`git show cf02419:corpus/README.md`,
held 4/14).

## Known gaps

- `SKILL.md` and `AGENTS.md` are absent (named debt, `SCORECARD.md`); no gate
  registry exists, so no verifier here is registered as a gate.
- Two pre-contract entries (`seed.md`, the readiness checklist) carried no
  `source:` / `verified-at:` / `recheck:` headers at `8bbcb4e`; headers and a
  dated re-verification were added on 2026-10-19, but neither entry has been
  re-gated against `QUALITY.md`.

## Frontier

Ground being explored and not yet held, nearest first.

- C07 firmware — REA `inspect_firmware_regions` / `extract_firmware` need
  caller-supplied Binwalk 3.1.x and Unblob 26.6.x; the host has binwalk 3.1.0
  and unblob 26.6.4 (`.ufo/waves/kaika-r1/scout-freshness.md`). Presence is not
  readiness: an authored known-truth firmware fixture is the next probe.
- C03 managed assemblies — REA `inspect_managed_artifact`; `dotnet` is on PATH
  but reports no SDK, so a locally built known-truth assembly is blocked.
- C05 Android — REA `inspect_android_package`; jadx 1.5.6 is present; needs an
  authored APK fixture. Round-66 update: the authored `fixtures/apk-r65` bundle
  landed with a candidate entry that the dispatched round-65 wave falsified
  (Q02/Q06/Q11 — `corpus/lessons/round-66.md` `## Gate`); the row is
  `uncovered`, the candidate retained rejected; a re-gate needs the corrected
  text, not new fixture bytes.
- C08 browser/Electron runtime — passive CDP observation of a declared local page.
- Evidence custody beyond fixity: collection and transfer records
  (SWGDE collection/acquisition guidance) — adjacent to this province; enter only
  as it bears on shipped-artifact evidence ledgers.
