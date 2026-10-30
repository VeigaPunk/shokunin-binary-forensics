# ReFrameworkTargets — framework/runtime-specific artifact recovery sources

Slice: Go, Rust, Unity IL2CPP, Flutter/Dart AOT, React Native Hermes, Python bundles, Electron/Node SEA/Bun/Deno/pkg, .NET R2R, JVM/DEX/R8, Lua/LuaJIT, WASM, game-engine and installer containers. All rows accessed 2026-10-29. Pins are full commit SHAs from the GitHub API at fetch time.

## Rows

```
ID-SLUG: goresym-readme
source: GoReSym README — https://github.com/mandiant/GoReSym/blob/722897e0a80da0a06c00c5e40591a253a551f04e/README.md (release v3.4.1; commit 722897e0a80d, 2026-09-14)
kind: tool
tier: A
scope: GoReSym's own README statement of what its Go-symbol parser extends beyond upstream debug/gosym
anchor: README.md §'# GoReSym' (top), commit 722897e0a80da0a06c00c5e40591a253a551f04e, accessed 2026-10-29: "malformed unpacked binaries, such as from UPX"
teaches: Go binaries keep runtime metadata (pclntab/moduledata) that survives stripping, but recovery from UPX-unpacked/split-section files is a tool-specific heuristic layer on top of the stdlib parser, so ledger it as inference-with-tool-version.
status: mined
limitation: The README lists handled cases; it does not prove recovery is correct on any given sample or Go version.
province-fit: in — static symbol/type recovery from shipped Go executables
obscurity: niche
```

```
ID-SLUG: go-pclntab-magic
source: Go internal/abi/symtab.go — https://github.com/golang/go/blob/430d19f07a57ee5ed4e3b1a04b0ab54dd5a24487/src/internal/abi/symtab.go (commit 430d19f07a57, 2026-10-29)
kind: spec
tier: A
scope: The Go toolchain's own constants for the .pclntab/pcHeader magic per Go release range
anchor: src/internal/abi/symtab.go lines 14-25 (const block), commit 430d19f07a57ee5ed4e3b1a04b0ab54dd5a24487, accessed 2026-10-29: "Initial PCLnTabMagic value used in Go 1.2 through Go 1.15." (0xfffffffb; 1.16-1.17 0xfffffffa; 1.18-1.19 0xfffffff0; 1.20+ 0xfffffff1)
teaches: The first 4 bytes of pclntab are a byte-checkable oracle that brackets the producing Go release range and endianness before any heuristic tool runs.
status: mined
limitation: A magic value brackets a toolchain range only; it does not identify the exact Go version (use buildinfo for that) and future releases may add values.
province-fit: in — byte-level fixture source for Go artifact triage
obscurity: niche
```

```
ID-SLUG: go-debug-gosym-pclntab
source: Go debug/gosym/pclntab.go — https://github.com/golang/go/blob/430d19f07a57ee5ed4e3b1a04b0ab54dd5a24487/src/debug/gosym/pclntab.go (commit 430d19f07a57)
kind: code
tier: A
scope: The stdlib reference parser for Go 1.2+ line tables, incl. header validation and endianness detection
anchor: pclntab.go ~line 210-224 (header check in parsePclnTab), commit 430d19f07a57ee5ed4e3b1a04b0ab54dd5a24487, accessed 2026-10-29: "// Check header: 4-byte magic, two zeros, pc quantum, pointer size."
teaches: A pclntab header is only accepted after magic + two zero bytes + pc-quantum∈{1,2,4} + pointer-size∈{4,8}; those five checks are a cheap forged-claim rejection test for 'this is a Go binary'.
status: mined
limitation: The stdlib parser assumes a well-formed table found via section symbols; it does not locate pclntab in stripped/packed files.
province-fit: in — reference implementation behind GoReSym-class tools
obscurity: niche
```

```
ID-SLUG: rustc-demangle
source: rustc-demangle README — https://github.com/rust-lang/rustc-demangle/blob/4023665a9bafb7cd9808033fd76fa50f83b9542c/README.md (commit 4023665a9baf, 2026-10-29)
kind: code
tier: A
scope: The Rust project's own demangler and its C API / native-C port statement
anchor: README.md §'Usage from non-Rust languages', commit 4023665a9bafb7cd9808033fd76fa50f83b9542c, accessed 2026-10-29: "Both the Rust and C versions don't require memory allocation or any other operating-system support."
teaches: Rust symbol names (legacy and v0) have an upstream reference demangler, so demangled names in a ledger should cite this implementation/version rather than a disassembler's built-in guess.
status: mined
limitation: Demangling only applies when symbols survive; it recovers nothing from stripped Rust binaries.
province-fit: in — name recovery for native Rust artifacts
obscurity: mainstream
```

```
ID-SLUG: rustbininfo
source: rustbininfo README — https://github.com/N0fix/rustbininfo/blob/edaf8e59f5f53f252d04ac036ac6518573c4fdfa/README.md (commit edaf8e59f5f5, 2025-05-09)
kind: tool
tier: A
scope: The tool author's README claim of what rbi extracts from stripped Rust executables
anchor: README.md §'## Usage' (argparse help text), commit edaf8e59f5f53f252d04ac036ac6518573c4fdfa, accessed 2026-10-29: "Get information about stripped rust executable, and download its dependencies."
teaches: Stripped Rust binaries still leak rustc commit hash and crate name@version strings (panic paths), which the README example shows mapping to rustc_version and a dependency list.
status: mined
limitation: The rustc/crate attribution is string-heuristic; a 'project-date' guess from dependency versions is inference, not observation.
province-fit: in — static triage of stripped Rust executables
obscurity: obscure
```

