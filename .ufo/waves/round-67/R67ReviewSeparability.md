SEPARABLE — the measured claim surfaces are file-disjoint inside corpus/ (C1: `corpus/knowledge/round-67-apk-axml-byte-evidence.md` + `corpus/SOURCES.md`; C2: `corpus/check_embedded_outputs.py`); the only jointly-modified file `SKILL.md` carries distinct additive registry rows per claim; joint files `reports/round-67/{claims.md,measure.py,measure-before.log}` are the shared contract/instrument, not claim-evidence bytes; one designed one-directional coupling remains: counter label `C7_V2_CLEAN` reads C1's v2 entry (`measure.py:412-418`), so C2's *pass* requires C1's file, while no C1 label reads any C2 byte.

# Scope
Seat: R67ReviewSeparability (reviewer, leaf). Task: causal separability of C1 vs C2 per `reports/round-67/claims.md` (frozen). No edits made; read-only audit. No tools installed (none needed).

# Build tip resolution
No `.ufo/waves/round-67/build-commit.txt` exists → used HEAD `7668510ffc49733daf023e40ff3300ef387ebde5` ("round-67: build — C05 v2 candidate …", 2026-10-24 21:03:19 -0300) per the brief's fallback. Working tree is clean except untracked `.ufo/waves/round-67/*` wave artifacts and untracked `corpus/lessons/round-67.md` (the registered round-67 mistakes file — NOT in the build tip; if committed later it lands outside both claims' surfaces: `lessons/`, not `knowledge/`/`README`/`SOURCES`/`check_*`).

# Command
`git -C /home/vgpnk/Projects/shokunin/revenger-shokunin diff --name-status fa0eb3eb33f22f56ebf066dea5440121a30d55a2..7668510ffc49733daf023e40ff3300ef387ebde5`

Actual output (17 files, all `A` except two `M`):
```
A  .ufo/waves/round-67/assimilation/{collisions,quarantine-slice,reg-ids,register-rows.json,staged-ids}
A  .ufo/waves/round-67/{build-entry.py,build-wave-spec.py,plan-validated.json,wave-spec.json}
A  .ufo/waves/round-67/source-snapshots/dex-format.html
M  SKILL.md
M  corpus/SOURCES.md
A  corpus/check_embedded_outputs.py
A  corpus/knowledge/round-67-apk-axml-byte-evidence.md
A  reports/round-67/{claims.md,measure-before.log,measure.py}
```
`git diff --stat`: 12454 insertions, **0 deletions** — every touch is additive.

# Per-file claim attribution
| file | owner | evidence |
|---|---|---|
| `corpus/knowledge/round-67-apk-axml-byte-evidence.md` (A, 187 ln) | **C1 only** | the v2 candidate; grep shows zero references to `check_embedded`/`verify_`/`measure.py` inside it |
| `corpus/SOURCES.md` (M, +2 ln) | **C1 only** | +S045 row after :56; +round-67 search-log note after :85 (C1 repair 4) |
| `corpus/check_embedded_outputs.py` (A, 169 ln) | **C2 only** | the C7 gate; reads only the `--entry` path argument, runs its declared `$ cmd` blocks (`run_cmd` shlex argv, no shell) |
| `SKILL.md` (M, +21 ln, two hunks) | **both — bookkeeping only** | hunk 1 (after :257): `## Gate registry` 15-row block for `check_embedded_outputs` = C2's registered row; hunk 2 (after :329): six `§7` inventory rows naming S045, the v2 entry, the gate, and the three reports files |
| `.ufo/waves/round-67/source-snapshots/dex-format.html` (A) | C1 evidence | S045 snapshot; outside `corpus/` → invisible to the counter (`git archive … corpus`) |
| `.ufo/…/assimilation/*`, `build-*.py`, `wave-spec.json`, `plan-validated.json` | wave contract | registered artifacts, not claim surfaces |
| `reports/round-67/claims.md`, `measure.py`, `measure-before.log` (all `A`) | **joint contract/instrument** | frozen predicate + counter + red-before receipt; assigned to C2's surface by the brief, but `measure.py` computes both claims' labels |
| `corpus/README.md` | **untouched** | `git show 7668510:corpus/README.md` :34 still reads `| C05 | Android packages (APK) | — | … | uncovered |` — consistent with "(post-adjudication only) README C05 row" |

