# ReFirmwareAndArchives — candidate rows for corpus/SOURCES.md

Slice: firmware, archives, filesystems, boot/embedded, binary-diff provenance.
Every row below was opened this session (2026-10-29) via `curl` (GitHub raw at a pinned commit, or the primary docs page). I checked each quote against the fetched bytes (README files, or HTML with the markup stripped). I checked every URL against /tmp/revenger-existing-urls.txt: none of them is listed there. The corpus already has the REA `docs/firmware-analysis.md` and the Android dex-format URL. Those were not reused.
I installed and ran no tools. The commit pins are `git ls-remote … HEAD` values observed on 2026-10-29. Where the GitHub API answered before it rate-limited, the commit date is given too.

---

## Extraction / carving suites

ID-SLUG: unblob-readme
source: unblob README — https://github.com/onekey-sec/unblob/blob/9f129397ab8e1d1b1e5df81ca33da38b9e1a5d9a/README.md (latest release 26.6.4; commit 2026-10-28)
kind: tool
tier: A
scope: the project's own README description of its chunk-boundary and unknown-chunk behaviour at commit 9f12939
anchor: README "Features" list; commit 9f129397; accessed 2026-10-29; "identifies both start and end offsets of each chunk according to the format standard, minimizing false positives."
teaches: For each carved chunk, record both the start and end offsets and the format rule that bounded the chunk; "found a signature" is not enough.
status: mined
limitation: This is the project's own claim about its design. It does not measure accuracy against binwalk or any other tool.
province-fit: in — artifact-first carving of firmware blobs
obscurity: mainstream

ID-SLUG: unblob-handler-limits
source: unblob — Handlers / Supported Formats page — https://unblob.org/handlers/ (docs for unblob 26.6.x)
kind: docs
tier: A
scope: unblob's per-handler "Fully/Partially supported" status and its Limitations notes
anchor: section "Airoha BT firmware" → Limitations; accessed 2026-10-29 (8 handlers marked "Partially supported"); "AES-encrypted firmware blobs are only carved, decryption requires a per-vendor AES key/IV not embedded in the file."
teaches: A carved encrypted chunk is an observation of its boundaries only. Its contents stay unknown, and the ledger should record that it was not decrypted.
status: mined
limitation: Handler status reflects what the maintainers list. It is not a test-suite coverage figure.
province-fit: in — bounds what an extraction can claim; decryption keys are explicitly out of scope
obscurity: niche

ID-SLUG: binwalk-v3-readme
source: Binwalk v3 README — https://github.com/ReFirmLabs/binwalk/blob/26713972e3f9f52dc37d4a421c4554b0bd9e82ef/README.md (release v3.1.0; commit 2026-08-11)
kind: tool
tier: A
scope: the README's statement of what Binwalk v3 does, at v3.1.0
anchor: README "What does it do?"; commit 26713972; accessed 2026-10-29; "Binwalk can identify, and optionally extract, files and data that have been embedded inside of other files."
teaches: The README separates identification from extraction, so log signature hits separately from extracted bytes.
status: mined
limitation: Entropy-based identification is a lead. It does not prove encryption or compression.
province-fit: in — firmware region mapping
obscurity: mainstream

ID-SLUG: emba-readme
source: EMBA README — https://github.com/e-m-b-a/emba/blob/e43a15c528004caea236f4b806397a9cb8b3fc7e/README.md (release v2.0.4-summer_edition; commit 2026-10-28)
kind: tool
tier: A
scope: EMBA's own statement of who is responsible for interpreting its output
anchor: README intro paragraph; commit e43a15c5; accessed 2026-10-29; "the tester can decide on focus areas and is responsible for verifying and interpreting the results."
teaches: Treat findings from automated firmware analysers as leads until the analyst re-verifies them. The authors say this themselves.
status: mined
limitation: EMBA also does dynamic analysis and emulation. Only its static extraction and SBOM parts are in province.
province-fit: adjacent — static parts in; emulation and pentest workflow out
obscurity: mainstream

ID-SLUG: fact-core-readme
source: FACT_core README — https://github.com/fkie-cad/FACT_core/blob/c34a0333b291be89357c9cc9f2dcf2b2a19f5722/README.md (release v4.4.1; commit 2026-10-28)
kind: tool
tier: A
scope: FACT's stated purpose and the properties it claims for its results
anchor: README "Why FACT?"; commit c34a0333; accessed 2026-10-29; "Some of the key features of the FACT analysis, is that results are - browsable - searchable - and comparable."
teaches: Being able to compare results across firmware versions is a design goal in itself. Diffing two unpacked images needs stable, comparable records.
status: mined
limitation: "Comparable" describes the UI and data model. It does not say that two analyses are equivalent.
province-fit: in — static firmware unpack and comparison
obscurity: niche

