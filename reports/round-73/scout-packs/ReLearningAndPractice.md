# ReLearningAndPractice — learning path, practice corpora, books, talks, community ground truth

Slice owner: REVENGER_SHOKUNIN.ReLearningAndPractice · accessed 2026-10-29 · all rows below were opened this session (read tool or curl); quotes copied from the fetched text.
Skip-list `/tmp/revenger-existing-urls.txt` checked: no row duplicates a listed URL.
Installs/updates: none.

Legend used in `anchor`: pin = the revision/commit/date the page or repo exposed at fetch time.

---

## A. Ground-truth instruction semantics and ABI (spec / docs)

ID-SLUG: intel-sdm-index
source: Intel® 64 and IA-32 Architectures Software Developer Manuals (index page, ID 767375) — https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html
kind: spec
tier: A
scope: Intel's own statement of which SDM volume set and version is current, and what each volume covers (Vol 2 = instruction set reference A–Z); this row does not cover the PDF bodies
anchor: Overview section; page "Updated 10/9/2026", SDM PDFs at version 093; accessed 2026-10-29; "The downloadable PDFs of all IA-32 Architectures Software Developer's Manual volumes are at version 093."
teaches: An instruction-semantics claim in a ledger should cite the SDM by volume and version number (here 093), because Intel ships documentation-change errata between versions.
status: mined
limitation: The index page only lists documents; it does not show that any given decoder or lifter matches the SDM.
province-fit: in — x86/x64 instruction semantics are the oracle for native-binary disassembly claims.
obscurity: mainstream

ID-SLUG: amd-apm-40332
source: AMD64 Architecture Programmer's Manual, Volumes 1–5, pub. 40332 rev 4.10 — https://docs.amd.com/v/u/en-US/40332_4.10_APM_Vol1-5_PUB
kind: spec
tier: A
scope: AMD's combined APM PDF (rev 4.10, July 2026; Vol 1 = pub 24592 rev 3.25, May 2026), as a vendor reference for AMD64 instruction and system semantics
anchor: Front matter, legal page p.2 of PDF fetched via docs.amd.com khub API (document SLs_hsYJwsu9rrIjE0rGxA, Release_Date 2026-07-29, 24,737,536 bytes, sha256 b95c6db015807bf38daed8cc0c294c42e479c42c62cf25655661754d21f591db); accessed 2026-10-29; "Reverse engineering or disassembly is prohibited."
teaches: A vendor "ground truth" manual has its own license terms and a separate revision number for each volume, so a citation needs the publication number, the revision, and the file hash; the HTML portal shell alone shows none of this.
status: mined
limitation: That legal sentence is product boilerplate about AMD products, not a statement on studying third-party binaries; it does not settle any legality question.
province-fit: in — the second x86-64 vendor oracle; Intel/AMD differences (e.g. extensions only one vendor has) are checkable here.
obscurity: niche

ID-SLUG: arm-arm-ddi0487-md
source: Arm® Architecture Reference Manual for A-profile architecture, ARM DDI 0487 issue M.d — https://support.arm.com/documentation/ddi0487/latest (metadata via https://documentation-service.arm.com/documentation/ddi0487/md?lang=en)
kind: spec
tier: A
scope: Arm's statement of the current Arm ARM issue (M.d, EAC, non-confidential) and which format counts as authoritative
anchor: Title/preface topic of ddi0487 version "md" (versionLabel M.d), JSON topic body decoded; accessed 2026-10-29; "In the event of any differences between the PDF and HTML versions, the PDF version shall be considered the authoritative reference."
teaches: Even inside one vendor document the formats rank differently (PDF over HTML preview, plus a known-issues document updated monthly), so the ledger should cite the PDF issue letter, not a web anchor.
status: mined
limitation: Covers A-profile Armv8/Armv9 only; it says nothing about M-profile firmware targets or vendor-specific extensions.
province-fit: in — the AArch64/AArch32 semantics oracle for Android native libraries and firmware.
obscurity: mainstream

