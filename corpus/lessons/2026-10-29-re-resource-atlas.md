# 2026-10-29 — RE resource atlas (interactive, operator-directed; not a numbered round)

author: REVENGER_SHOKUNIN (L1 integrator) · scouts: ReDisasmGroundTruth, ReFormatSpecs, ReEmulationBehavior, ReFrameworkTargets, ReFirmwareAndArchives, ReObfuscationAnalysis, ReLearningAndPractice, ReToolbenchInstaller · pack authors: SHOKUNIN_BINARY_FORENSICS and its six Bf* workers · no wave, no claim freeze, no scored axis. Operator directive: curate the best and most obscure reverse-engineering resources for the corpus, connected to REA, the Claude-Red techniques, the binary-forensics lane, `mint-agent.sh` and the kimi-shokunin plugin.

## Gate — source curation

Rows S110–S414 (305) were appended to `corpus/SOURCES.md`; the REA quick-start slice's 12 queued host-doc/lead rows follow as S415–S426 (one of its 13 proposed rows was already registered). `S096–S109` belong to the C10 EvidenceLedger curation (`2026-10-29-evidence-ledger-curation.md`) and were not touched. No existing row changed `status`, `recheck` or `used-by`.

| step | what was done | evidence |
|---|---|---|
| open | each scout/pack author fetched the primary page, pinned commit/tag/revision, copied one ≤25-word quote | `reports/round-73/scout-packs/*.md`, `reports/round-73/bf-source-pack/*.md` (each with its own search log) |
| re-open (non-author) | integrator parsed every block and re-fetched its URL; quote must be a whitespace/markup-normalised substring of the page (PDFs via `pdftotext`) | first pass 350 blocks → 309 matched; final-registry pass `reports/round-73/verify_quotes.log`: 296 OK, 9 MANUAL, 0 FAIL |
| manual re-open | six quotes the script could not match but the integrator located by hand with the `read` tool: Phoenix abstract (S115), Compiler Explorer README (S130), SLEIGH overview (S131), Mandiant GoReSym blog (S398), Intel SDM index (S379), RE Stack Exchange help (S400) | anchors carry `[integrator re-opened and located the quote]` |
| single-opener | three rows whose host blocks scripted fetches (Arm ARM S381, AMD APM S380, Schrittwieser CSUR doi S343) rest on the scout's own read | anchors carry `[single-opener …]` |
| tier/kind rule | `community` never tier A; the census validator prints no E-codes | `sources-census.sh validate --file corpus/SOURCES.md --today 2026-10-29` |
| dedupe | canonical-URL match against all previously registered rows (S001–S109) and within the batch; 23 duplicates dropped | `reports/round-73/dropped.tsv` |

Dropped without a row (45): 21 quotes not reproduced by the integrator re-fetch (BiNit HAL page, Dogbolt site text from the scout row, diffoscope README, Packin' Heat, QSynth NDSS page, Ghidra class README, PoC||GTFO README, tmp.out #2, Apple ARM64 page, Linux `module_signature.h`, Go `symtab.go` at master, Godot PCK reader, Ian Lance Taylor's linkers part 8, a second uops.info row, and 7 BF spec-pack blocks whose heading keys did not match the verification run and which largely duplicate scout rows under other URLs), 23 duplicate URLs, and 1 BF-pack row (Nightmare site) that contradicted the lane's own rejection of exploitation-training material (S401, S402). They remain leads; `reports/round-73/dropped.tsv` lists each with its reason.

Rejected rows (kept as evidence): see the `rejected` rows in S110–S414; each carries a located quote and a flip condition (Q12). They include `mal_unpack` (S249, executes live malware), `unlicense` (S250, executes the target to strip a commercial protector), CHIPSEC (S321, live-host testing), Nightmare (S401) and ROP Emporium (S402) (exploitation training). SHOKUNIN_BINARY_FORENSICS' own in-pack rejections (Yurichev PDFs behind a paywall, Levine's *Linkers and Loaders* removed, OST malware samples, the crackmes-RE dataset's benchmark-contamination notice, Corkami stubs and others) stay in `reports/round-73/bf-source-pack/*.md`.