```
ID-SLUG: il2cppdumper
source: Il2CppDumper README — https://github.com/Perfare/Il2CppDumper/blob/4741d46ba9cd6159c5d853eb9d6fc48b4bfa2b1a/README.md (release v6.7.46; commit 4741d46ba9cd, 2024-07-06)
kind: tool
tier: A
scope: Il2CppDumper's own feature list and output-file inventory
anchor: README.md §'## Features', commit 4741d46ba9cd6159c5d853eb9d6fc48b4bfa2b1a, accessed 2026-10-29: "Complete DLL restore (except code), can be used to extract `MonoBehaviour` and `MonoScript`"
teaches: Unity IL2CPP recovery pairs the native binary with global-metadata.dat; output 'DummyDll' assemblies carry signatures and metadata but no method bodies.
status: mined
limitation: README also advertises memory-dump input 'to bypass protection'; that path is live-target/protection-bypass and outside the province — use only the static file pair.
province-fit: adjacent — static metadata recovery is in; memory-dump/protection-bypass features are out
obscurity: mainstream
```

```
ID-SLUG: il2cppinspector-redux
source: Il2CppInspectorRedux README — https://github.com/LukeFZ/Il2CppInspectorRedux/blob/8cf49bdbe24cedd2bfa911071af727698aed3130/README.md (release 2026.2; commit 8cf49bdbe24c, 2026-10-28)
kind: tool
tier: A
scope: The maintained Il2CppInspector fork's stated metadata-version coverage
anchor: README.md §'### Redux only features', commit 8cf49bdbe24cedd2bfa911071af727698aed3130, accessed 2026-10-29: "Support for all newer metadata versions (29/29.1/31/35/38/39/104/105/106/106.1/107/108/110)"
teaches: IL2CPP metadata is versioned (24.x … 110) and the parser must match the version; record the metadata version observed in the file header as an Evidence ID before trusting recovered types.
status: mined
limitation: The README also offers DLL-injection projects and decryption loaders for specific commercial games — those are out of province and not endorsed by this row.
province-fit: adjacent — metadata parsing in; injection/game-protection loaders out
obscurity: niche
```

```
ID-SLUG: assetripper
source: AssetRipper README — https://github.com/AssetRipper/AssetRipper/blob/d8363d7aebd7132a7f531bb60ae201a2f167d815/README.md (release 2.0.0; commit d8363d7aebd7, 2026-10-25)
kind: tool
tier: A
scope: AssetRipper's own Unity-version support statement
anchor: README.md top section, commit d8363d7aebd7132a7f531bb60ae201a2f167d815, accessed 2026-10-29: "However, support quality may vary slightly for different Unity versions."
teaches: Unity serialized-asset recovery is version-sensitive across 3.5.0→6000.4.x; the tool itself flags uneven fidelity by version.
status: mined
limitation: Asset extraction from games may implicate copyright; the README's developer-oriented use cases do not license redistribution of extracted assets.
province-fit: adjacent — static asset/serialization recovery; publication of ripped assets is refused
obscurity: mainstream
```

```
ID-SLUG: blutter
source: B(l)utter README — https://github.com/worawit/blutter/blob/4a60ac648bf448c5a7596437243bcd0b9376fdf0/README.md (commit 4a60ac648bf4, 2026-08-18)
kind: tool
tier: A
scope: Blutter's own statement of platform scope and how it obtains a version-matched Dart runtime
anchor: README.md §'## Usage', commit 4a60ac648bf448c5a7596437243bcd0b9376fdf0, accessed 2026-10-29: "If the blutter executable for required Dart version does not exists, the script will automatically checkout Dart source code and compiling it."
teaches: Flutter AOT recovery here works by compiling the exact Dart VM version detected from the engine, so the toolchain build itself becomes part of the evidence chain.
status: mined
limitation: README scopes support to Android arm64 libapp.so and recent Dart versions; obfuscated apps are listed as still missing many functions.
province-fit: in — static Dart AOT snapshot introspection
obscurity: niche
```

```
ID-SLUG: darter
source: darter README — https://github.com/mildsunrise/darter/blob/a6498786ed0f96b2b70635f008fee62dc07796da/README.md (commit a6498786ed0f, 2026-02-03)
kind: tool
tier: A
scope: The author's own deprecation warning about Dart snapshot format churn, plus darter's feature list
anchor: README.md opening ⚠️ Warning banner, commit a6498786ed0f96b2b70635f008fee62dc07796da, accessed 2026-10-29: "The format of Dart snapshots changes CONSTANTLY, and any Dart RE tools like this one NEED constant maintenance"
teaches: Dart snapshot parsers bit-rot by design; any Dart-AOT claim must record the snapshot version hash and the parser revision that read it.
status: mined
limitation: darter's '100% of snapshot data' claim applies to the old versions it supported; the README itself says modern snapshots probably won't parse.
province-fit: in — historical Dart snapshot grammar reference
obscurity: obscure
```

