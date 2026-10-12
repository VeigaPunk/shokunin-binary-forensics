# pe-scope-sentinel — round 27

Evidence id: `ev_a524338e43a8a20a3fb0f018d46ef2fe06732e323bfb3ce98fd813bd223f50ef`  
operation: `inspect_pe_resources`

## git status --porcelain

```
 M .shokunin/revenger/LOG.md
?? .shokunin/revenger/corpus/fixtures/pe-r27/
?? .shokunin/revenger/corpus/live/runs/round-27/
?? .shokunin/revenger/corpus/verify_pe_resources.py
```

## git diff --stat

```
 .shokunin/revenger/LOG.md | 5 +++++
 1 file changed, 5 insertions(+)
```

## Dirty paths observed (flat list)

1. `.shokunin/revenger/LOG.md` (modified)
2. `.shokunin/revenger/corpus/fixtures/pe-r27/` (untracked)
3. `.shokunin/revenger/corpus/live/runs/round-27/` (untracked)
4. `.shokunin/revenger/corpus/verify_pe_resources.py` (untracked)

## Scope check

- All dirty paths are under `.shokunin/revenger/`.
- No `MANIFEST.json` dirty.
- No sibling lane books outside this tree.
- No domain source outside `.shokunin/revenger/`.

**Verdict: PASS** (scope confined to `.shokunin/revenger/`)
