RESULT: COMPLETE

Scope: frozen `a3498e25ad87bf756288812d0ea7c474b09433c7` only, extracted with `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive <rev> | tar -x -C /fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62FixturePremises`. Integrity: 128 extracted paths hashed with `git hash-object` against `git ls-tree -r <rev>`: 0 mismatches. The named round-62 candidate files are absent at that revision (`git ls-tree corpus/knowledge`), so this is input inventory only: no admission, no README change, no gate, no promotion.

Scratch deliverables (copy/rerun before landing; removed on cleanup; run from extracted root):
- `premises_probe.py` + `premises_probe.out` (239 lines): carriers, truth cross-checks, instruction walk, saved-record projection, JS source spans.
- `anti_vacuity.py` + `anti_vacuity.out`: N1-N20 negative examples.
- `fixture-input-inventory.md`: per-field classification and consequences.
Command: `python3 -B premises_probe.py`.

EVM inventory (values printed in `premises_probe.out`; line refs):
- Carriers: r19 hex 39 B sha `294e...` / decoded 18 B sha `d108...`; r21 raw 18 B = decoded; r22 34 B `94c1...`; r23 7 B `8047...`; r24 35 B `b698...`; r25 19 B `2d87...`; r26 19 B `ebe2...` (3-37).
- Walk: r19/r21 PUSH4@6 `deadbeef`, JUMPI@14 -> 16 (JUMPDEST); r22 PUSH4@7/17, JUMPI@15/25 -> 30/32 (both JUMPDEST); r23 PUSH4@0, POP, STOP, no JUMPI/JUMPDEST; r24 PUSH32@0 (32-byte immediate), POP@33, STOP@34, executable PUSH4 = 0; r25 STOP@0 then PUSH4@7, JUMPI@15 -> 16 (STOP), JUMPDEST@17; r26 same with byte@14 `10`->`11`, target 17 valid (39-56).
- Saved `inspect_evm_interface` (`evmole@0.9.3`, `inferred`, completeness `unknown`, runtime `not-performed`): r19/r21 `0xdeadbeef`@16; r22 `0xaaaaaaaa`@30, `0xbbbbbbbb`@32; r23-r26 empty. For the three records with functions, every reported offset is in the JUMPDEST set and not at a PUSH4 site; selectors equal PUSH4 immediates (126-174).
- r24 pattern derived from r19 bytes 6..14 = `63deadbeef14601057` (9 B); r24 start 1, inclusive span [1,9]; `code[1:9] != pattern`, `code[1:10] == pattern`; r24-local count 1, whole-tree count 4 (r19@6, r21@6, r24@1, r25@7) (117).

JS inventory (saved graph is the record under test; fixture source is ground):
- v1 js-r3: index 274 B `f7d8...`, transform 379 B `cd9f...`, package 85 B `92ef...`; line1 `const { rot13, checksum } = require('./transform');`; source order rot13@8, checksum@15; call [28,50); destructuring [6,50); index.js 1 `require(` call, 0 in the other two files.
- v2 js-r7-v2: index 209 B `b53d...`, same transform/package; line1 `const { rot13 } = require('./transform');`; rot13@8; call [18,40); destructuring [6,40); same 1/0/0 call counts. Columns are 0-based, end-exclusive; fixtures are ASCII so byte offset equals column; exact slices match (180-189).
- Saved imports: v1 3 edges (named rot13 [6,50), unnamed require [28,50), named checksum [6,50)); v2 2 (unnamed [18,40), named rot13 [6,40)); named sets match source; v1->v2 set delta removes `checksum`, keeps `rot13`; imports 3->2, edges 13->12 (200-201, 238).
- Named-edge location is the whole destructuring span and is identical for both v1 names; only the unnamed require edge carries the call span. Per-name spans are not in the record (200-201, 212).

Digest scopes:
- r19: `subject` = `artifact` = sha256(39-byte hex carrier `294e...`), NOT decoded bytes; `bytecode` = sha256(18 decoded `d108...`); the 36-byte hex body alone is a third digest `87167114...` (122-124).
- JS: `subject` = `root_artifact_sha256` = directory digest (v1 `8eec...`, v2 `696c...`), matching no file digest; edge/node `evidence.artifact.sha256` match per-file digests (193-194, 217).

Must come from bytes, not truth/record: every offset, count, span, size, digest, instruction start/immediate, PUSH4 site, JUMPDEST/JUMPI target, r24 occurrence, r25/r26 diff, JS call/destructuring span, name order, file digest, edge name set/location, set delta, edge/node artifact digest.
Truth/record intent only (label recorded): EVM selector constants (no truth `signature`/`keccak` key), notes, encoding labels, pedigree names, `instruction_stream` prose, `jump_target_valid`; JS evidence/graph/manifest ids, directory subject digest (method not re-derived), provider version strings, `subject.local_path`, relation label `imports`, node kind `electron-main`.

Anti-vacuity negatives (`anti_vacuity.out`): N1 exclusive [1,9] fails the slice; N2 "once" is false tree-wide (4); N3 raw `0x63` != executable PUSH4 (r24 1 vs 0); N4 r19 subject is carrier not decoded; N5 artifact 39 vs bytecode 18 B; N6 valid r26 target still reports `[]`.
N7 validity does not separate r25/r26 (both `[]`); N8 offset is JUMPDEST 30/32 not PUSH4 7/17; N9 no truth signature field; N10 JS subject matches no file digest; N11 named spans are destructuring [6,50), not call [28,50), and are name-identical; N12 sorted names reverse source order.
N13 a 3->2 count does not identify removal (set difference does: `checksum`); N14 v2 `transform.js` is byte-identical and still exports `checksum`; N15 `statistics.modules` 0 vs 4 module nodes; N16 `text_bytes_read` 738/673 is all-three-file bytes, not JS-only 653/588; N17 one `require(` call vs 3/2 `imports` edges; N18 `local_path` is outside the frozen tree; N19 raw `selector` `deadbeef` != normalized `0xdeadbeef`; name the scored layer; N20 `semantic_graph` has no `imports` and coverage `unknown` vs `graph` `complete`.

Consequences for entry writers (input side): C09 may compare the walk with saved selector/offset fields and state digest scopes explicitly, but must not present selectors as derived, quote a tree-wide occurrence count unscoped, equate raw `0x63` with executable PUSH4, or infer why r25/r26 are empty.
C04 may compare source name set/order and the require call span with that one unnamed edge, and the named set with source, but must use set difference for the delta, not per-name spans or count-only checks, and must not claim v2 removed an export. Every number in entry prose still needs its own in-entry command+output; this inventory is a cross-check, not a substitute.

Unknowns: directory subject-digest method and every evidence/graph/manifest id are recorded, not re-derived; provider versions are recorded, not re-probed (no runtime); r25/r26 empty-output cause unresolved (reachability vs stop); column unit beyond ASCII untested; truth notes are author prose, not ground.

Installs: none.
