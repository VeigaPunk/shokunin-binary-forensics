# R64RevengerLedger — ledger-discipline reversal: C07 entry draft, S036/S037 rows, evidence-ID transplant corollary

Seat: revenger (round 64, hyaku). Read-only on `corpus/**`; no git/jj mutation; no
installs (`installs: none`). Everything below is classed OBSERVATION (I ran it or read
it this session), RECORDED (read from a named saved artifact, cited), INFERENCE
(bounded interpretation, marked), or UNKNOWN (open).

## 1. Axes

- **A — trace fidelity**: does every conclusion in the C07 entry draft and the S036/S037
  source rows carry its class (observation/inference/unknown) and a tier-A basis for its
  scope?
- **B — transplant corollary**: reverse-engineer the receipt/Evidence-ID binding check the
  named owner round must register, and name one concrete attack it must catch.
- **C — routability**: is "a future calibration round" bounded enough to own that check?

## 2. State of the round's artifacts (dependency finding)

- OBSERVATION (re-checked at report time): `corpus/knowledge/round-64-firmware-region-byte-evidence.md`
  does **not exist** in the lane tree; `corpus/lessons/round-64.md` does not exist;
  `corpus/SOURCES.md` holds exactly 35 `S` rows (S001–S035) — **no S036/S037 rows landed**.
  Per-seat rule I did not wait on the scribes; sections 3–5 therefore deliver (a) the
  discipline model, (b) an **independent blind byte-derivation** the absent draft must match
  value-for-value, and (c) the trace rubric to run when it lands. This is the same
  dependency R64CriticEntryDeps recorded independently (its §"Dependency finding").
- OBSERVATION: the scribe-side inputs exist and are strong: pinned-tag guide snapshot with
  sidecar (`.ufo/waves/round-64/source-snapshots/rea-firmware-guide.md`, sha256
  `e422b481…93609`, tag commit `3b79af28…2a1847`, blob `15281917…227ed`; R64SourceReaGuide
  §2), a field-level record↔truth↔receipt readout (`.ufo/waves/round-64/record-recon.md`),
  and a 9-file digest census with ledger cross-check (`.ufo/waves/round-64/scout-fixture-bytes.md`).

## 3. The discipline model the artifacts must satisfy

- RECORDED: PROVINCE.md:4-7 — the lane works "with an evidence-ledger discipline: every
  conclusion separates observation, inference, and unknown, and cites Evidence IDs."
