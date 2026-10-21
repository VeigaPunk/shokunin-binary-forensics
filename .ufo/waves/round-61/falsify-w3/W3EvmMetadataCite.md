GRADE: HOLDS — C09 header cites S019 "§Encoding of the Metadata Hash in the Bytecode" and the Unknown sentence "CBOR metadata tail that solc appends by default"; both are verbatim on the re-opened page, and S019 is tier A for exactly that scope and was opened in round 61.

## Observation (source re-opened 2026-10-21)

- URL `https://docs.soliditylang.org/en/latest/metadata.html`, HTTP 200. `curl -sSI` headers: `date: Wed, 21 Oct 2026 16:42:39 GMT`, `last-modified: Tue, 29 Sep 2026 13:01:07 GMT`. Body 38117 bytes, SHA-256 `3407a364bf99c6a0b85bedc83d71afb4252fcef76bad8eeb5d5d9eca04c9ba64`.
- Page identity string in the served HTML: `Solidity 0.8.38-develop documentation` — matches S019 (`corpus/SOURCES.md:33`) "page \"Solidity 0.8.38-develop documentation\", last-modified 2026-09-29". The last-modified header matches to the day.
- Section name verbatim: `<h2>Encoding of the Metadata Hash in the Bytecode` with anchor `#encoding-of-the-metadata-hash-in-the-bytecode`. Exact match to the C09 `source:` header (`corpus/knowledge/evm-saved-interface-candidates.md:1`).
- "by default" in the cited section, verbatim (25 words): "currently by default appends the IPFS hash (in CID v0) of the canonical metadata file and the compiler version to the end of the bytecode". Same page, intro paragraph: "The compiler appends by default the IPFS hash of the metadata file to the end of the runtime bytecode".
- CBOR is the encoding of that appended blob, same section: "this information is stored CBOR-encoded"; "The last two bytes in the bytecode indicate the length of the CBOR encoded information."
- Opened in round 61, independently: `.ufo/waves/round-61/build/SrcSolidityMetadataTail.md:7-8` records the same URL opened HTTP 200 (38117 bytes, identical headers), `:27` drafts the row as docs/A for "placement, encoding and delimiting of the CBOR metadata tail that solc appends to runtime bytecode", `:52` verdict. Landed row S019 (`corpus/SOURCES.md:33`) keeps tier A and narrows scope to "placement ... by default" — narrower than what the seat mined, and the entry only uses placement/default.

## Check of the entry's use

- `evm-saved-interface-candidates.md:72` — "the CBOR metadata tail that solc appends by default (S019). None is in these fixtures." Docs name "the compiler", i.e. solc, and state the default append; "CBOR metadata tail" is faithful to "stored CBOR-encoded" at the end. No overstatement: the entries' fixtures indeed end without one — decoded tails are `...57005b00` (r19, r21, r25, r26), `...5b005b00` (r22), `...ee005000` (r23), `...00005000` (r24); no `0xa1`/`0xa2` map byte in the last six bytes of any fixture.
- The page's own qualifier "runtime bytecode (not necessarily the creation bytecode)" is absent from the entry, but the entry asserts nothing about creation bytecode, so this is silence, not contradiction.
- The Q01 basis cell (`:108`) lists S016/S017/S018/S026 but not S019; the S019-backed sentence is a limitation statement and the row is tier A, so Q01 is not failed by that omission. Minor documentation note only.
- `corpus/lessons/round-61.md:58` locates the opening under "§Contract Metadata, para 1" while the entry/row cite the §Encoding section. Both locations carry "by default" verbatim, so the two records do not conflict; the entry's own citation is the one with the section name and it is supported.

## Provenance

- Raw page kept at `/tmp/revenger-r61w3-W3EvmMetadataCite/metadata-latest.html`; extraction with `python3` tag-strip + exact-substring search.
- Read-only: no writes to the lane tree beyond this report; no commits, no fixture or saved-record changes, no bytecode or JS executed, no REA calls.

VERDICT: The C09 S019 citation is accurate at section-name, anchor, page-version and "by default" wording level; S019 is tier A for the scope it is cited for and was opened in round 61 (build seat `SrcSolidityMetadataTail`, same 38117-byte page); no evidence contradicts the entry's use. Installs: none.
