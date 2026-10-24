# W2AttackRecordForgery — C2 ledger-discipline attack (round-63 falsify, 2026-10-24)

Seat: revenger-r63.W2AttackRecordForgery (leaf; no subagents, no git/jj mutations, no
target execution — no npx, no binwalk/unblob invocation; only `oracle_check.py`,
re-hashing and static reads on committed bytes at tip 2a34e45562d965f9c8d32f6a27d2f2efa2e7d04e,
tree clean for `corpus/live/runs/round-63/` at attack time). Tooling: none installed
(no pacman — host-paused; no uv/npx/binary installs needed).

## 0. Axes named

1. **Inline-check reach**: which committed *executable* bytes constrain the round-63 C2
   record (`measure.py` F block, `oracle_check.py`) and what each is blind to.
2. **Forgery realizability**: can a self-consistent record+stdout+receipt set be built
   that every committed check passes (transplant / content-lie / receipt-only / minimal)?
3. **Credit surface**: does any `claims.md` C2 sentence credit more than the committed
   artifacts can witness?

## 1. Inline-check reach (re-read, not trusted from prior reports)

- Frozen counter `reports/round-63/measure.py:40-44` (F): counts any dict with truthy
  `evidence_id` + non-null `normalized_result`, keyed by `operation`. It never reads
  `receipt.json`, `stdout.raw`, `stderr.txt`, or any digest. **All `C2_*` labels in the
  same file (lines 72-122) are round-36 icon-verifier mutants — the frozen counter
  contains zero executable checks of the round-63 firmware record beyond presence.**
- `corpus/live/runs/round-63/oracle_check.py` (229 lines, read in full): checks
  `operation`, `subject.digest.sha256` ↔ fixture bytes, `input_size`, and region
  offset/size/signature pairing against `truth.json` re-derived from the fixture image.
  **The string `evidence_id` does not occur in the file.** It never reads the receipt.
- Consequence: the "byte-oracle agreement + real-run receipt + LEDGER cross-checks" of
  C2 are (i) one executable content check, (ii) one executable presence counter, and
  (iii) *prose* cross-checks in committed `LEDGER.md` rows plus the falsify-spec
  W2VerifyC2 checklist — process, not code.

## 2. Forgery experiments (all bytes in /tmp/revenger-r63-forgery, removed after)

Baseline re-runs (my own): `oracle_check.py` on the committed record → `ORACLE OK`,
exit 0; sha256 of record set: inspection.json = stdout.raw =
`f6997835…3aa71f9`, stderr empty, receipt `e930a549…5c6b94d`, fixture `bdfe9f46…8510be`,
truth `9663f90b…d5a65e6`, generator `4e5d5975…93db4` — all as LEDGER says **except one** (§3).

**Forgery A — foreign Evidence ID transplanted across record+stdout+receipt, digests
recomputed** (donor: `ev_5cc39f35…b33c6cf7d`, the genuine 20261012T164246Z archive
record ID; occurs exactly once in inspection.json, replaced, stdout.raw rewritten
byte-identically, receipt `evidence_id`+`stdout_sha256` recomputed):

- `oracle_check.py` → **`ORACLE OK`, exit 0** (reproduces the build-wave's finding;
  expected, since the checker never reads IDs).
- All five falsify-spec W2VerifyC2 "(b) real-run receipt" checks **pass on the forgery**:
  command names `rea-agents@6.5.0 inspect-firmware-regions`, exit_code 0,
  fixture_sha256 == sha256(fixture), stdout_sha256 == sha256(stdout copy) == inspection
  bytes, receipt evidence_id == record evidence_id.
- Frozen-counter F block (lines 40-44 verbatim) over the forged tree →
  `{'inspect_firmware_regions': 1}` → **firmware family counted, F=5/8 unchanged.**
- **No committed executable rejects Forgery A.** What does contradict it is
  *reconciliation across committed rows*: the donor ID is named in **7 committed files**
  (`corpus/knowledge/round-63-zip-central-directory-evidence.md` — the C06 candidate,
  which binds it to `artifact-inspection.json` sha `2fec924b…` at its lines 159/250 —
  plus the donor's own LEDGER/record and SOURCES.md), so the forged corpus shows one
  Evidence ID bound to two different record digests; and the committed LEDGER.md rows
  27 pin the genuine record-set digests (`f6997835…`), so any record-byte change trips
  the ledger table. Both are **adjudication stoppers, not inline checks**.

**Forgery B — genuine ID, one content lie** (region 1 `offset` 512→513, digests
recomputed end-to-end): `oracle_check.py` → **`ORACLE MISMATCH`, exit 1**. The byte
oracle is load-bearing exactly where it looks: content is not forgeable against the
committed authored fixture triple (deterministic generator, byte-preserved).

**Forgery C — receipt-only rewrite** (change `command`/`exit_code`/`duration_seconds`,
or swap in any self-consistent receipt; record+stdout+fixture untouched): **no
committed artifact detects this** — see §3.

**Forgery D — invented minimal record** (`{"evidence_id":"ev_<64hex>","operation":
"inspect_firmware_regions","normalized_result":{}}`): counted by F (lesson M34 already
discloses this) and rejected as C2 evidence by claims.md (b)+(c) themselves — claims.md
does **not** over-credit the counter here.

## 3. Fresh defect located: the receipt is the unpinned artifact, and its ledger pin is mis-keyed

Committed `LEDGER.md:26` records the receipt digest as
`e930a549db16a180d4ab05307e073cd71599a3317b9f3d15a0d97843d5c6b94b`.
The committed receipt bytes hash to
`e930a549db16a180d4ab05307e073cd71599a3317b9f3d15a0d97843d5c6b94d` — verified three
ways (`sha256sum`, `hashlib`, `git show HEAD:… | sha256sum`; `git status` clean), both
files landed in the same build commit 2a34e455. **The committed ledger's own digest
tripwire is wrong in the final hex char for exactly the receipt** — every other row of
its table (fixture, generator, truth, inspection/stdout, stderr, checker-at-check-time)
re-verified correct. Net effect:

- The record set's tamper-evidence is real for `inspection.json`/`stdout.raw` (pinned
  at LEDGER:27, correct) and the fixture triple — but **the receipt is effectively
  unpinned**: Forgery C leaves every correctly-pinned byte untouched and contradicts
  nothing. `exit_code`, `duration_seconds` and the verbatim `command` line are
  unattestable strings (U4 already marks receipt authenticity UNKNOWN; the mis-keyed
  pin is a new, concrete instance: the one row that would have made receipt bytes
  tamper-evident is false at the tip).
