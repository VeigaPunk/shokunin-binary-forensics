# specs-abi — primary format/ABI specifications as byte-level oracles

Opened 2026-10-29 via `read` (HTTP fetch by the read tool). Scope was narrowed mid-run by SHOKUNIN_BINARY_FORENSICS
(DROP: ELF gABI, DWARF, PE-format, WASM; PRIORITISE: Itanium ABI, x86-64 psABI, ECMA-335, PDB, Mach-O, Intel/Arm refs).
The gABI `ch4.sheader.html` and PE-format and WASM `binary/modules.html` pages were opened before the de-scope notice and are
recorded only in the search-log (not included, per de-scope). No S-ids written. Nothing installed, executed or downloaded other than page text.

---

### Itanium C++ ABI (core)
- title: https://itanium-cxx-abi.github.io/cxx-abi/abi.html
- kind: spec
- tier: A
- scope: vtable layout (§2.5), RTTI/typeinfo (§2.9), member-pointer/array-cookie/guard layout (§2.3,2.7,2.8) and name mangling (§5.1) for platforms that adopt the Itanium C++ ABI (GCC/Clang on Linux/BSD/macOS, and the generic Arm64 C++ ABI that mirrors it). NOT authoritative for MSVC.
- anchor: §2.5 "Virtual Table Layout", §5.1 "External Names (a.k.a. Mangling)"; repo itanium-cxx-abi/cxx-abi, abi.html last changed in commit 2837827a025f43d1fcfc37ec053d1314cfd1bba3 (2025-09-30); repo HEAD fae5e46c86147a457a057c6372fa95ec38209fe8 (2026-01-20).
- quote: "The order of the virtual function pointers in a virtual table is the order of declaration of the corresponding member functions in the class." (§2.5 Virtual Table Layout)
- teaches: recover class hierarchies from `.rodata`/`.data.rel.ro` by decoding vtable entries (offset-to-top, typeinfo ptr, address point, function ptrs) and demangle `_Z…` symbols against the grammar rather than a tool's output.
- obscurity/value: the maintainer-hosted spec itself (not a blog) is the only oracle that fixes secondary-vtable/thunk/ctor-vtable layout; most RE write-ups paraphrase it.
- rea-route: none today (no REA doc covers C++ vtables/RTTI); candidate oracle for `native-investigation` / `native-function-matching` naming checks.
- limits: "not an authoritative definition of the C++ ABI for any particular platform" (§1) — platform psABIs may amend; mangling is grammar only, no per-compiler divergences (e.g. Apple/Arm deviations are in separate docs below).

### Itanium C++ ABI: Exception Handling (Level I/II)
- title: https://itanium-cxx-abi.github.io/cxx-abi/abi-eh.html
- kind: spec
- tier: A
- scope: `_Unwind_*` API, two-phase search/cleanup, `_Unwind_Exception` header, personality-routine contract (Level I); C++ catch/throw data structures (Level II). Level III is declared incomplete. Applies to Itanium-ABI platforms.
- anchor: "Level I. Base ABI" §1.1 Exception Handler Framework, §1.2 Data Structures (reason codes `_URC_*`), Revision $Revision: 1.22 $; abi-eh.html last changed in commit 336b01ebc025a15bbf5796b5b9c037412b5210fe (2026-01-20); repo HEAD fae5e46c86147a457a057c6372fa95ec38209fe8.
- quote: "The personality routine is called by the unwinder to handle language-specific tasks such as identifying the frame handling a particular exception." (Introduction → Level I)
- teaches: interpret LSDA/personality references in `.eh_frame`/`.gcc_except_table` and tell a catch-site from a cleanup-only frame, i.e. check an analyst's "this function has a try/catch" claim against the phase-1/phase-2 model.
- obscurity/value: LSDA byte format itself lives in implementation sources, but this is the only normative statement of the reason-code and handler-found semantics other tools cite.
- rea-route: none (no REA doc for ELF unwind/EH); complements `elf-notes` as another independent ELF-adjacent oracle.
- limits: does not define `.eh_frame` CIE/FDE bytes (see psABI entry) nor the LSDA encoding; §Level II/III explicitly "not completed".

