# SrcSolidityAbiSelector — round 61 C1 (C09) source opening, read-only
Question: how a 4-byte selector is derived from a function signature. No lane edit; only this file written.

## 1. Source
- URL `https://docs.soliditylang.org/en/latest/abi-spec.html` — HTTP/2 200, no redirect (`FINAL_URL` identical),
  112838 B, `text/html; charset=utf-8`, `date: Wed, 21 Oct 2026 15:42:49 GMT`,
  `last-modified: Tue, 29 Sep 2026 13:01:06 GMT`, `x-rtd-version: latest`. Access date 2026-10-21.
- Version on page: `<title>Contract ABI Specification — Solidity 0.8.38-develop documentation</title>`; footer
  `© Copyright 2016-2025, The Solidity Authors`; Remix links pin `version=0.8.38`. No commit id: the edit target is
  `github.com/ethereum/solidity/blob/latest/docs/abi-spec.rst`, a mutable branch → row recheck `on-release`.
- Bytes sha256 `4bb56ed3f2aaed824d3eb3c6df758284cbd9c714f063bdc23bfb45cbb0943926`, identical to the independent
  fetch in `build/ScribeSourcesRowsEvm.md`: two seats read the same bytes.

## 2. Anchor
`#function-selector` (h2 "Function Selector"; alias `<span id="abi-function-selector">`). Companion
`#function-selector-and-argument-encoding` gives `function_selector(f) enc((a_1, ..., a_n))`: the selector is
call-data bytes 0–3, arguments start at byte 4.

## 3. Quotes (verbatim; each verified as a substring of the fetched page text)
1. 18 w, section "Function Selector", first `<p>`: "The first four bytes of the call data for a function call specifies the function to be called."
2. 20 w, same `<p>`: "It is the first (left, high-order in big-endian) four bytes of the Keccak-256 hash of the signature of the function."
3. 12 w, `admonition note` in the same section: "The return type of a function is not part of this signature."
Same `<p>`, not counted: signature = "the function name with the parenthesised list of parameter types";
types split by a single comma — "no spaces are used"; data-location specifiers excluded. Worked literals
(Examples): `0xcdcd77c0` for `baz(uint32,bool)`; `0xa5643bf2` for `sam(bytes,bool,uint256[])` with "uint is
replaced with its canonical representation uint256".

## 4. Derivation for the entry's Q11
`uv run -q --no-project --with pycryptodome==3.23.0 python -B -c "from Crypto.Hash import keccak; ..."` →
`baz(uint32,bool) -> 0xcdcd77c0`, `sam(bytes,bool,uint256[]) -> 0xa5643bf2`, `transfer(address,uint256) -> 0xa9059cbb`.
Both page literals reproduce. `hashlib.sha3_256(...)[:8]` gives `0xaf54f249` / `0xcf3d9ff5`, so the two page
vectors pin Keccak-256 over NIST SHA3-256.

## 5. Proposed `corpus/SOURCES.md` row (contract v1, 11 columns)
| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S016 | Contract ABI Specification — Solidity 0.8.38-develop documentation — https://docs.soliditylang.org/en/latest/abi-spec.html | spec | A | derivation of the 4-byte function selector from a canonical Solidity function signature, as this page states it | "Function Selector" (`#function-selector`, alias `#abi-function-selector`); `latest` docs branch, HTTP Last-Modified 2026-09-29 | A selector is the big-endian first four bytes of the Keccak-256 hash of the canonical signature `name(type1,...)` with no spaces and no data-location specifier; the return type is excluded. | queued | 2026-10-21 | on-release | — |

`queued` because no admitted entry cites it yet; flip to `mined` when the C09 entry path is added (log old→new).
Tier A for the stated scope only. Gate line: `S016 https://docs.soliditylang.org/en/latest/abi-spec.html — accessed 2026-10-21, HTTP 200, "Solidity 0.8.38-develop" — § Function Selector: "It is the first (left, high-order in big-endian) four bytes of the Keccak-256 hash of the signature of the function."`

## 6. What the source does NOT state
Counts over the fetched bytes: `JUMPDEST=0 PUSH=0 dispatch=0 sha3=0 SHA3=0 opcode=1 collision=1 Keccak=5`.
- 0 hits for JUMPDEST/PUSH/dispatch: that a `PUSH4` immediate is a selector, and that a comparison branches to a
  JUMPDEST, is inference from fixtures — never stated here. The entry must label it.
- No reverse mapping: nothing recovers a signature from an observed 4-byte value; only the forward rule is given.
- No selector-collision handling: the one `collision` hit is Argument Encoding (dynamic types), not selectors.
- No Keccak-vs-SHA3 distinction (0 hits for SHA3); pin the variant with §4's vectors.
- No statement of which compiler/optimizer emits `PUSH4`, no EVM-version or chain scope, and no guarantee that a
  deployed contract's selector set is statically discoverable.

## 7. Registry collision between seats (L1 action)
Two seats drafted different rows on `S016` (`ScribeSourcesRowsEvm.md` = this page; `ScribeSourcesRowsJs.md` = Node
modules); the registry read 2026-10-21 ends at S015 (15 rows). Reproduced on /tmp copies with
`sources-census.sh validate --today 2026-10-21 --file <copy>`: my row → `file ok`, exit 0; the EVM scribe's shape
(`mined`, `used-by "[C09 entry, TBD by L1]"`) → two `E11 S016 missing used-by`, exit 1; mine + the JS row both as
`S016` → `E03 S016 duplicate id`, exit 1; mine + the EVM row as `S017` → `W04 duplicate url ... across scopes`,
exit 0 (E04 therefore does not stop a second Solidity row — one row per source is an L1 call). Four C04/C09 rows
need four distinct ids at append.

## 8. Installs
- `uv 0.13.0` (already present) with an ephemeral PyPI `pycryptodome==3.23.0` env for the Keccak vectors; nothing
  persisted, no pacman call (host-wide pause respected).
- Written: this report only. No clone, no patch, no touch of `corpus/`, git or jj.
VERDICT: Selector derivation confirmed verbatim from the opened spec page (HTTP 200, "0.8.38-develop", last-modified 2026-09-29); S016 proposed as queued/tier-A/`spec` and passing `sources-census.sh validate`; the bytecode side (PUSH4→JUMPDEST) is provably absent from the source and must stay labeled inference; S016 is contested with the JS seat, and the EVM scribe's placeholder `used-by` fails E11.
