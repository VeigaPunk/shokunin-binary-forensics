# W2AttackEntryQ11 — Q11 attack on the C1 entry (committed bytes)

Seat: `revenger-r63.W2AttackEntryQ11` (independent leaf, no dispatch). Axis: coverage.
Attack surface: `corpus/knowledge/round-63-zip-central-directory-evidence.md` at lane tip
`db55bd6488e24e956df5818ae34c2a043d7ddc12` (`git rev-parse HEAD` = `git rev-parse main` = `db55bd6`),
`corpus/QUALITY.md` Q11, and the H1–H7 corrections claimed in the integration commit message.
Everything below was re-run by me from `/home/vgpnk/Projects/shokunin/revenger-shokunin`.

## Verdict

**Q11 FAIL as committed.** One printed command output is false (a word count), and two
source-metadata values (one digest, one version/status/date tuple) carry no in-entry command+output
while the entry's own inventory claims *every* factual sentence maps to one. Every other value
— all 17 `--fact` outputs in both places they appear, the stdout/script/snapshot measurements, the
base-commit and working-tree hashes, and 9 of 10 word counts — reproduces exactly.

Smallest correction to clear the hard failure: `entry:292` `8` → `7`.

## Method (what I attacked, with what)

1. Extracted the `### Code` block from the committed entry bytes (not from my read of it) to
   `/tmp/revenger-r63-q11/readout.py`; extracted every line beginning `{"fact":` from the same bytes.
2. Ran `python3 -B /tmp/revenger-r63-q11/readout.py .` from the lane root and compared, line-for-line,
   every embedded fact line against the run (34 embedded lines = 17 facts × 2 occurrences: per-item
   block + full stdout block).
3. Re-ran each non-fact command in §Reproduce and items 1–2, and independently re-decoded the archive
   with my own `struct`/`zlib` reader before trusting any printed value.
4. Re-opened the saved record's literal fields and the APPNOTE snapshot directly.

## Hard failure (Q11 value with a false printed output)

### F1 — HIGH — word count printed as 8, actual 7 (entry:291–292)

```
$ sed -n '291,292p' corpus/knowledge/round-63-zip-central-directory-evidence.md
$ printf '%s\n' "local file header signature 4 bytes (0x04034b50)" | wc -w
8
$ printf '%s\n' "local file header signature 4 bytes (0x04034b50)" | wc -w
7
```

The entry prints `8` for a command whose actual output is `7` (`local file header signature 4 bytes
(0x04034b50)` = 7 whitespace-separated words). This is the Q11 failure mode in its purest form: the
entry carries the command, and the output beside it is not that command's output. It also makes the
inventory row `S1` (entry:684, "the ten §Sources quotes and their word counts") print a false output.
The separate claim that every quote is ≤ 25 words is unaffected (7 ≤ 25; max actual count is 24).

The other nine counts reproduce exactly. My independent run of all ten, in §Sources order:

| quote | entry says | actual `wc -w` | verdict |
|---|---|---|---|
| central file header signature … | 7 | 7 | PASS |
| crc-32 4 bytes … | 21 | 21 | PASS |
| local file header signature … | **8** | **7** | **FAIL** |
| file name length 2 bytes … | 10 | 10 | PASS |
| end of central dir signature … | 8 | 8 | PASS |
| total number of entries … | 23 | 23 | PASS |
| This is the offset from the start … | 24 | 24 | PASS |
| All values MUST be stored … | 20 | 20 | PASS |
| If bit 3 … | 23 | 23 | PASS |
| value is put … | 12 | 12 | PASS |

## Q11 gaps that survive the H1–H7 corrections

### F2 — MEDIUM — §Sources digest with no in-entry derivation (entry:657)

The excluded page's snapshot digest is printed:

```
$ grep -n '9520a8cb' corpus/knowledge/round-63-zip-central-directory-evidence.md
657: … The excluded page's own snapshot is `.ufo/waves/round-63/source-snapshots/zipfile.html` (sha256 `9520a8cbce7d3c8b7ea6704f60ac1122856da14d1bdc4161075912303a270739`, accessed 2026-10-23); it is not cited as support for any claim.
```

No command anywhere in the entry prints this digest; §Reproduce measures only `appnote.txt`,
`readout.stdout.txt` and `readout.py`. It is not labeled *recorded*. Q11 enumerates digests without
carving out non-load-bearing ones. The value itself is correct:

