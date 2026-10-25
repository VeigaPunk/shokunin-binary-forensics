LEDGER-BROKEN — every §C1/§C2 do-nothing number matches the committed receipt and the cited anchors verify, but three ledger defects hold: (F1) the frozen separability sentence is false against the frozen counter — C1's pass branch requires `HOLDS_OK_V6`, which reads C2's artifact; (F2) C2's universal "every spec line number derived" is falsified by the landed entry at lines 237 and 244, and no frozen conjunct reads that property; (F3) the registered gate row (`SKILL.md:268`) still asserts the attribution marker "can never fire", the opposite of the landed gate's measured behavior.

seat: `L1Revenger68.R68RevengerLedger` (leaf, read-only, no subagents) · date 2026-10-25 · round 68
scope: `reports/round-68/claims.md`, `reports/round-68/measure-before.log`, `reports/round-68/measure.py`,
`corpus/check_embedded_outputs.py`, `corpus/knowledge/round-68-apk-axml-byte-evidence.md`,
`corpus/derive_axml_anchors.py`, `corpus/snapshots/ResourceTypes.h`, `corpus/README.md`, `SKILL.md`,
`corpus/lessons/round-67-verifier-spotcheck.md`. Nothing edited; every command below was run read-only
(the three behavioural replays write only under `/tmp`).

Instrument integrity first:

```
$ sha256sum reports/round-68/measure.py corpus/snapshots/ResourceTypes.h
0de4eb6f34bdb906fb69fdd173aaac9bcef629e6ff1d4c67f5ba8c91093f7766  reports/round-68/measure.py
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  corpus/snapshots/ResourceTypes.h
$ stat -c '%s' corpus/snapshots/ResourceTypes.h
86255
```

Both digests equal the pins in `claims.md:4-7` and `measure-before.log:101-102`. `git rev-parse HEAD`
= `4232235723cf8d4731a1e7e78ca098b8af953a57`; `git diff --stat f165908 -- SKILL.md corpus/README.md`
is empty (0 lines), so both registry texts are still the base bytes.

---

## 1 · Numbers: §C1 / §C2 do-nothing controls vs the receipt — **HOLDS**

Every value `claims.md` asserts for the base tree was compared to `measure-before.log` line-by-line:

| claims.md | asserted | receipt line | receipt value | verdict |
|---|---|---|---|---|
| `:81` | `C7_GATE_PRESENT=yes` | 68 | `C7_GATE_PRESENT=yes` | MATCH |
| `:81` | `C7_SELFTEST=pass` | 69 | `C7_SELFTEST=pass :: SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired` | MATCH (claims omits the `::` tail) |
| `:81` | `C7_CONTROL_PASS=1/1` | 75 | `C7_CONTROL_PASS=1/1` | MATCH |
| `:82` | `C7_MUTANT_KILLED=1/1` | 71/76 | `c7 exit=1 killed` → count 1 at `C7_MUTANT_KILLED=1/1` | MATCH |
| `:82` | `C7_MUTANT_KILLED_ATTRIBUTED=0/1` | 77 | `C7_MUTANT_KILLED_ATTRIBUTED=0/1` | MATCH |
| `:83` | `C7_NEG_SPOOF_KILLED=1/1` | 79 | `C7_NEG_SPOOF_KILLED=1/1` | MATCH |
| `:83` | `C7_NEG_SPOOF_KILLED_ATTRIBUTED=0/1` | 80 | `C7_NEG_SPOOF_KILLED_ATTRIBUTED=0/1` | MATCH |
| `:56` | `C7_RED_ON_R65_CANDIDATE=yes` | 72 | `C7_RED_ON_R65_CANDIDATE=yes exit=1 :: checked_blocks=15 problems=1` | MATCH |
| `:84` | `HOLDS_OK_V5=no` | 97 | `HOLDS_OK_V5=no` | MATCH |
| `:84` | `HOLDS_OK_V6=no` | 98 | `HOLDS_OK_V6=no` | MATCH |
| `:133` | `K_HELD_BACKED=8/14` | 4 | `K_HELD_BACKED=8/14` | MATCH |
| `:133` | `K_HELD_BACKED_STRICT=8/14` | 6 | `K_HELD_BACKED_STRICT=8/14` | MATCH |
| `:134` | `K_ROW C05 status=uncovered` | 2 | `K_ROW C05 status=uncovered` | MATCH |
| `:134` | `C05_SINGLE_V3=no` | 9 | `C05_SINGLE_V3=no` | MATCH |
| `:134` | `HOLDS_C2_V3=no` | 15 | `HOLDS_C2_V3=no` | MATCH |
| `:135` | `C7_V3_CLEAN=n/a (no v3 file)` | 74 | `C7_V3_CLEAN=n/a (no v3 file)` | MATCH |
| `:29` | `K_HELD` 8/14, score 5.7 | 1 | `K_HELD=8/14 score=5.7` | MATCH |
| `:4` | base `f165908aaffcf14798de53405fe788986bd33ff9` | 101 | `base commit: f165908aaffcf14798de53405fe788986bd33ff9` | MATCH |

