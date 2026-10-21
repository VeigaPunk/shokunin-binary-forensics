# ScribeSourcesRowsEvm — round 61 (C1 sources for C09)

Access date for every row below: 2026-10-21. Scratch: /tmp/revenger-r61-ScribeSourcesRowsEvm/ (abi.html, yp.pdf, yp.txt, plain.txt, headers). No lane file was written except this report.

## 1. Sources opened

| # | URL opened | HTTP | Version / revision / date shown | sha256 of fetched bytes |
|---|---|---|---|---|
| A | https://docs.soliditylang.org/en/latest/abi-spec.html | 200 (text/html, 112838 B) | page label "Solidity 0.8.38-develop documentation"; response `last-modified: Tue, 29 Sep 2026 13:01:06 GMT`; `x-rtd-version: latest` | 4bb56ed3f2aaed824d3eb3c6df758284cbd9c714f063bdc23bfb45cbb0943926 |
| B | https://ethereum.github.io/yellowpaper/paper.pdf | 200 (application/pdf, 597589 B) | cover: "SHANGHAI VERSION efc5f9a – 2025-02-04"; `last-modified: Tue, 04 Feb 2025 14:03:41 GMT` | d67c009c5d5a0542c8288aee3c4d470b3e2dbe6e664f72f00011543608477fa9 |

Both were opened by `curl -sSL` from the URLs above; no mirror or search snippet was used. Text was read through the HTML (tags stripped) and `pdftotext` (poppler, already installed at /usr/bin/pdftotext; no install performed).

## 2. Section anchors

- A: section "Function Selector" (HTML `id="function-selector"`, confirmed in abi.html). Also "Function Selector and Argument Encoding" for the call layout.
- B: §9.4.3 "Jump Destination Validity", equations (160)–(161), PDF page 15 (verified by `pdftotext -f 15 -l 15`). Appendix H opcode table, row `0x5b JUMPDEST`, PDF page 36.

## 3. Verbatim quotes (checked by exact substring match against the fetched text)

- Q-A1 (Function Selector, page A): "It is the first (left, high-order in big-endian) four bytes of the Keccak-256 hash of the signature of the function." — 20 words.
- Q-A2 (Function Selector, page A): "The signature is defined as the canonical expression of the basic prototype without data location specifier" — 16 words.
- Q-A3 (Function Selector note, page A): "The return type of a function is not part of this signature." — 12 words.
- Q-B1 (§9.4.3, PDF p.15): "We define this as any position in the code occupied by a JUMPDEST instruction." — 14 words.
- Q-B2 (§9.4.3, PDF p.15): "All such positions must be on valid instruction boundaries, rather than sitting in the data portion of PUSH" — 18 words.
- Q-B3 (Appendix H, row 0x5b, PDF p.36): "Mark a valid destination for jumps." — 7 words.

## 4. Proposed SOURCES.md rows (contract v1, 11 columns; ids are provisional, L1 assigns at append; registry ends at S015)

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S016 (TBD) | Contract ABI Specification, Solidity 0.8.38-develop docs — https://docs.soliditylang.org/en/latest/abi-spec.html | docs | A | the 4-byte function-selector derivation rule as the page states it (label "0.8.38-develop", Last-Modified 2026-09-29) | "Function Selector" (`#function-selector`) | A selector is the first four bytes of Keccak-256 over the canonical signature; return types are excluded. | mined | 2026-10-21 | 90d | [C09 entry, TBD by L1] |
| S017 (TBD) | Ethereum Yellow Paper, Shanghai version efc5f9a (2025-02-04) — https://ethereum.github.io/yellowpaper/paper.pdf | spec | A | the valid-jump-destination set for the Shanghai revision only (PDF p.15 and p.36) | §9.4.3 "Jump Destination Validity", eq. (160)–(161); Appendix H row 0x5b | A JUMPDEST position is a valid destination only on an instruction boundary (not PUSH data) inside the explicit code. Validity is a static set, not reachability. | mined | 2026-10-21 | 180d | [C09 entry, TBD by L1] |

Tier A is claimed only for the stated scope. Neither row supports claims about bytecode layout, dispatcher shape, or whether a function is reachable.

## 5. Lesson `## Gate` lines (draft; URL, access date, located quote ≤25 words)

- S016 — https://docs.soliditylang.org/en/latest/abi-spec.html — accessed 2026-10-21 — "It is the first (left, high-order in big-endian) four bytes of the Keccak-256 hash of the signature of the function." (§ Function Selector)
- S017 — https://ethereum.github.io/yellowpaper/paper.pdf — accessed 2026-10-21 — "We define this as any position in the code occupied by a JUMPDEST instruction." (§9.4.3 Jump Destination Validity, PDF p.15)
- S017 — same URL, accessed 2026-10-21 — "All such positions must be on valid instruction boundaries, rather than sitting in the data portion of PUSH" (§9.4.3, PDF p.15)
- S017 — same URL, accessed 2026-10-21 — "Mark a valid destination for jumps." (Appendix H, row 0x5b, PDF p.36)

## 6. What the sources do NOT state (for the C09 entry's `## Unknown`)

- Neither source says that a `PUSH4` constant in EVM bytecode is a selector. The link from a `PUSH4` value to a function is inference, and the entry must label it that way.
- The ABI page defines how selectors are derived and used in calldata. It does not describe compiled dispatcher code, JUMPI layout, or the pairing of a selector with a JUMPDEST. Those are [INFERENCE] from fixtures, not from A.
- The Yellow Paper defines JUMPDEST *validity* as a set over code (§9.4.3, eq. 160–161). It does not say any listed destination is taken at runtime, and it gives no selector or dispatch rule. Reachability needs execution, which is out of scope here.
- Neither source states how selector collisions are handled. This report did not search the full ABI page for that term; treat it as not checked.
- Solidity page version is "0.8.38-develop", a moving `latest` build. The row's recheck interval reflects that. The Yellow Paper is pinned to efc5f9a, so its recheck is longer.

## 7. Installs / updates

None. pdftotext was already present. pacman was not invoked (host-wide pacman pause in force).

## 8. Files written

- /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-61/build/ScribeSourcesRowsEvm.md (this file)
- scratch only: /tmp/revenger-r61-ScribeSourcesRowsEvm/{abi.html,yp.pdf,yp.txt,plain.txt,hdr-abi.txt,hdr-yp.txt}
- No edits to corpus/, SOURCES.md, knowledge/, MANIFEST.json, .ufo/state, or git/jj state. The registry append and the C09 entry are L1's to make.

VERDICT: Both C09 primary sources opened 2026-10-21 (HTTP 200 each); six verbatim quotes verified; two provisional tier-A rows and four Gate lines drafted; registry append and entry admission left to L1.
