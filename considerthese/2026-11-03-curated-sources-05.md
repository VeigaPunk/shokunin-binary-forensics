# Consider these: bytecode listings acquire a runtime dimension

**Status: unassimilated reading after hyaku, subject to João's later manual instruction.** Primary sources checked 2026-11-03 UTC. This is runtime and analysis-method evolution, not evidence that one decompiler is universally best. No Python artifact was loaded, imported or executed.

## Timeline and pinned sources

- **2021 baseline:** CPython's `v3.10.0` resolves to [b494f5935c92951e75597bfe1c8b1f3112fec270](https://github.com/python/cpython/blob/b494f5935c92951e75597bfe1c8b1f3112fec270/Doc/library/dis.rst), committed 4 October 2021. Its `dis` documentation warns that bytecode is implementation-specific; interpreting a listing already required the matching interpreter version.
- **Design transition:** [PEP 659](https://peps.python.org/pep-0659/), created **13 April 2021**, explains adaptive specialization and quickening. That creation date is a proposal date, not deployment evidence. Its motivation is interpreter efficiency, not forensic reconstruction.
- **2022 implementation documentation:** `v3.11.0` resolves to [deaf509e8fc6e0363bd6f26d52ad42f976ec42f2](https://github.com/python/cpython/blob/deaf509e8fc6e0363bd6f26d52ad42f976ec42f2/Doc/library/dis.rst), committed **24 October 2022**. The document introduces inline cache entries hidden from ordinary listings.
- **Current continuity:** [3.15 documentation snapshot](https://github.com/python/cpython/blob/37f4276351d86dede54c668c6ca29b8d3eef2058/Doc/library/dis.rst), committed **3 November 2026, 17:47:33 UTC**, distinguishes adaptive bytecode, cache visibility and later changes to jump interpretation and displayed labels. This is a verified source commit, not proof of the lane's installed runtime.

## What changed, and what remains useful

A listing now needs its representation choice recorded as well as its interpreter identity. Hidden cache entries and specialized instructions can explain differences without implying changed source behavior. The old, simpler listing remains useful for an artifact actually produced for that older runtime, and for comparing high-level instruction intent. It is not a safe decoding contract for arbitrary newer bytes. Neither a clean listing nor an attractive reconstructed function proves semantic equivalence.

## Future comparison question

After hyaku and manual authorization, could two reports about an already authorized Python artifact disagree solely because one retained offsets and caches while another used default labels? Propose a paper worksheet recording producer version, reader version, static versus runtime origin, display options and unknown history. Separate differences explained by presentation from differences that would require additional evidence. Do not execute a sample to fill an empty cell.

## Novelty and rights

Prior Python extraction/decompilation and PEP 552 material does not cover this representation transition; no PEP 659 or `dis` source match appeared in the reviewed inventory. PEP 659 declares public-domain/CC0 terms. The pinned [Python LICENSE](https://github.com/python/cpython/blob/deaf509e8fc6e0363bd6f26d52ad42f976ec42f2/LICENSE) covers documentation under PSF License 2, with separate dual terms for examples. Only original commentary is reproduced; no code, captures, corpus changes or training input.
