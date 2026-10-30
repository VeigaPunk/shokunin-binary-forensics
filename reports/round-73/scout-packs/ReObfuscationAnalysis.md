# ReObfuscationAnalysis — obfuscation, packers, and anti-analysis taxonomy (defensive recognition) + LLM-assisted RE evaluation

Slice owner: REVENGER_SHOKUNIN.ReObfuscationAnalysis. Accessed 2026-10-29. Every row below was opened in this session via `read` (rendered page/PDF/arXiv API) or `curl` + `git ls-remote` for commit pins. No tools were installed or run against artifacts. Nothing under /home/vgpnk/Projects was edited. URLs in /tmp/revenger-existing-urls.txt were skipped. The one arXiv prompt-injection paper already in the corpus (2605.30667, presumed S085) was not re-added; the three prompt-injection rows below are different papers.

Scope guard: rows about protections are kept only as **taxonomies and recognition vocabulary** or **evaluation methodology**. No row is a bypass or unpack how-to for a commercial DRM or protector.

---

## A. Obfuscation and protection taxonomy, and how to evaluate it

ID-SLUG: schrittwieser-csur16-obfuscation-vs-analysis
source: Schrittwieser, Katzenbeisser, Kinder, Merzdovnik, Weippl — "Protecting Software through Obfuscation: Can It Keep Pace with Progress in Code Analysis?", ACM CSUR 49(1):4, 2016 — https://doi.org/10.1145/2886012 (abstract read from TU Wien reposiTUm record https://repositum.tuwien.at/handle/20.500.12708/150118)
kind: paper
tier: A
scope: The survey's own abstract-level claim about how well obfuscation classes hold up against classes of analysis, depending on analyst goals and resources.
anchor: Abstract (reposiTUm DCTERMS.abstract; issued 2016; record available 2023-02-07); accessed 2026-10-29; "many forms of lightweight static analysis have difficulties with even basic obfuscation schemes"
teaches: The strength of an obfuscation is relative to the analyst's method and budget, so a ledger entry should say "resisted analysis X at cost Y" and not "resists analysis".
status: mined
limitation: This is a 2016 survey. It cannot vouch for any modern protector or post-2016 deobfuscation technique, and the full text was not opened (the univie eprint PDF did not respond).
province-fit: in — this is the reference frame for recording obfuscation as an analysis-cost observation.
obscurity: niche

ID-SLUG: desutter-csur24-sp-evaluation-methodologies
source: De Sutter, Schrittwieser, Coppens, Kochberger — "Evaluation Methodologies in Software Protection Research", arXiv:2307.07300v2 (2024-04-30); published ACM CSUR 57(4):86, DOI 10.1145/3702314 — https://arxiv.org/abs/2307.07300v2
kind: paper
tier: A
scope: The survey's meta-analysis of how 571 obfuscation and deobfuscation papers report their evaluations, and its list of nine validity challenges.
anchor: Abstract, v2 (v1 2023-07-14); accessed 2026-10-29; "For 571 papers, we collected 113 aspects of their evaluation methodologies"
teaches: A claim like "deobfuscator D beats obfuscation O" means nothing unless sample set, configuration, and measurement are pinned. The same standard applies to RE evidence fixtures.
status: mined
limitation: It audits how academics evaluate. It does not rank protections or tools.
province-fit: in — directly supports the rules for forged-claim rejection and fixture reproducibility.
obscurity: obscure

ID-SLUG: tigress-academics-config-pinning
source: Tigress C Obfuscator — "For Academics" page (Collberg) — https://tigress.wtf/academics.html (homepage https://tigress.wtf/ lists release 4.2 news)
kind: docs
tier: A
scope: The tool author's own statement on how Tigress output must be configured and reported when used as a test-case generator.
anchor: "For Academics" section, bullet "We run Tigress with default options"; site shows "New in 4.2"; accessed 2026-10-29; "Different options to the same transformation can have radically different performance characteristics."
teaches: When a protector generates a test corpus, the transform script and tool version are part of the evidence. "Obfuscated with Tigress" is not a reproducible label.
status: mined
limitation: This is an author's guidance page. It does not show that any particular Tigress transform resists any analysis.
province-fit: in — Tigress is a legitimate generator of ground-truth obfuscated fixtures (we own the source).
obscurity: niche

ID-SLUG: tigress-antianalysis-transform-catalog
source: Tigress — "Anti Analysis Transformations" catalog page — https://tigress.wtf/antiAnalysis-transforms.html
kind: docs
tier: A
scope: The names and one-line purposes of Tigress's anti-analysis transform families (AntiAliasAnalysis, AntiTaintAnalysis, Opaque Predicate, Implicit Flow).
anchor: Page heading "Anti Analysis Transformations" (Tigress 4.x site); accessed 2026-10-29; "These transformations impede particular program analyses."
teaches: Each anti-analysis transform targets a specific analysis (alias, taint, and so on). Recognition notes should name the analysis that was impeded, not just say "obfuscated".
status: mined
limitation: These are catalog labels only. Identifying a transform in a shipped binary needs separate evidence; the catalog alone is not a detector.
province-fit: in — vocabulary for the inference/unknown ledger fields.
obscurity: niche