# Verification independence (counter-level, from committed `measure.py` sha256 7933c060…bc07e)
- **C1 labels need no C2 byte.** `K_HELD`/`K_ROW C05`/`K_HELD_BACKED`/`K_HELD_BACKED_STRICT`/`README_TOKEN_LEGEND_MISMATCH` read only `corpus/README.md`, `corpus/knowledge/*.md` existence, and `corpus/live/runs/*.json` (`measure.py:28-43,54-58,83-98`); `C05_SINGLE_V2` reads the C05 row + entry filename (`:62-67`). Deleting `check_embedded_outputs.py` changes no K label. ✔ "K labels need only knowledge/SOURCES/README" holds (SOURCES.md itself is an adjudication input — the counter never opens it).
- **C7 labels evaluate without C1's file, but C2's pass does not.** `GATE_PRESENT`/`SELFTEST`/`CONTROL_PASS`/`MUTANT_KILLED_ATTRIBUTED`/`RED_ON_R65_CANDIDATE` consume only the gate file, its in-script forged control, and the **base-owned** r65 entry `round-65-apk-axml-byte-evidence.md` (`:364-411`); the mutant sandbox `copytree`s corpus but runs only `--self-test`, which is hermetic (gate `check_embedded_outputs.py:106-142`, tmp-tree cases). `C7_V2_CLEAN` alone reads `corpus/knowledge/round-67-apk-axml-byte-evidence.md` (`:412-418`) and degrades to `n/a (no v2 file)` if absent — so the frozen predicate `C7_V2_CLEAN=yes` is unreachable without C1's file landing. This is the declared re-gating coupling (the M39 fix re-run over the new candidate), strictly one-directional: nothing in C1's predicate or labels reads the gate.
- **`HOLDS_OK_V5` is a joint label by design** (`:452-454`: `holds_ok_v4 ∧ c7_targets`) — it appears in both claims' predicates and the void conditions, so a missing gate no's it for the round regardless of C1's state. That is a shared round-level invariant, not a claim-surface overlap.
- The brief's "C7 labels need only the gate file" is over-broad at file granularity: `C7_RED_ON_R65` reads the r65 entry and `C7_V2_CLEAN` reads the v2 entry. Harmless direction (C2→entries), but recorded for calibration.

# Residual observations (non-blocking)
1. `SKILL.md` is the single file touched by both claims' bookkeeping (C2 gate-registry hunk; C1-side S045/v2-entry inventory rows). Row-level, each hunk belongs to one claim; the brief itself assigns SKILL.md to C2's surface. If "touched by both" were read at whole-file granularity, `SKILL.md` would be the answer — but the touch is additive registry text, not shared claim-evidence bytes, and no predicate reads it.
2. `claims.md`'s separability sentence ("C2 … touches no existing byte") under-scopes the diff: `SKILL.md` and `corpus/SOURCES.md` are existing files modified this revision (both registered: gate-registry row, S045 row). The sentence is true only within `corpus/` claim-evidence scope.
3. `measure.py` does not read `SKILL.md`, `SOURCES.md`, or the snapshot — SKILL/SOURCES correctness matters to adjudication (Q decisions), not to the counter.

# Not verified (saturation boundary)
- I did not re-run `measure.py` on the after tree (measurements belong to committed trees; counter replay is another seat's item). Label dependency claims above are from reading the committed counter code (`measure.py:28-455`), which is the canonical logic for this check.
- I did not attack the gate's internals or the entry's content (assigned to other seats); the independence claim rests on file-set disjointness + the counter's read graph, both evidenced above.
- `corpus/fixtures/` and `corpus/live/` confirmed untouched by the name-status diff (void condition holds at surface level).

# Verdict
**SEPARABLE.** Disjoint claim-evidence file sets in the measured tree; C1 verifies fully without C2; C2 evaluates without C1 and its sole C1-facing read (`C7_V2_CLEAN`) is the designed re-gate. If the seat verdict requires naming a jointly-touched file: `SKILL.md` (bookkeeping rows only).
