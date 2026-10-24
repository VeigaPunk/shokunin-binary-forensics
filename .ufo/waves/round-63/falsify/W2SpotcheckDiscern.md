# W2SpotcheckDiscern — in-lane discernment first pass (round 63, falsify attempt 1)

Seat: `revenger-r63.W2SpotcheckDiscern` — fresh-seat reviewer, not the C06 author
or corrector. Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.
Bytes attacked: lane tip `db55bd6488e24e956df5818ae34c2a043d7ddc12` (`db55bd6`,
the integration commit carrying the C1 candidate entry + SOURCES S032/S033 +
lesson; build state `2a34e45`), claim base `55bcb6e1aeb4d42923a4e98db6580f67142b41ac`.
Frozen contract: `reports/round-63/claims.md`; counter `reports/round-63/measure.py`.
All citations below are to **committed bytes** (`git show db55bd6:<path>`), because
`corpus/lessons/round-63.md` was being edited in the worktree by a sibling while I
read (committed sha `ce7b47e8…`, worktree sha `3d6f643c…` at my read time).

**Verdicts.** (ADMIT) re-open of the C06 entry admission: **AGREE — recommend admit
(Q01–Q13 pass on the rows I evidenced).** (REJECT) re-open of the
S033-zipfile-docs screen-and-exclusion: **AGREE — exclusion is grounded; a flip
would be a source change.** Two commit-hygiene findings: one committed-bytes
narrative defect in the lesson's revision trail (medium, verdict-neutral, correction
already in flight and uncommitted) and one uncommitted `S034` row in `corpus/SOURCES.md`
that the entry does not cite (medium; would need the entry+lesson amended in the same
commit if landed, or dropped). Re-sample on the corrected tip `aaa0463`
(entry `285f641f…`): both verdicts stand, F1/F2/F4 resolved, two LOW sentence
fixes remain — see §6.

Tooling: none installed; no pacman (host-wide pause honored); read-only git
(`show`/`diff`/`archive` to /tmp), python3 stdlib, coreutils. No git/jj mutations,
no index writes, no sibling-lane or fleet-repo writes. Scratch: `/tmp/revenger-r63-discern/`
(removed after this report).

---

## 1. Commands I re-ran (mine, not inherited)

| # | command (cwd = lane root) | purpose |
|---|---|---|
| 1 | `git log --oneline -6; git rev-parse HEAD` | pin tip `db55bd6` |
| 2 | own `struct`/`zlib` script over `corpus/fixtures/archive-r2/fixture.zip` (stdlib, 40 lines, /tmp) | independent re-derivation, §2.1 |
| 3 | `git show 55bcb6e:<4 paths> \| sha256sum` + `sha256sum <4 paths>` | base-commit byte identity, §2.2 |
| 4 | extract `### Code` block from the committed entry to /tmp, `sha256sum`, `wc -l`; run `python3 -B readout.py .` | recheck reproduction, §2.3 |
| 5 | `sha256sum`/`grep -o` on `.ufo/waves/round-63/source-snapshots/{appnote.txt,zipfile.html}` | snapshot + quote evidence, §2.2, §3.1 |
| 6 | python3 over `corpus/live/runs/20261012T164246Z/artifact-inspection.json` | saved-record fields, §2.4 |
| 7 | `git archive db55bd6 corpus \| tar -x` + `TMPDIR=/tmp/revenger-r63-discern python3 -B reports/round-63/measure.py <tree>` | counter state at tip, §2.6 |
| 8 | `grep -c` for `import zipfile` / `compresslevel` / `truth_build_field`; `git diff 55bcb6e..db55bd6 -- corpus/` | exclusion grounds + preservation, §3.1, §5 |

---

## 2. (ADMIT) C06 entry `corpus/knowledge/round-63-zip-central-directory-evidence.md`

### 2.1 Independent re-derivation from bytes (my script, not the entry's readout)

