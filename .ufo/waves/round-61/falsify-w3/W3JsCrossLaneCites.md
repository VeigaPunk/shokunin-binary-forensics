GRADE: PARTIAL — C04 entry `corpus/knowledge/commonjs-destructured-require-edges.md`, cross-lane contest (Q10) section :79-85 on landed `ab58069`

Method: archive `ab58069` extracted to `/tmp/revenger-r61w3-W3JsCrossLaneCites` (EXTRACT_OK); entry sha256 3382f1b3c56fbffb78f87735f353f5737b24e3ae102542cf98d3271946bc5629. Kaidoku read-only at HEAD `fe10219ec6e92c32b7eb40d83fbcac888756c6c1` (2026-10-21 13:04 -0300), worktree clean for the three cited files (`git diff --stat` empty).

HOLDS — citation 1 (README row). Entry :81-82 says "Kaidoku holds the Electron/ASAR/JavaScript row (`kaidoku-shokunin/corpus/README.md:23`)".
Command: `awk -F'|' 'NR==23{print $2,$3,$NF}' kaidoku-shokunin/corpus/README.md`
Line 23 is `| Electron/ASAR/JS | 2026-10-13-asar-surface, 2026-10-13-r2-asar-deep-obsidian, 2026-10-13-r3-renderer-asar, … |` and its status cell is `held` ("obsidian app.asar (launcher) + obsidian.asar (real app: 45 ipcMain ops); N-API taxonomy; .jsc bytecode loader identified"). Attribution exact.

HOLDS — citation 2 (entrypoint). Entry :82-83 says "an unresolved package `main` on a real ASAR (`…/2026-10-13-r3-renderer-asar.md:79-81`)".
Command: `awk 'NR>=79&&NR<=85' corpus/knowledge/2026-10-13-r3-renderer-asar.md`
:79 `## Candidate: Entrypoint topology — package.json:main → index.js NOT-FOUND; preload specifier metadata unresolved-external; 3 HTML renderer entrypoints`; :81 "records package.json declaring `"main": "index.js"` → `resolution_status: "not-found"`". The range brackets the claim. No erratum touches it: errata at :109-121 cover only the `grep -c` recipe, the count 29, and inspect≡analyze. Attribution exact; kaidoku's line is a real ASAR (25,787,463 B obsidian.asar, :89 run log #1).

HOLDS — duplicate-ground scan (assigned question). No kaidoku CommonJS destructured-require ground exists.
`grep -rn 'destructur\|destructured\|imported_name\|named-import\|named import' kaidoku-shokunin/corpus/` → one hit, `corpus/knowledge/2026-10-13-r5-02-call-targets-jq.md:107` "N targets == N named imports" (ELF call targets, not JavaScript). `grep -rnE '\{[^}]{0,60}\} *= *require'` over the repo → no corpus hit; the only whole-repo match is wave scratch `.ufo/waves/arc3-loop1-round6/claims/c2/EX-8/scripts/keccak-selectors.js:5`, not a knowledge claim. The entry's core claim (destructured-require named-import edges, 3→2 delta) is not a duplicate.

HOLDS — evidence not overstated. Entry `## Reproduce` block extracted verbatim and run from the archive root (53 lines, `python3 -B`, exit 0): output is byte-identical to `## Provenance`, incl. `v1 imports=3 named=['checksum','rot13']`, `v2 imports=2 named=['rot13']`, `delta named removed=['checksum']`, record shas `7c3ba8c1…`/`331ec252…`, evidence ids `ev_4a93276c…`/`ev_66f5dc7e…`. No fixture or saved record changed at `ab58069`; the harm condition "a changed saved record or fixture" is not met.

HOLDS — admission inputs. S020-S027 rows: `opened=2026-10-21`, tiers A/A/A/A for S020-S023 and A for S027 (`mined`, `used-by corpus/knowledge/commonjs-destructured-require-edges.md`), so the "≥1 round-61-opened tier-A source" conjunct is met (corpus/SOURCES.md:34-37,41). K_HELD=6 by the claims.md regex `grep -cE '^\| C[0-9]+ .*\| held \|$' corpus/README.md`; C04 row (:30) carries the entry and status `held`.

PARTIAL — unreported adjacent cross-lane ground (Q10, QUALITY.md:22 "Cross-lane contested scope is reported, not absorbed"). Kaidoku's held JS row already covers authored synthetic CommonJS fixture graphs and the same `module.exports` export-binding fact the entry observes:
- `kaidoku-shokunin/corpus/knowledge/2026-10-13-r4-09-js-export-compare.md:59` — `/tmp/mini-a`/`/tmp/mini-b` = "two 4-line CJS apps", analyses `ev_6e6e173b…`/`ev_f36db5b9…`.
- same file :65 — "`module.exports = {config, tags}` yields `default` binding only, NO return shapes".
Entry :37-40 states the same family fact for its fixtures ("a single exposed export named `default`, not the `module.exports` keys"); `corpus/fixtures/js-r3/transform.js:12` is `module.exports = { rot13, checksum };`. Entry :84-85 narrows the contest to "its own ground is the destructured-require edge on authored CommonJS directories" and cites only the ASAR row; it never reports kaidoku's authored-CJS-fixture ground or the shared `default`-only binding. Q10's listed failure mode ("one family's observation is stated as a universal") is not triggered and the core edge claim is not absorbed, so this is a reporting gap, not a Q10 failure.

PARTIAL — exact line, exclusion ambiguity. Entry :4 `coverage-map: C04 (CommonJS destructured \`require\` only; no Electron, ASAR, ESM, bundler or \`exports\` ground)` vs :37-40 and :61 ("Export-side correspondence") which do carry export-side observations. Readable as "no `exports` *field* ground" (defensible; S021's field is only in Unknown); as written it is over-broad against the entry body.

Note (scope, not graded): entry pins no kaidoku commit, so the two citations are line-stable only against today's HEAD (kaidoku README last commit `2b40aec`, 2026-10-21 11:56 -0300; renderer file `999ce12`, 2026-10-13).

VERDICT: PARTIAL — both cited kaidoku statements are verbatim accurate and the destructured-require ground is not duplicated, but the Q10 section omits kaidoku's authored-CJS/`default`-binding ground (`2026-10-13-r4-09-js-export-compare.md:59,65`) and the :4 exclusion reads over-broad against :37-40/:61.
Installs: none.
