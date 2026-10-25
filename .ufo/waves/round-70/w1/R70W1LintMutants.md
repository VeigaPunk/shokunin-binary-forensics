GAPS — the lint flagged every assigned probe its docstring model covers (self-test OK; 7-missing and blank-decision §Q-map flagged; all five introducers flag non-resolving ids; the historical M47 one-count shape flagged), but six undeclared classes slip through, and on the actual v5 candidate bytes `LINT_Q14=0`/`LINT_Q15=0` are vacuous because the entry quotes no hex run in prose.

Seat R70W1LintMutants · round-70 wave 1 (advisory, pre-gate) · 2026-10-25.
Target attacked: `corpus/lint_entry.py` sha256 `43364943a357cc7961d16ced9a029859d07cf3cedb293c5782bef4d6b4704724` (identical before and after all work — restoration evidence §7). Scratch: `/tmp/revenger-r70-R70W1LintMutants` (deleted before return; all mutations were scratch fixtures). No lane file written or edited. No tools installed (pacman paused host-wide; python3 stdlib only). No subagents dispatched.

## 1. Baseline

- `python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/lint_entry.py --self-test` →
  `SELFTEST OK: clean 0; four planted defects each scored exactly their class; truncated-run-with-count flagged`, exit 0.
- Candidate bytes extracted read-only: `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin show aa1842fac199aa524930e5565ed3715de5f84c6d:corpus/knowledge/round-70-apk-axml-byte-evidence.md` → 273 lines, sha256 `0913f6515e93889a7a4204a613f52a3ff8d505742038dfa0d46443a79b088368`.
- Lint on the candidate: `LINT_QMAP=0 / LINT_Q14=0 / LINT_Q15=0 / LINT_HEADER=0`, exit 0.
- The scratch copy of the lint hashes identical to the lane bytes; a lane-script cross-check on probe_a reproduced the scratch run's output byte-for-byte (`LINT_Q14=2 [9, 11]`).

## 2. Probe (a) — Q14 historical classes (`probe_a.md`, one sentence per line; lint printed `LINT_Q14=2 [9, 11]`, exit 1)

| ln | sentence (probe_a.md) | expected | observed |
|---|---|---|---|
| 9 | The 16-byte prefix is `` `4d616e69666573742d` ``. — the historical M47 shape (round-68.md:97,103: one count, wrong) | flag | **FLAGGED** |
| 10 | The run `` `4d616e69666573742d` `` is 9 bytes, a 16-byte prefix. | flag (same defect class) | **SLIPS** — two counts in one clause |
| 11 | The run `` `4d616e69666573742d…` `` (9 bytes) continues past the fence. | flag | **FLAGGED** |
| 12 | The run `` `4d616e69666573742d` ``… (9 bytes) continues past the fence. | flag | **SLIPS** — ellipsis outside the backticks |
| 13 | The run `` `4d616e69666573742d...` `` (9 bytes) continues past the fence. | flag | **SLIPS** — ASCII dots make the run invisible |
| 14 | The bytes `` `4d616e69666573742d` `` decode to ASCII `` `ManifestX` `` (9 bytes). | flag (Q14 decode clause) | **SLIPS** — the lint never decodes |
| 15 | … decode to ASCII `` `Manifest-` `` (9 bytes). (control, correct decode) | pass | pass |
| 16 | The run `` `4D616E69666573742D` `` (9 bytes) starts the file. | flag | **SLIPS** — uppercase hex invisible |
| 17 | The truncated tail is `` `<120 hex>…` `` (64 bytes). | flag (docstring: ellipsis-terminated carries no count) | **SLIPS** — count > 32 short-circuits first |
| 18 | The prefix `` `4d616e69666573742d` `` is 9 bytes. (control) | pass | pass |
| 19 | The blob `` `a1b2c3d4e5…e5` `` (40 hex) is 20 bytes. | slip (declared: digest lengths) | SLIPS (declared) |
| 20 | Runs `` `4d61` `` and `` `6e69` `` (2 bytes) follow. | slip (declared: exactly one run) | SLIPS (declared) |

