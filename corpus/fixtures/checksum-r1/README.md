# checksum-r1 fixture provenance

- Source: `checksum.c` (SHA-256 `aa75b4aca3ff535c8050c28db21433727f686102d62c526e294458537084b517`).
- Build command: `cc -std=c11 -O0 -g0 -fno-inline -o .shokunin/revenger/corpus/fixtures/checksum-r1/checksum .shokunin/revenger/corpus/fixtures/checksum-r1/checksum.c`.
- Compiler: `cc (GCC) 16.2.1 20260810` (`cc --version | head -1`).
- Binary SHA-256: `f5ba069764ac66d5baa20224b0698a713823f45947a3364b67cfcb3f584897d0` (`sha256sum .shokunin/revenger/corpus/fixtures/checksum-r1/checksum`).
- `file`: ELF 64-bit LSB PIE executable, x86-64, dynamically linked, not stripped; size 16160 bytes. No target execution was used to establish behavior.
- Source truth: `rolling_checksum` starts at `0x13579bdf`, rotates state left 5 then XORs each input byte plus 17; `rotate_ascii` applies ROT13 only to lowercase ASCII, copying other bytes, stopping at NUL or 127 bytes; `main` uses argument 1 or `amber`, transforms, hashes transformed bytes and prints `r1:<transformed>:<8-digit lowercase hex>` (all source-derived, not REA recovered).
- Caveat: source has a 128-byte output buffer; input longer than 127 is truncated; no claim is made about non-ASCII signed-char display or locale-dependent execution. Compilation and static inspection only.
