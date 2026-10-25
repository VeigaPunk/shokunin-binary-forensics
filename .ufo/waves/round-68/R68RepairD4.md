# R68RepairD4 — routed defect D4: the S045 `used-by` cell points at a rejected candidate

**RE-POINT-SPECIFIED — two adjudication cases, two different exact cells; plus one mandatory
cell repair (S046) that holds in either outcome and is not visible to any registered census.**
Read-only seat: nothing was edited, no target touched, no tool installed. Every number and cell
below was printed by a command this seat ran against the committed tree.

Anchor: `corpus/SOURCES.md` sha256 `fa81a6148c89e47d8032c8b026ee7455f3df684e44829bf77b6862fcb5ff61f6`,
99 lines; the S045 row is line 59 (972 bytes, `NF=13`).

## 1 · The defect as routed, verified

`corpus/lessons/round-67-verifier-spotcheck.md:237-239` (§7 item 4):

> 4. **The S045 row's `used-by` points at a rejected candidate.** A mined row whose only consumer is a
>    retained-rejected entry is honest but worth a re-pointing rule when the candidate is re-gated, so
>    the registry does not look like it backs held ground.

**Current `used-by` value** (field `$12`, the 11th column of the row, `NF=13`):

```
S045 NF=13 status=[ mined ] used-by=[ corpus/knowledge/round-67-apk-axml-byte-evidence.md ]
```

The row as a whole, by contract column order (`corpus/SOURCES.md:13`
`| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |`):

| cell | value |
|---|---|
| id | `S045` |
| source | DEX format specification (Android Open Source Project) — https://source.android.com/docs/core/runtime/dex-format |
| kind / tier | `docs` / `A` |
| status | `mined` |
| opened / recheck | `2026-10-24` / `180d` |
| **used-by** | **`corpus/knowledge/round-67-apk-axml-byte-evidence.md`** |

**What it points at, confirmed by grep** — the round-67 candidate carries the rejected verdict
(`corpus/knowledge/round-67-apk-axml-byte-evidence.md:8`):

```
admission-status: rejected — the dispatched round-67 wave's named fresh seats ruled Q02 FAIL on these
bytes (seat `R67ReviewEntryQ02`: the S038 anchor cites `RES_XML_START_NAMESPACE_TYPE` at snapshot line
244 twice — entry:1 and :56 — but the pinned, re-hashed snapshot has it at line 245; :244 is
`RES_XML_FIRST_CHUNK_TYPE`; …) — the same anchor-precision class (M40) that falsified the round-65
draft recurs in one of the six repairs; per `reports/round-67/claims.md` §C1 kill rule the C05 row
stays `uncovered` and this candidate is retained as evidence …
```

