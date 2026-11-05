# corpus — revenger index

What this corpus holds, which province surfaces its knowledge covers, and the
frontier it is working toward. Province: `PROVINCE.md`. Admission bar:
`QUALITY.md`. Where the lane learns: `SOURCES.md`.

## Index

- `QUALITY.md` — admission criteria Q01–Q17 (Q11 supersedes Q08), each citing its mistake class.
- `SOURCES.md` — where the lane learns: tiered, opened sources with study paths and search log (contract v1).
- `knowledge/` — admitted domain entries (the map below names each one); also
  retains clearly marked rejected candidates (each carries an
  `admission-status: rejected` header), which are evidence, not admitted knowledge.
- `lessons/` — `2026-10-12-r1-provider-gap.md`; `2026-10-27-bounty-triage-module.md` (interactive, non-round); `2026-10-29-evidence-ledger-curation.md` (interactive C10 EvidenceLedger source gate); `2026-10-29-re-resource-atlas.md` (interactive RE resource atlas source gate, S110–S426); `round-1.md` (fleet round-1 gates and the mined `## Mistakes` table); `round-1-verifier-spotcheck.md` (integrator-written outside check of round 1); `round-N.md` (round gate, mistakes and source changes) with `round-N-verifier-spotcheck.md` (outside check) for completed rounds when present — `ls corpus/lessons` is the authority for exact files.
- `fixtures/` — authored known-truth inputs (byte-oracle fixtures; `fixtures/REPLAY.md`).
- `live/runs/` — saved REA outputs, receipts and non-author reviews per historical round.
- `verify_*.py` — saved-ledger replay verifiers (`--self-test`); census command in `SCORECARD.md` (C).
- `snapshots/` — byte-exact committed copies of the specifications the APK entries cite (`ResourceTypes.h`, `APPNOTE.TXT`, `dex-format.html`, `rea-android-applications.md`); each digest is printed by the entry that cites it.
- `audit_source_quotes.py` — committed fetch-receipt quote audit (`verify` / `chains` / `self-test`);
  read-only over committed bytes, no network.
- `census_reprobe.py` — host-readiness census re-probe (round 89, experimental, NOT admitted:
  see `SKILL.md` §Gate registry for its measured limits); re-derives the 18 census rows from
  the live host and prints `CENSUS_STALE_UNFLAGGED`.