ID-SLUG: ollvm-repo-spro15
source: Obfuscator-LLVM — https://github.com/obfuscator-llvm/obfuscator @ 2f19b5073660ec2e3a72f63c2cdb3a681bf4fa35 (citation: Junod et al., "Obfuscator-LLVM — Software Protection for the Masses", SPRO'15, DOI 10.1109/SPRO.2015.10)
kind: code
tier: A
scope: The project's README statement of its current branch and canonical citation at the pinned commit.
anchor: README.md at HEAD 2f19b50; accessed 2026-10-29; "Current version: LLVM-4.0"
teaches: The canonical O-LLVM is frozen at LLVM 4.0. "OLLVM-style" binaries built with modern compilers come from forks, so provenance claims must name the fork.
status: mined
limitation: The README contains no technical description (that is on the wiki, which was not opened). Do not infer which passes or flags exist from this row.
province-fit: in — common fixture generator (BinKit uses its FLA/SUB/BCF passes, see below).
obscurity: mainstream

ID-SLUG: packer-sok-sp15-complexity-types
source: Ugarte-Pedrero, Balzarotti, Santos, Bringas — "SoK: Deep Packer Inspection: A Longitudinal Study of the Complexity of Run-Time Packers", IEEE S&P 2015, DOI 10.1109/SP.2015.46 — https://www.ieee-security.org/TC/SP2015/papers-archived/6949a659.pdf
kind: paper
tier: A
scope: The paper's Type I–VI packer-complexity taxonomy (layers, transitions, isolation, frames, granularity) and its 2007–2014 prevalence table.
anchor: §II "Packer Complexity Types" and Table I (pp. 659–673, 2015); accessed 2026-10-29; "It is important to highlight that the complexity in this taxonomy is computed with respect to the difficulty of retrieving the original application code."
teaches: The usual assumptions are often false: a single dump point, original code in the last layer, a clean tail jump. A memory dump is a time-indexed observation, not "the unpacked binary".
status: mined
limitation: This is a measurement taxonomy from emulator traces (TEMU) on 2007–2014 Windows malware. Its percentages do not transfer to current packers, and it is not an unpacking procedure.
province-fit: in — gives recognition vocabulary for packed-artifact ledger entries without any bypass steps.
obscurity: niche

ID-SLUG: packin-heat-ndss20
source: Aghakhani et al. — "When Malware is Packin' Heat; Limits of Machine Learning Classifiers Based on Static Analysis Features", NDSS 2020, DOI 10.14722/ndss.2020.24310 — https://seclab.cs.ucsb.edu/publications/aghakhani2020_malware_packin_heat/ (PDF https://seclab.cs.ucsb.edu/files/publications/Aghakhani2020_Malware_Packin_Heat.pdf; artifacts ucsb-seclab/packware @ 563e22d9fbe43a075e01287a8a1c0cd411f21a53)
kind: paper
tier: A
scope: The paper's abstract-level finding about what static ML features capture on packed samples.
anchor: Abstract (NDSS, Feb 2020); accessed 2026-10-29; "this information does not necessarily capture the sample’s behavior"
teaches: "Packed" is not "malicious", and a static classifier's verdict on a packed artifact may only reflect the packer. Record packer identity separately from any behavioral claim.
status: mined
limitation: The results concern static-feature ML classifiers in 2020. This row is no evidence about any specific AV product or packer.
province-fit: in — evidence-ledger discipline for triaging packed artifacts.
obscurity: niche

## B. Anti-analysis catalogs (recognition and taxonomy only)

ID-SLUG: attack-t1027-v20
source: MITRE ATT&CK — "Obfuscated Files or Information, Technique T1027" v2.0 (ATT&CK v20) — https://attack.mitre.org/versions/v20/techniques/T1027/
kind: spec
tier: A
scope: ATT&CK's own definition of T1027 and its 18 sub-technique names (e.g., T1027.002 Software Packing, .007 Dynamic API Resolution, .016 Junk Code Insertion) as of v20.
anchor: T1027 page, "Version: 2.0", "Last Modified: 11 September 2026", tactic shown as "Stealth" (TA0005); accessed 2026-10-29; "Payloads may also be split into separate, seemingly benign files that only reveal malicious functionality when reassembled."
teaches: Use the stable sub-technique IDs as labels for an observed anti-analysis trait. In v20 the tactic label for TA0005 appears as "Stealth", so labels must be pinned to an ATT&CK version.
status: mined
limitation: The procedure examples are vendor-report citations that ATT&CK did not verify. Do not use them as byte-level evidence of any family's behavior.
province-fit: adjacent — used as a taxonomy key, not as a threat-intel source.
obscurity: mainstream

