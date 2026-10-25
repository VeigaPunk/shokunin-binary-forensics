# R68CensusReplay — source-census replay (round-68, revenger)

DEFECT (narrow, registry-only): the census exits 0 and shows exactly the four pre-existing W04 duplicate-URL warnings, but the fifth line is a **W03 `S046 mined but unused`** that is *not explained anywhere in the tree* and is contradicted by the lane's own precedent — S046 is the row C2's entry cites in its `source:` header (`corpus/knowledge/round-68-apk-axml-byte-evidence.md:4`), yet the row's `used-by` cell is `—`. No claim predicate and no counter value is affected.

## Axes
- **Coverage** — registry shape: 46 rows, ids contiguous S001–S046, no duplicate ids, no `superseded`/unknown statuses, 11 columns parse.
- **Freshness** — `recheck` values legal, none overdue; the row under test opened 2026-10-24 (≤ today 2026-10-25).
- **Honesty of the warning set** — are the 5 non-ok lines all accounted for (4× disclosed W04 + 1× explained W03)?

## 1. Census replay (full output + exit code)

```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger
revenger	W04	S024 duplicate url www.rfc-editor.org/rfc/rfc3227.txt across scopes
revenger	W04	S028 duplicate url github.com/ethereum/execution-specs/tree/v2.20.0/src/ethereum/forks/osaka/vm across scopes
revenger	W04	S029 duplicate url tc39.es/ecma262 across scopes
revenger	W04	S034 duplicate url pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT across scopes
revenger	W03	S046 mined but unused
revenger	ok	/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md
EXIT_CODE=0
```

Captured verbatim to a file: **6 stdout lines, 0 stderr lines, exit 0, stdout sha256 `9c3c730fc5e5c29b92094cc6dbae9dd95aecf8e1f38463bf0645877bcdfcaf48`**. A second independent run reproduced the identical 6 lines and exit 0.

Census tool identity (freshness of the checker itself): `sha256sum /home/vgpnk/Projects/shokunin/scripts/sources-census.sh` → `3fb7261569f46423dd80ecc23e0a23789a7926f667c7a3fc559d2439d4a64e30`.

The four W04 rows are **unchanged bytes from before this round** (see §3 — the diff adds no W04 row and touches no URL cell), so they are baseline, not new.

## 2. Row count and registry shape

```
$ grep -cE '^\| S[0-9]+ ' /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md
46
```

Contiguity/duplicate check over the same pattern: `min=1 max=46 count=46`, zero `uniq -d` hits, zero gaps.

Status tally (`awk -F'|'` over the same rows): `mined=38 queued=4 rejected=4`, and `mined && usedby=="—"` → **1** (S046). That one is exactly the W03 the census prints; the W03 rule is `status=="mined" && usedby=="—"` at `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh:673-674`.

No escaped/literal `|` corruption observed: the S046 row splits into the expected 11 columns + the two outer empties (checked field-by-field, `col1..col12`).

## 3. S046 and S045 status, and the diff against the committed round-67 bytes

S046 (`corpus/SOURCES.md:61`), cells verbatim:

| column | value |
|---|---|
| id | `S046` |
| source | `AXML anchor derivation — corpus/derive_axml_anchors.py over corpus/snapshots/ResourceTypes.h` |
| kind | `own-work` |
| tier | `A` |
| scope | `the machine derivation of every AOSP ResourceTypes.h line number the round-68 C05 candidate cites; the layout facts themselves rest on S038` |
| anchor | `script sha256 bce497d6…e249, 17 output lines; snapshot copy sha256 56b88bc4…c56f (86255 bytes, byte-exact copy of the S038 snapshot .ufo/waves/round-65/source-snapshots/ResourceTypes.h); located quote: enum RES_XML_START_NAMESPACE_TYPE : 245` |
| teaches | `Turns the transcribed spec line numbers into a re-derivable command…` |
| status | `mined` |
| opened | `2026-10-24` |
| recheck | `on-release` |
| **used-by** | **`—`** |

S045 (`corpus/SOURCES.md:59`): `status=mined`, `opened=2026-10-24`, `recheck=180d`, `used-by=corpus/knowledge/round-67-apk-axml-byte-evidence.md`.

Diff against the committed round-67 tip (HEAD is `4232235`, `main~2 = f165908`; `git status --porcelain corpus/SOURCES.md` is empty, so the working file equals HEAD):

```
$ git -C /home/vgpnk/Projects/shokunin/revenger-shokunin diff refs/heads/main~2 -- corpus/SOURCES.md
 corpus/SOURCES.md | 3 +++
 1 file changed, 3 insertions(+), 0 deletions(-)
   @@ -60,0 +61,2 @@   +| S046 | AXML anchor derivation … (new row) + (blank line)
   @@ -96,0 +99 @@    +- 2026-10-24, round-68 AXML anchor derivation (S046). Unit: … (changelog bullet)
```

**3 insertions, 0 deletions**: no row other than S046 changed, and no existing cell was rewritten. Current file sha256 `fa81a6148c89e47d8032c8b026ee7455f3df684e44829bf77b6862fcb5ff61f6`.

## 4. Why the W03 is a defect and not a disclosure

