# ReFormatSpecs — binary format specs & format-DSL tooling (byte-oracle material)

Slice owner: REVENGER_SHOKUNIN.ReFormatSpecs · accessed 2026-10-29 · all pages fetched this session (curl -sL / git ls-remote for pins). No tools installed or run beyond curl, git ls-remote, pdftotext (text extraction of the fetched DWARF PDF).
Skipped as already in corpus (/tmp/revenger-existing-urls.txt): learn.microsoft.com PE format, source.android.com dex-format, github.com/WerWolv/ImHex, PKWARE APPNOTE, Wikipedia PE.
Pin convention: `@<12-hex>` = `git ls-remote <repo> HEAD` (or named branch) result on 2026-10-29; the page was fetched from the default branch at that time.

---

## A. Object/executable container specs

ID-SLUG: elf-gabi-ehdr
source: System V ABI (gABI) DRAFT 10 June 2013, ch.4 "ELF Header" — https://www.sco.com/developers/gabi/latest/ch4.eheader.html
kind: spec
tier: A
scope: The gABI's own definition of the ELF header and e_ident bytes (EI_CLASS/EI_DATA/EI_PAD) in the 10 June 2013 draft.
anchor: §"ELF Identification", EI_PAD entry; contents page titled "System V Application Binary Interface - DRAFT - 10 June 2013"; accessed 2026-10-29; "These bytes are reserved and set to zero; programs that read object files should ignore them."
teaches: Spec-mandated "ignore" bytes (EI_PAD) are a place where a conforming reader and a byte-oracle check can legitimately disagree with what the file contains, so record padding contents as observation, not as format violation.
status: mined
limitation: A DRAFT gABI page says nothing about processor supplements, GNU extensions, or how any particular loader treats non-zero padding.
province-fit: in — ELF is the primary native-binary container.
obscurity: mainstream

ID-SLUG: x86-64-psabi-gnu-property
source: x86-64 psABI LaTeX source, dl.tex §"Program Property" — https://gitlab.com/x86-psABIs/x86-64-ABI/-/raw/master/x86-64-ABI/dl.tex (master head e1ce098331da, 2025-03-12, per GitLab API)
kind: spec
tier: A
scope: The psABI's own definition of x86 GNU program-property types (GNU_PROPERTY_X86_FEATURE_1_AND, ISA_1_NEEDED, …), their range values and AND/OR merge semantics.
anchor: \section{Program Property}, description of GNU_PROPERTY_X86_UINT32_AND_LO..HI, dl.tex lines ~466–471 @e1ce098331da; accessed 2026-10-29; "If the bit is 0 or the property is missing, it is unknown whether all input relocatables have the feature."
teaches: The ABI itself defines a missing/zero CET or ISA property as *unknown*, not *absent* — a ready-made three-state (observation/inference/unknown) rule for `readelf -n` property-note evidence.
status: mined
limitation: Covers x86 property semantics only; it does not say what a given kernel/loader actually enforces.
province-fit: in — ELF note evidence on native binaries.
obscurity: niche

ID-SLUG: dwarf5-std
source: DWARF Debugging Information Format Version 5 (February 13, 2017) — https://dwarfstd.org/doc/DWARF5.pdf (landing page https://dwarfstd.org/dwarf5std.html)
kind: spec
tier: A
scope: The DWARF Committee's normative description of DWARF 5 debug sections and its stated design philosophy.
anchor: §1.3.12 "Permissive Rather Than Prescriptive", printed page 7 (PDF p.25), dated February 13, 2017; accessed 2026-10-29; "DWARF is permissive, allowing different producers to generate different descriptions for the same source to object conversion"
teaches: Two compilers can emit different-but-valid DWARF for identical source, so DWARF differences are evidence about the producer, not proof of a source difference.
status: mined
limitation: Does not cover errata issued after publication (separate Errata page) nor DWARF 6 drafts.
province-fit: in — debug-info parsing of native binaries.
obscurity: mainstream

ID-SLUG: xnu-macho-loader-h
source: xnu EXTERNAL_HEADERS/mach-o/loader.h — https://raw.githubusercontent.com/apple-oss-distributions/xnu/main/EXTERNAL_HEADERS/mach-o/loader.h (@f6217f891ac0)
kind: code
tier: A
scope: Apple's open-source header defining mach_header(_64), MH_MAGIC/MH_CIGAM constants, load commands, and segment/section structs as shipped in xnu at that commit.
anchor: comment after `#define MH_CIGAM_64 0xcffaedfe` @f6217f891ac0; accessed 2026-10-29; "The layout of the file depends on the filetype."
teaches: MH_CIGAM* exists precisely so readers detect byte-swapped headers; a Mach-O parser must branch on magic and filetype before trusting any later offset.
status: mined
limitation: The xnu copy may lag the dyld/cctools copy and omits newer load-command payload layouts documented elsewhere (e.g. chained fixups).
province-fit: in — native Apple binaries.
obscurity: mainstream

