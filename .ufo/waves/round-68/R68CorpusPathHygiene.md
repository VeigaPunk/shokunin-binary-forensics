DEFECT — `corpus/snapshots/ResourceTypes.h` is tracked, not ignored, 84.2 KiB (inside the 1 MiB directory-commit rule) and byte-exact, but the new `corpus/snapshots/` directory (and the new top-level `corpus/derive_axml_anchors.py`) are named nowhere in the `corpus/README.md` index, which is the only placement authority over `corpus/`; `QUALITY.md` and `PROVINCE.md` impose no directory whitelist, so no rule is broken — the index is simply out of date by one directory and one script.

Seat: `L1Revenger68.R68CorpusPathHygiene` (read-only; nothing edited). Base `f165908`, tip `4232235723cf8d4731a1e7e78ca098b8af953a57`. No tool installs or upgrades were made; no repo/`git`/`jj` mutation was run — the only writes outside this report were a scratch `git archive` tree under `/tmp`, removed after use.

## 1. Every path this round added or changed under `corpus/`

```
$ git -C /home/vgpnk/Projects/shokunin/revenger-shokunin diff --name-status f165908 HEAD -- corpus/
M	corpus/SOURCES.md
M	corpus/check_embedded_outputs.py
A	corpus/derive_axml_anchors.py
A	corpus/knowledge/round-68-apk-axml-byte-evidence.md
A	corpus/snapshots/ResourceTypes.h
```
Identical against `HEAD~1` (`git diff --name-status HEAD~1 HEAD -- corpus/`), so all five belong to the single build commit `4232235`. Three additions, two modifications; `corpus/fixtures/`, `corpus/live/`, `corpus/lessons/` and every `corpus/verify_*.py` are untouched (claims.md:170-172 asserts exactly this and it holds).

Top-level `corpus/` surface before → after (`git ls-tree --name-only f165908 corpus/` vs `HEAD corpus/`): one new directory `corpus/snapshots` and one new file `corpus/derive_axml_anchors.py`; the other 18 top-level entries are unchanged.

## 2. Is `corpus/snapshots/ResourceTypes.h` tracked? — YES

```
$ git -C .../revenger-shokunin ls-files corpus/snapshots/
corpus/snapshots/ResourceTypes.h
$ git ls-tree -l HEAD corpus/snapshots/
100644 blob c2648909386ca3722c8a3bff98708505ab4f27a2   86255	corpus/snapshots/ResourceTypes.h
$ git status --porcelain corpus/
(no output — no untracked or modified corpus path; the working tree equals the commit)
```

## 3. Does `check-ignore` ignore it? — NO

