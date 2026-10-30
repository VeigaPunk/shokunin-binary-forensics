# bf-source-pack / ecosystems (round-73)

Slice: ecosystem-specific primary docs/code acting as independent oracles for REA routes.
Opened: 2026-10-29 via `curl -sL --max-redirs 15` (HTTP 200, text extracted locally, quotes grep-verified against the extracted text). Nothing installed or executed; no sample downloaded.
De-scope (per SHOKUNIN_BINARY_FORENSICS IRC): DEX/Dalvik, Il2CppDumper/Il2CppInspector, GoReSym, blutter/reFlutter and other Go/Rust/pyc/il2cpp/Flutter *extractors* are not in this slice. Rust v0 (a spec, not an extractor) is kept.
Installs/updates: none.

search-log: where = candidate list in assignment + REA doc crosswalk (`~/.local/share/rea/docs/*.md`, read heads/greps) + GitHub API for revisions (`gh api repos/<o>/<r>/commits`). identified 27, screened 22, included 16, excluded 6 (3 rejected-opened, 3 de-scoped), leads 5 (unopened/unreachable URL variants).

---

## 1. APK Signature Scheme v2
- title: https://source.android.com/docs/security/features/apksigning/v2
- kind: spec
- tier: A
- scope: APK Signing Block container layout (size/ID-value pairs/magic), v2 block ID, v2 verification steps; Android 7+ semantics. Not v3 rotation, not v4.
- anchor: sections "APK signing block" > "Format" and "APK signature scheme v2 verification"; page footer "Last updated 2026-09-30 UTC."
- quote: "The v2 signature of the APK is stored as an ID-value pair with ID 0x7109871a." (APK signing block intro)
- teaches: locate the block via EOCD → central-directory offset → 16-byte magic `APK Sig Block 42`, check the two size fields match, then walk uint64-length-prefixed ID/value pairs; check "EOCD not followed by more data" rule.
- obscurity/value: the byte-level oracle for every APK signing claim; also lists the verification invariants (two equal size fields, no trailing bytes) that tampering/repack triage needs.
- rea-route: apk-signature (REA parses "ZIP tail and the APK Signing Block" and recomputes content digests; this page is the independent layout oracle).
- limits: does not give digest-chunking numeric details beyond prose in this extract; says nothing about v3.1/v4; vendor (Google) statement of behaviour, not a test vector set.

## 2. APK Signature Scheme v3 (key rotation)
- title: https://source.android.com/docs/security/features/apksigning/v3
- kind: spec
- tier: A
- scope: v3 block ID, SDK min/max per signer, proof-of-rotation lineage and self-trusted-old-certs; Android 9+. Not v3.1 (rotation targeted at SDK ranges), not v4.
- anchor: sections "APK signature scheme v3 block" and "Proof-of-rotation and self-trusted-old-certs structs"; "Last updated 2026-09-30 UTC."
- quote: "The v3 signature of the APK is stored as an ID-value pair with ID 0xf05368c0."
- teaches: decode a lineage as a singly-linked list ordered oldest-root-first where each node's cert signs the next; distinguish what a rotated signer asserts to third parties vs what the app itself still trusts.
- obscurity/value: rotation lineage is the least-documented part of APK trust; this is the only primary statement of the node/flag semantics REA reports as `lineage`.
- rea-route: apk-signature ("Key rotation (v3/v3.1): the declared proof-of-rotation lineage, oldest…").
- limits: v3.1 ID/layout not covered on this page (REA reads v3.1; gap — separate AOSP source needed); no test vectors.

## 3. APK Signature Scheme v4 (.idsig / Merkle)
- title: https://source.android.com/docs/security/features/apksigning/v4
- kind: spec
- tier: A
- scope: v4 `.apk.idsig` structures (hashing_info, signing_info, Merkle tree), fs-verity relationship, Android 11+; incremental install only.
- anchor: top section and struct listings ("struct hashing_info.bytes", "struct signing_info.bytes"); "Last updated 2026-09-30 UTC."
- quote: "A v4 signature requires a complementary v2 or v3 signature."
- teaches: parse an `.idsig` sidecar (hash_algorithm=1 SHA256, log2_blocksize=12, salt ≤32 B, raw_root_hash) and cross-check `apk_digest` against a v2/v3 digest; know v4 is never standalone trust.
- obscurity/value: sidecar format few analysts have seen; protects against treating a lone `.idsig` as proof of signer.
- rea-route: none today (apk-signature doc covers v1/v2/v3/v3.1 only — recorded as a coverage gap, not a claim about REA internals).
- limits: Android 11+ incremental-install path; says nothing about APK Signing Block contents.