ID-SLUG: dyld-fixup-chains-h
source: dyld include/mach-o/fixup-chains.h — https://raw.githubusercontent.com/apple-oss-distributions/dyld/main/include/mach-o/fixup-chains.h (@fd8d0c4d5232)
kind: code
tier: A
scope: Apple's header defining the LC_DYLD_CHAINED_FIXUPS payload (dyld_chained_fixups_header, starts_in_segment, DYLD_CHAINED_PTR_* pointer formats).
anchor: `enum` "values for dyld_chained_starts_in_segment.pointer_format" @fd8d0c4d5232; accessed 2026-10-29; "DYLD_CHAINED_PTR_64 = 2, // target is vmaddr"
teaches: On modern Mach-O, pointer-sized words in __DATA are encoded fixup-chain entries, not addresses; reading them raw without the pointer_format produces false xrefs.
status: mined
limitation: Header only; it does not specify which OS/toolchain versions emit which pointer_format.
province-fit: in — static analysis of iOS/macOS binaries.
obscurity: obscure

ID-SLUG: msvc-x64-callconv
source: x64 calling convention (Microsoft Learn, C++ build docs, "Last updated on 2026-05-21") — https://learn.microsoft.com/en-us/cpp/build/x64-calling-convention
kind: docs
tier: A
scope: Microsoft's own description of the Windows x64 calling convention (register args, shadow store, varargs).
anchor: intro paragraph, "Last updated on 2026-05-21"; accessed 2026-10-29; "Space is allocated on the call stack as a shadow store for callees to save those registers."
teaches: The 32-byte shadow store is ABI-mandated, so stack slots at [rsp+8..+0x20] in a callee are not evidence of locals or extra arguments.
status: mined
limitation: Describes MSVC's documented ABI; it does not cover vectorcall details beyond its links nor non-MSVC compilers' deviations.
province-fit: in — PE/x64 disassembly interpretation.
obscurity: mainstream

## B. Debug-info formats (PDB/CodeView)

ID-SLUG: llvm-pdb-overview
source: The PDB File Format — LLVM docs — https://llvm.org/docs/PDB/index.html (llvm-project main @8d6e6472fd8f)
kind: docs
tier: A
scope: LLVM's reverse-documented description of PDB, and its stated provenance (Microsoft's published code).
anchor: §"Introduction"; accessed 2026-10-29; "This manual describes what we know about the PDB file format today."
teaches: A widely used format reference openly frames itself as current knowledge derived from reading another vendor's code — cite it as tier-A for LLVM's understanding, not as Microsoft's normative spec.
status: mined
limitation: Do not treat LLVM's PDB docs as complete or as authoritative over Microsoft's own tooling behaviour.
province-fit: in — Windows symbols/debug info.
obscurity: niche

ID-SLUG: llvm-pdb-msf
source: The MSF File Format — LLVM docs — https://llvm.org/docs/PDB/MsfFile.html (llvm-project main @8d6e6472fd8f)
kind: docs
tier: A
scope: LLVM's description of the MSF container (SuperBlock, FileMagic, BlockSize, Free Block Map intervals).
anchor: §"The Superblock", BlockSize field; accessed 2026-10-29; "Valid values are 512, 1024, 2048, and 4096 bytes."
teaches: The MSF superblock gives a checkable byte oracle (magic string + four legal block sizes) before any stream is trusted.
status: mined
limitation: Covers MSF only, not the newer MSFZ container.
province-fit: in — PDB container parsing.
obscurity: niche

ID-SLUG: llvm-pdb-tpi
source: The PDB TPI and IPI Streams — LLVM docs — https://llvm.org/docs/PDB/TpiStream.html (llvm-project main @8d6e6472fd8f)
kind: docs
tier: A
scope: LLVM's description of TpiStreamHeader fields and type-index ranges, including explicit statements of what has/hasn't been observed.
anchor: §"Stream Header", Version field (V80 = 20040203); accessed 2026-10-29; "It is assumed that should another value be observed, the layout described by this document may not be accurate."
teaches: A model evidence-ledger pattern inside a format doc — it states the observed value set, labels the layout as an assumption, and names the falsifying observation.
status: mined
limitation: "Always appears to be V80" is LLVM's observation sample, not a guarantee about all Microsoft toolchains.
province-fit: in — CodeView type records.
obscurity: niche