ID-SLUG: capec-188-reverse-engineering
source: MITRE CAPEC — "CAPEC-188: Reverse Engineering" (CAPEC List Version 3.9) — https://capec.mitre.org/data/definitions/188.html
kind: spec
tier: A
scope: CAPEC's meta-level definition of reverse engineering, its white-box/black-box children (CAPEC-167, CAPEC-189), and the listed mitigation.
anchor: "Example Instances" section; content history 2023-01-24 (Version 3.9); accessed 2026-10-29; "'Black Box' methods involve interacting with the software indirectly, in the absence of the ability to measure, instrument, or analyze an executable object directly."
teaches: CAPEC treats RE as an adversary attack pattern and lists obfuscation as its mitigation. That framing matters when explaining scope and refusals: our lane covers white-box artifact analysis only.
status: mined
limitation: This is a classification entry, not a method. "Likelihood Of Attack: Low" is MITRE's rating and is not an observation.
province-fit: adjacent — useful for wording scope and refusals.
obscurity: niche

ID-SLUG: unprotect-project-evasion-db
source: Unprotect Project — evasion technique database (Roccia, Lesueur) — https://unprotect.it/about/ (index https://unprotect.it/)
kind: community
tier: C
scope: The project's self-description and its counts at the time of access: 376 techniques with U-IDs, 242 snippets, 160 detection rules.
anchor: About page, "Platform Version: 7.0.7 / Last Update: 2026-03-30"; accessed 2026-10-29; "The goal of this free database is to centralize the information about malware evasion techniques."
teaches: A community catalog with per-technique U-IDs and YARA rules (e.g., "Detect Disassembly Obfuscation Rogue Byte") is a lead index for naming an anti-analysis trait. It does not confirm the trait.
status: mined
limitation: Entries are contributed and not peer-reviewed, and snippets are offensive PoCs. Cite only technique names and detection rules, never snippet code.
province-fit: adjacent — recognition vocabulary only.
obscurity: niche

ID-SLUG: checkpoint-evasions-antidebug-flags
source: Check Point Research — "Evasion techniques" encyclopedia, Anti-Debug: Debug Flags — https://evasions.checkpoint.com/src/Anti-Debug/techniques/debug-flags.html (source repo CheckPointSW/Evasions @ 9d31a14ffe7dc5e05d38aac5f5f10503b9967751)
kind: docs
tier: C
scope: The vendor's catalog page enumerating Windows debug-flag checks (IsDebuggerPresent, NtQueryInformationProcess classes 7/0x1f/0x1e, PEB BeingDebugged, NtGlobalFlag, heap flags, KUSER_SHARED_DATA), each with a "Mitigations" subsection.
anchor: "Debug Flags" intro; article published 2024-07-10; accessed 2026-10-29; "The states of these flags can be verified either by using specific API functions or examining the system tables in memory."
teaches: Anti-debug checks show up statically as specific API imports or resolved names plus PEB/heap field offsets. That gives byte-checkable recognition anchors (e.g., ProcessInformationClass 0x1f) for a ledger.
status: mined
limitation: This is a vendor research catalog of Windows-only checks. The "Mitigations" sections are debugger-hiding advice, which is outside this lane's static scope. Do not cite them as procedure.
province-fit: adjacent — the static-recognition part is in scope; the mitigation part is out.
obscurity: niche

ID-SLUG: al-khaser-check-catalog
source: al-khaser v0.81 — https://github.com/ayoubfaouzi/al-khaser @ f0e5559073fe02c4f50cc8c3ed8d5b302a6a0659
kind: code
tier: A
scope: The README's enumerated list of anti-debug, anti-injection, anti-dump, timing, anti-VM, and anti-disassembly check names at the pinned commit.
anchor: README "Introduction" and "Features" (Al-Khaser v0.81); accessed 2026-10-29; "It performs a bunch of common malware tricks with the goal of seeing if you stay under the radar."
teaches: An executable, named list of checks gives a cross-reference vocabulary for anti-analysis traits found during static triage, e.g., "Interrupt 0x2d", "PAGE_GUARD memory breakpoints".
status: mined
limitation: It is a PoC test binary for analysis labs. Running it or hardening a sandbox against it is outside the static, artifact-first province. Use the README as a name catalog only.
province-fit: adjacent — the catalog is useful; the execution use case is out.
obscurity: mainstream

## C. Deobfuscation by synthesis and algebra (checkable benchmarks)