## 4. Electron Fuses
- title: https://www.electronjs.org/docs/latest/tutorial/fuses
- kind: docs
- tier: A
- scope: Electron fuse wire layout (sentinel, fuse_version, fuse_wire_length, per-byte state `0`/`1`/`r`) and fuse semantics for the current docs line; app-specific fuse support varies by Electron version.
- anchor: section "Fuse Wire / Sentinel / Fuse Schema" glossary + "| ...binary | sentinel_bytes | fuse_version | fuse_wire_length | fuse_wire | ...binary |"; upstream `electron/electron` docs/tutorial/fuses.md last commit cea20e3ae385c809cacbdd3c95caa1703af575a3 (2026-09-12); repo HEAD 0acb55821bbc6bd2aad37877be2824896feb345c.
- quote: "sentinel_bytes is always this exact string: dL7pKGdnNz796PbbjQWNKmHXBZaB9tsX" (manual-flip section)
- teaches: locate the wire by searching for the 32-byte sentinel, read version/length bytes, interpret 0x30/0x31/0x72 (`r` = removed, flipping has no effect); explains why flips are made pre-signing so OS code-signing guards them.
- obscurity/value: a static, file-only way to answer "will this packaged app honor `--inspect`, RunAsNode, ASAR integrity?" without launching it.
- rea-route: electron-fuses (REA reports `sentinel_offset`, `wire_version`, `declared_length`, ordered fuses with raw bytes).
- limits: per-fuse index→name table depends on schema version (see `@electron/fuses` source; not opened here); does not describe bytes REA sees in multi-sentinel universal binaries.

## 5. Electron ASAR Integrity
- title: https://www.electronjs.org/docs/latest/tutorial/asar-integrity
- kind: docs
- tier: A
- scope: runtime ASAR integrity (macOS electron>=16, Windows electron>=30); the `integrity` header object, header-hash verification, dependency on `EnableEmbeddedAsarIntegrityValidation` + `onlyLoadAppFromAsar`.
- anchor: sections "Version support", "How it works", "Enabling ASAR integrity in the binary"; upstream docs/tutorial/asar-integrity.md last commit 8b057176618af9a47afed2a2e869932ebfc9093f (2026-02-18).
- quote: "If no hash is present or if there is a mismatch in the hashes, the app will forcefully terminate."
- teaches: ASAR header JSON carries `algorithm`, `hash`, `blockSize`, `blocks[]`; only the *header* hash is verified at runtime from a value recorded at packaging time; integrity is ineffective unless app-only-from-asar is also on.
- obscurity/value: pins what "integrity enabled" actually proves (header hash, not each file) — the correct limit for any tamper-evidence claim about an Electron app.
- rea-route: electron-fuses (EnableEmbeddedAsarIntegrityValidation / OnlyLoadAppFromAsar) and electron-observation (static ASAR analysis).
- limits: documents platform support only for macOS and Windows; does not state where the expected header hash is stored in each platform's binary/plist.

## 6. ASAR archive format (electron/asar README)
- title: https://github.com/electron/asar (README.md "Format")
- kind: code
- tier: A
- scope: ASAR container layout: Pickle-serialized header size + JSON header + concatenated file bytes; `offset` base; per-file `integrity`.
- anchor: README.md "## Format"; repo commit fde819a77fea5f6ca4f5f774cc78e033c04efc9f (2026-10-26); README last-changing commit 01bc908255640c544ac68ea2fe14926a7b80da37 (2026-08-18).
- quote: "The `header` is a JSON string, and the `header_size` is the size of `header`'s `Pickle` object."
- teaches: compute real file offset = Pickle(header_size) 8 B + header Pickle size + `offset`; offsets are decimal *strings* in JSON; per-file `integrity` blocks mirror the doc in #5.
- obscurity/value: maintainer-owned format description; the Pickle framing is the usual stumbling block when hand-parsing `app.asar`.
- rea-route: electron-fuses / electron-observation (ASAR paths `app.asar/...`), javascript-artifact-reconstruction (static ASAR read).
- limits: prose only; unpacked-file (`unpacked`) and link entries beyond this section not traced; Pickle padding details are not spelled out.

