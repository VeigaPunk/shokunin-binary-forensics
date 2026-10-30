# bf-source-pack / SLICE=triage-tools (round-73, opened 2026-10-29)

Slice owner: BfTriageTools. Scope after de-scope by SHOKUNIN_BINARY_FORENSICS: OFRAK, UEFITool, Diaphora / ghidriff / BinDiff, Dogbolt, Compiler Explorer, rev.ng, RetDec, Unicorn / Qiling, Binary Ninja, Cutter / rz-ghidra. Dropped as overlapping with another agent: capa, FLOSS, YARA, EMBA, FACT_core, unblob, binwalk.

Method note: web pages were opened with `read`. GitHub READMEs were first fetched with `curl -sL` on the raw URL and the facts re-confirmed via `read` for the raw-README ranges quoted for Qiling, ghidriff and RetDec. Commit shas come from `gh api repos/<o>/<r>/commits` (default branch HEAD, authenticated; the unauthenticated API was rate-limited). No tool was installed or executed, and no sample was downloaded. Installs recorded: none.

---

## Included sources

### 1. OFRAK
- title: https://github.com/redballoonsecurity/ofrak (docs: https://ofrak.com/docs/)
- kind: tool
- tier: A
- scope: what OFRAK claims to do (identify / unpack / analyze / modify / repack), which backends it integrates, and its license terms as stated in README. This says nothing about format coverage accuracy.
- anchor: README.md "License" section + ofrak.com/docs/ index ("OFRAK Docs", mkdocs); repo `master` @ `1e1ef750222c` (2026-08-13); latest GitHub release `ofrak-v3.2.0` (2023-08-10).
- quote: "Users interested in OFRAK for commercial purposes can request the Pro or Enterprise License." (README, "License" section)
- teaches: An agent can decide when a firmware blob needs a recursive unpack / analyze / repack workflow with a scriptable Python API and a GUI resource tree (entropy, byteclass and magnitude maps). It can also tell up front that use is gated by the OFRAK Community License, which README says is for "educational uses, personal development".
- obscurity/value: OFRAK is a firmware-aware resource-tree framework rather than a disassembler. It is the only tool in this slice that treats "unpack -> analyze -> modify -> repack" as one reproducible script.
- rea-route: firmware-analysis (independent oracle against Binwalk 3.1.x / Unblob 26.6.x region and extraction reports; REA does not use OFRAK). REA doc head confirms it accepts Binwalk 3.1.x and Unblob 26.6.x only, with no mount, emulation or execution of extracted programs.
- limits: README is a vendor claim with no format list. The license is the custom OFRAK Community License (GitHub reports `NOASSERTION` for it). Commercial use needs a paid license. Repack and patch features are outside the lane's static-only, no-modify posture. Last tagged release is 2023-08, while master is more recent.

### 2. UEFITool (+ UEFIExtract / UEFIFind)
- title: https://github.com/LongSoft/UEFITool
- kind: tool
- tier: A
- scope: UEFI PI firmware-image parsing into a tree, and the tool family's documented known issues. Scoped to the `new_engine` branch (the default branch).
- anchor: README.md (intro, "Derived projects", "Alternatives", "Known issues", "GUID Database"); `new_engine` @ `de73942df908` (2026-10-27); latest release `A76` (2026-10-24); license BSD-2-Clause per GitHub metadata.
- quote: "UEFITool is a viewer and editor of firmware images conforming to UEFI Platform Interface (PI) Specifications." (README, first paragraph under "Very Brief Introduction to UEFITool")
- teaches: An agent can parse a UEFI flash image into volumes, files and sections, dump the tree with UEFIExtract, and grep it with UEFIFind. It can cross-check GUID names against the fwupd/LVFS GUID database that ships with each release. README also lists independent parsers (FMMT, Fiano, uefi-firmware-parser, CHIPSEC, CERT UEFI Parser) for second-opinion parsing.
- obscurity/value: This is the de facto reference parser for UEFI firmware volumes, and its "Alternatives" list is a ready-made multi-parser oracle set.
- rea-route: firmware-analysis (UEFI images are not covered by Binwalk/Unblob-only REA; UEFITool would be the independent oracle for any future UEFI-volume claim). No REA UEFI doc was found in /home/vgpnk/.local/share/rea/docs, so the crosswalk is [INFERENCE].
- limits: README states "Image editing is currently only possible using an outdated and unsupported UEFITool 0.28". Some vendor update files (encrypted HP, Dell HDR/EXE, some InsydeFlash FD) cannot be opened. FIT editing is unsupported. It does not validate Secure Boot or Boot Guard signatures. Parsing is structural, not a security verdict.

