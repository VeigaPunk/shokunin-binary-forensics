# Independent LEAF review — round 7

## Source truth and saved Evidence

- Authored `js-r3/index.js:1` destructures `rot13, checksum` from `./transform`; `js-r7-v2/index.js:1` destructures only `rot13`. The render return also changes (checksum formatting removed), so the changed file is **not** a one-edit/one-cause fixture, although exactly one *named-import relationship* changes. `package.json` (`main: index.js`) and `transform.js` are byte-identical across versions. The sources were read, not executed.
- Baseline analysis `ev_4a93276c886da96f0b37c490e395dc0761ac32225dd7297c600a51ce100c1c7e` includes two resolved, inferred named-import graph edges (`rot13`, `checksum`), and v2 analysis `ev_66f5dc7e3e8a8d6033c17c400762521d815d77c5ac9a9c7e1b6a45232cd7987c` includes only `rot13`. Both include a resolved static `package.json:main` / `index.js` mapping. This is a **manual difference between per-version graphs**, not a version-comparison finding. Source also leaves `transform.js` exporting `checksum`; removed *import* must not be called a removed export or function.
- Comparison `ev_5e4b17c1db1a06126558586f188b8eae81117c4d4bdf43d2278aefcd945f1a78` reports one changed `index.js` asset (`content`, `properties`; `semantic-key`, **medium** confidence), unchanged package and electron-main nodes (`exact-node-identity`), and unchanged `transform.js` asset (`exact-content-digest`). It marks five module nodes removed and five added, all **unmatched**, rather than reliably pairing corresponding module identities. Its `items[]` do **not** report a relationship-level deletion naming `checksum`. Its combined graph retains edges including `checksum` on the left and `rot13` on both sides, but reading that graph against the two parent records is analyst-side inference, not an explicit changed-relationship item. `summary.unknown: 0` does not cure unmatched module pairing.

## Precision / recall and guardrails

The declared comparison-tool detection target is the single removed named import: **recall 0/1** from `items[]`; named-import precision **N/A** because no named-import delta is asserted. The manually compared parent graphs recover 1/1 bounded source-truth import delta but cannot be credited to `compare_application_versions`. At the coarse asset/package level, changed `index.js`, unchanged package/main-role and byte-identical `transform.js` align with truth; these are a different scoring unit. Stable `rot13` and stable package-main mapping are warranted as **source-backed, static per-version observations** (with matching parent graph edges); the comparison directly supports unchanged package and entrypoint role, but not a dedicated unchanged-`rot13` relationship verdict. Neither static record proves actual import execution, Electron launch or render output. The comparison's `complete-within-inputs` applies to non-omitted input application graphs, not complete semantic coverage or successful cross-version pairing; parent semantic coverage is `unknown`.

## Per-axis recommendation

- **Calibration: unchanged on the declared axis move / do not admit round 7.** The comparison does not explicitly identify `checksum` removal, despite correctly reporting broader changed asset and stable package. Preserving this failed detection and honest scope is useful telemetry, not fulfillment of the stated after condition.
- **Depth: unchanged.** Parent-level static import difference is a bounded corroboration, not a new comparison-tool semantic finding or observed behavior.
- **Coverage: unchanged.** No new route or provider capability demonstrated; native round-1 provider failure remains outside this review.

This review used only saved evidence and fixture text. No REA rerun, target execution or installation was performed.
