# ReEmulationBehavior — emulation, symbolic execution, behavior/capability ID, triage, diffing, DBI

Slice owner: REVENGER_SHOKUNIN.ReEmulationBehavior · accessed 2026-10-29 · all quotes machine-checked as verbatim substrings (whitespace-normalized) of the fetched README/doc at the pinned commit, or of the fetched web page.
Pins: GitHub rows pin the default-branch commit fetched via GitHub API on 2026-10-29 plus the latest release tag; README text was read at that commit (`repos/<r>/readme?ref=<sha>`).
Installs: none. No tool was installed or run.

ID-SLUG: capa-readme
source: mandiant/capa README — https://github.com/mandiant/capa/tree/2bdf7a4788ffe8696d3eabf7f746ca682eba294b
kind: tool
tier: A
scope: capa's own README statement of what it reports and on which input types, at the pinned commit
anchor: README.md intro; commit 2bdf7a4788ff (master), latest release v10.0.0 (2026-10-16); accessed 2026-10-29; "capa detects capabilities in executable files."
teaches: capa output is a rule-match claim ('it tells you what it thinks the program can do'), so each capability line belongs in the ledger as an inference tied to a rule name + match address, not as an observation.
status: mined
limitation: Do not conclude a capability is present at runtime; matches are rule hits over extracted features.
province-fit: in — static capability ID over PE/ELF/.NET/shellcode
obscurity: mainstream

ID-SLUG: capa-limitations
source: capa doc/limitations.md — https://github.com/mandiant/capa/blob/2bdf7a4788ffe8696d3eabf7f746ca682eba294b/doc/limitations.md
kind: docs
tier: A
scope: capa's own documented blind spots (packers, installers, wrapper functions, loops) at the pinned commit
anchor: doc/limitations.md § Wrapper functions and matches in child functions; commit 2bdf7a4788ff (master), latest release v10.0.0 (2026-10-16); accessed 2026-10-29; "Currently capa does not handle wrapper functions or other matches in child functions."
teaches: A capa 'no match' is not negative evidence: behavior split across a wrapper and its caller is invisible, so absence must be recorded as unknown.
status: mined
limitation: Do not treat the list as exhaustive of capa's failure modes.
province-fit: in — limits of a static capability identifier
obscurity: niche

ID-SLUG: capa-rules-format
source: capa-rules doc/format.md — https://github.com/mandiant/capa-rules/blob/21332a057f5be39fa145bc4aea7ae2431ff05fc3/doc/format.md
kind: spec
tier: A
scope: the capa rule YAML schema, scope semantics (static/dynamic) and example-offset requirement at the pinned commit
anchor: doc/format.md § rule metadata → examples; commit 21332a057f5b (master), latest release v10.0.0 (2026-10-16); accessed 2026-10-29; "`function` and `basic block` scope rules must contain offsets to the respective match locations using the format `<sample name>:<function or basic block offset>`."
teaches: Rule examples pin a hash plus a function/basic-block offset, which is exactly the shape of a byte-oracle fixture an evidence ledger can re-check.
status: mined
limitation: Do not conclude every published rule's examples still match current capa versions; that requires running the rule tests.
province-fit: in — machine-checkable behavior-rule format
obscurity: niche

ID-SLUG: capa-testfiles
source: mandiant/capa-testfiles README — https://github.com/mandiant/capa-testfiles/tree/4fa9a0448a1453a80bdcbcefb6dff870f6333b64
kind: dataset
tier: A
scope: naming/permission conventions of capa's test-binary corpus at the pinned commit
anchor: README.md § File permissions; commit 4fa9a0448a14 (master), no GitHub release; accessed 2026-10-29; "All files in this repository must be tracked in Git with non-executable permissions (`100644`)."
teaches: Fixture corpora of hostile samples are named by MD5/SHA256 with neutered extensions (.exe_, .raw32) and non-exec mode; a ledger fixture store can copy that convention.
status: mined
limitation: Do not conclude the corpus is safe to execute or redistribute; it contains real malware test data.
province-fit: in — fixture-corpus hygiene for static analysis
obscurity: obscure

ID-SLUG: floss
source: mandiant/flare-floss README — https://github.com/mandiant/flare-floss/tree/3f21c8a28f816e764831ff9787e95820e904273e
kind: tool
tier: A
scope: FLOSS's own README description of string classes it extracts (static, stack, tight, decoded, language-specific) at the pinned commit
anchor: README.md § Language-specific strings; commit 3f21c8a28f81 (master), latest release v3.2.0 (2026-10-16); accessed 2026-10-29; "Not all compilers use string formats that the classic `strings.exe` algorithm supports."
teaches: strings(1) output is an incomplete observation: Go/Rust strings without NUL terminators and stack/decoded strings need separate extractors, each recorded with its method.
status: mined
limitation: Do not conclude decoded strings are complete; emulation-based decoding only covers functions FLOSS identifies as decoders.
province-fit: in — static+emulated string recovery
obscurity: mainstream