```
ID-SLUG: r2flutter
source: r2flutter README — https://github.com/radareorg/r2flutter/blob/441d614937c8ada56e4d0c1175050667842c0971/README.md (release 0.5.1; commit 441d614937c8, 2026-10-21)
kind: tool
tier: A
scope: r2flutter's own scope statement (Dart 2.10–3.12 layouts, ObjectPool recovery) and non-goal
anchor: README.md §'## What it can do', commit 441d614937c8ada56e4d0c1175050667842c0971, accessed 2026-10-29: "r2flutter is a metadata and analysis aid, not a Dart source-code decompiler."
teaches: A tool that states its non-goal (not a decompiler; best-effort names) gives a clean boundary between observed metadata and inferred source.
status: mined
limitation: Coverage claims ('in-tree layouts for Dart 2.10 through 3.12') are the project's own; not validated here.
province-fit: in — radare2-integrated Dart AOT metadata recovery
obscurity: obscure
```

```
ID-SLUG: r2flutter-objpool-doc
source: r2flutter doc/objpool.md 'Dart AOT Object Pool Internals' — https://github.com/radareorg/r2flutter/blob/441d614937c8ada56e4d0c1175050667842c0971/doc/objpool.md
kind: docs
tier: A
scope: r2flutter's own written description of Dart AOT snapshot symbols and Object Pool placement on Android/iOS
anchor: doc/objpool.md §'## Overview' and §'## Binary Layout', commit 441d614937c8ada56e4d0c1175050667842c0971, accessed 2026-10-29: "The Object Pool is the runtime data structure that holds references to all Dart objects needed during execution."
teaches: The four snapshot symbols (_kDartVm/IsolateSnapshotData/Instructions) are byte-locatable anchors in libapp.so/App.framework and the Object Pool lives in isolate data.
status: mined
limitation: Third-party reverse documentation of an undocumented format; verify field layouts against the Dart SDK revision for the target.
province-fit: in — format notes for Flutter artifacts
obscurity: obscure
```

```
ID-SLUG: unflutter
source: unflutter README — https://github.com/zboralski/unflutter/blob/dbbc2c3c3d898d0726a29da875fb0cf084e21710/README.md (release v0.5.9; commit dbbc2c3c3d89, 2026-05-18)
kind: tool
tier: A
scope: unflutter's own design rationale (VM-free grammar parsing) and comparison to Blutter
anchor: README.md §'## Why Not Blutter', commit dbbc2c3c3d898d0726a29da875fb0cf084e21710, accessed 2026-10-29: "The snapshot is a byte stream with a known grammar. We parse it directly."
teaches: Two recovery strategies trade off explicitly: VM-embedding (fidelity via the real deserializer) vs. grammar parsing (portability, but every format change must be handled by hand) — record which one produced each claim.
status: mined
limitation: Very young, 2-star project; its fidelity claims are unreviewed self-statements.
province-fit: in — static Dart AOT parsing without executing any VM
obscurity: obscure
```

```
ID-SLUG: phrack-dart-aot
source: Phrack #71 'Reversing Dart AOT snapshots' (cryptax), Volume 0x10 Issue 0x47 Phile 0x0B — https://phrack.org/issues/71/reversing-dart-aot-snapshots_md.html
kind: paper
tier: A
scope: The author's walkthrough of Dart AOT calling conventions (PP/THR registers, SMI tagging) and why disassemblers miss the Object Pool
anchor: §'5 - Snapshot serialization', Phrack issue 71, accessed 2026-10-29: "there is no random access in the snapshot, only sequential access."
teaches: Dart AOT pins dedicated registers (x86-64 PP=r15, THR=r14) and tags SMIs with LSB=0, so constants in disassembly must be halved/resolved through the pool before being cited.
status: mined
limitation: Offsets such as THR+0x38 are per-SDK-version and the article targets a specific toolchain era.
province-fit: in — static reading of Dart AOT machine code
obscurity: niche
```

```
ID-SLUG: hermes-dec
source: hermes-dec README — https://github.com/P1sec/hermes-dec/blob/2e796663e1fedb93dca51060797ebf3327b3fedb/README.md (release 0.1.8; commit 2e796663e1fe, 2026-10-15)
kind: tool
tier: A
scope: hermes-dec's own background notes on Hermes bytecode versions and React Native defaults, plus its file(1) identification example
anchor: README.md §'## Background' / usage example, commit 2e796663e1fedb93dca51060797ebf3327b3fedb, accessed 2026-10-29: "assets/index.android.bundle: Hermes JavaScript bytecode, version 84"
teaches: An index.android.bundle may be Hermes bytecode (versioned) or plain minified JS; identify which with magic/version before choosing a decompiler.
status: mined
limitation: Decompiled HBC is a reconstruction; the README notes its header-dump output 'may not be stable over time'.
province-fit: in — React Native HBC disassembly/decompilation
obscurity: niche
```

```
ID-SLUG: hermes-bytecode-file-format
source: Hermes BytecodeFileFormat.h — https://github.com/facebook/hermes/blob/72b0009fa7097c58c273566083fbc298082cbcdd/include/hermes/BCGen/HBC/BytecodeFileFormat.h (commit 72b0009fa709, 2026-10-28)
kind: spec
tier: A
scope: Meta's own HBC header/footer struct definitions and magic constants
anchor: BytecodeFileFormat.h line 29-34 (MAGIC/DELTA_MAGIC) and BytecodeFileFooter, commit 72b0009fa7097c58c273566083fbc298082cbcdd, accessed 2026-10-29: ""Hermes" in ancient Greek encoded in UTF-16BE and truncated to 8 bytes."
teaches: HBC files are byte-checkable: 8-byte MAGIC 0x1F1903C103BC1FC6 (or ~MAGIC for delta-prepped form), a version field, and a SHA-1 footer over all preceding bytes — a ready integrity oracle for HBC fixtures.
status: mined
limitation: The header at main reflects the current bytecode version; older HBC versions need the header at the matching Hermes tag.
province-fit: in — primary format source for Hermes artifacts
obscurity: niche
```