```
$ sha256sum .ufo/waves/round-63/source-snapshots/zipfile.html
9520a8cbce7d3c8b7ea6704f60ac1122856da14d1bdc4161075912303a270739  .ufo/waves/round-63/source-snapshots/zipfile.html
```

So this is a derivation gap, not a wrong value — exactly Q11's first failure clause. Fix: add the
`sha256sum`+`wc -c` output for that file to §Reproduce, or label the value recorded.

### F3 — MEDIUM — the inventory's completeness claim is false (entry:661, entry:707)

```
$ sed -n '661p' corpus/knowledge/round-63-zip-central-directory-evidence.md
Every factual sentence above maps to a command that prints it and to the output that command printed. …
$ sed -n '707p' … | cut -c1-120
| Q11 | pass | the §Sentence-to-output inventory maps every factual sentence, including the header, source and run-metadata rows, to a command …
```

Two §Sources facts are not in the table at all: the S032 version/status/revised tuple and the
`zipfile.html` digest (F2). The table's own `S1` row also carries F1's false output. The Q11 "pass"
decision is therefore contradicted by the table it cites.

### F4 — LOW — S032 version/status/date tuple underived (entry:1, entry:644)

"Version 6.3.10, status FINAL, revised Nov 01 2022" is an identifier+date sentence with no command
and no output in the entry. The values are true in the snapshot, which I opened directly:

```
$ sed -n '1,4p' .ufo/waves/round-63/source-snapshots/appnote.txt
File:    APPNOTE.TXT - .ZIP File Format Specification
Version: 6.3.10 
Status: FINAL - replaces version 6.3.9
Revised: Nov 01, 2022
```

No `grep`/`sed` command printing these lines is carried in-entry, and the inventory does not map the
sentence. Low severity because it is source metadata, not a fixture value; still in Q11's enumeration
(identifier) and covered by the inventory's own completeness claim (F3).

### F5 — LOW — negative oracle-field claim is underived (entry:155/156, item 11)

"The oracle records no CRC-32, no EOCD location, no central-directory offset or size and no
local-header offsets" is a factual statement about `truth.json`'s key set with no command printing
that key set. I verified it is true (`truth.json` keys: `source_binary_sha256`, `archive_sha256`,
`archive_size`, `members[path,size,sha256,compressed_size]`, `build`), so this is a derivation gap,
not an error. A one-line `python3 -c 'import json;print(sorted(json.load(open("…/truth.json"))))'`
with its output would close it.

### F6 — LOW — `readout.stdout.txt` command names an unshipped file (entry:260–263)

`wc -l readout.stdout.txt` / `sha256sum readout.stdout.txt` reference a file the entry does not
provide; the reader must first save the printed block under that name. The outputs are correct — I
regenerated the file from a fresh run and got exactly:

```
$ wc -l readout.stdout.txt   → 17 readout.stdout.txt
$ sha256sum readout.stdout.txt → 02b0f495c1db8c50e22db835cd57e7a221dd0a9c82f09d442feea461de722ed4
```

So the value reproduces; only the command's prerequisite is unstated. Fix: say "save the block above
as readout.stdout.txt", or measure a pipe (`python3 -B readout.py . | tee …`).

### F7 — LOW/INFO — item 13's sentence is truncated in the committed bytes (entry:155)

The line ends with a literal `…`: "…but this entry does not establish who produced the record, that
it is…". No value is lost (the recorded-fields clause and the `saved_record` fact are complete), but
a truncated sentence in a committed knowledge entry is a defect worth fixing in the same pass.

### F8 — LOW/INFO — item 5's "every field offset used below is computed" is true of the quoted offsets, not of the parser

`entry:67` says every field offset "used below" is computed by summing APPNOTE widths. The
central-directory and EOCD parse loops still use literal offsets (`pos+16`, `pos+28`, `pos+42`,
`eocd_off+12`, …); the computed offsets are used for the local-header name/extra reads and for the
`spec_derived_field_offsets` verification block, which proves the literals equal the computed offsets
(`per_member_offset_checks`, `eocd_fixed_part_equals_observed_record_length`). I do **not** score this
as a Q11 failure — the offsets the entry prints are all in the fact output and each literal is
cross-checked — but the prose is stronger than the code. Precise wording: "every field offset printed
below is computed; the parser's literals are verified against them."

## Per-value Q11 verdicts (attacks, not restatements)