ID-SLUG: speakeasy-limitations
source: Speakeasy doc/limitations.md — https://github.com/mandiant/speakeasy/blob/bae336c7aa1d1e73ad0bb701374345a41ff2fe48/doc/limitations.md
kind: docs
tier: A
scope: Speakeasy's own statement of how unimplemented Windows APIs are handled and reported, at the pinned commit (latest tag v1.6.1)
anchor: doc/limitations.md § Documented APIs without a handler; commit bae336c7aa1d (master), latest release v1.6.1 (2025-02-19); accessed 2026-10-29; "treat calls in the trace that have parameter names (`name: value`) as unimplemented stubs when interpreting a report."
teaches: An emulator trace mixes modeled and stubbed API results; the report format itself marks which is which, and a ledger must carry that distinction instead of flattening it to 'the sample did X'.
status: mined
limitation: Do not conclude real-OS behavior from a Speakeasy report; environment drift can look like anti-analysis.
province-fit: adjacent — emulation executes sample code, but in a modeled userland without a live target
obscurity: niche

ID-SLUG: goresym
source: mandiant/GoReSym README — https://github.com/mandiant/GoReSym/tree/722897e0a80da0a06c00c5e40591a253a551f04e
kind: tool
tier: A
scope: GoReSym's README description of recovered Go metadata and its version-override caveat at the pinned commit
anchor: README.md § Usage, `-v` flag; commit 722897e0a80d (master), latest release v3.4.1 (2026-09-14); accessed 2026-10-29; "Type parsing will fail if the version is not accurate."
teaches: Go pclntab/moduledata recovery is version-keyed; the inferred Go version is a load-bearing inference that must be ledgered before trusting recovered types.
status: mined
limitation: Do not conclude recovered function names are authentic in deliberately tampered binaries.
province-fit: in — static Go symbol recovery
obscurity: niche

ID-SLUG: qiling
source: qilingframework/qiling README — https://github.com/qilingframework/qiling/tree/86c927cb329993b14e2586e04d1dd7a90deee5fb
kind: tool
tier: A
scope: Qiling's own feature list (OS/arch/format coverage, hooks, snapshots) at the pinned commit
anchor: README.md intro feature list; commit 86c927cb3299 (master), latest release v1.4.11 (2026-09-06); accessed 2026-10-29; "Emulate multi-platforms: Windows, macOS, Linux, Android, BSD, UEFI, DOS, MBR."
teaches: OS-level emulation sits above a CPU emulator (Unicorn); a ledger entry from Qiling should name the emulated OS profile and rootfs, since syscall results are modeled.
status: mined
limitation: Do not conclude every listed platform is equally complete; the README lists targets, not fidelity.
province-fit: adjacent — executes artifact code under emulation
obscurity: mainstream

ID-SLUG: unicorn
source: unicorn-engine/unicorn README — https://github.com/unicorn-engine/unicorn/tree/7c5db94191defc1e04a4f66f4eb1220903cba837
kind: tool
tier: A
scope: Unicorn's README self-description and architecture list at the pinned commit
anchor: README.md intro; commit 7c5db94191de (master), latest release 2.1.4 (2025-09-09); accessed 2026-10-29; "Unicorn is a lightweight, multi-platform, multi-architecture CPU emulator framework, based on"
teaches: Unicorn emulates CPU only (no OS); anything an emulated snippet 'does' beyond registers/memory is the harness's model, which the ledger must record as such.
status: mined
limitation: Do not conclude QEMU-derived semantics are bit-exact for every instruction/extension.
province-fit: adjacent — CPU-only emulation of extracted code
obscurity: mainstream

ID-SLUG: capstone
source: capstone-engine/capstone README — https://github.com/capstone-engine/capstone/tree/8b95af3e9441051e080f6ae32a624e5d435b944f
kind: tool
tier: A
scope: Capstone's README feature claims on branch `next` at the pinned commit (latest tag 6.0.0-Alpha11)
anchor: README.md feature list; commit 8b95af3e9441 (next), latest release 6.0.0-Alpha11 (2026-09-21); accessed 2026-10-29; "Provide details on disassembled instruction (called “decomposer” by others)."
teaches: Disassembler detail (operands, implicit regs, groups) is the citable unit; recording engine + version alongside each decoded instruction keeps the observation reproducible.
status: mined
limitation: Do not conclude the alpha-6 API/semantics match stable 5.x output.
province-fit: in — static disassembly
obscurity: mainstream

ID-SLUG: keystone
source: keystone-engine/keystone README — https://github.com/keystone-engine/keystone/tree/0d9567f08c0c23e8f604b2cad3d49450c93cfb40
kind: tool
tier: A
scope: Keystone's README description; last tagged release 0.9.2 (2020-06-21), commit pinned
anchor: README.md intro; commit 0d9567f08c0c (master), latest release 0.9.2 (2020-06-21); accessed 2026-10-29; "Keystone is based on LLVM, but it goes much further with"
teaches: An assembler is the inverse oracle for disassembly claims: re-assembling a recorded instruction and byte-comparing is a cheap check.
status: mined
limitation: Do not conclude active maintenance; the last release is from 2020.
province-fit: in — byte-level round-trip checks
obscurity: mainstream