### 3. Diaphora
- title: https://github.com/joxeankoret/diaphora
- kind: tool
- tier: A
- scope: Diaphora 3.5 feature set and IDA-version support as stated by its author. Not an accuracy benchmark.
- anchor: README.md "Installation" + "Unique Features" + "Licensing problems"; `master` @ `35c765708183` (2026-10-25); README names version 3.5.0.
- quote: "Diaphora supports versions of IDA >= 7.4 because the code only runs in Python 3.X (Python 3.11 was the last version being tested)." (README, "Installation")
- teaches: An agent can pick the right function-matching oracle for patch diffing. Documented features are call-graph matching, pseudo-code diffing, microcode support, struct/enum porting, "Potentially fixed vulnerabilities detection", and parallel diffing. README links a wiki for batch export and diff automation.
- obscurity/value: Diaphora has the widest heuristic set among public diffing tools and is the reference for pseudo-code and compilation-unit diffing. Its README links worked CVE patch-diff screenshots (CVE-2020-1350, CVE-2023-28231).
- rea-route: native-function-matching (independent oracle for REA `match_native_functions` pairings across builds). REA matches by exact names first, then independent body bytes, and says exact names establish name correspondence, not unchanged code. Diaphora's similarity ratio could cross-check that, but it requires IDA.
- limits: It is an IDA plugin, so it needs a licensed IDA (lane covers ida-pro-mcp already). License is AGPL-3.0 with commercial licenses available. The "most advanced... as of today (2026)" claim is the author's own and unverified. Tested only up to Python 3.11.

### 4. BinDiff (+ BinExport)
- title: https://github.com/google/bindiff
- kind: tool
- tier: A
- scope: BinDiff's stated purpose, supported disassemblers (IDA Pro, Binary Ninja, Ghidra), license, and the two original algorithm papers. Not an accuracy claim.
- anchor: README.md "Quickstart", "About BinDiff", "Further reading / Similar tools", "License"; `main` @ `13c437afa074` (2026-09-18); latest release `v8` (2023-09-25). Companion repo google/binexport @ `9648cacb21a7`.
- quote: "BinDiff relies on a separate disassembler. Out of the box, it ships with support for IDA Pro, Binary Ninja and Ghidra." (README, "Quickstart" note)
- teaches: An agent can run structural function matching over exported disassemblies and port names/comments between versions. README bundles `docs/papers/`: Dullien & Rolles, "Graph-Based Comparison of Executable Objects" (SSTIC 2005), and Flake, "Structural Comparison of Executable Objects" (DIMVA 2004), so the matching algorithm is checkable against primary literature.
- obscurity/value: The Apache-2.0 repo ships the algorithm papers next to the code, which makes it a ground-truth reference for what "BinDiff-style function match" means.
- rea-route: native-function-matching (independent oracle; Ghidra exports via BinExport are in the REA provider set).
- limits: The Java GUI build needs the commercial yFiles library. The README says "A subset of the existing manual" is in `docs/`. The last tagged release is v8 (2023-09), later than the paper but older than HEAD. It is not a verdict that a changed function is a vulnerability fix.

