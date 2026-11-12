# Revenger: a 64-bit load need not use 64-bit addresses

[Core 1.0](https://www.w3.org/TR/2019/REC-wasm-core-1-20191205/), 5 December 2019, already has 64-bit integer values but uses 32-bit dynamic memory-address operands. Its load typing rule returns the requested value type from an i32 address.

The [Wasm 3.0 announcement](https://webassembly.org/news/2025-09-17-wasm-3.0/), 17 September 2025, introduces declaring memories and tables with i64 rather than only i32 address types.

Thus i64.load describes its result type, not by itself the address width. In shipped-module evidence, record the selected memory's declared address type separately from load result and storage widths. Do not infer memory64 from 64-bit arithmetic.

This documents specification evolution, not engine adoption, host word size, successful instantiation, actual allocation or recovered source types. Existing preamble and metadata guidance remains separate.

W3C document-use rules apply to the recommendation; announcement reuse terms remain unverified. Original commentary only; no copied code, module execution, training or assimilation.

Destination: VeigaPunk/shokunin-binary-forensics, main, considerthese/2026-11-11-memory-address-width.md.
