# round-79 run ledger — native-authenticode family record through the current producer

One bounded, static, non-executing producer run, saved as producer-emitted bytes:

- fixture: `corpus/fixtures/native-auth-r79/fixture.dll` (authored inert minimal native
  PE32 with one 8-aligned WIN_CERTIFICATE entry; generator `generator.py` byte-verifies
  its own premises and regenerates byte-identically; truth pin `truth.json` sha256
  `813778b9d97cf74f2aa5ba1c963cecba5c91ba72adebc08b50d7ec8b3196cf80`). The embedded
  PKCS#7 blob is structurally valid DER (ContentInfo → signedData, one SignerInfo) and
  cryptographically meaningless by construction — the producer's own limitations say it
  decodes structure and never verifies signatures, chains, timestamps or digest
  coverage. No real credential exists here.
- record: `inspection.json` = the exact stdout of
  `rea inspect-pe-certificates <fixture> --format json` (rea 6.8.0, provider
  `rea-pe-certificates`), stdout sha256
  `317b0b744f6d18725387cedc73085edb6b197c22de800e2ba731842397447b79`, exit 0, stderr
  empty; receipt in `receipt.json`.
- identity oracle: `python -B ../../fixtures/native-auth-r79/oracle_check.py
  ../../fixtures/native-auth-r79/truth.json inspection.json
  ../../fixtures/native-auth-r79/fixture.dll` → `ORACLE OK (27/27 checks)`:
  operation `inspect_pe_certificates`, table at file offset 1024 / 120 bytes, data-directory
  slot at 216/8, entry length 120, revision 0x0200 (=512), type 0x0002 (=2, "pkcs7"),
  payload at 1032 / 109 bytes with sha256 `045837b5…eba41c`, content-type OID
  1.2.840.113549.1.7.2 (signedData), digest OIDs [2.16.840.1.101.3.4.2.1], signer SKI
  `abcd`, signature algorithm 1.2.840.113549.1.1.1 (rsaEncryption), coverage
  complete/1/0, subject digest == fixture sha256 — the producer's own parser derived
  exactly the authored structure from the authored bytes.
- observation vs inference vs unknown: the record's structural fields are observations
  (producer-derived from committed bytes); that the F2 counter counts this family is a
  predicate evaluation (mapping revision frozen in `reports/round-79/claims.md` before
  the run); whether the closure judge accepts the family move as an honest coverage
  improvement is outside this ledger (unknown, adjudicated externally).
- F is presence-only (routed debt, r63): this ledger's claim text is the gate — a real
  current-producer record on a real native-authenticode surface, not a counter-only
  flip.
- Scratch probes that informed this run (not evidence): the shape pre-probe is
  committed at `reports/round-79/preprobe-cert-shape.log` (two refused iterations
  disclosed there: arbitrary 64-byte payload and ContentInfo-without-SignerInfo both
  `invalid_request`, no record).