ID-SLUG: microsoft-pdb-archived
source: microsoft/microsoft-pdb README — https://github.com/microsoft/microsoft-pdb (@805655a28bd8; archived)
kind: code
tier: A
scope: Microsoft's own published PDB/CodeView headers (cvinfo.h, langapi) and the repo's maintenance status.
anchor: README "Update" banner, repo "archived by the owner on Apr 27, 2023" @805655a28bd8; accessed 2026-10-29; "Currently we are not planning any new updates nor are we taking PRs."
teaches: The primary Microsoft PDB source is frozen; record its archive date when citing it, because post-2023 PDB features will not appear there.
status: mined
limitation: README also states the code will not currently build; it is reference headers, not a working tool.
province-fit: in — Windows debug info.
obscurity: niche

ID-SLUG: ms-pdb-rs-msfz
source: microsoft/pdb-rs README — https://github.com/microsoft/pdb-rs (@2081a0dd6f11)
kind: code
tier: A
scope: Microsoft's Rust crates (ms-pdb, ms-pdb-msf, ms-pdb-msfz, pdbtool) and its README description of the MSFZ/PDZ container.
anchor: README §"PDB tools", ms-pdb-msfz paragraph @2081a0dd6f11; accessed 2026-10-29; "MSFZ is intended to be a format for storing PDBs, not for local development."
teaches: A second PDB container (MSFZ/PDZ, compressed, not in-place modifiable) exists; an MSF-only parser failing on a symbol-server PDB may be meeting MSFZ, not corruption.
status: mined
limitation: README-level claim; no statement here of which symbol servers serve MSFZ today.
province-fit: in — Windows symbol acquisition/parsing.
obscurity: obscure

## C. Language runtimes: symbol tables, mangling, ABIs

ID-SLUG: go-gosym-pclntab
source: Go debug/gosym/pclntab.go — https://go.dev/src/debug/gosym/pclntab.go (go master @430d19f07a57)
kind: code
tier: A
scope: The Go standard library's pclntab reader: version enum (ver11…ver120) and magic/endianness detection.
anchor: `parsePclnTab` comment above leMagic/beMagic, ~line 218 @430d19f07a57; accessed 2026-10-29; "The magic numbers are chosen such that reading the value with"
teaches: pclntab magic is designed to disambiguate both Go version and endianness, so the magic alone is a byte-oracle for "which pclntab layout applies".
status: mined
limitation: Reader code at master; layouts of future pclntab versions are not covered and stripped/obfuscated (garble) binaries may break assumptions.
province-fit: in — Go native binaries.
obscurity: niche

ID-SLUG: go-buildinfo
source: Go debug/buildinfo/buildinfo.go — https://go.dev/src/debug/buildinfo/buildinfo.go (go master @430d19f07a57)
kind: code
tier: A
scope: The Go standard library's locator/parser for the linker-embedded build-info blob (magic, header size, alignment).
anchor: comment + `var buildInfoMagic = []byte("\xff Go buildinf:")`, lines 55–58 @430d19f07a57; accessed 2026-10-29; "The build info blob left by the linker is identified by a 32-byte header,"
teaches: Go binaries carry a self-describing 16-byte-aligned build-info header (toolchain version, module list) that is a cheap, checkable provenance oracle.
status: mined
limitation: Absence or tampering of the blob proves nothing about non-Go origin; the content is producer-written and forgeable.
province-fit: in — Go binary identification/provenance.
obscurity: niche

ID-SLUG: go-abi-internal
source: Go internal ABI specification (go.dev/s/regabi) — https://go.googlesource.com/go/+/refs/heads/master/src/cmd/compile/abi-internal.md (@430d19f07a57)
kind: spec
tier: A
scope: Go's register-based ABIInternal definition and its explicit stability disclaimer.
anchor: opening paragraph @430d19f07a57; accessed 2026-10-29; "This ABI is unstable and will change between Go versions."
teaches: Calling-convention assumptions for Go functions must be tied to the observed Go toolchain version (e.g. from buildinfo), never assumed global.
status: mined
limitation: Describes the current master ABI; older binaries may follow ABI0 or earlier ABIInternal revisions.
province-fit: in — Go disassembly.
obscurity: niche

ID-SLUG: rustc-v0-mangling
source: v0 Symbol Format — The rustc book — https://doc.rust-lang.org/rustc/symbol-mangling/v0.html
kind: spec
tier: A
scope: The rustc book's normative grammar for Rust v0 symbol names (_R prefix, paths, generic args).
anchor: §"Symbol name" grammar (`symbol-name → _R …`); accessed 2026-10-29; "A mangled symbol starts with the two characters _R which is a prefix to identify the symbol as a Rust symbol."
teaches: `_R` vs legacy `_ZN…17h<hash>E` symbols is a byte-level oracle for Rust mangling scheme and a reversible source of generic-instantiation facts.
status: mined
limitation: Does not say which crates/toolchains default to v0; legacy mangling remains common.
province-fit: in — Rust native binaries.
obscurity: niche

