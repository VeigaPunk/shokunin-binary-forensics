# W2AttackOracle — mutation test of the C2 byte oracle (round 63 falsify)

**Seat:** `revenger-r63.W2AttackOracle` (leaf mutation-tester, no subagents dispatched)
**Axis:** coverage (C2 / byte-oracle agreement), calibration contribution (Q13-style clause-deletion sensitivity)
**Attacked:** `corpus/live/runs/round-63/oracle_check.py` — the C2 (c) byte-oracle gate named in
`reports/round-63/claims.md` §C2, and the saved-record/receipt envelope it is supposed to settle.
**Target bytes:** lane tip `db55bd6` ("round-63: C1 candidate entry … README still partial pending falsify wave").
Committed blob of the oracle at that tip = `d0dfd7a1cd105485e47bf52446056a2636fb803c05a404ce56da597f36ce0512`
(identical to the working-tree file; `git diff HEAD -- corpus/live/runs/round-63/oracle_check.py` is empty).

**Verdict in one line: C2 is NOT falsified** — the oracle is a genuine, non-vacuous, clause-deletion-sensitive
gate for every forgery it is credited with; but the credit line in the committed prose over-reaches in two
places, and two independent coverage gaps are named (neither falsifies C2's F count).

---

## 1. Method

All mutation was done in `/tmp/revenger-r63-W2AttackOracle/` (a **byte-mirrored** tree
`corpus/live/runs/round-63/` + `corpus/fixtures/firmware-r63/`). The mirror is required: the oracle
derives its default record/truth paths from `HERE.parents[3]`, so a flat `/tmp` copy raises
`IndexError: 3` at import time — a copy one level too shallow crashes before it can judge anything.
The repo file was **never** written; every probe restored from a pinned pristine backup and re-verified
by SHA-256 afterwards.

Detector: `python3 -B corpus/live/runs/round-63/oracle_check.py` (the committed oracle, unmodified
except in the explicitly-labelled mutant copies).

Kill semantics, stated before the runs:

| verdict | meaning |
|---|---|
| **KILLED** | exit ≠ 0 **and** last stdout line is exactly `ORACLE MISMATCH` — an attributed rejection |
| **SURVIVED** | exit 0 and last stdout line is `ORACLE OK` — the forgery slipped through |
| **CRASH** | exit ≠ 0 without `ORACLE MISMATCH` as the last line — *not* a kill (a mutant that cannot run proves nothing) |

Two harness bugs were found and fixed before any result was recorded; both are noted because the
first versions would have produced false kills:
1. A single-line `mismatch(...)` deletion leaves an empty `if` body → `IndentationError`. Those mutants
   exit 1 but print nothing; under a naive `rc != 0` rule they score as kills. Fixed by replacing the
   clause with `pass  # MUTANT: clause deleted` (or `if False: … pass` for multi-line blocks) and
   requiring `py_compile` success **before** a mutant is used.
2. Mutant files placed outside the mirrored tree crash on `HERE.parents[3]` → fixed by placing mutants
   at the same tree depth as the real oracle.

Every mutant was additionally required to be **green on pristine bytes** (all 16 are; see §5), so a
mutant's failure to kill is attributable to the deleted clause and not to a broken mutant.

---

## 2. Probe results — the five requested probes

### Baseline (pristine, repo bytes)

```
$ python3 -B corpus/live/runs/round-63/oracle_check.py
REGION name=padding kind=padding offset=0 size=512 record=not-expected padding=OK
REGION name=diagnostic-note kind=zlib offset=512 size=79 offset=OK size=OK signature=OK decompressed_sha256=OK (a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86)
REGION name=padding kind=padding offset=591 size=433 record=not-expected padding=OK
REGION name=component-note kind=zlib offset=1024 size=90 offset=OK size=OK signature=OK decompressed_sha256=OK (2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9)
REGION name=padding kind=padding offset=1114 size=934 record=not-expected padding=OK
ORACLE OK
exit=0
```

### P1 — shift one region offset by 1 byte → **KILLED, field named** ✅ (as expected)

Mutation: `normalized_result.regions[0].offset` 512 → 513 in a copied `inspection.json`.

```
REGION name=diagnostic-note kind=zlib offset=512 size=79 offset=MISMATCH size=OK signature=OK decompressed_sha256=OK (…)
MISMATCH normalized_result.regions[0].offset: expected 512, got 513
ORACLE MISMATCH
exit=1
```
The mismatch names the exact field and both values. **KILLED.**

### P2 — drop one region → **KILLED, two independent fields named** ✅ (as expected)

Mutation: `normalized_result.regions` truncated to its first element (`component-note` removed).

```
REGION name=component-note kind=zlib offset=1024 size=90 record=MISSING offset=MISSING size=MISSING decompressed_sha256=OK (…)
MISMATCH normalized_result.regions: expected 2 reportable regions, got 1
MISMATCH normalized_result.regions[1]: missing reported region
ORACLE MISMATCH
exit=1
```
Both the count clause and the per-region missing clause fire. **KILLED.**

### P3 — alternate image, same size (2048 B), record digest recomputed → **KILLED at the identity binding** ✅ (as expected)

Mutation: byte `0` of the image flipped `00`→`01` (inside the declared padding span at offset 0),
then `subject.digest.sha256` recomputed to the new image digest
(`75d6743d02c015faaf1fc6dc51653eb1ff425dd098bf9fa1e3b644f51eac9231`), so the record agrees with
the swapped image.

```
REGION name=padding kind=padding offset=0 size=512 record=not-expected padding=MISMATCH
MISMATCH truth.image.sha256: expected 'bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be', actual 75d6743d02c015faaf1fc6dc51653eb1ff425dd098bf9fa1e3b644f51eac9231
MISMATCH truth.regions[0].fill_hex: padding bytes do not match the declared fill
ORACLE MISMATCH
exit=1
```
The **truth-side** image digest (`truth.image.sha256`) is the binding that catches this: recomputing
the record's digest does not launder the swap, because the oracle re-hashes the image bytes and
compares them to the *authored* truth digest, and independently re-checks the padding fill.
**KILLED** — two independent clauses fired.

A stricter variant was also run:

### P3b — alternate image swapped *without* recomputing the record digest → **KILLED, three fields named** ✅

```
MISMATCH truth.image.sha256: expected 'bdfe9f46…', actual 75d6743d…'
MISMATCH subject.digest.sha256: expected 75d6743d…, got 'bdfe9f46…'
MISMATCH truth.regions[0].fill_hex: padding bytes do not match the declared fill
ORACLE MISMATCH   exit=1
```

### P4 — green run on the real record → **ORACLE OK, exit 0** ✅ (as expected)

Restored bytes, real record, real truth: `ORACLE OK`, exit 0, all five region lines `OK`. (Transcript:
`/tmp/revenger-r63-W2AttackOracle/transcript.txt`, `PROBE M4_green_real_record`.)

### P5 — forge a saved receipt field (`fixture_sha256`) → **SURVIVED by the oracle; flagged only by the record's own digest chain, and only by hand**

Mutation: `receipt.json.fixture_sha256` = `0`*64 (record and truth untouched).

```
[oracle] rc=0 last='ORACLE OK'          <-- oracle does not see the receipt at all
```

`grep -n "receipt\|stdout" corpus/live/runs/round-63/oracle_check.py` → **no match**. The oracle
never opens `receipt.json`; it only reads `inspection.json` and `truth.json`. So the *oracle* does
not flag a forged receipt field — as expected from its scope, but worth stating plainly.

The **record's own digest chain does** flag it, when recomputed:

```
--- digest chain [pristine] ---
  receipt.fixture_sha256 = bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be
  actual_fixture_sha256 = bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be
  CHAIN_BREAKS = none
--- digest chain [mutated] ---
  receipt.fixture_sha256 = 0000000000000000000000000000000000000000000000000000000000000000
  actual_fixture_sha256 = bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be
  CHAIN_BREAKS = ['receipt.fixture_sha256 != fixture bytes', 'receipt.fixture_sha256 != record subject digest']
```

**But the chain break is detected by no committed executable.** Evidence:

* `grep -rln "receipt" corpus --include=*.py` → only the **round-37…round-53** `reviewer-verify.py`
  files (which assert `receipt['stdout_sha256'] == sha(raw)` for *their* rounds) and the four
  `corpus/verify_*.py` icon verifiers (which check *their own* round-36/42/47 receipts).
  **No script references `round-63`.**
* `ls corpus/live/runs/round-63/` → `LEDGER.md inspection.json oracle_check.py receipt.json stderr.txt stdout.raw`
  — there is **no `reviewer-verify.py`** for round-63. Of the 17 rounds under `corpus/live/runs/`
  that carry a receipt file, 16 ship an executable receipt verifier (`round-34/35/37/38/39/41–45/47–49/51–53`
  `reviewer-verify.py` / `verify_review.py`); the 11 that do not are `round-32/33/36/40/46/50/54/55/56/57/59`,
  of which `round-56`/`round-57` at least carry a prose `receipt-review.md` that recomputes the chain
  by hand (`sha256(raw)` equals receipt `stdout_sha256`; inspection subject digest = receipt
  `fixture_sha256` = truth digest = actual fixture digest). **round-63 sits in the small group that
  has a receipt, no executable verifier for it, and no prose receipt review either** — its
  `oracle_check.py` is the only script in the directory and it never opens the receipt.
* All 10 `corpus/verify_*.py --self-test` scripts: **0 failures** with the forged receipt in place
  (`failing=0`) — they never read it.
* The frozen counter `reports/round-63/measure.py` counts `F_COVERAGE` by `operation` name and
  `normalized_result` presence; it never opens `receipt.json`.

So the forged receipt field is a **silent forgery against every committed executable**: the oracle
stays green, the counter stays green, all ten verifiers stay green. Only an ad-hoc recomputation of
the chain — which I performed — reveals it.

**Verdict on P5: SURVIVED by the oracle and by every committed checker; caught only by the receipt's
own digest chain, and only when recomputed by hand.** This is a *coverage finding about the C2
envelope*, not a falsification of C2's F count (see §4).

---

## 3. Additional probes I added (the frontier walked past the five named ones)

### P6 — forge the record's `subject.digest.sha256` alone (image bytes untouched) → **KILLED**

```
MISMATCH subject.digest.sha256: expected bdfe9f46…, got '1111111111111111111111111111111111111111111111111111111111111111'
ORACLE MISMATCH   exit=1
```
The record↔image identity binding is real and independently enforced.

### P7 — alternate image whose *region content is unchanged* (flip the last byte of the trailing
padding span, offset 2047) → **KILLED**

