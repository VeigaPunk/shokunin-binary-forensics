# SrcSolidityMetadataTail — C09 source opening (read-only)

Seat: `CloseChousa26.SrcSolidityMetadataTail-10` · base `e0a4b0c4348ef1fade46539f520e94fa140c4d8a` · 2026-10-21

## Fetch

- URL opened: `https://docs.soliditylang.org/en/latest/metadata.html`
- HTTP: `200` — `curl -sS -D /tmp/hdr.txt -o /tmp/sol-metadata.html -w '%{http_code} %{url_effective} %{size_download}\n'` printed `200 https://docs.soliditylang.org/en/latest/metadata.html 38117`; headers `date: Wed, 21 Oct 2026 15:42:49 GMT`, `last-modified: Tue, 29 Sep 2026 13:01:07 GMT`.
- Page identity: `<title>Contract Metadata — Solidity 0.8.38-develop documentation</title>`; `<meta name="readthedocs-version-slug" content="latest" />`; `<meta name="readthedocs-http-status" content="200" />`. No commit id is exposed on the page.
- Section anchors present in HTML: `id="contract-metadata"`, `id="encoding-of-the-metadata-hash-in-the-bytecode"`.
- Access date: 2026-10-21. Revision recorded: `latest` (0.8.38-develop docs bundle), last-modified 2026-09-29.

## Quotes (verbatim; source line wraps normalized to single spaces)

1. 19 words — “The compiler appends by default the IPFS hash of the metadata file to the end of the runtime bytecode” — §Contract Metadata (`#contract-metadata`), first paragraph.
2. 15 words — “The last two bytes in the bytecode indicate the length of the CBOR encoded information.” — §Encoding of the Metadata Hash in the Bytecode (`#encoding-of-the-metadata-hash-in-the-bytecode`), second paragraph.
3. 15 words — “Do not rely on it starting with 0xa264 or 0xa2 0x64 'i' 'p' 'f' 's'.” — same section, closing Note.

## Bearing on C09 “discovery completeness unknown”

Observed: solc documents that metadata is CBOR-encoded and appended **by default** to the end of *runtime* bytecode (explicitly “not necessarily the creation bytecode”), and that its length is readable from the final two bytes; the page also names the opt-outs `--no-cbor-metadata` and `settings.metadata.appendCBOR=false`. Inference (not stated by this page): for a linear byte scan for `0x63`/`0x5b`, the last `2 + 2 + N` bytes of a default solc runtime are metadata rather than code, so hash/version bytes can be read as PUSH4/JUMPDEST; and because presence is default-on but optional, a scanner cannot assume a fixed or always-present tail. Value to the entry: the page supplies a computable delimiter (read last two bytes, decode that many bytes with a CBOR parser) instead of a heuristic prefix, which is exactly the bound a “completeness unknown” statement needs; the page’s own warning against the `0xa264` prefix heuristic supports that framing.

Scope limit observed: the lane’s EVM fixtures carry no such tail — `corpus/fixtures/evm-r19/fixture.hex` is `0x60003560e01c63deadbeef14601057005b00` (18 decoded bytes, `truth.json` `"decoded_size": 18`), and `fixture.raw` sizes for r21–r26 are 18/34/7/35/19/19 bytes (authored inert bytecode). This row grounds the general caveat only; it must never be cited as fixture evidence.

## Proposed SOURCES.md row (11 columns; id TBD — S016 if no earlier round-61 row lands)

| S0NN | Contract Metadata — Solidity documentation — https://docs.soliditylang.org/en/latest/metadata.html | docs | A | placement, encoding and delimiting of the CBOR metadata tail that solc appends to runtime bytecode | “Encoding of the Metadata Hash in the Bytecode” (`#encoding-of-the-metadata-hash-in-the-bytecode`), 0.8.38-develop docs, HTTP 200 2026-10-21, last-modified 2026-09-29 | solc appends a CBOR-encoded metadata blob by default at the end of runtime bytecode, delimited by the length in the final two bytes, so a linear byte scan meets documented non-code bytes there unless it strips that tail | queued | 2026-10-21 | on-release | — (intended: the C09 knowledge entry) |

## What the source does NOT state

- No EVM opcode semantics: `grep -c 'PUSH\|JUMPDEST\|0x5b\|opcode' /tmp/sol.txt` printed `0` (exit 1). Nothing about PUSH4=`0x63`, selector extraction, or JUMPDEST validity.
- Nothing about executability of the tail: it says “appended”, never that the blob is unreachable or non-executable.
- No claim that the tail is the only non-code region (embedded constants, other compilers, constructor/immutable data are unmentioned).
- No byte order for the 2-byte length: `grep -c 'endian' /tmp/sol.txt` printed `0` (exit 1); also silent on whether those 2 length bytes are inside or outside the blob.
- No presence guarantee: “by default”, with named opt-outs, so absence is possible and no fixed tail length exists.
- No statement that hash bytes can spell `0x63` or create false selector candidates — that is inference from an external opcode table.
- No description of this lane’s fixtures or of evmole/@0.9.3-style interface extraction.

## Separation

Observed: HTTP 200, page version, anchors, the three quotes, fixture byte sizes. Inference: naive-scan false positives and the strip-before-scan rule. Unknown: CBOR length byte order and exact blob boundary convention (needs RFC 8949 or solc source as a second, still-unopened row).

## Search log line for `## Search log`

- 2026-10-21, C09 non-code bytes in runtime bytecode. Query: official documentation of the solc metadata appended to bytecode and its encoding. Where: docs.soliditylang.org metadata page (version selector assets absent from the served HTML; `/en/v0.8.37..35/metadata.html` returned 200 with the same shape). Identified 1, screened 1, included 1 (queued), excluded 0. Stop: the authoritative page covers placement, encoding and delimiting; opcode semantics and byte order are out of its scope and stay leads. Opener: L2 `SrcSolidityMetadataTail`.

## Leads (unopened)

- RFC 8949 (CBOR) — needed only if the entry must derive the length byte order rather than record it.
- solc source `libsolutil/` metadata encoding — would fix the boundary convention if the docs wording proves insufficient.

VERDICT: Solidity “Contract Metadata” opened HTTP 200 (0.8.38-develop, last-modified 2026-09-29); it documents a default CBOR tail at the end of runtime bytecode delimited by the final two bytes, supports the C09 non-code caveat at tier A, and states nothing about opcodes, endianness, executability or other data regions.