ID-SLUG: syntia-usenix17
source: Blazytko, Contag, Aschermann, Holz — "Syntia: Synthesizing the Semantics of Obfuscated Code", USENIX Security 2017, pp. 643–659 — https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/blazytko (code RUB-SysSec/syntia @ 36028935cac1a62a8909c1e46a1d818b7c2a43b4)
kind: paper
tier: A
scope: The paper's abstract-level results for MCTS-guided program synthesis on MBA expressions and VM handlers.
anchor: USENIX abstract page (Aug 2017); accessed 2026-10-29; "we automatically learn the semantics of 489 out of 500 random expressions obfuscated via Mixed Boolean-Arithmetic"
teaches: Black-box I/O synthesis gives a semantics hypothesis for a trace window. In a ledger it is an inference that needs an equivalence check before it becomes an observation.
status: mined
limitation: Its handler results on VMProtect/Themida are research measurements on 2017 versions. This row carries no claim about current protectors and no procedure for them.
province-fit: in — semantic recovery from owned or authorized artifacts.
obscurity: niche

ID-SLUG: xyntia-ccs21
source: Menguy, Bardin, Bonichon, de Souza Lima — "AI-based Blackbox Code Deobfuscation: Understand, Improve and Mitigate", arXiv:2102.04805v1 (published as "Search-Based Local Black-Box Deobfuscation", ACM CCS 2021, DOI 10.1145/3460120.3485250) — https://arxiv.org/abs/2102.04805v1 (code binsec/xyntia @ fb3017f54d6b59aedc54f76c16c1cb2a6006d758)
kind: paper
tier: A
scope: The abstract's framework for black-box deobfuscation and its claim that S-metaheuristics (ILS) beat MCTS.
anchor: Abstract, v1 2021-02-09; accessed 2026-10-29; "we are the first to point out that the search space underlying code deobfuscation is too unstable for simulation-based methods"
teaches: Synthesis-based deobfuscators have known countermeasures (the paper proposes two). A synthesis failure is therefore an "unknown", not evidence that no simple semantics exists.
status: mined
limitation: The arXiv title differs from the CCS title, so cite both. The success rates are on the authors' benchmarks.
province-fit: in
obscurity: niche