I parsed the fixture with my own `struct.unpack` walk (EOCD located by
`bytes.rfind(b"PK\x05\x06")`, not by the entry's code) and inflated with
`zlib.decompress(payload, -15)`.

| entry item | entry value | my derivation from `fixture.zip` bytes | agree |
|---|---|---|---|
| 1/3 EOCD offset | 2942, 22 from end | `rfind` → **2942**, `len-2942` → **22** | ✓ |
| 3 EOCD fields | disk 0/0, counts 2/2, cd_size 114, cd_off 2828, comment len 0 | `struct.unpack("<HHHHIIH")` → **0,0,2,2,114,2828,0** | ✓ |
| 4 CD range | [2828, 2942), `cd_off+cd_size==eocd` | end of 2 parsed records = **2942**; equality **True** | ✓ |
| 6 `bin/checksum` CD | off 2828, nlen 12, method 8, crc `b3df9ea7` (3017776807), csize 2668, usize 16160, lho 0 | identical (crc32 `0xb3df9ea7` = 3017776807) | ✓ |
| 7 `README.txt` CD | off 2886, nlen 10, crc `72a557b1` (1923438513), csize 78, usize 84, lho 2710 | identical (`0x72a557b1` = 1923438513) | ✓ |
| 8 `bin/checksum` local | sig `504b0304`, payload off 42, 2668 B, inflated 16160 B, sha `f5ba0697…`, crc `b3df9ea7` | identical; inflated sha256 **f5ba069764ac66d5baa20224b0698a713823f45947a3364b67cfcb3f584897d0** | ✓ |
| 9 `README.txt` local | sig `504b0304`, payload off 2750, 78 B, inflated 84 B, sha `7d8f6a8d…`, crc `72a557b1` | identical; inflated sha256 **7d8f6a8de39432f4119f0139c5ef5970c84c23520cfe6b40d19a3653081804d3** | ✓ |
| 1/10 archive | 2964 B, sha `857989f5…` | **2964**, **857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e**; `truth.json archive_sha256/archive_size` equal | ✓ |
| 5 fixed widths | 30 / 46 / 22 | width sums of the entry's own field tables: 30, 46, 22 | ✓ |

Two required values were re-derived (EOCD/CD geometry and both CRC-32 +
inflated digests); the rest corroborate. The oracle never fed a derived value in
my run either (I read `truth.json` only after the derivation).

### 2.2 Gate evidence confirmed

- **S032 snapshot**: `sha256sum .ufo/waves/round-63/source-snapshots/appnote.txt` =
  `0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6`, `wc -c` =
  174585 — both exactly as the entry header, §Sources and S032 row state.
- **Located quotes are verbatim in that snapshot and ≤25 words**: exact-line hits at
  §4.3.7 (line 389, 7 w), §4.3.12 (line 522, 7 w), §4.3.16 (line 634, 8 w); the
  wrapped quotes match under whitespace-flex in their cited sections — 21 w
  (`crc-32 … extra field length 2 bytes`, present in **both** §4.3.7 and §4.3.12),
  23 w (EOCD counts), 24 w (§4.4.16), 20 w (§4.3.3), 23 w (§4.4.7).
- **Base-commit identity (entry item 2)**: all four files hash identically at
  `55bcb6e` and in the tree (`fixture.zip` `857989f5…`, `truth.json` `7df773bf…`,
  `artifact-inspection.json` `2fec924b…`, `LEDGER.md` `05042a55…`) — same=yes ×4.
- **S033 row** is present at tip as `own-work`, tier A, with the same four paths and
  digests; ids are contiguous S032/S033 (`grep '^| S0'` ends at S033; no S034 row).

### 2.3 Recheck command reproduced (Q02/Q11 gate)

Extracted the committed `### Code` block myself:

- script: **328 lines**, sha256 **94f502cde75eb47ffd3d7d8a73de45ad8889337a5269b669d998126a063a4bac** — matches the entry's own measurement block;
- `python3 -B readout.py .` → **exit 0**, **17 stdout lines**, sha256
  **02b0f495c1db8c50e22db835cd57e7a221dd0a9c82f09d442feea461de722ed4** — exactly
  the `recheck:` header's stdout digest;
- imports of the script: `binascii, hashlib, json, os, struct, sys, zlib` — **no
  `zipfile`**; raw DEFLATE wbits `-15` confirmed at line 167.

### 2.4 Saved-record fields (entry items 13–16) verified independently

`artifact-inspection.json` = **7692 B**, sha `2fec924b…`. Read from the JSON, not
from the entry: `evidence_id ev_5cc39f35…`; `operation inspect_artifact`; provider
`rea-artifact-graph` v`1`; `subject.root_sha256 857989f5…`; `occurrence_count 3`;
substep evidence id `ev_cc681c2a…` (the nested inventory id); occurrences
`.` (declared 2964, compressed null), `README.txt` (84/78), `bin/checksum`
(16160/2668, `executable true`), all `encrypted false`, `hash_status verified`;
occurrence→node linkage via `artifact_id` gives node sha256 `f5ba0697…`/16160
(elf) and `7d8f6a8d…`/84 (file) — matching what items 14–15 claim. The record's
own limitations text ("ZIP inventory lists central-directory entries only…")
matches item 22's paraphrase.

### 2.5 Named fresh-seat decisions (Q01–Q13, evidence above)

| Q | decision | basis (mine) |
|---|---|---|
| Q01 | **pass** | S032 is a `spec` row, tier A, opened 2026-10-23, with URL + section anchors + snapshot digest (all re-checked); S033 own-work row carries the same four digests; no claim rests on a third row; the excluded zipfile page is not cited as support. |
| Q02 | **pass** | `source:` / `verified-at:` (base commit) / `recheck:` (reproduced: 17 lines, `02b0f495…`) / `coverage-map: C06` all present; anchors are section numbers. |
| Q03 | **pass** | derived-first order holds in the code and in stdout (member/local facts print before `truth_*` comparisons); my own derivation used no oracle. |
| Q04 | **pass** | manual analysis labelled (item 29); the one tool named (`rea-agents@6.4.0`) is credited only with the saved record's existence/literal fields — and `LEDGER.md` line 5 literally records `npx -y rea-agents@6.4.0 inspect-artifact …`. |
| Q05 | **n/a — no readiness/capability claim** (entry claims none; past-tense saved file only). |
| Q06 | **pass** | archive length/digest derived and compared; base-commit identity re-checked by me. |
| Q07 | **n/a — no predicted parser behaviour**; the offsets are arithmetic over the field tables, and item 26 disclaims parser semantics. |
| Q08 | **superseded by Q11** (as QUALITY.md states). |
| Q09 | **pass** | every printed digest binds its own bytes (archive / two inflated payloads / saved file); no origin, completeness or authenticity claim (items 20, 28). |
| Q10 | **pass** | scoped to one archive, one oracle, one saved record, one provider id+version, one operation; no other lane's file cited. |
| Q11 | **pass** | §Sentence-to-output inventory maps items 1–16 + RP + S1 to fact ids; I spot-verified items 3, 6, 8, 10, 13, 15 against live stdout and the saved record; item 2's command outputs are reproduced; the script/stdout/snapshot measurement blocks reproduce exactly. |
| Q12 | **n/a — no rejected row cited** (the zipfile page was excluded without a row, so no reject reason is owed; consistent with QUALITY.md Q12 being about rejected *rows*). |
| Q13 | **pass** | no verifier/recheck command is credited as a guard; §Q13 says so explicitly and the recheck is a reproduction, not a deletion-sensitive check. |

This is a **fresh-seat recommendation**, not admission: the README flip and the
lesson Gate decision remain L1's (entry's own Q01 cell says the same).

