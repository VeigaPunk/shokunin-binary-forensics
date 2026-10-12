# Round 16 — saved semantic trace verification

Command: `python3 .shokunin/revenger/corpus/verify_semantic_trace.py --self-test` (exit 0):

```
POSITIVE ev_53329396d6fe4843b89806ef1ed98b6db8358ec91c41c733d617ea846b995a8a 3/3 returned captures match source tokens and saved parent; partial static trace only
NEGATIVE REJECTED relation differs from source parent
```

The verifier matches the r14 request to saved r3 parent Evidence `ev_4a93276c886da96f0b37c490e395dc0761ac32225dd7297c600a51ce100c1c7e` and trace `ev_53329396d6fe4843b89806ef1ed98b6db8358ec91c41c733d617ea846b995a8a`, checks graph/seed/query/partial-coverage boundary, exact selected parent nodes and relations, source hash and three token ranges. An in-memory forged first-relation location is rejected. This is saved-record consistency, **not** independent REA producer authentication, exhaustive semantic coverage or JavaScript execution. OBSERVATION: saved trace reports resolved static captures; INFERENCE: lexical dependencies in the authored fixture; UNKNOWN: runtime invocation, actual values, omitted other semantic families.