So D4 is accurate as filed: the registry's *only* named consumer of S045 is a file whose own
`admission-status` is `rejected`, and the README C05 row is `uncovered`. The lane documented that
state honestly (`corpus/lessons/round-67.md:79-80`: "Status mined; used-by
`corpus/knowledge/round-67-apk-axml-byte-evidence.md`"), and the spot-check accepted it as honest —
the defect is **forward-looking**: what the cell must become when the candidate is re-gated.

## 2 · The rule that licenses the change (the registry contract's own)

Two clauses, both needed, both from the contract this file names at `corpus/SOURCES.md:3`
(fleet `.ufo/waves/kaika/SOURCES-CONTRACT-v1.md`, frozen 2026-10-19):

- **Definition** — `SOURCES.md:13` / contract §Field definitions:
  > `used-by` — repo-relative paths of the knowledge entries or lessons citing the row,
  > comma-separated, or `—`.
- **Mutation rule** — contract §Rules 2 (`SOURCES.md:6`, mirrored at `SKILL.md:118`):
  > **Append-only.** Only `status`, `recheck` and `used-by` change in place, and each change is
  > logged old→new in the round lesson.

Consequences, all load-bearing for the two cases:

1. The edit is **licensed in place** — no new row, no `supersedes`, no touch to any other cell.
   (A correction row is rule 2's *other* mechanism and is for corrections of a row's claim, not for
   a pointer update.)
2. The change **must be logged `old → new` in `corpus/lessons/round-68.md` `## Gate`**. That file does
   not exist yet — `ls corpus/lessons/ | grep round-68` is empty (only `round-67.md`,
   `round-67-verifier-spotcheck.md` are present) — so the log line is part of the same landing.
3. The change **lands in the same revision as the flip/Gate decision**, per
   `reports/round-68/claims.md:129-130`: "The flip and the Gate decision land in the same revision."
   It must **not** land before adjudication: pre-committing the cell to the round-68 path is a
   different defect (a pointer to a candidate whose status is still `candidate`).
4. `status` is **not** part of this repair. S045's `mined` claim stays true in both cases — contract
   §Field definitions: "`mined` (cited by ≥1 path in `used-by`)" — because in case (a) the `used-by`
   path is the admitted round-68 entry and in case (b) it is the retained round-67 entry. `mined`
   asserts *a citation exists*, not *admitted ground rests on it*; admittedness is carried by the
   README C05 row and by the entry's own `admission-status`, never by `status` here.

## 3 · The two cases — exact cells

### Case (a) — C2 passes, the v3 entry is admitted (README C05 row flips to held)

**Exact cell value:**

```
corpus/knowledge/round-68-apk-axml-byte-evidence.md
```

i.e. **replace** the round-67 path (old → new, logged). Why replace and not append:

- The round-68 entry is the *admitted consumer* of S045: `corpus/knowledge/round-68-apk-axml-byte-evidence.md:3`
  cites S045 for exactly the same scope the row declares (the `header_item` field semantics), and
  `:107` (item 9) re-derives the checksum/signature/header-size/endian facts from it.
- The lane's own single-entry convention is already fixed on the README side by C2's frozen
  predicate `C05_SINGLE_V3=yes` — "the C05 row's knowledge column names exactly the round-68 entry"
  (`reports/round-68/claims.md:119-120`). Naming exactly one entry is the round's declared shape for
  this candidate; the registry cell should not contradict it.
- The superseded round-67 file keeps its bytes (it is retained as rejection evidence); it simply
  stops being the entry of record for S045. Nothing is deleted from disk, so no provenance is lost.

*Alternative reading, stated for completeness and not recommended:* if the lane adopts exhaustive
citation semantics (every file that still contains `source: S045 —`), the cell becomes the ordered
two-path list `corpus/knowledge/round-67-apk-axml-byte-evidence.md, corpus/knowledge/round-68-apk-axml-byte-evidence.md`.
That permanently pins the rejected path into the cell — precisely what D4 asks the registry not to do —
and it is not required by the contract, whose definition does not demand exhaustiveness.

### Case (b) — C2 fails, the v3 entry is marked `admission-status: rejected`

**Exact cell value: unchanged**

```
corpus/knowledge/round-67-apk-axml-byte-evidence.md
```

**No re-point is licensed on a fail.** Per `reports/round-68/claims.md:126-130`, a fail executes the
kill rule: "the C05 row stays `uncovered`, the v3 entry is marked `admission-status: rejected`
(retained as evidence, every other byte kept)". A rejected entry creates **no** consumer of held
ground, so there is nothing for the cell to point at that would improve on the current value:

- pointing at `corpus/knowledge/round-68-apk-axml-byte-evidence.md` would mint a *newer rejected
  pointer to the same source* — D4 reproduced one round later, with strictly less information than
  the cell already carries (both candidates are the same evidence at different anchor precision);
- setting `—` is **factually false** — the row is still cited by two files on disk (`round-67:3,106`
  and `round-68:3,107`) — and it would also read as `mined`-without-citation, which the census cannot
  see (§4). Contract §Field definitions allows `—` only for a row nothing cites;
- flipping `status` to `queued` is backwards: `queued` means "opened, worth mining", and S045 has been
  mined since round 67.

The rejection is recorded where the contract puts admission evidence: in the entry's own
`admission-status`, in the README row (stays `uncovered`), and in the round lesson's `## Gate`
line — which must state that S045's sole consumer is a rejected candidate and that **D4 therefore
remains open**, pending an admitted consumer. That is the honest "honest-stop" disposition the
round-67 spot-check itself accepted for the identical situation.

## 4 · Counterexample found in the build state: S046 is `mined` with `used-by: —`

Not part of the routed D4 text, but the same cell family and it is a **live contract violation in
the landed C2 candidate**, so it is reported here rather than left for another round.

`corpus/SOURCES.md:60` (the row the round-68 entry opens and cites at
`corpus/knowledge/round-68-apk-axml-byte-evidence.md:4`):

```
S046 NF=13 status=[ mined ] opened=[ 2026-10-24 ] recheck=[ on-release ] used-by=[ — ]
```

Contract §Field definitions makes `mined` **mean** "cited by ≥1 path in `used-by`"; a `mined` row with
`—` is internally contradictory. S046 is cited — `round-68-apk-axml-byte-evidence.md:4` opens with
"source: S046 — AXML anchor derivation … row opened round 68 by this entry's author".

**Required cell (both adjudication outcomes):**

```
corpus/knowledge/round-68-apk-axml-byte-evidence.md
```

The citation is a build-time fact and does not depend on the verdict — the round-67 precedent is
exactly this shape: round 67 set S045's `used-by` to the round-67 entry in the round that wrote it,
and left it there when that entry was later rejected (`corpus/lessons/round-67.md:79-80`). If C2
fails, the lesson logs that S046's sole consumer is a rejected candidate — the same open class as
D4 — rather than leaving the cell saying nothing.

**Why no census will ever catch this.** The registered gate (`SKILL.md:213`, §6.2) is *"mined rows
whose `used-by` paths do not exist — must print nothing"*. It iterates the paths a row *has* and
skips `—`, so a `mined` row with no path passes vacuously. Run verbatim from the lane root:

```sh
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13 {s=$9; gsub(/[[:space:]]/,"",s); if (s=="mined") {n=split($12, a, /[,;]/); for (j=1;j<=n;j++) {p=a[j]; gsub(/^[[:space:]]+|[[:space:]]+$/,"",p); if (p!="" && p!="—") print p}}}' corpus/SOURCES.md | while read -r p; do [ -e "$p" ] || echo "missing: $p"; done
```
→ prints nothing, `GATE_EXIT=0`.

The complementary detector the gate is missing (length test avoids the em-dash literal that made
`awk` choke on the encoding):

```sh
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13 {s=$9; gsub(/[[:space:]]/,"",s); if(s=="mined"){u=$12; gsub(/^[[:space:]]+|[[:space:]]+$/,"",u); if(length(u)<=3) print "MINED_WITH_NO_USED_BY:", $2, "used-by-len=" length(u)}}' corpus/SOURCES.md
```
→ `MINED_WITH_NO_USED_BY:  S046  used-by-len=1`

Registry histogram at this hash (`awk` over `$9`): `mined=38  queued=4  rejected=4` — S046 is the only
`mined` row in the no-path state, so the violation is exactly one cell wide, and no other row is
affected by this repair.

## 5 · Same class elsewhere (flagged, not in scope this round)

Pointers at rejected candidates are not unique to S045 — they are the registry's de facto convention,
which is why D4 was written as "worth a re-pointing rule" rather than a violation:

| row | status | used-by | the target's own verdict |
|---|---|---|---|
| S038 | `mined` | `corpus/knowledge/round-65-apk-axml-byte-evidence.md` | `round-65-apk-axml-byte-evidence.md:7` — `admission-status: rejected … Q02 FAIL, Q06 FAIL, Q11 FAIL` |
| S041 | `mined` | `corpus/knowledge/round-65-apk-axml-byte-evidence.md` | same file, same `rejected` verdict |
| S043 | `queued` | `—` | cited by `round-67:2` and `round-68:2`, yet `queued`/`—` (the S046 class, one verdict milder) |

S038 and S041 were **not** re-pointed when the round-67 and round-68 entries re-cited them;
`corpus/lessons/round-67.md` records the policy explicitly for re-opens: "No prior row's
status/recheck/used-by changed" (`round-67.md:80-82`). So the re-pointing rule this round adopts has
to be stated as a rule and applied deliberately, not discovered per-row: **`used-by` follows the entry
of record for that source; a re-gate replaces the superseded candidate with its successor only when
the successor is admitted, and otherwise leaves the cell and logs the open defect.** Applying it
retroactively to S038/S041/S043 is a separate (non-blocking) repair, and none of them is required by
C2's frozen predicate.

## 6 · Calibration check — the re-point cannot move C1 or C2

The `used-by` cell is invisible to the frozen counter, so neither claim can be helped or harmed by
this repair:

- `grep -n "SOURCES\|used-by\|used_by" reports/round-68/measure.py` → **no matches, exit 1**: the
  counter never opens `corpus/SOURCES.md`.
- Enumerated inputs instead: `corpus/README.md` (`measure.py:34`), the three C05 candidates
  (`:45` round-65, `:432` round-67, `:439` round-68), `corpus/live/runs/**` (`:92,120`),
  `corpus/knowledge/seed.md` + `2026-10-12-rea-readiness-checklist.md` (`:138`).

Hence `C7_*` (C1) and `K_HELD_BACKED`, `K_ROW C05 status`, `C05_SINGLE_V3`, `HOLDS_C2_V3`,
`C7_V3_CLEAN` (C2) are all invariant under this edit. The flip that case (a) requires is the
**README C05 row plus the knowledge column**, not this cell — and C2's counter already gates that
(`C05_SINGLE_V3` asserts "the C05 row's knowledge column names exactly the round-68 entry").

## 7 · Verdict

**RE-POINT-SPECIFIED.**

- Case (a), C2 passes / v3 admitted → `corpus/knowledge/round-68-apk-axml-byte-evidence.md`
  (replace; lands with the README flip; old→new logged in `corpus/lessons/round-68.md` `## Gate`).
- Case (b), C2 fails / v3 rejected → cell **unchanged**
  `corpus/knowledge/round-67-apk-axml-byte-evidence.md`; no re-point licensed; D4 remains open and
  is logged as such in the same `## Gate` record.
- Independently of both: **S046** `used-by` must become
  `corpus/knowledge/round-68-apk-axml-byte-evidence.md` (it is `mined` with `—` today, and the
  registered census is blind to that state — §4).
- `status` stays `mined` for S045 in both cases; no other cell changes; the licensing rule is
  contract §Rules 2 (only `status`, `recheck`, `used-by` change in place, each logged old→new in the
  round lesson) read with the `used-by` definition ("paths of the knowledge entries or lessons citing
  the row, comma-separated, or `—`").

No edit was made. Tool installs/updates: none (all evidence produced with `awk`/`grep`/`sed`/`sha256sum`
already on the host).