ID-SLUG: qsynthesis-repo-bar20
source: QSynthesis (Quarkslab), implementing "QSynth — A Program Synthesis based approach for Binary Code Deobfuscation" (David, Coniglio, Ceccato; NDSS BAR 2020; https://www.ndss-symposium.org/ndss-paper/auto-draft-90/) — https://github.com/quarkslab/qsynthesis @ 44e7318200f8ce1dd0fd79a849d2c68e9a3694bc
kind: code
tier: A
scope: The repo README's statement of the greybox algorithm (I/O oracle tables plus AST search), its SMT equivalence check, and its stated limitations.
anchor: README "Limitations"; HEAD 44e7318; accessed 2026-10-29; "synthesis accuracy limited by pre-computed tables exhaustivness"
teaches: Synthesis output should go into the ledger together with the oracle table's grammar and size, and the SMT-equivalence result should be recorded as a separate observation.
status: mined
limitation: The README marks the code experimental, and trace-based synthesis is disabled. The paper PDF on NDSS returned HTML (not opened), so this row supports no paper numbers.
province-fit: in
obscurity: obscure

ID-SLUG: mba-blast-usenix21
source: Liu, Shen, Ming, Zheng, Li, Xu — "MBA-Blast: Unveiling and Simplifying Mixed Boolean-Arithmetic Obfuscation", USENIX Security 2021, pp. 1701–1718 — https://www.usenix.org/conference/usenixsecurity21/presentation/liu-binbin (code softsec-unh/MBA-Blast @ ceb12c28ac25ada0b5b9f3ffbf4dcec8e8fa3c39)
kind: paper
tier: A
scope: The abstract's claimed 1-bit/n-bit property of linear MBA, proven in the paper, and its evaluation on about 10,000 expressions. The paper passed USENIX Artifact Evaluation.
anchor: USENIX abstract page (Aug 2021; badge "Artifact Evaluation Passed"); accessed 2026-10-29; "Our key insight is that MBA transformations behave in the same way on 1-bit and n-bit variables."
teaches: Simplifying linear MBA has a proof-backed normal form, so a simplified expression can be checked byte-for-byte or by SMT instead of being trusted.
status: mined
limitation: The property applies to linear MBA. It is not a claim about polynomial or non-linear MBA, or about arbitrary bit-vector code.
province-fit: in
obscurity: niche

ID-SLUG: loki-hardening-obfuscation
source: Schloegel, Blazytko, Contag, Aschermann, Basler, Holz, Abbasi — "Technical Report: Hardening Code Obfuscation Against Automated Attacks", arXiv:2106.08913v3 (Loki; USENIX Security 2022) — https://arxiv.org/abs/2106.08913v3
kind: paper
tier: A
scope: The abstract's claim about Loki's resistance to known automated deobfuscation and its measured effect on program synthesis.
anchor: Abstract, v3 (latest listed); accessed 2026-10-29; "Loki protects against previously unaccounted attack vectors such as program synthesis, for which it reduces the success rate to merely 19%."
teaches: Each deobfuscation method has a published countermeasure. A ledger should record which method failed on which construct and not generalize to "undeobfuscatable".
status: mined
limitation: The work is from the protection side. The 19% figure is the authors' measurement against their chosen attackers.
province-fit: adjacent — informs the limits of recognition; we do not build protections.
obscurity: niche

## D. Binary similarity and decompiler-output ground truth

ID-SLUG: binkit-tse22-bcsa-lessons
source: Kim, Kim, Cha, Son, Kim — "Revisiting Binary Code Similarity Analysis using Interpretable Feature Engineering and Lessons Learned", arXiv:2011.10749v4 (IEEE TSE 2022, DOI 10.1109/TSE.2022.3187689) — https://arxiv.org/abs/2011.10749v4
kind: paper
tier: A
scope: The abstract's lessons on BCSA reproducibility and the effects of compiler options and tool correctness.
anchor: Abstract, v4 ("accepted to IEEE Transactions on Software Engineering (June 2022)"); accessed 2026-10-29; "we show that the way we compile binaries or the correctness of underlying binary analysis tools can significantly affect the performance of BCSA."
teaches: A similarity score depends on the toolchain and on the disassembler underneath. Record both as part of any "function X matches Y" claim.
status: mined
limitation: The headline about simple models matching deep ones applies only to the paper's benchmark and features.
province-fit: in
obscurity: niche

ID-SLUG: binkit-readme-dataset
source: BinKit 2.0 README — https://github.com/SoftSec-KAIST/BinKit/blob/f6565a37049d94a1835dd8459a9d40460daf7fe0/README.md
kind: dataset
tier: A
scope: The dataset's own statement of compiler, architecture, and optimization coverage (1,904 combinations, 371,928 binaries), its O-LLVM FLA/SUB/BCF variants, and its known missing binaries.
anchor: README "BinKit 2.0" and "Missing binaries" at f6565a3; accessed 2026-10-29; "In Binkit 2.0 dataset, the gsl package misses 8 binaries with Ofast option due to compiler bugs."
teaches: A ground-truth corpus generated by a matrix of compilers and obfuscators is the right shape for byte-oracle fixtures, and its documented holes must be carried into any coverage claim.
status: mined
limitation: The dataset downloads are Google Drive links that were not fetched or hashed. The counts are as stated in the README and were not verified.
province-fit: in — a source of labelled obfuscated and unobfuscated fixtures.
obscurity: niche

ID-SLUG: dire-ase19
source: Lacomis et al. — "DIRE: A Neural Approach to Decompiled Identifier Naming", arXiv:1909.09029v2 (ASE 2019) — https://arxiv.org/abs/1909.09029v2
kind: paper
tier: A
scope: The abstract's corpus construction (164,632 x86-64 binaries) and its exact-match name accuracy.
anchor: Abstract, v2; accessed 2026-10-29; "DIRE can predict variable names identical to the names in the original source code up to 74.3% of the time."
teaches: Recovered identifiers are model predictions. A ledger must label them as inference and never as the original names.
status: mined
limitation: VarBERT (row below) reports that DIRE drops to 31.8% on functions not seen in training, so the 74.3% figure overstates generalization.
province-fit: in
obscurity: niche

ID-SLUG: dirty-usenix22
source: Chen, Lacomis, Schwartz, Le Goues, Neubig, Vasilescu — "Augmenting Decompiler Output with Learned Variable Names and Types" (DIRTY), arXiv:2108.06363v1 (USENIX Security 2022) — https://arxiv.org/abs/2108.06363v1 (code CMUSTRUDEL/DIRTY @ 5f8e9494d52ef8788f0834342097f36462eeb2eb)
kind: paper
tier: A
scope: The abstract's statement of what decompilers can and cannot recover, and DIRTY's name and type accuracy on its dataset.
anchor: Abstract, v1 2021-08-13; accessed 2026-10-29; "comments, variable names, and custom variable types are technically impossible to recover."
teaches: Names, comments, and custom types never come from the bytes. Any such value in a report is a model or analyst inference and must carry provenance.
status: mined
limitation: The 66.4%/75.8% figures include functions seen in training (see VarBERT).
province-fit: in
obscurity: niche

ID-SLUG: varbert-sp24
source: Pal, Bajaj, et al. — "'Len or index or count, anything but v1': Predicting Variable Names in Decompilation Output with Transfer Learning" (VarBERT), IEEE S&P 2024, DOI 10.1109/SP54263.2024.00152 — https://sefcom.asu.edu/publications/varbert-oakland24.pdf (code sefcom/VarBERT @ 76f221a5e0af43a36169818cbbfd6e8dd3c98cdc)
kind: paper
tier: A
scope: The paper's abstract-level critique of DIRE/DIRTY generalization and VarBERT's accuracies on VarCorpus (IDA/Ghidra, O2).
anchor: Abstract (S&P 2024 author PDF); accessed 2026-10-29; "generalize poorly to functions in the testing set that are not included in the training set"
teaches: Evaluating RE-assist models on functions overlapping the training set inflates scores. Fixture splits must exclude seen functions before any accuracy is cited.
status: mined
limitation: Its accuracy numbers (54.43% IDA / 54.49% Ghidra at O2) are exact-match on VarCorpus only. The paper also notes semantically valid alternative names.
province-fit: in
obscurity: niche

## E. LLM-assisted RE and deobfuscation evaluation

ID-SLUG: degpt-ndss24
source: Hu, Liang, Chen — "DeGPT: Optimizing Decompiler Output with LLM", NDSS 2024 — https://www.ndss-symposium.org/ndss-paper/degpt-optimizing-decompiler-output-with-llm/ (code PeiweiHu/DeGPT @ 0f632cc52fabd70c7e7b3b9ad1ed7aef517a3714)
kind: paper
tier: A
scope: The abstract's three-role design (referee/advisor/operator) and its readability and comment-usefulness metrics on Ghidra output.
anchor: NDSS paper page abstract (modified 2024-10-15); accessed 2026-10-29; "R_ope inspects whether the optimization changes the original function semantics and concludes the final verdict about whether to accept the optimizations"
teaches: The semantic-preservation check in DeGPT is itself an LLM verdict. Treat LLM-cleaned decompiler output as inference unless the semantics are checked by a non-LLM oracle.
status: mined
limitation: The 24.4% "cognitive burden" reduction and the 62.9% useful comments are readability measures, not correctness.
province-fit: in
obscurity: niche

ID-SLUG: decompilebench-gao25
source: Gao et al. — "DecompileBench: A Comprehensive Benchmark for Evaluating Decompilers in Real-World Scenarios", arXiv:2505.11340v1 — https://arxiv.org/abs/2505.11340v1 (code Jennieett/DecompileBench @ 761c6513b10344f502474f3e5e78c74fd89ab839)
kind: paper
tier: A
scope: The benchmark design (23,400 functions from 130 programs, runtime-aware validation, LLM-as-judge) and its headline comparison of six decompilers with six LLM approaches.
anchor: Abstract, v1 2025-05-16; accessed 2026-10-29; "LLM-based methods surpass commercial tools in code understandability despite 52.2% lower functionality correctness."
teaches: Readability and correctness diverge, and LLM output wins on the wrong axis. Ledger fixtures must score re-executability separately from "looks right".
status: mined
limitation: The understandability score comes from an LLM-as-judge. It is not human ground truth. This is a different paper from Decompile-Bench (next row).
province-fit: in
obscurity: niche

ID-SLUG: decompile-bench-tan25
source: Tan et al. — "Decompile-Bench: Million-Scale Binary-Source Function Pairs for Real-World Binary Decompilation", arXiv:2505.12668v2 — https://arxiv.org/abs/2505.12668v2 (HF collection LLM4Binary/decompile-bench; code albertan017/LLM4Decompile @ 85b364bf093eb2ee4f3687cfe38a203fca89f23e)
kind: dataset
tier: A
scope: The dataset's construction (2M pairs condensed from 100M) and its leakage-mitigation design for Decompile-Bench-Eval.
anchor: Abstract, v2 (latest listed; v1 2025-05-19); accessed 2026-10-29; "compiled GitHub repositories released after 2025 to mitigate data leakage issues"
teaches: When evaluating an LLM decompiler, test only on code published after the model's training cutoff. Without that, re-executability gains may be memorization.
status: mined
limitation: The "20% improvement" is in the re-executability rate for the authors' fine-tune. The HF data was not downloaded or checked. This is distinct from the LLM4Decompile paper already in the corpus (2403.05286).
province-fit: in
obscurity: niche

ID-SLUG: bindeobfbench-2026
source: Hu et al. — "Can LLMs Deobfuscate Binary Code? A Systematic Analysis of Large Language Models into Pseudocode Deobfuscation" (BinDeObfBench), arXiv:2604.08083v1 — https://arxiv.org/abs/2604.08083v1
kind: paper
tier: A
scope: The benchmark's coverage of pre-compile, compile-time, and post-compile obfuscations, and its abstract-level findings on reasoning models vs. model scale.
anchor: Abstract, v1 2026-04-09; accessed 2026-10-29; "deobfuscation performance depends more on reasoning capability and domain expertise than on model scale"
teaches: LLM deobfuscation claims need the obfuscation stage, the ISA, and the optimization level pinned. Model size is not a proxy for reliability.
status: mined
limitation: This is a v1 preprint with no venue yet. The findings are aggregate and not per-transform guarantees.
province-fit: in
obscurity: obscure

ID-SLUG: deconstructing-obfuscation-llm-2025
source: Tkachenko, Suskevic, Adolphi — "Deconstructing Obfuscation: A four-dimensional framework for evaluating Large Language Models assembly code deobfuscation capabilities", arXiv:2505.19887v2 — https://arxiv.org/abs/2505.19887v2
kind: paper
tier: A
scope: The paper's resistance tiers for O-LLVM-style transforms (BCF low, CFF moderate, SUB/combined high) and its five named LLM error patterns.
anchor: Abstract, v2; accessed 2026-10-29; "Universal failure against combined techniques demonstrates that sophisticated obfuscation remains effective against advanced LLMs."
teaches: The named error patterns (predicate misinterpretation, constant-propagation errors, and others) give a checklist for rejecting forged or LLM-hallucinated claims about obfuscated code.
status: mined
limitation: Seven commercial models at one point in time. The tier ranking is not stable across model generations.
province-fit: in
obscurity: obscure

ID-SLUG: jsdeobsbench-ccs25
source: Chen, Jin, Lin — "JsDeObsBench: Measuring and Benchmarking LLMs for JavaScript Deobfuscation", arXiv:2506.20170v1 (ACM CCS 2025) — https://arxiv.org/abs/2506.20170v1
kind: paper
tier: A
scope: The benchmark's abstract-level finding on how LLMs trade simplification against syntax and execution correctness when deobfuscating JavaScript.
anchor: Abstract, v1 2025-06-25 ("Accepted by ACM CCS 2025"); accessed 2026-10-29; "revealing superior performance in code simplification despite challenges in maintaining syntax accuracy and execution reliability compared to baseline methods"
teaches: For Electron/JS artifacts, LLM-deobfuscated output must be run or parsed against the original before any behavior claim is recorded.
status: mined
limitation: Model list as of 2025 (GPT-4o, Mixtral, Llama, DeepSeek-Coder). The JS-malware subset is a demonstration, not a census.
province-fit: in — Electron/JS is a province target.
obscurity: niche

## F. Adversarial inputs to LLM-assisted RE (beyond the corpus's existing compiled-string prompt-injection paper)

ID-SLUG: rare-bench-representation-confusion
source: Santos-Grueiro — "When Binaries Talk Back: Representation-Confusion Attacks on LLM-Assisted Reverse Engineering" (RARE-Bench / RARE-Guard), arXiv:2607.12507v1 — https://arxiv.org/abs/2607.12507v1
kind: paper
tier: A
scope: The paper's measured failures where binary-derived data gains instruction or evidence authority, and its Tool Authorization / Provenance Gate controls, across Ghidra, r2pipe, and angr.
anchor: Abstract, v1 2026-07-14 (20 pages); accessed 2026-10-29; "Binary-derived content may therefore guide analysis without gaining authority over tools, and views from several tools do not necessarily provide independent evidence."
teaches: Records from several tools that come from one origin must be grouped before support is counted. In fused drafts a naive support gate validated 32/32 false claims, and a provenance gate validated 0/32.
status: mined
limitation: Single-author v1 preprint with small program sets (20 + 16) and two models. The control results are the author's own measurements.
province-fit: in — directly specifies an evidence-ID provenance rule for the ledger.
obscurity: obscure

ID-SLUG: alibi-legitimacy-injection
source: Choi, Jung, Seo, Nam — "ALIBI: Adversarial Legitimacy Injection in Binary Input against LLM Malware Analyzers", arXiv:2609.19722v1 — https://arxiv.org/abs/2609.19722v1
kind: paper
tier: A
scope: The paper's measured verdict flips from a non-executed, read-only "cover story" section added to PE/ELF binaries, and its defense-prompt result.
anchor: Abstract, v1 2026-09-17 (12 pages); accessed 2026-10-29; "LLM malware analyzers therefore require provenance checks that separate verified facts from attacker-controlled claims, not narrative trust."
teaches: Strings and embedded narratives inside an artifact are attacker-controlled observations. They must never be promoted to explanations of the artifact's behavior.
status: mined
limitation: Frozen 50-PE / 40-ELF sets on named 2026 models. Flip rates (30/35 on Gemini 2.5 Pro) are model- and prompt-specific.
province-fit: in — a forged-claim rejection control.
obscurity: obscure

ID-SLUG: pi-detection-re-agents
source: Crawford, McClure — "Investigating Detection and Obfuscation of Prompt Injection Attacks Against Software Reverse Engineering AI Agents", arXiv:2605.30677v1 — https://arxiv.org/abs/2605.30677v1
kind: paper
tier: A
scope: The abstract-level statement that the paper studies detecting prompt-injection strings in decompiler output, plus obfuscated variants of those strings.
anchor: Abstract, v1 2026-05-29; accessed 2026-10-29; "This research demonstrates defensive tactics for detecting the presences of prompt injection strings in the decompiler output of adversarial example programs."
teaches: Detection of injected strings can itself be evaded by obfuscation. String-level filtering is a weak control compared with data-only rendering plus authorization (see the RARE row).
status: mined
limitation: The abstract gives no metrics, and the full text was not opened. This is the defensive companion to 2605.30667, which is already in the corpus.
province-fit: in
obscurity: obscure

---

## Screened and dropped leads

- http://profs.sci.univr.it/~giaco/download/Watermarking-Obfuscation/Obfuscation%20Taxonomy.pdf (Collberg/Thomborson/Low 1997 TR148): the PDF is an image scan with no extractable text, and the ResearchSpace record (hdl 2292/3491) rendered empty. No verbatim quote could be taken. Flip condition: an OCR'd copy or a working record page.
- https://eprints.cs.univie.ac.at/7012/1/3465481.3465772.pdf (Kochberger et al., "SoK: Automatic Deobfuscation of Virtualization-protected Applications", ARES 2021): the host did not respond or returned nothing. Flip condition: open via the ACM DOI 10.1145/3465481.3465772. It is also close to a VM-protector devirtualization procedure, so mine only its classification scheme.
- https://eprints.cs.univie.ac.at/6372/1/ProtectingSoftwareThroughObfuscation.pdf: unreachable. The abstract was mined from the reposiTUm record instead (row above).
- https://www.ndss-symposium.org/wp-content/uploads/2020/04/bar2020-23009-paper.pdf (QSynth paper): returned HTML, not a PDF. It is covered by the qsynthesis README row, and no paper numbers were claimed.
- https://arxiv.org/abs/2310.06530 ("Refining Decompiled C Code with Large Language Models", v2): only the title was confirmed by curl and the abstract was not read. It overlaps the DeGPT and DecompileBench rows, so it was left as a lead.
- https://arxiv.org/abs/2511.19130 (LLM program-semantics recovery with KLEE): seen only in search. It works on source-level C, not binary input, so it is weaker fit.
- https://arxiv.org/abs/2605.30667: already in the corpus (prompt-injection attack on RE agents). Skipped per rule 3.
- https://attack.mitre.org/techniques/T1027/002/ (Software Packing): not opened separately. It is covered by the T1027 v20 row's sub-technique list.
- https://github.com/obfuscator-llvm/obfuscator/wiki: not opened. The O-LLVM row deliberately makes no pass-level claims.
- MITRE ATT&CK "Defense Evasion": in v20, TA0005 is displayed as "Stealth" on T1027, so no separate tactic row was made.

## Search log

- web_search (6 queries in batch 1): Xyntia arXiv; DeGPT NDSS 2024; Decompile-Bench arXiv; Schrittwieser CSUR DOI; BinKit/BCSA TSE; LLM deobfuscation benchmark 2025. These surfaced 2102.04805, NDSS DeGPT, 2505.12668 vs 2505.11340, DOI 10.1145/2886012, 2011.10749, 2604.08083, 2505.19887, and 2506.20170.
- web_search (6 queries in batch 2): De Sutter evaluation methodologies; SoK Deep Packer Inspection; VarBERT S&P 2024; QSynth BAR 2020; Collberg taxonomy TR148; prompt injection in RE agents. These surfaced 2307.07300, the S&P 2015 PDF, the sefcom PDF, the NDSS BAR page plus quarkslab/qsynthesis, the univr scan, 2605.30677, 2607.12507, and 2609.19722.
- web_search (3 more): Packin' Heat NDSS 2020; MBA-Blast USENIX 2021; Kochberger VM-deobfuscation SoK.
- Direct fetches (read/curl): tigress.wtf (home, academics, antiAnalysis), obfuscator-llvm repo, unprotect.it (home, about), evasions.checkpoint.com (home, anti-debug index, debug-flags), al-khaser, attack.mitre.org T1027, capec 188, 16 arXiv abstract pages (versions via curl of abs HTML), USENIX Syntia and MBA-Blast pages, NDSS QSynth and DeGPT pages, IEEE S&P 2015 PDF, UCSB SecLab page plus PDF, sefcom VarBERT PDF, reposiTUm Schrittwieser record, and the BinKit README at a pinned commit. Commits were pinned with `git ls-remote` for 15 repos.
- Counts: about 45 candidates identified; 39 URLs screened or opened; 30 rows kept (all opened this session); 10 screened and dropped or deferred (above).
- Installs/updates: none.
