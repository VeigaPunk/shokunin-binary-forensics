# ReDisasmGroundTruth — disassembly / decompilation / lifting: research & ground-truth sources

Slice owner: REVENGER_SHOKUNIN.ReDisasmGroundTruth · accessed 2026-10-29 · read-only (no repo edits).
All rows below were opened this session (`read` and/or `curl`). Every quote was re-checked by a script that
fetched the pinned URL, stripped tags/markdown and searched for the quote as a substring. 24 matched. Three
failed only because of tag-stripping spacing (Phoenix, SLEIGH) or a bot wall on curl (BiNit/HAL), so for
those three the quote was confirmed by eye against the `read` render. GitHub commit pins are `git ls-remote
HEAD` values taken on 2026-10-29, within minutes of the page fetch.
Excluded as already in corpus: `usenixsecurity22/presentation/burk` (Decomperson), `arxiv 2403.05286v3`
(LLM4Decompile/Decompile-Eval), `sec22-chen-qibin.pdf` (DIRTY), `NationalSecurityAgency/ghidra` repo root (the
SLEIGH/P-code rows below point at specific doc files under it, pinned to a commit).

---

ID-SLUG: sok-x86-disassembly-2021
source: SoK: All You Ever Wanted to Know About x86/x64 Binary Disassembly But Were Afraid to Ask (Pang et al., IEEE S&P 2021) — https://arxiv.org/abs/2007.14266 (v1, 2020-07-28)
kind: paper
tier: A
scope: The authors' own abstract claims about nine open-source disassemblers studied over 3,788 binaries, as published in arXiv v1.
anchor: Abstract, arXiv:2007.14266v1 (2020-07-28), accessed 2026-10-29 — "We find that while principled algorithms are used by all tools, they still heavily rely on heuristics to increase code coverage."
teaches: Every disassembly result mixes algorithmic recovery with heuristic recovery. The ledger should record which disassembler and which heuristic produced an instruction or function boundary, and should not treat disassembly as a single fact.
status: mined
limitation: Rankings cover specific 2020-era tool versions and x86/x64 only; do not rank today's tools from them.
province-fit: in — native-binary static disassembly is core province.
obscurity: niche