ID-SLUG: triton
source: JonathanSalwan/Triton README — https://github.com/JonathanSalwan/Triton/tree/bc84cf745e99768e07d51dcd734eba35c59f1b3e
kind: tool
tier: A
scope: Triton's README feature list and reliability disclaimer at the pinned commit (last tag v0.9, 2022)
anchor: README.md intro; commit bc84cf745e99 (master), latest release v0.9 (2022-02-09); accessed 2026-10-29; "if it is not fully reliable."
teaches: Symbolic/taint results from a self-declared part-time library are inferences whose solver + lifter version must be recorded; the author's own disclaimer is a calibration signal.
status: mined
limitation: Do not conclude SMT-simplified expressions equal the original semantics without concrete re-check.
province-fit: in — symbolic execution / taint on lifted semantics
obscurity: niche

ID-SLUG: miasm
source: cea-sec/miasm README — https://github.com/cea-sec/miasm/tree/0b08574babbf058ac0d516e9520593024809f023
kind: tool
tier: A
scope: Miasm's README feature list at the pinned commit (last tag v0.1.3, 2019)
anchor: README.md § What is Miasm?; commit 0b08574babbf (master), latest release v0.1.3 (2019-12-12); accessed 2026-10-29; "Expression simplification for automatic de-obfuscation"
teaches: IR-based simplification gives a second, independent lifter to cross-check another tool's reading of the same bytes.
status: mined
limitation: Do not conclude tag v0.1.3 reflects current behavior; development continues on master.
province-fit: in — IR, emulation, deobfuscation
obscurity: niche

ID-SLUG: binref
source: binref/refinery README — https://github.com/binref/refinery/tree/a3db260604490f2ade35ce978bda1c36acc0092e
kind: tool
tier: A
scope: Binary Refinery's README design statement at the pinned commit (no GitHub releases; PyPI package)
anchor: README.md intro; commit a3db26060449 (master), no GitHub release; accessed 2026-10-29; "The scripts are designed to exclusively read input from stdin and write output to stdout."
teaches: Composable stdin→stdout units make each transformation step a hashable, replayable ledger entry (input hash → unit+args → output hash).
status: mined
limitation: Do not conclude any unit's decoding is correct without a byte-oracle on known plaintext.
province-fit: in — static triage transforms
obscurity: niche

ID-SLUG: die-heur
source: horsicq/Detect-It-Easy README — https://github.com/horsicq/Detect-It-Easy/tree/241819515e6becd17d036fe2d9dadfb13fff9999
kind: tool
tier: A
scope: DiE README statement of how heuristic results are separated from signature matches, at the pinned commit
anchor: README.md § Heuristic results stay visible; commit 241819515e6b (master), no GitHub release; accessed 2026-10-29; "Every result produced by the heuristic layer is kept separate and marked with `(Heur)`"
teaches: A file identifier that labels exact-rule vs inferred results maps directly onto observation vs inference columns.
status: mined
limitation: Do not conclude a clean DiE report means a clean file; the README says so itself.
province-fit: in — static file/packer identification
obscurity: mainstream

ID-SLUG: yara-maint
source: VirusTotal/yara README — https://github.com/VirusTotal/yara/tree/6d47342e825e59f5d8f20874d0778332bcec83a6
kind: tool
tier: A
scope: YARA repo's status banner at the pinned commit (release v4.6.0, 2026-10-27)
anchor: README.md top banner; commit 6d47342e825e (master), latest release v4.6.0 (2026-10-27); accessed 2026-10-29; "This project is in maintenance mode."
teaches: Rule-engine choice is a ledger field: YARA 4.x is maintenance-only, so new rule work should name the engine (YARA vs YARA-X) used to produce a match.
status: mined
limitation: Do not conclude YARA rules stop working; only development status is stated.
province-fit: in — static pattern matching
obscurity: mainstream

ID-SLUG: yara-x
source: VirusTotal/yara-x README — https://github.com/VirusTotal/yara-x/tree/9e89546f509f098cdef1736deeeb7a1df3e4859c
kind: tool
tier: A
scope: YARA-X README goal statement at the pinned commit (release v1.22.1, 2026-10-26)
anchor: README.md § YARA-X; commit 9e89546f509f (main), latest release v1.22.1 (2026-10-26); accessed 2026-10-29; "The ultimate goal of YARA-X is replacing YARA as the default"
teaches: A match claim needs engine + version: YARA-X is a rewrite, so identical rule text can behave differently across engines.
status: mined
limitation: Do not conclude full rule compatibility with YARA 4.x.
province-fit: in — static pattern matching
obscurity: mainstream

ID-SLUG: lief
source: lief-project/LIEF README — https://github.com/lief-project/LIEF/tree/86a95f1d8cce71e3458641d1a8612116f9d98864
kind: tool
tier: A
scope: LIEF README feature claims (parse/modify/abstract ELF, PE, MachO, COFF, OAT, DEX…) at the pinned commit (release 1.0.0)
anchor: README.md § About → Main features; commit 86a95f1d8cce (main), latest release 1.0.0 (2026-07-12); accessed 2026-10-29; "LIEF can be used to modify some parts of these formats"
teaches: A parser that also rewrites binaries needs its parse output cross-checked against a second parser before a header field is ledgered as observed.
status: mined
limitation: Do not conclude LIEF's abstraction preserves format-specific quirks.
province-fit: in — format parsing
obscurity: mainstream

