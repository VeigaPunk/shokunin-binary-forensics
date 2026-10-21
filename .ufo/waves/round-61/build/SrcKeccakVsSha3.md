# SrcKeccakVsSha3 — C09 source opening (round 61, read-only)

Question: which hash must an independent EVM `PUSH4` selector derivation use. Lane base observed `e0a4b0c4348ef1fade46539f520e94fa140c4d8a` (`git rev-parse HEAD`); no lane write; no producer/REA call; no execution of bytecode.

## Opened 2026-10-21 (status from `curl -sS -o /dev/null -w 'HTTP %{http_code} %{content_type}' -L`)

| id | URL | HTTP | revision on page | fetched sha256 |
|---|---|---|---|---|
| A | https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf | 200 application/pdf 1459683B | "FIPS PUB 202 … August 2015", DOI 10.6028/NIST.FIPS.202 | `1592607831ff0908cc590632ce371c6c95e94025bb1a0c8ae90a4d0ec1ed025e` |
| B | https://ethereum.github.io/yellowpaper/paper.pdf | 200 application/pdf 597589B | "SHANGHAI VERSION efc5f9a { 2025-02-04"; pdfinfo CreationDate 2025-02-04, 42 pages | `d67c009c5d5a0542c8288aee3c4d470b3e2dbe6e664f72f00011543608477fa9` |
| C | https://docs.soliditylang.org/en/latest/units-and-global-variables.html | 200 text/html 64475B | "Solidity 0.8.38"; `<meta name="readthedocs-version-slug" content="latest">`; no publication date on page | `ea1f3a5dea280d69372077667c2fcbf6f6d3119b2539556739ae0a0efb8a2ef9` |

## Verbatim quotes (<=25 words, location = section + printed page)

1. A, §1 Introduction, printed p.1: "a two-bit suffix is appended to the messages, in order to distinguish the SHA-3 hash functions from the SHA-3 XOFs" (20 words). Same paragraph: "The four SHA-3 hash functions differ slightly from the instances of KECCAK that were proposed for the SHA-3 competition" (20).
2. A, §6 SHA-3 Function Specifications, p.20: "SHA3-256(M) = KECCAK[512] (M || 01, 256);" — §5.2 p.20 defines "KECCAK[c] = SPONGE[KECCAK-p[1600, 24], pad10*1, 1600 – c]"; §B.2 Table 6 p.28 lists Hash pads `M || 0x86`, `M || 0x0680`, `M || 0x06 || 0x00 … || 0x80`.
3. B, §3 Conventions, printed p.3 (pdftotext lines 73-77): "as per version 3 of the winning entry to the SHA-3 contest by Bertoni et al. [2011], rather than the final SHA-3 specification" (23 words); sentence continues "…is denoted KEC (and generally referred to as plain Keccak)".
4. C, "Mathematical and Cryptographic Functions", `keccak256` entry: "compute the Keccak-256 hash of the input". Supporting exact fragments: `msg.sig` = "first four bytes of the calldata (i.e. function identifier)"; `abi.encodeWithSignature` = "bytes4(keccak256(bytes(signature)))"; note "There used to be an alias for keccak256 called sha3, which was removed in version 0.5.0."

## What the opened sources establish (spec-level, no execution)

- SHA3-256 is KECCAK[512] applied to `M || 01`; the appended suffix is the stated difference from the competition KECCAK instances. Suffix-free KECCAK[512](M,256) is therefore a different function.
- Ethereum's KEC is that pre-final-spec function: "version 3 of the winning entry … rather than the final SHA-3 specification" (B).
- Solidity's own builtin is "Keccak-256", and a four-byte selector is `bytes4(keccak256(bytes(signature)))` (C).
- Conclusion for the scope: an independent selector derivation MUST hash the signature text with suffix-free Keccak-256 (pad10*1 beginning `0x01` in the final block byte), not SHA3-256 (suffix `01`, pad byte `0x06`/`0x86`).

## Local derivation (independent library, not a source; run for this report)

`/tmp/r61-hashvenv/bin/python` (pycryptodome 4.1.0) vs `hashlib.sha3_256`, output verbatim:
```
b'' keccak256= c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470 sha3_256= a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a
b'transfer(address,uint256)' keccak256= a9059cbb2ab09eb219583f4a59a5d0623ade346d962bcd4e46b11da047c9049b ... sel_keccak= a9059cbb sel_sha3= 4b40e901
b'balanceOf(address)' keccak256= 70a08231b98ef4ca268c9cc3f6b4590e4bfec28280db06bb5d45e689f2a360be ... sel_keccak= 70a08231 sel_sha3= 1d7976f3
```
Consequence: a selector pipeline built on `hashlib.sha3_256` (or any FIPS-202 SHA3-256) yields `4b40e901` for `transfer(address,uint256)`; the Keccak-256 selector is `a9059cbb`. A digest mismatch here is a falsifier of the pipeline, not of the source.