Claims-side forecasts also reproduce on the landed tree: `claims.md:121` "17 blocks, 0 problems" →
`python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-68-apk-axml-byte-evidence.md`
→ `checked_blocks=17 problems=0`, exit 0; the derivation's 17 printed lines (`entry:4`, `entry:194`)
→ `python3 -B corpus/derive_axml_anchors.py` prints exactly 17 lines. No number in §C1/§C2 is
unsupported by the receipt.

Anchors in the candidate are correct, not off-by-one (this is the r67 mode, checked first):

```
$ awk 'NR>=236 && NR<=238 || NR==244 || NR==245 {printf "%d:%s\n", NR, $0}' corpus/snapshots/ResourceTypes.h
236:
237:enum {
238:    RES_NULL_TYPE                     = 0x0000,
244:    RES_XML_FIRST_CHUNK_TYPE          = 0x0100,
245:    RES_XML_START_NAMESPACE_TYPE      = 0x0100,
$ awk 'NR>=686 && NR<=687 {printf "%d:%s\n", NR, $0}' corpus/snapshots/ResourceTypes.h
686:    // Byte offset from the start of this structure where the attributes start.
687:    uint16_t attributeStart;
```

`claims.md:102-105` (`:245` both places, comment `:686`, field `:687`) is exactly what the pinned bytes
say; `grep -c ':244'` on the v3 entry returns 2 and both are the correction sentences (entry:6,
entry:9), not live anchors. The r67 off-by-one is genuinely repaired.

---

## 2 · F1 — BROKEN: the frozen separability sentence is false against the frozen counter

`claims.md:34-37` (frozen, before any seat scored):

> The two claims are causally separable … C1 changes only `corpus/check_embedded_outputs.py` and the
> counter's new C7 labels; C2 changes only a new knowledge entry plus one README row. **Neither
> counter reads the other's artifact** (C1's counter labels read the gate file; C2's aggregate reads
> the README row and the knowledge column).

`claims.md:57` puts `HOLDS_OK_V6=yes` inside C1's frozen pass predicate. `reports/round-68/measure.py:525-527`:

```
holds_ok_v6 = (holds_ok_v5 and c7_neg_killed == 1 and c7_neg_attributed == 0
               and c7_v3_clean)
```

and `c7_v3_clean` is set only by running the gate over **C2's file**, `measure.py:439-444`:

```
v3 = TREE / "corpus/knowledge/round-68-apk-axml-byte-evidence.md"
...
rc, last = run(TREE, C7_GATE_REL, "--entry", "corpus/knowledge/round-68-apk-axml-byte-evidence.md")
c7_v3_clean = rc == 0
```

