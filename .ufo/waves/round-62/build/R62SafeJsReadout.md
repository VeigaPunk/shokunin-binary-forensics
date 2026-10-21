RESULT: COMPLETE

# R62 Safe JS readout

Axes: C1 coverage; untrusted-source handling.

## Finding

- Severity: Low / no present exploit observed in the bounded fixture set.
- Exploit path: none observed. An instruction-like string embedded in JS could only become a prompt-injection path if a reader elevated fixture text to authority; the readout below treats source and saved JSON as data and never follows target directives.
- Impact: none observed. No JavaScript, package entrypoint, producer, service, or external tool was imported or run.
- Smallest remediation: none for these frozen bytes. Keep this as a fail-closed recognizer for this exact simple binding form, not a general JavaScript tokenizer; keep source text untrusted. A block-commented line matching the regex could fool a generalized use, but no such comment exists in these inspected files.

## Frozen inputs and injection check

- Frozen revision: `a3498e25ad87bf756288812d0ea7c474b09433c7`.
- Extraction command: `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive a3498e25ad87bf756288812d0ea7c474b09433c7 | tar -x -C /fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62SafeJsReadout`; exit 0, no stdout.
- Read-only scan over `corpus/fixtures/js-r3/{index.js,transform.js,package.json}` and `js-r7-v2/{index.js,transform.js,package.json}`; pattern `(?i)(ignore|instruction|assistant|system|developer|prompt|secret|credential|token|exfiltrat|curl|wget|download|execute|run this)`: `No matches found.` Manual reads: js-r3 `index.js:1-7`, `transform.js:1-12`, `package.json:1`; js-r7-v2 `index.js:1-7`, `transform.js:1-12`, `package.json:1` contain ordinary fixture code/metadata, no prompt directive.
- Frozen `README.md:33` has C04 `uncovered`. No README or held-state edit is proposed; no admission claimed.

## Bounded static readout

Scratch artifact: `/fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62SafeJsReadout/js_readout.py`. It imports only `pathlib`, `json`, `re`; fixed fixture/record paths are checked to stay under this scratch root and reject symlink components. It reads JS as UTF-8 text, `fullmatch`es one single-line `const { identifiers } = require('literal');`, validates identifiers, and parses saved records with `json.loads`. It never evaluates source or follows paths from JSON. The recognizer intentionally does not support aliases, rest/nested/computed/multiline bindings or arbitrary JavaScript; do not generalize its result.

Command (cwd `/`): `python3 -B /fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62SafeJsReadout/js_readout.py`

Observed output:

```text
v1 source_line=1 specifier='./transform' names=['checksum', 'rot13'] ascii=True
v1 imports=3 named=2 unnamed=1 graph_names=['checksum', 'rot13'] names_match=True
v1 edge name='rot13' local='rot13' specifier='./transform' resolved='transform.js' span=1:6-1:50 source_slice="{ rot13, checksum } = require('./transform')"
v1 edge name=None local=None specifier='./transform' resolved='transform.js' span=1:28-1:50 source_slice="require('./transform')"
v1 edge name='checksum' local='checksum' specifier='./transform' resolved='transform.js' span=1:6-1:50 source_slice="{ rot13, checksum } = require('./transform')"
v2 source_line=1 specifier='./transform' names=['rot13'] ascii=True
v2 imports=2 named=1 unnamed=1 graph_names=['rot13'] names_match=True
v2 edge name=None local=None specifier='./transform' resolved='transform.js' span=1:18-1:40 source_slice="require('./transform')"
v2 edge name='rot13' local='rot13' specifier='./transform' resolved='transform.js' span=1:6-1:40 source_slice="{ rot13 } = require('./transform')"
```

This safely exposes the saved source-range fields omitted from the old CommonJS reproduction: each named record's source slice and the corresponding unnamed require-call slice are printed from the frozen fixture and saved JSON. The `names_match=True` results are equality checks only, not completeness or admission evidence. No new quality gate, producer capability, runtime, Electron-role, or authenticity claim is made.

Installs/updates: none.
