FAIL — both injected mutants were detected, but the pristine entry already misquotes one readout field (line 41, `META-INF/MANIFEST.MF` `payload_first16_hex`), so the entry's quoted output is not byte-true at base and its cited §Reproduce artifacts are absent.

Seat: R65MutEntry (mutation-tester, leaf). Contract read: `reports/round-65/claims.md` (C1 entry/fixture pair; kill rule and predicate taken from it). All work in a lane-owned scratch `/tmp/r65mutentry-arqnclnx`; the lane tree was read-only for this seat and is byte-unchanged (hashes at the end). No tool installs or upgrades were needed or performed.

## Baseline (pristine) — detector must pass before any mutant counts

```
$ python3 -B <scratch>/fixtures/apk-r65/readout.py
exit 0; 15 stdout lines; stdout sha256 = 507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247
scratch fixture.apk: 947 bytes, sha256 05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e
```
Matches the entry's `recheck:` claim (`corpus/knowledge/round-65-apk-axml-byte-evidence.md:160`) and `S041` fixture digest. The readout prints `"path": "corpus/fixtures/apk-r65/fixture.apk"` from the `/tmp` copy too (readout.py:45-46, hard-coded repo-relative path), so stdout is tree-independent as claimed.

Detector B baseline (entry embedded JSON vs readout stdout, see method below): **14/15 match — one pre-existing mismatch**, not caused by any mutation (reported under "Baseline defect").

## Method

- **Detector A (fixture bytes).** Copy `corpus/fixtures/apk-r65/` to scratch, flip exactly one byte in `fixture.apk`, run `readout.py`; compare full stdout (and exit code) against the pristine run.
- **Detector B (entry values).** For every `$ python3 -B corpus/fixtures/apk-r65/readout.py --fact <X>` line in the entry, `json.loads` the following JSON line, run `--fact <X>` against the *pristine* scratch fixture, and compare parsed objects for equality. 15 blocks extracted (command lines 22, 29, 36, 38, 40, 49, 58, 67, 74, 81, 88, 95, 97, 106, 115; each JSON object is the line immediately after its command — e.g. MANIFEST.MF JSON at line 41, `axml_start_element` JSON at line 82).
- Every mutant is applied to a scratch copy only; restoration is byte-level copy of the saved pristine bytes, then the pristine detector is re-run.

## Mutant (a) — one AXML string-pool byte: DETECTED (changes, exit stays 0)

Mutant: `fixture.apk` byte at **file offset 211** — inside the stored `AndroidManifest.xml` member payload (payload range `[49, 465)`, `local_header_offset 0`, `compressed_size 416`) — `0x72` `'r'` → `0x52` `'R'`, the 13th character of string-pool entry 4 (`com.example.r65`; pool chunk at AXML offset 8, `stringsStart 64`, string rel offset 76 → AXML 162).

```
before: fixture.apk 947 bytes sha256 05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e
after : fixture.apk 947 bytes sha256 60a413238cdfe6ceac9794332d590739d69fed250cddbd35854c85447aaeb529

$ python3 -B <scratch>/fixtures/apk-r65/readout.py
exit 0   (stderr empty)   15 stdout lines
stdout sha256 d790d49ff76f13d21973fce3c4c4d3dd25000d6a7e71d0eab10b3f95833adeee  (base 507d79f8…)
```

Four stdout lines change (unified diff, `-`=pristine, `+`=mutant; readout.py:116,118,159 derive these):

```
archive.sha256                     05d2280f…d03e  ->  60a41323…b529
member[AndroidManifest.xml]
  .crc32_matches                   true           ->  false
  .crc32_recomputed                962d075f       ->  fa665fec
  .sha256                          73d1e0f2…fae4  ->  65506f89…22c8
axml_string_pool.strings[4]        "com.example.r65" -> "com.example.R65"
axml_start_element.attributes[0]
  .raw_value                       "com.example.r65" -> "com.example.R65"
```

