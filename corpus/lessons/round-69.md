# round 69 — revenger (hyaku run 6)

Round 69 declared two claims (`reports/round-69/claims.md`, frozen at `e1d22caaf9a2fdc4c1c13d1f4a8a6813e7b07968`
against base `222a7a702529fb60598633ebdf5e1442007bc15d`, counter `reports/round-69/measure.py` sha256
`bca74e6d8b5010aee79886521474f072257ee22ec7ccc24e4186666bdc048377`):

- **C1 — coverage, K (lowest non-retired criterion, 5.7): the C05 fourth-pass re-gate with the complete
  round-68 routed repair bundle.** **Verdict: FALSIFIED** on four named wave decisions over the landed v4
  bytes: Q05 (`R69ReviewEntryQ05`), Q07 (`R69ReviewEntryQ07`), Q14 (`R69ReviewEntryQ14`), Q15
  (`R69ReviewEntryQ15`). Kill rule executed: the README C05 row stays `uncovered`, the v4 entry's
  `admission-status` flipped `candidate → rejected` with every other byte kept, `K_HELD_BACKED` stays 8/14.
- **C2 — calibration: the Q15 tree-identity criterion and the D1 restatement.** The criterion row landed
  (`corpus/QUALITY.md:27`) and its checker behaves as specified on the legs a seat ran by hand
  (`--self-test` exit 0; the D1 fixture scan exit 1; a true restatement scan exit 0 —
  `R69Q15CheckerRun`, `R69D1RestateCheck`), but **the frozen counter cannot evaluate it**:
  `reports/round-69/measure.py:158` calls `run(...)` at module level while `def run` is at `:187`, so any
  tree carrying `corpus/q15_tree_id_check.py` dies `NameError` with exit 1 before the C7/Q15/hold block.
  `Q15_SELFTEST`, `Q15_FALSE_KILLED`, `Q15_RESTATE_OK`, `C7_V4_CLEAN` and every `HOLDS_OK*` label are
  therefore unreachable with the pinned instrument. **Verdict: FALSIFIED — honest stop, instrument defect
  reported as measured, not repaired after scoring** (kumitate r42: a rule or instrument changed after a
  seat has scored is not the claim's rule).

The round's own frozen void conditions fired and are recorded, not hidden: "counter exit non-zero at
final" (`claims.md:193`) and "`HOLDS_OK_V4/V5/V6` not yes". `HOLDS_OK_V6` also reads `no` for an
independent reason the build caused: extending `corpus/derive_axml_anchors.py` in place changed seven
enum lines the retained round-68 candidate embeds verbatim, so `C7_V3_CLEAN` went `yes → no` (7 drift
lines) while the round-68 candidate's own bytes are unchanged (`R69HoldSweep`, `R69ReadmeFlipCheck` J,
`R69CriticC7Claim` (b)). Both are reported; neither target was narrowed and no acceptance condition was
repaired.

## Gate

### Source rows opened this round (CORPUS.md rule 1: URL or command, access date, located quote)

- **S047 (new row this round, own-work, tier A; supersedes S046).** What was opened:
  `corpus/derive_axml_anchors.py` (sha256 `74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa`)
  run over `corpus/snapshots/ResourceTypes.h` (sha256 `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f`,
  86255 bytes). Access date **2026-10-25**, re-run by this L1, by `R69AnchorDerive`, `R69AnchorBlind`,
  `R69SpotcheckDiscern` and `R69ReviewSourcesS047`. Located quote (≤ 25 words), from the script's own
  stdout: `enum RES_XML_START_NAMESPACE_TYPE : 245 = 0x0100`. The row's script digest, 20-line count and
  snapshot digest all re-derive; `R69ReviewSourcesS047` ruled ROW-CLEAN (11 columns, no `|` in any cell,
  supersedes is a verified strict superset: old 17 lines ⊂ new 20, new-only `244/237/263`).