### System V x86-64 psABI (source repo, ELF header / sections / .eh_frame)
- title: https://gitlab.com/x86-psABIs/x86-64-ABI/-/raw/master/x86-64-ABI/object-files.tex
- kind: spec
- tier: A
- scope: x86-64 ELF specifics: `e_machine`=62, `SHF_X86_64_LARGE`, `SHT_X86_64_UNWIND` (0x70000001), special/large-model sections, and the `.eh_frame` CIE/FDE field layout and augmentation characters z/P/R/L. NOT the calling convention (that is low-level-sys-info.tex, unopened).
- anchor: chapter "Object Files", subsection "EH_FRAME sections", tables "Common Information Entry (CIE)", "CIE Augmentation Section Content", "Frame Descriptor Entry (FDE)"; repo x86-psABIs/x86-64-ABI HEAD e1ce098331da5dbd66e1ffc74162380bcc213236 (2025-03-12); object-files.tex last changed e178c71028bb13da1464273ec51efcf6ddd661f5 (2024-11-16).
- quote: "If the code for a function is not one contiguous block, there will be a separate FDE for each contiguous sub-piece." (EH_FRAME sections)
- teaches: parse `.eh_frame` byte-for-byte (4-byte length, CIE id 0, augmentation "zR"/"zPLR", pointer encodings) and cross-check that cold/split function parts each carry their own FDE — a function-boundary oracle independent of symbols or disassembly.
- obscurity/value: raw LaTeX source of the maintained psABI is the canonical text, fresher than copies of the 2012-era PDFs that circulate; shows tables that PDFs obscure.
- rea-route: ground truth for the ELF side of `elf-notes` (REA doc reads `PT_NOTE`/`SHT_NOTE` tables; psABI fixes the x86-64 section/type constants around them); no `.eh_frame` REA tool.
- limits: it is TeX source (not rendered); x86-64 only; `.eh_frame_hdr` is delegated to LSB ch.7 ("enhanced LSB Chapter 7"), not reproduced here.