### 2.6 Counter state at the committed tip (I ran it)

`git archive db55bd6 corpus` → `python3 -B reports/round-63/measure.py <tree>`
(exit **0**):

```
K_HELD=6/14 score=4.3      K_ROW C06 status=partial      K_HELD_BACKED=6/14
F_COVERAGE=5/8 score=6.2   F_FAMILIES=[native-static, javascript, archives, firmware, evm]
C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2
C3_CONTROLS_PASS=2/2       C3_RECEIPT_KILLED_ATTRIBUTED=2/2
HOLD_CALIBRATION=4/4       HOLD_REPLAY=10/10   HOLDS_OK=yes
```

C1's target `K ≥ 7/14` is **not met at tip and not falsified**: the frozen admission
order makes the flip contingent on named fresh-seat decisions (this report is one),
and `README.md` contains **0** occurrences of the new entry name — a status-only
flip would satisfy the counter without the entry, which is exactly the M34
counter-substitution the contract forbids. The flip must add
`knowledge/round-63-zip-central-directory-evidence.md` to the C06 knowledge cell
(`K_HELD_BACKED` requires it).

---

## 3. (REJECT) S033-zipfile-docs screen-and-exclusion

### 3.1 Grounds checked, each from bytes

| ground | measurement | holds |
|---|---|---|
| **The page defers to APPNOTE itself** | `zipfile.html` (sha256 `9520a8cbce7d3c8b7ea6704f60ac1122856da14d1bdc4161075912303a270739`, 139782 B — matches lesson) contains, in the module introduction: "Any advanced use of this module will require an understanding of the format, as defined in `<a href="https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT">`PKZIP Application Note`</a>`." — **19 words**, exactly the quote and count the lesson records | ✓ |
| **0 zipfile imports (scoped to the readout)** | `.ufo/waves/round-63/build/zip-readout.py` imports `hashlib json pathlib struct zlib`; the committed entry's own `### Code` (the §Reproduce script) imports `binascii hashlib json os struct sys zlib` — **neither imports zipfile**, in either revision | ✓ |
| **APPNOTE already tier A for the scope** | S032 row: tier `A`, `spec`, with §4.3.3/§4.3.12/§4.3.16/§4.4.7/§4.4.10-12/§4.4.16/§4.4.21-22 and a snapshot digest; every load-bearing field claim anchors there | ✓ |
| **No entry sentence asserts zipfile behaviour** | the only occurrence in the entry is `truth_build_field`, printed with the note "this entry makes no claim about the behaviour of any library it names and does not rely on it for any value" (item RP, §Sources third bullet); `truth.json`'s `build` string is owned by S033 | ✓ |
| **Search-log counts** | line 73: "Identified 3, screened 3, included 1 row (S032), excluded 2 (…; Python zipfile docs — screened-and-excluded, no row …)" — internally consistent with 2 excluded | ✓ |

