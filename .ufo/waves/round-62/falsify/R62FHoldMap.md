GRADE: HOLDS — frozen round-62 candidate state, corpus coverage hold map (C1 pre-admission)

Frozen revision `d97761952be256d145d298022de03091de91d358` (full, `git rev-parse …^{commit}`
type commit); base `5bd4a90fc1a34caa94496601b60537b3aab12301`; pre-registration
`a3498e25ad87bf756288812d0ea7c474b09433c7`.
Candidate hashes (frozen): `round-62-commonjs-require-name-evidence.md`
`42096e9676d33e25c3b6092e60fbd0fdacd699435ed9dc9db59ce24a1ceaaba3`;
`round-62-evm-dispatch-byte-evidence.md`
`6a1d394ad92fcaa5344069d1225e428988f1397e80c8968745d7b48bf43fed6e`; both header
`admission-status: candidate`, neither named in README.
Workspace: `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive --format=tar <rev> |
tar -x -C /fast/scratch/hyaku/revenger-r62/R62FHoldMap/{base,frozen}`;
`TMPDIR=/fast/scratch/hyaku/revenger-r62/R62FHoldMap/tmp`. No repo mutation.

## Observation (command → exact output)
1. README identity. `sha256sum base/corpus/README.md frozen/corpus/README.md` → both
   `2c8606d3de51014c83f5be1e2b1309a8f42c343a5c2b006cc73ed0ee96e8e23f`; `diff` exit 0.
   `corpus/README.md:45` states rows 14.
2. Row/status parse by own parser (`holdmap.py`, no measure.py): `python3 -B holdmap.py <tree>`
   → `ROW_COUNT 14`, `DENOMINATOR_14 True`, `K_HELD 4 / 14`; held rows C01,C11,C12,C13 all
   `backed`; non-held C02 partial, C03 frontier, C04 uncovered, C05 frontier, C06 partial,
   C07 frontier, C08 frontier, C09 uncovered, C10 partial, C14 partial;
   `K_HELD_BACKED 4 / 14`. Base and frozen stdout byte-identical (`diff` → SAME_OUTPUT).
   Held knowledge paths exist under `frozen/corpus/` with no `admission-status` header:
   `knowledge/pe-resource-directory-layout.md`,
   `knowledge/utf16-unpaired-surrogates-in-resource-names.md`,
   `knowledge/tool-validation-by-function-and-version.md`,
   `knowledge/digest-scope-versus-provenance.md`; `knowledge/seed.md` anchors
   `## Verification discipline` :21 and `## Calibration strategy` :30 exist.
3. Exact README counts. `grep -cE '^\| C[0-9]+ ' corpus/README.md` → `14`;
   `grep -cE '^\| C[0-9]+ .*\| held \|$' corpus/README.md` → `4`.
   Status vector from `corpus/README.md:30-43`: C01=held C02=partial C03=frontier C04=uncovered
   C05=frontier C06=partial C07=frontier C08=frontier C09=uncovered C10=partial C11=held
   C12=held C13=held C14=partial. `corpus/README.md:33` C04 cell `— (round-61 candidate
   rejected; see lessons/round-61.md)`, `:38` C09 same shape.
4. No provisional credit. `grep -n 'round-62' corpus/README.md` → NONE.
   C04 candidate `:5` "the map row stays `uncovered` until a fresh falsify wave";
   C09 candidate `:15` "candidate — round-62 build wave, not admitted … nothing here flips a
   coverage row". Negative control: full frozen corpus copy with the C04 knowledge cell
   patched to name the C04 candidate → `K_HELD_BACKED 4 / 14` still, row reports
   `admission=candidate (not admitted)`; the candidate cannot add a backed row even if cited.
5. Held-row work evidence resolves: `corpus/verify_icon_states.py`, `verify_icon_languages.py`,
   `verify_multi_icon_states.py`, `verify_named_multi_icon_states.py`, `verify_pe_resources.py`;
   fixture dirs `pe-r27,r34,r51–r57,r59,r59d`; `corpus/lessons/round-1.md`; `reports/round-1/`
   all present.
6. Frozen vs base outside README: `diff -r base/corpus frozen/corpus --brief` → only
   `SOURCES.md` differs, plus new `knowledge/round-62-*.md` (2) and `lessons/round-62.md`.
   `fixtures/`, `live/`, `verify_*.py` byte-preserved (10 scripts each side; no diffs).
   `reports/round-1`, `reports/round-61` unchanged, only `reports/round-62` added.
   `corpus/QUALITY.md` identical `811ebf73179a86e0adff18874d0abf2d22e5161ac73c6a04ab3cf21fb51c45d1`,
   13 rows Q01–Q13, `grep -n 'Q14'` → none. `SCORECARD.md`, `SHONEN.md`, `PROVINCE.md` identical;
   `LOG.md` differs only by appended round-62 sections whose text keeps README uncovered
   (`LOG.md:822`, `:828`).

## Inference
- K_HELD_BACKED=4/14 with C04/C09 uncovered is the intended pre-admission state
  (`reports/round-62/claims.md`: "Land the candidate state WITHOUT held flips"), not a C1
  contradiction; ≥5/14 waits on independent Q01–Q13 admission by other seats.
- Hold-map integrity intact: denominator 14, no held loss, no non-target status change,
  rejected round-61 candidates byte-preserved and still marked rejected, candidates get no count.

## Unknown / not done
- `reports/round-61/measure.py` was not run (assignment: compute K independently); its
  internals/TMPDIR of the recorded before run are not evidence here.
- Q11 derivations inside the two candidate entries were not audited (separate fresh seats);
  this report decides only the coverage/hold state.
- No fixture-JS/EVM/provider/chain execution; S028–S031 source rows are other lanes' scope.

VERDICT: HOLDS — 14 rows; 4/14 held (C01,C11,C12,C13) each backed by an existing admitted
entry; C04/C09 uncovered; all non-target statuses unchanged; original held paths resolve;
candidate files carry zero provisional credit; independent K_HELD_BACKED = 4/14.
Installs: none (no package/tool changes; python3, git, sha256sum pre-existing).
