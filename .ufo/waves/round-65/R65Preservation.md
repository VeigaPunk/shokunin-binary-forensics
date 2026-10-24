PASS — protected-path diff is empty; all 10 pre-existing verifier self-tests retain baseline exit code 0.

## Scope

- File changed: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-65/R65Preservation.md` only.
- Behavior: read-only preservation check; no production files changed.
- Blockers: none. Risks: none observed within this check.

## Protected-path diff

Command:

```text
git -C /home/vgpnk/Projects/shokunin/revenger-shokunin diff --numstat 3eebcdd7ee7eb130b730a17fde1a0e40786c0f2f -- corpus/live corpus/fixtures/firmware-r63 corpus/fixtures/archive-r2
```

Actual output: empty (no numstat rows); command exit `0`.

## Verifier self-tests

The base tree contains the same 10 verifier paths listed below (`git ls-tree -r --name-only 3eebcdd7ee7eb130b730a17fde1a0e40786c0f2f -- corpus` listed them). Current invocation was `python3 -B <absolute verifier path> --self-test`; baseline source was fetched per path with `git show 3eebcdd7ee7eb130b730a17fde1a0e40786c0f2f:corpus/<filename>` and executed with `__file__` set to the absolute current verifier path. Every BASE and CURRENT invocation exited `0` (the original code was 0 for each). Each pair emitted the same output shown:

- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/verify_evm_evidence.py` — BASE `0`, CURRENT `0`:
  `POSITIVE ev_0ad0097eb137ff9196b29ac3fb6109d8f72ee0761e2655fa1fca594295cf6f42 1/1 selector candidate and two digests; destination 16 != PUSH4 6; inferred only`
  `NEGATIVE REJECTED candidate destination mismatch`
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/verify_icon_languages.py` — BASE `0`, CURRENT `0`:
  `PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED`
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/verify_icon_states.py` — BASE `0`, CURRENT `0`:
  `PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED`
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/verify_js_graph_delta.py` — BASE `0`, CURRENT `0`:
  `POSITIVE saved parent graphs: removed checksum 1/1; stable rot13 and package-main; static inference only`
  `NEGATIVE REJECTED saved graph disagrees with source truth`
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/verify_multi_icon_states.py` — BASE `0`, CURRENT `0`:
  `PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED`
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/verify_named_multi_icon_states.py` — BASE `0`, CURRENT `0`:
  `PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.`
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/verify_pe_resources.py` — BASE `0`, CURRENT `0`:
  `POSITIVE ev_a524338e43a8a20a3fb0f018d46ef2fe06732e323bfb3ce98fd813bd223f50ef 1/1 RT_RCDATA name 1 language 1033 maps to authored payload`
  `NEGATIVE REJECTED payload relation mismatch`
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/verify_saved_evidence.py` — BASE `0`, CURRENT `0`:
  `POSITIVE ev_cc681c2a03da4e9901275c1425fb1f726cca78bbdbec3defb13b6a0ac8ad156b ZIP root + 2 members: 3/3 identity units; formats, sizes, hashes, edges and fixture bytes match`
  `POSITIVE ev_4a93276c886da96f0b37c490e395dc0761ac32225dd7297c600a51ce100c1c7e JS 2 imports + package main: 3/3 static inferred relationships match source/export and artifact digests`
  `NEGATIVE ZIP REJECTED: ZIP: wrong root size/format`
  `NEGATIVE JS REJECTED: JS: wrong package-main mapping`
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/verify_semantic_trace.py` — BASE `0`, CURRENT `0`:
  `POSITIVE ev_53329396d6fe4843b89806ef1ed98b6db8358ec91c41c733d617ea846b995a8a 3/3 returned captures match source tokens and saved parent; partial static trace only`
  `NEGATIVE REJECTED relation differs from source parent`
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/verify_shape_evidence.py` — BASE `0`, CURRENT `0`:
  `POSITIVE ev_bb7e1c308a60b0cc45919a4a441347a0b6119df2c49f0de40c737615f94cb872 saved REA static shape evidence: 2/2 presence deltas; 2/2 stable names; no runtime claim`
  `NEGATIVE REJECTED changed-property evidence mismatch`

Relevant self-test/main entry points are at `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/verify_evm_evidence.py:77`, `verify_icon_languages.py:177`, `verify_icon_states.py:180`, `verify_js_graph_delta.py:82`, `verify_multi_icon_states.py:177`, `verify_named_multi_icon_states.py:106`, `verify_pe_resources.py:71`, `verify_saved_evidence.py:146`, `verify_semantic_trace.py:100`, and `verify_shape_evidence.py:123`.