ID-SLUG: agner-calling-conventions
source: Agner Fog, Software optimization resources — manual 5 "Calling conventions for different C++ compilers and operating systems" — https://www.agner.org/optimize/
kind: docs
tier: A
scope: The author's own description of what the five manuals cover and their epistemic status; calling_conventions.pdf last modified 2023-Jul-01, instruction_tables.pdf 2025-Sep-20, microarchitecture.pdf 2026-May-23
anchor: "Optimization manuals" section, item 5; accessed 2026-10-29; "The information provided here is based on my own research and therefore descriptive rather than normative."
teaches: Name-mangling and register-usage facts drawn from a measured, descriptive source get logged as observations with that provenance, not as ABI-normative facts.
status: mined
limitation: Being descriptive, it can lag or disagree with official psABI/MSVC documents; where the two conflict, cite the normative ABI.
province-fit: in — calling conventions and mangling schemes across compilers are central to native function-boundary and signature recovery.
obscurity: niche

ID-SLUG: uops-info
source: uops.info — Latency, Throughput, and Port Usage Information (Andreas Abel) — https://uops.info/
kind: dataset
tier: A
scope: The project's own claim about its coverage (>800,000 pages) and that it offers a machine-readable XML of instruction operands and measurements
anchor: Landing page, "Latency, Throughput, and Port Usage Information" section, no version shown; accessed 2026-10-29; "most of it is not documented in the official processor manuals."
teaches: Measured per-microarchitecture data and a machine-readable operand list can serve as an independent cross-check of decoder operand tables, distinct from the vendor manuals.
status: mined
limitation: It measures performance on Intel/AMD microarchitectures; it does not define architectural semantics, so it cannot override the SDM/APM.
province-fit: adjacent — useful as an operand/encoding cross-check, not primarily an RE source.
obscurity: niche

ID-SLUG: sandpile-x86
source: sandpile.org — technical x86 processor information (Christian Ludloff) — https://www.sandpile.org/
kind: docs
tier: C
scope: An index of opcode maps (1-, 2-, 3-byte, map 4/APX), ModR/M and SIB tables, CPUID and MSR pages maintained by one author; this row covers only the index page
anchor: Home page header; "© 1996-2026"; accessed 2026-10-29; "The world's leading source for technical x86 processor information."
teaches: Single-maintainer opcode maps are useful for locating encodings quickly, but the ledger should then confirm each encoding against the SDM/APM before recording it as an observation.
status: mined
limitation: The quoted line is the site's own self-description, not an independent quality assessment, and the page states no revision for its tables.
province-fit: in — opcode/encoding lookup for x86 decoding claims.
obscurity: obscure

ID-SLUG: hackers-delight-2e
source: Hacker's Delight, 2nd Edition (Henry S. Warren, Addison-Wesley, 2012; ISBN 978-0-13-308501-3) — https://www.informit.com/store/hackers-delight-9780133085013
kind: book
tier: A
scope: The publisher's page for the 2nd edition: table of contents (Ch. 10 "Integer Division By Constants") and the list of what the edition adds
anchor: Description section, "Extensive additions in this edition include"; published Sep 25, 2012, © 2013; accessed 2026-10-29; "More coverage of integer division by constants, including methods using only shifts and adds"
teaches: Magic-number division and bit tricks that compilers emit have a citable mathematical reference (Ch. 10), so a reconstruction of "x * 0x66666667 >> 35 = x/20" can cite an algebraic derivation rather than intuition.
status: mined
limitation: The publisher page is a book listing; it does not show which idioms a particular compiler version actually emits.
province-fit: in — the reference for compiler-generated arithmetic idioms.
obscurity: niche

---

## B. Learning path (books, courses)