Calibration nuance: the mutant **survives an exit-code-only detector** (exit 0). It is killed only by comparing field values (the entry's `recheck:` stdout SHA-256 changes, so that command does catch it; a single-fact `--fact spec_derived_struct_widths` would not — that line is unchanged).

## Mutant (a2) — one AXML string-pool header byte: DETECTED (hard failure)

Mutant: `fixture.apk` byte **65** = AXML offset 16 = string-pool `stringCount` low byte, `9` → `10`.

```
after : fixture.apk sha256 c722159cb543f932e028ebecc0dd0a52b34f7b5582cda96bbd2a77a004e41aea

$ python3 -B <scratch>/fixtures/apk-r65/readout.py
exit 1   7 stdout lines   stdout sha256 67ca1fbd12f4b2f62951cae3cbe0a36b8840e1d20e6817737440a6b63a567ed6
stderr tail:
    u16len = axml[base]
             ~~~~^^^^^^
IndexError: index out of range
```
Fails at `corpus/fixtures/apk-r65/readout.py:159`. Killed by exit status.

## Mutant (b) — one number in the entry's embedded JSON: DETECTED

Mutant: entry line 82 (command at line 81), `axml_start_element` object: `"attributeCount": 3` → `"attributeCount": 4`. Exactly one occurrence of the replaced literal in the file (`grep -c '"attributeCount": 3'` = 1), so the edit is the assigned single number.

```
pristine entry : sha256 e173e6436e9b8cce2ddd9f318b914fde6fd9bdfaf18335f5a873ac60fa3cdfb7
mutant entry   : sha256 d757081a9f40ce16f3533919431dc735b6f2c21d0bd6b35e58477af7cb77c27c

Detector B on mutant entry: 13/15 match; mismatches:
  member[META-INF/MANIFEST.MF] payload_first16_hex : entry='4d616e6966…' readout='4d616e6966…'   (pre-existing, see below)
  axml_start_element             attributeCount    : entry=4          readout=3                  (caused by this mutant)
```
The mutated fact's own baseline was a match (`axml_start_element` MATCH at pristine), so this kill is conclusive; the MANIFEST mismatch is a separate baseline defect and is **not** attributed to the mutation.

## Baseline defect (finding, not a mutant) — entry line 41 is false at pristine bytes

`corpus/knowledge/round-65-apk-axml-byte-evidence.md:41`, item 3's `member[META-INF/MANIFEST.MF]` record:

```
entry:   "payload_first16_hex": "4d616e696673742d56657273696f6e"
readout: "payload_first16_hex": "4d616e69666573742d56657273696f6e"   (actual stdout, pristine fixture)
```
Ground truth bytes: `4d616e69666573742d56657273696f6e` = `b"Manifest-Version"`, exactly 16 bytes; the entry's value = `4d616e696673742d56657273696f6e` = `b"Manifst-Version"`, **15 bytes** — internally inconsistent with its own field name and one `65` (`e`) short. Every other field in the same JSON object (offsets 618/668, sizes 69, crc `e948d738`, sha256 `2e5da249…0a49`) matches stdout, and the other 14 facts match exactly, so the defect is this one transcribed value.

Why the pair's own gate misses it: the entry's `recheck:` (`:160`) authenticates the *readout's* stdout hash (`507d79…`), which is unaffected by a bad transcription of a value into prose. The stdout hash authenticates bytes, not quoted values; only an entry-vs-stdout value comparison (Detector B) catches this. `truth.json` does not carry `payload_first16_hex` (`grep` → no match), so the oracle cannot arbitrate it either; the readout is the sole deriving command, and it contradicts the entry.

Consequence for C1: `Q11` ("every count, offset, identifier and digest carries its deriving command and output") is not met for this field as written — the cited command's output is different from the quoted value. This is a one-field transcription fix in the entry, not a fixture or readout defect; the fixture bytes, oracle and readout all reproduce exactly.

## Secondary finding — two cited §Reproduce artifacts do not exist

`corpus/knowledge/round-65-apk-axml-byte-evidence.md:15` states: *"the script is the `### Code` block of that section … and the same lines appear in the full 15-line stdout reproduced there."*

```
$ grep -c '^### ' corpus/knowledge/round-65-apk-axml-byte-evidence.md
0
$ sed -n '154,162p' …   # §Reproduce
## Reproduce
From the lane root, with the round-65 corpus tree:
```sh
python3 -B corpus/fixtures/apk-r65/readout.py
```
Exit 0; 15 stdout lines; their SHA-256 is `507d79f8…`; …
```
There is no `### Code` block anywhere in the entry and no 15-line stdout block in §Reproduce (the 15 JSON lines exist only as per-item quotes in §Observation). Two pointers in the entry's own evidence map resolve to nothing — a `Q02`/`Q11` pointer defect independent of the mutant tests.

## Verdict table

| mutant | expected detector | actual | verdict |
|---|---|---|---|
| (a) byte 211 `r`→`R` in AXML string pool | readout stdout change or non-zero exit | exit 0; 4 lines change (sha256, CRC flag, 2 string values) | killed (value-level); survives exit-code-only |
| (a2) byte 65 `stringCount` 9→10 | readout fails | exit 1, `IndexError` at readout.py:159 | killed (hard) |
| (b) entry `attributeCount` 3→4 | entry JSON ≠ readout stdout | 13/15 match, exact-field diff attributed | killed |
| baseline MANIFEST `payload_first16_hex` | entry JSON == readout stdout | 15-byte value vs 16-byte stdout | **pre-existing defect** |

No mutant survived a value-level detector. The pair's weakness is not fixture sensitivity — it is that the entry's admitted recheck (stdout hash) cannot detect transcription drift, and one such drift exists at base.

## Restoration evidence

```
# mutant (a)
[restore a] fixture.apk 947 bytes sha256 05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  (== base)
[restore a] readout exit 0; 15 lines; stdout sha256 507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247  (== base)

# mutant (a2)
[restore a2] fixture.apk sha256 05d2280f…d03e (== base); readout exit 0; stdout sha256 507d79f8…d247

# mutant (b)
[restore b] Detector B 14/15, only the pre-existing MANIFEST mismatch remains
[restore b] scratch entry copy identical to committed: True

# lane bytes never written by this seat (re-hashed after all probes)
corpus/fixtures/apk-r65/fixture.apk 05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e
corpus/fixtures/apk-r65/readout.py  92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976
corpus/fixtures/apk-r65/truth.json  27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173
```
All mutations and restores were confined to `/tmp/r65mutentry-arqnclnx`; this report is the only file written under the lane.

## Bounds honored

No git/jj mutation, no edit to `corpus/`, `reports/`, `LOG.md`, `SCORECARD.md`, `SHONEN.md`, or any sibling artifact. Only read-only probes plus this report. Nothing judged, integrated or shipped; `readout.py`, `truth.json` and the entry's admitted status are untouched — the cited defects are findings for the reviewers/L1, not edits by this seat.
