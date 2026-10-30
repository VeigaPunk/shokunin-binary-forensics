source: S110–S414 as merged into `corpus/SOURCES.md` on 2026-10-29; heading→id map `reports/round-73/source-id-map.tsv`. Rows cited here: S054, S115, S114, S123, S125, S126, S131, S134–S140, S144, S147, S148, S155–S157, S164, S181–S204, S212, S223, S225, S226, S233, S251–S256, S258, S277, S294–S305, S358, S360, S371–S377, S379, S382, S383, S388, S403–S412. Pack blocks with the located quotes are in `reports/round-73/bf-source-pack/{specs-abi,format-obscura,triage-tools,research-papers,ecosystems,learning}.md`. REA route names are file names under `~/.local/share/rea/docs/` (REA checkout `12f6e0974cc0db0b3a9b86246accc76556837222`, 2026-10-25, package.json 6.7.0).
verified-at: 2026-10-29. The curator sampled pack quotes: 30 blocks parsed from the five non-obscura packs (21 full-quote matches on the fetched page; 9 line-wrapped or JS-rendered pages matched by hand on a 3–6-word key phrase or the unrendered source) and all 26 format-obscura blocks (23 full matches, 3 key-phrase matches). The lane owner separately re-ran its own quote verifier over the merged rows (`reports/round-73/verify_quotes.py`); candidates it could not reproduce were dropped to `reports/round-73/dropped.tsv` and are not cited here as rows. Nothing was installed or run for this entry.
recheck: `python3 -B reports/round-73/verify_quotes.py --ids S110-S414` from the lane root for the rows; for GitHub-hosted rows compare `git ls-remote <repo> HEAD` with the row's recorded sha; for the REA crosswalk re-read the named REA doc head.
coverage-map: proposes a new row C16 — independent primary-source oracles per REA route (where each REA claim can be checked against something other than REA). `corpus/README.md` has no C16 row (adding one would change the frozen held counter); C03, C07 and C08 gain named oracles but stay frontier/partial until a fixture-backed entry exists.
admission-status: candidate

# Independent oracles for REA routes: a primary-source crosswalk

## Scope

REA reports Evidence about artifacts (S054). The lane's discipline (QUALITY Q03) requires an expected value derived from bytes, a specification, or a pin fixed outside the record under test. This entry maps each REA route to the specifications, maintainer sources and original papers that can serve as that outside source, plus obscure corpora showing where real parsers disagree with the specs. It is a reading map, not a capability claim: no REA route, tool or sample was run; every statement is what a cited source says, scoped to its version.

Lane limits (`PROVINCE.md`): static, artifact-first, no live targets, no malware samples, no DRM circumvention. Sources that instruct otherwise were rejected (below).

## Crosswalk: REA route → where to check it

