# bf-source-pack / research-papers (round 73, opened 2026-10-29)

Slice: decompilation / binary-analysis research with durable lessons. Peer de-scope applied (SHOKUNIN_BINARY_FORENSICS IRC): SoK-disassembly, ISSTA decompiler-correctness, SAILR, Kaitai/LIEF/etc. dropped. No tool installed, nothing executed, no sample downloaded. Installs/updates this slice: none.

REA docs read (head): native-function-matching.md, native-investigation.md, ghidra-provider.md, reconstruction-coverage.md, reconstruction-readiness.md, binary-diagnostics.md, reverse-engineering-tools.md. Crosswalk below names only docs whose text I read. No REA doc is about lifting to LLVM IR; those rows say `none`.

Standing caveat for the whole slice: every decompiler/type/name-prediction paper below measures *tool output*, so it grounds a rule that REA pseudocode (`rea decompile`, native-investigation.md) is a hypothesis to check against bytes, not an observation. None of these papers verifies any REA behaviour.

---

## S1 — Phoenix (USENIX Security 2013)
- title: https://www.usenix.org/conference/usenixsecurity13/technical-sessions/presentation/schwartz
- kind: paper
- tier: A (scope: original paper for semantics-preserving control-flow structuring in a native x86 decompiler; 2013 results on 107 GNU coreutils programs)
- scope: claim that structuring algorithms must be semantics-preserving to be safe for decompilation; evaluation numbers are 2013 Hex-Rays vs Phoenix only
- anchor: USENIX Security '13, pp. 353-368, abstract page (citation_publication_date 2013); PDF https://www.usenix.org/system/files/conference/usenixsecurity13/sec13-paper_schwartz.pdf (abstract page opened, not PDF body)
- quote: "existing structuring algorithms are not semantics-preserving, which means that they cannot safely be used for decompilation without modification." (abstract, para 2)
- teaches: separates "recovers more structure" from "recovers it correctly"; an RE agent can ask of any decompiled loop/branch whether the structure was derived under an equivalence-preserving rule or by pattern guess.
- obscurity/value: the origin of "decompiler correctness is a measurable property", the baseline all later fidelity work (Dream, Taxonomy) cites.
- rea-route: native-investigation.md (`rea decompile` pseudocode is advisory; verify against `instructions`).
- limits: abstract only; Hex-Rays version from 2013; says nothing about modern Ghidra; no data/type recovery.

## S2 — No More Gotos / DREAM (NDSS 2015)
- title: https://www.ndss-symposium.org/ndss2015/ndss-2015-programme/no-more-gotos-decompilation-using-pattern-independent-control-flow-structuring-and-semantics/ ; paper PDF https://www.ndss-symposium.org/wp-content/uploads/2017/09/11_4_2.pdf
- kind: paper
- tier: A (scope: original paper for pattern-independent structuring and goto-free output; 7 Feb 2015)
- scope: why goto appears in decompiled output and what a goto-free algorithm costs; comparison numbers are vs Hex-Rays and Phoenix on coreutils in 2015
- anchor: NDSS 2015 briefing paper, PDF page 1 abstract; programme page dated 7 Feb 2015
- quote: "Whenever no match is found, they generate goto statements and thus produce unstructured decompiled output." (abstract)
- teaches: a `goto` or odd loop shape in pseudocode is often a pattern-matching failure of the decompiler, not a property of the original control flow; check the CFG before drawing conclusions about the source.
- obscurity/value: well known but widely mis-cited as a goto-removal "improvement"; the abstract's own caveat (compactness measured in lines of code) is what matters for readers.
- rea-route: native-investigation.md (`decompile`, `instructions`).
- limits: wrong-file traps: .../2017/09/11_4_1.pdf is a different paper (Gyrus); the Uni-Bonn host timed out; the NDSS slide deck is not the paper. "Fewer lines" is not "easier to understand".

