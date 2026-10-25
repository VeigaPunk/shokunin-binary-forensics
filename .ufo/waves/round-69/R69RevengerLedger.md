LEDGER-BROKEN — the C1 side, the base/label and both sha pins re-derive exactly, but C2's red-before numbers contradict the committed receipt (claims.md:137-139 say `Q15_SELFTEST=pass`/`Q15_FALSE_KILLED=yes`; measure-before.log:23-24 say `n/a (no checker)`), the counter pin the claims says is "in `measure-before.log`" is absent there (claims.md:166-167; receipt has 0 sha lines), and the new `Q15_FALSE_KILLED` leg is a bare `rc != 0` (measure.py:165) that scores a forged/undeonstrating fixture as "killed" — the r68 C7 attribution class reintroduced.

seat: R69RevengerLedger (leaf, no dispatch) · round 69 (hyaku run 6) · 2026-10-25
lane: /home/vgpnk/Projects/shokunin/revenger-shokunin · HEAD at check: `35e1258`
frozen artifacts checked: `reports/round-69/claims.md` (committed `e1d22ca`),
`reports/round-69/measure.py`, `reports/round-69/measure-before.log`, r68 closure
`corpus/lessons/round-68-verifier-spotcheck.md`
write scope: this file only; `/tmp/revenger-r69-ledger-*` scratch used and deleted; no
lane/fleet byte edited, no git write anywhere; no tool installed or upgraded.

## 0 · Method (so every number below is checkable)

1. Base/label re-derived: `git log -1 --format='%H %p' 222a7a7` → `d00f779`; `git diff
   --name-status d00f779 222a7a7` → exactly `A corpus/lessons/round-68-verifier-spotcheck.md`.
2. Counter pins re-derived: `sha256sum reports/round-69/measure.py reports/round-68/measure.py`.
3. The receipt re-derived, not trusted: `git archive 222a7a7 corpus | tar -x -C /tmp/… &&
   python3 -B reports/round-69/measure.py /tmp/…/base` → **exit 0, byte-identical to
   `measure-before.log`** (`diff` clean), so the receipt is genuinely the base-tree red-before
   and the frozen counter reproduces it.
4. Every claims number diffed against that receipt line by line.
5. The Q15 checker probed with four crafted fixtures in `/tmp` (read-only on the lane) to test
   what its exit codes actually mean.

## 1 · Numbers that HOLD (checked, not assumed)