### 5. ghidriff
- title: https://github.com/clearbluejar/ghidriff (docs: https://clearbluejar.github.io/ghidriff)
- kind: tool
- tier: A
- scope: ghidriff's CLI patch-diff workflow, its three engines (SimpleDiff, StructualGraphDiff, VersionTrackingDiff) and output formats. Not a correctness benchmark.
- anchor: README.md "Ghidriff - Ghidra Binary Diffing Engine", "Features", "Engine", "Implementations"; `main` @ `4f5d895fcbb1` (2026-05-11); license GPL-3.0 per GitHub metadata.
- quote: "Its primary use case is patch diffing. Its ability to perform a patch diff with a single command makes it ideal for automated analysis." (README, "Ghidriff" intro)
- teaches: An agent can emit JSON plus Markdown (optionally side-by-side HTML) lists of added, deleted and modified functions from two binaries headlessly. It gets meta-diffs of strings, callers/callees and binary metadata. The README states Ghidra "(No license required)" in the "Batteries Included" list. The `SimpleDiff` engine "relies mostly on known symbol names", so symbol-poor targets need the Version Tracking engine.
- obscurity/value: It is the one open, scriptable, Ghidra-native differ with a clean engine-extension interface (`find_matches`), and it fits REA's Ghidra provider ecosystem.
- rea-route: native-function-matching (independent oracle; same Ghidra analysis substrate, so it is not independent of Ghidra analysis bugs. Pair with Diaphora/BinDiff for a different matcher).
- limits: Results depend on Ghidra auto-analysis quality. A "modified function" is a matcher output, not a source-level change claim. The README speed claim ("full Windows kernel in less than a minute", after analysis) is unverified by me.