ID-SLUG: firmware-mod-kit-lineage
source: Firmware Modification Kit (mirror of code.google.com/p/firmware-mod-kit) — https://github.com/rampageX/firmware-mod-kit/blob/c72f45d7a062156125ae00cb867d8a614b50b963/README.md
kind: tool
tier: C
scope: historical lineage of extract-and-rebuild firmware tooling; README at commit c72f45d
anchor: README "Disclaimer"; commit c72f45d7; accessed 2026-10-29; "Automatically exported from code.google.com/p/firmware-mod-kit"
teaches: This is a community mirror, not the original source. Cite it as lineage, and keep reading separate from rebuild/flash.
status: mined
limitation: It is an unofficial export and is unmaintained. Its rebuild and flash workflow is out of province.
province-fit: adjacent — extraction lineage in; modify and flash out
obscurity: niche

ID-SLUG: ofrak-readme
source: OFRAK README — https://github.com/redballoonsecurity/ofrak/blob/1e1ef750222c1a842248ae7bdcae576bfdedae65/README.md
kind: tool
tier: A
scope: OFRAK's own feature statement on identify, unpack, and repack
anchor: README intro; commit 1e1ef750; accessed 2026-10-29; "A **Python API** for readable and reproducible scripts that can be applied to entire classes of binaries, rather than just one specific binary"
teaches: Scripted unpack pipelines turn an extraction into a re-runnable procedure that can back a byte-oracle fixture.
status: mined
limitation: Repack and patching are out of province. Only the identify/unpack/analyze steps apply.
province-fit: adjacent — unpack in; modify/repack out
obscurity: niche

## Filesystems

ID-SLUG: squashfs-tools-official
source: Squashfs-tools README — https://github.com/plougher/squashfs-tools/blob/db038ef265ed00bb17aaf695a72f9b0c3489eb20/README.md (release 4.7.5; commit 2026-08-21)
kind: code
tier: A
scope: which repository is the upstream reference for mksquashfs/unsquashfs, at 4.7.5
anchor: README top; commit db038ef2; accessed 2026-10-29; "This is the official Squashfs-tools repository."
teaches: Pin SquashFS behaviour claims to the upstream tool version, not to a vendor fork.
status: mined
limitation: The upstream tool does not handle vendor-modified SquashFS (see sasquatch).
province-fit: in — reference implementation for a common firmware filesystem
obscurity: mainstream

ID-SLUG: squashfs-ng-binary-format
source: squashfs-tools-ng "Squashfs Binary Format" — https://github.com/AgentD/squashfs-tools-ng/blob/e3dcf1770fd77a0babcca422dcbe7b2cc7b8ab90/doc/format.adoc
kind: spec
tier: A
scope: a field-level on-disk description of SquashFS v4 that came out of reverse engineering (superblock magic, endianness, sentinel values)
anchor: "== Overview" and the superblock table; commit e3dcf177; accessed 2026-10-29; "SquashFS always stores integers in little endian format." (the table also gives magic `0x73717368` ("hsqs" on disk))
teaches: A community-derived byte-level format doc allows hand-checkable fixtures (magic, sentinel `0xFFFFFFFF`). Its origin should be recorded as reverse engineering, not kernel-authoritative.
status: mined
limitation: The doc says it grew out of reverse-engineering attempts, so the Linux kernel source wins on conflicts. The little-endian rule does not cover vendor big-endian forks.
province-fit: in — byte-checkable filesystem spec
obscurity: obscure

ID-SLUG: sasquatch-vendor-squashfs
source: sasquatch README — https://github.com/devttys0/sasquatch/blob/bd864a1b037bf57ca7d64a292a60ba0d6459611f/README.md (last commit 2021-03-25)
kind: tool
tier: A
scope: the project's own description of how it handles vendor-modified SquashFS
anchor: README "About"; commit bd864a1b; accessed 2026-10-29; "sasquatch will attempt to automatically resolve such customizations via a brute-force method."
teaches: If a parameter was recovered by brute force, mark it as inference. Do not record it as a format observation.
status: mined
limitation: The README calls itself "Very beta", and this repo is the older upstream. unblob installs the onekey-sec fork.
province-fit: in — vendor filesystem quirks
obscurity: niche

ID-SLUG: jefferson-jffs2
source: jefferson README — https://github.com/onekey-sec/jefferson/blob/f605cd1fed21177176cafef918d91b275054b187/README.md
kind: tool
tier: A
scope: what jefferson checks and does not check when extracting JFFS2
anchor: README "Features"; commit f605cd1f; accessed 2026-10-29; "CRC checks - for now only enforced on `hdr_crc`"
teaches: A successful JFFS2 extraction does not mean the data CRCs were verified. Record which checksums the tool actually checked.
status: mined
limitation: This describes behaviour at this commit only. It may change.
province-fit: in — flash filesystem extraction
obscurity: niche