ID-SLUG: rust-rfc-2603
source: RFC 2603 Rust Symbol Mangling (v0) — https://rust-lang.github.io/rfcs/2603-rust-symbol-name-mangling-v0.html (Start Date 2018-11-27; RFC PR rust-lang/rfcs#2603)
kind: spec
tier: A
scope: The RFC's stated design goals and rationale for v0 mangling.
anchor: §"Guide-level explanation"/goals ("The essential one is:"); accessed 2026-10-29; "The scheme must provide an unambiguous string encoding for everything that can end up in a binary’s symbol table."
teaches: Unambiguity is the design invariant, so two distinct v0 symbols demangling to the same text indicates a demangler bug or a forged symbol, a usable rejection control.
status: mined
limitation: RFC text is design intent; the rustc book page is the current normative grammar.
province-fit: in — Rust symbol evidence.
obscurity: niche

ID-SLUG: itanium-cxx-abi-mangling
source: Itanium C++ ABI — https://itanium-cxx-abi.github.io/cxx-abi/abi.html (repo itanium-cxx-abi/cxx-abi @fae5e46c8614)
kind: spec
tier: A
scope: The Itanium C++ ABI's own mangling grammar (§5.1) and runtime APIs (e.g. __cxa_demangle).
anchor: §5.1.2 "General Structure" @fae5e46c8614; accessed 2026-10-29; "Entities with C linkage and global namespace variables are not mangled."
teaches: Missing `_Z` mangling is expected for extern "C" and globals, so an unmangled symbol is not evidence the binary is plain C.
status: mined
limitation: Itanium mangling only; MSVC C++ decoration is a different, separately documented scheme.
province-fit: in — C++ native binaries on ELF/Mach-O.
obscurity: mainstream

ID-SLUG: swift-mangling-rst
source: swiftlang/swift docs/ABI/Mangling.rst — https://github.com/swiftlang/swift/blob/main/docs/ABI/Mangling.rst (@29c54d90afd0)
kind: spec
tier: A
scope: The Swift project's mangling grammar, including version prefixes ($s, _T0, $S, $e).
anchor: §"Mangling", prefix list (mangled-name ::= '$s' …) @29c54d90afd0; accessed 2026-10-29; "pre-stable versions may not exactly conform to this description."
teaches: The mangling prefix is a toolchain-era oracle ($S = Swift 4.2, $s = stable, $e = Embedded), and pre-stable symbols are explicitly out of spec.
status: mined
limitation: Document is a reference grammar; it states pre-stable output may deviate, so it cannot validate old binaries.
province-fit: in — Swift binaries on Apple/Linux.
obscurity: niche

## D. Managed / VM bytecode formats

ID-SLUG: jvms21-ch4-classfile
source: JVM Specification Java SE 21, Chapter 4 "The class File Format" — https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html
kind: spec
tier: A
scope: The normative ClassFile structure, constant pool, attributes, and verification rules for SE 21.
anchor: §4.1 "The ClassFile Structure", `magic` item, SE 21 edition; accessed 2026-10-29; "The magic item supplies the magic number identifying the class file format; it has the value 0xCAFEBABE"
teaches: major_version maps a class file to a JVMS edition, so the edition you cite must match the observed version bytes.
status: mined
limitation: SE 21 text only; newer class-file versions and Android DEX are out of its scope.
province-fit: in — JVM managed artifacts.
obscurity: mainstream

ID-SLUG: aosp-art-vdex-h
source: AOSP ART runtime/vdex_file.h — https://android.googlesource.com/platform/art/+/master/runtime/vdex_file.h (art master @6484611fd45e)
kind: code
tier: A
scope: ART's own VDEX layout comment, VdexFileHeader (magic "vdex", kVdexVersion "027\0"), and section list.
anchor: class-level "File format:" comment + `kVdexVersion[] = { '0','2','7','\0' }` @6484611fd45e; accessed 2026-10-29; "VDEX files contain extracted DEX files."
teaches: The same comment marks the DexSection as "Optionally:", so a VDEX lacking DEX bytes is legitimate and the version field must select the layout.
status: mined
limitation: Master-branch layout; device files must be checked against the AOSP tag matching their vdex_version.
province-fit: in — Android on-device artifacts.
obscurity: obscure