The brief admits CLEAN only for `exit 0 + the disclosed W04 warnings + an *explained* S046 W03`. The W03 is unexplained and self-contradictory:

1. **The row is used by a committed file, at a resolvable pointer.** `corpus/knowledge/round-68-apk-axml-byte-evidence.md:4` begins `source: S046 — AXML anchor derivation (own-work, tier A; row opened round 68 by this entry's author) …` and `reports/round-68/claims.md` §Frontier step states: "C2 cites the `S###` row opened this round (`S046`, own-work, tier A, opened 2026-10-24) in the entry's `source:` header." A cell reading `—` therefore contradicts both the entry and the round's own registered claim text.
2. **No explanation exists anywhere in the tree.** `grep -rn 'W03\|mined but unused' .ufo/waves/round-68/ reports/round-68/` returns only the seat prompts themselves (`build-wave-spec.py:196` and its `wave-spec.json` copy) — no disclosure text. The build commit body (`git log -1 --format=%B 4232235`) is a single subject line with no mention. The S046 changelog bullet (`corpus/SOURCES.md:99`) records identified/screened/included and an id-collision note, not this warning. `corpus/lessons/round-68.md` **does not exist** (`ls corpus/lessons/` ends at `round-67.md`), so the claims.md-ordered "census before → after … with both outputs and exit codes" record is still outstanding.
3. **Precedent in this same registry fills the cell at landing, including for a candidate entry.** `git log -S '| S045 |' -- corpus/SOURCES.md` → `7668510` (round-67 build). At `git show f505526:corpus/SOURCES.md` the S045 row already carries `used-by=corpus/knowledge/round-67-apk-axml-byte-evidence.md` — and that round-67 entry was itself a candidate, not an admitted entry. So "the consumer is only a candidate, hence `—`" is not the lane's practice; the round-68 row departs from it silently.

Fix (not applied by this read-only seat; one cell, contract-legal because `used-by` is a mutable field per `corpus/SOURCES.md:5-8`, with the old→new logged in the round lesson): set S046 `used-by` to `corpus/knowledge/round-68-apk-axml-byte-evidence.md`. If `—` is deliberate until C2 admission, the explanation must land in `corpus/lessons/round-68.md` next to the census before→after — today nothing carries it.

A dedicated seat already frames this exact question (`R68ReviewSourcesS046`: "is that honest?" for a CANDIDATE entry); this replay's evidence is that the tree currently answers "unexplained", and that the round-67 candidate precedent answers "fill it".

## 5. Freshness axis (separate, clean)

```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh overdue --root /home/vgpnk/Projects/shokunin revenger
… 47 cadence lines (S001–S046), OVERDUE_EXIT=0
```
No `overdue` line emitted: every dated cadence is in the future, and every `on-release`/`90d`/`180d` value is legal (`recheck` validation at `sources-census.sh` E09 branch). S046 `opened=2026-10-24` ≤ today 2026-10-25; `recheck=on-release` is legitimate for an own-work script tied to the pinned snapshot.

## 6. Adjacent observation (registered, not counted against the census)

S045's `used-by` names only `corpus/knowledge/round-67-apk-axml-byte-evidence.md`, while `corpus/knowledge/round-68-apk-axml-byte-evidence.md:3` also declares `source: S045`. That is round-67 defect **D4** ("the S045 `used-by` re-point"), registered at `reports/round-68/claims.md:199-201` as a carried repair with a spec-only seat in this wave (`wave-spec.json`, "`used-by` value and what it points at … Verdict: RE-POINT-SPECIFIED … Do not edit anything"). It is therefore disclosed by design and does not contribute to the verdict; recorded so the census "after" snapshot is read with it in view.

## 7. Risks / blockers
- Verdict scope: registry bookkeeping only. C1 (C7 attribution) and C2 (C05 v3 candidate) predicates are untouched by this finding; the counter is unaffected.
- `corpus/lessons/round-68.md` absent is a dependency for the frontier-step requirement, not a blocker for this replay.
- No files edited, no git/jj mutation, no tool installs or upgrades (nothing needed). Scratch capture under `/tmp/r68census.out`, `/tmp/r68census.err` removed.

## Evidence index
- `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh:673-674` (W03 rule), `:645-649` (W04 rule), `:139` (W03 self-test), `:361-364` (W04 mutation self-test); sha256 `3fb72615…a64e30`.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md:5-8` (mutable-field contract), `:13` (11-column header), `:59` (S045), `:61` (S046, used-by `—`), `:99` (round-68 changelog bullet); sha256 `fa81a614…5ff61f6`.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-68-apk-axml-byte-evidence.md:3` (S045), `:4` (S046), `:107` (S045 use in item 9).
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-68/claims.md:199-201` (D1–D4 register), `§Frontier step` (census before→after obligation; C2 cites S046).
- Git: `HEAD=4232235723cf8d4731a1e7e78ca098b8af953a57`, `main~2=f165908`; `7668510` adds S045 with `used-by` populated (verified at `f505526:corpus/SOURCES.md`).
- Census stdout sha256 `9c3c730fc5e5c29b92094cc6dbae9dd95aecf8e1f38463bf0645877bcdfcaf48` (6 lines, exit 0, reproduced twice).