ID-SLUG: ubi-reader-known-issues
source: UBI Reader README — https://github.com/onekey-sec/ubi_reader/blob/5f45e50c813599d689b8cf88e12e7c79dec1728f/README.md
kind: tool
tier: A
scope: the README's "Known Issues" on where UBI/UBIFS extraction is incomplete
anchor: README "Known Issues"; commit 5f45e50c; accessed 2026-10-29; "This does not replay the journal, so uncommitted data will not be retrieved."
teaches: Files missing from a UBIFS extraction can be uncommitted journal data. They are not proof that the files are absent from the device image.
status: mined
limitation: It says nothing about ECC-corrected versus raw NAND dumps beyond the README's warning.
province-fit: in — NAND/UBI artifact extraction
obscurity: niche

ID-SLUG: extfstools-ext4-partial
source: nlitsme/extfstools README — https://github.com/nlitsme/extfstools/blob/b57e885267194e56ce609f956a2a33bd1af21612/README.md
kind: tool
tier: A
scope: the author's statement of how complete its ext4 support is
anchor: README intro; commit b57e8852; accessed 2026-10-29; "Note that ext4 is not fully supported, some files may not be extracted."
teaches: Small single-author extractors document coverage gaps. Copy those gaps into the ledger as known unknowns.
status: mined
limitation: Use only as a cross-check reader. It is not authoritative for ext4.
province-fit: in — Android system-image extraction
obscurity: obscure

## UEFI / platform firmware

ID-SLUG: uefitool-readme
source: UEFITool README — https://github.com/LongSoft/UEFITool/blob/de73942df908b9466c055e15108ac4e4c0b1688c/README.md
kind: tool
tier: A
scope: UEFITool's self-description (PI-spec image parser) and its stated missing features
anchor: README "Very Brief Introduction to UEFITool"; commit de73942d; accessed 2026-10-29; "parses UEFI-compatible firmware image into a tree structure, verifies its integrity and provides a GUI to manipulate its elements."
teaches: A PI-spec tree parse plus its integrity checks gives structure-level observations: volume and file checksums.
status: mined
limitation: "Verifies its integrity" means format checksums. It is not signature or Secure Boot validation. The new engine's editor part is still missing.
province-fit: in — static UEFI image structure
obscurity: mainstream

ID-SLUG: uefi-firmware-parser
source: uefi-firmware-parser README — https://github.com/theopolis/uefi-firmware-parser/blob/c4b8c64e7a1ca647b68db99db80ef0410d9afe79/README.rst
kind: tool
tier: A
scope: the module's own scope statement (UEFI volumes, OptionROM, Intel ME)
anchor: README intro; commit c4b8c64e; accessed 2026-10-29; "The UEFI firmware parser is a simple module and set of scripts for parsing, extracting, and recreating UEFI firmware volumes."
teaches: A second, independent Python parser lets you cross-check the UEFITool tree (two readers, one artifact).
status: mined
limitation: The CI badge points to the defunct travis-ci.org, so maintenance status is unknown.
province-fit: in — static UEFI parsing
obscurity: niche

ID-SLUG: biosutilities
source: platomav/BIOSUtilities README — https://github.com/platomav/BIOSUtilities/blob/f799425af93264b62a2f3c3cc5bbabf8a2226114/README.md
kind: tool
tier: A
scope: the collection's own scope statement plus its per-utility sections (e.g. "AMI BIOS Guard Extractor")
anchor: README "Description"; commit f799425a; accessed 2026-10-29; "BIOSUtilities is a collection of various BIOS/UEFI-related utilities which aid in research and/or modding purposes."
teaches: Vendor update-package wrappers (AMI, Dell, etc.) need their own unwrappers before a PI-spec parser can see the image.
status: mined
limitation: Some utilities depend on external executables. The modding purposes are out of province.
province-fit: adjacent — vendor-wrapper extraction in; modding out
obscurity: obscure

ID-SLUG: fwhunt-scanner
source: FwHunt Community Scanner README — https://github.com/binarly-io/FwHunt-scanner/blob/6fc7115959e4825199882f5b397a0d7c34cbbfd1/README.md
kind: tool
tier: A
scope: what the scanner does, and its pinned rizin dependency
anchor: README top / "Dependencies"; commit 6fc71159; accessed 2026-10-29; "Tools for analyzing UEFI firmware and checking UEFI modules with [FwHunt rules](https://github.com/binarly-io/fwhunt)."
teaches: A rule match on a UEFI module is a detection lead tied to a rule ID. Record the rule revision, not just "vulnerable".
status: mined
limitation: A rule hit does not confirm a vulnerability. The pinned rizin v0.6.2 limits reproducibility.
province-fit: adjacent — static triage in; vulnerability claims need separate evidence
obscurity: niche