- **S038 (existing row, re-opened this round).** Opened from the committed snapshot copy, not the network:
  line 237 = `enum {`, 244 = `RES_XML_FIRST_CHUNK_TYPE = 0x0100,`, 245 = `RES_XML_START_NAMESPACE_TYPE = 0x0100,`,
  263 = `};`. Access date **2026-10-25**. Located quote: `RES_XML_START_NAMESPACE_TYPE      = 0x0100,`.
- **S045 (existing row).** Not re-fetched; the committed snapshot
  `.ufo/waves/round-67/source-snapshots/dex-format.html` (`c0428612…`) was re-hashed and its four quoted
  clauses re-located by `R69ReviewEntryQ01`. Access date **2026-10-25**. Located quote:
  `must be 0x70 (112) bytes (v40 or earlier)`.

Registry changes (append-only fields, logged old → new):

| row | field | old | new | reason |
|---|---|---|---|---|
| S047 | (new row) | — | `mined`, opened `2026-10-25`, `on-release`, used-by `corpus/knowledge/round-69-apk-axml-byte-evidence.md` | the round-69 entry cites it at `:6`; appending it without a consumer would have raised census `W03`, so the row and the entry landed in the same commit (`da02261`) |
| S046 | (unchanged) | `mined`, used-by round-68 entry | **unchanged** | superseded by S047 under rule 2; supersession is not rejection, and the round-68 entry keeps every byte |
| — | `## Search log` | — | one appended 2026-10-25 note (S047, id-note: the package's staged S047 space is not adopted) | SOURCES contract rule 5 |

Census before → after (fleet `scripts/sources-census.sh`, the specification in `CORPUS.md`):

```sh
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger
# round start (before any round-69 registry edit): exit 0
revenger	W04	S024 duplicate url www.rfc-editor.org/rfc/rfc3227.txt across scopes
revenger	W04	S028 duplicate url github.com/ethereum/execution-specs/tree/v2.20.0/src/ethereum/forks/osaka/vm across scopes
revenger	W04	S029 duplicate url tc39.es/ecma262 across scopes
revenger	W04	S034 duplicate url pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT across scopes
revenger	ok	/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md
```

```sh
# round end (after the S047 append): exit 0
revenger	W04	S024 duplicate url www.rfc-editor.org/rfc/rfc3227.txt across scopes
revenger	W04	S028 duplicate url github.com/ethereum/execution-specs/tree/v2.20.0/src/ethereum/forks/osaka/vm across scopes
revenger	W04	S029 duplicate url tc39.es/ecma262 across scopes
revenger	W04	S034 duplicate url pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT across scopes
revenger	ok	/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md
CENSUS_EXIT=0
```

Rows 46 → 47 (`census`: `rows 47`, tier A 45 / C 2, mined 39 / queued 4 / rejected 4, missing 0); the
round-68 `W03` stays clear and the four disclosed `W04` duplicate-scope warnings are unchanged.

### Admission decisions (QUALITY.md criteria Q01–Q15)

- `corpus/knowledge/round-69-apk-axml-byte-evidence.md` — **REJECTED.** Failing criteria on the landed
  bytes:
  - **Q05** (`R69ReviewEntryQ05`) — `:127` credits the derivation's refusal branch ("a missing or ambiguous
    symbol is exit 2") with no probe anywhere in the entry, and on the committed snapshot that branch is
    unreachable anyway: the digest pin (&:107-108) fires first. The identical sentence was routed in round 68
    (`R68ReviewEntryQ05.md:110-131`) and survived into v4 unchanged.
  - **Q07** (`R69ReviewEntryQ07`, corroborated by `R69Item8`) — `:91` says the start-namespace chunk
    "resolves" the `0xffffffff` namespace index on the android-carrying attributes; the readout's actual
    path is `readout.py:211` `strings[ans]` on a raw `ns_index` of **0**, and `:178-184` emits the
    namespace chunk as a separate fact that nothing consults. Wrong value, wrong mechanism.
  - **Q14** (`R69ReviewEntryQ14`) — `:48` states a byte count on an ellipsis-truncated run ("a 15-byte
    `4d616e696673742d…` pair": 16 hex chars = 8 bytes) and calls the printed 16-byte pair "9 bytes".
    Q14's own reject rule, reproduced inside the entry that added the sweep.
  - **Q15** (`R69ReviewEntryQ15`) — `:8` states a git object id ("unchanged since `c7b7cf98`") with no
    deriving command, and the §Q-map has no Q15 row at all.
  - **Q08** (`R69ReviewEntryQ08`, applying the Q11 rule it supersedes) — `:30` states the EOCD signature
    `504b0506` while `--fact eocd` prints no signature bytes at all (`grep -c 504b0506` on the real stdout
    = 0) under a framing that says every numbered item is readout-produced. The round-68 Q11 seat named
    this exact repair and v4 did not apply it.
  - **Q11** (`R69ReviewEntryQ11`) — `504b0506`, the 46-byte/30-byte ZIP fixed widths and the "agrees with
    the oracle on every shared field" sentence carry a value with no in-entry derivation and no
    `recorded` label; all three are numerically correct, which is precisely Q11's reject shape. The v3's
    underived enum lines are genuinely repaired (50/50 embedded output lines match the live stdout).
  - Passing on **Q01** (`R69ReviewEntryQ01`: every cited row tier A, S047 landed with the entry),
    **Q02** (`R69ReviewEntryQ02`: header complete, every row and digest resolves),
    **Q03** (`R69ReviewEntryQ03`: every value re-derived from bytes/spec/pin, nothing copied from the
    oracle it compares against), **Q04** (`R69ReviewEntryQ04`: manual labels present and true, derivation
    credit bounded to the 20 printed lines; residual: `readout.py:49-50` still asserts "computed here …
    not assumed"), **Q06** (`R69ReviewEntryQ06`: fixture re-built byte-identical from the pinned
    generator), **Q09** (`R69ReviewEntryQ09`: all six pins re-derive, no origin/authenticity claim),
    **Q10** (`R69ReviewEntryQ10`, `R69CriticEntryScope`: SCOPE-CLEAN, ADJ-06 at an open pointer),
    **Q13** (`R69ReviewEntryQ13`: deletion detected in every credited class); **Q12** is `n/a` with a
    named reason (`R69ReviewEntryQ12`: no rejected-sources row is written).
  - **§Q-map regression, recorded** (`R69QmapSelfCheck`, `R69CriticEntryScope` F1): v4's map carries 8
    rows where v3 carried 13 and `QUALITY.md` has 15 criteria; Q03/Q06/Q08/Q09/Q10/Q12/Q15 have no row
    and no `n/a` reason, and two published `pass` rows (Q11, Q14) are contradicted by the entry's own
    bytes. That alone makes C1's "every applicable Q decision PASS or a named n/a" unsatisfiable.
- **No entry admitted this round**, so no expansion credit is taken and `K_HELD_BACKED` stays 8/14.

**Label-naming hazard, recorded (`R69CriticSeparability` F7):** `HOLDS_C2_V4` and `HOLDS_C2_V3` are the
*coverage* aggregates inherited from round 68's claim numbering, not labels for this round's C2
(calibration). This round's C1 is the coverage claim and its target conjunct is `HOLDS_C2_V4`; its C2 is
the Q15 criterion and its labels are `Q15_*`. Read the labels by what they compute (`measure.py:114-125`
for `HOLDS_C2_*`), never by the claim letter.

**What the labels would read, reported as a diagnostic and never as the measurement.**
`reports/round-69/measure-after.log` carries the registered crash receipt and, separately labelled, one
diagnostic run of the same pinned counter with only the four-line `def run` helper relocated above its
first use (+67 bytes of layout, no logic change) on a tree archived as `corpus reports/round-69`. That
diagnostic reads `Q15_PRESENT=yes`, `Q15_SELFTEST=pass`, `Q15_FALSE_KILLED=yes`, `Q15_RESTATE_OK=yes`,
`C7_V4_CLEAN=yes`, `K_HELD_BACKED=8/14`, `C05_STATUS=uncovered`, `HOLDS_C2_V4=no`, `C7_V3_CLEAN=no`,
`HOLDS_OK_V6=no`, `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`, exit 0. The C2 claim stays **FALSIFIED as
declared** — its own kill rule reads a label the pinned instrument cannot print — and the diagnostic is
the honest disclosure that the criterion and the checker work while the instrument does not. A reader
must not quote the diagnostic as the claim's measurement.

### Item-10 quarantine posture (wave-4, adoption stays closed)

The register slice was re-derived at round start with the prompt's own recipe and every line carries an
S-id (`assimilation/quarantine-slice`, 26 data rows). Hand-checked verdicts below are quoted **per seat**
— the seat reports under `.ufo/waves/round-69/` are the authoritative per-row records; this block is the
L1's roll-up and does not overwrite a seat's finding.

| seat | rows | PRESENT | ABSENT | UNREACHABLE | UNVERIFIED-REACHABLE / other |
|---|---|---|---|---|---|
| `R69QuarA` | S053, S054, S055, S058, S060, S061, S062, S063, S064 | 1 (S055) | 7 | 1 (S054, auth-gated 302 loop) | 0 |
| `R69QuarB` | S075, S081, S083, S085, S087, S089, S090, S092, S093 | 2 (S090, S092) | 3 (S075, S083, S093 partial) | 1 (S085 — the census `url` cell is truncated at 140 chars, so the cited URL cannot resolve) | 3 UNVERIFIED-REACHABLE (S081, S087, S089: quote verbatim in a neighbouring document, not in the cited one) |
| `R69QuarC` | S094, S095, S098, S099, S100, S107, S108, S111, S113 | 4 (S107 literal, S111 under JSON re-serialization, S113 at the article's canonical URL, S108 under whitespace fold) | 3 (S094, S095, S098) | 0 | S099 UNVERIFIED-REACHABLE; S100 NO-ROW |
| `R69QuarD` | the slice itself (26 rows) + the 24 quoted rows re-checked | 4 (S055, S107, S108, S111) | 17 | 2 (S061 upstream 502, S085 upstream 404) | 1 PARTIAL (S083 — filename only, in `Content-Disposition`) |

- **Slice size re-derived: 26 data rows**; `R69QuarD` established there is no row beyond the named set
  (the "27" is a grep artifact of the `## By lane` summary row plus two never-checked rows) and that the
  register's `## By lane` summary (24) matches its own rows — the assumed summary mismatch is falsified.
- **The absent-defect label does not hold as a class.** `R69QuarA`: "7/7 of the rows it calls ABSENT
  carry a locatable payload elsewhere, and S055's quote is verbatim in its own cited source"; a one-row
  attribution shift runs through the round-1 block (S053→S054, S060→S061, S061 q2/q3→S062, S062 q2/q3→S063,
  S055 breaking it); `/abs/`-URL citations quoting body text (S063, S064) and absent `<meta content>`
  folding (S055, S061 q1) manufacture fabrication-class rows. **Zero fabrication confirmations in the
  slice** — the remediation is re-point/re-quote, not refuse.
- **Cross-pass disagreement is recorded, not smoothed.** Round 67 hand-checked the same 26 rows and read
  S061 as PRESENT and S085 as UNREACHABLE; this round's seats read S061 ABSENT-against-its-own-URL
  (PRESENT only in a neighbouring row's source) and S085 UNREACHABLE upstream. Both readings are kept:
  the row-level facts agree (the quote is not in the row's cited URL), the label differs on whether a
  wrong-row attribution counts as PRESENT. That disagreement is the campaign owner's to rule, not this
  lane's, and it is exactly the kind of split a single-pass hand-check hides.
- Campaign observations passed to the owner, **never edited by this lane**: the register's Totals cell
  says 324 spans while its tables hold 301 (`R69QuarD`); register row 169 has unescaped `||`; every
  revenger row resolves at `reg id + 2` in `lanes/revenger/**/SOURCES-PROPOSED.md` while `ID-REMAP.md`
  lands one short; r1's S061/S062 quotes are swapped across rows; the register's sha256 was unchanged
  (`5afe1810…`) throughout — verified by `R69QuarA` and `R69QuarD`.
- **Adoption: closed.** Zero package rows or entries were appended or copied.

## Mistakes

| id | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| M48 | attribution / identity-without-derivation (the r68 D1 class recurring, now inside this round's own frozen text) | (a) `reports/round-68/measure-after.log:102` — the original defect the round was routed to close; (b) `reports/round-69/claims.md:137-139` asserts red-before `Q15_SELFTEST=pass` / `Q15_FALSE_KILLED=yes` while its own committed receipt prints `n/a (no checker)` at `measure-before.log:22-25` (`git cat-file -e 222a7a7:corpus/q15_tree_id_check.py` → 128); (c) `claims.md:166-167` says the counter sha256 is pinned "in `measure-before.log`", which contains no digest at all (`grep -c sha256` = 0) | **none** before this round — the lane had no criterion for a stated identity or locator until Q15; found independently by `R69CounterReplay` F2, `R69CounterIntegrity`, `R69CriticClaimsC2`, `R69LessonCheck` F1, `R69FixtureHold`, `R69DeriveCritic` | `corpus/QUALITY.md` **Q15** added this round (a stated git object id or tree identity must be re-derived with the command that names it), with `corpus/q15_tree_id_check.py` as its mechanical form. Shown able to fail: `--scan reports/round-69/d1-false-sentence.md` exits **1** naming the contradicted pair, while the corrected restatement exits **0** (`R69Q15CheckerRun`), and `--self-test` exercises both legs (exit 0). Also shown able to fail on an absence: any restatement line whose pairs do not resolve exits 1 (`R69D1RestateCheck` probe). **Caveat, reported not hidden:** the checker only sees `tree-identity …:` prefixed ``` `<hex>:corpus` = `<40hex>` ``` pairs, so the v4 entry's `c7b7cf98` sentence is invisible to it (that is why Q15 FAIL comes from the criterion, not from a label); and `measure.py` reduces the kill leg to `rc != 0`, which a non-demonstrating fixture also satisfies (`R69CriticClaimsC2` counterexample 2). Both routed. |
| M49 | number-drift / bound-from-intent | `corpus/knowledge/round-68-apk-axml-byte-evidence.md:57,:148,:157` state the chunk-type enum block as "lines 237-253"; the pinned snapshot's block opens at `:237` (`enum {`) and closes at `:263` (`};`), with `RES_XML_RESOURCE_MAP_TYPE` at `:253` inside it. Reproduced by the extended derivation (`enum block open : 237`, `enum block close : 263`) and by `sed -n '237p;263p' corpus/snapshots/ResourceTypes.h` | the round-68 wave did not test the block bound (Q04/Q11 checked line numbers *stated* against *printed*, and 253 was printed); `R69AnchorDerive` and `R69AnchorBlind` caught it this round by adding the bound to the derivation | the v4 candidate states 237-263 with both bounds printed by `corpus/derive_axml_anchors.py`; the derived bound is now inside the verbatim-gated block, so the gate re-checks it. Registered as a routed repair, not as a claim. |
| M50 | landing / instrument regression (new code path using a helper defined below it; the red-before could not see it) | `reports/round-69/measure.py:158` (also `:163`, `:172`) calls `run(...)`; `def run` is at `:187`. On `git archive HEAD corpus` the counter prints `Q15_PRESENT=yes` then `NameError: name 'run' is not defined`, exit **1** — indistinguishable from "a hold failed" under the script's own exit contract. At base `222a7a7` the branch is not entered (no checker), which is exactly why the red-before receipt is clean: control and treatment ran different code paths | **none** — neither the counter's own self-checks nor the pre-registration could catch it, because the failing branch exists only on the treated tree. Found independently by five seats: `R69Q15CheckerRun`, `R69CounterIntegrity`, `R69HoldSweep`, `R69ReadmeFlipCheck`, `R69ReviewC7Gate`, `R69CriticClaimsC1` | **routed, deliberately not repaired in-revision**: `claims.md:167` freezes the instrument, and patching it after seats scored would be exactly the post-hoc rule change kumitate r42 forbids. Next counter hoists `def run` above the Q15 block, makes an uncaught exception exit **2** ("not evaluable") instead of 1, and adds a pre-freeze smoke run on a tree that *contains* every new artifact the round registers. The red-before lesson is recorded: a control tree must differ from the treatment tree in the artifact under test only, never in whether a whole code branch exists. |

## Routed forward (not claims; each with its owner surface)

1. **Counter repair (owner: next round's pre-registration, before any after-run).** Hoist `def run`;
   map uncaught exceptions to exit 2; move the D1 fixture inside `corpus/` (or archive `reports/round-69/`
   alongside `corpus` and say so in the invocation) so `Q15_FALSE_KILLED` is evaluable at all; key that
   label on the checker's `Q15_FALSE_KILLED:` prefix rather than `rc != 0` (`R69CriticClaimsC2`,
   `R69CorpusPathHygiene`, `R69KillRuleClosure`).
2. **Kill-rule closure (owner: next claims revision).** C1's kill rule covers only "any Q FAIL or a
   spot-check REJECT"; `K_HELD_BACKED`, `K_HELD_BACKED_STRICT`, `K_ROW C05 status`, `C05_SINGLE_V4`,
   `HOLDS_C2_V4`, `README_TOKEN_LEGEND_MISMATCH` and `C7_V4_CLEAN` have no kill clause and each is
   reachable with every hold green (`R69KillRuleClosure` counterexamples B and C). Append a
   tighten-only clause before adjudication next round.
3. **C05 repair set for a fifth pass** (owner: next coverage round): drop or probe the exit-2 clause
   (Q05); restate `:91` as direct string-pool indexing at `readout.py:211` with the namespace chunk
   reported separately (Q07); fix `:48`'s two counts and drop the length on the truncated run (Q14); add
   the `c7b7cf98` deriving command and a Q15 row to the §Q-map (Q15); add S032 §4.3.16 to the S032 scope
   (item 2's `+12`/`+16` offsets), cite `:477/:480` for the UTF-8 flag, and pin the "Appears
   header.headerSize bytes after…" sentence to `:675` (`R69CriticEntryDeps` S-1..S-3, `R69Item8` P3).
4. **Gate hardening (owner: next calibration round).** A `$ ` line indented by one space is skipped
   silently, so `C7_V4_CLEAN=yes` survives a corrupted derivation digest line; an entry quoting 0 or 1 of
   20 output lines also exits 0. Report unchecked blocks as problems (`R69CriticC7Claim` path 1,
   `R69AnchorCritic`). Keep the D5 two-line partial-drift fixture, the `lines[:1]` weakening and the
   `HOLDS_OK_V6`/`c7_v3_clean` coupling open — the round-68 C7 L0 is unanswered and this round did not
   pre-empt it.
5. **Derivation fail-open edges (owner: `corpus/derive_axml_anchors.py`).** `enum_block_bounds` returns the
   first `RES_NULL_TYPE` block with no uniqueness or containment check, and a non-hex initializer prints
   `= ?` with exit 0 (`R69DeriveCritic`); both should `fail()` (exit 2).
6. **`corpus/README.md` index staleness** (owner: next round's registered edit): `:9` still says
   `Q01–Q13`; `:17` does not cover `q15_tree_id_check.py`; `snapshots/`, `derive_axml_anchors.py` and
   `check_embedded_outputs.py` are named nowhere (`R69CorpusPathHygiene` §4, append-only patch).
7. **Misroot (fleet-level, reported not fixed here).** `.ufo/waves/round-69/w1/ScoutAmp.md` and
   `.ufo/waves/round-24/w2/RevUnlandedResolution.md` sit at the fleet root — kotoba's and tabi's seats,
   not this lane's; `git status` needs `-uall` to see them (`R69MisrootSweep`). No revenger round-69 seat
   note landed at the fleet root.
8. **SHONEN box-1 reconciliation** (routed D4, append-only): committed `SHONEN.md:4-9` reads `[x]` with
   `revenger-r64.R64ReviewSkill`; `SCORECARD.md:537-538`'s `[~]` sentence is superseded as a *state*
   statement and survives only as a *scope* statement — the `[x]` covers the r64 bytes (39098 B,
   `bfd92057…`), the current bytes (51809 B, `a12fb8e2…`) have no non-lane re-confirmation. Seven live
   defects on those bytes are listed in `R69ShonenBox1` F1–F7.

## Tree-identity records (Q15)

tree-identity false-sentence: `1c34603:corpus` = `51894d153a6e69487da2a273680d014abd240f61`

tree-identity restatement: `1c34603:corpus` = `ddc6a4f6aea51ef34e0b7669832ff1a9cb2023f7`; `14774a2c:corpus` = `51894d153a6e69487da2a273680d014abd240f61`; `dddf147:corpus` = `51894d153a6e69487da2a273680d014abd240f61`

The false line is round-68's D1 sentence as committed (`reports/round-68/measure-after.log:102`): the
`1c34603` corpus tree is **not** the `14774a2c` tree. The restatement is the truth: only
`corpus/lessons/round-68.md` differs between `14774a2c` and `1c34603` (`git diff --name-only 14774a2c 1c34603 -- corpus/`),
the counter's inputs are unchanged, and the counter's stdout is byte-identical on both trees
(`R69D1RestateCheck` re-ran the pinned round-68 counter on both: exits 0, `diff` exit 0). Both lines are
verified by `corpus/q15_tree_id_check.py --scan corpus/lessons/round-69.md --lane <lane>`.

## Wave record

ONE v2 wave, exactly **64 seats**, one batched `task` call carrying the validator's `taskCall` unchanged
(`.ufo/waves/round-69/dispatch/dispatch.json` ≡ `plan-validated.json`, `counts.spawn=64`,
`dispatch.calls=1`). Roles: reviewer 21 · critic 17 · executor 11 · scout 5 · mutation-tester 3 ·
sentinel 3 · scribe 2 · connector 1 · revenger 1 = 64. Attack share under **both** predicates (repair
D3): lane predicate (reviewer/critic/mutation-tester/sentinel/revenger) **45/64 = 70.3 %**; prompt §2 v2
floor list (reviewer/critic/mutation-tester/labrat) **41/64 = 64.1 %**. Slot, committed as evidence
(repair D2): `granted lane=revenger wave=round-69-w1 seats=64 live=66 pending=0 cap=256`
(`.ufo/waves/round-69/dispatch/slot-acquire.log`). §3 planner seat held by the L1 (the validator rejects
`planner`: exit 1 `unknown_role` on a scratch copy — `R69WaveContractAudit`). Validation env pair named:
`UFO_CONFIG_PATH=scripts/hyaku/ufo-wave-policy-v2.json` + `UFO_FLEET_ALLOW_EXTERNAL_TOOLS=1`
(band 64–128 reported there; the bare invocation validates under the default 32–256 band — F1 of the audit).
Twelve drafted items were dropped from 76 → 64 with the rationale committed in
`.ufo/waves/round-69/build-wave-spec.py:284-300`; no padding seat (`R69WaveContractAudit`).
**Dead seats: 0** — every one of the 64 seats returned a report. Residual `task` calls: none.
considerthese: `2026-10-24.md` proposal 2 (provider-refusal seats recorded as their own line) —
**no seat was lost to a provider refusal this round**, so the record is a zero line in this section.
Tool installs: none.
