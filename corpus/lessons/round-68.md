# round 68 — revenger (hyaku, attempt 2)

Round 68 declared two claims (`reports/round-68/claims.md`, frozen at `f505526` against base
`f165908aaffcf14798de53405fe788986bd33ff9`, counter `reports/round-68/measure.py` sha256
`0de4eb6f34bdb906fb69fdd173aaac9bcef629e6ff1d4c67f5ba8c91093f7766`):

- **C1 — calibration, C8: the registered embedded-output gate attributes its own kill.** Frozen
  predicate met on the final measured tree (`C7_MUTANT_KILLED_ATTRIBUTED 0/1 → 1/1`,
  `C7_NEG_SPOOF_KILLED 1/1` with `…ATTRIBUTED 0/1`, `HOLDS_OK_V5/V6 no → yes`, counter exit 0).
  **Verdict: improved.** Caveat: two critic seats showed the predicate is satisfiable by a gate that
  does not detect drift (`R68CriticC7Claim`, `R68CriticClaimsC1`) — the counter's C7 labels
  establish marker-presence, not behavioural attribution; the landed gate's behaviour itself was
  established by the behavioural seats (`R68MutC7Entry`, `R68MutC7Kill`, `R68MutC7Spoof`).
- **C2 — coverage, K (lowest non-retired criterion, 5.7): the C05 third-pass re-gate with
  machine-derived anchors.** Wave Q decisions on the landed v3 bytes: **FAIL** at Q04
  (`R68ReviewEntryQ04`), Q05 (`R68ReviewEntryQ05`), Q07 (`R68ReviewEntryQ07`), Q11
  (`R68ReviewEntryQ11`), Q13 (`R68ReviewEntryQ13`); PASS at Q02, Q03, Q08-under-Q11-routing, Q09,
  Q10, Q12 (n/a). **Verdict: FALSIFIED** — kill rule executed: C05 stays `uncovered`, the v3 entry
  is retained with `admission-status: rejected` and every other byte kept, `K_HELD_BACKED` stays
  8/14.

## Gate

Source rows opened this round (CORPUS.md rule 1: URL or command, access date, located quote):

- **S046 (new row this round, own-work, tier A).** What was opened: `corpus/derive_axml_anchors.py`
  (sha256 `bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249`) run over
  `corpus/snapshots/ResourceTypes.h` (sha256 `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f`,
  86255 bytes), plus `python3 -B corpus/derive_axml_anchors.py` re-run by this L1 and by five seats.
  Access date **2026-10-24/25**. Located quote (≤ 25 words), from the script's own stdout:
  `enum RES_XML_START_NAMESPACE_TYPE : 245`.
- **S038 (existing row, re-opened this round).** Opened from the committed snapshot copy, not the
  network: line 245 is `RES_XML_START_NAMESPACE_TYPE      = 0x0100,` and line 244 is
  `RES_XML_FIRST_CHUNK_TYPE          = 0x0100,`. Access date **2026-10-24/25**. Located quote:
  `RES_XML_START_NAMESPACE_TYPE      = 0x0100,`.
- **S045 (existing row).** Not re-opened as a live fetch; the committed snapshot
  `.ufo/waves/round-67/source-snapshots/dex-format.html` (`c0428612…`) was re-hashed and its four
  quoted clauses re-located by `R68ReviewEntryQ02`/`R68ReviewEntryQ03`. Access date **2026-10-25**.
  Located quote: `must be 0x70 (112) bytes (v40 or earlier)`.

Registry changes (append-only fields, logged old → new):

| row | field | old | new | reason |
|---|---|---|---|---|
| S046 | `used-by` | `—` | `corpus/knowledge/round-68-apk-axml-byte-evidence.md` | the row is cited at that entry's `source:` header; `—` made `mined` false and triggered census `W03` (`R68CensusReplay`, `R68ReviewSourcesS046`) |
| S045 | `used-by` | `corpus/knowledge/round-67-apk-axml-byte-evidence.md` | **unchanged** | repair D4 case (b): the round-68 candidate was rejected, so no re-point is licensed; D4 stays open and named |
| — | table structure | S046 row separated from the registry table by a blank line (two pipe tables) | single table | `R68ReviewSourcesS046` MEDIUM |

**S045 quote length (repair D3).** `corpus/lessons/round-67.md:75` states "(18 words)" for the
checksum sentence; the sentence is **19** words by whitespace count, and the `SOURCES.md:59` anchor
variant is **14** words. Both are ≤ 25, so the row was conformant and only the count was wrong.
`round-67.md` stays byte-preserved; this row is the correction.