ID-SLUG: chipsec-live-platform
source: CHIPSEC README — https://github.com/chipsec/chipsec/blob/25457060db45217c74b46f61cc934098ddff8d64/README.md
kind: tool
tier: A
scope: CHIPSEC's self-description as a live-platform security test framework
anchor: README intro; commit 25457060; accessed 2026-10-29; "NOTE: This software is for security testing purposes. Use at your own risk."
teaches: Tools that read hardware registers on the running host are live-target activity, which is a different evidence class from artifact parsing.
status: rejected — reject reason (located quote above): it is a live-host security-testing framework, and the province is artifact-first with no live-target activity. Flip condition: keep only if a row cites CHIPSEC's offline parsing of a supplied SPI-dump file, anchored to that module's docs.
limitation: The rejection does not say anything about CHIPSEC's quality.
province-fit: out — live platform testing
obscurity: mainstream

## Boot images / embedded formats

ID-SLUG: devicetree-spec-v0.4
source: Devicetree Specification Release v0.4 (28 June 2023) — https://github.com/devicetree-org/devicetree-specification/releases/download/v0.4/devicetree-specification-v0.4.pdf
kind: spec
tier: A
scope: FDT/DTB header layout (magic, totalsize, block offsets), per spec v0.4 (the latest release listed on the releases page)
anchor: §5.2 Header, field "magic"; Release v0.4, 28 June 2023; accessed 2026-10-29; "This field shall contain the value 0xd00dfeed (big-endian)."
teaches: DTB blobs carved from firmware can be checked against a normative header; `totalsize` gives an exact chunk end.
status: mined
limitation: A valid header does not mean the bindings match the actual hardware.
province-fit: in — byte-checkable embedded format spec
obscurity: niche

ID-SLUG: fit-spec-1.0
source: Flat Image Tree (FIT) Specification 1.0 — https://fitspec.osfw.foundation/ (Revision 1.0, 2026-APR-11)
kind: spec
tier: A
scope: FIT hash-node and signature-node semantics, including which `algo` values are non-cryptographic
anchor: §5.4 "Hash nodes" → algo table; rev 1.0 2026-04-11; accessed 2026-10-29; "FIT is formally a flattened devicetree (in the libfdt meaning), which conforms to bindings defined in this document."
teaches: FIT is a DTB, so parse it with an FDT parser. The hash-node table lists crc16-ccitt and crc32 next to sha256, so an `algo` value has to be read before the node is called an integrity proof.
status: mined
limitation: Hash nodes alone are not authentication; image-signature nodes (§5.5) do that. Signature validity also needs the verifier's key.
province-fit: in — U-Boot image format spec
obscurity: niche

ID-SLUG: android-boot-image-header
source: Android "Boot image header" — https://source.android.com/docs/core/architecture/bootloader/boot-image-header (Last updated 2026-10-09 UTC)
kind: spec
tier: A
scope: `boot_img_hdr` struct layouts for each header_version, with field offsets and sizes
anchor: struct listing for the version-0 header; last updated 2026-10-09; accessed 2026-10-29; "uint32_t header_version ; /* offset remains constant for version check */"
teaches: Dispatch boot.img parsing on `header_version` at its fixed offset, then read the version-specific layout. Kernel and ramdisk sizes follow from the header.
status: mined
limitation: OEM boot images can deviate from this header. The spec does not describe vendor_boot contents beyond its own section.
province-fit: in — Android boot artifact format
obscurity: mainstream

ID-SLUG: avb-vbmeta
source: Android Verified Boot 2.0 README (external/avb) — https://android.googlesource.com/platform/external/avb/+/refs/heads/main/README.md (branch main, as fetched 2026-10-29)
kind: spec
tier: A
scope: the VBMeta struct, its descriptor types (hash, hashtree, chained partition), and rollback index semantics
anchor: section "The VBMeta struct"; main @ 2026-10-29; accessed 2026-10-29; "This data structure contains a number of descriptors (and other metadata) and all of this data is cryptographically signed."
teaches: A boot partition's hash lives in vbmeta's hash descriptor. The system partition's root hash lives in a hashtree descriptor. Record which one you checked.
status: mined
limitation: The branch is pinned only by date. Checking a descriptor hash says nothing about whether the device enforced it.
province-fit: in — static parse of Android image metadata
obscurity: niche