(`LINT_QMAP=15` on this fixture is the expected over-flag for a fixture with no §Q-map; it does not affect Q14 attribution.)

## 3. Probe (b) — §Q-map

- **b1, 7 criteria missing** (rows Q01–Q08 only): `LINT_QMAP=7 ['Q09', 'Q10', 'Q11', 'Q12', 'Q13', 'Q14', 'Q15']`, exit 1 — exactly the 7 missing criteria, flagged.
- **b2, blank decision** (all 15 rows, Q07 decision cell empty): `LINT_QMAP=1 ['Q07']`, exit 1 — flagged.
- **b3, decision column reordered** (`| criterion | basis | decision |`, all 15 decision cells blank): `LINT_QMAP=0`, exit 0 — **SLIPS**. The lint hardcodes the second cell as the decision (`lint_entry.py:57-58`) and never reads the header row, so a map with every actual decision blank scores clean.
- **b4, duplicate §Q-map** (complete 15-row map, then a second `## §Q-map` carrying only Q01): `LINT_QMAP=0`, exit 0 — **SLIPS**. Only the first `## §Q-map` section is read (`lint_entry.py:54`, `re.search`).

## 4. Probe (c) — Q15 (`probe_c.md`; lint printed `LINT_Q15=6`, exit 1)

- **FLAGGED** (non-resolving under the lint's own `git cat-file -e <h>^{commit}`): findings `[(9, 'deadbee1'), (10, 'deadbee2'), (11, 'deadbee3'), (12, 'deadbee4'), (13, 'deadbee5'), (14, '1234567890abcdef1234567890abcdef12345678')]` — i.e. after `at` (ln 9), `base` (10), `tip` (11), `since` (12), `commit` (13, 7-hex) and `commit` (14, 40-hex). All five declared introducers fire.
- Control: ln 15 `Commit `aa1842f`` (resolves in the lane) → not flagged. Correct.
- **SLIPS after words the lint does not know** (ln 16–23, zero findings): `Revision` / `Sha` / `Hash` / `Object` / `Snapshot` / `Pinned` / `Tree` / `As of` each followed by a non-resolving `` `deadbeeN` ``. Declared scope — the docstring (`lint_entry.py:17-18`) enumerates exactly the five introducers — reported as assigned.
- Also slipping: uppercase `` `DEADBEEF` `` (ln 24, undeclared); unbackticked `Commit deadbee9` (ln 25, declared: "backticked"); `…`-truncated citation `Commit `deadbee0`…` (ln 26, the `(?!…)` lookahead at `lint_entry.py:83`); keyword and token on different lines (ln 27–28, per-line scan at `:84`).

## 5. Gap list (each: class · slipping sentence · located defect · declared?)

- **G1 (Q14, undeclared, highest):** ASCII rendering that does not decode from its run. `lint_entry.py:69` matches only `[0-9a-f]` runs; no `bytes.fromhex`/decode exists anywhere in the script. Slips: probe_a:14 "The bytes `4d616e69666573742d` decode to ASCII `ManifestX` (9 bytes)." QUALITY.md Q14 explicitly requires "an `ASCII `…`` rendering decodes from that same run"; the lint's docstring (`:14-16`) omits this clause entirely.
- **G2 (Q14, undeclared):** truncation renderings other than `…`-inside-backticks. `…` outside the backticks (probe_a:12) leaves the run length-consistent so the count check passes; ASCII `...` inside the backticks (probe_a:13) makes the run invisible outright (`:69` requires hex immediately followed by optional `…` then the closing backtick). The docstring (`:16`) says "an ellipsis-terminated H must carry no count" with no rendering qualifier, and the self-test exercises only the `…`-inside form.
- **G3 (Q14, doc-vs-code):** ellipsis-terminated run with a count > 32 bytes. `lint_entry.py:72` (`int(counts[0]) > 32: continue`) runs before the ellipsis check at `:75`, so probe_a:17 (120-hex + `…` + "(64 bytes)") slips although docstring `:16` states the rule unqualified.
- **G4 (Q14, model boundary):** a clause carrying two counts slips even when one is the historical defect: probe_a:10 "The run `4d616e69666573742d` is 9 bytes, a 16-byte prefix." (`:72` requires `len(counts) != 1 → skip`). The minimal historical M47 shape (one count) IS flagged (probe_a:9), but the same defect with the true count also present is not.
- **G5 (Q14+Q15, undeclared):** uppercase hex is invisible (`[0-9a-f]` at `:69` and `:83`): probe_a:16 and probe_c:24 both slip.
- **G6 (QMAP, undeclared assumption):** the decision cell is hardcoded as column 2 (`:57-58`); the header row is never read. probe_b3 (all 15 real decisions blank, decision in column 3) exits 0.
- **G7 (QMAP, undeclared):** only the first `## §Q-map` section is read (`:54`). probe_b4 (complete map + incomplete duplicate) exits 0.
- **G8 (Q15, declared):** introducer whitelist `commit|base|tip|since|at` (`:83`); the eight unknown-word sentences of probe_c:16-23 slip. Within stated scope.
- **G9 (Q15, declared):** unbackticked ids, `…`-truncated citations and cross-line keyword/token pairs slip (`:83-84`). Within stated scope.
- **G10 (Q14, declared, minor doc-code divergence):** digest-length exclusions — code excludes `(40, 64, 128)` (`:70`) while docstring `:64` says "(40, 64)"; probe_a:19 (40-hex + "20 bytes") slips as declared.

## 6. Candidate advisories (wave-1 advisory only; not kill-rule inputs)

- **O1 — the candidate's Q14/Q15 lint green is vacuous.** The 273-line candidate contains **zero** backticked hex tokens (`grep -nE '\x60[0-9a-f]{4,}\x60' candidate.md` → no hits), so `LINT_Q14=0`/`LINT_Q15=0` on it (§1) reflect an empty surface, not verified evidence. Its only prose length claim — candidate.md:50 "a 32-hex-character run, which is 16 bytes" — describes the run without quoting it, so the lint has no run to measure; I verified the claim true by hand (`payload_first16_hex` `4d616e69666573742d56657273696f6e` = 32 hex = 16 bytes, decodes to `Manifest-Version`), but the pre-flight could not have caught a wrong count there. The §Q-map Q14 row (candidate.md:262) cites exactly this statement as the entry's Q14 evidence.
- **O2 — claims.md vs candidate bytes disagree about the Q15 repair.** reports/round-70/claims.md (C1 claim paragraph) describes v5 as carrying "the `c7b7cf98` identity derived and a Q15 row", but the aa1842f bytes contain no `c7b7cf98` (grep → 0 hits) and the Q15 row reads "this entry states no git object id; identity statements are file digests printed by item 14" (candidate.md:263). Either the claims description is stale or the repair was dropped in the build — reconcile before wave 2.
- **O3 — the QMAP green on the candidate is substantive:** all 15 QUALITY.md rows present with non-empty decision cells (candidate.md:249-263 region; `LINT_QMAP=0`).

Calibration/operability summary: the lint is exact on every assigned probe inside its declared model (self-test clean; per-class counts exact; exit contract 0/1 observed as documented, runs in milliseconds), and it catches the historical M47 shape and the `…`-inside truncation shape. The gaps are the six undeclared classes above plus the vacuous-green risk (O1) on entries that keep hex out of prose — which the v5 candidate currently does.

## 7. Restoration evidence

- `corpus/lint_entry.py` sha256 before == after == `43364943a357cc7961d16ced9a029859d07cf3cedb293c5782bef4d6b4704724`; `corpus/QUALITY.md` `a924d1fbfc462c9d465f9f44abc36f3312462416cfa221a484a1d1c5e35f8632` unchanged.
- No lane file was written, edited, committed or pushed; every mutation lived in `/tmp/revenger-r70-R70W1LintMutants` (probe fixtures + read-only candidate extraction), deleted before return. No git state was mutated anywhere (only `git show` reads and the lint's internal `git cat-file -e` probes).