**Admission decisions (QUALITY.md, criteria Q01–Q14).**

- `corpus/knowledge/round-68-apk-axml-byte-evidence.md` — **REJECTED.** Failing criteria: Q04
  (item 11 credits `derive_axml_anchors.py` with printing every stated S038 line number while
  `:237` and `:244` are stated and never printed; item 5's struct widths are a literal at
  `readout.py:51-58` presented as computed from S038), Q05, Q07 (entry:89's namespace-resolution
  sentence), Q11, Q13 (the credit is bounded to 16 of 18 numbers; prose anchors unguarded). Passed
  on Q02, Q03, Q09, Q10, Q12; Q14 fails on line 46 (`4d616e69666573742d` is 9 bytes, the prose
  calls it "the 16-byte prefix"). Retained as evidence; the README C05 row is not flipped.
- **No entry admitted this round**, so no expansion credit is taken and `K_HELD_BACKED` stays 8/14.

Census before → after (fleet `scripts/sources-census.sh`, the specification in `CORPUS.md`):

```sh
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger
# round start (before any round-68 registry edit): exit 0
revenger	W04	S024 duplicate url www.rfc-editor.org/rfc/rfc3227.txt across scopes
revenger	W04	S028 duplicate url github.com/ethereum/execution-specs/tree/v2.20.0/src/ethereum/forks/osaka/vm across scopes
revenger	W04	S029 duplicate url tc39.es/ecma262 across scopes
revenger	W04	S034 duplicate url pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT across scopes
revenger	W03	S046 mined but unused
revenger	ok	/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md
```

```sh
# round end (after the S046 used-by repair): exit 0
revenger	W04	S024 duplicate url www.rfc-editor.org/rfc/rfc3227.txt across scopes
revenger	W04	S028 duplicate url github.com/ethereum/execution-specs/tree/v2.20.0/src/ethereum/forks/osaka/vm across scopes
revenger	W04	S029 duplicate url tc39.es/ecma262 across scopes
revenger	W04	S034 duplicate url pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT across scopes
revenger	ok	/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md
CENSUS_EXIT=0
```

Rows 45 → 46 (only S046 added); the `W03` warning is gone at round end, leaving the four disclosed
`W04` duplicate-scope warnings.

## Mistakes

