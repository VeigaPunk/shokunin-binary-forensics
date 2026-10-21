# SrcEcmaDestructuring — r61 C04 (JavaScript) source opening, read-only

Seat `CloseChousa26.SrcEcmaDestructuring-10`, 2026-10-21. No clone, no producer call, no install. Scope: ECMA-262 only (Node pages belong to sibling `ScribeSourcesRowsJs`). Question: does the language spec ground that `const {a, b} = require('./x')` destructures a returned object at run time and is not an import declaration?

## Exact URLs opened (HTTP result, revision evidence)

- `https://tc39.es/ecma262/` — HTTP/2 200, 7,629,271 B; `last-modified: Mon, 19 Oct 2026 16:26:53 GMT`; `etag: "6ad644cd-7469d7"`. Version block: h1 `Draft ECMA-262 / October 16, 2026`, title `ECMAScript® 2027 Language Specification`. No 40-hex revision is printed (`grep -oE '[0-9a-f]{40}' front.html` -> empty); revision evidence is Last-Modified+ETag.
- `https://tc39.es/ecma262/multipage/ecmascript-language-statements-and-declarations.html` — 200, 956,160 B, LM same day 16:26:52 GMT (mirror used for readable clause text); `.../syntax-directed-operations.html` — 200, 1,198,511 B; `.../ecmascript-language-scripts-and-modules.html` — 200, 1,033,596 B.
- Access date 2026-10-21. Each quote matched by exact string on the single page and the mirror (tags stripped, NBSP->space, whitespace collapsed); nothing is quoted from memory or a search snippet.

## Section anchors

`#sec-bindingevaluation` (14.3.1.3 RS: BindingEvaluation); `#sec-destructuring-binding-patterns` (14.3.3); `#sec-destructuring-binding-patterns-runtime-semantics-propertybindinginitialization` (14.3.3.1); `#sec-runtime-semantics-keyedbindinginitialization` (14.3.3.3); `#sec-runtime-semantics-bindinginitialization` (8.6.2); `#sec-variable-statement-runtime-semantics-evaluation` (14.3.2.1); `#sec-scripts` (16.1); `#sec-modules` (16.2); `#sec-imports` (16.2.2). All exist on the single page (`grep 'id=<anchor>'` -> present).

## Verbatim quotes (3, each <=25 words)

Q1 — 14.3.1.3, production `LexicalBinding : BindingPattern Initializer`, step 2 (7 words): "Let rhs be ? Evaluation of Initializer."
Q2 — same production, step 5 (10 words): "Return ? BindingInitialization of BindingPattern with arguments value and envRecord."
Q3 — 14.3.3.3, production `SingleNameBinding : BindingIdentifier Initializeropt`, step 3 (6 words): "Set value to ? GetV(value, propertyName)."

## Structural observations (rendered clause text; not counted above)

- O: 14.3.1.3 ordered list: 1 `Assert: kind is normal.` 2 `Let rhs be ? Evaluation of Initializer.` 3 `Let value be ? GetValue(rhs).` 4 `Let envRecord be the running execution context's LexicalEnvironment.` 5 `Return ? BindingInitialization of BindingPattern with arguments value and envRecord.` So the initializer (the `require(...)` call) is evaluated to a value before any binding.
- O: 8.6.2 `BindingPattern : ObjectBindingPattern` -> `Perform ? RequireObjectCoercible(value).` + `Return ? BindingInitialization of ObjectBindingPattern with arguments value and envRecord.`; `ObjectBindingPattern : { BindingPropertyList ,opt }` -> `Perform ? PropertyBindingInitialization of BindingPropertyList with arguments value and envRecord.`
- O: 14.3.3.1 `BindingProperty : SingleNameBinding` -> `Let name be the sole element of the BoundNames of SingleNameBinding.` + `Perform ? KeyedBindingInitialization of SingleNameBinding with arguments value, envRecord, and name.`; renamed form `BindingProperty : PropertyName : BindingElement` -> `Let propertyKey be ? Evaluation of PropertyName.` Hence shorthand key = local name; `{a: b}` reads property `a`, binds `b`.
- O: 7.3.3 `#sec-getv`: `Let obj be ? ToObject(value).Return ? obj.[[Get]](propertyKey, value).`; 10.1.8.1 `#sec-ordinaryget` falls through to `obj.[[GetPrototypeOf]]()` / `parent.[[Get]](propertyKey, receiver)` when the own descriptor is undefined.
- O: 16.2 `ModuleItem : ImportDeclaration | ExportDeclaration | StatementListItem[~Yield, +Await, ~Return]`; 16.2.2 `ImportDeclaration : import ImportClause FromClause WithClauseopt ;`; 16.2.1.7.3.1 `InitializeEnvironment` binds each import from `module.[[ImportEntries]]` via `CreateImportBinding(...)`, and `ModuleItem : ImportDeclaration` Runtime Semantics returns empty. 16.1 `Script : ScriptBodyopt`, `ScriptBody : StatementList[~Yield, ~Await, ~Return]`; 14.2 `StatementListItem : Statement | Declaration`.
- I: therefore an `ImportDeclaration` cannot occur in a Script, and `const {a,b} = <expr>` is a `LexicalDeclaration` statement form that has no `[[ImportEntries]]`, creates no import binding, and reads properties from the runtime value once, at the declaration's evaluation.