ID-SLUG: re4b-yurichev
source: "Reverse Engineering for Beginners" (RE4B) — Dennis Yurichev — https://beginners.re/
kind: book
tier: A
scope: The author's page for the free book (PDFs in EN/RU/FR/DE/JA/IT/PL plus CN/KR/FA translations), its CC BY-SA licence badge, and the list of universities that use it
anchor: "Supplementary materials" section; no version string on the page (the GitHub repo github.com/DennisYurichev/RE-for-beginners returned HTTP 404); accessed 2026-10-29; "All exercises are moved to standalone website"
teaches: A free, CC-licensed, multi-architecture textbook can be cited by exact chapter, but the citation must be pinned to the PDF file hash because the page carries no edition number.
status: mined
limitation: The "used at" list and praise quotes on the page are endorsements, not evidence that any chapter is technically correct.
province-fit: in — a foundational static-reading curriculum (x86/x64/ARM/MIPS listings).
obscurity: mainstream

ID-SLUG: ghidra-class-docs
source: GhidraDocs/GhidraClass (Beginner/Intermediate/Advanced/AdvancedDevelopment/BSim/Debugger/ExerciseFiles) — https://github.com/NationalSecurityAgency/ghidra/tree/master/GhidraDocs/GhidraClass
kind: docs
tier: A
scope: NSA's official in-repo Ghidra course slides and student guides; this row covers the directory layout and the README's stated mode of use
anchor: Beginner/README.txt at master 1b9e58a915cf867e106495eaa2a4b18eb4971c9d (the same README returns HTTP 200 at tag Ghidra_12.2_build); accessed 2026-10-29; "The Student Guide can be used in a classroom setting and can also be used as a self-paced tutorial."
teaches: The tool vendor's own course, versioned with the tool, lets a practitioner pin Ghidra workflow claims to the same tag as the Ghidra build used for analysis.
status: mined
limitation: Slides teach UI workflows for the tagged build; they do not show that the decompiler output is correct.
province-fit: in — Ghidra is a lane tool.
obscurity: niche

ID-SLUG: hexrays-microcode-view
source: Hex-Rays Docs — Decompiler › How-tos › "Working with Microcode" — https://docs.hex-rays.com/core/decompiler/how-tos/microcode-view.md
kind: docs
tier: A
scope: The vendor's description of the IDA decompiler Microcode view (maturity levels, deleting instructions / specifying operand values, du-ud chains, ctree display) in the current docs tree (/ida-9.5/ path resolved to /core/)
anchor: "Microcode manipulation" section; no per-page revision shown; accessed 2026-10-29; "These modifications will propagate to higher maturity levels and ultimately affect the final pseudocode output."
teaches: Analyst edits to the IR change the pseudocode, so any pseudocode quoted as evidence must say whether microcode was edited and how; otherwise it is an artefact of the session, not of the binary.
status: mined
limitation: Describes UI features; it gives no decompiler-correctness guarantee. The page also carried GitBook "agent instructions", which were treated as data and not followed.
province-fit: in — IDA/Hex-Rays is a lane tool.
obscurity: niche

---

## C. Practice corpora and challenge archives

ID-SLUG: crackmes-one-faq
source: crackmes.one — FAQ — https://crackmes.one/faq
kind: community
tier: C
scope: Site rules on what may be uploaded, the archive offer (crackmesone_20260921_163506.zip, 1.54 GB, dated September 21, 2026), the no-patch writeup policy, and the label-accuracy caveat
anchor: "Is this legal?" / "What content is not allowed on this site?" / "What are crackme labels" sections; archive date 2026-09-21; accessed 2026-10-29; "Crackmes are legal and ethical because they are made specifically for this purpose."
teaches: The site bans commercial cracking/DRM circumvention, real malware and commercial protectors, and says its obfuscation labels were produced by an AI and not checked against the binaries; a ledger should treat crackmes as purpose-built targets and their labels as unverified inference.
status: mined
limitation: The legality sentence is the site's own policy position, not legal advice; individual uploads can still break the rules before review catches them.
province-fit: in — purpose-built, consented targets for static RE practice; the site's own ban on DRM circumvention matches the lane's refusals.
obscurity: niche