| Value(s) | Derivation carried? | Output reproduces? | Q11 |
|---|---|---|---|
| item 1 archive 2964 / `857989f5…` | `--fact 'archive'` | yes (byte-identical) | PASS |
| item 2 four files at base `55bcb6e1…` + working tree | `git show`×4 + `sha256sum`×4 | yes, all 8 hashes identical to mine | PASS |
| item 3 EOCD 2942/22/`504b0506`/0,0/2,2/114/2828/0 | `--fact 'eocd'` | yes | PASS |
| item 4 CD [2828,2942), inclusive [2828,2941], 2 entries | `--fact 'central_directory'` | yes (inclusive range now printed — H3 real) | PASS |
| item 5 fixed 30/46/22 + computed offsets + signature checks | `--fact 'spec_derived_field_offsets'` | yes (3506-char line byte-identical; H1 real) | PASS |
| items 6–7 CD records (names, offsets, sizes, CRC, lengths) | `--fact 'member_cd[…]'` ×2 | yes; independently decoded same values | PASS |
| items 8–9 local headers, payload offsets 42/2750, inflated sizes/digests/CRC | `--fact 'member_local[…]'` ×2 | yes; independently inflated same digests | PASS |
| item 10 oracle archive digest/size | `--fact 'truth_archive_level'` | yes | PASS |
| item 11 oracle member fields | `--fact 'truth_member[…]'` ×2 | yes | PASS (negative claim F5 noted) |
| item 12 name-set delta | `--fact 'truth_member_set_delta'` | yes | PASS |
| RP recorded build string | `--fact 'truth_build_field'` | yes, labeled recorded | PASS |
| item 13 record 7692/`2fec924b…`/IDs/3 occurrences | `--fact 'saved_record'` | yes; record keys independently re-read (all 6 IDs/fields match) | PASS |
| items 14–15 occurrence/node fields | `--fact 'saved_occurrence[…]'` ×2 | yes; independent re-read matches | PASS |
| item 16 paths `.`/`README.txt`/`bin/checksum` | `--fact 'saved_occurrence_set_delta'` | yes | PASS |
| §Reproduce 17 lines / `02b0f495…` | `wc -l`, `sha256sum` on regenerated stdout | yes (17, exact digest) | PASS (prereq F6) |
| §Reproduce script 328 lines / `94f502cd…` | `wc -l`, `sha256sum` | yes — extracted block is 328 lines, exact digest | PASS |
| §Reproduce snapshot 174585 / `0b993022…` | `wc -c`, `sha256sum` | yes | PASS |
| §Sources 10 word counts | `printf | wc -w` ×10 | 9/10 | **FAIL (F1)** |
| §Sources zipfile.html digest | none | correct but underived | **FAIL (F2)** |
| §Sources S032 version/FINAL/date | none | true but underived | **FAIL (F4)** |
| `rea-agents@6.4.0` (item 29, Q04 row) | none | labeled recorded, credited with nothing | PASS by Q11's recorded clause; residual (no `grep`+output from LEDGER.md) |

## H1–H7 correction verification (each attacked against committed bytes)

- **H1 (local-header constants assumed)** — REAL. `local_header_fixed_part_bytes:30` and offsets
  26/28 are computed from `LFH_FIELDS` and used for the name/extra reads; `per_member_offset_checks`
  proves CD literals equal computed offsets. Caveat F8 (wording).
- **H2 (snapshot/stdout metadata without commands)** — REAL for the three measurements (all reproduce);
  caveat F6 (stdout file not shipped).
- **H3 (inclusive 2941 not printed)** — REAL: `"cd_byte_range_inclusive":[2828,2941]` is in the
  `central_directory` output.
- **H4 (working-tree truth.json hash missing)** — REAL: item 2's second block lists all four working-tree
  hashes, including `7df773bf…` for `truth.json`; I re-ran it.
- **H5 (ZIP64 absence without sweep)** — REAL: the entry now only says ZIP64 is outside scope and no
  record of it is read (`entry:221`, `entry:655`); it asserts neither presence nor absence. No sweep
  needed because no absence claim is made.
- **H6 ("every field" overclaim)** — PARTIAL. Item 11's per-field scoping is corrected, but the
  inventory's "Every factual sentence above maps to a command" (`entry:661`) and the Q11 pass row
  (`entry:707`) still overclaim: F2 and F4 are unmapped, and S1's output is wrong (F1).
- **H7 (trailing-bytes scope conflict)** — REAL: item 22 ("neither confirms nor denies that boundary")
  and item 26 ("nothing is claimed about any region … records do not describe") are consistent; no
  trailing-bytes claim survives.

## Independent decode (so the printed values are checked, not merely reproduced)