| claim | pointer | re-derived | verdict |
|---|---|---|---|
| claim base `222a7a7…` = r68 tip + the non-author spot-check | claims.md:3-5 | `222a7a7^` = `d00f779`; delta = `A corpus/lessons/round-68-verifier-spotcheck.md` only | HOLD |
| counter pin `bca74e6d…` | claims.md:6 | `sha256sum reports/round-69/measure.py` = `bca74e6d8b5010aee79886521474f072257ee22ec7ccc24e4186666bdc048377` | HOLD |
| r68 pin `0de4eb6f…` | claims.md:7 | `sha256sum reports/round-68/measure.py` = `0de4eb6f34bdb906fb69fdd173aaac9bcef629e6ff1d4c67f5ba8c91093f7766` | HOLD |
| "copy of the round-68 counter plus the round-69 labels" | claims.md:6-7 | `diff -u <e1d22ca:reports/round-68/measure.py> reports/round-69/measure.py` = pure additions (`LANE`, `C05_SINGLE_V4`, `HOLDS_C2_V4`, `C7_V4_CLEAN`, `Q15_*`); no r66/67/68 line changed | HOLD |
| receipt = base `222a7a7` | claims.md:9-11 | exact replay above, exit 0 | HOLD |
| exit contract 2/0/1 | claims.md:165 | `measure.py` tail: `sys.exit(2 if not evaluable else 0 if holds_ok else 1)` | HOLD |
| D1 hashes `1c34603:corpus`=`ddc6a4f6…`, `dddf147:corpus`=`51894d15…` | claims.md:25-26 | `git rev-parse` prints exactly those two ids; `14774a2c:corpus`=`51894d15…` | HOLD |
| C1 do-nothing control `8/14, 8/14, uncovered, V4=no, C2_V4=no, C7_V4=n/a` | claims.md:113-115 | receipt lines 4, 6, 2, 10, 17, 81 — all six match | HOLD |
| void floors: C2–C5 2/2, C6 4/4, C7 1/1, HOLDS, HOLD_CALIBRATION 4/4, HOLD_REPLAY 10/10, FRESH_ROWS 18/18, STRICT pass | claims.md:183-196 | receipt l.32/35/38/41/44, 82, 98, 99, 21, 11; 10 `corpus/verify_*.py`, 14 C-rows, 15 Q-rows | HOLD |
| C1 derivation "20 lines" / enum range 237-263 / subset 239-253 | claims.md:66-68, 74-75 | `python3 -B corpus/derive_axml_anchors.py` (tree `da02261`) → exit 0, **20** lines, `enum block open : 237`, `enum block close : 263`, values at 239/241/244/245/246/247/248/253 | HOLD |
| "every S038 line number the entry states is printed" (r68's F1 repair) | claims.md:66-68 | entry cites 218,237,239,241,244,245,246,247,248,253,263,287,461,612,677,686,687,707 — every one is in the 20-line stdout | HOLD (genuine repair) |
| Q14 hex clause (9 bytes vs "nine bytes") | claims.md:81-82 | entry:48 quotes `4d616e69666573742d` (18 hex = 9 B) against "9 bytes" | HOLD |
| S047 script sha + 20 lines; S041 four pins | claims.md:83-86 | `74d4c0d9…` = actual script sha; fixture `05d2280f…`, truth `27303bae…`, generator `eaa9444c…`, readout `92e347c3…` all equal `da02261` blobs | HOLD |
| `C7_V4_CLEAN=yes` reachable | claims.md:100 | `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-69-…md` → `checked_blocks=17 problems=0` exit 0 | HOLD |
| void surfaces untouched | claims.md:183-196 | `git diff 222a7a7 da02261 -- corpus/fixtures corpus/live <round-65/67/68 entries>` = empty | HOLD |
| D2 repair (raw slot acquire committed) | claims.md:205-207 | `.ufo/waves/round-69/dispatch/slot-acquire.log` in `35e1258`: `granted lane=revenger wave=round-69-w1 seats=64 live=66 pending=0 cap=256` | HOLD |
| D3 repair (both attack predicates named) | claims.md:209-212 | 64 items; roles reviewer 21 · critic 17 · executor 11 · scout 5 · mutation-tester 3 · sentinel 3 · scribe 2 · connector 1 · revenger 1 → lane predicate 45/64 = 70.3 %, prompt predicate (labrat 0) 41/64 = 64.1 %, both ≥ 25 % | HOLD |
| band 64–128, maxLanes 256 | claims.md:199-200 | `plan-validated.json` policy: `waveMinLanes 64, waveMaxLanes 128, maxLanes 256, hardCeiling 256`; `counts {spawn:64,total:64}`; no `planner` role | HOLD |
| claims/counter frozen after pre-registration | — | `git diff --stat -- reports/round-69/claims.md reports/round-69/measure.py` empty | HOLD |

## 2 · Findings

### F1 (high) — C2's red-before numbers are contradicted by the committed receipt
- claims.md:137-139: "**Red-before (committed history).** On the base tree: `Q15_PRESENT=no`
  …, `Q15_RESTATE_OK=n/a` …, `Q15_SELFTEST=pass` and `Q15_FALSE_KILLED=yes` (the checker
  ships with the claims revision …)".
- `reports/round-69/measure-before.log:22-25` (committed `e1d22ca`, exact replay verified):
  `Q15_PRESENT=no` / `Q15_SELFTEST=n/a (no checker)` / `Q15_FALSE_KILLED=n/a (no checker)` /
  `Q15_RESTATE_OK=n/a (no checker)`.
- Cause is structural and self-evident from the claims' own parenthesis: `measure.py:156` looks
  for `TREE/corpus/q15_tree_id_check.py`, and that file only enters `corpus/` at `e1d22ca`
  (`git show --stat e1d22ca` → `corpus/q15_tree_id_check.py | 129 +`), so on the `222a7a7`
  corpus tree it cannot be present. `pass`/`yes` are not red-before values for any tree; they
  are the *final-tree* target values (claims.md:130-131).
- Impact: two of C2's four red-before legs are misstated, and the receipt cannot support them.
  The other two legs (`Q15_PRESENT=no`, `Q15_RESTATE_OK=n/a`) are correct, so C2's do-nothing
  control is partly real and partly fabricated.

### F2 (high, calibration) — `Q15_FALSE_KILLED` is a bare `rc != 0`; the kill is not attributable
`measure.py:165`: `q15_false_killed = rc != 0` (printed at :167). The checker returns `rc=1` in
**at least three different states**, and the counter cannot tell them apart:

| probe (in `/tmp/revenger-r69-ledger`) | checker output | rc | counter would print |
|---|---|---|---|
| committed `d1-false-sentence.md` (false pair, no restatement) — the intended receipt | `Q15_FALSE_KILLED: all false-sentence pairs failed (defect receipt)` | 1 | `Q15_FALSE_KILLED=yes` ✓ intended |
| **forged**: `tree-identity false-sentence: \`1c34603:corpus\` = \`ddc6a4f6…\`` (the TRUE id), no restatement | `Q15_RESTATE_BAD: no false-sentence pair failed …` | 1 | `Q15_FALSE_KILLED=yes` ✗ — a fixture that demonstrates nothing scores as killed |
| **correct** lesson: valid restatement only, no false quote | `Q15_RESTATE_BAD: no false-sentence pair failed …` | 1 | `Q15_FALSE_KILLED=yes` (and `Q15_RESTATE_OK=no`) ✗ |

Textual proof of the shared branch: `corpus/q15_tree_id_check.py:88-105` — a file with no
`tree-identity restatement:` line falls into `if restate_count == 0:` (:103), prints the
`Q15_FALSE_KILLED:` marker (:104) and returns False (:105). So the marker that names a kill is
printed for a file that contains no false-sentence line at all, and the counter reads only the
exit code. This is exactly the class the r68 closure closed by adding
`C7_MUTANT_KILLED_ATTRIBUTED` (r68 receipt `0/1 → 1/1`, `corpus/lessons/round-68-verifier-spotcheck.md`
§2), and it is on r68's still-open routed list (D5: "counter C7 gameability … kill-rule
closure over every mechanical conjunct"). Round 69's new calibration criterion reproduces it.

### F3 (medium) — `Q15_RESTATE_OK`'s mechanical meaning is not the one the claims states, and it false-kills a correct lesson
- claims.md:133-134 defines the leg as "the lesson's restated tree-identity sentence re-derives
  against `git rev-parse <hash>:corpus`".
- Actual (`q15_tree_id_check.py:79-108`): exit 0 requires **both** ≥1 valid
  `tree-identity restatement:` pair **and** ≥1 `tree-identity false-sentence:` line whose pair
  fails. A lesson that correctly restates the D1 sentence and nothing else exits 1
  (`probe-restate-only.md` → `Q15_RESTATE_BAD: no false-sentence pair failed …`, rc=1) and would
  therefore be scored `Q15_RESTATE_OK=no` → C2 FALSIFIED under claims.md:144-147, with a
  correct restatement in hand. The kill rule can fire on the pass condition.

### F4 (medium) — criterion Q15's text covers a general class; the checker covers one notation
- `corpus/QUALITY.md:27` (Q15): "A stated git object id or tree identity is re-derived with the
  command that names it; a sentence asserting `X:corpus` equals a hash must resolve under
  `git rev-parse X:corpus`."
- `q15_tree_id_check.py:34`: `PAIR = re.compile(r"`([0-9a-f]{7,40}):corpus`\s*=\s*`([0-9a-f]{40})`")`
  — only the canonical `` `short:corpus` = `<40hex>` `` form is parsed, and only on lines with
  the two fixed prefixes.
- The real D1 sentence does not match: `probe-prose.md` with `reports/round-68/measure-after.log:102`
  verbatim → zero pairs matched, exit 1 with "no false-sentence pair failed" — the checker never
  evaluated the claim it was built for.
- The committed ability-to-fail receipt is a rewrite, not the sentence:
  `reports/round-69/d1-false-sentence.md:12` ends with "Normalized to the checker's pair syntax".
  So claims.md:131 ("the checker flags the committed D1 false-sentence fixture") is true of the
  normalized derivative only; the fixture documents this itself. Q15 as registered tests a
  notation, not the stated class.

### F5 (medium) — the r68 Q04-F2 contradiction survives in the readout the entry cites
- claims.md:71-73: "Item 5's struct-width table is labeled **manual** (transcribed in
  `readout.py:51-58` …); the Q04 'literal presented as derived' defect is removed."
