# Round 13 — saved static shape proof

Command: `python3 .shokunin/revenger/corpus/verify_shape_evidence.py --self-test`

```
POSITIVE ev_bb7e1c308a60b0cc45919a4a441347a0b6119df2c49f0de40c737615f94cb872 saved REA static shape evidence: 2/2 presence deltas; 2/2 stable names; no runtime claim
NEGATIVE REJECTED changed-property evidence mismatch
```

Exit 0, 2026-10-12. Parents: `ev_2a492f5d829a57115e954269e08d4c7d8465f3129dd2f82ded2d01b2fb4e3064` (v1) and `ev_913f14fa3ee334269cef30ff0af6835d6622a3053f08a5a4583260d7f35416d7` (v2). The verifier checks saved parent artifact SHA-256 against local source, exact export selection including selected-node equality with the checked parent return-shape node, complete selected static shape and comparison, property presence and an in-memory false-right-presence control. Re-running it neither calls REA nor executes fixture JS. The first reviewer identified the selected-node binding gap; the parent patched and reran the command after that review.

OBSERVATION: saved REA comparison reports the two property-presence changes and inventories; REA Evidence IDs above. INFERENCE: these source-backed syntax facts describe a statically inferred return shape. UNKNOWN: invocation, actual values and runtime mutations; native provider remains unavailable as last observed in round 1. The negative control checks proof consistency, not producer authenticity.
