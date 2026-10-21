GRADE: BROKEN — corpus/knowledge/round-62-commonjs-require-name-evidence.md (C04)

Frozen revision d97761952be256d145d298022de03091de91d358 (full; `git rev-parse`).
Candidate file SHA-256 42096e9676d33e25c3b6092e60fbd0fdacd699435ed9dc9db59ce24a1ceaaba3
(working tree and `git archive d977619… | tar -x` copy identical). Claim base
5bd4a90fc1a34caa94496601b60537b3aab12301; pre-registration
a3498e25ad87bf756288812d0ea7c474b09433c7. Scratch:
/fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62FJsSemantics.

## Observation (primary)

1. Public spec reopened read-only, 2026-10-21:
   `curl -sS -L https://tc39.es/ecma262/ -o ecma262.html` -> 7,629,271 B;
   `sha256sum ecma262.html` ->
   `06db92a8331aa452b0d4de8c8938f4b7559b72417769b57d0032002398f27d7f`.
   That is exactly the single-page digest pinned by the entry at :1 and :248.
2. Page identity: `grep -o 'Draft ECMA-262 / October 16, 2026'` ->
   `Draft ECMA-262 / October 16, 2026`; heading
   `14.3.3.3 Runtime Semantics: KeyedBindingInitialization` is present.
3. The quoted step is in §14.3.3.3 and verbatim:
   `Set value to ? GetV(value, propertyName).` It occurs twice in that section
   (BindingElement : BindingPattern Initializer_opt; SingleNameBinding :
   BindingIdentifier Initializer_opt). In the SingleNameBinding production it is
   step 3, after `Let lhs be ? ResolveBinding(name, envRecord).`
4. The entry's case label at :48 is `SingleNameBinding : BindingIdentifier`; the
   page's production is `SingleNameBinding : BindingIdentifier Initializer opt`.
   The quote itself is verbatim from that production; the label omits the optional
   Initializer. Every clause id in the header is real and related:
   §14.3.1.3 = BindingEvaluation; §16.2.1.7 contains Table 54 (ImportEntry Record
   Fields); §16.2.2 = Imports.
5. Word count: `python3 -c` over the quoted string ->
   `compact whitespace tokens: 6`, `spaced whitespace tokens: 10`,
   `lexical words: 6`. The entry at :248 says `"Set value to ? GetV(value,
   propertyName)." — 8 words`. The frozen build note
   `.ufo/waves/round-62/build/R62SourceEcma.md:36` says
   `— 6 words (whitespace split)`.
6. The §Sentence-to-output inventory (:251-282) does not map the §Sources word
   count; the entry's command (`readout.py`, :74-77) reads local fixture and
   saved-record bytes/JSON only, not the ECMA page. The Q11 row at :294 still says
   `pass`.

## Inference

- Quote, clause location, draft date and single-page digest all hold against the
  primary page; the digest match is exact. The quoted step is not a flattened
  grammar alternative mislabeled verbatim: it is verbatim in the actual
  SingleNameBinding production. The only grammar imprecision is the entry's
  shortened production label, which omits `Initializer_opt`.
- The property-read/static-import distinction in item 16 (:48) is correct for the
  quoted text: `GetV(value, propertyName)` reads a property of the destructured
  value; the entry explicitly disclaims an ECMAScript module import, an observed
  export binding, loader/graph-producer/CommonJS runtime behavior and host module
  loading. It imports no Node/Electron/runtime semantics from ECMA.
- Q11 fails on the asserted count at :248. `8` matches neither rendering the entry
  itself gives (6 compact, 10 spaced), contradicts the frozen build note's derived
  `6 words (whitespace split)`, and has no in-entry command/output. The entry's
  Q11 `pass` row is therefore false. This is an actual false value in an asserted
  factual field, not a wording variant.

## Unknown

- Whether the author intended a different counting convention; none is stated.
- The §13.15.5.3/§13.15.5.6 occurrences of the same sentence were only located,
  not audited; the entry cites §14.3.3.3, where the sentence is present.
- No runtime, Node, Electron or loader behavior was observed or claimed.

## Verdict

BROKEN — failed Q11 (entry :248 count `8 words`; derived value 6 whitespace
tokens; no in-entry derivation/output; Q11 pass row :294 false). Secondary
precision: :48 shortens the production to `SingleNameBinding : BindingIdentifier`;
the page's production is `SingleNameBinding : BindingIdentifier Initializer opt`
(the quoted step is still verbatim in it). Minimal correction only: change the
count to the derived 6 with its command/output or an explicit recorded label, and
state the full production form. No repair, no admission, no README/K edits here.

Installs: none.

## Focused rereview — 47511b2 (2026-10-21)

L1 rereview of this C04 entry at revision `47511b213bf556022869fa104a4bda9d7c9a3b95`
(full `git rev-parse`); C04 SHA-256 `d4544c7012a52c0b877022009de6056d6beeda53cd78c2054361e732dce5cafe`
(`git archive 47511b2… | tar -x` -> `sha256sum`; matches requested). Original
report above preserved; this section is the exact-hash rereview only.

- **8-word claim corrected.** §Reproduce :92-98 now carries `printf '%s\n' "Set value to ? GetV(value, propertyName)." | wc -w` -> `6`; the entry's exact multi-line printf form reproduces `6` here. §Sources :299 says "6 whitespace-separated words, counted in §Reproduce"; inventory :327 row S1 maps quote/count to that output; Q11 :349 claims pass.
- **Full production label.** :48 and :299 cite `SingleNameBinding : BindingIdentifier Initializer opt`, matching the page's production; the quote `Set value to ? GetV(value, propertyName).` is verbatim in that production's step 3 (§14.3.3.3, two occurrences).
- **Recorded pins.** :1 and :299 label the draft date, clause anchors and single-page digest `06db92a8…` as recorded from the S029 row, not derived; archived `corpus/SOURCES.md:43` carries the same digest/anchors; the local primary page still hashes to `06db92a8331aa452b0d4de8c8938f4b7559b72417769b57d0032002398f27d7f`.
- **Resolution:** the prior Q11 defect on the S029 quote count is corrected in this revision; no new defect on the assigned points. The original BROKEN finding remains the historical record for d977619. No repair, no admission, no README/K edit. No installs.