ID-SLUG: bindiff
source: google/bindiff README — https://github.com/google/bindiff/tree/13c437afa0740bd704cf396e3de3eb8d1a471ead
kind: tool
tier: A
scope: BinDiff README use cases at the pinned commit (release v8)
anchor: README.md § About BinDiff; commit 13c437afa074 (main), latest release v8 (2023-09-25); accessed 2026-10-29; "It can also be used to port symbols and comments"
teaches: Porting names across versions turns a prior analysis into evidence for a new build only via a recorded match confidence/similarity per function.
status: mined
limitation: Do not conclude a ported symbol is correct without the match's similarity/confidence.
province-fit: in — static binary diffing
obscurity: mainstream

ID-SLUG: binexport
source: google/binexport README — https://github.com/google/binexport/tree/9648cacb21a71aa6c21b3fca504f146c39164a53
kind: tool
tier: A
scope: BinExport README role statement at the pinned commit
anchor: README.md § Introduction; commit 9648cacb21a7 (main), latest release v12-20240417-ghidra_11.0.3 (2024-04-17); accessed 2026-10-29; "data into the Protocol Buffer format that BinDiff requires."
teaches: Diff results depend on the exporting disassembler (IDA/Binja/Ghidra); the exporter is part of the evidence chain.
status: mined
limitation: Do not conclude exports from different disassemblers are equivalent.
province-fit: in — disassembly export for diffing
obscurity: niche

ID-SLUG: diaphora
source: joxeankoret/diaphora README — https://github.com/joxeankoret/diaphora/tree/35c7657081836d18e9983571be153e954d86cbb4
kind: tool
tier: A
scope: Diaphora README version/support statement at the pinned commit (release 3.5.0)
anchor: README.md intro; commit 35c765708183 (master), latest release 3.5.0 (2026-10-25); accessed 2026-10-29; "Diaphora supports versions of IDA >= 7.4 because the code only runs in Python 3.X"
teaches: Diffing results carry a host-tool dependency (IDA version, Python version) that should be recorded with the diff.
status: mined
limitation: Do not conclude matching heuristics are documented in full in the README.
province-fit: in — static binary diffing
obscurity: niche

ID-SLUG: ghidriff
source: clearbluejar/ghidriff README — https://github.com/clearbluejar/ghidriff/tree/4f5d895fcbb1eacd65efd81145922c15bb7e741d
kind: tool
tier: A
scope: ghidriff README output-format statement at the pinned commit (release v1.0.0)
anchor: README.md intro; commit 4f5d895fcbb1 (main), latest release v1.0.0 (2025-07-04); accessed 2026-10-29; "The diffing results are stored in JSON and rendered in markdown (optionally side-by-side HTML)."
teaches: JSON diff output can be stored as a ledger artifact and re-hashed; the markdown is a rendering, not the evidence.
status: mined
limitation: Do not conclude diff completeness when Ghidra analysis options (logged as warnings) were changed.
province-fit: in — headless patch diffing
obscurity: niche

ID-SLUG: objdiff
source: encounter/objdiff README — https://github.com/encounter/objdiff/tree/9aeec9cbab1a056ade7dc1f1625aacc41b0f8511
kind: tool
tier: A
scope: objdiff README feature list at the pinned commit (release v3.8.3)
anchor: README.md feature list; commit 9aeec9cbab1a (main), latest release v3.8.3 (2026-10-19); accessed 2026-10-29; "Compare entire object files: functions and data"
teaches: Matching-decompilation projects use byte-identical object diffing as a ground-truth oracle; the same per-function match % is a strong fixture for decompiler-output claims.
status: mined
limitation: Do not conclude support for arbitrary desktop toolchains; the target list is console-oriented.
province-fit: adjacent — byte-oracle diffing of rebuilt objects
obscurity: obscure

ID-SLUG: rr-site
source: rr: lightweight recording & deterministic debugging — https://rr-project.org/
kind: tool
tier: A
scope: rr project page claims about replay determinism and limitations (page last-updated banner 'Fri Oct 18'; release 5.10.0)
anchor: rr-project.org § rr in context / background; accessed 2026-10-29; "rr replay guarantees that execution preserves instruction-level control flow and memory and register contents."
teaches: A recorded trace is a durable, replayable evidence object; claims about a run can cite the trace instead of a nondeterministic re-run.
status: mined
limitation: Do not conclude rr fits shipped-artifact RE: it records live processes, needs syscall support and a supported CPU.
province-fit: adjacent — dynamic recording, own builds only
obscurity: mainstream