### 3.2 A flip would be a source change — concretely

Flipping the screen would require: (a) appending a registry row (S034, or
renumbering S033 and its 5 uses), i.e. editing `corpus/SOURCES.md`; (b) amending
the same line-73 search note's counts (`excluded 2 → 1`, `included 1 → 2`); (c)
contradicting the lesson's "**S032 + S033 with no id skipped**" id-allocation
paragraph; (d) adding the page to the entry's §Sources/Q01/Q12. None of that buys
support: no claim needs the page, and the page itself points at the spec already
held. That is precisely Q12's "the flip asks for a change to the source" test —
here the change would be to the source *registry*, and the reject reason does not
exclude any scope the entry uses. **AGREE with the exclusion.**

### 3.3 Defect found while re-opening it (verdict-neutral)

The committed lesson (`db55bd6:corpus/lessons/round-63.md`, the "Revision trail"
sentence) says:

> the first candidate revision read (`630b974a…`) already carried the same
> `truth_build_field` fact (two occurrences) … the earlier premise was not.

That is **false on committed-bytes evidence**, independently of the seat that
reported it:

1. The committed build report `.ufo/waves/round-63/build/R63EntryC06.md`
   (tracked blob `a0351d0a…` at tip) pins rev1 `candidate.md` = `630b974a…` and its
   stdout = `e112d4092dfa8e3ed5398f07d1222457455ca06a94e01e988a0f58eab4c445ec`
   (17 lines).
2. I measured the preserved rev1 stdout (`/tmp/revenger-r63-entry/recheck-stdout.txt`,
   mtime 23:36): sha256 `e112d409…`, **17 lines**, `grep -c compresslevel` = **0**,
   `grep -c truth_build_field` = **0**.
3. The recorded build string necessarily contains `compresslevel`
   (`truth.json`: "Python zipfile.ZipFile(mode=w, compression=ZIP_DEFLATED,
   compresslevel=9); …"), so no 0-`compresslevel` stdout can carry a build-field
   line. Rev2 (`dcfe131c…`), not rev1, carried the two occurrences.