Consequence: C1 cannot read `HOLDS_OK_V6=yes` unless the round-68 knowledge entry (C2's only new
artifact) is clean under the gate — so an unclean or absent v3 candidate forces C1's predicate false
(`HOLDS_OK_V6=no`, exactly the base reading at `measure-before.log:98`). The reverse coupling is
explicit too: C2's predicate carries `C7_V3_CLEAN=yes` (`claims.md:121`), a C7-gate label. One C2 byte
defect therefore falsifies both axes at once, which is precisely the causal attribution the round is
built on. The counter, not the prose, is authoritative here, and it contradicts the sentence.

Secondary in the same sentence: "C2 changes only a new knowledge entry plus one README row" is not what
the build diff shows — `git diff --stat f165908` (HEAD `4232235`) names `corpus/SOURCES.md`,
`corpus/derive_axml_anchors.py`, `corpus/snapshots/ResourceTypes.h` as well.

---

## 3 · F2 — BROKEN: C2's universal derivation claim is falsified by the landed entry, and no frozen conjunct reads it

Frozen prose, `claims.md:96`: "with **every** spec line number derived by a committed script from the
pinned snapshot instead of transcribed". Entry, `corpus/knowledge/round-68-apk-axml-byte-evidence.md:125`:

> 11. Every S038 line number this entry states is printed by a committed derivation script … **no spec
> line number in this entry is transcribed by hand.**

Mechanical cross-check of every line-number citation in the entry against the derivation's own output:

```
$ python3 -B corpus/derive_axml_anchors.py        # 17 lines, 16 symbols
sha256 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f ResourceTypes.h
struct ResChunk_header : 218 ... field attributeStart : 687
$ (cross-check) cited: ['5','7','8','218','237','239','241','244','245','246','247','248','253','287','461','612','677','686','687','707']
  NOT derived: ['5','7','8','237','244']
    entry:1,57,148,157  'lines 237-253' -> 237 :: chunk-type enum block
    entry:148           'line 244'      -> 244 :: line 244 is RES_XML_FIRST_CHUNK_TYPE
```

