# ScoutReopen — round 97 wave w1 (frontier duty §2b.4)

Seat: ScoutReopen. Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.
Lane commit (claims frozen): `3b4b4e5c1d123d5fc5337ad59015b4752366854a`.
Base snapshot used for row counting: `7d380ce2c75d3dfd24dfb7759d04f207eeeb1a68`.

Scope: re-open the source rows C1 rests on (S502, S503, S504) and check each located quote
byte-for-byte. **Read-only: no corpus file was edited.** No git/jj mutation was run; only read-only
git (`git show`, `git grep`, `git archive` recipe not needed) was used.

Scratch root (deleted before yield): `/fast/scratch/hyaku/revenger-r97/ScoutReopen/`.
Bodies were fetched there, hashed, then deleted with the scratch dir; only sha256 values are cited.
No tool was installed or upgraded this seat (nothing needed beyond `curl`, `grep`, `sha256sum`,
`python3`, `git` — all preinstalled).

---

## 1. Re-opened source rows — table

| S-id | URL (pinned, `source` cell) | HTTP | bytes | sha256 | access date | located quote (verbatim, as recorded in `corpus/lessons/round-96.md` `## Gate`) | grep count | verdict |
|---|---|---|---|---|---|---|---|---|
| S502 | `https://raw.githubusercontent.com/morluto/rea/12f6e0974cc0db0b3a9b86246accc76556837222/.agents/skills/reverse-engineer-anything/references/native-and-artifacts.md` | 200 | 38167 | `c818ee342477a2b1bf613f8b2074f284298edd5ab989ac15f97f728de563cc24` | 2026-11-05 | `` `rea decompile <path> --file-offset=0x... --provider ghidra` resolves the source byte offset internally `` (12 words) | 1 | **verified** — byte-identical to the committed r96 body (`cmp` exit 0); quote present verbatim |
| S503 | `https://raw.githubusercontent.com/morluto/rea/12f6e0974cc0db0b3a9b86246accc76556837222/.agents/skills/reverse-engineer-anything/SKILL.md` | 200 | 35095 | `b5f17fdff254804c723c8fa34a5b51180569e117437cddc7305dba2c59796ccc` | 2026-11-05 | `Use shipped-artifact or requested runtime evidence to explain features, compare versions, decompile code, or guide a reconstruction.` (17 words) | 1 | **verified** — byte-identical to the committed r96 body (`cmp` exit 0); quote present verbatim |
| S504 | own-work: `corpus/live/runs/round-96/` | n/a (local) | `codeable-decompiled.c` = 170 bytes, sha256 `d717b49156faa1a627a5577a35ab7c158b103bd6adf31ee7ab5428abae3afc9d` | same | 2026-11-05 | lesson quote `undefined8 entry(void) { return 0x2a; }` — **ABSENT** (count 0) | **0** | **FAILED as recorded** — the recorded one-liner is a whitespace-reflowed rendering, not byte-verbatim. Replacement quote supplied in §3. |

Both HTTP fetches returned 200 on the first attempt; no retry was needed. Neither fetch failed, and
no source row was repaired. Neither S502 nor S503 quote is defective.

---

## 2. Exact commands and exit codes

All commands were run from the lane (read-only) or from the seat scratch root.

