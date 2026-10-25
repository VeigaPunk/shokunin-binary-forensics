PRESENT — the register's quoted payload resolves to line 26 of the fetched source verbatim once backslash escapes are resolved; the absence claim is wrong.

# Row S107 (`revenger` / round4 / `payload-absent`)

- Register row: `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md:167`
- Cited source: `https://raw.githubusercontent.com/morluto/rea/rea-agents-6.7.0/scripts/fixtures/firmware/generate.py`

## Fetch receipt

- Command: `curl -sL --max-redirs 15 -o source.bin -w '%{http_code}' <url>` (succeeded on try 1 of 3)
- HTTP code: `200`
- Byte size: `1873`
- sha256: `32625e04658d57739f2c1102c8fd029778b88c4905740ed124277b16d8048275`
- Saved: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/quarantine/S107/source.bin` (1873 B <= 2 MB, full bytes saved)

## Per-string results

Quoted string (as stored in register, backslash-escaped):
`` `image = b\"REA firmware fixture\\n\".ljust(64, b\"\\xff\") + compressed + b\"\\x00\" * 128` ``

1. **Literal register form** (`image = b\"REA firmware fixture\\n\"...` with literal backslashes): ABSENT — `grep -Fob` exit 1, no match. Also absent from the `html.unescape` + tag-stripped rendering (plain UTF-8 file, no entities, no tags).
2. **Backslash-unescaped form** (`image = b"REA firmware fixture\n".ljust(64, b"\xff") + compressed + b"\x00" * 128`): **PRESENT** — `grep -Fob` byte offset **992**, i.e. `source.bin` line 26:
   ```
   26:image = b"REA firmware fixture\n".ljust(64, b"\xff") + compressed + b"\x00" * 128
   ```
   15-word context: `... compressed = gzip.compress(buffer.getvalue(), mtime=0) | image = b"REA firmware fixture\n".ljust(64, b"\xff") + compressed + b"\x00" * 128 | (root / "firmware.bin").write_bytes(image) ...` (source.bin lines 25–27)
3. **HTML-escaped form** (`&quot;`-style entities): ABSENT — `grep -F` exit 1; the file is raw Python source, no HTML entities present anywhere.

## Analysis

The register stored the quote with JSON/repr-style escaping (`\"`, `\\n`, `\\xff`, `\\x00`). Byte-for-byte that escaped literal does not occur in the source, but resolving the escapes yields the exact code at line 26, byte offset 992 — a verbatim, character-for-character match including spacing. The register's claim "the quote is in none of them" is therefore incorrect for the cited source: the payload the register describes (the firmware image construction line) is present, not absent. No near-miss needed — the unescaped string is an exact hit, not a distortion.

## Verdict

**PRESENT** — string #1 (unescaped semantics): present at byte offset 992, line 26. The register row's absence verdict is falsified for the cited URL.
