# Round 59 — independent non-author review

## Verdict

**Declared calibration claim unmet.** The one-byte mutation is exactly as declared, and strict UTF-16LE rejects its unpaired low surrogate, but the saved REA result is a successful complete inspection, not an `invalid-format` refusal. It carries Evidence ID `ev_8ab30e10bf3d0e73c44c831c9cbb1839d1117db21379e163085ab9d8fec0f8db` and a JSON string `A=\ude00B!` containing an unpaired surrogate. This is a useful, reproducible *discovered gap*, not a successful prediction or an improved calibration result.

Per axis: **calibration: harmed relative to the declared validity/refusal expectation** (the static parser reports a malformed UTF-16 name as a successful Unicode string; do not misstate this as a regression against a previously tested malformed-name baseline). **Depth: unchanged**—the same three resource payloads and relationships were retained, with no added depth result. **Coverage: unchanged**—the saved inventory reports complete coverage of this small fixture; no evidence of a coverage loss. The honest falsification and new negative case improve knowledge of the boundary, not the declared calibration axis. No existing r55 valid-name behavior was retested or shown harmed.

## Reproducible, read-only checks and exact output

The only REA producer command was already recorded in `receipt.json`, not run by this reviewer:

```text
npx -y rea-agents@6.4.0 inspect-pe-resources /home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/fixtures/pe-r59/fixture.exe --format json
```

I read the fixture files as bytes with Python, compared all offsets, decoded the name with `bytes.decode('utf-16le', 'strict')`, parsed the PE resource directory and group payload with `struct.unpack_from`, and compared the resulting values to the saved JSON. The direct Python checks produced:

```text
r55 size=1536 sha256=41c0132a9ecd8274d9afcfc079fefc0c5beb14c1ae81bc7bfa0a2832e140572b
r59 size=1536 sha256=2d294161e9eebd965919aad91065e5335e693199a17d95533f6c6c8fc751e6a0
mutations: [(741, '0xd8', '0x0')]
name location=736 bytes=12; count=5; name UTF-16LE raw=41003d0000de42002100
strict: UnicodeDecodeError 'utf-16-le' codec can't decode bytes in position 4-5: illegal encoding
surrogatepass: 'A=\ude00B!'
truth source_sha256/sha256/invalid_name_utf16le_hex/changed_offsets match independently: True True True True
```

A resource-tree walk anchored at the PE `.rsrc` raw offset 512 found the following three leaves. For **each** leaf, independently extracted payload equals r55 payload byte-for-byte; the computed hash, RVA/offset/size, data-entry offset, three directory-entry offsets, code-page/reserved values, type and language all match saved `normalized_result.resources` (`True` for every check):

```text
index  path (type,name,language)                   data-entry  payload RVA/offset/bytes    payload SHA-256
0      (ID3, ID1, ID1033)                         672         8448/768/48                 d7aaca7bc7951c9249a7798838189374fa953d3def03aebb375ee731768e5003
1      (ID3, ID2, ID1033)                         688         8512/832/48                 2f503cace29956c75acd5356de2f8fa98485b01edd654daf0f81a739b44c82ae
2      (ID14, name raw 41003d0000de42002100,
        ID1033)                                   704         8576/896/34                 45eb70319667352d8bfea3249f7fb30166c6835d2cf564b5ec303bf2d716c17a
old name raw=41003dd800de42002100; old/new group payload byte-identical: True
saved malformed name equals surrogatepass decode: True
```

Group payload at offset 896: `00000100020001010000010020003000000001000202000001002000300000000200`. Its independent header decode is `(reserved=0, type=1, count=2)`; its two 14-byte links are, respectively, `(width=1, height=1, colors=0, reserved=0, planes=1, bits=32, declared=48, resource ID=1)` at offset 902 and `(2, 2, 0, 0, 1, 32, 48, ID=2)` at offset 916. Resource IDs 1 and 2 resolve respectively to icon leaves 0 and 1 in language 1033; their 48-byte payload sizes match. All saved `icon_groups[0].images` values, locations, candidate indices `[0]`/`[1]`, same-language indices `0`/`1` and `size_matches=true` matched the independently decoded links (`[True, True]`). Saved `resource_index=2` matches the group leaf.

Receipt comparison against actual saved files:

```text
inspection.stdout.json sha256=bf7922dbda2bc2dd817eaa13652f04e19c10ed8701feab5790a8703d55f22c0f
inspection.stderr.txt   sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 (0 bytes)
receipt fixture_sha256/stdout_sha256/stderr_sha256/evidence_id all match: True
receipt exit_code=0; saved output operation=inspect_pe_resources; coverage={status: complete, examined_entries: 8, resources: 3}
saved output Evidence ID=ev_8ab30e10bf3d0e73c44c831c9cbb1839d1117db21379e163085ab9d8fec0f8db
```

**Evidence-ID distinction:** the declared *refusal without successful Evidence ID is absent*. A successful Evidence ID is explicitly **present** in both saved stdout and receipt. Saved stderr is empty, not an invalid-format diagnostic.

## Evidence boundary

- **OBSERVATION:** Exact single-byte `d8→00` at offset 741; intact three payloads and both icon-group links; strict UTF-16LE decode fails; saved REA stdout contains the lone low surrogate, a complete inventory and successful Evidence ID; receipt hashes match saved artifact/stdout/stderr. The named Evidence ID cites the *successful saved REA observation*, not the predicted refusal. Truth metadata agrees with the independently checked bytes, but is not used as its own proof.
- **INFERENCE:** The parser accepted a malformed group-name encoding without scalar-value validation (at least on this saved fixture/operation). Its resulting JSON string should not be treated as a valid Unicode scalar name. The declared calibration improvement failed; the boundary gap is worth tracking and, if in scope, escalating to the REA PE-resource parser owner with the fixture SHA-256, mutation, raw name bytes and saved Evidence ID. Any claim that real Windows would accept or reject the malformed resource would be speculation.
- **UNKNOWN:** Actual shell/Windows loader behavior, icon image decoding, and whether other malformed-surrogate cases behave similarly. Receipt and hashes validate the saved local result; they do not independently prove a fresh producer run or an upstream fix.

**Next action:** Record round 59 as falsification rather than relabeling the claim. Escalate the bounded parser gap if the project owns/wants to report REA validation behavior. A new round is appropriate only for a newly declared acceptance criterion (for example an upstream fix/rejection or explicit preservation of raw malformed names); do not rerun the identical producer call to rescue this claim. No PE execution, producer rerun, commit, push or merge was performed here.
