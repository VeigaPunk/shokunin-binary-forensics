source: S010 — https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-3/ — anchors `3.8 Surrogates` (D71, D73, D75), `3.9 Unicode Encoding Forms` (D76, D84, D85), `3.9.2 UTF-16` (D91, Table 3-5), and clause C10; page meta-revision b734c94a21cc49b89c2e1823d65129189a40bf28 (version index marks 18.0.0 a preliminary draft)
source: S009 — https://learn.microsoft.com/en-us/windows/win32/debug/pe-format — anchor `Resource Directory String` (word-aligned Unicode, u16 length prefix); page ms.date 2026-09-10, git_commit_id 55e845e9f3a6a3261f59a2f460f61edc25ffcdd5
source: S011 — https://docs.python.org/3/library/codecs.html — anchor `Error Handlers`, `surrogatepass` row and strict default; Python 3.15.0 documentation
source: S013 — `corpus/live/runs/round-59/inspection.stdout.json` — saved `inspect_pe_resources` record, Evidence `ev_8ab30e10bf3d0e73c44c831c9cbb1839d1117db21379e163085ab9d8fec0f8db`; `corpus/live/runs/round-59/LEDGER.md:3`
verified-at: 2026-10-19
recheck: `python3 -c "b=open('corpus/fixtures/pe-r59/fixture.exe','rb').read(); print(b[741], b[738:748].hex()); bytes.fromhex('41003d0000de42002100').decode('utf-16-le')"` — prints `0 41003d0000de42002100` then raises UnicodeDecodeError
coverage-map: C11

# Unpaired surrogates in PE resource names — ill-formed per Unicode, preserved by one saved parser run

Fixture `corpus/fixtures/pe-r59/fixture.exe` (SHA-256
`2d294161e9eebd965919aad91065e5335e693199a17d95533f6c6c8fc751e6a0` by
`sha256sum corpus/fixtures/pe-r59/fixture.exe`, 1536
bytes) differs from the valid-name fixture pe-r55 at exactly file offset 741
(`0xd8` → `0x00`). Byte diff (L1 re-run 2026-10-19):
`python3 -c "a=open('corpus/fixtures/pe-r55/fixture.exe','rb').read();b=open('corpus/fixtures/pe-r59/fixture.exe','rb').read();print(len(a),len(b),[(i,hex(a[i]),hex(b[i])) for i in range(len(a)) if a[i]!=b[i]])"`
→ `1536 1536 [(741, '0xd8', '0x0')]`. Its group-name record at offset 736
then reads length 5 and code units `41003d0000de42002100` = `<0041 003D DE00
0042 0021>` (pe-r55: `<0041 D83D DE00 0042 0021>`). Reproduce:
`python3 -c "import struct; b=open('corpus/fixtures/pe-r59/fixture.exe','rb').read(); print(struct.unpack_from('<H',b,736)[0], ['%04X'%u for u in struct.unpack_from('<5H',b,738)])"`
→ `5 ['0041', '003D', 'DE00', '0042', '0021']`.

## Observation

1. **The mutated sequence is ill-formed UTF-16 by definition.** Unicode 18.0.0
   D91 assigns scalar values ≥ U+10000 to a surrogate *pair* (high then low,
   Table 3-5) and states isolated UTF-16 code units in `D800..DFFF` are
   ill-formed. `DE00` is a low-surrogate code point (D73: U+DC00–U+DFFF)
   appearing here after `003D` (`=`), a BMP unit — no high surrogate precedes it.
   The 5-unit sequence therefore contains an ill-formed subsequence, so the
   sequence as a whole is ill-formed (D84/D85). `😀` at U+1F600 encodes as
   the pair `D83D DE00`; the mutation destroys the high half.
2. **Strict decode fails; surrogatepass preserves.** Per the Python 3.15.0
   `codecs` docs (S011), the strict default treats a surrogate code point as
   an error, while `surrogatepass` allows decoding `U+D800`–`U+DFFF` as
   normal code points. Manual reproduction on the local interpreter, Python
   3.14.7 (`python3 --version`), so the observed behavior is scoped to 3.14.7;
   the documented semantics are cited from the 3.15.0 docs:

   ```text
   >>> bytes.fromhex('41003d0000de42002100').decode('utf-16-le')
   UnicodeDecodeError: 'utf-16-le' codec can't decode bytes in position 4-5: illegal encoding
   >>> bytes.fromhex('41003d0000de42002100').decode('utf-16-le', 'surrogatepass')
   'A=\ude00B!'
   ```

