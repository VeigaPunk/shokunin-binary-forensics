source: S005 — https://swgde.org/wp-content/uploads/2025/09/2025-08-05-Best-Practices-for-Computer-Forensic-Acquisitions-17-F-002-2.1.pdf — §8 "Verification and Preview", §9 "Documentation"; 17-F-002-2.1 (2025-08-05)
source: S006 — https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf — Announcement §3 "Explanation", §6 "Applicability", Abstract; FIPS PUB 180-4 (2015-08)
source: S014 — `LOG.md` — round 35 result provenance caveat (`:458`) at `8bbcb4e`
source: S015 — `corpus/lessons/round-1.md` — fleet round-1 `## Gate` (`:14-16`) at `8bbcb4e`
verified-at: 2026-10-19
recheck: `sha256sum corpus/live/runs/round-35/inspection.json; python3 -c "import json; print(json.load(open('corpus/live/runs/round-35/producer-receipt.json'))['output_sha256'])"` → `74a45d0c…` versus receipt-reported `8c8d96db…` (raw output not retained, so the second value is receipt-reported and unreproduced); re-check SWGDE current revision at https://www.swgde.org/documents
coverage-map: C13

# Digest scope versus provenance — C13

Falsifiable claims.

1. A digest equality claim holds only over the exact byte sequence hashed.
   FIPS 180-4 §3 defines the digest as the output on a supplied message and
   states: "Any change to a message will, with a very high probability,
   result in a different message digest." Lane demonstration (r35,
   `LOG.md:458`): the saved r35 JSON was reformatted, so its byte SHA-256
   differs from the receipt's raw-output SHA-256. Command (L1 re-run
   2026-10-19): the `recheck:` line above → saved file
   `74a45d0c7e25027090a0dfbad27f132dea14cf6b1b8cb447317f8174a7d02e4a`,
   receipt `output_sha256`
   `8c8d96db863e0f32b816d526fca3d1df04fb60e0ece5f166781dfc6ccd8988e2`. The raw
   CLI output was not retained (`corpus/live/runs/round-35/LEDGER.md`), so the
   receipt value is receipt-reported, not re-derived. The digest binds the
   serialization, not the logical content. Lesson M11
   (`corpus/lessons/round-1.md:48`): "a digest binds only the bytes hashed."
2. Acquisition verification is scoped to the data actually acquired, which
   may be less than the source. SWGDE 17-F-002-2.1 §8: "The process of
   verification might not verify all data as read from the subject media",
   naming damaged sectors, Host Protected Areas and Device Configuration
   Overlays as causes. A matching acquisition hash therefore does not by
   itself prove whole-source completeness.