## Fixture scope note (read-only)

`corpus/fixtures/evm-r19/truth.json`: `"selector_push4": "deadbeef"`, note "no ABI signature claim or execution"; `evm-r23/truth.json`: `"push4_immediate": "c0ffee00"`, "Inert negative fixture". No lane fixture carries a signature→selector pair, so a C09 entry must label any real-signature match as inference and keep the derivation above as a reference vector, never as fixture ground truth.

## Proposed SOURCES.md rows (11 columns; next free ids after S015)

`| S016 | NIST FIPS PUB 202, SHA-3 Standard — https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf | spec | A | only what FIPS 202 specifies: SHA-3 suffix, pad10*1 and the SHA3-256 construction | §1 Introduction (suffix paragraph, p.1), §5.2 (p.20), §6 (p.20), §B.2 + Table 6 (p.27-28); FIPS PUB 202 (August 2015), DOI 10.6028/NIST.FIPS.202 | SHA3-256(M) is KECCAK[512] of M||01; the two-bit suffix is the stated difference from competition KECCAK, so SHA3-256 is not suffix-free KECCAK-256. | queued | 2026-10-21 | on-release | — (pending C09 entry) |`

`| S017 | Ethereum Yellow Paper (Shanghai version) — https://ethereum.github.io/yellowpaper/paper.pdf | spec | A | what function Ethereum's KEC denotes | §3 Conventions, printed p.3; SHANGHAI VERSION efc5f9a, 2025-02-04 | KEC is "version 3 of the winning entry to the SHA-3 contest … rather than the final SHA-3 specification": Ethereum hashes are pre-final-spec Keccak-256, not SHA3-256. | queued | 2026-10-21 | on-release | — (pending C09 entry) |`

`| S018 | Solidity documentation — Units and Globally Available Variables — https://docs.soliditylang.org/en/latest/units-and-global-variables.html | docs | A | the `keccak256` builtin's identity and the four-byte selector derivation as stated in the docs | "Mathematical and Cryptographic Functions" (`keccak256`), "Block and Transaction Properties" (`msg.sig`), "ABI Encoding and Decoding Functions" (`abi.encodeWithSignature`); Solidity 0.8.38, readthedocs slug `latest` | `keccak256` computes Keccak-256, and a selector is `bytes4(keccak256(bytes(signature)))`; the `sha3` alias was removed in 0.5.0. | queued | 2026-10-21 | on-release | — (pending C09 entry) |`

Composed scope: "which hash a selector derivation must use" needs S016+S017 together (one states the SHA-3 construction, the other states Ethereum's choice); S018 supplies the selector formula. A lone row is not tier A for the composed claim (Q01).

## What the sources do NOT state (checked by command on the fetched text)

- FIPS 202: `grep -c -i ethereum` = 0, `grep -c -i keccak-256` = 0, `grep -c '0x01'` = 0. It never names Ethereum, never defines a suffix-free Keccak-256 invocation, and Table 6 carries no pre-standard pad row.
- Yellow Paper: no test vector, no pad byte, no selector/ABI algorithm; its KEC definition defers to Bertoni et al. [2011], which this report did not open.
- Solidity docs: `grep -o -i fips` = 0, `sha3` appears once (the removed-alias note); it never states that its Keccak-256 bytes differ from SHA3-256.

## Remaining unknowns

- The 2011 Keccak submission's own text (pad `0x01`) was not opened; that byte follows here by removing the suffix from FIPS 202 §5.2+§6, not from an opened copy of the submission.
- The Yellow Paper serves the Shanghai revision; KEC is unchanged across forks but post-Shanghai revisions were not opened.
- Solidity docs are the mutable `latest` branch; no immutable commit id or dated revision is published (`/en/v0.8.38/…` returned HTTP 404 on 2026-10-21).

VERDICT: Opened sources establish, with spec-level evidence, that an independent selector derivation must hash with suffix-free Keccak-256 (Ethereum KEC, pre-final-spec) and not FIPS 202 SHA3-256; the composed claim needs S016+S017, the selector formula is S018, and the 2011 Keccak submission remains unopened.
Installs: `uv venv /tmp/r61-hashvenv` + `uv pip install pycryptodome` 4.1.0 (PyPI via uv; reason: independent Keccak-256 implementation for the verification derivation). No pacman transaction.