ID-SLUG: update-engine-payload-proto
source: update_engine `update_metadata.proto` — https://android.googlesource.com/platform/system/update_engine/+/refs/heads/main/update_metadata.proto (main, fetched 2026-10-29)
kind: spec
tier: A
scope: the payload.bin header comment (magic, version, manifest size, metadata signature) and the per-operation hash fields
anchor: InstallOperation field `src_sha256_hash = 9`; main @ 2026-10-29; accessed 2026-10-29; "If present, the update_engine daemon // MUST read and verify the source data before applying the operation."
teaches: Delta OTA operations carry hashes for both source and data. You can verify an incremental payload offline only when you have the right base image.
status: mined
limitation: The proto describes structure only. Validating the payload signature needs the OEM public key.
province-fit: in — OTA artifact format
obscurity: niche

ID-SLUG: payload-dumper-go
source: payload-dumper-go README — https://github.com/ssut/payload-dumper-go/blob/c3a50ba8d784764c06143c1f82971cd81a77f9d6/README.md
kind: tool
tier: A
scope: the tool's own claims about verification and delta support
anchor: README "Features"; commit c3a50ba8; accessed 2026-10-29; "Verifies everything: operation data, source images, and final images (sha256). Fails loudly with a non-zero exit code."
teaches: Use a tool's exit code plus sha256 checks as the extraction oracle. Record the checks it claims to make and test them on a fixture.
status: mined
limitation: "Verifies everything" is the author's claim, and the README does not mention signature verification.
province-fit: in — OTA payload extraction
obscurity: niche

ID-SLUG: qc-image-unpacker
source: Android Qualcomm Image Unpacker README — https://github.com/anestisb/qc_image_unpacker/blob/28a783a9fc25dc87b7416b6d5b6f9ccd497d1c2e/README.md
kind: tool
tier: A
scope: the specific Qualcomm packed-image magic values the tool recognises
anchor: README intro list; commit 28a783a9; accessed 2026-10-29; "List of currently supported magic headers are: 1. 0xce1ad63c: msm8996 2. 0x4b504246: sdm845, sdm855, sdm670"
teaches: Vendor container magics with chipset mappings make good signature fixtures. Note which SoC generations were tested.
status: mined
limitation: Only the listed SoCs are claimed. Absence of these magics does not mean an image is not Qualcomm.
province-fit: in — vendor bootloader/modem container formats
obscurity: obscure

ID-SLUG: tfa-fip-layout
source: Trusted Firmware-A "Firmware Design" — Firmware Image Package (FIP) — https://github.com/ARM-software/arm-trusted-firmware/blob/221bb9b13bf44be3268b3410fac0b4118d7e7ddd/docs/design/firmware-design.rst
kind: docs
tier: A
scope: FIP container layout (ToC header, UUID-keyed entries, end marker)
anchor: section "Firmware Image Package layout"; commit 221bb9b1; accessed 2026-10-29; "The FIP layout consists of a table of contents (ToC) followed by payload data."
teaches: Arm boot-chain stages (BL2/BL31/BL33) in a FIP are located by UUID ToC entries, so the chunk boundaries come from the spec, not from guessed heuristics.
status: mined
limitation: Platforms can add vendor UUIDs. A FIP parse does not validate the trusted-board-boot certificates.
province-fit: in — Arm boot firmware container
obscurity: obscure

ID-SLUG: vmlinux-to-elf
source: vmlinux-to-elf README — https://github.com/marin-m/vmlinux-to-elf/blob/36da74ded9cd486f294c8852e0dcab9ef6a48c6b/README.md
kind: tool
tier: A
scope: the method the tool states it uses: kallsyms recovery from raw or stripped kernel images
anchor: README intro; commit 36da74de; accessed 2026-10-29; "For this, it scans your kernel for a kernel symbol table ([kallsyms](https://github.com/torvalds/linux/blob/master/kernel/kallsyms.c)), a compressed symbol table that is present in almost every kernel"
teaches: Kernel symbol names recovered from kallsyms are artifact-derived observations. Tag them with the recovery method, and keep them apart from names an analyst assigns.
status: mined
limitation: "almost every kernel" is the author's phrasing. Kernels built without CONFIG_KALLSYMS give nothing.
province-fit: in — embedded kernel symbol recovery
obscurity: obscure

## Peripheral maps

ID-SLUG: cmsis-svd-spec
source: Open-CMSIS-SVD: System View Description — https://open-cmsis-pack.github.io/svd-spec/main/index.html
kind: spec
tier: A
scope: what an SVD file formalises (memory-mapped peripheral registers and bit fields) and who maintains SVD files
anchor: "Introduction"; main branch docs, accessed 2026-10-29; "formalizes the description of the system contained in Arm Cortex processor-based devices, in particular, the memory mapped registers of peripherals."
teaches: In bare-metal firmware, register addresses can be labelled from a vendor SVD, a cited source, rather than guessed from magic constants.
status: mined
limitation: The SVD describes the documented chip, not the board. Vendor SVDs are known to need patches (see cmsis-svd-data).
province-fit: in — peripheral ground truth for static MCU RE
obscurity: niche

