# round-83 claims (frozen before any after-run)

Base `60693f2ce6b086ea3f0ee84fe27a8f8a13d46f46` (r82 tip + non-author
spot-check + the r83 carry-in receipt completion, which this round landed
FIRST per the r82 non-author closure's first obligation:
`reports/round-82/{ag-after.log, sweep3-selftest-after.log,
sweep3-mutant-kill.log, sweep3-real-after.log, c1-only.log, c2-only.log,
noharm-diff.txt}` — all seven byte-verified worktree == landed blob, and
the standing orphan_sweep v3 re-run went LANDABLE_ORPHANS=2 (exit 1,
`.ufo/waves/round-83/sweep-pre-landing.log`) → 0 (exit 0,
`.ufo/waves/round-83/sweep-post-landing.log`) over the landing). This
file, the sha-pinned v4 instrument (`orphan_sweep4.py`), the red-befores
(`ag-red.log`, `v3-prelanding-recon.log`) and the preprobe receipt
(`preprobe-app-shape.log`) freeze BEFORE the landing (fixture + producer
record) and BEFORE any after-run. Two claims, distinct axes (coverage,
calibration), causally separable, neither exploratory.

## C1 — coverage: the artifact-graph family's third operation (`decode_interface_builder`) moves through a real interface-builder producer record (criterion A1 2/3 → 3/3)

Registered criterion A1 (`reports/round-82/ag_probe.py`, frozen r82, blob
unchanged — sha re-verified below): the rea-artifact-graph provider's
declared operation group (`decode_interface_builder`,
`inspect_keyed_archive`, `trace_dylib_resolution`) counts RECORDED iff
some `corpus/live/runs/round-*/` carries both an `inspection.json` whose
`operation` equals the operation AND a `receipt.json` with
`exit_code == 0` and an `oracle.result` starting `ORACLE OK`. Denominator
disclosure (r82 freeze, unchanged): denominator 3.

- BEFORE (red, committed `ag-red.log`): over the base archive `60693f2`:
  `A1_RECORDED=2/3 score=6.67` with
  `decode_interface_builder=unrecorded`.
- WORK: author the inert `.app` bundle fixture
  (`corpus/fixtures/app-r83/`: `build_app.py` — 18-check SELFCHECK that
  re-parses the built bytes per the parser-source layout and re-derives
  every byte-derived oracle fact; regen byte-identical (verified in
  scratch across two builds); `truth.json` written by the generator's
  derive(); `oracle_check.py` with 26 BYTE + 18 pre-registered Q07
  HYPOTHESIS checks — 44 total; bundle `R83Sample.app/` = root-layout
  `Info.plist` (XML) + `Base.lproj/MainMenu.nib` (213 bytes, 4 objects /
  6 keys / 7 values / 3 classes incl. one source-encoded NSActionConnector
  and one sourceless NSIBHelpConnector annotation) +
  `Base.lproj/SecondView.nib` (79 bytes, 1 object)), run ONE bounded
  producer run on the committed bytes from the lane root
  (`rea decode-interface-builder corpus/fixtures/app-r83/R83Sample.app
  --format json`, exact stdout saved, exit 0, stderr 0 bytes, receipt),
  oracle `ORACLE OK (44/44 checks)`. Preprobe receipt committed at the
  freeze (`preprobe-app-shape.log`: the supported-Info.plist-layout
  premise failure, the standard-LEB128 varint rejection ("NIBArchive
  variable integer is too long" — the terminator-bit encoding is the
  inverse of LEB128), and the final-shape vocabulary probe).
- AFTER (green, `ag-after.log`, landing archive): `A1_RECORDED=3/3
  score=10.00` with `decode_interface_builder=round-83`; oracle re-run
  over the landing-archive bytes, 44/44.