3. **A pre-registered refusal prediction was falsified (r59).** The lane's
   r59 claim predicted an invalid-format refusal with no successful Evidence
   ID (`corpus/live/runs/round-59/LEDGER.md:3`). The saved record instead
   shows `rea-agents@6.4.0 inspect-pe-resources` (provider `rea-pe-resources`
   v1) exited 0 with empty stderr and produced successful Evidence
   `ev_8ab30e10bf3d0e73c44c831c9cbb1839d1117db21379e163085ab9d8fec0f8db`,
   reporting name kind `name` with JSON `"name": "A=\ude00B!"` — an
   unpaired surrogate inside the reported string — and a complete inventory
   (`coverage.status=complete`, 8 examined entries, 3 resources).
   Reproduce from the saved file only, no producer call:

   ```text
   python3 -c "import json; d=json.load(open('corpus/live/runs/round-59/inspection.stdout.json')); r=d['normalized_result']; n=r['resources'][2]['name']; print(repr(n['name']), n['utf16le_hex'], r['coverage'], d['evidence_id'])"
   'A=\ude00B!' 41003d0000de42002100 {'status': 'complete', 'examined_entries': 8, 'resources': 3} ev_8ab30e10bf3d0e73c44c831c9cbb1839d1117db21379e163085ab9d8fec0f8db
   ```

4. **C10 scoped.** Unicode C10 requires a process *interpreting* an
   ill-formed code unit sequence to treat it as an error; the same chapter
   notes processes may operate on code-unit sequences that do not purport to
   be in an encoding form. The saved record's behavior — carrying the lone
   surrogate through into output — is the observed fact; whether it violates
   C10 depends on whether the parser "interprets" the name, which the record
   alone does not settle.

## Inference

- On this one saved run, `inspect_pe_resources` decoded the name field in a
  `surrogatepass`-like manner (surrogates preserved, not refused or
  replaced) and surfaced the result verbatim in JSON. This is scoped to that
  tool version, operation, and fixture family (Q10).
- The falsified prediction is retained evidence: strict spec-derived ground
  truth (ill-formed per D84/D91) and the tool's observed acceptance can
  coexist — "not a valid UTF-16 string" does not imply "every parser
  refuses it".
- A JSON escape of the form backslash-u-DE00 is legal JSON syntax; consumers that then encode
  to UTF-8/UTF-16 without an error handler may themselves fail on it.

## Unknown

- The producer's actual decoder/implementation (not inspected).
- Behavior on other malformations: unpaired *high* surrogate, surrogate at
  string end, truncated code units, BOM or odd length fields.
- Whether a fresh producer run reproduces the saved result; the Evidence ID
  binds the saved output bytes only (Q09).
- Windows loader/resource-API treatment of the same bytes.

## Limitations

- Static, single-fixture, single-operation observation; no loader, runtime
  or rendering claim.
- No general claim about REA: one provider (`rea-pe-resources` v1), one
  operation, one saved run, verified from the saved record — no producer
  was called for this entry.
- The PE spec calls the field "Unicode strings" without fixing an
  encoding-form validity bar; the ill-formed verdict rests on Unicode D84/
  D91 applied to the observed UTF-16LE units, not on PE spec text.

## QUALITY check

| Q | verdict | basis |
|---|---|---|
| Q01 | pass | encoding claims rest on S010 definitions (tier A, spec); decoder behavior on S011 official docs; name-field format on S009; the r59 observation on S013 (own-work saved record) |
| Q02 | pass | source/verified-at/recheck headers present; anchors name sections, definition ids, doc revision |
| Q03 | pass | expected ill-formedness derived from bytes + Unicode definitions, not from the saved record |
| Q04 | pass | tool claim names `rea-agents@6.4.0`, `inspect_pe_resources`, provider v1, saved Evidence ID; Python decodes labeled manual |
| Q05 | pass | the capability/behavior observation carries its saved probe: receipt exit 0, empty stderr, Evidence ID, and the recheck command |
| Q06 | pass | offset 741, hex `41003d0000de42002100`, diff scope re-derived from bytes on 2026-10-19; falsified r59 input retained |
| Q07 | pass | the refusal was a pre-registered r59 hypothesis with spec ground truth; its falsification is recorded as such |
| Q08 | pass | every count/offset carries its command; `DE00` role (low surrogate) cites D73, not memory |
| Q09 | pass | the Evidence ID and stdout SHA-256 are cited only for the saved bytes; no producer-origin or rerun claim |
| Q10 | pass | observation scoped to provider/operation/version/fixture; other malformations and parsers left unknown |