The exclusion **conclusion** survives on every reading (the current entry prints
the string as a recorded field with a no-claim note), and a sibling is editing the
lesson to correct the attribution (worktree sha `3d6f643c…`; committed `ce7b47e8…`).
Recorded here because the round's committed bytes still carry the withdrawn claim.

---

## 4. Findings by severity

**F1 — MEDIUM (committed bytes, narrative): lesson revision-trail sentence is false
at tip `db55bd6`.** `corpus/lessons/round-63.md` (worktree lines ~107–112 / committed
equivalent) attributes two `truth_build_field` occurrences to rev1 `630b974a…`;
rev1's preserved stdout is `e112d409…` with `compresslevel` = 0 and
`truth_build_field` = 0 (my counts), and the committed build report pins the digest
pairing. Impact: none on the exclusion verdict or on C1/C2/C3; it does weaken the
lesson's own Q11-style audit trail if cited as written. Fix in flight by a sibling
(uncommitted at my read); land it in the integration commit.

**F2 — LOW (lesson wording): "both use `struct`/`binascii`/`zlib` directly".**
`build/zip-readout.py` imports no `binascii` (`hashlib, json, pathlib, struct,
zlib`). The load-bearing clause — neither readout script imports `zipfile` — is true
in both scripts, so the exclusion does not move.

**F3 — INFO (C1 state): at tip the claim is neither met nor falsified.** Counter
prints `K_HELD=6/14`, `K_ROW C06 status=partial`, and `README.md` names the new
entry zero times. C1 can only read 7/14 after L1's flip naming the entry in the row
(a status-only flip is counter-substitution, M34). My named Q01–Q13 recommendations
are the fresh-seat input for that flip.

**F4 — MEDIUM (uncommitted worktree change, integration hazard): an `S034` row
appeared in `corpus/SOURCES.md` that the entry does not cite.** At my read the
worktree `corpus/SOURCES.md` (uncommitted; the committed tip ends at S033) carries
`| S034 | PKWARE APPNOTE.TXT … | spec | A | local file header record field layout …
| §4.3.7 … snapshot lines 387-399, sha256 0b993022… | … | mined | 2026-10-23 | on-release |
corpus/knowledge/round-63-zip-central-directory-evidence.md |`. The entry is
unmodified in both bytes: `grep -c S034` = **0**, and it states "No third source is
cited" (§Sources) and "No claim in this entry rests on a row outside those two"
(Q01). The committed lesson states "S032 + S033 with no id skipped" and
"`S032 ×10 / S033 ×5 / S034 ×0`" (committed lines 132–133), with the earlier S034
reservation recorded as withdrawn. If S034 lands as-is: (a) the row's `used-by`
cell claims a citation the entry does not contain; (b) the lesson's id/count
paragraph becomes false; (c) the line-73 search note's "included 1 row (S032)"
becomes stale for that document set. Scope-split rows do have precedent
(S022/S029 for ECMA-262), but each was logged as its own screened/included
decision, and nothing in the entry needs the split: its local-header claims are
already quoted from S032 §4.3.7. **This is a source change** and is outside what
either verdict here requires — if it lands, the entry's §Sources/citation counts
and the lesson must be amended in the same commit, or the row dropped. I did not
edit or revert it.

No other defect found: every re-derived value in the entry matched my independent
`struct`/`zlib` walk; the recheck command reproduces bit-for-bit; the gate quotes
are verbatim and ≤25 words; the saved-record fields match the saved JSON.

---

## 5. Residual risk and verification gaps

1. **Scope breadth of C06.** The entry examines `fixtures/archive-r2` only; the
   README C06 row also lists `nested-r11` and `duplicate-r15`. The entry states this
   in item 33 and does not claim them — honest, but the row's coverage is broader
   than one archive. Any future C06 "held" audit should keep that boundary in view.
2. **Concurrent edits.** At my read, `corpus/lessons/round-63.md` differed between
   the committed tip (`ce7b47e8…`) and the worktree (`3d6f643c…`, the F1 correction),
   and `corpus/SOURCES.md` had an uncommitted `S034` row (F4). All my citations are
   pinned to `git show db55bd6:…`; the final bytes of both edits are L1's to verify,
   and F4 must land with its entry/lesson amendment or not at all.