ID-SLUG: hermes-hbc-fileformat
source: facebook/hermes include/hermes/BCGen/HBC/BytecodeFileFormat.h + BytecodeVersion.h — https://github.com/facebook/hermes/blob/main/include/hermes/BCGen/HBC/BytecodeFileFormat.h (@72b0009fa709)
kind: code
tier: A
scope: Hermes's own HBC header struct (magic, version, SHA-1 source hash, fileLength…) and the BYTECODE_VERSION constant on main.
anchor: `const static uint64_t MAGIC = 0x1F1903C103BC1FC6;` comment; BytecodeVersion.h shows `BYTECODE_VERSION = 96` "Updated: Aug 16, 2023" @72b0009fa709; accessed 2026-10-29; "in ancient Greek encoded in UTF-16BE and truncated to 8 bytes."
teaches: An HBC file's 8-byte magic plus u32 version at offset 8 selects the exact Hermes source revision needed to decode it; DELTA_MAGIC (~MAGIC) marks a non-executable delta form.
status: mined
limitation: main branch only; other branches (e.g. static_h) and older releases carry different version numbers and layouts.
province-fit: in — React Native/Electron-adjacent JS bundles.
obscurity: niche

ID-SLUG: wasm-binary-modules
source: WebAssembly 3.0 (2026-10-28) Core spec, Binary Format › Modules — https://webassembly.github.io/spec/core/binary/modules.html
kind: spec
tier: A
scope: The normative module preamble (\0asm magic, version), section ids and custom-section rules in the 2026-10-28 build.
anchor: §"Modules" and §"Custom Section"; build "WebAssembly 3.0 (2026-10-28)"; accessed 2026-10-29; "The current version of the WebAssembly binary format is 1."
teaches: Custom sections (id 0) are "ignored by the WebAssembly semantics", so anything there (names, producers, source maps) is unverifiable metadata, not behaviour.
status: mined
limitation: A living spec build; "WebAssembly 3.0" feature sections may not be supported by the engine that produced or runs a given module.
province-fit: in — WASM artifacts.
obscurity: mainstream

ID-SLUG: wasm-name-section
source: WebAssembly 3.0 (2026-10-28) Appendix › Custom Sections › Name Section — https://webassembly.github.io/spec/core/appendix/custom.html
kind: spec
tier: A
scope: The spec's definition of the optional "name" custom section and its subsections.
anchor: §"Name Section"; build 2026-10-28; accessed 2026-10-29; "Names need not be unique."
teaches: Function names recovered from the name section are producer-chosen labels with no uniqueness guarantee — log them as claims, not identities.
status: mined
limitation: Appendix material; engines may ignore or reject malformed name sections differently.
province-fit: in — WASM symbol recovery.
obscurity: niche

ID-SLUG: pep552-deterministic-pyc
source: PEP 552 – Deterministic pycs (Final, Python 3.7) — https://peps.python.org/pep-0552/
kind: spec
tier: A
scope: The pyc header layout from 3.7 onward (magic word, flags bit field, timestamp/size or SipHash).
anchor: §"Specification"; Status Final, Created 04-Sep-2017; accessed 2026-10-29; "If the bit field is 0, the pyc is a traditional timestamp-based pyc."
teaches: The 16-byte pyc header can carry either a source mtime+size or a source hash, so a pyc's header is a byte-checkable link to a candidate source file.
status: mined
limitation: Header only; it says nothing about code-object/marshal layout, which is unspecified (see next row).
province-fit: in — Python bytecode artifacts (PyInstaller etc.).
obscurity: niche

ID-SLUG: python-marshal-undocumented
source: marshal — Internal Python object serialization (Python 3.15.2 docs) — https://docs.python.org/3/library/marshal.html
kind: docs
tier: A
scope: CPython's own statement of the stability/documentation status of the marshal format used inside pyc files.
anchor: module intro paragraph, "Python 3.15.2 documentation"; accessed 2026-10-29; "Details of the format are undocumented on purpose; it may change between Python versions (although it rarely does)."
teaches: pyc payload decoding is version-pinned to CPython source, so the magic number must select the decoder and any cross-version claim is inference.
status: mined
limitation: Docs page, not a format description; byte-level truth is CPython's marshal.c for that version.
province-fit: in — Python bytecode artifacts.
obscurity: mainstream

## E. Unwind / type metadata (obscure)

ID-SLUG: sframe-spec-v3
source: The SFrame Format (GNU binutils docs; "DRAFT", July 26, 2026, Version 3) — https://sourceware.org/binutils/docs/sframe-spec.html
kind: spec
tier: A
scope: binutils' description of the .sframe section (preamble magic 0xdee2, version, FDE/FRE encodings).
anchor: §2.1.1 "SFrame Magic Number and Endianness" (preamble table); accessed 2026-10-29; "The magic number for SFrame section: 0xdee2."
teaches: .sframe is a compact unwind table alongside/instead of .eh_frame; its magic doubles as an endianness check and gives function-start boundaries for stripped ELF.
status: mined
limitation: Page is self-labelled DRAFT for Version 3; V1/V2 sections in shipped binaries use earlier layouts.
province-fit: in — ELF function-boundary recovery.
obscurity: obscure