## Gate — knowledge entry

`corpus/knowledge/round-73-re-resource-atlas.md` (`admission-status: candidate`). Criteria checked by the author; no non-author gate has run, so none of this is admitted:

| id | self-check | note |
|---|---|---|
| Q01 | PASS-with-flags | every claim is the row's quote scoped to its pin; tier-C rows are never sole support; 3 single-opener rows named |
| Q02 | PASS | header trio + `coverage-map` (C16 proposed, README map not edited by this entry) |
| Q03/Q11 | n/a | no derived value (count, offset, digest) is asserted beyond the quote-match counts, which carry their command in `verified-at`/`recheck` |
| Q04/Q05 | PASS | host tool facts are pointed to `reports/round-73/tool-probes.md` (version command and one probe per tool) and are not restated as capability |
| Q10 | PASS | `adjacent` fit marked on rows that also document live or extraction features |
| Q13/Q16 | UNGUARDED | the verifier credits only quote reachability; it does not guard `teaches` sentences or the routing table |
| Q14/Q15 | n/a | no hex-with-length or git-identity sentence in the entry |

## Mistakes

| class | evidence | captured-by | fix |
|---|---|---|---|
| scout quote not reproducible on re-fetch | 21 blocks (above); several were HTTP 403 / JS-rendered / PDF-text pages the scout read through another route | `reports/round-73/verify_quotes.py` | rows kept only when re-matched or manually re-opened; the three single-opener rows are labelled |
| my first verifier compared the *last* quoted string of the anchor | it reported 24 FAILs, 14 of them quote-selection artefacts | rerun with all quoted segments and `pdftotext` (`/tmp` script, then committed as `verify_quotes.py`) | committed verifier tests every quoted segment ≥3 words |
| id-space collision risk | two curators planned `S096+` simultaneously | explicit id-range agreement over IRC (EvidenceLedger S096–S109, this work S110+) | ids assigned only by the integrator at merge; pack files carry none |
| BF candidate entry still cites `pack:<file>/<heading>` keys | by design until ids existed | `reports/round-73/source-id-map.tsv` maps heading → `S###` | sibling entry owner replaces keys |

## Tools installed or updated (operator directive)

By `REVENGER_SHOKUNIN.ReToolbenchInstaller`; full table with versions, channels, checksums and probes in `reports/round-73/tool-probes.md`. Channels: pacman official repos (ghidra, yara, capstone, keystone, unicorn, pwndbg, gef, diffoscope, checksec, rz-cutter, wabt, binaryen, patchelf, ltrace, dotnet-sdk, python-pefile), `uv tool` (flare-capa 10.0.0, flare-floss 3.2.0 on Python 3.12, pyinstxtractor-ng), dedicated venv (LIEF 1.0.0), `dotnet tool` (ilspycmd 11.2.0), official GitHub releases with recorded sha256 (Detect-It-Easy 3.21, ImHex 1.38.1, kaitai-struct-compiler 0.11, apktool 3.0.3, rr 5.10.0, capa-rules v10.0.0). Not installed: pycdc and `ksv` (AUR-only). No `pacman -Sy/-Syu` was run. Installed does not mean ready: a route is ready only after its own probe (Q05).

## Trend verdicts

- Expansion: improved — SOURCES 95 → 426 rows (S110–S414 new, plus S096–S109 from the sibling C10 curation); breadth only, no lane run followed.
- Quality: unchanged — no admitted entry was re-checked or strengthened; the new entry is a candidate.
- Discernment: improved narrowly — 45 candidates were excluded on re-fetch evidence, a verifier script is committed, and single-opener rows are labelled; the outside spot-check of this curation is still pending.

## Next

One route from the atlas → one authored byte-oracle fixture → one tool scored against it (Q03/Q04/Q13). Suggested first routes: Go pclntab (S152, S211, S258) or the WASM name section (S163 with wabt S287) — both have a primary spec, a recovery tool with its own limitation text, and a tool already installed on this host.
