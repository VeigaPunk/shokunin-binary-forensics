# r67 post-adjudication drafts (scratch — copied into place only after wave adjudication)

## LOG.md entries (append, two entries)

### Entry 1 — "Round 67 declaration and build"

- Pre-registration landed `d11f81dfb77ddf67365acfff1e0256207d65bc27` on base `fa0eb3eb` (r66 tip + operator considerthese sweep `d4657ee` + non-author r66 spot-check `fa0eb3eb`): claims.md (C1 coverage — the round-66 routed C05 re-gate, one new v2 candidate carrying exactly the routed text-level repairs, README flipped only on a fresh-seat Q01–Q13 all-pass; C2 calibration — new criterion C7, the embedded-output verbatim gate, the M39 fix shape; frozen counter `reports/round-67/measure.py` sha256 `7933c060…bc07e`), red-before receipt `measure-before.log` (K 8/14, C05 uncovered, C7 labels 0/no, HOLDS_OK_V5=no, probe exit 0).
- Build landed `7668510ffc49733daf023e40ff3300ef387ebde5`: v2 candidate `corpus/knowledge/round-67-apk-axml-byte-evidence.md` (admission-status: candidate; every embedded output captured from actual command stdout at build; M39 hex pair repaired with the 16-byte `4d616e69666573742d…` prefix; S038 enum anchor lines 237-253 incl. :253; S043 route anchor lines 7-8; S045 dex-spec row opened 2026-10-24 — the r66 routed "dex-header spec row"; item-8 attrExt-relative provenance; Q08 Q-map row; no dangling pointers); `corpus/check_embedded_outputs.py` (C7 gate, outside the verify_* replay family; --self-test exit 0; --entry over the retained r65 candidate exit 1 naming entry:41) + `SKILL.md` `## Gate registry` row; `corpus/SOURCES.md` S045 + search-log note; census exit 0 (45 rows).
- Assimilation item 10, wave-4 quarantine-first: slice re-derived = 26 rows; zero adoptions; id-collision evidence committed (reg 44 / staged 146 / collisions 0; S045 id taken → package renumber-by-document obligation recorded).

### Entry 2 — "Round 67 adjudication and measurement" (values finalized at adjudication)

- Wave: ONE v2 wave, 64 seats, policy v2, dispatched in-seat as ONE batched OMP task call (dispatch evidence `.ufo/waves/round-67/dispatch-envelope.json` counts 64/1 + `dispatch-run.log`; slot grant `granted lane=revenger wave=r67-wave seats=64 live=28 cap=256` at dispatch-start). Roles: scribe 19, reviewer 13, scout 11, critic 10, executor 5, mutation-tester 2, connector/sentinel/simplifier/revenger 1 each — attack roles 25/64 = 39%. Dead seats: (fill). Reports: (fill) 64.
- C1 verdict: (fill — pass branch: flip + K 9/14; fail branch: honest stop).
- C2 verdict: (fill).
- Final measurement: (fill) — committed `reports/round-67/measure-after.log`.
- Trends + census after: (fill).

## SCORECARD round-67 section skeleton (append)

## Round 67 (hyaku) — quarantine-first: C05 re-gate + C7 verbatim gate

Pre-registration `d11f81df` (claims.md + counter `7933c060…` + red-before on base `fa0eb3eb`);
build `7668510f`; ONE dispatched v2 wave of 64 seats (attack 25/64); final measured tip (fill).

| axis / criterion | before → after | counting command | measured commits | verdict |
|---|---|---|---|---|
| coverage — C05 re-gate (K) | 8/14 → (fill) | `python3 -B reports/round-67/measure.py TREE` (K_HELD_BACKED, K_ROW C05) | `fa0eb3eb` → (fill) | (fill) |
| calibration — C7 embedded-output verbatim gate | 0 → (fill) | same probe (C7_*) | same | (fill) |
| calibration C2–C6 holds | 2/2·2/2·2/2·2/2·4/4 → (fill) | same probe | same | hold |
| calibration — selected runnability C | 4/4, replay 10/10 → (fill) | same probe (HOLD_*) | same | hold |
| coverage — F | 5/8 → (fill) | same probe | same | unchanged |
| freshness | 18/18 → (fill) | same probe | same | hold |
| diagnostics | C05_SINGLE_V2, C7_V2_CLEAN, MISMATCH 0 | same probe | same | registered |
| depth / operability / adjacency | no claim | — | — | unchanged (connector scan reported-not-absorbed) |

Capabilities: (none added / gate registered as probe — a registered gate is not a new capability
row unless demonstrated as one; recorded as probe registration under SKILL.md registry).
Sources: 44 → 45 (+S045 mined); census exit 0 both ends. Mistakes: M42 (provider), M43 (landing).
Quarantine: 26/26 verdicts, adoption closed (wave-4).

## README C05 flip (PASS branch only, applied with the Gate decision in one commit)

Line 34 →
| C05 | Android packages (APK) | `knowledge/round-67-apk-axml-byte-evidence.md` (manual byte-derived readout of `fixtures/apk-r65` only; no provider, signing, dex-validity or general-AXML claim) | `fixtures/apk-r65`; retained rejected candidate `knowledge/round-65-apk-axml-byte-evidence.md` (r65 falsified, adjudicated r66) | held |

Frontier C05 paragraph → Round-67 update: the re-gated v2 candidate (text-level repairs of the
falsified r65 draft) was admitted by the dispatched round-67 wave's named fresh seats; the row is
`held` on that entry alone.