### ECMA-335 6th edition (CLI) — metadata physical layout
- title: https://ecma-international.org/wp-content/uploads/ECMA-335_6th_edition_june_2012.pdf
- kind: spec
- tier: A
- scope: CLI metadata physical format (Partition II §II.24: root `BSJB`, stream headers, `#~` table stream, heaps, coded indexes) and logical tables (§II.22), CIL opcodes (Partition III), for ECMA-335 6th ed. only. Microsoft/.NET 5+ metadata extensions (portable PDB, newer table/coded-index behaviours) are not here.
- anchor: Partition II §II.24.2.1 "Metadata root" (table row Offset 0 / Size 4 / Signature), §II.24.2.6 "#~ stream", §II.22 Metadata logical format; 6th edition, June 2012 (landing page https://ecma-international.org/publications-and-standards/standards/ecma-335/ read, modified 2022-01-26).
- quote: "Magic signature for physical metadata : 0x424A5342." (§II.24.2.1 Metadata root table)
- teaches: locate and validate the CLI metadata root by magic, enumerate streams (`#Strings`, `#US`, `#Blob`, `#GUID`, `#~`), and decode coded indexes by table-bit rules — a hand-verification path independent of dnlib/ILSpy.
- obscurity/value: a 22k-line PDF people never read end-to-end; Partition II §II.24 is the only ground truth for byte offsets, and the spec itself states streams "need not be there if they are empty".
- rea-route: `managed-code-analysis.md` (it cites ECMA-335 for omitted empty `#Blob` streams); oracle for `inspect_managed_artifact` / `inspect_managed_members` metadata claims.
- limits: 2012 text; does not cover Portable PDB (separate spec), R2R/NativeAOT, or .NET runtime-specific deviations (e.g. dotnet/runtime docs/design/specs/Ecma-335-Augments.md, unopened — see LEADS).

### LLVM docs: The PDB File Format (overview and stream table)
- title: https://llvm.org/docs/PDB/index.html
- kind: docs
- tier: B
- scope: byte-level map of MSVC PDB (MSF 7.00) streams: fixed stream indices 0–4 (Old Dir, PDB, TPI, DBI, IPI), named streams, per-module streams, hash streams, and the MSF/PDB/CodeView layering. Reverse-engineered documentation, not vendor-normative.
- anchor: "File Layout → The MSF Container", "Streams" table; llvm-project docs path llvm/docs/PDB/ ; MsfFile.md last changed d0b078ef5b6b7792a4d63cb4082423acd1c01732 (2026-08-25); llvm-project HEAD 56dfa63dd1fde6f9ca39a2b2d62801d49fd63693 (2026-10-29).
- quote: "A PDB file is an MSF (Multi-Stream Format) file." (File Layout → The MSF Container)
- teaches: walk a PDB from superblock → stream directory → DBI → module streams, and verify EXE↔PDB identity via the PDB Info stream rather than trusting a debugger's "matched" message.
- obscurity/value: the only complete public byte-level PDB spec outside Microsoft's own sources; used by lld-link/llvm-pdbutil and therefore regression-tested against real PDBs.
- rea-route: none (REA has no PDB parser; `ghidra-provider.md` only reports Ghidra's "PDB Loaded" attribute and explicitly disclaims PDB identity) — LLVM PDB would be the independent oracle for that missing identity attestation.
- limits: LLVM supports only 4096-byte blocks ("BigMsf") in text; "Unknown" fields remain; some stream contents flagged unknown (/LinkInfo).

### LLVM docs: The MSF File Format
- title: https://llvm.org/docs/PDB/MsfFile.html
- kind: docs
- tier: B
- scope: MSF superblock, free-block map, stream directory and block-indirection layout, for the BigMsf/7.00 variant; byte arithmetic (`NumBlocks*BlockSize == file size`, `ceil(NumDirectoryBytes/BlockSize)` map entries).
- anchor: "The Superblock", "The Stream Directory" (worked 60-byte directory example); llvm/docs/PDB/MsfFile.md @ d0b078ef5b6b7792a4d63cb4082423acd1c01732 (2026-08-25).
- quote: Must be equal to "Microsoft C/C++ MSF 7.00\\r\\n" followed by the bytes 1A 44 53 00 00 00. (The Superblock → FileMagic)
- teaches: write a ~40-line validator that checks magic, `BlockSize ∈ {512,1024,2048,4096}`, `FreeBlockMapBlock ∈ {1,2}`, and reassembles non-contiguous streams — detecting truncated/tampered PDBs by arithmetic.
- obscurity/value: includes a worked example of jagged `StreamBlocks[][]`, the trap that "streams are discontiguous and you cannot assume anything about the layout of the blocks".
- rea-route: none (no REA PDB route); pairs with `pe-*` docs where a PDB path/GUID is carried in the debug directory.
- limits: LLVM only handles 4 KiB; the older MSF 2.00 ("JG") variant is not described.

### Microsoft pdb-rs docs: PDB and CodeView (vendor-side companion)
- title: https://github.com/microsoft/pdb-rs/blob/main/docs/index.md
- kind: docs
- tier: B
- scope: Microsoft-maintained description of PDB structure, CodeView type/symbol records, and normalization rules for deterministic PDBs. Explicitly self-labelled non-authoritative.
- anchor: docs/index.md (Contents: pdb/pdb.md, codeview/codeview.md, determinism.md, references.md); path-scoped commit cf59a66b6b2437ac9feb7f0ca650ed0c6bc9a24e (2025-12-12); repo HEAD 2081a0dd6f1150cf965dec10855e75cfecfde176 (2026-08-24).
- quote: It describes the structure of the PDBs with sufficient detail to read, create, and modify PDBs for some purposes.
- teaches: cross-check the LLVM description from a second, vendor-affiliated source and learn which PDB bytes are non-deterministic (GUID/age/timestamps) when comparing builds.
- obscurity/value: the `determinism.md` normalization rules are rarely cited and directly useful for diffing two PDBs from "reproducible" builds.
- rea-route: none.
- limits: only the index page was read (sub-pages not opened); it self-describes as "non-authoritative" — the verdict is B, and two-source agreement (LLVM + pdb-rs) is needed before recording a PDB byte fact.

### Apple XNU Mach-O `loader.h`
- title: https://raw.githubusercontent.com/apple-oss-distributions/xnu/main/EXTERNAL_HEADERS/mach-o/loader.h
- kind: code
- tier: A
- scope: Mach-O header/load-command structs and constants (`MH_MAGIC[_64]`, `MH_CIGAM[_64]`, filetypes `MH_OBJECT…MH_FILESET`, `struct mach_header[_64]`) as shipped in Apple's XNU open-source drop; header version as of the pinned commit (copyright 1999-2019).
- anchor: lines 1–120 (struct mach_header, struct mach_header_64, filetype `#define`s); apple-oss-distributions/xnu path-scoped commit e6231be02a03711ca404e5121a151b24afbff733 (2022-02-07); repo HEAD f6217f891ac0bb64f3d375211650a4c1ff8ca1ea (2025-10-16). Only the first ~120 of ~1580 lines were read; load-command (LC_*) constants were NOT read.
- quote: "The 64-bit mach header appears at the very beginning of object files for 64-bit architectures." (comment above `struct mach_header_64`)
- teaches: check magic (`0xfeedfacf` / byte-swapped `0xcffaedfe`), `ncmds`/`sizeofcmds` consistency and file type against raw bytes before trusting `otool`/LIEF output.
- obscurity/value: the header file *is* the spec — Apple publishes no prose Mach-O spec; newer LC_* commands (dyld chained fixups, LC_FILESET_ENTRY) appear only here.
- rea-route: `apple-application-analysis.md` (REA parses Mach-O and FAT headers in TypeScript for `trace_dylib_resolution`) — this header is the independent oracle for those constants.
- limits: dyld-compressed-info/chained-fixup opcode semantics are in dyld sources, not this header; the file last changed in 2022, so newer extensions may appear in other headers (e.g. `mach-o/fixup-chains.h`, unopened).

### Apple XNU Mach-O `fat.h` (universal binary header)
- title: https://raw.githubusercontent.com/apple-oss-distributions/xnu/main/EXTERNAL_HEADERS/mach-o/fat.h
- kind: code
- tier: A
- scope: universal ("fat") container: `FAT_MAGIC` 0xcafebabe, `struct fat_header`, `struct fat_arch` (32-bit offsets/sizes), always big-endian on disk. 64-bit fat_arch variant is not in the portion read.
- anchor: lines 30–110; path-scoped commit 3ca3bd5593ac4736fb236ffd68a7ccb91ee6c0f0 (2021-10-06); xnu HEAD f6217f891ac0bb64f3d375211650a4c1ff8ca1ea.
- quote: "All structures defined here are always written and read to/from disk in big-endian order."
- teaches: slice a universal binary by hand (`nfat_arch` records of cputype/cpusubtype/offset/size/align) and avoid the 0xCAFEBABE collision with Java class files (both big-endian magics) by validating `nfat_arch` against file size.
- obscurity/value: byte-order asymmetry (fat headers big-endian, embedded Mach-O little-endian on x86/arm64) is a classic parser trap documented only in this comment.
- rea-route: `apple-application-analysis.md` (FAT header parsing for dylib resolution).
- limits: the shown file lacks `fat_arch_64`/`FAT_MAGIC_64` (not seen in the lines read); no coverage of Java-class collision — that is analyst inference, not stated in the header.

### Arm AAPCS64 (Procedure Call Standard for AArch64), release 2025Q4
- title: https://raw.githubusercontent.com/ARM-software/abi-aa/main/aapcs64/aapcs64.rst
- kind: spec
- tier: A
- scope: AArch64 argument passing, register roles (x0–x7, x18 platform register, x29 FP, x30 LR), data layout, return values — generic Arm-ABI baseline; platform deviations (Apple, Windows) override it.
- anchor: Preamble → Abstract; release "2025Q4", date of issue 23 January 2026; abi-aa path-scoped commit ed4c4331cc3a2dde9ac41b0e538209bb609d2743 (2026-10-27) (same as repo HEAD). Only lines 1–80 (preamble) were read.
- quote: "This document describes the Procedure Call Standard used by the Application Binary Interface (ABI) for the Arm 64-bit architecture."
- teaches: derive a function's arity/types from register use in recovered arm64 code and know which registers are caller- vs callee-saved when validating decompiler prototypes.
- obscurity/value: source (reST) is public, CC-BY-SA, and updated quarterly — one can pin the exact quarterly release against a binary's era.
- rea-route: `ghidra-provider.md`/`native-investigation.md` arm64 reasoning (no REA doc owns arm64 calling conventions); useful oracle for decompiler-prototype claims.
- limits: only the preamble was read here (rules themselves unopened); Arm ARM (ISA semantics) was not opened; Apple/Windows deviations apply on those platforms.

### Apple: Writing ARM64 code for Apple platforms
- title: https://developer.apple.com/documentation/xcode/writing-arm64-code-for-apple-platforms
- kind: docs
- tier: A
- scope: Apple-platform (iOS/macOS/tvOS/watchOS/visionOS) deviations from AAPCS64 and from the generic Arm64 C++ ABI: reserved x18, mandatory frame pointer, 16-byte-aligned arg registers, caller-extends narrow args, `va_list`=`char*`, C1/C2/D1/D2 return `this`, 2-word array cookies, 64-bit guard variables. Undated page (retrieved 2026-10-29).
- anchor: sections "Respect the purpose of specific CPU registers", "Pass arguments to functions correctly", "Handle C++ differences".
- quote: "The ABI requires the complete object (C1) and base-object (C2) constructors to return this to their callers."
- teaches: avoid mis-decompiling Apple arm64 code with generic AAPCS64 assumptions (e.g. caller sign-extension, `Pc` vs `St9__va_list` mangling) and recognise Apple-style ctor/dtor returns.
- obscurity/value: the single most frequently-forgotten document for macOS/iOS arm64 RE, and the one that disproves "Apple arm64 == Itanium ABI on Arm".
- rea-route: `apple-application-analysis.md`, `apple-ips.md` (Apple targets); oracle for prototype/mangling claims on Mach-O arm64.
- limits: no revision/date on the page; mentions `x18` reserved but not PAC/arm64e (pointer-authentication) ABI — that is a separate Apple doc (see LEADS).

### Intel 64 and IA-32 SDM — landing page (version and canonical PDFs only)
- title: https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html
- kind: spec
- tier: B
- scope: only "which SDM revision is current and where the canonical PDF volumes live" (Combined, 4-volume, 10-volume sets; Volume 2D W–Z; Volume 3A etc.). Instruction semantics are NOT established — the PDFs were not opened.
- anchor: "Overview" header (ID 767375, Updated 10/9/2026) and "Ten-Volume Set" table (Vol 2A getContent/671199 … Vol 4 getContent/671098); no git sha (vendor page).
- quote: "The downloadable PDFs of all IA-32 Architectures Software Developer's Manual volumes are at version 093."
- teaches: pin the exact SDM version (093) and volume URL in an evidence ledger instead of a bare "per Intel SDM" citation.
- obscurity/value: also lists APX/AVX10.2/FRED specifications and the "Documentation Changes" volume that carries erratum-level instruction fixes.
- rea-route: none; would be an oracle for instruction-encoding facts if a specific volume/page were cited.
- limits: landing page only → tier B for versioning; page content is vendor marketing-adjacent and unarchived; quote concerns document version, not encoding truth.

### Microsoft: x64 exception handling (RUNTIME_FUNCTION / UNWIND_INFO / UNWIND_CODE)
- title: https://learn.microsoft.com/en-us/cpp/build/exception-handling-x64?view=msvc-170
- kind: docs
- tier: A
- scope: Windows x64 (PE32+) `.pdata` RUNTIME_FUNCTION (12 bytes: start/end/unwind RVAs), `UNWIND_INFO` header bitfields, `UNWIND_CODE` ops (UWOP_PUSH_NONVOL…UWOP_PUSH_MACHFRAME), chained info, and the unwind procedure. Excludes arm64 Windows and the Unwind V3 preview (linked, unopened).
- anchor: "struct RUNTIME_FUNCTION", "struct UNWIND_INFO", "struct UNWIND_CODE" ; source MicrosoftDocs/cpp-docs-pr git_commit_id e61067551f92a1c7beaad20c04b9f5ccfd2b5dd6, page updated_at 2026-05-21.
- quote: "These entries are sorted, and put in the `.pdata` section of a PE32+ image."
- teaches: walk `.pdata` and decode the unwind-code array (descending prolog offsets, 2-slot/3-slot codes, even-count padding, chained-info trailer) to recover function boundaries and stack frames from stripped Windows x64 binaries.
- obscurity/value: the exact-byte field table and the "array always contains an even number of entries" padding rule — the trap that breaks most hand-written unwinders.
- rea-route: `pe-load-config.md` / `pe-imports.md` family (PE data directories); `.pdata` (exception directory) has no REA tool — this is the independent oracle for one.
- limits: x64 only; language-specific handler data "is unspecified" (MSVC `FuncInfo`/`_C_specific_handler` formats are not here); 2019 `ms.date` but content updated 2026-05-21.

### Go `internal/abi/symtab.go` — pclntab magic values (version oracle)
- title: https://raw.githubusercontent.com/golang/go/master/src/internal/abi/symtab.go
- kind: code
- tier: A
- scope: `.pclntab`/`runtime.pcHeader` magic numbers and per-version semantics for Go 1.2–1.15 (0xfffffffb), 1.16–1.17 (0xfffffffa), 1.18–1.19 (0xfffffff0), 1.20+ (0xfffffff1); also FuncFlag, FuncID, PCDATA/FUNCDATA ids. Applies to the cited commit only; the format is explicitly internal and may change.
- anchor: `type PCLnTabMagic` and its `const` block; golang/go path-scoped commit 43cfd785e72ccd04fe638395aa80029aae23fef6 (2025-11-27); repo HEAD 430d19f07a57ee5ed4e3b1a04b0ab54dd5a24487 (2026-10-29). The consumer `src/debug/gosym/pclntab.go` (path-scoped commit e8c6e7775a0ed5b7d9261eac7e20fad3b6d90014, 2026-09-24) was also opened (lines 1–260: header check "4-byte magic, two zeros, pc quantum, pointer size").
- quote: "The magic numbers are chosen such that reading the value with a different endianness does not result in the same value."
- teaches: identify Go toolchain era and byte order of a stripped binary by reading the first 4 bytes of `.gopclntab`, then validate header (bytes 4–5 == 0, quantum ∈ {1,2,4}, ptrsize ∈ {4,8}) exactly as `debug/gosym` does.
- obscurity/value: the magic-per-version table in code comments is the only authoritative changelog of pclntab format breaks, and is invisible in public Go docs.
- rea-route: `go-binaries.md` (REA reports compiler version/modules from build metadata) — pclntab magic is an independent cross-check for the toolchain-version claim; `inspect_go_binary` reads build info, not pclntab (per the doc's first 40 lines).
- limits: says nothing about funcdata layouts beyond header (`runtime/symtab.go` not opened); "internal package" — no stability guarantee.

### Rust RFC 2603 — v0 symbol mangling
- title: https://rust-lang.github.io/rfcs/2603-rust-symbol-name-mangling-v0.html
- kind: spec
- tier: A
- scope: grammar and examples of the `_R…` v0 mangling (path tags N/C/I/E, namespace tags v/t, base-62 disambiguators `s…_`, basic-type letters) as accepted in RFC 2603. Whether a given rustc defaults to v0 vs legacy (`_ZN…17h<hash>E`) is not decided here.
- anchor: "Guide-level explanation → The Mangling Scheme by Example → Free-standing Functions and Statics", then "Reference-level explanation" (not read past line 300); rust-lang/rfcs path-scoped commit f17e8623ee2e2854570dcdb936a9f4ab08c0fcd4 (2025-11-29); repo HEAD 1dc48d761daaa2a0c80135d91f30d20ebdfb97b2 (2026-10-26).
- quote: "The final symbol name for the function would also include the prefix `_R` that is common to all symbol names generated by this scheme:"
- teaches: hand-demangle a Rust symbol (`_RNvNtCs1234_7mycrate3foo3bar` → `mycrate::foo::bar`) and decide legacy-vs-v0 from the prefix, recovering crate disambiguators and generic arguments that legacy mangling erased into a hash.
- obscurity/value: v0 retains monomorphization arguments in the symbol — a free generics oracle in stripped-but-symbol-bearing Rust binaries.
- rea-route: `rust-binaries.md` (cargo-auditable dependency metadata) — v0 symbols give an independent crate-name/version-disambiguator cross-check for the same crates.
- limits: RFC text, not the living reference (the Rust Reference / rustc-demangle test vectors are the implementation truth); only ~300 of 1152 lines were read; RFC states the scheme is "an implementation detail of the Rust compiler".

### PEP 552 — Deterministic pycs
- title: https://peps.python.org/pep-0552/
- kind: spec
- tier: A
- scope: CPython ≥3.7 `.pyc` header: 16 bytes = magic(4) + bit field(4) + (mtime(4) + size(4)) or 64-bit SipHash; `check_source` flag semantics; `PycInvalidationMode`. Magic-number→version mapping and marshal format are NOT here.
- anchor: §Specification (header words, bit field, hash-based pyc); PEP 552, Status Final, created 04-Sep-2017, Python-Version 3.7; python/peps path-scoped commit b39aefe6614b4e8a925d07c4b3ed47e147236dbe (2025-02-01); repo HEAD fc008c935df169de9b7669d8c22face10af4be4c (2026-10-28).
- quote: "If the lowest bit of the bit field is set, the pyc is a hash-based pyc."
- teaches: classify a `.pyc` as timestamp- vs hash-based and checked vs unchecked from bytes 4–7, and decide whether bytes 8–15 are `(mtime,size)` or a source hash.
- obscurity/value: distinguishes pyc files that are reproducible-build artefacts (hash-based, `check_source` unset) from stale-able caches — a provenance signal for packaged Python apps.
- rea-route: `python-pyc.md` (its `flags`, `hash_based`, `check_source` fields cite PEP 552) — this is the independent oracle for those fields.
- limits: header only; the 2-byte magic table lives in CPython `Lib/importlib/_bootstrap_external.py` / `importlib.util.MAGIC_NUMBER` (unopened — see LEADS); marshal opcodes not covered; the REA doc notes 3.11 alpha magics <3494 use other layouts.

---

## REJECTED
- REJECTED: x86-64 psABI "latest PDF" at gitlab artifact URL — read returned HTTP 404 ("Failed to fetch URL (HTTP 404)") for https://gitlab.com/x86-psABIs/x86-64-ABI/-/jobs/9388606854/artifacts/raw/x86-64-ABI/x86-64-ABI.pdf; flip: a working PDF release/tag URL (e.g. a tagged release artefact) opened with a quotable passage. The TeX source (included above) replaces it.
- REJECTED (as *standalone* oracle for instruction encodings): Intel SDM landing page — quote read is a version statement only: "The downloadable PDFs of all IA-32 Architectures Software Developer's Manual volumes are at version 093."; flip: opening a specific volume PDF (e.g. Vol 2D getContent/671143) with an anchored opcode-table page. It is included above only at tier B for version pinning.

## LEADS (unopened or unreachable)
- x86-64 psABI `low-level-sys-info.tex` (calling convention) — not opened (same repo, https://gitlab.com/x86-psABIs/x86-64-ABI/-/raw/master/x86-64-ABI/low-level-sys-info.tex); also the rendered PDF URL (404 above).
- Intel SDM Volume 2D/2A PDFs via https://cdrdv2.intel.com/v1/dl/getContent/671143 and /671199 — not opened (very large; need a page anchor).
- Arm Architecture Reference Manual (developer.arm.com, DDI 0487) — not opened; JS-heavy landing; ABI-aa `aapcs64.rst` rules sections (beyond line 80) also unread.
- Apple arm64e / pointer-authentication ABI doc and `mach-o/fixup-chains.h` / `mach-o/nlist.h` — not opened.
- dotnet/runtime `docs/design/specs/Ecma-335-Augments.md` and Portable PDB spec (https://github.com/dotnet/runtime/blob/main/docs/design/specs/PortablePdb-Metadata.md) — not opened.
- Rust RFC 2603 Reference-level explanation (lines 300–1152) and rustc-demangle test vectors — not read.
- CPython `Lib/importlib/_bootstrap_external.py` MAGIC_NUMBER table and `Python/marshal.c` — not opened (pyc magic→version oracle).
- Go `src/runtime/symtab.go` (pcHeader/funcInfo layouts) and `src/cmd/link/internal/ld/pcln.go` — not opened.
- Microsoft pdb-rs `docs/pdb/pdb.md`, `docs/codeview/codeview.md`, `docs/determinism.md`; LLVM PDB sub-pages `TpiStream.html`, `DbiStream.html`, `PdbStream.html`, `CodeViewTypes.html` — not opened.
- RISC-V ELF psABI (`riscv-non-isa/riscv-elf-psabi-doc`, riscv-elf.adoc @ 9b2767e2a8851709608c4e1452998ad232d6278b) — opened lines 1–60 only (code-model preamble); not quoted-for-tier because lines read cover code models only; promote after reading relocations section.
- Microsoft "x64 ABI conventions" (https://learn.microsoft.com/en-us/cpp/build/x64-software-conventions) — opened; quote available ("The x64 executable image format is PE32+."), omitted to keep slice at ~14 sources; register-volatility table (RAX/RCX/RDX/R8/R9 args) would make a good tier-A add.

## search-log
- Where/how: candidate list from assignment, then de-scoped by SHOKUNIN_BINARY_FORENSICS IRC (DROP gABI/DWARF/PE/WASM; PRIORITISE Itanium, x86-64 psABI, ECMA-335, PDB, Mach-O, Intel/Arm). Verified revisions with `gh api repos/<o>/<r>/commits?path=…` (authenticated; unauthenticated GitHub hit an abuse limiter once) and GitLab REST for the psABI repo.
- identified 24 candidates; opened 27 pages (incl. 3 de-scoped pages opened before the notice: refspecs gABI ch4.sheader.html, learn.microsoft.com PE format, webassembly.github.io core binary/modules.html; RISC-V psABI and MS x64 conventions opened but kept as leads); included 16 source blocks; excluded/rejected 2 (psABI PDF 404; Intel SDM as instruction oracle, kept only at tier B for version pinning); leads 10 bullets.
- No tool installed or executed; no sample downloaded; only page text read. No repo file other than this report was edited.
