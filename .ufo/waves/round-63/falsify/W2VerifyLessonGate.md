# W2VerifyLessonGate — lesson-gate verification (revenger round 63, falsify wave)

Seat `revenger-r63.W2VerifyLessonGate` (scribe). Axes: coverage, calibration.
No installs, no `pacman`, no `uv`/`npm`. Only pre-present tools were used:
`python3` 3.14.8 (`/usr/bin/python3`), `binwalk` 3.1.0 (`/usr/bin/binwalk`),
`curl`, `git`, `awk`/`grep`. Scratch: `/tmp/revenger-r63-w2lesson/` (removed
after this report lands). Nothing under `corpus/` was written; no git mutation,
no commit, no push.

**Tip attacked.** The lane tip moved under this seat while it ran. All findings
below are re-verified against the tip that was current when each check ran and
are marked with the commit they were taken at.

- `db55bd6488e24e956df5818ae34c2a043d7ddc12` — "round-63: C1 candidate entry …
  SOURCES S032+S033, round-63 lesson" (2 landed rows).
- `aaa046326d92ba983f3ae99341438c9b8509a6cc` — "round-63: corrected C1 entry
  (wc-w fix, S034/S035 citations, derived metadata), S034+S035 registry rows,
  LEDGER receipt-pin fix, lesson Gate+M35 updates" (4 landed rows). **Final
  tip; every verdict below is stated at `aaa0463`.**

---

## Verdict

**NOT CONFORMANT — 3 located gaps, 1 at-a-tip contradiction.** The lesson's
`## Gate`, `## Mistakes`, `## Search log` and `## Routed debt` sections are
substantially present and their load-bearing content re-verifies against
committed bytes. The gaps are in (a) the located-quote coverage for the two
newly-landed rows S033/S035, (b) the `## Mistakes` M34 fix column, which
names no falsifiable demonstration, and (c) the `## Search log` reconciliation
against the four rows actually landed at the final tip.

---

## Gap 1 — S033 and S035 land with no located quote in `## Gate`

**Located at:** `corpus/lessons/round-63.md` lines 130–140 (S033 record) and
lines 123–129 (S035 record).

The `## Gate` section opens at line 29 with the rule it is held to
(`corpus/lessons/round-63.md:33-35`):

> "Access date **2026-10-23** for every row below. Each located quote is at most
> 25 words and is verbatim against the pinned snapshot…"

and the fleet contract that rule comes from (`/home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md`, rule 1) says:

> "A row is a claim. Write it only after opening the source in the round that
> writes the row. **The round lesson's `## Gate` records, for every new row, the
> URL, the access date, and a ≤25-word quote with its location grounding
> `teaches`.**"

Four rows are new in this round (`corpus/SOURCES.md`, ids S032, S033, S034,
S035). Per-row state at the final tip:

| row | kind | URL in Gate? | access date in Gate? | ≤25-word located quote in Gate? | quote verbatim? |
|---|---|---|---|---|---|
| S032 | spec | yes (`https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT`) | yes (2026-10-23) | **yes** — 9 quotes, 7/21/7/8/23/24/23/12/20 words | yes (normalized) |
| S033 | own-work | n/a (own-work rows carry file paths, not URLs) | yes (2026-10-23) | **NO — zero quotes** | — |
| S034 | spec | yes (same APPNOTE URL) | yes (2026-10-23) | **yes** — 1 quote, 7 words | yes (normalized) |
| S035 | own-work | n/a (own-work rows carry file paths, not URLs) | yes (2026-10-23) | **NO — zero quotes** | — |

Evidence — the S033 Gate record contains **no double-quoted string at all**
(the only `"` pair in the segment is the contract-rule quotation about
`` `S` + 3 or more digits `` in the *Id allocation* paragraph, which follows
it):

```
$ python3 - <<'EOF'
t=open('corpus/lessons/round-63.md').read()
i=t.index('**S033 (own-work)'); j=t.index('**Id allocation')
seg=t[i:j]
import re
print('has double-quoted located quote:', re.search(r'"[^"]{10,}"', seg) is not None)
EOF
has double-quoted located quote: False
```

The S035 record quotes only its own **scope** string, not a located quote from
the source it names:

```
$ python3 -c "…print(re.findall(r'\"[^\"]{5,}\"', seg))"
['"the recorded\nobservation/inference/unknown layer of the saved archive inventory record,\ncited for provenance only"']
```

