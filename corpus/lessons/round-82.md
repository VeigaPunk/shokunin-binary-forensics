# Round 82 — a second artifact-graph operation moves through a real dylib-resolution producer run (criterion A1, `trace_dylib_resolution`); the orphan sweep learns the counting-command fidelity class (v3 supersession)

Base `33764dd29aaab69457327618e2a2c14900d5b634` (r81 tip + non-author
spot-check). Freeze `ad74dc88342a7f3b314c786ad0bbea379df8af15` (claims +
sha-pinned instruments + red-befores + preprobe receipt, committed before
any after-run). Landing `9201d97a92ea6b355e8c9d713d2c3b0c8aa7a13b`
(Mach-O fixture + producer record + S459–S461). Adjudication = the commit
carrying this lesson. Two claims, distinct axes, causally separable,
neither exploratory: **C1 coverage** (criterion A1 registration —
artifact-graph operation record depth — + one real
`rea trace-dylib-resolution` record on an authored inert two-image Mach-O
tree) and **C2 calibration** (orphan_sweep v3 — the r81 closure's routed
counting-command fidelity class closes inside the standing instrument:
registered corrected greps, a mutation-checked fidelity vector, and the
carried count-basis/full-output receipt rules).

## Carry-in dispositions (r81 non-author closure; addressed first)

1. **Red-grep count** — first-hand reproduced over committed bytes, not
   taken on trust (`reports/round-82/countgrep-red.log`, over
   `git show 33764dd:reports/round-81/sweep-v1-red.log`): the pasted
   trailing-space pattern returns **1** (not the stated 2); the corrected
   alternation (no trailing space) returns **2**; the separate-prefix form
   returns **1 + 1**. Substance unchanged (v1 misdispositions exactly those
   two committed files; line 160 is the multi-ref token
   `…evidence.md:57,:148,` whose first alternative can never be followed
   by a space). Fix landed as v3 change 5 (registered corrected counting
   commands + `SWEEP_SELFTEST_COUNT_FIDELITY` vector with truth=2 on
   exactly that shape + `SWEEP_SELFTEST_COUNTCMD_MUTANT_FLAGGED` mutant
   kill); this round's own texts quote only single-line corrected-form
   greps.
2. **Correction numstat convention** — first-hand reproduced
   (`reports/round-82/carryin-numstat.log`): raw numstat of the r81
   correction `b2fc6bb` vs its landing `88b7e7ce` on LOG.md = `10 0`
   (10 raw added lines = 9 content lines + 1 blank separator line; 0
   deletions). The r81 wording "0 deleted / 9 added" counted content lines
   excluding the blank separator; the raw-numstat convention includes it.
   Correction stated in this round's LOG entry (append-only; the r81 entry
   is not rewritten).
3. **Receipt-vs-regrown-corpus comparability** — adopted: this round's
   sweep receipt carries its basis line
   (`SWEEP_CORPUS fleet-reports=22 lessons=44` in
   `sweep3-real-after.log`); narrative counts cite `grep -c` of
   named-corpus receipts; basis lines are compared first, never bare CITED
   values across corpora (the v2 `SWEEP_CORPUS` header stands unchanged).

## Gate

Fresh-start §7 (r71/r72/r73 rejected closures re-read this round at fleet
`.ufo/reports/round-7{1,2,3}/revenger.md`): all three are K-admission
claims whose wave Q-review surface never existed or never settled on this
host — a do-nothing control reaches each identically here. Ruled out with
fresh probes (2026-11-01): **F android** (`REA_JADX_MCP_JAR` UNSET, no
jadx on PATH, `~/tools` = downloads/ + ghidra only — S448 stands; F4's
honest exception is 10/11, not 11/11); **macho/signature** (`rea
capabilities`: the native-macho provider `demangle_swift,inspect_macho,
inspect_plist,list_architectures` and the signature provider
`inspect_signature,observe_native_ui` both `unsupported_host`, S453);
**K admissions** (r74 L0 re-read, unanswered); **criterion C repair**
(§9 sizing, unchanged r78–r81); **criterion R full extension / criterion
N attribution pair** (stay routed — not declared; C2's registered-counting
form covers the parser classes only). The `decode_interface_builder`
operation is available but NOT claimed: its `--help` names an `.app`
bundle input — authoring a full inert app-bundle surface is a separate
bounded round. C1's route is the one the ruling-out map leaves open:
`trace_dylib_resolution` is a DIFFERENT surface from the
`unsupported_host` macho/signature providers (its own provider group,
`available: true`, `availability_code: null` on win32 — it parses the
file, no macOS native utility is invoked), in the r81-recorded family but
unrecorded.