## Proposed SOURCES.md row (contract v1, 11 columns)

Id `S018` proposed (next free if sibling rows S016/S017 for the Node pages land; renumber otherwise). Status `queued`, matching those rows: opened, not yet cited by an admitted entry.

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S018 | ECMAScript® 2027 Language Specification (Draft ECMA-262 / October 16, 2026) — https://tc39.es/ecma262/ | spec | A (only for this row's scope; not for CommonJS, `require`, exports, or package resolution) | language-level semantics: how a `const`/`var` binding pattern is initialized from its initializer value, and why an `ImportDeclaration` is a distinct syntactic form | `#sec-bindingevaluation` (14.3.1.3), `#sec-runtime-semantics-bindinginitialization` (8.6.2), `#sec-runtime-semantics-keyedbindinginitialization` (14.3.3.3), `#sec-imports` + `#sec-modules` (16.2.2/16.2) | A destructuring declaration evaluates its initializer to a value, then reads each listed property from that value with GetV (ordinary `[[Get]]`, prototype chain included); `ImportDeclaration` is a `ModuleItem` whose bindings come from `ImportEntries` at module instantiation, not from evaluating an expression. | queued | 2026-10-21 | on-release (draft h1 2026-10-16) | corpus/knowledge/commonjs-static-import-edges.md (drafted by ScribeEntryJs, unadmitted) |

## What the source does NOT state

- No `require`, `module.exports`, CommonJS, `package.json` or `main`: counts on the full single page are `module.exports` 0, `package.json` 0, `require(` 0; the 69 `require` tokens sampled are the English verb (e.g. "features require non-LIFO transitions"), none a call form. It cannot ground the object returned by `require('./x')`, the `main` mapping, or an export correspondence; those need S016/S017 plus an unopened `module.exports` anchor.
- It does not require destructuring to read own properties only: GetV is `ToObject(value).[[Get]]` and OrdinaryGet consults the prototype chain, so a missing own property does not imply an undefined or abrupt read.
- It defines no "import edge" and no relation between a property name and an export name; that naming is the static tool's representation, not spec language.
- It says nothing about static analyzability of the initializer: the pattern's names are syntactic; the value and its property presence are runtime.
- It does not make a destructured binding a live import binding: bindings are initialized once (`InitializeReferencedBinding`/`PutValue`), whereas imports use `CreateImportBinding` in `InitializeEnvironment`.
- No statement about bundlers, Electron, ASAR, or how a host defines `require`; the spec defines no such binding.

## Implication for the C04 entry (Q01/Q11)

- Groundable now: names come from the binding pattern and are read from the evaluated value at run time; `{rot13, checksum}` reads properties `rot13` and `checksum`; a rename would read the property key, not the local name.
- Not groundable from this row: that `require('./x')` returns the module's exports object, that package `main` is the file, or that a read property equals an export. S016 (folder/main) and S017 (`main`/`exports` precedence) do not cover exports-object semantics either; the Node `module.exports` section remains an unopened lead.
- Entry wording forced by this: "static inference: the destructured property names are read from the value returned by the call" plus a separate source or `Unknown` label for export correspondence; no "live import binding".
- Q11 derivation for the entry: print the ordered list at `id=sec-bindingevaluation` (five steps above), then `id=sec-runtime-semantics-keyedbindinginitialization` (name, lhs, `GetV(value, propertyName)`).

## Unknowns

- No commit id on the page; Last-Modified/ETag identify the served build, not source-tree content.
- Draft target moves: recheck on the 2027 edition release or any Last-Modified change; clause numbers (14.3.1.3, 14.3.3.3) may shift in the published edition.
- Whether the saved REA records' edge names are property keys or local names is outside this source's scope (the fixtures use shorthand, so the two coincide).

VERDICT: ECMA-262 opened (HTTP 200, Draft 2026-10-16) and grounds only the language half of C04 — `const {a,b}=expr` evaluates `expr` and reads `a,b` from its value via GetV, while `ImportDeclaration` is a separate ModuleItem form; it states nothing about `require`, exports correspondence, or package `main`, so those still need S016/S017 and an unopened `module.exports` anchor.
Installs: none.