That is the scope cell echoed back, not a located quote against
`corpus/live/runs/20261012T164246Z/LEDGER.md` (or against
`corpus/fixtures/archive-r2/*` for S033). Neither record names the anchor
inside the source (a field path, a line, a byte offset) that would ground its
`teaches` cell the way S032's and S034's do.

**Contrast — the pre-existing lane precedent is the opposite.** The same
contract's rule 1 was applied to own-work rows in round 62
(`corpus/lessons/round-62.md:76-84`): S030 carries the located quote
`const { rot13, checksum } = require('./transform');` anchored at
`corpus/fixtures/js-r3/index.js:1` at `a3498e25`, and S031 carries
`Original carrier and decoded bytecode SHA-256 are distinct identities; SHA-256
is not the Ethereum Keccak code hash.` anchored at
`corpus/live/runs/round-19/inspection.json` `limitations[4]`. So the round-62
lesson did give own-work rows a located quote; round 63 gives two of its four
new rows none. That is a gap in the same gate the round-62 lesson met, not a
matter of taste.

**Calibration consequence:** the `teaches` cells of S033 and S035 in
`corpus/SOURCES.md` are therefore ungrounded by any located quote in the
lesson. S033 `teaches` = "A byte readout of one archive's central directory can
be checked field by field against an independent oracle and against one saved
record's literal fields, without claiming the record is complete or
authentic."; S035 `teaches` = "The recorded observation/inference/unknown layer
of the saved archive inventory record is cited for provenance only, with no
value derived from it, so a ledger's own framing is never read as a provider
claim." Neither sentence is tied to a located quote.

---

## Gap 2 — M34's fix column names no falsifiable demonstration

**Located at:** `corpus/lessons/round-63.md:214`, `## Mistakes` table, column
`fix / falsifiable demonstration`.

The `## Mistakes` table header (line 211) is
`| id | class | evidence | captured-by | fix / falsifiable demonstration |`, so
the fifth column is required to carry a *falsifiable demonstration*, not a
process intention. All three rows populate all five cells:

```
$ python3 - <<'EOF'
for i,l in enumerate(open('corpus/lessons/round-63.md').read().split('\n'),1):
    if l.startswith('| M3'):
        c=l.split('|')[1:-1]
        print(f'line {i} id={c[0].strip()} cells={len(c)} nonempty={[bool(x.strip()) for x in c]}')
EOF
line 213 id=M33 cells=5 nonempty=[True, True, True, True, True]
line 214 id=M34 cells=5 nonempty=[True, True, True, True, True]
line 215 id=M35 cells=5 nonempty=[True, True, True, True, True]
```

But M34's fifth cell is:

> "keep the two gates separate in the report: the printed counter value is
> reported next to the substantive evidence (entry + fresh Q01–Q13 decisions;
> receipt + fixture + byte oracle; frozen diff of the `receipt_ok` refactor), and
> L1 reviews the committed diff against the frozen fix sentences as well as
> reading the attributed tally. The frozen counter and the round-61 probe stay
> untouched"

That is a reporting *policy*. It names no command, no expected output, and no
state in which the fix would be visibly wrong — nothing a falsifier could run
and watch fail. By contrast M33's fifth cell is a runnable falsifier
(`oracle_check.py` returns 1 with a named MISMATCH line on a mutated record)
and M35's fifth cell is a routing decision with a named residual. M34's cell
has neither.

**M34's own evidence cell is strong and its cited source exists** — I re-opened
`.ufo/waves/round-63/build/R63CriticClaims.md` and confirmed all three
sub-items are present there (line 45 the invented-evidence-id JSON, line 48 the
`F_COVERAGE=5/8` claim, lines 61/67 the two `forged receipt` source-text
canaries). The gap is that the *fix* column does not carry the demonstration
forward.

---

## Gap 3 — `## Search log` does not reconcile with the four rows landed at the tip