### 6. Decompiler Explorer (Dogbolt)
- title: https://dogbolt.org/faq (site: https://dogbolt.org/ ; code: https://github.com/decompiler-explorer/decompiler-explorer)
- kind: tool
- tier: A
- scope: what the service is, which decompilers it hosts, upload size and retention, and its no-automation policy. Valid for the FAQ read on 2026-10-29.
- anchor: dogbolt.org/faq headings "What is this?", "What happens to the binaries?", "Is there an API?"; homepage "Upload File" note; repo decompiler-explorer/decompiler-explorer @ `9afcaecd99ac` (2026-10-28).
- quote: "It is an interactive online decompiler which shows equivalent C-like output of decompiled programs from many popular decompilers." (FAQ, "What is this?")
- teaches: An agent can compare C-like output for the same sample across angr, Binary Ninja, Boomerang, dewolf, Ghidra, Hex-Rays, Kuna, REC Studio, Reko, Relyze, RetDec, rev.ng and Snowman as a disagreement-spotting oracle. The site provides its own samples, so no upload is needed.
- obscurity/value: It is the only place where 13 decompilers run on one input side by side. Comparing them is the quickest check for single-decompiler artifacts.
- rea-route: native-investigation / ghidra-provider (independent oracle for decompiler-output disagreements; supports REA's rule that pseudocode is not ground truth).
- limits: HOMEPAGE: "Your file must be less than 2MB in size. Uploaded binaries are retained." FAQ: "All submitted binaries are saved and made available to any of the authors of the tools used". FAQ: "there is intentionally no public API for automation". Lane rule: do NOT upload private or customer artifacts and do not automate. Use only the built-in samples or public, non-sensitive binaries. Hosting is provided by Vector 35 and Hex-Rays, and some engines are commercial.

### 7. Compiler Explorer (godbolt) documentation
- title: https://github.com/compiler-explorer/compiler-explorer/blob/main/docs/WhatIsCompilerExplorer.md (service: https://godbolt.org/)
- kind: docs
- tier: A
- scope: Compiler Explorer's documented behavior: source-to-assembly mapping, optimization flags, binary tools such as `strings`, and an "Execute the code" option. Not a claim about any target's toolchain.
- anchor: docs/WhatIsCompilerExplorer.md, sections "What is Compiler Explorer?", "Execution", "General UI"; repo main @ `c655710e809d` (2026-10-28).
- quote: "Compiler Explorer lets you see how a compiler sees your code." (opening paragraph)
- teaches: An agent can write a small source snippet that mimics a hypothesised function, compile it across compiler versions and `-O` levels, and compare the emitted assembly and idioms with a recovered function. That gives evidence for "this looks like -O2 GCC output" as a hypothesis, not a fact.
- obscurity/value: It is the cheapest oracle for compiler-idiom and ABI questions such as prologue shape, `lea` arithmetic and inlining behavior. The docs themselves show a worked `add` to `lea` example.
- rea-route: native-investigation / go-binaries / rust-binaries (a reference for what the compiler would emit for known source, checked against REA disassembly dossiers).
- limits: It is a hosted service. Do not paste proprietary source from a client artifact. The doc notes the default run has no optimization ("By default, the compiler is run with no optimization enabled"). It compiles source and does not decompile or analyze third-party binaries. An "Execute the code" option exists, but this lane must not use it on target-derived code.

### 8. rev.ng (framework and documentation)
- title: https://docs.rev.ng/what-is-revng/ (repo: https://github.com/revng/revng)
- kind: docs
- tier: A
- scope: rev.ng's architecture, design claims (QEMU lifting, LLVM passes, model-in-YAML), and license as stated by its maintainers. Not decompilation correctness.
- anchor: docs.rev.ng "What is rev.ng?" (mkdocs-material 9.7.7) + repo README "License"; `develop` @ `8c2db55d27d3` (2026-10-28); `master` @ `ba8cdb027808` (2026-09-11).
- quote: "Note that we never emulate any code, we simply use QEMU as a lifter." (docs.rev.ng/what-is-revng, "Based on QEMU" bullet)
- teaches: An agent can see how a static lifter keeps analysis non-executing. It learns the "model" YAML document, the artifact-versus-analysis split, `MetaAddress`, Data Layout Analysis for inferring data structures, and import from IDA `.idb`/`.i64`, DWARF and PDB.
- obscurity/value: It is a fully open decompilation pipeline that emits C "designed to be valid and recompilable", with data-structure inference as its distinguishing feature.
- rea-route: native-investigation (independent decompiler and lifter outside the Ghidra/IDA/Hopper providers; also supports reconstruction-readiness reasoning about recompilable output).
- limits: Design claims, not benchmarks. The project is GPLv2 as a whole (QEMU) with files individually MIT-licensed, per README. The repo default branch is `develop`, so docs may lead the releases. Architecture coverage is not enumerated on this page.

### 9. RetDec
- title: https://github.com/avast/retdec
- kind: tool
- tier: A
- scope: RetDec 5.0 supported formats and architectures, feature list, maintenance status and license as stated in README.
- anchor: README.md top warning, intro feature list, "License"; `master` @ `9450585772e6` (2026-05-26); latest release `v5.0` (2022-12-08); MIT license.
- quote: "Supported file formats: ELF, PE, Mach-O, COFF, AR (archive), Intel HEX, and raw machine code" (README, intro list)
- teaches: An agent can run a retargetable, LLVM-based decompile of ELF/PE/Mach-O/COFF/Intel HEX/raw code. The documented features include compiler and packer detection, signature-based removal of statically linked library code, DWARF/PDB extraction, C++ class reconstruction via RTTI/vtables, and output in C or a Python-like language. README names a "limited maintenance mode" warning, so treat output as a second-opinion decompiler.
- obscurity/value: It is one of the few permissively licensed (MIT), non-Ghidra, non-commercial decompilers with a library API and a published regression-test corpus.
- rea-route: native-investigation / raw-binary (independent decompiler for Ghidra-opened raw images, supports the REA rule that output is a hypothesis).
- limits: README warning: "limited maintenance mode due to a lack of resources". Issues are answered with delays up to a quarter. Supported 32-bit set is x86, ARM, MIPS, PIC32, PowerPC and 64-bit is x86-64 and ARM64 only. The last release is 2022-12. An installed copy needs about 5 to 6 GB. The README's feature claims are unverified by me.

### 10. Unicorn Engine FAQ
- title: https://github.com/unicorn-engine/unicorn/blob/master/docs/FAQ.md (README: https://github.com/unicorn-engine/unicorn)
- kind: docs
- tier: A
- scope: Unicorn behavior caveats: PC sync, hooks, TB caching, MMU and TLB, MIPS kseg and ARM M-class non-executable regions. Version-scoped: the PC rules differ before and after 2.1.4.
- anchor: docs/FAQ.md "Why do I get a wrong PC after emulation stops?" (sections "For version < 2.1.4" and ">= 2.1.4"), "Editing an instruction doesn't take effect"; `master` @ `7c5db94191de` (2026-02-17); latest release `2.1.4` (2025-09-09); GPLv2.
- quote: "We should always have valid PC all the time. Please report an issue for your case." (FAQ, "For version >= 2.1.4")
- teaches: An agent can interpret emulation outcomes correctly. Before 2.1.4 the PC may be left at the start of the basic block on an exception unless code/memory hooks are installed. TB chaining means patched code needs `uc_ctl_remove_cache`. ARM THUMB needs `UC_MODE_THUMB` with an odd start address, and `uc_mem_map` handles physical addresses.
- obscurity/value: It is an official, version-scoped oracle for emulator edge cases that silently corrupt emulated-trace conclusions.
- rea-route: binary-diagnostics. REA doc pins "Unicorn 2.1.2" and states "PLT inference can emulate selected instructions in Unicorn; its outputs are static candidates." Under this FAQ, 2.1.2 falls in the "< 2.1.4" PC-sync caveat group. Any REA claim relying on a final PC after an exception should be read with that caveat [INFERENCE: whether REA's PLT inference touches that path was not tested].
- limits: Unicorn is a CPU-only emulator, so there are no OS or syscall semantics. It "does lots of dirty hacks within qemu code" and bases on qemu 5.0.1 since 2.0.0, so newer instructions may be unsupported. The FAQ is maintainer prose and does not cover every ISA quirk. The README banner says "LOOKING FOR CONTRIBUTORS!", so maintenance cadence is a concern.

### 11. Qiling Framework
- title: https://github.com/qilingframework/qiling (docs: https://docs.qiling.io)
- kind: tool
- tier: A
- scope: what Qiling adds over Unicorn and QEMU user-mode (loaders, syscalls, OS context, hooks, snapshots), supported platforms, and license, as stated in README. Not a fidelity guarantee.
- anchor: README.md "Qiling vs. Unicorn engine", "Qiling vs. QEMU user mode", "License"; `master` @ `86c927cb3299` (2026-09-05); GPLv2.
- quote: "Unicorn can only emulate raw machine instructions, without Operating System (OS) context." (README, "Qiling vs. Unicorn engine")
- teaches: An agent can pick the right layer. Unicorn emulates raw instructions, while Qiling adds PE/Mach-O/ELF loaders, dynamic linkers, syscall and IO handlers, hooks at instruction/block/memory/syscall level, state save and restore, and "hot patch". It supports Windows, macOS, Linux, Android, BSD, UEFI, DOS and MBR on 8086 through RISC-V.
- obscurity/value: Its UEFI, MBR, DOS, firmware-MCU and kernel-driver (via Demigod) emulation targets are unusual in open tooling. They give a way to exercise firmware without hardware.
- rea-route: firmware-analysis / binary-diagnostics (adjacent only; REA states "No device, root privilege, mount, emulation or execution of extracted programs is needed" for firmware analysis, so Qiling is outside REA's static boundary).
- limits: Emulation executes target code in an emulator, which crosses the lane's static-only line. Detonating or running malware is refused by lane policy, so use only on benign or owned samples under explicit operator gating. README feature list is vendor prose. Unicorn's QEMU-5-era instruction limits (see #10) still apply.

### 12. Binary Ninja documentation (BNIL overview)
- title: https://docs.binary.ninja/dev/bnil-overview.html
- kind: docs
- tier: A
- scope: BNIL structure (Lifted IL, LLIL, MLIL, HLIL, SSA forms) and notation, as documented on 2026-10-29. License facts scoped to the Free Edition license page.
- anchor: docs.binary.ninja "Binary Ninja Intermediate Language: Overview" (zensical-0.0.50 generator; no page version stamp). Closest revision proxy: Vector35/binaryninja-api @ `ee31d1ca8251` (2026-10-28). Also read https://docs.binary.ninja/getting-started.html and https://docs.binary.ninja/about/license/free.html.
- quote: "The Binary Ninja Intermediate Language (BNIL) is a semantic representation of the assembly language instructions for a native architecture in Binary Ninja." (BNIL overview, first paragraph)
- teaches: An agent can read IL output correctly. All comparisons are signed `s<=` or unsigned `u>=`, size suffixes are `.q .d .w .b`, `sx`/`zx` mark extension, `COMBINE/LOWx/HIGHx` macros exist, and `rax_2:0.d` means the low 32 bits sign-extended. LLIL is flag-folded Lifted IL, MLIL has variables and types, and HLIL adds control-flow structure and an AST.
- obscurity/value: BNIL is a documented, tree-based, architecture-independent IR, so an agent can express lifter-level assertions such as "this call has N params in MLIL" without relying on decompiler prose. DogBolt and BinDiff both list Binary Ninja as a supported engine.
- rea-route: native-investigation (conceptual reference for IL vs disassembly vs pseudo-code distinctions; Binary Ninja is not an REA provider).
- limits: Binary Ninja is commercial software. The Free Edition license says "you may not decompile, decrypt, reverse engineer, disassemble or otherwise reduce the Software to human-readable form under this License", is "for your internal evaluation and non-commercial purposes only", and "we reserve the right to revoke or terminate the Software". Download links expire after 72 hours without active support. The doc pages carry no version stamp, so the revision proxy is approximate. Binary Ninja appears in this slice as a backend of Dogbolt, OFRAK and BinDiff as well as a standalone product; the brief's already-covered list does not name it.

### 13. rz-ghidra
- title: https://github.com/rizinorg/rz-ghidra
- kind: tool
- tier: A
- scope: how the plugin integrates the Ghidra decompiler and Sleigh into Rizin/Cutter, its commands, its Rizin version pairing, and its license, as stated in README.
- anchor: README.md "Usage", "Building", "Versioning and Rizin Compatibility", "License"; `dev` @ `39c4d0cfdbb9` (2026-10-22); LGPL-3.0.
- quote: "It is solely based on the decompiler part of Ghidra, which is written entirely in C++, so Ghidra itself is not required at all" (README, intro; line break in source after "in C++,")
- teaches: An agent can run the Ghidra decompiler (`pdg`, `pdgj` JSON, `pdgo` with offsets, `pdgs` for loaded Sleigh languages) inside Rizin without a Ghidra install. It can pin a Sleigh language with `ghidra.lang` (for example `x86:LE:32:default`) and must point `ghidra.sleighhome` at the `*.sla` / `*.lspec` files.
- obscurity/value: It is a lightweight way to get Ghidra's decompiler as an independent oracle against a Ghidra Java provider run. Sleigh language IDs are explicit, so mismatches are easy to detect.
- rea-route: ghidra-provider / reverse-engineering-tools (REA calls caller-supplied Rizin; rz-ghidra is the Rizin-side Ghidra decompiler, so same-decompiler cross-check on a different host).
- limits: README states "Rizin has a quickly evolving C API", so rz-ghidra versions are paired with Rizin versions and release numbers are "not guaranteed" to match. The plugin is LGPLv3, "more strict than Ghidra's license". It uses the same decompiler, so it is not an independent decompilation algorithm.

### 14. Cutter
- title: https://github.com/rizinorg/cutter (user docs: https://cutter.re/docs/user-docs.html)
- kind: tool
- tier: A
- scope: Cutter distribution channels, plugin model (Python and native C++), and Docker option as stated in README. User-docs pages themselves were not opened.
- anchor: README.md "Getting Cutter", "Plugins"; `dev` @ `d7f11b220884` (2026-09-11); GPL-3.0.
- quote: "Cutter supports both Python and Native C++ plugins." (README, "Plugins")
- teaches: An agent can drive a Rizin-backed GUI and bridge scripts through Python plugins. README points to the Ghidra decompiler integration, a DynamoRIO coverage visualiser, an official plugin list at `rizinorg/cutter-plugins`, and a provided Docker config.
- obscurity/value: Cutter is the maintained GUI for the Rizin ecosystem, and REA already ships a Cutter bridge.
- rea-route: reverse-engineering-tools (REA doc "Cutter bridge" section states Cutter commands use the local REA Python bridge and authenticated loopback messages; Cutter is already an REA integration).
- limits: README only. It does not specify decompiler or analysis accuracy. The "Docker image" option runs `docker` which this lane should treat as an installer, not as evidence. The Cutter user docs page was not opened by me, so docs.cutter.re claims are not made.

---

## REJECTED

- REJECTED: Binary Ninja Free Edition as a tool for the lane's own automated use. Located quote (docs.binary.ninja/about/license/free.html, clause 5): "These restrictions include prohibitions on the use the Software for service bureau or time-sharing purposes". The license forbids decompiling or reverse-engineering the software and limits the Free edition to "internal evaluation and non-commercial purposes", so it cannot be bundled or offered as a service. flip: a Commercial/Ultimate license or a Vector 35 headless license for the operator's own use; the BNIL docs (#12) remain usable independently.
- REJECTED: Dogbolt as an automation oracle. Located quote (dogbolt.org/faq, "Is there an API?"): "there is intentionally no public API for automation". It is kept in #6 only as a manual comparison tool with a no-private-upload rule. flip: the vendors' written automation terms, or a private self-hosted instance using only the open-source engines (the FAQ says private instances "may or may not" be compatible).

## LEADS (not opened or not fully opened)

- https://cutter.re/docs/user-docs.html : linked from Cutter README, not opened. Failure: not attempted (README facts suffice for a lead).
- https://github.com/avast/retdec/wiki and https://retdec.com/publications/ : linked from RetDec README, not opened. Failure: not attempted.
- https://github.com/joxeankoret/diaphora/wiki : linked from Diaphora README for batch/automation, not opened. Failure: not attempted.
- https://clearbluejar.github.io/ghidriff : linked ghidriff docs site, not opened. Failure: not attempted. README `:60-140` read via `read`; the remaining README was only skimmed with grep, so CLI-option claims are unverified.
- https://docs.binary.ninja/dev/bnil-llil.html, /bnil-mlil.html, /bnil-hlil.html : the per-IL instruction references (the true oracle for operator semantics) were not opened. Failure: not attempted.
- https://github.com/google/bindiff/blob/main/docs/disassemblers.md : the supported disassembler-version matrix was not opened. Failure: not attempted.
- GitHub unauthenticated API: rate-limited ("You have triggered an abuse detection mechanism" / "API rate limit exceeded") before re-running with the authenticated `gh` CLI; all shas above are from the authenticated run.
- Dropped by de-scope message, not screened: capa, FLOSS, YARA, EMBA, FACT_core, unblob, binwalk.

## search-log

Slice: triage-tools. Where: operator-listed candidate set (no web search), after the SHOKUNIN_BINARY_FORENSICS de-scope. Identified: 20 candidates in the brief (capa, capa-rules, FLOSS, YARA, OFRAK, EMBA, FACT_core, UEFITool, binwalk, unblob, Cutter/rz-ghidra, rev.ng, RetDec, BinDiff, Diaphora, ghidriff, Dogbolt, Compiler Explorer, Unicorn/Qiling, Binary Ninja). Screened: 14 (6 were dropped by the de-scope message without being opened; 1 shas-only attempt on capa/FLOSS before the de-scope). Included: 14 (OFRAK, UEFITool, Diaphora, BinDiff, ghidriff, Dogbolt, Compiler Explorer, rev.ng, RetDec, Unicorn, Qiling, Binary Ninja docs, rz-ghidra, Cutter). Excluded: 6 de-scoped and not opened. Rejected-with-flip entries: 2 (both partial scope rejections of otherwise included sources). Leads: 8. Install actions: none.