```
ID-SLUG: hermes-rs
source: hermes_rs README — https://github.com/Pilfer/hermes_rs/blob/c65ba858905411fa35a7d92ddd728ad2d71fa6e6/README.md (commit c65ba8589054, 2026-02-09)
kind: tool
tier: A
scope: hermes_rs's own supported-HBC-version table and known round-trip differences
anchor: README.md §'##### HBC File Size Differences', commit c65ba858905411fa35a7d92ddd728ad2d71fa6e6, accessed 2026-10-29: "The size of a binary produced with `hermes_rs` is going to be a bit larger than one compiled directly with hermes."
teaches: Reassembling bytecode is not byte-identical to the original compiler output (string-table merging differs), so 'round-trip equals original' is a forgeable claim unless hashes match.
status: mined
limitation: Disassembler/assembler only for HBC 76, 89, 90, 93–96; README table marks decompiler unsupported.
province-fit: in — HBC parsing library
obscurity: obscure
```

```
ID-SLUG: pyinstxtractor
source: PyInstaller Extractor README — https://github.com/extremecoders-re/pyinstxtractor/blob/815d31cf26bc71e62f851b2e549452e7b7c9dd98/README.md (release 2026.07; commit 815d31cf26bc, 2026-07-03)
kind: tool
tier: A
scope: pyinstxtractor's own supported PyInstaller version list and usage caveat
anchor: README.md §'## Usage', commit 815d31cf26bc71e62f851b2e549452e7b7c9dd98, accessed 2026-10-29: "It is recommended to run the script in the same version of Python which was used to generate the executable."
teaches: PyInstaller CArchive/PYZ extraction depends on the host Python's marshal format; record both the PyInstaller version detected and the extractor's Python version.
status: mined
limitation: Extraction yields .pyc, not source; header 'fixing' is a tool mutation that must be noted in provenance.
province-fit: in — static unpacking of frozen Python executables
obscurity: mainstream
```

```
ID-SLUG: pycdc
source: Decompyle++ (pycdc) README — https://github.com/zrax/pycdc/blob/b4289760970dbc399684f1e155ec6d1ea1cc787e/README.markdown (commit b4289760970d, 2026-04-07)
kind: tool
tier: A
scope: pycdc's own stated goal and its split into disassembler (pycdas) and decompiler (pycdc)
anchor: README.markdown top section, commit b4289760970dbc399684f1e155ec6d1ea1cc787e, accessed 2026-10-29: "Decompyle++ is unique in that it seeks to support byte-code from any version of Python."
teaches: Keep pycdas disassembly (observation) separate from pycdc source output (inference) in the ledger.
status: mined
limitation: 'Seeks to support' is an aim, not a coverage guarantee for any specific Python version.
province-fit: in — Python bytecode recovery
obscurity: mainstream
```

```
ID-SLUG: pylingual
source: PyLingual README — https://github.com/syssec-utd/pylingual/blob/11a1516d84a6c2aa71ec23fbd11e4b99dc8c4a86/README.md (release v0.1.0; commit 11a1516d84a6, 2026-10-19)
kind: tool
tier: A
scope: PyLingual's own description of its compile-and-compare correctness check across Python 3.6+
anchor: README.md §'### Decompiling End-Of-Life Python Versions', commit 11a1516d84a6c2aa71ec23fbd11e4b99dc8c4a86, accessed 2026-10-29: "To verify decompilation correctness and produce model training sets, PyLingual requires the ability to compile Python in the target version."
teaches: Decompiler output can be verified by recompiling with the target Python and comparing bytecode — a concrete byte-oracle pattern for decompilation claims.
status: mined
limitation: README warns the local codebase may have control-flow accuracy regressions vs. the hosted service; the web service sends code to a third party.
province-fit: in — verified Python decompilation
obscurity: niche
```

```
ID-SLUG: python-xdis
source: xdis README — https://github.com/rocky/python-xdis/blob/51e36c42a01a83d67f6530fdf7fbd42a0f387d86/README.rst (release 6.3.0; commit 51e36c42a01a, 2026-10-18)
kind: code
tier: A
scope: xdis's own statement of cross-version marshal loading and disassembly
anchor: README.rst §'Introduction', commit 51e36c42a01a83d67f6530fdf7fbd42a0f387d86, accessed 2026-10-29: "The Python dis_ module allows you to disassemble bytecode from the same version of Python that you are running on."
teaches: Stdlib dis is version-locked to the running interpreter; cross-version pyc observation needs a magic-number-aware loader such as xdis.
status: mined
limitation: Disassembly is not decompilation; xdis's own format claims are not independently validated here.
province-fit: in — Python bytecode observation layer
obscurity: niche
```