## Provenance (Q11, appended 2026-10-19)

Appended after orchestrator review; nothing above is rewritten. Each stated
value is derived by the command below, run from the lane root at `35b2e8b`
(lane HEAD `19b3174` for the corpus), with its observed output.

- fixture identity (exit 0):

  ```sh
  sha256sum corpus/fixtures/pe-r59/fixture.exe corpus/fixtures/pe-r55/fixture.exe
  ```

  ```text
  2d294161e9eebd965919aad91065e5335e693199a17d95533f6c6c8fc751e6a0  corpus/fixtures/pe-r59/fixture.exe
  41c0132a9ecd8274d9afcfc079fefc0c5beb14c1ae81bc7bfa0a2832e140572b  corpus/fixtures/pe-r55/fixture.exe
  ```

- byte diff r55→r59 (exit 0):

  ```sh
  python3 -c "a=open('corpus/fixtures/pe-r55/fixture.exe','rb').read();b=open('corpus/fixtures/pe-r59/fixture.exe','rb').read();print(len(a),len(b),[(i,hex(a[i]),hex(b[i])) for i in range(len(a)) if a[i]!=b[i]])"
  ```

  ```text
  1536 1536 [(741, '0xd8', '0x0')]
  ```

- code units r59 and r55 (exit 0):

  ```sh
  python3 -c "import struct
  for f in ('pe-r59','pe-r55'):
   b=open('corpus/fixtures/%s/fixture.exe'%f,'rb').read(); print(f,struct.unpack_from('<H',b,736)[0],['%04X'%u for u in struct.unpack_from('<5H',b,738)])"
  ```

  ```text
  pe-r59 5 ['0041', '003D', 'DE00', '0042', '0021']
  pe-r55 5 ['0041', 'D83D', 'DE00', '0042', '0021']
  ```

- interpreter and decode modes (manual reproduction) (exit 0):

  ```sh
  python3 --version; python3 -c "h=bytes.fromhex('41003d0000de42002100')
  try: h.decode('utf-16-le')
  except UnicodeDecodeError as e: print('strict:',e)
  print('surrogatepass:',repr(h.decode('utf-16-le','surrogatepass')))"
  ```

  ```text
  Python 3.14.7
  strict: 'utf-16-le' codec can't decode bytes in position 4-5: illegal encoding
  surrogatepass: 'A=\ude00B!'
  ```

- saved r59 record (obs. 3) (exit 0):

  ```sh
  sha256sum corpus/live/runs/round-59/inspection.stdout.json; python3 -c "import json;d=json.load(open('corpus/live/runs/round-59/inspection.stdout.json'));r=d['normalized_result'];n=r['resources'][2]['name'];print(d['operation'],d['evidence_id'],repr(n['name']),n['utf16le_hex'],r['coverage'])"; python3 -c "import json;r=json.load(open('corpus/live/runs/round-59/receipt.json'));print({k:r[k] for k in ('command','exit_code') if k in r})" 2>&1 | tail -1
  ```

  ```text
  bf7922dbda2bc2dd817eaa13652f04e19c10ed8701feab5790a8703d55f22c0f  corpus/live/runs/round-59/inspection.stdout.json
  inspect_pe_resources ev_8ab30e10bf3d0e73c44c831c9cbb1839d1117db21379e163085ab9d8fec0f8db 'A=\ude00B!' 41003d0000de42002100 {'status': 'complete', 'examined_entries': 8, 'resources': 3}
  {'command': 'npx -y rea-agents@6.4.0 inspect-pe-resources /home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/fixtures/pe-r59/fixture.exe --format json', 'exit_code': 0}
  ```

- Unicode D91 quote (S010) (exit 0):

  ```sh
  curl -sL https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-3/ | python3 -c "import sys,re,html;t=re.sub(r'\\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',sys.stdin.read())));i=t.find('isolated UTF-16 code units');print(t[i:i+70])"
  ```

  ```text
  isolated UTF-16 code units in the range D800 16 ..DFFF 16 are ill-form
  ```