ID-SLUG: rr-paper
source: Engineering Record And Replay For Deployability: Extended Technical Report — https://arxiv.org/abs/1705.05937v1
kind: paper
tier: A
scope: the rr design paper abstract, arXiv 1705.05937v1 (2017-05-16)
anchor: Abstract; accessed 2026-10-29; "if the CPU and operating system meet certain non-obvious constraints."
teaches: Record/replay fidelity is conditional on hardware/OS properties; the conditions are themselves facts to ledger.
status: mined
limitation: Do not quote performance figures from the body; only the abstract was opened.
province-fit: adjacent — dynamic-analysis background
obscurity: niche

ID-SLUG: pernosco
source: Pernosco — Overview — https://pernos.co/about/overview/
kind: docs
tier: A
scope: Pernosco's own overview page claims and caveats (no revision shown)
anchor: /about/overview § Caveats and restrictions; accessed 2026-10-29; "Pernosco currently targets C, C++, Rust, Ada, and V8 JS (e.g. node.js) applications that run on x86-64 Linux and work with"
teaches: Omniscient debugging reframes debugging 'as a data analysis problem' over a full trace; the same query-over-trace idea fits an evidence ledger.
status: mined
limitation: Do not conclude on-prem availability or pricing; recordings are uploaded unless on-prem.
province-fit: adjacent — trace analysis of own programs
obscurity: niche

ID-SLUG: qbdi
source: QBDI/QBDI README — https://github.com/QBDI/QBDI/tree/3318580550215a0c7a64e9c2476e02eb5fc55f14
kind: tool
tier: A
scope: QBDI README intro at the pinned commit on dev-next (release v0.12.1)
anchor: README.rst § Introduction; commit 331858055021 (dev-next), latest release v0.12.1 (2026-01-07); accessed 2026-10-29; "QBDI modularity means it doesn't contain a preferred injection method"
teaches: DBI results depend on how instrumentation was injected (Frida, LD_PRELOAD, own loader); record the injection path.
status: mined
limitation: Do not conclude listed OS/arch support is uniform across them.
province-fit: adjacent — dynamic instrumentation of running code
obscurity: niche

ID-SLUG: dynamorio
source: DynamoRIO/dynamorio README — https://github.com/DynamoRIO/dynamorio/tree/10972089fb56c057c44f67272655be86a306e04a
kind: tool
tier: A
scope: DynamoRIO README self-description at the pinned commit (cron build tag cronbuild-11.91.20749)
anchor: README.md § About DynamoRIO; commit 10972089fb56 (master), latest release cronbuild-11.91.20749 (2026-10-24); accessed 2026-10-29; "DynamoRIO is a runtime code manipulation system that supports code"
teaches: DBI frameworks rewrite the code they observe; a trace from DBI is an observation of the instrumented process.
status: mined
limitation: Do not conclude macOS support; the README says it is in progress.
province-fit: adjacent — dynamic instrumentation
obscurity: mainstream

ID-SLUG: bnil
source: Binary Ninja Intermediate Language: Overview — https://docs.binary.ninja/dev/bnil-overview.html
kind: docs
tier: A
scope: Binary Ninja docs' definition of the BNIL stack (Lifted IL → LLIL → MLIL → HLIL, SSA forms); page unversioned, current stable 6.0.10905
anchor: Developer Guide → Binary Ninja Intermediate Language: Overview § Summary; accessed 2026-10-29; "Lifted IL is intended to be a straight-forward translation from native instruction semantics to LLIL instructions."
teaches: Each IL level adds analysis (flag folding, variables, types, dead-code removal); a claim should cite the lowest IL level that supports it.
status: mined
limitation: Do not conclude HLIL output is equivalent to source; it is post-simplification.
province-fit: in — decompiler IR semantics
obscurity: mainstream

ID-SLUG: binja-debuginfo
source: Debug Info — Binary Ninja User Documentation — https://docs.binary.ninja/guide/types/debuginfo.html
kind: docs
tier: A
scope: Binary Ninja docs on PDB/DWARF import and export limitations (page unversioned)
anchor: User Guide → Types → Debug Info § DWARF Export Limitations; accessed 2026-10-29; "It also does not support function-local variable names or types."
teaches: DWARF round-tripping is lossy in a documented way; types imported from debug info should be marked with the import source and known gaps.
status: mined
limitation: Do not conclude DWARF 5 import is complete; the page points to caveats in issue 5423.
province-fit: in — debug-info-aware analysis
obscurity: niche

ID-SLUG: pwndbg
source: pwndbg/pwndbg README — https://github.com/pwndbg/pwndbg/tree/e78414e1b23f0eeb026101780db60c8eeb3b7c82
kind: tool
tier: A
scope: pwndbg README self-description at the pinned commit (release 2026.10.28)
anchor: README.md intro; commit e78414e1b23f (dev), latest release 2026.10.28 (2026-10-28); accessed 2026-10-29; "is a GDB and LLDB plug-in that makes debugging suck less,"
teaches: Debugger-plugin views are convenience renderings; the evidence is the underlying memory/register read.
status: mined
limitation: Do not conclude exploit-development features are in scope for this lane.
province-fit: adjacent — live debugging, exploit-dev oriented
obscurity: mainstream