ID-SLUG: crackmes-re-dataset
source: crackmesone/crackmes-re-dataset — labeled RE dataset over 4,598 crackmes — https://github.com/crackmesone/crackmes-re-dataset
kind: dataset
tier: A
scope: The README's own statement of coverage (1,217 recovered flags; 1,025 self-test-passing verifiers; 2,172 machine-checkable answers), the ARC training-data canary, and the `binary_verified: false` status
anchor: README "Coverage" and "Status" sections at commit 46b14a99bad4025ac5e6c32b55cae6ee584e1c06; accessed 2026-10-29; "labels are LLM-extracted from human-moderated writeups and not yet validated against the binaries"
teaches: A benchmark that ships keygen→verify round-trip verifiers gives a byte-checkable oracle for RE claims, and its explicit `binary_verified: false` field shows how to separate inference (LLM-transcribed labels) from observation.
status: mined
limitation: The binaries are not in the repo (join by hexid against the official archive); labels may be wrong, and published solutions mean an evaluation could be contaminated.
province-fit: in — evaluation corpus with oracles for agentic static RE; carries a training-exclusion canary that must be respected.
obscurity: obscure

ID-SLUG: challenges-re
source: Reverse Engineering challenges — Dennis Yurichev — https://challenges.re/
kind: dataset
tier: A
scope: The author's index of 87 numbered exercises (listing or executable; x86/x64/ARM/ARM64/MIPS/CLR/JVM), the stable-numbering promise, the CC BY-SA 4.0 licence, and the no-published-solutions policy
anchor: FAQ "Should I give low-level answer…" and "Exercise numbers" sections; no revision on the page; accessed 2026-10-29; "In fact, reverse engineer's job is to reduce amount of information he/she has."
teaches: The answer to an exercise is a one-sentence summary of behaviour plus a C rewrite, which is the same compression a ledger finding should do; the stable exercise numbers make the exercises citable fixtures.
status: mined
limitation: The site publishes no solutions, so it gives no answer oracle; correctness has to be checked by recompiling the C rewrite or by asking the author.
province-fit: in — multi-ISA static-reading drills.
obscurity: niche

ID-SLUG: flare-on-archive
source: The Flare-On Challenge — archive 2014–2025 (Google Cloud / Mandiant FLARE) — https://flare-on.com/
kind: dataset
tier: A
scope: The official page listing challenge zips (archive password "flare"), honor rolls, and links to the official solution write-ups for Flare-On 1–12
anchor: Landing page header "FlareOnOS v13.2"; accessed 2026-10-29; "It was a single-player series of Reverse Engineering puzzles that ran for every fall from 2014 to 2026."
teaches: Each yearly set comes with an official solutions write-up, which gives a vendor-authored expected answer for ledger self-grading on varied formats (PE, .NET, JS, firmware-like).
status: mined
limitation: The page uses the past tense, so the contest has apparently ended; some challenges behave like malware samples, so static-first handling applies, and the solution links point to blogs that may move.
province-fit: in — purpose-built RE puzzles; run them only in the lane's normal sandboxed, static-first posture.
obscurity: mainstream

---

## D. Talks and practitioner write-ups (type recovery, deobfuscation, lifting)

ID-SLUG: rolles-cpp-unwind-metadata
source: Rolf Rolles — "C++ Unwind Exception Metadata: A Hidden Reverse Engineering Bonanza" (Möbius Strip RE) — https://www.msreverseengineering.com/blog/2024/8/20/c-unwind-metadata-1
kind: paper
tier: A
scope: The author's explanation of MSVC/x64 C++ wind/unwind metadata and the Hex-Rays 9.0 support he built for it, as a source for structure recovery
anchor: Intro and "Hex-Rays 9.0 Support" sections; posted August 22, 2024; accessed 2026-10-29; "This blog entry describes an overlooked source of information in C++ programs that can make manual and automated type reconstruction more efficient."
teaches: Compiler-emitted exception/unwind tables record which objects are live at each program point (and therefore which destructor/type runs), giving a structure-layout clue backed by metadata rather than by usage guesses.
status: mined
limitation: Limited to MSVC/x64 and to the implementation in Hex-Rays 9.0; Itanium-ABI (GCC/Clang) LSDA layouts are different and not covered.
province-fit: in — static type/structure recovery for native C++.
obscurity: obscure