- RECORDED: `corpus/knowledge/seed.md:22-25` (the C10 row's cited surface) — "Every REA
  conclusion is ledger-bound: observation vs inference vs unknown, each tied to an Evidence
  ID … A claim without a cited Evidence ID is a hypothesis, not a finding."
- RECORDED: `corpus/live/runs/round-63/LEDGER.md` (the model): every row carries a class
  (OBSERVATION O1–O11 / INFERENCE I1–I6 / UNKNOWN U1–U6), a **basis** column naming the
  exact saved field or command, and a result column; its fixture table re-hashes every
  artifact from disk (rows at `:15-28`, including the disclosed receipt-pin correction at
  `:26`, found by W2AttackRecordForgery). Separation of layers is explicit: engine facts
  from the record envelope vs CLI version from the receipt command line (`:22`), and
  author-side probes (O11 unblob) kept outside the record's route.
- RECORDED: the Q09 boundary is corpus law — "digests bind the hashed bytes only; Evidence
  IDs are recorded identifiers" (`corpus/knowledge/commonjs-destructured-require-edges.md:204`),
  four seats failed to recompute any `evidence_id` (`corpus/knowledge/evm-saved-interface-candidates.md:79-80`),
  and the round-1 gate rejected equating receipt hashes/Evidence IDs with producer origin
  (`corpus/lessons/round-1.md:16`; lesson M13).

## 4. Independent blind byte-derivation (the diff-target for the C07 draft)

OBSERVATION — I derived the fixture layout **from `firmware-r63.bin` bytes alone** (phase 1),
loading `truth.json`/`inspection.json` only afterwards for comparison (phase 3). No author
readout script, no oracle-sized slices: member spans come from a whole-suffix `zlib`
decompress with required EOF; compressed size = consumed suffix; padding = complement spans,
checked all-zero. Reproduce (stdlib only, cwd anywhere):

```python
import hashlib, zlib, json, pathlib
L = pathlib.Path('/home/vgpnk/Projects/shokunin/revenger-shokunin')
img = (L/'corpus/fixtures/firmware-r63/firmware-r63.bin').read_bytes()
H = lambda b: hashlib.sha256(b).hexdigest()
members = []
for i in range(len(img)):
    if img[i] & 0x0F != 0x08: continue          # zlib CMF: compression method CM=8
    d = zlib.decompressobj()
    try: out = d.decompress(img[i:])
    except zlib.error: continue
    if d.eof: members.append((i, len(img)-i-len(d.unused_data), len(out), H(out)))
print(len(img), H(img)); print(members)
```

My output (OBSERVATION, this session):

| Value | Derived from bytes | truth.json | inspection.json (record) |
|---|---|---|---|
| image size / sha256 | 2048 / `bdfe9f46…a8510be` | equal | `subject.digest.sha256` equal; `input_size` 2048 |
| member A | start 512, compressed 79, decompressed 78 B, sha `a5718481696cea25…df7b86` | regions[1] equal on all four | regions[0]: offset 512, `reported_size` 79, `signature` `zlib` (record carries **no** decompressed digest) |
| member B | start 1024, compressed 90, decompressed 97 B, sha `2d0d86aa6fbbbb0e…9aba9` | regions[3] equal on all four | regions[1]: offset 1024, `reported_size` 90, `signature` `zlib` |
| padding | spans (0,512), (591,433), (1114,934), all bytes `00` | regions[0]/[2]/[4] equal | **absent** from the record; `coverage` = `signature_scan` |
| receipt fields | — | — | `receipt.json`: exit 0, `fixture_sha256` `bdfe9f46…`, `stdout_sha256` `f6997835…` = H(inspection.json) = H(stdout.raw) (byte-identical pair, record-recon §5), `evidence_id` `ev_aae7529f…` = record's ID |

This is exactly the observation layer claims.md §C1 demands ("each value derived in-entry by
command from the fixture bytes") and satisfies the blind-independence admission condition
(Q03): **a fresh seat can now diff the draft against this table value-for-value.** It also
sharpens R64CriticEntryDeps' data-flow rule: the draft's sizes must come from consumed
suffix/EOF (as above), never `image[offset:offset+truth_size]` — the round-63 checker's
oracle-sized slice is comparison material, not derivation.

## 5. Trace rubric — what the C07 draft and S036/S037 rows must show (Axis A)

**Class budget the draft must respect** (each item: command + output in-entry, then class):

- OBSERVATION-only: every value in the §4 table; S036 quote list with per-quote line numbers
  against the **tag** snapshot sha `e422b481…`, tag commit `3b79af28…` (R64SourceReaGuide §3,
  all quotes ≤25 words, max 21); S037 bundle composition = authored fixture bytes +
  `truth.json` + saved record + round-63 LEDGER (scout census: 8/9 files match recorded
  digests; the LEDGER's own digest `25a4a18b…` is **unrecorded** — cite it by path+line like
  S035 does, not by a self-digest pin).
- INFERENCE (must be labeled, fixture-scoped): "bytes ↔ record correspondence" precision/recall
  2/2; "digest agreement is checker-side — the record carries no decompressed digest" (round-63
  ledger I2); `size_basis=provider_reported_validation_unknown` means provider-claimed sizes
  coincided with truth here but are not generally validated (I3).
- UNKNOWN (must stay open, not absorbed): entropy scanning — **S036 contains zero entropy
  text** (R64SourceReaGuide §5, `grep -c -i entropy` = 0), so no entropy claim may be made
  from it; extraction (record `extractions={}`; unblob named by S036 Q1/Q2 but unexercised by
  the record); Evidence-ID recomputation (four seats failed — recorded identifiers only);
  producer origin (round-1 gate, internal consistency only); other signature families (U1).
- Row-scope boundaries: S036 is tier A **for route-scope sentences at the pinned tag only** —
  the drift finding (main = 15474 bytes, sha `d4a25c85…` ≠ tag) makes tag citation mandatory;
  quoting `main` would cite bytes the 6.5.0 producer never shipped. S037 is tier A **for
  byte/record correspondence only**. The `corpus/SOURCES.md` "Leads (unopened)" bullet —
  "REA firmware guide … open it when the firmware family is claimed" — is exactly discharged
  by S036.
- Verdict-shaped finding (no judgment issued): **no route-scope conclusion may rest on the
  round-63 checker alone** — its `truth→size→slice` data flow makes it an oracle-comparison
  tool (R64CriticEntryDeps counterexample), so the draft's derivations must be independent of
  it, per §4.

## 6. Evidence-ID transplant corollary (Axis B)

RECORDED — routed input 4 (claims.md, "Frontier and routed debt" item 4): owner = "a future
calibration round that registers a receipt/Evidence-ID binding check; this round records the
mechanism in the lesson"; round-63 lesson `:62` states the gap: "no committed check binds a
receipt/Evidence ID to origin."

**Why the check must recompute digests and treat the ID as opaque** (INFERENCE from corpus
law + recorded attempts): the ID is not recomputable (§3, four-seat failure), so it cannot be
derived from content; and recorded pins drift (round-63 LEDGER `:26` receipt pin was one hex
char off at every commit until W2AttackRecordForgery caught it). Therefore every digest in the
chain must be re-hashed from bytes at check time, and the ID functions purely as a **join key**
whose global use must be injective.

**Binding-check spec** the owner round must register (INFERENCE, harness precedent = the
frozen `measure.py` mutant-on-tree-copy pattern):

1. Partition `corpus/live/runs/**/*.json` with the frozen F predicate (truthy `evidence_id` +
   non-null `normalized_result` = record; digest-field JSON without it = receipt).
2. **R→S**: `receipt.stdout_sha256 == H(record bytes)` where raw output is retained
   (round-63: `stdout.raw` byte-identical to `inspection.json`).
3. **R→F**: `record.subject.digest.sha256 == H(fixture bytes at the path parsed from
   receipt.command) == receipt.fixture_sha256`.
4. **X→ID**: `receipt.evidence_id == record.evidence_id ==` the ID regex-extracted from that
   run's `LEDGER.md` (regex discipline precedent: `measure.py` K/ROW_OPS blocks).
5. **Injectivity (the transplant-catcher)**: across the whole corpus, one `evidence_id` maps
   to exactly one `(H(record bytes), H(fixture bytes))` pair — registry computed from the
   tree at check time, never committed.
6. Attribution: non-zero exit with a registered endswith message (C3/C4 pattern), red-before
   = planted transplant on a scratch tree copy must be killed, honest copy green.

**The one concrete attack the check must catch** — *self-consistent receipt re-signing with
ID reuse*: duplicate `corpus/live/runs/round-63/inspection.json` to
`corpus/live/runs/round-64/inspection.json`, change `normalized_result.regions[0].offset`
512→0 (claiming a zlib member at 0, which the bytes refute — offset 0 is `00`-padding), keep
`evidence_id: ev_aae7529f…`, and mint `round-64/receipt.json` with
`stdout_sha256 = H(forged record bytes)`, unchanged `fixture_sha256`/`command`/exit 0.
INFERENCE (from the read code, not executed): every existing per-pair guard passes — the
`receipt_ok()` conjunct set (`corpus/verify_icon_languages.py:118-120`,
`verify_multi_icon_states.py:122-123`) checks the pair **internally**, and the newly landed
in-script C4 controls (`:149-153` / `:151-153` respectively) forge only a mutated copy of
that same receipt, so a consistently re-signed forged pair is out of scope for all of them;
the F counter counts the forged record (predicate met). Only prong 5 fires (same ID → two
distinct record digests) together with a bytes-side falsification (the claimed offset-0
member does not exist under the §4 derivation). A fresh-random-ID variant of the same
forgery is caught by prong 4 (no honest LEDGER row binds it) — weaker, which is exactly why
the injectivity prong, not field equality, is the load-bearing one.

## 7. Routability verdict (Axis C)

**VERDICT: bounded enough to route — the owner round is named, the surface is enumerable,
the harness pattern exists, and red-before is constructible — conditional on three
pre-registration obligations the owner round must freeze before coding:**

1. **Receipt-field heterogeneity**: `corpus/live/runs/round-35/producer-receipt.json` names
   its digest field `output_sha256`, not `stdout_sha256` (RECORDED:
   `corpus/knowledge/digest-scope-versus-provenance.md` `recheck:` header and §Provenance).
   The check must enumerate accepted receipt field names (or fail closed with a disclosed
   exception list) — otherwise it is unsound for r35-shaped receipts or never green.
2. **Raw-output-not-retained policy**: r35 is a *recorded* permanent mismatch (saved file
   `74a45d0c…` vs receipt-reported `8c8d96db…`, raw output not retained; same entry, claim 1).
   Prong R→S cannot hold there. The owner must pre-register which prongs apply to which
   historical runs (strict for pairs with retained raw output; caveat-classified otherwise)
   or the check cannot satisfy red-before → green-after at all.
3. **Machine-readable joins without new mutation surface**: LEDGER prose joins by frozen
   regex (precedent exists in the frozen counter); the uniqueness registry is derived from
   the tree per run (a committed registry would violate the `corpus/live` byte-preservation
   void condition and create its own transplant target).

And the check's pass must ship with the Q09 disclaimer verbatim: green means
internal-consistency + uniqueness of the binding, **never** producer origin (round-1 gate,
S015). The mechanism sentence this round records in `corpus/lessons/round-64.md` should carry
all three obligations + the named attack so the owner round inherits a bounded spec, not a
title.

## 8. Findings for L1 (numbered, no judgment issued)

1. Draft/lesson/S036/S037 all unlanded at report time (dependency; §2). The §4 table is the
   ready-made blind-independence diff target for Q03 admission checking.
2. The draft must derive sizes by consumed-suffix/EOF, not oracle slices (§4, §5) — the only
   currently-available checker cannot serve as the derivation source (§5).
3. S036's decisive scope limit is the zero-entropy text plus the tag≠main drift; both belong
   in the row's scope cell, not only the lesson (§5).
4. The transplant corollary has a concrete, one-paragraph attack (§6) and a registrable check
   shape (§6 items 1–6); route it with the three §7 obligations frozen.
5. `installs: none`. Scratch: none created outside this report.

Report: .ufo/waves/round-64/R64RevengerLedger.md