**Located at:** `corpus/lessons/round-63.md:217-286` (`## Search log`) and
`corpus/SOURCES.md:73` (the registry's own search-log note).

At the final tip `corpus/SOURCES.md` carries **four** new round-63 rows —
S032, S033, S034, S035 — all `mined`:

```
$ grep -oE '^\| S0[0-9]+' corpus/SOURCES.md | tr -d ' |' | tail -5
S031
S032
S033
S034
S035
```

The lesson's `## Search log` still reports the counts from the two-row world:

```
Identified **3**, screened **3**, included **1** row (S032), excluded **2**.     # archive query
Identified **3**, screened **3**, included **0** registry rows, excluded **3**    # firmware query
```

and `corpus/SOURCES.md:73` says the same thing:

> "…Archive query: primary spec for ZIP central-directory/EOCD field layout.
> Identified 3, screened 3, **included 1 row (S032)**, excluded 2 … Unit: one
> proposed registry document set; the own-work archive fixture/record set is
> S033, counted outside the external-document totals."

`S034` and `S035` appear in **neither** search-log entry, in either file:

```
$ python3 -c "…print('mentions S034:', 'S034' in s, '| mentions S035:', 'S035' in s)"
mentions S034: False | mentions S035: False
```

So the "included" tally (1) is not reconcilable with the landed-row set (4)
without a reader independently discovering that the two later rows are
counted in neither query. The archive query's own exclusion list is also
stale — it names two exclusions (the APPNOTE 6.3.9 fallback revision and the
Python `zipfile` docs) but not the fact that a *second* APPNOTE row (S034, a
scoped re-open of the same document) was subsequently landed and included.
Contract rule 5 requires the counts to be stated per bounded search; the
lesson states them, but they no longer describe the round that produced the
committed registry.

**Two further stale count statements in the same lesson, same cause** (both
were true at `db55bd6` and are false at `aaa0463`):

1. `corpus/lessons/round-63.md:155-158` — "**Registry state at draft time
   (verified, not assumed):** `corpus/SOURCES.md` still ends at **S031**;
   `grep -n 'S032\|S033\|S034' corpus/SOURCES.md` returns nothing." At the tip
   `corpus/SOURCES.md` ends at **S035** and that grep returns five matches. The
   sentence is explicitly scoped "at draft time", so it is defensible as
   history — but it sits inside the committed lesson at `aaa0463` where the
   rows it denies are present in the same commit, and the `## Gate` S034/S035
   records added in that same commit do not update it.
2. `corpus/lessons/round-63.md:147-148` — "the earlier S034 reservation is
   withdrawn, and the candidate is renumbered to **S032 ×10 / S033 ×5 /
   S034 ×0**". At the tip the committed entry cites S034 **15** times and S035
   **11** times (S032 ×13, S033 ×11):

```
$ for id in S032 S033 S034 S035; do printf "%s: " $id; \
    grep -o "$id" corpus/knowledge/round-63-zip-central-directory-evidence.md | wc -l; done
S032: 13
S033: 11
S034: 15
S035: 11
```

The id-allocation paragraph was not updated in `aaa0463` even though that
commit landed S034 and S035 and added their Gate records. This is the
"contradiction" item: within one committed file, the `## Gate` records four
round-63 rows while the id-allocation paragraph says the round's ids are "the
contiguous pair **S032 + S033** with no id skipped" and that S034 was
"withdrawn".

**Calibration note — this is a documentation-staleness defect, not a
falsification.** The landed rows S032/S033/S034/S035 are internally consistent
and each carries a real opened date, a real tier, a real `mined` status and
existing `used-by` paths:

```
S032 | kind= spec     | tier= A | status= mined | opened= 2026-10-23 | recheck= on-release | used-by= corpus/knowledge/round-63-…md, corpus/lessons/round-63.md
S033 | kind= own-work | tier= A | status= mined | opened= 2026-10-23 | recheck= on-release | used-by= corpus/knowledge/round-63-…md, corpus/lessons/round-63.md
S034 | kind= spec     | tier= A | status= mined | opened= 2026-10-23 | recheck= on-release | used-by= corpus/knowledge/round-63-…md
S035 | kind= own-work | tier= A | status= mined | opened= 2026-10-23 | recheck= on-release | used-by= corpus/knowledge/round-63-…md
```

No duplicate ids, no malformed rows, no tier/kind enum violation among the
four new rows. The defect is that the lesson's prose and the registry's
search-log entry were not carried forward with the two rows the same commit
landed.

---

## Verified CONFORMANT

### Gate — S032 record: complete, and every quote re-verified verbatim

URL, kind, tier, scope, opened date (2026-10-23), HTTP 200, byte count
(174585), spec version (6.3.10), snapshot path + sha256
`0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6` — all
present (`corpus/lessons/round-63.md:37-47`).

**All nine located quotes are ≤25 words.** Counted by whitespace split:
7, 21, 7, 8, 23, 24, 23, 12, 20 — max 24. ✔

**All nine are verbatim substrings of the whitespace-normalized snapshot**, and
each cited line range contains its quote:

```
§4.3.12 L522           cited-range-contains-quote=True    (7 words)
§4.3.12 L529-533       cited-range-contains-quote=True   (21 words)
§4.3.12 L538           cited-range-contains-quote=True    (7 words)
§4.3.16 L634           cited-range-contains-quote=True    (8 words)
§4.3.16 L638-641       cited-range-contains-quote=True   (23 words)
§4.4.16 L983-985       cited-range-contains-quote=True   (24 words)
§4.4.7a L911-912       cited-range-contains-quote=True   (23 words)
§4.4.7b L912-913       cited-range-contains-quote=False  (12 words)  ← see below
§4.3.3 L350-351        cited-range-contains-quote=True   (20 words)
```

One nit worth recording, not a gap: the §4.4.7b quote "value is put in the
data descriptor and in the central directory." is cited as **lines 912–913**,
but line 912 is `field is set to zero in the local header and the correct` and
line 913 ends `…and in the central` — the word `directory.` is on **line 914**
(`directory. When encrypting the central directory, if the`). The quote text
itself is a correct substring of the normalized snapshot; the second line
citation is off by one. The preceding §4.4.7a quote cites 911–912 and is
exact.

**Independent re-fetch of the pinned source (network, 2026-10-24):**

```
$ curl -sS -o primary.txt -w "http=%{http_code} size=%{size_download}\n" \
    https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT
http=200 size=174585
$ sha256sum primary.txt
0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6  primary.txt
$ cmp primary.txt .ufo/waves/round-63/source-snapshots/appnote.txt && echo IDENTICAL
IDENTICAL
```

The lesson's S032 snapshot digest is exact. The fallback-URL divergence the
lesson records also re-verifies exactly — `https://pkware.com/documents/casestudies/APPNOTE.TXT`
redirects to `…/APPNOTE-6.3.9.TXT`, HTTP 200, 173575 bytes, sha256
`c7cf1fecfbde36ebbfbac643e6183d5c76fac983c2066fb8e32c6e4058a87e80`, header
"Version: 6.3.9 / Status: FINAL - replaces version 6.3.8 / Revised: July 15,
2020" — matching `corpus/lessons/round-63.md:65-70` verbatim.

**S034 record** (`corpus/lessons/round-63.md:111-121`): URL, opened date
(2026-10-23), tier, scope, snapshot digest, and a located quote
"local file header signature 4 bytes (0x04034b50)" — **7 words**, and
verbatim at snapshot **line 389**, `§4.3.7`:

```
$ python3 -c "…print(lines[388])"
'      local file header signature     4 bytes  (0x04034b50)'
```

✔ (whitespace-normalized; the raw line has the fixed-width padding, and the
lesson's normalization note covers that.)

### Gate — zipfile-docs screened-and-excluded record

Quote "Any advanced use of this module will require an understanding of the
format, as defined in PKZIP Application Note." — **19 words** as the lesson
claims, and it is verbatim against the pinned snapshot **after HTML tag
stripping** (the raw HTML has an `<a class="reference external" …>` wrapper
around "PKZIP Application Note", so the plain-text form is not a literal
substring of the raw file). The lesson presents it as a located quote without
stating that tags are stripped — a disclosed-normalization nit, not a
fabrication. The snapshot digest re-verifies:
`9520a8cbce7d3c8b7ea6704f60ac1122856da14d1bdc4161075912303a270739` (139782
bytes), and the page footer "Last updated on Oct 24, 2026 (00:13 UTC)." is
present in the committed snapshot.

### Mistakes — M33 fix is falsifiable, and I re-ran it

**The M33 red-before command and its observed failure** (the target's explicit
ask) — named from `corpus/lessons/round-63.md:213` and
`reports/round-63/claims.md` §C2, and reproduced by me:

- **Red-before command:** `binwalk` 3.1.0 signature scan of the fixture image
  (the committed form is
  `binwalk --quiet --search-all --threads 1 --log <report.json> <copied input>`,
  `.ufo/waves/round-63/build/R63ScoutFirmware.md:133`).
- **Observed failure:** **zero regions** found in the 1056-byte uImage-header
  image. I rebuilt that image from the recorded recipe
  (`struct.pack('>I', 0x27051956) + 1052 zero bytes`), confirmed it hashes to
  the recorded `b4e9f53c88b4c5a593ac6df61ae35f89e5b432cf454bde0f7167475f91164347`,
  and scanned it:

```
$ binwalk --threads 1 magic-only-1056.bin | tail -1
Analyzed 1 file for 85 file signatures (187 magic patterns) in 1.0 milliseconds
$ binwalk --search-all --threads 1 magic-only-1056.bin | tail -1
Analyzed 1 file for 85 file signatures (196 magic patterns) in 1.0 milliseconds
# both reports: file_map = []   → ZERO regions, exit 0
```

✔ matches the lesson's M33 evidence exactly ("zero findings under both the
default and `--search-all` scans"; 85 file signatures; 187 vs 196 magic
patterns).

- **Positive control, also reproduced:** a 512-zero-byte prefix + a 55-byte
  `zlib` stream at offset 512 → **default scan: zero hits**, `--search-all`:
  `512 0x200 Zlib compressed file, total size: 55 bytes` (JSON `offset 512`,
  `size 55`, `name "zlib"`, confidence 250). ✔ matches the lesson's "the
  positive control … needs binwalk's `--search-all`".

- **The M33 fix is shown able to fail — verified by execution, not assertion.**
  The fix cell names `corpus/live/runs/round-63/oracle_check.py` and two
  mutation outcomes. I ran the committed oracle on the committed record and on
  two mutated copies:

```
$ python3 -B corpus/live/runs/round-63/oracle_check.py     # on committed tree
REGION name=diagnostic-note kind=zlib offset=512 size=79 offset=OK size=OK signature=OK decompressed_sha256=OK (a5718481…)
REGION name=component-note  kind=zlib offset=1024 size=90 offset=OK size=OK signature=OK decompressed_sha256=OK (2d0d86aa…)
ORACLE OK                                                            # exit 0

# mutation 1 — shift first reported offset 512 -> 513
exit=1
MISMATCH normalized_result.regions[0].offset: expected 512, got 513

# mutation 2 — drop the last reported region
exit=1
MISMATCH normalized_result.regions: expected 2 reportable regions, got 1
MISMATCH normalized_result.regions[1]: missing reported region

# mutation 3 — swap the first 512 padding bytes for ff (different physical image)
exit=1
MISMATCH subject.digest.sha256: expected bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be, got '4653a32e…'
```

All three failure strings are **exactly** the ones the lesson's M33 fix cell
promises ("returns 1 with `MISMATCH normalized_result.regions[0].offset: expected
512, got 513`", "returns 1 with `MISMATCH normalized_result.regions: expected 2
reportable regions, got 1`", "yields `MISMATCH subject.digest.sha256`").
✔ **M33's fix is shown able to fail, by command and by observed output.**

### Mistakes — M35 evidence re-verified, and the corrected widening re-verified

M35's evidence claims that deleting the `stdout_sha256` conjunct from
`corpus/verify_icon_states.py` leaves the self-test **green**. Reproduced on a
/tmp copy of the committed corpus tree:

```
$ python3 -B verify_icon_states.py --self-test
PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
EXIT=0
```

✔ exact string match with the lesson's M35 evidence cell.

M35's `aaa0463` correction (widening the debt from one conjunct to two) also
re-verifies on committed bytes: `corpus/verify_named_multi_icon_states.py:17`
carries `receipt['stdout_sha256']==H(raw)` inside its `receipt_ok(...)`
conjunction, and `corpus/verify_icon_states.py:121` carries the `stdout_sha256`
assert — so **both** scripts have a `stdout_sha256` conjunct and neither is
guarded by the frozen in-script forged-receipt control, which forges `command`
(named) and `fixture_sha256` (icon_states) only. The corrected routed-debt row
names both files. ✔

### Search log — the two entries are structurally present

Both required queries are present with query / where / date / identified /
screened / included / excluded counts, exclusion reasons with reasons, and a
stop rationale (`corpus/lessons/round-63.md:225-286`). The convention is stated
("one proposed registry document set … the lane's own authored fixture/record
sets count once each"), the divergence from the sibling seat's counts is
recorded verbatim rather than smoothed, and L1's resolution is stated
("L1 resolved in favour of **this** note, dropping the §6 block"). The
`screened` count equals `identified` for both queries and
`included + excluded = screened` for both — the arithmetic is internally
consistent. **The gap is only that the counts predate the two rows the same
commit landed** (Gap 3).

### Routed debt — round-62 defect (a) named and dispositioned ✔

`corpus/lessons/round-63.md:292` is the first row of the `## Routed debt`
table and names the round-62 defect (a) explicitly:

> "**(a) on-tip re-verification output was not committed alongside the report
> claim in round 62** | `corpus/lessons/round-62-verifier-spotcheck.md:63` —
> "commit the resume re-verification output alongside the report claim when a
> resumed attempt re-runs the probe on the final tip (this round's on-tip
> re-run is closure-verified but was not itself committed)" | **Honored.** …"

I verified the quoted defect text is byte-exact against
`corpus/lessons/round-62-verifier-spotcheck.md:63` (the string is present on
that line), the disposition is stated (**Honored**), and the disposition names
the concrete binding measurement
(`python3 -B reports/round-63/measure.py TREE` over `git archive <final-commit>
corpus`, cwd `/`, `TMPDIR` under lane scratch, output committed as
`reports/round-63/measure-after.log` **in the same commit as the report
claim**). The defect is named, quoted, sourced to a line, and dispositioned.

**Outstanding at the tip (expected pre-admission, recorded as a dependency not
a gap):** `reports/round-63/measure-after.log` does not exist yet —

```
$ ls reports/round-63/
claims.md  measure-before.log  measure.py
```

The routed-debt disposition is a commitment to be discharged at the admitting
commit, and README C06 correctly still reads `partial` at the tip. The
discharge is L1's to make in the same commit as the report claim; this seat
does not assert it has happened.

### Out of scope, observed in passing (not part of this seat's target)

- `corpus/lessons/round-63.md` line 148's id-count claim is stale (Gap 3).
- `corpus/lessons/round-63.md:156`'s "still ends at S031" is stale (Gap 3).
- The §4.4.7b quote's second line citation is off by one (above).
- The zipfile-docs quote needs HTML tag stripping to be a substring of the
  snapshot (above).
- The S032/S034 rows' `teaches` cells assert fixed record sizes ("fixed
  46-byte record", "fixed 22-byte record", "fixed 30-byte record") that are
  **not** in the APPNOTE snapshot text — the strings "46 bytes", "22 bytes" and
  "fixed 30" do not occur in the normalized snapshot at all. Those sizes are
  *derived* (by summing the field widths the quotes do cover), not quoted.
  This bears on Q01/anchor grounding, which is the `W2AttackEntryQ01` seat's
  target, not this seat's — recorded here as an observation for the judge, not
  as a verdict.

---

## Reproduction commands (all read-only except the /tmp copies)

```sh
cd /home/vgpnk/Projects/shokunin/revenger-shokunin
git rev-parse HEAD                       # aaa046326d92ba983f3ae99341438c9b8509a6cc
git show --stat --oneline HEAD           # the tip move that added S034/S035

# Gate rows present + status
python3 - <<'EOF'
t=open('corpus/SOURCES.md').read()
for l in t.split('\n'):
    if l.startswith('| S03') and l.count('|')-1==11:
        c=[x.strip() for x in l.split('|')[1:-1]]
        if c[0] in ('S032','S033','S034','S035'):
            print(c[0], c[2], c[3], c[7], c[8], c[9], c[10])
EOF

# quote word counts + verbatim + line-range containment
python3 - <<'EOF'
import re
snap=open('.ufo/waves/round-63/source-snapshots/appnote.txt',encoding='utf-8',errors='replace').read()
n=re.sub(r'\s+',' ',snap); lines=snap.split('\n')
for q in ["central file header signature 4 bytes (0x02014b50)",
          "crc-32 4 bytes compressed size 4 bytes uncompressed size 4 bytes file name length 2 bytes extra field length 2 bytes",
          "relative offset of local header 4 bytes",
          "end of central dir signature 4 bytes (0x06054b50)",
          "total number of entries in the central directory on this disk 2 bytes total number of entries in the central directory 2 bytes",
          "This is the offset from the start of the first disk on which this file appears, to where the local header SHOULD be found.",
          "If bit 3 of the general purpose flag is set, this field is set to zero in the local header and the correct",
          "value is put in the data descriptor and in the central directory.",
          "All values MUST be stored in little-endian byte order unless otherwise specified in this document for a specific data element.",
          "local file header signature 4 bytes (0x04034b50)"]:
    print(len(q.split()), q in n)
EOF

# S033/S035 have no located quote
python3 - <<'EOF'
import re
t=open('corpus/lessons/round-63.md').read()
for a,b in [('**S033 (own-work)','**Id allocation'), ('**S035**','**S033 (own-work)')]:
    print(re.findall(r'"[^"]{10,}"', t[t.index(a):t.index(b)]))
EOF

# M33 red-before reproduction
python3 -c "import struct;open('/tmp/m.bin','wb').write(struct.pack('>I',0x27051956)+bytes(1052))"
binwalk --quiet --threads 1 --log /tmp/r1.json /tmp/m.bin && python3 -c "import json;print(json.load(open('/tmp/r1.json'))[0]['Analysis']['file_map'])"
binwalk --quiet --search-all --threads 1 --log /tmp/r2.json /tmp/m.bin && python3 -c "import json;print(json.load(open('/tmp/r2.json'))[0]['Analysis']['file_map'])"

# M33 fix able to fail (mutate copies in /tmp only)
git archive HEAD corpus | tar -x -C /tmp/tree && cp /tmp/tree/corpus/live/runs/round-63/inspection.json /tmp/mut.json
python3 - <<'EOF'
import json
d=json.load(open('/tmp/mut.json')); d['normalized_result']['regions'][0]['offset']=513
json.dump(d,open('/tmp/mut.json','w'))
EOF
python3 -B /tmp/tree/corpus/live/runs/round-63/oracle_check.py --record /tmp/mut.json; echo "exit=$?"

# M35 green-after-deletion
cp /tmp/tree/corpus/verify_icon_states.py /tmp/v.py   # then delete the stdout_sha256 assert
cd /tmp/tree/corpus && python3 -B verify_icon_states.py --self-test; echo "exit=$?"

# routed debt (a) source line
python3 -c "l=open('corpus/lessons/round-62-verifier-spotcheck.md').read().split(chr(10))[62]; print('commit the resume re-verification output alongside the report claim' in l)"
```

---

## Summary for the canonical judge

- **Verdict: NOT CONFORMANT.** Three gaps, one of them a live intra-file
  contradiction at the final tip.
- **Gap 1 (coverage):** `## Gate` records for the newly-landed **S033** and
  **S035** carry no located ≤25-word quote (contract rule 1 requires one for
  every new row; the round-62 lesson met this for its own-work rows S030/S031).
  S032 and S034 are complete and every one of their ten quotes re-verifies
  verbatim against the pinned snapshot, with a live re-fetch confirming the
  snapshot digest.
- **Gap 2 (calibration):** `## Mistakes` **M34**'s `fix / falsifiable
  demonstration` cell names no command, expected output, or observable failing
  state — it is a reporting policy, so the counter-substitution mistake has no
  runnable falsifier.
- **Gap 3 (calibration):** `## Search log` reports `included 1 row (S032)` while
  **four** rows are landed at the tip; **S034 and S035 appear in neither search
  log**, and the lesson's id-allocation paragraph still says the round's ids are
  "the contiguous pair S032 + S033 with no id skipped" and that S034 was
  "withdrawn" — in the same commit that landed S034/S035 and added their Gate
  records.
- **Routed debt (a) ✔** is named, quoted verbatim from
  `corpus/lessons/round-62-verifier-spotcheck.md:63`, and dispositioned
  **Honored**; the discharge (`reports/round-63/measure-after.log`) is still
  outstanding at the tip and is L1's to land with the report claim.
- **M33's fix is shown able to fail ✔** — the red-before command is the
  `binwalk` 3.1.0 signature scan, whose observed failure I reproduced (zero
  regions in the 1056-byte uImage-header image, under both the default and
  `--search-all` scans), and the committed oracle's three promised MISMATCH
  outputs I re-ran and matched exactly.
- **M35's evidence ✔** re-verified by execution: deleting the `stdout_sha256`
  conjunct leaves `verify_icon_states.py --self-test` green with exit 0 and
  the exact recorded PASS line; the `aaa0463` widening to two unguarded
  conjuncts (one per script) also re-verifies on committed bytes.