ID-SLUG: linux-btf
source: BPF Type Format (BTF) — The Linux Kernel documentation (7.3.0) — https://docs.kernel.org/bpf/btf.html
kind: docs
tier: A
scope: The kernel's description of BTF header, type and string encodings (include/uapi/linux/btf.h).
anchor: §2 "BTF Type and String Encoding", btf_header; kernel docs 7.3.0; accessed 2026-10-29; "which has different encoding for big and little endian systems"
teaches: BTF (magic 0xeB9F) is a compact type-info blob in eBPF objects and vmlinux that yields struct layouts without DWARF, and its magic self-reports endianness.
status: mined
limitation: Describes the kernel-docs revision; does not cover every BTF_KIND added later or out-of-tree producers.
province-fit: adjacent — kernel/eBPF artifacts, edge of the native-binary province.
obscurity: obscure

## F. Format-DSL & parsing tooling

ID-SLUG: kaitai-ug-valid
source: Kaitai Struct User Guide (Kaitai Project version 0.11) — https://doc.kaitai.io/user_guide.html
kind: docs
tier: A
scope: The KSY language as documented for 0.11, including `contents` magic checks and `valid` constraints.
anchor: §4.4 "Validating attribute values" ("Feature available since v0.9"); accessed 2026-10-29; "Kaitai Struct provides a mechanism for validating attribute values using the valid key."
teaches: A .ksy with `contents`/`valid` turns a format reading into an executable byte oracle that rejects out-of-domain files instead of silently parsing them.
status: mined
limitation: Validation semantics may vary by target-language runtime; a passing parse is not proof the spec matches the real producer.
province-fit: in — format-DSL byte oracles.
obscurity: mainstream

ID-SLUG: kaitai-format-gallery
source: Kaitai Struct Format Gallery — https://formats.kaitai.io/ (kaitai_struct_formats @f38fd7de89aa)
kind: dataset
tier: C
scope: A catalog of community .ksy specs (executables, firmware, archives, filesystems…) usable as starting oracles.
anchor: gallery intro; accessed 2026-10-29; "All formats in this gallery have formal specifications in Kaitai Struct language."
teaches: Gallery specs are reusable parser starting points but each one is a community reading of a format that must be checked against the primary spec before becoming an oracle.
status: mined
limitation: Tier C: individual .ksy files are unaudited community descriptions with varying completeness.
province-fit: in — format catalog for artifacts.
obscurity: mainstream

ID-SLUG: kaitai-issue-170-security
source: kaitai-io/kaitai_struct issue #170 "Document security expectations" (state Open at fetch) — https://github.com/kaitai-io/kaitai_struct/issues/170
kind: community
tier: C
scope: Maintainer/contributor discussion of the trust model for generated parsers and untrusted .ksy files.
anchor: opening post and maintainer reply; accessed 2026-10-29; "we are not recommending executing code generated from untrusted ksys and untrusted inputs"
teaches: Untrusted bytes and an untrusted grammar are two separate trust boundaries; a third-party .ksy is code and needs sandboxing like any tool input.
status: mined
limitation: Community thread, not a published security policy; positions may be outdated.
province-fit: in — safe handling of format specs in the evidence workflow.
obscurity: obscure

ID-SLUG: imhex-pattern-language-docs
source: ImHex Pattern Language docs — https://docs.werwolv.net/pattern-language
kind: docs
tier: A
scope: The ImHex project's own documentation of its C++/Rust-like pattern DSL (types, placement, attributes, std lib).
anchor: landing page "Pattern Language" intro; accessed 2026-10-29; "The Pattern Language is a C++ and Rust inspired DSL that was developed for the ImHex Hex Editor"
teaches: Pattern files bind declarations to file offsets (`@`), so a .hexpat is a reviewable, diffable statement of a byte-layout hypothesis.
status: mined
limitation: Docs site is unversioned; behaviour may differ from the ImHex release actually used.
province-fit: in — interactive byte-layout evidence.
obscurity: niche

ID-SLUG: construct-intro
source: Construct 2.10 documentation — Introduction — https://construct.readthedocs.io/en/latest/intro.html
kind: docs
tier: A
scope: Construct's own description of its declarative, symmetric (parse+build) Python data-structure model.
anchor: §"Introduction", Construct 2.10 docs ("Version 2.10 was released in January 2020"); accessed 2026-10-29; "Construct is a powerful declarative and symmetrical parser and builder for binary data."
teaches: A symmetric parse→build round trip that reproduces the input bytes exactly is a strong, cheap fixture check for a format hypothesis.
status: mined
limitation: Round-trip success shows internal consistency of the description, not that the producer's semantics were understood.
province-fit: in — Python format oracles.
obscurity: niche