3. [INFERENCE, case-scoped] In this lane's replays, a receipt hash or
   Evidence ID shows internal consistency only where it is recomputed against
   named bytes or fields (for example the receipt `stdout_sha256` against the
   saved raw output in `corpus/verify_named_multi_icon_states.py`); it does
   not establish producer origin, acquisition completeness, custody, or that a
   producer ever ran. The round-1 gate rejected equating them
   (`corpus/lessons/round-1.md:16`: "these checks establish internal
   consistency only; no producer was called"; lesson M13).
4. Because a digest alone carries no scope, acquisition documentation must
   record what the digest covers. 17-F-002-2.1 §9 lists "Acquisition
   details (e.g., type of acquisition, imaging tool and version number)",
   "Hash value(s) of the acquired data", and "Errors encountered during
   acquisition" among the fields; the lane's receipts analogously pin
   `command`, `fixture_sha256`, `evidence_id` and `stdout_sha256` per record
   (checked fields enumerated in
   `.ufo/waves/kaika-r1/reviewer-oracle.md:56-58`).

## Observation

- FIPS 180-4 is a cryptographic specification: it defines the SHA-1/SHA-2
  family digests and their change-detection property; §6 scopes the standard
  to "Federal departments and agencies" while noting it "may be adopted and
  used by non-Federal Government organizations." It says nothing about
  evidence provenance, custody, or completeness.
- 17-F-002-2.1 §9: "Examiners should compute cryptographic hash values over
  the acquired data using a NIST-approved hash algorithm to facilitate
  subsequent validation of the acquired data's integrity" — hash computation
  is one documented step beside log review and failure resolution, not a
  provenance mechanism.
- Lane ledger practice already enforces the boundary: the r35 provenance
  caveat (`LOG.md:458`) is recorded on the record itself, and the round-1
  gate rejected equating receipt hashes or Evidence IDs with producer origin
  (`corpus/lessons/round-1.md:16`) — a gate decision, separate from the six
  forged-field rejections the replay battery exercises (`:14`).

## Inference

- [INFERENCE] The reformatted-JSON divergence implies a storage rule for
  this lane: saved records must be byte-preserved, or any later digest check
  against the receipt's raw-output hash will fail even when content is
  logically identical — the two hashes describe different byte sequences,
  and neither is "the" digest of the finding.
- [INFERENCE] Reading §8 and §9 together, a complete fixity statement for a
  lane record should name: algorithm, the exact bytes covered (file or
  stream), and any known exclusions — mirroring acquisition documentation
  fields — rather than reporting a bare hash match.

## Unknown

- Whether the lane's historical saved records were ever captured with a
  stated byte scope beyond raw stdout; earlier rounds recorded `stdout_sha256`
  but the coverage of receipt-side fields is not comprehensively checked
  (`corpus/lessons/round-1.md:10` notes `parameters.path` and `locations`
  are not comprehensively checked by the named verifier).
- Whether any lane receipt hash has ever been independently re-derived by a
  non-author byte read; the replay verifier re-hashes current bytes but the
  producer was never observed running.

## Limitations

- SWGDE §8 addresses media acquisition, a different context than this lane's
  saved-record ledgers; the entry borrows the scope principle only and does
  not claim acquisition equivalence.
- FIPS 180-4's applicability clause concerns Federal systems; its use here
  is definitional (what a digest computes), not normative.
- The entry does not address chain-of-custody transfer records; custody is
  a separate proposed surface (`corpus/README.md` `## Frontier`).

## QUALITY check

| id | verdict | basis |
|---|---|---|
| Q01 | pass | Claim 1 rests on FIPS 180-4 §3 (spec, tier A for digest behavior); claim 2 on 17-F-002-2.1 §8 (guidance, tier A for what §8 states); both opened in full this round. |
| Q02 | pass | `source:` with URL + section + revision anchors (S005, S006) and own-work rows S014, S015; `verified-at: 2026-10-19`; `recheck:` is the r35-specific re-hash plus receipt read, and a SWGDE revision citation; `coverage-map: C13`. |
| Q03 | pass | The saved-file digest is recomputed from bytes by the `recheck:` command; the receipt digest is read and labeled receipt-reported, never used as the expected value for the file. |
| Q04 | n/a | No tool-output claim is made; FIPS/SWGDE texts and lane records are the subjects. |
| Q05 | n/a | No readiness or capability claim; no producer call asserted. |
| Q06 | n/a | No fixture bytes are stated or edited; cited records are referenced, not re-measured here. |
| Q07 | pass | No predicted parser behavior; the r35 divergence is an observed record fact (`LOG.md:458`). |
| Q08 | pass | Both r35 digests carry the `recheck:` command and its full output; the Evidence-field list cites `reviewer-oracle.md:56-58`. |
| Q09 | pass | This entry is the digest-scope claim itself: hash equality asserted only for exact hashed bytes; origin/completeness/custody explicitly excluded (claims 1-3). |
| Q10 | pass | Scope is bounded to saved-record fixity in this lane plus acquisition-verification scope as §8 states it; no universal provenance claim is made. |

## Provenance (Q11, appended 2026-10-19)

Appended after orchestrator review; nothing above is rewritten. Each stated
value is derived by the command below, run from the lane root at `35b2e8b`
(lane HEAD `19b3174` for the corpus), with its observed output.

- r35 saved-file digest vs receipt-reported digest (exit 0):

  ```sh
  sha256sum corpus/live/runs/round-35/inspection.json; python3 -c "import json; print(json.load(open('corpus/live/runs/round-35/producer-receipt.json'))['output_sha256'])"
  ```

  ```text
  74a45d0c7e25027090a0dfbad27f132dea14cf6b1b8cb447317f8174a7d02e4a  corpus/live/runs/round-35/inspection.json
  8c8d96db863e0f32b816d526fca3d1df04fb60e0ece5f166781dfc6ccd8988e2
  ```

- r35 raw output not retained (exit 0):

  ```sh
  ls corpus/live/runs/round-35/
  ```

  ```text
  attempt-invalid.json
  inspection.json
  LEDGER.md
  producer-receipt.json
  reviewer.md
  reviewer-verify.py
  ```

- receipt fields checked by the replay (claim 4) (exit 0):

  ```sh
  grep -c "receipt\['command'\]" corpus/verify_icon_languages.py corpus/verify_multi_icon_states.py corpus/verify_named_multi_icon_states.py; sed -n 56,58p .ufo/waves/kaika-r1/reviewer-oracle.md | cut -c1-120
  ```

  ```text
  corpus/verify_icon_languages.py:1
  corpus/verify_multi_icon_states.py:1
  corpus/verify_named_multi_icon_states.py:1
  - icon: file identity L124, evidence L125, subject L126, artifact L127, every decoded field L129, coverage L131, candida
  - icon cross-row: exact one-byte delta L149, intact icons L150, three distinct selections L151.
  - multi: fixture digest L127, Evidence identity L128, subject digest L129, artifact L130, every decoded key L132, covera
  ```

- FIPS 180-4 quotes (S006) (exit 0):

  ```sh
  curl -sL 'https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf' | pdftotext -layout - - | tr -s ' \n' ' ' | grep -oE 'Any change to a message will, with a very high probability, result in a different message digest|may be adopted and used by non-Federal Government organizations' | sort -u
  ```

  ```text
  Any change to a message will, with a very high probability, result in a different message digest
  may be adopted and used by non-Federal Government organizations
  ```

- SWGDE 17-F-002-2.1 quotes (S005) (exit 0):

  ```sh
  curl -sL 'https://swgde.org/wp-content/uploads/2025/09/2025-08-05-Best-Practices-for-Computer-Forensic-Acquisitions-17-F-002-2.1.pdf' | pdftotext -layout - - | tr -s ' \n' ' ' | grep -oE 'might not verify all data as read from the subject media|Hash value\(s\) of the acquired data|Errors encountered during acquisition|NIST-approved hash algorithm' | sort -u
  ```

  ```text
  Errors encountered during acquisition
  Hash value(s) of the acquired data
  might not verify all data as read from the subject media
  NIST-approved hash algorithm
  ```