Sources opened this round (rows appended inside the Registry section,
directly after S458):

| row | path/command | located quote (≤25 words) | decision |
|---|---|---|---|
| S459 | `PYTHONUTF8=1 rea trace-dylib-resolution --help` + `PYTHONUTF8=1 rea capabilities` (provider `rea-artifact-graph` group), opened 2026-11-01 | "Trace dyld load-path resolution for a Mach-O or every executable in an app bundle" | ADMIT (tier A, own-work environment) |
| S460 | `corpus/live/runs/round-82/` (record, receipt, LEDGER) + `corpus/fixtures/macho-r82/` (fixture, generator, truth, oracle), opened 2026-11-01 | exit 0; `operation: trace_dylib_resolution`, provider `rea-artifact-graph`; oracle `ORACLE OK (47/47 checks)` | ADMIT (tier A, own-work) |
| S461 | `corpus/lessons/round-81-verifier-spotcheck.md` §6 defect 1, opened 2026-11-01 | "the multi-ref token prints as `…evidence.md:57,:148,`, so the first alternative can never be followed by a space" | ADMIT (tier A, own-work) |

Census: round start — sanctioned explicit-lane-dir form exit 0, 31 W
(21 W01 + 10 W04, the same disclosed classes as r74–r81); literal form
exit 2, disclosed r74–r81 lineage (the consolidation L0 line stands).
Round end — receipts in `reports/round-82/census-after.log`: sanctioned
worktree form exit 0 (zero E-findings), literal form exit 2 (unchanged
lineage); landing-archive-bytes census over `9201d97` fires **E11 ×3**
(`S459`/`S460`/`S461` used-by `corpus/lessons/round-82.md` preceding the
lesson — the expected intermediate state, same shape as r80's S455 and
r81's S457/S458; resolved by the adjudication commit that carries this
lesson). Host convention disclosed: fixture `truth.json` files are written
text-mode on this host and carry CRLF (this round's and r81's alike —
bytes pinned where identity matters is the image bytes; JSON content
parses identically under universal newlines).

C1 evidence chain: S459 (the operation `available: true`, in the
r81-recorded family but unrecorded) → A1 mapping frozen at `ad74dc8`
BEFORE the run (ag_probe sha `22be124b…a08a5`; denominator disclosure in
the instrument header and claims: A1 is a NEW instrument, base prints
1/3 = 3.33; the family-level F4 instrument is NOT a claim this round) →
red `ag-red.log` (base archive: `A1_RECORDED=1/3 score=3.33`, only
`inspect_keyed_archive=round-81`) → preprobe receipt
(`preprobe-macho-shape.log`: probe 1 — the 6.8.0 parser REJECTS a
4-aligned `cmdsize 68` with `target_unavailable`, so the builder asserts
cmdsize % 8 == 0 per command; probe 2 — single-image shape; probe 3 — the
two-image resolved-candidate shape) → fixture authored
(`corpus/fixtures/macho-r82/`: image/main.dylib 304 bytes sha
`5f56d14d…9507d` — LC_ID_DYLIB `@rpath/librevenger-r82.dylib`, three
LC_LOAD_DYLIB covering the three resolution classes, LC_RPATH
`@loader_path/rpathdir`; image/rpathdir/libalpha.dylib 80 bytes sha
`bda3d4ff…bcf07` — leaf; generator 15/15 SELFCHECK derives every
byte-derived oracle fact from the built bytes; regen byte-identical) →
one bounded producer run on the committed bytes (`inspection.json` =
exact stdout, 7364 bytes, sha256 `05142d7e…6e786`, exit 0, stderr 0
bytes, Evidence `ev_851a74058ef2973352f214efbf3798b96f98de3d87a3d1e9340fb3ddc04d514a`)
→ oracle `ORACLE OK (47/47 checks)` — 37 BYTE checks (operation, provider,
subject format/sha == fixture sha, target sha, roots, 2 images parsed with
slice sizes 304/80 and cpu/file-type/install-name/rpath identity from the
built bytes, 3 edges in load-command order with versions "1.0.0" packed
from the authored 0x10000, candidate sources rpath/loader_path/literal,
edge0 candidate path == the authored tree, resolved_path present; host
fields never checked) + 10 pre-registered Q07 HYPOTHESIS checks
(outcome/resolution/coverage/confidence/authority — recorded as predicted,
whichever way they fall; no cause stated) → green `ag-after.log` (landing
archive: `A1_RECORDED=2/3 score=6.67` with
`trace_dylib_resolution=round-82`; oracle + regen re-run over archive
bytes; F4 hold 10/11 unchanged).