```
MISMATCH truth.image.sha256: expected 'bdfe9f46…', actual 97c32105cfcf84a6176f311ad6eb35c2cb61919f7a6eaf596780b51461bbdcc5
MISMATCH subject.digest.sha256: expected 97c32105…, got 'bdfe9f46…'
MISMATCH truth.regions[4].fill_hex: padding bytes do not match the declared fill
ORACLE MISMATCH   exit=1
```
The identity binding is not merely a checksum of the region set — a byte change *outside* every
reportable member is still caught.

### P8 — duplicate the first reported region (count-preserving shape attack) → **KILLED**

```
MISMATCH normalized_result.regions[1].offset: expected 1024, got 512
MISMATCH normalized_result.regions[1].reported_size: expected 90, got 79
ORACLE MISMATCH   exit=1
```

### P9 — cosmetic post-run edit of the record (a `description` string) → **oracle SURVIVES, digest chain breaks**

```
record_sha256 = 774c5a2ffcf60e9c6f4655a3b49fe3cd6eb3692509dea86d7d5ba2e1c22a4f1d   (edited)
stdout.raw_sha256 = f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9
receipt.stdout_sha256 = f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9
CHAIN_BREAKS = ['receipt.stdout_sha256 != record bytes']
[oracle] rc=0 last='ORACLE OK'
[lane corpus/verify_*.py --self-test] failing=0
```
**The oracle cannot detect a post-run edit of the record** — `stdout.raw` is byte-identical to
`inspection.json` at the tip (`f6997835…` both), so the receipt's `stdout_sha256` is a genuine
tamper-evidence anchor — but **no committed script recomputes it** (see P5). This is the strongest
form of the gap: a *post-hoc* edit of the saved record is caught by nothing executable.