```
$ git -C .../revenger-shokunin check-ignore -v corpus/snapshots/ResourceTypes.h
(no output)
exit=1
```
Exit 1 with no output is git's "not ignored" result. Every ignore source in the lane was enumerated: `.gitignore` (repo root) contains one line, `.ufo/interactive-sessions/`; `corpus/.gitignore` is empty (0 bytes); `.git/info/exclude` holds only the stock commented template (`# *.[oa]`, `# *~`). No `.gitattributes` exists anywhere in the lane (`find . -name .gitattributes -not -path './.git/*' -maxdepth 3` → no output), so no `text`/`eol`/filter attribute can rewrite the snapshot bytes on checkout — relevant because the file's value is its exact bytes.

## 4. Size versus the 1 MiB directory-commit rule — COMPLIANT

Rule text, `/home/vgpnk/Projects/shokunin/.ufo/prompts/tameshi-round-18.md:307-308` (same sentence in the other round-17/18/19/20 fleet prompts):

> "A named directory commits like `git add <dir>` (ignored content stays out; new files over 1 MiB inside it are skipped with a warning — name them as files)."

Observed size: `stat -c '%s %n' corpus/snapshots/ResourceTypes.h` → `86255 corpus/snapshots/ResourceTypes.h`, i.e. 86,255 B = 84.23 KiB, **12.2× below** 1,048,576 B, and far below the 10 MiB `--allow-large` threshold. The rule therefore never fired, and the commit proves it empirically:

```
$ T=$(mktemp -d); git archive HEAD corpus | tar -x -C "$T"; ls -l "$T"/corpus/snapshots/
-rw-r--r-- 1 vgpnk vgpnk 86255 ... ResourceTypes.h
```
The blob is present in the committed tree, not merely in the working directory. Total corpus growth this round is 86,255 + 33,442 (entry) + 3,667 (script) ≈ 120 KiB, so no repo-size concern either.

## 5. Bonus check — the copy is byte-exact and makes the recheck self-contained

```
$ sha256sum corpus/snapshots/ResourceTypes.h .ufo/waves/round-65/source-snapshots/ResourceTypes.h
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  corpus/snapshots/ResourceTypes.h
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  .ufo/waves/round-65/source-snapshots/ResourceTypes.h
```
`corpus/derive_axml_anchors.py:32,74` resolves the snapshot as `Path(__file__).resolve().parent / "snapshots/ResourceTypes.h"` and hard-fails on a digest mismatch (`:79-80`), so it does not depend on cwd. Run against the archived commit with `cwd=/`: exit 0, 17 lines, first line `sha256 56b88bc4… ResourceTypes.h`, `enum RES_XML_START_NAMESPACE_TYPE : 245` (the M40/M44 anchor this round repairs). The same run with `cwd=<tree>` gives a byte-identical stdout (`sha256 b02cfe54df5af9e8ca16c61c3d4c719ebb18ac3e9d1cf23b48686628bf3e0831`, 17 lines). So the copy is a deliberate, working self-containment measure, not a stray duplicate: the `.ufo` copy is also tracked (`git ls-files .ufo/waves/round-65/source-snapshots/` lists it), and the corpus copy costs 84 KiB to make the S046 recheck runnable from the `git archive corpus` trees the counter uses. Only one file of this size exists under `corpus/` (`find corpus -type f -size 86255c` → the snapshot alone), so there is no hidden second copy.

## 6. Does `corpus/README.md` index need to mention the new path? — YES, and it currently does not

`corpus/README.md:3` states the file's scope: "What this corpus holds, which province surfaces its knowledge covers, and the frontier it is working toward." Its `## Index` (`:7-17`) is a one-bullet-per-top-level-surface enumeration. Quoting the three bullets the brief names, verbatim:

> `- `knowledge/` — admitted domain entries (the map below names each one); also`
> `  retains clearly marked rejected candidates (each carries an`
> `  `admission-status: rejected` header), which are evidence, not admitted knowledge.`  (`:11-13`)

> `- `fixtures/` — authored known-truth inputs (byte-oracle fixtures; `fixtures/REPLAY.md`).`  (`:15`)

> `- `verify_*.py` — saved-ledger replay verifiers (`--self-test`); census command in `SCORECARD.md` (C).`  (`:17`)

Three consequences:

1. **`snapshots/` has no bullet at all.** `grep -n 'snapshots' corpus/README.md` → exit 1, no match. Every other top-level tracked surface has one (`:9` `QUALITY.md`, `:10` `SOURCES.md`, `:11` `knowledge/`, `:14` `lessons/`, `:15` `fixtures/`, `:16` `live/runs/`, `:17` `verify_*.py`), so the omission is a break in the index's own pattern, not a stylistic choice.
2. **`derive_axml_anchors.py` is not covered either.** It does not match `verify_*.py` (`:17`), so nothing in the index names it — yet the C05 candidate's `recheck:` (`corpus/knowledge/round-68-apk-axml-byte-evidence.md:7`) and S046 (`corpus/SOURCES.md:61`) both rest on it. `grep -n 'derive_axml' corpus/README.md` → exit 1.
3. **The placement sentence in the coverage legend does not admit the new directory.** `corpus/README.md:25-26`: "Work evidence is not knowledge: fixture and run records stay in `fixtures/` and `live/runs/`." A third-party source snapshot is neither a fixture nor a run record, so under the README's own wording `snapshots/` is placed outside the rule that describes where non-knowledge bytes may live. This is the concrete defect, not just a missing line.

Pre-existing instance of the same class (context, not this round's fault): `corpus/check_embedded_outputs.py` was already tracked at base `f165908` (`git ls-tree f165908 corpus/check_embedded_outputs.py` → blob `89cc0b49…`) and is likewise absent from the index (`git show f165908:corpus/README.md | grep -c check_embedded` → `0`). The index has been lagging one path since round 67; round 68 adds two more.

## 7. Does `corpus/QUALITY.md` or `PROVINCE.md` constrain what may live under `corpus/`? — NO directory whitelist exists

`corpus/QUALITY.md:1-4`:
> "# QUALITY — revenger's admission bar"
> "What a `corpus/knowledge/` entry must show before it is admitted. Each criterion cites the mistake class that produced it …"

Its criteria (Q01-Q13, `:13-25`) and admission procedure (`:29-33`) speak only to entries under `corpus/knowledge/`; nothing there enumerates or forbids other `corpus/` paths. The one general requirement that does reach the snapshot is Q09 (`:21`), "Saved records stay byte-preserved", which the copy satisfies (sha256 equality above; no `.gitattributes`, no annotation added to the `.h` — correct, since prepending a provenance comment would have destroyed the pin).

`PROVINCE.md:25-29`:
> "Writes only this `revenger-shokunin/` repository under the current interactive dispatch. Reports, continuation evidence and L0 requests stay in its own `.ufo/`; the fleet integrator alone copies them to shared ledgers/report paths. Domain source checkouts, shared fleet state and sibling repositories remain read-only."

That constrains the repository and the read-only substrates, not sub-directories of `corpus/`; `corpus/snapshots/ResourceTypes.h` is a copy inside the lane's own repo (the upstream checkout was never touched), and `PROVINCE.md:9-17` already treats host/domain sources as read-only inputs, not as things that must live only in `.ufo/`. So: no constraint violated, and none established — which is precisely why the README index is the binding index of record and why leaving `snapshots/` out of it is the defect.

## 8. Operability: the fix is counter-neutral

`reports/round-68/measure.py:34-41` reads `corpus/README.md` only to select `^\| C[0-9]+ ` table rows and to print `K_HELD`, `K_ROW C05/C07`, `K_HELD_BACKED`. A new `## Index` bullet cannot match that regex, so adding one cannot move any of `K_HELD`, `K_ROW C05`, `K_ROW C07` or `K_HELD_BACKED` (this seat did not run the counter; the claim is regex-scoped, read at `measure.py:35-41`). The verifier census is `sorted((TREE / "corpus").glob("verify_*.py"))` (`:496`, and `SCORECARD.md:36`, `SKILL.md:367`), so `derive_axml_anchors.py` correctly stays out of the frozen `HOLD_REPLAY=10/10` denominator — the same deliberate exclusion recorded for `check_embedded_outputs.py` at `SKILL.md:273`. No other counter path globs `corpus/` recursively (only `corpus/live/runs/**/*.json`, `measure.py:92,120`).

## 9. Exact fix (not applied — read-only seat)

Edit `corpus/README.md` only. Two additions, no deletion, no reordering:

1. After the `live/runs/` bullet (`:16`) and before `verify_*.py` (`:17`), insert:

```
- `snapshots/` — byte-exact copies of pinned source snapshots that a re-derivable
  command reads (`snapshots/ResourceTypes.h`, sha256 `56b88bc4…c56f`, byte-identical
  to `.ufo/waves/round-65/source-snapshots/ResourceTypes.h`; S046). Stored
  unmodified, never annotated: the digest is the identity (Q09).
