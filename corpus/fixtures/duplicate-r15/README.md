# Round 15 duplicate-name ZIP fixture

Python 3 `zipfile.ZipFile(mode="w", compression=ZIP_DEFLATED, compresslevel=9)` with `ZipInfo(filename, date_time=(2026,10,12,0,0,0))`, `compress_type=ZIP_DEFLATED`, `external_attr=0o100644<<16`; append, in order:

1. `same.txt` → ASCII `first occurrence\n`
2. `same.txt` → ASCII `second occurrence\n`
3. `marker.txt` → ASCII `unique marker\n`

Duplicate paths are intentional; use `ZipInfo` ordinal, not `ZipFile.read(name)`, when scoring bytes. Root and member digests are in `truth.json`. Fixture is never executed.
