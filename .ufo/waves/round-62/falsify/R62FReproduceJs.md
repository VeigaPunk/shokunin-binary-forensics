GRADE: PARTIAL — round-62 C04 candidate `corpus/knowledge/round-62-commonjs-require-name-evidence.md`: every reproduction axis (exit, stderr, full-stdout SHA-256, root-path independence, no external file dependency) holds byte-exactly; two non-fatal wording/count defects found (F1, F2 below).

Target (frozen). Entry file SHA-256 `42096e9676d33e25c3b6092e60fbd0fdacd699435ed9dc9db59ce24a1ceaaba3` — identical in the worktree and inside the candidate archive. Frozen candidate state `d97761952be256d145d298022de03091de91d358`; the entry's own derivation revision `a3498e25ad87bf756288812d0ea7c474b09433c7`; claim base `5bd4a90fc1a34caa94496601b60537b3aab12301`. Entry is `admission-status: candidate`; README C04 stays `uncovered`. I made no entry edit, no corpus/fixture/live byte change, no admission and no repair.

## Observation — reproduction

Extraction (own scratch only): `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive a3498e25ad87bf756288812d0ea7c474b09433c7 | tar -x -C treeA`; same for `d97761952be…` into `treeB`. `readout.py` was extracted programmatically from the entry's own fenced block (not retyped): 6973 B, SHA-256 `7996c744…` without trailing newline; **with** trailing newline `31dac2113f1b78967a635fbf65125ecedc7a7ab4924debad8ba3c4be77ee02ac` — exactly the digest the entry claims (entry line 80). The entry's printed stdout block is 7546 B; block+`\n` = 7547 B, SHA-256 `58b63dd9d7c7ae4a0311ff33f12317345f7e5b7c9e8f204cfb13d1d599f0c416` — exactly the digest the entry claims.

| run | cwd | root argument | exit | stderr | stdout SHA-256 | lines |
|---|---|---|---|---|---|---|
| A | scratch | `treeA` (relative) | 0 | 0 B | `58b63dd9…f0c416` | 25 |
| B | `treeA` | `/fast/scratch/hyaku/revenger-r62/R62FReproduceJs/treeB_copy_root_alt` (absolute, distinct path) | 0 | 0 B | `58b63dd9…f0c416` | 25 |
| C | scratch | `treeB` (candidate commit d9776195) | 0 | 0 B | `58b63dd9…f0c416` | 25 |
| D | scratch | `treeA/` (trailing slash) | 0 | 0 B | `58b63dd9…f0c416` | 25 |
| E | scratch | `linkA` (symlink to treeA) | 0 | 0 B | `58b63dd9…f0c416` | 25 |
| F | `treeA` | `.` | 0 | 0 B | `58b63dd9…f0c416` | 25 |

`diff` of the entry's printed stdout block (plus its trailing newline) against run A stdout: empty — byte-identical. Runs A–F byte-identical to each other (root-path independence holds across relative/absolute/symlink/`./`/trailing-slash/candidate-commit roots). Python 3.14.8; `TMPDIR=/fast/scratch/hyaku/revenger-r62/R62FReproduceJs/tmp`.

**No external file dependency.** `strace -e trace=openat,open,stat,newfstatat` of run A: the only corpus opens are the 10 paths under the supplied root (`treeA/corpus/fixtures/js-r3/{index.js,package.json,transform.js}`, `treeA/corpus/fixtures/js-r7-v2/{…}`, `treeA/corpus/live/runs/20261012T164357Z/analysis.json`, `treeA/corpus/live/runs/round-7/v2-analysis.json`); all other opens are interpreter/stdlib/locale (`/usr/lib/python3.14`, `/usr/lib/locale/locale-archive`, `/etc/ssl/openssl.cnf`, `/etc/localtime`). `readout.py` imports only `hashlib, json, os, re, sys` (stdlib; no install).

**Independent digests of the eight corpus inputs** (`sha256sum`, outside the script) match entry items 1 and 6 exactly: `f7d8bf47…`, `92ef8e3d…`, `cd9f3f63…` (js-r3); `b53d96d4…`, `92ef8e3d…`, `cd9f3f63…` (js-r7-v2); `7c3ba8c1…` and `331ec252…` (records). Fixture/record bytes at `a3498e25…` and `d9776195…` are byte-identical (`cmp`).

**Q11 semantic audit (not token-presence).** 112 field-level assertions were checked one by one against the parsed stdout for entry items 1–13: file sets/bytes/digests, `package_type`, source line text/names/specifier/line number/non-empty count, all three spans for both fixtures (both bases + text), record bytes/sha/evidence_id/operation/provider id+version/path, `recorded_root_artifact_sha256` for both fixtures, edge counts, every `imports` edge's `imported_name`/`specifier`/`resolved_path`/`state`/`location.*`/`target.*`, within-fixture deltas, cross-record delta, plus the item-11 equalities (saved columns vs manual spans, and saved `span_text_from_fixture` vs the fixture bytes sliced at the saved columns). All 112 pass; no prose value in items 1–13 contradicts or outruns its stdout record. (One audit expectation of mine was wrong, not the entry's: js-r3 has two named edges sharing one span — multiplicity, not defect.)