| REA route (doc) | Independent oracle(s) | What it fixes | Caveat to carry |
|---|---|---|---|
| `elf-notes`, `binary-diagnostics` | psABI `object-files.tex` S135; Linux kernel ELF idiosyncrasies S196; tmp.out "Dead Bytes" S197, "ELF Mangling Pt.4 Limit Break" S198, kernel-loader deep dive S199, 57-byte ELF S200; Drepper DSO HOWTO S406; LWN "How programs get run" S407; Godbolt "Bits Between the Bits" S408; Bendersky PIC S412 | Section vs segment views, which header bytes the kernel loader ignores and which duplicate program header it honours, `.eh_frame` CIE/FDE bytes, x86-64 section/type constants | Loader behavior is kernel-version scoped (S198 records a 2020 loader change); psABI row is TeX source, x86-64 only |
| `pe-imports`, `pe-load-config`, `pe-certificates` | "Lost in the Loader" S194 and `loaders_modeling` S195; Corkami `PE.md` S182 and `pocs/PE` readme S183; pefile malformed-PE handling S193; Microsoft x64 exception handling S140 (`.pdata`) | What a PE needs to be accepted by a loader vs what a parser tolerates; reference-reader behavior behind imphash | Loader models cover Windows XP/7/10; Corkami results are version-scoped; pefile is a reader, not a loader |
| `apk-signature` | Android APK Signature Scheme v2 S294, v3 S295, v4 S296 | Signing-block layout, digest computation, rotation lineage | REA's doc covers v1/v2/v3/v3.1; v4 is a recorded coverage gap |
| `electron-fuses`, `electron-observation`, `javascript-artifact-reconstruction` | Electron Fuses S297; ASAR integrity S298; `@electron/asar` README S277; Chrome DevTools Protocol S299 | Fuse wire format and sentinel, which fuses gate ASAR integrity, ASAR header layout | CDP is a live-target surface: read it to interpret recorded observations, not to connect (outside this province) |
| `managed-code-analysis` | ECMA-335 6th ed. S136 | CLI metadata physical layout and stream rules (REA's doc itself cites ECMA-335 for omitted `#Blob`) | 2012 edition; Portable PDB and augments are unopened leads |
| `python-pyc`, `python-packaged-applications` | PEP 552 S164; PyInstaller `archive/readers.py` S305 | pyc flag/hash-based fields; CArchive cookie and TOC | S305 is maintainer source at one commit, not a format standard |
| `go-binaries`, `rust-binaries` | Go `internal/abi/symtab.go` pclntab magics S258; Rust v0 mangling S155 and RFC 2603 S156 | Toolchain-era check independent of build info; crate/disambiguator recovery from symbols | REA reads build metadata, not pclntab, so this is a cross-check, not a mirror |
| `firmware-analysis`, `raw-binary` | OFRAK S251, UEFITool S252; EDK2 `PiFirmwareVolume.h` S304; DeviceTree flattened format S300; Corkami "Abusing file formats" S181; PoC‖GTFO index S185 and "The Treachery of Files" S186; PolyFile S188; `magic(5)` S190; APE spec S201; Koch et al. polyglots S204; ImHex-Patterns S191; 010 Editor templates S192 | Container identification at non-zero offsets, polyglot/chimera vocabulary, a second parser for UEFI volumes, FDT v16/v17 differences | The UEFI PI spec returned HTTP 403 for every URL tried; EDK2's header is the reference implementation at PI 1.6 |
| `devicetree`, `sqlite-databases`, `kernel-modules`, `erlang-beam` | DT spec S300; SQLite file format S301; kernel module-signing doc S302; OTP `beam_file.c` S303 | Header fields, db/WAL relation, appended-signature trailer, BEAM chunk-scan rule (the pack author reads the loop as "later duplicate wins") | No official byte-level BEAM document was found; S303 is runtime code at one commit |
| `godot-pck` | none admitted | — | The pack's Godot `file_access_pack` row and the Linux `module_signature.h` row were dropped by the lane verifier (`dropped.tsv`); no admitted oracle for PCK |
| `apple-application-analysis`, `apple-ips` | XNU `loader.h` S144 and `fat.h` S138 | Mach-O/FAT constants and big-endian fat header | Only the first ~120 lines of `loader.h` were read by the pack author; LC_* constants unchecked |
| `native-function-matching` | Diaphora S225, BinDiff S223, ghidriff S226; BinKit S358; Debin S372; DIRE S360 | A different matcher to disagree with; why build differences break similarity; predicted names are not original names | Diaphora needs IDA; ghidriff shares Ghidra's analysis substrate so it is not independent of Ghidra bugs |
| `native-investigation`, `ghidra-provider`, `reconstruction-*` | Dogbolt S253, rev.ng S254 and CC'17 paper S374, RetDec S126, rz-ghidra S256, Cutter S257; Phoenix S115; "No More Gotos" S114; Retypd S371; Taxonomy of C Decompiler Fidelity Issues S373; SLEIGH S131; remill S123/S376; McSema S125; lifter SoK S377; Ghidra class docs S403–S405 | Why pseudocode is a hypothesis: goto-free structuring is not semantics-preserving by default, types in stripped code are inferred, indirect target sets are not statically enumerable | Mostly abstract-page evidence; Dogbolt retains and shares uploads and has no API, so public samples only and never automated |
| `binary-diagnostics` (emulation hints) | Unicorn FAQ S255 | REA's doc pins Unicorn 2.1.2; the FAQ's "< 2.1.4" PC-sync caveat covers that version | Not tested whether REA's PLT inference reaches the affected path: an unknown, not a finding |
| *(no REA route)* | LLVM PDB S147 and MSF S148, pdb-rs S137; Itanium C++ ABI S157 and EH S134; AAPCS64 S139; Microsoft x64 `.pdata` S140; Intel SDM index S379; Agner calling conventions S382; uops.info S383; instruction reference S411 | Candidate oracles if those routes are added or checked by hand: PDB superblock and stream directory, vtable/RTTI/mangling, `.eh_frame` and LSDA semantics, calling conventions | LLVM/pdb-rs are tier B; S379 pins SDM version 093 only; S383 is adjacent-fit |

## Study paths (ordered)

1. **How an ELF actually gets loaded**: Drepper S406 → LWN S407 → Godbolt S408 → kernel ELF idiosyncrasies S196 → tmp.out Pt.4 S198 → psABI S135. Concepts first, then loader reality, then byte oracles.
2. **How a PE actually gets loaded**: Corkami PE notes S182 → PE corpus readme S183 → "Lost in the Loader" S194 → `loaders_modeling` S195 → pefile S193.
3. **How to doubt a decompiler**: Ghidra class "Improving Disassembly and Decompilation" S403 → Phoenix S115 → "No More Gotos" S114 → Retypd S371 → Debin S372 / DIRE S360 → Taxonomy S373 → Dogbolt S253 (manual, public samples only). Vendor caveat, algorithm limits, inference limits, measured defects.
4. **What a file is**: Corkami "Abusing file formats" S181 → "Treachery of Files" S186 → PolyFile S188 → `magic(5)` S190 → Koch et al. S204.
5. **Calling conventions and instruction facts**: Raymond Chen S410 → Agner Fog S382 → instruction reference S411 → uops.info S383 → AAPCS64 S139.

## Rejected or not admitted, with the reason carried

- Reverse Engineering for Beginners (S386 lineage): PDF redirects to a paywall page; GitHub repos returned 404 (learning pack).
- Linkers and Loaders: chapters removed ("due to chronic piracy"); only errata readable (learning pack).
- OST "Reverse Engineering Malware": ships live samples in a password-protected zip; the lane forbids sample download (learning pack).
- crackmes-RE dataset: README forbids appearing in training corpora; binaries come from a live archive (learning pack).
- Nightmare (S401): rejected row (exploitation training), not used here.
- Binary Ninja Free as the lane's automated tool: license clause 5 restrictions (triage-tools pack).
- Dogbolt as an automation oracle: "there is intentionally no public API for automation" (triage-tools pack).
- Dropped by the lane's quote verifier and therefore not cited as rows: Apple arm64 platform doc, Taylor "Linkers part 8", Godot `file_access_pack`, Linux `module_signature.h`, PoC‖GTFO mirror README, tmp.out "Some ELF Parser Bugs" (`reports/round-73/dropped.tsv`). The curator matched some of these on a key phrase (the pages wrap lines); the lane verifier's stricter match did not, so they remain pack-only leads.
- x86-64 psABI PDF artifact URL: HTTP 404; the TeX source (S135) is used instead.
- Corkami PDF notes, InitialValues, `formats`, `sbud`, `pocs` root readme: no REA route, stale, or stubs (format-obscura pack).

## §Q-map

| Q | decision | entry evidence / boundary |
|---|---|---|
| Q01 | PARTIAL | Rows are tier A for the scope in each row, tier B where marked in the pack (LLVM PDB, pdb-rs, Intel SDM index, Corkami PE notes, tmp.out, PoC‖GTFO); none is sole support. Several research rows rest on abstract pages only. The lane verifier run of 2026-10-29 (`verify_quotes.py --ids S110-S414`) marked two cited rows MANUAL, not machine-reproduced: S131 (SLEIGH, `quote-not-found`) and S379 (Intel SDM index, HTTP 403); the claims resting on them (SLEIGH semantics, SDM version pin) are leads until a manual re-open is recorded. |
| Q02 | PASS | `source:` names S-rows; `verified-at`, `recheck`, `coverage-map` present. |
| Q03 | n/a | No expected value is derived. |
| Q04 | PASS | No tool is credited with output; the Unicorn/REA version relation is stated as an unknown. |
| Q05 | n/a | No readiness or capability claim. |
| Q06 | n/a | No fixture. |
| Q07 | n/a | No parser prediction. |
| Q09 | n/a | No digest or provenance claim. |
| Q10 | PASS | Each claim is scoped to its source version; Claude-Red offensive material and CTF exploit recipes are not absorbed. |
| Q11 | PARTIAL | Revision shas, dates and versions are copied from rows and packs, labeled recorded, not re-derived here. |
| Q12 | PASS | Each rejection has a located quote in its pack or a drop reason in `dropped.tsv`. |
| Q13 | n/a | No verifier is credited as guarding a clause; the lane's `verify_quotes.py` is named only as the recheck command. |
| Q14 | n/a | No hex string with a byte count. |
| Q15 | n/a | Only the REA checkout hash is asserted, recorded from `git log -1` in `~/.local/share/rea`. |
| Q16 | PASS | The curator's re-match credits only the sampled quotes (counts in `verified-at`). |

## Observation, inference, unknown

**Observation:** the cited rows, opened 2026-10-29 by their authors, state the layouts, scopes and caveats attributed to them above.

**Inference:** REA's own docs repeatedly say decoded tables, names and pseudocode are advisory, so an outside byte-level or paper-level oracle per route is the cheapest way to meet Q03. The papers support a ledger rule: record indirect-target sets as unresolved, decompiler types and names as inferred.

**Unknown:** none of these sources was exercised against an artifact; REA route behavior against any oracle is untested; the UEFI PI spec, Intel/Arm architecture manuals, Portable PDB and Mach-O headers beyond the first lines were not read; whether any REA parser agrees with its oracle is the work a later fixture round must do.