3. **I did not re-run C2's producer or construct C3 mutants myself** (outside this
   ticket's target). The only C2/C3 numbers I report are the frozen counter's own
   output at tip (`C3 2/2`, `C2 attributed 2/2`, `HOLDS_OK=yes`, exit 0).
4. **Provider-field semantics** (`executable`, `encrypted`, `hash_status`) are
   recorded-only in the entry and explicitly unknown (item 21); nothing to test.
5. **Preservation check (context, not a claim):** `git diff 55bcb6e..db55bd6 -- corpus/`
   adds only round-63 paths (`fixtures/firmware-r63/`, `knowledge/round-63-…`,
   `lessons/round-63.md`, `live/runs/round-63/`) plus the SOURCES row append and the
   two C3 verifier patches; no deletions and no other fixture/live byte modified in
   the base..tip diff. The counter's `HOLD_REPLAY=10/10` run is consistent with that.

---

## 6. Re-sample on the corrected entry (tip `aaa0463`, L1 request)

New tip `aaa046326d92ba983f3ae99341438c9b8509a6cc`; entry sha256
`285f641f4774a35f663c7ace731839e789c24d028cab1f455078df60fc9e56a1`
(`git show aaa0463:…` and the worktree agree). Correction scope: source split
S032→S034 (local file header moved to its own row), S033 narrowed to fixture +
oracle + saved record, new S035 row for the run ledger, recheck digests re-pinned.

**Re-derivation on corrected bytes (same fixture, re-run by me).** `fixture.zip` is
still `857989f5…`, 2964 B at this tip; my own parser re-run gives the identical
values: EOCD at **2942** (22 from end), CD **[2828, 114)**, EOCD counts **2/2**,
`cd_end == eocd` True, `bin/checksum` crc **b3df9ea7** csize 2668 usize 16160 inflated
sha **f5ba0697…**, `README.txt` crc **72a557b1** csize 78 usize 84 inflated sha
**7d8f6a8d…**, both recomputed CRCs equal to the CD values.

**Recheck reproduced.** Extracted the corrected `### Code`: **329 lines**, sha256
**8dbefe4dae2fd170d4bd658c4d1111e66a15b266687fe586e385d9aab74c367f**; running it
gives **exit 0**, **17 lines**, stdout sha256
**ccaffa322c49d1850fb7da86dc9221ea3bd73c8e3db81cc2ce9be6a1e5b40dc5** — exactly the
new `recheck:` header and §Reproduce measurement block. The `wc-w` fix is real: the
measurement block now shows the generating command before `wc -l`/`sha256sum`, so
the printed numbers are reproducible from the block itself.

**Registry consistency (all four rows `mined`, used-by the entry).** S032 scope is
now the CD file header + EOCD record, matching the entry header; S034 carries the
§4.3.7 local-header scope with the same snapshot digest and lines 387–399; S033
covers fixture + oracle + saved record; S035 covers the ledger (`05042a55…`, 3959 B
— file size re-checked). The entry cites S032 ×13, S033 ×11, S034 ×15, S035 ×11
(raw occurrences) and its Q01/Q02 rows now name four rows with the scope discipline
stated ("no local-header-layout claim cites S032, and no CD/EOCD claim cites S034").

**Counter at `aaa0463`** (my run, exit 0): `K_HELD=6/14`, `K_ROW C06 status=partial`,
`K_HELD_BACKED=6/14`, `F_COVERAGE=5/8`, `C3_CONTROLS_PASS=2/2`,
`C3_RECEIPT_KILLED_ATTRIBUTED=2/2`, `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`,
`HOLDS_OK=yes`. C1 still awaits L1's flip naming the entry.

**Verdicts on corrected bytes: unchanged.** ADMIT **AGREE** — my Q01–Q03/Q06/Q09/
Q11/Q13 passes re-stand on the four-row sourcing (Q01 now cleaner: each claim cites
the row whose tier-A scope covers it). REJECT **AGREE** — the zipfile-docs exclusion
is untouched: still no row, Q12 still n/a, and the two new rows are the same APPNOTE
document under a second scope plus the ledger, neither of which is the excluded page.

