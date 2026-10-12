# Round 4 saved-evidence verification — 2026-10-12

- Non-author review input: `review-r1-r3.md` (reviewer `revenger-r1-r3-independent-reviewer`). It found the round-2 and round-3 command gaps while accepting the bounded underlying results.
- Command: `python3 .shokunin/revenger/corpus/verify_saved_evidence.py --self-test` (from repository root); exit 0.

```text
POSITIVE ev_cc681c2a03da4e9901275c1425fb1f726cca78bbdbec3defb13b6a0ac8ad156b ZIP root + 2 members: 3/3 identity units; formats, sizes, hashes, edges and fixture bytes match
POSITIVE ev_4a93276c886da96f0b37c490e395dc0761ac32225dd7297c600a51ce100c1c7e JS 2 imports + package main: 3/3 static inferred relationships match source/export and artifact digests
NEGATIVE ZIP REJECTED: ZIP: wrong root size/format
NEGATIVE JS REJECTED: JS: wrong package-main mapping
```

- Negative controls alter deep-copied saved evidence in memory only: ZIP root node size +1; JS package-entrypoint resolved path changed to `wrong.js`. Neither producer, fixture, nor committed Evidence file is mutated.
- OBSERVATION: cited REA JSON records are checked against local fixture bytes/source. INFERENCE: matches support only bounded ZIP identities and static JS relationships. UNKNOWN: actual execution, unobserved dynamic relationships, trailing ZIP bytes, and native function analysis remain untested. This verifier is not a cryptographic attestation of REA's producer or an independent REA run.
- Denominator: two previously under-tested route checks; both positive and both reject their targeted alterations. The old r2/r3 commands remain historical receipts and must be read with the review's caveat; this new command is the corrected proof for the stated bounded units.
