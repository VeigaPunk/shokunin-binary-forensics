recommend repair — draft the exact C05 row and K scorecard line only; keep C05 uncovered until wave-2 adjudication.

## Evidence

- Frozen C1 claims: `reports/round-71/claims.md:7-17` defines C05 sixth pass, requires K and strict K 9/14, C05 held with exactly `knowledge/round-71-apk-axml-byte-evidence.md`, and makes wave-2 Q01–Q16 decisions a separate necessary predicate. Landing order keeps the candidate and README uncovered before those votes; if any FAIL, leave the README uncovered and reject the entry.
- Current map row: `corpus/README.md:45` currently says C05 uncovered and explicitly labels the v6 candidate, gate/lint, and votes pending. Do not modify it during this pre-gate stage.
- Counter recipe: `reports/round-71/measure.py:25-32` counts README map rows and backed rows; `:72-80` derives K, strict K, status, and the path. Its output includes K score on `:77` as `10*len(br)/len(rr)` to one decimal. Contract baseline and falsifier: `reports/round-71/claims.md:9-11,17` sets 8/14 → 9/14; `reports/round-71/pre-registration.txt:7-8` says the D control reaches 9/14 with clean gate/lint but fails `C1_W2_Q_VOTES=0/16`.
- Scope precedent: `SCORECARD.md:631` reported round-70 K unchanged and C05 uncovered after falsification; `:644` identifies the sixth pass and same-revision K line as planned, not landed. Preserve all other rows/statuses and history.

## Draft only (not applied)

Exact final `corpus/README.md` C05 row, conditional on successful wave-2 adjudication and admitted v6 entry:

```markdown
| C05 | Android packages (APK) | `knowledge/round-71-apk-axml-byte-evidence.md` | `fixtures/apk-r65`; retained rejected candidates `knowledge/round-65-apk-axml-byte-evidence.md` (round-65 wave, falsified Q02/Q06/Q11), `knowledge/round-67-apk-axml-byte-evidence.md`, `knowledge/round-68-apk-axml-byte-evidence.md`, `knowledge/round-69-apk-axml-byte-evidence.md` and `knowledge/round-70-apk-axml-byte-evidence.md` (each `admission-status: rejected`; the round-70 v5.1 candidate failed three of sixteen wave-2 decisions, Q04/Q11b/Q13, `corpus/lessons/round-70.md` `## Gate`); round-71 v6 entry admitted only after all assigned Q01–Q16 votes PASS/n-a (`corpus/lessons/round-71.md` `## Gate`) | held |
```

Exact final `SCORECARD.md` K line, conditional on the same successful adjudication and measured final lane tip (row form matches nearby round-70 table):

```markdown
| coverage — knowledge-map ground K (C05 sixth pass) | 8/14 → 9/14 (5.7 → 6.4); C05 uncovered → held, backed by admitted v6 entry | `python3 -B reports/round-71/measure.py TREE` (`K_HELD_BACKED`, `K_HELD_BACKED_STRICT`, `C05_STATUS`, `C05_KNOWLEDGE_COLUMN`; separate frozen C1 wave-2 Q01–Q16 vote predicate) | base `b7abcd8` → final measured tip | **improved, C1 met** only if the frozen full predicate holds; otherwise preserve C05 uncovered and report falsified honestly |
```

The README draft replaces only the C05 row; retain all C01–C04 and C06–C14 lines and their statuses verbatim. The scorecard draft is one appended round-71 K row only; do not rewrite any prior row/status or claim calibration here. The phrase “only if” is material: gate/lint cleanliness or the 9/14 count alone does not admit C05.

## Falsifying 9/14

Run the frozen counter against the measured isolated corpus tree (the counter's documented `TREE` input):

```sh
python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-71/measure.py TREE
```

`K_HELD_BACKED=8/14` or `K_HELD_BACKED_STRICT=8/14` falsifies the 9/14 claim; so does any conjunct failure (`C05_STATUS` not held, wrong/non-single v6 path, entry not admitted, gate/lint failures, or `C1_W2_Q_VOTES` other than 16/16), with `HOLDS_C1_V6=no`. The pre-registration's concrete counterexample is control D: it prints 9/14 and clean gate/lint but `C1_W2_Q_VOTES=0/16`, hence `HOLDS_C1_V6=no` (`reports/round-71/pre-registration.txt:7-8`).
