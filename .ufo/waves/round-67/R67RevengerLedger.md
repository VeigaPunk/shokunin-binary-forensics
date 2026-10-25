HOLDS — observation/inference/unknown genuinely separated, digests byte-scoped, recheck hash verified on re-run, recorded-vs-re-derived labeling honest; one sub-defect wording finding on item 8's `0xffffffff` sentence (contradicted by the entry's own embedded output two lines later).

# Evidence-ledger attack — `corpus/knowledge/round-67-apk-axml-byte-evidence.md` (v2, admission-status: candidate)

All paths absolute under `/home/vgpnk/Projects/shokunin/revenger-shokunin`. Re-ran `python3 -B corpus/fixtures/apk-r65/readout.py` myself (exit 0).

## Axis 1 — Observation/inference/unknown separation (item 7, `0xffffffff`)

**Item 7 (entry:74-78) — HOLDS.** The resource-map sentence claims the loaded correspondence (`0x0101021b`/`0x0101021c` "are exactly the two framework attribute ids the fixture's authored oracle declares"), explicitly flags it as "the correspondence this entry claims", and disclaims semantics for zero entries ("recorded as observed, and no framework-wide semantics for a zero entry is claimed"). The same correspondence is independently listed under **Inference** (entry:129) — self-consistent, not masquerading. Grounding chain: truth.json `axml_declared.resource_ids` (`truth.json:26-36`, sha256 `27303bae…4f8173` — verified) declares the ids positionally; readout.py:172-175 maps `strings[i]`→`ids[i]` positionally; S038 snapshot :251-253 documents the map as "a uint32_t array mapping strings in the string pool back to resource identifiers". Arithmetic holds: chunk size 44 = 8 header + 9×4.

**`0xffffffff` (entry:88) — HOLDS with one wording finding.** "recorded as observed and treated as null by the readout (readout.py:22)" is literal fact: `NO_INDEX = 0xFFFFFFFF` at readout.py:22, mapped to `None` at :211/:213/:219, and `ns: null`/`element_ns: null` appear in the embedded output at entry:85. **Finding (wording defect, below defect threshold):** the clause "the same constant on `android`-carrying attributes resolves instead through the start-namespace chunk" misdescribes the bytes — the embedded output at entry:85 shows the `android` attributes carry `ns_index: 0`, **not** `0xffffffff`; what resolves through the start-namespace chunk (offset 248, `prefix_index: 0` → `android`, entry:92) is index 0, the *prefix index*. The resolvability claim is correct; "the same constant" is not. Severity minor — no scope inflation, no mislabeled derivation, and the entry's own embedded JSON contradicts only the phrasing.

## Axis 2 — Q09 digest scope

Every digest claims only the exact bytes hashed; all verified on this host:

| claimed digest | target | observed |
|---|---|---|
| `05d2280f…d03e` (947 B) | `corpus/fixtures/apk-r65/fixture.apk` | `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e` ✓ |
| `27303bae…f8173` | `corpus/fixtures/apk-r65/truth.json` | `27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173` ✓ |
| `92e347c3…3976` | `corpus/fixtures/apk-r65/readout.py` | `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976` ✓ |
| `412d9cb4…a74c` | `.ufo/waves/round-65/source-snapshots/rea-android-applications.md` | `412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c` ✓ |
| `c0428612…f4` | `.ufo/waves/round-67/source-snapshots/dex-format.html` | `c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4` ✓ (matches claims.md:47 pin) |

No origin/completeness/authenticity claim anywhere; dex self-consistency is fenced as "declared-header self-consistency facts about one inert member; dex validity is not claimed" (entry:106, raw-verified). Nit (sub-defect): the S041 anchor (entry:4) lists `generator.py` in its file set but carries no digest for it; not an over-claim — omission only, and generator is not re-run this round (its observed sha256 `eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a195930c27c1a` is unclaimed).

## Axis 3 — recheck stdout-sha256 scope (entry:6, entry:166)

Claim: exit 0, exactly 15 stdout lines, SHA-256 `507d79f8…d247`, repo-relative paths only. Re-run: `exit=0`, `wc -l` = 15, `sha256sum` = `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247`, stderr empty, zero absolute paths (`grep -c '^/'` → 0). The claim's scope is exactly the 15 lines and exit code — verified verbatim. Additionally: the full embedded §Reproduce block (entry:172-186) `diff`s identical to my observed stdout — `EMBEDDED-IDENTICAL`.

## Axis 4 — recorded vs re-derived honesty (Comparison, entry:124)

Stated plainly: "Regenerating the fixture from `generator.py` … was round-65 evidence (S041) and is not re-run by this entry; the committed bytes are hash-pinned above." Same statement at entry:149 (Q06). The hash-pin substitute is real (all three digests verified above). Q11 row (entry:154) "No recorded value is presented as re-derived" is accurate against QUALITY.md:23's reject clause; every re-derived claim ("captured from the named command's actual stdout at build time", verified-at :5) is borne out by the byte-identical embedded-vs-observed stdout diff. `readout.py` itself opens only `fixture.apk` (`read_bytes()` at :44; no `truth`/`open` elsewhere) — so the oracle comparison is genuinely record-vs-record, and the round-65 regeneration is correctly labeled cited-not-rerun.

## Supporting anchor checks (all pass)

- S038 snapshot: `struct ResChunk_header` :218; enum block :237-253 with `RES_XML_RESOURCE_MAP_TYPE = 0x0180` at :253 (ResourceTypes.h:237-253 read) — entry:1's new span exact; "It is optional" at :252.
- S043 snapshot :7-8 contains the quoted `inspect_android_package` sentence; :5 is `older server.` — the corrected anchor is right, and the entry's characterization of the old citation is accurate.
- S045 snapshot: `header_size` cell reads "must be 0x70 (112) bytes (v40 or earlier)" (dex-format.html ~:5975-5985); `checksum`/`signature` quotes verbatim (:5949, :5956); `ENDIAN_CONSTANT = 0x12345678` (:5035). The "(v40 or earlier)" qualifier belongs to header_size's value cell, not file_size's — entry:106 cites it correctly for `035`.
- Item 8 provenance (entry:81): S038 :675 "Appears header.headerSize bytes after a ResXMLTree_node" and :686-687 "Byte offset from the start of this structure where the attributes start" — quoted verbatim; `aoff = base + 16 + attribute_start + i * attribute_size` at readout.py:203 matches `chunk_base + 16 + attributeStart + i*attributeSize`.
- `4d616e69666573742d56657273696f6e` = "Manifest-Version" — the M39 fix is real 16 bytes; retained r65 candidate still carries drifted `4d616e696673742d` at its :41 with `admission-status: rejected` (byte-preserved red-before surface ✓).
- No `### Code` pointer remains; §Reproduce names the script path directly.
- Item 2 arithmetic: 737+188=925 ✓; item 4 walk: 8→204→248→272→368→392→416 ✓.

## Verdict line

HOLDS. Findings (sub-defect, for L1 weighing): **item 8** — "the same constant on `android`-carrying attributes" should read "the same index space"/"index 0"; the attributes carry `ns_index: 0`, not `0xffffffff` (entry:85 vs entry:88). S041 anchor omits a digest pin for `generator.py` (omission, not over-claim). No inference masquerades as observation; Q09 scope clean; recheck hash re-derived identical; recorded-vs-re-derived labeling honest.