## 7. Chrome DevTools Protocol (index / scope statement)
- title: https://chromedevtools.github.io/devtools-protocol/
- kind: spec
- tier: A (scope: CDP trust/support model and which protocol snapshots exist; not any domain's semantics)
- scope: protocol framing (JSON commands/events, domains), support policy, snapshots (tip-of-tree, v8-inspector, stable @ Chrome 64).
- anchor: sections "Scope and support" and "Protocol API docs"; repo ChromeDevTools/devtools-protocol HEAD a45ae55ca46eeb4c6768011da4470ec0f103d01c (2026-10-29). Page carries no revision stamp.
- quote: "CDP exposes a wide range of high-privilege capabilities, so protocol clients are assumed to be trusted."
- teaches: CDP targets are privileged control surfaces and not a stable API: an evidence record must name which protocol snapshot a target spoke; Node/Electron main-process debugging uses the v8-inspector subset.
- obscurity/value: the authoritative statement that CDP availability gates (e.g. Electron `EnableNodeCliInspectArguments`) change what an observer can see.
- rea-route: electron-observation, browser-observation (CDP provider authorities); crosswalk with electron-fuses (inspector flag gate). Note revenger policy: static artifact reading first; connecting to a live target is outside the lane.
- limits: this page only; per-domain command reference is the tip-of-tree/stable JSON (not opened); no wire examples here.

## 8. Devicetree Specification, Flattened Devicetree (DTB) Format
- title: https://devicetree-specification.readthedocs.io/en/stable/flattened-format.html
- kind: spec
- tier: A
- scope: FDT header fields, versions 16/17, structure/strings/memory-reservation blocks, tokens, alignment. Header of rendered page: "Devicetree Specification v0.3-dirty" (stable build).
- anchor: "5. Flattened Devicetree (DTB) Format" §5.1 Versioning, §5.2 Header; source `source/chapter5-flattened-format.rst` last-changing commit 2697c66a59b9177f8ff7813c355cc7aa05f6e40a (2024-02-05); repo HEAD 8314f1e1c9965482e5c1080d4118f52fef827fce (2026-09-23). Also read the rst at HEAD ("This document describes only version 17 of the format").
- quote: "This field shall contain the value 0xd00dfeed (big-endian)."
- teaches: validate a DTB header (magic, totalsize covers header + blocks + trailing free space, `last_comp_version`=16 for v17), compute block offsets, and know that all integers are big-endian.
- obscurity/value: the independent oracle for DTB bounds checking; the "free space gaps between blocks" rule explains DTB trailing padding a parser must not call corruption.
- rea-route: devicetree (REA supports FDT v16/v17; v16 has no `size_dt_struct`).
- limits: format only; the "stable" readthedocs build is older (v0.3-dirty) than repo HEAD; property/binding semantics (chapters 2-4, Linux bindings) not covered here.

## 9. SQLite Database File Format
- title: https://www.sqlite.org/fileformat2.html
- kind: spec
- tier: A
- scope: main-database-file layout (100-byte header, page types, freelist, record format, schema table), WAL and rollback journal semantics; SQLite 3 format, current doc.
- anchor: "1.3 The Database Header" (table "Database Header Format", 1.3.1 Magic Header String, 1.3.2 Page Size), "1.5 The Freelist", "4. WAL File Format"; page footer "This page was last updated on 2025-12-25 10:33:36Z".
- quote: `The header string: "SQLite format 3\000"` (Database Header Format table, offset 0)
- teaches: validate the first 16 bytes and offsets (page size @16, reserved-bytes @20, change counter @24, freelist head/count, schema format number); recover deleted rows from freelist/unused areas; know that a "hot" journal/WAL may hold committed state not in the main file.
- obscurity/value: the canonical reference for carving/validating SQLite artifacts and for explaining why a DB copy without its `-wal` is an incomplete observation.
- rea-route: sqlite-databases (REA copies database + sibling `-wal` and records separate SHA-256 identities).
- limits: no recovery tooling or freeblock carving recipes; no forensic-specific heuristics.

## 10. Linux kernel module signing facility
- title: https://docs.kernel.org/admin-guide/module-signing.html
- kind: docs
- tier: A
- scope: what a signed `.ko` is and how the kernel treats it (appended signature, marker string, stripping limits, key types RSA/ECDSA/ML-DSA); Linux 7.3.0 docs build.
- anchor: section "Signed modules and stripping"; source Documentation/admin-guide/module-signing.rst last commit 0ad9a71933e73c8a2af101d28e9a1dc35bae02d5 (2026-02-02); kernel HEAD c339f4010dea8b0d754f84ace70cd1b089878ef8.
- quote: "Signed modules are BRITTLE as the signature is outside of the defined ELF container."
- teaches: the signature is appended *after* the ELF; the marker `~Module signature appended~` only shows a signature is present, not valid; stripping after signing invalidates it; signed payload includes debug info.
- obscurity/value: explains why section-level ELF tools do not see the signature and why REA's "appended signature trailer" is a separate observation from ELF structure.
- rea-route: kernel-modules (`.modinfo`, `__versions`, appended signature trailer).
- limits: does not give the struct layout (see #11); acceptance policy depends on kernel config (lockdown, sig_enforce), not on the file.

## 11. Linux uapi `module_signature.h`
- title: https://raw.githubusercontent.com/torvalds/linux/master/include/uapi/linux/module_signature.h
- kind: code
- tier: A
- scope: on-disk trailer struct `module_signature` and `MODULE_SIGNATURE_MARKER`; PKCS#7 id_type only.
- anchor: lines 15-39 (`MODULE_SIGNATURE_MARKER`, `struct module_signature`); last-touching commit f9909cf0a2dcc9e99377f3fcc965ccd93e518e34 (2026-03-24); fetched from master 2026-10-29.
- quote: `#define MODULE_SIGNATURE_MARKER "~Module signature appended~\n"` (line 15)
- teaches: read the trailer backwards from EOF: marker, then 12-byte info block `{algo,hash,id_type,signer_len,key_id_len,pad[3],sig_len(be32)}`, then signature data, key id, signer name in that order.
- obscurity/value: exact byte layout (big-endian `sig_len`) that no doc page spells out; the oracle for validating a trailer parser.
- rea-route: kernel-modules (appended signature trailer reading).
- limits: header only; algorithm/hash id numbering is "[0]" in the header (unspecified here); ML-DSA specifics not in this file.

## 12. Erlang/OTP BEAM loader `beam_file.c`
- title: https://raw.githubusercontent.com/erlang/otp/master/erts/emulator/beam/beam_file.c
- kind: code
- tier: A
- scope: runtime reading of the `FOR1`/`BEAM` IFF container: form-type check, chunk framing (id, size, 32-bit-aligned storage), chunk-id table (`AtU8`,`Code`,`StrT`,`ImpT`,`ExpT`,`FunT`,`LitT`,`Attr`,`CInf`,`Line`,`LocT`,`Atom`…).
- anchor: `read_beam_chunks()` ~lines 1536-1585 and `beamfile_read()` chunk id table ~lines 1586+; last-touching commit 6fbf8a305e09b3fb5246d917f3c906d3ee9ad68c (2026-09-17); repo HEAD a6f47dbec54001cd4358ee37115c496840e7f4de (2026-10-28).
- quote: "Chunk storage is aligned to the next 32-bit boundary, so we'll need to skip (but not read)" (comment, line 1564)
- teaches: derive the 4-byte padding rule and that the loader scans all chunks and, for each wanted id, overwrites the slot (`chunks[i].data = chunk_data;`, line 1575) — i.e. a later duplicate chunk wins [INFERENCE from the loop; matches REA's "last occurrence of each name, matching OTP's loader"].
- obscurity/value: ground truth for duplicate-chunk and trailing-byte behaviours that BEAM docs omit; independent oracle for REA's chunk table.
- rea-route: erlang-beam.
- limits: runtime loader, not a spec; compressed/`.beam` wrapped formats and `beam_lib` APIs not covered; behaviour is for the sampled OTP commit only.

## 13. Godot `file_access_pack.{h,cpp}` (PCK reader)
- title: https://raw.githubusercontent.com/godotengine/godot/master/core/io/file_access_pack.cpp (+ file_access_pack.h)
- kind: code
- tier: A (scope: PCK formats 2/3/4 as read by the engine at this commit; there is no separate official byte-level PCK doc — see LEADS)
- scope: header fields (magic `GDPC`, version, engine ver major/minor/patch, flags, file_base, dir_offset, reserved), directory, per-file flags (encrypted/removal/delta), V2 vs V3/V4 differences, sparse bundle/salt.
- anchor: file_access_pack.h lines 40-60 (`PACK_HEADER_MAGIC 0x43504447`, `PackFlags`, `PackFileFlags`); file_access_pack.cpp lines ~286-370 (header parse, directory read). .cpp last-touching commit 6103c0bc4240f5e63408ec08cbbac076a7627b61 (2026-04-29); .h fdda64e59e32b20e1f95c5e82ae3c332b7e13b24 (2026-03-11); repo HEAD cafc17a192acf67903910a68aeb3c076c0907a4b (2026-10-28).
- quote: `// Godot's packed file magic header ("GDPC" in ASCII).` (file_access_pack.h line 40)
- teaches: parse PCK start (embedded packs: `pck_start_pos`), the V3/V4 `dir_offset` jump, the `file_base += pck_start_pos` rule, encrypted-directory handling, and that V2 reads 16 reserved u32s.
- obscurity/value: the only primary byte-level source for PCK; independently checks REA's "formats 2, 3 and 4; format 1 unsupported".
- rea-route: godot-pck.
- limits: reader code, not a specification; per-file record layout (path, offset, size, MD5) is beyond lines read here; engine at HEAD supports V4 which REA verifies only on tested releases.

## 14. EDK2 `PiFirmwareVolume.h` (PI firmware volume header)
- title: https://raw.githubusercontent.com/tianocore/edk2/master/MdePkg/Include/Pi/PiFirmwareVolume.h
- kind: code
- tier: A for the `EFI_FIRMWARE_VOLUME_HEADER` field layout and `_FVH` signature as defined by the reference implementation (header says "Revision Reference: PI Version 1.6"); B for anything claimed about later PI versions.
- scope: FV header: ZeroVector[16], FileSystemGuid, FvLength, Signature `_FVH`, Attributes, HeaderLength, Checksum, ExtHeaderOffset, Revision=2, BlockMap.
- anchor: `EFI_FIRMWARE_VOLUME_HEADER` lines ~98-152; last-touching commit 21e021ffbaa738956fb8142cf5cf215eeb71e50b (2026-02-27); repo HEAD fde052fbd89c35617e14f628ca96e2d9ceff6c6f (2026-10-29).
- quote: "A 16-bit checksum of the firmware volume header. A valid header sums to zero." (line 128)
- teaches: carve FVs by scanning for `_FVH` at offset 40 (after 16-byte zero vector + 16-byte GUID + 8-byte length), verify 16-bit header checksum, read the block map to find length.
- obscurity/value: stands in for the UEFI PI spec, whose pages return HTTP 403 to automated clients today (LEADS).
- rea-route: firmware-analysis (Binwalk/Unblob regions — an independent check of whether a reported FV region has a valid `_FVH` header).
- limits: defines the volume header, not FFS file/section headers (`PiFirmwareFile.h`, not opened) nor the PI spec text; not the vendor-modified layouts seen in real firmware.

## 15. PyInstaller `PyInstaller/archive/readers.py` (CArchive cookie/TOC)
- title: https://raw.githubusercontent.com/pyinstaller/pyinstaller/develop/PyInstaller/archive/readers.py
- kind: code
- tier: A (maintainer source; scope: CArchive cookie and TOC entry format as the project's own reader parses it at this commit). The prose doc https://pyinstaller.org/en/stable/advanced-topics.html (6.22.3) describes the same archive at a high level but its "Structure of the CArchive" body is a collapsed section not present in the extracted text → B/context only.
- scope: cookie `MEI\014\013\012\013\016` + `'!8sIIII64s'`, TOC entry `'!IIIIBc'` + name.
- anchor: `CArchiveReader` lines 38-80, `_COOKIE_FORMAT`, `_TOC_ENTRY_FORMAT`; last-touching commit 54fa8355b279bc57803385f23c25477a7efe238a (2025-08-31); repo HEAD 44697216a20cbadff64cce2b806e3d67cffcbbc8 (2026-10-25).
- quote: "char name[1]; /* Variable-length name, padded to multiple of 16 */" (line 71)
- teaches: find the cookie by magic, read `pkg_length`, `toc_offset`, `toc_length`, `python_version`, 64-byte libname; entries are big-endian with variable length; offsets are relative to archive start.
- obscurity/value: maintainer ground truth for the layout REA calls CArchive 2.0/2.1; gives an independent check of Python-version/libname extraction.
- rea-route: python-packaged-applications (and python-pyc for the embedded modules).
- limits: PyInstaller ≥ the commit read; the older 2.0 cookie shape (no 64-byte libname) is not shown here; extraction/decryption (`pyimod00_crypto_key`) not covered.

## 16. rustc book — v0 Symbol Format
- title: https://doc.rust-lang.org/rustc/symbol-mangling/v0.html
- kind: spec
- tier: A
- scope: Rust v0 mangling grammar (`_R` prefix, paths, instantiating crate, disambiguators, generics); not legacy `_ZN…E` mangling.
- anchor: "v0 Symbol Format" > "Symbol name" grammar; source src/doc/rustc/src/symbol-mangling/v0.md last commit e574edfbac1e8cc64da3834d83f1ebe63f3ebd1d (2026-07-30); repo HEAD ce37c4ff837c5c5dc45cddf9e1e3704e42ca67ea.
- quote: "A mangled symbol starts with the two characters _R which is a prefix to identify the symbol as a Rust symbol."
- teaches: decode `_RNvCs…` symbols into crate/disambiguator/path and generics without a demangler; extract crate hash + name from a stripped binary's symbol table.
- obscurity/value: complements cargo-auditable dependency data with a symbol-level, crate-hash oracle that survives when auditable sections are stripped.
- rea-route: none directly (rust-binaries reads cargo-auditable; this grounds the native-function-matching / symbol-name side — recorded as a cross-route, not a claim).
- limits: toolchains still emit legacy mangling by default in places; grammar only, not a demangler test suite.

---

## Rejections (opened)
- REJECTED: https://www.erlang.org/doc/apps/erts/beam_makeops.html — wrong scope for the BEAM *file* format: "This document describes the beam_makeops script." (Introduction); it documents the build-time opcode generator. flip: a section of this doc that specifies the on-disk container; none found.
- REJECTED (as format oracle): https://docs.godotengine.org/en/stable/tutorials/export/exporting_pcks.html — user/export guide, not byte-level: "This is a security vulnerability in three scenarios." (Security concerns); no header or directory layout. flip: a docs page specifying the PCK binary layout (404 at engine_details/file_formats/pck.html).
- REJECTED (as primary): https://blog.stenmans.org/theBeamBook/ — opened (HTTP 200, 1.4 MB) but is a book; the BEAM file-format section was not located by keyword in the converted text, so no verbatim format quote; tier C at best. flip: a located chapter quote on chunk layout with a book revision.

## De-scoped (not opened this run, by instruction)
- Dalvik bytecode / dex-format (source.android.com), Il2CppDumper, Il2CppInspectorRedux, GoReSym, blutter, reFlutter, Mandiant Go RE blog: covered by peer lanes per SHOKUNIN_BINARY_FORENSICS IRC. (Fetched HTTP 200 for dalvik-bytecode, GoReSym, blutter, Il2CppDumper during probing but not read for quotes — do not cite from this pack.)

## LEADS (unopened / unreachable)
- UEFI PI Specification, Firmware Volume Format: https://uefi.org/specs/PI/1.8A/V3_Firmware_Volume_Format.html — HTTP 403 (also /specs/PI/1.8/…, /specs/PI/1.9/…, PI_Spec_1_8A_Final.pdf, PI_Spec_1_7_A_final_May1.pdf; with browser UA and referer; `read` tool also HTTP 403). Substituted by #14.
- Godot byte-level PCK doc: https://docs.godotengine.org/en/stable/engine_details/file_formats/pck.html and …/contributing/development/file_formats/pck.html — HTTP 404 (no official PCK format page found; engine_details/file_formats lists tscn only). Substituted by #13.
- `@electron/fuses` schema (https://raw.githubusercontent.com/electron/fuses/main/src/constants.ts — fetched HTTP 200, repo HEAD a523b7674fd07da6740e69c4cbd3f4e16dcbebdd, SENTINEL equals the doc's; FuseState adds INHERIT=0x90 for config-only) — only skimmed, not quoted; per-version fuse name table not verified.
- ChromeDevTools `json/browser_protocol.json` / `js_protocol.json` — not opened; needed for per-domain claims.
- Linux `Documentation/ABI`/`modinfo` man page for `.modinfo` key set — not opened.

counts: included 16, rejected 3, leads 5.