### 2.1 Row location
```
$ grep -n '| S50[234] |' corpus/SOURCES.md
519:| S502 | …
520:| S503 | …
521:| S504 | …
exit=0
```
(`corpus/SOURCES.md` lines 519–521; each row has 11 cells; the `source` cell is cell 1, the
quote/anchor cell is cell 5, the used-by cell is cell 10 = `corpus/knowledge/round-96-native-analysis-sessions.md`
for all three rows — used by the candidate entry exactly once per row, the exclusivity leg's input.)

### 2.2 Fetches (S502, S503)
```
$ curl -sSL -o $S/S502.body -w '%{http_code}\n' 'https://raw.githubusercontent.com/morluto/rea/12f6e0974cc0db0b3a9b86246accc76556837222/.agents/skills/reverse-engineer-anything/references/native-and-artifacts.md'
200
exit=0
$ curl -sSL -o $S/S503.body -w '%{http_code}\n' 'https://raw.githubusercontent.com/morluto/rea/12f6e0974cc0db0b3a9b86246accc76556837222/.agents/skills/reverse-engineer-anything/SKILL.md'
200
exit=0
$ sha256sum S502.body S503.body
c818ee342477a2b1bf613f8b2074f284298edd5ab989ac15f97f728de563cc24  S502.body
b5f17fdff254804c723c8fa34a5b51180569e117437cddc7305dba2c59796ccc  S503.body
$ wc -c S502.body S503.body
38167 S502.body
35095 S503.body
$ date -I
2026-11-05
exit=0
```
Both sha256 values equal the values recorded in `corpus/SOURCES.md` (S502/S503 cells) and in the
committed r96 receipts (`reports/round-96/quote-receipts/S50{2,3}.receipt.json`:
`fetch_sha256` c818ee34… / b5f17fdf…, `length` 38167 / 35095, `http_status` 200,
`fetched_at` 2026-11-05). No drift at the pinned revision.

Byte-identity against the committed r96 raw bodies (re-fetch vs committed):
```
$ cmp $S/S502.body reports/round-96/quote-receipts/raw/S502.body   → exit 0
$ cmp $S/S503.body reports/round-96/quote-receipts/raw/S503.body   → exit 0
```

### 2.3 Quote presence — S502 / S503
```
$ grep -c -F '`rea decompile <path> --file-offset=0x... --provider ghidra` resolves the source byte offset internally' S502.body
1
exit=0
$ grep -c -F 'Use shipped-artifact or requested runtime evidence to explain features, compare versions, decompile code, or guide a reconstruction.' S503.body
1
exit=0
$ grep -o -F '<S502 quote>' S502.body | wc -w   → 12   (exit 0)
$ grep -o -F '<S503 quote>' S503.body | wc -w   → 17   (exit 0)
```
Word counts match the lesson's recorded counts (12 and 17) and are ≤25 as the row contract requires.
Anchors named in the rows also hold: `grep -c -F 'DOS MZ with Ghidra' S502.body` → 1 (exit 0);
`grep -c -F 'Use shipped-artifact or requested runtime evidence' S503.body` → 1 (exit 0).

Byte-span reconciliation (byte offsets vs the r96 receipt's character offsets):
- S502 lesson quote: 1-based **bytes 26311–26413** (103 bytes, incl. both backticks).
  The committed receipt stores the quote *without* the leading backtick
  (`"rea decompile … ghidra\` resolves the source byte offset internally"`) at **character** span
  26309–26411; `text[26309:26411] == receipt.quote` → True (the audit script slices *decoded text*,
  `corpus/audit_source_quotes.py:103-107`, so its spans are character offsets; the S502 body is
  38167 bytes / 38165 chars — 2 bytes of multibyte UTF-8 explain the offset delta).
  The receipt's own `norm(body[span]) == norm(quote)` check passes → **the r96 receipt is internally
  consistent**; the leading backtick is carried by the *lesson* quote, not by the receipt.
- S503 lesson quote: 1-based bytes 258–389 (132 bytes) = receipt character span 257–389. Consistent.

### 2.4 S504 own-work record — quote presence and defect D1
```
$ grep -c -F 'undefined8 entry(void) { return 0x2a; }' corpus/live/runs/round-96/codeable-decompiled.c
0
exit=1        ← ABSENT (grep exit 1 = no match)
$ git grep -c -F 'entry(void) { return 0x2a; }' 66cb784 -- corpus/live/runs/round-96
(no output)
exit=1        ← reproduces the r96 spot-check's D1 evidence at the r96 commit
```
File facts: `corpus/live/runs/round-96/codeable-decompiled.c`, 170 bytes, 14 lines,
sha256 `d717b49156faa1a627a5577a35ab7c158b103bd6adf31ee7ab5428abae3afc9d`.
Bytes 1–14 of the entry block (`od -c` verified): `undefined8 entry(void)\n\n{\n  return 0x2a;\n}`.

### 2.5 Evidence ID
```
$ grep -c -F 'ev_cc0b9d88200afef1e7bf90e77f4d52faa20a049f85f1db1a7bf4a531282ffefe' corpus/live/runs/round-96/rea-decompile.raw.txt
1
exit=0
```
It is on **line 1** (`evidence_id: ev_cc0b9d88…`). The same ID is **not** in
`ghidra-headless-r96.log` (count 0) nor in `rea-doctor-r96.txt` (count 0) — expected, those are
provider receipts, not the session record. The Evidence's `normalized_result` (raw.txt line 61)
carries the same multi-line body, so the entry body is independently attested by the raw receipt:
`normalized_result: "\nundefined8 entry(void)\n\n{\n  return 0x2a;\n}\n\n"`.

### 2.6 Base S5xx row count
```
$ git -C /home/vgpnk/Projects/shokunin/revenger-shokunin show 7d380ce:corpus/SOURCES.md | grep -c '^| S5'
5
exit=0
```
The five base S5xx rows are S500, S501, S502, S503, S504 (`git show 7d380ce:corpus/SOURCES.md | grep -o '^| S5[0-9]*'`
→ `| S500 | S501 | S502 | S503 | S504`). The lane worktree carries the identical set
(`grep -c '^| S50[234] |' corpus/SOURCES.md` → 3; `grep -c '^| S5' corpus/SOURCES.md` → 5).
**S502/S503/S504 are present at the base commit — the base count of 5 already includes them.**
This matters for C1: the three rows C1 rests on are not a post-freeze addition to the registry.

---

## 3. Replacement quote for defect D1 (round-96 spot-check, item 3)

D1 (routed in `corpus/lessons/round-96-verifier-spotcheck.md` §5, item 3 / §4 row 3) is **confirmed
live**: the S504 located quote in `corpus/lessons/round-96.md` `## Gate` (line 48) is
`undefined8 entry(void) { return 0x2a; }` with the descriptor "entry block, 3 lines" — that string is
**not present** in the saved bytes (grep count 0, exit 1), and the saved entry block is **5 lines**,
not 3 (line 7 is blank). The r96 spot-check is correct on both points.

**Smallest byte-verbatim span containing `return 0x2a;`** in `codeable-decompiled.c`:

- Byte range **129–140** (1-based, inclusive), 12 bytes: `return 0x2a;` — line 9, token only.
  The whole line including its two-space indent is bytes **127–140**: `  return 0x2a;` (14 bytes).

**Recommended replacement quote** (byte-verbatim, ≤25 words, carries the function shape the old
one-liner tried to convey) — `codeable-decompiled.c` **lines 6–10**, 1-based bytes **101–142**
(42 bytes, 6 whitespace-separated words):

```
undefined8 entry(void)

{
  return 0x2a;
}
```

Verbatim-presence proof for the recommended span (`bytes.count(span) == 1`), and the reflowed
one-liner's absence (`bytes.count(b'undefined8 entry(void) { return 0x2a; }') == 0`).
If the row must carry a single line instead, use line 9 exactly as `  return 0x2a;` — but then the
"3 lines" descriptor must become "1 line" (or "line 9").

**Where the defect must be fixed (read-only observation, not edited by this seat):**
- `corpus/lessons/round-96.md:48` — the `## Gate` located quote + its "3 lines" descriptor.
- `corpus/SOURCES.md` row S504 (line 521) — cell 5 carries the anchor
  `Evidence ev_cc0b9d88…; fixture sha256 fe060de1…; record file digests printed in the citing entry's
  derivation table` and **no** body quote; the row's used-by cell names the candidate entry once.
  The `## Gate` line is where the non-verbatim quote actually lives, so the SOURCES row edit the
  r96 D1 text asks for is not textually present in the row.
- The candidate entry `corpus/knowledge/round-96-native-analysis-sessions.md:64` already records the
  body in a form that is faithful to the bytes (`undefined8 entry(void)` … `{` … `return 0x2a;` … `}`
  and `// decompiled_ok=1 of 1`, cited as lines 6–10) — it does **not** contain the reflowed
  one-liner (grep count 0).
- Repo-wide, the reflowed one-liner string occurs in exactly two places, both descriptive prose:
  `corpus/lessons/round-96.md:48` (the defect site) and
  `corpus/lessons/round-96-verifier-spotcheck.md:105` (the spot-check row quoting the defect itself,
  which is correct to keep as the record of D1).

**Note for the v6 counter author (not this seat's to build):** D1 requires a quote-check leg that
covers **own-work** rows — the current `C1_QUOTES` leg passes S504 because the lesson's one-liner
does not survive a byte-verbatim comparison. A leg that normalizes whitespace (as
`corpus/audit_source_quotes.py:22-23` `norm()` does) will *not* catch this class of defect, since
`norm("undefined8 entry(void) { return 0x2a; }")` == `norm("undefined8 entry(void)\n\n{\n  return 0x2a;\n}")`.
The distinguishing check is a byte-exact / line-anchored comparison against the cited file and line
range. This is a fact about the counter's contract, stated here for the executor seat; the v6 counter
was not scored or run by this seat.

---

## 4. Findings summary

| # | finding | evidence | verdict |
|---|---|---|---|
| F1 | S502 pinned body unchanged; located quote byte-verbatim present | HTTP 200, 38167 bytes, sha256 `c818ee34…` (= row and r96 receipt), `cmp` vs committed body exit 0, `grep -c -F` → 1 | **pass** |
| F2 | S503 pinned body unchanged; located quote byte-verbatim present | HTTP 200, 35095 bytes, sha256 `b5f17fdf…` (= row and r96 receipt), `cmp` exit 0, `grep -c -F` → 1 | **pass** |
| F3 | S504 located quote is **not** byte-verbatim (defect D1 live); "3 lines" is wrong (5 lines) | `grep -c -F` → 0 (exit 1); `git grep` at 66cb784 exit 1; byte layout read from the file | **fail as recorded** — replacement quote in §3, not repaired by this seat |
| F4 | S504 Evidence ID present | `grep -c -F` in `rea-decompile.raw.txt` → 1, on line 1 | **pass** |
| F5 | Base `7d380ce` carries 5 `^| S5` rows (S500–S504); S502/S503/S504 are already in the base registry | `git show 7d380ce:corpus/SOURCES.md \| grep -c '^| S5'` → 5, exit 0 | **pass** (informational for C1) |
| F6 | r96 receipts for S502/S503 are internally consistent; their `span` fields are **character** offsets while `SOURCES.md` records **byte** lengths/sha256 | `text[26309:26411] == receipt.quote` → True; S502 body 38167 bytes / 38165 chars | **pass** (no defect; offset convention documented to prevent a false D1) |
| F7 | The S504 reflowed one-liner occurs nowhere as a source-of-record; the candidate entry records the body in the byte-faithful per-line form | `grep -rn -F 'undefined8 entry(void) { return 0x2a; }' corpus reports` → 2 hits, both prose (lesson line 48 = the defect site; spot-check line 105 = the D1 record) | **pass** |

**Verdict for this seat:** the two external rows C1 rests on (S502, S503) re-open clean — bytes,
sha256, HTTP status and both located quotes unchanged and byte-verbatim, so §2b.4's sourced-claim
duty for C1 is satisfied on the source side. The third row (S504, own-work) fails its quote check
exactly as the r96 spot-check recorded; D1 is confirmed live and the byte-verbatim replacement quote
is supplied (§3) for the round to apply. Nothing in `corpus/` was edited.

## 5. Open questions

1. **Who applies D1.** The correction touches `corpus/lessons/round-96.md:48` (and the "3 lines"
   descriptor). This seat is read-only by contract; the L1 must route the edit. The r96 D1 text says
   "replace the one-line quote in `corpus/SOURCES.md` S504 and in `corpus/lessons/round-96.md`
   `## Gate`" — the SOURCES.md S504 row contains **no** such one-line quote (cell 5 is the
   Evidence/fixture/digest anchor), so that half of the D1 instruction has no text to act on.
   [INFERENCE, from the row's 11 cells; the row was not edited.]
2. **Which quote form the v6 quote-check leg should accept** — byte-exact only, or byte-exact with a
   named normalization (the D1 text allows either, if the normalization is named). The D1 fix and the
   v6 leg's acceptance rule must be the same rule, or the counter will accept what D1 forbids.
3. **Whether the v6 counter's `C1_QUOTES` leg is extended to own-work rows in this round** — D1 asks
   for it; this seat did not run or score any counter (freeze order: the L1 commits v6 after this wave
   returns), so no leg was exercised here.
4. **Whether the "3 lines" descriptor is also a D1 instance.** It is a second, separate inaccuracy in
   the same lesson line (the block is 5 lines: 6, 7 blank, 8, 9, 10). Reported, not repaired.