ID-SLUG: 010-binary-templates
source: 010 Editor — Binary Templates (SweetScape) — https://www.sweetscape.com/010editor/templates.html (+ repository https://www.sweetscape.com/010editor/repository/templates/)
kind: docs
tier: A
scope: SweetScape's description of the 010 template execution model; the repository page lists community .bt files (EXE.bt, ELF.bt, MachO.bt, bpf_elf.bt…).
anchor: templates page, "Binary Templates" section; accessed 2026-10-29; "A Template is executed as a program, starting from the first line of the file."
teaches: 010 templates are imperative programs, not declarative layouts, so a template's output depends on its control flow and must be cited with the template version.
status: mined
limitation: Commercial tool; repository templates are community-authored with mixed quality (e.g. ELF.bt notes views that "do not handle writing").
province-fit: in — format-template evidence.
obscurity: obscure

ID-SLUG: lief-docs
source: LIEF Documentation (2.0.0, build 9ee6eaa9) — https://lief.re/doc/latest/index.html
kind: docs
tier: A
scope: LIEF's own statement of supported formats and APIs (ELF, PE, Mach-O, COFF, Android formats) at doc build 2.0.0/9ee6eaa9.
anchor: landing page header "2.0.0 9ee6eaa9"; accessed 2026-10-29; "LIEF is a cross-platform library for parsing, inspecting, modifying, and writing executable formats."
teaches: One parser library across ELF/PE/Mach-O lets you cross-check another tool's header reading on the same bytes, which acts as a second-opinion oracle.
status: mined
limitation: Documentation claim of support; it says nothing about parse fidelity on malformed inputs.
province-fit: in — multi-format static parsing.
obscurity: mainstream

ID-SLUG: pefile-readme
source: erocarrera/pefile README — https://github.com/erocarrera/pefile (@274e0b8ce0b8)
kind: tool
tier: A
scope: pefile's own feature list, including warnings for suspicious/malformed values and the limits of its write support.
anchor: README §"Features" @274e0b8ce0b8; accessed 2026-10-29; "This functionality won't rearrange PE file structures to make room for new fields, so use it with care."
teaches: pefile reports malformed values as warnings and keeps parsing, so its warning list belongs in the ledger as observations next to the parsed values.
status: mined
limitation: README claims only; malformed-PE handling details live in the code and its version.
province-fit: in — PE parsing.
obscurity: mainstream

ID-SLUG: magic5-archlinux
source: magic(5) man page, Arch package core/file 5.48-1 — https://man.archlinux.org/man/magic.5.en
kind: docs
tier: A
scope: The file(1) magic-database language (offsets, types, indirect, !:mime, !:strength) as shipped in file 5.48.
anchor: §DESCRIPTION, "!:strength" paragraph; file 5.48-1; accessed 2026-10-29; "This constant is applied using the specified operator to the currently computed default magic strength."
teaches: file(1) output is the highest-strength matching rule in a heuristic ranking, so cite it as a first-pass type guess, not a format determination.
status: mined
limitation: Distribution-rendered page for one version; magic rules themselves live in the separate Magdir database.
province-fit: in — artifact triage.
obscurity: mainstream

## G. Parser generators with stronger guarantees (adjacent, obscure)

ID-SLUG: everparse-manual
source: EverParse Manual — https://project-everest.github.io/everparse/
kind: docs
tier: A
scope: The EverParse project's description of its components (LowParse, 3D, QuackyDucky, EverCBOR, EverCDDL) and claims of verification.
anchor: landing page intro; accessed 2026-10-29; "EverParse is a framework for generating verified secure parsers and formatters from domain-specific format specification languages."
teaches: Formally verified validators are only correct *relative to the spec you write*, which makes the spec itself the artefact needing evidence review.
status: mined
limitation: Project self-description; verification guarantees cover generated components only, not callers or the spec's fidelity to real files.
province-fit: adjacent — parser assurance for RE tooling rather than RE itself.
obscurity: obscure

ID-SLUG: spicy-docs
source: Spicy — Generating Robust Parsers for Protocols & File Formats (Spicy 1.18.0-dev.55 docs) — https://docs.zeek.org/projects/spicy/en/latest/index.html
kind: docs
tier: A
scope: Zeek's Spicy attributed-grammar parser generator for protocols and file formats, as documented at 1.18.0-dev.55.
anchor: §"Overview"; accessed 2026-10-29; "Spicy is a parser generator that makes it easy to create robust C++ parsers for network protocols, file formats, and more."
teaches: Grammar plus semantic hooks in one DSL gives incremental, stream-safe parsing, useful when an artifact is a captured stream rather than a seekable file.
status: mined
limitation: "Robust" is the project's design goal, not a proof; dev-version docs.
province-fit: adjacent — offline parsing of captured protocol/file data.
obscurity: obscure

