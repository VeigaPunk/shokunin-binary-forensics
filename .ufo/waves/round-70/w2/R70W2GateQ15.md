# R70W2GateQ15 — Q15 decision on the landed C05 v5.1 candidate

**PASS** — the landed entry states no git object id and no tree identity anywhere (0 hits in prose, the only 40-hex token is the dex SHA-1 signature, re-derived), so Q15 is vacuously satisfied; every identity it does state is a `sha256` file digest, and all 10 re-derive byte-for-byte against the extracted landed bytes.

Target: `corpus/knowledge/round-70-apk-axml-byte-evidence.md` at lane commit `17ee7f87ea8ee72a427af0fd8e7586d09bad99cd`, sha256 `819efcb8e2f6065c6b73456ed24502fe0b4e9751c94366e5a6c3f3b4990b4c31` (from `git archive 17ee7f87… | tar -x`, not the working tree). Criterion: `corpus/QUALITY.md:27`. Contract: `reports/round-70/claims.md` §C1 (kill rule: a FAIL carrying a located defect falsifies C1). Amendment: `reports/round-70/claims-amendment-A1.md:46-50`. I did not consult `.ufo/waves/round-70/w1/` before forming this verdict.

## 1. Sweep — no git object id, no `X:corpus` sentence

```
$ git -C …/revenger-shokunin archive 17ee7f87ea8ee72a427af0fd8e7586d09bad99cd corpus SHONEN.md SCORECARD.md SKILL.md README.md | tar -x -C /tmp/revenger-r70-R70W2GateQ15
$ cd /tmp/revenger-r70-R70W2GateQ15 && sha256sum corpus/knowledge/round-70-apk-axml-byte-evidence.md
819efcb8e2f6065c6b73456ed24502fe0b4e9751c94366e5a6c3f3b4990b4c31  corpus/knowledge/round-70-apk-axml-byte-evidence.md
```

Search 1 — git-identity constructs over all 322 lines:

```
$ grep -n -i -E "\bcommit|\btree\b|\bblob\b|object id|rev-parse|:corpus|git -C|git show|git archive" corpus/knowledge/round-70-apk-axml-byte-evidence.md
1: … https://android.googlesource.com/…            (URL host, not an id)
2: … compared it byte for byte with the committed snapshot …   (author action, no id)
3: … re-fetched the live page and compared it with the committed snapshot … (author action, no id)
4: … "committed snapshot copy `corpus/snapshots/APPNOTE.TXT`" … (path, no id)
15: … committed standard-library scripts named below …          (prose, no id)
119: … printed by the committed derivation …                     (prose, no id)
282: … from the committed bytes …                               (prose, no id)
312:| Q15 | pass | this entry states no git object id; …        (the row under test)
```

No `rev-parse`, no `X:corpus`, no `git show`, no `blob`, no 40- or 64-hex object token in any of these lines. `:corpus` occurs zero times.

Search 2 — every hex run of 7-40 chars, partitioned by fence membership (computed, not eyeballed):