### P10 — hand-fabricated **minimal** record (no real run behind it) → **SURVIVES the oracle**

A record containing only the three fields the oracle reads, written from scratch:

```json
{"operation": "inspect_firmware_regions",
 "subject": {"digest": {"sha256": "<fixture sha>"}},
 "normalized_result": {"input_size": 2048,
   "regions": [{"offset":512,"reported_size":79,"signature":"zlib"},
               {"offset":1024,"reported_size":90,"signature":"zlib"}]}}
```
(record bytes sha256 `70acd2fc2e88e0c61333015931d804dc5c4e63392f82bdfaa0475346596bb825`)

```
[oracle] rc=0  →  ORACLE OK
```
**A hand-written JSON with three fields passes the byte oracle.** No `evidence_id`, no `provider`,
no `raw_result`, no `parameters`, no producer provenance — and the oracle is green. This is *expected*
from the oracle's stated scope (it settles byte agreement, not provenance — the ledger says so at
O6/I2), but it is the sharp boundary of what "byte-oracle agreement" buys, and it is worth stating
because the ledger's I1 wording ("precision 2/2, recall 2/2, zero mismatched fields across 6 checked
region fields") is scoped correctly while the *lesson*'s search-log sentence is not scoped at all.

### P11 — attacker rewrites the image **and** `truth.json` consistently → **SURVIVES the oracle (ORACLE OK)**