- O9's five cross-checks themselves all re-verified TRUE (they compare receipt *fields*
  against other artifacts, not the receipt digest), so the defect is confined to the
  route-table row — but it means the C2 ledger contains one false OBSERVATION row.
- Related, by design: `oracle_check.py` is deliberately cited "by path and behaviour,
  not by a pinned digest" (LEDGER:28), so "oracle_check.py prints ORACLE OK" is not
  committed-bytes evidence either; the falsify-spec's W2VerifyC2 covers this by
  requiring the seat to re-derive every region from fixture bytes itself.

## 4. Does any claims.md sentence over-credit?

- **C2(a)** — envelope fields: exactly what the F counter sees; claims.md pairs it with
  (b)+(c), so no over-credit.
- **C2(b)** — "*is the output of one real npx -y rea-agents@6.5.0 … run (receipt
  committed with command, exit code, fixture SHA-256, stdout SHA-256, Evidence ID)*":
  this is the one clause whose evidence (a self-asserted receipt) cannot witness the
  assertion. Forgery A/C satisfies every named artifact. Because no wave may execute
  the target, real-run-ness is permanently unverifiable *inside the wave rules*; the
  content it would uniquely add ("binwalk 3.1.0 actually fires on these bytes" — the
  M33 fixture premise) is receipt-trusted only. **Localized over-credit: the real-run
  clause credits a property no committed artifact can falsify; it holds only as long
  as the receipt is honest.** The ledger's U4 discloses exactly this — so the claim is
  honest about the gap, but the sentence as written still asks the reader to accept
  "real run" on receipt self-assertion.
- **C2(c)** — byte-oracle agreement: fully witnessed by committed bytes (fixture triple
  + checker + seat re-derivation; Forgery B shows the check bites). No over-credit.
- **Evidence ID as a named receipt field**: IDs are recorded identifiers — four seats
  could not recompute any (`corpus/knowledge/evm-saved-interface-candidates.md:79-80`;
  same stance at `round-62-evm-dispatch-byte-evidence.md:169-171`). Treating the ID in
  the receipt as real-run evidence over-credits it by one notch: it proves internal
  consistency only, and only cross-row reconciliation (donor-ID double-binding, §2A)
  would ever expose a transplant.

## 5. Verdict

**Discipline HOLDS with named residuals — with one located leak and one located
defect.** Content is genuinely oracle-bound to committed authored bytes (Forgery B
killed); record-set bytes are ledger-pinned and the pins verify; an Evidence-ID
transplant passes every inline check (Forgery A) and is stopped only by committed
*cross-row* reconciliation (7 donor rows + LEDGER:27) at adjudication — a process
stopper, not an artifact check. **Leak located: the receipt** — its committed ledger
pin is mis-keyed (`…5c6b94b` vs actual `…5c6b94d`, LEDGER:26), leaving command /
exit_code / duration free fields, and claims.md C2(b)'s "output of one real npx run"
clause rests on that unpinned, self-asserted artifact alone. Second residual, already
disclosed upstream: F is a presence counter (M34) and `oracle_check.py` is digest-unpinned
by the ledger's own admission (LEDGER:28), so both matter only through the falsify
seat's independent re-derivation.

## 6. Evidence commands (all re-run by this seat)

```sh
sha256sum corpus/live/runs/round-63/{inspection.json,receipt.json,stdout.raw,stderr.txt,oracle_check.py} \
          corpus/fixtures/firmware-r63/{generator.py,truth.json,firmware-r63.bin}
git status --porcelain corpus/live/runs/round-63/      # clean
git show HEAD:corpus/live/runs/round-63/receipt.json | sha256sum   # …5c6b94d vs LEDGER:26 …5c6b94b
python3 -B corpus/live/runs/round-63/oracle_check.py   # ORACLE OK, exit 0 (baseline)
# forgeries in /tmp/revenger-r63-forgery (transplant + content-lie), each:
python3 -B <tree>/corpus/live/runs/round-63/oracle_check.py
#   A transplant: ORACLE OK exit 0; B offset-lie: ORACLE MISMATCH exit 1
grep -rl ev_5cc39f356009773bb3d8a214ec39536a99f0799f6709f4cd7bb3badb33c6cf7d corpus
#   → 7 committed rows bind the donor ID (incl. C06 candidate at its lines 159/250)
```

Scratch `/tmp/revenger-r63-forgery` removed after this report. No corpus/live or
corpus/fixtures byte touched; no target executed; no pacman transaction.