ID-SLUG: msynth
source: mrphrazer/msynth README — https://github.com/mrphrazer/msynth/tree/dfd0f9e2cd0890658fe752aa207a2cfda2aef8d7
kind: code
tier: A
scope: msynth README description of MBA simplification approach at the pinned commit (no releases)
anchor: README.md intro; commit dfd0f9e2cd08 (main), no GitHub release; accessed 2026-10-29; "Given a pre-computed simplification oracle, it walks over a complex expression represented as an abstract syntax tree (AST)"
teaches: MBA simplification is oracle-driven; a simplified expression is an inference that should be checked by random concrete evaluation against the original.
status: mined
limitation: Do not conclude semantic equivalence from synthesis output alone.
province-fit: in — static deobfuscation of arithmetic
obscurity: obscure

ID-SLUG: sogen
source: momo5502/sogen README — https://github.com/momo5502/sogen/tree/3242195ab04615ab69528455cd3b81062bd45ce1
kind: tool
tier: A
scope: Sogen README claims about deterministic Windows/Linux userspace emulation at the pinned commit (no releases)
anchor: README.md intro; commit 3242195ab046 (main), no GitHub release; accessed 2026-10-29; "runs are fully deterministic, and the entire emulator state can be snapshotted and restored."
teaches: Running real system DLLs at syscall level shifts fidelity questions from API models to syscall models; determinism + snapshots make runs citable.
status: mined
limitation: Do not conclude anti-emulation resistance; determinism itself is detectable.
province-fit: adjacent — emulated execution of artifacts
obscurity: obscure

ID-SLUG: dumpulator
source: mrexodia/dumpulator README — https://github.com/mrexodia/dumpulator/tree/18a64d7ab6ccded24c5ffe72ba17ac03fd853f8b
kind: code
tier: A
scope: dumpulator README self-description and prototype warning at the pinned commit (release v0.2.6)
anchor: README.md intro; commit 18a64d7ab6cc (main), latest release v0.2.6 (2023-10-02); accessed 2026-10-29; "An easy-to-use library for emulating code in minidump files."
teaches: Emulating from a memory dump lets one function (e.g. a string decryptor) be run as an oracle in isolation; the dump hash is part of the evidence.
status: mined
limitation: Do not conclude production readiness; the README calls it a work-in-progress prototype.
province-fit: adjacent — emulation from a captured dump
obscurity: obscure

ID-SLUG: tracer
source: SideChannelMarvels/Tracer README — https://github.com/SideChannelMarvels/Tracer/tree/8fe26af12d7dd37948d23efb2c1aa701557008ab
kind: tool
tier: A
scope: Tracer README component list (TracerPIN, TracerGrind, TraceGraph) at the pinned commit (no releases, last push 2024-07)
anchor: README.md § TraceGraph; commit 8fe26af12d7d (master), no GitHub release; accessed 2026-10-29; "TraceGraph is a GUI for visualizing execution traces produced by TracerGrind and TracerPin."
teaches: Execution-trace visualization of memory/instruction addresses exposes table lookups and rounds structurally (e.g. white-box crypto) without reading code.
status: mined
limitation: Do not conclude maintenance; repository is quiet since 2024.
province-fit: adjacent — DBI tracing (Pin/Valgrind)
obscurity: obscure

ID-SLUG: tiny-tracer
source: hasherezade/tiny_tracer README — https://github.com/hasherezade/tiny_tracer/tree/99618fc0569a4a06b7955e507e1707792ad1bef5
kind: tool
tier: A
scope: tiny_tracer README feature list at the pinned commit (release 4.0)
anchor: README.md intro; commit 99618fc0569a (master), latest release 4.0 (2026-05-28); accessed 2026-10-29; "A Pin Tool for tracing:"
teaches: API/syscall/RDTSC/CPUID tag files are a compact behavioral observation format keyed by RVA, easy to cross-link to static addresses.
status: mined
limitation: Do not conclude coverage of code paths not executed.
province-fit: adjacent — Pin-based dynamic tracing
obscurity: niche

ID-SLUG: maat
source: trailofbits/maat README — https://github.com/trailofbits/maat/tree/ac068c6cc7120cdab817ba97d362203dccb9e29b
kind: tool
tier: A
scope: Maat README description at the pinned commit (last release v0.6.9, 2022)
anchor: README.md § About; commit ac068c6cc712 (master), latest release v0.6.9 (2022-09-21); accessed 2026-10-29; "leverages Ghidra's sleigh library for assembly lifting"
teaches: A sleigh-based lifter shares Ghidra's instruction semantics; agreement between Maat and Ghidra is not independent confirmation.
status: mined
limitation: Do not conclude active maintenance from recent pushes; last release is 2022.
province-fit: in — symbolic execution / taint
obscurity: niche