- `q15_tree_id_check.py` — Q15 tree-identity sentence checker (`--self-test`, `--scan`).
- `derive_axml_anchors.py` — prints the `ResourceTypes.h` line numbers and enum values an APK entry cites, from the pinned snapshot.
- `check_embedded_outputs.py` — embedded-output verbatim gate (`--entry`, `--self-test`); reads `embedded_output_pins.json`.
- `derive_axml_anchors_r68.py` — byte-exact earlier revision of the derivation script (sha256 `bce497d6…`), pinned in `embedded_output_pins.json` so the retained round-68 candidate re-derives against the revision that printed it.
- `self_assessment_check.py` — counts the lane's self-assessment mismatches against repo state (classes SM1–SM6; `--root`, `--self-test`).
- `self_assessment_check2.py` — v2 of the above (round 90 C1): SM6 checks the K statement's numerator AND denominator against the map (v1 hard-coded `/14`); SM1–SM5 unchanged. v1 bytes stay as the frozen r70 instrument.
- `self_assessment_check3.py` — v3 of the above (round 91 C1): SM6 reads the K statement in the **stated before→after cell** of the lane's own SCORECARD row instead of the last token-adjacent `N/D` anywhere on the line (the r90 critic's pointer-cell defect); SM1–SM5 unchanged, v2 bytes stay as the frozen r90 instrument.
- `lint_entry.py` — mechanical pre-flight lint for a knowledge entry (§Q-map completeness, Q14 byte-count heuristic, unresolved commit ids, header trio); not an admission gate.
- `training/bounty-triage/` — instruction module for authorized, artifact-first bounty
  triage (`MODULE.md`), its package validator (`check_package.py`), and two offline
  exercise packages. Instruction only: it fills no coverage row and is not an admission
  gate; `check_package.py` validates structure and evidence binding, not truth.

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
| C02 | native analysis sessions (decompile/disassemble providers) | `knowledge/round-96-native-analysis-sessions.md` (round-96 admission; REA's documented native routes at the pinned revision plus one demonstrated session on this host, 2026-11-05) | `live/runs/20261012T163909Z/native-analyze.json` (`provider_unavailable`); `lessons/2026-10-12-r1-provider-gap.md` | held |
| C03 | managed (.NET/CLI) assemblies | `knowledge/round-92-managed-assembly-metadata-evidence.md` (round 92; two authored inert PE/CLI fixtures, four saved producer records; fixture-scoped, no general .NET claim) | `fixtures/managed-r76`, `fixtures/managed-r85`; `live/runs/round-76/`, `live/runs/round-85/inspect-managed-*` (oracle receipts 20/20, 47/47, 39/39) | held |
| C04 | JavaScript/Electron packages | `knowledge/round-62-commonjs-require-name-evidence.md` (source names and saved call spans on authored directories only; no Electron/runtime/export-binding ground) | `fixtures/js-r3`, `js-r7-v2`, `shapes-r12`; `verify_js_graph_delta.py`, `verify_semantic_trace.py`, `verify_shape_evidence.py`; shape/semantic work is outside the new entry; retained rejected candidate `knowledge/commonjs-destructured-require-edges.md` | held |
| C05 | Android packages (APK) | — | `fixtures/apk-r65`; retained rejected candidates `knowledge/round-65-apk-axml-byte-evidence.md` (round-65 wave, falsified Q02/Q06/Q11), `knowledge/round-67-apk-axml-byte-evidence.md`, `knowledge/round-68-apk-axml-byte-evidence.md`, `knowledge/round-69-apk-axml-byte-evidence.md` and `knowledge/round-70-apk-axml-byte-evidence.md` (each `admission-status: rejected`; the round-70 v5.1 candidate failed three of sixteen wave-2 decisions, Q04/Q11b/Q13, `corpus/lessons/round-70.md` `## Gate`); `knowledge/round-71-apk-axml-byte-evidence.md` (sixth-pass candidate retained rejected after Q09/Q16 wave-2 FAILs, `.ufo/waves/round-71/w2/R71W2Q09Q12.md` and `R71W2Q13Q16.md`; gate 24/24 and lint 0/0/0/0 were necessary but not admission) | uncovered |
| C01 | native static: PE resource directory (`.rsrc`) | `knowledge/pe-resource-directory-layout.md` | `fixtures/pe-r27`…`pe-r59d`; `verify_*icon*.py`, `verify_pe_resources.py` | held |
| C07 | firmware images | `knowledge/round-64-firmware-region-byte-evidence.md` (manual byte-derived readout of `fixtures/firmware-r63/firmware-r63.bin` only; no general firmware-format, extraction/execution, provider-completeness or authenticity claim) | — | held |
| C08 | browser/Electron runtime evidence | `knowledge/round-93-browser-cdp-runtime-evidence.md` (round 93; one authored inert fixture and one saved round-77 CDP record, fixture-scoped, no general browser, Chrome, CDP or Electron claim) | `live/runs/round-77/` (CDP `inspect_web_page` over an authored loopback fixture, receipt exit 0, S447; S495 names this record) | held |
| C09 | EVM bytecode interfaces | `knowledge/round-62-evm-dispatch-byte-evidence.md` (manual authored-byte/saved-field correspondence only) | `fixtures/evm-r19`, `evm-r21`…`evm-r26` (no `evm-r20`); `verify_evm_evidence.py`; retained rejected candidate `knowledge/evm-saved-interface-candidates.md` | held |
| C10 | evidence-ledger discipline (Evidence IDs; observation/inference/unknown) | `knowledge/round-95-evidence-ledger-discipline.md` (round 95 admission, superseding the r74-rejected 2026-10-29 candidate; REA's Evidence record, session ledger, residual-unknown and completion-ledger contracts at pinned revision 12f6e09, drift-checked 2026-11-05 on S500/S501; scoped to REA's documented contracts, not a run receipt) | `corpus/SOURCES.md` (S096–S109, S500, S501); `reports/round-95/quote-receipts/`; `verify_saved_evidence.py`; `corpus/lessons/2026-10-29-evidence-ledger-curation.md` | held |
| C11 | text encodings inside artifacts (UTF-16 names, surrogates) | `knowledge/utf16-unpaired-surrogates-in-resource-names.md` | `fixtures/pe-r34`, `pe-r51`…`pe-r57`, `pe-r59` | held |
| C12 | tool and process validation against known truth | `knowledge/tool-validation-by-function-and-version.md`; `knowledge/seed.md` §Calibration strategy | authored fixtures carrying `truth.json` | held |
| C13 | fixity and provenance (digest scope, receipts versus origin) | `knowledge/digest-scope-versus-provenance.md`; `knowledge/seed.md` §Calibration strategy (fixture provenance fields only) | `lessons/round-1.md` gate, `reports/round-1/` | held |
| C14 | host readiness for REA routes | `knowledge/2026-10-12-rea-readiness-checklist.md` (re-verified 2026-10-19; pre-contract, not re-gated) | `.ufo/waves/kaika-r1/scout-freshness.md` | partial |
| C15 | Selected reverse-engineering tool repositories and declared boundaries | `knowledge/round-72-tool-landscape.md` (admitted round 94 on named project sources, re-grounded 2026-11-05 with drift-check rows S498/S499; scoped to the declared tool roles and boundaries, not tool execution, host readiness, accuracy or complete market coverage) | `corpus/SOURCES.md`; `reports/round-72/shortlink-dispositions.md` | held |

Rows 15 — `grep -cE '^\| C[0-9]+ ' corpus/README.md` (2026-10-27, observed 15). Statuses before the kaika
round's admissions are frozen at `a7acc20` (`git show a7acc20:corpus/README.md`);
statuses before round 61 at `cf02419` (`git show cf02419:corpus/README.md`,
held 4/14).

## Known gaps

- `AGENTS.md` is absent (named debt, `SCORECARD.md`). `SKILL.md` exists and carries a
  `## Gate registry` of 17 instrument blocks (`grep -c '^| name |' SKILL.md`), each row's
  `kind` saying gate or probe (from round 91: `self_assessment_check3` and
  `message_tree_check`); the ten `verify_*.py` replay verifiers are still not registered gates.
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
  authored APK fixture. Round-70 update: the fifth-pass candidate
  (`knowledge/round-70-apk-axml-byte-evidence.md`, generated from command stdout,
  gated by a 40-seat pre-gate wave then a 45-seat fresh wave) failed three of
  sixteen decisions, all on four prose sentences that credit a script for more
  than it prints (`:119`, `:152`, `:282`, `:310` of the candidate); the row is
  `uncovered`, the candidate retained rejected; the sixth pass is a repair of
  those four sentences against the printed outputs, not new fixture bytes
  (`corpus/lessons/round-70.md` `## Routed forward`).
- C08 browser/Electron runtime — passive CDP observation of a declared local page.
- Evidence custody beyond fixity: collection and transfer records
  (SWGDE collection/acquisition guidance) — adjacent to this province; enter only
  as it bears on shipped-artifact evidence ledgers.
- C10 — admitted in round 95 as `knowledge/round-95-evidence-ledger-discipline.md`
  (superseding the r74-rejected 2026-10-29 candidate; row held in the coverage map).
  Open follow-ups: a non-author re-fetch of S500/S501, and the residual-unknown
  qualification rule exercised against a fixture-scoped REA run (not claimed here).
- RE resource atlas (candidate `knowledge/round-73-re-resource-atlas.md`, sources S110–S426,
  gate `lessons/2026-10-29-re-resource-atlas.md`): breadth map of primary specs, papers,
  format tooling, framework extractors, firmware/provenance sources and practice corpora.
  A coverage row C16 is proposed (with `knowledge/re-ground-truth-resource-atlas.md`) but not
  added: a new row would change the frozen K held-row counter. The next quality move is one
  route from the atlas turned into an authored byte-oracle fixture with a scored tool.