My own reader (no `zipfile`) on `corpus/fixtures/archive-r2/fixture.zip`:

```
len 2964 sha 857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e
eocd 2942 22 504b0506 ; disks 0 0 counts 2 2 cdsize 114 cdoff 2828 clen 0
cd 2828 bin/checksum crc 3017776807 cs 2668 us 16160 lho 0 nl 12
cd 2886 README.txt   crc 1923438513 cs 78   us 84   lho 2710 nl 10
lfh 0    504b0304 bin/checksum dataoff 42   infl 16160 f5ba0697… b3df9ea7
lfh 2710 504b0304 README.txt   dataoff 2750 infl 84    7d8f6a8d… 72a557b1
```

Every derived number in items 1–9 matches. `truth.json` (728 bytes) and the saved record (7692 bytes)
literal fields match items 10–16 and item 13 respectively.

## Residual risk

- If only `entry:292` is fixed, Q11 still fails on F2/F4 unless those values get a command+output or a
  recorded label — the entry's own inventory claim (F3) makes the gap self-incriminating.
- The `rea-agents@6.4.0` identifier is compliant only because item 29 labels it recorded; if a later
  edit presents it as verified, Q11 breaks.
- The word-count block is the only place where a printed output is wrong; because it sits inside the
  §Sources word-count evidence, a reader who trusts the block would carry a false count forward.

## Verification gaps / notes

- No tool installs were needed or performed (no pacman, no uv/npx/cargo); no network used; no target
  execution; no model arguments; no writes outside this report and `/tmp/revenger-r63-q11`.
- Lane tip attacked: `db55bd6` (equals `main`); build state `2a34e45` not separately re-read because
  all fixture/record bytes were hash-verified against base `55bcb6e1…` and the working tree.
- `corpus/live` and `corpus/fixtures` outside round-63 paths were only read (hashes unchanged by me).

---

# Re-review — corrected bytes at lane tip `aaa046326d92ba983f3ae99341438c9b8509a6cc`

Exact hash attacked (verified twice, working tree and `git show <tip>:<path>`):

```
$ sha256sum corpus/knowledge/round-63-zip-central-directory-evidence.md
285f641f4774a35f663c7ace731839e789c24d028cab1f455078df60fc9e56a1  corpus/knowledge/round-63-zip-central-directory-evidence.md
$ git show aaa046326d92ba983f3ae99341438c9b8509a6cc:corpus/knowledge/round-63-zip-central-directory-evidence.md | sha256sum
285f641f4774a35f663c7ace731839e789c24d028cab1f455078df60fc9e56a1  -
```

(`git rev-parse HEAD` = `git rev-parse main` = `aaa046326d92ba983f3ae99341438c9b8509a6cc`.)

## Re-review verdict: **Q11 FAIL** — one value remains underived

Every previously failing value is fixed and every printed block reproduces; one count still lacks
an in-entry command+output:

### R1 — MEDIUM (Q11 value) — LEDGER.md's `3959 bytes` is underived (entry:4, entry:681)

`grep -n '3959'` finds only the two source-row statements, never a command output. The readout has no
ledger reference (17 facts, none about the ledger), and §Reproduce prints `sha256sum` for the ledger
but no `wc -c`. The value is a count, it is correct (I measured `wc -c corpus/live/runs/20261012T164246Z/LEDGER.md`
→ `3959`), it carries no `wc -c` command+output, and it is not labeled *recorded*. Q11's first clause
is unconditional for counts. This is the same class as the H2/H4 holes, in the one file the H4 fix
did not cover.

The new Derived/Recorded split (entry:686) also overstates: its Derived clause says the
file-measurement commands' outputs are printed in §Reproduce "for the script, the stdout, the APPNOTE
snapshot, the zipfile snapshot and the fixture/oracle/record/ledger files", but no `wc -c`/`wc -l` for
the ledger (or the fixture/oracle/record) appears there; those byte counts come from the `archive` and
`saved_record` facts, and the ledger's does not appear anywhere. The Q11 decision row (entry:732) still
claims the inventory maps every factual sentence "including ... source and run-metadata rows".

Smallest correction: add one block to §Reproduce (or item 2) —
`$ wc -c corpus/live/runs/20261012T164246Z/LEDGER.md` / `3959 corpus/live/runs/20261012T164246Z/LEDGER.md`
— or delete `, 3959 bytes` from the S035 row. Both are one-line changes; the second removes the last
unmapped count entirely.

## Corrections verified real at `aaa0463` (my re-runs, not the author's)