```
ID-SLUG: nuitka-extractor
source: Nuitka Extractor README — https://github.com/extremecoders-re/nuitka-extractor/blob/a0a50f9ac98ccfe50793a7b89b251eb977440bbb/README.md (release 2024.01.11; commit a0a50f9ac98c, 2026-01-18)
kind: tool
tier: A
scope: The tool's own statement of what can (and cannot) be pulled from Nuitka onefile executables
anchor: README.md top section, commit a0a50f9ac98ccfe50793a7b89b251eb977440bbb, accessed 2026-10-29: "A nuitka compiled executable doesn't contain pyc file."
teaches: Nuitka compiles Python to native code, so extraction yields only embedded DLLs/.so/assets; any 'recovered Python source' claim for a Nuitka binary is forged by construction.
status: mined
limitation: Onefile only; README notes signed PE executables are not yet supported.
province-fit: in — static unpacking; doubles as a forged-claim rejection control
obscurity: obscure
```

```
ID-SLUG: electron-asar
source: @electron/asar README — https://github.com/electron/asar/blob/fde819a77fea5f6ca4f5f774cc78e033c04efc9f/README.md (release v4.3.1; commit fde819a77fea, 2026-10-26)
kind: docs
tier: A
scope: Electron's own description of the ASAR archive format and CLI
anchor: README.md top section and §'## Features', commit fde819a77fea5f6ca4f5f774cc78e033c04efc9f, accessed 2026-10-29: "It concatenates all files together without compression"
teaches: ASAR is a JSON header + concatenated uncompressed payloads with random access, so file offsets/hashes inside app.asar are directly verifiable without execution.
status: mined
limitation: Says nothing about ASAR integrity fuses or app.asar.unpacked handling at runtime.
province-fit: in — Electron artifact container format
obscurity: mainstream
```

```
ID-SLUG: node-sea-docs
source: Node.js 'Single executable applications' docs — https://nodejs.org/api/single-executable-applications.html (doc version v26.13.0)
kind: docs
tier: A
scope: Node.js's own documentation of the SEA blob injection mechanism and configuration fields
anchor: §'Generating single executable applications with --build-sea', Node.js v26.13.0 docs, accessed 2026-10-29: "The version of the Node.js binary used to produce the blob must be the same as the one to which the blob will be injected."
teaches: SEA executables are a stock node binary plus an injected blob; the host node version is a matching constraint, and useSnapshot/useCodeCache mean the payload may be V8 data, not source.
status: mined
limitation: Docs describe the build side (Stability 1.1); they do not specify the injected blob's byte layout.
province-fit: in — primary source for Node SEA artifacts
obscurity: niche
```

```
ID-SLUG: bun-compile-docs
source: Bun 'Single-file executable' docs source — https://github.com/oven-sh/bun/blob/000ef503730334a388c47b1bd025851a76b4832e/docs/compiler/executables.mdx (commit 000ef5037303)
kind: docs
tier: A
scope: Bun's own documentation of --compile, --bytecode, embedded files (/$bunfs/) and Bun.embeddedFiles
anchor: executables.mdx §'### Bytecode compilation' (line 301), commit 000ef503730334a388c47b1bd025851a76b4832e, accessed 2026-10-29: "Bytecode compilation doesn't obscure source code."
teaches: Bun standalone binaries carry the bundled JS plus assets under an internal /$bunfs/ path; Bun itself states --bytecode is not an obfuscation layer.
status: mined
limitation: The public bun.com/docs/bundler/executables URL returned HTTP 404 this session; the repo file is the pinned source. Byte layout of the embedded table is not specified.
province-fit: in — primary source for Bun-compiled artifacts
obscurity: niche
```

```
ID-SLUG: pkg-unpacker
source: pkg-unpacker README — https://github.com/LockBlock-dev/pkg-unpacker/blob/f1db108bc6285a854680e7f24bb1ce77f7c3b747/README.md (commit f1db108bc628, 2026-10-14)
kind: tool
tier: A
scope: The tool's own per-format notes for pkg, nexe, caxa, Node SEA and Bun single-file binaries
anchor: README.md top note and §'## How it works', commit f1db108bc6285a854680e7f24bb1ce77f7c3b747, accessed 2026-10-29: "this tool doesn't give you the full source code if the application was compiled into bytecode"
teaches: Five JS single-binary packers store payloads differently (pkg trailer metadata, SEA blob, Bun /$bunfs/ table, nexe ZIP+sentinel, caxa tar+JSON footer); identify the packer before claiming source recovery.
status: mined
limitation: Its `--run` evaluation mode executes the target — out of province; use extraction only.
province-fit: in — static unpacking (execution mode excluded)
obscurity: obscure
```

```
ID-SLUG: denodig
source: Deno Dig README — https://github.com/theGEBIRGE/DenoDig/blob/46b864340c1e3bf638cd65cd2df27af90bb7ba47/README.md (release v1.3.0; commit 46b864340c1e, 2024-10-29)
kind: tool
tier: A
scope: The tool's own enumeration of four `deno compile` payload layouts by Deno version
anchor: README.md top list, commit 46b864340c1e3bf638cd65cd2df27af90bb7ba47, accessed 2026-10-29: "`>= 1.46`: [eszip](https://github.com/denoland/eszip) included in an object file section of the Deno binary"
teaches: deno compile payload location changed across versions (appended bundle → metadata+bundle → appended eszip → eszip in an object-file section), so locating it is itself a version fingerprint.
status: mined
limitation: Coverage stops at the layouts known in late 2024; newer Deno releases may differ.
province-fit: in — static extraction from Deno standalone binaries
obscurity: obscure
```

