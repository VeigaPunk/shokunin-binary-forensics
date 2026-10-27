# CoreS060Review — S060 (frida/frida) source review, round-72 wave 1

Seat: reviewer, leaf member (no subagents). Scope: S060 row, its linked entry text, and the pinned frida/frida README only. Read-only throughout; sole write is this file. No git/jj mutation, no scratch created, no installs (none needed).

**Judgment: SUPPORT** — the S060 row and its cited entry text are accurate to the pinned source, every row field the frozen counter consumes is correct, and nothing in the S060 chain claims live-target use, installation, or a tested capability.

## Frozen-claim identity

- `reports/round-72/measure.py` sha256 = `9559b10d49690c4247a4100516bef94c8607fcd198dd77d274c770bdb6df48b3` — matches the freeze in `claims.md`. Predicate read: S060 counts toward `C15_TOOL_ROWS` iff its 11-cell registry row has `tool`/`A`/`mined`/entry-path-in-used-by AND the entry text contains `\bS060\b`.

## Row fields (corpus/SOURCES.md:74)

Checked with the counter's own parsing (`strip('|').split('|')`, 11 cells):

- cells: `S060` / `Frida — https://github.com/frida/frida` / `tool` / `A` / scope / anchor / note / `mined` / `2026-10-27` / `on-release` / `corpus/knowledge/round-72-tool-landscape.md`.
- `cells[2]="tool"`, `cells[3]="A"`, `cells[7]="mined"`, `cells[10]` contains the entry path — all four counter conditions hold. Tier A is appropriate: first-party project README.
- Uniqueness: S060 is the only row naming frida/frida; no sibling-row collision.

## Quote / anchor verification against the pinned source

- Fetched `https://raw.githubusercontent.com/frida/frida/e598d053f4154fa78a26bb60d4f6cbc407ea387c/README.md` (200; 1,931 B; sha256 `8478d48f61310d01be76702014de292852260f32cda695a64f8f86ab110b655b`). A raw fetch at an unknown SHA would 404, so the pinned commit exists in frida/frida.
- Quote `"Dynamic instrumentation toolkit for developers, reverse-engineers, and security researchers."` is present verbatim in the README introduction (first prose paragraph after `# Frida`), modulo one line-wrap fold: the file reads `…and security\nresearchers.` — registry/lesson join with a space; rendered sentence unchanged. Non-material.
- Commit metadata via the GitHub commit page (REST API rate-limited, so HTML + raw fetch): title `Revise certificate identifiers in README · frida/frida@e598d05`, `committedDate 2026-03-23T15:45:43+01:00` — predates the row's `accessed 2026-10-27`, so the access date is coherent. The row pins a commit without claiming it is the latest revision; current `master` README's introduction is byte-identical anyway (drift check this run).
- Lesson Gate (`corpus/lessons/round-72.md:19`): located quote matches the registry quote exactly, 9 words ≤ 25, decision `ADMIT, tier A for declared dynamic-instrumentation purpose only; not a run or permission to use a target.` — scope bounds preserved at admit time.

## Entry text (corpus/knowledge/round-72-tool-landscape.md:28)

- Citation form: `Frida S060` in the table row "Need process instrumentation or debugging" — contextual (adjacent to the project name), not a bare ID; satisfies the frozen counter's `\bS060\b` citation test. (The entry's top-of-file `source:` headers cover the REA rows only; tool rows are cited in the table body — accepted by the frozen predicate, noted here for form.)
- Stated instrumentation scope: `Frida describes dynamic instrumentation.` — accurate minimal paraphrase of the README's own one-line scope statement; nothing more is attributed. Boundary column: `This round does not run any target. Any later dynamic work needs explicit authorization and a bounded local artifact lifecycle…`. Entry Scope header: `Dynamic-process and traffic tools are named only to identify their documented scope; none was run.` Entry Unknown: `no tool was installed or run`.
- Registry note: `any use remains limited to an explicitly authorized local artifact/lifecycle, not a live target`.

## No live-target use or tested capability claimed

README's total disclosed scope is the intro sentence plus two install paths (prebuilt binaries from the GitHub releases page; build-your-own) — which is exactly what the row's scope cell claims ("declared dynamic instrumentation purpose and published release-binary role; no target activity or host installation"). Across the whole S060 chain (SOURCES row, entry, lesson Gate, claims.md) there is no execution, installation, target activity, or capability-on-host claim. The only dynamic-instrumentation statement is the project's own self-description, attributed as such.

## Committed-bytes status (read-only git)

- `git status --porcelain` shows only untracked `.ufo/waves/round-72/w1*`; `corpus/SOURCES.md` and the entry are clean, and `git show HEAD:…` finds the frida row (1 hit) and the `S060` citation (1 hit) in committed bytes at `99911e8` (the curation commit atop freeze commit `1c5b748e`). The counter's final-tree target is reachable with this row as committed.

## Uncertainty / limits

- GitHub REST API was rate-limited; commit existence/date rests on the rendered commit page plus the SHA-addressed raw fetch (both independent, mutually consistent).
- The pinned commit's full ancestry in `master` was not separately verified; its existence and README content at that SHA are verified, which is all the row asserts.
- Historical ID note: round-67/69 lane lessons mention a different `S060` (a crifan jadx quarantine row in the shokuknow absent-defect register). Round-72's S060 is a freshly appended row in this lane's registry; the old references are historical records and no contamination exists — noted only to prevent confusion in later audits.
- Nothing here judges the C15 README row status, other rows, or the counter run; those are other seats' items.

**Verdict: SUPPORT — no revision required for S060.**