## S3 — Polymorphic Type Inference for Machine Code / Retypd (arXiv 1603.05495)
- title: https://arxiv.org/abs/1603.05495
- kind: paper
- tier: A (scope: original type-reconstruction paper for stripped machine code; arXiv v1 17 Mar 2016, page lists v2)
- scope: what type information survives compilation and why recovery needs subtyping + polymorphism; the venue (PLDI 2016) is [INFERENCE] from the briefing, not read on the arXiv page
- anchor: arXiv:1603.05495, abstract; code repo https://github.com/GrammaTech/retypd HEAD 8f7f72be9a567731bb82636cc91d70a3551050bf (2023-04-10), repo not opened beyond SHA
- quote: "Type-unsafe idioms in the original source and type-unsafe optimizations mean that type information in a stripped binary is essentially nonexistent." (abstract)
- teaches: struct/pointer/const types seen in pseudocode are inferred, not recorded; an agent can label a recovered type as "inferred" in the evidence ledger and require a use-site (load/store/call-arg) for each.
- obscurity/value: the best statement of why decompiler types are hypotheses; also explains polymorphism (one routine, many type instantiations).
- rea-route: ghidra-provider.md / native-investigation.md (type recovery is the provider's inference; no REA doc claims otherwise).
- limits: abstract only; 98% const-recall number is a paper-time benchmark, not a Ghidra property.

## S4 — Debin (CCS 2018)
- title: https://files.sri.inf.ethz.ch/website/papers/ccs18-debin.pdf (project page https://jsnice.org/debin.html)
- kind: paper
- tier: A (scope: original paper for ML-predicted names/types in stripped ELF; x86/x64/ARM, 2018 training corpus)
- scope: what "predicted debug information" is and how accurate it was in 2018
- anchor: CCS '18, DOI 10.1145/3243734.3243866, PDF page 1 abstract; repo https://github.com/eth-sri/debin HEAD 715771c1e1468eaafbb599d8bf81a19b5b2e22d2 (2022-05-20), SHA only
- quote: "Given a stripped binary, Debin outputs a binary augmented with the predicted debug information." (abstract)
- teaches: predicted symbol names are probabilistic annotations, never ground truth; if an artifact carries ML-derived names, the ledger must mark them inferred and keep the original bytes/address.
- obscurity/value: formalises names/types/locations as separate prediction targets, a good checklist for what a stripped binary lost.
- rea-route: native-function-matching.md (names establish name correspondence only; here, predicted names establish nothing about original source).
- limits: 68.8% precision / 68.3% recall is x64 on 2018 data; the ACM DL page returned HTTP 403 (see LEADS), so the SRI PDF was opened instead.

## S5 — DIRE (arXiv 1909.09029)
- title: https://arxiv.org/abs/1909.09029
- kind: paper
- tier: A (scope: original paper for neural variable-name recovery from decompiler output; arXiv v1 19 Sep 2019, page lists v2)
- scope: decompiler variable names are synthetic; name recovery quality on a 164,632-binary GitHub corpus
- anchor: arXiv:1909.09029 abstract; repo https://github.com/CMUSTRUDEL/DIRE HEAD 4c66092f52364ae37114f89676c615006e66581d (2021-04-15), SHA only
- quote: "Unfortunately, they do not reconstruct semantically meaningful variable names, which are known to increase code understandability." (abstract)
- teaches: `v3`/`a1` names carry no evidence; any semantic name an agent proposes must cite a use (API call, string, field access) and be flagged as proposed.
- obscurity/value: shows the corpus-building trick (compile with and without symbols to get ground truth), reusable for any "recover X" self-test.
- rea-route: native-function-matching.md (display spelling like `FUN_` does not establish generated-vs-real name; REA says so explicitly).
- limits: 74.3% exact-match is on the paper's own corpus and decompiler; not a Ghidra benchmark.

## S6 — A Taxonomy of C Decompiler Fidelity Issues (USENIX Security 2024)
- title: https://www.usenix.org/conference/usenixsecurity24/presentation/dramko
- kind: paper
- tier: A (scope: original taxonomy of defects in C decompiler output across four decompilers; 2024)
- scope: catalogue of fidelity defects beyond missing names/types, with mitigation directions
- anchor: USENIX Security '24, pp. 379-396, abstract page; PDF https://www.usenix.org/system/files/usenixsecurity24-dramko.pdf (abstract page opened)
- quote: "we use open-coding techniques to identify defects in decompiled code beyond missing names and types" (abstract)
- teaches: gives a defect vocabulary for annotating pseudocode ("this is a decompiler defect class, not program behaviour") before it enters an evidence ledger.
- obscurity/value: the only recent systematic cross-decompiler defect taxonomy; the abstract states it compares four decompilers (the names are in the body, not read).
- rea-route: native-investigation.md / ghidra-provider.md (pseudocode as advisory).
- limits: abstract only; decompiler versions in the study not read; taxonomy completeness not verified.

## S7 — rev.ng: CFG and function-boundary recovery (CC 2017)
- title: https://rev.ng/downloads/cc-2017-paper.pdf
- kind: paper
- tier: A (scope: original paper for architecture-agnostic CFG/function-boundary recovery via QEMU+LLVM IR; 2017 evaluation vs IDA, BAP/ByteWeight, angr)
- scope: why indirect jumps bound static CFG completeness; handling predicated instructions, noreturn, tail calls
- anchor: CC 2017 (venue per ACM DL page, not opened: HTTP 403), PDF section 2.1 "Challenges in CFG recovery"; repo https://github.com/revng/revng HEAD 8c2db55d27d33b50b2e4b23f6b683b1a5ef1321b (2026-10-28), SHA only
- quote: "In general, it is impossible to enumerate the exact set of possible jump targets for indirect control transfers." (section 2.1)
- teaches: a static call/branch trace is a lower bound whenever indirect transfers exist; the agent should record "indirect target set unresolved" rather than claim reachability completeness.
- obscurity/value: clean statement of the three indirect-jump classes (compiler switch, hand-written asm, indirect calls) and which ones a static tool can bound.
- rea-route: native-investigation.md ("Bounded static traces" section title read; body not read).
- limits: x86-64/ARM/MIPS binaries from 2017 compilers; code-vs-data discrimination explicitly out of scope per the paper. A later rev.ng ICCST 2018 paper (https://rev.ng/downloads/iccst-18-paper.pdf) was also opened but is not separately listed.

## S8 — SoK: (State of) The Art of War (IEEE S&P 2016, angr)
- title: https://oaklandsok.github.io/papers/shoshitaishvili2016.pdf
- kind: paper
- tier: A (scope: the angr founding paper; 2016 CGC dataset evaluation of offensive analyses)
- scope: trade-offs between replayability, semantic insight and coverage in automated binary analysis; NOT current angr behaviour (repo HEAD d752a326ebdeecc65bccde605e6a31cc2c2174a1, 2026-10-28, SHA only)
- anchor: S&P 2016 pp.138-157, DOI 10.1109/SP.2016.17, section II.A "Trade-offs" (page 2)
- quote: "For example, high replayability is associated with low coverage." (section II.A)
- teaches: when summarising a symbolic/dynamic trace, say what scope it covers and whether it is replayable; a replayable result covers less, a broad result may be unreplayable false-positive-prone.
- obscurity/value: the frame (replayability, semantic insight) is reusable for deciding whether a static finding needs runtime confirmation; note this lane refuses live-target exploitation, so use it for analysis-trade-off reasoning only, not for its exploit-generation sections.
- rea-route: none.
- limits: offensive-technique oriented; 2016 numbers; the paper-section on exploitation is out of lane scope.

## S9 — BinKit / Revisiting BCSA (arXiv 2011.10749)
- title: https://arxiv.org/abs/2011.10749
- kind: paper
- tier: A (scope: original BCSA benchmark study; arXiv page lists v1-v4, first submitted 21 Nov 2020; published later in TSE per the briefing, not read on this page)
- scope: effect of compiler options and disassembler/tool correctness on binary-similarity results
- anchor: arXiv:2011.10749 abstract; benchmark repo https://github.com/SoftSec-KAIST/BinKit HEAD f6565a37049d94a1835dd8459a9d40460daf7fe0 (2023-12-15), SHA only
- quote: "we show that the way we compile binaries or the correctness of underlying binary analysis tools can significantly affect the performance of BCSA" (abstract)
- teaches: matching/similarity between builds is confounded by compiler, optimisation and tool bugs; any cross-build function pairing must record both toolchains and the disassembler used.
- obscurity/value: the abstract states the authors release all source code and the benchmark, so cross-build matching claims can be re-tested on shared data.
- rea-route: native-function-matching.md (pairs two `list_procedures` inventories; "Exact names establish name correspondence, not unchanged code" - this paper supplies the reasoning why build differences break similarity).
- limits: abstract only; the interpretable model is a research baseline, not a verified matcher for REA.

## S10 — Ghidra SLEIGH language documentation
- title: https://raw.githubusercontent.com/NationalSecurityAgency/ghidra/master/GhidraDocs/languages/html/sleigh.html (also rendered in Ghidra repo at GhidraDocs/languages/html/sleigh.html)
- kind: docs
- tier: A (scope: SLEIGH processor-specification semantics and p-code, as shipped in the Ghidra repo; the document header says "Last updated October 31, 2023")
- scope: how Ghidra's instruction semantics and p-code originate; says nothing about the Ghidra Java/decompiler release behaviour
- anchor: sleigh.html section "History" (and TOC: 1 Introduction to P-Code ... 9 P-code Tables); Ghidra repo HEAD 1b9e58a915cf867e106495eaa2a4b18eb4971c9d (2026-10-27)
- quote: "The main addition of SLEIGH is the ability to provide semantic descriptions of instructions for data-flow and decompilation analysis." (History)
- teaches: wrong decompilation can come from a wrong or missing p-code semantic for one instruction; when pseudocode contradicts disassembly the agent can inspect the language spec rather than trusting either.
- obscurity/value: the primary oracle for what Ghidra believes an instruction does; the History also points to Cifuentes' reverse-compilation thesis as design root.
- rea-route: ghidra-provider.md, ghidra-riscv.md, ghidra-ppc.md, ghidra-mips.md (language/import behaviour; only ghidra-provider.md head was read).
- limits: sections 1-9 body not read beyond the TOC and History; p-code operation semantics not quoted. Sibling-doc, not independently checked against a Ghidra release.

## S11 — remill DESIGN.md (instruction semantics tested against native)
- title: https://raw.githubusercontent.com/lifting-bits/remill/master/docs/DESIGN.md
- kind: docs
- tier: A (scope: maintainer design doc for remill instruction-lifting; AArch64/SPARC/x86 per README)
- scope: how a lifter models machine state/memory and validates semantics; not a claim about any other lifter
- anchor: docs/DESIGN.md section "Instruction semantics"; repo HEAD 56918a8c2554088e93389e97d292f4035286506c (2026-08-27)
- quote: "Instruction semantics are implemented using C++, and tested against their native counterparts." (section "Instruction semantics")
- teaches: the independent-oracle pattern for lifters: compare modelled semantics to execution on real hardware; an agent should demand such a test before trusting a lifted/p-code semantics claim.
- obscurity/value: short, precise design doc for memory-intrinsic deferral and machine-state "tear fields" that explains why lifted IR is not a decompiler output.
- rea-route: none (no REA doc covers LLVM lifting).
- limits: README (read) names McSema as consumer; design doc says nothing about accuracy rates; master branch at fetch time.

## S12 — McSema README (archived)
- title: https://github.com/lifting-bits/mcsema
- kind: tool
- tier: A for "what McSema is and its dependencies", scope: README at commit 26368053f761be05dab708bc28fb97090c64b2be (2022-04-26); repository archived 2022-08-23 (page notice "archived by the owner on Aug 23, 2022")
- scope: lifter architecture and its disassembler dependency; historical, not current
- anchor: README "McSema" intro (two-step process) and "Comparison with other machine code to LLVM bitcode lifters" table
- quote: "Using McSema is a two-step process: control flow recovery, and instruction translation." (intro)
- teaches: separates CFG recovery (IDA Pro dependency) from instruction translation (remill); an agent sees which errors come from which stage.
- obscurity/value: the comparison table is a compact map of the lifter landscape as of 2022 (rev.ng, RetDec, reopt, mctoll, fcd).
- rea-route: none.
- limits: archived read-only; IDA Pro required for control-flow recovery per README; maintenance claims in the table are the authors' own and dated.

## S13 — SoK: Demystifying Binary Lifters (S&P 2022) — artifact README
- title: https://github.com/monkbai/ir_lifting_data
- kind: dataset
- tier: B (scope: authors' S&P 2022 artifact README for four lifters; the paper abstract itself was not opened, see LEADS)
- scope: which lifters/applications the study compared and its own version caveat
- anchor: README top, note under "SoK ... (IEEE S&P 2022 artifacts)"; repo HEAD 4a1726b1a91e84148ff5ca8142d3280972a50f9a (2022-07-29)
- quote: "The results in the paper may not fully reflect the state of each tool at this time." (README note)
- teaches: lifter comparisons are version-bound; an agent citing "lifter X cannot do Y" must name the tool version and date.
- obscurity/value: ships the downstream-application test data (alias_test, ncc_data, decompile_data) and correctness-check scripts; the README names McSema, RetDec, Mctoll, BinRec.
- rea-route: none.
- limits: README only; the "expressiveness vs correctness" framing and the counts come from web-search summaries I did not verify against the paper.

## S14 — Where Did My Variable Go? (ASPLOS 2023, arXiv 2211.09568)
- title: https://arxiv.org/abs/2211.09568
- kind: paper
- tier: A (scope: original paper for completeness-of-debug-information testing in gcc/clang + gdb/lldb; arXiv v1 17 Nov 2022)
- scope: DWARF completeness defects in optimised code; not a method for recovering variables from stripped binaries
- anchor: arXiv:2211.09568 abstract; test repo https://github.com/cristianassaiante/incomplete-debuginfo HEAD 0308e4903543bf5600b8d70f2aab564a183b7e72 (2024-03-04), SHA only
- quote: "empirically derived conjectures on the expected availability of debug information can serve as an effective means to expose classes of these defects" (abstract)
- teaches: when debug info says "optimized out" there is no oracle to say whether the loss was unavoidable; an agent must report absent DWARF locations as unknown, not as absent variables.
- obscurity/value: a forensics-relevant caution about trusting DWARF and gdb output on optimised binaries; applies to crash/triage reasoning.
- rea-route: reverse-engineering-tools.md (objdump `dwarf` operation: "complete raw output is authoritative").
- limits: abstract only; synthetic Csmith programs; 24 confirmed bugs is a point-in-time count.

---

## REJECTED / de-scoped after opening
- REJECTED: NDSS slide deck `.../2017/09/11NoMoreGotos.slide_.pdf` as a Dream source — "Khaled Yakdan (University of Bonn) Dream Decompiler NDSS 2015 1 / 28" (slide footer, pdftotext); flip: only for talk-level material, not for claims.
- REJECTED: https://www.ndss-symposium.org/wp-content/uploads/2017/09/11_4_1.pdf as Dream — opened text starts "Gyrus: A Framework for User-Intent Monitoring of Text-Based Networked Applications"; flip: none (different paper).
- DE-SCOPED (opened, not used, per peer instruction): Andriesse et al. USENIX Sec 2016 (https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/andriesse, abstract: "static disassembly is an unsolved problem") and Pang et al. USENIX Sec 2022 "Ground Truth for Binary Disassembly is Not Easy" (https://www.usenix.org/conference/usenixsecurity22/presentation/pang-chengbin, abstract: "trace the compiling process of the target binaries to collect the ground truth information"). Both are disassembly ground-truth sources; flip: if the disasm-ground-truth peer lane lacks them, include as tier A.

## LEADS (not opened / failed)
- ACM DL Debin page https://dl.acm.org/doi/10.1145/3243734.3243866 — HTTP 403; ACM DL rev.ng page https://dl.acm.org/doi/10.1145/3033019.3033028 — HTTP 403 (venue taken from search summary only).
- https://net.cs.uni-bonn.de/fileadmin/ag/martini/Staff/yakdan/dream_ndss2015.pdf — fetch timed out (replaced by NDSS-hosted PDF).
- https://www.research-collection.ethz.ch/handle/20.500.11850/307507 — HTTP 500.
- https://repository.hkust.edu.hk/ir/Record/1783.1-119386/RDF — timeout; https://www.computer.org/csdl/proceedings-article/sp/2022/131600a453/1FlQDRnPqj6 — page rendered only a JS shell (no abstract text); S&P 2022 lifter SoK abstract unread.
- https://raw.githubusercontent.com/NationalSecurityAgency/ghidra/master/Ghidra/Features/Decompiler/src/decompile/doc/sleigh.xml — empty (the file lives at Ghidra/Features/Decompiler/src/main/doc/sleigh.xml; not opened).
- Not attempted (no URL located/opened): Phoenix PDF body, Retypd PLDI proceedings page, "Type Inference on Executables" (Caballero & Lin), ISSTA 2020 "How Far We Have Come" (de-scoped), compiler-provenance recovery (Rosenblum et al.), Dagger.

## search-log
Where: usenix.org, ndss-symposium.org, arxiv.org, github (gh api for SHAs), jsnice.org, rev.ng, oaklandsok.github.io, ghidra repo docs; 4 web_search queries (Dream URL, Debin URLs, rev.ng URL, angr SoK URL, plus lifter SoK and debug-info paper) used only to locate URLs, never as quotes. identified 20 candidates (14 included + Andriesse, Pang, ISSTA 2020, compiler provenance, Dagger, Caballero-Lin); screened 17 (opened); included 14; rejected 2 (wrong-file Gyrus PDF, slide deck); de-scoped 2 (opened); leads 8 failures/unopened items above.