(The `5`/`7`/`8` hits are the S043 row's different snapshot and its quoted round-65 error, outside the
S038 universal.) So two **S038** line numbers the entry states are not printed by
`derive_axml_anchors.py`: `237` (the enum block's opening line, cited in four places as the range start)
and `244` (`RES_XML_FIRST_CHUNK_TYPE`, stated at entry:148 as the contrasting symbol). Both values are
*correct* (`237:enum {`, `244:RES_XML_FIRST_CHUNK_TYPE` above), so this is not a wrong anchor — it is a
false completeness assertion, and the script's symbol tables (`derive_axml_anchors.py:84-92`) contain no
`RES_XML_FIRST_CHUNK_TYPE` predicate to derive 244 at all.

No frozen conjunct tests the property: `C7_V3_CLEAN` only re-checks the entry's embedded **output
blocks** verbatim (`check_embedded_outputs.py:88-107`, 17 blocks/0 problems), `HOLDS_C2_V3`
(`measure.py:114-117`) reads only README row/column state. The entry's own Q-map then self-certifies the
universal: `entry:182` `| Q11 | pass | … the spec line numbers carry their deriving command and output
(item 11, machine-derived, not transcribed) |`. That is the r67 M40/M44 shape — an anchor claim not
carried by its derivation — with an instance already in the landed file, and the pass branch leans on a
Q row authored by the same entry.

---

## 4 · F3 — BROKEN: the registered gate row still states the opposite of the landed behavior

`claims.md:23` names the defect being repaired as the gate's "**registered** attribution" being false.
`SKILL.md:268` is unchanged since `f165908` (`git diff --stat f165908 -- SKILL.md` empty) and still says:

> **correction 2026-10-24 (r67 adjudication):** the trailing forged-drift control's marker `drifted
> entry output accepted` is structurally shadowed by that earlier require and **can never fire** — seats
> `R67ReviewC7Gate`/`R67MutC7Kill`/`R67CriticC7Claim`; recorded limitation, **reorder fix routed**

The landed gate fires it, measured by replaying the counter's own frozen mutations (`measure.py:385-397`
mutant clause, `:460-470` spoof clause) on a copy of the landed corpus:

```
$ python3 -B A.py --self-test          # mutant only
MUTANT exit= 1 last= 'drifted entry output accepted' attributed= True
$ python3 -B B.py --self-test          # mutant + spoofed MARKER
SPOOF  exit= 1 last= 'drifted entry output accepted (spoofed)' attributed= False
```

Both clauses match exactly once; the marker is the last line only in the unspoofed case. So C1's
mechanism is real and is **not** another shadow (that part of the repair holds), but the lane's
authoritative registry now mis-describes its own instrument, and C1's pass branch has no conjunct
requiring the row to be reconciled — only the **kill rule** says the row is corrected (`claims.md:77-78`).
r67's closure's own standard was that no false attribution be left standing; the false attribution is
left standing, inverted. `SKILL.md:270` (`measured-against`) likewise still pins the round-**67** counter
and its sha.

---

## 5 · Minor findings (not load-bearing, but precision debts)

- **M1 — `C7_CONTROL_PASS` is non-discriminating.** `measure.py:408`
  `c7_control_ok += c7_selftest_ok and C7_MARKER in c7_gate.read_text(...)` is a content-presence check,
  so it reads `1/1` on the base tree where the marker is dead code (`measure-before.log:75`) — the exact
  "text present ≠ reachable" premise of r67's M45. It is inside C1's pass predicate (`claims.md:50`).
  Mitigation: the load-bearing conjunct `measure.py:428` is behavioural (`last.endswith(C7_MARKER)`), so
  C1 does not rest on it; the label's name still overstates what it checks.
- **M2 — "exactly these deltas" is not literal.** `claims.md:100` enumerates six deltas; the v2→v3 diff
  (`git show f165908:corpus/knowledge/round-67-...md` vs the v3 file) additionally rewrites
  `verified-at`, `recheck`, the chunk-type sentence, item 8, the Q11 map row, the Observation bullet and
  the Reproduce paragraph, and adds the S046 source row. No frozen conjunct reads the delta set (the
  S046 row is separately registered in "Frontier step"), so this is prose overstatement, not a scoring
  path.
- **M3 — base-relative pointer unlabelled.** `claims.md:23` cites `check_embedded_outputs.py:132-134`
  and `:141`. Verified line-for-line **on base `f165908`** (`git show f165908:…`: 132-134 is the
  `require(… "self-test: drifted entry not caught")`, 141 is `require(not ok(dproblems), MARKER)`); on
  the tip those lines are the repair's comment block and `:144` is `print(MARKER)`. Round-67's lesson
  was exactly "a resolvable pointer at closure"; the pointer resolves only against the base commit named
  in `claims.md:4`.
- **M4 — void-condition ambiguity.** `claims.md:176` lists "attributed calibration counts below target
  (… C7 1/1)" in a list whose only time-qualified clause is "counter exit non-zero **at final**". On the
  base tree `C7_MUTANT_KILLED_ATTRIBUTED=0/1` (`measure-before.log:77`), so a literal reading voids the
  round at pre-registration. The intended reading (final-tree only) is implied by the do-nothing-control
  section but is not stated for this clause.
- **M5 — receipt invocation is ref-based.** `measure-before.log:102-104` records `git archive
  refs/heads/main corpus`; the footer pins `f165908`, which is what the receipt must be replayed against
  (main is now `4232235`). Re-derivable, but by the footer's hash, not the recorded command.

---

## 6 · Checked and clean (negative results, so the wave does not re-litigate them)

- Counter column index is **correct**: `README.md` columns are `| row | surface | knowledge entries |
  work evidence | status |`; `measure.py:41-42` and `:61-63` read `l.split("|")[3]` = the knowledge
  column. Base C05 knowledge column is `—`, so `C05_KNOWLEDGE_COLUMN=-` (`measure-before.log:7`) is
  right, and `C05_SINGLE_V3=yes` is satisfiable by writing the one v3 path there — no off-by-one column
  defect.
- README C05 row is **not flipped**: `corpus/README.md:34` still `… | uncovered |`, knowledge column
  `—`; `corpus/README.md` is byte-identical to `f165908`. No void condition on the README status fires.
- `K_HELD_BACKED`/`STRICT` semantics are meaningful: both count held rows whose knowledge column names
  an existing file (`measure.py:41-42`, `:61-63`); base 8 held rows (C01, C04, C06, C07, C09, C11, C12,
  C13), no rejected-marked entry among them.
- The derivation script is honest about what it checks: snapshot path is script-relative
  (`derive_axml_anchors.py:74`), digest pinned and hard-failing (`:78-80`), `find_unique` exits 2 on
  missing/ambiguous (`:58-60`, `:64-70`) — so claims item 3's exit-2 contract (`claims.md:106-109`) is
  real; the defect is only that two stated line numbers are outside its symbol list (F2).
- The mutant/spoof clauses are unique (`len(findall)=1` each) exactly as `claims.md:60-70` requires.
- Gate still red on the r65 candidate (`exit=1 :: checked_blocks=15 problems=1`), i.e.
  `C7_RED_ON_R65_CANDIDATE=yes` survives the repair.

---

## 7 · r67 failure-mode map (the question asked)

| r67 mode | recurs in r68 pre-registration? | where |
|---|---|---|
| shadowed marker (presence mistaken for reachability) | **partly** — the gate is repaired and behaviourally verified (§4), but `C7_CONTROL_PASS` is still a content check (M1) and the registry still says "can never fire" (F3) | `measure.py:408`; `SKILL.md:268` |
| off-by-one anchor | **no** on the cited table (`245`/`686`/`687` verified); **yes** as an un-derived anchor set — `237`, `244` stated, not derivable | entry:1,57,148,157; §3 |
| predicate weaker than prose | **yes** — separability (F1), "every spec line number" (F2) | `claims.md:34-37`, `:96` |
| assertion with no resolvable pointer | **no** new one in claims (all §C1/§C2 numbers resolve); `SKILL.md:268` is resolvable but **false** | §1, F3 |

confidence: numbers/matches and the two behavioural replays are directly observed (high). F1 is a
code-path read of the frozen counter plus the frozen predicate (high; no execution ambiguity). F2 is a
mechanical set difference between the entry's citations and the script's actual stdout (high); severity
is judgement — the values are right, the universal is wrong (high certainty, medium impact). F3 is a
byte comparison plus a replay (high).

attestation: no file outside `.ufo/waves/round-68/R68RevengerLedger.md` was written; no git/jj mutation,
no subagent, no message to another seat; no tool installed or upgraded; `/home/vgpnk/Projects/shokuknow`
untouched.

---

## 8 · Environmental note (not a claim defect, but a live void-condition risk)

`git status --porcelain` at 03:34 shows an untracked `corpus/__pycache__/check_embedded_outputs.cpython-314.pyc`
(directory mtime `2026-10-25 03:29:00 -0300`, 9356 B). It is **not** attributable to this seat: every
script I executed used `python3 -B`, my inline replays imported only the standard library, and running
a module as `__main__` does not write a `__pycache__` entry — only an `import` of it does, which I never
performed. The wave has 60+ concurrent seats touching this gate, so the writer is most likely another
seat importing it for unit inspection.

Consequence to flag for settlement: `claims.md` §Void conditions names `corpus/snapshots/` as "the only
new corpus path", so **committing** this `.pyc` would create a second new corpus path and trip that
void clause. The frozen measurement is unaffected (`git archive <commit> corpus` never sees untracked
files), so no number in §1 moves — but the file must stay untracked/removed before the measured commit,
and the seat that created it should record itself in its own report.