```
ID-SLUG: readytorun-format
source: ReadyToRun File Format (BOTR) — https://github.com/dotnet/runtime/blob/8ccc1569f5b5987ef17e54d769436aa7ecbd74ff/docs/design/coreclr/botr/readytorun-format.md (commit 8ccc1569f5b5, 2026-10-29)
kind: spec
tier: A
scope: The .NET runtime team's own R2R header, flags and section-type definitions
anchor: §'### READYTORUN_HEADER::Signature' (line 103), commit 8ccc1569f5b5987ef17e54d769436aa7ecbd74ff, accessed 2026-10-29: "Always set to 0x00525452 (ASCII encoding for RTR)."
teaches: R2R images are recognisable by signature 0x00525452 ('RTR') and carry both precompiled native code and IL/metadata, so managed decompilers still see IL while the native code is a separate, versioned layer.
status: mined
limitation: The doc's intro pins format 3.1 'as of June 2019' with later sections added; trust readytorun.h at the matching tag for current version numbers. Does not cover NativeAOT (no IL).
province-fit: in — primary format source for .NET R2R artifacts
obscurity: niche
```

```
ID-SLUG: de4dot
source: de4dot README — https://github.com/de4dot/de4dot/blob/b7d5728fc0c82fb0ad758e3a4c0fbb70368a4853/README.md (archived; last commit b7d5728fc0c8, 2020-08-29)
kind: tool
tier: A
scope: de4dot's own statement of what deobfuscation can and cannot restore
anchor: README.md §'Description', commit b7d5728fc0c82fb0ad758e3a4c0fbb70368a4853, accessed 2026-10-29: "symbol renaming is impossible to restore since the original names aren't (usually) part of the obfuscated assembly."
teaches: Obfuscator renaming is information-destroying: restored names are always inference, while decrypted strings/inlined methods can be checked against the assembly bytes.
status: mined
limitation: Archived since 2020; unmaintained against current obfuscators. Unpacking commercial protectors may conflict with licensing — case-by-case.
province-fit: adjacent — managed deobfuscation; protector-unpacking edges toward refused circumvention
obscurity: mainstream
```

```
ID-SLUG: cfr
source: CFR README — https://github.com/leibnitz27/cfr/blob/c4145259dfcd8ad3e99004e4d9ecb0aed55dcc5a/README.md (release 0.152; commit c4145259dfcd, 2026-06-04)
kind: tool
tier: A
scope: CFR's own statement of supported Java features and non-Java JVM input
anchor: README.md §'# CFR - Another Java Decompiler', commit c4145259dfcd8ad3e99004e4d9ecb0aed55dcc5a, accessed 2026-10-29: "It'll even make a decent go of turning class files from other JVM languages back into java!"
teaches: A second JVM decompiler with an independent codebase lets a ledger cross-check JADX output; disagreements mark inference hotspots.
status: mined
limitation: 'Decent go' at Kotlin/Scala classes is the author's hedge, not a fidelity claim.
province-fit: in — JVM bytecode decompilation
obscurity: mainstream
```

```
ID-SLUG: vineflower
source: Vineflower README — https://github.com/Vineflower/vineflower/blob/b8273988af850e8cfb234ca08d129058502b032f/README.md (release 1.12.0; commit b8273988af85, 2026-04-29)
kind: tool
tier: A
scope: Vineflower's own feature statement (Fernflower fork; Java 21+ constructs)
anchor: README.md top section, commit b8273988af850e8cfb234ca08d129058502b032f, accessed 2026-10-29: "Vineflower is a modern general purpose Java & JVM language decompiler focused on providing the best quality, speed, and usability."
teaches: A third, Fernflower-lineage JVM decompiler for triangulating decompiled Java/Kotlin claims.
status: mined
limitation: 'Best quality' is self-description; the linked output comparison is the project's own.
province-fit: in — JVM bytecode decompilation
obscurity: mainstream
```

```
ID-SLUG: luajit-decompiler-v2
source: LuaJIT Decompiler v2 README — https://github.com/marsinator358/luajit-decompiler-v2/blob/6a8a0cec48fdf175dddaca5d3fbfe3aa59b5550a/README.md (release Mar_24_2024; commit 6a8a0cec48fd, 2026-05-14)
kind: tool
tier: A
scope: The tool's own claims about stripped-bytecode handling and its cited algorithm paper
anchor: README.md §'## LuaJIT Decompiler v2', commit 6a8a0cec48fdf175dddaca5d3fbfe3aa59b5550a, accessed 2026-10-29: "full support for gotos and stripped bytecode including locals and upvalues."
teaches: LuaJIT bytecode (distinct from PUC-Lua luac) has its own decompiler; names for stripped locals/upvalues are necessarily synthesized, so treat them as inference.
status: mined
limitation: README TODO lists no big-endian bytecode support.
province-fit: in — LuaJIT bytecode recovery (games/embedded)
obscurity: obscure
```

```
ID-SLUG: wabt
source: WABT README — https://github.com/WebAssembly/wabt/blob/ed1a832d9553158a2a67bf6c6d98a96207a4ee6b/README.md (release 1.0.42; commit ed1a832d9553, 2026-10-28)
kind: tool
tier: A
scope: The WebAssembly CG toolkit's own list of tools (wasm2wat, wasm-objdump, wasm2c, wasm-decompile, wasm-validate)
anchor: README.md tool list (line 12, wasm2c), commit ed1a832d9553158a2a67bf6c6d98a96207a4ee6b, accessed 2026-10-29: "convert a WebAssembly binary file to a C source and header"
teaches: wasm2wat is a near-lossless observation of a module; wasm2c/wasm-decompile outputs are derived views and must be ledgered as such.
status: mined
limitation: The README is a tool index; it does not establish decompiled-output fidelity.
province-fit: in — WASM artifact inspection
obscurity: mainstream
```