ID-SLUG: cmsis-svd-data
source: CMSIS-SVD Repository README — https://github.com/cmsis-svd/cmsis-svd-data/blob/c65f8551e57c770344d229dcaa0bf838fa29aff4/README.md
kind: dataset
tier: C
scope: the aggregation of vendor SVD files plus svdtools patches
anchor: README list item 2; commit c65f8551; accessed 2026-10-29; "Provide a convenient place to access and aggregate CMIS-SVD file patches generated with [rust-embedded/svdtools]"
teaches: Aggregated SVDs are not always the vendor original, so record whether a peripheral label came from an unpatched or a patched SVD.
status: mined
limitation: This is an aggregator, so the vendor publication stays the primary source per file (hence tier C). The "CMIS" typo is in the original.
province-fit: in — peripheral map dataset
obscurity: niche

ID-SLUG: svd-loader-ghidra
source: SVD-Loader for Ghidra README — https://github.com/leveldown-security/SVD-Loader-Ghidra/blob/4b21fa54a1f516e25e959939f6e1251263c74725/README.md
kind: tool
tier: A
scope: how the loader is installed and where its SVD parser came from
anchor: README "Getting SVDs"/credits; commit 4b21fa54; accessed 2026-10-29; "The cmsis-svd code is a fork from Posborne's [cmsis-svd](https://github.com/posborne/cmsis-svd/), ported to work on Ghidra's Jython."
teaches: Applying an SVD inside Ghidra creates labelled memory blocks. Record the SVD file hash used, so the labelling can be reproduced.
status: mined
limitation: It is built on Ghidra Jython, so it may not run in newer PyGhidra-only setups (inference; not tested).
province-fit: in — Ghidra firmware loader aid
obscurity: obscure

## Binary diff & build provenance

ID-SLUG: diffoscope-readme
source: diffoscope README — https://salsa.debian.org/reproducible-builds/diffoscope/-/blob/d3e59476da9b3312c9c4affec03fb100b0047395/README.rst (latest release 335, 23 Oct 2026 per diffoscope.org)
kind: tool
tier: A
scope: diffoscope's stated method: recursive unpacking plus transformation to readable form before diffing
anchor: README intro; commit d3e59476; accessed 2026-10-29; "It will recursively unpack archives of many kinds and transform various binary formats into more human-readable form to compare them."
teaches: A difference between two artifacts should be localised to the nested member and field. Hash inequality alone is not enough evidence.
status: mined
limitation: A diff of the transformed view can hide or invent differences, depending on which converter was used.
province-fit: in — artifact comparison
obscurity: mainstream

ID-SLUG: rb-definition
source: Reproducible Builds — Definitions — https://reproducible-builds.org/docs/definition/
kind: docs
tier: A
scope: the project's definition of a reproducible build and how reproducibility is verified
anchor: "When is a build reproducible?"; accessed 2026-10-29; "A build is reproducible if given the same source code, build environment and build instructions, any party can recreate bit-by-bit identical copies of all specified artifacts."
teaches: "This binary corresponds to source X" holds only as bit-identical rebuild evidence under a declared environment. Anything short of that is inference.
status: mined
limitation: This is a definition, not a reproducibility guarantee for any particular artifact.
province-fit: in — binary provenance claims
obscurity: mainstream

ID-SLUG: source-date-epoch-spec
source: SOURCE_DATE_EPOCH specification (Revision 1.1, 27 November 2017) — https://reproducible-builds.org/specs/source-date-epoch/
kind: spec
tier: A
scope: the normative format and semantics of SOURCE_DATE_EPOCH
anchor: "Specification → SOURCE_DATE_EPOCH"; Rev 1.1 (2017-11-27); accessed 2026-10-29; "The value MUST be an ASCII representation of an integer with no fractional component, identical to the output format of date +%s ."
teaches: An embedded build timestamp may be a clamped SOURCE_DATE_EPOCH, not the actual build time. Record it as the declared source date.
status: mined
limitation: It does not tell you whether a given artifact's build honoured the variable.
province-fit: in — timestamp evidence in artifacts
obscurity: niche