C2 evidence chain: S461 (the r81 closure's routed repin rule) → v3 frozen
at `ad74dc8` (orphan_sweep3 sha `af64b4c5…b8748`; v2 blob unchanged
`30aa3527…93eb6` re-verified over the landing archive; declared exits
0/1/64 unchanged) → red `sweep-v2-selftest-red.log` (committed v2 over the
base archive: selftest exits 0, 7 legs, ZERO count-fidelity legs —
`grep -c "SWEEP_SELFTEST_COUNT\|SWEEP_PARSER"` = 0 — and no plain run
prints any `SWEEP_PARSER_*` value) + `countgrep-red.log` (the drift
itself: pasted 1 vs corrected 2 over committed r81 bytes) → green
`sweep3-selftest-after.log` (9 legs from the landing-archive extraction
outside any repo: v2's seven + `SWEEP_SELFTEST_COUNT_FIDELITY=ok
(truth=2, A=1, B=1)` + `SWEEP_SELFTEST_COUNTCMD_MUTANT_FLAGGED=ok
(mutant=1 truth=2)`; `SWEEP_SELFTEST=pass`, exit 0) +
`sweep3-mutant-kill.log` (the frozen one-substitution sed mutant over the
landing-archive bytes dies exit 1 with the attributed last line
`selftest: counting-command fidelity drifted (trailing-space class)`) +
`sweep3-real-after.log` (full output over the real tree, exit 0,
`SWEEP_PARSER_GREP_A=0 _B=0 _AB=0` each reproduced by its registered
`grep -cE` over the receipt bytes, `SWEEP_CORPUS fleet-reports=22
lessons=44`, `CITED=369 COMMITTED=357 LANDABLE_ORPHANS=0 ABSENT=12` —
verdict values identical to the v2 receipt's corpus, basis lines cited
first per carry-in item 3). Separability: `c1-only.log` (A1 2/3 + oracle
OK with orphan_sweep3 ABSENT) and `c2-only.log` (selftest pass with
ag_probe ABSENT).

Boundary: C1's print moves 1/3 (3.33) → 2/3 (6.67) on a NEW instrument —
the moved quantity is the in-province operation with an oracle-checked
record, not family presence (F4 stays 10/11; the family's numerator did
not move). The record demonstrates the built-in provider's dyld
load-path read of one authored inert two-image tree; the producer's own
`coverage: partial` semantics are recorded as observed, not explained
(Q07). `decode_interface_builder` and android stay unrecorded — A1's
honest exception is 2/3, not 3/3. C2 moves no criterion score; the moved
quantity is the standing capability's counting-command fidelity (the
drift class the r81 closure caught by hand becomes machine-caught inside
the instrument) plus receipt value lines. No knowledge admission (K 8/15
untouched — operator-blocked route re-checked, not attempted); no README
byte changes; PROVINCE byte-unchanged.

## Mistakes

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| Layout-from-intent: the LC_RPATH header was drafted 16 bytes wide (like a dylib command) when its header is 12 bytes (cmd, cmdsize, path.offset) | the builder's own tiling assert before any producer call: `AssertionError: load commands do not tile the declared size` — the walked sizes (56+48+68+52+40=264) overran the declared sizeofcmds 260 because the rpath command wrote 36 body bytes while declaring cmdsize 40 | the Q06 derive-then-assert discipline (the structural walk re-derives offsets from the built bytes; SKILL.md §2) | header width derived from the struct field list per command type; the tiling assert retained; final build tiles exactly |
| Producer-premise: a 4-byte-aligned cmdsize (68) was rejected by the 6.8.0 parser (`target_unavailable`, "invalid cmdsize 68") — the 64-bit image requires cmdsize % 8 == 0 even where the spec text allows 4 | the M33 pre-probe itself (`preprobe-macho-shape.log` probe 1; exit 1, stderr 0 bytes) | the pre-probe (Q05: probe the premise against the tool before any committed call) | `align8` + per-command `%8` asserts in the builder; the constraint recorded in the generator docstring and truth recipe |
| Counting-command fidelity (the carry-in class, self-caught on my own first reproduction): the reproduction grep was run with `\|` inside double quotes under `-E`, which matches a literal pipe — it printed 0 (exit 1), agreeing with NEITHER the r81 text (2) nor the closure's correction (1) | the count disagreeing with both stated values (0 ≠ 1 ≠ 2) before any receipt was committed | the closure's stated 1 conflicting with my first observed 0 | re-run single-quoted so `|` is alternation (1 reproduced, corrected form 2); the committed receipts quote only single-line, single-quoted, corrected-form greps; mined so a pasted pattern is de-escaped and re-quoted as one line before it is counted |
| (process, self-caught pre-commit) the two long receipts (sweep receipts, claims) and instruments were drafted in a Windows editor session that wrote CRLF; the r81 CRLF lesson's byte-check (`worktree == blob`) was run BEFORE the freeze instead of after the landing, and the freeze blobs landed LF with pins matching the blobs | `git show ad74dc8:reports/round-82/ag_probe.py \| sha256sum` == the pinned `22be124b…` (verified post-commit) | the r81 CRLF class check applied at commit time (this time before pushing further work) | the freeze sha pins are stated over LF blob bytes and re-verified from `git show` after the commit; the same check repeated for the landing (all landed artifacts CR=0 except the disclosed text-mode truth.json convention) |

## Routed forward

- **Criterion R full extension** (the legacy receipt-quoting rows beyond
  the parser classes) and **criterion N's mutation-killed attribution
  pair** — r75–r82 lineage; still open, not declared this round.
- **Criterion C repair** — §9 sizing, unchanged since r78.
- **Criterion-instrument class question** — unchanged; orphan_sweep3 lands
  as a capability supersession note in the existing r80 row (current
  instrument v3), NOT a registry row.
- **A1's remaining operation** — `decode_interface_builder` on an
  authored inert `.app` bundle surface is one bounded fixture+record
  round if a later round wants it (bundle authoring is a larger fixture
  than r79–r82's file-shaped fixtures).
- **F android** — hard-gated on the caller-supplied `REA_JADX_MCP_JAR`
  (re-probed; S448 receipt stands). A1's honest exception: 2/3, not 3/3.
- **K** — blocked on the wave Q-review surface (r74 L0 unanswered,
  re-read this round at the fleet `.ufo/l0-questions.md`).
- **Census literal form** — operator-side routing continues (r74–r82
  lineage; the consolidation L0 line stands).
- The real sweep absents keep their recorded dispositions (ScoutAmp
  misroot, round-73/votes, w1.ready, .pyc, measurements.json,
  controls/A-H) — v3 touches only the counting-command class.