| Correction | Evidence | Verdict |
|---|---|---|
| wc -w 8→7 | entry:312–314 prints `7`; I reran all ten `printf \| wc -w`: 7,21,7,10,8,23,24,20,23,12 — every printed count matches | **FIXED** |
| zipfile.html digest derived | entry:288–291 `wc -c`→139782, `sha256sum`→`9520a8cb…`; I reran both, exact match | **FIXED** |
| APPNOTE revision facts derived | entry:299–303 `tr -d '\r' < appnote.txt \| head -5`; I reran it — output is byte-identical to the block, including the trailing space on `Version: 6.3.10 ` | **FIXED** |
| stdout prereq | entry:262–265 now generates and measures in one command (`> readout.stdout.txt && wc -l && sha256sum`); fresh run → 17 lines, `ccaffa322c49d1850fb7da86dc9221ea3bd73c8e3db81cc2ce9be6a1e5b40dc5` | **FIXED** |
| script measurement | entry:269–272 `8dbefe4d…`, 329 lines; extracted block has exactly that sha256 and line count | **FIXED/current** |
| S034/S035 rows | S032 narrowed; S034 (§4.3.7) and S035 (ledger) rows landed; S033 narrowed to fixture/oracle/record; snapshot digests/size shared and printed by the appnote block | **FIXED** (except R1's size) |
| item 13 truncation | line 157's only `…` is the legitimate `npx -y rea-agents@6.4.0 inspect-artifact …` command elision; the sentence now ends cleanly | **FIXED** |
| inventory universal claim | replaced by the Derived/Recorded split (entry:686) | **PARTIAL** — split itself overstates ledger measurement (R1) |

Full readout re-run: 34 embedded fact lines (17 facts × 2 placements) compare byte-identical to the
fresh run; zero mismatches, zero missing ids. Word counts, base-commit and working-tree hashes, and the
snapshot/script/stdout measurements all reproduce.

## Prose defects found outside the Q11 value set (reported for the C1 owner, not scored as Q11 fails)

- **entry:680** — literal template placeholders in the committed §Sources prose:
  `({{R:spec_offsets}}, {{R:local_member_1}}, {{R:local_member_2}})`. These are unresolved citation
  markers, not prose; they should be replaced with the item numbers or removed.
- **entry:682** — "No third source is cited." after §Sources now lists four rows (S032, S034, S033,
  S035). The intended meaning (no third *external document*: S034 is the same APPNOTE, S035 is own-work)
  is not what the sentence says; it is literally false. Reword to "No source beyond the APPNOTE
  document and this lane's own artifacts is cited."

These do not enter the Q11 per-value verdict, but they are factual-sentence defects in an entry whose
Q11 inventory claims every factual sentence is mapped.

## Residual Q11 notes (unchanged, low)

- Item 11's negative oracle-field claim ("The oracle records no CRC-32, no EOCD location, …") still has
  no command printing `truth.json`'s key set; I verified the claim is true (keys: `source_binary_sha256`,
  `archive_sha256`, `archive_size`, `members[path,size,sha256,compressed_size]`, `build`).
- `rea-agents@6.4.0` is cited from the ledger and labeled as a recorded invocation; Q11's recorded
  clause covers it.

## Bottom line

At `aaa0463` / entry `285f641f…`: **Q11 FAIL per value — exactly one value (LEDGER.md `3959 bytes`,
entry:4/681)**; all other counts, identifiers, offsets and digests now carry a reproducing command and
output. The C1 Q11 pass cannot be recommended until that count is printed by a command or removed.

---

# Final confirm — lane tip `3af3acbab51ab38c929d6d81524e07ded70dec44`, entry sha256 `4ece6cfb980f834b6dcf5fe2fc9bf4de8436a3f50ea5081d829182b5e6d8027c`

Exact hash confirmed both ways (`git rev-parse HEAD` = `git rev-parse main` = `3af3acb`;
`sha256sum <path>` and `git show 3af3acb:<path> | sha256sum` both `4ece6cfb…`).

## Verdict: **Q11 PASS** on this exact hash — every count, identifier, offset and digest now carries a reproducing command+output or a recorded label.

The one remaining value from the previous round is closed at the source row itself:

```
$ wc -c < corpus/live/runs/20261012T164246Z/LEDGER.md
3959
$ sha256sum corpus/live/runs/20261012T164246Z/LEDGER.md
05042a555f91511c9c191565d92f83527f54d1c9b14de331587f4cbffff9e6cb  corpus/live/runs/20261012T164246Z/LEDGER.md
```

