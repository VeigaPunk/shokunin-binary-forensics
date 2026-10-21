GRADE: HOLDS — SOURCES.md row S029 (ECMA-262 object binding / import-name roles) and its round-62 Gate quotes, frozen candidate state.

Frozen identity
- Candidate `d97761952be256d145d298022de03091de91d358` (`git -C <lane> rev-parse HEAD`), extracted by `git archive` to own scratch; claim base `5bd4a90fc1a34caa94496601b60537b3aab12301`; declaration `a3498e25ad87bf756288812d0ea7c474b09433c7`.
- `corpus/SOURCES.md` at the tree: SHA-256 `5c13831b8b64b1a2d715fc4031415750d92af4daf3ef8021c91a8912b5d66bbe`; S029 is line 43. Gate block `corpus/lessons/round-62.md:69-75`, access date `:59`. C04 candidate SHA-256 `42096e9676d33e25c3b6092e60fbd0fdacd699435ed9dc9db59ce24a1ceaaba3`.

Primary evidence (https://tc39.es/ecma262/ reopened read-only, 2026-10-21)
1. `curl -sSL https://tc39.es/ecma262/ -o ecma262.html`: HTTP/2 200, `content-length: 7629271`, `etag: "6ad644cf-7469d7"`. `sha256sum ecma262.html` -> `06db92a8331aa452b0d4de8c8938f4b7559b72417769b57d0032002398f27d7f`, identical to the row's anchor.
2. Version line in those bytes: `Draft ECMA-262 / October 16, 2026`; title `ECMAScript® 2027 Language Specification`. The row's "Draft ECMA-262 October 16 2026" identifies the same line (punctuation dropped only).
3. §14.3.1.3 heading `Runtime Semantics: BindingEvaluation`; rule `LexicalBinding : BindingPattern Initializer`: "Let rhs be ? Evaluation of Initializer.", "Let value be ? GetValue(rhs).", "Return ? BindingInitialization of BindingPattern with arguments value and envRecord." (offsets 3247232-3266445).
4. §8.6.2: `BindingPattern : ObjectBindingPattern` does "Perform ? RequireObjectCoercible(value)." then delegates to `ObjectBindingPattern`, which delegates to `PropertyBindingInitialization` (offset 1685759 ff.).
5. §14.3.3.1 rule `BindingProperty : SingleNameBinding`: "Perform ? KeyedBindingInitialization of SingleNameBinding with arguments value, envRecord, and name." (offset 3277220 ff.).
6. §14.3.3.3 raw at offset 3290287: `Set <var>value</var> to ?\xa0...aoid=GetV...GetV</emu-xref>(<var>value</var>, <var>propertyName</var>).`; normalized "Set value to ? GetV(value, propertyName)." The lesson quote is exact and is SingleNameBinding step 3 (1 name, 2 ResolveBinding, 3 GetV). The same step also occurs in 13.15.5.3/13.15.5.6 (verified headings), so the clause slice is required and correct.
7. Table 54 at offset 4191387, inside §16.2.1.7 (4183255) and before §16.2.1.7.1 (4207447); caption `ImportEntry Record Fields`; `[[ImportName]]` meaning cell: "The name under which the desired binding is exported by the module identified by [[ModuleRequest]]." Exact, 15 words.
8. §16.2.2 heading `Imports`; production `ImportDeclaration : import ImportClause FromClause WithClauseopt ;`; §16.2.2.2 returns ImportEntry Records. Static module syntax only.

Gate conditions
- Q1 6 words, Q2 15 words (whitespace split), both <=25; access date 2026-10-21 stated; row opened this round (base archive 0 lines `^| S029`, frozen tree 1; base-to-candidate diff = 4 added S0 rows, 0 removed/changed).
- No producer-accuracy-from-own-work: S029 cites only the specification; its scope excludes loader, graph-producer and CommonJS runtime behavior; the teaches cell is a language-role statement plus a negative caution, not a saved-record accuracy claim. S030 carries own-work separately.
- README C04/C09 remain `uncovered` at lines 33/38; no held flip.

Observation / inference / unknown
- Observation: all values above were read from the fetched bytes or the archive; no JS/EVM execution, producer/runtime call or service.
- Inference: "read from an evaluated value" follows from 14.3.1.3 (`GetValue` of the evaluated initializer) plus 14.3.3.3 (`GetV(value, propertyName)`); the import-name role is static (Table 54 / 16.2.2). The row stays inside its declared scope. No misstatement found in the row fields or in either Gate quote.
- Nonfatal formatting only: the lesson writes "Draft October16 2026" (missing space); the row omits the page's slash/comma. No criterion is failed.
- Unknown: the page is a living draft; the hash pins today's bytes and `on-release` recheck is the right control. The opener's recorded Last-Modified (16:26:55Z) differs by 2 s from my HEAD (16:26:53Z) with identical ETag/content-length/SHA-256; body identity is unaffected and this is not a row field.
- Adjacent, not a basis for this row's grade (C04's own fresh reviewers own it): C04 `§Sources` line 248 calls the same quote "— 8 words" (whitespace split is 6; opener `R62SourceEcma.md` itself records 6), and its parenthetical "HTML text renders ... GetV ( value , propertyName )" does not match tag-stripped textContent of these bytes (`GetV(value, propertyName)`).

VERDICT: HOLDS for S029 — no actual contradiction or missing requirement; cosmetic formatting only. Usable as the language-role authority for C04 subject to L1's independent decision. No repair and no admission made here. Installs: none.