ID-SLUG: ground-truth-disasm-not-easy
source: Ground Truth for Binary Disassembly is Not Easy (Pang, Zhang, Yu, Mao, Xu; USENIX Security 2022, pp. 2479–2495) — https://www.usenix.org/conference/usenixsecurity22/presentation/pang-chengbin
kind: paper
tier: A
scope: The authors' taxonomy of five ground-truth-collection mechanisms, their recommendation of compile-process tracing, and their extension of that approach to ARM32/AArch64/MIPS.
anchor: Abstract on USENIX presentation page (Sec '22, artifact badges: available/functional/reproduced), accessed 2026-10-29 — "The mechanism best serving today's need is to trace the compiling process of the target binaries to collect the ground truth information."
teaches: A byte-oracle fixture's ground truth is only as good as how it was collected. Derive it from the build (compiler/linker tracing), not from another disassembler or from debug symbols alone, and record the collection mechanism with the fixture.
status: mined
limitation: Covers compiler-built binaries where you control the build; it gives no ground-truth method for shipped third-party artifacts.
province-fit: in — directly governs byte-oracle fixture construction.
obscurity: niche

ID-SLUG: andriesse-disasm-full-scale-2016
source: An In-Depth Analysis of Disassembly on Full-Scale x86/x64 Binaries (Andriesse, Chen, van der Veen, Slowinska, Bos; USENIX Security 2016, pp. 583–600) — https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/andriesse
kind: paper
tier: A
scope: The authors' abstract claims from evaluating nine disassemblers on 981 compiler-generated binaries, plus their review of 30 security papers.
anchor: Abstract on USENIX presentation page (Sec '16), accessed 2026-10-29 — "some constructs, such as function boundaries, are much harder to recover accurately than is reflected in the literature"
teaches: Function-boundary claims deserve lower default confidence than instruction-level claims. Treat recovered function starts and ends as inference unless a symbol table, unwind data or build trace corroborates them.
status: mined
limitation: Covers compiler-generated, non-obfuscated binaries; it supports no conclusion about packed or hand-written code.
province-fit: in — native static disassembly.
obscurity: niche

ID-SLUG: sailr-compiler-aware-structuring
source: Ahoy SAILR! There is No Need to DREAM of C: A Compiler-Aware Structuring Algorithm for Binary Decompilation (Basque et al., USENIX Security 2024, pp. 361–378) — https://www.usenix.org/conference/usenixsecurity24/presentation/basque
kind: paper
tier: A
scope: The authors' claims that spurious gotos come from compiler optimizations, plus their open-source angr decompiler implementations of SAILR, Phoenix, DREAM and Combing.
anchor: Abstract on USENIX page (Sec '24, artifact available/functional), accessed 2026-10-29 — "the root cause of spurious gotos is compiler-induced optimizations that occur at all optimization levels (17% in non-optimized compilation)"
teaches: Do not log the control-flow shape of decompiled output as the source's shape. Structuring artifacts (gotos, duplicated blocks) can come from compiler transforms, and closeness to the source is a separate, measurable property.
status: mined
limitation: The evaluation centers on GCC-style transforms; it does not establish source-structure fidelity for other compilers or obfuscated code.
province-fit: in — decompiler-output interpretation.
obscurity: niche

ID-SLUG: dream-no-more-gotos-ndss15
source: No More Gotos: Decompilation Using Pattern-Independent Control-Flow Structuring and Semantics-Preserving Transformations (Yakdan, Eschweiler, Gerhards-Padilla, Smith; NDSS 2015) — https://www.ndss-symposium.org/ndss2015/ndss-2015-programme/no-more-gotos-decompilation-using-pattern-independent-control-flow-structuring-and-semantics/
kind: paper
tier: A
scope: The authors' description of DREAM's goto-free structuring and its coreutils comparison against Hex-Rays and Phoenix.
anchor: Abstract, NDSS 2015 programme page (dated 7 Feb 2015; page modified 2023-07-25), accessed 2026-10-29 — "Whenever no match is found they generate goto statements and thus produce unstructured decompiled output."
teaches: A goto in decompiler output can mean "the structurer found no pattern", not "the binary contains a goto". Log it as a tool limitation, not as a behavioral fact.
status: mined
limitation: Its goal of zero gotos is a readability target, and SAILR (above) disputes it as a fidelity target; do not read "goto-free" as "correct".
province-fit: in — decompiler-output interpretation.
obscurity: niche

ID-SLUG: phoenix-semantics-preserving-structuring
source: Native x86 Decompilation Using Semantics-Preserving Structural Analysis and Iterative Control-Flow Structuring (Schwartz, Lee, Woo, Brumley; USENIX Security 2013, pp. 353–368) — https://www.usenix.org/conference/usenixsecurity13/technical-sessions/presentation/schwartz
kind: paper
tier: A
scope: The authors' claim that earlier structuring algorithms were not semantics-preserving, and their Phoenix evaluation on 107 coreutils programs.
anchor: Abstract on USENIX Sec '13 page, accessed 2026-10-29 — "existing structuring algorithms are not semantics-preserving, which means that they cannot safely be used for decompilation without modification"
teaches: Structuring is a transformation that can change meaning. A decompiler's C is a derived artifact whose correctness needs its own check, separate from the disassembly it came from.
status: mined
limitation: The "outperforms Hex-Rays by 114%" claim is about 2013 versions under the authors' own correctness metric; it is not evidence about current Hex-Rays.
province-fit: in — decompiler correctness.
obscurity: niche

ID-SLUG: issta20-decompilation-correctness
source: How Far We Have Come: Testing Decompilation Correctness of C Decompilers (Zhibo Liu, Shuai Wang; ISSTA 2020, pp. 475–487, DOI 10.1145/3395363.3397370) — https://researchportal.hkust.edu.hk/en/publications/how-far-we-have-come-testing-decompilation-correctness-of-c-decom/
kind: paper
tier: A
scope: The authors' abstract: 1,423 error-triggering inputs across four decompilers and 13 bugs in two open-source ones, published 18 Jul 2020 (the institutional record of the ACM paper).
anchor: Abstract, HKUST research portal record (publication date 2020-07-18), accessed 2026-10-29 — "some tasks that have been studied for years in academia, such as type inference and optimization, still impede C decompilers from generating quality outputs"
teaches: Recompile-and-compare (EMI/Csmith differential testing) is a usable oracle for decompiler correctness. Type recovery and optimized code are where decompiler C is least trustworthy, so claims built on recovered types need corroboration.
status: mined
limitation: Error-triggering inputs are not distinct bugs, and results describe 2020 versions (IDA, JEB3, RetDec, r2ghidra), not current tools.
province-fit: in — decompiler trust calibration.
obscurity: niche

ID-SLUG: decfuzzer-issta20-artifact
source: DecFuzzer — ISSTA'20 artifact (monkbai/DecFuzzer @ 8e109c12d499df0223430ae17f71aac3109bd1f6) — https://github.com/monkbai/DecFuzzer
kind: code
tier: A
scope: The artifact README's statement of the pipeline (Csmith seeds → compile → decompile → replace main → compare outputs) and of which decompilers ship in the artifact.
anchor: README §3.3 "Decompilers", commit 8e109c1, accessed 2026-10-29 — "We assure that two commercial decompilers are tested in exactly the same way."
teaches: A worked example of a self-attested, unreproducible claim: the commercial-tool results (IDA, JEB3) cannot be re-run from the artifact. A ledger should mark such results "attested, not reproducible" and keep them apart from the reproducible RetDec/r2ghidra results.
status: mined
limitation: Pins old dependencies (Ubuntu 18.04, RetDec v4.0, a 2020 radare2 commit); do not assume it runs today.
province-fit: in — decompiler correctness oracle method.
obscurity: obscure

ID-SLUG: scalable-validation-binary-lifters
source: Scalable Validation of Binary Lifters (Dasgupta, Dinesh, Venkatesh, Adve, Fletcher; PLDI 2020) — implementation README at https://github.com/sdasgup3/validating-binary-decompilation (@ c0fcd6f099e38195dcbbac9e8c13a825865c5cb5)
kind: code
tier: A
scope: The repo's own description of single-instruction validation (K-framework x86-64 semantics vs LLVM symbolic summaries, checked with Z3) and program-level validation (graph matching), plus its claim of 29 McSema bugs.
anchor: README intro, commit c0fcd6f, accessed 2026-10-29 — "if these summaries are not logically equivalent, a bug is detected in McSema."
teaches: Lifted IR can be checked per instruction against an independent formal ISA semantics. Treat a lifter's IR as a translation that needs validation before facts derived from it are cited.
status: mined
limitation: Covers McSema/Remill x86-64 → LLVM at that time only; it does not certify any other lifter or later versions. The PLDI paper PDF itself was not opened.
province-fit: in — lifting correctness.
obscurity: obscure

ID-SLUG: binit-x64-lifter-semantic-bugs
source: BiNit: Nitpicking Semantic Bugs in x64 Binary Lifters (Royer, Tronel, Vinçont; SURE 2026 workshop, DOI 10.1145/3847158.3847383) — https://inria.hal.science/hal-05753704 (HAL version 1, 2026-09-17)
kind: paper
tier: A
scope: The authors' abstract: a differential tester comparing concrete instruction execution with emulated lifted IR across 7 tools, reporting 35 semantic bugs.
anchor: Abstract, HAL record hal-05753704v1 (submitted 2026-09-17), accessed 2026-10-29 — "BiNit compares concrete values from instruction executions and their emulated lifted counterparts, making lifter bugs easier to detect and diagnose."
teaches: Instruction-semantics bugs are still common in mature lifters. A claim that rests on the IR semantics of one unusual instruction (flags, undefined behavior) needs a concrete-execution cross-check or should be logged as unknown.
status: mined
limitation: Its comparison against concrete execution means running instructions on a CPU. That is local test-harness execution, not live-target activity, but the ledger lesson is static. The 35 bugs and 7 tools are not named in the abstract.
province-fit: in — lifting correctness.
obscurity: obscure

ID-SLUG: decompile-diverge-recompile-vs-preserve
source: When LLM Decompilers Recompile More and Preserve Less (Liu, Raff, Micinski) — https://arxiv.org/abs/2609.05370 (v1, 2026-09-04)
kind: paper
tier: A
scope: The authors' abstract claims that recompilability and re-executability metrics can pass functions that still diverge in behavior (4.9% overall; Crash Absence in some vulnerable functions).
anchor: Abstract, arXiv:2609.05370v1 (2026-09-04), accessed 2026-10-29 — "a function may recompile and pass every shipped test yet diverge on other legitimate inputs"
teaches: "It recompiles" and "it passes the shipped tests" are weak oracles. LLM-cleaned decompiler output can silently drop the very guard or crash under investigation, so keep the raw decompiler placeholders as evidence and treat any rewrite as inference.
status: mined
limitation: Preprint with no peer-review status; figures apply to the systems and corpora it tested.
province-fit: in — decompiler/LLM output trust.
obscurity: obscure

ID-SLUG: decompilebench-real-world
source: DecompileBench: A Comprehensive Benchmark for Evaluating Decompilers in Real-World Scenarios (Gao et al.) — https://arxiv.org/abs/2505.11340 (v1, 2025-05-16)
kind: paper
tier: A
scope: The authors' benchmark design (23,400 functions from 130 programs, runtime-aware validation, LLM-as-judge) and their headline comparison claim.
anchor: Abstract, arXiv:2505.11340v1 (2025-05-16), accessed 2026-10-29 — "LLM-based methods surpass commercial tools in code understandability despite 52.2% lower functionality correctness"
teaches: Readability and functional correctness of decompiled code are separate axes that can move in opposite directions. A ledger should never use "reads cleanly" as evidence of correctness.
status: mined
limitation: The understandability scores come from an LLM judge, not humans; do not cite them as analyst-validated.
province-fit: in — decompiler evaluation.
obscurity: niche

ID-SLUG: decbench-living-benchmark
source: DecBench — Noelo-Lab/decbench (@ ae070b885b4e005ed37510a2c3445af6284dc2b9; site decbench.com) — https://github.com/Noelo-Lab/decbench
kind: dataset
tier: A
scope: The README's definition of three exactness metrics (CFG graph-edit distance, DWARF type match, recompilation bytematch with the original toolchain) and its pipeline notes.
anchor: README "Generating results" section, commit ae070b8, accessed 2026-10-29 — "without the `.i` files GED is silently skipped for the entire run"
teaches: Evaluation pipelines can silently drop a metric. A ledger entry citing a benchmark score should record which metrics actually ran, and a missing input should block the claim rather than shrink it.
status: mined
limitation: Self-described as "experimental" and "living", so scores change over time; pin the snapshot before citing any number. The leaderboard site itself was not opened.
province-fit: in — decompiler ground-truth metrics.
obscurity: obscure

ID-SLUG: decompiler-types-benchmark
source: Benchmarking Binary Type Inference Techniques in Decompilers — artifact repo sefcom/decompiler-types-benchmark (@ 49259a0e86b43e48602b158580264155a18ef8aa) — https://github.com/sefcom/decompiler-types-benchmark
kind: dataset
tier: A
scope: The repo's own statement of what it contains: binaries, DWARF-extraction and evaluation scripts, extracted types and results for the SURE'25 paper.
anchor: README (entire text), commit 49259a0, accessed 2026-10-29 — "This repository contains the binaries, extraction and evaluation scripts, extracted type data and the results of the paper"
teaches: Build type-recovery ground truth by extracting DWARF from an unstripped build and scoring the stripped twin, so a recovered type can be checked against the build rather than accepted.
status: mined
limitation: The README makes no accuracy claims; numbers cited elsewhere (e.g. Hex-Rays struct-identification rates) come from the ACM paper, which was not opened here.
province-fit: in — type-recovery evaluation.
obscurity: obscure

ID-SLUG: remill-life-of-an-instruction
source: Remill — "Machine code to bitcode: the life of an instruction" (lifting-bits/remill @ 56918a8c2554088e93389e97d292f4035286506c, docs/LIFE_OF_AN_INSTRUCTION.md) — https://github.com/lifting-bits/remill/blob/56918a8c2554088e93389e97d292f4035286506c/docs/LIFE_OF_AN_INSTRUCTION.md
kind: docs
tier: A
scope: The project's own explanation of decode → semantics function → LLVM bitcode, the State/Memory model and the intrinsics boundary.
anchor: § "The Remill runtime exposed", commit 56918a8, accessed 2026-10-29 — "Remill has no way of knowing what this actually means or how it works"
teaches: A lifter marks where its knowledge ends (here `int 0x80` becomes `__remill_async_hyper_call`). Whatever lies past such an intrinsic is unknown until OS/ABI evidence fills it.
status: mined
limitation: Describes Remill's design only; it is no evidence that any particular instruction's semantics are correct (see the validation rows above).
province-fit: in — lifting internals.
obscurity: niche

ID-SLUG: rellic-goto-free-from-bitcode
source: Rellic — lifting-bits/rellic (@ 370abaad86ae5adad82f85b81aff14557462b7f2) — https://github.com/lifting-bits/rellic
kind: code
tier: A
scope: The README's statement of what Rellic implements (DREAM pattern-independent structuring over LLVM bitcode) and its side-by-side examples.
anchor: README intro, commit 370abaa, accessed 2026-10-29 — "Rellic is an implementation of the pattern-independent structuring algorithm to produce a goto-free C output from LLVM bitcode."
teaches: The README's own fizzbuzz example shows correct but restructured conditions (`if ((int)i % 3 != 0U || !(...))`). Decompiled control flow can be equivalent yet look nothing like the source.
status: mined
limitation: Input is LLVM bitcode, not machine code, so its output quality also depends on the upstream lifter.
province-fit: in — decompilation pipeline.
obscurity: niche

ID-SLUG: mcsema-archived-lifter
source: McSema — lifting-bits/mcsema (archived 2022-08-23; @ 26368053f761be05dab708bc28fb97090c64b2be) — https://github.com/lifting-bits/mcsema
kind: code
tier: A
scope: The README's two-stage design (IDA-based CFG recovery, then Remill instruction translation) and the archive banner.
anchor: README intro, commit 2636805 (repo archived Aug 23, 2022), accessed 2026-10-29 — "which relies on IDA Pro to disassemble a binary file and produce a control flow graph"
teaches: A lifter's IR inherits its disassembler's CFG errors. Separately, the archived README still says "Actively maintained? Yes" in its comparison table, so a project's self-description can go stale and needs a dated check.
status: mined
limitation: Archived; do not plan current work around it. Its comparison table of other lifters is a dated self-report, not a fact about those tools today.
province-fit: in — lifting.
obscurity: niche

ID-SLUG: retdec-limited-maintenance
source: RetDec — avast/retdec (@ 9450585772e6f1c18e5f0b2ad5518a18d6bce71e) — https://github.com/avast/retdec
kind: tool
tier: A
scope: The README's maintenance-status banner and its own list of supported formats and architectures.
anchor: README top warning box, commit 9450585, accessed 2026-10-29 — "Only a very limited development is carried on."
teaches: Record a tool's maintenance status next to its output in the ledger. Output from a limited-maintenance decompiler is weaker corroboration for newer compiler idioms.
status: mined
limitation: The feature list (RTTI/vtable reconstruction, PDB/DWARF use) is the project's own claim, not verified here.
province-fit: in — native decompiler.
obscurity: mainstream

ID-SLUG: reko-decompiler
source: Reko — uxmal/reko (@ d75c841b6d088577e915b01200b2e00093d4924a) — https://github.com/uxmal/reko
kind: tool
tier: A
scope: The README's description of Reko's frontends, decompiler engine and project files, plus its legal-use notice.
anchor: README intro, commit d75c841, accessed 2026-10-29 — "Use this decompiler only if you have legal rights to decompile the binary"
teaches: A primary-source tool notice that matches the province refusal line. Record the license/authorization basis in the ledger before decompiling a third-party artifact.
status: mined
limitation: The README makes no correctness claims; architecture coverage is on a wiki page that was not opened.
province-fit: in — multi-arch decompiler (incl. m68k/RISC-V, useful for firmware).
obscurity: niche

ID-SLUG: bap-binary-analysis-platform
source: CMU Binary Analysis Platform — BinaryAnalysisPlatform/bap (@ 034bbd09646a589d5eb1f10b740177d628da80fd) — https://github.com/BinaryAnalysisPlatform/bap
kind: tool
tier: A
scope: The README's overview of supported architectures, the Primus interpreter/symbolic executor and the plugin model, at that commit.
anchor: README § Overview, commit 034bbd0, accessed 2026-10-29 — "BAP supports x86, x86-64, ARM, MIPS, PowerPC and new architectures can be added using plugins."
teaches: BAP is a second, independent lifter and IR (BIL/Core Theory) to cross-check another tool's semantics, and agreement between independent lifters is stronger evidence than one lifter's output.
status: mined
limitation: Latest packaged release referenced is v2.5.0; the README alone does not establish current maintenance pace.
province-fit: in — lifting/IR.
obscurity: niche

ID-SLUG: dewolf-research-decompiler
source: dewolf — fkie-cad/dewolf (@ 3c389e18f03cd922f4b424a62d3717dac6fe3eee) — https://github.com/fkie-cad/dewolf
kind: tool
tier: A
scope: The README's statement that dewolf is a Binary Ninja MLIL-based research decompiler whose restructuring follows DREAM/DREAM++.
anchor: README intro, commit 3c389e1, accessed 2026-10-29 — "you will likely observe a few bugs or even decompilation failures when applying dewolf on real-world binaries."
teaches: The authors' own disclaimer is a good default: label research-decompiler output as low-confidence inference and corroborate it with a production decompiler.
status: mined
limitation: Requires a commercial Binary Ninja (≥3.4) license; the source does not say how well it works without one.
province-fit: in — decompiler.
obscurity: niche

ID-SLUG: dogbolt-decompiler-explorer
source: Decompiler Explorer — https://dogbolt.org/ (service) + source decompiler-explorer/decompiler-explorer @ 9afcaecd99ac90c445106c10eb5abbb4247c6c4d
kind: tool
tier: A
scope: The service's own upload policy (under 2MB, binaries retained), its decompiler list (angr, Binary Ninja, Boomerang, dewolf, Ghidra, Hex-Rays, Kuna, RecStudio, Reko, Relyze, RetDec, rev.ng, Snowman) and the README's purpose statement.
anchor: dogbolt.org "Upload File" panel, accessed 2026-10-29 — "Uploaded binaries are retained"; README (commit 9afcaec): "This web service lets you compare the output of different decompilers on small executables."
teaches: Comparing several decompilers on the same binary gives a quick disagreement map. Because uploads are retained, only self-built or explicitly shareable fixtures may be uploaded, never a client's shipped artifact.
status: mined
limitation: The site does not pin decompiler versions in what was opened; record the version shown per run, and do not treat agreement as ground truth.
province-fit: in — triage and cross-decompiler disagreement.
obscurity: niche

ID-SLUG: compiler-explorer-fixture-oracle
source: Compiler Explorer — compiler-explorer/compiler-explorer README (@ c655710e809d203f988ce34653e2aa854937177c); service https://godbolt.org/
kind: tool
tier: A
scope: The README's description of interactive source-to-assembly compilation, the local-instance option and the REST API pointer.
anchor: README § intro, commit c655710, accessed 2026-10-29 — "see how that code looks after being compiled in real time."
teaches: Forward compilation of known source with a pinned compiler and flags produces small byte-oracle fixtures, i.e. known source↔asm pairs. A local instance keeps them reproducible and offline.
status: mined
limitation: Public godbolt.org links store code via a URL shortener; do not paste proprietary or third-party code there. Its asm view is filtered, so it is not a byte-exact image of a linked binary.
province-fit: adjacent — builds fixtures; it does not analyze shipped artifacts.
obscurity: mainstream

ID-SLUG: ghidra-sleigh-spec
source: SLEIGH: A Language for Rapid Processor Specification — Ghidra repo GhidraDocs/languages/html/sleigh.html (@ 1b9e58a915cf867e106495eaa2a4b18eb4971c9d; doc "Last updated October 31, 2023") — https://github.com/NationalSecurityAgency/ghidra/blob/1b9e58a915cf867e106495eaa2a4b18eb4971c9d/GhidraDocs/languages/html/sleigh.html
kind: spec
tier: A
scope: The official SLEIGH spec's overview, its lineage (SLED, UQBT's SSL, Cifuentes 1994) and its definition of SLEIGH's role in disassembly and decompilation.
anchor: § Overview, commit 1b9e58a, accessed 2026-10-29 — "For decompilation, SLEIGH describes the translation from machine instructions into p-code."
teaches: Ghidra's disassembly and decompilation semantics come from a hand-written per-processor spec. A suspicious Ghidra result can be traced to the exact `.slaspec` constructor and cited as the source of the semantics.
status: mined
limitation: The spec defines the language, not the correctness of any processor module written in it.
province-fit: in — Ghidra internals.
obscurity: niche

ID-SLUG: ghidra-pcode-reference
source: P-Code Reference Manual — Ghidra repo GhidraDocs/languages/html/pcoderef.html (@ 1b9e58a915cf867e106495eaa2a4b18eb4971c9d; doc "Last updated January 16, 2026") — https://github.com/NationalSecurityAgency/ghidra/blob/1b9e58a915cf867e106495eaa2a4b18eb4971c9d/GhidraDocs/languages/html/pcoderef.html
kind: spec
tier: A
scope: The official definitions of address space, varnode and raw vs analysis p-code (MULTIEQUAL/INDIRECT exist only after analysis).
anchor: § "A Brief Introduction to P-Code" → Varnode, commit 1b9e58a, accessed 2026-10-29 — "Varnodes by themselves are just a contiguous chunk of bytes, identified by their address and size, and they have no type."
teaches: Types in Ghidra's decompiler output are inferred on top of untyped varnodes. A recovered type is always inference, and raw p-code (emulatable) and analysis p-code should be cited separately.
status: mined
limitation: The manual describes Ghidra's IR only; it implies nothing about other tools' IRs.
province-fit: in — Ghidra internals.
obscurity: niche

ID-SLUG: no-bit-left-behind-superset-lifting
source: No Bit Left Behind: Using Brute-Force Lifting to Achieve Fully Static Binary Recompilation (Huang, Chen, Baron, Franz) — https://arxiv.org/abs/2609.16423 (v1, 2026-09-14)
kind: paper
tier: A
scope: The authors' claims of superset-CFG lifting with no code/data heuristics, and of an x86-64 → LLVM IR → AArch64 static cross-compilation.
anchor: Abstract, arXiv:2609.16423v1 (2026-09-14), accessed 2026-10-29 — "we treat every byte offset as a potential branch target and lift the entire binary in a brute-force manner"
teaches: Statically recovering a CFG is impossible in general, so a superset (every offset) is the only heuristic-free over-approximation. A ledger's code/data split is an inference that should name the heuristic used.
status: mined
limitation: Preprint and prototype; the abstract reports no scale or overhead figures, and recompilation is outside province (cite only the disassembly lesson).
province-fit: adjacent — lifting theory is in; binary recompilation/translation as an end use is not the province's goal.
obscurity: obscure

---

## Screened and dropped / not opened

- https://dl.acm.org/doi/10.1145/3395363.3397370 — HTTP 403 from ACM DL; replaced by the HKUST institutional record (same DOI, abstract).
- https://conf.researchr.org/details/issta-2020/issta-2020-papers/23/... — the guessed path id served a different paper (CoCoNuT); discarded.
- https://www.usenix.org/conference/usenixsecurity24/presentation/dramko-taxonomy — HTTP 404 (guessed slug); also listed as a peer slice (BfResearchPapers), so not chased.
- https://github.com/ltfish/decbench — fork of Noelo-Lab/decbench; the upstream was used.
- https://www.usenix.org/conference/usenixsecurity22/presentation/burk, arXiv 2403.05286 (LLM4Decompile), sec22-chen-qibin (DIRTY) — already in corpus.
- Leads found by search but NOT opened (so no rows): LiftFuzz (CCS 2024, DOI 10.1145/3658644.3670276); "Testing Intermediate Representations for Binary Analysis" (ASE 2017, N-version IR testing); RecStruct (USENIX Sec 2026, nested struct recovery); "Formally verified lifting of C-compiled x86-64 binaries" (PLDI 2022); "Verifiably Correct Lifting of Position-Independent x86-64 Binaries" (CCS 2024); arXiv 2505.12668 Decompile-Bench; Scalable Validation PLDI PDF (sushant94.me). These are strong next candidates for the next round.
- https://dogbolt.org/faq — the retention policy details behind "are retained" were not opened.

## Search log

- Direct opens from slice brief (read tool): arXiv 2007.14266; USENIX pang-chengbin, andriesse, basque, burk (dup), schwartz; NDSS DREAM page; dogbolt.org; decompiler-explorer, dewolf, remill (+LIFE_OF_AN_INSTRUCTION.md), rellic, mcsema, retdec, reko, bap repos; Ghidra sleigh.html and pcoderef.html (raw); compiler-explorer README (raw); ACM DL (403); researchr (wrong paper).
- web_search (4 queries): (1) "How Far We Have Come … ISSTA 2020 Liu Wang" → HKUST portal, DecFuzzer; (2) "decompiler correctness benchmark recompilable decompilation evaluation arXiv 2024 2025" → DecompileBench, Decompile-Diverge, Decompile-Bench; (3) "binary lifting validation formal semantics x86-64 lifter testing" → PLDI'20 validator repo, BiNit, No Bit Left Behind, LiftFuzz, ASE'17; (4) "type recovery binary evaluation benchmark ground truth DWARF struct inference" → sefcom types benchmark, decbench, RecStruct, DIRTY.
- Pinning: `git ls-remote HEAD` for 14 repos; arXiv version check by curl of the abs pages (all v1).
- Quote verification: a scripted curl + tag strip + substring match for 27 quotes found 24 exact. The other 3 differ only by stripping spacing (Phoenix, SLEIGH) or were bot-walled on curl (HAL BiNit); those were confirmed against the `read` render.
- Counts: about 38 candidates identified (12 brief items, about 26 from search results), 32 opened, 26 kept, 6 opened and dropped (403, wrong paper, 404, fork, duplicates), about 7 noted but not opened.
- Tools installed or updated: none.
