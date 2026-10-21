# ScribeLessonDraft — round-61 lesson skeleton (DRAFT, report only)

Seat `CloseChousa26.ScribeLessonDraft-10`. Base HEAD `e0a4b0c` (claims base `cf02419`, claims.md:6). Nothing written to `corpus/lessons/round-61.md`.

## Draft skeleton — `corpus/lessons/round-61.md`

```
# Round 61 lesson — C04/C09 knowledge admissions; receipt-command control

Round: revenger hyaku round 61, attempt 1. Pre-registration: `reports/round-61/claims.md`. Bar: `corpus/QUALITY.md` Q01–Q11, frozen at e0a4b0c.

## Spot-check intake (from `corpus/lessons/round-1-verifier-spotcheck.md`)

Prior outside check (:12-13): C11 admit agree; long-term-fixity reject agree; RFC 3227 record disputed. Debts routed (:17):

| debt | routed to | status at base |
|---|---|---|
| receipt-command mutation survivor | C2 (two verifier scripts) | open: C2_RECEIPT_B_KILLED 0/2 |
| SKILL.md absent | none this round (`corpus/README.md:47`) | open |
| F03 verdict vs scout STALE | TBD — no F03 record located | open / unknown |
| kaidoku/revenger overlap (ADJ-06) | L0, out of scope | open |

## Mistakes

| id | class | evidence | captured-by | fix |
|---|---|---|---|---|
| M21 | TBD | TBD (path:line or command + output) | TBD (Q id, or `none` + reason) | TBD |

Ids continue from M20. Count: `awk -F'|' '/^\| M[0-9]+ /{n++; if ($5 ~ /none/) z++} END{print n, n-z, z}' corpus/lessons/round-61.md`.

## Gate

### Sources opened this round (contract rule 1)

Access date 2026-10-21 for every row. Quotes ≤25 words, verbatim, located.

- S016 TBD — URL TBD — section TBD, revision/version/date TBD — "TBD"

Base registry ends at S015 (`corpus/SOURCES.md:29`). Unopened leads: Node.js modules documentation (CommonJS `require`, package `main`) — URL TBD; EVM opcode reference (PUSH4, JUMPDEST) — URL TBD.

### Admission decisions

| candidate | map row (status at base) | decision | criteria |
|---|---|---|---|
| `knowledge/TBD-js-commonjs-require-edges.md` (C04: destructured `require` named-import edges; package `main`, static inference) | C04 (uncovered) | TBD | TBD (Q01 S016+; Q02; Q03/Q06 `fixtures/js-r3`, `js-r7-v2`; Q11) |
| `knowledge/TBD-evm-push4-selector-candidates.md` (C09: PUSH4 selector candidates, JUMPDEST destinations, inferred, no execution) | C09 (uncovered) | TBD | TBD (Q01; Q03/Q06 `fixtures/evm-r19`, `evm-r21`; Q11) |

Rejected candidates recorded with failing Q id; not counted. Saved falsifiers: `verify_js_graph_delta.py` "saved graph disagrees with source truth"; `verify_saved_evidence.py` "JS: wrong package-main mapping"; `verify_evm_evidence.py` "candidate destination mismatch".

### Outside spot-check

TBD — non-author verifier; ≥1 admit and ≥1 reject sampled; ≥3 `SOURCES.md` rows re-opened; verdict per sample. Until filled: not performed.

### Row status changes (old → new)

| row | old | new | condition |
|---|---|---|---|
| C04 | uncovered | TBD | held only if admitted |
| C09 | uncovered | TBD | held only if admitted |

K_HELD 4/14 → TBD (6/14 both; 5/14 one; 4/14 none = C1 falsified, claims.md:39). C2 is calibration: C2_RECEIPT_B_KILLED 0/2 → TBD. SOURCES census: `revenger ok` at base (rc 0); after: TBD.
```

## Findings

1. Base observed: `K_HELD=4/14 score=2.9`, C04/C09 `uncovered` (`reports/round-61/measure-before.log:2-4`); `C2_RECEIPT_B_KILLED=0/2` (:12); census `revenger ok`, exit 0. No C04/C09 source row exists, so Q01 cannot pass until an S016+ row is opened. Base ambiguity: claims.md names `cf02419`, HEAD is `e0a4b0c`.
2. Guard for C09: `verify_evm_evidence.py:74` raises "selector opcode offset mistaken for destination"; the entry must not present a PUSH4 operand offset as a JUMPDEST destination.

VERDICT: skeleton drafted in this report only; quotes, URLs, decisions, outside spot-check and K_HELD outcome are TBD pending gate execution. Installs: none. Web: none opened.