```

2. Replace the `verify_*.py` bullet (`:17`) with the same sentence plus one line, so the new script is named without joining the frozen census:

```
- `verify_*.py` — saved-ledger replay verifiers (`--self-test`); census command in `SCORECARD.md` (C).
- `derive_axml_anchors.py` — AXML anchor derivation (`python3 -B corpus/derive_axml_anchors.py`;
  exit 2 on a missing/ambiguous symbol or snapshot-digest drift); outside the `verify_*`
  replay family, like `check_embedded_outputs.py`.
```

3. Optional, closes the round-67 instance in the same edit: append to the same paragraph a clause naming `check_embedded_outputs.py` as the registered embedded-output gate (`SKILL.md` §Gate registry).

Do **not** add a provenance banner to `corpus/snapshots/ResourceTypes.h` itself: the file's pin is its sha256, and any byte edit fails `derive_axml_anchors.py:79-80` and voids S046.

## 10. Minor, non-operative finding

`reports/round-68/claims.md:173` says "the only new corpus path is `corpus/snapshots/`". Measured, the round adds three `corpus/` paths (`snapshots/ResourceTypes.h`, `derive_axml_anchors.py`, the C05 candidate) plus two modifications (§1). The sentence sits inside the void conditions, whose operative clause is "Changed `corpus/live` or `corpus/fixtures` bytes" — and that clause is satisfied correctly (both trees byte-frozen), so there is no adjudication effect. Recorded because claims.md is frozen and cannot be repaired post-registration; the parenthetical should have read "the only new non-frozen corpus path".

## Verdict

**DEFECT** — one exact fix: add the `snapshots/` bullet and the `derive_axml_anchors.py` bullet to `corpus/README.md` `## Index` as in §9. Everything else is HYGIENE-CLEAN: tracked, not ignored, 84.2 KiB (1 MiB rule not triggered, empirically in the commit), byte-exact with the pinned snapshot, no `.gitattributes`/eol hazard, no recursive counter glob affected, and no `QUALITY.md`/`PROVINCE.md` constraint violated.

Risks: none to the frozen counter (fix is a bullet-only README edit; §8). Blocker for anyone applying the fix: `corpus/README.md` is inside the frozen counter's input set, so the edit must land as a text-only change and be re-counted by the parent, not by a seat; the C05 row must stay `uncovered` (`corpus/README.md:34`) — unrelated to this edit and owned by `R68ReadmeFlipCheck`.