ID-SLUG: binsec
source: binsec/binsec README — https://github.com/binsec/binsec/tree/9749bd8aed7ee0a27959158b1e53e8789cb0e5ab
kind: tool
tier: A
scope: BINSEC README description at the pinned commit (release 0.11.3)
anchor: README.md intro; commit 9749bd8aed7e (master), latest release 0.11.3 (2026-08-26); accessed 2026-10-29; "binary-level formal methods, symbolic execution, abstract interpretation,"
teaches: Formal-methods tooling at binary level yields proof-style claims whose assumptions (memory model, stubs) must be ledgered with the result.
status: mined
limitation: Do not conclude results transfer between the tool's analyses; each has its own assumptions.
province-fit: in — binary-level formal analysis
obscurity: obscure

ID-SLUG: icicle
source: icicle-emu/icicle-emu README — https://github.com/icicle-emu/icicle-emu/tree/638508b72f480f9be6fe2e267ef09de8f1541f9a
kind: tool
tier: A
scope: Icicle README self-description and crate layout at the pinned commit (no releases)
anchor: README.md intro; commit 638508b72f48 (master), no GitHub release; accessed 2026-10-29; "Icicle is an experimental fuzzing-specific, multi-architecture emulation framework."
teaches: A SLEIGH/p-code emulator gives a semantics source independent of QEMU/Unicorn for cross-checking emulated results.
status: mined
limitation: Do not conclude fitness for general RE; it is fuzzing-specific and experimental.
province-fit: adjacent — emulation; fuzzing focus is outside the lane
obscurity: obscure

ID-SLUG: kavanoz
source: eybisi/kavanoz README — https://github.com/eybisi/kavanoz/tree/9feb6acf589ee3aff14796c638113c763776e524
kind: tool
tier: A
scope: kavanoz README purpose statement at the pinned commit (release v0.0.6, repo archived)
anchor: README.md intro; commit 9feb6acf589e (main), latest release v0.0.6 (2025-04-02); accessed 2026-10-29; "Kavanoz (jar in turkish) is a tool to statically unpack common android banker malware."
teaches: Static, plugin-per-packer APK unpacking produces a payload plus the plugin name that succeeded — both belong in the ledger.
status: mined
limitation: Do not conclude coverage of current packers; the repository is archived.
province-fit: in — static APK unpacking
obscurity: obscure

ID-SLUG: de4dotex
source: GDATAAdvancedAnalytics/de4dotEx README — https://github.com/GDATAAdvancedAnalytics/de4dotEx/tree/ee602ca73474cdd8c7d23f487bc0c588a2b2bbeb
kind: tool
tier: A
scope: de4dotEx README warning about executing input during deobfuscation at the pinned commit (release 3.12.0)
anchor: README.md ***WARNING***; commit ee602ca73474 (master), latest release 3.12.0 (2026-10-23); accessed 2026-10-29; "Other backends such as Eazfuscator and ILProtector may attempt to run parts of the input assembly for deobfuscation, which is dangerous."
teaches: 'Static' deobfuscators can execute input; the tool's backend choice decides whether a run was static or dynamic, which the ledger must state.
status: mined
limitation: Do not conclude restored symbol names are original; the README says renaming cannot be undone.
province-fit: in — .NET deobfuscation, with execution caveat
obscurity: niche

ID-SLUG: hashdb
source: OALabs/hashdb README — https://github.com/OALabs/hashdb/tree/28fc56a7f4ad614e8525b66395dfb307d0553459
kind: code
tier: A
scope: HashDB README description of its algorithm library and lookup service at the pinned commit
anchor: README.md § HashDB; commit 28fc56a7f4ad (main), no GitHub release; accessed 2026-10-29; "HashDB is a community-sourced library of hashing algorithms used in malware."
teaches: API-hash resolution is a byte-checkable claim: recompute the hash of the candidate name with the named algorithm and compare.
status: mined
limitation: Do not conclude a lookup-service hit is unique; collisions across algorithms/strings are possible.
province-fit: in — static API-hash resolution
obscurity: niche

ID-SLUG: manalyze
source: JusticeRage/Manalyze README — https://github.com/JusticeRage/Manalyze/tree/8d7cbb5bc8c68103b429c6738b2f5cc5ce5e8a32
kind: tool
tier: A
scope: Manalyze README description at the pinned commit (release v1.0.0)
anchor: README.md § Introduction; commit 8d7cbb5bc8c6 (master), latest release v1.0.0 (2026-07-21); accessed 2026-10-29; "It collects weak signals that could indicate malicious behavior"
teaches: Triage outputs framed as 'weak signals' are leads, not findings; ledger them as inferences with the plugin that raised them.
status: mined
limitation: Do not conclude maliciousness from any single signal.
province-fit: in — static PE triage
obscurity: niche

ID-SLUG: xrefer
source: mandiant/xrefer README — https://github.com/mandiant/xrefer/tree/1aeda163ccae9be7b01dd6172513c28878f758b6
kind: tool
tier: A
scope: XRefer README description incl. LLM integration at the pinned commit (release v1.0.3)
anchor: README.md intro; commit 1aeda163ccae (main), latest release v1.0.3 (2025-01-22); accessed 2026-10-29; "It integrates with Google's Gemini model to produce natural language descriptions of code relationships and behaviors."
teaches: LLM-generated function descriptions are model inferences and must be tagged with model + prompt, never promoted to observation.
status: mined
limitation: Do not conclude cluster labels are verified behavior.
province-fit: in — static navigation with LLM-assisted labeling
obscurity: niche