A wholly forged 2048-byte image (two zlib members at 512/1024, zero padding) plus a rewritten
`truth.json` that describes it, plus a record updated to match:

```
[mutator] forged image sha256=8105114ed96f6513119372793b5db3a7d95a8cbe2cb98f520e135111c69c9380 member_size=48
[oracle] rc=0 last='ORACLE OK'
```
This is the honest boundary of the mechanism: **`truth.json` is the trust anchor and is not
self-authenticating.** An adversary who can rewrite the authored oracle gets a green run. (The first
attempt at this forgery was *rejected* by the oracle — `MISMATCH truth.regions[3].offset: expected
contiguous start 1536, got 1024` — because my forged truth's region spans did not tile the image;
the contiguity clause caught a genuine inconsistency. The forgery above is the corrected, fully
tiling version and it is green.) This does **not** falsify C2: `truth.json` is a committed artifact
whose integrity is the subject of the separate preservation checks, and the claim's own U5 row in the
ledger already names oracle non-independence. But it is the limit that must not be papered over.

### P12 — forge `receipt.stdout_sha256`, `receipt.evidence_id`, `receipt.exit_code` → **oracle green, chain broken**

```
[oracle forged receipt] rc=0 last='ORACLE OK'
receipt.stdout_sha256 = 0000…0000   vs actual stdout.raw sha f6997835…   → mismatch
receipt.evidence_id   = ev_0000…0000 vs record ev_aae7529f…              → mismatch
receipt.exit_code     = 1           (the committed value is 0)            → altered
```
A forged receipt can claim a **failed** producer run and the oracle is still green.

### P13 — field-sensitivity sweep of the record (21 fields)

| record field | oracle verdict |
|---|---|
| `regions[0].offset` (control) | **constrained** — rejected |
| `regions[0].reported_size` (control) | **constrained** — rejected |
| `regions[0].signature` (control) | **constrained** — rejected |
| `normalized_result.input_size` (control) | **constrained** — rejected |
| `subject.digest.sha256` (control) | **constrained** — rejected |
| `operation` (control) | **constrained** — rejected |
| `top.evidence_id` | **UNCONSTRAINED** — oracle says OK |
| `top.predicate_type` | UNCONSTRAINED |
| `top.authority` | UNCONSTRAINED |
| `top.confidence` | UNCONSTRAINED |
| `top.provider.id` | UNCONSTRAINED |
| `top.provider.version` | UNCONSTRAINED |
| `top.subject.name` | UNCONSTRAINED |
| `top.subject.local_path` | UNCONSTRAINED |
| `top.subject.format` | UNCONSTRAINED |
| `top.normalized_result.coverage` | UNCONSTRAINED |
| `top.normalized_result.engine.name` | UNCONSTRAINED |
| `region0.description` | UNCONSTRAINED |
| `region0.reported_confidence` | UNCONSTRAINED |
| `region0.provider_id` | UNCONSTRAINED |
| `region0.size_basis` | UNCONSTRAINED |