ID-SLUG: slsa-1.2-threats
source: SLSA v1.2 "Threats & mitigations" (Status: Approved) — https://slsa.dev/spec/v1.2/threats
kind: spec
tier: A
scope: the threats SLSA v1.2 explicitly does not address, which limits what SLSA provenance on a hash proves
anchor: "Dependency threats"; v1.2 Approved; accessed 2026-10-29; "This version of SLSA does not explicitly address dependency threats, but we expect that a future version will."
teaches: SLSA provenance binds an artifact hash to a build process. It does not vouch for the dependencies, so do not raise trust in the artifact's contents.
status: mined
limitation: This covers the threat model only. It does not tell you any artifact's SLSA level. (The v1.0 page is marked "Status: Retired".)
province-fit: adjacent — bounds provenance claims
obscurity: mainstream

ID-SLUG: sigstore-not-guaranteed
source: Sigstore Security Model — "What Sigstore Doesn't Guarantee" — https://docs.sigstore.dev/about/security/
kind: docs
tier: A
scope: Sigstore's own list of things a signature/log entry does not guarantee
anchor: section "What Sigstore Doesn't Guarantee"; accessed 2026-10-29; "If no third parties monitor the logs, then any misbehavior by Rekor and Fulcio might go undetected."
teaches: A valid Sigstore bundle proves an identity-bound signature over a digest, under a trust model that needs log monitoring. It says nothing about whether the artifact is safe.
status: mined
limitation: There is no page revision pin, so it is accessed-date only.
province-fit: adjacent — bounds what a signed hash proves
obscurity: mainstream

ID-SLUG: in-toto-attestation
source: in-toto Attestation Framework README — https://github.com/in-toto/attestation/blob/50bf01716982189898823e90586075f37cd9bb7d/README.md
kind: spec
tier: A
scope: the framework's statement of purpose (verifiable claims about how software was produced)
anchor: README intro; commit 50bf0171; accessed 2026-10-29; "The in-toto Attestation Framework provides a specification for generating verifiable claims about any aspect of how a piece of software is produced."
teaches: An attestation is a signed claim, and verifying it proves who claimed what. Ledger it as the producer's claim, not as an observation about the bytes.
status: mined
limitation: It defines the envelope/statement format, not the truth of any predicate.
province-fit: adjacent — provenance claim format
obscurity: niche

## SBOM / binary composition

ID-SLUG: syft-readme
source: Syft README — https://github.com/anchore/syft/blob/12f0e2d83722544b45507c983590c479fc7bec52/README.md
kind: tool
tier: A
scope: Syft's stated scan targets and output formats
anchor: README tagline; commit 12f0e2d8; accessed 2026-10-29; "A CLI tool and Go library for generating a Software Bill of Materials (SBOM) from container images and filesystems."
teaches: Run an SBOM generator over an extracted firmware rootfs. Its package list mostly comes from package-manager metadata, so record which cataloger made each entry.
status: mined
limitation: Not stated in the README: binaries without package metadata may be missed or only heuristically matched [INFERENCE].
province-fit: in — composition of extracted artifacts
obscurity: mainstream

ID-SLUG: cve-bin-tool-readme
source: CVE Binary Tool README (doc/README.md) — https://github.com/intel/cve-bin-tool/blob/ab93508aacdcd96bf48b8a7d45c40fbe1412062d/doc/README.md
kind: tool
tier: A
scope: the binary-checker approach and how many checkers exist at this commit
anchor: README item 1; commit ab93508a; accessed 2026-10-29; "A binary scanner which helps you determine which packages may have been included as part of a piece of software."
teaches: Binary version checkers work from signatures over embedded strings. They give "may have been included" leads (456 checkers at this commit), not confirmed components.
status: mined
limitation: The README's own wording ("may have been included") rules out reading a hit as confirmed presence or exposure to a CVE.
province-fit: in — static composition leads
obscurity: mainstream

## Research methodology / datasets

ID-SLUG: lfwc-ndss25
source: Helmke, Padilla, Aschenbruck — "Mens Sana In Corpore Sano: Sound Firmware Corpora for Vulnerability Research" — https://arxiv.org/abs/2404.11977 (v4, 21 Nov 2024; accepted manuscript NDSS'25; DOI 10.14722/ndss.2025.230669; NDSS page https://www.ndss-symposium.org/ndss-paper/mens-sana-in-corpore-sano-sound-firmware-corpora-for-vulnerability-research/)
kind: paper
tier: A
scope: the abstract's claims about corpus soundness requirements and LFwC's verified-unpacking design
anchor: arXiv abstract, v4 (2024-11-21); accessed 2026-10-29; "We verify unpacking, deduplicate, identify contents, provide ground truth, and show LFwC's utility for research."
teaches: Unpacking success has to be verified and documented per sample. Unverified extraction output should not be treated as ground truth.
status: mined
limitation: Only the abstract was quoted. The body's figures (e.g. the share of papers that do not describe unpacking) are search-summary leads I did not open.
province-fit: in — evidence discipline for firmware extraction
obscurity: niche