ID-SLUG: rolles-ghidrapal-absint
source: Rolf Rolles — "An Abstract Interpretation-Based Deobfuscation Plugin for Ghidra" (GhidraPAL; repo HEAD 749ae9546ebf3e987aa97dfd66a42c35cad0046d) — https://www.msreverseengineering.com/blog/2019/4/17/an-abstract-interpretation-based-deobfuscation-plugin-for-ghidra
kind: paper
tier: A
scope: The author's description of three-valued bitvector abstract interpretation on Ghidra p-code to resolve opaque predicates, including the false negative he documented and the p-code modelling gap he hit
anchor: "Problem: Parity Flag" section; April 17, 2019; accessed 2026-10-29; "by default, Ghidra's x86 language model does not model the updates to this flag."
teaches: A lifter's IR can silently leave out architectural effects (here x86 PF), so a static deduction from p-code is only as good as the SLEIGH spec version, which goes in the ledger next to the result.
status: mined
limitation: Describes Ghidra as of 2019; whether the current SLEIGH x86 spec models PF must be re-checked against the pinned Ghidra tag. The worked example ships a malware sample in an "infected" zip (static use only).
province-fit: in — static deobfuscation without executing the target.
obscurity: obscure

ID-SLUG: openrce-magic-division
source: ero (Ero Carrera) — "Reverse engineering a compiler-produced artifact" (OpenRCE read-only archive) — https://www.openrce.org/blog/view/892/function.session-start
kind: community
tier: C
scope: A worked derivation that `mov eax,66666667h; imul ecx; sar edx,3` means x/20, from OpenRCE, a 2005-era RE community now preserved read-only
anchor: Blog entry, Created September 10 2007, modified September 11 2007 (imported from blog.dkbza.org); accessed 2026-10-29; "Effectively dividing the value by 20, without actually using the division instruction."
teaches: A magic-constant idiom is checked by algebra (2^33/0x66666667 ≈ 5, then >>3 gives /20), which is a byte-and-arithmetic oracle a ledger can recompute instead of trusting the decompiler's "/ 20".
status: mined
limitation: Covers one signed 32-bit case on MSVC-era x86; signed-correction sequences and 64-bit variants need Hacker's Delight Ch. 10. Its hackersdelight.org links are dead (see dropped leads).
province-fit: in — compiler-idiom recognition in native code.
obscurity: obscure

ID-SLUG: tob-mishegos-blog
source: Trail of Bits — "Destroying x86_64 instruction decoders with differential fuzzing" (William Woodruff) — https://blog.trailofbits.com/2019/10/31/destroying-x86_64-instruction-decoders-with-differential-fuzzing/
kind: paper
tier: A
scope: The authors' description of the sliding-window mutation strategy, the worker ABI, and the discrepancy classes found across Capstone, libopcodes, udis86, XED and Zydis
anchor: "In the beginning, there was instruction decoding" section; published 2019-10-31; accessed 2026-10-29; "Analysis platforms give analysts a false sense of confidence by encouraging them to treat disassembled output as ground truth"
teaches: Disassembly is itself an inference made by one particular decoder; where it matters, the ledger records the decoder name and version and cross-checks contested bytes against a second decoder.
status: mined
limitation: Its findings are 2019 decoder versions; it does not say that any current decoder still has a given bug.
province-fit: in — evidence discipline for the disassembly layer.
obscurity: niche

ID-SLUG: tob-mishegos-repo
source: trailofbits/mishegos — differential fuzzer for x86 decoders — https://github.com/trailofbits/mishegos
kind: tool
tier: A
scope: The repo README's stated purpose, worker set (now incl. bddisasm, fadec, iced, yaxpeax-x86, dynamorio, llvm, ghidra), analysis passes, and the LangSec 2021 paper citation, at the pinned commit
anchor: README top, commit 314da02fb132f285cb503bdd64bf2b53cef090c0; accessed 2026-10-29; "A differential fuzzer for x86 decoders."
teaches: The `same-size-different-decodings` style of pass is a ready-made way to turn decoder disagreement into a byte-level fixture for forged-claim rejection tests.
status: mined
limitation: Not installed or run here; README build claims (e.g. macOS support) are unverified.
province-fit: in — a decoder-oracle tool, not an exploitation tool.
obscurity: niche