```
ID-SLUG: google-smali
source: smali/baksmali (Google fork) README — https://github.com/google/smali/blob/1a36aa30d18d92e63994f4b1e67a055931f5a707/README.md (release 3.0.6; commit 1a36aa30d18d, 2026-08-25)
kind: tool
tier: A
scope: Google's statement that it maintains the smali fork and the renamed Maven coordinates
anchor: README.md §'### About', commit 1a36aa30d18d92e63994f4b1e67a055931f5a707, accessed 2026-10-29: "This is a fork of https://github.com/JesusFreke/smali for patches needed by Google as the original repository is currently not maintained."
teaches: Cite the maintained fork (com.android.tools.smali) and version for baksmali output; the original JesusFreke repo is archived.
status: mined
limitation: Assembler/disassembler fidelity for new dex versions is not asserted by the README.
province-fit: in — DEX disassembly/reassembly
obscurity: mainstream
```

```
ID-SLUG: r8-retrace-mapping-versioning
source: R8 'Retrace and map file versioning' — https://r8.googlesource.com/r8/+/refs/tags/8.3.37/doc/retrace.md (tag 8.3.37)
kind: spec
tier: A
scope: R8's own specification of versioned JSON-comment metadata in ProGuard/R8 mapping files
anchor: doc/retrace.md intro and §'### Version', tag 8.3.37, accessed 2026-10-29: "Programs compiled by R8 are not structurally the same as the input."
teaches: Mapping files are versioned via '# {"id":"com.android.tools.r8.mapping","version":…}' comments and mark synthesized/outlined members, so a deobfuscated name is only an observation when a matching mapping file is in evidence.
status: mined
limitation: Shipped APKs normally lack mapping files; this spec does not enable name recovery without one.
province-fit: in — Android obfuscation-mapping semantics
obscurity: obscure
```

```
ID-SLUG: unrpyc
source: unrpyc README — https://github.com/CensoredUsername/unrpyc/blob/3ae8334ed71a05535927dcc559663d3aca51215b/README.md (release v2.0.4; commit 3ae8334ed71a, 2026-02-23)
kind: tool
tier: A
scope: unrpyc's own scope: decompiling Ren'Py .rpyc, explicitly not unpacking .rpa
anchor: README.md top section, commit 3ae8334ed71a05535927dcc559663d3aca51215b, accessed 2026-10-29: "It will not extract files from .rpa archives."
teaches: Engine-specific script formats split container extraction (.rpa) from script decompilation (.rpyc); ledger each stage with its own tool.
status: mined
limitation: Ren'Py version compatibility is per-branch (py2 legacy vs py3); not validated here.
province-fit: in — game-engine script artifact recovery
obscurity: obscure
```

```
ID-SLUG: gdsdecomp
source: Godot RE Tools (gdsdecomp) README — https://github.com/GDRETools/gdsdecomp/blob/e2780fcc73ab14083967d3945e513d1f6af1dbd0/README.md (release v2.7.4; commit e2780fcc73ab, 2026-10-14)
kind: tool
tier: A
scope: GDRE Tools' own feature list for PCK extraction, GDScript decompilation and resource conversion
anchor: README.md §'## Introduction', commit e2780fcc73ab14083967d3945e513d1f6af1dbd0, accessed 2026-10-29: "Converts any auto-converted binary resources back to their original text formats"
teaches: 'Full project recovery' includes format conversions back to text, so recovered .tscn/.tres are regenerated artifacts, not original bytes.
status: mined
limitation: Encrypted PCKs need the key; this row does not cover key extraction.
province-fit: in — Godot artifact recovery
obscurity: niche
```

```
ID-SLUG: innoextract
source: innoextract README — https://github.com/dscharrer/innoextract/blob/6e9e34ed0876014fdb46e684103ef8c3605e382e/README.md (release 1.9; commit 6e9e34ed0876, 2025-02-06)
kind: tool
tier: A
scope: innoextract's own supported Inno Setup version range and variants
anchor: README.md top section, commit 6e9e34ed0876014fdb46e684103ef8c3605e382e, accessed 2026-10-29: "innoextract allows to extract such installers under non-Windows systems without running the actual installer using wine."
teaches: Installer payloads can be unpacked statically without executing the installer (supports Inno Setup 1.2.10–6.3.3 per README).
status: mined
limitation: Newer Inno Setup releases after 6.3.3 may not parse; README version is the bound.
province-fit: in — static installer/archive unpacking
obscurity: niche
```

```
ID-SLUG: autoit-ripper
source: AutoIt-Ripper README — https://github.com/nazywam/AutoIt-Ripper/blob/d60d449dd779d4f604716c839a16521444ed3b11/README.md (release v1.2.0; commit d60d449dd779, 2026-03-07)
kind: tool
tier: A
scope: The tool's own supported AutoIt/AutoHotKey script-resource versions (EA05, EA06, JB01) and lineage
anchor: README.md §'## What is this', commit d60d449dd779d4f604716c839a16521444ed3b11, accessed 2026-10-29: "This is a short python script that allows for extraction of "compiled" AutoIt scripts from PE executables."
teaches: AutoIt 'compiled' executables embed script resources tagged by version markers (EA05/EA06/JB01), so extraction is container-parsing, not decompilation.
status: mined
limitation: Lineage cites ClamAV/myaut sources; marker-to-version mapping is the README's claim.
province-fit: in — static script extraction from PE wrappers
obscurity: obscure
```