```
$ python3 - <<'PY'   # fence-aware sweep
… re.finditer(r'\b[0-9a-f]{7,40}\b', line) for lines outside ``` fences …
PY
hex tokens >=7 inside PROSE (outside fences): 0
```

All hex-shaped values live inside command-output fences and are labeled at their source: `504b0506` (EOCD signature, `:36`), `03000800…` / `6465780a…` / `4d616e69…` (`payload_first16_hex`, `:43,45,47`), crc32s `962d075f`/`2635c82a`/`e948d738` (`:43,45,47`), resource ids `16843291`/`16843292` and `4294967295` (`NO_INDEX`, `:90,94,202`), `6465780a30333500` (`magic_hex`, `:105`). None is presented as a git id; none is introduced by `commit`/`base`/`tip`/`since`/`at`.

Search 3 — uppercase and non-ASCII confusables (a git id is case-insensitive at the CLI, so a lower-case-only sweep is not enough):

```
$ grep -n -o -E "\b[0-9A-F]{7,40}\b" …   → only 4294967295 / 16843291 / 16843292 (decimal fields in JSON output)
$ grep -n -P "[^\x00-\x7F]" …             → only em-dashes and `…` ellipses; no zero-width or homoglyph inside a hex run
```

## 2. The single 40-hex token is not a git id — re-derived

`:105` prints `"signature_sha1": "a5fc7bea8fa9ffaa52243540c8026066511b9fce"` and `"signature_recomputed"` with the same value. Re-derived from the landed fixture, and compared against the git blob id of the same member:

```
$ python3 - <<'PY'
z=zipfile.ZipFile('corpus/fixtures/apk-r65/fixture.apk'); dex=z.read('classes.dex')
print(hashlib.sha1(dex[32:]).hexdigest())                 # dex signature field
print(hashlib.sha1(b'blob %d\0'%len(dex)+dex).hexdigest())  # git blob id of that file
PY
dex len 112 sha1(dex[32:])= a5fc7bea8fa9ffaa52243540c8026066511b9fce token==that: True
git blob id of classes.dex = e69eef0c8b9f615df232ce7a12b39397e4585c4f token==blob: False
```

The value is the dex `signature` field (SHA-1 of the file after byte 32), exactly as labeled; it is not `git hash-object` of any file.

## 3. Digests are file digests, and they re-derive (10/10)

The `:312` row says identity statements are file digests printed by item 14. I did not take that row as evidence; I ran the item-14 command from the extraction and diffed it against the embedded block:

```
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --pins > pins.actual        # exit=0
$ sed -n '222,231p' corpus/knowledge/round-70-apk-axml-byte-evidence.md > pins.embedded
$ diff pins.actual pins.embedded && echo "IDENTICAL: 10/10 digest lines re-derive byte-for-byte"
IDENTICAL: 10/10 digest lines re-derive byte-for-byte
```

Independently (`sha256sum`, outside the entry's tooling) the same ten values:

```
05d2280f…7d03e  corpus/fixtures/apk-r65/fixture.apk
27303bae…f8173  corpus/fixtures/apk-r65/truth.json
eaa9444c…27c1a  corpus/fixtures/apk-r65/generator.py
92e347c3…13976  corpus/fixtures/apk-r65/readout.py
2d4f25f6…b1f9  corpus/fixtures/apk-r65/entry_checks.py
74d4c0d9…a83aa  corpus/derive_axml_anchors.py
56b88bc4…7c56f  corpus/snapshots/ResourceTypes.h
0b993022…0cd6  corpus/snapshots/APPNOTE.TXT
c0428612…d9f4  corpus/snapshots/dex-format.html
412d9cb4…a74c  corpus/snapshots/rea-android-applications.md
```

Every one is prefixed `sha256` in the entry and matches the bytes; the member digests at `:43,45,47` match the actual ZIP member bytes (`73d1e0f2…`, `57cfe887…`, `2e5da249…`). None of the ten is a git object in this repo, and the repo's object format rules out a 64-hex id here:

```
$ git -C …/revenger-shokunin rev-parse --show-object-format
sha1
$ for h in $(awk '{print $2}' pins.actual); do git -C …/revenger-shokunin cat-file -t $h; done | sort | uniq -c
     10 -> fatal: Not a valid object        # all ten digests: not in the object namespace