**6 constrained / 15 unconstrained.** Every field that carries *provenance* (evidence id, provider
identity and version, engine identity, subject path/name, coverage class, authority, confidence)
is outside the oracle's scope; every field that carries *byte geometry* is inside it. The oracle's
6-field constraint set matches the ledger's I2 statement ("the record reports only `offset`,
`reported_size`, `signature`, `description`, `reported_confidence`, `size_basis`") — but note
`description`, `reported_confidence` and `size_basis` are in fact *not* constrained; the ledger's I2
describes what the record *carries*, not what the oracle *checks*, so this is a wording precision
point, not a contradiction.

---

## 4. Clause-deletion mutant matrix — is each credited clause load-bearing?

Sixteen single-clause mutants of the oracle, each `py_compile`-clean and **green on pristine bytes**
(all 16 verified — see `/tmp/revenger-r63-W2AttackOracle/mutant_control.txt`), each run against the
forgery it is supposed to catch.

| forgery | mutant (clause deleted) | result | reading |
|---|---|---|---|
| P1 offset shift | `no_offset_check` | **SURVIVED** (rc=0, `ORACLE OK`) | the offset clause is the **sole** guard for an offset forgery |
| P2 drop region | `no_region_count_check` | KILLED | redundant — the missing-region clause also fires |
| P2 drop region | `no_missing_region_check` | KILLED | redundant — the count clause also fires |
| P3 alt image, digest recomputed | `no_truth_image_sha_check` | KILLED | redundant — the padding-fill clause also fires |
| P3 alt image, digest recomputed | `no_padding_fill_check` | KILLED | redundant — the truth digest clause also fires |
| P3b alt image, raw swap | `no_truth_image_sha_check` | KILLED | redundant — subject-digest + padding-fill also fire |
| P3b alt image, raw swap | `no_subject_digest_binding` | KILLED | redundant |
| P3b alt image, raw swap | `no_padding_fill_check` | KILLED | redundant |
| P6 subject digest forged | `no_subject_digest_binding` | **SURVIVED** (rc=0, `ORACLE OK`) | the subject-digest binding is the **sole** guard for a forged record digest |
| P7 alt image, regions unchanged | `no_truth_image_sha_check` | KILLED | redundant |
| P7 alt image, regions unchanged | `no_subject_digest_binding` | KILLED | redundant |
| P7 alt image, regions unchanged | `no_padding_fill_check` | KILLED | redundant |
| P5 forged receipt | *(no oracle clause exists)* | SURVIVED | the oracle has no receipt clause to delete |

Two mutants survived, and both survivals are **informative rather than alarming**:

* `no_offset_check` survives **only** against the offset-shift forgery. The oracle's offset clause is
  load-bearing and non-redundant for that specific class — deleting it lets a +1 byte offset
  forgery through with a clean `ORACLE OK`. That is the correct behaviour of a clause-deletion
  mutant and it means the clause is genuinely detecting the defect it is credited with.
* `no_subject_digest_binding` survives **only** against the forged-subject-digest forgery (P6),
  and is redundant against both image-swap variants (P3b, P7) because `truth.image.sha256` fires
  first. So the record↔image identity binding is enforced by a two-clause pair, and neither clause
  is decorative.

The remaining twelve mutant/forgery pairs are all KILLED, i.e. **redundant** — the oracle's checks
overlap. That redundancy is a *strength* for the forgery classes it covers (P2, P3, P3b, P7 are each
caught by ≥2 independent clauses) and is why the oracle is not a one-string checker.

