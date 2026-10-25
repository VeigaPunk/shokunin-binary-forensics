# R69ConnectorOverlap — sibling adjacency scan of the round-69 claims

**CONTEST-NAMED** — the *province* is named and open (ADJ-06: kaidoku/revenger shipped-artifact overlap; fleet `l0-questions.md:42` still carries no `L0 ANSWER`), but of the three r69 claim subjects only the APK *noun* is contested: the AXML chunk-type anchors/enum values are **NO-OVERLAP** (0/20 lanes, 0 fleet-wide spec citations), the C05 container / dex declared-header ground is **CONTEST-NAMED at province-noun / CONTEST-UNNAMED at the byte layer**, and the new Q15 tree-identity criterion is **CONTEST-UNNAMED** (0 sibling Q15 of this class; 7 sibling lanes hold *adjacent* object-id criteria, closest is mori 93/94 — reported, not absorbed). Revenger's C1 and C2 stay inside its own province with two wording caveats (§5).

Read-only seat. Nothing written outside this file; no lane, fleet, jj or Git mutation. No install performed (no tool needed).

## 1. The province is named, and none of the three subjects is named in it

| pointer | text (verbatim excerpt) | what it names |
|---|---|---|
| `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:42` | "arbitrate the **kaidoku/revenger shipped-artifact overlap** before an ADJ-06 analysis is routed … [no `L0 ANSWER` tail; only lines 52 and 53 carry one]" | fleet-level **CONTEST-NAMED**, **unresolved** (`grep -n 'L0 ANSWER'` → 52,53 only) |
| `/home/vgpnk/Projects/shokunin/tsukuroi-shokunin/PROVINCE.md:150` | "R20-OUT009: OUT-009 is Revenger's sibling declaration … Android APKs … **It is not a tsukuroi grant of ownership. Kaidoku/Revenger arbitration remains unresolved**" | named; explicitly *not* a grant |
| `/home/vgpnk/Projects/shokunin/kaidoku-shokunin/PROVINCE.md:242,274,305` | "remain unheld/Adjacent; kaidoku/revenger arbitration is still open"; "Both live debugger verbs remain Adjacent/unheld; the kaidoku/revenger arbitration is open" | named — subject is **live debugger/dynamic-analysis verbs** |
| `/home/vgpnk/Projects/shokunin/revenger-shokunin/PROVINCE.md:3-7` | "Owns: … Android APKs …" | revenger's side of the same broad claim |

The contested subjects on record remain EVM/selector ground (kaidoku rounds 28-29) and live-debugger verbs. **No pointer names revenger for AXML, for `AndroidManifest.xml` byte layout, for a dex declared header, or for a tree-identity criterion.**

## 2. Subject A — AOSP AXML chunk-type anchors / enum values — **NO-OVERLAP**

