# Fixture source ground truth — checksum-r1

Scope: source-derived inventory only. No REA analysis or target execution was performed. This report cites the checked-in C source and the round records, not REA Evidence IDs; it is not a binary-analysis finding.

## Source facts (OBSERVATION)

Source: `.shokunin/revenger/corpus/fixtures/checksum-r1/checksum.c` (numbered source lines below).

- `rolling_checksum(const unsigned char *bytes, size_t len)` is `static`, returns `uint32_t`, starts state at `0x13579bdfu` (line 6), processes exactly `len` bytes (7), rotates the 32-bit state left by 5 using `(state << 5) | (state >> 27)` (8), then XORs with the byte value plus 17 (9); returns final state (11). The unsigned fixed-width type makes the intended rotation 32-bit.
- `rotate_ascii(char *out, const char *in)` is `static` (14). It processes while input is non-NUL and index is below 127 (16), casts each input byte to `unsigned char` (17), applies ROT13 only to lowercase ASCII `a`–`z` (18), and copies other bytes unchanged. It terminates output at the stopping index (20). This bounds output to at most 127 data bytes plus NUL in the 128-byte destination declared in `main` (25).
- `main(int argc, char **argv)` (23) selects `argv[1]` when `argc > 1`, otherwise literal `"amber"` (24); transforms it (26); prints `r1:`, transformed text, `:`, an eight-digit lowercase hexadecimal checksum (`%08x`), newline (27–28); checksum input is the transformed string bytes up to `strlen` (28); returns 0 (29).
- Includes are `<stdint.h>`, `<stdio.h>`, `<string.h>` (1–3). The two helpers have internal linkage because they are `static` (5,14); `main` is externally named entry point (23).

## Derived behavior (INFERENCE from the source)

- Default invocation's transform is `nzo re`? Correction: lowercase ROT13 of `amber` is `nzore` (per the character-wise formula); output takes the form `r1:nzore:<checksum>`. The checksum should be computed from bytes `nzore`, excluding the terminating NUL. This is a source-level prediction, not an observed run.
- Uppercase letters, punctuation, and non-lowercase bytes are unchanged by the conditional; processing stops at the first NUL or after 127 bytes. The checksum recurrence wraps in `uint32_t` arithmetic.
- The checksum is not computed from original input, but from transformed output, as the call argument at line 28 establishes.

## Constants / exact expressions

Seed `0x13579bdfu`; rotation left 5 (`<< 5`, `>> 27`); per-byte addition `17u`; lowercase ASCII bounds `'a'`, `'z'`; alphabet rotation offset 13 modulo 26; input cap 127; output buffer 128; default `amber`; output prefix `r1:`; format `%08x`.

## Limits and unresolved

No compiler identity/flags/provenance assessment is made here; see the separate provenance lane. The built artifact was not executed or independently inspected. No REA Evidence IDs exist in this source-truth report, so it must not be treated as scoring evidence for REA coverage. Runtime behavior for unusual byte encodings/platforms is not claimed beyond the C source expressions and host compilation semantics.

## Context / scope citations

Round declaration and the stated no-runtime boundary: `.shokunin/revenger/LOG.md`, “Round 1 declaration — coverage”. Fixture calibration rationale: `.shokunin/revenger/corpus/knowledge/seed.md`, “Calibration strategy”. REA’s requirement to distinguish evidence types: `~/.agents/skills/reverse-engineer-anything/SKILL.md`, “Work summary-first”.
