# Round 64 Binwalk cross-oracle

Fixture: `corpus/fixtures/firmware-r63/firmware-r63.bin` (2048 bytes). Oracle: `corpus/fixtures/firmware-r63/truth.json`.

The scans below are read-only; no extraction option was used. The installed binary is `/usr/bin/binwalk`, version 3.1.0.

## Version

Command:

```sh
command -v binwalk; binwalk --version
```

Output:

```text
/usr/bin/binwalk
binwalk 3.1.0
```

## Default scan

Command:

```sh
binwalk /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/firmware-r63.bin
```

Output:

```text
Analyzed 1 file for 85 file signatures (187 magic patterns) in 3.0 milliseconds
```

This default scan printed no signature rows. That is the M33 behavior: Binwalk 3.1.0's zlib signature is marked `short: true`, so its default scan misses these nonzero-offset zlib streams.

## All-offset scan (M33 control)

Command:

```sh
binwalk --search-all /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/firmware-r63.bin
```

Output:

```text
                                                      /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/firmware-r63.bin
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
DECIMAL                            HEXADECIMAL                        DESCRIPTION
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
512                                0x200                              Zlib compressed file, total size: 79 bytes
1024                               0x400                              Zlib compressed file, total size: 90 bytes
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Analyzed 1 file for 85 file signatures (196 magic patterns) in 2.0 milliseconds
```

## Raw `-R` option availability

Command:

```sh
binwalk -R zlib /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/firmware-r63.bin
```

Standard error:

```text
error: unexpected argument '-R' found

  tip: to pass '-R' as a value, use '-- -R'

Usage: binwalk [OPTIONS] [FILE_NAME]

For more information, try '--help'.
```

Exit status: `2`. The installed 3.1.0 CLI does not offer `-R`; `--search-all` was used for the all-offset signature scan instead.

## Oracle comparison and precise wording

`truth.json` has five contiguous regions: zero padding at `[0,512)`, zlib `diagnostic-note` at offset 512 size 79, zero padding at `[591,1024)`, zlib `component-note` at offset 1024 size 90, then zero padding at `[1114,2048)`. Under `--search-all`, Binwalk reports exactly two signatures, both `Zlib compressed file`, at offsets 512 and 1024 with sizes 79 and 90; these match the oracle's two zlib regions, and there are no other signature rows. The member names and decompressed contents are oracle facts, not Binwalk output.

Use this scoped wording: **“Binwalk 3.1.0 with `--search-all` reports the two zlib regions at offsets 512 (79 bytes) and 1024 (90 bytes), and no other signatures; the default scan reports neither, as expected for M33.”**