Per-lane receipt (each lane's `corpus/knowledge/` + `SCORECARD.md`), tokens `RES_XML_|RES_STRING_POOL_TYPE|ResourceTypes\.h|RES_XML_FIRST_CHUNK_TYPE|0x0180|0x0181|0x0182`:

```
$ cd /home/vgpnk/Projects/shokunin && for d in audio chousa game-dev-2d game-dev-3d kagi kaidoku
    kake kama kasegi kengaku kotoba kotodama kumitate lore mado mori souji tabi tameshi tsukuroi; do
    h=$(grep -rlE 'RES_XML_|RES_STRING_POOL_TYPE|ResourceTypes\.h|RES_XML_FIRST_CHUNK_TYPE|0x0180|0x0181|0x0182' \
        "$d-shokunin/corpus/knowledge" "$d-shokunin/SCORECARD.md" 2>/dev/null | wc -l); printf '%-22s %s\n' "$d" "$h"; done
audio 0 · chousa 0 · game-dev-2d 0 · game-dev-3d 0 · kagi 0 · kaidoku 0 · kake 0 · kama 0 · kasegi 0
kengaku 0 · kotoba 0 · kotodama 0 · kumitate 0 · lore 0 · mado 0 · mori 0 · souji 0 · tabi 0 · tameshi 0 · tsukuroi 0
```

Fleet-wide spec-citation receipt (any file type, excluding this lane, `.git` and the fleet evidence tree):

```
$ grep -rlE 'ResourceTypes|androidfw|android\.googlesource\.com' --include='*.md' --include='*.py' . \
    | grep -v '^./revenger-shokunin/' | grep -v '/.git/' | grep -v '^./.ufo/reports/'
(no output)
```

Consequence for the r69 delta: the enum-block bounds (`:237` open, `:263` close) and the enum values the v4 entry must now *derive* are **sibling-unclaimed**. The r68 sweep result is unchanged on the r69 token set, so C1's AXML leg is still first-claim fleet-wide. One precision point for the build seats, not a contest: the **rejected** v3 entry already lists the six chunk-type values (`corpus/knowledge/round-68-apk-axml-byte-evidence.md:57` — "`0x0001` string pool, `0x0180` resource map, `0x0100` start namespace, `0x0102` start element, `0x0103` end element, `0x0101` end namespace"). The r69 delta is *derivation coverage* (the script prints them plus the `:237-:263` block), not new anchors — a claim of "new enum values" would overstate and re-open the M44 number-drift class.

## 3. Subject B — C05 APK container / dex declared-header ground — **CONTEST-NAMED (noun) / CONTEST-UNNAMED (bytes)**

kaidoku is the only lane with hits on `dex header|dex_header|header_item|classes\.dex|APK container|authored.*\.apk` in `corpus/knowledge/`+`SCORECARD.md` (**2** files, all other lanes 0), and neither hit is a byte claim:

| pointer | text | subject |
|---|---|---|
| `kaidoku-shokunin/corpus/knowledge/2026-10-13-r4u-02-jadx-decode.md:84` | "(`classes.dex`); release-only members `assets/dexopt/baseline.prof` + …" | APK **member inventory** from a real Godot APK |
| `kaidoku-shokunin/corpus/knowledge/2026-10-14-r12-01-queue-b-ready.md:50` | "`project-android-application-graph` takes `inputJson` and its contract … is the same homogeneous `inventory_evidence` feed" | **provider feed contract** |
| `kaidoku-shokunin/PROVINCE.md:56` | "`| APK surface (full) | … inspect-android-package (jadx-headless-mcp 0.7.1); decode-android-resources (apktool 3.0.3) … 1,925 classes + **full manifest decode** (r4u-02) |`" | the **noun**, by provider output |

Byte-layer fencing holds: no lane carries an authored APK fixture at all —

```
$ find . -maxdepth 5 -name '*.apk' -not -path './.git/*'
./revenger-shokunin/corpus/fixtures/apk-r65/fixture.apk
```

so the C05 v4 subject (one authored 947-byte APK's binary-AXML chunk walk and `classes.dex` `header_item` fields against an authored oracle; `corpus/knowledge/round-69-apk-axml-byte-evidence.md` header lines `source: S038/S043/S045/S047/S041`, `coverage-map: C05`, `admission-status: candidate`) is untouched fleet-wide. r68's partition argument stands verbatim and no sibling closed the gap.

## 4. Subject C — Q15 tree-identity criterion — **CONTEST-UNNAMED**

New surface this round (r68 scanned the C7 gate concept, not a criterion row). Four receipts:

**(a) The label `Q15` is a lane-local namespace, empirically.** Six sibling lanes carry a `Q15` row and all six mean different things — the label carries no cross-lane meaning, so reuse cannot be a contest:

```
$ grep -rn '^| Q15' */corpus/QUALITY.md
audio-shokunin/corpus/QUALITY.md:23        generated work-products stay under corpus/live/<round>/
game-dev-2d-shokunin/corpus/QUALITY.md:27  seat write scope + orphan disposition
game-dev-3d-shokunin/corpus/QUALITY.md:26  documentation reproduces its stated result
kotoba-shokunin/corpus/QUALITY.md:26       an honest stop names its blocker
revenger-shokunin/corpus/QUALITY.md:27     a stated git object id or tree identity is re-derived …   ← new this round
souji-shokunin/corpus/QUALITY.md:39        /dev/shm second device …  [WITHDRAWN by Q16, :40]
```

**(b) souji's Q15 is the precedent to satisfy, and revenger's does.** `souji-shokunin/corpus/QUALITY.md:40` supersedes it: "Q16 — Supersedes Q15 — WITHDRAWN. Q15's only lesson pointer was the K5 admission it was written for (**circular**; orchestrator review, 2026-10-19)". Revenger's row cites `M48 (lessons/round-69.md)`, and M48 is the r68 D1 **defect** (`corpus/lessons/round-68-verifier-spotcheck.md:171-177`, the false `1c34603:corpus` identity sentence), i.e. a defect independent of the C05 admission the criterion serves — non-circular by souji's own test.

**(c) Red-before is sound on this surface.** `git show 222a7a7:corpus/QUALITY.md | grep -E '^\| ?Q1[4-6]'` returns **only Q14** — Q15 was absent at the claim base, so `Q15_PRESENT=no` in `reports/round-69/measure-before.log` is a true red-before (the working tree carries the row uncommitted, as the milestone's build state requires).

**(d) Seven sibling lanes hold *adjacent* object-id criteria; none claims this class.** Named, so no seat can later present Q15 as fleet-novel:

| pointer | what it holds | relation to revenger Q15 |
|---|---|---|
| `mori-shokunin/corpus/QUALITY.md:672` (crit. 94, supersedes 93) | "the receipt's gate blob equals `git rev-parse F:<gate>`" | **CONTEST-UNNAMED** — object-id resolution, subject = one gate blob, not prose identity sentences |
| `mori-shokunin/corpus/QUALITY.md:642-643` | `blob = sh("rev-parse", R+":"+p)`; `frozen = … sh("rev-parse",added+":"+p) == blob` | the **exact operation** whose absence produced r68 D1; mori has it as a checker, revenger lacked it |
| `mori-shokunin/corpus/QUALITY.md:93-94` | 93 was voided because "criterion 93 **cannot fail** on its stated property" | the failability defect class revenger's `Q15_SELFTEST` + `Q15_FALSE_KILLED` legs exist to avoid — same class as D5 |
| `kake-shokunin/corpus/QUALITY.md:870(d),:903(f)` + `.ufo/waves/round-36/criteria/control_tree_check.py` | "Bind the **tree identity**/listing to the control artifact"; checker accepts `ls -la` or `git ls-tree` listing, rejects key paths | **CONTEST-UNNAMED** — tree identity bound to a *key-free control build*, not to a stated hash sentence |
| `tameshi-shokunin/corpus/QUALITY.md:861` (crit. 73) | mutant control "names and verifies the counter revision, **input-tree identity**, and explicit control mode" | **CONTEST-UNNAMED** — counter-control provenance |
| `game-dev-2d-shokunin/corpus/QUALITY.md:21` (Q9) | "The verdict cites the **blob SHA** it ran"; `:55` `git rev-parse HEAD:<path>` | blob pinning inside one verdict |
| `kotoba-shokunin/corpus/QUALITY.md:47` (Q36) | a receipt "names the revision it measured in the receipt itself (a printed `git rev-parse HEAD` …)" | revision naming, not object equality |
| `mado-shokunin/corpus/QUALITY.md:174` (crit. 27) | anchor reproducible via "a content-addressed object id" | anchor reproducibility |
| practice pool: `kake-shokunin/corpus/lessons/round-34-verifier-spotcheck.md:38`; `kama-shokunin/corpus/lessons/round-36-verifier-spotcheck.md:68` | `git rev-parse <rev>:corpus/SOURCES.md` / `…:corpus/lessons/round-35.md` used to prove blob identity across commits | 2 of 20 lanes already *practise* the derivation; neither has a criterion row |

## 5. Do the claims stay inside revenger's province? — **Yes, with two wording caveats**

- **C1 (AXML anchors, enum values, C05 byte ground):** inside. Zero sibling claim at the byte layer (§2), zero sibling authored APK fixture (§3), and S047 is own-work while S038/S045/S032/S034/S041 are upstream specs — no sibling knowledge is used as support. The only contest is the *noun* (APK), which is exactly what ADJ-06 left open.
- **C2 (Q15):** inside, but **scoped**: revenger may claim the *sentence-level* criterion (a stated `X:corpus` identity resolves under `git rev-parse X:corpus`). It may **not** claim fleet novelty for "re-deriving tree identity" — mori `:642-643/:672` and kake's `control_tree_check.py` already hold the mechanism in other subjects, and two lanes practise it in lessons. The frozen claim text does not overstate; a seat writing C2 up as new fleet capability would be taking mori's/kake's ground.
- **Carried, still unfixed (r68 §4, unchanged):** `grep -ci kaidoku revenger-shokunin/PROVINCE.md` → **0**; `grep -ci 'ADJ-06' revenger-shokunin/PROVINCE.md` → **0**, while kaidoku `PROVINCE.md:66-71` already routes by revenger's r1 connector. Every AXML/C05 round widens this one-sided split. A r69 C05 flip would be the fourth such round (r61, r63-64, r68). **Reported, not applied:** `PROVINCE.md` is outside `claims.md`'s declared change surface (C1 = entry + README row + script + S047; C2 = QUALITY row + lesson + checker + fixture), so editing it would be a void-condition risk.

## 6. Risks

- **Novelty overstatement on AXML (§2):** the v3 file already lists the six values; only the derivation coverage is new. "Every S038 line" phrasing is exactly what claims.md item 2 bounds to "the numbers the command prints" — keep it.
- **Novelty overstatement on Q15 (§4d):** mori/kake/tameshi hold the mechanism; revenger holds the criterion over prose sentences. Presentation risk, not priority.
- **Checker pointer absent at scan time:** `claims.md` §C2 names "the committed checker" but `ls reports/round-69/` shows only `claims.md`, `d1-false-sentence.md`, `measure-before.log`, `measure.py`. The Q15 build seat must land it and its self-test before `Q15_SELFTEST`/`Q15_FALSE_KILLED` are evaluable — a build-state dependency, not a defect.
- **Label false friends:** kaidoku's `SCORECARD.md:411` "C05 inverted the authority question" is kaidoku's *claim id* C05 (discernment), not revenger's coverage row C05; `kama-shokunin/SCORECARD.md:348,354` "KQ15" is a different label family. Neither is same-ground.
- **Fleet evidence-tree false positive:** `/home/vgpnk/Projects/shokunin/.ufo/reports/round-6*/revenger.md` holds **revenger's own** report text (round-68 copy: 20,558 B, sha256 `3fb7057eac599cc36382c29a69bb01ee3d972ec07122172c5a4ecaf9ecfb34c0`). A fleet-wide AXML sweep hits revenger prose there; it is not sibling evidence and must not be counted as corroboration.
- **Silence is not proof:** receipts cover 20 sibling lanes' `corpus/knowledge/` + `SCORECARD.md` + fleet-wide `*.md`/`*.py` sweeps. Unindexed synonyms, binaries, `.git` history and other lanes' `.ufo/` scratch are outside the receipt.

## 7. Axes

- **Adjacency (this seat's axis):** improved — three subjects with fresh r69 receipts, the first scan of the Q15/tree-identity surface fleet-wide, and the mori-93 failability precedent recorded against the D5 class.
- **Coverage (C1):** unaffected by this report; the added finding is that no sibling pre-owns the enum anchors or the dex-header bytes, which strengthens the admission basis without touching the counter.
- **Calibration (C2):** unaffected; the added finding is that the Q15 label is lane-local (6 distinct Q15s) and its lesson pointer is non-circular by souji's Q16 test.
- **No axis harmed:** no file outside this report written, no counter or claim text changed.

## 8. Tooling

No install or upgrade performed; pacman transactions paused host-wide and not needed. Commands used were stock `grep`/`find`/`sed`/`awk`/`sha256sum` plus read-only `git show`/`git log`/`git status`.
