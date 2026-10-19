# corpus — revenger index

What this corpus holds, which province surfaces its knowledge covers, and the
frontier it is working toward. Province: `PROVINCE.md`. Admission bar:
`QUALITY.md`. Where the lane learns: `SOURCES.md`.

## Index

- `QUALITY.md` — admission criteria Q01–Q10, each citing its mistake class.
- `knowledge/` — admitted domain entries (the map below names each one).
- `lessons/` — `2026-10-12-r1-provider-gap.md`; `round-1.md` (fleet round-1 gates and the mined `## Mistakes` table).
- `fixtures/` — authored known-truth inputs (byte-oracle fixtures; `fixtures/REPLAY.md`).
- `live/runs/` — saved REA outputs, receipts and non-author reviews per historical round.
- `verify_*.py` — saved-ledger replay verifiers (`--self-test`); census command in `SCORECARD.md` (C).

## Coverage map

Status: `held` — at least one admitted knowledge entry covers the ground;
`partial` — covered only by unsourced or pre-contract text; `uncovered` — work
evidence exists but no knowledge entry; `frontier` — no knowledge and no saved
record. Work evidence is not knowledge: fixture and run records stay in `fixtures/`
and `live/runs/`.

| row | surface | knowledge entries | work evidence | status |
|---|---|---|---|---|
| C01 | native static: PE resource directory (`.rsrc`) | — | `fixtures/pe-r27`…`pe-r59d`; `verify_*icon*.py`, `verify_pe_resources.py` | uncovered |
| C02 | native analysis sessions (decompile/disassemble providers) | `knowledge/seed.md` (census), `knowledge/2026-10-12-rea-readiness-checklist.md` | `live/runs/20261012T163909Z/native-analyze.json` (`provider_unavailable`); `lessons/2026-10-12-r1-provider-gap.md` | partial |
| C03 | managed (.NET/CLI) assemblies | — | — | frontier |
| C04 | JavaScript/Electron packages | — | `fixtures/js-r3`, `js-r7-v2`, `shapes-r12`; `verify_js_graph_delta.py`, `verify_semantic_trace.py`, `verify_shape_evidence.py` | uncovered |
| C05 | Android packages (APK) | — | — | frontier |
| C06 | archives (ZIP inventory) | `knowledge/2026-10-12-rea-readiness-checklist.md` (archive-tool row only) | `fixtures/archive-r2`, `nested-r11`, `duplicate-r15` | partial |
| C07 | firmware images | — | — | frontier |
| C08 | browser/Electron runtime evidence | — | — | frontier |
| C09 | EVM bytecode interfaces | — | `fixtures/evm-r19`, `evm-r21`…`evm-r26` (no `evm-r20`); `verify_evm_evidence.py` | uncovered |
| C10 | evidence-ledger discipline (Evidence IDs; observation/inference/unknown) | `knowledge/seed.md` §Verification discipline | `verify_saved_evidence.py` | partial |
| C11 | text encodings inside artifacts (UTF-16 names, surrogates) | — | `fixtures/pe-r34`, `pe-r51`…`pe-r57`, `pe-r59` | uncovered |
| C12 | tool and process validation against known truth | `knowledge/seed.md` §Calibration strategy | authored fixtures carrying `truth.json` | partial |
| C13 | fixity and provenance (digest scope, receipts versus origin) | `knowledge/seed.md` §Calibration strategy (fixture provenance fields only) | `lessons/round-1.md` gate, `reports/round-1/` | partial |
| C14 | host readiness for REA routes | `knowledge/2026-10-12-rea-readiness-checklist.md` | — | partial |

Rows 14 — `grep -cE '^\| C[0-9]+ ' corpus/README.md`.

## Known gaps

- `SKILL.md` and `AGENTS.md` are absent (named debt, `SCORECARD.md`); no gate
  registry exists, so no verifier here is registered as a gate.
- Two pre-contract entries (`seed.md`, the readiness checklist) carry no
  `source:` / `verified-at:` / `recheck:` headers at `8bbcb4e`.

## Frontier

Ground being explored and not yet held, nearest first.

- C03 managed assemblies — REA `inspect_managed_artifact`; a locally built
  known-truth assembly is the next fixture.
- C07 firmware — REA `inspect_firmware_regions` / `extract_firmware`, which need
  caller-supplied Binwalk 3.1.x and Unblob 26.6.x.
- C05 Android — REA `inspect_android_package`; needs an authored APK fixture.
- C08 browser/Electron runtime — passive CDP observation of a declared local page.
- Evidence custody beyond fixity: collection and transfer records
  (SWGDE collection/acquisition guidance) — adjacent to this province; enter only
  as it bears on shipped-artifact evidence ledgers.