VERIFY conditions (all four must hold): (a) A1 prints 3/3 over the
landing archive; (b) the record's `operation ==
decode_interface_builder`, provider `rea-artifact-graph`, exit 0, stderr
0 bytes, `evidence_id` form `ev_<64hex>`; (c) oracle `ORACLE OK (44/44
checks)` over the archive bytes (the 18 HYP checks pass against their
pre-registered values in `truth.json` — recorded whichever way they
fall); (d) the family-level instrument F4 hold unchanged (10/11 — this
record does not move F4; the family is already present) and the r82
A1 holds unchanged (`inspect_keyed_archive=round-81`,
`trace_dylib_resolution=round-82`). KILL RULE: any condition fails → the
candidate record is retained rejected (`admission-status` note in the
LEDGER), README byte-unchanged, A1 prints 2/3 — recorded honestly as
falsified.

Boundary: operation-record presence only; the record demonstrates the
built-in provider's compiled-NIB decode of one authored inert two-document
bundle (Q10 scope note in the LEDGER: no general app-bundle claim, no
storyboard claim — no `.storyboardc` surface authored; the producer's own
coverage semantics, incl. the `hierarchy: unsupported` facets, are
recorded as observed, not explained). No knowledge admission (K untouched,
8/15); no README byte changes; PROVINCE byte-unchanged.

## C2 — calibration: orphan_sweep v4 — the bare-filename citation class closes inside the standing instrument

v4 supersession of the r82 capability instrument (`reports/round-83/
orphan_sweep4.py`, sha256 pinned below; v3 `reports/round-82/
orphan_sweep3.py`, v2, v1 stay byte-untouched). One named change (v4
change 6), closing the class THIS round's carry-in demonstrated:

6. Bare-filename receipt normalization. The r82 carry-in: seven green
   receipts cited by the r82 report/LOG/lesson but never committed, of
   which the standing v3 flagged only TWO (LANDABLE_ORPHANS=2, exit 1,
   `.ufo/waves/round-83/sweep-pre-landing.log`) — the other five were
   cited by BARE FILENAME and the lane-domain filter
   `^(?:reports|corpus|\.ufo/waves)/` skips every token without a slash,
   so a cited landable receipt was never flagged (fail-open corpus blind
   spot). v4 collects bare single tokens (no slash, ASCII, no
   space/{}*<>|) as citations and normalizes each against the basename
   index of HEAD ∪ working tree: no match → skipped (counted
   `SWEEP_BARE_TOKENS matched=… unmatched_skipped=…`); matches → every
   candidate classified, any never-committed candidate flags ORPHAN
   naming the candidates (conservative ambiguity: one committed match
   never launders a second uncommitted match under the same basename).
   Selftest gains four legs (13 total):
   `SWEEP_SELFTEST_BARE_ORPHAN_FLAGGED` (committed r81 match + on-disk
   r82 match under one basename → orphan),
   `SWEEP_SELFTEST_BARE_COMMITTED`, `SWEEP_SELFTEST_BARE_UNMATCHED_SKIPPED`,
   and `SWEEP_SELFTEST_BARE_MUTANT_FLAGGED` (the disabled twin must
   disagree with the vector). The frozen sed mutant (one substitution,
   recipe pinned below) flips `BARE_TOKEN_CLASSIFICATION` to False; the
   mutated `--selftest` must die exit 1 with the attributed last line
   `selftest: bare-filename classification drifted (bare-token class)`.

- BEFORE (red, committed `v3-prelanding-recon.log`): the MINIMAL
  pre-landing state reconstructed in scratch (fresh repo, HEAD =
  `c153e448…` via fetch + update-ref — no checkout — plus exactly the
  seven worktree receipts on disk): committed v3 exits 1 with
  `LANDABLE_ORPHANS=2` while SEVEN landable cited receipts exist on
  disk; v4 over the SAME state (`v4-prelanding-recon.log`) flags 9
  orphan rows covering all seven files (`ag-after.log` and
  `noharm-diff.txt` are each cited in two forms — full path and bare —
  and rows count citation forms, the instrument's CITED basis).
- AFTER (green): v4 `--selftest` 13/13 legs + `SWEEP_SELFTEST=pass`,
  exit 0 (hermetic; `selftest-v4.log`); the sed-mutated bytes die exit 1
  attributed (`mutant-kill.log`); v4 over the same reconstruction with
  HEAD = the carry-in landing `60693f2` reports `LANDABLE_ORPHANS=0`
  exit 0 (`v4-postlanding-recon.log` — the class is resolved by the
  landing, not by the instrument's absence); real-tree full receipt
  exit 0 with the `SWEEP_CORPUS` basis line + `SWEEP_BARE_TOKENS` line
  (`sweep4-real-after.log`).

VERIFY conditions (all four must hold): (a) v4 selftest 13/13 legs +
pass, exit 0; (b) the sed-mutated v4 dies exit 1 with the attributed
last line; (c) real-tree full receipt: exit 0, LANDABLE_ORPHANS 0,
`SWEEP_CORPUS` and `SWEEP_BARE_TOKENS` lines present; (d) v3 bytes and
the r82 receipts unchanged (no rewrite of r82 evidence). KILL RULE: any
condition fails → v4 retained as a rejected candidate in
`reports/round-83/`, the carry-in receipts stay landed (they are the
closure duty, not claim-consequent), and C2 records falsified honestly.

Boundary: v4 moves no criterion score; the moved quantity is the
standing capability's citation-form coverage (the blind spot the carry-in
demonstrated becomes machine-caught inside the instrument). Counts remain
per-revision-corpus (basis lines cited first): this round's receipts
disclose the corpus movements against r82's receipt (fleet-reports 22→23:
`round-82/revenger.md` landed in the fleet root at 13:51, after the r82
receipt at 13:28; lessons 44→46: the r82 receipt ran over the
landing-archive lane extraction, the live worktree carries the two r82
lesson files). Every narrative count cites a `grep -c` of a named-corpus
receipt.

## Frozen sha256 pins

- `reports/round-83/orphan_sweep4.py` =
  `f520f8d69875d1ca83eb8daeddbffecb5f471bf5f5e6aba43bd97029fc2ea701`
- `reports/round-82/ag_probe.py` (frozen r82, unchanged) =
  `22be124b248338ccc7f29fd9096a86c86e0d15b2475073a2f6f026bbe74a08a5`
- fixture bytes (scratch-built, copied unchanged into the landing):
  `corpus/fixtures/app-r83/R83Sample.app/Info.plist` = 313 bytes,
  `1bb04ef837337b2ed0650ef97d86811c03474a82b36738dc346a37aa3169319e`;
  `Base.lproj/MainMenu.nib` = 213 bytes,
  `f0746e35b970492e46d8cfec1fe01f46efd6623e1dad86e74055e1aa7286315e`;
  `Base.lproj/SecondView.nib` = 79 bytes,
  `7953ce251d651a27c002a251ff90c723d7b6493c5c634d9b106f93a246fd3566`
- frozen sed mutant recipe (C2):
  `sed 's/^BARE_TOKEN_CLASSIFICATION = True$/BARE_TOKEN_CLASSIFICATION = False/'`
  applied to `reports/round-83/orphan_sweep4.py` (exactly one
  substitution, verified line 87) — demonstration receipt
  `mutant-kill.log` at adjudication.

## §7 fresh-start gate (r71/r72/r73 rejected closures re-read this round; fresh probes 2026-11-01)

All three closures are K-admission claims whose wave Q-review surface
never settled on this host (r71: Q09/Q16 FAIL at the wave; r72: wave
unconfirmed, no worker outcomes; r73: 34/64 spawned, 0 settled, no vote
files) — a do-nothing control reaches each identically here; K stays
operator-blocked (the r74 L0, re-read unanswered this round). Ruled out
with fresh probes (2026-11-01):

- **F android** (the only unrecorded F4 family): `REA_JADX_MCP_JAR`
  UNSET; no jadx on PATH; `~/tools` = downloads/ + ghidra only — S448
  stands; F4's honest exception stays 10/11.
- **macho/signature F families**: `rea capabilities` →
  `unsupported_host` (native-macho, signature providers) — S453 stands;
  the artifact-graph provider group stays `available: true` on win32.
- **K admissions**: the r74 L0 unanswered (re-read this round) — routed
  around, never treated as answered.
- **criterion C repair**: §9 sizing (the r78–r82 standing disposition).
- **criterion R full extension / criterion N attribution pair**: stay
  routed — not declared; this round's calibration claim is the v4
  bare-token class instead, which the carry-in demonstrated live.
- **A1 `decode_interface_builder`**: AVAILABLE and CLAIMED this round
  (C1) — it is the one route the r82 ruling-out map left open ("a
  separate bounded round"); this is that round.

## Carry-in dispositions (r82 non-author closure; addressed first, before any claim work)

1. **Seven cited receipts uncommitted** — landed FIRST as
   `60693f2ce6b086ea3f0ee84fe27a8f8a13d46f46` (treecommit explicit
   paths, the b1e0c60e receipt-completion class; 7 files, 433
   insertions, all seven byte-verified worktree == landed blob, all
   `git show`-readable); the standing v3 sweep receipted both states:
   pre-landing `LANDABLE_ORPHANS=2` exit 1
   (`.ufo/waves/round-83/sweep-pre-landing.log`) → post-landing 0 exit 0
   (`.ufo/waves/round-83/sweep-post-landing.log`).
2. **The class the carry-in demonstrated** (five of the seven cited
   receipts invisible to the instrument's lane-domain filter because
   they were cited by bare filename) — mined as C2's v4 change 6 above,
   with the reconstruction receipts as the falsifiable red/green.

## Sources opened this round (rows appended inside the Registry after S461 at the landing)

| row | path/command | decision |
|---|---|---|
| S462 | `PYTHONUTF8=1 rea decode-interface-builder --help` + `--schema` + `PYTHONUTF8=1 rea capabilities` (provider `rea-artifact-graph` group, `available: true`), opened 2026-11-01 | ADMIT (tier A, own-work environment) |
| S463 | the installed rea-agents 6.8.0 parser source — `dist/artifacts/apple/NibArchive.js` (+ `appleArchiveFormat.js`, `InterfaceBuilderAnalysis.js`, `application/AppBundleExecutable.js`, `cli-runtime/interfaceBuilderGraph-DKoO7eCM.js`), opened 2026-11-01 | ADMIT (tier A, own-work environment: the lane's own installed tool source, read to derive the fixture layout) |
| S464 | `corpus/live/runs/round-83/` (record, receipt, LEDGER) + `corpus/fixtures/app-r83/` (fixture, generator, truth, oracle), opened 2026-11-01 | ADMIT (tier A, own-work) |
| S465 | this round's carry-in class evidence — `.ufo/waves/round-83/sweep-pre-landing.log` (v3 LANDABLE_ORPHANS=2 over 7 landable receipts) + `v3-prelanding-recon.log`/`v4-prelanding-recon.log` (reconstruction red/green), opened 2026-11-01 | ADMIT (tier A, own-work) |

C1 is sourced by S462 + S463 + S464; C2 is sourced by S465.