ID-SLUG: lfwc-artifact-repo
source: Linux Firmware Corpus (LFwC) artifact repo README — https://github.com/fkie-cad/linux-firmware-corpus/blob/43647c19c4a22492f1c20a7567c8213c378dac7d/README.md
kind: dataset
tier: A
scope: the LFwC corpus composition and its FACT-based verified-unpacking process, as the authors state them
anchor: README intro; commit 43647c19; accessed 2026-10-29; "We tear down the firmware unpacking barrier with an open source process for verified unpacking success based on the [Firmware Analysis and Comparison Tool (FACT)]"
teaches: The corpus is a source of metadata and scripts for a firmware unpack-success oracle (10,913 images, data until June 2023).
status: mined
limitation: The authors say they share "as much data as legally possible", so not every image may be redistributed.
province-fit: in — firmware ground-truth dataset
obscurity: obscure

## Screened and dropped / rejected leads

- Bluetrum Tools — https://github.com/kagaimiq/bluetrum-tools (opened, commit 5e7f367e): the README describes reading and writing flash on a physical chip over USB/UART ("A simple tool that allows to read and write flash of an bluetrum chip."). That is live-device activity, so it is out of province. Flip condition: if a static Bluetrum image-format parser is documented in the repo.
- frizzoot/BRCM-Unpack — https://github.com/frizzoot/BRCM-Unpack: 4 commits and no visible maintainers or spec; not opened beyond the search snippet.
- Jetset / HALucinator / Pretender / Greenhouse / Pandawan / Khost rehosting papers (USENIX): dynamic emulation and rehosting, so outside artifact-first static scope.
- BinSift thesis (LiU DiVA, diva2:2060854): the record page failed to fetch twice, so it was not opened and is not quoted. Lead only: blind decompression of untagged data.
- NDSS "Sound Firmware Corpora" first URL (/ndss-paper/sound-firmware-corpora-for-vulnerability-research/): 404; replaced by the arXiv v4 and the correct NDSS slug.
- SLSA v1.0 threats page (https://slsa.dev/spec/v1.0/threats): opened but "Status: Retired"; replaced by v1.2.
- U-Boot FIT docs index (https://docs.u-boot.org/en/latest/usage/fit/index.html): only a navigation index pointing to the FIT project; replaced by fitspec.osfw.foundation 1.0.
- third-party comparison blogs (pistack.xyz, berkner.tech, agentwikis, rea-reverse.com): blog mirrors or secondary sources, which the contract excludes.
- MTK scatter / SP Flash Tool orgs (search hits): flashing utilities and possible repackaged binaries; out of province and of untrusted provenance.

## Search log

- Direct primary fetches (GitHub raw at pinned `ls-remote` HEAD; the GitHub API answered for 5 repos and then rate-limited): unblob, binwalk, EMBA, FACT_core, squashfs-tools, sasquatch, jefferson, ubi_reader, uefi-firmware-parser, UEFITool, chipsec, syft, cve-bin-tool, firmware-mod-kit, OFRAK, FwHunt-scanner, cmsis-svd-data, SVD-Loader-Ghidra, in-toto/attestation, squashfs-tools-ng, qc_image_unpacker, bluetrum-tools, payload-dumper-go, TF-A, extfstools, BIOSUtilities, vmlinux-to-elf, linux-firmware-corpus; diffoscope via salsa.debian.org.
- Docs/specs fetched: unblob.org/handlers, docs.u-boot.org FIT index, fitspec.osfw.foundation, source.android.com boot-image-header, AVB README, update_metadata.proto, reproducible-builds.org (definition, SOURCE_DATE_EPOCH), slsa.dev v1.0 and v1.2 threats, docs.sigstore.dev security, open-cmsis-pack SVD spec, devicetree-spec releases page plus the v0.4 PDF (pdftotext), diffoscope.org, arXiv 2404.11977, NDSS paper page.
- web_search queries (4): "obscure firmware extraction tool vendor image format unpacker…" (parallel backend, 10 hits); "firmware rehosting… USENIX dataset ground truth" (10 hits, all dropped as dynamic); "evaluation of firmware unpacking tools accuracy binwalk unblob…" (22 sources, which led to LFwC and BinSift); "\"Sound Firmware Corpora…\" NDSS 2025 Helmke" (10 sources).
- Counts: about 55 identified, 45 screened/opened, 40 kept (39 mined + 1 rejected: chipsec), 9 dropped.
- Obscure picks found via search or ecosystem walking: squashfs-ng-binary-format, extfstools, BIOSUtilities, qc-image-unpacker, tfa-fip-layout, vmlinux-to-elf, svd-loader-ghidra, lfwc-artifact-repo.
- Installs or updates: none.