- The entry now says manual (`corpus/knowledge/round-69-apk-axml-byte-evidence.md:61`).
- But the cited evidence still asserts derivation: `corpus/fixtures/apk-r65/readout.py:49-50`
  — "Every fixed offset the readout uses is computed here from the field widths in
  ResourceTypes.h's own struct definitions, not assumed" — immediately above the literal
  `w8, w16, w32 = 1, 2, 4` (:51) and the hand-written `widths` dict (:52-58). The exact
  bytes the r68 closure failed Q04 on are unchanged; the defect is now entry-vs-evidence
  instead of entry-internal. Readout bytes are frozen by this round's own void condition
  (claims.md:176-178), so the honest repair is a disclosed residual, not a silence — the
  claims says "the defect is removed", which is true only of item 5's label.

### F6 (medium) — the counter pin is asserted to be in the receipt; it is not
- claims.md:166-167: "The counter's sha256 is pinned above and in `measure-before.log`;
  it is never edited after this revision."
- `git show e1d22ca:reports/round-69/measure-before.log | grep -cE 'sha256|[0-9a-f]{64}'` = **0**;
  worktree file identical (`git diff --stat` empty); the receipt's first line is `K_HELD=8/14`.
- The pin itself is correct (verified), but the sentence asserts a verification that the named
  bytes do not carry — the r68-D1 class (an identity asserted without the deriving artifact)
  reinstated in the very pre-registration that registers Q15 to catch it. Q15 cannot catch it:
  it parses only `<hash>:corpus` = `<hash>`, not a sha256-vs-file-absence claim.

