RESULT: COMPLETE

Frozen revision a3498e25ad87bf756288812d0ea7c474b09433c7 (`git -C … rev-parse HEAD`). Extracted read-only with `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive a3498e25ad87bf756288812d0ea7c474b09433c7 | tar -x -C /fast/scratch/hyaku/revenger-r62/R62MapBaseline` (`EXTRACT_OK`); reads below are from that archive unless a historical revision is explicitly named (`cf02419`).

## Observations

Parser `/fast/scratch/hyaku/revenger-r62/R62MapBaseline/parse_map.py` (stdlib only, stdout only), run as `python3 -B …/parse_map.py /fast/scratch/hyaku/revenger-r62/R62MapBaseline`:

```text
rows=14 held=4 held_rows=['C01', 'C11', 'C12', 'C13']
statuses=C01=held,C02=partial,C03=frontier,C04=uncovered,C05=frontier,C06=partial,
C07=frontier,C08=frontier,C09=uncovered,C10=partial,C11=held,C12=held,C13=held,C14=partial
rejected_files_in_knowledge_dir:
  commonjs-destructured-require-edges.md, evm-saved-interface-candidates.md
rejected_in_entries_column=[]
non_target_invariant_drift={}
denominator_ok=True held_ok=True target_ok=True invariant_ok=True
```

`statuses=` is wrapped here for display; `map-parse.out` holds the literal one-line output.

README's own formula, from the archive root: `grep -cE '^\| C[0-9]+ ' corpus/README.md` -> `14`; `grep -E '^\| C[0-9]+ ' corpus/README.md | grep -cE '\| held \|$'` -> `4`.

Targets, quoted by `path:line`:
- `corpus/README.md:33` C04: knowledge cell `— (round-61 candidate rejected; see lessons/round-61.md)`; status `uncovered`.
- `corpus/README.md:38` C09: the same bare `—` note; status `uncovered`.
- Rule at `corpus/README.md:21-24`: a retained rejected candidate "is clearly marked in the file and is not coverage."

Rejected candidates checked in place: `corpus/knowledge/commonjs-destructured-require-edges.md:5` and `corpus/knowledge/evm-saved-interface-candidates.md:5` both carry `admission-status: rejected — round-61 fresh falsify wave on ab58069; see lessons/round-61.md`. Directory census: `ls corpus/knowledge/*.md | wc -l` -> `8`; `grep -l '^admission-status: rejected' corpus/knowledge/*.md | wc -l` -> `2`, so 6 carry no rejection header. The two rejected files appear only in C04/C09 **work-evidence** cells, never a knowledge-entries cell (`rejected_in_entries_column=[]`).

No prior rejected candidate counts; held rows back only to admitted files:
- `held_backed`: C01→`pe-resource-directory-layout.md`; C11→`utf16-unpaired-surrogates-in-resource-names.md`; C12→`seed.md`+`tool-validation-by-function-and-version.md`; C13→`digest-scope-versus-provenance.md`+`seed.md`.
- Prior baseline `cf02419` extracted with `git show cf02419:corpus/README.md` into scratch; `python3 -B …/status_diff.py …/cf02419-README.md …/corpus/README.md` printed `A_rows=14 A_held=4 B_rows=14 B_held=4` and `status_diff=EMPTY`. Corroborated by `SCORECARD.md:243` ("README C04/C09 return to `uncovered`") and `:247` (provisional 6/14 withdrawn).
- README count notes agree: `corpus/README.md:45` (`Rows 14 — grep -cE …`) and `:48` (`held 4/14`).

Expected non-target status invariant (12 rows; all observed equal now): C01 held, C02 partial, C03 frontier, C05 frontier, C06 partial, C07 frontier, C08 frontier, C10 partial, C11 held, C12 held, C13 held, C14 partial. Also saved at `/fast/scratch/hyaku/revenger-r62/R62MapBaseline/expected-non-target-statuses.txt`. Denominator must stay 14 and held exactly C01/C11/C12/C13 until an admission is separately adjudicated.

## After-build recheck for L1 (no new gate claimed)

Run `python3 -B /fast/scratch/hyaku/revenger-r62/R62MapBaseline/parse_map.py <NEW_TREE>`. Pre-admission expected: `rows=14`, `held=4 held_rows=['C01','C11','C12','C13']`, `non_target_invariant_drift={}`, `denominator_ok=True held_ok=True target_ok=True invariant_ok=True`. Post-admission, only a target row may flip; `non_target_invariant_drift={}` and `denominator_ok=True` must still hold, and `target_ok=False` is expected output of a deliberate admitted flip, not permission to admit. C04/C09 stay `uncovered` through drafting/attacking (`reports/round-62/claims.md:45-46`); a 4/14 final falsifies C1 (`claims.md:13`).

## Limits / unknowns

- Records map statuses and path existence; does not re-gate entries. Pre-contract `seed.md` and the readiness checklist remain unregated per README "Known gaps"; `partial` rows are not promoted.
- Ellipsis/wildcard references were checked as endpoints/patterns only; `evm-r20` is absent, matching the map's explicit "(no `evm-r20`)".
- No `measure.py`, producer, fixture JavaScript or EVM byte execution. No corpus byte was modified.
- Unresolved: none within this assigned map-baseline question.

## Proposed changes

None to production. Reusable scratch artifacts: `parse_map.py`, `status_diff.py`, `map-parse.out`, `expected-non-target-statuses.txt` under `/fast/scratch/hyaku/revenger-r62/R62MapBaseline/`.

Installs: none.