ID-SLUG: cxiao-rust-types-reverse2025
source: Cindy Xiao — "Reconstructing Rust Types: A Practical Guide for Reverse Engineers" (RE//verse 2025; slides repo HEAD 8b4bf07edba854f80636eba57dddf4a14088822f) — https://cxiao.net/posts/2025-02-28-reconstructing-rust-types-re-verse-2025/
kind: talk
tier: A
scope: The speaker's page with the abstract, video and slides (HTML/PDF, GitHub mirror) on Rust type layout and the artefacts in binaries that reveal it
anchor: Abstract block; published 2025-02-28, modified 2025-05-10; accessed 2026-10-29; "As of 2024, most reverse engineers still struggle to statically reverse Rust binaries."
teaches: Rust layout facts (std types, formatting/error types) need toolchain-version provenance, because rustc does not promise a stable layout; a type reconstruction is an inference tied to that compiler version.
status: mined
limitation: Opinion and teaching material for a talk; it does not cover every rustc version or layout optimisation.
province-fit: in — static type recovery for Rust native binaries.
obscurity: niche

ID-SLUG: mandiant-goresym-internals
source: Mandiant (Stephen Eckels) — "Ready, Set, Go — Golang Internals and Symbol Recovery" — https://cloud.google.com/blog/topics/threat-intelligence/golang-internals-symbol-recovery
kind: paper
tier: A
scope: The authors' account of how pclntab, moduledata and buildinfo are located (symbols → named sections → byte scan) and how GoReSym changes the Go runtime parsers
anchor: "PCLNTAB" section; dated February 28, 2022; accessed 2026-10-29; "Byte scanning is always required for stripped PE files and occasionally for ELF and Mach-O binaries with mutated section names."
teaches: Go metadata gives a fallback order with decreasing confidence (symbol, then section name, then magic-number scan), and the ledger should record which path located the table.
status: mined
limitation: Structure layouts change between Go versions; the post reflects Go up to early 2022 and is not a spec.
province-fit: in — static symbol recovery for Go native binaries.
obscurity: niche

ID-SLUG: oalabs-dotnet-dnlib-static
source: OALABS Research — "Dot NET Static Analysis With Python" (pythonnet + dnlib) — https://research.openanalysis.net/dot%20net/static%20analysis/stormkitty/dnlib/python/research/2021/07/14/dot_net_static_analysis.html
kind: community
tier: C
scope: A worked notebook that finds a .NET string-decryption method by IL pattern and pulls `ldtoken` field InitialValue bytes with dnlib, without executing the assembly
anchor: ".NET Assembly Analysis" section; Jul 14, 2021; accessed 2026-10-29; "I think this works because the array is static making the initial value the actual value but I'm not entirely sure."
teaches: The author marks his own uncertainty inside the method (an inference about field initial values), which is the observation/inference split a ledger needs when extracting static IL data.
status: mined
limitation: The target is a real stealer sample from malshare; use the method, not the sample. It does not show that the InitialValue assumption holds for non-static fields.
province-fit: adjacent — static-only managed-assembly technique on a malware sample; no protection-disabling steps were present.
obscurity: niche

---

## E. Community ground truth

ID-SLUG: re-stackexchange-on-topic
source: Reverse Engineering Stack Exchange — Help Center "What topics can I ask about here?" — https://reverseengineering.stackexchange.com/help/on-topic (live page blocked by a Cloudflare challenge; text read from the Wayback snapshot http://web.archive.org/web/20251231045737/https://reverseengineering.stackexchange.com/help/on-topic)
kind: community
tier: C
scope: The site's scope statement as of snapshot 2025-12-31 (site rev 2025.12.22.38265); site size from api.stackexchange.com/2.3/info (9,905 questions, 11,344 answers, api_revision 2026.5.26.43284)
anchor: Help Center "What topics can I ask about here?"; snapshot 20251231045737; accessed 2026-10-29; "Reverse Engineering Stack Exchange is for researchers and developers who explore the principles of a system through analysis of its structure, function, and operation."
teaches: Answers there are community leads (CC BY-SA) for idiom identification, e.g. magic-constant questions, but each one needs re-deriving before it enters the ledger.
status: mined
limitation: Taken from an archive snapshot, not the live page; the API reported 0.00 questions/minute, so the site may be low-activity and its answers dated.
province-fit: in — the scope explicitly covers static/dynamic software analysis and disassembly/decompilation.
obscurity: niche

---

## F. Rejected (screened, out of province)

ID-SLUG: nightmare-guyinatuxedo
source: guyinatuxedo/nightmare — https://github.com/guyinatuxedo/nightmare
kind: code
tier: A
scope: The course README's self-description and module index at commit c1d643aeade6893944fea413694dbd46f56fa197
anchor: README "Nightmare" section; commit c1d643aeade6893944fea413694dbd46f56fa197; accessed 2026-10-29; "Nightmare is an intro to binary exploitation / reverse engineering course based around ctf challenges."
teaches: Of 90+ challenges, only module 3 "Beginner RE" (pico18_strings, helithumper_re, csaw18_tourofx86pt1, csaw19_beleaf) is pure reversing; the rest builds exploit chains.
status: rejected
limitation: Reject reason (located quote above, plus the README's statement that the skills "directly translate" into weaponized 0-day work): the curriculum is exploitation-centred. Flip condition: admit only module 3 "Beginner RE" as a separate row if the lane wants extra static drills.
province-fit: out — exploitation course; only one module is adjacent.
obscurity: mainstream

ID-SLUG: rop-emporium
source: ROP Emporium (Max Kamper) — https://ropemporium.com/
kind: dataset
tier: A
scope: The site's statement of purpose and its 8-challenge list (ret2win … ret2csu)
anchor: Landing page; no version; accessed 2026-10-29; "Learn return-oriented programming through a series of challenges."
teaches: Its challenge text notes 32- vs 64-bit calling-convention differences (callme), but every exercise ends in building a ROP chain.
status: rejected
limitation: Reject reason: the located quote states the purpose is return-oriented programming, i.e. exploitation, which the lane refuses. Flip condition: none within the current PROVINCE; reconsider only if the province formally adds exploit-development training.
province-fit: out — exploitation training (ret2win included).
obscurity: niche

---

## Screened-and-dropped leads (URL + reason)

- https://github.com/DennisYurichev/RE-for-beginners — HTTP 404 this session; use beginners.re instead.
- https://www.wiley.com/en-us/Practical+Reverse+Engineering…-p-9781118787250 and …-p-9781118787311 — HTTP 403 Cloudflare challenge (read and curl); O'Reilly (oreilly.com/library/view/practical-reverse-engineering/9781118787311/) and ACM record dl.acm.org/doi/10.5555/2636663 also 403. Not opened, so no row.
- https://www.wiley.com/en-us/Reversing%3A+Secrets+of+Reverse+Engineering-p-9780764574818 (Eilam) — HTTP 403; O'Reilly mirror 403. Not opened, so no row.
- https://onlinelibrary.wiley.com/doi/book/10.1002/9781394277131 (Domas, "x86 Software Reverse-Engineering, Cracking, and Counter-Measures", 2024; seen in search) — HTTP 403; not opened.
- https://www.hackersdelight.org/ — opened; the domain now serves unrelated French lifestyle content, so it is NOT a Hacker's Delight source. Legacy links to it (e.g. OpenRCE → hackersdelight.org/divcMore.pdf) are dead; cite InformIT/Pearson instead.
- https://docs.hex-rays.com/developer-guide/decompiler-sdk — HTTP 404 (docs restructured); replaced by the /core/decompiler microcode page.
- https://docs.amd.com/v/u/en-US/40332_4.10_APM_Vol1-5_PUB — the HTML is a JS shell; content verified via the khub API and the PDF instead (row amd-apm-40332).
- https://reverseengineering.stackexchange.com/help/on-topic (live) — Cloudflare "Just a moment…"; used the Wayback snapshot.
- "The Art of Disassembly" / "Low-Level Programming" publisher pages — not searched in time; no row.
- https://recon.cx/2024/presentations.html, https://recon.cx/cfp.recon.cx/recon2024/talk/QCA37X/index.html (cxiao Rust workshop) — found by search, not opened; the RE//verse talk page was used instead. Candidate for a later pass.
- https://www.msreverseengineering.com/blog/2019/8/5/automation-techniques-in-c-reverse-engineering (Rolles RECON 2019 C++ automation) — search result only; not opened.
- https://blog.trailofbits.com/2024/02/07/binary-type-inference-in-ghidra/ (BTIGhidra) and …/2018/01/23/heavy-lifting-with-mcsema-2-0/ — search results only; likely BfResearchPapers/BfTriageTools overlap.
- https://blog.ret2.io/ (RET2 Systems) — search shows exploitation-centred posts (Pwn2Own browser/JSC exploits); out of province.
- https://repnz.github.io/posts/reversing-optimizations-division/ and https://www.reverseengineering.app/en/learn/compiler-idioms — search results only; not opened (lower priority than the Hacker's Delight + OpenRCE pair).
- https://github.com/NDXDeveloper/reverse-engineering-gcc-gpp-training — search result; an unknown-provenance course with a mirror fork (MBenDelphi), so low trust; not opened.

## Search log

Engine: `web_search` tool (Perplexity, fell back to Parallel after Perplexity 429 rate limits) + direct `read`/`curl` of known URLs + `git ls-remote` for commit pins + api.stackexchange.com, documentation-service.arm.com and docs.amd.com khub APIs for JS-only portals. GitHub REST API hit an unauthenticated rate limit, so pins come from `git ls-remote`.

Queries run (web_search):
1. Rolf Rolles Möbius Strip Reverse Engineering blog static deobfuscation
2. Hacker's Delight 2nd edition Henry Warren informit pearson
3. Rust binary reverse engineering talk RTTI type recovery REcon
4. Trail of Bits blog binary lifting remill decompilation ground truth
5. "OpenRCE" OR "reverse engineering" magic division constant compiler idiom recognition article
6. recon.cx archive talks reverse engineering conference slides
7. docs.hex-rays.com decompiler SDK microcode developer guide
8. AMD64 Architecture Programmer's Manual volumes 1-5 24592 documentation hub
9. OALabs static analysis tutorial unpacking IDA string decryption blog
10. ret2.systems blog reverse engineering binary analysis
11. Go binary reverse engineering pclntab type recovery talk slides
12. Arm Architecture Reference Manual for A-profile architecture DDI0487 latest issue
13. "Practical Reverse Engineering" Dang Gazet Bachaalany Wiley onlinelibrary doi book

Direct fetches (seeded from the slice list): beginners.re, RE4B GitHub, crackmes.one/faq, flare-on.com, agner.org/optimize, GhidraClass (dir + Beginner + Intermediate README + student guide at tag Ghidra_12.2_build), RE.SE help (live + Wayback + API), ROP Emporium, Nightmare, Intel SDM, Wiley ×2, O'Reilly ×2, ACM, Wiley Online Library, Arm ARM, hackersdelight.org, challenges.re, uops.info, sandpile.org, mishegos repo.

Counts: identified 52 candidate URLs · opened 38 (including 9 that failed with 403/404 or returned a JS shell) · kept 24 rows (22 mined + 2 rejected) · dropped 15 leads listed above.
Obscure/niche finds from web_search (≥5): Rolles C++ unwind metadata, Rolles GhidraPAL parity-flag gap, OpenRCE magic-division post, crackmes-re-dataset, mishegos blog+repo, cxiao Rust types, Mandiant GoReSym internals, sandpile.org, plus the hackersdelight.org domain-squat finding.