**Derivation is live, not assumed (mutations on scratch copies only).** Two matching lines → exit 1, stdout 0 B, stderr `expected exactly one destructured require line, found 2`; zero matching lines → exit 1, `found 0`; missing record file or missing `index.js` → exit 1 `FileNotFoundError`, stdout 0 B; an extra file in a fixture dir → exit 0 but stdout changes (`files[]` gains `extra.js`). The "exactly three files" and one-line bounds are printed values, not assumptions.

**Item 29 / item 30 claims hold.** `corpus/knowledge/commonjs-destructured-require-edges.md` blob is identical (`df24b9ad1a09d9f1ebbe9a8e42bd13ab54a9e634`) at `5bd4a90…`, `a3498e25…` and `d9776195…`; the entry names that file only in item 29, never as support. `corpus/lessons/round-62.md:29` carries `ADJ-06 sibling arbitration | Operator-owned and unresolved; new entries do not declare ownership or a ruling.`

## Findings (material, both non-fatal)

F1 — entry line 80 (§Reproduce): "The stdout carries no path, so the same bytes give the same 25 lines from any extraction directory." **Literal wording is false**: the stdout carries ten root-relative path strings (`corpus/fixtures/js-r3`, `corpus/fixtures/js-r3/index.js`, `corpus/fixtures/js-r7-v2`, `corpus/fixtures/js-r7-v2/index.js`, `corpus/live/runs/20261012T164357Z/analysis.json`, `corpus/live/runs/round-7/v2-analysis.json`, and `files[].path`). The property the sentence argues for — no absolute or root-dependent path — is true and verified (runs A–F). Wording defect only; no load-bearing value changes. Minimal correction: "The stdout carries no absolute or root-dependent path (its path strings are root-relative), so …".

F2 — entry line 248 (§Sources, S029): "This entry uses **one** quoted text, the property read in §14.3.3.3: "Set value to ? GetV(value, propertyName)." — 8 words." **The count is wrong under every standard counting**: the quoted string is 6 whitespace tokens and 6 word-character tokens (`Set, value, to, ?, GetV(value,, propertyName).`), and the entry's own HTML-normalised variant "Set value to ? GetV ( value , propertyName )." is 10 whitespace tokens. No counting yields 8. Q11 (unchanged `corpus/QUALITY.md:23`) requires that "Each count, identifier, offset and digest in an entry carries, inside the entry, the command that derives it … and that command's output"; this count carries no derivation and its value is wrong. Non-fatal: the quoted text is still far under the 25-word limit and the quote itself is unchanged. Minimal correction: replace "— 8 words" with "— 6 words", or delete the count.

## Inference

- [INFERENCE] The entry's central reproduction claim — one command, exit 0, 25 stdout lines, stdout SHA-256 `58b63dd9…f0c416`, independent of the extraction directory — is reproduced exactly on six distinct roots, including the candidate commit's tree; the printed block in the entry is byte-identical to the produced stdout.
- [INFERENCE] Every value in entry items 1–13 is derivable from the printed stdout at the frozen revision; the Q11 inventory's record/field pointers exist and carry the claimed values (112/112).
- [INFERENCE] F1 and F2 are wording/count defects at the prose layer; neither changes a byte, a digest, a span, a name set, a coverage-map row or the entry's scope.

## Unknown / not attacked

- The S029 single-page digest `06db92a8…` and the row's `mined` status rest on the authoring lane's page fetch; not re-verified here (no network use by this seat).
- Whether the saved records' other nodes/relations/fields are correct (entry item 21) is out of my scope; only the named fields were read.
- Runtime/export/module-loading behaviour (items 18–19) remains unknown and unclaimed by this entry; nothing here bears on it.

## Verdict

Reproduction axis: **holds** on every assigned point (exit, stderr, full-stdout SHA-256, root-path independence, no external file dependency). Q11: **holds for items 1–13** (112/112 field checks). Two wording-level defects stand (F1 false literal about paths; F2 wrong word count, Q11 count clause) — non-fatal, no repair applied, minimal corrections named above for the L1's adjudication. Overall grade **PARTIAL** (BROKEN is not warranted: no contradiction in any load-bearing value, no missing requirement). No admission decision is mine to make; README C04 remains `uncovered`.

Installs/updates: none (no package installed or upgraded; Python 3.14.8 and `strace` were already present). Scratch/transcript: `/fast/scratch/hyaku/revenger-r62/R62FReproduceJs/` (`run/A.stdout`, `run/A.stderr`, `run/A.strace`, `tmp/q11_audit.py`, `readout.py`, `expected_stdout.txt`).