ID-SLUG: mal-unpack
source: hasherezade/mal_unpack README — https://github.com/hasherezade/mal_unpack/tree/cecb9eed03c63d651c5b47834b15bac8086cb2fb
kind: tool
tier: A
scope: mal_unpack README statement of how it unpacks, at the pinned commit (release 1.0)
anchor: README.md intro; commit cecb9eed03c6 (master), latest release 1.0 (2025-09-13); accessed 2026-10-29; "It deploys a packed malware, waits for it to unpack the payload, dumps the payload, and kills the original process."
teaches: Dynamic unpackers execute the sample; outputs are live-execution artifacts.
status: rejected — README: "This unpacker deploys the original malware. Use it only on a VirtualMachine." → live-malware execution is refused in this province. Flip: lane charter adds an isolated dynamic-detonation lane with its own controls.
limitation: Do not conclude static safety.
province-fit: out — requires executing live malware
obscurity: niche

ID-SLUG: unlicense
source: ergrelet/unlicense README — https://github.com/ergrelet/unlicense/tree/95c8dc6a4324ff70c04bceda8bd166be6c5f0c73
kind: tool
tier: A
scope: Unlicense README features and warnings at the pinned commit (release 0.4.0)
anchor: README.md intro / Known Limitations; commit 95c8dc6a4324 (main), latest release 0.4.0 (2023-08-14); accessed 2026-10-29; "Warning: This tool will execute the target executable."
teaches: Commercial-protector unpackers execute the target and recover OEP/imports.
status: rejected — README: "A Python 3 tool to dynamically unpack executables protected with" Themida/WinLicense, executing the target to strip a commercial protector (DRM-adjacent, live execution). Flip: lane accepts it purely as a cited description of protector structure, never as a procedure.
limitation: Do not conclude runnable dumps; README says it usually does not produce them.
province-fit: out — executes target to strip a commercial software protector (DRM-adjacent)
obscurity: niche

## Screened and dropped (opened or metadata-checked, not kept)

- https://github.com/hasherezade/pe-sieve — scans/dumps implants from live running processes (live-target activity; out of province).
- https://github.com/hugsy/gef — install path in README is `bash -c "$(curl -fsSL …)"`; capability overlaps pwndbg row.
- https://github.com/fkie-cad/cwe_checker — goal is finding vulnerable code paths (vuln-hunting, exploitation-adjacent); hand to a firmware/vuln lane if wanted.
- https://github.com/JonathanSalwan/VMProtect-devirtualization — README is research notes on devirtualizing a commercial protector; DRM-adjacent, no pinned release; keep only as a citation if the lane adds protector-structure scope.
- https://github.com/de4dot/de4dot — archived 2020; superseded by de4dotEx row.
- https://github.com/mandiant/flare-emu — archived (2025-08-14).
- https://github.com/rizinorg/cutter — GUI over rizin; rizin/radare2 already in corpus, Cutter adds no checkable claim.
- https://github.com/airbus-cert/Winshark — ETW live capture; dynamic host monitoring, out of artifact-first scope.
- https://github.com/mandiant/flare-fakenet-ng — network simulation for live detonation; out.
- https://github.com/Alk4lo1d/VMDragonSlayer, https://github.com/anpa1200/Unpacker, https://github.com/1-3-7/disrobe — surfaced by search; new, low-provenance aggregators (search snippets only, not opened); not kept.
- Radare2 ESIL — radare2/rizin repos already in /tmp/revenger-existing-urls.txt; skipped per rule 3.
- Intel Pin product page — not opened this session (Pin represented via tiny_tracer/TracerPIN rows); lead: https://www.intel.com/content/www/us/en/developer/articles/tool/pin-a-dynamic-binary-instrumentation-tool.html

## Search log

- GitHub API (gh, authenticated): metadata+latest release+HEAD commit for 63 repos; README fetched at pinned commit for 45; extra docs fetched at pinned commit: capa doc/limitations.md, capa-rules doc/format.md, speakeasy doc/limitations.md.
- web_search (Parallel fallback; Perplexity rate-limited): (1) "open source unpacker deobfuscator tool symbolic execution github obscure malware triage emulator" → de4dotEx, kavanoz, VMDragonSlayer, disrobe, Unpacker, safe-deobs; (2) "DWARF-aware binary diffing tool debug info diff github" → objdiff, Binja Debug Info docs, radiff2; (3) "binary taint analysis tool open source dynamic taint tracking framework github" → maat, DTA++ paper, opentaint (source-level, out).
- Web pages opened: docs.binary.ninja bnil-overview, docs.binary.ninja debuginfo, rr-project.org, pernos.co/about/overview, arXiv 1705.05937 (abs).
- Counts: identified ≈70 · screened 63 repos + 5 pages · kept (mined) 44 · rejected rows 2 · dropped leads 12.
- Obscure picks (≥4 required): capa-testfiles, objdiff, msynth, sogen, dumpulator, SideChannelMarvels Tracer, BINSEC, Icicle, kavanoz.