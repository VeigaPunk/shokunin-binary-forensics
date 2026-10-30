# bf-source-pack / format-obscura

Agent: SHOKUNIN_BINARY_FORENSICS.BfFormatObscura. Date opened: 2026-10-29.
Scope after coordinator de-scope: Corkami, PoC||GTFO, ImHex-Patterns, 010 templates, magic(5), pefile malformed-PE handling, other obscure format-quirk resources. Dropped by instruction: Kaitai, LIEF, binref, DIE, ELF gABI / PE spec / DEX / WASM specs.
Method: every `quote` below was copied from text returned by `read` (or `read` of the raw.githubusercontent.com / arXiv-API rendering of the same page) on 2026-10-29. Nothing was installed, executed, or downloaded as a sample. GitHub commits API was rate-limited (HTTP 403 rate limit), so repo revisions come from `git ls-remote <repo> HEAD` (HEAD of default branch at fetch time).
Installs/updates performed: none.

Safety posture for the whole pack: these sources describe file-format abuse (polyglots, malformed headers, loader differentials). They are included as *oracles for what a static inspector must report*, not as recipes. Several corpora (Corkami PoCs, PoC||GTFO PDFs, Poor-Man's-Obfuscator binaries, Mitra output) are hand-made hostile-looking binaries: read the text and annotated sources only; never run or detonate them.

Reading order if budget is short (top 12): Lost in the Loader; loaders_modeling; Linux ELF idiosyncrasies (kernel docs); tmp.out Pt.4 Limit Break; tmp.out Dead Bytes; Corkami PE.md; Corkami PE corpus readme; Corkami Abusing File Formats; pefile; PolyFile README; APE spec; Poor Man's Obfuscator.

---

## INCLUDED

### Corkami "Abusing file formats" (AbusingFileFormats/README.md)
- title: https://github.com/corkami/docs/blob/master/AbusingFileFormats/README.md
- kind: docs
- tier: A
- scope: Ange Albertini's taxonomy and vocabulary of file-identification/polyglot/chimera/parasite behaviour for ~30 formats (ELF, PE, Mach-O/CAFEBABE, PDF, ZIP, RAR, TAR, MP4 atoms, ROM headers); not a loader-version-specific claim set.
- anchor: section "Introduction" and "Identification" / "Specific Examples" / "Bad Magic Signatures"; 1192-line file; repo corkami/docs commit fd339bf6bebe7aa086a02a95b5a4fd9ef0c1bd28 (2024-05-04). Base article is PoC||GTFO 7:6.
- quote: "First, you must realize that a file has no intrinsic meaning." — section "Introduction".
- teaches: Distinguishes polyglot vs multi-personality vs chimera vs collision, and lists where magic is (not) enforced (e.g. "Java .CLASS and Universal Mach-O" share `CA FE BA BE`, ZIP/PDF/7z/RAR parsed from the tail), so an RE agent can state which magic checks a file-type claim actually rests on and which format-confusion alternatives must be listed as limitations.
- obscurity/value: The single densest "what does each parser really require at offset 0 / near EOF" reference; the oracle for why `file`-style identification is a hypothesis, not a fact.
- rea-route: raw-binary (what "unrecognized bytes" can legitimately mean), native-investigation limitations, firmware-analysis (embedded/offset-nonzero containers). Read REA docs raw-binary.md and firmware-analysis.md heads.
- limits: Author's analysis, not a standard; many examples are 2013-2017-era viewers (Adobe Reader versions, WinRAR); blacklisting claims are version-scoped to those readers.

### Corkami "PE" notes (PE/PE.md)
- title: https://github.com/corkami/docs/blob/master/PE/PE.md
- kind: docs
- tier: B
- scope: Windows XP–7 x86/x64 PE loader *observed* behaviour (required vs ignored header elements); not current Windows builds, not OBJ/COFF.
- anchor: sections "required elements", "structure by structure → e_lfanew / SizeOfOptionalHeader / NumberOfSections"; 2040-line file; repo corkami/docs commit fd339bf6bebe7aa086a02a95b5a4fd9ef0c1bd28. Self-declared scope line: "x86/x64 Windows (from XP to W7) binaries".
- quote: "`tiny` has a `e_lfanew` of 4, which means the NT Headers is overlapping the DOS Header." — section "e_lfanew".
- teaches: Concrete header-overlap, low-alignment, zero-section, virtual-section-table and `SizeOfOptionalHeader`-as-delta facts; an agent can predict which PE fields a static reader must tolerate and why "section table lies in file slack/virtual space" is a valid, not corrupt, reading.
- obscurity/value: Ground truth for "the PE the loader accepts is smaller than the PE the spec describes"; pairs every claim with a hand-assembled PoC.
- rea-route: pe-imports, pe-load-config, pe-certificates (all decode PE tables from declared directories; this notes which declarations can lie or overlap). Read pe-imports.md ("`import_directory` ... locations are the file spans actually read") and pe-load-config.md.
- limits: Loader behaviour is XP/W7-era and explicitly "reality of the loader" observations; later Windows may differ (see Lost in the Loader for XP/7/10 deltas). Wiki-gadget/flash embeds are dead.

### Corkami PE corpus (pocs/PE, readme.txt + file list)
- title: https://github.com/corkami/pocs/tree/master/PE
- kind: dataset
- tier: B
- scope: Catalogue and source (NASM/FASM `.asm`) of ~200 hand-built PE variants; use the readme and `.asm` sources as annotated specifications; do not run `.exe`.
- anchor: `PE/readme.txt` ranking list (`*..` common, `**.` non-standard, `***` complex), directory listing incl. `cfgbogus.asm`, `delaycorrupt.asm`, `delayfake.asm`, `dllfwloop.asm`, `foldedhdr.asm`, `appendedhdr.asm`; repo corkami/pocs commit 6d277c83efdceb6916ee8c6efe6ff0639cc6193f (2024-12-22). Repo root README is a one-line stub.
- quote: "a set of handmade files showing the various possibilities of the Portable Executable format, under Windows." — readme.txt first paragraph.
- teaches: A named test-corpus map for parser regression: delay-import corruption, forwarder loops, CFG-table bogus values, appended/folded headers, null/virtual entry points; an agent can cite a specific PoC name when asserting what a PE inspector should survive.
- obscurity/value: The reference corpus other parsers (pefile README itself links it as "corkami's treasure trove of PE weirdness") test against.
- rea-route: pe-imports (delayimports/delaycorrupt/dllfw*), pe-load-config (cfgbogus, dllcfgdup), pe-certificates (security-directory file-offset semantics). Only static reading of sources is in-scope.
- limits: Samples are intentionally hostile-looking; behaviour claims are XP–W7; the repo README is a stub, authority sits in readme.txt and `.asm` bodies.

### Corkami "x86 oddities" (x86/x86.md)
- title: https://github.com/corkami/docs/blob/master/x86/x86.md
- kind: docs
- tier: B
- scope: x86/x64 instruction-encoding oddities as of 2011-era CPUs (prefix limits, register order, undocumented encodings), tested via author's CoST file.
- anchor: section "general → instruction length"; 643-line file; repo corkami/docs commit fd339bf6bebe7aa086a02a95b5a4fd9ef0c1bd28.
- quote: "An instruction is limited to 15 bytes on recent CPUs (it changed over time):" — section "instruction length".
- teaches: Checks for decoder disagreement: overlong prefix chains, 15-byte limit exceptions, encoding-order facts that a function-boundary or instruction-length claim must respect.
- obscurity/value: Cheap independent check when two disassemblers disagree on instruction length at the same offset.
- rea-route: native-function-matching (matches rely on decoded procedure inventories; instruction-length disagreement poisons matches). Read native-function-matching.md head.
- limits: CPU-vendor-specific details drift; Intel SDM / AMD APM are authoritative (other peer slice).

### PoC||GTFO archive index (pocorgtfo.hacke.rs)
- title: https://pocorgtfo.hacke.rs/
- kind: docs
- tier: B
- scope: Issue index, per-issue `file(1)` classification and MD5 of pocorgtfo00–22 PDFs; read index only, do not open/execute the PDFs (several are executable polyglots).
- anchor: top `info pocorgtfo*` block and per-issue headings; last release listed 0x22 (Feb 06 2024).
- quote: "pocorgtfo06.pdf : POSIX tar archive (GNU)" — top `info pocorgtfo*` block (same file is a PDF, ZIP and tar).
- teaches: The same bytes classify as PDF, boot sector, ISO9660, tar, WavPack, NES ROM, HTML depending on the identifier; a worked demonstration that `file(1)` output is one reading.
- obscurity/value: The canonical living museum of multi-format files; the `file` column alone is a lesson in classification ambiguity.
- rea-route: raw-binary, firmware-analysis (container identification), packet-captures (pcapng polyglots in 0x21).
- limits: Index/metadata only; per-article technical content was not opened here (see angea mirror and 11:9 below).

### PoC||GTFO mirror (angea/pocorgtfo README)
- title: https://github.com/angea/pocorgtfo/blob/master/README.md
- kind: docs
- tier: B
- scope: Article index with per-issue "polyglot:" format list and links to per-article PDFs and archive.org scans, 0x00–0x22.
- anchor: per-issue headers, e.g. "0x06 ... polyglot: TAR, ZIP, PDF"; repo angea/pocorgtfo commit 933c020f498bcfa85b4ed2cea6fd213eac1c9fe7.
- quote: "polyglot: TAR, ZIP, PDF" — heading line under "### 0x06".
- teaches: Lets an agent pull one narrow article (e.g. 0x00 "ELFs are dorky, elves are cool", 0x07 "Innovations with Core Files", 0x06 "Davinci Seal: Self-decrypting Executables") rather than a 300-page PDF; names the exact polyglot stack per issue.
- obscurity/value: Article-granular index of ELF/PE/ROM structure papers that are otherwise only in giant PDFs.
- rea-route: elf-notes (core-file and ELF-structure articles), kernel-modules (ELF .ko), raw-binary.
- limits: Index only; hosts executable polyglot PDFs — never run them.

### "The Treachery of Files" (PoC||GTFO 11:9, Evan Sultanik)
- title: https://github.com/angea/pocorgtfo/blob/master/contents/articles/11-09.pdf
- kind: paper
- tier: B
- scope: One concrete HTML/Ruby/PDF/ZIP polyglot built to show how parsers disagree; anatomy figure of which bytes each parser consumes; PDF-reader 1024-byte `%PDF` window.
- anchor: article PDF `contents/articles/11-09.pdf` (PoC||GTFO issue 0x11, 2016); repo angea/pocorgtfo commit 933c020f498bcfa85b4ed2cea6fd213eac1c9fe7.
- quote: "this PDF is an HTTP quine: it is a web server that serves copies of itself." — page 1.
- teaches: How to reason about "which bytes does parser X consume" with a figure per format; the "PDFium requires %PDF within first 1024 bytes" differential.
- obscurity/value: Compact worked example of the schizophrenic/polyglot distinction later productized in PolyFile.
- rea-route: raw-binary and firmware-analysis (container-in-container reasoning).
- limits: Article contains runnable polyglot source; static reading only; PDF-to-text extraction (markit) garbled layout.

### Trail of Bits "Two New Tools that Tame the Treachery of Files"
- title: https://blog.trailofbits.com/2019/11/01/two-new-tools-that-tame-the-treachery-of-files/
- kind: docs
- tier: B
- scope: Definitions (polyglot vs schizophrenic file), motivation for PolyFile/PolyTracker, DARPA SafeDocs framing; 2019 state of tools.
- anchor: sections "Ceci N'est Pas Un PDF", "PolyFile: Ground Truth Labeling of File Semantics"; published 2019-11-01.
- quote: "Polyglots are files that can be validly interpreted as two different formats." — second paragraph of intro.
- teaches: Vocabulary and a hypothesis ("unsafe portions exist in the symmetric difference of the parsers' accepted grammars") an agent can use to phrase format-ambiguity limitations.
- obscurity/value: Short authoritative-by-author statement of the parser-differential model for file formats.
- rea-route: raw-binary, firmware-analysis.
- limits: Blog (2019); counts such as "10,000 file formats" were superseded (see PolyFile README: libmagic definitions).

### PolyFile README (trailofbits/polyfile)
- title: https://github.com/trailofbits/polyfile/blob/master/README.md
- kind: tool
- tier: A
- scope: Behaviour/claims of the PolyFile CLI as documented at the pinned commit (recursive identification, pure-Python libmagic re-implementation, not an every-offset scanner).
- anchor: first paragraph and "Quickstart"/"Usage" sections; repo trailofbits/polyfile commit 6aaeee1fd521938e62279582e4df4d52348c4f96.
- quote: "A utility to identify and map the semantic and syntactic structure of files, including polyglots, chimeras, and schizophrenic files." — first paragraph.
- teaches: States its own limit ("does not scan every offset the way binwalk does") — an agent can cite exactly what a PolyFile-style result does and does not establish.
- obscurity/value: Maintainer statement of an independent file-identification oracle whose output is a byte-range map, aligning with REA's evidence-range discipline.
- rea-route: raw-binary, firmware-analysis (Binwalk/Unblob are the REA tools; PolyFile is an independent cross-check).
- limits: Not installed or run here; behaviour claims are the README's. Quickstart tells you to `uv tool install`; only relevant if a later wave decides to adopt it.

### Mitra (corkami/mitra README)
- title: https://github.com/corkami/mitra/blob/master/README.md
- kind: tool
- tier: B
- scope: Layout taxonomy of weird-file construction (Stack, Cavity, Parasite, Zipper, overlap) and per-format status matrix; first 64 of 339 lines read.
- anchor: sections "Features", "Goals → Exploration", "Status"; repo corkami/mitra commit 95e1d2a7e4fcac552111a9fbe708223e0c60383a.
- quote: "Stacks (appended data), Cavities (blank space), Parasites (comments), Zippers (mutual comments)." — "Features" section.
- teaches: A four-way vocabulary for where foreign bytes can sit relative to a format's structure, plus a status table of which formats tolerate magic-at-offset-zero, appended data, footers.
- obscurity/value: The only systematic "which formats permit which polyglot layout" table.
- rea-route: raw-binary, firmware-analysis (embedded payload placement).
- limits: Generator tool; included for taxonomy only. Do not use it to produce files; README is partial (first 60 lines read).

### file(1) magic(5) manual (darwinsys/file doc/magic.man)
- title: https://github.com/file/file/blob/master/doc/magic.man
- kind: spec
- tier: A
- scope: Syntax and evaluation semantics of libmagic magic source fragments (offsets, types, `string`/`regex`/`indirect`/`use`/`name`), as of the pinned revision.
- anchor: `$File: magic.man,v 1.118 2026/04/19 19:56:49 christos` (Dd April 19, 2026); repo file/file commit 41b1123083ab0bbdfe32f6d4ec14f6aec9a91e59 (2026-10-22). 882-line file, first 300 read. man7.org URL returned 404 (see LEADS).
- quote: "A test compares the data starting at a particular offset in the file with a byte value, a string or a numeric value." — DESCRIPTION.
- teaches: How to read a `file` verdict as a list of offset/type/value tests; negative offsets from EOF, `indirect` re-entry, endianness-typed integers (`lelong`/`belong`/`melong`), and the warning that `regex` "can take exponential time" — so an agent can say which tests a classification actually rests on.
- obscurity/value: The maintainers' own definition of the thing behind every `file` answer; also the grammar for ImHex `magic/` files and PolyFile's re-implementation.
- rea-route: raw-binary (REA does not infer architecture from ".bin" or unrecognized bytes; magic(5) says what libmagic can and cannot infer).
- limits: Describes the rule language, not the shipped database's completeness; rest of man page (strength rules, mime/apple/ext options) not read.

### ImHex-Patterns (WerWolv/ImHex-Patterns)
- title: https://github.com/WerWolv/ImHex-Patterns
- kind: code
- tier: B
- scope: Community-curated `.hexpat` structural definitions (713-line README table incl. ELF, COFF, DOS, DEX, DMP64, ESP32/ESP8266 images, ARM VTOR, AMD ucode, APFS/ext4/exFAT, bplist, EVTX) plus libmagic `magic/` files and YARA rules.
- anchor: README "Hex Patterns" table and top-level directory list (`patterns`, `includes`, `magic`, `yara`); repo WerWolv/ImHex-Patterns commit e07e98adc810f0c052035ee1fdabae7ec65110e2 (2026-09-22).
- quote: "Patterns - Binary Format definitions for the Pattern Language" — README bullet list.
- teaches: An independent, executable structural description per format (byte ranges and field names) to check an inspector's offsets against, including vendor/firmware formats with few other public parsers.
- obscurity/value: Breadth: ESP image, AMD microcode, ARM Cortex-M vector table, Windows kernel dump, `$I` recycle-bin — formats that nothing else documents as a grammar.
- rea-route: firmware-analysis, elf-notes (patterns/elf.hexpat cross-check), managed-code-analysis (no direct), raw-binary (arm_cm_vtor.hexpat describes a vector table used to pick `--entry-point`).
- limits: Community-submitted, unequal quality; a pattern is a hypothesis about field layout and trusts fixed sizes (BraekerCTF write-up below shows the Mach-O pattern desynchronising on a declared-size mismatch). Read the README table only; individual `.hexpat` bodies not audited.

### 010 Editor Binary Template repository
- title: https://www.sweetscape.com/010editor/repository/templates/
- kind: code
- tier: B
- scope: Listing and per-file descriptions of ~410 `.bt` templates by category (Archive, Drives, Executable, Electronics, Game…); templates are downloadable text but require the proprietary 010 Editor to execute.
- anchor: Repository index page, sort by Category, 413-row table (page banner: "010 Editor v17.0"); first 163 lines read; no per-template revision shown.
- quote: "This page contains a repository of Binary Templates for use with 010 Editor." — page lead paragraph.
- teaches: Names of reusable independent grammars for firmware containers (`UImage.bt`, `SquashFS.bt`, `ROMFS.bt`, `SRec.bt`), executables (`ELF.bt`, `EXE.bt`, `MachO.bt`, `CLI.bt` for .NET metadata header, `bpf_elf.bt`), and disk/FS images (`MBR.bt`, `GPTHeader.bt`, `Ext4.bt`, `LUKS.bt`).
- obscurity/value: Decades-deep long tail of obscure formats (retro floppies, Mifare dumps, game archives) that can serve as byte-range cross-checks.
- rea-route: firmware-analysis (UImage/SquashFS/ROMFS), managed-code-analysis (CLI.bt as second reading of the CLI header), elf-notes (ELF.bt).
- limits: Templates are third-party, unversioned on the index; per-template pages (`file_info.php?file=…`) not opened; execution requires a commercial editor, so only the text is usable as documentation here.

### pefile (erocarrera/pefile): malformed-PE handling
- title: https://github.com/erocarrera/pefile/blob/master/pefile.py (and README.md)
- kind: code
- tier: A
- scope: Behaviour of pefile 2024.8.26 toward malformed/abusive PEs: warning categories, section-table checks, import/export "Assuming corrupt" bail-outs, `max_symbol_exports` caps; also the PEiD-signature and import-hash features REA mirrors.
- anchor: module docstring lines 8-16; `__version__ = "2024.8.26"` (line 20); warning strings near lines 3566 ("Too many sections ... (>=MAX_SECTIONS)"), 3609/3623 ("Suspicious value found parsing section"), 3675 ("Suspicious flags ... WRITE and EXECUTE ... packed executable"), 5515-5604 ("Assuming corrupt"); repo erocarrera/pefile commit 274e0b8ce0b804a09a3cb68314f41b00ae2ed8a0 (2026-10-28). README "Additional resources" links Corkami's PE weirdness.
- quote: "pefile has been tested against many edge cases such as corrupted and malformed PEs as well as malware" — pefile.py module docstring.
- teaches: The de-facto compatibility target for "pefile-compatible import hash" (REA's `inspect_pe_imports` says it computes that); the exact warning vocabulary, caps and abort paths tell an agent what a Python reference reader will refuse vs tolerate, and a section warning text states "this might imply the file is trying to confuse tools which parse this incorrectly."
- obscurity/value: Reading the warning branches is a fast, citable checklist of PE anomalies; pefile is the oracle other tooling hashes against (imphash).
- rea-route: pe-imports (imphash, delay-load, overflow-RVA handling), pe-load-config, pe-certificates (pefile points to verify-sigs for Authenticode, i.e. does not itself validate it).
- limits: Single implementation (Python) not the Windows loader; "tested against many edge cases" is a maintainer claim, not a conformance suite; tests corpus lives in a separate repo (pefile-tests), not opened. Version-scoped to 2024.8.26.

### Lost in the Loader: The Many Faces of the Windows PE File Format (RAID 2021)
- title: https://www.s3.eurecom.fr/docs/raid21_nisi.pdf (DOI https://doi.org/10.1145/3471621.3471848; ACM full-text returned HTTP 403, see LEADS)
- kind: paper
- tier: A
- scope: Windows XP SP3, 7 SP1, 10 v1909 loader models (`MiCreateImageFileMap`, `LdrpInitializeProcess`) vs ClamAV/YARA/radare2 parsers; findings are version-scoped to those builds and tool versions.
- anchor: author's version of Nisi, Graziano, Fratantonio, Balzarotti, RAID '21 (Oct 6-8, 2021), 16 pp; sections 3 (structural vs compliance checks vs memory mapping), 5 (differential generation), 6 (model validation: 80/72/20 generated cases ran), 8; first 225 of 460 converted lines read.
- quote: "we present the first systematic analysis and exploration of PE parsers." — abstract.
- teaches: A three-way split of what any PE consumer does (structural checks / compliance checks / memory mapping) and that "there is no reference implementation"; an agent should report PE facts as loader-model-relative and name which Windows version model it assumes. Introduction also cites Kim et al.: AV engines skipping files that carry a copied Authenticode signature.
- obscurity/value: The best-in-class demonstration that PE validity is not a Boolean; supplies the vocabulary REA's evidence ledger needs when a PE is "valid for X, rejected by Y".
- rea-route: pe-imports, pe-load-config (paper models the Import Directory, IAT, Load Config and Base Relocation directories), pe-certificates (Authenticode-skip motivation).
- limits: Windows 10 v1909 and earlier; later Windows (11, 24H2) not modelled; models were extracted by manual RE, authors report validation by generated cases, not exhaustive proof. Abstract-level quotes only; Table 1 truncated in the converted text.

### eurecom-s3/loaders_modeling (models, generator, differential tooling)
- title: https://github.com/eurecom-s3/loaders_modeling
- kind: dataset
- tier: A
- scope: Released framework and models for Windows XP/7/10 loaders and RE/AV tools; scope is exactly what the README states (models are submodule `eurecom-s3/loaders-models` @ d29d62b).
- anchor: README sections "What is this about?", "Modeling Language", "Analysis Tasks & Examples" (sample validation, generation, differential generation, differences enumeration, corner-case generation), requires `z3`; repo eurecom-s3/loaders_modeling commit 80d105df90169b54539360cd100fd8bd238cc348.
- quote: "This project provides a framework for modeling and analyzing the behavior of parsers for executable file formats" — "What is this about?".
- teaches: The `.lmod` model language lets an agent read the loader's check list (MZ magic, `e_lfanew + 0xf8 <= FILESIZE`, PE signature `0x4550`) as explicit predicates; also a way to ask "does model X accept sample Y" offline.
- obscurity/value: Machine-readable ground truth for PE loader acceptance; no other public artifact does this.
- rea-route: pe-imports, pe-load-config, pe-certificates (acceptance gating for the tables those tools decode).
- limits: Python 3 + z3, Ubuntu-20.04-era install notes; `generate.py` can emit hostile samples — documentation use only; not run here. Model accuracy is the paper's claim (see above).

### Linux-specific ELF idiosyncrasies (kernel docs)
- title: https://docs.kernel.org/next/ELF/ELF.html
- kind: docs
- tier: A
- scope: Which duplicated program headers the Linux kernel honours: PT_INTERP, PT_GNU_STACK, PT_GNU_PROPERTY (kernel docs "next" tree as of fetch date; versions tagged inline).
- anchor: sections "Definitions", "PT_INTERP" (since Linux 2.4.11), "PT_GNU_STACK" (since 2.6.6), "PT_GNU_PROPERTY" (since 5.8); fetched 2026-10-29 from the `next` tree (no commit shown on page).
- quote: "First PT_INTERP program header is used to locate the filename of ELF interpreter. Other PT_INTERP headers are ignored (since Linux 2.4.11)." — "PT_INTERP".
- teaches: "First" = smallest file offset, "Last" = biggest; with duplicates the kernel picks the first PT_INTERP and the last PT_GNU_STACK / PT_GNU_PROPERTY. An agent can state which of several declared headers actually governed loading, and flag when a static reader picked a different duplicate.
- obscurity/value: Three-paragraph page that settles duplicate-header ambiguity authoritatively; most tools silently pick one.
- rea-route: binary-diagnostics (reports "mitigation indicators" such as NX, which rides on PT_GNU_STACK), elf-notes (PT_NOTE / SHT_NOTE are enumerated independently), kernel-modules.
- limits: Covers only three header types; says nothing on PT_NOTE, PT_LOAD overlap or section headers; `next` tree may change.

### tmp.out #1 "Dead Bytes" (xcellerator, LibGolf)
- title: https://tmpout.sh/1/1.html
- kind: community
- tier: B
- scope: x86-64 Linux kernel ELF loader: which `e_ident` / ELF-header / program-header bytes were ignored at write-up time (2021, kernel version not stated). Empirical, reproducible via LibGolf hexdump.
- anchor: sections "Falling At The First Hurdle", "Turning The Corruption Up To 11"; includes 127-byte annotated hexdump with 50 bytes replaced by `X`; issue 1 of tmp.0ut (date not shown on page).
- quote: "Just how much of the ELF and program headers will the Linux loader ignore?" — "Turning The Corruption Up To 11".
- teaches: Loader-ignored vs loader-required fields (ignored: EI_CLASS/EI_DATA/EI_VERSION/EI_OSABI/e_version/e_flags/all section-header fields/p_paddr/p_align; required: e_type, e_machine, e_entry, e_phoff, e_ehsize, e_phentsize, e_phnum). Shows `gdb`/`objdump` refusing a file the loader runs.
- obscurity/value: Hands-on enumeration an RE agent can use to explain why "malformed per readelf" does not mean "not executable".
- rea-route: elf-notes, binary-diagnostics (REA checks header-table file ranges before seeks).
- limits: Not kernel-versioned (the later tmp.out Pt.4 shows the kernel behaviour changed in 2020); author's own testing; community write-up, never tier A.

### tmp.out #2 "ELF Binary Mangling Pt.4: Limit Break" (netspooky)
- title: https://tmpout.sh/2/11.html
- kind: community
- tier: B
- scope: Linux kernel ELF loader behaviour change in 2020 (READ_IMPLIES_EXEC / PT_GNU_STACK interplay) and tracing `load_elf_binary` in binfmt_elf.c; first 70 of ~850 lines read.
- anchor: sections 1 "Background", 2 "Read No Longer Implies Exec", 4 "Tracing the ELF Loader"; tmp.0ut issue 2.
- quote: "a change in the kernel's ELF loader that would render this trick useless." — section 0 "Introduction".
- teaches: The loader contract moves between kernel versions; a header trick (program header at 0x1C, `p_flags` overlapping `e_phoff`) stopped working, so any claim about "what the loader accepts" must name a kernel version.
- obscurity/value: Rare dated evidence of loader drift, with the section-vs-segment and ignored-field analysis that REA ELF routes depend on.
- rea-route: elf-notes, binary-diagnostics.
- limits: Only the introduction/background read; later sections (Overlay 0x38/0x31, write-or-die) not read. Author-reported results.

### tmp.out #5 "A deep dive into how the Linux kernel loads executable files" (dominikr)
- title: https://tmpout.sh/5/9.html
- kind: community
- tier: B
- scope: Kernel 6.18 LTS `fs/exec.c` / `binfmt_*` dispatch, x86 subarchitectures (X86_64, X86_X32_ABI, IA32_EMULATION); first 140 of ~445 lines read.
- anchor: sections "Methodology", "Open questions", "What actually happens inside the kernel" (linking to elixir.bootlin.com v6.18 `fs/exec.c#L1651`); tmp.0ut issue 5.
- quote: "it will try all loaders until one signals back that it can load the file." — "What actually happens inside the kernel".
- teaches: Which binfmt handler gets first refusal and when `point_of_no_return` commits; why an EM_386 or EM_X86_64 ELF ignores EI_CLASS/EI_DATA (e_machine alone selects layout), and how x32 (EM_X86_64 with 32-bit structures) fits.
- obscurity/value: The first rigorous source-level walk of ELF acceptance the authors know of ("never been a rigorous analysis" per its intro).
- rea-route: elf-notes, kernel-modules, binary-diagnostics (ELF64 x86-64 only verified).
- limits: Secondary analysis of kernel source; x86-focused, ~half unread; verify against the cited kernel version before reuse.

### tmp.out #5 "Inside and Outside a 57-Byte x86-64 Linux ELF" (Fanda Uchytil)
- title: https://tmpout.sh/5/3.html
- kind: community
- tier: B
- scope: Minimal ELF64 that passes `execve(2)` (57 and 60 bytes), overlapping header fields; first 80 of ~1120 lines read.
- anchor: section "Officer, I Swear It Is a Working Example" (annotated 57-byte xxd); tmp.0ut issue 5.
- quote: "The Linux ELF loader is willing to put up with a surprising amount of abuse." — "INTRO".
- teaches: Minimum viable fields for the loader and how e_phentsize/e_phnum/e_type/e_machine alone drive acceptance; a fixture an ELF inspector's "structural limits" tests can be compared to.
- obscurity/value: Smallest known accepted structures; shows "having a program header record" ≠ "meaningful PT_LOAD".
- rea-route: elf-notes, binary-diagnostics.
- limits: Process crashes on run (segfault) by design — a loader-accepted ELF is not a functioning program; read-only study.

### tmp.out #2 "Some ELF Parser Bugs" (netspooky)
- title: https://tmpout.sh/2/3.html
- kind: community
- tier: B
- scope: ELF-parser assumption failures in readelf/rabin2/Ghidra 10.1.1/IDA 7.6/GDB (endianness byte, trusted sizes) circa 2021; sections 1.0 and 2.0 read (lines 1-420 of 760).
- anchor: sections "1.0 Endianness Assumptions", "2.0 Trusting Reported Sizes"; tmp.0ut issue 2.
- quote: "Assuming data is little endian unless explicitly specified can lead to misparsing issues that will cascade across a complex analysis stack." — section 1.0.
- teaches: `ei_data` flipped gives `e_machine` read as 0x800 and absurd header counts across several tools while the loader ignores it; "spooky tip": check `e_machine` before guessing endianness and report the inconsistency.
- obscurity/value: Names concrete analyzer assumptions that a trustworthy inspector must surface as "limitations", not silently coerce.
- rea-route: elf-notes, binary-diagnostics.
- limits / safety: Section 1.2 measures detection-rate evasion on VirusTotal and section 2 includes tool-crash PoCs (base64 ELF, rizin memory corruption, kernel SIGBUS). Use only the parser-assumption facts; do not reproduce the evasion measurement or the crash PoCs. Tool versions are 2021 (radare2 5.3.1, rizin 0.3.0-git, Ghidra 10.1.1, IDA 7.6).

### Actually Portable Executable (APE) Specification v0.1 (jart/cosmopolitan)
- title: https://github.com/jart/cosmopolitan/blob/master/ape/specification.md
- kind: spec
- tier: A
- scope: The APE file-format definition itself (three 8-byte magics, MZ-polyglot with UNIX shell script, ELF/Mach-O/PE/BIOS entrypoints); first 130 of ~680 lines read.
- anchor: sections "File Header" → "(1) APE MZ Magic" (`MZqFpD='`, hex 4d 5a 71 46 70 44 3d 27), "(2) APE UNIX-Only Magic" (`jartsr='`); repo jart/cosmopolitan commit aefad27c09ffda64c6ac64bd69f758e9f9c7b91d.
- quote: "an executable file format that polyglots the Windows Portable Executable (PE) format with a UNIX Sixth Edition style shell script" — page lead paragraph.
- teaches: How to recognise an APE file (magic is both an MZ header and a shell string assignment; letters are valid x86 in 16/32/64-bit modes) so that a PE/ELF/Mach-O inspector's partial reading is reported as a polyglot, with the MS-DOS stub as the dispatch point.
- obscurity/value: A modern polyglot executable shipping as real software; the one case where a PE reader seeing a stub is *by design* a partial view.
- rea-route: raw-binary, pe-imports (PE tables of an APE are minimal; absence is observed absence only), pe-certificates.
- limits: Spec v0.1; remainder (sections on ELF/Mach-O/PE structures, runtime behaviour) unread. The author's own page justine.lol/ape.html timed out (see LEADS).

### The Poor Man's Obfuscator (Romain Thomas, Pass the Salt 2022)
- title: https://www.romainthomas.fr/publication/22-pst-the-poor-mans-obfuscator/whitepaper.pdf
- kind: paper
- tier: A
- scope: ELF and Mach-O metadata transformations (exports, `.eh_frame`/`__unwind_info` shuffle, section swaps, `LC_FUNCTION_STARTS`, `.dynsym` size) against IDA 7.7.211224, Binary Ninja 3.0, radare2 5.7.0, Ghidra 10.1.4; results are tool-version-scoped.
- anchor: whitepaper PDF, July 2022; sections 2 (unwind info), 3.3 (export addresses), 4.1 (ELF sections swap list), 4.2 (Mach-O `__text`/`__stubs` shift and dyld layout checks); first 300 of 402 converted lines read. Companion repo and slides not opened.
- quote: "these transformations do not modify the assembly code or the data of the binary." — section 1.
- teaches: Section-vs-segment trust boundary: loaders use segments/program headers while analyzers trust sections, exports, unwind data; table of which of the four tools was impacted by each metadata change; Mach-O `dyld` enforces stricter section layout than ELF loaders.
- obscurity/value: Quantifies how little metadata editing it takes to mislead a disassembler without touching code — the exact threat model for an artifact-first RE lane.
- rea-route: binary-diagnostics (section/segment inventory), elf-notes, native-function-matching (function-start poisoning feeds procedure inventories).
- limits: Tool versions are mid-2022; paper itself warns loading options may change outcomes; transformations use LIEF (not run here).

### BraekerCTF 2024 "Injecting Commands" write-up (Intrigus)
- title: https://intrigus.org/research/2024/03/03/braeker-ctf-2024-injecting-commands-writeup/
- kind: community
- tier: B
- scope: One Mach-O x86-64 CTF binary with code inside load commands: `LC_UUID` cmdsize 0x32, fake `__PAGEZERO` mapping file offset 0 as r-x, `LC_UNIXTHREAD` entry; first 300 of 346 lines read.
- anchor: sections "Analyzing the Binary in Ghidra", "Analyzing the Binary in ImHex", "Emulating the Binary with Unicorn"; published 2024-03-03.
- quote: "so the `commandSize` should be 4 + 4 + 16 = 0x18, but it is 0x32." — "Analyzing the Binary in ImHex".
- teaches: Real instance where Ghidra (SubFrameworkCommand EOF exception) and an ImHex pattern (fixed-size assumption) fail on declared load-command sizes while the binary runs; entry comes from `LC_UNIXTHREAD` RIP, not LC_MAIN. Shows a static+emulation (Unicorn, mapped at 0x1000) path.
- obscurity/value: Rare public Mach-O malformed-load-command case study with concrete tool failures.
- rea-route: raw-binary (map-and-emulate with explicit base), native-investigation limitations.
- limits: Single CTF sample; tool versions unstated; it suggests running the binary on a macOS CI runner (dynamic execution) — outside this lane, static/emulation parts only; says nothing about current dyld acceptance.

### "On the Abuse and Detection of Polyglot Files" (Koch et al., arXiv 2407.01529)
- title: https://arxiv.org/abs/2407.01529
- kind: paper
- tier: A
- scope: Survey of 30 in-the-wild polyglot samples and 15 attack chains; detection-tool failures on polyglots; PolyConv classifier and ImSan sanitizer results as claimed by the authors.
- anchor: arXiv:2407.01529, published 2024-07-01 (cs.CR, cs.ML); version suffix not shown by the fetch; abstract only was read.
- quote: "A polyglot is a file that is valid in two or more formats." — abstract, first sentence.
- teaches: Evidence that identification/embedded-file tools "fail to reliably detect polyglot files used in the wild"; supports the pack's rule that a format label is a hypothesis.
- obscurity/value: First survey of real polyglot usage; counts and categories are citable.
- rea-route: raw-binary, firmware-analysis.
- limits: Abstract only; claims about PolyConv/ImSan performance are the authors'. Neither Mach-O/dyld-specific nor PE-loader-specific.

---

## REJECTED

- REJECTED: Corkami "PDF tricks" (https://github.com/corkami/docs/blob/master/PDF/PDF.md) — reason: no REA route (REA has no PDF analysis doc) and Google-Code-era wiki with dead gadget embeds; located quote: "In short: they're odd, but they work, and they're clean." (intro disclaimer); flip: if REA gains a PDF/document-analysis route, reopen as tier B for PDF structure quirks.
- REJECTED: Corkami "Initial register values under Windows" (https://github.com/corkami/docs/blob/master/InitialValues.md) — reason: stale (NT4–Vista dumps, VM-dependent); located quote: "Note: some values may change slightly, depending on your exact configuration and settings."; flip: a Win32 emulation-fidelity route targeting XP–Vista guests.
- REJECTED: corkami/formats README (https://github.com/corkami/formats) — reason: stub, no content; located quote: "# formats File formats" (entire README); flip: a populated README at a later revision (HEAD 723090cf82ee54044d02583aed0f1da623fa136e had none).
- REJECTED: corkami/sbud README (https://github.com/corkami/sbud) — reason: stub (only "# sbud"); Trail of Bits post confirms it "only supports a couple image formats"; flip: documentation added beyond the title (HEAD 5eb7a064be3c0a0991971e98d3978ad990577253).
- REJECTED: corkami/pocs repo-root README (https://github.com/corkami/pocs) as its own source — reason: one-line stub; located quote: "Proof of Concepts" (entire README); folded into the PE corpus entry above where `PE/readme.txt` is the real document; flip: root README that documents layout/hostile-sample policy.

---

## LEADS (unopened/unreachable; nothing here is a verified source)

- https://justine.lol/ape.html — author's APE write-up; `read` failed: "The operation timed out"; spec on GitHub opened instead.
- https://dl.acm.org/doi/fullHtml/10.1145/3471621.3471848 — ACM full text of Lost in the Loader; `read` returned HTTP 403; author-hosted PDF opened instead.
- https://man7.org/linux/man-pages/man5/magic.5.html — HTTP 404; used upstream `doc/magic.man`.
- https://api.github.com/repos/*/commits?per_page=1 — HTTP 403 "API rate limit exceeded" for most repos (first batch for corkami/docs … kaitai succeeded); shas taken with `git ls-remote` instead.
- Stefan Esser "Death of the vmsize=0 dyld trick" (SyScan 2015 deck) — surfaced by search, not opened; would give historic dyld multi-pass segment-handling evidence.
- Romain Thomas Poor Man's Obfuscator slides + repo (https://www.romainthomas.fr/publication/22-pst-the-poor-mans-obfuscator/ , https://github.com/romainthomas/the-poor-mans-obfuscator) — not opened.
- https://tmpout.sh/5/13.html (halfexec) and https://tmpout.sh/5/14.html (halfshelf) — search-snippet only; not opened.
- tmp.out "Creating polyglot ELF files for fun and anti-forensics" (issue 5, referenced from 5/9) — URL not located.
- netspooky "ELF Binary Mangling" parts 1-3 (tmp.out issue 1/2 and 0xFFtactics PoC) — not opened.
- https://gist.github.com/malx-labs/1db7e755627666aa8a443258a138e52f ("99 Adversarial PE Fixtures") and https://iwishi808.github.io/2026/06/11/pe-parser-validation-analysis/ — search results only; unvetted blogs, not opened.
- https://deepwiki.com/angea/pocorgtfo/1.2-polyglot-files-explained — auto-generated summary site, not opened (prefer upstream articles).
- https://hexbase.dev/formats/elf — search snippet only; not opened.
- Ange Albertini "Funky File Formats" video series (https://www.youtube.com/watch?v=hdCs6bPM4is) — video, not opened.
- Kim et al. 2017, AV products' handling of signed PEs with copied Authenticode signatures (cited in Lost in the Loader intro) — paper not located.
- Cozzi et al., study of tampered executable formats in malware (cited in Lost in the Loader intro) — paper not located.
- Phrack "Cheating the ELF" (grugq) and related RTLD articles — recalled from memory, not found via search, not opened.
- Not pursued by instruction (de-scope): Kaitai Struct gallery/docs, LIEF docs, Binary Refinery, Detect It Easy signature docs.

---

## search-log

Where/query: (1) direct opens of the candidate list in the assignment (corkami/docs, corkami/pocs, ImHex-Patterns, 010 repository, pefile, PoC||GTFO index/mirror, magic(5)); (2) web_search for "Art of ELF", ELF/Mach-O/PE loader-vs-analyzer differentials, tmp.out ELF mangling, Treachery of Files / PolyFile, Mach-O malformed load commands, Poor Man's Obfuscator, BraekerCTF Mach-O; (3) REA docs (elf-notes, pe-imports, pe-load-config, pe-certificates, raw-binary, binary-diagnostics, firmware-analysis, managed-code-analysis, native-function-matching, kernel-modules) read first 22-40 lines for crosswalk.
Identified 47 candidates (assignment list + search results + citations inside opened sources); screened 31 by opening; included 26; excluded 5 (REJECTED with located quotes); left as unopened/unreachable LEADS 16 (some LEADS are categories of repeated failures or unlocated citations). Dropped without screening per coordinator de-scope: Kaitai, LIEF, binref, DIE, capa, FLOSS, YARA, ELF gABI/PE/WASM/DEX specs.
Notes: the pack over-delivers the 8-12 target (26) because the long tail of loader-differential and ELF-mangling sources each ground a distinct REA route; the top-12 reading order is given at the head. Cross-slice overlap to dedupe at merge: "Lost in the Loader" and "Poor Man's Obfuscator" may also be surfaced by BfResearchPapers / obfuscation lanes; tmp.out items may duplicate BfEcosystems ELF coverage.