**Finding status after the correction.**

| id | status |
|---|---|
| F1 lesson revision-trail misattribution | **resolved** — committed correction ("Revision trail, CORRECTED against preserved evidence…", `e112d409…`, 0 `compresslevel`) |
| F2 lesson "struct/binascii/zlib" parenthetical | **resolved** — the parenthetical is gone from the lesson |
| F4 uncited S034 registry row | **resolved** — the entry now cites S034 and S035; both rows are honest `used-by` |
| F5 (new, LOW) | entry §Sources still says "**No third source is cited.**" while the header and body cite four rows; false as written, fix is "no further source is cited" or the four-row form |
| F6 (new, LOW) | lesson id-allocation paragraph still says "the earlier S034 reservation is withdrawn", "`S032 ×10 / S033 ×5 / S034 ×0`" and "the contiguous pair **S032 + S033 with no id skipped**", with no supersedes marker beside the later S034/S035 paragraphs that landed in the same commit; the dated revision clause softens but does not remove the contradiction |
| F7 (new, INFO) | S035 row scope wording ("the recorded observation/inference/unknown layer of the saved archive inventory record") reads as the saved record's layer; the row title/anchor/note make the referent (the ledger) clear, and the entry's use is provenance-only, so Q01 is unaffected |

No value-bearing defect found on the corrected bytes.

---

## 7. Evidence appendix (exact output snippets)

```
$ sha256sum corpus/fixtures/archive-r2/fixture.zip corpus/fixtures/archive-r2/truth.json \
    corpus/live/runs/20261012T164246Z/artifact-inspection.json corpus/live/runs/20261012T164246Z/LEDGER.md
857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e  corpus/fixtures/archive-r2/fixture.zip
7df773bf46b7c1273f8c3402b7825e7dacbb7f990c7d7ef41f30917c94726e68  corpus/fixtures/archive-r2/truth.json
2fec924b5217885674149b6a516970f419a8e731c8e6e49eab178a4f065f3380  corpus/live/runs/20261012T164246Z/artifact-inspection.json
05042a555f91511c9c191565d92f83527f54d1c9b14de331587f4cbffff9e6cb  corpus/live/runs/20261012T164246Z/LEDGER.md
# (identical at 55bcb6e via git show for all four — same=yes)

own derivation (EOCD found by bytes.rfind(b"PK\x05\x06")):
{'disk': 0, 'disk_cd': 0, 'n_disk': 2, 'n_tot': 2, 'cd_size': 114, 'cd_off': 2828, 'clen': 0}  eocd=2942 from_end=22
bin/checksum  crc=b3df9ea7 csize=2668 usize=16160 lho=0    payload@42  inflated=16160 sha=f5ba0697…  crc_match=True
README.txt    crc=72a557b1 csize=78   usize=84   lho=2710 payload@2750 inflated=84    sha=7d8f6a8d…  crc_match=True
cd_end=2942 == eocd: True

$ python3 -B readout.py .        # extracted from the committed entry's ### Code
exit=0   17 lines   sha256(stdout)=02b0f495c1db8c50e22db835cd57e7a221dd0a9c82f09d442feea461de722ed4
sha256(readout.py)=94f502cde75eb47ffd3d7d8a73de45ad8889337a5269b669d998126a063a4bac   lines=328

$ sha256sum .ufo/waves/round-63/source-snapshots/appnote.txt
0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6   (174585 bytes)
$ sha256sum .ufo/waves/round-63/source-snapshots/zipfile.html
9520a8cbce7d3c8b7ea6704f60ac1122856da14d1bdc4161075912303a270739   (139782 bytes)
quote in body: "Any advanced use of this module will require an understanding of the
format, as defined in <a …APPNOTE.TXT>PKZIP Application Note</a>."   wc -w = 19

rev1 preserved stdout: sha256 e112d4092dfa8e3ed5398f07d1222457455ca06a94e01e988a0f58eab4c445ec
                       17 lines   compresslevel=0   truth_build_field=0
committed build report pins: candidate 630b974a… ↔ stdout e112d409… (17 lines)
```