**Q13 read-through:** the committed prose credits the byte oracle with settling the record↔truth
agreement ("the byte oracle, not a document, is what settles the agreement",
`corpus/lessons/round-63.md` search log). The mutant matrix shows that credit is **earned for the
byte-geometry clauses** (offset / size / signature / decompressed digest / padding fill / identity
binding are each shown to detect the defect they are cited for). It is **not earned for anything
about the receipt**, because the oracle contains no receipt clause at all — the receipt is outside
its subject, and no other committed script covers it either (§2 P5).

---

## 5. What this does and does not falsify

**C2 is not falsified.** Re-running the frozen counter myself on a committed archive of the lane tip:

```
$ git archive HEAD corpus | tar -x -C /tmp/…/archive
$ cd / && python3 -B reports/round-63/measure.py /tmp/…/archive
K_HELD=6/14 score=4.3
K_ROW C06 status=partial
K_HELD_BACKED=6/14
F_COVERAGE=5/8 score=6.2
F_FAMILIES=['native-static', 'javascript', 'archives', 'firmware', 'evm']
FRESH_ROWS=18/18
C3_CONTROLS_PASS=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=2/2
HOLD_CALIBRATION=4/4
HOLD_REPLAY=10/10
HOLDS_OK=yes
exit=0
```