Entry:681 prints exactly those two commands and outputs (`wc -c < …` → `3959`). Re-run at
`3af3acb`: identical. The header row's `3959 bytes` (entry:4) is the same value, derived in the same
entry at entry:681 — Q11's "inside the entry" is satisfied.

## Checks run on this hash

| Check | Result |
|---|---|
| entry sha256 (tree and `git show 3af3acb:`) | `4ece6cfb…` / `4ece6cfb…` — match |
| readout stdout | 17 lines, `ccaffa322c49d1850fb7da86dc9221ea3bd73c8e3db81cc2ce9be6a1e5b40dc5` — matches entry:237/264 |
| script | 329 lines, `8dbefe4dae2fd170d4bd658c4d1111e66a15b266687fe586e385d9aab74c367f` — matches entry:271 |
| embedded fact lines vs fresh run | 34/34 byte-identical (17 facts × 2 placements), 0 missing, 0 unparseable |
| ten `wc -w` spot | 7,21,7,10,8,23,24,20,23,12 — matches entry:308–327 (the old `8` is gone) |
| `{{R:` tokens | 0 in the committed bytes |
| "No fifth source" | entry:682 now says "No fifth source is cited: S032, S033, S034 and S035 above are this entry's complete registry basis." — consistent with the four rows |
| APPNOTE / zipfile measurements | `0b993022…`/174585 and `9520a8cb…`/139782 still match the files I hashed |
| base-commit + working-tree hashes | four `git show` + four-path `sha256sum` outputs still match (ledger `05042a…` unchanged across `aaa0463`→`3af3acb`) |

## Residual notes (non-blocking, no Q11 value affected)

- Entry:681's parenthetical says the ledger commands were "run 2026-10-24 at the aaa0463 tip"; the
  entry now sits at `3af3acb`. I re-ran both commands at `3af3acb` and got identical output, and the
  ledger hash is unchanged across the two commits, so the value reproduces at the tip. A future edit
  could drop the stale tip reference or restate it as "run at aaa0463; ledger bytes unchanged at the
  entry tip".
- `npx -y rea-agents@6.4.0` (entry:681/item 29) has no `grep`+output from the ledger, but it is
  presented as the ledger's recorded invocation and credited with nothing derived, so Q11's recorded
  clause covers it.

**Recommendation: C1 Q11 PASS at entry `4ece6cfb…` (tip `3af3acb`).** No actionable Q11 finding remains.

---

# Transition confirm — lane tip `34cfa2435a424541d09a95c88cbdca2eb9ebe33b`, entry sha256 `854e33d78034e8d53ca68e813cab2394a1bc9a38770c9b47ee1bf0dc07a1a0d7`

Hash confirmed both ways (`sha256sum <path>` and `git show 34cfa243:<path> | sha256sum` → `854e33d7…`;
`HEAD` = `main` = `34cfa243`). Diff from my PASSed hash (`3af3acb`/`4ece6cfb…`) is **exactly 2 changed
lines, 4 column-line insertions/deletions, all in the two embedded registry-row copies**: `| queued |`
→ `| mined |` at the S034 copy (entry:680) and the S035 copy (entry:681). No derivation, value, quote
or fact line changed: 34/34 embedded fact lines remain byte-identical to a fresh run, stdout is still
`ccaffa32…`/17 lines, script still `8dbefe4d…`/329, the ledger `wc -c <` → `3959` derivation and its
sha256 are intact, and `{{R:` count is 0. **Q11 PASS carries forward to entry `854e33d7…` (tip `34cfa243`).**

One delta discrepancy, outside Q11's value set and filed for the registry/bookkeeping owner: the
transition message says the copies flipped to "`mined`/used-by entry path with a landed-state note",
but the diff only changed the status token. Both copies still show `used-by` as `—` and still carry
the stale trailing instruction "(flip to `mined` with this entry's path in `used-by` when the entry
lands, logged old→new in the round lesson)" even though the row now reads `mined`. The S033 embedded
copy (entry:676) still reads `| queued | … | — |`, while the authoritative `corpus/SOURCES.md` lines
46–49 show all four rows (`S032`, `S033`, `S034`, `S035`) as `mined` with `corpus/knowledge/round-63-zip-central-directory-evidence.md`
in `used-by`. This is a landed-state/copy-sync defect, not a Q11 derivation defect; Q11's PASS is
unaffected because none of the changed text derives any value.