## Screened and dropped
- https://github.com/goretk/redress — redress README opened (commit fe38d961b5d8, 2024-10-12); overlaps GoReSym, stale since 2024; kept GoReSym + stdlib sources instead.
- https://github.com/0xjiayu/go_parser — IDA-only Go parser (commit e90ad706f958, 2024-01); README not mined; superseded by GoReSym/stdlib anchors.
- https://github.com/rscloura/Doldrums — README scopes to "all Dart version 2.10 releases", stale since 2022; darter row carries the same version-lock lesson.
- https://github.com/Impact-I/reFlutter — fetched; works by patching the Flutter engine and repackaging for traffic interception (runtime/live-target posture) → out of province.
- https://github.com/bongtrop/hbctool — README opened; stale (2023-04) and limited to old HBC versions; hermes-dec / hermes_rs kept.
- https://github.com/rocky/python-decompile3 — description limits it to Python 3.7–3.8; pycdc/pylingual kept.
- https://github.com/mstrobel/procyon — last commit 2022-02; CFR/Vineflower kept.
- https://github.com/JesusFreke/smali — archived; Google fork kept.
- https://github.com/pxb1988/dex2jar — opened; upstream stale since 2023 (fork ThexXTURBOXx/dex2jar active, README not mined); JADX already in corpus.
- https://github.com/WebAssembly/binaryen — optimizer/toolchain, not a recovery source; wabt kept.
- https://github.com/MichalStrehovsky/sizoscope — needs .mstat files emitted at build time, not present in shipped NativeAOT binaries → not artifact-first.
- https://github.com/denoland/eszip — README says the Rust crate moved into denoland/deno; repo is only JS/Wasm bindings → weak primary for format.
- https://sourceforge.net/projects/unluac/ — main page returned HTTP 403 via curl; read only reached the RSS feed of jar uploads (latest /Unstable/unluac_2025_12_23.jar) — not enough to quote scope. Flip: fetch the project summary page successfully.
- https://www.computer.org/csdl/proceedings-article/sp/2025/223600a052/21B7QZB86cg — PyLingual IEEE S&P 2025 page rendered empty (JS app); flip: fetch via IEEE Xplore/DOI abstract.
- https://bun.com/docs/bundler/executables — HTTP 404 this session; used the pinned repo mdx instead.
- https://developer.android.com/tools/retrace — opened (last updated 2026-03-05); CLI usage only, the R8 googlesource versioning spec is the stronger primary.
- https://github.com/UnderminersTeam/UndertaleModTool, https://github.com/Col-E/Recaf, https://github.com/nesrak1/AssetsTools.NET, https://github.com/Washi1337/AsmResolver, https://github.com/lifting-bits/rellic — metadata fetched, READMEs not mined; modding/editing libraries or LLVM-lifting rather than artifact-recovery anchors for this slice.
- Leads surfaced by search but not opened: mildsunrise-adjacent DarkLineX/unpackFlutter (archived 2023), BroNils/aotopsy, ejfkdev/dae, caverav/flutterdec, IR0NBYTE/Jadart, xv4l3x/hermit, 1-3-7/disrobe, recipes.tst.sh 'Anatomy of a snapshot', belz.news Deno extraction post, gebir.ge DenoDig article, cloud.google.com 'Golang internals symbol recovery' blog (vendor blog; GoReSym README links it).

## Search log
- web_search (6 queries): "Dart AOT snapshot object pool recovery tool github obscure"; "Hermes bytecode Ghidra processor module github hbc"; "deno compile binary extract eszip source github tool"; ".NET ReadyToRun format design doc dotnet runtime botr readytorun-format.md"; "Go 1.2 runtime symbol table design document pclntab golang.org/s/go12symtab"; "unluac Lua decompiler sourceforge"; plus 2 follow-ups: Bun --compile docs URL; "R8 mapping file format specification com.android.tools.r8.mapping".
- GitHub API (gh, authenticated): repo metadata + HEAD commit + latest release + README for 51 repos (42 seed + 9 from search).
- Direct fetches: golang/go src/internal/abi/symtab.go and src/debug/gosym/pclntab.go @430d19f07a57; dotnet/runtime readytorun-format.md @8ccc1569f5b5; facebook/hermes BytecodeFileFormat.h @72b0009fa709; r2flutter doc/objpool.md @441d614937c8; oven-sh/bun docs/compiler/executables.mdx @000ef5037303; Phrack #71 article; Node.js SEA docs v26.13.0; R8 doc/retrace.md @8.3.37; developer.android.com/tools/retrace.
- Every quote above was machine-checked as a verbatim (whitespace-normalised) substring of the fetched raw page/file.
- Counts: identified ~75 candidates (seed list + search results); screened 60 (opened/metadata-fetched); kept 39 rows; dropped 22 listed above (some grouped).
- Obscure picks via web_search: r2flutter (+objpool.md), unflutter, darter, hermes_rs, DenoDig, Phrack Dart AOT, R8 map-file versioning spec; also obscure from seed expansion: rustbininfo, nuitka-extractor, pkg-unpacker, AutoIt-Ripper, unrpyc, luajit-decompiler-v2.
- Installs: none (no tools installed or run; nothing under /home/vgpnk/Projects touched).
