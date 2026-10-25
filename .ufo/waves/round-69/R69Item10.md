MATCH — all four emitted fields of the live `jar_manifest` readout are byte-identical to the entry's embedded line (lines 122 and 214); the item-10 prose sentence (line 118) states nothing false, but one phrase ("of ASCII") is not a printed output field and one word ("blank-line-separated") describes a terminator, not a separator.

## Command (exact, from `/home/vgpnk/Projects/shokunin/revenger-shokunin`)

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact jar_manifest
```

- exit code: **0**
- stderr: **0 bytes** (`/tmp/revenger-r69-err.txt`, `wc -c` → `0`)
- stdout, one line, LF-terminated (`od -c` tail: `... "section_count": 1}\n`)

## Actual output (stdout, verbatim)

```json
{"bytes": 69, "fact": "jar_manifest", "first_line": "Manifest-Version: 1.0", "section_count": 1}
```

Empty-space-exact is preserved here because I compared strings programmatically, not by eye.

## Entry's embedded lines

`corpus/knowledge/round-69-apk-axml-byte-evidence.md`

- **line 121** (the command shown in the item-10 block): `$ python3 -B corpus/fixtures/apk-r65/readout.py --fact jar_manifest`
- **line 122** (the embedded output line, under item 10):
  `{"bytes": 69, "fact": "jar_manifest", "first_line": "Manifest-Version: 1.0", "section_count": 1}`
- **line 214** (second copy, inside the full `## Reproduce` transcript):
  `{"bytes": 69, "fact": "jar_manifest", "first_line": "Manifest-Version: 1.0", "section_count": 1}`

Both copies compared with Python `==` against `actual.rstrip()`:

```
121 equal_to_actual: False   # line 121 is the '$ ...' command, not an output line (expected)
122 equal_to_actual: True
214 equal_to_actual: True
```

## Field-by-field verdict (actual vs embedded, line 122)

| field | actual | embedded | verdict |
|---|---|---|---|
| `fact` | `"jar_manifest"` | `"jar_manifest"` | MATCH |
| `bytes` | `69` | `69` | MATCH |
| `first_line` | `"Manifest-Version: 1.0"` | `"Manifest-Version: 1.0"` | MATCH |
| `section_count` | `1` | `1` | MATCH |

No field differs. No extra fields in either direction. Key order and `", "` spacing also identical (single-line sorted-JSON emit).

## Prose judgement — entry line 118

> 10. The `META-INF/MANIFEST.MF` payload is 69 bytes of ASCII whose first line is `Manifest-Version: 1.0` with one blank-line-separated section:

Clause-by-clause against the output:

1. **"`META-INF/MANIFEST.MF` payload"** — supported: the emitter selects `members["META-INF/MANIFEST.MF"]` (`corpus/fixtures/apk-r65/readout.py:122`) and the same member name is printed by the archive walk as `"fact": "member[META-INF/MANIFEST.MF]"` (entry line 213).
2. **"is 69 bytes"** — supported by `bytes: 69`. Independently confirmed: `zipfile.ZipFile(...).read('META-INF/MANIFEST.MF')` → `len 69`.
3. **"of ASCII"** — **NOT a printed field.** The fact emits no `ascii`/`encoding` key. Nearest support is `first_line=jar.split(b"\r\n")[0].decode("ascii")` (`readout.py:251`), which proves ASCII-ness of the *first line only*, not of the whole 69-byte payload. Independently true for this fixture (`all(b < 128 for b in payload)` → `True`; bytes are `b'Manifest-Version: 1.0\r\nCreated-By: revenger-r65 fixture generator\r\n\r\n'`), so the prose is not false — it is merely asserted one step beyond what the command prints.
4. **"whose first line is `Manifest-Version: 1.0`"** — supported exactly by `first_line`. Note the emitted value has no trailing `\r\n` (split on `b"\r\n"`, index 0), and the prose quotes it without a line terminator, so it is faithful.
5. **"with one blank-line-separated section"** — the *count* `1` is right, but the field's definition is a separator count, not a section count: `section_count=jar.count(b"\r\n\r\n")` (`readout.py:252`). On these bytes (`\r\n\r\n` count → `1`, `\n\n` count → `0`) that single blank line **terminates** the lone main section rather than separating two sections. So the arithmetic coincides (`1` section, `0` further sections) but the prose word "separated" is a semantic description the emitter does not compute; "one blank-line-terminated section" would be the strictly derived reading. Not a factual error at N=1 — worth a word-level nit only.

Nothing in the sentence claims a value the output contradicts. The one non-derived word is "separated"; the one non-printed attribution is "ASCII".

## Independent corroboration of the bytes

```
$ python3 -B - <<'PY' (zipfile read)
len 69
repr b'Manifest-Version: 1.0\r\nCreated-By: revenger-r65 fixture generator\r\n\r\n'
crcrlfcrlf count 1
lflf count 0
ascii ok True
first_line repr b'Manifest-Version: 1.0'
```

## Frozen-artifact fingerprints (context, not re-derived here)

```
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  corpus/fixtures/apk-r65/fixture.apk
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  corpus/fixtures/apk-r65/readout.py
bca74e6d8b5010aee79886521474f072257ee22ec7ccc24e4186666bdc048377  reports/round-69/measure.py
```

`measure.py` sha256 equals the frozen value named in the round-69 contract, so the counter body was not altered between the committed red-before receipt and this re-derivation. Fixture sha256 equals the `archive` fact's `sha256` in the entry's Reproduce transcript (entry line 202), so the readout ran against the authored fixture, not a mutated copy.

## Axis notes

- **Coverage (C1/C05 v4)**: this item is one of Q01–Q15's derivation re-runs; `jar_manifest` re-derives cleanly and its embedded line is exact — no correction of the entry is indicated on this fact.
- **Calibration (C2/Q15)**: the item-10 prose is a further instance of the entry's habit of stating derivable-but-unprinted context ("ASCII", "separated"). It does not rise to a misstatement, but under a strict "every stated field must be printed" criterion it is the kind of phrase that separates a byte-exact entry from an over-reading one.

## Risks / blockers

- None blocking. Residual risk is interpretive only: whether "one blank-line-separated section" should count as a prose defect depends on the C2 criterion's strictness about describing mechanism (separator vs terminator) versus reporting the numeric value (`1`), which the output does support.
- No files outside this report and `/tmp/revenger-r69-*` were written; no git/jj mutation; no package installs were needed or attempted (`python3` stdlib only).
