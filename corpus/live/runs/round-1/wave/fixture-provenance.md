# Fixture build provenance (round 1)

**Scope and safety.** Inspected the supplied C source and ELF using read-only host tools (`file`, `stat`, `sha256sum` via Python hashlib, `readelf`, `strings`, `nm`). The fixture executable was not run. This report does not establish observed runtime output.

## Observations

- Source: `corpus/fixtures/checksum-r1/checksum.c`. Lines 5–12 implement `rolling_checksum`: initialize `0x13579bdfu`, rotate 32-bit state left five bits, XOR each input byte plus 17. Lines 14–20 implement `rotate_ascii`, rotating lowercase ASCII letters by 13 and copying other bytes, capped at 127. Lines 22–31 default argument to `amber`, transform, then print `r1:%s:%08x\n` with checksum over transformed bytes. (Source line numbers are 1-based.)
- Binary SHA-256, computed over file bytes: `f5ba069764ac66d5baa20224b0698a713823f45947a3364b67cfcb3f584897d0`.
- `file` identifies 64-bit little-endian x86-64 ELF PIE, dynamically linked, not stripped; interpreter `/lib64/ld-linux-x86-64.so.2`; BuildID `b58042814dad2078cdf09b9cf9f111ccab3a5a69`.
- `stat` reports size 16160 bytes, mode 755, mtime `2026-10-12 13:38:31.520085677 -0300`.
- `readelf -h -l -S` reports ELF type DYN (PIE), entry `0x1060`, 31 sections. `.symtab` and `.strtab` exist; `.comment` exists. `nm -n` shows local text symbols `rolling_checksum` at `0x1159`, `rotate_ascii` at `0x11a5`, and global `main` at `0x1245`.
- `strings -a` and `readelf -p .comment` expose `amber`, `r1:%s:%08x`, `checksum.c`, and `GCC: (GNU) 16.2.1 20260810`.

## Provenance assessment

**Inference (strong, not independently verified):** Source semantics and retained symbols/string literals are consistent with a GCC-built, unstripped PIE compiled from this source. GCC 16.2.1 is the compiler version recorded in ELF `.comment`; it is not proof of the exact invocation or source revision. The binary’s symbol names support the source-function mapping, but do not prove byte-for-byte source correspondence.

**Unknown:** No build command, compiler flags, compiler executable hash, build log, or reproducibility comparison is present in the fixture directory (it contains only `checksum.c` and `checksum`). Thus flags such as optimization/debug settings, exact compiler invocation, and whether these exact source bytes produced this binary cannot be confirmed from the available artifacts. No behavioral output was tested because executing the binary was prohibited.

## REA context and limitation

The REA skill says native executable workflows begin with `open_binary`; offline ELF layout inspection is a separate route requiring caller-supplied pwntools (`references/native-and-artifacts.md`, “Offline ELF layout”). The readiness checklist records REA CLI absent and Ghidra/IDA/pwntools absent at mint. This provenance check did not acquire or invoke REA and yields no REA Evidence ID; static host-tool observations above are not REA findings.