| id | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| M46 | landing/registry drift — the authoritative registry row was not re-derived from the repaired instrument's bytes after a repair (the inverse of M45) | `SKILL.md:268` at build tip `4232235` still asserts the C7 marker "is structurally shadowed … can never fire … reorder fix routed", while the landed `corpus/check_embedded_outputs.py:140-146` prints that marker as the last line of a killed run; measured `C7_MUTANT_KILLED_ATTRIBUTED=1/1` (`.ufo/waves/round-68/R68MutC7Kill.md`, `R68MutC7Spoof.md`) against `0/1` at base (`reports/round-68/measure-before.log`) | round-67 spot-check routed defect 2, plus three wave seats that re-read the row independently: `R68ReviewSkillRegistry`, `R68ReviewC7Gate` F3, `R68SimplifierGate` | the registry row was rewritten from the after-run in this round (`SKILL.md` self-test cell, kind, verdict map with `64` declared, `measured-against` re-pointed to the round-68 counter); **shown able to fail**: the pre-fix cell contradicts the measured `C7_MUTANT_KILLED_ATTRIBUTED=1/1` and the frozen-mutant transcript, so a reader applying the old cell would reject a true repair |
| M47 | number-drift/prose (the M39/M44 class recurring at prose level) | `corpus/knowledge/round-68-apk-axml-byte-evidence.md:46` — `4d616e69666573742d` (9 bytes) called "the 16-byte prefix"; found independently by `R68Item1` (F1) and `R68Item10` (secondary), both non-author byte derivations, and by `R68ReviewEntryQ04` §F2 in the same class | two wave seats deriving from the fixture bytes (Q08's rule "a non-author byte-derived value supersedes author prose"); no author-side check existed — the bar had no criterion for a quoted hex string's stated byte length | `corpus/QUALITY.md` **Q14** added this round (considerthese 2026-10-24 proposal 1): a hex string quoted with a byte count in the same clause must have `2 × N` hex characters, an ellipsis-truncated run carries no length, and an `ASCII …` rendering must decode from the same run. **Shown able to fail**: applied to the rejected entry it flags line 46 (`18 hex chars` vs `2 × 16 = 32`); applied to the five admitted `round-6x-*.md` entries it finds no such claim (`n/a`, criterion not exercised) |

Q14's falsifier, run at adjudication so the criterion is shown able to fail:

```sh
$ python3 -B -c "import pathlib,re; l=pathlib.Path('corpus/knowledge/round-68-apk-axml-byte-evidence.md').read_text().splitlines()[45]; h=re.search(r'\`([0-9a-f]+)\`',l).group(1); i=l.index('the 16-byte'); print(len(h)//2,'bytes quoted; clause:',l[max(0,i-30):i+22])"
9 bytes quoted; clause: 573742d` — ASCII `Manifest-`, the 16-byte prefix of
$ # same shape on the admitted round-63 entry, line 97
4 bytes quoted; clause: , the four bytes `504b03
```

The first is the rejected v3 entry's line 46 (9 bytes quoted against a stated 16 → **fails**);
the second is `corpus/knowledge/round-63-zip-central-directory-evidence.md:97` (4 bytes quoted
against "four bytes" → **passes**). Ellipsis-truncated runs carry no length and are excluded.

## Routed forward (not claims; each named with its owner surface)

1. **Counter gameability of C7** (`R68CriticC7Claim`, `R68CriticClaimsC1`, `R68CriticC7Surface`): the
   frozen labels prove marker-presence on a textual mutation, not behavioural attribution. Next
   counter: generate the drifted entry from the entry's own declared command and add a
   non-attributed behavioural leg (true line + appended text → exit 1, `ATTRIBUTED=0/1`).
2. **C1/C2 separability coupling** (`R68CriticSeparability`, `R68CriticClaimsC2`): `HOLDS_OK_V6`
   folds in `c7_v3_clean`, the only cross-artifact edge. `claims.md:34-37`'s "neither counter reads
   the other's artifact" is false in both directions; drop `c7_v3_clean` from V6 next round.
3. **Kill-rule closure** (`R68CriticClaimsC1` DEFECT C): a conjunct that reads off-target leaves the
   claim neither PASS nor FALSIFIED. Every mechanical conjunct must appear in the kill rule.
4. **C7 self-test discrimination** (`R68CriticC7Surface`): the drift fixture quotes one line, so a
   `lines[:1]` weakening survives. Add a two-line partial-drift fixture.
5. **C7 registry/gate holes** (`R68ReviewSkillRegistry`, `R68RepairD2`): the gate ignores
   `admission-status`, does not verify its digest pin, and maps a missing entry to exit 1 (drift)
   rather than 2. The row now declares the digest-verification clause unmet.
6. **C05 repair set for the next coverage round** (all five Q FAILs): extend
   `derive_axml_anchors.py` (`RES_XML_FIRST_CHUNK_TYPE`, enum block bounds 237/263, enum values),
   re-embed item 11 → 19+ lines, update S046's count and every "17 lines" claim in one commit;
   label item 5's width table manual; bound item 11's credit to the numbers it actually prints;
   drop "framework" from the resource-id sentence; fix entry:89's namespace-resolution claim; add
   S032/S034 `source:` lines; pin `generator.py`.
7. **`SKILL.md` §6.1** stops at `HOLDS_OK_V4` and never names `C7_*`/`HOLDS_OK_V5`/`V6`
   (`R68ReviewSkillRefresh` item 2).
8. **S045 defect D4 stays open**; `S038`/`S043`/`S041` still carry `used-by` pointers at rejected
   candidates (`R68RepairD4` counterexample).
9. **`readout.py --fact <unknown>` exits 0 with no output** (`R68Item3` N4) — a typo'd fact id
   yields a silently empty block.

## Wave record

One v2 wave, 64 seats, one batched call, 46 attack seats (71.9 %). Reports:
`.ufo/waves/round-68/R68*.md` (64/64 seats wrote one). Inherited spec repair: milestone 235 bytes
(was > 256, `plan` exit 1) and 66 → 64 seats (the two duplicate seats dropped); re-validated `plan`
exit 0 and committed with the dispatch receipt
(`.ufo/waves/round-68/dispatch/plan-validated.json`, `dispatch-run.log`). **Dead seats: 0** — every
one of the 64 seats returned a report; the only refusals this round were none. Residual `task`
calls: none (no follow-up reviewer/critic batch was needed; the wave produced 64 distinct attack and
build items). Wave-contract audit: `R68WaveContractAudit` CONTRACT-OK, with three named defects
(abridged Q-criterion lines in 13 seat prompts; `R68ReviewEntryQ08` a pure redirect to Q11;
`R68ReviewSkillRefresh` the one seat serving no claim — 1/64).