`F_COVERAGE=5/8` with `firmware` present → **C2's target (F 5/8) is met**, so C2 is not falsified by
the count. `C3_RECEIPT_KILLED_ATTRIBUTED=2/2` is independently confirmed on the same tree, so C3 is
not falsified either. `K_HELD_BACKED=6/14` at the tip is expected — the README C06 row is still
`partial` and flips only after the named fresh-seat Q decisions land (not this seat's decision).

**Coverage findings (routed, not claim extensions):**

* **F-A — the C2 envelope's receipt is unguarded by every committed executable.** Forging
  `receipt.fixture_sha256` (§2 P5), `receipt.stdout_sha256`/`evidence_id`/`exit_code` (§3 P12), or
  editing the record after the run (§3 P9) leaves the oracle, the frozen counter, and all ten
  `corpus/verify_*.py` green. Only a hand recomputation of the receipt digest chain detects it.
  Every other round that claims a receipt-backed record ships a verifier that recomputes the chain:
  16 of the 17 receipt-carrying rounds have a `reviewer-verify.py`/`verify_review.py` asserting
  `receipt['stdout_sha256'] == sha(raw)`, and `round-56`/`round-57` have a prose `receipt-review.md`
  doing the same by hand. **round-63 has neither** — no receipt verifier and no receipt review — and
  `oracle_check.py`, the only script in its directory, never opens the receipt. This is exactly the
  M35 shape already routed as coverage debt for the icon verifiers, one round earlier and one
  artifact over. It does not move the F counter (a presence counter) and does not falsify C2; it is
  a Q13-shaped gap in the *credit* the envelope receives.
* **F-B — "byte-oracle agreement" does not attest provenance, and one committed sentence over-reaches.**
  The oracle is green on a hand-written three-field record (§3 P10) and on a fully forged
  image+truth pair (§3 P11). The ledger states this correctly (U5 "Oracle independence", I2, and the
  "Cannot see" list), but `corpus/lessons/round-63.md`'s search-log sentence — "the byte oracle, not
  a document, is what settles the agreement" — is unscoped and reads as if the oracle settles the
  record's reality. It settles byte geometry only.
* **F-C — one committed prose sentence names fields the oracle does not check.** The ledger I2 lists
  `description`, `reported_confidence` and `size_basis` among what the record reports; §3 P13 shows
  all three (and `provider_id`, `evidence_id`, `provider.*`, `engine.name`, `coverage`, `subject.name`,
  `subject.local_path`, `subject.format`, `authority`, `confidence`, `predicate_type`) are
  **unconstrained** by the oracle. I2 is a statement about what the record carries, not about what
  the oracle checks, so this is a wording-precision item for whoever re-derives it, not a
  contradiction. Flagged because Q13 forbids crediting a verifier for clauses its run does not
  detect.

None of F-A/F-B/F-C changes a counter, and I claim no extension of any target.

---

## 6. Reproduction

Scratch root: `/tmp/revenger-r63-W2AttackOracle/` (removed after this report lands).

| artifact | path |
|---|---|
| byte-mirrored tree | `tree/corpus/{live/runs/round-63,fixtures/firmware-r63}/` |
| pinned pristine backups | `pristine/{inspection.json,receipt.json,firmware-r63.bin,truth.json}` |
| probe harness (P1–P5, restore+verify) | `harness.py` → `transcript.txt` |
| mutant harness (16 mutants) | `mutant_harness.py` → `mutants3.txt` |
| mutant pristine-green control | `mutant_control.txt` |
| receipt-chain probes (P9, P12, inventory) | `receipt_chain.py` → `receipt_chain.txt` |
| fabricated-record probes (P10, P11) | `fabricated.py` → `fabricated.txt`, `m12.py` → `m12b.txt` |
| field-sensitivity sweep (P13) | `sensitivity.py` → `sensitivity.txt` |
| frozen counter on committed archive | `measure-archive.txt` |

## 7. Preservation evidence

No repo file was written by this seat. The only repo write is this report file.

Before (lane tip `db55bd6`) and after the full probe run, the C2 artifact bytes are identical:

```
bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be  corpus/fixtures/firmware-r63/firmware-r63.bin
4e5d5975e3cf6362f6fd430f2147d42f75d011978f7d6b5ec86d224c77793db4  corpus/fixtures/firmware-r63/generator.py
9663f90b2b9f29c5beb621e554ed7584eedf5e77d4785f26a453e70dbd5a65e6  corpus/fixtures/firmware-r63/truth.json
f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9  corpus/live/runs/round-63/inspection.json
d0dfd7a1cd105485e47bf52446056a2636fb803c05a404ce56da597f36ce0512  corpus/live/runs/round-63/oracle_check.py
e930a549db16a180d4ab05307e073cd71599a3317b9f3d15a0d97843d5c6b94d  corpus/live/runs/round-63/receipt.json
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  corpus/live/runs/round-63/stderr.txt
f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9  corpus/live/runs/round-63/stdout.raw
```

`corpus/live/runs/round-63/LEDGER.md` was `d41bbeac…` at my baseline and is `25a4a18b…` at the end of
my run. **That change is not mine** — this seat never opened the ledger for writing. It is a
concurrent sibling edit: a one-line correction to the ledger's `Receipt` row, whose own text records
`pin corrected 2026-10-24: the pre-correction pin ended 5c6b94b, one hex char off the bytes at every
commit since landing — defect found by W2AttackRecordForgery`. The corrected pin
`e930a549…d5c6b94d` is the digest this seat independently measured from the file on disk, so the
sibling's correction agrees with my measurement. The ledger edit touches no byte my probes read
(record, receipt, truth, image, oracle are all unchanged), so it does not affect any result above.

`git status --porcelain -- corpus/` after the run shows `corpus/SOURCES.md`,
`corpus/lessons/round-63.md` and `corpus/live/runs/round-63/LEDGER.md` modified — **all three are
other seats' in-flight edits, not mine**; the only repo file this seat wrote is this report. The
oracle file equals its committed blob at the tip (`git diff HEAD -- corpus/live/runs/round-63/oracle_check.py` empty).

**Tooling:** none installed, none upgraded. No `pacman` transaction (host gate paused), no `uv tool
install`, no npm install, no binary download. Everything used was pre-present: `python3` 3.14.8,
`git`, `grep`, `sha256sum`, `tar`. No firmware payload was executed and no REA producer was re-run —
the only bytes touched were copies in `/tmp`.

**Cooperation note:** the wave roster contained no dependency on this seat; nothing was awaited and
no peer was blocked. One inbound IRC message (from `kotodama-r64.RevVerifyO2`, concerning round-64's
`accept-o.py` mutant indentation) belongs to a different lane and round and was left for its owner.