### F7 (low) — frontier provenance pointer is unresolvable as written
claims.md:223: "considerthese: `2026-10-24.md` proposal 2 (provider-refusal seats recorded as
their own line)". No `considerthese/2026-10-24.md` exists at the fleet root; the file is
`revenger-shokunin/considerthese/2026-10-24.md` (proposal 2 at its line 17: "### 2. The first
honestly falsified coverage claim: C05 (APK) moved frontier → uncovered"). Also the sentence is
spliced onto the tail of the "Registered (not claims)" paragraph (claims.md:215-226), so it reads
as part of D1-D5 routing. Content is right; the pointer form is not.

### F8 (low, pending not broken) — D4 not landed at HEAD
`grep -c 'round-69' SCORECARD.md` = **0**; claims.md:216-217 registers "D4 reconciliation
appended". No round-69 SCORECARD entry exists at `35e1258`. Tracked as pending; must be present
before the final measured commit or the registered repair is unfulfilled.

## 3 · Does any r68 failure mode repeat?

| r68 mode | r69 state | evidence |
|---|---|---|
| D1 false tree-identity sentence | **partially repeated** — F6 (pin location asserted against contradicting bytes) and F1 (values asserted against the receipt); the D1 *repair* itself (Q15 + restatement) is only a notation checker (F4) | §2 F1, F4, F6 |
| D2 uncommitted wave-slot grant | **repaired** — raw `acquire` line committed | §1 row |
| D3 unnamed attack-share predicate | **repaired** — both predicates named; spec has no `planner` | §1 row |
| D4 SCORECARD prose inconsistency | **pending** at HEAD | F8 |
| C2 falsified by v3's F1/F2 (stated-but-not-printed; literal-as-derived) | F1 **genuinely repaired** (all 18 cited S038 line numbers printed); F2 **residual** in `readout.py:49-50` | §1 row, F5 |
| C7 kill not attributable (`C7_MUTANT_KILLED_ATTRIBUTED 0/1`) | **repeated under a new name** — `Q15_FALSE_KILLED` is `rc != 0` with a branch that prints the kill marker for a file that demonstrates nothing | F2 |
| non-hermetic measurement input | pre-disclosed for Q15 (`LANE` hard-coded, `measure.py:30`, claims.md:167-170) — disclosed, not a defect | §1 |

## 4 · Verdict

**LEDGER-BROKEN.** The C1 claim's numbers, the base/label, both sha pins, the receipt
provenance (exact replay), the void floors and the D2/D3 repairs all re-derive cleanly, and the
r68 F1-class defect is genuinely repaired. But the C2 pre-registration misstates its own
red-before receipt (F1: `pass`/`yes` where the receipt prints `n/a`), asserts a pin the receipt
does not carry (F6), defines `Q15_RESTATE_OK` as something the checker does not test and
false-kills the correct case (F3), and makes an unattributed `rc != 0` the falsifier of a
calibration claim (F2) — a repeat of the r68 C7 attribution failure the round registers as its
own mining target. Criterion Q15 as written also overstates its coverage (F4) and leaves the
Q04-F2 contradiction in the cited readout (F5).

Fixable without touching the build: restate claims.md:137-139 to the receipt values
(`Q15_SELFTEST=n/a`, `Q15_FALSE_KILLED=n/a` on the base tree, with the checker's arrival at
`e1d22ca` named as the reason), delete the "and in `measure-before.log`" clause or append the
pin line to the receipt, add an attributed `Q15_FALSE_KILLED_ATTRIBUTED` leg keyed on the
checker's message text, and state in the claims that `Q15_RESTATE_OK` requires the lesson to
carry both a `tree-identity restatement:` line and a failing `tree-identity false-sentence:`
quote. All four are pre-registration text/mechanism edits at a *frozen* artifact, so they are
for the L1/operator, not for this seat.

confidence: **high** — every finding is a committed byte or a reproduced command output; no
network, no lane writes.