ID-SLUG: ogf-dfdl-v1
source: Data Format Description Language (DFDL) v1.0 Specification, GFD-R-P.240, February 2021 (OGF; hosted by Apache Daffodil) — https://daffodil.apache.org/docs/dfdl/
kind: spec
tier: A
scope: The OGF standard for describing text/binary formats in annotated XML Schema, incl. its error taxonomy.
anchor: §3.2 "Failure Types", GFD-R-P.240 February 2021 (obsoletes GFD-P-R.207/174); accessed 2026-10-29; "Schema Definition Error or SDE for short - these indicate the DFDL schema is not meaningful."
teaches: DFDL separates "the description is wrong" (SDE) from "the data does not fit" (Processing Error), the same split a ledger needs between hypothesis failure and artifact anomaly.
status: mined
limitation: Aimed at legacy/scientific data interchange; few RE tools consume DFDL directly.
province-fit: adjacent — format-description methodology.
obscurity: obscure

## H. Visual references

ID-SLUG: corkami-binary-posters
source: corkami/pics binary/README.md (Ange Albertini) — https://github.com/corkami/pics/blob/master/binary/README.md (@669facbb0b6a)
kind: docs
tier: C
scope: An index of annotated format posters/dissections (PE, ELF, Mach-O, Class, DEX, PYC, WOFF2, UF2, …) with source SVGs and PoC files.
anchor: §"101" heading @669facbb0b6a; accessed 2026-10-29; "Dissection with more descriptions, and explanations (my initial style of binary posters)."
teaches: Hand-built minimal PoC files beside each poster are ready-made byte fixtures for checking a parser against a known-annotated layout.
status: mined
limitation: Secondary/visual reference by one author; defer to primary specs for normative field semantics.
province-fit: in — format orientation and fixtures.
obscurity: niche

---

## Screened and dropped
- https://refspecs.linuxfoundation.org/elf/gabi4+/ch4.eheader.html and LSB symversion page — Anubis anti-bot wall returned instead of content; replaced by the sco.com gABI host.
- https://gitlab.com/x86-psABIs/x86-64-ABI (project page) — JS-rendered, no spec text; used raw dl.tex instead. Tags list only goes to abi_0_96 (2005), not useful as a pin.
- https://man7.org/linux/man-pages/man5/magic.5.html — 404; used man.archlinux.org copy.
- https://www.sweetscape.com/010editor/manual/IntroTempScripts.html, …/IntroTemplates.html — 404.
- https://raw.githubusercontent.com/apple-oss-distributions/dyld/main/cache-builder/dyld_cache_format.h — 404 (path guess); dyld shared cache format left unmined.
- https://raw.githubusercontent.com/hjl-tools/linux-abi/master/linux-abi.tex — 404; psABI dl.tex covers GNU property notes.
- https://docs.google.com/document/d/1lyPIbmsYbXnpNj57a261hgOYVpNRcgydurVQIyZOz_o/pub (go.dev/s/go12symtab, Russ Cox, July 2013) — Go 1.2-only design doc, superseded by gosym reader code.
- https://github.com/facebook/hermes/blob/main/doc/Design.md — architecture prose, not byte format; replaced by BytecodeFileFormat.h.
- https://www.darwinsys.com/file/ — upstream homepage/history, no byte-checkable content beyond magic(5).
- https://llvm.org/docs/PDB/* via GitHub commit API — GitHub REST API rate-limited (unauthenticated); pins taken with git ls-remote instead.
- https://dwarfstd.org/dwarf5std.html — landing page only; mined the PDF it links.
- source.android.com dex-format, learn.microsoft.com PE format, github.com/WerWolv/ImHex — already in corpus (skipped by rule 3).

## Search log
- Direct fetch (curl, 2026-10-29) of 56 candidate URLs from the slice brief plus leads; 4 more pin/aux fetches (gosym, constructintro, pdb-rs, psABI raw tex ×4).
- web_search queries (4):
  1. "Corkami file format posters PE ELF Mach-O pics github" → corkami/pics (kept).
  2. "Hermes bytecode format BytecodeFileFormat.h facebook hermes BytecodeVersion" → BytecodeFileFormat.h/BytecodeVersion.h (kept).
  3. "Android VDEX OAT ART file format vdex_file.h source googlesource" → vdex_file.h (kept); oat.h/image.h noted, not fetched.
  4. "binary format description language DFDL OR Spicy OR binary templates parser generator untrusted file formats" → DFDL, Spicy, EverParse, Kaitai #170 (all kept).
- Leads found inside fetched pages: microsoft/pdb-rs (from LLVM PDB index) → kept; LLVM TpiStream → kept.
- Pins: git ls-remote HEAD on 12 GitHub repos + go/art googlesource + llvm-project main; GitLab API for psABI head commit.
- Counts: identified ≈62 · opened/screened 56 · kept 40 rows (obscure 10, niche 17, mainstream 13) · dropped 12 (+3 corpus duplicates skipped).
- Installs/updates: none.