```

The item-11 digest is the same story: `:123` prints `sha256 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f ResourceTypes.h`, and running the entry's own command reproduces that line and the 19 anchor lines below it:

```
$ python3 -B corpus/derive_axml_anchors.py | head -1
sha256 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f ResourceTypes.h
$ diff <(sed -n '2,20p' derive.actual) <(sed -n '124,142p' entry.md) && echo match
enum/anchor lines 2-20 match embedded
```

**No digest is mislabeled as a git id, and no git id is labeled as a digest.**

## 4. Negative controls on the mechanical Q15 guard (lint scope, not entry defect)

`corpus/lint_entry.py:17` defines the Q15 class as *a backticked 7-40 hex token introduced by `commit`, `base`, `tip`, `since` or `at` must resolve under `git cat-file -e <h>^{commit}`*. Mutants on copies (lane files untouched), lint run with `--lane …/revenger-shokunin`:

| mutant (inserted prose line) | LINT_Q15 | exit |
|---|---|---|
| none (landed bytes) | 0 | 0 |
| `The fixture bytes are unchanged since \`deadbeef\`.` | 1 `[(18,'deadbeef')]` | 1 |
| `The corpus tree at \`17ee7f87:corpus\` is byte-identical to the tree whose digest is sha256 \`819efcb8…\`.` (wrong value; real tree is `fa1010d4…`) | **0** | 0 |
| `The corpus tree is \`fa1010d4\`.` (a tree id, not a commit) | 0 | 0 |
| `The base is \`deadbeef\`, the landed target.` (introducer not adjacent) | 0 | 0 |

`git -C … rev-parse 17ee7f87:corpus` → `fa1010d45808261d5c32dcb98332d3c7b8557b86`; `…:corpus/knowledge` → `08c3fc3cf47d20c8aaae2548fc5c73644153d540`. So the second half of `QUALITY.md:27` — "a sentence asserting `X:corpus` equals a hash must resolve under `git rev-parse X:corpus`" — has **no mechanical guard**: a future entry could assert a wrong `X:corpus` hash and still read `LINT_Q15=0`. This is a lint-coverage limit (its docstring scopes itself to four classes), not a defect in these bytes and not a Q15 FAIL; it does mean `LINT_Q15=0` is strictly weaker than the Q15 rule and my PASS rests on §1-§3, not on the lint.

## 5. Provenance notes (recorded, not kill-rule inputs)

1. `claims.md:35` names "the `c7b7cf98` identity derived and a Q15 row" among the v5 repairs, but neither the v5 build (`aa1842f`) nor the landed v5.1 states it: `git show aa1842f:…| grep c7b7cf98` → `(absent in v5 entry)`; landed → `(absent in v5.1)`. `c7b7cf98` **does** resolve (`git cat-file -t c7b7cf98` → `commit`; `c7b7cf98ddeecbd5464e47396f224e6384b78905 round-65: candidates …`). A1:46-50 already records this deviation as "the v5 entry instead states no git object id at all", so the `:312` row is true of the bytes and the stale C1 prose is not a Q15 defect. Consequence for admission: Q15's PASS is **vacuous** — it certifies the absence of an un-derivable identity, not the presence of a derived one.
2. `:312`'s basis clause is slightly overbroad: identity digests also print at `:27`, `:43,45,47`, `:123`, `:182-214` and `:238`, not only in item 14. Every one of them carries its command, so no Q11-style defect; and my decision does not rest on the row.
3. `:2`-`:3` assert author actions ("re-fetched the raw file and compared it byte for byte with the committed snapshot"; "the live page differs from the snapshot only in page-chrome lines") that no committed command can re-derive offline. They name no git id and no tree, so they are outside Q15; routed to Q06/Q09 (`:4` and `:308` already fence currency, and `:14`'s sentence disclaims faithful fetching).

## 6. Decision

**PASS** for Q15 on the landed bytes `sha256 819efcb8e2f6065c6b73456ed24502fe0b4e9751c94366e5a6c3f3b4990b4c31`. Basis: zero git object ids / tree identities in the 322 lines (§1), the only 40-hex token re-derived as the dex signature and shown not to be a blob id (§2), ten digests re-derived byte-for-byte and shown to be sha256 file digests, not git ids (§3). No FAIL, no defect pointer, therefore no kill-rule input against C1 from this seat. Independent of the entry's `:312` row.

No lane file was edited; the only writes were `/tmp/revenger-r70-R70W2GateQ15/*` (deleted) and this report. No git or jj mutating command was run. No package installed or upgraded; tools used: system `python3`, `git`, `sha256sum`/`diff` — no installs, so no tool record is due.
