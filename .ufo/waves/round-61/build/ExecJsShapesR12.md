# ExecJsShapesR12 — round 61, C04 read of shapes-r12 (RUNS, read-only)

Seat CloseChousa26.ExecJsShapesR12-10 · base e0a4b0c4348ef1fade46539f520e94fa140c4d8a (observed `git rev-parse HEAD` in clone) · clone /tmp/revenger-r61-ExecJsShapesR12 (branch r61-ExecJsShapesR12) · scratch /tmp/revenger-r61-ExecJsShapesR12-scratch · lane not written. Web access date 2026-10-21.

## 1. Saved records the verifier binds (verify_shape_evidence.py:11-19; verifier sha256 eed7725a…, 124 lines)
- corpus/live/runs/round-12/v1-direct-analysis.json — sha256 0986a0af… — pin ev_2a492f5d… (:16). Not reproduced by 3 canonical-JSON candidates.
- corpus/live/runs/round-12/v2-direct-analysis.json — sha256 3d657eff… — pin ev_913f14fa… (:17). Not reproduced.
- corpus/live/runs/round-12/comparison-direct.json — sha256 48143dec… — pin ev_bb7e1c30… (:18). Reproduced as sha256(sorted-key compact JSON of record minus evidence_id).
- Clone and lane hashes identical (sha256sum).
- Retained, not bound: v1-analysis.json (ev_b71e7b75…; exposes-edge artifact sha 2a698b56… ≠ current df0badbf…; stale initial `module.exports = {describe}` revision, LEDGER.md:4); comparison.json (ev_31a28f22…, partial); comparison-default.json (ev_46bff65e…, partial, both sides unavailable).
- Direct records: raw_result null; subject.local_path = /home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/fixtures/shapes-r12/{v1,v2}. That path exists on this host; its index.js bytes equal the lane's.

## 2. Fixture facts derived from bytes (acorn 8.19.0 parse only; fixture not executed)
| side | index.js bytes, sha256 | return line:col | fields | callable | `module.exports` stmt | require/import | Electron tokens |
|---|---|---|---|---|---|---|---|
| v1 | 110, df0badbf… | 2:2–2:58 | kind:"fixture", retained:1, removed:"old" | callable:function:0:82 | 4:0–4:25 | 0 / 0 | 0 |
| v2 | 108, 0357ec38… | 2:2–2:56 | kind:"fixture", retained:1, added:"new" | callable:function:0:80 | 4:0–4:25 | 0 / 0 | 0 |
- package.json (v1 = v2, 88 B, sha256 3f3521c6…): main "index.js", type "commonjs"; main target exists.
- `grep -rn 'require\|import\|main' corpus/fixtures/shapes-r12` → hits only the two package.json lines.
- Record vs bytes, all match: callable_id, return ranges, field values, exposes edge 4:0–4:25, contains edge end 5:0, artifact sha on exposes edge, electron-main props (declared/resolved index.js; mechanism package.json:main), comparison removed={removed}, added={added}, stable={kind,retained}, summary 1/1/0/0.

## 3. Verifier run
- clone `corpus/`: `python3 verify_shape_evidence.py --self-test` → `POSITIVE ev_bb7e1c30… saved REA static shape evidence: 2/2 presence deltas; 2/2 stable names; no runtime claim` / `NEGATIVE REJECTED changed-property evidence mismatch`; exit 0.
- Line 105 returns that summary as a literal string, so "2/2" is not computed. Self-test mutates one field only (:113-114).

## 4. Falsifiers (corpus copies in scratch, same command; exit and last stderr line)
| mutant | exit | stderr | shows |
|---|---|---|---|
| M0 unmodified | 0 | — | control |
| Ma fixture package.json main index.js→lib.js | 0 | — | package.json unbound |
| Mb saved electron-main props → lib.js, mechanism none | 0 | — | main-mapping record unbound |
| Mc saved comparison left_source_range start line 2→9 | 0 | — | source ranges unbound |
| Mf saved v1 callable_id → callable:function:0:999 | 0 | — | callable_id unbound |
| Md fixture v1 index.js retained 1→2 (same length) | 1 | ValueError: v1: parent artifact identity | index.js bytes bound |
| Me saved v1 /removed value old→new | 1 | ValueError: v1: source mismatch | return fields bound |
- grep of the verifier for edges|package|main|exposes|loads|maps_to|export-binding|callable|source_range|electron → no hit except its own `require(` assertion helper.

## 5. Facet scope against C04 (claims.md:27-28)
| facet | in bytes / record | verifier binds | C04 verdict |
|---|---|---|---|
| package main → index.js (electron-main node; loads and maps_to edges) | yes / yes | NO (Ma, Mb) | IS the claimed main-mapping facet. Admissible only as recorded static inference with its own recheck. "electron-main" is REA's kind label, not Electron evidence (0 tokens). |
| CommonJS destructured require / named-import edges | NO: 0 require calls, 0 import nodes | — | NOT in shapes-r12; no basis here |
| `module.exports = describe` default export (exposes edge) | yes / yes | NO | adjacent CommonJS export edge; outside the named-import wording unless L1 re-scopes |
| return-object fields, presence deltas, stable names, "2/2" | yes / yes | YES (Md, Me) | EXCEEDS C04: separate capability; one fixture pair, one literal return site. 2/2 = two authored deltas, not accuracy. |
| callable_id, source ranges | yes / yes | NO (Mc, Mf) | supporting detail; state as recorded |
| subject.digest (a54bf1ff… v1; a1aa283e… v2) | recorded | NO | derivation unknown |
| top-level authority `shipped-artifact` | recorded | — | overstated for a lane-authored synthetic fixture (Q10) |

## 6. Blockers and sources
- LEDGER.md:16 check (`Path('.shokunin/revenger/corpus/live/runs/round-12/comparison-direct.json')`) → `FileNotFoundError` from clone root; lane has no `.shokunin`. Not a valid recheck; the verifier is.
- SOURCES.md registry S001–S015 (:15-29): no Node.js, CommonJS, npm or Electron row. C04 has zero tier-A rows (Q01 blocker).
- Opened 2026-10-21: https://nodejs.org/api/packages.html#main, "Modules: Packages | Node.js v26.12.1 Documentation", section "main" (Added in: v0.4.0; page markdown lines 1122-1127; code spans unformatted):
  - "The "main" field defines the entry point of a package when imported by name via a node_modules lookup. Its value is a path." (23 words)
  - "The "exports" field, if it exists, takes precedence over the "main" field when importing the package by name." (18 words)
  - "It also defines the script that is used when the package directory is loaded via require()." (16 words)
  Scope: Node.js only. No Electron source opened.

## 7. Falsifiers a C04 entry needs (none exists)
- Recheck recomputing `main` from package.json bytes and matching the saved electron-main / maps_to edges (Ma and Mb pass today, so they are not caught).
- Recheck binding exposes edge, callable_id and source ranges (Mc and Mf pass today).

## Installs and writes
- Installed: acorn 8.19.0 from the npm registry into /tmp/revenger-r61-ExecJsShapesR12-scratch (scratch-local, not -g); reason: independent AST derivation. Already present and unchanged: node v24.21.0, npm 11.19.0, uv. No pacman, no global install.
- Writes: /tmp clone (read only), /tmp scratch (corpus copies, mutants, node_modules), and this report in the lane.

VERDICT: shapes-r12 supports only the package-main mapping (unbound by the verifier) and an adjacent CommonJS export edge; the destructured-require facet is absent; return-shape comparison exceeds C04; no C04 entry is admissible on this fixture alone.
